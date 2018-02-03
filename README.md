# tozti-discussion
*A tozti extension providing discussion threads.*

## Installing the extension.

To use the extension in your tozti installation, either:
- Download one of the releases, and unzip it into your `extensions/` folder.
- Clone this repository, run `npm install && npm run release`, and simlink it into your `extensions/` folder.

## Contributing.

Once the dependencies are installed using `npm install`, you can use the following `npm` scripts.

- `npm run build` will compile all the .js, .vue, .sass files and all the assets of your extension for development.
- `npm run watch` will do the same as `npm run build`, but will automatically re-trigger when one of the files changes.
- `npm run release` will compile all the files of your extension for production use. 
   In particular, this means that all the files will be minified, and that source maps will be deleted.
- `npm run package` will run `npm run release`, and then package all of the compiled files into a .tar.gz archive.