_At='cienaCesDpSubPortEgressGeneratorMac'
_As='cienaCesDpSubPortEgressReflectorMac'
_Ar='cienaCesDpL2CftProfileL2CftProtocolType'
_Aq='cienaCesDpPfgProfileIndex'
_Ap='cienaCesDpCpuSubInterfaceIndex'
_Ao='cienaCesDpPbtTransitLiIndex'
_An='cienaCesDpAccessFlowLiIndex'
_Am='cienaCesDpQosFlowLiIndex'
_Al='garpBlock'
_Ak='allBridgesBlock'
_Aj='brigeBlock'
_Ai='lacpMarker'
_Ah='vlanBridge'
_Ag='ciscoStpUplinkFast'
_Af='ciscoPvst'
_Ae='ciscoUdld'
_Ad='ciscoPagp'
_Ac='cienaCesDpVirtualSwitchRlanL2CftProtocolType'
_Ab='cienaCesDpVirtualSwitchRlanIfLiIndex'
_Aa='cienaCesDpVirtualSwitchRlanIfLiType'
_AZ='dscpMplsTcToRcos'
_AY='dscpToRcos'
_AX='dot1dToRcosTag2'
_AW='dot1dToRcosTag1'
_AV='000000000000'
_AU='cienaCesDpTrafficClassTermPresentType'
_AT='cienaCesDpTrafficClassElemId'
_AS='cienaCesDpTrafficClassId'
_AR='cienaCesDpTrafficClassType'
_AQ='cienaCesDpTsQSchedulerInstanceIndex'
_AP='cienaCesDpTsQSchedulerInstancePgid'
_AO='cienaCesDpTsQSchedulerTapPointIndex'
_AN='autoAdjustDisabled'
_AM='cienaCesDpTsQGroupInstanceIndex'
_AL='cienaCesDpTsQGroupInstancePgid'
_AK='cienaCesDpTsQGroupProfileQueueIndex'
_AJ='cienaCesDpTsQRCOSQMapYellowCurveId'
_AI='wred-curve-2'
_AH='wred-curve-1'
_AG='cienaCesDpTsQRCOSQMapGreenCurveId'
_AF='cienaCesDpTsQRCOSQMapQueueId'
_AE='cienaCesDpTsQCAProfileWREDCurveId'
_AD='cienaCesDpTsShaperProfileAttachmentLiIndex'
_AC='cienaCesDpTsShaperProfileAttachmentLiType'
_AB='cienaCesDpTsCosMapFcosMapId'
_AA='cienaCesDpTsCosMapRcosMapId'
_A9='cienaCesDpTsCosMapRcosProfileId'
_A8='cienaCesDpTsMeterProfileAttachmentLiIndex'
_A7='cienaCesDpTsMeterProfileAttachmentLiType'
_A6='DpCouplingFlag'
_A5='cienaCesDpTsMeterFloodContainerAttachmentLiIndex'
_A4='cienaCesDpTsMeterFloodContainerAttachmentLiType'
_A3='servicePbt'
_A2='accessFlow'
_A1='transitPbt'
_A0='tunnelDecapPbt'
_z='TruthValue'
_y='cienaCesDpSubPortName'
_x='cienaCesDpL2CftProfileIndex'
_w='mappedDscp'
_v='leave'
_u='fixed'
_t='ignore'
_s='none'
_r='cienaCesDpTsQCAProfileWREDId'
_q='cienaCesDpTsShaperProfileIndex'
_p='cienaCesDpTsMeterProfileIndex'
_o='rateId3'
_n='rateId2'
_m='rateId1'
_l='noLimit'
_k='cienaCesDpTsMeterFloodContainerProfileIndex'
_j='MacAddress'
_i='IpAddress'
_h='cienaCesPortPgIdMappingNotifSlotIndex'
_g='cienaCesPortPgIdMappingNotifShelfIndex'
_f='cienaCesPortPgIdMappingNotifPortNumber'
_e='cienaCesPortPgIdMappingNotifChassisIndex'
_d='cienaCesLogicalPortConfigPortName'
_c='cienaCesDpVirtualSwitchRlanIndex'
_b='DpIngressMeterPolicy'
_a='cienaCesDpSubPortLiIndex'
_Z='cienaCesDpTsQSchedulerProfileId'
_Y='percent'
_X='cienaCesDpTsQGroupProfileId'
_W='accessible-for-notify'
_V='CienaGlobalState'
_U='cienaCesDpVirtualSwitchIndex'
_T='cienaCesDpTsQRCOSQMapId'
_S='Unsigned32'
_R='unknown'
_Q='PrivateForwardGroupPolicy'
_P='kilobytes'
_O='cienaCesDpTsMeterFloodContainerAttachmentInterfaceName'
_N='cienaCesDpTsMeterFloodContainerProfileName'
_M='cienaCesDpTsMeterFloodContainerNotifAttachmentLiIndex'
_L='cienaCesDpTsMeterFloodContainerNotifAttachmentLiType'
_K='cienaCesDpTsMeterFloodContainerNotifProfileIndex'
_J='CIENA-CES-PORT-MIB'
_I='cienaGlobalSeverity'
_H='cienaGlobalMacAddress'
_G='kilobits/sec'
_F='CIENA-GLOBAL-MIB'
_E='not-accessible'
_D='Integer32'
_C='CIENA-CES-DATAPLANE-MIB'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
cienaCesLogicalPortConfigPortName,cienaCesPortPgIdMappingNotifChassisIndex,cienaCesPortPgIdMappingNotifPortNumber,cienaCesPortPgIdMappingNotifShelfIndex,cienaCesPortPgIdMappingNotifSlotIndex=mibBuilder.importSymbols(_J,_d,_e,_f,_g,_h)
cienaGlobalMacAddress,cienaGlobalSeverity=mibBuilder.importSymbols(_F,_H,_I)
cienaCesConfig,cienaCesNotifications=mibBuilder.importSymbols('CIENA-SMI','cienaCesConfig','cienaCesNotifications')
CienaGlobalState,=mibBuilder.importSymbols('CIENA-TC',_V)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,_i,'ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_S,'iso')
DisplayString,MacAddress,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString',_j,'PhysAddress','TextualConvention',_z)
cienaCesDataplaneMIB=ModuleIdentity((1,3,6,1,4,1,1271,2,1,7))
if mibBuilder.loadTexts:cienaCesDataplaneMIB.setRevisions(('2017-06-07 00:00','2017-04-11 00:00','2016-03-06 00:00','2015-11-03 00:00','2015-10-27 00:00','2015-10-10 00:00','2015-09-22 00:00','2015-08-21 00:00','2015-06-25 00:00','2015-05-08 00:00','2014-08-28 00:00','2014-06-03 00:00','2014-04-14 00:00','2014-02-07 00:00','2013-09-13 00:00','2013-09-04 00:00','2013-08-12 00:00','2013-08-07 00:00','2013-08-06 00:00','2013-07-26 00:00','2013-07-25 00:00','2011-01-06 00:00'))
class DpTsAttachType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,99)));namedValues=NamedValues(*(('port',1),('tunnelEncapPbt',2),(_A0,3),('tunnelGroupPbt',4),(_A1,5),('tunnelEncapMpls',6),('tunnelDecapMpls',7),('tunnelGroupMpls',8),('transitMpls',9),('subPort',10),('qosFlow',11),(_A2,12),(_A3,13),('servicePbb',14),('vcMpls',15),('serviceMplsMesh',16),('cpuInterface',17),('cpuSubInterface',18),('ettp',19),('lspEncapMpls',20),('lspDecapMpls',21),('l3Interface',22),('l3Adjacency',23),(_R,99)))
class PrivateForwardGroupPolicy(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*(('talkToA',1),('talkToB',2),('talkToC',3),('talkToAB',4),('talkToAC',5),('talkToBC',6),('talkToABC',7)))
class DpCouplingFlag(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('off',0),('on',1)))
class DpIngressMeterPolicy(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('nonhierarchical',1),('hierarchical',2)))
class DpSchedulingType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('strict',1),('mdrr',2)))
_CienaCesDpMIBObjects_ObjectIdentity=ObjectIdentity
cienaCesDpMIBObjects=_CienaCesDpMIBObjects_ObjectIdentity((1,3,6,1,4,1,1271,2,1,7,1))
_CienaCesDpTsMeterFloodContainerNotifAttrs_ObjectIdentity=ObjectIdentity
cienaCesDpTsMeterFloodContainerNotifAttrs=_CienaCesDpTsMeterFloodContainerNotifAttrs_ObjectIdentity((1,3,6,1,4,1,1271,2,1,7,1,1))
_CienaCesDpTsMeterFloodContainerProfileTable_Object=MibTable
cienaCesDpTsMeterFloodContainerProfileTable=_CienaCesDpTsMeterFloodContainerProfileTable_Object((1,3,6,1,4,1,1271,2,1,7,1,1,1))
if mibBuilder.loadTexts:cienaCesDpTsMeterFloodContainerProfileTable.setStatus(_A)
_CienaCesDpTsMeterFloodContainerProfileEntry_Object=MibTableRow
cienaCesDpTsMeterFloodContainerProfileEntry=_CienaCesDpTsMeterFloodContainerProfileEntry_Object((1,3,6,1,4,1,1271,2,1,7,1,1,1,1))
cienaCesDpTsMeterFloodContainerProfileEntry.setIndexNames((0,_C,_k))
if mibBuilder.loadTexts:cienaCesDpTsMeterFloodContainerProfileEntry.setStatus(_A)
class _CienaCesDpTsMeterFloodContainerProfileIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_CienaCesDpTsMeterFloodContainerProfileIndex_Type.__name__=_D
_CienaCesDpTsMeterFloodContainerProfileIndex_Object=MibTableColumn
cienaCesDpTsMeterFloodContainerProfileIndex=_CienaCesDpTsMeterFloodContainerProfileIndex_Object((1,3,6,1,4,1,1271,2,1,7,1,1,1,1,1),_CienaCesDpTsMeterFloodContainerProfileIndex_Type())
cienaCesDpTsMeterFloodContainerProfileIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:cienaCesDpTsMeterFloodContainerProfileIndex.setStatus(_A)
_CienaCesDpTsMeterFloodContainerProfileName_Type=DisplayString
_CienaCesDpTsMeterFloodContainerProfileName_Object=MibTableColumn
cienaCesDpTsMeterFloodContainerProfileName=_CienaCesDpTsMeterFloodContainerProfileName_Object((1,3,6,1,4,1,1271,2,1,7,1,1,1,1,2),_CienaCesDpTsMeterFloodContainerProfileName_Type())
cienaCesDpTsMeterFloodContainerProfileName.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesDpTsMeterFloodContainerProfileName.setStatus(_A)
class _CienaCesDpTsMeterFloodContainerNotifProfileIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_CienaCesDpTsMeterFloodContainerNotifProfileIndex_Type.__name__=_D
_CienaCesDpTsMeterFloodContainerNotifProfileIndex_Object=MibTableColumn
cienaCesDpTsMeterFloodContainerNotifProfileIndex=_CienaCesDpTsMeterFloodContainerNotifProfileIndex_Object((1,3,6,1,4,1,1271,2,1,7,1,1,1,1,3),_CienaCesDpTsMeterFloodContainerNotifProfileIndex_Type())
cienaCesDpTsMeterFloodContainerNotifProfileIndex.setMaxAccess(_W)
if mibBuilder.loadTexts:cienaCesDpTsMeterFloodContainerNotifProfileIndex.setStatus(_A)
_CienaCesDpTsMeterFloodContainerProfileRate1_Type=Unsigned32
_CienaCesDpTsMeterFloodContainerProfileRate1_Object=MibTableColumn
cienaCesDpTsMeterFloodContainerProfileRate1=_CienaCesDpTsMeterFloodContainerProfileRate1_Object((1,3,6,1,4,1,1271,2,1,7,1,1,1,1,4),_CienaCesDpTsMeterFloodContainerProfileRate1_Type())
cienaCesDpTsMeterFloodContainerProfileRate1.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesDpTsMeterFloodContainerProfileRate1.setStatus(_A)
if mibBuilder.loadTexts:cienaCesDpTsMeterFloodContainerProfileRate1.setUnits(_G)
_CienaCesDpTsMeterFloodContainerProfileRate2_Type=Unsigned32
_CienaCesDpTsMeterFloodContainerProfileRate2_Object=MibTableColumn
cienaCesDpTsMeterFloodContainerProfileRate2=_CienaCesDpTsMeterFloodContainerProfileRate2_Object((1,3,6,1,4,1,1271,2,1,7,1,1,1,1,5),_CienaCesDpTsMeterFloodContainerProfileRate2_Type())
cienaCesDpTsMeterFloodContainerProfileRate2.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesDpTsMeterFloodContainerProfileRate2.setStatus(_A)
if mibBuilder.loadTexts:cienaCesDpTsMeterFloodContainerProfileRate2.setUnits(_G)
_CienaCesDpTsMeterFloodContainerProfileRate3_Type=Unsigned32
_CienaCesDpTsMeterFloodContainerProfileRate3_Object=MibTableColumn
cienaCesDpTsMeterFloodContainerProfileRate3=_CienaCesDpTsMeterFloodContainerProfileRate3_Object((1,3,6,1,4,1,1271,2,1,7,1,1,1,1,6),_CienaCesDpTsMeterFloodContainerProfileRate3_Type())
cienaCesDpTsMeterFloodContainerProfileRate3.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesDpTsMeterFloodContainerProfileRate3.setStatus(_A)
if mibBuilder.loadTexts:cienaCesDpTsMeterFloodContainerProfileRate3.setUnits(_G)
class _CienaCesDpTsMeterFloodContainerProfileUnknownUnicastRateId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_l,1),(_m,2),(_n,3),(_o,4)))
_CienaCesDpTsMeterFloodContainerProfileUnknownUnicastRateId_Type.__name__=_D
_CienaCesDpTsMeterFloodContainerProfileUnknownUnicastRateId_Object=MibTableColumn
cienaCesDpTsMeterFloodContainerProfileUnknownUnicastRateId=_CienaCesDpTsMeterFloodContainerProfileUnknownUnicastRateId_Object((1,3,6,1,4,1,1271,2,1,7,1,1,1,1,7),_CienaCesDpTsMeterFloodContainerProfileUnknownUnicastRateId_Type())
cienaCesDpTsMeterFloodContainerProfileUnknownUnicastRateId.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesDpTsMeterFloodContainerProfileUnknownUnicastRateId.setStatus(_A)
class _CienaCesDpTsMeterFloodContainerProfileL2BroadcastRateId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_l,1),(_m,2),(_n,3),(_o,4)))
_CienaCesDpTsMeterFloodContainerProfileL2BroadcastRateId_Type.__name__=_D
_CienaCesDpTsMeterFloodContainerProfileL2BroadcastRateId_Object=MibTableColumn
cienaCesDpTsMeterFloodContainerProfileL2BroadcastRateId=_CienaCesDpTsMeterFloodContainerProfileL2BroadcastRateId_Object((1,3,6,1,4,1,1271,2,1,7,1,1,1,1,8),_CienaCesDpTsMeterFloodContainerProfileL2BroadcastRateId_Type())
cienaCesDpTsMeterFloodContainerProfileL2BroadcastRateId.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesDpTsMeterFloodContainerProfileL2BroadcastRateId.setStatus(_A)
class _CienaCesDpTsMeterFloodContainerProfileL2UnknownMulticastRateId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_l,1),(_m,2),(_n,3),(_o,4)))
_CienaCesDpTsMeterFloodContainerProfileL2UnknownMulticastRateId_Type.__name__=_D
_CienaCesDpTsMeterFloodContainerProfileL2UnknownMulticastRateId_Object=MibTableColumn
cienaCesDpTsMeterFloodContainerProfileL2UnknownMulticastRateId=_CienaCesDpTsMeterFloodContainerProfileL2UnknownMulticastRateId_Object((1,3,6,1,4,1,1271,2,1,7,1,1,1,1,9),_CienaCesDpTsMeterFloodContainerProfileL2UnknownMulticastRateId_Type())
cienaCesDpTsMeterFloodContainerProfileL2UnknownMulticastRateId.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesDpTsMeterFloodContainerProfileL2UnknownMulticastRateId.setStatus(_A)
_CienaCesDpTsMeterFloodContainerAttachmentTable_Object=MibTable
cienaCesDpTsMeterFloodContainerAttachmentTable=_CienaCesDpTsMeterFloodContainerAttachmentTable_Object((1,3,6,1,4,1,1271,2,1,7,1,1,2))
if mibBuilder.loadTexts:cienaCesDpTsMeterFloodContainerAttachmentTable.setStatus(_A)
_CienaCesDpTsMeterFloodContainerAttachmentEntry_Object=MibTableRow
cienaCesDpTsMeterFloodContainerAttachmentEntry=_CienaCesDpTsMeterFloodContainerAttachmentEntry_Object((1,3,6,1,4,1,1271,2,1,7,1,1,2,1))
cienaCesDpTsMeterFloodContainerAttachmentEntry.setIndexNames((0,_C,_k),(0,_C,_A4),(0,_C,_A5))
if mibBuilder.loadTexts:cienaCesDpTsMeterFloodContainerAttachmentEntry.setStatus(_A)
_CienaCesDpTsMeterFloodContainerAttachmentLiType_Type=DpTsAttachType
_CienaCesDpTsMeterFloodContainerAttachmentLiType_Object=MibTableColumn
cienaCesDpTsMeterFloodContainerAttachmentLiType=_CienaCesDpTsMeterFloodContainerAttachmentLiType_Object((1,3,6,1,4,1,1271,2,1,7,1,1,2,1,1),_CienaCesDpTsMeterFloodContainerAttachmentLiType_Type())
cienaCesDpTsMeterFloodContainerAttachmentLiType.setMaxAccess(_E)
if mibBuilder.loadTexts:cienaCesDpTsMeterFloodContainerAttachmentLiType.setStatus(_A)
class _CienaCesDpTsMeterFloodContainerAttachmentLiIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,16777215))
_CienaCesDpTsMeterFloodContainerAttachmentLiIndex_Type.__name__=_D
_CienaCesDpTsMeterFloodContainerAttachmentLiIndex_Object=MibTableColumn
cienaCesDpTsMeterFloodContainerAttachmentLiIndex=_CienaCesDpTsMeterFloodContainerAttachmentLiIndex_Object((1,3,6,1,4,1,1271,2,1,7,1,1,2,1,2),_CienaCesDpTsMeterFloodContainerAttachmentLiIndex_Type())
cienaCesDpTsMeterFloodContainerAttachmentLiIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:cienaCesDpTsMeterFloodContainerAttachmentLiIndex.setStatus(_A)
_CienaCesDpTsMeterFloodContainerAttachmentInterfaceName_Type=DisplayString
_CienaCesDpTsMeterFloodContainerAttachmentInterfaceName_Object=MibTableColumn
cienaCesDpTsMeterFloodContainerAttachmentInterfaceName=_CienaCesDpTsMeterFloodContainerAttachmentInterfaceName_Object((1,3,6,1,4,1,1271,2,1,7,1,1,2,1,3),_CienaCesDpTsMeterFloodContainerAttachmentInterfaceName_Type())
cienaCesDpTsMeterFloodContainerAttachmentInterfaceName.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesDpTsMeterFloodContainerAttachmentInterfaceName.setStatus(_A)
_CienaCesDpTsMeterFloodContainerNotifAttachmentLiType_Type=DpTsAttachType
_CienaCesDpTsMeterFloodContainerNotifAttachmentLiType_Object=MibTableColumn
cienaCesDpTsMeterFloodContainerNotifAttachmentLiType=_CienaCesDpTsMeterFloodContainerNotifAttachmentLiType_Object((1,3,6,1,4,1,1271,2,1,7,1,1,2,1,4),_CienaCesDpTsMeterFloodContainerNotifAttachmentLiType_Type())
cienaCesDpTsMeterFloodContainerNotifAttachmentLiType.setMaxAccess(_W)
if mibBuilder.loadTexts:cienaCesDpTsMeterFloodContainerNotifAttachmentLiType.setStatus(_A)
_CienaCesDpTsMeterFloodContainerNotifAttachmentLiIndex_Type=Integer32
_CienaCesDpTsMeterFloodContainerNotifAttachmentLiIndex_Object=MibTableColumn
cienaCesDpTsMeterFloodContainerNotifAttachmentLiIndex=_CienaCesDpTsMeterFloodContainerNotifAttachmentLiIndex_Object((1,3,6,1,4,1,1271,2,1,7,1,1,2,1,5),_CienaCesDpTsMeterFloodContainerNotifAttachmentLiIndex_Type())
cienaCesDpTsMeterFloodContainerNotifAttachmentLiIndex.setMaxAccess(_W)
if mibBuilder.loadTexts:cienaCesDpTsMeterFloodContainerNotifAttachmentLiIndex.setStatus(_A)
_CienaCesDpTsMeterFloodContainerAttachmentUcastRateState_Type=CienaGlobalState
_CienaCesDpTsMeterFloodContainerAttachmentUcastRateState_Object=MibTableColumn
cienaCesDpTsMeterFloodContainerAttachmentUcastRateState=_CienaCesDpTsMeterFloodContainerAttachmentUcastRateState_Object((1,3,6,1,4,1,1271,2,1,7,1,1,2,1,6),_CienaCesDpTsMeterFloodContainerAttachmentUcastRateState_Type())
cienaCesDpTsMeterFloodContainerAttachmentUcastRateState.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesDpTsMeterFloodContainerAttachmentUcastRateState.setStatus(_A)
_CienaCesDpTsMeterFloodContainerAttachmentL2BcastRateState_Type=CienaGlobalState
_CienaCesDpTsMeterFloodContainerAttachmentL2BcastRateState_Object=MibTableColumn
cienaCesDpTsMeterFloodContainerAttachmentL2BcastRateState=_CienaCesDpTsMeterFloodContainerAttachmentL2BcastRateState_Object((1,3,6,1,4,1,1271,2,1,7,1,1,2,1,7),_CienaCesDpTsMeterFloodContainerAttachmentL2BcastRateState_Type())
cienaCesDpTsMeterFloodContainerAttachmentL2BcastRateState.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesDpTsMeterFloodContainerAttachmentL2BcastRateState.setStatus(_A)
_CienaCesDpTsMeterFloodContainerAttachmentL2McastRateState_Type=CienaGlobalState
_CienaCesDpTsMeterFloodContainerAttachmentL2McastRateState_Object=MibTableColumn
cienaCesDpTsMeterFloodContainerAttachmentL2McastRateState=_CienaCesDpTsMeterFloodContainerAttachmentL2McastRateState_Object((1,3,6,1,4,1,1271,2,1,7,1,1,2,1,8),_CienaCesDpTsMeterFloodContainerAttachmentL2McastRateState_Type())
cienaCesDpTsMeterFloodContainerAttachmentL2McastRateState.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesDpTsMeterFloodContainerAttachmentL2McastRateState.setStatus(_A)
_CienaCesDpTsMeterFloodContainerAttachmentTotalBandwidth_Type=Unsigned32
_CienaCesDpTsMeterFloodContainerAttachmentTotalBandwidth_Object=MibTableColumn
cienaCesDpTsMeterFloodContainerAttachmentTotalBandwidth=_CienaCesDpTsMeterFloodContainerAttachmentTotalBandwidth_Object((1,3,6,1,4,1,1271,2,1,7,1,1,2,1,9),_CienaCesDpTsMeterFloodContainerAttachmentTotalBandwidth_Type())
cienaCesDpTsMeterFloodContainerAttachmentTotalBandwidth.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesDpTsMeterFloodContainerAttachmentTotalBandwidth.setStatus(_A)
_CienaCesDpTsMeterFloodContainerAttachmentUsedBandwidth_Type=Unsigned32
_CienaCesDpTsMeterFloodContainerAttachmentUsedBandwidth_Object=MibTableColumn
cienaCesDpTsMeterFloodContainerAttachmentUsedBandwidth=_CienaCesDpTsMeterFloodContainerAttachmentUsedBandwidth_Object((1,3,6,1,4,1,1271,2,1,7,1,1,2,1,10),_CienaCesDpTsMeterFloodContainerAttachmentUsedBandwidth_Type())
cienaCesDpTsMeterFloodContainerAttachmentUsedBandwidth.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesDpTsMeterFloodContainerAttachmentUsedBandwidth.setStatus(_A)
_CienaCesDpTsMeterFloodContainerAttachmentTotalRateState_Type=CienaGlobalState
_CienaCesDpTsMeterFloodContainerAttachmentTotalRateState_Object=MibTableColumn
cienaCesDpTsMeterFloodContainerAttachmentTotalRateState=_CienaCesDpTsMeterFloodContainerAttachmentTotalRateState_Object((1,3,6,1,4,1,1271,2,1,7,1,1,2,1,11),_CienaCesDpTsMeterFloodContainerAttachmentTotalRateState_Type())
cienaCesDpTsMeterFloodContainerAttachmentTotalRateState.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesDpTsMeterFloodContainerAttachmentTotalRateState.setStatus(_A)
_CienaCesDpTsMeter_ObjectIdentity=ObjectIdentity
cienaCesDpTsMeter=_CienaCesDpTsMeter_ObjectIdentity((1,3,6,1,4,1,1271,2,1,7,1,2))
_CienaCesDpTsMeterProfile_ObjectIdentity=ObjectIdentity
cienaCesDpTsMeterProfile=_CienaCesDpTsMeterProfile_ObjectIdentity((1,3,6,1,4,1,1271,2,1,7,1,2,1))
_CienaCesDpTsMeterProfileTable_Object=MibTable
cienaCesDpTsMeterProfileTable=_CienaCesDpTsMeterProfileTable_Object((1,3,6,1,4,1,1271,2,1,7,1,2,1,1))
if mibBuilder.loadTexts:cienaCesDpTsMeterProfileTable.setStatus(_A)
_CienaCesDpTsMeterProfileEntry_Object=MibTableRow
cienaCesDpTsMeterProfileEntry=_CienaCesDpTsMeterProfileEntry_Object((1,3,6,1,4,1,1271,2,1,7,1,2,1,1,1))
cienaCesDpTsMeterProfileEntry.setIndexNames((0,_C,_p))
if mibBuilder.loadTexts:cienaCesDpTsMeterProfileEntry.setStatus(_A)
class _CienaCesDpTsMeterProfileIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_CienaCesDpTsMeterProfileIndex_Type.__name__=_D
_CienaCesDpTsMeterProfileIndex_Object=MibTableColumn
cienaCesDpTsMeterProfileIndex=_CienaCesDpTsMeterProfileIndex_Object((1,3,6,1,4,1,1271,2,1,7,1,2,1,1,1,1),_CienaCesDpTsMeterProfileIndex_Type())
cienaCesDpTsMeterProfileIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:cienaCesDpTsMeterProfileIndex.setStatus(_A)
_CienaCesDpTsMeterProfileName_Type=DisplayString
_CienaCesDpTsMeterProfileName_Object=MibTableColumn
cienaCesDpTsMeterProfileName=_CienaCesDpTsMeterProfileName_Object((1,3,6,1,4,1,1271,2,1,7,1,2,1,1,1,2),_CienaCesDpTsMeterProfileName_Type())
cienaCesDpTsMeterProfileName.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesDpTsMeterProfileName.setStatus(_A)
_CienaCesDpTsMeterProfileCIR_Type=Unsigned32
_CienaCesDpTsMeterProfileCIR_Object=MibTableColumn
cienaCesDpTsMeterProfileCIR=_CienaCesDpTsMeterProfileCIR_Object((1,3,6,1,4,1,1271,2,1,7,1,2,1,1,1,3),_CienaCesDpTsMeterProfileCIR_Type())
cienaCesDpTsMeterProfileCIR.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesDpTsMeterProfileCIR.setStatus(_A)
if mibBuilder.loadTexts:cienaCesDpTsMeterProfileCIR.setUnits(_G)
_CienaCesDpTsMeterProfileCBS_Type=Unsigned32
_CienaCesDpTsMeterProfileCBS_Object=MibTableColumn
cienaCesDpTsMeterProfileCBS=_CienaCesDpTsMeterProfileCBS_Object((1,3,6,1,4,1,1271,2,1,7,1,2,1,1,1,4),_CienaCesDpTsMeterProfileCBS_Type())
cienaCesDpTsMeterProfileCBS.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesDpTsMeterProfileCBS.setStatus(_A)
if mibBuilder.loadTexts:cienaCesDpTsMeterProfileCBS.setUnits(_P)
_CienaCesDpTsMeterProfileEIR_Type=Unsigned32
_CienaCesDpTsMeterProfileEIR_Object=MibTableColumn
cienaCesDpTsMeterProfileEIR=_CienaCesDpTsMeterProfileEIR_Object((1,3,6,1,4,1,1271,2,1,7,1,2,1,1,1,5),_CienaCesDpTsMeterProfileEIR_Type())
cienaCesDpTsMeterProfileEIR.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesDpTsMeterProfileEIR.setStatus(_A)
if mibBuilder.loadTexts:cienaCesDpTsMeterProfileEIR.setUnits(_G)
_CienaCesDpTsMeterProfileEBS_Type=Unsigned32
_CienaCesDpTsMeterProfileEBS_Object=MibTableColumn
cienaCesDpTsMeterProfileEBS=_CienaCesDpTsMeterProfileEBS_Object((1,3,6,1,4,1,1271,2,1,7,1,2,1,1,1,6),_CienaCesDpTsMeterProfileEBS_Type())
cienaCesDpTsMeterProfileEBS.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesDpTsMeterProfileEBS.setStatus(_A)
if mibBuilder.loadTexts:cienaCesDpTsMeterProfileEBS.setUnits(_P)
class _CienaCesDpTsMeterProfileColorMode_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('color-mode-none',0),('color-blind',1),('color-aware',2)))
_CienaCesDpTsMeterProfileColorMode_Type.__name__=_D
_CienaCesDpTsMeterProfileColorMode_Object=MibTableColumn
cienaCesDpTsMeterProfileColorMode=_CienaCesDpTsMeterProfileColorMode_Object((1,3,6,1,4,1,1271,2,1,7,1,2,1,1,1,7),_CienaCesDpTsMeterProfileColorMode_Type())
cienaCesDpTsMeterProfileColorMode.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesDpTsMeterProfileColorMode.setStatus(_A)
class _CienaCesDpTsMeterProfileCouplingFlag_Type(DpCouplingFlag):defaultValue=0
_CienaCesDpTsMeterProfileCouplingFlag_Type.__name__=_A6
_CienaCesDpTsMeterProfileCouplingFlag_Object=MibTableColumn
cienaCesDpTsMeterProfileCouplingFlag=_CienaCesDpTsMeterProfileCouplingFlag_Object((1,3,6,1,4,1,1271,2,1,7,1,2,1,1,1,8),_CienaCesDpTsMeterProfileCouplingFlag_Type())
cienaCesDpTsMeterProfileCouplingFlag.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesDpTsMeterProfileCouplingFlag.setStatus(_A)
_CienaCesDpTsMeterProfileAttachmentTable_Object=MibTable
cienaCesDpTsMeterProfileAttachmentTable=_CienaCesDpTsMeterProfileAttachmentTable_Object((1,3,6,1,4,1,1271,2,1,7,1,2,1,2))
if mibBuilder.loadTexts:cienaCesDpTsMeterProfileAttachmentTable.setStatus(_A)
_CienaCesDpTsMeterProfileAttachmentEntry_Object=MibTableRow
cienaCesDpTsMeterProfileAttachmentEntry=_CienaCesDpTsMeterProfileAttachmentEntry_Object((1,3,6,1,4,1,1271,2,1,7,1,2,1,2,1))
cienaCesDpTsMeterProfileAttachmentEntry.setIndexNames((0,_C,_p),(0,_C,_A7),(0,_C,_A8))
if mibBuilder.loadTexts:cienaCesDpTsMeterProfileAttachmentEntry.setStatus(_A)
_CienaCesDpTsMeterProfileAttachmentLiType_Type=DpTsAttachType
_CienaCesDpTsMeterProfileAttachmentLiType_Object=MibTableColumn
cienaCesDpTsMeterProfileAttachmentLiType=_CienaCesDpTsMeterProfileAttachmentLiType_Object((1,3,6,1,4,1,1271,2,1,7,1,2,1,2,1,1),_CienaCesDpTsMeterProfileAttachmentLiType_Type())
cienaCesDpTsMeterProfileAttachmentLiType.setMaxAccess(_E)
if mibBuilder.loadTexts:cienaCesDpTsMeterProfileAttachmentLiType.setStatus(_A)
class _CienaCesDpTsMeterProfileAttachmentLiIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,16777215))
_CienaCesDpTsMeterProfileAttachmentLiIndex_Type.__name__=_D
_CienaCesDpTsMeterProfileAttachmentLiIndex_Object=MibTableColumn
cienaCesDpTsMeterProfileAttachmentLiIndex=_CienaCesDpTsMeterProfileAttachmentLiIndex_Object((1,3,6,1,4,1,1271,2,1,7,1,2,1,2,1,2),_CienaCesDpTsMeterProfileAttachmentLiIndex_Type())
cienaCesDpTsMeterProfileAttachmentLiIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:cienaCesDpTsMeterProfileAttachmentLiIndex.setStatus(_A)
_CienaCesDpTsMeterProfileAttachmentTotalCIR_Type=Unsigned32
_CienaCesDpTsMeterProfileAttachmentTotalCIR_Object=MibTableColumn
cienaCesDpTsMeterProfileAttachmentTotalCIR=_CienaCesDpTsMeterProfileAttachmentTotalCIR_Object((1,3,6,1,4,1,1271,2,1,7,1,2,1,2,1,3),_CienaCesDpTsMeterProfileAttachmentTotalCIR_Type())
cienaCesDpTsMeterProfileAttachmentTotalCIR.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesDpTsMeterProfileAttachmentTotalCIR.setStatus(_A)
if mibBuilder.loadTexts:cienaCesDpTsMeterProfileAttachmentTotalCIR.setUnits(_G)
_CienaCesDpTsMeterProfileAttachmentTotalEIR_Type=Unsigned32
_CienaCesDpTsMeterProfileAttachmentTotalEIR_Object=MibTableColumn
cienaCesDpTsMeterProfileAttachmentTotalEIR=_CienaCesDpTsMeterProfileAttachmentTotalEIR_Object((1,3,6,1,4,1,1271,2,1,7,1,2,1,2,1,4),_CienaCesDpTsMeterProfileAttachmentTotalEIR_Type())
cienaCesDpTsMeterProfileAttachmentTotalEIR.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesDpTsMeterProfileAttachmentTotalEIR.setStatus(_A)
if mibBuilder.loadTexts:cienaCesDpTsMeterProfileAttachmentTotalEIR.setUnits(_G)
_CienaCesDpTsMeterProfileAttachmentUsedCIR_Type=Unsigned32
_CienaCesDpTsMeterProfileAttachmentUsedCIR_Object=MibTableColumn
cienaCesDpTsMeterProfileAttachmentUsedCIR=_CienaCesDpTsMeterProfileAttachmentUsedCIR_Object((1,3,6,1,4,1,1271,2,1,7,1,2,1,2,1,5),_CienaCesDpTsMeterProfileAttachmentUsedCIR_Type())
cienaCesDpTsMeterProfileAttachmentUsedCIR.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesDpTsMeterProfileAttachmentUsedCIR.setStatus(_A)
if mibBuilder.loadTexts:cienaCesDpTsMeterProfileAttachmentUsedCIR.setUnits(_G)
_CienaCesDpTsMeterProfileAttachmentMaxUsedEIR_Type=Unsigned32
_CienaCesDpTsMeterProfileAttachmentMaxUsedEIR_Object=MibTableColumn
cienaCesDpTsMeterProfileAttachmentMaxUsedEIR=_CienaCesDpTsMeterProfileAttachmentMaxUsedEIR_Object((1,3,6,1,4,1,1271,2,1,7,1,2,1,2,1,6),_CienaCesDpTsMeterProfileAttachmentMaxUsedEIR_Type())
cienaCesDpTsMeterProfileAttachmentMaxUsedEIR.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesDpTsMeterProfileAttachmentMaxUsedEIR.setStatus(_A)
if mibBuilder.loadTexts:cienaCesDpTsMeterProfileAttachmentMaxUsedEIR.setUnits(_G)
_CienaCesDpTsCosMap_ObjectIdentity=ObjectIdentity
cienaCesDpTsCosMap=_CienaCesDpTsCosMap_ObjectIdentity((1,3,6,1,4,1,1271,2,1,7,1,3))
_CienaCesDpTsCosMapRcos_ObjectIdentity=ObjectIdentity
cienaCesDpTsCosMapRcos=_CienaCesDpTsCosMapRcos_ObjectIdentity((1,3,6,1,4,1,1271,2,1,7,1,3,1))
_CienaCesDpTsCosMapRcosProfileTable_Object=MibTable
cienaCesDpTsCosMapRcosProfileTable=_CienaCesDpTsCosMapRcosProfileTable_Object((1,3,6,1,4,1,1271,2,1,7,1,3,1,1))
if mibBuilder.loadTexts:cienaCesDpTsCosMapRcosProfileTable.setStatus(_A)
_CienaCesDpTsCosMapRcosProfileEntry_Object=MibTableRow
cienaCesDpTsCosMapRcosProfileEntry=_CienaCesDpTsCosMapRcosProfileEntry_Object((1,3,6,1,4,1,1271,2,1,7,1,3,1,1,1))
cienaCesDpTsCosMapRcosProfileEntry.setIndexNames((0,_C,_A9))
if mibBuilder.loadTexts:cienaCesDpTsCosMapRcosProfileEntry.setStatus(_A)
class _CienaCesDpTsCosMapRcosProfileId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_CienaCesDpTsCosMapRcosProfileId_Type.__name__=_D
_CienaCesDpTsCosMapRcosProfileId_Object=MibTableColumn
cienaCesDpTsCosMapRcosProfileId=_CienaCesDpTsCosMapRcosProfileId_Object((1,3,6,1,4,1,1271,2,1,7,1,3,1,1,1,1),_CienaCesDpTsCosMapRcosProfileId_Type())
cienaCesDpTsCosMapRcosProfileId.setMaxAccess(_E)
if mibBuilder.loadTexts:cienaCesDpTsCosMapRcosProfileId.setStatus(_A)
_CienaCesDpTsCosMapRcosProfileName_Type=DisplayString
_CienaCesDpTsCosMapRcosProfileName_Object=MibTableColumn
cienaCesDpTsCosMapRcosProfileName=_CienaCesDpTsCosMapRcosProfileName_Object((1,3,6,1,4,1,1271,2,1,7,1,3,1,1,1,2),_CienaCesDpTsCosMapRcosProfileName_Type())
cienaCesDpTsCosMapRcosProfileName.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesDpTsCosMapRcosProfileName.setStatus(_A)
_CienaCesDpTsCosMapRcosFixedRCoSValue_Type=Integer32
_CienaCesDpTsCosMapRcosFixedRCoSValue_Object=MibTableColumn
cienaCesDpTsCosMapRcosFixedRCoSValue=_CienaCesDpTsCosMapRcosFixedRCoSValue_Object((1,3,6,1,4,1,1271,2,1,7,1,3,1,1,1,3),_CienaCesDpTsCosMapRcosFixedRCoSValue_Type())
cienaCesDpTsCosMapRcosFixedRCoSValue.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesDpTsCosMapRcosFixedRCoSValue.setStatus(_A)
class _CienaCesDpTsCosMapRcosFixedRcolour_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('green',1),('yellow',2)))
_CienaCesDpTsCosMapRcosFixedRcolour_Type.__name__=_D
_CienaCesDpTsCosMapRcosFixedRcolour_Object=MibTableColumn
cienaCesDpTsCosMapRcosFixedRcolour=_CienaCesDpTsCosMapRcosFixedRcolour_Object((1,3,6,1,4,1,1271,2,1,7,1,3,1,1,1,4),_CienaCesDpTsCosMapRcosFixedRcolour_Type())
cienaCesDpTsCosMapRcosFixedRcolour.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesDpTsCosMapRcosFixedRcolour.setStatus(_A)
class _CienaCesDpTsCosMapRcosCosMapId_Type(Integer32):defaultValue=0
_CienaCesDpTsCosMapRcosCosMapId_Type.__name__=_D
_CienaCesDpTsCosMapRcosCosMapId_Object=MibTableColumn
cienaCesDpTsCosMapRcosCosMapId=_CienaCesDpTsCosMapRcosCosMapId_Object((1,3,6,1,4,1,1271,2,1,7,1,3,1,1,1,5),_CienaCesDpTsCosMapRcosCosMapId_Type())
cienaCesDpTsCosMapRcosCosMapId.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesDpTsCosMapRcosCosMapId.setStatus(_A)
_CienaCesDpTsCosMapRcosCosMapName_Type=OctetString
_CienaCesDpTsCosMapRcosCosMapName_Object=MibTableColumn
cienaCesDpTsCosMapRcosCosMapName=_CienaCesDpTsCosMapRcosCosMapName_Object((1,3,6,1,4,1,1271,2,1,7,1,3,1,1,1,6),_CienaCesDpTsCosMapRcosCosMapName_Type())
cienaCesDpTsCosMapRcosCosMapName.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesDpTsCosMapRcosCosMapName.setStatus(_A)
_CienaCesDpTsCosMapRcosMapTable_Object=MibTable
cienaCesDpTsCosMapRcosMapTable=_CienaCesDpTsCosMapRcosMapTable_Object((1,3,6,1,4,1,1271,2,1,7,1,3,1,2))
if mibBuilder.loadTexts:cienaCesDpTsCosMapRcosMapTable.setStatus(_A)
_CienaCesDpTsCosMapRcosMapEntry_Object=MibTableRow
cienaCesDpTsCosMapRcosMapEntry=_CienaCesDpTsCosMapRcosMapEntry_Object((1,3,6,1,4,1,1271,2,1,7,1,3,1,2,1))
cienaCesDpTsCosMapRcosMapEntry.setIndexNames((0,_C,_AA))
if mibBuilder.loadTexts:cienaCesDpTsCosMapRcosMapEntry.setStatus(_A)
class _CienaCesDpTsCosMapRcosMapId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_CienaCesDpTsCosMapRcosMapId_Type.__name__=_D
_CienaCesDpTsCosMapRcosMapId_Object=MibTableColumn
cienaCesDpTsCosMapRcosMapId=_CienaCesDpTsCosMapRcosMapId_Object((1,3,6,1,4,1,1271,2,1,7,1,3,1,2,1,1),_CienaCesDpTsCosMapRcosMapId_Type())
cienaCesDpTsCosMapRcosMapId.setMaxAccess(_E)
if mibBuilder.loadTexts:cienaCesDpTsCosMapRcosMapId.setStatus(_A)
_CienaCesDpTsCosMapRcosMapName_Type=DisplayString
_CienaCesDpTsCosMapRcosMapName_Object=MibTableColumn
cienaCesDpTsCosMapRcosMapName=_CienaCesDpTsCosMapRcosMapName_Object((1,3,6,1,4,1,1271,2,1,7,1,3,1,2,1,2),_CienaCesDpTsCosMapRcosMapName_Type())
cienaCesDpTsCosMapRcosMapName.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesDpTsCosMapRcosMapName.setStatus(_A)
_CienaCesDpTsCosMapRcosMapL2RCoS_Type=OctetString
_CienaCesDpTsCosMapRcosMapL2RCoS_Object=MibTableColumn
cienaCesDpTsCosMapRcosMapL2RCoS=_CienaCesDpTsCosMapRcosMapL2RCoS_Object((1,3,6,1,4,1,1271,2,1,7,1,3,1,2,1,3),_CienaCesDpTsCosMapRcosMapL2RCoS_Type())
cienaCesDpTsCosMapRcosMapL2RCoS.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesDpTsCosMapRcosMapL2RCoS.setStatus(_A)
_CienaCesDpTsCosMapRcosMapL2RColour_Type=OctetString
_CienaCesDpTsCosMapRcosMapL2RColour_Object=MibTableColumn
cienaCesDpTsCosMapRcosMapL2RColour=_CienaCesDpTsCosMapRcosMapL2RColour_Object((1,3,6,1,4,1,1271,2,1,7,1,3,1,2,1,4),_CienaCesDpTsCosMapRcosMapL2RColour_Type())
cienaCesDpTsCosMapRcosMapL2RColour.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesDpTsCosMapRcosMapL2RColour.setStatus(_A)
_CienaCesDpTsCosMapRcosMapL3DscpRCoS_Type=OctetString
_CienaCesDpTsCosMapRcosMapL3DscpRCoS_Object=MibTableColumn
cienaCesDpTsCosMapRcosMapL3DscpRCoS=_CienaCesDpTsCosMapRcosMapL3DscpRCoS_Object((1,3,6,1,4,1,1271,2,1,7,1,3,1,2,1,5),_CienaCesDpTsCosMapRcosMapL3DscpRCoS_Type())
cienaCesDpTsCosMapRcosMapL3DscpRCoS.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesDpTsCosMapRcosMapL3DscpRCoS.setStatus(_A)
_CienaCesDpTsCosMapRcosMapL3DscpRColour_Type=OctetString
_CienaCesDpTsCosMapRcosMapL3DscpRColour_Object=MibTableColumn
cienaCesDpTsCosMapRcosMapL3DscpRColour=_CienaCesDpTsCosMapRcosMapL3DscpRColour_Object((1,3,6,1,4,1,1271,2,1,7,1,3,1,2,1,6),_CienaCesDpTsCosMapRcosMapL3DscpRColour_Type())
cienaCesDpTsCosMapRcosMapL3DscpRColour.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesDpTsCosMapRcosMapL3DscpRColour.setStatus(_A)
_CienaCesDpTsCosMapRcosMapExpRCoS_Type=OctetString
_CienaCesDpTsCosMapRcosMapExpRCoS_Object=MibTableColumn
cienaCesDpTsCosMapRcosMapExpRCoS=_CienaCesDpTsCosMapRcosMapExpRCoS_Object((1,3,6,1,4,1,1271,2,1,7,1,3,1,2,1,7),_CienaCesDpTsCosMapRcosMapExpRCoS_Type())
cienaCesDpTsCosMapRcosMapExpRCoS.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesDpTsCosMapRcosMapExpRCoS.setStatus(_A)
_CienaCesDpTsCosMapRcosMapExpRColour_Type=OctetString
_CienaCesDpTsCosMapRcosMapExpRColour_Object=MibTableColumn
cienaCesDpTsCosMapRcosMapExpRColour=_CienaCesDpTsCosMapRcosMapExpRColour_Object((1,3,6,1,4,1,1271,2,1,7,1,3,1,2,1,8),_CienaCesDpTsCosMapRcosMapExpRColour_Type())
cienaCesDpTsCosMapRcosMapExpRColour.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesDpTsCosMapRcosMapExpRColour.setStatus(_A)
_CienaCesDpTsCosMapFcos_ObjectIdentity=ObjectIdentity
cienaCesDpTsCosMapFcos=_CienaCesDpTsCosMapFcos_ObjectIdentity((1,3,6,1,4,1,1271,2,1,7,1,3,2))
_CienaCesDpTsCosMapFcosMapTable_Object=MibTable
cienaCesDpTsCosMapFcosMapTable=_CienaCesDpTsCosMapFcosMapTable_Object((1,3,6,1,4,1,1271,2,1,7,1,3,2,1))
if mibBuilder.loadTexts:cienaCesDpTsCosMapFcosMapTable.setStatus(_A)
_CienaCesDpTsCosMapFcosMapEntry_Object=MibTableRow
cienaCesDpTsCosMapFcosMapEntry=_CienaCesDpTsCosMapFcosMapEntry_Object((1,3,6,1,4,1,1271,2,1,7,1,3,2,1,1))
cienaCesDpTsCosMapFcosMapEntry.setIndexNames((0,_C,_AB))
if mibBuilder.loadTexts:cienaCesDpTsCosMapFcosMapEntry.setStatus(_A)
class _CienaCesDpTsCosMapFcosMapId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_CienaCesDpTsCosMapFcosMapId_Type.__name__=_D
_CienaCesDpTsCosMapFcosMapId_Object=MibTableColumn
cienaCesDpTsCosMapFcosMapId=_CienaCesDpTsCosMapFcosMapId_Object((1,3,6,1,4,1,1271,2,1,7,1,3,2,1,1,1),_CienaCesDpTsCosMapFcosMapId_Type())
cienaCesDpTsCosMapFcosMapId.setMaxAccess(_E)
if mibBuilder.loadTexts:cienaCesDpTsCosMapFcosMapId.setStatus(_A)
_CienaCesDpTsCosMapFcosMapName_Type=DisplayString
_CienaCesDpTsCosMapFcosMapName_Object=MibTableColumn
cienaCesDpTsCosMapFcosMapName=_CienaCesDpTsCosMapFcosMapName_Object((1,3,6,1,4,1,1271,2,1,7,1,3,2,1,1,2),_CienaCesDpTsCosMapFcosMapName_Type())
cienaCesDpTsCosMapFcosMapName.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesDpTsCosMapFcosMapName.setStatus(_A)
_CienaCesDpTsCosMapFcosL2CoS_Type=OctetString
_CienaCesDpTsCosMapFcosL2CoS_Object=MibTableColumn
cienaCesDpTsCosMapFcosL2CoS=_CienaCesDpTsCosMapFcosL2CoS_Object((1,3,6,1,4,1,1271,2,1,7,1,3,2,1,1,3),_CienaCesDpTsCosMapFcosL2CoS_Type())
cienaCesDpTsCosMapFcosL2CoS.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesDpTsCosMapFcosL2CoS.setStatus(_A)
_CienaCesDpTsCosMapFcosL2Dei_Type=OctetString
_CienaCesDpTsCosMapFcosL2Dei_Object=MibTableColumn
cienaCesDpTsCosMapFcosL2Dei=_CienaCesDpTsCosMapFcosL2Dei_Object((1,3,6,1,4,1,1271,2,1,7,1,3,2,1,1,4),_CienaCesDpTsCosMapFcosL2Dei_Type())
cienaCesDpTsCosMapFcosL2Dei.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesDpTsCosMapFcosL2Dei.setStatus(_A)
_CienaCesDpTsCosMapFcosL3Dscp_Type=OctetString
_CienaCesDpTsCosMapFcosL3Dscp_Object=MibTableColumn
cienaCesDpTsCosMapFcosL3Dscp=_CienaCesDpTsCosMapFcosL3Dscp_Object((1,3,6,1,4,1,1271,2,1,7,1,3,2,1,1,5),_CienaCesDpTsCosMapFcosL3Dscp_Type())
cienaCesDpTsCosMapFcosL3Dscp.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesDpTsCosMapFcosL3Dscp.setStatus(_A)
_CienaCesDpTsCosMapFcosExp_Type=OctetString
_CienaCesDpTsCosMapFcosExp_Object=MibTableColumn
cienaCesDpTsCosMapFcosExp=_CienaCesDpTsCosMapFcosExp_Object((1,3,6,1,4,1,1271,2,1,7,1,3,2,1,1,6),_CienaCesDpTsCosMapFcosExp_Type())
cienaCesDpTsCosMapFcosExp.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesDpTsCosMapFcosExp.setStatus(_A)
_CienaCesDpTsShaper_ObjectIdentity=ObjectIdentity
cienaCesDpTsShaper=_CienaCesDpTsShaper_ObjectIdentity((1,3,6,1,4,1,1271,2,1,7,1,4))
_CienaCesDpTsShaperProfile_ObjectIdentity=ObjectIdentity
cienaCesDpTsShaperProfile=_CienaCesDpTsShaperProfile_ObjectIdentity((1,3,6,1,4,1,1271,2,1,7,1,4,1))
_CienaCesDpTsShaperProfileTable_Object=MibTable
cienaCesDpTsShaperProfileTable=_CienaCesDpTsShaperProfileTable_Object((1,3,6,1,4,1,1271,2,1,7,1,4,1,1))
if mibBuilder.loadTexts:cienaCesDpTsShaperProfileTable.setStatus(_A)
_CienaCesDpTsShaperProfileEntry_Object=MibTableRow
cienaCesDpTsShaperProfileEntry=_CienaCesDpTsShaperProfileEntry_Object((1,3,6,1,4,1,1271,2,1,7,1,4,1,1,1))
cienaCesDpTsShaperProfileEntry.setIndexNames((0,_C,_q))
if mibBuilder.loadTexts:cienaCesDpTsShaperProfileEntry.setStatus(_A)
class _CienaCesDpTsShaperProfileIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_CienaCesDpTsShaperProfileIndex_Type.__name__=_D
_CienaCesDpTsShaperProfileIndex_Object=MibTableColumn
cienaCesDpTsShaperProfileIndex=_CienaCesDpTsShaperProfileIndex_Object((1,3,6,1,4,1,1271,2,1,7,1,4,1,1,1,1),_CienaCesDpTsShaperProfileIndex_Type())
cienaCesDpTsShaperProfileIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:cienaCesDpTsShaperProfileIndex.setStatus(_A)
_CienaCesDpTsShaperProfileName_Type=DisplayString
_CienaCesDpTsShaperProfileName_Object=MibTableColumn
cienaCesDpTsShaperProfileName=_CienaCesDpTsShaperProfileName_Object((1,3,6,1,4,1,1271,2,1,7,1,4,1,1,1,2),_CienaCesDpTsShaperProfileName_Type())
cienaCesDpTsShaperProfileName.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesDpTsShaperProfileName.setStatus(_A)
_CienaCesDpTsShaperProfileCIR_Type=Unsigned32
_CienaCesDpTsShaperProfileCIR_Object=MibTableColumn
cienaCesDpTsShaperProfileCIR=_CienaCesDpTsShaperProfileCIR_Object((1,3,6,1,4,1,1271,2,1,7,1,4,1,1,1,3),_CienaCesDpTsShaperProfileCIR_Type())
cienaCesDpTsShaperProfileCIR.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesDpTsShaperProfileCIR.setStatus(_A)
if mibBuilder.loadTexts:cienaCesDpTsShaperProfileCIR.setUnits(_G)
_CienaCesDpTsShaperProfileCBS_Type=Unsigned32
_CienaCesDpTsShaperProfileCBS_Object=MibTableColumn
cienaCesDpTsShaperProfileCBS=_CienaCesDpTsShaperProfileCBS_Object((1,3,6,1,4,1,1271,2,1,7,1,4,1,1,1,4),_CienaCesDpTsShaperProfileCBS_Type())
cienaCesDpTsShaperProfileCBS.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesDpTsShaperProfileCBS.setStatus(_A)
if mibBuilder.loadTexts:cienaCesDpTsShaperProfileCBS.setUnits(_P)
_CienaCesDpTsShaperProfileAttachmentTable_Object=MibTable
cienaCesDpTsShaperProfileAttachmentTable=_CienaCesDpTsShaperProfileAttachmentTable_Object((1,3,6,1,4,1,1271,2,1,7,1,4,1,2))
if mibBuilder.loadTexts:cienaCesDpTsShaperProfileAttachmentTable.setStatus(_A)
_CienaCesDpTsShaperProfileAttachmentEntry_Object=MibTableRow
cienaCesDpTsShaperProfileAttachmentEntry=_CienaCesDpTsShaperProfileAttachmentEntry_Object((1,3,6,1,4,1,1271,2,1,7,1,4,1,2,1))
cienaCesDpTsShaperProfileAttachmentEntry.setIndexNames((0,_C,_q),(0,_C,_AC),(0,_C,_AD))
if mibBuilder.loadTexts:cienaCesDpTsShaperProfileAttachmentEntry.setStatus(_A)
_CienaCesDpTsShaperProfileAttachmentLiType_Type=DpTsAttachType
_CienaCesDpTsShaperProfileAttachmentLiType_Object=MibTableColumn
cienaCesDpTsShaperProfileAttachmentLiType=_CienaCesDpTsShaperProfileAttachmentLiType_Object((1,3,6,1,4,1,1271,2,1,7,1,4,1,2,1,1),_CienaCesDpTsShaperProfileAttachmentLiType_Type())
cienaCesDpTsShaperProfileAttachmentLiType.setMaxAccess(_E)
if mibBuilder.loadTexts:cienaCesDpTsShaperProfileAttachmentLiType.setStatus(_A)
class _CienaCesDpTsShaperProfileAttachmentLiIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,16777215))
_CienaCesDpTsShaperProfileAttachmentLiIndex_Type.__name__=_D
_CienaCesDpTsShaperProfileAttachmentLiIndex_Object=MibTableColumn
cienaCesDpTsShaperProfileAttachmentLiIndex=_CienaCesDpTsShaperProfileAttachmentLiIndex_Object((1,3,6,1,4,1,1271,2,1,7,1,4,1,2,1,2),_CienaCesDpTsShaperProfileAttachmentLiIndex_Type())
cienaCesDpTsShaperProfileAttachmentLiIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:cienaCesDpTsShaperProfileAttachmentLiIndex.setStatus(_A)
_CienaCesDpTsShaperProfileAttachmentTotalCIR_Type=Unsigned32
_CienaCesDpTsShaperProfileAttachmentTotalCIR_Object=MibTableColumn
cienaCesDpTsShaperProfileAttachmentTotalCIR=_CienaCesDpTsShaperProfileAttachmentTotalCIR_Object((1,3,6,1,4,1,1271,2,1,7,1,4,1,2,1,3),_CienaCesDpTsShaperProfileAttachmentTotalCIR_Type())
cienaCesDpTsShaperProfileAttachmentTotalCIR.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesDpTsShaperProfileAttachmentTotalCIR.setStatus(_A)
if mibBuilder.loadTexts:cienaCesDpTsShaperProfileAttachmentTotalCIR.setUnits(_G)
_CienaCesDpTsShaperProfileAttachmentTotalEIR_Type=Unsigned32
_CienaCesDpTsShaperProfileAttachmentTotalEIR_Object=MibTableColumn
cienaCesDpTsShaperProfileAttachmentTotalEIR=_CienaCesDpTsShaperProfileAttachmentTotalEIR_Object((1,3,6,1,4,1,1271,2,1,7,1,4,1,2,1,4),_CienaCesDpTsShaperProfileAttachmentTotalEIR_Type())
cienaCesDpTsShaperProfileAttachmentTotalEIR.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesDpTsShaperProfileAttachmentTotalEIR.setStatus(_A)
if mibBuilder.loadTexts:cienaCesDpTsShaperProfileAttachmentTotalEIR.setUnits(_G)
_CienaCesDpTsShaperProfileAttachmentUsedCIR_Type=Unsigned32
_CienaCesDpTsShaperProfileAttachmentUsedCIR_Object=MibTableColumn
cienaCesDpTsShaperProfileAttachmentUsedCIR=_CienaCesDpTsShaperProfileAttachmentUsedCIR_Object((1,3,6,1,4,1,1271,2,1,7,1,4,1,2,1,5),_CienaCesDpTsShaperProfileAttachmentUsedCIR_Type())
cienaCesDpTsShaperProfileAttachmentUsedCIR.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesDpTsShaperProfileAttachmentUsedCIR.setStatus(_A)
if mibBuilder.loadTexts:cienaCesDpTsShaperProfileAttachmentUsedCIR.setUnits(_G)
_CienaCesDpTsShaperProfileAttachmentMaxUsedEIR_Type=Unsigned32
_CienaCesDpTsShaperProfileAttachmentMaxUsedEIR_Object=MibTableColumn
cienaCesDpTsShaperProfileAttachmentMaxUsedEIR=_CienaCesDpTsShaperProfileAttachmentMaxUsedEIR_Object((1,3,6,1,4,1,1271,2,1,7,1,4,1,2,1,6),_CienaCesDpTsShaperProfileAttachmentMaxUsedEIR_Type())
cienaCesDpTsShaperProfileAttachmentMaxUsedEIR.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesDpTsShaperProfileAttachmentMaxUsedEIR.setStatus(_A)
if mibBuilder.loadTexts:cienaCesDpTsShaperProfileAttachmentMaxUsedEIR.setUnits(_G)
_CienaCesDpTsQ_ObjectIdentity=ObjectIdentity
cienaCesDpTsQ=_CienaCesDpTsQ_ObjectIdentity((1,3,6,1,4,1,1271,2,1,7,1,5))
_CienaCesDpTsQCongestionAvoidanceProfile_ObjectIdentity=ObjectIdentity
cienaCesDpTsQCongestionAvoidanceProfile=_CienaCesDpTsQCongestionAvoidanceProfile_ObjectIdentity((1,3,6,1,4,1,1271,2,1,7,1,5,1))
_CienaCesDpTsQCAProfileWREDTable_Object=MibTable
cienaCesDpTsQCAProfileWREDTable=_CienaCesDpTsQCAProfileWREDTable_Object((1,3,6,1,4,1,1271,2,1,7,1,5,1,1))
if mibBuilder.loadTexts:cienaCesDpTsQCAProfileWREDTable.setStatus(_A)
_CienaCesDpTsQCAProfileWREDEntry_Object=MibTableRow
cienaCesDpTsQCAProfileWREDEntry=_CienaCesDpTsQCAProfileWREDEntry_Object((1,3,6,1,4,1,1271,2,1,7,1,5,1,1,1))
cienaCesDpTsQCAProfileWREDEntry.setIndexNames((0,_C,_r))
if mibBuilder.loadTexts:cienaCesDpTsQCAProfileWREDEntry.setStatus(_A)
class _CienaCesDpTsQCAProfileWREDId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_CienaCesDpTsQCAProfileWREDId_Type.__name__=_D
_CienaCesDpTsQCAProfileWREDId_Object=MibTableColumn
cienaCesDpTsQCAProfileWREDId=_CienaCesDpTsQCAProfileWREDId_Object((1,3,6,1,4,1,1271,2,1,7,1,5,1,1,1,1),_CienaCesDpTsQCAProfileWREDId_Type())
cienaCesDpTsQCAProfileWREDId.setMaxAccess(_E)
if mibBuilder.loadTexts:cienaCesDpTsQCAProfileWREDId.setStatus(_A)
_CienaCesDpTsQCAProfileWREDName_Type=DisplayString
_CienaCesDpTsQCAProfileWREDName_Object=MibTableColumn
cienaCesDpTsQCAProfileWREDName=_CienaCesDpTsQCAProfileWREDName_Object((1,3,6,1,4,1,1271,2,1,7,1,5,1,1,1,2),_CienaCesDpTsQCAProfileWREDName_Type())
cienaCesDpTsQCAProfileWREDName.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesDpTsQCAProfileWREDName.setStatus(_A)
_CienaCesDpTsQCAProfileWREDDropRateExponent_Type=Unsigned32
_CienaCesDpTsQCAProfileWREDDropRateExponent_Object=MibTableColumn
cienaCesDpTsQCAProfileWREDDropRateExponent=_CienaCesDpTsQCAProfileWREDDropRateExponent_Object((1,3,6,1,4,1,1271,2,1,7,1,5,1,1,1,3),_CienaCesDpTsQCAProfileWREDDropRateExponent_Type())
cienaCesDpTsQCAProfileWREDDropRateExponent.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesDpTsQCAProfileWREDDropRateExponent.setStatus(_A)
_CienaCesDpTsQCAProfileWREDMaxQueueSize_Type=Integer32
_CienaCesDpTsQCAProfileWREDMaxQueueSize_Object=MibTableColumn
cienaCesDpTsQCAProfileWREDMaxQueueSize=_CienaCesDpTsQCAProfileWREDMaxQueueSize_Object((1,3,6,1,4,1,1271,2,1,7,1,5,1,1,1,4),_CienaCesDpTsQCAProfileWREDMaxQueueSize_Type())
cienaCesDpTsQCAProfileWREDMaxQueueSize.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesDpTsQCAProfileWREDMaxQueueSize.setStatus(_A)
_CienaCesDpTsQCAProfileWREDMinQueueGuarantee_Type=Integer32
_CienaCesDpTsQCAProfileWREDMinQueueGuarantee_Object=MibTableColumn
cienaCesDpTsQCAProfileWREDMinQueueGuarantee=_CienaCesDpTsQCAProfileWREDMinQueueGuarantee_Object((1,3,6,1,4,1,1271,2,1,7,1,5,1,1,1,5),_CienaCesDpTsQCAProfileWREDMinQueueGuarantee_Type())
cienaCesDpTsQCAProfileWREDMinQueueGuarantee.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesDpTsQCAProfileWREDMinQueueGuarantee.setStatus(_A)
_CienaCesDpTsQCAProfileWREDCurveTable_Object=MibTable
cienaCesDpTsQCAProfileWREDCurveTable=_CienaCesDpTsQCAProfileWREDCurveTable_Object((1,3,6,1,4,1,1271,2,1,7,1,5,1,2))
if mibBuilder.loadTexts:cienaCesDpTsQCAProfileWREDCurveTable.setStatus(_A)
_CienaCesDpTsQCAProfileWREDCurveEntry_Object=MibTableRow
cienaCesDpTsQCAProfileWREDCurveEntry=_CienaCesDpTsQCAProfileWREDCurveEntry_Object((1,3,6,1,4,1,1271,2,1,7,1,5,1,2,1))
cienaCesDpTsQCAProfileWREDCurveEntry.setIndexNames((0,_C,_r),(0,_C,_AE))
if mibBuilder.loadTexts:cienaCesDpTsQCAProfileWREDCurveEntry.setStatus(_A)
class _CienaCesDpTsQCAProfileWREDCurveId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,3))
_CienaCesDpTsQCAProfileWREDCurveId_Type.__name__=_D
_CienaCesDpTsQCAProfileWREDCurveId_Object=MibTableColumn
cienaCesDpTsQCAProfileWREDCurveId=_CienaCesDpTsQCAProfileWREDCurveId_Object((1,3,6,1,4,1,1271,2,1,7,1,5,1,2,1,1),_CienaCesDpTsQCAProfileWREDCurveId_Type())
cienaCesDpTsQCAProfileWREDCurveId.setMaxAccess(_E)
if mibBuilder.loadTexts:cienaCesDpTsQCAProfileWREDCurveId.setStatus(_A)
_CienaCesDpTsQCAProfileWREDCurveLowerThreshold_Type=Unsigned32
_CienaCesDpTsQCAProfileWREDCurveLowerThreshold_Object=MibTableColumn
cienaCesDpTsQCAProfileWREDCurveLowerThreshold=_CienaCesDpTsQCAProfileWREDCurveLowerThreshold_Object((1,3,6,1,4,1,1271,2,1,7,1,5,1,2,1,2),_CienaCesDpTsQCAProfileWREDCurveLowerThreshold_Type())
cienaCesDpTsQCAProfileWREDCurveLowerThreshold.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesDpTsQCAProfileWREDCurveLowerThreshold.setStatus(_A)
_CienaCesDpTsQCAProfileWREDCurveUpperThreshold_Type=Unsigned32
_CienaCesDpTsQCAProfileWREDCurveUpperThreshold_Object=MibTableColumn
cienaCesDpTsQCAProfileWREDCurveUpperThreshold=_CienaCesDpTsQCAProfileWREDCurveUpperThreshold_Object((1,3,6,1,4,1,1271,2,1,7,1,5,1,2,1,3),_CienaCesDpTsQCAProfileWREDCurveUpperThreshold_Type())
cienaCesDpTsQCAProfileWREDCurveUpperThreshold.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesDpTsQCAProfileWREDCurveUpperThreshold.setStatus(_A)
_CienaCesDpTsQCAProfileWREDCurveMaxDropProbability_Type=Unsigned32
_CienaCesDpTsQCAProfileWREDCurveMaxDropProbability_Object=MibTableColumn
cienaCesDpTsQCAProfileWREDCurveMaxDropProbability=_CienaCesDpTsQCAProfileWREDCurveMaxDropProbability_Object((1,3,6,1,4,1,1271,2,1,7,1,5,1,2,1,4),_CienaCesDpTsQCAProfileWREDCurveMaxDropProbability_Type())
cienaCesDpTsQCAProfileWREDCurveMaxDropProbability.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesDpTsQCAProfileWREDCurveMaxDropProbability.setStatus(_A)
_CienaCesDpTsQRCOSQMap_ObjectIdentity=ObjectIdentity
cienaCesDpTsQRCOSQMap=_CienaCesDpTsQRCOSQMap_ObjectIdentity((1,3,6,1,4,1,1271,2,1,7,1,5,2))
_CienaCesDpTsQRCOSQMapTable_Object=MibTable
cienaCesDpTsQRCOSQMapTable=_CienaCesDpTsQRCOSQMapTable_Object((1,3,6,1,4,1,1271,2,1,7,1,5,2,1))
if mibBuilder.loadTexts:cienaCesDpTsQRCOSQMapTable.setStatus(_A)
_CienaCesDpTsQRCOSQMapEntry_Object=MibTableRow
cienaCesDpTsQRCOSQMapEntry=_CienaCesDpTsQRCOSQMapEntry_Object((1,3,6,1,4,1,1271,2,1,7,1,5,2,1,1))
cienaCesDpTsQRCOSQMapEntry.setIndexNames((0,_C,_T))
if mibBuilder.loadTexts:cienaCesDpTsQRCOSQMapEntry.setStatus(_A)
class _CienaCesDpTsQRCOSQMapId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_CienaCesDpTsQRCOSQMapId_Type.__name__=_D
_CienaCesDpTsQRCOSQMapId_Object=MibTableColumn
cienaCesDpTsQRCOSQMapId=_CienaCesDpTsQRCOSQMapId_Object((1,3,6,1,4,1,1271,2,1,7,1,5,2,1,1,1),_CienaCesDpTsQRCOSQMapId_Type())
cienaCesDpTsQRCOSQMapId.setMaxAccess(_E)
if mibBuilder.loadTexts:cienaCesDpTsQRCOSQMapId.setStatus(_A)
_CienaCesDpTsQRCOSQMapName_Type=DisplayString
_CienaCesDpTsQRCOSQMapName_Object=MibTableColumn
cienaCesDpTsQRCOSQMapName=_CienaCesDpTsQRCOSQMapName_Object((1,3,6,1,4,1,1271,2,1,7,1,5,2,1,1,2),_CienaCesDpTsQRCOSQMapName_Type())
cienaCesDpTsQRCOSQMapName.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesDpTsQRCOSQMapName.setStatus(_A)
_CienaCesDpTsQRCOSQMapQueueTable_Object=MibTable
cienaCesDpTsQRCOSQMapQueueTable=_CienaCesDpTsQRCOSQMapQueueTable_Object((1,3,6,1,4,1,1271,2,1,7,1,5,2,2))
if mibBuilder.loadTexts:cienaCesDpTsQRCOSQMapQueueTable.setStatus(_A)
_CienaCesDpTsQRCOSQMapQueueEntry_Object=MibTableRow
cienaCesDpTsQRCOSQMapQueueEntry=_CienaCesDpTsQRCOSQMapQueueEntry_Object((1,3,6,1,4,1,1271,2,1,7,1,5,2,2,1))
cienaCesDpTsQRCOSQMapQueueEntry.setIndexNames((0,_C,_T),(0,_C,_AF))
if mibBuilder.loadTexts:cienaCesDpTsQRCOSQMapQueueEntry.setStatus(_A)
class _CienaCesDpTsQRCOSQMapQueueId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_CienaCesDpTsQRCOSQMapQueueId_Type.__name__=_D
_CienaCesDpTsQRCOSQMapQueueId_Object=MibTableColumn
cienaCesDpTsQRCOSQMapQueueId=_CienaCesDpTsQRCOSQMapQueueId_Object((1,3,6,1,4,1,1271,2,1,7,1,5,2,2,1,1),_CienaCesDpTsQRCOSQMapQueueId_Type())
cienaCesDpTsQRCOSQMapQueueId.setMaxAccess(_E)
if mibBuilder.loadTexts:cienaCesDpTsQRCOSQMapQueueId.setStatus(_A)
class _CienaCesDpTsQRCOSQMapQueueNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7)));namedValues=NamedValues(*(('queue-0',0),('queue-1',1),('queue-2',2),('queue-3',3),('queue-4',4),('queue-5',5),('queue-6',6),('queue-7',7)))
_CienaCesDpTsQRCOSQMapQueueNumber_Type.__name__=_D
_CienaCesDpTsQRCOSQMapQueueNumber_Object=MibTableColumn
cienaCesDpTsQRCOSQMapQueueNumber=_CienaCesDpTsQRCOSQMapQueueNumber_Object((1,3,6,1,4,1,1271,2,1,7,1,5,2,2,1,2),_CienaCesDpTsQRCOSQMapQueueNumber_Type())
cienaCesDpTsQRCOSQMapQueueNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesDpTsQRCOSQMapQueueNumber.setStatus(_A)
_CienaCesDpTsQRCOSQMapGreenCurveTable_Object=MibTable
cienaCesDpTsQRCOSQMapGreenCurveTable=_CienaCesDpTsQRCOSQMapGreenCurveTable_Object((1,3,6,1,4,1,1271,2,1,7,1,5,2,3))
if mibBuilder.loadTexts:cienaCesDpTsQRCOSQMapGreenCurveTable.setStatus(_A)
_CienaCesDpTsQRCOSQMapGreenCurveEntry_Object=MibTableRow
cienaCesDpTsQRCOSQMapGreenCurveEntry=_CienaCesDpTsQRCOSQMapGreenCurveEntry_Object((1,3,6,1,4,1,1271,2,1,7,1,5,2,3,1))
cienaCesDpTsQRCOSQMapGreenCurveEntry.setIndexNames((0,_C,_T),(0,_C,_AG))
if mibBuilder.loadTexts:cienaCesDpTsQRCOSQMapGreenCurveEntry.setStatus(_A)
class _CienaCesDpTsQRCOSQMapGreenCurveId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,63))
_CienaCesDpTsQRCOSQMapGreenCurveId_Type.__name__=_D
_CienaCesDpTsQRCOSQMapGreenCurveId_Object=MibTableColumn
cienaCesDpTsQRCOSQMapGreenCurveId=_CienaCesDpTsQRCOSQMapGreenCurveId_Object((1,3,6,1,4,1,1271,2,1,7,1,5,2,3,1,1),_CienaCesDpTsQRCOSQMapGreenCurveId_Type())
cienaCesDpTsQRCOSQMapGreenCurveId.setMaxAccess(_E)
if mibBuilder.loadTexts:cienaCesDpTsQRCOSQMapGreenCurveId.setStatus(_A)
class _CienaCesDpTsQRCOSQMapGreenCurveNumber_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_AH,1),(_AI,2)))
_CienaCesDpTsQRCOSQMapGreenCurveNumber_Type.__name__=_D
_CienaCesDpTsQRCOSQMapGreenCurveNumber_Object=MibTableColumn
cienaCesDpTsQRCOSQMapGreenCurveNumber=_CienaCesDpTsQRCOSQMapGreenCurveNumber_Object((1,3,6,1,4,1,1271,2,1,7,1,5,2,3,1,2),_CienaCesDpTsQRCOSQMapGreenCurveNumber_Type())
cienaCesDpTsQRCOSQMapGreenCurveNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesDpTsQRCOSQMapGreenCurveNumber.setStatus(_A)
_CienaCesDpTsQRCOSQMapYellowCurveTable_Object=MibTable
cienaCesDpTsQRCOSQMapYellowCurveTable=_CienaCesDpTsQRCOSQMapYellowCurveTable_Object((1,3,6,1,4,1,1271,2,1,7,1,5,2,4))
if mibBuilder.loadTexts:cienaCesDpTsQRCOSQMapYellowCurveTable.setStatus(_A)
_CienaCesDpTsQRCOSQMapYellowCurveEntry_Object=MibTableRow
cienaCesDpTsQRCOSQMapYellowCurveEntry=_CienaCesDpTsQRCOSQMapYellowCurveEntry_Object((1,3,6,1,4,1,1271,2,1,7,1,5,2,4,1))
cienaCesDpTsQRCOSQMapYellowCurveEntry.setIndexNames((0,_C,_T),(0,_C,_AJ))
if mibBuilder.loadTexts:cienaCesDpTsQRCOSQMapYellowCurveEntry.setStatus(_A)
class _CienaCesDpTsQRCOSQMapYellowCurveId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,63))
_CienaCesDpTsQRCOSQMapYellowCurveId_Type.__name__=_D
_CienaCesDpTsQRCOSQMapYellowCurveId_Object=MibTableColumn
cienaCesDpTsQRCOSQMapYellowCurveId=_CienaCesDpTsQRCOSQMapYellowCurveId_Object((1,3,6,1,4,1,1271,2,1,7,1,5,2,4,1,1),_CienaCesDpTsQRCOSQMapYellowCurveId_Type())
cienaCesDpTsQRCOSQMapYellowCurveId.setMaxAccess(_E)
if mibBuilder.loadTexts:cienaCesDpTsQRCOSQMapYellowCurveId.setStatus(_A)
class _CienaCesDpTsQRCOSQMapYellowCurveNumber_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_AH,1),(_AI,2)))
_CienaCesDpTsQRCOSQMapYellowCurveNumber_Type.__name__=_D
_CienaCesDpTsQRCOSQMapYellowCurveNumber_Object=MibTableColumn
cienaCesDpTsQRCOSQMapYellowCurveNumber=_CienaCesDpTsQRCOSQMapYellowCurveNumber_Object((1,3,6,1,4,1,1271,2,1,7,1,5,2,4,1,2),_CienaCesDpTsQRCOSQMapYellowCurveNumber_Type())
cienaCesDpTsQRCOSQMapYellowCurveNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesDpTsQRCOSQMapYellowCurveNumber.setStatus(_A)
_CienaCesDpTsQGroupProfile_ObjectIdentity=ObjectIdentity
cienaCesDpTsQGroupProfile=_CienaCesDpTsQGroupProfile_ObjectIdentity((1,3,6,1,4,1,1271,2,1,7,1,5,3))
_CienaCesDpTsQGroupProfileTable_Object=MibTable
cienaCesDpTsQGroupProfileTable=_CienaCesDpTsQGroupProfileTable_Object((1,3,6,1,4,1,1271,2,1,7,1,5,3,1))
if mibBuilder.loadTexts:cienaCesDpTsQGroupProfileTable.setStatus(_A)
_CienaCesDpTsQGroupProfileEntry_Object=MibTableRow
cienaCesDpTsQGroupProfileEntry=_CienaCesDpTsQGroupProfileEntry_Object((1,3,6,1,4,1,1271,2,1,7,1,5,3,1,1))
cienaCesDpTsQGroupProfileEntry.setIndexNames((0,_C,_X))
if mibBuilder.loadTexts:cienaCesDpTsQGroupProfileEntry.setStatus(_A)
class _CienaCesDpTsQGroupProfileId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_CienaCesDpTsQGroupProfileId_Type.__name__=_D
_CienaCesDpTsQGroupProfileId_Object=MibTableColumn
cienaCesDpTsQGroupProfileId=_CienaCesDpTsQGroupProfileId_Object((1,3,6,1,4,1,1271,2,1,7,1,5,3,1,1,1),_CienaCesDpTsQGroupProfileId_Type())
cienaCesDpTsQGroupProfileId.setMaxAccess(_E)
if mibBuilder.loadTexts:cienaCesDpTsQGroupProfileId.setStatus(_A)
_CienaCesDpTsQGroupProfileName_Type=DisplayString
_CienaCesDpTsQGroupProfileName_Object=MibTableColumn
cienaCesDpTsQGroupProfileName=_CienaCesDpTsQGroupProfileName_Object((1,3,6,1,4,1,1271,2,1,7,1,5,3,1,1,2),_CienaCesDpTsQGroupProfileName_Type())
cienaCesDpTsQGroupProfileName.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesDpTsQGroupProfileName.setStatus(_A)
_CienaCesDpTsQGroupProfileQueueCount_Type=Integer32
_CienaCesDpTsQGroupProfileQueueCount_Object=MibTableColumn
cienaCesDpTsQGroupProfileQueueCount=_CienaCesDpTsQGroupProfileQueueCount_Object((1,3,6,1,4,1,1271,2,1,7,1,5,3,1,1,3),_CienaCesDpTsQGroupProfileQueueCount_Type())
cienaCesDpTsQGroupProfileQueueCount.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesDpTsQGroupProfileQueueCount.setStatus(_A)
_CienaCesDpTsQGroupProfileRCOSQMapId_Type=Unsigned32
_CienaCesDpTsQGroupProfileRCOSQMapId_Object=MibTableColumn
cienaCesDpTsQGroupProfileRCOSQMapId=_CienaCesDpTsQGroupProfileRCOSQMapId_Object((1,3,6,1,4,1,1271,2,1,7,1,5,3,1,1,4),_CienaCesDpTsQGroupProfileRCOSQMapId_Type())
cienaCesDpTsQGroupProfileRCOSQMapId.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesDpTsQGroupProfileRCOSQMapId.setStatus(_A)
_CienaCesDpTsQGroupProfileShaperCompensation_Type=Integer32
_CienaCesDpTsQGroupProfileShaperCompensation_Object=MibTableColumn
cienaCesDpTsQGroupProfileShaperCompensation=_CienaCesDpTsQGroupProfileShaperCompensation_Object((1,3,6,1,4,1,1271,2,1,7,1,5,3,1,1,5),_CienaCesDpTsQGroupProfileShaperCompensation_Type())
cienaCesDpTsQGroupProfileShaperCompensation.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesDpTsQGroupProfileShaperCompensation.setStatus(_A)
_CienaCesDpTsQGroupProfileQueueTable_Object=MibTable
cienaCesDpTsQGroupProfileQueueTable=_CienaCesDpTsQGroupProfileQueueTable_Object((1,3,6,1,4,1,1271,2,1,7,1,5,3,2))
if mibBuilder.loadTexts:cienaCesDpTsQGroupProfileQueueTable.setStatus(_A)
_CienaCesDpTsQGroupProfileQueueEntry_Object=MibTableRow
cienaCesDpTsQGroupProfileQueueEntry=_CienaCesDpTsQGroupProfileQueueEntry_Object((1,3,6,1,4,1,1271,2,1,7,1,5,3,2,1))
cienaCesDpTsQGroupProfileQueueEntry.setIndexNames((0,_C,_X),(0,_C,_AK))
if mibBuilder.loadTexts:cienaCesDpTsQGroupProfileQueueEntry.setStatus(_A)
class _CienaCesDpTsQGroupProfileQueueIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_CienaCesDpTsQGroupProfileQueueIndex_Type.__name__=_D
_CienaCesDpTsQGroupProfileQueueIndex_Object=MibTableColumn
cienaCesDpTsQGroupProfileQueueIndex=_CienaCesDpTsQGroupProfileQueueIndex_Object((1,3,6,1,4,1,1271,2,1,7,1,5,3,2,1,1),_CienaCesDpTsQGroupProfileQueueIndex_Type())
cienaCesDpTsQGroupProfileQueueIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:cienaCesDpTsQGroupProfileQueueIndex.setStatus(_A)
_CienaCesDpTsQGroupProfileQueueCAPId_Type=Unsigned32
_CienaCesDpTsQGroupProfileQueueCAPId_Object=MibTableColumn
cienaCesDpTsQGroupProfileQueueCAPId=_CienaCesDpTsQGroupProfileQueueCAPId_Object((1,3,6,1,4,1,1271,2,1,7,1,5,3,2,1,2),_CienaCesDpTsQGroupProfileQueueCAPId_Type())
cienaCesDpTsQGroupProfileQueueCAPId.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesDpTsQGroupProfileQueueCAPId.setStatus(_A)
_CienaCesDpTsQGroupProfileQueueCIR_Type=Unsigned32
_CienaCesDpTsQGroupProfileQueueCIR_Object=MibTableColumn
cienaCesDpTsQGroupProfileQueueCIR=_CienaCesDpTsQGroupProfileQueueCIR_Object((1,3,6,1,4,1,1271,2,1,7,1,5,3,2,1,3),_CienaCesDpTsQGroupProfileQueueCIR_Type())
cienaCesDpTsQGroupProfileQueueCIR.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesDpTsQGroupProfileQueueCIR.setStatus(_A)
if mibBuilder.loadTexts:cienaCesDpTsQGroupProfileQueueCIR.setUnits(_G)
_CienaCesDpTsQGroupProfileQueueCBS_Type=Unsigned32
_CienaCesDpTsQGroupProfileQueueCBS_Object=MibTableColumn
cienaCesDpTsQGroupProfileQueueCBS=_CienaCesDpTsQGroupProfileQueueCBS_Object((1,3,6,1,4,1,1271,2,1,7,1,5,3,2,1,4),_CienaCesDpTsQGroupProfileQueueCBS_Type())
cienaCesDpTsQGroupProfileQueueCBS.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesDpTsQGroupProfileQueueCBS.setStatus(_A)
if mibBuilder.loadTexts:cienaCesDpTsQGroupProfileQueueCBS.setUnits(_P)
_CienaCesDpTsQGroupProfileQueueEIR_Type=Unsigned32
_CienaCesDpTsQGroupProfileQueueEIR_Object=MibTableColumn
cienaCesDpTsQGroupProfileQueueEIR=_CienaCesDpTsQGroupProfileQueueEIR_Object((1,3,6,1,4,1,1271,2,1,7,1,5,3,2,1,5),_CienaCesDpTsQGroupProfileQueueEIR_Type())
cienaCesDpTsQGroupProfileQueueEIR.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesDpTsQGroupProfileQueueEIR.setStatus(_A)
if mibBuilder.loadTexts:cienaCesDpTsQGroupProfileQueueEIR.setUnits(_G)
_CienaCesDpTsQGroupProfileQueueEBS_Type=Unsigned32
_CienaCesDpTsQGroupProfileQueueEBS_Object=MibTableColumn
cienaCesDpTsQGroupProfileQueueEBS=_CienaCesDpTsQGroupProfileQueueEBS_Object((1,3,6,1,4,1,1271,2,1,7,1,5,3,2,1,6),_CienaCesDpTsQGroupProfileQueueEBS_Type())
cienaCesDpTsQGroupProfileQueueEBS.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesDpTsQGroupProfileQueueEBS.setStatus(_A)
if mibBuilder.loadTexts:cienaCesDpTsQGroupProfileQueueEBS.setUnits(_P)
_CienaCesDpTsQGroupProfileQueueCirPercent_Type=Unsigned32
_CienaCesDpTsQGroupProfileQueueCirPercent_Object=MibTableColumn
cienaCesDpTsQGroupProfileQueueCirPercent=_CienaCesDpTsQGroupProfileQueueCirPercent_Object((1,3,6,1,4,1,1271,2,1,7,1,5,3,2,1,7),_CienaCesDpTsQGroupProfileQueueCirPercent_Type())
cienaCesDpTsQGroupProfileQueueCirPercent.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesDpTsQGroupProfileQueueCirPercent.setStatus(_A)
if mibBuilder.loadTexts:cienaCesDpTsQGroupProfileQueueCirPercent.setUnits(_Y)
_CienaCesDpTsQGroupProfileQueueEirPercent_Type=Unsigned32
_CienaCesDpTsQGroupProfileQueueEirPercent_Object=MibTableColumn
cienaCesDpTsQGroupProfileQueueEirPercent=_CienaCesDpTsQGroupProfileQueueEirPercent_Object((1,3,6,1,4,1,1271,2,1,7,1,5,3,2,1,8),_CienaCesDpTsQGroupProfileQueueEirPercent_Type())
cienaCesDpTsQGroupProfileQueueEirPercent.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesDpTsQGroupProfileQueueEirPercent.setStatus(_A)
if mibBuilder.loadTexts:cienaCesDpTsQGroupProfileQueueEirPercent.setUnits(_Y)
_CienaCesDpTsQGroupInstance_ObjectIdentity=ObjectIdentity
cienaCesDpTsQGroupInstance=_CienaCesDpTsQGroupInstance_ObjectIdentity((1,3,6,1,4,1,1271,2,1,7,1,5,4))
_CienaCesDpTsQGroupInstanceTable_Object=MibTable
cienaCesDpTsQGroupInstanceTable=_CienaCesDpTsQGroupInstanceTable_Object((1,3,6,1,4,1,1271,2,1,7,1,5,4,1))
if mibBuilder.loadTexts:cienaCesDpTsQGroupInstanceTable.setStatus(_A)
_CienaCesDpTsQGroupInstanceEntry_Object=MibTableRow
cienaCesDpTsQGroupInstanceEntry=_CienaCesDpTsQGroupInstanceEntry_Object((1,3,6,1,4,1,1271,2,1,7,1,5,4,1,1))
cienaCesDpTsQGroupInstanceEntry.setIndexNames((0,_C,_AL),(0,_C,_X),(0,_C,_AM))
if mibBuilder.loadTexts:cienaCesDpTsQGroupInstanceEntry.setStatus(_A)
_CienaCesDpTsQGroupInstancePgid_Type=Unsigned32
_CienaCesDpTsQGroupInstancePgid_Object=MibTableColumn
cienaCesDpTsQGroupInstancePgid=_CienaCesDpTsQGroupInstancePgid_Object((1,3,6,1,4,1,1271,2,1,7,1,5,4,1,1,1),_CienaCesDpTsQGroupInstancePgid_Type())
cienaCesDpTsQGroupInstancePgid.setMaxAccess(_E)
if mibBuilder.loadTexts:cienaCesDpTsQGroupInstancePgid.setStatus(_A)
class _CienaCesDpTsQGroupInstanceIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_CienaCesDpTsQGroupInstanceIndex_Type.__name__=_D
_CienaCesDpTsQGroupInstanceIndex_Object=MibTableColumn
cienaCesDpTsQGroupInstanceIndex=_CienaCesDpTsQGroupInstanceIndex_Object((1,3,6,1,4,1,1271,2,1,7,1,5,4,1,1,2),_CienaCesDpTsQGroupInstanceIndex_Type())
cienaCesDpTsQGroupInstanceIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:cienaCesDpTsQGroupInstanceIndex.setStatus(_A)
_CienaCesDpTsQGroupInstanceParentSchedId_Type=Integer32
_CienaCesDpTsQGroupInstanceParentSchedId_Object=MibTableColumn
cienaCesDpTsQGroupInstanceParentSchedId=_CienaCesDpTsQGroupInstanceParentSchedId_Object((1,3,6,1,4,1,1271,2,1,7,1,5,4,1,1,3),_CienaCesDpTsQGroupInstanceParentSchedId_Type())
cienaCesDpTsQGroupInstanceParentSchedId.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesDpTsQGroupInstanceParentSchedId.setStatus(_A)
_CienaCesDpTsQGroupInstanceParentInstanceId_Type=Integer32
_CienaCesDpTsQGroupInstanceParentInstanceId_Object=MibTableColumn
cienaCesDpTsQGroupInstanceParentInstanceId=_CienaCesDpTsQGroupInstanceParentInstanceId_Object((1,3,6,1,4,1,1271,2,1,7,1,5,4,1,1,4),_CienaCesDpTsQGroupInstanceParentInstanceId_Type())
cienaCesDpTsQGroupInstanceParentInstanceId.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesDpTsQGroupInstanceParentInstanceId.setStatus(_A)
_CienaCesDpTsQSchedulerProfile_ObjectIdentity=ObjectIdentity
cienaCesDpTsQSchedulerProfile=_CienaCesDpTsQSchedulerProfile_ObjectIdentity((1,3,6,1,4,1,1271,2,1,7,1,5,5))
_CienaCesDpTsQSchedulerProfileTable_Object=MibTable
cienaCesDpTsQSchedulerProfileTable=_CienaCesDpTsQSchedulerProfileTable_Object((1,3,6,1,4,1,1271,2,1,7,1,5,5,1))
if mibBuilder.loadTexts:cienaCesDpTsQSchedulerProfileTable.setStatus(_A)
_CienaCesDpTsQSchedulerProfileEntry_Object=MibTableRow
cienaCesDpTsQSchedulerProfileEntry=_CienaCesDpTsQSchedulerProfileEntry_Object((1,3,6,1,4,1,1271,2,1,7,1,5,5,1,1))
cienaCesDpTsQSchedulerProfileEntry.setIndexNames((0,_C,_Z))
if mibBuilder.loadTexts:cienaCesDpTsQSchedulerProfileEntry.setStatus(_A)
class _CienaCesDpTsQSchedulerProfileId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_CienaCesDpTsQSchedulerProfileId_Type.__name__=_D
_CienaCesDpTsQSchedulerProfileId_Object=MibTableColumn
cienaCesDpTsQSchedulerProfileId=_CienaCesDpTsQSchedulerProfileId_Object((1,3,6,1,4,1,1271,2,1,7,1,5,5,1,1,1),_CienaCesDpTsQSchedulerProfileId_Type())
cienaCesDpTsQSchedulerProfileId.setMaxAccess(_E)
if mibBuilder.loadTexts:cienaCesDpTsQSchedulerProfileId.setStatus(_A)
_CienaCesDpTsQSchedulerProfileName_Type=DisplayString
_CienaCesDpTsQSchedulerProfileName_Object=MibTableColumn
cienaCesDpTsQSchedulerProfileName=_CienaCesDpTsQSchedulerProfileName_Object((1,3,6,1,4,1,1271,2,1,7,1,5,5,1,1,2),_CienaCesDpTsQSchedulerProfileName_Type())
cienaCesDpTsQSchedulerProfileName.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesDpTsQSchedulerProfileName.setStatus(_A)
class _CienaCesDpTsQSchedulerProfileSchedulerAlgorithm_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*((_R,0),('strictPriority',1),('weightedFairQueuing',2),('roundRobin',3)))
_CienaCesDpTsQSchedulerProfileSchedulerAlgorithm_Type.__name__=_D
_CienaCesDpTsQSchedulerProfileSchedulerAlgorithm_Object=MibTableColumn
cienaCesDpTsQSchedulerProfileSchedulerAlgorithm=_CienaCesDpTsQSchedulerProfileSchedulerAlgorithm_Object((1,3,6,1,4,1,1271,2,1,7,1,5,5,1,1,3),_CienaCesDpTsQSchedulerProfileSchedulerAlgorithm_Type())
cienaCesDpTsQSchedulerProfileSchedulerAlgorithm.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesDpTsQSchedulerProfileSchedulerAlgorithm.setStatus(_A)
_CienaCesDpTsQSchedulerProfileCIR_Type=Unsigned32
_CienaCesDpTsQSchedulerProfileCIR_Object=MibTableColumn
cienaCesDpTsQSchedulerProfileCIR=_CienaCesDpTsQSchedulerProfileCIR_Object((1,3,6,1,4,1,1271,2,1,7,1,5,5,1,1,4),_CienaCesDpTsQSchedulerProfileCIR_Type())
cienaCesDpTsQSchedulerProfileCIR.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesDpTsQSchedulerProfileCIR.setStatus(_A)
if mibBuilder.loadTexts:cienaCesDpTsQSchedulerProfileCIR.setUnits(_G)
_CienaCesDpTsQSchedulerProfileCBS_Type=Unsigned32
_CienaCesDpTsQSchedulerProfileCBS_Object=MibTableColumn
cienaCesDpTsQSchedulerProfileCBS=_CienaCesDpTsQSchedulerProfileCBS_Object((1,3,6,1,4,1,1271,2,1,7,1,5,5,1,1,5),_CienaCesDpTsQSchedulerProfileCBS_Type())
cienaCesDpTsQSchedulerProfileCBS.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesDpTsQSchedulerProfileCBS.setStatus(_A)
if mibBuilder.loadTexts:cienaCesDpTsQSchedulerProfileCBS.setUnits(_P)
_CienaCesDpTsQSchedulerProfileEIR_Type=Unsigned32
_CienaCesDpTsQSchedulerProfileEIR_Object=MibTableColumn
cienaCesDpTsQSchedulerProfileEIR=_CienaCesDpTsQSchedulerProfileEIR_Object((1,3,6,1,4,1,1271,2,1,7,1,5,5,1,1,6),_CienaCesDpTsQSchedulerProfileEIR_Type())
cienaCesDpTsQSchedulerProfileEIR.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesDpTsQSchedulerProfileEIR.setStatus(_A)
if mibBuilder.loadTexts:cienaCesDpTsQSchedulerProfileEIR.setUnits(_G)
class _CienaCesDpTsQSchedulerProfileEBS_Type(Unsigned32):defaultValue=32
_CienaCesDpTsQSchedulerProfileEBS_Type.__name__=_S
_CienaCesDpTsQSchedulerProfileEBS_Object=MibTableColumn
cienaCesDpTsQSchedulerProfileEBS=_CienaCesDpTsQSchedulerProfileEBS_Object((1,3,6,1,4,1,1271,2,1,7,1,5,5,1,1,7),_CienaCesDpTsQSchedulerProfileEBS_Type())
cienaCesDpTsQSchedulerProfileEBS.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesDpTsQSchedulerProfileEBS.setStatus(_A)
if mibBuilder.loadTexts:cienaCesDpTsQSchedulerProfileEBS.setUnits(_P)
class _CienaCesDpTsQSchedulerProfileScheduledUcastWt_Type(Integer32):defaultValue=80
_CienaCesDpTsQSchedulerProfileScheduledUcastWt_Type.__name__=_D
_CienaCesDpTsQSchedulerProfileScheduledUcastWt_Object=MibTableColumn
cienaCesDpTsQSchedulerProfileScheduledUcastWt=_CienaCesDpTsQSchedulerProfileScheduledUcastWt_Object((1,3,6,1,4,1,1271,2,1,7,1,5,5,1,1,8),_CienaCesDpTsQSchedulerProfileScheduledUcastWt_Type())
cienaCesDpTsQSchedulerProfileScheduledUcastWt.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesDpTsQSchedulerProfileScheduledUcastWt.setStatus(_A)
class _CienaCesDpTsQSchedulerProfileScheduledMcastWt_Type(Integer32):defaultValue=20
_CienaCesDpTsQSchedulerProfileScheduledMcastWt_Type.__name__=_D
_CienaCesDpTsQSchedulerProfileScheduledMcastWt_Object=MibTableColumn
cienaCesDpTsQSchedulerProfileScheduledMcastWt=_CienaCesDpTsQSchedulerProfileScheduledMcastWt_Object((1,3,6,1,4,1,1271,2,1,7,1,5,5,1,1,9),_CienaCesDpTsQSchedulerProfileScheduledMcastWt_Type())
cienaCesDpTsQSchedulerProfileScheduledMcastWt.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesDpTsQSchedulerProfileScheduledMcastWt.setStatus(_A)
_CienaCesDpTsQSchedulerProfileTapPointCount_Type=Integer32
_CienaCesDpTsQSchedulerProfileTapPointCount_Object=MibTableColumn
cienaCesDpTsQSchedulerProfileTapPointCount=_CienaCesDpTsQSchedulerProfileTapPointCount_Object((1,3,6,1,4,1,1271,2,1,7,1,5,5,1,1,10),_CienaCesDpTsQSchedulerProfileTapPointCount_Type())
cienaCesDpTsQSchedulerProfileTapPointCount.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesDpTsQSchedulerProfileTapPointCount.setStatus(_A)
_CienaCesDpTsQSchedulerProfileShaperOverSpeed_Type=Integer32
_CienaCesDpTsQSchedulerProfileShaperOverSpeed_Object=MibTableColumn
cienaCesDpTsQSchedulerProfileShaperOverSpeed=_CienaCesDpTsQSchedulerProfileShaperOverSpeed_Object((1,3,6,1,4,1,1271,2,1,7,1,5,5,1,1,11),_CienaCesDpTsQSchedulerProfileShaperOverSpeed_Type())
cienaCesDpTsQSchedulerProfileShaperOverSpeed.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesDpTsQSchedulerProfileShaperOverSpeed.setStatus(_A)
class _CienaCesDpTsQSchedulerProfileCirPolicy_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4)));namedValues=NamedValues(*((_s,0),(_AN,1),('cirAsPercent',2),('childCirAsPercent',3),('childCirSum',4)))
_CienaCesDpTsQSchedulerProfileCirPolicy_Type.__name__=_D
_CienaCesDpTsQSchedulerProfileCirPolicy_Object=MibTableColumn
cienaCesDpTsQSchedulerProfileCirPolicy=_CienaCesDpTsQSchedulerProfileCirPolicy_Object((1,3,6,1,4,1,1271,2,1,7,1,5,5,1,1,12),_CienaCesDpTsQSchedulerProfileCirPolicy_Type())
cienaCesDpTsQSchedulerProfileCirPolicy.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesDpTsQSchedulerProfileCirPolicy.setStatus(_A)
class _CienaCesDpTsQSchedulerProfileEirPolicy_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*((_s,0),(_AN,1),('eirAsPercent',2),('childEirAsPercent',3)))
_CienaCesDpTsQSchedulerProfileEirPolicy_Type.__name__=_D
_CienaCesDpTsQSchedulerProfileEirPolicy_Object=MibTableColumn
cienaCesDpTsQSchedulerProfileEirPolicy=_CienaCesDpTsQSchedulerProfileEirPolicy_Object((1,3,6,1,4,1,1271,2,1,7,1,5,5,1,1,13),_CienaCesDpTsQSchedulerProfileEirPolicy_Type())
cienaCesDpTsQSchedulerProfileEirPolicy.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesDpTsQSchedulerProfileEirPolicy.setStatus(_A)
_CienaCesDpTsQSchedulerProfileCirPercent_Type=Unsigned32
_CienaCesDpTsQSchedulerProfileCirPercent_Object=MibTableColumn
cienaCesDpTsQSchedulerProfileCirPercent=_CienaCesDpTsQSchedulerProfileCirPercent_Object((1,3,6,1,4,1,1271,2,1,7,1,5,5,1,1,14),_CienaCesDpTsQSchedulerProfileCirPercent_Type())
cienaCesDpTsQSchedulerProfileCirPercent.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesDpTsQSchedulerProfileCirPercent.setStatus(_A)
if mibBuilder.loadTexts:cienaCesDpTsQSchedulerProfileCirPercent.setUnits(_Y)
_CienaCesDpTsQSchedulerProfileEirPercent_Type=Unsigned32
_CienaCesDpTsQSchedulerProfileEirPercent_Object=MibTableColumn
cienaCesDpTsQSchedulerProfileEirPercent=_CienaCesDpTsQSchedulerProfileEirPercent_Object((1,3,6,1,4,1,1271,2,1,7,1,5,5,1,1,15),_CienaCesDpTsQSchedulerProfileEirPercent_Type())
cienaCesDpTsQSchedulerProfileEirPercent.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesDpTsQSchedulerProfileEirPercent.setStatus(_A)
if mibBuilder.loadTexts:cienaCesDpTsQSchedulerProfileEirPercent.setUnits(_Y)
_CienaCesDpTsQSchedulerTapPointTable_Object=MibTable
cienaCesDpTsQSchedulerTapPointTable=_CienaCesDpTsQSchedulerTapPointTable_Object((1,3,6,1,4,1,1271,2,1,7,1,5,5,2))
if mibBuilder.loadTexts:cienaCesDpTsQSchedulerTapPointTable.setStatus(_A)
_CienaCesDpTsQSchedulerTapPointEntry_Object=MibTableRow
cienaCesDpTsQSchedulerTapPointEntry=_CienaCesDpTsQSchedulerTapPointEntry_Object((1,3,6,1,4,1,1271,2,1,7,1,5,5,2,1))
cienaCesDpTsQSchedulerTapPointEntry.setIndexNames((0,_C,_Z),(0,_C,_AO))
if mibBuilder.loadTexts:cienaCesDpTsQSchedulerTapPointEntry.setStatus(_A)
class _CienaCesDpTsQSchedulerTapPointIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_CienaCesDpTsQSchedulerTapPointIndex_Type.__name__=_D
_CienaCesDpTsQSchedulerTapPointIndex_Object=MibTableColumn
cienaCesDpTsQSchedulerTapPointIndex=_CienaCesDpTsQSchedulerTapPointIndex_Object((1,3,6,1,4,1,1271,2,1,7,1,5,5,2,1,1),_CienaCesDpTsQSchedulerTapPointIndex_Type())
cienaCesDpTsQSchedulerTapPointIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:cienaCesDpTsQSchedulerTapPointIndex.setStatus(_A)
_CienaCesDpTsQSchedulerTapPointPriority_Type=Integer32
_CienaCesDpTsQSchedulerTapPointPriority_Object=MibTableColumn
cienaCesDpTsQSchedulerTapPointPriority=_CienaCesDpTsQSchedulerTapPointPriority_Object((1,3,6,1,4,1,1271,2,1,7,1,5,5,2,1,2),_CienaCesDpTsQSchedulerTapPointPriority_Type())
cienaCesDpTsQSchedulerTapPointPriority.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesDpTsQSchedulerTapPointPriority.setStatus(_A)
_CienaCesDpTsQSchedulerTapPointWeight_Type=Integer32
_CienaCesDpTsQSchedulerTapPointWeight_Object=MibTableColumn
cienaCesDpTsQSchedulerTapPointWeight=_CienaCesDpTsQSchedulerTapPointWeight_Object((1,3,6,1,4,1,1271,2,1,7,1,5,5,2,1,3),_CienaCesDpTsQSchedulerTapPointWeight_Type())
cienaCesDpTsQSchedulerTapPointWeight.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesDpTsQSchedulerTapPointWeight.setStatus(_A)
_CienaCesDpTsQSchedulerInstance_ObjectIdentity=ObjectIdentity
cienaCesDpTsQSchedulerInstance=_CienaCesDpTsQSchedulerInstance_ObjectIdentity((1,3,6,1,4,1,1271,2,1,7,1,5,6))
_CienaCesDpTsQSchedulerInstanceTable_Object=MibTable
cienaCesDpTsQSchedulerInstanceTable=_CienaCesDpTsQSchedulerInstanceTable_Object((1,3,6,1,4,1,1271,2,1,7,1,5,6,1))
if mibBuilder.loadTexts:cienaCesDpTsQSchedulerInstanceTable.setStatus(_A)
_CienaCesDpTsQSchedulerInstanceEntry_Object=MibTableRow
cienaCesDpTsQSchedulerInstanceEntry=_CienaCesDpTsQSchedulerInstanceEntry_Object((1,3,6,1,4,1,1271,2,1,7,1,5,6,1,1))
cienaCesDpTsQSchedulerInstanceEntry.setIndexNames((0,_C,_AP),(0,_C,_Z),(0,_C,_AQ))
if mibBuilder.loadTexts:cienaCesDpTsQSchedulerInstanceEntry.setStatus(_A)
_CienaCesDpTsQSchedulerInstancePgid_Type=Unsigned32
_CienaCesDpTsQSchedulerInstancePgid_Object=MibTableColumn
cienaCesDpTsQSchedulerInstancePgid=_CienaCesDpTsQSchedulerInstancePgid_Object((1,3,6,1,4,1,1271,2,1,7,1,5,6,1,1,1),_CienaCesDpTsQSchedulerInstancePgid_Type())
cienaCesDpTsQSchedulerInstancePgid.setMaxAccess(_E)
if mibBuilder.loadTexts:cienaCesDpTsQSchedulerInstancePgid.setStatus(_A)
class _CienaCesDpTsQSchedulerInstanceIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_CienaCesDpTsQSchedulerInstanceIndex_Type.__name__=_D
_CienaCesDpTsQSchedulerInstanceIndex_Object=MibTableColumn
cienaCesDpTsQSchedulerInstanceIndex=_CienaCesDpTsQSchedulerInstanceIndex_Object((1,3,6,1,4,1,1271,2,1,7,1,5,6,1,1,2),_CienaCesDpTsQSchedulerInstanceIndex_Type())
cienaCesDpTsQSchedulerInstanceIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:cienaCesDpTsQSchedulerInstanceIndex.setStatus(_A)
_CienaCesDpTsQSchedulerInstanceParentSchedId_Type=Integer32
_CienaCesDpTsQSchedulerInstanceParentSchedId_Object=MibTableColumn
cienaCesDpTsQSchedulerInstanceParentSchedId=_CienaCesDpTsQSchedulerInstanceParentSchedId_Object((1,3,6,1,4,1,1271,2,1,7,1,5,6,1,1,3),_CienaCesDpTsQSchedulerInstanceParentSchedId_Type())
cienaCesDpTsQSchedulerInstanceParentSchedId.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesDpTsQSchedulerInstanceParentSchedId.setStatus(_A)
_CienaCesDpTsQSchedulerInstanceParentInstanceId_Type=Integer32
_CienaCesDpTsQSchedulerInstanceParentInstanceId_Object=MibTableColumn
cienaCesDpTsQSchedulerInstanceParentInstanceId=_CienaCesDpTsQSchedulerInstanceParentInstanceId_Object((1,3,6,1,4,1,1271,2,1,7,1,5,6,1,1,4),_CienaCesDpTsQSchedulerInstanceParentInstanceId_Type())
cienaCesDpTsQSchedulerInstanceParentInstanceId.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesDpTsQSchedulerInstanceParentInstanceId.setStatus(_A)
_CienaCesDpTsQSchedulerInstanceParentTapPoint_Type=Integer32
_CienaCesDpTsQSchedulerInstanceParentTapPoint_Object=MibTableColumn
cienaCesDpTsQSchedulerInstanceParentTapPoint=_CienaCesDpTsQSchedulerInstanceParentTapPoint_Object((1,3,6,1,4,1,1271,2,1,7,1,5,6,1,1,5),_CienaCesDpTsQSchedulerInstanceParentTapPoint_Type())
cienaCesDpTsQSchedulerInstanceParentTapPoint.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesDpTsQSchedulerInstanceParentTapPoint.setStatus(_A)
_CienaCesDpTsQSchedulerInstanceControlPlaneUsedCir_Type=Unsigned32
_CienaCesDpTsQSchedulerInstanceControlPlaneUsedCir_Object=MibTableColumn
cienaCesDpTsQSchedulerInstanceControlPlaneUsedCir=_CienaCesDpTsQSchedulerInstanceControlPlaneUsedCir_Object((1,3,6,1,4,1,1271,2,1,7,1,5,6,1,1,6),_CienaCesDpTsQSchedulerInstanceControlPlaneUsedCir_Type())
cienaCesDpTsQSchedulerInstanceControlPlaneUsedCir.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesDpTsQSchedulerInstanceControlPlaneUsedCir.setStatus(_A)
if mibBuilder.loadTexts:cienaCesDpTsQSchedulerInstanceControlPlaneUsedCir.setUnits(_G)
_CienaCesDpTrafficClassTerm_ObjectIdentity=ObjectIdentity
cienaCesDpTrafficClassTerm=_CienaCesDpTrafficClassTerm_ObjectIdentity((1,3,6,1,4,1,1271,2,1,7,1,6))
_CienaCesDpTrafficClassTermTable_Object=MibTable
cienaCesDpTrafficClassTermTable=_CienaCesDpTrafficClassTermTable_Object((1,3,6,1,4,1,1271,2,1,7,1,6,1))
if mibBuilder.loadTexts:cienaCesDpTrafficClassTermTable.setStatus(_A)
_CienaCesDpTrafficClassTermEntry_Object=MibTableRow
cienaCesDpTrafficClassTermEntry=_CienaCesDpTrafficClassTermEntry_Object((1,3,6,1,4,1,1271,2,1,7,1,6,1,1))
cienaCesDpTrafficClassTermEntry.setIndexNames((0,_C,_AR),(0,_C,_AS),(0,_C,_AT),(0,_C,_AU))
if mibBuilder.loadTexts:cienaCesDpTrafficClassTermEntry.setStatus(_A)
class _CienaCesDpTrafficClassType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7,8)));namedValues=NamedValues(*((_R,0),('subPort',1),('qosFlow',2),(_A2,3),(_A1,4),(_A3,5),(_A0,6),('vcMpls',7),('named',8)))
_CienaCesDpTrafficClassType_Type.__name__=_D
_CienaCesDpTrafficClassType_Object=MibTableColumn
cienaCesDpTrafficClassType=_CienaCesDpTrafficClassType_Object((1,3,6,1,4,1,1271,2,1,7,1,6,1,1,1),_CienaCesDpTrafficClassType_Type())
cienaCesDpTrafficClassType.setMaxAccess(_E)
if mibBuilder.loadTexts:cienaCesDpTrafficClassType.setStatus(_A)
class _CienaCesDpTrafficClassId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_CienaCesDpTrafficClassId_Type.__name__=_D
_CienaCesDpTrafficClassId_Object=MibTableColumn
cienaCesDpTrafficClassId=_CienaCesDpTrafficClassId_Object((1,3,6,1,4,1,1271,2,1,7,1,6,1,1,2),_CienaCesDpTrafficClassId_Type())
cienaCesDpTrafficClassId.setMaxAccess(_E)
if mibBuilder.loadTexts:cienaCesDpTrafficClassId.setStatus(_A)
class _CienaCesDpTrafficClassElemId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_CienaCesDpTrafficClassElemId_Type.__name__=_D
_CienaCesDpTrafficClassElemId_Object=MibTableColumn
cienaCesDpTrafficClassElemId=_CienaCesDpTrafficClassElemId_Object((1,3,6,1,4,1,1271,2,1,7,1,6,1,1,3),_CienaCesDpTrafficClassElemId_Type())
cienaCesDpTrafficClassElemId.setMaxAccess(_E)
if mibBuilder.loadTexts:cienaCesDpTrafficClassElemId.setStatus(_A)
class _CienaCesDpTrafficClassTermPresentType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27)));namedValues=NamedValues(*((_R,0),('trafficClassElement',1),('vid1',2),('l2Pcp1',3),('vid2',4),('l2Pcp2',5),('vlanUntaggedData',6),('l2Control',7),('cMacSa',8),('cMacDa',9),('ipSrcIp',10),('ipDstIp',11),('ipProtoType',12),('ipDscp',13),('ipL4SrcPort',14),('ipL4DstPort',15),('mplsVcLabel',16),('mplsVcExp',17),('mplsTunLabel',18),('mplsTunExp',19),('baseEtype',20),('bvid',21),('bPcp',22),('isid',23),('isidPcp',24),('any',25),('l2Rcos',26),('ipL4Application',27)))
_CienaCesDpTrafficClassTermPresentType_Type.__name__=_D
_CienaCesDpTrafficClassTermPresentType_Object=MibTableColumn
cienaCesDpTrafficClassTermPresentType=_CienaCesDpTrafficClassTermPresentType_Object((1,3,6,1,4,1,1271,2,1,7,1,6,1,1,4),_CienaCesDpTrafficClassTermPresentType_Type())
cienaCesDpTrafficClassTermPresentType.setMaxAccess(_E)
if mibBuilder.loadTexts:cienaCesDpTrafficClassTermPresentType.setStatus(_A)
class _CienaCesDpTrafficClassTermStartValue32_Type(Unsigned32):defaultValue=0
_CienaCesDpTrafficClassTermStartValue32_Type.__name__=_S
_CienaCesDpTrafficClassTermStartValue32_Object=MibTableColumn
cienaCesDpTrafficClassTermStartValue32=_CienaCesDpTrafficClassTermStartValue32_Object((1,3,6,1,4,1,1271,2,1,7,1,6,1,1,5),_CienaCesDpTrafficClassTermStartValue32_Type())
cienaCesDpTrafficClassTermStartValue32.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesDpTrafficClassTermStartValue32.setStatus(_A)
class _CienaCesDpTrafficClassTermEndOrMaskValue32_Type(Unsigned32):defaultValue=0
_CienaCesDpTrafficClassTermEndOrMaskValue32_Type.__name__=_S
_CienaCesDpTrafficClassTermEndOrMaskValue32_Object=MibTableColumn
cienaCesDpTrafficClassTermEndOrMaskValue32=_CienaCesDpTrafficClassTermEndOrMaskValue32_Object((1,3,6,1,4,1,1271,2,1,7,1,6,1,1,6),_CienaCesDpTrafficClassTermEndOrMaskValue32_Type())
cienaCesDpTrafficClassTermEndOrMaskValue32.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesDpTrafficClassTermEndOrMaskValue32.setStatus(_A)
class _CienaCesDpTrafficClassTermStartValueMac_Type(MacAddress):defaultHexValue=_AV
_CienaCesDpTrafficClassTermStartValueMac_Type.__name__=_j
_CienaCesDpTrafficClassTermStartValueMac_Object=MibTableColumn
cienaCesDpTrafficClassTermStartValueMac=_CienaCesDpTrafficClassTermStartValueMac_Object((1,3,6,1,4,1,1271,2,1,7,1,6,1,1,7),_CienaCesDpTrafficClassTermStartValueMac_Type())
cienaCesDpTrafficClassTermStartValueMac.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesDpTrafficClassTermStartValueMac.setStatus(_A)
class _CienaCesDpTrafficClassTermMaskValueMac_Type(MacAddress):defaultHexValue=_AV
_CienaCesDpTrafficClassTermMaskValueMac_Type.__name__=_j
_CienaCesDpTrafficClassTermMaskValueMac_Object=MibTableColumn
cienaCesDpTrafficClassTermMaskValueMac=_CienaCesDpTrafficClassTermMaskValueMac_Object((1,3,6,1,4,1,1271,2,1,7,1,6,1,1,8),_CienaCesDpTrafficClassTermMaskValueMac_Type())
cienaCesDpTrafficClassTermMaskValueMac.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesDpTrafficClassTermMaskValueMac.setStatus(_A)
class _CienaCesDpTrafficClassTermStartValueIp_Type(IpAddress):defaultHexValue='00000000'
_CienaCesDpTrafficClassTermStartValueIp_Type.__name__=_i
_CienaCesDpTrafficClassTermStartValueIp_Object=MibTableColumn
cienaCesDpTrafficClassTermStartValueIp=_CienaCesDpTrafficClassTermStartValueIp_Object((1,3,6,1,4,1,1271,2,1,7,1,6,1,1,9),_CienaCesDpTrafficClassTermStartValueIp_Type())
cienaCesDpTrafficClassTermStartValueIp.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesDpTrafficClassTermStartValueIp.setStatus(_A)
class _CienaCesDpTrafficClassTermMaskValueIp_Type(IpAddress):defaultHexValue='00000000'
_CienaCesDpTrafficClassTermMaskValueIp_Type.__name__=_i
_CienaCesDpTrafficClassTermMaskValueIp_Object=MibTableColumn
cienaCesDpTrafficClassTermMaskValueIp=_CienaCesDpTrafficClassTermMaskValueIp_Object((1,3,6,1,4,1,1271,2,1,7,1,6,1,1,10),_CienaCesDpTrafficClassTermMaskValueIp_Type())
cienaCesDpTrafficClassTermMaskValueIp.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesDpTrafficClassTermMaskValueIp.setStatus(_A)
_CienaCesDpSubPort_ObjectIdentity=ObjectIdentity
cienaCesDpSubPort=_CienaCesDpSubPort_ObjectIdentity((1,3,6,1,4,1,1271,2,1,7,1,7))
_CienaCesDpSubPortTable_Object=MibTable
cienaCesDpSubPortTable=_CienaCesDpSubPortTable_Object((1,3,6,1,4,1,1271,2,1,7,1,7,1))
if mibBuilder.loadTexts:cienaCesDpSubPortTable.setStatus(_A)
_CienaCesDpSubPortEntry_Object=MibTableRow
cienaCesDpSubPortEntry=_CienaCesDpSubPortEntry_Object((1,3,6,1,4,1,1271,2,1,7,1,7,1,1))
cienaCesDpSubPortEntry.setIndexNames((0,_C,_a))
if mibBuilder.loadTexts:cienaCesDpSubPortEntry.setStatus(_A)
class _CienaCesDpSubPortLiIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,16777215))
_CienaCesDpSubPortLiIndex_Type.__name__=_D
_CienaCesDpSubPortLiIndex_Object=MibTableColumn
cienaCesDpSubPortLiIndex=_CienaCesDpSubPortLiIndex_Object((1,3,6,1,4,1,1271,2,1,7,1,7,1,1,1),_CienaCesDpSubPortLiIndex_Type())
cienaCesDpSubPortLiIndex.setMaxAccess(_W)
if mibBuilder.loadTexts:cienaCesDpSubPortLiIndex.setStatus(_A)
_CienaCesDpSubPortName_Type=DisplayString
_CienaCesDpSubPortName_Object=MibTableColumn
cienaCesDpSubPortName=_CienaCesDpSubPortName_Object((1,3,6,1,4,1,1271,2,1,7,1,7,1,1,2),_CienaCesDpSubPortName_Type())
cienaCesDpSubPortName.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesDpSubPortName.setStatus(_A)
_CienaCesDpSubPortClassifierPrecedence_Type=Unsigned32
_CienaCesDpSubPortClassifierPrecedence_Object=MibTableColumn
cienaCesDpSubPortClassifierPrecedence=_CienaCesDpSubPortClassifierPrecedence_Object((1,3,6,1,4,1,1271,2,1,7,1,7,1,1,3),_CienaCesDpSubPortClassifierPrecedence_Type())
cienaCesDpSubPortClassifierPrecedence.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesDpSubPortClassifierPrecedence.setStatus(_A)
_CienaCesDpSubPortParentIfId_Type=Integer32
_CienaCesDpSubPortParentIfId_Object=MibTableColumn
cienaCesDpSubPortParentIfId=_CienaCesDpSubPortParentIfId_Object((1,3,6,1,4,1,1271,2,1,7,1,7,1,1,4),_CienaCesDpSubPortParentIfId_Type())
cienaCesDpSubPortParentIfId.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesDpSubPortParentIfId.setStatus(_A)
class _CienaCesDpSubPortVirtualSwitchIndex_Type(Integer32):defaultValue=0
_CienaCesDpSubPortVirtualSwitchIndex_Type.__name__=_D
_CienaCesDpSubPortVirtualSwitchIndex_Object=MibTableColumn
cienaCesDpSubPortVirtualSwitchIndex=_CienaCesDpSubPortVirtualSwitchIndex_Object((1,3,6,1,4,1,1271,2,1,7,1,7,1,1,5),_CienaCesDpSubPortVirtualSwitchIndex_Type())
cienaCesDpSubPortVirtualSwitchIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesDpSubPortVirtualSwitchIndex.setStatus(_A)
class _CienaCesDpSubPortRlanIndex_Type(Integer32):defaultValue=0
_CienaCesDpSubPortRlanIndex_Type.__name__=_D
_CienaCesDpSubPortRlanIndex_Object=MibTableColumn
cienaCesDpSubPortRlanIndex=_CienaCesDpSubPortRlanIndex_Object((1,3,6,1,4,1,1271,2,1,7,1,7,1,1,6),_CienaCesDpSubPortRlanIndex_Type())
cienaCesDpSubPortRlanIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesDpSubPortRlanIndex.setStatus(_A)
_CienaCesDpSubPortVirtualSwitchName_Type=OctetString
_CienaCesDpSubPortVirtualSwitchName_Object=MibTableColumn
cienaCesDpSubPortVirtualSwitchName=_CienaCesDpSubPortVirtualSwitchName_Object((1,3,6,1,4,1,1271,2,1,7,1,7,1,1,7),_CienaCesDpSubPortVirtualSwitchName_Type())
cienaCesDpSubPortVirtualSwitchName.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesDpSubPortVirtualSwitchName.setStatus(_A)
_CienaCesDpSubPortIngressMeterProfileId_Type=Integer32
_CienaCesDpSubPortIngressMeterProfileId_Object=MibTableColumn
cienaCesDpSubPortIngressMeterProfileId=_CienaCesDpSubPortIngressMeterProfileId_Object((1,3,6,1,4,1,1271,2,1,7,1,7,1,1,8),_CienaCesDpSubPortIngressMeterProfileId_Type())
cienaCesDpSubPortIngressMeterProfileId.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesDpSubPortIngressMeterProfileId.setStatus(_A)
_CienaCesDpSubPortIngressMeterProfileName_Type=OctetString
_CienaCesDpSubPortIngressMeterProfileName_Object=MibTableColumn
cienaCesDpSubPortIngressMeterProfileName=_CienaCesDpSubPortIngressMeterProfileName_Object((1,3,6,1,4,1,1271,2,1,7,1,7,1,1,9),_CienaCesDpSubPortIngressMeterProfileName_Type())
cienaCesDpSubPortIngressMeterProfileName.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesDpSubPortIngressMeterProfileName.setStatus(_A)
class _CienaCesDpSubportIngressMeterPolicy_Type(DpIngressMeterPolicy):defaultValue=1
_CienaCesDpSubportIngressMeterPolicy_Type.__name__=_b
_CienaCesDpSubportIngressMeterPolicy_Object=MibTableColumn
cienaCesDpSubportIngressMeterPolicy=_CienaCesDpSubportIngressMeterPolicy_Object((1,3,6,1,4,1,1271,2,1,7,1,7,1,1,10),_CienaCesDpSubportIngressMeterPolicy_Type())
cienaCesDpSubportIngressMeterPolicy.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesDpSubportIngressMeterPolicy.setStatus(_A)
_CienaCesDpSubPortIngressFloodContainerId_Type=Integer32
_CienaCesDpSubPortIngressFloodContainerId_Object=MibTableColumn
cienaCesDpSubPortIngressFloodContainerId=_CienaCesDpSubPortIngressFloodContainerId_Object((1,3,6,1,4,1,1271,2,1,7,1,7,1,1,11),_CienaCesDpSubPortIngressFloodContainerId_Type())
cienaCesDpSubPortIngressFloodContainerId.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesDpSubPortIngressFloodContainerId.setStatus(_A)
_CienaCesDpSubPortIngressFloodContainerName_Type=OctetString
_CienaCesDpSubPortIngressFloodContainerName_Object=MibTableColumn
cienaCesDpSubPortIngressFloodContainerName=_CienaCesDpSubPortIngressFloodContainerName_Object((1,3,6,1,4,1,1271,2,1,7,1,7,1,1,12),_CienaCesDpSubPortIngressFloodContainerName_Type())
cienaCesDpSubPortIngressFloodContainerName.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesDpSubPortIngressFloodContainerName.setStatus(_A)
_CienaCesDpSubPortIngressRcosProfileId_Type=Integer32
_CienaCesDpSubPortIngressRcosProfileId_Object=MibTableColumn
cienaCesDpSubPortIngressRcosProfileId=_CienaCesDpSubPortIngressRcosProfileId_Object((1,3,6,1,4,1,1271,2,1,7,1,7,1,1,13),_CienaCesDpSubPortIngressRcosProfileId_Type())
cienaCesDpSubPortIngressRcosProfileId.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesDpSubPortIngressRcosProfileId.setStatus(_A)
_CienaCesDpSubPortIngressRcosProfileName_Type=OctetString
_CienaCesDpSubPortIngressRcosProfileName_Object=MibTableColumn
cienaCesDpSubPortIngressRcosProfileName=_CienaCesDpSubPortIngressRcosProfileName_Object((1,3,6,1,4,1,1271,2,1,7,1,7,1,1,14),_CienaCesDpSubPortIngressRcosProfileName_Type())
cienaCesDpSubPortIngressRcosProfileName.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesDpSubPortIngressRcosProfileName.setStatus(_A)
class _CienaCesDpSubPortIngressRcosPolicy_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*((_t,1),(_u,2),(_AW,3),(_AX,4),(_AY,5),(_AZ,6)))
_CienaCesDpSubPortIngressRcosPolicy_Type.__name__=_D
_CienaCesDpSubPortIngressRcosPolicy_Object=MibTableColumn
cienaCesDpSubPortIngressRcosPolicy=_CienaCesDpSubPortIngressRcosPolicy_Object((1,3,6,1,4,1,1271,2,1,7,1,7,1,1,15),_CienaCesDpSubPortIngressRcosPolicy_Type())
cienaCesDpSubPortIngressRcosPolicy.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesDpSubPortIngressRcosPolicy.setStatus(_A)
class _CienaCesDpSubPortIngressFcosMapId_Type(Integer32):defaultValue=0
_CienaCesDpSubPortIngressFcosMapId_Type.__name__=_D
_CienaCesDpSubPortIngressFcosMapId_Object=MibTableColumn
cienaCesDpSubPortIngressFcosMapId=_CienaCesDpSubPortIngressFcosMapId_Object((1,3,6,1,4,1,1271,2,1,7,1,7,1,1,16),_CienaCesDpSubPortIngressFcosMapId_Type())
cienaCesDpSubPortIngressFcosMapId.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesDpSubPortIngressFcosMapId.setStatus(_A)
_CienaCesDpSubPortIngressFcosMapName_Type=OctetString
_CienaCesDpSubPortIngressFcosMapName_Object=MibTableColumn
cienaCesDpSubPortIngressFcosMapName=_CienaCesDpSubPortIngressFcosMapName_Object((1,3,6,1,4,1,1271,2,1,7,1,7,1,1,17),_CienaCesDpSubPortIngressFcosMapName_Type())
cienaCesDpSubPortIngressFcosMapName.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesDpSubPortIngressFcosMapName.setStatus(_A)
class _CienaCesDpSubPortEgressFcosMapId_Type(Integer32):defaultValue=0
_CienaCesDpSubPortEgressFcosMapId_Type.__name__=_D
_CienaCesDpSubPortEgressFcosMapId_Object=MibTableColumn
cienaCesDpSubPortEgressFcosMapId=_CienaCesDpSubPortEgressFcosMapId_Object((1,3,6,1,4,1,1271,2,1,7,1,7,1,1,18),_CienaCesDpSubPortEgressFcosMapId_Type())
cienaCesDpSubPortEgressFcosMapId.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesDpSubPortEgressFcosMapId.setStatus(_A)
_CienaCesDpSubPortEgressFcosMapName_Type=OctetString
_CienaCesDpSubPortEgressFcosMapName_Object=MibTableColumn
cienaCesDpSubPortEgressFcosMapName=_CienaCesDpSubPortEgressFcosMapName_Object((1,3,6,1,4,1,1271,2,1,7,1,7,1,1,19),_CienaCesDpSubPortEgressFcosMapName_Type())
cienaCesDpSubPortEgressFcosMapName.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesDpSubPortEgressFcosMapName.setStatus(_A)
class _CienaCesDpSubPortEgressL2PtTransform_Type(TruthValue):defaultValue=2
_CienaCesDpSubPortEgressL2PtTransform_Type.__name__=_z
_CienaCesDpSubPortEgressL2PtTransform_Object=MibTableColumn
cienaCesDpSubPortEgressL2PtTransform=_CienaCesDpSubPortEgressL2PtTransform_Object((1,3,6,1,4,1,1271,2,1,7,1,7,1,1,20),_CienaCesDpSubPortEgressL2PtTransform_Type())
cienaCesDpSubPortEgressL2PtTransform.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesDpSubPortEgressL2PtTransform.setStatus(_A)
_CienaCesDpSubPortIngressL2Transform_Type=OctetString
_CienaCesDpSubPortIngressL2Transform_Object=MibTableColumn
cienaCesDpSubPortIngressL2Transform=_CienaCesDpSubPortIngressL2Transform_Object((1,3,6,1,4,1,1271,2,1,7,1,7,1,1,21),_CienaCesDpSubPortIngressL2Transform_Type())
cienaCesDpSubPortIngressL2Transform.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesDpSubPortIngressL2Transform.setStatus(_A)
_CienaCesDpSubPortEgressL2Transform_Type=OctetString
_CienaCesDpSubPortEgressL2Transform_Object=MibTableColumn
cienaCesDpSubPortEgressL2Transform=_CienaCesDpSubPortEgressL2Transform_Object((1,3,6,1,4,1,1271,2,1,7,1,7,1,1,22),_CienaCesDpSubPortEgressL2Transform_Type())
cienaCesDpSubPortEgressL2Transform.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesDpSubPortEgressL2Transform.setStatus(_A)
class _CienaCesDpSubPortIngressL3TransformPolicy_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_v,1),(_w,2)))
_CienaCesDpSubPortIngressL3TransformPolicy_Type.__name__=_D
_CienaCesDpSubPortIngressL3TransformPolicy_Object=MibTableColumn
cienaCesDpSubPortIngressL3TransformPolicy=_CienaCesDpSubPortIngressL3TransformPolicy_Object((1,3,6,1,4,1,1271,2,1,7,1,7,1,1,23),_CienaCesDpSubPortIngressL3TransformPolicy_Type())
cienaCesDpSubPortIngressL3TransformPolicy.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesDpSubPortIngressL3TransformPolicy.setStatus(_A)
class _CienaCesDpSubPortEgressL3TransformPolicy_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_v,1),(_w,2)))
_CienaCesDpSubPortEgressL3TransformPolicy_Type.__name__=_D
_CienaCesDpSubPortEgressL3TransformPolicy_Object=MibTableColumn
cienaCesDpSubPortEgressL3TransformPolicy=_CienaCesDpSubPortEgressL3TransformPolicy_Object((1,3,6,1,4,1,1271,2,1,7,1,7,1,1,24),_CienaCesDpSubPortEgressL3TransformPolicy_Type())
cienaCesDpSubPortEgressL3TransformPolicy.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesDpSubPortEgressL3TransformPolicy.setStatus(_A)
class _CienaCesDpSubPortPrivateFwdGroup_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('groupA',1),('groupB',2),('groupC',3)))
_CienaCesDpSubPortPrivateFwdGroup_Type.__name__=_D
_CienaCesDpSubPortPrivateFwdGroup_Object=MibTableColumn
cienaCesDpSubPortPrivateFwdGroup=_CienaCesDpSubPortPrivateFwdGroup_Object((1,3,6,1,4,1,1271,2,1,7,1,7,1,1,25),_CienaCesDpSubPortPrivateFwdGroup_Type())
cienaCesDpSubPortPrivateFwdGroup.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesDpSubPortPrivateFwdGroup.setStatus(_A)
class _CienaCesDpSubPortFilterPolicy_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('allow',1),('deny',2)))
_CienaCesDpSubPortFilterPolicy_Type.__name__=_D
_CienaCesDpSubPortFilterPolicy_Object=MibTableColumn
cienaCesDpSubPortFilterPolicy=_CienaCesDpSubPortFilterPolicy_Object((1,3,6,1,4,1,1271,2,1,7,1,7,1,1,26),_CienaCesDpSubPortFilterPolicy_Type())
cienaCesDpSubPortFilterPolicy.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesDpSubPortFilterPolicy.setStatus(_A)
_CienaCesDpSubPortLogicalRingIndex_Type=Integer32
_CienaCesDpSubPortLogicalRingIndex_Object=MibTableColumn
cienaCesDpSubPortLogicalRingIndex=_CienaCesDpSubPortLogicalRingIndex_Object((1,3,6,1,4,1,1271,2,1,7,1,7,1,1,27),_CienaCesDpSubPortLogicalRingIndex_Type())
cienaCesDpSubPortLogicalRingIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesDpSubPortLogicalRingIndex.setStatus(_A)
_CienaCesDpSubPortVirtualRingIndex_Type=Integer32
_CienaCesDpSubPortVirtualRingIndex_Object=MibTableColumn
cienaCesDpSubPortVirtualRingIndex=_CienaCesDpSubPortVirtualRingIndex_Object((1,3,6,1,4,1,1271,2,1,7,1,7,1,1,28),_CienaCesDpSubPortVirtualRingIndex_Type())
cienaCesDpSubPortVirtualRingIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesDpSubPortVirtualRingIndex.setStatus(_A)
_CienaCesDpSubPortEgressReflectorMac_Type=MacAddress
_CienaCesDpSubPortEgressReflectorMac_Object=MibTableColumn
cienaCesDpSubPortEgressReflectorMac=_CienaCesDpSubPortEgressReflectorMac_Object((1,3,6,1,4,1,1271,2,1,7,1,7,1,1,29),_CienaCesDpSubPortEgressReflectorMac_Type())
cienaCesDpSubPortEgressReflectorMac.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesDpSubPortEgressReflectorMac.setStatus(_A)
_CienaCesDpSubPortEgressGeneratorMac_Type=MacAddress
_CienaCesDpSubPortEgressGeneratorMac_Object=MibTableColumn
cienaCesDpSubPortEgressGeneratorMac=_CienaCesDpSubPortEgressGeneratorMac_Object((1,3,6,1,4,1,1271,2,1,7,1,7,1,1,30),_CienaCesDpSubPortEgressGeneratorMac_Type())
cienaCesDpSubPortEgressGeneratorMac.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesDpSubPortEgressGeneratorMac.setStatus(_A)
_CienaCesDpSubPortQueueGroupProfileId_Type=Integer32
_CienaCesDpSubPortQueueGroupProfileId_Object=MibTableColumn
cienaCesDpSubPortQueueGroupProfileId=_CienaCesDpSubPortQueueGroupProfileId_Object((1,3,6,1,4,1,1271,2,1,7,1,7,1,1,31),_CienaCesDpSubPortQueueGroupProfileId_Type())
cienaCesDpSubPortQueueGroupProfileId.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesDpSubPortQueueGroupProfileId.setStatus(_A)
_CienaCesDpSubPortQueueGroupProfileName_Type=OctetString
_CienaCesDpSubPortQueueGroupProfileName_Object=MibTableColumn
cienaCesDpSubPortQueueGroupProfileName=_CienaCesDpSubPortQueueGroupProfileName_Object((1,3,6,1,4,1,1271,2,1,7,1,7,1,1,32),_CienaCesDpSubPortQueueGroupProfileName_Type())
cienaCesDpSubPortQueueGroupProfileName.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesDpSubPortQueueGroupProfileName.setStatus(_A)
_CienaCesDpSubPortQueueGroupInstanceId_Type=Integer32
_CienaCesDpSubPortQueueGroupInstanceId_Object=MibTableColumn
cienaCesDpSubPortQueueGroupInstanceId=_CienaCesDpSubPortQueueGroupInstanceId_Object((1,3,6,1,4,1,1271,2,1,7,1,7,1,1,33),_CienaCesDpSubPortQueueGroupInstanceId_Type())
cienaCesDpSubPortQueueGroupInstanceId.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesDpSubPortQueueGroupInstanceId.setStatus(_A)
_CienaCesDpVirtualSwitch_ObjectIdentity=ObjectIdentity
cienaCesDpVirtualSwitch=_CienaCesDpVirtualSwitch_ObjectIdentity((1,3,6,1,4,1,1271,2,1,7,1,8))
_CienaCesDpVirtualSwitchTable_Object=MibTable
cienaCesDpVirtualSwitchTable=_CienaCesDpVirtualSwitchTable_Object((1,3,6,1,4,1,1271,2,1,7,1,8,1))
if mibBuilder.loadTexts:cienaCesDpVirtualSwitchTable.setStatus(_A)
_CienaCesDpVirtualSwitchEntry_Object=MibTableRow
cienaCesDpVirtualSwitchEntry=_CienaCesDpVirtualSwitchEntry_Object((1,3,6,1,4,1,1271,2,1,7,1,8,1,1))
cienaCesDpVirtualSwitchEntry.setIndexNames((0,_C,_U))
if mibBuilder.loadTexts:cienaCesDpVirtualSwitchEntry.setStatus(_A)
class _CienaCesDpVirtualSwitchIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1048575))
_CienaCesDpVirtualSwitchIndex_Type.__name__=_D
_CienaCesDpVirtualSwitchIndex_Object=MibTableColumn
cienaCesDpVirtualSwitchIndex=_CienaCesDpVirtualSwitchIndex_Object((1,3,6,1,4,1,1271,2,1,7,1,8,1,1,1),_CienaCesDpVirtualSwitchIndex_Type())
cienaCesDpVirtualSwitchIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:cienaCesDpVirtualSwitchIndex.setStatus(_A)
class _CienaCesDpVirtualSwitchRlanIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4095))
_CienaCesDpVirtualSwitchRlanIndex_Type.__name__=_D
_CienaCesDpVirtualSwitchRlanIndex_Object=MibTableColumn
cienaCesDpVirtualSwitchRlanIndex=_CienaCesDpVirtualSwitchRlanIndex_Object((1,3,6,1,4,1,1271,2,1,7,1,8,1,1,2),_CienaCesDpVirtualSwitchRlanIndex_Type())
cienaCesDpVirtualSwitchRlanIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesDpVirtualSwitchRlanIndex.setStatus(_A)
_CienaCesDpVirtualSwitchRlanTable_Object=MibTable
cienaCesDpVirtualSwitchRlanTable=_CienaCesDpVirtualSwitchRlanTable_Object((1,3,6,1,4,1,1271,2,1,7,1,8,2))
if mibBuilder.loadTexts:cienaCesDpVirtualSwitchRlanTable.setStatus(_A)
_CienaCesDpVirtualSwitchRlanEntry_Object=MibTableRow
cienaCesDpVirtualSwitchRlanEntry=_CienaCesDpVirtualSwitchRlanEntry_Object((1,3,6,1,4,1,1271,2,1,7,1,8,2,1))
cienaCesDpVirtualSwitchRlanEntry.setIndexNames((0,_C,_U),(0,_C,_c))
if mibBuilder.loadTexts:cienaCesDpVirtualSwitchRlanEntry.setStatus(_A)
_CienaCesDpVirtualSwitchRlanName_Type=DisplayString
_CienaCesDpVirtualSwitchRlanName_Object=MibTableColumn
cienaCesDpVirtualSwitchRlanName=_CienaCesDpVirtualSwitchRlanName_Object((1,3,6,1,4,1,1271,2,1,7,1,8,2,1,1),_CienaCesDpVirtualSwitchRlanName_Type())
cienaCesDpVirtualSwitchRlanName.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesDpVirtualSwitchRlanName.setStatus(_A)
class _CienaCesDpVirtualSwitchRlanMcastForwardingMode_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('default',1),('l2Enhanced',2)))
_CienaCesDpVirtualSwitchRlanMcastForwardingMode_Type.__name__=_D
_CienaCesDpVirtualSwitchRlanMcastForwardingMode_Object=MibTableColumn
cienaCesDpVirtualSwitchRlanMcastForwardingMode=_CienaCesDpVirtualSwitchRlanMcastForwardingMode_Object((1,3,6,1,4,1,1271,2,1,7,1,8,2,1,2),_CienaCesDpVirtualSwitchRlanMcastForwardingMode_Type())
cienaCesDpVirtualSwitchRlanMcastForwardingMode.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesDpVirtualSwitchRlanMcastForwardingMode.setStatus(_A)
class _CienaCesDpVirtualSwitchRlanL2CftStatus_Type(CienaGlobalState):defaultValue=2
_CienaCesDpVirtualSwitchRlanL2CftStatus_Type.__name__=_V
_CienaCesDpVirtualSwitchRlanL2CftStatus_Object=MibTableColumn
cienaCesDpVirtualSwitchRlanL2CftStatus=_CienaCesDpVirtualSwitchRlanL2CftStatus_Object((1,3,6,1,4,1,1271,2,1,7,1,8,2,1,3),_CienaCesDpVirtualSwitchRlanL2CftStatus_Type())
cienaCesDpVirtualSwitchRlanL2CftStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesDpVirtualSwitchRlanL2CftStatus.setStatus(_A)
class _CienaCesDpVirtualSwitchRlanL2CftL2ControlRcos_Type(Integer32):defaultValue=48
_CienaCesDpVirtualSwitchRlanL2CftL2ControlRcos_Type.__name__=_D
_CienaCesDpVirtualSwitchRlanL2CftL2ControlRcos_Object=MibTableColumn
cienaCesDpVirtualSwitchRlanL2CftL2ControlRcos=_CienaCesDpVirtualSwitchRlanL2CftL2ControlRcos_Object((1,3,6,1,4,1,1271,2,1,7,1,8,2,1,4),_CienaCesDpVirtualSwitchRlanL2CftL2ControlRcos_Type())
cienaCesDpVirtualSwitchRlanL2CftL2ControlRcos.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesDpVirtualSwitchRlanL2CftL2ControlRcos.setStatus(_A)
class _CienaCesDpVirtualSwitchRlanMacLearningStatus_Type(CienaGlobalState):defaultValue=1
_CienaCesDpVirtualSwitchRlanMacLearningStatus_Type.__name__=_V
_CienaCesDpVirtualSwitchRlanMacLearningStatus_Object=MibTableColumn
cienaCesDpVirtualSwitchRlanMacLearningStatus=_CienaCesDpVirtualSwitchRlanMacLearningStatus_Object((1,3,6,1,4,1,1271,2,1,7,1,8,2,1,5),_CienaCesDpVirtualSwitchRlanMacLearningStatus_Type())
cienaCesDpVirtualSwitchRlanMacLearningStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesDpVirtualSwitchRlanMacLearningStatus.setStatus(_A)
class _CienaCesDpVirtualSwitchRlanPrivateFwdGroupStatus_Type(CienaGlobalState):defaultValue=2
_CienaCesDpVirtualSwitchRlanPrivateFwdGroupStatus_Type.__name__=_V
_CienaCesDpVirtualSwitchRlanPrivateFwdGroupStatus_Object=MibTableColumn
cienaCesDpVirtualSwitchRlanPrivateFwdGroupStatus=_CienaCesDpVirtualSwitchRlanPrivateFwdGroupStatus_Object((1,3,6,1,4,1,1271,2,1,7,1,8,2,1,6),_CienaCesDpVirtualSwitchRlanPrivateFwdGroupStatus_Type())
cienaCesDpVirtualSwitchRlanPrivateFwdGroupStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesDpVirtualSwitchRlanPrivateFwdGroupStatus.setStatus(_A)
class _CienaCesDpVirtualSwitchRlanPrivateFwdGroupAPolicy_Type(PrivateForwardGroupPolicy):defaultValue=7
_CienaCesDpVirtualSwitchRlanPrivateFwdGroupAPolicy_Type.__name__=_Q
_CienaCesDpVirtualSwitchRlanPrivateFwdGroupAPolicy_Object=MibTableColumn
cienaCesDpVirtualSwitchRlanPrivateFwdGroupAPolicy=_CienaCesDpVirtualSwitchRlanPrivateFwdGroupAPolicy_Object((1,3,6,1,4,1,1271,2,1,7,1,8,2,1,7),_CienaCesDpVirtualSwitchRlanPrivateFwdGroupAPolicy_Type())
cienaCesDpVirtualSwitchRlanPrivateFwdGroupAPolicy.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesDpVirtualSwitchRlanPrivateFwdGroupAPolicy.setStatus(_A)
class _CienaCesDpVirtualSwitchRlanPrivateFwdGroupBPolicy_Type(PrivateForwardGroupPolicy):defaultValue=7
_CienaCesDpVirtualSwitchRlanPrivateFwdGroupBPolicy_Type.__name__=_Q
_CienaCesDpVirtualSwitchRlanPrivateFwdGroupBPolicy_Object=MibTableColumn
cienaCesDpVirtualSwitchRlanPrivateFwdGroupBPolicy=_CienaCesDpVirtualSwitchRlanPrivateFwdGroupBPolicy_Object((1,3,6,1,4,1,1271,2,1,7,1,8,2,1,8),_CienaCesDpVirtualSwitchRlanPrivateFwdGroupBPolicy_Type())
cienaCesDpVirtualSwitchRlanPrivateFwdGroupBPolicy.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesDpVirtualSwitchRlanPrivateFwdGroupBPolicy.setStatus(_A)
class _CienaCesDpVirtualSwitchRlanPrivateFwdGroupCPolicy_Type(PrivateForwardGroupPolicy):defaultValue=7
_CienaCesDpVirtualSwitchRlanPrivateFwdGroupCPolicy_Type.__name__=_Q
_CienaCesDpVirtualSwitchRlanPrivateFwdGroupCPolicy_Object=MibTableColumn
cienaCesDpVirtualSwitchRlanPrivateFwdGroupCPolicy=_CienaCesDpVirtualSwitchRlanPrivateFwdGroupCPolicy_Object((1,3,6,1,4,1,1271,2,1,7,1,8,2,1,9),_CienaCesDpVirtualSwitchRlanPrivateFwdGroupCPolicy_Type())
cienaCesDpVirtualSwitchRlanPrivateFwdGroupCPolicy.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesDpVirtualSwitchRlanPrivateFwdGroupCPolicy.setStatus(_A)
_CienaCesDpVirtualSwitchRlanDescription_Type=DisplayString
_CienaCesDpVirtualSwitchRlanDescription_Object=MibTableColumn
cienaCesDpVirtualSwitchRlanDescription=_CienaCesDpVirtualSwitchRlanDescription_Object((1,3,6,1,4,1,1271,2,1,7,1,8,2,1,10),_CienaCesDpVirtualSwitchRlanDescription_Type())
cienaCesDpVirtualSwitchRlanDescription.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesDpVirtualSwitchRlanDescription.setStatus(_A)
_CienaCesDpVirtualSwitchRlanPfgProfileId_Type=Integer32
_CienaCesDpVirtualSwitchRlanPfgProfileId_Object=MibTableColumn
cienaCesDpVirtualSwitchRlanPfgProfileId=_CienaCesDpVirtualSwitchRlanPfgProfileId_Object((1,3,6,1,4,1,1271,2,1,7,1,8,2,1,11),_CienaCesDpVirtualSwitchRlanPfgProfileId_Type())
cienaCesDpVirtualSwitchRlanPfgProfileId.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesDpVirtualSwitchRlanPfgProfileId.setStatus(_A)
_CienaCesDpVirtualSwitchRlanPfgProfileName_Type=OctetString
_CienaCesDpVirtualSwitchRlanPfgProfileName_Object=MibTableColumn
cienaCesDpVirtualSwitchRlanPfgProfileName=_CienaCesDpVirtualSwitchRlanPfgProfileName_Object((1,3,6,1,4,1,1271,2,1,7,1,8,2,1,12),_CienaCesDpVirtualSwitchRlanPfgProfileName_Type())
cienaCesDpVirtualSwitchRlanPfgProfileName.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesDpVirtualSwitchRlanPfgProfileName.setStatus(_A)
_CienaCesDpVirtualSwitchRlanL2CftProfileId_Type=Integer32
_CienaCesDpVirtualSwitchRlanL2CftProfileId_Object=MibTableColumn
cienaCesDpVirtualSwitchRlanL2CftProfileId=_CienaCesDpVirtualSwitchRlanL2CftProfileId_Object((1,3,6,1,4,1,1271,2,1,7,1,8,2,1,13),_CienaCesDpVirtualSwitchRlanL2CftProfileId_Type())
cienaCesDpVirtualSwitchRlanL2CftProfileId.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesDpVirtualSwitchRlanL2CftProfileId.setStatus(_A)
_CienaCesDpVirtualSwitchRlanL2CftProfileName_Type=OctetString
_CienaCesDpVirtualSwitchRlanL2CftProfileName_Object=MibTableColumn
cienaCesDpVirtualSwitchRlanL2CftProfileName=_CienaCesDpVirtualSwitchRlanL2CftProfileName_Object((1,3,6,1,4,1,1271,2,1,7,1,8,2,1,14),_CienaCesDpVirtualSwitchRlanL2CftProfileName_Type())
cienaCesDpVirtualSwitchRlanL2CftProfileName.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesDpVirtualSwitchRlanL2CftProfileName.setStatus(_A)
class _CienaCesDpVirtualSwitchRlanLearnLimit_Type(Integer32):defaultValue=64000
_CienaCesDpVirtualSwitchRlanLearnLimit_Type.__name__=_D
_CienaCesDpVirtualSwitchRlanLearnLimit_Object=MibTableColumn
cienaCesDpVirtualSwitchRlanLearnLimit=_CienaCesDpVirtualSwitchRlanLearnLimit_Object((1,3,6,1,4,1,1271,2,1,7,1,8,2,1,15),_CienaCesDpVirtualSwitchRlanLearnLimit_Type())
cienaCesDpVirtualSwitchRlanLearnLimit.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesDpVirtualSwitchRlanLearnLimit.setStatus(_A)
_CienaCesDpVirtualSwitchRlanIfTable_Object=MibTable
cienaCesDpVirtualSwitchRlanIfTable=_CienaCesDpVirtualSwitchRlanIfTable_Object((1,3,6,1,4,1,1271,2,1,7,1,8,3))
if mibBuilder.loadTexts:cienaCesDpVirtualSwitchRlanIfTable.setStatus(_A)
_CienaCesDpVirtualSwitchRlanIfEntry_Object=MibTableRow
cienaCesDpVirtualSwitchRlanIfEntry=_CienaCesDpVirtualSwitchRlanIfEntry_Object((1,3,6,1,4,1,1271,2,1,7,1,8,3,1))
cienaCesDpVirtualSwitchRlanIfEntry.setIndexNames((0,_C,_U),(0,_C,_c),(0,_C,_Aa),(0,_C,_Ab))
if mibBuilder.loadTexts:cienaCesDpVirtualSwitchRlanIfEntry.setStatus(_A)
_CienaCesDpVirtualSwitchRlanIfLiType_Type=DpTsAttachType
_CienaCesDpVirtualSwitchRlanIfLiType_Object=MibTableColumn
cienaCesDpVirtualSwitchRlanIfLiType=_CienaCesDpVirtualSwitchRlanIfLiType_Object((1,3,6,1,4,1,1271,2,1,7,1,8,3,1,1),_CienaCesDpVirtualSwitchRlanIfLiType_Type())
cienaCesDpVirtualSwitchRlanIfLiType.setMaxAccess(_E)
if mibBuilder.loadTexts:cienaCesDpVirtualSwitchRlanIfLiType.setStatus(_A)
class _CienaCesDpVirtualSwitchRlanIfLiIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,16777215))
_CienaCesDpVirtualSwitchRlanIfLiIndex_Type.__name__=_D
_CienaCesDpVirtualSwitchRlanIfLiIndex_Object=MibTableColumn
cienaCesDpVirtualSwitchRlanIfLiIndex=_CienaCesDpVirtualSwitchRlanIfLiIndex_Object((1,3,6,1,4,1,1271,2,1,7,1,8,3,1,2),_CienaCesDpVirtualSwitchRlanIfLiIndex_Type())
cienaCesDpVirtualSwitchRlanIfLiIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:cienaCesDpVirtualSwitchRlanIfLiIndex.setStatus(_A)
_CienaCesDpVirtualSwitchRlanIfLportIngress_Type=Integer32
_CienaCesDpVirtualSwitchRlanIfLportIngress_Object=MibTableColumn
cienaCesDpVirtualSwitchRlanIfLportIngress=_CienaCesDpVirtualSwitchRlanIfLportIngress_Object((1,3,6,1,4,1,1271,2,1,7,1,8,3,1,3),_CienaCesDpVirtualSwitchRlanIfLportIngress_Type())
cienaCesDpVirtualSwitchRlanIfLportIngress.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesDpVirtualSwitchRlanIfLportIngress.setStatus(_A)
_CienaCesDpVirtualSwitchRlanIfLportEgress_Type=Integer32
_CienaCesDpVirtualSwitchRlanIfLportEgress_Object=MibTableColumn
cienaCesDpVirtualSwitchRlanIfLportEgress=_CienaCesDpVirtualSwitchRlanIfLportEgress_Object((1,3,6,1,4,1,1271,2,1,7,1,8,3,1,4),_CienaCesDpVirtualSwitchRlanIfLportEgress_Type())
cienaCesDpVirtualSwitchRlanIfLportEgress.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesDpVirtualSwitchRlanIfLportEgress.setStatus(_A)
_CienaCesDpVirtualSwitchRlanL2CftProtocolTable_Object=MibTable
cienaCesDpVirtualSwitchRlanL2CftProtocolTable=_CienaCesDpVirtualSwitchRlanL2CftProtocolTable_Object((1,3,6,1,4,1,1271,2,1,7,1,8,4))
if mibBuilder.loadTexts:cienaCesDpVirtualSwitchRlanL2CftProtocolTable.setStatus(_A)
_CienaCesDpVirtualSwitchRlanL2CftProtocolEntry_Object=MibTableRow
cienaCesDpVirtualSwitchRlanL2CftProtocolEntry=_CienaCesDpVirtualSwitchRlanL2CftProtocolEntry_Object((1,3,6,1,4,1,1271,2,1,7,1,8,4,1))
cienaCesDpVirtualSwitchRlanL2CftProtocolEntry.setIndexNames((0,_C,_U),(0,_C,_c),(0,_C,_Ac))
if mibBuilder.loadTexts:cienaCesDpVirtualSwitchRlanL2CftProtocolEntry.setStatus(_A)
class _CienaCesDpVirtualSwitchRlanL2CftProtocolType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21)));namedValues=NamedValues(*((_R,0),('ciscoCdp',1),('ciscoDtp',2),(_Ad,3),(_Ae,4),('ciscoVtp',5),(_Af,6),(_Ag,7),(_Ah,8),('rstp',9),('lacp',10),(_Ai,11),('oam',12),('lldp',13),('i8021x',14),('gmrp',15),('gvrp',16),(_Aj,17),(_Ak,18),(_Al,19),('elmi',20),('ptpPeerDelay',21)))
_CienaCesDpVirtualSwitchRlanL2CftProtocolType_Type.__name__=_D
_CienaCesDpVirtualSwitchRlanL2CftProtocolType_Object=MibTableColumn
cienaCesDpVirtualSwitchRlanL2CftProtocolType=_CienaCesDpVirtualSwitchRlanL2CftProtocolType_Object((1,3,6,1,4,1,1271,2,1,7,1,8,4,1,1),_CienaCesDpVirtualSwitchRlanL2CftProtocolType_Type())
cienaCesDpVirtualSwitchRlanL2CftProtocolType.setMaxAccess(_E)
if mibBuilder.loadTexts:cienaCesDpVirtualSwitchRlanL2CftProtocolType.setStatus(_A)
class _CienaCesDpVirtualSwitchRlanL2CftProtocolDisposition_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('forward',1),('discard',2)))
_CienaCesDpVirtualSwitchRlanL2CftProtocolDisposition_Type.__name__=_D
_CienaCesDpVirtualSwitchRlanL2CftProtocolDisposition_Object=MibTableColumn
cienaCesDpVirtualSwitchRlanL2CftProtocolDisposition=_CienaCesDpVirtualSwitchRlanL2CftProtocolDisposition_Object((1,3,6,1,4,1,1271,2,1,7,1,8,4,1,2),_CienaCesDpVirtualSwitchRlanL2CftProtocolDisposition_Type())
cienaCesDpVirtualSwitchRlanL2CftProtocolDisposition.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesDpVirtualSwitchRlanL2CftProtocolDisposition.setStatus(_A)
_CienaCesDpQosFlow_ObjectIdentity=ObjectIdentity
cienaCesDpQosFlow=_CienaCesDpQosFlow_ObjectIdentity((1,3,6,1,4,1,1271,2,1,7,1,9))
_CienaCesDpQosFlowTable_Object=MibTable
cienaCesDpQosFlowTable=_CienaCesDpQosFlowTable_Object((1,3,6,1,4,1,1271,2,1,7,1,9,1))
if mibBuilder.loadTexts:cienaCesDpQosFlowTable.setStatus(_A)
_CienaCesDpQosFlowEntry_Object=MibTableRow
cienaCesDpQosFlowEntry=_CienaCesDpQosFlowEntry_Object((1,3,6,1,4,1,1271,2,1,7,1,9,1,1))
cienaCesDpQosFlowEntry.setIndexNames((0,_C,_Am))
if mibBuilder.loadTexts:cienaCesDpQosFlowEntry.setStatus(_A)
class _CienaCesDpQosFlowLiIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,16777215))
_CienaCesDpQosFlowLiIndex_Type.__name__=_D
_CienaCesDpQosFlowLiIndex_Object=MibTableColumn
cienaCesDpQosFlowLiIndex=_CienaCesDpQosFlowLiIndex_Object((1,3,6,1,4,1,1271,2,1,7,1,9,1,1,1),_CienaCesDpQosFlowLiIndex_Type())
cienaCesDpQosFlowLiIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:cienaCesDpQosFlowLiIndex.setStatus(_A)
_CienaCesDpQosFlowName_Type=DisplayString
_CienaCesDpQosFlowName_Object=MibTableColumn
cienaCesDpQosFlowName=_CienaCesDpQosFlowName_Object((1,3,6,1,4,1,1271,2,1,7,1,9,1,1,2),_CienaCesDpQosFlowName_Type())
cienaCesDpQosFlowName.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesDpQosFlowName.setStatus(_A)
_CienaCesDpQosFlowClassifierPrecedence_Type=Unsigned32
_CienaCesDpQosFlowClassifierPrecedence_Object=MibTableColumn
cienaCesDpQosFlowClassifierPrecedence=_CienaCesDpQosFlowClassifierPrecedence_Object((1,3,6,1,4,1,1271,2,1,7,1,9,1,1,3),_CienaCesDpQosFlowClassifierPrecedence_Type())
cienaCesDpQosFlowClassifierPrecedence.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesDpQosFlowClassifierPrecedence.setStatus(_A)
_CienaCesDpQosFlowParentIfId_Type=Integer32
_CienaCesDpQosFlowParentIfId_Object=MibTableColumn
cienaCesDpQosFlowParentIfId=_CienaCesDpQosFlowParentIfId_Object((1,3,6,1,4,1,1271,2,1,7,1,9,1,1,4),_CienaCesDpQosFlowParentIfId_Type())
cienaCesDpQosFlowParentIfId.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesDpQosFlowParentIfId.setStatus(_A)
_CienaCesDpQosFlowParentIfType_Type=DpTsAttachType
_CienaCesDpQosFlowParentIfType_Object=MibTableColumn
cienaCesDpQosFlowParentIfType=_CienaCesDpQosFlowParentIfType_Object((1,3,6,1,4,1,1271,2,1,7,1,9,1,1,5),_CienaCesDpQosFlowParentIfType_Type())
cienaCesDpQosFlowParentIfType.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesDpQosFlowParentIfType.setStatus(_A)
_CienaCesDpQosFlowIngressMeterProfileId_Type=Integer32
_CienaCesDpQosFlowIngressMeterProfileId_Object=MibTableColumn
cienaCesDpQosFlowIngressMeterProfileId=_CienaCesDpQosFlowIngressMeterProfileId_Object((1,3,6,1,4,1,1271,2,1,7,1,9,1,1,6),_CienaCesDpQosFlowIngressMeterProfileId_Type())
cienaCesDpQosFlowIngressMeterProfileId.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesDpQosFlowIngressMeterProfileId.setStatus(_A)
_CienaCesDpQosFlowIngressMeterProfileName_Type=OctetString
_CienaCesDpQosFlowIngressMeterProfileName_Object=MibTableColumn
cienaCesDpQosFlowIngressMeterProfileName=_CienaCesDpQosFlowIngressMeterProfileName_Object((1,3,6,1,4,1,1271,2,1,7,1,9,1,1,7),_CienaCesDpQosFlowIngressMeterProfileName_Type())
cienaCesDpQosFlowIngressMeterProfileName.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesDpQosFlowIngressMeterProfileName.setStatus(_A)
class _CienaCesDpQosFlowIngressMeterPolicy_Type(DpIngressMeterPolicy):defaultValue=1
_CienaCesDpQosFlowIngressMeterPolicy_Type.__name__=_b
_CienaCesDpQosFlowIngressMeterPolicy_Object=MibTableColumn
cienaCesDpQosFlowIngressMeterPolicy=_CienaCesDpQosFlowIngressMeterPolicy_Object((1,3,6,1,4,1,1271,2,1,7,1,9,1,1,8),_CienaCesDpQosFlowIngressMeterPolicy_Type())
cienaCesDpQosFlowIngressMeterPolicy.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesDpQosFlowIngressMeterPolicy.setStatus(_A)
_CienaCesDpQosFlowIngressRcosProfileId_Type=Integer32
_CienaCesDpQosFlowIngressRcosProfileId_Object=MibTableColumn
cienaCesDpQosFlowIngressRcosProfileId=_CienaCesDpQosFlowIngressRcosProfileId_Object((1,3,6,1,4,1,1271,2,1,7,1,9,1,1,9),_CienaCesDpQosFlowIngressRcosProfileId_Type())
cienaCesDpQosFlowIngressRcosProfileId.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesDpQosFlowIngressRcosProfileId.setStatus(_A)
_CienaCesDpQosFlowIngressRcosProfileName_Type=OctetString
_CienaCesDpQosFlowIngressRcosProfileName_Object=MibTableColumn
cienaCesDpQosFlowIngressRcosProfileName=_CienaCesDpQosFlowIngressRcosProfileName_Object((1,3,6,1,4,1,1271,2,1,7,1,9,1,1,10),_CienaCesDpQosFlowIngressRcosProfileName_Type())
cienaCesDpQosFlowIngressRcosProfileName.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesDpQosFlowIngressRcosProfileName.setStatus(_A)
class _CienaCesDpQosFlowIngressRcosPolicy_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*((_t,1),(_u,2),(_AW,3),(_AX,4),(_AY,5),(_AZ,6)))
_CienaCesDpQosFlowIngressRcosPolicy_Type.__name__=_D
_CienaCesDpQosFlowIngressRcosPolicy_Object=MibTableColumn
cienaCesDpQosFlowIngressRcosPolicy=_CienaCesDpQosFlowIngressRcosPolicy_Object((1,3,6,1,4,1,1271,2,1,7,1,9,1,1,11),_CienaCesDpQosFlowIngressRcosPolicy_Type())
cienaCesDpQosFlowIngressRcosPolicy.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesDpQosFlowIngressRcosPolicy.setStatus(_A)
_CienaCesDpAccessFlow_ObjectIdentity=ObjectIdentity
cienaCesDpAccessFlow=_CienaCesDpAccessFlow_ObjectIdentity((1,3,6,1,4,1,1271,2,1,7,1,10))
_CienaCesDpAccessFlowTable_Object=MibTable
cienaCesDpAccessFlowTable=_CienaCesDpAccessFlowTable_Object((1,3,6,1,4,1,1271,2,1,7,1,10,1))
if mibBuilder.loadTexts:cienaCesDpAccessFlowTable.setStatus(_A)
_CienaCesDpAccessFlowEntry_Object=MibTableRow
cienaCesDpAccessFlowEntry=_CienaCesDpAccessFlowEntry_Object((1,3,6,1,4,1,1271,2,1,7,1,10,1,1))
cienaCesDpAccessFlowEntry.setIndexNames((0,_C,_An))
if mibBuilder.loadTexts:cienaCesDpAccessFlowEntry.setStatus(_A)
class _CienaCesDpAccessFlowLiIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,16777215))
_CienaCesDpAccessFlowLiIndex_Type.__name__=_D
_CienaCesDpAccessFlowLiIndex_Object=MibTableColumn
cienaCesDpAccessFlowLiIndex=_CienaCesDpAccessFlowLiIndex_Object((1,3,6,1,4,1,1271,2,1,7,1,10,1,1,1),_CienaCesDpAccessFlowLiIndex_Type())
cienaCesDpAccessFlowLiIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:cienaCesDpAccessFlowLiIndex.setStatus(_A)
_CienaCesDpAccessFlowName_Type=DisplayString
_CienaCesDpAccessFlowName_Object=MibTableColumn
cienaCesDpAccessFlowName=_CienaCesDpAccessFlowName_Object((1,3,6,1,4,1,1271,2,1,7,1,10,1,1,2),_CienaCesDpAccessFlowName_Type())
cienaCesDpAccessFlowName.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesDpAccessFlowName.setStatus(_A)
_CienaCesDpAccessFlowClassifierPrecedence_Type=Unsigned32
_CienaCesDpAccessFlowClassifierPrecedence_Object=MibTableColumn
cienaCesDpAccessFlowClassifierPrecedence=_CienaCesDpAccessFlowClassifierPrecedence_Object((1,3,6,1,4,1,1271,2,1,7,1,10,1,1,3),_CienaCesDpAccessFlowClassifierPrecedence_Type())
cienaCesDpAccessFlowClassifierPrecedence.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesDpAccessFlowClassifierPrecedence.setStatus(_A)
_CienaCesDpAccessFlowParentIfId_Type=Integer32
_CienaCesDpAccessFlowParentIfId_Object=MibTableColumn
cienaCesDpAccessFlowParentIfId=_CienaCesDpAccessFlowParentIfId_Object((1,3,6,1,4,1,1271,2,1,7,1,10,1,1,4),_CienaCesDpAccessFlowParentIfId_Type())
cienaCesDpAccessFlowParentIfId.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesDpAccessFlowParentIfId.setStatus(_A)
_CienaCesDpAccessFlowParentIfType_Type=DpTsAttachType
_CienaCesDpAccessFlowParentIfType_Object=MibTableColumn
cienaCesDpAccessFlowParentIfType=_CienaCesDpAccessFlowParentIfType_Object((1,3,6,1,4,1,1271,2,1,7,1,10,1,1,5),_CienaCesDpAccessFlowParentIfType_Type())
cienaCesDpAccessFlowParentIfType.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesDpAccessFlowParentIfType.setStatus(_A)
class _CienaCesDpAccessFlowFilterPolicy_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('allow',1),('deny',2),('l2ptmactranslation',3)))
_CienaCesDpAccessFlowFilterPolicy_Type.__name__=_D
_CienaCesDpAccessFlowFilterPolicy_Object=MibTableColumn
cienaCesDpAccessFlowFilterPolicy=_CienaCesDpAccessFlowFilterPolicy_Object((1,3,6,1,4,1,1271,2,1,7,1,10,1,1,6),_CienaCesDpAccessFlowFilterPolicy_Type())
cienaCesDpAccessFlowFilterPolicy.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesDpAccessFlowFilterPolicy.setStatus(_A)
_CienaCesDpPbtTransit_ObjectIdentity=ObjectIdentity
cienaCesDpPbtTransit=_CienaCesDpPbtTransit_ObjectIdentity((1,3,6,1,4,1,1271,2,1,7,1,11))
_CienaCesDpPbtTransitTable_Object=MibTable
cienaCesDpPbtTransitTable=_CienaCesDpPbtTransitTable_Object((1,3,6,1,4,1,1271,2,1,7,1,11,1))
if mibBuilder.loadTexts:cienaCesDpPbtTransitTable.setStatus(_A)
_CienaCesDpPbtTransitEntry_Object=MibTableRow
cienaCesDpPbtTransitEntry=_CienaCesDpPbtTransitEntry_Object((1,3,6,1,4,1,1271,2,1,7,1,11,1,1))
cienaCesDpPbtTransitEntry.setIndexNames((0,_C,_Ao))
if mibBuilder.loadTexts:cienaCesDpPbtTransitEntry.setStatus(_A)
class _CienaCesDpPbtTransitLiIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,16777215))
_CienaCesDpPbtTransitLiIndex_Type.__name__=_D
_CienaCesDpPbtTransitLiIndex_Object=MibTableColumn
cienaCesDpPbtTransitLiIndex=_CienaCesDpPbtTransitLiIndex_Object((1,3,6,1,4,1,1271,2,1,7,1,11,1,1,1),_CienaCesDpPbtTransitLiIndex_Type())
cienaCesDpPbtTransitLiIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:cienaCesDpPbtTransitLiIndex.setStatus(_A)
_CienaCesDpPbtTransitName_Type=DisplayString
_CienaCesDpPbtTransitName_Object=MibTableColumn
cienaCesDpPbtTransitName=_CienaCesDpPbtTransitName_Object((1,3,6,1,4,1,1271,2,1,7,1,11,1,1,2),_CienaCesDpPbtTransitName_Type())
cienaCesDpPbtTransitName.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesDpPbtTransitName.setStatus(_A)
_CienaCesDpPbtTransitParentIfId_Type=Integer32
_CienaCesDpPbtTransitParentIfId_Object=MibTableColumn
cienaCesDpPbtTransitParentIfId=_CienaCesDpPbtTransitParentIfId_Object((1,3,6,1,4,1,1271,2,1,7,1,11,1,1,3),_CienaCesDpPbtTransitParentIfId_Type())
cienaCesDpPbtTransitParentIfId.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesDpPbtTransitParentIfId.setStatus(_A)
_CienaCesDpPbtTransitIngressMeterProfileId_Type=Integer32
_CienaCesDpPbtTransitIngressMeterProfileId_Object=MibTableColumn
cienaCesDpPbtTransitIngressMeterProfileId=_CienaCesDpPbtTransitIngressMeterProfileId_Object((1,3,6,1,4,1,1271,2,1,7,1,11,1,1,4),_CienaCesDpPbtTransitIngressMeterProfileId_Type())
cienaCesDpPbtTransitIngressMeterProfileId.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesDpPbtTransitIngressMeterProfileId.setStatus(_A)
_CienaCesDpPbtTransitIngressMeterProfileName_Type=OctetString
_CienaCesDpPbtTransitIngressMeterProfileName_Object=MibTableColumn
cienaCesDpPbtTransitIngressMeterProfileName=_CienaCesDpPbtTransitIngressMeterProfileName_Object((1,3,6,1,4,1,1271,2,1,7,1,11,1,1,5),_CienaCesDpPbtTransitIngressMeterProfileName_Type())
cienaCesDpPbtTransitIngressMeterProfileName.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesDpPbtTransitIngressMeterProfileName.setStatus(_A)
_CienaCesDpPbtTransitIngressFloodContainerId_Type=Integer32
_CienaCesDpPbtTransitIngressFloodContainerId_Object=MibTableColumn
cienaCesDpPbtTransitIngressFloodContainerId=_CienaCesDpPbtTransitIngressFloodContainerId_Object((1,3,6,1,4,1,1271,2,1,7,1,11,1,1,6),_CienaCesDpPbtTransitIngressFloodContainerId_Type())
cienaCesDpPbtTransitIngressFloodContainerId.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesDpPbtTransitIngressFloodContainerId.setStatus(_A)
_CienaCesDpPbtTransitIngressFloodContainerName_Type=OctetString
_CienaCesDpPbtTransitIngressFloodContainerName_Object=MibTableColumn
cienaCesDpPbtTransitIngressFloodContainerName=_CienaCesDpPbtTransitIngressFloodContainerName_Object((1,3,6,1,4,1,1271,2,1,7,1,11,1,1,7),_CienaCesDpPbtTransitIngressFloodContainerName_Type())
cienaCesDpPbtTransitIngressFloodContainerName.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesDpPbtTransitIngressFloodContainerName.setStatus(_A)
_CienaCesDpPbtTransitIngressRcosProfileId_Type=Integer32
_CienaCesDpPbtTransitIngressRcosProfileId_Object=MibTableColumn
cienaCesDpPbtTransitIngressRcosProfileId=_CienaCesDpPbtTransitIngressRcosProfileId_Object((1,3,6,1,4,1,1271,2,1,7,1,11,1,1,8),_CienaCesDpPbtTransitIngressRcosProfileId_Type())
cienaCesDpPbtTransitIngressRcosProfileId.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesDpPbtTransitIngressRcosProfileId.setStatus(_A)
_CienaCesDpPbtTransitIngressRcosProfileName_Type=OctetString
_CienaCesDpPbtTransitIngressRcosProfileName_Object=MibTableColumn
cienaCesDpPbtTransitIngressRcosProfileName=_CienaCesDpPbtTransitIngressRcosProfileName_Object((1,3,6,1,4,1,1271,2,1,7,1,11,1,1,9),_CienaCesDpPbtTransitIngressRcosProfileName_Type())
cienaCesDpPbtTransitIngressRcosProfileName.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesDpPbtTransitIngressRcosProfileName.setStatus(_A)
class _CienaCesDpPbtTransitIngressRcosPolicy_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_t,1),(_u,2),('bvidPcpToRcos',3)))
_CienaCesDpPbtTransitIngressRcosPolicy_Type.__name__=_D
_CienaCesDpPbtTransitIngressRcosPolicy_Object=MibTableColumn
cienaCesDpPbtTransitIngressRcosPolicy=_CienaCesDpPbtTransitIngressRcosPolicy_Object((1,3,6,1,4,1,1271,2,1,7,1,11,1,1,10),_CienaCesDpPbtTransitIngressRcosPolicy_Type())
cienaCesDpPbtTransitIngressRcosPolicy.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesDpPbtTransitIngressRcosPolicy.setStatus(_A)
class _CienaCesDpPbtTransitIngressFcosMapId_Type(Integer32):defaultValue=0
_CienaCesDpPbtTransitIngressFcosMapId_Type.__name__=_D
_CienaCesDpPbtTransitIngressFcosMapId_Object=MibTableColumn
cienaCesDpPbtTransitIngressFcosMapId=_CienaCesDpPbtTransitIngressFcosMapId_Object((1,3,6,1,4,1,1271,2,1,7,1,11,1,1,11),_CienaCesDpPbtTransitIngressFcosMapId_Type())
cienaCesDpPbtTransitIngressFcosMapId.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesDpPbtTransitIngressFcosMapId.setStatus(_A)
_CienaCesDpPbtTransitIngressFcosMapName_Type=OctetString
_CienaCesDpPbtTransitIngressFcosMapName_Object=MibTableColumn
cienaCesDpPbtTransitIngressFcosMapName=_CienaCesDpPbtTransitIngressFcosMapName_Object((1,3,6,1,4,1,1271,2,1,7,1,11,1,1,12),_CienaCesDpPbtTransitIngressFcosMapName_Type())
cienaCesDpPbtTransitIngressFcosMapName.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesDpPbtTransitIngressFcosMapName.setStatus(_A)
class _CienaCesDpPbtTransitEgressFcosMapId_Type(Integer32):defaultValue=0
_CienaCesDpPbtTransitEgressFcosMapId_Type.__name__=_D
_CienaCesDpPbtTransitEgressFcosMapId_Object=MibTableColumn
cienaCesDpPbtTransitEgressFcosMapId=_CienaCesDpPbtTransitEgressFcosMapId_Object((1,3,6,1,4,1,1271,2,1,7,1,11,1,1,13),_CienaCesDpPbtTransitEgressFcosMapId_Type())
cienaCesDpPbtTransitEgressFcosMapId.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesDpPbtTransitEgressFcosMapId.setStatus(_A)
_CienaCesDpPbtTransitEgressFcosMapName_Type=OctetString
_CienaCesDpPbtTransitEgressFcosMapName_Object=MibTableColumn
cienaCesDpPbtTransitEgressFcosMapName=_CienaCesDpPbtTransitEgressFcosMapName_Object((1,3,6,1,4,1,1271,2,1,7,1,11,1,1,14),_CienaCesDpPbtTransitEgressFcosMapName_Type())
cienaCesDpPbtTransitEgressFcosMapName.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesDpPbtTransitEgressFcosMapName.setStatus(_A)
_CienaCesDpPbtTransitIngressBvidTransform_Type=OctetString
_CienaCesDpPbtTransitIngressBvidTransform_Object=MibTableColumn
cienaCesDpPbtTransitIngressBvidTransform=_CienaCesDpPbtTransitIngressBvidTransform_Object((1,3,6,1,4,1,1271,2,1,7,1,11,1,1,15),_CienaCesDpPbtTransitIngressBvidTransform_Type())
cienaCesDpPbtTransitIngressBvidTransform.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesDpPbtTransitIngressBvidTransform.setStatus(_A)
_CienaCesDpPbtTransitEgressBvidTransform_Type=OctetString
_CienaCesDpPbtTransitEgressBvidTransform_Object=MibTableColumn
cienaCesDpPbtTransitEgressBvidTransform=_CienaCesDpPbtTransitEgressBvidTransform_Object((1,3,6,1,4,1,1271,2,1,7,1,11,1,1,16),_CienaCesDpPbtTransitEgressBvidTransform_Type())
cienaCesDpPbtTransitEgressBvidTransform.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesDpPbtTransitEgressBvidTransform.setStatus(_A)
class _CienaCesDpPbtTransitVirtualSwitchId_Type(Integer32):defaultValue=0
_CienaCesDpPbtTransitVirtualSwitchId_Type.__name__=_D
_CienaCesDpPbtTransitVirtualSwitchId_Object=MibTableColumn
cienaCesDpPbtTransitVirtualSwitchId=_CienaCesDpPbtTransitVirtualSwitchId_Object((1,3,6,1,4,1,1271,2,1,7,1,11,1,1,17),_CienaCesDpPbtTransitVirtualSwitchId_Type())
cienaCesDpPbtTransitVirtualSwitchId.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesDpPbtTransitVirtualSwitchId.setStatus(_A)
class _CienaCesDpPbtTransitRlanId_Type(Integer32):defaultValue=0
_CienaCesDpPbtTransitRlanId_Type.__name__=_D
_CienaCesDpPbtTransitRlanId_Object=MibTableColumn
cienaCesDpPbtTransitRlanId=_CienaCesDpPbtTransitRlanId_Object((1,3,6,1,4,1,1271,2,1,7,1,11,1,1,18),_CienaCesDpPbtTransitRlanId_Type())
cienaCesDpPbtTransitRlanId.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesDpPbtTransitRlanId.setStatus(_A)
_CienaCesDpPbtTransitVirtualSwitchName_Type=OctetString
_CienaCesDpPbtTransitVirtualSwitchName_Object=MibTableColumn
cienaCesDpPbtTransitVirtualSwitchName=_CienaCesDpPbtTransitVirtualSwitchName_Object((1,3,6,1,4,1,1271,2,1,7,1,11,1,1,19),_CienaCesDpPbtTransitVirtualSwitchName_Type())
cienaCesDpPbtTransitVirtualSwitchName.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesDpPbtTransitVirtualSwitchName.setStatus(_A)
class _CienaCesDpPbtTransitPrivateFwdGroup_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('groupA',1),('groupB',2),('groupC',3)))
_CienaCesDpPbtTransitPrivateFwdGroup_Type.__name__=_D
_CienaCesDpPbtTransitPrivateFwdGroup_Object=MibTableColumn
cienaCesDpPbtTransitPrivateFwdGroup=_CienaCesDpPbtTransitPrivateFwdGroup_Object((1,3,6,1,4,1,1271,2,1,7,1,11,1,1,20),_CienaCesDpPbtTransitPrivateFwdGroup_Type())
cienaCesDpPbtTransitPrivateFwdGroup.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesDpPbtTransitPrivateFwdGroup.setStatus(_A)
class _CienaCesDpPbtTransitIngressMeterPolicy_Type(DpIngressMeterPolicy):defaultValue=1
_CienaCesDpPbtTransitIngressMeterPolicy_Type.__name__=_b
_CienaCesDpPbtTransitIngressMeterPolicy_Object=MibTableColumn
cienaCesDpPbtTransitIngressMeterPolicy=_CienaCesDpPbtTransitIngressMeterPolicy_Object((1,3,6,1,4,1,1271,2,1,7,1,11,1,1,21),_CienaCesDpPbtTransitIngressMeterPolicy_Type())
cienaCesDpPbtTransitIngressMeterPolicy.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesDpPbtTransitIngressMeterPolicy.setStatus(_A)
_CienaCesDpCpuSubInterface_ObjectIdentity=ObjectIdentity
cienaCesDpCpuSubInterface=_CienaCesDpCpuSubInterface_ObjectIdentity((1,3,6,1,4,1,1271,2,1,7,1,12))
_CienaCesDpCpuSubInterfaceTable_Object=MibTable
cienaCesDpCpuSubInterfaceTable=_CienaCesDpCpuSubInterfaceTable_Object((1,3,6,1,4,1,1271,2,1,7,1,12,1))
if mibBuilder.loadTexts:cienaCesDpCpuSubInterfaceTable.setStatus(_A)
_CienaCesDpCpuSubInterfaceEntry_Object=MibTableRow
cienaCesDpCpuSubInterfaceEntry=_CienaCesDpCpuSubInterfaceEntry_Object((1,3,6,1,4,1,1271,2,1,7,1,12,1,1))
cienaCesDpCpuSubInterfaceEntry.setIndexNames((0,_C,_Ap))
if mibBuilder.loadTexts:cienaCesDpCpuSubInterfaceEntry.setStatus(_A)
_CienaCesDpCpuSubInterfaceIndex_Type=Unsigned32
_CienaCesDpCpuSubInterfaceIndex_Object=MibTableColumn
cienaCesDpCpuSubInterfaceIndex=_CienaCesDpCpuSubInterfaceIndex_Object((1,3,6,1,4,1,1271,2,1,7,1,12,1,1,1),_CienaCesDpCpuSubInterfaceIndex_Type())
cienaCesDpCpuSubInterfaceIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:cienaCesDpCpuSubInterfaceIndex.setStatus(_A)
_CienaCesDpCpuSubInterfaceName_Type=OctetString
_CienaCesDpCpuSubInterfaceName_Object=MibTableColumn
cienaCesDpCpuSubInterfaceName=_CienaCesDpCpuSubInterfaceName_Object((1,3,6,1,4,1,1271,2,1,7,1,12,1,1,2),_CienaCesDpCpuSubInterfaceName_Type())
cienaCesDpCpuSubInterfaceName.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesDpCpuSubInterfaceName.setStatus(_A)
_CienaCesDpCpuSubInterfaceEgressL2Transform_Type=OctetString
_CienaCesDpCpuSubInterfaceEgressL2Transform_Object=MibTableColumn
cienaCesDpCpuSubInterfaceEgressL2Transform=_CienaCesDpCpuSubInterfaceEgressL2Transform_Object((1,3,6,1,4,1,1271,2,1,7,1,12,1,1,3),_CienaCesDpCpuSubInterfaceEgressL2Transform_Type())
cienaCesDpCpuSubInterfaceEgressL2Transform.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesDpCpuSubInterfaceEgressL2Transform.setStatus(_A)
_CienaCesDpCpuSubInterfaceIngressL2Transform_Type=OctetString
_CienaCesDpCpuSubInterfaceIngressL2Transform_Object=MibTableColumn
cienaCesDpCpuSubInterfaceIngressL2Transform=_CienaCesDpCpuSubInterfaceIngressL2Transform_Object((1,3,6,1,4,1,1271,2,1,7,1,12,1,1,4),_CienaCesDpCpuSubInterfaceIngressL2Transform_Type())
cienaCesDpCpuSubInterfaceIngressL2Transform.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesDpCpuSubInterfaceIngressL2Transform.setStatus(_A)
class _CienaCesDpCpuSubInterfaceEgressL3TransformPolicy_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_v,1),(_w,2)))
_CienaCesDpCpuSubInterfaceEgressL3TransformPolicy_Type.__name__=_D
_CienaCesDpCpuSubInterfaceEgressL3TransformPolicy_Object=MibTableColumn
cienaCesDpCpuSubInterfaceEgressL3TransformPolicy=_CienaCesDpCpuSubInterfaceEgressL3TransformPolicy_Object((1,3,6,1,4,1,1271,2,1,7,1,12,1,1,5),_CienaCesDpCpuSubInterfaceEgressL3TransformPolicy_Type())
cienaCesDpCpuSubInterfaceEgressL3TransformPolicy.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesDpCpuSubInterfaceEgressL3TransformPolicy.setStatus(_A)
class _CienaCesDpCpuSubInterfaceEgressRCosPolicy_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,99)));namedValues=NamedValues(*(('fixed-cos',1),(_s,99)))
_CienaCesDpCpuSubInterfaceEgressRCosPolicy_Type.__name__=_D
_CienaCesDpCpuSubInterfaceEgressRCosPolicy_Object=MibTableColumn
cienaCesDpCpuSubInterfaceEgressRCosPolicy=_CienaCesDpCpuSubInterfaceEgressRCosPolicy_Object((1,3,6,1,4,1,1271,2,1,7,1,12,1,1,6),_CienaCesDpCpuSubInterfaceEgressRCosPolicy_Type())
cienaCesDpCpuSubInterfaceEgressRCosPolicy.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesDpCpuSubInterfaceEgressRCosPolicy.setStatus(_A)
_CienaCesDpCpuSubInterfaceEgressRCosProfileIndex_Type=Unsigned32
_CienaCesDpCpuSubInterfaceEgressRCosProfileIndex_Object=MibTableColumn
cienaCesDpCpuSubInterfaceEgressRCosProfileIndex=_CienaCesDpCpuSubInterfaceEgressRCosProfileIndex_Object((1,3,6,1,4,1,1271,2,1,7,1,12,1,1,7),_CienaCesDpCpuSubInterfaceEgressRCosProfileIndex_Type())
cienaCesDpCpuSubInterfaceEgressRCosProfileIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesDpCpuSubInterfaceEgressRCosProfileIndex.setStatus(_A)
_CienaCesDpCpuSubInterfaceEgressRCosProfile_Type=OctetString
_CienaCesDpCpuSubInterfaceEgressRCosProfile_Object=MibTableColumn
cienaCesDpCpuSubInterfaceEgressRCosProfile=_CienaCesDpCpuSubInterfaceEgressRCosProfile_Object((1,3,6,1,4,1,1271,2,1,7,1,12,1,1,8),_CienaCesDpCpuSubInterfaceEgressRCosProfile_Type())
cienaCesDpCpuSubInterfaceEgressRCosProfile.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesDpCpuSubInterfaceEgressRCosProfile.setStatus(_A)
class _CienaCesDpCpuSubInterfaceVirtualSwitchIndex_Type(Unsigned32):defaultValue=0
_CienaCesDpCpuSubInterfaceVirtualSwitchIndex_Type.__name__=_S
_CienaCesDpCpuSubInterfaceVirtualSwitchIndex_Object=MibTableColumn
cienaCesDpCpuSubInterfaceVirtualSwitchIndex=_CienaCesDpCpuSubInterfaceVirtualSwitchIndex_Object((1,3,6,1,4,1,1271,2,1,7,1,12,1,1,9),_CienaCesDpCpuSubInterfaceVirtualSwitchIndex_Type())
cienaCesDpCpuSubInterfaceVirtualSwitchIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesDpCpuSubInterfaceVirtualSwitchIndex.setStatus(_A)
_CienaCesDpCpuSubInterfaceRlanIndex_Type=Unsigned32
_CienaCesDpCpuSubInterfaceRlanIndex_Object=MibTableColumn
cienaCesDpCpuSubInterfaceRlanIndex=_CienaCesDpCpuSubInterfaceRlanIndex_Object((1,3,6,1,4,1,1271,2,1,7,1,12,1,1,10),_CienaCesDpCpuSubInterfaceRlanIndex_Type())
cienaCesDpCpuSubInterfaceRlanIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesDpCpuSubInterfaceRlanIndex.setStatus(_A)
_CienaCesDpCpuSubInterfaceVirtualSwitchName_Type=OctetString
_CienaCesDpCpuSubInterfaceVirtualSwitchName_Object=MibTableColumn
cienaCesDpCpuSubInterfaceVirtualSwitchName=_CienaCesDpCpuSubInterfaceVirtualSwitchName_Object((1,3,6,1,4,1,1271,2,1,7,1,12,1,1,11),_CienaCesDpCpuSubInterfaceVirtualSwitchName_Type())
cienaCesDpCpuSubInterfaceVirtualSwitchName.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesDpCpuSubInterfaceVirtualSwitchName.setStatus(_A)
_CienaCesDpPfgProfile_ObjectIdentity=ObjectIdentity
cienaCesDpPfgProfile=_CienaCesDpPfgProfile_ObjectIdentity((1,3,6,1,4,1,1271,2,1,7,1,13))
_CienaCesDpPfgProfileTable_Object=MibTable
cienaCesDpPfgProfileTable=_CienaCesDpPfgProfileTable_Object((1,3,6,1,4,1,1271,2,1,7,1,13,1))
if mibBuilder.loadTexts:cienaCesDpPfgProfileTable.setStatus(_A)
_CienaCesDpPfgProfileEntry_Object=MibTableRow
cienaCesDpPfgProfileEntry=_CienaCesDpPfgProfileEntry_Object((1,3,6,1,4,1,1271,2,1,7,1,13,1,1))
cienaCesDpPfgProfileEntry.setIndexNames((0,_C,_Aq))
if mibBuilder.loadTexts:cienaCesDpPfgProfileEntry.setStatus(_A)
class _CienaCesDpPfgProfileIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_CienaCesDpPfgProfileIndex_Type.__name__=_D
_CienaCesDpPfgProfileIndex_Object=MibTableColumn
cienaCesDpPfgProfileIndex=_CienaCesDpPfgProfileIndex_Object((1,3,6,1,4,1,1271,2,1,7,1,13,1,1,1),_CienaCesDpPfgProfileIndex_Type())
cienaCesDpPfgProfileIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:cienaCesDpPfgProfileIndex.setStatus(_A)
_CienaCesDpPfgProfileName_Type=DisplayString
_CienaCesDpPfgProfileName_Object=MibTableColumn
cienaCesDpPfgProfileName=_CienaCesDpPfgProfileName_Object((1,3,6,1,4,1,1271,2,1,7,1,13,1,1,2),_CienaCesDpPfgProfileName_Type())
cienaCesDpPfgProfileName.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesDpPfgProfileName.setStatus(_A)
class _CienaCesDpPfgProfileAPolicy_Type(PrivateForwardGroupPolicy):defaultValue=7
_CienaCesDpPfgProfileAPolicy_Type.__name__=_Q
_CienaCesDpPfgProfileAPolicy_Object=MibTableColumn
cienaCesDpPfgProfileAPolicy=_CienaCesDpPfgProfileAPolicy_Object((1,3,6,1,4,1,1271,2,1,7,1,13,1,1,3),_CienaCesDpPfgProfileAPolicy_Type())
cienaCesDpPfgProfileAPolicy.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesDpPfgProfileAPolicy.setStatus(_A)
class _CienaCesDpPfgProfileBPolicy_Type(PrivateForwardGroupPolicy):defaultValue=7
_CienaCesDpPfgProfileBPolicy_Type.__name__=_Q
_CienaCesDpPfgProfileBPolicy_Object=MibTableColumn
cienaCesDpPfgProfileBPolicy=_CienaCesDpPfgProfileBPolicy_Object((1,3,6,1,4,1,1271,2,1,7,1,13,1,1,4),_CienaCesDpPfgProfileBPolicy_Type())
cienaCesDpPfgProfileBPolicy.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesDpPfgProfileBPolicy.setStatus(_A)
class _CienaCesDpPfgProfileCPolicy_Type(PrivateForwardGroupPolicy):defaultValue=7
_CienaCesDpPfgProfileCPolicy_Type.__name__=_Q
_CienaCesDpPfgProfileCPolicy_Object=MibTableColumn
cienaCesDpPfgProfileCPolicy=_CienaCesDpPfgProfileCPolicy_Object((1,3,6,1,4,1,1271,2,1,7,1,13,1,1,5),_CienaCesDpPfgProfileCPolicy_Type())
cienaCesDpPfgProfileCPolicy.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesDpPfgProfileCPolicy.setStatus(_A)
_CienaCesDpL2CftProfile_ObjectIdentity=ObjectIdentity
cienaCesDpL2CftProfile=_CienaCesDpL2CftProfile_ObjectIdentity((1,3,6,1,4,1,1271,2,1,7,1,14))
_CienaCesDpL2CftProfileTable_Object=MibTable
cienaCesDpL2CftProfileTable=_CienaCesDpL2CftProfileTable_Object((1,3,6,1,4,1,1271,2,1,7,1,14,1))
if mibBuilder.loadTexts:cienaCesDpL2CftProfileTable.setStatus(_A)
_CienaCesDpL2CftProfileEntry_Object=MibTableRow
cienaCesDpL2CftProfileEntry=_CienaCesDpL2CftProfileEntry_Object((1,3,6,1,4,1,1271,2,1,7,1,14,1,1))
cienaCesDpL2CftProfileEntry.setIndexNames((0,_C,_x))
if mibBuilder.loadTexts:cienaCesDpL2CftProfileEntry.setStatus(_A)
_CienaCesDpL2CftProfileIndex_Type=Integer32
_CienaCesDpL2CftProfileIndex_Object=MibTableColumn
cienaCesDpL2CftProfileIndex=_CienaCesDpL2CftProfileIndex_Object((1,3,6,1,4,1,1271,2,1,7,1,14,1,1,1),_CienaCesDpL2CftProfileIndex_Type())
cienaCesDpL2CftProfileIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:cienaCesDpL2CftProfileIndex.setStatus(_A)
_CienaCesDpL2CftProfileName_Type=DisplayString
_CienaCesDpL2CftProfileName_Object=MibTableColumn
cienaCesDpL2CftProfileName=_CienaCesDpL2CftProfileName_Object((1,3,6,1,4,1,1271,2,1,7,1,14,1,1,2),_CienaCesDpL2CftProfileName_Type())
cienaCesDpL2CftProfileName.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesDpL2CftProfileName.setStatus(_A)
class _CienaCesDpL2CftProfileL2ControlRcos_Type(Integer32):defaultValue=48
_CienaCesDpL2CftProfileL2ControlRcos_Type.__name__=_D
_CienaCesDpL2CftProfileL2ControlRcos_Object=MibTableColumn
cienaCesDpL2CftProfileL2ControlRcos=_CienaCesDpL2CftProfileL2ControlRcos_Object((1,3,6,1,4,1,1271,2,1,7,1,14,1,1,3),_CienaCesDpL2CftProfileL2ControlRcos_Type())
cienaCesDpL2CftProfileL2ControlRcos.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesDpL2CftProfileL2ControlRcos.setStatus(_A)
_CienaCesDpL2CftProfileL2CftProtocolTable_Object=MibTable
cienaCesDpL2CftProfileL2CftProtocolTable=_CienaCesDpL2CftProfileL2CftProtocolTable_Object((1,3,6,1,4,1,1271,2,1,7,1,14,2))
if mibBuilder.loadTexts:cienaCesDpL2CftProfileL2CftProtocolTable.setStatus(_A)
_CienaCesDpL2CftProfileL2CftProtocolEntry_Object=MibTableRow
cienaCesDpL2CftProfileL2CftProtocolEntry=_CienaCesDpL2CftProfileL2CftProtocolEntry_Object((1,3,6,1,4,1,1271,2,1,7,1,14,2,1))
cienaCesDpL2CftProfileL2CftProtocolEntry.setIndexNames((0,_C,_x),(0,_C,_Ar))
if mibBuilder.loadTexts:cienaCesDpL2CftProfileL2CftProtocolEntry.setStatus(_A)
class _CienaCesDpL2CftProfileL2CftProtocolType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23)));namedValues=NamedValues(*((_R,0),('ciscoCdp',1),('ciscoDtp',2),(_Ad,3),(_Ae,4),('ciscoVtp',5),(_Af,6),(_Ag,7),(_Ah,8),('rstp',9),('lacp',10),(_Ai,11),('oam',12),('lldp',13),('i8021x',14),('gmrp',15),('gvrp',16),('isis',17),('esmc',18),('bridgeReserved0C0D',19),('bridgeReserved0B0F',20),(_Aj,21),(_Ak,22),(_Al,23)))
_CienaCesDpL2CftProfileL2CftProtocolType_Type.__name__=_D
_CienaCesDpL2CftProfileL2CftProtocolType_Object=MibTableColumn
cienaCesDpL2CftProfileL2CftProtocolType=_CienaCesDpL2CftProfileL2CftProtocolType_Object((1,3,6,1,4,1,1271,2,1,7,1,14,2,1,1),_CienaCesDpL2CftProfileL2CftProtocolType_Type())
cienaCesDpL2CftProfileL2CftProtocolType.setMaxAccess(_E)
if mibBuilder.loadTexts:cienaCesDpL2CftProfileL2CftProtocolType.setStatus(_A)
class _CienaCesDpL2CftProfileL2CftProtocolDisposition_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('forward',1),('discard',2)))
_CienaCesDpL2CftProfileL2CftProtocolDisposition_Type.__name__=_D
_CienaCesDpL2CftProfileL2CftProtocolDisposition_Object=MibTableColumn
cienaCesDpL2CftProfileL2CftProtocolDisposition=_CienaCesDpL2CftProfileL2CftProtocolDisposition_Object((1,3,6,1,4,1,1271,2,1,7,1,14,2,1,2),_CienaCesDpL2CftProfileL2CftProtocolDisposition_Type())
cienaCesDpL2CftProfileL2CftProtocolDisposition.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesDpL2CftProfileL2CftProtocolDisposition.setStatus(_A)
_CienaCesDpMIBNotificationPrefix_ObjectIdentity=ObjectIdentity
cienaCesDpMIBNotificationPrefix=_CienaCesDpMIBNotificationPrefix_ObjectIdentity((1,3,6,1,4,1,1271,2,2,7))
_CienaCesDpMIBNotifications_ObjectIdentity=ObjectIdentity
cienaCesDpMIBNotifications=_CienaCesDpMIBNotifications_ObjectIdentity((1,3,6,1,4,1,1271,2,2,7,0))
cienaCesDpTsMeterFloodContainerUcastThresholdExceeded=NotificationType((1,3,6,1,4,1,1271,2,2,7,0,1))
cienaCesDpTsMeterFloodContainerUcastThresholdExceeded.setObjects(*((_F,_I),(_F,_H),(_C,_K),(_C,_L),(_C,_M),(_C,_N),(_C,_O)))
if mibBuilder.loadTexts:cienaCesDpTsMeterFloodContainerUcastThresholdExceeded.setStatus(_A)
cienaCesDpTsMeterFloodContainerUcastThresholdNormal=NotificationType((1,3,6,1,4,1,1271,2,2,7,0,2))
cienaCesDpTsMeterFloodContainerUcastThresholdNormal.setObjects(*((_F,_I),(_F,_H),(_C,_K),(_C,_L),(_C,_M),(_C,_N),(_C,_O)))
if mibBuilder.loadTexts:cienaCesDpTsMeterFloodContainerUcastThresholdNormal.setStatus(_A)
cienaCesDpTsMeterFloodContainerBcastThresholdExceeded=NotificationType((1,3,6,1,4,1,1271,2,2,7,0,3))
cienaCesDpTsMeterFloodContainerBcastThresholdExceeded.setObjects(*((_F,_I),(_F,_H),(_C,_K),(_C,_L),(_C,_M),(_C,_N),(_C,_O)))
if mibBuilder.loadTexts:cienaCesDpTsMeterFloodContainerBcastThresholdExceeded.setStatus(_A)
cienaCesDpTsMeterFloodContainerBcastThresholdNormal=NotificationType((1,3,6,1,4,1,1271,2,2,7,0,4))
cienaCesDpTsMeterFloodContainerBcastThresholdNormal.setObjects(*((_F,_I),(_F,_H),(_C,_K),(_C,_L),(_C,_M),(_C,_N),(_C,_O)))
if mibBuilder.loadTexts:cienaCesDpTsMeterFloodContainerBcastThresholdNormal.setStatus(_A)
cienaCesDpTsMeterFloodContainerL2McastThresholdExceeded=NotificationType((1,3,6,1,4,1,1271,2,2,7,0,5))
cienaCesDpTsMeterFloodContainerL2McastThresholdExceeded.setObjects(*((_F,_I),(_F,_H),(_C,_K),(_C,_L),(_C,_M),(_C,_N),(_C,_O)))
if mibBuilder.loadTexts:cienaCesDpTsMeterFloodContainerL2McastThresholdExceeded.setStatus(_A)
cienaCesDpTsMeterFloodContainerL2McastThresholdNormal=NotificationType((1,3,6,1,4,1,1271,2,2,7,0,6))
cienaCesDpTsMeterFloodContainerL2McastThresholdNormal.setObjects(*((_F,_I),(_F,_H),(_C,_K),(_C,_L),(_C,_M),(_C,_N),(_C,_O)))
if mibBuilder.loadTexts:cienaCesDpTsMeterFloodContainerL2McastThresholdNormal.setStatus(_A)
cienaCesDataplaneEgressReflectorEnabled=NotificationType((1,3,6,1,4,1,1271,2,2,7,0,7))
cienaCesDataplaneEgressReflectorEnabled.setObjects(*((_F,_I),(_F,_H),(_C,_y),(_C,_a),(_C,_As),(_C,_At)))
if mibBuilder.loadTexts:cienaCesDataplaneEgressReflectorEnabled.setStatus(_A)
cienaCesDataplaneEgressReflectorDisabled=NotificationType((1,3,6,1,4,1,1271,2,2,7,0,8))
cienaCesDataplaneEgressReflectorDisabled.setObjects(*((_F,_I),(_F,_H),(_C,_y),(_C,_a)))
if mibBuilder.loadTexts:cienaCesDataplaneEgressReflectorDisabled.setStatus(_A)
cienaCesDpPortShapingSubscriptionExceedsOperSpeed=NotificationType((1,3,6,1,4,1,1271,2,2,7,0,9))
cienaCesDpPortShapingSubscriptionExceedsOperSpeed.setObjects(*((_F,_I),(_F,_H),(_J,_e),(_J,_g),(_J,_h),(_J,_f),(_J,_d)))
if mibBuilder.loadTexts:cienaCesDpPortShapingSubscriptionExceedsOperSpeed.setStatus(_A)
cienaCesDpPortShapingSubscriptionWithinOperSpeed=NotificationType((1,3,6,1,4,1,1271,2,2,7,0,10))
cienaCesDpPortShapingSubscriptionWithinOperSpeed.setObjects(*((_F,_I),(_F,_H),(_J,_e),(_J,_g),(_J,_h),(_J,_f),(_J,_d)))
if mibBuilder.loadTexts:cienaCesDpPortShapingSubscriptionWithinOperSpeed.setStatus(_A)
cienaCesDpTsMeterFloodContainerTotalThresholdExceeded=NotificationType((1,3,6,1,4,1,1271,2,2,7,0,11))
cienaCesDpTsMeterFloodContainerTotalThresholdExceeded.setObjects(*((_F,_I),(_F,_H),(_C,_K),(_C,_L),(_C,_M),(_C,_N),(_C,_O)))
if mibBuilder.loadTexts:cienaCesDpTsMeterFloodContainerTotalThresholdExceeded.setStatus(_A)
cienaCesDpTsMeterFloodContainerTotalThresholdNormal=NotificationType((1,3,6,1,4,1,1271,2,2,7,0,12))
cienaCesDpTsMeterFloodContainerTotalThresholdNormal.setObjects(*((_F,_I),(_F,_H),(_C,_K),(_C,_L),(_C,_M),(_C,_N),(_C,_O)))
if mibBuilder.loadTexts:cienaCesDpTsMeterFloodContainerTotalThresholdNormal.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'DpTsAttachType':DpTsAttachType,_Q:PrivateForwardGroupPolicy,_A6:DpCouplingFlag,_b:DpIngressMeterPolicy,'DpSchedulingType':DpSchedulingType,'cienaCesDataplaneMIB':cienaCesDataplaneMIB,'cienaCesDpMIBObjects':cienaCesDpMIBObjects,'cienaCesDpTsMeterFloodContainerNotifAttrs':cienaCesDpTsMeterFloodContainerNotifAttrs,'cienaCesDpTsMeterFloodContainerProfileTable':cienaCesDpTsMeterFloodContainerProfileTable,'cienaCesDpTsMeterFloodContainerProfileEntry':cienaCesDpTsMeterFloodContainerProfileEntry,_k:cienaCesDpTsMeterFloodContainerProfileIndex,_N:cienaCesDpTsMeterFloodContainerProfileName,_K:cienaCesDpTsMeterFloodContainerNotifProfileIndex,'cienaCesDpTsMeterFloodContainerProfileRate1':cienaCesDpTsMeterFloodContainerProfileRate1,'cienaCesDpTsMeterFloodContainerProfileRate2':cienaCesDpTsMeterFloodContainerProfileRate2,'cienaCesDpTsMeterFloodContainerProfileRate3':cienaCesDpTsMeterFloodContainerProfileRate3,'cienaCesDpTsMeterFloodContainerProfileUnknownUnicastRateId':cienaCesDpTsMeterFloodContainerProfileUnknownUnicastRateId,'cienaCesDpTsMeterFloodContainerProfileL2BroadcastRateId':cienaCesDpTsMeterFloodContainerProfileL2BroadcastRateId,'cienaCesDpTsMeterFloodContainerProfileL2UnknownMulticastRateId':cienaCesDpTsMeterFloodContainerProfileL2UnknownMulticastRateId,'cienaCesDpTsMeterFloodContainerAttachmentTable':cienaCesDpTsMeterFloodContainerAttachmentTable,'cienaCesDpTsMeterFloodContainerAttachmentEntry':cienaCesDpTsMeterFloodContainerAttachmentEntry,_A4:cienaCesDpTsMeterFloodContainerAttachmentLiType,_A5:cienaCesDpTsMeterFloodContainerAttachmentLiIndex,_O:cienaCesDpTsMeterFloodContainerAttachmentInterfaceName,_L:cienaCesDpTsMeterFloodContainerNotifAttachmentLiType,_M:cienaCesDpTsMeterFloodContainerNotifAttachmentLiIndex,'cienaCesDpTsMeterFloodContainerAttachmentUcastRateState':cienaCesDpTsMeterFloodContainerAttachmentUcastRateState,'cienaCesDpTsMeterFloodContainerAttachmentL2BcastRateState':cienaCesDpTsMeterFloodContainerAttachmentL2BcastRateState,'cienaCesDpTsMeterFloodContainerAttachmentL2McastRateState':cienaCesDpTsMeterFloodContainerAttachmentL2McastRateState,'cienaCesDpTsMeterFloodContainerAttachmentTotalBandwidth':cienaCesDpTsMeterFloodContainerAttachmentTotalBandwidth,'cienaCesDpTsMeterFloodContainerAttachmentUsedBandwidth':cienaCesDpTsMeterFloodContainerAttachmentUsedBandwidth,'cienaCesDpTsMeterFloodContainerAttachmentTotalRateState':cienaCesDpTsMeterFloodContainerAttachmentTotalRateState,'cienaCesDpTsMeter':cienaCesDpTsMeter,'cienaCesDpTsMeterProfile':cienaCesDpTsMeterProfile,'cienaCesDpTsMeterProfileTable':cienaCesDpTsMeterProfileTable,'cienaCesDpTsMeterProfileEntry':cienaCesDpTsMeterProfileEntry,_p:cienaCesDpTsMeterProfileIndex,'cienaCesDpTsMeterProfileName':cienaCesDpTsMeterProfileName,'cienaCesDpTsMeterProfileCIR':cienaCesDpTsMeterProfileCIR,'cienaCesDpTsMeterProfileCBS':cienaCesDpTsMeterProfileCBS,'cienaCesDpTsMeterProfileEIR':cienaCesDpTsMeterProfileEIR,'cienaCesDpTsMeterProfileEBS':cienaCesDpTsMeterProfileEBS,'cienaCesDpTsMeterProfileColorMode':cienaCesDpTsMeterProfileColorMode,'cienaCesDpTsMeterProfileCouplingFlag':cienaCesDpTsMeterProfileCouplingFlag,'cienaCesDpTsMeterProfileAttachmentTable':cienaCesDpTsMeterProfileAttachmentTable,'cienaCesDpTsMeterProfileAttachmentEntry':cienaCesDpTsMeterProfileAttachmentEntry,_A7:cienaCesDpTsMeterProfileAttachmentLiType,_A8:cienaCesDpTsMeterProfileAttachmentLiIndex,'cienaCesDpTsMeterProfileAttachmentTotalCIR':cienaCesDpTsMeterProfileAttachmentTotalCIR,'cienaCesDpTsMeterProfileAttachmentTotalEIR':cienaCesDpTsMeterProfileAttachmentTotalEIR,'cienaCesDpTsMeterProfileAttachmentUsedCIR':cienaCesDpTsMeterProfileAttachmentUsedCIR,'cienaCesDpTsMeterProfileAttachmentMaxUsedEIR':cienaCesDpTsMeterProfileAttachmentMaxUsedEIR,'cienaCesDpTsCosMap':cienaCesDpTsCosMap,'cienaCesDpTsCosMapRcos':cienaCesDpTsCosMapRcos,'cienaCesDpTsCosMapRcosProfileTable':cienaCesDpTsCosMapRcosProfileTable,'cienaCesDpTsCosMapRcosProfileEntry':cienaCesDpTsCosMapRcosProfileEntry,_A9:cienaCesDpTsCosMapRcosProfileId,'cienaCesDpTsCosMapRcosProfileName':cienaCesDpTsCosMapRcosProfileName,'cienaCesDpTsCosMapRcosFixedRCoSValue':cienaCesDpTsCosMapRcosFixedRCoSValue,'cienaCesDpTsCosMapRcosFixedRcolour':cienaCesDpTsCosMapRcosFixedRcolour,'cienaCesDpTsCosMapRcosCosMapId':cienaCesDpTsCosMapRcosCosMapId,'cienaCesDpTsCosMapRcosCosMapName':cienaCesDpTsCosMapRcosCosMapName,'cienaCesDpTsCosMapRcosMapTable':cienaCesDpTsCosMapRcosMapTable,'cienaCesDpTsCosMapRcosMapEntry':cienaCesDpTsCosMapRcosMapEntry,_AA:cienaCesDpTsCosMapRcosMapId,'cienaCesDpTsCosMapRcosMapName':cienaCesDpTsCosMapRcosMapName,'cienaCesDpTsCosMapRcosMapL2RCoS':cienaCesDpTsCosMapRcosMapL2RCoS,'cienaCesDpTsCosMapRcosMapL2RColour':cienaCesDpTsCosMapRcosMapL2RColour,'cienaCesDpTsCosMapRcosMapL3DscpRCoS':cienaCesDpTsCosMapRcosMapL3DscpRCoS,'cienaCesDpTsCosMapRcosMapL3DscpRColour':cienaCesDpTsCosMapRcosMapL3DscpRColour,'cienaCesDpTsCosMapRcosMapExpRCoS':cienaCesDpTsCosMapRcosMapExpRCoS,'cienaCesDpTsCosMapRcosMapExpRColour':cienaCesDpTsCosMapRcosMapExpRColour,'cienaCesDpTsCosMapFcos':cienaCesDpTsCosMapFcos,'cienaCesDpTsCosMapFcosMapTable':cienaCesDpTsCosMapFcosMapTable,'cienaCesDpTsCosMapFcosMapEntry':cienaCesDpTsCosMapFcosMapEntry,_AB:cienaCesDpTsCosMapFcosMapId,'cienaCesDpTsCosMapFcosMapName':cienaCesDpTsCosMapFcosMapName,'cienaCesDpTsCosMapFcosL2CoS':cienaCesDpTsCosMapFcosL2CoS,'cienaCesDpTsCosMapFcosL2Dei':cienaCesDpTsCosMapFcosL2Dei,'cienaCesDpTsCosMapFcosL3Dscp':cienaCesDpTsCosMapFcosL3Dscp,'cienaCesDpTsCosMapFcosExp':cienaCesDpTsCosMapFcosExp,'cienaCesDpTsShaper':cienaCesDpTsShaper,'cienaCesDpTsShaperProfile':cienaCesDpTsShaperProfile,'cienaCesDpTsShaperProfileTable':cienaCesDpTsShaperProfileTable,'cienaCesDpTsShaperProfileEntry':cienaCesDpTsShaperProfileEntry,_q:cienaCesDpTsShaperProfileIndex,'cienaCesDpTsShaperProfileName':cienaCesDpTsShaperProfileName,'cienaCesDpTsShaperProfileCIR':cienaCesDpTsShaperProfileCIR,'cienaCesDpTsShaperProfileCBS':cienaCesDpTsShaperProfileCBS,'cienaCesDpTsShaperProfileAttachmentTable':cienaCesDpTsShaperProfileAttachmentTable,'cienaCesDpTsShaperProfileAttachmentEntry':cienaCesDpTsShaperProfileAttachmentEntry,_AC:cienaCesDpTsShaperProfileAttachmentLiType,_AD:cienaCesDpTsShaperProfileAttachmentLiIndex,'cienaCesDpTsShaperProfileAttachmentTotalCIR':cienaCesDpTsShaperProfileAttachmentTotalCIR,'cienaCesDpTsShaperProfileAttachmentTotalEIR':cienaCesDpTsShaperProfileAttachmentTotalEIR,'cienaCesDpTsShaperProfileAttachmentUsedCIR':cienaCesDpTsShaperProfileAttachmentUsedCIR,'cienaCesDpTsShaperProfileAttachmentMaxUsedEIR':cienaCesDpTsShaperProfileAttachmentMaxUsedEIR,'cienaCesDpTsQ':cienaCesDpTsQ,'cienaCesDpTsQCongestionAvoidanceProfile':cienaCesDpTsQCongestionAvoidanceProfile,'cienaCesDpTsQCAProfileWREDTable':cienaCesDpTsQCAProfileWREDTable,'cienaCesDpTsQCAProfileWREDEntry':cienaCesDpTsQCAProfileWREDEntry,_r:cienaCesDpTsQCAProfileWREDId,'cienaCesDpTsQCAProfileWREDName':cienaCesDpTsQCAProfileWREDName,'cienaCesDpTsQCAProfileWREDDropRateExponent':cienaCesDpTsQCAProfileWREDDropRateExponent,'cienaCesDpTsQCAProfileWREDMaxQueueSize':cienaCesDpTsQCAProfileWREDMaxQueueSize,'cienaCesDpTsQCAProfileWREDMinQueueGuarantee':cienaCesDpTsQCAProfileWREDMinQueueGuarantee,'cienaCesDpTsQCAProfileWREDCurveTable':cienaCesDpTsQCAProfileWREDCurveTable,'cienaCesDpTsQCAProfileWREDCurveEntry':cienaCesDpTsQCAProfileWREDCurveEntry,_AE:cienaCesDpTsQCAProfileWREDCurveId,'cienaCesDpTsQCAProfileWREDCurveLowerThreshold':cienaCesDpTsQCAProfileWREDCurveLowerThreshold,'cienaCesDpTsQCAProfileWREDCurveUpperThreshold':cienaCesDpTsQCAProfileWREDCurveUpperThreshold,'cienaCesDpTsQCAProfileWREDCurveMaxDropProbability':cienaCesDpTsQCAProfileWREDCurveMaxDropProbability,'cienaCesDpTsQRCOSQMap':cienaCesDpTsQRCOSQMap,'cienaCesDpTsQRCOSQMapTable':cienaCesDpTsQRCOSQMapTable,'cienaCesDpTsQRCOSQMapEntry':cienaCesDpTsQRCOSQMapEntry,_T:cienaCesDpTsQRCOSQMapId,'cienaCesDpTsQRCOSQMapName':cienaCesDpTsQRCOSQMapName,'cienaCesDpTsQRCOSQMapQueueTable':cienaCesDpTsQRCOSQMapQueueTable,'cienaCesDpTsQRCOSQMapQueueEntry':cienaCesDpTsQRCOSQMapQueueEntry,_AF:cienaCesDpTsQRCOSQMapQueueId,'cienaCesDpTsQRCOSQMapQueueNumber':cienaCesDpTsQRCOSQMapQueueNumber,'cienaCesDpTsQRCOSQMapGreenCurveTable':cienaCesDpTsQRCOSQMapGreenCurveTable,'cienaCesDpTsQRCOSQMapGreenCurveEntry':cienaCesDpTsQRCOSQMapGreenCurveEntry,_AG:cienaCesDpTsQRCOSQMapGreenCurveId,'cienaCesDpTsQRCOSQMapGreenCurveNumber':cienaCesDpTsQRCOSQMapGreenCurveNumber,'cienaCesDpTsQRCOSQMapYellowCurveTable':cienaCesDpTsQRCOSQMapYellowCurveTable,'cienaCesDpTsQRCOSQMapYellowCurveEntry':cienaCesDpTsQRCOSQMapYellowCurveEntry,_AJ:cienaCesDpTsQRCOSQMapYellowCurveId,'cienaCesDpTsQRCOSQMapYellowCurveNumber':cienaCesDpTsQRCOSQMapYellowCurveNumber,'cienaCesDpTsQGroupProfile':cienaCesDpTsQGroupProfile,'cienaCesDpTsQGroupProfileTable':cienaCesDpTsQGroupProfileTable,'cienaCesDpTsQGroupProfileEntry':cienaCesDpTsQGroupProfileEntry,_X:cienaCesDpTsQGroupProfileId,'cienaCesDpTsQGroupProfileName':cienaCesDpTsQGroupProfileName,'cienaCesDpTsQGroupProfileQueueCount':cienaCesDpTsQGroupProfileQueueCount,'cienaCesDpTsQGroupProfileRCOSQMapId':cienaCesDpTsQGroupProfileRCOSQMapId,'cienaCesDpTsQGroupProfileShaperCompensation':cienaCesDpTsQGroupProfileShaperCompensation,'cienaCesDpTsQGroupProfileQueueTable':cienaCesDpTsQGroupProfileQueueTable,'cienaCesDpTsQGroupProfileQueueEntry':cienaCesDpTsQGroupProfileQueueEntry,_AK:cienaCesDpTsQGroupProfileQueueIndex,'cienaCesDpTsQGroupProfileQueueCAPId':cienaCesDpTsQGroupProfileQueueCAPId,'cienaCesDpTsQGroupProfileQueueCIR':cienaCesDpTsQGroupProfileQueueCIR,'cienaCesDpTsQGroupProfileQueueCBS':cienaCesDpTsQGroupProfileQueueCBS,'cienaCesDpTsQGroupProfileQueueEIR':cienaCesDpTsQGroupProfileQueueEIR,'cienaCesDpTsQGroupProfileQueueEBS':cienaCesDpTsQGroupProfileQueueEBS,'cienaCesDpTsQGroupProfileQueueCirPercent':cienaCesDpTsQGroupProfileQueueCirPercent,'cienaCesDpTsQGroupProfileQueueEirPercent':cienaCesDpTsQGroupProfileQueueEirPercent,'cienaCesDpTsQGroupInstance':cienaCesDpTsQGroupInstance,'cienaCesDpTsQGroupInstanceTable':cienaCesDpTsQGroupInstanceTable,'cienaCesDpTsQGroupInstanceEntry':cienaCesDpTsQGroupInstanceEntry,_AL:cienaCesDpTsQGroupInstancePgid,_AM:cienaCesDpTsQGroupInstanceIndex,'cienaCesDpTsQGroupInstanceParentSchedId':cienaCesDpTsQGroupInstanceParentSchedId,'cienaCesDpTsQGroupInstanceParentInstanceId':cienaCesDpTsQGroupInstanceParentInstanceId,'cienaCesDpTsQSchedulerProfile':cienaCesDpTsQSchedulerProfile,'cienaCesDpTsQSchedulerProfileTable':cienaCesDpTsQSchedulerProfileTable,'cienaCesDpTsQSchedulerProfileEntry':cienaCesDpTsQSchedulerProfileEntry,_Z:cienaCesDpTsQSchedulerProfileId,'cienaCesDpTsQSchedulerProfileName':cienaCesDpTsQSchedulerProfileName,'cienaCesDpTsQSchedulerProfileSchedulerAlgorithm':cienaCesDpTsQSchedulerProfileSchedulerAlgorithm,'cienaCesDpTsQSchedulerProfileCIR':cienaCesDpTsQSchedulerProfileCIR,'cienaCesDpTsQSchedulerProfileCBS':cienaCesDpTsQSchedulerProfileCBS,'cienaCesDpTsQSchedulerProfileEIR':cienaCesDpTsQSchedulerProfileEIR,'cienaCesDpTsQSchedulerProfileEBS':cienaCesDpTsQSchedulerProfileEBS,'cienaCesDpTsQSchedulerProfileScheduledUcastWt':cienaCesDpTsQSchedulerProfileScheduledUcastWt,'cienaCesDpTsQSchedulerProfileScheduledMcastWt':cienaCesDpTsQSchedulerProfileScheduledMcastWt,'cienaCesDpTsQSchedulerProfileTapPointCount':cienaCesDpTsQSchedulerProfileTapPointCount,'cienaCesDpTsQSchedulerProfileShaperOverSpeed':cienaCesDpTsQSchedulerProfileShaperOverSpeed,'cienaCesDpTsQSchedulerProfileCirPolicy':cienaCesDpTsQSchedulerProfileCirPolicy,'cienaCesDpTsQSchedulerProfileEirPolicy':cienaCesDpTsQSchedulerProfileEirPolicy,'cienaCesDpTsQSchedulerProfileCirPercent':cienaCesDpTsQSchedulerProfileCirPercent,'cienaCesDpTsQSchedulerProfileEirPercent':cienaCesDpTsQSchedulerProfileEirPercent,'cienaCesDpTsQSchedulerTapPointTable':cienaCesDpTsQSchedulerTapPointTable,'cienaCesDpTsQSchedulerTapPointEntry':cienaCesDpTsQSchedulerTapPointEntry,_AO:cienaCesDpTsQSchedulerTapPointIndex,'cienaCesDpTsQSchedulerTapPointPriority':cienaCesDpTsQSchedulerTapPointPriority,'cienaCesDpTsQSchedulerTapPointWeight':cienaCesDpTsQSchedulerTapPointWeight,'cienaCesDpTsQSchedulerInstance':cienaCesDpTsQSchedulerInstance,'cienaCesDpTsQSchedulerInstanceTable':cienaCesDpTsQSchedulerInstanceTable,'cienaCesDpTsQSchedulerInstanceEntry':cienaCesDpTsQSchedulerInstanceEntry,_AP:cienaCesDpTsQSchedulerInstancePgid,_AQ:cienaCesDpTsQSchedulerInstanceIndex,'cienaCesDpTsQSchedulerInstanceParentSchedId':cienaCesDpTsQSchedulerInstanceParentSchedId,'cienaCesDpTsQSchedulerInstanceParentInstanceId':cienaCesDpTsQSchedulerInstanceParentInstanceId,'cienaCesDpTsQSchedulerInstanceParentTapPoint':cienaCesDpTsQSchedulerInstanceParentTapPoint,'cienaCesDpTsQSchedulerInstanceControlPlaneUsedCir':cienaCesDpTsQSchedulerInstanceControlPlaneUsedCir,'cienaCesDpTrafficClassTerm':cienaCesDpTrafficClassTerm,'cienaCesDpTrafficClassTermTable':cienaCesDpTrafficClassTermTable,'cienaCesDpTrafficClassTermEntry':cienaCesDpTrafficClassTermEntry,_AR:cienaCesDpTrafficClassType,_AS:cienaCesDpTrafficClassId,_AT:cienaCesDpTrafficClassElemId,_AU:cienaCesDpTrafficClassTermPresentType,'cienaCesDpTrafficClassTermStartValue32':cienaCesDpTrafficClassTermStartValue32,'cienaCesDpTrafficClassTermEndOrMaskValue32':cienaCesDpTrafficClassTermEndOrMaskValue32,'cienaCesDpTrafficClassTermStartValueMac':cienaCesDpTrafficClassTermStartValueMac,'cienaCesDpTrafficClassTermMaskValueMac':cienaCesDpTrafficClassTermMaskValueMac,'cienaCesDpTrafficClassTermStartValueIp':cienaCesDpTrafficClassTermStartValueIp,'cienaCesDpTrafficClassTermMaskValueIp':cienaCesDpTrafficClassTermMaskValueIp,'cienaCesDpSubPort':cienaCesDpSubPort,'cienaCesDpSubPortTable':cienaCesDpSubPortTable,'cienaCesDpSubPortEntry':cienaCesDpSubPortEntry,_a:cienaCesDpSubPortLiIndex,_y:cienaCesDpSubPortName,'cienaCesDpSubPortClassifierPrecedence':cienaCesDpSubPortClassifierPrecedence,'cienaCesDpSubPortParentIfId':cienaCesDpSubPortParentIfId,'cienaCesDpSubPortVirtualSwitchIndex':cienaCesDpSubPortVirtualSwitchIndex,'cienaCesDpSubPortRlanIndex':cienaCesDpSubPortRlanIndex,'cienaCesDpSubPortVirtualSwitchName':cienaCesDpSubPortVirtualSwitchName,'cienaCesDpSubPortIngressMeterProfileId':cienaCesDpSubPortIngressMeterProfileId,'cienaCesDpSubPortIngressMeterProfileName':cienaCesDpSubPortIngressMeterProfileName,'cienaCesDpSubportIngressMeterPolicy':cienaCesDpSubportIngressMeterPolicy,'cienaCesDpSubPortIngressFloodContainerId':cienaCesDpSubPortIngressFloodContainerId,'cienaCesDpSubPortIngressFloodContainerName':cienaCesDpSubPortIngressFloodContainerName,'cienaCesDpSubPortIngressRcosProfileId':cienaCesDpSubPortIngressRcosProfileId,'cienaCesDpSubPortIngressRcosProfileName':cienaCesDpSubPortIngressRcosProfileName,'cienaCesDpSubPortIngressRcosPolicy':cienaCesDpSubPortIngressRcosPolicy,'cienaCesDpSubPortIngressFcosMapId':cienaCesDpSubPortIngressFcosMapId,'cienaCesDpSubPortIngressFcosMapName':cienaCesDpSubPortIngressFcosMapName,'cienaCesDpSubPortEgressFcosMapId':cienaCesDpSubPortEgressFcosMapId,'cienaCesDpSubPortEgressFcosMapName':cienaCesDpSubPortEgressFcosMapName,'cienaCesDpSubPortEgressL2PtTransform':cienaCesDpSubPortEgressL2PtTransform,'cienaCesDpSubPortIngressL2Transform':cienaCesDpSubPortIngressL2Transform,'cienaCesDpSubPortEgressL2Transform':cienaCesDpSubPortEgressL2Transform,'cienaCesDpSubPortIngressL3TransformPolicy':cienaCesDpSubPortIngressL3TransformPolicy,'cienaCesDpSubPortEgressL3TransformPolicy':cienaCesDpSubPortEgressL3TransformPolicy,'cienaCesDpSubPortPrivateFwdGroup':cienaCesDpSubPortPrivateFwdGroup,'cienaCesDpSubPortFilterPolicy':cienaCesDpSubPortFilterPolicy,'cienaCesDpSubPortLogicalRingIndex':cienaCesDpSubPortLogicalRingIndex,'cienaCesDpSubPortVirtualRingIndex':cienaCesDpSubPortVirtualRingIndex,_As:cienaCesDpSubPortEgressReflectorMac,_At:cienaCesDpSubPortEgressGeneratorMac,'cienaCesDpSubPortQueueGroupProfileId':cienaCesDpSubPortQueueGroupProfileId,'cienaCesDpSubPortQueueGroupProfileName':cienaCesDpSubPortQueueGroupProfileName,'cienaCesDpSubPortQueueGroupInstanceId':cienaCesDpSubPortQueueGroupInstanceId,'cienaCesDpVirtualSwitch':cienaCesDpVirtualSwitch,'cienaCesDpVirtualSwitchTable':cienaCesDpVirtualSwitchTable,'cienaCesDpVirtualSwitchEntry':cienaCesDpVirtualSwitchEntry,_U:cienaCesDpVirtualSwitchIndex,_c:cienaCesDpVirtualSwitchRlanIndex,'cienaCesDpVirtualSwitchRlanTable':cienaCesDpVirtualSwitchRlanTable,'cienaCesDpVirtualSwitchRlanEntry':cienaCesDpVirtualSwitchRlanEntry,'cienaCesDpVirtualSwitchRlanName':cienaCesDpVirtualSwitchRlanName,'cienaCesDpVirtualSwitchRlanMcastForwardingMode':cienaCesDpVirtualSwitchRlanMcastForwardingMode,'cienaCesDpVirtualSwitchRlanL2CftStatus':cienaCesDpVirtualSwitchRlanL2CftStatus,'cienaCesDpVirtualSwitchRlanL2CftL2ControlRcos':cienaCesDpVirtualSwitchRlanL2CftL2ControlRcos,'cienaCesDpVirtualSwitchRlanMacLearningStatus':cienaCesDpVirtualSwitchRlanMacLearningStatus,'cienaCesDpVirtualSwitchRlanPrivateFwdGroupStatus':cienaCesDpVirtualSwitchRlanPrivateFwdGroupStatus,'cienaCesDpVirtualSwitchRlanPrivateFwdGroupAPolicy':cienaCesDpVirtualSwitchRlanPrivateFwdGroupAPolicy,'cienaCesDpVirtualSwitchRlanPrivateFwdGroupBPolicy':cienaCesDpVirtualSwitchRlanPrivateFwdGroupBPolicy,'cienaCesDpVirtualSwitchRlanPrivateFwdGroupCPolicy':cienaCesDpVirtualSwitchRlanPrivateFwdGroupCPolicy,'cienaCesDpVirtualSwitchRlanDescription':cienaCesDpVirtualSwitchRlanDescription,'cienaCesDpVirtualSwitchRlanPfgProfileId':cienaCesDpVirtualSwitchRlanPfgProfileId,'cienaCesDpVirtualSwitchRlanPfgProfileName':cienaCesDpVirtualSwitchRlanPfgProfileName,'cienaCesDpVirtualSwitchRlanL2CftProfileId':cienaCesDpVirtualSwitchRlanL2CftProfileId,'cienaCesDpVirtualSwitchRlanL2CftProfileName':cienaCesDpVirtualSwitchRlanL2CftProfileName,'cienaCesDpVirtualSwitchRlanLearnLimit':cienaCesDpVirtualSwitchRlanLearnLimit,'cienaCesDpVirtualSwitchRlanIfTable':cienaCesDpVirtualSwitchRlanIfTable,'cienaCesDpVirtualSwitchRlanIfEntry':cienaCesDpVirtualSwitchRlanIfEntry,_Aa:cienaCesDpVirtualSwitchRlanIfLiType,_Ab:cienaCesDpVirtualSwitchRlanIfLiIndex,'cienaCesDpVirtualSwitchRlanIfLportIngress':cienaCesDpVirtualSwitchRlanIfLportIngress,'cienaCesDpVirtualSwitchRlanIfLportEgress':cienaCesDpVirtualSwitchRlanIfLportEgress,'cienaCesDpVirtualSwitchRlanL2CftProtocolTable':cienaCesDpVirtualSwitchRlanL2CftProtocolTable,'cienaCesDpVirtualSwitchRlanL2CftProtocolEntry':cienaCesDpVirtualSwitchRlanL2CftProtocolEntry,_Ac:cienaCesDpVirtualSwitchRlanL2CftProtocolType,'cienaCesDpVirtualSwitchRlanL2CftProtocolDisposition':cienaCesDpVirtualSwitchRlanL2CftProtocolDisposition,'cienaCesDpQosFlow':cienaCesDpQosFlow,'cienaCesDpQosFlowTable':cienaCesDpQosFlowTable,'cienaCesDpQosFlowEntry':cienaCesDpQosFlowEntry,_Am:cienaCesDpQosFlowLiIndex,'cienaCesDpQosFlowName':cienaCesDpQosFlowName,'cienaCesDpQosFlowClassifierPrecedence':cienaCesDpQosFlowClassifierPrecedence,'cienaCesDpQosFlowParentIfId':cienaCesDpQosFlowParentIfId,'cienaCesDpQosFlowParentIfType':cienaCesDpQosFlowParentIfType,'cienaCesDpQosFlowIngressMeterProfileId':cienaCesDpQosFlowIngressMeterProfileId,'cienaCesDpQosFlowIngressMeterProfileName':cienaCesDpQosFlowIngressMeterProfileName,'cienaCesDpQosFlowIngressMeterPolicy':cienaCesDpQosFlowIngressMeterPolicy,'cienaCesDpQosFlowIngressRcosProfileId':cienaCesDpQosFlowIngressRcosProfileId,'cienaCesDpQosFlowIngressRcosProfileName':cienaCesDpQosFlowIngressRcosProfileName,'cienaCesDpQosFlowIngressRcosPolicy':cienaCesDpQosFlowIngressRcosPolicy,'cienaCesDpAccessFlow':cienaCesDpAccessFlow,'cienaCesDpAccessFlowTable':cienaCesDpAccessFlowTable,'cienaCesDpAccessFlowEntry':cienaCesDpAccessFlowEntry,_An:cienaCesDpAccessFlowLiIndex,'cienaCesDpAccessFlowName':cienaCesDpAccessFlowName,'cienaCesDpAccessFlowClassifierPrecedence':cienaCesDpAccessFlowClassifierPrecedence,'cienaCesDpAccessFlowParentIfId':cienaCesDpAccessFlowParentIfId,'cienaCesDpAccessFlowParentIfType':cienaCesDpAccessFlowParentIfType,'cienaCesDpAccessFlowFilterPolicy':cienaCesDpAccessFlowFilterPolicy,'cienaCesDpPbtTransit':cienaCesDpPbtTransit,'cienaCesDpPbtTransitTable':cienaCesDpPbtTransitTable,'cienaCesDpPbtTransitEntry':cienaCesDpPbtTransitEntry,_Ao:cienaCesDpPbtTransitLiIndex,'cienaCesDpPbtTransitName':cienaCesDpPbtTransitName,'cienaCesDpPbtTransitParentIfId':cienaCesDpPbtTransitParentIfId,'cienaCesDpPbtTransitIngressMeterProfileId':cienaCesDpPbtTransitIngressMeterProfileId,'cienaCesDpPbtTransitIngressMeterProfileName':cienaCesDpPbtTransitIngressMeterProfileName,'cienaCesDpPbtTransitIngressFloodContainerId':cienaCesDpPbtTransitIngressFloodContainerId,'cienaCesDpPbtTransitIngressFloodContainerName':cienaCesDpPbtTransitIngressFloodContainerName,'cienaCesDpPbtTransitIngressRcosProfileId':cienaCesDpPbtTransitIngressRcosProfileId,'cienaCesDpPbtTransitIngressRcosProfileName':cienaCesDpPbtTransitIngressRcosProfileName,'cienaCesDpPbtTransitIngressRcosPolicy':cienaCesDpPbtTransitIngressRcosPolicy,'cienaCesDpPbtTransitIngressFcosMapId':cienaCesDpPbtTransitIngressFcosMapId,'cienaCesDpPbtTransitIngressFcosMapName':cienaCesDpPbtTransitIngressFcosMapName,'cienaCesDpPbtTransitEgressFcosMapId':cienaCesDpPbtTransitEgressFcosMapId,'cienaCesDpPbtTransitEgressFcosMapName':cienaCesDpPbtTransitEgressFcosMapName,'cienaCesDpPbtTransitIngressBvidTransform':cienaCesDpPbtTransitIngressBvidTransform,'cienaCesDpPbtTransitEgressBvidTransform':cienaCesDpPbtTransitEgressBvidTransform,'cienaCesDpPbtTransitVirtualSwitchId':cienaCesDpPbtTransitVirtualSwitchId,'cienaCesDpPbtTransitRlanId':cienaCesDpPbtTransitRlanId,'cienaCesDpPbtTransitVirtualSwitchName':cienaCesDpPbtTransitVirtualSwitchName,'cienaCesDpPbtTransitPrivateFwdGroup':cienaCesDpPbtTransitPrivateFwdGroup,'cienaCesDpPbtTransitIngressMeterPolicy':cienaCesDpPbtTransitIngressMeterPolicy,'cienaCesDpCpuSubInterface':cienaCesDpCpuSubInterface,'cienaCesDpCpuSubInterfaceTable':cienaCesDpCpuSubInterfaceTable,'cienaCesDpCpuSubInterfaceEntry':cienaCesDpCpuSubInterfaceEntry,_Ap:cienaCesDpCpuSubInterfaceIndex,'cienaCesDpCpuSubInterfaceName':cienaCesDpCpuSubInterfaceName,'cienaCesDpCpuSubInterfaceEgressL2Transform':cienaCesDpCpuSubInterfaceEgressL2Transform,'cienaCesDpCpuSubInterfaceIngressL2Transform':cienaCesDpCpuSubInterfaceIngressL2Transform,'cienaCesDpCpuSubInterfaceEgressL3TransformPolicy':cienaCesDpCpuSubInterfaceEgressL3TransformPolicy,'cienaCesDpCpuSubInterfaceEgressRCosPolicy':cienaCesDpCpuSubInterfaceEgressRCosPolicy,'cienaCesDpCpuSubInterfaceEgressRCosProfileIndex':cienaCesDpCpuSubInterfaceEgressRCosProfileIndex,'cienaCesDpCpuSubInterfaceEgressRCosProfile':cienaCesDpCpuSubInterfaceEgressRCosProfile,'cienaCesDpCpuSubInterfaceVirtualSwitchIndex':cienaCesDpCpuSubInterfaceVirtualSwitchIndex,'cienaCesDpCpuSubInterfaceRlanIndex':cienaCesDpCpuSubInterfaceRlanIndex,'cienaCesDpCpuSubInterfaceVirtualSwitchName':cienaCesDpCpuSubInterfaceVirtualSwitchName,'cienaCesDpPfgProfile':cienaCesDpPfgProfile,'cienaCesDpPfgProfileTable':cienaCesDpPfgProfileTable,'cienaCesDpPfgProfileEntry':cienaCesDpPfgProfileEntry,_Aq:cienaCesDpPfgProfileIndex,'cienaCesDpPfgProfileName':cienaCesDpPfgProfileName,'cienaCesDpPfgProfileAPolicy':cienaCesDpPfgProfileAPolicy,'cienaCesDpPfgProfileBPolicy':cienaCesDpPfgProfileBPolicy,'cienaCesDpPfgProfileCPolicy':cienaCesDpPfgProfileCPolicy,'cienaCesDpL2CftProfile':cienaCesDpL2CftProfile,'cienaCesDpL2CftProfileTable':cienaCesDpL2CftProfileTable,'cienaCesDpL2CftProfileEntry':cienaCesDpL2CftProfileEntry,_x:cienaCesDpL2CftProfileIndex,'cienaCesDpL2CftProfileName':cienaCesDpL2CftProfileName,'cienaCesDpL2CftProfileL2ControlRcos':cienaCesDpL2CftProfileL2ControlRcos,'cienaCesDpL2CftProfileL2CftProtocolTable':cienaCesDpL2CftProfileL2CftProtocolTable,'cienaCesDpL2CftProfileL2CftProtocolEntry':cienaCesDpL2CftProfileL2CftProtocolEntry,_Ar:cienaCesDpL2CftProfileL2CftProtocolType,'cienaCesDpL2CftProfileL2CftProtocolDisposition':cienaCesDpL2CftProfileL2CftProtocolDisposition,'cienaCesDpMIBNotificationPrefix':cienaCesDpMIBNotificationPrefix,'cienaCesDpMIBNotifications':cienaCesDpMIBNotifications,'cienaCesDpTsMeterFloodContainerUcastThresholdExceeded':cienaCesDpTsMeterFloodContainerUcastThresholdExceeded,'cienaCesDpTsMeterFloodContainerUcastThresholdNormal':cienaCesDpTsMeterFloodContainerUcastThresholdNormal,'cienaCesDpTsMeterFloodContainerBcastThresholdExceeded':cienaCesDpTsMeterFloodContainerBcastThresholdExceeded,'cienaCesDpTsMeterFloodContainerBcastThresholdNormal':cienaCesDpTsMeterFloodContainerBcastThresholdNormal,'cienaCesDpTsMeterFloodContainerL2McastThresholdExceeded':cienaCesDpTsMeterFloodContainerL2McastThresholdExceeded,'cienaCesDpTsMeterFloodContainerL2McastThresholdNormal':cienaCesDpTsMeterFloodContainerL2McastThresholdNormal,'cienaCesDataplaneEgressReflectorEnabled':cienaCesDataplaneEgressReflectorEnabled,'cienaCesDataplaneEgressReflectorDisabled':cienaCesDataplaneEgressReflectorDisabled,'cienaCesDpPortShapingSubscriptionExceedsOperSpeed':cienaCesDpPortShapingSubscriptionExceedsOperSpeed,'cienaCesDpPortShapingSubscriptionWithinOperSpeed':cienaCesDpPortShapingSubscriptionWithinOperSpeed,'cienaCesDpTsMeterFloodContainerTotalThresholdExceeded':cienaCesDpTsMeterFloodContainerTotalThresholdExceeded,'cienaCesDpTsMeterFloodContainerTotalThresholdNormal':cienaCesDpTsMeterFloodContainerTotalThresholdNormal})