mkdir -p ~/.streamlit/

echo "\
[server]\n\
port = $PORT\n\
enableCORS = false\n\
headless = ture\n\
\n\
" > ~/.streamlit/confit.toml