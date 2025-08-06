#!/usr/bin/env python3
"""
Test script for Riverside BLS OES scrapers
"""

import sys
import os

# Add the scrapers directory to the path (go up one level from test/ to find scrapers/)
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'scrapers'))

def test_2024_scraper():
    """Test the 2024 Riverside scraper"""
    print("🧪 Testing 2024 Riverside scraper...")
    
    try:
        from selenium_oes_scraper import SeleniumBLSOESScraper
        
        scraper = SeleniumBLSOESScraper()
        print(f"✅ 2024 scraper initialized")
        print(f"📍 Area code: {scraper.riverside_area_code}")
        print(f"🌐 Base URL: {scraper.base_url}")
        print(f"📁 Data directory: {scraper.data_dir}")
        
        return True
        
    except Exception as e:
        print(f"❌ Error testing 2024 scraper: {e}")
        return False

def test_2019_scraper():
    """Test the 2019 Riverside scraper"""
    print("🧪 Testing 2019 Riverside scraper...")
    
    try:
        from selenium_oes_scraper_2019 import SeleniumBLSOESScraper2019
        
        scraper = SeleniumBLSOESScraper2019()
        print(f"✅ 2019 scraper initialized")
        print(f"🌐 URL: {scraper.url}")
        print(f"📁 Data directory: {scraper.data_dir}")
        
        return True
        
    except Exception as e:
        print(f"❌ Error testing 2019 scraper: {e}")
        return False

def main():
    """Run tests for both scrapers"""
    print("🚀 Testing Riverside BLS OES Scrapers")
    print("=" * 50)
    
    # Test 2024 scraper
    success_2024 = test_2024_scraper()
    print()
    
    # Test 2019 scraper
    success_2019 = test_2019_scraper()
    print()
    
    # Summary
    print("📊 Test Results:")
    print(f"   2024 Scraper: {'✅ PASS' if success_2024 else '❌ FAIL'}")
    print(f"   2019 Scraper: {'✅ PASS' if success_2019 else '❌ FAIL'}")
    
    if success_2024 and success_2019:
        print("\n🎉 All tests passed! Scrapers are ready to use.")
        print("\n📝 To run the scrapers:")
        print("   python scrapers/selenium_oes_scraper.py")
        print("   python scrapers/selenium_oes_scraper_2019.py")
    else:
        print("\n⚠️  Some tests failed. Please check the configuration.")

if __name__ == "__main__":
    main() 