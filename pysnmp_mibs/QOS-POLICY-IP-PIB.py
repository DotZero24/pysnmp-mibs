_Ae='qosTargetGroup'
_Ad='qosActionGroup'
_Ac='qosMeterGroup'
_Ab='qosIfQueueGroup'
_Aa='qosInterfaceTypeGroup'
_AZ='qosIpAclDefinitionLabel'
_AY='qosIpAclDefinitionStatus'
_AX='qosIpAclDefinitionStorageType'
_AW='qosIpAclDefinitionAceOrder'
_AV='qosIpAclDefinitionAceId'
_AU='qosIpAclDefinitionAclId'
_AT='qosIpAceStatus'
_AS='qosIpAceStorageType'
_AR='qosIpAcePermit'
_AQ='qosIpAceSrcL4PortMax'
_AP='qosIpAceSrcL4PortMin'
_AO='qosIpAceDstL4PortMax'
_AN='qosIpAceDstL4PortMin'
_AM='qosIpAceProtocol'
_AL='qosIpAceDscp'
_AK='qosIpAceSrcAddrMask'
_AJ='qosIpAceSrcAddr'
_AI='qosIpAceDstAddrMask'
_AH='qosIpAceDstAddr'
_AG='qosTargetUserGroupSession'
_AF='qosTargetOutOfProfileAction'
_AE='qosTargetInProfileAction'
_AD='qosTargetLabel'
_AC='qosTargetShapingGroup'
_AB='qosTargetShapingParams'
_AA='qosTargetStatus'
_A9='qosTargetStorageType'
_A8='qosTargetMeter'
_A7='qosTargetOrder'
_A6='qosTargetInterfaceDirection'
_A5='qosTargetInterfaceRoles'
_A4='qosTargetAclType'
_A3='qosTargetAclId'
_A2='qosActionLabel'
_A1='qosActionStatus'
_A0='qosActionStorageType'
_z='qosActionMeter'
_y='qosActionUpdateDSCP'
_x='qosActionDrop'
_w='qosMeterLabel'
_v='qosMeterStatus'
_u='qosMeterStorageType'
_t='qosMeterLowConfAction'
_s='qosMeterMedConfAction'
_r='qosMeterHighConfAction'
_q='qosMeterPeakBurst'
_p='qosMeterPeakRate'
_o='qosMeterCommittedBurst'
_n='qosMeterCommittedRate'
_m='qosMeterDataSpecification'
_l='qosIfDscpAssignmentStatus'
_k='qosIfDscpAssignmentStorageType'
_j='qosIfDscpAssignmentQueue'
_i='qosIfDscpAssignmentDscp'
_h='qosIfDscpAssignmentRoles'
_g='qosIfQueueStatus'
_f='qosIfQueueStorageType'
_e='qosIfQueueSize'
_d='qosIfQueueServiceOrder'
_c='qosIfQueueBandwidthAllocation'
_b='qosIfQueueAbsBandwidth'
_a='qosIfQueueDrainSize'
_Z='qosIfQueueExtDiscipline'
_Y='qosIfQueueGenDiscipline'
_X='qosIfQueueIndex'
_W='qosIfQueueSetId'
_V='qosInterfaceTypeStatus'
_U='qosInterfaceTypeStorageType'
_T='qosInterfaceTypeCapabilities'
_S='qosInterfaceTypeQueueSet'
_R='qosInterfaceTypeRoles'
_Q='qosIpAclDefinitionId'
_P='qosIpAceId'
_O='qosTargetId'
_N='qosActionId'
_M='qosMeterId'
_L='qosIfDscpAssignmentId'
_K='qosIfQueueId'
_J='qosInterfaceTypeId'
_I='PolicyInstanceIdOrZero'
_H='SnmpAdminString'
_G='Unsigned32'
_F='not-accessible'
_E='StorageType'
_D='Integer32'
_C='read-create'
_B='QOS-POLICY-IP-PIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
PolicyInstanceId,RoleCombination=mibBuilder.importSymbols('POLICY-FRAMEWORK-PIB','PolicyInstanceId','RoleCombination')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB',_H)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_G,'iso')
DisplayString,PhysAddress,RowStatus,StorageType,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus',_E,'TextualConvention','TruthValue')
policy,=mibBuilder.importSymbols('SYNOPTICS-ROOT-MIB','policy')
qosPolicyIpPib=ModuleIdentity((1,3,6,1,4,1,45,4,2))
if mibBuilder.loadTexts:qosPolicyIpPib.setRevisions(('2004-07-20 00:00',))
class Dscp(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,63))
class PolicyInstanceIdOrZero(TextualConvention,Unsigned32):status=_A;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
class QosInterfaceQueueCount(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,64))
_QosPolicyGenPibClasses_ObjectIdentity=ObjectIdentity
qosPolicyGenPibClasses=_QosPolicyGenPibClasses_ObjectIdentity((1,3,6,1,4,1,45,4,2,1))
_QosIfParameters_ObjectIdentity=ObjectIdentity
qosIfParameters=_QosIfParameters_ObjectIdentity((1,3,6,1,4,1,45,4,2,1,1))
_QosInterfaceTypeTable_Object=MibTable
qosInterfaceTypeTable=_QosInterfaceTypeTable_Object((1,3,6,1,4,1,45,4,2,1,1,1))
if mibBuilder.loadTexts:qosInterfaceTypeTable.setStatus(_A)
_QosInterfaceTypeEntry_Object=MibTableRow
qosInterfaceTypeEntry=_QosInterfaceTypeEntry_Object((1,3,6,1,4,1,45,4,2,1,1,1,1))
qosInterfaceTypeEntry.setIndexNames((0,_B,_J))
if mibBuilder.loadTexts:qosInterfaceTypeEntry.setStatus(_A)
_QosInterfaceTypeId_Type=PolicyInstanceId
_QosInterfaceTypeId_Object=MibTableColumn
qosInterfaceTypeId=_QosInterfaceTypeId_Object((1,3,6,1,4,1,45,4,2,1,1,1,1,1),_QosInterfaceTypeId_Type())
qosInterfaceTypeId.setMaxAccess(_F)
if mibBuilder.loadTexts:qosInterfaceTypeId.setStatus(_A)
_QosInterfaceTypeRoles_Type=RoleCombination
_QosInterfaceTypeRoles_Object=MibTableColumn
qosInterfaceTypeRoles=_QosInterfaceTypeRoles_Object((1,3,6,1,4,1,45,4,2,1,1,1,1,2),_QosInterfaceTypeRoles_Type())
qosInterfaceTypeRoles.setMaxAccess(_C)
if mibBuilder.loadTexts:qosInterfaceTypeRoles.setStatus(_A)
_QosInterfaceTypeQueueSet_Type=PolicyInstanceId
_QosInterfaceTypeQueueSet_Object=MibTableColumn
qosInterfaceTypeQueueSet=_QosInterfaceTypeQueueSet_Object((1,3,6,1,4,1,45,4,2,1,1,1,1,3),_QosInterfaceTypeQueueSet_Type())
qosInterfaceTypeQueueSet.setMaxAccess(_C)
if mibBuilder.loadTexts:qosInterfaceTypeQueueSet.setStatus(_A)
class _QosInterfaceTypeCapabilities_Type(Bits):namedValues=NamedValues(*(('other',0),('inputIpClassification',1),('outputIpClassification',2),('input802Classification',3),('output802Classification',4),('singleQueuingDiscipline',5),('hybridQueuingDiscipline',6)))
_QosInterfaceTypeCapabilities_Type.__name__='Bits'
_QosInterfaceTypeCapabilities_Object=MibTableColumn
qosInterfaceTypeCapabilities=_QosInterfaceTypeCapabilities_Object((1,3,6,1,4,1,45,4,2,1,1,1,1,4),_QosInterfaceTypeCapabilities_Type())
qosInterfaceTypeCapabilities.setMaxAccess(_C)
if mibBuilder.loadTexts:qosInterfaceTypeCapabilities.setStatus(_A)
class _QosInterfaceTypeStorageType_Type(StorageType):defaultValue=2
_QosInterfaceTypeStorageType_Type.__name__=_E
_QosInterfaceTypeStorageType_Object=MibTableColumn
qosInterfaceTypeStorageType=_QosInterfaceTypeStorageType_Object((1,3,6,1,4,1,45,4,2,1,1,1,1,5),_QosInterfaceTypeStorageType_Type())
qosInterfaceTypeStorageType.setMaxAccess(_C)
if mibBuilder.loadTexts:qosInterfaceTypeStorageType.setStatus(_A)
_QosInterfaceTypeStatus_Type=RowStatus
_QosInterfaceTypeStatus_Object=MibTableColumn
qosInterfaceTypeStatus=_QosInterfaceTypeStatus_Object((1,3,6,1,4,1,45,4,2,1,1,1,1,6),_QosInterfaceTypeStatus_Type())
qosInterfaceTypeStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:qosInterfaceTypeStatus.setStatus(_A)
_QosIfQueueTable_Object=MibTable
qosIfQueueTable=_QosIfQueueTable_Object((1,3,6,1,4,1,45,4,2,1,1,2))
if mibBuilder.loadTexts:qosIfQueueTable.setStatus(_A)
_QosIfQueueEntry_Object=MibTableRow
qosIfQueueEntry=_QosIfQueueEntry_Object((1,3,6,1,4,1,45,4,2,1,1,2,1))
qosIfQueueEntry.setIndexNames((0,_B,_K))
if mibBuilder.loadTexts:qosIfQueueEntry.setStatus(_A)
_QosIfQueueId_Type=PolicyInstanceId
_QosIfQueueId_Object=MibTableColumn
qosIfQueueId=_QosIfQueueId_Object((1,3,6,1,4,1,45,4,2,1,1,2,1,1),_QosIfQueueId_Type())
qosIfQueueId.setMaxAccess(_F)
if mibBuilder.loadTexts:qosIfQueueId.setStatus(_A)
class _QosIfQueueSetId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_QosIfQueueSetId_Type.__name__=_D
_QosIfQueueSetId_Object=MibTableColumn
qosIfQueueSetId=_QosIfQueueSetId_Object((1,3,6,1,4,1,45,4,2,1,1,2,1,2),_QosIfQueueSetId_Type())
qosIfQueueSetId.setMaxAccess(_C)
if mibBuilder.loadTexts:qosIfQueueSetId.setStatus(_A)
_QosIfQueueIndex_Type=QosInterfaceQueueCount
_QosIfQueueIndex_Object=MibTableColumn
qosIfQueueIndex=_QosIfQueueIndex_Object((1,3,6,1,4,1,45,4,2,1,1,2,1,3),_QosIfQueueIndex_Type())
qosIfQueueIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:qosIfQueueIndex.setStatus(_A)
class _QosIfQueueGenDiscipline_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('other',1),('fifo',2),('pq',3),('fq',4),('wfq',5)))
_QosIfQueueGenDiscipline_Type.__name__=_D
_QosIfQueueGenDiscipline_Object=MibTableColumn
qosIfQueueGenDiscipline=_QosIfQueueGenDiscipline_Object((1,3,6,1,4,1,45,4,2,1,1,2,1,4),_QosIfQueueGenDiscipline_Type())
qosIfQueueGenDiscipline.setMaxAccess(_C)
if mibBuilder.loadTexts:qosIfQueueGenDiscipline.setStatus(_A)
_QosIfQueueExtDiscipline_Type=ObjectIdentifier
_QosIfQueueExtDiscipline_Object=MibTableColumn
qosIfQueueExtDiscipline=_QosIfQueueExtDiscipline_Object((1,3,6,1,4,1,45,4,2,1,1,2,1,5),_QosIfQueueExtDiscipline_Type())
qosIfQueueExtDiscipline.setMaxAccess(_C)
if mibBuilder.loadTexts:qosIfQueueExtDiscipline.setStatus(_A)
_QosIfQueueDrainSize_Type=Unsigned32
_QosIfQueueDrainSize_Object=MibTableColumn
qosIfQueueDrainSize=_QosIfQueueDrainSize_Object((1,3,6,1,4,1,45,4,2,1,1,2,1,6),_QosIfQueueDrainSize_Type())
qosIfQueueDrainSize.setMaxAccess(_C)
if mibBuilder.loadTexts:qosIfQueueDrainSize.setStatus(_A)
_QosIfQueueAbsBandwidth_Type=Unsigned32
_QosIfQueueAbsBandwidth_Object=MibTableColumn
qosIfQueueAbsBandwidth=_QosIfQueueAbsBandwidth_Object((1,3,6,1,4,1,45,4,2,1,1,2,1,7),_QosIfQueueAbsBandwidth_Type())
qosIfQueueAbsBandwidth.setMaxAccess(_C)
if mibBuilder.loadTexts:qosIfQueueAbsBandwidth.setStatus(_A)
class _QosIfQueueBandwidthAllocation_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('absolute',1),('relative',2)))
_QosIfQueueBandwidthAllocation_Type.__name__=_D
_QosIfQueueBandwidthAllocation_Object=MibTableColumn
qosIfQueueBandwidthAllocation=_QosIfQueueBandwidthAllocation_Object((1,3,6,1,4,1,45,4,2,1,1,2,1,8),_QosIfQueueBandwidthAllocation_Type())
qosIfQueueBandwidthAllocation.setMaxAccess(_C)
if mibBuilder.loadTexts:qosIfQueueBandwidthAllocation.setStatus(_A)
_QosIfQueueServiceOrder_Type=QosInterfaceQueueCount
_QosIfQueueServiceOrder_Object=MibTableColumn
qosIfQueueServiceOrder=_QosIfQueueServiceOrder_Object((1,3,6,1,4,1,45,4,2,1,1,2,1,9),_QosIfQueueServiceOrder_Type())
qosIfQueueServiceOrder.setMaxAccess(_C)
if mibBuilder.loadTexts:qosIfQueueServiceOrder.setStatus(_A)
_QosIfQueueSize_Type=Integer32
_QosIfQueueSize_Object=MibTableColumn
qosIfQueueSize=_QosIfQueueSize_Object((1,3,6,1,4,1,45,4,2,1,1,2,1,10),_QosIfQueueSize_Type())
qosIfQueueSize.setMaxAccess(_C)
if mibBuilder.loadTexts:qosIfQueueSize.setStatus(_A)
class _QosIfQueueStorageType_Type(StorageType):defaultValue=2
_QosIfQueueStorageType_Type.__name__=_E
_QosIfQueueStorageType_Object=MibTableColumn
qosIfQueueStorageType=_QosIfQueueStorageType_Object((1,3,6,1,4,1,45,4,2,1,1,2,1,11),_QosIfQueueStorageType_Type())
qosIfQueueStorageType.setMaxAccess(_C)
if mibBuilder.loadTexts:qosIfQueueStorageType.setStatus(_A)
_QosIfQueueStatus_Type=RowStatus
_QosIfQueueStatus_Object=MibTableColumn
qosIfQueueStatus=_QosIfQueueStatus_Object((1,3,6,1,4,1,45,4,2,1,1,2,1,12),_QosIfQueueStatus_Type())
qosIfQueueStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:qosIfQueueStatus.setStatus(_A)
_QosIfDscpAssignmentTable_Object=MibTable
qosIfDscpAssignmentTable=_QosIfDscpAssignmentTable_Object((1,3,6,1,4,1,45,4,2,1,1,3))
if mibBuilder.loadTexts:qosIfDscpAssignmentTable.setStatus(_A)
_QosIfDscpAssignmentEntry_Object=MibTableRow
qosIfDscpAssignmentEntry=_QosIfDscpAssignmentEntry_Object((1,3,6,1,4,1,45,4,2,1,1,3,1))
qosIfDscpAssignmentEntry.setIndexNames((0,_B,_L))
if mibBuilder.loadTexts:qosIfDscpAssignmentEntry.setStatus(_A)
_QosIfDscpAssignmentId_Type=PolicyInstanceId
_QosIfDscpAssignmentId_Object=MibTableColumn
qosIfDscpAssignmentId=_QosIfDscpAssignmentId_Object((1,3,6,1,4,1,45,4,2,1,1,3,1,1),_QosIfDscpAssignmentId_Type())
qosIfDscpAssignmentId.setMaxAccess(_F)
if mibBuilder.loadTexts:qosIfDscpAssignmentId.setStatus(_A)
_QosIfDscpAssignmentRoles_Type=RoleCombination
_QosIfDscpAssignmentRoles_Object=MibTableColumn
qosIfDscpAssignmentRoles=_QosIfDscpAssignmentRoles_Object((1,3,6,1,4,1,45,4,2,1,1,3,1,2),_QosIfDscpAssignmentRoles_Type())
qosIfDscpAssignmentRoles.setMaxAccess(_C)
if mibBuilder.loadTexts:qosIfDscpAssignmentRoles.setStatus(_A)
_QosIfDscpAssignmentDscp_Type=Dscp
_QosIfDscpAssignmentDscp_Object=MibTableColumn
qosIfDscpAssignmentDscp=_QosIfDscpAssignmentDscp_Object((1,3,6,1,4,1,45,4,2,1,1,3,1,3),_QosIfDscpAssignmentDscp_Type())
qosIfDscpAssignmentDscp.setMaxAccess(_C)
if mibBuilder.loadTexts:qosIfDscpAssignmentDscp.setStatus(_A)
_QosIfDscpAssignmentQueue_Type=QosInterfaceQueueCount
_QosIfDscpAssignmentQueue_Object=MibTableColumn
qosIfDscpAssignmentQueue=_QosIfDscpAssignmentQueue_Object((1,3,6,1,4,1,45,4,2,1,1,3,1,4),_QosIfDscpAssignmentQueue_Type())
qosIfDscpAssignmentQueue.setMaxAccess(_C)
if mibBuilder.loadTexts:qosIfDscpAssignmentQueue.setStatus(_A)
class _QosIfDscpAssignmentStorageType_Type(StorageType):defaultValue=2
_QosIfDscpAssignmentStorageType_Type.__name__=_E
_QosIfDscpAssignmentStorageType_Object=MibTableColumn
qosIfDscpAssignmentStorageType=_QosIfDscpAssignmentStorageType_Object((1,3,6,1,4,1,45,4,2,1,1,3,1,5),_QosIfDscpAssignmentStorageType_Type())
qosIfDscpAssignmentStorageType.setMaxAccess(_C)
if mibBuilder.loadTexts:qosIfDscpAssignmentStorageType.setStatus(_A)
_QosIfDscpAssignmentStatus_Type=RowStatus
_QosIfDscpAssignmentStatus_Object=MibTableColumn
qosIfDscpAssignmentStatus=_QosIfDscpAssignmentStatus_Object((1,3,6,1,4,1,45,4,2,1,1,3,1,6),_QosIfDscpAssignmentStatus_Type())
qosIfDscpAssignmentStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:qosIfDscpAssignmentStatus.setStatus(_A)
_QosMeter_ObjectIdentity=ObjectIdentity
qosMeter=_QosMeter_ObjectIdentity((1,3,6,1,4,1,45,4,2,1,2))
_QosMeterTable_Object=MibTable
qosMeterTable=_QosMeterTable_Object((1,3,6,1,4,1,45,4,2,1,2,1))
if mibBuilder.loadTexts:qosMeterTable.setStatus(_A)
_QosMeterEntry_Object=MibTableRow
qosMeterEntry=_QosMeterEntry_Object((1,3,6,1,4,1,45,4,2,1,2,1,1))
qosMeterEntry.setIndexNames((0,_B,_M))
if mibBuilder.loadTexts:qosMeterEntry.setStatus(_A)
_QosMeterId_Type=PolicyInstanceId
_QosMeterId_Object=MibTableColumn
qosMeterId=_QosMeterId_Object((1,3,6,1,4,1,45,4,2,1,2,1,1,1),_QosMeterId_Type())
qosMeterId.setMaxAccess(_F)
if mibBuilder.loadTexts:qosMeterId.setStatus(_A)
class _QosMeterDataSpecification_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('noMeterData',1),('committedData',2),('peakData',3),('committedRestricted',4)))
_QosMeterDataSpecification_Type.__name__=_D
_QosMeterDataSpecification_Object=MibTableColumn
qosMeterDataSpecification=_QosMeterDataSpecification_Object((1,3,6,1,4,1,45,4,2,1,2,1,1,2),_QosMeterDataSpecification_Type())
qosMeterDataSpecification.setMaxAccess(_C)
if mibBuilder.loadTexts:qosMeterDataSpecification.setStatus(_A)
class _QosMeterCommittedRate_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_QosMeterCommittedRate_Type.__name__=_G
_QosMeterCommittedRate_Object=MibTableColumn
qosMeterCommittedRate=_QosMeterCommittedRate_Object((1,3,6,1,4,1,45,4,2,1,2,1,1,3),_QosMeterCommittedRate_Type())
qosMeterCommittedRate.setMaxAccess(_C)
if mibBuilder.loadTexts:qosMeterCommittedRate.setStatus(_A)
class _QosMeterCommittedBurst_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_QosMeterCommittedBurst_Type.__name__=_G
_QosMeterCommittedBurst_Object=MibTableColumn
qosMeterCommittedBurst=_QosMeterCommittedBurst_Object((1,3,6,1,4,1,45,4,2,1,2,1,1,4),_QosMeterCommittedBurst_Type())
qosMeterCommittedBurst.setMaxAccess(_C)
if mibBuilder.loadTexts:qosMeterCommittedBurst.setStatus(_A)
class _QosMeterPeakRate_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_QosMeterPeakRate_Type.__name__=_G
_QosMeterPeakRate_Object=MibTableColumn
qosMeterPeakRate=_QosMeterPeakRate_Object((1,3,6,1,4,1,45,4,2,1,2,1,1,5),_QosMeterPeakRate_Type())
qosMeterPeakRate.setMaxAccess(_C)
if mibBuilder.loadTexts:qosMeterPeakRate.setStatus(_A)
class _QosMeterPeakBurst_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_QosMeterPeakBurst_Type.__name__=_G
_QosMeterPeakBurst_Object=MibTableColumn
qosMeterPeakBurst=_QosMeterPeakBurst_Object((1,3,6,1,4,1,45,4,2,1,2,1,1,6),_QosMeterPeakBurst_Type())
qosMeterPeakBurst.setMaxAccess(_C)
if mibBuilder.loadTexts:qosMeterPeakBurst.setStatus(_A)
_QosMeterHighConfAction_Type=PolicyInstanceIdOrZero
_QosMeterHighConfAction_Object=MibTableColumn
qosMeterHighConfAction=_QosMeterHighConfAction_Object((1,3,6,1,4,1,45,4,2,1,2,1,1,7),_QosMeterHighConfAction_Type())
qosMeterHighConfAction.setMaxAccess(_C)
if mibBuilder.loadTexts:qosMeterHighConfAction.setStatus(_A)
_QosMeterMedConfAction_Type=PolicyInstanceIdOrZero
_QosMeterMedConfAction_Object=MibTableColumn
qosMeterMedConfAction=_QosMeterMedConfAction_Object((1,3,6,1,4,1,45,4,2,1,2,1,1,8),_QosMeterMedConfAction_Type())
qosMeterMedConfAction.setMaxAccess(_C)
if mibBuilder.loadTexts:qosMeterMedConfAction.setStatus(_A)
_QosMeterLowConfAction_Type=PolicyInstanceIdOrZero
_QosMeterLowConfAction_Object=MibTableColumn
qosMeterLowConfAction=_QosMeterLowConfAction_Object((1,3,6,1,4,1,45,4,2,1,2,1,1,9),_QosMeterLowConfAction_Type())
qosMeterLowConfAction.setMaxAccess(_C)
if mibBuilder.loadTexts:qosMeterLowConfAction.setStatus(_A)
class _QosMeterStorageType_Type(StorageType):defaultValue=2
_QosMeterStorageType_Type.__name__=_E
_QosMeterStorageType_Object=MibTableColumn
qosMeterStorageType=_QosMeterStorageType_Object((1,3,6,1,4,1,45,4,2,1,2,1,1,10),_QosMeterStorageType_Type())
qosMeterStorageType.setMaxAccess(_C)
if mibBuilder.loadTexts:qosMeterStorageType.setStatus(_A)
_QosMeterStatus_Type=RowStatus
_QosMeterStatus_Object=MibTableColumn
qosMeterStatus=_QosMeterStatus_Object((1,3,6,1,4,1,45,4,2,1,2,1,1,11),_QosMeterStatus_Type())
qosMeterStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:qosMeterStatus.setStatus(_A)
class _QosMeterLabel_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_QosMeterLabel_Type.__name__=_H
_QosMeterLabel_Object=MibTableColumn
qosMeterLabel=_QosMeterLabel_Object((1,3,6,1,4,1,45,4,2,1,2,1,1,12),_QosMeterLabel_Type())
qosMeterLabel.setMaxAccess(_C)
if mibBuilder.loadTexts:qosMeterLabel.setStatus(_A)
_QosAction_ObjectIdentity=ObjectIdentity
qosAction=_QosAction_ObjectIdentity((1,3,6,1,4,1,45,4,2,1,3))
_QosActionTable_Object=MibTable
qosActionTable=_QosActionTable_Object((1,3,6,1,4,1,45,4,2,1,3,1))
if mibBuilder.loadTexts:qosActionTable.setStatus(_A)
_QosActionEntry_Object=MibTableRow
qosActionEntry=_QosActionEntry_Object((1,3,6,1,4,1,45,4,2,1,3,1,1))
qosActionEntry.setIndexNames((0,_B,_N))
if mibBuilder.loadTexts:qosActionEntry.setStatus(_A)
_QosActionId_Type=PolicyInstanceId
_QosActionId_Object=MibTableColumn
qosActionId=_QosActionId_Object((1,3,6,1,4,1,45,4,2,1,3,1,1,1),_QosActionId_Type())
qosActionId.setMaxAccess(_F)
if mibBuilder.loadTexts:qosActionId.setStatus(_A)
_QosActionDrop_Type=TruthValue
_QosActionDrop_Object=MibTableColumn
qosActionDrop=_QosActionDrop_Object((1,3,6,1,4,1,45,4,2,1,3,1,1,2),_QosActionDrop_Type())
qosActionDrop.setMaxAccess(_C)
if mibBuilder.loadTexts:qosActionDrop.setStatus(_A)
class _QosActionUpdateDSCP_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,-1),ValueRangeConstraint(0,63))
_QosActionUpdateDSCP_Type.__name__=_D
_QosActionUpdateDSCP_Object=MibTableColumn
qosActionUpdateDSCP=_QosActionUpdateDSCP_Object((1,3,6,1,4,1,45,4,2,1,3,1,1,3),_QosActionUpdateDSCP_Type())
qosActionUpdateDSCP.setMaxAccess(_C)
if mibBuilder.loadTexts:qosActionUpdateDSCP.setStatus(_A)
_QosActionMeter_Type=PolicyInstanceId
_QosActionMeter_Object=MibTableColumn
qosActionMeter=_QosActionMeter_Object((1,3,6,1,4,1,45,4,2,1,3,1,1,4),_QosActionMeter_Type())
qosActionMeter.setMaxAccess(_C)
if mibBuilder.loadTexts:qosActionMeter.setStatus(_A)
class _QosActionStorageType_Type(StorageType):defaultValue=2
_QosActionStorageType_Type.__name__=_E
_QosActionStorageType_Object=MibTableColumn
qosActionStorageType=_QosActionStorageType_Object((1,3,6,1,4,1,45,4,2,1,3,1,1,5),_QosActionStorageType_Type())
qosActionStorageType.setMaxAccess(_C)
if mibBuilder.loadTexts:qosActionStorageType.setStatus(_A)
_QosActionStatus_Type=RowStatus
_QosActionStatus_Object=MibTableColumn
qosActionStatus=_QosActionStatus_Object((1,3,6,1,4,1,45,4,2,1,3,1,1,6),_QosActionStatus_Type())
qosActionStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:qosActionStatus.setStatus(_A)
class _QosActionLabel_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_QosActionLabel_Type.__name__=_H
_QosActionLabel_Object=MibTableColumn
qosActionLabel=_QosActionLabel_Object((1,3,6,1,4,1,45,4,2,1,3,1,1,7),_QosActionLabel_Type())
qosActionLabel.setMaxAccess(_C)
if mibBuilder.loadTexts:qosActionLabel.setStatus(_A)
_QosTargetTable_Object=MibTable
qosTargetTable=_QosTargetTable_Object((1,3,6,1,4,1,45,4,2,1,3,2))
if mibBuilder.loadTexts:qosTargetTable.setStatus(_A)
_QosTargetEntry_Object=MibTableRow
qosTargetEntry=_QosTargetEntry_Object((1,3,6,1,4,1,45,4,2,1,3,2,1))
qosTargetEntry.setIndexNames((0,_B,_O))
if mibBuilder.loadTexts:qosTargetEntry.setStatus(_A)
_QosTargetId_Type=PolicyInstanceId
_QosTargetId_Object=MibTableColumn
qosTargetId=_QosTargetId_Object((1,3,6,1,4,1,45,4,2,1,3,2,1,1),_QosTargetId_Type())
qosTargetId.setMaxAccess(_F)
if mibBuilder.loadTexts:qosTargetId.setStatus(_A)
_QosTargetAclId_Type=PolicyInstanceId
_QosTargetAclId_Object=MibTableColumn
qosTargetAclId=_QosTargetAclId_Object((1,3,6,1,4,1,45,4,2,1,3,2,1,2),_QosTargetAclId_Type())
qosTargetAclId.setMaxAccess(_C)
if mibBuilder.loadTexts:qosTargetAclId.setStatus(_A)
_QosTargetAclType_Type=ObjectIdentifier
_QosTargetAclType_Object=MibTableColumn
qosTargetAclType=_QosTargetAclType_Object((1,3,6,1,4,1,45,4,2,1,3,2,1,3),_QosTargetAclType_Type())
qosTargetAclType.setMaxAccess(_C)
if mibBuilder.loadTexts:qosTargetAclType.setStatus(_A)
_QosTargetInterfaceRoles_Type=RoleCombination
_QosTargetInterfaceRoles_Object=MibTableColumn
qosTargetInterfaceRoles=_QosTargetInterfaceRoles_Object((1,3,6,1,4,1,45,4,2,1,3,2,1,4),_QosTargetInterfaceRoles_Type())
qosTargetInterfaceRoles.setMaxAccess(_C)
if mibBuilder.loadTexts:qosTargetInterfaceRoles.setStatus(_A)
class _QosTargetInterfaceDirection_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('in',1),('out',2)))
_QosTargetInterfaceDirection_Type.__name__=_D
_QosTargetInterfaceDirection_Object=MibTableColumn
qosTargetInterfaceDirection=_QosTargetInterfaceDirection_Object((1,3,6,1,4,1,45,4,2,1,3,2,1,5),_QosTargetInterfaceDirection_Type())
qosTargetInterfaceDirection.setMaxAccess(_C)
if mibBuilder.loadTexts:qosTargetInterfaceDirection.setStatus(_A)
_QosTargetOrder_Type=Unsigned32
_QosTargetOrder_Object=MibTableColumn
qosTargetOrder=_QosTargetOrder_Object((1,3,6,1,4,1,45,4,2,1,3,2,1,6),_QosTargetOrder_Type())
qosTargetOrder.setMaxAccess(_C)
if mibBuilder.loadTexts:qosTargetOrder.setStatus(_A)
_QosTargetMeter_Type=PolicyInstanceIdOrZero
_QosTargetMeter_Object=MibTableColumn
qosTargetMeter=_QosTargetMeter_Object((1,3,6,1,4,1,45,4,2,1,3,2,1,7),_QosTargetMeter_Type())
qosTargetMeter.setMaxAccess(_C)
if mibBuilder.loadTexts:qosTargetMeter.setStatus(_A)
class _QosTargetStorageType_Type(StorageType):defaultValue=2
_QosTargetStorageType_Type.__name__=_E
_QosTargetStorageType_Object=MibTableColumn
qosTargetStorageType=_QosTargetStorageType_Object((1,3,6,1,4,1,45,4,2,1,3,2,1,8),_QosTargetStorageType_Type())
qosTargetStorageType.setMaxAccess(_C)
if mibBuilder.loadTexts:qosTargetStorageType.setStatus(_A)
_QosTargetStatus_Type=RowStatus
_QosTargetStatus_Object=MibTableColumn
qosTargetStatus=_QosTargetStatus_Object((1,3,6,1,4,1,45,4,2,1,3,2,1,9),_QosTargetStatus_Type())
qosTargetStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:qosTargetStatus.setStatus(_A)
class _QosTargetShapingParams_Type(PolicyInstanceIdOrZero):defaultValue=0
_QosTargetShapingParams_Type.__name__=_I
_QosTargetShapingParams_Object=MibTableColumn
qosTargetShapingParams=_QosTargetShapingParams_Object((1,3,6,1,4,1,45,4,2,1,3,2,1,10),_QosTargetShapingParams_Type())
qosTargetShapingParams.setMaxAccess(_C)
if mibBuilder.loadTexts:qosTargetShapingParams.setStatus(_A)
class _QosTargetShapingGroup_Type(Unsigned32):defaultValue=0
_QosTargetShapingGroup_Type.__name__=_G
_QosTargetShapingGroup_Object=MibTableColumn
qosTargetShapingGroup=_QosTargetShapingGroup_Object((1,3,6,1,4,1,45,4,2,1,3,2,1,11),_QosTargetShapingGroup_Type())
qosTargetShapingGroup.setMaxAccess(_C)
if mibBuilder.loadTexts:qosTargetShapingGroup.setStatus(_A)
class _QosTargetLabel_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_QosTargetLabel_Type.__name__=_H
_QosTargetLabel_Object=MibTableColumn
qosTargetLabel=_QosTargetLabel_Object((1,3,6,1,4,1,45,4,2,1,3,2,1,12),_QosTargetLabel_Type())
qosTargetLabel.setMaxAccess(_C)
if mibBuilder.loadTexts:qosTargetLabel.setStatus(_A)
class _QosTargetInProfileAction_Type(PolicyInstanceIdOrZero):defaultValue=0
_QosTargetInProfileAction_Type.__name__=_I
_QosTargetInProfileAction_Object=MibTableColumn
qosTargetInProfileAction=_QosTargetInProfileAction_Object((1,3,6,1,4,1,45,4,2,1,3,2,1,13),_QosTargetInProfileAction_Type())
qosTargetInProfileAction.setMaxAccess(_C)
if mibBuilder.loadTexts:qosTargetInProfileAction.setStatus(_A)
class _QosTargetOutOfProfileAction_Type(PolicyInstanceIdOrZero):defaultValue=0
_QosTargetOutOfProfileAction_Type.__name__=_I
_QosTargetOutOfProfileAction_Object=MibTableColumn
qosTargetOutOfProfileAction=_QosTargetOutOfProfileAction_Object((1,3,6,1,4,1,45,4,2,1,3,2,1,14),_QosTargetOutOfProfileAction_Type())
qosTargetOutOfProfileAction.setMaxAccess(_C)
if mibBuilder.loadTexts:qosTargetOutOfProfileAction.setStatus(_A)
class _QosTargetUserGroupSession_Type(Unsigned32):defaultValue=0
_QosTargetUserGroupSession_Type.__name__=_G
_QosTargetUserGroupSession_Object=MibTableColumn
qosTargetUserGroupSession=_QosTargetUserGroupSession_Object((1,3,6,1,4,1,45,4,2,1,3,2,1,15),_QosTargetUserGroupSession_Type())
qosTargetUserGroupSession.setMaxAccess(_C)
if mibBuilder.loadTexts:qosTargetUserGroupSession.setStatus(_A)
_QosPolicyIpPibClasses_ObjectIdentity=ObjectIdentity
qosPolicyIpPibClasses=_QosPolicyIpPibClasses_ObjectIdentity((1,3,6,1,4,1,45,4,2,2))
_QosIpQos_ObjectIdentity=ObjectIdentity
qosIpQos=_QosIpQos_ObjectIdentity((1,3,6,1,4,1,45,4,2,2,1))
_QosIpAceTable_Object=MibTable
qosIpAceTable=_QosIpAceTable_Object((1,3,6,1,4,1,45,4,2,2,1,1))
if mibBuilder.loadTexts:qosIpAceTable.setStatus(_A)
_QosIpAceEntry_Object=MibTableRow
qosIpAceEntry=_QosIpAceEntry_Object((1,3,6,1,4,1,45,4,2,2,1,1,1))
qosIpAceEntry.setIndexNames((0,_B,_P))
if mibBuilder.loadTexts:qosIpAceEntry.setStatus(_A)
_QosIpAceId_Type=PolicyInstanceId
_QosIpAceId_Object=MibTableColumn
qosIpAceId=_QosIpAceId_Object((1,3,6,1,4,1,45,4,2,2,1,1,1,1),_QosIpAceId_Type())
qosIpAceId.setMaxAccess(_F)
if mibBuilder.loadTexts:qosIpAceId.setStatus(_A)
_QosIpAceDstAddr_Type=IpAddress
_QosIpAceDstAddr_Object=MibTableColumn
qosIpAceDstAddr=_QosIpAceDstAddr_Object((1,3,6,1,4,1,45,4,2,2,1,1,1,2),_QosIpAceDstAddr_Type())
qosIpAceDstAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:qosIpAceDstAddr.setStatus(_A)
_QosIpAceDstAddrMask_Type=IpAddress
_QosIpAceDstAddrMask_Object=MibTableColumn
qosIpAceDstAddrMask=_QosIpAceDstAddrMask_Object((1,3,6,1,4,1,45,4,2,2,1,1,1,3),_QosIpAceDstAddrMask_Type())
qosIpAceDstAddrMask.setMaxAccess(_C)
if mibBuilder.loadTexts:qosIpAceDstAddrMask.setStatus(_A)
_QosIpAceSrcAddr_Type=IpAddress
_QosIpAceSrcAddr_Object=MibTableColumn
qosIpAceSrcAddr=_QosIpAceSrcAddr_Object((1,3,6,1,4,1,45,4,2,2,1,1,1,4),_QosIpAceSrcAddr_Type())
qosIpAceSrcAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:qosIpAceSrcAddr.setStatus(_A)
_QosIpAceSrcAddrMask_Type=IpAddress
_QosIpAceSrcAddrMask_Object=MibTableColumn
qosIpAceSrcAddrMask=_QosIpAceSrcAddrMask_Object((1,3,6,1,4,1,45,4,2,2,1,1,1,5),_QosIpAceSrcAddrMask_Type())
qosIpAceSrcAddrMask.setMaxAccess(_C)
if mibBuilder.loadTexts:qosIpAceSrcAddrMask.setStatus(_A)
class _QosIpAceDscp_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,-1),ValueRangeConstraint(0,63))
_QosIpAceDscp_Type.__name__=_D
_QosIpAceDscp_Object=MibTableColumn
qosIpAceDscp=_QosIpAceDscp_Object((1,3,6,1,4,1,45,4,2,2,1,1,1,6),_QosIpAceDscp_Type())
qosIpAceDscp.setMaxAccess(_C)
if mibBuilder.loadTexts:qosIpAceDscp.setStatus(_A)
class _QosIpAceProtocol_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_QosIpAceProtocol_Type.__name__=_D
_QosIpAceProtocol_Object=MibTableColumn
qosIpAceProtocol=_QosIpAceProtocol_Object((1,3,6,1,4,1,45,4,2,2,1,1,1,7),_QosIpAceProtocol_Type())
qosIpAceProtocol.setMaxAccess(_C)
if mibBuilder.loadTexts:qosIpAceProtocol.setStatus(_A)
class _QosIpAceDstL4PortMin_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_QosIpAceDstL4PortMin_Type.__name__=_D
_QosIpAceDstL4PortMin_Object=MibTableColumn
qosIpAceDstL4PortMin=_QosIpAceDstL4PortMin_Object((1,3,6,1,4,1,45,4,2,2,1,1,1,8),_QosIpAceDstL4PortMin_Type())
qosIpAceDstL4PortMin.setMaxAccess(_C)
if mibBuilder.loadTexts:qosIpAceDstL4PortMin.setStatus(_A)
class _QosIpAceDstL4PortMax_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_QosIpAceDstL4PortMax_Type.__name__=_D
_QosIpAceDstL4PortMax_Object=MibTableColumn
qosIpAceDstL4PortMax=_QosIpAceDstL4PortMax_Object((1,3,6,1,4,1,45,4,2,2,1,1,1,9),_QosIpAceDstL4PortMax_Type())
qosIpAceDstL4PortMax.setMaxAccess(_C)
if mibBuilder.loadTexts:qosIpAceDstL4PortMax.setStatus(_A)
class _QosIpAceSrcL4PortMin_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_QosIpAceSrcL4PortMin_Type.__name__=_D
_QosIpAceSrcL4PortMin_Object=MibTableColumn
qosIpAceSrcL4PortMin=_QosIpAceSrcL4PortMin_Object((1,3,6,1,4,1,45,4,2,2,1,1,1,10),_QosIpAceSrcL4PortMin_Type())
qosIpAceSrcL4PortMin.setMaxAccess(_C)
if mibBuilder.loadTexts:qosIpAceSrcL4PortMin.setStatus(_A)
class _QosIpAceSrcL4PortMax_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_QosIpAceSrcL4PortMax_Type.__name__=_D
_QosIpAceSrcL4PortMax_Object=MibTableColumn
qosIpAceSrcL4PortMax=_QosIpAceSrcL4PortMax_Object((1,3,6,1,4,1,45,4,2,2,1,1,1,11),_QosIpAceSrcL4PortMax_Type())
qosIpAceSrcL4PortMax.setMaxAccess(_C)
if mibBuilder.loadTexts:qosIpAceSrcL4PortMax.setStatus(_A)
_QosIpAcePermit_Type=TruthValue
_QosIpAcePermit_Object=MibTableColumn
qosIpAcePermit=_QosIpAcePermit_Object((1,3,6,1,4,1,45,4,2,2,1,1,1,12),_QosIpAcePermit_Type())
qosIpAcePermit.setMaxAccess(_C)
if mibBuilder.loadTexts:qosIpAcePermit.setStatus(_A)
class _QosIpAceStorageType_Type(StorageType):defaultValue=2
_QosIpAceStorageType_Type.__name__=_E
_QosIpAceStorageType_Object=MibTableColumn
qosIpAceStorageType=_QosIpAceStorageType_Object((1,3,6,1,4,1,45,4,2,2,1,1,1,13),_QosIpAceStorageType_Type())
qosIpAceStorageType.setMaxAccess(_C)
if mibBuilder.loadTexts:qosIpAceStorageType.setStatus(_A)
_QosIpAceStatus_Type=RowStatus
_QosIpAceStatus_Object=MibTableColumn
qosIpAceStatus=_QosIpAceStatus_Object((1,3,6,1,4,1,45,4,2,2,1,1,1,14),_QosIpAceStatus_Type())
qosIpAceStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:qosIpAceStatus.setStatus(_A)
_QosIpAclDefinitionTable_Object=MibTable
qosIpAclDefinitionTable=_QosIpAclDefinitionTable_Object((1,3,6,1,4,1,45,4,2,2,1,2))
if mibBuilder.loadTexts:qosIpAclDefinitionTable.setStatus(_A)
_QosIpAclDefinitionEntry_Object=MibTableRow
qosIpAclDefinitionEntry=_QosIpAclDefinitionEntry_Object((1,3,6,1,4,1,45,4,2,2,1,2,1))
qosIpAclDefinitionEntry.setIndexNames((0,_B,_Q))
if mibBuilder.loadTexts:qosIpAclDefinitionEntry.setStatus(_A)
_QosIpAclDefinitionId_Type=PolicyInstanceId
_QosIpAclDefinitionId_Object=MibTableColumn
qosIpAclDefinitionId=_QosIpAclDefinitionId_Object((1,3,6,1,4,1,45,4,2,2,1,2,1,1),_QosIpAclDefinitionId_Type())
qosIpAclDefinitionId.setMaxAccess(_F)
if mibBuilder.loadTexts:qosIpAclDefinitionId.setStatus(_A)
_QosIpAclDefinitionAclId_Type=PolicyInstanceId
_QosIpAclDefinitionAclId_Object=MibTableColumn
qosIpAclDefinitionAclId=_QosIpAclDefinitionAclId_Object((1,3,6,1,4,1,45,4,2,2,1,2,1,2),_QosIpAclDefinitionAclId_Type())
qosIpAclDefinitionAclId.setMaxAccess(_C)
if mibBuilder.loadTexts:qosIpAclDefinitionAclId.setStatus(_A)
_QosIpAclDefinitionAceId_Type=PolicyInstanceId
_QosIpAclDefinitionAceId_Object=MibTableColumn
qosIpAclDefinitionAceId=_QosIpAclDefinitionAceId_Object((1,3,6,1,4,1,45,4,2,2,1,2,1,3),_QosIpAclDefinitionAceId_Type())
qosIpAclDefinitionAceId.setMaxAccess(_C)
if mibBuilder.loadTexts:qosIpAclDefinitionAceId.setStatus(_A)
_QosIpAclDefinitionAceOrder_Type=Unsigned32
_QosIpAclDefinitionAceOrder_Object=MibTableColumn
qosIpAclDefinitionAceOrder=_QosIpAclDefinitionAceOrder_Object((1,3,6,1,4,1,45,4,2,2,1,2,1,4),_QosIpAclDefinitionAceOrder_Type())
qosIpAclDefinitionAceOrder.setMaxAccess(_C)
if mibBuilder.loadTexts:qosIpAclDefinitionAceOrder.setStatus(_A)
class _QosIpAclDefinitionStorageType_Type(StorageType):defaultValue=2
_QosIpAclDefinitionStorageType_Type.__name__=_E
_QosIpAclDefinitionStorageType_Object=MibTableColumn
qosIpAclDefinitionStorageType=_QosIpAclDefinitionStorageType_Object((1,3,6,1,4,1,45,4,2,2,1,2,1,5),_QosIpAclDefinitionStorageType_Type())
qosIpAclDefinitionStorageType.setMaxAccess(_C)
if mibBuilder.loadTexts:qosIpAclDefinitionStorageType.setStatus(_A)
_QosIpAclDefinitionStatus_Type=RowStatus
_QosIpAclDefinitionStatus_Object=MibTableColumn
qosIpAclDefinitionStatus=_QosIpAclDefinitionStatus_Object((1,3,6,1,4,1,45,4,2,2,1,2,1,6),_QosIpAclDefinitionStatus_Type())
qosIpAclDefinitionStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:qosIpAclDefinitionStatus.setStatus(_A)
class _QosIpAclDefinitionLabel_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_QosIpAclDefinitionLabel_Type.__name__=_H
_QosIpAclDefinitionLabel_Object=MibTableColumn
qosIpAclDefinitionLabel=_QosIpAclDefinitionLabel_Object((1,3,6,1,4,1,45,4,2,2,1,2,1,7),_QosIpAclDefinitionLabel_Type())
qosIpAclDefinitionLabel.setMaxAccess(_C)
if mibBuilder.loadTexts:qosIpAclDefinitionLabel.setStatus(_A)
_QosPolicyIpPibConformance_ObjectIdentity=ObjectIdentity
qosPolicyIpPibConformance=_QosPolicyIpPibConformance_ObjectIdentity((1,3,6,1,4,1,45,4,2,3))
_QosPolicyIpPibCompliances_ObjectIdentity=ObjectIdentity
qosPolicyIpPibCompliances=_QosPolicyIpPibCompliances_ObjectIdentity((1,3,6,1,4,1,45,4,2,3,1))
_QosPolicyIpPibGroups_ObjectIdentity=ObjectIdentity
qosPolicyIpPibGroups=_QosPolicyIpPibGroups_ObjectIdentity((1,3,6,1,4,1,45,4,2,3,2))
qosInterfaceTypeGroup=ObjectGroup((1,3,6,1,4,1,45,4,2,3,2,1))
qosInterfaceTypeGroup.setObjects(*((_B,_R),(_B,_S),(_B,_T),(_B,_U),(_B,_V)))
if mibBuilder.loadTexts:qosInterfaceTypeGroup.setStatus(_A)
qosIfQueueGroup=ObjectGroup((1,3,6,1,4,1,45,4,2,3,2,2))
qosIfQueueGroup.setObjects(*((_B,_W),(_B,_X),(_B,_Y),(_B,_Z),(_B,_a),(_B,_b),(_B,_c),(_B,_d),(_B,_e),(_B,_f),(_B,_g)))
if mibBuilder.loadTexts:qosIfQueueGroup.setStatus(_A)
qosIfDscpAssignmentGroup=ObjectGroup((1,3,6,1,4,1,45,4,2,3,2,3))
qosIfDscpAssignmentGroup.setObjects(*((_B,_h),(_B,_i),(_B,_j),(_B,_k),(_B,_l)))
if mibBuilder.loadTexts:qosIfDscpAssignmentGroup.setStatus(_A)
qosMeterGroup=ObjectGroup((1,3,6,1,4,1,45,4,2,3,2,4))
qosMeterGroup.setObjects(*((_B,_m),(_B,_n),(_B,_o),(_B,_p),(_B,_q),(_B,_r),(_B,_s),(_B,_t),(_B,_u),(_B,_v),(_B,_w)))
if mibBuilder.loadTexts:qosMeterGroup.setStatus(_A)
qosActionGroup=ObjectGroup((1,3,6,1,4,1,45,4,2,3,2,5))
qosActionGroup.setObjects(*((_B,_x),(_B,_y),(_B,_z),(_B,_A0),(_B,_A1),(_B,_A2)))
if mibBuilder.loadTexts:qosActionGroup.setStatus(_A)
qosTargetGroup=ObjectGroup((1,3,6,1,4,1,45,4,2,3,2,6))
qosTargetGroup.setObjects(*((_B,_A3),(_B,_A4),(_B,_A5),(_B,_A6),(_B,_A7),(_B,_A8),(_B,_A9),(_B,_AA),(_B,_AB),(_B,_AC),(_B,_AD),(_B,_AE),(_B,_AF),(_B,_AG)))
if mibBuilder.loadTexts:qosTargetGroup.setStatus(_A)
qosIpAceGroup=ObjectGroup((1,3,6,1,4,1,45,4,2,3,2,7))
qosIpAceGroup.setObjects(*((_B,_AH),(_B,_AI),(_B,_AJ),(_B,_AK),(_B,_AL),(_B,_AM),(_B,_AN),(_B,_AO),(_B,_AP),(_B,_AQ),(_B,_AR),(_B,_AS),(_B,_AT)))
if mibBuilder.loadTexts:qosIpAceGroup.setStatus(_A)
qosIpAclDefinitionGroup=ObjectGroup((1,3,6,1,4,1,45,4,2,3,2,8))
qosIpAclDefinitionGroup.setObjects(*((_B,_AU),(_B,_AV),(_B,_AW),(_B,_AX),(_B,_AY),(_B,_AZ)))
if mibBuilder.loadTexts:qosIpAclDefinitionGroup.setStatus(_A)
qosPolicyIpPibCompliance=ModuleCompliance((1,3,6,1,4,1,45,4,2,3,1,1))
qosPolicyIpPibCompliance.setObjects(*((_B,_Aa),(_B,_Ab),(_B,_Ac),(_B,_Ad),(_B,_Ae)))
if mibBuilder.loadTexts:qosPolicyIpPibCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'Dscp':Dscp,_I:PolicyInstanceIdOrZero,'QosInterfaceQueueCount':QosInterfaceQueueCount,'qosPolicyIpPib':qosPolicyIpPib,'qosPolicyGenPibClasses':qosPolicyGenPibClasses,'qosIfParameters':qosIfParameters,'qosInterfaceTypeTable':qosInterfaceTypeTable,'qosInterfaceTypeEntry':qosInterfaceTypeEntry,_J:qosInterfaceTypeId,_R:qosInterfaceTypeRoles,_S:qosInterfaceTypeQueueSet,_T:qosInterfaceTypeCapabilities,_U:qosInterfaceTypeStorageType,_V:qosInterfaceTypeStatus,'qosIfQueueTable':qosIfQueueTable,'qosIfQueueEntry':qosIfQueueEntry,_K:qosIfQueueId,_W:qosIfQueueSetId,_X:qosIfQueueIndex,_Y:qosIfQueueGenDiscipline,_Z:qosIfQueueExtDiscipline,_a:qosIfQueueDrainSize,_b:qosIfQueueAbsBandwidth,_c:qosIfQueueBandwidthAllocation,_d:qosIfQueueServiceOrder,_e:qosIfQueueSize,_f:qosIfQueueStorageType,_g:qosIfQueueStatus,'qosIfDscpAssignmentTable':qosIfDscpAssignmentTable,'qosIfDscpAssignmentEntry':qosIfDscpAssignmentEntry,_L:qosIfDscpAssignmentId,_h:qosIfDscpAssignmentRoles,_i:qosIfDscpAssignmentDscp,_j:qosIfDscpAssignmentQueue,_k:qosIfDscpAssignmentStorageType,_l:qosIfDscpAssignmentStatus,'qosMeter':qosMeter,'qosMeterTable':qosMeterTable,'qosMeterEntry':qosMeterEntry,_M:qosMeterId,_m:qosMeterDataSpecification,_n:qosMeterCommittedRate,_o:qosMeterCommittedBurst,_p:qosMeterPeakRate,_q:qosMeterPeakBurst,_r:qosMeterHighConfAction,_s:qosMeterMedConfAction,_t:qosMeterLowConfAction,_u:qosMeterStorageType,_v:qosMeterStatus,_w:qosMeterLabel,'qosAction':qosAction,'qosActionTable':qosActionTable,'qosActionEntry':qosActionEntry,_N:qosActionId,_x:qosActionDrop,_y:qosActionUpdateDSCP,_z:qosActionMeter,_A0:qosActionStorageType,_A1:qosActionStatus,_A2:qosActionLabel,'qosTargetTable':qosTargetTable,'qosTargetEntry':qosTargetEntry,_O:qosTargetId,_A3:qosTargetAclId,_A4:qosTargetAclType,_A5:qosTargetInterfaceRoles,_A6:qosTargetInterfaceDirection,_A7:qosTargetOrder,_A8:qosTargetMeter,_A9:qosTargetStorageType,_AA:qosTargetStatus,_AB:qosTargetShapingParams,_AC:qosTargetShapingGroup,_AD:qosTargetLabel,_AE:qosTargetInProfileAction,_AF:qosTargetOutOfProfileAction,_AG:qosTargetUserGroupSession,'qosPolicyIpPibClasses':qosPolicyIpPibClasses,'qosIpQos':qosIpQos,'qosIpAceTable':qosIpAceTable,'qosIpAceEntry':qosIpAceEntry,_P:qosIpAceId,_AH:qosIpAceDstAddr,_AI:qosIpAceDstAddrMask,_AJ:qosIpAceSrcAddr,_AK:qosIpAceSrcAddrMask,_AL:qosIpAceDscp,_AM:qosIpAceProtocol,_AN:qosIpAceDstL4PortMin,_AO:qosIpAceDstL4PortMax,_AP:qosIpAceSrcL4PortMin,_AQ:qosIpAceSrcL4PortMax,_AR:qosIpAcePermit,_AS:qosIpAceStorageType,_AT:qosIpAceStatus,'qosIpAclDefinitionTable':qosIpAclDefinitionTable,'qosIpAclDefinitionEntry':qosIpAclDefinitionEntry,_Q:qosIpAclDefinitionId,_AU:qosIpAclDefinitionAclId,_AV:qosIpAclDefinitionAceId,_AW:qosIpAclDefinitionAceOrder,_AX:qosIpAclDefinitionStorageType,_AY:qosIpAclDefinitionStatus,_AZ:qosIpAclDefinitionLabel,'qosPolicyIpPibConformance':qosPolicyIpPibConformance,'qosPolicyIpPibCompliances':qosPolicyIpPibCompliances,'qosPolicyIpPibCompliance':qosPolicyIpPibCompliance,'qosPolicyIpPibGroups':qosPolicyIpPibGroups,_Aa:qosInterfaceTypeGroup,_Ab:qosIfQueueGroup,'qosIfDscpAssignmentGroup':qosIfDscpAssignmentGroup,_Ac:qosMeterGroup,_Ad:qosActionGroup,_Ae:qosTargetGroup,'qosIpAceGroup':qosIpAceGroup,'qosIpAclDefinitionGroup':qosIpAclDefinitionGroup})