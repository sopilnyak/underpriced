/* WARNING: we have only dev version of config files.
For production there must be another webpack config with minifiers, etc. */

var baseWebpackConfig = require('./webpack.base.conf');
var merge = require('webpack-merge');
var FriendlyErrorsPlugin = require('friendly-errors-webpack-plugin');

module.exports = merge(baseWebpackConfig, {
    devtool: '#cheap-module-eval-source-map',
    plugins: [
        new FriendlyErrorsPlugin()
    ]
});
