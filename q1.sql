SELECT Id, BilldingDate, C.Name as Name, CC.Name as ReferredByName
FROM Invoices 
JOIN Customers C on Invoices.CustomerId = C.Id
LEFT JOIN Customers CC on C.ReferredBy = CC.Id
ORDER BY BilldingDate 


