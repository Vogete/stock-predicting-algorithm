var fs = require('fs');
var json2csv = require('json2csv');
var common = require('./common.js');


function convertToCSVasync(fileJSON, fileCSV, title = false) {
    fs.readFile(fileJSON, 'utf8', function (err, data) {
        if (err) throw err;
        obj = JSON.parse(data);

        var columns = [
            "pub_date",
            "snippet",
            "headline.main"
        ];

        try {
            var csv = json2csv({
                data: obj,
                fields: columns,
                hasCSVColumnTitle: title
            });

            fs.writeFile(fileCSV, csv, function (err) {
                if (err) throw err;
                console.log('file saved');
            });

        } catch (err) {
            // Errors are thrown for bad options, or if the data is empty and no fields are provided.
            // Be sure to provide fields if it is possible that your data array will be empty.
            console.error(err);
        }

    });

}

function convertToCSV(jsonData, hasTitle = false) {
    var columns = [
        "pub_date",
        "snippet",
        "headline.main"
    ];

    try {
        var csv = json2csv({
            data: jsonData,
            fields: columns,
            hasCSVColumnTitle: hasTitle
        });

        return csv;
    } catch (err) {
        console.error(err);
    }

}

function readFromJsonFile(JSON_Path) {
    var data = fs.readFileSync(JSON_Path, 'utf8');
    var jsonData = JSON.parse(data);
    return jsonData;
}


function writeToCSVFile(CSV_Path, data) {

    fs.writeFileSync(CSV_Path, data);

}


(function main() {
    var beginDate = new Date();
    var endDate = new Date();
    beginDate.setFullYear(2017, 0, 1);
    endDate.setFullYear(2017, 10, 12);

    var includeHeader = true;
    var csvData, jsonData;
    var currentDay = new Date(beginDate);

    while (currentDay < endDate) {
        var currentFileName = common.dateConverter(currentDay) + "-" + common.dateConverter(common.addDay(currentDay)) + "_nytimes";

        jsonData += readFromJsonFile("./data/" + currentFileName + ".json");

        currentDay = common.addDay(currentDay);
    }

    // convertToCSVasync("20171110-20171111_nytimes.json", "20171110-20171111_nytimes.csv");
    csvData = convertToCSV(jsonData, includeHeader);

    writeToCSVFile("trainingData.csv", csvData);


})();
