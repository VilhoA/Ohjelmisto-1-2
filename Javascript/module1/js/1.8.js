'use strict'

let start = Number(prompt('Input starting year'))
const stop = Number(prompt('Input ending year'))
let yearlist = []
let leapyear = []

for (let i = start; i <= stop; i++){
  yearlist.push(i)
}

yearlist.forEach((year) =>{
  if (year % 4 === 0 && year % 100 !== 0 || (year % 400 === 0)){
    leapyear.push(year)
  }
});


function addtolist(text) {
  let unordered = document.getElementById("list")
  let html_li = document.createElement("li")
  html_li.appendChild(document.createTextNode(text))
  unordered.appendChild(html_li)
}


leapyear.forEach((year) => {
  addtolist(year)
})

//addtolist("testi")