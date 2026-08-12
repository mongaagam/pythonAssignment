--Monthly Revenue
Select
    strftime('%Y-%m', InvoiceDate) AS month,
    ROUND(SUM(Total), 2) AS revenue
From Invoice
Where InvoiceDate >= '2013-01-01'
  AND InvoiceDate < '2014-01-01'
Group BY month
Order BY month;
