# Imports and Setup

from qiskit import QuantumCircuit, transpile, Aer
from qiskit_ibm_provider import IBMProvider
import numpy as np

provider = IBMProvider('IBM_API_Key')

# Encode
def encode_message(bits, bases):
    message = []
    for i in range(len(bits)):
        qc = QuantumCircuit(1, 1)
        if bases[i] == 0:  # Prepare qubit in Z-basis
            if bits[i] == 1:
                qc.x(0)
        else:  # Prepare qubit in X-basis
            if bits[i] == 0:
                qc.h(0)
            else:
                qc.x(0)
                qc.h(0)
        qc.measure(0, 0)
        message.append(qc)
    return message

# Measure
def measure_message(message, bases):
    measurements = []
    for q, basis in zip(message, bases):
        if basis == 1:  # measuring in X-basis
            q.h(0)
        measurements.append(q)
    return measurements

# Key Sifting
def remove_garbage(a_bases, b_bases, bits):
    return [bit for i, bit in enumerate(bits) if a_bases[i] == b_bases[i]]


# Implement BB84 protocol
np.random.seed(seed=0)

    # Alice generates random bits and bases
alice_bits = np.random.randint(2, size=4)
alice_bases = np.random.randint(2, size=4)
message = encode_message(alice_bits, alice_bases)

    # Bob generates random bases for measurement
bob_bases = np.random.randint(2, size=4)
bob_results = measure_message(message, bob_bases)


# Execute on backend
Backend='ibm_kyiv'
backend = provider.get_backend(Backend)
transpiled_circuits = transpile(bob_results, backend)
job = backend.run(transpiled_circuits, shots=1)
result = job.result()
counts = result.get_counts()

# Process results
bob_measured_bits = [int(list(count.keys())[0]) for count in counts]

# Step 3
alice_key = remove_garbage(alice_bases, bob_bases, alice_bits)
bob_key = remove_garbage(alice_bases, bob_bases, bob_measured_bits)

print("Alice's bits:", alice_bits)
print("Alice's bases:", alice_bases)
print("Bob's bases:", bob_bases)
print("Bob's results:", bob_measured_bits)
print("Alice's key:", alice_key)
print("Bob's key:", bob_key)

# Key Verification
if alice_key == bob_key:
    print("Success: Alice and Bob's keys match!")
else:
    print("Warning: Alice and Bob's keys do not match.")
    print("Mismatched positions:")
    for i, (a, b) in enumerate(zip(alice_key, bob_key)):
        if a != b:
            print(f"Position {i}: Alice has {a}, Bob has {b}")

    print("\nDetailed analysis:")
    print("Matching bases positions:", [i for i, (a, b) in enumerate(zip(alice_bases, bob_bases)) if a == b])
    print("Alice's bits at matching bases:", [alice_bits[i] for i, (a, b) in enumerate(zip(alice_bases, bob_bases)) if a == b])
    print("Bob's measured bits at matching bases:", [bob_measured_bits[i] for i, (a, b) in enumerate(zip(alice_bases, bob_bases)) if a == b])

# Q Circuit
qc = QuantumCircuit(4, 4)

for i in range(4):
    if alice_bases[i] == 0:
        if alice_bits[i] == 1:
            qc.x(i)
    else:
        if alice_bits[i] == 0:
            qc.h(i)
        else:
            qc.x(i)
            qc.h(i)
    
    if bob_bases[i] == 1:
        qc.h(i)
    
    qc.measure(i, i)

print(qc)
