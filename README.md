# Tourist Destinations

A web application that helps users discover popular tourist destinations.

## Features

- **Search Destinations**: Users can search for various tourist destinations.
- **Destination Details**: Detailed information about each destination including images and descriptions.
- **User Authentication**: Secure login and registration for users.
- **Database Integration**: Stores user data and destination information in a SQLite database.

## Tech Stack

- **Backend**: Python, Django
- **Frontend**: HTML, CSS
- **Database**: SQLite

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/melbinproy2003/Tourist-destinations.git
   ```
2. Navigate to the project directory:
   ```bash
   cd Tourist-destinations
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Run migrations:
   ```bash
   python manage.py migrate
   ```
5. Start the development server:
   ```bash
   python manage.py runserver
   ```

## Usage

- Visit `http://127.0.0.1:8000/` in your browser.
- Register or log in to access all features.
- Search for destinations and view detailed information.

## Project Structure

- `guestapp/`: Main application directory.
- `media/`: Directory for media files such as images.
- `templates/`: HTML templates for the web application.
- `tourist_destinations/`: Additional project files and configurations.
- `db.sqlite3`: SQLite database file.
- `manage.py`: Django's command-line utility for administrative tasks.

## License

This project is licensed under the MIT License.

## Contact

For any inquiries or issues, please contact [melbinproy2003](https://github.com/melbinproy2003).

---

Feel free to customize this template further based on specific project needs.
