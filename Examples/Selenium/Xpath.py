https://www.youtube.com/watch?v=zGYdbHACmLI

//h3[@class="header"]
//h3[2]

// - начало
h3 - блок на странице
[
@ - обращаемся к тэгу
class="header"
]
[2] - достать элемент под номером из выборки

//h3[@class="header"][2]

class="header yellow"
//h3[@class="header yellow"]

class="header" thestyle = "red"
//h3[@class ="header"][@thestyle="red"]
//h3[@class ="header" and @thestyle="red"]

если длинный заголовок
//h3[contains(@class, "kitty-kat")][contains(@class, "abracadabra")]

