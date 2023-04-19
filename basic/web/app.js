/*function hello() {
    return document.write("hello world!");
}
hello();

store = {};
store.candyPrice = 4;
store.candyNum = 3;
document.writeln(store.candyPrice * store.candyNum);

var wall = new Object();
wall.store = store;
document.write(typeof wall.store);

var IO = new Object();
function print(result){
    document.write(result);
}
IO.print = print;
IO.print("Koukou Luotianyi");
IO.print(typeof IO.print);

var Person = function() {
    this.name = "phodal";
    this.weight = 50;
    this.height = 166;
    this.future = function dream() {
        return "Future";
    };
};

var person = new Person();
document.write(person.name + "<br>");
document.write(typeof person + "<br>");
document.write(person.future() + "<br>");
*/

var Chinese = function() {
    this.country = "China";
}

var People = function(height, weight, name) {
    this.height = height;
    this.weight = weight;
    this.name = name;
}

Chinese.prototype = new People();
var phodal = new Chinese("phodal", 50, 166);
// document.write(phodal.country);
// document.write(phodal.prototype.name);

var para = document.getElementById("para");
// para.style.color = "blue";