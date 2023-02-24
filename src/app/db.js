const path = require("path");
const fs = require("fs");

const DATA_PATH = "../data.json";
const getData = async () =>
{
    const a = await fs.readFile( path.join( __dirname, DATA_PATH ), "utf8", ( err, data ) =>
    {
        if ( err )
        {
            console.log( err );
        }
        else
        {
            return data;
        }
    });

    console.log(a)
    return a;
};

const db = {
  getData,
};

module.exports = db;
