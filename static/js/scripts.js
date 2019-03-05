var table = new Tabulator("#data-table", {
    height: "95%",
    data:db_data,
    placeholder: 'No data available',
    layout:"fitColumns",
    initialSort: [{column:"id", dir:"asc"}],
    columns:[
        {title:"ID", field:"id", visible: false},
        {title:"Category", field:"category", headerFilter: "input"},
        {title:"Comment", field:"comment", headerFilter: "input"},
        {title:"Amount", field:"amount", headerFilter: "input"}
    ]
});