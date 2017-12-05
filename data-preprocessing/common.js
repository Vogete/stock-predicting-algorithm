var fs = require('fs');
var json2csv = require('json2csv');
var csv2json = require('csvtojson');

Date.prototype.yyyymmdd = function () {
    var mm = this.getMonth() + 1; // getMonth() is zero-based
    var dd = this.getDate();

    return [this.getFullYear(),
        (mm > 9 ? '' : '0') + mm,
        (dd > 9 ? '' : '0') + dd
    ].join('');
};


module.exports.dateConverter = function dateConverter(date) {
    return date.yyyymmdd();
};

module.exports.dateToEpoch = function dateToEpoch(dateString) {
    // 2017-01-01T17:39:17+0000
    var date = Date.parse(dateString);
    return date;
};

module.exports.subtractDay = function subtractDay(date, numberOfDays = 1) {
    var subtractedDay = new Date(date.getFullYear(), date.getMonth(), date.getDate() - numberOfDays);
    return subtractedDay;
};

module.exports.addDay = function addDay(date, numberOfDays = 1) {
    var subtractedDay = new Date(date.getFullYear(), date.getMonth(), date.getDate() + numberOfDays);
    return subtractedDay;
};

module.exports.readFromJsonFile = function readFromJsonFile(JSON_Path, encoding = "UTF8") {
    var data = fs.readFileSync(JSON_Path, encoding);
    var jsonData = JSON.parse(data);
    return jsonData;
};

module.exports.writeToCSVFile = function writeToCSVFile(CSV_Path, data) {
    fs.writeFileSync(CSV_Path, data);
};

module.exports.readFromFile = function readFromFile(File_Path, encoding = "UTF8") {
    var data = fs.readFileSync(File_Path, encoding);
    return data;
};

module.exports.convertToCSV = function convertToCSV(jsonData, columns, hasTitle = true) {
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
};

module.exports.readFromCSVFile = function readFromCSVFile(CSV_Path, options = {}) {
    // var jsonData = [];
    // jsonData = csv2json.toObject(csv, options);
    // return jsonData;

    var promise = new Promise(function (resolve, reject) {

        csv2json(options).fromFile(CSV_Path, function (err, result) {
            // if an error has occured then handle it
            if(err){
                console.log("An Error Has Occured");
                console.log(err);
            }
            resolve(result);
        });

    });

    return promise;

};

