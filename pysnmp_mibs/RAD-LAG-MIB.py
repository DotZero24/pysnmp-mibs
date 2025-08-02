_U='lagMinimumLinks'
_T='dot3adAggPortXEntry'
_S='read-only'
_R='not-accessible'
_Q='lagCnfgIdx'
_P='lagIdx'
_O='deprecated'
_N='Unsigned32'
_M='RAD-LAG-MIB'
_L='Integer32'
_K='alarmEventReason'
_J='alarmEventLogSourceName'
_I='alarmEventLogSeverity'
_H='alarmEventLogDescription'
_G='alarmEventLogDateAndTime'
_F='alarmEventLogAlarmOrEventId'
_E='ifAlias'
_D='IF-MIB'
_C='read-create'
_B='current'
_A='RAD-GEN-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
dot3adAggPortEntry,=mibBuilder.importSymbols('IEEE8023-LAG-MIB','dot3adAggPortEntry')
InterfaceIndexOrZero,ifAlias=mibBuilder.importSymbols(_D,'InterfaceIndexOrZero',_E)
PortList,=mibBuilder.importSymbols('Q-BRIDGE-MIB','PortList')
alarmEventLogAlarmOrEventId,alarmEventLogDateAndTime,alarmEventLogDescription,alarmEventLogSeverity,alarmEventLogSourceName,alarmEventReason=mibBuilder.importSymbols(_A,_F,_G,_H,_I,_J,_K)
agnt,=mibBuilder.importSymbols('RAD-SMI-MIB','agnt')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB','SnmpAdminString')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_L,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_N,'iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention')
lag=ModuleIdentity((1,3,6,1,4,1,164,6,2,54))
_LagEvents_ObjectIdentity=ObjectIdentity
lagEvents=_LagEvents_ObjectIdentity((1,3,6,1,4,1,164,6,2,54,0))
_LagTable_Object=MibTable
lagTable=_LagTable_Object((1,3,6,1,4,1,164,6,2,54,1))
if mibBuilder.loadTexts:lagTable.setStatus(_B)
_LagEntry_Object=MibTableRow
lagEntry=_LagEntry_Object((1,3,6,1,4,1,164,6,2,54,1,1))
lagEntry.setIndexNames((0,_M,_Q),(0,_M,_P))
if mibBuilder.loadTexts:lagEntry.setStatus(_B)
class _LagCnfgIdx_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_LagCnfgIdx_Type.__name__=_N
_LagCnfgIdx_Object=MibTableColumn
lagCnfgIdx=_LagCnfgIdx_Object((1,3,6,1,4,1,164,6,2,54,1,1,1),_LagCnfgIdx_Type())
lagCnfgIdx.setMaxAccess(_R)
if mibBuilder.loadTexts:lagCnfgIdx.setStatus(_B)
_LagIdx_Type=Unsigned32
_LagIdx_Object=MibTableColumn
lagIdx=_LagIdx_Object((1,3,6,1,4,1,164,6,2,54,1,1,2),_LagIdx_Type())
lagIdx.setMaxAccess(_R)
if mibBuilder.loadTexts:lagIdx.setStatus(_B)
_LagPortMembers_Type=PortList
_LagPortMembers_Object=MibTableColumn
lagPortMembers=_LagPortMembers_Object((1,3,6,1,4,1,164,6,2,54,1,1,3),_LagPortMembers_Type())
lagPortMembers.setMaxAccess(_C)
if mibBuilder.loadTexts:lagPortMembers.setStatus(_B)
class _LagDistributionMethod_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(2,3,4,5,6,7,8,9,10,11,12)));namedValues=NamedValues(*(('portBased',2),('oneToOne',3),('sourceMac',4),('destinationMac',5),('sourceXorDestinationMac',6),('sourceAndDestinationMac',7),('sourceIp',8),('destinationIp',9),('sourceAndDestinationMacAndIp',10),('roundRobin',11),('sourceAndDestinationIp',12)))
_LagDistributionMethod_Type.__name__=_L
_LagDistributionMethod_Object=MibTableColumn
lagDistributionMethod=_LagDistributionMethod_Object((1,3,6,1,4,1,164,6,2,54,1,1,4),_LagDistributionMethod_Type())
lagDistributionMethod.setMaxAccess(_C)
if mibBuilder.loadTexts:lagDistributionMethod.setStatus(_B)
class _LagRecoveryMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(2,3)));namedValues=NamedValues(*(('nonRevertive',2),('revertive',3)))
_LagRecoveryMode_Type.__name__=_L
_LagRecoveryMode_Object=MibTableColumn
lagRecoveryMode=_LagRecoveryMode_Object((1,3,6,1,4,1,164,6,2,54,1,1,5),_LagRecoveryMode_Type())
lagRecoveryMode.setMaxAccess(_C)
if mibBuilder.loadTexts:lagRecoveryMode.setStatus(_B)
class _LagWaitToRestore_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,720))
_LagWaitToRestore_Type.__name__=_N
_LagWaitToRestore_Object=MibTableColumn
lagWaitToRestore=_LagWaitToRestore_Object((1,3,6,1,4,1,164,6,2,54,1,1,6),_LagWaitToRestore_Type())
lagWaitToRestore.setMaxAccess(_C)
if mibBuilder.loadTexts:lagWaitToRestore.setStatus(_B)
_LagRowStatus_Type=RowStatus
_LagRowStatus_Object=MibTableColumn
lagRowStatus=_LagRowStatus_Object((1,3,6,1,4,1,164,6,2,54,1,1,7),_LagRowStatus_Type())
lagRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:lagRowStatus.setStatus(_B)
class _LagShutDownDurationUponFlip_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,30))
_LagShutDownDurationUponFlip_Type.__name__=_N
_LagShutDownDurationUponFlip_Object=MibTableColumn
lagShutDownDurationUponFlip=_LagShutDownDurationUponFlip_Object((1,3,6,1,4,1,164,6,2,54,1,1,8),_LagShutDownDurationUponFlip_Type())
lagShutDownDurationUponFlip.setMaxAccess(_C)
if mibBuilder.loadTexts:lagShutDownDurationUponFlip.setStatus(_B)
class _LagRdnMethod_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('loadSharing',1),('redundancy',2)))
_LagRdnMethod_Type.__name__=_L
_LagRdnMethod_Object=MibTableColumn
lagRdnMethod=_LagRdnMethod_Object((1,3,6,1,4,1,164,6,2,54,1,1,9),_LagRdnMethod_Type())
lagRdnMethod.setMaxAccess(_C)
if mibBuilder.loadTexts:lagRdnMethod.setStatus(_B)
class _LagLacpEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(2,3)));namedValues=NamedValues(*(('no',2),('yes',3)))
_LagLacpEnable_Type.__name__=_L
_LagLacpEnable_Object=MibTableColumn
lagLacpEnable=_LagLacpEnable_Object((1,3,6,1,4,1,164,6,2,54,1,1,10),_LagLacpEnable_Type())
lagLacpEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:lagLacpEnable.setStatus(_B)
class _LagMinimumLinks_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4))
_LagMinimumLinks_Type.__name__=_N
_LagMinimumLinks_Object=MibTableColumn
lagMinimumLinks=_LagMinimumLinks_Object((1,3,6,1,4,1,164,6,2,54,1,1,12),_LagMinimumLinks_Type())
lagMinimumLinks.setMaxAccess(_C)
if mibBuilder.loadTexts:lagMinimumLinks.setStatus(_B)
_LagAnchorPort_Type=InterfaceIndexOrZero
_LagAnchorPort_Object=MibTableColumn
lagAnchorPort=_LagAnchorPort_Object((1,3,6,1,4,1,164,6,2,54,1,1,13),_LagAnchorPort_Type())
lagAnchorPort.setMaxAccess(_C)
if mibBuilder.loadTexts:lagAnchorPort.setStatus(_B)
_LagStatTable_Object=MibTable
lagStatTable=_LagStatTable_Object((1,3,6,1,4,1,164,6,2,54,2))
if mibBuilder.loadTexts:lagStatTable.setStatus(_B)
_LagStatEntry_Object=MibTableRow
lagStatEntry=_LagStatEntry_Object((1,3,6,1,4,1,164,6,2,54,2,1))
lagStatEntry.setIndexNames((0,_M,_P))
if mibBuilder.loadTexts:lagStatEntry.setStatus(_B)
_LagStatForcePort_Type=Unsigned32
_LagStatForcePort_Object=MibTableColumn
lagStatForcePort=_LagStatForcePort_Object((1,3,6,1,4,1,164,6,2,54,2,1,1),_LagStatForcePort_Type())
lagStatForcePort.setMaxAccess('read-write')
if mibBuilder.loadTexts:lagStatForcePort.setStatus(_B)
_LagStatActivePort_Type=Unsigned32
_LagStatActivePort_Object=MibTableColumn
lagStatActivePort=_LagStatActivePort_Object((1,3,6,1,4,1,164,6,2,54,2,1,2),_LagStatActivePort_Type())
lagStatActivePort.setMaxAccess(_S)
if mibBuilder.loadTexts:lagStatActivePort.setStatus(_B)
_Dot3adAggPortXTable_Object=MibTable
dot3adAggPortXTable=_Dot3adAggPortXTable_Object((1,3,6,1,4,1,164,6,2,54,3))
if mibBuilder.loadTexts:dot3adAggPortXTable.setStatus(_B)
_Dot3adAggPortXEntry_Object=MibTableRow
dot3adAggPortXEntry=_Dot3adAggPortXEntry_Object((1,3,6,1,4,1,164,6,2,54,3,1))
if mibBuilder.loadTexts:dot3adAggPortXEntry.setStatus(_B)
class _Dot3adAggPortXprotectionState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('notApplicable',1),('standby',2),('active',3)))
_Dot3adAggPortXprotectionState_Type.__name__=_L
_Dot3adAggPortXprotectionState_Object=MibTableColumn
dot3adAggPortXprotectionState=_Dot3adAggPortXprotectionState_Object((1,3,6,1,4,1,164,6,2,54,3,1,1),_Dot3adAggPortXprotectionState_Type())
dot3adAggPortXprotectionState.setMaxAccess(_S)
if mibBuilder.loadTexts:dot3adAggPortXprotectionState.setStatus(_B)
dot3adAggPortEntry.registerAugmentions((_M,_T))
dot3adAggPortXEntry.setIndexNames(*dot3adAggPortEntry.getIndexNames())
lagLacpDown=NotificationType((1,3,6,1,4,1,164,6,2,54,0,1))
lagLacpDown.setObjects(*((_A,_J),(_A,_F),(_A,_H),(_A,_I),(_A,_G),(_A,_K),(_D,_E),(_D,_E)))
if mibBuilder.loadTexts:lagLacpDown.setStatus(_O)
lagLacpLoopDetection=NotificationType((1,3,6,1,4,1,164,6,2,54,0,2))
lagLacpLoopDetection.setObjects(*((_A,_J),(_A,_F),(_A,_H),(_A,_I),(_A,_G),(_A,_K),(_D,_E)))
if mibBuilder.loadTexts:lagLacpLoopDetection.setStatus(_O)
lagLacpChurn=NotificationType((1,3,6,1,4,1,164,6,2,54,0,3))
lagLacpChurn.setObjects(*((_A,_J),(_A,_F),(_A,_H),(_A,_I),(_A,_G),(_A,_K),(_D,_E)))
if mibBuilder.loadTexts:lagLacpChurn.setStatus(_O)
lagSubGroupSwitchover=NotificationType((1,3,6,1,4,1,164,6,2,54,0,4))
lagSubGroupSwitchover.setObjects(*((_A,_J),(_A,_F),(_A,_H),(_A,_I),(_A,_G),(_A,_K),(_D,_E)))
if mibBuilder.loadTexts:lagSubGroupSwitchover.setStatus(_B)
lagFailure=NotificationType((1,3,6,1,4,1,164,6,2,54,0,5))
lagFailure.setObjects(*((_A,_J),(_A,_F),(_A,_H),(_A,_I),(_A,_G),(_A,_K),(_D,_E)))
if mibBuilder.loadTexts:lagFailure.setStatus(_O)
lagMinimumMembers=NotificationType((1,3,6,1,4,1,164,6,2,54,0,6))
lagMinimumMembers.setObjects(*((_A,_J),(_A,_F),(_A,_H),(_A,_I),(_A,_G),(_A,_K),(_D,_E),(_M,_U)))
if mibBuilder.loadTexts:lagMinimumMembers.setStatus(_O)
mibBuilder.exportSymbols(_M,**{'lag':lag,'lagEvents':lagEvents,'lagLacpDown':lagLacpDown,'lagLacpLoopDetection':lagLacpLoopDetection,'lagLacpChurn':lagLacpChurn,'lagSubGroupSwitchover':lagSubGroupSwitchover,'lagFailure':lagFailure,'lagMinimumMembers':lagMinimumMembers,'lagTable':lagTable,'lagEntry':lagEntry,_Q:lagCnfgIdx,_P:lagIdx,'lagPortMembers':lagPortMembers,'lagDistributionMethod':lagDistributionMethod,'lagRecoveryMode':lagRecoveryMode,'lagWaitToRestore':lagWaitToRestore,'lagRowStatus':lagRowStatus,'lagShutDownDurationUponFlip':lagShutDownDurationUponFlip,'lagRdnMethod':lagRdnMethod,'lagLacpEnable':lagLacpEnable,_U:lagMinimumLinks,'lagAnchorPort':lagAnchorPort,'lagStatTable':lagStatTable,'lagStatEntry':lagStatEntry,'lagStatForcePort':lagStatForcePort,'lagStatActivePort':lagStatActivePort,'dot3adAggPortXTable':dot3adAggPortXTable,_T:dot3adAggPortXEntry,'dot3adAggPortXprotectionState':dot3adAggPortXprotectionState})