from qiskit import QuantumCircuit
from qiskit.quantum_info import Pauli
from qiskit_aer.primitives import Estimator

import matplotlib.pyplot as plt

import display

def get_qc_for_n_qubit_GHZ_state(n):
    qc = QuantumCircuit(n)
    qc.h(0)
    for i in range(n-1):
        qc.cx(i, i+1)
    return qc

if __name__ == "__main__":
    print("Hello, Qiskit!")

    qc = QuantumCircuit(2)
    qc.h(0)
    qc.cx(0, 1)

    display.circuit(qc)

    ZZ = Pauli("ZZ")
    ZI = Pauli("ZI")
    IZ = Pauli("IZ")
    XX = Pauli("XX")
    XI = Pauli("XI")
    IX = Pauli("IX")

    observables = [ZZ, ZI, IZ, XX, XI, IX]

    estimator = Estimator()
    job = estimator.run([qc] * len(observables), observables)
    print(job.result())

    data = ['ZZ', 'ZI', 'IZ', 'XX', 'XI', 'IX']
    values = job.result().values

    plt.plot(data, values, '-o')
    plt.xlabel('Observables')
    plt.ylabel('Expectation values')   
    plt.show()

    qc = get_qc_for_n_qubit_GHZ_state(100)
    display.circuit(qc)