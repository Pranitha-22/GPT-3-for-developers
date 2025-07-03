from gpt_utils import ask_gpt

def generate_eda_code(dataset_name='homeprices.csv'):
    prompt = f"Write Python code to perform exploratory data analysis using pandas on a dataset named '{dataset_name}'."
    return ask_gpt(prompt)

def generate_visualization_code(dataset_name='homeprices.csv'):
    """Generate Python code to visualize a dataset using matplotlib and seaborn."""
    prompt = f"Write Python code to visualize the dataset '{dataset_name}' using matplotlib and seaborn."
    return ask_gpt(prompt)

