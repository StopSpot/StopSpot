function downloadCSV(filename, data){
    let a = document.createElement('a');
    console.log(data)
    let pct_err_csv = jsonToCSV(data);
    a.setAttribute('href', 'data:text/plain;charset=utf-8,' + encodeURIComponent(pct_err_csv));
    a.setAttribute('download', filename);
    a.style.display = 'none';
    document.body.appendChild(a);

    a.click();

    document.body.removeChild(a);

}
function jsonToCSV(json_data){
    header = json_data['Header'];

    csv = '';
    for(i = 0; i< header.length; i++){
        csv += header[i];
        if(i < header.length - 1){
        csv += ", "
        }
    }
    csv += '\n';

    keys = Object.keys(json_data);
    for(key in keys){
        if(keys[key] != 'Header'){
        csv += keys[key] + ',' + json_data[keys[key]] + '\n';
        }
    }
    console.log(csv);
    return csv;
}