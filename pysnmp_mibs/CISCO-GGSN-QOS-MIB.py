_AO='cggsnQosUmtsCacGroupRev2'
_AN='cggsnQosUmtsCacGroupRev1'
_AM='cggsnQosUmtsCacGroup'
_AL='cggsnUmtsQosCacTcRevBitRate'
_AK='cggsnUmtsQosMapImsSigTrafHandPri'
_AJ='cggsnUmtsQosMapImsSigTrafClass'
_AI='cggsnQosUmtsDscpUnmodified'
_AH='cggsnQosDscp'
_AG='cggsnQosUmtsPdps'
_AF='cggsnQosUmtsDiffServPhbgroup'
_AE='cggsnQosBestEffortMeanThroughput'
_AD='cggsnQosNormalMeanThroughput'
_AC='cggsnQosPremiumMeanThroughput'
_AB='cggsnQosBestEffrtBandWidthFactor'
_AA='cggsnQosPremiumMtDeviationFactor'
_A9='cggsnQosCurrentUsedBandwidth'
_A8='cggsnQosTotalBandwidthResrc'
_A7='cggsnQosCurrentPdps'
_A6='cggsnQosMappedIpTos'
_A5='cggsnQosMappingMethod'
_A4='cggsnQosBWPoolTrafClass'
_A3='cggsnUmtsQosCacTcDirection'
_A2='cggsnUmtsQosCacTcBitRateType'
_A1='cggsnUmtsQosCacTcTrafClass'
_A0='priority3'
_z='priority2'
_y='priority1'
_x='UmtsQosTrafficClass'
_w='cggsnQosDiffServPhb'
_v='bestEffort'
_u='efClass'
_t='signallingClass'
_s='cggsnQosUmtsTrafficClass'
_r='cggsnQosClass'
_q='background'
_p='interactive'
_o='streaming'
_n='conversational'
_m='cggsnUmtsQosCacTcBitRate'
_l='cggsnUmtsQosCacBWPoolName'
_k='Kbps'
_j='cggsnUmtsQosCacPolicyName'
_i='bytes/sec'
_h='bits/sec'
_g='SnmpAdminString'
_f='cggsnQosBWPoolTrafClassAvailBw'
_e='cggsnQosBWPoolTrafClassAbsVal'
_d='cggsnQosBWPoolTrafClassPerVal'
_c='cggsnQosBWPoolTrafClassPercent'
_b='cggsnQosBWPoolTrafClassRowStatus'
_a='cggsnUmtsQosCacBWPoolBWVal'
_Z='cggsnUmtsQosCacBWPoolRowStatus'
_Y='cggsnUmtsQosCacTcReject'
_X='cggsnUmtsQosCacTcRowStatus'
_W='cggsnUmtsQosCacMaxDelayClassRej'
_V='cggsnUmtsQosCacMaxDelayClass'
_U='cggsnUmtsQosCacMaxThruPutReject'
_T='cggsnUmtsQosCacMaxThruPut'
_S='cggsnUmtsQosCacMaxTrafHandPrio'
_R='cggsnUmtsQosCacMaxTrafficClass'
_Q='cggsnUmtsQosCacPdpThreshold'
_P='cggsnUmtsQosCacMaxPdp'
_O='cggsnUmtsQosCacRowStatus'
_N='none'
_M='cggsnQosUmtsQosGroup'
_L='TruthValue'
_K='cggsnQosCanonicalQosGroup'
_J='cggsnQosGeneralConfigGroup'
_I='read-only'
_H='deprecated'
_G='not-accessible'
_F='read-write'
_E='Unsigned32'
_D='Integer32'
_C='read-create'
_B='current'
_A='CISCO-GGSN-QOS-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB',_g)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_E,'iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention',_L)
cggsnQosMIB=ModuleIdentity((1,3,6,1,4,1,9,9,241))
if mibBuilder.loadTexts:cggsnQosMIB.setRevisions(('2008-12-17 00:00','2006-09-11 00:00','2005-03-21 17:00','2003-11-27 13:00','2002-04-18 14:00','2001-12-06 13:30'))
class UmtsQosTrafficClass(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_n,1),(_o,2),(_p,3),(_q,4)))
_CggsnQosMIBObjects_ObjectIdentity=ObjectIdentity
cggsnQosMIBObjects=_CggsnQosMIBObjects_ObjectIdentity((1,3,6,1,4,1,9,9,241,1))
_CggsnQosGeneralConfig_ObjectIdentity=ObjectIdentity
cggsnQosGeneralConfig=_CggsnQosGeneralConfig_ObjectIdentity((1,3,6,1,4,1,9,9,241,1,1))
class _CggsnQosMappingMethod_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_N,1),('canonical',2),('delay',3),('umts',4)))
_CggsnQosMappingMethod_Type.__name__=_D
_CggsnQosMappingMethod_Object=MibScalar
cggsnQosMappingMethod=_CggsnQosMappingMethod_Object((1,3,6,1,4,1,9,9,241,1,1,1),_CggsnQosMappingMethod_Type())
cggsnQosMappingMethod.setMaxAccess(_F)
if mibBuilder.loadTexts:cggsnQosMappingMethod.setStatus(_B)
_CggsnQosClassIpTosMapTable_Object=MibTable
cggsnQosClassIpTosMapTable=_CggsnQosClassIpTosMapTable_Object((1,3,6,1,4,1,9,9,241,1,1,2))
if mibBuilder.loadTexts:cggsnQosClassIpTosMapTable.setStatus(_B)
_CggsnQosClassIpTosMapEntry_Object=MibTableRow
cggsnQosClassIpTosMapEntry=_CggsnQosClassIpTosMapEntry_Object((1,3,6,1,4,1,9,9,241,1,1,2,1))
cggsnQosClassIpTosMapEntry.setIndexNames((0,_A,_r))
if mibBuilder.loadTexts:cggsnQosClassIpTosMapEntry.setStatus(_B)
class _CggsnQosClass_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4))
_CggsnQosClass_Type.__name__=_D
_CggsnQosClass_Object=MibTableColumn
cggsnQosClass=_CggsnQosClass_Object((1,3,6,1,4,1,9,9,241,1,1,2,1,1),_CggsnQosClass_Type())
cggsnQosClass.setMaxAccess(_G)
if mibBuilder.loadTexts:cggsnQosClass.setStatus(_B)
class _CggsnQosMappedIpTos_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,5))
_CggsnQosMappedIpTos_Type.__name__=_D
_CggsnQosMappedIpTos_Object=MibTableColumn
cggsnQosMappedIpTos=_CggsnQosMappedIpTos_Object((1,3,6,1,4,1,9,9,241,1,1,2,1,2),_CggsnQosMappedIpTos_Type())
cggsnQosMappedIpTos.setMaxAccess(_F)
if mibBuilder.loadTexts:cggsnQosMappedIpTos.setStatus(_B)
_CggsnQosCurrentPdps_Type=Gauge32
_CggsnQosCurrentPdps_Object=MibTableColumn
cggsnQosCurrentPdps=_CggsnQosCurrentPdps_Object((1,3,6,1,4,1,9,9,241,1,1,2,1,3),_CggsnQosCurrentPdps_Type())
cggsnQosCurrentPdps.setMaxAccess(_I)
if mibBuilder.loadTexts:cggsnQosCurrentPdps.setStatus(_B)
_CggsnQosCanonicalQos_ObjectIdentity=ObjectIdentity
cggsnQosCanonicalQos=_CggsnQosCanonicalQos_ObjectIdentity((1,3,6,1,4,1,9,9,241,1,2))
class _CggsnQosTotalBandwidthResrc_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_CggsnQosTotalBandwidthResrc_Type.__name__=_E
_CggsnQosTotalBandwidthResrc_Object=MibScalar
cggsnQosTotalBandwidthResrc=_CggsnQosTotalBandwidthResrc_Object((1,3,6,1,4,1,9,9,241,1,2,1),_CggsnQosTotalBandwidthResrc_Type())
cggsnQosTotalBandwidthResrc.setMaxAccess(_F)
if mibBuilder.loadTexts:cggsnQosTotalBandwidthResrc.setStatus(_B)
if mibBuilder.loadTexts:cggsnQosTotalBandwidthResrc.setUnits(_h)
_CggsnQosCurrentUsedBandwidth_Type=Gauge32
_CggsnQosCurrentUsedBandwidth_Object=MibScalar
cggsnQosCurrentUsedBandwidth=_CggsnQosCurrentUsedBandwidth_Object((1,3,6,1,4,1,9,9,241,1,2,2),_CggsnQosCurrentUsedBandwidth_Type())
cggsnQosCurrentUsedBandwidth.setMaxAccess(_I)
if mibBuilder.loadTexts:cggsnQosCurrentUsedBandwidth.setStatus(_B)
if mibBuilder.loadTexts:cggsnQosCurrentUsedBandwidth.setUnits(_h)
class _CggsnQosPremiumMtDeviationFactor_Type(Unsigned32):defaultValue=100;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1000))
_CggsnQosPremiumMtDeviationFactor_Type.__name__=_E
_CggsnQosPremiumMtDeviationFactor_Object=MibScalar
cggsnQosPremiumMtDeviationFactor=_CggsnQosPremiumMtDeviationFactor_Object((1,3,6,1,4,1,9,9,241,1,2,3),_CggsnQosPremiumMtDeviationFactor_Type())
cggsnQosPremiumMtDeviationFactor.setMaxAccess(_F)
if mibBuilder.loadTexts:cggsnQosPremiumMtDeviationFactor.setStatus(_B)
class _CggsnQosBestEffrtBandWidthFactor_Type(Unsigned32):defaultValue=10;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4000000))
_CggsnQosBestEffrtBandWidthFactor_Type.__name__=_E
_CggsnQosBestEffrtBandWidthFactor_Object=MibScalar
cggsnQosBestEffrtBandWidthFactor=_CggsnQosBestEffrtBandWidthFactor_Object((1,3,6,1,4,1,9,9,241,1,2,4),_CggsnQosBestEffrtBandWidthFactor_Type())
cggsnQosBestEffrtBandWidthFactor.setMaxAccess(_F)
if mibBuilder.loadTexts:cggsnQosBestEffrtBandWidthFactor.setStatus(_B)
if mibBuilder.loadTexts:cggsnQosBestEffrtBandWidthFactor.setUnits(_h)
_CggsnQosPremiumMeanThroughput_Type=Gauge32
_CggsnQosPremiumMeanThroughput_Object=MibScalar
cggsnQosPremiumMeanThroughput=_CggsnQosPremiumMeanThroughput_Object((1,3,6,1,4,1,9,9,241,1,2,5),_CggsnQosPremiumMeanThroughput_Type())
cggsnQosPremiumMeanThroughput.setMaxAccess(_I)
if mibBuilder.loadTexts:cggsnQosPremiumMeanThroughput.setStatus(_B)
if mibBuilder.loadTexts:cggsnQosPremiumMeanThroughput.setUnits(_i)
_CggsnQosNormalMeanThroughput_Type=Gauge32
_CggsnQosNormalMeanThroughput_Object=MibScalar
cggsnQosNormalMeanThroughput=_CggsnQosNormalMeanThroughput_Object((1,3,6,1,4,1,9,9,241,1,2,6),_CggsnQosNormalMeanThroughput_Type())
cggsnQosNormalMeanThroughput.setMaxAccess(_I)
if mibBuilder.loadTexts:cggsnQosNormalMeanThroughput.setStatus(_B)
if mibBuilder.loadTexts:cggsnQosNormalMeanThroughput.setUnits(_i)
_CggsnQosBestEffortMeanThroughput_Type=Gauge32
_CggsnQosBestEffortMeanThroughput_Object=MibScalar
cggsnQosBestEffortMeanThroughput=_CggsnQosBestEffortMeanThroughput_Object((1,3,6,1,4,1,9,9,241,1,2,7),_CggsnQosBestEffortMeanThroughput_Type())
cggsnQosBestEffortMeanThroughput.setMaxAccess(_I)
if mibBuilder.loadTexts:cggsnQosBestEffortMeanThroughput.setStatus(_B)
if mibBuilder.loadTexts:cggsnQosBestEffortMeanThroughput.setUnits(_i)
_CggsnQosUmtsQos_ObjectIdentity=ObjectIdentity
cggsnQosUmtsQos=_CggsnQosUmtsQos_ObjectIdentity((1,3,6,1,4,1,9,9,241,1,3))
_CggsnQosTrafficClassPhbTable_Object=MibTable
cggsnQosTrafficClassPhbTable=_CggsnQosTrafficClassPhbTable_Object((1,3,6,1,4,1,9,9,241,1,3,1))
if mibBuilder.loadTexts:cggsnQosTrafficClassPhbTable.setStatus(_B)
_CggsnQosTrafficClassPhbEntry_Object=MibTableRow
cggsnQosTrafficClassPhbEntry=_CggsnQosTrafficClassPhbEntry_Object((1,3,6,1,4,1,9,9,241,1,3,1,1))
cggsnQosTrafficClassPhbEntry.setIndexNames((0,_A,_s))
if mibBuilder.loadTexts:cggsnQosTrafficClassPhbEntry.setStatus(_B)
class _CggsnQosUmtsTrafficClass_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('signalling',1),(_n,2),(_o,3),(_p,4),(_q,5)))
_CggsnQosUmtsTrafficClass_Type.__name__=_D
_CggsnQosUmtsTrafficClass_Object=MibTableColumn
cggsnQosUmtsTrafficClass=_CggsnQosUmtsTrafficClass_Object((1,3,6,1,4,1,9,9,241,1,3,1,1,1),_CggsnQosUmtsTrafficClass_Type())
cggsnQosUmtsTrafficClass.setMaxAccess(_G)
if mibBuilder.loadTexts:cggsnQosUmtsTrafficClass.setStatus(_B)
class _CggsnQosUmtsDiffServPhbgroup_Type(Integer32):defaultValue=7;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*((_t,1),(_u,2),('afClass1',3),('afClass2',4),('afClass3',5),('afClass4',6),(_v,7)))
_CggsnQosUmtsDiffServPhbgroup_Type.__name__=_D
_CggsnQosUmtsDiffServPhbgroup_Object=MibTableColumn
cggsnQosUmtsDiffServPhbgroup=_CggsnQosUmtsDiffServPhbgroup_Object((1,3,6,1,4,1,9,9,241,1,3,1,1,2),_CggsnQosUmtsDiffServPhbgroup_Type())
cggsnQosUmtsDiffServPhbgroup.setMaxAccess(_F)
if mibBuilder.loadTexts:cggsnQosUmtsDiffServPhbgroup.setStatus(_B)
_CggsnQosUmtsPdps_Type=Gauge32
_CggsnQosUmtsPdps_Object=MibTableColumn
cggsnQosUmtsPdps=_CggsnQosUmtsPdps_Object((1,3,6,1,4,1,9,9,241,1,3,1,1,3),_CggsnQosUmtsPdps_Type())
cggsnQosUmtsPdps.setMaxAccess(_I)
if mibBuilder.loadTexts:cggsnQosUmtsPdps.setStatus(_B)
_CggsnQosPhbToDscpMapTable_Object=MibTable
cggsnQosPhbToDscpMapTable=_CggsnQosPhbToDscpMapTable_Object((1,3,6,1,4,1,9,9,241,1,3,2))
if mibBuilder.loadTexts:cggsnQosPhbToDscpMapTable.setStatus(_B)
_CggsnQosPhbToDscpMapEntry_Object=MibTableRow
cggsnQosPhbToDscpMapEntry=_CggsnQosPhbToDscpMapEntry_Object((1,3,6,1,4,1,9,9,241,1,3,2,1))
cggsnQosPhbToDscpMapEntry.setIndexNames((0,_A,_w))
if mibBuilder.loadTexts:cggsnQosPhbToDscpMapEntry.setStatus(_B)
class _CggsnQosDiffServPhb_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15)));namedValues=NamedValues(*((_t,1),(_u,2),('afClass1Low',3),('afClass1Medium',4),('afClass1High',5),('afClass2Low',6),('afClass2Medium',7),('afClass2High',8),('afClass3Low',9),('afClass3Medium',10),('afClass3High',11),('afClass4Low',12),('afClass4Medium',13),('afClass4High',14),(_v,15)))
_CggsnQosDiffServPhb_Type.__name__=_D
_CggsnQosDiffServPhb_Object=MibTableColumn
cggsnQosDiffServPhb=_CggsnQosDiffServPhb_Object((1,3,6,1,4,1,9,9,241,1,3,2,1,1),_CggsnQosDiffServPhb_Type())
cggsnQosDiffServPhb.setMaxAccess(_G)
if mibBuilder.loadTexts:cggsnQosDiffServPhb.setStatus(_B)
class _CggsnQosDscp_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,63))
_CggsnQosDscp_Type.__name__=_D
_CggsnQosDscp_Object=MibTableColumn
cggsnQosDscp=_CggsnQosDscp_Object((1,3,6,1,4,1,9,9,241,1,3,2,1,2),_CggsnQosDscp_Type())
cggsnQosDscp.setMaxAccess(_F)
if mibBuilder.loadTexts:cggsnQosDscp.setStatus(_B)
class _CggsnQosUmtsDscpUnmodified_Type(Integer32):defaultValue=4;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('up',1),('down',2),('all',3),(_N,4)))
_CggsnQosUmtsDscpUnmodified_Type.__name__=_D
_CggsnQosUmtsDscpUnmodified_Object=MibScalar
cggsnQosUmtsDscpUnmodified=_CggsnQosUmtsDscpUnmodified_Object((1,3,6,1,4,1,9,9,241,1,3,3),_CggsnQosUmtsDscpUnmodified_Type())
cggsnQosUmtsDscpUnmodified.setMaxAccess(_F)
if mibBuilder.loadTexts:cggsnQosUmtsDscpUnmodified.setStatus(_B)
_CggsnQosUmtsCac_ObjectIdentity=ObjectIdentity
cggsnQosUmtsCac=_CggsnQosUmtsCac_ObjectIdentity((1,3,6,1,4,1,9,9,241,1,3,4))
class _CggsnUmtsQosMapImsSigTrafClass_Type(UmtsQosTrafficClass):defaultValue=3
_CggsnUmtsQosMapImsSigTrafClass_Type.__name__=_x
_CggsnUmtsQosMapImsSigTrafClass_Object=MibScalar
cggsnUmtsQosMapImsSigTrafClass=_CggsnUmtsQosMapImsSigTrafClass_Object((1,3,6,1,4,1,9,9,241,1,3,4,1),_CggsnUmtsQosMapImsSigTrafClass_Type())
cggsnUmtsQosMapImsSigTrafClass.setMaxAccess(_F)
if mibBuilder.loadTexts:cggsnUmtsQosMapImsSigTrafClass.setStatus(_H)
class _CggsnUmtsQosMapImsSigTrafHandPri_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_y,1),(_z,2),(_A0,3)))
_CggsnUmtsQosMapImsSigTrafHandPri_Type.__name__=_D
_CggsnUmtsQosMapImsSigTrafHandPri_Object=MibScalar
cggsnUmtsQosMapImsSigTrafHandPri=_CggsnUmtsQosMapImsSigTrafHandPri_Object((1,3,6,1,4,1,9,9,241,1,3,4,2),_CggsnUmtsQosMapImsSigTrafHandPri_Type())
cggsnUmtsQosMapImsSigTrafHandPri.setMaxAccess(_F)
if mibBuilder.loadTexts:cggsnUmtsQosMapImsSigTrafHandPri.setStatus(_H)
_CggsnUmtsQosCacPolicyTable_Object=MibTable
cggsnUmtsQosCacPolicyTable=_CggsnUmtsQosCacPolicyTable_Object((1,3,6,1,4,1,9,9,241,1,3,4,3))
if mibBuilder.loadTexts:cggsnUmtsQosCacPolicyTable.setStatus(_B)
_CggsnUmtsQosCacPolicyEntry_Object=MibTableRow
cggsnUmtsQosCacPolicyEntry=_CggsnUmtsQosCacPolicyEntry_Object((1,3,6,1,4,1,9,9,241,1,3,4,3,1))
cggsnUmtsQosCacPolicyEntry.setIndexNames((0,_A,_j))
if mibBuilder.loadTexts:cggsnUmtsQosCacPolicyEntry.setStatus(_B)
class _CggsnUmtsQosCacPolicyName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,40))
_CggsnUmtsQosCacPolicyName_Type.__name__=_g
_CggsnUmtsQosCacPolicyName_Object=MibTableColumn
cggsnUmtsQosCacPolicyName=_CggsnUmtsQosCacPolicyName_Object((1,3,6,1,4,1,9,9,241,1,3,4,3,1,1),_CggsnUmtsQosCacPolicyName_Type())
cggsnUmtsQosCacPolicyName.setMaxAccess(_G)
if mibBuilder.loadTexts:cggsnUmtsQosCacPolicyName.setStatus(_B)
_CggsnUmtsQosCacRowStatus_Type=RowStatus
_CggsnUmtsQosCacRowStatus_Object=MibTableColumn
cggsnUmtsQosCacRowStatus=_CggsnUmtsQosCacRowStatus_Object((1,3,6,1,4,1,9,9,241,1,3,4,3,1,2),_CggsnUmtsQosCacRowStatus_Type())
cggsnUmtsQosCacRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:cggsnUmtsQosCacRowStatus.setStatus(_B)
class _CggsnUmtsQosCacMaxPdp_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_CggsnUmtsQosCacMaxPdp_Type.__name__=_E
_CggsnUmtsQosCacMaxPdp_Object=MibTableColumn
cggsnUmtsQosCacMaxPdp=_CggsnUmtsQosCacMaxPdp_Object((1,3,6,1,4,1,9,9,241,1,3,4,3,1,3),_CggsnUmtsQosCacMaxPdp_Type())
cggsnUmtsQosCacMaxPdp.setMaxAccess(_C)
if mibBuilder.loadTexts:cggsnUmtsQosCacMaxPdp.setStatus(_B)
class _CggsnUmtsQosCacPdpThreshold_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_CggsnUmtsQosCacPdpThreshold_Type.__name__=_E
_CggsnUmtsQosCacPdpThreshold_Object=MibTableColumn
cggsnUmtsQosCacPdpThreshold=_CggsnUmtsQosCacPdpThreshold_Object((1,3,6,1,4,1,9,9,241,1,3,4,3,1,4),_CggsnUmtsQosCacPdpThreshold_Type())
cggsnUmtsQosCacPdpThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:cggsnUmtsQosCacPdpThreshold.setStatus(_B)
_CggsnUmtsQosCacMaxTrafficClass_Type=UmtsQosTrafficClass
_CggsnUmtsQosCacMaxTrafficClass_Object=MibTableColumn
cggsnUmtsQosCacMaxTrafficClass=_CggsnUmtsQosCacMaxTrafficClass_Object((1,3,6,1,4,1,9,9,241,1,3,4,3,1,5),_CggsnUmtsQosCacMaxTrafficClass_Type())
cggsnUmtsQosCacMaxTrafficClass.setMaxAccess(_C)
if mibBuilder.loadTexts:cggsnUmtsQosCacMaxTrafficClass.setStatus(_B)
class _CggsnUmtsQosCacMaxTrafHandPrio_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*((_N,0),(_y,1),(_z,2),(_A0,3)))
_CggsnUmtsQosCacMaxTrafHandPrio_Type.__name__=_D
_CggsnUmtsQosCacMaxTrafHandPrio_Object=MibTableColumn
cggsnUmtsQosCacMaxTrafHandPrio=_CggsnUmtsQosCacMaxTrafHandPrio_Object((1,3,6,1,4,1,9,9,241,1,3,4,3,1,6),_CggsnUmtsQosCacMaxTrafHandPrio_Type())
cggsnUmtsQosCacMaxTrafHandPrio.setMaxAccess(_C)
if mibBuilder.loadTexts:cggsnUmtsQosCacMaxTrafHandPrio.setStatus(_B)
class _CggsnUmtsQosCacMaxThruPut_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_CggsnUmtsQosCacMaxThruPut_Type.__name__=_E
_CggsnUmtsQosCacMaxThruPut_Object=MibTableColumn
cggsnUmtsQosCacMaxThruPut=_CggsnUmtsQosCacMaxThruPut_Object((1,3,6,1,4,1,9,9,241,1,3,4,3,1,7),_CggsnUmtsQosCacMaxThruPut_Type())
cggsnUmtsQosCacMaxThruPut.setMaxAccess(_C)
if mibBuilder.loadTexts:cggsnUmtsQosCacMaxThruPut.setStatus(_B)
class _CggsnUmtsQosCacMaxThruPutReject_Type(TruthValue):defaultValue=2
_CggsnUmtsQosCacMaxThruPutReject_Type.__name__=_L
_CggsnUmtsQosCacMaxThruPutReject_Object=MibTableColumn
cggsnUmtsQosCacMaxThruPutReject=_CggsnUmtsQosCacMaxThruPutReject_Object((1,3,6,1,4,1,9,9,241,1,3,4,3,1,8),_CggsnUmtsQosCacMaxThruPutReject_Type())
cggsnUmtsQosCacMaxThruPutReject.setMaxAccess(_C)
if mibBuilder.loadTexts:cggsnUmtsQosCacMaxThruPutReject.setStatus(_B)
class _CggsnUmtsQosCacMaxDelayClass_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4)));namedValues=NamedValues(*((_N,0),('delayClass1',1),('delayClass2',2),('delayClass3',3),('delayClass4',4)))
_CggsnUmtsQosCacMaxDelayClass_Type.__name__=_D
_CggsnUmtsQosCacMaxDelayClass_Object=MibTableColumn
cggsnUmtsQosCacMaxDelayClass=_CggsnUmtsQosCacMaxDelayClass_Object((1,3,6,1,4,1,9,9,241,1,3,4,3,1,9),_CggsnUmtsQosCacMaxDelayClass_Type())
cggsnUmtsQosCacMaxDelayClass.setMaxAccess(_C)
if mibBuilder.loadTexts:cggsnUmtsQosCacMaxDelayClass.setStatus(_B)
class _CggsnUmtsQosCacMaxDelayClassRej_Type(TruthValue):defaultValue=2
_CggsnUmtsQosCacMaxDelayClassRej_Type.__name__=_L
_CggsnUmtsQosCacMaxDelayClassRej_Object=MibTableColumn
cggsnUmtsQosCacMaxDelayClassRej=_CggsnUmtsQosCacMaxDelayClassRej_Object((1,3,6,1,4,1,9,9,241,1,3,4,3,1,10),_CggsnUmtsQosCacMaxDelayClassRej_Type())
cggsnUmtsQosCacMaxDelayClassRej.setMaxAccess(_C)
if mibBuilder.loadTexts:cggsnUmtsQosCacMaxDelayClassRej.setStatus(_B)
_CggsnUmtsQosCacTcTable_Object=MibTable
cggsnUmtsQosCacTcTable=_CggsnUmtsQosCacTcTable_Object((1,3,6,1,4,1,9,9,241,1,3,4,4))
if mibBuilder.loadTexts:cggsnUmtsQosCacTcTable.setStatus(_B)
_CggsnUmtsQosCacTcEntry_Object=MibTableRow
cggsnUmtsQosCacTcEntry=_CggsnUmtsQosCacTcEntry_Object((1,3,6,1,4,1,9,9,241,1,3,4,4,1))
cggsnUmtsQosCacTcEntry.setIndexNames((0,_A,_j),(0,_A,_A1),(0,_A,_A2),(0,_A,_A3))
if mibBuilder.loadTexts:cggsnUmtsQosCacTcEntry.setStatus(_B)
_CggsnUmtsQosCacTcTrafClass_Type=UmtsQosTrafficClass
_CggsnUmtsQosCacTcTrafClass_Object=MibTableColumn
cggsnUmtsQosCacTcTrafClass=_CggsnUmtsQosCacTcTrafClass_Object((1,3,6,1,4,1,9,9,241,1,3,4,4,1,1),_CggsnUmtsQosCacTcTrafClass_Type())
cggsnUmtsQosCacTcTrafClass.setMaxAccess(_G)
if mibBuilder.loadTexts:cggsnUmtsQosCacTcTrafClass.setStatus(_B)
class _CggsnUmtsQosCacTcBitRateType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('maximum',1),('guaranteed',2)))
_CggsnUmtsQosCacTcBitRateType_Type.__name__=_D
_CggsnUmtsQosCacTcBitRateType_Object=MibTableColumn
cggsnUmtsQosCacTcBitRateType=_CggsnUmtsQosCacTcBitRateType_Object((1,3,6,1,4,1,9,9,241,1,3,4,4,1,2),_CggsnUmtsQosCacTcBitRateType_Type())
cggsnUmtsQosCacTcBitRateType.setMaxAccess(_G)
if mibBuilder.loadTexts:cggsnUmtsQosCacTcBitRateType.setStatus(_B)
class _CggsnUmtsQosCacTcDirection_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('uplink',1),('downlink',2)))
_CggsnUmtsQosCacTcDirection_Type.__name__=_D
_CggsnUmtsQosCacTcDirection_Object=MibTableColumn
cggsnUmtsQosCacTcDirection=_CggsnUmtsQosCacTcDirection_Object((1,3,6,1,4,1,9,9,241,1,3,4,4,1,3),_CggsnUmtsQosCacTcDirection_Type())
cggsnUmtsQosCacTcDirection.setMaxAccess(_G)
if mibBuilder.loadTexts:cggsnUmtsQosCacTcDirection.setStatus(_B)
_CggsnUmtsQosCacTcRowStatus_Type=RowStatus
_CggsnUmtsQosCacTcRowStatus_Object=MibTableColumn
cggsnUmtsQosCacTcRowStatus=_CggsnUmtsQosCacTcRowStatus_Object((1,3,6,1,4,1,9,9,241,1,3,4,4,1,4),_CggsnUmtsQosCacTcRowStatus_Type())
cggsnUmtsQosCacTcRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:cggsnUmtsQosCacTcRowStatus.setStatus(_B)
class _CggsnUmtsQosCacTcBitRate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,16000))
_CggsnUmtsQosCacTcBitRate_Type.__name__=_D
_CggsnUmtsQosCacTcBitRate_Object=MibTableColumn
cggsnUmtsQosCacTcBitRate=_CggsnUmtsQosCacTcBitRate_Object((1,3,6,1,4,1,9,9,241,1,3,4,4,1,5),_CggsnUmtsQosCacTcBitRate_Type())
cggsnUmtsQosCacTcBitRate.setMaxAccess(_C)
if mibBuilder.loadTexts:cggsnUmtsQosCacTcBitRate.setStatus(_H)
if mibBuilder.loadTexts:cggsnUmtsQosCacTcBitRate.setUnits(_k)
class _CggsnUmtsQosCacTcReject_Type(TruthValue):defaultValue=2
_CggsnUmtsQosCacTcReject_Type.__name__=_L
_CggsnUmtsQosCacTcReject_Object=MibTableColumn
cggsnUmtsQosCacTcReject=_CggsnUmtsQosCacTcReject_Object((1,3,6,1,4,1,9,9,241,1,3,4,4,1,6),_CggsnUmtsQosCacTcReject_Type())
cggsnUmtsQosCacTcReject.setMaxAccess(_C)
if mibBuilder.loadTexts:cggsnUmtsQosCacTcReject.setStatus(_B)
class _CggsnUmtsQosCacTcRevBitRate_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,256000))
_CggsnUmtsQosCacTcRevBitRate_Type.__name__=_E
_CggsnUmtsQosCacTcRevBitRate_Object=MibTableColumn
cggsnUmtsQosCacTcRevBitRate=_CggsnUmtsQosCacTcRevBitRate_Object((1,3,6,1,4,1,9,9,241,1,3,4,4,1,7),_CggsnUmtsQosCacTcRevBitRate_Type())
cggsnUmtsQosCacTcRevBitRate.setMaxAccess(_C)
if mibBuilder.loadTexts:cggsnUmtsQosCacTcRevBitRate.setStatus(_B)
if mibBuilder.loadTexts:cggsnUmtsQosCacTcRevBitRate.setUnits(_k)
_CggsnUmtsQosCacBWPoolTable_Object=MibTable
cggsnUmtsQosCacBWPoolTable=_CggsnUmtsQosCacBWPoolTable_Object((1,3,6,1,4,1,9,9,241,1,3,4,5))
if mibBuilder.loadTexts:cggsnUmtsQosCacBWPoolTable.setStatus(_B)
_CggsnUmtsQosCacBWPoolEntry_Object=MibTableRow
cggsnUmtsQosCacBWPoolEntry=_CggsnUmtsQosCacBWPoolEntry_Object((1,3,6,1,4,1,9,9,241,1,3,4,5,1))
cggsnUmtsQosCacBWPoolEntry.setIndexNames((0,_A,_l))
if mibBuilder.loadTexts:cggsnUmtsQosCacBWPoolEntry.setStatus(_B)
class _CggsnUmtsQosCacBWPoolName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,40))
_CggsnUmtsQosCacBWPoolName_Type.__name__=_g
_CggsnUmtsQosCacBWPoolName_Object=MibTableColumn
cggsnUmtsQosCacBWPoolName=_CggsnUmtsQosCacBWPoolName_Object((1,3,6,1,4,1,9,9,241,1,3,4,5,1,1),_CggsnUmtsQosCacBWPoolName_Type())
cggsnUmtsQosCacBWPoolName.setMaxAccess(_G)
if mibBuilder.loadTexts:cggsnUmtsQosCacBWPoolName.setStatus(_B)
_CggsnUmtsQosCacBWPoolRowStatus_Type=RowStatus
_CggsnUmtsQosCacBWPoolRowStatus_Object=MibTableColumn
cggsnUmtsQosCacBWPoolRowStatus=_CggsnUmtsQosCacBWPoolRowStatus_Object((1,3,6,1,4,1,9,9,241,1,3,4,5,1,2),_CggsnUmtsQosCacBWPoolRowStatus_Type())
cggsnUmtsQosCacBWPoolRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:cggsnUmtsQosCacBWPoolRowStatus.setStatus(_B)
class _CggsnUmtsQosCacBWPoolBWVal_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_CggsnUmtsQosCacBWPoolBWVal_Type.__name__=_E
_CggsnUmtsQosCacBWPoolBWVal_Object=MibTableColumn
cggsnUmtsQosCacBWPoolBWVal=_CggsnUmtsQosCacBWPoolBWVal_Object((1,3,6,1,4,1,9,9,241,1,3,4,5,1,3),_CggsnUmtsQosCacBWPoolBWVal_Type())
cggsnUmtsQosCacBWPoolBWVal.setMaxAccess(_C)
if mibBuilder.loadTexts:cggsnUmtsQosCacBWPoolBWVal.setStatus(_B)
if mibBuilder.loadTexts:cggsnUmtsQosCacBWPoolBWVal.setUnits(_k)
_CggsnQosBWPoolTrafClassTable_Object=MibTable
cggsnQosBWPoolTrafClassTable=_CggsnQosBWPoolTrafClassTable_Object((1,3,6,1,4,1,9,9,241,1,3,4,6))
if mibBuilder.loadTexts:cggsnQosBWPoolTrafClassTable.setStatus(_B)
_CggsnQosBWPoolTrafClassEntry_Object=MibTableRow
cggsnQosBWPoolTrafClassEntry=_CggsnQosBWPoolTrafClassEntry_Object((1,3,6,1,4,1,9,9,241,1,3,4,6,1))
cggsnQosBWPoolTrafClassEntry.setIndexNames((0,_A,_l),(0,_A,_A4))
if mibBuilder.loadTexts:cggsnQosBWPoolTrafClassEntry.setStatus(_B)
_CggsnQosBWPoolTrafClass_Type=UmtsQosTrafficClass
_CggsnQosBWPoolTrafClass_Object=MibTableColumn
cggsnQosBWPoolTrafClass=_CggsnQosBWPoolTrafClass_Object((1,3,6,1,4,1,9,9,241,1,3,4,6,1,1),_CggsnQosBWPoolTrafClass_Type())
cggsnQosBWPoolTrafClass.setMaxAccess(_G)
if mibBuilder.loadTexts:cggsnQosBWPoolTrafClass.setStatus(_B)
_CggsnQosBWPoolTrafClassRowStatus_Type=RowStatus
_CggsnQosBWPoolTrafClassRowStatus_Object=MibTableColumn
cggsnQosBWPoolTrafClassRowStatus=_CggsnQosBWPoolTrafClassRowStatus_Object((1,3,6,1,4,1,9,9,241,1,3,4,6,1,2),_CggsnQosBWPoolTrafClassRowStatus_Type())
cggsnQosBWPoolTrafClassRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:cggsnQosBWPoolTrafClassRowStatus.setStatus(_B)
class _CggsnQosBWPoolTrafClassPercent_Type(TruthValue):defaultValue=2
_CggsnQosBWPoolTrafClassPercent_Type.__name__=_L
_CggsnQosBWPoolTrafClassPercent_Object=MibTableColumn
cggsnQosBWPoolTrafClassPercent=_CggsnQosBWPoolTrafClassPercent_Object((1,3,6,1,4,1,9,9,241,1,3,4,6,1,3),_CggsnQosBWPoolTrafClassPercent_Type())
cggsnQosBWPoolTrafClassPercent.setMaxAccess(_C)
if mibBuilder.loadTexts:cggsnQosBWPoolTrafClassPercent.setStatus(_B)
class _CggsnQosBWPoolTrafClassPerVal_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_CggsnQosBWPoolTrafClassPerVal_Type.__name__=_D
_CggsnQosBWPoolTrafClassPerVal_Object=MibTableColumn
cggsnQosBWPoolTrafClassPerVal=_CggsnQosBWPoolTrafClassPerVal_Object((1,3,6,1,4,1,9,9,241,1,3,4,6,1,4),_CggsnQosBWPoolTrafClassPerVal_Type())
cggsnQosBWPoolTrafClassPerVal.setMaxAccess(_C)
if mibBuilder.loadTexts:cggsnQosBWPoolTrafClassPerVal.setStatus(_B)
class _CggsnQosBWPoolTrafClassAbsVal_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_CggsnQosBWPoolTrafClassAbsVal_Type.__name__=_E
_CggsnQosBWPoolTrafClassAbsVal_Object=MibTableColumn
cggsnQosBWPoolTrafClassAbsVal=_CggsnQosBWPoolTrafClassAbsVal_Object((1,3,6,1,4,1,9,9,241,1,3,4,6,1,5),_CggsnQosBWPoolTrafClassAbsVal_Type())
cggsnQosBWPoolTrafClassAbsVal.setMaxAccess(_C)
if mibBuilder.loadTexts:cggsnQosBWPoolTrafClassAbsVal.setStatus(_B)
class _CggsnQosBWPoolTrafClassAvailBw_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_CggsnQosBWPoolTrafClassAvailBw_Type.__name__=_E
_CggsnQosBWPoolTrafClassAvailBw_Object=MibTableColumn
cggsnQosBWPoolTrafClassAvailBw=_CggsnQosBWPoolTrafClassAvailBw_Object((1,3,6,1,4,1,9,9,241,1,3,4,6,1,6),_CggsnQosBWPoolTrafClassAvailBw_Type())
cggsnQosBWPoolTrafClassAvailBw.setMaxAccess(_I)
if mibBuilder.loadTexts:cggsnQosBWPoolTrafClassAvailBw.setStatus(_B)
_CggsnQosMIBConformances_ObjectIdentity=ObjectIdentity
cggsnQosMIBConformances=_CggsnQosMIBConformances_ObjectIdentity((1,3,6,1,4,1,9,9,241,2))
_CggsnQosMIBCompliances_ObjectIdentity=ObjectIdentity
cggsnQosMIBCompliances=_CggsnQosMIBCompliances_ObjectIdentity((1,3,6,1,4,1,9,9,241,2,1))
_CggsnQosMIBGroups_ObjectIdentity=ObjectIdentity
cggsnQosMIBGroups=_CggsnQosMIBGroups_ObjectIdentity((1,3,6,1,4,1,9,9,241,2,2))
cggsnQosGeneralConfigGroup=ObjectGroup((1,3,6,1,4,1,9,9,241,2,2,1))
cggsnQosGeneralConfigGroup.setObjects(*((_A,_A5),(_A,_A6),(_A,_A7)))
if mibBuilder.loadTexts:cggsnQosGeneralConfigGroup.setStatus(_B)
cggsnQosCanonicalQosGroup=ObjectGroup((1,3,6,1,4,1,9,9,241,2,2,2))
cggsnQosCanonicalQosGroup.setObjects(*((_A,_A8),(_A,_A9),(_A,_AA),(_A,_AB),(_A,_AC),(_A,_AD),(_A,_AE)))
if mibBuilder.loadTexts:cggsnQosCanonicalQosGroup.setStatus(_B)
cggsnQosUmtsQosGroup=ObjectGroup((1,3,6,1,4,1,9,9,241,2,2,3))
cggsnQosUmtsQosGroup.setObjects(*((_A,_AF),(_A,_AG),(_A,_AH),(_A,_AI)))
if mibBuilder.loadTexts:cggsnQosUmtsQosGroup.setStatus(_B)
cggsnQosUmtsCacGroup=ObjectGroup((1,3,6,1,4,1,9,9,241,2,2,4))
cggsnQosUmtsCacGroup.setObjects(*((_A,_AJ),(_A,_AK),(_A,_O),(_A,_P),(_A,_Q),(_A,_R),(_A,_S),(_A,_T),(_A,_U),(_A,_V),(_A,_W),(_A,_X),(_A,_m),(_A,_Y),(_A,_Z),(_A,_a),(_A,_b),(_A,_c),(_A,_d),(_A,_e),(_A,_f)))
if mibBuilder.loadTexts:cggsnQosUmtsCacGroup.setStatus(_H)
cggsnQosUmtsCacGroupRev1=ObjectGroup((1,3,6,1,4,1,9,9,241,2,2,5))
cggsnQosUmtsCacGroupRev1.setObjects(*((_A,_O),(_A,_P),(_A,_Q),(_A,_R),(_A,_S),(_A,_T),(_A,_U),(_A,_V),(_A,_W),(_A,_X),(_A,_m),(_A,_Y),(_A,_Z),(_A,_a),(_A,_b),(_A,_c),(_A,_d),(_A,_e),(_A,_f)))
if mibBuilder.loadTexts:cggsnQosUmtsCacGroupRev1.setStatus(_H)
cggsnQosUmtsCacGroupRev2=ObjectGroup((1,3,6,1,4,1,9,9,241,2,2,6))
cggsnQosUmtsCacGroupRev2.setObjects(*((_A,_O),(_A,_P),(_A,_Q),(_A,_R),(_A,_S),(_A,_T),(_A,_U),(_A,_V),(_A,_W),(_A,_X),(_A,_Y),(_A,_AL),(_A,_Z),(_A,_a),(_A,_b),(_A,_c),(_A,_d),(_A,_e),(_A,_f)))
if mibBuilder.loadTexts:cggsnQosUmtsCacGroupRev2.setStatus(_B)
cggsnQosMIBCompliance=ModuleCompliance((1,3,6,1,4,1,9,9,241,2,1,1))
cggsnQosMIBCompliance.setObjects(*((_A,_J),(_A,_K)))
if mibBuilder.loadTexts:cggsnQosMIBCompliance.setStatus('obsolete')
cggsnQosMIBComplianceRev1=ModuleCompliance((1,3,6,1,4,1,9,9,241,2,1,2))
cggsnQosMIBComplianceRev1.setObjects(*((_A,_J),(_A,_K),(_A,_M)))
if mibBuilder.loadTexts:cggsnQosMIBComplianceRev1.setStatus(_H)
cggsnQosMIBComplianceRev2=ModuleCompliance((1,3,6,1,4,1,9,9,241,2,1,3))
cggsnQosMIBComplianceRev2.setObjects(*((_A,_J),(_A,_K),(_A,_M),(_A,_AM)))
if mibBuilder.loadTexts:cggsnQosMIBComplianceRev2.setStatus(_H)
cggsnQosMIBComplianceRev3=ModuleCompliance((1,3,6,1,4,1,9,9,241,2,1,4))
cggsnQosMIBComplianceRev3.setObjects(*((_A,_J),(_A,_K),(_A,_M),(_A,_AN)))
if mibBuilder.loadTexts:cggsnQosMIBComplianceRev3.setStatus(_H)
cggsnQosMIBComplianceRev4=ModuleCompliance((1,3,6,1,4,1,9,9,241,2,1,5))
cggsnQosMIBComplianceRev4.setObjects(*((_A,_J),(_A,_K),(_A,_M),(_A,_AO)))
if mibBuilder.loadTexts:cggsnQosMIBComplianceRev4.setStatus(_B)
mibBuilder.exportSymbols(_A,**{_x:UmtsQosTrafficClass,'cggsnQosMIB':cggsnQosMIB,'cggsnQosMIBObjects':cggsnQosMIBObjects,'cggsnQosGeneralConfig':cggsnQosGeneralConfig,_A5:cggsnQosMappingMethod,'cggsnQosClassIpTosMapTable':cggsnQosClassIpTosMapTable,'cggsnQosClassIpTosMapEntry':cggsnQosClassIpTosMapEntry,_r:cggsnQosClass,_A6:cggsnQosMappedIpTos,_A7:cggsnQosCurrentPdps,'cggsnQosCanonicalQos':cggsnQosCanonicalQos,_A8:cggsnQosTotalBandwidthResrc,_A9:cggsnQosCurrentUsedBandwidth,_AA:cggsnQosPremiumMtDeviationFactor,_AB:cggsnQosBestEffrtBandWidthFactor,_AC:cggsnQosPremiumMeanThroughput,_AD:cggsnQosNormalMeanThroughput,_AE:cggsnQosBestEffortMeanThroughput,'cggsnQosUmtsQos':cggsnQosUmtsQos,'cggsnQosTrafficClassPhbTable':cggsnQosTrafficClassPhbTable,'cggsnQosTrafficClassPhbEntry':cggsnQosTrafficClassPhbEntry,_s:cggsnQosUmtsTrafficClass,_AF:cggsnQosUmtsDiffServPhbgroup,_AG:cggsnQosUmtsPdps,'cggsnQosPhbToDscpMapTable':cggsnQosPhbToDscpMapTable,'cggsnQosPhbToDscpMapEntry':cggsnQosPhbToDscpMapEntry,_w:cggsnQosDiffServPhb,_AH:cggsnQosDscp,_AI:cggsnQosUmtsDscpUnmodified,'cggsnQosUmtsCac':cggsnQosUmtsCac,_AJ:cggsnUmtsQosMapImsSigTrafClass,_AK:cggsnUmtsQosMapImsSigTrafHandPri,'cggsnUmtsQosCacPolicyTable':cggsnUmtsQosCacPolicyTable,'cggsnUmtsQosCacPolicyEntry':cggsnUmtsQosCacPolicyEntry,_j:cggsnUmtsQosCacPolicyName,_O:cggsnUmtsQosCacRowStatus,_P:cggsnUmtsQosCacMaxPdp,_Q:cggsnUmtsQosCacPdpThreshold,_R:cggsnUmtsQosCacMaxTrafficClass,_S:cggsnUmtsQosCacMaxTrafHandPrio,_T:cggsnUmtsQosCacMaxThruPut,_U:cggsnUmtsQosCacMaxThruPutReject,_V:cggsnUmtsQosCacMaxDelayClass,_W:cggsnUmtsQosCacMaxDelayClassRej,'cggsnUmtsQosCacTcTable':cggsnUmtsQosCacTcTable,'cggsnUmtsQosCacTcEntry':cggsnUmtsQosCacTcEntry,_A1:cggsnUmtsQosCacTcTrafClass,_A2:cggsnUmtsQosCacTcBitRateType,_A3:cggsnUmtsQosCacTcDirection,_X:cggsnUmtsQosCacTcRowStatus,_m:cggsnUmtsQosCacTcBitRate,_Y:cggsnUmtsQosCacTcReject,_AL:cggsnUmtsQosCacTcRevBitRate,'cggsnUmtsQosCacBWPoolTable':cggsnUmtsQosCacBWPoolTable,'cggsnUmtsQosCacBWPoolEntry':cggsnUmtsQosCacBWPoolEntry,_l:cggsnUmtsQosCacBWPoolName,_Z:cggsnUmtsQosCacBWPoolRowStatus,_a:cggsnUmtsQosCacBWPoolBWVal,'cggsnQosBWPoolTrafClassTable':cggsnQosBWPoolTrafClassTable,'cggsnQosBWPoolTrafClassEntry':cggsnQosBWPoolTrafClassEntry,_A4:cggsnQosBWPoolTrafClass,_b:cggsnQosBWPoolTrafClassRowStatus,_c:cggsnQosBWPoolTrafClassPercent,_d:cggsnQosBWPoolTrafClassPerVal,_e:cggsnQosBWPoolTrafClassAbsVal,_f:cggsnQosBWPoolTrafClassAvailBw,'cggsnQosMIBConformances':cggsnQosMIBConformances,'cggsnQosMIBCompliances':cggsnQosMIBCompliances,'cggsnQosMIBCompliance':cggsnQosMIBCompliance,'cggsnQosMIBComplianceRev1':cggsnQosMIBComplianceRev1,'cggsnQosMIBComplianceRev2':cggsnQosMIBComplianceRev2,'cggsnQosMIBComplianceRev3':cggsnQosMIBComplianceRev3,'cggsnQosMIBComplianceRev4':cggsnQosMIBComplianceRev4,'cggsnQosMIBGroups':cggsnQosMIBGroups,_J:cggsnQosGeneralConfigGroup,_K:cggsnQosCanonicalQosGroup,_M:cggsnQosUmtsQosGroup,_AM:cggsnQosUmtsCacGroup,_AN:cggsnQosUmtsCacGroupRev1,_AO:cggsnQosUmtsCacGroupRev2})