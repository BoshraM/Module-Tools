Do not use any tools or programming to solve these problems. Work it out yourself by hand, and fill in the answers.

Do not convert any binary numbers to decimal when solving a question unless the question explicitly tells you to.

The goal of these exercises is for you to gain an intuition for binary numbers. Using tools to solve the problems defeats the point.

The answers to these questions will require a bit of explanation, not just a simple answer.

Q16: How can you test if a binary number is a power of two (e.g. 1, 2, 4, 8, 16, ...)?
Answer: If there is just one 1 in a binary number, then it is a power of 2. This is because each bit represents a power of 2, so if there is just one 1 bit in a binary number, the value represents a power of 2.

Q17: If reading the byte 0x21 as an ASCII character, what character would it mean?
Answer: !

Q18: If reading the byte 0x21 as a greyscale colour, as described in "Approaches for Representing Colors and Images", what colour would it mean?
Answer: It represents 33, which is in the range of 0–255 from dark to light. This value represents a very dark grey.

Q19: If reading the bytes 0xAA00FF as a sequence of three one-byte decimal numbers, what decimal numbers would they be?
Answer:  three one-byte => 
AA | 00 | FF ==> AA : 10 * 16 + 10 * 1 = 170 | 00 : 0 * 16 + 0 * 1 = 0 | FF : 15 * 16 + 15 * 1 = 255
so it reperesnt 170, 0, 255

Q20: If reading the bytes 0xAA00FF as an RGB colour, as described in "Approaches for Representing Colors and Images", what colour would it mean?
Answer: AA => 170 Red,  00 => 0 green , FF : 255 is blue
