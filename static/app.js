"use strict";
const $CupcakeList = $('#cupcakes');
const $FlavorInput = $('#flavor');
const $SizeInput = $('#size');
const $RatingInput = $('#rating');
const $ImageInput = $('#image-url');
const $SubmitBtn = $('#submit-btn');

const API_ENDPOINT = 'http://127.0.0.1:5000/api/cupcakes';




/**
 * Handles the creation of a new cupcake via cupcake form
 * Post request to /api/cupcakes
 * @param {*} evt
 */
async function submitNewCupcake(evt) {
  evt.preventDefault();

  let response = await axios.post(API_ENDPOINT,
    {
      flavor: $FlavorInput.val(),
      size: $SizeInput.val(),
      rating: $RatingInput.val(),
      image_url: $ImageInput.val(),
    });

  appendCupcake(response.data.cupcake);
}

$SubmitBtn.on("click", submitNewCupcake);

/**
 * appends html representing a cupcake POJO to the cupcake list
 * @param {*} cupcake
 */
function appendCupcake(cupcake) {
  $CupcakeList.append(
    $('<div>').html(
            `<img src = '${cupcake.image_url}' style="height:100px; width:auto"/>
            <ul class="d-inline-block">
              <li>Flavor:${cupcake.flavor}</li>
              <li>Size:${cupcake.size}</li>
              <li>Rating:${cupcake.rating}</li>
            </ul>`
    )
  )
}

