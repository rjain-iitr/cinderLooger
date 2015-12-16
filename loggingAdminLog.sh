function usage {
echo "see usage"	
	
	
	
}

#       usage
#       exit 1

datestr=`date +'%Y%m%d'`
filename="$1$datestr"
adminid=$2
tentantid=$3
echo $datestr
./parser.py $filename $adminid $tentantid

