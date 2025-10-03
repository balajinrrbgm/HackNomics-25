'use client';

import { useEffect, useRef } from 'react';
import * as d3 from 'd3';

interface EconomicData {
  date: string;
  value: number;
  indicator: string;
}

interface Props {
  data: EconomicData[];
}

export function EconomicChart({ data }: Props) {
  const chartRef = useRef<SVGSVGElement | null>(null);

  useEffect(() => {
    if (!data || !chartRef.current) return;

    // Clear previous chart
    d3.select(chartRef.current).selectAll('*').remove();

    // Set dimensions
    const margin = { top: 20, right: 30, bottom: 30, left: 60 };
    const width = 600 - margin.left - margin.right;
    const height = 400 - margin.top - margin.bottom;

    // Create SVG
    const svg = d3.select(chartRef.current)
      .attr('width', width + margin.left + margin.right)
      .attr('height', height + margin.top + margin.bottom)
      .append('g')
      .attr('transform', `translate(${margin.left},${margin.top})`);

    // Parse dates
    const dates = data.map(d => new Date(d.date));
    const values = data.map(d => d.value);

    // Create scales
    const x = d3.scaleTime()
      .domain(d3.extent(dates) as [Date, Date])
      .range([0, width]);

    const y = d3.scaleLinear()
      .domain([d3.min(values) || 0, d3.max(values) || 0])
      .range([height, 0]);

    // Add axes
    svg.append('g')
      .attr('transform', `translate(0,${height})`)
      .call(d3.axisBottom(x));

    svg.append('g')
      .call(d3.axisLeft(y));

    // Create line generator
    const line = d3.line<EconomicData>()
      .x(d => x(new Date(d.date)))
      .y(d => y(d.value));

    // Add line path
    svg.append('path')
      .datum(data)
      .attr('fill', 'none')
      .attr('stroke', 'steelblue')
      .attr('stroke-width', 1.5)
      .attr('d', line);

  }, [data]);

  return (
    <div className="relative">
      <svg ref={chartRef}></svg>
    </div>
  );
}