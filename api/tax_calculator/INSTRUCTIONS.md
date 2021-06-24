## Tax Calculator

The purpose is to develop an income tax calculator to help illustrate how marginal taxes work. This server is pretty simple, only returning the tax rates for a given year. You are to calculate the amount of taxes owed by inputting a yearly salary, then displaying *the rates per bracket*, *the total amount owed* and *the effective tax rates*.

_[What are marginal tax rates?](https://investinganswers.com/dictionary/m/marginal-tax-rate#:~:text=To%20calculate%20marginal%20tax%20rate,bracket%20your%20current%20income%20falls)_

There are two different levels, if you complete the first one with ease, feel free to work on the next one, which returns similar information, but sometimes the API will throw an error.

**Please timebox your solution to about 4 hours**

### Instructions

* Download and run this server (see [Getting Started](../../README.md#getting-started))
* Build an application / tool in a language as agreed with your hiring manager:
    * Fetches the tax rates from this API server
    * Takes a yearly salary as input
    * Calculates and displays the total taxes owed for the salary
    * Displays the amount of taxes owed per bracket
    * Displays the effective rate

### Level 1

* Fetch the tax rates from this server at: [localhost:5000/tax-calculator/brackets](http://localhost:5000/tax-calculator/brackets)

### Level 2
_sometimes returns bad responses, handle accordingly_

* Fetch the tax rates by year: [localhost:5000/tax-calculator/brackets/<2019,2020...>](http://localhost:5000/tax-calculator/brackets/2020)
