# Blog Personal con Django y Docker

Este proyecto es un blog personal básico desarrollado con Django y Docker. Permite crear y gestionar publicaciones, categorías y comentarios.

## Características

* Publicaciones con título, contenido, fecha de publicación y autor.
* Categorías para organizar las publicaciones.
* Comentarios para que los usuarios puedan interactuar con las publicaciones.
* Panel de administración de Django para gestionar el contenido.
* Contenedores Docker para un entorno de desarrollo y producción consistente.
* Base de datos PostgreSQL.

## Tecnologías Utilizadas

* Django
* Python
* PostgreSQL
* Docker
* HTML
* CSS

## Requisitos

* Docker y Docker Compose instalados.

## Configuración

1.  **Clonar el repositorio:**

    ```bash
    git clone https://github.com/DanielRodZa/BlogPersonal_ejemploDjango.git
    cd ../BlogPersonal_ejemploDjango
    ```

2.  **Construir y ejecutar los contenedores Docker:**

    ```bash
    docker-compose up --build
    ```

3.  **Aplicar las migraciones de Django:**

    ```bash
    docker-compose exec web python manage.py migrate
    ```

4.  **Crear un superusuario:**

    ```bash
    docker-compose exec web python manage.py createsuperuser
    ```

5.  **Acceder al blog en tu navegador:**

    [http://localhost:8000](http://localhost:8000)

6.  **Acceder al panel de administración:**

    [http://localhost:8000/admin](http://localhost:8000/admin)

## Estructura del Proyecto

```
BlogPersonal/
├── blog/
│   ├── migrations/
│   ├── init.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   └── views.py
├── personal_blog/
│   ├── init.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── manage.py
├── Dockerfile.python
├── Dockerfile.db
├── docker-compose.yml
└── requirements.txt
```

## Próximas Mejoras

* Implementar un sistema de autenticación para los usuarios.
* Agregar un editor de texto enriquecido para las publicaciones.
* Mejorar el diseño y la usabilidad del blog.
* Agregar pruebas unitarias y de integración.
* Implementar un sistema de búsqueda.
* Mejorar el frontend