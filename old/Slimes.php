<?php
fscanf(STDIN, "%d", $n);
fscanf(STDIN, "%s", $s);
$fusion = 0;
for ($i = 0; $i < $n-1; $i++) {
    if($s[$i] === $s[$i+1]) {
        $fusion++;
    }
}

echo $n - $fusion;