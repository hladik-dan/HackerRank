function sides(literals, ...expressions) {
    let a = expressions[0];
    let p = expressions[1];
    let d = Math.sqrt((p * p) - 16 * a);

    return [(p + d) / 4, (p - d) / 4].sort();
}
