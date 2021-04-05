# Interview Test Server

For the Points developer take-home assignment, the following task is required: you are to build a tax calculator against this API. The purpose is to develop an income tax calculator to help illustrate how marginal taxes work. This server is pretty simple, only returning the tax rates for a given year. You are to calculate the amount of taxes owed by inputting a yearly salary, then displaying the different rates, the total amount owed and the effective tax rates.

## Instructions

* Download and run this server (see [Getting Started](#getting-started))
* Build an application / tool in a language as agreed with your hiring manager:
    * Fetches the tax rates from this API server
    * Takes a yearly salary as input
    * Calculates and displays the total taxes owed for the salary
    * Displays the amount of taxes owed per band
    * Displays the effective rate

There are different levels to this assignment, level 1 being the easiest, level 2 having some gotchas, etc. If you complete a level with ease, feel free to jump to the next one. Please timebox your solution to one day total.

### Level 1

* Fetch the tax rates from this server at: http://localhost:5000/tax-calculator/brackets

### Level 2

* Fetch the tax rates by year: http://localhost:5000/tax-calculator/brackets/<2019|2020|...>

_Warning: this endpoint has gotchas_

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

* Implement your solution using a language agreed upon by your hiring manager.
* Include comments where you feel that they would be helpful.
* Include a README with instructions on how setup, run, and test the application.
* Include unit tests.

**If using JavaScript**

* Create a simple, yet visually appealing and responsive design.
* Target the latest stable version of Google Chrome.

**If using a backend language**

* Implement a simple yet intuitive command line interface.

**Code Formatting**

If using one of the following languages, make sure it adheres to the corresponding style guide:

* JavaScript : Eslint
* Python : PEP8
