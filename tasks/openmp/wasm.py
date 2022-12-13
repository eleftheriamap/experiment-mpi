from invoke import task
from os.path import join
from tasks.util.env import (
    DGEMM_DOCKER_WASM,
    DGEMM_FAASM_USER,
    DGEMM_FAASM_FUNC,
    LULESH_DOCKER_WASM,
    LULESH_FAASM_USER,
    LULESH_FAASM_FUNC,
    KERNELS_WASM_DIR,
    OPENMP_KERNELS,
    OPENMP_KERNELS_FAASM_USER,
)
from tasks.util.upload import upload_wasm


@task(default=True)
def upload(ctx):
    """
    Upload the OpenMP functions to Granny
    """
    wasm_file_details = [
        {
            "wasm_file": LULESH_DOCKER_WASM,
            "wasm_user": LULESH_FAASM_USER,
            "wasm_function": LULESH_FAASM_FUNC,
            "copies": 1,
        },
        {
            "wasm_file": DGEMM_DOCKER_WASM,
            "wasm_user": DGEMM_FAASM_USER,
            "wasm_function": DGEMM_FAASM_FUNC,
            "copies": 1,
        },
    ]

    for kernel in OPENMP_KERNELS:
        wasm_file_details.append(
            {
                "wasm_file": join(
                    KERNELS_WASM_DIR, "omp_{}.wasm".format(kernel)
                ),
                "wasm_user": OPENMP_KERNELS_FAASM_USER,
                "wasm_function": kernel,
                "copies": 1,
            }
        )

    upload_wasm(wasm_file_details)
