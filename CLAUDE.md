# CLAUDE.md for carbonbyte

## Run Commands
- Start server: `python app.py`
- Install dependencies: `pip install -r requirements.txt`
- Database initialization: Flask automatically creates SQLite DB at first run

## Code Style Guidelines
- **Project Structure**: Flask with blueprints (routes/auth.py, routes/main.py)
- **Imports**: Group in order: standard library, third-party, local application
- **Naming**:
  - Variables/functions: snake_case
  - Classes: PascalCase
  - Blueprint routes: prefix with blueprint name
- **Type Annotations**: Use Python type hints for function parameters and returns
- **Error Handling**: Use try/except blocks with specific exceptions
- **Database**: SQLAlchemy ORM models defined in models/ directory
- **Templates**: Jinja2 HTML templates in templates/ directory
- **Form Validation**: Use Flask-WTF for form handling and validation
- **Authentication**: Implement via Flask-Login

## Project Context
carbonbyte is a web application for calculating carbon footprints of digital products with authentication, data storage, and export capabilities.