CREATE TABLE clients (
    id serial PRIMARY KEY,
    name VARCHAR(200),
    location VARCHAR(10000),
    phone VARCHAR
)

-- Verificador
SELECT * from clients