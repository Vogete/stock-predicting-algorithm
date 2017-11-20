var common = require('../common.js');


(function main() {
    var articleDirectory = "../../assets/news_articles/nytimes/";

    var beginDate = new Date();
    var endDate = new Date();
    var csvData = [];
    var jsonData = [];


    beginDate.setFullYear(2017, 0, 1);
    endDate.setFullYear(2017, 10, 13);
    var csvOptions = {
        includeHeader: true,
        columns: [
            "pub_date",
            "pub_date_epoch",
            "snippet",
            "headline.main"
        ]
    };

    var currentDay = new Date(beginDate);

    while (currentDay < endDate) {
        var currentFileName = common.dateConverter(currentDay) + "-" + common.dateConverter(common.addDay(currentDay)) + "_nytimes";

        var tempjson = common.readFromJsonFile(articleDirectory + "json-articles/" + currentFileName + ".json");
        for (let i = 0; i < tempjson.length; i++) {

            // convert date string to epoch (second column is the epoch date!)
            tempjson[i][csvOptions.columns[1]] = common.dateToEpoch(tempjson[i][csvOptions.columns[0]]).toString();


            jsonData.push(tempjson[i]);
        }

        currentDay = common.addDay(currentDay);
    }

    csvData = common.convertToCSV(jsonData, csvOptions.columns, csvOptions.includeHeader);
    common.writeToCSVFile(articleDirectory + "nytimes-articles.csv", csvData);


})();
