'use strict'

let useri

document.getElementById("search_button").onclick = function(){
  useri = document.getElementById("user_search").value
  console.log(useri)
  fetch(`https://api.tvmaze.com/search/shows?q=${useri}`)
    .then(res => res.json())
    .then(data => console.log(data))
}




