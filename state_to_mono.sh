

if [ $# -eq 0 ]
then
    echo "usage ./state_to_mono.sh state_dir mono_dir"
    exit
fi

mkdir "$2"

for st_f in $1/*.lab
do
    python3 ./state_to_mono.py < $st_f > "$2/${st_f##*/}"
done
