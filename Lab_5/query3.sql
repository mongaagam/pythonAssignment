Select Customer.Country
Sum(Invoice.Total) AS Revenue
From Customer
Join Invoice
on Customer.Customer.Id=Invoice.CustomerId,
Group by Customer.Country;
