--Questions:
--1- Do customers respond to the surveys multiple times?
--2- What are the top 5 product subcategories leading customers to respond to the survey?
--
--
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

-- Response question 1: Although there are customers that have participated more than one time in the 
-- Survey, the maximum number of customers responding to the survey is 5, just for one customer. 
-- The average participation count is 2 per customer.

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

-- Answer 2: The top 5 product subcategories according to survey response are Shorts, Tights, Pumps, Gloves
-- and Panniers

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