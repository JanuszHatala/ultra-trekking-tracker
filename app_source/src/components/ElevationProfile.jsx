import React, { useRef, useEffect, useState } from 'react';

export function ElevationProfile({ points, checkpoints, height = 200, hoverPoint, onHoverPoint }) {
  const [localHover, setLocalHover] = useState(null);
  const canvasRef = useRef(null);

  useEffect(() => {
    if (!points || points.length === 0 || !canvasRef.current) return;

    const canvas = canvasRef.current;
    const ctx = canvas.getContext('2d');
    const width = canvas.offsetWidth;
    const h = height;
    const dpr = window.devicePixelRatio || 1;

    canvas.width = width * dpr;
    canvas.height = h * dpr;
    
    // Important: Scale the context to match the DPR so drawing logic remains identical
    ctx.scale(dpr, dpr);

    ctx.clearRect(0, 0, width, h);

    const maxDist = points[points.length - 1].dist;
    const minEle = Math.min(...points.map(p => p.ele));
    const maxEle = Math.max(...points.map(p => p.ele));
    const eleRange = maxEle - minEle || 1;

    // Draw grid
    ctx.strokeStyle = 'rgba(255,255,255,0.1)';
    ctx.lineWidth = 1;
    for (let i = 0; i <= 4; i++) {
      const y = (h / 4) * i;
      ctx.beginPath();
      ctx.moveTo(0, y);
      ctx.lineTo(width, y);
      ctx.stroke();
    }

    // Draw profile path for FILL
    ctx.beginPath();
    ctx.moveTo(0, h);
    points.forEach((p) => {
      const x = (p.dist / maxDist) * width;
      const y = h - ((p.ele - minEle) / eleRange) * h;
      ctx.lineTo(x, y);
    });
    ctx.lineTo(width, h);
    ctx.closePath();

    // Fill gradient
    const gradient = ctx.createLinearGradient(0, 0, 0, h);
    gradient.addColorStop(0, 'rgba(132, 204, 22, 0.4)');
    gradient.addColorStop(1, 'rgba(132, 204, 22, 0.0)');
    ctx.fillStyle = gradient;
    ctx.fill();

    // Draw profile path for STROKE with slope colors
    for (let i = 1; i < points.length; i++) {
      const p1 = points[i - 1];
      const p2 = points[i];
      
      const x1 = (p1.dist / maxDist) * width;
      const y1 = h - ((p1.ele - minEle) / eleRange) * h;
      const x2 = (p2.dist / maxDist) * width;
      const y2 = h - ((p2.ele - minEle) / eleRange) * h;
      
      // Calculate slope %
      const distDiff = (p2.dist - p1.dist) * 1000; // in meters
      const eleDiff = p2.ele - p1.ele;
      const slope = distDiff > 0 ? (eleDiff / distDiff) * 100 : 0;
      
      ctx.beginPath();
      ctx.moveTo(x1, y1);
      ctx.lineTo(x2, y2);
      
      if (slope > 15) ctx.strokeStyle = '#dc2626'; // red-600
      else if (slope > 5) ctx.strokeStyle = '#f97316'; // orange-500
      else if (slope > -5) ctx.strokeStyle = '#84cc16'; // lime-500
      else if (slope > -15) ctx.strokeStyle = '#15803d'; // green-700
      else ctx.strokeStyle = '#3b82f6'; // blue-500
      
      ctx.lineWidth = 2;
      ctx.stroke();
    }

    // Draw hovered section if passed via hoverPoint props that has a section
    if (hoverPoint && hoverPoint.sectionPoints && hoverPoint.sectionPoints.length > 0) {
      ctx.beginPath();
      const firstSectionPoint = hoverPoint.sectionPoints[0];
      const lastSectionPoint = hoverPoint.sectionPoints[hoverPoint.sectionPoints.length - 1];
      
      const x1 = (firstSectionPoint.dist / maxDist) * width;
      const x2 = (lastSectionPoint.dist / maxDist) * width;
      
      ctx.fillStyle = 'rgba(255, 255, 255, 0.15)';
      ctx.fillRect(x1, 0, x2 - x1, h);
    }

    // Draw checkpoints
    if (checkpoints && checkpoints.length > 0) {
      ctx.fillStyle = '#84cc16'; // lime-400
      ctx.strokeStyle = '#0f172a'; // slate-900
      ctx.lineWidth = 2;

      checkpoints.forEach(cp => {
        const x = (cp.km / maxDist) * width;
        const y = h - ((cp.ele - minEle) / eleRange) * h;
        
        ctx.beginPath();
        ctx.arc(x, y, 4, 0, Math.PI * 2);
        ctx.fill();
        ctx.stroke();
      });
    }

    // Draw local hover
    const activeHover = localHover || (hoverPoint && !hoverPoint.sectionPoints ? hoverPoint : null);

    if (activeHover) {
       const x = (activeHover.dist / maxDist) * width;
       const y = h - ((activeHover.ele - minEle) / eleRange) * h;

       // Vertical line
       ctx.beginPath();
       ctx.setLineDash([5, 5]);
       ctx.moveTo(x, 0);
       ctx.lineTo(x, h);
       ctx.strokeStyle = 'rgba(255, 255, 255, 0.5)';
       ctx.lineWidth = 1;
       ctx.stroke();
       ctx.setLineDash([]);

       // Point dot
       ctx.beginPath();
       ctx.arc(x, y, 6, 0, Math.PI * 2);
       ctx.fillStyle = '#ec4899'; // pink-500
       ctx.fill();
       ctx.lineWidth = 2;
       ctx.strokeStyle = '#ffffff';
       ctx.stroke();

       // Tooltip
       const text = `${activeHover.dist ? activeHover.dist.toFixed(1) : (activeHover.km ? activeHover.km.toFixed(1) : 0)} km | ${Math.round(activeHover.ele)} m`;
       ctx.font = '12px sans-serif';
       const textWidth = ctx.measureText(text).width;
       
       let tooltipX = x - textWidth / 2;
       if (tooltipX < 10) tooltipX = 10;
       if (tooltipX + textWidth + 20 > width) tooltipX = width - textWidth - 20;

       let tooltipY = y - 35;
       let textY = y - 18;
       
       if (tooltipY < 5) {
           tooltipY = y + 15;
           textY = y + 32;
       }

       ctx.fillStyle = 'rgba(15, 23, 42, 0.9)'; // slate-900
       ctx.fillRect(tooltipX - 5, tooltipY, textWidth + 10, 24);
       
       ctx.strokeStyle = 'rgba(255, 255, 255, 0.2)';
       ctx.strokeRect(tooltipX - 5, tooltipY, textWidth + 10, 24);
       
       ctx.fillStyle = '#ffffff';
       ctx.fillText(text, tooltipX, textY);
    }

  }, [points, checkpoints, height, localHover, hoverPoint]);

  const handleMouseMove = (e) => {
    if (!points || points.length === 0) return;
    const rect = canvasRef.current.getBoundingClientRect();
    const x = e.clientX - rect.left;
    const width = rect.width;
    const maxDist = points[points.length - 1].dist;
    
    const targetDist = (x / width) * maxDist;
    const closest = points.reduce((prev, curr) => 
      Math.abs(curr.dist - targetDist) < Math.abs(prev.dist - targetDist) ? curr : prev
    );
    
    setLocalHover(closest);
    if (onHoverPoint) onHoverPoint(closest);
  };

  const handleMouseLeave = () => {
    setLocalHover(null);
    if (onHoverPoint) onHoverPoint(null);
  };

  return (
    <canvas 
      ref={canvasRef} 
      className="w-full h-full cursor-crosshair"
      onMouseMove={handleMouseMove}
      onMouseLeave={handleMouseLeave}
    />
  );
}
