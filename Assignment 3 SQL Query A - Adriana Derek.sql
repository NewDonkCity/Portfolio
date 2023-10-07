-- Fact Internet Sales
-- Dimension Product & Promotion
-- 
-- Question 1: Are promotion influencing sales of products on Internet?
---Question 2: What is the most sold product on the internet?
--
--Answer 1: Promotions are not influencing sales of products on Internet. 
-- However, the price of the product seems to influence the sales as the top 5 products sold on
-- the internet do not exceed 35 dollars price.

Select Product.EnglishProductName,
	   Product.Weight,
	   Product.ListPrice,
	   Internet_Sales.OrderQuantity,
	   Internet_Sales.CustomerKey,
	   Promotion.DiscountPct "Discount",
	   Promotion.Englishpromotiontype "Promotion_Type"		
from dbo.FactInternetSales Internet_Sales
left join dbo.DimProduct Product
on Internet_Sales.ProductKey = product.ProductKey
left join dbo.DimPromotion Promotion
on Internet_Sales.ProductKey = Promotion.PromotionKey		
Order by Product.ListPrice 
--
--
--
Select Product.EnglishProductName, count(product.EnglishProductName) "Product_Count"
	   
from dbo.FactInternetSales Internet_Sales
left join dbo.DimProduct Product
on Internet_Sales.ProductKey = product.ProductKey
left join dbo.DimPromotion Promotion
on Internet_Sales.ProductKey = Promotion.PromotionKey
Group by (product.EnglishProductName)
Order by "Product_Count" desc

-- The top 5 products more sold on Internet are:
--Water Bottle- 30 oz-price 499
--Patch Kit/8 - price 2.29
--Mountain Tire Tube - price 499
--Road Tire Tube - price 3.99
--Sport - 100 Helment, Red - price 34.99


