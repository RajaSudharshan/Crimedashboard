const dataTable = new simpleDatatables.DataTable("#datatable",{
    searchable: true,
    fixedHeight: true,
    data:{
        headings:["Head1","Head2","Head3"],
    }
})
dataTable.rows.add([
    [data = [
        ["value1, value2, value3"],
        ["value4, value5, value6"],
        ["value7, value8, value9"]
    ]
    
    ]
])