-- Top 10 best-selling track

Select Track.name,
       Sum(InvoiceLine.Quantity) AS TotalSold
From InvoiceLine
Join Track
On InvoiceLine.TrackId=Track.TrackId
Group by Track.TrackId
Order by TotalSold Desc
Limit 10;
