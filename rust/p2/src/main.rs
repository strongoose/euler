struct Fibonacci {
    curr: u32,
    next: u32,
}

impl Iterator for Fibonacci {
    type Item = u32;

    fn next(&mut self) -> Option<u32> {
        let new_next = self.curr + self.next;

        self.curr = self.next;
        self.next = new_next;

        Some(self.curr)
    }
}

fn fibonacci() -> Fibonacci {
    Fibonacci { curr: 1, next: 1 }
}

fn main() {
    println!(
        "{}",
        fibonacci()
            .take_while(|n| *n < 4000000_u32)
            .filter(|n| n % 2 == 0)
            .sum::<u32>()
    )
}
