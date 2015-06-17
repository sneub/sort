#!/usr/bin/env perl
sub randomstr {
    my $size = shift;
    my @chars = ("A".."Z", "a".."z");
    my $string;
    $string .= $chars[rand @chars] for 1..$size;
    return $string;
}
print randomstr($ARGV[0]);
