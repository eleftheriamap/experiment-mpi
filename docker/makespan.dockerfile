ARG EXPERIMENT_VERSION
FROM faasm/experiment-lammps:${EXPERIMENT_VERSION}

WORKDIR /code/experiment-mpi
