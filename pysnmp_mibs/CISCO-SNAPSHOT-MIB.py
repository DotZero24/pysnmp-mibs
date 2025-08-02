_a='ciscoSnapshotMIBGroup'
_Z='ciscoSnapshotProtocolsExchanged'
_Y='ciscoSnapshotSourceAddress'
_X='ciscoSnapshotSourceProtocol'
_W='ciscoSnapshotDialerMap'
_V='ciscoSnapshotExchangeTimer'
_U='ciscoSnapshotActivityTimer'
_T='ciscoSnapshotActivityState'
_S='ciscoSnapshotRowStatus'
_R='ciscoSnapshotIfUpAction'
_Q='ciscoSnapshotRetryInterval'
_P='ciscoSnapshotQuietInterval'
_O='ciscoSnapshotActiveInterval'
_N='ciscoSnapshotDialer'
_M='ciscoSnapshotClient'
_L='ciscoSnapshotForceActive'
_K='ciscoSnapshotActivityIndex'
_J='not-accessible'
_I='OctetString'
_H='ciscoSnapshotIfIndex'
_G='TruthValue'
_F='minutes'
_E='read-create'
_D='Integer32'
_C='read-only'
_B='CISCO-SNAPSHOT-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_I,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
CiscoNetworkAddress,CiscoNetworkProtocol=mibBuilder.importSymbols('CISCO-TC','CiscoNetworkAddress','CiscoNetworkProtocol')
InterfaceIndex,=mibBuilder.importSymbols('IF-MIB','InterfaceIndex')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention',_G)
ciscoSnapshotMIB=ModuleIdentity((1,3,6,1,4,1,9,9,19))
if mibBuilder.loadTexts:ciscoSnapshotMIB.setRevisions(('1995-08-15 00:00','1995-03-21 00:00','1995-01-11 00:00'))
_CiscoSnapshotMIBObjects_ObjectIdentity=ObjectIdentity
ciscoSnapshotMIBObjects=_CiscoSnapshotMIBObjects_ObjectIdentity((1,3,6,1,4,1,9,9,19,1))
_CiscoSnapshotForceActive_Type=Integer32
_CiscoSnapshotForceActive_Object=MibScalar
ciscoSnapshotForceActive=_CiscoSnapshotForceActive_Object((1,3,6,1,4,1,9,9,19,1,1),_CiscoSnapshotForceActive_Type())
ciscoSnapshotForceActive.setMaxAccess('read-write')
if mibBuilder.loadTexts:ciscoSnapshotForceActive.setStatus(_A)
_CiscoSnapshotInterfaceTable_Object=MibTable
ciscoSnapshotInterfaceTable=_CiscoSnapshotInterfaceTable_Object((1,3,6,1,4,1,9,9,19,1,2))
if mibBuilder.loadTexts:ciscoSnapshotInterfaceTable.setStatus(_A)
_CiscoSnapshotInterfaceEntry_Object=MibTableRow
ciscoSnapshotInterfaceEntry=_CiscoSnapshotInterfaceEntry_Object((1,3,6,1,4,1,9,9,19,1,2,1))
ciscoSnapshotInterfaceEntry.setIndexNames((0,_B,_H))
if mibBuilder.loadTexts:ciscoSnapshotInterfaceEntry.setStatus(_A)
_CiscoSnapshotIfIndex_Type=InterfaceIndex
_CiscoSnapshotIfIndex_Object=MibTableColumn
ciscoSnapshotIfIndex=_CiscoSnapshotIfIndex_Object((1,3,6,1,4,1,9,9,19,1,2,1,1),_CiscoSnapshotIfIndex_Type())
ciscoSnapshotIfIndex.setMaxAccess(_J)
if mibBuilder.loadTexts:ciscoSnapshotIfIndex.setStatus(_A)
class _CiscoSnapshotClient_Type(TruthValue):defaultValue=1
_CiscoSnapshotClient_Type.__name__=_G
_CiscoSnapshotClient_Object=MibTableColumn
ciscoSnapshotClient=_CiscoSnapshotClient_Object((1,3,6,1,4,1,9,9,19,1,2,1,2),_CiscoSnapshotClient_Type())
ciscoSnapshotClient.setMaxAccess(_E)
if mibBuilder.loadTexts:ciscoSnapshotClient.setStatus(_A)
class _CiscoSnapshotDialer_Type(TruthValue):defaultValue=2
_CiscoSnapshotDialer_Type.__name__=_G
_CiscoSnapshotDialer_Object=MibTableColumn
ciscoSnapshotDialer=_CiscoSnapshotDialer_Object((1,3,6,1,4,1,9,9,19,1,2,1,3),_CiscoSnapshotDialer_Type())
ciscoSnapshotDialer.setMaxAccess(_E)
if mibBuilder.loadTexts:ciscoSnapshotDialer.setStatus(_A)
class _CiscoSnapshotActiveInterval_Type(Integer32):defaultValue=5;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(5,1000))
_CiscoSnapshotActiveInterval_Type.__name__=_D
_CiscoSnapshotActiveInterval_Object=MibTableColumn
ciscoSnapshotActiveInterval=_CiscoSnapshotActiveInterval_Object((1,3,6,1,4,1,9,9,19,1,2,1,4),_CiscoSnapshotActiveInterval_Type())
ciscoSnapshotActiveInterval.setMaxAccess(_E)
if mibBuilder.loadTexts:ciscoSnapshotActiveInterval.setStatus(_A)
if mibBuilder.loadTexts:ciscoSnapshotActiveInterval.setUnits(_F)
class _CiscoSnapshotQuietInterval_Type(Integer32):defaultValue=8;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(8,100000))
_CiscoSnapshotQuietInterval_Type.__name__=_D
_CiscoSnapshotQuietInterval_Object=MibTableColumn
ciscoSnapshotQuietInterval=_CiscoSnapshotQuietInterval_Object((1,3,6,1,4,1,9,9,19,1,2,1,5),_CiscoSnapshotQuietInterval_Type())
ciscoSnapshotQuietInterval.setMaxAccess(_E)
if mibBuilder.loadTexts:ciscoSnapshotQuietInterval.setStatus(_A)
if mibBuilder.loadTexts:ciscoSnapshotQuietInterval.setUnits(_F)
_CiscoSnapshotRetryInterval_Type=Integer32
_CiscoSnapshotRetryInterval_Object=MibTableColumn
ciscoSnapshotRetryInterval=_CiscoSnapshotRetryInterval_Object((1,3,6,1,4,1,9,9,19,1,2,1,6),_CiscoSnapshotRetryInterval_Type())
ciscoSnapshotRetryInterval.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoSnapshotRetryInterval.setStatus(_A)
if mibBuilder.loadTexts:ciscoSnapshotRetryInterval.setUnits(_F)
class _CiscoSnapshotIfUpAction_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('goActive',1),('noAction',2)))
_CiscoSnapshotIfUpAction_Type.__name__=_D
_CiscoSnapshotIfUpAction_Object=MibTableColumn
ciscoSnapshotIfUpAction=_CiscoSnapshotIfUpAction_Object((1,3,6,1,4,1,9,9,19,1,2,1,7),_CiscoSnapshotIfUpAction_Type())
ciscoSnapshotIfUpAction.setMaxAccess(_E)
if mibBuilder.loadTexts:ciscoSnapshotIfUpAction.setStatus(_A)
_CiscoSnapshotRowStatus_Type=RowStatus
_CiscoSnapshotRowStatus_Object=MibTableColumn
ciscoSnapshotRowStatus=_CiscoSnapshotRowStatus_Object((1,3,6,1,4,1,9,9,19,1,2,1,8),_CiscoSnapshotRowStatus_Type())
ciscoSnapshotRowStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:ciscoSnapshotRowStatus.setStatus(_A)
_CiscoSnapshotActivityTable_Object=MibTable
ciscoSnapshotActivityTable=_CiscoSnapshotActivityTable_Object((1,3,6,1,4,1,9,9,19,1,3))
if mibBuilder.loadTexts:ciscoSnapshotActivityTable.setStatus(_A)
_CiscoSnapshotActivityEntry_Object=MibTableRow
ciscoSnapshotActivityEntry=_CiscoSnapshotActivityEntry_Object((1,3,6,1,4,1,9,9,19,1,3,1))
ciscoSnapshotActivityEntry.setIndexNames((0,_B,_H),(0,_B,_K))
if mibBuilder.loadTexts:ciscoSnapshotActivityEntry.setStatus(_A)
class _CiscoSnapshotActivityIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_CiscoSnapshotActivityIndex_Type.__name__=_D
_CiscoSnapshotActivityIndex_Object=MibTableColumn
ciscoSnapshotActivityIndex=_CiscoSnapshotActivityIndex_Object((1,3,6,1,4,1,9,9,19,1,3,1,1),_CiscoSnapshotActivityIndex_Type())
ciscoSnapshotActivityIndex.setMaxAccess(_J)
if mibBuilder.loadTexts:ciscoSnapshotActivityIndex.setStatus(_A)
class _CiscoSnapshotActivityState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*(('active',1),('quiet',2),('serverPostActive',3),('transitionToQuiet',4),('transitionToActive',5),('limbo',6)))
_CiscoSnapshotActivityState_Type.__name__=_D
_CiscoSnapshotActivityState_Object=MibTableColumn
ciscoSnapshotActivityState=_CiscoSnapshotActivityState_Object((1,3,6,1,4,1,9,9,19,1,3,1,2),_CiscoSnapshotActivityState_Type())
ciscoSnapshotActivityState.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoSnapshotActivityState.setStatus(_A)
_CiscoSnapshotActivityTimer_Type=Integer32
_CiscoSnapshotActivityTimer_Object=MibTableColumn
ciscoSnapshotActivityTimer=_CiscoSnapshotActivityTimer_Object((1,3,6,1,4,1,9,9,19,1,3,1,3),_CiscoSnapshotActivityTimer_Type())
ciscoSnapshotActivityTimer.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoSnapshotActivityTimer.setStatus(_A)
if mibBuilder.loadTexts:ciscoSnapshotActivityTimer.setUnits(_F)
_CiscoSnapshotExchangeTimer_Type=Integer32
_CiscoSnapshotExchangeTimer_Object=MibTableColumn
ciscoSnapshotExchangeTimer=_CiscoSnapshotExchangeTimer_Object((1,3,6,1,4,1,9,9,19,1,3,1,4),_CiscoSnapshotExchangeTimer_Type())
ciscoSnapshotExchangeTimer.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoSnapshotExchangeTimer.setStatus(_A)
if mibBuilder.loadTexts:ciscoSnapshotExchangeTimer.setUnits(_F)
_CiscoSnapshotDialerMap_Type=Integer32
_CiscoSnapshotDialerMap_Object=MibTableColumn
ciscoSnapshotDialerMap=_CiscoSnapshotDialerMap_Object((1,3,6,1,4,1,9,9,19,1,3,1,5),_CiscoSnapshotDialerMap_Type())
ciscoSnapshotDialerMap.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoSnapshotDialerMap.setStatus(_A)
_CiscoSnapshotSourceProtocol_Type=CiscoNetworkProtocol
_CiscoSnapshotSourceProtocol_Object=MibTableColumn
ciscoSnapshotSourceProtocol=_CiscoSnapshotSourceProtocol_Object((1,3,6,1,4,1,9,9,19,1,3,1,6),_CiscoSnapshotSourceProtocol_Type())
ciscoSnapshotSourceProtocol.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoSnapshotSourceProtocol.setStatus(_A)
_CiscoSnapshotSourceAddress_Type=CiscoNetworkAddress
_CiscoSnapshotSourceAddress_Object=MibTableColumn
ciscoSnapshotSourceAddress=_CiscoSnapshotSourceAddress_Object((1,3,6,1,4,1,9,9,19,1,3,1,7),_CiscoSnapshotSourceAddress_Type())
ciscoSnapshotSourceAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoSnapshotSourceAddress.setStatus(_A)
class _CiscoSnapshotProtocolsExchanged_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,4))
_CiscoSnapshotProtocolsExchanged_Type.__name__=_I
_CiscoSnapshotProtocolsExchanged_Object=MibTableColumn
ciscoSnapshotProtocolsExchanged=_CiscoSnapshotProtocolsExchanged_Object((1,3,6,1,4,1,9,9,19,1,3,1,8),_CiscoSnapshotProtocolsExchanged_Type())
ciscoSnapshotProtocolsExchanged.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoSnapshotProtocolsExchanged.setStatus(_A)
_CiscoSnapshotMIBConformance_ObjectIdentity=ObjectIdentity
ciscoSnapshotMIBConformance=_CiscoSnapshotMIBConformance_ObjectIdentity((1,3,6,1,4,1,9,9,19,2))
_CiscoSnapshotMIBCompliances_ObjectIdentity=ObjectIdentity
ciscoSnapshotMIBCompliances=_CiscoSnapshotMIBCompliances_ObjectIdentity((1,3,6,1,4,1,9,9,19,2,1))
_CiscoSnapshotMIBGroups_ObjectIdentity=ObjectIdentity
ciscoSnapshotMIBGroups=_CiscoSnapshotMIBGroups_ObjectIdentity((1,3,6,1,4,1,9,9,19,2,2))
ciscoSnapshotMIBGroup=ObjectGroup((1,3,6,1,4,1,9,9,19,2,2,1))
ciscoSnapshotMIBGroup.setObjects(*((_B,_L),(_B,_M),(_B,_N),(_B,_O),(_B,_P),(_B,_Q),(_B,_R),(_B,_S),(_B,_T),(_B,_U),(_B,_V),(_B,_W),(_B,_X),(_B,_Y),(_B,_Z)))
if mibBuilder.loadTexts:ciscoSnapshotMIBGroup.setStatus(_A)
ciscoSnapshotMIBCompliance=ModuleCompliance((1,3,6,1,4,1,9,9,19,2,1,1))
ciscoSnapshotMIBCompliance.setObjects((_B,_a))
if mibBuilder.loadTexts:ciscoSnapshotMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'ciscoSnapshotMIB':ciscoSnapshotMIB,'ciscoSnapshotMIBObjects':ciscoSnapshotMIBObjects,_L:ciscoSnapshotForceActive,'ciscoSnapshotInterfaceTable':ciscoSnapshotInterfaceTable,'ciscoSnapshotInterfaceEntry':ciscoSnapshotInterfaceEntry,_H:ciscoSnapshotIfIndex,_M:ciscoSnapshotClient,_N:ciscoSnapshotDialer,_O:ciscoSnapshotActiveInterval,_P:ciscoSnapshotQuietInterval,_Q:ciscoSnapshotRetryInterval,_R:ciscoSnapshotIfUpAction,_S:ciscoSnapshotRowStatus,'ciscoSnapshotActivityTable':ciscoSnapshotActivityTable,'ciscoSnapshotActivityEntry':ciscoSnapshotActivityEntry,_K:ciscoSnapshotActivityIndex,_T:ciscoSnapshotActivityState,_U:ciscoSnapshotActivityTimer,_V:ciscoSnapshotExchangeTimer,_W:ciscoSnapshotDialerMap,_X:ciscoSnapshotSourceProtocol,_Y:ciscoSnapshotSourceAddress,_Z:ciscoSnapshotProtocolsExchanged,'ciscoSnapshotMIBConformance':ciscoSnapshotMIBConformance,'ciscoSnapshotMIBCompliances':ciscoSnapshotMIBCompliances,'ciscoSnapshotMIBCompliance':ciscoSnapshotMIBCompliance,'ciscoSnapshotMIBGroups':ciscoSnapshotMIBGroups,_a:ciscoSnapshotMIBGroup})