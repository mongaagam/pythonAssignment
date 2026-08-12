--Revenue by Country
Select
    BillingCountry AS Country,
    Round(SUM(Total), 2) AS Revenue
From Invoice
Group By BillingCountry
Order BY Revenue Desc
