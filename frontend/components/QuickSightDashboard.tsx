'use client';

import { useEffect, useState } from 'react';

export function QuickSightDashboard() {
  const [dashboardUrl, setDashboardUrl] = useState<string>('');

  useEffect(() => {
    const getQuickSightDashboardUrl = async () => {
      try {
        const response = await fetch('/api/quicksight-embed');
        const data = await response.json();
        setDashboardUrl(data.embedUrl);
      } catch (error) {
        console.error('Error fetching QuickSight dashboard URL:', error);
      }
    };

    getQuickSightDashboardUrl();
  }, []);

  return (
    <div className="w-full h-[600px] bg-white rounded-lg shadow">
      {dashboardUrl ? (
        <iframe
          title="QuickSight Dashboard"
          src={dashboardUrl}
          width="100%"
          height="100%"
          allowFullScreen
        />
      ) : (
        <div className="flex items-center justify-center h-full">
          <div className="animate-spin rounded-full h-32 w-32 border-t-2 border-b-2 border-blue-500"></div>
        </div>
      )}
    </div>
  );
}