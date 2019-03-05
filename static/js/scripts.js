var table = new Tabulator("#data-table", {
    height: "95%", // set height of table (in CSS or here), this enables the Virtual DOM and improves render speed dramatically (can be any valid css height value)
    data:db_data, //assign data to table
    placeholder: 'No data available',
    layout:"fitColumns", //fit columns to width of table (optional)
    initialSort: [{column:"id", dir:"asc"}],
    columns:[ //Define Table Columns
        {title:"ID", field:"id", visible: false},
        {title:"Category", field:"category", headerFilter: "input", editor:"input"},
        {title:"Comment", field:"comment", headerFilter: "input"},
        {title:"Amount", field:"amount", headerFilter: "input"}
    ]
});