# Safe Space

### Contributors

### Reuben Kipkemboi
### Charity Mutembei
### Norah Waswala
### Kelvin Wepo

## Table of Content

+ [Description](#description)
+ [Installation Requirement](#installation-requirements)
+ [Technology Used](#technologies-used)
+ [License](#license)
+ [Authors Info](#authors-info)

## Description
How much is our generation broken? In the midst of any conflict there is  always a third party,   who is indirectly affected by the situation and most  of the time , they are children and they end up with some sort of trauma. Safe space is a Peer-Based Recovery Support platform that allows people  open up and heal from the past by joining live sessions , getting advice  and counselling  from other users who have overcame such situations.

[Go Back to the top](#safe-space)


## User Stories

- As a user I would like to login to the application if i want to.
- As a user I would like to comment on other peoples stories anonymously.
- As a user i would like to share my story in writing , and also be able to see other people's stories and be able to comment them.
- As a user I would like to see the user story in details

[Go Back to the top](##safe-space)

Home module

![Home page](./app/static/images/home1.png)

Users View

![logged in User](./app/static/images/logged.png)


## Behaviour Driven Development
| Behaviour | Input | Output |
| :---------------- | :---------------: | ------------------: |
| Application starts | **On page load** | Application hoe page/landing page |
| Login| **user email** and **user Password/passcode** | If account already exists redirect to home page. |
| Sign up/ Register | **Username**, **user email** **password** | Redirects to login page for user to login into the application|
| click on Create route | **Share story** | User make a story of previous experiences|
| Comment button | **button click** | users can give opinions on other peoples experiences|

## Installation Requirements

### Prerequisites

- pip
- gunicorn
- flask
- wtf-forms

## Instructions

1) Git clone the repository to your local computer
```
https://github.com/Reuben-Kipkemboi/Safe-Space.git
```
2. change Directory `cd` into safe

```
cd blog
```
3. create a virtual environment

```
python3.8 -m venv virtual
```
4. activate the virtual environment 
```
source virtual/bin/activate

```
5. To deactivate the environment

```
deactivate
```

6. Install Flask

```
pip install flask || pip3 install flask
```
7. Execute start.sh

```python

chmod a+x start.sh

./start.sh

```

[Go Back to the top](##safe-space)


## Technologies Used

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![HTML5](https://img.shields.io/badge/html5-%23E34F26.svg?style=for-the-badge&logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/css3-%231572B6.svg?style=for-the-badge&logo=css3&logoColor=white)
![Flask](https://img.shields.io/badge/flask-%23000.svg?style=for-the-badge&logo=flask&logoColor=white)
![Bootstrap](https://img.shields.io/badge/bootstrap-%23563D7C.svg?style=for-the-badge&logo=bootstrap&logoColor=white)
![Postgres](https://img.shields.io/badge/postgres-%23316192.svg?style=for-the-badge&logo=postgresql&logoColor=white)

## License
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

[MIT License](LICENSE)

## Design Link
* [Design](https://www.figma.com/file/pWbQO9a7W4LvFM6ArLdQhW/Safe-Space?node-id=0%3A1)

## Live Site

* #### safe-space22.herokuapp.com

## Authors Info

* [Reuben Kipkemboi](https://gmail.com) :email: 
* [Charity Mutembei](https://gmail.com) :email:
* [Norah Waswala](https://gmail.com) :email:
* [Kelvin Wepo](https://gmail.com) :email:


<p align = "center">
    &copy; 2022 @Group-Five-Invictus.
</p>