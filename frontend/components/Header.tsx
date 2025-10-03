'use client';

export function Header() {
  return (
    <header className="bg-white shadow">
      <div className="container mx-auto px-4 py-6">
        <div className="flex items-center justify-between">
          <div>
            <h1 className="text-3xl font-bold text-gray-900">EconoSense AI</h1>
            <p className="text-gray-600">Economic Analysis & Forecasting Dashboard</p>
          </div>
          <nav>
            <ul className="flex space-x-6">
              <li>
                <a href="/dashboard" className="text-gray-700 hover:text-blue-500">
                  Dashboard
                </a>
              </li>
              <li>
                <a href="/forecasts" className="text-gray-700 hover:text-blue-500">
                  Forecasts
                </a>
              </li>
              <li>
                <a href="/sentiment" className="text-gray-700 hover:text-blue-500">
                  Sentiment
                </a>
              </li>
              <li>
                <a href="/analysis" className="text-gray-700 hover:text-blue-500">
                  Analysis
                </a>
              </li>
            </ul>
          </nav>
        </div>
      </div>
    </header>
  );
}