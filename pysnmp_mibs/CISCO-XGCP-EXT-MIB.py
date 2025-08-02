_AL='cxeCcProfileGroup'
_AK='cxeCallCtrlGroup'
_AJ='cxeCcProfileRowStatus'
_AI='cxeCcProfileCot2Timeout'
_AH='cxeCcProfileCot1Timeout'
_AG='cxeCcProfileRoTimeout'
_AF='cxeCcProfileRgTimeout'
_AE='cxeCcProfileSlTimeout'
_AD='cxeCcProfileDlTimeout'
_AC='cxeCcProfileBzTimeout'
_AB='cxeCcProfileCgTimeout'
_AA='cxeCcProfileRbkTimeout'
_A9='cxeCcProfileRtTimeout'
_A8='cxeCcProfileThistTimeout'
_A7='cxeCcProfileTparTimeout'
_A6='cxeCcProfileTcritTimeout'
_A5='cxeCcProfileTdmaxTimeout'
_A4='cxeCcProfileTdminTimeout'
_A3='cxeCcProfileTdinitTimeout'
_A2='cxeCcProfileTsmaxTimeout'
_A1='cxeCcProfileMwiTimeout'
_A0='cxeCcProfileDnsLookupMax2'
_z='cxeCcProfileRetryMax2'
_y='cxeCcProfileDnsLookupMax1'
_x='cxeCcProfileRetryMax1'
_w='cxeCcProfileXgcpRetryMethod'
_v='cxeCcProfileProtocolIdx'
_u='cxeCcProfileMgcAddress'
_t='cxeCcProfileMgcAddrType'
_s='cxeCcProfileMgcGrpNum'
_r='cxeCcProfileNumVifs'
_q='cxeCcProfileName'
_p='cxeCallCtrlLastFailedMgcAddress'
_o='cxeCallCtrlLastFailedMgcAddrType'
_n='cxeCallCtrlDefaultBearTraffic'
_m='cxeCallCtrlVselDselFselSupport'
_l='cxeCallCtrlT38NsfVendorCode'
_k='cxeCallCtrlT38NsfCountryCode'
_j='cxeCallCtrlT38HsRedundancy'
_i='cxeCallCtrlT38LsRedundancy'
_h='cxeCallCtrlT38FecEnabled'
_g='cxeCallCtrlT38NseRspTimer'
_f='cxeCallCtrlT38Inhibited'
_e='cxeCallCtrlDigitMapOrder'
_d='cxeCallCtrlIgnoreAal2LcoCodec'
_c='cxeCallCtrlRtcpRcvTimer'
_b='cxeCallCtrlNetNseTimer'
_a='cxeCallCtrlTsePayload'
_Z='cxeCallCtrlVoAal2DtmfCodec'
_Y='cxeCallCtrlVoAal2DtmfRelayMode'
_X='cxeCallCtrlVoIpDtmfCodec'
_W='cxeCallCtrlVoIpDtmfRelayMode'
_V='cxeCallCtrlBearerServiceType'
_U='cxeCallCtrlControlServiceType'
_T='cxeCcProfileIndex'
_S='CxeTerminalProviderCode'
_R='DisplayString'
_Q='InetAddressType'
_P='InetAddress'
_O='CXgcpRetryMethod'
_N='CountryCodeITU'
_M='read-only'
_L='milliseconds'
_K='DtmfCodecType'
_J='DtmfRelayMode'
_I='cmgwIndex'
_H='CISCO-MEDIA-GATEWAY-MIB'
_G='TruthValue'
_F='seconds'
_E='read-write'
_D='read-create'
_C='Integer32'
_B='CISCO-XGCP-EXT-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
CCallControlProfileIndex,cmgwIndex=mibBuilder.importSymbols(_H,'CCallControlProfileIndex',_I)
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
CountryCodeITU,=mibBuilder.importSymbols('CISCO-TC',_N)
CXgcpRetryMethod,=mibBuilder.importSymbols('CISCO-XGCP-MIB',_O)
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB',_P,_Q)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC',_R,'PhysAddress','RowStatus','TextualConvention',_G)
ciscoXgcpExtMIB=ModuleIdentity((1,3,6,1,4,1,9,9,325))
if mibBuilder.loadTexts:ciscoXgcpExtMIB.setRevisions(('2003-01-30 00:00',))
class DtmfRelayMode(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8)));namedValues=NamedValues(*(('dtmfRelayDisabled',1),('dtmfRelayCisco',2),('dtmfRelayNse',3),('dtmfRelayOutOfBand',4),('dtmfRelayNteGw',5),('dtmfRelayNteCa',6),('dtmfRelayInband',7),('dtmfRelayType3',8)))
class DtmfCodecType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('dtmfCodecAll',1),('dtmfCodecLowRate',2)))
class CxeTerminalProviderCode(TextualConvention,OctetString):status=_A;subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,0),ValueSizeConstraint(2,2))
_CxgcpExtObjects_ObjectIdentity=ObjectIdentity
cxgcpExtObjects=_CxgcpExtObjects_ObjectIdentity((1,3,6,1,4,1,9,9,325,1))
_CxgcpExtConfig_ObjectIdentity=ObjectIdentity
cxgcpExtConfig=_CxgcpExtConfig_ObjectIdentity((1,3,6,1,4,1,9,9,325,1,1))
_CxeCallCtrlConfigTable_Object=MibTable
cxeCallCtrlConfigTable=_CxeCallCtrlConfigTable_Object((1,3,6,1,4,1,9,9,325,1,1,1))
if mibBuilder.loadTexts:cxeCallCtrlConfigTable.setStatus(_A)
_CxeCallCtrlConfigEntry_Object=MibTableRow
cxeCallCtrlConfigEntry=_CxeCallCtrlConfigEntry_Object((1,3,6,1,4,1,9,9,325,1,1,1,1))
cxeCallCtrlConfigEntry.setIndexNames((0,_H,_I))
if mibBuilder.loadTexts:cxeCallCtrlConfigEntry.setStatus(_A)
class _CxeCallCtrlControlServiceType_Type(Integer32):defaultValue=96;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_CxeCallCtrlControlServiceType_Type.__name__=_C
_CxeCallCtrlControlServiceType_Object=MibTableColumn
cxeCallCtrlControlServiceType=_CxeCallCtrlControlServiceType_Object((1,3,6,1,4,1,9,9,325,1,1,1,1,1),_CxeCallCtrlControlServiceType_Type())
cxeCallCtrlControlServiceType.setMaxAccess(_E)
if mibBuilder.loadTexts:cxeCallCtrlControlServiceType.setStatus(_A)
class _CxeCallCtrlBearerServiceType_Type(Integer32):defaultValue=160;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_CxeCallCtrlBearerServiceType_Type.__name__=_C
_CxeCallCtrlBearerServiceType_Object=MibTableColumn
cxeCallCtrlBearerServiceType=_CxeCallCtrlBearerServiceType_Object((1,3,6,1,4,1,9,9,325,1,1,1,1,2),_CxeCallCtrlBearerServiceType_Type())
cxeCallCtrlBearerServiceType.setMaxAccess(_E)
if mibBuilder.loadTexts:cxeCallCtrlBearerServiceType.setStatus(_A)
class _CxeCallCtrlVoIpDtmfRelayMode_Type(DtmfRelayMode):defaultValue=1
_CxeCallCtrlVoIpDtmfRelayMode_Type.__name__=_J
_CxeCallCtrlVoIpDtmfRelayMode_Object=MibTableColumn
cxeCallCtrlVoIpDtmfRelayMode=_CxeCallCtrlVoIpDtmfRelayMode_Object((1,3,6,1,4,1,9,9,325,1,1,1,1,3),_CxeCallCtrlVoIpDtmfRelayMode_Type())
cxeCallCtrlVoIpDtmfRelayMode.setMaxAccess(_E)
if mibBuilder.loadTexts:cxeCallCtrlVoIpDtmfRelayMode.setStatus(_A)
class _CxeCallCtrlVoIpDtmfCodec_Type(DtmfCodecType):defaultValue=1
_CxeCallCtrlVoIpDtmfCodec_Type.__name__=_K
_CxeCallCtrlVoIpDtmfCodec_Object=MibTableColumn
cxeCallCtrlVoIpDtmfCodec=_CxeCallCtrlVoIpDtmfCodec_Object((1,3,6,1,4,1,9,9,325,1,1,1,1,4),_CxeCallCtrlVoIpDtmfCodec_Type())
cxeCallCtrlVoIpDtmfCodec.setMaxAccess(_E)
if mibBuilder.loadTexts:cxeCallCtrlVoIpDtmfCodec.setStatus(_A)
class _CxeCallCtrlVoAal2DtmfRelayMode_Type(DtmfRelayMode):defaultValue=1
_CxeCallCtrlVoAal2DtmfRelayMode_Type.__name__=_J
_CxeCallCtrlVoAal2DtmfRelayMode_Object=MibTableColumn
cxeCallCtrlVoAal2DtmfRelayMode=_CxeCallCtrlVoAal2DtmfRelayMode_Object((1,3,6,1,4,1,9,9,325,1,1,1,1,5),_CxeCallCtrlVoAal2DtmfRelayMode_Type())
cxeCallCtrlVoAal2DtmfRelayMode.setMaxAccess(_E)
if mibBuilder.loadTexts:cxeCallCtrlVoAal2DtmfRelayMode.setStatus(_A)
class _CxeCallCtrlVoAal2DtmfCodec_Type(DtmfCodecType):defaultValue=1
_CxeCallCtrlVoAal2DtmfCodec_Type.__name__=_K
_CxeCallCtrlVoAal2DtmfCodec_Object=MibTableColumn
cxeCallCtrlVoAal2DtmfCodec=_CxeCallCtrlVoAal2DtmfCodec_Object((1,3,6,1,4,1,9,9,325,1,1,1,1,6),_CxeCallCtrlVoAal2DtmfCodec_Type())
cxeCallCtrlVoAal2DtmfCodec.setMaxAccess(_E)
if mibBuilder.loadTexts:cxeCallCtrlVoAal2DtmfCodec.setStatus(_A)
class _CxeCallCtrlTsePayload_Type(Integer32):defaultValue=100;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,200))
_CxeCallCtrlTsePayload_Type.__name__=_C
_CxeCallCtrlTsePayload_Object=MibTableColumn
cxeCallCtrlTsePayload=_CxeCallCtrlTsePayload_Object((1,3,6,1,4,1,9,9,325,1,1,1,1,7),_CxeCallCtrlTsePayload_Type())
cxeCallCtrlTsePayload.setMaxAccess(_E)
if mibBuilder.loadTexts:cxeCallCtrlTsePayload.setStatus(_A)
class _CxeCallCtrlNetNseTimer_Type(Integer32):defaultValue=1000;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(250,10000))
_CxeCallCtrlNetNseTimer_Type.__name__=_C
_CxeCallCtrlNetNseTimer_Object=MibTableColumn
cxeCallCtrlNetNseTimer=_CxeCallCtrlNetNseTimer_Object((1,3,6,1,4,1,9,9,325,1,1,1,1,8),_CxeCallCtrlNetNseTimer_Type())
cxeCallCtrlNetNseTimer.setMaxAccess(_E)
if mibBuilder.loadTexts:cxeCallCtrlNetNseTimer.setStatus(_A)
if mibBuilder.loadTexts:cxeCallCtrlNetNseTimer.setUnits(_L)
class _CxeCallCtrlRtcpRcvTimer_Type(Integer32):defaultValue=5;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,10))
_CxeCallCtrlRtcpRcvTimer_Type.__name__=_C
_CxeCallCtrlRtcpRcvTimer_Object=MibTableColumn
cxeCallCtrlRtcpRcvTimer=_CxeCallCtrlRtcpRcvTimer_Object((1,3,6,1,4,1,9,9,325,1,1,1,1,9),_CxeCallCtrlRtcpRcvTimer_Type())
cxeCallCtrlRtcpRcvTimer.setMaxAccess(_E)
if mibBuilder.loadTexts:cxeCallCtrlRtcpRcvTimer.setStatus(_A)
if mibBuilder.loadTexts:cxeCallCtrlRtcpRcvTimer.setUnits('times')
class _CxeCallCtrlIgnoreAal2LcoCodec_Type(TruthValue):defaultValue=2
_CxeCallCtrlIgnoreAal2LcoCodec_Type.__name__=_G
_CxeCallCtrlIgnoreAal2LcoCodec_Object=MibTableColumn
cxeCallCtrlIgnoreAal2LcoCodec=_CxeCallCtrlIgnoreAal2LcoCodec_Object((1,3,6,1,4,1,9,9,325,1,1,1,1,10),_CxeCallCtrlIgnoreAal2LcoCodec_Type())
cxeCallCtrlIgnoreAal2LcoCodec.setMaxAccess(_E)
if mibBuilder.loadTexts:cxeCallCtrlIgnoreAal2LcoCodec.setStatus(_A)
class _CxeCallCtrlDigitMapOrder_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('dmOrderShortest',1),('dmOrderOrdered',2)))
_CxeCallCtrlDigitMapOrder_Type.__name__=_C
_CxeCallCtrlDigitMapOrder_Object=MibTableColumn
cxeCallCtrlDigitMapOrder=_CxeCallCtrlDigitMapOrder_Object((1,3,6,1,4,1,9,9,325,1,1,1,1,11),_CxeCallCtrlDigitMapOrder_Type())
cxeCallCtrlDigitMapOrder.setMaxAccess(_E)
if mibBuilder.loadTexts:cxeCallCtrlDigitMapOrder.setStatus(_A)
class _CxeCallCtrlT38Inhibited_Type(TruthValue):defaultValue=2
_CxeCallCtrlT38Inhibited_Type.__name__=_G
_CxeCallCtrlT38Inhibited_Object=MibTableColumn
cxeCallCtrlT38Inhibited=_CxeCallCtrlT38Inhibited_Object((1,3,6,1,4,1,9,9,325,1,1,1,1,12),_CxeCallCtrlT38Inhibited_Type())
cxeCallCtrlT38Inhibited.setMaxAccess(_E)
if mibBuilder.loadTexts:cxeCallCtrlT38Inhibited.setStatus(_A)
class _CxeCallCtrlT38NseRspTimer_Type(Integer32):defaultValue=1000;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(250,10000))
_CxeCallCtrlT38NseRspTimer_Type.__name__=_C
_CxeCallCtrlT38NseRspTimer_Object=MibTableColumn
cxeCallCtrlT38NseRspTimer=_CxeCallCtrlT38NseRspTimer_Object((1,3,6,1,4,1,9,9,325,1,1,1,1,13),_CxeCallCtrlT38NseRspTimer_Type())
cxeCallCtrlT38NseRspTimer.setMaxAccess(_E)
if mibBuilder.loadTexts:cxeCallCtrlT38NseRspTimer.setStatus(_A)
if mibBuilder.loadTexts:cxeCallCtrlT38NseRspTimer.setUnits(_L)
class _CxeCallCtrlT38FecEnabled_Type(TruthValue):defaultValue=1
_CxeCallCtrlT38FecEnabled_Type.__name__=_G
_CxeCallCtrlT38FecEnabled_Object=MibTableColumn
cxeCallCtrlT38FecEnabled=_CxeCallCtrlT38FecEnabled_Object((1,3,6,1,4,1,9,9,325,1,1,1,1,14),_CxeCallCtrlT38FecEnabled_Type())
cxeCallCtrlT38FecEnabled.setMaxAccess(_E)
if mibBuilder.loadTexts:cxeCallCtrlT38FecEnabled.setStatus(_A)
class _CxeCallCtrlT38LsRedundancy_Type(Integer32):defaultValue=5;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,5))
_CxeCallCtrlT38LsRedundancy_Type.__name__=_C
_CxeCallCtrlT38LsRedundancy_Object=MibTableColumn
cxeCallCtrlT38LsRedundancy=_CxeCallCtrlT38LsRedundancy_Object((1,3,6,1,4,1,9,9,325,1,1,1,1,15),_CxeCallCtrlT38LsRedundancy_Type())
cxeCallCtrlT38LsRedundancy.setMaxAccess(_E)
if mibBuilder.loadTexts:cxeCallCtrlT38LsRedundancy.setStatus(_A)
class _CxeCallCtrlT38HsRedundancy_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2))
_CxeCallCtrlT38HsRedundancy_Type.__name__=_C
_CxeCallCtrlT38HsRedundancy_Object=MibTableColumn
cxeCallCtrlT38HsRedundancy=_CxeCallCtrlT38HsRedundancy_Object((1,3,6,1,4,1,9,9,325,1,1,1,1,16),_CxeCallCtrlT38HsRedundancy_Type())
cxeCallCtrlT38HsRedundancy.setMaxAccess(_E)
if mibBuilder.loadTexts:cxeCallCtrlT38HsRedundancy.setStatus(_A)
class _CxeCallCtrlT38NsfCountryCode_Type(CountryCodeITU):defaultValue=173
_CxeCallCtrlT38NsfCountryCode_Type.__name__=_N
_CxeCallCtrlT38NsfCountryCode_Object=MibTableColumn
cxeCallCtrlT38NsfCountryCode=_CxeCallCtrlT38NsfCountryCode_Object((1,3,6,1,4,1,9,9,325,1,1,1,1,17),_CxeCallCtrlT38NsfCountryCode_Type())
cxeCallCtrlT38NsfCountryCode.setMaxAccess(_E)
if mibBuilder.loadTexts:cxeCallCtrlT38NsfCountryCode.setStatus(_A)
class _CxeCallCtrlT38NsfVendorCode_Type(CxeTerminalProviderCode):defaultHexValue='0051'
_CxeCallCtrlT38NsfVendorCode_Type.__name__=_S
_CxeCallCtrlT38NsfVendorCode_Object=MibTableColumn
cxeCallCtrlT38NsfVendorCode=_CxeCallCtrlT38NsfVendorCode_Object((1,3,6,1,4,1,9,9,325,1,1,1,1,18),_CxeCallCtrlT38NsfVendorCode_Type())
cxeCallCtrlT38NsfVendorCode.setMaxAccess(_E)
if mibBuilder.loadTexts:cxeCallCtrlT38NsfVendorCode.setStatus(_A)
class _CxeCallCtrlVselDselFselSupport_Type(TruthValue):defaultValue=2
_CxeCallCtrlVselDselFselSupport_Type.__name__=_G
_CxeCallCtrlVselDselFselSupport_Object=MibTableColumn
cxeCallCtrlVselDselFselSupport=_CxeCallCtrlVselDselFselSupport_Object((1,3,6,1,4,1,9,9,325,1,1,1,1,19),_CxeCallCtrlVselDselFselSupport_Type())
cxeCallCtrlVselDselFselSupport.setMaxAccess(_E)
if mibBuilder.loadTexts:cxeCallCtrlVselDselFselSupport.setStatus(_A)
class _CxeCallCtrlDefaultBearTraffic_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('ipPvcAal5',1),('atmPvcAal2',2),('atmSvcAal2',3),('atmSvcAal1',4)))
_CxeCallCtrlDefaultBearTraffic_Type.__name__=_C
_CxeCallCtrlDefaultBearTraffic_Object=MibTableColumn
cxeCallCtrlDefaultBearTraffic=_CxeCallCtrlDefaultBearTraffic_Object((1,3,6,1,4,1,9,9,325,1,1,1,1,20),_CxeCallCtrlDefaultBearTraffic_Type())
cxeCallCtrlDefaultBearTraffic.setMaxAccess(_E)
if mibBuilder.loadTexts:cxeCallCtrlDefaultBearTraffic.setStatus(_A)
_CxeCallCtrlLastFailedMgcAddrType_Type=InetAddressType
_CxeCallCtrlLastFailedMgcAddrType_Object=MibTableColumn
cxeCallCtrlLastFailedMgcAddrType=_CxeCallCtrlLastFailedMgcAddrType_Object((1,3,6,1,4,1,9,9,325,1,1,1,1,21),_CxeCallCtrlLastFailedMgcAddrType_Type())
cxeCallCtrlLastFailedMgcAddrType.setMaxAccess(_M)
if mibBuilder.loadTexts:cxeCallCtrlLastFailedMgcAddrType.setStatus(_A)
_CxeCallCtrlLastFailedMgcAddress_Type=InetAddress
_CxeCallCtrlLastFailedMgcAddress_Object=MibTableColumn
cxeCallCtrlLastFailedMgcAddress=_CxeCallCtrlLastFailedMgcAddress_Object((1,3,6,1,4,1,9,9,325,1,1,1,1,22),_CxeCallCtrlLastFailedMgcAddress_Type())
cxeCallCtrlLastFailedMgcAddress.setMaxAccess(_M)
if mibBuilder.loadTexts:cxeCallCtrlLastFailedMgcAddress.setStatus(_A)
_CxeCallCtrlProfileTable_Object=MibTable
cxeCallCtrlProfileTable=_CxeCallCtrlProfileTable_Object((1,3,6,1,4,1,9,9,325,1,1,2))
if mibBuilder.loadTexts:cxeCallCtrlProfileTable.setStatus(_A)
_CxeCallCtrlProfileEntry_Object=MibTableRow
cxeCallCtrlProfileEntry=_CxeCallCtrlProfileEntry_Object((1,3,6,1,4,1,9,9,325,1,1,2,1))
cxeCallCtrlProfileEntry.setIndexNames((0,_H,_I),(0,_B,_T))
if mibBuilder.loadTexts:cxeCallCtrlProfileEntry.setStatus(_A)
_CxeCcProfileIndex_Type=CCallControlProfileIndex
_CxeCcProfileIndex_Object=MibTableColumn
cxeCcProfileIndex=_CxeCcProfileIndex_Object((1,3,6,1,4,1,9,9,325,1,1,2,1,1),_CxeCcProfileIndex_Type())
cxeCcProfileIndex.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:cxeCcProfileIndex.setStatus(_A)
class _CxeCcProfileName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,64))
_CxeCcProfileName_Type.__name__=_R
_CxeCcProfileName_Object=MibTableColumn
cxeCcProfileName=_CxeCcProfileName_Object((1,3,6,1,4,1,9,9,325,1,1,2,1,2),_CxeCcProfileName_Type())
cxeCcProfileName.setMaxAccess(_D)
if mibBuilder.loadTexts:cxeCcProfileName.setStatus(_A)
class _CxeCcProfileNumVifs_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1000))
_CxeCcProfileNumVifs_Type.__name__=_C
_CxeCcProfileNumVifs_Object=MibTableColumn
cxeCcProfileNumVifs=_CxeCcProfileNumVifs_Object((1,3,6,1,4,1,9,9,325,1,1,2,1,3),_CxeCcProfileNumVifs_Type())
cxeCcProfileNumVifs.setMaxAccess(_M)
if mibBuilder.loadTexts:cxeCcProfileNumVifs.setStatus(_A)
class _CxeCcProfileMgcGrpNum_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_CxeCcProfileMgcGrpNum_Type.__name__=_C
_CxeCcProfileMgcGrpNum_Object=MibTableColumn
cxeCcProfileMgcGrpNum=_CxeCcProfileMgcGrpNum_Object((1,3,6,1,4,1,9,9,325,1,1,2,1,4),_CxeCcProfileMgcGrpNum_Type())
cxeCcProfileMgcGrpNum.setMaxAccess(_D)
if mibBuilder.loadTexts:cxeCcProfileMgcGrpNum.setStatus(_A)
class _CxeCcProfileMgcAddrType_Type(InetAddressType):defaultValue=1
_CxeCcProfileMgcAddrType_Type.__name__=_Q
_CxeCcProfileMgcAddrType_Object=MibTableColumn
cxeCcProfileMgcAddrType=_CxeCcProfileMgcAddrType_Object((1,3,6,1,4,1,9,9,325,1,1,2,1,5),_CxeCcProfileMgcAddrType_Type())
cxeCcProfileMgcAddrType.setMaxAccess(_D)
if mibBuilder.loadTexts:cxeCcProfileMgcAddrType.setStatus(_A)
class _CxeCcProfileMgcAddress_Type(InetAddress):defaultHexValue='00000000'
_CxeCcProfileMgcAddress_Type.__name__=_P
_CxeCcProfileMgcAddress_Object=MibTableColumn
cxeCcProfileMgcAddress=_CxeCcProfileMgcAddress_Object((1,3,6,1,4,1,9,9,325,1,1,2,1,6),_CxeCcProfileMgcAddress_Type())
cxeCcProfileMgcAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:cxeCcProfileMgcAddress.setStatus(_A)
class _CxeCcProfileProtocolIdx_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,32))
_CxeCcProfileProtocolIdx_Type.__name__=_C
_CxeCcProfileProtocolIdx_Object=MibTableColumn
cxeCcProfileProtocolIdx=_CxeCcProfileProtocolIdx_Object((1,3,6,1,4,1,9,9,325,1,1,2,1,7),_CxeCcProfileProtocolIdx_Type())
cxeCcProfileProtocolIdx.setMaxAccess(_D)
if mibBuilder.loadTexts:cxeCcProfileProtocolIdx.setStatus(_A)
class _CxeCcProfileXgcpRetryMethod_Type(CXgcpRetryMethod):defaultValue=1
_CxeCcProfileXgcpRetryMethod_Type.__name__=_O
_CxeCcProfileXgcpRetryMethod_Object=MibTableColumn
cxeCcProfileXgcpRetryMethod=_CxeCcProfileXgcpRetryMethod_Object((1,3,6,1,4,1,9,9,325,1,1,2,1,8),_CxeCcProfileXgcpRetryMethod_Type())
cxeCcProfileXgcpRetryMethod.setMaxAccess(_D)
if mibBuilder.loadTexts:cxeCcProfileXgcpRetryMethod.setStatus(_A)
class _CxeCcProfileRetryMax1_Type(Integer32):defaultValue=5;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,20))
_CxeCcProfileRetryMax1_Type.__name__=_C
_CxeCcProfileRetryMax1_Object=MibTableColumn
cxeCcProfileRetryMax1=_CxeCcProfileRetryMax1_Object((1,3,6,1,4,1,9,9,325,1,1,2,1,9),_CxeCcProfileRetryMax1_Type())
cxeCcProfileRetryMax1.setMaxAccess(_D)
if mibBuilder.loadTexts:cxeCcProfileRetryMax1.setStatus(_A)
class _CxeCcProfileDnsLookupMax1_Type(TruthValue):defaultValue=1
_CxeCcProfileDnsLookupMax1_Type.__name__=_G
_CxeCcProfileDnsLookupMax1_Object=MibTableColumn
cxeCcProfileDnsLookupMax1=_CxeCcProfileDnsLookupMax1_Object((1,3,6,1,4,1,9,9,325,1,1,2,1,10),_CxeCcProfileDnsLookupMax1_Type())
cxeCcProfileDnsLookupMax1.setMaxAccess(_D)
if mibBuilder.loadTexts:cxeCcProfileDnsLookupMax1.setStatus(_A)
class _CxeCcProfileRetryMax2_Type(Integer32):defaultValue=7;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,20))
_CxeCcProfileRetryMax2_Type.__name__=_C
_CxeCcProfileRetryMax2_Object=MibTableColumn
cxeCcProfileRetryMax2=_CxeCcProfileRetryMax2_Object((1,3,6,1,4,1,9,9,325,1,1,2,1,11),_CxeCcProfileRetryMax2_Type())
cxeCcProfileRetryMax2.setMaxAccess(_D)
if mibBuilder.loadTexts:cxeCcProfileRetryMax2.setStatus(_A)
class _CxeCcProfileDnsLookupMax2_Type(TruthValue):defaultValue=1
_CxeCcProfileDnsLookupMax2_Type.__name__=_G
_CxeCcProfileDnsLookupMax2_Object=MibTableColumn
cxeCcProfileDnsLookupMax2=_CxeCcProfileDnsLookupMax2_Object((1,3,6,1,4,1,9,9,325,1,1,2,1,12),_CxeCcProfileDnsLookupMax2_Type())
cxeCcProfileDnsLookupMax2.setMaxAccess(_D)
if mibBuilder.loadTexts:cxeCcProfileDnsLookupMax2.setStatus(_A)
class _CxeCcProfileMwiTimeout_Type(Integer32):defaultValue=16;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,50))
_CxeCcProfileMwiTimeout_Type.__name__=_C
_CxeCcProfileMwiTimeout_Object=MibTableColumn
cxeCcProfileMwiTimeout=_CxeCcProfileMwiTimeout_Object((1,3,6,1,4,1,9,9,325,1,1,2,1,13),_CxeCcProfileMwiTimeout_Type())
cxeCcProfileMwiTimeout.setMaxAccess(_D)
if mibBuilder.loadTexts:cxeCcProfileMwiTimeout.setStatus(_A)
if mibBuilder.loadTexts:cxeCcProfileMwiTimeout.setUnits(_L)
class _CxeCcProfileTsmaxTimeout_Type(Integer32):defaultValue=20;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1000))
_CxeCcProfileTsmaxTimeout_Type.__name__=_C
_CxeCcProfileTsmaxTimeout_Object=MibTableColumn
cxeCcProfileTsmaxTimeout=_CxeCcProfileTsmaxTimeout_Object((1,3,6,1,4,1,9,9,325,1,1,2,1,14),_CxeCcProfileTsmaxTimeout_Type())
cxeCcProfileTsmaxTimeout.setMaxAccess(_D)
if mibBuilder.loadTexts:cxeCcProfileTsmaxTimeout.setStatus(_A)
if mibBuilder.loadTexts:cxeCcProfileTsmaxTimeout.setUnits(_F)
class _CxeCcProfileTdinitTimeout_Type(Integer32):defaultValue=15;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,100))
_CxeCcProfileTdinitTimeout_Type.__name__=_C
_CxeCcProfileTdinitTimeout_Object=MibTableColumn
cxeCcProfileTdinitTimeout=_CxeCcProfileTdinitTimeout_Object((1,3,6,1,4,1,9,9,325,1,1,2,1,15),_CxeCcProfileTdinitTimeout_Type())
cxeCcProfileTdinitTimeout.setMaxAccess(_D)
if mibBuilder.loadTexts:cxeCcProfileTdinitTimeout.setStatus(_A)
if mibBuilder.loadTexts:cxeCcProfileTdinitTimeout.setUnits(_F)
class _CxeCcProfileTdminTimeout_Type(Integer32):defaultValue=15;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,100))
_CxeCcProfileTdminTimeout_Type.__name__=_C
_CxeCcProfileTdminTimeout_Object=MibTableColumn
cxeCcProfileTdminTimeout=_CxeCcProfileTdminTimeout_Object((1,3,6,1,4,1,9,9,325,1,1,2,1,17),_CxeCcProfileTdminTimeout_Type())
cxeCcProfileTdminTimeout.setMaxAccess(_D)
if mibBuilder.loadTexts:cxeCcProfileTdminTimeout.setStatus(_A)
if mibBuilder.loadTexts:cxeCcProfileTdminTimeout.setUnits(_F)
class _CxeCcProfileTdmaxTimeout_Type(Integer32):defaultValue=600;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1000))
_CxeCcProfileTdmaxTimeout_Type.__name__=_C
_CxeCcProfileTdmaxTimeout_Object=MibTableColumn
cxeCcProfileTdmaxTimeout=_CxeCcProfileTdmaxTimeout_Object((1,3,6,1,4,1,9,9,325,1,1,2,1,18),_CxeCcProfileTdmaxTimeout_Type())
cxeCcProfileTdmaxTimeout.setMaxAccess(_D)
if mibBuilder.loadTexts:cxeCcProfileTdmaxTimeout.setStatus(_A)
if mibBuilder.loadTexts:cxeCcProfileTdmaxTimeout.setUnits(_F)
class _CxeCcProfileTcritTimeout_Type(Integer32):defaultValue=4;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1000))
_CxeCcProfileTcritTimeout_Type.__name__=_C
_CxeCcProfileTcritTimeout_Object=MibTableColumn
cxeCcProfileTcritTimeout=_CxeCcProfileTcritTimeout_Object((1,3,6,1,4,1,9,9,325,1,1,2,1,19),_CxeCcProfileTcritTimeout_Type())
cxeCcProfileTcritTimeout.setMaxAccess(_D)
if mibBuilder.loadTexts:cxeCcProfileTcritTimeout.setStatus(_A)
if mibBuilder.loadTexts:cxeCcProfileTcritTimeout.setUnits(_F)
class _CxeCcProfileTparTimeout_Type(Integer32):defaultValue=16;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1000))
_CxeCcProfileTparTimeout_Type.__name__=_C
_CxeCcProfileTparTimeout_Object=MibTableColumn
cxeCcProfileTparTimeout=_CxeCcProfileTparTimeout_Object((1,3,6,1,4,1,9,9,325,1,1,2,1,20),_CxeCcProfileTparTimeout_Type())
cxeCcProfileTparTimeout.setMaxAccess(_D)
if mibBuilder.loadTexts:cxeCcProfileTparTimeout.setStatus(_A)
if mibBuilder.loadTexts:cxeCcProfileTparTimeout.setUnits(_F)
class _CxeCcProfileThistTimeout_Type(Integer32):defaultValue=30;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1000))
_CxeCcProfileThistTimeout_Type.__name__=_C
_CxeCcProfileThistTimeout_Object=MibTableColumn
cxeCcProfileThistTimeout=_CxeCcProfileThistTimeout_Object((1,3,6,1,4,1,9,9,325,1,1,2,1,21),_CxeCcProfileThistTimeout_Type())
cxeCcProfileThistTimeout.setMaxAccess(_D)
if mibBuilder.loadTexts:cxeCcProfileThistTimeout.setStatus(_A)
if mibBuilder.loadTexts:cxeCcProfileThistTimeout.setUnits(_F)
class _CxeCcProfileRtTimeout_Type(Integer32):defaultValue=180;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,3600))
_CxeCcProfileRtTimeout_Type.__name__=_C
_CxeCcProfileRtTimeout_Object=MibTableColumn
cxeCcProfileRtTimeout=_CxeCcProfileRtTimeout_Object((1,3,6,1,4,1,9,9,325,1,1,2,1,22),_CxeCcProfileRtTimeout_Type())
cxeCcProfileRtTimeout.setMaxAccess(_D)
if mibBuilder.loadTexts:cxeCcProfileRtTimeout.setStatus(_A)
if mibBuilder.loadTexts:cxeCcProfileRtTimeout.setUnits(_F)
class _CxeCcProfileRbkTimeout_Type(Integer32):defaultValue=180;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,3600))
_CxeCcProfileRbkTimeout_Type.__name__=_C
_CxeCcProfileRbkTimeout_Object=MibTableColumn
cxeCcProfileRbkTimeout=_CxeCcProfileRbkTimeout_Object((1,3,6,1,4,1,9,9,325,1,1,2,1,23),_CxeCcProfileRbkTimeout_Type())
cxeCcProfileRbkTimeout.setMaxAccess(_D)
if mibBuilder.loadTexts:cxeCcProfileRbkTimeout.setStatus(_A)
if mibBuilder.loadTexts:cxeCcProfileRbkTimeout.setUnits(_F)
class _CxeCcProfileCgTimeout_Type(Integer32):defaultValue=180;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,3600))
_CxeCcProfileCgTimeout_Type.__name__=_C
_CxeCcProfileCgTimeout_Object=MibTableColumn
cxeCcProfileCgTimeout=_CxeCcProfileCgTimeout_Object((1,3,6,1,4,1,9,9,325,1,1,2,1,24),_CxeCcProfileCgTimeout_Type())
cxeCcProfileCgTimeout.setMaxAccess(_D)
if mibBuilder.loadTexts:cxeCcProfileCgTimeout.setStatus(_A)
if mibBuilder.loadTexts:cxeCcProfileCgTimeout.setUnits(_F)
class _CxeCcProfileBzTimeout_Type(Integer32):defaultValue=30;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,3600))
_CxeCcProfileBzTimeout_Type.__name__=_C
_CxeCcProfileBzTimeout_Object=MibTableColumn
cxeCcProfileBzTimeout=_CxeCcProfileBzTimeout_Object((1,3,6,1,4,1,9,9,325,1,1,2,1,25),_CxeCcProfileBzTimeout_Type())
cxeCcProfileBzTimeout.setMaxAccess(_D)
if mibBuilder.loadTexts:cxeCcProfileBzTimeout.setStatus(_A)
if mibBuilder.loadTexts:cxeCcProfileBzTimeout.setUnits(_F)
class _CxeCcProfileDlTimeout_Type(Integer32):defaultValue=16;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,3600))
_CxeCcProfileDlTimeout_Type.__name__=_C
_CxeCcProfileDlTimeout_Object=MibTableColumn
cxeCcProfileDlTimeout=_CxeCcProfileDlTimeout_Object((1,3,6,1,4,1,9,9,325,1,1,2,1,26),_CxeCcProfileDlTimeout_Type())
cxeCcProfileDlTimeout.setMaxAccess(_D)
if mibBuilder.loadTexts:cxeCcProfileDlTimeout.setStatus(_A)
if mibBuilder.loadTexts:cxeCcProfileDlTimeout.setUnits(_F)
class _CxeCcProfileSlTimeout_Type(Integer32):defaultValue=16;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,3600))
_CxeCcProfileSlTimeout_Type.__name__=_C
_CxeCcProfileSlTimeout_Object=MibTableColumn
cxeCcProfileSlTimeout=_CxeCcProfileSlTimeout_Object((1,3,6,1,4,1,9,9,325,1,1,2,1,27),_CxeCcProfileSlTimeout_Type())
cxeCcProfileSlTimeout.setMaxAccess(_D)
if mibBuilder.loadTexts:cxeCcProfileSlTimeout.setStatus(_A)
if mibBuilder.loadTexts:cxeCcProfileSlTimeout.setUnits(_F)
class _CxeCcProfileRgTimeout_Type(Integer32):defaultValue=180;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,3600))
_CxeCcProfileRgTimeout_Type.__name__=_C
_CxeCcProfileRgTimeout_Object=MibTableColumn
cxeCcProfileRgTimeout=_CxeCcProfileRgTimeout_Object((1,3,6,1,4,1,9,9,325,1,1,2,1,28),_CxeCcProfileRgTimeout_Type())
cxeCcProfileRgTimeout.setMaxAccess(_D)
if mibBuilder.loadTexts:cxeCcProfileRgTimeout.setStatus(_A)
if mibBuilder.loadTexts:cxeCcProfileRgTimeout.setUnits(_F)
class _CxeCcProfileRoTimeout_Type(Integer32):defaultValue=30;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,3600))
_CxeCcProfileRoTimeout_Type.__name__=_C
_CxeCcProfileRoTimeout_Object=MibTableColumn
cxeCcProfileRoTimeout=_CxeCcProfileRoTimeout_Object((1,3,6,1,4,1,9,9,325,1,1,2,1,29),_CxeCcProfileRoTimeout_Type())
cxeCcProfileRoTimeout.setMaxAccess(_D)
if mibBuilder.loadTexts:cxeCcProfileRoTimeout.setStatus(_A)
if mibBuilder.loadTexts:cxeCcProfileRoTimeout.setUnits(_F)
class _CxeCcProfileCot1Timeout_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_CxeCcProfileCot1Timeout_Type.__name__=_C
_CxeCcProfileCot1Timeout_Object=MibTableColumn
cxeCcProfileCot1Timeout=_CxeCcProfileCot1Timeout_Object((1,3,6,1,4,1,9,9,325,1,1,2,1,30),_CxeCcProfileCot1Timeout_Type())
cxeCcProfileCot1Timeout.setMaxAccess(_D)
if mibBuilder.loadTexts:cxeCcProfileCot1Timeout.setStatus(_A)
if mibBuilder.loadTexts:cxeCcProfileCot1Timeout.setUnits(_F)
class _CxeCcProfileCot2Timeout_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_CxeCcProfileCot2Timeout_Type.__name__=_C
_CxeCcProfileCot2Timeout_Object=MibTableColumn
cxeCcProfileCot2Timeout=_CxeCcProfileCot2Timeout_Object((1,3,6,1,4,1,9,9,325,1,1,2,1,31),_CxeCcProfileCot2Timeout_Type())
cxeCcProfileCot2Timeout.setMaxAccess(_D)
if mibBuilder.loadTexts:cxeCcProfileCot2Timeout.setStatus(_A)
if mibBuilder.loadTexts:cxeCcProfileCot2Timeout.setUnits(_F)
_CxeCcProfileRowStatus_Type=RowStatus
_CxeCcProfileRowStatus_Object=MibTableColumn
cxeCcProfileRowStatus=_CxeCcProfileRowStatus_Object((1,3,6,1,4,1,9,9,325,1,1,2,1,32),_CxeCcProfileRowStatus_Type())
cxeCcProfileRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:cxeCcProfileRowStatus.setStatus(_A)
_CxeCallCtrlMIBConformance_ObjectIdentity=ObjectIdentity
cxeCallCtrlMIBConformance=_CxeCallCtrlMIBConformance_ObjectIdentity((1,3,6,1,4,1,9,9,325,2))
_CxeCallCtrlMIBCompliances_ObjectIdentity=ObjectIdentity
cxeCallCtrlMIBCompliances=_CxeCallCtrlMIBCompliances_ObjectIdentity((1,3,6,1,4,1,9,9,325,2,1))
_CxeCallCtrlMIBGroups_ObjectIdentity=ObjectIdentity
cxeCallCtrlMIBGroups=_CxeCallCtrlMIBGroups_ObjectIdentity((1,3,6,1,4,1,9,9,325,2,2))
cxeCallCtrlGroup=ObjectGroup((1,3,6,1,4,1,9,9,325,2,2,1))
cxeCallCtrlGroup.setObjects(*((_B,_U),(_B,_V),(_B,_W),(_B,_X),(_B,_Y),(_B,_Z),(_B,_a),(_B,_b),(_B,_c),(_B,_d),(_B,_e),(_B,_f),(_B,_g),(_B,_h),(_B,_i),(_B,_j),(_B,_k),(_B,_l),(_B,_m),(_B,_n),(_B,_o),(_B,_p)))
if mibBuilder.loadTexts:cxeCallCtrlGroup.setStatus(_A)
cxeCcProfileGroup=ObjectGroup((1,3,6,1,4,1,9,9,325,2,2,2))
cxeCcProfileGroup.setObjects(*((_B,_q),(_B,_r),(_B,_s),(_B,_t),(_B,_u),(_B,_v),(_B,_w),(_B,_x),(_B,_y),(_B,_z),(_B,_A0),(_B,_A1),(_B,_A2),(_B,_A3),(_B,_A4),(_B,_A5),(_B,_A6),(_B,_A7),(_B,_A8),(_B,_A9),(_B,_AA),(_B,_AB),(_B,_AC),(_B,_AD),(_B,_AE),(_B,_AF),(_B,_AG),(_B,_AH),(_B,_AI),(_B,_AJ)))
if mibBuilder.loadTexts:cxeCcProfileGroup.setStatus(_A)
cxeCallCtrlMIBCompliance=ModuleCompliance((1,3,6,1,4,1,9,9,325,2,1,1))
cxeCallCtrlMIBCompliance.setObjects(*((_B,_AK),(_B,_AL)))
if mibBuilder.loadTexts:cxeCallCtrlMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{_J:DtmfRelayMode,_K:DtmfCodecType,_S:CxeTerminalProviderCode,'ciscoXgcpExtMIB':ciscoXgcpExtMIB,'cxgcpExtObjects':cxgcpExtObjects,'cxgcpExtConfig':cxgcpExtConfig,'cxeCallCtrlConfigTable':cxeCallCtrlConfigTable,'cxeCallCtrlConfigEntry':cxeCallCtrlConfigEntry,_U:cxeCallCtrlControlServiceType,_V:cxeCallCtrlBearerServiceType,_W:cxeCallCtrlVoIpDtmfRelayMode,_X:cxeCallCtrlVoIpDtmfCodec,_Y:cxeCallCtrlVoAal2DtmfRelayMode,_Z:cxeCallCtrlVoAal2DtmfCodec,_a:cxeCallCtrlTsePayload,_b:cxeCallCtrlNetNseTimer,_c:cxeCallCtrlRtcpRcvTimer,_d:cxeCallCtrlIgnoreAal2LcoCodec,_e:cxeCallCtrlDigitMapOrder,_f:cxeCallCtrlT38Inhibited,_g:cxeCallCtrlT38NseRspTimer,_h:cxeCallCtrlT38FecEnabled,_i:cxeCallCtrlT38LsRedundancy,_j:cxeCallCtrlT38HsRedundancy,_k:cxeCallCtrlT38NsfCountryCode,_l:cxeCallCtrlT38NsfVendorCode,_m:cxeCallCtrlVselDselFselSupport,_n:cxeCallCtrlDefaultBearTraffic,_o:cxeCallCtrlLastFailedMgcAddrType,_p:cxeCallCtrlLastFailedMgcAddress,'cxeCallCtrlProfileTable':cxeCallCtrlProfileTable,'cxeCallCtrlProfileEntry':cxeCallCtrlProfileEntry,_T:cxeCcProfileIndex,_q:cxeCcProfileName,_r:cxeCcProfileNumVifs,_s:cxeCcProfileMgcGrpNum,_t:cxeCcProfileMgcAddrType,_u:cxeCcProfileMgcAddress,_v:cxeCcProfileProtocolIdx,_w:cxeCcProfileXgcpRetryMethod,_x:cxeCcProfileRetryMax1,_y:cxeCcProfileDnsLookupMax1,_z:cxeCcProfileRetryMax2,_A0:cxeCcProfileDnsLookupMax2,_A1:cxeCcProfileMwiTimeout,_A2:cxeCcProfileTsmaxTimeout,_A3:cxeCcProfileTdinitTimeout,_A4:cxeCcProfileTdminTimeout,_A5:cxeCcProfileTdmaxTimeout,_A6:cxeCcProfileTcritTimeout,_A7:cxeCcProfileTparTimeout,_A8:cxeCcProfileThistTimeout,_A9:cxeCcProfileRtTimeout,_AA:cxeCcProfileRbkTimeout,_AB:cxeCcProfileCgTimeout,_AC:cxeCcProfileBzTimeout,_AD:cxeCcProfileDlTimeout,_AE:cxeCcProfileSlTimeout,_AF:cxeCcProfileRgTimeout,_AG:cxeCcProfileRoTimeout,_AH:cxeCcProfileCot1Timeout,_AI:cxeCcProfileCot2Timeout,_AJ:cxeCcProfileRowStatus,'cxeCallCtrlMIBConformance':cxeCallCtrlMIBConformance,'cxeCallCtrlMIBCompliances':cxeCallCtrlMIBCompliances,'cxeCallCtrlMIBCompliance':cxeCallCtrlMIBCompliance,'cxeCallCtrlMIBGroups':cxeCallCtrlMIBGroups,_AK:cxeCallCtrlGroup,_AL:cxeCcProfileGroup})