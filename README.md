# Prueba Usuario SOP

## 1 Crear el entorno virtual
`python3 -m venv env`

## 2 Activamos el entorno

Windows
`cd env`
`cd Scripts`
`activate`

Mac
`source env/bin/activate`

## 3 Volvemos a la ruta raiz e instalamos requerimientos
`pip install --upgrade -r requirements.txt`

## 4 Ejecutamos el servidor para ambientes de prueba
`python manage.py runserver`

## Credenciales de acceso a las bases de datos ( Por prueba )

<!-- Postgres cluster usuariostest-postgres created
  Username:    postgres
  Password:    H1lA5LpxnCEASfp
  Hostname:    usuariostest-postgres.internal
  Proxy port:  5432
  Postgres port:  5433
  Connection string: postgres://postgres:H1lA5LpxnCEASfp@usuariostest-postgres.internal:5432 -->