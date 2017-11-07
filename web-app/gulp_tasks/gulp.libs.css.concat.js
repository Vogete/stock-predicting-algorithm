// Import gulp concat
var concat = require('gulp-concat');

// Import config
var config = require('./gulp.config.js');

module.exports = function(gulp){

	gulp.task('libs.css.concat', function() {
		return gulp
			.src(config.libs.css)
			.pipe(concat('libs.css'))
			.pipe(gulp.dest(config.dist.css));
	});
};
