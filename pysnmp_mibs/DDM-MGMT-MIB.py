_P='accessible-for-notify'
_O='warning'
_N='swDdmActionType'
_M='swDdmThresholdExceedOrRecover'
_L='swDdmThresholdExceedType'
_K='other'
_J='swDdmThresholdType'
_I='obsolete'
_H='disabled'
_G='enabled'
_F='swDdmPort'
_E='read-only'
_D='read-write'
_C='Integer32'
_B='DDM-MGMT-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
dlink_common_mgmt,=mibBuilder.importSymbols('DLINK-ID-REC-MIB','dlink-common-mgmt')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB','SnmpAdminString')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
swDdmMIB=ModuleIdentity((1,3,6,1,4,1,171,12,72))
_SwDdmCtrl_ObjectIdentity=ObjectIdentity
swDdmCtrl=_SwDdmCtrl_ObjectIdentity((1,3,6,1,4,1,171,12,72,1))
class _SwDdmTrapState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_SwDdmTrapState_Type.__name__=_C
_SwDdmTrapState_Object=MibScalar
swDdmTrapState=_SwDdmTrapState_Object((1,3,6,1,4,1,171,12,72,1,1),_SwDdmTrapState_Type())
swDdmTrapState.setMaxAccess(_D)
if mibBuilder.loadTexts:swDdmTrapState.setStatus(_A)
class _SwDdmLogState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_SwDdmLogState_Type.__name__=_C
_SwDdmLogState_Object=MibScalar
swDdmLogState=_SwDdmLogState_Object((1,3,6,1,4,1,171,12,72,1,2),_SwDdmLogState_Type())
swDdmLogState.setMaxAccess(_D)
if mibBuilder.loadTexts:swDdmLogState.setStatus(_A)
class _SwDdmPowerUnit_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('mw',1),('dbm',2)))
_SwDdmPowerUnit_Type.__name__=_C
_SwDdmPowerUnit_Object=MibScalar
swDdmPowerUnit=_SwDdmPowerUnit_Object((1,3,6,1,4,1,171,12,72,1,3),_SwDdmPowerUnit_Type())
swDdmPowerUnit.setMaxAccess(_D)
if mibBuilder.loadTexts:swDdmPowerUnit.setStatus(_A)
_SwDdmInfo_ObjectIdentity=ObjectIdentity
swDdmInfo=_SwDdmInfo_ObjectIdentity((1,3,6,1,4,1,171,12,72,2))
_SwDdmStatus_ObjectIdentity=ObjectIdentity
swDdmStatus=_SwDdmStatus_ObjectIdentity((1,3,6,1,4,1,171,12,72,2,1))
_SwDdmStatusTable_Object=MibTable
swDdmStatusTable=_SwDdmStatusTable_Object((1,3,6,1,4,1,171,12,72,2,1,1))
if mibBuilder.loadTexts:swDdmStatusTable.setStatus(_A)
_SwDdmStatusEntry_Object=MibTableRow
swDdmStatusEntry=_SwDdmStatusEntry_Object((1,3,6,1,4,1,171,12,72,2,1,1,1))
swDdmStatusEntry.setIndexNames((0,_B,_F))
if mibBuilder.loadTexts:swDdmStatusEntry.setStatus(_A)
class _SwDdmPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_SwDdmPort_Type.__name__=_C
_SwDdmPort_Object=MibTableColumn
swDdmPort=_SwDdmPort_Object((1,3,6,1,4,1,171,12,72,2,1,1,1,1),_SwDdmPort_Type())
swDdmPort.setMaxAccess(_E)
if mibBuilder.loadTexts:swDdmPort.setStatus(_A)
_SwDdmTemperature_Type=DisplayString
_SwDdmTemperature_Object=MibTableColumn
swDdmTemperature=_SwDdmTemperature_Object((1,3,6,1,4,1,171,12,72,2,1,1,1,2),_SwDdmTemperature_Type())
swDdmTemperature.setMaxAccess(_E)
if mibBuilder.loadTexts:swDdmTemperature.setStatus(_A)
_SwDdmVoltage_Type=DisplayString
_SwDdmVoltage_Object=MibTableColumn
swDdmVoltage=_SwDdmVoltage_Object((1,3,6,1,4,1,171,12,72,2,1,1,1,3),_SwDdmVoltage_Type())
swDdmVoltage.setMaxAccess(_E)
if mibBuilder.loadTexts:swDdmVoltage.setStatus(_A)
_SwDdmBiasCurrent_Type=DisplayString
_SwDdmBiasCurrent_Object=MibTableColumn
swDdmBiasCurrent=_SwDdmBiasCurrent_Object((1,3,6,1,4,1,171,12,72,2,1,1,1,4),_SwDdmBiasCurrent_Type())
swDdmBiasCurrent.setMaxAccess(_E)
if mibBuilder.loadTexts:swDdmBiasCurrent.setStatus(_A)
_SwDdmTxPower_Type=DisplayString
_SwDdmTxPower_Object=MibTableColumn
swDdmTxPower=_SwDdmTxPower_Object((1,3,6,1,4,1,171,12,72,2,1,1,1,5),_SwDdmTxPower_Type())
swDdmTxPower.setMaxAccess(_E)
if mibBuilder.loadTexts:swDdmTxPower.setStatus(_A)
_SwDdmRxPower_Type=DisplayString
_SwDdmRxPower_Object=MibTableColumn
swDdmRxPower=_SwDdmRxPower_Object((1,3,6,1,4,1,171,12,72,2,1,1,1,6),_SwDdmRxPower_Type())
swDdmRxPower.setMaxAccess(_E)
if mibBuilder.loadTexts:swDdmRxPower.setStatus(_A)
_SwDdmMgmt_ObjectIdentity=ObjectIdentity
swDdmMgmt=_SwDdmMgmt_ObjectIdentity((1,3,6,1,4,1,171,12,72,3))
_SwDdmThresholdMgmt_ObjectIdentity=ObjectIdentity
swDdmThresholdMgmt=_SwDdmThresholdMgmt_ObjectIdentity((1,3,6,1,4,1,171,12,72,3,1))
_SwDdmThresholdMgmtTable_Object=MibTable
swDdmThresholdMgmtTable=_SwDdmThresholdMgmtTable_Object((1,3,6,1,4,1,171,12,72,3,1,1))
if mibBuilder.loadTexts:swDdmThresholdMgmtTable.setStatus(_A)
_SwDdmThresholdMgmtEntry_Object=MibTableRow
swDdmThresholdMgmtEntry=_SwDdmThresholdMgmtEntry_Object((1,3,6,1,4,1,171,12,72,3,1,1,1))
swDdmThresholdMgmtEntry.setIndexNames((0,_B,_F),(0,_B,_J))
if mibBuilder.loadTexts:swDdmThresholdMgmtEntry.setStatus(_A)
class _SwDdmThresholdType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('temperature',1),('voltage',2),('bias',3),('txPower',4),('rxPower',5)))
_SwDdmThresholdType_Type.__name__=_C
_SwDdmThresholdType_Object=MibTableColumn
swDdmThresholdType=_SwDdmThresholdType_Object((1,3,6,1,4,1,171,12,72,3,1,1,1,1),_SwDdmThresholdType_Type())
swDdmThresholdType.setMaxAccess(_E)
if mibBuilder.loadTexts:swDdmThresholdType.setStatus(_A)
_SwDdmHighAlarm_Type=DisplayString
_SwDdmHighAlarm_Object=MibTableColumn
swDdmHighAlarm=_SwDdmHighAlarm_Object((1,3,6,1,4,1,171,12,72,3,1,1,1,2),_SwDdmHighAlarm_Type())
swDdmHighAlarm.setMaxAccess(_D)
if mibBuilder.loadTexts:swDdmHighAlarm.setStatus(_A)
_SwDdmLowAlarm_Type=DisplayString
_SwDdmLowAlarm_Object=MibTableColumn
swDdmLowAlarm=_SwDdmLowAlarm_Object((1,3,6,1,4,1,171,12,72,3,1,1,1,3),_SwDdmLowAlarm_Type())
swDdmLowAlarm.setMaxAccess(_D)
if mibBuilder.loadTexts:swDdmLowAlarm.setStatus(_A)
_SwDdmHighWarning_Type=DisplayString
_SwDdmHighWarning_Object=MibTableColumn
swDdmHighWarning=_SwDdmHighWarning_Object((1,3,6,1,4,1,171,12,72,3,1,1,1,4),_SwDdmHighWarning_Type())
swDdmHighWarning.setMaxAccess(_D)
if mibBuilder.loadTexts:swDdmHighWarning.setStatus(_A)
_SwDdmLowWarning_Type=DisplayString
_SwDdmLowWarning_Object=MibTableColumn
swDdmLowWarning=_SwDdmLowWarning_Object((1,3,6,1,4,1,171,12,72,3,1,1,1,5),_SwDdmLowWarning_Type())
swDdmLowWarning.setMaxAccess(_D)
if mibBuilder.loadTexts:swDdmLowWarning.setStatus(_A)
_SwDdmActionMgmt_ObjectIdentity=ObjectIdentity
swDdmActionMgmt=_SwDdmActionMgmt_ObjectIdentity((1,3,6,1,4,1,171,12,72,3,2))
_SwDdmActionMgmtTable_Object=MibTable
swDdmActionMgmtTable=_SwDdmActionMgmtTable_Object((1,3,6,1,4,1,171,12,72,3,2,1))
if mibBuilder.loadTexts:swDdmActionMgmtTable.setStatus(_I)
_SwDdmActionMgmtEntry_Object=MibTableRow
swDdmActionMgmtEntry=_SwDdmActionMgmtEntry_Object((1,3,6,1,4,1,171,12,72,3,2,1,1))
swDdmActionMgmtEntry.setIndexNames((0,_B,_F),(0,_B,_N))
if mibBuilder.loadTexts:swDdmActionMgmtEntry.setStatus(_I)
class _SwDdmActionType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('alarm',1),(_O,2)))
_SwDdmActionType_Type.__name__=_C
_SwDdmActionType_Object=MibTableColumn
swDdmActionType=_SwDdmActionType_Object((1,3,6,1,4,1,171,12,72,3,2,1,1,1),_SwDdmActionType_Type())
swDdmActionType.setMaxAccess(_E)
if mibBuilder.loadTexts:swDdmActionType.setStatus(_I)
class _SwDdmShutdown_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_G,1),(_H,2),(_K,3)))
_SwDdmShutdown_Type.__name__=_C
_SwDdmShutdown_Object=MibTableColumn
swDdmShutdown=_SwDdmShutdown_Object((1,3,6,1,4,1,171,12,72,3,2,1,1,2),_SwDdmShutdown_Type())
swDdmShutdown.setMaxAccess(_D)
if mibBuilder.loadTexts:swDdmShutdown.setStatus(_I)
class _SwDdmTrapAndLog_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_G,1),(_H,2),(_K,3)))
_SwDdmTrapAndLog_Type.__name__=_C
_SwDdmTrapAndLog_Object=MibTableColumn
swDdmTrapAndLog=_SwDdmTrapAndLog_Object((1,3,6,1,4,1,171,12,72,3,2,1,1,3),_SwDdmTrapAndLog_Type())
swDdmTrapAndLog.setMaxAccess(_D)
if mibBuilder.loadTexts:swDdmTrapAndLog.setStatus(_I)
_SwDdmPortMgmtTable_Object=MibTable
swDdmPortMgmtTable=_SwDdmPortMgmtTable_Object((1,3,6,1,4,1,171,12,72,3,2,2))
if mibBuilder.loadTexts:swDdmPortMgmtTable.setStatus(_A)
_SwDdmPortMgmtEntry_Object=MibTableRow
swDdmPortMgmtEntry=_SwDdmPortMgmtEntry_Object((1,3,6,1,4,1,171,12,72,3,2,2,1))
swDdmPortMgmtEntry.setIndexNames((0,_B,_F))
if mibBuilder.loadTexts:swDdmPortMgmtEntry.setStatus(_A)
class _SwDdmPortState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_SwDdmPortState_Type.__name__=_C
_SwDdmPortState_Object=MibTableColumn
swDdmPortState=_SwDdmPortState_Object((1,3,6,1,4,1,171,12,72,3,2,2,1,1),_SwDdmPortState_Type())
swDdmPortState.setMaxAccess(_D)
if mibBuilder.loadTexts:swDdmPortState.setStatus(_A)
class _SwDdmPortShutdown_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('alarm',1),(_O,2),('none',3),(_K,4)))
_SwDdmPortShutdown_Type.__name__=_C
_SwDdmPortShutdown_Object=MibTableColumn
swDdmPortShutdown=_SwDdmPortShutdown_Object((1,3,6,1,4,1,171,12,72,3,2,2,1,2),_SwDdmPortShutdown_Type())
swDdmPortShutdown.setMaxAccess(_D)
if mibBuilder.loadTexts:swDdmPortShutdown.setStatus(_A)
_SwDdmNotify_ObjectIdentity=ObjectIdentity
swDdmNotify=_SwDdmNotify_ObjectIdentity((1,3,6,1,4,1,171,12,72,4))
_SwDdmNotifyPrefix_ObjectIdentity=ObjectIdentity
swDdmNotifyPrefix=_SwDdmNotifyPrefix_ObjectIdentity((1,3,6,1,4,1,171,12,72,4,0))
_SwDdmNotificationBinding_ObjectIdentity=ObjectIdentity
swDdmNotificationBinding=_SwDdmNotificationBinding_ObjectIdentity((1,3,6,1,4,1,171,12,72,4,1))
class _SwDdmThresholdExceedType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('high',1),('low',2)))
_SwDdmThresholdExceedType_Type.__name__=_C
_SwDdmThresholdExceedType_Object=MibScalar
swDdmThresholdExceedType=_SwDdmThresholdExceedType_Object((1,3,6,1,4,1,171,12,72,4,1,1),_SwDdmThresholdExceedType_Type())
swDdmThresholdExceedType.setMaxAccess(_P)
if mibBuilder.loadTexts:swDdmThresholdExceedType.setStatus(_A)
class _SwDdmThresholdExceedOrRecover_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('exceed',1),('recover',2)))
_SwDdmThresholdExceedOrRecover_Type.__name__=_C
_SwDdmThresholdExceedOrRecover_Object=MibScalar
swDdmThresholdExceedOrRecover=_SwDdmThresholdExceedOrRecover_Object((1,3,6,1,4,1,171,12,72,4,1,2),_SwDdmThresholdExceedOrRecover_Type())
swDdmThresholdExceedOrRecover.setMaxAccess(_P)
if mibBuilder.loadTexts:swDdmThresholdExceedOrRecover.setStatus(_A)
swDdmAlarmTrap=NotificationType((1,3,6,1,4,1,171,12,72,4,0,1))
swDdmAlarmTrap.setObjects(*((_B,_F),(_B,_J),(_B,_L),(_B,_M)))
if mibBuilder.loadTexts:swDdmAlarmTrap.setStatus(_A)
swDdmWarningTrap=NotificationType((1,3,6,1,4,1,171,12,72,4,0,2))
swDdmWarningTrap.setObjects(*((_B,_F),(_B,_J),(_B,_L),(_B,_M)))
if mibBuilder.loadTexts:swDdmWarningTrap.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'swDdmMIB':swDdmMIB,'swDdmCtrl':swDdmCtrl,'swDdmTrapState':swDdmTrapState,'swDdmLogState':swDdmLogState,'swDdmPowerUnit':swDdmPowerUnit,'swDdmInfo':swDdmInfo,'swDdmStatus':swDdmStatus,'swDdmStatusTable':swDdmStatusTable,'swDdmStatusEntry':swDdmStatusEntry,_F:swDdmPort,'swDdmTemperature':swDdmTemperature,'swDdmVoltage':swDdmVoltage,'swDdmBiasCurrent':swDdmBiasCurrent,'swDdmTxPower':swDdmTxPower,'swDdmRxPower':swDdmRxPower,'swDdmMgmt':swDdmMgmt,'swDdmThresholdMgmt':swDdmThresholdMgmt,'swDdmThresholdMgmtTable':swDdmThresholdMgmtTable,'swDdmThresholdMgmtEntry':swDdmThresholdMgmtEntry,_J:swDdmThresholdType,'swDdmHighAlarm':swDdmHighAlarm,'swDdmLowAlarm':swDdmLowAlarm,'swDdmHighWarning':swDdmHighWarning,'swDdmLowWarning':swDdmLowWarning,'swDdmActionMgmt':swDdmActionMgmt,'swDdmActionMgmtTable':swDdmActionMgmtTable,'swDdmActionMgmtEntry':swDdmActionMgmtEntry,_N:swDdmActionType,'swDdmShutdown':swDdmShutdown,'swDdmTrapAndLog':swDdmTrapAndLog,'swDdmPortMgmtTable':swDdmPortMgmtTable,'swDdmPortMgmtEntry':swDdmPortMgmtEntry,'swDdmPortState':swDdmPortState,'swDdmPortShutdown':swDdmPortShutdown,'swDdmNotify':swDdmNotify,'swDdmNotifyPrefix':swDdmNotifyPrefix,'swDdmAlarmTrap':swDdmAlarmTrap,'swDdmWarningTrap':swDdmWarningTrap,'swDdmNotificationBinding':swDdmNotificationBinding,_L:swDdmThresholdExceedType,_M:swDdmThresholdExceedOrRecover})