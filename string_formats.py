ESCAPE	DESCRIPTION.	EXAMPLE
%d	Decimal integers (not floating point).	"%d" % 45 == '45'
%i	Same as %d.	"%i" % 45 == '45'
%o	Octal number.	"%o" % 1000 == '1750'
%u	Unsigned decimal.	"%u" % -1000 == '-1000'
%x	Hexadecimal lowercase.	"%x" % 1000 == '3e8'
%X	Hexadecimal uppercase.	"%X" % 1000 == '3E8'
%e	Exponential notation, lowercase 'e'.	"%e" % 1000 == '1.000000e+03'
%E	Exponential notation, uppercase 'E'.	"%E" % 1000 == '1.000000E+03'
%f	Floating point real number.	"%f" % 10.34 == '10.340000'
%F	Same as %f.	"%F" % 10.34 == '10.340000'
%g	Either %f or %e, whichever is shorter.	"%g" % 10.34 == '10.34'
%G	Same as %g but uppercase.	"%G" % 10.34 == '10.34'
%c	Character format.	"%c" % 34 == '"'
%r	Repr format (debugging format).	"%r" % int == "<type 'int'>"
%s	String format.	"%s there" % 'hi' == 'hi there'
%%	A percent sign.	"%g%%" % 10.34 == '10.34%'