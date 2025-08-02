_Aw='rcQosBandwidthCosBwpIndex'
_Av='rcQosBandwidthVlanHcBwpIndex'
_Au='rcQosBandwidthVlanHBwEnable'
_At='rcQosBandwidthVlanBwpIndex'
_As='rcQosBandwidthPortHvBwpIndex'
_Ar='rcQosBandwidthPortHBwEnable'
_Aq='rcQosBandwidthPortEgrBwpIndex'
_Ap='rcQosBandwidthPortBwpIndex'
_Ao='rcQosCosStatisticsDirection'
_An='rcQosCosStatisticsCos'
_Am='rcQosCosStatisticsVlan'
_Al='rcQosCosStatisticsPort'
_Ak='rcQosVlanStatisticsDirection'
_Aj='rcQosVlanStatisticsVlan'
_Ai='rcQosVlanStatisticsPort'
_Ah='rcQosTrafficStatsCmapName'
_Ag='rcQosTrafficStatsDirection'
_Af='rcQosTrafficStatsPort'
_Ae='rcQosHVlanBandwidthProfileVlan'
_Ad='rcQosHVlanBandwidthProfileIndex'
_Ac='rcQosHierarchyVlanIndex'
_Ab='rcQosHCosBandwidthProfileCos'
_Aa='rcQosHCosBandwidthProfileIndex'
_AZ='rcQosHierarchyCosIndex'
_AY='rcQosBandwidthProfileCfgIndex'
_AX='rcQosCosPolicyCos'
_AW='rcQosCosPolicyPmapName'
_AV='rcQosVlanPolicyVlan'
_AU='rcQosVlanPolicyPmapName'
_AT='rcQosCosServicePolicyVlan'
_AS='rcQosCosServicePolicyPort'
_AR='rcQosServicePolicyEgressIndex'
_AQ='rcQosActionCmapName'
_AP='rcQosActionPmapName'
_AO='color-aware'
_AN='color-blind'
_AM='rcQosPolicerCfgName'
_AL='rcQosMatchStmtValue'
_AK='rcQosMatchStmtType'
_AJ='rcQosMatchStmtClassName'
_AI='rcQosCMName'
_AH='rcQosPolicyMapName'
_AG='rcQosServicePolicyIngress'
_AF='rcQosPortWredProfileQueueId'
_AE='rcQosPortWredProfilePortId'
_AD='rcQosGloWredProfileQueueId'
_AC='rcQosWredProfileIndex'
_AB='rcQosCosRemarkLpri'
_AA='rcQosCosRemarkIndex'
_A9='rcQosDscpMutationDscp'
_A8='rcQosDscpMutationIndex'
_A7='rcQosDscpToPriDscp'
_A6='rcQosDscpToPriIndex'
_A5='rcQosTosToPriTos'
_A4='rcQosTosToPriIndex'
_A3='rcQosCosToPriCos'
_A2='rcQosCosToPriIndex'
_A1='rcQosPortStatisticsQueueId'
_A0='rcQosPortStatisticsPortId'
_z='rcQosPortDscpValue'
_y='rcQosPortDscpPortId'
_x='rcQosPortTosValue'
_w='rcQosPortTosPortId'
_v='rcQosPortCosValue'
_u='rcQosPortCosPortId'
_t='rcQosPortShapingQueueId'
_s='rcQosPortShapingPortId'
_r='rcQosShapingQueueId'
_q='rcQosPortWredQueueId'
_p='rcQosPortWredPortId'
_o='rcQosWredQueueId'
_n='rcQosSchedulerQueueId'
_m='rcQosDscpValue'
_l='rcQosTosValue'
_k='rcQosCosValue'
_j='rcQosLocalPriority'
_i='rcQosPortSchedulerQueueId'
_h='rcQosPortSchedulerPortId'
_g='rcQosPortCfgPortId'
_f='pkts'
_e='rcQosBandwidthCosPortType'
_d='rcQosBandwidthCosIndex'
_c='rcQosBandwidthCosVlan'
_b='rcQosBandwidthCosPort'
_a='rcQosBandwidthVlanPortType'
_Z='rcQosBandwidthVlanIndex'
_Y='rcQosBandwidthVlanPort'
_X='rcQosBandwidthPortIndex'
_W='queue-priority'
_V='frame-priority'
_U='dscp'
_T='cos'
_S='bytes'
_R='egress'
_Q='ingress'
_P='none'
_O='disable'
_N='enable'
_M='both'
_L='null'
_K='red'
_J='yellow'
_I='green'
_H='OctetString'
_G='read-only'
_F='not-accessible'
_E='read-write'
_D='RAISECOM-QOS-MIB'
_C='Integer32'
_B='read-create'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_H,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress','InetAddressType')
raisecomAgent,=mibBuilder.importSymbols('RAISECOM-BASE-MIB','raisecomAgent')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress','RowStatus','TextualConvention','TruthValue')
EnableVar,ObjName,PortList,Vlanset=mibBuilder.importSymbols('SWITCH-TC','EnableVar','ObjName','PortList','Vlanset')
raisecomQosMIB=ModuleIdentity((1,3,6,1,4,1,8886,1,33))
if mibBuilder.loadTexts:raisecomQosMIB.setRevisions(('2009-03-20 00:00',))
_RaisecomQosCfg_ObjectIdentity=ObjectIdentity
raisecomQosCfg=_RaisecomQosCfg_ObjectIdentity((1,3,6,1,4,1,8886,1,33,1))
_RcQosEnable_Type=EnableVar
_RcQosEnable_Object=MibScalar
rcQosEnable=_RcQosEnable_Object((1,3,6,1,4,1,8886,1,33,1,1),_RcQosEnable_Type())
rcQosEnable.setMaxAccess(_E)
if mibBuilder.loadTexts:rcQosEnable.setStatus(_A)
class _RcQosTrust_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('port-prio',1),(_T,2),('tos',3),(_U,4)))
_RcQosTrust_Type.__name__=_C
_RcQosTrust_Object=MibScalar
rcQosTrust=_RcQosTrust_Object((1,3,6,1,4,1,8886,1,33,1,2),_RcQosTrust_Type())
rcQosTrust.setMaxAccess(_E)
if mibBuilder.loadTexts:rcQosTrust.setStatus(_A)
class _RcQosQueueScheduler_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('sp',1),('wrr',2),('drr',3),('wfq',4)))
_RcQosQueueScheduler_Type.__name__=_C
_RcQosQueueScheduler_Object=MibScalar
rcQosQueueScheduler=_RcQosQueueScheduler_Object((1,3,6,1,4,1,8886,1,33,1,3),_RcQosQueueScheduler_Type())
rcQosQueueScheduler.setMaxAccess(_E)
if mibBuilder.loadTexts:rcQosQueueScheduler.setStatus(_A)
_RcQosWredEnable_Type=EnableVar
_RcQosWredEnable_Object=MibScalar
rcQosWredEnable=_RcQosWredEnable_Object((1,3,6,1,4,1,8886,1,33,1,4),_RcQosWredEnable_Type())
rcQosWredEnable.setMaxAccess(_E)
if mibBuilder.loadTexts:rcQosWredEnable.setStatus(_A)
_RcQosCos2PriProfile_Type=Integer32
_RcQosCos2PriProfile_Object=MibScalar
rcQosCos2PriProfile=_RcQosCos2PriProfile_Object((1,3,6,1,4,1,8886,1,33,1,5),_RcQosCos2PriProfile_Type())
rcQosCos2PriProfile.setMaxAccess(_E)
if mibBuilder.loadTexts:rcQosCos2PriProfile.setStatus(_A)
_RcQosTos2PriProfile_Type=Integer32
_RcQosTos2PriProfile_Object=MibScalar
rcQosTos2PriProfile=_RcQosTos2PriProfile_Object((1,3,6,1,4,1,8886,1,33,1,6),_RcQosTos2PriProfile_Type())
rcQosTos2PriProfile.setMaxAccess(_E)
if mibBuilder.loadTexts:rcQosTos2PriProfile.setStatus(_A)
_RcQosDscp2PriProfile_Type=Integer32
_RcQosDscp2PriProfile_Object=MibScalar
rcQosDscp2PriProfile=_RcQosDscp2PriProfile_Object((1,3,6,1,4,1,8886,1,33,1,7),_RcQosDscp2PriProfile_Type())
rcQosDscp2PriProfile.setMaxAccess(_E)
if mibBuilder.loadTexts:rcQosDscp2PriProfile.setStatus(_A)
_RcQosDscpMutationProfile_Type=Integer32
_RcQosDscpMutationProfile_Object=MibScalar
rcQosDscpMutationProfile=_RcQosDscpMutationProfile_Object((1,3,6,1,4,1,8886,1,33,1,8),_RcQosDscpMutationProfile_Type())
rcQosDscpMutationProfile.setMaxAccess(_E)
if mibBuilder.loadTexts:rcQosDscpMutationProfile.setStatus(_A)
_RcQosCosRemarkProfile_Type=Integer32
_RcQosCosRemarkProfile_Object=MibScalar
rcQosCosRemarkProfile=_RcQosCosRemarkProfile_Object((1,3,6,1,4,1,8886,1,33,1,9),_RcQosCosRemarkProfile_Type())
rcQosCosRemarkProfile.setMaxAccess(_E)
if mibBuilder.loadTexts:rcQosCosRemarkProfile.setStatus(_A)
_RcQosPortCfgTable_Object=MibTable
rcQosPortCfgTable=_RcQosPortCfgTable_Object((1,3,6,1,4,1,8886,1,33,1,10))
if mibBuilder.loadTexts:rcQosPortCfgTable.setStatus(_A)
_RcQosPortCfgEntry_Object=MibTableRow
rcQosPortCfgEntry=_RcQosPortCfgEntry_Object((1,3,6,1,4,1,8886,1,33,1,10,1))
rcQosPortCfgEntry.setIndexNames((0,_D,_g))
if mibBuilder.loadTexts:rcQosPortCfgEntry.setStatus(_A)
_RcQosPortCfgPortId_Type=Integer32
_RcQosPortCfgPortId_Object=MibTableColumn
rcQosPortCfgPortId=_RcQosPortCfgPortId_Object((1,3,6,1,4,1,8886,1,33,1,10,1,1),_RcQosPortCfgPortId_Type())
rcQosPortCfgPortId.setMaxAccess(_F)
if mibBuilder.loadTexts:rcQosPortCfgPortId.setStatus(_A)
class _RcQosPortCfgTrust_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('port-priority',1),(_T,2),('tos',3),(_U,4),('cos-inner',5)))
_RcQosPortCfgTrust_Type.__name__=_C
_RcQosPortCfgTrust_Object=MibTableColumn
rcQosPortCfgTrust=_RcQosPortCfgTrust_Object((1,3,6,1,4,1,8886,1,33,1,10,1,2),_RcQosPortCfgTrust_Type())
rcQosPortCfgTrust.setMaxAccess(_E)
if mibBuilder.loadTexts:rcQosPortCfgTrust.setStatus(_A)
_RcQosPortCfgPriority_Type=Integer32
_RcQosPortCfgPriority_Object=MibTableColumn
rcQosPortCfgPriority=_RcQosPortCfgPriority_Object((1,3,6,1,4,1,8886,1,33,1,10,1,3),_RcQosPortCfgPriority_Type())
rcQosPortCfgPriority.setMaxAccess(_E)
if mibBuilder.loadTexts:rcQosPortCfgPriority.setStatus(_A)
_RcQosPortCfgPriorityOverride_Type=EnableVar
_RcQosPortCfgPriorityOverride_Object=MibTableColumn
rcQosPortCfgPriorityOverride=_RcQosPortCfgPriorityOverride_Object((1,3,6,1,4,1,8886,1,33,1,10,1,4),_RcQosPortCfgPriorityOverride_Type())
rcQosPortCfgPriorityOverride.setMaxAccess(_E)
if mibBuilder.loadTexts:rcQosPortCfgPriorityOverride.setStatus(_A)
class _RcQosPortCfgQueueScheduler_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('sp',1),('wrr',2),('drr',3),('wfq',4)))
_RcQosPortCfgQueueScheduler_Type.__name__=_C
_RcQosPortCfgQueueScheduler_Object=MibTableColumn
rcQosPortCfgQueueScheduler=_RcQosPortCfgQueueScheduler_Object((1,3,6,1,4,1,8886,1,33,1,10,1,5),_RcQosPortCfgQueueScheduler_Type())
rcQosPortCfgQueueScheduler.setMaxAccess(_E)
if mibBuilder.loadTexts:rcQosPortCfgQueueScheduler.setStatus(_A)
class _RcQosPortCfgSmacPriorityOverride_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*((_L,0),(_V,1),(_W,2),(_M,3)))
_RcQosPortCfgSmacPriorityOverride_Type.__name__=_C
_RcQosPortCfgSmacPriorityOverride_Object=MibTableColumn
rcQosPortCfgSmacPriorityOverride=_RcQosPortCfgSmacPriorityOverride_Object((1,3,6,1,4,1,8886,1,33,1,10,1,6),_RcQosPortCfgSmacPriorityOverride_Type())
rcQosPortCfgSmacPriorityOverride.setMaxAccess(_E)
if mibBuilder.loadTexts:rcQosPortCfgSmacPriorityOverride.setStatus(_A)
class _RcQosPortCfgDmacPriorityOverride_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*((_L,0),(_V,1),(_W,2),(_M,3)))
_RcQosPortCfgDmacPriorityOverride_Type.__name__=_C
_RcQosPortCfgDmacPriorityOverride_Object=MibTableColumn
rcQosPortCfgDmacPriorityOverride=_RcQosPortCfgDmacPriorityOverride_Object((1,3,6,1,4,1,8886,1,33,1,10,1,7),_RcQosPortCfgDmacPriorityOverride_Type())
rcQosPortCfgDmacPriorityOverride.setMaxAccess(_E)
if mibBuilder.loadTexts:rcQosPortCfgDmacPriorityOverride.setStatus(_A)
class _RcQosPortCfgVlanPriorityOverride_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*((_L,0),(_V,1),(_W,2),(_M,3)))
_RcQosPortCfgVlanPriorityOverride_Type.__name__=_C
_RcQosPortCfgVlanPriorityOverride_Object=MibTableColumn
rcQosPortCfgVlanPriorityOverride=_RcQosPortCfgVlanPriorityOverride_Object((1,3,6,1,4,1,8886,1,33,1,10,1,8),_RcQosPortCfgVlanPriorityOverride_Type())
rcQosPortCfgVlanPriorityOverride.setMaxAccess(_E)
if mibBuilder.loadTexts:rcQosPortCfgVlanPriorityOverride.setStatus(_A)
_RcQosPortCos2PriProfile_Type=Integer32
_RcQosPortCos2PriProfile_Object=MibTableColumn
rcQosPortCos2PriProfile=_RcQosPortCos2PriProfile_Object((1,3,6,1,4,1,8886,1,33,1,10,1,9),_RcQosPortCos2PriProfile_Type())
rcQosPortCos2PriProfile.setMaxAccess(_E)
if mibBuilder.loadTexts:rcQosPortCos2PriProfile.setStatus(_A)
_RcQosPortTos2PriProfile_Type=Integer32
_RcQosPortTos2PriProfile_Object=MibTableColumn
rcQosPortTos2PriProfile=_RcQosPortTos2PriProfile_Object((1,3,6,1,4,1,8886,1,33,1,10,1,10),_RcQosPortTos2PriProfile_Type())
rcQosPortTos2PriProfile.setMaxAccess(_E)
if mibBuilder.loadTexts:rcQosPortTos2PriProfile.setStatus(_A)
_RcQosPortDscp2PriProfile_Type=Integer32
_RcQosPortDscp2PriProfile_Object=MibTableColumn
rcQosPortDscp2PriProfile=_RcQosPortDscp2PriProfile_Object((1,3,6,1,4,1,8886,1,33,1,10,1,11),_RcQosPortDscp2PriProfile_Type())
rcQosPortDscp2PriProfile.setMaxAccess(_E)
if mibBuilder.loadTexts:rcQosPortDscp2PriProfile.setStatus(_A)
_RcQosPortDscpMutationProfile_Type=Integer32
_RcQosPortDscpMutationProfile_Object=MibTableColumn
rcQosPortDscpMutationProfile=_RcQosPortDscpMutationProfile_Object((1,3,6,1,4,1,8886,1,33,1,10,1,12),_RcQosPortDscpMutationProfile_Type())
rcQosPortDscpMutationProfile.setMaxAccess(_E)
if mibBuilder.loadTexts:rcQosPortDscpMutationProfile.setStatus(_A)
_RcQosPortCosRemarkProfile_Type=Integer32
_RcQosPortCosRemarkProfile_Object=MibTableColumn
rcQosPortCosRemarkProfile=_RcQosPortCosRemarkProfile_Object((1,3,6,1,4,1,8886,1,33,1,10,1,13),_RcQosPortCosRemarkProfile_Type())
rcQosPortCosRemarkProfile.setMaxAccess(_E)
if mibBuilder.loadTexts:rcQosPortCosRemarkProfile.setStatus(_A)
_RcQosPortSchedulerQueueTable_Object=MibTable
rcQosPortSchedulerQueueTable=_RcQosPortSchedulerQueueTable_Object((1,3,6,1,4,1,8886,1,33,1,11))
if mibBuilder.loadTexts:rcQosPortSchedulerQueueTable.setStatus(_A)
_RcQosPortSchedulerQueueEntry_Object=MibTableRow
rcQosPortSchedulerQueueEntry=_RcQosPortSchedulerQueueEntry_Object((1,3,6,1,4,1,8886,1,33,1,11,1))
rcQosPortSchedulerQueueEntry.setIndexNames((0,_D,_h),(0,_D,_i))
if mibBuilder.loadTexts:rcQosPortSchedulerQueueEntry.setStatus(_A)
_RcQosPortSchedulerPortId_Type=Integer32
_RcQosPortSchedulerPortId_Object=MibTableColumn
rcQosPortSchedulerPortId=_RcQosPortSchedulerPortId_Object((1,3,6,1,4,1,8886,1,33,1,11,1,1),_RcQosPortSchedulerPortId_Type())
rcQosPortSchedulerPortId.setMaxAccess(_F)
if mibBuilder.loadTexts:rcQosPortSchedulerPortId.setStatus(_A)
_RcQosPortSchedulerQueueId_Type=Integer32
_RcQosPortSchedulerQueueId_Object=MibTableColumn
rcQosPortSchedulerQueueId=_RcQosPortSchedulerQueueId_Object((1,3,6,1,4,1,8886,1,33,1,11,1,2),_RcQosPortSchedulerQueueId_Type())
rcQosPortSchedulerQueueId.setMaxAccess(_F)
if mibBuilder.loadTexts:rcQosPortSchedulerQueueId.setStatus(_A)
_RcQosPortSchedulerWRR_Type=Integer32
_RcQosPortSchedulerWRR_Object=MibTableColumn
rcQosPortSchedulerWRR=_RcQosPortSchedulerWRR_Object((1,3,6,1,4,1,8886,1,33,1,11,1,3),_RcQosPortSchedulerWRR_Type())
rcQosPortSchedulerWRR.setMaxAccess(_E)
if mibBuilder.loadTexts:rcQosPortSchedulerWRR.setStatus(_A)
_RcQosPortSchedulerDRR_Type=Integer32
_RcQosPortSchedulerDRR_Object=MibTableColumn
rcQosPortSchedulerDRR=_RcQosPortSchedulerDRR_Object((1,3,6,1,4,1,8886,1,33,1,11,1,4),_RcQosPortSchedulerDRR_Type())
rcQosPortSchedulerDRR.setMaxAccess(_E)
if mibBuilder.loadTexts:rcQosPortSchedulerDRR.setStatus(_A)
_RcQosPortSchedulerWFQ_Type=Integer32
_RcQosPortSchedulerWFQ_Object=MibTableColumn
rcQosPortSchedulerWFQ=_RcQosPortSchedulerWFQ_Object((1,3,6,1,4,1,8886,1,33,1,11,1,5),_RcQosPortSchedulerWFQ_Type())
rcQosPortSchedulerWFQ.setMaxAccess(_E)
if mibBuilder.loadTexts:rcQosPortSchedulerWFQ.setStatus(_A)
_RcQosLocalPrioMappingTable_Object=MibTable
rcQosLocalPrioMappingTable=_RcQosLocalPrioMappingTable_Object((1,3,6,1,4,1,8886,1,33,1,12))
if mibBuilder.loadTexts:rcQosLocalPrioMappingTable.setStatus(_A)
_RcQosLocalPrioMappingEntry_Object=MibTableRow
rcQosLocalPrioMappingEntry=_RcQosLocalPrioMappingEntry_Object((1,3,6,1,4,1,8886,1,33,1,12,1))
rcQosLocalPrioMappingEntry.setIndexNames((0,_D,_j))
if mibBuilder.loadTexts:rcQosLocalPrioMappingEntry.setStatus(_A)
class _RcQosLocalPriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_RcQosLocalPriority_Type.__name__=_C
_RcQosLocalPriority_Object=MibTableColumn
rcQosLocalPriority=_RcQosLocalPriority_Object((1,3,6,1,4,1,8886,1,33,1,12,1,1),_RcQosLocalPriority_Type())
rcQosLocalPriority.setMaxAccess(_F)
if mibBuilder.loadTexts:rcQosLocalPriority.setStatus(_A)
class _RcQosQueueId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_RcQosQueueId_Type.__name__=_C
_RcQosQueueId_Object=MibTableColumn
rcQosQueueId=_RcQosQueueId_Object((1,3,6,1,4,1,8886,1,33,1,12,1,2),_RcQosQueueId_Type())
rcQosQueueId.setMaxAccess(_G)
if mibBuilder.loadTexts:rcQosQueueId.setStatus(_A)
_RcQosCosMappingTable_Object=MibTable
rcQosCosMappingTable=_RcQosCosMappingTable_Object((1,3,6,1,4,1,8886,1,33,1,13))
if mibBuilder.loadTexts:rcQosCosMappingTable.setStatus(_A)
_RcQosCosMappingEntry_Object=MibTableRow
rcQosCosMappingEntry=_RcQosCosMappingEntry_Object((1,3,6,1,4,1,8886,1,33,1,13,1))
rcQosCosMappingEntry.setIndexNames((0,_D,_k))
if mibBuilder.loadTexts:rcQosCosMappingEntry.setStatus(_A)
class _RcQosCosValue_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_RcQosCosValue_Type.__name__=_C
_RcQosCosValue_Object=MibTableColumn
rcQosCosValue=_RcQosCosValue_Object((1,3,6,1,4,1,8886,1,33,1,13,1,1),_RcQosCosValue_Type())
rcQosCosValue.setMaxAccess(_F)
if mibBuilder.loadTexts:rcQosCosValue.setStatus(_A)
class _RcQosCosLocalPriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_RcQosCosLocalPriority_Type.__name__=_C
_RcQosCosLocalPriority_Object=MibTableColumn
rcQosCosLocalPriority=_RcQosCosLocalPriority_Object((1,3,6,1,4,1,8886,1,33,1,13,1,2),_RcQosCosLocalPriority_Type())
rcQosCosLocalPriority.setMaxAccess(_E)
if mibBuilder.loadTexts:rcQosCosLocalPriority.setStatus(_A)
class _RcQosCosColor_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*((_L,0),(_I,1),(_J,2),(_K,3)))
_RcQosCosColor_Type.__name__=_C
_RcQosCosColor_Object=MibTableColumn
rcQosCosColor=_RcQosCosColor_Object((1,3,6,1,4,1,8886,1,33,1,13,1,3),_RcQosCosColor_Type())
rcQosCosColor.setMaxAccess(_E)
if mibBuilder.loadTexts:rcQosCosColor.setStatus(_A)
_RcQosTosMappingTable_Object=MibTable
rcQosTosMappingTable=_RcQosTosMappingTable_Object((1,3,6,1,4,1,8886,1,33,1,14))
if mibBuilder.loadTexts:rcQosTosMappingTable.setStatus(_A)
_RcQosTosMappingEntry_Object=MibTableRow
rcQosTosMappingEntry=_RcQosTosMappingEntry_Object((1,3,6,1,4,1,8886,1,33,1,14,1))
rcQosTosMappingEntry.setIndexNames((0,_D,_l))
if mibBuilder.loadTexts:rcQosTosMappingEntry.setStatus(_A)
class _RcQosTosValue_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_RcQosTosValue_Type.__name__=_C
_RcQosTosValue_Object=MibTableColumn
rcQosTosValue=_RcQosTosValue_Object((1,3,6,1,4,1,8886,1,33,1,14,1,1),_RcQosTosValue_Type())
rcQosTosValue.setMaxAccess(_F)
if mibBuilder.loadTexts:rcQosTosValue.setStatus(_A)
class _RcQosTosLocalPriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_RcQosTosLocalPriority_Type.__name__=_C
_RcQosTosLocalPriority_Object=MibTableColumn
rcQosTosLocalPriority=_RcQosTosLocalPriority_Object((1,3,6,1,4,1,8886,1,33,1,14,1,2),_RcQosTosLocalPriority_Type())
rcQosTosLocalPriority.setMaxAccess(_E)
if mibBuilder.loadTexts:rcQosTosLocalPriority.setStatus(_A)
class _RcQosTosColor_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*((_L,0),(_I,1),(_J,2),(_K,3)))
_RcQosTosColor_Type.__name__=_C
_RcQosTosColor_Object=MibTableColumn
rcQosTosColor=_RcQosTosColor_Object((1,3,6,1,4,1,8886,1,33,1,14,1,3),_RcQosTosColor_Type())
rcQosTosColor.setMaxAccess(_E)
if mibBuilder.loadTexts:rcQosTosColor.setStatus(_A)
_RcQosDscpMapingTable_Object=MibTable
rcQosDscpMapingTable=_RcQosDscpMapingTable_Object((1,3,6,1,4,1,8886,1,33,1,15))
if mibBuilder.loadTexts:rcQosDscpMapingTable.setStatus(_A)
_RcQosDscpMapingEntry_Object=MibTableRow
rcQosDscpMapingEntry=_RcQosDscpMapingEntry_Object((1,3,6,1,4,1,8886,1,33,1,15,1))
rcQosDscpMapingEntry.setIndexNames((0,_D,_m))
if mibBuilder.loadTexts:rcQosDscpMapingEntry.setStatus(_A)
class _RcQosDscpValue_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,63))
_RcQosDscpValue_Type.__name__=_C
_RcQosDscpValue_Object=MibTableColumn
rcQosDscpValue=_RcQosDscpValue_Object((1,3,6,1,4,1,8886,1,33,1,15,1,1),_RcQosDscpValue_Type())
rcQosDscpValue.setMaxAccess(_F)
if mibBuilder.loadTexts:rcQosDscpValue.setStatus(_A)
class _RcQosDscpLocalPriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_RcQosDscpLocalPriority_Type.__name__=_C
_RcQosDscpLocalPriority_Object=MibTableColumn
rcQosDscpLocalPriority=_RcQosDscpLocalPriority_Object((1,3,6,1,4,1,8886,1,33,1,15,1,2),_RcQosDscpLocalPriority_Type())
rcQosDscpLocalPriority.setMaxAccess(_E)
if mibBuilder.loadTexts:rcQosDscpLocalPriority.setStatus(_A)
class _RcQosDscpColor_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*((_L,0),(_I,1),(_J,2),(_K,3)))
_RcQosDscpColor_Type.__name__=_C
_RcQosDscpColor_Object=MibTableColumn
rcQosDscpColor=_RcQosDscpColor_Object((1,3,6,1,4,1,8886,1,33,1,15,1,3),_RcQosDscpColor_Type())
rcQosDscpColor.setMaxAccess(_E)
if mibBuilder.loadTexts:rcQosDscpColor.setStatus(_A)
_RcQosSchedulerQueueTable_Object=MibTable
rcQosSchedulerQueueTable=_RcQosSchedulerQueueTable_Object((1,3,6,1,4,1,8886,1,33,1,16))
if mibBuilder.loadTexts:rcQosSchedulerQueueTable.setStatus(_A)
_RcQosSchedulerQueueEntry_Object=MibTableRow
rcQosSchedulerQueueEntry=_RcQosSchedulerQueueEntry_Object((1,3,6,1,4,1,8886,1,33,1,16,1))
rcQosSchedulerQueueEntry.setIndexNames((0,_D,_n))
if mibBuilder.loadTexts:rcQosSchedulerQueueEntry.setStatus(_A)
_RcQosSchedulerQueueId_Type=Integer32
_RcQosSchedulerQueueId_Object=MibTableColumn
rcQosSchedulerQueueId=_RcQosSchedulerQueueId_Object((1,3,6,1,4,1,8886,1,33,1,16,1,1),_RcQosSchedulerQueueId_Type())
rcQosSchedulerQueueId.setMaxAccess(_F)
if mibBuilder.loadTexts:rcQosSchedulerQueueId.setStatus(_A)
_RcQosSchedulerWRR_Type=Integer32
_RcQosSchedulerWRR_Object=MibTableColumn
rcQosSchedulerWRR=_RcQosSchedulerWRR_Object((1,3,6,1,4,1,8886,1,33,1,16,1,2),_RcQosSchedulerWRR_Type())
rcQosSchedulerWRR.setMaxAccess(_E)
if mibBuilder.loadTexts:rcQosSchedulerWRR.setStatus(_A)
_RcQosSchedulerDRR_Type=Integer32
_RcQosSchedulerDRR_Object=MibTableColumn
rcQosSchedulerDRR=_RcQosSchedulerDRR_Object((1,3,6,1,4,1,8886,1,33,1,16,1,3),_RcQosSchedulerDRR_Type())
rcQosSchedulerDRR.setMaxAccess(_E)
if mibBuilder.loadTexts:rcQosSchedulerDRR.setStatus(_A)
_RcQosSchedulerWFQ_Type=Integer32
_RcQosSchedulerWFQ_Object=MibTableColumn
rcQosSchedulerWFQ=_RcQosSchedulerWFQ_Object((1,3,6,1,4,1,8886,1,33,1,16,1,4),_RcQosSchedulerWFQ_Type())
rcQosSchedulerWFQ.setMaxAccess(_E)
if mibBuilder.loadTexts:rcQosSchedulerWFQ.setStatus(_A)
_RcQosWredTcpConfigTable_Object=MibTable
rcQosWredTcpConfigTable=_RcQosWredTcpConfigTable_Object((1,3,6,1,4,1,8886,1,33,1,17))
if mibBuilder.loadTexts:rcQosWredTcpConfigTable.setStatus(_A)
_RcQosWredTcpConfigEntry_Object=MibTableRow
rcQosWredTcpConfigEntry=_RcQosWredTcpConfigEntry_Object((1,3,6,1,4,1,8886,1,33,1,17,1))
rcQosWredTcpConfigEntry.setIndexNames((0,_D,_o))
if mibBuilder.loadTexts:rcQosWredTcpConfigEntry.setStatus(_A)
_RcQosWredQueueId_Type=Integer32
_RcQosWredQueueId_Object=MibTableColumn
rcQosWredQueueId=_RcQosWredQueueId_Object((1,3,6,1,4,1,8886,1,33,1,17,1,1),_RcQosWredQueueId_Type())
rcQosWredQueueId.setMaxAccess(_F)
if mibBuilder.loadTexts:rcQosWredQueueId.setStatus(_A)
_RcQosWredGreenDropStartPoint_Type=Integer32
_RcQosWredGreenDropStartPoint_Object=MibTableColumn
rcQosWredGreenDropStartPoint=_RcQosWredGreenDropStartPoint_Object((1,3,6,1,4,1,8886,1,33,1,17,1,2),_RcQosWredGreenDropStartPoint_Type())
rcQosWredGreenDropStartPoint.setMaxAccess(_E)
if mibBuilder.loadTexts:rcQosWredGreenDropStartPoint.setStatus(_A)
_RcQosWredGreenDropEndPoint_Type=Integer32
_RcQosWredGreenDropEndPoint_Object=MibTableColumn
rcQosWredGreenDropEndPoint=_RcQosWredGreenDropEndPoint_Object((1,3,6,1,4,1,8886,1,33,1,17,1,3),_RcQosWredGreenDropEndPoint_Type())
rcQosWredGreenDropEndPoint.setMaxAccess(_E)
if mibBuilder.loadTexts:rcQosWredGreenDropEndPoint.setStatus(_A)
_RcQosWredGreenDropProbability_Type=Integer32
_RcQosWredGreenDropProbability_Object=MibTableColumn
rcQosWredGreenDropProbability=_RcQosWredGreenDropProbability_Object((1,3,6,1,4,1,8886,1,33,1,17,1,4),_RcQosWredGreenDropProbability_Type())
rcQosWredGreenDropProbability.setMaxAccess(_E)
if mibBuilder.loadTexts:rcQosWredGreenDropProbability.setStatus(_A)
_RcQosWredYellowDropStartPoint_Type=Integer32
_RcQosWredYellowDropStartPoint_Object=MibTableColumn
rcQosWredYellowDropStartPoint=_RcQosWredYellowDropStartPoint_Object((1,3,6,1,4,1,8886,1,33,1,17,1,5),_RcQosWredYellowDropStartPoint_Type())
rcQosWredYellowDropStartPoint.setMaxAccess(_E)
if mibBuilder.loadTexts:rcQosWredYellowDropStartPoint.setStatus(_A)
_RcQosWredYellowDropEndPoint_Type=Integer32
_RcQosWredYellowDropEndPoint_Object=MibTableColumn
rcQosWredYellowDropEndPoint=_RcQosWredYellowDropEndPoint_Object((1,3,6,1,4,1,8886,1,33,1,17,1,6),_RcQosWredYellowDropEndPoint_Type())
rcQosWredYellowDropEndPoint.setMaxAccess(_E)
if mibBuilder.loadTexts:rcQosWredYellowDropEndPoint.setStatus(_A)
_RcQosWredYellowDropProbability_Type=Integer32
_RcQosWredYellowDropProbability_Object=MibTableColumn
rcQosWredYellowDropProbability=_RcQosWredYellowDropProbability_Object((1,3,6,1,4,1,8886,1,33,1,17,1,7),_RcQosWredYellowDropProbability_Type())
rcQosWredYellowDropProbability.setMaxAccess(_E)
if mibBuilder.loadTexts:rcQosWredYellowDropProbability.setStatus(_A)
_RcQosWredRedDropStartPoint_Type=Integer32
_RcQosWredRedDropStartPoint_Object=MibTableColumn
rcQosWredRedDropStartPoint=_RcQosWredRedDropStartPoint_Object((1,3,6,1,4,1,8886,1,33,1,17,1,8),_RcQosWredRedDropStartPoint_Type())
rcQosWredRedDropStartPoint.setMaxAccess(_E)
if mibBuilder.loadTexts:rcQosWredRedDropStartPoint.setStatus(_A)
_RcQosWredRedDropEndPoint_Type=Integer32
_RcQosWredRedDropEndPoint_Object=MibTableColumn
rcQosWredRedDropEndPoint=_RcQosWredRedDropEndPoint_Object((1,3,6,1,4,1,8886,1,33,1,17,1,9),_RcQosWredRedDropEndPoint_Type())
rcQosWredRedDropEndPoint.setMaxAccess(_E)
if mibBuilder.loadTexts:rcQosWredRedDropEndPoint.setStatus(_A)
_RcQosWredRedDropProbability_Type=Integer32
_RcQosWredRedDropProbability_Object=MibTableColumn
rcQosWredRedDropProbability=_RcQosWredRedDropProbability_Object((1,3,6,1,4,1,8886,1,33,1,17,1,10),_RcQosWredRedDropProbability_Type())
rcQosWredRedDropProbability.setMaxAccess(_E)
if mibBuilder.loadTexts:rcQosWredRedDropProbability.setStatus(_A)
class _RcQosWredStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_N,1),(_O,2)))
_RcQosWredStatus_Type.__name__=_C
_RcQosWredStatus_Object=MibTableColumn
rcQosWredStatus=_RcQosWredStatus_Object((1,3,6,1,4,1,8886,1,33,1,17,1,11),_RcQosWredStatus_Type())
rcQosWredStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:rcQosWredStatus.setStatus(_A)
_RcQosPortWredTcpConfigTable_Object=MibTable
rcQosPortWredTcpConfigTable=_RcQosPortWredTcpConfigTable_Object((1,3,6,1,4,1,8886,1,33,1,18))
if mibBuilder.loadTexts:rcQosPortWredTcpConfigTable.setStatus(_A)
_RcQosPortWredTcpConfigEntry_Object=MibTableRow
rcQosPortWredTcpConfigEntry=_RcQosPortWredTcpConfigEntry_Object((1,3,6,1,4,1,8886,1,33,1,18,1))
rcQosPortWredTcpConfigEntry.setIndexNames((0,_D,_p),(0,_D,_q))
if mibBuilder.loadTexts:rcQosPortWredTcpConfigEntry.setStatus(_A)
_RcQosPortWredPortId_Type=Integer32
_RcQosPortWredPortId_Object=MibTableColumn
rcQosPortWredPortId=_RcQosPortWredPortId_Object((1,3,6,1,4,1,8886,1,33,1,18,1,1),_RcQosPortWredPortId_Type())
rcQosPortWredPortId.setMaxAccess(_F)
if mibBuilder.loadTexts:rcQosPortWredPortId.setStatus(_A)
_RcQosPortWredQueueId_Type=Integer32
_RcQosPortWredQueueId_Object=MibTableColumn
rcQosPortWredQueueId=_RcQosPortWredQueueId_Object((1,3,6,1,4,1,8886,1,33,1,18,1,2),_RcQosPortWredQueueId_Type())
rcQosPortWredQueueId.setMaxAccess(_F)
if mibBuilder.loadTexts:rcQosPortWredQueueId.setStatus(_A)
_RcQosPortWredGreenDropStartPoint_Type=Integer32
_RcQosPortWredGreenDropStartPoint_Object=MibTableColumn
rcQosPortWredGreenDropStartPoint=_RcQosPortWredGreenDropStartPoint_Object((1,3,6,1,4,1,8886,1,33,1,18,1,3),_RcQosPortWredGreenDropStartPoint_Type())
rcQosPortWredGreenDropStartPoint.setMaxAccess(_E)
if mibBuilder.loadTexts:rcQosPortWredGreenDropStartPoint.setStatus(_A)
_RcQosPortWredGreenDropEndPoint_Type=Integer32
_RcQosPortWredGreenDropEndPoint_Object=MibTableColumn
rcQosPortWredGreenDropEndPoint=_RcQosPortWredGreenDropEndPoint_Object((1,3,6,1,4,1,8886,1,33,1,18,1,4),_RcQosPortWredGreenDropEndPoint_Type())
rcQosPortWredGreenDropEndPoint.setMaxAccess(_E)
if mibBuilder.loadTexts:rcQosPortWredGreenDropEndPoint.setStatus(_A)
_RcQosPortWredGreenDropProbability_Type=Integer32
_RcQosPortWredGreenDropProbability_Object=MibTableColumn
rcQosPortWredGreenDropProbability=_RcQosPortWredGreenDropProbability_Object((1,3,6,1,4,1,8886,1,33,1,18,1,5),_RcQosPortWredGreenDropProbability_Type())
rcQosPortWredGreenDropProbability.setMaxAccess(_E)
if mibBuilder.loadTexts:rcQosPortWredGreenDropProbability.setStatus(_A)
_RcQosPortWredYellowDropStartPoint_Type=Integer32
_RcQosPortWredYellowDropStartPoint_Object=MibTableColumn
rcQosPortWredYellowDropStartPoint=_RcQosPortWredYellowDropStartPoint_Object((1,3,6,1,4,1,8886,1,33,1,18,1,6),_RcQosPortWredYellowDropStartPoint_Type())
rcQosPortWredYellowDropStartPoint.setMaxAccess(_E)
if mibBuilder.loadTexts:rcQosPortWredYellowDropStartPoint.setStatus(_A)
_RcQosPortWredYellowDropEndPoint_Type=Integer32
_RcQosPortWredYellowDropEndPoint_Object=MibTableColumn
rcQosPortWredYellowDropEndPoint=_RcQosPortWredYellowDropEndPoint_Object((1,3,6,1,4,1,8886,1,33,1,18,1,7),_RcQosPortWredYellowDropEndPoint_Type())
rcQosPortWredYellowDropEndPoint.setMaxAccess(_E)
if mibBuilder.loadTexts:rcQosPortWredYellowDropEndPoint.setStatus(_A)
_RcQosPortWredYellowDropProbability_Type=Integer32
_RcQosPortWredYellowDropProbability_Object=MibTableColumn
rcQosPortWredYellowDropProbability=_RcQosPortWredYellowDropProbability_Object((1,3,6,1,4,1,8886,1,33,1,18,1,8),_RcQosPortWredYellowDropProbability_Type())
rcQosPortWredYellowDropProbability.setMaxAccess(_E)
if mibBuilder.loadTexts:rcQosPortWredYellowDropProbability.setStatus(_A)
_RcQosPortWredRedDropStartPoint_Type=Integer32
_RcQosPortWredRedDropStartPoint_Object=MibTableColumn
rcQosPortWredRedDropStartPoint=_RcQosPortWredRedDropStartPoint_Object((1,3,6,1,4,1,8886,1,33,1,18,1,9),_RcQosPortWredRedDropStartPoint_Type())
rcQosPortWredRedDropStartPoint.setMaxAccess(_E)
if mibBuilder.loadTexts:rcQosPortWredRedDropStartPoint.setStatus(_A)
_RcQosPortWredRedDropEndPoint_Type=Integer32
_RcQosPortWredRedDropEndPoint_Object=MibTableColumn
rcQosPortWredRedDropEndPoint=_RcQosPortWredRedDropEndPoint_Object((1,3,6,1,4,1,8886,1,33,1,18,1,10),_RcQosPortWredRedDropEndPoint_Type())
rcQosPortWredRedDropEndPoint.setMaxAccess(_E)
if mibBuilder.loadTexts:rcQosPortWredRedDropEndPoint.setStatus(_A)
_RcQosPortWredRedDropProbability_Type=Integer32
_RcQosPortWredRedDropProbability_Object=MibTableColumn
rcQosPortWredRedDropProbability=_RcQosPortWredRedDropProbability_Object((1,3,6,1,4,1,8886,1,33,1,18,1,11),_RcQosPortWredRedDropProbability_Type())
rcQosPortWredRedDropProbability.setMaxAccess(_E)
if mibBuilder.loadTexts:rcQosPortWredRedDropProbability.setStatus(_A)
class _RcQosPortWredStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_N,1),(_O,2)))
_RcQosPortWredStatus_Type.__name__=_C
_RcQosPortWredStatus_Object=MibTableColumn
rcQosPortWredStatus=_RcQosPortWredStatus_Object((1,3,6,1,4,1,8886,1,33,1,18,1,12),_RcQosPortWredStatus_Type())
rcQosPortWredStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:rcQosPortWredStatus.setStatus(_A)
_RcQosShapingTable_Object=MibTable
rcQosShapingTable=_RcQosShapingTable_Object((1,3,6,1,4,1,8886,1,33,1,19))
if mibBuilder.loadTexts:rcQosShapingTable.setStatus(_A)
_RcQosShapingEntry_Object=MibTableRow
rcQosShapingEntry=_RcQosShapingEntry_Object((1,3,6,1,4,1,8886,1,33,1,19,1))
rcQosShapingEntry.setIndexNames((0,_D,_r))
if mibBuilder.loadTexts:rcQosShapingEntry.setStatus(_A)
_RcQosShapingQueueId_Type=Integer32
_RcQosShapingQueueId_Object=MibTableColumn
rcQosShapingQueueId=_RcQosShapingQueueId_Object((1,3,6,1,4,1,8886,1,33,1,19,1,1),_RcQosShapingQueueId_Type())
rcQosShapingQueueId.setMaxAccess(_F)
if mibBuilder.loadTexts:rcQosShapingQueueId.setStatus(_A)
_RcQosShapingCir_Type=Integer32
_RcQosShapingCir_Object=MibTableColumn
rcQosShapingCir=_RcQosShapingCir_Object((1,3,6,1,4,1,8886,1,33,1,19,1,2),_RcQosShapingCir_Type())
rcQosShapingCir.setMaxAccess(_E)
if mibBuilder.loadTexts:rcQosShapingCir.setStatus(_A)
_RcQosShapingCbs_Type=Integer32
_RcQosShapingCbs_Object=MibTableColumn
rcQosShapingCbs=_RcQosShapingCbs_Object((1,3,6,1,4,1,8886,1,33,1,19,1,3),_RcQosShapingCbs_Type())
rcQosShapingCbs.setMaxAccess(_E)
if mibBuilder.loadTexts:rcQosShapingCbs.setStatus(_A)
_RcQosShapingPir_Type=Integer32
_RcQosShapingPir_Object=MibTableColumn
rcQosShapingPir=_RcQosShapingPir_Object((1,3,6,1,4,1,8886,1,33,1,19,1,4),_RcQosShapingPir_Type())
rcQosShapingPir.setMaxAccess(_E)
if mibBuilder.loadTexts:rcQosShapingPir.setStatus(_A)
_RcQosShapingPbs_Type=Integer32
_RcQosShapingPbs_Object=MibTableColumn
rcQosShapingPbs=_RcQosShapingPbs_Object((1,3,6,1,4,1,8886,1,33,1,19,1,5),_RcQosShapingPbs_Type())
rcQosShapingPbs.setMaxAccess(_E)
if mibBuilder.loadTexts:rcQosShapingPbs.setStatus(_A)
class _RcQosShapingStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_N,1),(_O,2)))
_RcQosShapingStatus_Type.__name__=_C
_RcQosShapingStatus_Object=MibTableColumn
rcQosShapingStatus=_RcQosShapingStatus_Object((1,3,6,1,4,1,8886,1,33,1,19,1,6),_RcQosShapingStatus_Type())
rcQosShapingStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:rcQosShapingStatus.setStatus(_A)
_RcQosPortShapingTable_Object=MibTable
rcQosPortShapingTable=_RcQosPortShapingTable_Object((1,3,6,1,4,1,8886,1,33,1,20))
if mibBuilder.loadTexts:rcQosPortShapingTable.setStatus(_A)
_RcQosPortShapingEntry_Object=MibTableRow
rcQosPortShapingEntry=_RcQosPortShapingEntry_Object((1,3,6,1,4,1,8886,1,33,1,20,1))
rcQosPortShapingEntry.setIndexNames((0,_D,_s),(0,_D,_t))
if mibBuilder.loadTexts:rcQosPortShapingEntry.setStatus(_A)
_RcQosPortShapingPortId_Type=Integer32
_RcQosPortShapingPortId_Object=MibTableColumn
rcQosPortShapingPortId=_RcQosPortShapingPortId_Object((1,3,6,1,4,1,8886,1,33,1,20,1,1),_RcQosPortShapingPortId_Type())
rcQosPortShapingPortId.setMaxAccess(_F)
if mibBuilder.loadTexts:rcQosPortShapingPortId.setStatus(_A)
_RcQosPortShapingQueueId_Type=Integer32
_RcQosPortShapingQueueId_Object=MibTableColumn
rcQosPortShapingQueueId=_RcQosPortShapingQueueId_Object((1,3,6,1,4,1,8886,1,33,1,20,1,2),_RcQosPortShapingQueueId_Type())
rcQosPortShapingQueueId.setMaxAccess(_F)
if mibBuilder.loadTexts:rcQosPortShapingQueueId.setStatus(_A)
_RcQosPortShapingCir_Type=Integer32
_RcQosPortShapingCir_Object=MibTableColumn
rcQosPortShapingCir=_RcQosPortShapingCir_Object((1,3,6,1,4,1,8886,1,33,1,20,1,3),_RcQosPortShapingCir_Type())
rcQosPortShapingCir.setMaxAccess(_E)
if mibBuilder.loadTexts:rcQosPortShapingCir.setStatus(_A)
_RcQosPortShapingCbs_Type=Integer32
_RcQosPortShapingCbs_Object=MibTableColumn
rcQosPortShapingCbs=_RcQosPortShapingCbs_Object((1,3,6,1,4,1,8886,1,33,1,20,1,4),_RcQosPortShapingCbs_Type())
rcQosPortShapingCbs.setMaxAccess(_E)
if mibBuilder.loadTexts:rcQosPortShapingCbs.setStatus(_A)
_RcQosPortShapingPir_Type=Integer32
_RcQosPortShapingPir_Object=MibTableColumn
rcQosPortShapingPir=_RcQosPortShapingPir_Object((1,3,6,1,4,1,8886,1,33,1,20,1,5),_RcQosPortShapingPir_Type())
rcQosPortShapingPir.setMaxAccess(_E)
if mibBuilder.loadTexts:rcQosPortShapingPir.setStatus(_A)
_RcQosPortShapingPbs_Type=Integer32
_RcQosPortShapingPbs_Object=MibTableColumn
rcQosPortShapingPbs=_RcQosPortShapingPbs_Object((1,3,6,1,4,1,8886,1,33,1,20,1,6),_RcQosPortShapingPbs_Type())
rcQosPortShapingPbs.setMaxAccess(_E)
if mibBuilder.loadTexts:rcQosPortShapingPbs.setStatus(_A)
class _RcQosPortShapingStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_N,1),(_O,2)))
_RcQosPortShapingStatus_Type.__name__=_C
_RcQosPortShapingStatus_Object=MibTableColumn
rcQosPortShapingStatus=_RcQosPortShapingStatus_Object((1,3,6,1,4,1,8886,1,33,1,20,1,7),_RcQosPortShapingStatus_Type())
rcQosPortShapingStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:rcQosPortShapingStatus.setStatus(_A)
_RcQosPortCosMappingTable_Object=MibTable
rcQosPortCosMappingTable=_RcQosPortCosMappingTable_Object((1,3,6,1,4,1,8886,1,33,1,21))
if mibBuilder.loadTexts:rcQosPortCosMappingTable.setStatus(_A)
_RcQosPortCosMappingEntry_Object=MibTableRow
rcQosPortCosMappingEntry=_RcQosPortCosMappingEntry_Object((1,3,6,1,4,1,8886,1,33,1,21,1))
rcQosPortCosMappingEntry.setIndexNames((0,_D,_u),(0,_D,_v))
if mibBuilder.loadTexts:rcQosPortCosMappingEntry.setStatus(_A)
_RcQosPortCosPortId_Type=Integer32
_RcQosPortCosPortId_Object=MibTableColumn
rcQosPortCosPortId=_RcQosPortCosPortId_Object((1,3,6,1,4,1,8886,1,33,1,21,1,1),_RcQosPortCosPortId_Type())
rcQosPortCosPortId.setMaxAccess(_F)
if mibBuilder.loadTexts:rcQosPortCosPortId.setStatus(_A)
class _RcQosPortCosValue_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_RcQosPortCosValue_Type.__name__=_C
_RcQosPortCosValue_Object=MibTableColumn
rcQosPortCosValue=_RcQosPortCosValue_Object((1,3,6,1,4,1,8886,1,33,1,21,1,2),_RcQosPortCosValue_Type())
rcQosPortCosValue.setMaxAccess(_F)
if mibBuilder.loadTexts:rcQosPortCosValue.setStatus(_A)
class _RcQosPortCosLocalPriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_RcQosPortCosLocalPriority_Type.__name__=_C
_RcQosPortCosLocalPriority_Object=MibTableColumn
rcQosPortCosLocalPriority=_RcQosPortCosLocalPriority_Object((1,3,6,1,4,1,8886,1,33,1,21,1,3),_RcQosPortCosLocalPriority_Type())
rcQosPortCosLocalPriority.setMaxAccess(_E)
if mibBuilder.loadTexts:rcQosPortCosLocalPriority.setStatus(_A)
class _RcQosPortCosColor_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*((_L,0),(_I,1),(_J,2),(_K,3)))
_RcQosPortCosColor_Type.__name__=_C
_RcQosPortCosColor_Object=MibTableColumn
rcQosPortCosColor=_RcQosPortCosColor_Object((1,3,6,1,4,1,8886,1,33,1,21,1,4),_RcQosPortCosColor_Type())
rcQosPortCosColor.setMaxAccess(_E)
if mibBuilder.loadTexts:rcQosPortCosColor.setStatus(_A)
_RcQosPortTosMappingTable_Object=MibTable
rcQosPortTosMappingTable=_RcQosPortTosMappingTable_Object((1,3,6,1,4,1,8886,1,33,1,22))
if mibBuilder.loadTexts:rcQosPortTosMappingTable.setStatus(_A)
_RcQosPortTosMappingEntry_Object=MibTableRow
rcQosPortTosMappingEntry=_RcQosPortTosMappingEntry_Object((1,3,6,1,4,1,8886,1,33,1,22,1))
rcQosPortTosMappingEntry.setIndexNames((0,_D,_w),(0,_D,_x))
if mibBuilder.loadTexts:rcQosPortTosMappingEntry.setStatus(_A)
_RcQosPortTosPortId_Type=Integer32
_RcQosPortTosPortId_Object=MibTableColumn
rcQosPortTosPortId=_RcQosPortTosPortId_Object((1,3,6,1,4,1,8886,1,33,1,22,1,1),_RcQosPortTosPortId_Type())
rcQosPortTosPortId.setMaxAccess(_F)
if mibBuilder.loadTexts:rcQosPortTosPortId.setStatus(_A)
class _RcQosPortTosValue_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_RcQosPortTosValue_Type.__name__=_C
_RcQosPortTosValue_Object=MibTableColumn
rcQosPortTosValue=_RcQosPortTosValue_Object((1,3,6,1,4,1,8886,1,33,1,22,1,2),_RcQosPortTosValue_Type())
rcQosPortTosValue.setMaxAccess(_F)
if mibBuilder.loadTexts:rcQosPortTosValue.setStatus(_A)
class _RcQosPortTosLocalPriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_RcQosPortTosLocalPriority_Type.__name__=_C
_RcQosPortTosLocalPriority_Object=MibTableColumn
rcQosPortTosLocalPriority=_RcQosPortTosLocalPriority_Object((1,3,6,1,4,1,8886,1,33,1,22,1,3),_RcQosPortTosLocalPriority_Type())
rcQosPortTosLocalPriority.setMaxAccess(_E)
if mibBuilder.loadTexts:rcQosPortTosLocalPriority.setStatus(_A)
class _RcQosPortTosColor_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*((_L,0),(_I,1),(_J,2),(_K,3)))
_RcQosPortTosColor_Type.__name__=_C
_RcQosPortTosColor_Object=MibTableColumn
rcQosPortTosColor=_RcQosPortTosColor_Object((1,3,6,1,4,1,8886,1,33,1,22,1,4),_RcQosPortTosColor_Type())
rcQosPortTosColor.setMaxAccess(_E)
if mibBuilder.loadTexts:rcQosPortTosColor.setStatus(_A)
_RcQosPortDscpMapingTable_Object=MibTable
rcQosPortDscpMapingTable=_RcQosPortDscpMapingTable_Object((1,3,6,1,4,1,8886,1,33,1,23))
if mibBuilder.loadTexts:rcQosPortDscpMapingTable.setStatus(_A)
_RcQosPortDscpMapingEntry_Object=MibTableRow
rcQosPortDscpMapingEntry=_RcQosPortDscpMapingEntry_Object((1,3,6,1,4,1,8886,1,33,1,23,1))
rcQosPortDscpMapingEntry.setIndexNames((0,_D,_y),(0,_D,_z))
if mibBuilder.loadTexts:rcQosPortDscpMapingEntry.setStatus(_A)
_RcQosPortDscpPortId_Type=Integer32
_RcQosPortDscpPortId_Object=MibTableColumn
rcQosPortDscpPortId=_RcQosPortDscpPortId_Object((1,3,6,1,4,1,8886,1,33,1,23,1,1),_RcQosPortDscpPortId_Type())
rcQosPortDscpPortId.setMaxAccess(_F)
if mibBuilder.loadTexts:rcQosPortDscpPortId.setStatus(_A)
class _RcQosPortDscpValue_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,63))
_RcQosPortDscpValue_Type.__name__=_C
_RcQosPortDscpValue_Object=MibTableColumn
rcQosPortDscpValue=_RcQosPortDscpValue_Object((1,3,6,1,4,1,8886,1,33,1,23,1,2),_RcQosPortDscpValue_Type())
rcQosPortDscpValue.setMaxAccess(_F)
if mibBuilder.loadTexts:rcQosPortDscpValue.setStatus(_A)
class _RcQosPortDscpLocalPriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_RcQosPortDscpLocalPriority_Type.__name__=_C
_RcQosPortDscpLocalPriority_Object=MibTableColumn
rcQosPortDscpLocalPriority=_RcQosPortDscpLocalPriority_Object((1,3,6,1,4,1,8886,1,33,1,23,1,3),_RcQosPortDscpLocalPriority_Type())
rcQosPortDscpLocalPriority.setMaxAccess(_E)
if mibBuilder.loadTexts:rcQosPortDscpLocalPriority.setStatus(_A)
class _RcQosPortDscpColor_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*((_L,0),(_I,1),(_J,2),(_K,3)))
_RcQosPortDscpColor_Type.__name__=_C
_RcQosPortDscpColor_Object=MibTableColumn
rcQosPortDscpColor=_RcQosPortDscpColor_Object((1,3,6,1,4,1,8886,1,33,1,23,1,4),_RcQosPortDscpColor_Type())
rcQosPortDscpColor.setMaxAccess(_E)
if mibBuilder.loadTexts:rcQosPortDscpColor.setStatus(_A)
_RcQosPortDropPktsStatisticTable_Object=MibTable
rcQosPortDropPktsStatisticTable=_RcQosPortDropPktsStatisticTable_Object((1,3,6,1,4,1,8886,1,33,1,24))
if mibBuilder.loadTexts:rcQosPortDropPktsStatisticTable.setStatus(_A)
_RcQosPortDropPktsStatisticEntry_Object=MibTableRow
rcQosPortDropPktsStatisticEntry=_RcQosPortDropPktsStatisticEntry_Object((1,3,6,1,4,1,8886,1,33,1,24,1))
rcQosPortDropPktsStatisticEntry.setIndexNames((0,_D,_A0),(0,_D,_A1))
if mibBuilder.loadTexts:rcQosPortDropPktsStatisticEntry.setStatus(_A)
_RcQosPortStatisticsPortId_Type=Integer32
_RcQosPortStatisticsPortId_Object=MibTableColumn
rcQosPortStatisticsPortId=_RcQosPortStatisticsPortId_Object((1,3,6,1,4,1,8886,1,33,1,24,1,1),_RcQosPortStatisticsPortId_Type())
rcQosPortStatisticsPortId.setMaxAccess(_F)
if mibBuilder.loadTexts:rcQosPortStatisticsPortId.setStatus(_A)
_RcQosPortStatisticsQueueId_Type=Integer32
_RcQosPortStatisticsQueueId_Object=MibTableColumn
rcQosPortStatisticsQueueId=_RcQosPortStatisticsQueueId_Object((1,3,6,1,4,1,8886,1,33,1,24,1,2),_RcQosPortStatisticsQueueId_Type())
rcQosPortStatisticsQueueId.setMaxAccess(_F)
if mibBuilder.loadTexts:rcQosPortStatisticsQueueId.setStatus(_A)
_RcQosPortStatisticsDropPkts_Type=Counter64
_RcQosPortStatisticsDropPkts_Object=MibTableColumn
rcQosPortStatisticsDropPkts=_RcQosPortStatisticsDropPkts_Object((1,3,6,1,4,1,8886,1,33,1,24,1,3),_RcQosPortStatisticsDropPkts_Type())
rcQosPortStatisticsDropPkts.setMaxAccess(_G)
if mibBuilder.loadTexts:rcQosPortStatisticsDropPkts.setStatus(_A)
_RcQosPortStatisticsDropBytes_Type=Counter64
_RcQosPortStatisticsDropBytes_Object=MibTableColumn
rcQosPortStatisticsDropBytes=_RcQosPortStatisticsDropBytes_Object((1,3,6,1,4,1,8886,1,33,1,24,1,4),_RcQosPortStatisticsDropBytes_Type())
rcQosPortStatisticsDropBytes.setMaxAccess(_G)
if mibBuilder.loadTexts:rcQosPortStatisticsDropBytes.setStatus(_A)
class _RcQosPortStatisticsDropUnit_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('packets',0),(_S,1)))
_RcQosPortStatisticsDropUnit_Type.__name__=_C
_RcQosPortStatisticsDropUnit_Object=MibTableColumn
rcQosPortStatisticsDropUnit=_RcQosPortStatisticsDropUnit_Object((1,3,6,1,4,1,8886,1,33,1,24,1,5),_RcQosPortStatisticsDropUnit_Type())
rcQosPortStatisticsDropUnit.setMaxAccess(_G)
if mibBuilder.loadTexts:rcQosPortStatisticsDropUnit.setStatus(_A)
_RcQosPortStatisticsClear_Type=EnableVar
_RcQosPortStatisticsClear_Object=MibTableColumn
rcQosPortStatisticsClear=_RcQosPortStatisticsClear_Object((1,3,6,1,4,1,8886,1,33,1,24,1,6),_RcQosPortStatisticsClear_Type())
rcQosPortStatisticsClear.setMaxAccess(_E)
if mibBuilder.loadTexts:rcQosPortStatisticsClear.setStatus(_A)
_RcQosMappingCosToPriTable_Object=MibTable
rcQosMappingCosToPriTable=_RcQosMappingCosToPriTable_Object((1,3,6,1,4,1,8886,1,33,1,25))
if mibBuilder.loadTexts:rcQosMappingCosToPriTable.setStatus(_A)
_RcQosMappingCosToPriEntry_Object=MibTableRow
rcQosMappingCosToPriEntry=_RcQosMappingCosToPriEntry_Object((1,3,6,1,4,1,8886,1,33,1,25,1))
rcQosMappingCosToPriEntry.setIndexNames((0,_D,_A2),(0,_D,_A3))
if mibBuilder.loadTexts:rcQosMappingCosToPriEntry.setStatus(_A)
class _RcQosCosToPriIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,100))
_RcQosCosToPriIndex_Type.__name__=_C
_RcQosCosToPriIndex_Object=MibTableColumn
rcQosCosToPriIndex=_RcQosCosToPriIndex_Object((1,3,6,1,4,1,8886,1,33,1,25,1,1),_RcQosCosToPriIndex_Type())
rcQosCosToPriIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:rcQosCosToPriIndex.setStatus(_A)
class _RcQosCosToPriCos_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_RcQosCosToPriCos_Type.__name__=_C
_RcQosCosToPriCos_Object=MibTableColumn
rcQosCosToPriCos=_RcQosCosToPriCos_Object((1,3,6,1,4,1,8886,1,33,1,25,1,2),_RcQosCosToPriCos_Type())
rcQosCosToPriCos.setMaxAccess(_F)
if mibBuilder.loadTexts:rcQosCosToPriCos.setStatus(_A)
class _RcQosCosToPriLpri_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_RcQosCosToPriLpri_Type.__name__=_C
_RcQosCosToPriLpri_Object=MibTableColumn
rcQosCosToPriLpri=_RcQosCosToPriLpri_Object((1,3,6,1,4,1,8886,1,33,1,25,1,3),_RcQosCosToPriLpri_Type())
rcQosCosToPriLpri.setMaxAccess(_B)
if mibBuilder.loadTexts:rcQosCosToPriLpri.setStatus(_A)
class _RcQosCosToPriColor_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_I,1),(_J,2),(_K,3)))
_RcQosCosToPriColor_Type.__name__=_C
_RcQosCosToPriColor_Object=MibTableColumn
rcQosCosToPriColor=_RcQosCosToPriColor_Object((1,3,6,1,4,1,8886,1,33,1,25,1,4),_RcQosCosToPriColor_Type())
rcQosCosToPriColor.setMaxAccess(_B)
if mibBuilder.loadTexts:rcQosCosToPriColor.setStatus(_A)
_RcQosCosToPriDesc_Type=ObjName
_RcQosCosToPriDesc_Object=MibTableColumn
rcQosCosToPriDesc=_RcQosCosToPriDesc_Object((1,3,6,1,4,1,8886,1,33,1,25,1,5),_RcQosCosToPriDesc_Type())
rcQosCosToPriDesc.setMaxAccess(_B)
if mibBuilder.loadTexts:rcQosCosToPriDesc.setStatus(_A)
_RcQosCosToPriRef_Type=Integer32
_RcQosCosToPriRef_Object=MibTableColumn
rcQosCosToPriRef=_RcQosCosToPriRef_Object((1,3,6,1,4,1,8886,1,33,1,25,1,6),_RcQosCosToPriRef_Type())
rcQosCosToPriRef.setMaxAccess(_B)
if mibBuilder.loadTexts:rcQosCosToPriRef.setStatus(_A)
_RcQosCosToPriStatus_Type=RowStatus
_RcQosCosToPriStatus_Object=MibTableColumn
rcQosCosToPriStatus=_RcQosCosToPriStatus_Object((1,3,6,1,4,1,8886,1,33,1,25,1,7),_RcQosCosToPriStatus_Type())
rcQosCosToPriStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:rcQosCosToPriStatus.setStatus(_A)
_RcQosMappingTosToPriTable_Object=MibTable
rcQosMappingTosToPriTable=_RcQosMappingTosToPriTable_Object((1,3,6,1,4,1,8886,1,33,1,26))
if mibBuilder.loadTexts:rcQosMappingTosToPriTable.setStatus(_A)
_RcQosMappingTosToPriEntry_Object=MibTableRow
rcQosMappingTosToPriEntry=_RcQosMappingTosToPriEntry_Object((1,3,6,1,4,1,8886,1,33,1,26,1))
rcQosMappingTosToPriEntry.setIndexNames((0,_D,_A4),(0,_D,_A5))
if mibBuilder.loadTexts:rcQosMappingTosToPriEntry.setStatus(_A)
class _RcQosTosToPriIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,100))
_RcQosTosToPriIndex_Type.__name__=_C
_RcQosTosToPriIndex_Object=MibTableColumn
rcQosTosToPriIndex=_RcQosTosToPriIndex_Object((1,3,6,1,4,1,8886,1,33,1,26,1,1),_RcQosTosToPriIndex_Type())
rcQosTosToPriIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:rcQosTosToPriIndex.setStatus(_A)
class _RcQosTosToPriTos_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_RcQosTosToPriTos_Type.__name__=_C
_RcQosTosToPriTos_Object=MibTableColumn
rcQosTosToPriTos=_RcQosTosToPriTos_Object((1,3,6,1,4,1,8886,1,33,1,26,1,2),_RcQosTosToPriTos_Type())
rcQosTosToPriTos.setMaxAccess(_F)
if mibBuilder.loadTexts:rcQosTosToPriTos.setStatus(_A)
class _RcQosTosToPriLpri_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_RcQosTosToPriLpri_Type.__name__=_C
_RcQosTosToPriLpri_Object=MibTableColumn
rcQosTosToPriLpri=_RcQosTosToPriLpri_Object((1,3,6,1,4,1,8886,1,33,1,26,1,3),_RcQosTosToPriLpri_Type())
rcQosTosToPriLpri.setMaxAccess(_B)
if mibBuilder.loadTexts:rcQosTosToPriLpri.setStatus(_A)
class _RcQosTosToPriColor_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_I,1),(_J,2),(_K,3)))
_RcQosTosToPriColor_Type.__name__=_C
_RcQosTosToPriColor_Object=MibTableColumn
rcQosTosToPriColor=_RcQosTosToPriColor_Object((1,3,6,1,4,1,8886,1,33,1,26,1,4),_RcQosTosToPriColor_Type())
rcQosTosToPriColor.setMaxAccess(_B)
if mibBuilder.loadTexts:rcQosTosToPriColor.setStatus(_A)
_RcQosTosToPriDesc_Type=ObjName
_RcQosTosToPriDesc_Object=MibTableColumn
rcQosTosToPriDesc=_RcQosTosToPriDesc_Object((1,3,6,1,4,1,8886,1,33,1,26,1,5),_RcQosTosToPriDesc_Type())
rcQosTosToPriDesc.setMaxAccess(_B)
if mibBuilder.loadTexts:rcQosTosToPriDesc.setStatus(_A)
_RcQosTosToPriRef_Type=Integer32
_RcQosTosToPriRef_Object=MibTableColumn
rcQosTosToPriRef=_RcQosTosToPriRef_Object((1,3,6,1,4,1,8886,1,33,1,26,1,6),_RcQosTosToPriRef_Type())
rcQosTosToPriRef.setMaxAccess(_B)
if mibBuilder.loadTexts:rcQosTosToPriRef.setStatus(_A)
_RcQosTosToPriStatus_Type=RowStatus
_RcQosTosToPriStatus_Object=MibTableColumn
rcQosTosToPriStatus=_RcQosTosToPriStatus_Object((1,3,6,1,4,1,8886,1,33,1,26,1,7),_RcQosTosToPriStatus_Type())
rcQosTosToPriStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:rcQosTosToPriStatus.setStatus(_A)
_RcQosMappingDscpToPriTable_Object=MibTable
rcQosMappingDscpToPriTable=_RcQosMappingDscpToPriTable_Object((1,3,6,1,4,1,8886,1,33,1,27))
if mibBuilder.loadTexts:rcQosMappingDscpToPriTable.setStatus(_A)
_RcQosMappingDscpToPriEntry_Object=MibTableRow
rcQosMappingDscpToPriEntry=_RcQosMappingDscpToPriEntry_Object((1,3,6,1,4,1,8886,1,33,1,27,1))
rcQosMappingDscpToPriEntry.setIndexNames((0,_D,_A6),(0,_D,_A7))
if mibBuilder.loadTexts:rcQosMappingDscpToPriEntry.setStatus(_A)
class _RcQosDscpToPriIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,100))
_RcQosDscpToPriIndex_Type.__name__=_C
_RcQosDscpToPriIndex_Object=MibTableColumn
rcQosDscpToPriIndex=_RcQosDscpToPriIndex_Object((1,3,6,1,4,1,8886,1,33,1,27,1,1),_RcQosDscpToPriIndex_Type())
rcQosDscpToPriIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:rcQosDscpToPriIndex.setStatus(_A)
class _RcQosDscpToPriDscp_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,63))
_RcQosDscpToPriDscp_Type.__name__=_C
_RcQosDscpToPriDscp_Object=MibTableColumn
rcQosDscpToPriDscp=_RcQosDscpToPriDscp_Object((1,3,6,1,4,1,8886,1,33,1,27,1,2),_RcQosDscpToPriDscp_Type())
rcQosDscpToPriDscp.setMaxAccess(_F)
if mibBuilder.loadTexts:rcQosDscpToPriDscp.setStatus(_A)
class _RcQosDscpToPriLpri_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_RcQosDscpToPriLpri_Type.__name__=_C
_RcQosDscpToPriLpri_Object=MibTableColumn
rcQosDscpToPriLpri=_RcQosDscpToPriLpri_Object((1,3,6,1,4,1,8886,1,33,1,27,1,3),_RcQosDscpToPriLpri_Type())
rcQosDscpToPriLpri.setMaxAccess(_B)
if mibBuilder.loadTexts:rcQosDscpToPriLpri.setStatus(_A)
class _RcQosDscpToPriColor_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_I,1),(_J,2),(_K,3)))
_RcQosDscpToPriColor_Type.__name__=_C
_RcQosDscpToPriColor_Object=MibTableColumn
rcQosDscpToPriColor=_RcQosDscpToPriColor_Object((1,3,6,1,4,1,8886,1,33,1,27,1,4),_RcQosDscpToPriColor_Type())
rcQosDscpToPriColor.setMaxAccess(_B)
if mibBuilder.loadTexts:rcQosDscpToPriColor.setStatus(_A)
_RcQosDscpToPriDesc_Type=ObjName
_RcQosDscpToPriDesc_Object=MibTableColumn
rcQosDscpToPriDesc=_RcQosDscpToPriDesc_Object((1,3,6,1,4,1,8886,1,33,1,27,1,5),_RcQosDscpToPriDesc_Type())
rcQosDscpToPriDesc.setMaxAccess(_B)
if mibBuilder.loadTexts:rcQosDscpToPriDesc.setStatus(_A)
_RcQosDscpToPriRef_Type=Integer32
_RcQosDscpToPriRef_Object=MibTableColumn
rcQosDscpToPriRef=_RcQosDscpToPriRef_Object((1,3,6,1,4,1,8886,1,33,1,27,1,6),_RcQosDscpToPriRef_Type())
rcQosDscpToPriRef.setMaxAccess(_B)
if mibBuilder.loadTexts:rcQosDscpToPriRef.setStatus(_A)
_RcQosDscpToPriStatus_Type=RowStatus
_RcQosDscpToPriStatus_Object=MibTableColumn
rcQosDscpToPriStatus=_RcQosDscpToPriStatus_Object((1,3,6,1,4,1,8886,1,33,1,27,1,7),_RcQosDscpToPriStatus_Type())
rcQosDscpToPriStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:rcQosDscpToPriStatus.setStatus(_A)
_RcQosMappingDscpMutationTable_Object=MibTable
rcQosMappingDscpMutationTable=_RcQosMappingDscpMutationTable_Object((1,3,6,1,4,1,8886,1,33,1,28))
if mibBuilder.loadTexts:rcQosMappingDscpMutationTable.setStatus(_A)
_RcQosMappingDscpMutationEntry_Object=MibTableRow
rcQosMappingDscpMutationEntry=_RcQosMappingDscpMutationEntry_Object((1,3,6,1,4,1,8886,1,33,1,28,1))
rcQosMappingDscpMutationEntry.setIndexNames((0,_D,_A8),(0,_D,_A9))
if mibBuilder.loadTexts:rcQosMappingDscpMutationEntry.setStatus(_A)
class _RcQosDscpMutationIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,100))
_RcQosDscpMutationIndex_Type.__name__=_C
_RcQosDscpMutationIndex_Object=MibTableColumn
rcQosDscpMutationIndex=_RcQosDscpMutationIndex_Object((1,3,6,1,4,1,8886,1,33,1,28,1,1),_RcQosDscpMutationIndex_Type())
rcQosDscpMutationIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:rcQosDscpMutationIndex.setStatus(_A)
class _RcQosDscpMutationDscp_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,63))
_RcQosDscpMutationDscp_Type.__name__=_C
_RcQosDscpMutationDscp_Object=MibTableColumn
rcQosDscpMutationDscp=_RcQosDscpMutationDscp_Object((1,3,6,1,4,1,8886,1,33,1,28,1,2),_RcQosDscpMutationDscp_Type())
rcQosDscpMutationDscp.setMaxAccess(_F)
if mibBuilder.loadTexts:rcQosDscpMutationDscp.setStatus(_A)
class _RcQosDscpMutationNewDscp_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,63))
_RcQosDscpMutationNewDscp_Type.__name__=_C
_RcQosDscpMutationNewDscp_Object=MibTableColumn
rcQosDscpMutationNewDscp=_RcQosDscpMutationNewDscp_Object((1,3,6,1,4,1,8886,1,33,1,28,1,3),_RcQosDscpMutationNewDscp_Type())
rcQosDscpMutationNewDscp.setMaxAccess(_B)
if mibBuilder.loadTexts:rcQosDscpMutationNewDscp.setStatus(_A)
_RcQosDscpMutationDesc_Type=ObjName
_RcQosDscpMutationDesc_Object=MibTableColumn
rcQosDscpMutationDesc=_RcQosDscpMutationDesc_Object((1,3,6,1,4,1,8886,1,33,1,28,1,4),_RcQosDscpMutationDesc_Type())
rcQosDscpMutationDesc.setMaxAccess(_B)
if mibBuilder.loadTexts:rcQosDscpMutationDesc.setStatus(_A)
_RcQosDscpMutationRef_Type=Integer32
_RcQosDscpMutationRef_Object=MibTableColumn
rcQosDscpMutationRef=_RcQosDscpMutationRef_Object((1,3,6,1,4,1,8886,1,33,1,28,1,5),_RcQosDscpMutationRef_Type())
rcQosDscpMutationRef.setMaxAccess(_B)
if mibBuilder.loadTexts:rcQosDscpMutationRef.setStatus(_A)
_RcQosDscpMutationStatus_Type=RowStatus
_RcQosDscpMutationStatus_Object=MibTableColumn
rcQosDscpMutationStatus=_RcQosDscpMutationStatus_Object((1,3,6,1,4,1,8886,1,33,1,28,1,6),_RcQosDscpMutationStatus_Type())
rcQosDscpMutationStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:rcQosDscpMutationStatus.setStatus(_A)
_RcQosMappingCosRemarkTable_Object=MibTable
rcQosMappingCosRemarkTable=_RcQosMappingCosRemarkTable_Object((1,3,6,1,4,1,8886,1,33,1,29))
if mibBuilder.loadTexts:rcQosMappingCosRemarkTable.setStatus(_A)
_RcQosMappingCosRemarkEntry_Object=MibTableRow
rcQosMappingCosRemarkEntry=_RcQosMappingCosRemarkEntry_Object((1,3,6,1,4,1,8886,1,33,1,29,1))
rcQosMappingCosRemarkEntry.setIndexNames((0,_D,_AA),(0,_D,_AB))
if mibBuilder.loadTexts:rcQosMappingCosRemarkEntry.setStatus(_A)
class _RcQosCosRemarkIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,100))
_RcQosCosRemarkIndex_Type.__name__=_C
_RcQosCosRemarkIndex_Object=MibTableColumn
rcQosCosRemarkIndex=_RcQosCosRemarkIndex_Object((1,3,6,1,4,1,8886,1,33,1,29,1,1),_RcQosCosRemarkIndex_Type())
rcQosCosRemarkIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:rcQosCosRemarkIndex.setStatus(_A)
class _RcQosCosRemarkLpri_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_RcQosCosRemarkLpri_Type.__name__=_C
_RcQosCosRemarkLpri_Object=MibTableColumn
rcQosCosRemarkLpri=_RcQosCosRemarkLpri_Object((1,3,6,1,4,1,8886,1,33,1,29,1,2),_RcQosCosRemarkLpri_Type())
rcQosCosRemarkLpri.setMaxAccess(_F)
if mibBuilder.loadTexts:rcQosCosRemarkLpri.setStatus(_A)
class _RcQosCosRemarkCos_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_RcQosCosRemarkCos_Type.__name__=_C
_RcQosCosRemarkCos_Object=MibTableColumn
rcQosCosRemarkCos=_RcQosCosRemarkCos_Object((1,3,6,1,4,1,8886,1,33,1,29,1,3),_RcQosCosRemarkCos_Type())
rcQosCosRemarkCos.setMaxAccess(_B)
if mibBuilder.loadTexts:rcQosCosRemarkCos.setStatus(_A)
_RcQosCosRemarkDesc_Type=ObjName
_RcQosCosRemarkDesc_Object=MibTableColumn
rcQosCosRemarkDesc=_RcQosCosRemarkDesc_Object((1,3,6,1,4,1,8886,1,33,1,29,1,4),_RcQosCosRemarkDesc_Type())
rcQosCosRemarkDesc.setMaxAccess(_B)
if mibBuilder.loadTexts:rcQosCosRemarkDesc.setStatus(_A)
_RcQosCosRemarkRef_Type=Integer32
_RcQosCosRemarkRef_Object=MibTableColumn
rcQosCosRemarkRef=_RcQosCosRemarkRef_Object((1,3,6,1,4,1,8886,1,33,1,29,1,5),_RcQosCosRemarkRef_Type())
rcQosCosRemarkRef.setMaxAccess(_B)
if mibBuilder.loadTexts:rcQosCosRemarkRef.setStatus(_A)
_RcQosCosRemarkStatus_Type=RowStatus
_RcQosCosRemarkStatus_Object=MibTableColumn
rcQosCosRemarkStatus=_RcQosCosRemarkStatus_Object((1,3,6,1,4,1,8886,1,33,1,29,1,6),_RcQosCosRemarkStatus_Type())
rcQosCosRemarkStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:rcQosCosRemarkStatus.setStatus(_A)
_RcQosWredProfileTable_Object=MibTable
rcQosWredProfileTable=_RcQosWredProfileTable_Object((1,3,6,1,4,1,8886,1,33,1,30))
if mibBuilder.loadTexts:rcQosWredProfileTable.setStatus(_A)
_RcQosWredProfileEntry_Object=MibTableRow
rcQosWredProfileEntry=_RcQosWredProfileEntry_Object((1,3,6,1,4,1,8886,1,33,1,30,1))
rcQosWredProfileEntry.setIndexNames((0,_D,_AC))
if mibBuilder.loadTexts:rcQosWredProfileEntry.setStatus(_A)
class _RcQosWredProfileIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,100))
_RcQosWredProfileIndex_Type.__name__=_C
_RcQosWredProfileIndex_Object=MibTableColumn
rcQosWredProfileIndex=_RcQosWredProfileIndex_Object((1,3,6,1,4,1,8886,1,33,1,30,1,1),_RcQosWredProfileIndex_Type())
rcQosWredProfileIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:rcQosWredProfileIndex.setStatus(_A)
_RcQosWredProfileGreenDropStartPoint_Type=Integer32
_RcQosWredProfileGreenDropStartPoint_Object=MibTableColumn
rcQosWredProfileGreenDropStartPoint=_RcQosWredProfileGreenDropStartPoint_Object((1,3,6,1,4,1,8886,1,33,1,30,1,2),_RcQosWredProfileGreenDropStartPoint_Type())
rcQosWredProfileGreenDropStartPoint.setMaxAccess(_B)
if mibBuilder.loadTexts:rcQosWredProfileGreenDropStartPoint.setStatus(_A)
_RcQosWredProfileGreenDropEndPoint_Type=Integer32
_RcQosWredProfileGreenDropEndPoint_Object=MibTableColumn
rcQosWredProfileGreenDropEndPoint=_RcQosWredProfileGreenDropEndPoint_Object((1,3,6,1,4,1,8886,1,33,1,30,1,3),_RcQosWredProfileGreenDropEndPoint_Type())
rcQosWredProfileGreenDropEndPoint.setMaxAccess(_B)
if mibBuilder.loadTexts:rcQosWredProfileGreenDropEndPoint.setStatus(_A)
_RcQosWredProfileGreenDropProbability_Type=Integer32
_RcQosWredProfileGreenDropProbability_Object=MibTableColumn
rcQosWredProfileGreenDropProbability=_RcQosWredProfileGreenDropProbability_Object((1,3,6,1,4,1,8886,1,33,1,30,1,4),_RcQosWredProfileGreenDropProbability_Type())
rcQosWredProfileGreenDropProbability.setMaxAccess(_B)
if mibBuilder.loadTexts:rcQosWredProfileGreenDropProbability.setStatus(_A)
_RcQosWredProfileYellowDropStartPoint_Type=Integer32
_RcQosWredProfileYellowDropStartPoint_Object=MibTableColumn
rcQosWredProfileYellowDropStartPoint=_RcQosWredProfileYellowDropStartPoint_Object((1,3,6,1,4,1,8886,1,33,1,30,1,5),_RcQosWredProfileYellowDropStartPoint_Type())
rcQosWredProfileYellowDropStartPoint.setMaxAccess(_B)
if mibBuilder.loadTexts:rcQosWredProfileYellowDropStartPoint.setStatus(_A)
_RcQosWredProfileYellowDropEndPoint_Type=Integer32
_RcQosWredProfileYellowDropEndPoint_Object=MibTableColumn
rcQosWredProfileYellowDropEndPoint=_RcQosWredProfileYellowDropEndPoint_Object((1,3,6,1,4,1,8886,1,33,1,30,1,6),_RcQosWredProfileYellowDropEndPoint_Type())
rcQosWredProfileYellowDropEndPoint.setMaxAccess(_B)
if mibBuilder.loadTexts:rcQosWredProfileYellowDropEndPoint.setStatus(_A)
_RcQosWredProfileYellowDropProbability_Type=Integer32
_RcQosWredProfileYellowDropProbability_Object=MibTableColumn
rcQosWredProfileYellowDropProbability=_RcQosWredProfileYellowDropProbability_Object((1,3,6,1,4,1,8886,1,33,1,30,1,7),_RcQosWredProfileYellowDropProbability_Type())
rcQosWredProfileYellowDropProbability.setMaxAccess(_B)
if mibBuilder.loadTexts:rcQosWredProfileYellowDropProbability.setStatus(_A)
_RcQosWredProfileRedDropStartPoint_Type=Integer32
_RcQosWredProfileRedDropStartPoint_Object=MibTableColumn
rcQosWredProfileRedDropStartPoint=_RcQosWredProfileRedDropStartPoint_Object((1,3,6,1,4,1,8886,1,33,1,30,1,8),_RcQosWredProfileRedDropStartPoint_Type())
rcQosWredProfileRedDropStartPoint.setMaxAccess(_B)
if mibBuilder.loadTexts:rcQosWredProfileRedDropStartPoint.setStatus(_A)
_RcQosWredProfileRedDropEndPoint_Type=Integer32
_RcQosWredProfileRedDropEndPoint_Object=MibTableColumn
rcQosWredProfileRedDropEndPoint=_RcQosWredProfileRedDropEndPoint_Object((1,3,6,1,4,1,8886,1,33,1,30,1,9),_RcQosWredProfileRedDropEndPoint_Type())
rcQosWredProfileRedDropEndPoint.setMaxAccess(_B)
if mibBuilder.loadTexts:rcQosWredProfileRedDropEndPoint.setStatus(_A)
_RcQosWredProfileRedDropProbability_Type=Integer32
_RcQosWredProfileRedDropProbability_Object=MibTableColumn
rcQosWredProfileRedDropProbability=_RcQosWredProfileRedDropProbability_Object((1,3,6,1,4,1,8886,1,33,1,30,1,10),_RcQosWredProfileRedDropProbability_Type())
rcQosWredProfileRedDropProbability.setMaxAccess(_B)
if mibBuilder.loadTexts:rcQosWredProfileRedDropProbability.setStatus(_A)
_RcQosWredProfileDesc_Type=ObjName
_RcQosWredProfileDesc_Object=MibTableColumn
rcQosWredProfileDesc=_RcQosWredProfileDesc_Object((1,3,6,1,4,1,8886,1,33,1,30,1,11),_RcQosWredProfileDesc_Type())
rcQosWredProfileDesc.setMaxAccess(_B)
if mibBuilder.loadTexts:rcQosWredProfileDesc.setStatus(_A)
_RcQosWredProfileRef_Type=Integer32
_RcQosWredProfileRef_Object=MibTableColumn
rcQosWredProfileRef=_RcQosWredProfileRef_Object((1,3,6,1,4,1,8886,1,33,1,30,1,12),_RcQosWredProfileRef_Type())
rcQosWredProfileRef.setMaxAccess(_B)
if mibBuilder.loadTexts:rcQosWredProfileRef.setStatus(_A)
_RcQosWredProfileStatus_Type=RowStatus
_RcQosWredProfileStatus_Object=MibTableColumn
rcQosWredProfileStatus=_RcQosWredProfileStatus_Object((1,3,6,1,4,1,8886,1,33,1,30,1,13),_RcQosWredProfileStatus_Type())
rcQosWredProfileStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:rcQosWredProfileStatus.setStatus(_A)
_RcQosGloWredProfileTable_Object=MibTable
rcQosGloWredProfileTable=_RcQosGloWredProfileTable_Object((1,3,6,1,4,1,8886,1,33,1,31))
if mibBuilder.loadTexts:rcQosGloWredProfileTable.setStatus(_A)
_RcQosGloWredProfileEntry_Object=MibTableRow
rcQosGloWredProfileEntry=_RcQosGloWredProfileEntry_Object((1,3,6,1,4,1,8886,1,33,1,31,1))
rcQosGloWredProfileEntry.setIndexNames((0,_D,_AD))
if mibBuilder.loadTexts:rcQosGloWredProfileEntry.setStatus(_A)
_RcQosGloWredProfileQueueId_Type=Integer32
_RcQosGloWredProfileQueueId_Object=MibTableColumn
rcQosGloWredProfileQueueId=_RcQosGloWredProfileQueueId_Object((1,3,6,1,4,1,8886,1,33,1,31,1,1),_RcQosGloWredProfileQueueId_Type())
rcQosGloWredProfileQueueId.setMaxAccess(_F)
if mibBuilder.loadTexts:rcQosGloWredProfileQueueId.setStatus(_A)
class _RcQosGloWredProfileIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,100))
_RcQosGloWredProfileIndex_Type.__name__=_C
_RcQosGloWredProfileIndex_Object=MibTableColumn
rcQosGloWredProfileIndex=_RcQosGloWredProfileIndex_Object((1,3,6,1,4,1,8886,1,33,1,31,1,2),_RcQosGloWredProfileIndex_Type())
rcQosGloWredProfileIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:rcQosGloWredProfileIndex.setStatus(_A)
_RcQosGloWredProfileStatus_Type=RowStatus
_RcQosGloWredProfileStatus_Object=MibTableColumn
rcQosGloWredProfileStatus=_RcQosGloWredProfileStatus_Object((1,3,6,1,4,1,8886,1,33,1,31,1,3),_RcQosGloWredProfileStatus_Type())
rcQosGloWredProfileStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:rcQosGloWredProfileStatus.setStatus(_A)
_RcQosPortWredProfileTable_Object=MibTable
rcQosPortWredProfileTable=_RcQosPortWredProfileTable_Object((1,3,6,1,4,1,8886,1,33,1,32))
if mibBuilder.loadTexts:rcQosPortWredProfileTable.setStatus(_A)
_RcQosPortWredProfileEntry_Object=MibTableRow
rcQosPortWredProfileEntry=_RcQosPortWredProfileEntry_Object((1,3,6,1,4,1,8886,1,33,1,32,1))
rcQosPortWredProfileEntry.setIndexNames((0,_D,_AE),(0,_D,_AF))
if mibBuilder.loadTexts:rcQosPortWredProfileEntry.setStatus(_A)
_RcQosPortWredProfilePortId_Type=Integer32
_RcQosPortWredProfilePortId_Object=MibTableColumn
rcQosPortWredProfilePortId=_RcQosPortWredProfilePortId_Object((1,3,6,1,4,1,8886,1,33,1,32,1,1),_RcQosPortWredProfilePortId_Type())
rcQosPortWredProfilePortId.setMaxAccess(_F)
if mibBuilder.loadTexts:rcQosPortWredProfilePortId.setStatus(_A)
_RcQosPortWredProfileQueueId_Type=Integer32
_RcQosPortWredProfileQueueId_Object=MibTableColumn
rcQosPortWredProfileQueueId=_RcQosPortWredProfileQueueId_Object((1,3,6,1,4,1,8886,1,33,1,32,1,2),_RcQosPortWredProfileQueueId_Type())
rcQosPortWredProfileQueueId.setMaxAccess(_F)
if mibBuilder.loadTexts:rcQosPortWredProfileQueueId.setStatus(_A)
class _RcQosPortWredProfileIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,100))
_RcQosPortWredProfileIndex_Type.__name__=_C
_RcQosPortWredProfileIndex_Object=MibTableColumn
rcQosPortWredProfileIndex=_RcQosPortWredProfileIndex_Object((1,3,6,1,4,1,8886,1,33,1,32,1,3),_RcQosPortWredProfileIndex_Type())
rcQosPortWredProfileIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:rcQosPortWredProfileIndex.setStatus(_A)
_RcQosPortWredProfileStatus_Type=RowStatus
_RcQosPortWredProfileStatus_Object=MibTableColumn
rcQosPortWredProfileStatus=_RcQosPortWredProfileStatus_Object((1,3,6,1,4,1,8886,1,33,1,32,1,4),_RcQosPortWredProfileStatus_Type())
rcQosPortWredProfileStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:rcQosPortWredProfileStatus.setStatus(_A)
_RaisecomQosTrafficClass_ObjectIdentity=ObjectIdentity
raisecomQosTrafficClass=_RaisecomQosTrafficClass_ObjectIdentity((1,3,6,1,4,1,8886,1,33,2))
_RcPolicyEnable_Type=EnableVar
_RcPolicyEnable_Object=MibScalar
rcPolicyEnable=_RcPolicyEnable_Object((1,3,6,1,4,1,8886,1,33,2,1),_RcPolicyEnable_Type())
rcPolicyEnable.setMaxAccess(_E)
if mibBuilder.loadTexts:rcPolicyEnable.setStatus(_A)
_RcQosServicePolicyTable_Object=MibTable
rcQosServicePolicyTable=_RcQosServicePolicyTable_Object((1,3,6,1,4,1,8886,1,33,2,2))
if mibBuilder.loadTexts:rcQosServicePolicyTable.setStatus(_A)
_RcQosServicePolicyEntry_Object=MibTableRow
rcQosServicePolicyEntry=_RcQosServicePolicyEntry_Object((1,3,6,1,4,1,8886,1,33,2,2,1))
rcQosServicePolicyEntry.setIndexNames((0,_D,_AG))
if mibBuilder.loadTexts:rcQosServicePolicyEntry.setStatus(_A)
_RcQosServicePolicyIngress_Type=Integer32
_RcQosServicePolicyIngress_Object=MibTableColumn
rcQosServicePolicyIngress=_RcQosServicePolicyIngress_Object((1,3,6,1,4,1,8886,1,33,2,2,1,1),_RcQosServicePolicyIngress_Type())
rcQosServicePolicyIngress.setMaxAccess(_F)
if mibBuilder.loadTexts:rcQosServicePolicyIngress.setStatus(_A)
_RcQosServicePolicyEgress_Type=PortList
_RcQosServicePolicyEgress_Object=MibTableColumn
rcQosServicePolicyEgress=_RcQosServicePolicyEgress_Object((1,3,6,1,4,1,8886,1,33,2,2,1,2),_RcQosServicePolicyEgress_Type())
rcQosServicePolicyEgress.setMaxAccess(_B)
if mibBuilder.loadTexts:rcQosServicePolicyEgress.setStatus(_A)
_RcQosServicePolicyMapName_Type=ObjName
_RcQosServicePolicyMapName_Object=MibTableColumn
rcQosServicePolicyMapName=_RcQosServicePolicyMapName_Object((1,3,6,1,4,1,8886,1,33,2,2,1,3),_RcQosServicePolicyMapName_Type())
rcQosServicePolicyMapName.setMaxAccess(_B)
if mibBuilder.loadTexts:rcQosServicePolicyMapName.setStatus(_A)
_RcQosServicePolicyStatus_Type=RowStatus
_RcQosServicePolicyStatus_Object=MibTableColumn
rcQosServicePolicyStatus=_RcQosServicePolicyStatus_Object((1,3,6,1,4,1,8886,1,33,2,2,1,4),_RcQosServicePolicyStatus_Type())
rcQosServicePolicyStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:rcQosServicePolicyStatus.setStatus(_A)
_RcQosPolicyMapCfgTable_Object=MibTable
rcQosPolicyMapCfgTable=_RcQosPolicyMapCfgTable_Object((1,3,6,1,4,1,8886,1,33,2,3))
if mibBuilder.loadTexts:rcQosPolicyMapCfgTable.setStatus(_A)
_RcQosPolicyMapCfgEntry_Object=MibTableRow
rcQosPolicyMapCfgEntry=_RcQosPolicyMapCfgEntry_Object((1,3,6,1,4,1,8886,1,33,2,3,1))
rcQosPolicyMapCfgEntry.setIndexNames((0,_D,_AH))
if mibBuilder.loadTexts:rcQosPolicyMapCfgEntry.setStatus(_A)
_RcQosPolicyMapName_Type=ObjName
_RcQosPolicyMapName_Object=MibTableColumn
rcQosPolicyMapName=_RcQosPolicyMapName_Object((1,3,6,1,4,1,8886,1,33,2,3,1,1),_RcQosPolicyMapName_Type())
rcQosPolicyMapName.setMaxAccess(_F)
if mibBuilder.loadTexts:rcQosPolicyMapName.setStatus(_A)
class _RcQosPolicyMapDesc_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_RcQosPolicyMapDesc_Type.__name__=_H
_RcQosPolicyMapDesc_Object=MibTableColumn
rcQosPolicyMapDesc=_RcQosPolicyMapDesc_Object((1,3,6,1,4,1,8886,1,33,2,3,1,2),_RcQosPolicyMapDesc_Type())
rcQosPolicyMapDesc.setMaxAccess(_B)
if mibBuilder.loadTexts:rcQosPolicyMapDesc.setStatus(_A)
_RcQosPolicyMapCfgStatus_Type=RowStatus
_RcQosPolicyMapCfgStatus_Object=MibTableColumn
rcQosPolicyMapCfgStatus=_RcQosPolicyMapCfgStatus_Object((1,3,6,1,4,1,8886,1,33,2,3,1,3),_RcQosPolicyMapCfgStatus_Type())
rcQosPolicyMapCfgStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:rcQosPolicyMapCfgStatus.setStatus(_A)
class _RcQosPolicyMapType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('policy-map',1),('vlan-policy-map',2),('cos-policy-map',3),('pw-policy-map',4)))
_RcQosPolicyMapType_Type.__name__=_C
_RcQosPolicyMapType_Object=MibTableColumn
rcQosPolicyMapType=_RcQosPolicyMapType_Object((1,3,6,1,4,1,8886,1,33,2,3,1,4),_RcQosPolicyMapType_Type())
rcQosPolicyMapType.setMaxAccess(_B)
if mibBuilder.loadTexts:rcQosPolicyMapType.setStatus(_A)
_RcQosCMCfgTable_Object=MibTable
rcQosCMCfgTable=_RcQosCMCfgTable_Object((1,3,6,1,4,1,8886,1,33,2,4))
if mibBuilder.loadTexts:rcQosCMCfgTable.setStatus(_A)
_RcQosCMCfgEntry_Object=MibTableRow
rcQosCMCfgEntry=_RcQosCMCfgEntry_Object((1,3,6,1,4,1,8886,1,33,2,4,1))
rcQosCMCfgEntry.setIndexNames((0,_D,_AI))
if mibBuilder.loadTexts:rcQosCMCfgEntry.setStatus(_A)
_RcQosCMName_Type=ObjName
_RcQosCMName_Object=MibTableColumn
rcQosCMName=_RcQosCMName_Object((1,3,6,1,4,1,8886,1,33,2,4,1,1),_RcQosCMName_Type())
rcQosCMName.setMaxAccess(_F)
if mibBuilder.loadTexts:rcQosCMName.setStatus(_A)
class _RcQosCMDesc_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_RcQosCMDesc_Type.__name__=_H
_RcQosCMDesc_Object=MibTableColumn
rcQosCMDesc=_RcQosCMDesc_Object((1,3,6,1,4,1,8886,1,33,2,4,1,2),_RcQosCMDesc_Type())
rcQosCMDesc.setMaxAccess(_B)
if mibBuilder.loadTexts:rcQosCMDesc.setStatus(_A)
class _RcQosCMMatchType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('matchAll',1),('matchAny',2)))
_RcQosCMMatchType_Type.__name__=_C
_RcQosCMMatchType_Object=MibTableColumn
rcQosCMMatchType=_RcQosCMMatchType_Object((1,3,6,1,4,1,8886,1,33,2,4,1,3),_RcQosCMMatchType_Type())
rcQosCMMatchType.setMaxAccess(_B)
if mibBuilder.loadTexts:rcQosCMMatchType.setStatus(_A)
_RcQosCMClassID_Type=Integer32
_RcQosCMClassID_Object=MibTableColumn
rcQosCMClassID=_RcQosCMClassID_Object((1,3,6,1,4,1,8886,1,33,2,4,1,4),_RcQosCMClassID_Type())
rcQosCMClassID.setMaxAccess(_G)
if mibBuilder.loadTexts:rcQosCMClassID.setStatus(_A)
_RcQosCMStatus_Type=RowStatus
_RcQosCMStatus_Object=MibTableColumn
rcQosCMStatus=_RcQosCMStatus_Object((1,3,6,1,4,1,8886,1,33,2,4,1,5),_RcQosCMStatus_Type())
rcQosCMStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:rcQosCMStatus.setStatus(_A)
_RcQosCMDoubleTagging_Type=TruthValue
_RcQosCMDoubleTagging_Object=MibTableColumn
rcQosCMDoubleTagging=_RcQosCMDoubleTagging_Object((1,3,6,1,4,1,8886,1,33,2,4,1,6),_RcQosCMDoubleTagging_Type())
rcQosCMDoubleTagging.setMaxAccess(_B)
if mibBuilder.loadTexts:rcQosCMDoubleTagging.setStatus('deprecated')
_RcQosMatchStmtTable_Object=MibTable
rcQosMatchStmtTable=_RcQosMatchStmtTable_Object((1,3,6,1,4,1,8886,1,33,2,5))
if mibBuilder.loadTexts:rcQosMatchStmtTable.setStatus(_A)
_RcQosMatchStmtEntry_Object=MibTableRow
rcQosMatchStmtEntry=_RcQosMatchStmtEntry_Object((1,3,6,1,4,1,8886,1,33,2,5,1))
rcQosMatchStmtEntry.setIndexNames((0,_D,_AJ),(0,_D,_AK),(0,_D,_AL))
if mibBuilder.loadTexts:rcQosMatchStmtEntry.setStatus(_A)
_RcQosMatchStmtClassName_Type=ObjName
_RcQosMatchStmtClassName_Object=MibTableColumn
rcQosMatchStmtClassName=_RcQosMatchStmtClassName_Object((1,3,6,1,4,1,8886,1,33,2,5,1,1),_RcQosMatchStmtClassName_Type())
rcQosMatchStmtClassName.setMaxAccess(_F)
if mibBuilder.loadTexts:rcQosMatchStmtClassName.setStatus(_A)
class _RcQosMatchStmtType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17)));namedValues=NamedValues(*(('ip-acl',1),('mac-acl',2),('user-acl',3),(_U,4),('ipprecedence',5),('class',6),('vlan',7),('vlan-inner',8),(_T,9),('ipv6-acl',10),('traffic-class',11),('inner-outer-vlan',12),('tunnel-label',13),('tunnel-exp',14),('vc-label',15),('vc-exp',16),('flow-label',17)))
_RcQosMatchStmtType_Type.__name__=_C
_RcQosMatchStmtType_Object=MibTableColumn
rcQosMatchStmtType=_RcQosMatchStmtType_Object((1,3,6,1,4,1,8886,1,33,2,5,1,2),_RcQosMatchStmtType_Type())
rcQosMatchStmtType.setMaxAccess(_F)
if mibBuilder.loadTexts:rcQosMatchStmtType.setStatus(_A)
class _RcQosMatchStmtValue_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4094))
_RcQosMatchStmtValue_Type.__name__=_C
_RcQosMatchStmtValue_Object=MibTableColumn
rcQosMatchStmtValue=_RcQosMatchStmtValue_Object((1,3,6,1,4,1,8886,1,33,2,5,1,3),_RcQosMatchStmtValue_Type())
rcQosMatchStmtValue.setMaxAccess(_F)
if mibBuilder.loadTexts:rcQosMatchStmtValue.setStatus(_A)
_RcQosMatchStmtSubName_Type=ObjName
_RcQosMatchStmtSubName_Object=MibTableColumn
rcQosMatchStmtSubName=_RcQosMatchStmtSubName_Object((1,3,6,1,4,1,8886,1,33,2,5,1,4),_RcQosMatchStmtSubName_Type())
rcQosMatchStmtSubName.setMaxAccess(_G)
if mibBuilder.loadTexts:rcQosMatchStmtSubName.setStatus(_A)
_RcQosMatchStmtStatus_Type=RowStatus
_RcQosMatchStmtStatus_Object=MibTableColumn
rcQosMatchStmtStatus=_RcQosMatchStmtStatus_Object((1,3,6,1,4,1,8886,1,33,2,5,1,5),_RcQosMatchStmtStatus_Type())
rcQosMatchStmtStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:rcQosMatchStmtStatus.setStatus(_A)
_RcQosPolicerCfgTable_Object=MibTable
rcQosPolicerCfgTable=_RcQosPolicerCfgTable_Object((1,3,6,1,4,1,8886,1,33,2,6))
if mibBuilder.loadTexts:rcQosPolicerCfgTable.setStatus(_A)
_RcQosPolicerCfgEntry_Object=MibTableRow
rcQosPolicerCfgEntry=_RcQosPolicerCfgEntry_Object((1,3,6,1,4,1,8886,1,33,2,6,1))
rcQosPolicerCfgEntry.setIndexNames((0,_D,_AM))
if mibBuilder.loadTexts:rcQosPolicerCfgEntry.setStatus(_A)
_RcQosPolicerCfgName_Type=ObjName
_RcQosPolicerCfgName_Object=MibTableColumn
rcQosPolicerCfgName=_RcQosPolicerCfgName_Object((1,3,6,1,4,1,8886,1,33,2,6,1,1),_RcQosPolicerCfgName_Type())
rcQosPolicerCfgName.setMaxAccess(_F)
if mibBuilder.loadTexts:rcQosPolicerCfgName.setStatus(_A)
class _RcQosPolicerCfgType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('single-policer',1),('class-policer',2),('aggregate-policer',3),('hierarchy-policer',4)))
_RcQosPolicerCfgType_Type.__name__=_C
_RcQosPolicerCfgType_Object=MibTableColumn
rcQosPolicerCfgType=_RcQosPolicerCfgType_Object((1,3,6,1,4,1,8886,1,33,2,6,1,2),_RcQosPolicerCfgType_Type())
rcQosPolicerCfgType.setMaxAccess(_B)
if mibBuilder.loadTexts:rcQosPolicerCfgType.setStatus(_A)
class _RcQosPolicerCfgMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*(('flow',1),('rfc2697',2),('rfc2698',3),('rfc4115',4),('mef',5),('single',6),('double',7)))
_RcQosPolicerCfgMode_Type.__name__=_C
_RcQosPolicerCfgMode_Object=MibTableColumn
rcQosPolicerCfgMode=_RcQosPolicerCfgMode_Object((1,3,6,1,4,1,8886,1,33,2,6,1,3),_RcQosPolicerCfgMode_Type())
rcQosPolicerCfgMode.setMaxAccess(_B)
if mibBuilder.loadTexts:rcQosPolicerCfgMode.setStatus(_A)
class _RcQosPolicerCfgCIR_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1000))
_RcQosPolicerCfgCIR_Type.__name__=_C
_RcQosPolicerCfgCIR_Object=MibTableColumn
rcQosPolicerCfgCIR=_RcQosPolicerCfgCIR_Object((1,3,6,1,4,1,8886,1,33,2,6,1,4),_RcQosPolicerCfgCIR_Type())
rcQosPolicerCfgCIR.setMaxAccess(_B)
if mibBuilder.loadTexts:rcQosPolicerCfgCIR.setStatus(_A)
class _RcQosPolicerCfgEIR_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1000))
_RcQosPolicerCfgEIR_Type.__name__=_C
_RcQosPolicerCfgEIR_Object=MibTableColumn
rcQosPolicerCfgEIR=_RcQosPolicerCfgEIR_Object((1,3,6,1,4,1,8886,1,33,2,6,1,5),_RcQosPolicerCfgEIR_Type())
rcQosPolicerCfgEIR.setMaxAccess(_B)
if mibBuilder.loadTexts:rcQosPolicerCfgEIR.setStatus(_A)
_RcQosPolicerCfgCBS_Type=Integer32
_RcQosPolicerCfgCBS_Object=MibTableColumn
rcQosPolicerCfgCBS=_RcQosPolicerCfgCBS_Object((1,3,6,1,4,1,8886,1,33,2,6,1,6),_RcQosPolicerCfgCBS_Type())
rcQosPolicerCfgCBS.setMaxAccess(_B)
if mibBuilder.loadTexts:rcQosPolicerCfgCBS.setStatus(_A)
_RcQosPolicerCfgEBS_Type=Integer32
_RcQosPolicerCfgEBS_Object=MibTableColumn
rcQosPolicerCfgEBS=_RcQosPolicerCfgEBS_Object((1,3,6,1,4,1,8886,1,33,2,6,1,7),_RcQosPolicerCfgEBS_Type())
rcQosPolicerCfgEBS.setMaxAccess(_B)
if mibBuilder.loadTexts:rcQosPolicerCfgEBS.setStatus(_A)
_RcQosPolicerGreenActType_Type=Integer32
_RcQosPolicerGreenActType_Object=MibTableColumn
rcQosPolicerGreenActType=_RcQosPolicerGreenActType_Object((1,3,6,1,4,1,8886,1,33,2,6,1,8),_RcQosPolicerGreenActType_Type())
rcQosPolicerGreenActType.setMaxAccess(_B)
if mibBuilder.loadTexts:rcQosPolicerGreenActType.setStatus(_A)
class _RcQosPolicerGreenActDscp_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,63))
_RcQosPolicerGreenActDscp_Type.__name__=_C
_RcQosPolicerGreenActDscp_Object=MibTableColumn
rcQosPolicerGreenActDscp=_RcQosPolicerGreenActDscp_Object((1,3,6,1,4,1,8886,1,33,2,6,1,9),_RcQosPolicerGreenActDscp_Type())
rcQosPolicerGreenActDscp.setMaxAccess(_B)
if mibBuilder.loadTexts:rcQosPolicerGreenActDscp.setStatus(_A)
class _RcQosPolicerGreenActCos_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_RcQosPolicerGreenActCos_Type.__name__=_C
_RcQosPolicerGreenActCos_Object=MibTableColumn
rcQosPolicerGreenActCos=_RcQosPolicerGreenActCos_Object((1,3,6,1,4,1,8886,1,33,2,6,1,10),_RcQosPolicerGreenActCos_Type())
rcQosPolicerGreenActCos.setMaxAccess(_B)
if mibBuilder.loadTexts:rcQosPolicerGreenActCos.setStatus(_A)
class _RcQosPolicerGreenActLocalPrio_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_RcQosPolicerGreenActLocalPrio_Type.__name__=_C
_RcQosPolicerGreenActLocalPrio_Object=MibTableColumn
rcQosPolicerGreenActLocalPrio=_RcQosPolicerGreenActLocalPrio_Object((1,3,6,1,4,1,8886,1,33,2,6,1,11),_RcQosPolicerGreenActLocalPrio_Type())
rcQosPolicerGreenActLocalPrio.setMaxAccess(_B)
if mibBuilder.loadTexts:rcQosPolicerGreenActLocalPrio.setStatus(_A)
class _RcQosPolicerGreenActColor_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_P,0),(_J,1),(_K,2)))
_RcQosPolicerGreenActColor_Type.__name__=_C
_RcQosPolicerGreenActColor_Object=MibTableColumn
rcQosPolicerGreenActColor=_RcQosPolicerGreenActColor_Object((1,3,6,1,4,1,8886,1,33,2,6,1,12),_RcQosPolicerGreenActColor_Type())
rcQosPolicerGreenActColor.setMaxAccess(_B)
if mibBuilder.loadTexts:rcQosPolicerGreenActColor.setStatus(_A)
_RcQosPolicerGreenActCopytoCpu_Type=TruthValue
_RcQosPolicerGreenActCopytoCpu_Object=MibTableColumn
rcQosPolicerGreenActCopytoCpu=_RcQosPolicerGreenActCopytoCpu_Object((1,3,6,1,4,1,8886,1,33,2,6,1,13),_RcQosPolicerGreenActCopytoCpu_Type())
rcQosPolicerGreenActCopytoCpu.setMaxAccess(_B)
if mibBuilder.loadTexts:rcQosPolicerGreenActCopytoCpu.setStatus(_A)
_RcQosPolicerYellowActType_Type=Integer32
_RcQosPolicerYellowActType_Object=MibTableColumn
rcQosPolicerYellowActType=_RcQosPolicerYellowActType_Object((1,3,6,1,4,1,8886,1,33,2,6,1,14),_RcQosPolicerYellowActType_Type())
rcQosPolicerYellowActType.setMaxAccess(_B)
if mibBuilder.loadTexts:rcQosPolicerYellowActType.setStatus(_A)
class _RcQosPolicerYellowActDscp_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,63))
_RcQosPolicerYellowActDscp_Type.__name__=_C
_RcQosPolicerYellowActDscp_Object=MibTableColumn
rcQosPolicerYellowActDscp=_RcQosPolicerYellowActDscp_Object((1,3,6,1,4,1,8886,1,33,2,6,1,15),_RcQosPolicerYellowActDscp_Type())
rcQosPolicerYellowActDscp.setMaxAccess(_B)
if mibBuilder.loadTexts:rcQosPolicerYellowActDscp.setStatus(_A)
class _RcQosPolicerYellowActCos_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_RcQosPolicerYellowActCos_Type.__name__=_C
_RcQosPolicerYellowActCos_Object=MibTableColumn
rcQosPolicerYellowActCos=_RcQosPolicerYellowActCos_Object((1,3,6,1,4,1,8886,1,33,2,6,1,16),_RcQosPolicerYellowActCos_Type())
rcQosPolicerYellowActCos.setMaxAccess(_B)
if mibBuilder.loadTexts:rcQosPolicerYellowActCos.setStatus(_A)
class _RcQosPolicerYellowActLocalPrio_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_RcQosPolicerYellowActLocalPrio_Type.__name__=_C
_RcQosPolicerYellowActLocalPrio_Object=MibTableColumn
rcQosPolicerYellowActLocalPrio=_RcQosPolicerYellowActLocalPrio_Object((1,3,6,1,4,1,8886,1,33,2,6,1,17),_RcQosPolicerYellowActLocalPrio_Type())
rcQosPolicerYellowActLocalPrio.setMaxAccess(_B)
if mibBuilder.loadTexts:rcQosPolicerYellowActLocalPrio.setStatus(_A)
class _RcQosPolicerYellowActColor_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_P,0),(_I,1),(_K,2)))
_RcQosPolicerYellowActColor_Type.__name__=_C
_RcQosPolicerYellowActColor_Object=MibTableColumn
rcQosPolicerYellowActColor=_RcQosPolicerYellowActColor_Object((1,3,6,1,4,1,8886,1,33,2,6,1,18),_RcQosPolicerYellowActColor_Type())
rcQosPolicerYellowActColor.setMaxAccess(_B)
if mibBuilder.loadTexts:rcQosPolicerYellowActColor.setStatus(_A)
_RcQosPolicerYellowActCopytoCpu_Type=TruthValue
_RcQosPolicerYellowActCopytoCpu_Object=MibTableColumn
rcQosPolicerYellowActCopytoCpu=_RcQosPolicerYellowActCopytoCpu_Object((1,3,6,1,4,1,8886,1,33,2,6,1,19),_RcQosPolicerYellowActCopytoCpu_Type())
rcQosPolicerYellowActCopytoCpu.setMaxAccess(_B)
if mibBuilder.loadTexts:rcQosPolicerYellowActCopytoCpu.setStatus(_A)
_RcQosPolicerRedActType_Type=Integer32
_RcQosPolicerRedActType_Object=MibTableColumn
rcQosPolicerRedActType=_RcQosPolicerRedActType_Object((1,3,6,1,4,1,8886,1,33,2,6,1,20),_RcQosPolicerRedActType_Type())
rcQosPolicerRedActType.setMaxAccess(_B)
if mibBuilder.loadTexts:rcQosPolicerRedActType.setStatus(_A)
class _RcQosPolicerRedActDscp_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,63))
_RcQosPolicerRedActDscp_Type.__name__=_C
_RcQosPolicerRedActDscp_Object=MibTableColumn
rcQosPolicerRedActDscp=_RcQosPolicerRedActDscp_Object((1,3,6,1,4,1,8886,1,33,2,6,1,21),_RcQosPolicerRedActDscp_Type())
rcQosPolicerRedActDscp.setMaxAccess(_B)
if mibBuilder.loadTexts:rcQosPolicerRedActDscp.setStatus(_A)
class _RcQosPolicerRedActCos_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_RcQosPolicerRedActCos_Type.__name__=_C
_RcQosPolicerRedActCos_Object=MibTableColumn
rcQosPolicerRedActCos=_RcQosPolicerRedActCos_Object((1,3,6,1,4,1,8886,1,33,2,6,1,22),_RcQosPolicerRedActCos_Type())
rcQosPolicerRedActCos.setMaxAccess(_B)
if mibBuilder.loadTexts:rcQosPolicerRedActCos.setStatus(_A)
class _RcQosPolicerRedActLocalPrio_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_RcQosPolicerRedActLocalPrio_Type.__name__=_C
_RcQosPolicerRedActLocalPrio_Object=MibTableColumn
rcQosPolicerRedActLocalPrio=_RcQosPolicerRedActLocalPrio_Object((1,3,6,1,4,1,8886,1,33,2,6,1,23),_RcQosPolicerRedActLocalPrio_Type())
rcQosPolicerRedActLocalPrio.setMaxAccess(_B)
if mibBuilder.loadTexts:rcQosPolicerRedActLocalPrio.setStatus(_A)
class _RcQosPolicerRedActColor_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_P,0),(_I,1),(_J,2)))
_RcQosPolicerRedActColor_Type.__name__=_C
_RcQosPolicerRedActColor_Object=MibTableColumn
rcQosPolicerRedActColor=_RcQosPolicerRedActColor_Object((1,3,6,1,4,1,8886,1,33,2,6,1,24),_RcQosPolicerRedActColor_Type())
rcQosPolicerRedActColor.setMaxAccess(_B)
if mibBuilder.loadTexts:rcQosPolicerRedActColor.setStatus(_A)
_RcQosPolicerRedActCopytoCpu_Type=TruthValue
_RcQosPolicerRedActCopytoCpu_Object=MibTableColumn
rcQosPolicerRedActCopytoCpu=_RcQosPolicerRedActCopytoCpu_Object((1,3,6,1,4,1,8886,1,33,2,6,1,25),_RcQosPolicerRedActCopytoCpu_Type())
rcQosPolicerRedActCopytoCpu.setMaxAccess(_B)
if mibBuilder.loadTexts:rcQosPolicerRedActCopytoCpu.setStatus(_A)
class _RcQosPolicerColorMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_AN,0),(_AO,1)))
_RcQosPolicerColorMode_Type.__name__=_C
_RcQosPolicerColorMode_Object=MibTableColumn
rcQosPolicerColorMode=_RcQosPolicerColorMode_Object((1,3,6,1,4,1,8886,1,33,2,6,1,26),_RcQosPolicerColorMode_Type())
rcQosPolicerColorMode.setMaxAccess(_B)
if mibBuilder.loadTexts:rcQosPolicerColorMode.setStatus(_A)
_RcQoSPolicerRef_Type=Integer32
_RcQoSPolicerRef_Object=MibTableColumn
rcQoSPolicerRef=_RcQoSPolicerRef_Object((1,3,6,1,4,1,8886,1,33,2,6,1,27),_RcQoSPolicerRef_Type())
rcQoSPolicerRef.setMaxAccess(_G)
if mibBuilder.loadTexts:rcQoSPolicerRef.setStatus(_A)
_RcQosPolicerStatus_Type=RowStatus
_RcQosPolicerStatus_Object=MibTableColumn
rcQosPolicerStatus=_RcQosPolicerStatus_Object((1,3,6,1,4,1,8886,1,33,2,6,1,28),_RcQosPolicerStatus_Type())
rcQosPolicerStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:rcQosPolicerStatus.setStatus(_A)
_RcQosActionCfgTable_Object=MibTable
rcQosActionCfgTable=_RcQosActionCfgTable_Object((1,3,6,1,4,1,8886,1,33,2,7))
if mibBuilder.loadTexts:rcQosActionCfgTable.setStatus(_A)
_RcQosActionCfgEntry_Object=MibTableRow
rcQosActionCfgEntry=_RcQosActionCfgEntry_Object((1,3,6,1,4,1,8886,1,33,2,7,1))
rcQosActionCfgEntry.setIndexNames((0,_D,_AP),(0,_D,_AQ))
if mibBuilder.loadTexts:rcQosActionCfgEntry.setStatus(_A)
_RcQosActionPmapName_Type=ObjName
_RcQosActionPmapName_Object=MibTableColumn
rcQosActionPmapName=_RcQosActionPmapName_Object((1,3,6,1,4,1,8886,1,33,2,7,1,1),_RcQosActionPmapName_Type())
rcQosActionPmapName.setMaxAccess(_F)
if mibBuilder.loadTexts:rcQosActionPmapName.setStatus(_A)
_RcQosActionCmapName_Type=ObjName
_RcQosActionCmapName_Object=MibTableColumn
rcQosActionCmapName=_RcQosActionCmapName_Object((1,3,6,1,4,1,8886,1,33,2,7,1,2),_RcQosActionCmapName_Type())
rcQosActionCmapName.setMaxAccess(_F)
if mibBuilder.loadTexts:rcQosActionCmapName.setStatus(_A)
class _RcQosActionType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*((_P,0),('set-dscp',1),('set-cos',2),('set-ipprec',3)))
_RcQosActionType_Type.__name__=_C
_RcQosActionType_Object=MibTableColumn
rcQosActionType=_RcQosActionType_Object((1,3,6,1,4,1,8886,1,33,2,7,1,3),_RcQosActionType_Type())
rcQosActionType.setMaxAccess(_B)
if mibBuilder.loadTexts:rcQosActionType.setStatus(_A)
class _RcQosActionSetValue_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,63))
_RcQosActionSetValue_Type.__name__=_C
_RcQosActionSetValue_Object=MibTableColumn
rcQosActionSetValue=_RcQosActionSetValue_Object((1,3,6,1,4,1,8886,1,33,2,7,1,4),_RcQosActionSetValue_Type())
rcQosActionSetValue.setMaxAccess(_B)
if mibBuilder.loadTexts:rcQosActionSetValue.setStatus(_A)
_RcQosActionPoliceName_Type=ObjName
_RcQosActionPoliceName_Object=MibTableColumn
rcQosActionPoliceName=_RcQosActionPoliceName_Object((1,3,6,1,4,1,8886,1,33,2,7,1,5),_RcQosActionPoliceName_Type())
rcQosActionPoliceName.setMaxAccess(_B)
if mibBuilder.loadTexts:rcQosActionPoliceName.setStatus(_A)
_RcQosActionStatsEnable_Type=EnableVar
_RcQosActionStatsEnable_Object=MibTableColumn
rcQosActionStatsEnable=_RcQosActionStatsEnable_Object((1,3,6,1,4,1,8886,1,33,2,7,1,6),_RcQosActionStatsEnable_Type())
rcQosActionStatsEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:rcQosActionStatsEnable.setStatus(_A)
_RcQosActionStatus_Type=RowStatus
_RcQosActionStatus_Object=MibTableColumn
rcQosActionStatus=_RcQosActionStatus_Object((1,3,6,1,4,1,8886,1,33,2,7,1,7),_RcQosActionStatus_Type())
rcQosActionStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:rcQosActionStatus.setStatus(_A)
_RcQosActionRedirectPort_Type=Integer32
_RcQosActionRedirectPort_Object=MibTableColumn
rcQosActionRedirectPort=_RcQosActionRedirectPort_Object((1,3,6,1,4,1,8886,1,33,2,7,1,8),_RcQosActionRedirectPort_Type())
rcQosActionRedirectPort.setMaxAccess(_B)
if mibBuilder.loadTexts:rcQosActionRedirectPort.setStatus(_A)
class _RcQosActionSetVlan_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4094))
_RcQosActionSetVlan_Type.__name__=_C
_RcQosActionSetVlan_Object=MibTableColumn
rcQosActionSetVlan=_RcQosActionSetVlan_Object((1,3,6,1,4,1,8886,1,33,2,7,1,9),_RcQosActionSetVlan_Type())
rcQosActionSetVlan.setMaxAccess(_B)
if mibBuilder.loadTexts:rcQosActionSetVlan.setStatus(_A)
class _RcQosActionSetInnerVlan_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4094))
_RcQosActionSetInnerVlan_Type.__name__=_C
_RcQosActionSetInnerVlan_Object=MibTableColumn
rcQosActionSetInnerVlan=_RcQosActionSetInnerVlan_Object((1,3,6,1,4,1,8886,1,33,2,7,1,10),_RcQosActionSetInnerVlan_Type())
rcQosActionSetInnerVlan.setMaxAccess(_B)
if mibBuilder.loadTexts:rcQosActionSetInnerVlan.setStatus(_A)
class _RcQosActionAddOuterVlan_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4094))
_RcQosActionAddOuterVlan_Type.__name__=_C
_RcQosActionAddOuterVlan_Object=MibTableColumn
rcQosActionAddOuterVlan=_RcQosActionAddOuterVlan_Object((1,3,6,1,4,1,8886,1,33,2,7,1,11),_RcQosActionAddOuterVlan_Type())
rcQosActionAddOuterVlan.setMaxAccess(_B)
if mibBuilder.loadTexts:rcQosActionAddOuterVlan.setStatus(_A)
_RcQosActionCopyToMirror_Type=EnableVar
_RcQosActionCopyToMirror_Object=MibTableColumn
rcQosActionCopyToMirror=_RcQosActionCopyToMirror_Object((1,3,6,1,4,1,8886,1,33,2,7,1,12),_RcQosActionCopyToMirror_Type())
rcQosActionCopyToMirror.setMaxAccess(_B)
if mibBuilder.loadTexts:rcQosActionCopyToMirror.setStatus(_A)
_RcQosActionMirrorToPort_Type=Integer32
_RcQosActionMirrorToPort_Object=MibTableColumn
rcQosActionMirrorToPort=_RcQosActionMirrorToPort_Object((1,3,6,1,4,1,8886,1,33,2,7,1,13),_RcQosActionMirrorToPort_Type())
rcQosActionMirrorToPort.setMaxAccess(_B)
if mibBuilder.loadTexts:rcQosActionMirrorToPort.setStatus(_A)
class _RcQosActionSetLocalPriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,8))
_RcQosActionSetLocalPriority_Type.__name__=_C
_RcQosActionSetLocalPriority_Object=MibTableColumn
rcQosActionSetLocalPriority=_RcQosActionSetLocalPriority_Object((1,3,6,1,4,1,8886,1,33,2,7,1,14),_RcQosActionSetLocalPriority_Type())
rcQosActionSetLocalPriority.setMaxAccess(_B)
if mibBuilder.loadTexts:rcQosActionSetLocalPriority.setStatus(_A)
_RcQosActionHierarchyPoliceName_Type=ObjName
_RcQosActionHierarchyPoliceName_Object=MibTableColumn
rcQosActionHierarchyPoliceName=_RcQosActionHierarchyPoliceName_Object((1,3,6,1,4,1,8886,1,33,2,7,1,15),_RcQosActionHierarchyPoliceName_Type())
rcQosActionHierarchyPoliceName.setMaxAccess(_B)
if mibBuilder.loadTexts:rcQosActionHierarchyPoliceName.setStatus(_A)
class _RcQosActionSetIpPrece_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,8))
_RcQosActionSetIpPrece_Type.__name__=_C
_RcQosActionSetIpPrece_Object=MibTableColumn
rcQosActionSetIpPrece=_RcQosActionSetIpPrece_Object((1,3,6,1,4,1,8886,1,33,2,7,1,16),_RcQosActionSetIpPrece_Type())
rcQosActionSetIpPrece.setMaxAccess(_B)
if mibBuilder.loadTexts:rcQosActionSetIpPrece.setStatus(_A)
class _RcQosActionSetIpDscp_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,64))
_RcQosActionSetIpDscp_Type.__name__=_C
_RcQosActionSetIpDscp_Object=MibTableColumn
rcQosActionSetIpDscp=_RcQosActionSetIpDscp_Object((1,3,6,1,4,1,8886,1,33,2,7,1,17),_RcQosActionSetIpDscp_Type())
rcQosActionSetIpDscp.setMaxAccess(_B)
if mibBuilder.loadTexts:rcQosActionSetIpDscp.setStatus(_A)
class _RcQosActionSetCos_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,8))
_RcQosActionSetCos_Type.__name__=_C
_RcQosActionSetCos_Object=MibTableColumn
rcQosActionSetCos=_RcQosActionSetCos_Object((1,3,6,1,4,1,8886,1,33,2,7,1,18),_RcQosActionSetCos_Type())
rcQosActionSetCos.setMaxAccess(_B)
if mibBuilder.loadTexts:rcQosActionSetCos.setStatus(_A)
class _RcQosActionSetIPAddressType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,16))
_RcQosActionSetIPAddressType_Type.__name__=_C
_RcQosActionSetIPAddressType_Object=MibTableColumn
rcQosActionSetIPAddressType=_RcQosActionSetIPAddressType_Object((1,3,6,1,4,1,8886,1,33,2,7,1,19),_RcQosActionSetIPAddressType_Type())
rcQosActionSetIPAddressType.setMaxAccess(_B)
if mibBuilder.loadTexts:rcQosActionSetIPAddressType.setStatus(_A)
_RcQosActionSetIPAddress_Type=InetAddress
_RcQosActionSetIPAddress_Object=MibTableColumn
rcQosActionSetIPAddress=_RcQosActionSetIPAddress_Object((1,3,6,1,4,1,8886,1,33,2,7,1,20),_RcQosActionSetIPAddress_Type())
rcQosActionSetIPAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:rcQosActionSetIPAddress.setStatus(_A)
class _RcQosActionCopyToMirrorSession_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4))
_RcQosActionCopyToMirrorSession_Type.__name__=_C
_RcQosActionCopyToMirrorSession_Object=MibTableColumn
rcQosActionCopyToMirrorSession=_RcQosActionCopyToMirrorSession_Object((1,3,6,1,4,1,8886,1,33,2,7,1,21),_RcQosActionCopyToMirrorSession_Type())
rcQosActionCopyToMirrorSession.setMaxAccess(_B)
if mibBuilder.loadTexts:rcQosActionCopyToMirrorSession.setStatus(_A)
_RcQosServicePolicyEgressTable_Object=MibTable
rcQosServicePolicyEgressTable=_RcQosServicePolicyEgressTable_Object((1,3,6,1,4,1,8886,1,33,2,8))
if mibBuilder.loadTexts:rcQosServicePolicyEgressTable.setStatus(_A)
_RcQosServicePolicyEgressEntry_Object=MibTableRow
rcQosServicePolicyEgressEntry=_RcQosServicePolicyEgressEntry_Object((1,3,6,1,4,1,8886,1,33,2,8,1))
rcQosServicePolicyEgressEntry.setIndexNames((0,_D,_AR))
if mibBuilder.loadTexts:rcQosServicePolicyEgressEntry.setStatus(_A)
_RcQosServicePolicyEgressIndex_Type=Integer32
_RcQosServicePolicyEgressIndex_Object=MibTableColumn
rcQosServicePolicyEgressIndex=_RcQosServicePolicyEgressIndex_Object((1,3,6,1,4,1,8886,1,33,2,8,1,1),_RcQosServicePolicyEgressIndex_Type())
rcQosServicePolicyEgressIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:rcQosServicePolicyEgressIndex.setStatus(_A)
_RcQosServicePolicyEgressMapName_Type=ObjName
_RcQosServicePolicyEgressMapName_Object=MibTableColumn
rcQosServicePolicyEgressMapName=_RcQosServicePolicyEgressMapName_Object((1,3,6,1,4,1,8886,1,33,2,8,1,2),_RcQosServicePolicyEgressMapName_Type())
rcQosServicePolicyEgressMapName.setMaxAccess(_B)
if mibBuilder.loadTexts:rcQosServicePolicyEgressMapName.setStatus(_A)
_RcQosServicePolicyEgressStatus_Type=RowStatus
_RcQosServicePolicyEgressStatus_Object=MibTableColumn
rcQosServicePolicyEgressStatus=_RcQosServicePolicyEgressStatus_Object((1,3,6,1,4,1,8886,1,33,2,8,1,3),_RcQosServicePolicyEgressStatus_Type())
rcQosServicePolicyEgressStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:rcQosServicePolicyEgressStatus.setStatus(_A)
_RcQosCosServicePolicyTable_Object=MibTable
rcQosCosServicePolicyTable=_RcQosCosServicePolicyTable_Object((1,3,6,1,4,1,8886,1,33,2,9))
if mibBuilder.loadTexts:rcQosCosServicePolicyTable.setStatus(_A)
_RcQosCosServicePolicyEntry_Object=MibTableRow
rcQosCosServicePolicyEntry=_RcQosCosServicePolicyEntry_Object((1,3,6,1,4,1,8886,1,33,2,9,1))
rcQosCosServicePolicyEntry.setIndexNames((0,_D,_AS),(0,_D,_AT))
if mibBuilder.loadTexts:rcQosCosServicePolicyEntry.setStatus(_A)
_RcQosCosServicePolicyPort_Type=Integer32
_RcQosCosServicePolicyPort_Object=MibTableColumn
rcQosCosServicePolicyPort=_RcQosCosServicePolicyPort_Object((1,3,6,1,4,1,8886,1,33,2,9,1,1),_RcQosCosServicePolicyPort_Type())
rcQosCosServicePolicyPort.setMaxAccess(_F)
if mibBuilder.loadTexts:rcQosCosServicePolicyPort.setStatus(_A)
_RcQosCosServicePolicyVlan_Type=Integer32
_RcQosCosServicePolicyVlan_Object=MibTableColumn
rcQosCosServicePolicyVlan=_RcQosCosServicePolicyVlan_Object((1,3,6,1,4,1,8886,1,33,2,9,1,2),_RcQosCosServicePolicyVlan_Type())
rcQosCosServicePolicyVlan.setMaxAccess(_F)
if mibBuilder.loadTexts:rcQosCosServicePolicyVlan.setStatus(_A)
class _RcQosCosServicePolicyMapName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,16))
_RcQosCosServicePolicyMapName_Type.__name__=_H
_RcQosCosServicePolicyMapName_Object=MibTableColumn
rcQosCosServicePolicyMapName=_RcQosCosServicePolicyMapName_Object((1,3,6,1,4,1,8886,1,33,2,9,1,3),_RcQosCosServicePolicyMapName_Type())
rcQosCosServicePolicyMapName.setMaxAccess(_B)
if mibBuilder.loadTexts:rcQosCosServicePolicyMapName.setStatus(_A)
_RcQosCosServicePolicyRowStatus_Type=RowStatus
_RcQosCosServicePolicyRowStatus_Object=MibTableColumn
rcQosCosServicePolicyRowStatus=_RcQosCosServicePolicyRowStatus_Object((1,3,6,1,4,1,8886,1,33,2,9,1,4),_RcQosCosServicePolicyRowStatus_Type())
rcQosCosServicePolicyRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:rcQosCosServicePolicyRowStatus.setStatus(_A)
_RcQosVlanPolicyTable_Object=MibTable
rcQosVlanPolicyTable=_RcQosVlanPolicyTable_Object((1,3,6,1,4,1,8886,1,33,2,10))
if mibBuilder.loadTexts:rcQosVlanPolicyTable.setStatus(_A)
_RcQosVlanPolicyEntry_Object=MibTableRow
rcQosVlanPolicyEntry=_RcQosVlanPolicyEntry_Object((1,3,6,1,4,1,8886,1,33,2,10,1))
rcQosVlanPolicyEntry.setIndexNames((0,_D,_AU),(0,_D,_AV))
if mibBuilder.loadTexts:rcQosVlanPolicyEntry.setStatus(_A)
class _RcQosVlanPolicyPmapName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,16))
_RcQosVlanPolicyPmapName_Type.__name__=_H
_RcQosVlanPolicyPmapName_Object=MibTableColumn
rcQosVlanPolicyPmapName=_RcQosVlanPolicyPmapName_Object((1,3,6,1,4,1,8886,1,33,2,10,1,1),_RcQosVlanPolicyPmapName_Type())
rcQosVlanPolicyPmapName.setMaxAccess(_F)
if mibBuilder.loadTexts:rcQosVlanPolicyPmapName.setStatus(_A)
class _RcQosVlanPolicyVlan_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4094))
_RcQosVlanPolicyVlan_Type.__name__=_C
_RcQosVlanPolicyVlan_Object=MibTableColumn
rcQosVlanPolicyVlan=_RcQosVlanPolicyVlan_Object((1,3,6,1,4,1,8886,1,33,2,10,1,2),_RcQosVlanPolicyVlan_Type())
rcQosVlanPolicyVlan.setMaxAccess(_F)
if mibBuilder.loadTexts:rcQosVlanPolicyVlan.setStatus(_A)
class _RcQosVlanPolicyPolicerName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,16))
_RcQosVlanPolicyPolicerName_Type.__name__=_H
_RcQosVlanPolicyPolicerName_Object=MibTableColumn
rcQosVlanPolicyPolicerName=_RcQosVlanPolicyPolicerName_Object((1,3,6,1,4,1,8886,1,33,2,10,1,3),_RcQosVlanPolicyPolicerName_Type())
rcQosVlanPolicyPolicerName.setMaxAccess(_B)
if mibBuilder.loadTexts:rcQosVlanPolicyPolicerName.setStatus(_A)
_RcQosVlanPolicyRowStatus_Type=RowStatus
_RcQosVlanPolicyRowStatus_Object=MibTableColumn
rcQosVlanPolicyRowStatus=_RcQosVlanPolicyRowStatus_Object((1,3,6,1,4,1,8886,1,33,2,10,1,4),_RcQosVlanPolicyRowStatus_Type())
rcQosVlanPolicyRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:rcQosVlanPolicyRowStatus.setStatus(_A)
_RcQosCosPolicyTable_Object=MibTable
rcQosCosPolicyTable=_RcQosCosPolicyTable_Object((1,3,6,1,4,1,8886,1,33,2,11))
if mibBuilder.loadTexts:rcQosCosPolicyTable.setStatus(_A)
_RcQosCosPolicyEntry_Object=MibTableRow
rcQosCosPolicyEntry=_RcQosCosPolicyEntry_Object((1,3,6,1,4,1,8886,1,33,2,11,1))
rcQosCosPolicyEntry.setIndexNames((0,_D,_AW),(0,_D,_AX))
if mibBuilder.loadTexts:rcQosCosPolicyEntry.setStatus(_A)
class _RcQosCosPolicyPmapName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,16))
_RcQosCosPolicyPmapName_Type.__name__=_H
_RcQosCosPolicyPmapName_Object=MibTableColumn
rcQosCosPolicyPmapName=_RcQosCosPolicyPmapName_Object((1,3,6,1,4,1,8886,1,33,2,11,1,1),_RcQosCosPolicyPmapName_Type())
rcQosCosPolicyPmapName.setMaxAccess(_F)
if mibBuilder.loadTexts:rcQosCosPolicyPmapName.setStatus(_A)
class _RcQosCosPolicyCos_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,8))
_RcQosCosPolicyCos_Type.__name__=_C
_RcQosCosPolicyCos_Object=MibTableColumn
rcQosCosPolicyCos=_RcQosCosPolicyCos_Object((1,3,6,1,4,1,8886,1,33,2,11,1,2),_RcQosCosPolicyCos_Type())
rcQosCosPolicyCos.setMaxAccess(_F)
if mibBuilder.loadTexts:rcQosCosPolicyCos.setStatus(_A)
class _RcQosCosPolicyPolicerName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,16))
_RcQosCosPolicyPolicerName_Type.__name__=_H
_RcQosCosPolicyPolicerName_Object=MibTableColumn
rcQosCosPolicyPolicerName=_RcQosCosPolicyPolicerName_Object((1,3,6,1,4,1,8886,1,33,2,11,1,3),_RcQosCosPolicyPolicerName_Type())
rcQosCosPolicyPolicerName.setMaxAccess(_B)
if mibBuilder.loadTexts:rcQosCosPolicyPolicerName.setStatus(_A)
_RcQosCosPolicyRowStatus_Type=RowStatus
_RcQosCosPolicyRowStatus_Object=MibTableColumn
rcQosCosPolicyRowStatus=_RcQosCosPolicyRowStatus_Object((1,3,6,1,4,1,8886,1,33,2,11,1,4),_RcQosCosPolicyRowStatus_Type())
rcQosCosPolicyRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:rcQosCosPolicyRowStatus.setStatus(_A)
_RcQosBandwidthProfileCfgTable_Object=MibTable
rcQosBandwidthProfileCfgTable=_RcQosBandwidthProfileCfgTable_Object((1,3,6,1,4,1,8886,1,33,2,12))
if mibBuilder.loadTexts:rcQosBandwidthProfileCfgTable.setStatus(_A)
_RcQosBandwidthProfileCfgEntry_Object=MibTableRow
rcQosBandwidthProfileCfgEntry=_RcQosBandwidthProfileCfgEntry_Object((1,3,6,1,4,1,8886,1,33,2,12,1))
rcQosBandwidthProfileCfgEntry.setIndexNames((0,_D,_AY))
if mibBuilder.loadTexts:rcQosBandwidthProfileCfgEntry.setStatus(_A)
_RcQosBandwidthProfileCfgIndex_Type=Integer32
_RcQosBandwidthProfileCfgIndex_Object=MibTableColumn
rcQosBandwidthProfileCfgIndex=_RcQosBandwidthProfileCfgIndex_Object((1,3,6,1,4,1,8886,1,33,2,12,1,1),_RcQosBandwidthProfileCfgIndex_Type())
rcQosBandwidthProfileCfgIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:rcQosBandwidthProfileCfgIndex.setStatus(_A)
class _RcQosBandwidthProfileCfgCIR_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,10000))
_RcQosBandwidthProfileCfgCIR_Type.__name__=_C
_RcQosBandwidthProfileCfgCIR_Object=MibTableColumn
rcQosBandwidthProfileCfgCIR=_RcQosBandwidthProfileCfgCIR_Object((1,3,6,1,4,1,8886,1,33,2,12,1,2),_RcQosBandwidthProfileCfgCIR_Type())
rcQosBandwidthProfileCfgCIR.setMaxAccess(_B)
if mibBuilder.loadTexts:rcQosBandwidthProfileCfgCIR.setStatus(_A)
class _RcQosBandwidthProfileCfgEIR_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,10000))
_RcQosBandwidthProfileCfgEIR_Type.__name__=_C
_RcQosBandwidthProfileCfgEIR_Object=MibTableColumn
rcQosBandwidthProfileCfgEIR=_RcQosBandwidthProfileCfgEIR_Object((1,3,6,1,4,1,8886,1,33,2,12,1,3),_RcQosBandwidthProfileCfgEIR_Type())
rcQosBandwidthProfileCfgEIR.setMaxAccess(_B)
if mibBuilder.loadTexts:rcQosBandwidthProfileCfgEIR.setStatus(_A)
_RcQosBandwidthProfileCfgCBS_Type=Integer32
_RcQosBandwidthProfileCfgCBS_Object=MibTableColumn
rcQosBandwidthProfileCfgCBS=_RcQosBandwidthProfileCfgCBS_Object((1,3,6,1,4,1,8886,1,33,2,12,1,4),_RcQosBandwidthProfileCfgCBS_Type())
rcQosBandwidthProfileCfgCBS.setMaxAccess(_B)
if mibBuilder.loadTexts:rcQosBandwidthProfileCfgCBS.setStatus(_A)
_RcQosBandwidthProfileCfgEBS_Type=Integer32
_RcQosBandwidthProfileCfgEBS_Object=MibTableColumn
rcQosBandwidthProfileCfgEBS=_RcQosBandwidthProfileCfgEBS_Object((1,3,6,1,4,1,8886,1,33,2,12,1,5),_RcQosBandwidthProfileCfgEBS_Type())
rcQosBandwidthProfileCfgEBS.setMaxAccess(_B)
if mibBuilder.loadTexts:rcQosBandwidthProfileCfgEBS.setStatus(_A)
class _RcQosBandwidthProfileColorMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_AN,0),(_AO,1)))
_RcQosBandwidthProfileColorMode_Type.__name__=_C
_RcQosBandwidthProfileColorMode_Object=MibTableColumn
rcQosBandwidthProfileColorMode=_RcQosBandwidthProfileColorMode_Object((1,3,6,1,4,1,8886,1,33,2,12,1,6),_RcQosBandwidthProfileColorMode_Type())
rcQosBandwidthProfileColorMode.setMaxAccess(_B)
if mibBuilder.loadTexts:rcQosBandwidthProfileColorMode.setStatus(_A)
class _RcQosBandwidthProfileCoupling_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_N,1),(_O,2)))
_RcQosBandwidthProfileCoupling_Type.__name__=_C
_RcQosBandwidthProfileCoupling_Object=MibTableColumn
rcQosBandwidthProfileCoupling=_RcQosBandwidthProfileCoupling_Object((1,3,6,1,4,1,8886,1,33,2,12,1,7),_RcQosBandwidthProfileCoupling_Type())
rcQosBandwidthProfileCoupling.setMaxAccess(_B)
if mibBuilder.loadTexts:rcQosBandwidthProfileCoupling.setStatus(_A)
_RcQoSBandwidthProfileRef_Type=Integer32
_RcQoSBandwidthProfileRef_Object=MibTableColumn
rcQoSBandwidthProfileRef=_RcQoSBandwidthProfileRef_Object((1,3,6,1,4,1,8886,1,33,2,12,1,8),_RcQoSBandwidthProfileRef_Type())
rcQoSBandwidthProfileRef.setMaxAccess(_G)
if mibBuilder.loadTexts:rcQoSBandwidthProfileRef.setStatus(_A)
_RcQosBandwidthProfileStatus_Type=RowStatus
_RcQosBandwidthProfileStatus_Object=MibTableColumn
rcQosBandwidthProfileStatus=_RcQosBandwidthProfileStatus_Object((1,3,6,1,4,1,8886,1,33,2,12,1,9),_RcQosBandwidthProfileStatus_Type())
rcQosBandwidthProfileStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:rcQosBandwidthProfileStatus.setStatus(_A)
class _RcQosBandwidthProfileDesc_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_RcQosBandwidthProfileDesc_Type.__name__=_H
_RcQosBandwidthProfileDesc_Object=MibTableColumn
rcQosBandwidthProfileDesc=_RcQosBandwidthProfileDesc_Object((1,3,6,1,4,1,8886,1,33,2,12,1,10),_RcQosBandwidthProfileDesc_Type())
rcQosBandwidthProfileDesc.setMaxAccess(_B)
if mibBuilder.loadTexts:rcQosBandwidthProfileDesc.setStatus(_A)
_RcQosHierarchyCosIndexCfgTable_Object=MibTable
rcQosHierarchyCosIndexCfgTable=_RcQosHierarchyCosIndexCfgTable_Object((1,3,6,1,4,1,8886,1,33,2,13))
if mibBuilder.loadTexts:rcQosHierarchyCosIndexCfgTable.setStatus(_A)
_RcQosHierarchyCosIndexCfgEntry_Object=MibTableRow
rcQosHierarchyCosIndexCfgEntry=_RcQosHierarchyCosIndexCfgEntry_Object((1,3,6,1,4,1,8886,1,33,2,13,1))
rcQosHierarchyCosIndexCfgEntry.setIndexNames((0,_D,_AZ))
if mibBuilder.loadTexts:rcQosHierarchyCosIndexCfgEntry.setStatus(_A)
_RcQosHierarchyCosIndex_Type=Integer32
_RcQosHierarchyCosIndex_Object=MibTableColumn
rcQosHierarchyCosIndex=_RcQosHierarchyCosIndex_Object((1,3,6,1,4,1,8886,1,33,2,13,1,1),_RcQosHierarchyCosIndex_Type())
rcQosHierarchyCosIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:rcQosHierarchyCosIndex.setStatus(_A)
_RcQosHierarchyCosRef_Type=Integer32
_RcQosHierarchyCosRef_Object=MibTableColumn
rcQosHierarchyCosRef=_RcQosHierarchyCosRef_Object((1,3,6,1,4,1,8886,1,33,2,13,1,2),_RcQosHierarchyCosRef_Type())
rcQosHierarchyCosRef.setMaxAccess(_G)
if mibBuilder.loadTexts:rcQosHierarchyCosRef.setStatus(_A)
_RcQosHierarchyCosCfgStatus_Type=RowStatus
_RcQosHierarchyCosCfgStatus_Object=MibTableColumn
rcQosHierarchyCosCfgStatus=_RcQosHierarchyCosCfgStatus_Object((1,3,6,1,4,1,8886,1,33,2,13,1,3),_RcQosHierarchyCosCfgStatus_Type())
rcQosHierarchyCosCfgStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:rcQosHierarchyCosCfgStatus.setStatus(_A)
class _RcQosHierarchyCosCfgDesc_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_RcQosHierarchyCosCfgDesc_Type.__name__=_H
_RcQosHierarchyCosCfgDesc_Object=MibTableColumn
rcQosHierarchyCosCfgDesc=_RcQosHierarchyCosCfgDesc_Object((1,3,6,1,4,1,8886,1,33,2,13,1,4),_RcQosHierarchyCosCfgDesc_Type())
rcQosHierarchyCosCfgDesc.setMaxAccess(_B)
if mibBuilder.loadTexts:rcQosHierarchyCosCfgDesc.setStatus(_A)
_RcQosHCosBandwidthProfileTable_Object=MibTable
rcQosHCosBandwidthProfileTable=_RcQosHCosBandwidthProfileTable_Object((1,3,6,1,4,1,8886,1,33,2,14))
if mibBuilder.loadTexts:rcQosHCosBandwidthProfileTable.setStatus(_A)
_RcQosHCosBandwidthProfileEntry_Object=MibTableRow
rcQosHCosBandwidthProfileEntry=_RcQosHCosBandwidthProfileEntry_Object((1,3,6,1,4,1,8886,1,33,2,14,1))
rcQosHCosBandwidthProfileEntry.setIndexNames((0,_D,_Aa),(0,_D,_Ab))
if mibBuilder.loadTexts:rcQosHCosBandwidthProfileEntry.setStatus(_A)
_RcQosHCosBandwidthProfileIndex_Type=Integer32
_RcQosHCosBandwidthProfileIndex_Object=MibTableColumn
rcQosHCosBandwidthProfileIndex=_RcQosHCosBandwidthProfileIndex_Object((1,3,6,1,4,1,8886,1,33,2,14,1,1),_RcQosHCosBandwidthProfileIndex_Type())
rcQosHCosBandwidthProfileIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:rcQosHCosBandwidthProfileIndex.setStatus(_A)
class _RcQosHCosBandwidthProfileCos_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,8))
_RcQosHCosBandwidthProfileCos_Type.__name__=_C
_RcQosHCosBandwidthProfileCos_Object=MibTableColumn
rcQosHCosBandwidthProfileCos=_RcQosHCosBandwidthProfileCos_Object((1,3,6,1,4,1,8886,1,33,2,14,1,2),_RcQosHCosBandwidthProfileCos_Type())
rcQosHCosBandwidthProfileCos.setMaxAccess(_F)
if mibBuilder.loadTexts:rcQosHCosBandwidthProfileCos.setStatus(_A)
_RcQosHCosBandwidthProfileBwpIndex_Type=Integer32
_RcQosHCosBandwidthProfileBwpIndex_Object=MibTableColumn
rcQosHCosBandwidthProfileBwpIndex=_RcQosHCosBandwidthProfileBwpIndex_Object((1,3,6,1,4,1,8886,1,33,2,14,1,3),_RcQosHCosBandwidthProfileBwpIndex_Type())
rcQosHCosBandwidthProfileBwpIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:rcQosHCosBandwidthProfileBwpIndex.setStatus(_A)
_RcQoSHCosBandwidthProfileRef_Type=Integer32
_RcQoSHCosBandwidthProfileRef_Object=MibTableColumn
rcQoSHCosBandwidthProfileRef=_RcQoSHCosBandwidthProfileRef_Object((1,3,6,1,4,1,8886,1,33,2,14,1,4),_RcQoSHCosBandwidthProfileRef_Type())
rcQoSHCosBandwidthProfileRef.setMaxAccess(_G)
if mibBuilder.loadTexts:rcQoSHCosBandwidthProfileRef.setStatus(_A)
_RcQosHCosBandwidthProfileRowStatus_Type=RowStatus
_RcQosHCosBandwidthProfileRowStatus_Object=MibTableColumn
rcQosHCosBandwidthProfileRowStatus=_RcQosHCosBandwidthProfileRowStatus_Object((1,3,6,1,4,1,8886,1,33,2,14,1,5),_RcQosHCosBandwidthProfileRowStatus_Type())
rcQosHCosBandwidthProfileRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:rcQosHCosBandwidthProfileRowStatus.setStatus(_A)
_RcQosHierarchyVlanIndexCfgTable_Object=MibTable
rcQosHierarchyVlanIndexCfgTable=_RcQosHierarchyVlanIndexCfgTable_Object((1,3,6,1,4,1,8886,1,33,2,15))
if mibBuilder.loadTexts:rcQosHierarchyVlanIndexCfgTable.setStatus(_A)
_RcQosHierarchyVlanIndexCfgEntry_Object=MibTableRow
rcQosHierarchyVlanIndexCfgEntry=_RcQosHierarchyVlanIndexCfgEntry_Object((1,3,6,1,4,1,8886,1,33,2,15,1))
rcQosHierarchyVlanIndexCfgEntry.setIndexNames((0,_D,_Ac))
if mibBuilder.loadTexts:rcQosHierarchyVlanIndexCfgEntry.setStatus(_A)
_RcQosHierarchyVlanIndex_Type=Integer32
_RcQosHierarchyVlanIndex_Object=MibTableColumn
rcQosHierarchyVlanIndex=_RcQosHierarchyVlanIndex_Object((1,3,6,1,4,1,8886,1,33,2,15,1,1),_RcQosHierarchyVlanIndex_Type())
rcQosHierarchyVlanIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:rcQosHierarchyVlanIndex.setStatus(_A)
_RcQosHierarchyVlanRef_Type=Integer32
_RcQosHierarchyVlanRef_Object=MibTableColumn
rcQosHierarchyVlanRef=_RcQosHierarchyVlanRef_Object((1,3,6,1,4,1,8886,1,33,2,15,1,2),_RcQosHierarchyVlanRef_Type())
rcQosHierarchyVlanRef.setMaxAccess(_G)
if mibBuilder.loadTexts:rcQosHierarchyVlanRef.setStatus(_A)
_RcQosHierarchyVlanCfgStatus_Type=RowStatus
_RcQosHierarchyVlanCfgStatus_Object=MibTableColumn
rcQosHierarchyVlanCfgStatus=_RcQosHierarchyVlanCfgStatus_Object((1,3,6,1,4,1,8886,1,33,2,15,1,3),_RcQosHierarchyVlanCfgStatus_Type())
rcQosHierarchyVlanCfgStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:rcQosHierarchyVlanCfgStatus.setStatus(_A)
class _RcQosHierarchyVlanCfgDesc_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_RcQosHierarchyVlanCfgDesc_Type.__name__=_H
_RcQosHierarchyVlanCfgDesc_Object=MibTableColumn
rcQosHierarchyVlanCfgDesc=_RcQosHierarchyVlanCfgDesc_Object((1,3,6,1,4,1,8886,1,33,2,15,1,4),_RcQosHierarchyVlanCfgDesc_Type())
rcQosHierarchyVlanCfgDesc.setMaxAccess(_B)
if mibBuilder.loadTexts:rcQosHierarchyVlanCfgDesc.setStatus(_A)
_RcQosHVlanBandwidthProfileTable_Object=MibTable
rcQosHVlanBandwidthProfileTable=_RcQosHVlanBandwidthProfileTable_Object((1,3,6,1,4,1,8886,1,33,2,16))
if mibBuilder.loadTexts:rcQosHVlanBandwidthProfileTable.setStatus(_A)
_RcQosHVlanBandwidthProfileEntry_Object=MibTableRow
rcQosHVlanBandwidthProfileEntry=_RcQosHVlanBandwidthProfileEntry_Object((1,3,6,1,4,1,8886,1,33,2,16,1))
rcQosHVlanBandwidthProfileEntry.setIndexNames((0,_D,_Ad),(0,_D,_Ae))
if mibBuilder.loadTexts:rcQosHVlanBandwidthProfileEntry.setStatus(_A)
_RcQosHVlanBandwidthProfileIndex_Type=Integer32
_RcQosHVlanBandwidthProfileIndex_Object=MibTableColumn
rcQosHVlanBandwidthProfileIndex=_RcQosHVlanBandwidthProfileIndex_Object((1,3,6,1,4,1,8886,1,33,2,16,1,1),_RcQosHVlanBandwidthProfileIndex_Type())
rcQosHVlanBandwidthProfileIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:rcQosHVlanBandwidthProfileIndex.setStatus(_A)
class _RcQosHVlanBandwidthProfileVlan_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4094))
_RcQosHVlanBandwidthProfileVlan_Type.__name__=_C
_RcQosHVlanBandwidthProfileVlan_Object=MibTableColumn
rcQosHVlanBandwidthProfileVlan=_RcQosHVlanBandwidthProfileVlan_Object((1,3,6,1,4,1,8886,1,33,2,16,1,2),_RcQosHVlanBandwidthProfileVlan_Type())
rcQosHVlanBandwidthProfileVlan.setMaxAccess(_F)
if mibBuilder.loadTexts:rcQosHVlanBandwidthProfileVlan.setStatus(_A)
_RcQosHVlanBandwidthProfileBwpIndex_Type=Integer32
_RcQosHVlanBandwidthProfileBwpIndex_Object=MibTableColumn
rcQosHVlanBandwidthProfileBwpIndex=_RcQosHVlanBandwidthProfileBwpIndex_Object((1,3,6,1,4,1,8886,1,33,2,16,1,3),_RcQosHVlanBandwidthProfileBwpIndex_Type())
rcQosHVlanBandwidthProfileBwpIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:rcQosHVlanBandwidthProfileBwpIndex.setStatus(_A)
_RcQoSHVlanBandwidthProfileRef_Type=Integer32
_RcQoSHVlanBandwidthProfileRef_Object=MibTableColumn
rcQoSHVlanBandwidthProfileRef=_RcQoSHVlanBandwidthProfileRef_Object((1,3,6,1,4,1,8886,1,33,2,16,1,4),_RcQoSHVlanBandwidthProfileRef_Type())
rcQoSHVlanBandwidthProfileRef.setMaxAccess(_G)
if mibBuilder.loadTexts:rcQoSHVlanBandwidthProfileRef.setStatus(_A)
_RcQosHVlanBandwidthProfileRowStatus_Type=RowStatus
_RcQosHVlanBandwidthProfileRowStatus_Object=MibTableColumn
rcQosHVlanBandwidthProfileRowStatus=_RcQosHVlanBandwidthProfileRowStatus_Object((1,3,6,1,4,1,8886,1,33,2,16,1,5),_RcQosHVlanBandwidthProfileRowStatus_Type())
rcQosHVlanBandwidthProfileRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:rcQosHVlanBandwidthProfileRowStatus.setStatus(_A)
_RcQosBandwidthPortTable_Object=MibTable
rcQosBandwidthPortTable=_RcQosBandwidthPortTable_Object((1,3,6,1,4,1,8886,1,33,2,17))
if mibBuilder.loadTexts:rcQosBandwidthPortTable.setStatus(_A)
_RcQosBandwidthPortEntry_Object=MibTableRow
rcQosBandwidthPortEntry=_RcQosBandwidthPortEntry_Object((1,3,6,1,4,1,8886,1,33,2,17,1))
rcQosBandwidthPortEntry.setIndexNames((0,_D,_X))
if mibBuilder.loadTexts:rcQosBandwidthPortEntry.setStatus(_A)
_RcQosBandwidthPortIndex_Type=Integer32
_RcQosBandwidthPortIndex_Object=MibTableColumn
rcQosBandwidthPortIndex=_RcQosBandwidthPortIndex_Object((1,3,6,1,4,1,8886,1,33,2,17,1,1),_RcQosBandwidthPortIndex_Type())
rcQosBandwidthPortIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:rcQosBandwidthPortIndex.setStatus(_A)
_RcQosBandwidthPortBwpIndex_Type=Integer32
_RcQosBandwidthPortBwpIndex_Object=MibTableColumn
rcQosBandwidthPortBwpIndex=_RcQosBandwidthPortBwpIndex_Object((1,3,6,1,4,1,8886,1,33,2,17,1,2),_RcQosBandwidthPortBwpIndex_Type())
rcQosBandwidthPortBwpIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:rcQosBandwidthPortBwpIndex.setStatus(_A)
_RcQosBandwidthPortEgrBwpIndex_Type=Integer32
_RcQosBandwidthPortEgrBwpIndex_Object=MibTableColumn
rcQosBandwidthPortEgrBwpIndex=_RcQosBandwidthPortEgrBwpIndex_Object((1,3,6,1,4,1,8886,1,33,2,17,1,3),_RcQosBandwidthPortEgrBwpIndex_Type())
rcQosBandwidthPortEgrBwpIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:rcQosBandwidthPortEgrBwpIndex.setStatus(_A)
_RcQosBandwidthPortHBwEnable_Type=EnableVar
_RcQosBandwidthPortHBwEnable_Object=MibTableColumn
rcQosBandwidthPortHBwEnable=_RcQosBandwidthPortHBwEnable_Object((1,3,6,1,4,1,8886,1,33,2,17,1,4),_RcQosBandwidthPortHBwEnable_Type())
rcQosBandwidthPortHBwEnable.setMaxAccess(_E)
if mibBuilder.loadTexts:rcQosBandwidthPortHBwEnable.setStatus(_A)
_RcQosBandwidthPortHvBwpIndex_Type=Integer32
_RcQosBandwidthPortHvBwpIndex_Object=MibTableColumn
rcQosBandwidthPortHvBwpIndex=_RcQosBandwidthPortHvBwpIndex_Object((1,3,6,1,4,1,8886,1,33,2,17,1,5),_RcQosBandwidthPortHvBwpIndex_Type())
rcQosBandwidthPortHvBwpIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:rcQosBandwidthPortHvBwpIndex.setStatus(_A)
_RcQosBandwidthPortDeiRemarkEnable_Type=EnableVar
_RcQosBandwidthPortDeiRemarkEnable_Object=MibTableColumn
rcQosBandwidthPortDeiRemarkEnable=_RcQosBandwidthPortDeiRemarkEnable_Object((1,3,6,1,4,1,8886,1,33,2,17,1,6),_RcQosBandwidthPortDeiRemarkEnable_Type())
rcQosBandwidthPortDeiRemarkEnable.setMaxAccess(_E)
if mibBuilder.loadTexts:rcQosBandwidthPortDeiRemarkEnable.setStatus(_A)
_RcQosBandwidthPortColorAwareEnable_Type=EnableVar
_RcQosBandwidthPortColorAwareEnable_Object=MibTableColumn
rcQosBandwidthPortColorAwareEnable=_RcQosBandwidthPortColorAwareEnable_Object((1,3,6,1,4,1,8886,1,33,2,17,1,7),_RcQosBandwidthPortColorAwareEnable_Type())
rcQosBandwidthPortColorAwareEnable.setMaxAccess(_E)
if mibBuilder.loadTexts:rcQosBandwidthPortColorAwareEnable.setStatus(_A)
_RcQosBandwidthVlanTable_Object=MibTable
rcQosBandwidthVlanTable=_RcQosBandwidthVlanTable_Object((1,3,6,1,4,1,8886,1,33,2,18))
if mibBuilder.loadTexts:rcQosBandwidthVlanTable.setStatus(_A)
_RcQosBandwidthVlanEntry_Object=MibTableRow
rcQosBandwidthVlanEntry=_RcQosBandwidthVlanEntry_Object((1,3,6,1,4,1,8886,1,33,2,18,1))
rcQosBandwidthVlanEntry.setIndexNames((0,_D,_Y),(0,_D,_Z),(0,_D,_a))
if mibBuilder.loadTexts:rcQosBandwidthVlanEntry.setStatus(_A)
class _RcQosBandwidthVlanIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4094))
_RcQosBandwidthVlanIndex_Type.__name__=_C
_RcQosBandwidthVlanIndex_Object=MibTableColumn
rcQosBandwidthVlanIndex=_RcQosBandwidthVlanIndex_Object((1,3,6,1,4,1,8886,1,33,2,18,1,1),_RcQosBandwidthVlanIndex_Type())
rcQosBandwidthVlanIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:rcQosBandwidthVlanIndex.setStatus(_A)
_RcQosBandwidthVlanPort_Type=Integer32
_RcQosBandwidthVlanPort_Object=MibTableColumn
rcQosBandwidthVlanPort=_RcQosBandwidthVlanPort_Object((1,3,6,1,4,1,8886,1,33,2,18,1,2),_RcQosBandwidthVlanPort_Type())
rcQosBandwidthVlanPort.setMaxAccess(_F)
if mibBuilder.loadTexts:rcQosBandwidthVlanPort.setStatus(_A)
class _RcQosBandwidthVlanPortType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_Q,1),(_R,2)))
_RcQosBandwidthVlanPortType_Type.__name__=_C
_RcQosBandwidthVlanPortType_Object=MibTableColumn
rcQosBandwidthVlanPortType=_RcQosBandwidthVlanPortType_Object((1,3,6,1,4,1,8886,1,33,2,18,1,3),_RcQosBandwidthVlanPortType_Type())
rcQosBandwidthVlanPortType.setMaxAccess(_F)
if mibBuilder.loadTexts:rcQosBandwidthVlanPortType.setStatus(_A)
_RcQosBandwidthVlanBwpIndex_Type=Integer32
_RcQosBandwidthVlanBwpIndex_Object=MibTableColumn
rcQosBandwidthVlanBwpIndex=_RcQosBandwidthVlanBwpIndex_Object((1,3,6,1,4,1,8886,1,33,2,18,1,4),_RcQosBandwidthVlanBwpIndex_Type())
rcQosBandwidthVlanBwpIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:rcQosBandwidthVlanBwpIndex.setStatus(_A)
_RcQosBandwidthVlanHBwEnable_Type=EnableVar
_RcQosBandwidthVlanHBwEnable_Object=MibTableColumn
rcQosBandwidthVlanHBwEnable=_RcQosBandwidthVlanHBwEnable_Object((1,3,6,1,4,1,8886,1,33,2,18,1,5),_RcQosBandwidthVlanHBwEnable_Type())
rcQosBandwidthVlanHBwEnable.setMaxAccess(_E)
if mibBuilder.loadTexts:rcQosBandwidthVlanHBwEnable.setStatus(_A)
_RcQosBandwidthVlanHcBwpIndex_Type=Integer32
_RcQosBandwidthVlanHcBwpIndex_Object=MibTableColumn
rcQosBandwidthVlanHcBwpIndex=_RcQosBandwidthVlanHcBwpIndex_Object((1,3,6,1,4,1,8886,1,33,2,18,1,6),_RcQosBandwidthVlanHcBwpIndex_Type())
rcQosBandwidthVlanHcBwpIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:rcQosBandwidthVlanHcBwpIndex.setStatus(_A)
_RcQosBandwidthVlanRowStatus_Type=RowStatus
_RcQosBandwidthVlanRowStatus_Object=MibTableColumn
rcQosBandwidthVlanRowStatus=_RcQosBandwidthVlanRowStatus_Object((1,3,6,1,4,1,8886,1,33,2,18,1,7),_RcQosBandwidthVlanRowStatus_Type())
rcQosBandwidthVlanRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:rcQosBandwidthVlanRowStatus.setStatus(_A)
_RcQosBandwidthCosTable_Object=MibTable
rcQosBandwidthCosTable=_RcQosBandwidthCosTable_Object((1,3,6,1,4,1,8886,1,33,2,19))
if mibBuilder.loadTexts:rcQosBandwidthCosTable.setStatus(_A)
_RcQosBandwidthCosEntry_Object=MibTableRow
rcQosBandwidthCosEntry=_RcQosBandwidthCosEntry_Object((1,3,6,1,4,1,8886,1,33,2,19,1))
rcQosBandwidthCosEntry.setIndexNames((0,_D,_b),(0,_D,_c),(0,_D,_d),(0,_D,_e))
if mibBuilder.loadTexts:rcQosBandwidthCosEntry.setStatus(_A)
class _RcQosBandwidthCosIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_RcQosBandwidthCosIndex_Type.__name__=_C
_RcQosBandwidthCosIndex_Object=MibTableColumn
rcQosBandwidthCosIndex=_RcQosBandwidthCosIndex_Object((1,3,6,1,4,1,8886,1,33,2,19,1,1),_RcQosBandwidthCosIndex_Type())
rcQosBandwidthCosIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:rcQosBandwidthCosIndex.setStatus(_A)
class _RcQosBandwidthCosVlan_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4094))
_RcQosBandwidthCosVlan_Type.__name__=_C
_RcQosBandwidthCosVlan_Object=MibTableColumn
rcQosBandwidthCosVlan=_RcQosBandwidthCosVlan_Object((1,3,6,1,4,1,8886,1,33,2,19,1,2),_RcQosBandwidthCosVlan_Type())
rcQosBandwidthCosVlan.setMaxAccess(_G)
if mibBuilder.loadTexts:rcQosBandwidthCosVlan.setStatus(_A)
_RcQosBandwidthCosPort_Type=Integer32
_RcQosBandwidthCosPort_Object=MibTableColumn
rcQosBandwidthCosPort=_RcQosBandwidthCosPort_Object((1,3,6,1,4,1,8886,1,33,2,19,1,3),_RcQosBandwidthCosPort_Type())
rcQosBandwidthCosPort.setMaxAccess(_G)
if mibBuilder.loadTexts:rcQosBandwidthCosPort.setStatus(_A)
class _RcQosBandwidthCosPortType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_Q,1),(_R,2)))
_RcQosBandwidthCosPortType_Type.__name__=_C
_RcQosBandwidthCosPortType_Object=MibTableColumn
rcQosBandwidthCosPortType=_RcQosBandwidthCosPortType_Object((1,3,6,1,4,1,8886,1,33,2,19,1,4),_RcQosBandwidthCosPortType_Type())
rcQosBandwidthCosPortType.setMaxAccess(_G)
if mibBuilder.loadTexts:rcQosBandwidthCosPortType.setStatus(_A)
_RcQosBandwidthCosBwpIndex_Type=Integer32
_RcQosBandwidthCosBwpIndex_Object=MibTableColumn
rcQosBandwidthCosBwpIndex=_RcQosBandwidthCosBwpIndex_Object((1,3,6,1,4,1,8886,1,33,2,19,1,5),_RcQosBandwidthCosBwpIndex_Type())
rcQosBandwidthCosBwpIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:rcQosBandwidthCosBwpIndex.setStatus(_A)
_RcQosBandwidthCosRowStatus_Type=RowStatus
_RcQosBandwidthCosRowStatus_Object=MibTableColumn
rcQosBandwidthCosRowStatus=_RcQosBandwidthCosRowStatus_Object((1,3,6,1,4,1,8886,1,33,2,19,1,6),_RcQosBandwidthCosRowStatus_Type())
rcQosBandwidthCosRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:rcQosBandwidthCosRowStatus.setStatus(_A)
_RcQosBandwidthGlobalEnable_Type=EnableVar
_RcQosBandwidthGlobalEnable_Object=MibScalar
rcQosBandwidthGlobalEnable=_RcQosBandwidthGlobalEnable_Object((1,3,6,1,4,1,8886,1,33,2,20),_RcQosBandwidthGlobalEnable_Type())
rcQosBandwidthGlobalEnable.setMaxAccess(_E)
if mibBuilder.loadTexts:rcQosBandwidthGlobalEnable.setStatus(_A)
_RcQosBandwidthNotificationGroup_ObjectIdentity=ObjectIdentity
rcQosBandwidthNotificationGroup=_RcQosBandwidthNotificationGroup_ObjectIdentity((1,3,6,1,4,1,8886,1,33,2,21))
_RaisecomQosStatistics_ObjectIdentity=ObjectIdentity
raisecomQosStatistics=_RaisecomQosStatistics_ObjectIdentity((1,3,6,1,4,1,8886,1,33,3))
_RcQosTrafficStatsTable_Object=MibTable
rcQosTrafficStatsTable=_RcQosTrafficStatsTable_Object((1,3,6,1,4,1,8886,1,33,3,1))
if mibBuilder.loadTexts:rcQosTrafficStatsTable.setStatus(_A)
_RcQosTrafficStatsEntry_Object=MibTableRow
rcQosTrafficStatsEntry=_RcQosTrafficStatsEntry_Object((1,3,6,1,4,1,8886,1,33,3,1,1))
rcQosTrafficStatsEntry.setIndexNames((0,_D,_Af),(0,_D,_Ag),(0,_D,_Ah))
if mibBuilder.loadTexts:rcQosTrafficStatsEntry.setStatus(_A)
_RcQosTrafficStatsPort_Type=Integer32
_RcQosTrafficStatsPort_Object=MibTableColumn
rcQosTrafficStatsPort=_RcQosTrafficStatsPort_Object((1,3,6,1,4,1,8886,1,33,3,1,1,1),_RcQosTrafficStatsPort_Type())
rcQosTrafficStatsPort.setMaxAccess(_F)
if mibBuilder.loadTexts:rcQosTrafficStatsPort.setStatus(_A)
class _RcQosTrafficStatsDirection_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_Q,1),(_R,2)))
_RcQosTrafficStatsDirection_Type.__name__=_C
_RcQosTrafficStatsDirection_Object=MibTableColumn
rcQosTrafficStatsDirection=_RcQosTrafficStatsDirection_Object((1,3,6,1,4,1,8886,1,33,3,1,1,2),_RcQosTrafficStatsDirection_Type())
rcQosTrafficStatsDirection.setMaxAccess(_F)
if mibBuilder.loadTexts:rcQosTrafficStatsDirection.setStatus(_A)
_RcQosTrafficStatsCmapName_Type=ObjName
_RcQosTrafficStatsCmapName_Object=MibTableColumn
rcQosTrafficStatsCmapName=_RcQosTrafficStatsCmapName_Object((1,3,6,1,4,1,8886,1,33,3,1,1,3),_RcQosTrafficStatsCmapName_Type())
rcQosTrafficStatsCmapName.setMaxAccess(_F)
if mibBuilder.loadTexts:rcQosTrafficStatsCmapName.setStatus(_A)
class _RcQosTrafficStatsPolicerType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*((_P,0),('singleflow',1),('classflow',2),('aggregate',3)))
_RcQosTrafficStatsPolicerType_Type.__name__=_C
_RcQosTrafficStatsPolicerType_Object=MibTableColumn
rcQosTrafficStatsPolicerType=_RcQosTrafficStatsPolicerType_Object((1,3,6,1,4,1,8886,1,33,3,1,1,4),_RcQosTrafficStatsPolicerType_Type())
rcQosTrafficStatsPolicerType.setMaxAccess(_G)
if mibBuilder.loadTexts:rcQosTrafficStatsPolicerType.setStatus(_A)
_RcQosTrafficCounterReset_Type=EnableVar
_RcQosTrafficCounterReset_Object=MibTableColumn
rcQosTrafficCounterReset=_RcQosTrafficCounterReset_Object((1,3,6,1,4,1,8886,1,33,3,1,1,5),_RcQosTrafficCounterReset_Type())
rcQosTrafficCounterReset.setMaxAccess(_E)
if mibBuilder.loadTexts:rcQosTrafficCounterReset.setStatus(_A)
_RcQosTrafficPolicyName_Type=ObjName
_RcQosTrafficPolicyName_Object=MibTableColumn
rcQosTrafficPolicyName=_RcQosTrafficPolicyName_Object((1,3,6,1,4,1,8886,1,33,3,1,1,6),_RcQosTrafficPolicyName_Type())
rcQosTrafficPolicyName.setMaxAccess(_E)
if mibBuilder.loadTexts:rcQosTrafficPolicyName.setStatus(_A)
_RcQosTrafficPolicerName_Type=ObjName
_RcQosTrafficPolicerName_Object=MibTableColumn
rcQosTrafficPolicerName=_RcQosTrafficPolicerName_Object((1,3,6,1,4,1,8886,1,33,3,1,1,7),_RcQosTrafficPolicerName_Type())
rcQosTrafficPolicerName.setMaxAccess(_E)
if mibBuilder.loadTexts:rcQosTrafficPolicerName.setStatus(_A)
_RcQosTrafficCounterHwStatus_Type=TruthValue
_RcQosTrafficCounterHwStatus_Object=MibTableColumn
rcQosTrafficCounterHwStatus=_RcQosTrafficCounterHwStatus_Object((1,3,6,1,4,1,8886,1,33,3,1,1,8),_RcQosTrafficCounterHwStatus_Type())
rcQosTrafficCounterHwStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:rcQosTrafficCounterHwStatus.setStatus(_A)
class _RcQosTrafficStatisticsUnit_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_S,1),(_f,2)))
_RcQosTrafficStatisticsUnit_Type.__name__=_C
_RcQosTrafficStatisticsUnit_Object=MibTableColumn
rcQosTrafficStatisticsUnit=_RcQosTrafficStatisticsUnit_Object((1,3,6,1,4,1,8886,1,33,3,1,1,9),_RcQosTrafficStatisticsUnit_Type())
rcQosTrafficStatisticsUnit.setMaxAccess(_E)
if mibBuilder.loadTexts:rcQosTrafficStatisticsUnit.setStatus(_A)
_RcQosTrafficCounterInprofilePkt64_Type=Counter64
_RcQosTrafficCounterInprofilePkt64_Object=MibTableColumn
rcQosTrafficCounterInprofilePkt64=_RcQosTrafficCounterInprofilePkt64_Object((1,3,6,1,4,1,8886,1,33,3,1,1,10),_RcQosTrafficCounterInprofilePkt64_Type())
rcQosTrafficCounterInprofilePkt64.setMaxAccess(_G)
if mibBuilder.loadTexts:rcQosTrafficCounterInprofilePkt64.setStatus(_A)
_RcQosTrafficCounterInprofileByte64_Type=Counter64
_RcQosTrafficCounterInprofileByte64_Object=MibTableColumn
rcQosTrafficCounterInprofileByte64=_RcQosTrafficCounterInprofileByte64_Object((1,3,6,1,4,1,8886,1,33,3,1,1,11),_RcQosTrafficCounterInprofileByte64_Type())
rcQosTrafficCounterInprofileByte64.setMaxAccess(_G)
if mibBuilder.loadTexts:rcQosTrafficCounterInprofileByte64.setStatus(_A)
_RcQosTrafficCounterOutprofilePkt64_Type=Counter64
_RcQosTrafficCounterOutprofilePkt64_Object=MibTableColumn
rcQosTrafficCounterOutprofilePkt64=_RcQosTrafficCounterOutprofilePkt64_Object((1,3,6,1,4,1,8886,1,33,3,1,1,12),_RcQosTrafficCounterOutprofilePkt64_Type())
rcQosTrafficCounterOutprofilePkt64.setMaxAccess(_G)
if mibBuilder.loadTexts:rcQosTrafficCounterOutprofilePkt64.setStatus(_A)
_RcQosTrafficCounterOutprofileByte64_Type=Counter64
_RcQosTrafficCounterOutprofileByte64_Object=MibTableColumn
rcQosTrafficCounterOutprofileByte64=_RcQosTrafficCounterOutprofileByte64_Object((1,3,6,1,4,1,8886,1,33,3,1,1,13),_RcQosTrafficCounterOutprofileByte64_Type())
rcQosTrafficCounterOutprofileByte64.setMaxAccess(_G)
if mibBuilder.loadTexts:rcQosTrafficCounterOutprofileByte64.setStatus(_A)
_RcQosTrafficbStatistics_Type=EnableVar
_RcQosTrafficbStatistics_Object=MibTableColumn
rcQosTrafficbStatistics=_RcQosTrafficbStatistics_Object((1,3,6,1,4,1,8886,1,33,3,1,1,14),_RcQosTrafficbStatistics_Type())
rcQosTrafficbStatistics.setMaxAccess(_G)
if mibBuilder.loadTexts:rcQosTrafficbStatistics.setStatus(_A)
_RcQosVlanStatisticsTable_Object=MibTable
rcQosVlanStatisticsTable=_RcQosVlanStatisticsTable_Object((1,3,6,1,4,1,8886,1,33,3,2))
if mibBuilder.loadTexts:rcQosVlanStatisticsTable.setStatus(_A)
_RcQosVlanStatisticsEntry_Object=MibTableRow
rcQosVlanStatisticsEntry=_RcQosVlanStatisticsEntry_Object((1,3,6,1,4,1,8886,1,33,3,2,1))
rcQosVlanStatisticsEntry.setIndexNames((0,_D,_Ai),(0,_D,_Aj),(0,_D,_Ak))
if mibBuilder.loadTexts:rcQosVlanStatisticsEntry.setStatus(_A)
_RcQosVlanStatisticsPort_Type=Integer32
_RcQosVlanStatisticsPort_Object=MibTableColumn
rcQosVlanStatisticsPort=_RcQosVlanStatisticsPort_Object((1,3,6,1,4,1,8886,1,33,3,2,1,1),_RcQosVlanStatisticsPort_Type())
rcQosVlanStatisticsPort.setMaxAccess(_F)
if mibBuilder.loadTexts:rcQosVlanStatisticsPort.setStatus(_A)
_RcQosVlanStatisticsVlan_Type=Integer32
_RcQosVlanStatisticsVlan_Object=MibTableColumn
rcQosVlanStatisticsVlan=_RcQosVlanStatisticsVlan_Object((1,3,6,1,4,1,8886,1,33,3,2,1,2),_RcQosVlanStatisticsVlan_Type())
rcQosVlanStatisticsVlan.setMaxAccess(_F)
if mibBuilder.loadTexts:rcQosVlanStatisticsVlan.setStatus(_A)
class _RcQosVlanStatisticsDirection_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_Q,1),(_R,2)))
_RcQosVlanStatisticsDirection_Type.__name__=_C
_RcQosVlanStatisticsDirection_Object=MibTableColumn
rcQosVlanStatisticsDirection=_RcQosVlanStatisticsDirection_Object((1,3,6,1,4,1,8886,1,33,3,2,1,3),_RcQosVlanStatisticsDirection_Type())
rcQosVlanStatisticsDirection.setMaxAccess(_F)
if mibBuilder.loadTexts:rcQosVlanStatisticsDirection.setStatus(_A)
class _RcQosVlanStatisticsUnit_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_f,1),(_S,2),(_M,3)))
_RcQosVlanStatisticsUnit_Type.__name__=_C
_RcQosVlanStatisticsUnit_Object=MibTableColumn
rcQosVlanStatisticsUnit=_RcQosVlanStatisticsUnit_Object((1,3,6,1,4,1,8886,1,33,3,2,1,4),_RcQosVlanStatisticsUnit_Type())
rcQosVlanStatisticsUnit.setMaxAccess(_G)
if mibBuilder.loadTexts:rcQosVlanStatisticsUnit.setStatus(_A)
_RcQosVlanStatisticsReset_Type=Integer32
_RcQosVlanStatisticsReset_Object=MibTableColumn
rcQosVlanStatisticsReset=_RcQosVlanStatisticsReset_Object((1,3,6,1,4,1,8886,1,33,3,2,1,5),_RcQosVlanStatisticsReset_Type())
rcQosVlanStatisticsReset.setMaxAccess(_B)
if mibBuilder.loadTexts:rcQosVlanStatisticsReset.setStatus(_A)
_RcQosVlanStatisticsPkt_Type=Counter64
_RcQosVlanStatisticsPkt_Object=MibTableColumn
rcQosVlanStatisticsPkt=_RcQosVlanStatisticsPkt_Object((1,3,6,1,4,1,8886,1,33,3,2,1,6),_RcQosVlanStatisticsPkt_Type())
rcQosVlanStatisticsPkt.setMaxAccess(_G)
if mibBuilder.loadTexts:rcQosVlanStatisticsPkt.setStatus(_A)
_RcQosVlanStatisticsByte_Type=Counter64
_RcQosVlanStatisticsByte_Object=MibTableColumn
rcQosVlanStatisticsByte=_RcQosVlanStatisticsByte_Object((1,3,6,1,4,1,8886,1,33,3,2,1,7),_RcQosVlanStatisticsByte_Type())
rcQosVlanStatisticsByte.setMaxAccess(_G)
if mibBuilder.loadTexts:rcQosVlanStatisticsByte.setStatus(_A)
_RcQosVlanStatisticsRowStatus_Type=RowStatus
_RcQosVlanStatisticsRowStatus_Object=MibTableColumn
rcQosVlanStatisticsRowStatus=_RcQosVlanStatisticsRowStatus_Object((1,3,6,1,4,1,8886,1,33,3,2,1,8),_RcQosVlanStatisticsRowStatus_Type())
rcQosVlanStatisticsRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:rcQosVlanStatisticsRowStatus.setStatus(_A)
_RcQosCosStatisticsTable_Object=MibTable
rcQosCosStatisticsTable=_RcQosCosStatisticsTable_Object((1,3,6,1,4,1,8886,1,33,3,3))
if mibBuilder.loadTexts:rcQosCosStatisticsTable.setStatus(_A)
_RcQosCosStatisticsEntry_Object=MibTableRow
rcQosCosStatisticsEntry=_RcQosCosStatisticsEntry_Object((1,3,6,1,4,1,8886,1,33,3,3,1))
rcQosCosStatisticsEntry.setIndexNames((0,_D,_Al),(0,_D,_Am),(0,_D,_An),(0,_D,_Ao))
if mibBuilder.loadTexts:rcQosCosStatisticsEntry.setStatus(_A)
_RcQosCosStatisticsPort_Type=Integer32
_RcQosCosStatisticsPort_Object=MibTableColumn
rcQosCosStatisticsPort=_RcQosCosStatisticsPort_Object((1,3,6,1,4,1,8886,1,33,3,3,1,1),_RcQosCosStatisticsPort_Type())
rcQosCosStatisticsPort.setMaxAccess(_F)
if mibBuilder.loadTexts:rcQosCosStatisticsPort.setStatus(_A)
_RcQosCosStatisticsVlan_Type=Integer32
_RcQosCosStatisticsVlan_Object=MibTableColumn
rcQosCosStatisticsVlan=_RcQosCosStatisticsVlan_Object((1,3,6,1,4,1,8886,1,33,3,3,1,2),_RcQosCosStatisticsVlan_Type())
rcQosCosStatisticsVlan.setMaxAccess(_F)
if mibBuilder.loadTexts:rcQosCosStatisticsVlan.setStatus(_A)
class _RcQosCosStatisticsCos_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_RcQosCosStatisticsCos_Type.__name__=_C
_RcQosCosStatisticsCos_Object=MibTableColumn
rcQosCosStatisticsCos=_RcQosCosStatisticsCos_Object((1,3,6,1,4,1,8886,1,33,3,3,1,3),_RcQosCosStatisticsCos_Type())
rcQosCosStatisticsCos.setMaxAccess(_F)
if mibBuilder.loadTexts:rcQosCosStatisticsCos.setStatus(_A)
class _RcQosCosStatisticsDirection_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_Q,1),(_R,2)))
_RcQosCosStatisticsDirection_Type.__name__=_C
_RcQosCosStatisticsDirection_Object=MibTableColumn
rcQosCosStatisticsDirection=_RcQosCosStatisticsDirection_Object((1,3,6,1,4,1,8886,1,33,3,3,1,4),_RcQosCosStatisticsDirection_Type())
rcQosCosStatisticsDirection.setMaxAccess(_F)
if mibBuilder.loadTexts:rcQosCosStatisticsDirection.setStatus(_A)
class _RcQosCosStatisticsUnit_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_f,1),(_S,2),(_M,3)))
_RcQosCosStatisticsUnit_Type.__name__=_C
_RcQosCosStatisticsUnit_Object=MibTableColumn
rcQosCosStatisticsUnit=_RcQosCosStatisticsUnit_Object((1,3,6,1,4,1,8886,1,33,3,3,1,5),_RcQosCosStatisticsUnit_Type())
rcQosCosStatisticsUnit.setMaxAccess(_G)
if mibBuilder.loadTexts:rcQosCosStatisticsUnit.setStatus(_A)
_RcQosCosStatisticsReset_Type=Integer32
_RcQosCosStatisticsReset_Object=MibTableColumn
rcQosCosStatisticsReset=_RcQosCosStatisticsReset_Object((1,3,6,1,4,1,8886,1,33,3,3,1,6),_RcQosCosStatisticsReset_Type())
rcQosCosStatisticsReset.setMaxAccess(_B)
if mibBuilder.loadTexts:rcQosCosStatisticsReset.setStatus(_A)
_RcQosCosStatisticsPkt_Type=Counter64
_RcQosCosStatisticsPkt_Object=MibTableColumn
rcQosCosStatisticsPkt=_RcQosCosStatisticsPkt_Object((1,3,6,1,4,1,8886,1,33,3,3,1,7),_RcQosCosStatisticsPkt_Type())
rcQosCosStatisticsPkt.setMaxAccess(_G)
if mibBuilder.loadTexts:rcQosCosStatisticsPkt.setStatus(_A)
_RcQosCosStatisticsByte_Type=Counter64
_RcQosCosStatisticsByte_Object=MibTableColumn
rcQosCosStatisticsByte=_RcQosCosStatisticsByte_Object((1,3,6,1,4,1,8886,1,33,3,3,1,8),_RcQosCosStatisticsByte_Type())
rcQosCosStatisticsByte.setMaxAccess(_G)
if mibBuilder.loadTexts:rcQosCosStatisticsByte.setStatus(_A)
_RcQosCosStatisticsRowStatus_Type=RowStatus
_RcQosCosStatisticsRowStatus_Object=MibTableColumn
rcQosCosStatisticsRowStatus=_RcQosCosStatisticsRowStatus_Object((1,3,6,1,4,1,8886,1,33,3,3,1,9),_RcQosCosStatisticsRowStatus_Type())
rcQosCosStatisticsRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:rcQosCosStatisticsRowStatus.setStatus(_A)
rcQosBandwidthPortModification=NotificationType((1,3,6,1,4,1,8886,1,33,2,21,1))
rcQosBandwidthPortModification.setObjects(*((_D,_X),(_D,_Ap),(_D,_Aq),(_D,_Ar),(_D,_As)))
if mibBuilder.loadTexts:rcQosBandwidthPortModification.setStatus(_A)
rcQosBandwidthVlanModification=NotificationType((1,3,6,1,4,1,8886,1,33,2,21,2))
rcQosBandwidthVlanModification.setObjects(*((_D,_Z),(_D,_Y),(_D,_a),(_D,_At),(_D,_Au),(_D,_Av)))
if mibBuilder.loadTexts:rcQosBandwidthVlanModification.setStatus(_A)
rcQosBandwidthCosModification=NotificationType((1,3,6,1,4,1,8886,1,33,2,21,3))
rcQosBandwidthCosModification.setObjects(*((_D,_c),(_D,_d),(_D,_b),(_D,_e),(_D,_Aw)))
if mibBuilder.loadTexts:rcQosBandwidthCosModification.setStatus(_A)
mibBuilder.exportSymbols(_D,**{'raisecomQosMIB':raisecomQosMIB,'raisecomQosCfg':raisecomQosCfg,'rcQosEnable':rcQosEnable,'rcQosTrust':rcQosTrust,'rcQosQueueScheduler':rcQosQueueScheduler,'rcQosWredEnable':rcQosWredEnable,'rcQosCos2PriProfile':rcQosCos2PriProfile,'rcQosTos2PriProfile':rcQosTos2PriProfile,'rcQosDscp2PriProfile':rcQosDscp2PriProfile,'rcQosDscpMutationProfile':rcQosDscpMutationProfile,'rcQosCosRemarkProfile':rcQosCosRemarkProfile,'rcQosPortCfgTable':rcQosPortCfgTable,'rcQosPortCfgEntry':rcQosPortCfgEntry,_g:rcQosPortCfgPortId,'rcQosPortCfgTrust':rcQosPortCfgTrust,'rcQosPortCfgPriority':rcQosPortCfgPriority,'rcQosPortCfgPriorityOverride':rcQosPortCfgPriorityOverride,'rcQosPortCfgQueueScheduler':rcQosPortCfgQueueScheduler,'rcQosPortCfgSmacPriorityOverride':rcQosPortCfgSmacPriorityOverride,'rcQosPortCfgDmacPriorityOverride':rcQosPortCfgDmacPriorityOverride,'rcQosPortCfgVlanPriorityOverride':rcQosPortCfgVlanPriorityOverride,'rcQosPortCos2PriProfile':rcQosPortCos2PriProfile,'rcQosPortTos2PriProfile':rcQosPortTos2PriProfile,'rcQosPortDscp2PriProfile':rcQosPortDscp2PriProfile,'rcQosPortDscpMutationProfile':rcQosPortDscpMutationProfile,'rcQosPortCosRemarkProfile':rcQosPortCosRemarkProfile,'rcQosPortSchedulerQueueTable':rcQosPortSchedulerQueueTable,'rcQosPortSchedulerQueueEntry':rcQosPortSchedulerQueueEntry,_h:rcQosPortSchedulerPortId,_i:rcQosPortSchedulerQueueId,'rcQosPortSchedulerWRR':rcQosPortSchedulerWRR,'rcQosPortSchedulerDRR':rcQosPortSchedulerDRR,'rcQosPortSchedulerWFQ':rcQosPortSchedulerWFQ,'rcQosLocalPrioMappingTable':rcQosLocalPrioMappingTable,'rcQosLocalPrioMappingEntry':rcQosLocalPrioMappingEntry,_j:rcQosLocalPriority,'rcQosQueueId':rcQosQueueId,'rcQosCosMappingTable':rcQosCosMappingTable,'rcQosCosMappingEntry':rcQosCosMappingEntry,_k:rcQosCosValue,'rcQosCosLocalPriority':rcQosCosLocalPriority,'rcQosCosColor':rcQosCosColor,'rcQosTosMappingTable':rcQosTosMappingTable,'rcQosTosMappingEntry':rcQosTosMappingEntry,_l:rcQosTosValue,'rcQosTosLocalPriority':rcQosTosLocalPriority,'rcQosTosColor':rcQosTosColor,'rcQosDscpMapingTable':rcQosDscpMapingTable,'rcQosDscpMapingEntry':rcQosDscpMapingEntry,_m:rcQosDscpValue,'rcQosDscpLocalPriority':rcQosDscpLocalPriority,'rcQosDscpColor':rcQosDscpColor,'rcQosSchedulerQueueTable':rcQosSchedulerQueueTable,'rcQosSchedulerQueueEntry':rcQosSchedulerQueueEntry,_n:rcQosSchedulerQueueId,'rcQosSchedulerWRR':rcQosSchedulerWRR,'rcQosSchedulerDRR':rcQosSchedulerDRR,'rcQosSchedulerWFQ':rcQosSchedulerWFQ,'rcQosWredTcpConfigTable':rcQosWredTcpConfigTable,'rcQosWredTcpConfigEntry':rcQosWredTcpConfigEntry,_o:rcQosWredQueueId,'rcQosWredGreenDropStartPoint':rcQosWredGreenDropStartPoint,'rcQosWredGreenDropEndPoint':rcQosWredGreenDropEndPoint,'rcQosWredGreenDropProbability':rcQosWredGreenDropProbability,'rcQosWredYellowDropStartPoint':rcQosWredYellowDropStartPoint,'rcQosWredYellowDropEndPoint':rcQosWredYellowDropEndPoint,'rcQosWredYellowDropProbability':rcQosWredYellowDropProbability,'rcQosWredRedDropStartPoint':rcQosWredRedDropStartPoint,'rcQosWredRedDropEndPoint':rcQosWredRedDropEndPoint,'rcQosWredRedDropProbability':rcQosWredRedDropProbability,'rcQosWredStatus':rcQosWredStatus,'rcQosPortWredTcpConfigTable':rcQosPortWredTcpConfigTable,'rcQosPortWredTcpConfigEntry':rcQosPortWredTcpConfigEntry,_p:rcQosPortWredPortId,_q:rcQosPortWredQueueId,'rcQosPortWredGreenDropStartPoint':rcQosPortWredGreenDropStartPoint,'rcQosPortWredGreenDropEndPoint':rcQosPortWredGreenDropEndPoint,'rcQosPortWredGreenDropProbability':rcQosPortWredGreenDropProbability,'rcQosPortWredYellowDropStartPoint':rcQosPortWredYellowDropStartPoint,'rcQosPortWredYellowDropEndPoint':rcQosPortWredYellowDropEndPoint,'rcQosPortWredYellowDropProbability':rcQosPortWredYellowDropProbability,'rcQosPortWredRedDropStartPoint':rcQosPortWredRedDropStartPoint,'rcQosPortWredRedDropEndPoint':rcQosPortWredRedDropEndPoint,'rcQosPortWredRedDropProbability':rcQosPortWredRedDropProbability,'rcQosPortWredStatus':rcQosPortWredStatus,'rcQosShapingTable':rcQosShapingTable,'rcQosShapingEntry':rcQosShapingEntry,_r:rcQosShapingQueueId,'rcQosShapingCir':rcQosShapingCir,'rcQosShapingCbs':rcQosShapingCbs,'rcQosShapingPir':rcQosShapingPir,'rcQosShapingPbs':rcQosShapingPbs,'rcQosShapingStatus':rcQosShapingStatus,'rcQosPortShapingTable':rcQosPortShapingTable,'rcQosPortShapingEntry':rcQosPortShapingEntry,_s:rcQosPortShapingPortId,_t:rcQosPortShapingQueueId,'rcQosPortShapingCir':rcQosPortShapingCir,'rcQosPortShapingCbs':rcQosPortShapingCbs,'rcQosPortShapingPir':rcQosPortShapingPir,'rcQosPortShapingPbs':rcQosPortShapingPbs,'rcQosPortShapingStatus':rcQosPortShapingStatus,'rcQosPortCosMappingTable':rcQosPortCosMappingTable,'rcQosPortCosMappingEntry':rcQosPortCosMappingEntry,_u:rcQosPortCosPortId,_v:rcQosPortCosValue,'rcQosPortCosLocalPriority':rcQosPortCosLocalPriority,'rcQosPortCosColor':rcQosPortCosColor,'rcQosPortTosMappingTable':rcQosPortTosMappingTable,'rcQosPortTosMappingEntry':rcQosPortTosMappingEntry,_w:rcQosPortTosPortId,_x:rcQosPortTosValue,'rcQosPortTosLocalPriority':rcQosPortTosLocalPriority,'rcQosPortTosColor':rcQosPortTosColor,'rcQosPortDscpMapingTable':rcQosPortDscpMapingTable,'rcQosPortDscpMapingEntry':rcQosPortDscpMapingEntry,_y:rcQosPortDscpPortId,_z:rcQosPortDscpValue,'rcQosPortDscpLocalPriority':rcQosPortDscpLocalPriority,'rcQosPortDscpColor':rcQosPortDscpColor,'rcQosPortDropPktsStatisticTable':rcQosPortDropPktsStatisticTable,'rcQosPortDropPktsStatisticEntry':rcQosPortDropPktsStatisticEntry,_A0:rcQosPortStatisticsPortId,_A1:rcQosPortStatisticsQueueId,'rcQosPortStatisticsDropPkts':rcQosPortStatisticsDropPkts,'rcQosPortStatisticsDropBytes':rcQosPortStatisticsDropBytes,'rcQosPortStatisticsDropUnit':rcQosPortStatisticsDropUnit,'rcQosPortStatisticsClear':rcQosPortStatisticsClear,'rcQosMappingCosToPriTable':rcQosMappingCosToPriTable,'rcQosMappingCosToPriEntry':rcQosMappingCosToPriEntry,_A2:rcQosCosToPriIndex,_A3:rcQosCosToPriCos,'rcQosCosToPriLpri':rcQosCosToPriLpri,'rcQosCosToPriColor':rcQosCosToPriColor,'rcQosCosToPriDesc':rcQosCosToPriDesc,'rcQosCosToPriRef':rcQosCosToPriRef,'rcQosCosToPriStatus':rcQosCosToPriStatus,'rcQosMappingTosToPriTable':rcQosMappingTosToPriTable,'rcQosMappingTosToPriEntry':rcQosMappingTosToPriEntry,_A4:rcQosTosToPriIndex,_A5:rcQosTosToPriTos,'rcQosTosToPriLpri':rcQosTosToPriLpri,'rcQosTosToPriColor':rcQosTosToPriColor,'rcQosTosToPriDesc':rcQosTosToPriDesc,'rcQosTosToPriRef':rcQosTosToPriRef,'rcQosTosToPriStatus':rcQosTosToPriStatus,'rcQosMappingDscpToPriTable':rcQosMappingDscpToPriTable,'rcQosMappingDscpToPriEntry':rcQosMappingDscpToPriEntry,_A6:rcQosDscpToPriIndex,_A7:rcQosDscpToPriDscp,'rcQosDscpToPriLpri':rcQosDscpToPriLpri,'rcQosDscpToPriColor':rcQosDscpToPriColor,'rcQosDscpToPriDesc':rcQosDscpToPriDesc,'rcQosDscpToPriRef':rcQosDscpToPriRef,'rcQosDscpToPriStatus':rcQosDscpToPriStatus,'rcQosMappingDscpMutationTable':rcQosMappingDscpMutationTable,'rcQosMappingDscpMutationEntry':rcQosMappingDscpMutationEntry,_A8:rcQosDscpMutationIndex,_A9:rcQosDscpMutationDscp,'rcQosDscpMutationNewDscp':rcQosDscpMutationNewDscp,'rcQosDscpMutationDesc':rcQosDscpMutationDesc,'rcQosDscpMutationRef':rcQosDscpMutationRef,'rcQosDscpMutationStatus':rcQosDscpMutationStatus,'rcQosMappingCosRemarkTable':rcQosMappingCosRemarkTable,'rcQosMappingCosRemarkEntry':rcQosMappingCosRemarkEntry,_AA:rcQosCosRemarkIndex,_AB:rcQosCosRemarkLpri,'rcQosCosRemarkCos':rcQosCosRemarkCos,'rcQosCosRemarkDesc':rcQosCosRemarkDesc,'rcQosCosRemarkRef':rcQosCosRemarkRef,'rcQosCosRemarkStatus':rcQosCosRemarkStatus,'rcQosWredProfileTable':rcQosWredProfileTable,'rcQosWredProfileEntry':rcQosWredProfileEntry,_AC:rcQosWredProfileIndex,'rcQosWredProfileGreenDropStartPoint':rcQosWredProfileGreenDropStartPoint,'rcQosWredProfileGreenDropEndPoint':rcQosWredProfileGreenDropEndPoint,'rcQosWredProfileGreenDropProbability':rcQosWredProfileGreenDropProbability,'rcQosWredProfileYellowDropStartPoint':rcQosWredProfileYellowDropStartPoint,'rcQosWredProfileYellowDropEndPoint':rcQosWredProfileYellowDropEndPoint,'rcQosWredProfileYellowDropProbability':rcQosWredProfileYellowDropProbability,'rcQosWredProfileRedDropStartPoint':rcQosWredProfileRedDropStartPoint,'rcQosWredProfileRedDropEndPoint':rcQosWredProfileRedDropEndPoint,'rcQosWredProfileRedDropProbability':rcQosWredProfileRedDropProbability,'rcQosWredProfileDesc':rcQosWredProfileDesc,'rcQosWredProfileRef':rcQosWredProfileRef,'rcQosWredProfileStatus':rcQosWredProfileStatus,'rcQosGloWredProfileTable':rcQosGloWredProfileTable,'rcQosGloWredProfileEntry':rcQosGloWredProfileEntry,_AD:rcQosGloWredProfileQueueId,'rcQosGloWredProfileIndex':rcQosGloWredProfileIndex,'rcQosGloWredProfileStatus':rcQosGloWredProfileStatus,'rcQosPortWredProfileTable':rcQosPortWredProfileTable,'rcQosPortWredProfileEntry':rcQosPortWredProfileEntry,_AE:rcQosPortWredProfilePortId,_AF:rcQosPortWredProfileQueueId,'rcQosPortWredProfileIndex':rcQosPortWredProfileIndex,'rcQosPortWredProfileStatus':rcQosPortWredProfileStatus,'raisecomQosTrafficClass':raisecomQosTrafficClass,'rcPolicyEnable':rcPolicyEnable,'rcQosServicePolicyTable':rcQosServicePolicyTable,'rcQosServicePolicyEntry':rcQosServicePolicyEntry,_AG:rcQosServicePolicyIngress,'rcQosServicePolicyEgress':rcQosServicePolicyEgress,'rcQosServicePolicyMapName':rcQosServicePolicyMapName,'rcQosServicePolicyStatus':rcQosServicePolicyStatus,'rcQosPolicyMapCfgTable':rcQosPolicyMapCfgTable,'rcQosPolicyMapCfgEntry':rcQosPolicyMapCfgEntry,_AH:rcQosPolicyMapName,'rcQosPolicyMapDesc':rcQosPolicyMapDesc,'rcQosPolicyMapCfgStatus':rcQosPolicyMapCfgStatus,'rcQosPolicyMapType':rcQosPolicyMapType,'rcQosCMCfgTable':rcQosCMCfgTable,'rcQosCMCfgEntry':rcQosCMCfgEntry,_AI:rcQosCMName,'rcQosCMDesc':rcQosCMDesc,'rcQosCMMatchType':rcQosCMMatchType,'rcQosCMClassID':rcQosCMClassID,'rcQosCMStatus':rcQosCMStatus,'rcQosCMDoubleTagging':rcQosCMDoubleTagging,'rcQosMatchStmtTable':rcQosMatchStmtTable,'rcQosMatchStmtEntry':rcQosMatchStmtEntry,_AJ:rcQosMatchStmtClassName,_AK:rcQosMatchStmtType,_AL:rcQosMatchStmtValue,'rcQosMatchStmtSubName':rcQosMatchStmtSubName,'rcQosMatchStmtStatus':rcQosMatchStmtStatus,'rcQosPolicerCfgTable':rcQosPolicerCfgTable,'rcQosPolicerCfgEntry':rcQosPolicerCfgEntry,_AM:rcQosPolicerCfgName,'rcQosPolicerCfgType':rcQosPolicerCfgType,'rcQosPolicerCfgMode':rcQosPolicerCfgMode,'rcQosPolicerCfgCIR':rcQosPolicerCfgCIR,'rcQosPolicerCfgEIR':rcQosPolicerCfgEIR,'rcQosPolicerCfgCBS':rcQosPolicerCfgCBS,'rcQosPolicerCfgEBS':rcQosPolicerCfgEBS,'rcQosPolicerGreenActType':rcQosPolicerGreenActType,'rcQosPolicerGreenActDscp':rcQosPolicerGreenActDscp,'rcQosPolicerGreenActCos':rcQosPolicerGreenActCos,'rcQosPolicerGreenActLocalPrio':rcQosPolicerGreenActLocalPrio,'rcQosPolicerGreenActColor':rcQosPolicerGreenActColor,'rcQosPolicerGreenActCopytoCpu':rcQosPolicerGreenActCopytoCpu,'rcQosPolicerYellowActType':rcQosPolicerYellowActType,'rcQosPolicerYellowActDscp':rcQosPolicerYellowActDscp,'rcQosPolicerYellowActCos':rcQosPolicerYellowActCos,'rcQosPolicerYellowActLocalPrio':rcQosPolicerYellowActLocalPrio,'rcQosPolicerYellowActColor':rcQosPolicerYellowActColor,'rcQosPolicerYellowActCopytoCpu':rcQosPolicerYellowActCopytoCpu,'rcQosPolicerRedActType':rcQosPolicerRedActType,'rcQosPolicerRedActDscp':rcQosPolicerRedActDscp,'rcQosPolicerRedActCos':rcQosPolicerRedActCos,'rcQosPolicerRedActLocalPrio':rcQosPolicerRedActLocalPrio,'rcQosPolicerRedActColor':rcQosPolicerRedActColor,'rcQosPolicerRedActCopytoCpu':rcQosPolicerRedActCopytoCpu,'rcQosPolicerColorMode':rcQosPolicerColorMode,'rcQoSPolicerRef':rcQoSPolicerRef,'rcQosPolicerStatus':rcQosPolicerStatus,'rcQosActionCfgTable':rcQosActionCfgTable,'rcQosActionCfgEntry':rcQosActionCfgEntry,_AP:rcQosActionPmapName,_AQ:rcQosActionCmapName,'rcQosActionType':rcQosActionType,'rcQosActionSetValue':rcQosActionSetValue,'rcQosActionPoliceName':rcQosActionPoliceName,'rcQosActionStatsEnable':rcQosActionStatsEnable,'rcQosActionStatus':rcQosActionStatus,'rcQosActionRedirectPort':rcQosActionRedirectPort,'rcQosActionSetVlan':rcQosActionSetVlan,'rcQosActionSetInnerVlan':rcQosActionSetInnerVlan,'rcQosActionAddOuterVlan':rcQosActionAddOuterVlan,'rcQosActionCopyToMirror':rcQosActionCopyToMirror,'rcQosActionMirrorToPort':rcQosActionMirrorToPort,'rcQosActionSetLocalPriority':rcQosActionSetLocalPriority,'rcQosActionHierarchyPoliceName':rcQosActionHierarchyPoliceName,'rcQosActionSetIpPrece':rcQosActionSetIpPrece,'rcQosActionSetIpDscp':rcQosActionSetIpDscp,'rcQosActionSetCos':rcQosActionSetCos,'rcQosActionSetIPAddressType':rcQosActionSetIPAddressType,'rcQosActionSetIPAddress':rcQosActionSetIPAddress,'rcQosActionCopyToMirrorSession':rcQosActionCopyToMirrorSession,'rcQosServicePolicyEgressTable':rcQosServicePolicyEgressTable,'rcQosServicePolicyEgressEntry':rcQosServicePolicyEgressEntry,_AR:rcQosServicePolicyEgressIndex,'rcQosServicePolicyEgressMapName':rcQosServicePolicyEgressMapName,'rcQosServicePolicyEgressStatus':rcQosServicePolicyEgressStatus,'rcQosCosServicePolicyTable':rcQosCosServicePolicyTable,'rcQosCosServicePolicyEntry':rcQosCosServicePolicyEntry,_AS:rcQosCosServicePolicyPort,_AT:rcQosCosServicePolicyVlan,'rcQosCosServicePolicyMapName':rcQosCosServicePolicyMapName,'rcQosCosServicePolicyRowStatus':rcQosCosServicePolicyRowStatus,'rcQosVlanPolicyTable':rcQosVlanPolicyTable,'rcQosVlanPolicyEntry':rcQosVlanPolicyEntry,_AU:rcQosVlanPolicyPmapName,_AV:rcQosVlanPolicyVlan,'rcQosVlanPolicyPolicerName':rcQosVlanPolicyPolicerName,'rcQosVlanPolicyRowStatus':rcQosVlanPolicyRowStatus,'rcQosCosPolicyTable':rcQosCosPolicyTable,'rcQosCosPolicyEntry':rcQosCosPolicyEntry,_AW:rcQosCosPolicyPmapName,_AX:rcQosCosPolicyCos,'rcQosCosPolicyPolicerName':rcQosCosPolicyPolicerName,'rcQosCosPolicyRowStatus':rcQosCosPolicyRowStatus,'rcQosBandwidthProfileCfgTable':rcQosBandwidthProfileCfgTable,'rcQosBandwidthProfileCfgEntry':rcQosBandwidthProfileCfgEntry,_AY:rcQosBandwidthProfileCfgIndex,'rcQosBandwidthProfileCfgCIR':rcQosBandwidthProfileCfgCIR,'rcQosBandwidthProfileCfgEIR':rcQosBandwidthProfileCfgEIR,'rcQosBandwidthProfileCfgCBS':rcQosBandwidthProfileCfgCBS,'rcQosBandwidthProfileCfgEBS':rcQosBandwidthProfileCfgEBS,'rcQosBandwidthProfileColorMode':rcQosBandwidthProfileColorMode,'rcQosBandwidthProfileCoupling':rcQosBandwidthProfileCoupling,'rcQoSBandwidthProfileRef':rcQoSBandwidthProfileRef,'rcQosBandwidthProfileStatus':rcQosBandwidthProfileStatus,'rcQosBandwidthProfileDesc':rcQosBandwidthProfileDesc,'rcQosHierarchyCosIndexCfgTable':rcQosHierarchyCosIndexCfgTable,'rcQosHierarchyCosIndexCfgEntry':rcQosHierarchyCosIndexCfgEntry,_AZ:rcQosHierarchyCosIndex,'rcQosHierarchyCosRef':rcQosHierarchyCosRef,'rcQosHierarchyCosCfgStatus':rcQosHierarchyCosCfgStatus,'rcQosHierarchyCosCfgDesc':rcQosHierarchyCosCfgDesc,'rcQosHCosBandwidthProfileTable':rcQosHCosBandwidthProfileTable,'rcQosHCosBandwidthProfileEntry':rcQosHCosBandwidthProfileEntry,_Aa:rcQosHCosBandwidthProfileIndex,_Ab:rcQosHCosBandwidthProfileCos,'rcQosHCosBandwidthProfileBwpIndex':rcQosHCosBandwidthProfileBwpIndex,'rcQoSHCosBandwidthProfileRef':rcQoSHCosBandwidthProfileRef,'rcQosHCosBandwidthProfileRowStatus':rcQosHCosBandwidthProfileRowStatus,'rcQosHierarchyVlanIndexCfgTable':rcQosHierarchyVlanIndexCfgTable,'rcQosHierarchyVlanIndexCfgEntry':rcQosHierarchyVlanIndexCfgEntry,_Ac:rcQosHierarchyVlanIndex,'rcQosHierarchyVlanRef':rcQosHierarchyVlanRef,'rcQosHierarchyVlanCfgStatus':rcQosHierarchyVlanCfgStatus,'rcQosHierarchyVlanCfgDesc':rcQosHierarchyVlanCfgDesc,'rcQosHVlanBandwidthProfileTable':rcQosHVlanBandwidthProfileTable,'rcQosHVlanBandwidthProfileEntry':rcQosHVlanBandwidthProfileEntry,_Ad:rcQosHVlanBandwidthProfileIndex,_Ae:rcQosHVlanBandwidthProfileVlan,'rcQosHVlanBandwidthProfileBwpIndex':rcQosHVlanBandwidthProfileBwpIndex,'rcQoSHVlanBandwidthProfileRef':rcQoSHVlanBandwidthProfileRef,'rcQosHVlanBandwidthProfileRowStatus':rcQosHVlanBandwidthProfileRowStatus,'rcQosBandwidthPortTable':rcQosBandwidthPortTable,'rcQosBandwidthPortEntry':rcQosBandwidthPortEntry,_X:rcQosBandwidthPortIndex,_Ap:rcQosBandwidthPortBwpIndex,_Aq:rcQosBandwidthPortEgrBwpIndex,_Ar:rcQosBandwidthPortHBwEnable,_As:rcQosBandwidthPortHvBwpIndex,'rcQosBandwidthPortDeiRemarkEnable':rcQosBandwidthPortDeiRemarkEnable,'rcQosBandwidthPortColorAwareEnable':rcQosBandwidthPortColorAwareEnable,'rcQosBandwidthVlanTable':rcQosBandwidthVlanTable,'rcQosBandwidthVlanEntry':rcQosBandwidthVlanEntry,_Z:rcQosBandwidthVlanIndex,_Y:rcQosBandwidthVlanPort,_a:rcQosBandwidthVlanPortType,_At:rcQosBandwidthVlanBwpIndex,_Au:rcQosBandwidthVlanHBwEnable,_Av:rcQosBandwidthVlanHcBwpIndex,'rcQosBandwidthVlanRowStatus':rcQosBandwidthVlanRowStatus,'rcQosBandwidthCosTable':rcQosBandwidthCosTable,'rcQosBandwidthCosEntry':rcQosBandwidthCosEntry,_d:rcQosBandwidthCosIndex,_c:rcQosBandwidthCosVlan,_b:rcQosBandwidthCosPort,_e:rcQosBandwidthCosPortType,_Aw:rcQosBandwidthCosBwpIndex,'rcQosBandwidthCosRowStatus':rcQosBandwidthCosRowStatus,'rcQosBandwidthGlobalEnable':rcQosBandwidthGlobalEnable,'rcQosBandwidthNotificationGroup':rcQosBandwidthNotificationGroup,'rcQosBandwidthPortModification':rcQosBandwidthPortModification,'rcQosBandwidthVlanModification':rcQosBandwidthVlanModification,'rcQosBandwidthCosModification':rcQosBandwidthCosModification,'raisecomQosStatistics':raisecomQosStatistics,'rcQosTrafficStatsTable':rcQosTrafficStatsTable,'rcQosTrafficStatsEntry':rcQosTrafficStatsEntry,_Af:rcQosTrafficStatsPort,_Ag:rcQosTrafficStatsDirection,_Ah:rcQosTrafficStatsCmapName,'rcQosTrafficStatsPolicerType':rcQosTrafficStatsPolicerType,'rcQosTrafficCounterReset':rcQosTrafficCounterReset,'rcQosTrafficPolicyName':rcQosTrafficPolicyName,'rcQosTrafficPolicerName':rcQosTrafficPolicerName,'rcQosTrafficCounterHwStatus':rcQosTrafficCounterHwStatus,'rcQosTrafficStatisticsUnit':rcQosTrafficStatisticsUnit,'rcQosTrafficCounterInprofilePkt64':rcQosTrafficCounterInprofilePkt64,'rcQosTrafficCounterInprofileByte64':rcQosTrafficCounterInprofileByte64,'rcQosTrafficCounterOutprofilePkt64':rcQosTrafficCounterOutprofilePkt64,'rcQosTrafficCounterOutprofileByte64':rcQosTrafficCounterOutprofileByte64,'rcQosTrafficbStatistics':rcQosTrafficbStatistics,'rcQosVlanStatisticsTable':rcQosVlanStatisticsTable,'rcQosVlanStatisticsEntry':rcQosVlanStatisticsEntry,_Ai:rcQosVlanStatisticsPort,_Aj:rcQosVlanStatisticsVlan,_Ak:rcQosVlanStatisticsDirection,'rcQosVlanStatisticsUnit':rcQosVlanStatisticsUnit,'rcQosVlanStatisticsReset':rcQosVlanStatisticsReset,'rcQosVlanStatisticsPkt':rcQosVlanStatisticsPkt,'rcQosVlanStatisticsByte':rcQosVlanStatisticsByte,'rcQosVlanStatisticsRowStatus':rcQosVlanStatisticsRowStatus,'rcQosCosStatisticsTable':rcQosCosStatisticsTable,'rcQosCosStatisticsEntry':rcQosCosStatisticsEntry,_Al:rcQosCosStatisticsPort,_Am:rcQosCosStatisticsVlan,_An:rcQosCosStatisticsCos,_Ao:rcQosCosStatisticsDirection,'rcQosCosStatisticsUnit':rcQosCosStatisticsUnit,'rcQosCosStatisticsReset':rcQosCosStatisticsReset,'rcQosCosStatisticsPkt':rcQosCosStatisticsPkt,'rcQosCosStatisticsByte':rcQosCosStatisticsByte,'rcQosCosStatisticsRowStatus':rcQosCosStatisticsRowStatus})