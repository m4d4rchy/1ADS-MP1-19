touch README.md
git init
git add .
git commit -m "$1"
git remote add origin git@github.com:gameeklab/$2.git
git push -u origin master

