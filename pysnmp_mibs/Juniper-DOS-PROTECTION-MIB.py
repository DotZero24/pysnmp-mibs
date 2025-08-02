_A7='juniDosProtectionGroup2'
_A6='juniDosProtectionGroup'
_A5='juniDosProtectionDpgProfileName'
_A4='juniDosProtectionDpgProfileRowStatus'
_A3='juniDosProtectionDpgAttachName'
_A2='juniDosProtectionDpgAttachRowStatus'
_A1='juniDosProtectionDpgPriorityModified'
_A0='juniDosProtectionDpgPriorityRate'
_z='juniDosProtectionDpgPriorityOverSubscriptionFactor'
_y='juniDosProtectionDpgPriorityBurst'
_x='juniDosProtectionDpgProtocolModified'
_w='juniDosProtectionDpgProtocolWeight'
_v='juniDosProtectionDpgProtocolSkipPriorityRateLimiter'
_u='juniDosProtectionDpgProtocolRate'
_t='juniDosProtectionDpgProtocolDropProbability'
_s='juniDosProtectionDpgProtocolBurst'
_r='juniDosProtectionDpgReferences'
_q='juniDosProtectionDpgModified'
_p='juniDosProtectionDpgRevert'
_o='juniDosProtectionDpgCanned'
_n='juniDosProtectionDpgRowStatus'
_m='obsolete'
_l='juniDosProtectionDpgProfileLayerId'
_k='juniDosProtectionDpgProfileProfileId'
_j='juniDosProtectionDpgAttachIndex'
_i='juniDosProtectionDpgPriorityPriority'
_h='juniDosProtectionDpgPriorityName'
_g='juniDosProtectionDpgProtocolProtocol'
_f='juniDosProtectionDpgProtocolName'
_e='JuniDosProtectionProtocolCannedType'
_d='juniDosProtectionDpgIndex'
_c='juniDosProtectionScfdsProtocolIndex'
_b='dataPath'
_a='juniDosProtectionScfdsProtocolTransitions'
_Z='juniDosProtectionScfdsProtocolState'
_Y='juniDosProtectionScfdsProtocolBackoffTime'
_X='juniDosProtectionScfdsProtocolLowThreshold'
_W='juniDosProtectionScfdsProtocolThreshold'
_V='juniDosProtectionScfdsGlobalNumberTableOverflows'
_U='juniDosProtectionScfdsGlobalNumberFalseNegativeFlows'
_T='juniDosProtectionScfdsGlobalCurrentFalseNegativeFlows'
_S='juniDosProtectionScfdsGlobalNumberSuspiciousFlowGroups'
_R='juniDosProtectionScfdsGlobalCurrentSuspiciousFlowGroups'
_Q='juniDosProtectionScfdsGlobalNumberSuspiciousFlows'
_P='juniDosProtectionScfdsGlobalCurrentSuspiciousFlows'
_O='juniDosProtectionScfdsGlobalTableOverflowState'
_N='juniDosProtectionScfdsGlobalDiscontinuityTime'
_M='juniDosProtectionScfdsGlobalClearAll'
_L='juniDosProtectionScfdsGlobalGrouping'
_K='juniDosProtectionScfdsGlobalState'
_J='Integer32'
_I='JuniEnable'
_H='DisplayString'
_G='read-create'
_F='not-accessible'
_E='Unsigned32'
_D='read-write'
_C='read-only'
_B='Juniper-DOS-PROTECTION-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
InterfaceIndex,=mibBuilder.importSymbols('IF-MIB','InterfaceIndex')
juniMibs,=mibBuilder.importSymbols('Juniper-MIBs','juniMibs')
JuniEnable,=mibBuilder.importSymbols('Juniper-TC',_I)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_J,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_E,'iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC',_H,'PhysAddress','RowStatus','TextualConvention','TruthValue')
juniDosProtectionMIB=ModuleIdentity((1,3,6,1,4,1,4874,2,2,80))
if mibBuilder.loadTexts:juniDosProtectionMIB.setRevisions(('2008-05-06 00:00','2006-07-01 00:00','2006-08-18 04:00','2006-08-17 19:26','2006-01-01 05:00'))
class JuniDosProtectionProtocolType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74)));namedValues=NamedValues(*(('pppEchoRequest',0),('ppEchoReply',1),('pppEchoReplyFast',2),('pppControl',3),('atmControl',4),('atmOam',5),('atmDynamicIf',6),('atmInverseArp',7),('frameRelayControl',8),('frameRelayArp',9),('pppoeControl',10),('pppoePppConfig',11),('ethernetArpMiss',12),('ethernetArp',13),('ethernetFcBasedArp',14),('ethernetLacp',15),('ethernetOam',16),('ethernetDynamicIf',17),('ethernetPppTerminate',18),('slepSlarp',19),('slepSlarpReplyFast',20),('mplsTtlOnReceive',21),('mplsTtlOnTransmit',22),('mplsMtuExceeded',23),('itmL2tpControl',24),('flisInPayload',25),('flisInPayloadUpdateTable',26),('dhcpExternal',27),('ipOsi',28),('ipTtlExpired',29),('ipOptionsOther',30),('ipOptionsRouterAlert',31),('ipMulticastBroadcastOther',32),('ipMulticastDhcpSc',33),('ipMulticastControlSc',34),('ipMulticastControlIc',35),('ipMulticastVrrp',36),('ipMulticastCacheMiss',37),('ipMulticastCacheMissAutoReply',38),('ipMulticastWrongIf',39),('ipLocalDhcpSc',40),('ipLocalDhcpIc',41),('ipLocalIcmpEcho',42),('ipLocalIcmpOther',43),('ipLocalLDP',44),('ipLocalBgp',45),('ipLocalOspf',46),('ipLocalRsvp',47),('ipLocalPim',48),('ipLocalCops',49),('ipLocalL2tpControlSc',50),('ipLocalL2tpControlIc',51),('ipLocalOther',52),('ipLocalDemuxMiss',53),('ipRouteToSrpEthernet',54),('ipRouteNoRoute',55),('ipNull0Interface',56),('ipNormalPathMtu',57),('ipNeighborDiscovery',58),('ipNeighborDiscoveryMiss',59),('ipSearchError',60),('ipMld',61),('ipLocalPimAssert',62),('ipLocalBfd',63),('ipFastBfd',64),('ipLocalFastBfd',65),('ipIke',66),('ipReassembly',67),('ipLocalIcmpFragment',68),('ipLocalFragment',69),('ipAppClassifierHttpRedirect',70),('ipMulticastDhcpIc',71),('dhcpTesterIc',72),('atmDynamicIfPppData',73),('ipLocalLspPing',74)))
class JuniDosProtectionPriorityType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7)));namedValues=NamedValues(*(('hiGreenFcIc',0),('hiYellowFcIc',1),('loGreenFcIc',2),('loYellowFcIc',3),('hiGreenFcSc',4),('hiYellowFcSc',5),('loGreenFcSc',6),('loYellowFcSc',7)))
class JuniDosProtectionProtocolState(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('ok',1),('inTrouble',2)))
class JuniDosProtectionScfdsTableOverflowState(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('notOverflowingOrGrouping',1),('grouping',2),('overflowing',3)))
class JuniDosProtectionProtocolPriorityType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4)));namedValues=NamedValues(*(('hiGreen',0),('hiYellow',1),('loGreen',2),('loYellow',3),(_b,4)))
class JuniDosProtectionProtocolCannedType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4)));namedValues=NamedValues(*(('default',0),('enetAccess',1),('atmAccess',2),('frame',3),('uplink',4)))
class JuniDosProtectionLayerId(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,6,11,17,19,35,50)));namedValues=NamedValues(*(('ip',0),('ppp',1),('ethernet',6),('atm1483',11),('pppoe',17),('bridge1483',19),('vlan',35),('ipv6',50)))
class JuniDosProtectionControlProcessorDestination(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('ic',0),('sc',1),(_b,2)))
_JuniDosProtectionObjects_ObjectIdentity=ObjectIdentity
juniDosProtectionObjects=_JuniDosProtectionObjects_ObjectIdentity((1,3,6,1,4,1,4874,2,2,80,1))
_JuniDosProtectionScfdsGroup_ObjectIdentity=ObjectIdentity
juniDosProtectionScfdsGroup=_JuniDosProtectionScfdsGroup_ObjectIdentity((1,3,6,1,4,1,4874,2,2,80,1,1))
class _JuniDosProtectionScfdsGlobalState_Type(JuniEnable):defaultValue=1
_JuniDosProtectionScfdsGlobalState_Type.__name__=_I
_JuniDosProtectionScfdsGlobalState_Object=MibScalar
juniDosProtectionScfdsGlobalState=_JuniDosProtectionScfdsGlobalState_Object((1,3,6,1,4,1,4874,2,2,80,1,1,1),_JuniDosProtectionScfdsGlobalState_Type())
juniDosProtectionScfdsGlobalState.setMaxAccess(_D)
if mibBuilder.loadTexts:juniDosProtectionScfdsGlobalState.setStatus(_A)
class _JuniDosProtectionScfdsGlobalGrouping_Type(JuniEnable):defaultValue=1
_JuniDosProtectionScfdsGlobalGrouping_Type.__name__=_I
_JuniDosProtectionScfdsGlobalGrouping_Object=MibScalar
juniDosProtectionScfdsGlobalGrouping=_JuniDosProtectionScfdsGlobalGrouping_Object((1,3,6,1,4,1,4874,2,2,80,1,1,2),_JuniDosProtectionScfdsGlobalGrouping_Type())
juniDosProtectionScfdsGlobalGrouping.setMaxAccess(_D)
if mibBuilder.loadTexts:juniDosProtectionScfdsGlobalGrouping.setStatus(_A)
class _JuniDosProtectionScfdsGlobalClearAll_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('ok',0),('clear',1)))
_JuniDosProtectionScfdsGlobalClearAll_Type.__name__=_J
_JuniDosProtectionScfdsGlobalClearAll_Object=MibScalar
juniDosProtectionScfdsGlobalClearAll=_JuniDosProtectionScfdsGlobalClearAll_Object((1,3,6,1,4,1,4874,2,2,80,1,1,3),_JuniDosProtectionScfdsGlobalClearAll_Type())
juniDosProtectionScfdsGlobalClearAll.setMaxAccess(_D)
if mibBuilder.loadTexts:juniDosProtectionScfdsGlobalClearAll.setStatus(_A)
_JuniDosProtectionScfdsGlobalDiscontinuityTime_Type=Unsigned32
_JuniDosProtectionScfdsGlobalDiscontinuityTime_Object=MibScalar
juniDosProtectionScfdsGlobalDiscontinuityTime=_JuniDosProtectionScfdsGlobalDiscontinuityTime_Object((1,3,6,1,4,1,4874,2,2,80,1,1,4),_JuniDosProtectionScfdsGlobalDiscontinuityTime_Type())
juniDosProtectionScfdsGlobalDiscontinuityTime.setMaxAccess(_C)
if mibBuilder.loadTexts:juniDosProtectionScfdsGlobalDiscontinuityTime.setStatus(_A)
_JuniDosProtectionScfdsGlobalTableOverflowState_Type=JuniDosProtectionScfdsTableOverflowState
_JuniDosProtectionScfdsGlobalTableOverflowState_Object=MibScalar
juniDosProtectionScfdsGlobalTableOverflowState=_JuniDosProtectionScfdsGlobalTableOverflowState_Object((1,3,6,1,4,1,4874,2,2,80,1,1,5),_JuniDosProtectionScfdsGlobalTableOverflowState_Type())
juniDosProtectionScfdsGlobalTableOverflowState.setMaxAccess(_C)
if mibBuilder.loadTexts:juniDosProtectionScfdsGlobalTableOverflowState.setStatus(_A)
_JuniDosProtectionScfdsGlobalCurrentSuspiciousFlows_Type=Counter32
_JuniDosProtectionScfdsGlobalCurrentSuspiciousFlows_Object=MibScalar
juniDosProtectionScfdsGlobalCurrentSuspiciousFlows=_JuniDosProtectionScfdsGlobalCurrentSuspiciousFlows_Object((1,3,6,1,4,1,4874,2,2,80,1,1,6),_JuniDosProtectionScfdsGlobalCurrentSuspiciousFlows_Type())
juniDosProtectionScfdsGlobalCurrentSuspiciousFlows.setMaxAccess(_C)
if mibBuilder.loadTexts:juniDosProtectionScfdsGlobalCurrentSuspiciousFlows.setStatus(_A)
_JuniDosProtectionScfdsGlobalNumberSuspiciousFlows_Type=Counter32
_JuniDosProtectionScfdsGlobalNumberSuspiciousFlows_Object=MibScalar
juniDosProtectionScfdsGlobalNumberSuspiciousFlows=_JuniDosProtectionScfdsGlobalNumberSuspiciousFlows_Object((1,3,6,1,4,1,4874,2,2,80,1,1,7),_JuniDosProtectionScfdsGlobalNumberSuspiciousFlows_Type())
juniDosProtectionScfdsGlobalNumberSuspiciousFlows.setMaxAccess(_C)
if mibBuilder.loadTexts:juniDosProtectionScfdsGlobalNumberSuspiciousFlows.setStatus(_A)
_JuniDosProtectionScfdsGlobalCurrentSuspiciousFlowGroups_Type=Counter32
_JuniDosProtectionScfdsGlobalCurrentSuspiciousFlowGroups_Object=MibScalar
juniDosProtectionScfdsGlobalCurrentSuspiciousFlowGroups=_JuniDosProtectionScfdsGlobalCurrentSuspiciousFlowGroups_Object((1,3,6,1,4,1,4874,2,2,80,1,1,8),_JuniDosProtectionScfdsGlobalCurrentSuspiciousFlowGroups_Type())
juniDosProtectionScfdsGlobalCurrentSuspiciousFlowGroups.setMaxAccess(_C)
if mibBuilder.loadTexts:juniDosProtectionScfdsGlobalCurrentSuspiciousFlowGroups.setStatus(_A)
_JuniDosProtectionScfdsGlobalNumberSuspiciousFlowGroups_Type=Counter32
_JuniDosProtectionScfdsGlobalNumberSuspiciousFlowGroups_Object=MibScalar
juniDosProtectionScfdsGlobalNumberSuspiciousFlowGroups=_JuniDosProtectionScfdsGlobalNumberSuspiciousFlowGroups_Object((1,3,6,1,4,1,4874,2,2,80,1,1,9),_JuniDosProtectionScfdsGlobalNumberSuspiciousFlowGroups_Type())
juniDosProtectionScfdsGlobalNumberSuspiciousFlowGroups.setMaxAccess(_C)
if mibBuilder.loadTexts:juniDosProtectionScfdsGlobalNumberSuspiciousFlowGroups.setStatus(_A)
_JuniDosProtectionScfdsGlobalCurrentFalseNegativeFlows_Type=Counter32
_JuniDosProtectionScfdsGlobalCurrentFalseNegativeFlows_Object=MibScalar
juniDosProtectionScfdsGlobalCurrentFalseNegativeFlows=_JuniDosProtectionScfdsGlobalCurrentFalseNegativeFlows_Object((1,3,6,1,4,1,4874,2,2,80,1,1,10),_JuniDosProtectionScfdsGlobalCurrentFalseNegativeFlows_Type())
juniDosProtectionScfdsGlobalCurrentFalseNegativeFlows.setMaxAccess(_C)
if mibBuilder.loadTexts:juniDosProtectionScfdsGlobalCurrentFalseNegativeFlows.setStatus(_A)
_JuniDosProtectionScfdsGlobalNumberFalseNegativeFlows_Type=Counter32
_JuniDosProtectionScfdsGlobalNumberFalseNegativeFlows_Object=MibScalar
juniDosProtectionScfdsGlobalNumberFalseNegativeFlows=_JuniDosProtectionScfdsGlobalNumberFalseNegativeFlows_Object((1,3,6,1,4,1,4874,2,2,80,1,1,11),_JuniDosProtectionScfdsGlobalNumberFalseNegativeFlows_Type())
juniDosProtectionScfdsGlobalNumberFalseNegativeFlows.setMaxAccess(_C)
if mibBuilder.loadTexts:juniDosProtectionScfdsGlobalNumberFalseNegativeFlows.setStatus(_A)
_JuniDosProtectionScfdsGlobalNumberTableOverflows_Type=Counter32
_JuniDosProtectionScfdsGlobalNumberTableOverflows_Object=MibScalar
juniDosProtectionScfdsGlobalNumberTableOverflows=_JuniDosProtectionScfdsGlobalNumberTableOverflows_Object((1,3,6,1,4,1,4874,2,2,80,1,1,12),_JuniDosProtectionScfdsGlobalNumberTableOverflows_Type())
juniDosProtectionScfdsGlobalNumberTableOverflows.setMaxAccess(_C)
if mibBuilder.loadTexts:juniDosProtectionScfdsGlobalNumberTableOverflows.setStatus(_A)
_JuniDosProtectionScfdsProtocolTable_Object=MibTable
juniDosProtectionScfdsProtocolTable=_JuniDosProtectionScfdsProtocolTable_Object((1,3,6,1,4,1,4874,2,2,80,1,1,13))
if mibBuilder.loadTexts:juniDosProtectionScfdsProtocolTable.setStatus(_A)
_JuniDosProtectionScfdsProtocolEntry_Object=MibTableRow
juniDosProtectionScfdsProtocolEntry=_JuniDosProtectionScfdsProtocolEntry_Object((1,3,6,1,4,1,4874,2,2,80,1,1,13,1))
juniDosProtectionScfdsProtocolEntry.setIndexNames((0,_B,_c))
if mibBuilder.loadTexts:juniDosProtectionScfdsProtocolEntry.setStatus(_A)
_JuniDosProtectionScfdsProtocolIndex_Type=JuniDosProtectionProtocolType
_JuniDosProtectionScfdsProtocolIndex_Object=MibTableColumn
juniDosProtectionScfdsProtocolIndex=_JuniDosProtectionScfdsProtocolIndex_Object((1,3,6,1,4,1,4874,2,2,80,1,1,13,1,1),_JuniDosProtectionScfdsProtocolIndex_Type())
juniDosProtectionScfdsProtocolIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:juniDosProtectionScfdsProtocolIndex.setStatus(_A)
class _JuniDosProtectionScfdsProtocolThreshold_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(3,65535))
_JuniDosProtectionScfdsProtocolThreshold_Type.__name__=_E
_JuniDosProtectionScfdsProtocolThreshold_Object=MibTableColumn
juniDosProtectionScfdsProtocolThreshold=_JuniDosProtectionScfdsProtocolThreshold_Object((1,3,6,1,4,1,4874,2,2,80,1,1,13,1,2),_JuniDosProtectionScfdsProtocolThreshold_Type())
juniDosProtectionScfdsProtocolThreshold.setMaxAccess(_D)
if mibBuilder.loadTexts:juniDosProtectionScfdsProtocolThreshold.setStatus(_A)
class _JuniDosProtectionScfdsProtocolLowThreshold_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,32767))
_JuniDosProtectionScfdsProtocolLowThreshold_Type.__name__=_E
_JuniDosProtectionScfdsProtocolLowThreshold_Object=MibTableColumn
juniDosProtectionScfdsProtocolLowThreshold=_JuniDosProtectionScfdsProtocolLowThreshold_Object((1,3,6,1,4,1,4874,2,2,80,1,1,13,1,3),_JuniDosProtectionScfdsProtocolLowThreshold_Type())
juniDosProtectionScfdsProtocolLowThreshold.setMaxAccess(_D)
if mibBuilder.loadTexts:juniDosProtectionScfdsProtocolLowThreshold.setStatus(_A)
class _JuniDosProtectionScfdsProtocolBackoffTime_Type(Unsigned32):defaultValue=300;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(10,1000))
_JuniDosProtectionScfdsProtocolBackoffTime_Type.__name__=_E
_JuniDosProtectionScfdsProtocolBackoffTime_Object=MibTableColumn
juniDosProtectionScfdsProtocolBackoffTime=_JuniDosProtectionScfdsProtocolBackoffTime_Object((1,3,6,1,4,1,4874,2,2,80,1,1,13,1,4),_JuniDosProtectionScfdsProtocolBackoffTime_Type())
juniDosProtectionScfdsProtocolBackoffTime.setMaxAccess(_D)
if mibBuilder.loadTexts:juniDosProtectionScfdsProtocolBackoffTime.setStatus(_A)
_JuniDosProtectionScfdsProtocolState_Type=JuniDosProtectionProtocolState
_JuniDosProtectionScfdsProtocolState_Object=MibTableColumn
juniDosProtectionScfdsProtocolState=_JuniDosProtectionScfdsProtocolState_Object((1,3,6,1,4,1,4874,2,2,80,1,1,13,1,5),_JuniDosProtectionScfdsProtocolState_Type())
juniDosProtectionScfdsProtocolState.setMaxAccess(_C)
if mibBuilder.loadTexts:juniDosProtectionScfdsProtocolState.setStatus(_A)
_JuniDosProtectionScfdsProtocolTransitions_Type=Counter32
_JuniDosProtectionScfdsProtocolTransitions_Object=MibTableColumn
juniDosProtectionScfdsProtocolTransitions=_JuniDosProtectionScfdsProtocolTransitions_Object((1,3,6,1,4,1,4874,2,2,80,1,1,13,1,6),_JuniDosProtectionScfdsProtocolTransitions_Type())
juniDosProtectionScfdsProtocolTransitions.setMaxAccess(_C)
if mibBuilder.loadTexts:juniDosProtectionScfdsProtocolTransitions.setStatus(_A)
_JuniDosProtectionDpgGroup_ObjectIdentity=ObjectIdentity
juniDosProtectionDpgGroup=_JuniDosProtectionDpgGroup_ObjectIdentity((1,3,6,1,4,1,4874,2,2,80,1,2))
_JuniDosProtectionDpgTable_Object=MibTable
juniDosProtectionDpgTable=_JuniDosProtectionDpgTable_Object((1,3,6,1,4,1,4874,2,2,80,1,2,1))
if mibBuilder.loadTexts:juniDosProtectionDpgTable.setStatus(_A)
_JuniDosProtectionDpgEntry_Object=MibTableRow
juniDosProtectionDpgEntry=_JuniDosProtectionDpgEntry_Object((1,3,6,1,4,1,4874,2,2,80,1,2,1,1))
juniDosProtectionDpgEntry.setIndexNames((0,_B,_d))
if mibBuilder.loadTexts:juniDosProtectionDpgEntry.setStatus(_A)
class _JuniDosProtectionDpgIndex_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_JuniDosProtectionDpgIndex_Type.__name__=_H
_JuniDosProtectionDpgIndex_Object=MibTableColumn
juniDosProtectionDpgIndex=_JuniDosProtectionDpgIndex_Object((1,3,6,1,4,1,4874,2,2,80,1,2,1,1,1),_JuniDosProtectionDpgIndex_Type())
juniDosProtectionDpgIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:juniDosProtectionDpgIndex.setStatus(_A)
_JuniDosProtectionDpgRowStatus_Type=RowStatus
_JuniDosProtectionDpgRowStatus_Object=MibTableColumn
juniDosProtectionDpgRowStatus=_JuniDosProtectionDpgRowStatus_Object((1,3,6,1,4,1,4874,2,2,80,1,2,1,1,2),_JuniDosProtectionDpgRowStatus_Type())
juniDosProtectionDpgRowStatus.setMaxAccess(_G)
if mibBuilder.loadTexts:juniDosProtectionDpgRowStatus.setStatus(_A)
class _JuniDosProtectionDpgCanned_Type(JuniDosProtectionProtocolCannedType):defaultValue=0
_JuniDosProtectionDpgCanned_Type.__name__=_e
_JuniDosProtectionDpgCanned_Object=MibTableColumn
juniDosProtectionDpgCanned=_JuniDosProtectionDpgCanned_Object((1,3,6,1,4,1,4874,2,2,80,1,2,1,1,3),_JuniDosProtectionDpgCanned_Type())
juniDosProtectionDpgCanned.setMaxAccess(_G)
if mibBuilder.loadTexts:juniDosProtectionDpgCanned.setStatus(_A)
class _JuniDosProtectionDpgRevert_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('no-revert',0),('revert',1)))
_JuniDosProtectionDpgRevert_Type.__name__=_J
_JuniDosProtectionDpgRevert_Object=MibTableColumn
juniDosProtectionDpgRevert=_JuniDosProtectionDpgRevert_Object((1,3,6,1,4,1,4874,2,2,80,1,2,1,1,4),_JuniDosProtectionDpgRevert_Type())
juniDosProtectionDpgRevert.setMaxAccess(_G)
if mibBuilder.loadTexts:juniDosProtectionDpgRevert.setStatus(_A)
_JuniDosProtectionDpgModified_Type=TruthValue
_JuniDosProtectionDpgModified_Object=MibTableColumn
juniDosProtectionDpgModified=_JuniDosProtectionDpgModified_Object((1,3,6,1,4,1,4874,2,2,80,1,2,1,1,5),_JuniDosProtectionDpgModified_Type())
juniDosProtectionDpgModified.setMaxAccess(_C)
if mibBuilder.loadTexts:juniDosProtectionDpgModified.setStatus(_A)
_JuniDosProtectionDpgReferences_Type=Integer32
_JuniDosProtectionDpgReferences_Object=MibTableColumn
juniDosProtectionDpgReferences=_JuniDosProtectionDpgReferences_Object((1,3,6,1,4,1,4874,2,2,80,1,2,1,1,6),_JuniDosProtectionDpgReferences_Type())
juniDosProtectionDpgReferences.setMaxAccess(_C)
if mibBuilder.loadTexts:juniDosProtectionDpgReferences.setStatus(_A)
_JuniDosProtectionDpgProtocolTable_Object=MibTable
juniDosProtectionDpgProtocolTable=_JuniDosProtectionDpgProtocolTable_Object((1,3,6,1,4,1,4874,2,2,80,1,2,2))
if mibBuilder.loadTexts:juniDosProtectionDpgProtocolTable.setStatus(_A)
_JuniDosProtectionDpgProtocolEntry_Object=MibTableRow
juniDosProtectionDpgProtocolEntry=_JuniDosProtectionDpgProtocolEntry_Object((1,3,6,1,4,1,4874,2,2,80,1,2,2,1))
juniDosProtectionDpgProtocolEntry.setIndexNames((0,_B,_f),(0,_B,_g))
if mibBuilder.loadTexts:juniDosProtectionDpgProtocolEntry.setStatus(_A)
class _JuniDosProtectionDpgProtocolName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_JuniDosProtectionDpgProtocolName_Type.__name__=_H
_JuniDosProtectionDpgProtocolName_Object=MibTableColumn
juniDosProtectionDpgProtocolName=_JuniDosProtectionDpgProtocolName_Object((1,3,6,1,4,1,4874,2,2,80,1,2,2,1,1),_JuniDosProtectionDpgProtocolName_Type())
juniDosProtectionDpgProtocolName.setMaxAccess(_F)
if mibBuilder.loadTexts:juniDosProtectionDpgProtocolName.setStatus(_A)
_JuniDosProtectionDpgProtocolProtocol_Type=JuniDosProtectionProtocolType
_JuniDosProtectionDpgProtocolProtocol_Object=MibTableColumn
juniDosProtectionDpgProtocolProtocol=_JuniDosProtectionDpgProtocolProtocol_Object((1,3,6,1,4,1,4874,2,2,80,1,2,2,1,2),_JuniDosProtectionDpgProtocolProtocol_Type())
juniDosProtectionDpgProtocolProtocol.setMaxAccess(_F)
if mibBuilder.loadTexts:juniDosProtectionDpgProtocolProtocol.setStatus(_A)
class _JuniDosProtectionDpgProtocolBurst_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(32,65535))
_JuniDosProtectionDpgProtocolBurst_Type.__name__=_E
_JuniDosProtectionDpgProtocolBurst_Object=MibTableColumn
juniDosProtectionDpgProtocolBurst=_JuniDosProtectionDpgProtocolBurst_Object((1,3,6,1,4,1,4874,2,2,80,1,2,2,1,3),_JuniDosProtectionDpgProtocolBurst_Type())
juniDosProtectionDpgProtocolBurst.setMaxAccess(_D)
if mibBuilder.loadTexts:juniDosProtectionDpgProtocolBurst.setStatus(_A)
class _JuniDosProtectionDpgProtocolDropProbability_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(10,100))
_JuniDosProtectionDpgProtocolDropProbability_Type.__name__=_E
_JuniDosProtectionDpgProtocolDropProbability_Object=MibTableColumn
juniDosProtectionDpgProtocolDropProbability=_JuniDosProtectionDpgProtocolDropProbability_Object((1,3,6,1,4,1,4874,2,2,80,1,2,2,1,4),_JuniDosProtectionDpgProtocolDropProbability_Type())
juniDosProtectionDpgProtocolDropProbability.setMaxAccess(_D)
if mibBuilder.loadTexts:juniDosProtectionDpgProtocolDropProbability.setStatus(_A)
class _JuniDosProtectionDpgProtocolRate_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(64,65535))
_JuniDosProtectionDpgProtocolRate_Type.__name__=_E
_JuniDosProtectionDpgProtocolRate_Object=MibTableColumn
juniDosProtectionDpgProtocolRate=_JuniDosProtectionDpgProtocolRate_Object((1,3,6,1,4,1,4874,2,2,80,1,2,2,1,5),_JuniDosProtectionDpgProtocolRate_Type())
juniDosProtectionDpgProtocolRate.setMaxAccess(_D)
if mibBuilder.loadTexts:juniDosProtectionDpgProtocolRate.setStatus(_A)
_JuniDosProtectionDpgProtocolSkipPriorityRateLimiter_Type=JuniEnable
_JuniDosProtectionDpgProtocolSkipPriorityRateLimiter_Object=MibTableColumn
juniDosProtectionDpgProtocolSkipPriorityRateLimiter=_JuniDosProtectionDpgProtocolSkipPriorityRateLimiter_Object((1,3,6,1,4,1,4874,2,2,80,1,2,2,1,6),_JuniDosProtectionDpgProtocolSkipPriorityRateLimiter_Type())
juniDosProtectionDpgProtocolSkipPriorityRateLimiter.setMaxAccess(_D)
if mibBuilder.loadTexts:juniDosProtectionDpgProtocolSkipPriorityRateLimiter.setStatus(_A)
class _JuniDosProtectionDpgProtocolWeight_Type(Unsigned32):defaultValue=100;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(100,500))
_JuniDosProtectionDpgProtocolWeight_Type.__name__=_E
_JuniDosProtectionDpgProtocolWeight_Object=MibTableColumn
juniDosProtectionDpgProtocolWeight=_JuniDosProtectionDpgProtocolWeight_Object((1,3,6,1,4,1,4874,2,2,80,1,2,2,1,7),_JuniDosProtectionDpgProtocolWeight_Type())
juniDosProtectionDpgProtocolWeight.setMaxAccess(_D)
if mibBuilder.loadTexts:juniDosProtectionDpgProtocolWeight.setStatus(_A)
_JuniDosProtectionDpgProtocolPriority_Type=JuniDosProtectionProtocolPriorityType
_JuniDosProtectionDpgProtocolPriority_Object=MibTableColumn
juniDosProtectionDpgProtocolPriority=_JuniDosProtectionDpgProtocolPriority_Object((1,3,6,1,4,1,4874,2,2,80,1,2,2,1,8),_JuniDosProtectionDpgProtocolPriority_Type())
juniDosProtectionDpgProtocolPriority.setMaxAccess(_D)
if mibBuilder.loadTexts:juniDosProtectionDpgProtocolPriority.setStatus(_A)
_JuniDosProtectionDpgProtocolModified_Type=TruthValue
_JuniDosProtectionDpgProtocolModified_Object=MibTableColumn
juniDosProtectionDpgProtocolModified=_JuniDosProtectionDpgProtocolModified_Object((1,3,6,1,4,1,4874,2,2,80,1,2,2,1,9),_JuniDosProtectionDpgProtocolModified_Type())
juniDosProtectionDpgProtocolModified.setMaxAccess(_C)
if mibBuilder.loadTexts:juniDosProtectionDpgProtocolModified.setStatus(_A)
_JuniDosProtectionDpgProtocolDestination_Type=JuniDosProtectionControlProcessorDestination
_JuniDosProtectionDpgProtocolDestination_Object=MibTableColumn
juniDosProtectionDpgProtocolDestination=_JuniDosProtectionDpgProtocolDestination_Object((1,3,6,1,4,1,4874,2,2,80,1,2,2,1,10),_JuniDosProtectionDpgProtocolDestination_Type())
juniDosProtectionDpgProtocolDestination.setMaxAccess(_C)
if mibBuilder.loadTexts:juniDosProtectionDpgProtocolDestination.setStatus(_A)
_JuniDosProtectionDpgPriorityTable_Object=MibTable
juniDosProtectionDpgPriorityTable=_JuniDosProtectionDpgPriorityTable_Object((1,3,6,1,4,1,4874,2,2,80,1,2,3))
if mibBuilder.loadTexts:juniDosProtectionDpgPriorityTable.setStatus(_A)
_JuniDosProtectionDpgPriorityEntry_Object=MibTableRow
juniDosProtectionDpgPriorityEntry=_JuniDosProtectionDpgPriorityEntry_Object((1,3,6,1,4,1,4874,2,2,80,1,2,3,1))
juniDosProtectionDpgPriorityEntry.setIndexNames((0,_B,_h),(0,_B,_i))
if mibBuilder.loadTexts:juniDosProtectionDpgPriorityEntry.setStatus(_A)
class _JuniDosProtectionDpgPriorityName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_JuniDosProtectionDpgPriorityName_Type.__name__=_H
_JuniDosProtectionDpgPriorityName_Object=MibTableColumn
juniDosProtectionDpgPriorityName=_JuniDosProtectionDpgPriorityName_Object((1,3,6,1,4,1,4874,2,2,80,1,2,3,1,1),_JuniDosProtectionDpgPriorityName_Type())
juniDosProtectionDpgPriorityName.setMaxAccess(_F)
if mibBuilder.loadTexts:juniDosProtectionDpgPriorityName.setStatus(_A)
_JuniDosProtectionDpgPriorityPriority_Type=JuniDosProtectionPriorityType
_JuniDosProtectionDpgPriorityPriority_Object=MibTableColumn
juniDosProtectionDpgPriorityPriority=_JuniDosProtectionDpgPriorityPriority_Object((1,3,6,1,4,1,4874,2,2,80,1,2,3,1,2),_JuniDosProtectionDpgPriorityPriority_Type())
juniDosProtectionDpgPriorityPriority.setMaxAccess(_F)
if mibBuilder.loadTexts:juniDosProtectionDpgPriorityPriority.setStatus(_A)
class _JuniDosProtectionDpgPriorityBurst_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(32,65535))
_JuniDosProtectionDpgPriorityBurst_Type.__name__=_E
_JuniDosProtectionDpgPriorityBurst_Object=MibTableColumn
juniDosProtectionDpgPriorityBurst=_JuniDosProtectionDpgPriorityBurst_Object((1,3,6,1,4,1,4874,2,2,80,1,2,3,1,3),_JuniDosProtectionDpgPriorityBurst_Type())
juniDosProtectionDpgPriorityBurst.setMaxAccess(_D)
if mibBuilder.loadTexts:juniDosProtectionDpgPriorityBurst.setStatus(_A)
class _JuniDosProtectionDpgPriorityOverSubscriptionFactor_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(100,1000))
_JuniDosProtectionDpgPriorityOverSubscriptionFactor_Type.__name__=_E
_JuniDosProtectionDpgPriorityOverSubscriptionFactor_Object=MibTableColumn
juniDosProtectionDpgPriorityOverSubscriptionFactor=_JuniDosProtectionDpgPriorityOverSubscriptionFactor_Object((1,3,6,1,4,1,4874,2,2,80,1,2,3,1,4),_JuniDosProtectionDpgPriorityOverSubscriptionFactor_Type())
juniDosProtectionDpgPriorityOverSubscriptionFactor.setMaxAccess(_D)
if mibBuilder.loadTexts:juniDosProtectionDpgPriorityOverSubscriptionFactor.setStatus(_A)
class _JuniDosProtectionDpgPriorityRate_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(64,65535))
_JuniDosProtectionDpgPriorityRate_Type.__name__=_E
_JuniDosProtectionDpgPriorityRate_Object=MibTableColumn
juniDosProtectionDpgPriorityRate=_JuniDosProtectionDpgPriorityRate_Object((1,3,6,1,4,1,4874,2,2,80,1,2,3,1,5),_JuniDosProtectionDpgPriorityRate_Type())
juniDosProtectionDpgPriorityRate.setMaxAccess(_D)
if mibBuilder.loadTexts:juniDosProtectionDpgPriorityRate.setStatus(_A)
_JuniDosProtectionDpgPriorityModified_Type=TruthValue
_JuniDosProtectionDpgPriorityModified_Object=MibTableColumn
juniDosProtectionDpgPriorityModified=_JuniDosProtectionDpgPriorityModified_Object((1,3,6,1,4,1,4874,2,2,80,1,2,3,1,6),_JuniDosProtectionDpgPriorityModified_Type())
juniDosProtectionDpgPriorityModified.setMaxAccess(_C)
if mibBuilder.loadTexts:juniDosProtectionDpgPriorityModified.setStatus(_A)
_JuniDosProtectionDpgAttachTable_Object=MibTable
juniDosProtectionDpgAttachTable=_JuniDosProtectionDpgAttachTable_Object((1,3,6,1,4,1,4874,2,2,80,1,2,4))
if mibBuilder.loadTexts:juniDosProtectionDpgAttachTable.setStatus(_A)
_JuniDosProtectionDpgAttachEntry_Object=MibTableRow
juniDosProtectionDpgAttachEntry=_JuniDosProtectionDpgAttachEntry_Object((1,3,6,1,4,1,4874,2,2,80,1,2,4,1))
juniDosProtectionDpgAttachEntry.setIndexNames((0,_B,_j))
if mibBuilder.loadTexts:juniDosProtectionDpgAttachEntry.setStatus(_A)
_JuniDosProtectionDpgAttachIndex_Type=InterfaceIndex
_JuniDosProtectionDpgAttachIndex_Object=MibTableColumn
juniDosProtectionDpgAttachIndex=_JuniDosProtectionDpgAttachIndex_Object((1,3,6,1,4,1,4874,2,2,80,1,2,4,1,1),_JuniDosProtectionDpgAttachIndex_Type())
juniDosProtectionDpgAttachIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:juniDosProtectionDpgAttachIndex.setStatus(_A)
_JuniDosProtectionDpgAttachRowStatus_Type=RowStatus
_JuniDosProtectionDpgAttachRowStatus_Object=MibTableColumn
juniDosProtectionDpgAttachRowStatus=_JuniDosProtectionDpgAttachRowStatus_Object((1,3,6,1,4,1,4874,2,2,80,1,2,4,1,2),_JuniDosProtectionDpgAttachRowStatus_Type())
juniDosProtectionDpgAttachRowStatus.setMaxAccess(_G)
if mibBuilder.loadTexts:juniDosProtectionDpgAttachRowStatus.setStatus(_A)
class _JuniDosProtectionDpgAttachName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_JuniDosProtectionDpgAttachName_Type.__name__=_H
_JuniDosProtectionDpgAttachName_Object=MibTableColumn
juniDosProtectionDpgAttachName=_JuniDosProtectionDpgAttachName_Object((1,3,6,1,4,1,4874,2,2,80,1,2,4,1,3),_JuniDosProtectionDpgAttachName_Type())
juniDosProtectionDpgAttachName.setMaxAccess(_G)
if mibBuilder.loadTexts:juniDosProtectionDpgAttachName.setStatus(_A)
_JuniDosProtectionDpgAttachConfigured_Type=TruthValue
_JuniDosProtectionDpgAttachConfigured_Object=MibTableColumn
juniDosProtectionDpgAttachConfigured=_JuniDosProtectionDpgAttachConfigured_Object((1,3,6,1,4,1,4874,2,2,80,1,2,4,1,4),_JuniDosProtectionDpgAttachConfigured_Type())
juniDosProtectionDpgAttachConfigured.setMaxAccess(_G)
if mibBuilder.loadTexts:juniDosProtectionDpgAttachConfigured.setStatus(_A)
_JuniDosProtectionDpgProfileTable_Object=MibTable
juniDosProtectionDpgProfileTable=_JuniDosProtectionDpgProfileTable_Object((1,3,6,1,4,1,4874,2,2,80,1,2,5))
if mibBuilder.loadTexts:juniDosProtectionDpgProfileTable.setStatus(_A)
_JuniDosProtectionDpgProfileEntry_Object=MibTableRow
juniDosProtectionDpgProfileEntry=_JuniDosProtectionDpgProfileEntry_Object((1,3,6,1,4,1,4874,2,2,80,1,2,5,1))
juniDosProtectionDpgProfileEntry.setIndexNames((0,_B,_k),(0,_B,_l))
if mibBuilder.loadTexts:juniDosProtectionDpgProfileEntry.setStatus(_A)
_JuniDosProtectionDpgProfileProfileId_Type=Unsigned32
_JuniDosProtectionDpgProfileProfileId_Object=MibTableColumn
juniDosProtectionDpgProfileProfileId=_JuniDosProtectionDpgProfileProfileId_Object((1,3,6,1,4,1,4874,2,2,80,1,2,5,1,1),_JuniDosProtectionDpgProfileProfileId_Type())
juniDosProtectionDpgProfileProfileId.setMaxAccess(_F)
if mibBuilder.loadTexts:juniDosProtectionDpgProfileProfileId.setStatus(_A)
_JuniDosProtectionDpgProfileLayerId_Type=JuniDosProtectionLayerId
_JuniDosProtectionDpgProfileLayerId_Object=MibTableColumn
juniDosProtectionDpgProfileLayerId=_JuniDosProtectionDpgProfileLayerId_Object((1,3,6,1,4,1,4874,2,2,80,1,2,5,1,2),_JuniDosProtectionDpgProfileLayerId_Type())
juniDosProtectionDpgProfileLayerId.setMaxAccess(_F)
if mibBuilder.loadTexts:juniDosProtectionDpgProfileLayerId.setStatus(_A)
_JuniDosProtectionDpgProfileRowStatus_Type=RowStatus
_JuniDosProtectionDpgProfileRowStatus_Object=MibTableColumn
juniDosProtectionDpgProfileRowStatus=_JuniDosProtectionDpgProfileRowStatus_Object((1,3,6,1,4,1,4874,2,2,80,1,2,5,1,3),_JuniDosProtectionDpgProfileRowStatus_Type())
juniDosProtectionDpgProfileRowStatus.setMaxAccess(_G)
if mibBuilder.loadTexts:juniDosProtectionDpgProfileRowStatus.setStatus(_A)
class _JuniDosProtectionDpgProfileName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_JuniDosProtectionDpgProfileName_Type.__name__=_H
_JuniDosProtectionDpgProfileName_Object=MibTableColumn
juniDosProtectionDpgProfileName=_JuniDosProtectionDpgProfileName_Object((1,3,6,1,4,1,4874,2,2,80,1,2,5,1,4),_JuniDosProtectionDpgProfileName_Type())
juniDosProtectionDpgProfileName.setMaxAccess(_G)
if mibBuilder.loadTexts:juniDosProtectionDpgProfileName.setStatus(_A)
_JuniDosProtectionMIBConformance_ObjectIdentity=ObjectIdentity
juniDosProtectionMIBConformance=_JuniDosProtectionMIBConformance_ObjectIdentity((1,3,6,1,4,1,4874,2,2,80,4))
_JuniDosProtectionMIBCompliances_ObjectIdentity=ObjectIdentity
juniDosProtectionMIBCompliances=_JuniDosProtectionMIBCompliances_ObjectIdentity((1,3,6,1,4,1,4874,2,2,80,4,1))
_JuniDosProtectionMIBGroups_ObjectIdentity=ObjectIdentity
juniDosProtectionMIBGroups=_JuniDosProtectionMIBGroups_ObjectIdentity((1,3,6,1,4,1,4874,2,2,80,4,2))
juniDosProtectionGroup=ObjectGroup((1,3,6,1,4,1,4874,2,2,80,4,2,1))
juniDosProtectionGroup.setObjects(*((_B,_K),(_B,_L),(_B,_M),(_B,_N),(_B,_O),(_B,_P),(_B,_Q),(_B,_R),(_B,_S),(_B,_T),(_B,_U),(_B,_V),(_B,_W),(_B,_X),(_B,_Y),(_B,_Z),(_B,_a)))
if mibBuilder.loadTexts:juniDosProtectionGroup.setStatus(_m)
juniDosProtectionGroup2=ObjectGroup((1,3,6,1,4,1,4874,2,2,80,4,2,2))
juniDosProtectionGroup2.setObjects(*((_B,_K),(_B,_L),(_B,_M),(_B,_N),(_B,_O),(_B,_P),(_B,_Q),(_B,_R),(_B,_S),(_B,_T),(_B,_U),(_B,_V),(_B,_W),(_B,_X),(_B,_Y),(_B,_Z),(_B,_a),(_B,_n),(_B,_o),(_B,_p),(_B,_q),(_B,_r),(_B,_s),(_B,_t),(_B,_u),(_B,_v),(_B,_w),(_B,_x),(_B,_y),(_B,_z),(_B,_A0),(_B,_A1),(_B,_A2),(_B,_A3),(_B,_A4),(_B,_A5)))
if mibBuilder.loadTexts:juniDosProtectionGroup2.setStatus(_A)
juniDosProtectionCompliance=ModuleCompliance((1,3,6,1,4,1,4874,2,2,80,4,1,1))
juniDosProtectionCompliance.setObjects((_B,_A6))
if mibBuilder.loadTexts:juniDosProtectionCompliance.setStatus(_m)
juniDosProtectionCompliance2=ModuleCompliance((1,3,6,1,4,1,4874,2,2,80,4,1,2))
juniDosProtectionCompliance2.setObjects((_B,_A7))
if mibBuilder.loadTexts:juniDosProtectionCompliance2.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'JuniDosProtectionProtocolType':JuniDosProtectionProtocolType,'JuniDosProtectionPriorityType':JuniDosProtectionPriorityType,'JuniDosProtectionProtocolState':JuniDosProtectionProtocolState,'JuniDosProtectionScfdsTableOverflowState':JuniDosProtectionScfdsTableOverflowState,'JuniDosProtectionProtocolPriorityType':JuniDosProtectionProtocolPriorityType,_e:JuniDosProtectionProtocolCannedType,'JuniDosProtectionLayerId':JuniDosProtectionLayerId,'JuniDosProtectionControlProcessorDestination':JuniDosProtectionControlProcessorDestination,'juniDosProtectionMIB':juniDosProtectionMIB,'juniDosProtectionObjects':juniDosProtectionObjects,'juniDosProtectionScfdsGroup':juniDosProtectionScfdsGroup,_K:juniDosProtectionScfdsGlobalState,_L:juniDosProtectionScfdsGlobalGrouping,_M:juniDosProtectionScfdsGlobalClearAll,_N:juniDosProtectionScfdsGlobalDiscontinuityTime,_O:juniDosProtectionScfdsGlobalTableOverflowState,_P:juniDosProtectionScfdsGlobalCurrentSuspiciousFlows,_Q:juniDosProtectionScfdsGlobalNumberSuspiciousFlows,_R:juniDosProtectionScfdsGlobalCurrentSuspiciousFlowGroups,_S:juniDosProtectionScfdsGlobalNumberSuspiciousFlowGroups,_T:juniDosProtectionScfdsGlobalCurrentFalseNegativeFlows,_U:juniDosProtectionScfdsGlobalNumberFalseNegativeFlows,_V:juniDosProtectionScfdsGlobalNumberTableOverflows,'juniDosProtectionScfdsProtocolTable':juniDosProtectionScfdsProtocolTable,'juniDosProtectionScfdsProtocolEntry':juniDosProtectionScfdsProtocolEntry,_c:juniDosProtectionScfdsProtocolIndex,_W:juniDosProtectionScfdsProtocolThreshold,_X:juniDosProtectionScfdsProtocolLowThreshold,_Y:juniDosProtectionScfdsProtocolBackoffTime,_Z:juniDosProtectionScfdsProtocolState,_a:juniDosProtectionScfdsProtocolTransitions,'juniDosProtectionDpgGroup':juniDosProtectionDpgGroup,'juniDosProtectionDpgTable':juniDosProtectionDpgTable,'juniDosProtectionDpgEntry':juniDosProtectionDpgEntry,_d:juniDosProtectionDpgIndex,_n:juniDosProtectionDpgRowStatus,_o:juniDosProtectionDpgCanned,_p:juniDosProtectionDpgRevert,_q:juniDosProtectionDpgModified,_r:juniDosProtectionDpgReferences,'juniDosProtectionDpgProtocolTable':juniDosProtectionDpgProtocolTable,'juniDosProtectionDpgProtocolEntry':juniDosProtectionDpgProtocolEntry,_f:juniDosProtectionDpgProtocolName,_g:juniDosProtectionDpgProtocolProtocol,_s:juniDosProtectionDpgProtocolBurst,_t:juniDosProtectionDpgProtocolDropProbability,_u:juniDosProtectionDpgProtocolRate,_v:juniDosProtectionDpgProtocolSkipPriorityRateLimiter,_w:juniDosProtectionDpgProtocolWeight,'juniDosProtectionDpgProtocolPriority':juniDosProtectionDpgProtocolPriority,_x:juniDosProtectionDpgProtocolModified,'juniDosProtectionDpgProtocolDestination':juniDosProtectionDpgProtocolDestination,'juniDosProtectionDpgPriorityTable':juniDosProtectionDpgPriorityTable,'juniDosProtectionDpgPriorityEntry':juniDosProtectionDpgPriorityEntry,_h:juniDosProtectionDpgPriorityName,_i:juniDosProtectionDpgPriorityPriority,_y:juniDosProtectionDpgPriorityBurst,_z:juniDosProtectionDpgPriorityOverSubscriptionFactor,_A0:juniDosProtectionDpgPriorityRate,_A1:juniDosProtectionDpgPriorityModified,'juniDosProtectionDpgAttachTable':juniDosProtectionDpgAttachTable,'juniDosProtectionDpgAttachEntry':juniDosProtectionDpgAttachEntry,_j:juniDosProtectionDpgAttachIndex,_A2:juniDosProtectionDpgAttachRowStatus,_A3:juniDosProtectionDpgAttachName,'juniDosProtectionDpgAttachConfigured':juniDosProtectionDpgAttachConfigured,'juniDosProtectionDpgProfileTable':juniDosProtectionDpgProfileTable,'juniDosProtectionDpgProfileEntry':juniDosProtectionDpgProfileEntry,_k:juniDosProtectionDpgProfileProfileId,_l:juniDosProtectionDpgProfileLayerId,_A4:juniDosProtectionDpgProfileRowStatus,_A5:juniDosProtectionDpgProfileName,'juniDosProtectionMIBConformance':juniDosProtectionMIBConformance,'juniDosProtectionMIBCompliances':juniDosProtectionMIBCompliances,'juniDosProtectionCompliance':juniDosProtectionCompliance,'juniDosProtectionCompliance2':juniDosProtectionCompliance2,'juniDosProtectionMIBGroups':juniDosProtectionMIBGroups,_A6:juniDosProtectionGroup,_A7:juniDosProtectionGroup2})