# Sequentially-Controlled Interactive Multi-Particle Flow-Maps (IMPFM)

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![License](https://img.shields.io/badge/License-MIT-green)
![Status](https://img.shields.io/badge/Status-Active-brightgreen)
![Contributions](https://img.shields.io/badge/Contributions-Welcome-orange)

---

## Overview

This repository contains the official Python implementation of the paper **[Sequentially-Controlled Interactive Multi-Particle Flow-Maps for Online Feedback-Driven Search](https://arxiv.org/pdf/2607.01144v1)** by Binglin Ji, Anindya Sarkar, Hengchang Lu, Jens Sjölund, and Yevgeniy Vorobeychik.

In this work, the authors propose **IMPFM**, a novel framework for **sample-efficient online feedback-driven search**. The method is designed to address scenarios where preferences are unknown a priori and are revealed sequentially through feedback. Unlike traditional methods that focus on local exploration, IMPFM enables **broad exploration** of the underlying distribution while progressively steering particles toward high-utility regions.

### Key Contributions of the Paper:
1. **Interactive Multi-Particle Flow-Maps (IMPFM):** A framework for feedback-driven search that uses a principled posterior sample sharing mechanism across particles to maintain broad exploration and prevent mode collapse.
2. **Exploration-Exploitation Trade-off:** A reweighting mechanism that balances exploration and exploitation, ensuring structural diversity and mitigating weight degeneracy.
3. **Feynman-Kac Corrector:** Theoretical guarantees that the multi-particle system is steered toward a KL-tilted target distribution, facilitating robust global exploration.
4. **Empirical Validation:** Extensive experiments demonstrate the superiority of IMPFM over existing baselines in diverse search and alignment tasks.

---

## How It Works

IMPFM combines the principles of particle filtering, flow maps, and sequential Monte Carlo (SMC) methods to create a novel framework for online search. Here's a high-level breakdown of how it works:

### 1. **Multi-Particle Dynamics**
   - A set of particles is initialized to represent the search space.
   - These particles interact through a **posterior sample sharing mechanism**, which corrects individual particle drift using the collective posterior samples of the entire ensemble.

### 2. **Flow Maps for Efficient Transport**
   - Flow maps are employed to progressively transport the particles toward the target distribution.
   - This ensures that the particles maintain broad coverage of the search space while moving toward regions of higher utility.

### 3. **Exploration-Exploitation Reweighting**
   - A principled reweighting mechanism balances exploration and exploitation.
   - This prevents particles from collapsing into a single mode and preserves structural diversity.

### 4. **Feynman-Kac Corrector**
   - The framework introduces a Feynman-Kac corrector that ensures the particle system converges to a KL-tilted target distribution.
   - This corrector actively mitigates reward over-optimization, a common issue in standard control frameworks.

### 5. **Feedback-Driven Search**
   - The framework is designed for scenarios where preferences are revealed sequentially through feedback.
   - IMPFM uses this feedback to iteratively refine the particle distribution, improving sample efficiency and alignment with the target distribution.

---

## Installation

To use this implementation, ensure you have Python 3.8 or higher installed. Clone this repository and install the required dependencies:

```bash
git clone https://github.com/your-username/IMPFM.git
cd IMPFM
pip install -r requirements.txt
```

---

## Usage

The implementation is provided in the `implementation.py` script. Below is an example of how to use the script to run the IMPFM framework on a sample task.

### Example Usage

1. **Prepare Your Data:**
   Ensure you have a dataset or a search space defined. For example:
   ```python
   import numpy as np
   # Define a sample search space
   search_space = np.random.uniform(-10, 10, (1000, 2))  # 1000 2D points
   ```

2. **Run the IMPFM Framework:**
   Use the `IMPFM` class from `implementation.py` to initialize and run the framework:
   ```python
   from implementation import IMPFM

   # Initialize the IMPFM framework
   impfm = IMPFM(search_space=search_space, num_particles=50, feedback_function=my_feedback_function)

   # Run the feedback-driven search
   results = impfm.run(num_iterations=100)

   # Access the final particle distribution
   final_particles = results['particles']
   ```

3. **Define a Feedback Function:**
   The feedback function should evaluate the utility of a given particle based on your specific task. For example:
   ```python
   def my_feedback_function(particle):
       # Example: A simple 2D Gaussian reward function
       return -np.linalg.norm(particle - np.array([3, 3]))
   ```

4. **Visualize Results:**
   You can visualize the particle trajectories and final distribution using your preferred plotting library (e.g., Matplotlib):
   ```python
   import matplotlib.pyplot as plt

   # Plot initial and final particle distributions
   plt.scatter(search_space[:, 0], search_space[:, 1], alpha=0.3, label='Search Space')
   plt.scatter(final_particles[:, 0], final_particles[:, 1], color='red', label='Final Particles')
   plt.legend()
   plt.show()
   ```

---

## File Structure

```
IMPFM/
│
├── implementation.py       # Main implementation of the IMPFM framework
├── requirements.txt        # List of dependencies
├── examples/               # Example scripts to run the framework
│   └── example_task.py     # Example usage on a sample task
├── README.md               # Project documentation
└── LICENSE                 # MIT License
```

---

## Contributing

We welcome contributions to improve this implementation! If you'd like to contribute, please follow these steps:
1. Fork this repository.
2. Create a new branch (`git checkout -b feature-name`).
3. Commit your changes (`git commit -m "Add some feature"`).
4. Push to the branch (`git push origin feature-name`).
5. Open a pull request.

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## Acknowledgments

This implementation is based on the paper **[Sequentially-Controlled Interactive Multi-Particle Flow-Maps for Online Feedback-Driven Search](https://arxiv.org/pdf/2607.01144v1)**. If you find this work useful, please consider citing the paper:

```
@article{ji2023impfm,
  title={Sequentially-Controlled Interactive Multi-Particle Flow-Maps for Online Feedback-Driven Search},
  author={Binglin Ji and Anindya Sarkar and Hengchang Lu and Jens Sjölund and Yevgeniy Vorobeychik},
  journal={arXiv preprint arXiv:2607.01144v1},
  year={2023}
}
```

---

Happy exploring with IMPFM! 🚀