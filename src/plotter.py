import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

class Plotter:
    def __init__(self, output_dir="plots"):
        self.output_dir = output_dir
        os.makedirs(output_dir, exist_ok=True)

    def draw_plots(self, data_path):
        # Load data
        df = pd.read_json(data_path)

        # List to store paths of saved plots
        plot_paths = []

        # Plotting Mean, Max, and Min deviation per room
        deviation_columns = ['mean', 'max', 'min']  # Updated column names
        for col in deviation_columns:
            plt.figure(figsize=(10, 6))
            sns.histplot(df[col], kde=True, color='skyblue')
            plt.title(f'{col} Deviation Distribution')
            plt.xlabel(f'{col} Deviation (degrees)')
            plt.ylabel('Frequency')
            
            plot_path = os.path.join(self.output_dir, f"{col}_deviation.png")
            plt.savefig(plot_path)
            plot_paths.append(plot_path)
            plt.close()

        # Comparison of Gt_corners and Rb_corners
        plt.figure(figsize=(10, 6))
        sns.scatterplot(data=df, x='gt_corners', y='rb_corners')  # Column names updated to lowercase
        plt.plot([df['gt_corners'].min(), df['gt_corners'].max()],
                 [df['gt_corners'].min(), df['gt_corners'].max()],
                 'r--', label='Perfect Prediction')
        plt.xlabel('Ground Truth Corners')
        plt.ylabel('Predicted Corners')
        plt.legend()
        
        plot_path = os.path.join(self.output_dir, "Gt_vs_Rb_corners.png")
        plt.savefig(plot_path)
        plot_paths.append(plot_path)
        plt.close()

        return plot_paths
