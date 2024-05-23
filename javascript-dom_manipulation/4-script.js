// Sélection de l'élément avec l'ID 'add_item'
const addItem = document.querySelector('#add_item');

// Ajout d'un écouteur d'événement pour le clic
addItem.addEventListener('click', () => {
  // Création d'un nouvel élément <li>
  const newItem = document.createElement('li');
  newItem.textContent = 'Item';

  // Sélection de l'élément <ul> avec la classe 'my_list'
  const myList = document.querySelector('.my_list');

  // Ajout du nouvel élément <li> à la liste
  myList.appendChild(newItem);
});
