# test_plotter.py
import unittest
from src.plotter import Plotter

class TestPlotter(unittest.TestCase):
    def test_draw_plots(self):
        plotter = Plotter(output_dir="test_plots")
        plot_paths = plotter.draw_plots("deviation.json")

        # Check that the function returns the expected output paths
        self.assertTrue(len(plot_paths) > 0, "No plots were generated")
        for path in plot_paths:
            self.assertTrue(path.endswith(".png"), "Plot paths should be PNG files")

if __name__ == "__main__":
    unittest.main()
