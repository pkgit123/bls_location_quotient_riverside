# Riverside BLS OES Location Quotient Analysis

[![Python](https://img.shields.io/badge/Python-3.7+-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![GitHub](https://img.shields.io/badge/GitHub-Repository-blue.svg)](https://github.com/pkgit123/bls_location_quotient_riverside)

This project contains Selenium-based web scrapers for extracting Occupational Employment and Wage Statistics (OES) data for the Riverside-San Bernardino-Ontario, CA Metropolitan Statistical Area (MSA).

## Overview

The scrapers are designed to extract location quotient data from the Bureau of Labor Statistics (BLS) OES website for Riverside County. Location quotients help identify industries and occupations that are more concentrated in Riverside compared to the national average.

## Project Structure

### Core Files
- `scrapers/selenium_oes_scraper.py` - Scraper for current (2024) Riverside OES data
- `scrapers/selenium_oes_scraper_2019.py` - Scraper for 2019 Riverside OES data
- `test/test_riverside_scrapers.py` - Test script to verify scraper configuration

### Analysis Tools
- `utils/analyze_2019_data.py` - 2019 data analysis
- `utils/process_extracted_data.py` - 2024 data processing
- `utils/compare_2019_2024.py` - Comparison analysis

### Documentation
- `docs/methodology.md` - Comprehensive methodology and technical details
- `docs/lq_changes_analysis.md` - Analysis of location quotient changes (2019-2024)
- `docs/ANALYSIS_SUMMARY.md` - Project summary and key findings

## URLs

- **2024 Data**: https://data.bls.gov/oes/#/area/0040140
- **2019 Data**: https://www.bls.gov/oes/2019/may/oes_40140.htm

## Area Code

- **Riverside-San Bernardino-Ontario, CA MSA**: `0040140`

## Requirements

- Python 3.7+
- Chrome browser
- ChromeDriver
- Required Python packages (see requirements.txt)

## Installation

1. Install required packages:
```bash
pip install selenium pandas
```

2. Install ChromeDriver:
   - Download from: https://chromedriver.chromium.org/
   - Add to your PATH or place in the project directory

## Usage

### Test the Scrapers

First, test that the scrapers are properly configured:

```bash
python test/test_riverside_scrapers.py
```

### Run the 2024 Scraper

```bash
python scrapers/selenium_oes_scraper.py
```

This will:
- Navigate to the 2024 Riverside OES page
- Extract location quotient data
- Save results to `oes_data/riverside_oes_selenium_data.csv`

### Run the 2019 Scraper

```bash
python scrapers/selenium_oes_scraper_2019.py
```

This will:
- Navigate to the 2019 Riverside OES page
- Extract location quotient data
- Save results to `oes_data_2019/riverside_oes_2019_selenium_data.csv`

## Output Files

The scrapers generate several output files for debugging and analysis:

- **CSV Data**: Main extracted data in CSV format
- **HTML Source**: Page source for debugging
- **Screenshots**: Visual capture of the scraped page

## Key Features

- **Headless Mode**: Runs Chrome in background
- **Error Handling**: Robust error handling and fallback methods
- **Debugging**: Saves page source and screenshots
- **Data Validation**: Checks for Riverside-specific data
- **Multiple Extraction Methods**: Falls back to alternative extraction if primary method fails

## Data Structure

The scrapers extract:
- Occupation titles
- Employment numbers
- Wage data
- Location quotients (LQ)
- Other relevant OES metrics

## Troubleshooting

1. **ChromeDriver Issues**: Ensure ChromeDriver is installed and compatible with your Chrome version
2. **No Data Found**: Check if the BLS website structure has changed
3. **Timeout Errors**: Increase timeout values in the scraper code
4. **Permission Errors**: Ensure write permissions for the data directories

## Modifications Made

The scrapers were modified from the original Los Angeles scrapers:

- Changed area code from `0031080` (Los Angeles) to `0040140` (Riverside)
- Updated URLs to point to Riverside data
- Modified data validation to look for Riverside indicators
- Updated output file names to reflect Riverside data
- Changed all references from "Los Angeles" to "Riverside"

## Documentation

For detailed information about this project, see the documentation in the `docs/` folder:

- **[Methodology](docs/methodology.md)** - Comprehensive methodology, data sources, and technical implementation details
- **[Location Quotient Changes Analysis](docs/lq_changes_analysis.md)** - Detailed analysis of occupational concentration changes between 2019-2024
- **[Analysis Summary](docs/ANALYSIS_SUMMARY.md)** - Project overview and key findings

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request. For major changes, please open an issue first to discuss what you would like to change.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

This project is for educational and research purposes. Please respect the BLS website's terms of service when using these scrapers.

## Acknowledgments

- [Bureau of Labor Statistics (BLS)](https://www.bls.gov/) for providing the OES data
- [Selenium](https://selenium-python.readthedocs.io/) for web automation capabilities
- [Pandas](https://pandas.pydata.org/) for data manipulation and analysis 