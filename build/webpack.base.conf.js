/* WARNING: we have only dev version of config files.
For production there must be another webpack config with minifiers, etc. */

var path = require('path');
var BundleTracker = require('webpack-bundle-tracker');

function resolve(dir) {
    return path.join(__dirname, '..', dir)
}

module.exports = {
    entry: {
        index: ['babel-polyfill', './static/index.js'],
    },
    output: {
        filename: "[name].js",
        path: resolve('static/dist'),
    },
    module: {
        rules: [
            {
                test: /\.vue$/,
                loader: 'vue-loader'
            },
            {
                test: /\.js$/,
                loader: 'babel-loader', // used for browser support
                exclude: /node_modules/
            },
            {
                test: /\.(png|jpe?g|gif)(\?.*)?$/,
                loader: 'file-loader',
                options: {
                    name: '[name].[ext]?[hash:7]' // returns file's public url
                }
            }
        ]
    },
    plugins: [
        new BundleTracker({filename: './webpack-stats.json'}),
    ],
    resolve: {
        alias: {
            'vue$': 'vue/dist/vue.esm.js',
            '@': resolve('static'),
        }
    },
    performance: {
        hints: false
    }
};
