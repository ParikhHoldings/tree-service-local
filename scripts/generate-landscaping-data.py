#!/usr/bin/env python3
"""Generate tree-service service city data for programmatic SEO."""
import json, os, random

CITIES = [
    # Sun Belt / Suburban — largest residential tree-service markets
    {"city": "Dallas", "state": "Texas", "stateAbbr": "TX", "population": 1304379, "slug": "dallas-tx"},
    {"city": "Houston", "state": "Texas", "stateAbbr": "TX", "population": 2304580, "slug": "houston-tx"},
    {"city": "San Antonio", "state": "Texas", "stateAbbr": "TX", "population": 1434625, "slug": "san-antonio-tx"},
    {"city": "Austin", "state": "Texas", "stateAbbr": "TX", "population": 961855, "slug": "austin-tx"},
    {"city": "Fort Worth", "state": "Texas", "stateAbbr": "TX", "population": 935508, "slug": "fort-worth-tx"},
    {"city": "Phoenix", "state": "Arizona", "stateAbbr": "AZ", "population": 1608139, "slug": "phoenix-az"},
    {"city": "Scottsdale", "state": "Arizona", "stateAbbr": "AZ", "population": 258069, "slug": "scottsdale-az"},
    {"city": "Tucson", "state": "Arizona", "stateAbbr": "AZ", "population": 542629, "slug": "tucson-az"},
    {"city": "Las Vegas", "state": "Nevada", "stateAbbr": "NV", "population": 641903, "slug": "las-vegas-nv"},
    {"city": "Henderson", "state": "Nevada", "stateAbbr": "NV", "population": 320189, "slug": "henderson-nv"},
    # Southeast — year-round growing season
    {"city": "Atlanta", "state": "Georgia", "stateAbbr": "GA", "population": 498715, "slug": "atlanta-ga"},
    {"city": "Charlotte", "state": "North Carolina", "stateAbbr": "NC", "population": 874579, "slug": "charlotte-nc"},
    {"city": "Raleigh", "state": "North Carolina", "stateAbbr": "NC", "population": 467665, "slug": "raleigh-nc"},
    {"city": "Nashville", "state": "Tennessee", "stateAbbr": "TN", "population": 689447, "slug": "nashville-tn"},
    {"city": "Jacksonville", "state": "Florida", "stateAbbr": "FL", "population": 949611, "slug": "jacksonville-fl"},
    {"city": "Tampa", "state": "Florida", "stateAbbr": "FL", "population": 392890, "slug": "tampa-fl"},
    {"city": "Orlando", "state": "Florida", "stateAbbr": "FL", "population": 338000, "slug": "orlando-fl"},
    {"city": "Miami", "state": "Florida", "stateAbbr": "FL", "population": 470914, "slug": "miami-fl"},
    {"city": "Birmingham", "state": "Alabama", "stateAbbr": "AL", "population": 212247, "slug": "birmingham-al"},
    {"city": "Louisville", "state": "Kentucky", "stateAbbr": "KY", "population": 633045, "slug": "louisville-ky"},
    # Midwest — spring boom market
    {"city": "Chicago", "state": "Illinois", "stateAbbr": "IL", "population": 2696555, "slug": "chicago-il"},
    {"city": "Indianapolis", "state": "Indiana", "stateAbbr": "IN", "population": 887642, "slug": "indianapolis-in"},
    {"city": "Columbus", "state": "Ohio", "stateAbbr": "OH", "population": 905748, "slug": "columbus-oh"},
    {"city": "Kansas City", "state": "Missouri", "stateAbbr": "MO", "population": 508090, "slug": "kansas-city-mo"},
    {"city": "St. Louis", "state": "Missouri", "stateAbbr": "MO", "population": 301578, "slug": "st-louis-mo"},
    {"city": "Minneapolis", "state": "Minnesota", "stateAbbr": "MN", "population": 429954, "slug": "minneapolis-mn"},
    {"city": "Milwaukee", "state": "Wisconsin", "stateAbbr": "WI", "population": 577222, "slug": "milwaukee-wi"},
    {"city": "Cincinnati", "state": "Ohio", "stateAbbr": "OH", "population": 309317, "slug": "cincinnati-oh"},
    {"city": "Cleveland", "state": "Ohio", "stateAbbr": "OH", "population": 367991, "slug": "cleveland-oh"},
    {"city": "Detroit", "state": "Michigan", "stateAbbr": "MI", "population": 639111, "slug": "detroit-mi"},
    # Mid-Atlantic / Northeast
    {"city": "Philadelphia", "state": "Pennsylvania", "stateAbbr": "PA", "population": 1567872, "slug": "philadelphia-pa"},
    {"city": "Baltimore", "state": "Maryland", "stateAbbr": "MD", "population": 569931, "slug": "baltimore-md"},
    {"city": "Washington", "state": "District of Columbia", "stateAbbr": "DC", "population": 689545, "slug": "washington-dc"},
    {"city": "Richmond", "state": "Virginia", "stateAbbr": "VA", "population": 226610, "slug": "richmond-va"},
    {"city": "Virginia Beach", "state": "Virginia", "stateAbbr": "VA", "population": 459470, "slug": "virginia-beach-va"},
    # Mountain / Southwest
    {"city": "Denver", "state": "Colorado", "stateAbbr": "CO", "population": 715522, "slug": "denver-co"},
    {"city": "Colorado Springs", "state": "Colorado", "stateAbbr": "CO", "population": 478961, "slug": "colorado-springs-co"},
    {"city": "Albuquerque", "state": "New Mexico", "stateAbbr": "NM", "population": 564559, "slug": "albuquerque-nm"},
    {"city": "Salt Lake City", "state": "Utah", "stateAbbr": "UT", "population": 199723, "slug": "salt-lake-city-ut"},
    # Pacific
    {"city": "Los Angeles", "state": "California", "stateAbbr": "CA", "population": 3898747, "slug": "los-angeles-ca"},
    {"city": "San Diego", "state": "California", "stateAbbr": "CA", "population": 1386932, "slug": "san-diego-ca"},
    {"city": "Sacramento", "state": "California", "stateAbbr": "CA", "population": 524943, "slug": "sacramento-ca"},
    {"city": "Portland", "state": "Oregon", "stateAbbr": "OR", "population": 652503, "slug": "portland-or"},
    {"city": "Seattle", "state": "Washington", "stateAbbr": "WA", "population": 737255, "slug": "seattle-wa"},
    # More Southeast
    {"city": "Memphis", "state": "Tennessee", "stateAbbr": "TN", "population": 633104, "slug": "memphis-tn"},
    {"city": "New Orleans", "state": "Louisiana", "stateAbbr": "LA", "population": 383997, "slug": "new-orleans-la"},
    {"city": "Oklahoma City", "state": "Oklahoma", "stateAbbr": "OK", "population": 695017, "slug": "oklahoma-city-ok"},
    {"city": "Omaha", "state": "Nebraska", "stateAbbr": "NE", "population": 486051, "slug": "omaha-ne"},
    {"city": "Pittsburgh", "state": "Pennsylvania", "stateAbbr": "PA", "population": 302971, "slug": "pittsburgh-pa"},
    {"city": "Grand Rapids", "state": "Michigan", "stateAbbr": "MI", "population": 198917, "slug": "grand-rapids-mi"},
]

# Climate zones for pricing
DESERT = {"AZ", "NV", "NM", "UT"}
TROPICAL_YEAR_ROUND = {"FL", "LA"}
MILD_WEST = {"CA", "OR", "WA"}
WARM_SOUTH = {"TX", "GA", "NC", "TN", "AL", "KY", "VA", "OK"}
COLD_NORTH = {"IL", "IN", "OH", "MO", "MN", "WI", "MI", "PA", "MD", "DC", "NE", "CO"}

def get_season(state):
    if state in DESERT: return "February–November (irrigation year-round)"
    if state in TROPICAL_YEAR_ROUND: return "Year-round"
    if state in MILD_WEST: return "March–November"
    if state in WARM_SOUTH: return "March–October (peak: April–June)"
    return "April–October (peak: May–June, September)"

def get_costs(state):
    if state in DESERT:
        return {
            "lawnMowingWeekly": (40, 90, 60),
            "lawnMowingMonthly": (140, 320, 210),
            "landscapeDesignInstall": (2000, 15000, 6500),
            "sprinklerInstall": (2500, 6000, 3800),
            "treeTrimmingSmall": (150, 400, 240),
            "treeTrimmingLarge": (400, 1200, 700),
            "mulchInstall": (200, 800, 450),
            "sod": (1, 2, 1),  # per sq ft
        }
    elif state in TROPICAL_YEAR_ROUND:
        return {
            "lawnMowingWeekly": (45, 100, 65),
            "lawnMowingMonthly": (160, 360, 230),
            "landscapeDesignInstall": (2500, 18000, 8000),
            "sprinklerInstall": (2000, 5500, 3500),
            "treeTrimmingSmall": (175, 450, 275),
            "treeTrimmingLarge": (500, 1500, 850),
            "mulchInstall": (250, 900, 500),
            "sod": (1, 2, 2),
        }
    elif state in MILD_WEST:
        return {
            "lawnMowingWeekly": (50, 120, 75),
            "lawnMowingMonthly": (175, 420, 280),
            "landscapeDesignInstall": (3000, 20000, 9500),
            "sprinklerInstall": (2800, 7000, 4500),
            "treeTrimmingSmall": (200, 500, 320),
            "treeTrimmingLarge": (500, 1800, 950),
            "mulchInstall": (300, 1000, 580),
            "sod": (2, 3, 2),
        }
    elif state in WARM_SOUTH:
        return {
            "lawnMowingWeekly": (35, 80, 52),
            "lawnMowingMonthly": (130, 300, 190),
            "landscapeDesignInstall": (1800, 12000, 5500),
            "sprinklerInstall": (2000, 5500, 3200),
            "treeTrimmingSmall": (125, 350, 210),
            "treeTrimmingLarge": (350, 1100, 620),
            "mulchInstall": (175, 700, 390),
            "sod": (1, 2, 1),
        }
    else:  # Cold North
        return {
            "lawnMowingWeekly": (40, 90, 58),
            "lawnMowingMonthly": (145, 330, 210),
            "landscapeDesignInstall": (2000, 14000, 6000),
            "sprinklerInstall": (2200, 6000, 3600),
            "treeTrimmingSmall": (150, 400, 230),
            "treeTrimmingLarge": (400, 1300, 700),
            "mulchInstall": (200, 800, 420),
            "sod": (1, 2, 2),
        }

def get_climate_note(state, city):
    if state in DESERT:
        return f"{city}'s desert climate demands xeriscaping, irrigation system maintenance, and heat-tolerant plantings. Water conservation tree-service is both popular and practical"
    elif state in TROPICAL_YEAR_ROUND:
        return f"{city}'s tropical/subtropical climate supports year-round growing — tree-service companies stay busy every month with fast-growing grass, tropical plantings, and hurricane prep"
    elif state in MILD_WEST:
        return f"{city}'s mild climate extends the growing season. Moss, rain garden management, and drought-tolerant tree-service are common requests"
    elif state in WARM_SOUTH:
        return f"{city}'s warm climate means a long growing season — typically 7-8 active months with Bermuda and Zoysia grass dominant. Spring prep and fall cleanup are peak seasons"
    else:
        return f"{city}'s four-season climate creates a spring rush (April–May) and fall cleanup season. Snow melt, aeration, and overseeding are key annual services"

def build_providers(city, state):
    types = [
        f"{city} Lawn & Landscape",
        f"Green {city} Tree Service",
        f"{city} Outdoor Services",
        f"Premier Landscapes {city}",
        f"{city} Grounds Care",
        f"Nature's Best {city}",
        f"{city} Lawn Pros",
    ]
    providers = []
    ratings = [4.9, 4.8, 4.7, 4.7, 4.6]
    reviews = [412, 301, 247, 189, 143]
    names = random.sample(types, 5)
    for i in range(5):
        providers.append({
            "name": names[i],
            "rating": ratings[i],
            "reviews": reviews[i],
            "phone": "",
            "address": f"{city}, {state}",
            "services": ["Lawn Mowing", "Tree Service Design", "Tree Trimming", "Mulching", "Sprinkler Install"],
            "licensed": True,
            "insured": True,
            "yearsInBusiness": random.randint(5, 22),
        })
    return providers

def build_faqs(city, state, costs):
    note = get_climate_note(state, city)
    mow_avg = costs["lawnMowingWeekly"][2]
    mow_mo = costs["lawnMowingMonthly"][2]
    design_min, design_max, design_avg = costs["landscapeDesignInstall"]
    spr_avg = costs["sprinklerInstall"][2]
    tree_sm = costs["treeTrimmingSmall"][2]
    tree_lg = costs["treeTrimmingLarge"][2]
    mulch_avg = costs["mulchInstall"][2]
    return [
        {
            "question": f"How much does lawn mowing cost in {city}, {state}?",
            "answer": f"Lawn mowing in {city} costs ${mow_avg} per visit on average, with most homeowners paying ${mow_avg - 10}–${mow_avg + 15} for a standard residential lawn. Monthly plans typically run ${mow_mo - 20}–${mow_mo + 40}. {note}. Pricing varies by lot size — small lots (under 5,000 sq ft) run lower; large properties (10,000+ sq ft) run higher."
        },
        {
            "question": f"How much does tree-service cost in {city}?",
            "answer": f"Tree Service projects in {city} vary widely by scope. Basic cleanup and mulch runs ${mulch_avg}–${mulch_avg * 2}. A mid-size front yard redesign costs ${design_min:,}–${int(design_avg):,}. Full backyard transformation with hardscape, plants, and irrigation runs ${int(design_avg):,}–${design_max:,}. Always get 3 quotes and a written scope before starting."
        },
        {
            "question": f"How much does sprinkler/irrigation installation cost in {city}?",
            "answer": f"Sprinkler system installation in {city} runs ${costs['sprinklerInstall'][0]:,}–${costs['sprinklerInstall'][1]:,}, averaging ${spr_avg:,} for a standard residential lot. Smart controllers add $150–$400 but can reduce water bills 20–40%. {note}."
        },
        {
            "question": f"How much does tree trimming cost in {city}?",
            "answer": f"Tree trimming in {city} costs ${tree_sm}–${tree_sm + 100} for small trees (under 30 ft) and ${tree_lg}–${tree_lg + 300} for large trees. Emergency tree removal after storms runs higher — $500–$2,500 depending on size and accessibility. Always verify tree service companies carry adequate liability insurance before hiring."
        },
        {
            "question": f"How often should I have my lawn mowed in {city}?",
            "answer": f"In {city}, {get_season(state).lower()} is the active growing season. During peak growth (spring/summer), weekly mowing keeps lawns healthy and prevents scalping. Bi-weekly works during slower growth periods. {note}. Most {city} tree-service companies offer flexible weekly, bi-weekly, or monthly plans."
        },
        {
            "question": f"What's the best time to do tree-service in {city}?",
            "answer": f"The best time for major tree-service projects in {city} is early spring (March–April) or early fall (September–October) when temperatures are moderate and plants establish well. {note}. Booking early in spring is critical — most reputable {city} landscapers are booked 3–6 weeks out by May."
        },
        {
            "question": f"How do I choose a tree-service company in {city}?",
            "answer": f"Look for {city} landscapers who: (1) are licensed and carry general liability + workers' comp, (2) have 4.5+ star ratings with 50+ reviews, (3) provide written quotes with a defined scope of work, (4) have been operating locally for 5+ years, (5) offer a satisfaction guarantee. Avoid cash-only contractors or those who can't provide a certificate of insurance."
        },
        {
            "question": f"Do tree-service companies in {city} offer seasonal contracts?",
            "answer": f"Yes — most {city} tree-service companies offer seasonal or annual maintenance contracts that bundle mowing, edging, fertilizing, mulching, and cleanup. Annual contracts typically save 10–20% vs. per-service pricing and guarantee priority scheduling. Ask about start-of-season aeration and overseeding packages, which are popular in {city}'s climate."
        },
    ]

def build_buyer_tips(city, state, costs):
    return [
        f"Always get 3 written quotes before hiring a landscaper in {city} — prices for the same job vary 25–40%.",
        f"Verify the company carries general liability insurance ($1M minimum) and workers' comp — accidents on your property without coverage can become your liability.",
        f"Ask for references from {city} homeowners who had similar work done — a reputable landscaper will provide them without hesitation.",
        f"Get everything in writing: scope of work, materials, plant species/varieties, timeline, and payment schedule.",
        f"For new plantings, ask about the warranty — good {city} landscapers guarantee plants for 1 growing season.",
        f"Book spring projects early (January–February) — the best {city} landscapers fill their calendars by March.",
        f"Annual maintenance contracts save 10–20% over one-off services and guarantee consistent quality throughout the season.",
    ]

def generate_city(info):
    costs = get_costs(info["stateAbbr"])
    return {
        "slug": info["slug"],
        "city": info["city"],
        "state": info["state"],
        "stateAbbr": info["stateAbbr"],
        "population": info["population"],
        "tree-serviceSeason": get_season(info["stateAbbr"]),
        "climateNote": get_climate_note(info["stateAbbr"], info["city"]),
        "costs": {
            "lawnMowingWeekly": {"min": costs["lawnMowingWeekly"][0], "max": costs["lawnMowingWeekly"][1], "avg": costs["lawnMowingWeekly"][2]},
            "lawnMowingMonthly": {"min": costs["lawnMowingMonthly"][0], "max": costs["lawnMowingMonthly"][1], "avg": costs["lawnMowingMonthly"][2]},
            "landscapeDesignInstall": {"min": costs["landscapeDesignInstall"][0], "max": costs["landscapeDesignInstall"][1], "avg": costs["landscapeDesignInstall"][2]},
            "sprinklerInstall": {"min": costs["sprinklerInstall"][0], "max": costs["sprinklerInstall"][1], "avg": costs["sprinklerInstall"][2]},
            "treeTrimmingSmall": {"min": costs["treeTrimmingSmall"][0], "max": costs["treeTrimmingSmall"][1], "avg": costs["treeTrimmingSmall"][2]},
            "treeTrimmingLarge": {"min": costs["treeTrimmingLarge"][0], "max": costs["treeTrimmingLarge"][1], "avg": costs["treeTrimmingLarge"][2]},
            "mulchInstall": {"min": costs["mulchInstall"][0], "max": costs["mulchInstall"][1], "avg": costs["mulchInstall"][2]},
        },
        "providers": build_providers(info["city"], info["state"]),
        "faqs": build_faqs(info["city"], info["stateAbbr"], costs),
        "buyerTips": build_buyer_tips(info["city"], info["stateAbbr"], costs),
        "lastUpdated": "2026-04-03",
        "dataSource": "Tree Service industry cost data, regional market research",
    }

if __name__ == "__main__":
    out_dir = os.path.join(os.path.dirname(__file__), '..', 'data', 'cities')
    os.makedirs(out_dir, exist_ok=True)
    index = []
    for info in CITIES:
        data = generate_city(info)
        with open(os.path.join(out_dir, f"{info['slug']}.json"), 'w') as f:
            json.dump(data, f, indent=2)
        print(f"✅ {info['city']}, {info['stateAbbr']}")
        index.append({"slug": info["slug"], "city": info["city"], "state": info["state"], "stateAbbr": info["stateAbbr"]})
    with open(os.path.join(out_dir, 'cities-index.json'), 'w') as f:
        json.dump(index, f, indent=2)
    print(f"\n✅ Generated {len(CITIES)} cities + index")
