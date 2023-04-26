const md5 = require('md5-node')
const CryptoJS = require('crypto-js')

function fn(e){
    const hash = md5(e);
    return Buffer.from(hash, 'hex');
}

function c(t, e, n) {
    if (t = t.toLowerCase(),
    o[t])
        return i.createDecipheriv(t, e, n);
    if (s[t])
        return new r({
            key: e,
            iv: n,
            mode: t,
            decrypt: !0
        });
    throw new TypeError("invalid suite type")
}

t1 = '_jsUyA02rwkOJ4enKX7c4dhd7CjvGkcKfbRx0BjNGW8OgIRH1rgaj5tPhWMKWNW-K3LvAiHRuWyRQBuU0gsuSO1UMxOFFDAcuWENI9r5kAC_7uF2IYJB6c0tWv4hIs7AuFlzgAB95o1_JgWV7d1N9DJdD-laTCZ5Hl57jDPB_l4='
o1 = "ydsecret://query/key/B*RGygVywfNBwpmBaZg*WT7SIOUP2T0C9WHMZN39j^DAdaZhAnxvGcCY6VYFwnHl"
n1 = "ydsecret://query/iv/C@lZe2YzHtZ2CYgaXKSVfsb7Y4QWHjITPPZ0nQp87fBeJ!Iv6v^6fvi2WN@bYpJ4"

console.log(fn(o1).inspect())
