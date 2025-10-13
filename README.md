# ☀️ Predicting Solar Energy Efficiency of Buildings in Lagos

## 🌍 Project Overview
This project applies machine learning to estimate how efficiently buildings in Lagos can generate solar energy from their rooftops.  
Using the **Lagos Rooftop Solar Potential dataset**, we analyze the physical characteristics of more than 200,000 buildings—such as roof surface area, tilt, height, and potential installable capacity—to predict their **annual solar energy output**.

The goal is to provide a **data-driven tool** that helps homeowners, builders, and urban planners identify which buildings are best suited for solar installation and how much power they can realistically produce.  
This supports Nigeria’s broader sustainability efforts by promoting clean, renewable energy adoption.

---

## 🎯 Objectives
- Clean and preprocess the Lagos Rooftop Solar Potential dataset for analysis.  
- Explore rooftop characteristics to uncover energy-related trends.  
- Engineer additional features such as **area utilization ratio**, **energy density**, **capacity density**, and **system efficiency**.  
- Build **regression models** to predict annual energy potential (kWh/year).  
- Develop **classification models** to categorize buildings as *Low*, *Medium*, or *High* efficiency.  
- Evaluate model performance using **RMSE**, **MAE**, **Accuracy**, **Precision**, **Recall**, and **F1-Score**.  
- Deploy an interactive **Streamlit web app** that allows users to input building parameters and instantly see energy efficiency predictions.

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
It includes attributes such as:
- Surface Area  
- Potential Installable Area  
- Peak Installable Capacity  
- Capacity Factor  
- Energy Potential per Year  
- Building Height  
- Roof Tilt  
- Building Type  

---

## 🧩 Feature Engineering Highlights
To enrich the dataset and improve model accuracy, several new columns were derived:
- **Area Utilization Ratio** → Ratio of usable to total roof area.  
- **Energy Density** → Energy potential per square meter of usable area.  
- **Capacity Density** → Installed capacity per square meter.  
- **System Efficiency** → Actual energy output vs. theoretical maximum (based on capacity × 8760 hours).  
These engineered features help capture building efficiency patterns more effectively for model training.

---

## 🤖 Modeling Approach
### Regression Models
Used to predict the **continuous variable**: annual energy potential (kWh/year).
- Linear Regression (baseline)
- Random Forest Regressor
- Gradient Boosting (XGBoost / LightGBM)

### Classification Models
Used to label buildings as *Low*, *Medium*, or *High* efficiency based on annual potential.
- Logistic Regression
- Random Forest Classifier
- Gradient Boosting Classifier

Each model is compared using cross-validation and evaluated with:
- **Regression:** RMSE, MAE, R²  
- **Classification:** Accuracy, Precision, Recall, F1-Score  

---

## 🧠 Insights & Expected Outcomes
- A robust predictive model for solar energy efficiency of Lagos buildings.  
- An understanding of which physical rooftop features most influence energy generation.  
- A user-friendly, web-based application that makes solar feasibility assessment accessible to the public.  
- Actionable data that supports sustainable development and renewable energy adoption in Nigeria.

---

## 🧭 Repository Structure
```
📁 doc/
 └── Project_Proposal_Predicting_Solar_Efficiency.pdf
📁 data/
 └── lagos_rooftop_solar_potential.csv
📁 notebooks/
 └── data_preparation.ipynb
📁 src/
 └── model_training.py  (future addition)
📄 README.md
```


---

## 👥 Contributors
- **Team Lead:** Chitom Ernesto Uzokwe  
- **Team Members:** Precious Ita, Joy Eromosele, Toluwani Abiodun, Precious Odutola  
- **Program:** AI Saturdays Lagos – Machine Learning Cohort

---

## 📜 Acknowledgement
This project was developed as part of the **AI Saturdays Lagos Machine Learning Program**, focusing on applying data science to real-world sustainability problems.  
Special thanks to mentors and cohort peers for their guidance and contributions.

---

## 🔗 References
1. [Lagos State Rooftop Solar Potential Mapping Dataset](https://energydata.info/dataset/lagos-state-rooftop-solar-potential-mapping)  
2. [Global Solar Atlas](https://globalsolaratlas.info/map)  
3. [AI Saturdays Lagos – Machine Learning for Social Good](https://aisaturdayslagos.com)
