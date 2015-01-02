fn main() {
  println!("If you see this, the tests were not compiled nor ran!");
}

fn solution(x: i32) -> i32 {
  let mut y = 0;
  for i in 0..x {
    if i%3 == 0 {
      y = y + i;
    } else if i%5 == 0 {
      y = y + i;
    } else {
      continue;
    }
  }
  return y;
}

#[test]
fn test_solution_zero() {
  assert!(solution(0) == 0);
}

#[test]
fn test_solution_ten() {
  assert!(solution(10) == 23);
}

#[test]
fn test_solution(){
  assert!(solution(1000) == 233168);
}
