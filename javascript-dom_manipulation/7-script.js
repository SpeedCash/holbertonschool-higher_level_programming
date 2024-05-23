// URL de l'API pour obtenir la liste des films Star Wars
const apiUrl = 'https://swapi-api.hbtn.io/api/films/?format=json';

// Utilisation de l'API Fetch pour récupérer les données
fetch(apiUrl)
  .then(response => response.json())
  .then(data => {
    // Sélection de l'élément avec l'ID 'list_movies'
    const listMovies = document.querySelector('#list_movies');

    // Parcours de la liste des films et ajout de chaque titre à la liste <ul>
    data.results.forEach(film => {
      const listItem = document.createElement('li');
      listItem.textContent = film.title;
      listMovies.appendChild(listItem);
    });
  })
  .catch(error => {
    console.error('Error fetching data:', error);
  });
