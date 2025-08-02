_Ab='hpnicfDot11ConfigureAPMacAddress'
_Aa='hpnicfDot11ConfigureRadioID'
_AZ='hpnicfDot11ConfigureAPID'
_AY='hpnicfDot11ConflictCipherIdx'
_AX='hpnicfDot11CurrConflictTemplateNum'
_AW='hpnicfDot11PreConflictTemplateNum'
_AV='hpnicfDot11SecurityCiphers'
_AU='hpnicfDot11nRadioCfg2RadioIDIndex'
_AT='hpnicfDot11nRadioCfg2APIDIndex'
_AS='hpnicfDot11RadioWDSIndex'
_AR='hpnicfDot11nRadioCfgIndex'
_AQ='hpnicfDot11WlanMeshIfNumber'
_AP='hpnicfDot11WlanEthernetIfNumber'
_AO='hpnicfDot11WlanBssIfNumber'
_AN='hpnicfDot11WlanEssIfNumber'
_AM='hpnicfDot11RadioTypeID'
_AL='hpnicfDot11RadioIntfBindSvcPlcyID'
_AK='hpnicfDot11RadioSSIDWLANID'
_AJ='hpnicfDot11RadioSSIDRadioID'
_AI='hpnicfDot11RadioSSIDSerialID'
_AH='hpnicfDot11RCRadioID'
_AG='hpnicfDot11RCAPSerialID'
_AF='hpnicfDot11APServiceVlanSPID'
_AE='hpnicfDot11APServiceVlanSerialID'
_AD='hpnicfDot11APSetIfIndex'
_AC='dhcpAlloc'
_AB='hpnicfDot11APTemplateName'
_AA='userLoginTxKeyTypeRsaRC4Key'
_A9='userLoginTxKeyTypeDot11Key'
_A8='userLoginTxKeyTypeNone'
_A7='userLoginSecureExtOrPsk'
_A6='macAddressAndPsk'
_A5='userLoginSecureExt'
_A4='noRestrictions'
_A3='hpnicfDot11SecurityServicePolicyID'
_A2='hpnicfDot11RPRadioID'
_A1='hpnicfDot11RPAPSerialID'
_A0='hpnicfDot11ServicePolicyExtID'
_z='millisecond'
_y='hpnicfDot11RadioPolicyName'
_x='minute'
_w='passive'
_v='active'
_u='ifIndex'
_t='IF-MIB'
_s='HpnicfDot11TunnelSecSchemType'
_r='HpnicfDot11ChannelScopeType'
_q='hpnicfDot11SSIDName'
_p='mode40'
_o='mode20'
_n='hpnicfDot11RadioIfIdx'
_m='hpnicfDot11CfgServicePolicyID'
_l='hpnicfDot11APTemplateNameCfg'
_k='pskKeyModeRawKey'
_j='pskKeyModePassPhrase'
_i='pskKeyModeNone'
_h='psk'
_g='none'
_f='hpnicfDot11ServicePolicyID'
_e='disable'
_d='enable'
_c='hybrid'
_b='DisplayString'
_a='hpnicfDot11APElementIndex'
_Z='HpnicfDot11CirMode'
_Y='HPN-ICF-DOT11-REF-MIB'
_X='hpnicfDot11SIDAPSerialID'
_W='hpnicfDot11CfgRadioID'
_V='byte'
_U='monitor'
_T='onepercent'
_S='HpnicfDot11TruthValueCM'
_R='HpnicfDot11PreambleType'
_Q='on'
_P='off'
_O='dbm'
_N='accessible-for-notify'
_M='Kbps'
_L='normal'
_K='Unsigned32'
_J='second'
_I='read-only'
_H='OctetString'
_G='TruthValue'
_F='not-accessible'
_E='HPN-ICF-DOT11-CFG-MIB'
_D='Integer32'
_C='read-create'
_B='read-write'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_H,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
HpnicfDot11AuthenType,HpnicfDot11ChannelScopeType,HpnicfDot11CirMode,HpnicfDot11ObjectIDType,HpnicfDot11PreambleType,HpnicfDot11RadioElementIndex,HpnicfDot11RadioScopeType,HpnicfDot11RadioType,HpnicfDot11RadioType2,HpnicfDot11SSIDEncryptModeType,HpnicfDot11SSIDStringType,HpnicfDot11SecIEStatusType,HpnicfDot11ServicePolicyIDType,HpnicfDot11TruthValueCM,HpnicfDot11TunnelSecSchemType,HpnicfDot11TxPwrLevelScopeType,HpnicfDot11WorkMode,hpnicfDot11,hpnicfDot11APElementIndex=mibBuilder.importSymbols(_Y,'HpnicfDot11AuthenType',_r,_Z,'HpnicfDot11ObjectIDType',_R,'HpnicfDot11RadioElementIndex','HpnicfDot11RadioScopeType','HpnicfDot11RadioType','HpnicfDot11RadioType2','HpnicfDot11SSIDEncryptModeType','HpnicfDot11SSIDStringType','HpnicfDot11SecIEStatusType','HpnicfDot11ServicePolicyIDType',_S,_s,'HpnicfDot11TxPwrLevelScopeType','HpnicfDot11WorkMode','hpnicfDot11',_a)
ifIndex,=mibBuilder.importSymbols(_t,_u)
InetAddress,=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_K,'iso')
DateAndTime,DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime',_b,'MacAddress','PhysAddress','RowStatus','TextualConvention',_G)
hpnicfDot11CFG=ModuleIdentity((1,3,6,1,4,1,11,2,14,11,15,2,75,4))
if mibBuilder.loadTexts:hpnicfDot11CFG.setRevisions(('2010-09-25 18:00','2010-09-02 18:00','2009-07-29 18:00','2009-05-07 20:00','2009-03-20 15:30','2008-11-07 15:30','2008-07-09 18:00','2008-02-25 18:00','2007-12-21 18:00','2007-10-09 16:55','2007-06-19 18:00','2007-04-27 20:00','2007-02-01 20:00','2006-05-10 19:00'))
_HpnicfDot11GlobeConfigGroup_ObjectIdentity=ObjectIdentity
hpnicfDot11GlobeConfigGroup=_HpnicfDot11GlobeConfigGroup_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,75,4,1))
class _HpnicfDot11GlobalCountryCode_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(3,3));fixedLength=3
_HpnicfDot11GlobalCountryCode_Type.__name__=_H
_HpnicfDot11GlobalCountryCode_Object=MibScalar
hpnicfDot11GlobalCountryCode=_HpnicfDot11GlobalCountryCode_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,4,1,1),_HpnicfDot11GlobalCountryCode_Type())
hpnicfDot11GlobalCountryCode.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11GlobalCountryCode.setStatus(_A)
class _HpnicfDot11StaKeepALiveTimerIntvl_Type(Unsigned32):defaultValue=0
_HpnicfDot11StaKeepALiveTimerIntvl_Type.__name__=_K
_HpnicfDot11StaKeepALiveTimerIntvl_Object=MibScalar
hpnicfDot11StaKeepALiveTimerIntvl=_HpnicfDot11StaKeepALiveTimerIntvl_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,4,1,2),_HpnicfDot11StaKeepALiveTimerIntvl_Type())
hpnicfDot11StaKeepALiveTimerIntvl.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11StaKeepALiveTimerIntvl.setStatus(_A)
if mibBuilder.loadTexts:hpnicfDot11StaKeepALiveTimerIntvl.setUnits(_J)
_HpnicfDot11StaIdleTimerIntvl_Type=Integer32
_HpnicfDot11StaIdleTimerIntvl_Object=MibScalar
hpnicfDot11StaIdleTimerIntvl=_HpnicfDot11StaIdleTimerIntvl_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,4,1,3),_HpnicfDot11StaIdleTimerIntvl_Type())
hpnicfDot11StaIdleTimerIntvl.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11StaIdleTimerIntvl.setStatus(_A)
if mibBuilder.loadTexts:hpnicfDot11StaIdleTimerIntvl.setUnits(_J)
class _HpnicfDot11BroadcastProbeReply_Type(TruthValue):defaultValue=1
_HpnicfDot11BroadcastProbeReply_Type.__name__=_G
_HpnicfDot11BroadcastProbeReply_Object=MibScalar
hpnicfDot11BroadcastProbeReply=_HpnicfDot11BroadcastProbeReply_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,4,1,4),_HpnicfDot11BroadcastProbeReply_Type())
hpnicfDot11BroadcastProbeReply.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11BroadcastProbeReply.setStatus(_A)
class _HpnicfDot11APScanMode_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_v,1),(_w,2)))
_HpnicfDot11APScanMode_Type.__name__=_D
_HpnicfDot11APScanMode_Object=MibScalar
hpnicfDot11APScanMode=_HpnicfDot11APScanMode_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,4,1,5),_HpnicfDot11APScanMode_Type())
hpnicfDot11APScanMode.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11APScanMode.setStatus(_A)
_HpnicfDot11ACCtrlTunnelSecSupport_Type=HpnicfDot11TunnelSecSchemType
_HpnicfDot11ACCtrlTunnelSecSupport_Object=MibScalar
hpnicfDot11ACCtrlTunnelSecSupport=_HpnicfDot11ACCtrlTunnelSecSupport_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,4,1,6),_HpnicfDot11ACCtrlTunnelSecSupport_Type())
hpnicfDot11ACCtrlTunnelSecSupport.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11ACCtrlTunnelSecSupport.setStatus(_A)
class _HpnicfDot11ACDataTunnelSecSupport_Type(HpnicfDot11TunnelSecSchemType):defaultValue=1
_HpnicfDot11ACDataTunnelSecSupport_Type.__name__=_s
_HpnicfDot11ACDataTunnelSecSupport_Object=MibScalar
hpnicfDot11ACDataTunnelSecSupport=_HpnicfDot11ACDataTunnelSecSupport_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,4,1,7),_HpnicfDot11ACDataTunnelSecSupport_Type())
hpnicfDot11ACDataTunnelSecSupport.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11ACDataTunnelSecSupport.setStatus(_A)
class _HpnicfDot11ACAutoAPSupport_Type(TruthValue):defaultValue=2
_HpnicfDot11ACAutoAPSupport_Type.__name__=_G
_HpnicfDot11ACAutoAPSupport_Object=MibScalar
hpnicfDot11ACAutoAPSupport=_HpnicfDot11ACAutoAPSupport_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,4,1,8),_HpnicfDot11ACAutoAPSupport_Type())
hpnicfDot11ACAutoAPSupport.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11ACAutoAPSupport.setStatus(_A)
class _HpnicfDot11AutoAPName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,127))
_HpnicfDot11AutoAPName_Type.__name__=_H
_HpnicfDot11AutoAPName_Object=MibScalar
hpnicfDot11AutoAPName=_HpnicfDot11AutoAPName_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,4,1,9),_HpnicfDot11AutoAPName_Type())
hpnicfDot11AutoAPName.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11AutoAPName.setStatus(_A)
class _HpnicfDot11PersistentName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,127))
_HpnicfDot11PersistentName_Type.__name__=_H
_HpnicfDot11PersistentName_Object=MibScalar
hpnicfDot11PersistentName=_HpnicfDot11PersistentName_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,4,1,10),_HpnicfDot11PersistentName_Type())
hpnicfDot11PersistentName.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11PersistentName.setStatus(_A)
_HpnicfDot11IntfTrapThreshold_Type=Integer32
_HpnicfDot11IntfTrapThreshold_Object=MibScalar
hpnicfDot11IntfTrapThreshold=_HpnicfDot11IntfTrapThreshold_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,4,1,11),_HpnicfDot11IntfTrapThreshold_Type())
hpnicfDot11IntfTrapThreshold.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11IntfTrapThreshold.setStatus(_A)
if mibBuilder.loadTexts:hpnicfDot11IntfTrapThreshold.setUnits(_O)
class _HpnicfDot11MonitorInterval_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(5,15))
_HpnicfDot11MonitorInterval_Type.__name__=_K
_HpnicfDot11MonitorInterval_Object=MibScalar
hpnicfDot11MonitorInterval=_HpnicfDot11MonitorInterval_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,4,1,12),_HpnicfDot11MonitorInterval_Type())
hpnicfDot11MonitorInterval.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11MonitorInterval.setStatus(_A)
if mibBuilder.loadTexts:hpnicfDot11MonitorInterval.setUnits(_x)
class _HpnicfDot11SampleInterval_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(10,300))
_HpnicfDot11SampleInterval_Type.__name__=_K
_HpnicfDot11SampleInterval_Object=MibScalar
hpnicfDot11SampleInterval=_HpnicfDot11SampleInterval_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,4,1,13),_HpnicfDot11SampleInterval_Type())
hpnicfDot11SampleInterval.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11SampleInterval.setStatus(_A)
if mibBuilder.loadTexts:hpnicfDot11SampleInterval.setUnits(_J)
class _HpnicfDot11ChnlSwitChkInterval_Type(Unsigned32):defaultValue=8;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(8,180))
_HpnicfDot11ChnlSwitChkInterval_Type.__name__=_K
_HpnicfDot11ChnlSwitChkInterval_Object=MibScalar
hpnicfDot11ChnlSwitChkInterval=_HpnicfDot11ChnlSwitChkInterval_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,4,1,14),_HpnicfDot11ChnlSwitChkInterval_Type())
hpnicfDot11ChnlSwitChkInterval.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11ChnlSwitChkInterval.setStatus(_A)
if mibBuilder.loadTexts:hpnicfDot11ChnlSwitChkInterval.setUnits(_x)
class _HpnicfDot11APUserUplimit_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_HpnicfDot11APUserUplimit_Type.__name__=_K
_HpnicfDot11APUserUplimit_Object=MibScalar
hpnicfDot11APUserUplimit=_HpnicfDot11APUserUplimit_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,4,1,15),_HpnicfDot11APUserUplimit_Type())
hpnicfDot11APUserUplimit.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11APUserUplimit.setStatus(_A)
class _HpnicfDot11APL2IsolateEnable_Type(TruthValue):defaultValue=2
_HpnicfDot11APL2IsolateEnable_Type.__name__=_G
_HpnicfDot11APL2IsolateEnable_Object=MibScalar
hpnicfDot11APL2IsolateEnable=_HpnicfDot11APL2IsolateEnable_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,4,1,16),_HpnicfDot11APL2IsolateEnable_Type())
hpnicfDot11APL2IsolateEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11APL2IsolateEnable.setStatus(_A)
_HpnicfDot11APBSSIDSupportNum_Type=Integer32
_HpnicfDot11APBSSIDSupportNum_Object=MibScalar
hpnicfDot11APBSSIDSupportNum=_HpnicfDot11APBSSIDSupportNum_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,4,1,17),_HpnicfDot11APBSSIDSupportNum_Type())
hpnicfDot11APBSSIDSupportNum.setMaxAccess(_I)
if mibBuilder.loadTexts:hpnicfDot11APBSSIDSupportNum.setStatus(_A)
_HpnicfDot11APLastUpdateStatTime_Type=DateAndTime
_HpnicfDot11APLastUpdateStatTime_Object=MibScalar
hpnicfDot11APLastUpdateStatTime=_HpnicfDot11APLastUpdateStatTime_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,4,1,18),_HpnicfDot11APLastUpdateStatTime_Type())
hpnicfDot11APLastUpdateStatTime.setMaxAccess(_I)
if mibBuilder.loadTexts:hpnicfDot11APLastUpdateStatTime.setStatus(_A)
class _HpnicfDot11APDoSProtectEnable_Type(TruthValue):defaultValue=2
_HpnicfDot11APDoSProtectEnable_Type.__name__=_G
_HpnicfDot11APDoSProtectEnable_Object=MibScalar
hpnicfDot11APDoSProtectEnable=_HpnicfDot11APDoSProtectEnable_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,4,1,19),_HpnicfDot11APDoSProtectEnable_Type())
hpnicfDot11APDoSProtectEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11APDoSProtectEnable.setStatus(_A)
class _HpnicfDot11MaxAPPerIf_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_HpnicfDot11MaxAPPerIf_Type.__name__=_K
_HpnicfDot11MaxAPPerIf_Object=MibScalar
hpnicfDot11MaxAPPerIf=_HpnicfDot11MaxAPPerIf_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,4,1,20),_HpnicfDot11MaxAPPerIf_Type())
hpnicfDot11MaxAPPerIf.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11MaxAPPerIf.setStatus(_A)
_HpnicfDot11SampleTimeStamp_Type=DateAndTime
_HpnicfDot11SampleTimeStamp_Object=MibScalar
hpnicfDot11SampleTimeStamp=_HpnicfDot11SampleTimeStamp_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,4,1,21),_HpnicfDot11SampleTimeStamp_Type())
hpnicfDot11SampleTimeStamp.setMaxAccess(_I)
if mibBuilder.loadTexts:hpnicfDot11SampleTimeStamp.setStatus(_A)
class _HpnicfDot11UplinkTrackId_Type(Unsigned32):defaultValue=0
_HpnicfDot11UplinkTrackId_Type.__name__=_K
_HpnicfDot11UplinkTrackId_Object=MibScalar
hpnicfDot11UplinkTrackId=_HpnicfDot11UplinkTrackId_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,4,1,22),_HpnicfDot11UplinkTrackId_Type())
hpnicfDot11UplinkTrackId.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11UplinkTrackId.setStatus(_A)
class _HpnicfDot11RtCollectSwitch_Type(TruthValue):defaultValue=2
_HpnicfDot11RtCollectSwitch_Type.__name__=_G
_HpnicfDot11RtCollectSwitch_Object=MibScalar
hpnicfDot11RtCollectSwitch=_HpnicfDot11RtCollectSwitch_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,4,1,23),_HpnicfDot11RtCollectSwitch_Type())
hpnicfDot11RtCollectSwitch.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11RtCollectSwitch.setStatus(_A)
_HpnicfDot11RglCollectIntvl_Type=Integer32
_HpnicfDot11RglCollectIntvl_Object=MibScalar
hpnicfDot11RglCollectIntvl=_HpnicfDot11RglCollectIntvl_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,4,1,24),_HpnicfDot11RglCollectIntvl_Type())
hpnicfDot11RglCollectIntvl.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11RglCollectIntvl.setStatus(_A)
if mibBuilder.loadTexts:hpnicfDot11RglCollectIntvl.setUnits(_J)
_HpnicfDot11RtCollectIntvl_Type=Integer32
_HpnicfDot11RtCollectIntvl_Object=MibScalar
hpnicfDot11RtCollectIntvl=_HpnicfDot11RtCollectIntvl_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,4,1,25),_HpnicfDot11RtCollectIntvl_Type())
hpnicfDot11RtCollectIntvl.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11RtCollectIntvl.setStatus(_A)
if mibBuilder.loadTexts:hpnicfDot11RtCollectIntvl.setUnits(_J)
class _HpnicfDot11AllAPCpuUsageThreshold_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_HpnicfDot11AllAPCpuUsageThreshold_Type.__name__=_D
_HpnicfDot11AllAPCpuUsageThreshold_Object=MibScalar
hpnicfDot11AllAPCpuUsageThreshold=_HpnicfDot11AllAPCpuUsageThreshold_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,4,1,26),_HpnicfDot11AllAPCpuUsageThreshold_Type())
hpnicfDot11AllAPCpuUsageThreshold.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11AllAPCpuUsageThreshold.setStatus(_A)
if mibBuilder.loadTexts:hpnicfDot11AllAPCpuUsageThreshold.setUnits(_T)
class _HpnicfDot11AllAPMemUsageThreshold_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_HpnicfDot11AllAPMemUsageThreshold_Type.__name__=_D
_HpnicfDot11AllAPMemUsageThreshold_Object=MibScalar
hpnicfDot11AllAPMemUsageThreshold=_HpnicfDot11AllAPMemUsageThreshold_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,4,1,27),_HpnicfDot11AllAPMemUsageThreshold_Type())
hpnicfDot11AllAPMemUsageThreshold.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11AllAPMemUsageThreshold.setStatus(_A)
if mibBuilder.loadTexts:hpnicfDot11AllAPMemUsageThreshold.setUnits(_T)
_HpnicfDot11AdjIntfTrapThreshold_Type=Integer32
_HpnicfDot11AdjIntfTrapThreshold_Object=MibScalar
hpnicfDot11AdjIntfTrapThreshold=_HpnicfDot11AdjIntfTrapThreshold_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,4,1,28),_HpnicfDot11AdjIntfTrapThreshold_Type())
hpnicfDot11AdjIntfTrapThreshold.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11AdjIntfTrapThreshold.setStatus(_A)
if mibBuilder.loadTexts:hpnicfDot11AdjIntfTrapThreshold.setUnits(_O)
class _HpnicfDot11AllAPMonitorMode_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_L,1),(_U,2),(_c,3)))
_HpnicfDot11AllAPMonitorMode_Type.__name__=_D
_HpnicfDot11AllAPMonitorMode_Object=MibScalar
hpnicfDot11AllAPMonitorMode=_HpnicfDot11AllAPMonitorMode_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,4,1,29),_HpnicfDot11AllAPMonitorMode_Type())
hpnicfDot11AllAPMonitorMode.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11AllAPMonitorMode.setStatus(_A)
class _HpnicfDot11GlobalApFmwUpdState_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_d,1),(_e,2)))
_HpnicfDot11GlobalApFmwUpdState_Type.__name__=_D
_HpnicfDot11GlobalApFmwUpdState_Object=MibScalar
hpnicfDot11GlobalApFmwUpdState=_HpnicfDot11GlobalApFmwUpdState_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,4,1,30),_HpnicfDot11GlobalApFmwUpdState_Type())
hpnicfDot11GlobalApFmwUpdState.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11GlobalApFmwUpdState.setStatus(_A)
_HpnicfDot11ACNasIDCM_Type=OctetString
_HpnicfDot11ACNasIDCM_Object=MibScalar
hpnicfDot11ACNasIDCM=_HpnicfDot11ACNasIDCM_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,4,1,31),_HpnicfDot11ACNasIDCM_Type())
hpnicfDot11ACNasIDCM.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11ACNasIDCM.setStatus(_A)
_HpnicfDot11PolicyConfigGroup_ObjectIdentity=ObjectIdentity
hpnicfDot11PolicyConfigGroup=_HpnicfDot11PolicyConfigGroup_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,75,4,2))
_HpnicfDot11RadioPolicyTable_Object=MibTable
hpnicfDot11RadioPolicyTable=_HpnicfDot11RadioPolicyTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,4,2,1))
if mibBuilder.loadTexts:hpnicfDot11RadioPolicyTable.setStatus(_A)
_HpnicfDot11RadioPolicyEntry_Object=MibTableRow
hpnicfDot11RadioPolicyEntry=_HpnicfDot11RadioPolicyEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,4,2,1,1))
hpnicfDot11RadioPolicyEntry.setIndexNames((1,_E,_y))
if mibBuilder.loadTexts:hpnicfDot11RadioPolicyEntry.setStatus(_A)
class _HpnicfDot11RadioPolicyName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,127))
_HpnicfDot11RadioPolicyName_Type.__name__=_H
_HpnicfDot11RadioPolicyName_Object=MibTableColumn
hpnicfDot11RadioPolicyName=_HpnicfDot11RadioPolicyName_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,4,2,1,1,1),_HpnicfDot11RadioPolicyName_Type())
hpnicfDot11RadioPolicyName.setMaxAccess(_F)
if mibBuilder.loadTexts:hpnicfDot11RadioPolicyName.setStatus(_A)
class _HpnicfDot11BeaconInterval_Type(Integer32):defaultValue=100
_HpnicfDot11BeaconInterval_Type.__name__=_D
_HpnicfDot11BeaconInterval_Object=MibTableColumn
hpnicfDot11BeaconInterval=_HpnicfDot11BeaconInterval_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,4,2,1,1,2),_HpnicfDot11BeaconInterval_Type())
hpnicfDot11BeaconInterval.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfDot11BeaconInterval.setStatus(_A)
if mibBuilder.loadTexts:hpnicfDot11BeaconInterval.setUnits('TU')
class _HpnicfDot11DtimInterval_Type(Integer32):defaultValue=1
_HpnicfDot11DtimInterval_Type.__name__=_D
_HpnicfDot11DtimInterval_Object=MibTableColumn
hpnicfDot11DtimInterval=_HpnicfDot11DtimInterval_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,4,2,1,1,3),_HpnicfDot11DtimInterval_Type())
hpnicfDot11DtimInterval.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfDot11DtimInterval.setStatus(_A)
class _HpnicfDot11RtsThreshold_Type(Integer32):defaultValue=2346
_HpnicfDot11RtsThreshold_Type.__name__=_D
_HpnicfDot11RtsThreshold_Object=MibTableColumn
hpnicfDot11RtsThreshold=_HpnicfDot11RtsThreshold_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,4,2,1,1,4),_HpnicfDot11RtsThreshold_Type())
hpnicfDot11RtsThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfDot11RtsThreshold.setStatus(_A)
if mibBuilder.loadTexts:hpnicfDot11RtsThreshold.setUnits(_V)
class _HpnicfDot11FragThreshold_Type(Integer32):defaultValue=2346
_HpnicfDot11FragThreshold_Type.__name__=_D
_HpnicfDot11FragThreshold_Object=MibTableColumn
hpnicfDot11FragThreshold=_HpnicfDot11FragThreshold_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,4,2,1,1,5),_HpnicfDot11FragThreshold_Type())
hpnicfDot11FragThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfDot11FragThreshold.setStatus(_A)
if mibBuilder.loadTexts:hpnicfDot11FragThreshold.setUnits(_V)
class _HpnicfDot11ShortRetryThreshold_Type(Integer32):defaultValue=7
_HpnicfDot11ShortRetryThreshold_Type.__name__=_D
_HpnicfDot11ShortRetryThreshold_Object=MibTableColumn
hpnicfDot11ShortRetryThreshold=_HpnicfDot11ShortRetryThreshold_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,4,2,1,1,6),_HpnicfDot11ShortRetryThreshold_Type())
hpnicfDot11ShortRetryThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfDot11ShortRetryThreshold.setStatus(_A)
class _HpnicfDot11LongRetryThreshold_Type(Integer32):defaultValue=4
_HpnicfDot11LongRetryThreshold_Type.__name__=_D
_HpnicfDot11LongRetryThreshold_Object=MibTableColumn
hpnicfDot11LongRetryThreshold=_HpnicfDot11LongRetryThreshold_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,4,2,1,1,7),_HpnicfDot11LongRetryThreshold_Type())
hpnicfDot11LongRetryThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfDot11LongRetryThreshold.setStatus(_A)
class _HpnicfDot11MaxRxLifetime_Type(Unsigned32):defaultValue=2000
_HpnicfDot11MaxRxLifetime_Type.__name__=_K
_HpnicfDot11MaxRxLifetime_Object=MibTableColumn
hpnicfDot11MaxRxLifetime=_HpnicfDot11MaxRxLifetime_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,4,2,1,1,8),_HpnicfDot11MaxRxLifetime_Type())
hpnicfDot11MaxRxLifetime.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfDot11MaxRxLifetime.setStatus(_A)
if mibBuilder.loadTexts:hpnicfDot11MaxRxLifetime.setUnits(_z)
_HpnicfDot11RdoPolicyRowStatus_Type=RowStatus
_HpnicfDot11RdoPolicyRowStatus_Object=MibTableColumn
hpnicfDot11RdoPolicyRowStatus=_HpnicfDot11RdoPolicyRowStatus_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,4,2,1,1,9),_HpnicfDot11RdoPolicyRowStatus_Type())
hpnicfDot11RdoPolicyRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfDot11RdoPolicyRowStatus.setStatus(_A)
class _HpnicfDot11RdoClientMaxCount_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_HpnicfDot11RdoClientMaxCount_Type.__name__=_D
_HpnicfDot11RdoClientMaxCount_Object=MibTableColumn
hpnicfDot11RdoClientMaxCount=_HpnicfDot11RdoClientMaxCount_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,4,2,1,1,10),_HpnicfDot11RdoClientMaxCount_Type())
hpnicfDot11RdoClientMaxCount.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfDot11RdoClientMaxCount.setStatus(_A)
_HpnicfDot11BeaconIntervalMs_Type=Integer32
_HpnicfDot11BeaconIntervalMs_Object=MibTableColumn
hpnicfDot11BeaconIntervalMs=_HpnicfDot11BeaconIntervalMs_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,4,2,1,1,11),_HpnicfDot11BeaconIntervalMs_Type())
hpnicfDot11BeaconIntervalMs.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfDot11BeaconIntervalMs.setStatus(_A)
if mibBuilder.loadTexts:hpnicfDot11BeaconIntervalMs.setUnits('ms')
_HpnicfDot11ServicePolicyTable_Object=MibTable
hpnicfDot11ServicePolicyTable=_HpnicfDot11ServicePolicyTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,4,2,2))
if mibBuilder.loadTexts:hpnicfDot11ServicePolicyTable.setStatus(_A)
_HpnicfDot11ServicePolicyEntry_Object=MibTableRow
hpnicfDot11ServicePolicyEntry=_HpnicfDot11ServicePolicyEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,4,2,2,1))
hpnicfDot11ServicePolicyEntry.setIndexNames((0,_E,_f))
if mibBuilder.loadTexts:hpnicfDot11ServicePolicyEntry.setStatus(_A)
_HpnicfDot11ServicePolicyID_Type=HpnicfDot11ServicePolicyIDType
_HpnicfDot11ServicePolicyID_Object=MibTableColumn
hpnicfDot11ServicePolicyID=_HpnicfDot11ServicePolicyID_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,4,2,2,1,1),_HpnicfDot11ServicePolicyID_Type())
hpnicfDot11ServicePolicyID.setMaxAccess(_F)
if mibBuilder.loadTexts:hpnicfDot11ServicePolicyID.setStatus(_A)
_HpnicfDot11SSIDName_Type=HpnicfDot11SSIDStringType
_HpnicfDot11SSIDName_Object=MibTableColumn
hpnicfDot11SSIDName=_HpnicfDot11SSIDName_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,4,2,2,1,2),_HpnicfDot11SSIDName_Type())
hpnicfDot11SSIDName.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfDot11SSIDName.setStatus(_A)
class _HpnicfDot11SSIDHidden_Type(TruthValue):defaultValue=2
_HpnicfDot11SSIDHidden_Type.__name__=_G
_HpnicfDot11SSIDHidden_Object=MibTableColumn
hpnicfDot11SSIDHidden=_HpnicfDot11SSIDHidden_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,4,2,2,1,3),_HpnicfDot11SSIDHidden_Type())
hpnicfDot11SSIDHidden.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfDot11SSIDHidden.setStatus(_A)
_HpnicfDot11AuthenMode_Type=HpnicfDot11AuthenType
_HpnicfDot11AuthenMode_Object=MibTableColumn
hpnicfDot11AuthenMode=_HpnicfDot11AuthenMode_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,4,2,2,1,4),_HpnicfDot11AuthenMode_Type())
hpnicfDot11AuthenMode.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfDot11AuthenMode.setStatus(_A)
_HpnicfDot11SSIDEncryptionMode_Type=HpnicfDot11SSIDEncryptModeType
_HpnicfDot11SSIDEncryptionMode_Object=MibTableColumn
hpnicfDot11SSIDEncryptionMode=_HpnicfDot11SSIDEncryptionMode_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,4,2,2,1,5),_HpnicfDot11SSIDEncryptionMode_Type())
hpnicfDot11SSIDEncryptionMode.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfDot11SSIDEncryptionMode.setStatus(_A)
class _HpnicfDot11WlanInfBindingType_Type(OctetString):defaultValue=OctetString('WLAN-ESS')
_HpnicfDot11WlanInfBindingType_Type.__name__=_H
_HpnicfDot11WlanInfBindingType_Object=MibTableColumn
hpnicfDot11WlanInfBindingType=_HpnicfDot11WlanInfBindingType_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,4,2,2,1,6),_HpnicfDot11WlanInfBindingType_Type())
hpnicfDot11WlanInfBindingType.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfDot11WlanInfBindingType.setStatus(_A)
_HpnicfDot11WlanInfBindingID_Type=Integer32
_HpnicfDot11WlanInfBindingID_Object=MibTableColumn
hpnicfDot11WlanInfBindingID=_HpnicfDot11WlanInfBindingID_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,4,2,2,1,7),_HpnicfDot11WlanInfBindingID_Type())
hpnicfDot11WlanInfBindingID.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfDot11WlanInfBindingID.setStatus(_A)
_HpnicfDot11SrvPolicyRowStatus_Type=RowStatus
_HpnicfDot11SrvPolicyRowStatus_Object=MibTableColumn
hpnicfDot11SrvPolicyRowStatus=_HpnicfDot11SrvPolicyRowStatus_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,4,2,2,1,8),_HpnicfDot11SrvPolicyRowStatus_Type())
hpnicfDot11SrvPolicyRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfDot11SrvPolicyRowStatus.setStatus(_A)
class _HpnicfDot11ClientMaxCount_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_HpnicfDot11ClientMaxCount_Type.__name__=_D
_HpnicfDot11ClientMaxCount_Object=MibTableColumn
hpnicfDot11ClientMaxCount=_HpnicfDot11ClientMaxCount_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,4,2,2,1,9),_HpnicfDot11ClientMaxCount_Type())
hpnicfDot11ClientMaxCount.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfDot11ClientMaxCount.setStatus(_A)
class _HpnicfDot11SPInCirMode_Type(HpnicfDot11CirMode):defaultValue=1
_HpnicfDot11SPInCirMode_Type.__name__=_Z
_HpnicfDot11SPInCirMode_Object=MibTableColumn
hpnicfDot11SPInCirMode=_HpnicfDot11SPInCirMode_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,4,2,2,1,10),_HpnicfDot11SPInCirMode_Type())
hpnicfDot11SPInCirMode.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfDot11SPInCirMode.setStatus(_A)
class _HpnicfDot11SPInCirValue_Type(Integer32):defaultValue=0
_HpnicfDot11SPInCirValue_Type.__name__=_D
_HpnicfDot11SPInCirValue_Object=MibTableColumn
hpnicfDot11SPInCirValue=_HpnicfDot11SPInCirValue_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,4,2,2,1,11),_HpnicfDot11SPInCirValue_Type())
hpnicfDot11SPInCirValue.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfDot11SPInCirValue.setStatus(_A)
if mibBuilder.loadTexts:hpnicfDot11SPInCirValue.setUnits(_M)
class _HpnicfDot11SPOutCirMode_Type(HpnicfDot11CirMode):defaultValue=1
_HpnicfDot11SPOutCirMode_Type.__name__=_Z
_HpnicfDot11SPOutCirMode_Object=MibTableColumn
hpnicfDot11SPOutCirMode=_HpnicfDot11SPOutCirMode_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,4,2,2,1,12),_HpnicfDot11SPOutCirMode_Type())
hpnicfDot11SPOutCirMode.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfDot11SPOutCirMode.setStatus(_A)
class _HpnicfDot11SPOutCirValue_Type(Integer32):defaultValue=0
_HpnicfDot11SPOutCirValue_Type.__name__=_D
_HpnicfDot11SPOutCirValue_Object=MibTableColumn
hpnicfDot11SPOutCirValue=_HpnicfDot11SPOutCirValue_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,4,2,2,1,13),_HpnicfDot11SPOutCirValue_Type())
hpnicfDot11SPOutCirValue.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfDot11SPOutCirValue.setStatus(_A)
if mibBuilder.loadTexts:hpnicfDot11SPOutCirValue.setUnits(_M)
class _HpnicfDot11WlanInfPVID_Type(Integer32):defaultValue=1
_HpnicfDot11WlanInfPVID_Type.__name__=_D
_HpnicfDot11WlanInfPVID_Object=MibTableColumn
hpnicfDot11WlanInfPVID=_HpnicfDot11WlanInfPVID_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,4,2,2,1,14),_HpnicfDot11WlanInfPVID_Type())
hpnicfDot11WlanInfPVID.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfDot11WlanInfPVID.setStatus(_A)
class _HpnicfDot11SPInCirStaticValue_Type(Integer32):defaultValue=0
_HpnicfDot11SPInCirStaticValue_Type.__name__=_D
_HpnicfDot11SPInCirStaticValue_Object=MibTableColumn
hpnicfDot11SPInCirStaticValue=_HpnicfDot11SPInCirStaticValue_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,4,2,2,1,15),_HpnicfDot11SPInCirStaticValue_Type())
hpnicfDot11SPInCirStaticValue.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfDot11SPInCirStaticValue.setStatus(_A)
if mibBuilder.loadTexts:hpnicfDot11SPInCirStaticValue.setUnits(_M)
class _HpnicfDot11SPOutCirStaticValue_Type(Integer32):defaultValue=0
_HpnicfDot11SPOutCirStaticValue_Type.__name__=_D
_HpnicfDot11SPOutCirStaticValue_Object=MibTableColumn
hpnicfDot11SPOutCirStaticValue=_HpnicfDot11SPOutCirStaticValue_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,4,2,2,1,16),_HpnicfDot11SPOutCirStaticValue_Type())
hpnicfDot11SPOutCirStaticValue.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfDot11SPOutCirStaticValue.setStatus(_A)
if mibBuilder.loadTexts:hpnicfDot11SPOutCirStaticValue.setUnits(_M)
class _HpnicfDot11SPIsolate_Type(TruthValue):defaultValue=2
_HpnicfDot11SPIsolate_Type.__name__=_G
_HpnicfDot11SPIsolate_Object=MibTableColumn
hpnicfDot11SPIsolate=_HpnicfDot11SPIsolate_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,4,2,2,1,17),_HpnicfDot11SPIsolate_Type())
hpnicfDot11SPIsolate.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfDot11SPIsolate.setStatus(_A)
_HpnicfDot11WlanexAuthServerIP_Type=IpAddress
_HpnicfDot11WlanexAuthServerIP_Object=MibTableColumn
hpnicfDot11WlanexAuthServerIP=_HpnicfDot11WlanexAuthServerIP_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,4,2,2,1,18),_HpnicfDot11WlanexAuthServerIP_Type())
hpnicfDot11WlanexAuthServerIP.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfDot11WlanexAuthServerIP.setStatus(_A)
class _HpnicfDot11SPBeaconMeasEnable_Type(TruthValue):defaultValue=2
_HpnicfDot11SPBeaconMeasEnable_Type.__name__=_G
_HpnicfDot11SPBeaconMeasEnable_Object=MibTableColumn
hpnicfDot11SPBeaconMeasEnable=_HpnicfDot11SPBeaconMeasEnable_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,4,2,2,1,19),_HpnicfDot11SPBeaconMeasEnable_Type())
hpnicfDot11SPBeaconMeasEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfDot11SPBeaconMeasEnable.setStatus(_A)
class _HpnicfDot11SPBeaconMeasType_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_w,1),(_v,2),('beaconTable',3)))
_HpnicfDot11SPBeaconMeasType_Type.__name__=_D
_HpnicfDot11SPBeaconMeasType_Object=MibTableColumn
hpnicfDot11SPBeaconMeasType=_HpnicfDot11SPBeaconMeasType_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,4,2,2,1,20),_HpnicfDot11SPBeaconMeasType_Type())
hpnicfDot11SPBeaconMeasType.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfDot11SPBeaconMeasType.setStatus(_A)
class _HpnicfDot11SPBeaconMeasInterval_Type(Integer32):defaultValue=60;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(10,200))
_HpnicfDot11SPBeaconMeasInterval_Type.__name__=_D
_HpnicfDot11SPBeaconMeasInterval_Object=MibTableColumn
hpnicfDot11SPBeaconMeasInterval=_HpnicfDot11SPBeaconMeasInterval_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,4,2,2,1,21),_HpnicfDot11SPBeaconMeasInterval_Type())
hpnicfDot11SPBeaconMeasInterval.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfDot11SPBeaconMeasInterval.setStatus(_A)
if mibBuilder.loadTexts:hpnicfDot11SPBeaconMeasInterval.setUnits(_J)
class _HpnicfDot11AuthenModeCM_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('opensystem',0),('sharedkey',1)))
_HpnicfDot11AuthenModeCM_Type.__name__=_D
_HpnicfDot11AuthenModeCM_Object=MibTableColumn
hpnicfDot11AuthenModeCM=_HpnicfDot11AuthenModeCM_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,4,2,2,1,22),_HpnicfDot11AuthenModeCM_Type())
hpnicfDot11AuthenModeCM.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfDot11AuthenModeCM.setStatus(_A)
class _HpnicfDot11SecIEStatusCM_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*((_g,0),('wpa',1),('wpa2',2),('wlanex',3)))
_HpnicfDot11SecIEStatusCM_Type.__name__=_D
_HpnicfDot11SecIEStatusCM_Object=MibTableColumn
hpnicfDot11SecIEStatusCM=_HpnicfDot11SecIEStatusCM_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,4,2,2,1,23),_HpnicfDot11SecIEStatusCM_Type())
hpnicfDot11SecIEStatusCM.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfDot11SecIEStatusCM.setStatus(_A)
class _HpnicfDot11SecurityCiphersCM_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5)));namedValues=NamedValues(*((_g,0),('wep40',1),('wep104',2),('tkip',3),('aesccmp',4),('wpisms4',5)))
_HpnicfDot11SecurityCiphersCM_Type.__name__=_D
_HpnicfDot11SecurityCiphersCM_Object=MibTableColumn
hpnicfDot11SecurityCiphersCM=_HpnicfDot11SecurityCiphersCM_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,4,2,2,1,24),_HpnicfDot11SecurityCiphersCM_Type())
hpnicfDot11SecurityCiphersCM.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfDot11SecurityCiphersCM.setStatus(_A)
class _HpnicfDot11SrvPolicyStatusCM_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_P,0),(_Q,1)))
_HpnicfDot11SrvPolicyStatusCM_Type.__name__=_D
_HpnicfDot11SrvPolicyStatusCM_Object=MibTableColumn
hpnicfDot11SrvPolicyStatusCM=_HpnicfDot11SrvPolicyStatusCM_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,4,2,2,1,25),_HpnicfDot11SrvPolicyStatusCM_Type())
hpnicfDot11SrvPolicyStatusCM.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfDot11SrvPolicyStatusCM.setStatus(_A)
class _HpnicfDot11SSIDHiddenCM_Type(HpnicfDot11TruthValueCM):defaultValue=0
_HpnicfDot11SSIDHiddenCM_Type.__name__=_S
_HpnicfDot11SSIDHiddenCM_Object=MibTableColumn
hpnicfDot11SSIDHiddenCM=_HpnicfDot11SSIDHiddenCM_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,4,2,2,1,26),_HpnicfDot11SSIDHiddenCM_Type())
hpnicfDot11SSIDHiddenCM.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfDot11SSIDHiddenCM.setStatus(_A)
class _HpnicfDot11SPIsolateCM_Type(HpnicfDot11TruthValueCM):defaultValue=0
_HpnicfDot11SPIsolateCM_Type.__name__=_S
_HpnicfDot11SPIsolateCM_Object=MibTableColumn
hpnicfDot11SPIsolateCM=_HpnicfDot11SPIsolateCM_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,4,2,2,1,27),_HpnicfDot11SPIsolateCM_Type())
hpnicfDot11SPIsolateCM.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfDot11SPIsolateCM.setStatus(_A)
_HpnicfDot11ServicePolicyExtTable_Object=MibTable
hpnicfDot11ServicePolicyExtTable=_HpnicfDot11ServicePolicyExtTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,4,2,3))
if mibBuilder.loadTexts:hpnicfDot11ServicePolicyExtTable.setStatus(_A)
_HpnicfDot11ServicePolicyExtEntry_Object=MibTableRow
hpnicfDot11ServicePolicyExtEntry=_HpnicfDot11ServicePolicyExtEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,4,2,3,1))
hpnicfDot11ServicePolicyExtEntry.setIndexNames((0,_E,_A0))
if mibBuilder.loadTexts:hpnicfDot11ServicePolicyExtEntry.setStatus(_A)
_HpnicfDot11ServicePolicyExtID_Type=HpnicfDot11ServicePolicyIDType
_HpnicfDot11ServicePolicyExtID_Object=MibTableColumn
hpnicfDot11ServicePolicyExtID=_HpnicfDot11ServicePolicyExtID_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,4,2,3,1,1),_HpnicfDot11ServicePolicyExtID_Type())
hpnicfDot11ServicePolicyExtID.setMaxAccess(_F)
if mibBuilder.loadTexts:hpnicfDot11ServicePolicyExtID.setStatus(_A)
_HpnicfDot11SecIEStatus_Type=HpnicfDot11SecIEStatusType
_HpnicfDot11SecIEStatus_Object=MibTableColumn
hpnicfDot11SecIEStatus=_HpnicfDot11SecIEStatus_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,4,2,3,1,2),_HpnicfDot11SecIEStatus_Type())
hpnicfDot11SecIEStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfDot11SecIEStatus.setStatus(_A)
_HpnicfDot11SecurityCiphers_Type=Integer32
_HpnicfDot11SecurityCiphers_Object=MibTableColumn
hpnicfDot11SecurityCiphers=_HpnicfDot11SecurityCiphers_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,4,2,3,1,3),_HpnicfDot11SecurityCiphers_Type())
hpnicfDot11SecurityCiphers.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfDot11SecurityCiphers.setStatus(_A)
class _HpnicfDot11CipherKeyIndex_Type(Integer32):defaultValue=1
_HpnicfDot11CipherKeyIndex_Type.__name__=_D
_HpnicfDot11CipherKeyIndex_Object=MibTableColumn
hpnicfDot11CipherKeyIndex=_HpnicfDot11CipherKeyIndex_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,4,2,3,1,4),_HpnicfDot11CipherKeyIndex_Type())
hpnicfDot11CipherKeyIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfDot11CipherKeyIndex.setStatus(_A)
_HpnicfDot11CipherKey_Type=OctetString
_HpnicfDot11CipherKey_Object=MibTableColumn
hpnicfDot11CipherKey=_HpnicfDot11CipherKey_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,4,2,3,1,5),_HpnicfDot11CipherKey_Type())
hpnicfDot11CipherKey.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfDot11CipherKey.setStatus(_A)
_HpnicfDot11SrvPolicyExtRowStatus_Type=RowStatus
_HpnicfDot11SrvPolicyExtRowStatus_Object=MibTableColumn
hpnicfDot11SrvPolicyExtRowStatus=_HpnicfDot11SrvPolicyExtRowStatus_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,4,2,3,1,6),_HpnicfDot11SrvPolicyExtRowStatus_Type())
hpnicfDot11SrvPolicyExtRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfDot11SrvPolicyExtRowStatus.setStatus(_A)
class _HpnicfDot11CipherKeyType_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('char',1),('hex',2)))
_HpnicfDot11CipherKeyType_Type.__name__=_D
_HpnicfDot11CipherKeyType_Object=MibTableColumn
hpnicfDot11CipherKeyType=_HpnicfDot11CipherKeyType_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,4,2,3,1,7),_HpnicfDot11CipherKeyType_Type())
hpnicfDot11CipherKeyType.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfDot11CipherKeyType.setStatus(_A)
_HpnicfDot11RadioPolicyExtTable_Object=MibTable
hpnicfDot11RadioPolicyExtTable=_HpnicfDot11RadioPolicyExtTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,4,2,4))
if mibBuilder.loadTexts:hpnicfDot11RadioPolicyExtTable.setStatus(_A)
_HpnicfDot11RadioPolicyExtEntry_Object=MibTableRow
hpnicfDot11RadioPolicyExtEntry=_HpnicfDot11RadioPolicyExtEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,4,2,4,1))
hpnicfDot11RadioPolicyExtEntry.setIndexNames((0,_E,_A1),(0,_E,_A2))
if mibBuilder.loadTexts:hpnicfDot11RadioPolicyExtEntry.setStatus(_A)
class _HpnicfDot11RPAPSerialID_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,127))
_HpnicfDot11RPAPSerialID_Type.__name__=_H
_HpnicfDot11RPAPSerialID_Object=MibTableColumn
hpnicfDot11RPAPSerialID=_HpnicfDot11RPAPSerialID_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,4,2,4,1,1),_HpnicfDot11RPAPSerialID_Type())
hpnicfDot11RPAPSerialID.setMaxAccess(_F)
if mibBuilder.loadTexts:hpnicfDot11RPAPSerialID.setStatus(_A)
_HpnicfDot11RPRadioID_Type=HpnicfDot11RadioScopeType
_HpnicfDot11RPRadioID_Object=MibTableColumn
hpnicfDot11RPRadioID=_HpnicfDot11RPRadioID_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,4,2,4,1,2),_HpnicfDot11RPRadioID_Type())
hpnicfDot11RPRadioID.setMaxAccess(_F)
if mibBuilder.loadTexts:hpnicfDot11RPRadioID.setStatus(_A)
class _HpnicfDot11RPBeaconInterval_Type(Integer32):defaultValue=100
_HpnicfDot11RPBeaconInterval_Type.__name__=_D
_HpnicfDot11RPBeaconInterval_Object=MibTableColumn
hpnicfDot11RPBeaconInterval=_HpnicfDot11RPBeaconInterval_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,4,2,4,1,3),_HpnicfDot11RPBeaconInterval_Type())
hpnicfDot11RPBeaconInterval.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11RPBeaconInterval.setStatus(_A)
if mibBuilder.loadTexts:hpnicfDot11RPBeaconInterval.setUnits('milliseconds')
class _HpnicfDot11RPDtimInterval_Type(Integer32):defaultValue=1
_HpnicfDot11RPDtimInterval_Type.__name__=_D
_HpnicfDot11RPDtimInterval_Object=MibTableColumn
hpnicfDot11RPDtimInterval=_HpnicfDot11RPDtimInterval_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,4,2,4,1,4),_HpnicfDot11RPDtimInterval_Type())
hpnicfDot11RPDtimInterval.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11RPDtimInterval.setStatus(_A)
class _HpnicfDot11RPRtsThreshold_Type(Integer32):defaultValue=2346
_HpnicfDot11RPRtsThreshold_Type.__name__=_D
_HpnicfDot11RPRtsThreshold_Object=MibTableColumn
hpnicfDot11RPRtsThreshold=_HpnicfDot11RPRtsThreshold_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,4,2,4,1,5),_HpnicfDot11RPRtsThreshold_Type())
hpnicfDot11RPRtsThreshold.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11RPRtsThreshold.setStatus(_A)
if mibBuilder.loadTexts:hpnicfDot11RPRtsThreshold.setUnits(_V)
class _HpnicfDot11RPFragThreshold_Type(Integer32):defaultValue=2346
_HpnicfDot11RPFragThreshold_Type.__name__=_D
_HpnicfDot11RPFragThreshold_Object=MibTableColumn
hpnicfDot11RPFragThreshold=_HpnicfDot11RPFragThreshold_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,4,2,4,1,6),_HpnicfDot11RPFragThreshold_Type())
hpnicfDot11RPFragThreshold.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11RPFragThreshold.setStatus(_A)
if mibBuilder.loadTexts:hpnicfDot11RPFragThreshold.setUnits(_V)
class _HpnicfDot11RPShortRetryThreshold_Type(Integer32):defaultValue=7
_HpnicfDot11RPShortRetryThreshold_Type.__name__=_D
_HpnicfDot11RPShortRetryThreshold_Object=MibTableColumn
hpnicfDot11RPShortRetryThreshold=_HpnicfDot11RPShortRetryThreshold_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,4,2,4,1,7),_HpnicfDot11RPShortRetryThreshold_Type())
hpnicfDot11RPShortRetryThreshold.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11RPShortRetryThreshold.setStatus(_A)
class _HpnicfDot11RPLongRetryThreshold_Type(Integer32):defaultValue=4
_HpnicfDot11RPLongRetryThreshold_Type.__name__=_D
_HpnicfDot11RPLongRetryThreshold_Object=MibTableColumn
hpnicfDot11RPLongRetryThreshold=_HpnicfDot11RPLongRetryThreshold_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,4,2,4,1,8),_HpnicfDot11RPLongRetryThreshold_Type())
hpnicfDot11RPLongRetryThreshold.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11RPLongRetryThreshold.setStatus(_A)
class _HpnicfDot11RPClientMaxCount_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_HpnicfDot11RPClientMaxCount_Type.__name__=_D
_HpnicfDot11RPClientMaxCount_Object=MibTableColumn
hpnicfDot11RPClientMaxCount=_HpnicfDot11RPClientMaxCount_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,4,2,4,1,9),_HpnicfDot11RPClientMaxCount_Type())
hpnicfDot11RPClientMaxCount.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11RPClientMaxCount.setStatus(_A)
class _HpnicfDot11RPBeaconIntervalCM_Type(Integer32):defaultValue=100
_HpnicfDot11RPBeaconIntervalCM_Type.__name__=_D
_HpnicfDot11RPBeaconIntervalCM_Object=MibTableColumn
hpnicfDot11RPBeaconIntervalCM=_HpnicfDot11RPBeaconIntervalCM_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,4,2,4,1,10),_HpnicfDot11RPBeaconIntervalCM_Type())
hpnicfDot11RPBeaconIntervalCM.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11RPBeaconIntervalCM.setStatus(_A)
if mibBuilder.loadTexts:hpnicfDot11RPBeaconIntervalCM.setUnits('timeunit')
_HpnicfDot11SrvPortSecurityTable_Object=MibTable
hpnicfDot11SrvPortSecurityTable=_HpnicfDot11SrvPortSecurityTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,4,2,5))
if mibBuilder.loadTexts:hpnicfDot11SrvPortSecurityTable.setStatus(_A)
_HpnicfDot11SrvPortSecurityEntry_Object=MibTableRow
hpnicfDot11SrvPortSecurityEntry=_HpnicfDot11SrvPortSecurityEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,4,2,5,1))
hpnicfDot11SrvPortSecurityEntry.setIndexNames((0,_E,_A3))
if mibBuilder.loadTexts:hpnicfDot11SrvPortSecurityEntry.setStatus(_A)
_HpnicfDot11SecurityServicePolicyID_Type=HpnicfDot11ServicePolicyIDType
_HpnicfDot11SecurityServicePolicyID_Object=MibTableColumn
hpnicfDot11SecurityServicePolicyID=_HpnicfDot11SecurityServicePolicyID_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,4,2,5,1,1),_HpnicfDot11SecurityServicePolicyID_Type())
hpnicfDot11SecurityServicePolicyID.setMaxAccess(_F)
if mibBuilder.loadTexts:hpnicfDot11SecurityServicePolicyID.setStatus(_A)
class _HpnicfDot11SrvPortSecurityMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*((_A4,1),(_A5,2),(_h,3),(_A6,4),(_A7,5),('ext',6)))
_HpnicfDot11SrvPortSecurityMode_Type.__name__=_D
_HpnicfDot11SrvPortSecurityMode_Object=MibTableColumn
hpnicfDot11SrvPortSecurityMode=_HpnicfDot11SrvPortSecurityMode_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,4,2,5,1,2),_HpnicfDot11SrvPortSecurityMode_Type())
hpnicfDot11SrvPortSecurityMode.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11SrvPortSecurityMode.setStatus(_A)
class _HpnicfDot11SrvSecurityKeyType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_A8,1),(_A9,2),(_AA,3)))
_HpnicfDot11SrvSecurityKeyType_Type.__name__=_D
_HpnicfDot11SrvSecurityKeyType_Object=MibTableColumn
hpnicfDot11SrvSecurityKeyType=_HpnicfDot11SrvSecurityKeyType_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,4,2,5,1,3),_HpnicfDot11SrvSecurityKeyType_Type())
hpnicfDot11SrvSecurityKeyType.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11SrvSecurityKeyType.setStatus(_A)
class _HpnicfDot11SrvSecurityPskKeyMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_i,1),(_j,2),(_k,3)))
_HpnicfDot11SrvSecurityPskKeyMode_Type.__name__=_D
_HpnicfDot11SrvSecurityPskKeyMode_Object=MibTableColumn
hpnicfDot11SrvSecurityPskKeyMode=_HpnicfDot11SrvSecurityPskKeyMode_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,4,2,5,1,4),_HpnicfDot11SrvSecurityPskKeyMode_Type())
hpnicfDot11SrvSecurityPskKeyMode.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11SrvSecurityPskKeyMode.setStatus(_A)
class _HpnicfDot11SrvSecurityPskKeyString_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_HpnicfDot11SrvSecurityPskKeyString_Type.__name__=_b
_HpnicfDot11SrvSecurityPskKeyString_Object=MibTableColumn
hpnicfDot11SrvSecurityPskKeyString=_HpnicfDot11SrvSecurityPskKeyString_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,4,2,5,1,5),_HpnicfDot11SrvSecurityPskKeyString_Type())
hpnicfDot11SrvSecurityPskKeyString.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11SrvSecurityPskKeyString.setStatus(_A)
class _HpnicfDot11SrvPortSecurityModeCM_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*((_g,0),(_h,1),('radius',2),('wlanex',3)))
_HpnicfDot11SrvPortSecurityModeCM_Type.__name__=_D
_HpnicfDot11SrvPortSecurityModeCM_Object=MibTableColumn
hpnicfDot11SrvPortSecurityModeCM=_HpnicfDot11SrvPortSecurityModeCM_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,4,2,5,1,6),_HpnicfDot11SrvPortSecurityModeCM_Type())
hpnicfDot11SrvPortSecurityModeCM.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11SrvPortSecurityModeCM.setStatus(_A)
_HpnicfDot11SrvPolicyExtendTable_Object=MibTable
hpnicfDot11SrvPolicyExtendTable=_HpnicfDot11SrvPolicyExtendTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,4,2,6))
if mibBuilder.loadTexts:hpnicfDot11SrvPolicyExtendTable.setStatus(_A)
_HpnicfDot11SrvPolicyExtendEntry_Object=MibTableRow
hpnicfDot11SrvPolicyExtendEntry=_HpnicfDot11SrvPolicyExtendEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,4,2,6,1))
hpnicfDot11SrvPolicyExtendEntry.setIndexNames((0,_E,_f))
if mibBuilder.loadTexts:hpnicfDot11SrvPolicyExtendEntry.setStatus(_A)
class _HpnicfDot11SPEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_d,1),(_e,2)))
_HpnicfDot11SPEnable_Type.__name__=_D
_HpnicfDot11SPEnable_Object=MibTableColumn
hpnicfDot11SPEnable=_HpnicfDot11SPEnable_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,4,2,6,1,1),_HpnicfDot11SPEnable_Type())
hpnicfDot11SPEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11SPEnable.setStatus(_A)
_HpnicfDot11APConfigGroup_ObjectIdentity=ObjectIdentity
hpnicfDot11APConfigGroup=_HpnicfDot11APConfigGroup_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,75,4,3))
_HpnicfDot11APTemplateTable_Object=MibTable
hpnicfDot11APTemplateTable=_HpnicfDot11APTemplateTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,4,3,1))
if mibBuilder.loadTexts:hpnicfDot11APTemplateTable.setStatus(_A)
_HpnicfDot11APTemplateEntry_Object=MibTableRow
hpnicfDot11APTemplateEntry=_HpnicfDot11APTemplateEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,4,3,1,1))
hpnicfDot11APTemplateEntry.setIndexNames((0,_E,_AB))
if mibBuilder.loadTexts:hpnicfDot11APTemplateEntry.setStatus(_A)
class _HpnicfDot11APTemplateName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,127))
_HpnicfDot11APTemplateName_Type.__name__=_H
_HpnicfDot11APTemplateName_Object=MibTableColumn
hpnicfDot11APTemplateName=_HpnicfDot11APTemplateName_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,4,3,1,1,1),_HpnicfDot11APTemplateName_Type())
hpnicfDot11APTemplateName.setMaxAccess(_F)
if mibBuilder.loadTexts:hpnicfDot11APTemplateName.setStatus(_A)
_HpnicfDot11APSerialID_Type=OctetString
_HpnicfDot11APSerialID_Object=MibTableColumn
hpnicfDot11APSerialID=_HpnicfDot11APSerialID_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,4,3,1,1,2),_HpnicfDot11APSerialID_Type())
hpnicfDot11APSerialID.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfDot11APSerialID.setStatus(_A)
_HpnicfDot11TemplateAPModelAlias_Type=OctetString
_HpnicfDot11TemplateAPModelAlias_Object=MibTableColumn
hpnicfDot11TemplateAPModelAlias=_HpnicfDot11TemplateAPModelAlias_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,4,3,1,1,3),_HpnicfDot11TemplateAPModelAlias_Type())
hpnicfDot11TemplateAPModelAlias.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfDot11TemplateAPModelAlias.setStatus(_A)
_HpnicfDot11Description_Type=OctetString
_HpnicfDot11Description_Object=MibTableColumn
hpnicfDot11Description=_HpnicfDot11Description_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,4,3,1,1,4),_HpnicfDot11Description_Type())
hpnicfDot11Description.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfDot11Description.setStatus(_A)
class _HpnicfDot11APWorkMode_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_L,1),(_U,2),(_c,3)))
_HpnicfDot11APWorkMode_Type.__name__=_D
_HpnicfDot11APWorkMode_Object=MibTableColumn
hpnicfDot11APWorkMode=_HpnicfDot11APWorkMode_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,4,3,1,1,5),_HpnicfDot11APWorkMode_Type())
hpnicfDot11APWorkMode.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfDot11APWorkMode.setStatus(_A)
_HpnicfDot11APTemplateRowStatus_Type=RowStatus
_HpnicfDot11APTemplateRowStatus_Object=MibTableColumn
hpnicfDot11APTemplateRowStatus=_HpnicfDot11APTemplateRowStatus_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,4,3,1,1,6),_HpnicfDot11APTemplateRowStatus_Type())
hpnicfDot11APTemplateRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfDot11APTemplateRowStatus.setStatus(_A)
_HpnicfDot11APName_Type=OctetString
_HpnicfDot11APName_Object=MibTableColumn
hpnicfDot11APName=_HpnicfDot11APName_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,4,3,1,1,7),_HpnicfDot11APName_Type())
hpnicfDot11APName.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfDot11APName.setStatus(_A)
_HpnicfDot11StatisInterv_Type=Integer32
_HpnicfDot11StatisInterv_Object=MibTableColumn
hpnicfDot11StatisInterv=_HpnicfDot11StatisInterv_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,4,3,1,1,8),_HpnicfDot11StatisInterv_Type())
hpnicfDot11StatisInterv.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfDot11StatisInterv.setStatus(_A)
if mibBuilder.loadTexts:hpnicfDot11StatisInterv.setUnits(_J)
class _HpnicfDot11APBroadcastProbeReply_Type(TruthValue):defaultValue=1
_HpnicfDot11APBroadcastProbeReply_Type.__name__=_G
_HpnicfDot11APBroadcastProbeReply_Object=MibTableColumn
hpnicfDot11APBroadcastProbeReply=_HpnicfDot11APBroadcastProbeReply_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,4,3,1,1,9),_HpnicfDot11APBroadcastProbeReply_Type())
hpnicfDot11APBroadcastProbeReply.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfDot11APBroadcastProbeReply.setStatus(_A)
_HpnicfDot11StaIdleTimerInterv_Type=Integer32
_HpnicfDot11StaIdleTimerInterv_Object=MibTableColumn
hpnicfDot11StaIdleTimerInterv=_HpnicfDot11StaIdleTimerInterv_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,4,3,1,1,10),_HpnicfDot11StaIdleTimerInterv_Type())
hpnicfDot11StaIdleTimerInterv.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfDot11StaIdleTimerInterv.setStatus(_A)
if mibBuilder.loadTexts:hpnicfDot11StaIdleTimerInterv.setUnits(_J)
_HpnicfDot11StaKeepAliveTimerInterv_Type=Integer32
_HpnicfDot11StaKeepAliveTimerInterv_Object=MibTableColumn
hpnicfDot11StaKeepAliveTimerInterv=_HpnicfDot11StaKeepAliveTimerInterv_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,4,3,1,1,11),_HpnicfDot11StaKeepAliveTimerInterv_Type())
hpnicfDot11StaKeepAliveTimerInterv.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfDot11StaKeepAliveTimerInterv.setStatus(_A)
if mibBuilder.loadTexts:hpnicfDot11StaKeepAliveTimerInterv.setUnits(_J)
_HpnicfDot11APCir_Type=Integer32
_HpnicfDot11APCir_Object=MibTableColumn
hpnicfDot11APCir=_HpnicfDot11APCir_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,4,3,1,1,12),_HpnicfDot11APCir_Type())
hpnicfDot11APCir.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfDot11APCir.setStatus(_A)
if mibBuilder.loadTexts:hpnicfDot11APCir.setUnits(_M)
_HpnicfDot11APCbs_Type=Integer32
_HpnicfDot11APCbs_Object=MibTableColumn
hpnicfDot11APCbs=_HpnicfDot11APCbs_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,4,3,1,1,13),_HpnicfDot11APCbs_Type())
hpnicfDot11APCbs.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfDot11APCbs.setStatus(_A)
if mibBuilder.loadTexts:hpnicfDot11APCbs.setUnits('Bytes')
class _HpnicfDot11APPriorityLevel_Type(Integer32):defaultValue=4;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_HpnicfDot11APPriorityLevel_Type.__name__=_D
_HpnicfDot11APPriorityLevel_Object=MibTableColumn
hpnicfDot11APPriorityLevel=_HpnicfDot11APPriorityLevel_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,4,3,1,1,14),_HpnicfDot11APPriorityLevel_Type())
hpnicfDot11APPriorityLevel.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfDot11APPriorityLevel.setStatus(_A)
_HpnicfDot11APElementID_Type=Integer32
_HpnicfDot11APElementID_Object=MibTableColumn
hpnicfDot11APElementID=_HpnicfDot11APElementID_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,4,3,1,1,15),_HpnicfDot11APElementID_Type())
hpnicfDot11APElementID.setMaxAccess(_I)
if mibBuilder.loadTexts:hpnicfDot11APElementID.setStatus(_A)
class _HpnicfDot11APDevDetectEnable_Type(TruthValue):defaultValue=2
_HpnicfDot11APDevDetectEnable_Type.__name__=_G
_HpnicfDot11APDevDetectEnable_Object=MibTableColumn
hpnicfDot11APDevDetectEnable=_HpnicfDot11APDevDetectEnable_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,4,3,1,1,16),_HpnicfDot11APDevDetectEnable_Type())
hpnicfDot11APDevDetectEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfDot11APDevDetectEnable.setStatus(_A)
class _HpnicfDot11APGetIPMethod_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_AC,1),('static',2)))
_HpnicfDot11APGetIPMethod_Type.__name__=_D
_HpnicfDot11APGetIPMethod_Object=MibTableColumn
hpnicfDot11APGetIPMethod=_HpnicfDot11APGetIPMethod_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,4,3,1,1,17),_HpnicfDot11APGetIPMethod_Type())
hpnicfDot11APGetIPMethod.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfDot11APGetIPMethod.setStatus(_A)
class _HpnicfDot11StatisIntervMode_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_L,1),('realtime',2)))
_HpnicfDot11StatisIntervMode_Type.__name__=_D
_HpnicfDot11StatisIntervMode_Object=MibTableColumn
hpnicfDot11StatisIntervMode=_HpnicfDot11StatisIntervMode_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,4,3,1,1,18),_HpnicfDot11StatisIntervMode_Type())
hpnicfDot11StatisIntervMode.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfDot11StatisIntervMode.setStatus(_A)
class _HpnicfDot11ApTrapEnabled_Type(TruthValue):defaultValue=1
_HpnicfDot11ApTrapEnabled_Type.__name__=_G
_HpnicfDot11ApTrapEnabled_Object=MibTableColumn
hpnicfDot11ApTrapEnabled=_HpnicfDot11ApTrapEnabled_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,4,3,1,1,19),_HpnicfDot11ApTrapEnabled_Type())
hpnicfDot11ApTrapEnabled.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11ApTrapEnabled.setStatus(_A)
class _HpnicfDot11ApFmwUpdState_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_d,1),(_e,2),('inherit',3)))
_HpnicfDot11ApFmwUpdState_Type.__name__=_D
_HpnicfDot11ApFmwUpdState_Object=MibTableColumn
hpnicfDot11ApFmwUpdState=_HpnicfDot11ApFmwUpdState_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,4,3,1,1,20),_HpnicfDot11ApFmwUpdState_Type())
hpnicfDot11ApFmwUpdState.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfDot11ApFmwUpdState.setStatus(_A)
class _HpnicfDot11StatisIntervModeCM_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_P,0),(_Q,1)))
_HpnicfDot11StatisIntervModeCM_Type.__name__=_D
_HpnicfDot11StatisIntervModeCM_Object=MibTableColumn
hpnicfDot11StatisIntervModeCM=_HpnicfDot11StatisIntervModeCM_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,4,3,1,1,21),_HpnicfDot11StatisIntervModeCM_Type())
hpnicfDot11StatisIntervModeCM.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfDot11StatisIntervModeCM.setStatus(_A)
_HpnicfDot11ApNasIDCM_Type=OctetString
_HpnicfDot11ApNasIDCM_Object=MibTableColumn
hpnicfDot11ApNasIDCM=_HpnicfDot11ApNasIDCM_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,4,3,1,1,22),_HpnicfDot11ApNasIDCM_Type())
hpnicfDot11ApNasIDCM.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfDot11ApNasIDCM.setStatus(_A)
_HpnicfDot11RadioToConfigTable_Object=MibTable
hpnicfDot11RadioToConfigTable=_HpnicfDot11RadioToConfigTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,4,3,2))
if mibBuilder.loadTexts:hpnicfDot11RadioToConfigTable.setStatus(_A)
_HpnicfDot11RadioToConfigEntry_Object=MibTableRow
hpnicfDot11RadioToConfigEntry=_HpnicfDot11RadioToConfigEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,4,3,2,1))
hpnicfDot11RadioToConfigEntry.setIndexNames((0,_E,_l),(0,_E,_W))
if mibBuilder.loadTexts:hpnicfDot11RadioToConfigEntry.setStatus(_A)
class _HpnicfDot11APTemplateNameCfg_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,127))
_HpnicfDot11APTemplateNameCfg_Type.__name__=_H
_HpnicfDot11APTemplateNameCfg_Object=MibTableColumn
hpnicfDot11APTemplateNameCfg=_HpnicfDot11APTemplateNameCfg_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,4,3,2,1,1),_HpnicfDot11APTemplateNameCfg_Type())
hpnicfDot11APTemplateNameCfg.setMaxAccess(_F)
if mibBuilder.loadTexts:hpnicfDot11APTemplateNameCfg.setStatus(_A)
_HpnicfDot11CfgRadioID_Type=HpnicfDot11RadioScopeType
_HpnicfDot11CfgRadioID_Object=MibTableColumn
hpnicfDot11CfgRadioID=_HpnicfDot11CfgRadioID_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,4,3,2,1,2),_HpnicfDot11CfgRadioID_Type())
hpnicfDot11CfgRadioID.setMaxAccess(_F)
if mibBuilder.loadTexts:hpnicfDot11CfgRadioID.setStatus(_A)
_HpnicfDot11CfgRadioPolicyName_Type=OctetString
_HpnicfDot11CfgRadioPolicyName_Object=MibTableColumn
hpnicfDot11CfgRadioPolicyName=_HpnicfDot11CfgRadioPolicyName_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,4,3,2,1,3),_HpnicfDot11CfgRadioPolicyName_Type())
hpnicfDot11CfgRadioPolicyName.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11CfgRadioPolicyName.setStatus(_A)
_HpnicfDot11CfgRadioType_Type=HpnicfDot11RadioType
_HpnicfDot11CfgRadioType_Object=MibTableColumn
hpnicfDot11CfgRadioType=_HpnicfDot11CfgRadioType_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,4,3,2,1,4),_HpnicfDot11CfgRadioType_Type())
hpnicfDot11CfgRadioType.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11CfgRadioType.setStatus(_A)
_HpnicfDot11CfgChannel_Type=HpnicfDot11ChannelScopeType
_HpnicfDot11CfgChannel_Object=MibTableColumn
hpnicfDot11CfgChannel=_HpnicfDot11CfgChannel_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,4,3,2,1,5),_HpnicfDot11CfgChannel_Type())
hpnicfDot11CfgChannel.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11CfgChannel.setStatus(_A)
_HpnicfDot11CfgMaxTxPowerLevel_Type=HpnicfDot11TxPwrLevelScopeType
_HpnicfDot11CfgMaxTxPowerLevel_Object=MibTableColumn
hpnicfDot11CfgMaxTxPowerLevel=_HpnicfDot11CfgMaxTxPowerLevel_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,4,3,2,1,6),_HpnicfDot11CfgMaxTxPowerLevel_Type())
hpnicfDot11CfgMaxTxPowerLevel.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11CfgMaxTxPowerLevel.setStatus(_A)
if mibBuilder.loadTexts:hpnicfDot11CfgMaxTxPowerLevel.setUnits(_O)
class _HpnicfDot11PreambleLen_Type(HpnicfDot11PreambleType):defaultValue=2
_HpnicfDot11PreambleLen_Type.__name__=_R
_HpnicfDot11PreambleLen_Object=MibTableColumn
hpnicfDot11PreambleLen=_HpnicfDot11PreambleLen_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,4,3,2,1,7),_HpnicfDot11PreambleLen_Type())
hpnicfDot11PreambleLen.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11PreambleLen.setStatus(_A)
_HpnicfDot11CfgRadioStatus_Type=TruthValue
_HpnicfDot11CfgRadioStatus_Object=MibTableColumn
hpnicfDot11CfgRadioStatus=_HpnicfDot11CfgRadioStatus_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,4,3,2,1,8),_HpnicfDot11CfgRadioStatus_Type())
hpnicfDot11CfgRadioStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11CfgRadioStatus.setStatus(_A)
_HpnicfDot11CfgRdElementID_Type=Unsigned32
_HpnicfDot11CfgRdElementID_Object=MibTableColumn
hpnicfDot11CfgRdElementID=_HpnicfDot11CfgRdElementID_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,4,3,2,1,9),_HpnicfDot11CfgRdElementID_Type())
hpnicfDot11CfgRdElementID.setMaxAccess(_I)
if mibBuilder.loadTexts:hpnicfDot11CfgRdElementID.setStatus(_A)
_HpnicfDot11CfgWorkMode_Type=HpnicfDot11WorkMode
_HpnicfDot11CfgWorkMode_Object=MibTableColumn
hpnicfDot11CfgWorkMode=_HpnicfDot11CfgWorkMode_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,4,3,2,1,10),_HpnicfDot11CfgWorkMode_Type())
hpnicfDot11CfgWorkMode.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11CfgWorkMode.setStatus(_A)
_HpnicfDot11CfgPwrAttValue_Type=Integer32
_HpnicfDot11CfgPwrAttValue_Object=MibTableColumn
hpnicfDot11CfgPwrAttValue=_HpnicfDot11CfgPwrAttValue_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,4,3,2,1,11),_HpnicfDot11CfgPwrAttValue_Type())
hpnicfDot11CfgPwrAttValue.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11CfgPwrAttValue.setStatus(_A)
class _HpnicfDot11RadioTxArithmetic_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('quality',1),('bandwidth',2)))
_HpnicfDot11RadioTxArithmetic_Type.__name__=_D
_HpnicfDot11RadioTxArithmetic_Object=MibTableColumn
hpnicfDot11RadioTxArithmetic=_HpnicfDot11RadioTxArithmetic_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,4,3,2,1,12),_HpnicfDot11RadioTxArithmetic_Type())
hpnicfDot11RadioTxArithmetic.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11RadioTxArithmetic.setStatus(_A)
class _HpnicfDot11CfgChannelLockStat_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('unlocked',1),('locked',2)))
_HpnicfDot11CfgChannelLockStat_Type.__name__=_D
_HpnicfDot11CfgChannelLockStat_Object=MibTableColumn
hpnicfDot11CfgChannelLockStat=_HpnicfDot11CfgChannelLockStat_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,4,3,2,1,13),_HpnicfDot11CfgChannelLockStat_Type())
hpnicfDot11CfgChannelLockStat.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11CfgChannelLockStat.setStatus(_A)
class _HpnicfDot11CfgPowerLockStat_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('unlocked',1),('locked',2)))
_HpnicfDot11CfgPowerLockStat_Type.__name__=_D
_HpnicfDot11CfgPowerLockStat_Object=MibTableColumn
hpnicfDot11CfgPowerLockStat=_HpnicfDot11CfgPowerLockStat_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,4,3,2,1,14),_HpnicfDot11CfgPowerLockStat_Type())
hpnicfDot11CfgPowerLockStat.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11CfgPowerLockStat.setStatus(_A)
_HpnicfDot11CfgLBRdGroupId_Type=Unsigned32
_HpnicfDot11CfgLBRdGroupId_Object=MibTableColumn
hpnicfDot11CfgLBRdGroupId=_HpnicfDot11CfgLBRdGroupId_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,4,3,2,1,15),_HpnicfDot11CfgLBRdGroupId_Type())
hpnicfDot11CfgLBRdGroupId.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11CfgLBRdGroupId.setStatus(_A)
_HpnicfDot11CfgRRMSDRdGroupId_Type=Unsigned32
_HpnicfDot11CfgRRMSDRdGroupId_Object=MibTableColumn
hpnicfDot11CfgRRMSDRdGroupId=_HpnicfDot11CfgRRMSDRdGroupId_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,4,3,2,1,16),_HpnicfDot11CfgRRMSDRdGroupId_Type())
hpnicfDot11CfgRRMSDRdGroupId.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11CfgRRMSDRdGroupId.setStatus(_A)
_HpnicfDot11CfgRadioType2_Type=HpnicfDot11RadioType2
_HpnicfDot11CfgRadioType2_Object=MibTableColumn
hpnicfDot11CfgRadioType2=_HpnicfDot11CfgRadioType2_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,4,3,2,1,17),_HpnicfDot11CfgRadioType2_Type())
hpnicfDot11CfgRadioType2.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11CfgRadioType2.setStatus(_A)
_HpnicfDot11CfgIDSEnable_Type=TruthValue
_HpnicfDot11CfgIDSEnable_Object=MibTableColumn
hpnicfDot11CfgIDSEnable=_HpnicfDot11CfgIDSEnable_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,4,3,2,1,18),_HpnicfDot11CfgIDSEnable_Type())
hpnicfDot11CfgIDSEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11CfgIDSEnable.setStatus(_A)
_HpnicfDot11CfgSaEnable_Type=TruthValue
_HpnicfDot11CfgSaEnable_Object=MibTableColumn
hpnicfDot11CfgSaEnable=_HpnicfDot11CfgSaEnable_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,4,3,2,1,19),_HpnicfDot11CfgSaEnable_Type())
hpnicfDot11CfgSaEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11CfgSaEnable.setStatus(_A)
_HpnicfDot11CfgSaCltRtFFTData_Type=TruthValue
_HpnicfDot11CfgSaCltRtFFTData_Object=MibTableColumn
hpnicfDot11CfgSaCltRtFFTData=_HpnicfDot11CfgSaCltRtFFTData_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,4,3,2,1,20),_HpnicfDot11CfgSaCltRtFFTData_Type())
hpnicfDot11CfgSaCltRtFFTData.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11CfgSaCltRtFFTData.setStatus(_A)
class _HpnicfDot11CfgSaBand_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('dot11g',1),('dot11aLower',2),('dot11aMiddle',3),('dot11aUpper',4)))
_HpnicfDot11CfgSaBand_Type.__name__=_D
_HpnicfDot11CfgSaBand_Object=MibTableColumn
hpnicfDot11CfgSaBand=_HpnicfDot11CfgSaBand_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,4,3,2,1,21),_HpnicfDot11CfgSaBand_Type())
hpnicfDot11CfgSaBand.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11CfgSaBand.setStatus(_A)
_HpnicfDot11APServiceSetTable_Object=MibTable
hpnicfDot11APServiceSetTable=_HpnicfDot11APServiceSetTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,4,3,3))
if mibBuilder.loadTexts:hpnicfDot11APServiceSetTable.setStatus(_A)
_HpnicfDot11APServiceSetEntry_Object=MibTableRow
hpnicfDot11APServiceSetEntry=_HpnicfDot11APServiceSetEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,4,3,3,1))
hpnicfDot11APServiceSetEntry.setIndexNames((0,_E,_l),(0,_E,_W),(0,_E,_m))
if mibBuilder.loadTexts:hpnicfDot11APServiceSetEntry.setStatus(_A)
_HpnicfDot11CfgServicePolicyID_Type=HpnicfDot11ServicePolicyIDType
_HpnicfDot11CfgServicePolicyID_Object=MibTableColumn
hpnicfDot11CfgServicePolicyID=_HpnicfDot11CfgServicePolicyID_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,4,3,3,1,1),_HpnicfDot11CfgServicePolicyID_Type())
hpnicfDot11CfgServicePolicyID.setMaxAccess(_F)
if mibBuilder.loadTexts:hpnicfDot11CfgServicePolicyID.setStatus(_A)
_HpnicfDot11SrvSetRowStatus_Type=RowStatus
_HpnicfDot11SrvSetRowStatus_Object=MibTableColumn
hpnicfDot11SrvSetRowStatus=_HpnicfDot11SrvSetRowStatus_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,4,3,3,1,2),_HpnicfDot11SrvSetRowStatus_Type())
hpnicfDot11SrvSetRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfDot11SrvSetRowStatus.setStatus(_A)
class _HpnicfDot11ServiceSetVlanId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4094))
_HpnicfDot11ServiceSetVlanId_Type.__name__=_D
_HpnicfDot11ServiceSetVlanId_Object=MibTableColumn
hpnicfDot11ServiceSetVlanId=_HpnicfDot11ServiceSetVlanId_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,4,3,3,1,3),_HpnicfDot11ServiceSetVlanId_Type())
hpnicfDot11ServiceSetVlanId.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfDot11ServiceSetVlanId.setStatus(_A)
_HpnicfDot11APSysInfoSetTable_Object=MibTable
hpnicfDot11APSysInfoSetTable=_HpnicfDot11APSysInfoSetTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,4,3,4))
if mibBuilder.loadTexts:hpnicfDot11APSysInfoSetTable.setStatus(_A)
_HpnicfDot11APSysInfoSetEntry_Object=MibTableRow
hpnicfDot11APSysInfoSetEntry=_HpnicfDot11APSysInfoSetEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,4,3,4,1))
hpnicfDot11APSysInfoSetEntry.setIndexNames((0,_E,_X))
if mibBuilder.loadTexts:hpnicfDot11APSysInfoSetEntry.setStatus(_A)
class _HpnicfDot11APSysNetID_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,127))
_HpnicfDot11APSysNetID_Type.__name__=_H
_HpnicfDot11APSysNetID_Object=MibTableColumn
hpnicfDot11APSysNetID=_HpnicfDot11APSysNetID_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,4,3,4,1,1),_HpnicfDot11APSysNetID_Type())
hpnicfDot11APSysNetID.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11APSysNetID.setStatus(_A)
class _HpnicfDot11APCpuUsageThreshold_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_HpnicfDot11APCpuUsageThreshold_Type.__name__=_D
_HpnicfDot11APCpuUsageThreshold_Object=MibTableColumn
hpnicfDot11APCpuUsageThreshold=_HpnicfDot11APCpuUsageThreshold_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,4,3,4,1,2),_HpnicfDot11APCpuUsageThreshold_Type())
hpnicfDot11APCpuUsageThreshold.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11APCpuUsageThreshold.setStatus(_A)
if mibBuilder.loadTexts:hpnicfDot11APCpuUsageThreshold.setUnits(_T)
class _HpnicfDot11APMemUsageThreshold_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_HpnicfDot11APMemUsageThreshold_Type.__name__=_D
_HpnicfDot11APMemUsageThreshold_Object=MibTableColumn
hpnicfDot11APMemUsageThreshold=_HpnicfDot11APMemUsageThreshold_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,4,3,4,1,3),_HpnicfDot11APMemUsageThreshold_Type())
hpnicfDot11APMemUsageThreshold.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11APMemUsageThreshold.setStatus(_A)
if mibBuilder.loadTexts:hpnicfDot11APMemUsageThreshold.setUnits(_T)
_HpnicfDot11APLimitTable_Object=MibTable
hpnicfDot11APLimitTable=_HpnicfDot11APLimitTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,4,3,5))
if mibBuilder.loadTexts:hpnicfDot11APLimitTable.setStatus(_A)
_HpnicfDot11APLimitEntry_Object=MibTableRow
hpnicfDot11APLimitEntry=_HpnicfDot11APLimitEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,4,3,5,1))
hpnicfDot11APLimitEntry.setIndexNames((0,_Y,_a))
if mibBuilder.loadTexts:hpnicfDot11APLimitEntry.setStatus(_A)
class _HpnicfDot11APSsidNumLimit_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_HpnicfDot11APSsidNumLimit_Type.__name__=_D
_HpnicfDot11APSsidNumLimit_Object=MibTableColumn
hpnicfDot11APSsidNumLimit=_HpnicfDot11APSsidNumLimit_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,4,3,5,1,1),_HpnicfDot11APSsidNumLimit_Type())
hpnicfDot11APSsidNumLimit.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11APSsidNumLimit.setStatus(_A)
class _HpnicfDot11APUserCntLimit_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_HpnicfDot11APUserCntLimit_Type.__name__=_D
_HpnicfDot11APUserCntLimit_Object=MibTableColumn
hpnicfDot11APUserCntLimit=_HpnicfDot11APUserCntLimit_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,4,3,5,1,2),_HpnicfDot11APUserCntLimit_Type())
hpnicfDot11APUserCntLimit.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11APUserCntLimit.setStatus(_A)
class _HpnicfDot11APUserThreshold_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_HpnicfDot11APUserThreshold_Type.__name__=_D
_HpnicfDot11APUserThreshold_Object=MibTableColumn
hpnicfDot11APUserThreshold=_HpnicfDot11APUserThreshold_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,4,3,5,1,3),_HpnicfDot11APUserThreshold_Type())
hpnicfDot11APUserThreshold.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11APUserThreshold.setStatus(_A)
_HpnicfDot11APIfSetTable_Object=MibTable
hpnicfDot11APIfSetTable=_HpnicfDot11APIfSetTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,4,3,6))
if mibBuilder.loadTexts:hpnicfDot11APIfSetTable.setStatus(_A)
_HpnicfDot11APIfSetEntry_Object=MibTableRow
hpnicfDot11APIfSetEntry=_HpnicfDot11APIfSetEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,4,3,6,1))
hpnicfDot11APIfSetEntry.setIndexNames((0,_Y,_a),(0,_E,_AD))
if mibBuilder.loadTexts:hpnicfDot11APIfSetEntry.setStatus(_A)
_HpnicfDot11APSetIfIndex_Type=Integer32
_HpnicfDot11APSetIfIndex_Object=MibTableColumn
hpnicfDot11APSetIfIndex=_HpnicfDot11APSetIfIndex_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,4,3,6,1,1),_HpnicfDot11APSetIfIndex_Type())
hpnicfDot11APSetIfIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:hpnicfDot11APSetIfIndex.setStatus(_A)
_HpnicfDot11APIfAlias_Type=DisplayString
_HpnicfDot11APIfAlias_Object=MibTableColumn
hpnicfDot11APIfAlias=_HpnicfDot11APIfAlias_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,4,3,6,1,2),_HpnicfDot11APIfAlias_Type())
hpnicfDot11APIfAlias.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11APIfAlias.setStatus(_A)
_HpnicfDot11APServiceVlanTable_Object=MibTable
hpnicfDot11APServiceVlanTable=_HpnicfDot11APServiceVlanTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,4,3,7))
if mibBuilder.loadTexts:hpnicfDot11APServiceVlanTable.setStatus(_A)
_HpnicfDot11APServiceVlanEntry_Object=MibTableRow
hpnicfDot11APServiceVlanEntry=_HpnicfDot11APServiceVlanEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,4,3,7,1))
hpnicfDot11APServiceVlanEntry.setIndexNames((0,_E,_AE),(0,_E,_AF))
if mibBuilder.loadTexts:hpnicfDot11APServiceVlanEntry.setStatus(_A)
_HpnicfDot11APServiceVlanSerialID_Type=OctetString
_HpnicfDot11APServiceVlanSerialID_Object=MibTableColumn
hpnicfDot11APServiceVlanSerialID=_HpnicfDot11APServiceVlanSerialID_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,4,3,7,1,1),_HpnicfDot11APServiceVlanSerialID_Type())
hpnicfDot11APServiceVlanSerialID.setMaxAccess(_F)
if mibBuilder.loadTexts:hpnicfDot11APServiceVlanSerialID.setStatus(_A)
_HpnicfDot11APServiceVlanSPID_Type=HpnicfDot11ServicePolicyIDType
_HpnicfDot11APServiceVlanSPID_Object=MibTableColumn
hpnicfDot11APServiceVlanSPID=_HpnicfDot11APServiceVlanSPID_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,4,3,7,1,2),_HpnicfDot11APServiceVlanSPID_Type())
hpnicfDot11APServiceVlanSPID.setMaxAccess(_F)
if mibBuilder.loadTexts:hpnicfDot11APServiceVlanSPID.setStatus(_A)
class _HpnicfDot11APServiceVlanId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4094))
_HpnicfDot11APServiceVlanId_Type.__name__=_D
_HpnicfDot11APServiceVlanId_Object=MibTableColumn
hpnicfDot11APServiceVlanId=_HpnicfDot11APServiceVlanId_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,4,3,7,1,3),_HpnicfDot11APServiceVlanId_Type())
hpnicfDot11APServiceVlanId.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfDot11APServiceVlanId.setStatus(_A)
_HpnicfDot11APServiceVlanRowStatus_Type=RowStatus
_HpnicfDot11APServiceVlanRowStatus_Object=MibTableColumn
hpnicfDot11APServiceVlanRowStatus=_HpnicfDot11APServiceVlanRowStatus_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,4,3,7,1,4),_HpnicfDot11APServiceVlanRowStatus_Type())
hpnicfDot11APServiceVlanRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfDot11APServiceVlanRowStatus.setStatus(_A)
_HpnicfDot11RadioConfigTable_Object=MibTable
hpnicfDot11RadioConfigTable=_HpnicfDot11RadioConfigTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,4,3,8))
if mibBuilder.loadTexts:hpnicfDot11RadioConfigTable.setStatus(_A)
_HpnicfDot11RadioConfigEntry_Object=MibTableRow
hpnicfDot11RadioConfigEntry=_HpnicfDot11RadioConfigEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,4,3,8,1))
hpnicfDot11RadioConfigEntry.setIndexNames((0,_E,_AG),(0,_E,_AH))
if mibBuilder.loadTexts:hpnicfDot11RadioConfigEntry.setStatus(_A)
class _HpnicfDot11RCAPSerialID_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,127))
_HpnicfDot11RCAPSerialID_Type.__name__=_H
_HpnicfDot11RCAPSerialID_Object=MibTableColumn
hpnicfDot11RCAPSerialID=_HpnicfDot11RCAPSerialID_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,4,3,8,1,1),_HpnicfDot11RCAPSerialID_Type())
hpnicfDot11RCAPSerialID.setMaxAccess(_F)
if mibBuilder.loadTexts:hpnicfDot11RCAPSerialID.setStatus(_A)
_HpnicfDot11RCRadioID_Type=HpnicfDot11RadioScopeType
_HpnicfDot11RCRadioID_Object=MibTableColumn
hpnicfDot11RCRadioID=_HpnicfDot11RCRadioID_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,4,3,8,1,2),_HpnicfDot11RCRadioID_Type())
hpnicfDot11RCRadioID.setMaxAccess(_F)
if mibBuilder.loadTexts:hpnicfDot11RCRadioID.setStatus(_A)
_HpnicfDot11RCRadioType_Type=HpnicfDot11RadioType
_HpnicfDot11RCRadioType_Object=MibTableColumn
hpnicfDot11RCRadioType=_HpnicfDot11RCRadioType_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,4,3,8,1,3),_HpnicfDot11RCRadioType_Type())
hpnicfDot11RCRadioType.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11RCRadioType.setStatus(_A)
_HpnicfDot11RCChannel_Type=HpnicfDot11ChannelScopeType
_HpnicfDot11RCChannel_Object=MibTableColumn
hpnicfDot11RCChannel=_HpnicfDot11RCChannel_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,4,3,8,1,4),_HpnicfDot11RCChannel_Type())
hpnicfDot11RCChannel.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11RCChannel.setStatus(_A)
class _HpnicfDot11RCPreambleLen_Type(HpnicfDot11PreambleType):defaultValue=2
_HpnicfDot11RCPreambleLen_Type.__name__=_R
_HpnicfDot11RCPreambleLen_Object=MibTableColumn
hpnicfDot11RCPreambleLen=_HpnicfDot11RCPreambleLen_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,4,3,8,1,5),_HpnicfDot11RCPreambleLen_Type())
hpnicfDot11RCPreambleLen.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11RCPreambleLen.setStatus(_A)
_HpnicfDot11RCPwrAttValue_Type=Integer32
_HpnicfDot11RCPwrAttValue_Object=MibTableColumn
hpnicfDot11RCPwrAttValue=_HpnicfDot11RCPwrAttValue_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,4,3,8,1,6),_HpnicfDot11RCPwrAttValue_Type())
hpnicfDot11RCPwrAttValue.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11RCPwrAttValue.setStatus(_A)
_HpnicfDot11RCApPowerLevel_Type=HpnicfDot11TxPwrLevelScopeType
_HpnicfDot11RCApPowerLevel_Object=MibTableColumn
hpnicfDot11RCApPowerLevel=_HpnicfDot11RCApPowerLevel_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,4,3,8,1,7),_HpnicfDot11RCApPowerLevel_Type())
hpnicfDot11RCApPowerLevel.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11RCApPowerLevel.setStatus(_A)
if mibBuilder.loadTexts:hpnicfDot11RCApPowerLevel.setUnits(_O)
_HpnicfDot11RCDynamicChlState_Type=TruthValue
_HpnicfDot11RCDynamicChlState_Object=MibTableColumn
hpnicfDot11RCDynamicChlState=_HpnicfDot11RCDynamicChlState_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,4,3,8,1,8),_HpnicfDot11RCDynamicChlState_Type())
hpnicfDot11RCDynamicChlState.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11RCDynamicChlState.setStatus(_A)
_HpnicfDot11RCDynamicPowerState_Type=TruthValue
_HpnicfDot11RCDynamicPowerState_Object=MibTableColumn
hpnicfDot11RCDynamicPowerState=_HpnicfDot11RCDynamicPowerState_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,4,3,8,1,9),_HpnicfDot11RCDynamicPowerState_Type())
hpnicfDot11RCDynamicPowerState.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11RCDynamicPowerState.setStatus(_A)
_HpnicfDot11RCRadioStatus_Type=TruthValue
_HpnicfDot11RCRadioStatus_Object=MibTableColumn
hpnicfDot11RCRadioStatus=_HpnicfDot11RCRadioStatus_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,4,3,8,1,10),_HpnicfDot11RCRadioStatus_Type())
hpnicfDot11RCRadioStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11RCRadioStatus.setStatus(_A)
class _HpnicfDot11RCRadioRate_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_HpnicfDot11RCRadioRate_Type.__name__=_H
_HpnicfDot11RCRadioRate_Object=MibTableColumn
hpnicfDot11RCRadioRate=_HpnicfDot11RCRadioRate_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,4,3,8,1,11),_HpnicfDot11RCRadioRate_Type())
hpnicfDot11RCRadioRate.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11RCRadioRate.setStatus(_A)
_HpnicfDot11RCPwrAdjustStepLength_Type=Integer32
_HpnicfDot11RCPwrAdjustStepLength_Object=MibTableColumn
hpnicfDot11RCPwrAdjustStepLength=_HpnicfDot11RCPwrAdjustStepLength_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,4,3,8,1,12),_HpnicfDot11RCPwrAdjustStepLength_Type())
hpnicfDot11RCPwrAdjustStepLength.setMaxAccess(_I)
if mibBuilder.loadTexts:hpnicfDot11RCPwrAdjustStepLength.setStatus(_A)
_HpnicfDot11RCRadioType2_Type=HpnicfDot11RadioType2
_HpnicfDot11RCRadioType2_Object=MibTableColumn
hpnicfDot11RCRadioType2=_HpnicfDot11RCRadioType2_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,4,3,8,1,13),_HpnicfDot11RCRadioType2_Type())
hpnicfDot11RCRadioType2.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11RCRadioType2.setStatus(_A)
class _HpnicfDot11RCPreambleLenCM_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('long',0),('short',1)))
_HpnicfDot11RCPreambleLenCM_Type.__name__=_D
_HpnicfDot11RCPreambleLenCM_Object=MibTableColumn
hpnicfDot11RCPreambleLenCM=_HpnicfDot11RCPreambleLenCM_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,4,3,8,1,14),_HpnicfDot11RCPreambleLenCM_Type())
hpnicfDot11RCPreambleLenCM.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11RCPreambleLenCM.setStatus(_A)
class _HpnicfDot11RCDynamicChlStateCM_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_P,0),(_Q,1)))
_HpnicfDot11RCDynamicChlStateCM_Type.__name__=_D
_HpnicfDot11RCDynamicChlStateCM_Object=MibTableColumn
hpnicfDot11RCDynamicChlStateCM=_HpnicfDot11RCDynamicChlStateCM_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,4,3,8,1,15),_HpnicfDot11RCDynamicChlStateCM_Type())
hpnicfDot11RCDynamicChlStateCM.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11RCDynamicChlStateCM.setStatus(_A)
class _HpnicfDot11RCRadioStatusCM_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('up',1),('down',2),('testing',3)))
_HpnicfDot11RCRadioStatusCM_Type.__name__=_D
_HpnicfDot11RCRadioStatusCM_Object=MibTableColumn
hpnicfDot11RCRadioStatusCM=_HpnicfDot11RCRadioStatusCM_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,4,3,8,1,16),_HpnicfDot11RCRadioStatusCM_Type())
hpnicfDot11RCRadioStatusCM.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11RCRadioStatusCM.setStatus(_A)
class _HpnicfDot11RCRadioRateCM_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_HpnicfDot11RCRadioRateCM_Type.__name__=_H
_HpnicfDot11RCRadioRateCM_Object=MibTableColumn
hpnicfDot11RCRadioRateCM=_HpnicfDot11RCRadioRateCM_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,4,3,8,1,17),_HpnicfDot11RCRadioRateCM_Type())
hpnicfDot11RCRadioRateCM.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11RCRadioRateCM.setStatus(_A)
_HpnicfDot11RCDynamicPowerStateCM_Type=HpnicfDot11TruthValueCM
_HpnicfDot11RCDynamicPowerStateCM_Object=MibTableColumn
hpnicfDot11RCDynamicPowerStateCM=_HpnicfDot11RCDynamicPowerStateCM_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,4,3,8,1,18),_HpnicfDot11RCDynamicPowerStateCM_Type())
hpnicfDot11RCDynamicPowerStateCM.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11RCDynamicPowerStateCM.setStatus(_A)
class _HpnicfDot11RCRssiThresholdCM_Type(Integer32):defaultValue=1
_HpnicfDot11RCRssiThresholdCM_Type.__name__=_D
_HpnicfDot11RCRssiThresholdCM_Object=MibTableColumn
hpnicfDot11RCRssiThresholdCM=_HpnicfDot11RCRssiThresholdCM_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,4,3,8,1,19),_HpnicfDot11RCRssiThresholdCM_Type())
hpnicfDot11RCRssiThresholdCM.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11RCRssiThresholdCM.setStatus(_A)
if mibBuilder.loadTexts:hpnicfDot11RCRssiThresholdCM.setUnits('dBm')
_HpnicfDot11RadioSSIDCfgTable_Object=MibTable
hpnicfDot11RadioSSIDCfgTable=_HpnicfDot11RadioSSIDCfgTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,4,3,9))
if mibBuilder.loadTexts:hpnicfDot11RadioSSIDCfgTable.setStatus(_A)
_HpnicfDot11RadioSSIDCfgEntry_Object=MibTableRow
hpnicfDot11RadioSSIDCfgEntry=_HpnicfDot11RadioSSIDCfgEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,4,3,9,1))
hpnicfDot11RadioSSIDCfgEntry.setIndexNames((0,_E,_AI),(0,_E,_AJ),(0,_E,_AK))
if mibBuilder.loadTexts:hpnicfDot11RadioSSIDCfgEntry.setStatus(_A)
_HpnicfDot11RadioSSIDSerialID_Type=HpnicfDot11ObjectIDType
_HpnicfDot11RadioSSIDSerialID_Object=MibTableColumn
hpnicfDot11RadioSSIDSerialID=_HpnicfDot11RadioSSIDSerialID_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,4,3,9,1,1),_HpnicfDot11RadioSSIDSerialID_Type())
hpnicfDot11RadioSSIDSerialID.setMaxAccess(_F)
if mibBuilder.loadTexts:hpnicfDot11RadioSSIDSerialID.setStatus(_A)
_HpnicfDot11RadioSSIDRadioID_Type=HpnicfDot11RadioScopeType
_HpnicfDot11RadioSSIDRadioID_Object=MibTableColumn
hpnicfDot11RadioSSIDRadioID=_HpnicfDot11RadioSSIDRadioID_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,4,3,9,1,2),_HpnicfDot11RadioSSIDRadioID_Type())
hpnicfDot11RadioSSIDRadioID.setMaxAccess(_F)
if mibBuilder.loadTexts:hpnicfDot11RadioSSIDRadioID.setStatus(_A)
_HpnicfDot11RadioSSIDWLANID_Type=Integer32
_HpnicfDot11RadioSSIDWLANID_Object=MibTableColumn
hpnicfDot11RadioSSIDWLANID=_HpnicfDot11RadioSSIDWLANID_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,4,3,9,1,3),_HpnicfDot11RadioSSIDWLANID_Type())
hpnicfDot11RadioSSIDWLANID.setMaxAccess(_F)
if mibBuilder.loadTexts:hpnicfDot11RadioSSIDWLANID.setStatus(_A)
_HpnicfDot11RadioSSIDIndex_Type=HpnicfDot11ServicePolicyIDType
_HpnicfDot11RadioSSIDIndex_Object=MibTableColumn
hpnicfDot11RadioSSIDIndex=_HpnicfDot11RadioSSIDIndex_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,4,3,9,1,4),_HpnicfDot11RadioSSIDIndex_Type())
hpnicfDot11RadioSSIDIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfDot11RadioSSIDIndex.setStatus(_A)
_HpnicfDot11RadioBSSID_Type=MacAddress
_HpnicfDot11RadioBSSID_Object=MibTableColumn
hpnicfDot11RadioBSSID=_HpnicfDot11RadioBSSID_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,4,3,9,1,5),_HpnicfDot11RadioBSSID_Type())
hpnicfDot11RadioBSSID.setMaxAccess(_I)
if mibBuilder.loadTexts:hpnicfDot11RadioBSSID.setStatus(_A)
_HpnicfDot11RadioSSIDRowStatus_Type=RowStatus
_HpnicfDot11RadioSSIDRowStatus_Object=MibTableColumn
hpnicfDot11RadioSSIDRowStatus=_HpnicfDot11RadioSSIDRowStatus_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,4,3,9,1,6),_HpnicfDot11RadioSSIDRowStatus_Type())
hpnicfDot11RadioSSIDRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfDot11RadioSSIDRowStatus.setStatus(_A)
_HpnicfDot11APSerialIDTable_Object=MibTable
hpnicfDot11APSerialIDTable=_HpnicfDot11APSerialIDTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,4,3,10))
if mibBuilder.loadTexts:hpnicfDot11APSerialIDTable.setStatus(_A)
_HpnicfDot11APSerialIDEntry_Object=MibTableRow
hpnicfDot11APSerialIDEntry=_HpnicfDot11APSerialIDEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,4,3,10,1))
hpnicfDot11APSerialIDEntry.setIndexNames((0,_E,_X))
if mibBuilder.loadTexts:hpnicfDot11APSerialIDEntry.setStatus(_A)
_HpnicfDot11SIDAPSerialID_Type=OctetString
_HpnicfDot11SIDAPSerialID_Object=MibTableColumn
hpnicfDot11SIDAPSerialID=_HpnicfDot11SIDAPSerialID_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,4,3,10,1,1),_HpnicfDot11SIDAPSerialID_Type())
hpnicfDot11SIDAPSerialID.setMaxAccess(_F)
if mibBuilder.loadTexts:hpnicfDot11SIDAPSerialID.setStatus(_A)
class _HpnicfDot11SIDAPWorkMode_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_L,1),(_U,2),(_c,3)))
_HpnicfDot11SIDAPWorkMode_Type.__name__=_D
_HpnicfDot11SIDAPWorkMode_Object=MibTableColumn
hpnicfDot11SIDAPWorkMode=_HpnicfDot11SIDAPWorkMode_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,4,3,10,1,2),_HpnicfDot11SIDAPWorkMode_Type())
hpnicfDot11SIDAPWorkMode.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfDot11SIDAPWorkMode.setStatus(_A)
class _HpnicfDot11SIDAPGetIPMethod_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_AC,1),('static',2)))
_HpnicfDot11SIDAPGetIPMethod_Type.__name__=_D
_HpnicfDot11SIDAPGetIPMethod_Object=MibTableColumn
hpnicfDot11SIDAPGetIPMethod=_HpnicfDot11SIDAPGetIPMethod_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,4,3,10,1,3),_HpnicfDot11SIDAPGetIPMethod_Type())
hpnicfDot11SIDAPGetIPMethod.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfDot11SIDAPGetIPMethod.setStatus(_A)
_HpnicfDot11SIDAPTemplateName_Type=OctetString
_HpnicfDot11SIDAPTemplateName_Object=MibTableColumn
hpnicfDot11SIDAPTemplateName=_HpnicfDot11SIDAPTemplateName_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,4,3,10,1,4),_HpnicfDot11SIDAPTemplateName_Type())
hpnicfDot11SIDAPTemplateName.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfDot11SIDAPTemplateName.setStatus(_A)
_HpnicfDot11SIDModelAlias_Type=OctetString
_HpnicfDot11SIDModelAlias_Object=MibTableColumn
hpnicfDot11SIDModelAlias=_HpnicfDot11SIDModelAlias_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,4,3,10,1,5),_HpnicfDot11SIDModelAlias_Type())
hpnicfDot11SIDModelAlias.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfDot11SIDModelAlias.setStatus(_A)
_HpnicfDot11SIDAPDescription_Type=OctetString
_HpnicfDot11SIDAPDescription_Object=MibTableColumn
hpnicfDot11SIDAPDescription=_HpnicfDot11SIDAPDescription_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,4,3,10,1,6),_HpnicfDot11SIDAPDescription_Type())
hpnicfDot11SIDAPDescription.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfDot11SIDAPDescription.setStatus(_A)
_HpnicfDot11SIDRowStatus_Type=RowStatus
_HpnicfDot11SIDRowStatus_Object=MibTableColumn
hpnicfDot11SIDRowStatus=_HpnicfDot11SIDRowStatus_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,4,3,10,1,7),_HpnicfDot11SIDRowStatus_Type())
hpnicfDot11SIDRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfDot11SIDRowStatus.setStatus(_A)
_HpnicfDot11SIDAPName_Type=OctetString
_HpnicfDot11SIDAPName_Object=MibTableColumn
hpnicfDot11SIDAPName=_HpnicfDot11SIDAPName_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,4,3,10,1,8),_HpnicfDot11SIDAPName_Type())
hpnicfDot11SIDAPName.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfDot11SIDAPName.setStatus(_A)
_HpnicfDot11SIDStatisInterv_Type=Integer32
_HpnicfDot11SIDStatisInterv_Object=MibTableColumn
hpnicfDot11SIDStatisInterv=_HpnicfDot11SIDStatisInterv_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,4,3,10,1,9),_HpnicfDot11SIDStatisInterv_Type())
hpnicfDot11SIDStatisInterv.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfDot11SIDStatisInterv.setStatus(_A)
if mibBuilder.loadTexts:hpnicfDot11SIDStatisInterv.setUnits(_J)
class _HpnicfDot11SIDAPBroadcastProbeReply_Type(TruthValue):defaultValue=1
_HpnicfDot11SIDAPBroadcastProbeReply_Type.__name__=_G
_HpnicfDot11SIDAPBroadcastProbeReply_Object=MibTableColumn
hpnicfDot11SIDAPBroadcastProbeReply=_HpnicfDot11SIDAPBroadcastProbeReply_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,4,3,10,1,10),_HpnicfDot11SIDAPBroadcastProbeReply_Type())
hpnicfDot11SIDAPBroadcastProbeReply.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfDot11SIDAPBroadcastProbeReply.setStatus(_A)
_HpnicfDot11SIDAPStaIdleTimerInterv_Type=Integer32
_HpnicfDot11SIDAPStaIdleTimerInterv_Object=MibTableColumn
hpnicfDot11SIDAPStaIdleTimerInterv=_HpnicfDot11SIDAPStaIdleTimerInterv_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,4,3,10,1,11),_HpnicfDot11SIDAPStaIdleTimerInterv_Type())
hpnicfDot11SIDAPStaIdleTimerInterv.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfDot11SIDAPStaIdleTimerInterv.setStatus(_A)
if mibBuilder.loadTexts:hpnicfDot11SIDAPStaIdleTimerInterv.setUnits(_J)
_HpnicfDot11SIDStaKeepAliveTimerInterv_Type=Integer32
_HpnicfDot11SIDStaKeepAliveTimerInterv_Object=MibTableColumn
hpnicfDot11SIDStaKeepAliveTimerInterv=_HpnicfDot11SIDStaKeepAliveTimerInterv_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,4,3,10,1,12),_HpnicfDot11SIDStaKeepAliveTimerInterv_Type())
hpnicfDot11SIDStaKeepAliveTimerInterv.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfDot11SIDStaKeepAliveTimerInterv.setStatus(_A)
if mibBuilder.loadTexts:hpnicfDot11SIDStaKeepAliveTimerInterv.setUnits(_J)
_HpnicfDot11SIDAPCir_Type=Integer32
_HpnicfDot11SIDAPCir_Object=MibTableColumn
hpnicfDot11SIDAPCir=_HpnicfDot11SIDAPCir_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,4,3,10,1,13),_HpnicfDot11SIDAPCir_Type())
hpnicfDot11SIDAPCir.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfDot11SIDAPCir.setStatus(_A)
if mibBuilder.loadTexts:hpnicfDot11SIDAPCir.setUnits(_M)
_HpnicfDot11SIDAPCbs_Type=Integer32
_HpnicfDot11SIDAPCbs_Object=MibTableColumn
hpnicfDot11SIDAPCbs=_HpnicfDot11SIDAPCbs_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,4,3,10,1,14),_HpnicfDot11SIDAPCbs_Type())
hpnicfDot11SIDAPCbs.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfDot11SIDAPCbs.setStatus(_A)
if mibBuilder.loadTexts:hpnicfDot11SIDAPCbs.setUnits('Bytes')
class _HpnicfDot11SIDAPPriorityLevel_Type(Integer32):defaultValue=4;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_HpnicfDot11SIDAPPriorityLevel_Type.__name__=_D
_HpnicfDot11SIDAPPriorityLevel_Object=MibTableColumn
hpnicfDot11SIDAPPriorityLevel=_HpnicfDot11SIDAPPriorityLevel_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,4,3,10,1,15),_HpnicfDot11SIDAPPriorityLevel_Type())
hpnicfDot11SIDAPPriorityLevel.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfDot11SIDAPPriorityLevel.setStatus(_A)
_HpnicfDot11SIDAPElementID_Type=Integer32
_HpnicfDot11SIDAPElementID_Object=MibTableColumn
hpnicfDot11SIDAPElementID=_HpnicfDot11SIDAPElementID_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,4,3,10,1,16),_HpnicfDot11SIDAPElementID_Type())
hpnicfDot11SIDAPElementID.setMaxAccess(_I)
if mibBuilder.loadTexts:hpnicfDot11SIDAPElementID.setStatus(_A)
class _HpnicfDot11SIDAPDevDetectEnable_Type(TruthValue):defaultValue=2
_HpnicfDot11SIDAPDevDetectEnable_Type.__name__=_G
_HpnicfDot11SIDAPDevDetectEnable_Object=MibTableColumn
hpnicfDot11SIDAPDevDetectEnable=_HpnicfDot11SIDAPDevDetectEnable_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,4,3,10,1,17),_HpnicfDot11SIDAPDevDetectEnable_Type())
hpnicfDot11SIDAPDevDetectEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfDot11SIDAPDevDetectEnable.setStatus(_A)
class _HpnicfDot11SIDAPStatisIntervMode_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_L,1),('realtime',2)))
_HpnicfDot11SIDAPStatisIntervMode_Type.__name__=_D
_HpnicfDot11SIDAPStatisIntervMode_Object=MibTableColumn
hpnicfDot11SIDAPStatisIntervMode=_HpnicfDot11SIDAPStatisIntervMode_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,4,3,10,1,18),_HpnicfDot11SIDAPStatisIntervMode_Type())
hpnicfDot11SIDAPStatisIntervMode.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfDot11SIDAPStatisIntervMode.setStatus(_A)
class _HpnicfDot11SIDAPWorkModeCM_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_L,0),(_U,1),('semimonitor',2)))
_HpnicfDot11SIDAPWorkModeCM_Type.__name__=_D
_HpnicfDot11SIDAPWorkModeCM_Object=MibTableColumn
hpnicfDot11SIDAPWorkModeCM=_HpnicfDot11SIDAPWorkModeCM_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,4,3,10,1,19),_HpnicfDot11SIDAPWorkModeCM_Type())
hpnicfDot11SIDAPWorkModeCM.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfDot11SIDAPWorkModeCM.setStatus(_A)
_HpnicfDot11APSTVlanTable_Object=MibTable
hpnicfDot11APSTVlanTable=_HpnicfDot11APSTVlanTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,4,3,11))
if mibBuilder.loadTexts:hpnicfDot11APSTVlanTable.setStatus(_A)
_HpnicfDot11APSTVlanEntry_Object=MibTableRow
hpnicfDot11APSTVlanEntry=_HpnicfDot11APSTVlanEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,4,3,11,1))
hpnicfDot11APSTVlanEntry.setIndexNames((0,_E,_X),(0,_E,_W),(0,_E,_m))
if mibBuilder.loadTexts:hpnicfDot11APSTVlanEntry.setStatus(_A)
class _HpnicfDot11CfgSTVLANID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4094))
_HpnicfDot11CfgSTVLANID_Type.__name__=_D
_HpnicfDot11CfgSTVLANID_Object=MibTableColumn
hpnicfDot11CfgSTVLANID=_HpnicfDot11CfgSTVLANID_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,4,3,11,1,1),_HpnicfDot11CfgSTVLANID_Type())
hpnicfDot11CfgSTVLANID.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfDot11CfgSTVLANID.setStatus(_A)
class _HpnicfDot11CfgSTNASPortID_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,127))
_HpnicfDot11CfgSTNASPortID_Type.__name__=_H
_HpnicfDot11CfgSTNASPortID_Object=MibTableColumn
hpnicfDot11CfgSTNASPortID=_HpnicfDot11CfgSTNASPortID_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,4,3,11,1,2),_HpnicfDot11CfgSTNASPortID_Type())
hpnicfDot11CfgSTNASPortID.setMaxAccess(_I)
if mibBuilder.loadTexts:hpnicfDot11CfgSTNASPortID.setStatus(_A)
_HpnicfDot11CfgServiceSetRowStatus_Type=RowStatus
_HpnicfDot11CfgServiceSetRowStatus_Object=MibTableColumn
hpnicfDot11CfgServiceSetRowStatus=_HpnicfDot11CfgServiceSetRowStatus_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,4,3,11,1,3),_HpnicfDot11CfgServiceSetRowStatus_Type())
hpnicfDot11CfgServiceSetRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfDot11CfgServiceSetRowStatus.setStatus(_A)
class _HpnicfDot11CfgSTNASID_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,127))
_HpnicfDot11CfgSTNASID_Type.__name__=_H
_HpnicfDot11CfgSTNASID_Object=MibTableColumn
hpnicfDot11CfgSTNASID=_HpnicfDot11CfgSTNASID_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,4,3,11,1,4),_HpnicfDot11CfgSTNASID_Type())
hpnicfDot11CfgSTNASID.setMaxAccess(_I)
if mibBuilder.loadTexts:hpnicfDot11CfgSTNASID.setStatus(_A)
_HpnicfDot11RadioIntfConfigGroup_ObjectIdentity=ObjectIdentity
hpnicfDot11RadioIntfConfigGroup=_HpnicfDot11RadioIntfConfigGroup_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,75,4,4))
_HpnicfDot11RadioIntfConfigTable_Object=MibTable
hpnicfDot11RadioIntfConfigTable=_HpnicfDot11RadioIntfConfigTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,4,4,1))
if mibBuilder.loadTexts:hpnicfDot11RadioIntfConfigTable.setStatus(_A)
_HpnicfDot11RadioIntfConfigEntry_Object=MibTableRow
hpnicfDot11RadioIntfConfigEntry=_HpnicfDot11RadioIntfConfigEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,4,4,1,1))
hpnicfDot11RadioIntfConfigEntry.setIndexNames((0,_E,_n))
if mibBuilder.loadTexts:hpnicfDot11RadioIntfConfigEntry.setStatus(_A)
_HpnicfDot11RadioIfIdx_Type=Integer32
_HpnicfDot11RadioIfIdx_Object=MibTableColumn
hpnicfDot11RadioIfIdx=_HpnicfDot11RadioIfIdx_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,4,4,1,1,1),_HpnicfDot11RadioIfIdx_Type())
hpnicfDot11RadioIfIdx.setMaxAccess(_F)
if mibBuilder.loadTexts:hpnicfDot11RadioIfIdx.setStatus(_A)
class _HpnicfDot11RadioCfgBeaconIntvl_Type(Integer32):defaultValue=100
_HpnicfDot11RadioCfgBeaconIntvl_Type.__name__=_D
_HpnicfDot11RadioCfgBeaconIntvl_Object=MibTableColumn
hpnicfDot11RadioCfgBeaconIntvl=_HpnicfDot11RadioCfgBeaconIntvl_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,4,4,1,1,2),_HpnicfDot11RadioCfgBeaconIntvl_Type())
hpnicfDot11RadioCfgBeaconIntvl.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11RadioCfgBeaconIntvl.setStatus(_A)
if mibBuilder.loadTexts:hpnicfDot11RadioCfgBeaconIntvl.setUnits('TU')
class _HpnicfDot11RadioCfgDtimIntvl_Type(Integer32):defaultValue=1
_HpnicfDot11RadioCfgDtimIntvl_Type.__name__=_D
_HpnicfDot11RadioCfgDtimIntvl_Object=MibTableColumn
hpnicfDot11RadioCfgDtimIntvl=_HpnicfDot11RadioCfgDtimIntvl_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,4,4,1,1,3),_HpnicfDot11RadioCfgDtimIntvl_Type())
hpnicfDot11RadioCfgDtimIntvl.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11RadioCfgDtimIntvl.setStatus(_A)
class _HpnicfDot11RadioCfgRtsThreshold_Type(Integer32):defaultValue=2346
_HpnicfDot11RadioCfgRtsThreshold_Type.__name__=_D
_HpnicfDot11RadioCfgRtsThreshold_Object=MibTableColumn
hpnicfDot11RadioCfgRtsThreshold=_HpnicfDot11RadioCfgRtsThreshold_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,4,4,1,1,4),_HpnicfDot11RadioCfgRtsThreshold_Type())
hpnicfDot11RadioCfgRtsThreshold.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11RadioCfgRtsThreshold.setStatus(_A)
if mibBuilder.loadTexts:hpnicfDot11RadioCfgRtsThreshold.setUnits('Byte')
class _HpnicfDot11RadioCfgFragThreshold_Type(Integer32):defaultValue=2346
_HpnicfDot11RadioCfgFragThreshold_Type.__name__=_D
_HpnicfDot11RadioCfgFragThreshold_Object=MibTableColumn
hpnicfDot11RadioCfgFragThreshold=_HpnicfDot11RadioCfgFragThreshold_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,4,4,1,1,5),_HpnicfDot11RadioCfgFragThreshold_Type())
hpnicfDot11RadioCfgFragThreshold.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11RadioCfgFragThreshold.setStatus(_A)
if mibBuilder.loadTexts:hpnicfDot11RadioCfgFragThreshold.setUnits('Byte')
class _HpnicfDot11RadioCfgShtRetryThld_Type(Integer32):defaultValue=5
_HpnicfDot11RadioCfgShtRetryThld_Type.__name__=_D
_HpnicfDot11RadioCfgShtRetryThld_Object=MibTableColumn
hpnicfDot11RadioCfgShtRetryThld=_HpnicfDot11RadioCfgShtRetryThld_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,4,4,1,1,6),_HpnicfDot11RadioCfgShtRetryThld_Type())
hpnicfDot11RadioCfgShtRetryThld.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11RadioCfgShtRetryThld.setStatus(_A)
class _HpnicfDot11RadioCfglongRtrThld_Type(Integer32):defaultValue=5
_HpnicfDot11RadioCfglongRtrThld_Type.__name__=_D
_HpnicfDot11RadioCfglongRtrThld_Object=MibTableColumn
hpnicfDot11RadioCfglongRtrThld=_HpnicfDot11RadioCfglongRtrThld_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,4,4,1,1,7),_HpnicfDot11RadioCfglongRtrThld_Type())
hpnicfDot11RadioCfglongRtrThld.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11RadioCfglongRtrThld.setStatus(_A)
class _HpnicfDot11RadioCfgMaxRxLifetime_Type(Unsigned32):defaultValue=2000
_HpnicfDot11RadioCfgMaxRxLifetime_Type.__name__=_K
_HpnicfDot11RadioCfgMaxRxLifetime_Object=MibTableColumn
hpnicfDot11RadioCfgMaxRxLifetime=_HpnicfDot11RadioCfgMaxRxLifetime_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,4,4,1,1,8),_HpnicfDot11RadioCfgMaxRxLifetime_Type())
hpnicfDot11RadioCfgMaxRxLifetime.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11RadioCfgMaxRxLifetime.setStatus(_A)
if mibBuilder.loadTexts:hpnicfDot11RadioCfgMaxRxLifetime.setUnits(_z)
_HpnicfDot11RadioCfgType_Type=HpnicfDot11RadioType
_HpnicfDot11RadioCfgType_Object=MibTableColumn
hpnicfDot11RadioCfgType=_HpnicfDot11RadioCfgType_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,4,4,1,1,9),_HpnicfDot11RadioCfgType_Type())
hpnicfDot11RadioCfgType.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11RadioCfgType.setStatus(_A)
class _HpnicfDot11RadioCfgChannel_Type(HpnicfDot11ChannelScopeType):defaultValue=1
_HpnicfDot11RadioCfgChannel_Type.__name__=_r
_HpnicfDot11RadioCfgChannel_Object=MibTableColumn
hpnicfDot11RadioCfgChannel=_HpnicfDot11RadioCfgChannel_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,4,4,1,1,10),_HpnicfDot11RadioCfgChannel_Type())
hpnicfDot11RadioCfgChannel.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11RadioCfgChannel.setStatus(_A)
_HpnicfDot11RadioCfgMaxTxPwrLvl_Type=HpnicfDot11TxPwrLevelScopeType
_HpnicfDot11RadioCfgMaxTxPwrLvl_Object=MibTableColumn
hpnicfDot11RadioCfgMaxTxPwrLvl=_HpnicfDot11RadioCfgMaxTxPwrLvl_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,4,4,1,1,11),_HpnicfDot11RadioCfgMaxTxPwrLvl_Type())
hpnicfDot11RadioCfgMaxTxPwrLvl.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11RadioCfgMaxTxPwrLvl.setStatus(_A)
if mibBuilder.loadTexts:hpnicfDot11RadioCfgMaxTxPwrLvl.setUnits(_O)
class _HpnicfDot11RadioCfgPreambleLen_Type(HpnicfDot11PreambleType):defaultValue=2
_HpnicfDot11RadioCfgPreambleLen_Type.__name__=_R
_HpnicfDot11RadioCfgPreambleLen_Object=MibTableColumn
hpnicfDot11RadioCfgPreambleLen=_HpnicfDot11RadioCfgPreambleLen_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,4,4,1,1,12),_HpnicfDot11RadioCfgPreambleLen_Type())
hpnicfDot11RadioCfgPreambleLen.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11RadioCfgPreambleLen.setStatus(_A)
_HpnicfDot11RadioCfgWorkMode_Type=HpnicfDot11WorkMode
_HpnicfDot11RadioCfgWorkMode_Object=MibTableColumn
hpnicfDot11RadioCfgWorkMode=_HpnicfDot11RadioCfgWorkMode_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,4,4,1,1,13),_HpnicfDot11RadioCfgWorkMode_Type())
hpnicfDot11RadioCfgWorkMode.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11RadioCfgWorkMode.setStatus(_A)
class _HpnicfDot11RadioCfgOnly11gEnable_Type(TruthValue):defaultValue=2
_HpnicfDot11RadioCfgOnly11gEnable_Type.__name__=_G
_HpnicfDot11RadioCfgOnly11gEnable_Object=MibTableColumn
hpnicfDot11RadioCfgOnly11gEnable=_HpnicfDot11RadioCfgOnly11gEnable_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,4,4,1,1,14),_HpnicfDot11RadioCfgOnly11gEnable_Type())
hpnicfDot11RadioCfgOnly11gEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11RadioCfgOnly11gEnable.setStatus(_A)
_HpnicfDot11RadioCfgType2_Type=HpnicfDot11RadioType2
_HpnicfDot11RadioCfgType2_Object=MibTableColumn
hpnicfDot11RadioCfgType2=_HpnicfDot11RadioCfgType2_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,4,4,1,1,15),_HpnicfDot11RadioCfgType2_Type())
hpnicfDot11RadioCfgType2.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11RadioCfgType2.setStatus(_A)
class _HpnicfDot11RadioCfgRssithresholdCM_Type(Integer32):defaultValue=1
_HpnicfDot11RadioCfgRssithresholdCM_Type.__name__=_D
_HpnicfDot11RadioCfgRssithresholdCM_Object=MibTableColumn
hpnicfDot11RadioCfgRssithresholdCM=_HpnicfDot11RadioCfgRssithresholdCM_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,4,4,1,1,16),_HpnicfDot11RadioCfgRssithresholdCM_Type())
hpnicfDot11RadioCfgRssithresholdCM.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11RadioCfgRssithresholdCM.setStatus(_A)
if mibBuilder.loadTexts:hpnicfDot11RadioCfgRssithresholdCM.setUnits('dBm')
_HpnicfDot11RadioIntfBindTable_Object=MibTable
hpnicfDot11RadioIntfBindTable=_HpnicfDot11RadioIntfBindTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,4,4,2))
if mibBuilder.loadTexts:hpnicfDot11RadioIntfBindTable.setStatus(_A)
_HpnicfDot11RadioIntfBindEntry_Object=MibTableRow
hpnicfDot11RadioIntfBindEntry=_HpnicfDot11RadioIntfBindEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,4,4,2,1))
hpnicfDot11RadioIntfBindEntry.setIndexNames((0,_E,_n),(0,_E,_AL))
if mibBuilder.loadTexts:hpnicfDot11RadioIntfBindEntry.setStatus(_A)
_HpnicfDot11RadioIntfBindSvcPlcyID_Type=HpnicfDot11ServicePolicyIDType
_HpnicfDot11RadioIntfBindSvcPlcyID_Object=MibTableColumn
hpnicfDot11RadioIntfBindSvcPlcyID=_HpnicfDot11RadioIntfBindSvcPlcyID_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,4,4,2,1,1),_HpnicfDot11RadioIntfBindSvcPlcyID_Type())
hpnicfDot11RadioIntfBindSvcPlcyID.setMaxAccess(_F)
if mibBuilder.loadTexts:hpnicfDot11RadioIntfBindSvcPlcyID.setStatus(_A)
_HpnicfDot11RadioIntfBindIfIdx_Type=Unsigned32
_HpnicfDot11RadioIntfBindIfIdx_Object=MibTableColumn
hpnicfDot11RadioIntfBindIfIdx=_HpnicfDot11RadioIntfBindIfIdx_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,4,4,2,1,2),_HpnicfDot11RadioIntfBindIfIdx_Type())
hpnicfDot11RadioIntfBindIfIdx.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfDot11RadioIntfBindIfIdx.setStatus(_A)
_HpnicfDot11RadioIntfBindRowStatus_Type=RowStatus
_HpnicfDot11RadioIntfBindRowStatus_Object=MibTableColumn
hpnicfDot11RadioIntfBindRowStatus=_HpnicfDot11RadioIntfBindRowStatus_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,4,4,2,1,3),_HpnicfDot11RadioIntfBindRowStatus_Type())
hpnicfDot11RadioIntfBindRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfDot11RadioIntfBindRowStatus.setStatus(_A)
_HpnicfDot11DataRateConfigGroup_ObjectIdentity=ObjectIdentity
hpnicfDot11DataRateConfigGroup=_HpnicfDot11DataRateConfigGroup_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,75,4,5))
_HpnicfDot11DataRateConfigTable_Object=MibTable
hpnicfDot11DataRateConfigTable=_HpnicfDot11DataRateConfigTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,4,5,1))
if mibBuilder.loadTexts:hpnicfDot11DataRateConfigTable.setStatus(_A)
_HpnicfDot11DataRateConfigEntry_Object=MibTableRow
hpnicfDot11DataRateConfigEntry=_HpnicfDot11DataRateConfigEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,4,5,1,1))
hpnicfDot11DataRateConfigEntry.setIndexNames((0,_E,_AM))
if mibBuilder.loadTexts:hpnicfDot11DataRateConfigEntry.setStatus(_A)
_HpnicfDot11RadioTypeID_Type=HpnicfDot11RadioType
_HpnicfDot11RadioTypeID_Object=MibTableColumn
hpnicfDot11RadioTypeID=_HpnicfDot11RadioTypeID_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,4,5,1,1,1),_HpnicfDot11RadioTypeID_Type())
hpnicfDot11RadioTypeID.setMaxAccess(_F)
if mibBuilder.loadTexts:hpnicfDot11RadioTypeID.setStatus(_A)
class _HpnicfDot11SupportedRateSet_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_HpnicfDot11SupportedRateSet_Type.__name__=_H
_HpnicfDot11SupportedRateSet_Object=MibTableColumn
hpnicfDot11SupportedRateSet=_HpnicfDot11SupportedRateSet_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,4,5,1,1,2),_HpnicfDot11SupportedRateSet_Type())
hpnicfDot11SupportedRateSet.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11SupportedRateSet.setStatus(_A)
class _HpnicfDot11MandatoryRateSet_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_HpnicfDot11MandatoryRateSet_Type.__name__=_H
_HpnicfDot11MandatoryRateSet_Object=MibTableColumn
hpnicfDot11MandatoryRateSet=_HpnicfDot11MandatoryRateSet_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,4,5,1,1,3),_HpnicfDot11MandatoryRateSet_Type())
hpnicfDot11MandatoryRateSet.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11MandatoryRateSet.setStatus(_A)
class _HpnicfDot11DisabledRateSet_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_HpnicfDot11DisabledRateSet_Type.__name__=_H
_HpnicfDot11DisabledRateSet_Object=MibTableColumn
hpnicfDot11DisabledRateSet=_HpnicfDot11DisabledRateSet_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,4,5,1,1,4),_HpnicfDot11DisabledRateSet_Type())
hpnicfDot11DisabledRateSet.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11DisabledRateSet.setStatus(_A)
class _HpnicfDot11SmartRateSet_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_HpnicfDot11SmartRateSet_Type.__name__=_H
_HpnicfDot11SmartRateSet_Object=MibTableColumn
hpnicfDot11SmartRateSet=_HpnicfDot11SmartRateSet_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,4,5,1,1,5),_HpnicfDot11SmartRateSet_Type())
hpnicfDot11SmartRateSet.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11SmartRateSet.setStatus(_A)
_HpnicfDot11InterfaceConfigGroup_ObjectIdentity=ObjectIdentity
hpnicfDot11InterfaceConfigGroup=_HpnicfDot11InterfaceConfigGroup_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,75,4,6))
_HpnicfDot11WlanEssIfTable_Object=MibTable
hpnicfDot11WlanEssIfTable=_HpnicfDot11WlanEssIfTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,4,6,1))
if mibBuilder.loadTexts:hpnicfDot11WlanEssIfTable.setStatus(_A)
_HpnicfDot11WlanEssIfEntry_Object=MibTableRow
hpnicfDot11WlanEssIfEntry=_HpnicfDot11WlanEssIfEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,4,6,1,1))
hpnicfDot11WlanEssIfEntry.setIndexNames((0,_E,_AN))
if mibBuilder.loadTexts:hpnicfDot11WlanEssIfEntry.setStatus(_A)
_HpnicfDot11WlanEssIfNumber_Type=Integer32
_HpnicfDot11WlanEssIfNumber_Object=MibTableColumn
hpnicfDot11WlanEssIfNumber=_HpnicfDot11WlanEssIfNumber_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,4,6,1,1,1),_HpnicfDot11WlanEssIfNumber_Type())
hpnicfDot11WlanEssIfNumber.setMaxAccess(_F)
if mibBuilder.loadTexts:hpnicfDot11WlanEssIfNumber.setStatus(_A)
_HpnicfDot11WlanEssIfIndex_Type=Integer32
_HpnicfDot11WlanEssIfIndex_Object=MibTableColumn
hpnicfDot11WlanEssIfIndex=_HpnicfDot11WlanEssIfIndex_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,4,6,1,1,2),_HpnicfDot11WlanEssIfIndex_Type())
hpnicfDot11WlanEssIfIndex.setMaxAccess(_I)
if mibBuilder.loadTexts:hpnicfDot11WlanEssIfIndex.setStatus(_A)
_HpnicfDot11WlanEssRowStatus_Type=RowStatus
_HpnicfDot11WlanEssRowStatus_Object=MibTableColumn
hpnicfDot11WlanEssRowStatus=_HpnicfDot11WlanEssRowStatus_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,4,6,1,1,3),_HpnicfDot11WlanEssRowStatus_Type())
hpnicfDot11WlanEssRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfDot11WlanEssRowStatus.setStatus(_A)
_HpnicfDot11WlanBssIfTable_Object=MibTable
hpnicfDot11WlanBssIfTable=_HpnicfDot11WlanBssIfTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,4,6,2))
if mibBuilder.loadTexts:hpnicfDot11WlanBssIfTable.setStatus(_A)
_HpnicfDot11WlanBssIfEntry_Object=MibTableRow
hpnicfDot11WlanBssIfEntry=_HpnicfDot11WlanBssIfEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,4,6,2,1))
hpnicfDot11WlanBssIfEntry.setIndexNames((0,_E,_AO))
if mibBuilder.loadTexts:hpnicfDot11WlanBssIfEntry.setStatus(_A)
_HpnicfDot11WlanBssIfNumber_Type=Integer32
_HpnicfDot11WlanBssIfNumber_Object=MibTableColumn
hpnicfDot11WlanBssIfNumber=_HpnicfDot11WlanBssIfNumber_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,4,6,2,1,1),_HpnicfDot11WlanBssIfNumber_Type())
hpnicfDot11WlanBssIfNumber.setMaxAccess(_F)
if mibBuilder.loadTexts:hpnicfDot11WlanBssIfNumber.setStatus(_A)
_HpnicfDot11WlanBssIfIndex_Type=Integer32
_HpnicfDot11WlanBssIfIndex_Object=MibTableColumn
hpnicfDot11WlanBssIfIndex=_HpnicfDot11WlanBssIfIndex_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,4,6,2,1,2),_HpnicfDot11WlanBssIfIndex_Type())
hpnicfDot11WlanBssIfIndex.setMaxAccess(_I)
if mibBuilder.loadTexts:hpnicfDot11WlanBssIfIndex.setStatus(_A)
_HpnicfDot11WlanBssRowStatus_Type=RowStatus
_HpnicfDot11WlanBssRowStatus_Object=MibTableColumn
hpnicfDot11WlanBssRowStatus=_HpnicfDot11WlanBssRowStatus_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,4,6,2,1,3),_HpnicfDot11WlanBssRowStatus_Type())
hpnicfDot11WlanBssRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfDot11WlanBssRowStatus.setStatus(_A)
_HpnicfDot11WLANEthernetIfTable_Object=MibTable
hpnicfDot11WLANEthernetIfTable=_HpnicfDot11WLANEthernetIfTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,4,6,3))
if mibBuilder.loadTexts:hpnicfDot11WLANEthernetIfTable.setStatus(_A)
_HpnicfDot11WLANEthernetIfEntry_Object=MibTableRow
hpnicfDot11WLANEthernetIfEntry=_HpnicfDot11WLANEthernetIfEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,4,6,3,1))
hpnicfDot11WLANEthernetIfEntry.setIndexNames((0,_E,_AP))
if mibBuilder.loadTexts:hpnicfDot11WLANEthernetIfEntry.setStatus(_A)
_HpnicfDot11WlanEthernetIfNumber_Type=Integer32
_HpnicfDot11WlanEthernetIfNumber_Object=MibTableColumn
hpnicfDot11WlanEthernetIfNumber=_HpnicfDot11WlanEthernetIfNumber_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,4,6,3,1,1),_HpnicfDot11WlanEthernetIfNumber_Type())
hpnicfDot11WlanEthernetIfNumber.setMaxAccess(_F)
if mibBuilder.loadTexts:hpnicfDot11WlanEthernetIfNumber.setStatus(_A)
_HpnicfDot11WLANEthernetIfIndex_Type=Integer32
_HpnicfDot11WLANEthernetIfIndex_Object=MibTableColumn
hpnicfDot11WLANEthernetIfIndex=_HpnicfDot11WLANEthernetIfIndex_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,4,6,3,1,2),_HpnicfDot11WLANEthernetIfIndex_Type())
hpnicfDot11WLANEthernetIfIndex.setMaxAccess(_I)
if mibBuilder.loadTexts:hpnicfDot11WLANEthernetIfIndex.setStatus(_A)
_HpnicfDot11WlanEthernetRowStatus_Type=RowStatus
_HpnicfDot11WlanEthernetRowStatus_Object=MibTableColumn
hpnicfDot11WlanEthernetRowStatus=_HpnicfDot11WlanEthernetRowStatus_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,4,6,3,1,3),_HpnicfDot11WlanEthernetRowStatus_Type())
hpnicfDot11WlanEthernetRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfDot11WlanEthernetRowStatus.setStatus(_A)
_HpnicfDot11PortSecurityTable_Object=MibTable
hpnicfDot11PortSecurityTable=_HpnicfDot11PortSecurityTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,4,6,4))
if mibBuilder.loadTexts:hpnicfDot11PortSecurityTable.setStatus(_A)
_HpnicfDot11PortSecurityEntry_Object=MibTableRow
hpnicfDot11PortSecurityEntry=_HpnicfDot11PortSecurityEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,4,6,4,1))
hpnicfDot11PortSecurityEntry.setIndexNames((0,_t,_u))
if mibBuilder.loadTexts:hpnicfDot11PortSecurityEntry.setStatus(_A)
class _HpnicfDot11PortSecurityMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*((_A4,1),(_A5,2),(_h,3),(_A6,4),(_A7,5),('ext',6)))
_HpnicfDot11PortSecurityMode_Type.__name__=_D
_HpnicfDot11PortSecurityMode_Object=MibTableColumn
hpnicfDot11PortSecurityMode=_HpnicfDot11PortSecurityMode_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,4,6,4,1,1),_HpnicfDot11PortSecurityMode_Type())
hpnicfDot11PortSecurityMode.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11PortSecurityMode.setStatus(_A)
class _HpnicfDot11SecurityUserLoginTxKeyType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_A8,1),(_A9,2),(_AA,3)))
_HpnicfDot11SecurityUserLoginTxKeyType_Type.__name__=_D
_HpnicfDot11SecurityUserLoginTxKeyType_Object=MibTableColumn
hpnicfDot11SecurityUserLoginTxKeyType=_HpnicfDot11SecurityUserLoginTxKeyType_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,4,6,4,1,2),_HpnicfDot11SecurityUserLoginTxKeyType_Type())
hpnicfDot11SecurityUserLoginTxKeyType.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11SecurityUserLoginTxKeyType.setStatus(_A)
class _HpnicfDot11SecurityPskKeyMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_i,1),(_j,2),(_k,3)))
_HpnicfDot11SecurityPskKeyMode_Type.__name__=_D
_HpnicfDot11SecurityPskKeyMode_Object=MibTableColumn
hpnicfDot11SecurityPskKeyMode=_HpnicfDot11SecurityPskKeyMode_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,4,6,4,1,3),_HpnicfDot11SecurityPskKeyMode_Type())
hpnicfDot11SecurityPskKeyMode.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11SecurityPskKeyMode.setStatus(_A)
_HpnicfDot11SecurityPskKeyString_Type=DisplayString
_HpnicfDot11SecurityPskKeyString_Object=MibTableColumn
hpnicfDot11SecurityPskKeyString=_HpnicfDot11SecurityPskKeyString_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,4,6,4,1,4),_HpnicfDot11SecurityPskKeyString_Type())
hpnicfDot11SecurityPskKeyString.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11SecurityPskKeyString.setStatus(_A)
_HpnicfDot11WlanMeshIfTable_Object=MibTable
hpnicfDot11WlanMeshIfTable=_HpnicfDot11WlanMeshIfTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,4,6,5))
if mibBuilder.loadTexts:hpnicfDot11WlanMeshIfTable.setStatus(_A)
_HpnicfDot11WlanMeshIfEntry_Object=MibTableRow
hpnicfDot11WlanMeshIfEntry=_HpnicfDot11WlanMeshIfEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,4,6,5,1))
hpnicfDot11WlanMeshIfEntry.setIndexNames((0,_E,_AQ))
if mibBuilder.loadTexts:hpnicfDot11WlanMeshIfEntry.setStatus(_A)
_HpnicfDot11WlanMeshIfNumber_Type=Integer32
_HpnicfDot11WlanMeshIfNumber_Object=MibTableColumn
hpnicfDot11WlanMeshIfNumber=_HpnicfDot11WlanMeshIfNumber_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,4,6,5,1,1),_HpnicfDot11WlanMeshIfNumber_Type())
hpnicfDot11WlanMeshIfNumber.setMaxAccess(_F)
if mibBuilder.loadTexts:hpnicfDot11WlanMeshIfNumber.setStatus(_A)
_HpnicfDot11WlanMeshIfIndex_Type=Integer32
_HpnicfDot11WlanMeshIfIndex_Object=MibTableColumn
hpnicfDot11WlanMeshIfIndex=_HpnicfDot11WlanMeshIfIndex_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,4,6,5,1,2),_HpnicfDot11WlanMeshIfIndex_Type())
hpnicfDot11WlanMeshIfIndex.setMaxAccess(_I)
if mibBuilder.loadTexts:hpnicfDot11WlanMeshIfIndex.setStatus(_A)
_HpnicfDot11WlanMeshRowStatus_Type=RowStatus
_HpnicfDot11WlanMeshRowStatus_Object=MibTableColumn
hpnicfDot11WlanMeshRowStatus=_HpnicfDot11WlanMeshRowStatus_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,4,6,5,1,3),_HpnicfDot11WlanMeshRowStatus_Type())
hpnicfDot11WlanMeshRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfDot11WlanMeshRowStatus.setStatus(_A)
_HpnicfDot11ACBackupGroup_ObjectIdentity=ObjectIdentity
hpnicfDot11ACBackupGroup=_HpnicfDot11ACBackupGroup_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,75,4,7))
_HpnicfDot11BackupACAdrssIP_Type=InetAddress
_HpnicfDot11BackupACAdrssIP_Object=MibScalar
hpnicfDot11BackupACAdrssIP=_HpnicfDot11BackupACAdrssIP_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,4,7,1),_HpnicfDot11BackupACAdrssIP_Type())
hpnicfDot11BackupACAdrssIP.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11BackupACAdrssIP.setStatus(_A)
_HpnicfDot11BackupACAdrssIPv6_Type=InetAddress
_HpnicfDot11BackupACAdrssIPv6_Object=MibScalar
hpnicfDot11BackupACAdrssIPv6=_HpnicfDot11BackupACAdrssIPv6_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,4,7,2),_HpnicfDot11BackupACAdrssIPv6_Type())
hpnicfDot11BackupACAdrssIPv6.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11BackupACAdrssIPv6.setStatus(_A)
_HpnicfDot11RadioElementConfigGroup_ObjectIdentity=ObjectIdentity
hpnicfDot11RadioElementConfigGroup=_HpnicfDot11RadioElementConfigGroup_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,75,4,8))
_HpnicfDot11nRadioCfgTable_Object=MibTable
hpnicfDot11nRadioCfgTable=_HpnicfDot11nRadioCfgTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,4,8,1))
if mibBuilder.loadTexts:hpnicfDot11nRadioCfgTable.setStatus(_A)
_HpnicfDot11nRadioCfgEntry_Object=MibTableRow
hpnicfDot11nRadioCfgEntry=_HpnicfDot11nRadioCfgEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,4,8,1,1))
hpnicfDot11nRadioCfgEntry.setIndexNames((0,_E,_AR))
if mibBuilder.loadTexts:hpnicfDot11nRadioCfgEntry.setStatus(_A)
_HpnicfDot11nRadioCfgIndex_Type=HpnicfDot11RadioElementIndex
_HpnicfDot11nRadioCfgIndex_Object=MibTableColumn
hpnicfDot11nRadioCfgIndex=_HpnicfDot11nRadioCfgIndex_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,4,8,1,1,1),_HpnicfDot11nRadioCfgIndex_Type())
hpnicfDot11nRadioCfgIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:hpnicfDot11nRadioCfgIndex.setStatus(_A)
class _HpnicfDot11nAMpduEnable_Type(TruthValue):defaultValue=1
_HpnicfDot11nAMpduEnable_Type.__name__=_G
_HpnicfDot11nAMpduEnable_Object=MibTableColumn
hpnicfDot11nAMpduEnable=_HpnicfDot11nAMpduEnable_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,4,8,1,1,2),_HpnicfDot11nAMpduEnable_Type())
hpnicfDot11nAMpduEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11nAMpduEnable.setStatus(_A)
class _HpnicfDot11nAMsduEnable_Type(TruthValue):defaultValue=1
_HpnicfDot11nAMsduEnable_Type.__name__=_G
_HpnicfDot11nAMsduEnable_Object=MibTableColumn
hpnicfDot11nAMsduEnable=_HpnicfDot11nAMsduEnable_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,4,8,1,1,3),_HpnicfDot11nAMsduEnable_Type())
hpnicfDot11nAMsduEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11nAMsduEnable.setStatus(_A)
class _HpnicfDot11nClientDot11nOnly_Type(TruthValue):defaultValue=2
_HpnicfDot11nClientDot11nOnly_Type.__name__=_G
_HpnicfDot11nClientDot11nOnly_Object=MibTableColumn
hpnicfDot11nClientDot11nOnly=_HpnicfDot11nClientDot11nOnly_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,4,8,1,1,4),_HpnicfDot11nClientDot11nOnly_Type())
hpnicfDot11nClientDot11nOnly.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11nClientDot11nOnly.setStatus(_A)
class _HpnicfDot11nChanelBand_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_o,1),(_p,2),('mode80',3)))
_HpnicfDot11nChanelBand_Type.__name__=_D
_HpnicfDot11nChanelBand_Object=MibTableColumn
hpnicfDot11nChanelBand=_HpnicfDot11nChanelBand_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,4,8,1,1,5),_HpnicfDot11nChanelBand_Type())
hpnicfDot11nChanelBand.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11nChanelBand.setStatus(_A)
class _HpnicfDot11nShortGiEnable_Type(TruthValue):defaultValue=1
_HpnicfDot11nShortGiEnable_Type.__name__=_G
_HpnicfDot11nShortGiEnable_Object=MibTableColumn
hpnicfDot11nShortGiEnable=_HpnicfDot11nShortGiEnable_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,4,8,1,1,6),_HpnicfDot11nShortGiEnable_Type())
hpnicfDot11nShortGiEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11nShortGiEnable.setStatus(_A)
class _HpnicfDot11nClientDot11acOnly_Type(TruthValue):defaultValue=2
_HpnicfDot11nClientDot11acOnly_Type.__name__=_G
_HpnicfDot11nClientDot11acOnly_Object=MibTableColumn
hpnicfDot11nClientDot11acOnly=_HpnicfDot11nClientDot11acOnly_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,4,8,1,1,7),_HpnicfDot11nClientDot11acOnly_Type())
hpnicfDot11nClientDot11acOnly.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11nClientDot11acOnly.setStatus(_A)
_HpnicfDot11RadioWDSTable_Object=MibTable
hpnicfDot11RadioWDSTable=_HpnicfDot11RadioWDSTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,4,8,2))
if mibBuilder.loadTexts:hpnicfDot11RadioWDSTable.setStatus(_A)
_HpnicfDot11RadioWDSEntry_Object=MibTableRow
hpnicfDot11RadioWDSEntry=_HpnicfDot11RadioWDSEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,4,8,2,1))
hpnicfDot11RadioWDSEntry.setIndexNames((0,_E,_AS))
if mibBuilder.loadTexts:hpnicfDot11RadioWDSEntry.setStatus(_A)
_HpnicfDot11RadioWDSIndex_Type=HpnicfDot11RadioElementIndex
_HpnicfDot11RadioWDSIndex_Object=MibTableColumn
hpnicfDot11RadioWDSIndex=_HpnicfDot11RadioWDSIndex_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,4,8,2,1,1),_HpnicfDot11RadioWDSIndex_Type())
hpnicfDot11RadioWDSIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:hpnicfDot11RadioWDSIndex.setStatus(_A)
class _HpnicfDot11RadioWDSMode_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('nowds',1),('wds',2)))
_HpnicfDot11RadioWDSMode_Type.__name__=_D
_HpnicfDot11RadioWDSMode_Object=MibTableColumn
hpnicfDot11RadioWDSMode=_HpnicfDot11RadioWDSMode_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,4,8,2,1,2),_HpnicfDot11RadioWDSMode_Type())
hpnicfDot11RadioWDSMode.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11RadioWDSMode.setStatus(_A)
class _HpnicfDot11RadioWDSNetWorkID_Type(OctetString):defaultValue=OctetString('');subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_HpnicfDot11RadioWDSNetWorkID_Type.__name__=_H
_HpnicfDot11RadioWDSNetWorkID_Object=MibTableColumn
hpnicfDot11RadioWDSNetWorkID=_HpnicfDot11RadioWDSNetWorkID_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,4,8,2,1,3),_HpnicfDot11RadioWDSNetWorkID_Type())
hpnicfDot11RadioWDSNetWorkID.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11RadioWDSNetWorkID.setStatus(_A)
class _HpnicfDot11WDSSecPskKeyMode_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_i,1),(_j,2),(_k,3)))
_HpnicfDot11WDSSecPskKeyMode_Type.__name__=_D
_HpnicfDot11WDSSecPskKeyMode_Object=MibTableColumn
hpnicfDot11WDSSecPskKeyMode=_HpnicfDot11WDSSecPskKeyMode_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,4,8,2,1,4),_HpnicfDot11WDSSecPskKeyMode_Type())
hpnicfDot11WDSSecPskKeyMode.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11WDSSecPskKeyMode.setStatus(_A)
class _HpnicfDot11WDSSecPskKeyString_Type(DisplayString):defaultValue=OctetString('')
_HpnicfDot11WDSSecPskKeyString_Type.__name__=_b
_HpnicfDot11WDSSecPskKeyString_Object=MibTableColumn
hpnicfDot11WDSSecPskKeyString=_HpnicfDot11WDSSecPskKeyString_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,4,8,2,1,5),_HpnicfDot11WDSSecPskKeyString_Type())
hpnicfDot11WDSSecPskKeyString.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11WDSSecPskKeyString.setStatus(_A)
_HpnicfDot11nRadioCfg2Table_Object=MibTable
hpnicfDot11nRadioCfg2Table=_HpnicfDot11nRadioCfg2Table_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,4,8,3))
if mibBuilder.loadTexts:hpnicfDot11nRadioCfg2Table.setStatus(_A)
_HpnicfDot11nRadioCfg2Entry_Object=MibTableRow
hpnicfDot11nRadioCfg2Entry=_HpnicfDot11nRadioCfg2Entry_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,4,8,3,1))
hpnicfDot11nRadioCfg2Entry.setIndexNames((0,_E,_AT),(0,_E,_AU))
if mibBuilder.loadTexts:hpnicfDot11nRadioCfg2Entry.setStatus(_A)
_HpnicfDot11nRadioCfg2APIDIndex_Type=HpnicfDot11ObjectIDType
_HpnicfDot11nRadioCfg2APIDIndex_Object=MibTableColumn
hpnicfDot11nRadioCfg2APIDIndex=_HpnicfDot11nRadioCfg2APIDIndex_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,4,8,3,1,1),_HpnicfDot11nRadioCfg2APIDIndex_Type())
hpnicfDot11nRadioCfg2APIDIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:hpnicfDot11nRadioCfg2APIDIndex.setStatus(_A)
_HpnicfDot11nRadioCfg2RadioIDIndex_Type=HpnicfDot11RadioScopeType
_HpnicfDot11nRadioCfg2RadioIDIndex_Object=MibTableColumn
hpnicfDot11nRadioCfg2RadioIDIndex=_HpnicfDot11nRadioCfg2RadioIDIndex_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,4,8,3,1,2),_HpnicfDot11nRadioCfg2RadioIDIndex_Type())
hpnicfDot11nRadioCfg2RadioIDIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:hpnicfDot11nRadioCfg2RadioIDIndex.setStatus(_A)
class _HpnicfDot11nRadioCfg2AMpduEnable_Type(TruthValue):defaultValue=1
_HpnicfDot11nRadioCfg2AMpduEnable_Type.__name__=_G
_HpnicfDot11nRadioCfg2AMpduEnable_Object=MibTableColumn
hpnicfDot11nRadioCfg2AMpduEnable=_HpnicfDot11nRadioCfg2AMpduEnable_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,4,8,3,1,3),_HpnicfDot11nRadioCfg2AMpduEnable_Type())
hpnicfDot11nRadioCfg2AMpduEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11nRadioCfg2AMpduEnable.setStatus(_A)
class _HpnicfDot11nRadioCfg2AMsduEnable_Type(TruthValue):defaultValue=1
_HpnicfDot11nRadioCfg2AMsduEnable_Type.__name__=_G
_HpnicfDot11nRadioCfg2AMsduEnable_Object=MibTableColumn
hpnicfDot11nRadioCfg2AMsduEnable=_HpnicfDot11nRadioCfg2AMsduEnable_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,4,8,3,1,4),_HpnicfDot11nRadioCfg2AMsduEnable_Type())
hpnicfDot11nRadioCfg2AMsduEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11nRadioCfg2AMsduEnable.setStatus(_A)
class _HpnicfDot11nRadioCfg2ClientDot11nOnly_Type(TruthValue):defaultValue=2
_HpnicfDot11nRadioCfg2ClientDot11nOnly_Type.__name__=_G
_HpnicfDot11nRadioCfg2ClientDot11nOnly_Object=MibTableColumn
hpnicfDot11nRadioCfg2ClientDot11nOnly=_HpnicfDot11nRadioCfg2ClientDot11nOnly_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,4,8,3,1,5),_HpnicfDot11nRadioCfg2ClientDot11nOnly_Type())
hpnicfDot11nRadioCfg2ClientDot11nOnly.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11nRadioCfg2ClientDot11nOnly.setStatus(_A)
class _HpnicfDot11nRadioCfg2ChannelBand_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_o,1),(_p,2),('mode80',3)))
_HpnicfDot11nRadioCfg2ChannelBand_Type.__name__=_D
_HpnicfDot11nRadioCfg2ChannelBand_Object=MibTableColumn
hpnicfDot11nRadioCfg2ChannelBand=_HpnicfDot11nRadioCfg2ChannelBand_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,4,8,3,1,6),_HpnicfDot11nRadioCfg2ChannelBand_Type())
hpnicfDot11nRadioCfg2ChannelBand.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11nRadioCfg2ChannelBand.setStatus(_A)
class _HpnicfDot11nRadioCfg2ShortGiEnable_Type(TruthValue):defaultValue=1
_HpnicfDot11nRadioCfg2ShortGiEnable_Type.__name__=_G
_HpnicfDot11nRadioCfg2ShortGiEnable_Object=MibTableColumn
hpnicfDot11nRadioCfg2ShortGiEnable=_HpnicfDot11nRadioCfg2ShortGiEnable_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,4,8,3,1,7),_HpnicfDot11nRadioCfg2ShortGiEnable_Type())
hpnicfDot11nRadioCfg2ShortGiEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11nRadioCfg2ShortGiEnable.setStatus(_A)
class _HpnicfDot11nRadioCfg2AMpduEnableCM_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_P,0),(_Q,1)))
_HpnicfDot11nRadioCfg2AMpduEnableCM_Type.__name__=_D
_HpnicfDot11nRadioCfg2AMpduEnableCM_Object=MibTableColumn
hpnicfDot11nRadioCfg2AMpduEnableCM=_HpnicfDot11nRadioCfg2AMpduEnableCM_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,4,8,3,1,8),_HpnicfDot11nRadioCfg2AMpduEnableCM_Type())
hpnicfDot11nRadioCfg2AMpduEnableCM.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11nRadioCfg2AMpduEnableCM.setStatus(_A)
class _HpnicfDot11nRadioCfg2ChannelBandCM_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_p,1),(_o,2)))
_HpnicfDot11nRadioCfg2ChannelBandCM_Type.__name__=_D
_HpnicfDot11nRadioCfg2ChannelBandCM_Object=MibTableColumn
hpnicfDot11nRadioCfg2ChannelBandCM=_HpnicfDot11nRadioCfg2ChannelBandCM_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,4,8,3,1,9),_HpnicfDot11nRadioCfg2ChannelBandCM_Type())
hpnicfDot11nRadioCfg2ChannelBandCM.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11nRadioCfg2ChannelBandCM.setStatus(_A)
class _HpnicfDot11nRadioCfg2ShortGiEnableCM_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_P,0),(_Q,1)))
_HpnicfDot11nRadioCfg2ShortGiEnableCM_Type.__name__=_D
_HpnicfDot11nRadioCfg2ShortGiEnableCM_Object=MibTableColumn
hpnicfDot11nRadioCfg2ShortGiEnableCM=_HpnicfDot11nRadioCfg2ShortGiEnableCM_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,4,8,3,1,10),_HpnicfDot11nRadioCfg2ShortGiEnableCM_Type())
hpnicfDot11nRadioCfg2ShortGiEnableCM.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11nRadioCfg2ShortGiEnableCM.setStatus(_A)
class _HpnicfDot11nRadioCfg2ClientDot11acOnly_Type(TruthValue):defaultValue=2
_HpnicfDot11nRadioCfg2ClientDot11acOnly_Type.__name__=_G
_HpnicfDot11nRadioCfg2ClientDot11acOnly_Object=MibTableColumn
hpnicfDot11nRadioCfg2ClientDot11acOnly=_HpnicfDot11nRadioCfg2ClientDot11acOnly_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,4,8,3,1,11),_HpnicfDot11nRadioCfg2ClientDot11acOnly_Type())
hpnicfDot11nRadioCfg2ClientDot11acOnly.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11nRadioCfg2ClientDot11acOnly.setStatus(_A)
class _HpnicfDot11nRadioCfg2ClientDot11nOnlyCM_Type(HpnicfDot11TruthValueCM):defaultValue=0
_HpnicfDot11nRadioCfg2ClientDot11nOnlyCM_Type.__name__=_S
_HpnicfDot11nRadioCfg2ClientDot11nOnlyCM_Object=MibTableColumn
hpnicfDot11nRadioCfg2ClientDot11nOnlyCM=_HpnicfDot11nRadioCfg2ClientDot11nOnlyCM_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,4,8,3,1,12),_HpnicfDot11nRadioCfg2ClientDot11nOnlyCM_Type())
hpnicfDot11nRadioCfg2ClientDot11nOnlyCM.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot11nRadioCfg2ClientDot11nOnlyCM.setStatus(_A)
_HpnicfDot11CfgNotifyGroup_ObjectIdentity=ObjectIdentity
hpnicfDot11CfgNotifyGroup=_HpnicfDot11CfgNotifyGroup_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,75,4,9))
_HpnicfDot11CfgNotifications_ObjectIdentity=ObjectIdentity
hpnicfDot11CfgNotifications=_HpnicfDot11CfgNotifications_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,75,4,9,0))
_HpnicfDot11CfgTrapVarObjects_ObjectIdentity=ObjectIdentity
hpnicfDot11CfgTrapVarObjects=_HpnicfDot11CfgTrapVarObjects_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,75,4,9,1))
class _HpnicfDot11PreConflictTemplateNum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1024))
_HpnicfDot11PreConflictTemplateNum_Type.__name__=_D
_HpnicfDot11PreConflictTemplateNum_Object=MibScalar
hpnicfDot11PreConflictTemplateNum=_HpnicfDot11PreConflictTemplateNum_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,4,9,1,1),_HpnicfDot11PreConflictTemplateNum_Type())
hpnicfDot11PreConflictTemplateNum.setMaxAccess(_N)
if mibBuilder.loadTexts:hpnicfDot11PreConflictTemplateNum.setStatus(_A)
class _HpnicfDot11CurrConflictTemplateNum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1024))
_HpnicfDot11CurrConflictTemplateNum_Type.__name__=_D
_HpnicfDot11CurrConflictTemplateNum_Object=MibScalar
hpnicfDot11CurrConflictTemplateNum=_HpnicfDot11CurrConflictTemplateNum_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,4,9,1,2),_HpnicfDot11CurrConflictTemplateNum_Type())
hpnicfDot11CurrConflictTemplateNum.setMaxAccess(_N)
if mibBuilder.loadTexts:hpnicfDot11CurrConflictTemplateNum.setStatus(_A)
class _HpnicfDot11ConflictCipherIdx_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4))
_HpnicfDot11ConflictCipherIdx_Type.__name__=_D
_HpnicfDot11ConflictCipherIdx_Object=MibScalar
hpnicfDot11ConflictCipherIdx=_HpnicfDot11ConflictCipherIdx_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,4,9,1,3),_HpnicfDot11ConflictCipherIdx_Type())
hpnicfDot11ConflictCipherIdx.setMaxAccess(_N)
if mibBuilder.loadTexts:hpnicfDot11ConflictCipherIdx.setStatus(_A)
_HpnicfDot11ConfigureAPID_Type=HpnicfDot11ObjectIDType
_HpnicfDot11ConfigureAPID_Object=MibScalar
hpnicfDot11ConfigureAPID=_HpnicfDot11ConfigureAPID_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,4,9,1,4),_HpnicfDot11ConfigureAPID_Type())
hpnicfDot11ConfigureAPID.setMaxAccess(_N)
if mibBuilder.loadTexts:hpnicfDot11ConfigureAPID.setStatus(_A)
_HpnicfDot11ConfigureRadioID_Type=HpnicfDot11RadioScopeType
_HpnicfDot11ConfigureRadioID_Object=MibScalar
hpnicfDot11ConfigureRadioID=_HpnicfDot11ConfigureRadioID_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,4,9,1,5),_HpnicfDot11ConfigureRadioID_Type())
hpnicfDot11ConfigureRadioID.setMaxAccess(_N)
if mibBuilder.loadTexts:hpnicfDot11ConfigureRadioID.setStatus(_A)
_HpnicfDot11ConfigureAPMacAddress_Type=MacAddress
_HpnicfDot11ConfigureAPMacAddress_Object=MibScalar
hpnicfDot11ConfigureAPMacAddress=_HpnicfDot11ConfigureAPMacAddress_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,4,9,1,6),_HpnicfDot11ConfigureAPMacAddress_Type())
hpnicfDot11ConfigureAPMacAddress.setMaxAccess(_N)
if mibBuilder.loadTexts:hpnicfDot11ConfigureAPMacAddress.setStatus(_A)
hpnicfDot11CfgCipherChange=NotificationType((1,3,6,1,4,1,11,2,14,11,15,2,75,4,9,0,1))
hpnicfDot11CfgCipherChange.setObjects(*((_E,_q),(_E,_AV)))
if mibBuilder.loadTexts:hpnicfDot11CfgCipherChange.setStatus(_A)
hpnicfDot11CfgPSKChange=NotificationType((1,3,6,1,4,1,11,2,14,11,15,2,75,4,9,0,2))
hpnicfDot11CfgPSKChange.setObjects((_E,_q))
if mibBuilder.loadTexts:hpnicfDot11CfgPSKChange.setStatus(_A)
hpnicfDot11SSIDWepIDConflictTrap=NotificationType((1,3,6,1,4,1,11,2,14,11,15,2,75,4,9,0,3))
hpnicfDot11SSIDWepIDConflictTrap.setObjects(*((_E,_AW),(_E,_AX),(_E,_AY),(_E,_AZ),(_E,_Aa),(_E,_Ab)))
if mibBuilder.loadTexts:hpnicfDot11SSIDWepIDConflictTrap.setStatus(_A)
mibBuilder.exportSymbols(_E,**{'hpnicfDot11CFG':hpnicfDot11CFG,'hpnicfDot11GlobeConfigGroup':hpnicfDot11GlobeConfigGroup,'hpnicfDot11GlobalCountryCode':hpnicfDot11GlobalCountryCode,'hpnicfDot11StaKeepALiveTimerIntvl':hpnicfDot11StaKeepALiveTimerIntvl,'hpnicfDot11StaIdleTimerIntvl':hpnicfDot11StaIdleTimerIntvl,'hpnicfDot11BroadcastProbeReply':hpnicfDot11BroadcastProbeReply,'hpnicfDot11APScanMode':hpnicfDot11APScanMode,'hpnicfDot11ACCtrlTunnelSecSupport':hpnicfDot11ACCtrlTunnelSecSupport,'hpnicfDot11ACDataTunnelSecSupport':hpnicfDot11ACDataTunnelSecSupport,'hpnicfDot11ACAutoAPSupport':hpnicfDot11ACAutoAPSupport,'hpnicfDot11AutoAPName':hpnicfDot11AutoAPName,'hpnicfDot11PersistentName':hpnicfDot11PersistentName,'hpnicfDot11IntfTrapThreshold':hpnicfDot11IntfTrapThreshold,'hpnicfDot11MonitorInterval':hpnicfDot11MonitorInterval,'hpnicfDot11SampleInterval':hpnicfDot11SampleInterval,'hpnicfDot11ChnlSwitChkInterval':hpnicfDot11ChnlSwitChkInterval,'hpnicfDot11APUserUplimit':hpnicfDot11APUserUplimit,'hpnicfDot11APL2IsolateEnable':hpnicfDot11APL2IsolateEnable,'hpnicfDot11APBSSIDSupportNum':hpnicfDot11APBSSIDSupportNum,'hpnicfDot11APLastUpdateStatTime':hpnicfDot11APLastUpdateStatTime,'hpnicfDot11APDoSProtectEnable':hpnicfDot11APDoSProtectEnable,'hpnicfDot11MaxAPPerIf':hpnicfDot11MaxAPPerIf,'hpnicfDot11SampleTimeStamp':hpnicfDot11SampleTimeStamp,'hpnicfDot11UplinkTrackId':hpnicfDot11UplinkTrackId,'hpnicfDot11RtCollectSwitch':hpnicfDot11RtCollectSwitch,'hpnicfDot11RglCollectIntvl':hpnicfDot11RglCollectIntvl,'hpnicfDot11RtCollectIntvl':hpnicfDot11RtCollectIntvl,'hpnicfDot11AllAPCpuUsageThreshold':hpnicfDot11AllAPCpuUsageThreshold,'hpnicfDot11AllAPMemUsageThreshold':hpnicfDot11AllAPMemUsageThreshold,'hpnicfDot11AdjIntfTrapThreshold':hpnicfDot11AdjIntfTrapThreshold,'hpnicfDot11AllAPMonitorMode':hpnicfDot11AllAPMonitorMode,'hpnicfDot11GlobalApFmwUpdState':hpnicfDot11GlobalApFmwUpdState,'hpnicfDot11ACNasIDCM':hpnicfDot11ACNasIDCM,'hpnicfDot11PolicyConfigGroup':hpnicfDot11PolicyConfigGroup,'hpnicfDot11RadioPolicyTable':hpnicfDot11RadioPolicyTable,'hpnicfDot11RadioPolicyEntry':hpnicfDot11RadioPolicyEntry,_y:hpnicfDot11RadioPolicyName,'hpnicfDot11BeaconInterval':hpnicfDot11BeaconInterval,'hpnicfDot11DtimInterval':hpnicfDot11DtimInterval,'hpnicfDot11RtsThreshold':hpnicfDot11RtsThreshold,'hpnicfDot11FragThreshold':hpnicfDot11FragThreshold,'hpnicfDot11ShortRetryThreshold':hpnicfDot11ShortRetryThreshold,'hpnicfDot11LongRetryThreshold':hpnicfDot11LongRetryThreshold,'hpnicfDot11MaxRxLifetime':hpnicfDot11MaxRxLifetime,'hpnicfDot11RdoPolicyRowStatus':hpnicfDot11RdoPolicyRowStatus,'hpnicfDot11RdoClientMaxCount':hpnicfDot11RdoClientMaxCount,'hpnicfDot11BeaconIntervalMs':hpnicfDot11BeaconIntervalMs,'hpnicfDot11ServicePolicyTable':hpnicfDot11ServicePolicyTable,'hpnicfDot11ServicePolicyEntry':hpnicfDot11ServicePolicyEntry,_f:hpnicfDot11ServicePolicyID,_q:hpnicfDot11SSIDName,'hpnicfDot11SSIDHidden':hpnicfDot11SSIDHidden,'hpnicfDot11AuthenMode':hpnicfDot11AuthenMode,'hpnicfDot11SSIDEncryptionMode':hpnicfDot11SSIDEncryptionMode,'hpnicfDot11WlanInfBindingType':hpnicfDot11WlanInfBindingType,'hpnicfDot11WlanInfBindingID':hpnicfDot11WlanInfBindingID,'hpnicfDot11SrvPolicyRowStatus':hpnicfDot11SrvPolicyRowStatus,'hpnicfDot11ClientMaxCount':hpnicfDot11ClientMaxCount,'hpnicfDot11SPInCirMode':hpnicfDot11SPInCirMode,'hpnicfDot11SPInCirValue':hpnicfDot11SPInCirValue,'hpnicfDot11SPOutCirMode':hpnicfDot11SPOutCirMode,'hpnicfDot11SPOutCirValue':hpnicfDot11SPOutCirValue,'hpnicfDot11WlanInfPVID':hpnicfDot11WlanInfPVID,'hpnicfDot11SPInCirStaticValue':hpnicfDot11SPInCirStaticValue,'hpnicfDot11SPOutCirStaticValue':hpnicfDot11SPOutCirStaticValue,'hpnicfDot11SPIsolate':hpnicfDot11SPIsolate,'hpnicfDot11WlanexAuthServerIP':hpnicfDot11WlanexAuthServerIP,'hpnicfDot11SPBeaconMeasEnable':hpnicfDot11SPBeaconMeasEnable,'hpnicfDot11SPBeaconMeasType':hpnicfDot11SPBeaconMeasType,'hpnicfDot11SPBeaconMeasInterval':hpnicfDot11SPBeaconMeasInterval,'hpnicfDot11AuthenModeCM':hpnicfDot11AuthenModeCM,'hpnicfDot11SecIEStatusCM':hpnicfDot11SecIEStatusCM,'hpnicfDot11SecurityCiphersCM':hpnicfDot11SecurityCiphersCM,'hpnicfDot11SrvPolicyStatusCM':hpnicfDot11SrvPolicyStatusCM,'hpnicfDot11SSIDHiddenCM':hpnicfDot11SSIDHiddenCM,'hpnicfDot11SPIsolateCM':hpnicfDot11SPIsolateCM,'hpnicfDot11ServicePolicyExtTable':hpnicfDot11ServicePolicyExtTable,'hpnicfDot11ServicePolicyExtEntry':hpnicfDot11ServicePolicyExtEntry,_A0:hpnicfDot11ServicePolicyExtID,'hpnicfDot11SecIEStatus':hpnicfDot11SecIEStatus,_AV:hpnicfDot11SecurityCiphers,'hpnicfDot11CipherKeyIndex':hpnicfDot11CipherKeyIndex,'hpnicfDot11CipherKey':hpnicfDot11CipherKey,'hpnicfDot11SrvPolicyExtRowStatus':hpnicfDot11SrvPolicyExtRowStatus,'hpnicfDot11CipherKeyType':hpnicfDot11CipherKeyType,'hpnicfDot11RadioPolicyExtTable':hpnicfDot11RadioPolicyExtTable,'hpnicfDot11RadioPolicyExtEntry':hpnicfDot11RadioPolicyExtEntry,_A1:hpnicfDot11RPAPSerialID,_A2:hpnicfDot11RPRadioID,'hpnicfDot11RPBeaconInterval':hpnicfDot11RPBeaconInterval,'hpnicfDot11RPDtimInterval':hpnicfDot11RPDtimInterval,'hpnicfDot11RPRtsThreshold':hpnicfDot11RPRtsThreshold,'hpnicfDot11RPFragThreshold':hpnicfDot11RPFragThreshold,'hpnicfDot11RPShortRetryThreshold':hpnicfDot11RPShortRetryThreshold,'hpnicfDot11RPLongRetryThreshold':hpnicfDot11RPLongRetryThreshold,'hpnicfDot11RPClientMaxCount':hpnicfDot11RPClientMaxCount,'hpnicfDot11RPBeaconIntervalCM':hpnicfDot11RPBeaconIntervalCM,'hpnicfDot11SrvPortSecurityTable':hpnicfDot11SrvPortSecurityTable,'hpnicfDot11SrvPortSecurityEntry':hpnicfDot11SrvPortSecurityEntry,_A3:hpnicfDot11SecurityServicePolicyID,'hpnicfDot11SrvPortSecurityMode':hpnicfDot11SrvPortSecurityMode,'hpnicfDot11SrvSecurityKeyType':hpnicfDot11SrvSecurityKeyType,'hpnicfDot11SrvSecurityPskKeyMode':hpnicfDot11SrvSecurityPskKeyMode,'hpnicfDot11SrvSecurityPskKeyString':hpnicfDot11SrvSecurityPskKeyString,'hpnicfDot11SrvPortSecurityModeCM':hpnicfDot11SrvPortSecurityModeCM,'hpnicfDot11SrvPolicyExtendTable':hpnicfDot11SrvPolicyExtendTable,'hpnicfDot11SrvPolicyExtendEntry':hpnicfDot11SrvPolicyExtendEntry,'hpnicfDot11SPEnable':hpnicfDot11SPEnable,'hpnicfDot11APConfigGroup':hpnicfDot11APConfigGroup,'hpnicfDot11APTemplateTable':hpnicfDot11APTemplateTable,'hpnicfDot11APTemplateEntry':hpnicfDot11APTemplateEntry,_AB:hpnicfDot11APTemplateName,'hpnicfDot11APSerialID':hpnicfDot11APSerialID,'hpnicfDot11TemplateAPModelAlias':hpnicfDot11TemplateAPModelAlias,'hpnicfDot11Description':hpnicfDot11Description,'hpnicfDot11APWorkMode':hpnicfDot11APWorkMode,'hpnicfDot11APTemplateRowStatus':hpnicfDot11APTemplateRowStatus,'hpnicfDot11APName':hpnicfDot11APName,'hpnicfDot11StatisInterv':hpnicfDot11StatisInterv,'hpnicfDot11APBroadcastProbeReply':hpnicfDot11APBroadcastProbeReply,'hpnicfDot11StaIdleTimerInterv':hpnicfDot11StaIdleTimerInterv,'hpnicfDot11StaKeepAliveTimerInterv':hpnicfDot11StaKeepAliveTimerInterv,'hpnicfDot11APCir':hpnicfDot11APCir,'hpnicfDot11APCbs':hpnicfDot11APCbs,'hpnicfDot11APPriorityLevel':hpnicfDot11APPriorityLevel,'hpnicfDot11APElementID':hpnicfDot11APElementID,'hpnicfDot11APDevDetectEnable':hpnicfDot11APDevDetectEnable,'hpnicfDot11APGetIPMethod':hpnicfDot11APGetIPMethod,'hpnicfDot11StatisIntervMode':hpnicfDot11StatisIntervMode,'hpnicfDot11ApTrapEnabled':hpnicfDot11ApTrapEnabled,'hpnicfDot11ApFmwUpdState':hpnicfDot11ApFmwUpdState,'hpnicfDot11StatisIntervModeCM':hpnicfDot11StatisIntervModeCM,'hpnicfDot11ApNasIDCM':hpnicfDot11ApNasIDCM,'hpnicfDot11RadioToConfigTable':hpnicfDot11RadioToConfigTable,'hpnicfDot11RadioToConfigEntry':hpnicfDot11RadioToConfigEntry,_l:hpnicfDot11APTemplateNameCfg,_W:hpnicfDot11CfgRadioID,'hpnicfDot11CfgRadioPolicyName':hpnicfDot11CfgRadioPolicyName,'hpnicfDot11CfgRadioType':hpnicfDot11CfgRadioType,'hpnicfDot11CfgChannel':hpnicfDot11CfgChannel,'hpnicfDot11CfgMaxTxPowerLevel':hpnicfDot11CfgMaxTxPowerLevel,'hpnicfDot11PreambleLen':hpnicfDot11PreambleLen,'hpnicfDot11CfgRadioStatus':hpnicfDot11CfgRadioStatus,'hpnicfDot11CfgRdElementID':hpnicfDot11CfgRdElementID,'hpnicfDot11CfgWorkMode':hpnicfDot11CfgWorkMode,'hpnicfDot11CfgPwrAttValue':hpnicfDot11CfgPwrAttValue,'hpnicfDot11RadioTxArithmetic':hpnicfDot11RadioTxArithmetic,'hpnicfDot11CfgChannelLockStat':hpnicfDot11CfgChannelLockStat,'hpnicfDot11CfgPowerLockStat':hpnicfDot11CfgPowerLockStat,'hpnicfDot11CfgLBRdGroupId':hpnicfDot11CfgLBRdGroupId,'hpnicfDot11CfgRRMSDRdGroupId':hpnicfDot11CfgRRMSDRdGroupId,'hpnicfDot11CfgRadioType2':hpnicfDot11CfgRadioType2,'hpnicfDot11CfgIDSEnable':hpnicfDot11CfgIDSEnable,'hpnicfDot11CfgSaEnable':hpnicfDot11CfgSaEnable,'hpnicfDot11CfgSaCltRtFFTData':hpnicfDot11CfgSaCltRtFFTData,'hpnicfDot11CfgSaBand':hpnicfDot11CfgSaBand,'hpnicfDot11APServiceSetTable':hpnicfDot11APServiceSetTable,'hpnicfDot11APServiceSetEntry':hpnicfDot11APServiceSetEntry,_m:hpnicfDot11CfgServicePolicyID,'hpnicfDot11SrvSetRowStatus':hpnicfDot11SrvSetRowStatus,'hpnicfDot11ServiceSetVlanId':hpnicfDot11ServiceSetVlanId,'hpnicfDot11APSysInfoSetTable':hpnicfDot11APSysInfoSetTable,'hpnicfDot11APSysInfoSetEntry':hpnicfDot11APSysInfoSetEntry,'hpnicfDot11APSysNetID':hpnicfDot11APSysNetID,'hpnicfDot11APCpuUsageThreshold':hpnicfDot11APCpuUsageThreshold,'hpnicfDot11APMemUsageThreshold':hpnicfDot11APMemUsageThreshold,'hpnicfDot11APLimitTable':hpnicfDot11APLimitTable,'hpnicfDot11APLimitEntry':hpnicfDot11APLimitEntry,'hpnicfDot11APSsidNumLimit':hpnicfDot11APSsidNumLimit,'hpnicfDot11APUserCntLimit':hpnicfDot11APUserCntLimit,'hpnicfDot11APUserThreshold':hpnicfDot11APUserThreshold,'hpnicfDot11APIfSetTable':hpnicfDot11APIfSetTable,'hpnicfDot11APIfSetEntry':hpnicfDot11APIfSetEntry,_AD:hpnicfDot11APSetIfIndex,'hpnicfDot11APIfAlias':hpnicfDot11APIfAlias,'hpnicfDot11APServiceVlanTable':hpnicfDot11APServiceVlanTable,'hpnicfDot11APServiceVlanEntry':hpnicfDot11APServiceVlanEntry,_AE:hpnicfDot11APServiceVlanSerialID,_AF:hpnicfDot11APServiceVlanSPID,'hpnicfDot11APServiceVlanId':hpnicfDot11APServiceVlanId,'hpnicfDot11APServiceVlanRowStatus':hpnicfDot11APServiceVlanRowStatus,'hpnicfDot11RadioConfigTable':hpnicfDot11RadioConfigTable,'hpnicfDot11RadioConfigEntry':hpnicfDot11RadioConfigEntry,_AG:hpnicfDot11RCAPSerialID,_AH:hpnicfDot11RCRadioID,'hpnicfDot11RCRadioType':hpnicfDot11RCRadioType,'hpnicfDot11RCChannel':hpnicfDot11RCChannel,'hpnicfDot11RCPreambleLen':hpnicfDot11RCPreambleLen,'hpnicfDot11RCPwrAttValue':hpnicfDot11RCPwrAttValue,'hpnicfDot11RCApPowerLevel':hpnicfDot11RCApPowerLevel,'hpnicfDot11RCDynamicChlState':hpnicfDot11RCDynamicChlState,'hpnicfDot11RCDynamicPowerState':hpnicfDot11RCDynamicPowerState,'hpnicfDot11RCRadioStatus':hpnicfDot11RCRadioStatus,'hpnicfDot11RCRadioRate':hpnicfDot11RCRadioRate,'hpnicfDot11RCPwrAdjustStepLength':hpnicfDot11RCPwrAdjustStepLength,'hpnicfDot11RCRadioType2':hpnicfDot11RCRadioType2,'hpnicfDot11RCPreambleLenCM':hpnicfDot11RCPreambleLenCM,'hpnicfDot11RCDynamicChlStateCM':hpnicfDot11RCDynamicChlStateCM,'hpnicfDot11RCRadioStatusCM':hpnicfDot11RCRadioStatusCM,'hpnicfDot11RCRadioRateCM':hpnicfDot11RCRadioRateCM,'hpnicfDot11RCDynamicPowerStateCM':hpnicfDot11RCDynamicPowerStateCM,'hpnicfDot11RCRssiThresholdCM':hpnicfDot11RCRssiThresholdCM,'hpnicfDot11RadioSSIDCfgTable':hpnicfDot11RadioSSIDCfgTable,'hpnicfDot11RadioSSIDCfgEntry':hpnicfDot11RadioSSIDCfgEntry,_AI:hpnicfDot11RadioSSIDSerialID,_AJ:hpnicfDot11RadioSSIDRadioID,_AK:hpnicfDot11RadioSSIDWLANID,'hpnicfDot11RadioSSIDIndex':hpnicfDot11RadioSSIDIndex,'hpnicfDot11RadioBSSID':hpnicfDot11RadioBSSID,'hpnicfDot11RadioSSIDRowStatus':hpnicfDot11RadioSSIDRowStatus,'hpnicfDot11APSerialIDTable':hpnicfDot11APSerialIDTable,'hpnicfDot11APSerialIDEntry':hpnicfDot11APSerialIDEntry,_X:hpnicfDot11SIDAPSerialID,'hpnicfDot11SIDAPWorkMode':hpnicfDot11SIDAPWorkMode,'hpnicfDot11SIDAPGetIPMethod':hpnicfDot11SIDAPGetIPMethod,'hpnicfDot11SIDAPTemplateName':hpnicfDot11SIDAPTemplateName,'hpnicfDot11SIDModelAlias':hpnicfDot11SIDModelAlias,'hpnicfDot11SIDAPDescription':hpnicfDot11SIDAPDescription,'hpnicfDot11SIDRowStatus':hpnicfDot11SIDRowStatus,'hpnicfDot11SIDAPName':hpnicfDot11SIDAPName,'hpnicfDot11SIDStatisInterv':hpnicfDot11SIDStatisInterv,'hpnicfDot11SIDAPBroadcastProbeReply':hpnicfDot11SIDAPBroadcastProbeReply,'hpnicfDot11SIDAPStaIdleTimerInterv':hpnicfDot11SIDAPStaIdleTimerInterv,'hpnicfDot11SIDStaKeepAliveTimerInterv':hpnicfDot11SIDStaKeepAliveTimerInterv,'hpnicfDot11SIDAPCir':hpnicfDot11SIDAPCir,'hpnicfDot11SIDAPCbs':hpnicfDot11SIDAPCbs,'hpnicfDot11SIDAPPriorityLevel':hpnicfDot11SIDAPPriorityLevel,'hpnicfDot11SIDAPElementID':hpnicfDot11SIDAPElementID,'hpnicfDot11SIDAPDevDetectEnable':hpnicfDot11SIDAPDevDetectEnable,'hpnicfDot11SIDAPStatisIntervMode':hpnicfDot11SIDAPStatisIntervMode,'hpnicfDot11SIDAPWorkModeCM':hpnicfDot11SIDAPWorkModeCM,'hpnicfDot11APSTVlanTable':hpnicfDot11APSTVlanTable,'hpnicfDot11APSTVlanEntry':hpnicfDot11APSTVlanEntry,'hpnicfDot11CfgSTVLANID':hpnicfDot11CfgSTVLANID,'hpnicfDot11CfgSTNASPortID':hpnicfDot11CfgSTNASPortID,'hpnicfDot11CfgServiceSetRowStatus':hpnicfDot11CfgServiceSetRowStatus,'hpnicfDot11CfgSTNASID':hpnicfDot11CfgSTNASID,'hpnicfDot11RadioIntfConfigGroup':hpnicfDot11RadioIntfConfigGroup,'hpnicfDot11RadioIntfConfigTable':hpnicfDot11RadioIntfConfigTable,'hpnicfDot11RadioIntfConfigEntry':hpnicfDot11RadioIntfConfigEntry,_n:hpnicfDot11RadioIfIdx,'hpnicfDot11RadioCfgBeaconIntvl':hpnicfDot11RadioCfgBeaconIntvl,'hpnicfDot11RadioCfgDtimIntvl':hpnicfDot11RadioCfgDtimIntvl,'hpnicfDot11RadioCfgRtsThreshold':hpnicfDot11RadioCfgRtsThreshold,'hpnicfDot11RadioCfgFragThreshold':hpnicfDot11RadioCfgFragThreshold,'hpnicfDot11RadioCfgShtRetryThld':hpnicfDot11RadioCfgShtRetryThld,'hpnicfDot11RadioCfglongRtrThld':hpnicfDot11RadioCfglongRtrThld,'hpnicfDot11RadioCfgMaxRxLifetime':hpnicfDot11RadioCfgMaxRxLifetime,'hpnicfDot11RadioCfgType':hpnicfDot11RadioCfgType,'hpnicfDot11RadioCfgChannel':hpnicfDot11RadioCfgChannel,'hpnicfDot11RadioCfgMaxTxPwrLvl':hpnicfDot11RadioCfgMaxTxPwrLvl,'hpnicfDot11RadioCfgPreambleLen':hpnicfDot11RadioCfgPreambleLen,'hpnicfDot11RadioCfgWorkMode':hpnicfDot11RadioCfgWorkMode,'hpnicfDot11RadioCfgOnly11gEnable':hpnicfDot11RadioCfgOnly11gEnable,'hpnicfDot11RadioCfgType2':hpnicfDot11RadioCfgType2,'hpnicfDot11RadioCfgRssithresholdCM':hpnicfDot11RadioCfgRssithresholdCM,'hpnicfDot11RadioIntfBindTable':hpnicfDot11RadioIntfBindTable,'hpnicfDot11RadioIntfBindEntry':hpnicfDot11RadioIntfBindEntry,_AL:hpnicfDot11RadioIntfBindSvcPlcyID,'hpnicfDot11RadioIntfBindIfIdx':hpnicfDot11RadioIntfBindIfIdx,'hpnicfDot11RadioIntfBindRowStatus':hpnicfDot11RadioIntfBindRowStatus,'hpnicfDot11DataRateConfigGroup':hpnicfDot11DataRateConfigGroup,'hpnicfDot11DataRateConfigTable':hpnicfDot11DataRateConfigTable,'hpnicfDot11DataRateConfigEntry':hpnicfDot11DataRateConfigEntry,_AM:hpnicfDot11RadioTypeID,'hpnicfDot11SupportedRateSet':hpnicfDot11SupportedRateSet,'hpnicfDot11MandatoryRateSet':hpnicfDot11MandatoryRateSet,'hpnicfDot11DisabledRateSet':hpnicfDot11DisabledRateSet,'hpnicfDot11SmartRateSet':hpnicfDot11SmartRateSet,'hpnicfDot11InterfaceConfigGroup':hpnicfDot11InterfaceConfigGroup,'hpnicfDot11WlanEssIfTable':hpnicfDot11WlanEssIfTable,'hpnicfDot11WlanEssIfEntry':hpnicfDot11WlanEssIfEntry,_AN:hpnicfDot11WlanEssIfNumber,'hpnicfDot11WlanEssIfIndex':hpnicfDot11WlanEssIfIndex,'hpnicfDot11WlanEssRowStatus':hpnicfDot11WlanEssRowStatus,'hpnicfDot11WlanBssIfTable':hpnicfDot11WlanBssIfTable,'hpnicfDot11WlanBssIfEntry':hpnicfDot11WlanBssIfEntry,_AO:hpnicfDot11WlanBssIfNumber,'hpnicfDot11WlanBssIfIndex':hpnicfDot11WlanBssIfIndex,'hpnicfDot11WlanBssRowStatus':hpnicfDot11WlanBssRowStatus,'hpnicfDot11WLANEthernetIfTable':hpnicfDot11WLANEthernetIfTable,'hpnicfDot11WLANEthernetIfEntry':hpnicfDot11WLANEthernetIfEntry,_AP:hpnicfDot11WlanEthernetIfNumber,'hpnicfDot11WLANEthernetIfIndex':hpnicfDot11WLANEthernetIfIndex,'hpnicfDot11WlanEthernetRowStatus':hpnicfDot11WlanEthernetRowStatus,'hpnicfDot11PortSecurityTable':hpnicfDot11PortSecurityTable,'hpnicfDot11PortSecurityEntry':hpnicfDot11PortSecurityEntry,'hpnicfDot11PortSecurityMode':hpnicfDot11PortSecurityMode,'hpnicfDot11SecurityUserLoginTxKeyType':hpnicfDot11SecurityUserLoginTxKeyType,'hpnicfDot11SecurityPskKeyMode':hpnicfDot11SecurityPskKeyMode,'hpnicfDot11SecurityPskKeyString':hpnicfDot11SecurityPskKeyString,'hpnicfDot11WlanMeshIfTable':hpnicfDot11WlanMeshIfTable,'hpnicfDot11WlanMeshIfEntry':hpnicfDot11WlanMeshIfEntry,_AQ:hpnicfDot11WlanMeshIfNumber,'hpnicfDot11WlanMeshIfIndex':hpnicfDot11WlanMeshIfIndex,'hpnicfDot11WlanMeshRowStatus':hpnicfDot11WlanMeshRowStatus,'hpnicfDot11ACBackupGroup':hpnicfDot11ACBackupGroup,'hpnicfDot11BackupACAdrssIP':hpnicfDot11BackupACAdrssIP,'hpnicfDot11BackupACAdrssIPv6':hpnicfDot11BackupACAdrssIPv6,'hpnicfDot11RadioElementConfigGroup':hpnicfDot11RadioElementConfigGroup,'hpnicfDot11nRadioCfgTable':hpnicfDot11nRadioCfgTable,'hpnicfDot11nRadioCfgEntry':hpnicfDot11nRadioCfgEntry,_AR:hpnicfDot11nRadioCfgIndex,'hpnicfDot11nAMpduEnable':hpnicfDot11nAMpduEnable,'hpnicfDot11nAMsduEnable':hpnicfDot11nAMsduEnable,'hpnicfDot11nClientDot11nOnly':hpnicfDot11nClientDot11nOnly,'hpnicfDot11nChanelBand':hpnicfDot11nChanelBand,'hpnicfDot11nShortGiEnable':hpnicfDot11nShortGiEnable,'hpnicfDot11nClientDot11acOnly':hpnicfDot11nClientDot11acOnly,'hpnicfDot11RadioWDSTable':hpnicfDot11RadioWDSTable,'hpnicfDot11RadioWDSEntry':hpnicfDot11RadioWDSEntry,_AS:hpnicfDot11RadioWDSIndex,'hpnicfDot11RadioWDSMode':hpnicfDot11RadioWDSMode,'hpnicfDot11RadioWDSNetWorkID':hpnicfDot11RadioWDSNetWorkID,'hpnicfDot11WDSSecPskKeyMode':hpnicfDot11WDSSecPskKeyMode,'hpnicfDot11WDSSecPskKeyString':hpnicfDot11WDSSecPskKeyString,'hpnicfDot11nRadioCfg2Table':hpnicfDot11nRadioCfg2Table,'hpnicfDot11nRadioCfg2Entry':hpnicfDot11nRadioCfg2Entry,_AT:hpnicfDot11nRadioCfg2APIDIndex,_AU:hpnicfDot11nRadioCfg2RadioIDIndex,'hpnicfDot11nRadioCfg2AMpduEnable':hpnicfDot11nRadioCfg2AMpduEnable,'hpnicfDot11nRadioCfg2AMsduEnable':hpnicfDot11nRadioCfg2AMsduEnable,'hpnicfDot11nRadioCfg2ClientDot11nOnly':hpnicfDot11nRadioCfg2ClientDot11nOnly,'hpnicfDot11nRadioCfg2ChannelBand':hpnicfDot11nRadioCfg2ChannelBand,'hpnicfDot11nRadioCfg2ShortGiEnable':hpnicfDot11nRadioCfg2ShortGiEnable,'hpnicfDot11nRadioCfg2AMpduEnableCM':hpnicfDot11nRadioCfg2AMpduEnableCM,'hpnicfDot11nRadioCfg2ChannelBandCM':hpnicfDot11nRadioCfg2ChannelBandCM,'hpnicfDot11nRadioCfg2ShortGiEnableCM':hpnicfDot11nRadioCfg2ShortGiEnableCM,'hpnicfDot11nRadioCfg2ClientDot11acOnly':hpnicfDot11nRadioCfg2ClientDot11acOnly,'hpnicfDot11nRadioCfg2ClientDot11nOnlyCM':hpnicfDot11nRadioCfg2ClientDot11nOnlyCM,'hpnicfDot11CfgNotifyGroup':hpnicfDot11CfgNotifyGroup,'hpnicfDot11CfgNotifications':hpnicfDot11CfgNotifications,'hpnicfDot11CfgCipherChange':hpnicfDot11CfgCipherChange,'hpnicfDot11CfgPSKChange':hpnicfDot11CfgPSKChange,'hpnicfDot11SSIDWepIDConflictTrap':hpnicfDot11SSIDWepIDConflictTrap,'hpnicfDot11CfgTrapVarObjects':hpnicfDot11CfgTrapVarObjects,_AW:hpnicfDot11PreConflictTemplateNum,_AX:hpnicfDot11CurrConflictTemplateNum,_AY:hpnicfDot11ConflictCipherIdx,_AZ:hpnicfDot11ConfigureAPID,_Aa:hpnicfDot11ConfigureRadioID,_Ab:hpnicfDot11ConfigureAPMacAddress})