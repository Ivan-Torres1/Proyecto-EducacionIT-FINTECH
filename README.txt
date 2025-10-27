# 💳 Sistema de Gestión Fintech  
> Proyecto integrador - Etapa 1  
> Desarrollado en **Python** aplicando **Programación Orientada a Objetos (POO)**

---

## 🧠 Descripción del proyecto

Este sistema simula el funcionamiento de una **fintech** que ofrece servicios bancarios digitales.  
Permite la **gestión de clientes, cuentas y movimientos** (depósitos y retiros), manteniendo un registro detallado de todas las operaciones realizadas.

El desarrollo se basa en **buenas prácticas de POO**, aplicando principios como **abstracción, encapsulamiento, modularización y reutilización de código**.

---

## 🎯 Objetivos del sistema

- 🧍 **Gestión de clientes**:  
  Crear, modificar y eliminar clientes.  
  Cada cliente tiene un identificador único, nombre, apellido, DNI, correo electrónico y contraseña de acceso.

- 💰 **Gestión de cuentas bancarias**:  
  Crear cuentas asociadas a un cliente, con código único y saldo inicial configurable.

- 💸 **Movimientos**:  
  Registrar operaciones de depósito y retiro, almacenando tipo, monto y fecha del movimiento.

- 🧾 **Consulta de saldo**:  
  Permitir a los clientes visualizar su saldo actual.

---


mi_fintech/
│
├── main.py
│
├── mi_fintech/
│   ├── __init__.py
│   ├── database.py              # 🔹 configuración SQLAlchemy
│   │
│   ├── modelos/
│   │   ├── __init__.py
│   │   ├── usuario.py           # ahora hereda de Base (ORM)
│   │   ├── cuenta_bancaria.py
│   │   └── movimiento.py
│   │
│   ├── servicios/
│   │   ├── __init__.py
│   │   └── gestor_fintech.py    # usará sesiones de SQLAlchemy
│   │
│   └── utils/
│       └── validaciones.py
└── requirements.txt
