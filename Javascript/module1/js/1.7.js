'use strict'

const rounds = Number(prompt('Input the amount of dices thrown'))
let dices = 0

for (let i = 0; i <= rounds; i++){
  const dice = Math.floor(Math.random()*6)
  dices += dice
}

document.querySelector('#print').innerHTML = "The sum of all the dices: " +  dices