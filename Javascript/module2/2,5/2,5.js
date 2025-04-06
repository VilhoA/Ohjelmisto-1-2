'use strict'

let numlist = []
let useri= Number(prompt('Input a number'))
let bol= numlist.includes(useri)

while (!bol){
  numlist.push(useri)
  useri = Number(prompt('Input a number'))
  bol = numlist.includes(useri)
}

alert('Number already given')

numlist.sort((a, b) => b - a)

for (let i = 0; i < numlist.length; i++){
  console.log(numlist[i])
}