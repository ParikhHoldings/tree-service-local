export interface Provider {
  name: string; rating: number; reviews: number; phone: string; address: string;
  services: string[]; yearsInBusiness?: number; licensed: boolean; insured: boolean;
}
export interface LandCostData {
  lawnMowingWeekly: { min: number; max: number; avg: number };
  lawnMowingMonthly: { min: number; max: number; avg: number };
  landscapeDesignInstall: { min: number; max: number; avg: number };
  sprinklerInstall: { min: number; max: number; avg: number };
  treeTrimmingSmall: { min: number; max: number; avg: number };
  treeTrimmingLarge: { min: number; max: number; avg: number };
  mulchInstall: { min: number; max: number; avg: number };
}
export interface CityData {
  slug: string; city: string; state: string; stateAbbr: string; population: number;
  tree-serviceSeason: string; climateNote: string; costs: LandCostData;
  providers: Provider[]; faqs: { question: string; answer: string }[];
  buyerTips: string[]; lastUpdated: string; dataSource: string;
}
