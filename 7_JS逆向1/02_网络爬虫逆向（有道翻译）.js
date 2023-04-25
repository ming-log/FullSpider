function e(e, n, r) {
    return t.call(this, o(e, n, r)) || this
}

function uu(t) {
    if (!(this instanceof uu))
        return new uu(t);
    e.call(this, t),
    e.call(this, t),
    this.allowHalfOpen = !0,
    t && (!1 === t.readable && (this.readable = !1),
    !1 === t.writable && (this.writable = !1),
    !1 === t.allowHalfOpen && (this.allowHalfOpen = !1,
    this.once("end", f)))
}


function f(t) {
    if (!(this instanceof f))
        return new f(t);
    uu.call(this, t),
    this._transformState = {
        afterTransform: h.bind(this),
        needTransform: !1,
        transforming: !1,
        writecb: null,
        writechunk: null,
        writeencoding: null
    },
    this._readableState.needReadable = !0,
    this._readableState.sync = !1,
    t && ("function" === typeof t.transform && (this._transform = t.transform),
    "function" === typeof t.flush && (this._flush = t.flush)),
    this.on("prefinish", c)
}


function a() {
    f.call(this, 64),
    this._a = 1732584193,
    this._b = 4023233417,
    this._c = 2562383102,
    this._d = 271733878
}

function md5(t) {
    return t = t.toLowerCase(),
    "md5" === t ? new a : "rmd160" === t || "ripemd160" === t ? new o : new u(s(t))
}
function v(e) {
    return md5("md5").update(e.toString()).digest("hex")
}

function hh(e, t) {
    return v(`client=${d}&mysticTime=${e}&product=${u}&key=${t}`)
}

const t = (new Date).getTime();
let e = 'fsdsogkndfokasodnaso'
let d = "fanyideskweb"
let u = 'webfanyi'

console.log(hh(t, e))
