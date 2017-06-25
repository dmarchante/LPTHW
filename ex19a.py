def orchestra (string, percussion, brass, wind):
    print "There are %d filled seats in the string section." % string
    print "Currently, there are %d percussionists." % percussion
    print "The brass section has %d musicians." % brass
    print "All of the %d wind seats are filled" % wind
    print "Now we can perform. \n"

print "1. Defined directly:"
orchestra(10, 4, 15, 12)

print "2. Defined through math:"
orchestra(10 + 12, 11 + 4, 8 + 9, 11 + 1)

print "3. Defined by script and math:"
string_violin = 5
string_cello = 3
string_bass = 2
percussion_snare = 4
percussion_bass = 2
brass_trumpet = 4
brass_trombone = 3
wind_sax = 4
wind_flute = 4
wind_clarinet = 4
wind_oboe = 2
total_string = string_violin + string_cello + string_bass
total_percussion = percussion_bass + percussion_snare
total_brass = brass_trombone + brass_trumpet
total_wind = wind_oboe + wind_sax + wind_clarinet + wind_flute

orchestra(string_violin + string_cello + string_bass, percussion_bass + percussion_snare, brass_trombone + brass_trumpet, wind_oboe + wind_sax + wind_flute + wind_clarinet)

print "4. Defined by total variables:"
orchestra(total_string, total_percussion, total_brass , total_wind)

print "5. Defined by total variables and math:"
orchestra(total_string - 4, total_percussion + 2, total_brass + 3, total_wind +0)

print "6. Define arguments individually:"
orchestra(string = 10, percussion = 5, brass = 3, wind= 2)

