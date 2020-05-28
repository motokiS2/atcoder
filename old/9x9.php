<?php
fscanf(STDIN, "%d %d", $a, $b);

if ($a < 10 && $b < 10) {
    echo $a * $b;
} else {
    echo -1;
}