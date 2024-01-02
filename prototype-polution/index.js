function extendArrayPrototype() {
  Array.prototype.myCustomFunction = function () {
    console.log("Custom function called!");
  };
}
function extendnewArrayPrototype() {
  Object.prototype.newCustomFunction = function () {
    console.log("bạn đa tạo một customer mới ở trong class");
  };
}
extendnewArrayPrototype();
extendArrayPrototype();
var myArray = [1, 2, 3];
myArray.myCustomFunction(); // In ra 'Custom function called!'

Array.prototype.myCustomFunction = function () {
  console.log("bạn hãy hack tôi đi");
};
var newArray = [1, 2, 3];
newArray.myCustomFunction();

// ví dụ khác với Object như sau

let read = {};
Object.prototype.homeless = "có hay không";
console.log(
  read.homeless,
  "đây là giá trị của homeless nha các bạn tôi ở dòng 28"
);

console.log(read.__proto__.homeless, "đây lad dòng 31 nha các bạn");
