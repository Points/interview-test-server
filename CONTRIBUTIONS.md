# Interview Test Server

If you'd like to contribute, please submit a Pull Request to this repo.

## New Assignments

For new assignments, please add a new folder under [api](./api/) and keep the work isolated to there. If you wish to make improvements outside of the scope of your assignment, please submit another Pull Request. Your assignment should include:

* *INSTRUCTIONS.md*: a markdown file explaining the task
* HTML Instructions: An html page in the [templates folder](./templates/) containing similar contents to the newly created INSTRUCTIONS.md file
* `routes.py`: A list of routes relating to this assignment. The root should contain instructions, the sub-routes should contain restful endpoints. These endpoints will be linked at the bottom of [app.py](./app.py#L40).

_See the [tax calculator](./api/tax_calculator) assignment as an example implementation_

## Local Development

If you'd like to run it locally for development purposes, it runs like a typical flask app:

```python
export FLASK_APP=app:app
flask run [--reload]
# navigate to 127.0.0.1:5000
```
