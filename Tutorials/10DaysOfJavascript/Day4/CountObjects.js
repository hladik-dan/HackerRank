function getCount(objects) {
    let result = 0;

    for (let object of objects) {
        if (object.x === object.y) {
            result += 1;
        }
    }

    return result;
}
