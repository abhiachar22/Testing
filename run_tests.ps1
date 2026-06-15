# Run tests: installs deps, browsers, and runs pytest with HTML report
python -m pip install -r requirements.txt
python -m playwright install
pytest -v --html=reports/report.html --self-contained-html
