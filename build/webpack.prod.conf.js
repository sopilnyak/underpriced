/* Production config */

var baseWebpackConfig = require('./webpack.base.conf.js');
var merge = require('webpack-merge');
var BabelMinifyWebpackPlugin = require('babel-minify-webpack-plugin');
var webpack = require('webpack');

module.exports = merge(baseWebpackConfig, {
    plugins: [
        new BabelMinifyWebpackPlugin(),
        new webpack.DefinePlugin({
            'process.env': {
                NODE_ENV: '"production"'
          }
        })
    ]
});
