use rand::{thread_rng, Rng};

pub fn random_image_array(
    rows: u32,
    cols: u32,
    channels: u32,
    verbose: bool,
) -> Result<Vec<Vec<Vec<u8>>>, String> {
    let mut rng = thread_rng();
    let ret: Vec<Vec<Vec<u8>>> = (0..rows)
        .map(|_| {
            (0..cols)
                .map(|_| (0..channels).map(|_| rng.gen_range(0..256) as u8).collect())
                .collect()
        })
        .collect();

    if verbose {
        for row in ret.iter() {
            for col in row {
                print!("[ ");
                for channel in col {
                    print!("{} ", channel);
                }
                print!("]");
            }
            println!();
        }
    }

    Ok(ret)
}
