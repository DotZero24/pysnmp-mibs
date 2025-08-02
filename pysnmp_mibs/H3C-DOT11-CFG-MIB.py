_At='h3cDot11CurrConflictTemplateSSID'
_As='h3cDot11PreConflictTemplateSSID'
_Ar='h3cDot11ConfigureAPMacAddress'
_Aq='h3cDot11ConfigureRadioID'
_Ap='h3cDot11ConfigureAPID'
_Ao='h3cDot11ConflictCipherIdx'
_An='h3cDot11CurrConflictTemplateNum'
_Am='h3cDot11PreConflictTemplateNum'
_Al='h3cDot11SecurityCiphers'
_Ak='h3cDot11LocalACTemplateName'
_Aj='h3cDot11nRadioCfg2RadioIDIndex'
_Ai='h3cDot11nRadioCfg2APIDIndex'
_Ah='h3cDot11RadioWDSIndex'
_Ag='h3cDot11nRadioCfgIndex'
_Af='h3cDot11WlanMeshIfNumber'
_Ae='h3cDot11WlanEthernetIfNumber'
_Ad='h3cDot11WlanBssIfNumber'
_Ac='h3cDot11WlanEssIfNumber'
_Ab='h3cDot11RadioTypeID'
_Aa='h3cDot11RadioIntfBindSvcPlcyID'
_AZ='h3cDot11RadioSSIDWLANID'
_AY='h3cDot11RadioSSIDRadioID'
_AX='h3cDot11RadioSSIDSerialID'
_AW='h3cDot11RCRadioID'
_AV='h3cDot11RCAPSerialID'
_AU='h3cDot11APServiceVlanSPID'
_AT='h3cDot11APServiceVlanSerialID'
_AS='h3cDot11APSetIfIndex'
_AR='genericInterferer'
_AQ='freqHopperXbox'
_AP='freqHopperCordlessNetwork'
_AO='freqHopperCordlessBase'
_AN='freqHopperOthers'
_AM='fixedFreqAudio'
_AL='fixedFreqVideo'
_AK='fixedFreqCordlessPhone'
_AJ='fixedFreqOthers'
_AI='bluetooth'
_AH='microwaveInverter'
_AG='microwave'
_AF='dhcpAlloc'
_AE='h3cDot11APTemplateName'
_AD='h3cDot11SrvL2AuthenID'
_AC='userLoginTxKeyTypeRsaRC4Key'
_AB='userLoginTxKeyTypeDot11Key'
_AA='userLoginTxKeyTypeNone'
_A9='userLoginSecureExtOrPsk'
_A8='macAddressAndPsk'
_A7='userLoginSecureExt'
_A6='noRestrictions'
_A5='h3cDot11SecurityServicePolicyID'
_A4='h3cDot11RPRadioID'
_A3='h3cDot11RPAPSerialID'
_A2='h3cDot11ServicePolicyExtID'
_A1='millisecond'
_A0='h3cDot11RadioPolicyName'
_z='ifIndex'
_y='IF-MIB'
_x='H3cDot11TunnelSecSchemType'
_w='H3cDot11ChannelScopeType'
_v='h3cDot11SSIDName'
_u='mode80and80'
_t='mode160'
_s='mode80'
_r='mode40'
_q='mode20'
_p='h3cDot11RadioIfIdx'
_o='h3cDot11CfgServicePolicyID'
_n='h3cDot11APTemplateNameCfg'
_m='pskKeyModeRawKey'
_l='pskKeyModePassPhrase'
_k='pskKeyModeNone'
_j='wlanex'
_i='h3cDot11ServicePolicyID'
_h='hybrid'
_g='DisplayString'
_f='Bits'
_e='h3cDot11APElementIndex'
_d='H3cDot11CirMode'
_c='H3C-DOT11-REF-MIB'
_b='h3cDot11SIDAPSerialID'
_a='h3cDot11CfgRadioID'
_Z='none'
_Y='monitor'
_X='onepercent'
_W='H3cDot11TruthValueCM'
_V='H3cDot11PreambleType'
_U='psk'
_T='on'
_S='off'
_R='dbm'
_Q='Kbps'
_P='byte'
_O='disable'
_N='enable'
_M='normal'
_L='accessible-for-notify'
_K='Unsigned32'
_J='second'
_I='read-only'
_H='OctetString'
_G='TruthValue'
_F='not-accessible'
_E='H3C-DOT11-CFG-MIB'
_D='read-create'
_C='Integer32'
_B='read-write'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_H,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
H3cDot11AuthenType,H3cDot11ChannelScopeType,H3cDot11CirMode,H3cDot11ObjectIDType,H3cDot11PreambleType,H3cDot11RadioElementIndex,H3cDot11RadioScopeType,H3cDot11RadioType,H3cDot11RadioType2,H3cDot11SSIDEncryptModeType,H3cDot11SSIDStringType,H3cDot11SecIEStatusType,H3cDot11ServicePolicyIDType,H3cDot11TruthValueCM,H3cDot11TunnelSecSchemType,H3cDot11TxPwrLevelScopeType,H3cDot11WorkMode,h3cDot11,h3cDot11APElementIndex=mibBuilder.importSymbols(_c,'H3cDot11AuthenType',_w,_d,'H3cDot11ObjectIDType',_V,'H3cDot11RadioElementIndex','H3cDot11RadioScopeType','H3cDot11RadioType','H3cDot11RadioType2','H3cDot11SSIDEncryptModeType','H3cDot11SSIDStringType','H3cDot11SecIEStatusType','H3cDot11ServicePolicyIDType',_W,_x,'H3cDot11TxPwrLevelScopeType','H3cDot11WorkMode','h3cDot11',_e)
ifIndex,=mibBuilder.importSymbols(_y,_z)
InetAddress,=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI',_f,'Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_K,'iso')
DateAndTime,DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime',_g,'MacAddress','PhysAddress','RowStatus','TextualConvention',_G)
h3cDot11CFG=ModuleIdentity((1,3,6,1,4,1,2011,10,2,75,4))
if mibBuilder.loadTexts:h3cDot11CFG.setRevisions(('2017-10-09 18:00','2016-03-11 18:00','2014-09-19 18:00','2010-09-25 18:00','2010-09-02 18:00','2009-07-29 18:00','2009-05-07 20:00','2009-03-20 15:30','2008-11-07 15:30','2008-07-09 18:00','2008-02-25 18:00','2007-12-21 18:00','2007-10-09 16:55','2007-06-19 18:00','2007-04-27 20:00','2007-02-01 20:00','2006-05-10 19:00'))
_H3cDot11GlobeConfigGroup_ObjectIdentity=ObjectIdentity
h3cDot11GlobeConfigGroup=_H3cDot11GlobeConfigGroup_ObjectIdentity((1,3,6,1,4,1,2011,10,2,75,4,1))
class _H3cDot11GlobalCountryCode_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(3,3));fixedLength=3
_H3cDot11GlobalCountryCode_Type.__name__=_H
_H3cDot11GlobalCountryCode_Object=MibScalar
h3cDot11GlobalCountryCode=_H3cDot11GlobalCountryCode_Object((1,3,6,1,4,1,2011,10,2,75,4,1,1),_H3cDot11GlobalCountryCode_Type())
h3cDot11GlobalCountryCode.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11GlobalCountryCode.setStatus(_A)
class _H3cDot11StaKeepALiveTimerIntvl_Type(Unsigned32):defaultValue=0
_H3cDot11StaKeepALiveTimerIntvl_Type.__name__=_K
_H3cDot11StaKeepALiveTimerIntvl_Object=MibScalar
h3cDot11StaKeepALiveTimerIntvl=_H3cDot11StaKeepALiveTimerIntvl_Object((1,3,6,1,4,1,2011,10,2,75,4,1,2),_H3cDot11StaKeepALiveTimerIntvl_Type())
h3cDot11StaKeepALiveTimerIntvl.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11StaKeepALiveTimerIntvl.setStatus(_A)
if mibBuilder.loadTexts:h3cDot11StaKeepALiveTimerIntvl.setUnits(_J)
_H3cDot11StaIdleTimerIntvl_Type=Integer32
_H3cDot11StaIdleTimerIntvl_Object=MibScalar
h3cDot11StaIdleTimerIntvl=_H3cDot11StaIdleTimerIntvl_Object((1,3,6,1,4,1,2011,10,2,75,4,1,3),_H3cDot11StaIdleTimerIntvl_Type())
h3cDot11StaIdleTimerIntvl.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11StaIdleTimerIntvl.setStatus(_A)
if mibBuilder.loadTexts:h3cDot11StaIdleTimerIntvl.setUnits(_J)
class _H3cDot11BroadcastProbeReply_Type(TruthValue):defaultValue=1
_H3cDot11BroadcastProbeReply_Type.__name__=_G
_H3cDot11BroadcastProbeReply_Object=MibScalar
h3cDot11BroadcastProbeReply=_H3cDot11BroadcastProbeReply_Object((1,3,6,1,4,1,2011,10,2,75,4,1,4),_H3cDot11BroadcastProbeReply_Type())
h3cDot11BroadcastProbeReply.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11BroadcastProbeReply.setStatus(_A)
class _H3cDot11APScanMode_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('active',1),('passive',2)))
_H3cDot11APScanMode_Type.__name__=_C
_H3cDot11APScanMode_Object=MibScalar
h3cDot11APScanMode=_H3cDot11APScanMode_Object((1,3,6,1,4,1,2011,10,2,75,4,1,5),_H3cDot11APScanMode_Type())
h3cDot11APScanMode.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11APScanMode.setStatus(_A)
_H3cDot11ACCtrlTunnelSecSupport_Type=H3cDot11TunnelSecSchemType
_H3cDot11ACCtrlTunnelSecSupport_Object=MibScalar
h3cDot11ACCtrlTunnelSecSupport=_H3cDot11ACCtrlTunnelSecSupport_Object((1,3,6,1,4,1,2011,10,2,75,4,1,6),_H3cDot11ACCtrlTunnelSecSupport_Type())
h3cDot11ACCtrlTunnelSecSupport.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11ACCtrlTunnelSecSupport.setStatus(_A)
class _H3cDot11ACDataTunnelSecSupport_Type(H3cDot11TunnelSecSchemType):defaultValue=1
_H3cDot11ACDataTunnelSecSupport_Type.__name__=_x
_H3cDot11ACDataTunnelSecSupport_Object=MibScalar
h3cDot11ACDataTunnelSecSupport=_H3cDot11ACDataTunnelSecSupport_Object((1,3,6,1,4,1,2011,10,2,75,4,1,7),_H3cDot11ACDataTunnelSecSupport_Type())
h3cDot11ACDataTunnelSecSupport.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11ACDataTunnelSecSupport.setStatus(_A)
class _H3cDot11ACAutoAPSupport_Type(TruthValue):defaultValue=2
_H3cDot11ACAutoAPSupport_Type.__name__=_G
_H3cDot11ACAutoAPSupport_Object=MibScalar
h3cDot11ACAutoAPSupport=_H3cDot11ACAutoAPSupport_Object((1,3,6,1,4,1,2011,10,2,75,4,1,8),_H3cDot11ACAutoAPSupport_Type())
h3cDot11ACAutoAPSupport.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11ACAutoAPSupport.setStatus(_A)
class _H3cDot11AutoAPName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,127))
_H3cDot11AutoAPName_Type.__name__=_H
_H3cDot11AutoAPName_Object=MibScalar
h3cDot11AutoAPName=_H3cDot11AutoAPName_Object((1,3,6,1,4,1,2011,10,2,75,4,1,9),_H3cDot11AutoAPName_Type())
h3cDot11AutoAPName.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11AutoAPName.setStatus(_A)
class _H3cDot11PersistentName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,127))
_H3cDot11PersistentName_Type.__name__=_H
_H3cDot11PersistentName_Object=MibScalar
h3cDot11PersistentName=_H3cDot11PersistentName_Object((1,3,6,1,4,1,2011,10,2,75,4,1,10),_H3cDot11PersistentName_Type())
h3cDot11PersistentName.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11PersistentName.setStatus(_A)
_H3cDot11IntfTrapThreshold_Type=Integer32
_H3cDot11IntfTrapThreshold_Object=MibScalar
h3cDot11IntfTrapThreshold=_H3cDot11IntfTrapThreshold_Object((1,3,6,1,4,1,2011,10,2,75,4,1,11),_H3cDot11IntfTrapThreshold_Type())
h3cDot11IntfTrapThreshold.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11IntfTrapThreshold.setStatus(_A)
if mibBuilder.loadTexts:h3cDot11IntfTrapThreshold.setUnits(_R)
class _H3cDot11MonitorInterval_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(5,15))
_H3cDot11MonitorInterval_Type.__name__=_K
_H3cDot11MonitorInterval_Object=MibScalar
h3cDot11MonitorInterval=_H3cDot11MonitorInterval_Object((1,3,6,1,4,1,2011,10,2,75,4,1,12),_H3cDot11MonitorInterval_Type())
h3cDot11MonitorInterval.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11MonitorInterval.setStatus(_A)
if mibBuilder.loadTexts:h3cDot11MonitorInterval.setUnits('minute')
class _H3cDot11SampleInterval_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(10,300))
_H3cDot11SampleInterval_Type.__name__=_K
_H3cDot11SampleInterval_Object=MibScalar
h3cDot11SampleInterval=_H3cDot11SampleInterval_Object((1,3,6,1,4,1,2011,10,2,75,4,1,13),_H3cDot11SampleInterval_Type())
h3cDot11SampleInterval.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11SampleInterval.setStatus(_A)
if mibBuilder.loadTexts:h3cDot11SampleInterval.setUnits(_J)
class _H3cDot11ChnlSwitChkInterval_Type(Unsigned32):defaultValue=8;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(8,180))
_H3cDot11ChnlSwitChkInterval_Type.__name__=_K
_H3cDot11ChnlSwitChkInterval_Object=MibScalar
h3cDot11ChnlSwitChkInterval=_H3cDot11ChnlSwitChkInterval_Object((1,3,6,1,4,1,2011,10,2,75,4,1,14),_H3cDot11ChnlSwitChkInterval_Type())
h3cDot11ChnlSwitChkInterval.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11ChnlSwitChkInterval.setStatus(_A)
if mibBuilder.loadTexts:h3cDot11ChnlSwitChkInterval.setUnits('minute')
class _H3cDot11APUserUplimit_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_H3cDot11APUserUplimit_Type.__name__=_K
_H3cDot11APUserUplimit_Object=MibScalar
h3cDot11APUserUplimit=_H3cDot11APUserUplimit_Object((1,3,6,1,4,1,2011,10,2,75,4,1,15),_H3cDot11APUserUplimit_Type())
h3cDot11APUserUplimit.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11APUserUplimit.setStatus(_A)
class _H3cDot11APL2IsolateEnable_Type(TruthValue):defaultValue=2
_H3cDot11APL2IsolateEnable_Type.__name__=_G
_H3cDot11APL2IsolateEnable_Object=MibScalar
h3cDot11APL2IsolateEnable=_H3cDot11APL2IsolateEnable_Object((1,3,6,1,4,1,2011,10,2,75,4,1,16),_H3cDot11APL2IsolateEnable_Type())
h3cDot11APL2IsolateEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11APL2IsolateEnable.setStatus(_A)
_H3cDot11APBSSIDSupportNum_Type=Integer32
_H3cDot11APBSSIDSupportNum_Object=MibScalar
h3cDot11APBSSIDSupportNum=_H3cDot11APBSSIDSupportNum_Object((1,3,6,1,4,1,2011,10,2,75,4,1,17),_H3cDot11APBSSIDSupportNum_Type())
h3cDot11APBSSIDSupportNum.setMaxAccess(_I)
if mibBuilder.loadTexts:h3cDot11APBSSIDSupportNum.setStatus(_A)
_H3cDot11APLastUpdateStatTime_Type=DateAndTime
_H3cDot11APLastUpdateStatTime_Object=MibScalar
h3cDot11APLastUpdateStatTime=_H3cDot11APLastUpdateStatTime_Object((1,3,6,1,4,1,2011,10,2,75,4,1,18),_H3cDot11APLastUpdateStatTime_Type())
h3cDot11APLastUpdateStatTime.setMaxAccess(_I)
if mibBuilder.loadTexts:h3cDot11APLastUpdateStatTime.setStatus(_A)
class _H3cDot11APDoSProtectEnable_Type(TruthValue):defaultValue=2
_H3cDot11APDoSProtectEnable_Type.__name__=_G
_H3cDot11APDoSProtectEnable_Object=MibScalar
h3cDot11APDoSProtectEnable=_H3cDot11APDoSProtectEnable_Object((1,3,6,1,4,1,2011,10,2,75,4,1,19),_H3cDot11APDoSProtectEnable_Type())
h3cDot11APDoSProtectEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11APDoSProtectEnable.setStatus(_A)
class _H3cDot11MaxAPPerIf_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_H3cDot11MaxAPPerIf_Type.__name__=_K
_H3cDot11MaxAPPerIf_Object=MibScalar
h3cDot11MaxAPPerIf=_H3cDot11MaxAPPerIf_Object((1,3,6,1,4,1,2011,10,2,75,4,1,20),_H3cDot11MaxAPPerIf_Type())
h3cDot11MaxAPPerIf.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11MaxAPPerIf.setStatus(_A)
_H3cDot11SampleTimeStamp_Type=DateAndTime
_H3cDot11SampleTimeStamp_Object=MibScalar
h3cDot11SampleTimeStamp=_H3cDot11SampleTimeStamp_Object((1,3,6,1,4,1,2011,10,2,75,4,1,21),_H3cDot11SampleTimeStamp_Type())
h3cDot11SampleTimeStamp.setMaxAccess(_I)
if mibBuilder.loadTexts:h3cDot11SampleTimeStamp.setStatus(_A)
class _H3cDot11UplinkTrackId_Type(Unsigned32):defaultValue=0
_H3cDot11UplinkTrackId_Type.__name__=_K
_H3cDot11UplinkTrackId_Object=MibScalar
h3cDot11UplinkTrackId=_H3cDot11UplinkTrackId_Object((1,3,6,1,4,1,2011,10,2,75,4,1,22),_H3cDot11UplinkTrackId_Type())
h3cDot11UplinkTrackId.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11UplinkTrackId.setStatus(_A)
class _H3cDot11RtCollectSwitch_Type(TruthValue):defaultValue=2
_H3cDot11RtCollectSwitch_Type.__name__=_G
_H3cDot11RtCollectSwitch_Object=MibScalar
h3cDot11RtCollectSwitch=_H3cDot11RtCollectSwitch_Object((1,3,6,1,4,1,2011,10,2,75,4,1,23),_H3cDot11RtCollectSwitch_Type())
h3cDot11RtCollectSwitch.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11RtCollectSwitch.setStatus(_A)
_H3cDot11RglCollectIntvl_Type=Integer32
_H3cDot11RglCollectIntvl_Object=MibScalar
h3cDot11RglCollectIntvl=_H3cDot11RglCollectIntvl_Object((1,3,6,1,4,1,2011,10,2,75,4,1,24),_H3cDot11RglCollectIntvl_Type())
h3cDot11RglCollectIntvl.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11RglCollectIntvl.setStatus(_A)
if mibBuilder.loadTexts:h3cDot11RglCollectIntvl.setUnits(_J)
_H3cDot11RtCollectIntvl_Type=Integer32
_H3cDot11RtCollectIntvl_Object=MibScalar
h3cDot11RtCollectIntvl=_H3cDot11RtCollectIntvl_Object((1,3,6,1,4,1,2011,10,2,75,4,1,25),_H3cDot11RtCollectIntvl_Type())
h3cDot11RtCollectIntvl.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11RtCollectIntvl.setStatus(_A)
if mibBuilder.loadTexts:h3cDot11RtCollectIntvl.setUnits(_J)
class _H3cDot11AllAPCpuUsageThreshold_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_H3cDot11AllAPCpuUsageThreshold_Type.__name__=_C
_H3cDot11AllAPCpuUsageThreshold_Object=MibScalar
h3cDot11AllAPCpuUsageThreshold=_H3cDot11AllAPCpuUsageThreshold_Object((1,3,6,1,4,1,2011,10,2,75,4,1,26),_H3cDot11AllAPCpuUsageThreshold_Type())
h3cDot11AllAPCpuUsageThreshold.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11AllAPCpuUsageThreshold.setStatus(_A)
if mibBuilder.loadTexts:h3cDot11AllAPCpuUsageThreshold.setUnits(_X)
class _H3cDot11AllAPMemUsageThreshold_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_H3cDot11AllAPMemUsageThreshold_Type.__name__=_C
_H3cDot11AllAPMemUsageThreshold_Object=MibScalar
h3cDot11AllAPMemUsageThreshold=_H3cDot11AllAPMemUsageThreshold_Object((1,3,6,1,4,1,2011,10,2,75,4,1,27),_H3cDot11AllAPMemUsageThreshold_Type())
h3cDot11AllAPMemUsageThreshold.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11AllAPMemUsageThreshold.setStatus(_A)
if mibBuilder.loadTexts:h3cDot11AllAPMemUsageThreshold.setUnits(_X)
_H3cDot11AdjIntfTrapThreshold_Type=Integer32
_H3cDot11AdjIntfTrapThreshold_Object=MibScalar
h3cDot11AdjIntfTrapThreshold=_H3cDot11AdjIntfTrapThreshold_Object((1,3,6,1,4,1,2011,10,2,75,4,1,28),_H3cDot11AdjIntfTrapThreshold_Type())
h3cDot11AdjIntfTrapThreshold.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11AdjIntfTrapThreshold.setStatus(_A)
if mibBuilder.loadTexts:h3cDot11AdjIntfTrapThreshold.setUnits(_R)
class _H3cDot11AllAPMonitorMode_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_M,1),(_Y,2),(_h,3)))
_H3cDot11AllAPMonitorMode_Type.__name__=_C
_H3cDot11AllAPMonitorMode_Object=MibScalar
h3cDot11AllAPMonitorMode=_H3cDot11AllAPMonitorMode_Object((1,3,6,1,4,1,2011,10,2,75,4,1,29),_H3cDot11AllAPMonitorMode_Type())
h3cDot11AllAPMonitorMode.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11AllAPMonitorMode.setStatus(_A)
class _H3cDot11GlobalApFmwUpdState_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_N,1),(_O,2)))
_H3cDot11GlobalApFmwUpdState_Type.__name__=_C
_H3cDot11GlobalApFmwUpdState_Object=MibScalar
h3cDot11GlobalApFmwUpdState=_H3cDot11GlobalApFmwUpdState_Object((1,3,6,1,4,1,2011,10,2,75,4,1,30),_H3cDot11GlobalApFmwUpdState_Type())
h3cDot11GlobalApFmwUpdState.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11GlobalApFmwUpdState.setStatus(_A)
_H3cDot11ACNasIDCM_Type=OctetString
_H3cDot11ACNasIDCM_Object=MibScalar
h3cDot11ACNasIDCM=_H3cDot11ACNasIDCM_Object((1,3,6,1,4,1,2011,10,2,75,4,1,31),_H3cDot11ACNasIDCM_Type())
h3cDot11ACNasIDCM.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11ACNasIDCM.setStatus(_A)
class _H3cDot11ACRole_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_M,1),('central',2),('local',3)))
_H3cDot11ACRole_Type.__name__=_C
_H3cDot11ACRole_Object=MibScalar
h3cDot11ACRole=_H3cDot11ACRole_Object((1,3,6,1,4,1,2011,10,2,75,4,1,32),_H3cDot11ACRole_Type())
h3cDot11ACRole.setMaxAccess(_I)
if mibBuilder.loadTexts:h3cDot11ACRole.setStatus(_A)
class _H3cDot11GlobalLocalACState_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_N,1),(_O,2)))
_H3cDot11GlobalLocalACState_Type.__name__=_C
_H3cDot11GlobalLocalACState_Object=MibScalar
h3cDot11GlobalLocalACState=_H3cDot11GlobalLocalACState_Object((1,3,6,1,4,1,2011,10,2,75,4,1,33),_H3cDot11GlobalLocalACState_Type())
h3cDot11GlobalLocalACState.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11GlobalLocalACState.setStatus(_A)
_H3cDot11CentralACIPAddress_Type=IpAddress
_H3cDot11CentralACIPAddress_Object=MibScalar
h3cDot11CentralACIPAddress=_H3cDot11CentralACIPAddress_Object((1,3,6,1,4,1,2011,10,2,75,4,1,34),_H3cDot11CentralACIPAddress_Type())
h3cDot11CentralACIPAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11CentralACIPAddress.setStatus(_A)
_H3cDot11CentralACIPv6Address_Type=OctetString
_H3cDot11CentralACIPv6Address_Object=MibScalar
h3cDot11CentralACIPv6Address=_H3cDot11CentralACIPv6Address_Object((1,3,6,1,4,1,2011,10,2,75,4,1,35),_H3cDot11CentralACIPv6Address_Type())
h3cDot11CentralACIPv6Address.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11CentralACIPv6Address.setStatus(_A)
_H3cDot11PolicyConfigGroup_ObjectIdentity=ObjectIdentity
h3cDot11PolicyConfigGroup=_H3cDot11PolicyConfigGroup_ObjectIdentity((1,3,6,1,4,1,2011,10,2,75,4,2))
_H3cDot11RadioPolicyTable_Object=MibTable
h3cDot11RadioPolicyTable=_H3cDot11RadioPolicyTable_Object((1,3,6,1,4,1,2011,10,2,75,4,2,1))
if mibBuilder.loadTexts:h3cDot11RadioPolicyTable.setStatus(_A)
_H3cDot11RadioPolicyEntry_Object=MibTableRow
h3cDot11RadioPolicyEntry=_H3cDot11RadioPolicyEntry_Object((1,3,6,1,4,1,2011,10,2,75,4,2,1,1))
h3cDot11RadioPolicyEntry.setIndexNames((1,_E,_A0))
if mibBuilder.loadTexts:h3cDot11RadioPolicyEntry.setStatus(_A)
class _H3cDot11RadioPolicyName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,127))
_H3cDot11RadioPolicyName_Type.__name__=_H
_H3cDot11RadioPolicyName_Object=MibTableColumn
h3cDot11RadioPolicyName=_H3cDot11RadioPolicyName_Object((1,3,6,1,4,1,2011,10,2,75,4,2,1,1,1),_H3cDot11RadioPolicyName_Type())
h3cDot11RadioPolicyName.setMaxAccess(_F)
if mibBuilder.loadTexts:h3cDot11RadioPolicyName.setStatus(_A)
class _H3cDot11BeaconInterval_Type(Integer32):defaultValue=100
_H3cDot11BeaconInterval_Type.__name__=_C
_H3cDot11BeaconInterval_Object=MibTableColumn
h3cDot11BeaconInterval=_H3cDot11BeaconInterval_Object((1,3,6,1,4,1,2011,10,2,75,4,2,1,1,2),_H3cDot11BeaconInterval_Type())
h3cDot11BeaconInterval.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cDot11BeaconInterval.setStatus(_A)
if mibBuilder.loadTexts:h3cDot11BeaconInterval.setUnits('TU')
class _H3cDot11DtimInterval_Type(Integer32):defaultValue=1
_H3cDot11DtimInterval_Type.__name__=_C
_H3cDot11DtimInterval_Object=MibTableColumn
h3cDot11DtimInterval=_H3cDot11DtimInterval_Object((1,3,6,1,4,1,2011,10,2,75,4,2,1,1,3),_H3cDot11DtimInterval_Type())
h3cDot11DtimInterval.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cDot11DtimInterval.setStatus(_A)
class _H3cDot11RtsThreshold_Type(Integer32):defaultValue=2346
_H3cDot11RtsThreshold_Type.__name__=_C
_H3cDot11RtsThreshold_Object=MibTableColumn
h3cDot11RtsThreshold=_H3cDot11RtsThreshold_Object((1,3,6,1,4,1,2011,10,2,75,4,2,1,1,4),_H3cDot11RtsThreshold_Type())
h3cDot11RtsThreshold.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cDot11RtsThreshold.setStatus(_A)
if mibBuilder.loadTexts:h3cDot11RtsThreshold.setUnits(_P)
class _H3cDot11FragThreshold_Type(Integer32):defaultValue=2346
_H3cDot11FragThreshold_Type.__name__=_C
_H3cDot11FragThreshold_Object=MibTableColumn
h3cDot11FragThreshold=_H3cDot11FragThreshold_Object((1,3,6,1,4,1,2011,10,2,75,4,2,1,1,5),_H3cDot11FragThreshold_Type())
h3cDot11FragThreshold.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cDot11FragThreshold.setStatus(_A)
if mibBuilder.loadTexts:h3cDot11FragThreshold.setUnits(_P)
class _H3cDot11ShortRetryThreshold_Type(Integer32):defaultValue=7
_H3cDot11ShortRetryThreshold_Type.__name__=_C
_H3cDot11ShortRetryThreshold_Object=MibTableColumn
h3cDot11ShortRetryThreshold=_H3cDot11ShortRetryThreshold_Object((1,3,6,1,4,1,2011,10,2,75,4,2,1,1,6),_H3cDot11ShortRetryThreshold_Type())
h3cDot11ShortRetryThreshold.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cDot11ShortRetryThreshold.setStatus(_A)
class _H3cDot11LongRetryThreshold_Type(Integer32):defaultValue=4
_H3cDot11LongRetryThreshold_Type.__name__=_C
_H3cDot11LongRetryThreshold_Object=MibTableColumn
h3cDot11LongRetryThreshold=_H3cDot11LongRetryThreshold_Object((1,3,6,1,4,1,2011,10,2,75,4,2,1,1,7),_H3cDot11LongRetryThreshold_Type())
h3cDot11LongRetryThreshold.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cDot11LongRetryThreshold.setStatus(_A)
class _H3cDot11MaxRxLifetime_Type(Unsigned32):defaultValue=2000
_H3cDot11MaxRxLifetime_Type.__name__=_K
_H3cDot11MaxRxLifetime_Object=MibTableColumn
h3cDot11MaxRxLifetime=_H3cDot11MaxRxLifetime_Object((1,3,6,1,4,1,2011,10,2,75,4,2,1,1,8),_H3cDot11MaxRxLifetime_Type())
h3cDot11MaxRxLifetime.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cDot11MaxRxLifetime.setStatus(_A)
if mibBuilder.loadTexts:h3cDot11MaxRxLifetime.setUnits(_A1)
_H3cDot11RdoPolicyRowStatus_Type=RowStatus
_H3cDot11RdoPolicyRowStatus_Object=MibTableColumn
h3cDot11RdoPolicyRowStatus=_H3cDot11RdoPolicyRowStatus_Object((1,3,6,1,4,1,2011,10,2,75,4,2,1,1,9),_H3cDot11RdoPolicyRowStatus_Type())
h3cDot11RdoPolicyRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cDot11RdoPolicyRowStatus.setStatus(_A)
class _H3cDot11RdoClientMaxCount_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_H3cDot11RdoClientMaxCount_Type.__name__=_C
_H3cDot11RdoClientMaxCount_Object=MibTableColumn
h3cDot11RdoClientMaxCount=_H3cDot11RdoClientMaxCount_Object((1,3,6,1,4,1,2011,10,2,75,4,2,1,1,10),_H3cDot11RdoClientMaxCount_Type())
h3cDot11RdoClientMaxCount.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cDot11RdoClientMaxCount.setStatus(_A)
_H3cDot11BeaconIntervalMs_Type=Integer32
_H3cDot11BeaconIntervalMs_Object=MibTableColumn
h3cDot11BeaconIntervalMs=_H3cDot11BeaconIntervalMs_Object((1,3,6,1,4,1,2011,10,2,75,4,2,1,1,11),_H3cDot11BeaconIntervalMs_Type())
h3cDot11BeaconIntervalMs.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cDot11BeaconIntervalMs.setStatus(_A)
if mibBuilder.loadTexts:h3cDot11BeaconIntervalMs.setUnits('ms')
_H3cDot11ServicePolicyTable_Object=MibTable
h3cDot11ServicePolicyTable=_H3cDot11ServicePolicyTable_Object((1,3,6,1,4,1,2011,10,2,75,4,2,2))
if mibBuilder.loadTexts:h3cDot11ServicePolicyTable.setStatus(_A)
_H3cDot11ServicePolicyEntry_Object=MibTableRow
h3cDot11ServicePolicyEntry=_H3cDot11ServicePolicyEntry_Object((1,3,6,1,4,1,2011,10,2,75,4,2,2,1))
h3cDot11ServicePolicyEntry.setIndexNames((0,_E,_i))
if mibBuilder.loadTexts:h3cDot11ServicePolicyEntry.setStatus(_A)
_H3cDot11ServicePolicyID_Type=H3cDot11ServicePolicyIDType
_H3cDot11ServicePolicyID_Object=MibTableColumn
h3cDot11ServicePolicyID=_H3cDot11ServicePolicyID_Object((1,3,6,1,4,1,2011,10,2,75,4,2,2,1,1),_H3cDot11ServicePolicyID_Type())
h3cDot11ServicePolicyID.setMaxAccess(_F)
if mibBuilder.loadTexts:h3cDot11ServicePolicyID.setStatus(_A)
_H3cDot11SSIDName_Type=H3cDot11SSIDStringType
_H3cDot11SSIDName_Object=MibTableColumn
h3cDot11SSIDName=_H3cDot11SSIDName_Object((1,3,6,1,4,1,2011,10,2,75,4,2,2,1,2),_H3cDot11SSIDName_Type())
h3cDot11SSIDName.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cDot11SSIDName.setStatus(_A)
class _H3cDot11SSIDHidden_Type(TruthValue):defaultValue=2
_H3cDot11SSIDHidden_Type.__name__=_G
_H3cDot11SSIDHidden_Object=MibTableColumn
h3cDot11SSIDHidden=_H3cDot11SSIDHidden_Object((1,3,6,1,4,1,2011,10,2,75,4,2,2,1,3),_H3cDot11SSIDHidden_Type())
h3cDot11SSIDHidden.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cDot11SSIDHidden.setStatus(_A)
_H3cDot11AuthenMode_Type=H3cDot11AuthenType
_H3cDot11AuthenMode_Object=MibTableColumn
h3cDot11AuthenMode=_H3cDot11AuthenMode_Object((1,3,6,1,4,1,2011,10,2,75,4,2,2,1,4),_H3cDot11AuthenMode_Type())
h3cDot11AuthenMode.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cDot11AuthenMode.setStatus(_A)
_H3cDot11SSIDEncryptionMode_Type=H3cDot11SSIDEncryptModeType
_H3cDot11SSIDEncryptionMode_Object=MibTableColumn
h3cDot11SSIDEncryptionMode=_H3cDot11SSIDEncryptionMode_Object((1,3,6,1,4,1,2011,10,2,75,4,2,2,1,5),_H3cDot11SSIDEncryptionMode_Type())
h3cDot11SSIDEncryptionMode.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cDot11SSIDEncryptionMode.setStatus(_A)
class _H3cDot11WlanInfBindingType_Type(OctetString):defaultValue=OctetString('WLAN-ESS')
_H3cDot11WlanInfBindingType_Type.__name__=_H
_H3cDot11WlanInfBindingType_Object=MibTableColumn
h3cDot11WlanInfBindingType=_H3cDot11WlanInfBindingType_Object((1,3,6,1,4,1,2011,10,2,75,4,2,2,1,6),_H3cDot11WlanInfBindingType_Type())
h3cDot11WlanInfBindingType.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cDot11WlanInfBindingType.setStatus(_A)
_H3cDot11WlanInfBindingID_Type=Integer32
_H3cDot11WlanInfBindingID_Object=MibTableColumn
h3cDot11WlanInfBindingID=_H3cDot11WlanInfBindingID_Object((1,3,6,1,4,1,2011,10,2,75,4,2,2,1,7),_H3cDot11WlanInfBindingID_Type())
h3cDot11WlanInfBindingID.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cDot11WlanInfBindingID.setStatus(_A)
_H3cDot11SrvPolicyRowStatus_Type=RowStatus
_H3cDot11SrvPolicyRowStatus_Object=MibTableColumn
h3cDot11SrvPolicyRowStatus=_H3cDot11SrvPolicyRowStatus_Object((1,3,6,1,4,1,2011,10,2,75,4,2,2,1,8),_H3cDot11SrvPolicyRowStatus_Type())
h3cDot11SrvPolicyRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cDot11SrvPolicyRowStatus.setStatus(_A)
class _H3cDot11ClientMaxCount_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_H3cDot11ClientMaxCount_Type.__name__=_C
_H3cDot11ClientMaxCount_Object=MibTableColumn
h3cDot11ClientMaxCount=_H3cDot11ClientMaxCount_Object((1,3,6,1,4,1,2011,10,2,75,4,2,2,1,9),_H3cDot11ClientMaxCount_Type())
h3cDot11ClientMaxCount.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cDot11ClientMaxCount.setStatus(_A)
class _H3cDot11SPInCirMode_Type(H3cDot11CirMode):defaultValue=1
_H3cDot11SPInCirMode_Type.__name__=_d
_H3cDot11SPInCirMode_Object=MibTableColumn
h3cDot11SPInCirMode=_H3cDot11SPInCirMode_Object((1,3,6,1,4,1,2011,10,2,75,4,2,2,1,10),_H3cDot11SPInCirMode_Type())
h3cDot11SPInCirMode.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cDot11SPInCirMode.setStatus(_A)
class _H3cDot11SPInCirValue_Type(Integer32):defaultValue=0
_H3cDot11SPInCirValue_Type.__name__=_C
_H3cDot11SPInCirValue_Object=MibTableColumn
h3cDot11SPInCirValue=_H3cDot11SPInCirValue_Object((1,3,6,1,4,1,2011,10,2,75,4,2,2,1,11),_H3cDot11SPInCirValue_Type())
h3cDot11SPInCirValue.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cDot11SPInCirValue.setStatus(_A)
if mibBuilder.loadTexts:h3cDot11SPInCirValue.setUnits(_Q)
class _H3cDot11SPOutCirMode_Type(H3cDot11CirMode):defaultValue=1
_H3cDot11SPOutCirMode_Type.__name__=_d
_H3cDot11SPOutCirMode_Object=MibTableColumn
h3cDot11SPOutCirMode=_H3cDot11SPOutCirMode_Object((1,3,6,1,4,1,2011,10,2,75,4,2,2,1,12),_H3cDot11SPOutCirMode_Type())
h3cDot11SPOutCirMode.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cDot11SPOutCirMode.setStatus(_A)
class _H3cDot11SPOutCirValue_Type(Integer32):defaultValue=0
_H3cDot11SPOutCirValue_Type.__name__=_C
_H3cDot11SPOutCirValue_Object=MibTableColumn
h3cDot11SPOutCirValue=_H3cDot11SPOutCirValue_Object((1,3,6,1,4,1,2011,10,2,75,4,2,2,1,13),_H3cDot11SPOutCirValue_Type())
h3cDot11SPOutCirValue.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cDot11SPOutCirValue.setStatus(_A)
if mibBuilder.loadTexts:h3cDot11SPOutCirValue.setUnits(_Q)
class _H3cDot11WlanInfPVID_Type(Integer32):defaultValue=1
_H3cDot11WlanInfPVID_Type.__name__=_C
_H3cDot11WlanInfPVID_Object=MibTableColumn
h3cDot11WlanInfPVID=_H3cDot11WlanInfPVID_Object((1,3,6,1,4,1,2011,10,2,75,4,2,2,1,14),_H3cDot11WlanInfPVID_Type())
h3cDot11WlanInfPVID.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cDot11WlanInfPVID.setStatus(_A)
class _H3cDot11SPInCirStaticValue_Type(Integer32):defaultValue=0
_H3cDot11SPInCirStaticValue_Type.__name__=_C
_H3cDot11SPInCirStaticValue_Object=MibTableColumn
h3cDot11SPInCirStaticValue=_H3cDot11SPInCirStaticValue_Object((1,3,6,1,4,1,2011,10,2,75,4,2,2,1,15),_H3cDot11SPInCirStaticValue_Type())
h3cDot11SPInCirStaticValue.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cDot11SPInCirStaticValue.setStatus(_A)
if mibBuilder.loadTexts:h3cDot11SPInCirStaticValue.setUnits(_Q)
class _H3cDot11SPOutCirStaticValue_Type(Integer32):defaultValue=0
_H3cDot11SPOutCirStaticValue_Type.__name__=_C
_H3cDot11SPOutCirStaticValue_Object=MibTableColumn
h3cDot11SPOutCirStaticValue=_H3cDot11SPOutCirStaticValue_Object((1,3,6,1,4,1,2011,10,2,75,4,2,2,1,16),_H3cDot11SPOutCirStaticValue_Type())
h3cDot11SPOutCirStaticValue.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cDot11SPOutCirStaticValue.setStatus(_A)
if mibBuilder.loadTexts:h3cDot11SPOutCirStaticValue.setUnits(_Q)
class _H3cDot11SPIsolate_Type(TruthValue):defaultValue=2
_H3cDot11SPIsolate_Type.__name__=_G
_H3cDot11SPIsolate_Object=MibTableColumn
h3cDot11SPIsolate=_H3cDot11SPIsolate_Object((1,3,6,1,4,1,2011,10,2,75,4,2,2,1,17),_H3cDot11SPIsolate_Type())
h3cDot11SPIsolate.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cDot11SPIsolate.setStatus(_A)
_H3cDot11WlanexAuthServerIP_Type=IpAddress
_H3cDot11WlanexAuthServerIP_Object=MibTableColumn
h3cDot11WlanexAuthServerIP=_H3cDot11WlanexAuthServerIP_Object((1,3,6,1,4,1,2011,10,2,75,4,2,2,1,18),_H3cDot11WlanexAuthServerIP_Type())
h3cDot11WlanexAuthServerIP.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cDot11WlanexAuthServerIP.setStatus(_A)
class _H3cDot11SPBeaconMeasEnable_Type(TruthValue):defaultValue=2
_H3cDot11SPBeaconMeasEnable_Type.__name__=_G
_H3cDot11SPBeaconMeasEnable_Object=MibTableColumn
h3cDot11SPBeaconMeasEnable=_H3cDot11SPBeaconMeasEnable_Object((1,3,6,1,4,1,2011,10,2,75,4,2,2,1,19),_H3cDot11SPBeaconMeasEnable_Type())
h3cDot11SPBeaconMeasEnable.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cDot11SPBeaconMeasEnable.setStatus(_A)
class _H3cDot11SPBeaconMeasType_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('passive',1),('active',2),('beaconTable',3)))
_H3cDot11SPBeaconMeasType_Type.__name__=_C
_H3cDot11SPBeaconMeasType_Object=MibTableColumn
h3cDot11SPBeaconMeasType=_H3cDot11SPBeaconMeasType_Object((1,3,6,1,4,1,2011,10,2,75,4,2,2,1,20),_H3cDot11SPBeaconMeasType_Type())
h3cDot11SPBeaconMeasType.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cDot11SPBeaconMeasType.setStatus(_A)
class _H3cDot11SPBeaconMeasInterval_Type(Integer32):defaultValue=60;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(10,200))
_H3cDot11SPBeaconMeasInterval_Type.__name__=_C
_H3cDot11SPBeaconMeasInterval_Object=MibTableColumn
h3cDot11SPBeaconMeasInterval=_H3cDot11SPBeaconMeasInterval_Object((1,3,6,1,4,1,2011,10,2,75,4,2,2,1,21),_H3cDot11SPBeaconMeasInterval_Type())
h3cDot11SPBeaconMeasInterval.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cDot11SPBeaconMeasInterval.setStatus(_A)
if mibBuilder.loadTexts:h3cDot11SPBeaconMeasInterval.setUnits(_J)
class _H3cDot11AuthenModeCM_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('opensystem',0),('sharedkey',1)))
_H3cDot11AuthenModeCM_Type.__name__=_C
_H3cDot11AuthenModeCM_Object=MibTableColumn
h3cDot11AuthenModeCM=_H3cDot11AuthenModeCM_Object((1,3,6,1,4,1,2011,10,2,75,4,2,2,1,22),_H3cDot11AuthenModeCM_Type())
h3cDot11AuthenModeCM.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cDot11AuthenModeCM.setStatus(_A)
class _H3cDot11SecIEStatusCM_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*((_Z,0),('wpa',1),('wpa2',2),(_j,3)))
_H3cDot11SecIEStatusCM_Type.__name__=_C
_H3cDot11SecIEStatusCM_Object=MibTableColumn
h3cDot11SecIEStatusCM=_H3cDot11SecIEStatusCM_Object((1,3,6,1,4,1,2011,10,2,75,4,2,2,1,23),_H3cDot11SecIEStatusCM_Type())
h3cDot11SecIEStatusCM.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cDot11SecIEStatusCM.setStatus(_A)
class _H3cDot11SecurityCiphersCM_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5)));namedValues=NamedValues(*((_Z,0),('wep40',1),('wep104',2),('tkip',3),('aesccmp',4),('wpisms4',5)))
_H3cDot11SecurityCiphersCM_Type.__name__=_C
_H3cDot11SecurityCiphersCM_Object=MibTableColumn
h3cDot11SecurityCiphersCM=_H3cDot11SecurityCiphersCM_Object((1,3,6,1,4,1,2011,10,2,75,4,2,2,1,24),_H3cDot11SecurityCiphersCM_Type())
h3cDot11SecurityCiphersCM.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cDot11SecurityCiphersCM.setStatus(_A)
class _H3cDot11SrvPolicyStatusCM_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_S,0),(_T,1)))
_H3cDot11SrvPolicyStatusCM_Type.__name__=_C
_H3cDot11SrvPolicyStatusCM_Object=MibTableColumn
h3cDot11SrvPolicyStatusCM=_H3cDot11SrvPolicyStatusCM_Object((1,3,6,1,4,1,2011,10,2,75,4,2,2,1,25),_H3cDot11SrvPolicyStatusCM_Type())
h3cDot11SrvPolicyStatusCM.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cDot11SrvPolicyStatusCM.setStatus(_A)
class _H3cDot11SSIDHiddenCM_Type(H3cDot11TruthValueCM):defaultValue=0
_H3cDot11SSIDHiddenCM_Type.__name__=_W
_H3cDot11SSIDHiddenCM_Object=MibTableColumn
h3cDot11SSIDHiddenCM=_H3cDot11SSIDHiddenCM_Object((1,3,6,1,4,1,2011,10,2,75,4,2,2,1,26),_H3cDot11SSIDHiddenCM_Type())
h3cDot11SSIDHiddenCM.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cDot11SSIDHiddenCM.setStatus(_A)
class _H3cDot11SPIsolateCM_Type(H3cDot11TruthValueCM):defaultValue=0
_H3cDot11SPIsolateCM_Type.__name__=_W
_H3cDot11SPIsolateCM_Object=MibTableColumn
h3cDot11SPIsolateCM=_H3cDot11SPIsolateCM_Object((1,3,6,1,4,1,2011,10,2,75,4,2,2,1,27),_H3cDot11SPIsolateCM_Type())
h3cDot11SPIsolateCM.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cDot11SPIsolateCM.setStatus(_A)
class _H3cDot11FwdVlanBitMapLow_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,256))
_H3cDot11FwdVlanBitMapLow_Type.__name__=_H
_H3cDot11FwdVlanBitMapLow_Object=MibTableColumn
h3cDot11FwdVlanBitMapLow=_H3cDot11FwdVlanBitMapLow_Object((1,3,6,1,4,1,2011,10,2,75,4,2,2,1,28),_H3cDot11FwdVlanBitMapLow_Type())
h3cDot11FwdVlanBitMapLow.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cDot11FwdVlanBitMapLow.setStatus(_A)
class _H3cDot11FwdVlanBitMapHigh_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,256))
_H3cDot11FwdVlanBitMapHigh_Type.__name__=_H
_H3cDot11FwdVlanBitMapHigh_Object=MibTableColumn
h3cDot11FwdVlanBitMapHigh=_H3cDot11FwdVlanBitMapHigh_Object((1,3,6,1,4,1,2011,10,2,75,4,2,2,1,29),_H3cDot11FwdVlanBitMapHigh_Type())
h3cDot11FwdVlanBitMapHigh.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cDot11FwdVlanBitMapHigh.setStatus(_A)
_H3cDot11ServicePolicyName_Type=OctetString
_H3cDot11ServicePolicyName_Object=MibTableColumn
h3cDot11ServicePolicyName=_H3cDot11ServicePolicyName_Object((1,3,6,1,4,1,2011,10,2,75,4,2,2,1,30),_H3cDot11ServicePolicyName_Type())
h3cDot11ServicePolicyName.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cDot11ServicePolicyName.setStatus(_A)
class _H3cDot11SecurityModeCM_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*((_Z,0),(_U,1),('radius',2),(_j,3)))
_H3cDot11SecurityModeCM_Type.__name__=_C
_H3cDot11SecurityModeCM_Object=MibTableColumn
h3cDot11SecurityModeCM=_H3cDot11SecurityModeCM_Object((1,3,6,1,4,1,2011,10,2,75,4,2,2,1,31),_H3cDot11SecurityModeCM_Type())
h3cDot11SecurityModeCM.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11SecurityModeCM.setStatus(_A)
class _H3cDot11SPInCbsValue_Type(Integer32):defaultValue=0
_H3cDot11SPInCbsValue_Type.__name__=_C
_H3cDot11SPInCbsValue_Object=MibTableColumn
h3cDot11SPInCbsValue=_H3cDot11SPInCbsValue_Object((1,3,6,1,4,1,2011,10,2,75,4,2,2,1,32),_H3cDot11SPInCbsValue_Type())
h3cDot11SPInCbsValue.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cDot11SPInCbsValue.setStatus(_A)
if mibBuilder.loadTexts:h3cDot11SPInCbsValue.setUnits(_P)
class _H3cDot11SPOutCbsValue_Type(Integer32):defaultValue=0
_H3cDot11SPOutCbsValue_Type.__name__=_C
_H3cDot11SPOutCbsValue_Object=MibTableColumn
h3cDot11SPOutCbsValue=_H3cDot11SPOutCbsValue_Object((1,3,6,1,4,1,2011,10,2,75,4,2,2,1,33),_H3cDot11SPOutCbsValue_Type())
h3cDot11SPOutCbsValue.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cDot11SPOutCbsValue.setStatus(_A)
if mibBuilder.loadTexts:h3cDot11SPOutCbsValue.setUnits(_P)
_H3cDot11ServicePolicyExtTable_Object=MibTable
h3cDot11ServicePolicyExtTable=_H3cDot11ServicePolicyExtTable_Object((1,3,6,1,4,1,2011,10,2,75,4,2,3))
if mibBuilder.loadTexts:h3cDot11ServicePolicyExtTable.setStatus(_A)
_H3cDot11ServicePolicyExtEntry_Object=MibTableRow
h3cDot11ServicePolicyExtEntry=_H3cDot11ServicePolicyExtEntry_Object((1,3,6,1,4,1,2011,10,2,75,4,2,3,1))
h3cDot11ServicePolicyExtEntry.setIndexNames((0,_E,_A2))
if mibBuilder.loadTexts:h3cDot11ServicePolicyExtEntry.setStatus(_A)
_H3cDot11ServicePolicyExtID_Type=H3cDot11ServicePolicyIDType
_H3cDot11ServicePolicyExtID_Object=MibTableColumn
h3cDot11ServicePolicyExtID=_H3cDot11ServicePolicyExtID_Object((1,3,6,1,4,1,2011,10,2,75,4,2,3,1,1),_H3cDot11ServicePolicyExtID_Type())
h3cDot11ServicePolicyExtID.setMaxAccess(_F)
if mibBuilder.loadTexts:h3cDot11ServicePolicyExtID.setStatus(_A)
_H3cDot11SecIEStatus_Type=H3cDot11SecIEStatusType
_H3cDot11SecIEStatus_Object=MibTableColumn
h3cDot11SecIEStatus=_H3cDot11SecIEStatus_Object((1,3,6,1,4,1,2011,10,2,75,4,2,3,1,2),_H3cDot11SecIEStatus_Type())
h3cDot11SecIEStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cDot11SecIEStatus.setStatus(_A)
_H3cDot11SecurityCiphers_Type=Integer32
_H3cDot11SecurityCiphers_Object=MibTableColumn
h3cDot11SecurityCiphers=_H3cDot11SecurityCiphers_Object((1,3,6,1,4,1,2011,10,2,75,4,2,3,1,3),_H3cDot11SecurityCiphers_Type())
h3cDot11SecurityCiphers.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cDot11SecurityCiphers.setStatus(_A)
class _H3cDot11CipherKeyIndex_Type(Integer32):defaultValue=1
_H3cDot11CipherKeyIndex_Type.__name__=_C
_H3cDot11CipherKeyIndex_Object=MibTableColumn
h3cDot11CipherKeyIndex=_H3cDot11CipherKeyIndex_Object((1,3,6,1,4,1,2011,10,2,75,4,2,3,1,4),_H3cDot11CipherKeyIndex_Type())
h3cDot11CipherKeyIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cDot11CipherKeyIndex.setStatus(_A)
_H3cDot11CipherKey_Type=OctetString
_H3cDot11CipherKey_Object=MibTableColumn
h3cDot11CipherKey=_H3cDot11CipherKey_Object((1,3,6,1,4,1,2011,10,2,75,4,2,3,1,5),_H3cDot11CipherKey_Type())
h3cDot11CipherKey.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cDot11CipherKey.setStatus(_A)
_H3cDot11SrvPolicyExtRowStatus_Type=RowStatus
_H3cDot11SrvPolicyExtRowStatus_Object=MibTableColumn
h3cDot11SrvPolicyExtRowStatus=_H3cDot11SrvPolicyExtRowStatus_Object((1,3,6,1,4,1,2011,10,2,75,4,2,3,1,6),_H3cDot11SrvPolicyExtRowStatus_Type())
h3cDot11SrvPolicyExtRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cDot11SrvPolicyExtRowStatus.setStatus(_A)
class _H3cDot11CipherKeyType_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('char',1),('hex',2)))
_H3cDot11CipherKeyType_Type.__name__=_C
_H3cDot11CipherKeyType_Object=MibTableColumn
h3cDot11CipherKeyType=_H3cDot11CipherKeyType_Object((1,3,6,1,4,1,2011,10,2,75,4,2,3,1,7),_H3cDot11CipherKeyType_Type())
h3cDot11CipherKeyType.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cDot11CipherKeyType.setStatus(_A)
class _H3cDot11AkmMode_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('dot1x',1),(_U,2)))
_H3cDot11AkmMode_Type.__name__=_C
_H3cDot11AkmMode_Object=MibTableColumn
h3cDot11AkmMode=_H3cDot11AkmMode_Object((1,3,6,1,4,1,2011,10,2,75,4,2,3,1,8),_H3cDot11AkmMode_Type())
h3cDot11AkmMode.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cDot11AkmMode.setStatus(_A)
_H3cDot11PskKey_Type=OctetString
_H3cDot11PskKey_Object=MibTableColumn
h3cDot11PskKey=_H3cDot11PskKey_Object((1,3,6,1,4,1,2011,10,2,75,4,2,3,1,9),_H3cDot11PskKey_Type())
h3cDot11PskKey.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cDot11PskKey.setStatus(_A)
_H3cDot11RadioPolicyExtTable_Object=MibTable
h3cDot11RadioPolicyExtTable=_H3cDot11RadioPolicyExtTable_Object((1,3,6,1,4,1,2011,10,2,75,4,2,4))
if mibBuilder.loadTexts:h3cDot11RadioPolicyExtTable.setStatus(_A)
_H3cDot11RadioPolicyExtEntry_Object=MibTableRow
h3cDot11RadioPolicyExtEntry=_H3cDot11RadioPolicyExtEntry_Object((1,3,6,1,4,1,2011,10,2,75,4,2,4,1))
h3cDot11RadioPolicyExtEntry.setIndexNames((0,_E,_A3),(0,_E,_A4))
if mibBuilder.loadTexts:h3cDot11RadioPolicyExtEntry.setStatus(_A)
class _H3cDot11RPAPSerialID_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,127))
_H3cDot11RPAPSerialID_Type.__name__=_H
_H3cDot11RPAPSerialID_Object=MibTableColumn
h3cDot11RPAPSerialID=_H3cDot11RPAPSerialID_Object((1,3,6,1,4,1,2011,10,2,75,4,2,4,1,1),_H3cDot11RPAPSerialID_Type())
h3cDot11RPAPSerialID.setMaxAccess(_F)
if mibBuilder.loadTexts:h3cDot11RPAPSerialID.setStatus(_A)
_H3cDot11RPRadioID_Type=H3cDot11RadioScopeType
_H3cDot11RPRadioID_Object=MibTableColumn
h3cDot11RPRadioID=_H3cDot11RPRadioID_Object((1,3,6,1,4,1,2011,10,2,75,4,2,4,1,2),_H3cDot11RPRadioID_Type())
h3cDot11RPRadioID.setMaxAccess(_F)
if mibBuilder.loadTexts:h3cDot11RPRadioID.setStatus(_A)
class _H3cDot11RPBeaconInterval_Type(Integer32):defaultValue=100
_H3cDot11RPBeaconInterval_Type.__name__=_C
_H3cDot11RPBeaconInterval_Object=MibTableColumn
h3cDot11RPBeaconInterval=_H3cDot11RPBeaconInterval_Object((1,3,6,1,4,1,2011,10,2,75,4,2,4,1,3),_H3cDot11RPBeaconInterval_Type())
h3cDot11RPBeaconInterval.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11RPBeaconInterval.setStatus(_A)
if mibBuilder.loadTexts:h3cDot11RPBeaconInterval.setUnits('milliseconds')
class _H3cDot11RPDtimInterval_Type(Integer32):defaultValue=1
_H3cDot11RPDtimInterval_Type.__name__=_C
_H3cDot11RPDtimInterval_Object=MibTableColumn
h3cDot11RPDtimInterval=_H3cDot11RPDtimInterval_Object((1,3,6,1,4,1,2011,10,2,75,4,2,4,1,4),_H3cDot11RPDtimInterval_Type())
h3cDot11RPDtimInterval.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11RPDtimInterval.setStatus(_A)
class _H3cDot11RPRtsThreshold_Type(Integer32):defaultValue=2346
_H3cDot11RPRtsThreshold_Type.__name__=_C
_H3cDot11RPRtsThreshold_Object=MibTableColumn
h3cDot11RPRtsThreshold=_H3cDot11RPRtsThreshold_Object((1,3,6,1,4,1,2011,10,2,75,4,2,4,1,5),_H3cDot11RPRtsThreshold_Type())
h3cDot11RPRtsThreshold.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11RPRtsThreshold.setStatus(_A)
if mibBuilder.loadTexts:h3cDot11RPRtsThreshold.setUnits(_P)
class _H3cDot11RPFragThreshold_Type(Integer32):defaultValue=2346
_H3cDot11RPFragThreshold_Type.__name__=_C
_H3cDot11RPFragThreshold_Object=MibTableColumn
h3cDot11RPFragThreshold=_H3cDot11RPFragThreshold_Object((1,3,6,1,4,1,2011,10,2,75,4,2,4,1,6),_H3cDot11RPFragThreshold_Type())
h3cDot11RPFragThreshold.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11RPFragThreshold.setStatus(_A)
if mibBuilder.loadTexts:h3cDot11RPFragThreshold.setUnits(_P)
class _H3cDot11RPShortRetryThreshold_Type(Integer32):defaultValue=7
_H3cDot11RPShortRetryThreshold_Type.__name__=_C
_H3cDot11RPShortRetryThreshold_Object=MibTableColumn
h3cDot11RPShortRetryThreshold=_H3cDot11RPShortRetryThreshold_Object((1,3,6,1,4,1,2011,10,2,75,4,2,4,1,7),_H3cDot11RPShortRetryThreshold_Type())
h3cDot11RPShortRetryThreshold.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11RPShortRetryThreshold.setStatus(_A)
class _H3cDot11RPLongRetryThreshold_Type(Integer32):defaultValue=4
_H3cDot11RPLongRetryThreshold_Type.__name__=_C
_H3cDot11RPLongRetryThreshold_Object=MibTableColumn
h3cDot11RPLongRetryThreshold=_H3cDot11RPLongRetryThreshold_Object((1,3,6,1,4,1,2011,10,2,75,4,2,4,1,8),_H3cDot11RPLongRetryThreshold_Type())
h3cDot11RPLongRetryThreshold.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11RPLongRetryThreshold.setStatus(_A)
class _H3cDot11RPClientMaxCount_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_H3cDot11RPClientMaxCount_Type.__name__=_C
_H3cDot11RPClientMaxCount_Object=MibTableColumn
h3cDot11RPClientMaxCount=_H3cDot11RPClientMaxCount_Object((1,3,6,1,4,1,2011,10,2,75,4,2,4,1,9),_H3cDot11RPClientMaxCount_Type())
h3cDot11RPClientMaxCount.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11RPClientMaxCount.setStatus(_A)
class _H3cDot11RPBeaconIntervalCM_Type(Integer32):defaultValue=100
_H3cDot11RPBeaconIntervalCM_Type.__name__=_C
_H3cDot11RPBeaconIntervalCM_Object=MibTableColumn
h3cDot11RPBeaconIntervalCM=_H3cDot11RPBeaconIntervalCM_Object((1,3,6,1,4,1,2011,10,2,75,4,2,4,1,10),_H3cDot11RPBeaconIntervalCM_Type())
h3cDot11RPBeaconIntervalCM.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11RPBeaconIntervalCM.setStatus(_A)
if mibBuilder.loadTexts:h3cDot11RPBeaconIntervalCM.setUnits('timeunit')
_H3cDot11SrvPortSecurityTable_Object=MibTable
h3cDot11SrvPortSecurityTable=_H3cDot11SrvPortSecurityTable_Object((1,3,6,1,4,1,2011,10,2,75,4,2,5))
if mibBuilder.loadTexts:h3cDot11SrvPortSecurityTable.setStatus(_A)
_H3cDot11SrvPortSecurityEntry_Object=MibTableRow
h3cDot11SrvPortSecurityEntry=_H3cDot11SrvPortSecurityEntry_Object((1,3,6,1,4,1,2011,10,2,75,4,2,5,1))
h3cDot11SrvPortSecurityEntry.setIndexNames((0,_E,_A5))
if mibBuilder.loadTexts:h3cDot11SrvPortSecurityEntry.setStatus(_A)
_H3cDot11SecurityServicePolicyID_Type=H3cDot11ServicePolicyIDType
_H3cDot11SecurityServicePolicyID_Object=MibTableColumn
h3cDot11SecurityServicePolicyID=_H3cDot11SecurityServicePolicyID_Object((1,3,6,1,4,1,2011,10,2,75,4,2,5,1,1),_H3cDot11SecurityServicePolicyID_Type())
h3cDot11SecurityServicePolicyID.setMaxAccess(_F)
if mibBuilder.loadTexts:h3cDot11SecurityServicePolicyID.setStatus(_A)
class _H3cDot11SrvPortSecurityMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*((_A6,1),(_A7,2),(_U,3),(_A8,4),(_A9,5),('ext',6)))
_H3cDot11SrvPortSecurityMode_Type.__name__=_C
_H3cDot11SrvPortSecurityMode_Object=MibTableColumn
h3cDot11SrvPortSecurityMode=_H3cDot11SrvPortSecurityMode_Object((1,3,6,1,4,1,2011,10,2,75,4,2,5,1,2),_H3cDot11SrvPortSecurityMode_Type())
h3cDot11SrvPortSecurityMode.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11SrvPortSecurityMode.setStatus(_A)
class _H3cDot11SrvSecurityKeyType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_AA,1),(_AB,2),(_AC,3)))
_H3cDot11SrvSecurityKeyType_Type.__name__=_C
_H3cDot11SrvSecurityKeyType_Object=MibTableColumn
h3cDot11SrvSecurityKeyType=_H3cDot11SrvSecurityKeyType_Object((1,3,6,1,4,1,2011,10,2,75,4,2,5,1,3),_H3cDot11SrvSecurityKeyType_Type())
h3cDot11SrvSecurityKeyType.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11SrvSecurityKeyType.setStatus(_A)
class _H3cDot11SrvSecurityPskKeyMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_k,1),(_l,2),(_m,3)))
_H3cDot11SrvSecurityPskKeyMode_Type.__name__=_C
_H3cDot11SrvSecurityPskKeyMode_Object=MibTableColumn
h3cDot11SrvSecurityPskKeyMode=_H3cDot11SrvSecurityPskKeyMode_Object((1,3,6,1,4,1,2011,10,2,75,4,2,5,1,4),_H3cDot11SrvSecurityPskKeyMode_Type())
h3cDot11SrvSecurityPskKeyMode.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11SrvSecurityPskKeyMode.setStatus(_A)
class _H3cDot11SrvSecurityPskKeyString_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_H3cDot11SrvSecurityPskKeyString_Type.__name__=_g
_H3cDot11SrvSecurityPskKeyString_Object=MibTableColumn
h3cDot11SrvSecurityPskKeyString=_H3cDot11SrvSecurityPskKeyString_Object((1,3,6,1,4,1,2011,10,2,75,4,2,5,1,5),_H3cDot11SrvSecurityPskKeyString_Type())
h3cDot11SrvSecurityPskKeyString.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11SrvSecurityPskKeyString.setStatus(_A)
class _H3cDot11SrvPortSecurityModeCM_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*((_Z,0),(_U,1),('radius',2),(_j,3)))
_H3cDot11SrvPortSecurityModeCM_Type.__name__=_C
_H3cDot11SrvPortSecurityModeCM_Object=MibTableColumn
h3cDot11SrvPortSecurityModeCM=_H3cDot11SrvPortSecurityModeCM_Object((1,3,6,1,4,1,2011,10,2,75,4,2,5,1,6),_H3cDot11SrvPortSecurityModeCM_Type())
h3cDot11SrvPortSecurityModeCM.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11SrvPortSecurityModeCM.setStatus(_A)
_H3cDot11SrvPolicyExtendTable_Object=MibTable
h3cDot11SrvPolicyExtendTable=_H3cDot11SrvPolicyExtendTable_Object((1,3,6,1,4,1,2011,10,2,75,4,2,6))
if mibBuilder.loadTexts:h3cDot11SrvPolicyExtendTable.setStatus(_A)
_H3cDot11SrvPolicyExtendEntry_Object=MibTableRow
h3cDot11SrvPolicyExtendEntry=_H3cDot11SrvPolicyExtendEntry_Object((1,3,6,1,4,1,2011,10,2,75,4,2,6,1))
h3cDot11SrvPolicyExtendEntry.setIndexNames((0,_E,_i))
if mibBuilder.loadTexts:h3cDot11SrvPolicyExtendEntry.setStatus(_A)
class _H3cDot11SPEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_N,1),(_O,2)))
_H3cDot11SPEnable_Type.__name__=_C
_H3cDot11SPEnable_Object=MibTableColumn
h3cDot11SPEnable=_H3cDot11SPEnable_Object((1,3,6,1,4,1,2011,10,2,75,4,2,6,1,1),_H3cDot11SPEnable_Type())
h3cDot11SPEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11SPEnable.setStatus(_A)
_H3cDot11SrvL2AuthenTable_Object=MibTable
h3cDot11SrvL2AuthenTable=_H3cDot11SrvL2AuthenTable_Object((1,3,6,1,4,1,2011,10,2,75,4,2,7))
if mibBuilder.loadTexts:h3cDot11SrvL2AuthenTable.setStatus(_A)
_H3cDot11SrvL2AuthenEntry_Object=MibTableRow
h3cDot11SrvL2AuthenEntry=_H3cDot11SrvL2AuthenEntry_Object((1,3,6,1,4,1,2011,10,2,75,4,2,7,1))
h3cDot11SrvL2AuthenEntry.setIndexNames((0,_E,_AD))
if mibBuilder.loadTexts:h3cDot11SrvL2AuthenEntry.setStatus(_A)
_H3cDot11SrvL2AuthenID_Type=H3cDot11ServicePolicyIDType
_H3cDot11SrvL2AuthenID_Object=MibTableColumn
h3cDot11SrvL2AuthenID=_H3cDot11SrvL2AuthenID_Object((1,3,6,1,4,1,2011,10,2,75,4,2,7,1,1),_H3cDot11SrvL2AuthenID_Type())
h3cDot11SrvL2AuthenID.setMaxAccess(_F)
if mibBuilder.loadTexts:h3cDot11SrvL2AuthenID.setStatus(_A)
class _H3cDot11L2AuthenMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*(('bypass',1),('macAuthentication',2),('macThenDot1xAuthentication',3),('dot1xAuthentication',4),('dot1xThenMacAuthentication',5),('ouiThenDot1x',6)))
_H3cDot11L2AuthenMode_Type.__name__=_C
_H3cDot11L2AuthenMode_Object=MibTableColumn
h3cDot11L2AuthenMode=_H3cDot11L2AuthenMode_Object((1,3,6,1,4,1,2011,10,2,75,4,2,7,1,2),_H3cDot11L2AuthenMode_Type())
h3cDot11L2AuthenMode.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11L2AuthenMode.setStatus(_A)
_H3cDot11L2IntrusProtectEnable_Type=TruthValue
_H3cDot11L2IntrusProtectEnable_Object=MibTableColumn
h3cDot11L2IntrusProtectEnable=_H3cDot11L2IntrusProtectEnable_Object((1,3,6,1,4,1,2011,10,2,75,4,2,7,1,3),_H3cDot11L2IntrusProtectEnable_Type())
h3cDot11L2IntrusProtectEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11L2IntrusProtectEnable.setStatus(_A)
class _H3cDot11L2IntrusProtectOpt_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('blockMACTemporarily',1),('stopServiceTemporarily',2),('stopService',3)))
_H3cDot11L2IntrusProtectOpt_Type.__name__=_C
_H3cDot11L2IntrusProtectOpt_Object=MibTableColumn
h3cDot11L2IntrusProtectOpt=_H3cDot11L2IntrusProtectOpt_Object((1,3,6,1,4,1,2011,10,2,75,4,2,7,1,4),_H3cDot11L2IntrusProtectOpt_Type())
h3cDot11L2IntrusProtectOpt.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11L2IntrusProtectOpt.setStatus(_A)
class _H3cDot11TempServiceStopTimer_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(10,300))
_H3cDot11TempServiceStopTimer_Type.__name__=_C
_H3cDot11TempServiceStopTimer_Object=MibTableColumn
h3cDot11TempServiceStopTimer=_H3cDot11TempServiceStopTimer_Object((1,3,6,1,4,1,2011,10,2,75,4,2,7,1,5),_H3cDot11TempServiceStopTimer_Type())
h3cDot11TempServiceStopTimer.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11TempServiceStopTimer.setStatus(_A)
class _H3cDot11TempBlockMACTimer_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(60,300))
_H3cDot11TempBlockMACTimer_Type.__name__=_C
_H3cDot11TempBlockMACTimer_Object=MibTableColumn
h3cDot11TempBlockMACTimer=_H3cDot11TempBlockMACTimer_Object((1,3,6,1,4,1,2011,10,2,75,4,2,7,1,6),_H3cDot11TempBlockMACTimer_Type())
h3cDot11TempBlockMACTimer.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11TempBlockMACTimer.setStatus(_A)
_H3cDot11L2IgnoreAuthorization_Type=TruthValue
_H3cDot11L2IgnoreAuthorization_Object=MibTableColumn
h3cDot11L2IgnoreAuthorization=_H3cDot11L2IgnoreAuthorization_Object((1,3,6,1,4,1,2011,10,2,75,4,2,7,1,7),_H3cDot11L2IgnoreAuthorization_Type())
h3cDot11L2IgnoreAuthorization.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11L2IgnoreAuthorization.setStatus(_A)
class _H3cDot11L2FailVLAN_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4094))
_H3cDot11L2FailVLAN_Type.__name__=_C
_H3cDot11L2FailVLAN_Object=MibTableColumn
h3cDot11L2FailVLAN=_H3cDot11L2FailVLAN_Object((1,3,6,1,4,1,2011,10,2,75,4,2,7,1,8),_H3cDot11L2FailVLAN_Type())
h3cDot11L2FailVLAN.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11L2FailVLAN.setStatus(_A)
class _H3cDot11L2CriticalVLAN_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4094))
_H3cDot11L2CriticalVLAN_Type.__name__=_C
_H3cDot11L2CriticalVLAN_Object=MibTableColumn
h3cDot11L2CriticalVLAN=_H3cDot11L2CriticalVLAN_Object((1,3,6,1,4,1,2011,10,2,75,4,2,7,1,9),_H3cDot11L2CriticalVLAN_Type())
h3cDot11L2CriticalVLAN.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11L2CriticalVLAN.setStatus(_A)
_H3cDot11L2AuthorFailOffline_Type=TruthValue
_H3cDot11L2AuthorFailOffline_Object=MibTableColumn
h3cDot11L2AuthorFailOffline=_H3cDot11L2AuthorFailOffline_Object((1,3,6,1,4,1,2011,10,2,75,4,2,7,1,10),_H3cDot11L2AuthorFailOffline_Type())
h3cDot11L2AuthorFailOffline.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11L2AuthorFailOffline.setStatus(_A)
_H3cDot11L2AccountFailOffline_Type=TruthValue
_H3cDot11L2AccountFailOffline_Object=MibTableColumn
h3cDot11L2AccountFailOffline=_H3cDot11L2AccountFailOffline_Object((1,3,6,1,4,1,2011,10,2,75,4,2,7,1,11),_H3cDot11L2AccountFailOffline_Type())
h3cDot11L2AccountFailOffline.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11L2AccountFailOffline.setStatus(_A)
_H3cDot11Dot1xHSEnable_Type=TruthValue
_H3cDot11Dot1xHSEnable_Object=MibTableColumn
h3cDot11Dot1xHSEnable=_H3cDot11Dot1xHSEnable_Object((1,3,6,1,4,1,2011,10,2,75,4,2,7,1,12),_H3cDot11Dot1xHSEnable_Type())
h3cDot11Dot1xHSEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11Dot1xHSEnable.setStatus(_A)
_H3cDot11Dot1xSecureHSEnable_Type=TruthValue
_H3cDot11Dot1xSecureHSEnable_Object=MibTableColumn
h3cDot11Dot1xSecureHSEnable=_H3cDot11Dot1xSecureHSEnable_Object((1,3,6,1,4,1,2011,10,2,75,4,2,7,1,13),_H3cDot11Dot1xSecureHSEnable_Type())
h3cDot11Dot1xSecureHSEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11Dot1xSecureHSEnable.setStatus(_A)
_H3cDot11Dot1xReauthenEnable_Type=TruthValue
_H3cDot11Dot1xReauthenEnable_Object=MibTableColumn
h3cDot11Dot1xReauthenEnable=_H3cDot11Dot1xReauthenEnable_Object((1,3,6,1,4,1,2011,10,2,75,4,2,7,1,14),_H3cDot11Dot1xReauthenEnable_Type())
h3cDot11Dot1xReauthenEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11Dot1xReauthenEnable.setStatus(_A)
_H3cDot11Dot1xMandatoryDomain_Type=OctetString
_H3cDot11Dot1xMandatoryDomain_Object=MibTableColumn
h3cDot11Dot1xMandatoryDomain=_H3cDot11Dot1xMandatoryDomain_Object((1,3,6,1,4,1,2011,10,2,75,4,2,7,1,15),_H3cDot11Dot1xMandatoryDomain_Type())
h3cDot11Dot1xMandatoryDomain.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11Dot1xMandatoryDomain.setStatus(_A)
_H3cDot11Dot1xMaxUserCount_Type=Integer32
_H3cDot11Dot1xMaxUserCount_Object=MibTableColumn
h3cDot11Dot1xMaxUserCount=_H3cDot11Dot1xMaxUserCount_Object((1,3,6,1,4,1,2011,10,2,75,4,2,7,1,16),_H3cDot11Dot1xMaxUserCount_Type())
h3cDot11Dot1xMaxUserCount.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11Dot1xMaxUserCount.setStatus(_A)
_H3cDot11MACAuthenDomain_Type=OctetString
_H3cDot11MACAuthenDomain_Object=MibTableColumn
h3cDot11MACAuthenDomain=_H3cDot11MACAuthenDomain_Object((1,3,6,1,4,1,2011,10,2,75,4,2,7,1,17),_H3cDot11MACAuthenDomain_Type())
h3cDot11MACAuthenDomain.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11MACAuthenDomain.setStatus(_A)
_H3cDot11MACAuthenMaxUserCount_Type=Integer32
_H3cDot11MACAuthenMaxUserCount_Object=MibTableColumn
h3cDot11MACAuthenMaxUserCount=_H3cDot11MACAuthenMaxUserCount_Object((1,3,6,1,4,1,2011,10,2,75,4,2,7,1,18),_H3cDot11MACAuthenMaxUserCount_Type())
h3cDot11MACAuthenMaxUserCount.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11MACAuthenMaxUserCount.setStatus(_A)
_H3cDot11APConfigGroup_ObjectIdentity=ObjectIdentity
h3cDot11APConfigGroup=_H3cDot11APConfigGroup_ObjectIdentity((1,3,6,1,4,1,2011,10,2,75,4,3))
_H3cDot11APTemplateTable_Object=MibTable
h3cDot11APTemplateTable=_H3cDot11APTemplateTable_Object((1,3,6,1,4,1,2011,10,2,75,4,3,1))
if mibBuilder.loadTexts:h3cDot11APTemplateTable.setStatus(_A)
_H3cDot11APTemplateEntry_Object=MibTableRow
h3cDot11APTemplateEntry=_H3cDot11APTemplateEntry_Object((1,3,6,1,4,1,2011,10,2,75,4,3,1,1))
h3cDot11APTemplateEntry.setIndexNames((0,_E,_AE))
if mibBuilder.loadTexts:h3cDot11APTemplateEntry.setStatus(_A)
class _H3cDot11APTemplateName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,127))
_H3cDot11APTemplateName_Type.__name__=_H
_H3cDot11APTemplateName_Object=MibTableColumn
h3cDot11APTemplateName=_H3cDot11APTemplateName_Object((1,3,6,1,4,1,2011,10,2,75,4,3,1,1,1),_H3cDot11APTemplateName_Type())
h3cDot11APTemplateName.setMaxAccess(_F)
if mibBuilder.loadTexts:h3cDot11APTemplateName.setStatus(_A)
_H3cDot11APSerialID_Type=OctetString
_H3cDot11APSerialID_Object=MibTableColumn
h3cDot11APSerialID=_H3cDot11APSerialID_Object((1,3,6,1,4,1,2011,10,2,75,4,3,1,1,2),_H3cDot11APSerialID_Type())
h3cDot11APSerialID.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cDot11APSerialID.setStatus(_A)
_H3cDot11TemplateAPModelAlias_Type=OctetString
_H3cDot11TemplateAPModelAlias_Object=MibTableColumn
h3cDot11TemplateAPModelAlias=_H3cDot11TemplateAPModelAlias_Object((1,3,6,1,4,1,2011,10,2,75,4,3,1,1,3),_H3cDot11TemplateAPModelAlias_Type())
h3cDot11TemplateAPModelAlias.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cDot11TemplateAPModelAlias.setStatus(_A)
_H3cDot11Description_Type=OctetString
_H3cDot11Description_Object=MibTableColumn
h3cDot11Description=_H3cDot11Description_Object((1,3,6,1,4,1,2011,10,2,75,4,3,1,1,4),_H3cDot11Description_Type())
h3cDot11Description.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cDot11Description.setStatus(_A)
class _H3cDot11APWorkMode_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_M,1),(_Y,2),(_h,3)))
_H3cDot11APWorkMode_Type.__name__=_C
_H3cDot11APWorkMode_Object=MibTableColumn
h3cDot11APWorkMode=_H3cDot11APWorkMode_Object((1,3,6,1,4,1,2011,10,2,75,4,3,1,1,5),_H3cDot11APWorkMode_Type())
h3cDot11APWorkMode.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cDot11APWorkMode.setStatus(_A)
_H3cDot11APTemplateRowStatus_Type=RowStatus
_H3cDot11APTemplateRowStatus_Object=MibTableColumn
h3cDot11APTemplateRowStatus=_H3cDot11APTemplateRowStatus_Object((1,3,6,1,4,1,2011,10,2,75,4,3,1,1,6),_H3cDot11APTemplateRowStatus_Type())
h3cDot11APTemplateRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cDot11APTemplateRowStatus.setStatus(_A)
_H3cDot11APName_Type=OctetString
_H3cDot11APName_Object=MibTableColumn
h3cDot11APName=_H3cDot11APName_Object((1,3,6,1,4,1,2011,10,2,75,4,3,1,1,7),_H3cDot11APName_Type())
h3cDot11APName.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cDot11APName.setStatus(_A)
_H3cDot11StatisInterv_Type=Integer32
_H3cDot11StatisInterv_Object=MibTableColumn
h3cDot11StatisInterv=_H3cDot11StatisInterv_Object((1,3,6,1,4,1,2011,10,2,75,4,3,1,1,8),_H3cDot11StatisInterv_Type())
h3cDot11StatisInterv.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cDot11StatisInterv.setStatus(_A)
if mibBuilder.loadTexts:h3cDot11StatisInterv.setUnits(_J)
class _H3cDot11APBroadcastProbeReply_Type(TruthValue):defaultValue=1
_H3cDot11APBroadcastProbeReply_Type.__name__=_G
_H3cDot11APBroadcastProbeReply_Object=MibTableColumn
h3cDot11APBroadcastProbeReply=_H3cDot11APBroadcastProbeReply_Object((1,3,6,1,4,1,2011,10,2,75,4,3,1,1,9),_H3cDot11APBroadcastProbeReply_Type())
h3cDot11APBroadcastProbeReply.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cDot11APBroadcastProbeReply.setStatus(_A)
_H3cDot11StaIdleTimerInterv_Type=Integer32
_H3cDot11StaIdleTimerInterv_Object=MibTableColumn
h3cDot11StaIdleTimerInterv=_H3cDot11StaIdleTimerInterv_Object((1,3,6,1,4,1,2011,10,2,75,4,3,1,1,10),_H3cDot11StaIdleTimerInterv_Type())
h3cDot11StaIdleTimerInterv.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cDot11StaIdleTimerInterv.setStatus(_A)
if mibBuilder.loadTexts:h3cDot11StaIdleTimerInterv.setUnits(_J)
_H3cDot11StaKeepAliveTimerInterv_Type=Integer32
_H3cDot11StaKeepAliveTimerInterv_Object=MibTableColumn
h3cDot11StaKeepAliveTimerInterv=_H3cDot11StaKeepAliveTimerInterv_Object((1,3,6,1,4,1,2011,10,2,75,4,3,1,1,11),_H3cDot11StaKeepAliveTimerInterv_Type())
h3cDot11StaKeepAliveTimerInterv.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cDot11StaKeepAliveTimerInterv.setStatus(_A)
if mibBuilder.loadTexts:h3cDot11StaKeepAliveTimerInterv.setUnits(_J)
_H3cDot11APCir_Type=Integer32
_H3cDot11APCir_Object=MibTableColumn
h3cDot11APCir=_H3cDot11APCir_Object((1,3,6,1,4,1,2011,10,2,75,4,3,1,1,12),_H3cDot11APCir_Type())
h3cDot11APCir.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cDot11APCir.setStatus(_A)
if mibBuilder.loadTexts:h3cDot11APCir.setUnits(_Q)
_H3cDot11APCbs_Type=Integer32
_H3cDot11APCbs_Object=MibTableColumn
h3cDot11APCbs=_H3cDot11APCbs_Object((1,3,6,1,4,1,2011,10,2,75,4,3,1,1,13),_H3cDot11APCbs_Type())
h3cDot11APCbs.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cDot11APCbs.setStatus(_A)
if mibBuilder.loadTexts:h3cDot11APCbs.setUnits('Bytes')
class _H3cDot11APPriorityLevel_Type(Integer32):defaultValue=4;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_H3cDot11APPriorityLevel_Type.__name__=_C
_H3cDot11APPriorityLevel_Object=MibTableColumn
h3cDot11APPriorityLevel=_H3cDot11APPriorityLevel_Object((1,3,6,1,4,1,2011,10,2,75,4,3,1,1,14),_H3cDot11APPriorityLevel_Type())
h3cDot11APPriorityLevel.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cDot11APPriorityLevel.setStatus(_A)
_H3cDot11APElementID_Type=Integer32
_H3cDot11APElementID_Object=MibTableColumn
h3cDot11APElementID=_H3cDot11APElementID_Object((1,3,6,1,4,1,2011,10,2,75,4,3,1,1,15),_H3cDot11APElementID_Type())
h3cDot11APElementID.setMaxAccess(_I)
if mibBuilder.loadTexts:h3cDot11APElementID.setStatus(_A)
class _H3cDot11APDevDetectEnable_Type(TruthValue):defaultValue=2
_H3cDot11APDevDetectEnable_Type.__name__=_G
_H3cDot11APDevDetectEnable_Object=MibTableColumn
h3cDot11APDevDetectEnable=_H3cDot11APDevDetectEnable_Object((1,3,6,1,4,1,2011,10,2,75,4,3,1,1,16),_H3cDot11APDevDetectEnable_Type())
h3cDot11APDevDetectEnable.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cDot11APDevDetectEnable.setStatus(_A)
class _H3cDot11APGetIPMethod_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_AF,1),('static',2)))
_H3cDot11APGetIPMethod_Type.__name__=_C
_H3cDot11APGetIPMethod_Object=MibTableColumn
h3cDot11APGetIPMethod=_H3cDot11APGetIPMethod_Object((1,3,6,1,4,1,2011,10,2,75,4,3,1,1,17),_H3cDot11APGetIPMethod_Type())
h3cDot11APGetIPMethod.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cDot11APGetIPMethod.setStatus(_A)
class _H3cDot11StatisIntervMode_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_M,1),('realtime',2)))
_H3cDot11StatisIntervMode_Type.__name__=_C
_H3cDot11StatisIntervMode_Object=MibTableColumn
h3cDot11StatisIntervMode=_H3cDot11StatisIntervMode_Object((1,3,6,1,4,1,2011,10,2,75,4,3,1,1,18),_H3cDot11StatisIntervMode_Type())
h3cDot11StatisIntervMode.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cDot11StatisIntervMode.setStatus(_A)
class _H3cDot11ApTrapEnabled_Type(TruthValue):defaultValue=1
_H3cDot11ApTrapEnabled_Type.__name__=_G
_H3cDot11ApTrapEnabled_Object=MibTableColumn
h3cDot11ApTrapEnabled=_H3cDot11ApTrapEnabled_Object((1,3,6,1,4,1,2011,10,2,75,4,3,1,1,19),_H3cDot11ApTrapEnabled_Type())
h3cDot11ApTrapEnabled.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11ApTrapEnabled.setStatus(_A)
class _H3cDot11ApFmwUpdState_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_N,1),(_O,2),('inherit',3)))
_H3cDot11ApFmwUpdState_Type.__name__=_C
_H3cDot11ApFmwUpdState_Object=MibTableColumn
h3cDot11ApFmwUpdState=_H3cDot11ApFmwUpdState_Object((1,3,6,1,4,1,2011,10,2,75,4,3,1,1,20),_H3cDot11ApFmwUpdState_Type())
h3cDot11ApFmwUpdState.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cDot11ApFmwUpdState.setStatus(_A)
class _H3cDot11StatisIntervModeCM_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_S,0),(_T,1)))
_H3cDot11StatisIntervModeCM_Type.__name__=_C
_H3cDot11StatisIntervModeCM_Object=MibTableColumn
h3cDot11StatisIntervModeCM=_H3cDot11StatisIntervModeCM_Object((1,3,6,1,4,1,2011,10,2,75,4,3,1,1,21),_H3cDot11StatisIntervModeCM_Type())
h3cDot11StatisIntervModeCM.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cDot11StatisIntervModeCM.setStatus(_A)
_H3cDot11ApNasIDCM_Type=OctetString
_H3cDot11ApNasIDCM_Object=MibTableColumn
h3cDot11ApNasIDCM=_H3cDot11ApNasIDCM_Object((1,3,6,1,4,1,2011,10,2,75,4,3,1,1,22),_H3cDot11ApNasIDCM_Type())
h3cDot11ApNasIDCM.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cDot11ApNasIDCM.setStatus(_A)
class _H3cDot11ApCoveragetype_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('school',1),('traffic',2),('shopping',3),('company',4)))
_H3cDot11ApCoveragetype_Type.__name__=_C
_H3cDot11ApCoveragetype_Object=MibTableColumn
h3cDot11ApCoveragetype=_H3cDot11ApCoveragetype_Object((1,3,6,1,4,1,2011,10,2,75,4,3,1,1,23),_H3cDot11ApCoveragetype_Type())
h3cDot11ApCoveragetype.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cDot11ApCoveragetype.setStatus(_A)
class _H3cDot11APControlAddressState_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_N,1),(_O,2)))
_H3cDot11APControlAddressState_Type.__name__=_C
_H3cDot11APControlAddressState_Object=MibTableColumn
h3cDot11APControlAddressState=_H3cDot11APControlAddressState_Object((1,3,6,1,4,1,2011,10,2,75,4,3,1,1,24),_H3cDot11APControlAddressState_Type())
h3cDot11APControlAddressState.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cDot11APControlAddressState.setStatus(_A)
_H3cDot11APControlAddressIPv4_Type=IpAddress
_H3cDot11APControlAddressIPv4_Object=MibTableColumn
h3cDot11APControlAddressIPv4=_H3cDot11APControlAddressIPv4_Object((1,3,6,1,4,1,2011,10,2,75,4,3,1,1,25),_H3cDot11APControlAddressIPv4_Type())
h3cDot11APControlAddressIPv4.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cDot11APControlAddressIPv4.setStatus(_A)
_H3cDot11APControlAddressIPv6_Type=OctetString
_H3cDot11APControlAddressIPv6_Object=MibTableColumn
h3cDot11APControlAddressIPv6=_H3cDot11APControlAddressIPv6_Object((1,3,6,1,4,1,2011,10,2,75,4,3,1,1,26),_H3cDot11APControlAddressIPv6_Type())
h3cDot11APControlAddressIPv6.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cDot11APControlAddressIPv6.setStatus(_A)
_H3cDot11APLocalACName_Type=OctetString
_H3cDot11APLocalACName_Object=MibTableColumn
h3cDot11APLocalACName=_H3cDot11APLocalACName_Object((1,3,6,1,4,1,2011,10,2,75,4,3,1,1,27),_H3cDot11APLocalACName_Type())
h3cDot11APLocalACName.setMaxAccess(_I)
if mibBuilder.loadTexts:h3cDot11APLocalACName.setStatus(_A)
_H3cDot11APEchoInterval_Type=Integer32
_H3cDot11APEchoInterval_Object=MibTableColumn
h3cDot11APEchoInterval=_H3cDot11APEchoInterval_Object((1,3,6,1,4,1,2011,10,2,75,4,3,1,1,28),_H3cDot11APEchoInterval_Type())
h3cDot11APEchoInterval.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11APEchoInterval.setStatus(_A)
_H3cDot11RadioToConfigTable_Object=MibTable
h3cDot11RadioToConfigTable=_H3cDot11RadioToConfigTable_Object((1,3,6,1,4,1,2011,10,2,75,4,3,2))
if mibBuilder.loadTexts:h3cDot11RadioToConfigTable.setStatus(_A)
_H3cDot11RadioToConfigEntry_Object=MibTableRow
h3cDot11RadioToConfigEntry=_H3cDot11RadioToConfigEntry_Object((1,3,6,1,4,1,2011,10,2,75,4,3,2,1))
h3cDot11RadioToConfigEntry.setIndexNames((0,_E,_n),(0,_E,_a))
if mibBuilder.loadTexts:h3cDot11RadioToConfigEntry.setStatus(_A)
class _H3cDot11APTemplateNameCfg_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,127))
_H3cDot11APTemplateNameCfg_Type.__name__=_H
_H3cDot11APTemplateNameCfg_Object=MibTableColumn
h3cDot11APTemplateNameCfg=_H3cDot11APTemplateNameCfg_Object((1,3,6,1,4,1,2011,10,2,75,4,3,2,1,1),_H3cDot11APTemplateNameCfg_Type())
h3cDot11APTemplateNameCfg.setMaxAccess(_F)
if mibBuilder.loadTexts:h3cDot11APTemplateNameCfg.setStatus(_A)
_H3cDot11CfgRadioID_Type=H3cDot11RadioScopeType
_H3cDot11CfgRadioID_Object=MibTableColumn
h3cDot11CfgRadioID=_H3cDot11CfgRadioID_Object((1,3,6,1,4,1,2011,10,2,75,4,3,2,1,2),_H3cDot11CfgRadioID_Type())
h3cDot11CfgRadioID.setMaxAccess(_F)
if mibBuilder.loadTexts:h3cDot11CfgRadioID.setStatus(_A)
_H3cDot11CfgRadioPolicyName_Type=OctetString
_H3cDot11CfgRadioPolicyName_Object=MibTableColumn
h3cDot11CfgRadioPolicyName=_H3cDot11CfgRadioPolicyName_Object((1,3,6,1,4,1,2011,10,2,75,4,3,2,1,3),_H3cDot11CfgRadioPolicyName_Type())
h3cDot11CfgRadioPolicyName.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11CfgRadioPolicyName.setStatus(_A)
_H3cDot11CfgRadioType_Type=H3cDot11RadioType
_H3cDot11CfgRadioType_Object=MibTableColumn
h3cDot11CfgRadioType=_H3cDot11CfgRadioType_Object((1,3,6,1,4,1,2011,10,2,75,4,3,2,1,4),_H3cDot11CfgRadioType_Type())
h3cDot11CfgRadioType.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11CfgRadioType.setStatus(_A)
_H3cDot11CfgChannel_Type=H3cDot11ChannelScopeType
_H3cDot11CfgChannel_Object=MibTableColumn
h3cDot11CfgChannel=_H3cDot11CfgChannel_Object((1,3,6,1,4,1,2011,10,2,75,4,3,2,1,5),_H3cDot11CfgChannel_Type())
h3cDot11CfgChannel.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11CfgChannel.setStatus(_A)
_H3cDot11CfgMaxTxPowerLevel_Type=H3cDot11TxPwrLevelScopeType
_H3cDot11CfgMaxTxPowerLevel_Object=MibTableColumn
h3cDot11CfgMaxTxPowerLevel=_H3cDot11CfgMaxTxPowerLevel_Object((1,3,6,1,4,1,2011,10,2,75,4,3,2,1,6),_H3cDot11CfgMaxTxPowerLevel_Type())
h3cDot11CfgMaxTxPowerLevel.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11CfgMaxTxPowerLevel.setStatus(_A)
if mibBuilder.loadTexts:h3cDot11CfgMaxTxPowerLevel.setUnits(_R)
class _H3cDot11PreambleLen_Type(H3cDot11PreambleType):defaultValue=2
_H3cDot11PreambleLen_Type.__name__=_V
_H3cDot11PreambleLen_Object=MibTableColumn
h3cDot11PreambleLen=_H3cDot11PreambleLen_Object((1,3,6,1,4,1,2011,10,2,75,4,3,2,1,7),_H3cDot11PreambleLen_Type())
h3cDot11PreambleLen.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11PreambleLen.setStatus(_A)
_H3cDot11CfgRadioStatus_Type=TruthValue
_H3cDot11CfgRadioStatus_Object=MibTableColumn
h3cDot11CfgRadioStatus=_H3cDot11CfgRadioStatus_Object((1,3,6,1,4,1,2011,10,2,75,4,3,2,1,8),_H3cDot11CfgRadioStatus_Type())
h3cDot11CfgRadioStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11CfgRadioStatus.setStatus(_A)
_H3cDot11CfgRdElementID_Type=Unsigned32
_H3cDot11CfgRdElementID_Object=MibTableColumn
h3cDot11CfgRdElementID=_H3cDot11CfgRdElementID_Object((1,3,6,1,4,1,2011,10,2,75,4,3,2,1,9),_H3cDot11CfgRdElementID_Type())
h3cDot11CfgRdElementID.setMaxAccess(_I)
if mibBuilder.loadTexts:h3cDot11CfgRdElementID.setStatus(_A)
_H3cDot11CfgWorkMode_Type=H3cDot11WorkMode
_H3cDot11CfgWorkMode_Object=MibTableColumn
h3cDot11CfgWorkMode=_H3cDot11CfgWorkMode_Object((1,3,6,1,4,1,2011,10,2,75,4,3,2,1,10),_H3cDot11CfgWorkMode_Type())
h3cDot11CfgWorkMode.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11CfgWorkMode.setStatus(_A)
_H3cDot11CfgPwrAttValue_Type=Integer32
_H3cDot11CfgPwrAttValue_Object=MibTableColumn
h3cDot11CfgPwrAttValue=_H3cDot11CfgPwrAttValue_Object((1,3,6,1,4,1,2011,10,2,75,4,3,2,1,11),_H3cDot11CfgPwrAttValue_Type())
h3cDot11CfgPwrAttValue.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11CfgPwrAttValue.setStatus(_A)
class _H3cDot11RadioTxArithmetic_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('quality',1),('bandwidth',2)))
_H3cDot11RadioTxArithmetic_Type.__name__=_C
_H3cDot11RadioTxArithmetic_Object=MibTableColumn
h3cDot11RadioTxArithmetic=_H3cDot11RadioTxArithmetic_Object((1,3,6,1,4,1,2011,10,2,75,4,3,2,1,12),_H3cDot11RadioTxArithmetic_Type())
h3cDot11RadioTxArithmetic.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11RadioTxArithmetic.setStatus(_A)
class _H3cDot11CfgChannelLockStat_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('unlocked',1),('locked',2)))
_H3cDot11CfgChannelLockStat_Type.__name__=_C
_H3cDot11CfgChannelLockStat_Object=MibTableColumn
h3cDot11CfgChannelLockStat=_H3cDot11CfgChannelLockStat_Object((1,3,6,1,4,1,2011,10,2,75,4,3,2,1,13),_H3cDot11CfgChannelLockStat_Type())
h3cDot11CfgChannelLockStat.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11CfgChannelLockStat.setStatus(_A)
class _H3cDot11CfgPowerLockStat_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('unlocked',1),('locked',2)))
_H3cDot11CfgPowerLockStat_Type.__name__=_C
_H3cDot11CfgPowerLockStat_Object=MibTableColumn
h3cDot11CfgPowerLockStat=_H3cDot11CfgPowerLockStat_Object((1,3,6,1,4,1,2011,10,2,75,4,3,2,1,14),_H3cDot11CfgPowerLockStat_Type())
h3cDot11CfgPowerLockStat.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11CfgPowerLockStat.setStatus(_A)
_H3cDot11CfgLBRdGroupId_Type=Unsigned32
_H3cDot11CfgLBRdGroupId_Object=MibTableColumn
h3cDot11CfgLBRdGroupId=_H3cDot11CfgLBRdGroupId_Object((1,3,6,1,4,1,2011,10,2,75,4,3,2,1,15),_H3cDot11CfgLBRdGroupId_Type())
h3cDot11CfgLBRdGroupId.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11CfgLBRdGroupId.setStatus(_A)
_H3cDot11CfgRRMSDRdGroupId_Type=Unsigned32
_H3cDot11CfgRRMSDRdGroupId_Object=MibTableColumn
h3cDot11CfgRRMSDRdGroupId=_H3cDot11CfgRRMSDRdGroupId_Object((1,3,6,1,4,1,2011,10,2,75,4,3,2,1,16),_H3cDot11CfgRRMSDRdGroupId_Type())
h3cDot11CfgRRMSDRdGroupId.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11CfgRRMSDRdGroupId.setStatus(_A)
_H3cDot11CfgRadioType2_Type=H3cDot11RadioType2
_H3cDot11CfgRadioType2_Object=MibTableColumn
h3cDot11CfgRadioType2=_H3cDot11CfgRadioType2_Object((1,3,6,1,4,1,2011,10,2,75,4,3,2,1,17),_H3cDot11CfgRadioType2_Type())
h3cDot11CfgRadioType2.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11CfgRadioType2.setStatus(_A)
_H3cDot11CfgIDSEnable_Type=TruthValue
_H3cDot11CfgIDSEnable_Object=MibTableColumn
h3cDot11CfgIDSEnable=_H3cDot11CfgIDSEnable_Object((1,3,6,1,4,1,2011,10,2,75,4,3,2,1,18),_H3cDot11CfgIDSEnable_Type())
h3cDot11CfgIDSEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11CfgIDSEnable.setStatus(_A)
_H3cDot11CfgSaEnable_Type=TruthValue
_H3cDot11CfgSaEnable_Object=MibTableColumn
h3cDot11CfgSaEnable=_H3cDot11CfgSaEnable_Object((1,3,6,1,4,1,2011,10,2,75,4,3,2,1,19),_H3cDot11CfgSaEnable_Type())
h3cDot11CfgSaEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11CfgSaEnable.setStatus(_A)
_H3cDot11CfgSaCltRtFFTData_Type=TruthValue
_H3cDot11CfgSaCltRtFFTData_Object=MibTableColumn
h3cDot11CfgSaCltRtFFTData=_H3cDot11CfgSaCltRtFFTData_Object((1,3,6,1,4,1,2011,10,2,75,4,3,2,1,20),_H3cDot11CfgSaCltRtFFTData_Type())
h3cDot11CfgSaCltRtFFTData.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11CfgSaCltRtFFTData.setStatus(_A)
class _H3cDot11CfgSaBand_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('dot11g',1),('dot11aLower',2),('dot11aMiddle',3),('dot11aUpper',4)))
_H3cDot11CfgSaBand_Type.__name__=_C
_H3cDot11CfgSaBand_Object=MibTableColumn
h3cDot11CfgSaBand=_H3cDot11CfgSaBand_Object((1,3,6,1,4,1,2011,10,2,75,4,3,2,1,21),_H3cDot11CfgSaBand_Type())
h3cDot11CfgSaBand.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11CfgSaBand.setStatus(_A)
class _H3cDot11CfgSaRptDevType_Type(Bits):namedValues=NamedValues(*((_AG,0),(_AH,1),(_AI,2),(_AJ,3),(_AK,4),(_AL,5),(_AM,6),(_AN,7),(_AO,8),(_AP,9),(_AQ,10),(_AR,11)))
_H3cDot11CfgSaRptDevType_Type.__name__=_f
_H3cDot11CfgSaRptDevType_Object=MibTableColumn
h3cDot11CfgSaRptDevType=_H3cDot11CfgSaRptDevType_Object((1,3,6,1,4,1,2011,10,2,75,4,3,2,1,22),_H3cDot11CfgSaRptDevType_Type())
h3cDot11CfgSaRptDevType.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11CfgSaRptDevType.setStatus(_A)
_H3cDot11CfgSaTrapDevEnable_Type=TruthValue
_H3cDot11CfgSaTrapDevEnable_Object=MibTableColumn
h3cDot11CfgSaTrapDevEnable=_H3cDot11CfgSaTrapDevEnable_Object((1,3,6,1,4,1,2011,10,2,75,4,3,2,1,23),_H3cDot11CfgSaTrapDevEnable_Type())
h3cDot11CfgSaTrapDevEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11CfgSaTrapDevEnable.setStatus(_A)
class _H3cDot11CfgSaTrapDevType_Type(Bits):namedValues=NamedValues(*((_AG,0),(_AH,1),(_AI,2),(_AJ,3),(_AK,4),(_AL,5),(_AM,6),(_AN,7),(_AO,8),(_AP,9),(_AQ,10),(_AR,11)))
_H3cDot11CfgSaTrapDevType_Type.__name__=_f
_H3cDot11CfgSaTrapDevType_Object=MibTableColumn
h3cDot11CfgSaTrapDevType=_H3cDot11CfgSaTrapDevType_Object((1,3,6,1,4,1,2011,10,2,75,4,3,2,1,24),_H3cDot11CfgSaTrapDevType_Type())
h3cDot11CfgSaTrapDevType.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11CfgSaTrapDevType.setStatus(_A)
_H3cDot11CfgSaTrapAQEnable_Type=TruthValue
_H3cDot11CfgSaTrapAQEnable_Object=MibTableColumn
h3cDot11CfgSaTrapAQEnable=_H3cDot11CfgSaTrapAQEnable_Object((1,3,6,1,4,1,2011,10,2,75,4,3,2,1,25),_H3cDot11CfgSaTrapAQEnable_Type())
h3cDot11CfgSaTrapAQEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11CfgSaTrapAQEnable.setStatus(_A)
class _H3cDot11CfgSaTrapAQThreshold_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,100))
_H3cDot11CfgSaTrapAQThreshold_Type.__name__=_C
_H3cDot11CfgSaTrapAQThreshold_Object=MibTableColumn
h3cDot11CfgSaTrapAQThreshold=_H3cDot11CfgSaTrapAQThreshold_Object((1,3,6,1,4,1,2011,10,2,75,4,3,2,1,26),_H3cDot11CfgSaTrapAQThreshold_Type())
h3cDot11CfgSaTrapAQThreshold.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11CfgSaTrapAQThreshold.setStatus(_A)
_H3cDot11CfgSaDrivenRRMEnable_Type=TruthValue
_H3cDot11CfgSaDrivenRRMEnable_Object=MibTableColumn
h3cDot11CfgSaDrivenRRMEnable=_H3cDot11CfgSaDrivenRRMEnable_Object((1,3,6,1,4,1,2011,10,2,75,4,3,2,1,27),_H3cDot11CfgSaDrivenRRMEnable_Type())
h3cDot11CfgSaDrivenRRMEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11CfgSaDrivenRRMEnable.setStatus(_A)
class _H3cDot11CfgSaDrivenRRMSnt_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('low',1),('medium',2),('high',3)))
_H3cDot11CfgSaDrivenRRMSnt_Type.__name__=_C
_H3cDot11CfgSaDrivenRRMSnt_Object=MibTableColumn
h3cDot11CfgSaDrivenRRMSnt=_H3cDot11CfgSaDrivenRRMSnt_Object((1,3,6,1,4,1,2011,10,2,75,4,3,2,1,28),_H3cDot11CfgSaDrivenRRMSnt_Type())
h3cDot11CfgSaDrivenRRMSnt.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11CfgSaDrivenRRMSnt.setStatus(_A)
_H3cDot11APServiceSetTable_Object=MibTable
h3cDot11APServiceSetTable=_H3cDot11APServiceSetTable_Object((1,3,6,1,4,1,2011,10,2,75,4,3,3))
if mibBuilder.loadTexts:h3cDot11APServiceSetTable.setStatus(_A)
_H3cDot11APServiceSetEntry_Object=MibTableRow
h3cDot11APServiceSetEntry=_H3cDot11APServiceSetEntry_Object((1,3,6,1,4,1,2011,10,2,75,4,3,3,1))
h3cDot11APServiceSetEntry.setIndexNames((0,_E,_n),(0,_E,_a),(0,_E,_o))
if mibBuilder.loadTexts:h3cDot11APServiceSetEntry.setStatus(_A)
_H3cDot11CfgServicePolicyID_Type=H3cDot11ServicePolicyIDType
_H3cDot11CfgServicePolicyID_Object=MibTableColumn
h3cDot11CfgServicePolicyID=_H3cDot11CfgServicePolicyID_Object((1,3,6,1,4,1,2011,10,2,75,4,3,3,1,1),_H3cDot11CfgServicePolicyID_Type())
h3cDot11CfgServicePolicyID.setMaxAccess(_F)
if mibBuilder.loadTexts:h3cDot11CfgServicePolicyID.setStatus(_A)
_H3cDot11SrvSetRowStatus_Type=RowStatus
_H3cDot11SrvSetRowStatus_Object=MibTableColumn
h3cDot11SrvSetRowStatus=_H3cDot11SrvSetRowStatus_Object((1,3,6,1,4,1,2011,10,2,75,4,3,3,1,2),_H3cDot11SrvSetRowStatus_Type())
h3cDot11SrvSetRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cDot11SrvSetRowStatus.setStatus(_A)
class _H3cDot11ServiceSetVlanId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4094))
_H3cDot11ServiceSetVlanId_Type.__name__=_C
_H3cDot11ServiceSetVlanId_Object=MibTableColumn
h3cDot11ServiceSetVlanId=_H3cDot11ServiceSetVlanId_Object((1,3,6,1,4,1,2011,10,2,75,4,3,3,1,3),_H3cDot11ServiceSetVlanId_Type())
h3cDot11ServiceSetVlanId.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cDot11ServiceSetVlanId.setStatus(_A)
_H3cDot11APSysInfoSetTable_Object=MibTable
h3cDot11APSysInfoSetTable=_H3cDot11APSysInfoSetTable_Object((1,3,6,1,4,1,2011,10,2,75,4,3,4))
if mibBuilder.loadTexts:h3cDot11APSysInfoSetTable.setStatus(_A)
_H3cDot11APSysInfoSetEntry_Object=MibTableRow
h3cDot11APSysInfoSetEntry=_H3cDot11APSysInfoSetEntry_Object((1,3,6,1,4,1,2011,10,2,75,4,3,4,1))
h3cDot11APSysInfoSetEntry.setIndexNames((0,_E,_b))
if mibBuilder.loadTexts:h3cDot11APSysInfoSetEntry.setStatus(_A)
class _H3cDot11APSysNetID_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,127))
_H3cDot11APSysNetID_Type.__name__=_H
_H3cDot11APSysNetID_Object=MibTableColumn
h3cDot11APSysNetID=_H3cDot11APSysNetID_Object((1,3,6,1,4,1,2011,10,2,75,4,3,4,1,1),_H3cDot11APSysNetID_Type())
h3cDot11APSysNetID.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11APSysNetID.setStatus(_A)
class _H3cDot11APCpuUsageThreshold_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_H3cDot11APCpuUsageThreshold_Type.__name__=_C
_H3cDot11APCpuUsageThreshold_Object=MibTableColumn
h3cDot11APCpuUsageThreshold=_H3cDot11APCpuUsageThreshold_Object((1,3,6,1,4,1,2011,10,2,75,4,3,4,1,2),_H3cDot11APCpuUsageThreshold_Type())
h3cDot11APCpuUsageThreshold.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11APCpuUsageThreshold.setStatus(_A)
if mibBuilder.loadTexts:h3cDot11APCpuUsageThreshold.setUnits(_X)
class _H3cDot11APMemUsageThreshold_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_H3cDot11APMemUsageThreshold_Type.__name__=_C
_H3cDot11APMemUsageThreshold_Object=MibTableColumn
h3cDot11APMemUsageThreshold=_H3cDot11APMemUsageThreshold_Object((1,3,6,1,4,1,2011,10,2,75,4,3,4,1,3),_H3cDot11APMemUsageThreshold_Type())
h3cDot11APMemUsageThreshold.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11APMemUsageThreshold.setStatus(_A)
if mibBuilder.loadTexts:h3cDot11APMemUsageThreshold.setUnits(_X)
_H3cDot11APLimitTable_Object=MibTable
h3cDot11APLimitTable=_H3cDot11APLimitTable_Object((1,3,6,1,4,1,2011,10,2,75,4,3,5))
if mibBuilder.loadTexts:h3cDot11APLimitTable.setStatus(_A)
_H3cDot11APLimitEntry_Object=MibTableRow
h3cDot11APLimitEntry=_H3cDot11APLimitEntry_Object((1,3,6,1,4,1,2011,10,2,75,4,3,5,1))
h3cDot11APLimitEntry.setIndexNames((0,_c,_e))
if mibBuilder.loadTexts:h3cDot11APLimitEntry.setStatus(_A)
class _H3cDot11APSsidNumLimit_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_H3cDot11APSsidNumLimit_Type.__name__=_C
_H3cDot11APSsidNumLimit_Object=MibTableColumn
h3cDot11APSsidNumLimit=_H3cDot11APSsidNumLimit_Object((1,3,6,1,4,1,2011,10,2,75,4,3,5,1,1),_H3cDot11APSsidNumLimit_Type())
h3cDot11APSsidNumLimit.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11APSsidNumLimit.setStatus(_A)
class _H3cDot11APUserCntLimit_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_H3cDot11APUserCntLimit_Type.__name__=_C
_H3cDot11APUserCntLimit_Object=MibTableColumn
h3cDot11APUserCntLimit=_H3cDot11APUserCntLimit_Object((1,3,6,1,4,1,2011,10,2,75,4,3,5,1,2),_H3cDot11APUserCntLimit_Type())
h3cDot11APUserCntLimit.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11APUserCntLimit.setStatus(_A)
class _H3cDot11APUserThreshold_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_H3cDot11APUserThreshold_Type.__name__=_C
_H3cDot11APUserThreshold_Object=MibTableColumn
h3cDot11APUserThreshold=_H3cDot11APUserThreshold_Object((1,3,6,1,4,1,2011,10,2,75,4,3,5,1,3),_H3cDot11APUserThreshold_Type())
h3cDot11APUserThreshold.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11APUserThreshold.setStatus(_A)
_H3cDot11APIfSetTable_Object=MibTable
h3cDot11APIfSetTable=_H3cDot11APIfSetTable_Object((1,3,6,1,4,1,2011,10,2,75,4,3,6))
if mibBuilder.loadTexts:h3cDot11APIfSetTable.setStatus(_A)
_H3cDot11APIfSetEntry_Object=MibTableRow
h3cDot11APIfSetEntry=_H3cDot11APIfSetEntry_Object((1,3,6,1,4,1,2011,10,2,75,4,3,6,1))
h3cDot11APIfSetEntry.setIndexNames((0,_c,_e),(0,_E,_AS))
if mibBuilder.loadTexts:h3cDot11APIfSetEntry.setStatus(_A)
_H3cDot11APSetIfIndex_Type=Integer32
_H3cDot11APSetIfIndex_Object=MibTableColumn
h3cDot11APSetIfIndex=_H3cDot11APSetIfIndex_Object((1,3,6,1,4,1,2011,10,2,75,4,3,6,1,1),_H3cDot11APSetIfIndex_Type())
h3cDot11APSetIfIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:h3cDot11APSetIfIndex.setStatus(_A)
_H3cDot11APIfAlias_Type=DisplayString
_H3cDot11APIfAlias_Object=MibTableColumn
h3cDot11APIfAlias=_H3cDot11APIfAlias_Object((1,3,6,1,4,1,2011,10,2,75,4,3,6,1,2),_H3cDot11APIfAlias_Type())
h3cDot11APIfAlias.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11APIfAlias.setStatus(_A)
_H3cDot11APServiceVlanTable_Object=MibTable
h3cDot11APServiceVlanTable=_H3cDot11APServiceVlanTable_Object((1,3,6,1,4,1,2011,10,2,75,4,3,7))
if mibBuilder.loadTexts:h3cDot11APServiceVlanTable.setStatus(_A)
_H3cDot11APServiceVlanEntry_Object=MibTableRow
h3cDot11APServiceVlanEntry=_H3cDot11APServiceVlanEntry_Object((1,3,6,1,4,1,2011,10,2,75,4,3,7,1))
h3cDot11APServiceVlanEntry.setIndexNames((0,_E,_AT),(0,_E,_AU))
if mibBuilder.loadTexts:h3cDot11APServiceVlanEntry.setStatus(_A)
_H3cDot11APServiceVlanSerialID_Type=OctetString
_H3cDot11APServiceVlanSerialID_Object=MibTableColumn
h3cDot11APServiceVlanSerialID=_H3cDot11APServiceVlanSerialID_Object((1,3,6,1,4,1,2011,10,2,75,4,3,7,1,1),_H3cDot11APServiceVlanSerialID_Type())
h3cDot11APServiceVlanSerialID.setMaxAccess(_F)
if mibBuilder.loadTexts:h3cDot11APServiceVlanSerialID.setStatus(_A)
_H3cDot11APServiceVlanSPID_Type=H3cDot11ServicePolicyIDType
_H3cDot11APServiceVlanSPID_Object=MibTableColumn
h3cDot11APServiceVlanSPID=_H3cDot11APServiceVlanSPID_Object((1,3,6,1,4,1,2011,10,2,75,4,3,7,1,2),_H3cDot11APServiceVlanSPID_Type())
h3cDot11APServiceVlanSPID.setMaxAccess(_F)
if mibBuilder.loadTexts:h3cDot11APServiceVlanSPID.setStatus(_A)
class _H3cDot11APServiceVlanId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4094))
_H3cDot11APServiceVlanId_Type.__name__=_C
_H3cDot11APServiceVlanId_Object=MibTableColumn
h3cDot11APServiceVlanId=_H3cDot11APServiceVlanId_Object((1,3,6,1,4,1,2011,10,2,75,4,3,7,1,3),_H3cDot11APServiceVlanId_Type())
h3cDot11APServiceVlanId.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cDot11APServiceVlanId.setStatus(_A)
_H3cDot11APServiceVlanRowStatus_Type=RowStatus
_H3cDot11APServiceVlanRowStatus_Object=MibTableColumn
h3cDot11APServiceVlanRowStatus=_H3cDot11APServiceVlanRowStatus_Object((1,3,6,1,4,1,2011,10,2,75,4,3,7,1,4),_H3cDot11APServiceVlanRowStatus_Type())
h3cDot11APServiceVlanRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cDot11APServiceVlanRowStatus.setStatus(_A)
_H3cDot11RadioConfigTable_Object=MibTable
h3cDot11RadioConfigTable=_H3cDot11RadioConfigTable_Object((1,3,6,1,4,1,2011,10,2,75,4,3,8))
if mibBuilder.loadTexts:h3cDot11RadioConfigTable.setStatus(_A)
_H3cDot11RadioConfigEntry_Object=MibTableRow
h3cDot11RadioConfigEntry=_H3cDot11RadioConfigEntry_Object((1,3,6,1,4,1,2011,10,2,75,4,3,8,1))
h3cDot11RadioConfigEntry.setIndexNames((0,_E,_AV),(0,_E,_AW))
if mibBuilder.loadTexts:h3cDot11RadioConfigEntry.setStatus(_A)
class _H3cDot11RCAPSerialID_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,127))
_H3cDot11RCAPSerialID_Type.__name__=_H
_H3cDot11RCAPSerialID_Object=MibTableColumn
h3cDot11RCAPSerialID=_H3cDot11RCAPSerialID_Object((1,3,6,1,4,1,2011,10,2,75,4,3,8,1,1),_H3cDot11RCAPSerialID_Type())
h3cDot11RCAPSerialID.setMaxAccess(_F)
if mibBuilder.loadTexts:h3cDot11RCAPSerialID.setStatus(_A)
_H3cDot11RCRadioID_Type=H3cDot11RadioScopeType
_H3cDot11RCRadioID_Object=MibTableColumn
h3cDot11RCRadioID=_H3cDot11RCRadioID_Object((1,3,6,1,4,1,2011,10,2,75,4,3,8,1,2),_H3cDot11RCRadioID_Type())
h3cDot11RCRadioID.setMaxAccess(_F)
if mibBuilder.loadTexts:h3cDot11RCRadioID.setStatus(_A)
_H3cDot11RCRadioType_Type=H3cDot11RadioType
_H3cDot11RCRadioType_Object=MibTableColumn
h3cDot11RCRadioType=_H3cDot11RCRadioType_Object((1,3,6,1,4,1,2011,10,2,75,4,3,8,1,3),_H3cDot11RCRadioType_Type())
h3cDot11RCRadioType.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11RCRadioType.setStatus(_A)
_H3cDot11RCChannel_Type=H3cDot11ChannelScopeType
_H3cDot11RCChannel_Object=MibTableColumn
h3cDot11RCChannel=_H3cDot11RCChannel_Object((1,3,6,1,4,1,2011,10,2,75,4,3,8,1,4),_H3cDot11RCChannel_Type())
h3cDot11RCChannel.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11RCChannel.setStatus(_A)
class _H3cDot11RCPreambleLen_Type(H3cDot11PreambleType):defaultValue=2
_H3cDot11RCPreambleLen_Type.__name__=_V
_H3cDot11RCPreambleLen_Object=MibTableColumn
h3cDot11RCPreambleLen=_H3cDot11RCPreambleLen_Object((1,3,6,1,4,1,2011,10,2,75,4,3,8,1,5),_H3cDot11RCPreambleLen_Type())
h3cDot11RCPreambleLen.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11RCPreambleLen.setStatus(_A)
_H3cDot11RCPwrAttValue_Type=Integer32
_H3cDot11RCPwrAttValue_Object=MibTableColumn
h3cDot11RCPwrAttValue=_H3cDot11RCPwrAttValue_Object((1,3,6,1,4,1,2011,10,2,75,4,3,8,1,6),_H3cDot11RCPwrAttValue_Type())
h3cDot11RCPwrAttValue.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11RCPwrAttValue.setStatus(_A)
_H3cDot11RCApPowerLevel_Type=H3cDot11TxPwrLevelScopeType
_H3cDot11RCApPowerLevel_Object=MibTableColumn
h3cDot11RCApPowerLevel=_H3cDot11RCApPowerLevel_Object((1,3,6,1,4,1,2011,10,2,75,4,3,8,1,7),_H3cDot11RCApPowerLevel_Type())
h3cDot11RCApPowerLevel.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11RCApPowerLevel.setStatus(_A)
if mibBuilder.loadTexts:h3cDot11RCApPowerLevel.setUnits(_R)
_H3cDot11RCDynamicChlState_Type=TruthValue
_H3cDot11RCDynamicChlState_Object=MibTableColumn
h3cDot11RCDynamicChlState=_H3cDot11RCDynamicChlState_Object((1,3,6,1,4,1,2011,10,2,75,4,3,8,1,8),_H3cDot11RCDynamicChlState_Type())
h3cDot11RCDynamicChlState.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11RCDynamicChlState.setStatus(_A)
_H3cDot11RCDynamicPowerState_Type=TruthValue
_H3cDot11RCDynamicPowerState_Object=MibTableColumn
h3cDot11RCDynamicPowerState=_H3cDot11RCDynamicPowerState_Object((1,3,6,1,4,1,2011,10,2,75,4,3,8,1,9),_H3cDot11RCDynamicPowerState_Type())
h3cDot11RCDynamicPowerState.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11RCDynamicPowerState.setStatus(_A)
_H3cDot11RCRadioStatus_Type=TruthValue
_H3cDot11RCRadioStatus_Object=MibTableColumn
h3cDot11RCRadioStatus=_H3cDot11RCRadioStatus_Object((1,3,6,1,4,1,2011,10,2,75,4,3,8,1,10),_H3cDot11RCRadioStatus_Type())
h3cDot11RCRadioStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11RCRadioStatus.setStatus(_A)
class _H3cDot11RCRadioRate_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_H3cDot11RCRadioRate_Type.__name__=_H
_H3cDot11RCRadioRate_Object=MibTableColumn
h3cDot11RCRadioRate=_H3cDot11RCRadioRate_Object((1,3,6,1,4,1,2011,10,2,75,4,3,8,1,11),_H3cDot11RCRadioRate_Type())
h3cDot11RCRadioRate.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11RCRadioRate.setStatus(_A)
_H3cDot11RCPwrAdjustStepLength_Type=Integer32
_H3cDot11RCPwrAdjustStepLength_Object=MibTableColumn
h3cDot11RCPwrAdjustStepLength=_H3cDot11RCPwrAdjustStepLength_Object((1,3,6,1,4,1,2011,10,2,75,4,3,8,1,12),_H3cDot11RCPwrAdjustStepLength_Type())
h3cDot11RCPwrAdjustStepLength.setMaxAccess(_I)
if mibBuilder.loadTexts:h3cDot11RCPwrAdjustStepLength.setStatus(_A)
_H3cDot11RCRadioType2_Type=H3cDot11RadioType2
_H3cDot11RCRadioType2_Object=MibTableColumn
h3cDot11RCRadioType2=_H3cDot11RCRadioType2_Object((1,3,6,1,4,1,2011,10,2,75,4,3,8,1,13),_H3cDot11RCRadioType2_Type())
h3cDot11RCRadioType2.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11RCRadioType2.setStatus(_A)
class _H3cDot11RCPreambleLenCM_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('long',0),('short',1)))
_H3cDot11RCPreambleLenCM_Type.__name__=_C
_H3cDot11RCPreambleLenCM_Object=MibTableColumn
h3cDot11RCPreambleLenCM=_H3cDot11RCPreambleLenCM_Object((1,3,6,1,4,1,2011,10,2,75,4,3,8,1,14),_H3cDot11RCPreambleLenCM_Type())
h3cDot11RCPreambleLenCM.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11RCPreambleLenCM.setStatus(_A)
class _H3cDot11RCDynamicChlStateCM_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_S,0),(_T,1)))
_H3cDot11RCDynamicChlStateCM_Type.__name__=_C
_H3cDot11RCDynamicChlStateCM_Object=MibTableColumn
h3cDot11RCDynamicChlStateCM=_H3cDot11RCDynamicChlStateCM_Object((1,3,6,1,4,1,2011,10,2,75,4,3,8,1,15),_H3cDot11RCDynamicChlStateCM_Type())
h3cDot11RCDynamicChlStateCM.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11RCDynamicChlStateCM.setStatus(_A)
class _H3cDot11RCRadioStatusCM_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('up',1),('down',2),('testing',3)))
_H3cDot11RCRadioStatusCM_Type.__name__=_C
_H3cDot11RCRadioStatusCM_Object=MibTableColumn
h3cDot11RCRadioStatusCM=_H3cDot11RCRadioStatusCM_Object((1,3,6,1,4,1,2011,10,2,75,4,3,8,1,16),_H3cDot11RCRadioStatusCM_Type())
h3cDot11RCRadioStatusCM.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11RCRadioStatusCM.setStatus(_A)
class _H3cDot11RCRadioRateCM_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_H3cDot11RCRadioRateCM_Type.__name__=_H
_H3cDot11RCRadioRateCM_Object=MibTableColumn
h3cDot11RCRadioRateCM=_H3cDot11RCRadioRateCM_Object((1,3,6,1,4,1,2011,10,2,75,4,3,8,1,17),_H3cDot11RCRadioRateCM_Type())
h3cDot11RCRadioRateCM.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11RCRadioRateCM.setStatus(_A)
_H3cDot11RCDynamicPowerStateCM_Type=H3cDot11TruthValueCM
_H3cDot11RCDynamicPowerStateCM_Object=MibTableColumn
h3cDot11RCDynamicPowerStateCM=_H3cDot11RCDynamicPowerStateCM_Object((1,3,6,1,4,1,2011,10,2,75,4,3,8,1,18),_H3cDot11RCDynamicPowerStateCM_Type())
h3cDot11RCDynamicPowerStateCM.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11RCDynamicPowerStateCM.setStatus(_A)
class _H3cDot11RCRssiThresholdCM_Type(Integer32):defaultValue=1
_H3cDot11RCRssiThresholdCM_Type.__name__=_C
_H3cDot11RCRssiThresholdCM_Object=MibTableColumn
h3cDot11RCRssiThresholdCM=_H3cDot11RCRssiThresholdCM_Object((1,3,6,1,4,1,2011,10,2,75,4,3,8,1,19),_H3cDot11RCRssiThresholdCM_Type())
h3cDot11RCRssiThresholdCM.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11RCRssiThresholdCM.setStatus(_A)
if mibBuilder.loadTexts:h3cDot11RCRssiThresholdCM.setUnits('dBm')
_H3cDot11RCDynamicChlStateSelfDecisiveCM_Type=H3cDot11TruthValueCM
_H3cDot11RCDynamicChlStateSelfDecisiveCM_Object=MibTableColumn
h3cDot11RCDynamicChlStateSelfDecisiveCM=_H3cDot11RCDynamicChlStateSelfDecisiveCM_Object((1,3,6,1,4,1,2011,10,2,75,4,3,8,1,20),_H3cDot11RCDynamicChlStateSelfDecisiveCM_Type())
h3cDot11RCDynamicChlStateSelfDecisiveCM.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11RCDynamicChlStateSelfDecisiveCM.setStatus(_A)
_H3cDot11RCDynamicPowerStateSelfDecisiveCM_Type=H3cDot11TruthValueCM
_H3cDot11RCDynamicPowerStateSelfDecisiveCM_Object=MibTableColumn
h3cDot11RCDynamicPowerStateSelfDecisiveCM=_H3cDot11RCDynamicPowerStateSelfDecisiveCM_Object((1,3,6,1,4,1,2011,10,2,75,4,3,8,1,21),_H3cDot11RCDynamicPowerStateSelfDecisiveCM_Type())
h3cDot11RCDynamicPowerStateSelfDecisiveCM.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11RCDynamicPowerStateSelfDecisiveCM.setStatus(_A)
_H3cDot11RadioSSIDCfgTable_Object=MibTable
h3cDot11RadioSSIDCfgTable=_H3cDot11RadioSSIDCfgTable_Object((1,3,6,1,4,1,2011,10,2,75,4,3,9))
if mibBuilder.loadTexts:h3cDot11RadioSSIDCfgTable.setStatus(_A)
_H3cDot11RadioSSIDCfgEntry_Object=MibTableRow
h3cDot11RadioSSIDCfgEntry=_H3cDot11RadioSSIDCfgEntry_Object((1,3,6,1,4,1,2011,10,2,75,4,3,9,1))
h3cDot11RadioSSIDCfgEntry.setIndexNames((0,_E,_AX),(0,_E,_AY),(0,_E,_AZ))
if mibBuilder.loadTexts:h3cDot11RadioSSIDCfgEntry.setStatus(_A)
_H3cDot11RadioSSIDSerialID_Type=H3cDot11ObjectIDType
_H3cDot11RadioSSIDSerialID_Object=MibTableColumn
h3cDot11RadioSSIDSerialID=_H3cDot11RadioSSIDSerialID_Object((1,3,6,1,4,1,2011,10,2,75,4,3,9,1,1),_H3cDot11RadioSSIDSerialID_Type())
h3cDot11RadioSSIDSerialID.setMaxAccess(_F)
if mibBuilder.loadTexts:h3cDot11RadioSSIDSerialID.setStatus(_A)
_H3cDot11RadioSSIDRadioID_Type=H3cDot11RadioScopeType
_H3cDot11RadioSSIDRadioID_Object=MibTableColumn
h3cDot11RadioSSIDRadioID=_H3cDot11RadioSSIDRadioID_Object((1,3,6,1,4,1,2011,10,2,75,4,3,9,1,2),_H3cDot11RadioSSIDRadioID_Type())
h3cDot11RadioSSIDRadioID.setMaxAccess(_F)
if mibBuilder.loadTexts:h3cDot11RadioSSIDRadioID.setStatus(_A)
_H3cDot11RadioSSIDWLANID_Type=Integer32
_H3cDot11RadioSSIDWLANID_Object=MibTableColumn
h3cDot11RadioSSIDWLANID=_H3cDot11RadioSSIDWLANID_Object((1,3,6,1,4,1,2011,10,2,75,4,3,9,1,3),_H3cDot11RadioSSIDWLANID_Type())
h3cDot11RadioSSIDWLANID.setMaxAccess(_F)
if mibBuilder.loadTexts:h3cDot11RadioSSIDWLANID.setStatus(_A)
_H3cDot11RadioSSIDIndex_Type=H3cDot11ServicePolicyIDType
_H3cDot11RadioSSIDIndex_Object=MibTableColumn
h3cDot11RadioSSIDIndex=_H3cDot11RadioSSIDIndex_Object((1,3,6,1,4,1,2011,10,2,75,4,3,9,1,4),_H3cDot11RadioSSIDIndex_Type())
h3cDot11RadioSSIDIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cDot11RadioSSIDIndex.setStatus(_A)
_H3cDot11RadioBSSID_Type=MacAddress
_H3cDot11RadioBSSID_Object=MibTableColumn
h3cDot11RadioBSSID=_H3cDot11RadioBSSID_Object((1,3,6,1,4,1,2011,10,2,75,4,3,9,1,5),_H3cDot11RadioBSSID_Type())
h3cDot11RadioBSSID.setMaxAccess(_I)
if mibBuilder.loadTexts:h3cDot11RadioBSSID.setStatus(_A)
_H3cDot11RadioSSIDRowStatus_Type=RowStatus
_H3cDot11RadioSSIDRowStatus_Object=MibTableColumn
h3cDot11RadioSSIDRowStatus=_H3cDot11RadioSSIDRowStatus_Object((1,3,6,1,4,1,2011,10,2,75,4,3,9,1,6),_H3cDot11RadioSSIDRowStatus_Type())
h3cDot11RadioSSIDRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cDot11RadioSSIDRowStatus.setStatus(_A)
_H3cDot11APSerialIDTable_Object=MibTable
h3cDot11APSerialIDTable=_H3cDot11APSerialIDTable_Object((1,3,6,1,4,1,2011,10,2,75,4,3,10))
if mibBuilder.loadTexts:h3cDot11APSerialIDTable.setStatus(_A)
_H3cDot11APSerialIDEntry_Object=MibTableRow
h3cDot11APSerialIDEntry=_H3cDot11APSerialIDEntry_Object((1,3,6,1,4,1,2011,10,2,75,4,3,10,1))
h3cDot11APSerialIDEntry.setIndexNames((0,_E,_b))
if mibBuilder.loadTexts:h3cDot11APSerialIDEntry.setStatus(_A)
_H3cDot11SIDAPSerialID_Type=OctetString
_H3cDot11SIDAPSerialID_Object=MibTableColumn
h3cDot11SIDAPSerialID=_H3cDot11SIDAPSerialID_Object((1,3,6,1,4,1,2011,10,2,75,4,3,10,1,1),_H3cDot11SIDAPSerialID_Type())
h3cDot11SIDAPSerialID.setMaxAccess(_F)
if mibBuilder.loadTexts:h3cDot11SIDAPSerialID.setStatus(_A)
class _H3cDot11SIDAPWorkMode_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_M,1),(_Y,2),(_h,3)))
_H3cDot11SIDAPWorkMode_Type.__name__=_C
_H3cDot11SIDAPWorkMode_Object=MibTableColumn
h3cDot11SIDAPWorkMode=_H3cDot11SIDAPWorkMode_Object((1,3,6,1,4,1,2011,10,2,75,4,3,10,1,2),_H3cDot11SIDAPWorkMode_Type())
h3cDot11SIDAPWorkMode.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cDot11SIDAPWorkMode.setStatus(_A)
class _H3cDot11SIDAPGetIPMethod_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_AF,1),('static',2)))
_H3cDot11SIDAPGetIPMethod_Type.__name__=_C
_H3cDot11SIDAPGetIPMethod_Object=MibTableColumn
h3cDot11SIDAPGetIPMethod=_H3cDot11SIDAPGetIPMethod_Object((1,3,6,1,4,1,2011,10,2,75,4,3,10,1,3),_H3cDot11SIDAPGetIPMethod_Type())
h3cDot11SIDAPGetIPMethod.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cDot11SIDAPGetIPMethod.setStatus(_A)
_H3cDot11SIDAPTemplateName_Type=OctetString
_H3cDot11SIDAPTemplateName_Object=MibTableColumn
h3cDot11SIDAPTemplateName=_H3cDot11SIDAPTemplateName_Object((1,3,6,1,4,1,2011,10,2,75,4,3,10,1,4),_H3cDot11SIDAPTemplateName_Type())
h3cDot11SIDAPTemplateName.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cDot11SIDAPTemplateName.setStatus(_A)
_H3cDot11SIDModelAlias_Type=OctetString
_H3cDot11SIDModelAlias_Object=MibTableColumn
h3cDot11SIDModelAlias=_H3cDot11SIDModelAlias_Object((1,3,6,1,4,1,2011,10,2,75,4,3,10,1,5),_H3cDot11SIDModelAlias_Type())
h3cDot11SIDModelAlias.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cDot11SIDModelAlias.setStatus(_A)
_H3cDot11SIDAPDescription_Type=OctetString
_H3cDot11SIDAPDescription_Object=MibTableColumn
h3cDot11SIDAPDescription=_H3cDot11SIDAPDescription_Object((1,3,6,1,4,1,2011,10,2,75,4,3,10,1,6),_H3cDot11SIDAPDescription_Type())
h3cDot11SIDAPDescription.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cDot11SIDAPDescription.setStatus(_A)
_H3cDot11SIDRowStatus_Type=RowStatus
_H3cDot11SIDRowStatus_Object=MibTableColumn
h3cDot11SIDRowStatus=_H3cDot11SIDRowStatus_Object((1,3,6,1,4,1,2011,10,2,75,4,3,10,1,7),_H3cDot11SIDRowStatus_Type())
h3cDot11SIDRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cDot11SIDRowStatus.setStatus(_A)
_H3cDot11SIDAPName_Type=OctetString
_H3cDot11SIDAPName_Object=MibTableColumn
h3cDot11SIDAPName=_H3cDot11SIDAPName_Object((1,3,6,1,4,1,2011,10,2,75,4,3,10,1,8),_H3cDot11SIDAPName_Type())
h3cDot11SIDAPName.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cDot11SIDAPName.setStatus(_A)
_H3cDot11SIDStatisInterv_Type=Integer32
_H3cDot11SIDStatisInterv_Object=MibTableColumn
h3cDot11SIDStatisInterv=_H3cDot11SIDStatisInterv_Object((1,3,6,1,4,1,2011,10,2,75,4,3,10,1,9),_H3cDot11SIDStatisInterv_Type())
h3cDot11SIDStatisInterv.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cDot11SIDStatisInterv.setStatus(_A)
if mibBuilder.loadTexts:h3cDot11SIDStatisInterv.setUnits(_J)
class _H3cDot11SIDAPBroadcastProbeReply_Type(TruthValue):defaultValue=1
_H3cDot11SIDAPBroadcastProbeReply_Type.__name__=_G
_H3cDot11SIDAPBroadcastProbeReply_Object=MibTableColumn
h3cDot11SIDAPBroadcastProbeReply=_H3cDot11SIDAPBroadcastProbeReply_Object((1,3,6,1,4,1,2011,10,2,75,4,3,10,1,10),_H3cDot11SIDAPBroadcastProbeReply_Type())
h3cDot11SIDAPBroadcastProbeReply.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cDot11SIDAPBroadcastProbeReply.setStatus(_A)
_H3cDot11SIDAPStaIdleTimerInterv_Type=Integer32
_H3cDot11SIDAPStaIdleTimerInterv_Object=MibTableColumn
h3cDot11SIDAPStaIdleTimerInterv=_H3cDot11SIDAPStaIdleTimerInterv_Object((1,3,6,1,4,1,2011,10,2,75,4,3,10,1,11),_H3cDot11SIDAPStaIdleTimerInterv_Type())
h3cDot11SIDAPStaIdleTimerInterv.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cDot11SIDAPStaIdleTimerInterv.setStatus(_A)
if mibBuilder.loadTexts:h3cDot11SIDAPStaIdleTimerInterv.setUnits(_J)
_H3cDot11SIDStaKeepAliveTimerInterv_Type=Integer32
_H3cDot11SIDStaKeepAliveTimerInterv_Object=MibTableColumn
h3cDot11SIDStaKeepAliveTimerInterv=_H3cDot11SIDStaKeepAliveTimerInterv_Object((1,3,6,1,4,1,2011,10,2,75,4,3,10,1,12),_H3cDot11SIDStaKeepAliveTimerInterv_Type())
h3cDot11SIDStaKeepAliveTimerInterv.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cDot11SIDStaKeepAliveTimerInterv.setStatus(_A)
if mibBuilder.loadTexts:h3cDot11SIDStaKeepAliveTimerInterv.setUnits(_J)
_H3cDot11SIDAPCir_Type=Integer32
_H3cDot11SIDAPCir_Object=MibTableColumn
h3cDot11SIDAPCir=_H3cDot11SIDAPCir_Object((1,3,6,1,4,1,2011,10,2,75,4,3,10,1,13),_H3cDot11SIDAPCir_Type())
h3cDot11SIDAPCir.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cDot11SIDAPCir.setStatus(_A)
if mibBuilder.loadTexts:h3cDot11SIDAPCir.setUnits(_Q)
_H3cDot11SIDAPCbs_Type=Integer32
_H3cDot11SIDAPCbs_Object=MibTableColumn
h3cDot11SIDAPCbs=_H3cDot11SIDAPCbs_Object((1,3,6,1,4,1,2011,10,2,75,4,3,10,1,14),_H3cDot11SIDAPCbs_Type())
h3cDot11SIDAPCbs.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cDot11SIDAPCbs.setStatus(_A)
if mibBuilder.loadTexts:h3cDot11SIDAPCbs.setUnits('Bytes')
class _H3cDot11SIDAPPriorityLevel_Type(Integer32):defaultValue=4;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_H3cDot11SIDAPPriorityLevel_Type.__name__=_C
_H3cDot11SIDAPPriorityLevel_Object=MibTableColumn
h3cDot11SIDAPPriorityLevel=_H3cDot11SIDAPPriorityLevel_Object((1,3,6,1,4,1,2011,10,2,75,4,3,10,1,15),_H3cDot11SIDAPPriorityLevel_Type())
h3cDot11SIDAPPriorityLevel.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cDot11SIDAPPriorityLevel.setStatus(_A)
_H3cDot11SIDAPElementID_Type=Integer32
_H3cDot11SIDAPElementID_Object=MibTableColumn
h3cDot11SIDAPElementID=_H3cDot11SIDAPElementID_Object((1,3,6,1,4,1,2011,10,2,75,4,3,10,1,16),_H3cDot11SIDAPElementID_Type())
h3cDot11SIDAPElementID.setMaxAccess(_I)
if mibBuilder.loadTexts:h3cDot11SIDAPElementID.setStatus(_A)
class _H3cDot11SIDAPDevDetectEnable_Type(TruthValue):defaultValue=2
_H3cDot11SIDAPDevDetectEnable_Type.__name__=_G
_H3cDot11SIDAPDevDetectEnable_Object=MibTableColumn
h3cDot11SIDAPDevDetectEnable=_H3cDot11SIDAPDevDetectEnable_Object((1,3,6,1,4,1,2011,10,2,75,4,3,10,1,17),_H3cDot11SIDAPDevDetectEnable_Type())
h3cDot11SIDAPDevDetectEnable.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cDot11SIDAPDevDetectEnable.setStatus(_A)
class _H3cDot11SIDAPStatisIntervMode_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_M,1),('realtime',2)))
_H3cDot11SIDAPStatisIntervMode_Type.__name__=_C
_H3cDot11SIDAPStatisIntervMode_Object=MibTableColumn
h3cDot11SIDAPStatisIntervMode=_H3cDot11SIDAPStatisIntervMode_Object((1,3,6,1,4,1,2011,10,2,75,4,3,10,1,18),_H3cDot11SIDAPStatisIntervMode_Type())
h3cDot11SIDAPStatisIntervMode.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cDot11SIDAPStatisIntervMode.setStatus(_A)
class _H3cDot11SIDAPWorkModeCM_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_M,0),(_Y,1),('semimonitor',2)))
_H3cDot11SIDAPWorkModeCM_Type.__name__=_C
_H3cDot11SIDAPWorkModeCM_Object=MibTableColumn
h3cDot11SIDAPWorkModeCM=_H3cDot11SIDAPWorkModeCM_Object((1,3,6,1,4,1,2011,10,2,75,4,3,10,1,19),_H3cDot11SIDAPWorkModeCM_Type())
h3cDot11SIDAPWorkModeCM.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cDot11SIDAPWorkModeCM.setStatus(_A)
_H3cDot11SIDEchoInterval_Type=Integer32
_H3cDot11SIDEchoInterval_Object=MibTableColumn
h3cDot11SIDEchoInterval=_H3cDot11SIDEchoInterval_Object((1,3,6,1,4,1,2011,10,2,75,4,3,10,1,20),_H3cDot11SIDEchoInterval_Type())
h3cDot11SIDEchoInterval.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11SIDEchoInterval.setStatus(_A)
if mibBuilder.loadTexts:h3cDot11SIDEchoInterval.setUnits(_J)
_H3cDot11APSTVlanTable_Object=MibTable
h3cDot11APSTVlanTable=_H3cDot11APSTVlanTable_Object((1,3,6,1,4,1,2011,10,2,75,4,3,11))
if mibBuilder.loadTexts:h3cDot11APSTVlanTable.setStatus(_A)
_H3cDot11APSTVlanEntry_Object=MibTableRow
h3cDot11APSTVlanEntry=_H3cDot11APSTVlanEntry_Object((1,3,6,1,4,1,2011,10,2,75,4,3,11,1))
h3cDot11APSTVlanEntry.setIndexNames((0,_E,_b),(0,_E,_a),(0,_E,_o))
if mibBuilder.loadTexts:h3cDot11APSTVlanEntry.setStatus(_A)
class _H3cDot11CfgSTVLANID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4094))
_H3cDot11CfgSTVLANID_Type.__name__=_C
_H3cDot11CfgSTVLANID_Object=MibTableColumn
h3cDot11CfgSTVLANID=_H3cDot11CfgSTVLANID_Object((1,3,6,1,4,1,2011,10,2,75,4,3,11,1,1),_H3cDot11CfgSTVLANID_Type())
h3cDot11CfgSTVLANID.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cDot11CfgSTVLANID.setStatus(_A)
class _H3cDot11CfgSTNASPortID_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,127))
_H3cDot11CfgSTNASPortID_Type.__name__=_H
_H3cDot11CfgSTNASPortID_Object=MibTableColumn
h3cDot11CfgSTNASPortID=_H3cDot11CfgSTNASPortID_Object((1,3,6,1,4,1,2011,10,2,75,4,3,11,1,2),_H3cDot11CfgSTNASPortID_Type())
h3cDot11CfgSTNASPortID.setMaxAccess(_I)
if mibBuilder.loadTexts:h3cDot11CfgSTNASPortID.setStatus(_A)
_H3cDot11CfgServiceSetRowStatus_Type=RowStatus
_H3cDot11CfgServiceSetRowStatus_Object=MibTableColumn
h3cDot11CfgServiceSetRowStatus=_H3cDot11CfgServiceSetRowStatus_Object((1,3,6,1,4,1,2011,10,2,75,4,3,11,1,3),_H3cDot11CfgServiceSetRowStatus_Type())
h3cDot11CfgServiceSetRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cDot11CfgServiceSetRowStatus.setStatus(_A)
class _H3cDot11CfgSTNASID_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,127))
_H3cDot11CfgSTNASID_Type.__name__=_H
_H3cDot11CfgSTNASID_Object=MibTableColumn
h3cDot11CfgSTNASID=_H3cDot11CfgSTNASID_Object((1,3,6,1,4,1,2011,10,2,75,4,3,11,1,4),_H3cDot11CfgSTNASID_Type())
h3cDot11CfgSTNASID.setMaxAccess(_I)
if mibBuilder.loadTexts:h3cDot11CfgSTNASID.setStatus(_A)
_H3cDot11RadioIntfConfigGroup_ObjectIdentity=ObjectIdentity
h3cDot11RadioIntfConfigGroup=_H3cDot11RadioIntfConfigGroup_ObjectIdentity((1,3,6,1,4,1,2011,10,2,75,4,4))
_H3cDot11RadioIntfConfigTable_Object=MibTable
h3cDot11RadioIntfConfigTable=_H3cDot11RadioIntfConfigTable_Object((1,3,6,1,4,1,2011,10,2,75,4,4,1))
if mibBuilder.loadTexts:h3cDot11RadioIntfConfigTable.setStatus(_A)
_H3cDot11RadioIntfConfigEntry_Object=MibTableRow
h3cDot11RadioIntfConfigEntry=_H3cDot11RadioIntfConfigEntry_Object((1,3,6,1,4,1,2011,10,2,75,4,4,1,1))
h3cDot11RadioIntfConfigEntry.setIndexNames((0,_E,_p))
if mibBuilder.loadTexts:h3cDot11RadioIntfConfigEntry.setStatus(_A)
_H3cDot11RadioIfIdx_Type=Integer32
_H3cDot11RadioIfIdx_Object=MibTableColumn
h3cDot11RadioIfIdx=_H3cDot11RadioIfIdx_Object((1,3,6,1,4,1,2011,10,2,75,4,4,1,1,1),_H3cDot11RadioIfIdx_Type())
h3cDot11RadioIfIdx.setMaxAccess(_F)
if mibBuilder.loadTexts:h3cDot11RadioIfIdx.setStatus(_A)
class _H3cDot11RadioCfgBeaconIntvl_Type(Integer32):defaultValue=100
_H3cDot11RadioCfgBeaconIntvl_Type.__name__=_C
_H3cDot11RadioCfgBeaconIntvl_Object=MibTableColumn
h3cDot11RadioCfgBeaconIntvl=_H3cDot11RadioCfgBeaconIntvl_Object((1,3,6,1,4,1,2011,10,2,75,4,4,1,1,2),_H3cDot11RadioCfgBeaconIntvl_Type())
h3cDot11RadioCfgBeaconIntvl.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11RadioCfgBeaconIntvl.setStatus(_A)
if mibBuilder.loadTexts:h3cDot11RadioCfgBeaconIntvl.setUnits('TU')
class _H3cDot11RadioCfgDtimIntvl_Type(Integer32):defaultValue=1
_H3cDot11RadioCfgDtimIntvl_Type.__name__=_C
_H3cDot11RadioCfgDtimIntvl_Object=MibTableColumn
h3cDot11RadioCfgDtimIntvl=_H3cDot11RadioCfgDtimIntvl_Object((1,3,6,1,4,1,2011,10,2,75,4,4,1,1,3),_H3cDot11RadioCfgDtimIntvl_Type())
h3cDot11RadioCfgDtimIntvl.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11RadioCfgDtimIntvl.setStatus(_A)
class _H3cDot11RadioCfgRtsThreshold_Type(Integer32):defaultValue=2346
_H3cDot11RadioCfgRtsThreshold_Type.__name__=_C
_H3cDot11RadioCfgRtsThreshold_Object=MibTableColumn
h3cDot11RadioCfgRtsThreshold=_H3cDot11RadioCfgRtsThreshold_Object((1,3,6,1,4,1,2011,10,2,75,4,4,1,1,4),_H3cDot11RadioCfgRtsThreshold_Type())
h3cDot11RadioCfgRtsThreshold.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11RadioCfgRtsThreshold.setStatus(_A)
if mibBuilder.loadTexts:h3cDot11RadioCfgRtsThreshold.setUnits('Byte')
class _H3cDot11RadioCfgFragThreshold_Type(Integer32):defaultValue=2346
_H3cDot11RadioCfgFragThreshold_Type.__name__=_C
_H3cDot11RadioCfgFragThreshold_Object=MibTableColumn
h3cDot11RadioCfgFragThreshold=_H3cDot11RadioCfgFragThreshold_Object((1,3,6,1,4,1,2011,10,2,75,4,4,1,1,5),_H3cDot11RadioCfgFragThreshold_Type())
h3cDot11RadioCfgFragThreshold.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11RadioCfgFragThreshold.setStatus(_A)
if mibBuilder.loadTexts:h3cDot11RadioCfgFragThreshold.setUnits('Byte')
class _H3cDot11RadioCfgShtRetryThld_Type(Integer32):defaultValue=5
_H3cDot11RadioCfgShtRetryThld_Type.__name__=_C
_H3cDot11RadioCfgShtRetryThld_Object=MibTableColumn
h3cDot11RadioCfgShtRetryThld=_H3cDot11RadioCfgShtRetryThld_Object((1,3,6,1,4,1,2011,10,2,75,4,4,1,1,6),_H3cDot11RadioCfgShtRetryThld_Type())
h3cDot11RadioCfgShtRetryThld.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11RadioCfgShtRetryThld.setStatus(_A)
class _H3cDot11RadioCfglongRtrThld_Type(Integer32):defaultValue=5
_H3cDot11RadioCfglongRtrThld_Type.__name__=_C
_H3cDot11RadioCfglongRtrThld_Object=MibTableColumn
h3cDot11RadioCfglongRtrThld=_H3cDot11RadioCfglongRtrThld_Object((1,3,6,1,4,1,2011,10,2,75,4,4,1,1,7),_H3cDot11RadioCfglongRtrThld_Type())
h3cDot11RadioCfglongRtrThld.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11RadioCfglongRtrThld.setStatus(_A)
class _H3cDot11RadioCfgMaxRxLifetime_Type(Unsigned32):defaultValue=2000
_H3cDot11RadioCfgMaxRxLifetime_Type.__name__=_K
_H3cDot11RadioCfgMaxRxLifetime_Object=MibTableColumn
h3cDot11RadioCfgMaxRxLifetime=_H3cDot11RadioCfgMaxRxLifetime_Object((1,3,6,1,4,1,2011,10,2,75,4,4,1,1,8),_H3cDot11RadioCfgMaxRxLifetime_Type())
h3cDot11RadioCfgMaxRxLifetime.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11RadioCfgMaxRxLifetime.setStatus(_A)
if mibBuilder.loadTexts:h3cDot11RadioCfgMaxRxLifetime.setUnits(_A1)
_H3cDot11RadioCfgType_Type=H3cDot11RadioType
_H3cDot11RadioCfgType_Object=MibTableColumn
h3cDot11RadioCfgType=_H3cDot11RadioCfgType_Object((1,3,6,1,4,1,2011,10,2,75,4,4,1,1,9),_H3cDot11RadioCfgType_Type())
h3cDot11RadioCfgType.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11RadioCfgType.setStatus(_A)
class _H3cDot11RadioCfgChannel_Type(H3cDot11ChannelScopeType):defaultValue=1
_H3cDot11RadioCfgChannel_Type.__name__=_w
_H3cDot11RadioCfgChannel_Object=MibTableColumn
h3cDot11RadioCfgChannel=_H3cDot11RadioCfgChannel_Object((1,3,6,1,4,1,2011,10,2,75,4,4,1,1,10),_H3cDot11RadioCfgChannel_Type())
h3cDot11RadioCfgChannel.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11RadioCfgChannel.setStatus(_A)
_H3cDot11RadioCfgMaxTxPwrLvl_Type=H3cDot11TxPwrLevelScopeType
_H3cDot11RadioCfgMaxTxPwrLvl_Object=MibTableColumn
h3cDot11RadioCfgMaxTxPwrLvl=_H3cDot11RadioCfgMaxTxPwrLvl_Object((1,3,6,1,4,1,2011,10,2,75,4,4,1,1,11),_H3cDot11RadioCfgMaxTxPwrLvl_Type())
h3cDot11RadioCfgMaxTxPwrLvl.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11RadioCfgMaxTxPwrLvl.setStatus(_A)
if mibBuilder.loadTexts:h3cDot11RadioCfgMaxTxPwrLvl.setUnits(_R)
class _H3cDot11RadioCfgPreambleLen_Type(H3cDot11PreambleType):defaultValue=2
_H3cDot11RadioCfgPreambleLen_Type.__name__=_V
_H3cDot11RadioCfgPreambleLen_Object=MibTableColumn
h3cDot11RadioCfgPreambleLen=_H3cDot11RadioCfgPreambleLen_Object((1,3,6,1,4,1,2011,10,2,75,4,4,1,1,12),_H3cDot11RadioCfgPreambleLen_Type())
h3cDot11RadioCfgPreambleLen.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11RadioCfgPreambleLen.setStatus(_A)
_H3cDot11RadioCfgWorkMode_Type=H3cDot11WorkMode
_H3cDot11RadioCfgWorkMode_Object=MibTableColumn
h3cDot11RadioCfgWorkMode=_H3cDot11RadioCfgWorkMode_Object((1,3,6,1,4,1,2011,10,2,75,4,4,1,1,13),_H3cDot11RadioCfgWorkMode_Type())
h3cDot11RadioCfgWorkMode.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11RadioCfgWorkMode.setStatus(_A)
class _H3cDot11RadioCfgOnly11gEnable_Type(TruthValue):defaultValue=2
_H3cDot11RadioCfgOnly11gEnable_Type.__name__=_G
_H3cDot11RadioCfgOnly11gEnable_Object=MibTableColumn
h3cDot11RadioCfgOnly11gEnable=_H3cDot11RadioCfgOnly11gEnable_Object((1,3,6,1,4,1,2011,10,2,75,4,4,1,1,14),_H3cDot11RadioCfgOnly11gEnable_Type())
h3cDot11RadioCfgOnly11gEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11RadioCfgOnly11gEnable.setStatus(_A)
_H3cDot11RadioCfgType2_Type=H3cDot11RadioType2
_H3cDot11RadioCfgType2_Object=MibTableColumn
h3cDot11RadioCfgType2=_H3cDot11RadioCfgType2_Object((1,3,6,1,4,1,2011,10,2,75,4,4,1,1,15),_H3cDot11RadioCfgType2_Type())
h3cDot11RadioCfgType2.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11RadioCfgType2.setStatus(_A)
class _H3cDot11RadioCfgRssithresholdCM_Type(Integer32):defaultValue=1
_H3cDot11RadioCfgRssithresholdCM_Type.__name__=_C
_H3cDot11RadioCfgRssithresholdCM_Object=MibTableColumn
h3cDot11RadioCfgRssithresholdCM=_H3cDot11RadioCfgRssithresholdCM_Object((1,3,6,1,4,1,2011,10,2,75,4,4,1,1,16),_H3cDot11RadioCfgRssithresholdCM_Type())
h3cDot11RadioCfgRssithresholdCM.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11RadioCfgRssithresholdCM.setStatus(_A)
if mibBuilder.loadTexts:h3cDot11RadioCfgRssithresholdCM.setUnits('dBm')
_H3cDot11RadioIntfBindTable_Object=MibTable
h3cDot11RadioIntfBindTable=_H3cDot11RadioIntfBindTable_Object((1,3,6,1,4,1,2011,10,2,75,4,4,2))
if mibBuilder.loadTexts:h3cDot11RadioIntfBindTable.setStatus(_A)
_H3cDot11RadioIntfBindEntry_Object=MibTableRow
h3cDot11RadioIntfBindEntry=_H3cDot11RadioIntfBindEntry_Object((1,3,6,1,4,1,2011,10,2,75,4,4,2,1))
h3cDot11RadioIntfBindEntry.setIndexNames((0,_E,_p),(0,_E,_Aa))
if mibBuilder.loadTexts:h3cDot11RadioIntfBindEntry.setStatus(_A)
_H3cDot11RadioIntfBindSvcPlcyID_Type=H3cDot11ServicePolicyIDType
_H3cDot11RadioIntfBindSvcPlcyID_Object=MibTableColumn
h3cDot11RadioIntfBindSvcPlcyID=_H3cDot11RadioIntfBindSvcPlcyID_Object((1,3,6,1,4,1,2011,10,2,75,4,4,2,1,1),_H3cDot11RadioIntfBindSvcPlcyID_Type())
h3cDot11RadioIntfBindSvcPlcyID.setMaxAccess(_F)
if mibBuilder.loadTexts:h3cDot11RadioIntfBindSvcPlcyID.setStatus(_A)
_H3cDot11RadioIntfBindIfIdx_Type=Unsigned32
_H3cDot11RadioIntfBindIfIdx_Object=MibTableColumn
h3cDot11RadioIntfBindIfIdx=_H3cDot11RadioIntfBindIfIdx_Object((1,3,6,1,4,1,2011,10,2,75,4,4,2,1,2),_H3cDot11RadioIntfBindIfIdx_Type())
h3cDot11RadioIntfBindIfIdx.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cDot11RadioIntfBindIfIdx.setStatus(_A)
_H3cDot11RadioIntfBindRowStatus_Type=RowStatus
_H3cDot11RadioIntfBindRowStatus_Object=MibTableColumn
h3cDot11RadioIntfBindRowStatus=_H3cDot11RadioIntfBindRowStatus_Object((1,3,6,1,4,1,2011,10,2,75,4,4,2,1,3),_H3cDot11RadioIntfBindRowStatus_Type())
h3cDot11RadioIntfBindRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cDot11RadioIntfBindRowStatus.setStatus(_A)
_H3cDot11DataRateConfigGroup_ObjectIdentity=ObjectIdentity
h3cDot11DataRateConfigGroup=_H3cDot11DataRateConfigGroup_ObjectIdentity((1,3,6,1,4,1,2011,10,2,75,4,5))
_H3cDot11DataRateConfigTable_Object=MibTable
h3cDot11DataRateConfigTable=_H3cDot11DataRateConfigTable_Object((1,3,6,1,4,1,2011,10,2,75,4,5,1))
if mibBuilder.loadTexts:h3cDot11DataRateConfigTable.setStatus(_A)
_H3cDot11DataRateConfigEntry_Object=MibTableRow
h3cDot11DataRateConfigEntry=_H3cDot11DataRateConfigEntry_Object((1,3,6,1,4,1,2011,10,2,75,4,5,1,1))
h3cDot11DataRateConfigEntry.setIndexNames((0,_E,_Ab))
if mibBuilder.loadTexts:h3cDot11DataRateConfigEntry.setStatus(_A)
_H3cDot11RadioTypeID_Type=H3cDot11RadioType
_H3cDot11RadioTypeID_Object=MibTableColumn
h3cDot11RadioTypeID=_H3cDot11RadioTypeID_Object((1,3,6,1,4,1,2011,10,2,75,4,5,1,1,1),_H3cDot11RadioTypeID_Type())
h3cDot11RadioTypeID.setMaxAccess(_F)
if mibBuilder.loadTexts:h3cDot11RadioTypeID.setStatus(_A)
class _H3cDot11SupportedRateSet_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_H3cDot11SupportedRateSet_Type.__name__=_H
_H3cDot11SupportedRateSet_Object=MibTableColumn
h3cDot11SupportedRateSet=_H3cDot11SupportedRateSet_Object((1,3,6,1,4,1,2011,10,2,75,4,5,1,1,2),_H3cDot11SupportedRateSet_Type())
h3cDot11SupportedRateSet.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11SupportedRateSet.setStatus(_A)
class _H3cDot11MandatoryRateSet_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_H3cDot11MandatoryRateSet_Type.__name__=_H
_H3cDot11MandatoryRateSet_Object=MibTableColumn
h3cDot11MandatoryRateSet=_H3cDot11MandatoryRateSet_Object((1,3,6,1,4,1,2011,10,2,75,4,5,1,1,3),_H3cDot11MandatoryRateSet_Type())
h3cDot11MandatoryRateSet.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11MandatoryRateSet.setStatus(_A)
class _H3cDot11DisabledRateSet_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_H3cDot11DisabledRateSet_Type.__name__=_H
_H3cDot11DisabledRateSet_Object=MibTableColumn
h3cDot11DisabledRateSet=_H3cDot11DisabledRateSet_Object((1,3,6,1,4,1,2011,10,2,75,4,5,1,1,4),_H3cDot11DisabledRateSet_Type())
h3cDot11DisabledRateSet.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11DisabledRateSet.setStatus(_A)
class _H3cDot11SmartRateSet_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_H3cDot11SmartRateSet_Type.__name__=_H
_H3cDot11SmartRateSet_Object=MibTableColumn
h3cDot11SmartRateSet=_H3cDot11SmartRateSet_Object((1,3,6,1,4,1,2011,10,2,75,4,5,1,1,5),_H3cDot11SmartRateSet_Type())
h3cDot11SmartRateSet.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11SmartRateSet.setStatus(_A)
_H3cDot11InterfaceConfigGroup_ObjectIdentity=ObjectIdentity
h3cDot11InterfaceConfigGroup=_H3cDot11InterfaceConfigGroup_ObjectIdentity((1,3,6,1,4,1,2011,10,2,75,4,6))
_H3cDot11WlanEssIfTable_Object=MibTable
h3cDot11WlanEssIfTable=_H3cDot11WlanEssIfTable_Object((1,3,6,1,4,1,2011,10,2,75,4,6,1))
if mibBuilder.loadTexts:h3cDot11WlanEssIfTable.setStatus(_A)
_H3cDot11WlanEssIfEntry_Object=MibTableRow
h3cDot11WlanEssIfEntry=_H3cDot11WlanEssIfEntry_Object((1,3,6,1,4,1,2011,10,2,75,4,6,1,1))
h3cDot11WlanEssIfEntry.setIndexNames((0,_E,_Ac))
if mibBuilder.loadTexts:h3cDot11WlanEssIfEntry.setStatus(_A)
_H3cDot11WlanEssIfNumber_Type=Integer32
_H3cDot11WlanEssIfNumber_Object=MibTableColumn
h3cDot11WlanEssIfNumber=_H3cDot11WlanEssIfNumber_Object((1,3,6,1,4,1,2011,10,2,75,4,6,1,1,1),_H3cDot11WlanEssIfNumber_Type())
h3cDot11WlanEssIfNumber.setMaxAccess(_F)
if mibBuilder.loadTexts:h3cDot11WlanEssIfNumber.setStatus(_A)
_H3cDot11WlanEssIfIndex_Type=Integer32
_H3cDot11WlanEssIfIndex_Object=MibTableColumn
h3cDot11WlanEssIfIndex=_H3cDot11WlanEssIfIndex_Object((1,3,6,1,4,1,2011,10,2,75,4,6,1,1,2),_H3cDot11WlanEssIfIndex_Type())
h3cDot11WlanEssIfIndex.setMaxAccess(_I)
if mibBuilder.loadTexts:h3cDot11WlanEssIfIndex.setStatus(_A)
_H3cDot11WlanEssRowStatus_Type=RowStatus
_H3cDot11WlanEssRowStatus_Object=MibTableColumn
h3cDot11WlanEssRowStatus=_H3cDot11WlanEssRowStatus_Object((1,3,6,1,4,1,2011,10,2,75,4,6,1,1,3),_H3cDot11WlanEssRowStatus_Type())
h3cDot11WlanEssRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cDot11WlanEssRowStatus.setStatus(_A)
_H3cDot11WlanBssIfTable_Object=MibTable
h3cDot11WlanBssIfTable=_H3cDot11WlanBssIfTable_Object((1,3,6,1,4,1,2011,10,2,75,4,6,2))
if mibBuilder.loadTexts:h3cDot11WlanBssIfTable.setStatus(_A)
_H3cDot11WlanBssIfEntry_Object=MibTableRow
h3cDot11WlanBssIfEntry=_H3cDot11WlanBssIfEntry_Object((1,3,6,1,4,1,2011,10,2,75,4,6,2,1))
h3cDot11WlanBssIfEntry.setIndexNames((0,_E,_Ad))
if mibBuilder.loadTexts:h3cDot11WlanBssIfEntry.setStatus(_A)
_H3cDot11WlanBssIfNumber_Type=Integer32
_H3cDot11WlanBssIfNumber_Object=MibTableColumn
h3cDot11WlanBssIfNumber=_H3cDot11WlanBssIfNumber_Object((1,3,6,1,4,1,2011,10,2,75,4,6,2,1,1),_H3cDot11WlanBssIfNumber_Type())
h3cDot11WlanBssIfNumber.setMaxAccess(_F)
if mibBuilder.loadTexts:h3cDot11WlanBssIfNumber.setStatus(_A)
_H3cDot11WlanBssIfIndex_Type=Integer32
_H3cDot11WlanBssIfIndex_Object=MibTableColumn
h3cDot11WlanBssIfIndex=_H3cDot11WlanBssIfIndex_Object((1,3,6,1,4,1,2011,10,2,75,4,6,2,1,2),_H3cDot11WlanBssIfIndex_Type())
h3cDot11WlanBssIfIndex.setMaxAccess(_I)
if mibBuilder.loadTexts:h3cDot11WlanBssIfIndex.setStatus(_A)
_H3cDot11WlanBssRowStatus_Type=RowStatus
_H3cDot11WlanBssRowStatus_Object=MibTableColumn
h3cDot11WlanBssRowStatus=_H3cDot11WlanBssRowStatus_Object((1,3,6,1,4,1,2011,10,2,75,4,6,2,1,3),_H3cDot11WlanBssRowStatus_Type())
h3cDot11WlanBssRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cDot11WlanBssRowStatus.setStatus(_A)
_H3cDot11WLANEthernetIfTable_Object=MibTable
h3cDot11WLANEthernetIfTable=_H3cDot11WLANEthernetIfTable_Object((1,3,6,1,4,1,2011,10,2,75,4,6,3))
if mibBuilder.loadTexts:h3cDot11WLANEthernetIfTable.setStatus(_A)
_H3cDot11WLANEthernetIfEntry_Object=MibTableRow
h3cDot11WLANEthernetIfEntry=_H3cDot11WLANEthernetIfEntry_Object((1,3,6,1,4,1,2011,10,2,75,4,6,3,1))
h3cDot11WLANEthernetIfEntry.setIndexNames((0,_E,_Ae))
if mibBuilder.loadTexts:h3cDot11WLANEthernetIfEntry.setStatus(_A)
_H3cDot11WlanEthernetIfNumber_Type=Integer32
_H3cDot11WlanEthernetIfNumber_Object=MibTableColumn
h3cDot11WlanEthernetIfNumber=_H3cDot11WlanEthernetIfNumber_Object((1,3,6,1,4,1,2011,10,2,75,4,6,3,1,1),_H3cDot11WlanEthernetIfNumber_Type())
h3cDot11WlanEthernetIfNumber.setMaxAccess(_F)
if mibBuilder.loadTexts:h3cDot11WlanEthernetIfNumber.setStatus(_A)
_H3cDot11WLANEthernetIfIndex_Type=Integer32
_H3cDot11WLANEthernetIfIndex_Object=MibTableColumn
h3cDot11WLANEthernetIfIndex=_H3cDot11WLANEthernetIfIndex_Object((1,3,6,1,4,1,2011,10,2,75,4,6,3,1,2),_H3cDot11WLANEthernetIfIndex_Type())
h3cDot11WLANEthernetIfIndex.setMaxAccess(_I)
if mibBuilder.loadTexts:h3cDot11WLANEthernetIfIndex.setStatus(_A)
_H3cDot11WlanEthernetRowStatus_Type=RowStatus
_H3cDot11WlanEthernetRowStatus_Object=MibTableColumn
h3cDot11WlanEthernetRowStatus=_H3cDot11WlanEthernetRowStatus_Object((1,3,6,1,4,1,2011,10,2,75,4,6,3,1,3),_H3cDot11WlanEthernetRowStatus_Type())
h3cDot11WlanEthernetRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cDot11WlanEthernetRowStatus.setStatus(_A)
_H3cDot11PortSecurityTable_Object=MibTable
h3cDot11PortSecurityTable=_H3cDot11PortSecurityTable_Object((1,3,6,1,4,1,2011,10,2,75,4,6,4))
if mibBuilder.loadTexts:h3cDot11PortSecurityTable.setStatus(_A)
_H3cDot11PortSecurityEntry_Object=MibTableRow
h3cDot11PortSecurityEntry=_H3cDot11PortSecurityEntry_Object((1,3,6,1,4,1,2011,10,2,75,4,6,4,1))
h3cDot11PortSecurityEntry.setIndexNames((0,_y,_z))
if mibBuilder.loadTexts:h3cDot11PortSecurityEntry.setStatus(_A)
class _H3cDot11PortSecurityMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*((_A6,1),(_A7,2),(_U,3),(_A8,4),(_A9,5),('ext',6)))
_H3cDot11PortSecurityMode_Type.__name__=_C
_H3cDot11PortSecurityMode_Object=MibTableColumn
h3cDot11PortSecurityMode=_H3cDot11PortSecurityMode_Object((1,3,6,1,4,1,2011,10,2,75,4,6,4,1,1),_H3cDot11PortSecurityMode_Type())
h3cDot11PortSecurityMode.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11PortSecurityMode.setStatus(_A)
class _H3cDot11SecurityUserLoginTxKeyType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_AA,1),(_AB,2),(_AC,3)))
_H3cDot11SecurityUserLoginTxKeyType_Type.__name__=_C
_H3cDot11SecurityUserLoginTxKeyType_Object=MibTableColumn
h3cDot11SecurityUserLoginTxKeyType=_H3cDot11SecurityUserLoginTxKeyType_Object((1,3,6,1,4,1,2011,10,2,75,4,6,4,1,2),_H3cDot11SecurityUserLoginTxKeyType_Type())
h3cDot11SecurityUserLoginTxKeyType.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11SecurityUserLoginTxKeyType.setStatus(_A)
class _H3cDot11SecurityPskKeyMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_k,1),(_l,2),(_m,3)))
_H3cDot11SecurityPskKeyMode_Type.__name__=_C
_H3cDot11SecurityPskKeyMode_Object=MibTableColumn
h3cDot11SecurityPskKeyMode=_H3cDot11SecurityPskKeyMode_Object((1,3,6,1,4,1,2011,10,2,75,4,6,4,1,3),_H3cDot11SecurityPskKeyMode_Type())
h3cDot11SecurityPskKeyMode.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11SecurityPskKeyMode.setStatus(_A)
_H3cDot11SecurityPskKeyString_Type=DisplayString
_H3cDot11SecurityPskKeyString_Object=MibTableColumn
h3cDot11SecurityPskKeyString=_H3cDot11SecurityPskKeyString_Object((1,3,6,1,4,1,2011,10,2,75,4,6,4,1,4),_H3cDot11SecurityPskKeyString_Type())
h3cDot11SecurityPskKeyString.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11SecurityPskKeyString.setStatus(_A)
_H3cDot11WlanMeshIfTable_Object=MibTable
h3cDot11WlanMeshIfTable=_H3cDot11WlanMeshIfTable_Object((1,3,6,1,4,1,2011,10,2,75,4,6,5))
if mibBuilder.loadTexts:h3cDot11WlanMeshIfTable.setStatus(_A)
_H3cDot11WlanMeshIfEntry_Object=MibTableRow
h3cDot11WlanMeshIfEntry=_H3cDot11WlanMeshIfEntry_Object((1,3,6,1,4,1,2011,10,2,75,4,6,5,1))
h3cDot11WlanMeshIfEntry.setIndexNames((0,_E,_Af))
if mibBuilder.loadTexts:h3cDot11WlanMeshIfEntry.setStatus(_A)
_H3cDot11WlanMeshIfNumber_Type=Integer32
_H3cDot11WlanMeshIfNumber_Object=MibTableColumn
h3cDot11WlanMeshIfNumber=_H3cDot11WlanMeshIfNumber_Object((1,3,6,1,4,1,2011,10,2,75,4,6,5,1,1),_H3cDot11WlanMeshIfNumber_Type())
h3cDot11WlanMeshIfNumber.setMaxAccess(_F)
if mibBuilder.loadTexts:h3cDot11WlanMeshIfNumber.setStatus(_A)
_H3cDot11WlanMeshIfIndex_Type=Integer32
_H3cDot11WlanMeshIfIndex_Object=MibTableColumn
h3cDot11WlanMeshIfIndex=_H3cDot11WlanMeshIfIndex_Object((1,3,6,1,4,1,2011,10,2,75,4,6,5,1,2),_H3cDot11WlanMeshIfIndex_Type())
h3cDot11WlanMeshIfIndex.setMaxAccess(_I)
if mibBuilder.loadTexts:h3cDot11WlanMeshIfIndex.setStatus(_A)
_H3cDot11WlanMeshRowStatus_Type=RowStatus
_H3cDot11WlanMeshRowStatus_Object=MibTableColumn
h3cDot11WlanMeshRowStatus=_H3cDot11WlanMeshRowStatus_Object((1,3,6,1,4,1,2011,10,2,75,4,6,5,1,3),_H3cDot11WlanMeshRowStatus_Type())
h3cDot11WlanMeshRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cDot11WlanMeshRowStatus.setStatus(_A)
_H3cDot11ACBackupGroup_ObjectIdentity=ObjectIdentity
h3cDot11ACBackupGroup=_H3cDot11ACBackupGroup_ObjectIdentity((1,3,6,1,4,1,2011,10,2,75,4,7))
_H3cDot11BackupACAdrssIP_Type=InetAddress
_H3cDot11BackupACAdrssIP_Object=MibScalar
h3cDot11BackupACAdrssIP=_H3cDot11BackupACAdrssIP_Object((1,3,6,1,4,1,2011,10,2,75,4,7,1),_H3cDot11BackupACAdrssIP_Type())
h3cDot11BackupACAdrssIP.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11BackupACAdrssIP.setStatus(_A)
_H3cDot11BackupACAdrssIPv6_Type=InetAddress
_H3cDot11BackupACAdrssIPv6_Object=MibScalar
h3cDot11BackupACAdrssIPv6=_H3cDot11BackupACAdrssIPv6_Object((1,3,6,1,4,1,2011,10,2,75,4,7,2),_H3cDot11BackupACAdrssIPv6_Type())
h3cDot11BackupACAdrssIPv6.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11BackupACAdrssIPv6.setStatus(_A)
_H3cDot11RadioElementConfigGroup_ObjectIdentity=ObjectIdentity
h3cDot11RadioElementConfigGroup=_H3cDot11RadioElementConfigGroup_ObjectIdentity((1,3,6,1,4,1,2011,10,2,75,4,8))
_H3cDot11nRadioCfgTable_Object=MibTable
h3cDot11nRadioCfgTable=_H3cDot11nRadioCfgTable_Object((1,3,6,1,4,1,2011,10,2,75,4,8,1))
if mibBuilder.loadTexts:h3cDot11nRadioCfgTable.setStatus(_A)
_H3cDot11nRadioCfgEntry_Object=MibTableRow
h3cDot11nRadioCfgEntry=_H3cDot11nRadioCfgEntry_Object((1,3,6,1,4,1,2011,10,2,75,4,8,1,1))
h3cDot11nRadioCfgEntry.setIndexNames((0,_E,_Ag))
if mibBuilder.loadTexts:h3cDot11nRadioCfgEntry.setStatus(_A)
_H3cDot11nRadioCfgIndex_Type=H3cDot11RadioElementIndex
_H3cDot11nRadioCfgIndex_Object=MibTableColumn
h3cDot11nRadioCfgIndex=_H3cDot11nRadioCfgIndex_Object((1,3,6,1,4,1,2011,10,2,75,4,8,1,1,1),_H3cDot11nRadioCfgIndex_Type())
h3cDot11nRadioCfgIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:h3cDot11nRadioCfgIndex.setStatus(_A)
class _H3cDot11nAMpduEnable_Type(TruthValue):defaultValue=1
_H3cDot11nAMpduEnable_Type.__name__=_G
_H3cDot11nAMpduEnable_Object=MibTableColumn
h3cDot11nAMpduEnable=_H3cDot11nAMpduEnable_Object((1,3,6,1,4,1,2011,10,2,75,4,8,1,1,2),_H3cDot11nAMpduEnable_Type())
h3cDot11nAMpduEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11nAMpduEnable.setStatus(_A)
class _H3cDot11nAMsduEnable_Type(TruthValue):defaultValue=1
_H3cDot11nAMsduEnable_Type.__name__=_G
_H3cDot11nAMsduEnable_Object=MibTableColumn
h3cDot11nAMsduEnable=_H3cDot11nAMsduEnable_Object((1,3,6,1,4,1,2011,10,2,75,4,8,1,1,3),_H3cDot11nAMsduEnable_Type())
h3cDot11nAMsduEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11nAMsduEnable.setStatus(_A)
class _H3cDot11nClientDot11nOnly_Type(TruthValue):defaultValue=2
_H3cDot11nClientDot11nOnly_Type.__name__=_G
_H3cDot11nClientDot11nOnly_Object=MibTableColumn
h3cDot11nClientDot11nOnly=_H3cDot11nClientDot11nOnly_Object((1,3,6,1,4,1,2011,10,2,75,4,8,1,1,4),_H3cDot11nClientDot11nOnly_Type())
h3cDot11nClientDot11nOnly.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11nClientDot11nOnly.setStatus(_A)
class _H3cDot11nChanelBand_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_q,1),(_r,2),(_s,3),(_t,4),(_u,5)))
_H3cDot11nChanelBand_Type.__name__=_C
_H3cDot11nChanelBand_Object=MibTableColumn
h3cDot11nChanelBand=_H3cDot11nChanelBand_Object((1,3,6,1,4,1,2011,10,2,75,4,8,1,1,5),_H3cDot11nChanelBand_Type())
h3cDot11nChanelBand.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11nChanelBand.setStatus(_A)
class _H3cDot11nShortGiEnable_Type(TruthValue):defaultValue=1
_H3cDot11nShortGiEnable_Type.__name__=_G
_H3cDot11nShortGiEnable_Object=MibTableColumn
h3cDot11nShortGiEnable=_H3cDot11nShortGiEnable_Object((1,3,6,1,4,1,2011,10,2,75,4,8,1,1,6),_H3cDot11nShortGiEnable_Type())
h3cDot11nShortGiEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11nShortGiEnable.setStatus(_A)
class _H3cDot11nClientDot11acOnly_Type(TruthValue):defaultValue=2
_H3cDot11nClientDot11acOnly_Type.__name__=_G
_H3cDot11nClientDot11acOnly_Object=MibTableColumn
h3cDot11nClientDot11acOnly=_H3cDot11nClientDot11acOnly_Object((1,3,6,1,4,1,2011,10,2,75,4,8,1,1,7),_H3cDot11nClientDot11acOnly_Type())
h3cDot11nClientDot11acOnly.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11nClientDot11acOnly.setStatus(_A)
class _H3cDot11nSupportMaxMcs_Type(Integer32):defaultValue=76;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,76))
_H3cDot11nSupportMaxMcs_Type.__name__=_C
_H3cDot11nSupportMaxMcs_Object=MibTableColumn
h3cDot11nSupportMaxMcs=_H3cDot11nSupportMaxMcs_Object((1,3,6,1,4,1,2011,10,2,75,4,8,1,1,8),_H3cDot11nSupportMaxMcs_Type())
h3cDot11nSupportMaxMcs.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11nSupportMaxMcs.setStatus(_A)
class _H3cDot11nMandatoryMaxMcs_Type(Integer32):defaultValue=255;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,76),ValueRangeConstraint(255,255))
_H3cDot11nMandatoryMaxMcs_Type.__name__=_C
_H3cDot11nMandatoryMaxMcs_Object=MibTableColumn
h3cDot11nMandatoryMaxMcs=_H3cDot11nMandatoryMaxMcs_Object((1,3,6,1,4,1,2011,10,2,75,4,8,1,1,9),_H3cDot11nMandatoryMaxMcs_Type())
h3cDot11nMandatoryMaxMcs.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11nMandatoryMaxMcs.setStatus(_A)
_H3cDot11RadioWDSTable_Object=MibTable
h3cDot11RadioWDSTable=_H3cDot11RadioWDSTable_Object((1,3,6,1,4,1,2011,10,2,75,4,8,2))
if mibBuilder.loadTexts:h3cDot11RadioWDSTable.setStatus(_A)
_H3cDot11RadioWDSEntry_Object=MibTableRow
h3cDot11RadioWDSEntry=_H3cDot11RadioWDSEntry_Object((1,3,6,1,4,1,2011,10,2,75,4,8,2,1))
h3cDot11RadioWDSEntry.setIndexNames((0,_E,_Ah))
if mibBuilder.loadTexts:h3cDot11RadioWDSEntry.setStatus(_A)
_H3cDot11RadioWDSIndex_Type=H3cDot11RadioElementIndex
_H3cDot11RadioWDSIndex_Object=MibTableColumn
h3cDot11RadioWDSIndex=_H3cDot11RadioWDSIndex_Object((1,3,6,1,4,1,2011,10,2,75,4,8,2,1,1),_H3cDot11RadioWDSIndex_Type())
h3cDot11RadioWDSIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:h3cDot11RadioWDSIndex.setStatus(_A)
class _H3cDot11RadioWDSMode_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('nowds',1),('wds',2)))
_H3cDot11RadioWDSMode_Type.__name__=_C
_H3cDot11RadioWDSMode_Object=MibTableColumn
h3cDot11RadioWDSMode=_H3cDot11RadioWDSMode_Object((1,3,6,1,4,1,2011,10,2,75,4,8,2,1,2),_H3cDot11RadioWDSMode_Type())
h3cDot11RadioWDSMode.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11RadioWDSMode.setStatus(_A)
class _H3cDot11RadioWDSNetWorkID_Type(OctetString):defaultValue=OctetString('');subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_H3cDot11RadioWDSNetWorkID_Type.__name__=_H
_H3cDot11RadioWDSNetWorkID_Object=MibTableColumn
h3cDot11RadioWDSNetWorkID=_H3cDot11RadioWDSNetWorkID_Object((1,3,6,1,4,1,2011,10,2,75,4,8,2,1,3),_H3cDot11RadioWDSNetWorkID_Type())
h3cDot11RadioWDSNetWorkID.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11RadioWDSNetWorkID.setStatus(_A)
class _H3cDot11WDSSecPskKeyMode_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_k,1),(_l,2),(_m,3)))
_H3cDot11WDSSecPskKeyMode_Type.__name__=_C
_H3cDot11WDSSecPskKeyMode_Object=MibTableColumn
h3cDot11WDSSecPskKeyMode=_H3cDot11WDSSecPskKeyMode_Object((1,3,6,1,4,1,2011,10,2,75,4,8,2,1,4),_H3cDot11WDSSecPskKeyMode_Type())
h3cDot11WDSSecPskKeyMode.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11WDSSecPskKeyMode.setStatus(_A)
class _H3cDot11WDSSecPskKeyString_Type(DisplayString):defaultValue=OctetString('')
_H3cDot11WDSSecPskKeyString_Type.__name__=_g
_H3cDot11WDSSecPskKeyString_Object=MibTableColumn
h3cDot11WDSSecPskKeyString=_H3cDot11WDSSecPskKeyString_Object((1,3,6,1,4,1,2011,10,2,75,4,8,2,1,5),_H3cDot11WDSSecPskKeyString_Type())
h3cDot11WDSSecPskKeyString.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11WDSSecPskKeyString.setStatus(_A)
_H3cDot11nRadioCfg2Table_Object=MibTable
h3cDot11nRadioCfg2Table=_H3cDot11nRadioCfg2Table_Object((1,3,6,1,4,1,2011,10,2,75,4,8,3))
if mibBuilder.loadTexts:h3cDot11nRadioCfg2Table.setStatus(_A)
_H3cDot11nRadioCfg2Entry_Object=MibTableRow
h3cDot11nRadioCfg2Entry=_H3cDot11nRadioCfg2Entry_Object((1,3,6,1,4,1,2011,10,2,75,4,8,3,1))
h3cDot11nRadioCfg2Entry.setIndexNames((0,_E,_Ai),(0,_E,_Aj))
if mibBuilder.loadTexts:h3cDot11nRadioCfg2Entry.setStatus(_A)
_H3cDot11nRadioCfg2APIDIndex_Type=H3cDot11ObjectIDType
_H3cDot11nRadioCfg2APIDIndex_Object=MibTableColumn
h3cDot11nRadioCfg2APIDIndex=_H3cDot11nRadioCfg2APIDIndex_Object((1,3,6,1,4,1,2011,10,2,75,4,8,3,1,1),_H3cDot11nRadioCfg2APIDIndex_Type())
h3cDot11nRadioCfg2APIDIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:h3cDot11nRadioCfg2APIDIndex.setStatus(_A)
_H3cDot11nRadioCfg2RadioIDIndex_Type=H3cDot11RadioScopeType
_H3cDot11nRadioCfg2RadioIDIndex_Object=MibTableColumn
h3cDot11nRadioCfg2RadioIDIndex=_H3cDot11nRadioCfg2RadioIDIndex_Object((1,3,6,1,4,1,2011,10,2,75,4,8,3,1,2),_H3cDot11nRadioCfg2RadioIDIndex_Type())
h3cDot11nRadioCfg2RadioIDIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:h3cDot11nRadioCfg2RadioIDIndex.setStatus(_A)
class _H3cDot11nRadioCfg2AMpduEnable_Type(TruthValue):defaultValue=1
_H3cDot11nRadioCfg2AMpduEnable_Type.__name__=_G
_H3cDot11nRadioCfg2AMpduEnable_Object=MibTableColumn
h3cDot11nRadioCfg2AMpduEnable=_H3cDot11nRadioCfg2AMpduEnable_Object((1,3,6,1,4,1,2011,10,2,75,4,8,3,1,3),_H3cDot11nRadioCfg2AMpduEnable_Type())
h3cDot11nRadioCfg2AMpduEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11nRadioCfg2AMpduEnable.setStatus(_A)
class _H3cDot11nRadioCfg2AMsduEnable_Type(TruthValue):defaultValue=1
_H3cDot11nRadioCfg2AMsduEnable_Type.__name__=_G
_H3cDot11nRadioCfg2AMsduEnable_Object=MibTableColumn
h3cDot11nRadioCfg2AMsduEnable=_H3cDot11nRadioCfg2AMsduEnable_Object((1,3,6,1,4,1,2011,10,2,75,4,8,3,1,4),_H3cDot11nRadioCfg2AMsduEnable_Type())
h3cDot11nRadioCfg2AMsduEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11nRadioCfg2AMsduEnable.setStatus(_A)
class _H3cDot11nRadioCfg2ClientDot11nOnly_Type(TruthValue):defaultValue=2
_H3cDot11nRadioCfg2ClientDot11nOnly_Type.__name__=_G
_H3cDot11nRadioCfg2ClientDot11nOnly_Object=MibTableColumn
h3cDot11nRadioCfg2ClientDot11nOnly=_H3cDot11nRadioCfg2ClientDot11nOnly_Object((1,3,6,1,4,1,2011,10,2,75,4,8,3,1,5),_H3cDot11nRadioCfg2ClientDot11nOnly_Type())
h3cDot11nRadioCfg2ClientDot11nOnly.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11nRadioCfg2ClientDot11nOnly.setStatus(_A)
class _H3cDot11nRadioCfg2ChannelBand_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_q,1),(_r,2),(_s,3),(_t,4),(_u,5)))
_H3cDot11nRadioCfg2ChannelBand_Type.__name__=_C
_H3cDot11nRadioCfg2ChannelBand_Object=MibTableColumn
h3cDot11nRadioCfg2ChannelBand=_H3cDot11nRadioCfg2ChannelBand_Object((1,3,6,1,4,1,2011,10,2,75,4,8,3,1,6),_H3cDot11nRadioCfg2ChannelBand_Type())
h3cDot11nRadioCfg2ChannelBand.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11nRadioCfg2ChannelBand.setStatus(_A)
class _H3cDot11nRadioCfg2ShortGiEnable_Type(TruthValue):defaultValue=1
_H3cDot11nRadioCfg2ShortGiEnable_Type.__name__=_G
_H3cDot11nRadioCfg2ShortGiEnable_Object=MibTableColumn
h3cDot11nRadioCfg2ShortGiEnable=_H3cDot11nRadioCfg2ShortGiEnable_Object((1,3,6,1,4,1,2011,10,2,75,4,8,3,1,7),_H3cDot11nRadioCfg2ShortGiEnable_Type())
h3cDot11nRadioCfg2ShortGiEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11nRadioCfg2ShortGiEnable.setStatus(_A)
class _H3cDot11nRadioCfg2AMpduEnableCM_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_S,0),(_T,1)))
_H3cDot11nRadioCfg2AMpduEnableCM_Type.__name__=_C
_H3cDot11nRadioCfg2AMpduEnableCM_Object=MibTableColumn
h3cDot11nRadioCfg2AMpduEnableCM=_H3cDot11nRadioCfg2AMpduEnableCM_Object((1,3,6,1,4,1,2011,10,2,75,4,8,3,1,8),_H3cDot11nRadioCfg2AMpduEnableCM_Type())
h3cDot11nRadioCfg2AMpduEnableCM.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11nRadioCfg2AMpduEnableCM.setStatus(_A)
class _H3cDot11nRadioCfg2ChannelBandCM_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_r,1),(_q,2),(_s,3),(_t,4),(_u,5)))
_H3cDot11nRadioCfg2ChannelBandCM_Type.__name__=_C
_H3cDot11nRadioCfg2ChannelBandCM_Object=MibTableColumn
h3cDot11nRadioCfg2ChannelBandCM=_H3cDot11nRadioCfg2ChannelBandCM_Object((1,3,6,1,4,1,2011,10,2,75,4,8,3,1,9),_H3cDot11nRadioCfg2ChannelBandCM_Type())
h3cDot11nRadioCfg2ChannelBandCM.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11nRadioCfg2ChannelBandCM.setStatus(_A)
class _H3cDot11nRadioCfg2ShortGiEnableCM_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_S,0),(_T,1)))
_H3cDot11nRadioCfg2ShortGiEnableCM_Type.__name__=_C
_H3cDot11nRadioCfg2ShortGiEnableCM_Object=MibTableColumn
h3cDot11nRadioCfg2ShortGiEnableCM=_H3cDot11nRadioCfg2ShortGiEnableCM_Object((1,3,6,1,4,1,2011,10,2,75,4,8,3,1,10),_H3cDot11nRadioCfg2ShortGiEnableCM_Type())
h3cDot11nRadioCfg2ShortGiEnableCM.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11nRadioCfg2ShortGiEnableCM.setStatus(_A)
class _H3cDot11nRadioCfg2ClientDot11acOnly_Type(TruthValue):defaultValue=2
_H3cDot11nRadioCfg2ClientDot11acOnly_Type.__name__=_G
_H3cDot11nRadioCfg2ClientDot11acOnly_Object=MibTableColumn
h3cDot11nRadioCfg2ClientDot11acOnly=_H3cDot11nRadioCfg2ClientDot11acOnly_Object((1,3,6,1,4,1,2011,10,2,75,4,8,3,1,11),_H3cDot11nRadioCfg2ClientDot11acOnly_Type())
h3cDot11nRadioCfg2ClientDot11acOnly.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11nRadioCfg2ClientDot11acOnly.setStatus(_A)
class _H3cDot11nRadioCfg2ClientDot11nOnlyCM_Type(H3cDot11TruthValueCM):defaultValue=0
_H3cDot11nRadioCfg2ClientDot11nOnlyCM_Type.__name__=_W
_H3cDot11nRadioCfg2ClientDot11nOnlyCM_Object=MibTableColumn
h3cDot11nRadioCfg2ClientDot11nOnlyCM=_H3cDot11nRadioCfg2ClientDot11nOnlyCM_Object((1,3,6,1,4,1,2011,10,2,75,4,8,3,1,12),_H3cDot11nRadioCfg2ClientDot11nOnlyCM_Type())
h3cDot11nRadioCfg2ClientDot11nOnlyCM.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11nRadioCfg2ClientDot11nOnlyCM.setStatus(_A)
class _H3cDot11nRadioCfg2SupportMaxMcs_Type(Integer32):defaultValue=76;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,76))
_H3cDot11nRadioCfg2SupportMaxMcs_Type.__name__=_C
_H3cDot11nRadioCfg2SupportMaxMcs_Object=MibTableColumn
h3cDot11nRadioCfg2SupportMaxMcs=_H3cDot11nRadioCfg2SupportMaxMcs_Object((1,3,6,1,4,1,2011,10,2,75,4,8,3,1,13),_H3cDot11nRadioCfg2SupportMaxMcs_Type())
h3cDot11nRadioCfg2SupportMaxMcs.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11nRadioCfg2SupportMaxMcs.setStatus(_A)
class _H3cDot11nRadioCfg2MandatoryMaxMcs_Type(Integer32):defaultValue=255;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,76),ValueRangeConstraint(255,255))
_H3cDot11nRadioCfg2MandatoryMaxMcs_Type.__name__=_C
_H3cDot11nRadioCfg2MandatoryMaxMcs_Object=MibTableColumn
h3cDot11nRadioCfg2MandatoryMaxMcs=_H3cDot11nRadioCfg2MandatoryMaxMcs_Object((1,3,6,1,4,1,2011,10,2,75,4,8,3,1,14),_H3cDot11nRadioCfg2MandatoryMaxMcs_Type())
h3cDot11nRadioCfg2MandatoryMaxMcs.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11nRadioCfg2MandatoryMaxMcs.setStatus(_A)
_H3cDot11CfgNotifyGroup_ObjectIdentity=ObjectIdentity
h3cDot11CfgNotifyGroup=_H3cDot11CfgNotifyGroup_ObjectIdentity((1,3,6,1,4,1,2011,10,2,75,4,9))
_H3cDot11CfgNotifications_ObjectIdentity=ObjectIdentity
h3cDot11CfgNotifications=_H3cDot11CfgNotifications_ObjectIdentity((1,3,6,1,4,1,2011,10,2,75,4,9,0))
_H3cDot11CfgTrapVarObjects_ObjectIdentity=ObjectIdentity
h3cDot11CfgTrapVarObjects=_H3cDot11CfgTrapVarObjects_ObjectIdentity((1,3,6,1,4,1,2011,10,2,75,4,9,1))
class _H3cDot11PreConflictTemplateNum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1024))
_H3cDot11PreConflictTemplateNum_Type.__name__=_C
_H3cDot11PreConflictTemplateNum_Object=MibScalar
h3cDot11PreConflictTemplateNum=_H3cDot11PreConflictTemplateNum_Object((1,3,6,1,4,1,2011,10,2,75,4,9,1,1),_H3cDot11PreConflictTemplateNum_Type())
h3cDot11PreConflictTemplateNum.setMaxAccess(_L)
if mibBuilder.loadTexts:h3cDot11PreConflictTemplateNum.setStatus(_A)
class _H3cDot11CurrConflictTemplateNum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1024))
_H3cDot11CurrConflictTemplateNum_Type.__name__=_C
_H3cDot11CurrConflictTemplateNum_Object=MibScalar
h3cDot11CurrConflictTemplateNum=_H3cDot11CurrConflictTemplateNum_Object((1,3,6,1,4,1,2011,10,2,75,4,9,1,2),_H3cDot11CurrConflictTemplateNum_Type())
h3cDot11CurrConflictTemplateNum.setMaxAccess(_L)
if mibBuilder.loadTexts:h3cDot11CurrConflictTemplateNum.setStatus(_A)
class _H3cDot11ConflictCipherIdx_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4))
_H3cDot11ConflictCipherIdx_Type.__name__=_C
_H3cDot11ConflictCipherIdx_Object=MibScalar
h3cDot11ConflictCipherIdx=_H3cDot11ConflictCipherIdx_Object((1,3,6,1,4,1,2011,10,2,75,4,9,1,3),_H3cDot11ConflictCipherIdx_Type())
h3cDot11ConflictCipherIdx.setMaxAccess(_L)
if mibBuilder.loadTexts:h3cDot11ConflictCipherIdx.setStatus(_A)
_H3cDot11ConfigureAPID_Type=H3cDot11ObjectIDType
_H3cDot11ConfigureAPID_Object=MibScalar
h3cDot11ConfigureAPID=_H3cDot11ConfigureAPID_Object((1,3,6,1,4,1,2011,10,2,75,4,9,1,4),_H3cDot11ConfigureAPID_Type())
h3cDot11ConfigureAPID.setMaxAccess(_L)
if mibBuilder.loadTexts:h3cDot11ConfigureAPID.setStatus(_A)
_H3cDot11ConfigureRadioID_Type=H3cDot11RadioScopeType
_H3cDot11ConfigureRadioID_Object=MibScalar
h3cDot11ConfigureRadioID=_H3cDot11ConfigureRadioID_Object((1,3,6,1,4,1,2011,10,2,75,4,9,1,5),_H3cDot11ConfigureRadioID_Type())
h3cDot11ConfigureRadioID.setMaxAccess(_L)
if mibBuilder.loadTexts:h3cDot11ConfigureRadioID.setStatus(_A)
_H3cDot11ConfigureAPMacAddress_Type=MacAddress
_H3cDot11ConfigureAPMacAddress_Object=MibScalar
h3cDot11ConfigureAPMacAddress=_H3cDot11ConfigureAPMacAddress_Object((1,3,6,1,4,1,2011,10,2,75,4,9,1,6),_H3cDot11ConfigureAPMacAddress_Type())
h3cDot11ConfigureAPMacAddress.setMaxAccess(_L)
if mibBuilder.loadTexts:h3cDot11ConfigureAPMacAddress.setStatus(_A)
_H3cDot11PreConflictTemplateSSID_Type=H3cDot11SSIDStringType
_H3cDot11PreConflictTemplateSSID_Object=MibScalar
h3cDot11PreConflictTemplateSSID=_H3cDot11PreConflictTemplateSSID_Object((1,3,6,1,4,1,2011,10,2,75,4,9,1,7),_H3cDot11PreConflictTemplateSSID_Type())
h3cDot11PreConflictTemplateSSID.setMaxAccess(_L)
if mibBuilder.loadTexts:h3cDot11PreConflictTemplateSSID.setStatus(_A)
_H3cDot11CurrConflictTemplateSSID_Type=H3cDot11SSIDStringType
_H3cDot11CurrConflictTemplateSSID_Object=MibScalar
h3cDot11CurrConflictTemplateSSID=_H3cDot11CurrConflictTemplateSSID_Object((1,3,6,1,4,1,2011,10,2,75,4,9,1,8),_H3cDot11CurrConflictTemplateSSID_Type())
h3cDot11CurrConflictTemplateSSID.setMaxAccess(_L)
if mibBuilder.loadTexts:h3cDot11CurrConflictTemplateSSID.setStatus(_A)
_H3cDot11LocalACConfigGroup_ObjectIdentity=ObjectIdentity
h3cDot11LocalACConfigGroup=_H3cDot11LocalACConfigGroup_ObjectIdentity((1,3,6,1,4,1,2011,10,2,75,4,10))
_H3cDot11LocalACTemplateTable_Object=MibTable
h3cDot11LocalACTemplateTable=_H3cDot11LocalACTemplateTable_Object((1,3,6,1,4,1,2011,10,2,75,4,10,1))
if mibBuilder.loadTexts:h3cDot11LocalACTemplateTable.setStatus(_A)
_H3cDot11LocalACTemplateEntry_Object=MibTableRow
h3cDot11LocalACTemplateEntry=_H3cDot11LocalACTemplateEntry_Object((1,3,6,1,4,1,2011,10,2,75,4,10,1,1))
h3cDot11LocalACTemplateEntry.setIndexNames((0,_E,_Ak))
if mibBuilder.loadTexts:h3cDot11LocalACTemplateEntry.setStatus(_A)
class _H3cDot11LocalACTemplateName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,127))
_H3cDot11LocalACTemplateName_Type.__name__=_H
_H3cDot11LocalACTemplateName_Object=MibTableColumn
h3cDot11LocalACTemplateName=_H3cDot11LocalACTemplateName_Object((1,3,6,1,4,1,2011,10,2,75,4,10,1,1,1),_H3cDot11LocalACTemplateName_Type())
h3cDot11LocalACTemplateName.setMaxAccess(_F)
if mibBuilder.loadTexts:h3cDot11LocalACTemplateName.setStatus(_A)
_H3cDot11LocalACName_Type=OctetString
_H3cDot11LocalACName_Object=MibTableColumn
h3cDot11LocalACName=_H3cDot11LocalACName_Object((1,3,6,1,4,1,2011,10,2,75,4,10,1,1,2),_H3cDot11LocalACName_Type())
h3cDot11LocalACName.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cDot11LocalACName.setStatus(_A)
_H3cDot11LocalACSerialID_Type=OctetString
_H3cDot11LocalACSerialID_Object=MibTableColumn
h3cDot11LocalACSerialID=_H3cDot11LocalACSerialID_Object((1,3,6,1,4,1,2011,10,2,75,4,10,1,1,3),_H3cDot11LocalACSerialID_Type())
h3cDot11LocalACSerialID.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cDot11LocalACSerialID.setStatus(_A)
_H3cDot11TemLocalACModelAlias_Type=OctetString
_H3cDot11TemLocalACModelAlias_Object=MibTableColumn
h3cDot11TemLocalACModelAlias=_H3cDot11TemLocalACModelAlias_Object((1,3,6,1,4,1,2011,10,2,75,4,10,1,1,4),_H3cDot11TemLocalACModelAlias_Type())
h3cDot11TemLocalACModelAlias.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cDot11TemLocalACModelAlias.setStatus(_A)
_H3cDot11LocalACTempRowStatus_Type=RowStatus
_H3cDot11LocalACTempRowStatus_Object=MibTableColumn
h3cDot11LocalACTempRowStatus=_H3cDot11LocalACTempRowStatus_Object((1,3,6,1,4,1,2011,10,2,75,4,10,1,1,5),_H3cDot11LocalACTempRowStatus_Type())
h3cDot11LocalACTempRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cDot11LocalACTempRowStatus.setStatus(_A)
class _H3cDot11LocalACStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*(('join',1),('joinConfirm',2),('download',3),('config',4),('run',5),('idle',6)))
_H3cDot11LocalACStatus_Type.__name__=_C
_H3cDot11LocalACStatus_Object=MibTableColumn
h3cDot11LocalACStatus=_H3cDot11LocalACStatus_Object((1,3,6,1,4,1,2011,10,2,75,4,10,1,1,6),_H3cDot11LocalACStatus_Type())
h3cDot11LocalACStatus.setMaxAccess(_I)
if mibBuilder.loadTexts:h3cDot11LocalACStatus.setStatus(_A)
_H3cDot11LocalACIPAddress_Type=IpAddress
_H3cDot11LocalACIPAddress_Object=MibTableColumn
h3cDot11LocalACIPAddress=_H3cDot11LocalACIPAddress_Object((1,3,6,1,4,1,2011,10,2,75,4,10,1,1,7),_H3cDot11LocalACIPAddress_Type())
h3cDot11LocalACIPAddress.setMaxAccess(_I)
if mibBuilder.loadTexts:h3cDot11LocalACIPAddress.setStatus(_A)
_H3cDot11LocalACIPv6Address_Type=OctetString
_H3cDot11LocalACIPv6Address_Object=MibTableColumn
h3cDot11LocalACIPv6Address=_H3cDot11LocalACIPv6Address_Object((1,3,6,1,4,1,2011,10,2,75,4,10,1,1,8),_H3cDot11LocalACIPv6Address_Type())
h3cDot11LocalACIPv6Address.setMaxAccess(_I)
if mibBuilder.loadTexts:h3cDot11LocalACIPv6Address.setStatus(_A)
class _H3cDot11EchoInterval_Type(Integer32):defaultValue=10;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(5,80))
_H3cDot11EchoInterval_Type.__name__=_C
_H3cDot11EchoInterval_Object=MibTableColumn
h3cDot11EchoInterval=_H3cDot11EchoInterval_Object((1,3,6,1,4,1,2011,10,2,75,4,10,1,1,9),_H3cDot11EchoInterval_Type())
h3cDot11EchoInterval.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cDot11EchoInterval.setStatus(_A)
if mibBuilder.loadTexts:h3cDot11EchoInterval.setUnits(_J)
class _H3cDot11RetransInterval_Type(Integer32):defaultValue=5;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(3,8))
_H3cDot11RetransInterval_Type.__name__=_C
_H3cDot11RetransInterval_Object=MibTableColumn
h3cDot11RetransInterval=_H3cDot11RetransInterval_Object((1,3,6,1,4,1,2011,10,2,75,4,10,1,1,10),_H3cDot11RetransInterval_Type())
h3cDot11RetransInterval.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cDot11RetransInterval.setStatus(_A)
if mibBuilder.loadTexts:h3cDot11RetransInterval.setUnits(_J)
class _H3cDot11RetransCount_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(2,5))
_H3cDot11RetransCount_Type.__name__=_C
_H3cDot11RetransCount_Object=MibTableColumn
h3cDot11RetransCount=_H3cDot11RetransCount_Object((1,3,6,1,4,1,2011,10,2,75,4,10,1,1,11),_H3cDot11RetransCount_Type())
h3cDot11RetransCount.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cDot11RetransCount.setStatus(_A)
if mibBuilder.loadTexts:h3cDot11RetransCount.setUnits(_J)
class _H3cDot11FirmwareUpgrade_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_N,1),(_O,2)))
_H3cDot11FirmwareUpgrade_Type.__name__=_C
_H3cDot11FirmwareUpgrade_Object=MibTableColumn
h3cDot11FirmwareUpgrade=_H3cDot11FirmwareUpgrade_Object((1,3,6,1,4,1,2011,10,2,75,4,10,1,1,12),_H3cDot11FirmwareUpgrade_Type())
h3cDot11FirmwareUpgrade.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cDot11FirmwareUpgrade.setStatus(_A)
h3cDot11CfgCipherChange=NotificationType((1,3,6,1,4,1,2011,10,2,75,4,9,0,1))
h3cDot11CfgCipherChange.setObjects(*((_E,_v),(_E,_Al)))
if mibBuilder.loadTexts:h3cDot11CfgCipherChange.setStatus(_A)
h3cDot11CfgPSKChange=NotificationType((1,3,6,1,4,1,2011,10,2,75,4,9,0,2))
h3cDot11CfgPSKChange.setObjects((_E,_v))
if mibBuilder.loadTexts:h3cDot11CfgPSKChange.setStatus(_A)
h3cDot11SSIDWepIDConflictTrap=NotificationType((1,3,6,1,4,1,2011,10,2,75,4,9,0,3))
h3cDot11SSIDWepIDConflictTrap.setObjects(*((_E,_Am),(_E,_An),(_E,_Ao),(_E,_Ap),(_E,_Aq),(_E,_Ar),(_E,_As),(_E,_At)))
if mibBuilder.loadTexts:h3cDot11SSIDWepIDConflictTrap.setStatus(_A)
mibBuilder.exportSymbols(_E,**{'h3cDot11CFG':h3cDot11CFG,'h3cDot11GlobeConfigGroup':h3cDot11GlobeConfigGroup,'h3cDot11GlobalCountryCode':h3cDot11GlobalCountryCode,'h3cDot11StaKeepALiveTimerIntvl':h3cDot11StaKeepALiveTimerIntvl,'h3cDot11StaIdleTimerIntvl':h3cDot11StaIdleTimerIntvl,'h3cDot11BroadcastProbeReply':h3cDot11BroadcastProbeReply,'h3cDot11APScanMode':h3cDot11APScanMode,'h3cDot11ACCtrlTunnelSecSupport':h3cDot11ACCtrlTunnelSecSupport,'h3cDot11ACDataTunnelSecSupport':h3cDot11ACDataTunnelSecSupport,'h3cDot11ACAutoAPSupport':h3cDot11ACAutoAPSupport,'h3cDot11AutoAPName':h3cDot11AutoAPName,'h3cDot11PersistentName':h3cDot11PersistentName,'h3cDot11IntfTrapThreshold':h3cDot11IntfTrapThreshold,'h3cDot11MonitorInterval':h3cDot11MonitorInterval,'h3cDot11SampleInterval':h3cDot11SampleInterval,'h3cDot11ChnlSwitChkInterval':h3cDot11ChnlSwitChkInterval,'h3cDot11APUserUplimit':h3cDot11APUserUplimit,'h3cDot11APL2IsolateEnable':h3cDot11APL2IsolateEnable,'h3cDot11APBSSIDSupportNum':h3cDot11APBSSIDSupportNum,'h3cDot11APLastUpdateStatTime':h3cDot11APLastUpdateStatTime,'h3cDot11APDoSProtectEnable':h3cDot11APDoSProtectEnable,'h3cDot11MaxAPPerIf':h3cDot11MaxAPPerIf,'h3cDot11SampleTimeStamp':h3cDot11SampleTimeStamp,'h3cDot11UplinkTrackId':h3cDot11UplinkTrackId,'h3cDot11RtCollectSwitch':h3cDot11RtCollectSwitch,'h3cDot11RglCollectIntvl':h3cDot11RglCollectIntvl,'h3cDot11RtCollectIntvl':h3cDot11RtCollectIntvl,'h3cDot11AllAPCpuUsageThreshold':h3cDot11AllAPCpuUsageThreshold,'h3cDot11AllAPMemUsageThreshold':h3cDot11AllAPMemUsageThreshold,'h3cDot11AdjIntfTrapThreshold':h3cDot11AdjIntfTrapThreshold,'h3cDot11AllAPMonitorMode':h3cDot11AllAPMonitorMode,'h3cDot11GlobalApFmwUpdState':h3cDot11GlobalApFmwUpdState,'h3cDot11ACNasIDCM':h3cDot11ACNasIDCM,'h3cDot11ACRole':h3cDot11ACRole,'h3cDot11GlobalLocalACState':h3cDot11GlobalLocalACState,'h3cDot11CentralACIPAddress':h3cDot11CentralACIPAddress,'h3cDot11CentralACIPv6Address':h3cDot11CentralACIPv6Address,'h3cDot11PolicyConfigGroup':h3cDot11PolicyConfigGroup,'h3cDot11RadioPolicyTable':h3cDot11RadioPolicyTable,'h3cDot11RadioPolicyEntry':h3cDot11RadioPolicyEntry,_A0:h3cDot11RadioPolicyName,'h3cDot11BeaconInterval':h3cDot11BeaconInterval,'h3cDot11DtimInterval':h3cDot11DtimInterval,'h3cDot11RtsThreshold':h3cDot11RtsThreshold,'h3cDot11FragThreshold':h3cDot11FragThreshold,'h3cDot11ShortRetryThreshold':h3cDot11ShortRetryThreshold,'h3cDot11LongRetryThreshold':h3cDot11LongRetryThreshold,'h3cDot11MaxRxLifetime':h3cDot11MaxRxLifetime,'h3cDot11RdoPolicyRowStatus':h3cDot11RdoPolicyRowStatus,'h3cDot11RdoClientMaxCount':h3cDot11RdoClientMaxCount,'h3cDot11BeaconIntervalMs':h3cDot11BeaconIntervalMs,'h3cDot11ServicePolicyTable':h3cDot11ServicePolicyTable,'h3cDot11ServicePolicyEntry':h3cDot11ServicePolicyEntry,_i:h3cDot11ServicePolicyID,_v:h3cDot11SSIDName,'h3cDot11SSIDHidden':h3cDot11SSIDHidden,'h3cDot11AuthenMode':h3cDot11AuthenMode,'h3cDot11SSIDEncryptionMode':h3cDot11SSIDEncryptionMode,'h3cDot11WlanInfBindingType':h3cDot11WlanInfBindingType,'h3cDot11WlanInfBindingID':h3cDot11WlanInfBindingID,'h3cDot11SrvPolicyRowStatus':h3cDot11SrvPolicyRowStatus,'h3cDot11ClientMaxCount':h3cDot11ClientMaxCount,'h3cDot11SPInCirMode':h3cDot11SPInCirMode,'h3cDot11SPInCirValue':h3cDot11SPInCirValue,'h3cDot11SPOutCirMode':h3cDot11SPOutCirMode,'h3cDot11SPOutCirValue':h3cDot11SPOutCirValue,'h3cDot11WlanInfPVID':h3cDot11WlanInfPVID,'h3cDot11SPInCirStaticValue':h3cDot11SPInCirStaticValue,'h3cDot11SPOutCirStaticValue':h3cDot11SPOutCirStaticValue,'h3cDot11SPIsolate':h3cDot11SPIsolate,'h3cDot11WlanexAuthServerIP':h3cDot11WlanexAuthServerIP,'h3cDot11SPBeaconMeasEnable':h3cDot11SPBeaconMeasEnable,'h3cDot11SPBeaconMeasType':h3cDot11SPBeaconMeasType,'h3cDot11SPBeaconMeasInterval':h3cDot11SPBeaconMeasInterval,'h3cDot11AuthenModeCM':h3cDot11AuthenModeCM,'h3cDot11SecIEStatusCM':h3cDot11SecIEStatusCM,'h3cDot11SecurityCiphersCM':h3cDot11SecurityCiphersCM,'h3cDot11SrvPolicyStatusCM':h3cDot11SrvPolicyStatusCM,'h3cDot11SSIDHiddenCM':h3cDot11SSIDHiddenCM,'h3cDot11SPIsolateCM':h3cDot11SPIsolateCM,'h3cDot11FwdVlanBitMapLow':h3cDot11FwdVlanBitMapLow,'h3cDot11FwdVlanBitMapHigh':h3cDot11FwdVlanBitMapHigh,'h3cDot11ServicePolicyName':h3cDot11ServicePolicyName,'h3cDot11SecurityModeCM':h3cDot11SecurityModeCM,'h3cDot11SPInCbsValue':h3cDot11SPInCbsValue,'h3cDot11SPOutCbsValue':h3cDot11SPOutCbsValue,'h3cDot11ServicePolicyExtTable':h3cDot11ServicePolicyExtTable,'h3cDot11ServicePolicyExtEntry':h3cDot11ServicePolicyExtEntry,_A2:h3cDot11ServicePolicyExtID,'h3cDot11SecIEStatus':h3cDot11SecIEStatus,_Al:h3cDot11SecurityCiphers,'h3cDot11CipherKeyIndex':h3cDot11CipherKeyIndex,'h3cDot11CipherKey':h3cDot11CipherKey,'h3cDot11SrvPolicyExtRowStatus':h3cDot11SrvPolicyExtRowStatus,'h3cDot11CipherKeyType':h3cDot11CipherKeyType,'h3cDot11AkmMode':h3cDot11AkmMode,'h3cDot11PskKey':h3cDot11PskKey,'h3cDot11RadioPolicyExtTable':h3cDot11RadioPolicyExtTable,'h3cDot11RadioPolicyExtEntry':h3cDot11RadioPolicyExtEntry,_A3:h3cDot11RPAPSerialID,_A4:h3cDot11RPRadioID,'h3cDot11RPBeaconInterval':h3cDot11RPBeaconInterval,'h3cDot11RPDtimInterval':h3cDot11RPDtimInterval,'h3cDot11RPRtsThreshold':h3cDot11RPRtsThreshold,'h3cDot11RPFragThreshold':h3cDot11RPFragThreshold,'h3cDot11RPShortRetryThreshold':h3cDot11RPShortRetryThreshold,'h3cDot11RPLongRetryThreshold':h3cDot11RPLongRetryThreshold,'h3cDot11RPClientMaxCount':h3cDot11RPClientMaxCount,'h3cDot11RPBeaconIntervalCM':h3cDot11RPBeaconIntervalCM,'h3cDot11SrvPortSecurityTable':h3cDot11SrvPortSecurityTable,'h3cDot11SrvPortSecurityEntry':h3cDot11SrvPortSecurityEntry,_A5:h3cDot11SecurityServicePolicyID,'h3cDot11SrvPortSecurityMode':h3cDot11SrvPortSecurityMode,'h3cDot11SrvSecurityKeyType':h3cDot11SrvSecurityKeyType,'h3cDot11SrvSecurityPskKeyMode':h3cDot11SrvSecurityPskKeyMode,'h3cDot11SrvSecurityPskKeyString':h3cDot11SrvSecurityPskKeyString,'h3cDot11SrvPortSecurityModeCM':h3cDot11SrvPortSecurityModeCM,'h3cDot11SrvPolicyExtendTable':h3cDot11SrvPolicyExtendTable,'h3cDot11SrvPolicyExtendEntry':h3cDot11SrvPolicyExtendEntry,'h3cDot11SPEnable':h3cDot11SPEnable,'h3cDot11SrvL2AuthenTable':h3cDot11SrvL2AuthenTable,'h3cDot11SrvL2AuthenEntry':h3cDot11SrvL2AuthenEntry,_AD:h3cDot11SrvL2AuthenID,'h3cDot11L2AuthenMode':h3cDot11L2AuthenMode,'h3cDot11L2IntrusProtectEnable':h3cDot11L2IntrusProtectEnable,'h3cDot11L2IntrusProtectOpt':h3cDot11L2IntrusProtectOpt,'h3cDot11TempServiceStopTimer':h3cDot11TempServiceStopTimer,'h3cDot11TempBlockMACTimer':h3cDot11TempBlockMACTimer,'h3cDot11L2IgnoreAuthorization':h3cDot11L2IgnoreAuthorization,'h3cDot11L2FailVLAN':h3cDot11L2FailVLAN,'h3cDot11L2CriticalVLAN':h3cDot11L2CriticalVLAN,'h3cDot11L2AuthorFailOffline':h3cDot11L2AuthorFailOffline,'h3cDot11L2AccountFailOffline':h3cDot11L2AccountFailOffline,'h3cDot11Dot1xHSEnable':h3cDot11Dot1xHSEnable,'h3cDot11Dot1xSecureHSEnable':h3cDot11Dot1xSecureHSEnable,'h3cDot11Dot1xReauthenEnable':h3cDot11Dot1xReauthenEnable,'h3cDot11Dot1xMandatoryDomain':h3cDot11Dot1xMandatoryDomain,'h3cDot11Dot1xMaxUserCount':h3cDot11Dot1xMaxUserCount,'h3cDot11MACAuthenDomain':h3cDot11MACAuthenDomain,'h3cDot11MACAuthenMaxUserCount':h3cDot11MACAuthenMaxUserCount,'h3cDot11APConfigGroup':h3cDot11APConfigGroup,'h3cDot11APTemplateTable':h3cDot11APTemplateTable,'h3cDot11APTemplateEntry':h3cDot11APTemplateEntry,_AE:h3cDot11APTemplateName,'h3cDot11APSerialID':h3cDot11APSerialID,'h3cDot11TemplateAPModelAlias':h3cDot11TemplateAPModelAlias,'h3cDot11Description':h3cDot11Description,'h3cDot11APWorkMode':h3cDot11APWorkMode,'h3cDot11APTemplateRowStatus':h3cDot11APTemplateRowStatus,'h3cDot11APName':h3cDot11APName,'h3cDot11StatisInterv':h3cDot11StatisInterv,'h3cDot11APBroadcastProbeReply':h3cDot11APBroadcastProbeReply,'h3cDot11StaIdleTimerInterv':h3cDot11StaIdleTimerInterv,'h3cDot11StaKeepAliveTimerInterv':h3cDot11StaKeepAliveTimerInterv,'h3cDot11APCir':h3cDot11APCir,'h3cDot11APCbs':h3cDot11APCbs,'h3cDot11APPriorityLevel':h3cDot11APPriorityLevel,'h3cDot11APElementID':h3cDot11APElementID,'h3cDot11APDevDetectEnable':h3cDot11APDevDetectEnable,'h3cDot11APGetIPMethod':h3cDot11APGetIPMethod,'h3cDot11StatisIntervMode':h3cDot11StatisIntervMode,'h3cDot11ApTrapEnabled':h3cDot11ApTrapEnabled,'h3cDot11ApFmwUpdState':h3cDot11ApFmwUpdState,'h3cDot11StatisIntervModeCM':h3cDot11StatisIntervModeCM,'h3cDot11ApNasIDCM':h3cDot11ApNasIDCM,'h3cDot11ApCoveragetype':h3cDot11ApCoveragetype,'h3cDot11APControlAddressState':h3cDot11APControlAddressState,'h3cDot11APControlAddressIPv4':h3cDot11APControlAddressIPv4,'h3cDot11APControlAddressIPv6':h3cDot11APControlAddressIPv6,'h3cDot11APLocalACName':h3cDot11APLocalACName,'h3cDot11APEchoInterval':h3cDot11APEchoInterval,'h3cDot11RadioToConfigTable':h3cDot11RadioToConfigTable,'h3cDot11RadioToConfigEntry':h3cDot11RadioToConfigEntry,_n:h3cDot11APTemplateNameCfg,_a:h3cDot11CfgRadioID,'h3cDot11CfgRadioPolicyName':h3cDot11CfgRadioPolicyName,'h3cDot11CfgRadioType':h3cDot11CfgRadioType,'h3cDot11CfgChannel':h3cDot11CfgChannel,'h3cDot11CfgMaxTxPowerLevel':h3cDot11CfgMaxTxPowerLevel,'h3cDot11PreambleLen':h3cDot11PreambleLen,'h3cDot11CfgRadioStatus':h3cDot11CfgRadioStatus,'h3cDot11CfgRdElementID':h3cDot11CfgRdElementID,'h3cDot11CfgWorkMode':h3cDot11CfgWorkMode,'h3cDot11CfgPwrAttValue':h3cDot11CfgPwrAttValue,'h3cDot11RadioTxArithmetic':h3cDot11RadioTxArithmetic,'h3cDot11CfgChannelLockStat':h3cDot11CfgChannelLockStat,'h3cDot11CfgPowerLockStat':h3cDot11CfgPowerLockStat,'h3cDot11CfgLBRdGroupId':h3cDot11CfgLBRdGroupId,'h3cDot11CfgRRMSDRdGroupId':h3cDot11CfgRRMSDRdGroupId,'h3cDot11CfgRadioType2':h3cDot11CfgRadioType2,'h3cDot11CfgIDSEnable':h3cDot11CfgIDSEnable,'h3cDot11CfgSaEnable':h3cDot11CfgSaEnable,'h3cDot11CfgSaCltRtFFTData':h3cDot11CfgSaCltRtFFTData,'h3cDot11CfgSaBand':h3cDot11CfgSaBand,'h3cDot11CfgSaRptDevType':h3cDot11CfgSaRptDevType,'h3cDot11CfgSaTrapDevEnable':h3cDot11CfgSaTrapDevEnable,'h3cDot11CfgSaTrapDevType':h3cDot11CfgSaTrapDevType,'h3cDot11CfgSaTrapAQEnable':h3cDot11CfgSaTrapAQEnable,'h3cDot11CfgSaTrapAQThreshold':h3cDot11CfgSaTrapAQThreshold,'h3cDot11CfgSaDrivenRRMEnable':h3cDot11CfgSaDrivenRRMEnable,'h3cDot11CfgSaDrivenRRMSnt':h3cDot11CfgSaDrivenRRMSnt,'h3cDot11APServiceSetTable':h3cDot11APServiceSetTable,'h3cDot11APServiceSetEntry':h3cDot11APServiceSetEntry,_o:h3cDot11CfgServicePolicyID,'h3cDot11SrvSetRowStatus':h3cDot11SrvSetRowStatus,'h3cDot11ServiceSetVlanId':h3cDot11ServiceSetVlanId,'h3cDot11APSysInfoSetTable':h3cDot11APSysInfoSetTable,'h3cDot11APSysInfoSetEntry':h3cDot11APSysInfoSetEntry,'h3cDot11APSysNetID':h3cDot11APSysNetID,'h3cDot11APCpuUsageThreshold':h3cDot11APCpuUsageThreshold,'h3cDot11APMemUsageThreshold':h3cDot11APMemUsageThreshold,'h3cDot11APLimitTable':h3cDot11APLimitTable,'h3cDot11APLimitEntry':h3cDot11APLimitEntry,'h3cDot11APSsidNumLimit':h3cDot11APSsidNumLimit,'h3cDot11APUserCntLimit':h3cDot11APUserCntLimit,'h3cDot11APUserThreshold':h3cDot11APUserThreshold,'h3cDot11APIfSetTable':h3cDot11APIfSetTable,'h3cDot11APIfSetEntry':h3cDot11APIfSetEntry,_AS:h3cDot11APSetIfIndex,'h3cDot11APIfAlias':h3cDot11APIfAlias,'h3cDot11APServiceVlanTable':h3cDot11APServiceVlanTable,'h3cDot11APServiceVlanEntry':h3cDot11APServiceVlanEntry,_AT:h3cDot11APServiceVlanSerialID,_AU:h3cDot11APServiceVlanSPID,'h3cDot11APServiceVlanId':h3cDot11APServiceVlanId,'h3cDot11APServiceVlanRowStatus':h3cDot11APServiceVlanRowStatus,'h3cDot11RadioConfigTable':h3cDot11RadioConfigTable,'h3cDot11RadioConfigEntry':h3cDot11RadioConfigEntry,_AV:h3cDot11RCAPSerialID,_AW:h3cDot11RCRadioID,'h3cDot11RCRadioType':h3cDot11RCRadioType,'h3cDot11RCChannel':h3cDot11RCChannel,'h3cDot11RCPreambleLen':h3cDot11RCPreambleLen,'h3cDot11RCPwrAttValue':h3cDot11RCPwrAttValue,'h3cDot11RCApPowerLevel':h3cDot11RCApPowerLevel,'h3cDot11RCDynamicChlState':h3cDot11RCDynamicChlState,'h3cDot11RCDynamicPowerState':h3cDot11RCDynamicPowerState,'h3cDot11RCRadioStatus':h3cDot11RCRadioStatus,'h3cDot11RCRadioRate':h3cDot11RCRadioRate,'h3cDot11RCPwrAdjustStepLength':h3cDot11RCPwrAdjustStepLength,'h3cDot11RCRadioType2':h3cDot11RCRadioType2,'h3cDot11RCPreambleLenCM':h3cDot11RCPreambleLenCM,'h3cDot11RCDynamicChlStateCM':h3cDot11RCDynamicChlStateCM,'h3cDot11RCRadioStatusCM':h3cDot11RCRadioStatusCM,'h3cDot11RCRadioRateCM':h3cDot11RCRadioRateCM,'h3cDot11RCDynamicPowerStateCM':h3cDot11RCDynamicPowerStateCM,'h3cDot11RCRssiThresholdCM':h3cDot11RCRssiThresholdCM,'h3cDot11RCDynamicChlStateSelfDecisiveCM':h3cDot11RCDynamicChlStateSelfDecisiveCM,'h3cDot11RCDynamicPowerStateSelfDecisiveCM':h3cDot11RCDynamicPowerStateSelfDecisiveCM,'h3cDot11RadioSSIDCfgTable':h3cDot11RadioSSIDCfgTable,'h3cDot11RadioSSIDCfgEntry':h3cDot11RadioSSIDCfgEntry,_AX:h3cDot11RadioSSIDSerialID,_AY:h3cDot11RadioSSIDRadioID,_AZ:h3cDot11RadioSSIDWLANID,'h3cDot11RadioSSIDIndex':h3cDot11RadioSSIDIndex,'h3cDot11RadioBSSID':h3cDot11RadioBSSID,'h3cDot11RadioSSIDRowStatus':h3cDot11RadioSSIDRowStatus,'h3cDot11APSerialIDTable':h3cDot11APSerialIDTable,'h3cDot11APSerialIDEntry':h3cDot11APSerialIDEntry,_b:h3cDot11SIDAPSerialID,'h3cDot11SIDAPWorkMode':h3cDot11SIDAPWorkMode,'h3cDot11SIDAPGetIPMethod':h3cDot11SIDAPGetIPMethod,'h3cDot11SIDAPTemplateName':h3cDot11SIDAPTemplateName,'h3cDot11SIDModelAlias':h3cDot11SIDModelAlias,'h3cDot11SIDAPDescription':h3cDot11SIDAPDescription,'h3cDot11SIDRowStatus':h3cDot11SIDRowStatus,'h3cDot11SIDAPName':h3cDot11SIDAPName,'h3cDot11SIDStatisInterv':h3cDot11SIDStatisInterv,'h3cDot11SIDAPBroadcastProbeReply':h3cDot11SIDAPBroadcastProbeReply,'h3cDot11SIDAPStaIdleTimerInterv':h3cDot11SIDAPStaIdleTimerInterv,'h3cDot11SIDStaKeepAliveTimerInterv':h3cDot11SIDStaKeepAliveTimerInterv,'h3cDot11SIDAPCir':h3cDot11SIDAPCir,'h3cDot11SIDAPCbs':h3cDot11SIDAPCbs,'h3cDot11SIDAPPriorityLevel':h3cDot11SIDAPPriorityLevel,'h3cDot11SIDAPElementID':h3cDot11SIDAPElementID,'h3cDot11SIDAPDevDetectEnable':h3cDot11SIDAPDevDetectEnable,'h3cDot11SIDAPStatisIntervMode':h3cDot11SIDAPStatisIntervMode,'h3cDot11SIDAPWorkModeCM':h3cDot11SIDAPWorkModeCM,'h3cDot11SIDEchoInterval':h3cDot11SIDEchoInterval,'h3cDot11APSTVlanTable':h3cDot11APSTVlanTable,'h3cDot11APSTVlanEntry':h3cDot11APSTVlanEntry,'h3cDot11CfgSTVLANID':h3cDot11CfgSTVLANID,'h3cDot11CfgSTNASPortID':h3cDot11CfgSTNASPortID,'h3cDot11CfgServiceSetRowStatus':h3cDot11CfgServiceSetRowStatus,'h3cDot11CfgSTNASID':h3cDot11CfgSTNASID,'h3cDot11RadioIntfConfigGroup':h3cDot11RadioIntfConfigGroup,'h3cDot11RadioIntfConfigTable':h3cDot11RadioIntfConfigTable,'h3cDot11RadioIntfConfigEntry':h3cDot11RadioIntfConfigEntry,_p:h3cDot11RadioIfIdx,'h3cDot11RadioCfgBeaconIntvl':h3cDot11RadioCfgBeaconIntvl,'h3cDot11RadioCfgDtimIntvl':h3cDot11RadioCfgDtimIntvl,'h3cDot11RadioCfgRtsThreshold':h3cDot11RadioCfgRtsThreshold,'h3cDot11RadioCfgFragThreshold':h3cDot11RadioCfgFragThreshold,'h3cDot11RadioCfgShtRetryThld':h3cDot11RadioCfgShtRetryThld,'h3cDot11RadioCfglongRtrThld':h3cDot11RadioCfglongRtrThld,'h3cDot11RadioCfgMaxRxLifetime':h3cDot11RadioCfgMaxRxLifetime,'h3cDot11RadioCfgType':h3cDot11RadioCfgType,'h3cDot11RadioCfgChannel':h3cDot11RadioCfgChannel,'h3cDot11RadioCfgMaxTxPwrLvl':h3cDot11RadioCfgMaxTxPwrLvl,'h3cDot11RadioCfgPreambleLen':h3cDot11RadioCfgPreambleLen,'h3cDot11RadioCfgWorkMode':h3cDot11RadioCfgWorkMode,'h3cDot11RadioCfgOnly11gEnable':h3cDot11RadioCfgOnly11gEnable,'h3cDot11RadioCfgType2':h3cDot11RadioCfgType2,'h3cDot11RadioCfgRssithresholdCM':h3cDot11RadioCfgRssithresholdCM,'h3cDot11RadioIntfBindTable':h3cDot11RadioIntfBindTable,'h3cDot11RadioIntfBindEntry':h3cDot11RadioIntfBindEntry,_Aa:h3cDot11RadioIntfBindSvcPlcyID,'h3cDot11RadioIntfBindIfIdx':h3cDot11RadioIntfBindIfIdx,'h3cDot11RadioIntfBindRowStatus':h3cDot11RadioIntfBindRowStatus,'h3cDot11DataRateConfigGroup':h3cDot11DataRateConfigGroup,'h3cDot11DataRateConfigTable':h3cDot11DataRateConfigTable,'h3cDot11DataRateConfigEntry':h3cDot11DataRateConfigEntry,_Ab:h3cDot11RadioTypeID,'h3cDot11SupportedRateSet':h3cDot11SupportedRateSet,'h3cDot11MandatoryRateSet':h3cDot11MandatoryRateSet,'h3cDot11DisabledRateSet':h3cDot11DisabledRateSet,'h3cDot11SmartRateSet':h3cDot11SmartRateSet,'h3cDot11InterfaceConfigGroup':h3cDot11InterfaceConfigGroup,'h3cDot11WlanEssIfTable':h3cDot11WlanEssIfTable,'h3cDot11WlanEssIfEntry':h3cDot11WlanEssIfEntry,_Ac:h3cDot11WlanEssIfNumber,'h3cDot11WlanEssIfIndex':h3cDot11WlanEssIfIndex,'h3cDot11WlanEssRowStatus':h3cDot11WlanEssRowStatus,'h3cDot11WlanBssIfTable':h3cDot11WlanBssIfTable,'h3cDot11WlanBssIfEntry':h3cDot11WlanBssIfEntry,_Ad:h3cDot11WlanBssIfNumber,'h3cDot11WlanBssIfIndex':h3cDot11WlanBssIfIndex,'h3cDot11WlanBssRowStatus':h3cDot11WlanBssRowStatus,'h3cDot11WLANEthernetIfTable':h3cDot11WLANEthernetIfTable,'h3cDot11WLANEthernetIfEntry':h3cDot11WLANEthernetIfEntry,_Ae:h3cDot11WlanEthernetIfNumber,'h3cDot11WLANEthernetIfIndex':h3cDot11WLANEthernetIfIndex,'h3cDot11WlanEthernetRowStatus':h3cDot11WlanEthernetRowStatus,'h3cDot11PortSecurityTable':h3cDot11PortSecurityTable,'h3cDot11PortSecurityEntry':h3cDot11PortSecurityEntry,'h3cDot11PortSecurityMode':h3cDot11PortSecurityMode,'h3cDot11SecurityUserLoginTxKeyType':h3cDot11SecurityUserLoginTxKeyType,'h3cDot11SecurityPskKeyMode':h3cDot11SecurityPskKeyMode,'h3cDot11SecurityPskKeyString':h3cDot11SecurityPskKeyString,'h3cDot11WlanMeshIfTable':h3cDot11WlanMeshIfTable,'h3cDot11WlanMeshIfEntry':h3cDot11WlanMeshIfEntry,_Af:h3cDot11WlanMeshIfNumber,'h3cDot11WlanMeshIfIndex':h3cDot11WlanMeshIfIndex,'h3cDot11WlanMeshRowStatus':h3cDot11WlanMeshRowStatus,'h3cDot11ACBackupGroup':h3cDot11ACBackupGroup,'h3cDot11BackupACAdrssIP':h3cDot11BackupACAdrssIP,'h3cDot11BackupACAdrssIPv6':h3cDot11BackupACAdrssIPv6,'h3cDot11RadioElementConfigGroup':h3cDot11RadioElementConfigGroup,'h3cDot11nRadioCfgTable':h3cDot11nRadioCfgTable,'h3cDot11nRadioCfgEntry':h3cDot11nRadioCfgEntry,_Ag:h3cDot11nRadioCfgIndex,'h3cDot11nAMpduEnable':h3cDot11nAMpduEnable,'h3cDot11nAMsduEnable':h3cDot11nAMsduEnable,'h3cDot11nClientDot11nOnly':h3cDot11nClientDot11nOnly,'h3cDot11nChanelBand':h3cDot11nChanelBand,'h3cDot11nShortGiEnable':h3cDot11nShortGiEnable,'h3cDot11nClientDot11acOnly':h3cDot11nClientDot11acOnly,'h3cDot11nSupportMaxMcs':h3cDot11nSupportMaxMcs,'h3cDot11nMandatoryMaxMcs':h3cDot11nMandatoryMaxMcs,'h3cDot11RadioWDSTable':h3cDot11RadioWDSTable,'h3cDot11RadioWDSEntry':h3cDot11RadioWDSEntry,_Ah:h3cDot11RadioWDSIndex,'h3cDot11RadioWDSMode':h3cDot11RadioWDSMode,'h3cDot11RadioWDSNetWorkID':h3cDot11RadioWDSNetWorkID,'h3cDot11WDSSecPskKeyMode':h3cDot11WDSSecPskKeyMode,'h3cDot11WDSSecPskKeyString':h3cDot11WDSSecPskKeyString,'h3cDot11nRadioCfg2Table':h3cDot11nRadioCfg2Table,'h3cDot11nRadioCfg2Entry':h3cDot11nRadioCfg2Entry,_Ai:h3cDot11nRadioCfg2APIDIndex,_Aj:h3cDot11nRadioCfg2RadioIDIndex,'h3cDot11nRadioCfg2AMpduEnable':h3cDot11nRadioCfg2AMpduEnable,'h3cDot11nRadioCfg2AMsduEnable':h3cDot11nRadioCfg2AMsduEnable,'h3cDot11nRadioCfg2ClientDot11nOnly':h3cDot11nRadioCfg2ClientDot11nOnly,'h3cDot11nRadioCfg2ChannelBand':h3cDot11nRadioCfg2ChannelBand,'h3cDot11nRadioCfg2ShortGiEnable':h3cDot11nRadioCfg2ShortGiEnable,'h3cDot11nRadioCfg2AMpduEnableCM':h3cDot11nRadioCfg2AMpduEnableCM,'h3cDot11nRadioCfg2ChannelBandCM':h3cDot11nRadioCfg2ChannelBandCM,'h3cDot11nRadioCfg2ShortGiEnableCM':h3cDot11nRadioCfg2ShortGiEnableCM,'h3cDot11nRadioCfg2ClientDot11acOnly':h3cDot11nRadioCfg2ClientDot11acOnly,'h3cDot11nRadioCfg2ClientDot11nOnlyCM':h3cDot11nRadioCfg2ClientDot11nOnlyCM,'h3cDot11nRadioCfg2SupportMaxMcs':h3cDot11nRadioCfg2SupportMaxMcs,'h3cDot11nRadioCfg2MandatoryMaxMcs':h3cDot11nRadioCfg2MandatoryMaxMcs,'h3cDot11CfgNotifyGroup':h3cDot11CfgNotifyGroup,'h3cDot11CfgNotifications':h3cDot11CfgNotifications,'h3cDot11CfgCipherChange':h3cDot11CfgCipherChange,'h3cDot11CfgPSKChange':h3cDot11CfgPSKChange,'h3cDot11SSIDWepIDConflictTrap':h3cDot11SSIDWepIDConflictTrap,'h3cDot11CfgTrapVarObjects':h3cDot11CfgTrapVarObjects,_Am:h3cDot11PreConflictTemplateNum,_An:h3cDot11CurrConflictTemplateNum,_Ao:h3cDot11ConflictCipherIdx,_Ap:h3cDot11ConfigureAPID,_Aq:h3cDot11ConfigureRadioID,_Ar:h3cDot11ConfigureAPMacAddress,_As:h3cDot11PreConflictTemplateSSID,_At:h3cDot11CurrConflictTemplateSSID,'h3cDot11LocalACConfigGroup':h3cDot11LocalACConfigGroup,'h3cDot11LocalACTemplateTable':h3cDot11LocalACTemplateTable,'h3cDot11LocalACTemplateEntry':h3cDot11LocalACTemplateEntry,_Ak:h3cDot11LocalACTemplateName,'h3cDot11LocalACName':h3cDot11LocalACName,'h3cDot11LocalACSerialID':h3cDot11LocalACSerialID,'h3cDot11TemLocalACModelAlias':h3cDot11TemLocalACModelAlias,'h3cDot11LocalACTempRowStatus':h3cDot11LocalACTempRowStatus,'h3cDot11LocalACStatus':h3cDot11LocalACStatus,'h3cDot11LocalACIPAddress':h3cDot11LocalACIPAddress,'h3cDot11LocalACIPv6Address':h3cDot11LocalACIPv6Address,'h3cDot11EchoInterval':h3cDot11EchoInterval,'h3cDot11RetransInterval':h3cDot11RetransInterval,'h3cDot11RetransCount':h3cDot11RetransCount,'h3cDot11FirmwareUpgrade':h3cDot11FirmwareUpgrade})