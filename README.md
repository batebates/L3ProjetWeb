# L3ProjetWeb

## Mise en place du projet
Si virtualenv n'est pas installé :


	pip install virtualenv

On créer l'environnement virtuel :


	cd
	virtualenv archiWeb

On lance l'environnement :


	source ./archiWeb/bin/activate	

On installe le projet :
On clone le projet et on installe les packets necessaires :


	git clone https://github.com/batebates/L3ProjetWeb.git
	pip install -r requirements.txt

On installe la base de donnée :


	cd BDR/
	python manage.py migrate
	python manage.py loaddata initial.yaml

On lance le serveur :


	python manage.py runserver

On peut maintenant se connecter au site à l'adresse 127.0.0.0:8000
