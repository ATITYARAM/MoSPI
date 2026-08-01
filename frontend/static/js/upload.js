let csvData = [];
let headers = [];

document
    .getElementById("csvFile")
    .addEventListener("change", readCSV);

function readCSV(event){

    const file = event.target.files[0];

    if(!file){
        return;
    }

    document.getElementById("fileName").textContent =
        file.name;

    document.getElementById("fileStatus").textContent =
        "Reading CSV...";

    Papa.parse(file,{

        header:true,

        skipEmptyLines:true,

        complete:function(result){

            csvData = result.data;

            headers = result.meta.fields || [];

            document.getElementById("fileStatus").textContent =
                "✔ CSV Loaded";

            document.getElementById("rowCount").textContent =
                csvData.length;

            document.getElementById("columnCount").textContent =
                headers.length;

            showColumns();

        },

        error:function(){

            document.getElementById("fileStatus").textContent =
                "✖ Invalid CSV";

        }

    });

}

function showColumns(){

    const container =
        document.getElementById("columns");

    container.innerHTML = "";

    headers.forEach(header=>{

        const button =
            document.createElement("button");

        button.textContent = header;

        button.onclick = function(){

            selectColumn(header);

        };

        container.appendChild(button);

    });

}

function selectColumn(column){

    document.getElementById("selectedColumn").textContent = column;

    const values = csvData
        .map(row => row[column])
        .filter(value => value !== "");

    const uniqueValues = [...new Set(values)];

    document.getElementById("json").textContent =
        JSON.stringify(
            {
                column: column,
                totalUniqueValues: uniqueValues.length,
                values: uniqueValues
            },
            null,
            2
        );

}