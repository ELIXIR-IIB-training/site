// Function to update the date
function updateLastUpdate() {
  // Get the current date
  const now = new Date();
  const formattedDate = now.toLocaleDateString('it-IT');

  // Update the content of the element with the ID "lastUpdate"
  document.getElementById('lastUpdate').textContent = formattedDate;
}

// Execute the function when the document is loaded
document.addEventListener('DOMContentLoaded', updateLastUpdate);
