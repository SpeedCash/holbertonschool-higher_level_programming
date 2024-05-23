// Sélection de l'élément avec l'ID 'toggle_header'
const toggleHeader = document.querySelector('#toggle_header');

// Ajout d'un écouteur d'événement pour le clic
toggleHeader.addEventListener('click', () => {
  // Sélection de l'élément <header>
  const header = document.querySelector('header');
  
  // Vérification de la classe actuelle et bascule entre 'red' et 'green'
  if (header.classList.contains('red')) {
    header.classList.replace('red', 'green');
  } else {
    header.classList.replace('green', 'red');
  }
});
