'use strict'

const name1 = Number(prompt("Input number #1"))
const name2 = Number(prompt("Input number #2"))
const name3 = Number(prompt("input number #3"))

const sum = (name1+name2+name3)
const average = (name1+name2+name3)/3

document.querySelector('#sum').innerHTML = 'Sum of given numbers: ' + sum
document.querySelector('#average').innerHTML = 'Average of given numbers: ' + average