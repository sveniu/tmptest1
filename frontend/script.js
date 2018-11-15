const elExecute = document.getElementById("execute")
const elOutput = document.getElementById("output")

elExecute.addEventListener("click", e => {
    e.preventDefault()

    const target_url = document.getElementById("target_url").value
    fetch(target_url)
        .then(response => response.json())
        .then(json => elOutput.innerText = JSON.stringify(json, null, 4))
}, false)