 Here is Rust code to reverse a string:

```rust
fn reverse_string(input: &str) -> String {
  let mut result = String::new();
  for c in input.chars().rev() {
    result.push(c);
  }
  result
}

fn main() {
  let original = "Hello";
  let reversed = reverse_string(&original);
  println!("{} reversed is {}", original, reversed);
}
```

The key points:

- The `reverse_string` function takes a string slice (`&str`) as input and returns an owned `String` as output. 
- It iterates through the characters in reverse order using `chars().rev()` and pushes each one onto a `String`.
- The `main` function shows an example of calling `reverse_string` and printing the original and reversed strings.