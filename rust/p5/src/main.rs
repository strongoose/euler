fn gcd(x: usize, y: usize) -> usize {
    let [mut a, mut b] = if x >= y { [x, y] } else { [y, x] };
    let mut t;

    while b != 0 {
        t = b;
        b = a % b;
        a = t;
    }
    a
}

fn lcm(x: usize, y: usize) -> usize {
    x / gcd(x, y) * y
}

fn main() {
    // This relies on lcm(a, b, c) == lcm(lcm(a, b), c), which follows from the fundamental theorem
    // of arithmetic.
    println!("{}", (2..=20).fold(1, lcm));
}
