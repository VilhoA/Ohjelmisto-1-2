'use strict'

const pic = document.getElementById('target')
const oldpic = pic.src


const trigger= document.getElementById('trigger')

trigger.addEventListener('mouseover', () => {pic.src = 'img/picB.jpg'})
trigger.addEventListener('mouseout', () => {pic.src = oldpic})

