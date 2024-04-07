# SoftDesk
![image](https://github.com/Roxhe/softdesk/assets/88476983/4877cad4-6f61-4ac0-866b-ecc802e67342)
SoftDesk Support est une application permettant de remonter et suivre des problèmes techniques. Cette solution s’adresse à des entreprises en B2B (Business to Business).

Ce travail est issu du projet 10 de la formation DA Python OpenClassrooms.

Il est développé avec [Python 3.11](https://www.python.org/downloads/release/python-3110/) sur Windows 11 Pro.

#### Cloner le projet, installer l'environnement virtuel et l'activer :

Rendez vous dans le dossier de votre choix et cloner le projet avec : \
`git clone https://github.com/Roxhe/softdesk.git`

Rendez vous dans le dossier du projet avec `cd softdesk`, puis installer l'environnement virtuel avec : \
`python -m venv 'env'`  

Puis activez le avec : \
`source env/Scripts/activate`

#### Installer les modules nécessaire dans l'environnement virtuel :

Toujours dans le dossier du projet, exécuter : \
`pip install -r requirements.txt`

Puis rendez-vous dans le dossier de l'application avec `cd softdesk`.

Une fois dans le dossier, exécutez : \
`python manage.py makemigrations` puis `python manage.py migrate` 

Puis lancez l'API sur votre serveur local en exécutant la commande : \
`python manage.py runserver`

#### Effectuer les tests de l'API :

Lancez votre navigateur et rendez vous sur l'adresse `http://127.0.0.1:8000`
ou \
Utiliser un outil comme [Postman](https://www.postman.com)
