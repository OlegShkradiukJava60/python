# HW#36 solution
## Update code of LTR Evaluation from CW #36
### Write additional function __checkArithmeticExpr
takes: expression<br>
checks matching against defined regex. It is only syntax checking that includes placing parentheses, operands as any number (either integer or float), given operators (see CW + ** as pow additional operator) with appropriate placing operands and operators
checks pairing of parentheses ( and ) only. Regex may check placing parentheses but cannot check pairing. So "(10 + 20))))" is ok from syntax aspect but no pairing; () + 10 (/) 20 - is ok from pairing aspect but no from syntax
### Write addition tests for testing  syntax and pairing parentheses
