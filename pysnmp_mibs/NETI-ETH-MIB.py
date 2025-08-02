_A4='ethIfQDropThresDropPrecedence'
_A3='IfgProtectionStatus'
_A2='ethEtsLocalDsti'
_A1='ethEtsTConnectionIndex'
_A0='notApplicable'
_z='AdvertisedFlowControl'
_y='AdvertisedDuplex'
_x='AdvertisedSpeed'
_w='ethIfVLANSetIndex'
_v='TrafficClass'
_u='ethFwdDiffservIndex'
_t='taildrop'
_s='legacy'
_r='provider'
_q='customer'
_p='transparent'
_o='b10GbaseZR'
_n='b10GbaseER'
_m='b10GbaseLRM'
_l='b10GbaseLR'
_k='b10GbaseSR'
_j='b1000baseT'
_i='b1000baseLX'
_h='b1000baseSX'
_g='b100baseTX'
_f='halfDuplex'
_e='fullDuplex'
_d='ethIfQueueTrafficClass'
_c='all'
_b='process'
_a='nomac'
_Z='mac'
_Y='Timeout'
_X='ethFwdIndex'
_W='forward'
_V='drop'
_U='SnmpAdminString'
_T='OctetString'
_S='untagged'
_R='vlanTagged'
_Q='centi-seconds'
_P='off'
_O='on'
_N='not-accessible'
_M='TruthValue'
_L='auto'
_K='Bits'
_J='ethIfIndex'
_I='read-create'
_H='ethDevIndex'
_G='Unsigned32'
_F='FrameProcess'
_E='NETI-ETH-MIB'
_D='Integer32'
_C='read-write'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_T,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
Dsti,=mibBuilder.importSymbols('NETI-CHMGR-MIB','Dsti')
netiGeneric,=mibBuilder.importSymbols('NETI-COMMON-MIB','netiGeneric')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB',_U)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI',_K,'Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_G,'iso')
DisplayString,PhysAddress,RowPointer,RowStatus,TextualConvention,TimeStamp,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowPointer','RowStatus','TextualConvention','TimeStamp',_M)
netiEthMIB=ModuleIdentity((1,3,6,1,4,1,2928,2,2))
if mibBuilder.loadTexts:netiEthMIB.setRevisions(('2014-03-20 10:00','2013-02-28 10:00','2012-09-12 10:00','2012-01-27 15:00','2011-10-26 09:00','2011-09-05 11:00','2010-10-20 16:00','2009-07-08 12:00'))
class TrafficClass(TextualConvention,Integer32):status=_A;displayHint='d';subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
class VLANSet(TextualConvention,OctetString):status=_A;displayHint='1x';subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(512,512));fixedLength=512
class AdvertisedSpeed(TextualConvention,Bits):status=_A;namedValues=NamedValues(*((_L,0),('b10',1),('b100',2),('b1000',3),('b10g',4)))
class AdvertisedDuplex(TextualConvention,Bits):status=_A;namedValues=NamedValues(*((_L,0),(_e,1),(_f,2)))
class AdvertisedFlowControl(TextualConvention,Bits):status=_A;namedValues=NamedValues(*((_L,0),('pause',1),('asmDir',2)))
class BridgeIdentifier(TextualConvention,OctetString):status=_A;displayHint='1x:';subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(8,8));fixedLength=8
class EthInterfaceType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7,8,9,10,11,12)));namedValues=NamedValues(*((_L,0),('unknown',1),('bETS',2),(_g,3),(_h,4),(_i,5),(_j,6),('bETSGroup',7),(_k,8),(_l,9),(_m,10),(_n,11),(_o,12)))
class PortIdentifier(TextualConvention,OctetString):status=_A;subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(2,2));fixedLength=2
class Timeout(TextualConvention,Integer32):status=_A;displayHint='d'
class FrameProcess(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('notSupported',0),(_V,1),(_W,2)))
class InterfaceIndexList(TextualConvention,OctetString):status=_A;displayHint='4d,'
class IfgProtectionStatus(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('unavailable',1),('unprotected',2),('standbyProtected',3),('hitlessCapable',4),('hitlessProtected',5)))
_EthObjects_ObjectIdentity=ObjectIdentity
ethObjects=_EthObjects_ObjectIdentity((1,3,6,1,4,1,2928,2,2,1))
_EthDeviceGroup_ObjectIdentity=ObjectIdentity
ethDeviceGroup=_EthDeviceGroup_ObjectIdentity((1,3,6,1,4,1,2928,2,2,1,1))
_EthDeviceTable_Object=MibTable
ethDeviceTable=_EthDeviceTable_Object((1,3,6,1,4,1,2928,2,2,1,1,1))
if mibBuilder.loadTexts:ethDeviceTable.setStatus(_A)
_EthDeviceEntry_Object=MibTableRow
ethDeviceEntry=_EthDeviceEntry_Object((1,3,6,1,4,1,2928,2,2,1,1,1,1))
ethDeviceEntry.setIndexNames((0,_E,_H))
if mibBuilder.loadTexts:ethDeviceEntry.setStatus(_A)
_EthDevIndex_Type=Unsigned32
_EthDevIndex_Object=MibTableColumn
ethDevIndex=_EthDevIndex_Object((1,3,6,1,4,1,2928,2,2,1,1,1,1,1),_EthDevIndex_Type())
ethDevIndex.setMaxAccess(_N)
if mibBuilder.loadTexts:ethDevIndex.setStatus(_A)
_EthDevRowStatus_Type=RowStatus
_EthDevRowStatus_Object=MibTableColumn
ethDevRowStatus=_EthDevRowStatus_Object((1,3,6,1,4,1,2928,2,2,1,1,1,1,2),_EthDevRowStatus_Type())
ethDevRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:ethDevRowStatus.setStatus(_A)
_EthDevName_Type=SnmpAdminString
_EthDevName_Object=MibTableColumn
ethDevName=_EthDevName_Object((1,3,6,1,4,1,2928,2,2,1,1,1,1,3),_EthDevName_Type())
ethDevName.setMaxAccess(_B)
if mibBuilder.loadTexts:ethDevName.setStatus(_A)
_EthDevContainerName_Type=SnmpAdminString
_EthDevContainerName_Object=MibTableColumn
ethDevContainerName=_EthDevContainerName_Object((1,3,6,1,4,1,2928,2,2,1,1,1,1,4),_EthDevContainerName_Type())
ethDevContainerName.setMaxAccess(_B)
if mibBuilder.loadTexts:ethDevContainerName.setStatus(_A)
_EthDevProductName_Type=SnmpAdminString
_EthDevProductName_Object=MibTableColumn
ethDevProductName=_EthDevProductName_Object((1,3,6,1,4,1,2928,2,2,1,1,1,1,5),_EthDevProductName_Type())
ethDevProductName.setMaxAccess(_B)
if mibBuilder.loadTexts:ethDevProductName.setStatus(_A)
class _EthDevStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('present',1),('absent',2),('mismatch',3)))
_EthDevStatus_Type.__name__=_D
_EthDevStatus_Object=MibTableColumn
ethDevStatus=_EthDevStatus_Object((1,3,6,1,4,1,2928,2,2,1,1,1,1,6),_EthDevStatus_Type())
ethDevStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:ethDevStatus.setStatus(_A)
class _EthDevCapJumboFrames_Type(Bits):namedValues=NamedValues(*((_O,0),(_P,1)))
_EthDevCapJumboFrames_Type.__name__=_K
_EthDevCapJumboFrames_Object=MibTableColumn
ethDevCapJumboFrames=_EthDevCapJumboFrames_Object((1,3,6,1,4,1,2928,2,2,1,1,1,1,7),_EthDevCapJumboFrames_Type())
ethDevCapJumboFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:ethDevCapJumboFrames.setStatus(_A)
_EthDevCapMaxAgingTime_Type=Unsigned32
_EthDevCapMaxAgingTime_Object=MibTableColumn
ethDevCapMaxAgingTime=_EthDevCapMaxAgingTime_Object((1,3,6,1,4,1,2928,2,2,1,1,1,1,8),_EthDevCapMaxAgingTime_Type())
ethDevCapMaxAgingTime.setMaxAccess(_B)
if mibBuilder.loadTexts:ethDevCapMaxAgingTime.setStatus(_A)
class _EthDevCapMACMode_Type(Bits):namedValues=NamedValues(*((_L,0),(_Z,1),(_a,2)))
_EthDevCapMACMode_Type.__name__=_K
_EthDevCapMACMode_Object=MibTableColumn
ethDevCapMACMode=_EthDevCapMACMode_Object((1,3,6,1,4,1,2928,2,2,1,1,1,1,9),_EthDevCapMACMode_Type())
ethDevCapMACMode.setMaxAccess(_B)
if mibBuilder.loadTexts:ethDevCapMACMode.setStatus(_A)
class _EthDevCapSpanningTree_Type(Bits):namedValues=NamedValues(*((_L,0),(_W,1),(_V,2),(_b,3)))
_EthDevCapSpanningTree_Type.__name__=_K
_EthDevCapSpanningTree_Object=MibTableColumn
ethDevCapSpanningTree=_EthDevCapSpanningTree_Object((1,3,6,1,4,1,2928,2,2,1,1,1,1,10),_EthDevCapSpanningTree_Type())
ethDevCapSpanningTree.setMaxAccess(_B)
if mibBuilder.loadTexts:ethDevCapSpanningTree.setStatus(_A)
class _EthDevCapVLANMode_Type(Bits):namedValues=NamedValues(*((_p,0),(_q,1),(_r,2)))
_EthDevCapVLANMode_Type.__name__=_K
_EthDevCapVLANMode_Object=MibTableColumn
ethDevCapVLANMode=_EthDevCapVLANMode_Object((1,3,6,1,4,1,2928,2,2,1,1,1,1,11),_EthDevCapVLANMode_Type())
ethDevCapVLANMode.setMaxAccess(_B)
if mibBuilder.loadTexts:ethDevCapVLANMode.setStatus(_A)
_EthDevCapAdvertisedDuplex_Type=AdvertisedDuplex
_EthDevCapAdvertisedDuplex_Object=MibTableColumn
ethDevCapAdvertisedDuplex=_EthDevCapAdvertisedDuplex_Object((1,3,6,1,4,1,2928,2,2,1,1,1,1,12),_EthDevCapAdvertisedDuplex_Type())
ethDevCapAdvertisedDuplex.setMaxAccess(_B)
if mibBuilder.loadTexts:ethDevCapAdvertisedDuplex.setStatus(_A)
_EthDevCapAdvertisedFlowControl_Type=AdvertisedFlowControl
_EthDevCapAdvertisedFlowControl_Object=MibTableColumn
ethDevCapAdvertisedFlowControl=_EthDevCapAdvertisedFlowControl_Object((1,3,6,1,4,1,2928,2,2,1,1,1,1,13),_EthDevCapAdvertisedFlowControl_Type())
ethDevCapAdvertisedFlowControl.setMaxAccess(_B)
if mibBuilder.loadTexts:ethDevCapAdvertisedFlowControl.setStatus(_A)
class _EthDevCapAcceptableFrameType_Type(Bits):namedValues=NamedValues(*((_c,0),(_R,1),(_S,2)))
_EthDevCapAcceptableFrameType_Type.__name__=_K
_EthDevCapAcceptableFrameType_Object=MibTableColumn
ethDevCapAcceptableFrameType=_EthDevCapAcceptableFrameType_Object((1,3,6,1,4,1,2928,2,2,1,1,1,1,14),_EthDevCapAcceptableFrameType_Type())
ethDevCapAcceptableFrameType.setMaxAccess(_B)
if mibBuilder.loadTexts:ethDevCapAcceptableFrameType.setStatus(_A)
class _EthDevCapDefaultEthernetPriority_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(2,2));fixedLength=2
_EthDevCapDefaultEthernetPriority_Type.__name__=_T
_EthDevCapDefaultEthernetPriority_Object=MibTableColumn
ethDevCapDefaultEthernetPriority=_EthDevCapDefaultEthernetPriority_Object((1,3,6,1,4,1,2928,2,2,1,1,1,1,15),_EthDevCapDefaultEthernetPriority_Type())
ethDevCapDefaultEthernetPriority.setMaxAccess(_B)
if mibBuilder.loadTexts:ethDevCapDefaultEthernetPriority.setStatus(_A)
class _EthDevCapLearning_Type(Bits):namedValues=NamedValues(*((_O,0),(_P,1)))
_EthDevCapLearning_Type.__name__=_K
_EthDevCapLearning_Object=MibTableColumn
ethDevCapLearning=_EthDevCapLearning_Object((1,3,6,1,4,1,2928,2,2,1,1,1,1,16),_EthDevCapLearning_Type())
ethDevCapLearning.setMaxAccess(_B)
if mibBuilder.loadTexts:ethDevCapLearning.setStatus(_A)
class _EthDevCapTransmittedFrameTypeETS_Type(Bits):namedValues=NamedValues(*((_R,1),(_S,2),(_s,3)))
_EthDevCapTransmittedFrameTypeETS_Type.__name__=_K
_EthDevCapTransmittedFrameTypeETS_Object=MibTableColumn
ethDevCapTransmittedFrameTypeETS=_EthDevCapTransmittedFrameTypeETS_Object((1,3,6,1,4,1,2928,2,2,1,1,1,1,17),_EthDevCapTransmittedFrameTypeETS_Type())
ethDevCapTransmittedFrameTypeETS.setMaxAccess(_B)
if mibBuilder.loadTexts:ethDevCapTransmittedFrameTypeETS.setStatus(_A)
class _EthDevCapTransmittedFrameTypeDot3_Type(Bits):namedValues=NamedValues(*((_R,1),(_S,2)))
_EthDevCapTransmittedFrameTypeDot3_Type.__name__=_K
_EthDevCapTransmittedFrameTypeDot3_Object=MibTableColumn
ethDevCapTransmittedFrameTypeDot3=_EthDevCapTransmittedFrameTypeDot3_Object((1,3,6,1,4,1,2928,2,2,1,1,1,1,18),_EthDevCapTransmittedFrameTypeDot3_Type())
ethDevCapTransmittedFrameTypeDot3.setMaxAccess(_B)
if mibBuilder.loadTexts:ethDevCapTransmittedFrameTypeDot3.setStatus(_A)
_EthDevCapMaxMaxQueueOctets_Type=Unsigned32
_EthDevCapMaxMaxQueueOctets_Object=MibTableColumn
ethDevCapMaxMaxQueueOctets=_EthDevCapMaxMaxQueueOctets_Object((1,3,6,1,4,1,2928,2,2,1,1,1,1,19),_EthDevCapMaxMaxQueueOctets_Type())
ethDevCapMaxMaxQueueOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:ethDevCapMaxMaxQueueOctets.setStatus(_A)
_EthDevCapMaxMaxQueueFrames_Type=Unsigned32
_EthDevCapMaxMaxQueueFrames_Object=MibTableColumn
ethDevCapMaxMaxQueueFrames=_EthDevCapMaxMaxQueueFrames_Object((1,3,6,1,4,1,2928,2,2,1,1,1,1,20),_EthDevCapMaxMaxQueueFrames_Type())
ethDevCapMaxMaxQueueFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:ethDevCapMaxMaxQueueFrames.setStatus('deprecated')
_EthDevCapMaxTrafficClass_Type=TrafficClass
_EthDevCapMaxTrafficClass_Object=MibTableColumn
ethDevCapMaxTrafficClass=_EthDevCapMaxTrafficClass_Object((1,3,6,1,4,1,2928,2,2,1,1,1,1,21),_EthDevCapMaxTrafficClass_Type())
ethDevCapMaxTrafficClass.setMaxAccess(_B)
if mibBuilder.loadTexts:ethDevCapMaxTrafficClass.setStatus(_A)
_EthDevEtsNextIndex_Type=Unsigned32
_EthDevEtsNextIndex_Object=MibTableColumn
ethDevEtsNextIndex=_EthDevEtsNextIndex_Object((1,3,6,1,4,1,2928,2,2,1,1,1,1,22),_EthDevEtsNextIndex_Type())
ethDevEtsNextIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:ethDevEtsNextIndex.setStatus(_A)
_EthDevFwdFuncNextIndex_Type=Unsigned32
_EthDevFwdFuncNextIndex_Object=MibTableColumn
ethDevFwdFuncNextIndex=_EthDevFwdFuncNextIndex_Object((1,3,6,1,4,1,2928,2,2,1,1,1,1,23),_EthDevFwdFuncNextIndex_Type())
ethDevFwdFuncNextIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:ethDevFwdFuncNextIndex.setStatus(_A)
class _EthDevCapPerformanceMonitoring_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_O,1),(_P,2)))
_EthDevCapPerformanceMonitoring_Type.__name__=_D
_EthDevCapPerformanceMonitoring_Object=MibTableColumn
ethDevCapPerformanceMonitoring=_EthDevCapPerformanceMonitoring_Object((1,3,6,1,4,1,2928,2,2,1,1,1,1,24),_EthDevCapPerformanceMonitoring_Type())
ethDevCapPerformanceMonitoring.setMaxAccess(_B)
if mibBuilder.loadTexts:ethDevCapPerformanceMonitoring.setStatus(_A)
class _EthDevCapConfigurableFaultMgmt_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_O,1),(_P,2)))
_EthDevCapConfigurableFaultMgmt_Type.__name__=_D
_EthDevCapConfigurableFaultMgmt_Object=MibTableColumn
ethDevCapConfigurableFaultMgmt=_EthDevCapConfigurableFaultMgmt_Object((1,3,6,1,4,1,2928,2,2,1,1,1,1,25),_EthDevCapConfigurableFaultMgmt_Type())
ethDevCapConfigurableFaultMgmt.setMaxAccess(_B)
if mibBuilder.loadTexts:ethDevCapConfigurableFaultMgmt.setStatus(_A)
_EthDevIfgFirstIndex_Type=Unsigned32
_EthDevIfgFirstIndex_Object=MibTableColumn
ethDevIfgFirstIndex=_EthDevIfgFirstIndex_Object((1,3,6,1,4,1,2928,2,2,1,1,1,1,26),_EthDevIfgFirstIndex_Type())
ethDevIfgFirstIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:ethDevIfgFirstIndex.setStatus(_A)
_EthDevIfgNextIndex_Type=Unsigned32
_EthDevIfgNextIndex_Object=MibTableColumn
ethDevIfgNextIndex=_EthDevIfgNextIndex_Object((1,3,6,1,4,1,2928,2,2,1,1,1,1,27),_EthDevIfgNextIndex_Type())
ethDevIfgNextIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:ethDevIfgNextIndex.setStatus(_A)
_EthDevCapDropPrecedenceLevels_Type=Unsigned32
_EthDevCapDropPrecedenceLevels_Object=MibTableColumn
ethDevCapDropPrecedenceLevels=_EthDevCapDropPrecedenceLevels_Object((1,3,6,1,4,1,2928,2,2,1,1,1,1,28),_EthDevCapDropPrecedenceLevels_Type())
ethDevCapDropPrecedenceLevels.setMaxAccess(_B)
if mibBuilder.loadTexts:ethDevCapDropPrecedenceLevels.setStatus(_A)
class _EthDevCapDropProbabilityFunctions_Type(Bits):namedValues=NamedValues(*((_t,0),('wred',1)))
_EthDevCapDropProbabilityFunctions_Type.__name__=_K
_EthDevCapDropProbabilityFunctions_Object=MibTableColumn
ethDevCapDropProbabilityFunctions=_EthDevCapDropProbabilityFunctions_Object((1,3,6,1,4,1,2928,2,2,1,1,1,1,29),_EthDevCapDropProbabilityFunctions_Type())
ethDevCapDropProbabilityFunctions.setMaxAccess(_B)
if mibBuilder.loadTexts:ethDevCapDropProbabilityFunctions.setStatus(_A)
_EthDevFailure_Type=SnmpAdminString
_EthDevFailure_Object=MibTableColumn
ethDevFailure=_EthDevFailure_Object((1,3,6,1,4,1,2928,2,2,1,1,1,1,30),_EthDevFailure_Type())
ethDevFailure.setMaxAccess(_B)
if mibBuilder.loadTexts:ethDevFailure.setStatus(_A)
_EthFwdFuncGroup_ObjectIdentity=ObjectIdentity
ethFwdFuncGroup=_EthFwdFuncGroup_ObjectIdentity((1,3,6,1,4,1,2928,2,2,1,2))
_EthFwdFuncLastChange_Type=TimeStamp
_EthFwdFuncLastChange_Object=MibScalar
ethFwdFuncLastChange=_EthFwdFuncLastChange_Object((1,3,6,1,4,1,2928,2,2,1,2,1),_EthFwdFuncLastChange_Type())
ethFwdFuncLastChange.setMaxAccess(_B)
if mibBuilder.loadTexts:ethFwdFuncLastChange.setStatus(_A)
_EthFwdFuncTable_Object=MibTable
ethFwdFuncTable=_EthFwdFuncTable_Object((1,3,6,1,4,1,2928,2,2,1,2,2))
if mibBuilder.loadTexts:ethFwdFuncTable.setStatus(_A)
_EthFwdFuncEntry_Object=MibTableRow
ethFwdFuncEntry=_EthFwdFuncEntry_Object((1,3,6,1,4,1,2928,2,2,1,2,2,1))
ethFwdFuncEntry.setIndexNames((0,_E,_H),(0,_E,_X))
if mibBuilder.loadTexts:ethFwdFuncEntry.setStatus(_A)
class _EthFwdIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_EthFwdIndex_Type.__name__=_D
_EthFwdIndex_Object=MibTableColumn
ethFwdIndex=_EthFwdIndex_Object((1,3,6,1,4,1,2928,2,2,1,2,2,1,1),_EthFwdIndex_Type())
ethFwdIndex.setMaxAccess(_N)
if mibBuilder.loadTexts:ethFwdIndex.setStatus(_A)
_EthFwdRowStatus_Type=RowStatus
_EthFwdRowStatus_Object=MibTableColumn
ethFwdRowStatus=_EthFwdRowStatus_Object((1,3,6,1,4,1,2928,2,2,1,2,2,1,2),_EthFwdRowStatus_Type())
ethFwdRowStatus.setMaxAccess(_I)
if mibBuilder.loadTexts:ethFwdRowStatus.setStatus(_A)
_EthFwdName_Type=SnmpAdminString
_EthFwdName_Object=MibTableColumn
ethFwdName=_EthFwdName_Object((1,3,6,1,4,1,2928,2,2,1,2,2,1,3),_EthFwdName_Type())
ethFwdName.setMaxAccess(_B)
if mibBuilder.loadTexts:ethFwdName.setStatus(_A)
class _EthFwdCustomerId_Type(Unsigned32):defaultValue=0
_EthFwdCustomerId_Type.__name__=_G
_EthFwdCustomerId_Object=MibTableColumn
ethFwdCustomerId=_EthFwdCustomerId_Object((1,3,6,1,4,1,2928,2,2,1,2,2,1,4),_EthFwdCustomerId_Type())
ethFwdCustomerId.setMaxAccess(_I)
if mibBuilder.loadTexts:ethFwdCustomerId.setStatus(_A)
class _EthFwdPurpose_Type(SnmpAdminString):defaultHexValue=''
_EthFwdPurpose_Type.__name__=_U
_EthFwdPurpose_Object=MibTableColumn
ethFwdPurpose=_EthFwdPurpose_Object((1,3,6,1,4,1,2928,2,2,1,2,2,1,5),_EthFwdPurpose_Type())
ethFwdPurpose.setMaxAccess(_I)
if mibBuilder.loadTexts:ethFwdPurpose.setStatus(_A)
class _EthFwdJumboFrames_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_O,1),(_P,2)))
_EthFwdJumboFrames_Type.__name__=_D
_EthFwdJumboFrames_Object=MibTableColumn
ethFwdJumboFrames=_EthFwdJumboFrames_Object((1,3,6,1,4,1,2928,2,2,1,2,2,1,6),_EthFwdJumboFrames_Type())
ethFwdJumboFrames.setMaxAccess(_C)
if mibBuilder.loadTexts:ethFwdJumboFrames.setStatus(_A)
class _EthFwdMACMode_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_L,1),(_Z,2),(_a,3)))
_EthFwdMACMode_Type.__name__=_D
_EthFwdMACMode_Object=MibTableColumn
ethFwdMACMode=_EthFwdMACMode_Object((1,3,6,1,4,1,2928,2,2,1,2,2,1,7),_EthFwdMACMode_Type())
ethFwdMACMode.setMaxAccess(_C)
if mibBuilder.loadTexts:ethFwdMACMode.setStatus(_A)
class _EthFwdCurrentMACMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(2,3)));namedValues=NamedValues(*((_Z,2),(_a,3)))
_EthFwdCurrentMACMode_Type.__name__=_D
_EthFwdCurrentMACMode_Object=MibTableColumn
ethFwdCurrentMACMode=_EthFwdCurrentMACMode_Object((1,3,6,1,4,1,2928,2,2,1,2,2,1,8),_EthFwdCurrentMACMode_Type())
ethFwdCurrentMACMode.setMaxAccess(_B)
if mibBuilder.loadTexts:ethFwdCurrentMACMode.setStatus(_A)
class _EthFwdSpanningTree_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_L,1),(_W,2),(_V,3),(_b,4)))
_EthFwdSpanningTree_Type.__name__=_D
_EthFwdSpanningTree_Object=MibTableColumn
ethFwdSpanningTree=_EthFwdSpanningTree_Object((1,3,6,1,4,1,2928,2,2,1,2,2,1,9),_EthFwdSpanningTree_Type())
ethFwdSpanningTree.setMaxAccess(_C)
if mibBuilder.loadTexts:ethFwdSpanningTree.setStatus(_A)
class _EthFwdVLANMode_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_p,1),(_q,2),(_r,3)))
_EthFwdVLANMode_Type.__name__=_D
_EthFwdVLANMode_Object=MibTableColumn
ethFwdVLANMode=_EthFwdVLANMode_Object((1,3,6,1,4,1,2928,2,2,1,2,2,1,10),_EthFwdVLANMode_Type())
ethFwdVLANMode.setMaxAccess(_C)
if mibBuilder.loadTexts:ethFwdVLANMode.setStatus(_A)
class _EthFwdAgingTime_Type(Unsigned32):defaultValue=300
_EthFwdAgingTime_Type.__name__=_G
_EthFwdAgingTime_Object=MibTableColumn
ethFwdAgingTime=_EthFwdAgingTime_Object((1,3,6,1,4,1,2928,2,2,1,2,2,1,11),_EthFwdAgingTime_Type())
ethFwdAgingTime.setMaxAccess(_C)
if mibBuilder.loadTexts:ethFwdAgingTime.setStatus(_A)
if mibBuilder.loadTexts:ethFwdAgingTime.setUnits('seconds')
_EthFwdFailure_Type=SnmpAdminString
_EthFwdFailure_Object=MibTableColumn
ethFwdFailure=_EthFwdFailure_Object((1,3,6,1,4,1,2928,2,2,1,2,2,1,12),_EthFwdFailure_Type())
ethFwdFailure.setMaxAccess(_B)
if mibBuilder.loadTexts:ethFwdFailure.setStatus(_A)
_EthFwdLastChange_Type=TimeTicks
_EthFwdLastChange_Object=MibTableColumn
ethFwdLastChange=_EthFwdLastChange_Object((1,3,6,1,4,1,2928,2,2,1,2,2,1,13),_EthFwdLastChange_Type())
ethFwdLastChange.setMaxAccess(_B)
if mibBuilder.loadTexts:ethFwdLastChange.setStatus(_A)
class _EthFwdPropagateFaults_Type(TruthValue):defaultValue=2
_EthFwdPropagateFaults_Type.__name__=_M
_EthFwdPropagateFaults_Object=MibTableColumn
ethFwdPropagateFaults=_EthFwdPropagateFaults_Object((1,3,6,1,4,1,2928,2,2,1,2,2,1,14),_EthFwdPropagateFaults_Type())
ethFwdPropagateFaults.setMaxAccess(_C)
if mibBuilder.loadTexts:ethFwdPropagateFaults.setStatus(_A)
class _EthFwdReservedAddr0180C2000002_Type(FrameProcess):defaultValue=1
_EthFwdReservedAddr0180C2000002_Type.__name__=_F
_EthFwdReservedAddr0180C2000002_Object=MibTableColumn
ethFwdReservedAddr0180C2000002=_EthFwdReservedAddr0180C2000002_Object((1,3,6,1,4,1,2928,2,2,1,2,2,1,15),_EthFwdReservedAddr0180C2000002_Type())
ethFwdReservedAddr0180C2000002.setMaxAccess(_C)
if mibBuilder.loadTexts:ethFwdReservedAddr0180C2000002.setStatus(_A)
class _EthFwdReservedAddr0180C2000003_Type(FrameProcess):defaultValue=1
_EthFwdReservedAddr0180C2000003_Type.__name__=_F
_EthFwdReservedAddr0180C2000003_Object=MibTableColumn
ethFwdReservedAddr0180C2000003=_EthFwdReservedAddr0180C2000003_Object((1,3,6,1,4,1,2928,2,2,1,2,2,1,16),_EthFwdReservedAddr0180C2000003_Type())
ethFwdReservedAddr0180C2000003.setMaxAccess(_C)
if mibBuilder.loadTexts:ethFwdReservedAddr0180C2000003.setStatus(_A)
class _EthFwdReservedAddr0180C2000004_Type(FrameProcess):defaultValue=1
_EthFwdReservedAddr0180C2000004_Type.__name__=_F
_EthFwdReservedAddr0180C2000004_Object=MibTableColumn
ethFwdReservedAddr0180C2000004=_EthFwdReservedAddr0180C2000004_Object((1,3,6,1,4,1,2928,2,2,1,2,2,1,17),_EthFwdReservedAddr0180C2000004_Type())
ethFwdReservedAddr0180C2000004.setMaxAccess(_C)
if mibBuilder.loadTexts:ethFwdReservedAddr0180C2000004.setStatus(_A)
class _EthFwdReservedAddr0180C2000005_Type(FrameProcess):defaultValue=1
_EthFwdReservedAddr0180C2000005_Type.__name__=_F
_EthFwdReservedAddr0180C2000005_Object=MibTableColumn
ethFwdReservedAddr0180C2000005=_EthFwdReservedAddr0180C2000005_Object((1,3,6,1,4,1,2928,2,2,1,2,2,1,18),_EthFwdReservedAddr0180C2000005_Type())
ethFwdReservedAddr0180C2000005.setMaxAccess(_C)
if mibBuilder.loadTexts:ethFwdReservedAddr0180C2000005.setStatus(_A)
class _EthFwdReservedAddr0180C2000006_Type(FrameProcess):defaultValue=1
_EthFwdReservedAddr0180C2000006_Type.__name__=_F
_EthFwdReservedAddr0180C2000006_Object=MibTableColumn
ethFwdReservedAddr0180C2000006=_EthFwdReservedAddr0180C2000006_Object((1,3,6,1,4,1,2928,2,2,1,2,2,1,19),_EthFwdReservedAddr0180C2000006_Type())
ethFwdReservedAddr0180C2000006.setMaxAccess(_C)
if mibBuilder.loadTexts:ethFwdReservedAddr0180C2000006.setStatus(_A)
class _EthFwdReservedAddr0180C2000007_Type(FrameProcess):defaultValue=1
_EthFwdReservedAddr0180C2000007_Type.__name__=_F
_EthFwdReservedAddr0180C2000007_Object=MibTableColumn
ethFwdReservedAddr0180C2000007=_EthFwdReservedAddr0180C2000007_Object((1,3,6,1,4,1,2928,2,2,1,2,2,1,20),_EthFwdReservedAddr0180C2000007_Type())
ethFwdReservedAddr0180C2000007.setMaxAccess(_C)
if mibBuilder.loadTexts:ethFwdReservedAddr0180C2000007.setStatus(_A)
class _EthFwdReservedAddr0180C2000008_Type(FrameProcess):defaultValue=1
_EthFwdReservedAddr0180C2000008_Type.__name__=_F
_EthFwdReservedAddr0180C2000008_Object=MibTableColumn
ethFwdReservedAddr0180C2000008=_EthFwdReservedAddr0180C2000008_Object((1,3,6,1,4,1,2928,2,2,1,2,2,1,21),_EthFwdReservedAddr0180C2000008_Type())
ethFwdReservedAddr0180C2000008.setMaxAccess(_C)
if mibBuilder.loadTexts:ethFwdReservedAddr0180C2000008.setStatus(_A)
class _EthFwdReservedAddr0180C2000009_Type(FrameProcess):defaultValue=1
_EthFwdReservedAddr0180C2000009_Type.__name__=_F
_EthFwdReservedAddr0180C2000009_Object=MibTableColumn
ethFwdReservedAddr0180C2000009=_EthFwdReservedAddr0180C2000009_Object((1,3,6,1,4,1,2928,2,2,1,2,2,1,22),_EthFwdReservedAddr0180C2000009_Type())
ethFwdReservedAddr0180C2000009.setMaxAccess(_C)
if mibBuilder.loadTexts:ethFwdReservedAddr0180C2000009.setStatus(_A)
class _EthFwdReservedAddr0180C200000A_Type(FrameProcess):defaultValue=1
_EthFwdReservedAddr0180C200000A_Type.__name__=_F
_EthFwdReservedAddr0180C200000A_Object=MibTableColumn
ethFwdReservedAddr0180C200000A=_EthFwdReservedAddr0180C200000A_Object((1,3,6,1,4,1,2928,2,2,1,2,2,1,23),_EthFwdReservedAddr0180C200000A_Type())
ethFwdReservedAddr0180C200000A.setMaxAccess(_C)
if mibBuilder.loadTexts:ethFwdReservedAddr0180C200000A.setStatus(_A)
class _EthFwdReservedAddr0180C200000B_Type(FrameProcess):defaultValue=1
_EthFwdReservedAddr0180C200000B_Type.__name__=_F
_EthFwdReservedAddr0180C200000B_Object=MibTableColumn
ethFwdReservedAddr0180C200000B=_EthFwdReservedAddr0180C200000B_Object((1,3,6,1,4,1,2928,2,2,1,2,2,1,24),_EthFwdReservedAddr0180C200000B_Type())
ethFwdReservedAddr0180C200000B.setMaxAccess(_C)
if mibBuilder.loadTexts:ethFwdReservedAddr0180C200000B.setStatus(_A)
class _EthFwdReservedAddr0180C200000C_Type(FrameProcess):defaultValue=1
_EthFwdReservedAddr0180C200000C_Type.__name__=_F
_EthFwdReservedAddr0180C200000C_Object=MibTableColumn
ethFwdReservedAddr0180C200000C=_EthFwdReservedAddr0180C200000C_Object((1,3,6,1,4,1,2928,2,2,1,2,2,1,25),_EthFwdReservedAddr0180C200000C_Type())
ethFwdReservedAddr0180C200000C.setMaxAccess(_C)
if mibBuilder.loadTexts:ethFwdReservedAddr0180C200000C.setStatus(_A)
class _EthFwdReservedAddr0180C200000D_Type(FrameProcess):defaultValue=1
_EthFwdReservedAddr0180C200000D_Type.__name__=_F
_EthFwdReservedAddr0180C200000D_Object=MibTableColumn
ethFwdReservedAddr0180C200000D=_EthFwdReservedAddr0180C200000D_Object((1,3,6,1,4,1,2928,2,2,1,2,2,1,26),_EthFwdReservedAddr0180C200000D_Type())
ethFwdReservedAddr0180C200000D.setMaxAccess(_C)
if mibBuilder.loadTexts:ethFwdReservedAddr0180C200000D.setStatus(_A)
class _EthFwdReservedAddr0180C200000E_Type(FrameProcess):defaultValue=1
_EthFwdReservedAddr0180C200000E_Type.__name__=_F
_EthFwdReservedAddr0180C200000E_Object=MibTableColumn
ethFwdReservedAddr0180C200000E=_EthFwdReservedAddr0180C200000E_Object((1,3,6,1,4,1,2928,2,2,1,2,2,1,27),_EthFwdReservedAddr0180C200000E_Type())
ethFwdReservedAddr0180C200000E.setMaxAccess(_C)
if mibBuilder.loadTexts:ethFwdReservedAddr0180C200000E.setStatus(_A)
class _EthFwdReservedAddr0180C200000F_Type(FrameProcess):defaultValue=1
_EthFwdReservedAddr0180C200000F_Type.__name__=_F
_EthFwdReservedAddr0180C200000F_Object=MibTableColumn
ethFwdReservedAddr0180C200000F=_EthFwdReservedAddr0180C200000F_Object((1,3,6,1,4,1,2928,2,2,1,2,2,1,28),_EthFwdReservedAddr0180C200000F_Type())
ethFwdReservedAddr0180C200000F.setMaxAccess(_C)
if mibBuilder.loadTexts:ethFwdReservedAddr0180C200000F.setStatus(_A)
class _EthFwdCurrentStpMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(2,3,4)));namedValues=NamedValues(*((_W,2),(_V,3),(_b,4)))
_EthFwdCurrentStpMode_Type.__name__=_D
_EthFwdCurrentStpMode_Object=MibTableColumn
ethFwdCurrentStpMode=_EthFwdCurrentStpMode_Object((1,3,6,1,4,1,2928,2,2,1,2,2,1,29),_EthFwdCurrentStpMode_Type())
ethFwdCurrentStpMode.setMaxAccess(_B)
if mibBuilder.loadTexts:ethFwdCurrentStpMode.setStatus(_A)
class _EthFwdMrpAddr0180C2000020_Type(FrameProcess):defaultValue=2
_EthFwdMrpAddr0180C2000020_Type.__name__=_F
_EthFwdMrpAddr0180C2000020_Object=MibTableColumn
ethFwdMrpAddr0180C2000020=_EthFwdMrpAddr0180C2000020_Object((1,3,6,1,4,1,2928,2,2,1,2,2,1,30),_EthFwdMrpAddr0180C2000020_Type())
ethFwdMrpAddr0180C2000020.setMaxAccess(_C)
if mibBuilder.loadTexts:ethFwdMrpAddr0180C2000020.setStatus(_A)
class _EthFwdMrpAddr0180C2000021_Type(FrameProcess):defaultValue=2
_EthFwdMrpAddr0180C2000021_Type.__name__=_F
_EthFwdMrpAddr0180C2000021_Object=MibTableColumn
ethFwdMrpAddr0180C2000021=_EthFwdMrpAddr0180C2000021_Object((1,3,6,1,4,1,2928,2,2,1,2,2,1,31),_EthFwdMrpAddr0180C2000021_Type())
ethFwdMrpAddr0180C2000021.setMaxAccess(_C)
if mibBuilder.loadTexts:ethFwdMrpAddr0180C2000021.setStatus(_A)
class _EthFwdMrpAddr0180C2000022_Type(FrameProcess):defaultValue=2
_EthFwdMrpAddr0180C2000022_Type.__name__=_F
_EthFwdMrpAddr0180C2000022_Object=MibTableColumn
ethFwdMrpAddr0180C2000022=_EthFwdMrpAddr0180C2000022_Object((1,3,6,1,4,1,2928,2,2,1,2,2,1,32),_EthFwdMrpAddr0180C2000022_Type())
ethFwdMrpAddr0180C2000022.setMaxAccess(_C)
if mibBuilder.loadTexts:ethFwdMrpAddr0180C2000022.setStatus(_A)
class _EthFwdMrpAddr0180C2000023_Type(FrameProcess):defaultValue=2
_EthFwdMrpAddr0180C2000023_Type.__name__=_F
_EthFwdMrpAddr0180C2000023_Object=MibTableColumn
ethFwdMrpAddr0180C2000023=_EthFwdMrpAddr0180C2000023_Object((1,3,6,1,4,1,2928,2,2,1,2,2,1,33),_EthFwdMrpAddr0180C2000023_Type())
ethFwdMrpAddr0180C2000023.setMaxAccess(_C)
if mibBuilder.loadTexts:ethFwdMrpAddr0180C2000023.setStatus(_A)
class _EthFwdMrpAddr0180C2000024_Type(FrameProcess):defaultValue=2
_EthFwdMrpAddr0180C2000024_Type.__name__=_F
_EthFwdMrpAddr0180C2000024_Object=MibTableColumn
ethFwdMrpAddr0180C2000024=_EthFwdMrpAddr0180C2000024_Object((1,3,6,1,4,1,2928,2,2,1,2,2,1,34),_EthFwdMrpAddr0180C2000024_Type())
ethFwdMrpAddr0180C2000024.setMaxAccess(_C)
if mibBuilder.loadTexts:ethFwdMrpAddr0180C2000024.setStatus(_A)
class _EthFwdMrpAddr0180C2000025_Type(FrameProcess):defaultValue=2
_EthFwdMrpAddr0180C2000025_Type.__name__=_F
_EthFwdMrpAddr0180C2000025_Object=MibTableColumn
ethFwdMrpAddr0180C2000025=_EthFwdMrpAddr0180C2000025_Object((1,3,6,1,4,1,2928,2,2,1,2,2,1,35),_EthFwdMrpAddr0180C2000025_Type())
ethFwdMrpAddr0180C2000025.setMaxAccess(_C)
if mibBuilder.loadTexts:ethFwdMrpAddr0180C2000025.setStatus(_A)
class _EthFwdMrpAddr0180C2000026_Type(FrameProcess):defaultValue=2
_EthFwdMrpAddr0180C2000026_Type.__name__=_F
_EthFwdMrpAddr0180C2000026_Object=MibTableColumn
ethFwdMrpAddr0180C2000026=_EthFwdMrpAddr0180C2000026_Object((1,3,6,1,4,1,2928,2,2,1,2,2,1,36),_EthFwdMrpAddr0180C2000026_Type())
ethFwdMrpAddr0180C2000026.setMaxAccess(_C)
if mibBuilder.loadTexts:ethFwdMrpAddr0180C2000026.setStatus(_A)
class _EthFwdMrpAddr0180C2000027_Type(FrameProcess):defaultValue=2
_EthFwdMrpAddr0180C2000027_Type.__name__=_F
_EthFwdMrpAddr0180C2000027_Object=MibTableColumn
ethFwdMrpAddr0180C2000027=_EthFwdMrpAddr0180C2000027_Object((1,3,6,1,4,1,2928,2,2,1,2,2,1,37),_EthFwdMrpAddr0180C2000027_Type())
ethFwdMrpAddr0180C2000027.setMaxAccess(_C)
if mibBuilder.loadTexts:ethFwdMrpAddr0180C2000027.setStatus(_A)
class _EthFwdMrpAddr0180C2000028_Type(FrameProcess):defaultValue=2
_EthFwdMrpAddr0180C2000028_Type.__name__=_F
_EthFwdMrpAddr0180C2000028_Object=MibTableColumn
ethFwdMrpAddr0180C2000028=_EthFwdMrpAddr0180C2000028_Object((1,3,6,1,4,1,2928,2,2,1,2,2,1,38),_EthFwdMrpAddr0180C2000028_Type())
ethFwdMrpAddr0180C2000028.setMaxAccess(_C)
if mibBuilder.loadTexts:ethFwdMrpAddr0180C2000028.setStatus(_A)
class _EthFwdMrpAddr0180C2000029_Type(FrameProcess):defaultValue=2
_EthFwdMrpAddr0180C2000029_Type.__name__=_F
_EthFwdMrpAddr0180C2000029_Object=MibTableColumn
ethFwdMrpAddr0180C2000029=_EthFwdMrpAddr0180C2000029_Object((1,3,6,1,4,1,2928,2,2,1,2,2,1,39),_EthFwdMrpAddr0180C2000029_Type())
ethFwdMrpAddr0180C2000029.setMaxAccess(_C)
if mibBuilder.loadTexts:ethFwdMrpAddr0180C2000029.setStatus(_A)
class _EthFwdMrpAddr0180C200002A_Type(FrameProcess):defaultValue=2
_EthFwdMrpAddr0180C200002A_Type.__name__=_F
_EthFwdMrpAddr0180C200002A_Object=MibTableColumn
ethFwdMrpAddr0180C200002A=_EthFwdMrpAddr0180C200002A_Object((1,3,6,1,4,1,2928,2,2,1,2,2,1,40),_EthFwdMrpAddr0180C200002A_Type())
ethFwdMrpAddr0180C200002A.setMaxAccess(_C)
if mibBuilder.loadTexts:ethFwdMrpAddr0180C200002A.setStatus(_A)
class _EthFwdMrpAddr0180C200002B_Type(FrameProcess):defaultValue=2
_EthFwdMrpAddr0180C200002B_Type.__name__=_F
_EthFwdMrpAddr0180C200002B_Object=MibTableColumn
ethFwdMrpAddr0180C200002B=_EthFwdMrpAddr0180C200002B_Object((1,3,6,1,4,1,2928,2,2,1,2,2,1,41),_EthFwdMrpAddr0180C200002B_Type())
ethFwdMrpAddr0180C200002B.setMaxAccess(_C)
if mibBuilder.loadTexts:ethFwdMrpAddr0180C200002B.setStatus(_A)
class _EthFwdMrpAddr0180C200002C_Type(FrameProcess):defaultValue=2
_EthFwdMrpAddr0180C200002C_Type.__name__=_F
_EthFwdMrpAddr0180C200002C_Object=MibTableColumn
ethFwdMrpAddr0180C200002C=_EthFwdMrpAddr0180C200002C_Object((1,3,6,1,4,1,2928,2,2,1,2,2,1,42),_EthFwdMrpAddr0180C200002C_Type())
ethFwdMrpAddr0180C200002C.setMaxAccess(_C)
if mibBuilder.loadTexts:ethFwdMrpAddr0180C200002C.setStatus(_A)
class _EthFwdMrpAddr0180C200002D_Type(FrameProcess):defaultValue=2
_EthFwdMrpAddr0180C200002D_Type.__name__=_F
_EthFwdMrpAddr0180C200002D_Object=MibTableColumn
ethFwdMrpAddr0180C200002D=_EthFwdMrpAddr0180C200002D_Object((1,3,6,1,4,1,2928,2,2,1,2,2,1,43),_EthFwdMrpAddr0180C200002D_Type())
ethFwdMrpAddr0180C200002D.setMaxAccess(_C)
if mibBuilder.loadTexts:ethFwdMrpAddr0180C200002D.setStatus(_A)
class _EthFwdMrpAddr0180C200002E_Type(FrameProcess):defaultValue=2
_EthFwdMrpAddr0180C200002E_Type.__name__=_F
_EthFwdMrpAddr0180C200002E_Object=MibTableColumn
ethFwdMrpAddr0180C200002E=_EthFwdMrpAddr0180C200002E_Object((1,3,6,1,4,1,2928,2,2,1,2,2,1,44),_EthFwdMrpAddr0180C200002E_Type())
ethFwdMrpAddr0180C200002E.setMaxAccess(_C)
if mibBuilder.loadTexts:ethFwdMrpAddr0180C200002E.setStatus(_A)
class _EthFwdMrpAddr0180C200002F_Type(FrameProcess):defaultValue=2
_EthFwdMrpAddr0180C200002F_Type.__name__=_F
_EthFwdMrpAddr0180C200002F_Object=MibTableColumn
ethFwdMrpAddr0180C200002F=_EthFwdMrpAddr0180C200002F_Object((1,3,6,1,4,1,2928,2,2,1,2,2,1,45),_EthFwdMrpAddr0180C200002F_Type())
ethFwdMrpAddr0180C200002F.setMaxAccess(_C)
if mibBuilder.loadTexts:ethFwdMrpAddr0180C200002F.setStatus(_A)
_EthFwdDiffservTable_Object=MibTable
ethFwdDiffservTable=_EthFwdDiffservTable_Object((1,3,6,1,4,1,2928,2,2,1,2,3))
if mibBuilder.loadTexts:ethFwdDiffservTable.setStatus(_A)
_EthFwdDiffservEntry_Object=MibTableRow
ethFwdDiffservEntry=_EthFwdDiffservEntry_Object((1,3,6,1,4,1,2928,2,2,1,2,3,1))
ethFwdDiffservEntry.setIndexNames((0,_E,_H),(0,_E,_X),(0,_E,_u))
if mibBuilder.loadTexts:ethFwdDiffservEntry.setStatus(_A)
class _EthFwdDiffservIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,63))
_EthFwdDiffservIndex_Type.__name__=_D
_EthFwdDiffservIndex_Object=MibTableColumn
ethFwdDiffservIndex=_EthFwdDiffservIndex_Object((1,3,6,1,4,1,2928,2,2,1,2,3,1,1),_EthFwdDiffservIndex_Type())
ethFwdDiffservIndex.setMaxAccess(_N)
if mibBuilder.loadTexts:ethFwdDiffservIndex.setStatus(_A)
class _EthFwdDiffservFlowGroup_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_EthFwdDiffservFlowGroup_Type.__name__=_D
_EthFwdDiffservFlowGroup_Object=MibTableColumn
ethFwdDiffservFlowGroup=_EthFwdDiffservFlowGroup_Object((1,3,6,1,4,1,2928,2,2,1,2,3,1,2),_EthFwdDiffservFlowGroup_Type())
ethFwdDiffservFlowGroup.setMaxAccess(_C)
if mibBuilder.loadTexts:ethFwdDiffservFlowGroup.setStatus(_A)
_EthFwdRstpTable_Object=MibTable
ethFwdRstpTable=_EthFwdRstpTable_Object((1,3,6,1,4,1,2928,2,2,1,2,4))
if mibBuilder.loadTexts:ethFwdRstpTable.setStatus(_A)
_EthFwdRstpEntry_Object=MibTableRow
ethFwdRstpEntry=_EthFwdRstpEntry_Object((1,3,6,1,4,1,2928,2,2,1,2,4,1))
ethFwdRstpEntry.setIndexNames((0,_E,_H),(0,_E,_X))
if mibBuilder.loadTexts:ethFwdRstpEntry.setStatus(_A)
_EthFwdRstpBridgeIdentifier_Type=BridgeIdentifier
_EthFwdRstpBridgeIdentifier_Object=MibTableColumn
ethFwdRstpBridgeIdentifier=_EthFwdRstpBridgeIdentifier_Object((1,3,6,1,4,1,2928,2,2,1,2,4,1,1),_EthFwdRstpBridgeIdentifier_Type())
ethFwdRstpBridgeIdentifier.setMaxAccess(_B)
if mibBuilder.loadTexts:ethFwdRstpBridgeIdentifier.setStatus(_A)
class _EthFwdRstpPriority_Type(Integer32):defaultValue=32768;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,61440))
_EthFwdRstpPriority_Type.__name__=_D
_EthFwdRstpPriority_Object=MibTableColumn
ethFwdRstpPriority=_EthFwdRstpPriority_Object((1,3,6,1,4,1,2928,2,2,1,2,4,1,2),_EthFwdRstpPriority_Type())
ethFwdRstpPriority.setMaxAccess(_C)
if mibBuilder.loadTexts:ethFwdRstpPriority.setStatus(_A)
_EthFwdRstpTimeSinceTopologyChange_Type=Timeout
_EthFwdRstpTimeSinceTopologyChange_Object=MibTableColumn
ethFwdRstpTimeSinceTopologyChange=_EthFwdRstpTimeSinceTopologyChange_Object((1,3,6,1,4,1,2928,2,2,1,2,4,1,3),_EthFwdRstpTimeSinceTopologyChange_Type())
ethFwdRstpTimeSinceTopologyChange.setMaxAccess(_B)
if mibBuilder.loadTexts:ethFwdRstpTimeSinceTopologyChange.setStatus(_A)
if mibBuilder.loadTexts:ethFwdRstpTimeSinceTopologyChange.setUnits(_Q)
_EthFwdRstpTopologyChangeCount_Type=Counter32
_EthFwdRstpTopologyChangeCount_Object=MibTableColumn
ethFwdRstpTopologyChangeCount=_EthFwdRstpTopologyChangeCount_Object((1,3,6,1,4,1,2928,2,2,1,2,4,1,4),_EthFwdRstpTopologyChangeCount_Type())
ethFwdRstpTopologyChangeCount.setMaxAccess(_B)
if mibBuilder.loadTexts:ethFwdRstpTopologyChangeCount.setStatus(_A)
_EthFwdRstpTopologyChange_Type=TruthValue
_EthFwdRstpTopologyChange_Object=MibTableColumn
ethFwdRstpTopologyChange=_EthFwdRstpTopologyChange_Object((1,3,6,1,4,1,2928,2,2,1,2,4,1,5),_EthFwdRstpTopologyChange_Type())
ethFwdRstpTopologyChange.setMaxAccess(_B)
if mibBuilder.loadTexts:ethFwdRstpTopologyChange.setStatus(_A)
_EthFwdRstpDesignatedRoot_Type=BridgeIdentifier
_EthFwdRstpDesignatedRoot_Object=MibTableColumn
ethFwdRstpDesignatedRoot=_EthFwdRstpDesignatedRoot_Object((1,3,6,1,4,1,2928,2,2,1,2,4,1,6),_EthFwdRstpDesignatedRoot_Type())
ethFwdRstpDesignatedRoot.setMaxAccess(_B)
if mibBuilder.loadTexts:ethFwdRstpDesignatedRoot.setStatus(_A)
_EthFwdRstpRootPathCost_Type=Integer32
_EthFwdRstpRootPathCost_Object=MibTableColumn
ethFwdRstpRootPathCost=_EthFwdRstpRootPathCost_Object((1,3,6,1,4,1,2928,2,2,1,2,4,1,7),_EthFwdRstpRootPathCost_Type())
ethFwdRstpRootPathCost.setMaxAccess(_B)
if mibBuilder.loadTexts:ethFwdRstpRootPathCost.setStatus(_A)
_EthFwdRstpRootPortName_Type=SnmpAdminString
_EthFwdRstpRootPortName_Object=MibTableColumn
ethFwdRstpRootPortName=_EthFwdRstpRootPortName_Object((1,3,6,1,4,1,2928,2,2,1,2,4,1,8),_EthFwdRstpRootPortName_Type())
ethFwdRstpRootPortName.setMaxAccess(_B)
if mibBuilder.loadTexts:ethFwdRstpRootPortName.setStatus(_A)
_EthFwdRstpMaxAge_Type=Timeout
_EthFwdRstpMaxAge_Object=MibTableColumn
ethFwdRstpMaxAge=_EthFwdRstpMaxAge_Object((1,3,6,1,4,1,2928,2,2,1,2,4,1,9),_EthFwdRstpMaxAge_Type())
ethFwdRstpMaxAge.setMaxAccess(_B)
if mibBuilder.loadTexts:ethFwdRstpMaxAge.setStatus(_A)
if mibBuilder.loadTexts:ethFwdRstpMaxAge.setUnits(_Q)
_EthFwdRstpHelloTime_Type=Timeout
_EthFwdRstpHelloTime_Object=MibTableColumn
ethFwdRstpHelloTime=_EthFwdRstpHelloTime_Object((1,3,6,1,4,1,2928,2,2,1,2,4,1,10),_EthFwdRstpHelloTime_Type())
ethFwdRstpHelloTime.setMaxAccess(_B)
if mibBuilder.loadTexts:ethFwdRstpHelloTime.setStatus(_A)
if mibBuilder.loadTexts:ethFwdRstpHelloTime.setUnits(_Q)
_EthFwdRstpForwardDelay_Type=Timeout
_EthFwdRstpForwardDelay_Object=MibTableColumn
ethFwdRstpForwardDelay=_EthFwdRstpForwardDelay_Object((1,3,6,1,4,1,2928,2,2,1,2,4,1,11),_EthFwdRstpForwardDelay_Type())
ethFwdRstpForwardDelay.setMaxAccess(_B)
if mibBuilder.loadTexts:ethFwdRstpForwardDelay.setStatus(_A)
if mibBuilder.loadTexts:ethFwdRstpForwardDelay.setUnits(_Q)
class _EthFwdRstpBridgeMaxAge_Type(Timeout):defaultValue=2000;subtypeSpec=Timeout.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(600,4000))
_EthFwdRstpBridgeMaxAge_Type.__name__=_Y
_EthFwdRstpBridgeMaxAge_Object=MibTableColumn
ethFwdRstpBridgeMaxAge=_EthFwdRstpBridgeMaxAge_Object((1,3,6,1,4,1,2928,2,2,1,2,4,1,12),_EthFwdRstpBridgeMaxAge_Type())
ethFwdRstpBridgeMaxAge.setMaxAccess(_C)
if mibBuilder.loadTexts:ethFwdRstpBridgeMaxAge.setStatus(_A)
if mibBuilder.loadTexts:ethFwdRstpBridgeMaxAge.setUnits(_Q)
class _EthFwdRstpBridgeHelloTime_Type(Timeout):defaultValue=200;subtypeSpec=Timeout.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(100,200))
_EthFwdRstpBridgeHelloTime_Type.__name__=_Y
_EthFwdRstpBridgeHelloTime_Object=MibTableColumn
ethFwdRstpBridgeHelloTime=_EthFwdRstpBridgeHelloTime_Object((1,3,6,1,4,1,2928,2,2,1,2,4,1,13),_EthFwdRstpBridgeHelloTime_Type())
ethFwdRstpBridgeHelloTime.setMaxAccess(_C)
if mibBuilder.loadTexts:ethFwdRstpBridgeHelloTime.setStatus(_A)
if mibBuilder.loadTexts:ethFwdRstpBridgeHelloTime.setUnits(_Q)
class _EthFwdRstpBridgeForwardDelay_Type(Timeout):defaultValue=1500;subtypeSpec=Timeout.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(400,3000))
_EthFwdRstpBridgeForwardDelay_Type.__name__=_Y
_EthFwdRstpBridgeForwardDelay_Object=MibTableColumn
ethFwdRstpBridgeForwardDelay=_EthFwdRstpBridgeForwardDelay_Object((1,3,6,1,4,1,2928,2,2,1,2,4,1,14),_EthFwdRstpBridgeForwardDelay_Type())
ethFwdRstpBridgeForwardDelay.setMaxAccess(_C)
if mibBuilder.loadTexts:ethFwdRstpBridgeForwardDelay.setStatus(_A)
class _EthFwdRstpTxHoldCount_Type(Integer32):defaultValue=6;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,10))
_EthFwdRstpTxHoldCount_Type.__name__=_D
_EthFwdRstpTxHoldCount_Object=MibTableColumn
ethFwdRstpTxHoldCount=_EthFwdRstpTxHoldCount_Object((1,3,6,1,4,1,2928,2,2,1,2,4,1,15),_EthFwdRstpTxHoldCount_Type())
ethFwdRstpTxHoldCount.setMaxAccess(_C)
if mibBuilder.loadTexts:ethFwdRstpTxHoldCount.setStatus(_A)
class _EthFwdRstpForceVersion_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('stp',1),('rstp',2)))
_EthFwdRstpForceVersion_Type.__name__=_D
_EthFwdRstpForceVersion_Object=MibTableColumn
ethFwdRstpForceVersion=_EthFwdRstpForceVersion_Object((1,3,6,1,4,1,2928,2,2,1,2,4,1,16),_EthFwdRstpForceVersion_Type())
ethFwdRstpForceVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:ethFwdRstpForceVersion.setStatus(_A)
_EthInterfaceGroup_ObjectIdentity=ObjectIdentity
ethInterfaceGroup=_EthInterfaceGroup_ObjectIdentity((1,3,6,1,4,1,2928,2,2,1,3))
_EthIfGroupLastChange_Type=TimeStamp
_EthIfGroupLastChange_Object=MibScalar
ethIfGroupLastChange=_EthIfGroupLastChange_Object((1,3,6,1,4,1,2928,2,2,1,3,1),_EthIfGroupLastChange_Type())
ethIfGroupLastChange.setMaxAccess(_B)
if mibBuilder.loadTexts:ethIfGroupLastChange.setStatus(_A)
_EthIfTable_Object=MibTable
ethIfTable=_EthIfTable_Object((1,3,6,1,4,1,2928,2,2,1,3,2))
if mibBuilder.loadTexts:ethIfTable.setStatus(_A)
_EthIfEntry_Object=MibTableRow
ethIfEntry=_EthIfEntry_Object((1,3,6,1,4,1,2928,2,2,1,3,2,1))
ethIfEntry.setIndexNames((0,_E,_H),(0,_E,_J))
if mibBuilder.loadTexts:ethIfEntry.setStatus(_A)
_EthIfIndex_Type=Unsigned32
_EthIfIndex_Object=MibTableColumn
ethIfIndex=_EthIfIndex_Object((1,3,6,1,4,1,2928,2,2,1,3,2,1,1),_EthIfIndex_Type())
ethIfIndex.setMaxAccess(_N)
if mibBuilder.loadTexts:ethIfIndex.setStatus(_A)
class _EthIfIfIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_EthIfIfIndex_Type.__name__=_D
_EthIfIfIndex_Object=MibTableColumn
ethIfIfIndex=_EthIfIfIndex_Object((1,3,6,1,4,1,2928,2,2,1,3,2,1,2),_EthIfIfIndex_Type())
ethIfIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:ethIfIfIndex.setStatus(_A)
_EthIfName_Type=SnmpAdminString
_EthIfName_Object=MibTableColumn
ethIfName=_EthIfName_Object((1,3,6,1,4,1,2928,2,2,1,3,2,1,3),_EthIfName_Type())
ethIfName.setMaxAccess(_B)
if mibBuilder.loadTexts:ethIfName.setStatus(_A)
_EthIfType_Type=EthInterfaceType
_EthIfType_Object=MibTableColumn
ethIfType=_EthIfType_Object((1,3,6,1,4,1,2928,2,2,1,3,2,1,4),_EthIfType_Type())
ethIfType.setMaxAccess(_B)
if mibBuilder.loadTexts:ethIfType.setStatus(_A)
class _EthIfCustomerId_Type(Unsigned32):defaultValue=0
_EthIfCustomerId_Type.__name__=_G
_EthIfCustomerId_Object=MibTableColumn
ethIfCustomerId=_EthIfCustomerId_Object((1,3,6,1,4,1,2928,2,2,1,3,2,1,5),_EthIfCustomerId_Type())
ethIfCustomerId.setMaxAccess(_C)
if mibBuilder.loadTexts:ethIfCustomerId.setStatus(_A)
class _EthIfPurpose_Type(SnmpAdminString):defaultHexValue=''
_EthIfPurpose_Type.__name__=_U
_EthIfPurpose_Object=MibTableColumn
ethIfPurpose=_EthIfPurpose_Object((1,3,6,1,4,1,2928,2,2,1,3,2,1,6),_EthIfPurpose_Type())
ethIfPurpose.setMaxAccess(_C)
if mibBuilder.loadTexts:ethIfPurpose.setStatus(_A)
class _EthIfAdminStatus_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('up',1),('down',2)))
_EthIfAdminStatus_Type.__name__=_D
_EthIfAdminStatus_Object=MibTableColumn
ethIfAdminStatus=_EthIfAdminStatus_Object((1,3,6,1,4,1,2928,2,2,1,3,2,1,7),_EthIfAdminStatus_Type())
ethIfAdminStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:ethIfAdminStatus.setStatus(_A)
class _EthIfOperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,5,6,9)));namedValues=NamedValues(*(('up',1),('down',2),('dormant',5),('notPresent',6),('partial',9)))
_EthIfOperStatus_Type.__name__=_D
_EthIfOperStatus_Object=MibTableColumn
ethIfOperStatus=_EthIfOperStatus_Object((1,3,6,1,4,1,2928,2,2,1,3,2,1,8),_EthIfOperStatus_Type())
ethIfOperStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:ethIfOperStatus.setStatus(_A)
_EthIfFailure_Type=SnmpAdminString
_EthIfFailure_Object=MibTableColumn
ethIfFailure=_EthIfFailure_Object((1,3,6,1,4,1,2928,2,2,1,3,2,1,9),_EthIfFailure_Type())
ethIfFailure.setMaxAccess(_B)
if mibBuilder.loadTexts:ethIfFailure.setStatus(_A)
class _EthIfForwardingFunction_Type(Integer32):defaultValue=-1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,2147483647))
_EthIfForwardingFunction_Type.__name__=_D
_EthIfForwardingFunction_Object=MibTableColumn
ethIfForwardingFunction=_EthIfForwardingFunction_Object((1,3,6,1,4,1,2928,2,2,1,3,2,1,10),_EthIfForwardingFunction_Type())
ethIfForwardingFunction.setMaxAccess(_C)
if mibBuilder.loadTexts:ethIfForwardingFunction.setStatus(_A)
class _EthIfAcceptableFrameTypes_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_c,1),(_R,2),(_S,3)))
_EthIfAcceptableFrameTypes_Type.__name__=_D
_EthIfAcceptableFrameTypes_Object=MibTableColumn
ethIfAcceptableFrameTypes=_EthIfAcceptableFrameTypes_Object((1,3,6,1,4,1,2928,2,2,1,3,2,1,11),_EthIfAcceptableFrameTypes_Type())
ethIfAcceptableFrameTypes.setMaxAccess(_C)
if mibBuilder.loadTexts:ethIfAcceptableFrameTypes.setStatus(_A)
class _EthIfTransmittedFrameType_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(2,3,4)));namedValues=NamedValues(*((_R,2),(_S,3),(_s,4)))
_EthIfTransmittedFrameType_Type.__name__=_D
_EthIfTransmittedFrameType_Object=MibTableColumn
ethIfTransmittedFrameType=_EthIfTransmittedFrameType_Object((1,3,6,1,4,1,2928,2,2,1,3,2,1,12),_EthIfTransmittedFrameType_Type())
ethIfTransmittedFrameType.setMaxAccess(_C)
if mibBuilder.loadTexts:ethIfTransmittedFrameType.setStatus(_A)
class _EthIfDefaultVLAN_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094))
_EthIfDefaultVLAN_Type.__name__=_D
_EthIfDefaultVLAN_Object=MibTableColumn
ethIfDefaultVLAN=_EthIfDefaultVLAN_Object((1,3,6,1,4,1,2928,2,2,1,3,2,1,13),_EthIfDefaultVLAN_Type())
ethIfDefaultVLAN.setMaxAccess(_C)
if mibBuilder.loadTexts:ethIfDefaultVLAN.setStatus(_A)
class _EthIfDefaultEthernetPriority_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_EthIfDefaultEthernetPriority_Type.__name__=_D
_EthIfDefaultEthernetPriority_Object=MibTableColumn
ethIfDefaultEthernetPriority=_EthIfDefaultEthernetPriority_Object((1,3,6,1,4,1,2928,2,2,1,3,2,1,14),_EthIfDefaultEthernetPriority_Type())
ethIfDefaultEthernetPriority.setMaxAccess(_C)
if mibBuilder.loadTexts:ethIfDefaultEthernetPriority.setStatus(_A)
class _EthIfPriorityMode_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('ethernet',1),('diffserv',2)))
_EthIfPriorityMode_Type.__name__=_D
_EthIfPriorityMode_Object=MibTableColumn
ethIfPriorityMode=_EthIfPriorityMode_Object((1,3,6,1,4,1,2928,2,2,1,3,2,1,15),_EthIfPriorityMode_Type())
ethIfPriorityMode.setMaxAccess(_C)
if mibBuilder.loadTexts:ethIfPriorityMode.setStatus(_A)
class _EthIfDefaultTrafficClass_Type(TrafficClass):defaultValue=0
_EthIfDefaultTrafficClass_Type.__name__=_v
_EthIfDefaultTrafficClass_Object=MibTableColumn
ethIfDefaultTrafficClass=_EthIfDefaultTrafficClass_Object((1,3,6,1,4,1,2928,2,2,1,3,2,1,16),_EthIfDefaultTrafficClass_Type())
ethIfDefaultTrafficClass.setMaxAccess(_C)
if mibBuilder.loadTexts:ethIfDefaultTrafficClass.setStatus(_A)
class _EthIfFlowGroupMap_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(8,8));fixedLength=8
_EthIfFlowGroupMap_Type.__name__=_T
_EthIfFlowGroupMap_Object=MibTableColumn
ethIfFlowGroupMap=_EthIfFlowGroupMap_Object((1,3,6,1,4,1,2928,2,2,1,3,2,1,17),_EthIfFlowGroupMap_Type())
ethIfFlowGroupMap.setMaxAccess(_C)
if mibBuilder.loadTexts:ethIfFlowGroupMap.setStatus(_A)
class _EthIfLearning_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_O,1),(_P,2)))
_EthIfLearning_Type.__name__=_D
_EthIfLearning_Object=MibTableColumn
ethIfLearning=_EthIfLearning_Object((1,3,6,1,4,1,2928,2,2,1,3,2,1,18),_EthIfLearning_Type())
ethIfLearning.setMaxAccess(_C)
if mibBuilder.loadTexts:ethIfLearning.setStatus(_A)
_EthIfInSpeed_Type=Gauge32
_EthIfInSpeed_Object=MibTableColumn
ethIfInSpeed=_EthIfInSpeed_Object((1,3,6,1,4,1,2928,2,2,1,3,2,1,19),_EthIfInSpeed_Type())
ethIfInSpeed.setMaxAccess(_B)
if mibBuilder.loadTexts:ethIfInSpeed.setStatus(_A)
_EthIfInHighSpeed_Type=Gauge32
_EthIfInHighSpeed_Object=MibTableColumn
ethIfInHighSpeed=_EthIfInHighSpeed_Object((1,3,6,1,4,1,2928,2,2,1,3,2,1,20),_EthIfInHighSpeed_Type())
ethIfInHighSpeed.setMaxAccess(_B)
if mibBuilder.loadTexts:ethIfInHighSpeed.setStatus(_A)
_EthIfOutSpeed_Type=Gauge32
_EthIfOutSpeed_Object=MibTableColumn
ethIfOutSpeed=_EthIfOutSpeed_Object((1,3,6,1,4,1,2928,2,2,1,3,2,1,21),_EthIfOutSpeed_Type())
ethIfOutSpeed.setMaxAccess(_B)
if mibBuilder.loadTexts:ethIfOutSpeed.setStatus(_A)
_EthIfOutHighSpeed_Type=Gauge32
_EthIfOutHighSpeed_Object=MibTableColumn
ethIfOutHighSpeed=_EthIfOutHighSpeed_Object((1,3,6,1,4,1,2928,2,2,1,3,2,1,22),_EthIfOutHighSpeed_Type())
ethIfOutHighSpeed.setMaxAccess(_B)
if mibBuilder.loadTexts:ethIfOutHighSpeed.setStatus(_A)
_EthIfVLANNextIndex_Type=Unsigned32
_EthIfVLANNextIndex_Object=MibTableColumn
ethIfVLANNextIndex=_EthIfVLANNextIndex_Object((1,3,6,1,4,1,2928,2,2,1,3,2,1,23),_EthIfVLANNextIndex_Type())
ethIfVLANNextIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:ethIfVLANNextIndex.setStatus(_A)
_EthIfLastChange_Type=TimeTicks
_EthIfLastChange_Object=MibTableColumn
ethIfLastChange=_EthIfLastChange_Object((1,3,6,1,4,1,2928,2,2,1,3,2,1,24),_EthIfLastChange_Type())
ethIfLastChange.setMaxAccess(_B)
if mibBuilder.loadTexts:ethIfLastChange.setStatus(_A)
_EthIfSrcPmReference_Type=RowPointer
_EthIfSrcPmReference_Object=MibTableColumn
ethIfSrcPmReference=_EthIfSrcPmReference_Object((1,3,6,1,4,1,2928,2,2,1,3,2,1,25),_EthIfSrcPmReference_Type())
ethIfSrcPmReference.setMaxAccess(_B)
if mibBuilder.loadTexts:ethIfSrcPmReference.setStatus(_A)
_EthIfSnkPmReference_Type=RowPointer
_EthIfSnkPmReference_Object=MibTableColumn
ethIfSnkPmReference=_EthIfSnkPmReference_Object((1,3,6,1,4,1,2928,2,2,1,3,2,1,26),_EthIfSnkPmReference_Type())
ethIfSnkPmReference.setMaxAccess(_B)
if mibBuilder.loadTexts:ethIfSnkPmReference.setStatus(_A)
class _EthIfSrcDegThreshold_Type(Unsigned32):defaultValue=100
_EthIfSrcDegThreshold_Type.__name__=_G
_EthIfSrcDegThreshold_Object=MibTableColumn
ethIfSrcDegThreshold=_EthIfSrcDegThreshold_Object((1,3,6,1,4,1,2928,2,2,1,3,2,1,27),_EthIfSrcDegThreshold_Type())
ethIfSrcDegThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:ethIfSrcDegThreshold.setStatus(_A)
class _EthIfSnkDegThreshold_Type(Unsigned32):defaultValue=100
_EthIfSnkDegThreshold_Type.__name__=_G
_EthIfSnkDegThreshold_Object=MibTableColumn
ethIfSnkDegThreshold=_EthIfSnkDegThreshold_Object((1,3,6,1,4,1,2928,2,2,1,3,2,1,28),_EthIfSnkDegThreshold_Type())
ethIfSnkDegThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:ethIfSnkDegThreshold.setStatus(_A)
class _EthIfSrcDegPeriod_Type(Unsigned32):defaultValue=7;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(2,10))
_EthIfSrcDegPeriod_Type.__name__=_G
_EthIfSrcDegPeriod_Object=MibTableColumn
ethIfSrcDegPeriod=_EthIfSrcDegPeriod_Object((1,3,6,1,4,1,2928,2,2,1,3,2,1,29),_EthIfSrcDegPeriod_Type())
ethIfSrcDegPeriod.setMaxAccess(_C)
if mibBuilder.loadTexts:ethIfSrcDegPeriod.setStatus(_A)
class _EthIfSnkDegPeriod_Type(Unsigned32):defaultValue=7;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(2,10))
_EthIfSnkDegPeriod_Type.__name__=_G
_EthIfSnkDegPeriod_Object=MibTableColumn
ethIfSnkDegPeriod=_EthIfSnkDegPeriod_Object((1,3,6,1,4,1,2928,2,2,1,3,2,1,30),_EthIfSnkDegPeriod_Type())
ethIfSnkDegPeriod.setMaxAccess(_C)
if mibBuilder.loadTexts:ethIfSnkDegPeriod.setStatus(_A)
class _EthIfSrcReducedBitRateThreshold_Type(Unsigned32):defaultValue=0
_EthIfSrcReducedBitRateThreshold_Type.__name__=_G
_EthIfSrcReducedBitRateThreshold_Object=MibTableColumn
ethIfSrcReducedBitRateThreshold=_EthIfSrcReducedBitRateThreshold_Object((1,3,6,1,4,1,2928,2,2,1,3,2,1,31),_EthIfSrcReducedBitRateThreshold_Type())
ethIfSrcReducedBitRateThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:ethIfSrcReducedBitRateThreshold.setStatus(_A)
class _EthIfSnkReducedBitRateThreshold_Type(Unsigned32):defaultValue=0
_EthIfSnkReducedBitRateThreshold_Type.__name__=_G
_EthIfSnkReducedBitRateThreshold_Object=MibTableColumn
ethIfSnkReducedBitRateThreshold=_EthIfSnkReducedBitRateThreshold_Object((1,3,6,1,4,1,2928,2,2,1,3,2,1,32),_EthIfSnkReducedBitRateThreshold_Type())
ethIfSnkReducedBitRateThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:ethIfSnkReducedBitRateThreshold.setStatus(_A)
class _EthIfSrcReducedBitRateHighThreshold_Type(Unsigned32):defaultValue=0
_EthIfSrcReducedBitRateHighThreshold_Type.__name__=_G
_EthIfSrcReducedBitRateHighThreshold_Object=MibTableColumn
ethIfSrcReducedBitRateHighThreshold=_EthIfSrcReducedBitRateHighThreshold_Object((1,3,6,1,4,1,2928,2,2,1,3,2,1,33),_EthIfSrcReducedBitRateHighThreshold_Type())
ethIfSrcReducedBitRateHighThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:ethIfSrcReducedBitRateHighThreshold.setStatus(_A)
class _EthIfSnkReducedBitRateHighThreshold_Type(Unsigned32):defaultValue=0
_EthIfSnkReducedBitRateHighThreshold_Type.__name__=_G
_EthIfSnkReducedBitRateHighThreshold_Object=MibTableColumn
ethIfSnkReducedBitRateHighThreshold=_EthIfSnkReducedBitRateHighThreshold_Object((1,3,6,1,4,1,2928,2,2,1,3,2,1,34),_EthIfSnkReducedBitRateHighThreshold_Type())
ethIfSnkReducedBitRateHighThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:ethIfSnkReducedBitRateHighThreshold.setStatus(_A)
class _EthIfSrcReducedBitRateAIS_Type(TruthValue):defaultValue=2
_EthIfSrcReducedBitRateAIS_Type.__name__=_M
_EthIfSrcReducedBitRateAIS_Object=MibTableColumn
ethIfSrcReducedBitRateAIS=_EthIfSrcReducedBitRateAIS_Object((1,3,6,1,4,1,2928,2,2,1,3,2,1,35),_EthIfSrcReducedBitRateAIS_Type())
ethIfSrcReducedBitRateAIS.setMaxAccess(_C)
if mibBuilder.loadTexts:ethIfSrcReducedBitRateAIS.setStatus(_A)
class _EthIfSnkReducedBitRateAIS_Type(TruthValue):defaultValue=2
_EthIfSnkReducedBitRateAIS_Type.__name__=_M
_EthIfSnkReducedBitRateAIS_Object=MibTableColumn
ethIfSnkReducedBitRateAIS=_EthIfSnkReducedBitRateAIS_Object((1,3,6,1,4,1,2928,2,2,1,3,2,1,36),_EthIfSnkReducedBitRateAIS_Type())
ethIfSnkReducedBitRateAIS.setMaxAccess(_C)
if mibBuilder.loadTexts:ethIfSnkReducedBitRateAIS.setStatus(_A)
class _EthIfSnkDegAIS_Type(TruthValue):defaultValue=2
_EthIfSnkDegAIS_Type.__name__=_M
_EthIfSnkDegAIS_Object=MibTableColumn
ethIfSnkDegAIS=_EthIfSnkDegAIS_Object((1,3,6,1,4,1,2928,2,2,1,3,2,1,37),_EthIfSnkDegAIS_Type())
ethIfSnkDegAIS.setMaxAccess(_C)
if mibBuilder.loadTexts:ethIfSnkDegAIS.setStatus(_A)
class _EthIfSrcMinorReducedBitRateThreshold_Type(Unsigned32):defaultValue=0
_EthIfSrcMinorReducedBitRateThreshold_Type.__name__=_G
_EthIfSrcMinorReducedBitRateThreshold_Object=MibTableColumn
ethIfSrcMinorReducedBitRateThreshold=_EthIfSrcMinorReducedBitRateThreshold_Object((1,3,6,1,4,1,2928,2,2,1,3,2,1,38),_EthIfSrcMinorReducedBitRateThreshold_Type())
ethIfSrcMinorReducedBitRateThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:ethIfSrcMinorReducedBitRateThreshold.setStatus(_A)
class _EthIfSnkMinorReducedBitRateThreshold_Type(Unsigned32):defaultValue=0
_EthIfSnkMinorReducedBitRateThreshold_Type.__name__=_G
_EthIfSnkMinorReducedBitRateThreshold_Object=MibTableColumn
ethIfSnkMinorReducedBitRateThreshold=_EthIfSnkMinorReducedBitRateThreshold_Object((1,3,6,1,4,1,2928,2,2,1,3,2,1,39),_EthIfSnkMinorReducedBitRateThreshold_Type())
ethIfSnkMinorReducedBitRateThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:ethIfSnkMinorReducedBitRateThreshold.setStatus(_A)
class _EthIfSrcMinorReducedBitRateHighThreshold_Type(Unsigned32):defaultValue=0
_EthIfSrcMinorReducedBitRateHighThreshold_Type.__name__=_G
_EthIfSrcMinorReducedBitRateHighThreshold_Object=MibTableColumn
ethIfSrcMinorReducedBitRateHighThreshold=_EthIfSrcMinorReducedBitRateHighThreshold_Object((1,3,6,1,4,1,2928,2,2,1,3,2,1,40),_EthIfSrcMinorReducedBitRateHighThreshold_Type())
ethIfSrcMinorReducedBitRateHighThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:ethIfSrcMinorReducedBitRateHighThreshold.setStatus(_A)
class _EthIfSnkMinorReducedBitRateHighThreshold_Type(Unsigned32):defaultValue=0
_EthIfSnkMinorReducedBitRateHighThreshold_Type.__name__=_G
_EthIfSnkMinorReducedBitRateHighThreshold_Object=MibTableColumn
ethIfSnkMinorReducedBitRateHighThreshold=_EthIfSnkMinorReducedBitRateHighThreshold_Object((1,3,6,1,4,1,2928,2,2,1,3,2,1,41),_EthIfSnkMinorReducedBitRateHighThreshold_Type())
ethIfSnkMinorReducedBitRateHighThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:ethIfSnkMinorReducedBitRateHighThreshold.setStatus(_A)
_EthIfSrcFailure_Type=SnmpAdminString
_EthIfSrcFailure_Object=MibTableColumn
ethIfSrcFailure=_EthIfSrcFailure_Object((1,3,6,1,4,1,2928,2,2,1,3,2,1,42),_EthIfSrcFailure_Type())
ethIfSrcFailure.setMaxAccess(_B)
if mibBuilder.loadTexts:ethIfSrcFailure.setStatus(_A)
_EthIfSnkFailure_Type=SnmpAdminString
_EthIfSnkFailure_Object=MibTableColumn
ethIfSnkFailure=_EthIfSnkFailure_Object((1,3,6,1,4,1,2928,2,2,1,3,2,1,43),_EthIfSnkFailure_Type())
ethIfSnkFailure.setMaxAccess(_B)
if mibBuilder.loadTexts:ethIfSnkFailure.setStatus(_A)
_EthIfInterfaceGroup_Type=Integer32
_EthIfInterfaceGroup_Object=MibTableColumn
ethIfInterfaceGroup=_EthIfInterfaceGroup_Object((1,3,6,1,4,1,2928,2,2,1,3,2,1,44),_EthIfInterfaceGroup_Type())
ethIfInterfaceGroup.setMaxAccess(_C)
if mibBuilder.loadTexts:ethIfInterfaceGroup.setStatus(_A)
_EthIfMaxMaxQueueFrames_Type=Unsigned32
_EthIfMaxMaxQueueFrames_Object=MibTableColumn
ethIfMaxMaxQueueFrames=_EthIfMaxMaxQueueFrames_Object((1,3,6,1,4,1,2928,2,2,1,3,2,1,45),_EthIfMaxMaxQueueFrames_Type())
ethIfMaxMaxQueueFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:ethIfMaxMaxQueueFrames.setStatus(_A)
class _EthIfDefaultDropPrecedence_Type(Unsigned32):defaultValue=0
_EthIfDefaultDropPrecedence_Type.__name__=_G
_EthIfDefaultDropPrecedence_Object=MibTableColumn
ethIfDefaultDropPrecedence=_EthIfDefaultDropPrecedence_Object((1,3,6,1,4,1,2928,2,2,1,3,2,1,46),_EthIfDefaultDropPrecedence_Type())
ethIfDefaultDropPrecedence.setMaxAccess(_C)
if mibBuilder.loadTexts:ethIfDefaultDropPrecedence.setStatus(_A)
class _EthIfDropPrecedenceMap_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(8,8));fixedLength=8
_EthIfDropPrecedenceMap_Type.__name__=_T
_EthIfDropPrecedenceMap_Object=MibTableColumn
ethIfDropPrecedenceMap=_EthIfDropPrecedenceMap_Object((1,3,6,1,4,1,2928,2,2,1,3,2,1,47),_EthIfDropPrecedenceMap_Type())
ethIfDropPrecedenceMap.setMaxAccess(_C)
if mibBuilder.loadTexts:ethIfDropPrecedenceMap.setStatus(_A)
_EthIfQueueTable_Object=MibTable
ethIfQueueTable=_EthIfQueueTable_Object((1,3,6,1,4,1,2928,2,2,1,3,3))
if mibBuilder.loadTexts:ethIfQueueTable.setStatus(_A)
_EthIfQueueEntry_Object=MibTableRow
ethIfQueueEntry=_EthIfQueueEntry_Object((1,3,6,1,4,1,2928,2,2,1,3,3,1))
ethIfQueueEntry.setIndexNames((0,_E,_H),(0,_E,_J),(0,_E,_d))
if mibBuilder.loadTexts:ethIfQueueEntry.setStatus(_A)
_EthIfQueueTrafficClass_Type=TrafficClass
_EthIfQueueTrafficClass_Object=MibTableColumn
ethIfQueueTrafficClass=_EthIfQueueTrafficClass_Object((1,3,6,1,4,1,2928,2,2,1,3,3,1,1),_EthIfQueueTrafficClass_Type())
ethIfQueueTrafficClass.setMaxAccess(_N)
if mibBuilder.loadTexts:ethIfQueueTrafficClass.setStatus(_A)
class _EthIfQueueMaxOctets_Type(Integer32):defaultValue=-1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,2147483647))
_EthIfQueueMaxOctets_Type.__name__=_D
_EthIfQueueMaxOctets_Object=MibTableColumn
ethIfQueueMaxOctets=_EthIfQueueMaxOctets_Object((1,3,6,1,4,1,2928,2,2,1,3,3,1,2),_EthIfQueueMaxOctets_Type())
ethIfQueueMaxOctets.setMaxAccess(_C)
if mibBuilder.loadTexts:ethIfQueueMaxOctets.setStatus(_A)
class _EthIfQueueMaxFrames_Type(Integer32):defaultValue=-1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,2147483647))
_EthIfQueueMaxFrames_Type.__name__=_D
_EthIfQueueMaxFrames_Object=MibTableColumn
ethIfQueueMaxFrames=_EthIfQueueMaxFrames_Object((1,3,6,1,4,1,2928,2,2,1,3,3,1,3),_EthIfQueueMaxFrames_Type())
ethIfQueueMaxFrames.setMaxAccess(_C)
if mibBuilder.loadTexts:ethIfQueueMaxFrames.setStatus(_A)
_EthIfVLANSetsTable_Object=MibTable
ethIfVLANSetsTable=_EthIfVLANSetsTable_Object((1,3,6,1,4,1,2928,2,2,1,3,4))
if mibBuilder.loadTexts:ethIfVLANSetsTable.setStatus(_A)
_EthIfVLANSetsEntry_Object=MibTableRow
ethIfVLANSetsEntry=_EthIfVLANSetsEntry_Object((1,3,6,1,4,1,2928,2,2,1,3,4,1))
ethIfVLANSetsEntry.setIndexNames((0,_E,_H),(0,_E,_J),(0,_E,_w))
if mibBuilder.loadTexts:ethIfVLANSetsEntry.setStatus(_A)
_EthIfVLANSetIndex_Type=Unsigned32
_EthIfVLANSetIndex_Object=MibTableColumn
ethIfVLANSetIndex=_EthIfVLANSetIndex_Object((1,3,6,1,4,1,2928,2,2,1,3,4,1,1),_EthIfVLANSetIndex_Type())
ethIfVLANSetIndex.setMaxAccess(_N)
if mibBuilder.loadTexts:ethIfVLANSetIndex.setStatus(_A)
_EthIfVLANRowStatus_Type=RowStatus
_EthIfVLANRowStatus_Object=MibTableColumn
ethIfVLANRowStatus=_EthIfVLANRowStatus_Object((1,3,6,1,4,1,2928,2,2,1,3,4,1,2),_EthIfVLANRowStatus_Type())
ethIfVLANRowStatus.setMaxAccess(_I)
if mibBuilder.loadTexts:ethIfVLANRowStatus.setStatus(_A)
_EthIfVLANSet_Type=VLANSet
_EthIfVLANSet_Object=MibTableColumn
ethIfVLANSet=_EthIfVLANSet_Object((1,3,6,1,4,1,2928,2,2,1,3,4,1,3),_EthIfVLANSet_Type())
ethIfVLANSet.setMaxAccess(_I)
if mibBuilder.loadTexts:ethIfVLANSet.setStatus(_A)
class _EthIfVLANCustomerId_Type(Unsigned32):defaultValue=0
_EthIfVLANCustomerId_Type.__name__=_G
_EthIfVLANCustomerId_Object=MibTableColumn
ethIfVLANCustomerId=_EthIfVLANCustomerId_Object((1,3,6,1,4,1,2928,2,2,1,3,4,1,4),_EthIfVLANCustomerId_Type())
ethIfVLANCustomerId.setMaxAccess(_I)
if mibBuilder.loadTexts:ethIfVLANCustomerId.setStatus(_A)
class _EthIfVLANPurpose_Type(SnmpAdminString):defaultHexValue=''
_EthIfVLANPurpose_Type.__name__=_U
_EthIfVLANPurpose_Object=MibTableColumn
ethIfVLANPurpose=_EthIfVLANPurpose_Object((1,3,6,1,4,1,2928,2,2,1,3,4,1,5),_EthIfVLANPurpose_Type())
ethIfVLANPurpose.setMaxAccess(_I)
if mibBuilder.loadTexts:ethIfVLANPurpose.setStatus(_A)
_EthDot3Table_Object=MibTable
ethDot3Table=_EthDot3Table_Object((1,3,6,1,4,1,2928,2,2,1,3,5))
if mibBuilder.loadTexts:ethDot3Table.setStatus(_A)
_EthDot3Entry_Object=MibTableRow
ethDot3Entry=_EthDot3Entry_Object((1,3,6,1,4,1,2928,2,2,1,3,5,1))
ethDot3Entry.setIndexNames((0,_E,_H),(0,_E,_J))
if mibBuilder.loadTexts:ethDot3Entry.setStatus(_A)
class _EthDot3AutoNegotiate_Type(TruthValue):defaultValue=1
_EthDot3AutoNegotiate_Type.__name__=_M
_EthDot3AutoNegotiate_Object=MibTableColumn
ethDot3AutoNegotiate=_EthDot3AutoNegotiate_Object((1,3,6,1,4,1,2928,2,2,1,3,5,1,1),_EthDot3AutoNegotiate_Type())
ethDot3AutoNegotiate.setMaxAccess(_C)
if mibBuilder.loadTexts:ethDot3AutoNegotiate.setStatus(_A)
class _EthDot3AdvertisedSpeed_Type(AdvertisedSpeed):defaultBinValue='1'
_EthDot3AdvertisedSpeed_Type.__name__=_x
_EthDot3AdvertisedSpeed_Object=MibTableColumn
ethDot3AdvertisedSpeed=_EthDot3AdvertisedSpeed_Object((1,3,6,1,4,1,2928,2,2,1,3,5,1,2),_EthDot3AdvertisedSpeed_Type())
ethDot3AdvertisedSpeed.setMaxAccess(_C)
if mibBuilder.loadTexts:ethDot3AdvertisedSpeed.setStatus(_A)
class _EthDot3AdvertisedDuplex_Type(AdvertisedDuplex):defaultBinValue='1'
_EthDot3AdvertisedDuplex_Type.__name__=_y
_EthDot3AdvertisedDuplex_Object=MibTableColumn
ethDot3AdvertisedDuplex=_EthDot3AdvertisedDuplex_Object((1,3,6,1,4,1,2928,2,2,1,3,5,1,3),_EthDot3AdvertisedDuplex_Type())
ethDot3AdvertisedDuplex.setMaxAccess(_C)
if mibBuilder.loadTexts:ethDot3AdvertisedDuplex.setStatus(_A)
class _EthDot3AdvertisedFlowControl_Type(AdvertisedFlowControl):defaultBinValue='1'
_EthDot3AdvertisedFlowControl_Type.__name__=_z
_EthDot3AdvertisedFlowControl_Object=MibTableColumn
ethDot3AdvertisedFlowControl=_EthDot3AdvertisedFlowControl_Object((1,3,6,1,4,1,2928,2,2,1,3,5,1,4),_EthDot3AdvertisedFlowControl_Type())
ethDot3AdvertisedFlowControl.setMaxAccess(_C)
if mibBuilder.loadTexts:ethDot3AdvertisedFlowControl.setStatus(_A)
class _EthDot3ActiveSpeed_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(10,10),ValueRangeConstraint(100,100),ValueRangeConstraint(1000,1000),ValueRangeConstraint(10000,10000))
_EthDot3ActiveSpeed_Type.__name__=_G
_EthDot3ActiveSpeed_Object=MibTableColumn
ethDot3ActiveSpeed=_EthDot3ActiveSpeed_Object((1,3,6,1,4,1,2928,2,2,1,3,5,1,5),_EthDot3ActiveSpeed_Type())
ethDot3ActiveSpeed.setMaxAccess(_B)
if mibBuilder.loadTexts:ethDot3ActiveSpeed.setStatus(_A)
class _EthDot3ActiveDuplex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_e,1),(_f,2),(_A0,3)))
_EthDot3ActiveDuplex_Type.__name__=_D
_EthDot3ActiveDuplex_Object=MibTableColumn
ethDot3ActiveDuplex=_EthDot3ActiveDuplex_Object((1,3,6,1,4,1,2928,2,2,1,3,5,1,6),_EthDot3ActiveDuplex_Type())
ethDot3ActiveDuplex.setMaxAccess(_B)
if mibBuilder.loadTexts:ethDot3ActiveDuplex.setStatus(_A)
class _EthDot3ActiveFlowControl_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_c,1),('receive',2),('transmit',3),('none',4),(_A0,5)))
_EthDot3ActiveFlowControl_Type.__name__=_D
_EthDot3ActiveFlowControl_Object=MibTableColumn
ethDot3ActiveFlowControl=_EthDot3ActiveFlowControl_Object((1,3,6,1,4,1,2928,2,2,1,3,5,1,7),_EthDot3ActiveFlowControl_Type())
ethDot3ActiveFlowControl.setMaxAccess(_B)
if mibBuilder.loadTexts:ethDot3ActiveFlowControl.setStatus(_A)
_EthDot3ForceVLANTagged_Type=VLANSet
_EthDot3ForceVLANTagged_Object=MibTableColumn
ethDot3ForceVLANTagged=_EthDot3ForceVLANTagged_Object((1,3,6,1,4,1,2928,2,2,1,3,5,1,8),_EthDot3ForceVLANTagged_Type())
ethDot3ForceVLANTagged.setMaxAccess(_C)
if mibBuilder.loadTexts:ethDot3ForceVLANTagged.setStatus(_A)
_EthDot3ForceVLANUntagged_Type=VLANSet
_EthDot3ForceVLANUntagged_Object=MibTableColumn
ethDot3ForceVLANUntagged=_EthDot3ForceVLANUntagged_Object((1,3,6,1,4,1,2928,2,2,1,3,5,1,9),_EthDot3ForceVLANUntagged_Type())
ethDot3ForceVLANUntagged.setMaxAccess(_C)
if mibBuilder.loadTexts:ethDot3ForceVLANUntagged.setStatus(_A)
_EthDot3SupportedSpeeds_Type=AdvertisedSpeed
_EthDot3SupportedSpeeds_Object=MibTableColumn
ethDot3SupportedSpeeds=_EthDot3SupportedSpeeds_Object((1,3,6,1,4,1,2928,2,2,1,3,5,1,10),_EthDot3SupportedSpeeds_Type())
ethDot3SupportedSpeeds.setMaxAccess(_B)
if mibBuilder.loadTexts:ethDot3SupportedSpeeds.setStatus(_A)
class _EthDot3ResetToDefaults_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0))
_EthDot3ResetToDefaults_Type.__name__=_D
_EthDot3ResetToDefaults_Object=MibTableColumn
ethDot3ResetToDefaults=_EthDot3ResetToDefaults_Object((1,3,6,1,4,1,2928,2,2,1,3,5,1,11),_EthDot3ResetToDefaults_Type())
ethDot3ResetToDefaults.setMaxAccess(_C)
if mibBuilder.loadTexts:ethDot3ResetToDefaults.setStatus(_A)
_EthDot3AutoNegotiateStatus_Type=TruthValue
_EthDot3AutoNegotiateStatus_Object=MibTableColumn
ethDot3AutoNegotiateStatus=_EthDot3AutoNegotiateStatus_Object((1,3,6,1,4,1,2928,2,2,1,3,5,1,12),_EthDot3AutoNegotiateStatus_Type())
ethDot3AutoNegotiateStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:ethDot3AutoNegotiateStatus.setStatus(_A)
_EthDot3AutoNegotiateAllowed_Type=TruthValue
_EthDot3AutoNegotiateAllowed_Object=MibTableColumn
ethDot3AutoNegotiateAllowed=_EthDot3AutoNegotiateAllowed_Object((1,3,6,1,4,1,2928,2,2,1,3,5,1,13),_EthDot3AutoNegotiateAllowed_Type())
ethDot3AutoNegotiateAllowed.setMaxAccess(_B)
if mibBuilder.loadTexts:ethDot3AutoNegotiateAllowed.setStatus(_A)
_EthDot3AutoNegotiateMandatory_Type=TruthValue
_EthDot3AutoNegotiateMandatory_Object=MibTableColumn
ethDot3AutoNegotiateMandatory=_EthDot3AutoNegotiateMandatory_Object((1,3,6,1,4,1,2928,2,2,1,3,5,1,14),_EthDot3AutoNegotiateMandatory_Type())
ethDot3AutoNegotiateMandatory.setMaxAccess(_B)
if mibBuilder.loadTexts:ethDot3AutoNegotiateMandatory.setStatus(_A)
class _EthDot3SupportedIfType_Type(Bits):namedValues=NamedValues(*((_g,3),(_h,4),(_i,5),(_j,6),(_k,8),(_l,9),(_m,10),(_n,11),(_o,12)))
_EthDot3SupportedIfType_Type.__name__=_K
_EthDot3SupportedIfType_Object=MibTableColumn
ethDot3SupportedIfType=_EthDot3SupportedIfType_Object((1,3,6,1,4,1,2928,2,2,1,3,5,1,15),_EthDot3SupportedIfType_Type())
ethDot3SupportedIfType.setMaxAccess(_B)
if mibBuilder.loadTexts:ethDot3SupportedIfType.setStatus(_A)
_EthDot3SelectedIfType_Type=EthInterfaceType
_EthDot3SelectedIfType_Object=MibTableColumn
ethDot3SelectedIfType=_EthDot3SelectedIfType_Object((1,3,6,1,4,1,2928,2,2,1,3,5,1,16),_EthDot3SelectedIfType_Type())
ethDot3SelectedIfType.setMaxAccess(_C)
if mibBuilder.loadTexts:ethDot3SelectedIfType.setStatus(_A)
_EthEtsTable_Object=MibTable
ethEtsTable=_EthEtsTable_Object((1,3,6,1,4,1,2928,2,2,1,3,6))
if mibBuilder.loadTexts:ethEtsTable.setStatus(_A)
_EthEtsEntry_Object=MibTableRow
ethEtsEntry=_EthEtsEntry_Object((1,3,6,1,4,1,2928,2,2,1,3,6,1))
ethEtsEntry.setIndexNames((0,_E,_H),(0,_E,_J))
if mibBuilder.loadTexts:ethEtsEntry.setStatus(_A)
_EthEtsRowStatus_Type=RowStatus
_EthEtsRowStatus_Object=MibTableColumn
ethEtsRowStatus=_EthEtsRowStatus_Object((1,3,6,1,4,1,2928,2,2,1,3,6,1,1),_EthEtsRowStatus_Type())
ethEtsRowStatus.setMaxAccess(_I)
if mibBuilder.loadTexts:ethEtsRowStatus.setStatus(_A)
class _EthEtsMode_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('unicast',1),('multicast',2),('unspecified',3)))
_EthEtsMode_Type.__name__=_D
_EthEtsMode_Object=MibTableColumn
ethEtsMode=_EthEtsMode_Object((1,3,6,1,4,1,2928,2,2,1,3,6,1,2),_EthEtsMode_Type())
ethEtsMode.setMaxAccess(_I)
if mibBuilder.loadTexts:ethEtsMode.setStatus(_A)
_EthEtsLocalDsti_Type=Dsti
_EthEtsLocalDsti_Object=MibTableColumn
ethEtsLocalDsti=_EthEtsLocalDsti_Object((1,3,6,1,4,1,2928,2,2,1,3,6,1,3),_EthEtsLocalDsti_Type())
ethEtsLocalDsti.setMaxAccess(_I)
if mibBuilder.loadTexts:ethEtsLocalDsti.setStatus(_A)
class _EthEtsODescription_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_EthEtsODescription_Type.__name__=_G
_EthEtsODescription_Object=MibTableColumn
ethEtsODescription=_EthEtsODescription_Object((1,3,6,1,4,1,2928,2,2,1,3,6,1,4),_EthEtsODescription_Type())
ethEtsODescription.setMaxAccess(_B)
if mibBuilder.loadTexts:ethEtsODescription.setStatus(_A)
_EthEtsOConnection_Type=Unsigned32
_EthEtsOConnection_Object=MibTableColumn
ethEtsOConnection=_EthEtsOConnection_Object((1,3,6,1,4,1,2928,2,2,1,3,6,1,5),_EthEtsOConnection_Type())
ethEtsOConnection.setMaxAccess(_B)
if mibBuilder.loadTexts:ethEtsOConnection.setStatus(_A)
class _EthEtsSnkExpectChannel_Type(TruthValue):defaultValue=2
_EthEtsSnkExpectChannel_Type.__name__=_M
_EthEtsSnkExpectChannel_Object=MibTableColumn
ethEtsSnkExpectChannel=_EthEtsSnkExpectChannel_Object((1,3,6,1,4,1,2928,2,2,1,3,6,1,6),_EthEtsSnkExpectChannel_Type())
ethEtsSnkExpectChannel.setMaxAccess(_C)
if mibBuilder.loadTexts:ethEtsSnkExpectChannel.setStatus(_A)
_EthEtsTConnectionTable_Object=MibTable
ethEtsTConnectionTable=_EthEtsTConnectionTable_Object((1,3,6,1,4,1,2928,2,2,1,3,7))
if mibBuilder.loadTexts:ethEtsTConnectionTable.setStatus(_A)
_EthEtsTConnectionEntry_Object=MibTableRow
ethEtsTConnectionEntry=_EthEtsTConnectionEntry_Object((1,3,6,1,4,1,2928,2,2,1,3,7,1))
ethEtsTConnectionEntry.setIndexNames((0,_E,_H),(0,_E,_J),(0,_E,_A1))
if mibBuilder.loadTexts:ethEtsTConnectionEntry.setStatus(_A)
_EthEtsTConnectionIndex_Type=Unsigned32
_EthEtsTConnectionIndex_Object=MibTableColumn
ethEtsTConnectionIndex=_EthEtsTConnectionIndex_Object((1,3,6,1,4,1,2928,2,2,1,3,7,1,1),_EthEtsTConnectionIndex_Type())
ethEtsTConnectionIndex.setMaxAccess(_N)
if mibBuilder.loadTexts:ethEtsTConnectionIndex.setStatus(_A)
_EthEtsTConnectionRowStatus_Type=RowStatus
_EthEtsTConnectionRowStatus_Object=MibTableColumn
ethEtsTConnectionRowStatus=_EthEtsTConnectionRowStatus_Object((1,3,6,1,4,1,2928,2,2,1,3,7,1,2),_EthEtsTConnectionRowStatus_Type())
ethEtsTConnectionRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:ethEtsTConnectionRowStatus.setStatus(_A)
_EthEtsTConnection_Type=Unsigned32
_EthEtsTConnection_Object=MibTableColumn
ethEtsTConnection=_EthEtsTConnection_Object((1,3,6,1,4,1,2928,2,2,1,3,7,1,3),_EthEtsTConnection_Type())
ethEtsTConnection.setMaxAccess(_B)
if mibBuilder.loadTexts:ethEtsTConnection.setStatus(_A)
_EthEtsIndexLookupTable_Object=MibTable
ethEtsIndexLookupTable=_EthEtsIndexLookupTable_Object((1,3,6,1,4,1,2928,2,2,1,3,8))
if mibBuilder.loadTexts:ethEtsIndexLookupTable.setStatus(_A)
_EthEtsIndexLookupEntry_Object=MibTableRow
ethEtsIndexLookupEntry=_EthEtsIndexLookupEntry_Object((1,3,6,1,4,1,2928,2,2,1,3,8,1))
ethEtsIndexLookupEntry.setIndexNames((0,_E,_A2))
if mibBuilder.loadTexts:ethEtsIndexLookupEntry.setStatus(_A)
_EthEtsIndexLookupDevIndex_Type=Unsigned32
_EthEtsIndexLookupDevIndex_Object=MibTableColumn
ethEtsIndexLookupDevIndex=_EthEtsIndexLookupDevIndex_Object((1,3,6,1,4,1,2928,2,2,1,3,8,1,1),_EthEtsIndexLookupDevIndex_Type())
ethEtsIndexLookupDevIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:ethEtsIndexLookupDevIndex.setStatus(_A)
_EthEtsIndexLookupIfIndex_Type=Unsigned32
_EthEtsIndexLookupIfIndex_Object=MibTableColumn
ethEtsIndexLookupIfIndex=_EthEtsIndexLookupIfIndex_Object((1,3,6,1,4,1,2928,2,2,1,3,8,1,2),_EthEtsIndexLookupIfIndex_Type())
ethEtsIndexLookupIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:ethEtsIndexLookupIfIndex.setStatus(_A)
_EthIfRstpTable_Object=MibTable
ethIfRstpTable=_EthIfRstpTable_Object((1,3,6,1,4,1,2928,2,2,1,3,9))
if mibBuilder.loadTexts:ethIfRstpTable.setStatus(_A)
_EthIfRstpEntry_Object=MibTableRow
ethIfRstpEntry=_EthIfRstpEntry_Object((1,3,6,1,4,1,2928,2,2,1,3,9,1))
ethIfRstpEntry.setIndexNames((0,_E,_H),(0,_E,_J))
if mibBuilder.loadTexts:ethIfRstpEntry.setStatus(_A)
_EthIfRstpPortIdentifier_Type=PortIdentifier
_EthIfRstpPortIdentifier_Object=MibTableColumn
ethIfRstpPortIdentifier=_EthIfRstpPortIdentifier_Object((1,3,6,1,4,1,2928,2,2,1,3,9,1,1),_EthIfRstpPortIdentifier_Type())
ethIfRstpPortIdentifier.setMaxAccess(_B)
if mibBuilder.loadTexts:ethIfRstpPortIdentifier.setStatus(_A)
class _EthIfRstpPriority_Type(Integer32):defaultValue=128;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,240))
_EthIfRstpPriority_Type.__name__=_D
_EthIfRstpPriority_Object=MibTableColumn
ethIfRstpPriority=_EthIfRstpPriority_Object((1,3,6,1,4,1,2928,2,2,1,3,9,1,2),_EthIfRstpPriority_Type())
ethIfRstpPriority.setMaxAccess(_C)
if mibBuilder.loadTexts:ethIfRstpPriority.setStatus(_A)
class _EthIfRstpState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('discarding',1),('learning',2),('forwarding',3)))
_EthIfRstpState_Type.__name__=_D
_EthIfRstpState_Object=MibTableColumn
ethIfRstpState=_EthIfRstpState_Object((1,3,6,1,4,1,2928,2,2,1,3,9,1,3),_EthIfRstpState_Type())
ethIfRstpState.setMaxAccess(_B)
if mibBuilder.loadTexts:ethIfRstpState.setStatus(_A)
_EthIfRstpTopologyChangeAcknowledge_Type=TruthValue
_EthIfRstpTopologyChangeAcknowledge_Object=MibTableColumn
ethIfRstpTopologyChangeAcknowledge=_EthIfRstpTopologyChangeAcknowledge_Object((1,3,6,1,4,1,2928,2,2,1,3,9,1,4),_EthIfRstpTopologyChangeAcknowledge_Type())
ethIfRstpTopologyChangeAcknowledge.setMaxAccess(_B)
if mibBuilder.loadTexts:ethIfRstpTopologyChangeAcknowledge.setStatus(_A)
class _EthIfRstpPathCost_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,200000000))
_EthIfRstpPathCost_Type.__name__=_D
_EthIfRstpPathCost_Object=MibTableColumn
ethIfRstpPathCost=_EthIfRstpPathCost_Object((1,3,6,1,4,1,2928,2,2,1,3,9,1,5),_EthIfRstpPathCost_Type())
ethIfRstpPathCost.setMaxAccess(_C)
if mibBuilder.loadTexts:ethIfRstpPathCost.setStatus(_A)
_EthIfRstpDesignatedRoot_Type=BridgeIdentifier
_EthIfRstpDesignatedRoot_Object=MibTableColumn
ethIfRstpDesignatedRoot=_EthIfRstpDesignatedRoot_Object((1,3,6,1,4,1,2928,2,2,1,3,9,1,6),_EthIfRstpDesignatedRoot_Type())
ethIfRstpDesignatedRoot.setMaxAccess(_B)
if mibBuilder.loadTexts:ethIfRstpDesignatedRoot.setStatus(_A)
_EthIfRstpDesignatedCost_Type=Integer32
_EthIfRstpDesignatedCost_Object=MibTableColumn
ethIfRstpDesignatedCost=_EthIfRstpDesignatedCost_Object((1,3,6,1,4,1,2928,2,2,1,3,9,1,7),_EthIfRstpDesignatedCost_Type())
ethIfRstpDesignatedCost.setMaxAccess(_B)
if mibBuilder.loadTexts:ethIfRstpDesignatedCost.setStatus(_A)
_EthIfRstpDesignatedBridge_Type=BridgeIdentifier
_EthIfRstpDesignatedBridge_Object=MibTableColumn
ethIfRstpDesignatedBridge=_EthIfRstpDesignatedBridge_Object((1,3,6,1,4,1,2928,2,2,1,3,9,1,8),_EthIfRstpDesignatedBridge_Type())
ethIfRstpDesignatedBridge.setMaxAccess(_B)
if mibBuilder.loadTexts:ethIfRstpDesignatedBridge.setStatus(_A)
_EthIfRstpDesignatedPort_Type=PortIdentifier
_EthIfRstpDesignatedPort_Object=MibTableColumn
ethIfRstpDesignatedPort=_EthIfRstpDesignatedPort_Object((1,3,6,1,4,1,2928,2,2,1,3,9,1,9),_EthIfRstpDesignatedPort_Type())
ethIfRstpDesignatedPort.setMaxAccess(_B)
if mibBuilder.loadTexts:ethIfRstpDesignatedPort.setStatus(_A)
class _EthIfRstpAdminEdgePort_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_L,0),('true',1),('false',2)))
_EthIfRstpAdminEdgePort_Type.__name__=_D
_EthIfRstpAdminEdgePort_Object=MibTableColumn
ethIfRstpAdminEdgePort=_EthIfRstpAdminEdgePort_Object((1,3,6,1,4,1,2928,2,2,1,3,9,1,10),_EthIfRstpAdminEdgePort_Type())
ethIfRstpAdminEdgePort.setMaxAccess(_C)
if mibBuilder.loadTexts:ethIfRstpAdminEdgePort.setStatus(_A)
_EthIfRstpOperEdgePort_Type=TruthValue
_EthIfRstpOperEdgePort_Object=MibTableColumn
ethIfRstpOperEdgePort=_EthIfRstpOperEdgePort_Object((1,3,6,1,4,1,2928,2,2,1,3,9,1,11),_EthIfRstpOperEdgePort_Type())
ethIfRstpOperEdgePort.setMaxAccess(_B)
if mibBuilder.loadTexts:ethIfRstpOperEdgePort.setStatus(_A)
class _EthIfRstpAdminPointToPointMAC_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_L,0),('true',1),('false',2)))
_EthIfRstpAdminPointToPointMAC_Type.__name__=_D
_EthIfRstpAdminPointToPointMAC_Object=MibTableColumn
ethIfRstpAdminPointToPointMAC=_EthIfRstpAdminPointToPointMAC_Object((1,3,6,1,4,1,2928,2,2,1,3,9,1,12),_EthIfRstpAdminPointToPointMAC_Type())
ethIfRstpAdminPointToPointMAC.setMaxAccess(_C)
if mibBuilder.loadTexts:ethIfRstpAdminPointToPointMAC.setStatus(_A)
_EthIfRstpOperPointToPointMAC_Type=TruthValue
_EthIfRstpOperPointToPointMAC_Object=MibTableColumn
ethIfRstpOperPointToPointMAC=_EthIfRstpOperPointToPointMAC_Object((1,3,6,1,4,1,2928,2,2,1,3,9,1,13),_EthIfRstpOperPointToPointMAC_Type())
ethIfRstpOperPointToPointMAC.setMaxAccess(_B)
if mibBuilder.loadTexts:ethIfRstpOperPointToPointMAC.setStatus(_A)
class _EthIfRstpCurrentPathCost_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,200000000))
_EthIfRstpCurrentPathCost_Type.__name__=_D
_EthIfRstpCurrentPathCost_Object=MibTableColumn
ethIfRstpCurrentPathCost=_EthIfRstpCurrentPathCost_Object((1,3,6,1,4,1,2928,2,2,1,3,9,1,14),_EthIfRstpCurrentPathCost_Type())
ethIfRstpCurrentPathCost.setMaxAccess(_B)
if mibBuilder.loadTexts:ethIfRstpCurrentPathCost.setStatus(_A)
_EthIfgTable_Object=MibTable
ethIfgTable=_EthIfgTable_Object((1,3,6,1,4,1,2928,2,2,1,3,10))
if mibBuilder.loadTexts:ethIfgTable.setStatus(_A)
_EthIfgEntry_Object=MibTableRow
ethIfgEntry=_EthIfgEntry_Object((1,3,6,1,4,1,2928,2,2,1,3,10,1))
ethIfgEntry.setIndexNames((0,_E,_H),(0,_E,_J))
if mibBuilder.loadTexts:ethIfgEntry.setStatus(_A)
_EthIfgRowStatus_Type=RowStatus
_EthIfgRowStatus_Object=MibTableColumn
ethIfgRowStatus=_EthIfgRowStatus_Object((1,3,6,1,4,1,2928,2,2,1,3,10,1,1),_EthIfgRowStatus_Type())
ethIfgRowStatus.setMaxAccess(_I)
if mibBuilder.loadTexts:ethIfgRowStatus.setStatus(_A)
_EthIfgMembers_Type=InterfaceIndexList
_EthIfgMembers_Object=MibTableColumn
ethIfgMembers=_EthIfgMembers_Object((1,3,6,1,4,1,2928,2,2,1,3,10,1,2),_EthIfgMembers_Type())
ethIfgMembers.setMaxAccess(_B)
if mibBuilder.loadTexts:ethIfgMembers.setStatus(_A)
_EthIfgDifferentialDelay_Type=Unsigned32
_EthIfgDifferentialDelay_Object=MibTableColumn
ethIfgDifferentialDelay=_EthIfgDifferentialDelay_Object((1,3,6,1,4,1,2928,2,2,1,3,10,1,3),_EthIfgDifferentialDelay_Type())
ethIfgDifferentialDelay.setMaxAccess(_B)
if mibBuilder.loadTexts:ethIfgDifferentialDelay.setStatus(_A)
_EthIfgDifferentialDelayValid_Type=TruthValue
_EthIfgDifferentialDelayValid_Object=MibTableColumn
ethIfgDifferentialDelayValid=_EthIfgDifferentialDelayValid_Object((1,3,6,1,4,1,2928,2,2,1,3,10,1,4),_EthIfgDifferentialDelayValid_Type())
ethIfgDifferentialDelayValid.setMaxAccess(_B)
if mibBuilder.loadTexts:ethIfgDifferentialDelayValid.setStatus(_A)
_EthIfgAheadInterface_Type=Unsigned32
_EthIfgAheadInterface_Object=MibTableColumn
ethIfgAheadInterface=_EthIfgAheadInterface_Object((1,3,6,1,4,1,2928,2,2,1,3,10,1,5),_EthIfgAheadInterface_Type())
ethIfgAheadInterface.setMaxAccess(_B)
if mibBuilder.loadTexts:ethIfgAheadInterface.setStatus(_A)
class _EthIfgHitlessProtection_Type(TruthValue):defaultValue=2
_EthIfgHitlessProtection_Type.__name__=_M
_EthIfgHitlessProtection_Object=MibTableColumn
ethIfgHitlessProtection=_EthIfgHitlessProtection_Object((1,3,6,1,4,1,2928,2,2,1,3,10,1,6),_EthIfgHitlessProtection_Type())
ethIfgHitlessProtection.setMaxAccess(_I)
if mibBuilder.loadTexts:ethIfgHitlessProtection.setStatus(_A)
_EthIfgProtectionStatus_Type=IfgProtectionStatus
_EthIfgProtectionStatus_Object=MibTableColumn
ethIfgProtectionStatus=_EthIfgProtectionStatus_Object((1,3,6,1,4,1,2928,2,2,1,3,10,1,7),_EthIfgProtectionStatus_Type())
ethIfgProtectionStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:ethIfgProtectionStatus.setStatus(_A)
class _EthIfgExpectedProtectionStatus_Type(IfgProtectionStatus):defaultValue=1
_EthIfgExpectedProtectionStatus_Type.__name__=_A3
_EthIfgExpectedProtectionStatus_Object=MibTableColumn
ethIfgExpectedProtectionStatus=_EthIfgExpectedProtectionStatus_Object((1,3,6,1,4,1,2928,2,2,1,3,10,1,8),_EthIfgExpectedProtectionStatus_Type())
ethIfgExpectedProtectionStatus.setMaxAccess(_I)
if mibBuilder.loadTexts:ethIfgExpectedProtectionStatus.setStatus(_A)
class _EthIfgForceHit_Type(Unsigned32):defaultValue=0
_EthIfgForceHit_Type.__name__=_G
_EthIfgForceHit_Object=MibTableColumn
ethIfgForceHit=_EthIfgForceHit_Object((1,3,6,1,4,1,2928,2,2,1,3,10,1,9),_EthIfgForceHit_Type())
ethIfgForceHit.setMaxAccess(_I)
if mibBuilder.loadTexts:ethIfgForceHit.setStatus(_A)
_EthIfgActiveInterface_Type=Unsigned32
_EthIfgActiveInterface_Object=MibTableColumn
ethIfgActiveInterface=_EthIfgActiveInterface_Object((1,3,6,1,4,1,2928,2,2,1,3,10,1,10),_EthIfgActiveInterface_Type())
ethIfgActiveInterface.setMaxAccess(_I)
if mibBuilder.loadTexts:ethIfgActiveInterface.setStatus(_A)
_EthIfgExpectChannel_Type=TruthValue
_EthIfgExpectChannel_Object=MibTableColumn
ethIfgExpectChannel=_EthIfgExpectChannel_Object((1,3,6,1,4,1,2928,2,2,1,3,10,1,11),_EthIfgExpectChannel_Type())
ethIfgExpectChannel.setMaxAccess(_I)
if mibBuilder.loadTexts:ethIfgExpectChannel.setStatus(_A)
_EthIfQDropThresholdTable_Object=MibTable
ethIfQDropThresholdTable=_EthIfQDropThresholdTable_Object((1,3,6,1,4,1,2928,2,2,1,3,11))
if mibBuilder.loadTexts:ethIfQDropThresholdTable.setStatus(_A)
_EthIfQDropThresholdEntry_Object=MibTableRow
ethIfQDropThresholdEntry=_EthIfQDropThresholdEntry_Object((1,3,6,1,4,1,2928,2,2,1,3,11,1))
ethIfQDropThresholdEntry.setIndexNames((0,_E,_H),(0,_E,_J),(0,_E,_d),(0,_E,_A4))
if mibBuilder.loadTexts:ethIfQDropThresholdEntry.setStatus(_A)
_EthIfQDropThresDropPrecedence_Type=Unsigned32
_EthIfQDropThresDropPrecedence_Object=MibTableColumn
ethIfQDropThresDropPrecedence=_EthIfQDropThresDropPrecedence_Object((1,3,6,1,4,1,2928,2,2,1,3,11,1,1),_EthIfQDropThresDropPrecedence_Type())
ethIfQDropThresDropPrecedence.setMaxAccess(_B)
if mibBuilder.loadTexts:ethIfQDropThresDropPrecedence.setStatus(_A)
class _EthIfQDropThresMaxFrames_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,2147483647))
_EthIfQDropThresMaxFrames_Type.__name__=_D
_EthIfQDropThresMaxFrames_Object=MibTableColumn
ethIfQDropThresMaxFrames=_EthIfQDropThresMaxFrames_Object((1,3,6,1,4,1,2928,2,2,1,3,11,1,2),_EthIfQDropThresMaxFrames_Type())
ethIfQDropThresMaxFrames.setMaxAccess(_C)
if mibBuilder.loadTexts:ethIfQDropThresMaxFrames.setStatus(_A)
class _EthIfQDropThresCurrentMaxFrames_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_EthIfQDropThresCurrentMaxFrames_Type.__name__=_D
_EthIfQDropThresCurrentMaxFrames_Object=MibTableColumn
ethIfQDropThresCurrentMaxFrames=_EthIfQDropThresCurrentMaxFrames_Object((1,3,6,1,4,1,2928,2,2,1,3,11,1,3),_EthIfQDropThresCurrentMaxFrames_Type())
ethIfQDropThresCurrentMaxFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:ethIfQDropThresCurrentMaxFrames.setStatus(_A)
class _EthIfQDropThresDropProbabilityFunction_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_t,0),('wred',1)))
_EthIfQDropThresDropProbabilityFunction_Type.__name__=_D
_EthIfQDropThresDropProbabilityFunction_Object=MibTableColumn
ethIfQDropThresDropProbabilityFunction=_EthIfQDropThresDropProbabilityFunction_Object((1,3,6,1,4,1,2928,2,2,1,3,11,1,4),_EthIfQDropThresDropProbabilityFunction_Type())
ethIfQDropThresDropProbabilityFunction.setMaxAccess(_C)
if mibBuilder.loadTexts:ethIfQDropThresDropProbabilityFunction.setStatus(_A)
_EthStatisticsGroup_ObjectIdentity=ObjectIdentity
ethStatisticsGroup=_EthStatisticsGroup_ObjectIdentity((1,3,6,1,4,1,2928,2,2,1,4))
_EthStatDcap1Table_Object=MibTable
ethStatDcap1Table=_EthStatDcap1Table_Object((1,3,6,1,4,1,2928,2,2,1,4,1))
if mibBuilder.loadTexts:ethStatDcap1Table.setStatus(_A)
_EthStatDcap1Entry_Object=MibTableRow
ethStatDcap1Entry=_EthStatDcap1Entry_Object((1,3,6,1,4,1,2928,2,2,1,4,1,1))
ethStatDcap1Entry.setIndexNames((0,_E,_H),(0,_E,_J))
if mibBuilder.loadTexts:ethStatDcap1Entry.setStatus(_A)
class _EthStatDcap1Reset_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0))
_EthStatDcap1Reset_Type.__name__=_D
_EthStatDcap1Reset_Object=MibTableColumn
ethStatDcap1Reset=_EthStatDcap1Reset_Object((1,3,6,1,4,1,2928,2,2,1,4,1,1,1),_EthStatDcap1Reset_Type())
ethStatDcap1Reset.setMaxAccess(_C)
if mibBuilder.loadTexts:ethStatDcap1Reset.setStatus(_A)
_EthStatDcap1TxOctets_Type=Counter64
_EthStatDcap1TxOctets_Object=MibTableColumn
ethStatDcap1TxOctets=_EthStatDcap1TxOctets_Object((1,3,6,1,4,1,2928,2,2,1,4,1,1,2),_EthStatDcap1TxOctets_Type())
ethStatDcap1TxOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:ethStatDcap1TxOctets.setStatus(_A)
_EthStatDcap1TxPackets_Type=Counter64
_EthStatDcap1TxPackets_Object=MibTableColumn
ethStatDcap1TxPackets=_EthStatDcap1TxPackets_Object((1,3,6,1,4,1,2928,2,2,1,4,1,1,3),_EthStatDcap1TxPackets_Type())
ethStatDcap1TxPackets.setMaxAccess(_B)
if mibBuilder.loadTexts:ethStatDcap1TxPackets.setStatus(_A)
_EthStatDcap1TxDiscardOctets_Type=Counter64
_EthStatDcap1TxDiscardOctets_Object=MibTableColumn
ethStatDcap1TxDiscardOctets=_EthStatDcap1TxDiscardOctets_Object((1,3,6,1,4,1,2928,2,2,1,4,1,1,4),_EthStatDcap1TxDiscardOctets_Type())
ethStatDcap1TxDiscardOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:ethStatDcap1TxDiscardOctets.setStatus(_A)
_EthStatDcap1TxDiscardPackets_Type=Counter64
_EthStatDcap1TxDiscardPackets_Object=MibTableColumn
ethStatDcap1TxDiscardPackets=_EthStatDcap1TxDiscardPackets_Object((1,3,6,1,4,1,2928,2,2,1,4,1,1,5),_EthStatDcap1TxDiscardPackets_Type())
ethStatDcap1TxDiscardPackets.setMaxAccess(_B)
if mibBuilder.loadTexts:ethStatDcap1TxDiscardPackets.setStatus(_A)
_EthStatDcap1TxBitrate_Type=Counter64
_EthStatDcap1TxBitrate_Object=MibTableColumn
ethStatDcap1TxBitrate=_EthStatDcap1TxBitrate_Object((1,3,6,1,4,1,2928,2,2,1,4,1,1,6),_EthStatDcap1TxBitrate_Type())
ethStatDcap1TxBitrate.setMaxAccess(_B)
if mibBuilder.loadTexts:ethStatDcap1TxBitrate.setStatus(_A)
class _EthStatDcap1TxLoad_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_EthStatDcap1TxLoad_Type.__name__=_G
_EthStatDcap1TxLoad_Object=MibTableColumn
ethStatDcap1TxLoad=_EthStatDcap1TxLoad_Object((1,3,6,1,4,1,2928,2,2,1,4,1,1,7),_EthStatDcap1TxLoad_Type())
ethStatDcap1TxLoad.setMaxAccess(_B)
if mibBuilder.loadTexts:ethStatDcap1TxLoad.setStatus(_A)
_EthStatDcap1RxOctets_Type=Counter64
_EthStatDcap1RxOctets_Object=MibTableColumn
ethStatDcap1RxOctets=_EthStatDcap1RxOctets_Object((1,3,6,1,4,1,2928,2,2,1,4,1,1,8),_EthStatDcap1RxOctets_Type())
ethStatDcap1RxOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:ethStatDcap1RxOctets.setStatus(_A)
_EthStatDcap1RxPackets_Type=Counter64
_EthStatDcap1RxPackets_Object=MibTableColumn
ethStatDcap1RxPackets=_EthStatDcap1RxPackets_Object((1,3,6,1,4,1,2928,2,2,1,4,1,1,9),_EthStatDcap1RxPackets_Type())
ethStatDcap1RxPackets.setMaxAccess(_B)
if mibBuilder.loadTexts:ethStatDcap1RxPackets.setStatus(_A)
_EthStatDcap1RxDiscardOctets_Type=Counter64
_EthStatDcap1RxDiscardOctets_Object=MibTableColumn
ethStatDcap1RxDiscardOctets=_EthStatDcap1RxDiscardOctets_Object((1,3,6,1,4,1,2928,2,2,1,4,1,1,10),_EthStatDcap1RxDiscardOctets_Type())
ethStatDcap1RxDiscardOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:ethStatDcap1RxDiscardOctets.setStatus(_A)
_EthStatDcap1RxDiscardPackets_Type=Counter64
_EthStatDcap1RxDiscardPackets_Object=MibTableColumn
ethStatDcap1RxDiscardPackets=_EthStatDcap1RxDiscardPackets_Object((1,3,6,1,4,1,2928,2,2,1,4,1,1,11),_EthStatDcap1RxDiscardPackets_Type())
ethStatDcap1RxDiscardPackets.setMaxAccess(_B)
if mibBuilder.loadTexts:ethStatDcap1RxDiscardPackets.setStatus(_A)
_EthStatDcap1RxErrorCRC_Type=Counter64
_EthStatDcap1RxErrorCRC_Object=MibTableColumn
ethStatDcap1RxErrorCRC=_EthStatDcap1RxErrorCRC_Object((1,3,6,1,4,1,2928,2,2,1,4,1,1,12),_EthStatDcap1RxErrorCRC_Type())
ethStatDcap1RxErrorCRC.setMaxAccess(_B)
if mibBuilder.loadTexts:ethStatDcap1RxErrorCRC.setStatus(_A)
_EthStatDcap1RxBitrate_Type=Counter64
_EthStatDcap1RxBitrate_Object=MibTableColumn
ethStatDcap1RxBitrate=_EthStatDcap1RxBitrate_Object((1,3,6,1,4,1,2928,2,2,1,4,1,1,13),_EthStatDcap1RxBitrate_Type())
ethStatDcap1RxBitrate.setMaxAccess(_B)
if mibBuilder.loadTexts:ethStatDcap1RxBitrate.setStatus(_A)
class _EthStatDcap1RxLoad_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_EthStatDcap1RxLoad_Type.__name__=_G
_EthStatDcap1RxLoad_Object=MibTableColumn
ethStatDcap1RxLoad=_EthStatDcap1RxLoad_Object((1,3,6,1,4,1,2928,2,2,1,4,1,1,14),_EthStatDcap1RxLoad_Type())
ethStatDcap1RxLoad.setMaxAccess(_B)
if mibBuilder.loadTexts:ethStatDcap1RxLoad.setStatus(_A)
_EthIfStatTable_Object=MibTable
ethIfStatTable=_EthIfStatTable_Object((1,3,6,1,4,1,2928,2,2,1,4,2))
if mibBuilder.loadTexts:ethIfStatTable.setStatus(_A)
_EthIfStatEntry_Object=MibTableRow
ethIfStatEntry=_EthIfStatEntry_Object((1,3,6,1,4,1,2928,2,2,1,4,2,1))
ethIfStatEntry.setIndexNames((0,_E,_H),(0,_E,_J))
if mibBuilder.loadTexts:ethIfStatEntry.setStatus(_A)
_EthIfStatReset_Type=Integer32
_EthIfStatReset_Object=MibTableColumn
ethIfStatReset=_EthIfStatReset_Object((1,3,6,1,4,1,2928,2,2,1,4,2,1,1),_EthIfStatReset_Type())
ethIfStatReset.setMaxAccess(_C)
if mibBuilder.loadTexts:ethIfStatReset.setStatus(_A)
_EthIfStatTxBitrate_Type=Counter64
_EthIfStatTxBitrate_Object=MibTableColumn
ethIfStatTxBitrate=_EthIfStatTxBitrate_Object((1,3,6,1,4,1,2928,2,2,1,4,2,1,2),_EthIfStatTxBitrate_Type())
ethIfStatTxBitrate.setMaxAccess(_B)
if mibBuilder.loadTexts:ethIfStatTxBitrate.setStatus(_A)
class _EthIfStatTxLoad_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_EthIfStatTxLoad_Type.__name__=_G
_EthIfStatTxLoad_Object=MibTableColumn
ethIfStatTxLoad=_EthIfStatTxLoad_Object((1,3,6,1,4,1,2928,2,2,1,4,2,1,3),_EthIfStatTxLoad_Type())
ethIfStatTxLoad.setMaxAccess(_B)
if mibBuilder.loadTexts:ethIfStatTxLoad.setStatus(_A)
_EthIfStatRxBitrate_Type=Counter64
_EthIfStatRxBitrate_Object=MibTableColumn
ethIfStatRxBitrate=_EthIfStatRxBitrate_Object((1,3,6,1,4,1,2928,2,2,1,4,2,1,4),_EthIfStatRxBitrate_Type())
ethIfStatRxBitrate.setMaxAccess(_B)
if mibBuilder.loadTexts:ethIfStatRxBitrate.setStatus(_A)
class _EthIfStatRxLoad_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_EthIfStatRxLoad_Type.__name__=_G
_EthIfStatRxLoad_Object=MibTableColumn
ethIfStatRxLoad=_EthIfStatRxLoad_Object((1,3,6,1,4,1,2928,2,2,1,4,2,1,5),_EthIfStatRxLoad_Type())
ethIfStatRxLoad.setMaxAccess(_B)
if mibBuilder.loadTexts:ethIfStatRxLoad.setStatus(_A)
mibBuilder.exportSymbols(_E,**{_v:TrafficClass,'VLANSet':VLANSet,_x:AdvertisedSpeed,_y:AdvertisedDuplex,_z:AdvertisedFlowControl,'BridgeIdentifier':BridgeIdentifier,'EthInterfaceType':EthInterfaceType,'PortIdentifier':PortIdentifier,_Y:Timeout,_F:FrameProcess,'InterfaceIndexList':InterfaceIndexList,_A3:IfgProtectionStatus,'netiEthMIB':netiEthMIB,'ethObjects':ethObjects,'ethDeviceGroup':ethDeviceGroup,'ethDeviceTable':ethDeviceTable,'ethDeviceEntry':ethDeviceEntry,_H:ethDevIndex,'ethDevRowStatus':ethDevRowStatus,'ethDevName':ethDevName,'ethDevContainerName':ethDevContainerName,'ethDevProductName':ethDevProductName,'ethDevStatus':ethDevStatus,'ethDevCapJumboFrames':ethDevCapJumboFrames,'ethDevCapMaxAgingTime':ethDevCapMaxAgingTime,'ethDevCapMACMode':ethDevCapMACMode,'ethDevCapSpanningTree':ethDevCapSpanningTree,'ethDevCapVLANMode':ethDevCapVLANMode,'ethDevCapAdvertisedDuplex':ethDevCapAdvertisedDuplex,'ethDevCapAdvertisedFlowControl':ethDevCapAdvertisedFlowControl,'ethDevCapAcceptableFrameType':ethDevCapAcceptableFrameType,'ethDevCapDefaultEthernetPriority':ethDevCapDefaultEthernetPriority,'ethDevCapLearning':ethDevCapLearning,'ethDevCapTransmittedFrameTypeETS':ethDevCapTransmittedFrameTypeETS,'ethDevCapTransmittedFrameTypeDot3':ethDevCapTransmittedFrameTypeDot3,'ethDevCapMaxMaxQueueOctets':ethDevCapMaxMaxQueueOctets,'ethDevCapMaxMaxQueueFrames':ethDevCapMaxMaxQueueFrames,'ethDevCapMaxTrafficClass':ethDevCapMaxTrafficClass,'ethDevEtsNextIndex':ethDevEtsNextIndex,'ethDevFwdFuncNextIndex':ethDevFwdFuncNextIndex,'ethDevCapPerformanceMonitoring':ethDevCapPerformanceMonitoring,'ethDevCapConfigurableFaultMgmt':ethDevCapConfigurableFaultMgmt,'ethDevIfgFirstIndex':ethDevIfgFirstIndex,'ethDevIfgNextIndex':ethDevIfgNextIndex,'ethDevCapDropPrecedenceLevels':ethDevCapDropPrecedenceLevels,'ethDevCapDropProbabilityFunctions':ethDevCapDropProbabilityFunctions,'ethDevFailure':ethDevFailure,'ethFwdFuncGroup':ethFwdFuncGroup,'ethFwdFuncLastChange':ethFwdFuncLastChange,'ethFwdFuncTable':ethFwdFuncTable,'ethFwdFuncEntry':ethFwdFuncEntry,_X:ethFwdIndex,'ethFwdRowStatus':ethFwdRowStatus,'ethFwdName':ethFwdName,'ethFwdCustomerId':ethFwdCustomerId,'ethFwdPurpose':ethFwdPurpose,'ethFwdJumboFrames':ethFwdJumboFrames,'ethFwdMACMode':ethFwdMACMode,'ethFwdCurrentMACMode':ethFwdCurrentMACMode,'ethFwdSpanningTree':ethFwdSpanningTree,'ethFwdVLANMode':ethFwdVLANMode,'ethFwdAgingTime':ethFwdAgingTime,'ethFwdFailure':ethFwdFailure,'ethFwdLastChange':ethFwdLastChange,'ethFwdPropagateFaults':ethFwdPropagateFaults,'ethFwdReservedAddr0180C2000002':ethFwdReservedAddr0180C2000002,'ethFwdReservedAddr0180C2000003':ethFwdReservedAddr0180C2000003,'ethFwdReservedAddr0180C2000004':ethFwdReservedAddr0180C2000004,'ethFwdReservedAddr0180C2000005':ethFwdReservedAddr0180C2000005,'ethFwdReservedAddr0180C2000006':ethFwdReservedAddr0180C2000006,'ethFwdReservedAddr0180C2000007':ethFwdReservedAddr0180C2000007,'ethFwdReservedAddr0180C2000008':ethFwdReservedAddr0180C2000008,'ethFwdReservedAddr0180C2000009':ethFwdReservedAddr0180C2000009,'ethFwdReservedAddr0180C200000A':ethFwdReservedAddr0180C200000A,'ethFwdReservedAddr0180C200000B':ethFwdReservedAddr0180C200000B,'ethFwdReservedAddr0180C200000C':ethFwdReservedAddr0180C200000C,'ethFwdReservedAddr0180C200000D':ethFwdReservedAddr0180C200000D,'ethFwdReservedAddr0180C200000E':ethFwdReservedAddr0180C200000E,'ethFwdReservedAddr0180C200000F':ethFwdReservedAddr0180C200000F,'ethFwdCurrentStpMode':ethFwdCurrentStpMode,'ethFwdMrpAddr0180C2000020':ethFwdMrpAddr0180C2000020,'ethFwdMrpAddr0180C2000021':ethFwdMrpAddr0180C2000021,'ethFwdMrpAddr0180C2000022':ethFwdMrpAddr0180C2000022,'ethFwdMrpAddr0180C2000023':ethFwdMrpAddr0180C2000023,'ethFwdMrpAddr0180C2000024':ethFwdMrpAddr0180C2000024,'ethFwdMrpAddr0180C2000025':ethFwdMrpAddr0180C2000025,'ethFwdMrpAddr0180C2000026':ethFwdMrpAddr0180C2000026,'ethFwdMrpAddr0180C2000027':ethFwdMrpAddr0180C2000027,'ethFwdMrpAddr0180C2000028':ethFwdMrpAddr0180C2000028,'ethFwdMrpAddr0180C2000029':ethFwdMrpAddr0180C2000029,'ethFwdMrpAddr0180C200002A':ethFwdMrpAddr0180C200002A,'ethFwdMrpAddr0180C200002B':ethFwdMrpAddr0180C200002B,'ethFwdMrpAddr0180C200002C':ethFwdMrpAddr0180C200002C,'ethFwdMrpAddr0180C200002D':ethFwdMrpAddr0180C200002D,'ethFwdMrpAddr0180C200002E':ethFwdMrpAddr0180C200002E,'ethFwdMrpAddr0180C200002F':ethFwdMrpAddr0180C200002F,'ethFwdDiffservTable':ethFwdDiffservTable,'ethFwdDiffservEntry':ethFwdDiffservEntry,_u:ethFwdDiffservIndex,'ethFwdDiffservFlowGroup':ethFwdDiffservFlowGroup,'ethFwdRstpTable':ethFwdRstpTable,'ethFwdRstpEntry':ethFwdRstpEntry,'ethFwdRstpBridgeIdentifier':ethFwdRstpBridgeIdentifier,'ethFwdRstpPriority':ethFwdRstpPriority,'ethFwdRstpTimeSinceTopologyChange':ethFwdRstpTimeSinceTopologyChange,'ethFwdRstpTopologyChangeCount':ethFwdRstpTopologyChangeCount,'ethFwdRstpTopologyChange':ethFwdRstpTopologyChange,'ethFwdRstpDesignatedRoot':ethFwdRstpDesignatedRoot,'ethFwdRstpRootPathCost':ethFwdRstpRootPathCost,'ethFwdRstpRootPortName':ethFwdRstpRootPortName,'ethFwdRstpMaxAge':ethFwdRstpMaxAge,'ethFwdRstpHelloTime':ethFwdRstpHelloTime,'ethFwdRstpForwardDelay':ethFwdRstpForwardDelay,'ethFwdRstpBridgeMaxAge':ethFwdRstpBridgeMaxAge,'ethFwdRstpBridgeHelloTime':ethFwdRstpBridgeHelloTime,'ethFwdRstpBridgeForwardDelay':ethFwdRstpBridgeForwardDelay,'ethFwdRstpTxHoldCount':ethFwdRstpTxHoldCount,'ethFwdRstpForceVersion':ethFwdRstpForceVersion,'ethInterfaceGroup':ethInterfaceGroup,'ethIfGroupLastChange':ethIfGroupLastChange,'ethIfTable':ethIfTable,'ethIfEntry':ethIfEntry,_J:ethIfIndex,'ethIfIfIndex':ethIfIfIndex,'ethIfName':ethIfName,'ethIfType':ethIfType,'ethIfCustomerId':ethIfCustomerId,'ethIfPurpose':ethIfPurpose,'ethIfAdminStatus':ethIfAdminStatus,'ethIfOperStatus':ethIfOperStatus,'ethIfFailure':ethIfFailure,'ethIfForwardingFunction':ethIfForwardingFunction,'ethIfAcceptableFrameTypes':ethIfAcceptableFrameTypes,'ethIfTransmittedFrameType':ethIfTransmittedFrameType,'ethIfDefaultVLAN':ethIfDefaultVLAN,'ethIfDefaultEthernetPriority':ethIfDefaultEthernetPriority,'ethIfPriorityMode':ethIfPriorityMode,'ethIfDefaultTrafficClass':ethIfDefaultTrafficClass,'ethIfFlowGroupMap':ethIfFlowGroupMap,'ethIfLearning':ethIfLearning,'ethIfInSpeed':ethIfInSpeed,'ethIfInHighSpeed':ethIfInHighSpeed,'ethIfOutSpeed':ethIfOutSpeed,'ethIfOutHighSpeed':ethIfOutHighSpeed,'ethIfVLANNextIndex':ethIfVLANNextIndex,'ethIfLastChange':ethIfLastChange,'ethIfSrcPmReference':ethIfSrcPmReference,'ethIfSnkPmReference':ethIfSnkPmReference,'ethIfSrcDegThreshold':ethIfSrcDegThreshold,'ethIfSnkDegThreshold':ethIfSnkDegThreshold,'ethIfSrcDegPeriod':ethIfSrcDegPeriod,'ethIfSnkDegPeriod':ethIfSnkDegPeriod,'ethIfSrcReducedBitRateThreshold':ethIfSrcReducedBitRateThreshold,'ethIfSnkReducedBitRateThreshold':ethIfSnkReducedBitRateThreshold,'ethIfSrcReducedBitRateHighThreshold':ethIfSrcReducedBitRateHighThreshold,'ethIfSnkReducedBitRateHighThreshold':ethIfSnkReducedBitRateHighThreshold,'ethIfSrcReducedBitRateAIS':ethIfSrcReducedBitRateAIS,'ethIfSnkReducedBitRateAIS':ethIfSnkReducedBitRateAIS,'ethIfSnkDegAIS':ethIfSnkDegAIS,'ethIfSrcMinorReducedBitRateThreshold':ethIfSrcMinorReducedBitRateThreshold,'ethIfSnkMinorReducedBitRateThreshold':ethIfSnkMinorReducedBitRateThreshold,'ethIfSrcMinorReducedBitRateHighThreshold':ethIfSrcMinorReducedBitRateHighThreshold,'ethIfSnkMinorReducedBitRateHighThreshold':ethIfSnkMinorReducedBitRateHighThreshold,'ethIfSrcFailure':ethIfSrcFailure,'ethIfSnkFailure':ethIfSnkFailure,'ethIfInterfaceGroup':ethIfInterfaceGroup,'ethIfMaxMaxQueueFrames':ethIfMaxMaxQueueFrames,'ethIfDefaultDropPrecedence':ethIfDefaultDropPrecedence,'ethIfDropPrecedenceMap':ethIfDropPrecedenceMap,'ethIfQueueTable':ethIfQueueTable,'ethIfQueueEntry':ethIfQueueEntry,_d:ethIfQueueTrafficClass,'ethIfQueueMaxOctets':ethIfQueueMaxOctets,'ethIfQueueMaxFrames':ethIfQueueMaxFrames,'ethIfVLANSetsTable':ethIfVLANSetsTable,'ethIfVLANSetsEntry':ethIfVLANSetsEntry,_w:ethIfVLANSetIndex,'ethIfVLANRowStatus':ethIfVLANRowStatus,'ethIfVLANSet':ethIfVLANSet,'ethIfVLANCustomerId':ethIfVLANCustomerId,'ethIfVLANPurpose':ethIfVLANPurpose,'ethDot3Table':ethDot3Table,'ethDot3Entry':ethDot3Entry,'ethDot3AutoNegotiate':ethDot3AutoNegotiate,'ethDot3AdvertisedSpeed':ethDot3AdvertisedSpeed,'ethDot3AdvertisedDuplex':ethDot3AdvertisedDuplex,'ethDot3AdvertisedFlowControl':ethDot3AdvertisedFlowControl,'ethDot3ActiveSpeed':ethDot3ActiveSpeed,'ethDot3ActiveDuplex':ethDot3ActiveDuplex,'ethDot3ActiveFlowControl':ethDot3ActiveFlowControl,'ethDot3ForceVLANTagged':ethDot3ForceVLANTagged,'ethDot3ForceVLANUntagged':ethDot3ForceVLANUntagged,'ethDot3SupportedSpeeds':ethDot3SupportedSpeeds,'ethDot3ResetToDefaults':ethDot3ResetToDefaults,'ethDot3AutoNegotiateStatus':ethDot3AutoNegotiateStatus,'ethDot3AutoNegotiateAllowed':ethDot3AutoNegotiateAllowed,'ethDot3AutoNegotiateMandatory':ethDot3AutoNegotiateMandatory,'ethDot3SupportedIfType':ethDot3SupportedIfType,'ethDot3SelectedIfType':ethDot3SelectedIfType,'ethEtsTable':ethEtsTable,'ethEtsEntry':ethEtsEntry,'ethEtsRowStatus':ethEtsRowStatus,'ethEtsMode':ethEtsMode,_A2:ethEtsLocalDsti,'ethEtsODescription':ethEtsODescription,'ethEtsOConnection':ethEtsOConnection,'ethEtsSnkExpectChannel':ethEtsSnkExpectChannel,'ethEtsTConnectionTable':ethEtsTConnectionTable,'ethEtsTConnectionEntry':ethEtsTConnectionEntry,_A1:ethEtsTConnectionIndex,'ethEtsTConnectionRowStatus':ethEtsTConnectionRowStatus,'ethEtsTConnection':ethEtsTConnection,'ethEtsIndexLookupTable':ethEtsIndexLookupTable,'ethEtsIndexLookupEntry':ethEtsIndexLookupEntry,'ethEtsIndexLookupDevIndex':ethEtsIndexLookupDevIndex,'ethEtsIndexLookupIfIndex':ethEtsIndexLookupIfIndex,'ethIfRstpTable':ethIfRstpTable,'ethIfRstpEntry':ethIfRstpEntry,'ethIfRstpPortIdentifier':ethIfRstpPortIdentifier,'ethIfRstpPriority':ethIfRstpPriority,'ethIfRstpState':ethIfRstpState,'ethIfRstpTopologyChangeAcknowledge':ethIfRstpTopologyChangeAcknowledge,'ethIfRstpPathCost':ethIfRstpPathCost,'ethIfRstpDesignatedRoot':ethIfRstpDesignatedRoot,'ethIfRstpDesignatedCost':ethIfRstpDesignatedCost,'ethIfRstpDesignatedBridge':ethIfRstpDesignatedBridge,'ethIfRstpDesignatedPort':ethIfRstpDesignatedPort,'ethIfRstpAdminEdgePort':ethIfRstpAdminEdgePort,'ethIfRstpOperEdgePort':ethIfRstpOperEdgePort,'ethIfRstpAdminPointToPointMAC':ethIfRstpAdminPointToPointMAC,'ethIfRstpOperPointToPointMAC':ethIfRstpOperPointToPointMAC,'ethIfRstpCurrentPathCost':ethIfRstpCurrentPathCost,'ethIfgTable':ethIfgTable,'ethIfgEntry':ethIfgEntry,'ethIfgRowStatus':ethIfgRowStatus,'ethIfgMembers':ethIfgMembers,'ethIfgDifferentialDelay':ethIfgDifferentialDelay,'ethIfgDifferentialDelayValid':ethIfgDifferentialDelayValid,'ethIfgAheadInterface':ethIfgAheadInterface,'ethIfgHitlessProtection':ethIfgHitlessProtection,'ethIfgProtectionStatus':ethIfgProtectionStatus,'ethIfgExpectedProtectionStatus':ethIfgExpectedProtectionStatus,'ethIfgForceHit':ethIfgForceHit,'ethIfgActiveInterface':ethIfgActiveInterface,'ethIfgExpectChannel':ethIfgExpectChannel,'ethIfQDropThresholdTable':ethIfQDropThresholdTable,'ethIfQDropThresholdEntry':ethIfQDropThresholdEntry,_A4:ethIfQDropThresDropPrecedence,'ethIfQDropThresMaxFrames':ethIfQDropThresMaxFrames,'ethIfQDropThresCurrentMaxFrames':ethIfQDropThresCurrentMaxFrames,'ethIfQDropThresDropProbabilityFunction':ethIfQDropThresDropProbabilityFunction,'ethStatisticsGroup':ethStatisticsGroup,'ethStatDcap1Table':ethStatDcap1Table,'ethStatDcap1Entry':ethStatDcap1Entry,'ethStatDcap1Reset':ethStatDcap1Reset,'ethStatDcap1TxOctets':ethStatDcap1TxOctets,'ethStatDcap1TxPackets':ethStatDcap1TxPackets,'ethStatDcap1TxDiscardOctets':ethStatDcap1TxDiscardOctets,'ethStatDcap1TxDiscardPackets':ethStatDcap1TxDiscardPackets,'ethStatDcap1TxBitrate':ethStatDcap1TxBitrate,'ethStatDcap1TxLoad':ethStatDcap1TxLoad,'ethStatDcap1RxOctets':ethStatDcap1RxOctets,'ethStatDcap1RxPackets':ethStatDcap1RxPackets,'ethStatDcap1RxDiscardOctets':ethStatDcap1RxDiscardOctets,'ethStatDcap1RxDiscardPackets':ethStatDcap1RxDiscardPackets,'ethStatDcap1RxErrorCRC':ethStatDcap1RxErrorCRC,'ethStatDcap1RxBitrate':ethStatDcap1RxBitrate,'ethStatDcap1RxLoad':ethStatDcap1RxLoad,'ethIfStatTable':ethIfStatTable,'ethIfStatEntry':ethIfStatEntry,'ethIfStatReset':ethIfStatReset,'ethIfStatTxBitrate':ethIfStatTxBitrate,'ethIfStatTxLoad':ethIfStatTxLoad,'ethIfStatRxBitrate':ethIfStatRxBitrate,'ethIfStatRxLoad':ethIfStatRxLoad})