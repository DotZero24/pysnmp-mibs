_As='qosInterfaceTypeTableGroup'
_Ar='qosDeviceAttributeTableGroup'
_Aq='qosDevicePibIncarnationTableGroup'
_Ap='qosIfWeightsQueueSize'
_Ao='qosIfWeightsDrainSize'
_An='qosIfWeightsQueue'
_Am='qosIfWeightsNumQueues'
_Al='qosIfWeightsRoles'
_Ak='qosIfTailDropThresholdSetValue'
_Aj='qosIfTailDropThresholdSet'
_Ai='qosIfTailDropNumThresholdSets'
_Ah='qosIfTailDropRoles'
_Ag='qosIfRedThresholdSetUpper'
_Af='qosIfRedThresholdSetLower'
_Ae='qosIfRedThresholdSet'
_Ad='qosIfRedNumThresholdSets'
_Ac='qosIfRedRoles'
_Ab='qosIfThresholdSet'
_Aa='qosIfQueue'
_AZ='qosIfDscp'
_AY='qosIfQueueType'
_AX='qosIfDscpRoles'
_AW='qosIfDropDiscipline'
_AV='qosIfDropPreference'
_AU='qosIfDropRoles'
_AT='qosIfSchedulingQueueType'
_AS='qosIfSchedulingDiscipline'
_AR='qosIfSchedulingPreference'
_AQ='qosIfSchedulingRoles'
_AP='qosIpAclAggregateId'
_AO='qosIpAclMicroFlowPolicerId'
_AN='qosIpAclDscpTrusted'
_AM='qosIpAclDscp'
_AL='qosIpAclOrder'
_AK='qosIpAclInterfaceDirection'
_AJ='qosIpAclInterfaceRoles'
_AI='qosIpAclActAclId'
_AH='qosIpAclDefAceId'
_AG='qosIpAceOrder'
_AF='qosIpAclId'
_AE='qosIpAcePermit'
_AD='qosIpAceSrcL4PortMax'
_AC='qosIpAceSrcL4PortMin'
_AB='qosIpAceDstL4PortMax'
_AA='qosIpAceDstL4PortMin'
_A9='qosIpAceProtocol'
_A8='qosIpAceDscpMax'
_A7='qosIpAceDscpMin'
_A6='qosIpAceSrcAddrMask'
_A5='qosIpAceSrcAddr'
_A4='qosIpAceDstAddrMask'
_A3='qosIpAceDstAddr'
_A2='qosDstMacCos'
_A1='qosDstMacAddress'
_A0='qosDstMacVlan'
_z='qosAggregatePolicerId'
_y='qosPolicerAction'
_x='qosPolicerExcessBurst'
_w='qosPolicerNormalBurst'
_v='qosPolicerRate'
_u='qosUnmatchedPolicyAggregateId'
_t='qosUnmatchPolMicroFlowPolicerId'
_s='qosUnmatchedPolicyDscpTrusted'
_r='qosUnmatchedPolicyDscp'
_q='qosUnmatchedPolicyDirection'
_p='qosUnmatchedPolicyRole'
_o='qosCosToDscpDscp'
_n='qosL2Cos'
_m='qosMarkedDscp'
_l='qosInterfaceTypeCapabilities'
_k='qosInterfaceTypeRoles'
_j='qosInterfaceQueueType'
_i='qosDeviceCapabilities'
_h='qosDeviceMaxMessageSize'
_g='qosDeviceSecondaryPdp'
_f='qosDevicePrimaryPdp'
_e='qosDevicePepDomain'
_d='qosDevicePibTtl'
_c='qosDevicePibIncarnation'
_b='qosDevicePdpName'
_a='qosIfWeightsId'
_Z='qosIfTailDropId'
_Y='qosIfRedId'
_X='qosIfDscpAssignmentId'
_W='qosIfDropPreferenceId'
_V='qosIfSchedulingPreferenceId'
_U='qosIpAclActionId'
_T='qosIpAclDefinitionId'
_S='qosIpAceId'
_R='qosMacClassificationId'
_Q='qosAggregateId'
_P='qosPolicerId'
_O='qosUnmatchedPolicyId'
_N='qosCosToDscpCos'
_M='qosDscp'
_L='qosInterfaceTypeId'
_K='qosDeviceAttributeId'
_J='qosDeviceIncarnationId'
_I='pqCbwfq'
_H='unspecified'
_G='Unsigned32'
_F='OctetString'
_E='not-accessible'
_D='Integer32'
_C='read-only'
_B='NMS-QOS-PIB-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_F,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
nmsPibToMib,=mibBuilder.importSymbols('NMS-SMI','nmsPibToMib')
Unsigned32,=mibBuilder.importSymbols('NMS-TC',_G)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_G,'iso')
DisplayString,MacAddress,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress','TextualConvention','TruthValue')
nmsQosPIBMIB=ModuleIdentity((1,3,6,1,4,1,3320,18,2,1))
if mibBuilder.loadTexts:nmsQosPIBMIB.setRevisions(('2003-10-16 00:00',))
class Dscp(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,63))
class QosLayer2Cos(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
class QueueRange(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,8,16,32,64)));namedValues=NamedValues(*(('oneQ',1),('twoQ',2),('threeQ',3),('fourQ',4),('eightQ',8),('sixteenQ',16),('thirtyTwoQ',32),('sixtyFourQ',64)))
class ThresholdSetRange(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,4,8)));namedValues=NamedValues(*(('zeroT',0),('oneT',1),('twoT',2),('fourT',4),('eightT',8)))
class Percent(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
class QosInterfaceQueueType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33)));namedValues=NamedValues(*(('oneQ1t',1),('oneQ2t',2),('oneQ4t',3),('oneQ8t',4),('twoQ1t',5),('twoQ2t',6),('twoQ4t',7),('twoQ8t',8),('threeQ1t',9),('threeQ2t',10),('threeQ4t',11),('threeQ8t',12),('fourQ1t',13),('fourQ2t',14),('fourQ4t',15),('fourQ8t',16),('eightQ1t',17),('eightQ2t',18),('eightQ4t',19),('eightQ8t',20),('sixteenQ1t',21),('sixteenQ2t',22),('sixteenQ4t',23),('sixtyfourQ1t',24),('sixtyfourQ2t',25),('sixtyfourQ4t',26),('oneP1Q0t',27),('oneP1Q4t',28),('oneP1Q8t',29),('oneP2Q1t',30),('oneP2Q2t',31),('oneP3Q1t',32),('oneP7Q8t',33)))
class QosInterfaceTypeCapabilities(TextualConvention,Bits):status=_A;namedValues=NamedValues(*((_H,0),('inputL2Classification',1),('inputIpClassification',2),('outputL2Classification',3),('outputIpClassification',4),('inputUflowPolicing',5),('inputAggregatePolicing',6),('outputUflowPolicing',7),('outputAggregatePolicing',8),('policeByMarkingDown',9),('policeByDropping',10),('fifo',11),('wrr',12),('wfq',13),('cq',14),('pq',15),('cbwfq',16),('tailDrop',17),('wred',18),('inputPortClassification',19),('outputPortClassification',20),('inputUflowShaping',21),('inputAggregateShaping',22),('outputUflowShaping',23),('outputAggregateShaping',24),('pqWrr',25),(_I,26)))
class RoleCombination(TextualConvention,OctetString):status=_A;subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
class PolicyInstanceId(TextualConvention,Unsigned32):status=_A
class Unsigned64(TextualConvention,Counter64):status=_A
_QosPIBConformance_ObjectIdentity=ObjectIdentity
qosPIBConformance=_QosPIBConformance_ObjectIdentity((1,3,6,1,4,1,3320,18,2,1,1))
_QosPIBCompliances_ObjectIdentity=ObjectIdentity
qosPIBCompliances=_QosPIBCompliances_ObjectIdentity((1,3,6,1,4,1,3320,18,2,1,1,1))
_QosPIBGroups_ObjectIdentity=ObjectIdentity
qosPIBGroups=_QosPIBGroups_ObjectIdentity((1,3,6,1,4,1,3320,18,2,1,1,2))
_QosDeviceConfig_ObjectIdentity=ObjectIdentity
qosDeviceConfig=_QosDeviceConfig_ObjectIdentity((1,3,6,1,4,1,3320,18,2,1,2))
_QosDevicePibIncarnationTable_Object=MibTable
qosDevicePibIncarnationTable=_QosDevicePibIncarnationTable_Object((1,3,6,1,4,1,3320,18,2,1,2,1))
if mibBuilder.loadTexts:qosDevicePibIncarnationTable.setStatus(_A)
_QosDevicePibIncarnationEntry_Object=MibTableRow
qosDevicePibIncarnationEntry=_QosDevicePibIncarnationEntry_Object((1,3,6,1,4,1,3320,18,2,1,2,1,1))
qosDevicePibIncarnationEntry.setIndexNames((0,_B,_J))
if mibBuilder.loadTexts:qosDevicePibIncarnationEntry.setStatus(_A)
_QosDeviceIncarnationId_Type=PolicyInstanceId
_QosDeviceIncarnationId_Object=MibTableColumn
qosDeviceIncarnationId=_QosDeviceIncarnationId_Object((1,3,6,1,4,1,3320,18,2,1,2,1,1,1),_QosDeviceIncarnationId_Type())
qosDeviceIncarnationId.setMaxAccess(_E)
if mibBuilder.loadTexts:qosDeviceIncarnationId.setStatus(_A)
_QosDevicePdpName_Type=DisplayString
_QosDevicePdpName_Object=MibTableColumn
qosDevicePdpName=_QosDevicePdpName_Object((1,3,6,1,4,1,3320,18,2,1,2,1,1,2),_QosDevicePdpName_Type())
qosDevicePdpName.setMaxAccess(_C)
if mibBuilder.loadTexts:qosDevicePdpName.setStatus(_A)
class _QosDevicePibIncarnation_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(128,128));fixedLength=128
_QosDevicePibIncarnation_Type.__name__=_F
_QosDevicePibIncarnation_Object=MibTableColumn
qosDevicePibIncarnation=_QosDevicePibIncarnation_Object((1,3,6,1,4,1,3320,18,2,1,2,1,1,3),_QosDevicePibIncarnation_Type())
qosDevicePibIncarnation.setMaxAccess(_C)
if mibBuilder.loadTexts:qosDevicePibIncarnation.setStatus(_A)
_QosDevicePibTtl_Type=Unsigned32
_QosDevicePibTtl_Object=MibTableColumn
qosDevicePibTtl=_QosDevicePibTtl_Object((1,3,6,1,4,1,3320,18,2,1,2,1,1,4),_QosDevicePibTtl_Type())
qosDevicePibTtl.setMaxAccess(_C)
if mibBuilder.loadTexts:qosDevicePibTtl.setStatus(_A)
_QosDeviceAttributeTable_Object=MibTable
qosDeviceAttributeTable=_QosDeviceAttributeTable_Object((1,3,6,1,4,1,3320,18,2,1,2,2))
if mibBuilder.loadTexts:qosDeviceAttributeTable.setStatus(_A)
_QosDeviceAttributeEntry_Object=MibTableRow
qosDeviceAttributeEntry=_QosDeviceAttributeEntry_Object((1,3,6,1,4,1,3320,18,2,1,2,2,1))
qosDeviceAttributeEntry.setIndexNames((0,_B,_K))
if mibBuilder.loadTexts:qosDeviceAttributeEntry.setStatus(_A)
_QosDeviceAttributeId_Type=PolicyInstanceId
_QosDeviceAttributeId_Object=MibTableColumn
qosDeviceAttributeId=_QosDeviceAttributeId_Object((1,3,6,1,4,1,3320,18,2,1,2,2,1,1),_QosDeviceAttributeId_Type())
qosDeviceAttributeId.setMaxAccess(_E)
if mibBuilder.loadTexts:qosDeviceAttributeId.setStatus(_A)
_QosDevicePepDomain_Type=DisplayString
_QosDevicePepDomain_Object=MibTableColumn
qosDevicePepDomain=_QosDevicePepDomain_Object((1,3,6,1,4,1,3320,18,2,1,2,2,1,2),_QosDevicePepDomain_Type())
qosDevicePepDomain.setMaxAccess(_C)
if mibBuilder.loadTexts:qosDevicePepDomain.setStatus(_A)
_QosDevicePrimaryPdp_Type=IpAddress
_QosDevicePrimaryPdp_Object=MibTableColumn
qosDevicePrimaryPdp=_QosDevicePrimaryPdp_Object((1,3,6,1,4,1,3320,18,2,1,2,2,1,3),_QosDevicePrimaryPdp_Type())
qosDevicePrimaryPdp.setMaxAccess(_C)
if mibBuilder.loadTexts:qosDevicePrimaryPdp.setStatus(_A)
_QosDeviceSecondaryPdp_Type=IpAddress
_QosDeviceSecondaryPdp_Object=MibTableColumn
qosDeviceSecondaryPdp=_QosDeviceSecondaryPdp_Object((1,3,6,1,4,1,3320,18,2,1,2,2,1,4),_QosDeviceSecondaryPdp_Type())
qosDeviceSecondaryPdp.setMaxAccess(_C)
if mibBuilder.loadTexts:qosDeviceSecondaryPdp.setStatus(_A)
_QosDeviceMaxMessageSize_Type=Unsigned32
_QosDeviceMaxMessageSize_Object=MibTableColumn
qosDeviceMaxMessageSize=_QosDeviceMaxMessageSize_Object((1,3,6,1,4,1,3320,18,2,1,2,2,1,5),_QosDeviceMaxMessageSize_Type())
qosDeviceMaxMessageSize.setMaxAccess(_C)
if mibBuilder.loadTexts:qosDeviceMaxMessageSize.setStatus(_A)
class _QosDeviceCapabilities_Type(Bits):namedValues=NamedValues(*((_H,0),('layer2Cos',1),('ipPrecedence',2),('dscp',3)))
_QosDeviceCapabilities_Type.__name__='Bits'
_QosDeviceCapabilities_Object=MibTableColumn
qosDeviceCapabilities=_QosDeviceCapabilities_Object((1,3,6,1,4,1,3320,18,2,1,2,2,1,6),_QosDeviceCapabilities_Type())
qosDeviceCapabilities.setMaxAccess(_C)
if mibBuilder.loadTexts:qosDeviceCapabilities.setStatus(_A)
_QosInterfaceTypeTable_Object=MibTable
qosInterfaceTypeTable=_QosInterfaceTypeTable_Object((1,3,6,1,4,1,3320,18,2,1,2,3))
if mibBuilder.loadTexts:qosInterfaceTypeTable.setStatus(_A)
_QosInterfaceTypeEntry_Object=MibTableRow
qosInterfaceTypeEntry=_QosInterfaceTypeEntry_Object((1,3,6,1,4,1,3320,18,2,1,2,3,1))
qosInterfaceTypeEntry.setIndexNames((0,_B,_L))
if mibBuilder.loadTexts:qosInterfaceTypeEntry.setStatus(_A)
_QosInterfaceTypeId_Type=PolicyInstanceId
_QosInterfaceTypeId_Object=MibTableColumn
qosInterfaceTypeId=_QosInterfaceTypeId_Object((1,3,6,1,4,1,3320,18,2,1,2,3,1,1),_QosInterfaceTypeId_Type())
qosInterfaceTypeId.setMaxAccess(_E)
if mibBuilder.loadTexts:qosInterfaceTypeId.setStatus(_A)
_QosInterfaceQueueType_Type=QosInterfaceQueueType
_QosInterfaceQueueType_Object=MibTableColumn
qosInterfaceQueueType=_QosInterfaceQueueType_Object((1,3,6,1,4,1,3320,18,2,1,2,3,1,2),_QosInterfaceQueueType_Type())
qosInterfaceQueueType.setMaxAccess(_C)
if mibBuilder.loadTexts:qosInterfaceQueueType.setStatus(_A)
_QosInterfaceTypeRoles_Type=RoleCombination
_QosInterfaceTypeRoles_Object=MibTableColumn
qosInterfaceTypeRoles=_QosInterfaceTypeRoles_Object((1,3,6,1,4,1,3320,18,2,1,2,3,1,3),_QosInterfaceTypeRoles_Type())
qosInterfaceTypeRoles.setMaxAccess(_C)
if mibBuilder.loadTexts:qosInterfaceTypeRoles.setStatus(_A)
_QosInterfaceTypeCapabilities_Type=QosInterfaceTypeCapabilities
_QosInterfaceTypeCapabilities_Object=MibTableColumn
qosInterfaceTypeCapabilities=_QosInterfaceTypeCapabilities_Object((1,3,6,1,4,1,3320,18,2,1,2,3,1,4),_QosInterfaceTypeCapabilities_Type())
qosInterfaceTypeCapabilities.setMaxAccess(_C)
if mibBuilder.loadTexts:qosInterfaceTypeCapabilities.setStatus(_A)
_QosDomainConfig_ObjectIdentity=ObjectIdentity
qosDomainConfig=_QosDomainConfig_ObjectIdentity((1,3,6,1,4,1,3320,18,2,1,3))
_QosDiffServMappingTable_Object=MibTable
qosDiffServMappingTable=_QosDiffServMappingTable_Object((1,3,6,1,4,1,3320,18,2,1,3,1))
if mibBuilder.loadTexts:qosDiffServMappingTable.setStatus(_A)
_QosDiffServMappingEntry_Object=MibTableRow
qosDiffServMappingEntry=_QosDiffServMappingEntry_Object((1,3,6,1,4,1,3320,18,2,1,3,1,1))
qosDiffServMappingEntry.setIndexNames((0,_B,_M))
if mibBuilder.loadTexts:qosDiffServMappingEntry.setStatus(_A)
_QosDscp_Type=Dscp
_QosDscp_Object=MibTableColumn
qosDscp=_QosDscp_Object((1,3,6,1,4,1,3320,18,2,1,3,1,1,1),_QosDscp_Type())
qosDscp.setMaxAccess(_E)
if mibBuilder.loadTexts:qosDscp.setStatus(_A)
_QosMarkedDscp_Type=Dscp
_QosMarkedDscp_Object=MibTableColumn
qosMarkedDscp=_QosMarkedDscp_Object((1,3,6,1,4,1,3320,18,2,1,3,1,1,2),_QosMarkedDscp_Type())
qosMarkedDscp.setMaxAccess(_C)
if mibBuilder.loadTexts:qosMarkedDscp.setStatus(_A)
_QosL2Cos_Type=QosLayer2Cos
_QosL2Cos_Object=MibTableColumn
qosL2Cos=_QosL2Cos_Object((1,3,6,1,4,1,3320,18,2,1,3,1,1,3),_QosL2Cos_Type())
qosL2Cos.setMaxAccess(_C)
if mibBuilder.loadTexts:qosL2Cos.setStatus(_A)
_QosCosToDscpTable_Object=MibTable
qosCosToDscpTable=_QosCosToDscpTable_Object((1,3,6,1,4,1,3320,18,2,1,3,2))
if mibBuilder.loadTexts:qosCosToDscpTable.setStatus(_A)
_QosCosToDscpEntry_Object=MibTableRow
qosCosToDscpEntry=_QosCosToDscpEntry_Object((1,3,6,1,4,1,3320,18,2,1,3,2,1))
qosCosToDscpEntry.setIndexNames((0,_B,_N))
if mibBuilder.loadTexts:qosCosToDscpEntry.setStatus(_A)
_QosCosToDscpCos_Type=QosLayer2Cos
_QosCosToDscpCos_Object=MibTableColumn
qosCosToDscpCos=_QosCosToDscpCos_Object((1,3,6,1,4,1,3320,18,2,1,3,2,1,1),_QosCosToDscpCos_Type())
qosCosToDscpCos.setMaxAccess(_E)
if mibBuilder.loadTexts:qosCosToDscpCos.setStatus(_A)
_QosCosToDscpDscp_Type=Dscp
_QosCosToDscpDscp_Object=MibTableColumn
qosCosToDscpDscp=_QosCosToDscpDscp_Object((1,3,6,1,4,1,3320,18,2,1,3,2,1,2),_QosCosToDscpDscp_Type())
qosCosToDscpDscp.setMaxAccess(_C)
if mibBuilder.loadTexts:qosCosToDscpDscp.setStatus(_A)
_QosUnmatchedPolicy_ObjectIdentity=ObjectIdentity
qosUnmatchedPolicy=_QosUnmatchedPolicy_ObjectIdentity((1,3,6,1,4,1,3320,18,2,1,4))
_QosUnmatchedPolicyTable_Object=MibTable
qosUnmatchedPolicyTable=_QosUnmatchedPolicyTable_Object((1,3,6,1,4,1,3320,18,2,1,4,1))
if mibBuilder.loadTexts:qosUnmatchedPolicyTable.setStatus(_A)
_QosUnmatchedPolicyEntry_Object=MibTableRow
qosUnmatchedPolicyEntry=_QosUnmatchedPolicyEntry_Object((1,3,6,1,4,1,3320,18,2,1,4,1,1))
qosUnmatchedPolicyEntry.setIndexNames((0,_B,_O))
if mibBuilder.loadTexts:qosUnmatchedPolicyEntry.setStatus(_A)
_QosUnmatchedPolicyId_Type=PolicyInstanceId
_QosUnmatchedPolicyId_Object=MibTableColumn
qosUnmatchedPolicyId=_QosUnmatchedPolicyId_Object((1,3,6,1,4,1,3320,18,2,1,4,1,1,1),_QosUnmatchedPolicyId_Type())
qosUnmatchedPolicyId.setMaxAccess(_E)
if mibBuilder.loadTexts:qosUnmatchedPolicyId.setStatus(_A)
_QosUnmatchedPolicyRole_Type=RoleCombination
_QosUnmatchedPolicyRole_Object=MibTableColumn
qosUnmatchedPolicyRole=_QosUnmatchedPolicyRole_Object((1,3,6,1,4,1,3320,18,2,1,4,1,1,2),_QosUnmatchedPolicyRole_Type())
qosUnmatchedPolicyRole.setMaxAccess(_C)
if mibBuilder.loadTexts:qosUnmatchedPolicyRole.setStatus(_A)
class _QosUnmatchedPolicyDirection_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('in',0),('out',1)))
_QosUnmatchedPolicyDirection_Type.__name__=_D
_QosUnmatchedPolicyDirection_Object=MibTableColumn
qosUnmatchedPolicyDirection=_QosUnmatchedPolicyDirection_Object((1,3,6,1,4,1,3320,18,2,1,4,1,1,3),_QosUnmatchedPolicyDirection_Type())
qosUnmatchedPolicyDirection.setMaxAccess(_C)
if mibBuilder.loadTexts:qosUnmatchedPolicyDirection.setStatus(_A)
_QosUnmatchedPolicyDscp_Type=Dscp
_QosUnmatchedPolicyDscp_Object=MibTableColumn
qosUnmatchedPolicyDscp=_QosUnmatchedPolicyDscp_Object((1,3,6,1,4,1,3320,18,2,1,4,1,1,4),_QosUnmatchedPolicyDscp_Type())
qosUnmatchedPolicyDscp.setMaxAccess(_C)
if mibBuilder.loadTexts:qosUnmatchedPolicyDscp.setStatus(_A)
_QosUnmatchedPolicyDscpTrusted_Type=TruthValue
_QosUnmatchedPolicyDscpTrusted_Object=MibTableColumn
qosUnmatchedPolicyDscpTrusted=_QosUnmatchedPolicyDscpTrusted_Object((1,3,6,1,4,1,3320,18,2,1,4,1,1,5),_QosUnmatchedPolicyDscpTrusted_Type())
qosUnmatchedPolicyDscpTrusted.setMaxAccess(_C)
if mibBuilder.loadTexts:qosUnmatchedPolicyDscpTrusted.setStatus(_A)
_QosUnmatchPolMicroFlowPolicerId_Type=PolicyInstanceId
_QosUnmatchPolMicroFlowPolicerId_Object=MibTableColumn
qosUnmatchPolMicroFlowPolicerId=_QosUnmatchPolMicroFlowPolicerId_Object((1,3,6,1,4,1,3320,18,2,1,4,1,1,6),_QosUnmatchPolMicroFlowPolicerId_Type())
qosUnmatchPolMicroFlowPolicerId.setMaxAccess(_C)
if mibBuilder.loadTexts:qosUnmatchPolMicroFlowPolicerId.setStatus(_A)
_QosUnmatchedPolicyAggregateId_Type=PolicyInstanceId
_QosUnmatchedPolicyAggregateId_Object=MibTableColumn
qosUnmatchedPolicyAggregateId=_QosUnmatchedPolicyAggregateId_Object((1,3,6,1,4,1,3320,18,2,1,4,1,1,7),_QosUnmatchedPolicyAggregateId_Type())
qosUnmatchedPolicyAggregateId.setMaxAccess(_C)
if mibBuilder.loadTexts:qosUnmatchedPolicyAggregateId.setStatus(_A)
_QosPolicer_ObjectIdentity=ObjectIdentity
qosPolicer=_QosPolicer_ObjectIdentity((1,3,6,1,4,1,3320,18,2,1,5))
_QosPolicerTable_Object=MibTable
qosPolicerTable=_QosPolicerTable_Object((1,3,6,1,4,1,3320,18,2,1,5,1))
if mibBuilder.loadTexts:qosPolicerTable.setStatus(_A)
_QosPolicerEntry_Object=MibTableRow
qosPolicerEntry=_QosPolicerEntry_Object((1,3,6,1,4,1,3320,18,2,1,5,1,1))
qosPolicerEntry.setIndexNames((0,_B,_P))
if mibBuilder.loadTexts:qosPolicerEntry.setStatus(_A)
_QosPolicerId_Type=PolicyInstanceId
_QosPolicerId_Object=MibTableColumn
qosPolicerId=_QosPolicerId_Object((1,3,6,1,4,1,3320,18,2,1,5,1,1,1),_QosPolicerId_Type())
qosPolicerId.setMaxAccess(_E)
if mibBuilder.loadTexts:qosPolicerId.setStatus(_A)
_QosPolicerRate_Type=Unsigned64
_QosPolicerRate_Object=MibTableColumn
qosPolicerRate=_QosPolicerRate_Object((1,3,6,1,4,1,3320,18,2,1,5,1,1,2),_QosPolicerRate_Type())
qosPolicerRate.setMaxAccess(_C)
if mibBuilder.loadTexts:qosPolicerRate.setStatus(_A)
_QosPolicerNormalBurst_Type=Unsigned32
_QosPolicerNormalBurst_Object=MibTableColumn
qosPolicerNormalBurst=_QosPolicerNormalBurst_Object((1,3,6,1,4,1,3320,18,2,1,5,1,1,3),_QosPolicerNormalBurst_Type())
qosPolicerNormalBurst.setMaxAccess(_C)
if mibBuilder.loadTexts:qosPolicerNormalBurst.setStatus(_A)
_QosPolicerExcessBurst_Type=Unsigned32
_QosPolicerExcessBurst_Object=MibTableColumn
qosPolicerExcessBurst=_QosPolicerExcessBurst_Object((1,3,6,1,4,1,3320,18,2,1,5,1,1,4),_QosPolicerExcessBurst_Type())
qosPolicerExcessBurst.setMaxAccess(_C)
if mibBuilder.loadTexts:qosPolicerExcessBurst.setStatus(_A)
class _QosPolicerAction_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('drop',0),('mark',1),('shape',2)))
_QosPolicerAction_Type.__name__=_D
_QosPolicerAction_Object=MibTableColumn
qosPolicerAction=_QosPolicerAction_Object((1,3,6,1,4,1,3320,18,2,1,5,1,1,5),_QosPolicerAction_Type())
qosPolicerAction.setMaxAccess(_C)
if mibBuilder.loadTexts:qosPolicerAction.setStatus(_A)
_QosAggregateTable_Object=MibTable
qosAggregateTable=_QosAggregateTable_Object((1,3,6,1,4,1,3320,18,2,1,5,2))
if mibBuilder.loadTexts:qosAggregateTable.setStatus(_A)
_QosAggregateEntry_Object=MibTableRow
qosAggregateEntry=_QosAggregateEntry_Object((1,3,6,1,4,1,3320,18,2,1,5,2,1))
qosAggregateEntry.setIndexNames((0,_B,_Q))
if mibBuilder.loadTexts:qosAggregateEntry.setStatus(_A)
_QosAggregateId_Type=PolicyInstanceId
_QosAggregateId_Object=MibTableColumn
qosAggregateId=_QosAggregateId_Object((1,3,6,1,4,1,3320,18,2,1,5,2,1,1),_QosAggregateId_Type())
qosAggregateId.setMaxAccess(_E)
if mibBuilder.loadTexts:qosAggregateId.setStatus(_A)
_QosAggregatePolicerId_Type=PolicyInstanceId
_QosAggregatePolicerId_Object=MibTableColumn
qosAggregatePolicerId=_QosAggregatePolicerId_Object((1,3,6,1,4,1,3320,18,2,1,5,2,1,2),_QosAggregatePolicerId_Type())
qosAggregatePolicerId.setMaxAccess(_C)
if mibBuilder.loadTexts:qosAggregatePolicerId.setStatus(_A)
_QosMacQos_ObjectIdentity=ObjectIdentity
qosMacQos=_QosMacQos_ObjectIdentity((1,3,6,1,4,1,3320,18,2,1,6))
_QosMacClassificationTable_Object=MibTable
qosMacClassificationTable=_QosMacClassificationTable_Object((1,3,6,1,4,1,3320,18,2,1,6,1))
if mibBuilder.loadTexts:qosMacClassificationTable.setStatus(_A)
_QosMacClassificationEntry_Object=MibTableRow
qosMacClassificationEntry=_QosMacClassificationEntry_Object((1,3,6,1,4,1,3320,18,2,1,6,1,1))
qosMacClassificationEntry.setIndexNames((0,_B,_R))
if mibBuilder.loadTexts:qosMacClassificationEntry.setStatus(_A)
_QosMacClassificationId_Type=PolicyInstanceId
_QosMacClassificationId_Object=MibTableColumn
qosMacClassificationId=_QosMacClassificationId_Object((1,3,6,1,4,1,3320,18,2,1,6,1,1,1),_QosMacClassificationId_Type())
qosMacClassificationId.setMaxAccess(_E)
if mibBuilder.loadTexts:qosMacClassificationId.setStatus(_A)
class _QosDstMacVlan_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4095))
_QosDstMacVlan_Type.__name__=_D
_QosDstMacVlan_Object=MibTableColumn
qosDstMacVlan=_QosDstMacVlan_Object((1,3,6,1,4,1,3320,18,2,1,6,1,1,2),_QosDstMacVlan_Type())
qosDstMacVlan.setMaxAccess(_C)
if mibBuilder.loadTexts:qosDstMacVlan.setStatus(_A)
_QosDstMacAddress_Type=MacAddress
_QosDstMacAddress_Object=MibTableColumn
qosDstMacAddress=_QosDstMacAddress_Object((1,3,6,1,4,1,3320,18,2,1,6,1,1,3),_QosDstMacAddress_Type())
qosDstMacAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:qosDstMacAddress.setStatus(_A)
_QosDstMacCos_Type=QosLayer2Cos
_QosDstMacCos_Object=MibTableColumn
qosDstMacCos=_QosDstMacCos_Object((1,3,6,1,4,1,3320,18,2,1,6,1,1,4),_QosDstMacCos_Type())
qosDstMacCos.setMaxAccess(_C)
if mibBuilder.loadTexts:qosDstMacCos.setStatus(_A)
_QosIpQos_ObjectIdentity=ObjectIdentity
qosIpQos=_QosIpQos_ObjectIdentity((1,3,6,1,4,1,3320,18,2,1,7))
_QosIpAceTable_Object=MibTable
qosIpAceTable=_QosIpAceTable_Object((1,3,6,1,4,1,3320,18,2,1,7,1))
if mibBuilder.loadTexts:qosIpAceTable.setStatus(_A)
_QosIpAceEntry_Object=MibTableRow
qosIpAceEntry=_QosIpAceEntry_Object((1,3,6,1,4,1,3320,18,2,1,7,1,1))
qosIpAceEntry.setIndexNames((0,_B,_S))
if mibBuilder.loadTexts:qosIpAceEntry.setStatus(_A)
_QosIpAceId_Type=PolicyInstanceId
_QosIpAceId_Object=MibTableColumn
qosIpAceId=_QosIpAceId_Object((1,3,6,1,4,1,3320,18,2,1,7,1,1,1),_QosIpAceId_Type())
qosIpAceId.setMaxAccess(_E)
if mibBuilder.loadTexts:qosIpAceId.setStatus(_A)
_QosIpAceDstAddr_Type=IpAddress
_QosIpAceDstAddr_Object=MibTableColumn
qosIpAceDstAddr=_QosIpAceDstAddr_Object((1,3,6,1,4,1,3320,18,2,1,7,1,1,2),_QosIpAceDstAddr_Type())
qosIpAceDstAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:qosIpAceDstAddr.setStatus(_A)
_QosIpAceDstAddrMask_Type=IpAddress
_QosIpAceDstAddrMask_Object=MibTableColumn
qosIpAceDstAddrMask=_QosIpAceDstAddrMask_Object((1,3,6,1,4,1,3320,18,2,1,7,1,1,3),_QosIpAceDstAddrMask_Type())
qosIpAceDstAddrMask.setMaxAccess(_C)
if mibBuilder.loadTexts:qosIpAceDstAddrMask.setStatus(_A)
_QosIpAceSrcAddr_Type=IpAddress
_QosIpAceSrcAddr_Object=MibTableColumn
qosIpAceSrcAddr=_QosIpAceSrcAddr_Object((1,3,6,1,4,1,3320,18,2,1,7,1,1,4),_QosIpAceSrcAddr_Type())
qosIpAceSrcAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:qosIpAceSrcAddr.setStatus(_A)
_QosIpAceSrcAddrMask_Type=IpAddress
_QosIpAceSrcAddrMask_Object=MibTableColumn
qosIpAceSrcAddrMask=_QosIpAceSrcAddrMask_Object((1,3,6,1,4,1,3320,18,2,1,7,1,1,5),_QosIpAceSrcAddrMask_Type())
qosIpAceSrcAddrMask.setMaxAccess(_C)
if mibBuilder.loadTexts:qosIpAceSrcAddrMask.setStatus(_A)
_QosIpAceDscpMin_Type=Dscp
_QosIpAceDscpMin_Object=MibTableColumn
qosIpAceDscpMin=_QosIpAceDscpMin_Object((1,3,6,1,4,1,3320,18,2,1,7,1,1,6),_QosIpAceDscpMin_Type())
qosIpAceDscpMin.setMaxAccess(_C)
if mibBuilder.loadTexts:qosIpAceDscpMin.setStatus(_A)
_QosIpAceDscpMax_Type=Dscp
_QosIpAceDscpMax_Object=MibTableColumn
qosIpAceDscpMax=_QosIpAceDscpMax_Object((1,3,6,1,4,1,3320,18,2,1,7,1,1,7),_QosIpAceDscpMax_Type())
qosIpAceDscpMax.setMaxAccess(_C)
if mibBuilder.loadTexts:qosIpAceDscpMax.setStatus(_A)
class _QosIpAceProtocol_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_QosIpAceProtocol_Type.__name__=_D
_QosIpAceProtocol_Object=MibTableColumn
qosIpAceProtocol=_QosIpAceProtocol_Object((1,3,6,1,4,1,3320,18,2,1,7,1,1,8),_QosIpAceProtocol_Type())
qosIpAceProtocol.setMaxAccess(_C)
if mibBuilder.loadTexts:qosIpAceProtocol.setStatus(_A)
class _QosIpAceDstL4PortMin_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_QosIpAceDstL4PortMin_Type.__name__=_D
_QosIpAceDstL4PortMin_Object=MibTableColumn
qosIpAceDstL4PortMin=_QosIpAceDstL4PortMin_Object((1,3,6,1,4,1,3320,18,2,1,7,1,1,9),_QosIpAceDstL4PortMin_Type())
qosIpAceDstL4PortMin.setMaxAccess(_C)
if mibBuilder.loadTexts:qosIpAceDstL4PortMin.setStatus(_A)
class _QosIpAceDstL4PortMax_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_QosIpAceDstL4PortMax_Type.__name__=_D
_QosIpAceDstL4PortMax_Object=MibTableColumn
qosIpAceDstL4PortMax=_QosIpAceDstL4PortMax_Object((1,3,6,1,4,1,3320,18,2,1,7,1,1,10),_QosIpAceDstL4PortMax_Type())
qosIpAceDstL4PortMax.setMaxAccess(_C)
if mibBuilder.loadTexts:qosIpAceDstL4PortMax.setStatus(_A)
class _QosIpAceSrcL4PortMin_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_QosIpAceSrcL4PortMin_Type.__name__=_D
_QosIpAceSrcL4PortMin_Object=MibTableColumn
qosIpAceSrcL4PortMin=_QosIpAceSrcL4PortMin_Object((1,3,6,1,4,1,3320,18,2,1,7,1,1,11),_QosIpAceSrcL4PortMin_Type())
qosIpAceSrcL4PortMin.setMaxAccess(_C)
if mibBuilder.loadTexts:qosIpAceSrcL4PortMin.setStatus(_A)
class _QosIpAceSrcL4PortMax_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_QosIpAceSrcL4PortMax_Type.__name__=_D
_QosIpAceSrcL4PortMax_Object=MibTableColumn
qosIpAceSrcL4PortMax=_QosIpAceSrcL4PortMax_Object((1,3,6,1,4,1,3320,18,2,1,7,1,1,12),_QosIpAceSrcL4PortMax_Type())
qosIpAceSrcL4PortMax.setMaxAccess(_C)
if mibBuilder.loadTexts:qosIpAceSrcL4PortMax.setStatus(_A)
_QosIpAcePermit_Type=TruthValue
_QosIpAcePermit_Object=MibTableColumn
qosIpAcePermit=_QosIpAcePermit_Object((1,3,6,1,4,1,3320,18,2,1,7,1,1,13),_QosIpAcePermit_Type())
qosIpAcePermit.setMaxAccess(_C)
if mibBuilder.loadTexts:qosIpAcePermit.setStatus(_A)
_QosIpAclDefinitionTable_Object=MibTable
qosIpAclDefinitionTable=_QosIpAclDefinitionTable_Object((1,3,6,1,4,1,3320,18,2,1,7,2))
if mibBuilder.loadTexts:qosIpAclDefinitionTable.setStatus(_A)
_QosIpAclDefinitionEntry_Object=MibTableRow
qosIpAclDefinitionEntry=_QosIpAclDefinitionEntry_Object((1,3,6,1,4,1,3320,18,2,1,7,2,1))
qosIpAclDefinitionEntry.setIndexNames((0,_B,_T))
if mibBuilder.loadTexts:qosIpAclDefinitionEntry.setStatus(_A)
_QosIpAclDefinitionId_Type=PolicyInstanceId
_QosIpAclDefinitionId_Object=MibTableColumn
qosIpAclDefinitionId=_QosIpAclDefinitionId_Object((1,3,6,1,4,1,3320,18,2,1,7,2,1,1),_QosIpAclDefinitionId_Type())
qosIpAclDefinitionId.setMaxAccess(_E)
if mibBuilder.loadTexts:qosIpAclDefinitionId.setStatus(_A)
_QosIpAclId_Type=PolicyInstanceId
_QosIpAclId_Object=MibTableColumn
qosIpAclId=_QosIpAclId_Object((1,3,6,1,4,1,3320,18,2,1,7,2,1,2),_QosIpAclId_Type())
qosIpAclId.setMaxAccess(_C)
if mibBuilder.loadTexts:qosIpAclId.setStatus(_A)
_QosIpAceOrder_Type=Unsigned32
_QosIpAceOrder_Object=MibTableColumn
qosIpAceOrder=_QosIpAceOrder_Object((1,3,6,1,4,1,3320,18,2,1,7,2,1,3),_QosIpAceOrder_Type())
qosIpAceOrder.setMaxAccess(_C)
if mibBuilder.loadTexts:qosIpAceOrder.setStatus(_A)
_QosIpAclDefAceId_Type=PolicyInstanceId
_QosIpAclDefAceId_Object=MibTableColumn
qosIpAclDefAceId=_QosIpAclDefAceId_Object((1,3,6,1,4,1,3320,18,2,1,7,2,1,4),_QosIpAclDefAceId_Type())
qosIpAclDefAceId.setMaxAccess(_C)
if mibBuilder.loadTexts:qosIpAclDefAceId.setStatus(_A)
_QosIpAclActionTable_Object=MibTable
qosIpAclActionTable=_QosIpAclActionTable_Object((1,3,6,1,4,1,3320,18,2,1,7,3))
if mibBuilder.loadTexts:qosIpAclActionTable.setStatus(_A)
_QosIpAclActionEntry_Object=MibTableRow
qosIpAclActionEntry=_QosIpAclActionEntry_Object((1,3,6,1,4,1,3320,18,2,1,7,3,1))
qosIpAclActionEntry.setIndexNames((0,_B,_U))
if mibBuilder.loadTexts:qosIpAclActionEntry.setStatus(_A)
_QosIpAclActionId_Type=PolicyInstanceId
_QosIpAclActionId_Object=MibTableColumn
qosIpAclActionId=_QosIpAclActionId_Object((1,3,6,1,4,1,3320,18,2,1,7,3,1,1),_QosIpAclActionId_Type())
qosIpAclActionId.setMaxAccess(_E)
if mibBuilder.loadTexts:qosIpAclActionId.setStatus(_A)
_QosIpAclActAclId_Type=PolicyInstanceId
_QosIpAclActAclId_Object=MibTableColumn
qosIpAclActAclId=_QosIpAclActAclId_Object((1,3,6,1,4,1,3320,18,2,1,7,3,1,2),_QosIpAclActAclId_Type())
qosIpAclActAclId.setMaxAccess(_C)
if mibBuilder.loadTexts:qosIpAclActAclId.setStatus(_A)
_QosIpAclInterfaceRoles_Type=RoleCombination
_QosIpAclInterfaceRoles_Object=MibTableColumn
qosIpAclInterfaceRoles=_QosIpAclInterfaceRoles_Object((1,3,6,1,4,1,3320,18,2,1,7,3,1,3),_QosIpAclInterfaceRoles_Type())
qosIpAclInterfaceRoles.setMaxAccess(_C)
if mibBuilder.loadTexts:qosIpAclInterfaceRoles.setStatus(_A)
class _QosIpAclInterfaceDirection_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('in',0),('out',1)))
_QosIpAclInterfaceDirection_Type.__name__=_D
_QosIpAclInterfaceDirection_Object=MibTableColumn
qosIpAclInterfaceDirection=_QosIpAclInterfaceDirection_Object((1,3,6,1,4,1,3320,18,2,1,7,3,1,4),_QosIpAclInterfaceDirection_Type())
qosIpAclInterfaceDirection.setMaxAccess(_C)
if mibBuilder.loadTexts:qosIpAclInterfaceDirection.setStatus(_A)
_QosIpAclOrder_Type=Unsigned32
_QosIpAclOrder_Object=MibTableColumn
qosIpAclOrder=_QosIpAclOrder_Object((1,3,6,1,4,1,3320,18,2,1,7,3,1,5),_QosIpAclOrder_Type())
qosIpAclOrder.setMaxAccess(_C)
if mibBuilder.loadTexts:qosIpAclOrder.setStatus(_A)
_QosIpAclDscp_Type=Dscp
_QosIpAclDscp_Object=MibTableColumn
qosIpAclDscp=_QosIpAclDscp_Object((1,3,6,1,4,1,3320,18,2,1,7,3,1,6),_QosIpAclDscp_Type())
qosIpAclDscp.setMaxAccess(_C)
if mibBuilder.loadTexts:qosIpAclDscp.setStatus(_A)
_QosIpAclDscpTrusted_Type=TruthValue
_QosIpAclDscpTrusted_Object=MibTableColumn
qosIpAclDscpTrusted=_QosIpAclDscpTrusted_Object((1,3,6,1,4,1,3320,18,2,1,7,3,1,7),_QosIpAclDscpTrusted_Type())
qosIpAclDscpTrusted.setMaxAccess(_C)
if mibBuilder.loadTexts:qosIpAclDscpTrusted.setStatus(_A)
_QosIpAclMicroFlowPolicerId_Type=PolicyInstanceId
_QosIpAclMicroFlowPolicerId_Object=MibTableColumn
qosIpAclMicroFlowPolicerId=_QosIpAclMicroFlowPolicerId_Object((1,3,6,1,4,1,3320,18,2,1,7,3,1,8),_QosIpAclMicroFlowPolicerId_Type())
qosIpAclMicroFlowPolicerId.setMaxAccess(_C)
if mibBuilder.loadTexts:qosIpAclMicroFlowPolicerId.setStatus(_A)
_QosIpAclAggregateId_Type=PolicyInstanceId
_QosIpAclAggregateId_Object=MibTableColumn
qosIpAclAggregateId=_QosIpAclAggregateId_Object((1,3,6,1,4,1,3320,18,2,1,7,3,1,9),_QosIpAclAggregateId_Type())
qosIpAclAggregateId.setMaxAccess(_C)
if mibBuilder.loadTexts:qosIpAclAggregateId.setStatus(_A)
_QosIfParameters_ObjectIdentity=ObjectIdentity
qosIfParameters=_QosIfParameters_ObjectIdentity((1,3,6,1,4,1,3320,18,2,1,8))
_QosIfSchedulingPreferencesTable_Object=MibTable
qosIfSchedulingPreferencesTable=_QosIfSchedulingPreferencesTable_Object((1,3,6,1,4,1,3320,18,2,1,8,1))
if mibBuilder.loadTexts:qosIfSchedulingPreferencesTable.setStatus(_A)
_QosIfSchedulingPreferenceEntry_Object=MibTableRow
qosIfSchedulingPreferenceEntry=_QosIfSchedulingPreferenceEntry_Object((1,3,6,1,4,1,3320,18,2,1,8,1,1))
qosIfSchedulingPreferenceEntry.setIndexNames((0,_B,_V))
if mibBuilder.loadTexts:qosIfSchedulingPreferenceEntry.setStatus(_A)
_QosIfSchedulingPreferenceId_Type=PolicyInstanceId
_QosIfSchedulingPreferenceId_Object=MibTableColumn
qosIfSchedulingPreferenceId=_QosIfSchedulingPreferenceId_Object((1,3,6,1,4,1,3320,18,2,1,8,1,1,1),_QosIfSchedulingPreferenceId_Type())
qosIfSchedulingPreferenceId.setMaxAccess(_E)
if mibBuilder.loadTexts:qosIfSchedulingPreferenceId.setStatus(_A)
_QosIfSchedulingRoles_Type=RoleCombination
_QosIfSchedulingRoles_Object=MibTableColumn
qosIfSchedulingRoles=_QosIfSchedulingRoles_Object((1,3,6,1,4,1,3320,18,2,1,8,1,1,2),_QosIfSchedulingRoles_Type())
qosIfSchedulingRoles.setMaxAccess(_C)
if mibBuilder.loadTexts:qosIfSchedulingRoles.setStatus(_A)
class _QosIfSchedulingPreference_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,16))
_QosIfSchedulingPreference_Type.__name__=_D
_QosIfSchedulingPreference_Object=MibTableColumn
qosIfSchedulingPreference=_QosIfSchedulingPreference_Object((1,3,6,1,4,1,3320,18,2,1,8,1,1,3),_QosIfSchedulingPreference_Type())
qosIfSchedulingPreference.setMaxAccess(_C)
if mibBuilder.loadTexts:qosIfSchedulingPreference.setStatus(_A)
class _QosIfSchedulingDiscipline_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8)));namedValues=NamedValues(*(('weightedFairQueueing',1),('weightedRoundRobin',2),('customQueueing',3),('priorityQueueing',4),('classBasedWFQ',5),('fifo',6),('pqWrr',7),(_I,8)))
_QosIfSchedulingDiscipline_Type.__name__=_D
_QosIfSchedulingDiscipline_Object=MibTableColumn
qosIfSchedulingDiscipline=_QosIfSchedulingDiscipline_Object((1,3,6,1,4,1,3320,18,2,1,8,1,1,4),_QosIfSchedulingDiscipline_Type())
qosIfSchedulingDiscipline.setMaxAccess(_C)
if mibBuilder.loadTexts:qosIfSchedulingDiscipline.setStatus(_A)
_QosIfSchedulingQueueType_Type=QosInterfaceQueueType
_QosIfSchedulingQueueType_Object=MibTableColumn
qosIfSchedulingQueueType=_QosIfSchedulingQueueType_Object((1,3,6,1,4,1,3320,18,2,1,8,1,1,5),_QosIfSchedulingQueueType_Type())
qosIfSchedulingQueueType.setMaxAccess(_C)
if mibBuilder.loadTexts:qosIfSchedulingQueueType.setStatus(_A)
_QosIfDropPreferenceTable_Object=MibTable
qosIfDropPreferenceTable=_QosIfDropPreferenceTable_Object((1,3,6,1,4,1,3320,18,2,1,8,2))
if mibBuilder.loadTexts:qosIfDropPreferenceTable.setStatus(_A)
_QosIfDropPreferenceEntry_Object=MibTableRow
qosIfDropPreferenceEntry=_QosIfDropPreferenceEntry_Object((1,3,6,1,4,1,3320,18,2,1,8,2,1))
qosIfDropPreferenceEntry.setIndexNames((0,_B,_W))
if mibBuilder.loadTexts:qosIfDropPreferenceEntry.setStatus(_A)
_QosIfDropPreferenceId_Type=PolicyInstanceId
_QosIfDropPreferenceId_Object=MibTableColumn
qosIfDropPreferenceId=_QosIfDropPreferenceId_Object((1,3,6,1,4,1,3320,18,2,1,8,2,1,1),_QosIfDropPreferenceId_Type())
qosIfDropPreferenceId.setMaxAccess(_E)
if mibBuilder.loadTexts:qosIfDropPreferenceId.setStatus(_A)
_QosIfDropRoles_Type=RoleCombination
_QosIfDropRoles_Object=MibTableColumn
qosIfDropRoles=_QosIfDropRoles_Object((1,3,6,1,4,1,3320,18,2,1,8,2,1,2),_QosIfDropRoles_Type())
qosIfDropRoles.setMaxAccess(_C)
if mibBuilder.loadTexts:qosIfDropRoles.setStatus(_A)
class _QosIfDropPreference_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,16))
_QosIfDropPreference_Type.__name__=_D
_QosIfDropPreference_Object=MibTableColumn
qosIfDropPreference=_QosIfDropPreference_Object((1,3,6,1,4,1,3320,18,2,1,8,2,1,3),_QosIfDropPreference_Type())
qosIfDropPreference.setMaxAccess(_C)
if mibBuilder.loadTexts:qosIfDropPreference.setStatus(_A)
class _QosIfDropDiscipline_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('qosIfDropWRED',1),('qosIfDropTailDrop',2)))
_QosIfDropDiscipline_Type.__name__=_D
_QosIfDropDiscipline_Object=MibTableColumn
qosIfDropDiscipline=_QosIfDropDiscipline_Object((1,3,6,1,4,1,3320,18,2,1,8,2,1,4),_QosIfDropDiscipline_Type())
qosIfDropDiscipline.setMaxAccess(_C)
if mibBuilder.loadTexts:qosIfDropDiscipline.setStatus(_A)
_QosIfDscpAssignmentTable_Object=MibTable
qosIfDscpAssignmentTable=_QosIfDscpAssignmentTable_Object((1,3,6,1,4,1,3320,18,2,1,8,3))
if mibBuilder.loadTexts:qosIfDscpAssignmentTable.setStatus(_A)
_QosIfDscpAssignmentEntry_Object=MibTableRow
qosIfDscpAssignmentEntry=_QosIfDscpAssignmentEntry_Object((1,3,6,1,4,1,3320,18,2,1,8,3,1))
qosIfDscpAssignmentEntry.setIndexNames((0,_B,_X))
if mibBuilder.loadTexts:qosIfDscpAssignmentEntry.setStatus(_A)
_QosIfDscpAssignmentId_Type=PolicyInstanceId
_QosIfDscpAssignmentId_Object=MibTableColumn
qosIfDscpAssignmentId=_QosIfDscpAssignmentId_Object((1,3,6,1,4,1,3320,18,2,1,8,3,1,1),_QosIfDscpAssignmentId_Type())
qosIfDscpAssignmentId.setMaxAccess(_E)
if mibBuilder.loadTexts:qosIfDscpAssignmentId.setStatus(_A)
_QosIfDscpRoles_Type=RoleCombination
_QosIfDscpRoles_Object=MibTableColumn
qosIfDscpRoles=_QosIfDscpRoles_Object((1,3,6,1,4,1,3320,18,2,1,8,3,1,2),_QosIfDscpRoles_Type())
qosIfDscpRoles.setMaxAccess(_C)
if mibBuilder.loadTexts:qosIfDscpRoles.setStatus(_A)
_QosIfQueueType_Type=QosInterfaceQueueType
_QosIfQueueType_Object=MibTableColumn
qosIfQueueType=_QosIfQueueType_Object((1,3,6,1,4,1,3320,18,2,1,8,3,1,3),_QosIfQueueType_Type())
qosIfQueueType.setMaxAccess(_C)
if mibBuilder.loadTexts:qosIfQueueType.setStatus(_A)
_QosIfDscp_Type=Dscp
_QosIfDscp_Object=MibTableColumn
qosIfDscp=_QosIfDscp_Object((1,3,6,1,4,1,3320,18,2,1,8,3,1,4),_QosIfDscp_Type())
qosIfDscp.setMaxAccess(_C)
if mibBuilder.loadTexts:qosIfDscp.setStatus(_A)
class _QosIfQueue_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,64))
_QosIfQueue_Type.__name__=_D
_QosIfQueue_Object=MibTableColumn
qosIfQueue=_QosIfQueue_Object((1,3,6,1,4,1,3320,18,2,1,8,3,1,5),_QosIfQueue_Type())
qosIfQueue.setMaxAccess(_C)
if mibBuilder.loadTexts:qosIfQueue.setStatus(_A)
class _QosIfThresholdSet_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,8))
_QosIfThresholdSet_Type.__name__=_D
_QosIfThresholdSet_Object=MibTableColumn
qosIfThresholdSet=_QosIfThresholdSet_Object((1,3,6,1,4,1,3320,18,2,1,8,3,1,6),_QosIfThresholdSet_Type())
qosIfThresholdSet.setMaxAccess(_C)
if mibBuilder.loadTexts:qosIfThresholdSet.setStatus(_A)
_QosIfRedTable_Object=MibTable
qosIfRedTable=_QosIfRedTable_Object((1,3,6,1,4,1,3320,18,2,1,8,4))
if mibBuilder.loadTexts:qosIfRedTable.setStatus(_A)
_QosIfRedEntry_Object=MibTableRow
qosIfRedEntry=_QosIfRedEntry_Object((1,3,6,1,4,1,3320,18,2,1,8,4,1))
qosIfRedEntry.setIndexNames((0,_B,_Y))
if mibBuilder.loadTexts:qosIfRedEntry.setStatus(_A)
_QosIfRedId_Type=PolicyInstanceId
_QosIfRedId_Object=MibTableColumn
qosIfRedId=_QosIfRedId_Object((1,3,6,1,4,1,3320,18,2,1,8,4,1,1),_QosIfRedId_Type())
qosIfRedId.setMaxAccess(_E)
if mibBuilder.loadTexts:qosIfRedId.setStatus(_A)
_QosIfRedRoles_Type=RoleCombination
_QosIfRedRoles_Object=MibTableColumn
qosIfRedRoles=_QosIfRedRoles_Object((1,3,6,1,4,1,3320,18,2,1,8,4,1,2),_QosIfRedRoles_Type())
qosIfRedRoles.setMaxAccess(_C)
if mibBuilder.loadTexts:qosIfRedRoles.setStatus(_A)
_QosIfRedNumThresholdSets_Type=ThresholdSetRange
_QosIfRedNumThresholdSets_Object=MibTableColumn
qosIfRedNumThresholdSets=_QosIfRedNumThresholdSets_Object((1,3,6,1,4,1,3320,18,2,1,8,4,1,3),_QosIfRedNumThresholdSets_Type())
qosIfRedNumThresholdSets.setMaxAccess(_C)
if mibBuilder.loadTexts:qosIfRedNumThresholdSets.setStatus(_A)
class _QosIfRedThresholdSet_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,8))
_QosIfRedThresholdSet_Type.__name__=_D
_QosIfRedThresholdSet_Object=MibTableColumn
qosIfRedThresholdSet=_QosIfRedThresholdSet_Object((1,3,6,1,4,1,3320,18,2,1,8,4,1,4),_QosIfRedThresholdSet_Type())
qosIfRedThresholdSet.setMaxAccess(_C)
if mibBuilder.loadTexts:qosIfRedThresholdSet.setStatus(_A)
_QosIfRedThresholdSetLower_Type=Percent
_QosIfRedThresholdSetLower_Object=MibTableColumn
qosIfRedThresholdSetLower=_QosIfRedThresholdSetLower_Object((1,3,6,1,4,1,3320,18,2,1,8,4,1,5),_QosIfRedThresholdSetLower_Type())
qosIfRedThresholdSetLower.setMaxAccess(_C)
if mibBuilder.loadTexts:qosIfRedThresholdSetLower.setStatus(_A)
_QosIfRedThresholdSetUpper_Type=Percent
_QosIfRedThresholdSetUpper_Object=MibTableColumn
qosIfRedThresholdSetUpper=_QosIfRedThresholdSetUpper_Object((1,3,6,1,4,1,3320,18,2,1,8,4,1,6),_QosIfRedThresholdSetUpper_Type())
qosIfRedThresholdSetUpper.setMaxAccess(_C)
if mibBuilder.loadTexts:qosIfRedThresholdSetUpper.setStatus(_A)
_QosIfTailDropTable_Object=MibTable
qosIfTailDropTable=_QosIfTailDropTable_Object((1,3,6,1,4,1,3320,18,2,1,8,5))
if mibBuilder.loadTexts:qosIfTailDropTable.setStatus(_A)
_QosIfTailDropEntry_Object=MibTableRow
qosIfTailDropEntry=_QosIfTailDropEntry_Object((1,3,6,1,4,1,3320,18,2,1,8,5,1))
qosIfTailDropEntry.setIndexNames((0,_B,_Z))
if mibBuilder.loadTexts:qosIfTailDropEntry.setStatus(_A)
_QosIfTailDropId_Type=PolicyInstanceId
_QosIfTailDropId_Object=MibTableColumn
qosIfTailDropId=_QosIfTailDropId_Object((1,3,6,1,4,1,3320,18,2,1,8,5,1,1),_QosIfTailDropId_Type())
qosIfTailDropId.setMaxAccess(_E)
if mibBuilder.loadTexts:qosIfTailDropId.setStatus(_A)
_QosIfTailDropRoles_Type=RoleCombination
_QosIfTailDropRoles_Object=MibTableColumn
qosIfTailDropRoles=_QosIfTailDropRoles_Object((1,3,6,1,4,1,3320,18,2,1,8,5,1,2),_QosIfTailDropRoles_Type())
qosIfTailDropRoles.setMaxAccess(_C)
if mibBuilder.loadTexts:qosIfTailDropRoles.setStatus(_A)
_QosIfTailDropNumThresholdSets_Type=ThresholdSetRange
_QosIfTailDropNumThresholdSets_Object=MibTableColumn
qosIfTailDropNumThresholdSets=_QosIfTailDropNumThresholdSets_Object((1,3,6,1,4,1,3320,18,2,1,8,5,1,3),_QosIfTailDropNumThresholdSets_Type())
qosIfTailDropNumThresholdSets.setMaxAccess(_C)
if mibBuilder.loadTexts:qosIfTailDropNumThresholdSets.setStatus(_A)
class _QosIfTailDropThresholdSet_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,8))
_QosIfTailDropThresholdSet_Type.__name__=_D
_QosIfTailDropThresholdSet_Object=MibTableColumn
qosIfTailDropThresholdSet=_QosIfTailDropThresholdSet_Object((1,3,6,1,4,1,3320,18,2,1,8,5,1,4),_QosIfTailDropThresholdSet_Type())
qosIfTailDropThresholdSet.setMaxAccess(_C)
if mibBuilder.loadTexts:qosIfTailDropThresholdSet.setStatus(_A)
_QosIfTailDropThresholdSetValue_Type=Percent
_QosIfTailDropThresholdSetValue_Object=MibTableColumn
qosIfTailDropThresholdSetValue=_QosIfTailDropThresholdSetValue_Object((1,3,6,1,4,1,3320,18,2,1,8,5,1,5),_QosIfTailDropThresholdSetValue_Type())
qosIfTailDropThresholdSetValue.setMaxAccess(_C)
if mibBuilder.loadTexts:qosIfTailDropThresholdSetValue.setStatus(_A)
_QosIfWeightsTable_Object=MibTable
qosIfWeightsTable=_QosIfWeightsTable_Object((1,3,6,1,4,1,3320,18,2,1,8,6))
if mibBuilder.loadTexts:qosIfWeightsTable.setStatus(_A)
_QosIfWeightsEntry_Object=MibTableRow
qosIfWeightsEntry=_QosIfWeightsEntry_Object((1,3,6,1,4,1,3320,18,2,1,8,6,1))
qosIfWeightsEntry.setIndexNames((0,_B,_a))
if mibBuilder.loadTexts:qosIfWeightsEntry.setStatus(_A)
_QosIfWeightsId_Type=PolicyInstanceId
_QosIfWeightsId_Object=MibTableColumn
qosIfWeightsId=_QosIfWeightsId_Object((1,3,6,1,4,1,3320,18,2,1,8,6,1,1),_QosIfWeightsId_Type())
qosIfWeightsId.setMaxAccess(_E)
if mibBuilder.loadTexts:qosIfWeightsId.setStatus(_A)
_QosIfWeightsRoles_Type=RoleCombination
_QosIfWeightsRoles_Object=MibTableColumn
qosIfWeightsRoles=_QosIfWeightsRoles_Object((1,3,6,1,4,1,3320,18,2,1,8,6,1,2),_QosIfWeightsRoles_Type())
qosIfWeightsRoles.setMaxAccess(_C)
if mibBuilder.loadTexts:qosIfWeightsRoles.setStatus(_A)
_QosIfWeightsNumQueues_Type=QueueRange
_QosIfWeightsNumQueues_Object=MibTableColumn
qosIfWeightsNumQueues=_QosIfWeightsNumQueues_Object((1,3,6,1,4,1,3320,18,2,1,8,6,1,3),_QosIfWeightsNumQueues_Type())
qosIfWeightsNumQueues.setMaxAccess(_C)
if mibBuilder.loadTexts:qosIfWeightsNumQueues.setStatus(_A)
class _QosIfWeightsQueue_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,64))
_QosIfWeightsQueue_Type.__name__=_D
_QosIfWeightsQueue_Object=MibTableColumn
qosIfWeightsQueue=_QosIfWeightsQueue_Object((1,3,6,1,4,1,3320,18,2,1,8,6,1,4),_QosIfWeightsQueue_Type())
qosIfWeightsQueue.setMaxAccess(_C)
if mibBuilder.loadTexts:qosIfWeightsQueue.setStatus(_A)
_QosIfWeightsDrainSize_Type=Unsigned32
_QosIfWeightsDrainSize_Object=MibTableColumn
qosIfWeightsDrainSize=_QosIfWeightsDrainSize_Object((1,3,6,1,4,1,3320,18,2,1,8,6,1,5),_QosIfWeightsDrainSize_Type())
qosIfWeightsDrainSize.setMaxAccess(_C)
if mibBuilder.loadTexts:qosIfWeightsDrainSize.setStatus(_A)
_QosIfWeightsQueueSize_Type=Unsigned32
_QosIfWeightsQueueSize_Object=MibTableColumn
qosIfWeightsQueueSize=_QosIfWeightsQueueSize_Object((1,3,6,1,4,1,3320,18,2,1,8,6,1,6),_QosIfWeightsQueueSize_Type())
qosIfWeightsQueueSize.setMaxAccess(_C)
if mibBuilder.loadTexts:qosIfWeightsQueueSize.setStatus(_A)
qosDevicePibIncarnationTableGroup=ObjectGroup((1,3,6,1,4,1,3320,18,2,1,1,2,1))
qosDevicePibIncarnationTableGroup.setObjects(*((_B,_b),(_B,_c),(_B,_d)))
if mibBuilder.loadTexts:qosDevicePibIncarnationTableGroup.setStatus(_A)
qosDeviceAttributeTableGroup=ObjectGroup((1,3,6,1,4,1,3320,18,2,1,1,2,2))
qosDeviceAttributeTableGroup.setObjects(*((_B,_e),(_B,_f),(_B,_g),(_B,_h),(_B,_i)))
if mibBuilder.loadTexts:qosDeviceAttributeTableGroup.setStatus(_A)
qosInterfaceTypeTableGroup=ObjectGroup((1,3,6,1,4,1,3320,18,2,1,1,2,3))
qosInterfaceTypeTableGroup.setObjects(*((_B,_j),(_B,_k),(_B,_l)))
if mibBuilder.loadTexts:qosInterfaceTypeTableGroup.setStatus(_A)
qosDiffServMappingTableGroup=ObjectGroup((1,3,6,1,4,1,3320,18,2,1,1,2,4))
qosDiffServMappingTableGroup.setObjects(*((_B,_m),(_B,_n)))
if mibBuilder.loadTexts:qosDiffServMappingTableGroup.setStatus(_A)
qosCosToDscpTableGroup=ObjectGroup((1,3,6,1,4,1,3320,18,2,1,1,2,5))
qosCosToDscpTableGroup.setObjects((_B,_o))
if mibBuilder.loadTexts:qosCosToDscpTableGroup.setStatus(_A)
qosUnmatchedPolicyTableGroup=ObjectGroup((1,3,6,1,4,1,3320,18,2,1,1,2,6))
qosUnmatchedPolicyTableGroup.setObjects(*((_B,_p),(_B,_q),(_B,_r),(_B,_s),(_B,_t),(_B,_u)))
if mibBuilder.loadTexts:qosUnmatchedPolicyTableGroup.setStatus(_A)
qosPolicerTableGroup=ObjectGroup((1,3,6,1,4,1,3320,18,2,1,1,2,7))
qosPolicerTableGroup.setObjects(*((_B,_v),(_B,_w),(_B,_x),(_B,_y)))
if mibBuilder.loadTexts:qosPolicerTableGroup.setStatus(_A)
qosAggregateTableGroup=ObjectGroup((1,3,6,1,4,1,3320,18,2,1,1,2,8))
qosAggregateTableGroup.setObjects((_B,_z))
if mibBuilder.loadTexts:qosAggregateTableGroup.setStatus(_A)
qosMacClassificationTableGroup=ObjectGroup((1,3,6,1,4,1,3320,18,2,1,1,2,9))
qosMacClassificationTableGroup.setObjects(*((_B,_A0),(_B,_A1),(_B,_A2)))
if mibBuilder.loadTexts:qosMacClassificationTableGroup.setStatus(_A)
qosIpAceTableGroup=ObjectGroup((1,3,6,1,4,1,3320,18,2,1,1,2,10))
qosIpAceTableGroup.setObjects(*((_B,_A3),(_B,_A4),(_B,_A5),(_B,_A6),(_B,_A7),(_B,_A8),(_B,_A9),(_B,_AA),(_B,_AB),(_B,_AC),(_B,_AD),(_B,_AE)))
if mibBuilder.loadTexts:qosIpAceTableGroup.setStatus(_A)
qosIpAclDefinitionTableGroup=ObjectGroup((1,3,6,1,4,1,3320,18,2,1,1,2,11))
qosIpAclDefinitionTableGroup.setObjects(*((_B,_AF),(_B,_AG),(_B,_AH)))
if mibBuilder.loadTexts:qosIpAclDefinitionTableGroup.setStatus(_A)
qosIpAclActionTableGroup=ObjectGroup((1,3,6,1,4,1,3320,18,2,1,1,2,12))
qosIpAclActionTableGroup.setObjects(*((_B,_AI),(_B,_AJ),(_B,_AK),(_B,_AL),(_B,_AM),(_B,_AN),(_B,_AO),(_B,_AP)))
if mibBuilder.loadTexts:qosIpAclActionTableGroup.setStatus(_A)
qosIfSchedulingPreferencesTableGroup=ObjectGroup((1,3,6,1,4,1,3320,18,2,1,1,2,13))
qosIfSchedulingPreferencesTableGroup.setObjects(*((_B,_AQ),(_B,_AR),(_B,_AS),(_B,_AT)))
if mibBuilder.loadTexts:qosIfSchedulingPreferencesTableGroup.setStatus(_A)
qosIfDropPreferenceTableGroup=ObjectGroup((1,3,6,1,4,1,3320,18,2,1,1,2,14))
qosIfDropPreferenceTableGroup.setObjects(*((_B,_AU),(_B,_AV),(_B,_AW)))
if mibBuilder.loadTexts:qosIfDropPreferenceTableGroup.setStatus(_A)
qosIfDscpAssignmentTableGroup=ObjectGroup((1,3,6,1,4,1,3320,18,2,1,1,2,15))
qosIfDscpAssignmentTableGroup.setObjects(*((_B,_AX),(_B,_AY),(_B,_AZ),(_B,_Aa),(_B,_Ab)))
if mibBuilder.loadTexts:qosIfDscpAssignmentTableGroup.setStatus(_A)
qosIfRedTableGroup=ObjectGroup((1,3,6,1,4,1,3320,18,2,1,1,2,16))
qosIfRedTableGroup.setObjects(*((_B,_Ac),(_B,_Ad),(_B,_Ae),(_B,_Af),(_B,_Ag)))
if mibBuilder.loadTexts:qosIfRedTableGroup.setStatus(_A)
qosIfTailDropTableGroup=ObjectGroup((1,3,6,1,4,1,3320,18,2,1,1,2,17))
qosIfTailDropTableGroup.setObjects(*((_B,_Ah),(_B,_Ai),(_B,_Aj),(_B,_Ak)))
if mibBuilder.loadTexts:qosIfTailDropTableGroup.setStatus(_A)
qosIfWeightsTableGroup=ObjectGroup((1,3,6,1,4,1,3320,18,2,1,1,2,18))
qosIfWeightsTableGroup.setObjects(*((_B,_Al),(_B,_Am),(_B,_An),(_B,_Ao),(_B,_Ap)))
if mibBuilder.loadTexts:qosIfWeightsTableGroup.setStatus(_A)
qosPIBCompliance=ModuleCompliance((1,3,6,1,4,1,3320,18,2,1,1,1,1))
qosPIBCompliance.setObjects(*((_B,_Aq),(_B,_Ar),(_B,_As)))
if mibBuilder.loadTexts:qosPIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'Dscp':Dscp,'QosLayer2Cos':QosLayer2Cos,'QueueRange':QueueRange,'ThresholdSetRange':ThresholdSetRange,'Percent':Percent,'QosInterfaceQueueType':QosInterfaceQueueType,'QosInterfaceTypeCapabilities':QosInterfaceTypeCapabilities,'RoleCombination':RoleCombination,'PolicyInstanceId':PolicyInstanceId,'Unsigned64':Unsigned64,'nmsQosPIBMIB':nmsQosPIBMIB,'qosPIBConformance':qosPIBConformance,'qosPIBCompliances':qosPIBCompliances,'qosPIBCompliance':qosPIBCompliance,'qosPIBGroups':qosPIBGroups,_Aq:qosDevicePibIncarnationTableGroup,_Ar:qosDeviceAttributeTableGroup,_As:qosInterfaceTypeTableGroup,'qosDiffServMappingTableGroup':qosDiffServMappingTableGroup,'qosCosToDscpTableGroup':qosCosToDscpTableGroup,'qosUnmatchedPolicyTableGroup':qosUnmatchedPolicyTableGroup,'qosPolicerTableGroup':qosPolicerTableGroup,'qosAggregateTableGroup':qosAggregateTableGroup,'qosMacClassificationTableGroup':qosMacClassificationTableGroup,'qosIpAceTableGroup':qosIpAceTableGroup,'qosIpAclDefinitionTableGroup':qosIpAclDefinitionTableGroup,'qosIpAclActionTableGroup':qosIpAclActionTableGroup,'qosIfSchedulingPreferencesTableGroup':qosIfSchedulingPreferencesTableGroup,'qosIfDropPreferenceTableGroup':qosIfDropPreferenceTableGroup,'qosIfDscpAssignmentTableGroup':qosIfDscpAssignmentTableGroup,'qosIfRedTableGroup':qosIfRedTableGroup,'qosIfTailDropTableGroup':qosIfTailDropTableGroup,'qosIfWeightsTableGroup':qosIfWeightsTableGroup,'qosDeviceConfig':qosDeviceConfig,'qosDevicePibIncarnationTable':qosDevicePibIncarnationTable,'qosDevicePibIncarnationEntry':qosDevicePibIncarnationEntry,_J:qosDeviceIncarnationId,_b:qosDevicePdpName,_c:qosDevicePibIncarnation,_d:qosDevicePibTtl,'qosDeviceAttributeTable':qosDeviceAttributeTable,'qosDeviceAttributeEntry':qosDeviceAttributeEntry,_K:qosDeviceAttributeId,_e:qosDevicePepDomain,_f:qosDevicePrimaryPdp,_g:qosDeviceSecondaryPdp,_h:qosDeviceMaxMessageSize,_i:qosDeviceCapabilities,'qosInterfaceTypeTable':qosInterfaceTypeTable,'qosInterfaceTypeEntry':qosInterfaceTypeEntry,_L:qosInterfaceTypeId,_j:qosInterfaceQueueType,_k:qosInterfaceTypeRoles,_l:qosInterfaceTypeCapabilities,'qosDomainConfig':qosDomainConfig,'qosDiffServMappingTable':qosDiffServMappingTable,'qosDiffServMappingEntry':qosDiffServMappingEntry,_M:qosDscp,_m:qosMarkedDscp,_n:qosL2Cos,'qosCosToDscpTable':qosCosToDscpTable,'qosCosToDscpEntry':qosCosToDscpEntry,_N:qosCosToDscpCos,_o:qosCosToDscpDscp,'qosUnmatchedPolicy':qosUnmatchedPolicy,'qosUnmatchedPolicyTable':qosUnmatchedPolicyTable,'qosUnmatchedPolicyEntry':qosUnmatchedPolicyEntry,_O:qosUnmatchedPolicyId,_p:qosUnmatchedPolicyRole,_q:qosUnmatchedPolicyDirection,_r:qosUnmatchedPolicyDscp,_s:qosUnmatchedPolicyDscpTrusted,_t:qosUnmatchPolMicroFlowPolicerId,_u:qosUnmatchedPolicyAggregateId,'qosPolicer':qosPolicer,'qosPolicerTable':qosPolicerTable,'qosPolicerEntry':qosPolicerEntry,_P:qosPolicerId,_v:qosPolicerRate,_w:qosPolicerNormalBurst,_x:qosPolicerExcessBurst,_y:qosPolicerAction,'qosAggregateTable':qosAggregateTable,'qosAggregateEntry':qosAggregateEntry,_Q:qosAggregateId,_z:qosAggregatePolicerId,'qosMacQos':qosMacQos,'qosMacClassificationTable':qosMacClassificationTable,'qosMacClassificationEntry':qosMacClassificationEntry,_R:qosMacClassificationId,_A0:qosDstMacVlan,_A1:qosDstMacAddress,_A2:qosDstMacCos,'qosIpQos':qosIpQos,'qosIpAceTable':qosIpAceTable,'qosIpAceEntry':qosIpAceEntry,_S:qosIpAceId,_A3:qosIpAceDstAddr,_A4:qosIpAceDstAddrMask,_A5:qosIpAceSrcAddr,_A6:qosIpAceSrcAddrMask,_A7:qosIpAceDscpMin,_A8:qosIpAceDscpMax,_A9:qosIpAceProtocol,_AA:qosIpAceDstL4PortMin,_AB:qosIpAceDstL4PortMax,_AC:qosIpAceSrcL4PortMin,_AD:qosIpAceSrcL4PortMax,_AE:qosIpAcePermit,'qosIpAclDefinitionTable':qosIpAclDefinitionTable,'qosIpAclDefinitionEntry':qosIpAclDefinitionEntry,_T:qosIpAclDefinitionId,_AF:qosIpAclId,_AG:qosIpAceOrder,_AH:qosIpAclDefAceId,'qosIpAclActionTable':qosIpAclActionTable,'qosIpAclActionEntry':qosIpAclActionEntry,_U:qosIpAclActionId,_AI:qosIpAclActAclId,_AJ:qosIpAclInterfaceRoles,_AK:qosIpAclInterfaceDirection,_AL:qosIpAclOrder,_AM:qosIpAclDscp,_AN:qosIpAclDscpTrusted,_AO:qosIpAclMicroFlowPolicerId,_AP:qosIpAclAggregateId,'qosIfParameters':qosIfParameters,'qosIfSchedulingPreferencesTable':qosIfSchedulingPreferencesTable,'qosIfSchedulingPreferenceEntry':qosIfSchedulingPreferenceEntry,_V:qosIfSchedulingPreferenceId,_AQ:qosIfSchedulingRoles,_AR:qosIfSchedulingPreference,_AS:qosIfSchedulingDiscipline,_AT:qosIfSchedulingQueueType,'qosIfDropPreferenceTable':qosIfDropPreferenceTable,'qosIfDropPreferenceEntry':qosIfDropPreferenceEntry,_W:qosIfDropPreferenceId,_AU:qosIfDropRoles,_AV:qosIfDropPreference,_AW:qosIfDropDiscipline,'qosIfDscpAssignmentTable':qosIfDscpAssignmentTable,'qosIfDscpAssignmentEntry':qosIfDscpAssignmentEntry,_X:qosIfDscpAssignmentId,_AX:qosIfDscpRoles,_AY:qosIfQueueType,_AZ:qosIfDscp,_Aa:qosIfQueue,_Ab:qosIfThresholdSet,'qosIfRedTable':qosIfRedTable,'qosIfRedEntry':qosIfRedEntry,_Y:qosIfRedId,_Ac:qosIfRedRoles,_Ad:qosIfRedNumThresholdSets,_Ae:qosIfRedThresholdSet,_Af:qosIfRedThresholdSetLower,_Ag:qosIfRedThresholdSetUpper,'qosIfTailDropTable':qosIfTailDropTable,'qosIfTailDropEntry':qosIfTailDropEntry,_Z:qosIfTailDropId,_Ah:qosIfTailDropRoles,_Ai:qosIfTailDropNumThresholdSets,_Aj:qosIfTailDropThresholdSet,_Ak:qosIfTailDropThresholdSetValue,'qosIfWeightsTable':qosIfWeightsTable,'qosIfWeightsEntry':qosIfWeightsEntry,_a:qosIfWeightsId,_Al:qosIfWeightsRoles,_Am:qosIfWeightsNumQueues,_An:qosIfWeightsQueue,_Ao:qosIfWeightsDrainSize,_Ap:qosIfWeightsQueueSize})