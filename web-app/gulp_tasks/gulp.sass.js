// Import gulp concat
var sass = require('gulp-sass');
// Import config
var config = require('./gulp.config.js');

module.exports = function(gulp){

	gulp.task('sass', function() {
		return gulp
			.src(config.src.sass)
			.pipe(sass().on('error', sass.logError))
			.pipe(gulp.dest(config.dist.css));
	});
};
