document.getElementById("execute").addEventListener("click", e => {
    e.preventDefault()
    fetch(document.getElementById("target_url").value)
        .then(response => response.json())
        .then(json => document.getElementById("output").innerText = JSON.stringify(json, null, 4))
}, false)