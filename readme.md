# Structure of the API

**By Gabriel Rosales**

Semester project, asked by the proffesor Byron Vasquez, this API is intended to be consume by a java desktop application and a webpage

It solves the problem set by a pharmacy that needs a new system to handle sells and inventory.

## Models:

### User (employee):
    - Name (String - full name)
    - Rol (Int - employee or manager, etc, level of access)
    - Phone (String)
    - Adress (String - short address)
    - Email (String - id)
    - status (Bool - active or not)
    - employeeNumber(String - carnet)
    - schedule (Int - map with different turns and schedules)

### Supplier:
    - Name (String - full company name)
    - Phone (String)
    - Adress (String - short address)
    - Email (String)
    - month (Array - String[])
    - ProductFamily (Array - ProductFamily[])

### Client:
    - Name (String - full company name)
    - Phone (String)
    - Adress (String - short address)
    - Email (String - id)
    - Recepits (Array - Receipt[])

### ProductFamily (Manages stock of a product):
    - ProductName (String - full product name)
    - UnitPrice (FLoat)
    - Stock (Int)
    - Supplier (Supplier - id)

### Product (Goes to a receipt, and gets saved):
    - ProductName (String - full product name)
    - ExplirationDate (Date)
    - PriceAtMoment (Float)
    - ProductFamily (ProductFamily - id)

### Sell:
    - Products (Array - Product[])
    - Cost (Int - Sumatory of all the PriceAtMoment)

### Receipt:
    - Employee (Employee)
    - Client (Client)
    - Sell (Sell)
    - TotalCost (Cost adding iva)
    - Date (Date)

