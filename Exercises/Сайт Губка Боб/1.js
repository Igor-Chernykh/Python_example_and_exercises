let in1 = document.getElementById("in1")
let but = document.getElementById("but1")

but.onclick =function(){
    let text = in1.value
    alert(text)
    in1.value = ""
}
