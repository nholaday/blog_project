## Blog site made using Django!

### To Run:
1. Create virtual environment
```
cd blog_project/
python3 -m venv venv
. venv/bin/activate
```
2. Install Requirements
```
pip install -r requirements.txt
```
3. Migrate database
```
python3 manage.py migrate
```
4. Run server
```
python3 manage.py runserver
```
5. Navigate to localhost:8000/ in your browser

### Features:
* Post Drafting and Publishing
* Comments
* User Login Page

![alt text](https://raw.githubusercontent.com/nholaday/blog_project/master/blogapp/static/media/post_list_screenshot.png)
