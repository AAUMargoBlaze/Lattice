package generated;

import com.intellij.lexer.FlexLexer;
import com.intellij.psi.tree.IElementType;

import static com.intellij.psi.TokenType.BAD_CHARACTER;
import static com.intellij.psi.TokenType.WHITE_SPACE;
import static generated.GeneratedTypes.*;

%%

%{
  public _GrammarLexer() {
    this((java.io.Reader)null);
  }
%}

%public
%class _GrammarLexer
%implements FlexLexer
%function advance
%type IElementType
%unicode

EOL=\R
WHITE_SPACE=\s+

SPACE=[ \t\n\x0B\f\r]+
ID=[a-zA-Z_0-9]+
STRING=('([^'\\]|\\.)*'|\"([^\"\\]|\\\"|\\'|\\)*\")
NUMBER=[0-9]+
LINE_COMMENT="//".*
BLOCK_COMMENT="/"\*(.|\n)*\*"/"

%%
<YYINITIAL> {
  {WHITE_SPACE}        { return WHITE_SPACE; }

  ";"                  { return SEMICOLON; }
  "{"                  { return LEFT_BRACE; }
  "}"                  { return RIGHT_BRACE; }
  "("                  { return LEFT_PAREN; }
  ")"                  { return RIGHT_PAREN; }
  ","                  { return COMMA; }
  "="                  { return OP_ASSIGN; }
  "=="                 { return OP_B_EQ; }
  "!="                 { return OP_B_NEQ; }
  "||"                 { return OP_B_OR; }
  "&&"                 { return OP_B_AND; }
  "!"                  { return OP_B_NOT; }
  "+"                  { return OP_ADD; }
  "-"                  { return OP_SUB; }
  "*"                  { return OP_MULT; }
  "/"                  { return OP_DIV; }
  "%"                  { return OP_REM; }
  "<"                  { return OP_GRT; }
  "ref"                { return OP_REF; }
  "clone"              { return OP_CLONE; }
  "print"              { return OP_PRINT; }
  "int"                { return TYPE_INT; }
  "float"              { return TYPE_FLOAT; }
  "str"                { return TYPE_STRING; }
  "bool"               { return TYPE_BOOL; }
  "graph"              { return TYPE_GRAPH; }
  "rel"                { return TYPE_RELATIONSHIP; }
  "true"               { return KEYWORD_TRUE; }
  "false"              { return KEYWORD_FALSE; }
  ""                   { return EPSILON; }
  "|-"                 { return OP_REL_LEFT; }
  "->"                 { return OP_REL_RIGHT; }
  "assign"             { return ASSIGN; }
  "num"                { return NUM; }
  "clone"              { return CLONE; }

  {SPACE}              { return SPACE; }
  {ID}                 { return ID; }
  {STRING}             { return STRING; }
  {NUMBER}             { return NUMBER; }
  {LINE_COMMENT}       { return LINE_COMMENT; }
  {BLOCK_COMMENT}      { return BLOCK_COMMENT; }

}

[^] { return BAD_CHARACTER; }
