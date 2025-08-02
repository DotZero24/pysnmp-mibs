_AU='pdnCpIwfPotsPortPacketStatsGroup'
_AT='pdnCpIwfIADConfigGroupV3'
_AS='pdnCpIwfIADConfigGroupV2'
_AR='pdnCpIwfPotsPortStatsGroup'
_AQ='pdnCpIwfPotsPortConfigGroup'
_AP='pdnCpIwfGeneralConfigGroup'
_AO='pdnCpIwfJitterBufferLength'
_AN='pdnPotsTestStatus'
_AM='pdnPotsTestCmd'
_AL='pdnPotsTestType'
_AK='pdnPotsPortActiveSoftswitch'
_AJ='pdnPotsPortLocalEndName'
_AI='pdnPotsPortEchoCanceller'
_AH='pdnPotsPortModemDetected'
_AG='pdnPotsPortCallElapsedTime'
_AF='pdnPotsPortActualVoiceCodec'
_AE='pdnPotsPortSilenceSuppression'
_AD='pdnPotsPortPreferredPacketPeriod'
_AC='pdnPotsPortPreferedVoiceCodec'
_AB='pdnPotsPortG729VoiceCodec'
_AA='pdnPotsPortCustInfo'
_A9='pdnPotsPortOutCallsFailure'
_A8='pdnPotsPortOutCallsConnected'
_A7='pdnPotsPortOutCallsAnswered'
_A6='pdnPotsPortOutCallsAttempted'
_A5='pdnPotsPortInCallsFailure'
_A4='pdnPotsPortInCallsConnected'
_A3='pdnPotsPortInCallsAnswered'
_A2='pdnPotsPortInCallsReceived'
_A1='pdnPotsPortTotalCallsDropped'
_A0='pdnPotsPortTotalCallsFailure'
_z='pdnCpIwfAal2CpsCidErrors'
_y='pdnCpIwfAal2CpsUuiErrors'
_x='pdnCpIwfAal2CpsHecOverlapErrors'
_w='pdnCpIwfAal2CpsReassemblyErrors'
_v='pdnCpIwfAal2CpsOversizeSduErrors'
_u='pdnCpIwfAal2CpsHecErrors'
_t='pdnCpIwfAal2CpsOsfErrors'
_s='pdnCpIwfAal2CpsOsfMismatchErrors'
_r='pdnCpIwfAal2CpsSeqNumErrors'
_q='pdnCpIwfAal2CpsParityErrors'
_p='pdnCpIwfAal2CpsTxPkts'
_o='pdnCpIwfAal2CpsRxPkts'
_n='pdnPotsPortIfIndex'
_m='Milliseconds'
_l='read-create'
_k='not-accessible'
_j='pdnCpIwfIndex'
_i='DisplayString'
_h='pdnCpIwfPotsPortTestGroupV2'
_g='pdnCpIwfPotsPortConfigGroupV2'
_f='pdnCpIwfPotsPortStatsGroupV2'
_e='pdnCpIwfGeneralConfigGroupV2'
_d='pdnPotsPortBytesReceived'
_c='pdnPotsPortBytesSent'
_b='pdnPotsPortPacketsLost'
_a='pdnPotsPortPacketsReceived'
_Z='pdnPotsPortPacketsSent'
_Y='pdnPotsPortTotalCalls'
_X='pdnPotsPortRxGain'
_W='pdnPotsPortTxGain'
_V='pdnPotsPortSignalingMethod'
_U='pdnPotsPortHookStatus'
_T='pdnPotsPortCpIwfIndex'
_S='pdnCpIwfRegion'
_R='pdnCpIwfIndexNext'
_Q='pdnCpIwfTotalNumber'
_P='pdnCpIwfAal2StatsGroup'
_O='pdnCpIwfMappingIndex'
_N='pdnCpIwfSscsPredefinedProfile'
_M='pdnCpIwfAtmBLESCapability'
_L='pdnCpIwfGatewayProtocol'
_K='pdnCpIwfNumPotsAssigned'
_J='pdnCpIwfRowStatus'
_I='pdnCpIwfIfIndex'
_H='deprecated'
_G='ifIndex'
_F='IF-MIB'
_E='read-write'
_D='Integer32'
_C='read-only'
_B='current'
_A='PDN-CP-IWF-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
InterfaceIndex,ifIndex=mibBuilder.importSymbols(_F,'InterfaceIndex',_G)
pdnCpIwf,=mibBuilder.importSymbols('PDN-HEADER-MIB','pdnCpIwf')
SwitchState,=mibBuilder.importSymbols('PDN-TC','SwitchState')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC',_i,'PhysAddress','RowStatus','TextualConvention','TruthValue')
pdnCpIwfMIB=ModuleIdentity((1,3,6,1,4,1,1795,2,24,2,50,1))
if mibBuilder.loadTexts:pdnCpIwfMIB.setRevisions(('2004-12-02 17:00','2004-10-07 11:00','2004-08-30 11:00','2004-07-15 00:00','2004-03-22 00:00'))
class CpIwfRegion(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('usa',1),('canada',2)))
class GatewayProtocol(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('lescas',1),('voiceband',2),('mgcp',3),('sip',4)))
class HookState(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('onhook',1),('offhook',2),('ringground',3)))
class PotsSignaling(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('loopstart',1),('groundstart',2)))
class ControlProtocol(TextualConvention,Bits):status=_B;namedValues=NamedValues(*(('cas',0),('eoc',1),('ccselcp',2)))
class VoiceEncoding(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('g711',0),('g726',1),('g729',2)))
class PdnPotsTestTypes(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('noTest',1),('loopback',2),('ringsignal',3)))
_PdnCpIwfNotifications_ObjectIdentity=ObjectIdentity
pdnCpIwfNotifications=_PdnCpIwfNotifications_ObjectIdentity((1,3,6,1,4,1,1795,2,24,2,50,1,0))
_PdnCpIwfMIBObjects_ObjectIdentity=ObjectIdentity
pdnCpIwfMIBObjects=_PdnCpIwfMIBObjects_ObjectIdentity((1,3,6,1,4,1,1795,2,24,2,50,1,1))
_PdnCpIwfConfigObjects_ObjectIdentity=ObjectIdentity
pdnCpIwfConfigObjects=_PdnCpIwfConfigObjects_ObjectIdentity((1,3,6,1,4,1,1795,2,24,2,50,1,1,1))
class _PdnCpIwfTotalNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_PdnCpIwfTotalNumber_Type.__name__=_D
_PdnCpIwfTotalNumber_Object=MibScalar
pdnCpIwfTotalNumber=_PdnCpIwfTotalNumber_Object((1,3,6,1,4,1,1795,2,24,2,50,1,1,1,1),_PdnCpIwfTotalNumber_Type())
pdnCpIwfTotalNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:pdnCpIwfTotalNumber.setStatus(_B)
class _PdnCpIwfIndexNext_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_PdnCpIwfIndexNext_Type.__name__=_D
_PdnCpIwfIndexNext_Object=MibScalar
pdnCpIwfIndexNext=_PdnCpIwfIndexNext_Object((1,3,6,1,4,1,1795,2,24,2,50,1,1,1,2),_PdnCpIwfIndexNext_Type())
pdnCpIwfIndexNext.setMaxAccess(_C)
if mibBuilder.loadTexts:pdnCpIwfIndexNext.setStatus(_B)
_PdnCpIwfRegion_Type=CpIwfRegion
_PdnCpIwfRegion_Object=MibScalar
pdnCpIwfRegion=_PdnCpIwfRegion_Object((1,3,6,1,4,1,1795,2,24,2,50,1,1,1,3),_PdnCpIwfRegion_Type())
pdnCpIwfRegion.setMaxAccess(_E)
if mibBuilder.loadTexts:pdnCpIwfRegion.setStatus(_B)
_PdnCpIwfTable_Object=MibTable
pdnCpIwfTable=_PdnCpIwfTable_Object((1,3,6,1,4,1,1795,2,24,2,50,1,1,1,4))
if mibBuilder.loadTexts:pdnCpIwfTable.setStatus(_B)
_PdnCpIwfEntry_Object=MibTableRow
pdnCpIwfEntry=_PdnCpIwfEntry_Object((1,3,6,1,4,1,1795,2,24,2,50,1,1,1,4,1))
pdnCpIwfEntry.setIndexNames((0,_A,_j))
if mibBuilder.loadTexts:pdnCpIwfEntry.setStatus(_B)
class _PdnCpIwfIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_PdnCpIwfIndex_Type.__name__=_D
_PdnCpIwfIndex_Object=MibTableColumn
pdnCpIwfIndex=_PdnCpIwfIndex_Object((1,3,6,1,4,1,1795,2,24,2,50,1,1,1,4,1,1),_PdnCpIwfIndex_Type())
pdnCpIwfIndex.setMaxAccess(_k)
if mibBuilder.loadTexts:pdnCpIwfIndex.setStatus(_B)
_PdnCpIwfIfIndex_Type=InterfaceIndex
_PdnCpIwfIfIndex_Object=MibTableColumn
pdnCpIwfIfIndex=_PdnCpIwfIfIndex_Object((1,3,6,1,4,1,1795,2,24,2,50,1,1,1,4,1,2),_PdnCpIwfIfIndex_Type())
pdnCpIwfIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:pdnCpIwfIfIndex.setStatus(_B)
_PdnCpIwfRowStatus_Type=RowStatus
_PdnCpIwfRowStatus_Object=MibTableColumn
pdnCpIwfRowStatus=_PdnCpIwfRowStatus_Object((1,3,6,1,4,1,1795,2,24,2,50,1,1,1,4,1,3),_PdnCpIwfRowStatus_Type())
pdnCpIwfRowStatus.setMaxAccess(_l)
if mibBuilder.loadTexts:pdnCpIwfRowStatus.setStatus(_B)
class _PdnCpIwfNumPotsAssigned_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,24))
_PdnCpIwfNumPotsAssigned_Type.__name__=_D
_PdnCpIwfNumPotsAssigned_Object=MibTableColumn
pdnCpIwfNumPotsAssigned=_PdnCpIwfNumPotsAssigned_Object((1,3,6,1,4,1,1795,2,24,2,50,1,1,1,4,1,4),_PdnCpIwfNumPotsAssigned_Type())
pdnCpIwfNumPotsAssigned.setMaxAccess(_C)
if mibBuilder.loadTexts:pdnCpIwfNumPotsAssigned.setStatus(_B)
_PdnCpIwfGatewayProtocol_Type=GatewayProtocol
_PdnCpIwfGatewayProtocol_Object=MibTableColumn
pdnCpIwfGatewayProtocol=_PdnCpIwfGatewayProtocol_Object((1,3,6,1,4,1,1795,2,24,2,50,1,1,1,4,1,5),_PdnCpIwfGatewayProtocol_Type())
pdnCpIwfGatewayProtocol.setMaxAccess(_l)
if mibBuilder.loadTexts:pdnCpIwfGatewayProtocol.setStatus(_B)
_PdnCpIwfAtmBLESCapability_Type=ControlProtocol
_PdnCpIwfAtmBLESCapability_Object=MibTableColumn
pdnCpIwfAtmBLESCapability=_PdnCpIwfAtmBLESCapability_Object((1,3,6,1,4,1,1795,2,24,2,50,1,1,1,4,1,6),_PdnCpIwfAtmBLESCapability_Type())
pdnCpIwfAtmBLESCapability.setMaxAccess(_C)
if mibBuilder.loadTexts:pdnCpIwfAtmBLESCapability.setStatus(_B)
_PdnCpIwfSscsPredefinedProfile_Type=Integer32
_PdnCpIwfSscsPredefinedProfile_Object=MibTableColumn
pdnCpIwfSscsPredefinedProfile=_PdnCpIwfSscsPredefinedProfile_Object((1,3,6,1,4,1,1795,2,24,2,50,1,1,1,4,1,7),_PdnCpIwfSscsPredefinedProfile_Type())
pdnCpIwfSscsPredefinedProfile.setMaxAccess(_E)
if mibBuilder.loadTexts:pdnCpIwfSscsPredefinedProfile.setStatus(_B)
class _PdnCpIwfJitterBufferLength_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(10,120))
_PdnCpIwfJitterBufferLength_Type.__name__=_D
_PdnCpIwfJitterBufferLength_Object=MibTableColumn
pdnCpIwfJitterBufferLength=_PdnCpIwfJitterBufferLength_Object((1,3,6,1,4,1,1795,2,24,2,50,1,1,1,4,1,8),_PdnCpIwfJitterBufferLength_Type())
pdnCpIwfJitterBufferLength.setMaxAccess(_E)
if mibBuilder.loadTexts:pdnCpIwfJitterBufferLength.setStatus(_B)
if mibBuilder.loadTexts:pdnCpIwfJitterBufferLength.setUnits(_m)
_PdnCpIwfMappingTable_Object=MibTable
pdnCpIwfMappingTable=_PdnCpIwfMappingTable_Object((1,3,6,1,4,1,1795,2,24,2,50,1,1,1,5))
if mibBuilder.loadTexts:pdnCpIwfMappingTable.setStatus(_B)
_PdnCpIwfMappingEntry_Object=MibTableRow
pdnCpIwfMappingEntry=_PdnCpIwfMappingEntry_Object((1,3,6,1,4,1,1795,2,24,2,50,1,1,1,5,1))
pdnCpIwfMappingEntry.setIndexNames((0,_F,_G))
if mibBuilder.loadTexts:pdnCpIwfMappingEntry.setStatus(_B)
class _PdnCpIwfMappingIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_PdnCpIwfMappingIndex_Type.__name__=_D
_PdnCpIwfMappingIndex_Object=MibTableColumn
pdnCpIwfMappingIndex=_PdnCpIwfMappingIndex_Object((1,3,6,1,4,1,1795,2,24,2,50,1,1,1,5,1,1),_PdnCpIwfMappingIndex_Type())
pdnCpIwfMappingIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:pdnCpIwfMappingIndex.setStatus(_B)
_PdnPotsPortTable_Object=MibTable
pdnPotsPortTable=_PdnPotsPortTable_Object((1,3,6,1,4,1,1795,2,24,2,50,1,1,1,6))
if mibBuilder.loadTexts:pdnPotsPortTable.setStatus(_B)
_PdnPotsPortEntry_Object=MibTableRow
pdnPotsPortEntry=_PdnPotsPortEntry_Object((1,3,6,1,4,1,1795,2,24,2,50,1,1,1,6,1))
pdnPotsPortEntry.setIndexNames((0,_A,_n))
if mibBuilder.loadTexts:pdnPotsPortEntry.setStatus(_B)
_PdnPotsPortIfIndex_Type=InterfaceIndex
_PdnPotsPortIfIndex_Object=MibTableColumn
pdnPotsPortIfIndex=_PdnPotsPortIfIndex_Object((1,3,6,1,4,1,1795,2,24,2,50,1,1,1,6,1,1),_PdnPotsPortIfIndex_Type())
pdnPotsPortIfIndex.setMaxAccess(_k)
if mibBuilder.loadTexts:pdnPotsPortIfIndex.setStatus(_B)
class _PdnPotsPortCpIwfIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_PdnPotsPortCpIwfIndex_Type.__name__=_D
_PdnPotsPortCpIwfIndex_Object=MibTableColumn
pdnPotsPortCpIwfIndex=_PdnPotsPortCpIwfIndex_Object((1,3,6,1,4,1,1795,2,24,2,50,1,1,1,6,1,2),_PdnPotsPortCpIwfIndex_Type())
pdnPotsPortCpIwfIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:pdnPotsPortCpIwfIndex.setStatus(_B)
_PdnPotsPortHookStatus_Type=HookState
_PdnPotsPortHookStatus_Object=MibTableColumn
pdnPotsPortHookStatus=_PdnPotsPortHookStatus_Object((1,3,6,1,4,1,1795,2,24,2,50,1,1,1,6,1,3),_PdnPotsPortHookStatus_Type())
pdnPotsPortHookStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:pdnPotsPortHookStatus.setStatus(_B)
_PdnPotsPortSignalingMethod_Type=PotsSignaling
_PdnPotsPortSignalingMethod_Object=MibTableColumn
pdnPotsPortSignalingMethod=_PdnPotsPortSignalingMethod_Object((1,3,6,1,4,1,1795,2,24,2,50,1,1,1,6,1,4),_PdnPotsPortSignalingMethod_Type())
pdnPotsPortSignalingMethod.setMaxAccess(_E)
if mibBuilder.loadTexts:pdnPotsPortSignalingMethod.setStatus(_B)
class _PdnPotsPortTxGain_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-24,23))
_PdnPotsPortTxGain_Type.__name__=_D
_PdnPotsPortTxGain_Object=MibTableColumn
pdnPotsPortTxGain=_PdnPotsPortTxGain_Object((1,3,6,1,4,1,1795,2,24,2,50,1,1,1,6,1,5),_PdnPotsPortTxGain_Type())
pdnPotsPortTxGain.setMaxAccess(_E)
if mibBuilder.loadTexts:pdnPotsPortTxGain.setStatus(_B)
if mibBuilder.loadTexts:pdnPotsPortTxGain.setUnits('dB')
class _PdnPotsPortRxGain_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-24,23))
_PdnPotsPortRxGain_Type.__name__=_D
_PdnPotsPortRxGain_Object=MibTableColumn
pdnPotsPortRxGain=_PdnPotsPortRxGain_Object((1,3,6,1,4,1,1795,2,24,2,50,1,1,1,6,1,6),_PdnPotsPortRxGain_Type())
pdnPotsPortRxGain.setMaxAccess(_E)
if mibBuilder.loadTexts:pdnPotsPortRxGain.setStatus(_B)
if mibBuilder.loadTexts:pdnPotsPortRxGain.setUnits('dB')
_PdnPotsPortCustInfo_Type=DisplayString
_PdnPotsPortCustInfo_Object=MibTableColumn
pdnPotsPortCustInfo=_PdnPotsPortCustInfo_Object((1,3,6,1,4,1,1795,2,24,2,50,1,1,1,6,1,7),_PdnPotsPortCustInfo_Type())
pdnPotsPortCustInfo.setMaxAccess(_E)
if mibBuilder.loadTexts:pdnPotsPortCustInfo.setStatus(_B)
_PdnPotsPortG729VoiceCodec_Type=SwitchState
_PdnPotsPortG729VoiceCodec_Object=MibTableColumn
pdnPotsPortG729VoiceCodec=_PdnPotsPortG729VoiceCodec_Object((1,3,6,1,4,1,1795,2,24,2,50,1,1,1,6,1,8),_PdnPotsPortG729VoiceCodec_Type())
pdnPotsPortG729VoiceCodec.setMaxAccess(_E)
if mibBuilder.loadTexts:pdnPotsPortG729VoiceCodec.setStatus(_B)
_PdnPotsPortPreferedVoiceCodec_Type=VoiceEncoding
_PdnPotsPortPreferedVoiceCodec_Object=MibTableColumn
pdnPotsPortPreferedVoiceCodec=_PdnPotsPortPreferedVoiceCodec_Object((1,3,6,1,4,1,1795,2,24,2,50,1,1,1,6,1,9),_PdnPotsPortPreferedVoiceCodec_Type())
pdnPotsPortPreferedVoiceCodec.setMaxAccess(_E)
if mibBuilder.loadTexts:pdnPotsPortPreferedVoiceCodec.setStatus(_B)
class _PdnPotsPortPreferredPacketPeriod_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_PdnPotsPortPreferredPacketPeriod_Type.__name__=_D
_PdnPotsPortPreferredPacketPeriod_Object=MibTableColumn
pdnPotsPortPreferredPacketPeriod=_PdnPotsPortPreferredPacketPeriod_Object((1,3,6,1,4,1,1795,2,24,2,50,1,1,1,6,1,10),_PdnPotsPortPreferredPacketPeriod_Type())
pdnPotsPortPreferredPacketPeriod.setMaxAccess(_E)
if mibBuilder.loadTexts:pdnPotsPortPreferredPacketPeriod.setStatus(_B)
if mibBuilder.loadTexts:pdnPotsPortPreferredPacketPeriod.setUnits(_m)
_PdnPotsPortSilenceSuppression_Type=SwitchState
_PdnPotsPortSilenceSuppression_Object=MibTableColumn
pdnPotsPortSilenceSuppression=_PdnPotsPortSilenceSuppression_Object((1,3,6,1,4,1,1795,2,24,2,50,1,1,1,6,1,11),_PdnPotsPortSilenceSuppression_Type())
pdnPotsPortSilenceSuppression.setMaxAccess(_E)
if mibBuilder.loadTexts:pdnPotsPortSilenceSuppression.setStatus(_B)
_PdnPotsPortActualVoiceCodec_Type=VoiceEncoding
_PdnPotsPortActualVoiceCodec_Object=MibTableColumn
pdnPotsPortActualVoiceCodec=_PdnPotsPortActualVoiceCodec_Object((1,3,6,1,4,1,1795,2,24,2,50,1,1,1,6,1,12),_PdnPotsPortActualVoiceCodec_Type())
pdnPotsPortActualVoiceCodec.setMaxAccess(_C)
if mibBuilder.loadTexts:pdnPotsPortActualVoiceCodec.setStatus(_B)
class _PdnPotsPortCallElapsedTime_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_PdnPotsPortCallElapsedTime_Type.__name__=_D
_PdnPotsPortCallElapsedTime_Object=MibTableColumn
pdnPotsPortCallElapsedTime=_PdnPotsPortCallElapsedTime_Object((1,3,6,1,4,1,1795,2,24,2,50,1,1,1,6,1,13),_PdnPotsPortCallElapsedTime_Type())
pdnPotsPortCallElapsedTime.setMaxAccess(_C)
if mibBuilder.loadTexts:pdnPotsPortCallElapsedTime.setStatus(_B)
if mibBuilder.loadTexts:pdnPotsPortCallElapsedTime.setUnits('Seconds')
_PdnPotsPortModemDetected_Type=TruthValue
_PdnPotsPortModemDetected_Object=MibTableColumn
pdnPotsPortModemDetected=_PdnPotsPortModemDetected_Object((1,3,6,1,4,1,1795,2,24,2,50,1,1,1,6,1,14),_PdnPotsPortModemDetected_Type())
pdnPotsPortModemDetected.setMaxAccess(_C)
if mibBuilder.loadTexts:pdnPotsPortModemDetected.setStatus(_B)
class _PdnPotsPortEchoCanceller_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('enabled',1),('disabled',2)))
_PdnPotsPortEchoCanceller_Type.__name__=_D
_PdnPotsPortEchoCanceller_Object=MibTableColumn
pdnPotsPortEchoCanceller=_PdnPotsPortEchoCanceller_Object((1,3,6,1,4,1,1795,2,24,2,50,1,1,1,6,1,15),_PdnPotsPortEchoCanceller_Type())
pdnPotsPortEchoCanceller.setMaxAccess(_C)
if mibBuilder.loadTexts:pdnPotsPortEchoCanceller.setStatus(_B)
class _PdnPotsPortLocalEndName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_PdnPotsPortLocalEndName_Type.__name__=_i
_PdnPotsPortLocalEndName_Object=MibTableColumn
pdnPotsPortLocalEndName=_PdnPotsPortLocalEndName_Object((1,3,6,1,4,1,1795,2,24,2,50,1,1,1,6,1,16),_PdnPotsPortLocalEndName_Type())
pdnPotsPortLocalEndName.setMaxAccess(_E)
if mibBuilder.loadTexts:pdnPotsPortLocalEndName.setStatus(_B)
class _PdnPotsPortActiveSoftswitch_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('primary',1),('secondary',2),('none',3)))
_PdnPotsPortActiveSoftswitch_Type.__name__=_D
_PdnPotsPortActiveSoftswitch_Object=MibTableColumn
pdnPotsPortActiveSoftswitch=_PdnPotsPortActiveSoftswitch_Object((1,3,6,1,4,1,1795,2,24,2,50,1,1,1,6,1,17),_PdnPotsPortActiveSoftswitch_Type())
pdnPotsPortActiveSoftswitch.setMaxAccess(_C)
if mibBuilder.loadTexts:pdnPotsPortActiveSoftswitch.setStatus(_B)
_PdnCpIwfTestObjects_ObjectIdentity=ObjectIdentity
pdnCpIwfTestObjects=_PdnCpIwfTestObjects_ObjectIdentity((1,3,6,1,4,1,1795,2,24,2,50,1,1,2))
_PdnPotsTestTable_Object=MibTable
pdnPotsTestTable=_PdnPotsTestTable_Object((1,3,6,1,4,1,1795,2,24,2,50,1,1,2,1))
if mibBuilder.loadTexts:pdnPotsTestTable.setStatus(_B)
_PdnPotsTestEntry_Object=MibTableRow
pdnPotsTestEntry=_PdnPotsTestEntry_Object((1,3,6,1,4,1,1795,2,24,2,50,1,1,2,1,1))
pdnPotsTestEntry.setIndexNames((0,_F,_G))
if mibBuilder.loadTexts:pdnPotsTestEntry.setStatus(_B)
_PdnPotsTestType_Type=PdnPotsTestTypes
_PdnPotsTestType_Object=MibTableColumn
pdnPotsTestType=_PdnPotsTestType_Object((1,3,6,1,4,1,1795,2,24,2,50,1,1,2,1,1,1),_PdnPotsTestType_Type())
pdnPotsTestType.setMaxAccess(_E)
if mibBuilder.loadTexts:pdnPotsTestType.setStatus(_B)
class _PdnPotsTestCmd_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('noOp',1),('start',2),('stop',3),('keepAlive',4)))
_PdnPotsTestCmd_Type.__name__=_D
_PdnPotsTestCmd_Object=MibTableColumn
pdnPotsTestCmd=_PdnPotsTestCmd_Object((1,3,6,1,4,1,1795,2,24,2,50,1,1,2,1,1,2),_PdnPotsTestCmd_Type())
pdnPotsTestCmd.setMaxAccess(_E)
if mibBuilder.loadTexts:pdnPotsTestCmd.setStatus(_B)
class _PdnPotsTestStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('active',1),('inactive',2)))
_PdnPotsTestStatus_Type.__name__=_D
_PdnPotsTestStatus_Object=MibTableColumn
pdnPotsTestStatus=_PdnPotsTestStatus_Object((1,3,6,1,4,1,1795,2,24,2,50,1,1,2,1,1,3),_PdnPotsTestStatus_Type())
pdnPotsTestStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:pdnPotsTestStatus.setStatus(_B)
_PdnCpIwfStatsObjects_ObjectIdentity=ObjectIdentity
pdnCpIwfStatsObjects=_PdnCpIwfStatsObjects_ObjectIdentity((1,3,6,1,4,1,1795,2,24,2,50,1,1,3))
_PdnCpIwfAal2StatsTable_Object=MibTable
pdnCpIwfAal2StatsTable=_PdnCpIwfAal2StatsTable_Object((1,3,6,1,4,1,1795,2,24,2,50,1,1,3,1))
if mibBuilder.loadTexts:pdnCpIwfAal2StatsTable.setStatus(_B)
_PdnCpIwfAal2StatsEntry_Object=MibTableRow
pdnCpIwfAal2StatsEntry=_PdnCpIwfAal2StatsEntry_Object((1,3,6,1,4,1,1795,2,24,2,50,1,1,3,1,1))
pdnCpIwfAal2StatsEntry.setIndexNames((0,_F,_G))
if mibBuilder.loadTexts:pdnCpIwfAal2StatsEntry.setStatus(_B)
_PdnCpIwfAal2CpsRxPkts_Type=Counter32
_PdnCpIwfAal2CpsRxPkts_Object=MibTableColumn
pdnCpIwfAal2CpsRxPkts=_PdnCpIwfAal2CpsRxPkts_Object((1,3,6,1,4,1,1795,2,24,2,50,1,1,3,1,1,1),_PdnCpIwfAal2CpsRxPkts_Type())
pdnCpIwfAal2CpsRxPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:pdnCpIwfAal2CpsRxPkts.setStatus(_B)
_PdnCpIwfAal2CpsTxPkts_Type=Counter32
_PdnCpIwfAal2CpsTxPkts_Object=MibTableColumn
pdnCpIwfAal2CpsTxPkts=_PdnCpIwfAal2CpsTxPkts_Object((1,3,6,1,4,1,1795,2,24,2,50,1,1,3,1,1,2),_PdnCpIwfAal2CpsTxPkts_Type())
pdnCpIwfAal2CpsTxPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:pdnCpIwfAal2CpsTxPkts.setStatus(_B)
_PdnCpIwfAal2CpsParityErrors_Type=Counter32
_PdnCpIwfAal2CpsParityErrors_Object=MibTableColumn
pdnCpIwfAal2CpsParityErrors=_PdnCpIwfAal2CpsParityErrors_Object((1,3,6,1,4,1,1795,2,24,2,50,1,1,3,1,1,3),_PdnCpIwfAal2CpsParityErrors_Type())
pdnCpIwfAal2CpsParityErrors.setMaxAccess(_C)
if mibBuilder.loadTexts:pdnCpIwfAal2CpsParityErrors.setStatus(_B)
_PdnCpIwfAal2CpsSeqNumErrors_Type=Counter32
_PdnCpIwfAal2CpsSeqNumErrors_Object=MibTableColumn
pdnCpIwfAal2CpsSeqNumErrors=_PdnCpIwfAal2CpsSeqNumErrors_Object((1,3,6,1,4,1,1795,2,24,2,50,1,1,3,1,1,4),_PdnCpIwfAal2CpsSeqNumErrors_Type())
pdnCpIwfAal2CpsSeqNumErrors.setMaxAccess(_C)
if mibBuilder.loadTexts:pdnCpIwfAal2CpsSeqNumErrors.setStatus(_B)
_PdnCpIwfAal2CpsOsfMismatchErrors_Type=Counter32
_PdnCpIwfAal2CpsOsfMismatchErrors_Object=MibTableColumn
pdnCpIwfAal2CpsOsfMismatchErrors=_PdnCpIwfAal2CpsOsfMismatchErrors_Object((1,3,6,1,4,1,1795,2,24,2,50,1,1,3,1,1,5),_PdnCpIwfAal2CpsOsfMismatchErrors_Type())
pdnCpIwfAal2CpsOsfMismatchErrors.setMaxAccess(_C)
if mibBuilder.loadTexts:pdnCpIwfAal2CpsOsfMismatchErrors.setStatus(_B)
_PdnCpIwfAal2CpsOsfErrors_Type=Counter32
_PdnCpIwfAal2CpsOsfErrors_Object=MibTableColumn
pdnCpIwfAal2CpsOsfErrors=_PdnCpIwfAal2CpsOsfErrors_Object((1,3,6,1,4,1,1795,2,24,2,50,1,1,3,1,1,6),_PdnCpIwfAal2CpsOsfErrors_Type())
pdnCpIwfAal2CpsOsfErrors.setMaxAccess(_C)
if mibBuilder.loadTexts:pdnCpIwfAal2CpsOsfErrors.setStatus(_B)
_PdnCpIwfAal2CpsHecErrors_Type=Counter32
_PdnCpIwfAal2CpsHecErrors_Object=MibTableColumn
pdnCpIwfAal2CpsHecErrors=_PdnCpIwfAal2CpsHecErrors_Object((1,3,6,1,4,1,1795,2,24,2,50,1,1,3,1,1,7),_PdnCpIwfAal2CpsHecErrors_Type())
pdnCpIwfAal2CpsHecErrors.setMaxAccess(_C)
if mibBuilder.loadTexts:pdnCpIwfAal2CpsHecErrors.setStatus(_B)
_PdnCpIwfAal2CpsOversizeSduErrors_Type=Counter32
_PdnCpIwfAal2CpsOversizeSduErrors_Object=MibTableColumn
pdnCpIwfAal2CpsOversizeSduErrors=_PdnCpIwfAal2CpsOversizeSduErrors_Object((1,3,6,1,4,1,1795,2,24,2,50,1,1,3,1,1,8),_PdnCpIwfAal2CpsOversizeSduErrors_Type())
pdnCpIwfAal2CpsOversizeSduErrors.setMaxAccess(_C)
if mibBuilder.loadTexts:pdnCpIwfAal2CpsOversizeSduErrors.setStatus(_B)
_PdnCpIwfAal2CpsReassemblyErrors_Type=Counter32
_PdnCpIwfAal2CpsReassemblyErrors_Object=MibTableColumn
pdnCpIwfAal2CpsReassemblyErrors=_PdnCpIwfAal2CpsReassemblyErrors_Object((1,3,6,1,4,1,1795,2,24,2,50,1,1,3,1,1,9),_PdnCpIwfAal2CpsReassemblyErrors_Type())
pdnCpIwfAal2CpsReassemblyErrors.setMaxAccess(_C)
if mibBuilder.loadTexts:pdnCpIwfAal2CpsReassemblyErrors.setStatus(_B)
_PdnCpIwfAal2CpsHecOverlapErrors_Type=Counter32
_PdnCpIwfAal2CpsHecOverlapErrors_Object=MibTableColumn
pdnCpIwfAal2CpsHecOverlapErrors=_PdnCpIwfAal2CpsHecOverlapErrors_Object((1,3,6,1,4,1,1795,2,24,2,50,1,1,3,1,1,10),_PdnCpIwfAal2CpsHecOverlapErrors_Type())
pdnCpIwfAal2CpsHecOverlapErrors.setMaxAccess(_C)
if mibBuilder.loadTexts:pdnCpIwfAal2CpsHecOverlapErrors.setStatus(_B)
_PdnCpIwfAal2CpsUuiErrors_Type=Counter32
_PdnCpIwfAal2CpsUuiErrors_Object=MibTableColumn
pdnCpIwfAal2CpsUuiErrors=_PdnCpIwfAal2CpsUuiErrors_Object((1,3,6,1,4,1,1795,2,24,2,50,1,1,3,1,1,11),_PdnCpIwfAal2CpsUuiErrors_Type())
pdnCpIwfAal2CpsUuiErrors.setMaxAccess(_C)
if mibBuilder.loadTexts:pdnCpIwfAal2CpsUuiErrors.setStatus(_B)
_PdnCpIwfAal2CpsCidErrors_Type=Counter32
_PdnCpIwfAal2CpsCidErrors_Object=MibTableColumn
pdnCpIwfAal2CpsCidErrors=_PdnCpIwfAal2CpsCidErrors_Object((1,3,6,1,4,1,1795,2,24,2,50,1,1,3,1,1,12),_PdnCpIwfAal2CpsCidErrors_Type())
pdnCpIwfAal2CpsCidErrors.setMaxAccess(_C)
if mibBuilder.loadTexts:pdnCpIwfAal2CpsCidErrors.setStatus(_B)
_PdnPotsPortStatsTable_Object=MibTable
pdnPotsPortStatsTable=_PdnPotsPortStatsTable_Object((1,3,6,1,4,1,1795,2,24,2,50,1,1,3,2))
if mibBuilder.loadTexts:pdnPotsPortStatsTable.setStatus(_B)
_PdnPotsPortStatsEntry_Object=MibTableRow
pdnPotsPortStatsEntry=_PdnPotsPortStatsEntry_Object((1,3,6,1,4,1,1795,2,24,2,50,1,1,3,2,1))
pdnPotsPortStatsEntry.setIndexNames((0,_F,_G))
if mibBuilder.loadTexts:pdnPotsPortStatsEntry.setStatus(_B)
_PdnPotsPortTotalCalls_Type=Counter32
_PdnPotsPortTotalCalls_Object=MibTableColumn
pdnPotsPortTotalCalls=_PdnPotsPortTotalCalls_Object((1,3,6,1,4,1,1795,2,24,2,50,1,1,3,2,1,1),_PdnPotsPortTotalCalls_Type())
pdnPotsPortTotalCalls.setMaxAccess(_C)
if mibBuilder.loadTexts:pdnPotsPortTotalCalls.setStatus(_B)
_PdnPotsPortTotalCallsFailure_Type=Counter32
_PdnPotsPortTotalCallsFailure_Object=MibTableColumn
pdnPotsPortTotalCallsFailure=_PdnPotsPortTotalCallsFailure_Object((1,3,6,1,4,1,1795,2,24,2,50,1,1,3,2,1,2),_PdnPotsPortTotalCallsFailure_Type())
pdnPotsPortTotalCallsFailure.setMaxAccess(_C)
if mibBuilder.loadTexts:pdnPotsPortTotalCallsFailure.setStatus(_B)
_PdnPotsPortTotalCallsDropped_Type=Counter32
_PdnPotsPortTotalCallsDropped_Object=MibTableColumn
pdnPotsPortTotalCallsDropped=_PdnPotsPortTotalCallsDropped_Object((1,3,6,1,4,1,1795,2,24,2,50,1,1,3,2,1,3),_PdnPotsPortTotalCallsDropped_Type())
pdnPotsPortTotalCallsDropped.setMaxAccess(_C)
if mibBuilder.loadTexts:pdnPotsPortTotalCallsDropped.setStatus(_B)
_PdnPotsPortInCallsReceived_Type=Counter32
_PdnPotsPortInCallsReceived_Object=MibTableColumn
pdnPotsPortInCallsReceived=_PdnPotsPortInCallsReceived_Object((1,3,6,1,4,1,1795,2,24,2,50,1,1,3,2,1,4),_PdnPotsPortInCallsReceived_Type())
pdnPotsPortInCallsReceived.setMaxAccess(_C)
if mibBuilder.loadTexts:pdnPotsPortInCallsReceived.setStatus(_B)
_PdnPotsPortInCallsAnswered_Type=Counter32
_PdnPotsPortInCallsAnswered_Object=MibTableColumn
pdnPotsPortInCallsAnswered=_PdnPotsPortInCallsAnswered_Object((1,3,6,1,4,1,1795,2,24,2,50,1,1,3,2,1,5),_PdnPotsPortInCallsAnswered_Type())
pdnPotsPortInCallsAnswered.setMaxAccess(_C)
if mibBuilder.loadTexts:pdnPotsPortInCallsAnswered.setStatus(_B)
_PdnPotsPortInCallsConnected_Type=Counter32
_PdnPotsPortInCallsConnected_Object=MibTableColumn
pdnPotsPortInCallsConnected=_PdnPotsPortInCallsConnected_Object((1,3,6,1,4,1,1795,2,24,2,50,1,1,3,2,1,6),_PdnPotsPortInCallsConnected_Type())
pdnPotsPortInCallsConnected.setMaxAccess(_C)
if mibBuilder.loadTexts:pdnPotsPortInCallsConnected.setStatus(_B)
_PdnPotsPortInCallsFailure_Type=Counter32
_PdnPotsPortInCallsFailure_Object=MibTableColumn
pdnPotsPortInCallsFailure=_PdnPotsPortInCallsFailure_Object((1,3,6,1,4,1,1795,2,24,2,50,1,1,3,2,1,7),_PdnPotsPortInCallsFailure_Type())
pdnPotsPortInCallsFailure.setMaxAccess(_C)
if mibBuilder.loadTexts:pdnPotsPortInCallsFailure.setStatus(_B)
_PdnPotsPortOutCallsAttempted_Type=Counter32
_PdnPotsPortOutCallsAttempted_Object=MibTableColumn
pdnPotsPortOutCallsAttempted=_PdnPotsPortOutCallsAttempted_Object((1,3,6,1,4,1,1795,2,24,2,50,1,1,3,2,1,8),_PdnPotsPortOutCallsAttempted_Type())
pdnPotsPortOutCallsAttempted.setMaxAccess(_C)
if mibBuilder.loadTexts:pdnPotsPortOutCallsAttempted.setStatus(_B)
_PdnPotsPortOutCallsAnswered_Type=Counter32
_PdnPotsPortOutCallsAnswered_Object=MibTableColumn
pdnPotsPortOutCallsAnswered=_PdnPotsPortOutCallsAnswered_Object((1,3,6,1,4,1,1795,2,24,2,50,1,1,3,2,1,9),_PdnPotsPortOutCallsAnswered_Type())
pdnPotsPortOutCallsAnswered.setMaxAccess(_C)
if mibBuilder.loadTexts:pdnPotsPortOutCallsAnswered.setStatus(_B)
_PdnPotsPortOutCallsConnected_Type=Counter32
_PdnPotsPortOutCallsConnected_Object=MibTableColumn
pdnPotsPortOutCallsConnected=_PdnPotsPortOutCallsConnected_Object((1,3,6,1,4,1,1795,2,24,2,50,1,1,3,2,1,10),_PdnPotsPortOutCallsConnected_Type())
pdnPotsPortOutCallsConnected.setMaxAccess(_C)
if mibBuilder.loadTexts:pdnPotsPortOutCallsConnected.setStatus(_B)
_PdnPotsPortOutCallsFailure_Type=Counter32
_PdnPotsPortOutCallsFailure_Object=MibTableColumn
pdnPotsPortOutCallsFailure=_PdnPotsPortOutCallsFailure_Object((1,3,6,1,4,1,1795,2,24,2,50,1,1,3,2,1,11),_PdnPotsPortOutCallsFailure_Type())
pdnPotsPortOutCallsFailure.setMaxAccess(_C)
if mibBuilder.loadTexts:pdnPotsPortOutCallsFailure.setStatus(_B)
_PdnPotsPortPacketsSent_Type=Counter32
_PdnPotsPortPacketsSent_Object=MibTableColumn
pdnPotsPortPacketsSent=_PdnPotsPortPacketsSent_Object((1,3,6,1,4,1,1795,2,24,2,50,1,1,3,2,1,12),_PdnPotsPortPacketsSent_Type())
pdnPotsPortPacketsSent.setMaxAccess(_C)
if mibBuilder.loadTexts:pdnPotsPortPacketsSent.setStatus(_B)
_PdnPotsPortPacketsReceived_Type=Counter32
_PdnPotsPortPacketsReceived_Object=MibTableColumn
pdnPotsPortPacketsReceived=_PdnPotsPortPacketsReceived_Object((1,3,6,1,4,1,1795,2,24,2,50,1,1,3,2,1,13),_PdnPotsPortPacketsReceived_Type())
pdnPotsPortPacketsReceived.setMaxAccess(_C)
if mibBuilder.loadTexts:pdnPotsPortPacketsReceived.setStatus(_B)
_PdnPotsPortPacketsLost_Type=Counter32
_PdnPotsPortPacketsLost_Object=MibTableColumn
pdnPotsPortPacketsLost=_PdnPotsPortPacketsLost_Object((1,3,6,1,4,1,1795,2,24,2,50,1,1,3,2,1,14),_PdnPotsPortPacketsLost_Type())
pdnPotsPortPacketsLost.setMaxAccess(_C)
if mibBuilder.loadTexts:pdnPotsPortPacketsLost.setStatus(_B)
_PdnPotsPortBytesSent_Type=Counter32
_PdnPotsPortBytesSent_Object=MibTableColumn
pdnPotsPortBytesSent=_PdnPotsPortBytesSent_Object((1,3,6,1,4,1,1795,2,24,2,50,1,1,3,2,1,15),_PdnPotsPortBytesSent_Type())
pdnPotsPortBytesSent.setMaxAccess(_C)
if mibBuilder.loadTexts:pdnPotsPortBytesSent.setStatus(_B)
_PdnPotsPortBytesReceived_Type=Counter32
_PdnPotsPortBytesReceived_Object=MibTableColumn
pdnPotsPortBytesReceived=_PdnPotsPortBytesReceived_Object((1,3,6,1,4,1,1795,2,24,2,50,1,1,3,2,1,16),_PdnPotsPortBytesReceived_Type())
pdnPotsPortBytesReceived.setMaxAccess(_C)
if mibBuilder.loadTexts:pdnPotsPortBytesReceived.setStatus(_B)
_PdnCpIwfMIBConformance_ObjectIdentity=ObjectIdentity
pdnCpIwfMIBConformance=_PdnCpIwfMIBConformance_ObjectIdentity((1,3,6,1,4,1,1795,2,24,2,50,1,2))
_PdnCpIwfMIBCompliances_ObjectIdentity=ObjectIdentity
pdnCpIwfMIBCompliances=_PdnCpIwfMIBCompliances_ObjectIdentity((1,3,6,1,4,1,1795,2,24,2,50,1,2,1))
_PdnCpIwfMIBGroups_ObjectIdentity=ObjectIdentity
pdnCpIwfMIBGroups=_PdnCpIwfMIBGroups_ObjectIdentity((1,3,6,1,4,1,1795,2,24,2,50,1,2,2))
pdnCpIwfGeneralConfigGroup=ObjectGroup((1,3,6,1,4,1,1795,2,24,2,50,1,2,2,1))
pdnCpIwfGeneralConfigGroup.setObjects(*((_A,_Q),(_A,_R),(_A,_S),(_A,_I),(_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_N),(_A,_O)))
if mibBuilder.loadTexts:pdnCpIwfGeneralConfigGroup.setStatus(_H)
pdnCpIwfPotsPortConfigGroup=ObjectGroup((1,3,6,1,4,1,1795,2,24,2,50,1,2,2,2))
pdnCpIwfPotsPortConfigGroup.setObjects(*((_A,_T),(_A,_U),(_A,_V),(_A,_W),(_A,_X)))
if mibBuilder.loadTexts:pdnCpIwfPotsPortConfigGroup.setStatus(_H)
pdnCpIwfAal2StatsGroup=ObjectGroup((1,3,6,1,4,1,1795,2,24,2,50,1,2,2,3))
pdnCpIwfAal2StatsGroup.setObjects(*((_A,_o),(_A,_p),(_A,_q),(_A,_r),(_A,_s),(_A,_t),(_A,_u),(_A,_v),(_A,_w),(_A,_x),(_A,_y),(_A,_z)))
if mibBuilder.loadTexts:pdnCpIwfAal2StatsGroup.setStatus(_B)
pdnCpIwfPotsPortStatsGroup=ObjectGroup((1,3,6,1,4,1,1795,2,24,2,50,1,2,2,4))
pdnCpIwfPotsPortStatsGroup.setObjects((_A,_Y))
if mibBuilder.loadTexts:pdnCpIwfPotsPortStatsGroup.setStatus(_H)
pdnCpIwfGeneralConfigGroupV2=ObjectGroup((1,3,6,1,4,1,1795,2,24,2,50,1,2,2,5))
pdnCpIwfGeneralConfigGroupV2.setObjects(*((_A,_Q),(_A,_R),(_A,_S)))
if mibBuilder.loadTexts:pdnCpIwfGeneralConfigGroupV2.setStatus(_B)
pdnCpIwfIADConfigGroupV2=ObjectGroup((1,3,6,1,4,1,1795,2,24,2,50,1,2,2,6))
pdnCpIwfIADConfigGroupV2.setObjects(*((_A,_I),(_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_N),(_A,_O)))
if mibBuilder.loadTexts:pdnCpIwfIADConfigGroupV2.setStatus(_B)
pdnCpIwfPotsPortStatsGroupV2=ObjectGroup((1,3,6,1,4,1,1795,2,24,2,50,1,2,2,7))
pdnCpIwfPotsPortStatsGroupV2.setObjects(*((_A,_Y),(_A,_A0),(_A,_A1),(_A,_A2),(_A,_A3),(_A,_A4),(_A,_A5),(_A,_A6),(_A,_A7),(_A,_A8),(_A,_A9),(_A,_Z),(_A,_a),(_A,_b),(_A,_c),(_A,_d)))
if mibBuilder.loadTexts:pdnCpIwfPotsPortStatsGroupV2.setStatus(_B)
pdnCpIwfPotsPortConfigGroupV2=ObjectGroup((1,3,6,1,4,1,1795,2,24,2,50,1,2,2,8))
pdnCpIwfPotsPortConfigGroupV2.setObjects(*((_A,_T),(_A,_U),(_A,_V),(_A,_W),(_A,_X),(_A,_AA),(_A,_AB),(_A,_AC),(_A,_AD),(_A,_AE),(_A,_AF),(_A,_AG),(_A,_AH),(_A,_AI),(_A,_AJ),(_A,_AK)))
if mibBuilder.loadTexts:pdnCpIwfPotsPortConfigGroupV2.setStatus(_B)
pdnCpIwfPotsPortTestGroupV2=ObjectGroup((1,3,6,1,4,1,1795,2,24,2,50,1,2,2,9))
pdnCpIwfPotsPortTestGroupV2.setObjects(*((_A,_AL),(_A,_AM),(_A,_AN)))
if mibBuilder.loadTexts:pdnCpIwfPotsPortTestGroupV2.setStatus(_B)
pdnCpIwfIADConfigGroupV3=ObjectGroup((1,3,6,1,4,1,1795,2,24,2,50,1,2,2,10))
pdnCpIwfIADConfigGroupV3.setObjects(*((_A,_I),(_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_N),(_A,_AO),(_A,_O)))
if mibBuilder.loadTexts:pdnCpIwfIADConfigGroupV3.setStatus(_B)
pdnCpIwfPotsPortPacketStatsGroup=ObjectGroup((1,3,6,1,4,1,1795,2,24,2,50,1,2,2,11))
pdnCpIwfPotsPortPacketStatsGroup.setObjects(*((_A,_Z),(_A,_a),(_A,_b),(_A,_c),(_A,_d)))
if mibBuilder.loadTexts:pdnCpIwfPotsPortPacketStatsGroup.setStatus(_B)
pdnCpIwfMIBCompliance=ModuleCompliance((1,3,6,1,4,1,1795,2,24,2,50,1,2,1,1))
pdnCpIwfMIBCompliance.setObjects(*((_A,_AP),(_A,_AQ),(_A,_P),(_A,_AR)))
if mibBuilder.loadTexts:pdnCpIwfMIBCompliance.setStatus(_H)
pdnCpIwfMIBComplianceV2=ModuleCompliance((1,3,6,1,4,1,1795,2,24,2,50,1,2,1,2))
pdnCpIwfMIBComplianceV2.setObjects(*((_A,_e),(_A,_AS),(_A,_P),(_A,_f),(_A,_g),(_A,_h)))
if mibBuilder.loadTexts:pdnCpIwfMIBComplianceV2.setStatus(_H)
pdnCpIwfMIBComplianceV3=ModuleCompliance((1,3,6,1,4,1,1795,2,24,2,50,1,2,1,3))
pdnCpIwfMIBComplianceV3.setObjects(*((_A,_e),(_A,_AT),(_A,_P),(_A,_f),(_A,_g),(_A,_h),(_A,_AU)))
if mibBuilder.loadTexts:pdnCpIwfMIBComplianceV3.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'CpIwfRegion':CpIwfRegion,'GatewayProtocol':GatewayProtocol,'HookState':HookState,'PotsSignaling':PotsSignaling,'ControlProtocol':ControlProtocol,'VoiceEncoding':VoiceEncoding,'PdnPotsTestTypes':PdnPotsTestTypes,'pdnCpIwfMIB':pdnCpIwfMIB,'pdnCpIwfNotifications':pdnCpIwfNotifications,'pdnCpIwfMIBObjects':pdnCpIwfMIBObjects,'pdnCpIwfConfigObjects':pdnCpIwfConfigObjects,_Q:pdnCpIwfTotalNumber,_R:pdnCpIwfIndexNext,_S:pdnCpIwfRegion,'pdnCpIwfTable':pdnCpIwfTable,'pdnCpIwfEntry':pdnCpIwfEntry,_j:pdnCpIwfIndex,_I:pdnCpIwfIfIndex,_J:pdnCpIwfRowStatus,_K:pdnCpIwfNumPotsAssigned,_L:pdnCpIwfGatewayProtocol,_M:pdnCpIwfAtmBLESCapability,_N:pdnCpIwfSscsPredefinedProfile,_AO:pdnCpIwfJitterBufferLength,'pdnCpIwfMappingTable':pdnCpIwfMappingTable,'pdnCpIwfMappingEntry':pdnCpIwfMappingEntry,_O:pdnCpIwfMappingIndex,'pdnPotsPortTable':pdnPotsPortTable,'pdnPotsPortEntry':pdnPotsPortEntry,_n:pdnPotsPortIfIndex,_T:pdnPotsPortCpIwfIndex,_U:pdnPotsPortHookStatus,_V:pdnPotsPortSignalingMethod,_W:pdnPotsPortTxGain,_X:pdnPotsPortRxGain,_AA:pdnPotsPortCustInfo,_AB:pdnPotsPortG729VoiceCodec,_AC:pdnPotsPortPreferedVoiceCodec,_AD:pdnPotsPortPreferredPacketPeriod,_AE:pdnPotsPortSilenceSuppression,_AF:pdnPotsPortActualVoiceCodec,_AG:pdnPotsPortCallElapsedTime,_AH:pdnPotsPortModemDetected,_AI:pdnPotsPortEchoCanceller,_AJ:pdnPotsPortLocalEndName,_AK:pdnPotsPortActiveSoftswitch,'pdnCpIwfTestObjects':pdnCpIwfTestObjects,'pdnPotsTestTable':pdnPotsTestTable,'pdnPotsTestEntry':pdnPotsTestEntry,_AL:pdnPotsTestType,_AM:pdnPotsTestCmd,_AN:pdnPotsTestStatus,'pdnCpIwfStatsObjects':pdnCpIwfStatsObjects,'pdnCpIwfAal2StatsTable':pdnCpIwfAal2StatsTable,'pdnCpIwfAal2StatsEntry':pdnCpIwfAal2StatsEntry,_o:pdnCpIwfAal2CpsRxPkts,_p:pdnCpIwfAal2CpsTxPkts,_q:pdnCpIwfAal2CpsParityErrors,_r:pdnCpIwfAal2CpsSeqNumErrors,_s:pdnCpIwfAal2CpsOsfMismatchErrors,_t:pdnCpIwfAal2CpsOsfErrors,_u:pdnCpIwfAal2CpsHecErrors,_v:pdnCpIwfAal2CpsOversizeSduErrors,_w:pdnCpIwfAal2CpsReassemblyErrors,_x:pdnCpIwfAal2CpsHecOverlapErrors,_y:pdnCpIwfAal2CpsUuiErrors,_z:pdnCpIwfAal2CpsCidErrors,'pdnPotsPortStatsTable':pdnPotsPortStatsTable,'pdnPotsPortStatsEntry':pdnPotsPortStatsEntry,_Y:pdnPotsPortTotalCalls,_A0:pdnPotsPortTotalCallsFailure,_A1:pdnPotsPortTotalCallsDropped,_A2:pdnPotsPortInCallsReceived,_A3:pdnPotsPortInCallsAnswered,_A4:pdnPotsPortInCallsConnected,_A5:pdnPotsPortInCallsFailure,_A6:pdnPotsPortOutCallsAttempted,_A7:pdnPotsPortOutCallsAnswered,_A8:pdnPotsPortOutCallsConnected,_A9:pdnPotsPortOutCallsFailure,_Z:pdnPotsPortPacketsSent,_a:pdnPotsPortPacketsReceived,_b:pdnPotsPortPacketsLost,_c:pdnPotsPortBytesSent,_d:pdnPotsPortBytesReceived,'pdnCpIwfMIBConformance':pdnCpIwfMIBConformance,'pdnCpIwfMIBCompliances':pdnCpIwfMIBCompliances,'pdnCpIwfMIBCompliance':pdnCpIwfMIBCompliance,'pdnCpIwfMIBComplianceV2':pdnCpIwfMIBComplianceV2,'pdnCpIwfMIBComplianceV3':pdnCpIwfMIBComplianceV3,'pdnCpIwfMIBGroups':pdnCpIwfMIBGroups,_AP:pdnCpIwfGeneralConfigGroup,_AQ:pdnCpIwfPotsPortConfigGroup,_P:pdnCpIwfAal2StatsGroup,_AR:pdnCpIwfPotsPortStatsGroup,_e:pdnCpIwfGeneralConfigGroupV2,_AS:pdnCpIwfIADConfigGroupV2,_f:pdnCpIwfPotsPortStatsGroupV2,_g:pdnCpIwfPotsPortConfigGroupV2,_h:pdnCpIwfPotsPortTestGroupV2,_AT:pdnCpIwfIADConfigGroupV3,_AU:pdnCpIwfPotsPortPacketStatsGroup})