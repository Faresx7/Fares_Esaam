# Data Cleaning Project

This project demonstrates my skills in **data cleaning and preprocessing** using Python and Pandas.  
The dataset used here is a sample (Customer Call List.xlsx).  

---

## Project Structure
- `data_cleaning.py` → main script for cleaning the dataset  
- `Customer Call List.xlsx` → sample dataset (dummy data for demonstration)  
- `output.xlsx` → cleaned dataset  

---

## Key Steps in Cleaning
1. **Handling Missing Values**  
   - Removed or replaced null/NaN values.  

2. **Standardizing Phone Numbers**  
   - Removed special characters (`-`, `/`, `|`) and kept only digits.  

3. **Fixing Customer Names**  
   - Removed unwanted symbols (`...`, `_`, `/`).  

4. **Normalizing Categorical Columns**  
   - Converted "Paying Customer" column to `Yes/No` format.  

5. **Splitting Columns**  
   - Used `str.split()` to separate combined fields.  

---

## Tech Stack
- Python 3  
- Pandas  
- Jupyter Notebook (optional)  
-openpyxl

