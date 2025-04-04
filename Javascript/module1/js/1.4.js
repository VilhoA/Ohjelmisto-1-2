'use strict'

const name = prompt('Tell me your name and be given your class')
const random = Math.floor(Math.random()*4)

if (random === 1){
  document.querySelector('#result').innerHTML = name + ', you are Gryffindor!'
}

if (random === 2){
  document.querySelector('#result').innerHTML = name + ', you are Slutherin!'
}

if (random === 3){
  document.querySelector('#result').innerHTML = name + ', you are Hufflepuff!'
}

if (random === 4){
  document.querySelector('#result').innerHTML = name + ', you are Ravenclaw!'
}