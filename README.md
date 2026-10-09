# Weather Forecast Application

A weather web application built with Django that displays current weather information for locations worldwide using the OpenWeather API.

## Features

* Search current weather by location.
* Display weather information retrieved from OpenWeather.
* Interactive popup notifications using Alertify.js.
* Responsive frontend built with HTML, CSS, JavaScript, and Bootstrap.

## Technologies Used

* **Backend:** Python, Django
* **Frontend:** HTML, CSS, JavaScript, Bootstrap
* **Notifications:** Alertify.js
* **API:** OpenWeather Current Weather API

## Installation and Setup

### 1. Clone the Repository

```bash
git clone <YOUR_REPOSITORY_URL>
cd <YOUR_PROJECT_FOLDER>
```

Replace the placeholders with your GitHub repository URL and project folder name.

### 2. Create a Virtual Environment

**Windows:**

```bash
python -m venv venv
```

**macOS / Linux:**

```bash
python3 -m venv venv
```

### 3. Activate the Virtual Environment

**Windows (Command Prompt):**

```cmd
venv\Scripts\activate.bat
```

**Windows (PowerShell):**

```powershell
.\venv\Scripts\Activate.ps1
```

**macOS / Linux:**

```bash
source venv/bin/activate
```

### 4. Install Dependencies

```bash
python -m pip install -r requirements.txt
```

### 5. Configure the OpenWeather API Key

1. Create an account at [OpenWeather](https://home.openweathermap.org/users/sign_up).
2. Generate an API key from your [OpenWeather API Keys page](https://home.openweathermap.org/api_keys).
3. Configure the key in the location expected by your project code.

Keep your API key private. If the project reads the key from a `.env` file, create that file locally and ensure it is excluded from Git using `.gitignore`.

### 6. Run Database Migrations

```bash
python manage.py migrate
```

### 7. Start the Development Server

```bash
python manage.py runserver
```

Open http://127.0.0.1:8000/ in your browser.

## Requirements

* Python
* pip
* An OpenWeather account and API key
* The dependencies listed in `requirements.txt`

## Notes

* Use a valid location supported by the OpenWeather API.
* API access may be subject to activation delays and usage limits.
* This application displays current weather data, not necessarily a multi-day forecast.

## License

Add a license if you intend to distribute this project for reuse. Otherwise, specify your chosen licensing terms before others reuse the code.
