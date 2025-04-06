'use strict'

let numlist = []
let useri = Number(prompt('Give a number to add or end by typing number 0'))

while (useri !== 0){
  numlist.push(useri)
  useri = Number(prompt('Give a number to add or end by typing number 0'))
}

numlist.sort((a, b) => b - a)

for (let i = 0; i < numlist.length; i++){
  console.log(numlist[i])
}

