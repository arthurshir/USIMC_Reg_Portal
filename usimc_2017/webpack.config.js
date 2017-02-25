var path = require("path")
var webpack = require('webpack')
var BundleTracker = require('webpack-bundle-tracker')


module.exports = {
  context: __dirname,
  entry: [
    'webpack-dev-server/client?http://localhost:3000',
    'webpack/hot/only-dev-server',
    './assets/js/index.js'
  ], // entry point of our app. assets/js/index.js should require other js modules and dependencies it needs

  output: {
    path: path.resolve('assets/bundles/'),
    // publicPath: '/static/bundles/',
    // filename: "[name]-[hash].js",
    
      // path: path.resolve('./apps/static/bundles/'),
      filename: '[name]-[hash].js',
      // publicPath: 'http://localhost:8000/static/bundles/', // Tell django to use this URL to load packages and not use STATIC_URL + bundle_name
  },

  plugins: [
    new webpack.HotModuleReplacementPlugin(),
    new BundleTracker({filename: './webpack-stats.json'}),
  ],
  module: {
    loaders: [
      {
        test: /\.jsx?$/,
        loader: 'babel-loader',
        exclude: /node_modules/,
        query: {
            presets: ['react']
        }
      },
      {
        test: /\.scss$/,
        loaders: [ 'style-loader', 'css-loader', 'sass-loader?sourceMap' ]
      },
      { 
        test: /\.svg$/,
        loader: 'svg-loader?pngScale=2'
      },
      {
        test: /\.(jpe?g|png|gif|svg)$/i,
        loader: "file-loader?name=/static/images/[name].[ext]"
      },
    ],
  },

  resolve: {
    modules: ['node_modules', 'bower_components'],
    extensions: ['.js', '.jsx'],
  },
}