# Task by "OnlineShopping"

## 1. Clone the Repository
git clone https://github.com/SanjarHikmatov/online_shopping
## 2. Change Directory
cd online_shoping
## 3. Create .env file using .env.example
cp .env.example .env
## 4. Create a virtual environment using Python 3.10 
python3 -m venv venv 
## 5. Activate the Virtual Environment On Linux/MacOS
source venv/bin/activate
## 5. Activate the Virtual Environment On Windows
venv\Scripts\activate
## 6. Install Packages from requirements.txt Inside the Virtual Environment:
pip install -r requirements.txt

## 7. Run the makemigrations and apply the changes to the database:
./manage.py makemigrations
./manage.py migrate
## 8. To start the server, run the following command inside your Django project directory:
./manage.py runserver
# Available APIs

1.Login API
   [http://127.0.0.1:8000/en/auth/login_page/](http://127.0.0.1:8000/en/auth/login_page/)

2.Register API
   [http://127.0.0.1:8000/en/auth/register_page/](http://127.0.0.1:8000/en/auth/register_page/)

3.Shop page
   [http://127.0.0.1:8000/en/products/](http://127.0.0.1:8000/en/products/)

4**Contact page**
   [http://127.0.0.1:8000/en/contact/](http://127.0.0.1:8000/en/contact/)

5.About page
   [http://127.0.0.1:8000/en/about/(http://127.0.0.1:8000/en/about/)