# Health Tracker API

This project provides a RESTful API for tracking and analyzing health data, such as sleep and steps, using Django and Django REST framework. The API includes functionalities for analyzing users' health data to provide personalized advice using OpenAI's GPT model.

## Features

- **Health Data Analysis**: Analyze users' sleep and step count data to provide personalized advice.
- **Integration with OpenAI**: Use OpenAI's GPT model to generate personalized advice for users based on their health data.

## Requirements

- Django
- Django REST framework
- Python 3.x

## Installation

1. **Clone the repository**:
    ```sh
    git clone https://github.com/TigistW/task2.git
    cd health-tracker-api
    ```

2. **Create and activate a virtual environment**:
    ```sh
    python3 -m venv env
    source env/bin/activate
    ```

3. **Install the dependencies**:
    ```sh
    pip install -r requirements.txt
    ```

4. **Save the openai secret api key in settings.py**:

    ```
    OPENAI_API_KEY=your_openai_api_key
    ```

5. **Create a superuser**:
    ```sh
    python manage.py createsuperuser
    ```
6. **Create users** using the Django admin panel:

7. **Run the generate-apple-health-data.py** to generate fake health data from the users:

    ```
    python manage.py generate-apple-health-data
    ```
    
8. **Run migrations**:
    ```sh
    python manage.py migrate
    ```


9. **Run the development server**:
    ```sh
    python manage.py runserver
    ```

## API Endpoints

### Health Data Analysis

- **Get Health Conditions and AI Response**
    ```sh
    GET /api/health-stats/
    ```
    This endpoint returns users who meet certain health conditions and provides a personalized AI-generated response based on their data.

## Utility Functions

- **get_week_date_range(weeks_ago)**
    - Returns the start and end dates of the specified week.
- **generate_ai_response(user)**
    - Generates a personalized AI response for the user based on their health data.

## Models

- **AppleHealthStat**
    - Model to store health data (sleep analysis, step count).

## How to Contribute

1. Fork the repository.
2. Create a new branch for your feature or bugfix.
3. Make your changes.
4. Commit your changes with a clear message.
5. Push to your branch.
6. Create a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact

If you have any questions or suggestions, feel free to open an issue or contact the repository owner.

---

*Happy coding!*
