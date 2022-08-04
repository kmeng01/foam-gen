use std::{io, str::FromStr};

fn get_square_array(n: u32) -> Result<Vec<Vec<i32>>, String> {
    let mut vec: Vec<Vec<i32>> = Vec::new();
    let n = n as usize;

    while vec.len() < n {
        let nums_str = get_single_line(Some(format!(
            "Enter {} space-separated numbers for row {} of the matrix",
            n,
            vec.len()
        )))?;

        let nums = nums_str
            .split(" ")
            .filter(|f| f.len() > 0)
            .map(|f| match f.parse::<i32>() {
                Ok(num) => Ok(num),
                Err(e) => return Err(format!("Could not parse input into numbers: {}", e)),
            })
            .collect::<Result<Vec<i32>, String>>();

        if nums.is_err() {
            println!("Error: {}. Continuing...", nums.unwrap_err());
            continue;
        }

        let nums = nums.unwrap();
        if nums.len() != n {
            println!(
                "Error: Expected {} items, found {}. Continuing...",
                n,
                nums.len()
            );
        }

        vec.push(nums);
    }

    Ok(vec)
}

fn get_fpath(is_input: bool) -> Result<String, String> {
    get_single_line(Some(format!(
        "Please enter the {} filepath",
        if is_input { "input" } else { "output" }
    )))
}

fn get_single_line(msg: Option<String>) -> Result<String, String> {
    match msg {
        None => {}
        Some(s) => println!("{}", s),
    };

    let mut buffer = String::new();
    match io::stdin().read_line(&mut buffer) {
        Ok(_) => {}
        Err(e) => return Err(format!("Error reading from stdin: {}", e)),
    };

    let buffer = match String::from_str(buffer.trim()) {
        Ok(s) => s,
        Err(e) => return Err(format!("Error parsing input: {}", e)),
    };

    return Ok(buffer);
}