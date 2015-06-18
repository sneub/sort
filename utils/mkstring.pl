#!/usr/bin/env perl
sub randomstr {
    my $size = shift;
    my @chars = ("A".."Z", "a".."z");
    print $chars[rand @chars] for 1..$size;
}
randomstr($ARGV[0]);
