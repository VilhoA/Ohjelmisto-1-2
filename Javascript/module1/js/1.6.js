'use strict'

const conf = confirm('Should i calculate the square root?')



if (conf) {
  const input = Number(prompt('Give a number'))
  if (input < 0) {
    document.querySelector(
        '#print').innerHTML = 'The square root of a negative number is not defined'
  }
  if (input > 0) {
    const square = Math.sqrt(input)
    document.querySelector('#print').innerHTML = 'The square of ' + input +
        ' is: ' + square
  }
}





if (!conf){
  document.querySelector('#print').innerHTML= 'The square root is not calculated'
}
