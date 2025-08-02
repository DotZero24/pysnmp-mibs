_a='rbnMcLagNotificationGroup'
_Z='rbnMcLagObjectGroup'
_Y='rbnMcLagConstituentPortDown'
_X='rbnMcLagConstituentPortUp'
_W='rbnMcLagOperFailureCleared'
_V='rbnMcLagOperFailed'
_U='rbnMcLagSwitchOverEvent'
_T='rbnMcLagSwitchOverTime'
_S='rbnMcLagRevertiveHoldTimer'
_R='rbnMcLagRevertiveMode'
_Q='rbnMcLagSystemMacAddress'
_P='rbnMcLagSystemPriority'
_O='rbnMcLagId'
_N='rbnMcLagConstituentPort'
_M='rbnMcLagConstituentSlot'
_L='SnmpAdminString'
_K='rbnMcLagSwitchOverReason'
_J='rbnMcLagOperErrorCode'
_I='not-accessible'
_H='rbnMcLagName'
_G='Integer32'
_F='rbnMcLagConstituentPortIfIndex'
_E='rbnMcLagConstituentPortPriority'
_D='rbnMcLagOperState'
_C='read-only'
_B='current'
_A='RBN-LAG-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
InterfaceIndexOrZero,=mibBuilder.importSymbols('IF-MIB','InterfaceIndexOrZero')
rbnMgmt,=mibBuilder.importSymbols('RBN-SMI','rbnMgmt')
RbnPort,RbnSlot=mibBuilder.importSymbols('RBN-TC','RbnPort','RbnSlot')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB',_L)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_G,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DateAndTime,DisplayString,MacAddress,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime','DisplayString','MacAddress','PhysAddress','TextualConvention','TruthValue')
rbnMcLagMIB=ModuleIdentity((1,3,6,1,4,1,2352,2,102))
if mibBuilder.loadTexts:rbnMcLagMIB.setRevisions(('2012-06-01 18:00',))
_RbnMcLagNotifications_ObjectIdentity=ObjectIdentity
rbnMcLagNotifications=_RbnMcLagNotifications_ObjectIdentity((1,3,6,1,4,1,2352,2,102,0))
_RbnMcLagObjects_ObjectIdentity=ObjectIdentity
rbnMcLagObjects=_RbnMcLagObjects_ObjectIdentity((1,3,6,1,4,1,2352,2,102,1))
_RbnMcLagTable_Object=MibTable
rbnMcLagTable=_RbnMcLagTable_Object((1,3,6,1,4,1,2352,2,102,1,1))
if mibBuilder.loadTexts:rbnMcLagTable.setStatus(_B)
_RbnMcLagEntry_Object=MibTableRow
rbnMcLagEntry=_RbnMcLagEntry_Object((1,3,6,1,4,1,2352,2,102,1,1,1))
rbnMcLagEntry.setIndexNames((0,_A,_H))
if mibBuilder.loadTexts:rbnMcLagEntry.setStatus(_B)
class _RbnMcLagName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,80))
_RbnMcLagName_Type.__name__=_L
_RbnMcLagName_Object=MibTableColumn
rbnMcLagName=_RbnMcLagName_Object((1,3,6,1,4,1,2352,2,102,1,1,1,1),_RbnMcLagName_Type())
rbnMcLagName.setMaxAccess(_I)
if mibBuilder.loadTexts:rbnMcLagName.setStatus(_B)
_RbnMcLagId_Type=Integer32
_RbnMcLagId_Object=MibTableColumn
rbnMcLagId=_RbnMcLagId_Object((1,3,6,1,4,1,2352,2,102,1,1,1,2),_RbnMcLagId_Type())
rbnMcLagId.setMaxAccess(_C)
if mibBuilder.loadTexts:rbnMcLagId.setStatus(_B)
_RbnMcLagSystemPriority_Type=Integer32
_RbnMcLagSystemPriority_Object=MibTableColumn
rbnMcLagSystemPriority=_RbnMcLagSystemPriority_Object((1,3,6,1,4,1,2352,2,102,1,1,1,3),_RbnMcLagSystemPriority_Type())
rbnMcLagSystemPriority.setMaxAccess(_C)
if mibBuilder.loadTexts:rbnMcLagSystemPriority.setStatus(_B)
_RbnMcLagSystemMacAddress_Type=MacAddress
_RbnMcLagSystemMacAddress_Object=MibTableColumn
rbnMcLagSystemMacAddress=_RbnMcLagSystemMacAddress_Object((1,3,6,1,4,1,2352,2,102,1,1,1,4),_RbnMcLagSystemMacAddress_Type())
rbnMcLagSystemMacAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:rbnMcLagSystemMacAddress.setStatus(_B)
_RbnMcLagRevertiveMode_Type=TruthValue
_RbnMcLagRevertiveMode_Object=MibTableColumn
rbnMcLagRevertiveMode=_RbnMcLagRevertiveMode_Object((1,3,6,1,4,1,2352,2,102,1,1,1,5),_RbnMcLagRevertiveMode_Type())
rbnMcLagRevertiveMode.setMaxAccess(_C)
if mibBuilder.loadTexts:rbnMcLagRevertiveMode.setStatus(_B)
_RbnMcLagRevertiveHoldTimer_Type=Integer32
_RbnMcLagRevertiveHoldTimer_Object=MibTableColumn
rbnMcLagRevertiveHoldTimer=_RbnMcLagRevertiveHoldTimer_Object((1,3,6,1,4,1,2352,2,102,1,1,1,6),_RbnMcLagRevertiveHoldTimer_Type())
rbnMcLagRevertiveHoldTimer.setMaxAccess(_C)
if mibBuilder.loadTexts:rbnMcLagRevertiveHoldTimer.setStatus(_B)
if mibBuilder.loadTexts:rbnMcLagRevertiveHoldTimer.setUnits('seconds')
class _RbnMcLagOperState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('up',1),('down',2),('standby',3)))
_RbnMcLagOperState_Type.__name__=_G
_RbnMcLagOperState_Object=MibTableColumn
rbnMcLagOperState=_RbnMcLagOperState_Object((1,3,6,1,4,1,2352,2,102,1,1,1,7),_RbnMcLagOperState_Type())
rbnMcLagOperState.setMaxAccess(_C)
if mibBuilder.loadTexts:rbnMcLagOperState.setStatus(_B)
class _RbnMcLagOperErrorCode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*(('noError',0),('configMismatch',1),('priorityError',2),('downMinLink',3)))
_RbnMcLagOperErrorCode_Type.__name__=_G
_RbnMcLagOperErrorCode_Object=MibTableColumn
rbnMcLagOperErrorCode=_RbnMcLagOperErrorCode_Object((1,3,6,1,4,1,2352,2,102,1,1,1,8),_RbnMcLagOperErrorCode_Type())
rbnMcLagOperErrorCode.setMaxAccess(_C)
if mibBuilder.loadTexts:rbnMcLagOperErrorCode.setStatus(_B)
_RbnMcLagSwitchOverTime_Type=DateAndTime
_RbnMcLagSwitchOverTime_Object=MibTableColumn
rbnMcLagSwitchOverTime=_RbnMcLagSwitchOverTime_Object((1,3,6,1,4,1,2352,2,102,1,1,1,9),_RbnMcLagSwitchOverTime_Type())
rbnMcLagSwitchOverTime.setMaxAccess(_C)
if mibBuilder.loadTexts:rbnMcLagSwitchOverTime.setStatus(_B)
_RbnMcLagSwitchOverReason_Type=SnmpAdminString
_RbnMcLagSwitchOverReason_Object=MibTableColumn
rbnMcLagSwitchOverReason=_RbnMcLagSwitchOverReason_Object((1,3,6,1,4,1,2352,2,102,1,1,1,10),_RbnMcLagSwitchOverReason_Type())
rbnMcLagSwitchOverReason.setMaxAccess(_C)
if mibBuilder.loadTexts:rbnMcLagSwitchOverReason.setStatus(_B)
_RbnMcLagConstituentTable_Object=MibTable
rbnMcLagConstituentTable=_RbnMcLagConstituentTable_Object((1,3,6,1,4,1,2352,2,102,1,2))
if mibBuilder.loadTexts:rbnMcLagConstituentTable.setStatus(_B)
_RbnMcLagConstituentEntry_Object=MibTableRow
rbnMcLagConstituentEntry=_RbnMcLagConstituentEntry_Object((1,3,6,1,4,1,2352,2,102,1,2,1))
rbnMcLagConstituentEntry.setIndexNames((0,_A,_H),(0,_A,_M),(0,_A,_N))
if mibBuilder.loadTexts:rbnMcLagConstituentEntry.setStatus(_B)
_RbnMcLagConstituentSlot_Type=RbnSlot
_RbnMcLagConstituentSlot_Object=MibTableColumn
rbnMcLagConstituentSlot=_RbnMcLagConstituentSlot_Object((1,3,6,1,4,1,2352,2,102,1,2,1,1),_RbnMcLagConstituentSlot_Type())
rbnMcLagConstituentSlot.setMaxAccess(_I)
if mibBuilder.loadTexts:rbnMcLagConstituentSlot.setStatus(_B)
_RbnMcLagConstituentPort_Type=RbnPort
_RbnMcLagConstituentPort_Object=MibTableColumn
rbnMcLagConstituentPort=_RbnMcLagConstituentPort_Object((1,3,6,1,4,1,2352,2,102,1,2,1,2),_RbnMcLagConstituentPort_Type())
rbnMcLagConstituentPort.setMaxAccess(_I)
if mibBuilder.loadTexts:rbnMcLagConstituentPort.setStatus(_B)
_RbnMcLagConstituentPortPriority_Type=Integer32
_RbnMcLagConstituentPortPriority_Object=MibTableColumn
rbnMcLagConstituentPortPriority=_RbnMcLagConstituentPortPriority_Object((1,3,6,1,4,1,2352,2,102,1,2,1,3),_RbnMcLagConstituentPortPriority_Type())
rbnMcLagConstituentPortPriority.setMaxAccess(_C)
if mibBuilder.loadTexts:rbnMcLagConstituentPortPriority.setStatus(_B)
_RbnMcLagConstituentPortIfIndex_Type=InterfaceIndexOrZero
_RbnMcLagConstituentPortIfIndex_Object=MibTableColumn
rbnMcLagConstituentPortIfIndex=_RbnMcLagConstituentPortIfIndex_Object((1,3,6,1,4,1,2352,2,102,1,2,1,4),_RbnMcLagConstituentPortIfIndex_Type())
rbnMcLagConstituentPortIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:rbnMcLagConstituentPortIfIndex.setStatus(_B)
_RbnMcLagConformance_ObjectIdentity=ObjectIdentity
rbnMcLagConformance=_RbnMcLagConformance_ObjectIdentity((1,3,6,1,4,1,2352,2,102,2))
_RbnMcLagGroups_ObjectIdentity=ObjectIdentity
rbnMcLagGroups=_RbnMcLagGroups_ObjectIdentity((1,3,6,1,4,1,2352,2,102,2,1))
_RbnMcLagCompliances_ObjectIdentity=ObjectIdentity
rbnMcLagCompliances=_RbnMcLagCompliances_ObjectIdentity((1,3,6,1,4,1,2352,2,102,2,2))
rbnMcLagObjectGroup=ObjectGroup((1,3,6,1,4,1,2352,2,102,2,1,1))
rbnMcLagObjectGroup.setObjects(*((_A,_O),(_A,_P),(_A,_Q),(_A,_R),(_A,_S),(_A,_D),(_A,_J),(_A,_T),(_A,_K),(_A,_E),(_A,_F)))
if mibBuilder.loadTexts:rbnMcLagObjectGroup.setStatus(_B)
rbnMcLagSwitchOverEvent=NotificationType((1,3,6,1,4,1,2352,2,102,0,1))
rbnMcLagSwitchOverEvent.setObjects(*((_A,_D),(_A,_K)))
if mibBuilder.loadTexts:rbnMcLagSwitchOverEvent.setStatus(_B)
rbnMcLagOperFailed=NotificationType((1,3,6,1,4,1,2352,2,102,0,2))
rbnMcLagOperFailed.setObjects(*((_A,_D),(_A,_J)))
if mibBuilder.loadTexts:rbnMcLagOperFailed.setStatus(_B)
rbnMcLagOperFailureCleared=NotificationType((1,3,6,1,4,1,2352,2,102,0,3))
rbnMcLagOperFailureCleared.setObjects((_A,_D))
if mibBuilder.loadTexts:rbnMcLagOperFailureCleared.setStatus(_B)
rbnMcLagConstituentPortUp=NotificationType((1,3,6,1,4,1,2352,2,102,0,4))
rbnMcLagConstituentPortUp.setObjects(*((_A,_E),(_A,_F)))
if mibBuilder.loadTexts:rbnMcLagConstituentPortUp.setStatus(_B)
rbnMcLagConstituentPortDown=NotificationType((1,3,6,1,4,1,2352,2,102,0,5))
rbnMcLagConstituentPortDown.setObjects(*((_A,_E),(_A,_F)))
if mibBuilder.loadTexts:rbnMcLagConstituentPortDown.setStatus(_B)
rbnMcLagNotificationGroup=NotificationGroup((1,3,6,1,4,1,2352,2,102,2,1,2))
rbnMcLagNotificationGroup.setObjects(*((_A,_U),(_A,_V),(_A,_W),(_A,_X),(_A,_Y)))
if mibBuilder.loadTexts:rbnMcLagNotificationGroup.setStatus(_B)
rbnMcLagModuleCompliance=ModuleCompliance((1,3,6,1,4,1,2352,2,102,2,2,1))
rbnMcLagModuleCompliance.setObjects(*((_A,_Z),(_A,_a)))
if mibBuilder.loadTexts:rbnMcLagModuleCompliance.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'rbnMcLagMIB':rbnMcLagMIB,'rbnMcLagNotifications':rbnMcLagNotifications,_U:rbnMcLagSwitchOverEvent,_V:rbnMcLagOperFailed,_W:rbnMcLagOperFailureCleared,_X:rbnMcLagConstituentPortUp,_Y:rbnMcLagConstituentPortDown,'rbnMcLagObjects':rbnMcLagObjects,'rbnMcLagTable':rbnMcLagTable,'rbnMcLagEntry':rbnMcLagEntry,_H:rbnMcLagName,_O:rbnMcLagId,_P:rbnMcLagSystemPriority,_Q:rbnMcLagSystemMacAddress,_R:rbnMcLagRevertiveMode,_S:rbnMcLagRevertiveHoldTimer,_D:rbnMcLagOperState,_J:rbnMcLagOperErrorCode,_T:rbnMcLagSwitchOverTime,_K:rbnMcLagSwitchOverReason,'rbnMcLagConstituentTable':rbnMcLagConstituentTable,'rbnMcLagConstituentEntry':rbnMcLagConstituentEntry,_M:rbnMcLagConstituentSlot,_N:rbnMcLagConstituentPort,_E:rbnMcLagConstituentPortPriority,_F:rbnMcLagConstituentPortIfIndex,'rbnMcLagConformance':rbnMcLagConformance,'rbnMcLagGroups':rbnMcLagGroups,_Z:rbnMcLagObjectGroup,_a:rbnMcLagNotificationGroup,'rbnMcLagCompliances':rbnMcLagCompliances,'rbnMcLagModuleCompliance':rbnMcLagModuleCompliance})