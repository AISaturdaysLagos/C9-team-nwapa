import joblib
import gradio as gr
import pandas as pd
import numpy as np

# ======================================
# ✅ Load trained Random Forest model
# ======================================
model = joblib.load("final_random_forest_model.pkl")

# ======================================
# ✅ Define categorical options
# ======================================
building_types = [
    "single family residential", 
    "multi-family residential",
    "peri-urban settlement", 
    "commercial", 
    "industrial", 
    "public"
]

# ======================================
# ✅ Prediction function
# ======================================
def predict_energy_category(estimated_tilt, estimated_building_height,
                             estimated_capacity_factor, area_utilization_ratio,
                             capacity_density, assumed_building_type):

    # Build input dictionary
    input_dict = {
        "Estimated_tilt": [estimated_tilt],
        "Estimated_building_height": [estimated_building_height],
        "Estimated_capacity_factor": [estimated_capacity_factor],
        "Area_utilization_ratio": [area_utilization_ratio],
        "Capacity_density": [capacity_density],
    }

    # One-hot encode the building type (drop_first=True was used in training)
    for btype in building_types[1:]:
        col_name = f"Assumed_building_type_{btype}"
        input_dict[col_name] = [1 if assumed_building_type == btype else 0]

    # Create DataFrame for prediction
    input_df = pd.DataFrame(input_dict)

    # Predict
    pred = model.predict(input_df)[0]
    return f"Predicted Energy Category: {pred}"

# ======================================
# ✅ Gradio Interface
# ======================================
iface = gr.Interface(
    fn=predict_energy_category,
    inputs=[
        gr.Number(label="Estimated Tilt (°)"),
        gr.Number(label="Building Height (m)"),
        gr.Number(label="Estimated Capacity Factor"),
        gr.Number(label="Area Utilization Ratio"),
        gr.Number(label="Capacity Density"),
        gr.Dropdown(building_types, label="Assumed Building Type"),
    ],
    outputs=gr.Textbox(label="Prediction"),
    title="🏙️ Lagos Building Solar Energy Efficiency Predictor",
    description="Predicts whether a building in Lagos has Low, Medium, or High solar energy efficiency potential."
)

# ======================================
# ✅ Launch for Hugging Face Spaces
# ======================================
if __name__ == "__main__":
    iface.launch()
