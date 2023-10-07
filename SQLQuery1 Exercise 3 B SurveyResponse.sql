-- Fact Survey Response
-- Dimension Date & Customer
-- 
-- Question 1: Which nation/year combination has the lowest % of GDP spent on health?
-- Question 2: Which nation/year combination has the highest % of government expenditure on health?
--
-- Answer 1: At 1.5% of national GDP during that year, 
-- Congo durng the yeart 2000 has the lowest % of GDP spent on health
-- 
-- Answer 2: At 31.9% of total government expenditure during that year,
-- Sao Tome and Principe during the year 2000 has the highest % of gov't expense on health.
--
Select Survey_Response.SurveyResponsekey,
	   Survey_Response.CustomerKey,
	   Survey_Response.EnglishProductCategoryName,
	   Survey_Response.EnglishProductSubcategoryName,
	   Customer.FirstName,
	   Customer.LastName,
	   Customer.EmailAddress,
	   Date.FiscalYear,
	   Date.EnglishMonthName "Month",
	   Geography.EnglishCountryRegionName
from dbo.FactSurveyResponse Survey_Response
Left join dbo.DimDate Date
on Survey_Response.DateKey = Date.DateKey
Left join dbo.DimCustomer Customer
on Customer.CustomerKey = Survey_Response.CustomerKey
Left Join dbo.DimGeography Geography
on Customer.GeographyKey = Geography.GeographyKey



Select Survey_Response.CustomerKey,count (Survey_Response.CustomerKey) "Customer_Participation"
	   
from dbo.FactSurveyResponse Survey_Response
Left join dbo.DimDate Date
on Survey_Response.DateKey = Date.DateKey
Left join dbo.DimCustomer Customer
on Customer.CustomerKey = Survey_Response.CustomerKey
Left Join dbo.DimGeography Geography
on Customer.GeographyKey = Geography.GeographyKey
Group by (Survey_Response.CustomerKey)
Order by "Customer_Participation" desc


Select Survey_Response.EnglishProductSubcategoryName,count (Survey_Response.EnglishProductSubcategoryName) "Respose_Survey_by_Product"
	   
from dbo.FactSurveyResponse Survey_Response
Left join dbo.DimDate Date
on Survey_Response.DateKey = Date.DateKey
Left join dbo.DimCustomer Customer
on Customer.CustomerKey = Survey_Response.CustomerKey
Left Join dbo.DimGeography Geography
on Customer.GeographyKey = Geography.GeographyKey
Group by (Survey_Response.EnglishProductSubcategoryName)
Order by "Respose_Survey_by_Product" desc