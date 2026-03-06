---
# --- INFO BASE ---
title: "Titolo Completo del Corso o Meeting"
schema_type: "Course"          # Usa "Course" per i corsi o "Event" per i meeting/workshop
type: meetings_workshops       # Lascialo per la compatibilità con le tue cartelle Jekyll
short_description: "Una frase chiara e concisa che riassuma l'evento (max 200 caratteri)."

# --- DATE (Formato AAAA-MM-GG) ---
startDate: "2026-05-20"
endDate: "2026-05-20"          # Se dura un giorno solo, ripeti la startDate

# --- LOGISTICA ---
courseMode: "onsite"           # "onsite" oppure "online"
venue: "Nome Edificio, Via e Numero Civico" # Se online, puoi cancellare questa riga
addressLocality: "Città"       # Se online, puoi cancellare questa riga
postalCode: "00185"            # Solo il CAP numerico | Se online, puoi cancellare questa riga
addressCountry: "Italy"

# --- ORGANIZZAZIONE ---
organizer:
  - "ELIXIR-IT"                # Lascialo sempre come primo 
  - "Università/Ente Partner"  # Aggiungi qui gli altri co-organizzatori

# --- CONTENUTI SCIENTIFICI (Cerca su edamontology.org/browser) ---
scientific_topic:
  - "Bioinformatics"           # Topic EDAM (Es: Proteomics, Genomics, Machine learning)
  - "Computational biology"

# --- INFO CORSO (Solo se schema_type è "Course") ---
learning_outcomes:                      # Facoltativi
  - "Cosa imparerà l'utente 1"
  - "Cosa imparerà l'utente 2"

target_audience:                        # Facoltativi
  - "PhD Students"
  - "Postdocs"

instructors:
  - "Nome Cognome del Docente"

# --- LINK E LINGUA ---
registration_url: "https://link-al-modulo-di-iscrizione.it" # A cura del creatore della webpage
inLanguage: "en-GB"            # "it-IT" oppure "en-GB"
---


