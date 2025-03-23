import unittest
import HtmlTestRunner
import os

# Cari semua test di dalam folder 'tests'
test_loader = unittest.TestLoader()
test_suite = test_loader.discover('tests')

# Path untuk menyimpan laporan HTML
report_dir = os.path.join(os.path.dirname(__file__), "reports")
if not os.path.exists(report_dir):
    os.makedirs(report_dir)

# Konfigurasi runner dengan HTMLTestRunner
runner = HtmlTestRunner.HTMLTestRunner(
    output=report_dir,
    report_name="TestReport",
    report_title="Automation Test Report",
    combine_reports=True
)

# Jalankan semua test
runner.run(test_suite)
