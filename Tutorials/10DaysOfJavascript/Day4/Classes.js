class Polygon {
    constructor(sideLengths) {
        this.sideLengths = sideLengths;
    }

    perimeter() {
        let result = 0;

        for (let sideLength of this.sideLengths) {
            result += sideLength;
        }

        return result;
    }
}
