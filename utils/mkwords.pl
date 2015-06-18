#!/usr/bin/env perl

my $size = $ARGV[0];
my $tracker = 0;
my $width   = 0;

open (F, "<", "wordlist.txt");
my @words = <F>;
close (F);
while ( $tracker < $size ) {
    my $word =  $words[rand @words];
    chomp($word);
    $tracker += length($word);
    $width   += length($word);
    if ($width >= 80) {
        $width = 0;
        print "\n";
    }
    print "$word ";
}
