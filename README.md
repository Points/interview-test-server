# Interview Test Server

Welcome to the Points developer take-home assignment.

Your task is to build an app against a small API. [Download the docker image](#Getting-started) onto your computer and run it locally. 

**Please timebox your solution to one day total.**

## Getting started

```bash
docker pull ptsdocker16/interview-test-server
docker run --init -p 5000:5000 -it ptsdocker16/interview-test-server
```

Navigate to [http://localhost:5000](http://localhost:5000). You should see a brief set of instructions. From there you'll be able to query the above endpoints and do your assignment. If you have any problems or need any sort of clarification, email the Team Lead or Engineering Hiring Manager for assistance.

## Submission Instructions

You can either submit your code as a zip file or send a link to a personal repository. Do not fork or submit pull requests to this repository. 

Please *do not fork or submit pull requests* to this repository.

Try to timebox your solution to 4 hours.

* Implement your solution using a language agreed upon by your hiring manager.
* Include comments where you feel that they would be helpful.
* Include a README with instructions on how setup, run, and test the application.
* Include unit tests.

**If using JavaScript**

* Create a simple, yet visually appealing and responsive design.
* Target the latest stable version of Google Chrome.

**If using a backend language**

* Implement a simple yet intuitive command line interface OR create an API endpoint to display the information in a JSON format.

**Code Formatting**

If using one of the following languages, make sure it adheres to the corresponding style guide:

* JavaScript : Eslint
* Python : PEP8
