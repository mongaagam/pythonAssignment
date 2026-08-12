--Top Customers
Select
    Customer.CustomerId,
    Customer.FirstName || ' ' || Customer.LastName AS CustomerName,
    Sum(Invoice.Total) AS TotalSpend
From Customer
Join Invoice
    On Customer.CustomerId = Invoice.CustomerId
Group by Customer.CustomerId
Order By TotalSpend DESC
Limit 5;
