'use strict'

const number = Number(prompt('Input a year'))

if (number % 4 === 0 || (number % 400 === 0 && number % 100 === 0)){

      document.querySelector('#print').innerHTML = number + 'is a leap year';
  } else{
    document.querySelector('#print').innerHTML = number + 'is not a leap year'

}