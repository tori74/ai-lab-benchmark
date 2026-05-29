"""Render HTML files in /tmp/ai-lab-post/*.html to PNG at /tmp/ai-lab-post/*.png"""
import sys, os
from playwright.sync_api import sync_playwright

html_file = sys.argv[1]
png_file = sys.argv[2]
width = int(sys.argv[3]) if len(sys.argv) > 3 else 1280
height = int(sys.argv[4]) if len(sys.argv) > 4 else 720

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page(viewport={"width": width, "height": height}, device_scale_factor=2)
    page.goto(f"file://{os.path.abspath(html_file)}")
    page.wait_for_timeout(800)
    page.screenshot(path=png_file, full_page=False, omit_background=False)
    browser.close()
print(f"saved: {png_file}")
