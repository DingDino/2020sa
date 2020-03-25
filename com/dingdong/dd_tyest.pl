#my $eseAuthKeyFile  = "/EMC/backend/CEM/ese/auth-key.txt";
use strict;
use warnings;
my $eseAuthKeyFile  = "report.txt";

# Generate auth-key.txt
$auth_key;
#for (0..7) { $auth_key .= chr( int(rand(25) + 65) ); }
my @chars = ("A".."Z", "a".."z", 0..9);
$auth_key .= $chars[rand @chars] for 0..7;
#/EMC/backend/CEM/ese/auth-key.txt
open(my $fh, '>', $eseAuthKeyFile) or die "Could not open file '$eseAuthKeyFile' $!";
#open(my $fh, '>', $auth_key_fn) or startHandler "Could not open file '$filename' $!";
print $fh $auth_key;
close $fh;
