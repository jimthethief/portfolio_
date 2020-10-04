const { merge } = require('webpack-merge');
const common = require('./webpack.common.js');
const BrotliPlugin = require('brotli-webpack-plugin');
const MiniCssExtractPlugin = require('mini-css-extract-plugin');

module.exports = merge(common, {
   mode: 'production',
   devtool: '',
   plugins: [
		new BrotliPlugin({
			asset: '[path].br[query]',
			test: /\.(js|css|html|svg)$/,
			threshold: 10240,
			minRatio: 0.8
		})
   ],
});