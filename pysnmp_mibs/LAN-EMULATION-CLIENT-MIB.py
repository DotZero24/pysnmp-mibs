_Ap='leClientRDArpGroup'
_Ao='leClientRouteDescriptorsGroup'
_An='leClientArpGroup'
_Am='leClientMacAddressesGroup'
_Al='leClientAtmAddressesGroup'
_Ak='leClientServerVccGroup'
_Aj='leClientStatisticsGroup'
_Ai='leClientMappingGroup'
_Ah='leClientStatusGroup'
_Ag='leClientConfigGroup'
_Af='leRDArpRowStatus'
_Ae='leRDArpEntryType'
_Ad='leRDArpAtmAddress'
_Ac='leArpRowStatus'
_Ab='leArpEntryType'
_Aa='leArpIsRemoteAddress'
_AZ='leArpAtmAddress'
_AY='lecRouteDescrAtmBinding'
_AX='lecMacAddressAtmBinding'
_AW='lecAtmAddressStatus'
_AV='lecMulticastForwardVci'
_AU='lecMulticastForwardVpi'
_AT='lecMulticastForwardInterface'
_AS='lecMulticastSendVci'
_AR='lecMulticastSendVpi'
_AQ='lecMulticastSendInterface'
_AP='lecControlDistributeVci'
_AO='lecControlDistributeVpi'
_AN='lecControlDistributeInterface'
_AM='lecControlDirectVci'
_AL='lecControlDirectVpi'
_AK='lecControlDirectInterface'
_AJ='lecConfigDirectVci'
_AI='lecConfigDirectVpi'
_AH='lecConfigDirectInterface'
_AG='lecSvcFailures'
_AF='lecControlFramesIn'
_AE='lecControlFramesOut'
_AD='lecArpRepliesIn'
_AC='lecArpRepliesOut'
_AB='lecArpRequestsIn'
_AA='lecArpRequestsOut'
_A9='lecMappingIndex'
_A8='lecProxyClient'
_A7='lecActualLesAtmAddress'
_A6='lecActualLanName'
_A5='lecActualMaxDataFrameSize'
_A4='lecActualLanType'
_A3='lecConfigSource'
_A2='lecConfigServerAtmAddress'
_A1='lecTopologyChange'
_A0='lecVersion'
_z='lecProtocol'
_y='lecLastFailureState'
_x='lecLastFailureRespCode'
_w='lecInterfaceState'
_v='lecPrimaryAtmAddress'
_u='lecIfIndex'
_t='lecConnectionCompleteTimer'
_s='lecMulticastSendPeakRate'
_r='lecMulticastSendAvgRate'
_q='lecMulticastSendType'
_p='lecLocalSegmentID'
_o='lecPathSwitchingDelay'
_n='lecFlushTimeOut'
_m='lecExpectedArpResponseTime'
_l='lecForwardDelayTime'
_k='lecAgingTime'
_j='lecMaxRetryCount'
_i='lecVccTimeoutPeriod'
_h='lecMaxUnknownFrameTime'
_g='lecMaxUnknownFrameCount'
_f='lecControlTimeout'
_e='lecConfigLesAtmAddress'
_d='lecConfigLanName'
_c='lecConfigMaxDataFrameSize'
_b='lecConfigLanType'
_a='lecConfigMode'
_Z='lecOwner'
_Y='lecRowStatus'
_X='leRDArpBridgeNumber'
_W='leRDArpSegmentID'
_V='leArpMacAddress'
_U='lecRouteDescrBridgeNumber'
_T='lecRouteDescrSegmentID'
_S='lecMacAddress'
_R='lecAtmAddress'
_Q='cells per second'
_P='LecDataFrameSize'
_O='LecDataFrameFormat'
_N='OwnerString'
_M='unspecified'
_L='ifIndex'
_K='IF-MIB'
_J='LeArpTableEntryType'
_I='OctetString'
_H='not-accessible'
_G='seconds'
_F='lecIndex'
_E='Integer32'
_D='read-create'
_C='read-only'
_B='LAN-EMULATION-CLIENT-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_I,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ifIndex,=mibBuilder.importSymbols(_K,_L)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress','RowStatus','TextualConvention','TruthValue')
leClientMIB=ModuleIdentity((1,3,6,1,4,1,353,5,3,1))
class OwnerString(DisplayString):0
class AtmLaneAddress(TextualConvention,OctetString):status=_A;subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,0),ValueSizeConstraint(20,20))
class VpiInteger(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
class VciInteger(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
class LeConnectionInterface(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
class LecState(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*(('initialState',1),('lecsConnect',2),('configure',3),('join',4),('initialRegistration',5),('busConnect',6),('operational',7)))
class LecDataFrameFormat(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_M,1),('aflane8023',2),('aflane8025',3)))
class LecDataFrameSize(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_M,1),('max1516',2),('max4544',3),('max9234',4),('max18190',5)))
class LeArpTableEntryType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('other',1),('learnedViaControl',2),('learnedViaData',3),('staticVolatile',4),('staticNonVolatile',5)))
_AtmfLanEmulation_ObjectIdentity=ObjectIdentity
atmfLanEmulation=_AtmfLanEmulation_ObjectIdentity((1,3,6,1,4,1,353,5,3))
_LeClientMIBObjects_ObjectIdentity=ObjectIdentity
leClientMIBObjects=_LeClientMIBObjects_ObjectIdentity((1,3,6,1,4,1,353,5,3,1,1))
_LecConfigTable_Object=MibTable
lecConfigTable=_LecConfigTable_Object((1,3,6,1,4,1,353,5,3,1,1,1))
if mibBuilder.loadTexts:lecConfigTable.setStatus(_A)
_LecConfigEntry_Object=MibTableRow
lecConfigEntry=_LecConfigEntry_Object((1,3,6,1,4,1,353,5,3,1,1,1,1))
lecConfigEntry.setIndexNames((0,_B,_F))
if mibBuilder.loadTexts:lecConfigEntry.setStatus(_A)
class _LecIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_LecIndex_Type.__name__=_E
_LecIndex_Object=MibTableColumn
lecIndex=_LecIndex_Object((1,3,6,1,4,1,353,5,3,1,1,1,1,1),_LecIndex_Type())
lecIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:lecIndex.setStatus(_A)
_LecRowStatus_Type=RowStatus
_LecRowStatus_Object=MibTableColumn
lecRowStatus=_LecRowStatus_Object((1,3,6,1,4,1,353,5,3,1,1,1,1,2),_LecRowStatus_Type())
lecRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:lecRowStatus.setStatus(_A)
class _LecOwner_Type(OwnerString):subtypeSpec=OwnerString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,127))
_LecOwner_Type.__name__=_N
_LecOwner_Object=MibTableColumn
lecOwner=_LecOwner_Object((1,3,6,1,4,1,353,5,3,1,1,1,1,3),_LecOwner_Type())
lecOwner.setMaxAccess(_D)
if mibBuilder.loadTexts:lecOwner.setStatus(_A)
class _LecConfigMode_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('automatic',1),('manual',2)))
_LecConfigMode_Type.__name__=_E
_LecConfigMode_Object=MibTableColumn
lecConfigMode=_LecConfigMode_Object((1,3,6,1,4,1,353,5,3,1,1,1,1,4),_LecConfigMode_Type())
lecConfigMode.setMaxAccess(_D)
if mibBuilder.loadTexts:lecConfigMode.setStatus(_A)
class _LecConfigLanType_Type(LecDataFrameFormat):defaultValue=1
_LecConfigLanType_Type.__name__=_O
_LecConfigLanType_Object=MibTableColumn
lecConfigLanType=_LecConfigLanType_Object((1,3,6,1,4,1,353,5,3,1,1,1,1,5),_LecConfigLanType_Type())
lecConfigLanType.setMaxAccess(_D)
if mibBuilder.loadTexts:lecConfigLanType.setStatus(_A)
class _LecConfigMaxDataFrameSize_Type(LecDataFrameSize):defaultValue=1
_LecConfigMaxDataFrameSize_Type.__name__=_P
_LecConfigMaxDataFrameSize_Object=MibTableColumn
lecConfigMaxDataFrameSize=_LecConfigMaxDataFrameSize_Object((1,3,6,1,4,1,353,5,3,1,1,1,1,6),_LecConfigMaxDataFrameSize_Type())
lecConfigMaxDataFrameSize.setMaxAccess(_D)
if mibBuilder.loadTexts:lecConfigMaxDataFrameSize.setStatus(_A)
class _LecConfigLanName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_LecConfigLanName_Type.__name__=_I
_LecConfigLanName_Object=MibTableColumn
lecConfigLanName=_LecConfigLanName_Object((1,3,6,1,4,1,353,5,3,1,1,1,1,7),_LecConfigLanName_Type())
lecConfigLanName.setMaxAccess(_D)
if mibBuilder.loadTexts:lecConfigLanName.setStatus(_A)
_LecConfigLesAtmAddress_Type=AtmLaneAddress
_LecConfigLesAtmAddress_Object=MibTableColumn
lecConfigLesAtmAddress=_LecConfigLesAtmAddress_Object((1,3,6,1,4,1,353,5,3,1,1,1,1,8),_LecConfigLesAtmAddress_Type())
lecConfigLesAtmAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:lecConfigLesAtmAddress.setStatus(_A)
class _LecControlTimeout_Type(Integer32):defaultValue=120;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(10,300))
_LecControlTimeout_Type.__name__=_E
_LecControlTimeout_Object=MibTableColumn
lecControlTimeout=_LecControlTimeout_Object((1,3,6,1,4,1,353,5,3,1,1,1,1,9),_LecControlTimeout_Type())
lecControlTimeout.setMaxAccess(_D)
if mibBuilder.loadTexts:lecControlTimeout.setStatus(_A)
if mibBuilder.loadTexts:lecControlTimeout.setUnits(_G)
class _LecMaxUnknownFrameCount_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,10))
_LecMaxUnknownFrameCount_Type.__name__=_E
_LecMaxUnknownFrameCount_Object=MibTableColumn
lecMaxUnknownFrameCount=_LecMaxUnknownFrameCount_Object((1,3,6,1,4,1,353,5,3,1,1,1,1,10),_LecMaxUnknownFrameCount_Type())
lecMaxUnknownFrameCount.setMaxAccess(_D)
if mibBuilder.loadTexts:lecMaxUnknownFrameCount.setStatus(_A)
if mibBuilder.loadTexts:lecMaxUnknownFrameCount.setUnits('frames')
class _LecMaxUnknownFrameTime_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,60))
_LecMaxUnknownFrameTime_Type.__name__=_E
_LecMaxUnknownFrameTime_Object=MibTableColumn
lecMaxUnknownFrameTime=_LecMaxUnknownFrameTime_Object((1,3,6,1,4,1,353,5,3,1,1,1,1,11),_LecMaxUnknownFrameTime_Type())
lecMaxUnknownFrameTime.setMaxAccess(_D)
if mibBuilder.loadTexts:lecMaxUnknownFrameTime.setStatus(_A)
if mibBuilder.loadTexts:lecMaxUnknownFrameTime.setUnits(_G)
class _LecVccTimeoutPeriod_Type(Integer32):defaultValue=1200
_LecVccTimeoutPeriod_Type.__name__=_E
_LecVccTimeoutPeriod_Object=MibTableColumn
lecVccTimeoutPeriod=_LecVccTimeoutPeriod_Object((1,3,6,1,4,1,353,5,3,1,1,1,1,12),_LecVccTimeoutPeriod_Type())
lecVccTimeoutPeriod.setMaxAccess(_D)
if mibBuilder.loadTexts:lecVccTimeoutPeriod.setStatus(_A)
if mibBuilder.loadTexts:lecVccTimeoutPeriod.setUnits(_G)
class _LecMaxRetryCount_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2))
_LecMaxRetryCount_Type.__name__=_E
_LecMaxRetryCount_Object=MibTableColumn
lecMaxRetryCount=_LecMaxRetryCount_Object((1,3,6,1,4,1,353,5,3,1,1,1,1,13),_LecMaxRetryCount_Type())
lecMaxRetryCount.setMaxAccess(_D)
if mibBuilder.loadTexts:lecMaxRetryCount.setStatus(_A)
class _LecAgingTime_Type(Integer32):defaultValue=300;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(10,300))
_LecAgingTime_Type.__name__=_E
_LecAgingTime_Object=MibTableColumn
lecAgingTime=_LecAgingTime_Object((1,3,6,1,4,1,353,5,3,1,1,1,1,14),_LecAgingTime_Type())
lecAgingTime.setMaxAccess(_D)
if mibBuilder.loadTexts:lecAgingTime.setStatus(_A)
if mibBuilder.loadTexts:lecAgingTime.setUnits(_G)
class _LecForwardDelayTime_Type(Integer32):defaultValue=15;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(4,30))
_LecForwardDelayTime_Type.__name__=_E
_LecForwardDelayTime_Object=MibTableColumn
lecForwardDelayTime=_LecForwardDelayTime_Object((1,3,6,1,4,1,353,5,3,1,1,1,1,15),_LecForwardDelayTime_Type())
lecForwardDelayTime.setMaxAccess(_D)
if mibBuilder.loadTexts:lecForwardDelayTime.setStatus(_A)
if mibBuilder.loadTexts:lecForwardDelayTime.setUnits(_G)
class _LecExpectedArpResponseTime_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,30))
_LecExpectedArpResponseTime_Type.__name__=_E
_LecExpectedArpResponseTime_Object=MibTableColumn
lecExpectedArpResponseTime=_LecExpectedArpResponseTime_Object((1,3,6,1,4,1,353,5,3,1,1,1,1,16),_LecExpectedArpResponseTime_Type())
lecExpectedArpResponseTime.setMaxAccess(_D)
if mibBuilder.loadTexts:lecExpectedArpResponseTime.setStatus(_A)
if mibBuilder.loadTexts:lecExpectedArpResponseTime.setUnits(_G)
class _LecFlushTimeOut_Type(Integer32):defaultValue=4;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4))
_LecFlushTimeOut_Type.__name__=_E
_LecFlushTimeOut_Object=MibTableColumn
lecFlushTimeOut=_LecFlushTimeOut_Object((1,3,6,1,4,1,353,5,3,1,1,1,1,17),_LecFlushTimeOut_Type())
lecFlushTimeOut.setMaxAccess(_D)
if mibBuilder.loadTexts:lecFlushTimeOut.setStatus(_A)
if mibBuilder.loadTexts:lecFlushTimeOut.setUnits(_G)
class _LecPathSwitchingDelay_Type(Integer32):defaultValue=6;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,8))
_LecPathSwitchingDelay_Type.__name__=_E
_LecPathSwitchingDelay_Object=MibTableColumn
lecPathSwitchingDelay=_LecPathSwitchingDelay_Object((1,3,6,1,4,1,353,5,3,1,1,1,1,18),_LecPathSwitchingDelay_Type())
lecPathSwitchingDelay.setMaxAccess(_D)
if mibBuilder.loadTexts:lecPathSwitchingDelay.setStatus(_A)
if mibBuilder.loadTexts:lecPathSwitchingDelay.setUnits(_G)
class _LecLocalSegmentID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4095))
_LecLocalSegmentID_Type.__name__=_E
_LecLocalSegmentID_Object=MibTableColumn
lecLocalSegmentID=_LecLocalSegmentID_Object((1,3,6,1,4,1,353,5,3,1,1,1,1,19),_LecLocalSegmentID_Type())
lecLocalSegmentID.setMaxAccess(_D)
if mibBuilder.loadTexts:lecLocalSegmentID.setStatus(_A)
class _LecMulticastSendType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('bestEffort',1),('variableBitRate',2),('constantBitRate',3)))
_LecMulticastSendType_Type.__name__=_E
_LecMulticastSendType_Object=MibTableColumn
lecMulticastSendType=_LecMulticastSendType_Object((1,3,6,1,4,1,353,5,3,1,1,1,1,20),_LecMulticastSendType_Type())
lecMulticastSendType.setMaxAccess(_D)
if mibBuilder.loadTexts:lecMulticastSendType.setStatus(_A)
_LecMulticastSendAvgRate_Type=Integer32
_LecMulticastSendAvgRate_Object=MibTableColumn
lecMulticastSendAvgRate=_LecMulticastSendAvgRate_Object((1,3,6,1,4,1,353,5,3,1,1,1,1,21),_LecMulticastSendAvgRate_Type())
lecMulticastSendAvgRate.setMaxAccess(_D)
if mibBuilder.loadTexts:lecMulticastSendAvgRate.setStatus(_A)
if mibBuilder.loadTexts:lecMulticastSendAvgRate.setUnits(_Q)
_LecMulticastSendPeakRate_Type=Integer32
_LecMulticastSendPeakRate_Object=MibTableColumn
lecMulticastSendPeakRate=_LecMulticastSendPeakRate_Object((1,3,6,1,4,1,353,5,3,1,1,1,1,22),_LecMulticastSendPeakRate_Type())
lecMulticastSendPeakRate.setMaxAccess(_D)
if mibBuilder.loadTexts:lecMulticastSendPeakRate.setStatus(_A)
if mibBuilder.loadTexts:lecMulticastSendPeakRate.setUnits(_Q)
class _LecConnectionCompleteTimer_Type(Integer32):defaultValue=4;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,10))
_LecConnectionCompleteTimer_Type.__name__=_E
_LecConnectionCompleteTimer_Object=MibTableColumn
lecConnectionCompleteTimer=_LecConnectionCompleteTimer_Object((1,3,6,1,4,1,353,5,3,1,1,1,1,23),_LecConnectionCompleteTimer_Type())
lecConnectionCompleteTimer.setMaxAccess(_D)
if mibBuilder.loadTexts:lecConnectionCompleteTimer.setStatus(_A)
if mibBuilder.loadTexts:lecConnectionCompleteTimer.setUnits(_G)
_LecStatusTable_Object=MibTable
lecStatusTable=_LecStatusTable_Object((1,3,6,1,4,1,353,5,3,1,1,2))
if mibBuilder.loadTexts:lecStatusTable.setStatus(_A)
_LecStatusEntry_Object=MibTableRow
lecStatusEntry=_LecStatusEntry_Object((1,3,6,1,4,1,353,5,3,1,1,2,1))
lecStatusEntry.setIndexNames((0,_B,_F))
if mibBuilder.loadTexts:lecStatusEntry.setStatus(_A)
_LecIfIndex_Type=Integer32
_LecIfIndex_Object=MibTableColumn
lecIfIndex=_LecIfIndex_Object((1,3,6,1,4,1,353,5,3,1,1,2,1,1),_LecIfIndex_Type())
lecIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:lecIfIndex.setStatus(_A)
_LecPrimaryAtmAddress_Type=AtmLaneAddress
_LecPrimaryAtmAddress_Object=MibTableColumn
lecPrimaryAtmAddress=_LecPrimaryAtmAddress_Object((1,3,6,1,4,1,353,5,3,1,1,2,1,2),_LecPrimaryAtmAddress_Type())
lecPrimaryAtmAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:lecPrimaryAtmAddress.setStatus(_A)
class _LecID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65279))
_LecID_Type.__name__=_E
_LecID_Object=MibTableColumn
lecID=_LecID_Object((1,3,6,1,4,1,353,5,3,1,1,2,1,3),_LecID_Type())
lecID.setMaxAccess(_C)
if mibBuilder.loadTexts:lecID.setStatus(_A)
_LecInterfaceState_Type=LecState
_LecInterfaceState_Object=MibTableColumn
lecInterfaceState=_LecInterfaceState_Object((1,3,6,1,4,1,353,5,3,1,1,2,1,4),_LecInterfaceState_Type())
lecInterfaceState.setMaxAccess(_C)
if mibBuilder.loadTexts:lecInterfaceState.setStatus(_A)
class _LecLastFailureRespCode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15)));namedValues=NamedValues(*(('none',1),('timeout',2),('undefinedError',3),('versionNotSupported',4),('invalidRequestParameters',5),('duplicateLanDestination',6),('duplicateAtmAddress',7),('insufficientResources',8),('accessDenied',9),('invalidRequesterId',10),('invalidLanDestination',11),('invalidAtmAddress',12),('noConfiguration',13),('leConfigureError',14),('insufficientInformation',15)))
_LecLastFailureRespCode_Type.__name__=_E
_LecLastFailureRespCode_Object=MibTableColumn
lecLastFailureRespCode=_LecLastFailureRespCode_Object((1,3,6,1,4,1,353,5,3,1,1,2,1,5),_LecLastFailureRespCode_Type())
lecLastFailureRespCode.setMaxAccess(_C)
if mibBuilder.loadTexts:lecLastFailureRespCode.setStatus(_A)
_LecLastFailureState_Type=LecState
_LecLastFailureState_Object=MibTableColumn
lecLastFailureState=_LecLastFailureState_Object((1,3,6,1,4,1,353,5,3,1,1,2,1,6),_LecLastFailureState_Type())
lecLastFailureState.setMaxAccess(_C)
if mibBuilder.loadTexts:lecLastFailureState.setStatus(_A)
class _LecProtocol_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_LecProtocol_Type.__name__=_E
_LecProtocol_Object=MibTableColumn
lecProtocol=_LecProtocol_Object((1,3,6,1,4,1,353,5,3,1,1,2,1,7),_LecProtocol_Type())
lecProtocol.setMaxAccess(_C)
if mibBuilder.loadTexts:lecProtocol.setStatus(_A)
class _LecVersion_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_LecVersion_Type.__name__=_E
_LecVersion_Object=MibTableColumn
lecVersion=_LecVersion_Object((1,3,6,1,4,1,353,5,3,1,1,2,1,8),_LecVersion_Type())
lecVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:lecVersion.setStatus(_A)
_LecTopologyChange_Type=TruthValue
_LecTopologyChange_Object=MibTableColumn
lecTopologyChange=_LecTopologyChange_Object((1,3,6,1,4,1,353,5,3,1,1,2,1,9),_LecTopologyChange_Type())
lecTopologyChange.setMaxAccess(_C)
if mibBuilder.loadTexts:lecTopologyChange.setStatus(_A)
_LecConfigServerAtmAddress_Type=AtmLaneAddress
_LecConfigServerAtmAddress_Object=MibTableColumn
lecConfigServerAtmAddress=_LecConfigServerAtmAddress_Object((1,3,6,1,4,1,353,5,3,1,1,2,1,10),_LecConfigServerAtmAddress_Type())
lecConfigServerAtmAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:lecConfigServerAtmAddress.setStatus(_A)
class _LecConfigSource_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('gotAddressViaIlmi',1),('usedWellKnownAddress',2),('usedLecsPvc',3),('didNotUseLecs',4)))
_LecConfigSource_Type.__name__=_E
_LecConfigSource_Object=MibTableColumn
lecConfigSource=_LecConfigSource_Object((1,3,6,1,4,1,353,5,3,1,1,2,1,11),_LecConfigSource_Type())
lecConfigSource.setMaxAccess(_C)
if mibBuilder.loadTexts:lecConfigSource.setStatus(_A)
_LecActualLanType_Type=LecDataFrameFormat
_LecActualLanType_Object=MibTableColumn
lecActualLanType=_LecActualLanType_Object((1,3,6,1,4,1,353,5,3,1,1,2,1,12),_LecActualLanType_Type())
lecActualLanType.setMaxAccess(_C)
if mibBuilder.loadTexts:lecActualLanType.setStatus(_A)
_LecActualMaxDataFrameSize_Type=LecDataFrameSize
_LecActualMaxDataFrameSize_Object=MibTableColumn
lecActualMaxDataFrameSize=_LecActualMaxDataFrameSize_Object((1,3,6,1,4,1,353,5,3,1,1,2,1,13),_LecActualMaxDataFrameSize_Type())
lecActualMaxDataFrameSize.setMaxAccess(_C)
if mibBuilder.loadTexts:lecActualMaxDataFrameSize.setStatus(_A)
class _LecActualLanName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_LecActualLanName_Type.__name__=_I
_LecActualLanName_Object=MibTableColumn
lecActualLanName=_LecActualLanName_Object((1,3,6,1,4,1,353,5,3,1,1,2,1,14),_LecActualLanName_Type())
lecActualLanName.setMaxAccess(_C)
if mibBuilder.loadTexts:lecActualLanName.setStatus(_A)
_LecActualLesAtmAddress_Type=AtmLaneAddress
_LecActualLesAtmAddress_Object=MibTableColumn
lecActualLesAtmAddress=_LecActualLesAtmAddress_Object((1,3,6,1,4,1,353,5,3,1,1,2,1,15),_LecActualLesAtmAddress_Type())
lecActualLesAtmAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:lecActualLesAtmAddress.setStatus(_A)
_LecProxyClient_Type=TruthValue
_LecProxyClient_Object=MibTableColumn
lecProxyClient=_LecProxyClient_Object((1,3,6,1,4,1,353,5,3,1,1,2,1,16),_LecProxyClient_Type())
lecProxyClient.setMaxAccess(_C)
if mibBuilder.loadTexts:lecProxyClient.setStatus(_A)
_LecMappingTable_Object=MibTable
lecMappingTable=_LecMappingTable_Object((1,3,6,1,4,1,353,5,3,1,1,3))
if mibBuilder.loadTexts:lecMappingTable.setStatus(_A)
_LecMappingEntry_Object=MibTableRow
lecMappingEntry=_LecMappingEntry_Object((1,3,6,1,4,1,353,5,3,1,1,3,1))
lecMappingEntry.setIndexNames((0,_K,_L))
if mibBuilder.loadTexts:lecMappingEntry.setStatus(_A)
class _LecMappingIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_LecMappingIndex_Type.__name__=_E
_LecMappingIndex_Object=MibTableColumn
lecMappingIndex=_LecMappingIndex_Object((1,3,6,1,4,1,353,5,3,1,1,3,1,1),_LecMappingIndex_Type())
lecMappingIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:lecMappingIndex.setStatus(_A)
_LecStatisticsTable_Object=MibTable
lecStatisticsTable=_LecStatisticsTable_Object((1,3,6,1,4,1,353,5,3,1,1,4))
if mibBuilder.loadTexts:lecStatisticsTable.setStatus(_A)
_LecStatisticsEntry_Object=MibTableRow
lecStatisticsEntry=_LecStatisticsEntry_Object((1,3,6,1,4,1,353,5,3,1,1,4,1))
lecStatisticsEntry.setIndexNames((0,_B,_F))
if mibBuilder.loadTexts:lecStatisticsEntry.setStatus(_A)
_LecArpRequestsOut_Type=Counter32
_LecArpRequestsOut_Object=MibTableColumn
lecArpRequestsOut=_LecArpRequestsOut_Object((1,3,6,1,4,1,353,5,3,1,1,4,1,1),_LecArpRequestsOut_Type())
lecArpRequestsOut.setMaxAccess(_C)
if mibBuilder.loadTexts:lecArpRequestsOut.setStatus(_A)
_LecArpRequestsIn_Type=Counter32
_LecArpRequestsIn_Object=MibTableColumn
lecArpRequestsIn=_LecArpRequestsIn_Object((1,3,6,1,4,1,353,5,3,1,1,4,1,2),_LecArpRequestsIn_Type())
lecArpRequestsIn.setMaxAccess(_C)
if mibBuilder.loadTexts:lecArpRequestsIn.setStatus(_A)
_LecArpRepliesOut_Type=Counter32
_LecArpRepliesOut_Object=MibTableColumn
lecArpRepliesOut=_LecArpRepliesOut_Object((1,3,6,1,4,1,353,5,3,1,1,4,1,3),_LecArpRepliesOut_Type())
lecArpRepliesOut.setMaxAccess(_C)
if mibBuilder.loadTexts:lecArpRepliesOut.setStatus(_A)
_LecArpRepliesIn_Type=Counter32
_LecArpRepliesIn_Object=MibTableColumn
lecArpRepliesIn=_LecArpRepliesIn_Object((1,3,6,1,4,1,353,5,3,1,1,4,1,4),_LecArpRepliesIn_Type())
lecArpRepliesIn.setMaxAccess(_C)
if mibBuilder.loadTexts:lecArpRepliesIn.setStatus(_A)
_LecControlFramesOut_Type=Counter32
_LecControlFramesOut_Object=MibTableColumn
lecControlFramesOut=_LecControlFramesOut_Object((1,3,6,1,4,1,353,5,3,1,1,4,1,5),_LecControlFramesOut_Type())
lecControlFramesOut.setMaxAccess(_C)
if mibBuilder.loadTexts:lecControlFramesOut.setStatus(_A)
_LecControlFramesIn_Type=Counter32
_LecControlFramesIn_Object=MibTableColumn
lecControlFramesIn=_LecControlFramesIn_Object((1,3,6,1,4,1,353,5,3,1,1,4,1,6),_LecControlFramesIn_Type())
lecControlFramesIn.setMaxAccess(_C)
if mibBuilder.loadTexts:lecControlFramesIn.setStatus(_A)
_LecSvcFailures_Type=Counter32
_LecSvcFailures_Object=MibTableColumn
lecSvcFailures=_LecSvcFailures_Object((1,3,6,1,4,1,353,5,3,1,1,4,1,7),_LecSvcFailures_Type())
lecSvcFailures.setMaxAccess(_C)
if mibBuilder.loadTexts:lecSvcFailures.setStatus(_A)
_LecServerVccTable_Object=MibTable
lecServerVccTable=_LecServerVccTable_Object((1,3,6,1,4,1,353,5,3,1,1,5))
if mibBuilder.loadTexts:lecServerVccTable.setStatus(_A)
_LecServerVccEntry_Object=MibTableRow
lecServerVccEntry=_LecServerVccEntry_Object((1,3,6,1,4,1,353,5,3,1,1,5,1))
lecServerVccEntry.setIndexNames((0,_B,_F))
if mibBuilder.loadTexts:lecServerVccEntry.setStatus(_A)
_LecConfigDirectInterface_Type=LeConnectionInterface
_LecConfigDirectInterface_Object=MibTableColumn
lecConfigDirectInterface=_LecConfigDirectInterface_Object((1,3,6,1,4,1,353,5,3,1,1,5,1,1),_LecConfigDirectInterface_Type())
lecConfigDirectInterface.setMaxAccess(_C)
if mibBuilder.loadTexts:lecConfigDirectInterface.setStatus(_A)
_LecConfigDirectVpi_Type=VpiInteger
_LecConfigDirectVpi_Object=MibTableColumn
lecConfigDirectVpi=_LecConfigDirectVpi_Object((1,3,6,1,4,1,353,5,3,1,1,5,1,2),_LecConfigDirectVpi_Type())
lecConfigDirectVpi.setMaxAccess(_C)
if mibBuilder.loadTexts:lecConfigDirectVpi.setStatus(_A)
_LecConfigDirectVci_Type=VciInteger
_LecConfigDirectVci_Object=MibTableColumn
lecConfigDirectVci=_LecConfigDirectVci_Object((1,3,6,1,4,1,353,5,3,1,1,5,1,3),_LecConfigDirectVci_Type())
lecConfigDirectVci.setMaxAccess(_C)
if mibBuilder.loadTexts:lecConfigDirectVci.setStatus(_A)
_LecControlDirectInterface_Type=LeConnectionInterface
_LecControlDirectInterface_Object=MibTableColumn
lecControlDirectInterface=_LecControlDirectInterface_Object((1,3,6,1,4,1,353,5,3,1,1,5,1,4),_LecControlDirectInterface_Type())
lecControlDirectInterface.setMaxAccess(_C)
if mibBuilder.loadTexts:lecControlDirectInterface.setStatus(_A)
_LecControlDirectVpi_Type=VpiInteger
_LecControlDirectVpi_Object=MibTableColumn
lecControlDirectVpi=_LecControlDirectVpi_Object((1,3,6,1,4,1,353,5,3,1,1,5,1,5),_LecControlDirectVpi_Type())
lecControlDirectVpi.setMaxAccess(_C)
if mibBuilder.loadTexts:lecControlDirectVpi.setStatus(_A)
_LecControlDirectVci_Type=VciInteger
_LecControlDirectVci_Object=MibTableColumn
lecControlDirectVci=_LecControlDirectVci_Object((1,3,6,1,4,1,353,5,3,1,1,5,1,6),_LecControlDirectVci_Type())
lecControlDirectVci.setMaxAccess(_C)
if mibBuilder.loadTexts:lecControlDirectVci.setStatus(_A)
_LecControlDistributeInterface_Type=LeConnectionInterface
_LecControlDistributeInterface_Object=MibTableColumn
lecControlDistributeInterface=_LecControlDistributeInterface_Object((1,3,6,1,4,1,353,5,3,1,1,5,1,7),_LecControlDistributeInterface_Type())
lecControlDistributeInterface.setMaxAccess(_C)
if mibBuilder.loadTexts:lecControlDistributeInterface.setStatus(_A)
_LecControlDistributeVpi_Type=VpiInteger
_LecControlDistributeVpi_Object=MibTableColumn
lecControlDistributeVpi=_LecControlDistributeVpi_Object((1,3,6,1,4,1,353,5,3,1,1,5,1,8),_LecControlDistributeVpi_Type())
lecControlDistributeVpi.setMaxAccess(_C)
if mibBuilder.loadTexts:lecControlDistributeVpi.setStatus(_A)
_LecControlDistributeVci_Type=VciInteger
_LecControlDistributeVci_Object=MibTableColumn
lecControlDistributeVci=_LecControlDistributeVci_Object((1,3,6,1,4,1,353,5,3,1,1,5,1,9),_LecControlDistributeVci_Type())
lecControlDistributeVci.setMaxAccess(_C)
if mibBuilder.loadTexts:lecControlDistributeVci.setStatus(_A)
_LecMulticastSendInterface_Type=LeConnectionInterface
_LecMulticastSendInterface_Object=MibTableColumn
lecMulticastSendInterface=_LecMulticastSendInterface_Object((1,3,6,1,4,1,353,5,3,1,1,5,1,10),_LecMulticastSendInterface_Type())
lecMulticastSendInterface.setMaxAccess(_C)
if mibBuilder.loadTexts:lecMulticastSendInterface.setStatus(_A)
_LecMulticastSendVpi_Type=VpiInteger
_LecMulticastSendVpi_Object=MibTableColumn
lecMulticastSendVpi=_LecMulticastSendVpi_Object((1,3,6,1,4,1,353,5,3,1,1,5,1,11),_LecMulticastSendVpi_Type())
lecMulticastSendVpi.setMaxAccess(_C)
if mibBuilder.loadTexts:lecMulticastSendVpi.setStatus(_A)
_LecMulticastSendVci_Type=VciInteger
_LecMulticastSendVci_Object=MibTableColumn
lecMulticastSendVci=_LecMulticastSendVci_Object((1,3,6,1,4,1,353,5,3,1,1,5,1,12),_LecMulticastSendVci_Type())
lecMulticastSendVci.setMaxAccess(_C)
if mibBuilder.loadTexts:lecMulticastSendVci.setStatus(_A)
_LecMulticastForwardInterface_Type=LeConnectionInterface
_LecMulticastForwardInterface_Object=MibTableColumn
lecMulticastForwardInterface=_LecMulticastForwardInterface_Object((1,3,6,1,4,1,353,5,3,1,1,5,1,13),_LecMulticastForwardInterface_Type())
lecMulticastForwardInterface.setMaxAccess(_C)
if mibBuilder.loadTexts:lecMulticastForwardInterface.setStatus(_A)
_LecMulticastForwardVpi_Type=VpiInteger
_LecMulticastForwardVpi_Object=MibTableColumn
lecMulticastForwardVpi=_LecMulticastForwardVpi_Object((1,3,6,1,4,1,353,5,3,1,1,5,1,14),_LecMulticastForwardVpi_Type())
lecMulticastForwardVpi.setMaxAccess(_C)
if mibBuilder.loadTexts:lecMulticastForwardVpi.setStatus(_A)
_LecMulticastForwardVci_Type=VciInteger
_LecMulticastForwardVci_Object=MibTableColumn
lecMulticastForwardVci=_LecMulticastForwardVci_Object((1,3,6,1,4,1,353,5,3,1,1,5,1,15),_LecMulticastForwardVci_Type())
lecMulticastForwardVci.setMaxAccess(_C)
if mibBuilder.loadTexts:lecMulticastForwardVci.setStatus(_A)
_LecAtmAddressTable_Object=MibTable
lecAtmAddressTable=_LecAtmAddressTable_Object((1,3,6,1,4,1,353,5,3,1,1,6))
if mibBuilder.loadTexts:lecAtmAddressTable.setStatus(_A)
_LecAtmAddressEntry_Object=MibTableRow
lecAtmAddressEntry=_LecAtmAddressEntry_Object((1,3,6,1,4,1,353,5,3,1,1,6,1))
lecAtmAddressEntry.setIndexNames((0,_B,_F),(0,_B,_R))
if mibBuilder.loadTexts:lecAtmAddressEntry.setStatus(_A)
_LecAtmAddress_Type=AtmLaneAddress
_LecAtmAddress_Object=MibTableColumn
lecAtmAddress=_LecAtmAddress_Object((1,3,6,1,4,1,353,5,3,1,1,6,1,1),_LecAtmAddress_Type())
lecAtmAddress.setMaxAccess(_H)
if mibBuilder.loadTexts:lecAtmAddress.setStatus(_A)
_LecAtmAddressStatus_Type=RowStatus
_LecAtmAddressStatus_Object=MibTableColumn
lecAtmAddressStatus=_LecAtmAddressStatus_Object((1,3,6,1,4,1,353,5,3,1,1,6,1,2),_LecAtmAddressStatus_Type())
lecAtmAddressStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:lecAtmAddressStatus.setStatus(_A)
_LecMacAddressTable_Object=MibTable
lecMacAddressTable=_LecMacAddressTable_Object((1,3,6,1,4,1,353,5,3,1,1,7))
if mibBuilder.loadTexts:lecMacAddressTable.setStatus(_A)
_LecMacAddressEntry_Object=MibTableRow
lecMacAddressEntry=_LecMacAddressEntry_Object((1,3,6,1,4,1,353,5,3,1,1,7,1))
lecMacAddressEntry.setIndexNames((0,_B,_F),(0,_B,_S))
if mibBuilder.loadTexts:lecMacAddressEntry.setStatus(_A)
_LecMacAddress_Type=MacAddress
_LecMacAddress_Object=MibTableColumn
lecMacAddress=_LecMacAddress_Object((1,3,6,1,4,1,353,5,3,1,1,7,1,1),_LecMacAddress_Type())
lecMacAddress.setMaxAccess(_H)
if mibBuilder.loadTexts:lecMacAddress.setStatus(_A)
_LecMacAddressAtmBinding_Type=AtmLaneAddress
_LecMacAddressAtmBinding_Object=MibTableColumn
lecMacAddressAtmBinding=_LecMacAddressAtmBinding_Object((1,3,6,1,4,1,353,5,3,1,1,7,1,2),_LecMacAddressAtmBinding_Type())
lecMacAddressAtmBinding.setMaxAccess(_C)
if mibBuilder.loadTexts:lecMacAddressAtmBinding.setStatus(_A)
_LecRouteDescrTable_Object=MibTable
lecRouteDescrTable=_LecRouteDescrTable_Object((1,3,6,1,4,1,353,5,3,1,1,8))
if mibBuilder.loadTexts:lecRouteDescrTable.setStatus(_A)
_LecRouteDescrEntry_Object=MibTableRow
lecRouteDescrEntry=_LecRouteDescrEntry_Object((1,3,6,1,4,1,353,5,3,1,1,8,1))
lecRouteDescrEntry.setIndexNames((0,_B,_F),(0,_B,_T),(0,_B,_U))
if mibBuilder.loadTexts:lecRouteDescrEntry.setStatus(_A)
class _LecRouteDescrSegmentID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4095))
_LecRouteDescrSegmentID_Type.__name__=_E
_LecRouteDescrSegmentID_Object=MibTableColumn
lecRouteDescrSegmentID=_LecRouteDescrSegmentID_Object((1,3,6,1,4,1,353,5,3,1,1,8,1,1),_LecRouteDescrSegmentID_Type())
lecRouteDescrSegmentID.setMaxAccess(_H)
if mibBuilder.loadTexts:lecRouteDescrSegmentID.setStatus(_A)
class _LecRouteDescrBridgeNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,15))
_LecRouteDescrBridgeNumber_Type.__name__=_E
_LecRouteDescrBridgeNumber_Object=MibTableColumn
lecRouteDescrBridgeNumber=_LecRouteDescrBridgeNumber_Object((1,3,6,1,4,1,353,5,3,1,1,8,1,2),_LecRouteDescrBridgeNumber_Type())
lecRouteDescrBridgeNumber.setMaxAccess(_H)
if mibBuilder.loadTexts:lecRouteDescrBridgeNumber.setStatus(_A)
_LecRouteDescrAtmBinding_Type=AtmLaneAddress
_LecRouteDescrAtmBinding_Object=MibTableColumn
lecRouteDescrAtmBinding=_LecRouteDescrAtmBinding_Object((1,3,6,1,4,1,353,5,3,1,1,8,1,3),_LecRouteDescrAtmBinding_Type())
lecRouteDescrAtmBinding.setMaxAccess(_C)
if mibBuilder.loadTexts:lecRouteDescrAtmBinding.setStatus(_A)
_LeArpTable_Object=MibTable
leArpTable=_LeArpTable_Object((1,3,6,1,4,1,353,5,3,1,1,9))
if mibBuilder.loadTexts:leArpTable.setStatus(_A)
_LeArpEntry_Object=MibTableRow
leArpEntry=_LeArpEntry_Object((1,3,6,1,4,1,353,5,3,1,1,9,1))
leArpEntry.setIndexNames((0,_B,_F),(0,_B,_V))
if mibBuilder.loadTexts:leArpEntry.setStatus(_A)
_LeArpMacAddress_Type=MacAddress
_LeArpMacAddress_Object=MibTableColumn
leArpMacAddress=_LeArpMacAddress_Object((1,3,6,1,4,1,353,5,3,1,1,9,1,1),_LeArpMacAddress_Type())
leArpMacAddress.setMaxAccess(_H)
if mibBuilder.loadTexts:leArpMacAddress.setStatus(_A)
_LeArpAtmAddress_Type=AtmLaneAddress
_LeArpAtmAddress_Object=MibTableColumn
leArpAtmAddress=_LeArpAtmAddress_Object((1,3,6,1,4,1,353,5,3,1,1,9,1,2),_LeArpAtmAddress_Type())
leArpAtmAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:leArpAtmAddress.setStatus(_A)
_LeArpIsRemoteAddress_Type=TruthValue
_LeArpIsRemoteAddress_Object=MibTableColumn
leArpIsRemoteAddress=_LeArpIsRemoteAddress_Object((1,3,6,1,4,1,353,5,3,1,1,9,1,3),_LeArpIsRemoteAddress_Type())
leArpIsRemoteAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:leArpIsRemoteAddress.setStatus(_A)
class _LeArpEntryType_Type(LeArpTableEntryType):defaultValue=4
_LeArpEntryType_Type.__name__=_J
_LeArpEntryType_Object=MibTableColumn
leArpEntryType=_LeArpEntryType_Object((1,3,6,1,4,1,353,5,3,1,1,9,1,4),_LeArpEntryType_Type())
leArpEntryType.setMaxAccess(_D)
if mibBuilder.loadTexts:leArpEntryType.setStatus(_A)
_LeArpRowStatus_Type=RowStatus
_LeArpRowStatus_Object=MibTableColumn
leArpRowStatus=_LeArpRowStatus_Object((1,3,6,1,4,1,353,5,3,1,1,9,1,5),_LeArpRowStatus_Type())
leArpRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:leArpRowStatus.setStatus(_A)
_LeRDArpTable_Object=MibTable
leRDArpTable=_LeRDArpTable_Object((1,3,6,1,4,1,353,5,3,1,1,10))
if mibBuilder.loadTexts:leRDArpTable.setStatus(_A)
_LeRDArpEntry_Object=MibTableRow
leRDArpEntry=_LeRDArpEntry_Object((1,3,6,1,4,1,353,5,3,1,1,10,1))
leRDArpEntry.setIndexNames((0,_B,_F),(0,_B,_W),(0,_B,_X))
if mibBuilder.loadTexts:leRDArpEntry.setStatus(_A)
class _LeRDArpSegmentID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4095))
_LeRDArpSegmentID_Type.__name__=_E
_LeRDArpSegmentID_Object=MibTableColumn
leRDArpSegmentID=_LeRDArpSegmentID_Object((1,3,6,1,4,1,353,5,3,1,1,10,1,1),_LeRDArpSegmentID_Type())
leRDArpSegmentID.setMaxAccess(_H)
if mibBuilder.loadTexts:leRDArpSegmentID.setStatus(_A)
class _LeRDArpBridgeNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,15))
_LeRDArpBridgeNumber_Type.__name__=_E
_LeRDArpBridgeNumber_Object=MibTableColumn
leRDArpBridgeNumber=_LeRDArpBridgeNumber_Object((1,3,6,1,4,1,353,5,3,1,1,10,1,2),_LeRDArpBridgeNumber_Type())
leRDArpBridgeNumber.setMaxAccess(_H)
if mibBuilder.loadTexts:leRDArpBridgeNumber.setStatus(_A)
_LeRDArpAtmAddress_Type=AtmLaneAddress
_LeRDArpAtmAddress_Object=MibTableColumn
leRDArpAtmAddress=_LeRDArpAtmAddress_Object((1,3,6,1,4,1,353,5,3,1,1,10,1,3),_LeRDArpAtmAddress_Type())
leRDArpAtmAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:leRDArpAtmAddress.setStatus(_A)
class _LeRDArpEntryType_Type(LeArpTableEntryType):defaultValue=4
_LeRDArpEntryType_Type.__name__=_J
_LeRDArpEntryType_Object=MibTableColumn
leRDArpEntryType=_LeRDArpEntryType_Object((1,3,6,1,4,1,353,5,3,1,1,10,1,4),_LeRDArpEntryType_Type())
leRDArpEntryType.setMaxAccess(_D)
if mibBuilder.loadTexts:leRDArpEntryType.setStatus(_A)
_LeRDArpRowStatus_Type=RowStatus
_LeRDArpRowStatus_Object=MibTableColumn
leRDArpRowStatus=_LeRDArpRowStatus_Object((1,3,6,1,4,1,353,5,3,1,1,10,1,5),_LeRDArpRowStatus_Type())
leRDArpRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:leRDArpRowStatus.setStatus(_A)
_LeClientMIBConformance_ObjectIdentity=ObjectIdentity
leClientMIBConformance=_LeClientMIBConformance_ObjectIdentity((1,3,6,1,4,1,353,5,3,1,2))
_LeClientMIBGroups_ObjectIdentity=ObjectIdentity
leClientMIBGroups=_LeClientMIBGroups_ObjectIdentity((1,3,6,1,4,1,353,5,3,1,2,1))
_LeClientMIBCompliances_ObjectIdentity=ObjectIdentity
leClientMIBCompliances=_LeClientMIBCompliances_ObjectIdentity((1,3,6,1,4,1,353,5,3,1,2,2))
leClientConfigGroup=ObjectGroup((1,3,6,1,4,1,353,5,3,1,2,1,1))
leClientConfigGroup.setObjects(*((_B,_Y),(_B,_Z),(_B,_a),(_B,_b),(_B,_c),(_B,_d),(_B,_e),(_B,_f),(_B,_g),(_B,_h),(_B,_i),(_B,_j),(_B,_k),(_B,_l),(_B,_m),(_B,_n),(_B,_o),(_B,_p),(_B,_q),(_B,_r),(_B,_s),(_B,_t)))
if mibBuilder.loadTexts:leClientConfigGroup.setStatus(_A)
leClientStatusGroup=ObjectGroup((1,3,6,1,4,1,353,5,3,1,2,1,2))
leClientStatusGroup.setObjects(*((_B,_u),(_B,_v),(_B,'lecID'),(_B,_w),(_B,_x),(_B,_y),(_B,_z),(_B,_A0),(_B,_A1),(_B,_A2),(_B,_A3),(_B,_A4),(_B,_A5),(_B,_A6),(_B,_A7),(_B,_A8)))
if mibBuilder.loadTexts:leClientStatusGroup.setStatus(_A)
leClientMappingGroup=ObjectGroup((1,3,6,1,4,1,353,5,3,1,2,1,3))
leClientMappingGroup.setObjects((_B,_A9))
if mibBuilder.loadTexts:leClientMappingGroup.setStatus(_A)
leClientStatisticsGroup=ObjectGroup((1,3,6,1,4,1,353,5,3,1,2,1,4))
leClientStatisticsGroup.setObjects(*((_B,_AA),(_B,_AB),(_B,_AC),(_B,_AD),(_B,_AE),(_B,_AF),(_B,_AG)))
if mibBuilder.loadTexts:leClientStatisticsGroup.setStatus(_A)
leClientServerVccGroup=ObjectGroup((1,3,6,1,4,1,353,5,3,1,2,1,5))
leClientServerVccGroup.setObjects(*((_B,_AH),(_B,_AI),(_B,_AJ),(_B,_AK),(_B,_AL),(_B,_AM),(_B,_AN),(_B,_AO),(_B,_AP),(_B,_AQ),(_B,_AR),(_B,_AS),(_B,_AT),(_B,_AU),(_B,_AV)))
if mibBuilder.loadTexts:leClientServerVccGroup.setStatus(_A)
leClientAtmAddressesGroup=ObjectGroup((1,3,6,1,4,1,353,5,3,1,2,1,6))
leClientAtmAddressesGroup.setObjects((_B,_AW))
if mibBuilder.loadTexts:leClientAtmAddressesGroup.setStatus(_A)
leClientMacAddressesGroup=ObjectGroup((1,3,6,1,4,1,353,5,3,1,2,1,7))
leClientMacAddressesGroup.setObjects((_B,_AX))
if mibBuilder.loadTexts:leClientMacAddressesGroup.setStatus(_A)
leClientRouteDescriptorsGroup=ObjectGroup((1,3,6,1,4,1,353,5,3,1,2,1,8))
leClientRouteDescriptorsGroup.setObjects((_B,_AY))
if mibBuilder.loadTexts:leClientRouteDescriptorsGroup.setStatus(_A)
leClientArpGroup=ObjectGroup((1,3,6,1,4,1,353,5,3,1,2,1,9))
leClientArpGroup.setObjects(*((_B,_AZ),(_B,_Aa),(_B,_Ab),(_B,_Ac)))
if mibBuilder.loadTexts:leClientArpGroup.setStatus(_A)
leClientRDArpGroup=ObjectGroup((1,3,6,1,4,1,353,5,3,1,2,1,10))
leClientRDArpGroup.setObjects(*((_B,_Ad),(_B,_Ae),(_B,_Af)))
if mibBuilder.loadTexts:leClientRDArpGroup.setStatus(_A)
leClientMIBCompliance=ModuleCompliance((1,3,6,1,4,1,353,5,3,1,2,2,1))
leClientMIBCompliance.setObjects(*((_B,_Ag),(_B,_Ah),(_B,_Ai),(_B,_Aj),(_B,_Ak),(_B,_Al),(_B,_Am),(_B,_An),(_B,_Ao),(_B,_Ap)))
if mibBuilder.loadTexts:leClientMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{_N:OwnerString,'AtmLaneAddress':AtmLaneAddress,'VpiInteger':VpiInteger,'VciInteger':VciInteger,'LeConnectionInterface':LeConnectionInterface,'LecState':LecState,_O:LecDataFrameFormat,_P:LecDataFrameSize,_J:LeArpTableEntryType,'atmfLanEmulation':atmfLanEmulation,'leClientMIB':leClientMIB,'leClientMIBObjects':leClientMIBObjects,'lecConfigTable':lecConfigTable,'lecConfigEntry':lecConfigEntry,_F:lecIndex,_Y:lecRowStatus,_Z:lecOwner,_a:lecConfigMode,_b:lecConfigLanType,_c:lecConfigMaxDataFrameSize,_d:lecConfigLanName,_e:lecConfigLesAtmAddress,_f:lecControlTimeout,_g:lecMaxUnknownFrameCount,_h:lecMaxUnknownFrameTime,_i:lecVccTimeoutPeriod,_j:lecMaxRetryCount,_k:lecAgingTime,_l:lecForwardDelayTime,_m:lecExpectedArpResponseTime,_n:lecFlushTimeOut,_o:lecPathSwitchingDelay,_p:lecLocalSegmentID,_q:lecMulticastSendType,_r:lecMulticastSendAvgRate,_s:lecMulticastSendPeakRate,_t:lecConnectionCompleteTimer,'lecStatusTable':lecStatusTable,'lecStatusEntry':lecStatusEntry,_u:lecIfIndex,_v:lecPrimaryAtmAddress,'lecID':lecID,_w:lecInterfaceState,_x:lecLastFailureRespCode,_y:lecLastFailureState,_z:lecProtocol,_A0:lecVersion,_A1:lecTopologyChange,_A2:lecConfigServerAtmAddress,_A3:lecConfigSource,_A4:lecActualLanType,_A5:lecActualMaxDataFrameSize,_A6:lecActualLanName,_A7:lecActualLesAtmAddress,_A8:lecProxyClient,'lecMappingTable':lecMappingTable,'lecMappingEntry':lecMappingEntry,_A9:lecMappingIndex,'lecStatisticsTable':lecStatisticsTable,'lecStatisticsEntry':lecStatisticsEntry,_AA:lecArpRequestsOut,_AB:lecArpRequestsIn,_AC:lecArpRepliesOut,_AD:lecArpRepliesIn,_AE:lecControlFramesOut,_AF:lecControlFramesIn,_AG:lecSvcFailures,'lecServerVccTable':lecServerVccTable,'lecServerVccEntry':lecServerVccEntry,_AH:lecConfigDirectInterface,_AI:lecConfigDirectVpi,_AJ:lecConfigDirectVci,_AK:lecControlDirectInterface,_AL:lecControlDirectVpi,_AM:lecControlDirectVci,_AN:lecControlDistributeInterface,_AO:lecControlDistributeVpi,_AP:lecControlDistributeVci,_AQ:lecMulticastSendInterface,_AR:lecMulticastSendVpi,_AS:lecMulticastSendVci,_AT:lecMulticastForwardInterface,_AU:lecMulticastForwardVpi,_AV:lecMulticastForwardVci,'lecAtmAddressTable':lecAtmAddressTable,'lecAtmAddressEntry':lecAtmAddressEntry,_R:lecAtmAddress,_AW:lecAtmAddressStatus,'lecMacAddressTable':lecMacAddressTable,'lecMacAddressEntry':lecMacAddressEntry,_S:lecMacAddress,_AX:lecMacAddressAtmBinding,'lecRouteDescrTable':lecRouteDescrTable,'lecRouteDescrEntry':lecRouteDescrEntry,_T:lecRouteDescrSegmentID,_U:lecRouteDescrBridgeNumber,_AY:lecRouteDescrAtmBinding,'leArpTable':leArpTable,'leArpEntry':leArpEntry,_V:leArpMacAddress,_AZ:leArpAtmAddress,_Aa:leArpIsRemoteAddress,_Ab:leArpEntryType,_Ac:leArpRowStatus,'leRDArpTable':leRDArpTable,'leRDArpEntry':leRDArpEntry,_W:leRDArpSegmentID,_X:leRDArpBridgeNumber,_Ad:leRDArpAtmAddress,_Ae:leRDArpEntryType,_Af:leRDArpRowStatus,'leClientMIBConformance':leClientMIBConformance,'leClientMIBGroups':leClientMIBGroups,_Ag:leClientConfigGroup,_Ah:leClientStatusGroup,_Ai:leClientMappingGroup,_Aj:leClientStatisticsGroup,_Ak:leClientServerVccGroup,_Al:leClientAtmAddressesGroup,_Am:leClientMacAddressesGroup,_Ao:leClientRouteDescriptorsGroup,_An:leClientArpGroup,_Ap:leClientRDArpGroup,'leClientMIBCompliances':leClientMIBCompliances,'leClientMIBCompliance':leClientMIBCompliance})