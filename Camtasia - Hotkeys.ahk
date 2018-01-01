;*********************************************************
;*	 				CAMTASIA - Hotkeys                   *
;*		 Script By Rogério Dec (www.rogeriodec.com.br) 	 *
;*********************************************************

; **************************************************************
; PAGE UP:				SCROLL one PAGE Left and CENTRALIZE Cursor
; PAGE DOWN: 			SCROLL one PAGE Right and CENTRALIZE Cursor
; Ctrl+Alt+Left: 		MOVE Cursor 30 frames Left (1 second)
; Ctrl+Alt+Right: 		MOVE Cursor 30 frames Right (1 second)
; Ctrl+Middle Mouse: 	Set cursor to the current mouse position
; Middle Mouse: 		Set cursor to the current mouse position and deselect any range pre-selected in timeline. Hold+move (left or right) to create a new selection
; Alt+S: 				Silence (Mute) current selection 
; X: 					Same as Ctrl+x (more ergonomic)
; **************************************************************

#NoEnv 
SendMode Input  
SetWorkingDir %A_ScriptDir%  

#IfWinActive ahk_exe CamtasiaStudio.exe

SetControlDelay -1
Global x, y

PgUp:: 
	Gosub, Prepare	
	Clk(150, h_Win-15) ; scroll left
	Clk(w_Win/2, y+h+120) ; centralize cursor
Return

PgDn::
	Gosub, Prepare
	Clk(w_Win-45, h_Win-15) ; scroll right
	Clk(w_Win/2, y+h+120) ; centralize cursor
Return

^Mbutton::
mbtn:
	Gosub, Prepare
	Clk(x_mouse, y+h+120)
Return

Mbutton::
	BlockInput, MouseMove
	Gosub mbtn
	Click 2
	Sleep 200
	ft=0
	While (GetKeyState("MButton","p")) {
		if ft=0 
		{
			MouseClick Left,15, -5,,,D, R
			ft=1
			BlockInput, MouseMoveOff
		}
	}
	BlockInput, MouseMoveOff
	Click Up
Return

^!Left::
	Send ^{Left 30}
Return

^!Right::
	Send ^{Right 30}
Return

x:: ^x

!s::
	ControlClick % FindControl("&Silence")
Return

;************** GENERIC FUNCTIONS *****************************

Prepare:
	MouseGetPos, x_mouse, y_mouse, WinTitle
	ControlGetPos, x, y, w, h, AfxFrameOrView100u2, ahk_id %WinTitle%
	WinGetPos,,,w_Win, h_Win
Return

FindControl(SearchText) 
{
	WinGet, List, ControlList, A
	Loop, Parse, List, `n
	{
		ControlGetText, Text, %A_LoopField%, A
		If (Text = SearchText) {
			Label = %A_LoopField%
			Return Label
		}
	}
}

Clk(x, y) 
{
	MouseMove x, y
	Click
}

Erro(Msg)
{
	MsgBox %Msg%
	Exit
}

; ************************************************************************
; Reload current script (just used when editing this script in Notepad++)
; ************************************************************************
#IfWinActive, ahk_class Notepad++

^r::
Send !as
WinGetActiveTitle, wtitle
if wtitle contains %A_ScriptFullPath%
   Reload
return

#IfWinActive
