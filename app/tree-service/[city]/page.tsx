import type { Metadata } from 'next'
import { notFound } from 'next/navigation'
import fs from 'fs'
import path from 'path'
import citiesIndex from '@/data/cities/cities-index.json'
import LeadCaptureForm from '@/components/LeadCaptureForm'

interface LandCityData {
  slug: string; city: string; state: string; stateAbbr: string; population: number
  tree-serviceSeason: string; climateNote: string
  costs: {
    lawnMowingWeekly: { min: number; max: number; avg: number }
    lawnMowingMonthly: { min: number; max: number; avg: number }
    landscapeDesignInstall: { min: number; max: number; avg: number }
    sprinklerInstall: { min: number; max: number; avg: number }
    treeTrimmingSmall: { min: number; max: number; avg: number }
    treeTrimmingLarge: { min: number; max: number; avg: number }
    mulchInstall: { min: number; max: number; avg: number }
  }
  providers: { name: string; rating: number; reviews: number; phone: string; address: string; services: string[]; licensed: boolean; insured: boolean; yearsInBusiness: number }[]
  faqs: { question: string; answer: string }[]
  buyerTips: string[]
  lastUpdated: string
}

function getCityData(slug: string): LandCityData | null {
  try { return JSON.parse(fs.readFileSync(path.join(process.cwd(), 'data', 'cities', `${slug}.json`), 'utf-8')) }
  catch { return null }
}

export async function generateStaticParams() {
  return citiesIndex.map(c => ({ city: c.slug }))
}

export async function generateMetadata({ params }: { params: { city: string } }): Promise<Metadata> {
  const d = getCityData(params.city)
  if (!d) return {}
  const year = new Date().getFullYear()
  const title = `Best Tree Service Companies in ${d.city}, ${d.stateAbbr} (${year}) — Lawn Care & More`
  const desc = `Top-rated landscapers in ${d.city}, ${d.stateAbbr}. Lawn mowing from $${d.costs.lawnMowingWeekly.min}/visit, tree-service from $${d.costs.landscapeDesignInstall.min.toLocaleString()}. Licensed, insured, free quotes.`
  return {
    title, description: desc,
    keywords: [`tree-service ${d.city}`, `lawn care ${d.city} ${d.stateAbbr}`, `landscapers ${d.city}`, `lawn mowing ${d.city}`, `tree trimming ${d.city}`, `tree-service companies ${d.city}`],
    openGraph: { title, description: desc, type: 'website' },
    alternates: { canonical: `/tree-service/${params.city}` },
  }
}

export default function CityTree ServicePage({ params }: { params: { city: string } }) {
  const d = getCityData(params.city)
  if (!d) notFound()
  const top = d.providers[0]

  const costRows = [
    ['Lawn Mowing (per visit)', d.costs.lawnMowingWeekly],
    ['Monthly Lawn Maintenance', d.costs.lawnMowingMonthly],
    ['Landscape Design & Install', d.costs.landscapeDesignInstall],
    ['Sprinkler System Install', d.costs.sprinklerInstall],
    ['Tree Trimming (small tree)', d.costs.treeTrimmingSmall],
    ['Tree Trimming (large tree)', d.costs.treeTrimmingLarge],
    ['Mulch Installation', d.costs.mulchInstall],
  ]

  return (
    <>
      <script type="application/ld+json" dangerouslySetInnerHTML={{ __html: JSON.stringify({
        '@context': 'https://schema.org', '@type': 'FAQPage',
        mainEntity: d.faqs.map(f => ({ '@type': 'Question', name: f.question, acceptedAnswer: { '@type': 'Answer', text: f.answer } }))
      })}} />
      <main>
        <div className="bg-white border-b border-gray-100 py-3 px-4 text-sm text-gray-500">
          <div className="max-w-6xl mx-auto flex items-center gap-2">
            <a href="/" className="hover:text-green-700">Home</a><span>›</span>
            <a href="/tree-service" className="hover:text-green-700">Tree Service</a><span>›</span>
            <span className="text-gray-900">{d.city}, {d.stateAbbr}</span>
          </div>
        </div>

        <section className="bg-gradient-to-br from-green-800 via-green-700 to-emerald-600 text-white py-16 px-4">
          <div className="max-w-6xl mx-auto">
            <div className="max-w-3xl">
              <div className="flex items-center gap-2 text-green-200 text-sm mb-4">
                <span>🌿 Tree Service</span><span>·</span><span>{d.city}, {d.stateAbbr}</span>
              </div>
              <h1 className="text-3xl md:text-4xl font-bold mb-4 leading-tight">
                Best Tree Service Companies in {d.city}, {d.stateAbbr}
              </h1>
              <p className="text-green-100 text-lg mb-6">
                {d.providers.length} top-rated, licensed landscapers. Mowing from ${d.costs.lawnMowingWeekly.min}/visit. Tree Service projects from ${d.costs.landscapeDesignInstall.min.toLocaleString()}. Season: {d.tree-serviceSeason}.
              </p>
              <div className="flex flex-wrap gap-4 text-sm mb-6">
                {[
                  [`$${d.costs.lawnMowingWeekly.avg}`, 'avg mow visit'],
                  [`$${d.costs.lawnMowingMonthly.avg}`, 'avg monthly plan'],
                  [`${d.providers.length}`, 'top landscapers'],
                ].map(([val, label]) => (
                  <div key={label} className="bg-white/15 rounded-lg px-4 py-2">
                    <span className="font-bold text-lg">{val}</span>
                    <span className="text-green-200"> {label}</span>
                  </div>
                ))}
              </div>
              <div className="flex flex-wrap gap-3 text-sm text-green-200">
                <span>⭐ Updated {d.lastUpdated}</span><span>·</span>
                <span>✓ Licensed & insured only</span><span>·</span>
                <span>✓ Spring season ready</span>
              </div>
            </div>
          </div>
        </section>

        <div className="max-w-6xl mx-auto px-4 py-12">
          <div className="grid lg:grid-cols-3 gap-8">
            <div className="lg:col-span-2 space-y-12">

              <section id="providers">
                <h2 className="text-2xl font-bold mb-6">Top Tree Service Companies in {d.city}</h2>
                <div className="space-y-4">
                  {d.providers.map((p, i) => (
                    <div key={p.name} className="bg-white rounded-xl border border-gray-200 p-5 flex gap-4 hover:border-green-400 hover:shadow-sm transition-all">
                      <div className={`flex-shrink-0 w-10 h-10 rounded-full flex items-center justify-center font-bold text-sm ${i === 0 ? 'bg-green-100 text-green-700' : 'bg-gray-100 text-gray-600'}`}>#{i+1}</div>
                      <div className="flex-1">
                        <div className="flex items-center justify-between flex-wrap gap-2">
                          <h3 className="font-semibold text-gray-900">{p.name}</h3>
                          <div className="flex items-center gap-1.5">
                            <span className="text-yellow-400">{'★'.repeat(Math.round(p.rating))}</span>
                            <span className="font-semibold text-sm">{p.rating}</span>
                            <span className="text-gray-400 text-sm">({p.reviews})</span>
                          </div>
                        </div>
                        <div className="text-sm text-gray-500 mt-1">{p.address} · {p.yearsInBusiness} yrs in business</div>
                        <div className="flex flex-wrap gap-2 mt-2">
                          {p.services.map(s => <span key={s} className="text-xs bg-gray-100 text-gray-600 px-2 py-0.5 rounded-full">{s}</span>)}
                        </div>
                        <div className="text-xs text-green-600 mt-2">{p.licensed && '✓ Licensed'}{p.insured && ' · ✓ Insured'}</div>
                      </div>
                    </div>
                  ))}
                </div>
              </section>

              <section id="costs">
                <h2 className="text-2xl font-bold mb-4">Tree Service Costs in {d.city}, {d.stateAbbr}</h2>
                <p className="text-gray-600 mb-2 text-sm">{d.climateNote}.</p>
                <p className="text-gray-600 mb-6 text-sm">Here are typical pricing ranges from local market data:</p>
                <div className="overflow-x-auto rounded-xl border border-gray-200">
                  <table className="w-full text-sm">
                    <thead>
                      <tr className="bg-gray-50 border-b border-gray-200">
                        <th className="text-left px-4 py-3 font-semibold text-gray-700">Service</th>
                        <th className="text-right px-4 py-3 font-semibold text-gray-700">Low</th>
                        <th className="text-right px-4 py-3 font-semibold text-gray-700">High</th>
                        <th className="text-right px-4 py-3 font-semibold text-green-700 bg-green-50">Avg ({d.city})</th>
                      </tr>
                    </thead>
                    <tbody>
                      {costRows.map(([label, cost], i) => (
                        <tr key={String(label)} className={i % 2 === 0 ? 'bg-white' : 'bg-gray-50/50'}>
                          <td className="px-4 py-3 font-medium text-gray-900">{String(label)}</td>
                          <td className="px-4 py-3 text-right text-gray-600">${(cost as any).min.toLocaleString()}</td>
                          <td className="px-4 py-3 text-right text-gray-600">${(cost as any).max.toLocaleString()}</td>
                          <td className="px-4 py-3 text-right font-semibold text-green-700 bg-green-50">${(cost as any).avg.toLocaleString()}</td>
                        </tr>
                      ))}
                    </tbody>
                  </table>
                </div>
                <div className="mt-4 p-4 bg-green-50 rounded-lg text-sm text-green-900">
                  <strong>🌿 Spring Tip:</strong> Book now — top {d.city} landscapers fill their spring schedules by late April. Getting 3 quotes takes 2–3 days; waiting until May means waiting 3–6 weeks for availability.
                </div>
              </section>

              <section id="how-to-choose">
                <h2 className="text-2xl font-bold mb-4">How to Choose a Landscaper in {d.city}</h2>
                <div className="space-y-3">
                  {d.buyerTips.map((tip, i) => (
                    <div key={i} className="flex gap-3 p-4 bg-white rounded-lg border border-gray-100">
                      <div className="flex-shrink-0 w-7 h-7 bg-green-100 text-green-700 rounded-full flex items-center justify-center text-sm font-bold">{i+1}</div>
                      <p className="text-gray-700 text-sm leading-relaxed">{tip}</p>
                    </div>
                  ))}
                </div>
              </section>

              <section id="faq">
                <h2 className="text-2xl font-bold mb-6">FAQs: Tree Service in {d.city}</h2>
                <div className="space-y-4">
                  {d.faqs.map((faq, i) => (
                    <details key={i} className="bg-white rounded-xl border border-gray-200 group">
                      <summary className="flex items-center justify-between p-5 cursor-pointer font-medium text-gray-900 list-none">
                        {faq.question}
                        <span className="text-gray-400 group-open:rotate-180 transition-transform text-lg ml-4 flex-shrink-0">⌄</span>
                      </summary>
                      <div className="px-5 pb-5 text-gray-700 text-sm leading-relaxed border-t border-gray-100 pt-4">{faq.answer}</div>
                    </details>
                  ))}
                </div>
              </section>
            </div>

            <aside className="space-y-6">
              <div id="get-quotes" className="bg-white rounded-2xl border border-gray-200 p-6 shadow-sm sticky top-24">
                <div className="text-center mb-5">
                  <div className="text-2xl mb-2">🌿</div>
                  <h3 className="text-lg font-bold">Get Free Tree Service Quotes</h3>
                  <p className="text-sm text-gray-600 mt-1">Connect with top {d.city} landscapers</p>
                </div>
                <LeadCaptureForm city={d.city} stateAbbr={d.stateAbbr} serviceType="tree-service" />
              </div>

              <div className="bg-green-50 rounded-2xl p-6">
                <h3 className="font-bold mb-4 text-green-900">{d.city} Tree Service Facts</h3>
                <div className="space-y-3 text-sm">
                  <div className="flex justify-between"><span className="text-gray-600">Active season:</span><span className="font-medium text-xs text-right max-w-32">{d.tree-serviceSeason.split('(')[0].trim()}</span></div>
                  <div className="flex justify-between"><span className="text-gray-600">Avg mow visit:</span><span className="font-medium">${d.costs.lawnMowingWeekly.avg}</span></div>
                  <div className="flex justify-between"><span className="text-gray-600">Avg monthly plan:</span><span className="font-medium">${d.costs.lawnMowingMonthly.avg}</span></div>
                  <div className="flex justify-between"><span className="text-gray-600">Mulch install:</span><span className="font-medium">${d.costs.mulchInstall.avg}</span></div>
                  <div className="flex justify-between"><span className="text-gray-600">Sprinkler install:</span><span className="font-medium">${d.costs.sprinklerInstall.avg.toLocaleString()}</span></div>
                </div>
              </div>

              <div className="bg-white rounded-2xl border border-gray-200 p-6">
                <div className="text-xs text-gray-500 font-semibold uppercase tracking-wide mb-3">⭐ Top Rated in {d.city}</div>
                <div className="font-bold text-gray-900">{top.name}</div>
                <div className="flex items-center gap-2 mt-1">
                  <span className="text-yellow-400">{'★'.repeat(Math.round(top.rating))}</span>
                  <span className="text-sm font-medium">{top.rating}</span>
                  <span className="text-sm text-gray-400">({top.reviews})</span>
                </div>
                <div className="text-xs text-gray-600 mt-2">{top.yearsInBusiness} years in business</div>
                <div className="text-xs text-green-600 mt-1">{top.licensed && '✓ Licensed'}{top.insured && ' · ✓ Insured'}</div>
              </div>
            </aside>
          </div>
        </div>
      </main>
    </>
  )
}
