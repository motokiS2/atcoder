<?php
$input = fgets(STDIN);
$q = substr_count($input,"?");
$input_length = strlen($input);
$count = 0;
$splitInput = str_split($input);
$qpos = array_keys($splitInput,"?");
// var_dump($splitInput);
// var_dump($input_length);


