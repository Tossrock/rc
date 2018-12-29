#SingleInstance force
#NoEnv  ; Recommended for performance and compatibility with future AutoHotkey releases.
; #Warn  ; Enable warnings to assist with detecting common errors.
SendMode Input  ; Recommended for new scripts due to its superior speed and reliability.
SetWorkingDir %A_ScriptDir%  ; Ensures a consistent starting directory.
#IfWinActive ahk_exe ubuntu.exe
#h::
Send, ^b
Send, h
return
#j::
Send, ^b
Send, j
return
#k::
Send, ^b
Send, k
return
#l::
Send, ^b
Send, l
return
#e::
Send, ^b
Send, q
return
#p::
Send, ^b
Send, p
return
#t::
Send, ^b
Send, c
return
^Tab::
Send, ^b
Send, n
return
^+Tab::
Send, ^b
Send, N
return
#'::
Send, ^b
Send, "
return
#z::
Send, ^b
Send, z
return
#;::
Send, ^b
Send, `%
return
#IfWinActive
