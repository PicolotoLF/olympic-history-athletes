# Olympic History Athletes API

## Setup Tasks
To run the routine to get the csv from Kaggle and save in database, it necessary run the command:
<p><code>python manage.py process_tasks"</code>


<h2>Methods</h2>
<p>
<h3>Update</h3>
To UPDATE some object use the PUT http method:
<p>PUT https://olympic-history-athletes.herokuapp.com/api/{category}/{id}/
<p>payload:
<p><code>{"name": {new_attribute}}</code>

<h3>Delete</h3>
To DELETE some object use the DELETE http method:
<p>DELETE https://olympic-history-athletes.herokuapp.com/api/{category}/{id}/

<h3>Insert</h3>
To CREATE some object use the DELETE http method:
<p>POST https://olympic-history-athletes.herokuapp.com/api/{category}
<p>payload:
<p><code>{"name": {new_attribute}}</code>


<h2>Filtering Attributes</h2>
To filter attribute make a request to endpoint /api/<category>?name=<attribute>

<p>Example:
<p>https://olympic-history-athletes.herokuapp.com/api/sport/?name=Judo


<h2>Filtering Athletes</h2>
To filter athlete make a request to endpoint /api/athletes_search?<params>
<p>Not work searching by the parameter id, just for the name.
<p>It's able to put multiple filter.
<p>Example:
<p>https://olympic-history-athletes.herokuapp.com/api/athletes_search?medal=Silver&season=Summer

<h3>Available filters:</h3>
<ul>
  <li>games</li>
  <li>team</li>
  <li>season</li>
  <li>city</li>
  <li>sport</li>
  <li>event</li>
  <li>medal</li>
</ul>
