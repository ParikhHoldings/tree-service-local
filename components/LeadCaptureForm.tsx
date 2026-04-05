'use client'
import { useState } from 'react'

const SERVICE_TYPES: Record<string, string[]> = {
  treeService: ['Lawn Mowing Service', 'TreeService Design & Install', 'Tree Trimming / Removal', 'Sprinkler System Install', 'Mulch & Cleanup', 'Tree Service Program (fertilize/weed)', 'Other'],
  electrician: ['Panel Upgrade', 'EV Charger Install', 'Outlet / Switch Work', 'Rewiring', 'Generator Install', 'Troubleshooting', 'Other'],
  roofing: ['Roof Repair', 'Full Replacement', 'Storm Damage', 'Gutter Install', 'Inspection', 'Other'],
  hvac: ['AC Repair', 'AC Replacement', 'Furnace Repair', 'Furnace Replacement', 'Tune-Up', 'Duct Cleaning', 'Other'],
}

const ACCENT: Record<string, { btn: string; ring: string }> = {
  treeService: {
    btn: 'w-full bg-green-600 text-white font-bold py-3 rounded-lg hover:bg-green-700 transition-colors disabled:opacity-70',
    ring: 'w-full border border-gray-300 rounded-lg px-4 py-2.5 text-sm focus:outline-none focus:border-green-500 focus:ring-1 focus:ring-green-500',
  },
  electrician: {
    btn: 'w-full bg-yellow-500 text-white font-bold py-3 rounded-lg hover:bg-yellow-600 transition-colors disabled:opacity-70',
    ring: 'w-full border border-gray-300 rounded-lg px-4 py-2.5 text-sm focus:outline-none focus:border-yellow-500 focus:ring-1 focus:ring-yellow-500',
  },
  roofing: {
    btn: 'w-full bg-slate-700 text-white font-bold py-3 rounded-lg hover:bg-slate-800 transition-colors disabled:opacity-70',
    ring: 'w-full border border-gray-300 rounded-lg px-4 py-2.5 text-sm focus:outline-none focus:border-slate-500 focus:ring-1 focus:ring-slate-500',
  },
  hvac: {
    btn: 'w-full bg-orange-600 text-white font-bold py-3 rounded-lg hover:bg-orange-700 transition-colors disabled:opacity-70',
    ring: 'w-full border border-gray-300 rounded-lg px-4 py-2.5 text-sm focus:outline-none focus:border-orange-500 focus:ring-1 focus:ring-orange-500',
  },
}

export default function LeadCaptureForm({ city, stateAbbr, serviceType = 'treeService' }: { city: string; stateAbbr: string; serviceType?: string }) {
  const services = SERVICE_TYPES[serviceType] || SERVICE_TYPES.treeService
  const accent = ACCENT[serviceType] || ACCENT.treeService
  const [form, setForm] = useState({ name: '', email: '', phone: '', selectedService: services[0], message: '' })
  const [submitting, setSubmitting] = useState(false)
  const [submitted, setSubmitted] = useState(false)
  const [error, setError] = useState('')

  async function handleSubmit(e: React.FormEvent) {
    e.preventDefault(); setSubmitting(true); setError('')
    try {
      const res = await fetch('/api/leads', { method: 'POST', headers: { 'Content-Type': 'application/json' }, body: JSON.stringify({ ...form, city, stateAbbr, serviceType }) })
      if (res.ok) setSubmitted(true); else throw new Error()
    } catch { setError('Something went wrong. Please try again.') }
    finally { setSubmitting(false) }
  }

  if (submitted) return (
    <div className="text-center py-4">
      <div className="text-4xl mb-3">✅</div>
      <h4 className="font-bold text-lg mb-2">Request Submitted!</h4>
      <p className="text-sm text-gray-600">Up to 3 {city} contractors will contact you within 24 hours.</p>
    </div>
  )

  return (
    <form onSubmit={handleSubmit} className="space-y-3">
      <input type="text" required placeholder="Your name" className={accent.ring} value={form.name} onChange={e => setForm({...form, name: e.target.value})} />
      <input type="email" required placeholder="Email address" className={accent.ring} value={form.email} onChange={e => setForm({...form, email: e.target.value})} />
      <input type="tel" required placeholder="Phone number" className={accent.ring} value={form.phone} onChange={e => setForm({...form, phone: e.target.value})} />
      <select className={`${accent.ring} bg-white`} value={form.selectedService} onChange={e => setForm({...form, selectedService: e.target.value})}>
        {services.map(s => <option key={s} value={s}>{s}</option>)}
      </select>
      <textarea placeholder="Any details? Yard size, what you're looking for... (optional)" rows={2} className={`${accent.ring} resize-none`} value={form.message} onChange={e => setForm({...form, message: e.target.value})} />
      {error && <p className="text-red-600 text-xs">{error}</p>}
      <button type="submit" disabled={submitting} className={accent.btn}>{submitting ? 'Sending...' : `Get Free Quotes in ${city}`}</button>
      <p className="text-xs text-center text-gray-500">Free · No obligation · Responds in &lt;24 hours</p>
    </form>
  )
}
