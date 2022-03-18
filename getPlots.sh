# Author: Jack Wagner
# Date: 3/18/2022
# LING 50.06

input="expressions.txt"

mkdir results

while IFS= read -r line
do
    read -a strarr <<< "$line"
    ORDER1="${strarr[0]} and ${strarr[2]}"
    ORDER2="${strarr[2]} and ${strarr[0]}"

    BOTH="${ORDER1},${ORDER2}"

    python3 getngrams.py $BOTH -startYear=1900 -endYear=2000 -plot -caseInsensitive


done < "$input"

mkdir ratios

for FILE in results/*
do  
    if [ "${FILE: -4}" == ".csv" ]
    then
        python3 calculateRatios.py $FILE
    fi
done