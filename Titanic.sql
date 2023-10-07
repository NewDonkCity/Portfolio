/****** Script for SelectTopNRows command from SSMS  ******/
SELECT * FROM [Titanic].[dbo].[Titanic]

---------------- Data warehouse
select * from [dbo].[Titanic_FACT]
select * from [dbo].[Dim_Name]
select * from [dbo].[Dim_Sex]
select * from [dbo].[Dim_Age]
select * from [dbo].[Dim_Survived]
select * from [dbo].[Dim_Pclass]
select * from [dbo].[Dim_Ticket]