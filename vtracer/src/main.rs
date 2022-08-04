mod algo;
mod util;

use std::fs;

fn main() {
    let img_ar = util::random_image_array(256, 256, 3, false).unwrap();
    let svg = algo::vtrace_image_array(img_ar).unwrap();

    fs::write("test.svg", svg).unwrap();
}
