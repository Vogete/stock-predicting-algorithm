var fs = require('fs');
var json2csv = require('json2csv');


Date.prototype.yyyymmdd = function () {
    var mm = this.getMonth() + 1; // getMonth() is zero-based
    var dd = this.getDate();

    return [this.getFullYear(),
        (mm > 9 ? '' : '0') + mm,
        (dd > 9 ? '' : '0') + dd
    ].join('');
};


module.exports.dateConverter = function (date) {
    return date.yyyymmdd();
};

module.exports.subtractDay = function (date, numberOfDays = 1) {
    var subtractedDay = new Date(date.getFullYear(), date.getMonth(), date.getDate() - numberOfDays );
    return subtractedDay;
};

module.exports.addDay = function (date, numberOfDays = 1) {
    var subtractedDay = new Date(date.getFullYear(), date.getMonth(), date.getDate() + numberOfDays );
    return subtractedDay;
};

module.exports.readFromJsonFile = function (JSON_Path, encoding = "UTF8") {
    var data = fs.readFileSync(JSON_Path, encoding);
    var jsonData = JSON.parse(data);
    return jsonData;
};

module.exports.writeToCSVFile = function (CSV_Path, data) {
    fs.writeFileSync(CSV_Path, data);
};

module.exports.convertToCSV = function (jsonData, columns, hasTitle = true) {
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
