mod algo;

use std::vec::Vec;
use pyo3::{prelude::*, exceptions};

#[pyfunction]
fn trace(img: Vec<Vec<Vec<u8>>>, color_precision: i32, layer_diff: i32, length_threshold: f64) -> PyResult<String> {
    match algo::vtrace_image_array(img, color_precision, layer_diff, length_threshold) {
        Ok(svg) => Ok(svg),
        Err(e) => Err(exceptions::PyRuntimeError::new_err(format!("Runtime Error: {}", e))),
    }
}

#[pymodule]
fn rustpy_vtracer(_py: Python, m: &PyModule) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(trace, m)?)?;
    Ok(())
}
