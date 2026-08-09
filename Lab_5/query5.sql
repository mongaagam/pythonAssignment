Select StrfTime('%m', InvoiceDate) AS Month,
       Sum(Total) As Revenue
From Invoice
Where StrfTime('%Y', InvoiceDate) = '2009'
Group By Month;

