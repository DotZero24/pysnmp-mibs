_L='raisecomFanSpeedDueValue'
_K='raisecomFanSpeedLevelIndex'
_J='not-accessible'
_I='raisecomFanCardState'
_H='raisecomFanSpeedValue'
_G='Unsigned32'
_F='raisecomFanIndex'
_E='read-write'
_D='Integer32'
_C='read-only'
_B='RAISECOM-FANMONITOR-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
raisecomSystem,=mibBuilder.importSymbols('RAISECOM-SYSTEM-MIB','raisecomSystem')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_G,'iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention','TruthValue')
raisecomFanMonitor=ModuleIdentity((1,3,6,1,4,1,8886,1,1,5))
if mibBuilder.loadTexts:raisecomFanMonitor.setRevisions(('2010-12-30 00:00',))
_RaisecomFanMonitorNotification_ObjectIdentity=ObjectIdentity
raisecomFanMonitorNotification=_RaisecomFanMonitorNotification_ObjectIdentity((1,3,6,1,4,1,8886,1,1,5,1))
_RaisecomFanMonitorMibObjects_ObjectIdentity=ObjectIdentity
raisecomFanMonitorMibObjects=_RaisecomFanMonitorMibObjects_ObjectIdentity((1,3,6,1,4,1,8886,1,1,5,2))
_RaisecomFanMonitorGlobalGroup_ObjectIdentity=ObjectIdentity
raisecomFanMonitorGlobalGroup=_RaisecomFanMonitorGlobalGroup_ObjectIdentity((1,3,6,1,4,1,8886,1,1,5,2,1))
class _RaisecomFanMonitorMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('enforce',1),('auto',2)))
_RaisecomFanMonitorMode_Type.__name__=_D
_RaisecomFanMonitorMode_Object=MibScalar
raisecomFanMonitorMode=_RaisecomFanMonitorMode_Object((1,3,6,1,4,1,8886,1,1,5,2,1,1),_RaisecomFanMonitorMode_Type())
raisecomFanMonitorMode.setMaxAccess(_E)
if mibBuilder.loadTexts:raisecomFanMonitorMode.setStatus(_A)
class _RaisecomFanMonitorSpdLevel_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4))
_RaisecomFanMonitorSpdLevel_Type.__name__=_G
_RaisecomFanMonitorSpdLevel_Object=MibScalar
raisecomFanMonitorSpdLevel=_RaisecomFanMonitorSpdLevel_Object((1,3,6,1,4,1,8886,1,1,5,2,1,2),_RaisecomFanMonitorSpdLevel_Type())
raisecomFanMonitorSpdLevel.setMaxAccess(_E)
if mibBuilder.loadTexts:raisecomFanMonitorSpdLevel.setStatus(_A)
_RaisecomFanMonitorNumber_Type=Unsigned32
_RaisecomFanMonitorNumber_Object=MibScalar
raisecomFanMonitorNumber=_RaisecomFanMonitorNumber_Object((1,3,6,1,4,1,8886,1,1,5,2,1,3),_RaisecomFanMonitorNumber_Type())
raisecomFanMonitorNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:raisecomFanMonitorNumber.setStatus(_A)
_RaisecomFanMonitorLevlNumber_Type=Unsigned32
_RaisecomFanMonitorLevlNumber_Object=MibScalar
raisecomFanMonitorLevlNumber=_RaisecomFanMonitorLevlNumber_Object((1,3,6,1,4,1,8886,1,1,5,2,1,4),_RaisecomFanMonitorLevlNumber_Type())
raisecomFanMonitorLevlNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:raisecomFanMonitorLevlNumber.setStatus(_A)
class _RaisecomFanCardState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('all-down',1),('all-up',2),('card1-up',3),('card2-up',4)))
_RaisecomFanCardState_Type.__name__=_D
_RaisecomFanCardState_Object=MibScalar
raisecomFanCardState=_RaisecomFanCardState_Object((1,3,6,1,4,1,8886,1,1,5,2,1,5),_RaisecomFanCardState_Type())
raisecomFanCardState.setMaxAccess(_C)
if mibBuilder.loadTexts:raisecomFanCardState.setStatus(_A)
_RaisecomFanCardSerialNumber_Type=OctetString
_RaisecomFanCardSerialNumber_Object=MibScalar
raisecomFanCardSerialNumber=_RaisecomFanCardSerialNumber_Object((1,3,6,1,4,1,8886,1,1,5,2,1,6),_RaisecomFanCardSerialNumber_Type())
raisecomFanCardSerialNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:raisecomFanCardSerialNumber.setStatus(_A)
class _RaisecomFanMonitorTrapSendEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('disable',0),('enable',1)))
_RaisecomFanMonitorTrapSendEnable_Type.__name__=_D
_RaisecomFanMonitorTrapSendEnable_Object=MibScalar
raisecomFanMonitorTrapSendEnable=_RaisecomFanMonitorTrapSendEnable_Object((1,3,6,1,4,1,8886,1,1,5,2,1,7),_RaisecomFanMonitorTrapSendEnable_Type())
raisecomFanMonitorTrapSendEnable.setMaxAccess(_E)
if mibBuilder.loadTexts:raisecomFanMonitorTrapSendEnable.setStatus(_A)
_RaisecomFanMonitorStateTable_Object=MibTable
raisecomFanMonitorStateTable=_RaisecomFanMonitorStateTable_Object((1,3,6,1,4,1,8886,1,1,5,2,2))
if mibBuilder.loadTexts:raisecomFanMonitorStateTable.setStatus(_A)
_RaisecomFanMonitorStateEntry_Object=MibTableRow
raisecomFanMonitorStateEntry=_RaisecomFanMonitorStateEntry_Object((1,3,6,1,4,1,8886,1,1,5,2,2,1))
raisecomFanMonitorStateEntry.setIndexNames((0,_B,_F))
if mibBuilder.loadTexts:raisecomFanMonitorStateEntry.setStatus(_A)
_RaisecomFanIndex_Type=Unsigned32
_RaisecomFanIndex_Object=MibTableColumn
raisecomFanIndex=_RaisecomFanIndex_Object((1,3,6,1,4,1,8886,1,1,5,2,2,1,1),_RaisecomFanIndex_Type())
raisecomFanIndex.setMaxAccess(_J)
if mibBuilder.loadTexts:raisecomFanIndex.setStatus(_A)
_RaisecomFanSpeedValue_Type=Unsigned32
_RaisecomFanSpeedValue_Object=MibTableColumn
raisecomFanSpeedValue=_RaisecomFanSpeedValue_Object((1,3,6,1,4,1,8886,1,1,5,2,2,1,2),_RaisecomFanSpeedValue_Type())
raisecomFanSpeedValue.setMaxAccess(_C)
if mibBuilder.loadTexts:raisecomFanSpeedValue.setStatus(_A)
class _RaisecomFanWorkState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('normal',1),('abnormal',2)))
_RaisecomFanWorkState_Type.__name__=_D
_RaisecomFanWorkState_Object=MibTableColumn
raisecomFanWorkState=_RaisecomFanWorkState_Object((1,3,6,1,4,1,8886,1,1,5,2,2,1,3),_RaisecomFanWorkState_Type())
raisecomFanWorkState.setMaxAccess(_C)
if mibBuilder.loadTexts:raisecomFanWorkState.setStatus(_A)
_RaisecomFanSpeedLevelTable_Object=MibTable
raisecomFanSpeedLevelTable=_RaisecomFanSpeedLevelTable_Object((1,3,6,1,4,1,8886,1,1,5,2,3))
if mibBuilder.loadTexts:raisecomFanSpeedLevelTable.setStatus(_A)
_RaisecomFanSpeedLevelEntry_Object=MibTableRow
raisecomFanSpeedLevelEntry=_RaisecomFanSpeedLevelEntry_Object((1,3,6,1,4,1,8886,1,1,5,2,3,1))
raisecomFanSpeedLevelEntry.setIndexNames((0,_B,_K))
if mibBuilder.loadTexts:raisecomFanSpeedLevelEntry.setStatus(_A)
_RaisecomFanSpeedLevelIndex_Type=Unsigned32
_RaisecomFanSpeedLevelIndex_Object=MibTableColumn
raisecomFanSpeedLevelIndex=_RaisecomFanSpeedLevelIndex_Object((1,3,6,1,4,1,8886,1,1,5,2,3,1,1),_RaisecomFanSpeedLevelIndex_Type())
raisecomFanSpeedLevelIndex.setMaxAccess(_J)
if mibBuilder.loadTexts:raisecomFanSpeedLevelIndex.setStatus(_A)
_RaisecomFanSpeedDueValue_Type=Unsigned32
_RaisecomFanSpeedDueValue_Object=MibTableColumn
raisecomFanSpeedDueValue=_RaisecomFanSpeedDueValue_Object((1,3,6,1,4,1,8886,1,1,5,2,3,1,2),_RaisecomFanSpeedDueValue_Type())
raisecomFanSpeedDueValue.setMaxAccess(_E)
if mibBuilder.loadTexts:raisecomFanSpeedDueValue.setStatus(_A)
class _RaisecomFanSpeedTemperatureScale_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(45,75))
_RaisecomFanSpeedTemperatureScale_Type.__name__=_G
_RaisecomFanSpeedTemperatureScale_Object=MibTableColumn
raisecomFanSpeedTemperatureScale=_RaisecomFanSpeedTemperatureScale_Object((1,3,6,1,4,1,8886,1,1,5,2,3,1,3),_RaisecomFanSpeedTemperatureScale_Type())
raisecomFanSpeedTemperatureScale.setMaxAccess(_E)
if mibBuilder.loadTexts:raisecomFanSpeedTemperatureScale.setStatus(_A)
raisecomFanSpeedNormal=NotificationType((1,3,6,1,4,1,8886,1,1,5,1,1))
raisecomFanSpeedNormal.setObjects(*((_B,_F),(_B,_H)))
if mibBuilder.loadTexts:raisecomFanSpeedNormal.setStatus(_A)
raisecomFanSpeedAbnormal=NotificationType((1,3,6,1,4,1,8886,1,1,5,1,2))
raisecomFanSpeedAbnormal.setObjects(*((_B,_F),(_B,_H),(_B,_L)))
if mibBuilder.loadTexts:raisecomFanSpeedAbnormal.setStatus(_A)
raisecomFanCardUp=NotificationType((1,3,6,1,4,1,8886,1,1,5,1,3))
raisecomFanCardUp.setObjects((_B,_I))
if mibBuilder.loadTexts:raisecomFanCardUp.setStatus(_A)
raisecomFanCardDown=NotificationType((1,3,6,1,4,1,8886,1,1,5,1,4))
raisecomFanCardDown.setObjects((_B,_I))
if mibBuilder.loadTexts:raisecomFanCardDown.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'raisecomFanMonitor':raisecomFanMonitor,'raisecomFanMonitorNotification':raisecomFanMonitorNotification,'raisecomFanSpeedNormal':raisecomFanSpeedNormal,'raisecomFanSpeedAbnormal':raisecomFanSpeedAbnormal,'raisecomFanCardUp':raisecomFanCardUp,'raisecomFanCardDown':raisecomFanCardDown,'raisecomFanMonitorMibObjects':raisecomFanMonitorMibObjects,'raisecomFanMonitorGlobalGroup':raisecomFanMonitorGlobalGroup,'raisecomFanMonitorMode':raisecomFanMonitorMode,'raisecomFanMonitorSpdLevel':raisecomFanMonitorSpdLevel,'raisecomFanMonitorNumber':raisecomFanMonitorNumber,'raisecomFanMonitorLevlNumber':raisecomFanMonitorLevlNumber,_I:raisecomFanCardState,'raisecomFanCardSerialNumber':raisecomFanCardSerialNumber,'raisecomFanMonitorTrapSendEnable':raisecomFanMonitorTrapSendEnable,'raisecomFanMonitorStateTable':raisecomFanMonitorStateTable,'raisecomFanMonitorStateEntry':raisecomFanMonitorStateEntry,_F:raisecomFanIndex,_H:raisecomFanSpeedValue,'raisecomFanWorkState':raisecomFanWorkState,'raisecomFanSpeedLevelTable':raisecomFanSpeedLevelTable,'raisecomFanSpeedLevelEntry':raisecomFanSpeedLevelEntry,_K:raisecomFanSpeedLevelIndex,_L:raisecomFanSpeedDueValue,'raisecomFanSpeedTemperatureScale':raisecomFanSpeedTemperatureScale})