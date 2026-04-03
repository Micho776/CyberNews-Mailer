# CyberNews Mailer 🛡️

Script Python qui récupère automatiquement les dernières news
cybersécurité via l'API NewsAPI et les envoie par email.

Réalisé dans le cadre du cours Scripting Python — B2 CS (EFREI 2025-2026)

---

## Fonctionnement

1. Appel à l'API NewsAPI pour récupérer les 5 derniers articles
2. Mise en forme des articles en texte lisible
3. Envoi par email via Gmail (SMTP SSL)
4. Sauvegarde des articles dans un fichier log `.txt`

---

## Installation

### 1. Cloner le repo

```bash
git clone https://github.com/ton-user/cybernews-mailer.git
cd cybernews-mailer
```

### 2. Créer un environnement virtuel

```bash
python -m venv .venv
.venv\Scripts\activate        # Windows
source .venv/bin/activate     # Linux/macOS
```

### 3. Installer les dépendances

```bash
pip install requests
```

---

## Configuration

Le script utilise des variables d'environnement pour ne jamais
stocker de credentials dans le code.

| Variable        | Description                        |
|-----------------|------------------------------------|
| `NEWS_API_KEY`  | Clé API NewsAPI (newsapi.org)      |
| `EMAIL_FROM`    | Adresse Gmail d'envoi              |
| `EMAIL_PASS`    | App Password Gmail (16 caractères) |
| `EMAIL_TO`      | Adresse email de réception         |

### Obtenir une clé NewsAPI

Créer un compte gratuit sur https://newsapi.org

### Obtenir un App Password Gmail

1. Activer la validation en deux étapes sur ton compte Google
2. Aller sur https://myaccount.google.com/apppasswords
3. Créer un mot de passe pour "Mail"
4. Copier le code à 16 caractères généré

### Configurer les variables

Windows (PowerShell) :

```powershell
$env:NEWS_API_KEY = "ta_cle_api"
$env:EMAIL_FROM   = "expediteur@gmail.com"
$env:EMAIL_PASS   = "app_password_16_chars"
$env:EMAIL_TO     = "destinataire@email.com"
```

Linux/macOS :

```bash
export NEWS_API_KEY="ta_cle_api"
export EMAIL_FROM="expediteur@gmail.com"
export EMAIL_PASS="app_password_16_chars"
export EMAIL_TO="destinataire@email.com"
```

---

## Utilisation

```bash
python news_mailer.py
```

Exemple de sortie :

```
Recuperation des news : cybersecurity...
Cybersecurity News — 03/04/2026
==================================================
1. OpenSSH vulnerability patched
   Source  : The Hacker News
   Publie  : 2026-04-03
   Lien    : https://...

Email envoye a destinataire@email.com
Log sauvegarde : news_2026-04-03.txt
```

---

## Structure du projet

```
cybernews-mailer/
├── news_mailer.py       # script principal
├── news_YYYY-MM-DD.txt  # log généré automatiquement
└── README.md
```

---

## Concepts utilisés

- `requests` — appels HTTP vers une API REST
- `smtplib` + `MIMEMultipart` — envoi d'email via SMTP SSL
- `os.environ` — gestion sécurisée des credentials
- `with open()` — écriture du fichier log
- `json` — parsing de la réponse API

---

## Auteur

Miche Achkar — B2 CS — EFREI 2025-2026
