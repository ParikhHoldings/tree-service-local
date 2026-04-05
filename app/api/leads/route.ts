import { NextRequest, NextResponse } from 'next/server'
export async function POST(req: NextRequest) {
  try {
    const body = await req.json()
    const { name, email, phone, selectedService, city, stateAbbr, message, serviceType } = body
    if (!name || !email || !phone || !city) return NextResponse.json({ error: 'Missing required fields' }, { status: 400 })
    console.log('[LEAD]', JSON.stringify({ timestamp: new Date().toISOString(), name, email, phone, selectedService, serviceType: serviceType || 'tree-service', city, stateAbbr, message: message || '', source: 'tree-service-service-local' }))
    return NextResponse.json({ success: true }, { status: 200 })
  } catch (error) {
    console.error('[LEAD ERROR]', error)
    return NextResponse.json({ error: 'Internal server error' }, { status: 500 })
  }
}
