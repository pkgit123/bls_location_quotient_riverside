# Riverside BLS OES Location Quotient Analysis Methodology

## Overview

This document describes the methodology used to analyze Occupational Employment and Wage Statistics (OES) location quotient data for the Riverside-San Bernardino-Ontario, CA Metropolitan Statistical Area (MSA). The analysis compares occupational concentration patterns between 2019 and 2024 to identify industries and occupations that have experienced significant changes in their relative concentration within the Riverside economy.

## Data Sources

### Primary Data Sources
- **Bureau of Labor Statistics (BLS) OES Data**: Official employment and wage statistics
- **2024 Data**: https://data.bls.gov/oes/#/area/0040140 (Riverside MSA)
- **2019 Data**: https://www.bls.gov/oes/2019/may/oes_40140.htm (Riverside MSA)

### Geographic Coverage
- **MSA Code**: 0040140 (Riverside-San Bernardino-Ontario, CA)
- **Coverage Period**: 2019-2024 (5-year comparison)
- **Data Frequency**: Annual OES surveys

## Location Quotient (LQ) Methodology

### Definition
Location Quotient (LQ) measures the relative concentration of an occupation in a specific geographic area compared to the national average. It is calculated as:

```
LQ = (Local Employment in Occupation / Total Local Employment) / 
     (National Employment in Occupation / Total National Employment)
```

### Interpretation
- **LQ > 1.0**: Occupation is more concentrated than national average
- **LQ = 1.0**: Occupation concentration matches national average
- **LQ < 1.0**: Occupation is less concentrated than national average

### Categories Used
- **Very High Concentration**: LQ > 2.0
- **High Concentration**: 1.5 < LQ ≤ 2.0
- **Above Average**: 1.0 < LQ ≤ 1.5
- **Below Average**: 0.5 < LQ ≤ 1.0
- **Low Concentration**: LQ ≤ 0.5

## Data Collection Methodology

### Web Scraping Approach
1. **Selenium-based Scrapers**: Automated data extraction from BLS website
2. **Headless Browser**: Chrome webdriver with appropriate options
3. **Error Handling**: Robust fallback mechanisms for data extraction
4. **Data Validation**: Multiple extraction methods to ensure completeness

### Data Processing Pipeline
1. **Raw Data Extraction**: HTML table parsing and conversion to CSV
2. **Data Cleaning**: Removal of header rows, empty entries, and formatting issues
3. **Column Standardization**: Consistent naming and data type conversion
4. **Quality Checks**: Validation of location quotient values and employment data

## Analysis Methodology

### Statistical Analysis
1. **Descriptive Statistics**: Mean, median, standard deviation of location quotients
2. **Distribution Analysis**: Categorization by concentration levels
3. **Ranking Analysis**: Top and bottom occupations by LQ values
4. **Change Analysis**: Comparison of 2019 vs 2024 LQ values

### Comparison Methodology
1. **Occupation Matching**: Alignment of occupation titles between years
2. **LQ Change Calculation**: Absolute and percentage changes
3. **Significance Testing**: Identification of meaningful changes
4. **Trend Analysis**: Patterns in occupational concentration shifts

## Data Quality Assurance

### Validation Steps
1. **Source Verification**: Confirmation of data from official BLS sources
2. **Completeness Checks**: Verification of all required fields
3. **Consistency Validation**: Cross-checking of employment and LQ data
4. **Outlier Detection**: Identification and review of extreme values

### Quality Metrics
- **Data Completeness**: >95% of expected occupations captured
- **Accuracy**: Cross-verification with BLS published statistics
- **Timeliness**: Use of most recent available data
- **Consistency**: Standardized methodology across time periods

## Technical Implementation

### Technology Stack
- **Python 3.7+**: Primary programming language
- **Selenium**: Web scraping and automation
- **Pandas**: Data manipulation and analysis
- **Chrome WebDriver**: Browser automation

### File Structure
```
bls_location_quotient_riverside/
├── scrapers/           # Data extraction scripts
├── utils/             # Analysis and processing tools
├── oes_data/          # 2024 data and analysis results
├── oes_data_2019/     # 2019 data and analysis results
├── docs/              # Documentation
└── notebooks/         # Jupyter notebooks for exploration
```

### Data Flow
1. **Extraction**: Web scraping → Raw CSV files
2. **Processing**: Data cleaning → Standardized datasets
3. **Analysis**: Statistical analysis → Results files
4. **Documentation**: Results compilation → Reports and summaries

## Limitations and Considerations

### Data Limitations
1. **Survey-based Data**: OES data is survey-based, not census-based
2. **Sample Size**: Some occupations may have limited sample sizes
3. **Geographic Boundaries**: MSA boundaries may change over time
4. **Occupation Classification**: SOC codes may be updated between periods

### Methodological Considerations
1. **Economic Context**: Analysis should consider broader economic conditions
2. **Industry Trends**: National trends may influence local concentration
3. **Data Lag**: OES data reflects conditions from previous year
4. **Seasonal Effects**: Employment patterns may vary seasonally

## Ethical Considerations

### Data Usage
- **Public Data**: All data sources are publicly available
- **Respectful Scraping**: Appropriate delays and rate limiting
- **Attribution**: Proper citation of BLS as data source
- **Educational Purpose**: Analysis for research and educational use

### Privacy and Confidentiality
- **Aggregate Data**: Analysis uses aggregate statistics only
- **No Individual Data**: No personal or confidential information included
- **BLS Guidelines**: Compliance with BLS data usage policies

## Future Enhancements

### Potential Improvements
1. **Longitudinal Analysis**: Multi-year trend analysis
2. **Industry Grouping**: Analysis by industry sectors
3. **Geographic Comparison**: Comparison with other MSAs
4. **Economic Impact**: Correlation with economic indicators

### Technical Enhancements
1. **Automated Updates**: Scheduled data refresh
2. **Interactive Dashboards**: Web-based visualization tools
3. **API Integration**: Direct BLS API usage
4. **Machine Learning**: Predictive analysis capabilities

## Conclusion

This methodology provides a comprehensive framework for analyzing occupational concentration patterns in the Riverside MSA. The approach combines robust data collection, rigorous analysis, and transparent reporting to deliver meaningful insights into the region's economic structure and its evolution over time.

The analysis supports economic development planning, workforce development initiatives, and regional economic research by identifying both strengths and opportunities in the local labor market. 