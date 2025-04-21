'use strict'

let useri
let json_result

document.getElementById("search_button").onclick = function(){
  useri = document.getElementById("user_search").value
  console.log(useri)
  fetch(`https://api.chucknorris.io/jokes/search?query=${useri}`)
    .then(res => res.json())
    //.then(data => console.log(data))
      .then(data => {
        console.log(data)
        json_result = data
        console.log(json_result)
            //for (let i = 0; i < json_result.result.length; i++)
             // console.log(json_result.result[i].value)

            const article = document.getElementById("jokelist")

              json_result.result.forEach(joke => {
                const p_element = document.createElement("p")
                p_element.textContent = joke.value
                article.appendChild(p_element)
              })
  })
}




