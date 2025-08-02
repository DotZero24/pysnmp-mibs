_Q='initialize'
_P='agentDot1xClientMacAddress'
_O='FASTPATH-DOT1X-ADVANCED-FEATURES-MIB'
_N='Dot1xSessionTerminationAction'
_M='unauthenticatedVlan'
_L='radius'
_K='Dot1xPortControlMode'
_J='dot1xPaePortNumber'
_I='IEEE8021-PAE-MIB'
_H='disable'
_G='enable'
_F='default'
_E='Unsigned32'
_D='read-write'
_C='Integer32'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
fastPath,=mibBuilder.importSymbols('BROADCOM-REF-MIB','fastPath')
dot1xPaePortNumber,=mibBuilder.importSymbols(_I,_J)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_E,'iso')
DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress','RowStatus','TextualConvention')
fastPathdot1xAdvanced=ModuleIdentity((1,3,6,1,4,1,4413,1,1,36))
if mibBuilder.loadTexts:fastPathdot1xAdvanced.setRevisions(('2007-05-23 00:00',))
class Dot1xPortControlMode(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('forceUnauthorized',1),('auto',2),('forceAuthorized',3),('macBased',4)))
class Dot1xSessionTerminationAction(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),('reauthenticate',2)))
_AgentDot1xEnhancementConfigGroup_ObjectIdentity=ObjectIdentity
agentDot1xEnhancementConfigGroup=_AgentDot1xEnhancementConfigGroup_ObjectIdentity((1,3,6,1,4,1,4413,1,1,36,1))
class _AgentDot1xRadiusVlanAssignment_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_AgentDot1xRadiusVlanAssignment_Type.__name__=_C
_AgentDot1xRadiusVlanAssignment_Object=MibScalar
agentDot1xRadiusVlanAssignment=_AgentDot1xRadiusVlanAssignment_Object((1,3,6,1,4,1,4413,1,1,36,1,1),_AgentDot1xRadiusVlanAssignment_Type())
agentDot1xRadiusVlanAssignment.setMaxAccess(_D)
if mibBuilder.loadTexts:agentDot1xRadiusVlanAssignment.setStatus(_A)
_AgentDot1xPortConfigGroup_ObjectIdentity=ObjectIdentity
agentDot1xPortConfigGroup=_AgentDot1xPortConfigGroup_ObjectIdentity((1,3,6,1,4,1,4413,1,1,36,2))
_AgentDot1xPortConfigTable_Object=MibTable
agentDot1xPortConfigTable=_AgentDot1xPortConfigTable_Object((1,3,6,1,4,1,4413,1,1,36,2,1))
if mibBuilder.loadTexts:agentDot1xPortConfigTable.setStatus(_A)
_AgentDot1xPortConfigEntry_Object=MibTableRow
agentDot1xPortConfigEntry=_AgentDot1xPortConfigEntry_Object((1,3,6,1,4,1,4413,1,1,36,2,1,1))
agentDot1xPortConfigEntry.setIndexNames((0,_I,_J))
if mibBuilder.loadTexts:agentDot1xPortConfigEntry.setStatus(_A)
class _AgentDot1xPortControlMode_Type(Dot1xPortControlMode):defaultValue=2
_AgentDot1xPortControlMode_Type.__name__=_K
_AgentDot1xPortControlMode_Object=MibTableColumn
agentDot1xPortControlMode=_AgentDot1xPortControlMode_Object((1,3,6,1,4,1,4413,1,1,36,2,1,1,1),_AgentDot1xPortControlMode_Type())
agentDot1xPortControlMode.setMaxAccess(_D)
if mibBuilder.loadTexts:agentDot1xPortControlMode.setStatus(_A)
class _AgentDot1xGuestVlanId_Type(Unsigned32):defaultValue=0
_AgentDot1xGuestVlanId_Type.__name__=_E
_AgentDot1xGuestVlanId_Object=MibTableColumn
agentDot1xGuestVlanId=_AgentDot1xGuestVlanId_Object((1,3,6,1,4,1,4413,1,1,36,2,1,1,2),_AgentDot1xGuestVlanId_Type())
agentDot1xGuestVlanId.setMaxAccess(_D)
if mibBuilder.loadTexts:agentDot1xGuestVlanId.setStatus(_A)
class _AgentDot1xGuestVlanPeriod_Type(Unsigned32):defaultValue=90;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_AgentDot1xGuestVlanPeriod_Type.__name__=_E
_AgentDot1xGuestVlanPeriod_Object=MibTableColumn
agentDot1xGuestVlanPeriod=_AgentDot1xGuestVlanPeriod_Object((1,3,6,1,4,1,4413,1,1,36,2,1,1,3),_AgentDot1xGuestVlanPeriod_Type())
agentDot1xGuestVlanPeriod.setMaxAccess(_D)
if mibBuilder.loadTexts:agentDot1xGuestVlanPeriod.setStatus(_A)
class _AgentDot1xUnauthenticatedVlan_Type(Unsigned32):defaultValue=0
_AgentDot1xUnauthenticatedVlan_Type.__name__=_E
_AgentDot1xUnauthenticatedVlan_Object=MibTableColumn
agentDot1xUnauthenticatedVlan=_AgentDot1xUnauthenticatedVlan_Object((1,3,6,1,4,1,4413,1,1,36,2,1,1,4),_AgentDot1xUnauthenticatedVlan_Type())
agentDot1xUnauthenticatedVlan.setMaxAccess(_D)
if mibBuilder.loadTexts:agentDot1xUnauthenticatedVlan.setStatus(_A)
_AgentDot1xMaxUsers_Type=Unsigned32
_AgentDot1xMaxUsers_Object=MibTableColumn
agentDot1xMaxUsers=_AgentDot1xMaxUsers_Object((1,3,6,1,4,1,4413,1,1,36,2,1,1,5),_AgentDot1xMaxUsers_Type())
agentDot1xMaxUsers.setMaxAccess(_D)
if mibBuilder.loadTexts:agentDot1xMaxUsers.setStatus(_A)
class _AgentDot1xPortVlanAssigned_Type(Unsigned32):defaultValue=0
_AgentDot1xPortVlanAssigned_Type.__name__=_E
_AgentDot1xPortVlanAssigned_Object=MibTableColumn
agentDot1xPortVlanAssigned=_AgentDot1xPortVlanAssigned_Object((1,3,6,1,4,1,4413,1,1,36,2,1,1,6),_AgentDot1xPortVlanAssigned_Type())
agentDot1xPortVlanAssigned.setMaxAccess(_B)
if mibBuilder.loadTexts:agentDot1xPortVlanAssigned.setStatus(_A)
class _AgentDot1xPortVlanAssignedReason_Type(Integer32):defaultValue=5;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_F,1),(_L,2),(_M,3),('guestVlan',4),('notAssigned',5)))
_AgentDot1xPortVlanAssignedReason_Type.__name__=_C
_AgentDot1xPortVlanAssignedReason_Object=MibTableColumn
agentDot1xPortVlanAssignedReason=_AgentDot1xPortVlanAssignedReason_Object((1,3,6,1,4,1,4413,1,1,36,2,1,1,7),_AgentDot1xPortVlanAssignedReason_Type())
agentDot1xPortVlanAssignedReason.setMaxAccess(_B)
if mibBuilder.loadTexts:agentDot1xPortVlanAssignedReason.setStatus(_A)
_AgentDot1xPortSessionTimeout_Type=Unsigned32
_AgentDot1xPortSessionTimeout_Object=MibTableColumn
agentDot1xPortSessionTimeout=_AgentDot1xPortSessionTimeout_Object((1,3,6,1,4,1,4413,1,1,36,2,1,1,8),_AgentDot1xPortSessionTimeout_Type())
agentDot1xPortSessionTimeout.setMaxAccess(_B)
if mibBuilder.loadTexts:agentDot1xPortSessionTimeout.setStatus(_A)
class _AgentDot1xPortTerminationAction_Type(Dot1xSessionTerminationAction):defaultValue=1
_AgentDot1xPortTerminationAction_Type.__name__=_N
_AgentDot1xPortTerminationAction_Object=MibTableColumn
agentDot1xPortTerminationAction=_AgentDot1xPortTerminationAction_Object((1,3,6,1,4,1,4413,1,1,36,2,1,1,9),_AgentDot1xPortTerminationAction_Type())
agentDot1xPortTerminationAction.setMaxAccess(_B)
if mibBuilder.loadTexts:agentDot1xPortTerminationAction.setStatus(_A)
class _AgentDot1xPortMABenabled_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_AgentDot1xPortMABenabled_Type.__name__=_C
_AgentDot1xPortMABenabled_Object=MibTableColumn
agentDot1xPortMABenabled=_AgentDot1xPortMABenabled_Object((1,3,6,1,4,1,4413,1,1,36,2,1,1,10),_AgentDot1xPortMABenabled_Type())
agentDot1xPortMABenabled.setMaxAccess(_D)
if mibBuilder.loadTexts:agentDot1xPortMABenabled.setStatus(_A)
class _AgentDot1xPortMABenabledOperational_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_AgentDot1xPortMABenabledOperational_Type.__name__=_C
_AgentDot1xPortMABenabledOperational_Object=MibTableColumn
agentDot1xPortMABenabledOperational=_AgentDot1xPortMABenabledOperational_Object((1,3,6,1,4,1,4413,1,1,36,2,1,1,11),_AgentDot1xPortMABenabledOperational_Type())
agentDot1xPortMABenabledOperational.setMaxAccess(_B)
if mibBuilder.loadTexts:agentDot1xPortMABenabledOperational.setStatus(_A)
_AgentDot1xClientConfigGroup_ObjectIdentity=ObjectIdentity
agentDot1xClientConfigGroup=_AgentDot1xClientConfigGroup_ObjectIdentity((1,3,6,1,4,1,4413,1,1,36,3))
_AgentDot1xClientConfigTable_Object=MibTable
agentDot1xClientConfigTable=_AgentDot1xClientConfigTable_Object((1,3,6,1,4,1,4413,1,1,36,3,1))
if mibBuilder.loadTexts:agentDot1xClientConfigTable.setStatus(_A)
_AgentDot1xClientConfigEntry_Object=MibTableRow
agentDot1xClientConfigEntry=_AgentDot1xClientConfigEntry_Object((1,3,6,1,4,1,4413,1,1,36,3,1,1))
agentDot1xClientConfigEntry.setIndexNames((0,_O,_P))
if mibBuilder.loadTexts:agentDot1xClientConfigEntry.setStatus(_A)
_AgentDot1xClientMacAddress_Type=MacAddress
_AgentDot1xClientMacAddress_Object=MibTableColumn
agentDot1xClientMacAddress=_AgentDot1xClientMacAddress_Object((1,3,6,1,4,1,4413,1,1,36,3,1,1,1),_AgentDot1xClientMacAddress_Type())
agentDot1xClientMacAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:agentDot1xClientMacAddress.setStatus(_A)
_AgentDot1xLogicalPort_Type=Unsigned32
_AgentDot1xLogicalPort_Object=MibTableColumn
agentDot1xLogicalPort=_AgentDot1xLogicalPort_Object((1,3,6,1,4,1,4413,1,1,36,3,1,1,2),_AgentDot1xLogicalPort_Type())
agentDot1xLogicalPort.setMaxAccess(_B)
if mibBuilder.loadTexts:agentDot1xLogicalPort.setStatus(_A)
_AgentDot1xInterface_Type=Unsigned32
_AgentDot1xInterface_Object=MibTableColumn
agentDot1xInterface=_AgentDot1xInterface_Object((1,3,6,1,4,1,4413,1,1,36,3,1,1,3),_AgentDot1xInterface_Type())
agentDot1xInterface.setMaxAccess(_B)
if mibBuilder.loadTexts:agentDot1xInterface.setStatus(_A)
class _AgentDot1xClientAuthPAEstate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9)));namedValues=NamedValues(*((_Q,1),('disconnected',2),('connecting',3),('authenticating',4),('authenticated',5),('aborting',6),('held',7),('forceAuth',8),('forceUnauth',9)))
_AgentDot1xClientAuthPAEstate_Type.__name__=_C
_AgentDot1xClientAuthPAEstate_Object=MibTableColumn
agentDot1xClientAuthPAEstate=_AgentDot1xClientAuthPAEstate_Object((1,3,6,1,4,1,4413,1,1,36,3,1,1,4),_AgentDot1xClientAuthPAEstate_Type())
agentDot1xClientAuthPAEstate.setMaxAccess(_B)
if mibBuilder.loadTexts:agentDot1xClientAuthPAEstate.setStatus(_A)
class _AgentDot1xClientBackendState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*(('request',1),('response',2),('success',3),('fail',4),('timeout',5),('idle',6),(_Q,7)))
_AgentDot1xClientBackendState_Type.__name__=_C
_AgentDot1xClientBackendState_Object=MibTableColumn
agentDot1xClientBackendState=_AgentDot1xClientBackendState_Object((1,3,6,1,4,1,4413,1,1,36,3,1,1,5),_AgentDot1xClientBackendState_Type())
agentDot1xClientBackendState.setMaxAccess(_B)
if mibBuilder.loadTexts:agentDot1xClientBackendState.setStatus(_A)
_AgentDot1xClientUserName_Type=DisplayString
_AgentDot1xClientUserName_Object=MibTableColumn
agentDot1xClientUserName=_AgentDot1xClientUserName_Object((1,3,6,1,4,1,4413,1,1,36,3,1,1,6),_AgentDot1xClientUserName_Type())
agentDot1xClientUserName.setMaxAccess(_B)
if mibBuilder.loadTexts:agentDot1xClientUserName.setStatus(_A)
_AgentDot1xClientSessionTime_Type=Unsigned32
_AgentDot1xClientSessionTime_Object=MibTableColumn
agentDot1xClientSessionTime=_AgentDot1xClientSessionTime_Object((1,3,6,1,4,1,4413,1,1,36,3,1,1,7),_AgentDot1xClientSessionTime_Type())
agentDot1xClientSessionTime.setMaxAccess(_B)
if mibBuilder.loadTexts:agentDot1xClientSessionTime.setStatus(_A)
_AgentDot1xClientFilterID_Type=DisplayString
_AgentDot1xClientFilterID_Object=MibTableColumn
agentDot1xClientFilterID=_AgentDot1xClientFilterID_Object((1,3,6,1,4,1,4413,1,1,36,3,1,1,8),_AgentDot1xClientFilterID_Type())
agentDot1xClientFilterID.setMaxAccess(_B)
if mibBuilder.loadTexts:agentDot1xClientFilterID.setStatus(_A)
_AgentDot1xClientVlanAssigned_Type=Unsigned32
_AgentDot1xClientVlanAssigned_Object=MibTableColumn
agentDot1xClientVlanAssigned=_AgentDot1xClientVlanAssigned_Object((1,3,6,1,4,1,4413,1,1,36,3,1,1,9),_AgentDot1xClientVlanAssigned_Type())
agentDot1xClientVlanAssigned.setMaxAccess(_B)
if mibBuilder.loadTexts:agentDot1xClientVlanAssigned.setStatus(_A)
class _AgentDot1xClientVlanAssignedReason_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_F,1),(_L,2),(_M,3),('invalid',4)))
_AgentDot1xClientVlanAssignedReason_Type.__name__=_C
_AgentDot1xClientVlanAssignedReason_Object=MibTableColumn
agentDot1xClientVlanAssignedReason=_AgentDot1xClientVlanAssignedReason_Object((1,3,6,1,4,1,4413,1,1,36,3,1,1,10),_AgentDot1xClientVlanAssignedReason_Type())
agentDot1xClientVlanAssignedReason.setMaxAccess(_B)
if mibBuilder.loadTexts:agentDot1xClientVlanAssignedReason.setStatus(_A)
_AgentDot1xClientSessionTimeout_Type=Unsigned32
_AgentDot1xClientSessionTimeout_Object=MibTableColumn
agentDot1xClientSessionTimeout=_AgentDot1xClientSessionTimeout_Object((1,3,6,1,4,1,4413,1,1,36,3,1,1,11),_AgentDot1xClientSessionTimeout_Type())
agentDot1xClientSessionTimeout.setMaxAccess(_B)
if mibBuilder.loadTexts:agentDot1xClientSessionTimeout.setStatus(_A)
_AgentDot1xClientTerminationAction_Type=Dot1xSessionTerminationAction
_AgentDot1xClientTerminationAction_Object=MibTableColumn
agentDot1xClientTerminationAction=_AgentDot1xClientTerminationAction_Object((1,3,6,1,4,1,4413,1,1,36,3,1,1,12),_AgentDot1xClientTerminationAction_Type())
agentDot1xClientTerminationAction.setMaxAccess(_B)
if mibBuilder.loadTexts:agentDot1xClientTerminationAction.setStatus(_A)
mibBuilder.exportSymbols(_O,**{_K:Dot1xPortControlMode,_N:Dot1xSessionTerminationAction,'fastPathdot1xAdvanced':fastPathdot1xAdvanced,'agentDot1xEnhancementConfigGroup':agentDot1xEnhancementConfigGroup,'agentDot1xRadiusVlanAssignment':agentDot1xRadiusVlanAssignment,'agentDot1xPortConfigGroup':agentDot1xPortConfigGroup,'agentDot1xPortConfigTable':agentDot1xPortConfigTable,'agentDot1xPortConfigEntry':agentDot1xPortConfigEntry,'agentDot1xPortControlMode':agentDot1xPortControlMode,'agentDot1xGuestVlanId':agentDot1xGuestVlanId,'agentDot1xGuestVlanPeriod':agentDot1xGuestVlanPeriod,'agentDot1xUnauthenticatedVlan':agentDot1xUnauthenticatedVlan,'agentDot1xMaxUsers':agentDot1xMaxUsers,'agentDot1xPortVlanAssigned':agentDot1xPortVlanAssigned,'agentDot1xPortVlanAssignedReason':agentDot1xPortVlanAssignedReason,'agentDot1xPortSessionTimeout':agentDot1xPortSessionTimeout,'agentDot1xPortTerminationAction':agentDot1xPortTerminationAction,'agentDot1xPortMABenabled':agentDot1xPortMABenabled,'agentDot1xPortMABenabledOperational':agentDot1xPortMABenabledOperational,'agentDot1xClientConfigGroup':agentDot1xClientConfigGroup,'agentDot1xClientConfigTable':agentDot1xClientConfigTable,'agentDot1xClientConfigEntry':agentDot1xClientConfigEntry,_P:agentDot1xClientMacAddress,'agentDot1xLogicalPort':agentDot1xLogicalPort,'agentDot1xInterface':agentDot1xInterface,'agentDot1xClientAuthPAEstate':agentDot1xClientAuthPAEstate,'agentDot1xClientBackendState':agentDot1xClientBackendState,'agentDot1xClientUserName':agentDot1xClientUserName,'agentDot1xClientSessionTime':agentDot1xClientSessionTime,'agentDot1xClientFilterID':agentDot1xClientFilterID,'agentDot1xClientVlanAssigned':agentDot1xClientVlanAssigned,'agentDot1xClientVlanAssignedReason':agentDot1xClientVlanAssignedReason,'agentDot1xClientSessionTimeout':agentDot1xClientSessionTimeout,'agentDot1xClientTerminationAction':agentDot1xClientTerminationAction})