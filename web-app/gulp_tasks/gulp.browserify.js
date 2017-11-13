var browserify = require('browserify');
var tsify = require('tsify');
var source = require('vinyl-source-stream');
var sourcemaps = require('gulp-sourcemaps');
// brfs
var fs = require('fs');

// Import config
var config = require('./gulp.config.js');

module.exports = function(gulp){
	gulp.task('browserify', function() {

		return browserify(config.src.clientTS, {debug: true})// "debug: true" will enable typscript source maps!! :)
            .add(config.libs.types)
			.plugin(tsify, { noImplicitAny: false })
			.transform('brfs')
			.bundle()
			.on('error', function (error) { console.error(error.toString()); })
			.pipe(source('app.js'))
			.pipe(gulp.dest(config.dist.js));
	});
};

