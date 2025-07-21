 CREATE TABLE usuarios (
  id SERIAL PRIMARY KEY,
  nombre VARCHAR(100),
  email VARCHAR(100) UNIQUE,
  telefono VARCHAR(20),
  direccion TEXT,
  password_hash TEXT
);

CREATE TABLE productos (
  id SERIAL PRIMARY KEY,
  nombre VARCHAR(100),
  descripcion TEXT,
  precio NUMERIC(10,2),
  stock INT,
  imagen_url TEXT
);

CREATE TABLE pedidos (
  id SERIAL PRIMARY KEY,
  usuario_id INT REFERENCES usuarios(id),
  fecha TIMESTAMP DEFAULT NOW(),
  estado VARCHAR(50),
  total NUMERIC(10,2)
);

CREATE TABLE pedido_detalle (
  id SERIAL PRIMARY KEY,
  pedido_id INT REFERENCES pedidos(id),
  producto_id INT REFERENCES productos(id),
  cantidad INT,
  precio_unitario NUMERIC(10,2)
);

CREATE TABLE pagos (
  id SERIAL PRIMARY KEY,
  pedido_id INT REFERENCES pedidos(id),
  metodo VARCHAR(50) DEFAULT 'Yape',
  monto NUMERIC(10,2) NOT NULL,
  estado VARCHAR(20) DEFAULT 'pendiente',
  fecha TIMESTAMP DEFAULT NOW(),
  referencia_yape VARCHAR(100),
  comprobante_url TEXT
);
