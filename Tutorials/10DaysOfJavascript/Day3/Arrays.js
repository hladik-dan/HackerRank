function getSecondLargest(numbers) {
    let first = Number.NEGATIVE_INFINITY;
    let second = Number.NEGATIVE_INFINITY;

    for (let number of numbers) {
        if (number > first) {
            second = first;
            first = number;

            continue;
        }

        if (second < number && number < first) {
            second = number;

            continue;
        }
    }

    return second;
}
