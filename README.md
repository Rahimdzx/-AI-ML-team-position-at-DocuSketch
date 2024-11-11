# Trainee Python Developer (AI-ML Team) - Task Solution

This repository contains my solution to the **"Trainee Python Developer (AI-ML Team)"** task. The task was designed to evaluate my skills in Python development, including unit testing, profiling, debugging, and using external libraries for data visualization.

## Task Steps and Implementation

### 1. **Setup**:
- Created a project in **IntelliJ IDEA**.
- Set up a virtual environment and added a `requirements.txt` file to manage dependencies.

### 2. **Class for Plotting**:
- Implemented a class that handles the plotting of deviations.
- The `draw_plots` function:
    - Reads the provided JSON file (deviation data) as a pandas dataframe.
    - Draws comparison plots for the different columns.
    - Saves the plots in a folder called `plots`.
    - Returns the file paths to the saved plots.

### 3. **Jupyter Notebook**:
- Created a `Notebook.ipynb` file in the root directory to call the `draw_plots` function and visualize the generated plots.

### 4. **Data Handling**:
- Downloaded and processed the provided deviation `JSON` file:
    - `Gt_corners`: Ground truth number of corners in the room.
    - `Rb_corners`: Number of corners detected by the model.
- Calculated statistics, including `mean`, `max`, and `min` deviations in degrees.

### 5. **Unit Testing**:
- Implemented unit tests to verify that the `draw_plots` function behaves as expected and that the generated plot paths are correct.

### 6. **Profiler and Debugger**:
- Used **IntelliJ IDEA**'s built-in profiler to capture performance metrics (CPU and memory usage).
- Set breakpoints and used the debugger to step through the code and evaluate variables.

### 7. **GitHub Repository**:
- Uploaded the project to **GitHub**. You can access the repository [here](https://github.com/Rahimdzx/-AI-ML-team-position-at-DocuSketch.git).

## Screencast

Recorded a screencast demonstrating the following:
- Running the application in **IntelliJ IDEA**.
- Using unit tests to validate functionality.
- Using the profiler to assess performance.
- Using the debugger for step-through debugging and variable evaluation.

You can view the screencast [here](https://drive.google.com/file/d/1o3zxfc6LkO1hmwRY7Esfr3mjq9mWHqH4/view?t=3).
