# FlaskList

FlaskList is a minimalist Flask-based project designed for rapid prototyping or as a foundation for more complex applications.

## Project Structure

- `app.py`: Main application file that runs the Flask server.
- `config.py`: Configuration file for the app.
- `models.py`: Database model definitions.
- `routes.py`: Route definitions for the app.
- `static/`: Directory for static files (CSS, JavaScript, images).
- `templates/`: Directory for HTML templates.

## Setup Instructions

Follow the steps below to set up a virtual environment and install the required dependencies.

### 1. Clone the repository

```bash
git clone https://github.com/Zephir0g/Flask_1hr.git
cd Flask_1hr
```

### 2. Create and activate a virtual environment

```bash
# On Windows
python -m venv venv
venv\Scripts\activate

# On macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the application

```bash
python app.py
```

Once started, the app will be accessible at `http://127.0.0.1:5000/`.

## Requirements

- Python 3.x
- Flask (as specified in `requirements.txt`)

