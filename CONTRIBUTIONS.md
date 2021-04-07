# Interview Test Server

If you'd like to contribute, please submit a Pull Request to this repo.

## New Assignments

For new assignments, please add a new folder under [api](https://github.com/Points/interview-test-server/tree/master/api)
 and keep the work isolated to there. If you wish to make improvements outside of the scope of your assignment, 
 please submit them under another Pull Request.

You can link the routes to your assignment at the bottom of 
[app.py](https://github.com/Points/interview-test-server/blob/master/app.py#L37).

## Local Development

If you'd like to run it locally for development purposes, it runs like a typical flask app:

```python
export FLASK_APP=app:app
flask run [--reload]
# navigate to 127.0.0.1:5000
```

## What is next
 - [ ] Update repository to include everything from the 
       [older developer assignment instruction repository](https://github.com/Points/developer-assignment-instructions)
       and update the README to include the description of the repo and a better break down of what it holds and how to
       use it.
 - [ ] Update the instruction HTML pages (functional) 
 - [ ] Update the instruction HTML pages (pretty and modern) 
 - [ ] Add more tax-brackets from the [Canadian federal income tax rates](https://www.canada.ca/en/revenue-agency/services/tax/individuals/frequently-asked-questions-individuals/canadian-income-tax-rates-individuals-current-previous-years.html#federal)
       and more autonomous car routes.
 - [ ] Improve endpoints, error messages and HTTP guidelines 