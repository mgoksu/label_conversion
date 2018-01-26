

if [ $# -eq 0 ]
then
    echo "usage ./state_to_phone.sh state_dir phone_dir"
fi

mkdir "$2"

for st_f in $1/*.lab
do
    python3 ./state_to_phone.py < $st_f > "$2/${st_f##*/}"
done
