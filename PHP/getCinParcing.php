<?php

$curl = curl_init();

curl_setopt_array($curl, array(
  CURLOPT_URL => "compdatasandbox.96.lt/getCinParcing.php",
  CURLOPT_RETURNTRANSFER => true,
  CURLOPT_ENCODING => "",
  CURLOPT_MAXREDIRS => 10,
  CURLOPT_TIMEOUT => 0,
  CURLOPT_FOLLOWLOCATION => true,
  CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
  CURLOPT_CUSTOMREQUEST => "POST",
  CURLOPT_POSTFIELDS => array('srn' => '123','cin' => 'U15549KA2012PTC067294','apiid' => 'mNp7yu3RthRs','apipass' => 'legaldesk@123'),
  CURLOPT_HTTPHEADER => array(
    "Content-Type: multipart/form-data; boundary=--------------------------776887819849444122523606"
  ),
));

$response = curl_exec($curl);

curl_close($curl);
echo $response;
