_Y='agentDot1xAuthHistoryResultIfIndex'
_X='agentDot1xAuthHistoryResultIndex'
_W='agentDot1xAuthHistoryResultIfaceIndex'
_V='success'
_U='initialize'
_T='agentDot1xClientMacAddress'
_S='Dot1xSessionTerminationAction'
_R='notAssigned'
_Q='voiceVlan'
_P='guestVlan'
_O='Dot1xPortControlMode'
_N='dot1xPaePortNumber'
_M='IEEE8021-PAE-MIB'
_L='monitorVlan'
_K='unauthenticatedVlan'
_J='radius'
_I='default'
_H='NETAPP-DOT1X-ADVANCED-FEATURES-MIB'
_G='Unsigned32'
_F='disable'
_E='enable'
_D='read-write'
_C='Integer32'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
dot1xPaePortNumber,=mibBuilder.importSymbols(_M,_N)
fastPath,=mibBuilder.importSymbols('NETAPP-REF-MIB','fastPath')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_G,'iso')
DateAndTime,DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime','DisplayString','MacAddress','PhysAddress','RowStatus','TextualConvention')
fastPathdot1xAdvanced=ModuleIdentity((1,3,6,1,4,1,789,4413,1,1,36))
if mibBuilder.loadTexts:fastPathdot1xAdvanced.setRevisions(('2011-01-26 00:00','2007-05-23 00:00'))
class Dot1xPortControlMode(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('forceUnauthorized',1),('auto',2),('forceAuthorized',3),('macBased',4)))
class Dot1xSessionTerminationAction(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_I,1),('reauthenticate',2)))
_AgentDot1xEnhancementConfigGroup_ObjectIdentity=ObjectIdentity
agentDot1xEnhancementConfigGroup=_AgentDot1xEnhancementConfigGroup_ObjectIdentity((1,3,6,1,4,1,789,4413,1,1,36,1))
class _AgentDot1xRadiusVlanAssignment_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_AgentDot1xRadiusVlanAssignment_Type.__name__=_C
_AgentDot1xRadiusVlanAssignment_Object=MibScalar
agentDot1xRadiusVlanAssignment=_AgentDot1xRadiusVlanAssignment_Object((1,3,6,1,4,1,789,4413,1,1,36,1,1),_AgentDot1xRadiusVlanAssignment_Type())
agentDot1xRadiusVlanAssignment.setMaxAccess(_D)
if mibBuilder.loadTexts:agentDot1xRadiusVlanAssignment.setStatus(_A)
class _AgentDot1xDynamicVlanCreationMode_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_AgentDot1xDynamicVlanCreationMode_Type.__name__=_C
_AgentDot1xDynamicVlanCreationMode_Object=MibScalar
agentDot1xDynamicVlanCreationMode=_AgentDot1xDynamicVlanCreationMode_Object((1,3,6,1,4,1,789,4413,1,1,36,1,2),_AgentDot1xDynamicVlanCreationMode_Type())
agentDot1xDynamicVlanCreationMode.setMaxAccess(_D)
if mibBuilder.loadTexts:agentDot1xDynamicVlanCreationMode.setStatus(_A)
class _AgentDot1xEapolFloodMode_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_AgentDot1xEapolFloodMode_Type.__name__=_C
_AgentDot1xEapolFloodMode_Object=MibScalar
agentDot1xEapolFloodMode=_AgentDot1xEapolFloodMode_Object((1,3,6,1,4,1,789,4413,1,1,36,1,3),_AgentDot1xEapolFloodMode_Type())
agentDot1xEapolFloodMode.setMaxAccess(_D)
if mibBuilder.loadTexts:agentDot1xEapolFloodMode.setStatus(_A)
_AgentDot1xPortConfigGroup_ObjectIdentity=ObjectIdentity
agentDot1xPortConfigGroup=_AgentDot1xPortConfigGroup_ObjectIdentity((1,3,6,1,4,1,789,4413,1,1,36,2))
_AgentDot1xPortConfigTable_Object=MibTable
agentDot1xPortConfigTable=_AgentDot1xPortConfigTable_Object((1,3,6,1,4,1,789,4413,1,1,36,2,1))
if mibBuilder.loadTexts:agentDot1xPortConfigTable.setStatus(_A)
_AgentDot1xPortConfigEntry_Object=MibTableRow
agentDot1xPortConfigEntry=_AgentDot1xPortConfigEntry_Object((1,3,6,1,4,1,789,4413,1,1,36,2,1,1))
agentDot1xPortConfigEntry.setIndexNames((0,_M,_N))
if mibBuilder.loadTexts:agentDot1xPortConfigEntry.setStatus(_A)
class _AgentDot1xPortControlMode_Type(Dot1xPortControlMode):defaultValue=2
_AgentDot1xPortControlMode_Type.__name__=_O
_AgentDot1xPortControlMode_Object=MibTableColumn
agentDot1xPortControlMode=_AgentDot1xPortControlMode_Object((1,3,6,1,4,1,789,4413,1,1,36,2,1,1,1),_AgentDot1xPortControlMode_Type())
agentDot1xPortControlMode.setMaxAccess(_D)
if mibBuilder.loadTexts:agentDot1xPortControlMode.setStatus(_A)
class _AgentDot1xGuestVlanId_Type(Unsigned32):defaultValue=0
_AgentDot1xGuestVlanId_Type.__name__=_G
_AgentDot1xGuestVlanId_Object=MibTableColumn
agentDot1xGuestVlanId=_AgentDot1xGuestVlanId_Object((1,3,6,1,4,1,789,4413,1,1,36,2,1,1,2),_AgentDot1xGuestVlanId_Type())
agentDot1xGuestVlanId.setMaxAccess(_D)
if mibBuilder.loadTexts:agentDot1xGuestVlanId.setStatus(_A)
class _AgentDot1xGuestVlanPeriod_Type(Unsigned32):defaultValue=90;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,300))
_AgentDot1xGuestVlanPeriod_Type.__name__=_G
_AgentDot1xGuestVlanPeriod_Object=MibTableColumn
agentDot1xGuestVlanPeriod=_AgentDot1xGuestVlanPeriod_Object((1,3,6,1,4,1,789,4413,1,1,36,2,1,1,3),_AgentDot1xGuestVlanPeriod_Type())
agentDot1xGuestVlanPeriod.setMaxAccess(_D)
if mibBuilder.loadTexts:agentDot1xGuestVlanPeriod.setStatus(_A)
class _AgentDot1xUnauthenticatedVlan_Type(Unsigned32):defaultValue=0
_AgentDot1xUnauthenticatedVlan_Type.__name__=_G
_AgentDot1xUnauthenticatedVlan_Object=MibTableColumn
agentDot1xUnauthenticatedVlan=_AgentDot1xUnauthenticatedVlan_Object((1,3,6,1,4,1,789,4413,1,1,36,2,1,1,4),_AgentDot1xUnauthenticatedVlan_Type())
agentDot1xUnauthenticatedVlan.setMaxAccess(_D)
if mibBuilder.loadTexts:agentDot1xUnauthenticatedVlan.setStatus(_A)
_AgentDot1xMaxUsers_Type=Unsigned32
_AgentDot1xMaxUsers_Object=MibTableColumn
agentDot1xMaxUsers=_AgentDot1xMaxUsers_Object((1,3,6,1,4,1,789,4413,1,1,36,2,1,1,5),_AgentDot1xMaxUsers_Type())
agentDot1xMaxUsers.setMaxAccess(_D)
if mibBuilder.loadTexts:agentDot1xMaxUsers.setStatus(_A)
class _AgentDot1xPortVlanAssigned_Type(Unsigned32):defaultValue=0
_AgentDot1xPortVlanAssigned_Type.__name__=_G
_AgentDot1xPortVlanAssigned_Object=MibTableColumn
agentDot1xPortVlanAssigned=_AgentDot1xPortVlanAssigned_Object((1,3,6,1,4,1,789,4413,1,1,36,2,1,1,6),_AgentDot1xPortVlanAssigned_Type())
agentDot1xPortVlanAssigned.setMaxAccess(_B)
if mibBuilder.loadTexts:agentDot1xPortVlanAssigned.setStatus(_A)
class _AgentDot1xPortVlanAssignedReason_Type(Integer32):defaultValue=5;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*((_I,1),(_J,2),(_K,3),(_P,4),(_Q,5),(_L,6),(_R,7)))
_AgentDot1xPortVlanAssignedReason_Type.__name__=_C
_AgentDot1xPortVlanAssignedReason_Object=MibTableColumn
agentDot1xPortVlanAssignedReason=_AgentDot1xPortVlanAssignedReason_Object((1,3,6,1,4,1,789,4413,1,1,36,2,1,1,7),_AgentDot1xPortVlanAssignedReason_Type())
agentDot1xPortVlanAssignedReason.setMaxAccess(_B)
if mibBuilder.loadTexts:agentDot1xPortVlanAssignedReason.setStatus(_A)
_AgentDot1xPortSessionTimeout_Type=Unsigned32
_AgentDot1xPortSessionTimeout_Object=MibTableColumn
agentDot1xPortSessionTimeout=_AgentDot1xPortSessionTimeout_Object((1,3,6,1,4,1,789,4413,1,1,36,2,1,1,8),_AgentDot1xPortSessionTimeout_Type())
agentDot1xPortSessionTimeout.setMaxAccess(_B)
if mibBuilder.loadTexts:agentDot1xPortSessionTimeout.setStatus(_A)
class _AgentDot1xPortTerminationAction_Type(Dot1xSessionTerminationAction):defaultValue=1
_AgentDot1xPortTerminationAction_Type.__name__=_S
_AgentDot1xPortTerminationAction_Object=MibTableColumn
agentDot1xPortTerminationAction=_AgentDot1xPortTerminationAction_Object((1,3,6,1,4,1,789,4413,1,1,36,2,1,1,9),_AgentDot1xPortTerminationAction_Type())
agentDot1xPortTerminationAction.setMaxAccess(_B)
if mibBuilder.loadTexts:agentDot1xPortTerminationAction.setStatus(_A)
class _AgentDot1xPortMABenabled_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_AgentDot1xPortMABenabled_Type.__name__=_C
_AgentDot1xPortMABenabled_Object=MibTableColumn
agentDot1xPortMABenabled=_AgentDot1xPortMABenabled_Object((1,3,6,1,4,1,789,4413,1,1,36,2,1,1,10),_AgentDot1xPortMABenabled_Type())
agentDot1xPortMABenabled.setMaxAccess(_D)
if mibBuilder.loadTexts:agentDot1xPortMABenabled.setStatus(_A)
class _AgentDot1xPortMABenabledOperational_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_AgentDot1xPortMABenabledOperational_Type.__name__=_C
_AgentDot1xPortMABenabledOperational_Object=MibTableColumn
agentDot1xPortMABenabledOperational=_AgentDot1xPortMABenabledOperational_Object((1,3,6,1,4,1,789,4413,1,1,36,2,1,1,11),_AgentDot1xPortMABenabledOperational_Type())
agentDot1xPortMABenabledOperational.setMaxAccess(_B)
if mibBuilder.loadTexts:agentDot1xPortMABenabledOperational.setStatus(_A)
_AgentDot1xClientConfigGroup_ObjectIdentity=ObjectIdentity
agentDot1xClientConfigGroup=_AgentDot1xClientConfigGroup_ObjectIdentity((1,3,6,1,4,1,789,4413,1,1,36,3))
_AgentDot1xClientConfigTable_Object=MibTable
agentDot1xClientConfigTable=_AgentDot1xClientConfigTable_Object((1,3,6,1,4,1,789,4413,1,1,36,3,1))
if mibBuilder.loadTexts:agentDot1xClientConfigTable.setStatus(_A)
_AgentDot1xClientConfigEntry_Object=MibTableRow
agentDot1xClientConfigEntry=_AgentDot1xClientConfigEntry_Object((1,3,6,1,4,1,789,4413,1,1,36,3,1,1))
agentDot1xClientConfigEntry.setIndexNames((0,_H,_T))
if mibBuilder.loadTexts:agentDot1xClientConfigEntry.setStatus(_A)
_AgentDot1xClientMacAddress_Type=MacAddress
_AgentDot1xClientMacAddress_Object=MibTableColumn
agentDot1xClientMacAddress=_AgentDot1xClientMacAddress_Object((1,3,6,1,4,1,789,4413,1,1,36,3,1,1,1),_AgentDot1xClientMacAddress_Type())
agentDot1xClientMacAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:agentDot1xClientMacAddress.setStatus(_A)
_AgentDot1xLogicalPort_Type=Unsigned32
_AgentDot1xLogicalPort_Object=MibTableColumn
agentDot1xLogicalPort=_AgentDot1xLogicalPort_Object((1,3,6,1,4,1,789,4413,1,1,36,3,1,1,2),_AgentDot1xLogicalPort_Type())
agentDot1xLogicalPort.setMaxAccess(_B)
if mibBuilder.loadTexts:agentDot1xLogicalPort.setStatus(_A)
_AgentDot1xInterface_Type=Unsigned32
_AgentDot1xInterface_Object=MibTableColumn
agentDot1xInterface=_AgentDot1xInterface_Object((1,3,6,1,4,1,789,4413,1,1,36,3,1,1,3),_AgentDot1xInterface_Type())
agentDot1xInterface.setMaxAccess(_B)
if mibBuilder.loadTexts:agentDot1xInterface.setStatus(_A)
class _AgentDot1xClientAuthPAEstate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9)));namedValues=NamedValues(*((_U,1),('disconnected',2),('connecting',3),('authenticating',4),('authenticated',5),('aborting',6),('held',7),('forceAuth',8),('forceUnauth',9)))
_AgentDot1xClientAuthPAEstate_Type.__name__=_C
_AgentDot1xClientAuthPAEstate_Object=MibTableColumn
agentDot1xClientAuthPAEstate=_AgentDot1xClientAuthPAEstate_Object((1,3,6,1,4,1,789,4413,1,1,36,3,1,1,4),_AgentDot1xClientAuthPAEstate_Type())
agentDot1xClientAuthPAEstate.setMaxAccess(_B)
if mibBuilder.loadTexts:agentDot1xClientAuthPAEstate.setStatus(_A)
class _AgentDot1xClientBackendState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*(('request',1),('response',2),(_V,3),('fail',4),('timeout',5),('idle',6),(_U,7)))
_AgentDot1xClientBackendState_Type.__name__=_C
_AgentDot1xClientBackendState_Object=MibTableColumn
agentDot1xClientBackendState=_AgentDot1xClientBackendState_Object((1,3,6,1,4,1,789,4413,1,1,36,3,1,1,5),_AgentDot1xClientBackendState_Type())
agentDot1xClientBackendState.setMaxAccess(_B)
if mibBuilder.loadTexts:agentDot1xClientBackendState.setStatus(_A)
_AgentDot1xClientUserName_Type=DisplayString
_AgentDot1xClientUserName_Object=MibTableColumn
agentDot1xClientUserName=_AgentDot1xClientUserName_Object((1,3,6,1,4,1,789,4413,1,1,36,3,1,1,6),_AgentDot1xClientUserName_Type())
agentDot1xClientUserName.setMaxAccess(_B)
if mibBuilder.loadTexts:agentDot1xClientUserName.setStatus(_A)
_AgentDot1xClientSessionTime_Type=Unsigned32
_AgentDot1xClientSessionTime_Object=MibTableColumn
agentDot1xClientSessionTime=_AgentDot1xClientSessionTime_Object((1,3,6,1,4,1,789,4413,1,1,36,3,1,1,7),_AgentDot1xClientSessionTime_Type())
agentDot1xClientSessionTime.setMaxAccess(_B)
if mibBuilder.loadTexts:agentDot1xClientSessionTime.setStatus(_A)
_AgentDot1xClientFilterID_Type=DisplayString
_AgentDot1xClientFilterID_Object=MibTableColumn
agentDot1xClientFilterID=_AgentDot1xClientFilterID_Object((1,3,6,1,4,1,789,4413,1,1,36,3,1,1,8),_AgentDot1xClientFilterID_Type())
agentDot1xClientFilterID.setMaxAccess(_B)
if mibBuilder.loadTexts:agentDot1xClientFilterID.setStatus(_A)
_AgentDot1xClientVlanAssigned_Type=Unsigned32
_AgentDot1xClientVlanAssigned_Object=MibTableColumn
agentDot1xClientVlanAssigned=_AgentDot1xClientVlanAssigned_Object((1,3,6,1,4,1,789,4413,1,1,36,3,1,1,9),_AgentDot1xClientVlanAssigned_Type())
agentDot1xClientVlanAssigned.setMaxAccess(_B)
if mibBuilder.loadTexts:agentDot1xClientVlanAssigned.setStatus(_A)
class _AgentDot1xClientVlanAssignedReason_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,6,7)));namedValues=NamedValues(*((_I,1),(_J,2),(_K,3),(_L,6),('invalid',7)))
_AgentDot1xClientVlanAssignedReason_Type.__name__=_C
_AgentDot1xClientVlanAssignedReason_Object=MibTableColumn
agentDot1xClientVlanAssignedReason=_AgentDot1xClientVlanAssignedReason_Object((1,3,6,1,4,1,789,4413,1,1,36,3,1,1,10),_AgentDot1xClientVlanAssignedReason_Type())
agentDot1xClientVlanAssignedReason.setMaxAccess(_B)
if mibBuilder.loadTexts:agentDot1xClientVlanAssignedReason.setStatus(_A)
_AgentDot1xClientSessionTimeout_Type=Unsigned32
_AgentDot1xClientSessionTimeout_Object=MibTableColumn
agentDot1xClientSessionTimeout=_AgentDot1xClientSessionTimeout_Object((1,3,6,1,4,1,789,4413,1,1,36,3,1,1,11),_AgentDot1xClientSessionTimeout_Type())
agentDot1xClientSessionTimeout.setMaxAccess(_B)
if mibBuilder.loadTexts:agentDot1xClientSessionTimeout.setStatus(_A)
_AgentDot1xClientTerminationAction_Type=Dot1xSessionTerminationAction
_AgentDot1xClientTerminationAction_Object=MibTableColumn
agentDot1xClientTerminationAction=_AgentDot1xClientTerminationAction_Object((1,3,6,1,4,1,789,4413,1,1,36,3,1,1,12),_AgentDot1xClientTerminationAction_Type())
agentDot1xClientTerminationAction.setMaxAccess(_B)
if mibBuilder.loadTexts:agentDot1xClientTerminationAction.setStatus(_A)
_AgentDot1xMonitorModeConfigGroup_ObjectIdentity=ObjectIdentity
agentDot1xMonitorModeConfigGroup=_AgentDot1xMonitorModeConfigGroup_ObjectIdentity((1,3,6,1,4,1,789,4413,1,1,36,4))
class _AgentDot1xMonitorModeEnabled_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_AgentDot1xMonitorModeEnabled_Type.__name__=_C
_AgentDot1xMonitorModeEnabled_Object=MibScalar
agentDot1xMonitorModeEnabled=_AgentDot1xMonitorModeEnabled_Object((1,3,6,1,4,1,789,4413,1,1,36,4,1),_AgentDot1xMonitorModeEnabled_Type())
agentDot1xMonitorModeEnabled.setMaxAccess(_D)
if mibBuilder.loadTexts:agentDot1xMonitorModeEnabled.setStatus(_A)
_AgentDot1xMonitorModeClients_Type=Unsigned32
_AgentDot1xMonitorModeClients_Object=MibScalar
agentDot1xMonitorModeClients=_AgentDot1xMonitorModeClients_Object((1,3,6,1,4,1,789,4413,1,1,36,4,2),_AgentDot1xMonitorModeClients_Type())
agentDot1xMonitorModeClients.setMaxAccess(_B)
if mibBuilder.loadTexts:agentDot1xMonitorModeClients.setStatus(_A)
_AgentDot1xNonMonitorModeClients_Type=Unsigned32
_AgentDot1xNonMonitorModeClients_Object=MibScalar
agentDot1xNonMonitorModeClients=_AgentDot1xNonMonitorModeClients_Object((1,3,6,1,4,1,789,4413,1,1,36,4,3),_AgentDot1xNonMonitorModeClients_Type())
agentDot1xNonMonitorModeClients.setMaxAccess(_B)
if mibBuilder.loadTexts:agentDot1xNonMonitorModeClients.setStatus(_A)
_AgentDot1xAuthHistoryResultsGroup_ObjectIdentity=ObjectIdentity
agentDot1xAuthHistoryResultsGroup=_AgentDot1xAuthHistoryResultsGroup_ObjectIdentity((1,3,6,1,4,1,789,4413,1,1,36,5))
_AgentDot1xPortAuthHistoryResultTable_Object=MibTable
agentDot1xPortAuthHistoryResultTable=_AgentDot1xPortAuthHistoryResultTable_Object((1,3,6,1,4,1,789,4413,1,1,36,5,1))
if mibBuilder.loadTexts:agentDot1xPortAuthHistoryResultTable.setStatus(_A)
_AgentDot1xPortAuthHistoryResultEntry_Object=MibTableRow
agentDot1xPortAuthHistoryResultEntry=_AgentDot1xPortAuthHistoryResultEntry_Object((1,3,6,1,4,1,789,4413,1,1,36,5,1,1))
agentDot1xPortAuthHistoryResultEntry.setIndexNames((0,_H,_W),(0,_H,_X))
if mibBuilder.loadTexts:agentDot1xPortAuthHistoryResultEntry.setStatus(_A)
_AgentDot1xAuthHistoryResultIfaceIndex_Type=Unsigned32
_AgentDot1xAuthHistoryResultIfaceIndex_Object=MibTableColumn
agentDot1xAuthHistoryResultIfaceIndex=_AgentDot1xAuthHistoryResultIfaceIndex_Object((1,3,6,1,4,1,789,4413,1,1,36,5,1,1,1),_AgentDot1xAuthHistoryResultIfaceIndex_Type())
agentDot1xAuthHistoryResultIfaceIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:agentDot1xAuthHistoryResultIfaceIndex.setStatus(_A)
_AgentDot1xAuthHistoryResultIndex_Type=Unsigned32
_AgentDot1xAuthHistoryResultIndex_Object=MibTableColumn
agentDot1xAuthHistoryResultIndex=_AgentDot1xAuthHistoryResultIndex_Object((1,3,6,1,4,1,789,4413,1,1,36,5,1,1,2),_AgentDot1xAuthHistoryResultIndex_Type())
agentDot1xAuthHistoryResultIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:agentDot1xAuthHistoryResultIndex.setStatus(_A)
_AgentDot1xAuthHistoryResultTimeStamp_Type=DateAndTime
_AgentDot1xAuthHistoryResultTimeStamp_Object=MibTableColumn
agentDot1xAuthHistoryResultTimeStamp=_AgentDot1xAuthHistoryResultTimeStamp_Object((1,3,6,1,4,1,789,4413,1,1,36,5,1,1,3),_AgentDot1xAuthHistoryResultTimeStamp_Type())
agentDot1xAuthHistoryResultTimeStamp.setMaxAccess(_B)
if mibBuilder.loadTexts:agentDot1xAuthHistoryResultTimeStamp.setStatus(_A)
_AgentDot1xAuthHistoryResultAge_Type=TimeTicks
_AgentDot1xAuthHistoryResultAge_Object=MibTableColumn
agentDot1xAuthHistoryResultAge=_AgentDot1xAuthHistoryResultAge_Object((1,3,6,1,4,1,789,4413,1,1,36,5,1,1,4),_AgentDot1xAuthHistoryResultAge_Type())
agentDot1xAuthHistoryResultAge.setMaxAccess(_B)
if mibBuilder.loadTexts:agentDot1xAuthHistoryResultAge.setStatus(_A)
_AgentDot1xAuthHistoryResultMacAddress_Type=MacAddress
_AgentDot1xAuthHistoryResultMacAddress_Object=MibTableColumn
agentDot1xAuthHistoryResultMacAddress=_AgentDot1xAuthHistoryResultMacAddress_Object((1,3,6,1,4,1,789,4413,1,1,36,5,1,1,5),_AgentDot1xAuthHistoryResultMacAddress_Type())
agentDot1xAuthHistoryResultMacAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:agentDot1xAuthHistoryResultMacAddress.setStatus(_A)
_AgentDot1xAuthHistoryResultVlanId_Type=Unsigned32
_AgentDot1xAuthHistoryResultVlanId_Object=MibTableColumn
agentDot1xAuthHistoryResultVlanId=_AgentDot1xAuthHistoryResultVlanId_Object((1,3,6,1,4,1,789,4413,1,1,36,5,1,1,6),_AgentDot1xAuthHistoryResultVlanId_Type())
agentDot1xAuthHistoryResultVlanId.setMaxAccess(_B)
if mibBuilder.loadTexts:agentDot1xAuthHistoryResultVlanId.setStatus(_A)
class _AgentDot1xAuthHistoryResultAuthStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_V,1),('failure',2)))
_AgentDot1xAuthHistoryResultAuthStatus_Type.__name__=_C
_AgentDot1xAuthHistoryResultAuthStatus_Object=MibTableColumn
agentDot1xAuthHistoryResultAuthStatus=_AgentDot1xAuthHistoryResultAuthStatus_Object((1,3,6,1,4,1,789,4413,1,1,36,5,1,1,7),_AgentDot1xAuthHistoryResultAuthStatus_Type())
agentDot1xAuthHistoryResultAuthStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:agentDot1xAuthHistoryResultAuthStatus.setStatus(_A)
class _AgentDot1xAuthHistoryResultAccessStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('granted',1),('denied',2)))
_AgentDot1xAuthHistoryResultAccessStatus_Type.__name__=_C
_AgentDot1xAuthHistoryResultAccessStatus_Object=MibTableColumn
agentDot1xAuthHistoryResultAccessStatus=_AgentDot1xAuthHistoryResultAccessStatus_Object((1,3,6,1,4,1,789,4413,1,1,36,5,1,1,8),_AgentDot1xAuthHistoryResultAccessStatus_Type())
agentDot1xAuthHistoryResultAccessStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:agentDot1xAuthHistoryResultAccessStatus.setStatus(_A)
_AgentDot1xAuthHistoryResultFilterID_Type=DisplayString
_AgentDot1xAuthHistoryResultFilterID_Object=MibTableColumn
agentDot1xAuthHistoryResultFilterID=_AgentDot1xAuthHistoryResultFilterID_Object((1,3,6,1,4,1,789,4413,1,1,36,5,1,1,9),_AgentDot1xAuthHistoryResultFilterID_Type())
agentDot1xAuthHistoryResultFilterID.setMaxAccess(_B)
if mibBuilder.loadTexts:agentDot1xAuthHistoryResultFilterID.setStatus(_A)
_AgentDot1xAuthHistoryResultVlanAssigned_Type=Unsigned32
_AgentDot1xAuthHistoryResultVlanAssigned_Object=MibTableColumn
agentDot1xAuthHistoryResultVlanAssigned=_AgentDot1xAuthHistoryResultVlanAssigned_Object((1,3,6,1,4,1,789,4413,1,1,36,5,1,1,10),_AgentDot1xAuthHistoryResultVlanAssigned_Type())
agentDot1xAuthHistoryResultVlanAssigned.setMaxAccess(_B)
if mibBuilder.loadTexts:agentDot1xAuthHistoryResultVlanAssigned.setStatus(_A)
class _AgentDot1xAuthHistoryResultVlanAssignedType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*((_I,1),(_J,2),(_K,3),(_P,4),(_Q,5),(_L,6),(_R,7)))
_AgentDot1xAuthHistoryResultVlanAssignedType_Type.__name__=_C
_AgentDot1xAuthHistoryResultVlanAssignedType_Object=MibTableColumn
agentDot1xAuthHistoryResultVlanAssignedType=_AgentDot1xAuthHistoryResultVlanAssignedType_Object((1,3,6,1,4,1,789,4413,1,1,36,5,1,1,11),_AgentDot1xAuthHistoryResultVlanAssignedType_Type())
agentDot1xAuthHistoryResultVlanAssignedType.setMaxAccess(_B)
if mibBuilder.loadTexts:agentDot1xAuthHistoryResultVlanAssignedType.setStatus(_A)
class _AgentDot1xAuthHistoryResultReasonCode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30)));namedValues=NamedValues(*(('supplicant-timeout',1),('eapol-timeout',2),('radius-request-timeout',3),('radius-auth-failure',4),('radius-auth-comm-failure',5),('radius-challenge-process-invalid-nas-port',6),('radius-challenge-process-wrong-eap-msg',7),('radius-request-send-msg-error',8),('radius-accept-process-invalid-nas-port',9),('radius-accept-process-wrong-eap-msg',10),('radius-accept-filter-assignment-failure',11),('radius-accept-diffserv-not-present',12),('radius-accept-vlan-assignment-failure',13),('vlan-assignment-feature-not-enabled',14),('radius-success',15),('local-auth-user-not-found',16),('local-auth-user-no-access',17),('local-auth-md5-validation-failure',18),('local-auth-invalid-eap-type',19),('local-failure',20),('local-success',21),('radius-invalid-radius-status',22),('guest-vlan-timer-expiry',23),('undefined-auth-method',24),('reject-auth-method',25),('invalid-auth-method',26),('auth-method-not-configured',27),('unauth-vlan-not-created',28),('guest-vlan-not-created',29),('radius-accept-invalid-vlan-failure',30)))
_AgentDot1xAuthHistoryResultReasonCode_Type.__name__=_C
_AgentDot1xAuthHistoryResultReasonCode_Object=MibTableColumn
agentDot1xAuthHistoryResultReasonCode=_AgentDot1xAuthHistoryResultReasonCode_Object((1,3,6,1,4,1,789,4413,1,1,36,5,1,1,12),_AgentDot1xAuthHistoryResultReasonCode_Type())
agentDot1xAuthHistoryResultReasonCode.setMaxAccess(_B)
if mibBuilder.loadTexts:agentDot1xAuthHistoryResultReasonCode.setStatus(_A)
class _AgentDot1xAuthHistoryResultsClear_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_AgentDot1xAuthHistoryResultsClear_Type.__name__=_C
_AgentDot1xAuthHistoryResultsClear_Object=MibScalar
agentDot1xAuthHistoryResultsClear=_AgentDot1xAuthHistoryResultsClear_Object((1,3,6,1,4,1,789,4413,1,1,36,5,2),_AgentDot1xAuthHistoryResultsClear_Type())
agentDot1xAuthHistoryResultsClear.setMaxAccess(_D)
if mibBuilder.loadTexts:agentDot1xAuthHistoryResultsClear.setStatus(_A)
_AgentDot1xPortAuthHistoryResultClearTable_Object=MibTable
agentDot1xPortAuthHistoryResultClearTable=_AgentDot1xPortAuthHistoryResultClearTable_Object((1,3,6,1,4,1,789,4413,1,1,36,5,3))
if mibBuilder.loadTexts:agentDot1xPortAuthHistoryResultClearTable.setStatus(_A)
_AgentDot1xPortAuthHistoryResultClearEntry_Object=MibTableRow
agentDot1xPortAuthHistoryResultClearEntry=_AgentDot1xPortAuthHistoryResultClearEntry_Object((1,3,6,1,4,1,789,4413,1,1,36,5,3,1))
agentDot1xPortAuthHistoryResultClearEntry.setIndexNames((0,_H,_Y))
if mibBuilder.loadTexts:agentDot1xPortAuthHistoryResultClearEntry.setStatus(_A)
_AgentDot1xAuthHistoryResultIfIndex_Type=Unsigned32
_AgentDot1xAuthHistoryResultIfIndex_Object=MibTableColumn
agentDot1xAuthHistoryResultIfIndex=_AgentDot1xAuthHistoryResultIfIndex_Object((1,3,6,1,4,1,789,4413,1,1,36,5,3,1,1),_AgentDot1xAuthHistoryResultIfIndex_Type())
agentDot1xAuthHistoryResultIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:agentDot1xAuthHistoryResultIfIndex.setStatus(_A)
class _AgentDot1xPortAuthHistoryResultsClear_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_AgentDot1xPortAuthHistoryResultsClear_Type.__name__=_C
_AgentDot1xPortAuthHistoryResultsClear_Object=MibTableColumn
agentDot1xPortAuthHistoryResultsClear=_AgentDot1xPortAuthHistoryResultsClear_Object((1,3,6,1,4,1,789,4413,1,1,36,5,3,1,2),_AgentDot1xPortAuthHistoryResultsClear_Type())
agentDot1xPortAuthHistoryResultsClear.setMaxAccess(_D)
if mibBuilder.loadTexts:agentDot1xPortAuthHistoryResultsClear.setStatus(_A)
mibBuilder.exportSymbols(_H,**{_O:Dot1xPortControlMode,_S:Dot1xSessionTerminationAction,'fastPathdot1xAdvanced':fastPathdot1xAdvanced,'agentDot1xEnhancementConfigGroup':agentDot1xEnhancementConfigGroup,'agentDot1xRadiusVlanAssignment':agentDot1xRadiusVlanAssignment,'agentDot1xDynamicVlanCreationMode':agentDot1xDynamicVlanCreationMode,'agentDot1xEapolFloodMode':agentDot1xEapolFloodMode,'agentDot1xPortConfigGroup':agentDot1xPortConfigGroup,'agentDot1xPortConfigTable':agentDot1xPortConfigTable,'agentDot1xPortConfigEntry':agentDot1xPortConfigEntry,'agentDot1xPortControlMode':agentDot1xPortControlMode,'agentDot1xGuestVlanId':agentDot1xGuestVlanId,'agentDot1xGuestVlanPeriod':agentDot1xGuestVlanPeriod,'agentDot1xUnauthenticatedVlan':agentDot1xUnauthenticatedVlan,'agentDot1xMaxUsers':agentDot1xMaxUsers,'agentDot1xPortVlanAssigned':agentDot1xPortVlanAssigned,'agentDot1xPortVlanAssignedReason':agentDot1xPortVlanAssignedReason,'agentDot1xPortSessionTimeout':agentDot1xPortSessionTimeout,'agentDot1xPortTerminationAction':agentDot1xPortTerminationAction,'agentDot1xPortMABenabled':agentDot1xPortMABenabled,'agentDot1xPortMABenabledOperational':agentDot1xPortMABenabledOperational,'agentDot1xClientConfigGroup':agentDot1xClientConfigGroup,'agentDot1xClientConfigTable':agentDot1xClientConfigTable,'agentDot1xClientConfigEntry':agentDot1xClientConfigEntry,_T:agentDot1xClientMacAddress,'agentDot1xLogicalPort':agentDot1xLogicalPort,'agentDot1xInterface':agentDot1xInterface,'agentDot1xClientAuthPAEstate':agentDot1xClientAuthPAEstate,'agentDot1xClientBackendState':agentDot1xClientBackendState,'agentDot1xClientUserName':agentDot1xClientUserName,'agentDot1xClientSessionTime':agentDot1xClientSessionTime,'agentDot1xClientFilterID':agentDot1xClientFilterID,'agentDot1xClientVlanAssigned':agentDot1xClientVlanAssigned,'agentDot1xClientVlanAssignedReason':agentDot1xClientVlanAssignedReason,'agentDot1xClientSessionTimeout':agentDot1xClientSessionTimeout,'agentDot1xClientTerminationAction':agentDot1xClientTerminationAction,'agentDot1xMonitorModeConfigGroup':agentDot1xMonitorModeConfigGroup,'agentDot1xMonitorModeEnabled':agentDot1xMonitorModeEnabled,'agentDot1xMonitorModeClients':agentDot1xMonitorModeClients,'agentDot1xNonMonitorModeClients':agentDot1xNonMonitorModeClients,'agentDot1xAuthHistoryResultsGroup':agentDot1xAuthHistoryResultsGroup,'agentDot1xPortAuthHistoryResultTable':agentDot1xPortAuthHistoryResultTable,'agentDot1xPortAuthHistoryResultEntry':agentDot1xPortAuthHistoryResultEntry,_W:agentDot1xAuthHistoryResultIfaceIndex,_X:agentDot1xAuthHistoryResultIndex,'agentDot1xAuthHistoryResultTimeStamp':agentDot1xAuthHistoryResultTimeStamp,'agentDot1xAuthHistoryResultAge':agentDot1xAuthHistoryResultAge,'agentDot1xAuthHistoryResultMacAddress':agentDot1xAuthHistoryResultMacAddress,'agentDot1xAuthHistoryResultVlanId':agentDot1xAuthHistoryResultVlanId,'agentDot1xAuthHistoryResultAuthStatus':agentDot1xAuthHistoryResultAuthStatus,'agentDot1xAuthHistoryResultAccessStatus':agentDot1xAuthHistoryResultAccessStatus,'agentDot1xAuthHistoryResultFilterID':agentDot1xAuthHistoryResultFilterID,'agentDot1xAuthHistoryResultVlanAssigned':agentDot1xAuthHistoryResultVlanAssigned,'agentDot1xAuthHistoryResultVlanAssignedType':agentDot1xAuthHistoryResultVlanAssignedType,'agentDot1xAuthHistoryResultReasonCode':agentDot1xAuthHistoryResultReasonCode,'agentDot1xAuthHistoryResultsClear':agentDot1xAuthHistoryResultsClear,'agentDot1xPortAuthHistoryResultClearTable':agentDot1xPortAuthHistoryResultClearTable,'agentDot1xPortAuthHistoryResultClearEntry':agentDot1xPortAuthHistoryResultClearEntry,_Y:agentDot1xAuthHistoryResultIfIndex,'agentDot1xPortAuthHistoryResultsClear':agentDot1xPortAuthHistoryResultsClear})