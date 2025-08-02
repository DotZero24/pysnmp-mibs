_P='levelSegID'
_O='levelID'
_N='transit'
_M='master'
_L='forward'
_K='block'
_J='ctrlVlanID'
_I='reset'
_H='DisplayString'
_G='unknown'
_F='ZESR-MIB'
_E='read-write'
_D='read-only'
_C='read-create'
_B='Integer32'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_B,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_H,'PhysAddress','RowStatus','TextualConvention')
zxr10switch,=mibBuilder.importSymbols('ZXR10-SMI','zxr10switch')
_Zesr_ObjectIdentity=ObjectIdentity
zesr=_Zesr_ObjectIdentity((1,3,6,1,4,1,3902,3,102,12))
_ZesrGeneralConfig_ObjectIdentity=ObjectIdentity
zesrGeneralConfig=_ZesrGeneralConfig_ObjectIdentity((1,3,6,1,4,1,3902,3,102,12,1))
class _RestartTime_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(30,600))
_RestartTime_Type.__name__=_B
_RestartTime_Object=MibScalar
restartTime=_RestartTime_Object((1,3,6,1,4,1,3902,3,102,12,1,1),_RestartTime_Type())
restartTime.setMaxAccess(_E)
if mibBuilder.loadTexts:restartTime.setStatus(_A)
class _ProtocolMac_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('normal',0),('special',1)))
_ProtocolMac_Type.__name__=_B
_ProtocolMac_Object=MibScalar
protocolMac=_ProtocolMac_Object((1,3,6,1,4,1,3902,3,102,12,1,2),_ProtocolMac_Type())
protocolMac.setMaxAccess(_E)
if mibBuilder.loadTexts:protocolMac.setStatus(_A)
class _ClearSwitchTimes_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues((_I,1))
_ClearSwitchTimes_Type.__name__=_B
_ClearSwitchTimes_Object=MibScalar
clearSwitchTimes=_ClearSwitchTimes_Object((1,3,6,1,4,1,3902,3,102,12,1,3),_ClearSwitchTimes_Type())
clearSwitchTimes.setMaxAccess(_E)
if mibBuilder.loadTexts:clearSwitchTimes.setStatus(_A)
_ZesrDomainTable_Object=MibTable
zesrDomainTable=_ZesrDomainTable_Object((1,3,6,1,4,1,3902,3,102,12,2))
if mibBuilder.loadTexts:zesrDomainTable.setStatus(_A)
_ZesrDomainEntry_Object=MibTableRow
zesrDomainEntry=_ZesrDomainEntry_Object((1,3,6,1,4,1,3902,3,102,12,2,1))
zesrDomainEntry.setIndexNames((0,_F,_J))
if mibBuilder.loadTexts:zesrDomainEntry.setStatus(_A)
class _CtrlVlanID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094))
_CtrlVlanID_Type.__name__=_B
_CtrlVlanID_Object=MibTableColumn
ctrlVlanID=_CtrlVlanID_Object((1,3,6,1,4,1,3902,3,102,12,2,1,1),_CtrlVlanID_Type())
ctrlVlanID.setMaxAccess(_D)
if mibBuilder.loadTexts:ctrlVlanID.setStatus(_A)
class _ProtectInstanceID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,16))
_ProtectInstanceID_Type.__name__=_B
_ProtectInstanceID_Object=MibTableColumn
protectInstanceID=_ProtectInstanceID_Object((1,3,6,1,4,1,3902,3,102,12,2,1,2),_ProtectInstanceID_Type())
protectInstanceID.setMaxAccess(_C)
if mibBuilder.loadTexts:protectInstanceID.setStatus(_A)
_ZesrDomainRowStatus_Type=RowStatus
_ZesrDomainRowStatus_Object=MibTableColumn
zesrDomainRowStatus=_ZesrDomainRowStatus_Object((1,3,6,1,4,1,3902,3,102,12,2,1,3),_ZesrDomainRowStatus_Type())
zesrDomainRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:zesrDomainRowStatus.setStatus(_A)
class _ZesrDomainclearSwitchTimes_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues((_I,1))
_ZesrDomainclearSwitchTimes_Type.__name__=_B
_ZesrDomainclearSwitchTimes_Object=MibTableColumn
zesrDomainclearSwitchTimes=_ZesrDomainclearSwitchTimes_Object((1,3,6,1,4,1,3902,3,102,12,2,1,4),_ZesrDomainclearSwitchTimes_Type())
zesrDomainclearSwitchTimes.setMaxAccess(_E)
if mibBuilder.loadTexts:zesrDomainclearSwitchTimes.setStatus(_A)
_ZesrMajorTable_Object=MibTable
zesrMajorTable=_ZesrMajorTable_Object((1,3,6,1,4,1,3902,3,102,12,3))
if mibBuilder.loadTexts:zesrMajorTable.setStatus(_A)
_ZesrMajorEntry_Object=MibTableRow
zesrMajorEntry=_ZesrMajorEntry_Object((1,3,6,1,4,1,3902,3,102,12,3,1))
zesrMajorEntry.setIndexNames((0,_F,_J))
if mibBuilder.loadTexts:zesrMajorEntry.setStatus(_A)
class _MajorRole_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*((_M,0),(_N,1),('zess-master',2),('zess-transit',3)))
_MajorRole_Type.__name__=_B
_MajorRole_Object=MibTableColumn
majorRole=_MajorRole_Object((1,3,6,1,4,1,3902,3,102,12,3,1,1),_MajorRole_Type())
majorRole.setMaxAccess(_E)
if mibBuilder.loadTexts:majorRole.setStatus(_A)
class _MajorFirstPort_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_MajorFirstPort_Type.__name__=_H
_MajorFirstPort_Object=MibTableColumn
majorFirstPort=_MajorFirstPort_Object((1,3,6,1,4,1,3902,3,102,12,3,1,2),_MajorFirstPort_Type())
majorFirstPort.setMaxAccess(_C)
if mibBuilder.loadTexts:majorFirstPort.setStatus(_A)
class _MajorSecondPort_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_MajorSecondPort_Type.__name__=_H
_MajorSecondPort_Object=MibTableColumn
majorSecondPort=_MajorSecondPort_Object((1,3,6,1,4,1,3902,3,102,12,3,1,3),_MajorSecondPort_Type())
majorSecondPort.setMaxAccess(_C)
if mibBuilder.loadTexts:majorSecondPort.setStatus(_A)
class _MajorPreforwardTime_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,600))
_MajorPreforwardTime_Type.__name__=_B
_MajorPreforwardTime_Object=MibTableColumn
majorPreforwardTime=_MajorPreforwardTime_Object((1,3,6,1,4,1,3902,3,102,12,3,1,4),_MajorPreforwardTime_Type())
majorPreforwardTime.setMaxAccess(_C)
if mibBuilder.loadTexts:majorPreforwardTime.setStatus(_A)
class _MajorPreupTime_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,500))
_MajorPreupTime_Type.__name__=_B
_MajorPreupTime_Object=MibTableColumn
majorPreupTime=_MajorPreupTime_Object((1,3,6,1,4,1,3902,3,102,12,3,1,5),_MajorPreupTime_Type())
majorPreupTime.setMaxAccess(_C)
if mibBuilder.loadTexts:majorPreupTime.setStatus(_A)
class _MajorHelloTime_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,6))
_MajorHelloTime_Type.__name__=_B
_MajorHelloTime_Object=MibTableColumn
majorHelloTime=_MajorHelloTime_Object((1,3,6,1,4,1,3902,3,102,12,3,1,6),_MajorHelloTime_Type())
majorHelloTime.setMaxAccess(_C)
if mibBuilder.loadTexts:majorHelloTime.setStatus(_A)
class _MajorFailTime_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(3,18))
_MajorFailTime_Type.__name__=_B
_MajorFailTime_Object=MibTableColumn
majorFailTime=_MajorFailTime_Object((1,3,6,1,4,1,3902,3,102,12,3,1,7),_MajorFailTime_Type())
majorFailTime.setMaxAccess(_C)
if mibBuilder.loadTexts:majorFailTime.setStatus(_A)
class _MajorState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5)));namedValues=NamedValues(*(('init',0),('up',1),('down',2),('preup',3),('start',4),(_G,5)))
_MajorState_Type.__name__=_B
_MajorState_Object=MibTableColumn
majorState=_MajorState_Object((1,3,6,1,4,1,3902,3,102,12,3,1,8),_MajorState_Type())
majorState.setMaxAccess(_D)
if mibBuilder.loadTexts:majorState.setStatus(_A)
class _MajorFirstPortState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_G,0),(_K,1),(_L,2)))
_MajorFirstPortState_Type.__name__=_B
_MajorFirstPortState_Object=MibTableColumn
majorFirstPortState=_MajorFirstPortState_Object((1,3,6,1,4,1,3902,3,102,12,3,1,9),_MajorFirstPortState_Type())
majorFirstPortState.setMaxAccess(_D)
if mibBuilder.loadTexts:majorFirstPortState.setStatus(_A)
class _MajorSecondPortState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_G,0),(_K,1),(_L,2)))
_MajorSecondPortState_Type.__name__=_B
_MajorSecondPortState_Object=MibTableColumn
majorSecondPortState=_MajorSecondPortState_Object((1,3,6,1,4,1,3902,3,102,12,3,1,10),_MajorSecondPortState_Type())
majorSecondPortState.setMaxAccess(_D)
if mibBuilder.loadTexts:majorSecondPortState.setStatus(_A)
_MajorSwitchTimes_Type=Integer32
_MajorSwitchTimes_Object=MibTableColumn
majorSwitchTimes=_MajorSwitchTimes_Object((1,3,6,1,4,1,3902,3,102,12,3,1,11),_MajorSwitchTimes_Type())
majorSwitchTimes.setMaxAccess(_D)
if mibBuilder.loadTexts:majorSwitchTimes.setStatus(_A)
_ZesrMajorRowStatus_Type=RowStatus
_ZesrMajorRowStatus_Object=MibTableColumn
zesrMajorRowStatus=_ZesrMajorRowStatus_Object((1,3,6,1,4,1,3902,3,102,12,3,1,12),_ZesrMajorRowStatus_Type())
zesrMajorRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:zesrMajorRowStatus.setStatus(_A)
class _ZesrMajorclearSwitchTimes_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues((_I,1))
_ZesrMajorclearSwitchTimes_Type.__name__=_B
_ZesrMajorclearSwitchTimes_Object=MibTableColumn
zesrMajorclearSwitchTimes=_ZesrMajorclearSwitchTimes_Object((1,3,6,1,4,1,3902,3,102,12,3,1,13),_ZesrMajorclearSwitchTimes_Type())
zesrMajorclearSwitchTimes.setMaxAccess(_E)
if mibBuilder.loadTexts:zesrMajorclearSwitchTimes.setStatus(_A)
_ZesrLevelTable_Object=MibTable
zesrLevelTable=_ZesrLevelTable_Object((1,3,6,1,4,1,3902,3,102,12,4))
if mibBuilder.loadTexts:zesrLevelTable.setStatus(_A)
_ZesrLevelEntry_Object=MibTableRow
zesrLevelEntry=_ZesrLevelEntry_Object((1,3,6,1,4,1,3902,3,102,12,4,1))
zesrLevelEntry.setIndexNames((0,_F,_J),(0,_F,_O),(0,_F,_P))
if mibBuilder.loadTexts:zesrLevelEntry.setStatus(_A)
class _LevelID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2))
_LevelID_Type.__name__=_B
_LevelID_Object=MibTableColumn
levelID=_LevelID_Object((1,3,6,1,4,1,3902,3,102,12,4,1,1),_LevelID_Type())
levelID.setMaxAccess(_D)
if mibBuilder.loadTexts:levelID.setStatus(_A)
class _LevelSegID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4))
_LevelSegID_Type.__name__=_B
_LevelSegID_Object=MibTableColumn
levelSegID=_LevelSegID_Object((1,3,6,1,4,1,3902,3,102,12,4,1,2),_LevelSegID_Type())
levelSegID.setMaxAccess(_D)
if mibBuilder.loadTexts:levelSegID.setStatus(_A)
class _LevelRole_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*((_M,0),(_N,1),('edge-assistant',2),('edge-control',3)))
_LevelRole_Type.__name__=_B
_LevelRole_Object=MibTableColumn
levelRole=_LevelRole_Object((1,3,6,1,4,1,3902,3,102,12,4,1,3),_LevelRole_Type())
levelRole.setMaxAccess(_E)
if mibBuilder.loadTexts:levelRole.setStatus(_A)
class _LevelFirstPort_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_LevelFirstPort_Type.__name__=_H
_LevelFirstPort_Object=MibTableColumn
levelFirstPort=_LevelFirstPort_Object((1,3,6,1,4,1,3902,3,102,12,4,1,4),_LevelFirstPort_Type())
levelFirstPort.setMaxAccess(_C)
if mibBuilder.loadTexts:levelFirstPort.setStatus(_A)
class _LevelSecondPort_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_LevelSecondPort_Type.__name__=_H
_LevelSecondPort_Object=MibTableColumn
levelSecondPort=_LevelSecondPort_Object((1,3,6,1,4,1,3902,3,102,12,4,1,5),_LevelSecondPort_Type())
levelSecondPort.setMaxAccess(_C)
if mibBuilder.loadTexts:levelSecondPort.setStatus(_A)
class _LevelPreforwardTime_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,600))
_LevelPreforwardTime_Type.__name__=_B
_LevelPreforwardTime_Object=MibTableColumn
levelPreforwardTime=_LevelPreforwardTime_Object((1,3,6,1,4,1,3902,3,102,12,4,1,6),_LevelPreforwardTime_Type())
levelPreforwardTime.setMaxAccess(_C)
if mibBuilder.loadTexts:levelPreforwardTime.setStatus(_A)
class _LevelPreupTime_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,500))
_LevelPreupTime_Type.__name__=_B
_LevelPreupTime_Object=MibTableColumn
levelPreupTime=_LevelPreupTime_Object((1,3,6,1,4,1,3902,3,102,12,4,1,7),_LevelPreupTime_Type())
levelPreupTime.setMaxAccess(_C)
if mibBuilder.loadTexts:levelPreupTime.setStatus(_A)
class _LevelHelloTime_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,6))
_LevelHelloTime_Type.__name__=_B
_LevelHelloTime_Object=MibTableColumn
levelHelloTime=_LevelHelloTime_Object((1,3,6,1,4,1,3902,3,102,12,4,1,8),_LevelHelloTime_Type())
levelHelloTime.setMaxAccess(_C)
if mibBuilder.loadTexts:levelHelloTime.setStatus(_A)
class _LevelFailTime_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(3,18))
_LevelFailTime_Type.__name__=_B
_LevelFailTime_Object=MibTableColumn
levelFailTime=_LevelFailTime_Object((1,3,6,1,4,1,3902,3,102,12,4,1,9),_LevelFailTime_Type())
levelFailTime.setMaxAccess(_C)
if mibBuilder.loadTexts:levelFailTime.setStatus(_A)
class _LevelState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5)));namedValues=NamedValues(*(('init',0),('up',1),('down',2),('preup',3),('start',4),(_G,5)))
_LevelState_Type.__name__=_B
_LevelState_Object=MibTableColumn
levelState=_LevelState_Object((1,3,6,1,4,1,3902,3,102,12,4,1,10),_LevelState_Type())
levelState.setMaxAccess(_D)
if mibBuilder.loadTexts:levelState.setStatus(_A)
class _LevelFirstPortState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_G,0),(_K,1),(_L,2)))
_LevelFirstPortState_Type.__name__=_B
_LevelFirstPortState_Object=MibTableColumn
levelFirstPortState=_LevelFirstPortState_Object((1,3,6,1,4,1,3902,3,102,12,4,1,11),_LevelFirstPortState_Type())
levelFirstPortState.setMaxAccess(_D)
if mibBuilder.loadTexts:levelFirstPortState.setStatus(_A)
class _LevelSecondPortState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_G,0),(_K,1),(_L,2)))
_LevelSecondPortState_Type.__name__=_B
_LevelSecondPortState_Object=MibTableColumn
levelSecondPortState=_LevelSecondPortState_Object((1,3,6,1,4,1,3902,3,102,12,4,1,12),_LevelSecondPortState_Type())
levelSecondPortState.setMaxAccess(_D)
if mibBuilder.loadTexts:levelSecondPortState.setStatus(_A)
_LevelSwitchTimes_Type=Integer32
_LevelSwitchTimes_Object=MibTableColumn
levelSwitchTimes=_LevelSwitchTimes_Object((1,3,6,1,4,1,3902,3,102,12,4,1,13),_LevelSwitchTimes_Type())
levelSwitchTimes.setMaxAccess(_D)
if mibBuilder.loadTexts:levelSwitchTimes.setStatus(_A)
_ZesrLevelRowStatus_Type=RowStatus
_ZesrLevelRowStatus_Object=MibTableColumn
zesrLevelRowStatus=_ZesrLevelRowStatus_Object((1,3,6,1,4,1,3902,3,102,12,4,1,14),_ZesrLevelRowStatus_Type())
zesrLevelRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:zesrLevelRowStatus.setStatus(_A)
class _ZesrLevelclearSwitchTimes_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues((_I,1))
_ZesrLevelclearSwitchTimes_Type.__name__=_B
_ZesrLevelclearSwitchTimes_Object=MibTableColumn
zesrLevelclearSwitchTimes=_ZesrLevelclearSwitchTimes_Object((1,3,6,1,4,1,3902,3,102,12,4,1,15),_ZesrLevelclearSwitchTimes_Type())
zesrLevelclearSwitchTimes.setMaxAccess(_E)
if mibBuilder.loadTexts:zesrLevelclearSwitchTimes.setStatus(_A)
mibBuilder.exportSymbols(_F,**{'zesr':zesr,'zesrGeneralConfig':zesrGeneralConfig,'restartTime':restartTime,'protocolMac':protocolMac,'clearSwitchTimes':clearSwitchTimes,'zesrDomainTable':zesrDomainTable,'zesrDomainEntry':zesrDomainEntry,_J:ctrlVlanID,'protectInstanceID':protectInstanceID,'zesrDomainRowStatus':zesrDomainRowStatus,'zesrDomainclearSwitchTimes':zesrDomainclearSwitchTimes,'zesrMajorTable':zesrMajorTable,'zesrMajorEntry':zesrMajorEntry,'majorRole':majorRole,'majorFirstPort':majorFirstPort,'majorSecondPort':majorSecondPort,'majorPreforwardTime':majorPreforwardTime,'majorPreupTime':majorPreupTime,'majorHelloTime':majorHelloTime,'majorFailTime':majorFailTime,'majorState':majorState,'majorFirstPortState':majorFirstPortState,'majorSecondPortState':majorSecondPortState,'majorSwitchTimes':majorSwitchTimes,'zesrMajorRowStatus':zesrMajorRowStatus,'zesrMajorclearSwitchTimes':zesrMajorclearSwitchTimes,'zesrLevelTable':zesrLevelTable,'zesrLevelEntry':zesrLevelEntry,_O:levelID,_P:levelSegID,'levelRole':levelRole,'levelFirstPort':levelFirstPort,'levelSecondPort':levelSecondPort,'levelPreforwardTime':levelPreforwardTime,'levelPreupTime':levelPreupTime,'levelHelloTime':levelHelloTime,'levelFailTime':levelFailTime,'levelState':levelState,'levelFirstPortState':levelFirstPortState,'levelSecondPortState':levelSecondPortState,'levelSwitchTimes':levelSwitchTimes,'zesrLevelRowStatus':zesrLevelRowStatus,'zesrLevelclearSwitchTimes':zesrLevelclearSwitchTimes})