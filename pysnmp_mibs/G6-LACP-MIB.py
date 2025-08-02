_T='partnerStatusPortIndex'
_S='actorStatusPortIndex'
_R='portStatusPortIndex'
_Q='trunkConfigIndex'
_P='portConfigPortIndex'
_O='configIndex'
_N='enabled'
_M='disabled'
_L='fast'
_K='slow'
_J='active'
_I='passive'
_H='not-accessible'
_G='G6-LACP-MIB'
_F='read-write'
_E='true'
_D='false'
_C='read-only'
_B='Integer32'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
g6,=mibBuilder.importSymbols('MICROSENS-G6-MIB','g6')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_B,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,MacAddress,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress','TextualConvention')
protocol=ModuleIdentity((1,3,6,1,4,1,3181,10,6,2))
if mibBuilder.loadTexts:protocol.setRevisions(('2018-02-12 16:19',))
_Lacp_ObjectIdentity=ObjectIdentity
lacp=_Lacp_ObjectIdentity((1,3,6,1,4,1,3181,10,6,2,54))
class _LacpEnableLacp_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_M,0),(_N,1)))
_LacpEnableLacp_Type.__name__=_B
_LacpEnableLacp_Object=MibScalar
lacpEnableLacp=_LacpEnableLacp_Object((1,3,6,1,4,1,3181,10,6,2,54,1),_LacpEnableLacp_Type())
lacpEnableLacp.setMaxAccess(_F)
if mibBuilder.loadTexts:lacpEnableLacp.setStatus(_A)
_ConfigTable_Object=MibTable
configTable=_ConfigTable_Object((1,3,6,1,4,1,3181,10,6,2,54,2))
if mibBuilder.loadTexts:configTable.setStatus(_A)
_ConfigEntry_Object=MibTableRow
configEntry=_ConfigEntry_Object((1,3,6,1,4,1,3181,10,6,2,54,2,1))
configEntry.setIndexNames((0,_G,_O))
if mibBuilder.loadTexts:configEntry.setStatus(_A)
class _ConfigIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0))
_ConfigIndex_Type.__name__=_B
_ConfigIndex_Object=MibTableColumn
configIndex=_ConfigIndex_Object((1,3,6,1,4,1,3181,10,6,2,54,2,1,1),_ConfigIndex_Type())
configIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:configIndex.setStatus(_A)
class _ConfigLinkAggregation_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('static',0),('dynamic',1)))
_ConfigLinkAggregation_Type.__name__=_B
_ConfigLinkAggregation_Object=MibTableColumn
configLinkAggregation=_ConfigLinkAggregation_Object((1,3,6,1,4,1,3181,10,6,2,54,2,1,2),_ConfigLinkAggregation_Type())
configLinkAggregation.setMaxAccess(_F)
if mibBuilder.loadTexts:configLinkAggregation.setStatus(_A)
class _ConfigSystemPriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_ConfigSystemPriority_Type.__name__=_B
_ConfigSystemPriority_Object=MibTableColumn
configSystemPriority=_ConfigSystemPriority_Object((1,3,6,1,4,1,3181,10,6,2,54,2,1,3),_ConfigSystemPriority_Type())
configSystemPriority.setMaxAccess(_F)
if mibBuilder.loadTexts:configSystemPriority.setStatus(_A)
class _ConfigMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_I,0),(_J,1)))
_ConfigMode_Type.__name__=_B
_ConfigMode_Object=MibTableColumn
configMode=_ConfigMode_Object((1,3,6,1,4,1,3181,10,6,2,54,2,1,4),_ConfigMode_Type())
configMode.setMaxAccess(_F)
if mibBuilder.loadTexts:configMode.setStatus(_A)
class _ConfigTransmitInterval_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_K,0),(_L,1)))
_ConfigTransmitInterval_Type.__name__=_B
_ConfigTransmitInterval_Object=MibTableColumn
configTransmitInterval=_ConfigTransmitInterval_Object((1,3,6,1,4,1,3181,10,6,2,54,2,1,5),_ConfigTransmitInterval_Type())
configTransmitInterval.setMaxAccess(_F)
if mibBuilder.loadTexts:configTransmitInterval.setStatus(_A)
_PortConfigTable_Object=MibTable
portConfigTable=_PortConfigTable_Object((1,3,6,1,4,1,3181,10,6,2,54,3))
if mibBuilder.loadTexts:portConfigTable.setStatus(_A)
_PortConfigEntry_Object=MibTableRow
portConfigEntry=_PortConfigEntry_Object((1,3,6,1,4,1,3181,10,6,2,54,3,1))
portConfigEntry.setIndexNames((0,_G,_P))
if mibBuilder.loadTexts:portConfigEntry.setStatus(_A)
class _PortConfigPortIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,24))
_PortConfigPortIndex_Type.__name__=_B
_PortConfigPortIndex_Object=MibTableColumn
portConfigPortIndex=_PortConfigPortIndex_Object((1,3,6,1,4,1,3181,10,6,2,54,3,1,1),_PortConfigPortIndex_Type())
portConfigPortIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:portConfigPortIndex.setStatus(_A)
class _PortConfigTrunkId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_PortConfigTrunkId_Type.__name__=_B
_PortConfigTrunkId_Object=MibTableColumn
portConfigTrunkId=_PortConfigTrunkId_Object((1,3,6,1,4,1,3181,10,6,2,54,3,1,2),_PortConfigTrunkId_Type())
portConfigTrunkId.setMaxAccess(_F)
if mibBuilder.loadTexts:portConfigTrunkId.setStatus(_A)
_TrunkConfigTable_Object=MibTable
trunkConfigTable=_TrunkConfigTable_Object((1,3,6,1,4,1,3181,10,6,2,54,4))
if mibBuilder.loadTexts:trunkConfigTable.setStatus(_A)
_TrunkConfigEntry_Object=MibTableRow
trunkConfigEntry=_TrunkConfigEntry_Object((1,3,6,1,4,1,3181,10,6,2,54,4,1))
trunkConfigEntry.setIndexNames((0,_G,_Q))
if mibBuilder.loadTexts:trunkConfigEntry.setStatus(_A)
class _TrunkConfigIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,15))
_TrunkConfigIndex_Type.__name__=_B
_TrunkConfigIndex_Object=MibTableColumn
trunkConfigIndex=_TrunkConfigIndex_Object((1,3,6,1,4,1,3181,10,6,2,54,4,1,1),_TrunkConfigIndex_Type())
trunkConfigIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:trunkConfigIndex.setStatus(_A)
_TrunkConfigName_Type=DisplayString
_TrunkConfigName_Object=MibTableColumn
trunkConfigName=_TrunkConfigName_Object((1,3,6,1,4,1,3181,10,6,2,54,4,1,2),_TrunkConfigName_Type())
trunkConfigName.setMaxAccess(_F)
if mibBuilder.loadTexts:trunkConfigName.setStatus(_A)
class _TrunkConfigTrunkEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_M,0),(_N,1)))
_TrunkConfigTrunkEnable_Type.__name__=_B
_TrunkConfigTrunkEnable_Object=MibTableColumn
trunkConfigTrunkEnable=_TrunkConfigTrunkEnable_Object((1,3,6,1,4,1,3181,10,6,2,54,4,1,3),_TrunkConfigTrunkEnable_Type())
trunkConfigTrunkEnable.setMaxAccess(_F)
if mibBuilder.loadTexts:trunkConfigTrunkEnable.setStatus(_A)
_PortStatusTable_Object=MibTable
portStatusTable=_PortStatusTable_Object((1,3,6,1,4,1,3181,10,6,2,54,100))
if mibBuilder.loadTexts:portStatusTable.setStatus(_A)
_PortStatusEntry_Object=MibTableRow
portStatusEntry=_PortStatusEntry_Object((1,3,6,1,4,1,3181,10,6,2,54,100,1))
portStatusEntry.setIndexNames((0,_G,_R))
if mibBuilder.loadTexts:portStatusEntry.setStatus(_A)
class _PortStatusPortIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,24))
_PortStatusPortIndex_Type.__name__=_B
_PortStatusPortIndex_Object=MibTableColumn
portStatusPortIndex=_PortStatusPortIndex_Object((1,3,6,1,4,1,3181,10,6,2,54,100,1,1),_PortStatusPortIndex_Type())
portStatusPortIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:portStatusPortIndex.setStatus(_A)
_PortStatusTrunkName_Type=DisplayString
_PortStatusTrunkName_Object=MibTableColumn
portStatusTrunkName=_PortStatusTrunkName_Object((1,3,6,1,4,1,3181,10,6,2,54,100,1,2),_PortStatusTrunkName_Type())
portStatusTrunkName.setMaxAccess(_C)
if mibBuilder.loadTexts:portStatusTrunkName.setStatus(_A)
class _PortStatusTrunkId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_PortStatusTrunkId_Type.__name__=_B
_PortStatusTrunkId_Object=MibTableColumn
portStatusTrunkId=_PortStatusTrunkId_Object((1,3,6,1,4,1,3181,10,6,2,54,100,1,3),_PortStatusTrunkId_Type())
portStatusTrunkId.setMaxAccess(_C)
if mibBuilder.loadTexts:portStatusTrunkId.setStatus(_A)
class _PortStatusActivityMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_I,0),(_J,1)))
_PortStatusActivityMode_Type.__name__=_B
_PortStatusActivityMode_Object=MibTableColumn
portStatusActivityMode=_PortStatusActivityMode_Object((1,3,6,1,4,1,3181,10,6,2,54,100,1,4),_PortStatusActivityMode_Type())
portStatusActivityMode.setMaxAccess(_C)
if mibBuilder.loadTexts:portStatusActivityMode.setStatus(_A)
class _PortStatusSynchronized_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_D,0),(_E,1)))
_PortStatusSynchronized_Type.__name__=_B
_PortStatusSynchronized_Object=MibTableColumn
portStatusSynchronized=_PortStatusSynchronized_Object((1,3,6,1,4,1,3181,10,6,2,54,100,1,5),_PortStatusSynchronized_Type())
portStatusSynchronized.setMaxAccess(_C)
if mibBuilder.loadTexts:portStatusSynchronized.setStatus(_A)
class _PortStatusAggregationPossible_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_D,0),(_E,1)))
_PortStatusAggregationPossible_Type.__name__=_B
_PortStatusAggregationPossible_Object=MibTableColumn
portStatusAggregationPossible=_PortStatusAggregationPossible_Object((1,3,6,1,4,1,3181,10,6,2,54,100,1,6),_PortStatusAggregationPossible_Type())
portStatusAggregationPossible.setMaxAccess(_C)
if mibBuilder.loadTexts:portStatusAggregationPossible.setStatus(_A)
class _PortStatusCollection_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_D,0),(_E,1)))
_PortStatusCollection_Type.__name__=_B
_PortStatusCollection_Object=MibTableColumn
portStatusCollection=_PortStatusCollection_Object((1,3,6,1,4,1,3181,10,6,2,54,100,1,7),_PortStatusCollection_Type())
portStatusCollection.setMaxAccess(_C)
if mibBuilder.loadTexts:portStatusCollection.setStatus(_A)
class _PortStatusDistribution_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_D,0),(_E,1)))
_PortStatusDistribution_Type.__name__=_B
_PortStatusDistribution_Object=MibTableColumn
portStatusDistribution=_PortStatusDistribution_Object((1,3,6,1,4,1,3181,10,6,2,54,100,1,8),_PortStatusDistribution_Type())
portStatusDistribution.setMaxAccess(_C)
if mibBuilder.loadTexts:portStatusDistribution.setStatus(_A)
class _PortStatusExpiredState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_D,0),(_E,1)))
_PortStatusExpiredState_Type.__name__=_B
_PortStatusExpiredState_Object=MibTableColumn
portStatusExpiredState=_PortStatusExpiredState_Object((1,3,6,1,4,1,3181,10,6,2,54,100,1,9),_PortStatusExpiredState_Type())
portStatusExpiredState.setMaxAccess(_C)
if mibBuilder.loadTexts:portStatusExpiredState.setStatus(_A)
class _PortStatusDefaultedState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_D,0),(_E,1)))
_PortStatusDefaultedState_Type.__name__=_B
_PortStatusDefaultedState_Object=MibTableColumn
portStatusDefaultedState=_PortStatusDefaultedState_Object((1,3,6,1,4,1,3181,10,6,2,54,100,1,10),_PortStatusDefaultedState_Type())
portStatusDefaultedState.setMaxAccess(_C)
if mibBuilder.loadTexts:portStatusDefaultedState.setStatus(_A)
_ActorStatusTable_Object=MibTable
actorStatusTable=_ActorStatusTable_Object((1,3,6,1,4,1,3181,10,6,2,54,101))
if mibBuilder.loadTexts:actorStatusTable.setStatus(_A)
_ActorStatusEntry_Object=MibTableRow
actorStatusEntry=_ActorStatusEntry_Object((1,3,6,1,4,1,3181,10,6,2,54,101,1))
actorStatusEntry.setIndexNames((0,_G,_S))
if mibBuilder.loadTexts:actorStatusEntry.setStatus(_A)
class _ActorStatusPortIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,24))
_ActorStatusPortIndex_Type.__name__=_B
_ActorStatusPortIndex_Object=MibTableColumn
actorStatusPortIndex=_ActorStatusPortIndex_Object((1,3,6,1,4,1,3181,10,6,2,54,101,1,1),_ActorStatusPortIndex_Type())
actorStatusPortIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:actorStatusPortIndex.setStatus(_A)
class _ActorStatusSystemPriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_ActorStatusSystemPriority_Type.__name__=_B
_ActorStatusSystemPriority_Object=MibTableColumn
actorStatusSystemPriority=_ActorStatusSystemPriority_Object((1,3,6,1,4,1,3181,10,6,2,54,101,1,2),_ActorStatusSystemPriority_Type())
actorStatusSystemPriority.setMaxAccess(_C)
if mibBuilder.loadTexts:actorStatusSystemPriority.setStatus(_A)
_ActorStatusSystemId_Type=MacAddress
_ActorStatusSystemId_Object=MibTableColumn
actorStatusSystemId=_ActorStatusSystemId_Object((1,3,6,1,4,1,3181,10,6,2,54,101,1,3),_ActorStatusSystemId_Type())
actorStatusSystemId.setMaxAccess(_C)
if mibBuilder.loadTexts:actorStatusSystemId.setStatus(_A)
class _ActorStatusPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_ActorStatusPort_Type.__name__=_B
_ActorStatusPort_Object=MibTableColumn
actorStatusPort=_ActorStatusPort_Object((1,3,6,1,4,1,3181,10,6,2,54,101,1,4),_ActorStatusPort_Type())
actorStatusPort.setMaxAccess(_C)
if mibBuilder.loadTexts:actorStatusPort.setStatus(_A)
class _ActorStatusPriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_ActorStatusPriority_Type.__name__=_B
_ActorStatusPriority_Object=MibTableColumn
actorStatusPriority=_ActorStatusPriority_Object((1,3,6,1,4,1,3181,10,6,2,54,101,1,5),_ActorStatusPriority_Type())
actorStatusPriority.setMaxAccess(_C)
if mibBuilder.loadTexts:actorStatusPriority.setStatus(_A)
class _ActorStatusAdminKey_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_ActorStatusAdminKey_Type.__name__=_B
_ActorStatusAdminKey_Object=MibTableColumn
actorStatusAdminKey=_ActorStatusAdminKey_Object((1,3,6,1,4,1,3181,10,6,2,54,101,1,6),_ActorStatusAdminKey_Type())
actorStatusAdminKey.setMaxAccess(_C)
if mibBuilder.loadTexts:actorStatusAdminKey.setStatus(_A)
class _ActorStatusOperKey_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_ActorStatusOperKey_Type.__name__=_B
_ActorStatusOperKey_Object=MibTableColumn
actorStatusOperKey=_ActorStatusOperKey_Object((1,3,6,1,4,1,3181,10,6,2,54,101,1,7),_ActorStatusOperKey_Type())
actorStatusOperKey.setMaxAccess(_C)
if mibBuilder.loadTexts:actorStatusOperKey.setStatus(_A)
class _ActorStatusTransmitInterval_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_K,0),(_L,1)))
_ActorStatusTransmitInterval_Type.__name__=_B
_ActorStatusTransmitInterval_Object=MibTableColumn
actorStatusTransmitInterval=_ActorStatusTransmitInterval_Object((1,3,6,1,4,1,3181,10,6,2,54,101,1,8),_ActorStatusTransmitInterval_Type())
actorStatusTransmitInterval.setMaxAccess(_C)
if mibBuilder.loadTexts:actorStatusTransmitInterval.setStatus(_A)
_PartnerStatusTable_Object=MibTable
partnerStatusTable=_PartnerStatusTable_Object((1,3,6,1,4,1,3181,10,6,2,54,102))
if mibBuilder.loadTexts:partnerStatusTable.setStatus(_A)
_PartnerStatusEntry_Object=MibTableRow
partnerStatusEntry=_PartnerStatusEntry_Object((1,3,6,1,4,1,3181,10,6,2,54,102,1))
partnerStatusEntry.setIndexNames((0,_G,_T))
if mibBuilder.loadTexts:partnerStatusEntry.setStatus(_A)
class _PartnerStatusPortIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,24))
_PartnerStatusPortIndex_Type.__name__=_B
_PartnerStatusPortIndex_Object=MibTableColumn
partnerStatusPortIndex=_PartnerStatusPortIndex_Object((1,3,6,1,4,1,3181,10,6,2,54,102,1,1),_PartnerStatusPortIndex_Type())
partnerStatusPortIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:partnerStatusPortIndex.setStatus(_A)
class _PartnerStatusSystemPriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_PartnerStatusSystemPriority_Type.__name__=_B
_PartnerStatusSystemPriority_Object=MibTableColumn
partnerStatusSystemPriority=_PartnerStatusSystemPriority_Object((1,3,6,1,4,1,3181,10,6,2,54,102,1,2),_PartnerStatusSystemPriority_Type())
partnerStatusSystemPriority.setMaxAccess(_C)
if mibBuilder.loadTexts:partnerStatusSystemPriority.setStatus(_A)
_PartnerStatusSystemId_Type=MacAddress
_PartnerStatusSystemId_Object=MibTableColumn
partnerStatusSystemId=_PartnerStatusSystemId_Object((1,3,6,1,4,1,3181,10,6,2,54,102,1,3),_PartnerStatusSystemId_Type())
partnerStatusSystemId.setMaxAccess(_C)
if mibBuilder.loadTexts:partnerStatusSystemId.setStatus(_A)
class _PartnerStatusPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_PartnerStatusPort_Type.__name__=_B
_PartnerStatusPort_Object=MibTableColumn
partnerStatusPort=_PartnerStatusPort_Object((1,3,6,1,4,1,3181,10,6,2,54,102,1,4),_PartnerStatusPort_Type())
partnerStatusPort.setMaxAccess(_C)
if mibBuilder.loadTexts:partnerStatusPort.setStatus(_A)
class _PartnerStatusPriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_PartnerStatusPriority_Type.__name__=_B
_PartnerStatusPriority_Object=MibTableColumn
partnerStatusPriority=_PartnerStatusPriority_Object((1,3,6,1,4,1,3181,10,6,2,54,102,1,5),_PartnerStatusPriority_Type())
partnerStatusPriority.setMaxAccess(_C)
if mibBuilder.loadTexts:partnerStatusPriority.setStatus(_A)
class _PartnerStatusAdminKey_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_PartnerStatusAdminKey_Type.__name__=_B
_PartnerStatusAdminKey_Object=MibTableColumn
partnerStatusAdminKey=_PartnerStatusAdminKey_Object((1,3,6,1,4,1,3181,10,6,2,54,102,1,6),_PartnerStatusAdminKey_Type())
partnerStatusAdminKey.setMaxAccess(_C)
if mibBuilder.loadTexts:partnerStatusAdminKey.setStatus(_A)
class _PartnerStatusOperKey_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_PartnerStatusOperKey_Type.__name__=_B
_PartnerStatusOperKey_Object=MibTableColumn
partnerStatusOperKey=_PartnerStatusOperKey_Object((1,3,6,1,4,1,3181,10,6,2,54,102,1,7),_PartnerStatusOperKey_Type())
partnerStatusOperKey.setMaxAccess(_C)
if mibBuilder.loadTexts:partnerStatusOperKey.setStatus(_A)
class _PartnerStatusReceiveInterval_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_K,0),(_L,1)))
_PartnerStatusReceiveInterval_Type.__name__=_B
_PartnerStatusReceiveInterval_Object=MibTableColumn
partnerStatusReceiveInterval=_PartnerStatusReceiveInterval_Object((1,3,6,1,4,1,3181,10,6,2,54,102,1,8),_PartnerStatusReceiveInterval_Type())
partnerStatusReceiveInterval.setMaxAccess(_C)
if mibBuilder.loadTexts:partnerStatusReceiveInterval.setStatus(_A)
class _PartnerStatusActivityMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_I,0),(_J,1)))
_PartnerStatusActivityMode_Type.__name__=_B
_PartnerStatusActivityMode_Object=MibTableColumn
partnerStatusActivityMode=_PartnerStatusActivityMode_Object((1,3,6,1,4,1,3181,10,6,2,54,102,1,9),_PartnerStatusActivityMode_Type())
partnerStatusActivityMode.setMaxAccess(_C)
if mibBuilder.loadTexts:partnerStatusActivityMode.setStatus(_A)
class _PartnerStatusSynchronized_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_D,0),(_E,1)))
_PartnerStatusSynchronized_Type.__name__=_B
_PartnerStatusSynchronized_Object=MibTableColumn
partnerStatusSynchronized=_PartnerStatusSynchronized_Object((1,3,6,1,4,1,3181,10,6,2,54,102,1,10),_PartnerStatusSynchronized_Type())
partnerStatusSynchronized.setMaxAccess(_C)
if mibBuilder.loadTexts:partnerStatusSynchronized.setStatus(_A)
class _PartnerStatusAggregationPossible_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_D,0),(_E,1)))
_PartnerStatusAggregationPossible_Type.__name__=_B
_PartnerStatusAggregationPossible_Object=MibTableColumn
partnerStatusAggregationPossible=_PartnerStatusAggregationPossible_Object((1,3,6,1,4,1,3181,10,6,2,54,102,1,11),_PartnerStatusAggregationPossible_Type())
partnerStatusAggregationPossible.setMaxAccess(_C)
if mibBuilder.loadTexts:partnerStatusAggregationPossible.setStatus(_A)
class _PartnerStatusCollection_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_D,0),(_E,1)))
_PartnerStatusCollection_Type.__name__=_B
_PartnerStatusCollection_Object=MibTableColumn
partnerStatusCollection=_PartnerStatusCollection_Object((1,3,6,1,4,1,3181,10,6,2,54,102,1,12),_PartnerStatusCollection_Type())
partnerStatusCollection.setMaxAccess(_C)
if mibBuilder.loadTexts:partnerStatusCollection.setStatus(_A)
class _PartnerStatusDistribution_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_D,0),(_E,1)))
_PartnerStatusDistribution_Type.__name__=_B
_PartnerStatusDistribution_Object=MibTableColumn
partnerStatusDistribution=_PartnerStatusDistribution_Object((1,3,6,1,4,1,3181,10,6,2,54,102,1,13),_PartnerStatusDistribution_Type())
partnerStatusDistribution.setMaxAccess(_C)
if mibBuilder.loadTexts:partnerStatusDistribution.setStatus(_A)
class _PartnerStatusExpiredState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_D,0),(_E,1)))
_PartnerStatusExpiredState_Type.__name__=_B
_PartnerStatusExpiredState_Object=MibTableColumn
partnerStatusExpiredState=_PartnerStatusExpiredState_Object((1,3,6,1,4,1,3181,10,6,2,54,102,1,14),_PartnerStatusExpiredState_Type())
partnerStatusExpiredState.setMaxAccess(_C)
if mibBuilder.loadTexts:partnerStatusExpiredState.setStatus(_A)
class _PartnerStatusDefaultedState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_D,0),(_E,1)))
_PartnerStatusDefaultedState_Type.__name__=_B
_PartnerStatusDefaultedState_Object=MibTableColumn
partnerStatusDefaultedState=_PartnerStatusDefaultedState_Object((1,3,6,1,4,1,3181,10,6,2,54,102,1,15),_PartnerStatusDefaultedState_Type())
partnerStatusDefaultedState.setMaxAccess(_C)
if mibBuilder.loadTexts:partnerStatusDefaultedState.setStatus(_A)
mibBuilder.exportSymbols(_G,**{'protocol':protocol,'lacp':lacp,'lacpEnableLacp':lacpEnableLacp,'configTable':configTable,'configEntry':configEntry,_O:configIndex,'configLinkAggregation':configLinkAggregation,'configSystemPriority':configSystemPriority,'configMode':configMode,'configTransmitInterval':configTransmitInterval,'portConfigTable':portConfigTable,'portConfigEntry':portConfigEntry,_P:portConfigPortIndex,'portConfigTrunkId':portConfigTrunkId,'trunkConfigTable':trunkConfigTable,'trunkConfigEntry':trunkConfigEntry,_Q:trunkConfigIndex,'trunkConfigName':trunkConfigName,'trunkConfigTrunkEnable':trunkConfigTrunkEnable,'portStatusTable':portStatusTable,'portStatusEntry':portStatusEntry,_R:portStatusPortIndex,'portStatusTrunkName':portStatusTrunkName,'portStatusTrunkId':portStatusTrunkId,'portStatusActivityMode':portStatusActivityMode,'portStatusSynchronized':portStatusSynchronized,'portStatusAggregationPossible':portStatusAggregationPossible,'portStatusCollection':portStatusCollection,'portStatusDistribution':portStatusDistribution,'portStatusExpiredState':portStatusExpiredState,'portStatusDefaultedState':portStatusDefaultedState,'actorStatusTable':actorStatusTable,'actorStatusEntry':actorStatusEntry,_S:actorStatusPortIndex,'actorStatusSystemPriority':actorStatusSystemPriority,'actorStatusSystemId':actorStatusSystemId,'actorStatusPort':actorStatusPort,'actorStatusPriority':actorStatusPriority,'actorStatusAdminKey':actorStatusAdminKey,'actorStatusOperKey':actorStatusOperKey,'actorStatusTransmitInterval':actorStatusTransmitInterval,'partnerStatusTable':partnerStatusTable,'partnerStatusEntry':partnerStatusEntry,_T:partnerStatusPortIndex,'partnerStatusSystemPriority':partnerStatusSystemPriority,'partnerStatusSystemId':partnerStatusSystemId,'partnerStatusPort':partnerStatusPort,'partnerStatusPriority':partnerStatusPriority,'partnerStatusAdminKey':partnerStatusAdminKey,'partnerStatusOperKey':partnerStatusOperKey,'partnerStatusReceiveInterval':partnerStatusReceiveInterval,'partnerStatusActivityMode':partnerStatusActivityMode,'partnerStatusSynchronized':partnerStatusSynchronized,'partnerStatusAggregationPossible':partnerStatusAggregationPossible,'partnerStatusCollection':partnerStatusCollection,'partnerStatusDistribution':partnerStatusDistribution,'partnerStatusExpiredState':partnerStatusExpiredState,'partnerStatusDefaultedState':partnerStatusDefaultedState})