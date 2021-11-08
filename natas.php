<?php

function natas8()
{
    $encodedSecret = "3d3d516343746d4d6d6c315669563362";

    echo base64_decode(strrev(hex2bin($encodedSecret)));
}

function natas11()
{
    $defaultdata = array( "showpassword" => "no", "bgcolor"=> "#ffffff");
    
    // A ^ B = C ---> A ^ C = B
    function xor_encrypt($in, $key)
    {
        $text = $in;
        $outText = '';
        for ($i=0; $i < strlen($text); $i++) {
            $outText .= $text[$i] ^ $key[$i % strlen($key)];
        }
        return $outText;
    }

    //x -> Json_encode -> xor_encrypt -> base64_encode -> y
    //so we need to go back step by step
    //to be able to figure out the key for encryption
    //we can get the encoded version of $defaultdata from the cookie

    $defaultdata_cookie = 'ClVLIh4ASCsCBE8lAxMacFMZV2hdVVotEhhUJQNVAmhSEV4sFxFeaAw';
    $decoded64 = base64_decode($defaultdata_cookie);

    //$decoded64 is a very strange value
    // but let's try to treat it as hex value
    //if we want to see it in a more clear form,
    //but it's not an important step at all

    $hexvalue = bin2hex($decoded64);
    //and it succeded, so let's complete the deocde process


    $xor_dec = xor_encrypt(json_encode($defaultdata), $decoded64);
    //and we got our key repeated multiple times { qw8J }

    //now it's time to repeat the process but with our good data
    $gooddata =  array( "showpassword" => "yes", "bgcolor"=> "#ffffff");
    $goodkey = 'qw8J';
    $encoded_gooddata = base64_encode(xor_encrypt(json_encode($gooddata), $goodkey));

    echo $encoded_gooddata .'\n';
}

natas11();

?>

