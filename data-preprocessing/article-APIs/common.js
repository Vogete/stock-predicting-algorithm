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



