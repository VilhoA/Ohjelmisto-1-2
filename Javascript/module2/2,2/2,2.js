'use strict'

const amount = Number(prompt('How many participants?'))
let people = []

for (let i = amount; i > 0; i--){
  const name = prompt('Give name for participant number ' + i)
  people.push(name)
}

people.sort()

let ol = document.getElementById('participants_ol')

for (let i = 0; i < people.length; i++){
  let le= document.createElement('li')
  le.textContent = people[i]
  ol.appendChild(le)
}
console.log(people)