// hook -> 记下来. 后面遇到了. 可以直接用. 不是百分之百可用.
Function.prototype._constructor = Function.prototype.constructor
Function.prototype.constructor = function(){
    if(arguments[0] === 'debugger'){
        return function(){}
    } else{
        return Function.prototype._constructor.apply(this, arguments)
    }
}
