# Test Directory

This directory contains test scripts for the Riverside BLS OES scrapers.

## Files

- `test_riverside_scrapers.py` - Test script to verify scraper configuration and functionality

## Usage

Run the test script from the project root:

```bash
python test/test_riverside_scrapers.py
```

This will:
- Test the 2024 Riverside scraper configuration
- Test the 2019 Riverside scraper configuration
- Verify that both scrapers can be initialized properly
- Display test results and next steps

## Test Coverage

The test script verifies:
- ✅ Scraper initialization
- ✅ Configuration parameters (area codes, URLs, data directories)
- ✅ Import functionality
- ✅ Basic setup validation

## Running Tests

Tests should be run before using the scrapers to ensure everything is properly configured:

1. **From project root**: `python test/test_riverside_scrapers.py`
2. **Check output**: Verify both scrapers show "✅ PASS"
3. **Proceed with scraping**: If tests pass, the scrapers are ready to use

## Troubleshooting

If tests fail:
1. Check that Chrome and ChromeDriver are installed
2. Verify Python dependencies are installed (`selenium`, `pandas`)
3. Ensure the project structure is correct
4. Check file permissions and paths 