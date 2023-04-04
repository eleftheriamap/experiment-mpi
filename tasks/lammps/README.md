# LAMMPS Experiment

This experiment is a single execution of the LAMMPS simulation stress tested
as part of the array experiment.

## Start AKS cluster

```bash
inv cluster.provision --vm Standard_D8_v5 --nodes 2
inv cluster.credentials
```

## Granny

Deploy the cluster:

```bash
WASM_VM=wamr inv k8s.deploy --workers=2
```

Upload the WASM file:

```bash
inv lammps.wasm.upload
```

And run:

```bash
inv lammps.run.granny --data=[compute-xl,network] --repeats=number_of_repeats
```

## Native

Deploy the cluster:

```bash
inv lammps.native.deploy
```

And run:

```bash
inv lammps.run.native --data=[compute-xl,network] --repeats=number_of_repeats
```

# Plot

TODO:

## Clean-Up

Remember to delete the cluster:

```bash
inv cluster.delete
```
