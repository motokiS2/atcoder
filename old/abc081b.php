<?php
$num = intval(trim(fgets(STDIN)));
$original = explode(" ",fgets(STDIN)); //explodeで半角スペースごとに分けるため、trimを使用すると半角スペースが消えてしまう
$min = array();
for ($i=0; $i<$num; $i++){
    $min[$i] = 0;
    while($original[$i] %2 == 0){
        $min[$i]++;
        $original[$i] /= 2;
    }
}

echo min($min);
