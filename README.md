# Jokes
This program is for practical purposes making use of technologies with Flask to create a REST API.

## Requirements
***The requirements are in the file [requirements.txt](requirements.txt)*** 

```bash
sudo apt-get install libpq-dev python3-dev
sudo pip3 install -r requirements.txt

or in a more traditional way

pip3 install flask flask-cors python-decouple psycopg2 python-dotenv flask-sqlalchemy flask-marshmallow marshmallow-sqlalchemy requests

--------------------------------------------------------------
In addition to this, the db.sql file is added to be executed in the database, which in this case is called squad_joke, the db data is in the .env file

```
## Quick Start
```bash
python3 src/app.py
```
## Example and EndPoints

​		http://127.0.0.1:5000/api/jokes/   _get a random joke_

​		http://127.0.0.1:5000/api/jokes/<id>   _get a specific joke_

​		http://127.0.0.1:5000/api/jokes/Chuck   _get a random joke from https://api.chucknorris.io _

​		http://127.0.0.1:5000/api/jokes/Dad   _get a random joke from https://icanhazdadjoke.com/ _

​		http://127.0.0.1:5000/api/jokes/add   _add a joke_
​				{
​                    "joke": "mi primer chiste"
​                }
​		http://127.0.0.1:5000/api/jokes/update/<id>   _update a joke_
​				{
​                    "joke": "mi primer chiste modificado"
​                }
​		http://127.0.0.1:5000/api/jokes/delete/<id>   _delete a joke_


## Observation
This time i didn't use swagger as flask-restplus didn't work in conjunction with flask to make use of swagger with recent python versions, for this reason the consumptions are made with postman.

## License
This program is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation; either version 3 of the License, or any later version.

This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with this program; if not, write to the Free Software Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA 02111-1307 USA

See './LICENSE' for more information.
