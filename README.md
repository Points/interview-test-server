# Interview Test Server

Welcome to the Points developer take-home assignment.

Your task is to build an app against a small API. You can [download the docker image](#get-up-and-running) onto your computer and run it locally. 

## The Assignment - Tax Calculator

Your task is to build an application that queries our dockerized API and displays the calculated total income tax for a given salary and tax year.
You may refer to this resource for context [on how to calculate total income tax](https://investinganswers.com/dictionary/m/marginal-tax-rate#:~:text=To%20calculate%20marginal%20tax%20rate) using marginal tax rates.

Please [see the official reference to tax brackets](https://www.canada.ca/en/financial-consumer-agency/services/financial-toolkit/taxes/taxes-2/5.html) and rates for more information.

## What we're looking for

The goal of this assessment is to provide a picture of your approach to development as it relates to:

* Design patterns/programming paradigm
* Scalability
* API interface design
* Frameworks
* Documentation
* Clean code
* UI
* Testing
* Automated testing
* Error handling
* Logging
* Readability

### For backend candidates

The application you’re building should have an HTTP API with an endpoint that takes an annual income and the tax year as parameters. The appropriate type of params (query vs body param vs URL etc.) is to be determined by you. Your endpoint should return a JSON object with the result of the calculation.

### For frontend candidates

The application should have a very basic UI with a form that accepts two inputs: annual income and the tax year. On form submission, the UI should print either an error or the total income tax for the inputted parameters. Feel free to use the frontend application framework that you're most comfortable with.

### In both cases, it should:

#### Accomplish the following:

* Fetch the tax rates by year i.e. 
  [/tax-calculator/tax-year/[2019|2020|2021|2022]](/tax-calculator/tax-year/2022)
* Receive a yearly salary
* Calculate and display the total taxes owed for the salary
* Display the amount of taxes owed per band
* Display the effective rate

#### Apply to the following 2022 tax year scenarios:

| Salary      | Total Taxes |
|-------------|-------------|
| $0 <=       | $0          |
| $50,000     | $7,500.00   |
| $100,000    | $17,739.17  |
| $1,234,567  | $385,587.65 |

### Sample Request

Please find a sample request at [/tax-calculator/](http://localhost:5001/tax-calculator/), 
which contains a reliable API endpoint and can be used for test and development purposes. 
It returns the following JSON response: 


```json
{
  "tax_brackets": [
    {
        "min": 0,
        "max": 50197,
        "rate": 0.15
    },
    {
        "min": 50197,
        "max": 100392,
        "rate": 0.205
    },
    {
        "min": 100392,
        "max": 155625,
        "rate": 0.26
    },
    {
        "min": 155625,
        "max": 221708,
        "rate": 0.29
    },
    {
        "min": 221708,
        "rate": 0.33
    }
  ]
}

```


### Please Note

Be aware that we’ve baked in two errors in our mock API — you may handle them and anything else you see fit to handle accordingly:

* only years 2019, 2020, 2021 and 2022 are supported
* the API throws errors randomly

These occur on the [/tax-calculator/tax-year/2022](/tax-calculator/tax-year/2022) endpoint, **which your assignment will be evaluated against**.

##  IMPORTANT

Design the application as you would a production app that you and your team are collaborating on. Your result should not be a proof of concept and should focus more on the assessment criteria listed below than on working code.

## Get up and running

In order to run the API locally, please follow these instructions:

```bash
docker pull ptsdocker16/interview-test-server
docker run --init -p 5001:5001 -it ptsdocker16/interview-test-server
```

Navigate to [http://localhost:5001](http://localhost:5001). You should be greeted with this set of instructions, and access to the different available endpoints. The following are the relevant endpoints:

* [/tax-calculator/](http://localhost:5001/tax-calculator/) - endpoint to develop against
* [/tax-calculator/tax-year/2022](/tax-calculator/tax-year/2022) - endpoint you'll be assessed against

If you have any problems or need any sort of clarification, email the engineering hiring manager for assistance.

## Results submission

You can either submit your code as a zip file or send a link to a personal repository. Do not fork or submit pull requests to this repository. 

Please be prepared to provide a walkthrough of your solution during the first 45 mins of the technical panel interview.

## Timeframe

We respect your time and understand that you may have other commitments. As such, our assignment is designed to be completed in 4 hours or less. Please try to timebox your effort.
