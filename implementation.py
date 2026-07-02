import numpy as np
import torch
from torch.distributions import MultivariateNormal

class IMPFM:
    def __init__(self, num_particles, dim, target_distribution, feedback_fn, alpha=0.5, beta=0.1):
        self.num_particles = num_particles
        self.dim = dim
        self.target_distribution = target_distribution
        self.feedback_fn = feedback_fn
        self.alpha = alpha  # exploration-exploitation tradeoff
        self.beta = beta    # correction factor
        self.particles = torch.randn(num_particles, dim)  # Initialize particles randomly
        self.weights = torch.ones(num_particles) / num_particles  # Uniform weights

    def compute_flow_map(self):
        # Compute the flow map based on the target distribution and feedback
        scores = self.feedback_fn(self.particles)
        normalized_scores = torch.softmax(scores, dim=0)
        flow_map = self.alpha * normalized_scores + (1 - self.alpha) * self.weights
        return flow_map

    def resample_particles(self, flow_map):
        # Resample particles based on the flow map
        indices = torch.multinomial(flow_map, self.num_particles, replacement=True)
        self.particles = self.particles[indices]
        self.weights = torch.ones(self.num_particles) / self.num_particles

    def correct_drift(self):
        # Correct drift using posterior sample sharing
        mean_particle = torch.mean(self.particles, dim=0)
        self.particles += self.beta * (mean_particle - self.particles)

    def step(self):
        # Perform one step of the IMPFM algorithm
        flow_map = self.compute_flow_map()
        self.resample_particles(flow_map)
        self.correct_drift()

    def run(self, num_steps):
        # Run the IMPFM algorithm for a given number of steps
        for _ in range(num_steps):
            self.step()
        return self.particles

def dummy_feedback_fn(particles):
    # Dummy feedback function: higher scores for particles closer to [1, 1, ..., 1]
    target = torch.ones(particles.shape[1])
    return -torch.norm(particles - target, dim=1)

if __name__ == '__main__':
    # Define the target distribution (Gaussian centered at [1, 1, ..., 1])
    dim = 2
    target_mean = torch.ones(dim)
    target_cov = torch.eye(dim) * 0.5
    target_distribution = MultivariateNormal(target_mean, target_cov)

    # Initialize IMPFM
    num_particles = 100
    impfm = IMPFM(num_particles, dim, target_distribution, dummy_feedback_fn)

    # Run IMPFM for 50 steps
    num_steps = 50
    final_particles = impfm.run(num_steps)

    # Print final particles
    print("Final particles:")
    print(final_particles)