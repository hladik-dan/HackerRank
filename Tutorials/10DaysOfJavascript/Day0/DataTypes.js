function add(first, second) {
    return first + second;
}

function performOperation(secondInteger, secondDecimal, secondString) {
    const firstInteger = 4;
    const firstDecimal = 4.0;
    const firstString = "HackerRank ";

    console.log(add(Number(firstInteger), Number(secondInteger)));
    console.log(add(Number(firstDecimal), Number(secondDecimal)));
    console.log(add(firstString, secondString));
}
