function modifyArray(numbers) {
    return numbers.map(number => (number % 2 == 0) ? number * 2 : number * 3);
}
