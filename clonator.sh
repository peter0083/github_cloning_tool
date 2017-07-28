#!/bin/sh

# reference: https://gist.github.com/benhurott/a85be9e534622d9e4e6acb4765bd4b38
# reference2: https://www.safaribooksonline.com/library/view/building-tools-with/9781491933497/ch04.html
# Clone multiple repositories.
# dependency: brew install jq

chmod +x ./clonator.sh

echo "=== CLONATOR ==="

# get ssh_url info
curl -i https://github.ubc.ca/api/v3/orgs/ubc-mds-2016/repos?access_token=***

array=( "https://github.ubc.ca/ubc-mds-2016/test.git",
"https://github.ubc.ca/ubc-mds-2016/test2.git")

for element in ${array[@]}
do
    echo "cloning $element"
    git clone $element
done

echo "=== DONE ==="
