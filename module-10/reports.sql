-- Report 1: Client and Financial Advisor
-- Shows each client with their assigned financial advisor and advisor role.
SELECT
    c.ClientID,
    CONCAT(c.FirstName,' ',c.LastName) AS Client,
    CONCAT(e.FirstName,' ',e.LastName) AS Advisor,
    e.Role
FROM Client c
JOIN Employee e
ON c.EmployeeID = e.EmployeeID
ORDER BY c.ClientID;


-- Report 2: Client Investment Portfolio
-- Lists each client's investment, value, and purchase date.
SELECT
    c.ClientID,
    CONCAT(c.FirstName,' ',c.LastName) AS Client,
    a.AssetType,
    a.Value,
    a.PurchaseDate
FROM Client c
JOIN Asset a
ON c.ClientID = a.ClientID
ORDER BY a.Value DESC;


-- Report 3: Billing Status
-- Displays each client's billing information and payment status.
SELECT
    b.BillingID,
    CONCAT(c.FirstName,' ',c.LastName) AS Client,
    b.BillingDate,
    b.Amount,
    b.Status
FROM Billing b
JOIN Client c
ON b.ClientID = c.ClientID
ORDER BY b.Status, b.BillingDate;