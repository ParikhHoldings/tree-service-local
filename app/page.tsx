import type { Metadata } from 'next'
import Link from 'next/link'
import citiesIndex from '@/data/cities/cities-index.json'

export const metadata: Metadata = {
  title: 'Tree Service Service Local — Find the Best Landscapers Near You',
  description: 'Compare top-rated, licensed tree-service and lawn care companies in 50+ US cities. Real prices on mowing, design, tree trimming, and sprinkler install. Get 3 free quotes.',
}

const FEATURED = ['dallas-tx','houston-tx','phoenix-az','atlanta-ga','charlotte-nc','nashville-tn','denver-co','chicago-il','los-angeles-ca','tampa-fl','seattle-wa','raleigh-nc']
const featured = citiesIndex.filter(c => FEATURED.includes(c.slug))

export default function HomePage() {
  return (
    <main>
      <section className="bg-gradient-to-br from-green-800 via-green-700 to-emerald-600 text-white py-20 px-4">
        <div className="max-w-5xl mx-auto text-center">
          <div className="inline-flex items-center gap-2 bg-white/15 rounded-full px-4 py-2 text-sm mb-6">
            🌿 50 cities · Licensed landscapers · Free quotes
          </div>
          <h1 className="text-4xl md:text-5xl font-bold mb-5 leading-tight">
            Find the Best Tree Service Company<br className="hidden md:block" /> in Your City
          </h1>
          <p className="text-green-100 text-xl max-w-2xl mx-auto mb-8">
            Compare licensed, top-rated landscapers. Real prices on lawn mowing, yard design, tree trimming, and sprinkler installation. Free quotes, no obligation.
          </p>
          <Link href="/tree-service" className="bg-white text-green-800 font-bold px-8 py-4 rounded-xl hover:bg-green-50 transition-colors text-lg inline-block">
            Browse Landscapers by City →
          </Link>
          <div className="mt-8 flex flex-wrap justify-center gap-6 text-sm text-green-200">
            <span>✓ Licensed & insured only</span>
            <span>✓ Real local pricing</span>
            <span>✓ Spring specials available</span>
          </div>
        </div>
      </section>

      <section className="py-16 px-4 bg-white">
        <div className="max-w-5xl mx-auto">
          <h2 className="text-2xl font-bold text-center mb-2">Popular Tree Service Markets</h2>
          <p className="text-gray-600 text-center mb-10">Click your city for top landscapers, local pricing, and free quotes.</p>
          <div className="grid sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-4">
            {featured.map(city => (
              <Link key={city.slug} href={`/tree-service/${city.slug}`}
                className="bg-white border border-gray-200 rounded-xl p-4 text-center hover:border-green-400 hover:shadow-md transition-all group">
                <div className="text-2xl mb-2">🌿</div>
                <div className="font-semibold group-hover:text-green-700 transition-colors">{city.city}</div>
                <div className="text-xs text-gray-500 mt-0.5">{city.stateAbbr}</div>
              </Link>
            ))}
          </div>
          <div className="text-center mt-8">
            <Link href="/tree-service" className="text-green-700 font-semibold hover:underline">View all 50 cities →</Link>
          </div>
        </div>
      </section>

      <section className="py-16 px-4 bg-gray-50">
        <div className="max-w-5xl mx-auto">
          <h2 className="text-2xl font-bold text-center mb-10">How It Works</h2>
          <div className="grid md:grid-cols-3 gap-8">
            {[
              { icon: '🔍', title: 'Find Your City', desc: 'Browse 50+ cities. See top-rated local landscapers, real pricing, and seasonal tips.' },
              { icon: '📋', title: 'Get Free Quotes', desc: 'Submit a quick request and connect with up to 3 licensed, local landscapers within 24 hours.' },
              { icon: '✅', title: 'Compare & Hire', desc: 'Review quotes, services, and reviews. Pick the best landscaper for your yard and budget.' },
            ].map(s => (
              <div key={s.title} className="text-center">
                <div className="text-4xl mb-4">{s.icon}</div>
                <h3 className="font-bold text-lg mb-2">{s.title}</h3>
                <p className="text-gray-600 text-sm leading-relaxed">{s.desc}</p>
              </div>
            ))}
          </div>
        </div>
      </section>

      <section className="py-16 px-4 bg-white">
        <div className="max-w-5xl mx-auto">
          <h2 className="text-2xl font-bold text-center mb-10">Tree Service Services We Help You Find</h2>
          <div className="grid sm:grid-cols-2 md:grid-cols-3 gap-4">
            {[
              { icon: '🌱', title: 'Lawn Mowing', desc: 'Weekly, bi-weekly, or monthly mowing service. $35–$120 per visit.' },
              { icon: '🏡', title: 'Tree Service Design', desc: 'Full yard design, planting, and installation. $2,000–$20,000.' },
              { icon: '🌳', title: 'Tree Trimming & Removal', desc: 'Pruning, shaping, and hazard tree removal. $150–$1,800.' },
              { icon: '💧', title: 'Sprinkler & Irrigation', desc: 'New system install, repairs, and winterization. $2,000–$7,000.' },
              { icon: '🍂', title: 'Mulch & Cleanup', desc: 'Mulch installation, leaf cleanup, and seasonal prep. $200–$1,000.' },
              { icon: '🌿', title: 'Lawn Care Programs', desc: 'Fertilizing, weed control, aeration, overseeding. Annual contracts save 15–20%.' },
            ].map(svc => (
              <div key={svc.title} className="bg-gray-50 rounded-xl p-5 border border-gray-100">
                <div className="text-2xl mb-3">{svc.icon}</div>
                <h3 className="font-semibold mb-1">{svc.title}</h3>
                <p className="text-sm text-gray-600">{svc.desc}</p>
              </div>
            ))}
          </div>
        </div>
      </section>

      <section className="py-16 px-4 bg-green-600 text-white text-center">
        <div className="max-w-2xl mx-auto">
          <h2 className="text-2xl font-bold mb-4">Spring Is Here — Book Now Before Schedules Fill Up</h2>
          <p className="text-green-100 mb-8">Top landscapers in most cities are booked 3–6 weeks out by May. Get your quotes now.</p>
          <Link href="/tree-service" className="bg-white text-green-800 font-bold px-8 py-4 rounded-xl hover:bg-green-50 transition-colors inline-block">
            Browse Landscapers by City →
          </Link>
        </div>
      </section>

      <footer className="bg-gray-900 text-gray-400 py-10 px-4 text-center text-sm">
        <div className="max-w-5xl mx-auto">
          <div className="font-semibold text-white mb-2">Tree Service Service Local</div>
          <p className="mb-4">Connecting homeowners with licensed tree-service companies in 50+ US cities.</p>
          <p className="text-xs">© {new Date().getFullYear()} Tree Service Service Local. Pricing data is based on regional market research and may vary.</p>
        </div>
      </footer>
    </main>
  )
}
