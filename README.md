### INF601 - Advanced Programming in Python  
### Tanzeem Siddique  
### Final Project  

# Final Project - Django Weather-Based Clothing Recommendation App

'''
INF601 - Programming in Python
Final Project
I,     Tanzeem Siddique    , affirm that the work submitted for this assignment is entirely my own. I have not engaged in any form of academic dishonesty, including but not limited to cheating, plagiarism, or the use of unauthorized materials. I have neither provided nor received unauthorized assistance and have accurately cited all sources in adherence to academic standards. I understand that failing to comply with this integrity statement may result in consequences, including disciplinary actions as determined by my course instructor and outlined in institutional policies. By signing this statement, I acknowledge my commitment to upholding the principles of academic integrity.
'''

## Description

This project is a Django-based web application that recommends clothing to users based on real-time weather conditions using the OpenWeatherMap API (via RapidAPI). Users can input a location, receive clothing suggestions based on weather data, and rate the recommendations. It includes a complete login and registration system, a "My Ratings" history page, and Bootstrap styling with modal usage.

### Key features include:

* **Weather Lookup:** Users can input any city to fetch live weather data and get a clothing recommendation.
* **Clothing Recommendation:** Suggestions are based on weather temperature and conditions (rain, cold, etc.).
* **User Ratings:** After receiving a suggestion, users can rate and provide feedback on its accuracy or usefulness.
* **Login and Registration:** Includes both combined and separate pages for user login and registration.
* **User Logout:** Logged-in users can securely log out from the navigation bar.
* **My Ratings:** Users can view a history of all their past ratings and feedback.
* **Django Admin:** Admins can manage users, preferences, and ratings through Django’s admin interface.
* **Bootstrap Integration:** The app uses Bootstrap for responsive design and includes a modal confirmation popup after rating submission.

---

## Getting Started

### Dependencies

1. **Install Required Packages:**
    ```bash
    pip install -r requirements.txt
    ```

2. **Make Migrations:**
    ```bash
    python manage.py makemigrations
    ```

3. **Apply Migrations:**
    ```bash
    python manage.py migrate
    ```

4. **Create a Superuser (for Django Admin):**
    ```bash
    python manage.py createsuperuser
    ```

---

### Executing Program

1. **Run the Application:**
    ```bash
    python manage.py runserver
    ```

---

### Output

* **Homepage (Login/Register):** Navigate to `http://127.0.0.1:8000/`  
  Redirects to login/register if not logged in. Logged-in users can input their location.
  
* **Weather Recommendation:** Submitting a location displays current weather and clothing suggestions.  
  Example: `http://127.0.0.1:8000/result/`

* **Rate Suggestion:** After viewing the recommendation, users can submit a rating and feedback.

* **My Ratings:** Navigate to `http://127.0.0.1:8000/myratings/` to view a table of your submitted ratings.

* **Django Admin Panel:** Go to `http://127.0.0.1:8000/admin/` and log in with your superuser credentials.

* **About Page:** Navigate to `http://127.0.0.1:8000/about/` to learn more about the app.

---

## Authors

Tanzeem Siddique

---

## Acknowledgments

Resources and inspiration:
* [Django Documentation](https://docs.djangoproject.com/en/4.2/)
* [Bootstrap 5](https://getbootstrap.com/docs/5.3/getting-started/introduction/)
* [RapidAPI Weather](https://rapidapi.com/)
