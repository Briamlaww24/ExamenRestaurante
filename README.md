# Restaurante Bien Pro

Aplicación Django para administrar las categorías y los platos de la carta. El inicio muestra el total de platos registrados, el total disponible y el menú para pedidos.

## Instalación y ejecución

Requiere Python 3.12 o superior. Ejecuta estos comandos desde la carpeta que contiene `manage.py`.

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

En PowerShell, crea el entorno con `py -m venv .venv` y actívalo con `.\.venv\Scripts\Activate.ps1`.

Abre la aplicación en http://127.0.0.1:8000/. La configuración incluida usa SQLite mediante el archivo `db.sqlite3`. La base entregada contiene tres categorías y cinco platos, de los cuales tres están disponibles.

## Uso

- En **Categorías de Platos** puedes crear y editar categorías y consultar los platos asociados. Si intentas eliminar una categoría con platos, la aplicación muestra un aviso y conserva los registros.
- En **Platos** puedes crear, consultar, editar y eliminar platos. El listado administrativo muestra la disponibilidad de cada plato y ofrece diez registros por página.
- En **Inicio**, el menú para pedidos muestra únicamente platos disponibles.

Para acceder al panel en http://127.0.0.1:8000/admin/, crea un usuario administrador con `python manage.py createsuperuser`.
