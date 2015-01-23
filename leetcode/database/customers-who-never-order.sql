select name from Customers a where id not in (select CustomerId from Orders);
