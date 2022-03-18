# Author: Jack Wagner
# Date: 3/18/2022
# LING 50.06

input="expressions.txt"

mkdir results

# loop over every binomial expression from the .txt file
while IFS= read -r line
do
    read -a strarr <<< "$line"
    ORDER1="${strarr[0]} and ${strarr[2]}"
    ORDER2="${strarr[2]} and ${strarr[0]}"

    # extract both alphabetical and reverse alphabetical word orders
    BOTH="${ORDER1},${ORDER2}"

    # pass into https://github.com/econpy/google-ngrams to generate CSV and plot
    python3 getngrams.py $BOTH -startYear=1900 -endYear=2000 -plot -caseInsensitive


done < "$input"

mkdir ratios

# open each csv and pass into calculateRatios.py to make a graph of the ratio changes by year
for FILE in results/*
do  
    if [ "${FILE: -4}" == ".csv" ]
    then
        python3 calculateRatios.py $FILE
    fi
done