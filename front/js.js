/*async function puxando_api() {
    const response = await fetch("http://127.0.0.1:8000/api/v1/personagem")
    const data = await response.json()
    return data
}

async function mostar_personagem() {
    const personagens = await puxando_api()
    const container = document.getElementById("transformers-container")

    personagens.array.forEach(personagem => {
        const personagemDiv = document.createElement("")
        personagemDiv.classList.add("personagem")
        personagemDiv.innerHTML = `
            <h2>${personagem.nome}</h2>
            <img src = "${personagem.foto}"></img>
            <p>${personagem.time}</p>
        `
    container.appendChild(personagemDiv)
    });
}
mostar_personagem() */


async function puxar_api() {
    await axios.get("http://127.0.0.1:8000/api/v1/personagem").then((response) =>{
        const personagens = response.data
        const container = document.getElementById("transformers-container")
        personagens.forEach(element =>{
            const personagemDiv = document.createElement("div")
            personagemDiv.classList.add("element")
            personagemDiv.innerHTML = `
            <h2>${element.nome}</h2>
            <img src = "${element.foto}"></img>
            <p>${element.time}</p>
            `
            container.append(personagemDiv)
        })
    })
}
puxar_api()