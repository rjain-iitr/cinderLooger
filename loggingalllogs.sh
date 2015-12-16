function usage {
echo "see usage"	
}
IFS=$'\r\n' GLOBIGNORE='*' ; XYZ=($(cat $1))
echo ${XYZ[@]}
datestr=`date +'%Y%m%d'`
filename="$1$datestr"
./parser.py $filename ${XYZ[@]}
