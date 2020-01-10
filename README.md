# Olympic History Athletes API

## Setup Tasks
To run the routine to get the csv from Kaggle and save in database, it necessary run the command:
<code>python manage.py process_tasks"</code>


<h2>Methods</h2>

<h3>Update</h3>
To UPDATE some object use the PUT http method:
PUT https://olympic-history-athletes.herokuapp.com/api/{category}/{id}/
payload:
{"name": {new_attribute}}

<h3>Delete</h3>
To DELETE some object use the DELETE http method:
DELETE https://olympic-history-athletes.herokuapp.com/api/{category}/{id}/

<h3>Insert</h3>
To CREATE some object use the DELETE http method:
POST https://olympic-history-athletes.herokuapp.com/api/{category}
payload:
{"name": {new_attribute}}


<h2>Filtering Attributes</h2>
To filter attribute make a request to endpoint /api/<category>?name=<attribute>

Example:
https://olympic-history-athletes.herokuapp.com/api/sport/?name=Judo


<h2>Filtering Athletes</h2>
To filter athlete make a request to endpoint /api/athletes_search?<params>
Not work searching by the parameter id, just for the name.
It's able to put multiple filter.
Example:
https://olympic-history-athletes.herokuapp.com/api/athletes_search?medal=Silver&season=Summer

Available filters:
- games
- team
- season
- city
- sport
- event
- medal
