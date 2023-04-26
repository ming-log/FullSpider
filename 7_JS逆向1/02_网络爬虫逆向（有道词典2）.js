function fn(t,o,n){
    if (!t)
        return null;
    const a = e.alloc(16, g(o))
      , c = e.alloc(16, g(n))
      , i = r.a.createDecipheriv("aes-128-cbc", a, c);
    let s = i.update(t, "base64", "utf-8");
    return s += i.final("utf-8"),
    s
}
t1 = '_jsUyA02rwkOJ4enKX7c4dhd7CjvGkcKfbRx0BjNGW8OgIRH1rgaj5tPhWMKWNW-K3LvAiHRuWyRQBuU0gsuSO1UMxOFFDAcuWENI9r5kAC_7uF2IYJB6c0tWv4hIs7AuFlzgAB95o1_JgWV7d1N9DJdD-laTCZ5Hl57jDPB_l4='
o1 = "ydsecret://query/key/B*RGygVywfNBwpmBaZg*WT7SIOUP2T0C9WHMZN39j^DAdaZhAnxvGcCY6VYFwnHl"
n1 = "ydsecret://query/iv/C@lZe2YzHtZ2CYgaXKSVfsb7Y4QWHjITPPZ0nQp87fBeJ!Iv6v^6fvi2WN@bYpJ4"

console.log(fn(t1,o1,n1))
