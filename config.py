[run]
omit =
    venv/*   
    /vscode
    .vscode
    __pycache__/
    .pytest_cache/
    *.pyc
    .cache/

[report]
ignore_errors = True

[html]
directory = coverage_html_report