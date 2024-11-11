import unittest
import os
from src.plotter import Plotter

class TestPlotter(unittest.TestCase):

    def test_draw_plots(self):
        # Initialize the Plotter object with an output directory
        plotter = Plotter(output_dir="test_plots")

        # Path to the input data file (deviation.json)
        data_path = "deviation.json"

        # Check if the data file exists (for debugging)
        if not os.path.exists(data_path):
            self.fail(f"Input data file '{data_path}' does not exist")

        # Call the method to generate plot paths
        plot_paths = plotter.draw_plots(data_path)

        # Debugging point: Inspect plot_paths
        print(f"Generated plot paths: {plot_paths}")

        # Ensure that the output paths are generated
        self.assertTrue(len(plot_paths) > 0, "No plots were generated")

        # Ensure all plot paths are valid PNG files (for debugging)
        for path in plot_paths:
            self.assertTrue(path.endswith(".png"), f"Plot path {path} should end with .png")
            # Debugging point: Check the content of each path variable
            print(f"Evaluating plot path: {path}")

    # You can add more tests here for other methods of Plotter if needed

if __name__ == "__main__":
    unittest.main()
