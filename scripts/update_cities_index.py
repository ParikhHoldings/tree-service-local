#!/usr/bin/env python3
"""Rebuild cities-index.json from all city JSON files."""
import json, os, glob

DATA_DIR = '/root/clawd/projects/portfolio/programmatic/service-city-seo/site/data/cities'
INDEX_PATH = os.path.join(DATA_DIR, 'cities-index.json')

cities = []
for filepath in sorted(glob.glob(os.path.join(DATA_DIR, '*.json'))):
    filename = os.path.basename(filepath)
    if filename in ('cities-index.json',):
        continue
    
    with open(filepath) as f:
        data = json.load(f)
    
    cities.append({
        "slug": data['slug'],
        "city": data['city'],
        "state": data['state'],
        "stateAbbr": data['stateAbbr']
    })

# Sort by state then city
cities.sort(key=lambda x: (x['stateAbbr'], x['city']))

with open(INDEX_PATH, 'w') as f:
    json.dump(cities, f, indent=2)

print(f"Updated cities-index.json with {len(cities)} cities:")
for c in cities:
    print(f"  {c['city']}, {c['stateAbbr']} ({c['slug']})")
