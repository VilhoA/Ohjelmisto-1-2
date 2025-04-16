



function add_list(text) {
  const li_element = document.createElement("li")
  li_element.innerText = text
  document.getElementById("target").appendChild(li_element)
  return(li_element)
}

add_list("First item")
let second = add_list("Second item")
add_list("Third item")

second.classList.add("my-item")

