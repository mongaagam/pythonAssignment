--Best Selling Tracks
Select
    Track.TrackId,
    Track.Name AS TrackName,
    SUM(InvoiceLine.Quantity) AS QuantitySold
From Track
Join InvoiceLine
On Track.TrackId = InvoiceLine.TrackId
Group By Track.TrackId
Order By QuantitySold DESC
Limit 10;
