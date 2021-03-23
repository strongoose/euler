struct Collatz {
    n: u64,
}

impl Collatz {
    fn new(n: u64) -> Collatz {
        Collatz { n: n }
    }
}

impl Iterator for Collatz {
    type Item = u64;

    fn next(&mut self) -> Option<u64> {
        if self.n == 1 {
            return None;
        }

        let new_n = match self.n % 2 == 0 {
            true => self.n / 2,
            false => 3 * self.n + 1,
        };

        self.n = new_n;
        Some(new_n)
    }
}

fn main() {
    let mut max_n = 0;
    let mut max = 0;

    for n in 1..1000000 {
        let seq: Vec<u64> = Collatz::new(n).collect();
        let l = seq.len();

        if l > max {
            max = l;
            max_n = n;
        }
    }

    println!("{} has a Collatz sequence of length {}", max_n, max)
}
