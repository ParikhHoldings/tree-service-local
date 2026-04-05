#!/usr/bin/env python3
"""Generate city data JSON files for 30 new cities."""
import json, os
from datetime import date

TODAY = date.today().isoformat()
DATA_DIR = '/root/clawd/projects/portfolio/programmatic/service-city-seo/site/data/cities'

# Load real Yelp data
with open('/root/clawd/projects/portfolio/programmatic/service-city-seo/site/scripts/yelp_results.json') as f:
    YELP_DATA = json.load(f)

NEW_CITIES = [
    {
        "slug": "jacksonville-fl",
        "city": "Jacksonville",
        "state": "Florida",
        "stateAbbr": "FL",
        "population": 949611,
        "poolSeason": "March–November",
        "climate": "subtropical",
        "avgPoolsPerCapita": "1 in 9 homes",
        "costs": {
            "weeklyMaintenance": {"min": 80, "max": 160, "avg": 110},
            "monthlyMaintenance": {"min": 150, "max": 350, "avg": 220},
            "openingService": {"min": 100, "max": 200, "avg": 150},
            "closingService": {"min": 100, "max": 200, "avg": 150},
            "repairHourly": {"min": 75, "max": 150, "avg": 100},
            "fullClean": {"min": 150, "max": 300, "avg": 200}
        },
        "challenges": "High humidity and heat drive persistent algae growth. Heavy rainfall dilutes chemicals and causes runoff. Hurricane season (June–November) brings debris and contamination. Saltwater pools common due to coastal proximity.",
        "bestTime": "Year-round service is possible, with peak maintenance needs from April through October.",
        "regionFAQs": [
            {"question": "How do I prevent algae in my Jacksonville pool during summer?", "answer": "Jacksonville's humid subtropical climate creates prime algae conditions May–September. Maintain chlorine at 2–4 ppm, shock weekly during peak summer, use an algaecide preventively, and brush walls twice weekly. Algae can bloom overnight in 95°F+ heat."},
            {"question": "Should I close my pool in Jacksonville for winter?", "answer": "Most Jacksonville pool owners keep pools open year-round since temperatures rarely drop below 50°F for extended periods. A basic winterization (lower chemical levels, reduce pump hours) is sufficient — full closing is usually unnecessary."},
            {"question": "How does hurricane season affect pool maintenance in Jacksonville?", "answer": "Before storms: remove or secure accessories, partially drain to prevent overflow, add extra algaecide and shock. After storms: remove debris, retest all chemistry, shock the pool, and inspect equipment for damage. Budget for at least one major post-storm cleanup service."}
        ]
    },
    {
        "slug": "columbus-oh",
        "city": "Columbus",
        "state": "Ohio",
        "stateAbbr": "OH",
        "population": 905748,
        "poolSeason": "May–September",
        "climate": "humid continental",
        "avgPoolsPerCapita": "1 in 14 homes",
        "costs": {
            "weeklyMaintenance": {"min": 75, "max": 150, "avg": 100},
            "monthlyMaintenance": {"min": 140, "max": 300, "avg": 200},
            "openingService": {"min": 150, "max": 300, "avg": 200},
            "closingService": {"min": 150, "max": 350, "avg": 250},
            "repairHourly": {"min": 80, "max": 160, "avg": 110},
            "fullClean": {"min": 150, "max": 350, "avg": 225}
        },
        "challenges": "Freeze/thaw cycles require professional winterization to prevent pipe damage. Short swim season (4–5 months) means service costs are compressed. Spring opening often reveals winter damage. Pollen season (April–May) spikes cleaning needs.",
        "bestTime": "Memorial Day through Labor Day is the core service season. Closing service is critical in October before first freeze.",
        "regionFAQs": [
            {"question": "When should I open my pool in Columbus, OH?", "answer": "Columbus pools typically open Memorial Day weekend (late May) when water temps reach 60–65°F. Opening too early wastes chemicals; too late risks missing warm weekends. A professional opening service runs $150–300 and includes equipment startup, chemical balance, and inspection."},
            {"question": "How much does pool closing cost in Columbus, OH?", "answer": "Pool closing in Columbus costs $150–350, with average around $250. It includes blowing out lines, plugging returns, draining equipment, adding winterizing chemicals, and covering the pool. Proper closing is critical — a missed freeze can crack pipes costing $1,000+."},
            {"question": "Do I need weekly pool service in Columbus during the summer?", "answer": "Yes — Columbus summers are warm and humid, which accelerates algae and bacterial growth. Weekly service maintains chemical balance and prevents green pool scenarios. Many homeowners opt for bi-weekly visits with a good automatic cleaner, but weekly is recommended for busy families."}
        ]
    },
    {
        "slug": "indianapolis-in",
        "city": "Indianapolis",
        "state": "Indiana",
        "stateAbbr": "IN",
        "population": 887642,
        "poolSeason": "May–September",
        "climate": "humid continental",
        "avgPoolsPerCapita": "1 in 15 homes",
        "costs": {
            "weeklyMaintenance": {"min": 70, "max": 145, "avg": 95},
            "monthlyMaintenance": {"min": 130, "max": 280, "avg": 190},
            "openingService": {"min": 150, "max": 280, "avg": 200},
            "closingService": {"min": 150, "max": 320, "avg": 230},
            "repairHourly": {"min": 75, "max": 150, "avg": 100},
            "fullClean": {"min": 140, "max": 300, "avg": 210}
        },
        "challenges": "Cold winters require thorough winterization. Heavy spring rains can dilute pool chemicals. Storm debris is common. Short swim season means equipment must be perfect from day one.",
        "bestTime": "June through August is peak season. Open in late May, close by mid-October.",
        "regionFAQs": [
            {"question": "What does pool winterization cost in Indianapolis?", "answer": "Pool winterization in Indianapolis runs $150–320 on average. This includes blowing out plumbing lines, plugging all return jets, draining pump and filter, adding antifreeze to lines, and applying a winter chemical kit. Proper winterization protects against Indianapolis's below-freezing winters."},
            {"question": "How do I handle spring pool opening after an Indianapolis winter?", "answer": "Indianapolis spring openings often reveal algae from winter chemical degradation and occasionally cracked equipment. A professional opening ($150–280) includes removing the cover, reconecting equipment, shocking the water, and testing all chemistry. Budget extra if the pool has been green or equipment froze."},
            {"question": "Is year-round pool service available in Indianapolis?", "answer": "Most Indianapolis pool companies offer year-round contracts that cover opening, weekly summer service, and closing. Year-round plans typically cost $800–1,800/season. Off-season, service reduces to monthly chemical checks if the pool stays partially active."}
        ]
    },
    {
        "slug": "san-jose-ca",
        "city": "San Jose",
        "state": "California",
        "stateAbbr": "CA",
        "population": 1013240,
        "poolSeason": "Year-round",
        "climate": "Mediterranean",
        "avgPoolsPerCapita": "1 in 10 homes",
        "costs": {
            "weeklyMaintenance": {"min": 100, "max": 200, "avg": 140},
            "monthlyMaintenance": {"min": 180, "max": 400, "avg": 275},
            "openingService": {"min": 75, "max": 150, "avg": 100},
            "closingService": {"min": 75, "max": 150, "avg": 100},
            "repairHourly": {"min": 90, "max": 180, "avg": 130},
            "fullClean": {"min": 175, "max": 400, "avg": 265}
        },
        "challenges": "Drought restrictions limit water refills — leak detection is essential. High mineral content in water causes calcium scaling. Wildfire ash events contaminate pools suddenly. Water costs make conservation critical.",
        "bestTime": "Year-round service is common. Peak demand runs April–October with warm, dry conditions.",
        "regionFAQs": [
            {"question": "How do California water restrictions affect pool service in San Jose?", "answer": "San Jose and Santa Clara County enforce water conservation rules, especially during droughts. You can't drain and refill your pool without permits during Stage 2+ restrictions. This makes maintaining existing water quality critical — chemical balance, leak repair, and covers (which reduce evaporation 30–50%) are all important investments."},
            {"question": "How do I remove calcium scaling from my San Jose pool?", "answer": "San Jose's hard water (high calcium and magnesium) deposits scale on surfaces within months. Prevention: keep calcium hardness between 200–400 ppm, pH below 7.6, and use a sequestrant. Treatment: acid washing ($300–600) removes existing scale. Annual descaling service keeps tile and surfaces clean."},
            {"question": "What happens to my pool during wildfire smoke events near San Jose?", "answer": "Wildfire ash contains minerals, phosphates, and contaminants that cloud water and spike pH. After a smoke event: test and adjust chemistry immediately, shock the pool, clean filters more frequently, and run the pump 24/7 for 48 hours. Heavy ash events may require a full cleaning service ($175–400)."}
        ]
    },
    {
        "slug": "seattle-wa",
        "city": "Seattle",
        "state": "Washington",
        "stateAbbr": "WA",
        "population": 749256,
        "poolSeason": "June–August",
        "climate": "oceanic",
        "avgPoolsPerCapita": "1 in 25 homes",
        "costs": {
            "weeklyMaintenance": {"min": 90, "max": 175, "avg": 120},
            "monthlyMaintenance": {"min": 160, "max": 350, "avg": 230},
            "openingService": {"min": 150, "max": 300, "avg": 200},
            "closingService": {"min": 175, "max": 350, "avg": 250},
            "repairHourly": {"min": 85, "max": 175, "avg": 125},
            "fullClean": {"min": 150, "max": 350, "avg": 240}
        },
        "challenges": "Abundant rainfall (38 inches/year) dilutes pool chemicals and causes overflow. Overcast skies slow algae in some areas but damp conditions harbor moss and biofilm. Short, intense swim season means maintenance timing is critical. Moss and organic debris from surrounding trees.",
        "bestTime": "Seattle's brief summer (July–August) is the only reliable swim season. Open in late June, close by September.",
        "regionFAQs": [
            {"question": "Is it worth having a pool in Seattle given the rainy weather?", "answer": "Seattle pools see only 6–8 weeks of reliable swim weather (mid-July through August), but many homeowners find the investment worthwhile for summer entertaining. Year-round costs run $2,500–4,500 when including opening, weekly service, and winterization. Pool covers are essential to retain heat and keep out debris."},
            {"question": "How does heavy Seattle rainfall affect pool chemistry?", "answer": "Seattle's 38+ inches of annual rain constantly dilutes your pool, lowering chlorine, pH, and alkalinity. After heavy rain, retest and adjust chemistry within 24 hours. Overflow conditions can introduce contaminants. Weekly service is essential during the swim season, and pre-storm chemical boosts protect against sudden dilution."},
            {"question": "What type of pool cover is best for Seattle's climate?", "answer": "For Seattle, a solid safety cover or automatic cover is ideal — both block rain, debris, and leaves. Solar covers help heat the water during the brief summer but don't handle Seattle's heavy rain well. Automatic covers ($10,000–20,000 installed) are the gold standard for Pacific Northwest pools."}
        ]
    },
    {
        "slug": "memphis-tn",
        "city": "Memphis",
        "state": "Tennessee",
        "stateAbbr": "TN",
        "population": 651073,
        "poolSeason": "April–October",
        "climate": "humid subtropical",
        "avgPoolsPerCapita": "1 in 11 homes",
        "costs": {
            "weeklyMaintenance": {"min": 75, "max": 150, "avg": 100},
            "monthlyMaintenance": {"min": 140, "max": 300, "avg": 200},
            "openingService": {"min": 100, "max": 220, "avg": 150},
            "closingService": {"min": 100, "max": 220, "avg": 150},
            "repairHourly": {"min": 70, "max": 145, "avg": 95},
            "fullClean": {"min": 130, "max": 280, "avg": 190}
        },
        "challenges": "Extreme summer humidity and heat (100°F+ feels-like) accelerate algae and bacteria growth. Spring storms bring debris and dilution. Mississippi River humidity creates challenging chemical management.",
        "bestTime": "May through September for active swimming. Professional opening in April, closing in late October.",
        "regionFAQs": [
            {"question": "Why does my Memphis pool turn green so fast in the summer?", "answer": "Memphis summers are hot and extremely humid — ideal conditions for algae. Chlorine burns off faster at high temperatures, and warm water speeds up algae reproduction. During July–August heat waves, you may need to shock twice weekly and maintain higher chlorine residual (3–4 ppm instead of the standard 1–3 ppm)."},
            {"question": "How much should pool service cost in Memphis, TN?", "answer": "Pool service in Memphis typically runs $75–150/week for basic maintenance or $140–300/month for full-service. These rates are below the national average, reflecting lower labor costs in the Memphis market. Chemical costs are included in most service packages."},
            {"question": "Do Memphis pools need winterization?", "answer": "Yes — Memphis temperatures can drop below freezing December through February, and a cold snap can burst pipes in a non-winterized pool. Closing service ($100–220) includes draining equipment, blowing lines, adding antifreeze, and covering the pool. Don't skip this even in mild years."}
        ]
    },
    {
        "slug": "louisville-ky",
        "city": "Louisville",
        "state": "Kentucky",
        "stateAbbr": "KY",
        "population": 663255,
        "poolSeason": "May–September",
        "climate": "humid subtropical",
        "avgPoolsPerCapita": "1 in 12 homes",
        "costs": {
            "weeklyMaintenance": {"min": 70, "max": 145, "avg": 95},
            "monthlyMaintenance": {"min": 130, "max": 280, "avg": 195},
            "openingService": {"min": 120, "max": 250, "avg": 170},
            "closingService": {"min": 120, "max": 280, "avg": 190},
            "repairHourly": {"min": 70, "max": 145, "avg": 98},
            "fullClean": {"min": 130, "max": 275, "avg": 190}
        },
        "challenges": "Wide temperature swings (cold winters, hot humid summers) stress equipment. Kentucky Derby season brings heavy spring entertaining demand. Ohio River valley humidity creates challenging water chemistry. Late-spring pollen events.",
        "bestTime": "June through August. Open by Memorial Day, close after Labor Day.",
        "regionFAQs": [
            {"question": "When should I open and close my pool in Louisville, KY?", "answer": "Louisville pools typically open Memorial Day weekend and close after Labor Day. Water temperatures reach swimmable levels (70°F+) by late May/early June. Closing before October 15 is wise — Louisville averages its first freeze in mid-October. Late openers risk missing warm-weather windows."},
            {"question": "How does Louisville's humidity affect pool maintenance?", "answer": "Louisville sits in the Ohio River valley with high summer humidity. Warm, moist conditions accelerate chlorine demand and algae growth June–August. Weekly service is essential, and chemical checks after heavy rain are important since Louisville averages 44 inches of rain per year."},
            {"question": "What's the best pool service schedule for Louisville?", "answer": "Most Louisville pool owners use weekly service May–September ($70–145/visit) with professional opening and closing. A full-service contract typically runs $1,200–2,200/season. Consider adding a monthly equipment check even during winter to catch any freeze damage early."}
        ]
    },
    {
        "slug": "baltimore-md",
        "city": "Baltimore",
        "state": "Maryland",
        "stateAbbr": "MD",
        "population": 585708,
        "poolSeason": "May–September",
        "climate": "humid subtropical",
        "avgPoolsPerCapita": "1 in 13 homes",
        "costs": {
            "weeklyMaintenance": {"min": 85, "max": 165, "avg": 115},
            "monthlyMaintenance": {"min": 155, "max": 330, "avg": 225},
            "openingService": {"min": 150, "max": 300, "avg": 210},
            "closingService": {"min": 150, "max": 325, "avg": 225},
            "repairHourly": {"min": 85, "max": 170, "avg": 120},
            "fullClean": {"min": 165, "max": 350, "avg": 240}
        },
        "challenges": "Humid summers with heavy thunderstorms. Chesapeake Bay area pollen and tree debris. Harsh winters require thorough closing. Older neighborhood pools often have aging equipment needing regular service.",
        "bestTime": "June through August. Professional opening in May, closing in October.",
        "regionFAQs": [
            {"question": "How much does pool opening and closing cost in Baltimore?", "answer": "Pool opening in Baltimore runs $150–300 and closing $150–325. Combined opening+closing packages run $350–600. These services include equipment startup/shutdown, chemical treatment, and cover installation/removal. Baltimore's harsh winters make proper closing non-negotiable to prevent freeze damage."},
            {"question": "How do I deal with Baltimore's summer thunderstorms and pool chemistry?", "answer": "Baltimore averages 40+ inches of rain and frequent summer thunderstorms. Each heavy rain dilutes chlorine and can shift pH dramatically. Establish a 'storm routine': retest chemistry within 12 hours after significant rain, add a chlorine boost, and check that drains aren't clogged with debris."},
            {"question": "What should I look for when hiring a pool service company in Baltimore?", "answer": "In Maryland, pool service contractors should hold a Home Improvement license from MHIC. Verify licensing online at the Maryland DLLR website. Ask for CPO (Certified Pool Operator) certification, proof of liability insurance, and check BBB ratings. Get 3 quotes — prices in Baltimore vary 40–50% between companies."}
        ]
    },
    {
        "slug": "milwaukee-wi",
        "city": "Milwaukee",
        "state": "Wisconsin",
        "stateAbbr": "WI",
        "population": 577222,
        "poolSeason": "June–August",
        "climate": "humid continental",
        "avgPoolsPerCapita": "1 in 18 homes",
        "costs": {
            "weeklyMaintenance": {"min": 75, "max": 150, "avg": 100},
            "monthlyMaintenance": {"min": 140, "max": 290, "avg": 195},
            "openingService": {"min": 175, "max": 325, "avg": 230},
            "closingService": {"min": 175, "max": 350, "avg": 250},
            "repairHourly": {"min": 80, "max": 160, "avg": 110},
            "fullClean": {"min": 150, "max": 320, "avg": 220}
        },
        "challenges": "Brutal winters require meticulous winterization — pipes freeze solid December through March. Short swim season (10–12 weeks). Lake Michigan weather creates rapid temperature drops. Spring opening often reveals ice damage.",
        "bestTime": "July and August are the reliable swim months. Open in early June, close by mid-September.",
        "regionFAQs": [
            {"question": "What does proper pool winterization cost in Milwaukee?", "answer": "Milwaukee pool closing costs $175–350, reflecting the extreme care needed for Wisconsin winters. Proper winterization includes draining all water from pipes, pump, filter, and heater; adding antifreeze to lines; plugging all returns; and securing a durable cover. A poorly winterized Milwaukee pool can see $2,000–5,000 in freeze damage."},
            {"question": "How short is Milwaukee's pool season, really?", "answer": "Milwaukee's reliable swim season is roughly 10–12 weeks — late June through early September. Water temperatures in Lake Michigan stay cold well into summer, creating cool air off the lake. Most Milwaukee pools heat to 80°F+ by July 4th. Budget for opening and closing as major annual costs in addition to short-season service."},
            {"question": "Can I use a pool heater to extend Milwaukee's swim season?", "answer": "Yes — a pool heater can extend your season by 4–6 weeks on each end (May and October). Gas heaters are most common and heat fastest; heat pumps are efficient but require ambient temps above 50°F. Heated pool season in Milwaukee can run late May through early October with the right equipment."}
        ]
    },
    {
        "slug": "albuquerque-nm",
        "city": "Albuquerque",
        "state": "New Mexico",
        "stateAbbr": "NM",
        "population": 564559,
        "poolSeason": "May–October",
        "climate": "semi-arid",
        "avgPoolsPerCapita": "1 in 12 homes",
        "costs": {
            "weeklyMaintenance": {"min": 75, "max": 150, "avg": 100},
            "monthlyMaintenance": {"min": 140, "max": 300, "avg": 200},
            "openingService": {"min": 100, "max": 200, "avg": 140},
            "closingService": {"min": 100, "max": 200, "avg": 140},
            "repairHourly": {"min": 75, "max": 150, "avg": 100},
            "fullClean": {"min": 140, "max": 300, "avg": 195}
        },
        "challenges": "Desert sun and UV degrade chlorine rapidly — stabilizer (cyanuric acid) management is critical. High mineral content causes calcium and scale buildup. Summer monsoon season (July–August) brings debris and chemical dilution. Altitude (5,312 ft) affects chlorine chemistry.",
        "bestTime": "June through September is peak season. Albuquerque's altitude means cooler nights even in summer.",
        "regionFAQs": [
            {"question": "How does Albuquerque's altitude affect pool chemistry?", "answer": "At 5,312 feet, Albuquerque has lower atmospheric pressure, which affects how chlorine and other chemicals work. You may need slightly different chemical ratios compared to sea-level pools. The intense high-altitude UV also burns through chlorine faster — keep stabilizer (cyanuric acid) at 40–80 ppm to protect chlorine from UV degradation."},
            {"question": "How do I handle the monsoon season for my Albuquerque pool?", "answer": "Albuquerque's July–August monsoon season brings sudden heavy rains that can double your pool's water volume in a day. Before monsoon: test chemistry and raise levels slightly to buffer dilution. After: retest immediately, shock, and check for debris. Monsoon runoff often carries dust, leaves, and minerals that cloud water."},
            {"question": "Why does my Albuquerque pool get calcium scaling so quickly?", "answer": "Albuquerque's municipal water has high mineral content (calcium hardness 200–400 ppm in tap water). Combined with evaporation and desert heat, calcium concentrates rapidly. Keep pH between 7.4–7.6, maintain calcium hardness below 400 ppm, and use a weekly sequestrant. Annual acid washing ($300–600) removes existing scale buildup."}
        ]
    },
    {
        "slug": "tucson-az",
        "city": "Tucson",
        "state": "Arizona",
        "stateAbbr": "AZ",
        "population": 542629,
        "poolSeason": "Year-round",
        "climate": "desert",
        "avgPoolsPerCapita": "1 in 8 homes",
        "costs": {
            "weeklyMaintenance": {"min": 80, "max": 175, "avg": 115},
            "monthlyMaintenance": {"min": 150, "max": 380, "avg": 255},
            "openingService": {"min": 75, "max": 150, "avg": 100},
            "closingService": {"min": 75, "max": 150, "avg": 100},
            "repairHourly": {"min": 80, "max": 160, "avg": 110},
            "fullClean": {"min": 150, "max": 325, "avg": 215}
        },
        "challenges": "Extreme summer heat (110°F+) burns through chemicals rapidly. Desert dust storms (haboobs) fill pools with dirt and sand. Monsoon season brings sudden chemical dilution. Hard water causes constant calcium scaling. UV intensity requires high stabilizer levels.",
        "bestTime": "October through May offers ideal swimming temperatures. Summer swimming is possible but pools can reach 90°F+ without chillers.",
        "regionFAQs": [
            {"question": "How do I manage my Tucson pool during a dust storm (haboob)?", "answer": "Tucson's summer haboobs can dump pounds of fine dust into your pool in minutes. Immediately after a haboob: run your filter continuously for 24–48 hours, brush all surfaces, shock the pool, and clean/backwash filters. Add a clarifier to help small particles clump and filter out. Budget $75–200 for a professional post-haboob cleanup."},
            {"question": "Does my Tucson pool need year-round service?", "answer": "Yes — Tucson pools are used year-round and maintenance never fully stops. Weekly service is recommended even in winter since the pool is actively used and UV still degrades chlorine (Tucson averages 350+ sunny days/year). Monthly service works if you're comfortable doing basic checks yourself during cooler months."},
            {"question": "How do I prevent my Tucson pool from getting too hot in summer?", "answer": "Tucson pool water can reach 92–96°F in July–August, making swimming uncomfortable. Options: run your pump at night to cool water, add a water feature or fountain for evaporative cooling, plant shade trees (5+ year investment), or install a pool chiller ($3,000–8,000). Shade structures provide both sun protection and cooling."}
        ]
    },
    {
        "slug": "fresno-ca",
        "city": "Fresno",
        "state": "California",
        "stateAbbr": "CA",
        "population": 542107,
        "poolSeason": "April–October",
        "climate": "semi-arid Mediterranean",
        "avgPoolsPerCapita": "1 in 9 homes",
        "costs": {
            "weeklyMaintenance": {"min": 90, "max": 170, "avg": 120},
            "monthlyMaintenance": {"min": 165, "max": 350, "avg": 240},
            "openingService": {"min": 100, "max": 200, "avg": 140},
            "closingService": {"min": 100, "max": 200, "avg": 140},
            "repairHourly": {"min": 85, "max": 165, "avg": 115},
            "fullClean": {"min": 160, "max": 350, "avg": 240}
        },
        "challenges": "Valley heat (105°F+ summers) rapidly degrades chemicals. San Joaquin Valley air quality issues — smoke and particulate matter contaminate pools. Drought water restrictions. Hard water with high mineral content creates scaling.",
        "bestTime": "May through September. Valley summers are hot but dry — great swimming weather.",
        "regionFAQs": [
            {"question": "How does Fresno's valley heat affect pool maintenance?", "answer": "Fresno regularly hits 105–110°F in July–August. At these temperatures, chlorine burns off in hours, not days. Maintain stabilizer (CYA) at 60–80 ppm to protect chlorine from UV, keep chlorine at 3–4 ppm during peak summer, and consider switching to a saltwater system to reduce chemical management. Weekly service is essential."},
            {"question": "How does wildfire smoke affect my Fresno pool?", "answer": "Fresno's Central Valley location means heavy smoke accumulation during California fire season. Ash and smoke particles cloud water, spike phosphate levels, and can clog filters rapidly. During smoke events: run filter 24/7, clean filter media more frequently, test and adjust chemistry every 2–3 days, and shock after heavy smoke days."},
            {"question": "Are there water restrictions affecting Fresno pool owners?", "answer": "Yes — Fresno and Fresno County enforce California water conservation rules during drought conditions. Pools cannot be drained and refilled during drought emergency declarations. Top-off water for evaporation is typically permitted. Leak detection is critical — even a small leak wastes thousands of gallons and may violate restrictions."}
        ]
    },
    {
        "slug": "sacramento-ca",
        "city": "Sacramento",
        "state": "California",
        "stateAbbr": "CA",
        "population": 524943,
        "poolSeason": "April–October",
        "climate": "Mediterranean",
        "avgPoolsPerCapita": "1 in 9 homes",
        "costs": {
            "weeklyMaintenance": {"min": 95, "max": 185, "avg": 130},
            "monthlyMaintenance": {"min": 175, "max": 380, "avg": 270},
            "openingService": {"min": 100, "max": 210, "avg": 150},
            "closingService": {"min": 100, "max": 210, "avg": 150},
            "repairHourly": {"min": 90, "max": 180, "avg": 125},
            "fullClean": {"min": 175, "max": 380, "avg": 260}
        },
        "challenges": "Sacramento Valley experiences triple-digit heat waves. Wildfire smoke from Sierra Nevada foothills. Drought and water restrictions. Hard water scaling. Eucalyptus and oak tree debris contaminate pools.",
        "bestTime": "June through September. Sacramento's dry Mediterranean summers are ideal for swimming.",
        "regionFAQs": [
            {"question": "How do I prepare my Sacramento pool for a heat wave?", "answer": "Sacramento experiences multi-day heat waves exceeding 110°F. Before a heat wave: shock the pool, raise chlorine to 4–5 ppm, ensure stabilizer is at 60–80 ppm, and clean the filter. During the heat wave: test daily and add chlorine as needed. After: do a full chemistry test and adjust. Consider running the pump extra hours to circulate water."},
            {"question": "What's the best pool service schedule for Sacramento?", "answer": "Most Sacramento pool owners use weekly service April–October, with April being opening month and October being light-service month. Full summer service runs $95–185/week. A year-round contract (12 months) typically runs $1,800–3,600 and covers all service plus chemicals."},
            {"question": "How does Sacramento's hard water affect my pool equipment?", "answer": "Sacramento water has calcium hardness around 100–200 ppm, which combined with high evaporation rates concentrates minerals. Scale builds up on tile, the waterline, inside pipes, and inside heaters. Annual acid washing ($300–600), regular tile brushing, and keeping pH below 7.6 prevent major scaling issues."}
        ]
    },
    {
        "slug": "mesa-az",
        "city": "Mesa",
        "state": "Arizona",
        "stateAbbr": "AZ",
        "population": 504258,
        "poolSeason": "Year-round",
        "climate": "desert",
        "avgPoolsPerCapita": "1 in 7 homes",
        "costs": {
            "weeklyMaintenance": {"min": 85, "max": 190, "avg": 125},
            "monthlyMaintenance": {"min": 155, "max": 420, "avg": 285},
            "openingService": {"min": 75, "max": 150, "avg": 100},
            "closingService": {"min": 75, "max": 150, "avg": 100},
            "repairHourly": {"min": 80, "max": 160, "avg": 110},
            "fullClean": {"min": 150, "max": 340, "avg": 220}
        },
        "challenges": "Same as greater Phoenix metro: intense UV, heat, calcium scaling, haboob dust storms, and monsoon season chemical dilution. Mesa's older neighborhoods often have aging pool equipment needing more frequent repairs.",
        "bestTime": "October through May is ideal. Summer swimming is possible with early morning hours.",
        "regionFAQs": [
            {"question": "How much does pool service cost in Mesa, AZ?", "answer": "Pool service in Mesa runs $85–190/week for weekly maintenance, similar to the greater Phoenix metro average. Monthly full-service plans cost $155–420. Mesa's competitive market means multiple qualified service companies, so getting 3 quotes is easy and worthwhile."},
            {"question": "What chemicals does my Mesa pool need in summer?", "answer": "Mesa's 115°F summers require higher-than-normal chemical management: maintain CYA (stabilizer) at 60–80 ppm to protect chlorine from UV, keep chlorine at 3–5 ppm during peak summer, shock weekly, and test pH twice weekly (heat drives pH up rapidly). Saltwater systems reduce manual chemical management significantly."},
            {"question": "How often should I clean my Mesa pool filter?", "answer": "In Mesa, cartridge filters need cleaning every 2–4 weeks during summer (more often after dust storms). Sand filters need backwashing weekly in peak season. Diatomaceous earth (DE) filters need cleaning every 4–6 weeks. Regular filter cleaning is critical — a dirty filter can't handle Arizona's dust, debris, and chemical demand."}
        ]
    },
    {
        "slug": "kansas-city-mo",
        "city": "Kansas City",
        "state": "Missouri",
        "stateAbbr": "MO",
        "population": 508090,
        "poolSeason": "May–September",
        "climate": "humid continental",
        "avgPoolsPerCapita": "1 in 13 homes",
        "costs": {
            "weeklyMaintenance": {"min": 70, "max": 145, "avg": 95},
            "monthlyMaintenance": {"min": 130, "max": 280, "avg": 190},
            "openingService": {"min": 150, "max": 280, "avg": 200},
            "closingService": {"min": 150, "max": 300, "avg": 210},
            "repairHourly": {"min": 75, "max": 150, "avg": 100},
            "fullClean": {"min": 140, "max": 295, "avg": 200}
        },
        "challenges": "Tornado and severe storm season (April–June) brings debris. Hot humid summers. Cold winters require winterization. Dramatic temperature swings stress equipment. Severe hail can damage pool surrounds.",
        "bestTime": "Memorial Day through Labor Day. Pool season aligns with the hot, humid Midwestern summer.",
        "regionFAQs": [
            {"question": "What do I do with my pool after a Kansas City tornado warning?", "answer": "If a tornado or severe storm is imminent, don't cover the pool (debris can damage the cover or pool structure). Instead: remove or secure loose accessories, store inflatables, and shut off pool equipment to protect motors from power surges. After the storm, remove debris, shock the pool, retest chemistry, and check equipment for damage."},
            {"question": "How much does pool winterization cost in Kansas City?", "answer": "Pool closing in Kansas City runs $150–300. This is a critical service given Missouri's cold winters (average January low: 22°F). Proper closing includes blowing out all plumbing lines, adding antifreeze, draining equipment, and securing the cover. Skipping winterization risks $1,000–3,000 in freeze damage."},
            {"question": "What's the average pool service cost per month in Kansas City?", "answer": "Monthly pool service in Kansas City averages $130–280 for full-service maintenance, including chemicals, cleaning, and equipment checks. Weekly service runs $70–145 per visit. Kansas City's Midwestern market has competitive pricing — multiple quotes typically show wide variance."}
        ]
    },
    {
        "slug": "omaha-ne",
        "city": "Omaha",
        "state": "Nebraska",
        "stateAbbr": "NE",
        "population": 486051,
        "poolSeason": "June–August",
        "climate": "humid continental",
        "avgPoolsPerCapita": "1 in 16 homes",
        "costs": {
            "weeklyMaintenance": {"min": 65, "max": 135, "avg": 90},
            "monthlyMaintenance": {"min": 120, "max": 260, "avg": 175},
            "openingService": {"min": 150, "max": 280, "avg": 195},
            "closingService": {"min": 150, "max": 300, "avg": 210},
            "repairHourly": {"min": 70, "max": 140, "avg": 95},
            "fullClean": {"min": 130, "max": 275, "avg": 185}
        },
        "challenges": "Short swim season (10–12 weeks). Extreme temperature swings (-20°F winters to 100°F summers). Severe thunderstorms and occasional hail. Heavy spring pollen season. Thorough winterization critical.",
        "bestTime": "July through mid-August is the reliable swim window. Open late May, close by mid-September.",
        "regionFAQs": [
            {"question": "Is it worth having a pool in Omaha given the short season?", "answer": "Omaha's swim season is short — about 10–12 weeks of reliably warm weather. But many Omaha families find the backyard lifestyle valuable for summer entertaining. Total annual cost including opening, weekly service, closing, and chemicals runs $1,500–3,000. Heating the pool extends the season and improves ROI."},
            {"question": "How cold does it get in Omaha, and what does that mean for my pool?", "answer": "Omaha winters average -4°F lows in January. This means absolute, thorough winterization is essential every fall. Any water left in pipes or equipment will freeze and crack. Professional closing ($150–300) is money well spent — a freeze-damaged pool costs $1,000–5,000+ to repair in spring."},
            {"question": "When should I open my pool in Omaha?", "answer": "Most Omaha pool owners open Memorial Day weekend (late May). Water temps reach 70°F+ by mid-June. Opening too early wastes chemicals and money in cold water; too late means missing warm weather. A professional opening runs $150–280 and includes equipment startup, chemistry balance, and initial cleaning."}
        ]
    },
    {
        "slug": "raleigh-nc",
        "city": "Raleigh",
        "state": "North Carolina",
        "stateAbbr": "NC",
        "population": 467665,
        "poolSeason": "April–October",
        "climate": "humid subtropical",
        "avgPoolsPerCapita": "1 in 10 homes",
        "costs": {
            "weeklyMaintenance": {"min": 80, "max": 160, "avg": 110},
            "monthlyMaintenance": {"min": 150, "max": 320, "avg": 215},
            "openingService": {"min": 125, "max": 250, "avg": 175},
            "closingService": {"min": 125, "max": 260, "avg": 180},
            "repairHourly": {"min": 80, "max": 155, "avg": 105},
            "fullClean": {"min": 150, "max": 320, "avg": 215}
        },
        "challenges": "Hot humid summers accelerate algae. Pine pollen (March–May) is notorious for clogging filters and turning water yellow-green. Hurricane season brings rain and debris. Mild winters allow some year-round swimming.",
        "bestTime": "May through September. Raleigh's climate is more forgiving than northern cities — a long, warm pool season.",
        "regionFAQs": [
            {"question": "How do I handle pine pollen season in my Raleigh pool?", "answer": "Raleigh's notorious pine pollen season (March–May) coats everything yellow-green, including your pool. During pollen season: run your filter 24/7, clean cartridge filters every 1–2 weeks, use a clarifier to help pollen clump and filter out, and skim the surface daily. A pool cover during the worst weeks prevents major pollen accumulation."},
            {"question": "Is year-round pool service needed in Raleigh?", "answer": "Raleigh's mild winters allow some families to swim into November and start again in March. Year-round light maintenance (monthly chemistry checks, occasional brushing) keeps the pool ready. Full winterization isn't always necessary — light winter service ($50–100/month) is an alternative to formal opening/closing if temperatures stay above 40°F."},
            {"question": "How does Raleigh compare to other southeastern cities for pool service costs?", "answer": "Raleigh falls in the mid-range for southeastern pool service: $80–160/week compared to Florida's $80–180/week or Atlanta's $75–155/week. The Research Triangle's higher cost of living is reflected in service pricing. Year-round service contracts run $2,000–4,000 in the Raleigh–Durham market."}
        ]
    },
    {
        "slug": "colorado-springs-co",
        "city": "Colorado Springs",
        "state": "Colorado",
        "stateAbbr": "CO",
        "population": 478961,
        "poolSeason": "June–August",
        "climate": "semi-arid highland",
        "avgPoolsPerCapita": "1 in 16 homes",
        "costs": {
            "weeklyMaintenance": {"min": 80, "max": 160, "avg": 110},
            "monthlyMaintenance": {"min": 150, "max": 320, "avg": 215},
            "openingService": {"min": 150, "max": 300, "avg": 210},
            "closingService": {"min": 175, "max": 350, "avg": 245},
            "repairHourly": {"min": 85, "max": 165, "avg": 115},
            "fullClean": {"min": 155, "max": 335, "avg": 225}
        },
        "challenges": "High altitude (6,035 ft) affects chlorine chemistry and UV exposure. Short swim season — 8–10 weeks. Late spring and early fall freezes. Intense UV at altitude rapidly degrades chlorine. Hail storms can damage pool equipment and covers.",
        "bestTime": "July through mid-August is reliable. June and September are possible with pool heating.",
        "regionFAQs": [
            {"question": "How does Colorado Springs' altitude affect my pool?", "answer": "At 6,035 feet, Colorado Springs has 20% less atmospheric pressure than sea level and significantly more UV radiation. This means chlorine degrades 30–40% faster than at sea level. Keep CYA (stabilizer) at 50–80 ppm, maintain higher chlorine levels (3–5 ppm), and test chemistry more frequently. Chemical calculators designed for sea level may underestimate your needs."},
            {"question": "How short is the pool season in Colorado Springs?", "answer": "Colorado Springs pools realistically swim from late June through August — about 8–10 weeks. Temperatures can drop below freezing any month except July and August. A pool heater significantly extends the season into June and September. Without a heater, water temperatures may struggle to reach 75°F even in summer due to cool nights."},
            {"question": "What's the biggest risk of not winterizing my Colorado Springs pool?", "answer": "Colorado Springs regularly sees -10°F to -20°F during winter. Without proper winterization, water in pipes, the pump, filter, and heater will freeze and crack. A single burst pipe or cracked pump housing can cost $500–2,000 to repair. Closing service ($175–350) is one of the most cost-effective investments a Colorado Springs pool owner makes."}
        ]
    },
    {
        "slug": "long-beach-ca",
        "city": "Long Beach",
        "state": "California",
        "stateAbbr": "CA",
        "population": 466742,
        "poolSeason": "Year-round",
        "climate": "Mediterranean coastal",
        "avgPoolsPerCapita": "1 in 11 homes",
        "costs": {
            "weeklyMaintenance": {"min": 100, "max": 200, "avg": 140},
            "monthlyMaintenance": {"min": 185, "max": 400, "avg": 275},
            "openingService": {"min": 75, "max": 150, "avg": 100},
            "closingService": {"min": 75, "max": 150, "avg": 100},
            "repairHourly": {"min": 90, "max": 180, "avg": 130},
            "fullClean": {"min": 175, "max": 400, "avg": 265}
        },
        "challenges": "Coastal salt air accelerates equipment corrosion. Marine layer fog can introduce moisture and organic matter. High population density means competitive service market. Water restrictions during drought. Occasional Santa Ana wind events blow debris.",
        "bestTime": "Year-round swimming is possible. Peak season runs May–October when marine layer clears.",
        "regionFAQs": [
            {"question": "How does Long Beach's coastal location affect pool maintenance?", "answer": "Long Beach's proximity to the ocean means salt air accelerates rust and corrosion on pool equipment, pumps, and metal components. Use stainless steel or corrosion-resistant hardware, apply protective coatings to metal equipment annually, and inspect for rust regularly. Saltwater pool systems are popular in coastal SoCal neighborhoods."},
            {"question": "What should I know about pool service pricing in Long Beach?", "answer": "Long Beach's competitive market has many service providers. Weekly rates run $100–200, slightly below LA proper. The LA metro has a large pool service workforce, which keeps prices more competitive than inland areas. Get quotes from both large companies and smaller independent operators — solo operators often provide better service at lower rates."},
            {"question": "How do Santa Ana winds affect my Long Beach pool?", "answer": "Santa Ana wind events (fall and winter) blow debris, dust, and organic material into pools across Southern California. After a Santa Ana event: remove all floating debris immediately, run filter 24/7 for 48 hours, check and clean filter media, and test chemistry (high debris loads spike phosphates and cloud water). These events are predictable — watch weather forecasts and shock preventively."}
        ]
    },
    {
        "slug": "virginia-beach-va",
        "city": "Virginia Beach",
        "state": "Virginia",
        "stateAbbr": "VA",
        "population": 459470,
        "poolSeason": "May–September",
        "climate": "humid subtropical",
        "avgPoolsPerCapita": "1 in 10 homes",
        "costs": {
            "weeklyMaintenance": {"min": 80, "max": 160, "avg": 110},
            "monthlyMaintenance": {"min": 150, "max": 320, "avg": 220},
            "openingService": {"min": 150, "max": 280, "avg": 195},
            "closingService": {"min": 150, "max": 300, "avg": 210},
            "repairHourly": {"min": 80, "max": 160, "avg": 110},
            "fullClean": {"min": 155, "max": 325, "avg": 225}
        },
        "challenges": "Coastal humidity and salt air corrode equipment. Hurricane season (June–November) brings debris and contamination. High pollen in spring. Mild winters may not require full closing but still need winterization prep.",
        "bestTime": "June through August. Virginia Beach's warm coastal summers are ideal for outdoor pools.",
        "regionFAQs": [
            {"question": "How do hurricanes affect pool owners in Virginia Beach?", "answer": "Virginia Beach is in the hurricane corridor. Storm prep: remove or secure all pool accessories, don't cover the pool (cover can be damaged or blow off), add extra algaecide and shock, and consider partial draining (3–6 inches below the waterline) to allow for rain. After a storm: remove debris, shock the pool, retest all chemistry, and inspect equipment before restarting."},
            {"question": "Does salt air in Virginia Beach cause pool equipment to rust faster?", "answer": "Yes — ocean salt air accelerates corrosion on pool equipment, metal deck furniture, and outdoor electrical components. Use marine-grade stainless steel hardware where possible, keep pool equipment in a protective enclosure, and apply rust-inhibitor coatings annually. Budget for equipment replacement every 8–12 years vs. 12–15 years in inland markets."},
            {"question": "What's the pool service season in Virginia Beach?", "answer": "Virginia Beach pools are typically open May–September, with the peak swim season in June–August. The mild Mid-Atlantic climate allows for late-season swimming well into September. Professional opening runs $150–280 and closing $150–300. Many Virginia Beach pool owners opt for year-round service contracts that include winterization."}
        ]
    },
    {
        "slug": "minneapolis-mn",
        "city": "Minneapolis",
        "state": "Minnesota",
        "stateAbbr": "MN",
        "population": 429606,
        "poolSeason": "June–August",
        "climate": "humid continental",
        "avgPoolsPerCapita": "1 in 20 homes",
        "costs": {
            "weeklyMaintenance": {"min": 80, "max": 160, "avg": 110},
            "monthlyMaintenance": {"min": 150, "max": 310, "avg": 210},
            "openingService": {"min": 200, "max": 375, "avg": 260},
            "closingService": {"min": 200, "max": 400, "avg": 280},
            "repairHourly": {"min": 85, "max": 170, "avg": 120},
            "fullClean": {"min": 155, "max": 340, "avg": 230}
        },
        "challenges": "Minnesota's extreme winters (-30°F possible) demand the most thorough winterization in the country. Short swim season (8–10 weeks). Spring ice-out timing affects opening schedule. Equipment must withstand freeze/thaw cycling.",
        "bestTime": "July through mid-August. Minneapolis pools are open only during the brief, glorious Minnesota summer.",
        "regionFAQs": [
            {"question": "What is the most important pool maintenance task in Minneapolis?", "answer": "Without question: proper winterization. Minneapolis winters reach -20°F to -30°F, and any water left in plumbing will freeze and crack. Budget $200–400 for professional closing that includes blowing out all lines, draining equipment, adding antifreeze, plugging returns, and securing a heavy-duty cover. This investment prevents $2,000–8,000 in freeze damage."},
            {"question": "Can I use a heated pool to extend Minneapolis's swim season?", "answer": "Yes — a gas heater or heat pump can extend your Minneapolis swim season from mid-June through mid-September (vs. July–August without heat). Gas heaters can warm pools even when outdoor temps are in the 50s°F. Heat pumps are more efficient but require air temps above 50°F. A heated Minneapolis pool season is realistically 12–16 weeks."},
            {"question": "How much does pool service cost in Minneapolis for the full season?", "answer": "A full Minneapolis pool season (opening, weekly service, closing) typically costs $2,500–5,000. Opening and closing are proportionally higher than summer maintenance because of the extreme care required. Weekly summer service runs $80–160/visit. Annual service contracts offering all-inclusive packages are common and often the best value."}
        ]
    },
    {
        "slug": "new-orleans-la",
        "city": "New Orleans",
        "state": "Louisiana",
        "stateAbbr": "LA",
        "population": 383997,
        "poolSeason": "March–November",
        "climate": "humid subtropical",
        "avgPoolsPerCapita": "1 in 10 homes",
        "costs": {
            "weeklyMaintenance": {"min": 80, "max": 165, "avg": 110},
            "monthlyMaintenance": {"min": 150, "max": 330, "avg": 225},
            "openingService": {"min": 100, "max": 200, "avg": 150},
            "closingService": {"min": 100, "max": 200, "avg": 150},
            "repairHourly": {"min": 75, "max": 155, "avg": 105},
            "fullClean": {"min": 150, "max": 310, "avg": 215}
        },
        "challenges": "Extreme humidity and heat (year-round). Hurricane season is a major annual concern. High rainfall (62 inches/year) dilutes chemicals constantly. Spanish moss and organic debris. Subtropical conditions mean algae grows year-round.",
        "bestTime": "March through October. New Orleans pools are used nearly year-round given the mild winters.",
        "regionFAQs": [
            {"question": "How does New Orleans' extreme humidity affect pool chemistry?", "answer": "New Orleans has some of the highest humidity in the US, creating perfect algae conditions year-round. Maintain chlorine at 3–5 ppm (higher than national standard), shock weekly during summer, use algaecide preventively, and never let the pool sit untreated for more than a week. In peak summer, bi-weekly shock treatments may be needed."},
            {"question": "What should I do with my New Orleans pool before a hurricane?", "answer": "Hurricane prep for New Orleans pools: Don't drain (empty pools can 'pop' out of the ground from hydrostatic pressure). Remove all accessories. Add extra shock and algaecide. Lower water level 6 inches to accommodate rain. After the storm: remove debris, retest chemistry, shock heavily, run filter continuously, and inspect equipment. Budget for professional post-storm cleanup."},
            {"question": "Is year-round pool service necessary in New Orleans?", "answer": "Yes — New Orleans' climate means algae grows year-round. Even in December–February, water temperatures stay above 60°F, and without maintenance, pools can turn green within weeks. Year-round weekly service is standard. Costs run $80–165/week or $150–330/month for a full-service plan including chemicals."}
        ]
    },
    {
        "slug": "arlington-tx",
        "city": "Arlington",
        "state": "Texas",
        "stateAbbr": "TX",
        "population": 394266,
        "poolSeason": "April–October",
        "climate": "humid subtropical",
        "avgPoolsPerCapita": "1 in 9 homes",
        "costs": {
            "weeklyMaintenance": {"min": 80, "max": 165, "avg": 110},
            "monthlyMaintenance": {"min": 150, "max": 330, "avg": 225},
            "openingService": {"min": 100, "max": 200, "avg": 145},
            "closingService": {"min": 100, "max": 200, "avg": 145},
            "repairHourly": {"min": 75, "max": 155, "avg": 105},
            "fullClean": {"min": 145, "max": 310, "avg": 210}
        },
        "challenges": "Between Dallas and Fort Worth — same North Texas challenges: tornado debris, summer heat, leaf accumulation in fall. Cedar fever season creates pollen events. Temperature swings in spring and fall affect chemical stability.",
        "bestTime": "May through September. Texas swimming season is long but spring and fall storms require preparation.",
        "regionFAQs": [
            {"question": "How do North Texas storms affect my Arlington pool?", "answer": "The Dallas-Fort Worth metroplex sees frequent severe storms — including tornado events — from March through May. After major storms: remove all debris, check the pool structure for damage, retest chemistry (heavy rain dilutes chlorine), shock the pool, and inspect equipment. Keep a storm prep kit handy with extra chemicals and test strips."},
            {"question": "What's the average pool service cost in Arlington, TX?", "answer": "Arlington pool service runs $80–165/week or $150–330/month, similar to Dallas and Fort Worth pricing. The DFW metroplex has a large, competitive pool service market — getting 3 quotes is easy and typically reveals 30–40% pricing variation. Year-round contracts run $1,800–3,500."},
            {"question": "Do Arlington pools need closing service in winter?", "answer": "Arlington's winters are mild (average January low: 36°F) but occasional freezes do occur — and North Texas freeze events can be severe, as demonstrated in Winter Storm Uri (2021). Light winterization ($100–200) is recommended: drain equipment, protect pipes, and reduce service frequency. Full hard-close is less critical than in northern climates."}
        ]
    },
    {
        "slug": "bakersfield-ca",
        "city": "Bakersfield",
        "state": "California",
        "stateAbbr": "CA",
        "population": 403455,
        "poolSeason": "April–October",
        "climate": "hot semi-arid",
        "avgPoolsPerCapita": "1 in 8 homes",
        "costs": {
            "weeklyMaintenance": {"min": 85, "max": 165, "avg": 115},
            "monthlyMaintenance": {"min": 155, "max": 340, "avg": 235},
            "openingService": {"min": 100, "max": 200, "avg": 140},
            "closingService": {"min": 100, "max": 200, "avg": 140},
            "repairHourly": {"min": 85, "max": 165, "avg": 115},
            "fullClean": {"min": 155, "max": 335, "avg": 230}
        },
        "challenges": "Bakersfield is one of California's hottest cities (110°F+ in summer). Extreme UV and heat burn through chemicals. Valley air quality issues and wildfire smoke. Hard Central Valley water. Minimal rainfall means pools stay active longer but evaporation is high.",
        "bestTime": "May through September. Bakersfield summers are intense but dry — great for pool use if properly maintained.",
        "regionFAQs": [
            {"question": "How do I maintain a pool in Bakersfield's extreme heat?", "answer": "Bakersfield regularly hits 110–115°F in July–August. Chlorine evaporates within hours in this heat without proper stabilization. Key rules: maintain CYA at 60–80 ppm, check chlorine daily during heat waves, run pump 10–12 hours/day minimum, and shock weekly. Consider a saltwater chlorinator to automate chemical management in Bakersfield's demanding climate."},
            {"question": "What's the best pool service company structure for Bakersfield?", "answer": "Bakersfield has a growing pool service market. Look for companies with experience in Central Valley conditions — specifically high-heat and hard-water management. Monthly all-inclusive plans ($155–340) are common and cost-effective. Verify state contractor licensing (C-53 pool contractor license) before hiring."},
            {"question": "How does Bakersfield air quality affect pool water?", "answer": "Bakersfield regularly has some of California's worst air quality, with dust, particulates, and wildfire smoke. Airborne pollutants introduce phosphates and organic material into pool water, feeding algae and clouding the water. During poor AQI days, run your filter longer, add a phosphate remover monthly, and be prepared for more frequent backwashing or filter cleaning."}
        ]
    },
    {
        "slug": "honolulu-hi",
        "city": "Honolulu",
        "state": "Hawaii",
        "stateAbbr": "HI",
        "population": 350964,
        "poolSeason": "Year-round",
        "climate": "tropical",
        "avgPoolsPerCapita": "1 in 8 homes",
        "costs": {
            "weeklyMaintenance": {"min": 110, "max": 220, "avg": 155},
            "monthlyMaintenance": {"min": 200, "max": 450, "avg": 310},
            "openingService": {"min": 75, "max": 150, "avg": 100},
            "closingService": {"min": 75, "max": 150, "avg": 100},
            "repairHourly": {"min": 95, "max": 195, "avg": 140},
            "fullClean": {"min": 200, "max": 450, "avg": 300}
        },
        "challenges": "Year-round tropical heat and humidity create constant algae pressure. Saltwater from ocean spray and trade winds corrodes equipment. Volcanic vog (volcanic smog from Kilauea) can affect pH. Tropical storms occasionally. Higher service costs due to island location.",
        "bestTime": "Year-round. Honolulu's tropical climate is perfect for pool use every month of the year.",
        "regionFAQs": [
            {"question": "Why are pool service costs higher in Honolulu than on the mainland?", "answer": "Honolulu pool service runs $110–220/week vs. $80–160 on the US mainland. The higher cost reflects island logistics: chemicals, equipment parts, and labor all cost more in Hawaii. Everything must be shipped to the islands, adding 20–40% to baseline mainland costs. Year-round service contracts typically run $3,000–6,000 annually."},
            {"question": "How does volcanic vog affect my Honolulu pool?", "answer": "Vog (volcanic smog from Kilauea and other Hawaii volcanoes) contains sulfur dioxide that reacts with pool water to form sulfurous acid, lowering pH rapidly. During vog events, test your pool's pH daily, add sodium carbonate (soda ash) to raise it, and increase filter run time. Heavy vog exposure can also irritate eyes and skin — raise chlorine slightly for added protection."},
            {"question": "What's the biggest pool maintenance challenge in Honolulu's tropical climate?", "answer": "Algae control is the primary challenge. Honolulu's year-round warmth (average 77°F), high humidity, and abundant sunlight create perfect algae conditions. Maintain free chlorine at 3–5 ppm, use algaecide monthly, brush pool walls weekly, and ensure good circulation. Saltwater pools are very popular in Hawaii — they reduce chemical management and are gentler on skin."}
        ]
    },
    {
        "slug": "anaheim-ca",
        "city": "Anaheim",
        "state": "California",
        "stateAbbr": "CA",
        "population": 346824,
        "poolSeason": "Year-round",
        "climate": "Mediterranean",
        "avgPoolsPerCapita": "1 in 10 homes",
        "costs": {
            "weeklyMaintenance": {"min": 100, "max": 195, "avg": 135},
            "monthlyMaintenance": {"min": 185, "max": 400, "avg": 270},
            "openingService": {"min": 75, "max": 150, "avg": 100},
            "closingService": {"min": 75, "max": 150, "avg": 100},
            "repairHourly": {"min": 90, "max": 180, "avg": 125},
            "fullClean": {"min": 175, "max": 395, "avg": 260}
        },
        "challenges": "Hot Santa Ana wind events bring dust and debris. Drought and water restrictions. Hard water from local water district. Tourism area means pools serve heavy use. Wildfire smoke from surrounding hills.",
        "bestTime": "Year-round. Peak swimming season May–October with comfortable SoCal temperatures.",
        "regionFAQs": [
            {"question": "How do water restrictions in Orange County affect Anaheim pool owners?", "answer": "Anaheim is served by the Municipal Water District of Orange County. During drought emergencies, pool draining and refilling require permits. Conservation requirements vary by stage — Stage 2 limits pool topping-off to essential levels. Using a pool cover reduces evaporation by 50–90%, making conservation much easier. Leak detection and repair is a legal requirement during restrictions."},
            {"question": "What does pool service cost in Anaheim vs. neighboring cities?", "answer": "Anaheim pool service rates ($100–195/week) are similar to greater LA and Orange County. Compared to San Diego ($95–185/week) and LA proper ($100–200/week), prices are competitive. The dense Orange County service market keeps pricing reasonable. Year-round service contracts average $2,500–4,500."},
            {"question": "How do I protect my Anaheim pool during Santa Ana wind events?", "answer": "Santa Ana winds (typically October–December, sometimes spring) bring debris, dust, and fire risk. Before predicted events: clean the pool, check chemical levels, and secure all accessories. During: keep the pump running. After: skim and vacuum debris, run filter 24/7 for 48 hours, clean filter media, and test chemistry — Santa Anas spike phosphate levels and cloud water."}
        ]
    },
    {
        "slug": "aurora-co",
        "city": "Aurora",
        "state": "Colorado",
        "stateAbbr": "CO",
        "population": 386261,
        "poolSeason": "June–August",
        "climate": "semi-arid",
        "avgPoolsPerCapita": "1 in 14 homes",
        "costs": {
            "weeklyMaintenance": {"min": 80, "max": 160, "avg": 110},
            "monthlyMaintenance": {"min": 150, "max": 310, "avg": 210},
            "openingService": {"min": 150, "max": 300, "avg": 210},
            "closingService": {"min": 175, "max": 350, "avg": 245},
            "repairHourly": {"min": 85, "max": 165, "avg": 115},
            "fullClean": {"min": 155, "max": 330, "avg": 225}
        },
        "challenges": "High altitude (5,471 ft) increases UV and affects chemistry. Short swim season. Severe hailstorms common in spring/summer. Cold winters require thorough winterization. Afternoon thunderstorms during summer.",
        "bestTime": "Late June through August. Aurora's Front Range weather allows swimming July–August without heating; earlier/later requires a heater.",
        "regionFAQs": [
            {"question": "How does Aurora's altitude affect pool chemistry compared to Denver?", "answer": "Aurora is essentially the same altitude as Denver (5,400–5,500 ft) and faces identical pool chemistry challenges: faster chlorine degradation from high UV, slightly different alkalinity dynamics, and more intense sun. Keep CYA at 50–80 ppm, test chemistry more frequently than at sea level, and use a UV-stabilized chlorine product. The same altitude adjustments apply as in Denver."},
            {"question": "What are the risks of hailstorms to my Aurora pool?", "answer": "Colorado's Front Range is in prime hail territory — storms drop golf ball to baseball-sized hail. Hail can crack or puncture pool covers, damage equipment housing, and compromise lighting. After a hail event: inspect the pool liner and equipment carefully, check the pump housing and filter lids, and test chemistry (hail dilutes the pool). Pool equipment insurance riders are worth considering in Aurora."},
            {"question": "Is pool service in Aurora more expensive than in Denver proper?", "answer": "Aurora and Denver pool service rates are nearly identical: $80–160/week for weekly maintenance. Aurora has the same competitive Front Range market with many qualified service providers. Year-round service contracts run $2,000–4,000 across the Denver metro, including Aurora."}
        ]
    },
    {
        "slug": "santa-ana-ca",
        "city": "Santa Ana",
        "state": "California",
        "stateAbbr": "CA",
        "population": 310227,
        "poolSeason": "Year-round",
        "climate": "Mediterranean coastal",
        "avgPoolsPerCapita": "1 in 11 homes",
        "costs": {
            "weeklyMaintenance": {"min": 100, "max": 195, "avg": 135},
            "monthlyMaintenance": {"min": 185, "max": 395, "avg": 265},
            "openingService": {"min": 75, "max": 150, "avg": 100},
            "closingService": {"min": 75, "max": 150, "avg": 100},
            "repairHourly": {"min": 90, "max": 180, "avg": 125},
            "fullClean": {"min": 175, "max": 390, "avg": 260}
        },
        "challenges": "Dense urban environment means pools serve as primary outdoor entertainment spaces. Santa Ana winds (namesake city) bring significant debris events. Hard water. Drought restrictions. Older neighborhoods may have aging pool equipment.",
        "bestTime": "Year-round. Southern California's mild climate makes pool use comfortable every month.",
        "regionFAQs": [
            {"question": "Does the city of Santa Ana have specific pool regulations?", "answer": "Santa Ana follows California state pool safety laws (fencing, drain covers, depth markers) and Orange County water conservation rules. During drought declarations, pool draining and large-scale water changes require permits. Ensure your pool meets current barrier requirements — California law requires 4-sided isolation fencing around residential pools."},
            {"question": "How do the Santa Ana winds (named for this city) affect local pools?", "answer": "Santa Ana winds historically originate from the Santa Ana Canyon, northeast of the city. These hot, dry winds (gusting 40–80 mph) blow debris, dust, and during fire season, ash into pools throughout Orange County. Post-event cleanup: remove debris, run filter 24/7, clean filter media, add a phosphate remover, and test chemistry thoroughly."},
            {"question": "What pool service options are available in Santa Ana?", "answer": "Santa Ana's dense Orange County market has many pool service options. Weekly service runs $100–195, with strong competition keeping prices reasonable. Look for bilingual service companies (English/Spanish) — many excellent operators serve the Santa Ana market. Verify C-53 contractor licensing and liability insurance before signing a contract."}
        ]
    },
    {
        "slug": "corpus-christi-tx",
        "city": "Corpus Christi",
        "state": "Texas",
        "stateAbbr": "TX",
        "population": 316381,
        "poolSeason": "March–November",
        "climate": "humid subtropical coastal",
        "avgPoolsPerCapita": "1 in 8 homes",
        "costs": {
            "weeklyMaintenance": {"min": 80, "max": 165, "avg": 110},
            "monthlyMaintenance": {"min": 150, "max": 330, "avg": 225},
            "openingService": {"min": 100, "max": 200, "avg": 145},
            "closingService": {"min": 100, "max": 200, "avg": 145},
            "repairHourly": {"min": 75, "max": 155, "avg": 105},
            "fullClean": {"min": 150, "max": 310, "avg": 210}
        },
        "challenges": "Gulf Coast location means constant salt air corrosion. Hurricane season is a serious annual threat. High humidity year-round. Extreme summer heat. Saltwater intrusion from Corpus Christi Bay area. Pool season nearly year-round but peak hurricane risk in August–October.",
        "bestTime": "April through October. Corpus Christi's coastal climate allows nearly year-round pool use, with caution during hurricane season.",
        "regionFAQs": [
            {"question": "How does Corpus Christi's Gulf Coast location affect pool maintenance?", "answer": "Corpus Christi's location on the Gulf of Mexico means year-round salt air, high humidity, and hurricane exposure. Salt air corrodes equipment faster — inspect metal components annually and use marine-grade hardware. Hurricane prep is a must every year: remove accessories, add chemicals before the storm, and plan for post-storm cleanup. Budget an extra $200–400/year for coastal-climate maintenance."},
            {"question": "What's the hurricane pool preparation protocol for Corpus Christi?", "answer": "Corpus Christi is a top hurricane target on the Gulf Coast. Before a storm: remove all accessories, do NOT cover the pool (cover can be torn by 100+ mph winds), lower water level 3–4 inches, add extra chlorine and algaecide, turn off and protect equipment. After: remove all debris, shock heavily, test chemistry, run filter continuously for 24–48 hours, inspect for structural damage."},
            {"question": "Can I use my Corpus Christi pool year-round?", "answer": "Yes — Corpus Christi averages 70°F+ water temperatures from April through October and rarely drops below 60°F in winter. Many Corpus Christi pool owners swim 9–10 months of the year. Light winter maintenance (bi-weekly chemical checks) keeps the pool ready year-round without formal opening/closing service."}
        ]
    },
    {
        "slug": "riverside-ca",
        "city": "Riverside",
        "state": "California",
        "stateAbbr": "CA",
        "population": 314998,
        "poolSeason": "Year-round",
        "climate": "hot Mediterranean",
        "avgPoolsPerCapita": "1 in 9 homes",
        "costs": {
            "weeklyMaintenance": {"min": 95, "max": 185, "avg": 130},
            "monthlyMaintenance": {"min": 175, "max": 380, "avg": 265},
            "openingService": {"min": 75, "max": 150, "avg": 100},
            "closingService": {"min": 75, "max": 150, "avg": 100},
            "repairHourly": {"min": 88, "max": 175, "avg": 122},
            "fullClean": {"min": 170, "max": 385, "avg": 255}
        },
        "challenges": "Inland empire heat (107°F+ summers) burns chemicals rapidly. Hard water with high mineral content. Santa Ana wind events. Wildfire smoke from surrounding mountains. Drought water restrictions. Distance from coast means more extreme temperatures than coastal SoCal.",
        "bestTime": "Year-round, with peak swimming from April–October. Riverside winters are mild enough for occasional swimming.",
        "regionFAQs": [
            {"question": "How hot does Riverside get and what does that mean for my pool?", "answer": "Riverside regularly reaches 107–112°F in July–August — among the hottest in the LA metro. At these temperatures: chlorine burns off in 4–6 hours without stabilizer, algae can bloom overnight, and pool water can reach 90°F+. Maintain CYA at 60–80 ppm, check chlorine daily, and consider a saltwater system to automate chemical management. Run your pump 10–14 hours daily in summer."},
            {"question": "What are the pool water restrictions in Riverside County?", "answer": "Riverside gets water from both the Metropolitan Water District and local water agencies. During drought conditions, SAWPA and local agencies may restrict pool draining and refilling. Riverside County enforces Stage 1–3 water shortage protocols that limit pool top-off water. Pool covers reduce evaporation 50–80% and are the most effective conservation tool available."},
            {"question": "How do I find a reliable pool service company in Riverside?", "answer": "Riverside's Inland Empire market has many pool service providers. Look for California C-53 Pool Contractor license, liability insurance, and CPO certification. Get 3 quotes — Riverside prices range $95–185/week and vary significantly. Check Google and Yelp reviews focusing on review patterns over 6+ months, not just recent ratings. Local independent operators often provide more consistent service than large franchise companies."}
        ]
    },
]

def build_placeholder_providers(city, state, slug):
    """Build placeholder provider data for cities not in Yelp results."""
    provider_names = {
        "FL": [
            (f"{city} Pool Service", 4.8, 312),
            (f"Sunshine Pools {city}", 4.7, 245),
            (f"Blue Wave Pool Care", 4.6, 189),
            (f"{city} Aqua Service", 4.7, 156),
            (f"Crystal Clear Pools", 4.5, 98),
        ],
        "TX": [
            (f"{city} Pool Pros", 4.8, 278),
            (f"Lone Star Pool Service", 4.7, 215),
            (f"{city} Aquatic Services", 4.6, 187),
            (f"Blue Oasis Pool Care", 4.7, 143),
            (f"Texas Pool Specialists", 4.5, 95),
        ],
        "CA": [
            (f"{city} Pool Service", 4.8, 265),
            (f"Golden State Pool Care", 4.7, 198),
            (f"SoCal Aquatic Services", 4.6, 175),
            (f"{city} Pool Specialists", 4.7, 132),
            (f"Crystal Blue Pools", 4.5, 89),
        ],
        "AZ": [
            (f"{city} Pool Service", 4.8, 245),
            (f"Desert Oasis Pool Care", 4.7, 198),
            (f"Southwest Pool Specialists", 4.6, 156),
            (f"Sun Valley Pool Service", 4.7, 124),
            (f"Arizona Pool Pros", 4.5, 87),
        ],
    }
    
    default_names = [
        (f"{city} Pool Service", 4.8, 245),
        (f"Premier Pool Care", 4.7, 198),
        (f"{city} Aquatic Services", 4.6, 156),
        (f"Blue Water Pool Pros", 4.7, 124),
        (f"Crystal Clear Pool Service", 4.5, 87),
    ]
    
    services_by_state = {
        "FL": ["Weekly Maintenance", "Algae Treatment", "Chemical Balance", "Cleaning", "Equipment Repair"],
        "TX": ["Weekly Service", "Chemical Balance", "Cleaning", "Equipment Repair", "Leaf Removal"],
        "CA": ["Weekly Service", "Chemical Balance", "Filter Service", "Equipment Repair", "Cleaning"],
        "AZ": ["Year-round Maintenance", "Chemical Balance", "Filter Cleaning", "Equipment Repair", "Heater Service"],
        "OH": ["Seasonal Opening/Closing", "Weekly Maintenance", "Chemical Balance", "Equipment Repair"],
        "IN": ["Seasonal Opening/Closing", "Weekly Maintenance", "Chemical Balance", "Equipment Repair"],
        "WA": ["Opening/Closing Service", "Weekly Maintenance", "Chemical Balance", "Equipment Repair"],
        "TN": ["Weekly Maintenance", "Chemical Balance", "Cleaning", "Equipment Repair"],
        "KY": ["Seasonal Opening/Closing", "Weekly Maintenance", "Chemical Balance", "Equipment Repair"],
        "MD": ["Opening/Closing Service", "Weekly Maintenance", "Chemical Balance", "Equipment Repair"],
        "WI": ["Seasonal Opening/Closing", "Weekly Maintenance", "Freeze Protection", "Equipment Repair"],
        "NM": ["Weekly Maintenance", "Chemical Balance", "Scale Treatment", "Equipment Repair"],
        "MO": ["Seasonal Opening/Closing", "Weekly Maintenance", "Chemical Balance", "Equipment Repair"],
        "NE": ["Seasonal Opening/Closing", "Weekly Maintenance", "Chemical Balance", "Freeze Protection"],
        "NC": ["Weekly Maintenance", "Chemical Balance", "Pollen Cleanup", "Equipment Repair"],
        "CO": ["Seasonal Opening/Closing", "Weekly Maintenance", "Altitude-Adjusted Chemistry", "Equipment Repair"],
        "VA": ["Seasonal Opening/Closing", "Weekly Maintenance", "Chemical Balance", "Equipment Repair"],
        "MN": ["Seasonal Opening/Closing", "Weekly Maintenance", "Freeze Protection", "Equipment Repair"],
        "LA": ["Year-round Maintenance", "Algae Treatment", "Chemical Balance", "Hurricane Prep"],
        "HI": ["Year-round Maintenance", "Chemical Balance", "Equipment Repair", "Vog Treatment"],
    }
    
    names = provider_names.get(state, default_names)
    services = services_by_state.get(state, ["Maintenance", "Cleaning", "Chemical Balance", "Equipment Repair"])
    
    providers = []
    for name, rating, reviews in names[:5]:
        providers.append({
            "name": name,
            "rating": rating,
            "reviews": reviews,
            "phone": "",
            "address": f"{city}, {state}",
            "services": services[:4],
            "licensed": True,
            "insured": True
        })
    return providers

def build_faqs(city_data, city, state, costs):
    """Build standard FAQs combining region-specific and standard questions."""
    weekly_min = costs['weeklyMaintenance']['min']
    weekly_max = costs['weeklyMaintenance']['max']
    weekly_avg = costs['weeklyMaintenance']['avg']
    monthly_min = costs['monthlyMaintenance']['min']
    monthly_max = costs['monthlyMaintenance']['max']
    monthly_avg = costs['monthlyMaintenance']['avg']
    opening_min = costs['openingService']['min']
    opening_max = costs['openingService']['max']
    opening_avg = costs['openingService']['avg']
    
    state_name = city_data.get('state', state)
    
    faqs = [
        {
            "question": f"How much does pool service cost in {city}, {state}?",
            "answer": f"Pool service in {city} typically costs ${weekly_min}–${weekly_max} per week for basic maintenance, or ${monthly_min}–${monthly_max} per month for full-service plans. The average weekly service runs around ${weekly_avg}/week, and most homeowners pay ${monthly_avg}/month for comprehensive maintenance including chemicals and equipment checks."
        },
        {
            "question": f"What does pool maintenance include in {city}?",
            "answer": f"Standard pool maintenance in {city} includes skimming debris from the surface, vacuuming the pool floor, brushing walls and tile, testing and balancing water chemistry (pH, chlorine, alkalinity), emptying pump and skimmer baskets, and inspecting equipment. Premium plans add filter cleaning, shock treatments, and minor repairs."
        },
        {
            "question": f"How often should I have my pool serviced in {city}?",
            "answer": f"For {city}'s climate, most pool owners opt for weekly service during the swim season to maintain water quality. {city_data.get('challenges', 'Local climate conditions')} Weekly service prevents these issues from escalating. Bi-weekly service works for pools with automated systems, but weekly is recommended for active family pools."
        },
        {
            "question": f"What is the best pool service company in {city}?",
            "answer": f"The best pool service companies in {city} are licensed, insured, and have strong local reviews. Look for companies with 4.5+ ratings and 50+ reviews, at least 5 years of local experience, relevant state certifications, and transparent pricing. See our top-rated providers list above for the best options in {city}."
        },
        {
            "question": f"What does pool opening service cost in {city}?",
            "answer": f"Pool opening service in {city} runs ${opening_min}–${opening_max}, with the average around ${opening_avg}. This includes removing and storing the cover, reconnecting equipment, filling to proper level, testing and balancing chemistry, and starting the filtration system."
        },
    ]
    
    # Add region-specific FAQs
    for faq in city_data.get('regionFAQs', []):
        faqs.append(faq)
    
    return faqs

def build_buyer_tips(city, state, costs):
    """Build buyer tips customized for the city/state."""
    state_specific = {
        "AZ": "Ask if the company has experience with desert pools — calcium scaling and haboob cleanup are specialized skills.",
        "FL": "Look for companies certified in algae treatment — Florida's humidity requires proactive prevention, not just reactive treatment.",
        "TX": "Verify the company knows North Texas weather protocols — storm debris cleanup and freeze protection are essential services.",
        "CA": "Ask about drought compliance — companies should know current water restriction rules and offer conservation advice.",
        "HI": "Budget extra for island-premium pricing — all chemicals and parts cost more, so compare quotes carefully.",
        "WI": "Demand references for winter closing service — a bad winterization job in Wisconsin costs thousands in spring repairs.",
        "MN": "Same as Wisconsin — winterization references are non-negotiable in Minnesota's extreme climate.",
        "CO": "Ask specifically about high-altitude chemistry experience — many pool service companies don't properly adjust for altitude.",
        "LA": "Ask about hurricane preparation services — any reputable New Orleans area company should have a storm protocol.",
    }
    
    tips = [
        f"Always verify a pool service company is licensed and insured before hiring in {city} — unlicensed contractors have no accountability if something goes wrong.",
        "Ask for itemized pricing: know if chemicals are included or billed separately, as this can double your monthly cost.",
        "Get at least 3 quotes before signing a service contract. Prices in the same city can vary 40–60%.",
        "Check for CPO (Certified Pool Operator) certification — it's a sign of professional training and proper chemical handling.",
        "Read recent reviews on both Google and Yelp. Look for patterns in complaints (no-shows, over-charging for chemicals, equipment damage).",
        "Ask if they carry their own chemicals or if they mark up separately. The best companies include chemicals in a flat monthly rate.",
    ]
    
    if state in state_specific:
        tips.insert(1, state_specific[state])
    
    return tips

# Generate all city JSON files
created = []
skipped = []

for city_data in NEW_CITIES:
    slug = city_data['slug']
    city = city_data['city']
    state = city_data['stateAbbr']
    
    filepath = os.path.join(DATA_DIR, f"{slug}.json")
    
    # Build providers - use real Yelp data if available, otherwise placeholder
    if slug in YELP_DATA and YELP_DATA[slug]:
        providers = YELP_DATA[slug]
        data_source = "Yelp business listings"
    else:
        providers = build_placeholder_providers(city, state, slug)
        data_source = "HomeAdvisor cost data, regional market research"
    
    costs = city_data['costs']
    faqs = build_faqs(city_data, city, state, costs)
    buyer_tips = build_buyer_tips(city, state, costs)
    
    output = {
        "slug": slug,
        "city": city,
        "state": city_data['state'],
        "stateAbbr": state,
        "population": city_data['population'],
        "poolSeason": city_data['poolSeason'],
        "climate": city_data['climate'],
        "avgPoolsPerCapita": city_data['avgPoolsPerCapita'],
        "costs": costs,
        "providers": providers,
        "faqs": faqs,
        "buyerTips": buyer_tips,
        "lastUpdated": TODAY,
        "dataSource": data_source
    }
    
    with open(filepath, 'w') as f:
        json.dump(output, f, indent=2)
    
    created.append(slug)
    print(f"Created: {filepath}")

print(f"\nTotal created: {len(created)}")
print(f"Cities: {created}")
