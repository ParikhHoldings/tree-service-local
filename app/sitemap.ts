import { MetadataRoute } from 'next'
import citiesIndex from '@/data/cities/cities-index.json'
export default function sitemap(): MetadataRoute.Sitemap {
  const siteUrl = process.env.NEXT_PUBLIC_SITE_URL || 'https://tree-serviceservicelocal.com'
  return [
    { url: siteUrl, lastModified: new Date().toISOString(), changeFrequency: 'weekly', priority: 1.0 },
    { url: `${siteUrl}/tree-service`, lastModified: new Date().toISOString(), changeFrequency: 'weekly', priority: 0.9 },
    ...citiesIndex.map(city => ({ url: `${siteUrl}/tree-service/${city.slug}`, lastModified: new Date().toISOString(), changeFrequency: 'weekly' as const, priority: 0.9 })),
  ]
}
