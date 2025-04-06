'use strict'

let dogs = []

for (let i = 1; i < 7; i++){
  const dog = prompt('Give a name to dog number ' + i)
  dogs.push(dog)
}

dogs.sort()
dogs.reverse()
let ul = document.getElementById('ul_list')

for (let i = 0; i < dogs.length; i++){
  let le = document.createElement('li')
  le.textContent = dogs[i]
  ul.appendChild(le)
}
