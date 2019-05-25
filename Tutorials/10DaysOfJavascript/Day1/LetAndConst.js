const PI = Math.PI;

function area(r) {
    return PI * r * r;
}

function perimeter(r) {
    return 2 * PI * r;
}

let r = readLine();
console.log(area(r));
console.log(perimeter(r));
