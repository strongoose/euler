use rand::prelude::*;

#[derive(Debug)]
struct Primes {
    prev: Vec<usize>,
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

fn primes() -> Primes {
    Primes { prev: vec![] }
}

fn factorise(n: usize) -> Vec<usize> {
    let mut D = n;
    let mut factors = vec![];
    let mut ps = primes();

    while D != 1 {
        let f = ps.find(|p| D % p == 0).unwrap();
        while D % f == 0 {
            factors.push(f);
            D = D / f;
        }
    }

    factors
}

fn main() {
    println!("{:#?}", factorise(600851475143).iter().max().unwrap());
}
