# Vodkaster movie scraper

---

This project consists of a small scraper for the website [Vodkaster](www.vodkaster.com). Given a movie URL, it automatically scrapes specific information (title, year, director, etc.) then writes everything to a Google Sheet.

### Usage

In order to add a line to the Google Sheet following the formatting:

```txt
year | title | director | country | genre | duration
```

You can simply write the following:

```bash
$ python main.py <movie-url>
```

### Installation

In order to setup the project, you will need to go through two major steps:

1. *Install the Python repository*:

I worked on the project through a virtual environment with `virtualenvwrapper`
and I highly recommend to do so as well. However, whether or not you are in a
virtual environment, the installation proceeds as follows:

* To download and install the source code of the project without a virtual environment:

  ```bash
    $ cd <directory you want to install to>
    $ git clone https://github.com/QDucasse/vodkaster
    $ python setup.py install
  ```
* To download and install the source code of the project in a new virtual environment:  

  *Download of the source code & Creation of the virtual environment*
  ```bash
    $ cd <directory you want to install to>
    $ git clone https://github.com/QDucasse/vodkaster
    $ cd vodkaster
    $ mkvirtualenv -a . -r requirements.txt VIRTUALENV_NAME
  ```
  *Launch of the environment & installation of the project*
  ```bash
    $ workon VIRTUALENV_NAME
    $ pip install -e .
  ```

2. *Setup your Google Sheet*:

In order for the project to run correctly, you need to setup your Google Sheet accordingly:

- Go to the [Google API Console](https://console.developers.google.com/).
- Create a new project.
- Click on ***Enable API*** and search for ***Google Sheet API / Google Drive API***.
- Click on ***Create credentials***, specify ***Webserver*** and ***Application Data***.
- Download the JSON file.
- Copy the file to the `vodkaster` root directory and rename it `client_secret.json`
- In your actual Google Sheet, ***Share*** the document with the email address that can be found under the field `client_email` in the `client_secret.json` file.
- Go to `writer.py` and modify the `open_sheet()` method with the correct name for your sheet. (For me it is `Films/séries`)

You are now ready to use the scraper/writer combination!



