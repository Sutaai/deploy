sudo apt install -y glob 

FILES="files="
for file in $(find . -name .env); do echo "FILES+=$file "; done
echo $FILES >> $GITHUB_OUTPUT
