
# Lab 2

## Lab Introduction

In this lab, services are created leveraging Headers and Cookies.

## Description

The following project leverages fastapi and uvicorn to run http services. In the static services, you are able to see strings, an image, or a video. The dynamic routes take variables either in the route or through the query. The user can leverage the services to get a greeting with their name, calculate 2 numbers with a specified operation, or play rock paper scissors against a computer. 

## Design

The design has been split into 3 parts:

### Part 1: Simple Routes

These routes are created to return a static message.

### Part 2: Query String Routes

These routes utilize a query string after url.

### Part 3: Path Routes

These routes utilize path routes to get information for their respective methods.

## How To Run 

Install the proper libraries:

```
pip install fastapi uvicorn
```

Run the following command on your Github Repo directory:

```
uvicorn lab1:app --port 8080 --reload
```

## Simple Routes

### Service 1: Root Route

The root route service shows a string that says "original root route".

### Service 2: Image

The image service shows an image of a smiley face.

### Service 3: Video

The video service shows a 15-second video of a man walking through the woods.

### Service 4: Something

The something service shows a string saying "this is something".

## Query String Routes

### Service 1: Name

The name service shows a string that says Hello name! The name variable is received through a query.

### Service 2: Calculate

The calculate service grabs 2 numbers and performs an operation of the users choice. The num1, num2 and operation are received through a query.

### Service 3: Rock Paper Scissors

The Rock Paper Scissors (rps) service grabs a user choice of rock paper and scissors and compares it to a random computer choice. The string shows if the user wins, loses or draws with the computer in a game of rock paper scissors.

## Path Routes

### Service 1: Name

The name service shows a string that says Hello name! The name variable is received through a path.

### Service 2: Calculate

The calculate service grabs 2 numbers and performs an operation of the users choice. The num1, num2 and operation are received through a path.

### Service 3: Rock Paper Scissors

The Rock Paper Scissors (rps) service grabs a user choice of rock paper and scissors and compares it to a random computer choice. The string shows if the user wins, loses or draws with the computer in a game of rock paper scissors.
