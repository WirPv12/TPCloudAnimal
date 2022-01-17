
let dropdownMenu = document.getElementsByClassName('option')[0];

fetch("./static/js/config.json")
.then(response => {
    return response.json();
})
.then(jsondata => {
    possibleAnimals = jsondata.possibleAnimals;
    favoriteAnimal = jsondata.favoriteAnimal;
});