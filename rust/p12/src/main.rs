use itertools::Itertools;

#[derive(Debug)]
struct Primes {
    prev: Vec<usize>,
}

impl Primes {
    fn new() -> Primes {
        Primes { prev: vec![] }
    }
}

impl Iterator for Primes {
    type Item = usize;

    fn next(&mut self) -> Option<usize> {
        let is_next_prime = |n| !self.prev.iter().any(|p| n % p == 0);

        let mut i: usize;
        if self.prev.len() == 0 {
            i = 2
        } else {
            i = self.prev.last().unwrap() + 1;
            while !is_next_prime(i) {
                i += 1;
            }
        }

        self.prev.push(i);
        Some(i)
    }
}

fn factorise(n: usize) -> Vec<usize> {
    let mut D = n;
    let mut factors = vec![];
    let mut ps = Primes::new();

    while D != 1 {
        let f = ps.find(|p| D % p == 0).unwrap();
        while D % f == 0 {
            factors.push(f);
            D = D / f;
        }
    }

    factors
}

fn divisors(n: usize) -> Vec<usize> {
    let prime_factors = factorise(n);

    let mut divisors = vec![];
    for i in 1..prime_factors.len() {
        for fs in prime_factors.iter().combinations(i) {
            let divisor = fs.iter().map(|&&n| n)
                .product();
            divisors.push(divisor)
        };
    }

    divisors.into_iter().unique().collect()
}

#[derive(Debug)]
struct Triangles {
    i: usize,
}

impl Triangles {
    fn new() -> Triangles {
        Triangles { i: 0 }
    }
}

impl Iterator for Triangles {
    type Item = usize;

    fn next(&mut self) -> Option<usize> {
        self.i += 1;
        Some((0..=self.i).sum())
    }
}

fn main() {
    println!("{:#?}", Triangles::new().find(|&n| {
        divisors(n).len() > 500
    }).unwrap())
}
