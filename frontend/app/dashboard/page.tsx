'use client';

import { useEffect, useState } from 'react';
import { EconomicChart } from '@/components/EconomicChart';
import { SentimentAnalysis } from '@/components/SentimentAnalysis';
import { QuickSightDashboard } from '@/components/QuickSightDashboard';
import { Header } from '@/components/Header';

export default function Dashboard() {
  const [economicData, setEconomicData] = useState(null);
  const [sentimentData, setSentimentData] = useState(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    // Fetch data from our API endpoints
    const fetchData = async () => {
      try {
        const [economicResponse, sentimentResponse] = await Promise.all([
          fetch('/api/economic-data'),
          fetch('/api/sentiment-data')
        ]);

        const economic = await economicResponse.json();
        const sentiment = await sentimentResponse.json();

        setEconomicData(economic);
        setSentimentData(sentiment);
        setLoading(false);
      } catch (error) {
        console.error('Error fetching data:', error);
        setLoading(false);
      }
    };

    fetchData();
  }, []);

  if (loading) {
    return (
      <div className="flex items-center justify-center min-h-screen">
        <div className="animate-spin rounded-full h-32 w-32 border-t-2 border-b-2 border-blue-500"></div>
      </div>
    );
  }

  return (
    <div className="min-h-screen bg-gray-100">
      <Header />
      
      <main className="container mx-auto px-4 py-8">
        <div className="grid grid-cols-1 md:grid-cols-2 gap-8">
          <div className="bg-white rounded-lg shadow-lg p-6">
            <h2 className="text-2xl font-bold mb-4">Economic Indicators</h2>
            <EconomicChart data={economicData} />
          </div>
          
          <div className="bg-white rounded-lg shadow-lg p-6">
            <h2 className="text-2xl font-bold mb-4">Market Sentiment</h2>
            <SentimentAnalysis data={sentimentData} />
          </div>
        </div>
        
        <div className="mt-8 bg-white rounded-lg shadow-lg p-6">
          <h2 className="text-2xl font-bold mb-4">Interactive Analysis</h2>
          <QuickSightDashboard />
        </div>
      </main>
    </div>
  );
}