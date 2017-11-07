var gulp = require('gulp-help')(require('gulp'));
// var runSequence = require('gulp-run-sequence');
var runSequence = require('run-sequence');
var config = require('./gulp_tasks/gulp.config.js');

// Concat js
require('./gulp_tasks/gulp.libs.js.concat')(gulp);

// Client TS to JS
require('./gulp_tasks/gulp.browserify')(gulp);

// Concat css
require('./gulp_tasks/gulp.libs.css.concat')(gulp);


// Compile and concat sass
require('./gulp_tasks/gulp.sass')(gulp);

// Compile Server TS
require('./gulp_tasks/gulp.ts')(gulp);

// Copy static
require('./gulp_tasks/gulp.copy_index')(gulp);
require('./gulp_tasks/gulp.copy_assets')(gulp);

// Clear dist folder
require('./gulp_tasks/gulp.clear')(gulp);

// Build dist
gulp.task('build', "Build solution", function(){
	runSequence('clear', 'copy_index', 'copy_assets', 'libs.css.concat', 'sass', 'libs.js.concat', 'browserify', 'ts');
});


gulp.task('watch', 'Builds the solution, then starts watching the files', function () {
    runSequence('build', 'watch-files');
});

gulp.task('watch-files', 'Watch files for change to execute tasks', function(){
    gulp.watch(config.src.copy_index, ['copy_index']);
    gulp.watch(config.src.copy_assets, ['copy_assets']);
    gulp.watch(config.src.sass, ['sass']);
    gulp.watch(config.libs.js, ['libs.js.concat']);
    gulp.watch(config.src.clientTS, ['browserify']);
    gulp.watch(config.src.serverTS, ['ts']);
});
