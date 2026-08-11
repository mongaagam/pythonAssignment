Select
    Track.TrackId,
    Track.Name AS TrackName,
    SUM(InvoiceLine.Quantity) AS QuantitySold
From Track
Join InvoiceLine
    ON Track.TrackId = InvoiceLine.TrackId
Group by Track.TrackId
Order by QuantitySold DESC
Limit 10;
