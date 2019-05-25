function vowels(string) {
    for (let s of string) {
        if (/([^aeiou])/.test(s)) {
            continue;
        }

        console.log(s);
    }
}

function consonants(string) {
    for (let s of string) {
        if (/([aeiou])/.test(s)) {
            continue;
        }

        console.log(s);
    }
}

function vowelsAndConsonants(string) {
    vowels(string);
    consonants(string);
}
