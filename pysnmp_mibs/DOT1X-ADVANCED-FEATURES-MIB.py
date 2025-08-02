_M='radius'
_L='agentDot1xClientLogicalInterface'
_K='DOT1X-ADVANCED-FEATURES-MIB'
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
dot1xPaePortNumber,=mibBuilder.importSymbols(_I,_J)
switch,=mibBuilder.importSymbols('QUANTA-SWITCH-MIB','switch')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_E,'iso')
DateAndTime,DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime','DisplayString','MacAddress','PhysAddress','RowStatus','TextualConvention')
dot1xAdvanced=ModuleIdentity((1,3,6,1,4,1,7244,2,36))
class Dot1xPortControlMode(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('forceUnauthorized',1),('auto',2),('forceAuthorized',3),('macBased',4)))
class Dot1xSessionTerminationAction(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),('reauthenticate',2)))
_AgentGuestVlanConfigGroup_ObjectIdentity=ObjectIdentity
agentGuestVlanConfigGroup=_AgentGuestVlanConfigGroup_ObjectIdentity((1,3,6,1,4,1,7244,2,36,1))
class _AgentGuestVlanSupplMode_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_AgentGuestVlanSupplMode_Type.__name__=_C
_AgentGuestVlanSupplMode_Object=MibScalar
agentGuestVlanSupplMode=_AgentGuestVlanSupplMode_Object((1,3,6,1,4,1,7244,2,36,1,1),_AgentGuestVlanSupplMode_Type())
agentGuestVlanSupplMode.setMaxAccess(_D)
if mibBuilder.loadTexts:agentGuestVlanSupplMode.setStatus(_A)
_AgentDot1xGuestVlanPortConfigTable_Object=MibTable
agentDot1xGuestVlanPortConfigTable=_AgentDot1xGuestVlanPortConfigTable_Object((1,3,6,1,4,1,7244,2,36,1,2))
if mibBuilder.loadTexts:agentDot1xGuestVlanPortConfigTable.setStatus(_A)
_AgentDot1xGuestVlanPortConfigEntry_Object=MibTableRow
agentDot1xGuestVlanPortConfigEntry=_AgentDot1xGuestVlanPortConfigEntry_Object((1,3,6,1,4,1,7244,2,36,1,2,1))
agentDot1xGuestVlanPortConfigEntry.setIndexNames((0,_I,_J))
if mibBuilder.loadTexts:agentDot1xGuestVlanPortConfigEntry.setStatus(_A)
class _AgentDot1xGuestVlanId_Type(Unsigned32):defaultValue=0
_AgentDot1xGuestVlanId_Type.__name__=_E
_AgentDot1xGuestVlanId_Object=MibTableColumn
agentDot1xGuestVlanId=_AgentDot1xGuestVlanId_Object((1,3,6,1,4,1,7244,2,36,1,2,1,1),_AgentDot1xGuestVlanId_Type())
agentDot1xGuestVlanId.setMaxAccess(_D)
if mibBuilder.loadTexts:agentDot1xGuestVlanId.setStatus(_A)
class _AgentDot1xGuestVlanPeriod_Type(Unsigned32):defaultValue=90;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_AgentDot1xGuestVlanPeriod_Type.__name__=_E
_AgentDot1xGuestVlanPeriod_Object=MibTableColumn
agentDot1xGuestVlanPeriod=_AgentDot1xGuestVlanPeriod_Object((1,3,6,1,4,1,7244,2,36,1,2,1,2),_AgentDot1xGuestVlanPeriod_Type())
agentDot1xGuestVlanPeriod.setMaxAccess(_D)
if mibBuilder.loadTexts:agentDot1xGuestVlanPeriod.setStatus(_A)
_AgentDot1xEnhancementConfigGroup_ObjectIdentity=ObjectIdentity
agentDot1xEnhancementConfigGroup=_AgentDot1xEnhancementConfigGroup_ObjectIdentity((1,3,6,1,4,1,7244,2,36,2))
class _AgentDot1xRadiusVlanAssignment_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_AgentDot1xRadiusVlanAssignment_Type.__name__=_C
_AgentDot1xRadiusVlanAssignment_Object=MibScalar
agentDot1xRadiusVlanAssignment=_AgentDot1xRadiusVlanAssignment_Object((1,3,6,1,4,1,7244,2,36,2,1),_AgentDot1xRadiusVlanAssignment_Type())
agentDot1xRadiusVlanAssignment.setMaxAccess(_D)
if mibBuilder.loadTexts:agentDot1xRadiusVlanAssignment.setStatus(_A)
class _AgentDot1xDynamicVlanCreationMode_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_AgentDot1xDynamicVlanCreationMode_Type.__name__=_C
_AgentDot1xDynamicVlanCreationMode_Object=MibScalar
agentDot1xDynamicVlanCreationMode=_AgentDot1xDynamicVlanCreationMode_Object((1,3,6,1,4,1,7244,2,36,2,2),_AgentDot1xDynamicVlanCreationMode_Type())
agentDot1xDynamicVlanCreationMode.setMaxAccess(_D)
if mibBuilder.loadTexts:agentDot1xDynamicVlanCreationMode.setStatus(_A)
_AgentDot1xClientGroup_ObjectIdentity=ObjectIdentity
agentDot1xClientGroup=_AgentDot1xClientGroup_ObjectIdentity((1,3,6,1,4,1,7244,2,36,3))
_AgentDot1xClientTable_Object=MibTable
agentDot1xClientTable=_AgentDot1xClientTable_Object((1,3,6,1,4,1,7244,2,36,3,1))
if mibBuilder.loadTexts:agentDot1xClientTable.setStatus(_A)
_AgentDot1xClientEntry_Object=MibTableRow
agentDot1xClientEntry=_AgentDot1xClientEntry_Object((1,3,6,1,4,1,7244,2,36,3,1,1))
agentDot1xClientEntry.setIndexNames((0,_K,_L))
if mibBuilder.loadTexts:agentDot1xClientEntry.setStatus(_A)
_AgentDot1xClientLogicalInterface_Type=Unsigned32
_AgentDot1xClientLogicalInterface_Object=MibTableColumn
agentDot1xClientLogicalInterface=_AgentDot1xClientLogicalInterface_Object((1,3,6,1,4,1,7244,2,36,3,1,1,1),_AgentDot1xClientLogicalInterface_Type())
agentDot1xClientLogicalInterface.setMaxAccess(_B)
if mibBuilder.loadTexts:agentDot1xClientLogicalInterface.setStatus(_A)
_AgentDot1xClientInterface_Type=DisplayString
_AgentDot1xClientInterface_Object=MibTableColumn
agentDot1xClientInterface=_AgentDot1xClientInterface_Object((1,3,6,1,4,1,7244,2,36,3,1,1,2),_AgentDot1xClientInterface_Type())
agentDot1xClientInterface.setMaxAccess(_B)
if mibBuilder.loadTexts:agentDot1xClientInterface.setStatus(_A)
_AgentDot1xClientUsername_Type=DisplayString
_AgentDot1xClientUsername_Object=MibTableColumn
agentDot1xClientUsername=_AgentDot1xClientUsername_Object((1,3,6,1,4,1,7244,2,36,3,1,1,3),_AgentDot1xClientUsername_Type())
agentDot1xClientUsername.setMaxAccess(_B)
if mibBuilder.loadTexts:agentDot1xClientUsername.setStatus(_A)
_AgentDot1xClientMacAddress_Type=PhysAddress
_AgentDot1xClientMacAddress_Object=MibTableColumn
agentDot1xClientMacAddress=_AgentDot1xClientMacAddress_Object((1,3,6,1,4,1,7244,2,36,3,1,1,4),_AgentDot1xClientMacAddress_Type())
agentDot1xClientMacAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:agentDot1xClientMacAddress.setStatus(_A)
_AgentDot1xClientSessionTime_Type=Unsigned32
_AgentDot1xClientSessionTime_Object=MibTableColumn
agentDot1xClientSessionTime=_AgentDot1xClientSessionTime_Object((1,3,6,1,4,1,7244,2,36,3,1,1,5),_AgentDot1xClientSessionTime_Type())
agentDot1xClientSessionTime.setMaxAccess(_B)
if mibBuilder.loadTexts:agentDot1xClientSessionTime.setStatus(_A)
_AgentDot1xClientVlanId_Type=Unsigned32
_AgentDot1xClientVlanId_Object=MibTableColumn
agentDot1xClientVlanId=_AgentDot1xClientVlanId_Object((1,3,6,1,4,1,7244,2,36,3,1,1,6),_AgentDot1xClientVlanId_Type())
agentDot1xClientVlanId.setMaxAccess(_B)
if mibBuilder.loadTexts:agentDot1xClientVlanId.setStatus(_A)
class _AgentDot1xClientVlanAssigned_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_F,1),(_M,2),('unauthenticated',3)))
_AgentDot1xClientVlanAssigned_Type.__name__=_C
_AgentDot1xClientVlanAssigned_Object=MibTableColumn
agentDot1xClientVlanAssigned=_AgentDot1xClientVlanAssigned_Object((1,3,6,1,4,1,7244,2,36,3,1,1,7),_AgentDot1xClientVlanAssigned_Type())
agentDot1xClientVlanAssigned.setMaxAccess(_B)
if mibBuilder.loadTexts:agentDot1xClientVlanAssigned.setStatus(_A)
_AgentDot1xClientSessionTimeout_Type=Unsigned32
_AgentDot1xClientSessionTimeout_Object=MibTableColumn
agentDot1xClientSessionTimeout=_AgentDot1xClientSessionTimeout_Object((1,3,6,1,4,1,7244,2,36,3,1,1,8),_AgentDot1xClientSessionTimeout_Type())
agentDot1xClientSessionTimeout.setMaxAccess(_B)
if mibBuilder.loadTexts:agentDot1xClientSessionTimeout.setStatus(_A)
class _AgentDot1xClientSessionTerminationAction_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_M,2)))
_AgentDot1xClientSessionTerminationAction_Type.__name__=_C
_AgentDot1xClientSessionTerminationAction_Object=MibTableColumn
agentDot1xClientSessionTerminationAction=_AgentDot1xClientSessionTerminationAction_Object((1,3,6,1,4,1,7244,2,36,3,1,1,9),_AgentDot1xClientSessionTerminationAction_Type())
agentDot1xClientSessionTerminationAction.setMaxAccess(_B)
if mibBuilder.loadTexts:agentDot1xClientSessionTerminationAction.setStatus(_A)
mibBuilder.exportSymbols(_K,**{'Dot1xPortControlMode':Dot1xPortControlMode,'Dot1xSessionTerminationAction':Dot1xSessionTerminationAction,'dot1xAdvanced':dot1xAdvanced,'agentGuestVlanConfigGroup':agentGuestVlanConfigGroup,'agentGuestVlanSupplMode':agentGuestVlanSupplMode,'agentDot1xGuestVlanPortConfigTable':agentDot1xGuestVlanPortConfigTable,'agentDot1xGuestVlanPortConfigEntry':agentDot1xGuestVlanPortConfigEntry,'agentDot1xGuestVlanId':agentDot1xGuestVlanId,'agentDot1xGuestVlanPeriod':agentDot1xGuestVlanPeriod,'agentDot1xEnhancementConfigGroup':agentDot1xEnhancementConfigGroup,'agentDot1xRadiusVlanAssignment':agentDot1xRadiusVlanAssignment,'agentDot1xDynamicVlanCreationMode':agentDot1xDynamicVlanCreationMode,'agentDot1xClientGroup':agentDot1xClientGroup,'agentDot1xClientTable':agentDot1xClientTable,'agentDot1xClientEntry':agentDot1xClientEntry,_L:agentDot1xClientLogicalInterface,'agentDot1xClientInterface':agentDot1xClientInterface,'agentDot1xClientUsername':agentDot1xClientUsername,'agentDot1xClientMacAddress':agentDot1xClientMacAddress,'agentDot1xClientSessionTime':agentDot1xClientSessionTime,'agentDot1xClientVlanId':agentDot1xClientVlanId,'agentDot1xClientVlanAssigned':agentDot1xClientVlanAssigned,'agentDot1xClientSessionTimeout':agentDot1xClientSessionTimeout,'agentDot1xClientSessionTerminationAction':agentDot1xClientSessionTerminationAction})