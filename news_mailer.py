import os
import smtplib
import requests
from datetime import date
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

API_KEY = os.environ.get("NEWS_API_KEY", "")
EMAIL_EXPEDITEUR = os.environ.get("EMAIL_FROM", "")
EMAIL_MOT_DE_PASSE = os.environ.get("EMAIL_PASS", "")
EMAIL_DESTINATAIRE = os.environ.get("EMAIL_TO", "")

SUJET = "cybersecurity"
NB_ARTICLES = 5

def recuperer_news(sujet, nb):
    url = "https://newsapi.org/v2/everything"
    parametres = {
        "q": sujet,
        "language": "en",
        "sortBy": "publishedAt",
        "pageSize": nb,
        "apiKey": API_KEY,
    }
    reponse = requests.get(url, params=parametres)
    donnees = reponse.json()
    return donnees.get("articles", [])


def formater_corps(articles):
    today = date.today().strftime("%d/%m/%Y")
    lignes = [
        f"Cybersecurity News — {today}",
        "=" * 50,
    ]
    for i, article in enumerate(articles, 1):
        lignes.append(f"\n{i}. {article['title']}")
        lignes.append(f"   Source  : {article['source']['name']}")
        lignes.append(f"   Publie  : {article['publishedAt'][:10]}")
        lignes.append(f"   Lien    : {article['url']}")
    return "\n".join(lignes)


def envoyer_email(sujet, corps):
    msg = MIMEMultipart()
    msg["From"] = EMAIL_EXPEDITEUR
    msg["To"] = EMAIL_DESTINATAIRE
    msg["Subject"] = f"[News] Cybersecurity — {date.today()}"
    msg.attach(MIMEText(corps, "plain", "utf-8"))

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as serveur:
        serveur.login(EMAIL_EXPEDITEUR, EMAIL_MOT_DE_PASSE)
        serveur.send_message(msg)


def sauvegarder_log(articles):
    nom = f"news_{date.today()}.txt"
    with open(nom, "w", encoding="utf-8") as f:
        for article in articles:
            f.write(f"{article['title']}\n{article['url']}\n\n")
    return nom


if __name__ == "__main__":
    print(f"Recuperation des news : {SUJET}...")

    articles = recuperer_news(SUJET, NB_ARTICLES)

    if not articles:
        print("Aucun article recupere. Verifie ta cle API.")
    else:
        corps = formater_corps(articles)
        print(corps)
        print("\nEnvoi de l'email...")
        envoyer_email(SUJET, corps)
        fichier = sauvegarder_log(articles)
        print(f"Email envoye a {EMAIL_DESTINATAIRE}")
        print(f"Log sauvegarde : {fichier}")