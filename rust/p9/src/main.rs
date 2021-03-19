use itertools::Itertools;

fn main() {
    let pythagorean = (1..1000)
        .combinations(2)
        .filter(|v| v[0] + v[1] < 1000)
        .map(|v| {
            let a = v[0];
            let b = v[1];
            let c = 1000 - (a + b);
            let mut res = vec![a, b, c];
            res.sort();
            res
        })
        .find(|v| {
            let a = v[0];
            let b = v[1];
            let c = v[2];

            a * a + b * b == c * c
        })
        .unwrap();

    let p: usize = pythagorean.iter().product();
    println!("{:#?}", p)
}
