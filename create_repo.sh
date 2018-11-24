echo "# $1" >> README.md
git init
git add README.md
git commit -m "first commit"
git remote set-url origin git@github.com:gameeklab/$1.git
git push -u origin master
