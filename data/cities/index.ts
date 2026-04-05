export interface Provider {
  name: string; rating: number; reviews: number; phone: string; address: string;
  services: string[]; yearsInBusiness?: number; licensed: boolean; insured: boolean;
}
export interface LandCostData {
  treeRemoval: { min: number; max: number; avg: number };
  treeTrimming: { min: number; max: number; avg: number };
  stumpGrinding: { min: number; max: number; avg: number };
  emergencyCleanup: { min: number; max: number; avg: number };
}
export interface CityData {
  slug: string; city: string; state: string; stateAbbr: string; population: number;
  treeServiceSeason: string; climateNote: string; costs: LandCostData;
  providers: Provider[]; faqs: { question: string; answer: string }[];
  buyerTips: string[]; lastUpdated: string; dataSource: string;
}
