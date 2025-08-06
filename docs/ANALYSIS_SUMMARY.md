# Riverside BLS OES Analysis Summary

## 🎯 **Project Overview**
Successfully modified and ran BLS OES scrapers and analysis tools for Riverside-San Bernardino-Ontario, CA MSA data.

## 📊 **Data Extracted**

### **2024 Riverside Data**
- **Source**: https://data.bls.gov/oes/#/area/0040140
- **File**: `oes_data/riverside_oes_selenium_data.csv`
- **Records**: 1,409 occupations
- **Size**: 360KB
- **Key Metrics**: Employment, wages, location quotients

### **2019 Riverside Data**
- **Source**: https://www.bls.gov/oes/2019/may/oes_40140.htm
- **File**: `oes_data_2019/riverside_oes_2019_selenium_data.csv`
- **Records**: 656 occupations
- **Size**: 67KB
- **Key Metrics**: Employment, wages, location quotients

## 🔧 **Files Modified**

### **Scrapers** (Modified from Los Angeles to Riverside)
1. `scrapers/selenium_oes_scraper.py` - 2024 Riverside scraper
2. `scrapers/selenium_oes_scraper_2019.py` - 2019 Riverside scraper

### **Analysis Tools** (Modified from Los Angeles to Riverside)
1. `utils/analyze_2019_data.py` - 2019 data analysis
2. `utils/process_extracted_data.py` - 2024 data processing
3. `utils/compare_2019_2024.py` - Comparison analysis

## 📁 **Generated Analysis Files**

### **2024 Analysis Results**
- `oes_data/riverside_oes_cleaned_data.csv` - Cleaned 2024 data
- `oes_data/riverside_oes_analysis_results.csv` - Statistical analysis
- `oes_data/riverside_location_quotient_report.csv` - Ranked LQ report

### **2019 Analysis Results**
- `oes_data_2019/riverside_oes_2019_analysis_results.csv` - Statistical analysis
- `oes_data_2019/riverside_location_quotient_2019_report.csv` - Ranked LQ report

## 🏆 **Key Findings**

### **2024 Riverside Top Occupations (High LQ)**
1. **Plasterers and Stucco Masons** - LQ: 5.800
2. **Gambling Change Persons and Booth Cashiers** - LQ: 5.050
3. **Material Moving Workers, All Other** - LQ: 4.890
4. **Tapers** - LQ: 4.640
5. **Helpers--Painters, Paperhangers, Plasterers** - LQ: 4.370

### **2019 Riverside Top Occupations (High LQ)**
1. **Tapers** - LQ: 5.780
2. **Marriage and Family Therapists** - LQ: 5.700
3. **Solar Photovoltaic Installers** - LQ: 4.350
4. **First-Line Supervisors of Gambling Services** - LQ: 4.180
5. **Drywall and Ceiling Tile Installers** - LQ: 4.000

### **Location Quotient Distribution (2024)**
- **Very High Concentration (LQ > 2.0)**: 45 occupations
- **High Concentration (LQ > 1.5)**: 84 occupations
- **Above Average (LQ > 1.0)**: 228 occupations
- **Below Average (LQ ≤ 1.0)**: 445 occupations

### **Location Quotient Distribution (2019)**
- **Very High Concentration (LQ > 2.0)**: 32 occupations
- **High Concentration (LQ > 1.5)**: 71 occupations
- **Above Average (LQ > 1.0)**: 202 occupations
- **Below Average (LQ ≤ 1.0)**: 453 occupations

## 🔄 **Changes Made**

### **Area Code Updates**
- Changed from Los Angeles (`0031080`) to Riverside (`0040140`)
- Updated URLs to point to Riverside BLS pages

### **File Path Updates**
- Updated all file paths to use Riverside data files
- Changed output file names to reflect Riverside data

### **Data Validation Updates**
- Modified validation logic to work with Riverside data structure
- Updated occupation matching for comparison analysis

## 📈 **Statistical Summary**

### **2024 Riverside Statistics**
- **Mean LQ**: 0.968
- **Median LQ**: 0.800
- **Min LQ**: 0.050
- **Max LQ**: 5.800
- **Standard Deviation**: 0.698

### **2019 Riverside Statistics**
- **Mean LQ**: 0.955
- **Median LQ**: 0.830
- **Min LQ**: 0.090
- **Max LQ**: 5.780
- **Standard Deviation**: 0.665

## 🎯 **Industry Insights**

Riverside shows high concentration in:
- **Construction trades** (plasterers, tapers, drywall installers)
- **Gambling services** (casino workers)
- **Material handling** (truck operators, movers)
- **Solar installation** (photovoltaic installers)

Low concentration in:
- **Financial services** (examiners, actuaries)
- **Aerospace engineering**
- **Postsecondary education**
- **Information security**

## ✅ **Status**
All scrapers and analysis tools successfully modified and tested. Riverside OES data extracted and analyzed for both 2019 and 2024 periods. 