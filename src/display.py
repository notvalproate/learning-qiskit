from qiskit import QuantumCircuit
import matplotlib.pyplot as plt

def circuit(qc: QuantumCircuit) -> None:
    qc.draw(output="mpl")
    plt.show()