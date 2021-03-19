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

impl Primes {
    fn new() -> Primes {
        Primes { prev: vec![] }
    }
}

fn main() {
    let result: usize = Primes::new().take_while(|p| *p < 2000000).sum();
    println!("{}", result)
}
