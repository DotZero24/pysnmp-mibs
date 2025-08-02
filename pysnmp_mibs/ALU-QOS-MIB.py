_BC='aluSecurityQueueGroup'
_BB='aluQosShaperPolicyGroup'
_BA='aluExtNetworkPolicyGroup'
_B9='aluHQosGroup'
_B8='aluSystemQosGroup'
_B7='aluShaperGroupRateType'
_B6='aluShaperGroupPIRPercent'
_B5='aluShaperGroupCIRPercent'
_B4='aluNetworkQueuePktOffset'
_B3='aluSapEgressQueuePktOffset'
_B2='aluSapIngressQueuePktOffset'
_B1='aluNetworkQueuePolicyPktOffset'
_B0='aluSapEgressPktOffset'
_A_='aluSapIngressPktOffset'
_Az='aluSecurityQueueLastChanged'
_Ay='aluSecurityQueueHiPrioOnly'
_Ax='aluSecurityQueueMBSBytes'
_Aw='aluSecurityQueueCBS'
_Av='aluSecurityQueuePIR'
_Au='aluSecurityQueueCIR'
_At='aluSecurityQueuePolicyLastChanged'
_As='aluSecurityQueuePolicyDescription'
_Ar='aluSecurityQueuePolicyRowStatus'
_Aq='aluShaperGroupLastChanged'
_Ap='aluShaperGroupPIR'
_Ao='aluShaperGroupCIR'
_An='aluShaperGroupDescription'
_Am='aluShaperGroupRowStatus'
_Al='aluShaperPolicyUnshapedIntfGroup'
_Ak='aluShaperPolicyUnshapedSapGroup'
_Aj='aluShaperPolicyDescription'
_Ai='aluShaperPolicyLastChanged'
_Ah='aluShaperPolicyRowStatus'
_Ag='aluExtNetworkRingDot1pQueue'
_Af='aluExtNetworkPolicyDefActionQueue'
_Ae='aluExtNetworkPolicyType'
_Ad='aluSystemIngUnshapedSapCir'
_Ac='aluFabricProfileUnshapedSapCir'
_Ab='aluSystemQosLastChanged'
_Aa='aluSystemNetworkIngAggRate'
_AZ='aluSystemAccessIngAggRate'
_AY='aluFabricProfileMultipointRate'
_AX='aluSapEgressPolicyType'
_AW='aluNetworkQueueSlopePolicy'
_AV='aluSapEgressQueueSlopePolicy'
_AU='aluSapIngressQueueSlopePolicy'
_AT='aluExtNetworkQueuePolicyEntry'
_AS='aluExtSapIngressEntry'
_AR='aluExtNetworkIngressDot1pEntry'
_AQ='aluExtNetworkPolicyEntry'
_AP='aluExtTSapEgressEntry'
_AO='aluNetworkQueueExtensionEntry'
_AN='aluSapEgressQueueExtensionEntry'
_AM='aluSapIngressQueueExtensionEntry'
_AL='aluSecurityQueueIndex'
_AK='hundredths of a percent'
_AJ='aluShaperGroup'
_AI='AluExtNetworkPolicyType'
_AH='AluFabricProfileMode'
_AG='AluFabricProfilePolicyID'
_AF='aluFabricProfileIndex'
_AE='TRateType'
_AD='TBurstSizeBytes'
_AC='TBurstSize'
_AB='TBurstPercentOrDefault'
_AA='Integer32'
_A9='aluQosFabricProfileGroupV4v0'
_A8='aluQosSapEgressPolicyTypeGroup'
_A7='aluQosFabricProfileGroup'
_A6='aluQosQueuePolicySlopePolicyGroup'
_A5='obsolete'
_A4='aluFabricProfileAggregateRate'
_A3='aluFabricProfileMode'
_A2='aluFabricProfileLastChanged'
_A1='aluFabricProfileRateToMdaIndex32'
_A0='aluFabricProfileRateToMdaIndex31'
_z='aluFabricProfileRateToMdaIndex30'
_y='aluFabricProfileRateToMdaIndex29'
_x='aluFabricProfileRateToMdaIndex28'
_w='aluFabricProfileRateToMdaIndex27'
_v='aluFabricProfileRateToMdaIndex26'
_u='aluFabricProfileRateToMdaIndex25'
_t='aluFabricProfileRateToMdaIndex24'
_s='aluFabricProfileRateToMdaIndex23'
_r='aluFabricProfileRateToMdaIndex22'
_q='aluFabricProfileRateToMdaIndex21'
_p='aluFabricProfileRateToMdaIndex20'
_o='aluFabricProfileRateToMdaIndex19'
_n='aluFabricProfileRateToMdaIndex18'
_m='aluFabricProfileRateToMdaIndex17'
_l='aluFabricProfileRateToMdaIndex16'
_k='aluFabricProfileRateToMdaIndex15'
_j='aluFabricProfileRateToMdaIndex14'
_i='aluFabricProfileRateToMdaIndex13'
_h='aluFabricProfileRateToMdaIndex12'
_g='aluFabricProfileRateToMdaIndex11'
_f='aluFabricProfileRateToMdaIndex10'
_e='aluFabricProfileRateToMdaIndex9'
_d='aluFabricProfileRateToMdaIndex8'
_c='aluFabricProfileRateToMdaIndex7'
_b='aluFabricProfileRateToMdaIndex6'
_a='aluFabricProfileRateToMdaIndex5'
_Z='aluFabricProfileRateToMdaIndex4'
_Y='aluFabricProfileRateToMdaIndex3'
_X='aluFabricProfileRateToMdaIndex2'
_W='aluFabricProfileRateToMdaIndex1'
_V='aluFabricProfileDescription'
_U='aluFabricProfileRowStatus'
_T='aluSecurityQueuePolicyIndex'
_S='aluShaperPolicy'
_R='AluSystemAggregateRate'
_Q='AluSapSchedulerCir'
_P='TQueueId'
_O='TPIRRate'
_N='TCIRRate'
_M='Unsigned32'
_L='TItemDescription'
_K='kbps'
_J='not-accessible'
_I='read-only'
_H='TNamedItem'
_G='AluPerPacketOffset'
_F='default'
_E='read-write'
_D='AluFabricProfileDestMdaRate'
_C='read-create'
_B='current'
_A='ALU-QOS-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
aluSARConfs,aluSARMIBModules,aluSARObjs=mibBuilder.importSymbols('ALU-SAR-GLOBAL-MIB','aluSARConfs','aluSARMIBModules','aluSARObjs')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_AA,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_M,'iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TimeStamp=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention','TimeStamp')
tNetworkIngressDot1pEntry,tNetworkPolicyEntry,tNetworkQueueEntry,tNetworkQueuePolicyEntry,tSapEgressEntry,tSapEgressQueueEntry,tSapIngressEntry,tSapIngressQueueEntry=mibBuilder.importSymbols('TIMETRA-QOS-MIB','tNetworkIngressDot1pEntry','tNetworkPolicyEntry','tNetworkQueueEntry','tNetworkQueuePolicyEntry','tSapEgressEntry','tSapEgressQueueEntry','tSapIngressEntry','tSapIngressQueueEntry')
TBurstPercentOrDefault,TBurstSize,TBurstSizeBytes,TCIRRate,TItemDescription,TNamedItem,TPIRRate,TPolicyID,TQueueId,TRateType=mibBuilder.importSymbols('TIMETRA-TC-MIB',_AB,_AC,_AD,_N,_L,_H,_O,'TPolicyID',_P,_AE)
aluQOSMIBModule=ModuleIdentity((1,3,6,1,4,1,6527,6,1,1,1,3,3))
if mibBuilder.loadTexts:aluQOSMIBModule.setRevisions(('1908-01-24 00:00',))
class AluIPsecStatsQueueId(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4)));namedValues=NamedValues(*(('notUsed',0),('ipsec-decrypt-bestEffort',1),('ipsec-decrypt-expedited',2),('ipsec-encrypt-bestEffort',3),('ipsec-encrypt-expedited',4)))
class AluSecQueueId(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('notUsed',0),('bestEffort',1),('expedited',2)))
class AluFabricProfilePolicyID(TPolicyID):status=_B;subtypeSpec=TPolicyID.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,256))
class AluFabricProfileMode(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('aggregate',1),('destination',2)))
class AluFabricProfileDestMdaRate(TextualConvention,Unsigned32):status=_B;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,10000000))
class AluSapSchedulerCir(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,-1),ValueRangeConstraint(0,10000000))
class AluSystemAggregateRate(TextualConvention,Unsigned32):status=_B;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,10000000))
class AluExtNetworkPolicyType(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_F,0),('ipInterface',1),('ring',2)))
class AluPerPacketOffset(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-62,62),ValueRangeConstraint(127,127))
_AluQOSConformance_ObjectIdentity=ObjectIdentity
aluQOSConformance=_AluQOSConformance_ObjectIdentity((1,3,6,1,4,1,6527,6,1,2,1,5))
_AluQOSCompliances_ObjectIdentity=ObjectIdentity
aluQOSCompliances=_AluQOSCompliances_ObjectIdentity((1,3,6,1,4,1,6527,6,1,2,1,5,1))
_AluQOSComp7705_ObjectIdentity=ObjectIdentity
aluQOSComp7705=_AluQOSComp7705_ObjectIdentity((1,3,6,1,4,1,6527,6,1,2,1,5,1,1))
_AluQOSGroups_ObjectIdentity=ObjectIdentity
aluQOSGroups=_AluQOSGroups_ObjectIdentity((1,3,6,1,4,1,6527,6,1,2,1,5,2))
_AluQOSObjs_ObjectIdentity=ObjectIdentity
aluQOSObjs=_AluQOSObjs_ObjectIdentity((1,3,6,1,4,1,6527,6,1,2,2,5))
_AluSapIngressQueueExtensionTable_Object=MibTable
aluSapIngressQueueExtensionTable=_AluSapIngressQueueExtensionTable_Object((1,3,6,1,4,1,6527,6,1,2,2,5,1))
if mibBuilder.loadTexts:aluSapIngressQueueExtensionTable.setStatus(_B)
_AluSapIngressQueueExtensionEntry_Object=MibTableRow
aluSapIngressQueueExtensionEntry=_AluSapIngressQueueExtensionEntry_Object((1,3,6,1,4,1,6527,6,1,2,2,5,1,1))
if mibBuilder.loadTexts:aluSapIngressQueueExtensionEntry.setStatus(_B)
class _AluSapIngressQueueSlopePolicy_Type(TNamedItem):defaultValue=OctetString(_F)
_AluSapIngressQueueSlopePolicy_Type.__name__=_H
_AluSapIngressQueueSlopePolicy_Object=MibTableColumn
aluSapIngressQueueSlopePolicy=_AluSapIngressQueueSlopePolicy_Object((1,3,6,1,4,1,6527,6,1,2,2,5,1,1,1),_AluSapIngressQueueSlopePolicy_Type())
aluSapIngressQueueSlopePolicy.setMaxAccess(_E)
if mibBuilder.loadTexts:aluSapIngressQueueSlopePolicy.setStatus(_B)
class _AluSapIngressQueuePktOffset_Type(AluPerPacketOffset):defaultValue=127
_AluSapIngressQueuePktOffset_Type.__name__=_G
_AluSapIngressQueuePktOffset_Object=MibTableColumn
aluSapIngressQueuePktOffset=_AluSapIngressQueuePktOffset_Object((1,3,6,1,4,1,6527,6,1,2,2,5,1,1,2),_AluSapIngressQueuePktOffset_Type())
aluSapIngressQueuePktOffset.setMaxAccess(_E)
if mibBuilder.loadTexts:aluSapIngressQueuePktOffset.setStatus(_B)
_AluSapEgressQueueExtensionTable_Object=MibTable
aluSapEgressQueueExtensionTable=_AluSapEgressQueueExtensionTable_Object((1,3,6,1,4,1,6527,6,1,2,2,5,2))
if mibBuilder.loadTexts:aluSapEgressQueueExtensionTable.setStatus(_B)
_AluSapEgressQueueExtensionEntry_Object=MibTableRow
aluSapEgressQueueExtensionEntry=_AluSapEgressQueueExtensionEntry_Object((1,3,6,1,4,1,6527,6,1,2,2,5,2,1))
if mibBuilder.loadTexts:aluSapEgressQueueExtensionEntry.setStatus(_B)
class _AluSapEgressQueueSlopePolicy_Type(TNamedItem):defaultValue=OctetString(_F)
_AluSapEgressQueueSlopePolicy_Type.__name__=_H
_AluSapEgressQueueSlopePolicy_Object=MibTableColumn
aluSapEgressQueueSlopePolicy=_AluSapEgressQueueSlopePolicy_Object((1,3,6,1,4,1,6527,6,1,2,2,5,2,1,1),_AluSapEgressQueueSlopePolicy_Type())
aluSapEgressQueueSlopePolicy.setMaxAccess(_E)
if mibBuilder.loadTexts:aluSapEgressQueueSlopePolicy.setStatus(_B)
class _AluSapEgressQueuePktOffset_Type(AluPerPacketOffset):defaultValue=127
_AluSapEgressQueuePktOffset_Type.__name__=_G
_AluSapEgressQueuePktOffset_Object=MibTableColumn
aluSapEgressQueuePktOffset=_AluSapEgressQueuePktOffset_Object((1,3,6,1,4,1,6527,6,1,2,2,5,2,1,2),_AluSapEgressQueuePktOffset_Type())
aluSapEgressQueuePktOffset.setMaxAccess(_E)
if mibBuilder.loadTexts:aluSapEgressQueuePktOffset.setStatus(_B)
_AluNetworkQueueExtensionTable_Object=MibTable
aluNetworkQueueExtensionTable=_AluNetworkQueueExtensionTable_Object((1,3,6,1,4,1,6527,6,1,2,2,5,3))
if mibBuilder.loadTexts:aluNetworkQueueExtensionTable.setStatus(_B)
_AluNetworkQueueExtensionEntry_Object=MibTableRow
aluNetworkQueueExtensionEntry=_AluNetworkQueueExtensionEntry_Object((1,3,6,1,4,1,6527,6,1,2,2,5,3,1))
if mibBuilder.loadTexts:aluNetworkQueueExtensionEntry.setStatus(_B)
class _AluNetworkQueueSlopePolicy_Type(TNamedItem):defaultValue=OctetString(_F)
_AluNetworkQueueSlopePolicy_Type.__name__=_H
_AluNetworkQueueSlopePolicy_Object=MibTableColumn
aluNetworkQueueSlopePolicy=_AluNetworkQueueSlopePolicy_Object((1,3,6,1,4,1,6527,6,1,2,2,5,3,1,1),_AluNetworkQueueSlopePolicy_Type())
aluNetworkQueueSlopePolicy.setMaxAccess(_E)
if mibBuilder.loadTexts:aluNetworkQueueSlopePolicy.setStatus(_B)
class _AluNetworkQueuePktOffset_Type(AluPerPacketOffset):defaultValue=127
_AluNetworkQueuePktOffset_Type.__name__=_G
_AluNetworkQueuePktOffset_Object=MibTableColumn
aluNetworkQueuePktOffset=_AluNetworkQueuePktOffset_Object((1,3,6,1,4,1,6527,6,1,2,2,5,3,1,2),_AluNetworkQueuePktOffset_Type())
aluNetworkQueuePktOffset.setMaxAccess(_E)
if mibBuilder.loadTexts:aluNetworkQueuePktOffset.setStatus(_B)
_AluFabricProfileTable_Object=MibTable
aluFabricProfileTable=_AluFabricProfileTable_Object((1,3,6,1,4,1,6527,6,1,2,2,5,4))
if mibBuilder.loadTexts:aluFabricProfileTable.setStatus(_B)
_AluFabricProfileEntry_Object=MibTableRow
aluFabricProfileEntry=_AluFabricProfileEntry_Object((1,3,6,1,4,1,6527,6,1,2,2,5,4,1))
aluFabricProfileEntry.setIndexNames((0,_A,_AF))
if mibBuilder.loadTexts:aluFabricProfileEntry.setStatus(_B)
class _AluFabricProfileIndex_Type(AluFabricProfilePolicyID):subtypeSpec=AluFabricProfilePolicyID.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,256))
_AluFabricProfileIndex_Type.__name__=_AG
_AluFabricProfileIndex_Object=MibTableColumn
aluFabricProfileIndex=_AluFabricProfileIndex_Object((1,3,6,1,4,1,6527,6,1,2,2,5,4,1,1),_AluFabricProfileIndex_Type())
aluFabricProfileIndex.setMaxAccess(_J)
if mibBuilder.loadTexts:aluFabricProfileIndex.setStatus(_B)
_AluFabricProfileRowStatus_Type=RowStatus
_AluFabricProfileRowStatus_Object=MibTableColumn
aluFabricProfileRowStatus=_AluFabricProfileRowStatus_Object((1,3,6,1,4,1,6527,6,1,2,2,5,4,1,2),_AluFabricProfileRowStatus_Type())
aluFabricProfileRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:aluFabricProfileRowStatus.setStatus(_B)
_AluFabricProfileDescription_Type=TItemDescription
_AluFabricProfileDescription_Object=MibTableColumn
aluFabricProfileDescription=_AluFabricProfileDescription_Object((1,3,6,1,4,1,6527,6,1,2,2,5,4,1,3),_AluFabricProfileDescription_Type())
aluFabricProfileDescription.setMaxAccess(_C)
if mibBuilder.loadTexts:aluFabricProfileDescription.setStatus(_B)
class _AluFabricProfileRateToMdaIndex1_Type(AluFabricProfileDestMdaRate):defaultValue=200000
_AluFabricProfileRateToMdaIndex1_Type.__name__=_D
_AluFabricProfileRateToMdaIndex1_Object=MibTableColumn
aluFabricProfileRateToMdaIndex1=_AluFabricProfileRateToMdaIndex1_Object((1,3,6,1,4,1,6527,6,1,2,2,5,4,1,4),_AluFabricProfileRateToMdaIndex1_Type())
aluFabricProfileRateToMdaIndex1.setMaxAccess(_C)
if mibBuilder.loadTexts:aluFabricProfileRateToMdaIndex1.setStatus(_B)
class _AluFabricProfileRateToMdaIndex2_Type(AluFabricProfileDestMdaRate):defaultValue=200000
_AluFabricProfileRateToMdaIndex2_Type.__name__=_D
_AluFabricProfileRateToMdaIndex2_Object=MibTableColumn
aluFabricProfileRateToMdaIndex2=_AluFabricProfileRateToMdaIndex2_Object((1,3,6,1,4,1,6527,6,1,2,2,5,4,1,5),_AluFabricProfileRateToMdaIndex2_Type())
aluFabricProfileRateToMdaIndex2.setMaxAccess(_C)
if mibBuilder.loadTexts:aluFabricProfileRateToMdaIndex2.setStatus(_B)
class _AluFabricProfileRateToMdaIndex3_Type(AluFabricProfileDestMdaRate):defaultValue=200000
_AluFabricProfileRateToMdaIndex3_Type.__name__=_D
_AluFabricProfileRateToMdaIndex3_Object=MibTableColumn
aluFabricProfileRateToMdaIndex3=_AluFabricProfileRateToMdaIndex3_Object((1,3,6,1,4,1,6527,6,1,2,2,5,4,1,6),_AluFabricProfileRateToMdaIndex3_Type())
aluFabricProfileRateToMdaIndex3.setMaxAccess(_C)
if mibBuilder.loadTexts:aluFabricProfileRateToMdaIndex3.setStatus(_B)
class _AluFabricProfileRateToMdaIndex4_Type(AluFabricProfileDestMdaRate):defaultValue=200000
_AluFabricProfileRateToMdaIndex4_Type.__name__=_D
_AluFabricProfileRateToMdaIndex4_Object=MibTableColumn
aluFabricProfileRateToMdaIndex4=_AluFabricProfileRateToMdaIndex4_Object((1,3,6,1,4,1,6527,6,1,2,2,5,4,1,7),_AluFabricProfileRateToMdaIndex4_Type())
aluFabricProfileRateToMdaIndex4.setMaxAccess(_C)
if mibBuilder.loadTexts:aluFabricProfileRateToMdaIndex4.setStatus(_B)
class _AluFabricProfileRateToMdaIndex5_Type(AluFabricProfileDestMdaRate):defaultValue=200000
_AluFabricProfileRateToMdaIndex5_Type.__name__=_D
_AluFabricProfileRateToMdaIndex5_Object=MibTableColumn
aluFabricProfileRateToMdaIndex5=_AluFabricProfileRateToMdaIndex5_Object((1,3,6,1,4,1,6527,6,1,2,2,5,4,1,8),_AluFabricProfileRateToMdaIndex5_Type())
aluFabricProfileRateToMdaIndex5.setMaxAccess(_C)
if mibBuilder.loadTexts:aluFabricProfileRateToMdaIndex5.setStatus(_B)
class _AluFabricProfileRateToMdaIndex6_Type(AluFabricProfileDestMdaRate):defaultValue=200000
_AluFabricProfileRateToMdaIndex6_Type.__name__=_D
_AluFabricProfileRateToMdaIndex6_Object=MibTableColumn
aluFabricProfileRateToMdaIndex6=_AluFabricProfileRateToMdaIndex6_Object((1,3,6,1,4,1,6527,6,1,2,2,5,4,1,9),_AluFabricProfileRateToMdaIndex6_Type())
aluFabricProfileRateToMdaIndex6.setMaxAccess(_C)
if mibBuilder.loadTexts:aluFabricProfileRateToMdaIndex6.setStatus(_B)
class _AluFabricProfileRateToMdaIndex7_Type(AluFabricProfileDestMdaRate):defaultValue=200000
_AluFabricProfileRateToMdaIndex7_Type.__name__=_D
_AluFabricProfileRateToMdaIndex7_Object=MibTableColumn
aluFabricProfileRateToMdaIndex7=_AluFabricProfileRateToMdaIndex7_Object((1,3,6,1,4,1,6527,6,1,2,2,5,4,1,10),_AluFabricProfileRateToMdaIndex7_Type())
aluFabricProfileRateToMdaIndex7.setMaxAccess(_C)
if mibBuilder.loadTexts:aluFabricProfileRateToMdaIndex7.setStatus(_B)
class _AluFabricProfileRateToMdaIndex8_Type(AluFabricProfileDestMdaRate):defaultValue=200000
_AluFabricProfileRateToMdaIndex8_Type.__name__=_D
_AluFabricProfileRateToMdaIndex8_Object=MibTableColumn
aluFabricProfileRateToMdaIndex8=_AluFabricProfileRateToMdaIndex8_Object((1,3,6,1,4,1,6527,6,1,2,2,5,4,1,11),_AluFabricProfileRateToMdaIndex8_Type())
aluFabricProfileRateToMdaIndex8.setMaxAccess(_C)
if mibBuilder.loadTexts:aluFabricProfileRateToMdaIndex8.setStatus(_B)
class _AluFabricProfileRateToMdaIndex9_Type(AluFabricProfileDestMdaRate):defaultValue=200000
_AluFabricProfileRateToMdaIndex9_Type.__name__=_D
_AluFabricProfileRateToMdaIndex9_Object=MibTableColumn
aluFabricProfileRateToMdaIndex9=_AluFabricProfileRateToMdaIndex9_Object((1,3,6,1,4,1,6527,6,1,2,2,5,4,1,12),_AluFabricProfileRateToMdaIndex9_Type())
aluFabricProfileRateToMdaIndex9.setMaxAccess(_C)
if mibBuilder.loadTexts:aluFabricProfileRateToMdaIndex9.setStatus(_B)
class _AluFabricProfileRateToMdaIndex10_Type(AluFabricProfileDestMdaRate):defaultValue=200000
_AluFabricProfileRateToMdaIndex10_Type.__name__=_D
_AluFabricProfileRateToMdaIndex10_Object=MibTableColumn
aluFabricProfileRateToMdaIndex10=_AluFabricProfileRateToMdaIndex10_Object((1,3,6,1,4,1,6527,6,1,2,2,5,4,1,13),_AluFabricProfileRateToMdaIndex10_Type())
aluFabricProfileRateToMdaIndex10.setMaxAccess(_C)
if mibBuilder.loadTexts:aluFabricProfileRateToMdaIndex10.setStatus(_B)
class _AluFabricProfileRateToMdaIndex11_Type(AluFabricProfileDestMdaRate):defaultValue=200000
_AluFabricProfileRateToMdaIndex11_Type.__name__=_D
_AluFabricProfileRateToMdaIndex11_Object=MibTableColumn
aluFabricProfileRateToMdaIndex11=_AluFabricProfileRateToMdaIndex11_Object((1,3,6,1,4,1,6527,6,1,2,2,5,4,1,14),_AluFabricProfileRateToMdaIndex11_Type())
aluFabricProfileRateToMdaIndex11.setMaxAccess(_C)
if mibBuilder.loadTexts:aluFabricProfileRateToMdaIndex11.setStatus(_B)
class _AluFabricProfileRateToMdaIndex12_Type(AluFabricProfileDestMdaRate):defaultValue=200000
_AluFabricProfileRateToMdaIndex12_Type.__name__=_D
_AluFabricProfileRateToMdaIndex12_Object=MibTableColumn
aluFabricProfileRateToMdaIndex12=_AluFabricProfileRateToMdaIndex12_Object((1,3,6,1,4,1,6527,6,1,2,2,5,4,1,15),_AluFabricProfileRateToMdaIndex12_Type())
aluFabricProfileRateToMdaIndex12.setMaxAccess(_C)
if mibBuilder.loadTexts:aluFabricProfileRateToMdaIndex12.setStatus(_B)
class _AluFabricProfileRateToMdaIndex13_Type(AluFabricProfileDestMdaRate):defaultValue=200000
_AluFabricProfileRateToMdaIndex13_Type.__name__=_D
_AluFabricProfileRateToMdaIndex13_Object=MibTableColumn
aluFabricProfileRateToMdaIndex13=_AluFabricProfileRateToMdaIndex13_Object((1,3,6,1,4,1,6527,6,1,2,2,5,4,1,16),_AluFabricProfileRateToMdaIndex13_Type())
aluFabricProfileRateToMdaIndex13.setMaxAccess(_C)
if mibBuilder.loadTexts:aluFabricProfileRateToMdaIndex13.setStatus(_B)
class _AluFabricProfileRateToMdaIndex14_Type(AluFabricProfileDestMdaRate):defaultValue=200000
_AluFabricProfileRateToMdaIndex14_Type.__name__=_D
_AluFabricProfileRateToMdaIndex14_Object=MibTableColumn
aluFabricProfileRateToMdaIndex14=_AluFabricProfileRateToMdaIndex14_Object((1,3,6,1,4,1,6527,6,1,2,2,5,4,1,17),_AluFabricProfileRateToMdaIndex14_Type())
aluFabricProfileRateToMdaIndex14.setMaxAccess(_C)
if mibBuilder.loadTexts:aluFabricProfileRateToMdaIndex14.setStatus(_B)
class _AluFabricProfileRateToMdaIndex15_Type(AluFabricProfileDestMdaRate):defaultValue=200000
_AluFabricProfileRateToMdaIndex15_Type.__name__=_D
_AluFabricProfileRateToMdaIndex15_Object=MibTableColumn
aluFabricProfileRateToMdaIndex15=_AluFabricProfileRateToMdaIndex15_Object((1,3,6,1,4,1,6527,6,1,2,2,5,4,1,18),_AluFabricProfileRateToMdaIndex15_Type())
aluFabricProfileRateToMdaIndex15.setMaxAccess(_C)
if mibBuilder.loadTexts:aluFabricProfileRateToMdaIndex15.setStatus(_B)
class _AluFabricProfileRateToMdaIndex16_Type(AluFabricProfileDestMdaRate):defaultValue=200000
_AluFabricProfileRateToMdaIndex16_Type.__name__=_D
_AluFabricProfileRateToMdaIndex16_Object=MibTableColumn
aluFabricProfileRateToMdaIndex16=_AluFabricProfileRateToMdaIndex16_Object((1,3,6,1,4,1,6527,6,1,2,2,5,4,1,19),_AluFabricProfileRateToMdaIndex16_Type())
aluFabricProfileRateToMdaIndex16.setMaxAccess(_C)
if mibBuilder.loadTexts:aluFabricProfileRateToMdaIndex16.setStatus(_B)
class _AluFabricProfileRateToMdaIndex17_Type(AluFabricProfileDestMdaRate):defaultValue=200000
_AluFabricProfileRateToMdaIndex17_Type.__name__=_D
_AluFabricProfileRateToMdaIndex17_Object=MibTableColumn
aluFabricProfileRateToMdaIndex17=_AluFabricProfileRateToMdaIndex17_Object((1,3,6,1,4,1,6527,6,1,2,2,5,4,1,20),_AluFabricProfileRateToMdaIndex17_Type())
aluFabricProfileRateToMdaIndex17.setMaxAccess(_C)
if mibBuilder.loadTexts:aluFabricProfileRateToMdaIndex17.setStatus(_B)
class _AluFabricProfileRateToMdaIndex18_Type(AluFabricProfileDestMdaRate):defaultValue=200000
_AluFabricProfileRateToMdaIndex18_Type.__name__=_D
_AluFabricProfileRateToMdaIndex18_Object=MibTableColumn
aluFabricProfileRateToMdaIndex18=_AluFabricProfileRateToMdaIndex18_Object((1,3,6,1,4,1,6527,6,1,2,2,5,4,1,21),_AluFabricProfileRateToMdaIndex18_Type())
aluFabricProfileRateToMdaIndex18.setMaxAccess(_C)
if mibBuilder.loadTexts:aluFabricProfileRateToMdaIndex18.setStatus(_B)
class _AluFabricProfileRateToMdaIndex19_Type(AluFabricProfileDestMdaRate):defaultValue=200000
_AluFabricProfileRateToMdaIndex19_Type.__name__=_D
_AluFabricProfileRateToMdaIndex19_Object=MibTableColumn
aluFabricProfileRateToMdaIndex19=_AluFabricProfileRateToMdaIndex19_Object((1,3,6,1,4,1,6527,6,1,2,2,5,4,1,22),_AluFabricProfileRateToMdaIndex19_Type())
aluFabricProfileRateToMdaIndex19.setMaxAccess(_C)
if mibBuilder.loadTexts:aluFabricProfileRateToMdaIndex19.setStatus(_B)
class _AluFabricProfileRateToMdaIndex20_Type(AluFabricProfileDestMdaRate):defaultValue=200000
_AluFabricProfileRateToMdaIndex20_Type.__name__=_D
_AluFabricProfileRateToMdaIndex20_Object=MibTableColumn
aluFabricProfileRateToMdaIndex20=_AluFabricProfileRateToMdaIndex20_Object((1,3,6,1,4,1,6527,6,1,2,2,5,4,1,23),_AluFabricProfileRateToMdaIndex20_Type())
aluFabricProfileRateToMdaIndex20.setMaxAccess(_C)
if mibBuilder.loadTexts:aluFabricProfileRateToMdaIndex20.setStatus(_B)
class _AluFabricProfileRateToMdaIndex21_Type(AluFabricProfileDestMdaRate):defaultValue=200000
_AluFabricProfileRateToMdaIndex21_Type.__name__=_D
_AluFabricProfileRateToMdaIndex21_Object=MibTableColumn
aluFabricProfileRateToMdaIndex21=_AluFabricProfileRateToMdaIndex21_Object((1,3,6,1,4,1,6527,6,1,2,2,5,4,1,24),_AluFabricProfileRateToMdaIndex21_Type())
aluFabricProfileRateToMdaIndex21.setMaxAccess(_C)
if mibBuilder.loadTexts:aluFabricProfileRateToMdaIndex21.setStatus(_B)
class _AluFabricProfileRateToMdaIndex22_Type(AluFabricProfileDestMdaRate):defaultValue=200000
_AluFabricProfileRateToMdaIndex22_Type.__name__=_D
_AluFabricProfileRateToMdaIndex22_Object=MibTableColumn
aluFabricProfileRateToMdaIndex22=_AluFabricProfileRateToMdaIndex22_Object((1,3,6,1,4,1,6527,6,1,2,2,5,4,1,25),_AluFabricProfileRateToMdaIndex22_Type())
aluFabricProfileRateToMdaIndex22.setMaxAccess(_C)
if mibBuilder.loadTexts:aluFabricProfileRateToMdaIndex22.setStatus(_B)
class _AluFabricProfileRateToMdaIndex23_Type(AluFabricProfileDestMdaRate):defaultValue=200000
_AluFabricProfileRateToMdaIndex23_Type.__name__=_D
_AluFabricProfileRateToMdaIndex23_Object=MibTableColumn
aluFabricProfileRateToMdaIndex23=_AluFabricProfileRateToMdaIndex23_Object((1,3,6,1,4,1,6527,6,1,2,2,5,4,1,26),_AluFabricProfileRateToMdaIndex23_Type())
aluFabricProfileRateToMdaIndex23.setMaxAccess(_C)
if mibBuilder.loadTexts:aluFabricProfileRateToMdaIndex23.setStatus(_B)
class _AluFabricProfileRateToMdaIndex24_Type(AluFabricProfileDestMdaRate):defaultValue=200000
_AluFabricProfileRateToMdaIndex24_Type.__name__=_D
_AluFabricProfileRateToMdaIndex24_Object=MibTableColumn
aluFabricProfileRateToMdaIndex24=_AluFabricProfileRateToMdaIndex24_Object((1,3,6,1,4,1,6527,6,1,2,2,5,4,1,27),_AluFabricProfileRateToMdaIndex24_Type())
aluFabricProfileRateToMdaIndex24.setMaxAccess(_C)
if mibBuilder.loadTexts:aluFabricProfileRateToMdaIndex24.setStatus(_B)
class _AluFabricProfileRateToMdaIndex25_Type(AluFabricProfileDestMdaRate):defaultValue=200000
_AluFabricProfileRateToMdaIndex25_Type.__name__=_D
_AluFabricProfileRateToMdaIndex25_Object=MibTableColumn
aluFabricProfileRateToMdaIndex25=_AluFabricProfileRateToMdaIndex25_Object((1,3,6,1,4,1,6527,6,1,2,2,5,4,1,28),_AluFabricProfileRateToMdaIndex25_Type())
aluFabricProfileRateToMdaIndex25.setMaxAccess(_C)
if mibBuilder.loadTexts:aluFabricProfileRateToMdaIndex25.setStatus(_B)
class _AluFabricProfileRateToMdaIndex26_Type(AluFabricProfileDestMdaRate):defaultValue=200000
_AluFabricProfileRateToMdaIndex26_Type.__name__=_D
_AluFabricProfileRateToMdaIndex26_Object=MibTableColumn
aluFabricProfileRateToMdaIndex26=_AluFabricProfileRateToMdaIndex26_Object((1,3,6,1,4,1,6527,6,1,2,2,5,4,1,29),_AluFabricProfileRateToMdaIndex26_Type())
aluFabricProfileRateToMdaIndex26.setMaxAccess(_C)
if mibBuilder.loadTexts:aluFabricProfileRateToMdaIndex26.setStatus(_B)
class _AluFabricProfileRateToMdaIndex27_Type(AluFabricProfileDestMdaRate):defaultValue=200000
_AluFabricProfileRateToMdaIndex27_Type.__name__=_D
_AluFabricProfileRateToMdaIndex27_Object=MibTableColumn
aluFabricProfileRateToMdaIndex27=_AluFabricProfileRateToMdaIndex27_Object((1,3,6,1,4,1,6527,6,1,2,2,5,4,1,30),_AluFabricProfileRateToMdaIndex27_Type())
aluFabricProfileRateToMdaIndex27.setMaxAccess(_C)
if mibBuilder.loadTexts:aluFabricProfileRateToMdaIndex27.setStatus(_B)
class _AluFabricProfileRateToMdaIndex28_Type(AluFabricProfileDestMdaRate):defaultValue=200000
_AluFabricProfileRateToMdaIndex28_Type.__name__=_D
_AluFabricProfileRateToMdaIndex28_Object=MibTableColumn
aluFabricProfileRateToMdaIndex28=_AluFabricProfileRateToMdaIndex28_Object((1,3,6,1,4,1,6527,6,1,2,2,5,4,1,31),_AluFabricProfileRateToMdaIndex28_Type())
aluFabricProfileRateToMdaIndex28.setMaxAccess(_C)
if mibBuilder.loadTexts:aluFabricProfileRateToMdaIndex28.setStatus(_B)
class _AluFabricProfileRateToMdaIndex29_Type(AluFabricProfileDestMdaRate):defaultValue=200000
_AluFabricProfileRateToMdaIndex29_Type.__name__=_D
_AluFabricProfileRateToMdaIndex29_Object=MibTableColumn
aluFabricProfileRateToMdaIndex29=_AluFabricProfileRateToMdaIndex29_Object((1,3,6,1,4,1,6527,6,1,2,2,5,4,1,32),_AluFabricProfileRateToMdaIndex29_Type())
aluFabricProfileRateToMdaIndex29.setMaxAccess(_C)
if mibBuilder.loadTexts:aluFabricProfileRateToMdaIndex29.setStatus(_B)
class _AluFabricProfileRateToMdaIndex30_Type(AluFabricProfileDestMdaRate):defaultValue=200000
_AluFabricProfileRateToMdaIndex30_Type.__name__=_D
_AluFabricProfileRateToMdaIndex30_Object=MibTableColumn
aluFabricProfileRateToMdaIndex30=_AluFabricProfileRateToMdaIndex30_Object((1,3,6,1,4,1,6527,6,1,2,2,5,4,1,33),_AluFabricProfileRateToMdaIndex30_Type())
aluFabricProfileRateToMdaIndex30.setMaxAccess(_C)
if mibBuilder.loadTexts:aluFabricProfileRateToMdaIndex30.setStatus(_B)
class _AluFabricProfileRateToMdaIndex31_Type(AluFabricProfileDestMdaRate):defaultValue=200000
_AluFabricProfileRateToMdaIndex31_Type.__name__=_D
_AluFabricProfileRateToMdaIndex31_Object=MibTableColumn
aluFabricProfileRateToMdaIndex31=_AluFabricProfileRateToMdaIndex31_Object((1,3,6,1,4,1,6527,6,1,2,2,5,4,1,34),_AluFabricProfileRateToMdaIndex31_Type())
aluFabricProfileRateToMdaIndex31.setMaxAccess(_C)
if mibBuilder.loadTexts:aluFabricProfileRateToMdaIndex31.setStatus(_B)
class _AluFabricProfileRateToMdaIndex32_Type(AluFabricProfileDestMdaRate):defaultValue=200000
_AluFabricProfileRateToMdaIndex32_Type.__name__=_D
_AluFabricProfileRateToMdaIndex32_Object=MibTableColumn
aluFabricProfileRateToMdaIndex32=_AluFabricProfileRateToMdaIndex32_Object((1,3,6,1,4,1,6527,6,1,2,2,5,4,1,35),_AluFabricProfileRateToMdaIndex32_Type())
aluFabricProfileRateToMdaIndex32.setMaxAccess(_C)
if mibBuilder.loadTexts:aluFabricProfileRateToMdaIndex32.setStatus(_B)
_AluFabricProfileLastChanged_Type=TimeStamp
_AluFabricProfileLastChanged_Object=MibTableColumn
aluFabricProfileLastChanged=_AluFabricProfileLastChanged_Object((1,3,6,1,4,1,6527,6,1,2,2,5,4,1,36),_AluFabricProfileLastChanged_Type())
aluFabricProfileLastChanged.setMaxAccess(_I)
if mibBuilder.loadTexts:aluFabricProfileLastChanged.setStatus(_B)
class _AluFabricProfileMode_Type(AluFabricProfileMode):defaultValue=1
_AluFabricProfileMode_Type.__name__=_AH
_AluFabricProfileMode_Object=MibTableColumn
aluFabricProfileMode=_AluFabricProfileMode_Object((1,3,6,1,4,1,6527,6,1,2,2,5,4,1,37),_AluFabricProfileMode_Type())
aluFabricProfileMode.setMaxAccess(_C)
if mibBuilder.loadTexts:aluFabricProfileMode.setStatus(_B)
class _AluFabricProfileAggregateRate_Type(AluFabricProfileDestMdaRate):defaultValue=200000
_AluFabricProfileAggregateRate_Type.__name__=_D
_AluFabricProfileAggregateRate_Object=MibTableColumn
aluFabricProfileAggregateRate=_AluFabricProfileAggregateRate_Object((1,3,6,1,4,1,6527,6,1,2,2,5,4,1,38),_AluFabricProfileAggregateRate_Type())
aluFabricProfileAggregateRate.setMaxAccess(_C)
if mibBuilder.loadTexts:aluFabricProfileAggregateRate.setStatus(_B)
class _AluFabricProfileMultipointRate_Type(AluFabricProfileDestMdaRate):defaultValue=200000
_AluFabricProfileMultipointRate_Type.__name__=_D
_AluFabricProfileMultipointRate_Object=MibTableColumn
aluFabricProfileMultipointRate=_AluFabricProfileMultipointRate_Object((1,3,6,1,4,1,6527,6,1,2,2,5,4,1,39),_AluFabricProfileMultipointRate_Type())
aluFabricProfileMultipointRate.setMaxAccess(_C)
if mibBuilder.loadTexts:aluFabricProfileMultipointRate.setStatus(_B)
class _AluFabricProfileUnshapedSapCir_Type(AluSapSchedulerCir):defaultValue=0
_AluFabricProfileUnshapedSapCir_Type.__name__=_Q
_AluFabricProfileUnshapedSapCir_Object=MibTableColumn
aluFabricProfileUnshapedSapCir=_AluFabricProfileUnshapedSapCir_Object((1,3,6,1,4,1,6527,6,1,2,2,5,4,1,40),_AluFabricProfileUnshapedSapCir_Type())
aluFabricProfileUnshapedSapCir.setMaxAccess(_C)
if mibBuilder.loadTexts:aluFabricProfileUnshapedSapCir.setStatus(_B)
if mibBuilder.loadTexts:aluFabricProfileUnshapedSapCir.setUnits(_K)
_AluExtTSapEgressTable_Object=MibTable
aluExtTSapEgressTable=_AluExtTSapEgressTable_Object((1,3,6,1,4,1,6527,6,1,2,2,5,5))
if mibBuilder.loadTexts:aluExtTSapEgressTable.setStatus(_B)
_AluExtTSapEgressEntry_Object=MibTableRow
aluExtTSapEgressEntry=_AluExtTSapEgressEntry_Object((1,3,6,1,4,1,6527,6,1,2,2,5,5,1))
if mibBuilder.loadTexts:aluExtTSapEgressEntry.setStatus(_B)
class _AluSapEgressPolicyType_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_F,1),('standard',2),('mc-mlppp',3)))
_AluSapEgressPolicyType_Type.__name__=_AA
_AluSapEgressPolicyType_Object=MibTableColumn
aluSapEgressPolicyType=_AluSapEgressPolicyType_Object((1,3,6,1,4,1,6527,6,1,2,2,5,5,1,1),_AluSapEgressPolicyType_Type())
aluSapEgressPolicyType.setMaxAccess(_E)
if mibBuilder.loadTexts:aluSapEgressPolicyType.setStatus(_B)
class _AluSapEgressPktOffset_Type(AluPerPacketOffset):defaultValue=127
_AluSapEgressPktOffset_Type.__name__=_G
_AluSapEgressPktOffset_Object=MibTableColumn
aluSapEgressPktOffset=_AluSapEgressPktOffset_Object((1,3,6,1,4,1,6527,6,1,2,2,5,5,1,2),_AluSapEgressPktOffset_Type())
aluSapEgressPktOffset.setMaxAccess(_E)
if mibBuilder.loadTexts:aluSapEgressPktOffset.setStatus(_B)
_AluSystemQosConfig_ObjectIdentity=ObjectIdentity
aluSystemQosConfig=_AluSystemQosConfig_ObjectIdentity((1,3,6,1,4,1,6527,6,1,2,2,5,6))
class _AluSystemAccessIngAggRate_Type(AluSystemAggregateRate):defaultValue=0
_AluSystemAccessIngAggRate_Type.__name__=_R
_AluSystemAccessIngAggRate_Object=MibScalar
aluSystemAccessIngAggRate=_AluSystemAccessIngAggRate_Object((1,3,6,1,4,1,6527,6,1,2,2,5,6,1),_AluSystemAccessIngAggRate_Type())
aluSystemAccessIngAggRate.setMaxAccess(_E)
if mibBuilder.loadTexts:aluSystemAccessIngAggRate.setStatus(_B)
class _AluSystemNetworkIngAggRate_Type(AluSystemAggregateRate):defaultValue=0
_AluSystemNetworkIngAggRate_Type.__name__=_R
_AluSystemNetworkIngAggRate_Object=MibScalar
aluSystemNetworkIngAggRate=_AluSystemNetworkIngAggRate_Object((1,3,6,1,4,1,6527,6,1,2,2,5,6,2),_AluSystemNetworkIngAggRate_Type())
aluSystemNetworkIngAggRate.setMaxAccess(_E)
if mibBuilder.loadTexts:aluSystemNetworkIngAggRate.setStatus(_B)
_AluSystemQosLastChanged_Type=TimeStamp
_AluSystemQosLastChanged_Object=MibScalar
aluSystemQosLastChanged=_AluSystemQosLastChanged_Object((1,3,6,1,4,1,6527,6,1,2,2,5,6,3),_AluSystemQosLastChanged_Type())
aluSystemQosLastChanged.setMaxAccess(_I)
if mibBuilder.loadTexts:aluSystemQosLastChanged.setStatus(_B)
class _AluSystemIngUnshapedSapCir_Type(AluSapSchedulerCir):defaultValue=0
_AluSystemIngUnshapedSapCir_Type.__name__=_Q
_AluSystemIngUnshapedSapCir_Object=MibScalar
aluSystemIngUnshapedSapCir=_AluSystemIngUnshapedSapCir_Object((1,3,6,1,4,1,6527,6,1,2,2,5,6,4),_AluSystemIngUnshapedSapCir_Type())
aluSystemIngUnshapedSapCir.setMaxAccess(_E)
if mibBuilder.loadTexts:aluSystemIngUnshapedSapCir.setStatus(_B)
_AluExtNetworkPolicyTable_Object=MibTable
aluExtNetworkPolicyTable=_AluExtNetworkPolicyTable_Object((1,3,6,1,4,1,6527,6,1,2,2,5,7))
if mibBuilder.loadTexts:aluExtNetworkPolicyTable.setStatus(_B)
_AluExtNetworkPolicyEntry_Object=MibTableRow
aluExtNetworkPolicyEntry=_AluExtNetworkPolicyEntry_Object((1,3,6,1,4,1,6527,6,1,2,2,5,7,1))
if mibBuilder.loadTexts:aluExtNetworkPolicyEntry.setStatus(_B)
class _AluExtNetworkPolicyType_Type(AluExtNetworkPolicyType):defaultValue=1
_AluExtNetworkPolicyType_Type.__name__=_AI
_AluExtNetworkPolicyType_Object=MibTableColumn
aluExtNetworkPolicyType=_AluExtNetworkPolicyType_Object((1,3,6,1,4,1,6527,6,1,2,2,5,7,1,1),_AluExtNetworkPolicyType_Type())
aluExtNetworkPolicyType.setMaxAccess(_E)
if mibBuilder.loadTexts:aluExtNetworkPolicyType.setStatus(_B)
class _AluExtNetworkPolicyDefActionQueue_Type(TQueueId):defaultValue=1;subtypeSpec=TQueueId.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,8))
_AluExtNetworkPolicyDefActionQueue_Type.__name__=_P
_AluExtNetworkPolicyDefActionQueue_Object=MibTableColumn
aluExtNetworkPolicyDefActionQueue=_AluExtNetworkPolicyDefActionQueue_Object((1,3,6,1,4,1,6527,6,1,2,2,5,7,1,2),_AluExtNetworkPolicyDefActionQueue_Type())
aluExtNetworkPolicyDefActionQueue.setMaxAccess(_E)
if mibBuilder.loadTexts:aluExtNetworkPolicyDefActionQueue.setStatus(_B)
_AluExtNetworkIngressDot1pTable_Object=MibTable
aluExtNetworkIngressDot1pTable=_AluExtNetworkIngressDot1pTable_Object((1,3,6,1,4,1,6527,6,1,2,2,5,8))
if mibBuilder.loadTexts:aluExtNetworkIngressDot1pTable.setStatus(_B)
_AluExtNetworkIngressDot1pEntry_Object=MibTableRow
aluExtNetworkIngressDot1pEntry=_AluExtNetworkIngressDot1pEntry_Object((1,3,6,1,4,1,6527,6,1,2,2,5,8,1))
if mibBuilder.loadTexts:aluExtNetworkIngressDot1pEntry.setStatus(_B)
class _AluExtNetworkRingDot1pQueue_Type(TQueueId):defaultValue=1;subtypeSpec=TQueueId.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,8))
_AluExtNetworkRingDot1pQueue_Type.__name__=_P
_AluExtNetworkRingDot1pQueue_Object=MibTableColumn
aluExtNetworkRingDot1pQueue=_AluExtNetworkRingDot1pQueue_Object((1,3,6,1,4,1,6527,6,1,2,2,5,8,1,1),_AluExtNetworkRingDot1pQueue_Type())
aluExtNetworkRingDot1pQueue.setMaxAccess(_E)
if mibBuilder.loadTexts:aluExtNetworkRingDot1pQueue.setStatus(_B)
_AluShaperPolicyTable_Object=MibTable
aluShaperPolicyTable=_AluShaperPolicyTable_Object((1,3,6,1,4,1,6527,6,1,2,2,5,9))
if mibBuilder.loadTexts:aluShaperPolicyTable.setStatus(_B)
_AluShaperPolicyEntry_Object=MibTableRow
aluShaperPolicyEntry=_AluShaperPolicyEntry_Object((1,3,6,1,4,1,6527,6,1,2,2,5,9,1))
aluShaperPolicyEntry.setIndexNames((0,_A,_S))
if mibBuilder.loadTexts:aluShaperPolicyEntry.setStatus(_B)
_AluShaperPolicy_Type=TNamedItem
_AluShaperPolicy_Object=MibTableColumn
aluShaperPolicy=_AluShaperPolicy_Object((1,3,6,1,4,1,6527,6,1,2,2,5,9,1,1),_AluShaperPolicy_Type())
aluShaperPolicy.setMaxAccess(_J)
if mibBuilder.loadTexts:aluShaperPolicy.setStatus(_B)
_AluShaperPolicyRowStatus_Type=RowStatus
_AluShaperPolicyRowStatus_Object=MibTableColumn
aluShaperPolicyRowStatus=_AluShaperPolicyRowStatus_Object((1,3,6,1,4,1,6527,6,1,2,2,5,9,1,2),_AluShaperPolicyRowStatus_Type())
aluShaperPolicyRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:aluShaperPolicyRowStatus.setStatus(_B)
_AluShaperPolicyLastChanged_Type=TimeStamp
_AluShaperPolicyLastChanged_Object=MibTableColumn
aluShaperPolicyLastChanged=_AluShaperPolicyLastChanged_Object((1,3,6,1,4,1,6527,6,1,2,2,5,9,1,3),_AluShaperPolicyLastChanged_Type())
aluShaperPolicyLastChanged.setMaxAccess(_I)
if mibBuilder.loadTexts:aluShaperPolicyLastChanged.setStatus(_B)
class _AluShaperPolicyDescription_Type(TItemDescription):defaultHexValue=''
_AluShaperPolicyDescription_Type.__name__=_L
_AluShaperPolicyDescription_Object=MibTableColumn
aluShaperPolicyDescription=_AluShaperPolicyDescription_Object((1,3,6,1,4,1,6527,6,1,2,2,5,9,1,4),_AluShaperPolicyDescription_Type())
aluShaperPolicyDescription.setMaxAccess(_C)
if mibBuilder.loadTexts:aluShaperPolicyDescription.setStatus(_B)
class _AluShaperPolicyUnshapedSapGroup_Type(TNamedItem):defaultValue=OctetString(_F)
_AluShaperPolicyUnshapedSapGroup_Type.__name__=_H
_AluShaperPolicyUnshapedSapGroup_Object=MibTableColumn
aluShaperPolicyUnshapedSapGroup=_AluShaperPolicyUnshapedSapGroup_Object((1,3,6,1,4,1,6527,6,1,2,2,5,9,1,5),_AluShaperPolicyUnshapedSapGroup_Type())
aluShaperPolicyUnshapedSapGroup.setMaxAccess(_C)
if mibBuilder.loadTexts:aluShaperPolicyUnshapedSapGroup.setStatus(_B)
class _AluShaperPolicyUnshapedIntfGroup_Type(TNamedItem):defaultValue=OctetString(_F)
_AluShaperPolicyUnshapedIntfGroup_Type.__name__=_H
_AluShaperPolicyUnshapedIntfGroup_Object=MibTableColumn
aluShaperPolicyUnshapedIntfGroup=_AluShaperPolicyUnshapedIntfGroup_Object((1,3,6,1,4,1,6527,6,1,2,2,5,9,1,6),_AluShaperPolicyUnshapedIntfGroup_Type())
aluShaperPolicyUnshapedIntfGroup.setMaxAccess(_C)
if mibBuilder.loadTexts:aluShaperPolicyUnshapedIntfGroup.setStatus(_B)
_AluShaperGroupTable_Object=MibTable
aluShaperGroupTable=_AluShaperGroupTable_Object((1,3,6,1,4,1,6527,6,1,2,2,5,10))
if mibBuilder.loadTexts:aluShaperGroupTable.setStatus(_B)
_AluShaperGroupEntry_Object=MibTableRow
aluShaperGroupEntry=_AluShaperGroupEntry_Object((1,3,6,1,4,1,6527,6,1,2,2,5,10,1))
aluShaperGroupEntry.setIndexNames((0,_A,_S),(0,_A,_AJ))
if mibBuilder.loadTexts:aluShaperGroupEntry.setStatus(_B)
_AluShaperGroup_Type=TNamedItem
_AluShaperGroup_Object=MibTableColumn
aluShaperGroup=_AluShaperGroup_Object((1,3,6,1,4,1,6527,6,1,2,2,5,10,1,1),_AluShaperGroup_Type())
aluShaperGroup.setMaxAccess(_J)
if mibBuilder.loadTexts:aluShaperGroup.setStatus(_B)
_AluShaperGroupRowStatus_Type=RowStatus
_AluShaperGroupRowStatus_Object=MibTableColumn
aluShaperGroupRowStatus=_AluShaperGroupRowStatus_Object((1,3,6,1,4,1,6527,6,1,2,2,5,10,1,2),_AluShaperGroupRowStatus_Type())
aluShaperGroupRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:aluShaperGroupRowStatus.setStatus(_B)
class _AluShaperGroupDescription_Type(TItemDescription):defaultHexValue=''
_AluShaperGroupDescription_Type.__name__=_L
_AluShaperGroupDescription_Object=MibTableColumn
aluShaperGroupDescription=_AluShaperGroupDescription_Object((1,3,6,1,4,1,6527,6,1,2,2,5,10,1,3),_AluShaperGroupDescription_Type())
aluShaperGroupDescription.setMaxAccess(_C)
if mibBuilder.loadTexts:aluShaperGroupDescription.setStatus(_B)
class _AluShaperGroupCIR_Type(TCIRRate):defaultValue=0
_AluShaperGroupCIR_Type.__name__=_N
_AluShaperGroupCIR_Object=MibTableColumn
aluShaperGroupCIR=_AluShaperGroupCIR_Object((1,3,6,1,4,1,6527,6,1,2,2,5,10,1,4),_AluShaperGroupCIR_Type())
aluShaperGroupCIR.setMaxAccess(_C)
if mibBuilder.loadTexts:aluShaperGroupCIR.setStatus(_B)
if mibBuilder.loadTexts:aluShaperGroupCIR.setUnits(_K)
class _AluShaperGroupPIR_Type(TPIRRate):defaultValue=-1
_AluShaperGroupPIR_Type.__name__=_O
_AluShaperGroupPIR_Object=MibTableColumn
aluShaperGroupPIR=_AluShaperGroupPIR_Object((1,3,6,1,4,1,6527,6,1,2,2,5,10,1,5),_AluShaperGroupPIR_Type())
aluShaperGroupPIR.setMaxAccess(_C)
if mibBuilder.loadTexts:aluShaperGroupPIR.setStatus(_B)
if mibBuilder.loadTexts:aluShaperGroupPIR.setUnits(_K)
_AluShaperGroupLastChanged_Type=TimeStamp
_AluShaperGroupLastChanged_Object=MibTableColumn
aluShaperGroupLastChanged=_AluShaperGroupLastChanged_Object((1,3,6,1,4,1,6527,6,1,2,2,5,10,1,6),_AluShaperGroupLastChanged_Type())
aluShaperGroupLastChanged.setMaxAccess(_I)
if mibBuilder.loadTexts:aluShaperGroupLastChanged.setStatus(_B)
class _AluShaperGroupCIRPercent_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,10000))
_AluShaperGroupCIRPercent_Type.__name__=_M
_AluShaperGroupCIRPercent_Object=MibTableColumn
aluShaperGroupCIRPercent=_AluShaperGroupCIRPercent_Object((1,3,6,1,4,1,6527,6,1,2,2,5,10,1,7),_AluShaperGroupCIRPercent_Type())
aluShaperGroupCIRPercent.setMaxAccess(_C)
if mibBuilder.loadTexts:aluShaperGroupCIRPercent.setStatus(_B)
if mibBuilder.loadTexts:aluShaperGroupCIRPercent.setUnits(_AK)
class _AluShaperGroupPIRPercent_Type(Unsigned32):defaultValue=10000;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,10000))
_AluShaperGroupPIRPercent_Type.__name__=_M
_AluShaperGroupPIRPercent_Object=MibTableColumn
aluShaperGroupPIRPercent=_AluShaperGroupPIRPercent_Object((1,3,6,1,4,1,6527,6,1,2,2,5,10,1,8),_AluShaperGroupPIRPercent_Type())
aluShaperGroupPIRPercent.setMaxAccess(_C)
if mibBuilder.loadTexts:aluShaperGroupPIRPercent.setStatus(_B)
if mibBuilder.loadTexts:aluShaperGroupPIRPercent.setUnits(_AK)
class _AluShaperGroupRateType_Type(TRateType):defaultValue=1
_AluShaperGroupRateType_Type.__name__=_AE
_AluShaperGroupRateType_Object=MibTableColumn
aluShaperGroupRateType=_AluShaperGroupRateType_Object((1,3,6,1,4,1,6527,6,1,2,2,5,10,1,9),_AluShaperGroupRateType_Type())
aluShaperGroupRateType.setMaxAccess(_C)
if mibBuilder.loadTexts:aluShaperGroupRateType.setStatus(_B)
_AluSecurityQueuePolicyTable_Object=MibTable
aluSecurityQueuePolicyTable=_AluSecurityQueuePolicyTable_Object((1,3,6,1,4,1,6527,6,1,2,2,5,11))
if mibBuilder.loadTexts:aluSecurityQueuePolicyTable.setStatus(_B)
_AluSecurityQueuePolicyEntry_Object=MibTableRow
aluSecurityQueuePolicyEntry=_AluSecurityQueuePolicyEntry_Object((1,3,6,1,4,1,6527,6,1,2,2,5,11,1))
aluSecurityQueuePolicyEntry.setIndexNames((0,_A,_T))
if mibBuilder.loadTexts:aluSecurityQueuePolicyEntry.setStatus(_B)
_AluSecurityQueuePolicyIndex_Type=TPolicyID
_AluSecurityQueuePolicyIndex_Object=MibTableColumn
aluSecurityQueuePolicyIndex=_AluSecurityQueuePolicyIndex_Object((1,3,6,1,4,1,6527,6,1,2,2,5,11,1,1),_AluSecurityQueuePolicyIndex_Type())
aluSecurityQueuePolicyIndex.setMaxAccess(_J)
if mibBuilder.loadTexts:aluSecurityQueuePolicyIndex.setStatus(_B)
_AluSecurityQueuePolicyRowStatus_Type=RowStatus
_AluSecurityQueuePolicyRowStatus_Object=MibTableColumn
aluSecurityQueuePolicyRowStatus=_AluSecurityQueuePolicyRowStatus_Object((1,3,6,1,4,1,6527,6,1,2,2,5,11,1,2),_AluSecurityQueuePolicyRowStatus_Type())
aluSecurityQueuePolicyRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:aluSecurityQueuePolicyRowStatus.setStatus(_B)
class _AluSecurityQueuePolicyDescription_Type(TItemDescription):defaultHexValue=''
_AluSecurityQueuePolicyDescription_Type.__name__=_L
_AluSecurityQueuePolicyDescription_Object=MibTableColumn
aluSecurityQueuePolicyDescription=_AluSecurityQueuePolicyDescription_Object((1,3,6,1,4,1,6527,6,1,2,2,5,11,1,3),_AluSecurityQueuePolicyDescription_Type())
aluSecurityQueuePolicyDescription.setMaxAccess(_C)
if mibBuilder.loadTexts:aluSecurityQueuePolicyDescription.setStatus(_B)
_AluSecurityQueuePolicyLastChanged_Type=TimeStamp
_AluSecurityQueuePolicyLastChanged_Object=MibTableColumn
aluSecurityQueuePolicyLastChanged=_AluSecurityQueuePolicyLastChanged_Object((1,3,6,1,4,1,6527,6,1,2,2,5,11,1,4),_AluSecurityQueuePolicyLastChanged_Type())
aluSecurityQueuePolicyLastChanged.setMaxAccess(_I)
if mibBuilder.loadTexts:aluSecurityQueuePolicyLastChanged.setStatus(_B)
_AluSecurityQueueTable_Object=MibTable
aluSecurityQueueTable=_AluSecurityQueueTable_Object((1,3,6,1,4,1,6527,6,1,2,2,5,12))
if mibBuilder.loadTexts:aluSecurityQueueTable.setStatus(_B)
_AluSecurityQueueEntry_Object=MibTableRow
aluSecurityQueueEntry=_AluSecurityQueueEntry_Object((1,3,6,1,4,1,6527,6,1,2,2,5,12,1))
aluSecurityQueueEntry.setIndexNames((0,_A,_T),(0,_A,_AL))
if mibBuilder.loadTexts:aluSecurityQueueEntry.setStatus(_B)
_AluSecurityQueueIndex_Type=AluSecQueueId
_AluSecurityQueueIndex_Object=MibTableColumn
aluSecurityQueueIndex=_AluSecurityQueueIndex_Object((1,3,6,1,4,1,6527,6,1,2,2,5,12,1,1),_AluSecurityQueueIndex_Type())
aluSecurityQueueIndex.setMaxAccess(_J)
if mibBuilder.loadTexts:aluSecurityQueueIndex.setStatus(_B)
class _AluSecurityQueueCIR_Type(TCIRRate):defaultValue=0
_AluSecurityQueueCIR_Type.__name__=_N
_AluSecurityQueueCIR_Object=MibTableColumn
aluSecurityQueueCIR=_AluSecurityQueueCIR_Object((1,3,6,1,4,1,6527,6,1,2,2,5,12,1,2),_AluSecurityQueueCIR_Type())
aluSecurityQueueCIR.setMaxAccess(_C)
if mibBuilder.loadTexts:aluSecurityQueueCIR.setStatus(_B)
if mibBuilder.loadTexts:aluSecurityQueueCIR.setUnits(_K)
class _AluSecurityQueuePIR_Type(TPIRRate):defaultValue=-1
_AluSecurityQueuePIR_Type.__name__=_O
_AluSecurityQueuePIR_Object=MibTableColumn
aluSecurityQueuePIR=_AluSecurityQueuePIR_Object((1,3,6,1,4,1,6527,6,1,2,2,5,12,1,3),_AluSecurityQueuePIR_Type())
aluSecurityQueuePIR.setMaxAccess(_C)
if mibBuilder.loadTexts:aluSecurityQueuePIR.setStatus(_B)
if mibBuilder.loadTexts:aluSecurityQueuePIR.setUnits(_K)
class _AluSecurityQueueCBS_Type(TBurstSize):defaultValue=-1
_AluSecurityQueueCBS_Type.__name__=_AC
_AluSecurityQueueCBS_Object=MibTableColumn
aluSecurityQueueCBS=_AluSecurityQueueCBS_Object((1,3,6,1,4,1,6527,6,1,2,2,5,12,1,4),_AluSecurityQueueCBS_Type())
aluSecurityQueueCBS.setMaxAccess(_C)
if mibBuilder.loadTexts:aluSecurityQueueCBS.setStatus(_B)
if mibBuilder.loadTexts:aluSecurityQueueCBS.setUnits('kilo-bytes')
class _AluSecurityQueueMBSBytes_Type(TBurstSizeBytes):defaultValue=500000
_AluSecurityQueueMBSBytes_Type.__name__=_AD
_AluSecurityQueueMBSBytes_Object=MibTableColumn
aluSecurityQueueMBSBytes=_AluSecurityQueueMBSBytes_Object((1,3,6,1,4,1,6527,6,1,2,2,5,12,1,5),_AluSecurityQueueMBSBytes_Type())
aluSecurityQueueMBSBytes.setMaxAccess(_C)
if mibBuilder.loadTexts:aluSecurityQueueMBSBytes.setStatus(_B)
if mibBuilder.loadTexts:aluSecurityQueueMBSBytes.setUnits('bytes')
class _AluSecurityQueueHiPrioOnly_Type(TBurstPercentOrDefault):defaultValue=10
_AluSecurityQueueHiPrioOnly_Type.__name__=_AB
_AluSecurityQueueHiPrioOnly_Object=MibTableColumn
aluSecurityQueueHiPrioOnly=_AluSecurityQueueHiPrioOnly_Object((1,3,6,1,4,1,6527,6,1,2,2,5,12,1,6),_AluSecurityQueueHiPrioOnly_Type())
aluSecurityQueueHiPrioOnly.setMaxAccess(_C)
if mibBuilder.loadTexts:aluSecurityQueueHiPrioOnly.setStatus(_B)
_AluSecurityQueueLastChanged_Type=TimeStamp
_AluSecurityQueueLastChanged_Object=MibTableColumn
aluSecurityQueueLastChanged=_AluSecurityQueueLastChanged_Object((1,3,6,1,4,1,6527,6,1,2,2,5,12,1,7),_AluSecurityQueueLastChanged_Type())
aluSecurityQueueLastChanged.setMaxAccess(_I)
if mibBuilder.loadTexts:aluSecurityQueueLastChanged.setStatus(_B)
_AluExtSapIngressTable_Object=MibTable
aluExtSapIngressTable=_AluExtSapIngressTable_Object((1,3,6,1,4,1,6527,6,1,2,2,5,13))
if mibBuilder.loadTexts:aluExtSapIngressTable.setStatus(_B)
_AluExtSapIngressEntry_Object=MibTableRow
aluExtSapIngressEntry=_AluExtSapIngressEntry_Object((1,3,6,1,4,1,6527,6,1,2,2,5,13,1))
if mibBuilder.loadTexts:aluExtSapIngressEntry.setStatus(_B)
class _AluSapIngressPktOffset_Type(AluPerPacketOffset):defaultValue=127
_AluSapIngressPktOffset_Type.__name__=_G
_AluSapIngressPktOffset_Object=MibTableColumn
aluSapIngressPktOffset=_AluSapIngressPktOffset_Object((1,3,6,1,4,1,6527,6,1,2,2,5,13,1,1),_AluSapIngressPktOffset_Type())
aluSapIngressPktOffset.setMaxAccess(_E)
if mibBuilder.loadTexts:aluSapIngressPktOffset.setStatus(_B)
_AluExtNetworkQueuePolicyTable_Object=MibTable
aluExtNetworkQueuePolicyTable=_AluExtNetworkQueuePolicyTable_Object((1,3,6,1,4,1,6527,6,1,2,2,5,14))
if mibBuilder.loadTexts:aluExtNetworkQueuePolicyTable.setStatus(_B)
_AluExtNetworkQueuePolicyEntry_Object=MibTableRow
aluExtNetworkQueuePolicyEntry=_AluExtNetworkQueuePolicyEntry_Object((1,3,6,1,4,1,6527,6,1,2,2,5,14,1))
if mibBuilder.loadTexts:aluExtNetworkQueuePolicyEntry.setStatus(_B)
class _AluNetworkQueuePolicyPktOffset_Type(AluPerPacketOffset):defaultValue=127
_AluNetworkQueuePolicyPktOffset_Type.__name__=_G
_AluNetworkQueuePolicyPktOffset_Object=MibTableColumn
aluNetworkQueuePolicyPktOffset=_AluNetworkQueuePolicyPktOffset_Object((1,3,6,1,4,1,6527,6,1,2,2,5,14,1,1),_AluNetworkQueuePolicyPktOffset_Type())
aluNetworkQueuePolicyPktOffset.setMaxAccess(_E)
if mibBuilder.loadTexts:aluNetworkQueuePolicyPktOffset.setStatus(_B)
tSapIngressQueueEntry.registerAugmentions((_A,_AM))
aluSapIngressQueueExtensionEntry.setIndexNames(*tSapIngressQueueEntry.getIndexNames())
tSapEgressQueueEntry.registerAugmentions((_A,_AN))
aluSapEgressQueueExtensionEntry.setIndexNames(*tSapEgressQueueEntry.getIndexNames())
tNetworkQueueEntry.registerAugmentions((_A,_AO))
aluNetworkQueueExtensionEntry.setIndexNames(*tNetworkQueueEntry.getIndexNames())
tSapEgressEntry.registerAugmentions((_A,_AP))
aluExtTSapEgressEntry.setIndexNames(*tSapEgressEntry.getIndexNames())
tNetworkPolicyEntry.registerAugmentions((_A,_AQ))
aluExtNetworkPolicyEntry.setIndexNames(*tNetworkPolicyEntry.getIndexNames())
tNetworkIngressDot1pEntry.registerAugmentions((_A,_AR))
aluExtNetworkIngressDot1pEntry.setIndexNames(*tNetworkIngressDot1pEntry.getIndexNames())
tSapIngressEntry.registerAugmentions((_A,_AS))
aluExtSapIngressEntry.setIndexNames(*tSapIngressEntry.getIndexNames())
tNetworkQueuePolicyEntry.registerAugmentions((_A,_AT))
aluExtNetworkQueuePolicyEntry.setIndexNames(*tNetworkQueuePolicyEntry.getIndexNames())
aluQosQueuePolicySlopePolicyGroup=ObjectGroup((1,3,6,1,4,1,6527,6,1,2,1,5,2,31))
aluQosQueuePolicySlopePolicyGroup.setObjects(*((_A,_AU),(_A,_AV),(_A,_AW)))
if mibBuilder.loadTexts:aluQosQueuePolicySlopePolicyGroup.setStatus(_B)
aluQosFabricProfileGroup=ObjectGroup((1,3,6,1,4,1,6527,6,1,2,1,5,2,32))
aluQosFabricProfileGroup.setObjects(*((_A,_U),(_A,_V),(_A,_W),(_A,_X),(_A,_Y),(_A,_Z),(_A,_a),(_A,_b),(_A,_c),(_A,_d),(_A,_e),(_A,_f),(_A,_g),(_A,_h),(_A,_i),(_A,_j),(_A,_k),(_A,_l),(_A,_m),(_A,_n),(_A,_o),(_A,_p),(_A,_q),(_A,_r),(_A,_s),(_A,_t),(_A,_u),(_A,_v),(_A,_w),(_A,_x),(_A,_y),(_A,_z),(_A,_A0),(_A,_A1),(_A,_A2),(_A,_A3),(_A,_A4)))
if mibBuilder.loadTexts:aluQosFabricProfileGroup.setStatus(_A5)
aluQosSapEgressPolicyTypeGroup=ObjectGroup((1,3,6,1,4,1,6527,6,1,2,1,5,2,33))
aluQosSapEgressPolicyTypeGroup.setObjects((_A,_AX))
if mibBuilder.loadTexts:aluQosSapEgressPolicyTypeGroup.setStatus(_B)
aluQosFabricProfileGroupV4v0=ObjectGroup((1,3,6,1,4,1,6527,6,1,2,1,5,2,34))
aluQosFabricProfileGroupV4v0.setObjects(*((_A,_U),(_A,_V),(_A,_W),(_A,_X),(_A,_Y),(_A,_Z),(_A,_a),(_A,_b),(_A,_c),(_A,_d),(_A,_e),(_A,_f),(_A,_g),(_A,_h),(_A,_i),(_A,_j),(_A,_k),(_A,_l),(_A,_m),(_A,_n),(_A,_o),(_A,_p),(_A,_q),(_A,_r),(_A,_s),(_A,_t),(_A,_u),(_A,_v),(_A,_w),(_A,_x),(_A,_y),(_A,_z),(_A,_A0),(_A,_A1),(_A,_A2),(_A,_A3),(_A,_A4),(_A,_AY)))
if mibBuilder.loadTexts:aluQosFabricProfileGroupV4v0.setStatus(_B)
aluSystemQosGroup=ObjectGroup((1,3,6,1,4,1,6527,6,1,2,1,5,2,35))
aluSystemQosGroup.setObjects(*((_A,_AZ),(_A,_Aa),(_A,_Ab)))
if mibBuilder.loadTexts:aluSystemQosGroup.setStatus(_B)
aluHQosGroup=ObjectGroup((1,3,6,1,4,1,6527,6,1,2,1,5,2,36))
aluHQosGroup.setObjects(*((_A,_Ac),(_A,_Ad)))
if mibBuilder.loadTexts:aluHQosGroup.setStatus(_B)
aluExtNetworkPolicyGroup=ObjectGroup((1,3,6,1,4,1,6527,6,1,2,1,5,2,37))
aluExtNetworkPolicyGroup.setObjects(*((_A,_Ae),(_A,_Af),(_A,_Ag)))
if mibBuilder.loadTexts:aluExtNetworkPolicyGroup.setStatus(_B)
aluQosShaperPolicyGroup=ObjectGroup((1,3,6,1,4,1,6527,6,1,2,1,5,2,38))
aluQosShaperPolicyGroup.setObjects(*((_A,_Ah),(_A,_Ai),(_A,_Aj),(_A,_Ak),(_A,_Al),(_A,_Am),(_A,_An),(_A,_Ao),(_A,_Ap),(_A,_Aq)))
if mibBuilder.loadTexts:aluQosShaperPolicyGroup.setStatus(_B)
aluSecurityQueueGroup=ObjectGroup((1,3,6,1,4,1,6527,6,1,2,1,5,2,39))
aluSecurityQueueGroup.setObjects(*((_A,_Ar),(_A,_As),(_A,_At),(_A,_Au),(_A,_Av),(_A,_Aw),(_A,_Ax),(_A,_Ay),(_A,_Az)))
if mibBuilder.loadTexts:aluSecurityQueueGroup.setStatus(_B)
aluExtQosV7v0Group=ObjectGroup((1,3,6,1,4,1,6527,6,1,2,1,5,2,40))
aluExtQosV7v0Group.setObjects(*((_A,_A_),(_A,_B0),(_A,_B1),(_A,_B2),(_A,_B3),(_A,_B4)))
if mibBuilder.loadTexts:aluExtQosV7v0Group.setStatus(_B)
aluQosV9v0Group=ObjectGroup((1,3,6,1,4,1,6527,6,1,2,1,5,2,41))
aluQosV9v0Group.setObjects(*((_A,_B5),(_A,_B6),(_A,_B7)))
if mibBuilder.loadTexts:aluQosV9v0Group.setStatus(_B)
aluQOSComp7705V1v0=ModuleCompliance((1,3,6,1,4,1,6527,6,1,2,1,5,1,1,1))
aluQOSComp7705V1v0.setObjects(*((_A,_A6),(_A,_A7),(_A,_A8)))
if mibBuilder.loadTexts:aluQOSComp7705V1v0.setStatus(_A5)
aluQOSComp7705V4v0=ModuleCompliance((1,3,6,1,4,1,6527,6,1,2,1,5,1,1,2))
aluQOSComp7705V4v0.setObjects((_A,_A9))
if mibBuilder.loadTexts:aluQOSComp7705V4v0.setStatus(_A5)
aluQOSComp7705V5v0=ModuleCompliance((1,3,6,1,4,1,6527,6,1,2,1,5,1,1,3))
aluQOSComp7705V5v0.setObjects(*((_A,_A6),(_A,_A7),(_A,_A8),(_A,_A9),(_A,_B8)))
if mibBuilder.loadTexts:aluQOSComp7705V5v0.setStatus(_B)
aluQOSComp7705V7v0=ModuleCompliance((1,3,6,1,4,1,6527,6,1,2,1,5,1,1,4))
aluQOSComp7705V7v0.setObjects(*((_A,_B9),(_A,_BA),(_A,_BB),(_A,_BC)))
if mibBuilder.loadTexts:aluQOSComp7705V7v0.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'AluIPsecStatsQueueId':AluIPsecStatsQueueId,'AluSecQueueId':AluSecQueueId,_AG:AluFabricProfilePolicyID,_AH:AluFabricProfileMode,_D:AluFabricProfileDestMdaRate,_Q:AluSapSchedulerCir,_R:AluSystemAggregateRate,_AI:AluExtNetworkPolicyType,_G:AluPerPacketOffset,'aluQOSMIBModule':aluQOSMIBModule,'aluQOSConformance':aluQOSConformance,'aluQOSCompliances':aluQOSCompliances,'aluQOSComp7705':aluQOSComp7705,'aluQOSComp7705V1v0':aluQOSComp7705V1v0,'aluQOSComp7705V4v0':aluQOSComp7705V4v0,'aluQOSComp7705V5v0':aluQOSComp7705V5v0,'aluQOSComp7705V7v0':aluQOSComp7705V7v0,'aluQOSGroups':aluQOSGroups,_A6:aluQosQueuePolicySlopePolicyGroup,_A7:aluQosFabricProfileGroup,_A8:aluQosSapEgressPolicyTypeGroup,_A9:aluQosFabricProfileGroupV4v0,_B8:aluSystemQosGroup,_B9:aluHQosGroup,_BA:aluExtNetworkPolicyGroup,_BB:aluQosShaperPolicyGroup,_BC:aluSecurityQueueGroup,'aluExtQosV7v0Group':aluExtQosV7v0Group,'aluQosV9v0Group':aluQosV9v0Group,'aluQOSObjs':aluQOSObjs,'aluSapIngressQueueExtensionTable':aluSapIngressQueueExtensionTable,_AM:aluSapIngressQueueExtensionEntry,_AU:aluSapIngressQueueSlopePolicy,_B2:aluSapIngressQueuePktOffset,'aluSapEgressQueueExtensionTable':aluSapEgressQueueExtensionTable,_AN:aluSapEgressQueueExtensionEntry,_AV:aluSapEgressQueueSlopePolicy,_B3:aluSapEgressQueuePktOffset,'aluNetworkQueueExtensionTable':aluNetworkQueueExtensionTable,_AO:aluNetworkQueueExtensionEntry,_AW:aluNetworkQueueSlopePolicy,_B4:aluNetworkQueuePktOffset,'aluFabricProfileTable':aluFabricProfileTable,'aluFabricProfileEntry':aluFabricProfileEntry,_AF:aluFabricProfileIndex,_U:aluFabricProfileRowStatus,_V:aluFabricProfileDescription,_W:aluFabricProfileRateToMdaIndex1,_X:aluFabricProfileRateToMdaIndex2,_Y:aluFabricProfileRateToMdaIndex3,_Z:aluFabricProfileRateToMdaIndex4,_a:aluFabricProfileRateToMdaIndex5,_b:aluFabricProfileRateToMdaIndex6,_c:aluFabricProfileRateToMdaIndex7,_d:aluFabricProfileRateToMdaIndex8,_e:aluFabricProfileRateToMdaIndex9,_f:aluFabricProfileRateToMdaIndex10,_g:aluFabricProfileRateToMdaIndex11,_h:aluFabricProfileRateToMdaIndex12,_i:aluFabricProfileRateToMdaIndex13,_j:aluFabricProfileRateToMdaIndex14,_k:aluFabricProfileRateToMdaIndex15,_l:aluFabricProfileRateToMdaIndex16,_m:aluFabricProfileRateToMdaIndex17,_n:aluFabricProfileRateToMdaIndex18,_o:aluFabricProfileRateToMdaIndex19,_p:aluFabricProfileRateToMdaIndex20,_q:aluFabricProfileRateToMdaIndex21,_r:aluFabricProfileRateToMdaIndex22,_s:aluFabricProfileRateToMdaIndex23,_t:aluFabricProfileRateToMdaIndex24,_u:aluFabricProfileRateToMdaIndex25,_v:aluFabricProfileRateToMdaIndex26,_w:aluFabricProfileRateToMdaIndex27,_x:aluFabricProfileRateToMdaIndex28,_y:aluFabricProfileRateToMdaIndex29,_z:aluFabricProfileRateToMdaIndex30,_A0:aluFabricProfileRateToMdaIndex31,_A1:aluFabricProfileRateToMdaIndex32,_A2:aluFabricProfileLastChanged,_A3:aluFabricProfileMode,_A4:aluFabricProfileAggregateRate,_AY:aluFabricProfileMultipointRate,_Ac:aluFabricProfileUnshapedSapCir,'aluExtTSapEgressTable':aluExtTSapEgressTable,_AP:aluExtTSapEgressEntry,_AX:aluSapEgressPolicyType,_B0:aluSapEgressPktOffset,'aluSystemQosConfig':aluSystemQosConfig,_AZ:aluSystemAccessIngAggRate,_Aa:aluSystemNetworkIngAggRate,_Ab:aluSystemQosLastChanged,_Ad:aluSystemIngUnshapedSapCir,'aluExtNetworkPolicyTable':aluExtNetworkPolicyTable,_AQ:aluExtNetworkPolicyEntry,_Ae:aluExtNetworkPolicyType,_Af:aluExtNetworkPolicyDefActionQueue,'aluExtNetworkIngressDot1pTable':aluExtNetworkIngressDot1pTable,_AR:aluExtNetworkIngressDot1pEntry,_Ag:aluExtNetworkRingDot1pQueue,'aluShaperPolicyTable':aluShaperPolicyTable,'aluShaperPolicyEntry':aluShaperPolicyEntry,_S:aluShaperPolicy,_Ah:aluShaperPolicyRowStatus,_Ai:aluShaperPolicyLastChanged,_Aj:aluShaperPolicyDescription,_Ak:aluShaperPolicyUnshapedSapGroup,_Al:aluShaperPolicyUnshapedIntfGroup,'aluShaperGroupTable':aluShaperGroupTable,'aluShaperGroupEntry':aluShaperGroupEntry,_AJ:aluShaperGroup,_Am:aluShaperGroupRowStatus,_An:aluShaperGroupDescription,_Ao:aluShaperGroupCIR,_Ap:aluShaperGroupPIR,_Aq:aluShaperGroupLastChanged,_B5:aluShaperGroupCIRPercent,_B6:aluShaperGroupPIRPercent,_B7:aluShaperGroupRateType,'aluSecurityQueuePolicyTable':aluSecurityQueuePolicyTable,'aluSecurityQueuePolicyEntry':aluSecurityQueuePolicyEntry,_T:aluSecurityQueuePolicyIndex,_Ar:aluSecurityQueuePolicyRowStatus,_As:aluSecurityQueuePolicyDescription,_At:aluSecurityQueuePolicyLastChanged,'aluSecurityQueueTable':aluSecurityQueueTable,'aluSecurityQueueEntry':aluSecurityQueueEntry,_AL:aluSecurityQueueIndex,_Au:aluSecurityQueueCIR,_Av:aluSecurityQueuePIR,_Aw:aluSecurityQueueCBS,_Ax:aluSecurityQueueMBSBytes,_Ay:aluSecurityQueueHiPrioOnly,_Az:aluSecurityQueueLastChanged,'aluExtSapIngressTable':aluExtSapIngressTable,_AS:aluExtSapIngressEntry,_A_:aluSapIngressPktOffset,'aluExtNetworkQueuePolicyTable':aluExtNetworkQueuePolicyTable,_AT:aluExtNetworkQueuePolicyEntry,_B1:aluNetworkQueuePolicyPktOffset})