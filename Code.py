%matplotlib inline
# Importing standard Qiskit libraries and configuring account
from qiskit import QuantumCircuit, execute, Aer, IBMQ
from qiskit.compiler import transpile, assemble
from qiskit.tools.jupyter import *
from qiskit.visualization import *
# Loading your IBM Q account(s)
provider = IBMQ.load_account()

secretnumber='110011'#random number, you can insert in any number here for the program to guess

circuit= QuantumCircuit(6+1,6)
circuit.h([0,1,2,3,4,5])#applying haadamard gates to qubits 0 to 5
circuit.x(6)#applying x gate to qubit 6
circuit.h(6)#applying haadamard gate to qubit 6
circuit.barrier()
circuit.cx(5,6)#controlled x gate on qubit 5,4,1,0
circuit.cx(4,6)
circuit.cx(1,6)
circuit.cx(0,6)
circuit.barrier()
circuit.h([0,1,2,3,4,5])#Applying haadamard gates on qubits 0 to 5
circuit.barrier()
circuit.measure([0,1,2,3,4,5],[0,1,2,3,4,5])#measuring qubits 
simulator=Aer.get_backend('qasm_simulator')
result=execute(circuit, backend=simulator, shots=1).result()
counts=result.get_counts()
print(counts)#printing out result
