document
.getElementById("load")
.addEventListener("click", async () => {

    const response = await fetch(
        "http://127.0.0.1:8000/api/datasets?page=1"
    );

    const data = await response.json();

    const container = document.getElementById("datasets");

    container.innerHTML = "";

    data.result.rows.forEach(dataset => {

        const div = document.createElement("div");

        div.innerHTML = `
            <h3>${dataset.title}</h3>
            <p>ID : ${dataset.id}</p>
            <p>Repository : ${dataset.repositoryid}</p>
            <hr>
        `;

        container.appendChild(div);

    });

});