
# Lab 2

## Lab Introduction

In this lab, services are created using Headers and Cookies. A second python file is created to test the services.

## Description

The following project leverages fastapi and uvicorn to run http services. The goal of this lab is to get familiar with Headers and Cookies. Headers use the GET request and Cookies use the POST request.. Along with the services, the file test_Lab2.py is used to test each individual service.

## Design

The design has been split into 3 parts:

### Part 1: Header Routes

These routes utilize Headers to use data.

### Part 2: Cookies Routes

These routes utilize Cookies to use data.

### Part 3: Testing

The tests are created to ensure that each service works as intended.

## How To Run Lab2.py

Install the proper libraries:

```
pip install fastapi uvicorn, httpx, pytest
```

Run the following command on your Github Repo directory:

```
uvicorn lab2:app --port 8080 --reload
```

## How to Run test_Lab2.py

Assuming you have installed the proper libraries and have followed the steps above

Run the following command on your cloned Repo directory

```
pytest ./test_Lab2.py
```