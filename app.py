import streamlit as st
import psycopg2
from psycopg2 import sql
import os
from dotenv import load_dotenv


load_dotenv(".env")

# Configurer les informations de connexion PostgreSQL
DB_HOST = os.getenv("DB_HOST")
DATABASE = os.getenv("DATABASE")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")

# Fonction pour se connecter à PostgreSQL
def connect_to_db():
    conn = psycopg2.connect(
        host=DB_HOST,
        database=DATABASE,
        user=DB_USER,
        password=DB_PASSWORD
    )
    return conn

# Fonction pour insérer des données dans la table PostgreSQL
def insert_user_data(idcommune, codepostal, commune):
    conn = connect_to_db()
    cur = conn.cursor()
    insert_query = sql.SQL(
        """INSERT INTO  "Test"."Streamlitdatabase" (idcommune, codepostal, commune) VALUES (%s, %s, %s)"""
    )
    cur.execute(insert_query, (idcommune, codepostal, commune))
    conn.commit()
    cur.close()
    conn.close()

# Titre de l'application
st.title("Application de saisie de données vers PostgreSQL")

# Formulaire de saisie
st.subheader("Veuillez saisir les informations de l'utilisateur")

id = st.number_input("id")
codepostal = st.number_input("codepostal")
commune = st.text_input("commune")

# Bouton d'envoi
if st.button("Envoyer"):
    if  id and codepostal and commune:
        # Appel de la fonction pour insérer les données
        insert_user_data(id, codepostal, commune)
        st.success(f"Données de {commune} ont été ajoutées avec succès dans la base de données.")
    else:
        st.error("Veuillez remplir tous les champs.")
