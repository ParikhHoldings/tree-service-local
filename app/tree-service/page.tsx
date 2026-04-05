import type { Metadata } from 'next'
import Link from 'next/link'
import citiesIndex from '@/data/cities/cities-index.json'

export const metadata: Metadata = {
  title: 'Tree Service Companies by City — Find Local Lawn Care Near You',
  description: 'Compare top-rated tree-service and lawn care companies in 50+ US cities. Real prices on mowing, design, tree trimming, and sprinkler install. Licensed, insured, free quotes.',
}

const STATE_NAMES: Record<string, string> = {
  TX: 'Texas', AZ: 'Arizona', NV: 'Nevada', GA: 'Georgia', NC: 'North Carolina',
  TN: 'Tennessee', FL: 'Florida', AL: 'Alabama', KY: 'Kentucky',
  IL: 'Illinois', IN: 'Indiana', OH: 'Ohio', MO: 'Missouri', MN: 'Minnesota',
  WI: 'Wisconsin', MI: 'Michigan', PA: 'Pennsylvania', MD: 'Maryland',
  DC: 'Dist. of Columbia', VA: 'Virginia', CO: 'Colorado', NM: 'New Mexico',
  UT: 'Utah', CA: 'California', OR: 'Oregon', WA: 'Washington',
  LA: 'Louisiana', OK: 'Oklahoma', NE: 'Nebraska',
}

const citiesByState = citiesIndex.reduce((acc, city) => {
  if (!acc[city.stateAbbr]) acc[city.stateAbbr] = []
  acc[city.stateAbbr].push(city)
  return acc
}, {} as Record<string, typeof citiesIndex>)

export default function Tree ServiceDirectoryPage() {
  return (
    <main className="py-12 px-4">
      <div className="max-w-6xl mx-auto">
        <div className="mb-10">
          <div className="inline-flex items-center gap-2 bg-green-50 border border-green-200 rounded-full px-4 py-1.5 text-sm text-green-700 font-medium mb-4">
            🌿 Serving 50 cities · Spring season now
          </div>
          <h1 className="text-3xl font-bold mb-3 text-gray-900">Tree Service Companies by City</h1>
          <p className="text-gray-600 text-lg max-w-2xl">Find the best local landscapers in your city. Compare pricing on lawn mowing, yard design, tree trimming, and irrigation. Licensed, insured, and rated.</p>
        </div>

        {Object.entries(citiesByState).sort(([a], [b]) => a.localeCompare(b)).map(([stateAbbr, cities]) => (
          <div key={stateAbbr} className="mb-10">
            <h2 className="text-xl font-bold mb-4 text-gray-900 border-b border-gray-200 pb-2">
              Tree Service in {STATE_NAMES[stateAbbr] || stateAbbr}
            </h2>
            <div className="grid md:grid-cols-2 lg:grid-cols-3 gap-4">
              {cities.map(city => (
                <Link key={city.slug} href={`/tree-service/${city.slug}`}
                  className="flex items-center justify-between bg-white rounded-lg border border-gray-200 px-5 py-4 hover:border-green-400 hover:shadow-sm transition-all group">
                  <div>
                    <span className="font-medium group-hover:text-green-700 transition-colors">Tree Service in {city.city}</span>
                    <div className="text-xs text-gray-500 mt-0.5">Top rated · Free quotes</div>
                  </div>
                  <span className="text-gray-300 group-hover:text-green-400 transition-colors">→</span>
                </Link>
              ))}
            </div>
          </div>
        ))}
      </div>
    </main>
  )
}
