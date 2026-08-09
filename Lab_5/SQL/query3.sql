-- Total REvenue from Each Country

Select Customer.Country,
       Sum(Invoice.Total) AS TotalRevenue
FROM Customer
JOIN Invoice
ON Customer.CustomerId = Invoice.CustomerId
GROUP BY Customer.Country
ORDER BY TotalRevenue DESC;
