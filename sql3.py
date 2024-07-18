import sqlite3

# Connect to SQLite
connection = sqlite3.connect("employeedb.db")

# Create a cursor object
cursor = connection.cursor()

# Drop the existing tables if they exist
cursor.execute("DROP TABLE IF EXISTS employees")
cursor.execute("DROP TABLE IF EXISTS locations")
cursor.execute("DROP TABLE IF EXISTS salary")
cursor.execute("DROP TABLE IF EXISTS department")

# Create the tables
cursor.execute("""
CREATE TABLE department(
    DEPARTMENT_ID INTEGER PRIMARY KEY,
    DEPARTMENT_NAME VARCHAR(25)
);
""")

cursor.execute("""
CREATE TABLE locations(
    CITY_ID INTEGER PRIMARY KEY,
    CITY_NAME VARCHAR(25)
);
""")

cursor.execute("""
CREATE TABLE employees(
    EMP_ID INTEGER PRIMARY KEY,
    NAME VARCHAR(25),
    DEPARTMENT_ID INTEGER,
    CITY_ID INTEGER,
    FOREIGN KEY(DEPARTMENT_ID) REFERENCES department(DEPARTMENT_ID),
    FOREIGN KEY(CITY_ID) REFERENCES locations(CITY_ID)
);
""")

cursor.execute("""
CREATE TABLE salary(
    EMP_ID INTEGER,
    SALARY INT,
    FOREIGN KEY(EMP_ID) REFERENCES employees(EMP_ID)
);
""")

# Insert 30 records into the department table
departments = [
    (101, 'HR'), (102, 'Engineering'), (103, 'Marketing'), (104, 'Finance'), 
    (105, 'Sales'), (106, 'IT'), (107, 'Legal'), (108, 'Support'), 
    (109, 'Operations'), (110, 'Research'), (111, 'Logistics'), 
    (112, 'Administration'), (113, 'Procurement'), (114, 'Public Relations'), 
    (115, 'Customer Service'), (116, 'Quality Assurance'), (117, 'Training'), 
    (118, 'Compliance'), (119, 'Facilities'), (120, 'Maintenance'), 
    (121, 'Security'), (122, 'Business Development'), (123, 'Content'), 
    (124, 'Design'), (125, 'Advertising'), (126, 'Analytics'), 
    (127, 'Data Science'), (128, 'Product'), (129, 'Finance'), (130, 'Legal')
]

for dept in departments:
    cursor.execute("INSERT INTO department (DEPARTMENT_ID, DEPARTMENT_NAME) VALUES (?, ?)", dept)

# Insert 30 records into the locations table
cities = [
    (1, 'Mumbai'), (2, 'Delhi'), (3, 'Bangalore'), (4, 'Hyderabad'), 
    (5, 'Chennai'), (6, 'Kolkata'), (7, 'Pune'), (8, 'Ahmedabad'), 
    (9, 'Surat'), (10, 'Jaipur'), (11, 'Lucknow'), (12, 'Kanpur'), 
    (13, 'Nagpur'), (14, 'Indore'), (15, 'Thane'), (16, 'Bhopal'), 
    (17, 'Visakhapatnam'), (18, 'Pimpri-Chinchwad'), (19, 'Patna'), 
    (20, 'Vadodara'), (21, 'Ghaziabad'), (22, 'Ludhiana'), (23, 'Agra'), 
    (24, 'Nashik'), (25, 'Faridabad'), (26, 'Meerut'), (27, 'Rajkot'), 
    (28, 'Kalyan-Dombivli'), (29, 'Vasai-Virar'), (30, 'Varanasi')
]

for city in cities:
    cursor.execute("INSERT INTO locations (CITY_ID, CITY_NAME) VALUES (?, ?)", city)

# Insert 30 records into the employees table
employees = [
    (1, 'Alice', 101, 1), (2, 'Bob', 102, 2), (3, 'Charlie', 103, 3), 
    (4, 'David', 104, 4), (5, 'Eve', 105, 5), (6, 'Frank', 106, 6), 
    (7, 'Grace', 107, 7), (8, 'Hannah', 108, 8), (9, 'Ivy', 109, 9), 
    (10, 'Jack', 110, 10), (11, 'Kathy', 111, 11), (12, 'Leo', 112, 12), 
    (13, 'Mike', 113, 13), (14, 'Nina', 114, 14), (15, 'Olivia', 115, 15), 
    (16, 'Paul', 116, 16), (17, 'Quinn', 117, 17), (18, 'Rose', 118, 18), 
    (19, 'Steve', 119, 19), (20, 'Tina', 120, 20), (21, 'Uma', 121, 21), 
    (22, 'Victor', 122, 22), (23, 'Wendy', 123, 23), (24, 'Xander', 124, 24), 
    (25, 'Yara', 125, 25), (26, 'Zane', 126, 26), (27, 'Ann', 127, 27), 
    (28, 'Ben', 128, 28), (29, 'Cody', 129, 29), (30, 'Daisy', 130, 30)
]
for emp in employees:
    cursor.execute("INSERT INTO employees (EMP_ID, NAME, DEPARTMENT_ID, CITY_ID) VALUES (?, ?, ?, ?)", emp)

# Insert 30 records into the salary table
salaries = [
    (1, 60000), (2, 75000), (3, 85000), (4, 90000), (5, 95000), 
    (6, 80000), (7, 70000), (8, 67000), (9, 72000), (10, 77000), 
    (11, 68000), (12, 71000), (13, 76000), (14, 64000), (15, 69000), 
    (16, 62000), (17, 60000), (18, 63000), (19, 66000), (20, 74000), 
    (21, 75000), (22, 82000), (23, 87000), (24, 88000), (25, 90000), 
    (26, 91000), (27, 94000), (28, 95000), (29, 97000), (30, 99000)
]

for salary in salaries:
    cursor.execute("INSERT INTO salary (EMP_ID, SALARY) VALUES (?, ?)", salary)

# Commit changes and close the connection
connection.commit()
connection.close()