// Import gulp typescript
var ts = require('gulp-typescript');
var concat = require('gulp-concat');
var tsProject = ts.createProject("./tsconfig.json");
var config = require('./gulp.config.js');

module.exports = function(gulp){

	// gulp.task('ts', function() {
	// 	return tsProject.src()
    //         .pipe(tsProject())
    //         .pipe(concat('server.js'))
    //         .pipe(gulp.dest(config.dist.root));
    // });

    gulp.task('ts', () => {
        const tsResult = tsProject.src()
        .pipe(tsProject());
        return tsResult.js.pipe(gulp.dest(config.dist.root));
    });

};
