# SoftDesk Support API

API REST securisee de gestion de projets, issues et commentaires pour SoftDesk Support, une application B2B de suivi de problemes techniques.

## Fonctionnalites

- Inscription avec age minimum de 15 ans et consentements RGPD
- Authentification JWT avec tokens d'acces et de rafraichissement
- Consultation, modification et suppression de son profil
- Creation, lecture, modification et suppression de projets
- Gestion des contributeurs par l'auteur du projet
- Creation, lecture, modification et suppression d'issues
- Assignation d'une issue uniquement a un contributeur du projet
- Creation, lecture, modification et suppression de commentaires
- Permissions : seuls les contributeurs accedent aux ressources d'un projet ; seul l'auteur modifie ou supprime sa ressource
- Pagination par 10 elements des listes de projets, contributeurs, issues et commentaires

## Stack

- Python 3
- Django 6
- Django REST Framework
- Simple JWT
- SQLite

## Installation

Prerequis : Python 3 et `pip`.

```bash
python3 -m venv .venv
./.venv/bin/pip install -r requirements.txt
./.venv/bin/python manage.py migrate
./.venv/bin/python manage.py runserver
```

L'API est accessible sur `http://127.0.0.1:8000/`.

## Authentification

Creer un compte avec `POST /api/register/`, puis obtenir des tokens avec `POST /api/token/`. Envoyer le token d'acces dans les requetes protegees :

```text
Authorization: Bearer <access_token>
```

## Routes Principales

- `POST /api/register/`
- `GET`, `PATCH`, `DELETE /api/profile/`
- `POST /api/token/`
- `POST /api/token/refresh/`
- `GET`, `POST /api/projects/`
- `GET`, `PATCH`, `DELETE /api/projects/<project_id>/`
- `GET`, `POST /api/projects/<project_id>/contributors/`
- `DELETE /api/projects/<project_id>/contributors/<contributor_id>/`
- `GET`, `POST /api/projects/<project_id>/issues/`
- `GET`, `PATCH`, `DELETE /api/projects/<project_id>/issues/<issue_id>/`
- `GET`, `POST /api/projects/<project_id>/issues/<issue_id>/comments/`
- `GET`, `PATCH`, `DELETE /api/projects/<project_id>/issues/<issue_id>/comments/<comment_id>/`

## Commandes Utiles

```bash
./.venv/bin/python manage.py check
./.venv/bin/python manage.py makemigrations
./.venv/bin/python manage.py migrate
./.venv/bin/python manage.py createsuperuser
./.venv/bin/python -m flake8 projects issues comments
./.venv/bin/python manage.py test
```

## Parcours Principal

1. Un utilisateur cree un compte et obtient un token JWT.
2. Il cree un projet et devient automatiquement son auteur et contributeur.
3. L'auteur ajoute des contributeurs au projet.
4. Les contributeurs creent et consultent les issues du projet.
5. Les contributeurs ajoutent des commentaires aux issues.
6. Seul l'auteur d'un projet, d'une issue ou d'un commentaire peut le modifier ou le supprimer.

## Structure

- `users/` : utilisateur, inscription et profil RGPD
- `projects/` : projets et contributeurs
- `issues/` : issues d'un projet
- `comments/` : commentaires d'une issue
- `config/` : configuration Django et routes principales
