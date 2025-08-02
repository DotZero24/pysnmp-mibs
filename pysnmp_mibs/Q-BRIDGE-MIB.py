_Av='qBridgeClassificationPortGroup'
_Au='qBridgeClassificationDeviceGroup'
_At='qBridgePortGroup2'
_As='qBridgePortGroup'
_Ar='dot1qPortRestrictedVlanRegistration'
_Aq='dot1vProtocolPortRowStatus'
_Ap='dot1vProtocolPortGroupVid'
_Ao='dot1vProtocolGroupRowStatus'
_An='dot1vProtocolGroupId'
_Am='dot1qConstraintTypeDefault'
_Al='dot1qConstraintSetDefault'
_Ak='dot1qConstraintStatus'
_Aj='dot1qConstraintType'
_Ai='dot1qTpVlanPortHCInDiscards'
_Ah='dot1qTpVlanPortHCOutFrames'
_Ag='dot1qTpVlanPortHCInFrames'
_Af='dot1qTpVlanPortInOverflowDiscards'
_Ae='dot1qTpVlanPortOutOverflowFrames'
_Ad='dot1qTpVlanPortInOverflowFrames'
_Ac='dot1qTpVlanPortInDiscards'
_Ab='dot1qTpVlanPortOutFrames'
_Aa='dot1qTpVlanPortInFrames'
_AZ='deprecated'
_AY='dot1qNextFreeLocalVlanIndex'
_AX='dot1qVlanStaticRowStatus'
_AW='dot1qVlanStaticUntaggedPorts'
_AV='dot1qVlanForbiddenEgressPorts'
_AU='dot1qVlanStaticEgressPorts'
_AT='dot1qVlanStaticName'
_AS='dot1qVlanCreationTime'
_AR='dot1qVlanStatus'
_AQ='dot1qVlanCurrentUntaggedPorts'
_AP='dot1qVlanCurrentEgressPorts'
_AO='dot1qVlanFdbId'
_AN='dot1qVlanNumDeletes'
_AM='dot1qStaticMulticastStatus'
_AL='dot1qStaticMulticastForbiddenEgressPorts'
_AK='dot1qStaticMulticastStaticEgressPorts'
_AJ='dot1qStaticUnicastStatus'
_AI='dot1qStaticUnicastAllowedToGoTo'
_AH='dot1qForwardUnregisteredForbiddenPorts'
_AG='dot1qForwardUnregisteredStaticPorts'
_AF='dot1qForwardUnregisteredPorts'
_AE='dot1qForwardAllForbiddenPorts'
_AD='dot1qForwardAllStaticPorts'
_AC='dot1qForwardAllPorts'
_AB='dot1qTpGroupLearnt'
_AA='dot1qTpGroupEgressPorts'
_A9='dot1qTpFdbStatus'
_A8='dot1qTpFdbPort'
_A7='dot1qFdbDynamicCount'
_A6='dot1qGvrpStatus'
_A5='dot1qNumVlans'
_A4='dot1qMaxSupportedVlans'
_A3='dot1qMaxVlanId'
_A2='dot1qVlanVersionNumber'
_A1='dot1qPortVlanEntry'
_A0='dot1vProtocolPortGroupId'
_z='dot1vProtocolTemplateProtocolValue'
_y='dot1vProtocolTemplateFrameType'
_x='shared'
_w='independent'
_v='dot1qConstraintSet'
_u='dot1qConstraintVlan'
_t='VlanIndex'
_s='dot1qVlanTimeMark'
_r='dot1qStaticMulticastReceivePort'
_q='dot1qStaticMulticastAddress'
_p='deleteOnTimeout'
_o='deleteOnReset'
_n='dot1qStaticUnicastReceivePort'
_m='dot1qStaticUnicastAddress'
_l='dot1qTpGroupAddress'
_k='dot1qTpFdbAddress'
_j='SnmpAdminString'
_i='OctetString'
_h='qBridgeLearningConstraintDefaultGroup'
_g='qBridgeLearningConstraintsGroup'
_f='qBridgeVlanHCStatisticsGroup'
_e='qBridgeVlanStatisticsOverflowGroup'
_d='qBridgeVlanStatisticsGroup'
_c='qBridgeFdbStaticGroup'
_b='qBridgeServiceRequirementsGroup'
_a='qBridgeFdbMulticastGroup'
_Z='qBridgeFdbUnicastGroup'
_Y='qBridgeVlanStaticGroup'
_X='qBridgeVlanGroup'
_W='qBridgeBaseGroup'
_V='dot1qPortGvrpLastPduOrigin'
_U='dot1qPortGvrpFailedRegistrations'
_T='dot1qPortGvrpStatus'
_S='dot1qPortIngressFiltering'
_R='dot1qPortAcceptableFrameTypes'
_Q='dot1qPvid'
_P='permanent'
_O='invalid'
_N='TruthValue'
_M='EnabledStatus'
_L='other'
_K='dot1qFdbId'
_J='dot1dBasePort'
_I='BRIDGE-MIB'
_H='dot1qVlanIndex'
_G='read-create'
_F='not-accessible'
_E='read-write'
_D='Integer32'
_C='read-only'
_B='Q-BRIDGE-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_i,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
dot1dBasePort,dot1dBasePortEntry,dot1dBridge=mibBuilder.importSymbols(_I,_J,'dot1dBasePortEntry','dot1dBridge')
EnabledStatus,=mibBuilder.importSymbols('P-BRIDGE-MIB',_M)
TimeFilter,=mibBuilder.importSymbols('RMON2-MIB','TimeFilter')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB',_j)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress','RowStatus','TextualConvention',_N)
qBridgeMIB=ModuleIdentity((1,3,6,1,2,1,17,7))
if mibBuilder.loadTexts:qBridgeMIB.setRevisions(('2006-01-09 00:00','1999-08-25 00:00'))
class PortList(TextualConvention,OctetString):status=_A
class VlanIndex(TextualConvention,Unsigned32):status=_A;displayHint='d'
class VlanId(TextualConvention,Integer32):status=_A;displayHint='d';subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094))
class VlanIdOrAny(TextualConvention,Integer32):status=_A;displayHint='d';subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094),ValueRangeConstraint(4095,4095))
class VlanIdOrNone(TextualConvention,Integer32):status=_A;displayHint='d';subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,4094))
class VlanIdOrAnyOrNone(TextualConvention,Integer32):status=_A;displayHint='d';subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,4094),ValueRangeConstraint(4095,4095))
_QBridgeMIBObjects_ObjectIdentity=ObjectIdentity
qBridgeMIBObjects=_QBridgeMIBObjects_ObjectIdentity((1,3,6,1,2,1,17,7,1))
_Dot1qBase_ObjectIdentity=ObjectIdentity
dot1qBase=_Dot1qBase_ObjectIdentity((1,3,6,1,2,1,17,7,1,1))
class _Dot1qVlanVersionNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues(('version1',1))
_Dot1qVlanVersionNumber_Type.__name__=_D
_Dot1qVlanVersionNumber_Object=MibScalar
dot1qVlanVersionNumber=_Dot1qVlanVersionNumber_Object((1,3,6,1,2,1,17,7,1,1,1),_Dot1qVlanVersionNumber_Type())
dot1qVlanVersionNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:dot1qVlanVersionNumber.setStatus(_A)
_Dot1qMaxVlanId_Type=VlanId
_Dot1qMaxVlanId_Object=MibScalar
dot1qMaxVlanId=_Dot1qMaxVlanId_Object((1,3,6,1,2,1,17,7,1,1,2),_Dot1qMaxVlanId_Type())
dot1qMaxVlanId.setMaxAccess(_C)
if mibBuilder.loadTexts:dot1qMaxVlanId.setStatus(_A)
_Dot1qMaxSupportedVlans_Type=Unsigned32
_Dot1qMaxSupportedVlans_Object=MibScalar
dot1qMaxSupportedVlans=_Dot1qMaxSupportedVlans_Object((1,3,6,1,2,1,17,7,1,1,3),_Dot1qMaxSupportedVlans_Type())
dot1qMaxSupportedVlans.setMaxAccess(_C)
if mibBuilder.loadTexts:dot1qMaxSupportedVlans.setStatus(_A)
_Dot1qNumVlans_Type=Unsigned32
_Dot1qNumVlans_Object=MibScalar
dot1qNumVlans=_Dot1qNumVlans_Object((1,3,6,1,2,1,17,7,1,1,4),_Dot1qNumVlans_Type())
dot1qNumVlans.setMaxAccess(_C)
if mibBuilder.loadTexts:dot1qNumVlans.setStatus(_A)
class _Dot1qGvrpStatus_Type(EnabledStatus):defaultValue=1
_Dot1qGvrpStatus_Type.__name__=_M
_Dot1qGvrpStatus_Object=MibScalar
dot1qGvrpStatus=_Dot1qGvrpStatus_Object((1,3,6,1,2,1,17,7,1,1,5),_Dot1qGvrpStatus_Type())
dot1qGvrpStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:dot1qGvrpStatus.setStatus(_A)
_Dot1qTp_ObjectIdentity=ObjectIdentity
dot1qTp=_Dot1qTp_ObjectIdentity((1,3,6,1,2,1,17,7,1,2))
_Dot1qFdbTable_Object=MibTable
dot1qFdbTable=_Dot1qFdbTable_Object((1,3,6,1,2,1,17,7,1,2,1))
if mibBuilder.loadTexts:dot1qFdbTable.setStatus(_A)
_Dot1qFdbEntry_Object=MibTableRow
dot1qFdbEntry=_Dot1qFdbEntry_Object((1,3,6,1,2,1,17,7,1,2,1,1))
dot1qFdbEntry.setIndexNames((0,_B,_K))
if mibBuilder.loadTexts:dot1qFdbEntry.setStatus(_A)
_Dot1qFdbId_Type=Unsigned32
_Dot1qFdbId_Object=MibTableColumn
dot1qFdbId=_Dot1qFdbId_Object((1,3,6,1,2,1,17,7,1,2,1,1,1),_Dot1qFdbId_Type())
dot1qFdbId.setMaxAccess(_F)
if mibBuilder.loadTexts:dot1qFdbId.setStatus(_A)
_Dot1qFdbDynamicCount_Type=Counter32
_Dot1qFdbDynamicCount_Object=MibTableColumn
dot1qFdbDynamicCount=_Dot1qFdbDynamicCount_Object((1,3,6,1,2,1,17,7,1,2,1,1,2),_Dot1qFdbDynamicCount_Type())
dot1qFdbDynamicCount.setMaxAccess(_C)
if mibBuilder.loadTexts:dot1qFdbDynamicCount.setStatus(_A)
_Dot1qTpFdbTable_Object=MibTable
dot1qTpFdbTable=_Dot1qTpFdbTable_Object((1,3,6,1,2,1,17,7,1,2,2))
if mibBuilder.loadTexts:dot1qTpFdbTable.setStatus(_A)
_Dot1qTpFdbEntry_Object=MibTableRow
dot1qTpFdbEntry=_Dot1qTpFdbEntry_Object((1,3,6,1,2,1,17,7,1,2,2,1))
dot1qTpFdbEntry.setIndexNames((0,_B,_K),(0,_B,_k))
if mibBuilder.loadTexts:dot1qTpFdbEntry.setStatus(_A)
_Dot1qTpFdbAddress_Type=MacAddress
_Dot1qTpFdbAddress_Object=MibTableColumn
dot1qTpFdbAddress=_Dot1qTpFdbAddress_Object((1,3,6,1,2,1,17,7,1,2,2,1,1),_Dot1qTpFdbAddress_Type())
dot1qTpFdbAddress.setMaxAccess(_F)
if mibBuilder.loadTexts:dot1qTpFdbAddress.setStatus(_A)
class _Dot1qTpFdbPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_Dot1qTpFdbPort_Type.__name__=_D
_Dot1qTpFdbPort_Object=MibTableColumn
dot1qTpFdbPort=_Dot1qTpFdbPort_Object((1,3,6,1,2,1,17,7,1,2,2,1,2),_Dot1qTpFdbPort_Type())
dot1qTpFdbPort.setMaxAccess(_C)
if mibBuilder.loadTexts:dot1qTpFdbPort.setStatus(_A)
class _Dot1qTpFdbStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_L,1),(_O,2),('learned',3),('self',4),('mgmt',5)))
_Dot1qTpFdbStatus_Type.__name__=_D
_Dot1qTpFdbStatus_Object=MibTableColumn
dot1qTpFdbStatus=_Dot1qTpFdbStatus_Object((1,3,6,1,2,1,17,7,1,2,2,1,3),_Dot1qTpFdbStatus_Type())
dot1qTpFdbStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:dot1qTpFdbStatus.setStatus(_A)
_Dot1qTpGroupTable_Object=MibTable
dot1qTpGroupTable=_Dot1qTpGroupTable_Object((1,3,6,1,2,1,17,7,1,2,3))
if mibBuilder.loadTexts:dot1qTpGroupTable.setStatus(_A)
_Dot1qTpGroupEntry_Object=MibTableRow
dot1qTpGroupEntry=_Dot1qTpGroupEntry_Object((1,3,6,1,2,1,17,7,1,2,3,1))
dot1qTpGroupEntry.setIndexNames((0,_B,_H),(0,_B,_l))
if mibBuilder.loadTexts:dot1qTpGroupEntry.setStatus(_A)
_Dot1qTpGroupAddress_Type=MacAddress
_Dot1qTpGroupAddress_Object=MibTableColumn
dot1qTpGroupAddress=_Dot1qTpGroupAddress_Object((1,3,6,1,2,1,17,7,1,2,3,1,1),_Dot1qTpGroupAddress_Type())
dot1qTpGroupAddress.setMaxAccess(_F)
if mibBuilder.loadTexts:dot1qTpGroupAddress.setStatus(_A)
_Dot1qTpGroupEgressPorts_Type=PortList
_Dot1qTpGroupEgressPorts_Object=MibTableColumn
dot1qTpGroupEgressPorts=_Dot1qTpGroupEgressPorts_Object((1,3,6,1,2,1,17,7,1,2,3,1,2),_Dot1qTpGroupEgressPorts_Type())
dot1qTpGroupEgressPorts.setMaxAccess(_C)
if mibBuilder.loadTexts:dot1qTpGroupEgressPorts.setStatus(_A)
_Dot1qTpGroupLearnt_Type=PortList
_Dot1qTpGroupLearnt_Object=MibTableColumn
dot1qTpGroupLearnt=_Dot1qTpGroupLearnt_Object((1,3,6,1,2,1,17,7,1,2,3,1,3),_Dot1qTpGroupLearnt_Type())
dot1qTpGroupLearnt.setMaxAccess(_C)
if mibBuilder.loadTexts:dot1qTpGroupLearnt.setStatus(_A)
_Dot1qForwardAllTable_Object=MibTable
dot1qForwardAllTable=_Dot1qForwardAllTable_Object((1,3,6,1,2,1,17,7,1,2,4))
if mibBuilder.loadTexts:dot1qForwardAllTable.setStatus(_A)
_Dot1qForwardAllEntry_Object=MibTableRow
dot1qForwardAllEntry=_Dot1qForwardAllEntry_Object((1,3,6,1,2,1,17,7,1,2,4,1))
dot1qForwardAllEntry.setIndexNames((0,_B,_H))
if mibBuilder.loadTexts:dot1qForwardAllEntry.setStatus(_A)
_Dot1qForwardAllPorts_Type=PortList
_Dot1qForwardAllPorts_Object=MibTableColumn
dot1qForwardAllPorts=_Dot1qForwardAllPorts_Object((1,3,6,1,2,1,17,7,1,2,4,1,1),_Dot1qForwardAllPorts_Type())
dot1qForwardAllPorts.setMaxAccess(_C)
if mibBuilder.loadTexts:dot1qForwardAllPorts.setStatus(_A)
_Dot1qForwardAllStaticPorts_Type=PortList
_Dot1qForwardAllStaticPorts_Object=MibTableColumn
dot1qForwardAllStaticPorts=_Dot1qForwardAllStaticPorts_Object((1,3,6,1,2,1,17,7,1,2,4,1,2),_Dot1qForwardAllStaticPorts_Type())
dot1qForwardAllStaticPorts.setMaxAccess(_E)
if mibBuilder.loadTexts:dot1qForwardAllStaticPorts.setStatus(_A)
_Dot1qForwardAllForbiddenPorts_Type=PortList
_Dot1qForwardAllForbiddenPorts_Object=MibTableColumn
dot1qForwardAllForbiddenPorts=_Dot1qForwardAllForbiddenPorts_Object((1,3,6,1,2,1,17,7,1,2,4,1,3),_Dot1qForwardAllForbiddenPorts_Type())
dot1qForwardAllForbiddenPorts.setMaxAccess(_E)
if mibBuilder.loadTexts:dot1qForwardAllForbiddenPorts.setStatus(_A)
_Dot1qForwardUnregisteredTable_Object=MibTable
dot1qForwardUnregisteredTable=_Dot1qForwardUnregisteredTable_Object((1,3,6,1,2,1,17,7,1,2,5))
if mibBuilder.loadTexts:dot1qForwardUnregisteredTable.setStatus(_A)
_Dot1qForwardUnregisteredEntry_Object=MibTableRow
dot1qForwardUnregisteredEntry=_Dot1qForwardUnregisteredEntry_Object((1,3,6,1,2,1,17,7,1,2,5,1))
dot1qForwardUnregisteredEntry.setIndexNames((0,_B,_H))
if mibBuilder.loadTexts:dot1qForwardUnregisteredEntry.setStatus(_A)
_Dot1qForwardUnregisteredPorts_Type=PortList
_Dot1qForwardUnregisteredPorts_Object=MibTableColumn
dot1qForwardUnregisteredPorts=_Dot1qForwardUnregisteredPorts_Object((1,3,6,1,2,1,17,7,1,2,5,1,1),_Dot1qForwardUnregisteredPorts_Type())
dot1qForwardUnregisteredPorts.setMaxAccess(_C)
if mibBuilder.loadTexts:dot1qForwardUnregisteredPorts.setStatus(_A)
_Dot1qForwardUnregisteredStaticPorts_Type=PortList
_Dot1qForwardUnregisteredStaticPorts_Object=MibTableColumn
dot1qForwardUnregisteredStaticPorts=_Dot1qForwardUnregisteredStaticPorts_Object((1,3,6,1,2,1,17,7,1,2,5,1,2),_Dot1qForwardUnregisteredStaticPorts_Type())
dot1qForwardUnregisteredStaticPorts.setMaxAccess(_E)
if mibBuilder.loadTexts:dot1qForwardUnregisteredStaticPorts.setStatus(_A)
_Dot1qForwardUnregisteredForbiddenPorts_Type=PortList
_Dot1qForwardUnregisteredForbiddenPorts_Object=MibTableColumn
dot1qForwardUnregisteredForbiddenPorts=_Dot1qForwardUnregisteredForbiddenPorts_Object((1,3,6,1,2,1,17,7,1,2,5,1,3),_Dot1qForwardUnregisteredForbiddenPorts_Type())
dot1qForwardUnregisteredForbiddenPorts.setMaxAccess(_E)
if mibBuilder.loadTexts:dot1qForwardUnregisteredForbiddenPorts.setStatus(_A)
_Dot1qStatic_ObjectIdentity=ObjectIdentity
dot1qStatic=_Dot1qStatic_ObjectIdentity((1,3,6,1,2,1,17,7,1,3))
_Dot1qStaticUnicastTable_Object=MibTable
dot1qStaticUnicastTable=_Dot1qStaticUnicastTable_Object((1,3,6,1,2,1,17,7,1,3,1))
if mibBuilder.loadTexts:dot1qStaticUnicastTable.setStatus(_A)
_Dot1qStaticUnicastEntry_Object=MibTableRow
dot1qStaticUnicastEntry=_Dot1qStaticUnicastEntry_Object((1,3,6,1,2,1,17,7,1,3,1,1))
dot1qStaticUnicastEntry.setIndexNames((0,_B,_K),(0,_B,_m),(0,_B,_n))
if mibBuilder.loadTexts:dot1qStaticUnicastEntry.setStatus(_A)
_Dot1qStaticUnicastAddress_Type=MacAddress
_Dot1qStaticUnicastAddress_Object=MibTableColumn
dot1qStaticUnicastAddress=_Dot1qStaticUnicastAddress_Object((1,3,6,1,2,1,17,7,1,3,1,1,1),_Dot1qStaticUnicastAddress_Type())
dot1qStaticUnicastAddress.setMaxAccess(_F)
if mibBuilder.loadTexts:dot1qStaticUnicastAddress.setStatus(_A)
class _Dot1qStaticUnicastReceivePort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_Dot1qStaticUnicastReceivePort_Type.__name__=_D
_Dot1qStaticUnicastReceivePort_Object=MibTableColumn
dot1qStaticUnicastReceivePort=_Dot1qStaticUnicastReceivePort_Object((1,3,6,1,2,1,17,7,1,3,1,1,2),_Dot1qStaticUnicastReceivePort_Type())
dot1qStaticUnicastReceivePort.setMaxAccess(_F)
if mibBuilder.loadTexts:dot1qStaticUnicastReceivePort.setStatus(_A)
_Dot1qStaticUnicastAllowedToGoTo_Type=PortList
_Dot1qStaticUnicastAllowedToGoTo_Object=MibTableColumn
dot1qStaticUnicastAllowedToGoTo=_Dot1qStaticUnicastAllowedToGoTo_Object((1,3,6,1,2,1,17,7,1,3,1,1,3),_Dot1qStaticUnicastAllowedToGoTo_Type())
dot1qStaticUnicastAllowedToGoTo.setMaxAccess(_E)
if mibBuilder.loadTexts:dot1qStaticUnicastAllowedToGoTo.setStatus(_A)
class _Dot1qStaticUnicastStatus_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_L,1),(_O,2),(_P,3),(_o,4),(_p,5)))
_Dot1qStaticUnicastStatus_Type.__name__=_D
_Dot1qStaticUnicastStatus_Object=MibTableColumn
dot1qStaticUnicastStatus=_Dot1qStaticUnicastStatus_Object((1,3,6,1,2,1,17,7,1,3,1,1,4),_Dot1qStaticUnicastStatus_Type())
dot1qStaticUnicastStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:dot1qStaticUnicastStatus.setStatus(_A)
_Dot1qStaticMulticastTable_Object=MibTable
dot1qStaticMulticastTable=_Dot1qStaticMulticastTable_Object((1,3,6,1,2,1,17,7,1,3,2))
if mibBuilder.loadTexts:dot1qStaticMulticastTable.setStatus(_A)
_Dot1qStaticMulticastEntry_Object=MibTableRow
dot1qStaticMulticastEntry=_Dot1qStaticMulticastEntry_Object((1,3,6,1,2,1,17,7,1,3,2,1))
dot1qStaticMulticastEntry.setIndexNames((0,_B,_H),(0,_B,_q),(0,_B,_r))
if mibBuilder.loadTexts:dot1qStaticMulticastEntry.setStatus(_A)
_Dot1qStaticMulticastAddress_Type=MacAddress
_Dot1qStaticMulticastAddress_Object=MibTableColumn
dot1qStaticMulticastAddress=_Dot1qStaticMulticastAddress_Object((1,3,6,1,2,1,17,7,1,3,2,1,1),_Dot1qStaticMulticastAddress_Type())
dot1qStaticMulticastAddress.setMaxAccess(_F)
if mibBuilder.loadTexts:dot1qStaticMulticastAddress.setStatus(_A)
class _Dot1qStaticMulticastReceivePort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_Dot1qStaticMulticastReceivePort_Type.__name__=_D
_Dot1qStaticMulticastReceivePort_Object=MibTableColumn
dot1qStaticMulticastReceivePort=_Dot1qStaticMulticastReceivePort_Object((1,3,6,1,2,1,17,7,1,3,2,1,2),_Dot1qStaticMulticastReceivePort_Type())
dot1qStaticMulticastReceivePort.setMaxAccess(_F)
if mibBuilder.loadTexts:dot1qStaticMulticastReceivePort.setStatus(_A)
_Dot1qStaticMulticastStaticEgressPorts_Type=PortList
_Dot1qStaticMulticastStaticEgressPorts_Object=MibTableColumn
dot1qStaticMulticastStaticEgressPorts=_Dot1qStaticMulticastStaticEgressPorts_Object((1,3,6,1,2,1,17,7,1,3,2,1,3),_Dot1qStaticMulticastStaticEgressPorts_Type())
dot1qStaticMulticastStaticEgressPorts.setMaxAccess(_E)
if mibBuilder.loadTexts:dot1qStaticMulticastStaticEgressPorts.setStatus(_A)
_Dot1qStaticMulticastForbiddenEgressPorts_Type=PortList
_Dot1qStaticMulticastForbiddenEgressPorts_Object=MibTableColumn
dot1qStaticMulticastForbiddenEgressPorts=_Dot1qStaticMulticastForbiddenEgressPorts_Object((1,3,6,1,2,1,17,7,1,3,2,1,4),_Dot1qStaticMulticastForbiddenEgressPorts_Type())
dot1qStaticMulticastForbiddenEgressPorts.setMaxAccess(_E)
if mibBuilder.loadTexts:dot1qStaticMulticastForbiddenEgressPorts.setStatus(_A)
class _Dot1qStaticMulticastStatus_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_L,1),(_O,2),(_P,3),(_o,4),(_p,5)))
_Dot1qStaticMulticastStatus_Type.__name__=_D
_Dot1qStaticMulticastStatus_Object=MibTableColumn
dot1qStaticMulticastStatus=_Dot1qStaticMulticastStatus_Object((1,3,6,1,2,1,17,7,1,3,2,1,5),_Dot1qStaticMulticastStatus_Type())
dot1qStaticMulticastStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:dot1qStaticMulticastStatus.setStatus(_A)
_Dot1qVlan_ObjectIdentity=ObjectIdentity
dot1qVlan=_Dot1qVlan_ObjectIdentity((1,3,6,1,2,1,17,7,1,4))
_Dot1qVlanNumDeletes_Type=Counter32
_Dot1qVlanNumDeletes_Object=MibScalar
dot1qVlanNumDeletes=_Dot1qVlanNumDeletes_Object((1,3,6,1,2,1,17,7,1,4,1),_Dot1qVlanNumDeletes_Type())
dot1qVlanNumDeletes.setMaxAccess(_C)
if mibBuilder.loadTexts:dot1qVlanNumDeletes.setStatus(_A)
_Dot1qVlanCurrentTable_Object=MibTable
dot1qVlanCurrentTable=_Dot1qVlanCurrentTable_Object((1,3,6,1,2,1,17,7,1,4,2))
if mibBuilder.loadTexts:dot1qVlanCurrentTable.setStatus(_A)
_Dot1qVlanCurrentEntry_Object=MibTableRow
dot1qVlanCurrentEntry=_Dot1qVlanCurrentEntry_Object((1,3,6,1,2,1,17,7,1,4,2,1))
dot1qVlanCurrentEntry.setIndexNames((0,_B,_s),(0,_B,_H))
if mibBuilder.loadTexts:dot1qVlanCurrentEntry.setStatus(_A)
_Dot1qVlanTimeMark_Type=TimeFilter
_Dot1qVlanTimeMark_Object=MibTableColumn
dot1qVlanTimeMark=_Dot1qVlanTimeMark_Object((1,3,6,1,2,1,17,7,1,4,2,1,1),_Dot1qVlanTimeMark_Type())
dot1qVlanTimeMark.setMaxAccess(_F)
if mibBuilder.loadTexts:dot1qVlanTimeMark.setStatus(_A)
_Dot1qVlanIndex_Type=VlanIndex
_Dot1qVlanIndex_Object=MibTableColumn
dot1qVlanIndex=_Dot1qVlanIndex_Object((1,3,6,1,2,1,17,7,1,4,2,1,2),_Dot1qVlanIndex_Type())
dot1qVlanIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:dot1qVlanIndex.setStatus(_A)
_Dot1qVlanFdbId_Type=Unsigned32
_Dot1qVlanFdbId_Object=MibTableColumn
dot1qVlanFdbId=_Dot1qVlanFdbId_Object((1,3,6,1,2,1,17,7,1,4,2,1,3),_Dot1qVlanFdbId_Type())
dot1qVlanFdbId.setMaxAccess(_C)
if mibBuilder.loadTexts:dot1qVlanFdbId.setStatus(_A)
_Dot1qVlanCurrentEgressPorts_Type=PortList
_Dot1qVlanCurrentEgressPorts_Object=MibTableColumn
dot1qVlanCurrentEgressPorts=_Dot1qVlanCurrentEgressPorts_Object((1,3,6,1,2,1,17,7,1,4,2,1,4),_Dot1qVlanCurrentEgressPorts_Type())
dot1qVlanCurrentEgressPorts.setMaxAccess(_C)
if mibBuilder.loadTexts:dot1qVlanCurrentEgressPorts.setStatus(_A)
_Dot1qVlanCurrentUntaggedPorts_Type=PortList
_Dot1qVlanCurrentUntaggedPorts_Object=MibTableColumn
dot1qVlanCurrentUntaggedPorts=_Dot1qVlanCurrentUntaggedPorts_Object((1,3,6,1,2,1,17,7,1,4,2,1,5),_Dot1qVlanCurrentUntaggedPorts_Type())
dot1qVlanCurrentUntaggedPorts.setMaxAccess(_C)
if mibBuilder.loadTexts:dot1qVlanCurrentUntaggedPorts.setStatus(_A)
class _Dot1qVlanStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_L,1),(_P,2),('dynamicGvrp',3)))
_Dot1qVlanStatus_Type.__name__=_D
_Dot1qVlanStatus_Object=MibTableColumn
dot1qVlanStatus=_Dot1qVlanStatus_Object((1,3,6,1,2,1,17,7,1,4,2,1,6),_Dot1qVlanStatus_Type())
dot1qVlanStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:dot1qVlanStatus.setStatus(_A)
_Dot1qVlanCreationTime_Type=TimeTicks
_Dot1qVlanCreationTime_Object=MibTableColumn
dot1qVlanCreationTime=_Dot1qVlanCreationTime_Object((1,3,6,1,2,1,17,7,1,4,2,1,7),_Dot1qVlanCreationTime_Type())
dot1qVlanCreationTime.setMaxAccess(_C)
if mibBuilder.loadTexts:dot1qVlanCreationTime.setStatus(_A)
_Dot1qVlanStaticTable_Object=MibTable
dot1qVlanStaticTable=_Dot1qVlanStaticTable_Object((1,3,6,1,2,1,17,7,1,4,3))
if mibBuilder.loadTexts:dot1qVlanStaticTable.setStatus(_A)
_Dot1qVlanStaticEntry_Object=MibTableRow
dot1qVlanStaticEntry=_Dot1qVlanStaticEntry_Object((1,3,6,1,2,1,17,7,1,4,3,1))
dot1qVlanStaticEntry.setIndexNames((0,_B,_H))
if mibBuilder.loadTexts:dot1qVlanStaticEntry.setStatus(_A)
class _Dot1qVlanStaticName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_Dot1qVlanStaticName_Type.__name__=_j
_Dot1qVlanStaticName_Object=MibTableColumn
dot1qVlanStaticName=_Dot1qVlanStaticName_Object((1,3,6,1,2,1,17,7,1,4,3,1,1),_Dot1qVlanStaticName_Type())
dot1qVlanStaticName.setMaxAccess(_G)
if mibBuilder.loadTexts:dot1qVlanStaticName.setStatus(_A)
_Dot1qVlanStaticEgressPorts_Type=PortList
_Dot1qVlanStaticEgressPorts_Object=MibTableColumn
dot1qVlanStaticEgressPorts=_Dot1qVlanStaticEgressPorts_Object((1,3,6,1,2,1,17,7,1,4,3,1,2),_Dot1qVlanStaticEgressPorts_Type())
dot1qVlanStaticEgressPorts.setMaxAccess(_G)
if mibBuilder.loadTexts:dot1qVlanStaticEgressPorts.setStatus(_A)
_Dot1qVlanForbiddenEgressPorts_Type=PortList
_Dot1qVlanForbiddenEgressPorts_Object=MibTableColumn
dot1qVlanForbiddenEgressPorts=_Dot1qVlanForbiddenEgressPorts_Object((1,3,6,1,2,1,17,7,1,4,3,1,3),_Dot1qVlanForbiddenEgressPorts_Type())
dot1qVlanForbiddenEgressPorts.setMaxAccess(_G)
if mibBuilder.loadTexts:dot1qVlanForbiddenEgressPorts.setStatus(_A)
_Dot1qVlanStaticUntaggedPorts_Type=PortList
_Dot1qVlanStaticUntaggedPorts_Object=MibTableColumn
dot1qVlanStaticUntaggedPorts=_Dot1qVlanStaticUntaggedPorts_Object((1,3,6,1,2,1,17,7,1,4,3,1,4),_Dot1qVlanStaticUntaggedPorts_Type())
dot1qVlanStaticUntaggedPorts.setMaxAccess(_G)
if mibBuilder.loadTexts:dot1qVlanStaticUntaggedPorts.setStatus(_A)
_Dot1qVlanStaticRowStatus_Type=RowStatus
_Dot1qVlanStaticRowStatus_Object=MibTableColumn
dot1qVlanStaticRowStatus=_Dot1qVlanStaticRowStatus_Object((1,3,6,1,2,1,17,7,1,4,3,1,5),_Dot1qVlanStaticRowStatus_Type())
dot1qVlanStaticRowStatus.setMaxAccess(_G)
if mibBuilder.loadTexts:dot1qVlanStaticRowStatus.setStatus(_A)
class _Dot1qNextFreeLocalVlanIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(4096,2147483647))
_Dot1qNextFreeLocalVlanIndex_Type.__name__=_D
_Dot1qNextFreeLocalVlanIndex_Object=MibScalar
dot1qNextFreeLocalVlanIndex=_Dot1qNextFreeLocalVlanIndex_Object((1,3,6,1,2,1,17,7,1,4,4),_Dot1qNextFreeLocalVlanIndex_Type())
dot1qNextFreeLocalVlanIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:dot1qNextFreeLocalVlanIndex.setStatus(_A)
_Dot1qPortVlanTable_Object=MibTable
dot1qPortVlanTable=_Dot1qPortVlanTable_Object((1,3,6,1,2,1,17,7,1,4,5))
if mibBuilder.loadTexts:dot1qPortVlanTable.setStatus(_A)
_Dot1qPortVlanEntry_Object=MibTableRow
dot1qPortVlanEntry=_Dot1qPortVlanEntry_Object((1,3,6,1,2,1,17,7,1,4,5,1))
if mibBuilder.loadTexts:dot1qPortVlanEntry.setStatus(_A)
class _Dot1qPvid_Type(VlanIndex):defaultValue=1
_Dot1qPvid_Type.__name__=_t
_Dot1qPvid_Object=MibTableColumn
dot1qPvid=_Dot1qPvid_Object((1,3,6,1,2,1,17,7,1,4,5,1,1),_Dot1qPvid_Type())
dot1qPvid.setMaxAccess(_E)
if mibBuilder.loadTexts:dot1qPvid.setStatus(_A)
class _Dot1qPortAcceptableFrameTypes_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('admitAll',1),('admitOnlyVlanTagged',2)))
_Dot1qPortAcceptableFrameTypes_Type.__name__=_D
_Dot1qPortAcceptableFrameTypes_Object=MibTableColumn
dot1qPortAcceptableFrameTypes=_Dot1qPortAcceptableFrameTypes_Object((1,3,6,1,2,1,17,7,1,4,5,1,2),_Dot1qPortAcceptableFrameTypes_Type())
dot1qPortAcceptableFrameTypes.setMaxAccess(_E)
if mibBuilder.loadTexts:dot1qPortAcceptableFrameTypes.setStatus(_A)
class _Dot1qPortIngressFiltering_Type(TruthValue):defaultValue=2
_Dot1qPortIngressFiltering_Type.__name__=_N
_Dot1qPortIngressFiltering_Object=MibTableColumn
dot1qPortIngressFiltering=_Dot1qPortIngressFiltering_Object((1,3,6,1,2,1,17,7,1,4,5,1,3),_Dot1qPortIngressFiltering_Type())
dot1qPortIngressFiltering.setMaxAccess(_E)
if mibBuilder.loadTexts:dot1qPortIngressFiltering.setStatus(_A)
class _Dot1qPortGvrpStatus_Type(EnabledStatus):defaultValue=1
_Dot1qPortGvrpStatus_Type.__name__=_M
_Dot1qPortGvrpStatus_Object=MibTableColumn
dot1qPortGvrpStatus=_Dot1qPortGvrpStatus_Object((1,3,6,1,2,1,17,7,1,4,5,1,4),_Dot1qPortGvrpStatus_Type())
dot1qPortGvrpStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:dot1qPortGvrpStatus.setStatus(_A)
_Dot1qPortGvrpFailedRegistrations_Type=Counter32
_Dot1qPortGvrpFailedRegistrations_Object=MibTableColumn
dot1qPortGvrpFailedRegistrations=_Dot1qPortGvrpFailedRegistrations_Object((1,3,6,1,2,1,17,7,1,4,5,1,5),_Dot1qPortGvrpFailedRegistrations_Type())
dot1qPortGvrpFailedRegistrations.setMaxAccess(_C)
if mibBuilder.loadTexts:dot1qPortGvrpFailedRegistrations.setStatus(_A)
_Dot1qPortGvrpLastPduOrigin_Type=MacAddress
_Dot1qPortGvrpLastPduOrigin_Object=MibTableColumn
dot1qPortGvrpLastPduOrigin=_Dot1qPortGvrpLastPduOrigin_Object((1,3,6,1,2,1,17,7,1,4,5,1,6),_Dot1qPortGvrpLastPduOrigin_Type())
dot1qPortGvrpLastPduOrigin.setMaxAccess(_C)
if mibBuilder.loadTexts:dot1qPortGvrpLastPduOrigin.setStatus(_A)
class _Dot1qPortRestrictedVlanRegistration_Type(TruthValue):defaultValue=2
_Dot1qPortRestrictedVlanRegistration_Type.__name__=_N
_Dot1qPortRestrictedVlanRegistration_Object=MibTableColumn
dot1qPortRestrictedVlanRegistration=_Dot1qPortRestrictedVlanRegistration_Object((1,3,6,1,2,1,17,7,1,4,5,1,7),_Dot1qPortRestrictedVlanRegistration_Type())
dot1qPortRestrictedVlanRegistration.setMaxAccess(_E)
if mibBuilder.loadTexts:dot1qPortRestrictedVlanRegistration.setStatus(_A)
_Dot1qPortVlanStatisticsTable_Object=MibTable
dot1qPortVlanStatisticsTable=_Dot1qPortVlanStatisticsTable_Object((1,3,6,1,2,1,17,7,1,4,6))
if mibBuilder.loadTexts:dot1qPortVlanStatisticsTable.setStatus(_A)
_Dot1qPortVlanStatisticsEntry_Object=MibTableRow
dot1qPortVlanStatisticsEntry=_Dot1qPortVlanStatisticsEntry_Object((1,3,6,1,2,1,17,7,1,4,6,1))
dot1qPortVlanStatisticsEntry.setIndexNames((0,_I,_J),(0,_B,_H))
if mibBuilder.loadTexts:dot1qPortVlanStatisticsEntry.setStatus(_A)
_Dot1qTpVlanPortInFrames_Type=Counter32
_Dot1qTpVlanPortInFrames_Object=MibTableColumn
dot1qTpVlanPortInFrames=_Dot1qTpVlanPortInFrames_Object((1,3,6,1,2,1,17,7,1,4,6,1,1),_Dot1qTpVlanPortInFrames_Type())
dot1qTpVlanPortInFrames.setMaxAccess(_C)
if mibBuilder.loadTexts:dot1qTpVlanPortInFrames.setStatus(_A)
_Dot1qTpVlanPortOutFrames_Type=Counter32
_Dot1qTpVlanPortOutFrames_Object=MibTableColumn
dot1qTpVlanPortOutFrames=_Dot1qTpVlanPortOutFrames_Object((1,3,6,1,2,1,17,7,1,4,6,1,2),_Dot1qTpVlanPortOutFrames_Type())
dot1qTpVlanPortOutFrames.setMaxAccess(_C)
if mibBuilder.loadTexts:dot1qTpVlanPortOutFrames.setStatus(_A)
_Dot1qTpVlanPortInDiscards_Type=Counter32
_Dot1qTpVlanPortInDiscards_Object=MibTableColumn
dot1qTpVlanPortInDiscards=_Dot1qTpVlanPortInDiscards_Object((1,3,6,1,2,1,17,7,1,4,6,1,3),_Dot1qTpVlanPortInDiscards_Type())
dot1qTpVlanPortInDiscards.setMaxAccess(_C)
if mibBuilder.loadTexts:dot1qTpVlanPortInDiscards.setStatus(_A)
_Dot1qTpVlanPortInOverflowFrames_Type=Counter32
_Dot1qTpVlanPortInOverflowFrames_Object=MibTableColumn
dot1qTpVlanPortInOverflowFrames=_Dot1qTpVlanPortInOverflowFrames_Object((1,3,6,1,2,1,17,7,1,4,6,1,4),_Dot1qTpVlanPortInOverflowFrames_Type())
dot1qTpVlanPortInOverflowFrames.setMaxAccess(_C)
if mibBuilder.loadTexts:dot1qTpVlanPortInOverflowFrames.setStatus(_A)
_Dot1qTpVlanPortOutOverflowFrames_Type=Counter32
_Dot1qTpVlanPortOutOverflowFrames_Object=MibTableColumn
dot1qTpVlanPortOutOverflowFrames=_Dot1qTpVlanPortOutOverflowFrames_Object((1,3,6,1,2,1,17,7,1,4,6,1,5),_Dot1qTpVlanPortOutOverflowFrames_Type())
dot1qTpVlanPortOutOverflowFrames.setMaxAccess(_C)
if mibBuilder.loadTexts:dot1qTpVlanPortOutOverflowFrames.setStatus(_A)
_Dot1qTpVlanPortInOverflowDiscards_Type=Counter32
_Dot1qTpVlanPortInOverflowDiscards_Object=MibTableColumn
dot1qTpVlanPortInOverflowDiscards=_Dot1qTpVlanPortInOverflowDiscards_Object((1,3,6,1,2,1,17,7,1,4,6,1,6),_Dot1qTpVlanPortInOverflowDiscards_Type())
dot1qTpVlanPortInOverflowDiscards.setMaxAccess(_C)
if mibBuilder.loadTexts:dot1qTpVlanPortInOverflowDiscards.setStatus(_A)
_Dot1qPortVlanHCStatisticsTable_Object=MibTable
dot1qPortVlanHCStatisticsTable=_Dot1qPortVlanHCStatisticsTable_Object((1,3,6,1,2,1,17,7,1,4,7))
if mibBuilder.loadTexts:dot1qPortVlanHCStatisticsTable.setStatus(_A)
_Dot1qPortVlanHCStatisticsEntry_Object=MibTableRow
dot1qPortVlanHCStatisticsEntry=_Dot1qPortVlanHCStatisticsEntry_Object((1,3,6,1,2,1,17,7,1,4,7,1))
dot1qPortVlanHCStatisticsEntry.setIndexNames((0,_I,_J),(0,_B,_H))
if mibBuilder.loadTexts:dot1qPortVlanHCStatisticsEntry.setStatus(_A)
_Dot1qTpVlanPortHCInFrames_Type=Counter64
_Dot1qTpVlanPortHCInFrames_Object=MibTableColumn
dot1qTpVlanPortHCInFrames=_Dot1qTpVlanPortHCInFrames_Object((1,3,6,1,2,1,17,7,1,4,7,1,1),_Dot1qTpVlanPortHCInFrames_Type())
dot1qTpVlanPortHCInFrames.setMaxAccess(_C)
if mibBuilder.loadTexts:dot1qTpVlanPortHCInFrames.setStatus(_A)
_Dot1qTpVlanPortHCOutFrames_Type=Counter64
_Dot1qTpVlanPortHCOutFrames_Object=MibTableColumn
dot1qTpVlanPortHCOutFrames=_Dot1qTpVlanPortHCOutFrames_Object((1,3,6,1,2,1,17,7,1,4,7,1,2),_Dot1qTpVlanPortHCOutFrames_Type())
dot1qTpVlanPortHCOutFrames.setMaxAccess(_C)
if mibBuilder.loadTexts:dot1qTpVlanPortHCOutFrames.setStatus(_A)
_Dot1qTpVlanPortHCInDiscards_Type=Counter64
_Dot1qTpVlanPortHCInDiscards_Object=MibTableColumn
dot1qTpVlanPortHCInDiscards=_Dot1qTpVlanPortHCInDiscards_Object((1,3,6,1,2,1,17,7,1,4,7,1,3),_Dot1qTpVlanPortHCInDiscards_Type())
dot1qTpVlanPortHCInDiscards.setMaxAccess(_C)
if mibBuilder.loadTexts:dot1qTpVlanPortHCInDiscards.setStatus(_A)
_Dot1qLearningConstraintsTable_Object=MibTable
dot1qLearningConstraintsTable=_Dot1qLearningConstraintsTable_Object((1,3,6,1,2,1,17,7,1,4,8))
if mibBuilder.loadTexts:dot1qLearningConstraintsTable.setStatus(_A)
_Dot1qLearningConstraintsEntry_Object=MibTableRow
dot1qLearningConstraintsEntry=_Dot1qLearningConstraintsEntry_Object((1,3,6,1,2,1,17,7,1,4,8,1))
dot1qLearningConstraintsEntry.setIndexNames((0,_B,_u),(0,_B,_v))
if mibBuilder.loadTexts:dot1qLearningConstraintsEntry.setStatus(_A)
_Dot1qConstraintVlan_Type=VlanIndex
_Dot1qConstraintVlan_Object=MibTableColumn
dot1qConstraintVlan=_Dot1qConstraintVlan_Object((1,3,6,1,2,1,17,7,1,4,8,1,1),_Dot1qConstraintVlan_Type())
dot1qConstraintVlan.setMaxAccess(_F)
if mibBuilder.loadTexts:dot1qConstraintVlan.setStatus(_A)
class _Dot1qConstraintSet_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_Dot1qConstraintSet_Type.__name__=_D
_Dot1qConstraintSet_Object=MibTableColumn
dot1qConstraintSet=_Dot1qConstraintSet_Object((1,3,6,1,2,1,17,7,1,4,8,1,2),_Dot1qConstraintSet_Type())
dot1qConstraintSet.setMaxAccess(_F)
if mibBuilder.loadTexts:dot1qConstraintSet.setStatus(_A)
class _Dot1qConstraintType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_w,1),(_x,2)))
_Dot1qConstraintType_Type.__name__=_D
_Dot1qConstraintType_Object=MibTableColumn
dot1qConstraintType=_Dot1qConstraintType_Object((1,3,6,1,2,1,17,7,1,4,8,1,3),_Dot1qConstraintType_Type())
dot1qConstraintType.setMaxAccess(_G)
if mibBuilder.loadTexts:dot1qConstraintType.setStatus(_A)
_Dot1qConstraintStatus_Type=RowStatus
_Dot1qConstraintStatus_Object=MibTableColumn
dot1qConstraintStatus=_Dot1qConstraintStatus_Object((1,3,6,1,2,1,17,7,1,4,8,1,4),_Dot1qConstraintStatus_Type())
dot1qConstraintStatus.setMaxAccess(_G)
if mibBuilder.loadTexts:dot1qConstraintStatus.setStatus(_A)
class _Dot1qConstraintSetDefault_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_Dot1qConstraintSetDefault_Type.__name__=_D
_Dot1qConstraintSetDefault_Object=MibScalar
dot1qConstraintSetDefault=_Dot1qConstraintSetDefault_Object((1,3,6,1,2,1,17,7,1,4,9),_Dot1qConstraintSetDefault_Type())
dot1qConstraintSetDefault.setMaxAccess(_E)
if mibBuilder.loadTexts:dot1qConstraintSetDefault.setStatus(_A)
class _Dot1qConstraintTypeDefault_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_w,1),(_x,2)))
_Dot1qConstraintTypeDefault_Type.__name__=_D
_Dot1qConstraintTypeDefault_Object=MibScalar
dot1qConstraintTypeDefault=_Dot1qConstraintTypeDefault_Object((1,3,6,1,2,1,17,7,1,4,10),_Dot1qConstraintTypeDefault_Type())
dot1qConstraintTypeDefault.setMaxAccess(_E)
if mibBuilder.loadTexts:dot1qConstraintTypeDefault.setStatus(_A)
_Dot1vProtocol_ObjectIdentity=ObjectIdentity
dot1vProtocol=_Dot1vProtocol_ObjectIdentity((1,3,6,1,2,1,17,7,1,5))
_Dot1vProtocolGroupTable_Object=MibTable
dot1vProtocolGroupTable=_Dot1vProtocolGroupTable_Object((1,3,6,1,2,1,17,7,1,5,1))
if mibBuilder.loadTexts:dot1vProtocolGroupTable.setStatus(_A)
_Dot1vProtocolGroupEntry_Object=MibTableRow
dot1vProtocolGroupEntry=_Dot1vProtocolGroupEntry_Object((1,3,6,1,2,1,17,7,1,5,1,1))
dot1vProtocolGroupEntry.setIndexNames((0,_B,_y),(0,_B,_z))
if mibBuilder.loadTexts:dot1vProtocolGroupEntry.setStatus(_A)
class _Dot1vProtocolTemplateFrameType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('ethernet',1),('rfc1042',2),('snap8021H',3),('snapOther',4),('llcOther',5)))
_Dot1vProtocolTemplateFrameType_Type.__name__=_D
_Dot1vProtocolTemplateFrameType_Object=MibTableColumn
dot1vProtocolTemplateFrameType=_Dot1vProtocolTemplateFrameType_Object((1,3,6,1,2,1,17,7,1,5,1,1,1),_Dot1vProtocolTemplateFrameType_Type())
dot1vProtocolTemplateFrameType.setMaxAccess(_F)
if mibBuilder.loadTexts:dot1vProtocolTemplateFrameType.setStatus(_A)
class _Dot1vProtocolTemplateProtocolValue_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(2,2),ValueSizeConstraint(5,5))
_Dot1vProtocolTemplateProtocolValue_Type.__name__=_i
_Dot1vProtocolTemplateProtocolValue_Object=MibTableColumn
dot1vProtocolTemplateProtocolValue=_Dot1vProtocolTemplateProtocolValue_Object((1,3,6,1,2,1,17,7,1,5,1,1,2),_Dot1vProtocolTemplateProtocolValue_Type())
dot1vProtocolTemplateProtocolValue.setMaxAccess(_F)
if mibBuilder.loadTexts:dot1vProtocolTemplateProtocolValue.setStatus(_A)
class _Dot1vProtocolGroupId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_Dot1vProtocolGroupId_Type.__name__=_D
_Dot1vProtocolGroupId_Object=MibTableColumn
dot1vProtocolGroupId=_Dot1vProtocolGroupId_Object((1,3,6,1,2,1,17,7,1,5,1,1,3),_Dot1vProtocolGroupId_Type())
dot1vProtocolGroupId.setMaxAccess(_G)
if mibBuilder.loadTexts:dot1vProtocolGroupId.setStatus(_A)
_Dot1vProtocolGroupRowStatus_Type=RowStatus
_Dot1vProtocolGroupRowStatus_Object=MibTableColumn
dot1vProtocolGroupRowStatus=_Dot1vProtocolGroupRowStatus_Object((1,3,6,1,2,1,17,7,1,5,1,1,4),_Dot1vProtocolGroupRowStatus_Type())
dot1vProtocolGroupRowStatus.setMaxAccess(_G)
if mibBuilder.loadTexts:dot1vProtocolGroupRowStatus.setStatus(_A)
_Dot1vProtocolPortTable_Object=MibTable
dot1vProtocolPortTable=_Dot1vProtocolPortTable_Object((1,3,6,1,2,1,17,7,1,5,2))
if mibBuilder.loadTexts:dot1vProtocolPortTable.setStatus(_A)
_Dot1vProtocolPortEntry_Object=MibTableRow
dot1vProtocolPortEntry=_Dot1vProtocolPortEntry_Object((1,3,6,1,2,1,17,7,1,5,2,1))
dot1vProtocolPortEntry.setIndexNames((0,_I,_J),(0,_B,_A0))
if mibBuilder.loadTexts:dot1vProtocolPortEntry.setStatus(_A)
class _Dot1vProtocolPortGroupId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_Dot1vProtocolPortGroupId_Type.__name__=_D
_Dot1vProtocolPortGroupId_Object=MibTableColumn
dot1vProtocolPortGroupId=_Dot1vProtocolPortGroupId_Object((1,3,6,1,2,1,17,7,1,5,2,1,1),_Dot1vProtocolPortGroupId_Type())
dot1vProtocolPortGroupId.setMaxAccess(_F)
if mibBuilder.loadTexts:dot1vProtocolPortGroupId.setStatus(_A)
class _Dot1vProtocolPortGroupVid_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094))
_Dot1vProtocolPortGroupVid_Type.__name__=_D
_Dot1vProtocolPortGroupVid_Object=MibTableColumn
dot1vProtocolPortGroupVid=_Dot1vProtocolPortGroupVid_Object((1,3,6,1,2,1,17,7,1,5,2,1,2),_Dot1vProtocolPortGroupVid_Type())
dot1vProtocolPortGroupVid.setMaxAccess(_G)
if mibBuilder.loadTexts:dot1vProtocolPortGroupVid.setStatus(_A)
_Dot1vProtocolPortRowStatus_Type=RowStatus
_Dot1vProtocolPortRowStatus_Object=MibTableColumn
dot1vProtocolPortRowStatus=_Dot1vProtocolPortRowStatus_Object((1,3,6,1,2,1,17,7,1,5,2,1,3),_Dot1vProtocolPortRowStatus_Type())
dot1vProtocolPortRowStatus.setMaxAccess(_G)
if mibBuilder.loadTexts:dot1vProtocolPortRowStatus.setStatus(_A)
_QBridgeConformance_ObjectIdentity=ObjectIdentity
qBridgeConformance=_QBridgeConformance_ObjectIdentity((1,3,6,1,2,1,17,7,2))
_QBridgeGroups_ObjectIdentity=ObjectIdentity
qBridgeGroups=_QBridgeGroups_ObjectIdentity((1,3,6,1,2,1,17,7,2,1))
_QBridgeCompliances_ObjectIdentity=ObjectIdentity
qBridgeCompliances=_QBridgeCompliances_ObjectIdentity((1,3,6,1,2,1,17,7,2,2))
dot1dBasePortEntry.registerAugmentions((_B,_A1))
dot1qPortVlanEntry.setIndexNames(*dot1dBasePortEntry.getIndexNames())
qBridgeBaseGroup=ObjectGroup((1,3,6,1,2,1,17,7,2,1,1))
qBridgeBaseGroup.setObjects(*((_B,_A2),(_B,_A3),(_B,_A4),(_B,_A5),(_B,_A6)))
if mibBuilder.loadTexts:qBridgeBaseGroup.setStatus(_A)
qBridgeFdbUnicastGroup=ObjectGroup((1,3,6,1,2,1,17,7,2,1,2))
qBridgeFdbUnicastGroup.setObjects(*((_B,_A7),(_B,_A8),(_B,_A9)))
if mibBuilder.loadTexts:qBridgeFdbUnicastGroup.setStatus(_A)
qBridgeFdbMulticastGroup=ObjectGroup((1,3,6,1,2,1,17,7,2,1,3))
qBridgeFdbMulticastGroup.setObjects(*((_B,_AA),(_B,_AB)))
if mibBuilder.loadTexts:qBridgeFdbMulticastGroup.setStatus(_A)
qBridgeServiceRequirementsGroup=ObjectGroup((1,3,6,1,2,1,17,7,2,1,4))
qBridgeServiceRequirementsGroup.setObjects(*((_B,_AC),(_B,_AD),(_B,_AE),(_B,_AF),(_B,_AG),(_B,_AH)))
if mibBuilder.loadTexts:qBridgeServiceRequirementsGroup.setStatus(_A)
qBridgeFdbStaticGroup=ObjectGroup((1,3,6,1,2,1,17,7,2,1,5))
qBridgeFdbStaticGroup.setObjects(*((_B,_AI),(_B,_AJ),(_B,_AK),(_B,_AL),(_B,_AM)))
if mibBuilder.loadTexts:qBridgeFdbStaticGroup.setStatus(_A)
qBridgeVlanGroup=ObjectGroup((1,3,6,1,2,1,17,7,2,1,6))
qBridgeVlanGroup.setObjects(*((_B,_AN),(_B,_AO),(_B,_AP),(_B,_AQ),(_B,_AR),(_B,_AS)))
if mibBuilder.loadTexts:qBridgeVlanGroup.setStatus(_A)
qBridgeVlanStaticGroup=ObjectGroup((1,3,6,1,2,1,17,7,2,1,7))
qBridgeVlanStaticGroup.setObjects(*((_B,_AT),(_B,_AU),(_B,_AV),(_B,_AW),(_B,_AX),(_B,_AY)))
if mibBuilder.loadTexts:qBridgeVlanStaticGroup.setStatus(_A)
qBridgePortGroup=ObjectGroup((1,3,6,1,2,1,17,7,2,1,8))
qBridgePortGroup.setObjects(*((_B,_Q),(_B,_R),(_B,_S),(_B,_T),(_B,_U),(_B,_V)))
if mibBuilder.loadTexts:qBridgePortGroup.setStatus(_AZ)
qBridgeVlanStatisticsGroup=ObjectGroup((1,3,6,1,2,1,17,7,2,1,9))
qBridgeVlanStatisticsGroup.setObjects(*((_B,_Aa),(_B,_Ab),(_B,_Ac)))
if mibBuilder.loadTexts:qBridgeVlanStatisticsGroup.setStatus(_A)
qBridgeVlanStatisticsOverflowGroup=ObjectGroup((1,3,6,1,2,1,17,7,2,1,10))
qBridgeVlanStatisticsOverflowGroup.setObjects(*((_B,_Ad),(_B,_Ae),(_B,_Af)))
if mibBuilder.loadTexts:qBridgeVlanStatisticsOverflowGroup.setStatus(_A)
qBridgeVlanHCStatisticsGroup=ObjectGroup((1,3,6,1,2,1,17,7,2,1,11))
qBridgeVlanHCStatisticsGroup.setObjects(*((_B,_Ag),(_B,_Ah),(_B,_Ai)))
if mibBuilder.loadTexts:qBridgeVlanHCStatisticsGroup.setStatus(_A)
qBridgeLearningConstraintsGroup=ObjectGroup((1,3,6,1,2,1,17,7,2,1,12))
qBridgeLearningConstraintsGroup.setObjects(*((_B,_Aj),(_B,_Ak)))
if mibBuilder.loadTexts:qBridgeLearningConstraintsGroup.setStatus(_A)
qBridgeLearningConstraintDefaultGroup=ObjectGroup((1,3,6,1,2,1,17,7,2,1,13))
qBridgeLearningConstraintDefaultGroup.setObjects(*((_B,_Al),(_B,_Am)))
if mibBuilder.loadTexts:qBridgeLearningConstraintDefaultGroup.setStatus(_A)
qBridgeClassificationDeviceGroup=ObjectGroup((1,3,6,1,2,1,17,7,2,1,14))
qBridgeClassificationDeviceGroup.setObjects(*((_B,_An),(_B,_Ao)))
if mibBuilder.loadTexts:qBridgeClassificationDeviceGroup.setStatus(_A)
qBridgeClassificationPortGroup=ObjectGroup((1,3,6,1,2,1,17,7,2,1,15))
qBridgeClassificationPortGroup.setObjects(*((_B,_Ap),(_B,_Aq)))
if mibBuilder.loadTexts:qBridgeClassificationPortGroup.setStatus(_A)
qBridgePortGroup2=ObjectGroup((1,3,6,1,2,1,17,7,2,1,16))
qBridgePortGroup2.setObjects(*((_B,_Q),(_B,_R),(_B,_S),(_B,_T),(_B,_U),(_B,_V),(_B,_Ar)))
if mibBuilder.loadTexts:qBridgePortGroup2.setStatus(_A)
qBridgeCompliance=ModuleCompliance((1,3,6,1,2,1,17,7,2,2,1))
qBridgeCompliance.setObjects(*((_B,_W),(_B,_X),(_B,_Y),(_B,_As),(_B,_Z),(_B,_a),(_B,_b),(_B,_c),(_B,_d),(_B,_e),(_B,_f),(_B,_g),(_B,_h)))
if mibBuilder.loadTexts:qBridgeCompliance.setStatus(_AZ)
qBridgeCompliance2=ModuleCompliance((1,3,6,1,2,1,17,7,2,2,2))
qBridgeCompliance2.setObjects(*((_B,_W),(_B,_X),(_B,_Y),(_B,_At),(_B,_Z),(_B,_a),(_B,_b),(_B,_c),(_B,_d),(_B,_e),(_B,_f),(_B,_g),(_B,_h),(_B,_Au),(_B,_Av)))
if mibBuilder.loadTexts:qBridgeCompliance2.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'PortList':PortList,_t:VlanIndex,'VlanId':VlanId,'VlanIdOrAny':VlanIdOrAny,'VlanIdOrNone':VlanIdOrNone,'VlanIdOrAnyOrNone':VlanIdOrAnyOrNone,'qBridgeMIB':qBridgeMIB,'qBridgeMIBObjects':qBridgeMIBObjects,'dot1qBase':dot1qBase,_A2:dot1qVlanVersionNumber,_A3:dot1qMaxVlanId,_A4:dot1qMaxSupportedVlans,_A5:dot1qNumVlans,_A6:dot1qGvrpStatus,'dot1qTp':dot1qTp,'dot1qFdbTable':dot1qFdbTable,'dot1qFdbEntry':dot1qFdbEntry,_K:dot1qFdbId,_A7:dot1qFdbDynamicCount,'dot1qTpFdbTable':dot1qTpFdbTable,'dot1qTpFdbEntry':dot1qTpFdbEntry,_k:dot1qTpFdbAddress,_A8:dot1qTpFdbPort,_A9:dot1qTpFdbStatus,'dot1qTpGroupTable':dot1qTpGroupTable,'dot1qTpGroupEntry':dot1qTpGroupEntry,_l:dot1qTpGroupAddress,_AA:dot1qTpGroupEgressPorts,_AB:dot1qTpGroupLearnt,'dot1qForwardAllTable':dot1qForwardAllTable,'dot1qForwardAllEntry':dot1qForwardAllEntry,_AC:dot1qForwardAllPorts,_AD:dot1qForwardAllStaticPorts,_AE:dot1qForwardAllForbiddenPorts,'dot1qForwardUnregisteredTable':dot1qForwardUnregisteredTable,'dot1qForwardUnregisteredEntry':dot1qForwardUnregisteredEntry,_AF:dot1qForwardUnregisteredPorts,_AG:dot1qForwardUnregisteredStaticPorts,_AH:dot1qForwardUnregisteredForbiddenPorts,'dot1qStatic':dot1qStatic,'dot1qStaticUnicastTable':dot1qStaticUnicastTable,'dot1qStaticUnicastEntry':dot1qStaticUnicastEntry,_m:dot1qStaticUnicastAddress,_n:dot1qStaticUnicastReceivePort,_AI:dot1qStaticUnicastAllowedToGoTo,_AJ:dot1qStaticUnicastStatus,'dot1qStaticMulticastTable':dot1qStaticMulticastTable,'dot1qStaticMulticastEntry':dot1qStaticMulticastEntry,_q:dot1qStaticMulticastAddress,_r:dot1qStaticMulticastReceivePort,_AK:dot1qStaticMulticastStaticEgressPorts,_AL:dot1qStaticMulticastForbiddenEgressPorts,_AM:dot1qStaticMulticastStatus,'dot1qVlan':dot1qVlan,_AN:dot1qVlanNumDeletes,'dot1qVlanCurrentTable':dot1qVlanCurrentTable,'dot1qVlanCurrentEntry':dot1qVlanCurrentEntry,_s:dot1qVlanTimeMark,_H:dot1qVlanIndex,_AO:dot1qVlanFdbId,_AP:dot1qVlanCurrentEgressPorts,_AQ:dot1qVlanCurrentUntaggedPorts,_AR:dot1qVlanStatus,_AS:dot1qVlanCreationTime,'dot1qVlanStaticTable':dot1qVlanStaticTable,'dot1qVlanStaticEntry':dot1qVlanStaticEntry,_AT:dot1qVlanStaticName,_AU:dot1qVlanStaticEgressPorts,_AV:dot1qVlanForbiddenEgressPorts,_AW:dot1qVlanStaticUntaggedPorts,_AX:dot1qVlanStaticRowStatus,_AY:dot1qNextFreeLocalVlanIndex,'dot1qPortVlanTable':dot1qPortVlanTable,_A1:dot1qPortVlanEntry,_Q:dot1qPvid,_R:dot1qPortAcceptableFrameTypes,_S:dot1qPortIngressFiltering,_T:dot1qPortGvrpStatus,_U:dot1qPortGvrpFailedRegistrations,_V:dot1qPortGvrpLastPduOrigin,_Ar:dot1qPortRestrictedVlanRegistration,'dot1qPortVlanStatisticsTable':dot1qPortVlanStatisticsTable,'dot1qPortVlanStatisticsEntry':dot1qPortVlanStatisticsEntry,_Aa:dot1qTpVlanPortInFrames,_Ab:dot1qTpVlanPortOutFrames,_Ac:dot1qTpVlanPortInDiscards,_Ad:dot1qTpVlanPortInOverflowFrames,_Ae:dot1qTpVlanPortOutOverflowFrames,_Af:dot1qTpVlanPortInOverflowDiscards,'dot1qPortVlanHCStatisticsTable':dot1qPortVlanHCStatisticsTable,'dot1qPortVlanHCStatisticsEntry':dot1qPortVlanHCStatisticsEntry,_Ag:dot1qTpVlanPortHCInFrames,_Ah:dot1qTpVlanPortHCOutFrames,_Ai:dot1qTpVlanPortHCInDiscards,'dot1qLearningConstraintsTable':dot1qLearningConstraintsTable,'dot1qLearningConstraintsEntry':dot1qLearningConstraintsEntry,_u:dot1qConstraintVlan,_v:dot1qConstraintSet,_Aj:dot1qConstraintType,_Ak:dot1qConstraintStatus,_Al:dot1qConstraintSetDefault,_Am:dot1qConstraintTypeDefault,'dot1vProtocol':dot1vProtocol,'dot1vProtocolGroupTable':dot1vProtocolGroupTable,'dot1vProtocolGroupEntry':dot1vProtocolGroupEntry,_y:dot1vProtocolTemplateFrameType,_z:dot1vProtocolTemplateProtocolValue,_An:dot1vProtocolGroupId,_Ao:dot1vProtocolGroupRowStatus,'dot1vProtocolPortTable':dot1vProtocolPortTable,'dot1vProtocolPortEntry':dot1vProtocolPortEntry,_A0:dot1vProtocolPortGroupId,_Ap:dot1vProtocolPortGroupVid,_Aq:dot1vProtocolPortRowStatus,'qBridgeConformance':qBridgeConformance,'qBridgeGroups':qBridgeGroups,_W:qBridgeBaseGroup,_Z:qBridgeFdbUnicastGroup,_a:qBridgeFdbMulticastGroup,_b:qBridgeServiceRequirementsGroup,_c:qBridgeFdbStaticGroup,_X:qBridgeVlanGroup,_Y:qBridgeVlanStaticGroup,_As:qBridgePortGroup,_d:qBridgeVlanStatisticsGroup,_e:qBridgeVlanStatisticsOverflowGroup,_f:qBridgeVlanHCStatisticsGroup,_g:qBridgeLearningConstraintsGroup,_h:qBridgeLearningConstraintDefaultGroup,_Au:qBridgeClassificationDeviceGroup,_Av:qBridgeClassificationPortGroup,_At:qBridgePortGroup2,'qBridgeCompliances':qBridgeCompliances,'qBridgeCompliance':qBridgeCompliance,'qBridgeCompliance2':qBridgeCompliance2})