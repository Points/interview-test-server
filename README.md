# Interview Test Server

For the Points developer take-home assignment, the following task is required: you are to build a tax calculator against
 this API. The purpose is to develop an income tax calculator to help illustrate how marginal taxes work. This server is
  pretty simple, only returning the tax rates for a given year. You are to calculate the amount of taxes owed by 
  inputting a yearly salary, then displaying the different rates, the total amount owed and the effective tax rates.

For all of the below assignments there are different levels that you can work on:
 * **Level 1:** The easier level, the API always behaves and the response never changes.
 * **Level 2:** More difficult, the API doesn't always behave and includes gotchas.
 
If you complete the first level with ease, feel free to jump to the next one. 

**Please timebox your solution to one day total.**

## Assignment 1: Tax Calculator

### Instructions

* Download and run this server (see [Getting Started](#getting-started))
* Build an application / tool in React or Python with the following criteria:
    * Fetches the tax rates from this API server
    * Takes a yearly salary as input
    * Calculates and displays the total taxes owed for the salary
    * Displays the amount of taxes owed per band
    * Displays the effective rate

### Level 1

* Fetch the tax rates from this server at: [localhost:5000/tax-calculator/brackets](http://localhost:5000/tax-calculator/brackets)

### Level 2

* Fetch the tax rates by year: [localhost:5000/tax-calculator/brackets/<2019,2020...>](http://localhost:5000/tax-calculator/brackets/2020)

_Warning: this endpoint has gotchas_

## Assignment 2: Autonomous Car

### Description

Points is developing an autonomous vehicle program. It's going well, but we need to iron out a few bugs. The 
 Engineering Team would like to demo our progress to the Product Team, so we need to develop a tool that can take 
 track and travel log data, and then determine whether our autonomous vehicle successfully navigated the track.

Track and travel log data are encoded as JSON. The "track" array contains entries for any position of the track where 
 there is an obstacle in any of the 3 lanes (`"a"`, `"b"` or `"c"`). The "travelLog" array contains entries for any 
 position of the track where the car has changed lanes, either to the `"left"` or `"right"`.

The autonomous car starts at position `0` on lane `"b"`, drives itself to the end of the track and can shift only one
 lane per position. The simulation should end when the car hits an obstacle, goes out-of-bounds, or when all "track" 
 and "travelLog" entries have been processed.
 
### Instructions

1. Download and run this server (see [Getting Started](#getting-started))
2. Build an application / tool in JavaScript or Python with the following criteria:
   * Fetches an autonomous car route JSON object from this API server (see the different levels below). 
   * Use the route object's "track" & "travelLog" information to determine if the simulation will end successfully or
     if it will fail. 
   * If the simulation results in a success, the application must return the following success response:
     ```json 
     {"status":  "success"}
     ```
   * If the simulation results in a failure (running out of bounds or hitting an obstacle), the application must 
     return an error response showing at which position the simulation fails:
     ```json 
     {"status":  "error", "position": 2}
     ```
            
### Level 1

For this level, you can use fetch a static route object from each of the following endpoints:
 * [/autonomous-car/routes/empty-route](http://localhost:5000/autonomous-car/routes/empty-route) will return a route
   object with an empty "track" and "travelLog" arrays.
 * [/autonomous-car/routes/success-no-obstacles](http://localhost:5000/autonomous-car/routes/success-no-obstacles) 
   will return a route object that should result in a successful simulation, **with zero obstacles on the track**.
 * [/autonomous-car/routes/success-with-obstacles](http://localhost:5000/autonomous-car/routes/success-with-obstacles) 
   will return a route object that should result in a successful simulation, **with obstacles on the track**.
 * [/autonomous-car/routes/failure-out-of-bounds](http://localhost:5000/autonomous-car/routes/failure-out-of-bounds) 
   will return a route object that should result in failure due to running out of bounds.
 * [/autonomous-car/routes/failure-hits-obstacle](http://localhost:5000/autonomous-car/routes/failure-hits-obstacle) 
   will return a route object that should result in failure due to running into an obstacle.


### Level 2

For this level, you can fetch a random route (including the empty-route) using the endpoint:
* [/autonomous-car/routes/random](http://localhost:5000/autonomous-car/routes/random)
* *Warning: this endpoint has gotchas*


## Getting started

```bash
docker pull ptsdocker16/interview-test-server
docker run --init -p 5000:5000 -it ptsdocker16/interview-test-server
```

Navigate to http://localhost:5000. You should see a brief set of instructions. From there you'll be able to query the above endpoints and do your assignments. If you have any problems, email the Team Lead or Engineering Hiring Manager for assistance.

## Submission Instructions

You can either submit your code as a zip file or send a link to a personal repository. Do not fork or submit pull requests to this repository. Please submit within a week or 2 of receipt of instructions, unless otherwise specified.

Please *do not fork or submit pull requests* to this repository.

Please timebox your solution to one day total.

* Implement your solution using JavaScript or Python.
* Include comments where you feel that they would be helpful.
* Include a README with instructions on how setup, run, and test the application.
* Include unit tests.

**If using JavaScript**

* Create a simple, yet visually appealing and responsive design.
* Target the latest stable version of Google Chrome.
* Format the code according to the latest eslint specs

**If using Python**

* Implement a simple yet intuitive command line interface.
* Format the code following PEP8 guidelines