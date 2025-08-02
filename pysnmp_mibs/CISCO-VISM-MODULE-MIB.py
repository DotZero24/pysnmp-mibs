_BW='ciscoVismSystemGroupSup1'
_BV='ciscoVismDspGroupSup1'
_BU='ciscoVismSystemFeatureGroup'
_BT='ciscoVismSystemGroup'
_BS='vismFaxDeJitterInitialDelay'
_BR='vismFaxDeJitterMode'
_BQ='vismContinuityCheckCellEnable'
_BP='vismPvcAlarmLogOperTimer'
_BO='vismPvcAlarmLogAdminTimer'
_BN='vismPvcAlarmLogEnable'
_BM='vismOamLoopbackSetCLP'
_BL='vismSSRCEnable'
_BK='vismSplModemToneBitMap'
_BJ='vismTrapIntegerValue'
_BI='vismPacketizationPeriod'
_BH='vismPrevMode'
_BG='vismJitterInitialDelay'
_BF='vismJitterDelayMode'
_BE='vismEcanCnfIdleDirection'
_BD='vismEcanCnfIdlePattern'
_BC='vismAal2CidFillTimer'
_BB='vismAal2VADTimer'
_BA='vismAal2Type3Redundancy'
_B9='vismAal2CasTransport'
_B8='vismAal2DtmfRelay'
_B7='vismAal2SubcellMuxing'
_B6='vismTrapStrIndex1'
_B5='vismTrapIntIndex2'
_B4='vismTrapIntIndex1'
_B3='vismConfigChangeTypeBitMap'
_B2='vismDynamicPT'
_B1='vismXgcpSdpOst'
_B0='vismAisSuppression'
_A_='vismDSPHeartbeat'
_Az='vismPayloadType'
_Ay='vismUpspeedCodec'
_Ax='vismDspHealth'
_Aw='vismAdaptiveGainControl'
_Av='vismCompCnfPacketSize'
_Au='vismVoIpEventNegotiationPolicy'
_At='vismVoIpLapdTrunkPVC'
_As='vismRtcpRecvMultiplier'
_Ar='vismVoIpDPvcRecoverCnt'
_Aq='vismVoIpDPvcRetryCnt'
_Ap='vismVoIpDPvcOamCellGap'
_Ao='vismVoIpSIDPayloadType'
_An='vismVoIpNTECapabilityNegotiate'
_Am='vismVoIpVADTimer'
_Al='vismVoIpTripleRedundancy'
_Ak='vismVoIpCasTransport'
_Aj='vismVoIpDtmfRelay'
_Ai='vismRtpReceiveTimer'
_Ah='vismRtcpRepInterval'
_Ag='vismBearerTos'
_Af='vismBearerSubNetMask'
_Ae='vismBearerIpAddress'
_Ad='vismControlTos'
_Ac='vismSubNetMask'
_Ab='vismIpAddress'
_Aa='vismCallStatsClrButton'
_AZ='vismFailedCalls'
_AY='vismSuccessfulCalls'
_AX='vismTotalCalls'
_AW='vismSysPerfClrButton'
_AV='vismMemoryUtilization'
_AU='vismCPUUtilization'
_AT='lclRcdLco'
_AS='lclLcoRcd'
_AR='rcdLclLco'
_AQ='rcdLcoLcl'
_AP='lcoLclRcd'
_AO='lcoRcdLcl'
_AN='aal2Trunking'
_AM='voipSwitching'
_AL='VismFaxDeJitterInitDelay'
_AK='VismFaxDeJitterMode'
_AJ='ninetyfive'
_AI='eightyfive'
_AH='seventyfive'
_AG='sixtyfive'
_AF='fiftyfive'
_AE='fortyfive'
_AD='thirtyfive'
_AC='twentyfive'
_AB='unSpecified'
_AA='OctetString'
_A9='ciscoVismSystemFeatureGroupRev1'
_A8='vismTrapFilteringEnable'
_A7='vismBearerIpPingEnable'
_A6='vismDualToneDetect'
_A5='vismMemoryUtilizationThreshold'
_A4='vismCPUUtilizationThreshold'
_A3='vismFreeDs0Threshold'
_A2='vismOamLoopThreshold'
_A1='vismSendDataGramSize'
_A0='vismSendDnEnable'
_z='vismReverseCotTone'
_y='vismContinuityCo2Timer'
_x='vismContinuityCo1Timer'
_w='vismLongDurationTimer'
_v='vismMaxConfNum'
_u='vismCaleaEnable'
_t='vismBearerContinuityTest'
_s='vismAggregateSvcBandwidth'
_r='vismAggregateTrafficClipping'
_q='vismVADDutyCycle'
_p='vismVADTolerance'
_o='vismFeatureBitMap'
_n='vismExtDnsServerDn'
_m='vismCacRejectionPolicy'
_l='vismCarrierLossPolicy'
_k='vismProfileNegotiationOption'
_j='vismCodecNegotiationOption'
_i='vismBearerContinuityTimer'
_h='vismXgcpBearerConnectionType'
_g='vismXgcpBearerVCType'
_f='vismXgcpBearerNetworkType'
_e='vismTftpServerDn'
_d='vismAppliedTemplate'
_c='vismAvailableDs0Count'
_b='vismCacEnable'
_a='vismMode'
_Z='vismEcanEncoding'
_Y='vismDaughterCardHWRev'
_X='vismDaughterCardDescription'
_W='vismDaughterCardSerialNum'
_V='Unsigned32'
_U='ciscoVismTrapVarbindGroup'
_T='milliseconds'
_S='ciscoVismSystemGroup1'
_R='ciscoVismAal2Group'
_Q='ciscoVismTrapObjGroup'
_P='ciscoVismInteropGroup'
_O='ciscoVismDspGroup'
_N='ciscoVismVoIpGroup'
_M='ciscoVismIpGroup'
_L='ciscoVismCallStatsGroup'
_K='ciscoVismPerfStatsGroup'
_J='enable'
_I='disable'
_H='SnmpAdminString'
_G='deprecated'
_F='TruthValue'
_E='read-only'
_D='Integer32'
_C='read-write'
_B='current'
_A='CISCO-VISM-MODULE-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_AA,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
cardSpecific,voice=mibBuilder.importSymbols('BASIS-MIB','cardSpecific','voice')
ciscoWan,=mibBuilder.importSymbols('CISCOWAN-SMI','ciscoWan')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB',_H)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_V,'iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention',_F)
ciscoVismModuleMIB=ModuleIdentity((1,3,6,1,4,1,351,150,82))
if mibBuilder.loadTexts:ciscoVismModuleMIB.setRevisions(('2005-10-17 00:00','2005-03-01 00:00','2004-05-24 00:00','2004-03-09 00:00','2003-10-31 00:00','2003-06-18 00:00'))
class VismFaxDeJitterMode(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_AB,1),('adaptive',2),('fixedWithTS',3),('fixedWithoutTS',4),('passThrough',5)))
class VismFaxDeJitterInitDelay(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,5,10,15,20,25,30,35,40,45,50,55,60,65,70,75,80,85,90,95,100)));namedValues=NamedValues(*((_AB,0),('five',5),('ten',10),('fifteen',15),('twenty',20),(_AC,25),('thirty',30),(_AD,35),('forty',40),(_AE,45),('fifty',50),(_AF,55),('sixty',60),(_AG,65),('seventy',70),(_AH,75),('eighty',80),(_AI,85),('ninety',90),(_AJ,95),('hundred',100)))
_VismConfig_ObjectIdentity=ObjectIdentity
vismConfig=_VismConfig_ObjectIdentity((1,3,6,1,4,1,351,110,3,17))
_VismIpGrp_ObjectIdentity=ObjectIdentity
vismIpGrp=_VismIpGrp_ObjectIdentity((1,3,6,1,4,1,351,110,3,17,1))
_VismIpAddress_Type=IpAddress
_VismIpAddress_Object=MibScalar
vismIpAddress=_VismIpAddress_Object((1,3,6,1,4,1,351,110,3,17,1,1),_VismIpAddress_Type())
vismIpAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:vismIpAddress.setStatus(_B)
_VismSubNetMask_Type=IpAddress
_VismSubNetMask_Object=MibScalar
vismSubNetMask=_VismSubNetMask_Object((1,3,6,1,4,1,351,110,3,17,1,2),_VismSubNetMask_Type())
vismSubNetMask.setMaxAccess(_C)
if mibBuilder.loadTexts:vismSubNetMask.setStatus(_B)
class _VismControlTos_Type(Integer32):defaultValue=96;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_VismControlTos_Type.__name__=_D
_VismControlTos_Object=MibScalar
vismControlTos=_VismControlTos_Object((1,3,6,1,4,1,351,110,3,17,1,3),_VismControlTos_Type())
vismControlTos.setMaxAccess(_C)
if mibBuilder.loadTexts:vismControlTos.setStatus(_B)
_VismBearerIpAddress_Type=IpAddress
_VismBearerIpAddress_Object=MibScalar
vismBearerIpAddress=_VismBearerIpAddress_Object((1,3,6,1,4,1,351,110,3,17,1,4),_VismBearerIpAddress_Type())
vismBearerIpAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:vismBearerIpAddress.setStatus(_B)
_VismBearerSubNetMask_Type=IpAddress
_VismBearerSubNetMask_Object=MibScalar
vismBearerSubNetMask=_VismBearerSubNetMask_Object((1,3,6,1,4,1,351,110,3,17,1,5),_VismBearerSubNetMask_Type())
vismBearerSubNetMask.setMaxAccess(_C)
if mibBuilder.loadTexts:vismBearerSubNetMask.setStatus(_B)
_VismVoIpGrp_ObjectIdentity=ObjectIdentity
vismVoIpGrp=_VismVoIpGrp_ObjectIdentity((1,3,6,1,4,1,351,110,3,17,2))
class _VismBearerTos_Type(Integer32):defaultValue=160;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_VismBearerTos_Type.__name__=_D
_VismBearerTos_Object=MibScalar
vismBearerTos=_VismBearerTos_Object((1,3,6,1,4,1,351,110,3,17,2,1),_VismBearerTos_Type())
vismBearerTos.setMaxAccess(_C)
if mibBuilder.loadTexts:vismBearerTos.setStatus(_B)
class _VismRtcpRepInterval_Type(Integer32):defaultValue=5000;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(500,15000))
_VismRtcpRepInterval_Type.__name__=_D
_VismRtcpRepInterval_Object=MibScalar
vismRtcpRepInterval=_VismRtcpRepInterval_Object((1,3,6,1,4,1,351,110,3,17,2,2),_VismRtcpRepInterval_Type())
vismRtcpRepInterval.setMaxAccess(_C)
if mibBuilder.loadTexts:vismRtcpRepInterval.setStatus(_B)
if mibBuilder.loadTexts:vismRtcpRepInterval.setUnits(_T)
class _VismRtpReceiveTimer_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_I,1),(_J,2)))
_VismRtpReceiveTimer_Type.__name__=_D
_VismRtpReceiveTimer_Object=MibScalar
vismRtpReceiveTimer=_VismRtpReceiveTimer_Object((1,3,6,1,4,1,351,110,3,17,2,3),_VismRtpReceiveTimer_Type())
vismRtpReceiveTimer.setMaxAccess(_C)
if mibBuilder.loadTexts:vismRtpReceiveTimer.setStatus(_B)
class _VismPacketizationPeriod_Type(Integer32):defaultValue=10;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(10,20,30,40)));namedValues=NamedValues(*(('tenms',10),('twentyms',20),('thirtyms',30),('fourtyms',40)))
_VismPacketizationPeriod_Type.__name__=_D
_VismPacketizationPeriod_Object=MibScalar
vismPacketizationPeriod=_VismPacketizationPeriod_Object((1,3,6,1,4,1,351,110,3,17,2,4),_VismPacketizationPeriod_Type())
vismPacketizationPeriod.setMaxAccess(_E)
if mibBuilder.loadTexts:vismPacketizationPeriod.setStatus(_G)
class _VismVoIpDtmfRelay_Type(TruthValue):defaultValue=1
_VismVoIpDtmfRelay_Type.__name__=_F
_VismVoIpDtmfRelay_Object=MibScalar
vismVoIpDtmfRelay=_VismVoIpDtmfRelay_Object((1,3,6,1,4,1,351,110,3,17,2,5),_VismVoIpDtmfRelay_Type())
vismVoIpDtmfRelay.setMaxAccess(_C)
if mibBuilder.loadTexts:vismVoIpDtmfRelay.setStatus(_B)
class _VismVoIpCasTransport_Type(TruthValue):defaultValue=2
_VismVoIpCasTransport_Type.__name__=_F
_VismVoIpCasTransport_Object=MibScalar
vismVoIpCasTransport=_VismVoIpCasTransport_Object((1,3,6,1,4,1,351,110,3,17,2,6),_VismVoIpCasTransport_Type())
vismVoIpCasTransport.setMaxAccess(_C)
if mibBuilder.loadTexts:vismVoIpCasTransport.setStatus(_B)
class _VismVoIpTripleRedundancy_Type(TruthValue):defaultValue=2
_VismVoIpTripleRedundancy_Type.__name__=_F
_VismVoIpTripleRedundancy_Object=MibScalar
vismVoIpTripleRedundancy=_VismVoIpTripleRedundancy_Object((1,3,6,1,4,1,351,110,3,17,2,7),_VismVoIpTripleRedundancy_Type())
vismVoIpTripleRedundancy.setMaxAccess(_C)
if mibBuilder.loadTexts:vismVoIpTripleRedundancy.setStatus(_B)
class _VismVoIpVADTimer_Type(Integer32):defaultValue=250;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(250,65535))
_VismVoIpVADTimer_Type.__name__=_D
_VismVoIpVADTimer_Object=MibScalar
vismVoIpVADTimer=_VismVoIpVADTimer_Object((1,3,6,1,4,1,351,110,3,17,2,8),_VismVoIpVADTimer_Type())
vismVoIpVADTimer.setMaxAccess(_C)
if mibBuilder.loadTexts:vismVoIpVADTimer.setStatus(_B)
if mibBuilder.loadTexts:vismVoIpVADTimer.setUnits(_T)
class _VismVoIpNTECapabilityNegotiate_Type(TruthValue):defaultValue=1
_VismVoIpNTECapabilityNegotiate_Type.__name__=_F
_VismVoIpNTECapabilityNegotiate_Object=MibScalar
vismVoIpNTECapabilityNegotiate=_VismVoIpNTECapabilityNegotiate_Object((1,3,6,1,4,1,351,110,3,17,2,9),_VismVoIpNTECapabilityNegotiate_Type())
vismVoIpNTECapabilityNegotiate.setMaxAccess(_C)
if mibBuilder.loadTexts:vismVoIpNTECapabilityNegotiate.setStatus(_B)
class _VismVoIpSIDPayloadType_Type(Integer32):defaultValue=13;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_VismVoIpSIDPayloadType_Type.__name__=_D
_VismVoIpSIDPayloadType_Object=MibScalar
vismVoIpSIDPayloadType=_VismVoIpSIDPayloadType_Object((1,3,6,1,4,1,351,110,3,17,2,10),_VismVoIpSIDPayloadType_Type())
vismVoIpSIDPayloadType.setMaxAccess(_C)
if mibBuilder.loadTexts:vismVoIpSIDPayloadType.setStatus(_B)
class _VismVoIpDPvcOamCellGap_Type(Integer32):defaultValue=500;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(10,5000))
_VismVoIpDPvcOamCellGap_Type.__name__=_D
_VismVoIpDPvcOamCellGap_Object=MibScalar
vismVoIpDPvcOamCellGap=_VismVoIpDPvcOamCellGap_Object((1,3,6,1,4,1,351,110,3,17,2,11),_VismVoIpDPvcOamCellGap_Type())
vismVoIpDPvcOamCellGap.setMaxAccess(_C)
if mibBuilder.loadTexts:vismVoIpDPvcOamCellGap.setStatus(_B)
if mibBuilder.loadTexts:vismVoIpDPvcOamCellGap.setUnits(_T)
class _VismVoIpDPvcRetryCnt_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,20))
_VismVoIpDPvcRetryCnt_Type.__name__=_D
_VismVoIpDPvcRetryCnt_Object=MibScalar
vismVoIpDPvcRetryCnt=_VismVoIpDPvcRetryCnt_Object((1,3,6,1,4,1,351,110,3,17,2,12),_VismVoIpDPvcRetryCnt_Type())
vismVoIpDPvcRetryCnt.setMaxAccess(_C)
if mibBuilder.loadTexts:vismVoIpDPvcRetryCnt.setStatus(_B)
class _VismVoIpDPvcRecoverCnt_Type(Integer32):defaultValue=5;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,20))
_VismVoIpDPvcRecoverCnt_Type.__name__=_D
_VismVoIpDPvcRecoverCnt_Object=MibScalar
vismVoIpDPvcRecoverCnt=_VismVoIpDPvcRecoverCnt_Object((1,3,6,1,4,1,351,110,3,17,2,13),_VismVoIpDPvcRecoverCnt_Type())
vismVoIpDPvcRecoverCnt.setMaxAccess(_C)
if mibBuilder.loadTexts:vismVoIpDPvcRecoverCnt.setStatus(_B)
class _VismRtcpRecvMultiplier_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,10))
_VismRtcpRecvMultiplier_Type.__name__=_D
_VismRtcpRecvMultiplier_Object=MibScalar
vismRtcpRecvMultiplier=_VismRtcpRecvMultiplier_Object((1,3,6,1,4,1,351,110,3,17,2,14),_VismRtcpRecvMultiplier_Type())
vismRtcpRecvMultiplier.setMaxAccess(_C)
if mibBuilder.loadTexts:vismRtcpRecvMultiplier.setStatus(_B)
if mibBuilder.loadTexts:vismRtcpRecvMultiplier.setUnits(_T)
class _VismVoIpLapdTrunkPVC_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('control',1),('bearer',2)))
_VismVoIpLapdTrunkPVC_Type.__name__=_D
_VismVoIpLapdTrunkPVC_Object=MibScalar
vismVoIpLapdTrunkPVC=_VismVoIpLapdTrunkPVC_Object((1,3,6,1,4,1,351,110,3,17,2,15),_VismVoIpLapdTrunkPVC_Type())
vismVoIpLapdTrunkPVC.setMaxAccess(_C)
if mibBuilder.loadTexts:vismVoIpLapdTrunkPVC.setStatus(_B)
class _VismVoIpEventNegotiationPolicy_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('none',1),('proprietary',2),('all',3)))
_VismVoIpEventNegotiationPolicy_Type.__name__=_D
_VismVoIpEventNegotiationPolicy_Object=MibScalar
vismVoIpEventNegotiationPolicy=_VismVoIpEventNegotiationPolicy_Object((1,3,6,1,4,1,351,110,3,17,2,16),_VismVoIpEventNegotiationPolicy_Type())
vismVoIpEventNegotiationPolicy.setMaxAccess(_C)
if mibBuilder.loadTexts:vismVoIpEventNegotiationPolicy.setStatus(_B)
_VismDspGrp_ObjectIdentity=ObjectIdentity
vismDspGrp=_VismDspGrp_ObjectIdentity((1,3,6,1,4,1,351,110,3,17,3))
class _VismEcanCnfIdlePattern_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('pattern1',1),('pattern2',2),('pattern3',3),('pattern4',4)))
_VismEcanCnfIdlePattern_Type.__name__=_D
_VismEcanCnfIdlePattern_Object=MibScalar
vismEcanCnfIdlePattern=_VismEcanCnfIdlePattern_Object((1,3,6,1,4,1,351,110,3,17,3,1),_VismEcanCnfIdlePattern_Type())
vismEcanCnfIdlePattern.setMaxAccess(_E)
if mibBuilder.loadTexts:vismEcanCnfIdlePattern.setStatus(_G)
class _VismEcanCnfIdleDirection_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('both',1),('either',2),('send',3),('receive',4)))
_VismEcanCnfIdleDirection_Type.__name__=_D
_VismEcanCnfIdleDirection_Object=MibScalar
vismEcanCnfIdleDirection=_VismEcanCnfIdleDirection_Object((1,3,6,1,4,1,351,110,3,17,3,2),_VismEcanCnfIdleDirection_Type())
vismEcanCnfIdleDirection.setMaxAccess(_E)
if mibBuilder.loadTexts:vismEcanCnfIdleDirection.setStatus(_G)
class _VismCompCnfPacketSize_Type(Integer32):defaultValue=80;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(80,80),ValueRangeConstraint(160,160))
_VismCompCnfPacketSize_Type.__name__=_D
_VismCompCnfPacketSize_Object=MibScalar
vismCompCnfPacketSize=_VismCompCnfPacketSize_Object((1,3,6,1,4,1,351,110,3,17,3,3),_VismCompCnfPacketSize_Type())
vismCompCnfPacketSize.setMaxAccess(_C)
if mibBuilder.loadTexts:vismCompCnfPacketSize.setStatus(_B)
class _VismERL_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('zerodb',1),('threedb',2),('sixdb',3),('worstdb',4)))
_VismERL_Type.__name__=_D
_VismERL_Object=MibScalar
vismERL=_VismERL_Object((1,3,6,1,4,1,351,110,3,17,3,4),_VismERL_Type())
vismERL.setMaxAccess(_C)
if mibBuilder.loadTexts:vismERL.setStatus(_B)
class _VismJitterDelayMode_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('fixed',1),('adaptive',2)))
_VismJitterDelayMode_Type.__name__=_D
_VismJitterDelayMode_Object=MibScalar
vismJitterDelayMode=_VismJitterDelayMode_Object((1,3,6,1,4,1,351,110,3,17,3,5),_VismJitterDelayMode_Type())
vismJitterDelayMode.setMaxAccess(_C)
if mibBuilder.loadTexts:vismJitterDelayMode.setStatus(_G)
class _VismJitterInitialDelay_Type(Integer32):defaultValue=40;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,5,10,15,20,25,30,35,40,45,50,55,60,65,70,75,80,85,90,95,100)));namedValues=NamedValues(*(('zero',1),('five',5),('ten',10),('fifteen',15),('twenty',20),(_AC,25),('thirty',30),(_AD,35),('fourty',40),(_AE,45),('fifty',50),(_AF,55),('sixty',60),(_AG,65),('seventy',70),(_AH,75),('eighty',80),(_AI,85),('ninty',90),(_AJ,95),('hundred',100)))
_VismJitterInitialDelay_Type.__name__=_D
_VismJitterInitialDelay_Object=MibScalar
vismJitterInitialDelay=_VismJitterInitialDelay_Object((1,3,6,1,4,1,351,110,3,17,3,6),_VismJitterInitialDelay_Type())
vismJitterInitialDelay.setMaxAccess(_C)
if mibBuilder.loadTexts:vismJitterInitialDelay.setStatus(_G)
class _VismAdaptiveGainControl_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('off',1),('on',2)))
_VismAdaptiveGainControl_Type.__name__=_D
_VismAdaptiveGainControl_Object=MibScalar
vismAdaptiveGainControl=_VismAdaptiveGainControl_Object((1,3,6,1,4,1,351,110,3,17,3,7),_VismAdaptiveGainControl_Type())
vismAdaptiveGainControl.setMaxAccess(_C)
if mibBuilder.loadTexts:vismAdaptiveGainControl.setStatus(_B)
class _VismDspHealth_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_VismDspHealth_Type.__name__=_D
_VismDspHealth_Object=MibScalar
vismDspHealth=_VismDspHealth_Object((1,3,6,1,4,1,351,110,3,17,3,8),_VismDspHealth_Type())
vismDspHealth.setMaxAccess(_E)
if mibBuilder.loadTexts:vismDspHealth.setStatus(_B)
class _VismUpspeedCodec_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9)));namedValues=NamedValues(*(('g-711u',1),('g-711a',2),('g-726-32',3),('clearChannel',4),('g-723h',5),('g-723l',6),('g-726-16',7),('g-726-24',8),('g-726-40',9)))
_VismUpspeedCodec_Type.__name__=_D
_VismUpspeedCodec_Object=MibScalar
vismUpspeedCodec=_VismUpspeedCodec_Object((1,3,6,1,4,1,351,110,3,17,3,9),_VismUpspeedCodec_Type())
vismUpspeedCodec.setMaxAccess(_C)
if mibBuilder.loadTexts:vismUpspeedCodec.setStatus(_B)
class _VismPayloadType_Type(Integer32):defaultValue=256;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,256))
_VismPayloadType_Type.__name__=_D
_VismPayloadType_Object=MibScalar
vismPayloadType=_VismPayloadType_Object((1,3,6,1,4,1,351,110,3,17,3,10),_VismPayloadType_Type())
vismPayloadType.setMaxAccess(_C)
if mibBuilder.loadTexts:vismPayloadType.setStatus(_B)
class _VismDSPHeartbeat_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_VismDSPHeartbeat_Type.__name__=_D
_VismDSPHeartbeat_Object=MibScalar
vismDSPHeartbeat=_VismDSPHeartbeat_Object((1,3,6,1,4,1,351,110,3,17,3,11),_VismDSPHeartbeat_Type())
vismDSPHeartbeat.setMaxAccess(_C)
if mibBuilder.loadTexts:vismDSPHeartbeat.setStatus(_B)
class _VismFaxDeJitterMode_Type(VismFaxDeJitterMode):defaultValue=1
_VismFaxDeJitterMode_Type.__name__=_AK
_VismFaxDeJitterMode_Object=MibScalar
vismFaxDeJitterMode=_VismFaxDeJitterMode_Object((1,3,6,1,4,1,351,110,3,17,3,12),_VismFaxDeJitterMode_Type())
vismFaxDeJitterMode.setMaxAccess(_C)
if mibBuilder.loadTexts:vismFaxDeJitterMode.setStatus(_B)
class _VismFaxDeJitterInitialDelay_Type(VismFaxDeJitterInitDelay):defaultValue=0
_VismFaxDeJitterInitialDelay_Type.__name__=_AL
_VismFaxDeJitterInitialDelay_Object=MibScalar
vismFaxDeJitterInitialDelay=_VismFaxDeJitterInitialDelay_Object((1,3,6,1,4,1,351,110,3,17,3,13),_VismFaxDeJitterInitialDelay_Type())
vismFaxDeJitterInitialDelay.setMaxAccess(_C)
if mibBuilder.loadTexts:vismFaxDeJitterInitialDelay.setStatus(_B)
_VismSystemGrp_ObjectIdentity=ObjectIdentity
vismSystemGrp=_VismSystemGrp_ObjectIdentity((1,3,6,1,4,1,351,110,3,17,4))
class _VismDaughterCardSerialNum_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,6))
_VismDaughterCardSerialNum_Type.__name__=_H
_VismDaughterCardSerialNum_Object=MibScalar
vismDaughterCardSerialNum=_VismDaughterCardSerialNum_Object((1,3,6,1,4,1,351,110,3,17,4,1),_VismDaughterCardSerialNum_Type())
vismDaughterCardSerialNum.setMaxAccess(_E)
if mibBuilder.loadTexts:vismDaughterCardSerialNum.setStatus(_B)
class _VismDaughterCardDescription_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,20))
_VismDaughterCardDescription_Type.__name__=_H
_VismDaughterCardDescription_Object=MibScalar
vismDaughterCardDescription=_VismDaughterCardDescription_Object((1,3,6,1,4,1,351,110,3,17,4,2),_VismDaughterCardDescription_Type())
vismDaughterCardDescription.setMaxAccess(_E)
if mibBuilder.loadTexts:vismDaughterCardDescription.setStatus(_B)
class _VismDaughterCardHWRev_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,2))
_VismDaughterCardHWRev_Type.__name__=_H
_VismDaughterCardHWRev_Object=MibScalar
vismDaughterCardHWRev=_VismDaughterCardHWRev_Object((1,3,6,1,4,1,351,110,3,17,4,3),_VismDaughterCardHWRev_Type())
vismDaughterCardHWRev.setMaxAccess(_E)
if mibBuilder.loadTexts:vismDaughterCardHWRev.setStatus(_B)
class _VismEcanEncoding_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('mu-law',1),('a-law',2)))
_VismEcanEncoding_Type.__name__=_D
_VismEcanEncoding_Object=MibScalar
vismEcanEncoding=_VismEcanEncoding_Object((1,3,6,1,4,1,351,110,3,17,4,4),_VismEcanEncoding_Type())
vismEcanEncoding.setMaxAccess(_E)
if mibBuilder.loadTexts:vismEcanEncoding.setStatus(_B)
class _VismMode_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,99,100)));namedValues=NamedValues(*((_AM,1),(_AN,2),('aal1Svc',3),('switchedVoipCASBh',4),('switchedVoipPRIBh',5),('switchedAal2CASBh',6),('switchedAal2Svc',7),('switchedAal2Pvc',8),('voipAndAal1Svc',9),('voipAndAal2Trunking',10),('superMode',99),('unknownMode',100)))
_VismMode_Type.__name__=_D
_VismMode_Object=MibScalar
vismMode=_VismMode_Object((1,3,6,1,4,1,351,110,3,17,4,5),_VismMode_Type())
vismMode.setMaxAccess(_E)
if mibBuilder.loadTexts:vismMode.setStatus(_B)
class _VismPrevMode_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_AM,1),(_AN,2),('aal1Svc',3),('aal2PvcSwitching',4)))
_VismPrevMode_Type.__name__=_D
_VismPrevMode_Object=MibScalar
vismPrevMode=_VismPrevMode_Object((1,3,6,1,4,1,351,110,3,17,4,6),_VismPrevMode_Type())
vismPrevMode.setMaxAccess(_E)
if mibBuilder.loadTexts:vismPrevMode.setStatus(_G)
class _VismCacEnable_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_I,1),(_J,2)))
_VismCacEnable_Type.__name__=_D
_VismCacEnable_Object=MibScalar
vismCacEnable=_VismCacEnable_Object((1,3,6,1,4,1,351,110,3,17,4,7),_VismCacEnable_Type())
vismCacEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:vismCacEnable.setStatus(_B)
class _VismAvailableDs0Count_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,248))
_VismAvailableDs0Count_Type.__name__=_D
_VismAvailableDs0Count_Object=MibScalar
vismAvailableDs0Count=_VismAvailableDs0Count_Object((1,3,6,1,4,1,351,110,3,17,4,8),_VismAvailableDs0Count_Type())
vismAvailableDs0Count.setMaxAccess(_E)
if mibBuilder.loadTexts:vismAvailableDs0Count.setStatus(_B)
class _VismAppliedTemplate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_VismAppliedTemplate_Type.__name__=_D
_VismAppliedTemplate_Object=MibScalar
vismAppliedTemplate=_VismAppliedTemplate_Object((1,3,6,1,4,1,351,110,3,17,4,9),_VismAppliedTemplate_Type())
vismAppliedTemplate.setMaxAccess(_E)
if mibBuilder.loadTexts:vismAppliedTemplate.setStatus(_B)
class _VismTftpServerDn_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,64))
_VismTftpServerDn_Type.__name__=_H
_VismTftpServerDn_Object=MibScalar
vismTftpServerDn=_VismTftpServerDn_Object((1,3,6,1,4,1,351,110,3,17,4,11),_VismTftpServerDn_Type())
vismTftpServerDn.setMaxAccess(_C)
if mibBuilder.loadTexts:vismTftpServerDn.setStatus(_B)
class _VismXgcpBearerNetworkType_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('ip',1),('atm',2)))
_VismXgcpBearerNetworkType_Type.__name__=_D
_VismXgcpBearerNetworkType_Object=MibScalar
vismXgcpBearerNetworkType=_VismXgcpBearerNetworkType_Object((1,3,6,1,4,1,351,110,3,17,4,12),_VismXgcpBearerNetworkType_Type())
vismXgcpBearerNetworkType.setMaxAccess(_C)
if mibBuilder.loadTexts:vismXgcpBearerNetworkType.setStatus(_B)
class _VismXgcpBearerVCType_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('pvc',1),('svc',2)))
_VismXgcpBearerVCType_Type.__name__=_D
_VismXgcpBearerVCType_Object=MibScalar
vismXgcpBearerVCType=_VismXgcpBearerVCType_Object((1,3,6,1,4,1,351,110,3,17,4,13),_VismXgcpBearerVCType_Type())
vismXgcpBearerVCType.setMaxAccess(_C)
if mibBuilder.loadTexts:vismXgcpBearerVCType.setStatus(_B)
class _VismXgcpBearerConnectionType_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('aal1Sdt',1),('aal2',2),('notApplicable',3)))
_VismXgcpBearerConnectionType_Type.__name__=_D
_VismXgcpBearerConnectionType_Object=MibScalar
vismXgcpBearerConnectionType=_VismXgcpBearerConnectionType_Object((1,3,6,1,4,1,351,110,3,17,4,14),_VismXgcpBearerConnectionType_Type())
vismXgcpBearerConnectionType.setMaxAccess(_C)
if mibBuilder.loadTexts:vismXgcpBearerConnectionType.setStatus(_B)
class _VismBearerContinuityTimer_Type(Integer32):defaultValue=1000;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,10000))
_VismBearerContinuityTimer_Type.__name__=_D
_VismBearerContinuityTimer_Object=MibScalar
vismBearerContinuityTimer=_VismBearerContinuityTimer_Object((1,3,6,1,4,1,351,110,3,17,4,15),_VismBearerContinuityTimer_Type())
vismBearerContinuityTimer.setMaxAccess(_C)
if mibBuilder.loadTexts:vismBearerContinuityTimer.setStatus(_B)
class _VismCodecNegotiationOption_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*((_AO,1),(_AP,2),(_AQ,3),(_AR,4),(_AS,5),(_AT,6)))
_VismCodecNegotiationOption_Type.__name__=_D
_VismCodecNegotiationOption_Object=MibScalar
vismCodecNegotiationOption=_VismCodecNegotiationOption_Object((1,3,6,1,4,1,351,110,3,17,4,16),_VismCodecNegotiationOption_Type())
vismCodecNegotiationOption.setMaxAccess(_C)
if mibBuilder.loadTexts:vismCodecNegotiationOption.setStatus(_B)
class _VismProfileNegotiationOption_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*((_AO,1),(_AP,2),(_AQ,3),(_AR,4),(_AS,5),(_AT,6)))
_VismProfileNegotiationOption_Type.__name__=_D
_VismProfileNegotiationOption_Object=MibScalar
vismProfileNegotiationOption=_VismProfileNegotiationOption_Object((1,3,6,1,4,1,351,110,3,17,4,17),_VismProfileNegotiationOption_Type())
vismProfileNegotiationOption.setMaxAccess(_C)
if mibBuilder.loadTexts:vismProfileNegotiationOption.setStatus(_B)
class _VismCarrierLossPolicy_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('previousCodec',1),('upspeedCodec',2)))
_VismCarrierLossPolicy_Type.__name__=_D
_VismCarrierLossPolicy_Object=MibScalar
vismCarrierLossPolicy=_VismCarrierLossPolicy_Object((1,3,6,1,4,1,351,110,3,17,4,18),_VismCarrierLossPolicy_Type())
vismCarrierLossPolicy.setMaxAccess(_C)
if mibBuilder.loadTexts:vismCarrierLossPolicy.setStatus(_B)
class _VismCacRejectionPolicy_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('delete',1),('maintain',2)))
_VismCacRejectionPolicy_Type.__name__=_D
_VismCacRejectionPolicy_Object=MibScalar
vismCacRejectionPolicy=_VismCacRejectionPolicy_Object((1,3,6,1,4,1,351,110,3,17,4,19),_VismCacRejectionPolicy_Type())
vismCacRejectionPolicy.setMaxAccess(_C)
if mibBuilder.loadTexts:vismCacRejectionPolicy.setStatus(_B)
class _VismExtDnsServerDn_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,64))
_VismExtDnsServerDn_Type.__name__=_H
_VismExtDnsServerDn_Object=MibScalar
vismExtDnsServerDn=_VismExtDnsServerDn_Object((1,3,6,1,4,1,351,110,3,17,4,20),_VismExtDnsServerDn_Type())
vismExtDnsServerDn.setMaxAccess(_C)
if mibBuilder.loadTexts:vismExtDnsServerDn.setStatus(_B)
class _VismFeatureBitMap_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_VismFeatureBitMap_Type.__name__=_D
_VismFeatureBitMap_Object=MibScalar
vismFeatureBitMap=_VismFeatureBitMap_Object((1,3,6,1,4,1,351,110,3,17,4,21),_VismFeatureBitMap_Type())
vismFeatureBitMap.setMaxAccess(_C)
if mibBuilder.loadTexts:vismFeatureBitMap.setStatus(_B)
class _VismVADTolerance_Type(Integer32):defaultValue=100;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,10000))
_VismVADTolerance_Type.__name__=_D
_VismVADTolerance_Object=MibScalar
vismVADTolerance=_VismVADTolerance_Object((1,3,6,1,4,1,351,110,3,17,4,22),_VismVADTolerance_Type())
vismVADTolerance.setMaxAccess(_C)
if mibBuilder.loadTexts:vismVADTolerance.setStatus(_B)
class _VismVADDutyCycle_Type(Integer32):defaultValue=61;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,100))
_VismVADDutyCycle_Type.__name__=_D
_VismVADDutyCycle_Object=MibScalar
vismVADDutyCycle=_VismVADDutyCycle_Object((1,3,6,1,4,1,351,110,3,17,4,23),_VismVADDutyCycle_Type())
vismVADDutyCycle.setMaxAccess(_C)
if mibBuilder.loadTexts:vismVADDutyCycle.setStatus(_B)
class _VismAggregateTrafficClipping_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_I,1),(_J,2)))
_VismAggregateTrafficClipping_Type.__name__=_D
_VismAggregateTrafficClipping_Object=MibScalar
vismAggregateTrafficClipping=_VismAggregateTrafficClipping_Object((1,3,6,1,4,1,351,110,3,17,4,24),_VismAggregateTrafficClipping_Type())
vismAggregateTrafficClipping.setMaxAccess(_C)
if mibBuilder.loadTexts:vismAggregateTrafficClipping.setStatus(_B)
class _VismAggregateSvcBandwidth_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100000))
_VismAggregateSvcBandwidth_Type.__name__=_D
_VismAggregateSvcBandwidth_Object=MibScalar
vismAggregateSvcBandwidth=_VismAggregateSvcBandwidth_Object((1,3,6,1,4,1,351,110,3,17,4,25),_VismAggregateSvcBandwidth_Type())
vismAggregateSvcBandwidth.setMaxAccess(_C)
if mibBuilder.loadTexts:vismAggregateSvcBandwidth.setStatus(_B)
class _VismBearerContinuityTest_Type(TruthValue):defaultValue=2
_VismBearerContinuityTest_Type.__name__=_F
_VismBearerContinuityTest_Object=MibScalar
vismBearerContinuityTest=_VismBearerContinuityTest_Object((1,3,6,1,4,1,351,110,3,17,4,26),_VismBearerContinuityTest_Type())
vismBearerContinuityTest.setMaxAccess(_C)
if mibBuilder.loadTexts:vismBearerContinuityTest.setStatus(_B)
class _VismCaleaEnable_Type(TruthValue):defaultValue=2
_VismCaleaEnable_Type.__name__=_F
_VismCaleaEnable_Object=MibScalar
vismCaleaEnable=_VismCaleaEnable_Object((1,3,6,1,4,1,351,110,3,17,4,27),_VismCaleaEnable_Type())
vismCaleaEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:vismCaleaEnable.setStatus(_B)
class _VismMaxConfNum_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,50))
_VismMaxConfNum_Type.__name__=_D
_VismMaxConfNum_Object=MibScalar
vismMaxConfNum=_VismMaxConfNum_Object((1,3,6,1,4,1,351,110,3,17,4,28),_VismMaxConfNum_Type())
vismMaxConfNum.setMaxAccess(_C)
if mibBuilder.loadTexts:vismMaxConfNum.setStatus(_B)
class _VismLongDurationTimer_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,24))
_VismLongDurationTimer_Type.__name__=_D
_VismLongDurationTimer_Object=MibScalar
vismLongDurationTimer=_VismLongDurationTimer_Object((1,3,6,1,4,1,351,110,3,17,4,29),_VismLongDurationTimer_Type())
vismLongDurationTimer.setMaxAccess(_C)
if mibBuilder.loadTexts:vismLongDurationTimer.setStatus(_B)
class _VismContinuityCo1Timer_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,60))
_VismContinuityCo1Timer_Type.__name__=_D
_VismContinuityCo1Timer_Object=MibScalar
vismContinuityCo1Timer=_VismContinuityCo1Timer_Object((1,3,6,1,4,1,351,110,3,17,4,30),_VismContinuityCo1Timer_Type())
vismContinuityCo1Timer.setMaxAccess(_C)
if mibBuilder.loadTexts:vismContinuityCo1Timer.setStatus(_B)
class _VismContinuityCo2Timer_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,60))
_VismContinuityCo2Timer_Type.__name__=_D
_VismContinuityCo2Timer_Object=MibScalar
vismContinuityCo2Timer=_VismContinuityCo2Timer_Object((1,3,6,1,4,1,351,110,3,17,4,31),_VismContinuityCo2Timer_Type())
vismContinuityCo2Timer.setMaxAccess(_C)
if mibBuilder.loadTexts:vismContinuityCo2Timer.setStatus(_B)
class _VismReverseCotTone_Type(TruthValue):defaultValue=2
_VismReverseCotTone_Type.__name__=_F
_VismReverseCotTone_Object=MibScalar
vismReverseCotTone=_VismReverseCotTone_Object((1,3,6,1,4,1,351,110,3,17,4,32),_VismReverseCotTone_Type())
vismReverseCotTone.setMaxAccess(_C)
if mibBuilder.loadTexts:vismReverseCotTone.setStatus(_B)
class _VismSendDnEnable_Type(TruthValue):defaultValue=2
_VismSendDnEnable_Type.__name__=_F
_VismSendDnEnable_Object=MibScalar
vismSendDnEnable=_VismSendDnEnable_Object((1,3,6,1,4,1,351,110,3,17,4,33),_VismSendDnEnable_Type())
vismSendDnEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:vismSendDnEnable.setStatus(_B)
class _VismSendDataGramSize_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,20000))
_VismSendDataGramSize_Type.__name__=_D
_VismSendDataGramSize_Object=MibScalar
vismSendDataGramSize=_VismSendDataGramSize_Object((1,3,6,1,4,1,351,110,3,17,4,34),_VismSendDataGramSize_Type())
vismSendDataGramSize.setMaxAccess(_C)
if mibBuilder.loadTexts:vismSendDataGramSize.setStatus(_B)
class _VismOamLoopThreshold_Type(Integer32):defaultValue=5;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,60))
_VismOamLoopThreshold_Type.__name__=_D
_VismOamLoopThreshold_Object=MibScalar
vismOamLoopThreshold=_VismOamLoopThreshold_Object((1,3,6,1,4,1,351,110,3,17,4,35),_VismOamLoopThreshold_Type())
vismOamLoopThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:vismOamLoopThreshold.setStatus(_B)
class _VismFreeDs0Threshold_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,248))
_VismFreeDs0Threshold_Type.__name__=_D
_VismFreeDs0Threshold_Object=MibScalar
vismFreeDs0Threshold=_VismFreeDs0Threshold_Object((1,3,6,1,4,1,351,110,3,17,4,36),_VismFreeDs0Threshold_Type())
vismFreeDs0Threshold.setMaxAccess(_C)
if mibBuilder.loadTexts:vismFreeDs0Threshold.setStatus(_B)
class _VismCPUUtilizationThreshold_Type(Integer32):defaultValue=100;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,100))
_VismCPUUtilizationThreshold_Type.__name__=_D
_VismCPUUtilizationThreshold_Object=MibScalar
vismCPUUtilizationThreshold=_VismCPUUtilizationThreshold_Object((1,3,6,1,4,1,351,110,3,17,4,37),_VismCPUUtilizationThreshold_Type())
vismCPUUtilizationThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:vismCPUUtilizationThreshold.setStatus(_B)
class _VismMemoryUtilizationThreshold_Type(Integer32):defaultValue=100;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,100))
_VismMemoryUtilizationThreshold_Type.__name__=_D
_VismMemoryUtilizationThreshold_Object=MibScalar
vismMemoryUtilizationThreshold=_VismMemoryUtilizationThreshold_Object((1,3,6,1,4,1,351,110,3,17,4,38),_VismMemoryUtilizationThreshold_Type())
vismMemoryUtilizationThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:vismMemoryUtilizationThreshold.setStatus(_B)
class _VismDualToneDetect_Type(TruthValue):defaultValue=2
_VismDualToneDetect_Type.__name__=_F
_VismDualToneDetect_Object=MibScalar
vismDualToneDetect=_VismDualToneDetect_Object((1,3,6,1,4,1,351,110,3,17,4,39),_VismDualToneDetect_Type())
vismDualToneDetect.setMaxAccess(_C)
if mibBuilder.loadTexts:vismDualToneDetect.setStatus(_B)
class _VismAisSuppression_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_J,1),(_I,2)))
_VismAisSuppression_Type.__name__=_D
_VismAisSuppression_Object=MibScalar
vismAisSuppression=_VismAisSuppression_Object((1,3,6,1,4,1,351,110,3,17,4,40),_VismAisSuppression_Type())
vismAisSuppression.setMaxAccess(_C)
if mibBuilder.loadTexts:vismAisSuppression.setStatus(_G)
class _VismBearerIpPingEnable_Type(TruthValue):defaultValue=1
_VismBearerIpPingEnable_Type.__name__=_F
_VismBearerIpPingEnable_Object=MibScalar
vismBearerIpPingEnable=_VismBearerIpPingEnable_Object((1,3,6,1,4,1,351,110,3,17,4,41),_VismBearerIpPingEnable_Type())
vismBearerIpPingEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:vismBearerIpPingEnable.setStatus(_B)
class _VismTrapFilteringEnable_Type(TruthValue):defaultValue=2
_VismTrapFilteringEnable_Type.__name__=_F
_VismTrapFilteringEnable_Object=MibScalar
vismTrapFilteringEnable=_VismTrapFilteringEnable_Object((1,3,6,1,4,1,351,110,3,17,4,42),_VismTrapFilteringEnable_Type())
vismTrapFilteringEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:vismTrapFilteringEnable.setStatus(_B)
class _VismSplModemToneBitMap_Type(Bits):namedValues=NamedValues(('vism1560980Tone',0))
_VismSplModemToneBitMap_Type.__name__='Bits'
_VismSplModemToneBitMap_Object=MibScalar
vismSplModemToneBitMap=_VismSplModemToneBitMap_Object((1,3,6,1,4,1,351,110,3,17,4,43),_VismSplModemToneBitMap_Type())
vismSplModemToneBitMap.setMaxAccess(_C)
if mibBuilder.loadTexts:vismSplModemToneBitMap.setStatus(_B)
class _VismSSRCEnable_Type(TruthValue):defaultValue=2
_VismSSRCEnable_Type.__name__=_F
_VismSSRCEnable_Object=MibScalar
vismSSRCEnable=_VismSSRCEnable_Object((1,3,6,1,4,1,351,110,3,17,4,44),_VismSSRCEnable_Type())
vismSSRCEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:vismSSRCEnable.setStatus(_B)
class _VismOamLoopbackSetCLP_Type(TruthValue):defaultValue=1
_VismOamLoopbackSetCLP_Type.__name__=_F
_VismOamLoopbackSetCLP_Object=MibScalar
vismOamLoopbackSetCLP=_VismOamLoopbackSetCLP_Object((1,3,6,1,4,1,351,110,3,17,4,45),_VismOamLoopbackSetCLP_Type())
vismOamLoopbackSetCLP.setMaxAccess(_C)
if mibBuilder.loadTexts:vismOamLoopbackSetCLP.setStatus(_B)
class _VismPvcAlarmLogEnable_Type(TruthValue):defaultValue=2
_VismPvcAlarmLogEnable_Type.__name__=_F
_VismPvcAlarmLogEnable_Object=MibScalar
vismPvcAlarmLogEnable=_VismPvcAlarmLogEnable_Object((1,3,6,1,4,1,351,110,3,17,4,46),_VismPvcAlarmLogEnable_Type())
vismPvcAlarmLogEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:vismPvcAlarmLogEnable.setStatus(_B)
class _VismPvcAlarmLogAdminTimer_Type(Unsigned32):defaultValue=7200;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_VismPvcAlarmLogAdminTimer_Type.__name__=_V
_VismPvcAlarmLogAdminTimer_Object=MibScalar
vismPvcAlarmLogAdminTimer=_VismPvcAlarmLogAdminTimer_Object((1,3,6,1,4,1,351,110,3,17,4,47),_VismPvcAlarmLogAdminTimer_Type())
vismPvcAlarmLogAdminTimer.setMaxAccess(_C)
if mibBuilder.loadTexts:vismPvcAlarmLogAdminTimer.setStatus(_B)
if mibBuilder.loadTexts:vismPvcAlarmLogAdminTimer.setUnits('minutes')
class _VismPvcAlarmLogOperTimer_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_VismPvcAlarmLogOperTimer_Type.__name__=_V
_VismPvcAlarmLogOperTimer_Object=MibScalar
vismPvcAlarmLogOperTimer=_VismPvcAlarmLogOperTimer_Object((1,3,6,1,4,1,351,110,3,17,4,48),_VismPvcAlarmLogOperTimer_Type())
vismPvcAlarmLogOperTimer.setMaxAccess(_E)
if mibBuilder.loadTexts:vismPvcAlarmLogOperTimer.setStatus(_B)
if mibBuilder.loadTexts:vismPvcAlarmLogOperTimer.setUnits('minutes')
class _VismContinuityCheckCellEnable_Type(TruthValue):defaultValue=1
_VismContinuityCheckCellEnable_Type.__name__=_F
_VismContinuityCheckCellEnable_Object=MibScalar
vismContinuityCheckCellEnable=_VismContinuityCheckCellEnable_Object((1,3,6,1,4,1,351,110,3,17,4,49),_VismContinuityCheckCellEnable_Type())
vismContinuityCheckCellEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:vismContinuityCheckCellEnable.setStatus(_B)
_VismTrapObjGrp_ObjectIdentity=ObjectIdentity
vismTrapObjGrp=_VismTrapObjGrp_ObjectIdentity((1,3,6,1,4,1,351,110,3,17,5))
class _VismConfigChangeTypeBitMap_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_VismConfigChangeTypeBitMap_Type.__name__=_D
_VismConfigChangeTypeBitMap_Object=MibScalar
vismConfigChangeTypeBitMap=_VismConfigChangeTypeBitMap_Object((1,3,6,1,4,1,351,110,3,17,5,1),_VismConfigChangeTypeBitMap_Type())
vismConfigChangeTypeBitMap.setMaxAccess(_E)
if mibBuilder.loadTexts:vismConfigChangeTypeBitMap.setStatus(_B)
class _VismTrapIntIndex1_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_VismTrapIntIndex1_Type.__name__=_D
_VismTrapIntIndex1_Object=MibScalar
vismTrapIntIndex1=_VismTrapIntIndex1_Object((1,3,6,1,4,1,351,110,3,17,5,2),_VismTrapIntIndex1_Type())
vismTrapIntIndex1.setMaxAccess(_E)
if mibBuilder.loadTexts:vismTrapIntIndex1.setStatus(_B)
class _VismTrapIntIndex2_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_VismTrapIntIndex2_Type.__name__=_D
_VismTrapIntIndex2_Object=MibScalar
vismTrapIntIndex2=_VismTrapIntIndex2_Object((1,3,6,1,4,1,351,110,3,17,5,3),_VismTrapIntIndex2_Type())
vismTrapIntIndex2.setMaxAccess(_E)
if mibBuilder.loadTexts:vismTrapIntIndex2.setStatus(_B)
class _VismTrapStrIndex1_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,66))
_VismTrapStrIndex1_Type.__name__=_AA
_VismTrapStrIndex1_Object=MibScalar
vismTrapStrIndex1=_VismTrapStrIndex1_Object((1,3,6,1,4,1,351,110,3,17,5,4),_VismTrapStrIndex1_Type())
vismTrapStrIndex1.setMaxAccess(_E)
if mibBuilder.loadTexts:vismTrapStrIndex1.setStatus(_B)
class _VismTrapIntegerValue_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_VismTrapIntegerValue_Type.__name__=_D
_VismTrapIntegerValue_Object=MibScalar
vismTrapIntegerValue=_VismTrapIntegerValue_Object((1,3,6,1,4,1,351,110,3,17,5,5),_VismTrapIntegerValue_Type())
vismTrapIntegerValue.setMaxAccess('accessible-for-notify')
if mibBuilder.loadTexts:vismTrapIntegerValue.setStatus(_B)
_VismAal2Grp_ObjectIdentity=ObjectIdentity
vismAal2Grp=_VismAal2Grp_ObjectIdentity((1,3,6,1,4,1,351,110,3,17,6))
_VismAal2SubcellMuxing_Type=TruthValue
_VismAal2SubcellMuxing_Object=MibScalar
vismAal2SubcellMuxing=_VismAal2SubcellMuxing_Object((1,3,6,1,4,1,351,110,3,17,6,1),_VismAal2SubcellMuxing_Type())
vismAal2SubcellMuxing.setMaxAccess(_C)
if mibBuilder.loadTexts:vismAal2SubcellMuxing.setStatus(_B)
class _VismAal2DtmfRelay_Type(TruthValue):defaultValue=2
_VismAal2DtmfRelay_Type.__name__=_F
_VismAal2DtmfRelay_Object=MibScalar
vismAal2DtmfRelay=_VismAal2DtmfRelay_Object((1,3,6,1,4,1,351,110,3,17,6,2),_VismAal2DtmfRelay_Type())
vismAal2DtmfRelay.setMaxAccess(_C)
if mibBuilder.loadTexts:vismAal2DtmfRelay.setStatus(_B)
class _VismAal2CasTransport_Type(TruthValue):defaultValue=2
_VismAal2CasTransport_Type.__name__=_F
_VismAal2CasTransport_Object=MibScalar
vismAal2CasTransport=_VismAal2CasTransport_Object((1,3,6,1,4,1,351,110,3,17,6,3),_VismAal2CasTransport_Type())
vismAal2CasTransport.setMaxAccess(_C)
if mibBuilder.loadTexts:vismAal2CasTransport.setStatus(_B)
class _VismAal2Type3Redundancy_Type(TruthValue):defaultValue=1
_VismAal2Type3Redundancy_Type.__name__=_F
_VismAal2Type3Redundancy_Object=MibScalar
vismAal2Type3Redundancy=_VismAal2Type3Redundancy_Object((1,3,6,1,4,1,351,110,3,17,6,4),_VismAal2Type3Redundancy_Type())
vismAal2Type3Redundancy.setMaxAccess(_C)
if mibBuilder.loadTexts:vismAal2Type3Redundancy.setStatus(_B)
class _VismAal2VADTimer_Type(Integer32):defaultValue=250;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(250,65535))
_VismAal2VADTimer_Type.__name__=_D
_VismAal2VADTimer_Object=MibScalar
vismAal2VADTimer=_VismAal2VADTimer_Object((1,3,6,1,4,1,351,110,3,17,6,5),_VismAal2VADTimer_Type())
vismAal2VADTimer.setMaxAccess(_C)
if mibBuilder.loadTexts:vismAal2VADTimer.setStatus(_B)
class _VismAal2CidFillTimer_Type(Integer32):defaultValue=30;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(5,100))
_VismAal2CidFillTimer_Type.__name__=_D
_VismAal2CidFillTimer_Object=MibScalar
vismAal2CidFillTimer=_VismAal2CidFillTimer_Object((1,3,6,1,4,1,351,110,3,17,6,6),_VismAal2CidFillTimer_Type())
vismAal2CidFillTimer.setMaxAccess(_C)
if mibBuilder.loadTexts:vismAal2CidFillTimer.setStatus(_B)
_VismInteropGrp_ObjectIdentity=ObjectIdentity
vismInteropGrp=_VismInteropGrp_ObjectIdentity((1,3,6,1,4,1,351,110,3,17,7))
class _VismXgcpSdpOst_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_J,1),(_I,2)))
_VismXgcpSdpOst_Type.__name__=_D
_VismXgcpSdpOst_Object=MibScalar
vismXgcpSdpOst=_VismXgcpSdpOst_Object((1,3,6,1,4,1,351,110,3,17,7,1),_VismXgcpSdpOst_Type())
vismXgcpSdpOst.setMaxAccess(_C)
if mibBuilder.loadTexts:vismXgcpSdpOst.setStatus(_B)
class _VismDynamicPT_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_J,1),(_I,2)))
_VismDynamicPT_Type.__name__=_D
_VismDynamicPT_Object=MibScalar
vismDynamicPT=_VismDynamicPT_Object((1,3,6,1,4,1,351,110,3,17,7,2),_VismDynamicPT_Type())
vismDynamicPT.setMaxAccess(_C)
if mibBuilder.loadTexts:vismDynamicPT.setStatus(_B)
_VismSystemPerfStats_ObjectIdentity=ObjectIdentity
vismSystemPerfStats=_VismSystemPerfStats_ObjectIdentity((1,3,6,1,4,1,351,110,3,25))
class _VismCPUUtilization_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_VismCPUUtilization_Type.__name__=_D
_VismCPUUtilization_Object=MibScalar
vismCPUUtilization=_VismCPUUtilization_Object((1,3,6,1,4,1,351,110,3,25,1),_VismCPUUtilization_Type())
vismCPUUtilization.setMaxAccess(_E)
if mibBuilder.loadTexts:vismCPUUtilization.setStatus(_B)
class _VismMemoryUtilization_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_VismMemoryUtilization_Type.__name__=_D
_VismMemoryUtilization_Object=MibScalar
vismMemoryUtilization=_VismMemoryUtilization_Object((1,3,6,1,4,1,351,110,3,25,2),_VismMemoryUtilization_Type())
vismMemoryUtilization.setMaxAccess(_E)
if mibBuilder.loadTexts:vismMemoryUtilization.setStatus(_B)
class _VismSysPerfClrButton_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('noaction',1),('clear',2)))
_VismSysPerfClrButton_Type.__name__=_D
_VismSysPerfClrButton_Object=MibScalar
vismSysPerfClrButton=_VismSysPerfClrButton_Object((1,3,6,1,4,1,351,110,3,25,3),_VismSysPerfClrButton_Type())
vismSysPerfClrButton.setMaxAccess(_C)
if mibBuilder.loadTexts:vismSysPerfClrButton.setStatus(_B)
_VismCallStats_ObjectIdentity=ObjectIdentity
vismCallStats=_VismCallStats_ObjectIdentity((1,3,6,1,4,1,351,110,5,5,13))
class _VismTotalCalls_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_VismTotalCalls_Type.__name__=_D
_VismTotalCalls_Object=MibScalar
vismTotalCalls=_VismTotalCalls_Object((1,3,6,1,4,1,351,110,5,5,13,1),_VismTotalCalls_Type())
vismTotalCalls.setMaxAccess(_E)
if mibBuilder.loadTexts:vismTotalCalls.setStatus(_B)
class _VismSuccessfulCalls_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_VismSuccessfulCalls_Type.__name__=_D
_VismSuccessfulCalls_Object=MibScalar
vismSuccessfulCalls=_VismSuccessfulCalls_Object((1,3,6,1,4,1,351,110,5,5,13,2),_VismSuccessfulCalls_Type())
vismSuccessfulCalls.setMaxAccess(_E)
if mibBuilder.loadTexts:vismSuccessfulCalls.setStatus(_B)
class _VismFailedCalls_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_VismFailedCalls_Type.__name__=_D
_VismFailedCalls_Object=MibScalar
vismFailedCalls=_VismFailedCalls_Object((1,3,6,1,4,1,351,110,5,5,13,3),_VismFailedCalls_Type())
vismFailedCalls.setMaxAccess(_E)
if mibBuilder.loadTexts:vismFailedCalls.setStatus(_B)
class _VismCallStatsClrButton_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('noaction',1),('clear',2)))
_VismCallStatsClrButton_Type.__name__=_D
_VismCallStatsClrButton_Object=MibScalar
vismCallStatsClrButton=_VismCallStatsClrButton_Object((1,3,6,1,4,1,351,110,5,5,13,4),_VismCallStatsClrButton_Type())
vismCallStatsClrButton.setMaxAccess(_C)
if mibBuilder.loadTexts:vismCallStatsClrButton.setStatus(_B)
_CiscoVismModuleMIBConformance_ObjectIdentity=ObjectIdentity
ciscoVismModuleMIBConformance=_CiscoVismModuleMIBConformance_ObjectIdentity((1,3,6,1,4,1,351,150,82,2))
_CiscoVismModuleMIBGroups_ObjectIdentity=ObjectIdentity
ciscoVismModuleMIBGroups=_CiscoVismModuleMIBGroups_ObjectIdentity((1,3,6,1,4,1,351,150,82,2,1))
_CiscoVismModuleMIBCompliances_ObjectIdentity=ObjectIdentity
ciscoVismModuleMIBCompliances=_CiscoVismModuleMIBCompliances_ObjectIdentity((1,3,6,1,4,1,351,150,82,2,2))
ciscoVismPerfStatsGroup=ObjectGroup((1,3,6,1,4,1,351,150,82,2,1,1))
ciscoVismPerfStatsGroup.setObjects(*((_A,_AU),(_A,_AV),(_A,_AW)))
if mibBuilder.loadTexts:ciscoVismPerfStatsGroup.setStatus(_B)
ciscoVismCallStatsGroup=ObjectGroup((1,3,6,1,4,1,351,150,82,2,1,2))
ciscoVismCallStatsGroup.setObjects(*((_A,_AX),(_A,_AY),(_A,_AZ),(_A,_Aa)))
if mibBuilder.loadTexts:ciscoVismCallStatsGroup.setStatus(_B)
ciscoVismIpGroup=ObjectGroup((1,3,6,1,4,1,351,150,82,2,1,3))
ciscoVismIpGroup.setObjects(*((_A,_Ab),(_A,_Ac),(_A,_Ad),(_A,_Ae),(_A,_Af)))
if mibBuilder.loadTexts:ciscoVismIpGroup.setStatus(_B)
ciscoVismVoIpGroup=ObjectGroup((1,3,6,1,4,1,351,150,82,2,1,4))
ciscoVismVoIpGroup.setObjects(*((_A,_Ag),(_A,_Ah),(_A,_Ai),(_A,_Aj),(_A,_Ak),(_A,_Al),(_A,_Am),(_A,_An),(_A,_Ao),(_A,_Ap),(_A,_Aq),(_A,_Ar),(_A,_As),(_A,_At),(_A,_Au)))
if mibBuilder.loadTexts:ciscoVismVoIpGroup.setStatus(_B)
ciscoVismDspGroup=ObjectGroup((1,3,6,1,4,1,351,150,82,2,1,5))
ciscoVismDspGroup.setObjects(*((_A,_Av),(_A,'vismERL'),(_A,_Aw),(_A,_Ax),(_A,_Ay),(_A,_Az),(_A,_A_)))
if mibBuilder.loadTexts:ciscoVismDspGroup.setStatus(_B)
ciscoVismSystemGroup=ObjectGroup((1,3,6,1,4,1,351,150,82,2,1,6))
ciscoVismSystemGroup.setObjects(*((_A,_W),(_A,_X),(_A,_Y),(_A,_Z),(_A,_a),(_A,_b),(_A,_c),(_A,_d),(_A,_e),(_A,_f),(_A,_g),(_A,_h),(_A,_i),(_A,_j),(_A,_k),(_A,_l),(_A,_m),(_A,_n),(_A,_o),(_A,_p),(_A,_q),(_A,_r),(_A,_s),(_A,_t),(_A,_u),(_A,_v),(_A,_w),(_A,_x),(_A,_y),(_A,_z),(_A,_A0),(_A,_A1),(_A,_A2),(_A,_A3),(_A,_A4),(_A,_A5),(_A,_A6),(_A,_B0)))
if mibBuilder.loadTexts:ciscoVismSystemGroup.setStatus(_G)
ciscoVismInteropGroup=ObjectGroup((1,3,6,1,4,1,351,150,82,2,1,7))
ciscoVismInteropGroup.setObjects(*((_A,_B1),(_A,_B2)))
if mibBuilder.loadTexts:ciscoVismInteropGroup.setStatus(_B)
ciscoVismTrapObjGroup=ObjectGroup((1,3,6,1,4,1,351,150,82,2,1,8))
ciscoVismTrapObjGroup.setObjects(*((_A,_B3),(_A,_B4),(_A,_B5),(_A,_B6)))
if mibBuilder.loadTexts:ciscoVismTrapObjGroup.setStatus(_B)
ciscoVismAal2Group=ObjectGroup((1,3,6,1,4,1,351,150,82,2,1,9))
ciscoVismAal2Group.setObjects(*((_A,_B7),(_A,_B8),(_A,_B9),(_A,_BA),(_A,_BB),(_A,_BC)))
if mibBuilder.loadTexts:ciscoVismAal2Group.setStatus(_B)
ciscoVismDspDeprecatedGroup=ObjectGroup((1,3,6,1,4,1,351,150,82,2,1,10))
ciscoVismDspDeprecatedGroup.setObjects(*((_A,_BD),(_A,_BE),(_A,_BF),(_A,_BG)))
if mibBuilder.loadTexts:ciscoVismDspDeprecatedGroup.setStatus(_G)
ciscoVismSystemDeprecatedGroup=ObjectGroup((1,3,6,1,4,1,351,150,82,2,1,11))
ciscoVismSystemDeprecatedGroup.setObjects((_A,_BH))
if mibBuilder.loadTexts:ciscoVismSystemDeprecatedGroup.setStatus(_G)
ciscoVismVoIpDeprecateGroup=ObjectGroup((1,3,6,1,4,1,351,150,82,2,1,12))
ciscoVismVoIpDeprecateGroup.setObjects((_A,_BI))
if mibBuilder.loadTexts:ciscoVismVoIpDeprecateGroup.setStatus(_G)
ciscoVismSystemGroup1=ObjectGroup((1,3,6,1,4,1,351,150,82,2,1,13))
ciscoVismSystemGroup1.setObjects(*((_A,_W),(_A,_X),(_A,_Y),(_A,_Z),(_A,_a),(_A,_b),(_A,_c),(_A,_d),(_A,_e),(_A,_f),(_A,_g),(_A,_h),(_A,_i),(_A,_j),(_A,_k),(_A,_l),(_A,_m),(_A,_n),(_A,_o),(_A,_p),(_A,_q),(_A,_r),(_A,_s),(_A,_t),(_A,_u),(_A,_v),(_A,_w),(_A,_x),(_A,_y),(_A,_z),(_A,_A0),(_A,_A1),(_A,_A2),(_A,_A3),(_A,_A4),(_A,_A5),(_A,_A6)))
if mibBuilder.loadTexts:ciscoVismSystemGroup1.setStatus(_B)
ciscoVismSystemFeatureGroup=ObjectGroup((1,3,6,1,4,1,351,150,82,2,1,14))
ciscoVismSystemFeatureGroup.setObjects(*((_A,_A7),(_A,_A8)))
if mibBuilder.loadTexts:ciscoVismSystemFeatureGroup.setStatus(_G)
ciscoVismTrapVarbindGroup=ObjectGroup((1,3,6,1,4,1,351,150,82,2,1,15))
ciscoVismTrapVarbindGroup.setObjects((_A,_BJ))
if mibBuilder.loadTexts:ciscoVismTrapVarbindGroup.setStatus(_B)
ciscoVismSystemFeatureGroupRev1=ObjectGroup((1,3,6,1,4,1,351,150,82,2,1,16))
ciscoVismSystemFeatureGroupRev1.setObjects(*((_A,_A7),(_A,_A8),(_A,_BK),(_A,_BL)))
if mibBuilder.loadTexts:ciscoVismSystemFeatureGroupRev1.setStatus(_B)
ciscoVismSystemGroupSup1=ObjectGroup((1,3,6,1,4,1,351,150,82,2,1,17))
ciscoVismSystemGroupSup1.setObjects(*((_A,_BM),(_A,_BN),(_A,_BO),(_A,_BP),(_A,_BQ)))
if mibBuilder.loadTexts:ciscoVismSystemGroupSup1.setStatus(_B)
ciscoVismDspGroupSup1=ObjectGroup((1,3,6,1,4,1,351,150,82,2,1,18))
ciscoVismDspGroupSup1.setObjects(*((_A,_BR),(_A,_BS)))
if mibBuilder.loadTexts:ciscoVismDspGroupSup1.setStatus(_B)
ciscoVismModuleCompliance=ModuleCompliance((1,3,6,1,4,1,351,150,82,2,2,1))
ciscoVismModuleCompliance.setObjects(*((_A,_K),(_A,_L),(_A,_M),(_A,_N),(_A,_O),(_A,_BT),(_A,_P),(_A,_Q),(_A,_R)))
if mibBuilder.loadTexts:ciscoVismModuleCompliance.setStatus(_G)
ciscoVismModuleCompliance1=ModuleCompliance((1,3,6,1,4,1,351,150,82,2,2,2))
ciscoVismModuleCompliance1.setObjects(*((_A,_K),(_A,_L),(_A,_M),(_A,_N),(_A,_O),(_A,_S),(_A,_P),(_A,_Q),(_A,_R)))
if mibBuilder.loadTexts:ciscoVismModuleCompliance1.setStatus(_G)
ciscoVismModuleComplianceRev2=ModuleCompliance((1,3,6,1,4,1,351,150,82,2,2,3))
ciscoVismModuleComplianceRev2.setObjects(*((_A,_K),(_A,_L),(_A,_M),(_A,_N),(_A,_O),(_A,_S),(_A,_P),(_A,_Q),(_A,_R),(_A,_BU),(_A,_U)))
if mibBuilder.loadTexts:ciscoVismModuleComplianceRev2.setStatus(_G)
ciscoVismModuleComplianceRev3=ModuleCompliance((1,3,6,1,4,1,351,150,82,2,2,4))
ciscoVismModuleComplianceRev3.setObjects(*((_A,_K),(_A,_L),(_A,_M),(_A,_N),(_A,_O),(_A,_S),(_A,_P),(_A,_Q),(_A,_R),(_A,_A9),(_A,_U)))
if mibBuilder.loadTexts:ciscoVismModuleComplianceRev3.setStatus(_G)
ciscoVismModuleComplianceRev4=ModuleCompliance((1,3,6,1,4,1,351,150,82,2,2,5))
ciscoVismModuleComplianceRev4.setObjects(*((_A,_K),(_A,_L),(_A,_M),(_A,_N),(_A,_O),(_A,_S),(_A,_P),(_A,_Q),(_A,_R),(_A,_A9),(_A,_U),(_A,_BV),(_A,_BW)))
if mibBuilder.loadTexts:ciscoVismModuleComplianceRev4.setStatus(_B)
mibBuilder.exportSymbols(_A,**{_AK:VismFaxDeJitterMode,_AL:VismFaxDeJitterInitDelay,'vismConfig':vismConfig,'vismIpGrp':vismIpGrp,_Ab:vismIpAddress,_Ac:vismSubNetMask,_Ad:vismControlTos,_Ae:vismBearerIpAddress,_Af:vismBearerSubNetMask,'vismVoIpGrp':vismVoIpGrp,_Ag:vismBearerTos,_Ah:vismRtcpRepInterval,_Ai:vismRtpReceiveTimer,_BI:vismPacketizationPeriod,_Aj:vismVoIpDtmfRelay,_Ak:vismVoIpCasTransport,_Al:vismVoIpTripleRedundancy,_Am:vismVoIpVADTimer,_An:vismVoIpNTECapabilityNegotiate,_Ao:vismVoIpSIDPayloadType,_Ap:vismVoIpDPvcOamCellGap,_Aq:vismVoIpDPvcRetryCnt,_Ar:vismVoIpDPvcRecoverCnt,_As:vismRtcpRecvMultiplier,_At:vismVoIpLapdTrunkPVC,_Au:vismVoIpEventNegotiationPolicy,'vismDspGrp':vismDspGrp,_BD:vismEcanCnfIdlePattern,_BE:vismEcanCnfIdleDirection,_Av:vismCompCnfPacketSize,'vismERL':vismERL,_BF:vismJitterDelayMode,_BG:vismJitterInitialDelay,_Aw:vismAdaptiveGainControl,_Ax:vismDspHealth,_Ay:vismUpspeedCodec,_Az:vismPayloadType,_A_:vismDSPHeartbeat,_BR:vismFaxDeJitterMode,_BS:vismFaxDeJitterInitialDelay,'vismSystemGrp':vismSystemGrp,_W:vismDaughterCardSerialNum,_X:vismDaughterCardDescription,_Y:vismDaughterCardHWRev,_Z:vismEcanEncoding,_a:vismMode,_BH:vismPrevMode,_b:vismCacEnable,_c:vismAvailableDs0Count,_d:vismAppliedTemplate,_e:vismTftpServerDn,_f:vismXgcpBearerNetworkType,_g:vismXgcpBearerVCType,_h:vismXgcpBearerConnectionType,_i:vismBearerContinuityTimer,_j:vismCodecNegotiationOption,_k:vismProfileNegotiationOption,_l:vismCarrierLossPolicy,_m:vismCacRejectionPolicy,_n:vismExtDnsServerDn,_o:vismFeatureBitMap,_p:vismVADTolerance,_q:vismVADDutyCycle,_r:vismAggregateTrafficClipping,_s:vismAggregateSvcBandwidth,_t:vismBearerContinuityTest,_u:vismCaleaEnable,_v:vismMaxConfNum,_w:vismLongDurationTimer,_x:vismContinuityCo1Timer,_y:vismContinuityCo2Timer,_z:vismReverseCotTone,_A0:vismSendDnEnable,_A1:vismSendDataGramSize,_A2:vismOamLoopThreshold,_A3:vismFreeDs0Threshold,_A4:vismCPUUtilizationThreshold,_A5:vismMemoryUtilizationThreshold,_A6:vismDualToneDetect,_B0:vismAisSuppression,_A7:vismBearerIpPingEnable,_A8:vismTrapFilteringEnable,_BK:vismSplModemToneBitMap,_BL:vismSSRCEnable,_BM:vismOamLoopbackSetCLP,_BN:vismPvcAlarmLogEnable,_BO:vismPvcAlarmLogAdminTimer,_BP:vismPvcAlarmLogOperTimer,_BQ:vismContinuityCheckCellEnable,'vismTrapObjGrp':vismTrapObjGrp,_B3:vismConfigChangeTypeBitMap,_B4:vismTrapIntIndex1,_B5:vismTrapIntIndex2,_B6:vismTrapStrIndex1,_BJ:vismTrapIntegerValue,'vismAal2Grp':vismAal2Grp,_B7:vismAal2SubcellMuxing,_B8:vismAal2DtmfRelay,_B9:vismAal2CasTransport,_BA:vismAal2Type3Redundancy,_BB:vismAal2VADTimer,_BC:vismAal2CidFillTimer,'vismInteropGrp':vismInteropGrp,_B1:vismXgcpSdpOst,_B2:vismDynamicPT,'vismSystemPerfStats':vismSystemPerfStats,_AU:vismCPUUtilization,_AV:vismMemoryUtilization,_AW:vismSysPerfClrButton,'vismCallStats':vismCallStats,_AX:vismTotalCalls,_AY:vismSuccessfulCalls,_AZ:vismFailedCalls,_Aa:vismCallStatsClrButton,'ciscoVismModuleMIB':ciscoVismModuleMIB,'ciscoVismModuleMIBConformance':ciscoVismModuleMIBConformance,'ciscoVismModuleMIBGroups':ciscoVismModuleMIBGroups,_K:ciscoVismPerfStatsGroup,_L:ciscoVismCallStatsGroup,_M:ciscoVismIpGroup,_N:ciscoVismVoIpGroup,_O:ciscoVismDspGroup,_BT:ciscoVismSystemGroup,_P:ciscoVismInteropGroup,_Q:ciscoVismTrapObjGroup,_R:ciscoVismAal2Group,'ciscoVismDspDeprecatedGroup':ciscoVismDspDeprecatedGroup,'ciscoVismSystemDeprecatedGroup':ciscoVismSystemDeprecatedGroup,'ciscoVismVoIpDeprecateGroup':ciscoVismVoIpDeprecateGroup,_S:ciscoVismSystemGroup1,_BU:ciscoVismSystemFeatureGroup,_U:ciscoVismTrapVarbindGroup,_A9:ciscoVismSystemFeatureGroupRev1,_BW:ciscoVismSystemGroupSup1,_BV:ciscoVismDspGroupSup1,'ciscoVismModuleMIBCompliances':ciscoVismModuleMIBCompliances,'ciscoVismModuleCompliance':ciscoVismModuleCompliance,'ciscoVismModuleCompliance1':ciscoVismModuleCompliance1,'ciscoVismModuleComplianceRev2':ciscoVismModuleComplianceRev2,'ciscoVismModuleComplianceRev3':ciscoVismModuleComplianceRev3,'ciscoVismModuleComplianceRev4':ciscoVismModuleComplianceRev4})