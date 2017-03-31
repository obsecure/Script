#!/usr/bin/tclsh

set sPath       [ file dirname [ info script ] ]
set sDate       [ clock format [ clock seconds ] -format "%Y%m%d" ]

set sYear       [ clock format [ clock seconds ] -format "%Y" ]
set sMonth      [ clock format [ clock seconds ] -format "%m" ]
set sDay        [ clock format [ clock seconds ] -format "%d" ]
set sHour       [ clock format [ clock seconds ] -format "%H" ]
