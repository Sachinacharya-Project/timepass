# IMPORT HERE
import os
from colorama import init, Fore
init(autoreset=True)
# START WORKING HERE
askPermission = input("Wanna Create Project?(Y/N): ").lower()
if askPermission == 'y':
    project = str(input("Enter Directory Name: "))
    os.system(f'mkdir "{project}"')
else:
    project = "."
serverString = """\
//Server generated
const express = require('express');
const bodyParser = require('body-parser');
const fs = require('fs');

// Routers Here
const index = require('./routers/index')

const app = express();

app.use(bodyParser.urlencoded({ extended: false }));
app.use(bodyParser.json());
app.set('view engine', 'ejs')
app.use(express.static(`${__dirname}/statics`));

app.use('/', index)

const IP = process.env.IP || 'localhost'
const Port = process.env.PORT || 3000;

app.listen(Port, (err) => {
    if (err) {
       console.log(err)
   } else {
       console.log(`Server is Listening at http://${IP}:${Port}`);
    }
});
"""

filename = f"{project}\\server.js"
file = open(filename, 'w')
file.write(serverString)
file.close()

os.system(f'cd "{project}"&&npm init')
permissionPartTwo = str(input("Wanna Install Basic Modules: (Y/N(def.))")).lower()

if permissionPartTwo == 'y':
    print('Installing Basics Modules\n#1. express\n#2. body-parser\n#3. ejs')
    os.system(f'cd "{project}"&&npm install express body-parser ejs')
else:
    pass
askmeplease = str(input("DO you wanna install Additional Modules (N: No, if yes separate modules name with ;\n)"))
if askmeplease.lower() == 'n':
    pass
else:
    askmeplease = askmeplease.replace(';', ' ')
    os.system(f'cd "{project}"&&npm install {askmeplease}')
print(Fore.MAGENTA+'Your main ejs files goes to "VIEWS" folder,\n\nFiles like CSS, JS, IMAGES goes to "STATICS" folder,\n\nRouters to "ROUTERS" folder\n\n')
os.system(f'cd "{project}"&&mkdir views&&mkdir statics&&mkdir routers')
os.system(f'mkdir "{project}"\\statics\\css')
os.system(f'mkdir "{project}"\\statics\\js')

serverString = """\
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="shortcut icon" href="favicon.ico" type="image/x-icon">
    <link href="https://fonts.googleapis.com/icon?family=Material+Icons" rel="stylesheet">
    <script src="https://kit.fontawesome.com/612f542d54.js" crossorigin="anonymous"></script>
    <link rel="preconnect" href="https://fonts.gstatic.com">
    <link href="https://fonts.googleapis.com/css2?family=Allan&family=Anton&family=Bebas+Neue&family=Courgette&family=Imbue&family=Kaushan+Script&family=Lobster&family=Nova+Square&family=Oswald:wght@300;400&family=PT+Sans+Narrow&family=Pathway+Gothic+One&family=Poppins&family=Potta+One&family=Righteous&family=Roboto:wght@300;400&family=Squada+One&family=Teko:wght@300;400&family=Trade+Winds&family=Yanone+Kaffeesatz:wght@400;500&family=Yellowtail&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="/css/style.css">
    <title>Document</title>
</head>
<body>

    <h1 style="color: green;font-family: sans-serif;"><center>Template Has been Created</center></h1>
    
    <script src="https://code.jquery.com/jquery-3.5.1.min.js" integrity="sha256-9/aliU8dGd2tb6OSsuzixeV4y/faTqgFtohetphbbj0=" crossorigin="anonymous"></script>
    <script src="/js/app.js"></script>
</body>
</html>
"""
indexHtmlFilePath = f"{project}\\views\\index.ejs"
indexHtml = open(indexHtmlFilePath, 'w')
indexHtml.write(serverString)
indexHtml.close()

indexJSFilePath = f"{project}\\statics\\js\\app.js"
indexJS = open(indexJSFilePath, 'w')
indexJS.write('// Here lies your Main JS codes')
indexJS.close()

serverString="""\
$allan: 'Allan', cursive;
$anton: 'Anton', sans-serif;
$bebas: 'Bebas Neue', cursive;
$courgette: 'Courgette', cursive;
$inbue: 'Imbue', serif;
$kaushan: 'Kaushan Script', cursive;
$lobster: 'Lobster', cursive;
$nove: 'Nova Square', cursive;
$oswald: 'Oswald', sans-serif;
$pathway: 'Pathway Gothic One', sans-serif;
$poppins: 'Poppins', sans-serif;
$potta: 'Potta One', cursive;
$pt: 'PT Sans Narrow', sans-serif;
$righteous: 'Righteous', cursive;
$roboto: 'Roboto', sans-serif;
$squada: 'Squada One', cursive;
$teko: 'Teko', sans-serif;
$trade: 'Trade Winds', cursive;
$yenone: 'Yanone Kaffeesatz', sans-serif;
$yellow: 'Yellowtail', cursive;

*{
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

body{
    width: 100%;
    min-height: 100vh;
}

h1{
    color: green;
    font-family: sans-serif;
    text-align: center;
}
/* GENERATED BY SACHIN */
"""

indexCSSFilePath = f"{project}\\statics\\css\\style.scss"
indexCSS = open(indexCSSFilePath, 'w')
indexCSS.write(serverString)
indexCSS.close()

serverString="""\
{
    "version": 3,
    "mappings": "AAqBA,AAAA,CAAC,CAAA;EACG,MAAM,EAAE,CAAC;EACT,OAAO,EAAE,CAAC;EACV,UAAU,EAAE,UAAU;CACzB;;AAED,AAAA,IAAI,CAAA;EACA,KAAK,EAAE,IAAI;EACX,UAAU,EAAE,KAAK;CAMpB;;AARD,AAGI,IAHA,CAGA,EAAE,CAAA;EACE,KAAK,EAAE,KAAK;EACZ,WAAW,EAAE,UAAU;EACvB,UAAU,EAAE,MAAM;CACrB;;AAGL,yBAAyB",
    "sources": [
        "style.scss"
    ],
    "names": [],
    "file": "style.css"
}
"""

indexCSSMAPFilePath = f"{project}\\statics\\css\\style.css.map"
indexCSSMAP = open(indexCSSMAPFilePath, 'w')
indexCSSMAP.write(serverString)
indexCSSMAP.close()

serverString="""\
* {
  margin: 0;
  padding: 0;
  -webkit-box-sizing: border-box;
          box-sizing: border-box;
}

body {
  width: 100%;
  min-height: 100vh;
}

body h1 {
  color: green;
  font-family: sans-serif;
  text-align: center;
}

/* GENERATED BY SACHIN */
/*# sourceMappingURL=style.css.map */
"""

indexCSSNorFilePath = f"{project}\\statics\\css\\style.css"
indexCSSNor = open(indexCSSNorFilePath, 'w')
indexCSSNor.write(serverString)
indexCSSNor.close()

serverString = """\
const express = require('express');
const router = express.Router()

router.get('/', (req, res)=>{
    res.render('index')
})

module.exports = router
"""

indexRouterFilePath = f"{project}\\routers\\index.js"
indexRouter = open(indexRouterFilePath, 'w')
indexRouter.write(serverString)
indexRouter.close()

print('BOILER PLATE GENERATED\n\nPress ENTER to continue\n\n'+ Fore.RED +'NOTE: SCREEN WILL BE CLEARED')


