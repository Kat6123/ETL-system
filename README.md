# ETL-system

System loads jobs from https://www.snap.com/en-US/jobs/ site and saves them in database.
It has an API which takes in location, and returns all the open job records in the database with the location.

### Requirements

- Based on Python 2.7
- PostgreSQL RSMDB
- Django
- Use pip to install all necessary modules
```sh
$ pip install -r /path/to/requirements.txt
```
- PyVirtualDisplay module needs Xvfb or Xephyr or Xvnc to be installed
```sh
$ sudo apt-get install xvfb xserver-xephyr vnc4server
```
- Selenium requires a driver to interface with the chosen browser. In this project Chrome is used. You can download here: https://sites.google.com/a/chromium.org/chromedriver/downloads
Make sure it’s in your PATH, e. g., place it in /usr/bin or /usr/local/bin or /path/to/virtualenv/bin.


### Installation

- Copy the repo
- Install requirements
- Create necessary table in databse using `schema.sql` script
- Change database connection params in `etl_system/settings.py` and `endpoint/endpoint/settings.py`
- Make migrations using
```sh
$ python endpoint/manage.py migrate
```
### Usage

##### 1. ETL

Using `etl_system` folder.

Run **all** ETL process with `ETL.py` script.
In this file you can set parametrs such as *SITE_URL*, *HTML_FILE*, *CSV_FILE*.

Use `crawler.py` to download *html page* from site with dynamic content.
```sh
$ ./crawler.py  https://www.snap.com/en-US/jobs/ snap.html
```

Use `extractor.py` to parse *html page* and extract jobs to *csv file*.
```sh
$ ./extractor.py  snap.html snap.csv
```

Use `loader.py` to load jobs from *csv file* to *database*.
```sh
$ ./loader.py  snap.csv
```

All functionality is located in `etl_functionality` module.

##### 2. Endpoint API
Run Django server
```sh
$ ./endpoint/manage.py runserver
```

Use API
```sh
$ curl http://localhost:port/jobs/London
```

### Authors
* **Katya Shilovskaya** - *Initial work* - [Kat6123](https://github.com/Kat6123)
