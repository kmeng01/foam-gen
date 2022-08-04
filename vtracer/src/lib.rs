mod algo;

use std::vec::Vec;
use pyo3::{prelude::*, exceptions};

#[pyfunction]
fn trace(img: Vec<Vec<Vec<u8>>>) -> PyResult<String> {
    match algo::vtrace_image_array(img) {
        Ok(svg) => Ok(svg),
        Err(e) => Err(exceptions::PyRuntimeError::new_err(format!("Runtime Error: {}", e))),
    }
}

#[pymodule]
fn rustpy_vtracer(_py: Python, m: &PyModule) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(trace, m)?)?;
    Ok(())
}
