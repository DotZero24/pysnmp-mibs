_I='tslineSesSession'
_H='tslineSesLine'
_G='tsLineNumber'
_F='OLD-CISCO-TS-MIB'
_E='unknown'
_D='read-write'
_C='Integer32'
_B='read-only'
_A='mandatory'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
local,=mibBuilder.importSymbols('CISCO-SMI','local')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
_Lts_ObjectIdentity=ObjectIdentity
lts=_Lts_ObjectIdentity((1,3,6,1,4,1,9,2,9))
_TsLines_Type=Integer32
_TsLines_Object=MibScalar
tsLines=_TsLines_Object((1,3,6,1,4,1,9,2,9,1),_TsLines_Type())
tsLines.setMaxAccess(_B)
if mibBuilder.loadTexts:tsLines.setStatus(_A)
_LtsLineTable_Object=MibTable
ltsLineTable=_LtsLineTable_Object((1,3,6,1,4,1,9,2,9,2))
if mibBuilder.loadTexts:ltsLineTable.setStatus(_A)
_LtsLineEntry_Object=MibTableRow
ltsLineEntry=_LtsLineEntry_Object((1,3,6,1,4,1,9,2,9,2,1))
ltsLineEntry.setIndexNames((0,_F,_G))
if mibBuilder.loadTexts:ltsLineEntry.setStatus(_A)
_TsLineActive_Type=Integer32
_TsLineActive_Object=MibTableColumn
tsLineActive=_TsLineActive_Object((1,3,6,1,4,1,9,2,9,2,1,1),_TsLineActive_Type())
tsLineActive.setMaxAccess(_B)
if mibBuilder.loadTexts:tsLineActive.setStatus(_A)
class _TsLineType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*((_E,1),('console',2),('terminal',3),('line-printer',4),('virtual-terminal',5),('auxiliary',6)))
_TsLineType_Type.__name__=_C
_TsLineType_Object=MibTableColumn
tsLineType=_TsLineType_Object((1,3,6,1,4,1,9,2,9,2,1,2),_TsLineType_Type())
tsLineType.setMaxAccess(_B)
if mibBuilder.loadTexts:tsLineType.setStatus(_A)
_TsLineAutobaud_Type=Integer32
_TsLineAutobaud_Object=MibTableColumn
tsLineAutobaud=_TsLineAutobaud_Object((1,3,6,1,4,1,9,2,9,2,1,3),_TsLineAutobaud_Type())
tsLineAutobaud.setMaxAccess(_B)
if mibBuilder.loadTexts:tsLineAutobaud.setStatus(_A)
_TsLineSpeedin_Type=Integer32
_TsLineSpeedin_Object=MibTableColumn
tsLineSpeedin=_TsLineSpeedin_Object((1,3,6,1,4,1,9,2,9,2,1,4),_TsLineSpeedin_Type())
tsLineSpeedin.setMaxAccess(_B)
if mibBuilder.loadTexts:tsLineSpeedin.setStatus(_A)
_TsLineSpeedout_Type=Integer32
_TsLineSpeedout_Object=MibTableColumn
tsLineSpeedout=_TsLineSpeedout_Object((1,3,6,1,4,1,9,2,9,2,1,5),_TsLineSpeedout_Type())
tsLineSpeedout.setMaxAccess(_B)
if mibBuilder.loadTexts:tsLineSpeedout.setStatus(_A)
class _TsLineFlow_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8)));namedValues=NamedValues(*((_E,1),('none',2),('software-input',3),('software-output',4),('software-both',5),('hardware-input',6),('hardware-output',7),('hardware-both',8)))
_TsLineFlow_Type.__name__=_C
_TsLineFlow_Object=MibTableColumn
tsLineFlow=_TsLineFlow_Object((1,3,6,1,4,1,9,2,9,2,1,6),_TsLineFlow_Type())
tsLineFlow.setMaxAccess(_B)
if mibBuilder.loadTexts:tsLineFlow.setStatus(_A)
class _TsLineModem_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*((_E,1),('none',2),('call-in',3),('call-out',4),('cts-required',5),('ri-is-cd',6),('inout',7)))
_TsLineModem_Type.__name__=_C
_TsLineModem_Object=MibTableColumn
tsLineModem=_TsLineModem_Object((1,3,6,1,4,1,9,2,9,2,1,7),_TsLineModem_Type())
tsLineModem.setMaxAccess(_B)
if mibBuilder.loadTexts:tsLineModem.setStatus(_A)
_TsLineLoc_Type=DisplayString
_TsLineLoc_Object=MibTableColumn
tsLineLoc=_TsLineLoc_Object((1,3,6,1,4,1,9,2,9,2,1,8),_TsLineLoc_Type())
tsLineLoc.setMaxAccess(_B)
if mibBuilder.loadTexts:tsLineLoc.setStatus(_A)
_TsLineTerm_Type=DisplayString
_TsLineTerm_Object=MibTableColumn
tsLineTerm=_TsLineTerm_Object((1,3,6,1,4,1,9,2,9,2,1,9),_TsLineTerm_Type())
tsLineTerm.setMaxAccess(_B)
if mibBuilder.loadTexts:tsLineTerm.setStatus(_A)
_TsLineScrlen_Type=Integer32
_TsLineScrlen_Object=MibTableColumn
tsLineScrlen=_TsLineScrlen_Object((1,3,6,1,4,1,9,2,9,2,1,10),_TsLineScrlen_Type())
tsLineScrlen.setMaxAccess(_B)
if mibBuilder.loadTexts:tsLineScrlen.setStatus(_A)
_TsLineScrwid_Type=Integer32
_TsLineScrwid_Object=MibTableColumn
tsLineScrwid=_TsLineScrwid_Object((1,3,6,1,4,1,9,2,9,2,1,11),_TsLineScrwid_Type())
tsLineScrwid.setMaxAccess(_B)
if mibBuilder.loadTexts:tsLineScrwid.setStatus(_A)
_TsLineEsc_Type=DisplayString
_TsLineEsc_Object=MibTableColumn
tsLineEsc=_TsLineEsc_Object((1,3,6,1,4,1,9,2,9,2,1,12),_TsLineEsc_Type())
tsLineEsc.setMaxAccess(_B)
if mibBuilder.loadTexts:tsLineEsc.setStatus(_A)
_TsLineTmo_Type=Integer32
_TsLineTmo_Object=MibTableColumn
tsLineTmo=_TsLineTmo_Object((1,3,6,1,4,1,9,2,9,2,1,13),_TsLineTmo_Type())
tsLineTmo.setMaxAccess(_B)
if mibBuilder.loadTexts:tsLineTmo.setStatus(_A)
_TsLineSestmo_Type=Integer32
_TsLineSestmo_Object=MibTableColumn
tsLineSestmo=_TsLineSestmo_Object((1,3,6,1,4,1,9,2,9,2,1,14),_TsLineSestmo_Type())
tsLineSestmo.setMaxAccess(_B)
if mibBuilder.loadTexts:tsLineSestmo.setStatus(_A)
_TsLineRotary_Type=Integer32
_TsLineRotary_Object=MibTableColumn
tsLineRotary=_TsLineRotary_Object((1,3,6,1,4,1,9,2,9,2,1,15),_TsLineRotary_Type())
tsLineRotary.setMaxAccess(_B)
if mibBuilder.loadTexts:tsLineRotary.setStatus(_A)
_TsLineUses_Type=Integer32
_TsLineUses_Object=MibTableColumn
tsLineUses=_TsLineUses_Object((1,3,6,1,4,1,9,2,9,2,1,16),_TsLineUses_Type())
tsLineUses.setMaxAccess(_B)
if mibBuilder.loadTexts:tsLineUses.setStatus(_A)
_TsLineNses_Type=Integer32
_TsLineNses_Object=MibTableColumn
tsLineNses=_TsLineNses_Object((1,3,6,1,4,1,9,2,9,2,1,17),_TsLineNses_Type())
tsLineNses.setMaxAccess(_B)
if mibBuilder.loadTexts:tsLineNses.setStatus(_A)
_TsLineUser_Type=DisplayString
_TsLineUser_Object=MibTableColumn
tsLineUser=_TsLineUser_Object((1,3,6,1,4,1,9,2,9,2,1,18),_TsLineUser_Type())
tsLineUser.setMaxAccess(_B)
if mibBuilder.loadTexts:tsLineUser.setStatus(_A)
_TsLineNoise_Type=Integer32
_TsLineNoise_Object=MibTableColumn
tsLineNoise=_TsLineNoise_Object((1,3,6,1,4,1,9,2,9,2,1,19),_TsLineNoise_Type())
tsLineNoise.setMaxAccess(_B)
if mibBuilder.loadTexts:tsLineNoise.setStatus(_A)
_TsLineNumber_Type=Integer32
_TsLineNumber_Object=MibTableColumn
tsLineNumber=_TsLineNumber_Object((1,3,6,1,4,1,9,2,9,2,1,20),_TsLineNumber_Type())
tsLineNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:tsLineNumber.setStatus(_A)
_TsLineTimeActive_Type=Integer32
_TsLineTimeActive_Object=MibTableColumn
tsLineTimeActive=_TsLineTimeActive_Object((1,3,6,1,4,1,9,2,9,2,1,21),_TsLineTimeActive_Type())
tsLineTimeActive.setMaxAccess(_B)
if mibBuilder.loadTexts:tsLineTimeActive.setStatus(_A)
_LtsLineSessionTable_Object=MibTable
ltsLineSessionTable=_LtsLineSessionTable_Object((1,3,6,1,4,1,9,2,9,3))
if mibBuilder.loadTexts:ltsLineSessionTable.setStatus(_A)
_LtsLineSessionEntry_Object=MibTableRow
ltsLineSessionEntry=_LtsLineSessionEntry_Object((1,3,6,1,4,1,9,2,9,3,1))
ltsLineSessionEntry.setIndexNames((0,_F,_H),(0,_F,_I))
if mibBuilder.loadTexts:ltsLineSessionEntry.setStatus(_A)
class _TslineSesType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11)));namedValues=NamedValues(*((_E,1),('pad',2),('stream',3),('rlogin',4),('telnet',5),('tcp',6),('lat',7),('mop',8),('slip',9),('xremote',10),('rshell',11)))
_TslineSesType_Type.__name__=_C
_TslineSesType_Object=MibTableColumn
tslineSesType=_TslineSesType_Object((1,3,6,1,4,1,9,2,9,3,1,1),_TslineSesType_Type())
tslineSesType.setMaxAccess(_B)
if mibBuilder.loadTexts:tslineSesType.setStatus(_A)
class _TslineSesDir_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_E,1),('incoming',2),('outgoing',3)))
_TslineSesDir_Type.__name__=_C
_TslineSesDir_Object=MibTableColumn
tslineSesDir=_TslineSesDir_Object((1,3,6,1,4,1,9,2,9,3,1,2),_TslineSesDir_Type())
tslineSesDir.setMaxAccess(_B)
if mibBuilder.loadTexts:tslineSesDir.setStatus(_A)
_TslineSesAddr_Type=IpAddress
_TslineSesAddr_Object=MibTableColumn
tslineSesAddr=_TslineSesAddr_Object((1,3,6,1,4,1,9,2,9,3,1,3),_TslineSesAddr_Type())
tslineSesAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:tslineSesAddr.setStatus(_A)
_TslineSesName_Type=DisplayString
_TslineSesName_Object=MibTableColumn
tslineSesName=_TslineSesName_Object((1,3,6,1,4,1,9,2,9,3,1,4),_TslineSesName_Type())
tslineSesName.setMaxAccess(_B)
if mibBuilder.loadTexts:tslineSesName.setStatus(_A)
_TslineSesCur_Type=Integer32
_TslineSesCur_Object=MibTableColumn
tslineSesCur=_TslineSesCur_Object((1,3,6,1,4,1,9,2,9,3,1,5),_TslineSesCur_Type())
tslineSesCur.setMaxAccess(_B)
if mibBuilder.loadTexts:tslineSesCur.setStatus(_A)
_TslineSesIdle_Type=Integer32
_TslineSesIdle_Object=MibTableColumn
tslineSesIdle=_TslineSesIdle_Object((1,3,6,1,4,1,9,2,9,3,1,6),_TslineSesIdle_Type())
tslineSesIdle.setMaxAccess(_B)
if mibBuilder.loadTexts:tslineSesIdle.setStatus(_A)
_TslineSesLine_Type=Integer32
_TslineSesLine_Object=MibTableColumn
tslineSesLine=_TslineSesLine_Object((1,3,6,1,4,1,9,2,9,3,1,7),_TslineSesLine_Type())
tslineSesLine.setMaxAccess(_B)
if mibBuilder.loadTexts:tslineSesLine.setStatus(_A)
_TslineSesSession_Type=Integer32
_TslineSesSession_Object=MibTableColumn
tslineSesSession=_TslineSesSession_Object((1,3,6,1,4,1,9,2,9,3,1,8),_TslineSesSession_Type())
tslineSesSession.setMaxAccess(_B)
if mibBuilder.loadTexts:tslineSesSession.setStatus(_A)
_TsMsgTtyLine_Type=Integer32
_TsMsgTtyLine_Object=MibScalar
tsMsgTtyLine=_TsMsgTtyLine_Object((1,3,6,1,4,1,9,2,9,4),_TsMsgTtyLine_Type())
tsMsgTtyLine.setMaxAccess(_D)
if mibBuilder.loadTexts:tsMsgTtyLine.setStatus(_A)
_TsMsgIntervaltim_Type=Integer32
_TsMsgIntervaltim_Object=MibScalar
tsMsgIntervaltim=_TsMsgIntervaltim_Object((1,3,6,1,4,1,9,2,9,5),_TsMsgIntervaltim_Type())
tsMsgIntervaltim.setMaxAccess(_D)
if mibBuilder.loadTexts:tsMsgIntervaltim.setStatus(_A)
_TsMsgDuration_Type=Integer32
_TsMsgDuration_Object=MibScalar
tsMsgDuration=_TsMsgDuration_Object((1,3,6,1,4,1,9,2,9,6),_TsMsgDuration_Type())
tsMsgDuration.setMaxAccess(_D)
if mibBuilder.loadTexts:tsMsgDuration.setStatus(_A)
_TsMsgText_Type=DisplayString
_TsMsgText_Object=MibScalar
tsMsgText=_TsMsgText_Object((1,3,6,1,4,1,9,2,9,7),_TsMsgText_Type())
tsMsgText.setMaxAccess(_D)
if mibBuilder.loadTexts:tsMsgText.setStatus(_A)
class _TsMsgTmpBanner_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('no',1),('additive',2)))
_TsMsgTmpBanner_Type.__name__=_C
_TsMsgTmpBanner_Object=MibScalar
tsMsgTmpBanner=_TsMsgTmpBanner_Object((1,3,6,1,4,1,9,2,9,8),_TsMsgTmpBanner_Type())
tsMsgTmpBanner.setMaxAccess(_D)
if mibBuilder.loadTexts:tsMsgTmpBanner.setStatus(_A)
class _TsMsgSend_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('nothing',1),('reload',2),('messagedone',3),('abort',4)))
_TsMsgSend_Type.__name__=_C
_TsMsgSend_Object=MibScalar
tsMsgSend=_TsMsgSend_Object((1,3,6,1,4,1,9,2,9,9),_TsMsgSend_Type())
tsMsgSend.setMaxAccess(_D)
if mibBuilder.loadTexts:tsMsgSend.setStatus(_A)
_TsClrTtyLine_Type=Integer32
_TsClrTtyLine_Object=MibScalar
tsClrTtyLine=_TsClrTtyLine_Object((1,3,6,1,4,1,9,2,9,10),_TsClrTtyLine_Type())
tsClrTtyLine.setMaxAccess(_D)
if mibBuilder.loadTexts:tsClrTtyLine.setStatus(_A)
mibBuilder.exportSymbols(_F,**{'lts':lts,'tsLines':tsLines,'ltsLineTable':ltsLineTable,'ltsLineEntry':ltsLineEntry,'tsLineActive':tsLineActive,'tsLineType':tsLineType,'tsLineAutobaud':tsLineAutobaud,'tsLineSpeedin':tsLineSpeedin,'tsLineSpeedout':tsLineSpeedout,'tsLineFlow':tsLineFlow,'tsLineModem':tsLineModem,'tsLineLoc':tsLineLoc,'tsLineTerm':tsLineTerm,'tsLineScrlen':tsLineScrlen,'tsLineScrwid':tsLineScrwid,'tsLineEsc':tsLineEsc,'tsLineTmo':tsLineTmo,'tsLineSestmo':tsLineSestmo,'tsLineRotary':tsLineRotary,'tsLineUses':tsLineUses,'tsLineNses':tsLineNses,'tsLineUser':tsLineUser,'tsLineNoise':tsLineNoise,_G:tsLineNumber,'tsLineTimeActive':tsLineTimeActive,'ltsLineSessionTable':ltsLineSessionTable,'ltsLineSessionEntry':ltsLineSessionEntry,'tslineSesType':tslineSesType,'tslineSesDir':tslineSesDir,'tslineSesAddr':tslineSesAddr,'tslineSesName':tslineSesName,'tslineSesCur':tslineSesCur,'tslineSesIdle':tslineSesIdle,_H:tslineSesLine,_I:tslineSesSession,'tsMsgTtyLine':tsMsgTtyLine,'tsMsgIntervaltim':tsMsgIntervaltim,'tsMsgDuration':tsMsgDuration,'tsMsgText':tsMsgText,'tsMsgTmpBanner':tsMsgTmpBanner,'tsMsgSend':tsMsgSend,'tsClrTtyLine':tsClrTtyLine})