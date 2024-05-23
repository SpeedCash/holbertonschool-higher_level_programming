// URL de l'API pour obtenir le nom du personnage
const apiUrl = 'https://swapi-api.hbtn.io/api/people/5/?format=json';

// Utilisation de l'API Fetch pour récupérer les données
fetch(apiUrl)
  .then(response => response.json())
  .then(data => {
    // Sélection de l'élément avec l'ID 'character'
    const characterElement = document.querySelector('#character');

    // Mise à jour du texte de l'élément avec le nom du personnage
    characterElement.textContent = data.name;
  })
  .catch(error => {
    console.error('Error fetching data:', error);
  });
