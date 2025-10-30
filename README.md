# ☀️ Predicting Solar Energy Efficiency Levels of Buildings in Lagos

## 🌍 Project Overview
This project applies **machine learning** to estimate how efficiently buildings in Lagos can generate solar energy from their rooftops.  
Using the **Lagos Rooftop Solar Potential dataset**, we analyze the physical characteristics of more than 200,000 buildings—such as roof surface area, tilt, height, and potential installable capacity—to predict their **energy efficiency categories** (Low, Medium, High).

The goal is to provide a **data-driven tool** that helps homeowners, builders, and urban planners identify which buildings are best suited for solar installation.  
This supports Nigeria’s broader sustainability efforts by promoting clean, renewable energy adoption.

---

## 🎯 Objectives
- Clean and preprocess the Lagos Rooftop Solar Potential dataset for analysis.  
- Explore rooftop characteristics to uncover energy-related trends.  
- Engineer additional features such as **area utilization ratio**, **energy density**, **capacity density**, and **system efficiency**.  
- Develop **classification models** to categorize buildings as *Low*, *Medium*, or *High* efficiency.  
- Evaluate model performance using **Accuracy, Precision, Recall, and F1-Score**.  
- Deploy an interactive **Streamlit web app** that allows users to input building parameters and instantly see energy efficiency predictions.

> **Note:** Regression models were initially considered for predicting continuous annual energy potential (kWh/year), but were discarded because the dataset exhibited extreme correlations and non-linear relationships after feature engineering, which made regression predictions unreliable. Classification models, especially Random Forest, proved more suitable for capturing discrete efficiency categories.

---

## ⚙️ Tools & Libraries
- **Python**
- **Pandas**, **NumPy**
- **Scikit-learn**
- **Matplotlib**, **Seaborn**
- **Streamlit** (for deployment)
- **Jupyter / Google Colab** (for experimentation)

---

## 📊 Dataset
**Source:** [Lagos State Rooftop Solar Potential Mapping Dataset](https://energydata.info/dataset/lagos-state-rooftop-solar-potential-mapping)  
This open dataset provides detailed information on rooftop geometry and solar potential for buildings across Lagos State, Nigeria.  
Both the original and preprocessed datasets are included for reproducibility and transparency.  

**Key attributes:**
- Surface Area  
- Potential Installable Area  
- Peak Installable Capacity  
- Capacity Factor  
- Energy Potential per Year  
- Building Height  
- Roof Tilt  
- Building Type  

Two datasets are provided in the `data/` folder:

- `lagos_rooftop_solar_potential.csv` – Original raw dataset.  
- `lagos_prepared_with_features.zip` – Cleaned and feature-engineered dataset used for modeling.

---

## 🧩 Feature Engineering Highlights
- **Area Utilization Ratio:** Ratio of usable to total roof area.  
- **Energy Density:** Energy potential per square meter of usable area.  
- **Capacity Density:** Installed capacity per square meter.  
- **System Efficiency:** Actual energy output vs. theoretical maximum (based on capacity × 8760 hours).  

These engineered features help the model **capture building efficiency patterns** more effectively for classification.

---

## 🤖 Modeling Approach
### Classification Models
Used to label buildings as *Low*, *Medium*, or *High* efficiency based on annual potential:  
- Logistic Regression (baseline)  
- Random Forest Classifier (selected)  
- Gradient Boosting Classifier  

**Model evaluation:**  
- Cross-validation and metrics: Accuracy, Precision, Recall, F1-Score  
- Random Forest achieved the best performance after hyperparameter tuning:  
  - `n_estimators=200, min_samples_split=5, min_samples_leaf=2, max_features='sqrt', max_depth=None`  
  - Test Accuracy ≈ 78.9%  

---

## 🧠 Insights & Expected Outcomes
- A robust predictive model for **solar energy efficiency** of Lagos buildings.  
- Insights into which physical rooftop features most influence energy generation.  
- A user-friendly, web-based application that makes solar feasibility assessment accessible to the public.  
- Actionable data supporting sustainable development and renewable energy adoption in Nigeria.

---

## 🧭 Repository Structure
📁 data/
  - lagos_rooftop_solar_potential.csv
  - lagos_prepared_with_features.zip

📁 doc/
  - Project_Proposal_Predicting_Solar_Efficiency.pdf
  - Energy_Efficiency_Project_Report.pdf
  - Energy_Efficiency_Project_Slides.pdf

📁 notebooks/
  - data_preparation.ipynb

📁 src/
  - model_training.py  # Random Forest classification

📄 README.md

## 👥 Contributors
- **Team Lead:** Chitom Uzokwe  
- **Team Members:** Precious Ita, Joy Eromosele, Toluwani Abiodun, Precious Odutola  
- **Program:** AI Saturdays Lagos – Machine Learning Cohort

---

## 📜 Acknowledgment
This project was developed as part of the **AI Saturdays Lagos Machine Learning Program**, focusing on applying data science to real-world sustainability problems.  
Special thanks to mentors and cohort peers for their guidance and contributions

---

## 🔗 References
1. [Lagos State Rooftop Solar Potential Mapping Dataset](https://energydata.info/dataset/lagos-state-rooftop-solar-potential-mapping)  
2. Global Solar Atlas – globalsolaratlas.info/map  
3. AI Saturdays Lagos – Machine Learning
