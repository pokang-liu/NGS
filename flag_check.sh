awk 'BEGIN {bigflag=0;}{print $2}
{
if($2>256){
    bigflag++;}
}END{printf "bigflag:%d\n",bigflag ;}'| sort | uniq -c | sort -n -r -k 2 | awk '{printf"%s\t%s\n",$2,$1}'
