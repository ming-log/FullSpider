const md5 = require('md5-node')

function hh(e) {
    return md5(`client=${d}&mysticTime=${e}&product=${u}&key=${'fsdsogkndfokasodnaso'}`)
}

const t = new Date().getTime();
let d = "fanyideskweb"
let u = 'webfanyi'
console.log(hh(t))

