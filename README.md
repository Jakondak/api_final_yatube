### How to start:

Clone the repository and go to it on the command line:

```
git clone https://github.com/yandex-praktikum/kittygram.git
```

```
cd kittygram
```

Create and activate the vertual environment:

```
python3 -m venv env
```

```
source env/bin/activate
```

Install dependencies from the requirements.txt file:

```
python3 -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```

Make migrations:

```
python3 manage.py migrate
```

Start the project:

```
python3 manage.py runserver
```