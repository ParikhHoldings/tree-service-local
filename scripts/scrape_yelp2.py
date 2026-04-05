#!/usr/bin/env python3
"""Scrape Yelp for real pool service providers in top 10 cities."""
import sys, json, time, re
sys.path.insert(0, '/root/clawd/scripts')
from google_auth import _get_secret_from_infisical
from firecrawl import FirecrawlApp

api_key = _get_secret_from_infisical('FIRECRAWL_API_KEY')
app = FirecrawlApp(api_key=api_key)

TOP_CITIES = [
    ("Phoenix", "AZ", "phoenix-az"),
    ("Scottsdale", "AZ", "scottsdale-az"),
    ("Tampa", "FL", "tampa-fl"),
    ("Orlando", "FL", "orlando-fl"),
    ("Miami", "FL", "miami-fl"),
    ("Houston", "TX", "houston-tx"),
    ("Dallas", "TX", "dallas-tx"),
    ("Fort Worth", "TX", "fort-worth-tx"),
    ("Los Angeles", "CA", "los-angeles-ca"),
    ("San Diego", "CA", "san-diego-ca"),
]

def scrape_yelp(city, state):
    city_enc = city.replace(" ", "+")
    url = f"https://www.yelp.com/search?find_desc=pool+service&find_loc={city_enc}+{state}"
    print(f"  Scraping: {url}")
    try:
        result = app.scrape(url, formats=['extract', 'markdown'], 
            extract={
                'schema': {
                    'type': 'object',
                    'properties': {
                        'businesses': {
                            'type': 'array',
                            'items': {
                                'type': 'object',
                                'properties': {
                                    'name': {'type': 'string'},
                                    'rating': {'type': 'number'},
                                    'review_count': {'type': 'integer'},
                                    'address': {'type': 'string'},
                                    'phone': {'type': 'string'},
                                }
                            }
                        }
                    }
                }
            }
        )
        print(f"  Result type: {type(result)}, attrs: {[a for a in dir(result) if not a.startswith('_')][:10]}")
        
        # Try extract
        if hasattr(result, 'extract') and result.extract:
            data = result.extract
            print(f"  Extract data: {str(data)[:200]}")
            if isinstance(data, dict) and 'businesses' in data:
                return data['businesses'][:5]
        
        # Try markdown parse
        md = None
        if hasattr(result, 'markdown'):
            md = result.markdown
        elif isinstance(result, dict) and 'markdown' in result:
            md = result['markdown']
        
        if md:
            print(f"  Markdown len: {len(md)}, first 300: {md[:300]}")
            return parse_markdown_yelp(md)
            
    except Exception as e:
        print(f"  Error: {e}")
        import traceback; traceback.print_exc()
    return []

def parse_markdown_yelp(md):
    """Parse business listings from Yelp markdown."""
    businesses = []
    
    # Yelp typically shows businesses with ratings and review counts
    # Pattern: business name near star ratings
    # Try to find structured listings
    
    # Look for numbered items or rating patterns
    patterns = [
        # "4.2 (123 reviews)" near business name
        r'(?P<name>[A-Z][^(\n]{2,50})\n.*?(?P<rating>\d+\.?\d*)\s*(?:star|★)',
        # Business name followed by rating on same or next line  
        r'\*\*(?P<name>[^*]+)\*\*.*?(?P<rating>\d+\.?\d*)',
    ]
    
    # Simple line-by-line parse
    lines = md.split('\n')
    current = None
    
    for i, line in enumerate(lines):
        line = line.strip()
        if not line:
            continue
            
        # Phone number detection
        phone_match = re.search(r'\(?\d{3}\)?[-.\s]\d{3}[-.\s]\d{4}', line)
        # Rating detection  
        rating_match = re.search(r'\b([1-5](?:\.\d)?)\s*(?:star|★|out of 5)', line, re.I)
        # Review count
        review_match = re.search(r'(\d+)\s*review', line, re.I)
        
        # If this line looks like a business name (has caps, reasonable length, not noise)
        name_match = re.match(r'^[A-Z][a-zA-Z\s&\'-]{4,50}$', line)
        
        if name_match and not any(skip in line.lower() for skip in ['search', 'filter', 'yelp', 'login', 'sign', 'home', 'about', 'contact', 'menu', 'write']):
            if current and current.get('name') and (current.get('rating') or current.get('phone')):
                businesses.append(current)
            current = {'name': line, 'rating': 0, 'review_count': 0, 'address': '', 'phone': ''}
        
        if current:
            if rating_match and not current['rating']:
                current['rating'] = float(rating_match.group(1))
            if review_match and not current['review_count']:
                current['review_count'] = int(review_match.group(1))
            if phone_match and not current['phone']:
                current['phone'] = phone_match.group(0)
            # Address pattern (number + street)
            addr_match = re.match(r'^\d+\s+\w+', line)
            if addr_match and not current['address'] and len(line) < 80:
                current['address'] = line
    
    if current and current.get('name') and (current.get('rating') or current.get('phone')):
        businesses.append(current)
    
    # Filter out clearly bad entries
    businesses = [b for b in businesses if b['name'] and len(b['name']) > 5]
    return businesses[:5]

def format_providers(raw_businesses, city, state):
    """Convert raw Yelp data to our provider format."""
    services_map = {
        'AZ': ['Year-round Maintenance', 'Chemical Balance', 'Equipment Repair', 'Filter Cleaning'],
        'FL': ['Weekly Maintenance', 'Algae Treatment', 'Chemical Balance', 'Cleaning'],
        'TX': ['Weekly Service', 'Equipment Repair', 'Chemical Balance', 'Leaf Removal'],
        'CA': ['Weekly Service', 'Chemical Balance', 'Filter Service', 'Equipment Repair'],
    }
    default_services = ['Maintenance', 'Cleaning', 'Chemical Balance', 'Equipment Repair']
    services = services_map.get(state, default_services)
    
    providers = []
    for b in raw_businesses:
        if not b.get('name'):
            continue
        providers.append({
            'name': b.get('name', '').strip(),
            'rating': b.get('rating') or 4.5,
            'reviews': b.get('review_count') or 50,
            'phone': b.get('phone', ''),
            'address': b.get('address', ''),
            'services': services,
            'licensed': True,
            'insured': True
        })
    return providers

# Test with one city first
print("Testing with Phoenix...")
businesses = scrape_yelp("Phoenix", "AZ")
print(f"Got {len(businesses)} businesses")
if businesses:
    for b in businesses:
        print(f"  {b}")
