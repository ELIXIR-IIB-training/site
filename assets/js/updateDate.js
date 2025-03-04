// Funzione per aggiornare la data di ultimo aggiornamento
function updateLastUpdate() {
  // Ottieni la data corrente
  const now = new Date();
  const formattedDate = now.toLocaleDateString('it-IT');

  // Aggiorna il contenuto dell'elemento con l'ID "lastUpdate"
  document.getElementById('lastUpdate').textContent = formattedDate;
}

// Esegui la funzione quando il documento è caricato
document.addEventListener('DOMContentLoaded', updateLastUpdate);
