""" (Intermediate): Rail Fence Cipher Before the days of computerised
encryption, cryptography was done manually by hand. This means the methods of
encryption were usually much simpler as they had to be done reliably by a
person, possibly in wartime scenarios. One such method was the rail-fence
cipher[1] . This involved choosing a number (we'll choose 3) and writing our
message as a zig-zag with that height (in this case, 3 lines high.) Let's say
our message is REDDITCOMRDAILYPROGRAMMER. We would write our message like this:

R   I   M   I   R   A   R
 E D T O R A L P O R M E
  D   C   D   Y   G   M

See how it goes up and down? Now, to get the ciphertext, instead of reading with
the zigzag, just read along the lines instead. The top line has RIMIRAR, the
second line has EDTORALPORME and the last line has DCDYGM. Putting those
together gives you RIMIRAREDTORALPORMEDCDYGM, which is the ciphertext. You can
also decrypt (it would be pretty useless if you couldn't!). This involves
putting the zig-zag shape in beforehand and filling it in along the lines. So,
start with the zig-zag shape:

?   ?   ?   ?   ?   ?   ?
 ? ? ? ? ? ? ? ? ? ? ? ?
  ?   ?   ?   ?   ?   ?

The first line has 7 spaces, so take the first 7 characters (RIMIRAR)
and fill them in.

R   I   M   I   R   A   R
 ? ? ? ? ? ? ? ? ? ? ? ?
  ?   ?   ?   ?   ?   ?

The next line has 12 spaces, so take 12 more characters (EDTORALPORME)
and fill them in.

R   I   M   I   R   A   R
 E D T O R A L P O R M E
  ?   ?   ?   ?   ?   ?

Lastly the final line has 6 spaces so take the remaining 6 characters
(DCDYGM) and fill them in.

R   I   M   I   R   A   R
 E D T O R A L P O R M E
  D   C   D   Y   G   M

Then, read along the fence-line (zig-zag) and you're done!
Input Description
You will accept lines in the format:

enc # PLAINTEXT
or
dec # CIPHERTEXT

where enc # encodes PLAINTEXT with a rail-fence cipher using # lines,
and dec # decodes CIPHERTEXT using # lines.

For example:
enc 3 REDDITCOMRDAILYPROGRAMMER
Output Description

Encrypt or decrypt depending on the command given. So the example above gives:
RIMIRAREDTORALPORMEDCDYGM
Sample Inputs and Outputs
enc 2 LOLOLOLOLOLOLOLOLO
Result: LLLLLLLLLOOOOOOOOO

enc 4 THEQUICKBROWNFOXJUMPSOVERTHELAZYDOG
Result: TCNMRZHIKWFUPETAYEUBOOJSVHLDGQRXOEO

dec 4 TCNMRZHIKWFUPETAYEUBOOJSVHLDGQRXOEO
Result: THEQUICKBROWNFOXJUMPSOVERTHELAZYDOG

dec 7 3934546187438171450245968893099481332327954266552620198731963475632908289907
Result: 3141592653589793238462643383279502884197169399375105820974944592307816406286 (pi)
"""
import itertools

# magic transformation for n=3, the sequence is [0, 1, 2, 1]
# for n=4, the sequence will be [0, 1, 2, 3, 2, 1]
# pass output of range() function to the sequence lambda
sequence = lambda x: x + x[::-1][1:-1]


def encrypt(text, nlines):
    r_nlines = range(nlines)
    lines = ['' for _ in r_nlines]

    seq = sequence(r_nlines)
    iter_cycle = itertools.cycle(seq)

    for x in text:
        lines[iter_cycle.next()] += str(x)

    return ''.join(lines)


def decrypt(text, nlines):
    r_nlines = range(nlines)
    seq = sequence(r_nlines)
    # starts = sequence
    # get the cycle
    iter_cycle = itertools.cycle(seq)
    # get an encrypted sequence
    list_cycle = [iter_cycle.next() for _ in range(len(text))]
    enc_list_cycle = encrypt(list_cycle, nlines)
    # zip the sequence and the encrypted sequence to get the line
    # correspondence
    zenc_list = zip(text, enc_list_cycle)
    # group the sequence by line numbers
    lines = {i: list(items) for i, items in itertools.groupby(zenc_list,
                                                              lambda x: x[1])}

    # reinitialize the cycle
    iter_cycle = itertools.cycle(seq)
    decrypted = ''
    for _ in range(len(text)):
        current = str(iter_cycle.next())
        # get the current line and remove the first element from it
        decrypted += str(lines[current].pop(0)[0])
    return decrypted


if __name__ == '__main__':
    testcases = [
        (3, 'REDDITCOMRDAILYPROGRAMMER'),
        (2, 'LOLOLOLOLOLOLOLOLO'),
        (4, 'THEQUICKBROWNFOXJUMPSOVERTHELAZYDOG'),
        (7, '3934546187438171450245968893099481332327954266552620198731963475632908289907')
    ]

    for n, testcase in testcases:
        assert testcase == decrypt(encrypt(testcase, n), n)

print 'All tests pass!'
