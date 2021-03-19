fn sum_of_squares(start: usize, end: usize) -> usize {
    (start..=end).fold(0, |acc, i| acc + i*i)
}

fn square_of_sum(start: usize, end: usize) -> usize {
    let s: usize = (start..=end).sum();
    s*s
}

fn main() {
    println!("{}", square_of_sum(1, 100) - sum_of_squares(1, 100));
}
