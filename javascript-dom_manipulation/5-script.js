// Sélection de l'élément avec l'ID 'update_header'
const updateHeader = document.querySelector('#update_header');

// Ajout d'un écouteur d'événement pour le clic
updateHeader.addEventListener('click', () => {
  // Sélection de l'élément <header>
  const header = document.querySelector('header');

  // Mise à jour du texte de l'élément <header>
  header.textContent = 'New Header!!!';
});
