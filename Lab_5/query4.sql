Select Track.Name,
SUM(InvoiceLine.Quantity) As TotalSold
From InvoiceLine
Joim Track
On InvoiceLine.TrackId = Track.TrackId
Group by Track.TrackId
Order by TotalSold DESC
LIMIT 10;
