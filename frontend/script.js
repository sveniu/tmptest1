const elExecute = document.getElementById("execute")
const elOutput = document.getElementById("output")
const elTargetURL = document.getElementById("target_url")

elTargetURL.value = window.location.href + "api/"

elExecute.addEventListener("click", e => {
    e.preventDefault()

    const target_url = elTargetURL.value
    fetch(target_url)
        .then(response => response.json())
        .then(json => elOutput.innerText = JSON.stringify(json, null, 4))
}, false)
