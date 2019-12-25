<?php

$curl = curl_init();

curl_setopt_array($curl, array(
  CURLOPT_URL => "compdatasandbox.96.lt/getDinByName.php",
  CURLOPT_RETURNTRANSFER => true,
  CURLOPT_ENCODING => "",
  CURLOPT_MAXREDIRS => 10,
  CURLOPT_TIMEOUT => 0,
  CURLOPT_FOLLOWLOCATION => true,
  CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
  CURLOPT_CUSTOMREQUEST => "POST",
  CURLOPT_POSTFIELDS => array('name' => 'sa','apiid' => 'mNp7yu3RthRs','apipass' => 'legaldesk@123'),
  CURLOPT_HTTPHEADER => array(
    "Content-Type: multipart/form-data; boundary=--------------------------520251517599687495464727"
  ),
));

$response = curl_exec($curl);

curl_close($curl);
echo $response;
