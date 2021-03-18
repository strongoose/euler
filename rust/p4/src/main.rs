struct Products {
    start: usize,
    end: usize,

    i: usize,
    j: usize,

    stop: bool,
}

impl Products {
    fn new(start: usize, end: usize) -> Products {
        Products {
            start,
            end,
            i: start,
            j: start,
            stop: false,
        }
    }
}

impl Iterator for Products {
    type Item = usize;

    fn next(&mut self) -> Option<usize> {
        if self.stop {
            return None;
        }

        let prod = self.i * self.j;

        if self.j < self.end {
            self.j += 1;
        } else if self.i < self.end {
            self.i += 1;
            self.j = self.start;
        } else {
            self.stop = true;
        }

        Some(prod)
    }
}

fn is_palindrome(s: &str) -> bool {
    let mut string = s.to_string();
    while string.len() > 1 {
        if string.remove(0) != string.pop().unwrap() {
            return false;
        }
    }
    return true;
}

fn main() {
    println!(
        "{:#?}",
        Products::new(100, 999)
            .filter(|n| is_palindrome(&n.to_string()))
            .max()
            .unwrap()
    );
}
