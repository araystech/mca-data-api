<?php

$curl = curl_init();

curl_setopt_array($curl, array(
  CURLOPT_URL => "compdatasandbox.96.lt/requestDownloadFile.php",
  CURLOPT_RETURNTRANSFER => true,
  CURLOPT_ENCODING => "",
  CURLOPT_MAXREDIRS => 10,
  CURLOPT_TIMEOUT => 0,
  CURLOPT_FOLLOWLOCATION => true,
  CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
  CURLOPT_CUSTOMREQUEST => "POST",
  CURLOPT_POSTFIELDS => array('cin' => '{cin}','apiid' => '{apiid}','apipass' => '{apipassword}'),
  CURLOPT_HTTPHEADER => array(
    "Content-Type: multipart/form-data; boundary=--------------------------735944852158856520680472"
  ),
));

$response = curl_exec($curl);

curl_close($curl);
echo $response;
