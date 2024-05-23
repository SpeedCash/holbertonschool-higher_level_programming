// Sélection de l'élément avec l'id 'red_header'
const redHeader = document.querySelector('#red_header');

// Ajout d'un écouteur d'événement pour le clic
redHeader.addEventListener('click', () => {
  // Mise à jour de la couleur du texte de l'élément <header> en rouge
  document.querySelector('header').style.color = '#FF0000';
});
