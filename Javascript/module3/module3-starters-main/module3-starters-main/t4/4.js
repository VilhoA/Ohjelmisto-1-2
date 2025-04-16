'use strict';
const students = [
  {
    name: 'John',
    id: '2345768',
  },
  {
    name: 'Paul',
    id: '2134657',
  },
  {
    name: 'Jones',
    id: '5423679',
  },
];

const names = ['John', 'Paul', 'Jones'];

for (let i = 0; i < names.length; i++){
  let text = names[i]
  const li_element = document.createElement("option")
  li_element.innerText = text
  li_element.id = text
  document.getElementById("target").appendChild(li_element)
}

for (let i = 0; i < names.length; i++){
 let chosen = document.getElementById(students[i].name)
  chosen.value = students[i].id
}