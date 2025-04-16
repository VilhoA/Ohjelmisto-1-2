'use strict';
const names = ['John', 'Paul', 'Jones'];

for (let i = 0; i < names.length; i++){
  let text = names[i]
  const li_element = document.createElement("li")
  li_element.innerText = text
  document.getElementById("target").appendChild(li_element)
}