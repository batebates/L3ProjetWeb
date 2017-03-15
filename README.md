<a href="https://codeclimate.com/github/batebates/L3ProjetWeb"><img src="https://codeclimate.com/github/batebates/L3ProjetWeb/badges/gpa.svg" /></a>
<a href="https://codeclimate.com/github/batebates/L3ProjetWeb"><img src="https://codeclimate.com/github/batebates/L3ProjetWeb/badges/issue_count.svg" /></a>

# L3ProjetWeb

## Mise en place du projet
Si virtualenv n'est pas installé :


	pip install virtualenv

On lance créer l'environnement virtuel :


	cd
	virtualenv archiWeb

On lance l'environnement :


	source ./archiWeb/bin/activate	

On install le projet :
On clone le projet et on install les packets necessaires :


	git clone https://github.com/batebates/L3ProjetWeb.git
	pip install -r requirements.txt

On install la base de donnée :


	cd BDR/
	python manage.py migrate
	python manage.py loaddata initial.yaml

On lance le server :


	python manage.py runserver

On peut maintenant se connecter au site à l'adresse 127.0.0.0:8000
