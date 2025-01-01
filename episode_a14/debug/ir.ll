; ModuleID = "main"
target triple = "x86_64-pc-windows-msvc"
target datalayout = ""

declare i32 @"printf"(i8* %".1", ...)

@"true" = constant i1 1
@"false" = constant i1 0
define i32 @"add"(i32 %".1", i32 %".2")
{
add_entry:
  %".4" = alloca i32
  store i32 %".1", i32* %".4"
  %".6" = alloca i32
  store i32 %".2", i32* %".6"
  %".8" = load i32, i32* %".4"
  %".9" = load i32, i32* %".6"
  %".10" = add i32 %".8", %".9"
  ret i32 %".10"
}

define i32 @"main"()
{
main_entry:
  %".2" = alloca i32
  store i32 0, i32* %".2"
  %".4" = alloca i32
  store i32 0, i32* %".4"
  br label %"for_loop_entry_1"
for_loop_entry_1:
  %".7" = load i32, i32* %".4"
  %".8" = icmp eq i32 %".7", 5
  br i1 %".8", label %"for_loop_entry_1.if", label %"for_loop_entry_1.endif"
for_loop_otherwise_1:
  %".32" = load i32, i32* %".2"
  ret i32 %".32"
for_loop_entry_1.if:
  br label %"for_loop_otherwise_1"
for_loop_entry_1.endif:
  %".11" = xor i1 0, -1
  br i1 %".11", label %"for_loop_entry_1.endif.if", label %"for_loop_entry_1.endif.endif"
for_loop_entry_1.endif.if:
  %".13" = alloca [9 x i8]*
  store [9 x i8]* @"__str_2", [9 x i8]** %".13"
  %".15" = bitcast [9 x i8]* @"__str_2" to i8*
  %".16" = call i32 (i8*, ...) @"printf"(i8* %".15")
  br label %"for_loop_entry_1.endif.endif"
for_loop_entry_1.endif.endif:
  %".18" = load i32, i32* %".4"
  %".19" = alloca [9 x i8]*
  store [9 x i8]* @"__str_3", [9 x i8]** %".19"
  %".21" = bitcast [9 x i8]* @"__str_3" to i8*
  %".22" = call i32 (i8*, ...) @"printf"(i8* %".21", i32 %".18")
  %".23" = load i32, i32* %".4"
  %".24" = load i32, i32* %".2"
  store i32 %".23", i32* %".2"
  %".26" = load i32, i32* %".4"
  %".27" = add i32 %".26", 1
  store i32 %".27", i32* %".4"
  %".29" = load i32, i32* %".4"
  %".30" = icmp slt i32 %".29", 10
  br i1 %".30", label %"for_loop_entry_1", label %"for_loop_otherwise_1"
}

@"__str_2" = internal constant [9 x i8] c"not true\00"
@"__str_3" = internal constant [9 x i8] c"i = %i\0a\00\00"