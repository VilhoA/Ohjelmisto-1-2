'use strict'

let useri = prompt("Give a full number")
const num = Number(useri)
let message

function isprime(num){
  if (num < 2) return false

    for (let i = 2; i < num; i++){
      if (num % i === 0){
        return false
      }
    }
  return true
}



const bol = isprime(num)
console.log(bol)

if(bol){
  document.getElementById("print").innerText = "The given number is a prime number"
}

else{
  document.getElementById("print").innerText = "The given number is not a prime number"
}