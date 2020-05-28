<?php
$input = fgets(STDIN);
$input = str_replace("eraser","",$input);
$input = str_replace("erase","",$input);
$input = str_replace("dreamer","",$input);
$input = str_replace("dream","",$input);
if (strlen($input) == 0) {
    echo "YES";
} else {
    echo "NO";
}
