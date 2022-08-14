## REST API test automation in Python 🐍
[//]: # (Автоматизация тестирования REST API на Python )


- **Simple API requests** ⚙️
  - [x] Parsing JSON
  - [x] Headers
  - [x] Cookie
  - [x] Status code 
  - [x] Redirects (300 & 301)


- **Pytest** 🛠
  - [x] Pytest and simple tests
  - [x] Parameterized test
  - [x] Positive/negative authorization tests
  - [x] The setup() function in Pytest
  - [x] BaseCase
  - [x] Assertions


- **Creation of a framework & running in Docker** 🐳
  - [x] Create an existing user
  - [x] Creating a new user
  - [x] User View
  - [x] User editing
  - [x] Transferring a request to a method
  - [x] Replacing Methods
  - [x] Logging
  - [x] Allure (add: @allure.epic + @allure.description + with allure.step("abc"))
  - [ ] Environment
  - [ ] Running Tests in Docker


---
`pip3 install -r requirements.txt` -> _install packages from requirements file_

#### Pytest
`python3 -m pytest tests` -> _running tests (all)_

#### Allure
```
INSTALL ALLURE VERSION = 2.18.1

    curl -o allure-2.18.1.tgz -Ls https://repo.maven.apache.org/maven2/io/qameta/allure/allure-commandline/2.18.1/allure-commandline-2.18.1.tgz
    sudo tar -zxvf allure-2.18.1.tgz -C /opt/
    sudo ln -s /opt/allure-2.18.1/bin/allure /usr/bin/allure
    rm -rf allure-2.18.1.tgz
    allure --version
    
JAVA_JDK
    sudo apt install default-jdk

```

`python3 -m pytest --alluredir=test_results/ tests/test_user_auth.py` -> _running test with allure_

`allure serve test_results/` -> _allure report generation_

#### Environment
`export ENV=prod` / `export ENV=dev`-> _set environment variable: prod or dev (* - Linux)_

`echo $ENV` / `printenv ENV` -> _check variable value (* - Linux)_
