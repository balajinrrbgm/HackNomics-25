'use client';

interface SentimentData {
  date: string;
  sentiment: 'positive' | 'negative' | 'neutral';
  score: number;
  source: string;
}

interface Props {
  data: SentimentData[];
}

export function SentimentAnalysis({ data }: Props) {
  const getOverallSentiment = () => {
    const averageScore = data.reduce((acc, curr) => acc + curr.score, 0) / data.length;
    return {
      score: averageScore,
      label: averageScore > 0.6 ? 'Positive' : averageScore < 0.4 ? 'Negative' : 'Neutral',
      color: averageScore > 0.6 ? 'text-green-600' : averageScore < 0.4 ? 'text-red-600' : 'text-yellow-600'
    };
  };

  const sentiment = getOverallSentiment();

  return (
    <div className="space-y-6">
      <div className="bg-gray-50 rounded-lg p-6">
        <h3 className="text-xl font-semibold mb-2">Overall Market Sentiment</h3>
        <div className={`text-4xl font-bold ${sentiment.color}`}>
          {sentiment.label}
        </div>
        <div className="text-gray-600">
          Confidence Score: {(sentiment.score * 100).toFixed(1)}%
        </div>
      </div>

      <div className="space-y-4">
        <h3 className="text-xl font-semibold">Recent Sentiment Analysis</h3>
        <div className="space-y-2">
          {data.slice(0, 5).map((item, index) => (
            <div key={index} className="bg-white rounded-lg shadow p-4">
              <div className="flex justify-between items-center">
                <div>
                  <div className="text-sm text-gray-600">{new Date(item.date).toLocaleDateString()}</div>
                  <div className={`font-semibold ${
                    item.sentiment === 'positive' ? 'text-green-600' :
                    item.sentiment === 'negative' ? 'text-red-600' :
                    'text-yellow-600'
                  }`}>
                    {item.sentiment.charAt(0).toUpperCase() + item.sentiment.slice(1)}
                  </div>
                </div>
                <div className="text-right">
                  <div className="text-sm text-gray-600">{item.source}</div>
                  <div className="font-semibold">{(item.score * 100).toFixed(1)}%</div>
                </div>
              </div>
            </div>
          ))}
        </div>
      </div>
    </div>
  );
}