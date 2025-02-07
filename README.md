# BB84 QKD Protocol Using Qiskit and Python

This repository contains the code for our IEEE research paper on the BB84 Quantum Key Distribution (QKD) protocol. Our implementation demonstrates secure key exchange by simulating the BB84 protocol on IBM Quantum hardware using Qiskit and Python.

## Code Overview

- **encode_message(bits, bases):**  
  Encodes a random sequence of bits into quantum circuits using either the Z or X basis.

- **measure_message(message, bases):**  
  Simulates Bob’s measurement of the qubits. Applies a Hadamard gate for X-basis measurements.

- **remove_garbage(a_bases, b_bases, bits):**  
  Filters out bits where Alice and Bob used mismatched bases, producing the final sifted key.

The script generates random bits and bases for both Alice and Bob, encodes each qubit accordingly, executes the circuits on the IBM Quantum backend (`ibm_kyiv`), and finally prints the sifted keys.

## How to Run

1. **Install Dependencies:**
   ```bash
   pip install qiskit qiskit-ibm-provider numpy
   ```
2. Set Your IBM API Key:
3. Replace 'YOUR_API_TOKEN_HERE' in the script with your IBM Quantum API key.
4. Run the Script:
```bash
python main_2.py
```

## Example Output
```pgsql
Alice's key: [0, 1, 1]
Bob's key: [0, 1, 1]

Circuit: 
    ┌───┐┌───┐┌─┐           
q_0: ┤ H ├┤ H ├┤M├───────────
     ├───┤├───┤└╥┘┌───┐┌─┐   
q_1: ┤ X ├┤ H ├─╫─┤ H ├┤M├───
     ├───┤├───┤ ║ ├───┤└╥┘┌─┐
q_2: ┤ X ├┤ H ├─╫─┤ H ├─╫─┤M├
     ├───┤└┬─┬┘ ║ └───┘ ║ └╥┘
q_3: ┤ H ├─┤M├──╫───────╫──╫─
     └───┘ └╥┘  ║       ║  ║ 
c: 4/═══════╩═══╩═══════╩══╩═
            3   0       1  2

```

## Performance Metrics
In practice, the performance of the protocol is assessed by two key metrics:
Quantum Bit Error Rate (QBER):
This metric indicates the ratio of erroneous bits in the sifted key. A low QBER signifies a high-quality key exchange.

### Key Generation Rate:
This reflects the fraction of transmitted qubits that remain in the final sifted key after basis reconciliation.

These metrics help evaluate the effectiveness of the protocol under various conditions and provide insight into the influence of factors such as quantum noise and potential eavesdropping.

## Conclusion
Provided an in-depth experimental analysis of the BB84 QKD protocol using Qiskit and Python, executed on IBM Quantum hardware. By detailing the process of qubit encoding, measurement, basis reconciliation, and key sifting, the paper demonstrates that secure key generation is achievable under ideal conditions. The discussion on performance metrics and security implications is intended to guide researchers and practitioners interested in implementing and extending quantum key distribution protocols.
The findings contribute to the ongoing efforts to develop practical and secure quantum-based communication systems. Future work will focus on improving system performance and security, as well as exploring the integration of QKD with other cryptographic techniques for a more robust secure communication infrastructure.

