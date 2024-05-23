// Sélection de l'élément avec l'ID 'red_header'
const redHeader = document.querySelector('#red_header');

// Ajout d'un écouteur d'événement pour le clic
redHeader.addEventListener('click', () => {
  // Ajout de la classe 'red' à l'élément <header>
  document.querySelector('header').classList.add('red');
});
