document
.getElementById("load")
.addEventListener("click", async () => {

    const status = document.getElementById("datasetStatus");

    status.textContent = "Loading datasets...";

    try{

        const response = await fetch(
            "http://127.0.0.1:8000/api/datasets?page=1"
        );

        const data = await response.json();

        const container = document.getElementById("datasets");

        container.innerHTML = "";

        data.result.rows.forEach(dataset => {

            const div = document.createElement("div");

            div.className = "dataset";

            div.innerHTML = `
                <h3>${dataset.title}</h3>

                <p><strong>ID:</strong> ${dataset.id}</p>

                <p><strong>Repository:</strong> ${dataset.repositoryid}</p>
            `;

            container.appendChild(div);

        });

        status.textContent =
            "✔ " + data.result.rows.length + " datasets loaded.";

    }

    catch(error){

        status.textContent = "✖ Failed to load datasets.";

        console.error(error);

    }

});