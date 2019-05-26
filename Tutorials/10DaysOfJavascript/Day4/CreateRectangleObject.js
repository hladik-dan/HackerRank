function Rectangle(length, width) {
    return {
        length: length,
        width: width,
        perimeter: 2 * (length + width),
        area: length * width
    };
}
