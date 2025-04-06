'use strict'

let list = []


for (let i = 0; i < 5; i++) {
  const num = prompt('Give a number: ')
  list += num
}

for (let indx = list.length -1; indx >= 0; indx--) {
  console.log(list[indx])
}
