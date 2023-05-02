"use strict";

const API_ENDPOINT = '/api/cupcakes';

const $searchBar = $('#search-bar');

const $cupcakeList = $('#cupcakes');
const $flavorInput = $('#flavor');
const $sizeInput = $('#size');
const $ratingInput = $('#rating');
const $imageInput = $('#image-url');
const $submitBtn = $('#submit-btn');


displayAllCupcakes();
$submitBtn.on("click", submitNewCupcake);
$searchBar.on("input", displayAllCupcakes);

/**
 * On load: Adds all the cupcakes to the list in the DOM using a GET request to /cupcakes
 * On search: Adds filtering cupcakes to the list in the DOM using a GET request to /cupcakes?q="searched"
 */
async function displayAllCupcakes() {

  $cupcakeList.html("");

  let userSearch = $searchBar.val();
  const response = await axios.get(API_ENDPOINT, { params: { q: userSearch } });

  for (const cupcake of response.data.cupcakes) {
    appendCupcake(cupcake);
  }
}


/**
 * Handles the creation of a new cupcake via cupcake form
 * Post request to /api/cupcakes
 * @param {*} evt
 */
async function submitNewCupcake(evt) {
  evt.preventDefault();

  const response = await axios.post(API_ENDPOINT,
    {
      flavor: $flavorInput.val(),
      size: $sizeInput.val(),
      rating: $ratingInput.val(),
      image_url: $imageInput.val(),
    });

  appendCupcake(response.data.cupcake);
}



/**
 * appends html representing a cupcake POJO to the cupcake list
 * @param {object} cupcake - a POJO containing the cupcake data
 */
function appendCupcake(cupcake) {
  $cupcakeList.append(
    $('<div>').html(
      `<img src = '${cupcake.image_url}' style="height:100px; width:auto"/>
            <ul class="d-inline-block">
              <li>Flavor: ${cupcake.flavor}</li>
              <li>Size: ${cupcake.size}</li>
              <li>Rating: ${cupcake.rating}</li>
            </ul>`
    )
  );
}

