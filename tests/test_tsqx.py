import io

from tsqx.__main__ import Emitter

TEST_INPUT = r"""~triangle A B C

P = (1, 2)
P = foot A B C
P = foot(A, B, C)
P = dir(180)

# comment
P := dir(1, 2) # comment

P_1 ;= foot A B C
P_2 := foot A B C
P_3 dl= foot A B C
P_4 d= foot A B C
P_5 l= foot A B C

P_6 S = (1, 2)
P_7 NE = (1, 2)
P_8 4E2N = (1, 2)
P_9 1N1SE1N = (1, 2)

P := midpoint A--B
P := midpoint (foot A B C)--B
P := midpoint B--(foot A B C)
P := midpoint (foot A B C)--(foot B C A)

P := (rotate -30 E)(D)
P := (rotate -30 E)(foot A B C)
P := (shift (0, 1))(rotate -30 E)(foot A B C)
P := (rotate -30 E)(extension A (foot A B C) C E)

A--B--C--cycle
(foot A B C)--D
D--(foot A B C)
(foot A B C)--(foot B C A)
circumcircle A B C
circumcircle A (extension A B C D) E

A--B / blue
A--B / dashed
A--B / dashed blue
A--B--C--cycle / lightgray / blue
A--B--C--cycle / 0.2 lightgray / dashed blue
A--B--C--cycle / 0.2 lightgray /"""

TEST_OUTPUT = r"""pair A = dir(110); // via ~triangle
pair B = dir(210); // via ~triangle
pair C = dir(330); // via ~triangle

pair P = (1 , 2);
pair P = foot(A, B, C);
pair P = foot(A, B, C);
pair P = dir(180);

//  comment
pair P = dir(1, 2); //  comment

pair P_1 = foot(A, B, C);
pair P_2 = foot(A, B, C);
pair P_3 = foot(A, B, C);
pair P_4 = foot(A, B, C);
pair P_5 = foot(A, B, C);

pair P_6 = (1 , 2);
pair P_7 = (1 , 2);
pair P_8 = (1 , 2);
pair P_9 = (1 , 2);

pair P = midpoint(A--B);
pair P = midpoint(foot(A, B, C)--B);
pair P = midpoint(B--foot(A, B, C));
pair P = midpoint(foot(A, B, C)--foot(B, C, A));

pair P = rotate(-30, E)*D;
pair P = rotate(-30, E)*foot(A, B, C);
pair P = shift((0 , 1))*rotate(-30, E)*foot(A, B, C);
pair P = rotate(-30, E)*extension(A, foot(A, B, C), C, E);

draw(A--B--C--cycle);
draw(foot(A, B, C)--D);
draw(D--foot(A, B, C));
draw(foot(A, B, C)*-(-)*foot(B, C, A));
draw(circumcircle(A, B, C));
draw(circumcircle(A, extension(A, B, C, D), E));

draw(A--B, blue);
draw(A--B, dashed);
draw(A--B, dashed+blue);
filldraw(A--B--C--cycle, lightgray, blue);
filldraw(A--B--C--cycle, opacity(0.2)+lightgray, dashed+blue);
filldraw(A--B--C--cycle, opacity(0.2)+lightgray, defaultpen);

dot("$A$", A, dir(A));
dot("$B$", B, dir(B));
dot("$C$", C, dir(C));
dot("$P$", P, dir(P));
dot("$P$", P, dir(P));
dot("$P$", P, dir(P));
dot("$P$", P, dir(P));
label("$P_1$", P_1, dir(P_1));
dot("$P_3$", P_3, dir(P_3));
dot(P_4);
label("$P_5$", P_5, dir(P_5));
dot("$P_6$", P_6, plain.S);
dot("$P_7$", P_7, plain.NE);
dot("$P_8$", P_8, 4*plain.E+2*plain.N);
dot("$P_9$", P_9, 1*plain.N+1*plain.SE+1*plain.N);

/* --------------------------------+
| TSQX: by Evan Chen and CJ Quines |
| https://github.com/vEnhance/tsqx |
+----------------------------------+
~triangle A B C

P = (1, 2)
P = foot A B C
P = foot(A, B, C)
P = dir(180)

# comment
P := dir(1, 2) # comment

P_1 ;= foot A B C
P_2 := foot A B C
P_3 dl= foot A B C
P_4 d= foot A B C
P_5 l= foot A B C

P_6 S = (1, 2)
P_7 NE = (1, 2)
P_8 4E2N = (1, 2)
P_9 1N1SE1N = (1, 2)

P := midpoint A--B
P := midpoint (foot A B C)--B
P := midpoint B--(foot A B C)
P := midpoint (foot A B C)--(foot B C A)

P := (rotate -30 E)(D)
P := (rotate -30 E)(foot A B C)
P := (shift (0, 1))(rotate -30 E)(foot A B C)
P := (rotate -30 E)(extension A (foot A B C) C E)

A--B--C--cycle
(foot A B C)--D
D--(foot A B C)
(foot A B C)--(foot B C A)
circumcircle A B C
circumcircle A (extension A B C D) E

A--B / blue
A--B / dashed
A--B / dashed blue
A--B--C--cycle / lightgray / blue
A--B--C--cycle / 0.2 lightgray / dashed blue
A--B--C--cycle / 0.2 lightgray /
*/"""


def test_default_conversion(capsys):
    input_stream = io.StringIO(TEST_INPUT)
    emitter = Emitter(input_stream)
    emitter.emit()
    captured = capsys.readouterr()
    assert captured.out.strip() == TEST_OUTPUT
