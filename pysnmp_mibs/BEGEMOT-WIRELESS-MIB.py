_u='wlanIfaceStatisticsEntry'
_t='wlanIfaceConfigEntry'
_s='wlanIfParentEntry'
_r='wlanMeshRouteDestination'
_q='wlanMeshNeighborAddress'
_p='wlanMACAccessControlMAC'
_o='wlanWepKeyID'
_n='wlanScanResultBssid'
_m='wlanScanResultID'
_l='wlanIfTxPhyMode'
_k='wlanIfRoamPhyMode'
_j='wlanIfaceChannelId'
_i='wlanIfacePeerAddress'
_h='monitor'
_g='hostAp'
_f='station'
_e='dot11g'
_d='dot11b'
_c='dot11a'
_b='shortPreamble'
_a='timeout'
_Z='cipherSuiteRejected'
_Y='akmpInvalid'
_X='groupCipherInvalid'
_W='notAssociated'
_V='unspecified'
_U='no-op'
_T='unknown'
_S='not-accessible'
_R='WlanIfaceDot11nPduType'
_Q='off'
_P='ibss'
_O='disabled'
_N='DisplayString'
_M='seconds'
_L='OctetString'
_K='read-create'
_J='Bits'
_I='TruthValue'
_H='milliseconds'
_G='wlanIfaceName'
_F='BEGEMOT-WIRELESS-MIB'
_E='Integer32'
_D='read-write'
_C='frames'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_L,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
begemot,=mibBuilder.importSymbols('BEGEMOT-MIB','begemot')
InterfaceIndex,ifIndex=mibBuilder.importSymbols('IF-MIB','InterfaceIndex','ifIndex')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso,mib_2=mibBuilder.importSymbols('SNMPv2-SMI',_J,'Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso','mib-2')
DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC',_N,'MacAddress','PhysAddress','RowStatus','TextualConvention',_I)
begemotWlan=ModuleIdentity((1,3,6,1,4,1,12325,1,210))
if mibBuilder.loadTexts:begemotWlan.setRevisions(('2010-05-17 00:00',))
class WlanMgmtReasonCode(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,13,14,15,16,17,18,19,20,21,22,23,24,32,33,34,35,36,37,38,39)));namedValues=NamedValues(*((_V,1),('authenticationExpire',2),('authenticationLeave',3),('associationExpire',4),('associationTooMany',5),('notAuthenticated',6),(_W,7),('associationLeave',8),('associationNotAuthenticated',9),('dissassocPwrcapBad',10),('dissassocSuperchanBad',11),('ieInvalid',13),('micFailure',14),('fourWayHandshakeTimeout',15),('groupKeyUpdateTimeout',16),('ieIn4FourWayDiffers',17),(_X,18),('pairwiseCiherInvalid',19),(_Y,20),('unsupportedRsnIeVersion',21),('invalidRsnIeCap',22),('dot1xAuthFailed',23),(_Z,24),('unspeciffiedQos',32),('insufficientBw',33),('tooManyFrames',34),('outsideTxOp',35),('leavingQbss',36),('badMechanism',37),('setupNeeded',38),(_a,39)))
class WlanMgmtMeshReasonCode(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(2,3,4,5,6,7,8,9,10,11,12,13)));namedValues=NamedValues(*(('peerLinkCancelled',2),('maxPeers',3),('cpViolation',4),('closeRcvd',5),('maxRetries',6),('confirmTimeout',7),('invalidGtk',8),('inconsistentParams',9),('invalidSecurity',10),('perrUnspecified',11),('perrNoFI',12),('perrDestUnreach',13)))
class WlanMgmtStatusCode(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,40,41,42,43,44,45,46)));namedValues=NamedValues(*(('success',0),(_V,1),('capabilitiesInfo',10),(_W,11),('other',12),('algorithm',13),('sequence',14),('challenge',15),(_a,16),('tooMany',17),('basicRate',18),('spRequired',19),('pbccRequired',20),('caRequired',21),('specMgmtRequired',22),('pwrcapRequire',23),('superchanRequired',24),('shortSlotRequired',25),('dssofdmRequired',26),('missingHTCaps',27),('invalidIE',40),(_X,41),('pairwiseCipherInvalid',42),(_Y,43),('unsupportedRsnIEVersion',44),('invalidRsnIECap',45),(_Z,46)))
class WlanRegDomainCode(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17)));namedValues=NamedValues(*(('fcc',1),('ca',2),('etsi',3),('etsi2',4),('etsi3',5),('fcc3',6),('japan',7),('korea',8),('apac',9),('apac2',10),('apac3',11),('row',12),('none',13),('debug',14),('sr9',15),('xr9',16),('gz901',17)))
class WlanIfaceDot11nPduType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*((_O,0),('rxOnly',1),('txOnly',2),('txAndRx',3)))
class WlanPeerCapabilityFlags(TextualConvention,Bits):status=_A;namedValues=NamedValues(*(('ess',1),(_P,2),('cfPollable',3),('cfPollRequest',4),('privacy',5),(_b,6),('pbcc',7),('channelAgility',8),('shortSlotTime',9),('rsn',10),('dsssofdm',11)))
class WlanIfPhyMode(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12)));namedValues=NamedValues(*(('auto',1),(_c,2),(_d,3),(_e,4),('fh',5),('turboA',6),('turboG',7),('sturboA',8),('dot11na',9),('dot11ng',10),('ofdmHalf',11),('ofdmQuarter',12)))
_BegemotWlanNotifications_ObjectIdentity=ObjectIdentity
begemotWlanNotifications=_BegemotWlanNotifications_ObjectIdentity((1,3,6,1,4,1,12325,1,210,0))
_BegemotWlanInterface_ObjectIdentity=ObjectIdentity
begemotWlanInterface=_BegemotWlanInterface_ObjectIdentity((1,3,6,1,4,1,12325,1,210,1))
_WlanInterfaceTable_Object=MibTable
wlanInterfaceTable=_WlanInterfaceTable_Object((1,3,6,1,4,1,12325,1,210,1,1))
if mibBuilder.loadTexts:wlanInterfaceTable.setStatus(_A)
_WlanInterfaceEntry_Object=MibTableRow
wlanInterfaceEntry=_WlanInterfaceEntry_Object((1,3,6,1,4,1,12325,1,210,1,1,1))
wlanInterfaceEntry.setIndexNames((0,_F,_G))
if mibBuilder.loadTexts:wlanInterfaceEntry.setStatus(_A)
_WlanIfaceIndex_Type=InterfaceIndex
_WlanIfaceIndex_Object=MibTableColumn
wlanIfaceIndex=_WlanIfaceIndex_Object((1,3,6,1,4,1,12325,1,210,1,1,1,1),_WlanIfaceIndex_Type())
wlanIfaceIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:wlanIfaceIndex.setStatus(_A)
class _WlanIfaceName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_WlanIfaceName_Type.__name__=_N
_WlanIfaceName_Object=MibTableColumn
wlanIfaceName=_WlanIfaceName_Object((1,3,6,1,4,1,12325,1,210,1,1,1,2),_WlanIfaceName_Type())
wlanIfaceName.setMaxAccess(_K)
if mibBuilder.loadTexts:wlanIfaceName.setStatus(_A)
class _WlanParentIfName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_WlanParentIfName_Type.__name__=_N
_WlanParentIfName_Object=MibTableColumn
wlanParentIfName=_WlanParentIfName_Object((1,3,6,1,4,1,12325,1,210,1,1,1,3),_WlanParentIfName_Type())
wlanParentIfName.setMaxAccess(_K)
if mibBuilder.loadTexts:wlanParentIfName.setStatus(_A)
class _WlanIfaceOperatingMode_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7)));namedValues=NamedValues(*((_P,0),(_f,1),('wds',2),('adhocDemo',3),(_g,4),(_h,5),('meshPoint',6),('tdma',7)))
_WlanIfaceOperatingMode_Type.__name__=_E
_WlanIfaceOperatingMode_Object=MibTableColumn
wlanIfaceOperatingMode=_WlanIfaceOperatingMode_Object((1,3,6,1,4,1,12325,1,210,1,1,1,4),_WlanIfaceOperatingMode_Type())
wlanIfaceOperatingMode.setMaxAccess(_K)
if mibBuilder.loadTexts:wlanIfaceOperatingMode.setStatus(_A)
class _WlanIfaceFlags_Type(Bits):namedValues=NamedValues(*(('uniqueBssid',1),('noBeacons',2),('wdsLegacy',3)))
_WlanIfaceFlags_Type.__name__=_J
_WlanIfaceFlags_Object=MibTableColumn
wlanIfaceFlags=_WlanIfaceFlags_Object((1,3,6,1,4,1,12325,1,210,1,1,1,5),_WlanIfaceFlags_Type())
wlanIfaceFlags.setMaxAccess(_K)
if mibBuilder.loadTexts:wlanIfaceFlags.setStatus(_A)
_WlanIfaceBssid_Type=MacAddress
_WlanIfaceBssid_Object=MibTableColumn
wlanIfaceBssid=_WlanIfaceBssid_Object((1,3,6,1,4,1,12325,1,210,1,1,1,6),_WlanIfaceBssid_Type())
wlanIfaceBssid.setMaxAccess(_K)
if mibBuilder.loadTexts:wlanIfaceBssid.setStatus(_A)
_WlanIfaceLocalAddress_Type=MacAddress
_WlanIfaceLocalAddress_Object=MibTableColumn
wlanIfaceLocalAddress=_WlanIfaceLocalAddress_Object((1,3,6,1,4,1,12325,1,210,1,1,1,7),_WlanIfaceLocalAddress_Type())
wlanIfaceLocalAddress.setMaxAccess(_K)
if mibBuilder.loadTexts:wlanIfaceLocalAddress.setStatus(_A)
_WlanIfaceStatus_Type=RowStatus
_WlanIfaceStatus_Object=MibTableColumn
wlanIfaceStatus=_WlanIfaceStatus_Object((1,3,6,1,4,1,12325,1,210,1,1,1,8),_WlanIfaceStatus_Type())
wlanIfaceStatus.setMaxAccess(_K)
if mibBuilder.loadTexts:wlanIfaceStatus.setStatus(_A)
class _WlanIfaceState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('up',1),('down',2)))
_WlanIfaceState_Type.__name__=_E
_WlanIfaceState_Object=MibTableColumn
wlanIfaceState=_WlanIfaceState_Object((1,3,6,1,4,1,12325,1,210,1,1,1,9),_WlanIfaceState_Type())
wlanIfaceState.setMaxAccess(_K)
if mibBuilder.loadTexts:wlanIfaceState.setStatus(_A)
_WlanIfParentTable_Object=MibTable
wlanIfParentTable=_WlanIfParentTable_Object((1,3,6,1,4,1,12325,1,210,1,2))
if mibBuilder.loadTexts:wlanIfParentTable.setStatus(_A)
_WlanIfParentEntry_Object=MibTableRow
wlanIfParentEntry=_WlanIfParentEntry_Object((1,3,6,1,4,1,12325,1,210,1,2,1))
if mibBuilder.loadTexts:wlanIfParentEntry.setStatus(_A)
class _WlanIfParentDriverCapabilities_Type(Bits):namedValues=NamedValues(*((_f,1),('ieee8023encap',2),('athFastFrames',3),('athTurbo',4),(_P,5),('pmgt',6),(_g,7),('ahDemo',8),('swRetry',9),('txPmgt',10),('shortSlot',11),(_b,12),(_h,13),('dfs',14),('mbss',15),('wpa1',16),('wpa2',17),('burst',18),('wme',19),('wds',20),('bgScan',21),('txFrag',22),('tdma',23)))
_WlanIfParentDriverCapabilities_Type.__name__=_J
_WlanIfParentDriverCapabilities_Object=MibTableColumn
wlanIfParentDriverCapabilities=_WlanIfParentDriverCapabilities_Object((1,3,6,1,4,1,12325,1,210,1,2,1,1),_WlanIfParentDriverCapabilities_Type())
wlanIfParentDriverCapabilities.setMaxAccess(_B)
if mibBuilder.loadTexts:wlanIfParentDriverCapabilities.setStatus(_A)
class _WlanIfParentCryptoCapabilities_Type(Bits):namedValues=NamedValues(*(('wep',1),('tkip',2),('aes',3),('aesCcm',4),('tkipMic',5),('ckip',6)))
_WlanIfParentCryptoCapabilities_Type.__name__=_J
_WlanIfParentCryptoCapabilities_Object=MibTableColumn
wlanIfParentCryptoCapabilities=_WlanIfParentCryptoCapabilities_Object((1,3,6,1,4,1,12325,1,210,1,2,1,2),_WlanIfParentCryptoCapabilities_Type())
wlanIfParentCryptoCapabilities.setMaxAccess(_B)
if mibBuilder.loadTexts:wlanIfParentCryptoCapabilities.setStatus(_A)
class _WlanIfParentHTCapabilities_Type(Bits):namedValues=NamedValues(*(('ldpc',1),('chwidth40',2),('greenField',3),('shortGi20',4),('shortGi40',5),('txStbc',6),('delba',7),('amsdu7935',8),('dssscck40',9),('psmp',10),('fortyMHzIntolerant',11),('lsigTxOpProt',12),('htcAmpdu',13),('htcAmsdu',14),('htcHt',15),('htcSmps',16),('htcRifs',17)))
_WlanIfParentHTCapabilities_Type.__name__=_J
_WlanIfParentHTCapabilities_Object=MibTableColumn
wlanIfParentHTCapabilities=_WlanIfParentHTCapabilities_Object((1,3,6,1,4,1,12325,1,210,1,2,1,3),_WlanIfParentHTCapabilities_Type())
wlanIfParentHTCapabilities.setMaxAccess(_B)
if mibBuilder.loadTexts:wlanIfParentHTCapabilities.setStatus(_A)
_WlanIfaceConfigTable_Object=MibTable
wlanIfaceConfigTable=_WlanIfaceConfigTable_Object((1,3,6,1,4,1,12325,1,210,1,3))
if mibBuilder.loadTexts:wlanIfaceConfigTable.setStatus(_A)
_WlanIfaceConfigEntry_Object=MibTableRow
wlanIfaceConfigEntry=_WlanIfaceConfigEntry_Object((1,3,6,1,4,1,12325,1,210,1,3,1))
if mibBuilder.loadTexts:wlanIfaceConfigEntry.setStatus(_A)
_WlanIfacePacketBurst_Type=TruthValue
_WlanIfacePacketBurst_Object=MibTableColumn
wlanIfacePacketBurst=_WlanIfacePacketBurst_Object((1,3,6,1,4,1,12325,1,210,1,3,1,1),_WlanIfacePacketBurst_Type())
wlanIfacePacketBurst.setMaxAccess(_D)
if mibBuilder.loadTexts:wlanIfacePacketBurst.setStatus(_A)
class _WlanIfaceCountryCode_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(3,3));fixedLength=3
_WlanIfaceCountryCode_Type.__name__=_L
_WlanIfaceCountryCode_Object=MibTableColumn
wlanIfaceCountryCode=_WlanIfaceCountryCode_Object((1,3,6,1,4,1,12325,1,210,1,3,1,2),_WlanIfaceCountryCode_Type())
wlanIfaceCountryCode.setMaxAccess(_D)
if mibBuilder.loadTexts:wlanIfaceCountryCode.setStatus(_A)
_WlanIfaceRegDomain_Type=WlanRegDomainCode
_WlanIfaceRegDomain_Object=MibTableColumn
wlanIfaceRegDomain=_WlanIfaceRegDomain_Object((1,3,6,1,4,1,12325,1,210,1,3,1,3),_WlanIfaceRegDomain_Type())
wlanIfaceRegDomain.setMaxAccess(_D)
if mibBuilder.loadTexts:wlanIfaceRegDomain.setStatus(_A)
class _WlanIfaceDesiredSsid_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_WlanIfaceDesiredSsid_Type.__name__=_L
_WlanIfaceDesiredSsid_Object=MibTableColumn
wlanIfaceDesiredSsid=_WlanIfaceDesiredSsid_Object((1,3,6,1,4,1,12325,1,210,1,3,1,4),_WlanIfaceDesiredSsid_Type())
wlanIfaceDesiredSsid.setMaxAccess(_D)
if mibBuilder.loadTexts:wlanIfaceDesiredSsid.setStatus(_A)
_WlanIfaceDesiredChannel_Type=Integer32
_WlanIfaceDesiredChannel_Object=MibTableColumn
wlanIfaceDesiredChannel=_WlanIfaceDesiredChannel_Object((1,3,6,1,4,1,12325,1,210,1,3,1,5),_WlanIfaceDesiredChannel_Type())
wlanIfaceDesiredChannel.setMaxAccess(_D)
if mibBuilder.loadTexts:wlanIfaceDesiredChannel.setStatus(_A)
class _WlanIfaceDynamicFreqSelection_Type(TruthValue):defaultValue=2
_WlanIfaceDynamicFreqSelection_Type.__name__=_I
_WlanIfaceDynamicFreqSelection_Object=MibTableColumn
wlanIfaceDynamicFreqSelection=_WlanIfaceDynamicFreqSelection_Object((1,3,6,1,4,1,12325,1,210,1,3,1,6),_WlanIfaceDynamicFreqSelection_Type())
wlanIfaceDynamicFreqSelection.setMaxAccess(_D)
if mibBuilder.loadTexts:wlanIfaceDynamicFreqSelection.setStatus(_A)
_WlanIfaceFastFrames_Type=TruthValue
_WlanIfaceFastFrames_Object=MibTableColumn
wlanIfaceFastFrames=_WlanIfaceFastFrames_Object((1,3,6,1,4,1,12325,1,210,1,3,1,7),_WlanIfaceFastFrames_Type())
wlanIfaceFastFrames.setMaxAccess(_D)
if mibBuilder.loadTexts:wlanIfaceFastFrames.setStatus(_A)
_WlanIfaceDturbo_Type=TruthValue
_WlanIfaceDturbo_Object=MibTableColumn
wlanIfaceDturbo=_WlanIfaceDturbo_Object((1,3,6,1,4,1,12325,1,210,1,3,1,8),_WlanIfaceDturbo_Type())
wlanIfaceDturbo.setMaxAccess(_D)
if mibBuilder.loadTexts:wlanIfaceDturbo.setStatus(_A)
_WlanIfaceTxPower_Type=Integer32
_WlanIfaceTxPower_Object=MibTableColumn
wlanIfaceTxPower=_WlanIfaceTxPower_Object((1,3,6,1,4,1,12325,1,210,1,3,1,9),_WlanIfaceTxPower_Type())
wlanIfaceTxPower.setMaxAccess(_D)
if mibBuilder.loadTexts:wlanIfaceTxPower.setStatus(_A)
class _WlanIfaceFragmentThreshold_Type(Integer32):defaultValue=2346;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(256,2346))
_WlanIfaceFragmentThreshold_Type.__name__=_E
_WlanIfaceFragmentThreshold_Object=MibTableColumn
wlanIfaceFragmentThreshold=_WlanIfaceFragmentThreshold_Object((1,3,6,1,4,1,12325,1,210,1,3,1,10),_WlanIfaceFragmentThreshold_Type())
wlanIfaceFragmentThreshold.setMaxAccess(_D)
if mibBuilder.loadTexts:wlanIfaceFragmentThreshold.setStatus(_A)
class _WlanIfaceRTSThreshold_Type(Integer32):defaultValue=2346;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2346))
_WlanIfaceRTSThreshold_Type.__name__=_E
_WlanIfaceRTSThreshold_Object=MibTableColumn
wlanIfaceRTSThreshold=_WlanIfaceRTSThreshold_Object((1,3,6,1,4,1,12325,1,210,1,3,1,11),_WlanIfaceRTSThreshold_Type())
wlanIfaceRTSThreshold.setMaxAccess(_D)
if mibBuilder.loadTexts:wlanIfaceRTSThreshold.setStatus(_A)
if mibBuilder.loadTexts:wlanIfaceRTSThreshold.setUnits('bytes')
_WlanIfaceWlanPrivacySubscribe_Type=TruthValue
_WlanIfaceWlanPrivacySubscribe_Object=MibTableColumn
wlanIfaceWlanPrivacySubscribe=_WlanIfaceWlanPrivacySubscribe_Object((1,3,6,1,4,1,12325,1,210,1,3,1,12),_WlanIfaceWlanPrivacySubscribe_Type())
wlanIfaceWlanPrivacySubscribe.setMaxAccess(_D)
if mibBuilder.loadTexts:wlanIfaceWlanPrivacySubscribe.setStatus(_A)
_WlanIfaceBgScan_Type=TruthValue
_WlanIfaceBgScan_Object=MibTableColumn
wlanIfaceBgScan=_WlanIfaceBgScan_Object((1,3,6,1,4,1,12325,1,210,1,3,1,13),_WlanIfaceBgScan_Type())
wlanIfaceBgScan.setMaxAccess(_D)
if mibBuilder.loadTexts:wlanIfaceBgScan.setStatus(_A)
class _WlanIfaceBgScanIdle_Type(Integer32):defaultValue=250
_WlanIfaceBgScanIdle_Type.__name__=_E
_WlanIfaceBgScanIdle_Object=MibTableColumn
wlanIfaceBgScanIdle=_WlanIfaceBgScanIdle_Object((1,3,6,1,4,1,12325,1,210,1,3,1,14),_WlanIfaceBgScanIdle_Type())
wlanIfaceBgScanIdle.setMaxAccess(_D)
if mibBuilder.loadTexts:wlanIfaceBgScanIdle.setStatus(_A)
if mibBuilder.loadTexts:wlanIfaceBgScanIdle.setUnits(_H)
class _WlanIfaceBgScanInterval_Type(Integer32):defaultValue=300
_WlanIfaceBgScanInterval_Type.__name__=_E
_WlanIfaceBgScanInterval_Object=MibTableColumn
wlanIfaceBgScanInterval=_WlanIfaceBgScanInterval_Object((1,3,6,1,4,1,12325,1,210,1,3,1,15),_WlanIfaceBgScanInterval_Type())
wlanIfaceBgScanInterval.setMaxAccess(_D)
if mibBuilder.loadTexts:wlanIfaceBgScanInterval.setStatus(_A)
if mibBuilder.loadTexts:wlanIfaceBgScanInterval.setUnits(_M)
class _WlanIfaceBeaconMissedThreshold_Type(Integer32):defaultValue=7;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_WlanIfaceBeaconMissedThreshold_Type.__name__=_E
_WlanIfaceBeaconMissedThreshold_Object=MibTableColumn
wlanIfaceBeaconMissedThreshold=_WlanIfaceBeaconMissedThreshold_Object((1,3,6,1,4,1,12325,1,210,1,3,1,16),_WlanIfaceBeaconMissedThreshold_Type())
wlanIfaceBeaconMissedThreshold.setMaxAccess(_D)
if mibBuilder.loadTexts:wlanIfaceBeaconMissedThreshold.setStatus(_A)
if mibBuilder.loadTexts:wlanIfaceBeaconMissedThreshold.setUnits(_C)
_WlanIfaceDesiredBssid_Type=MacAddress
_WlanIfaceDesiredBssid_Object=MibTableColumn
wlanIfaceDesiredBssid=_WlanIfaceDesiredBssid_Object((1,3,6,1,4,1,12325,1,210,1,3,1,17),_WlanIfaceDesiredBssid_Type())
wlanIfaceDesiredBssid.setMaxAccess(_D)
if mibBuilder.loadTexts:wlanIfaceDesiredBssid.setStatus(_A)
class _WlanIfaceRoamingMode_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('device',1),('auto',2),('manual',3)))
_WlanIfaceRoamingMode_Type.__name__=_E
_WlanIfaceRoamingMode_Object=MibTableColumn
wlanIfaceRoamingMode=_WlanIfaceRoamingMode_Object((1,3,6,1,4,1,12325,1,210,1,3,1,18),_WlanIfaceRoamingMode_Type())
wlanIfaceRoamingMode.setMaxAccess(_D)
if mibBuilder.loadTexts:wlanIfaceRoamingMode.setStatus(_A)
class _WlanIfaceDot11d_Type(TruthValue):defaultValue=2
_WlanIfaceDot11d_Type.__name__=_I
_WlanIfaceDot11d_Object=MibTableColumn
wlanIfaceDot11d=_WlanIfaceDot11d_Object((1,3,6,1,4,1,12325,1,210,1,3,1,19),_WlanIfaceDot11d_Type())
wlanIfaceDot11d.setMaxAccess(_D)
if mibBuilder.loadTexts:wlanIfaceDot11d.setStatus(_A)
class _WlanIfaceDot11h_Type(TruthValue):defaultValue=2
_WlanIfaceDot11h_Type.__name__=_I
_WlanIfaceDot11h_Object=MibTableColumn
wlanIfaceDot11h=_WlanIfaceDot11h_Object((1,3,6,1,4,1,12325,1,210,1,3,1,20),_WlanIfaceDot11h_Type())
wlanIfaceDot11h.setMaxAccess(_D)
if mibBuilder.loadTexts:wlanIfaceDot11h.setStatus(_A)
_WlanIfaceDynamicWds_Type=TruthValue
_WlanIfaceDynamicWds_Object=MibTableColumn
wlanIfaceDynamicWds=_WlanIfaceDynamicWds_Object((1,3,6,1,4,1,12325,1,210,1,3,1,21),_WlanIfaceDynamicWds_Type())
wlanIfaceDynamicWds.setMaxAccess(_D)
if mibBuilder.loadTexts:wlanIfaceDynamicWds.setStatus(_A)
_WlanIfacePowerSave_Type=TruthValue
_WlanIfacePowerSave_Object=MibTableColumn
wlanIfacePowerSave=_WlanIfacePowerSave_Object((1,3,6,1,4,1,12325,1,210,1,3,1,22),_WlanIfacePowerSave_Type())
wlanIfacePowerSave.setMaxAccess(_D)
if mibBuilder.loadTexts:wlanIfacePowerSave.setStatus(_A)
class _WlanIfaceApBridge_Type(TruthValue):defaultValue=1
_WlanIfaceApBridge_Type.__name__=_I
_WlanIfaceApBridge_Object=MibTableColumn
wlanIfaceApBridge=_WlanIfaceApBridge_Object((1,3,6,1,4,1,12325,1,210,1,3,1,23),_WlanIfaceApBridge_Type())
wlanIfaceApBridge.setMaxAccess(_D)
if mibBuilder.loadTexts:wlanIfaceApBridge.setStatus(_A)
class _WlanIfaceBeaconInterval_Type(Integer32):defaultValue=100;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(25,1000))
_WlanIfaceBeaconInterval_Type.__name__=_E
_WlanIfaceBeaconInterval_Object=MibTableColumn
wlanIfaceBeaconInterval=_WlanIfaceBeaconInterval_Object((1,3,6,1,4,1,12325,1,210,1,3,1,24),_WlanIfaceBeaconInterval_Type())
wlanIfaceBeaconInterval.setMaxAccess(_D)
if mibBuilder.loadTexts:wlanIfaceBeaconInterval.setStatus(_A)
class _WlanIfaceDtimPeriod_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,15))
_WlanIfaceDtimPeriod_Type.__name__=_E
_WlanIfaceDtimPeriod_Object=MibTableColumn
wlanIfaceDtimPeriod=_WlanIfaceDtimPeriod_Object((1,3,6,1,4,1,12325,1,210,1,3,1,25),_WlanIfaceDtimPeriod_Type())
wlanIfaceDtimPeriod.setMaxAccess(_D)
if mibBuilder.loadTexts:wlanIfaceDtimPeriod.setStatus(_A)
class _WlanIfaceHideSsid_Type(TruthValue):defaultValue=2
_WlanIfaceHideSsid_Type.__name__=_I
_WlanIfaceHideSsid_Object=MibTableColumn
wlanIfaceHideSsid=_WlanIfaceHideSsid_Object((1,3,6,1,4,1,12325,1,210,1,3,1,26),_WlanIfaceHideSsid_Type())
wlanIfaceHideSsid.setMaxAccess(_D)
if mibBuilder.loadTexts:wlanIfaceHideSsid.setStatus(_A)
class _WlanIfaceInactivityProccess_Type(TruthValue):defaultValue=1
_WlanIfaceInactivityProccess_Type.__name__=_I
_WlanIfaceInactivityProccess_Object=MibTableColumn
wlanIfaceInactivityProccess=_WlanIfaceInactivityProccess_Object((1,3,6,1,4,1,12325,1,210,1,3,1,27),_WlanIfaceInactivityProccess_Type())
wlanIfaceInactivityProccess.setMaxAccess(_D)
if mibBuilder.loadTexts:wlanIfaceInactivityProccess.setStatus(_A)
class _WlanIfaceDot11gProtMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_Q,1),('cts',2),('rtscts',3)))
_WlanIfaceDot11gProtMode_Type.__name__=_E
_WlanIfaceDot11gProtMode_Object=MibTableColumn
wlanIfaceDot11gProtMode=_WlanIfaceDot11gProtMode_Object((1,3,6,1,4,1,12325,1,210,1,3,1,28),_WlanIfaceDot11gProtMode_Type())
wlanIfaceDot11gProtMode.setMaxAccess(_D)
if mibBuilder.loadTexts:wlanIfaceDot11gProtMode.setStatus(_A)
_WlanIfaceDot11gPureMode_Type=TruthValue
_WlanIfaceDot11gPureMode_Object=MibTableColumn
wlanIfaceDot11gPureMode=_WlanIfaceDot11gPureMode_Object((1,3,6,1,4,1,12325,1,210,1,3,1,29),_WlanIfaceDot11gPureMode_Type())
wlanIfaceDot11gPureMode.setMaxAccess(_D)
if mibBuilder.loadTexts:wlanIfaceDot11gPureMode.setStatus(_A)
_WlanIfaceDot11nPureMode_Type=TruthValue
_WlanIfaceDot11nPureMode_Object=MibTableColumn
wlanIfaceDot11nPureMode=_WlanIfaceDot11nPureMode_Object((1,3,6,1,4,1,12325,1,210,1,3,1,30),_WlanIfaceDot11nPureMode_Type())
wlanIfaceDot11nPureMode.setMaxAccess(_D)
if mibBuilder.loadTexts:wlanIfaceDot11nPureMode.setStatus(_A)
class _WlanIfaceDot11nAmpdu_Type(WlanIfaceDot11nPduType):defaultValue=3
_WlanIfaceDot11nAmpdu_Type.__name__=_R
_WlanIfaceDot11nAmpdu_Object=MibTableColumn
wlanIfaceDot11nAmpdu=_WlanIfaceDot11nAmpdu_Object((1,3,6,1,4,1,12325,1,210,1,3,1,31),_WlanIfaceDot11nAmpdu_Type())
wlanIfaceDot11nAmpdu.setMaxAccess(_D)
if mibBuilder.loadTexts:wlanIfaceDot11nAmpdu.setStatus(_A)
class _WlanIfaceDot11nAmpduDensity_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(25,25),ValueRangeConstraint(50,50),ValueRangeConstraint(100,100),ValueRangeConstraint(200,200),ValueRangeConstraint(400,400),ValueRangeConstraint(800,800),ValueRangeConstraint(1600,1600))
_WlanIfaceDot11nAmpduDensity_Type.__name__=_E
_WlanIfaceDot11nAmpduDensity_Object=MibTableColumn
wlanIfaceDot11nAmpduDensity=_WlanIfaceDot11nAmpduDensity_Object((1,3,6,1,4,1,12325,1,210,1,3,1,32),_WlanIfaceDot11nAmpduDensity_Type())
wlanIfaceDot11nAmpduDensity.setMaxAccess(_D)
if mibBuilder.loadTexts:wlanIfaceDot11nAmpduDensity.setStatus(_A)
if mibBuilder.loadTexts:wlanIfaceDot11nAmpduDensity.setUnits('1/100ths-of-microsecond')
class _WlanIfaceDot11nAmpduLimit_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(8192,8192),ValueRangeConstraint(16384,16384),ValueRangeConstraint(32768,32768),ValueRangeConstraint(65536,65536))
_WlanIfaceDot11nAmpduLimit_Type.__name__=_E
_WlanIfaceDot11nAmpduLimit_Object=MibTableColumn
wlanIfaceDot11nAmpduLimit=_WlanIfaceDot11nAmpduLimit_Object((1,3,6,1,4,1,12325,1,210,1,3,1,33),_WlanIfaceDot11nAmpduLimit_Type())
wlanIfaceDot11nAmpduLimit.setMaxAccess(_D)
if mibBuilder.loadTexts:wlanIfaceDot11nAmpduLimit.setStatus(_A)
class _WlanIfaceDot11nAmsdu_Type(WlanIfaceDot11nPduType):defaultValue=1
_WlanIfaceDot11nAmsdu_Type.__name__=_R
_WlanIfaceDot11nAmsdu_Object=MibTableColumn
wlanIfaceDot11nAmsdu=_WlanIfaceDot11nAmsdu_Object((1,3,6,1,4,1,12325,1,210,1,3,1,34),_WlanIfaceDot11nAmsdu_Type())
wlanIfaceDot11nAmsdu.setMaxAccess(_D)
if mibBuilder.loadTexts:wlanIfaceDot11nAmsdu.setStatus(_A)
class _WlanIfaceDot11nAmsduLimit_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(3839,3839),ValueRangeConstraint(7935,7935))
_WlanIfaceDot11nAmsduLimit_Type.__name__=_E
_WlanIfaceDot11nAmsduLimit_Object=MibTableColumn
wlanIfaceDot11nAmsduLimit=_WlanIfaceDot11nAmsduLimit_Object((1,3,6,1,4,1,12325,1,210,1,3,1,35),_WlanIfaceDot11nAmsduLimit_Type())
wlanIfaceDot11nAmsduLimit.setMaxAccess(_D)
if mibBuilder.loadTexts:wlanIfaceDot11nAmsduLimit.setStatus(_A)
class _WlanIfaceDot11nHighThroughput_Type(TruthValue):defaultValue=1
_WlanIfaceDot11nHighThroughput_Type.__name__=_I
_WlanIfaceDot11nHighThroughput_Object=MibTableColumn
wlanIfaceDot11nHighThroughput=_WlanIfaceDot11nHighThroughput_Object((1,3,6,1,4,1,12325,1,210,1,3,1,36),_WlanIfaceDot11nHighThroughput_Type())
wlanIfaceDot11nHighThroughput.setMaxAccess(_D)
if mibBuilder.loadTexts:wlanIfaceDot11nHighThroughput.setStatus(_A)
class _WlanIfaceDot11nHTCompatible_Type(TruthValue):defaultValue=1
_WlanIfaceDot11nHTCompatible_Type.__name__=_I
_WlanIfaceDot11nHTCompatible_Object=MibTableColumn
wlanIfaceDot11nHTCompatible=_WlanIfaceDot11nHTCompatible_Object((1,3,6,1,4,1,12325,1,210,1,3,1,37),_WlanIfaceDot11nHTCompatible_Type())
wlanIfaceDot11nHTCompatible.setMaxAccess(_D)
if mibBuilder.loadTexts:wlanIfaceDot11nHTCompatible.setStatus(_A)
class _WlanIfaceDot11nHTProtMode_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_Q,1),('rts',2)))
_WlanIfaceDot11nHTProtMode_Type.__name__=_E
_WlanIfaceDot11nHTProtMode_Object=MibTableColumn
wlanIfaceDot11nHTProtMode=_WlanIfaceDot11nHTProtMode_Object((1,3,6,1,4,1,12325,1,210,1,3,1,38),_WlanIfaceDot11nHTProtMode_Type())
wlanIfaceDot11nHTProtMode.setMaxAccess(_D)
if mibBuilder.loadTexts:wlanIfaceDot11nHTProtMode.setStatus(_A)
_WlanIfaceDot11nRIFS_Type=TruthValue
_WlanIfaceDot11nRIFS_Object=MibTableColumn
wlanIfaceDot11nRIFS=_WlanIfaceDot11nRIFS_Object((1,3,6,1,4,1,12325,1,210,1,3,1,39),_WlanIfaceDot11nRIFS_Type())
wlanIfaceDot11nRIFS.setMaxAccess(_D)
if mibBuilder.loadTexts:wlanIfaceDot11nRIFS.setStatus(_A)
_WlanIfaceDot11nShortGI_Type=TruthValue
_WlanIfaceDot11nShortGI_Object=MibTableColumn
wlanIfaceDot11nShortGI=_WlanIfaceDot11nShortGI_Object((1,3,6,1,4,1,12325,1,210,1,3,1,40),_WlanIfaceDot11nShortGI_Type())
wlanIfaceDot11nShortGI.setMaxAccess(_D)
if mibBuilder.loadTexts:wlanIfaceDot11nShortGI.setStatus(_A)
class _WlanIfaceDot11nSMPSMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_O,1),('static',2),('dynamic',3)))
_WlanIfaceDot11nSMPSMode_Type.__name__=_E
_WlanIfaceDot11nSMPSMode_Object=MibTableColumn
wlanIfaceDot11nSMPSMode=_WlanIfaceDot11nSMPSMode_Object((1,3,6,1,4,1,12325,1,210,1,3,1,41),_WlanIfaceDot11nSMPSMode_Type())
wlanIfaceDot11nSMPSMode.setMaxAccess(_D)
if mibBuilder.loadTexts:wlanIfaceDot11nSMPSMode.setStatus(_A)
class _WlanIfaceTdmaSlot_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2))
_WlanIfaceTdmaSlot_Type.__name__=_E
_WlanIfaceTdmaSlot_Object=MibTableColumn
wlanIfaceTdmaSlot=_WlanIfaceTdmaSlot_Object((1,3,6,1,4,1,12325,1,210,1,3,1,42),_WlanIfaceTdmaSlot_Type())
wlanIfaceTdmaSlot.setMaxAccess(_D)
if mibBuilder.loadTexts:wlanIfaceTdmaSlot.setStatus(_A)
class _WlanIfaceTdmaSlotCount_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2))
_WlanIfaceTdmaSlotCount_Type.__name__=_E
_WlanIfaceTdmaSlotCount_Object=MibTableColumn
wlanIfaceTdmaSlotCount=_WlanIfaceTdmaSlotCount_Object((1,3,6,1,4,1,12325,1,210,1,3,1,43),_WlanIfaceTdmaSlotCount_Type())
wlanIfaceTdmaSlotCount.setMaxAccess(_D)
if mibBuilder.loadTexts:wlanIfaceTdmaSlotCount.setStatus(_A)
class _WlanIfaceTdmaSlotLength_Type(Integer32):defaultValue=10000;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(150,65000))
_WlanIfaceTdmaSlotLength_Type.__name__=_E
_WlanIfaceTdmaSlotLength_Object=MibTableColumn
wlanIfaceTdmaSlotLength=_WlanIfaceTdmaSlotLength_Object((1,3,6,1,4,1,12325,1,210,1,3,1,44),_WlanIfaceTdmaSlotLength_Type())
wlanIfaceTdmaSlotLength.setMaxAccess(_D)
if mibBuilder.loadTexts:wlanIfaceTdmaSlotLength.setStatus(_A)
if mibBuilder.loadTexts:wlanIfaceTdmaSlotLength.setUnits('microseconds')
class _WlanIfaceTdmaBeaconInterval_Type(Integer32):defaultValue=5
_WlanIfaceTdmaBeaconInterval_Type.__name__=_E
_WlanIfaceTdmaBeaconInterval_Object=MibTableColumn
wlanIfaceTdmaBeaconInterval=_WlanIfaceTdmaBeaconInterval_Object((1,3,6,1,4,1,12325,1,210,1,3,1,45),_WlanIfaceTdmaBeaconInterval_Type())
wlanIfaceTdmaBeaconInterval.setMaxAccess(_D)
if mibBuilder.loadTexts:wlanIfaceTdmaBeaconInterval.setStatus(_A)
_WlanIfacePeerTable_Object=MibTable
wlanIfacePeerTable=_WlanIfacePeerTable_Object((1,3,6,1,4,1,12325,1,210,1,4))
if mibBuilder.loadTexts:wlanIfacePeerTable.setStatus(_A)
_WlanIfacePeerEntry_Object=MibTableRow
wlanIfacePeerEntry=_WlanIfacePeerEntry_Object((1,3,6,1,4,1,12325,1,210,1,4,1))
wlanIfacePeerEntry.setIndexNames((0,_F,_G),(0,_F,_i))
if mibBuilder.loadTexts:wlanIfacePeerEntry.setStatus(_A)
_WlanIfacePeerAddress_Type=MacAddress
_WlanIfacePeerAddress_Object=MibTableColumn
wlanIfacePeerAddress=_WlanIfacePeerAddress_Object((1,3,6,1,4,1,12325,1,210,1,4,1,1),_WlanIfacePeerAddress_Type())
wlanIfacePeerAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:wlanIfacePeerAddress.setStatus(_A)
_WlanIfacePeerAssociationId_Type=Integer32
_WlanIfacePeerAssociationId_Object=MibTableColumn
wlanIfacePeerAssociationId=_WlanIfacePeerAssociationId_Object((1,3,6,1,4,1,12325,1,210,1,4,1,2),_WlanIfacePeerAssociationId_Type())
wlanIfacePeerAssociationId.setMaxAccess(_B)
if mibBuilder.loadTexts:wlanIfacePeerAssociationId.setStatus(_A)
class _WlanIfacePeerVlanTag_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4096))
_WlanIfacePeerVlanTag_Type.__name__=_E
_WlanIfacePeerVlanTag_Object=MibTableColumn
wlanIfacePeerVlanTag=_WlanIfacePeerVlanTag_Object((1,3,6,1,4,1,12325,1,210,1,4,1,3),_WlanIfacePeerVlanTag_Type())
wlanIfacePeerVlanTag.setMaxAccess(_D)
if mibBuilder.loadTexts:wlanIfacePeerVlanTag.setStatus(_A)
_WlanIfacePeerFrequency_Type=Integer32
_WlanIfacePeerFrequency_Object=MibTableColumn
wlanIfacePeerFrequency=_WlanIfacePeerFrequency_Object((1,3,6,1,4,1,12325,1,210,1,4,1,4),_WlanIfacePeerFrequency_Type())
wlanIfacePeerFrequency.setMaxAccess(_B)
if mibBuilder.loadTexts:wlanIfacePeerFrequency.setStatus(_A)
_WlanIfacePeerCurrentTXRate_Type=Integer32
_WlanIfacePeerCurrentTXRate_Object=MibTableColumn
wlanIfacePeerCurrentTXRate=_WlanIfacePeerCurrentTXRate_Object((1,3,6,1,4,1,12325,1,210,1,4,1,5),_WlanIfacePeerCurrentTXRate_Type())
wlanIfacePeerCurrentTXRate.setMaxAccess(_B)
if mibBuilder.loadTexts:wlanIfacePeerCurrentTXRate.setStatus(_A)
_WlanIfacePeerRxSignalStrength_Type=Integer32
_WlanIfacePeerRxSignalStrength_Object=MibTableColumn
wlanIfacePeerRxSignalStrength=_WlanIfacePeerRxSignalStrength_Object((1,3,6,1,4,1,12325,1,210,1,4,1,6),_WlanIfacePeerRxSignalStrength_Type())
wlanIfacePeerRxSignalStrength.setMaxAccess(_B)
if mibBuilder.loadTexts:wlanIfacePeerRxSignalStrength.setStatus(_A)
_WlanIfacePeerIdleTimer_Type=Integer32
_WlanIfacePeerIdleTimer_Object=MibTableColumn
wlanIfacePeerIdleTimer=_WlanIfacePeerIdleTimer_Object((1,3,6,1,4,1,12325,1,210,1,4,1,7),_WlanIfacePeerIdleTimer_Type())
wlanIfacePeerIdleTimer.setMaxAccess(_B)
if mibBuilder.loadTexts:wlanIfacePeerIdleTimer.setStatus(_A)
if mibBuilder.loadTexts:wlanIfacePeerIdleTimer.setUnits(_M)
_WlanIfacePeerTxSequenceNo_Type=Integer32
_WlanIfacePeerTxSequenceNo_Object=MibTableColumn
wlanIfacePeerTxSequenceNo=_WlanIfacePeerTxSequenceNo_Object((1,3,6,1,4,1,12325,1,210,1,4,1,8),_WlanIfacePeerTxSequenceNo_Type())
wlanIfacePeerTxSequenceNo.setMaxAccess(_B)
if mibBuilder.loadTexts:wlanIfacePeerTxSequenceNo.setStatus(_A)
_WlanIfacePeerRxSequenceNo_Type=Integer32
_WlanIfacePeerRxSequenceNo_Object=MibTableColumn
wlanIfacePeerRxSequenceNo=_WlanIfacePeerRxSequenceNo_Object((1,3,6,1,4,1,12325,1,210,1,4,1,9),_WlanIfacePeerRxSequenceNo_Type())
wlanIfacePeerRxSequenceNo.setMaxAccess(_B)
if mibBuilder.loadTexts:wlanIfacePeerRxSequenceNo.setStatus(_A)
_WlanIfacePeerTxPower_Type=Integer32
_WlanIfacePeerTxPower_Object=MibTableColumn
wlanIfacePeerTxPower=_WlanIfacePeerTxPower_Object((1,3,6,1,4,1,12325,1,210,1,4,1,10),_WlanIfacePeerTxPower_Type())
wlanIfacePeerTxPower.setMaxAccess(_B)
if mibBuilder.loadTexts:wlanIfacePeerTxPower.setStatus(_A)
_WlanIfacePeerCapabilities_Type=WlanPeerCapabilityFlags
_WlanIfacePeerCapabilities_Object=MibTableColumn
wlanIfacePeerCapabilities=_WlanIfacePeerCapabilities_Object((1,3,6,1,4,1,12325,1,210,1,4,1,11),_WlanIfacePeerCapabilities_Type())
wlanIfacePeerCapabilities.setMaxAccess(_B)
if mibBuilder.loadTexts:wlanIfacePeerCapabilities.setStatus(_A)
class _WlanIfacePeerFlags_Type(Bits):namedValues=NamedValues(*(('authorizedForData',1),('qosEnabled',2),('erpEnabled',3),('powerSaveMode',4),('authRefHeld',5),('htEnabled',6),('htCompat',7),('wpsAssoc',8),('tsnAssoc',9),('ampduRx',10),('ampduTx',11),('mimoPowerSave',12),('sendRts',13),('rifs',14),('shortGiHT20',15),('shortGiHT40',16),('amsduRx',17),('amsduTx',18)))
_WlanIfacePeerFlags_Type.__name__=_J
_WlanIfacePeerFlags_Object=MibTableColumn
wlanIfacePeerFlags=_WlanIfacePeerFlags_Object((1,3,6,1,4,1,12325,1,210,1,4,1,12),_WlanIfacePeerFlags_Type())
wlanIfacePeerFlags.setMaxAccess(_B)
if mibBuilder.loadTexts:wlanIfacePeerFlags.setStatus(_A)
_WlanIfaceChannelTable_Object=MibTable
wlanIfaceChannelTable=_WlanIfaceChannelTable_Object((1,3,6,1,4,1,12325,1,210,1,5))
if mibBuilder.loadTexts:wlanIfaceChannelTable.setStatus(_A)
_WlanIfaceChannelEntry_Object=MibTableRow
wlanIfaceChannelEntry=_WlanIfaceChannelEntry_Object((1,3,6,1,4,1,12325,1,210,1,5,1))
wlanIfaceChannelEntry.setIndexNames((0,_F,_G),(0,_F,_j))
if mibBuilder.loadTexts:wlanIfaceChannelEntry.setStatus(_A)
class _WlanIfaceChannelId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1536))
_WlanIfaceChannelId_Type.__name__=_E
_WlanIfaceChannelId_Object=MibTableColumn
wlanIfaceChannelId=_WlanIfaceChannelId_Object((1,3,6,1,4,1,12325,1,210,1,5,1,1),_WlanIfaceChannelId_Type())
wlanIfaceChannelId.setMaxAccess(_S)
if mibBuilder.loadTexts:wlanIfaceChannelId.setStatus(_A)
class _WlanIfaceChannelIeeeId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,256))
_WlanIfaceChannelIeeeId_Type.__name__=_E
_WlanIfaceChannelIeeeId_Object=MibTableColumn
wlanIfaceChannelIeeeId=_WlanIfaceChannelIeeeId_Object((1,3,6,1,4,1,12325,1,210,1,5,1,2),_WlanIfaceChannelIeeeId_Type())
wlanIfaceChannelIeeeId.setMaxAccess(_B)
if mibBuilder.loadTexts:wlanIfaceChannelIeeeId.setStatus(_A)
class _WlanIfaceChannelType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8)));namedValues=NamedValues(*(('fhss',1),(_c,2),(_d,3),(_e,4),('tenMHz',5),('fiveMHz',6),('turbo',7),('ht',8)))
_WlanIfaceChannelType_Type.__name__=_E
_WlanIfaceChannelType_Object=MibTableColumn
wlanIfaceChannelType=_WlanIfaceChannelType_Object((1,3,6,1,4,1,12325,1,210,1,5,1,3),_WlanIfaceChannelType_Type())
wlanIfaceChannelType.setMaxAccess(_B)
if mibBuilder.loadTexts:wlanIfaceChannelType.setStatus(_A)
class _WlanIfaceChannelFlags_Type(Bits):namedValues=NamedValues(*(('turbo',1),('cck',2),('ofdm',3),('spectrum2Ghz',4),('spectrum5Ghz',5),('passiveScan',6),('dynamicCckOfdm',7),('gfsk',8),('spectrum900Mhz',9),('dot11aStaticTurbo',10),('halfRate',11),('quarterRate',12),('ht20',13),('ht40u',14),('ht40d',15),('dfs',16),('xmit4ms',17),('noAdhoc',18),('noHostAp',19),('dot11d',20)))
_WlanIfaceChannelFlags_Type.__name__=_J
_WlanIfaceChannelFlags_Object=MibTableColumn
wlanIfaceChannelFlags=_WlanIfaceChannelFlags_Object((1,3,6,1,4,1,12325,1,210,1,5,1,4),_WlanIfaceChannelFlags_Type())
wlanIfaceChannelFlags.setMaxAccess(_B)
if mibBuilder.loadTexts:wlanIfaceChannelFlags.setStatus(_A)
_WlanIfaceChannelFrequency_Type=Integer32
_WlanIfaceChannelFrequency_Object=MibTableColumn
wlanIfaceChannelFrequency=_WlanIfaceChannelFrequency_Object((1,3,6,1,4,1,12325,1,210,1,5,1,5),_WlanIfaceChannelFrequency_Type())
wlanIfaceChannelFrequency.setMaxAccess(_B)
if mibBuilder.loadTexts:wlanIfaceChannelFrequency.setStatus(_A)
_WlanIfaceChannelMaxRegPower_Type=Integer32
_WlanIfaceChannelMaxRegPower_Object=MibTableColumn
wlanIfaceChannelMaxRegPower=_WlanIfaceChannelMaxRegPower_Object((1,3,6,1,4,1,12325,1,210,1,5,1,6),_WlanIfaceChannelMaxRegPower_Type())
wlanIfaceChannelMaxRegPower.setMaxAccess(_B)
if mibBuilder.loadTexts:wlanIfaceChannelMaxRegPower.setStatus(_A)
_WlanIfaceChannelMaxTxPower_Type=Integer32
_WlanIfaceChannelMaxTxPower_Object=MibTableColumn
wlanIfaceChannelMaxTxPower=_WlanIfaceChannelMaxTxPower_Object((1,3,6,1,4,1,12325,1,210,1,5,1,7),_WlanIfaceChannelMaxTxPower_Type())
wlanIfaceChannelMaxTxPower.setMaxAccess(_B)
if mibBuilder.loadTexts:wlanIfaceChannelMaxTxPower.setStatus(_A)
_WlanIfaceChannelMinTxPower_Type=Integer32
_WlanIfaceChannelMinTxPower_Object=MibTableColumn
wlanIfaceChannelMinTxPower=_WlanIfaceChannelMinTxPower_Object((1,3,6,1,4,1,12325,1,210,1,5,1,8),_WlanIfaceChannelMinTxPower_Type())
wlanIfaceChannelMinTxPower.setMaxAccess(_B)
if mibBuilder.loadTexts:wlanIfaceChannelMinTxPower.setStatus(_A)
class _WlanIfaceChannelState_Type(Bits):namedValues=NamedValues(*(('radar',1),('cacDone',2),('interferenceDetected',3),('radarClear',4)))
_WlanIfaceChannelState_Type.__name__=_J
_WlanIfaceChannelState_Object=MibTableColumn
wlanIfaceChannelState=_WlanIfaceChannelState_Object((1,3,6,1,4,1,12325,1,210,1,5,1,9),_WlanIfaceChannelState_Type())
wlanIfaceChannelState.setMaxAccess(_B)
if mibBuilder.loadTexts:wlanIfaceChannelState.setStatus(_A)
_WlanIfaceChannelHTExtension_Type=Integer32
_WlanIfaceChannelHTExtension_Object=MibTableColumn
wlanIfaceChannelHTExtension=_WlanIfaceChannelHTExtension_Object((1,3,6,1,4,1,12325,1,210,1,5,1,10),_WlanIfaceChannelHTExtension_Type())
wlanIfaceChannelHTExtension.setMaxAccess(_B)
if mibBuilder.loadTexts:wlanIfaceChannelHTExtension.setStatus(_A)
_WlanIfaceChannelMaxAntennaGain_Type=Integer32
_WlanIfaceChannelMaxAntennaGain_Object=MibTableColumn
wlanIfaceChannelMaxAntennaGain=_WlanIfaceChannelMaxAntennaGain_Object((1,3,6,1,4,1,12325,1,210,1,5,1,11),_WlanIfaceChannelMaxAntennaGain_Type())
wlanIfaceChannelMaxAntennaGain.setMaxAccess(_B)
if mibBuilder.loadTexts:wlanIfaceChannelMaxAntennaGain.setStatus(_A)
_WlanIfRoamParamsTable_Object=MibTable
wlanIfRoamParamsTable=_WlanIfRoamParamsTable_Object((1,3,6,1,4,1,12325,1,210,1,6))
if mibBuilder.loadTexts:wlanIfRoamParamsTable.setStatus(_A)
_WlanIfRoamParamsEntry_Object=MibTableRow
wlanIfRoamParamsEntry=_WlanIfRoamParamsEntry_Object((1,3,6,1,4,1,12325,1,210,1,6,1))
wlanIfRoamParamsEntry.setIndexNames((0,_F,_G),(0,_F,_k))
if mibBuilder.loadTexts:wlanIfRoamParamsEntry.setStatus(_A)
_WlanIfRoamPhyMode_Type=WlanIfPhyMode
_WlanIfRoamPhyMode_Object=MibTableColumn
wlanIfRoamPhyMode=_WlanIfRoamPhyMode_Object((1,3,6,1,4,1,12325,1,210,1,6,1,1),_WlanIfRoamPhyMode_Type())
wlanIfRoamPhyMode.setMaxAccess(_S)
if mibBuilder.loadTexts:wlanIfRoamPhyMode.setStatus(_A)
_WlanIfRoamRxSignalStrength_Type=Integer32
_WlanIfRoamRxSignalStrength_Object=MibTableColumn
wlanIfRoamRxSignalStrength=_WlanIfRoamRxSignalStrength_Object((1,3,6,1,4,1,12325,1,210,1,6,1,2),_WlanIfRoamRxSignalStrength_Type())
wlanIfRoamRxSignalStrength.setMaxAccess(_B)
if mibBuilder.loadTexts:wlanIfRoamRxSignalStrength.setStatus(_A)
_WlanIfRoamTxRateThreshold_Type=Integer32
_WlanIfRoamTxRateThreshold_Object=MibTableColumn
wlanIfRoamTxRateThreshold=_WlanIfRoamTxRateThreshold_Object((1,3,6,1,4,1,12325,1,210,1,6,1,3),_WlanIfRoamTxRateThreshold_Type())
wlanIfRoamTxRateThreshold.setMaxAccess(_B)
if mibBuilder.loadTexts:wlanIfRoamTxRateThreshold.setStatus(_A)
_WlanIfTxParamsTable_Object=MibTable
wlanIfTxParamsTable=_WlanIfTxParamsTable_Object((1,3,6,1,4,1,12325,1,210,1,7))
if mibBuilder.loadTexts:wlanIfTxParamsTable.setStatus(_A)
_WlanIfTxParamsEntry_Object=MibTableRow
wlanIfTxParamsEntry=_WlanIfTxParamsEntry_Object((1,3,6,1,4,1,12325,1,210,1,7,1))
wlanIfTxParamsEntry.setIndexNames((0,_F,_G),(0,_F,_l))
if mibBuilder.loadTexts:wlanIfTxParamsEntry.setStatus(_A)
_WlanIfTxPhyMode_Type=WlanIfPhyMode
_WlanIfTxPhyMode_Object=MibTableColumn
wlanIfTxPhyMode=_WlanIfTxPhyMode_Object((1,3,6,1,4,1,12325,1,210,1,7,1,1),_WlanIfTxPhyMode_Type())
wlanIfTxPhyMode.setMaxAccess(_S)
if mibBuilder.loadTexts:wlanIfTxPhyMode.setStatus(_A)
_WlanIfTxUnicastRate_Type=Integer32
_WlanIfTxUnicastRate_Object=MibTableColumn
wlanIfTxUnicastRate=_WlanIfTxUnicastRate_Object((1,3,6,1,4,1,12325,1,210,1,7,1,2),_WlanIfTxUnicastRate_Type())
wlanIfTxUnicastRate.setMaxAccess(_D)
if mibBuilder.loadTexts:wlanIfTxUnicastRate.setStatus(_A)
_WlanIfTxMcastRate_Type=Integer32
_WlanIfTxMcastRate_Object=MibTableColumn
wlanIfTxMcastRate=_WlanIfTxMcastRate_Object((1,3,6,1,4,1,12325,1,210,1,7,1,3),_WlanIfTxMcastRate_Type())
wlanIfTxMcastRate.setMaxAccess(_D)
if mibBuilder.loadTexts:wlanIfTxMcastRate.setStatus(_A)
_WlanIfTxMgmtRate_Type=Integer32
_WlanIfTxMgmtRate_Object=MibTableColumn
wlanIfTxMgmtRate=_WlanIfTxMgmtRate_Object((1,3,6,1,4,1,12325,1,210,1,7,1,4),_WlanIfTxMgmtRate_Type())
wlanIfTxMgmtRate.setMaxAccess(_D)
if mibBuilder.loadTexts:wlanIfTxMgmtRate.setStatus(_A)
_WlanIfTxMaxRetryCount_Type=Integer32
_WlanIfTxMaxRetryCount_Object=MibTableColumn
wlanIfTxMaxRetryCount=_WlanIfTxMaxRetryCount_Object((1,3,6,1,4,1,12325,1,210,1,7,1,5),_WlanIfTxMaxRetryCount_Type())
wlanIfTxMaxRetryCount.setMaxAccess(_D)
if mibBuilder.loadTexts:wlanIfTxMaxRetryCount.setStatus(_A)
_BegemotWlanScanning_ObjectIdentity=ObjectIdentity
begemotWlanScanning=_BegemotWlanScanning_ObjectIdentity((1,3,6,1,4,1,12325,1,210,2))
_WlanScanConfigTable_Object=MibTable
wlanScanConfigTable=_WlanScanConfigTable_Object((1,3,6,1,4,1,12325,1,210,2,1))
if mibBuilder.loadTexts:wlanScanConfigTable.setStatus(_A)
_WlanScanConfigEntry_Object=MibTableRow
wlanScanConfigEntry=_WlanScanConfigEntry_Object((1,3,6,1,4,1,12325,1,210,2,1,1))
wlanScanConfigEntry.setIndexNames((0,_F,_G))
if mibBuilder.loadTexts:wlanScanConfigEntry.setStatus(_A)
class _WlanScanFlags_Type(Bits):namedValues=NamedValues(*(('noSelection',1),('activeScan',2),('pickFirst',3),('backgroundScan',4),('once',5),('noBroadcast',6),('noAutoSequencing',7),('flushCashe',8),('chechCashe',9)))
_WlanScanFlags_Type.__name__=_J
_WlanScanFlags_Object=MibTableColumn
wlanScanFlags=_WlanScanFlags_Object((1,3,6,1,4,1,12325,1,210,2,1,1,1),_WlanScanFlags_Type())
wlanScanFlags.setMaxAccess(_D)
if mibBuilder.loadTexts:wlanScanFlags.setStatus(_A)
class _WlanScanDuration_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_WlanScanDuration_Type.__name__=_E
_WlanScanDuration_Object=MibTableColumn
wlanScanDuration=_WlanScanDuration_Object((1,3,6,1,4,1,12325,1,210,2,1,1,2),_WlanScanDuration_Type())
wlanScanDuration.setMaxAccess(_D)
if mibBuilder.loadTexts:wlanScanDuration.setStatus(_A)
if mibBuilder.loadTexts:wlanScanDuration.setUnits(_H)
_WlanScanMinChannelDwellTime_Type=Integer32
_WlanScanMinChannelDwellTime_Object=MibTableColumn
wlanScanMinChannelDwellTime=_WlanScanMinChannelDwellTime_Object((1,3,6,1,4,1,12325,1,210,2,1,1,3),_WlanScanMinChannelDwellTime_Type())
wlanScanMinChannelDwellTime.setMaxAccess(_D)
if mibBuilder.loadTexts:wlanScanMinChannelDwellTime.setStatus(_A)
if mibBuilder.loadTexts:wlanScanMinChannelDwellTime.setUnits(_H)
_WlanScanMaxChannelDwellTime_Type=Integer32
_WlanScanMaxChannelDwellTime_Object=MibTableColumn
wlanScanMaxChannelDwellTime=_WlanScanMaxChannelDwellTime_Object((1,3,6,1,4,1,12325,1,210,2,1,1,4),_WlanScanMaxChannelDwellTime_Type())
wlanScanMaxChannelDwellTime.setMaxAccess(_D)
if mibBuilder.loadTexts:wlanScanMaxChannelDwellTime.setStatus(_A)
if mibBuilder.loadTexts:wlanScanMaxChannelDwellTime.setUnits(_H)
class _WlanScanConfigStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4)));namedValues=NamedValues(*((_T,0),('notStarted',1),('running',2),('finished',3),('cancel',4)))
_WlanScanConfigStatus_Type.__name__=_E
_WlanScanConfigStatus_Object=MibTableColumn
wlanScanConfigStatus=_WlanScanConfigStatus_Object((1,3,6,1,4,1,12325,1,210,2,1,1,5),_WlanScanConfigStatus_Type())
wlanScanConfigStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:wlanScanConfigStatus.setStatus(_A)
_WlanScanResultsTable_Object=MibTable
wlanScanResultsTable=_WlanScanResultsTable_Object((1,3,6,1,4,1,12325,1,210,2,2))
if mibBuilder.loadTexts:wlanScanResultsTable.setStatus(_A)
_WlanScanResultsEntry_Object=MibTableRow
wlanScanResultsEntry=_WlanScanResultsEntry_Object((1,3,6,1,4,1,12325,1,210,2,2,1))
wlanScanResultsEntry.setIndexNames((0,_F,_G),(0,_F,_m),(0,_F,_n))
if mibBuilder.loadTexts:wlanScanResultsEntry.setStatus(_A)
class _WlanScanResultID_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_WlanScanResultID_Type.__name__=_L
_WlanScanResultID_Object=MibTableColumn
wlanScanResultID=_WlanScanResultID_Object((1,3,6,1,4,1,12325,1,210,2,2,1,1),_WlanScanResultID_Type())
wlanScanResultID.setMaxAccess(_B)
if mibBuilder.loadTexts:wlanScanResultID.setStatus(_A)
_WlanScanResultBssid_Type=MacAddress
_WlanScanResultBssid_Object=MibTableColumn
wlanScanResultBssid=_WlanScanResultBssid_Object((1,3,6,1,4,1,12325,1,210,2,2,1,2),_WlanScanResultBssid_Type())
wlanScanResultBssid.setMaxAccess(_B)
if mibBuilder.loadTexts:wlanScanResultBssid.setStatus(_A)
_WlanScanResultChannel_Type=Integer32
_WlanScanResultChannel_Object=MibTableColumn
wlanScanResultChannel=_WlanScanResultChannel_Object((1,3,6,1,4,1,12325,1,210,2,2,1,3),_WlanScanResultChannel_Type())
wlanScanResultChannel.setMaxAccess(_B)
if mibBuilder.loadTexts:wlanScanResultChannel.setStatus(_A)
_WlanScanResultRate_Type=Integer32
_WlanScanResultRate_Object=MibTableColumn
wlanScanResultRate=_WlanScanResultRate_Object((1,3,6,1,4,1,12325,1,210,2,2,1,4),_WlanScanResultRate_Type())
wlanScanResultRate.setMaxAccess(_B)
if mibBuilder.loadTexts:wlanScanResultRate.setStatus(_A)
_WlanScanResultNoise_Type=Integer32
_WlanScanResultNoise_Object=MibTableColumn
wlanScanResultNoise=_WlanScanResultNoise_Object((1,3,6,1,4,1,12325,1,210,2,2,1,5),_WlanScanResultNoise_Type())
wlanScanResultNoise.setMaxAccess(_B)
if mibBuilder.loadTexts:wlanScanResultNoise.setStatus(_A)
_WlanScanResultBeaconInterval_Type=Integer32
_WlanScanResultBeaconInterval_Object=MibTableColumn
wlanScanResultBeaconInterval=_WlanScanResultBeaconInterval_Object((1,3,6,1,4,1,12325,1,210,2,2,1,6),_WlanScanResultBeaconInterval_Type())
wlanScanResultBeaconInterval.setMaxAccess(_B)
if mibBuilder.loadTexts:wlanScanResultBeaconInterval.setStatus(_A)
_WlanScanResultCapabilities_Type=WlanPeerCapabilityFlags
_WlanScanResultCapabilities_Object=MibTableColumn
wlanScanResultCapabilities=_WlanScanResultCapabilities_Object((1,3,6,1,4,1,12325,1,210,2,2,1,7),_WlanScanResultCapabilities_Type())
wlanScanResultCapabilities.setMaxAccess(_B)
if mibBuilder.loadTexts:wlanScanResultCapabilities.setStatus(_A)
_BegemotWlanStatistics_ObjectIdentity=ObjectIdentity
begemotWlanStatistics=_BegemotWlanStatistics_ObjectIdentity((1,3,6,1,4,1,12325,1,210,3))
_WlanIfaceStatisticsTable_Object=MibTable
wlanIfaceStatisticsTable=_WlanIfaceStatisticsTable_Object((1,3,6,1,4,1,12325,1,210,3,1))
if mibBuilder.loadTexts:wlanIfaceStatisticsTable.setStatus(_A)
_WlanIfaceStatisticsEntry_Object=MibTableRow
wlanIfaceStatisticsEntry=_WlanIfaceStatisticsEntry_Object((1,3,6,1,4,1,12325,1,210,3,1,1))
if mibBuilder.loadTexts:wlanIfaceStatisticsEntry.setStatus(_A)
_WlanStatsRxBadVersion_Type=Counter32
_WlanStatsRxBadVersion_Object=MibTableColumn
wlanStatsRxBadVersion=_WlanStatsRxBadVersion_Object((1,3,6,1,4,1,12325,1,210,3,1,1,1),_WlanStatsRxBadVersion_Type())
wlanStatsRxBadVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:wlanStatsRxBadVersion.setStatus(_A)
if mibBuilder.loadTexts:wlanStatsRxBadVersion.setUnits(_C)
_WlanStatsRxTooShort_Type=Counter32
_WlanStatsRxTooShort_Object=MibTableColumn
wlanStatsRxTooShort=_WlanStatsRxTooShort_Object((1,3,6,1,4,1,12325,1,210,3,1,1,2),_WlanStatsRxTooShort_Type())
wlanStatsRxTooShort.setMaxAccess(_B)
if mibBuilder.loadTexts:wlanStatsRxTooShort.setStatus(_A)
if mibBuilder.loadTexts:wlanStatsRxTooShort.setUnits(_C)
_WlanStatsRxWrongBssid_Type=Counter32
_WlanStatsRxWrongBssid_Object=MibTableColumn
wlanStatsRxWrongBssid=_WlanStatsRxWrongBssid_Object((1,3,6,1,4,1,12325,1,210,3,1,1,3),_WlanStatsRxWrongBssid_Type())
wlanStatsRxWrongBssid.setMaxAccess(_B)
if mibBuilder.loadTexts:wlanStatsRxWrongBssid.setStatus(_A)
if mibBuilder.loadTexts:wlanStatsRxWrongBssid.setUnits(_C)
_WlanStatsRxDiscardedDups_Type=Counter32
_WlanStatsRxDiscardedDups_Object=MibTableColumn
wlanStatsRxDiscardedDups=_WlanStatsRxDiscardedDups_Object((1,3,6,1,4,1,12325,1,210,3,1,1,4),_WlanStatsRxDiscardedDups_Type())
wlanStatsRxDiscardedDups.setMaxAccess(_B)
if mibBuilder.loadTexts:wlanStatsRxDiscardedDups.setStatus(_A)
if mibBuilder.loadTexts:wlanStatsRxDiscardedDups.setUnits(_C)
_WlanStatsRxWrongDir_Type=Counter32
_WlanStatsRxWrongDir_Object=MibTableColumn
wlanStatsRxWrongDir=_WlanStatsRxWrongDir_Object((1,3,6,1,4,1,12325,1,210,3,1,1,5),_WlanStatsRxWrongDir_Type())
wlanStatsRxWrongDir.setMaxAccess(_B)
if mibBuilder.loadTexts:wlanStatsRxWrongDir.setStatus(_A)
if mibBuilder.loadTexts:wlanStatsRxWrongDir.setUnits(_C)
_WlanStatsRxDiscardMcastEcho_Type=Counter32
_WlanStatsRxDiscardMcastEcho_Object=MibTableColumn
wlanStatsRxDiscardMcastEcho=_WlanStatsRxDiscardMcastEcho_Object((1,3,6,1,4,1,12325,1,210,3,1,1,6),_WlanStatsRxDiscardMcastEcho_Type())
wlanStatsRxDiscardMcastEcho.setMaxAccess(_B)
if mibBuilder.loadTexts:wlanStatsRxDiscardMcastEcho.setStatus(_A)
if mibBuilder.loadTexts:wlanStatsRxDiscardMcastEcho.setUnits(_C)
_WlanStatsRxDiscardNoAssoc_Type=Counter32
_WlanStatsRxDiscardNoAssoc_Object=MibTableColumn
wlanStatsRxDiscardNoAssoc=_WlanStatsRxDiscardNoAssoc_Object((1,3,6,1,4,1,12325,1,210,3,1,1,7),_WlanStatsRxDiscardNoAssoc_Type())
wlanStatsRxDiscardNoAssoc.setMaxAccess(_B)
if mibBuilder.loadTexts:wlanStatsRxDiscardNoAssoc.setStatus(_A)
if mibBuilder.loadTexts:wlanStatsRxDiscardNoAssoc.setUnits(_C)
_WlanStatsRxWepNoPrivacy_Type=Counter32
_WlanStatsRxWepNoPrivacy_Object=MibTableColumn
wlanStatsRxWepNoPrivacy=_WlanStatsRxWepNoPrivacy_Object((1,3,6,1,4,1,12325,1,210,3,1,1,8),_WlanStatsRxWepNoPrivacy_Type())
wlanStatsRxWepNoPrivacy.setMaxAccess(_B)
if mibBuilder.loadTexts:wlanStatsRxWepNoPrivacy.setStatus(_A)
if mibBuilder.loadTexts:wlanStatsRxWepNoPrivacy.setUnits(_C)
_WlanStatsRxWepUnencrypted_Type=Counter32
_WlanStatsRxWepUnencrypted_Object=MibTableColumn
wlanStatsRxWepUnencrypted=_WlanStatsRxWepUnencrypted_Object((1,3,6,1,4,1,12325,1,210,3,1,1,9),_WlanStatsRxWepUnencrypted_Type())
wlanStatsRxWepUnencrypted.setMaxAccess(_B)
if mibBuilder.loadTexts:wlanStatsRxWepUnencrypted.setStatus(_A)
if mibBuilder.loadTexts:wlanStatsRxWepUnencrypted.setUnits(_C)
_WlanStatsRxWepFailed_Type=Counter32
_WlanStatsRxWepFailed_Object=MibTableColumn
wlanStatsRxWepFailed=_WlanStatsRxWepFailed_Object((1,3,6,1,4,1,12325,1,210,3,1,1,10),_WlanStatsRxWepFailed_Type())
wlanStatsRxWepFailed.setMaxAccess(_B)
if mibBuilder.loadTexts:wlanStatsRxWepFailed.setStatus(_A)
if mibBuilder.loadTexts:wlanStatsRxWepFailed.setUnits(_C)
_WlanStatsRxDecapsulationFailed_Type=Counter32
_WlanStatsRxDecapsulationFailed_Object=MibTableColumn
wlanStatsRxDecapsulationFailed=_WlanStatsRxDecapsulationFailed_Object((1,3,6,1,4,1,12325,1,210,3,1,1,11),_WlanStatsRxDecapsulationFailed_Type())
wlanStatsRxDecapsulationFailed.setMaxAccess(_B)
if mibBuilder.loadTexts:wlanStatsRxDecapsulationFailed.setStatus(_A)
if mibBuilder.loadTexts:wlanStatsRxDecapsulationFailed.setUnits(_C)
_WlanStatsRxDiscardMgmt_Type=Counter32
_WlanStatsRxDiscardMgmt_Object=MibTableColumn
wlanStatsRxDiscardMgmt=_WlanStatsRxDiscardMgmt_Object((1,3,6,1,4,1,12325,1,210,3,1,1,12),_WlanStatsRxDiscardMgmt_Type())
wlanStatsRxDiscardMgmt.setMaxAccess(_B)
if mibBuilder.loadTexts:wlanStatsRxDiscardMgmt.setStatus(_A)
if mibBuilder.loadTexts:wlanStatsRxDiscardMgmt.setUnits(_C)
_WlanStatsRxControl_Type=Counter32
_WlanStatsRxControl_Object=MibTableColumn
wlanStatsRxControl=_WlanStatsRxControl_Object((1,3,6,1,4,1,12325,1,210,3,1,1,13),_WlanStatsRxControl_Type())
wlanStatsRxControl.setMaxAccess(_B)
if mibBuilder.loadTexts:wlanStatsRxControl.setStatus(_A)
if mibBuilder.loadTexts:wlanStatsRxControl.setUnits(_C)
_WlanStatsRxBeacon_Type=Counter32
_WlanStatsRxBeacon_Object=MibTableColumn
wlanStatsRxBeacon=_WlanStatsRxBeacon_Object((1,3,6,1,4,1,12325,1,210,3,1,1,14),_WlanStatsRxBeacon_Type())
wlanStatsRxBeacon.setMaxAccess(_B)
if mibBuilder.loadTexts:wlanStatsRxBeacon.setStatus(_A)
if mibBuilder.loadTexts:wlanStatsRxBeacon.setUnits(_C)
_WlanStatsRxRateSetTooBig_Type=Counter32
_WlanStatsRxRateSetTooBig_Object=MibTableColumn
wlanStatsRxRateSetTooBig=_WlanStatsRxRateSetTooBig_Object((1,3,6,1,4,1,12325,1,210,3,1,1,15),_WlanStatsRxRateSetTooBig_Type())
wlanStatsRxRateSetTooBig.setMaxAccess(_B)
if mibBuilder.loadTexts:wlanStatsRxRateSetTooBig.setStatus(_A)
if mibBuilder.loadTexts:wlanStatsRxRateSetTooBig.setUnits(_C)
_WlanStatsRxElemMissing_Type=Counter32
_WlanStatsRxElemMissing_Object=MibTableColumn
wlanStatsRxElemMissing=_WlanStatsRxElemMissing_Object((1,3,6,1,4,1,12325,1,210,3,1,1,16),_WlanStatsRxElemMissing_Type())
wlanStatsRxElemMissing.setMaxAccess(_B)
if mibBuilder.loadTexts:wlanStatsRxElemMissing.setStatus(_A)
if mibBuilder.loadTexts:wlanStatsRxElemMissing.setUnits(_C)
_WlanStatsRxElemTooBig_Type=Counter32
_WlanStatsRxElemTooBig_Object=MibTableColumn
wlanStatsRxElemTooBig=_WlanStatsRxElemTooBig_Object((1,3,6,1,4,1,12325,1,210,3,1,1,17),_WlanStatsRxElemTooBig_Type())
wlanStatsRxElemTooBig.setMaxAccess(_B)
if mibBuilder.loadTexts:wlanStatsRxElemTooBig.setStatus(_A)
if mibBuilder.loadTexts:wlanStatsRxElemTooBig.setUnits(_C)
_WlanStatsRxElemTooSmall_Type=Counter32
_WlanStatsRxElemTooSmall_Object=MibTableColumn
wlanStatsRxElemTooSmall=_WlanStatsRxElemTooSmall_Object((1,3,6,1,4,1,12325,1,210,3,1,1,18),_WlanStatsRxElemTooSmall_Type())
wlanStatsRxElemTooSmall.setMaxAccess(_B)
if mibBuilder.loadTexts:wlanStatsRxElemTooSmall.setStatus(_A)
if mibBuilder.loadTexts:wlanStatsRxElemTooSmall.setUnits(_C)
_WlanStatsRxElemUnknown_Type=Counter32
_WlanStatsRxElemUnknown_Object=MibTableColumn
wlanStatsRxElemUnknown=_WlanStatsRxElemUnknown_Object((1,3,6,1,4,1,12325,1,210,3,1,1,19),_WlanStatsRxElemUnknown_Type())
wlanStatsRxElemUnknown.setMaxAccess(_B)
if mibBuilder.loadTexts:wlanStatsRxElemUnknown.setStatus(_A)
if mibBuilder.loadTexts:wlanStatsRxElemUnknown.setUnits(_C)
_WlanStatsRxChannelMismatch_Type=Counter32
_WlanStatsRxChannelMismatch_Object=MibTableColumn
wlanStatsRxChannelMismatch=_WlanStatsRxChannelMismatch_Object((1,3,6,1,4,1,12325,1,210,3,1,1,20),_WlanStatsRxChannelMismatch_Type())
wlanStatsRxChannelMismatch.setMaxAccess(_B)
if mibBuilder.loadTexts:wlanStatsRxChannelMismatch.setStatus(_A)
if mibBuilder.loadTexts:wlanStatsRxChannelMismatch.setUnits(_C)
_WlanStatsRxDropped_Type=Counter32
_WlanStatsRxDropped_Object=MibTableColumn
wlanStatsRxDropped=_WlanStatsRxDropped_Object((1,3,6,1,4,1,12325,1,210,3,1,1,21),_WlanStatsRxDropped_Type())
wlanStatsRxDropped.setMaxAccess(_B)
if mibBuilder.loadTexts:wlanStatsRxDropped.setStatus(_A)
if mibBuilder.loadTexts:wlanStatsRxDropped.setUnits(_C)
_WlanStatsRxSsidMismatch_Type=Counter32
_WlanStatsRxSsidMismatch_Object=MibTableColumn
wlanStatsRxSsidMismatch=_WlanStatsRxSsidMismatch_Object((1,3,6,1,4,1,12325,1,210,3,1,1,22),_WlanStatsRxSsidMismatch_Type())
wlanStatsRxSsidMismatch.setMaxAccess(_B)
if mibBuilder.loadTexts:wlanStatsRxSsidMismatch.setStatus(_A)
if mibBuilder.loadTexts:wlanStatsRxSsidMismatch.setUnits(_C)
_WlanStatsRxAuthNotSupported_Type=Counter32
_WlanStatsRxAuthNotSupported_Object=MibTableColumn
wlanStatsRxAuthNotSupported=_WlanStatsRxAuthNotSupported_Object((1,3,6,1,4,1,12325,1,210,3,1,1,23),_WlanStatsRxAuthNotSupported_Type())
wlanStatsRxAuthNotSupported.setMaxAccess(_B)
if mibBuilder.loadTexts:wlanStatsRxAuthNotSupported.setStatus(_A)
if mibBuilder.loadTexts:wlanStatsRxAuthNotSupported.setUnits(_C)
_WlanStatsRxAuthFailed_Type=Counter32
_WlanStatsRxAuthFailed_Object=MibTableColumn
wlanStatsRxAuthFailed=_WlanStatsRxAuthFailed_Object((1,3,6,1,4,1,12325,1,210,3,1,1,24),_WlanStatsRxAuthFailed_Type())
wlanStatsRxAuthFailed.setMaxAccess(_B)
if mibBuilder.loadTexts:wlanStatsRxAuthFailed.setStatus(_A)
if mibBuilder.loadTexts:wlanStatsRxAuthFailed.setUnits(_C)
_WlanStatsRxAuthCM_Type=Counter32
_WlanStatsRxAuthCM_Object=MibTableColumn
wlanStatsRxAuthCM=_WlanStatsRxAuthCM_Object((1,3,6,1,4,1,12325,1,210,3,1,1,25),_WlanStatsRxAuthCM_Type())
wlanStatsRxAuthCM.setMaxAccess(_B)
if mibBuilder.loadTexts:wlanStatsRxAuthCM.setStatus(_A)
if mibBuilder.loadTexts:wlanStatsRxAuthCM.setUnits(_C)
_WlanStatsRxAssocWrongBssid_Type=Counter32
_WlanStatsRxAssocWrongBssid_Object=MibTableColumn
wlanStatsRxAssocWrongBssid=_WlanStatsRxAssocWrongBssid_Object((1,3,6,1,4,1,12325,1,210,3,1,1,26),_WlanStatsRxAssocWrongBssid_Type())
wlanStatsRxAssocWrongBssid.setMaxAccess(_B)
if mibBuilder.loadTexts:wlanStatsRxAssocWrongBssid.setStatus(_A)
if mibBuilder.loadTexts:wlanStatsRxAssocWrongBssid.setUnits(_C)
_WlanStatsRxAssocNoAuth_Type=Counter32
_WlanStatsRxAssocNoAuth_Object=MibTableColumn
wlanStatsRxAssocNoAuth=_WlanStatsRxAssocNoAuth_Object((1,3,6,1,4,1,12325,1,210,3,1,1,27),_WlanStatsRxAssocNoAuth_Type())
wlanStatsRxAssocNoAuth.setMaxAccess(_B)
if mibBuilder.loadTexts:wlanStatsRxAssocNoAuth.setStatus(_A)
if mibBuilder.loadTexts:wlanStatsRxAssocNoAuth.setUnits(_C)
_WlanStatsRxAssocCapMismatch_Type=Counter32
_WlanStatsRxAssocCapMismatch_Object=MibTableColumn
wlanStatsRxAssocCapMismatch=_WlanStatsRxAssocCapMismatch_Object((1,3,6,1,4,1,12325,1,210,3,1,1,28),_WlanStatsRxAssocCapMismatch_Type())
wlanStatsRxAssocCapMismatch.setMaxAccess(_B)
if mibBuilder.loadTexts:wlanStatsRxAssocCapMismatch.setStatus(_A)
if mibBuilder.loadTexts:wlanStatsRxAssocCapMismatch.setUnits(_C)
_WlanStatsRxAssocNoRateMatch_Type=Counter32
_WlanStatsRxAssocNoRateMatch_Object=MibTableColumn
wlanStatsRxAssocNoRateMatch=_WlanStatsRxAssocNoRateMatch_Object((1,3,6,1,4,1,12325,1,210,3,1,1,29),_WlanStatsRxAssocNoRateMatch_Type())
wlanStatsRxAssocNoRateMatch.setMaxAccess(_B)
if mibBuilder.loadTexts:wlanStatsRxAssocNoRateMatch.setStatus(_A)
if mibBuilder.loadTexts:wlanStatsRxAssocNoRateMatch.setUnits(_C)
_WlanStatsRxBadWpaIE_Type=Counter32
_WlanStatsRxBadWpaIE_Object=MibTableColumn
wlanStatsRxBadWpaIE=_WlanStatsRxBadWpaIE_Object((1,3,6,1,4,1,12325,1,210,3,1,1,30),_WlanStatsRxBadWpaIE_Type())
wlanStatsRxBadWpaIE.setMaxAccess(_B)
if mibBuilder.loadTexts:wlanStatsRxBadWpaIE.setStatus(_A)
if mibBuilder.loadTexts:wlanStatsRxBadWpaIE.setUnits(_C)
_WlanStatsRxDeauthenticate_Type=Counter32
_WlanStatsRxDeauthenticate_Object=MibTableColumn
wlanStatsRxDeauthenticate=_WlanStatsRxDeauthenticate_Object((1,3,6,1,4,1,12325,1,210,3,1,1,31),_WlanStatsRxDeauthenticate_Type())
wlanStatsRxDeauthenticate.setMaxAccess(_B)
if mibBuilder.loadTexts:wlanStatsRxDeauthenticate.setStatus(_A)
if mibBuilder.loadTexts:wlanStatsRxDeauthenticate.setUnits(_C)
_WlanStatsRxDisassociate_Type=Counter32
_WlanStatsRxDisassociate_Object=MibTableColumn
wlanStatsRxDisassociate=_WlanStatsRxDisassociate_Object((1,3,6,1,4,1,12325,1,210,3,1,1,32),_WlanStatsRxDisassociate_Type())
wlanStatsRxDisassociate.setMaxAccess(_B)
if mibBuilder.loadTexts:wlanStatsRxDisassociate.setStatus(_A)
if mibBuilder.loadTexts:wlanStatsRxDisassociate.setUnits(_C)
_WlanStatsRxUnknownSubtype_Type=Counter32
_WlanStatsRxUnknownSubtype_Object=MibTableColumn
wlanStatsRxUnknownSubtype=_WlanStatsRxUnknownSubtype_Object((1,3,6,1,4,1,12325,1,210,3,1,1,33),_WlanStatsRxUnknownSubtype_Type())
wlanStatsRxUnknownSubtype.setMaxAccess(_B)
if mibBuilder.loadTexts:wlanStatsRxUnknownSubtype.setStatus(_A)
if mibBuilder.loadTexts:wlanStatsRxUnknownSubtype.setUnits(_C)
_WlanStatsRxFailedNoBuf_Type=Counter32
_WlanStatsRxFailedNoBuf_Object=MibTableColumn
wlanStatsRxFailedNoBuf=_WlanStatsRxFailedNoBuf_Object((1,3,6,1,4,1,12325,1,210,3,1,1,34),_WlanStatsRxFailedNoBuf_Type())
wlanStatsRxFailedNoBuf.setMaxAccess(_B)
if mibBuilder.loadTexts:wlanStatsRxFailedNoBuf.setStatus(_A)
if mibBuilder.loadTexts:wlanStatsRxFailedNoBuf.setUnits(_C)
_WlanStatsRxBadAuthRequest_Type=Counter32
_WlanStatsRxBadAuthRequest_Object=MibTableColumn
wlanStatsRxBadAuthRequest=_WlanStatsRxBadAuthRequest_Object((1,3,6,1,4,1,12325,1,210,3,1,1,35),_WlanStatsRxBadAuthRequest_Type())
wlanStatsRxBadAuthRequest.setMaxAccess(_B)
if mibBuilder.loadTexts:wlanStatsRxBadAuthRequest.setStatus(_A)
if mibBuilder.loadTexts:wlanStatsRxBadAuthRequest.setUnits(_C)
_WlanStatsRxUnAuthorized_Type=Counter32
_WlanStatsRxUnAuthorized_Object=MibTableColumn
wlanStatsRxUnAuthorized=_WlanStatsRxUnAuthorized_Object((1,3,6,1,4,1,12325,1,210,3,1,1,36),_WlanStatsRxUnAuthorized_Type())
wlanStatsRxUnAuthorized.setMaxAccess(_B)
if mibBuilder.loadTexts:wlanStatsRxUnAuthorized.setStatus(_A)
if mibBuilder.loadTexts:wlanStatsRxUnAuthorized.setUnits(_C)
_WlanStatsRxBadKeyId_Type=Counter32
_WlanStatsRxBadKeyId_Object=MibTableColumn
wlanStatsRxBadKeyId=_WlanStatsRxBadKeyId_Object((1,3,6,1,4,1,12325,1,210,3,1,1,37),_WlanStatsRxBadKeyId_Type())
wlanStatsRxBadKeyId.setMaxAccess(_B)
if mibBuilder.loadTexts:wlanStatsRxBadKeyId.setStatus(_A)
if mibBuilder.loadTexts:wlanStatsRxBadKeyId.setUnits(_C)
_WlanStatsRxCCMPSeqViolation_Type=Counter32
_WlanStatsRxCCMPSeqViolation_Object=MibTableColumn
wlanStatsRxCCMPSeqViolation=_WlanStatsRxCCMPSeqViolation_Object((1,3,6,1,4,1,12325,1,210,3,1,1,38),_WlanStatsRxCCMPSeqViolation_Type())
wlanStatsRxCCMPSeqViolation.setMaxAccess(_B)
if mibBuilder.loadTexts:wlanStatsRxCCMPSeqViolation.setStatus(_A)
if mibBuilder.loadTexts:wlanStatsRxCCMPSeqViolation.setUnits(_C)
_WlanStatsRxCCMPBadFormat_Type=Counter32
_WlanStatsRxCCMPBadFormat_Object=MibTableColumn
wlanStatsRxCCMPBadFormat=_WlanStatsRxCCMPBadFormat_Object((1,3,6,1,4,1,12325,1,210,3,1,1,39),_WlanStatsRxCCMPBadFormat_Type())
wlanStatsRxCCMPBadFormat.setMaxAccess(_B)
if mibBuilder.loadTexts:wlanStatsRxCCMPBadFormat.setStatus(_A)
if mibBuilder.loadTexts:wlanStatsRxCCMPBadFormat.setUnits(_C)
_WlanStatsRxCCMPFailedMIC_Type=Counter32
_WlanStatsRxCCMPFailedMIC_Object=MibTableColumn
wlanStatsRxCCMPFailedMIC=_WlanStatsRxCCMPFailedMIC_Object((1,3,6,1,4,1,12325,1,210,3,1,1,40),_WlanStatsRxCCMPFailedMIC_Type())
wlanStatsRxCCMPFailedMIC.setMaxAccess(_B)
if mibBuilder.loadTexts:wlanStatsRxCCMPFailedMIC.setStatus(_A)
if mibBuilder.loadTexts:wlanStatsRxCCMPFailedMIC.setUnits(_C)
_WlanStatsRxTKIPSeqViolation_Type=Counter32
_WlanStatsRxTKIPSeqViolation_Object=MibTableColumn
wlanStatsRxTKIPSeqViolation=_WlanStatsRxTKIPSeqViolation_Object((1,3,6,1,4,1,12325,1,210,3,1,1,41),_WlanStatsRxTKIPSeqViolation_Type())
wlanStatsRxTKIPSeqViolation.setMaxAccess(_B)
if mibBuilder.loadTexts:wlanStatsRxTKIPSeqViolation.setStatus(_A)
if mibBuilder.loadTexts:wlanStatsRxTKIPSeqViolation.setUnits(_C)
_WlanStatsRxTKIPBadFormat_Type=Counter32
_WlanStatsRxTKIPBadFormat_Object=MibTableColumn
wlanStatsRxTKIPBadFormat=_WlanStatsRxTKIPBadFormat_Object((1,3,6,1,4,1,12325,1,210,3,1,1,42),_WlanStatsRxTKIPBadFormat_Type())
wlanStatsRxTKIPBadFormat.setMaxAccess(_B)
if mibBuilder.loadTexts:wlanStatsRxTKIPBadFormat.setStatus(_A)
if mibBuilder.loadTexts:wlanStatsRxTKIPBadFormat.setUnits(_C)
_WlanStatsRxTKIPFailedMIC_Type=Counter32
_WlanStatsRxTKIPFailedMIC_Object=MibTableColumn
wlanStatsRxTKIPFailedMIC=_WlanStatsRxTKIPFailedMIC_Object((1,3,6,1,4,1,12325,1,210,3,1,1,43),_WlanStatsRxTKIPFailedMIC_Type())
wlanStatsRxTKIPFailedMIC.setMaxAccess(_B)
if mibBuilder.loadTexts:wlanStatsRxTKIPFailedMIC.setStatus(_A)
if mibBuilder.loadTexts:wlanStatsRxTKIPFailedMIC.setUnits(_C)
_WlanStatsRxTKIPFailedICV_Type=Counter32
_WlanStatsRxTKIPFailedICV_Object=MibTableColumn
wlanStatsRxTKIPFailedICV=_WlanStatsRxTKIPFailedICV_Object((1,3,6,1,4,1,12325,1,210,3,1,1,44),_WlanStatsRxTKIPFailedICV_Type())
wlanStatsRxTKIPFailedICV.setMaxAccess(_B)
if mibBuilder.loadTexts:wlanStatsRxTKIPFailedICV.setStatus(_A)
if mibBuilder.loadTexts:wlanStatsRxTKIPFailedICV.setUnits(_C)
_WlanStatsRxDiscardACL_Type=Counter32
_WlanStatsRxDiscardACL_Object=MibTableColumn
wlanStatsRxDiscardACL=_WlanStatsRxDiscardACL_Object((1,3,6,1,4,1,12325,1,210,3,1,1,45),_WlanStatsRxDiscardACL_Type())
wlanStatsRxDiscardACL.setMaxAccess(_B)
if mibBuilder.loadTexts:wlanStatsRxDiscardACL.setStatus(_A)
if mibBuilder.loadTexts:wlanStatsRxDiscardACL.setUnits(_C)
_WlanStatsTxFailedNoBuf_Type=Counter32
_WlanStatsTxFailedNoBuf_Object=MibTableColumn
wlanStatsTxFailedNoBuf=_WlanStatsTxFailedNoBuf_Object((1,3,6,1,4,1,12325,1,210,3,1,1,46),_WlanStatsTxFailedNoBuf_Type())
wlanStatsTxFailedNoBuf.setMaxAccess(_B)
if mibBuilder.loadTexts:wlanStatsTxFailedNoBuf.setStatus(_A)
if mibBuilder.loadTexts:wlanStatsTxFailedNoBuf.setUnits(_C)
_WlanStatsTxFailedNoNode_Type=Counter32
_WlanStatsTxFailedNoNode_Object=MibTableColumn
wlanStatsTxFailedNoNode=_WlanStatsTxFailedNoNode_Object((1,3,6,1,4,1,12325,1,210,3,1,1,47),_WlanStatsTxFailedNoNode_Type())
wlanStatsTxFailedNoNode.setMaxAccess(_B)
if mibBuilder.loadTexts:wlanStatsTxFailedNoNode.setStatus(_A)
if mibBuilder.loadTexts:wlanStatsTxFailedNoNode.setUnits(_C)
_WlanStatsTxUnknownMgmt_Type=Counter32
_WlanStatsTxUnknownMgmt_Object=MibTableColumn
wlanStatsTxUnknownMgmt=_WlanStatsTxUnknownMgmt_Object((1,3,6,1,4,1,12325,1,210,3,1,1,48),_WlanStatsTxUnknownMgmt_Type())
wlanStatsTxUnknownMgmt.setMaxAccess(_B)
if mibBuilder.loadTexts:wlanStatsTxUnknownMgmt.setStatus(_A)
if mibBuilder.loadTexts:wlanStatsTxUnknownMgmt.setUnits(_C)
_WlanStatsTxBadCipher_Type=Counter32
_WlanStatsTxBadCipher_Object=MibTableColumn
wlanStatsTxBadCipher=_WlanStatsTxBadCipher_Object((1,3,6,1,4,1,12325,1,210,3,1,1,49),_WlanStatsTxBadCipher_Type())
wlanStatsTxBadCipher.setMaxAccess(_B)
if mibBuilder.loadTexts:wlanStatsTxBadCipher.setStatus(_A)
if mibBuilder.loadTexts:wlanStatsTxBadCipher.setUnits(_C)
_WlanStatsTxNoDefKey_Type=Counter32
_WlanStatsTxNoDefKey_Object=MibTableColumn
wlanStatsTxNoDefKey=_WlanStatsTxNoDefKey_Object((1,3,6,1,4,1,12325,1,210,3,1,1,50),_WlanStatsTxNoDefKey_Type())
wlanStatsTxNoDefKey.setMaxAccess(_B)
if mibBuilder.loadTexts:wlanStatsTxNoDefKey.setStatus(_A)
if mibBuilder.loadTexts:wlanStatsTxNoDefKey.setUnits(_C)
_WlanStatsTxFragmented_Type=Counter32
_WlanStatsTxFragmented_Object=MibTableColumn
wlanStatsTxFragmented=_WlanStatsTxFragmented_Object((1,3,6,1,4,1,12325,1,210,3,1,1,51),_WlanStatsTxFragmented_Type())
wlanStatsTxFragmented.setMaxAccess(_B)
if mibBuilder.loadTexts:wlanStatsTxFragmented.setStatus(_A)
if mibBuilder.loadTexts:wlanStatsTxFragmented.setUnits(_C)
_WlanStatsTxFragmentsCreated_Type=Counter32
_WlanStatsTxFragmentsCreated_Object=MibTableColumn
wlanStatsTxFragmentsCreated=_WlanStatsTxFragmentsCreated_Object((1,3,6,1,4,1,12325,1,210,3,1,1,52),_WlanStatsTxFragmentsCreated_Type())
wlanStatsTxFragmentsCreated.setMaxAccess(_B)
if mibBuilder.loadTexts:wlanStatsTxFragmentsCreated.setStatus(_A)
if mibBuilder.loadTexts:wlanStatsTxFragmentsCreated.setUnits(_C)
_WlanStatsActiveScans_Type=Counter32
_WlanStatsActiveScans_Object=MibTableColumn
wlanStatsActiveScans=_WlanStatsActiveScans_Object((1,3,6,1,4,1,12325,1,210,3,1,1,53),_WlanStatsActiveScans_Type())
wlanStatsActiveScans.setMaxAccess(_B)
if mibBuilder.loadTexts:wlanStatsActiveScans.setStatus(_A)
_WlanStatsPassiveScans_Type=Counter32
_WlanStatsPassiveScans_Object=MibTableColumn
wlanStatsPassiveScans=_WlanStatsPassiveScans_Object((1,3,6,1,4,1,12325,1,210,3,1,1,54),_WlanStatsPassiveScans_Type())
wlanStatsPassiveScans.setMaxAccess(_B)
if mibBuilder.loadTexts:wlanStatsPassiveScans.setStatus(_A)
_WlanStatsTimeoutInactivity_Type=Counter32
_WlanStatsTimeoutInactivity_Object=MibTableColumn
wlanStatsTimeoutInactivity=_WlanStatsTimeoutInactivity_Object((1,3,6,1,4,1,12325,1,210,3,1,1,55),_WlanStatsTimeoutInactivity_Type())
wlanStatsTimeoutInactivity.setMaxAccess(_B)
if mibBuilder.loadTexts:wlanStatsTimeoutInactivity.setStatus(_A)
_WlanStatsCryptoNoMem_Type=Counter32
_WlanStatsCryptoNoMem_Object=MibTableColumn
wlanStatsCryptoNoMem=_WlanStatsCryptoNoMem_Object((1,3,6,1,4,1,12325,1,210,3,1,1,56),_WlanStatsCryptoNoMem_Type())
wlanStatsCryptoNoMem.setMaxAccess(_B)
if mibBuilder.loadTexts:wlanStatsCryptoNoMem.setStatus(_A)
_WlanStatsSwCryptoTKIP_Type=Counter32
_WlanStatsSwCryptoTKIP_Object=MibTableColumn
wlanStatsSwCryptoTKIP=_WlanStatsSwCryptoTKIP_Object((1,3,6,1,4,1,12325,1,210,3,1,1,57),_WlanStatsSwCryptoTKIP_Type())
wlanStatsSwCryptoTKIP.setMaxAccess(_B)
if mibBuilder.loadTexts:wlanStatsSwCryptoTKIP.setStatus(_A)
_WlanStatsSwCryptoTKIPEnMIC_Type=Counter32
_WlanStatsSwCryptoTKIPEnMIC_Object=MibTableColumn
wlanStatsSwCryptoTKIPEnMIC=_WlanStatsSwCryptoTKIPEnMIC_Object((1,3,6,1,4,1,12325,1,210,3,1,1,58),_WlanStatsSwCryptoTKIPEnMIC_Type())
wlanStatsSwCryptoTKIPEnMIC.setMaxAccess(_B)
if mibBuilder.loadTexts:wlanStatsSwCryptoTKIPEnMIC.setStatus(_A)
_WlanStatsSwCryptoTKIPDeMIC_Type=Counter32
_WlanStatsSwCryptoTKIPDeMIC_Object=MibTableColumn
wlanStatsSwCryptoTKIPDeMIC=_WlanStatsSwCryptoTKIPDeMIC_Object((1,3,6,1,4,1,12325,1,210,3,1,1,59),_WlanStatsSwCryptoTKIPDeMIC_Type())
wlanStatsSwCryptoTKIPDeMIC.setMaxAccess(_B)
if mibBuilder.loadTexts:wlanStatsSwCryptoTKIPDeMIC.setStatus(_A)
_WlanStatsCryptoTKIPCM_Type=Counter32
_WlanStatsCryptoTKIPCM_Object=MibTableColumn
wlanStatsCryptoTKIPCM=_WlanStatsCryptoTKIPCM_Object((1,3,6,1,4,1,12325,1,210,3,1,1,60),_WlanStatsCryptoTKIPCM_Type())
wlanStatsCryptoTKIPCM.setMaxAccess(_B)
if mibBuilder.loadTexts:wlanStatsCryptoTKIPCM.setStatus(_A)
if mibBuilder.loadTexts:wlanStatsCryptoTKIPCM.setUnits(_C)
_WlanStatsSwCryptoCCMP_Type=Counter32
_WlanStatsSwCryptoCCMP_Object=MibTableColumn
wlanStatsSwCryptoCCMP=_WlanStatsSwCryptoCCMP_Object((1,3,6,1,4,1,12325,1,210,3,1,1,61),_WlanStatsSwCryptoCCMP_Type())
wlanStatsSwCryptoCCMP.setMaxAccess(_B)
if mibBuilder.loadTexts:wlanStatsSwCryptoCCMP.setStatus(_A)
_WlanStatsSwCryptoWEP_Type=Counter32
_WlanStatsSwCryptoWEP_Object=MibTableColumn
wlanStatsSwCryptoWEP=_WlanStatsSwCryptoWEP_Object((1,3,6,1,4,1,12325,1,210,3,1,1,62),_WlanStatsSwCryptoWEP_Type())
wlanStatsSwCryptoWEP.setMaxAccess(_B)
if mibBuilder.loadTexts:wlanStatsSwCryptoWEP.setStatus(_A)
_WlanStatsCryptoCipherKeyRejected_Type=Counter32
_WlanStatsCryptoCipherKeyRejected_Object=MibTableColumn
wlanStatsCryptoCipherKeyRejected=_WlanStatsCryptoCipherKeyRejected_Object((1,3,6,1,4,1,12325,1,210,3,1,1,63),_WlanStatsCryptoCipherKeyRejected_Type())
wlanStatsCryptoCipherKeyRejected.setMaxAccess(_B)
if mibBuilder.loadTexts:wlanStatsCryptoCipherKeyRejected.setStatus(_A)
_WlanStatsCryptoNoKey_Type=Counter32
_WlanStatsCryptoNoKey_Object=MibTableColumn
wlanStatsCryptoNoKey=_WlanStatsCryptoNoKey_Object((1,3,6,1,4,1,12325,1,210,3,1,1,64),_WlanStatsCryptoNoKey_Type())
wlanStatsCryptoNoKey.setMaxAccess(_B)
if mibBuilder.loadTexts:wlanStatsCryptoNoKey.setStatus(_A)
_WlanStatsCryptoDeleteKeyFailed_Type=Counter32
_WlanStatsCryptoDeleteKeyFailed_Object=MibTableColumn
wlanStatsCryptoDeleteKeyFailed=_WlanStatsCryptoDeleteKeyFailed_Object((1,3,6,1,4,1,12325,1,210,3,1,1,65),_WlanStatsCryptoDeleteKeyFailed_Type())
wlanStatsCryptoDeleteKeyFailed.setMaxAccess(_B)
if mibBuilder.loadTexts:wlanStatsCryptoDeleteKeyFailed.setStatus(_A)
_WlanStatsCryptoUnknownCipher_Type=Counter32
_WlanStatsCryptoUnknownCipher_Object=MibTableColumn
wlanStatsCryptoUnknownCipher=_WlanStatsCryptoUnknownCipher_Object((1,3,6,1,4,1,12325,1,210,3,1,1,66),_WlanStatsCryptoUnknownCipher_Type())
wlanStatsCryptoUnknownCipher.setMaxAccess(_B)
if mibBuilder.loadTexts:wlanStatsCryptoUnknownCipher.setStatus(_A)
_WlanStatsCryptoAttachFailed_Type=Counter32
_WlanStatsCryptoAttachFailed_Object=MibTableColumn
wlanStatsCryptoAttachFailed=_WlanStatsCryptoAttachFailed_Object((1,3,6,1,4,1,12325,1,210,3,1,1,67),_WlanStatsCryptoAttachFailed_Type())
wlanStatsCryptoAttachFailed.setMaxAccess(_B)
if mibBuilder.loadTexts:wlanStatsCryptoAttachFailed.setStatus(_A)
_WlanStatsCryptoKeyFailed_Type=Counter32
_WlanStatsCryptoKeyFailed_Object=MibTableColumn
wlanStatsCryptoKeyFailed=_WlanStatsCryptoKeyFailed_Object((1,3,6,1,4,1,12325,1,210,3,1,1,68),_WlanStatsCryptoKeyFailed_Type())
wlanStatsCryptoKeyFailed.setMaxAccess(_B)
if mibBuilder.loadTexts:wlanStatsCryptoKeyFailed.setStatus(_A)
_WlanStatsCryptoEnMICFailed_Type=Counter32
_WlanStatsCryptoEnMICFailed_Object=MibTableColumn
wlanStatsCryptoEnMICFailed=_WlanStatsCryptoEnMICFailed_Object((1,3,6,1,4,1,12325,1,210,3,1,1,69),_WlanStatsCryptoEnMICFailed_Type())
wlanStatsCryptoEnMICFailed.setMaxAccess(_B)
if mibBuilder.loadTexts:wlanStatsCryptoEnMICFailed.setStatus(_A)
if mibBuilder.loadTexts:wlanStatsCryptoEnMICFailed.setUnits(_C)
_WlanStatsIBSSCapMismatch_Type=Counter32
_WlanStatsIBSSCapMismatch_Object=MibTableColumn
wlanStatsIBSSCapMismatch=_WlanStatsIBSSCapMismatch_Object((1,3,6,1,4,1,12325,1,210,3,1,1,70),_WlanStatsIBSSCapMismatch_Type())
wlanStatsIBSSCapMismatch.setMaxAccess(_B)
if mibBuilder.loadTexts:wlanStatsIBSSCapMismatch.setStatus(_A)
_WlanStatsUnassocStaPSPoll_Type=Counter32
_WlanStatsUnassocStaPSPoll_Object=MibTableColumn
wlanStatsUnassocStaPSPoll=_WlanStatsUnassocStaPSPoll_Object((1,3,6,1,4,1,12325,1,210,3,1,1,71),_WlanStatsUnassocStaPSPoll_Type())
wlanStatsUnassocStaPSPoll.setMaxAccess(_B)
if mibBuilder.loadTexts:wlanStatsUnassocStaPSPoll.setStatus(_A)
if mibBuilder.loadTexts:wlanStatsUnassocStaPSPoll.setUnits(_C)
_WlanStatsBadAidPSPoll_Type=Counter32
_WlanStatsBadAidPSPoll_Object=MibTableColumn
wlanStatsBadAidPSPoll=_WlanStatsBadAidPSPoll_Object((1,3,6,1,4,1,12325,1,210,3,1,1,72),_WlanStatsBadAidPSPoll_Type())
wlanStatsBadAidPSPoll.setMaxAccess(_B)
if mibBuilder.loadTexts:wlanStatsBadAidPSPoll.setStatus(_A)
if mibBuilder.loadTexts:wlanStatsBadAidPSPoll.setUnits(_C)
_WlanStatsEmptyPSPoll_Type=Counter32
_WlanStatsEmptyPSPoll_Object=MibTableColumn
wlanStatsEmptyPSPoll=_WlanStatsEmptyPSPoll_Object((1,3,6,1,4,1,12325,1,210,3,1,1,73),_WlanStatsEmptyPSPoll_Type())
wlanStatsEmptyPSPoll.setMaxAccess(_B)
if mibBuilder.loadTexts:wlanStatsEmptyPSPoll.setStatus(_A)
if mibBuilder.loadTexts:wlanStatsEmptyPSPoll.setUnits(_C)
_WlanStatsRxFFBadHdr_Type=Counter32
_WlanStatsRxFFBadHdr_Object=MibTableColumn
wlanStatsRxFFBadHdr=_WlanStatsRxFFBadHdr_Object((1,3,6,1,4,1,12325,1,210,3,1,1,74),_WlanStatsRxFFBadHdr_Type())
wlanStatsRxFFBadHdr.setMaxAccess(_B)
if mibBuilder.loadTexts:wlanStatsRxFFBadHdr.setStatus(_A)
if mibBuilder.loadTexts:wlanStatsRxFFBadHdr.setUnits(_C)
_WlanStatsRxFFTooShort_Type=Counter32
_WlanStatsRxFFTooShort_Object=MibTableColumn
wlanStatsRxFFTooShort=_WlanStatsRxFFTooShort_Object((1,3,6,1,4,1,12325,1,210,3,1,1,75),_WlanStatsRxFFTooShort_Type())
wlanStatsRxFFTooShort.setMaxAccess(_B)
if mibBuilder.loadTexts:wlanStatsRxFFTooShort.setStatus(_A)
if mibBuilder.loadTexts:wlanStatsRxFFTooShort.setUnits(_C)
_WlanStatsRxFFSplitError_Type=Counter32
_WlanStatsRxFFSplitError_Object=MibTableColumn
wlanStatsRxFFSplitError=_WlanStatsRxFFSplitError_Object((1,3,6,1,4,1,12325,1,210,3,1,1,76),_WlanStatsRxFFSplitError_Type())
wlanStatsRxFFSplitError.setMaxAccess(_B)
if mibBuilder.loadTexts:wlanStatsRxFFSplitError.setStatus(_A)
if mibBuilder.loadTexts:wlanStatsRxFFSplitError.setUnits(_C)
_WlanStatsRxFFDecap_Type=Counter32
_WlanStatsRxFFDecap_Object=MibTableColumn
wlanStatsRxFFDecap=_WlanStatsRxFFDecap_Object((1,3,6,1,4,1,12325,1,210,3,1,1,77),_WlanStatsRxFFDecap_Type())
wlanStatsRxFFDecap.setMaxAccess(_B)
if mibBuilder.loadTexts:wlanStatsRxFFDecap.setStatus(_A)
if mibBuilder.loadTexts:wlanStatsRxFFDecap.setUnits(_C)
_WlanStatsTxFFEncap_Type=Counter32
_WlanStatsTxFFEncap_Object=MibTableColumn
wlanStatsTxFFEncap=_WlanStatsTxFFEncap_Object((1,3,6,1,4,1,12325,1,210,3,1,1,78),_WlanStatsTxFFEncap_Type())
wlanStatsTxFFEncap.setMaxAccess(_B)
if mibBuilder.loadTexts:wlanStatsTxFFEncap.setStatus(_A)
if mibBuilder.loadTexts:wlanStatsTxFFEncap.setUnits(_C)
_WlanStatsRxBadBintval_Type=Counter32
_WlanStatsRxBadBintval_Object=MibTableColumn
wlanStatsRxBadBintval=_WlanStatsRxBadBintval_Object((1,3,6,1,4,1,12325,1,210,3,1,1,79),_WlanStatsRxBadBintval_Type())
wlanStatsRxBadBintval.setMaxAccess(_B)
if mibBuilder.loadTexts:wlanStatsRxBadBintval.setStatus(_A)
if mibBuilder.loadTexts:wlanStatsRxBadBintval.setUnits(_C)
_WlanStatsRxDemicFailed_Type=Counter32
_WlanStatsRxDemicFailed_Object=MibTableColumn
wlanStatsRxDemicFailed=_WlanStatsRxDemicFailed_Object((1,3,6,1,4,1,12325,1,210,3,1,1,80),_WlanStatsRxDemicFailed_Type())
wlanStatsRxDemicFailed.setMaxAccess(_B)
if mibBuilder.loadTexts:wlanStatsRxDemicFailed.setStatus(_A)
if mibBuilder.loadTexts:wlanStatsRxDemicFailed.setUnits(_C)
_WlanStatsRxDefragFailed_Type=Counter32
_WlanStatsRxDefragFailed_Object=MibTableColumn
wlanStatsRxDefragFailed=_WlanStatsRxDefragFailed_Object((1,3,6,1,4,1,12325,1,210,3,1,1,81),_WlanStatsRxDefragFailed_Type())
wlanStatsRxDefragFailed.setMaxAccess(_B)
if mibBuilder.loadTexts:wlanStatsRxDefragFailed.setStatus(_A)
if mibBuilder.loadTexts:wlanStatsRxDefragFailed.setUnits(_C)
_WlanStatsRxMgmt_Type=Counter32
_WlanStatsRxMgmt_Object=MibTableColumn
wlanStatsRxMgmt=_WlanStatsRxMgmt_Object((1,3,6,1,4,1,12325,1,210,3,1,1,82),_WlanStatsRxMgmt_Type())
wlanStatsRxMgmt.setMaxAccess(_B)
if mibBuilder.loadTexts:wlanStatsRxMgmt.setStatus(_A)
if mibBuilder.loadTexts:wlanStatsRxMgmt.setUnits(_C)
_WlanStatsRxActionMgmt_Type=Counter32
_WlanStatsRxActionMgmt_Object=MibTableColumn
wlanStatsRxActionMgmt=_WlanStatsRxActionMgmt_Object((1,3,6,1,4,1,12325,1,210,3,1,1,83),_WlanStatsRxActionMgmt_Type())
wlanStatsRxActionMgmt.setMaxAccess(_B)
if mibBuilder.loadTexts:wlanStatsRxActionMgmt.setStatus(_A)
if mibBuilder.loadTexts:wlanStatsRxActionMgmt.setUnits(_C)
_WlanStatsRxAMSDUTooShort_Type=Counter32
_WlanStatsRxAMSDUTooShort_Object=MibTableColumn
wlanStatsRxAMSDUTooShort=_WlanStatsRxAMSDUTooShort_Object((1,3,6,1,4,1,12325,1,210,3,1,1,84),_WlanStatsRxAMSDUTooShort_Type())
wlanStatsRxAMSDUTooShort.setMaxAccess(_B)
if mibBuilder.loadTexts:wlanStatsRxAMSDUTooShort.setStatus(_A)
if mibBuilder.loadTexts:wlanStatsRxAMSDUTooShort.setUnits(_C)
_WlanStatsRxAMSDUSplitError_Type=Counter32
_WlanStatsRxAMSDUSplitError_Object=MibTableColumn
wlanStatsRxAMSDUSplitError=_WlanStatsRxAMSDUSplitError_Object((1,3,6,1,4,1,12325,1,210,3,1,1,85),_WlanStatsRxAMSDUSplitError_Type())
wlanStatsRxAMSDUSplitError.setMaxAccess(_B)
if mibBuilder.loadTexts:wlanStatsRxAMSDUSplitError.setStatus(_A)
if mibBuilder.loadTexts:wlanStatsRxAMSDUSplitError.setUnits(_C)
_WlanStatsRxAMSDUDecap_Type=Counter32
_WlanStatsRxAMSDUDecap_Object=MibTableColumn
wlanStatsRxAMSDUDecap=_WlanStatsRxAMSDUDecap_Object((1,3,6,1,4,1,12325,1,210,3,1,1,86),_WlanStatsRxAMSDUDecap_Type())
wlanStatsRxAMSDUDecap.setMaxAccess(_B)
if mibBuilder.loadTexts:wlanStatsRxAMSDUDecap.setStatus(_A)
if mibBuilder.loadTexts:wlanStatsRxAMSDUDecap.setUnits(_C)
_WlanStatsTxAMSDUEncap_Type=Counter32
_WlanStatsTxAMSDUEncap_Object=MibTableColumn
wlanStatsTxAMSDUEncap=_WlanStatsTxAMSDUEncap_Object((1,3,6,1,4,1,12325,1,210,3,1,1,87),_WlanStatsTxAMSDUEncap_Type())
wlanStatsTxAMSDUEncap.setMaxAccess(_B)
if mibBuilder.loadTexts:wlanStatsTxAMSDUEncap.setStatus(_A)
if mibBuilder.loadTexts:wlanStatsTxAMSDUEncap.setUnits(_C)
_WlanStatsAMPDUBadBAR_Type=Counter32
_WlanStatsAMPDUBadBAR_Object=MibTableColumn
wlanStatsAMPDUBadBAR=_WlanStatsAMPDUBadBAR_Object((1,3,6,1,4,1,12325,1,210,3,1,1,88),_WlanStatsAMPDUBadBAR_Type())
wlanStatsAMPDUBadBAR.setMaxAccess(_B)
if mibBuilder.loadTexts:wlanStatsAMPDUBadBAR.setStatus(_A)
if mibBuilder.loadTexts:wlanStatsAMPDUBadBAR.setUnits(_C)
_WlanStatsAMPDUOowBar_Type=Counter32
_WlanStatsAMPDUOowBar_Object=MibTableColumn
wlanStatsAMPDUOowBar=_WlanStatsAMPDUOowBar_Object((1,3,6,1,4,1,12325,1,210,3,1,1,89),_WlanStatsAMPDUOowBar_Type())
wlanStatsAMPDUOowBar.setMaxAccess(_B)
if mibBuilder.loadTexts:wlanStatsAMPDUOowBar.setStatus(_A)
if mibBuilder.loadTexts:wlanStatsAMPDUOowBar.setUnits(_C)
_WlanStatsAMPDUMovedBAR_Type=Counter32
_WlanStatsAMPDUMovedBAR_Object=MibTableColumn
wlanStatsAMPDUMovedBAR=_WlanStatsAMPDUMovedBAR_Object((1,3,6,1,4,1,12325,1,210,3,1,1,90),_WlanStatsAMPDUMovedBAR_Type())
wlanStatsAMPDUMovedBAR.setMaxAccess(_B)
if mibBuilder.loadTexts:wlanStatsAMPDUMovedBAR.setStatus(_A)
if mibBuilder.loadTexts:wlanStatsAMPDUMovedBAR.setUnits(_C)
_WlanStatsAMPDURxBAR_Type=Counter32
_WlanStatsAMPDURxBAR_Object=MibTableColumn
wlanStatsAMPDURxBAR=_WlanStatsAMPDURxBAR_Object((1,3,6,1,4,1,12325,1,210,3,1,1,91),_WlanStatsAMPDURxBAR_Type())
wlanStatsAMPDURxBAR.setMaxAccess(_B)
if mibBuilder.loadTexts:wlanStatsAMPDURxBAR.setStatus(_A)
if mibBuilder.loadTexts:wlanStatsAMPDURxBAR.setUnits(_C)
_WlanStatsAMPDURxOor_Type=Counter32
_WlanStatsAMPDURxOor_Object=MibTableColumn
wlanStatsAMPDURxOor=_WlanStatsAMPDURxOor_Object((1,3,6,1,4,1,12325,1,210,3,1,1,92),_WlanStatsAMPDURxOor_Type())
wlanStatsAMPDURxOor.setMaxAccess(_B)
if mibBuilder.loadTexts:wlanStatsAMPDURxOor.setStatus(_A)
if mibBuilder.loadTexts:wlanStatsAMPDURxOor.setUnits(_C)
_WlanStatsAMPDURxCopied_Type=Counter32
_WlanStatsAMPDURxCopied_Object=MibTableColumn
wlanStatsAMPDURxCopied=_WlanStatsAMPDURxCopied_Object((1,3,6,1,4,1,12325,1,210,3,1,1,93),_WlanStatsAMPDURxCopied_Type())
wlanStatsAMPDURxCopied.setMaxAccess(_B)
if mibBuilder.loadTexts:wlanStatsAMPDURxCopied.setStatus(_A)
if mibBuilder.loadTexts:wlanStatsAMPDURxCopied.setUnits(_C)
_WlanStatsAMPDURxDropped_Type=Counter32
_WlanStatsAMPDURxDropped_Object=MibTableColumn
wlanStatsAMPDURxDropped=_WlanStatsAMPDURxDropped_Object((1,3,6,1,4,1,12325,1,210,3,1,1,94),_WlanStatsAMPDURxDropped_Type())
wlanStatsAMPDURxDropped.setMaxAccess(_B)
if mibBuilder.loadTexts:wlanStatsAMPDURxDropped.setStatus(_A)
if mibBuilder.loadTexts:wlanStatsAMPDURxDropped.setUnits(_C)
_WlanStatsTxDiscardBadState_Type=Counter32
_WlanStatsTxDiscardBadState_Object=MibTableColumn
wlanStatsTxDiscardBadState=_WlanStatsTxDiscardBadState_Object((1,3,6,1,4,1,12325,1,210,3,1,1,95),_WlanStatsTxDiscardBadState_Type())
wlanStatsTxDiscardBadState.setMaxAccess(_B)
if mibBuilder.loadTexts:wlanStatsTxDiscardBadState.setStatus(_A)
if mibBuilder.loadTexts:wlanStatsTxDiscardBadState.setUnits(_C)
_WlanStatsTxFailedNoAssoc_Type=Counter32
_WlanStatsTxFailedNoAssoc_Object=MibTableColumn
wlanStatsTxFailedNoAssoc=_WlanStatsTxFailedNoAssoc_Object((1,3,6,1,4,1,12325,1,210,3,1,1,96),_WlanStatsTxFailedNoAssoc_Type())
wlanStatsTxFailedNoAssoc.setMaxAccess(_B)
if mibBuilder.loadTexts:wlanStatsTxFailedNoAssoc.setStatus(_A)
if mibBuilder.loadTexts:wlanStatsTxFailedNoAssoc.setUnits(_C)
_WlanStatsTxClassifyFailed_Type=Counter32
_WlanStatsTxClassifyFailed_Object=MibTableColumn
wlanStatsTxClassifyFailed=_WlanStatsTxClassifyFailed_Object((1,3,6,1,4,1,12325,1,210,3,1,1,97),_WlanStatsTxClassifyFailed_Type())
wlanStatsTxClassifyFailed.setMaxAccess(_B)
if mibBuilder.loadTexts:wlanStatsTxClassifyFailed.setStatus(_A)
if mibBuilder.loadTexts:wlanStatsTxClassifyFailed.setUnits(_C)
_WlanStatsDwdsMcastDiscard_Type=Counter32
_WlanStatsDwdsMcastDiscard_Object=MibTableColumn
wlanStatsDwdsMcastDiscard=_WlanStatsDwdsMcastDiscard_Object((1,3,6,1,4,1,12325,1,210,3,1,1,98),_WlanStatsDwdsMcastDiscard_Type())
wlanStatsDwdsMcastDiscard.setMaxAccess(_B)
if mibBuilder.loadTexts:wlanStatsDwdsMcastDiscard.setStatus(_A)
if mibBuilder.loadTexts:wlanStatsDwdsMcastDiscard.setUnits(_C)
_WlanStatsHTAssocRejectNoHT_Type=Counter32
_WlanStatsHTAssocRejectNoHT_Object=MibTableColumn
wlanStatsHTAssocRejectNoHT=_WlanStatsHTAssocRejectNoHT_Object((1,3,6,1,4,1,12325,1,210,3,1,1,99),_WlanStatsHTAssocRejectNoHT_Type())
wlanStatsHTAssocRejectNoHT.setMaxAccess(_B)
if mibBuilder.loadTexts:wlanStatsHTAssocRejectNoHT.setStatus(_A)
if mibBuilder.loadTexts:wlanStatsHTAssocRejectNoHT.setUnits(_C)
_WlanStatsHTAssocDowngrade_Type=Counter32
_WlanStatsHTAssocDowngrade_Object=MibTableColumn
wlanStatsHTAssocDowngrade=_WlanStatsHTAssocDowngrade_Object((1,3,6,1,4,1,12325,1,210,3,1,1,100),_WlanStatsHTAssocDowngrade_Type())
wlanStatsHTAssocDowngrade.setMaxAccess(_B)
if mibBuilder.loadTexts:wlanStatsHTAssocDowngrade.setStatus(_A)
_WlanStatsHTAssocRateMismatch_Type=Counter32
_WlanStatsHTAssocRateMismatch_Object=MibTableColumn
wlanStatsHTAssocRateMismatch=_WlanStatsHTAssocRateMismatch_Object((1,3,6,1,4,1,12325,1,210,3,1,1,101),_WlanStatsHTAssocRateMismatch_Type())
wlanStatsHTAssocRateMismatch.setMaxAccess(_B)
if mibBuilder.loadTexts:wlanStatsHTAssocRateMismatch.setStatus(_A)
if mibBuilder.loadTexts:wlanStatsHTAssocRateMismatch.setUnits(_C)
_WlanStatsAMPDURxAge_Type=Counter32
_WlanStatsAMPDURxAge_Object=MibTableColumn
wlanStatsAMPDURxAge=_WlanStatsAMPDURxAge_Object((1,3,6,1,4,1,12325,1,210,3,1,1,102),_WlanStatsAMPDURxAge_Type())
wlanStatsAMPDURxAge.setMaxAccess(_B)
if mibBuilder.loadTexts:wlanStatsAMPDURxAge.setStatus(_A)
if mibBuilder.loadTexts:wlanStatsAMPDURxAge.setUnits(_C)
_WlanStatsAMPDUMoved_Type=Counter32
_WlanStatsAMPDUMoved_Object=MibTableColumn
wlanStatsAMPDUMoved=_WlanStatsAMPDUMoved_Object((1,3,6,1,4,1,12325,1,210,3,1,1,103),_WlanStatsAMPDUMoved_Type())
wlanStatsAMPDUMoved.setMaxAccess(_B)
if mibBuilder.loadTexts:wlanStatsAMPDUMoved.setStatus(_A)
_WlanStatsADDBADisabledReject_Type=Counter32
_WlanStatsADDBADisabledReject_Object=MibTableColumn
wlanStatsADDBADisabledReject=_WlanStatsADDBADisabledReject_Object((1,3,6,1,4,1,12325,1,210,3,1,1,104),_WlanStatsADDBADisabledReject_Type())
wlanStatsADDBADisabledReject.setMaxAccess(_B)
if mibBuilder.loadTexts:wlanStatsADDBADisabledReject.setStatus(_A)
if mibBuilder.loadTexts:wlanStatsADDBADisabledReject.setUnits(_C)
_WlanStatsADDBANoRequest_Type=Counter32
_WlanStatsADDBANoRequest_Object=MibTableColumn
wlanStatsADDBANoRequest=_WlanStatsADDBANoRequest_Object((1,3,6,1,4,1,12325,1,210,3,1,1,105),_WlanStatsADDBANoRequest_Type())
wlanStatsADDBANoRequest.setMaxAccess(_B)
if mibBuilder.loadTexts:wlanStatsADDBANoRequest.setStatus(_A)
if mibBuilder.loadTexts:wlanStatsADDBANoRequest.setUnits(_C)
_WlanStatsADDBABadToken_Type=Counter32
_WlanStatsADDBABadToken_Object=MibTableColumn
wlanStatsADDBABadToken=_WlanStatsADDBABadToken_Object((1,3,6,1,4,1,12325,1,210,3,1,1,106),_WlanStatsADDBABadToken_Type())
wlanStatsADDBABadToken.setMaxAccess(_B)
if mibBuilder.loadTexts:wlanStatsADDBABadToken.setStatus(_A)
if mibBuilder.loadTexts:wlanStatsADDBABadToken.setUnits(_C)
_WlanStatsADDBABadPolicy_Type=Counter32
_WlanStatsADDBABadPolicy_Object=MibTableColumn
wlanStatsADDBABadPolicy=_WlanStatsADDBABadPolicy_Object((1,3,6,1,4,1,12325,1,210,3,1,1,107),_WlanStatsADDBABadPolicy_Type())
wlanStatsADDBABadPolicy.setMaxAccess(_B)
if mibBuilder.loadTexts:wlanStatsADDBABadPolicy.setStatus(_A)
if mibBuilder.loadTexts:wlanStatsADDBABadPolicy.setUnits(_C)
_WlanStatsAMPDUStopped_Type=Counter32
_WlanStatsAMPDUStopped_Object=MibTableColumn
wlanStatsAMPDUStopped=_WlanStatsAMPDUStopped_Object((1,3,6,1,4,1,12325,1,210,3,1,1,108),_WlanStatsAMPDUStopped_Type())
wlanStatsAMPDUStopped.setMaxAccess(_B)
if mibBuilder.loadTexts:wlanStatsAMPDUStopped.setStatus(_A)
_WlanStatsAMPDUStopFailed_Type=Counter32
_WlanStatsAMPDUStopFailed_Object=MibTableColumn
wlanStatsAMPDUStopFailed=_WlanStatsAMPDUStopFailed_Object((1,3,6,1,4,1,12325,1,210,3,1,1,109),_WlanStatsAMPDUStopFailed_Type())
wlanStatsAMPDUStopFailed.setMaxAccess(_B)
if mibBuilder.loadTexts:wlanStatsAMPDUStopFailed.setStatus(_A)
_WlanStatsAMPDURxReorder_Type=Counter32
_WlanStatsAMPDURxReorder_Object=MibTableColumn
wlanStatsAMPDURxReorder=_WlanStatsAMPDURxReorder_Object((1,3,6,1,4,1,12325,1,210,3,1,1,110),_WlanStatsAMPDURxReorder_Type())
wlanStatsAMPDURxReorder.setMaxAccess(_B)
if mibBuilder.loadTexts:wlanStatsAMPDURxReorder.setStatus(_A)
if mibBuilder.loadTexts:wlanStatsAMPDURxReorder.setUnits(_C)
_WlanStatsScansBackground_Type=Counter32
_WlanStatsScansBackground_Object=MibTableColumn
wlanStatsScansBackground=_WlanStatsScansBackground_Object((1,3,6,1,4,1,12325,1,210,3,1,1,111),_WlanStatsScansBackground_Type())
wlanStatsScansBackground.setMaxAccess(_B)
if mibBuilder.loadTexts:wlanStatsScansBackground.setStatus(_A)
_WlanLastDeauthReason_Type=WlanMgmtReasonCode
_WlanLastDeauthReason_Object=MibTableColumn
wlanLastDeauthReason=_WlanLastDeauthReason_Object((1,3,6,1,4,1,12325,1,210,3,1,1,112),_WlanLastDeauthReason_Type())
wlanLastDeauthReason.setMaxAccess(_B)
if mibBuilder.loadTexts:wlanLastDeauthReason.setStatus(_A)
_WlanLastDissasocReason_Type=WlanMgmtReasonCode
_WlanLastDissasocReason_Object=MibTableColumn
wlanLastDissasocReason=_WlanLastDissasocReason_Object((1,3,6,1,4,1,12325,1,210,3,1,1,113),_WlanLastDissasocReason_Type())
wlanLastDissasocReason.setMaxAccess(_B)
if mibBuilder.loadTexts:wlanLastDissasocReason.setStatus(_A)
_WlanLastAuthFailReason_Type=WlanMgmtReasonCode
_WlanLastAuthFailReason_Object=MibTableColumn
wlanLastAuthFailReason=_WlanLastAuthFailReason_Object((1,3,6,1,4,1,12325,1,210,3,1,1,114),_WlanLastAuthFailReason_Type())
wlanLastAuthFailReason.setMaxAccess(_B)
if mibBuilder.loadTexts:wlanLastAuthFailReason.setStatus(_A)
_WlanStatsBeaconMissedEvents_Type=Counter32
_WlanStatsBeaconMissedEvents_Object=MibTableColumn
wlanStatsBeaconMissedEvents=_WlanStatsBeaconMissedEvents_Object((1,3,6,1,4,1,12325,1,210,3,1,1,115),_WlanStatsBeaconMissedEvents_Type())
wlanStatsBeaconMissedEvents.setMaxAccess(_B)
if mibBuilder.loadTexts:wlanStatsBeaconMissedEvents.setStatus(_A)
if mibBuilder.loadTexts:wlanStatsBeaconMissedEvents.setUnits(_C)
_WlanStatsRxDiscardBadStates_Type=Counter32
_WlanStatsRxDiscardBadStates_Object=MibTableColumn
wlanStatsRxDiscardBadStates=_WlanStatsRxDiscardBadStates_Object((1,3,6,1,4,1,12325,1,210,3,1,1,116),_WlanStatsRxDiscardBadStates_Type())
wlanStatsRxDiscardBadStates.setMaxAccess(_B)
if mibBuilder.loadTexts:wlanStatsRxDiscardBadStates.setStatus(_A)
if mibBuilder.loadTexts:wlanStatsRxDiscardBadStates.setUnits(_C)
_WlanStatsFFFlushed_Type=Counter32
_WlanStatsFFFlushed_Object=MibTableColumn
wlanStatsFFFlushed=_WlanStatsFFFlushed_Object((1,3,6,1,4,1,12325,1,210,3,1,1,117),_WlanStatsFFFlushed_Type())
wlanStatsFFFlushed.setMaxAccess(_B)
if mibBuilder.loadTexts:wlanStatsFFFlushed.setStatus(_A)
if mibBuilder.loadTexts:wlanStatsFFFlushed.setUnits(_C)
_WlanStatsTxControlFrames_Type=Counter32
_WlanStatsTxControlFrames_Object=MibTableColumn
wlanStatsTxControlFrames=_WlanStatsTxControlFrames_Object((1,3,6,1,4,1,12325,1,210,3,1,1,118),_WlanStatsTxControlFrames_Type())
wlanStatsTxControlFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:wlanStatsTxControlFrames.setStatus(_A)
if mibBuilder.loadTexts:wlanStatsTxControlFrames.setUnits(_C)
_WlanStatsAMPDURexmt_Type=Counter32
_WlanStatsAMPDURexmt_Object=MibTableColumn
wlanStatsAMPDURexmt=_WlanStatsAMPDURexmt_Object((1,3,6,1,4,1,12325,1,210,3,1,1,119),_WlanStatsAMPDURexmt_Type())
wlanStatsAMPDURexmt.setMaxAccess(_B)
if mibBuilder.loadTexts:wlanStatsAMPDURexmt.setStatus(_A)
if mibBuilder.loadTexts:wlanStatsAMPDURexmt.setUnits(_C)
_WlanStatsAMPDURexmtFailed_Type=Counter32
_WlanStatsAMPDURexmtFailed_Object=MibTableColumn
wlanStatsAMPDURexmtFailed=_WlanStatsAMPDURexmtFailed_Object((1,3,6,1,4,1,12325,1,210,3,1,1,120),_WlanStatsAMPDURexmtFailed_Type())
wlanStatsAMPDURexmtFailed.setMaxAccess(_B)
if mibBuilder.loadTexts:wlanStatsAMPDURexmtFailed.setStatus(_A)
if mibBuilder.loadTexts:wlanStatsAMPDURexmtFailed.setUnits(_C)
class _WlanStatsReset_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_U,1),('clear',2)))
_WlanStatsReset_Type.__name__=_E
_WlanStatsReset_Object=MibTableColumn
wlanStatsReset=_WlanStatsReset_Object((1,3,6,1,4,1,12325,1,210,3,1,1,121),_WlanStatsReset_Type())
wlanStatsReset.setMaxAccess(_D)
if mibBuilder.loadTexts:wlanStatsReset.setStatus(_A)
_BegemotWlanWep_ObjectIdentity=ObjectIdentity
begemotWlanWep=_BegemotWlanWep_ObjectIdentity((1,3,6,1,4,1,12325,1,210,4))
_WlanWepInterfaceTable_Object=MibTable
wlanWepInterfaceTable=_WlanWepInterfaceTable_Object((1,3,6,1,4,1,12325,1,210,4,1))
if mibBuilder.loadTexts:wlanWepInterfaceTable.setStatus(_A)
_WlanWepInterfaceEntry_Object=MibTableRow
wlanWepInterfaceEntry=_WlanWepInterfaceEntry_Object((1,3,6,1,4,1,12325,1,210,4,1,1))
wlanWepInterfaceEntry.setIndexNames((0,_F,_G))
if mibBuilder.loadTexts:wlanWepInterfaceEntry.setStatus(_A)
class _WlanWepMode_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_Q,0),('on',1),('mixed',2)))
_WlanWepMode_Type.__name__=_E
_WlanWepMode_Object=MibTableColumn
wlanWepMode=_WlanWepMode_Object((1,3,6,1,4,1,12325,1,210,4,1,1,1),_WlanWepMode_Type())
wlanWepMode.setMaxAccess(_D)
if mibBuilder.loadTexts:wlanWepMode.setStatus(_A)
_WlanWepDefTxKey_Type=Integer32
_WlanWepDefTxKey_Object=MibTableColumn
wlanWepDefTxKey=_WlanWepDefTxKey_Object((1,3,6,1,4,1,12325,1,210,4,1,1,2),_WlanWepDefTxKey_Type())
wlanWepDefTxKey.setMaxAccess(_D)
if mibBuilder.loadTexts:wlanWepDefTxKey.setStatus(_A)
_WlanWepKeyTable_Object=MibTable
wlanWepKeyTable=_WlanWepKeyTable_Object((1,3,6,1,4,1,12325,1,210,4,2))
if mibBuilder.loadTexts:wlanWepKeyTable.setStatus(_A)
_WlanWepKeyEntry_Object=MibTableRow
wlanWepKeyEntry=_WlanWepKeyEntry_Object((1,3,6,1,4,1,12325,1,210,4,2,1))
wlanWepKeyEntry.setIndexNames((0,_F,_G),(0,_F,_o))
if mibBuilder.loadTexts:wlanWepKeyEntry.setStatus(_A)
class _WlanWepKeyID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4))
_WlanWepKeyID_Type.__name__=_E
_WlanWepKeyID_Object=MibTableColumn
wlanWepKeyID=_WlanWepKeyID_Object((1,3,6,1,4,1,12325,1,210,4,2,1,1),_WlanWepKeyID_Type())
wlanWepKeyID.setMaxAccess(_D)
if mibBuilder.loadTexts:wlanWepKeyID.setStatus(_A)
_WlanWepKeyLength_Type=Integer32
_WlanWepKeyLength_Object=MibTableColumn
wlanWepKeyLength=_WlanWepKeyLength_Object((1,3,6,1,4,1,12325,1,210,4,2,1,2),_WlanWepKeyLength_Type())
wlanWepKeyLength.setMaxAccess(_B)
if mibBuilder.loadTexts:wlanWepKeyLength.setStatus(_A)
_WlanWepKeySet_Type=OctetString
_WlanWepKeySet_Object=MibTableColumn
wlanWepKeySet=_WlanWepKeySet_Object((1,3,6,1,4,1,12325,1,210,4,2,1,3),_WlanWepKeySet_Type())
wlanWepKeySet.setMaxAccess(_D)
if mibBuilder.loadTexts:wlanWepKeySet.setStatus(_A)
_WlanWepKeyHash_Type=OctetString
_WlanWepKeyHash_Object=MibTableColumn
wlanWepKeyHash=_WlanWepKeyHash_Object((1,3,6,1,4,1,12325,1,210,4,2,1,4),_WlanWepKeyHash_Type())
wlanWepKeyHash.setMaxAccess(_B)
if mibBuilder.loadTexts:wlanWepKeyHash.setStatus(_A)
_WlanWepKeyStatus_Type=RowStatus
_WlanWepKeyStatus_Object=MibTableColumn
wlanWepKeyStatus=_WlanWepKeyStatus_Object((1,3,6,1,4,1,12325,1,210,4,2,1,5),_WlanWepKeyStatus_Type())
wlanWepKeyStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:wlanWepKeyStatus.setStatus(_A)
_BegemotWlanMACAccessControl_ObjectIdentity=ObjectIdentity
begemotWlanMACAccessControl=_BegemotWlanMACAccessControl_ObjectIdentity((1,3,6,1,4,1,12325,1,210,5))
_WlanMACAccessControlTable_Object=MibTable
wlanMACAccessControlTable=_WlanMACAccessControlTable_Object((1,3,6,1,4,1,12325,1,210,5,1))
if mibBuilder.loadTexts:wlanMACAccessControlTable.setStatus(_A)
_WlanMACAccessControlEntry_Object=MibTableRow
wlanMACAccessControlEntry=_WlanMACAccessControlEntry_Object((1,3,6,1,4,1,12325,1,210,5,1,1))
wlanMACAccessControlEntry.setIndexNames((0,_F,_G))
if mibBuilder.loadTexts:wlanMACAccessControlEntry.setStatus(_A)
class _WlanMACAccessControlPolicy_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,7)));namedValues=NamedValues(*(('open',0),('allow',1),('deny',2),('radius',7)))
_WlanMACAccessControlPolicy_Type.__name__=_E
_WlanMACAccessControlPolicy_Object=MibTableColumn
wlanMACAccessControlPolicy=_WlanMACAccessControlPolicy_Object((1,3,6,1,4,1,12325,1,210,5,1,1,1),_WlanMACAccessControlPolicy_Type())
wlanMACAccessControlPolicy.setMaxAccess(_D)
if mibBuilder.loadTexts:wlanMACAccessControlPolicy.setStatus(_A)
_WlanMACAccessControlNacl_Type=Counter32
_WlanMACAccessControlNacl_Object=MibTableColumn
wlanMACAccessControlNacl=_WlanMACAccessControlNacl_Object((1,3,6,1,4,1,12325,1,210,5,1,1,2),_WlanMACAccessControlNacl_Type())
wlanMACAccessControlNacl.setMaxAccess(_B)
if mibBuilder.loadTexts:wlanMACAccessControlNacl.setStatus(_A)
class _WlanMACAccessControlFlush_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_U,0),('flush',1)))
_WlanMACAccessControlFlush_Type.__name__=_E
_WlanMACAccessControlFlush_Object=MibTableColumn
wlanMACAccessControlFlush=_WlanMACAccessControlFlush_Object((1,3,6,1,4,1,12325,1,210,5,1,1,3),_WlanMACAccessControlFlush_Type())
wlanMACAccessControlFlush.setMaxAccess(_D)
if mibBuilder.loadTexts:wlanMACAccessControlFlush.setStatus(_A)
_WlanMACAccessControlMACTable_Object=MibTable
wlanMACAccessControlMACTable=_WlanMACAccessControlMACTable_Object((1,3,6,1,4,1,12325,1,210,5,2))
if mibBuilder.loadTexts:wlanMACAccessControlMACTable.setStatus(_A)
_WlanMACAccessControlMACEntry_Object=MibTableRow
wlanMACAccessControlMACEntry=_WlanMACAccessControlMACEntry_Object((1,3,6,1,4,1,12325,1,210,5,2,1))
wlanMACAccessControlMACEntry.setIndexNames((0,_F,_G),(0,_F,_p))
if mibBuilder.loadTexts:wlanMACAccessControlMACEntry.setStatus(_A)
_WlanMACAccessControlMAC_Type=MacAddress
_WlanMACAccessControlMAC_Object=MibTableColumn
wlanMACAccessControlMAC=_WlanMACAccessControlMAC_Object((1,3,6,1,4,1,12325,1,210,5,2,1,1),_WlanMACAccessControlMAC_Type())
wlanMACAccessControlMAC.setMaxAccess(_D)
if mibBuilder.loadTexts:wlanMACAccessControlMAC.setStatus(_A)
_WlanMACAccessControlMACStatus_Type=RowStatus
_WlanMACAccessControlMACStatus_Object=MibTableColumn
wlanMACAccessControlMACStatus=_WlanMACAccessControlMACStatus_Object((1,3,6,1,4,1,12325,1,210,5,2,1,2),_WlanMACAccessControlMACStatus_Type())
wlanMACAccessControlMACStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:wlanMACAccessControlMACStatus.setStatus(_A)
_BegemotWlanMeshRouting_ObjectIdentity=ObjectIdentity
begemotWlanMeshRouting=_BegemotWlanMeshRouting_ObjectIdentity((1,3,6,1,4,1,12325,1,210,6))
_WlanMeshRoutingConfig_ObjectIdentity=ObjectIdentity
wlanMeshRoutingConfig=_WlanMeshRoutingConfig_ObjectIdentity((1,3,6,1,4,1,12325,1,210,6,1))
class _WlanMeshMaxRetries_Type(Integer32):defaultValue=2
_WlanMeshMaxRetries_Type.__name__=_E
_WlanMeshMaxRetries_Object=MibScalar
wlanMeshMaxRetries=_WlanMeshMaxRetries_Object((1,3,6,1,4,1,12325,1,210,6,1,1),_WlanMeshMaxRetries_Type())
wlanMeshMaxRetries.setMaxAccess(_D)
if mibBuilder.loadTexts:wlanMeshMaxRetries.setStatus(_A)
class _WlanMeshConfirmTimeout_Type(Integer32):defaultValue=40
_WlanMeshConfirmTimeout_Type.__name__=_E
_WlanMeshConfirmTimeout_Object=MibScalar
wlanMeshConfirmTimeout=_WlanMeshConfirmTimeout_Object((1,3,6,1,4,1,12325,1,210,6,1,2),_WlanMeshConfirmTimeout_Type())
wlanMeshConfirmTimeout.setMaxAccess(_D)
if mibBuilder.loadTexts:wlanMeshConfirmTimeout.setStatus(_A)
if mibBuilder.loadTexts:wlanMeshConfirmTimeout.setUnits(_H)
class _WlanMeshHoldingTimeout_Type(Integer32):defaultValue=40
_WlanMeshHoldingTimeout_Type.__name__=_E
_WlanMeshHoldingTimeout_Object=MibScalar
wlanMeshHoldingTimeout=_WlanMeshHoldingTimeout_Object((1,3,6,1,4,1,12325,1,210,6,1,3),_WlanMeshHoldingTimeout_Type())
wlanMeshHoldingTimeout.setMaxAccess(_D)
if mibBuilder.loadTexts:wlanMeshHoldingTimeout.setStatus(_A)
if mibBuilder.loadTexts:wlanMeshHoldingTimeout.setUnits(_H)
class _WlanMeshRetryTimeout_Type(Integer32):defaultValue=40
_WlanMeshRetryTimeout_Type.__name__=_E
_WlanMeshRetryTimeout_Object=MibScalar
wlanMeshRetryTimeout=_WlanMeshRetryTimeout_Object((1,3,6,1,4,1,12325,1,210,6,1,4),_WlanMeshRetryTimeout_Type())
wlanMeshRetryTimeout.setMaxAccess(_D)
if mibBuilder.loadTexts:wlanMeshRetryTimeout.setStatus(_A)
if mibBuilder.loadTexts:wlanMeshRetryTimeout.setUnits(_H)
_WlanMeshInterface_ObjectIdentity=ObjectIdentity
wlanMeshInterface=_WlanMeshInterface_ObjectIdentity((1,3,6,1,4,1,12325,1,210,6,2))
_WlanMeshInterfaceTable_Object=MibTable
wlanMeshInterfaceTable=_WlanMeshInterfaceTable_Object((1,3,6,1,4,1,12325,1,210,6,2,1))
if mibBuilder.loadTexts:wlanMeshInterfaceTable.setStatus(_A)
_WlanMeshInterfaceEntry_Object=MibTableRow
wlanMeshInterfaceEntry=_WlanMeshInterfaceEntry_Object((1,3,6,1,4,1,12325,1,210,6,2,1,1))
wlanMeshInterfaceEntry.setIndexNames((0,_F,_G))
if mibBuilder.loadTexts:wlanMeshInterfaceEntry.setStatus(_A)
class _WlanMeshId_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_WlanMeshId_Type.__name__=_L
_WlanMeshId_Object=MibTableColumn
wlanMeshId=_WlanMeshId_Object((1,3,6,1,4,1,12325,1,210,6,2,1,1,1),_WlanMeshId_Type())
wlanMeshId.setMaxAccess(_D)
if mibBuilder.loadTexts:wlanMeshId.setStatus(_A)
class _WlanMeshTTL_Type(Integer32):defaultValue=31
_WlanMeshTTL_Type.__name__=_E
_WlanMeshTTL_Object=MibTableColumn
wlanMeshTTL=_WlanMeshTTL_Object((1,3,6,1,4,1,12325,1,210,6,2,1,1,2),_WlanMeshTTL_Type())
wlanMeshTTL.setMaxAccess(_D)
if mibBuilder.loadTexts:wlanMeshTTL.setStatus(_A)
if mibBuilder.loadTexts:wlanMeshTTL.setUnits('hops')
class _WlanMeshPeeringEnabled_Type(TruthValue):defaultValue=1
_WlanMeshPeeringEnabled_Type.__name__=_I
_WlanMeshPeeringEnabled_Object=MibTableColumn
wlanMeshPeeringEnabled=_WlanMeshPeeringEnabled_Object((1,3,6,1,4,1,12325,1,210,6,2,1,1,3),_WlanMeshPeeringEnabled_Type())
wlanMeshPeeringEnabled.setMaxAccess(_D)
if mibBuilder.loadTexts:wlanMeshPeeringEnabled.setStatus(_A)
class _WlanMeshForwardingEnabled_Type(TruthValue):defaultValue=1
_WlanMeshForwardingEnabled_Type.__name__=_I
_WlanMeshForwardingEnabled_Object=MibTableColumn
wlanMeshForwardingEnabled=_WlanMeshForwardingEnabled_Object((1,3,6,1,4,1,12325,1,210,6,2,1,1,4),_WlanMeshForwardingEnabled_Type())
wlanMeshForwardingEnabled.setMaxAccess(_D)
if mibBuilder.loadTexts:wlanMeshForwardingEnabled.setStatus(_A)
class _WlanMeshMetric_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_T,0),('airtime',1)))
_WlanMeshMetric_Type.__name__=_E
_WlanMeshMetric_Object=MibTableColumn
wlanMeshMetric=_WlanMeshMetric_Object((1,3,6,1,4,1,12325,1,210,6,2,1,1,5),_WlanMeshMetric_Type())
wlanMeshMetric.setMaxAccess(_D)
if mibBuilder.loadTexts:wlanMeshMetric.setStatus(_A)
class _WlanMeshPath_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_T,0),('hwmp',1)))
_WlanMeshPath_Type.__name__=_E
_WlanMeshPath_Object=MibTableColumn
wlanMeshPath=_WlanMeshPath_Object((1,3,6,1,4,1,12325,1,210,6,2,1,1,6),_WlanMeshPath_Type())
wlanMeshPath.setMaxAccess(_D)
if mibBuilder.loadTexts:wlanMeshPath.setStatus(_A)
class _WlanMeshRoutesFlush_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_U,0),('flush',1)))
_WlanMeshRoutesFlush_Type.__name__=_E
_WlanMeshRoutesFlush_Object=MibTableColumn
wlanMeshRoutesFlush=_WlanMeshRoutesFlush_Object((1,3,6,1,4,1,12325,1,210,6,2,1,1,7),_WlanMeshRoutesFlush_Type())
wlanMeshRoutesFlush.setMaxAccess(_D)
if mibBuilder.loadTexts:wlanMeshRoutesFlush.setStatus(_A)
_WlanMeshNeighborTable_Object=MibTable
wlanMeshNeighborTable=_WlanMeshNeighborTable_Object((1,3,6,1,4,1,12325,1,210,6,2,2))
if mibBuilder.loadTexts:wlanMeshNeighborTable.setStatus(_A)
_WlanMeshNeighborEntry_Object=MibTableRow
wlanMeshNeighborEntry=_WlanMeshNeighborEntry_Object((1,3,6,1,4,1,12325,1,210,6,2,2,1))
wlanMeshNeighborEntry.setIndexNames((0,_F,_G),(0,_F,_q))
if mibBuilder.loadTexts:wlanMeshNeighborEntry.setStatus(_A)
_WlanMeshNeighborAddress_Type=MacAddress
_WlanMeshNeighborAddress_Object=MibTableColumn
wlanMeshNeighborAddress=_WlanMeshNeighborAddress_Object((1,3,6,1,4,1,12325,1,210,6,2,2,1,1),_WlanMeshNeighborAddress_Type())
wlanMeshNeighborAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:wlanMeshNeighborAddress.setStatus(_A)
_WlanMeshNeighborFrequency_Type=Integer32
_WlanMeshNeighborFrequency_Object=MibTableColumn
wlanMeshNeighborFrequency=_WlanMeshNeighborFrequency_Object((1,3,6,1,4,1,12325,1,210,6,2,2,1,2),_WlanMeshNeighborFrequency_Type())
wlanMeshNeighborFrequency.setMaxAccess(_B)
if mibBuilder.loadTexts:wlanMeshNeighborFrequency.setStatus(_A)
_WlanMeshNeighborLocalId_Type=Integer32
_WlanMeshNeighborLocalId_Object=MibTableColumn
wlanMeshNeighborLocalId=_WlanMeshNeighborLocalId_Object((1,3,6,1,4,1,12325,1,210,6,2,2,1,3),_WlanMeshNeighborLocalId_Type())
wlanMeshNeighborLocalId.setMaxAccess(_B)
if mibBuilder.loadTexts:wlanMeshNeighborLocalId.setStatus(_A)
_WlanMeshNeighborPeerId_Type=Integer32
_WlanMeshNeighborPeerId_Object=MibTableColumn
wlanMeshNeighborPeerId=_WlanMeshNeighborPeerId_Object((1,3,6,1,4,1,12325,1,210,6,2,2,1,4),_WlanMeshNeighborPeerId_Type())
wlanMeshNeighborPeerId.setMaxAccess(_B)
if mibBuilder.loadTexts:wlanMeshNeighborPeerId.setStatus(_A)
class _WlanMeshNeighborPeerState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5)));namedValues=NamedValues(*(('idle',0),('openTx',1),('openRx',2),('confirmRx',3),('established',4),('closing',5)))
_WlanMeshNeighborPeerState_Type.__name__=_E
_WlanMeshNeighborPeerState_Object=MibTableColumn
wlanMeshNeighborPeerState=_WlanMeshNeighborPeerState_Object((1,3,6,1,4,1,12325,1,210,6,2,2,1,5),_WlanMeshNeighborPeerState_Type())
wlanMeshNeighborPeerState.setMaxAccess(_B)
if mibBuilder.loadTexts:wlanMeshNeighborPeerState.setStatus(_A)
_WlanMeshNeighborCurrentTXRate_Type=Integer32
_WlanMeshNeighborCurrentTXRate_Object=MibTableColumn
wlanMeshNeighborCurrentTXRate=_WlanMeshNeighborCurrentTXRate_Object((1,3,6,1,4,1,12325,1,210,6,2,2,1,6),_WlanMeshNeighborCurrentTXRate_Type())
wlanMeshNeighborCurrentTXRate.setMaxAccess(_B)
if mibBuilder.loadTexts:wlanMeshNeighborCurrentTXRate.setStatus(_A)
_WlanMeshNeighborRxSignalStrength_Type=Integer32
_WlanMeshNeighborRxSignalStrength_Object=MibTableColumn
wlanMeshNeighborRxSignalStrength=_WlanMeshNeighborRxSignalStrength_Object((1,3,6,1,4,1,12325,1,210,6,2,2,1,7),_WlanMeshNeighborRxSignalStrength_Type())
wlanMeshNeighborRxSignalStrength.setMaxAccess(_B)
if mibBuilder.loadTexts:wlanMeshNeighborRxSignalStrength.setStatus(_A)
_WlanMeshNeighborIdleTimer_Type=Integer32
_WlanMeshNeighborIdleTimer_Object=MibTableColumn
wlanMeshNeighborIdleTimer=_WlanMeshNeighborIdleTimer_Object((1,3,6,1,4,1,12325,1,210,6,2,2,1,8),_WlanMeshNeighborIdleTimer_Type())
wlanMeshNeighborIdleTimer.setMaxAccess(_B)
if mibBuilder.loadTexts:wlanMeshNeighborIdleTimer.setStatus(_A)
if mibBuilder.loadTexts:wlanMeshNeighborIdleTimer.setUnits(_M)
_WlanMeshNeighborTxSequenceNo_Type=Integer32
_WlanMeshNeighborTxSequenceNo_Object=MibTableColumn
wlanMeshNeighborTxSequenceNo=_WlanMeshNeighborTxSequenceNo_Object((1,3,6,1,4,1,12325,1,210,6,2,2,1,9),_WlanMeshNeighborTxSequenceNo_Type())
wlanMeshNeighborTxSequenceNo.setMaxAccess(_B)
if mibBuilder.loadTexts:wlanMeshNeighborTxSequenceNo.setStatus(_A)
_WlanMeshNeighborRxSequenceNo_Type=Integer32
_WlanMeshNeighborRxSequenceNo_Object=MibTableColumn
wlanMeshNeighborRxSequenceNo=_WlanMeshNeighborRxSequenceNo_Object((1,3,6,1,4,1,12325,1,210,6,2,2,1,10),_WlanMeshNeighborRxSequenceNo_Type())
wlanMeshNeighborRxSequenceNo.setMaxAccess(_B)
if mibBuilder.loadTexts:wlanMeshNeighborRxSequenceNo.setStatus(_A)
_WlanMeshRoute_ObjectIdentity=ObjectIdentity
wlanMeshRoute=_WlanMeshRoute_ObjectIdentity((1,3,6,1,4,1,12325,1,210,6,3))
_WlanMeshRouteTable_Object=MibTable
wlanMeshRouteTable=_WlanMeshRouteTable_Object((1,3,6,1,4,1,12325,1,210,6,3,1))
if mibBuilder.loadTexts:wlanMeshRouteTable.setStatus(_A)
_WlanMeshRouteEntry_Object=MibTableRow
wlanMeshRouteEntry=_WlanMeshRouteEntry_Object((1,3,6,1,4,1,12325,1,210,6,3,1,1))
wlanMeshRouteEntry.setIndexNames((0,_F,_G),(0,_F,_r))
if mibBuilder.loadTexts:wlanMeshRouteEntry.setStatus(_A)
_WlanMeshRouteDestination_Type=MacAddress
_WlanMeshRouteDestination_Object=MibTableColumn
wlanMeshRouteDestination=_WlanMeshRouteDestination_Object((1,3,6,1,4,1,12325,1,210,6,3,1,1,1),_WlanMeshRouteDestination_Type())
wlanMeshRouteDestination.setMaxAccess(_K)
if mibBuilder.loadTexts:wlanMeshRouteDestination.setStatus(_A)
_WlanMeshRouteNextHop_Type=MacAddress
_WlanMeshRouteNextHop_Object=MibTableColumn
wlanMeshRouteNextHop=_WlanMeshRouteNextHop_Object((1,3,6,1,4,1,12325,1,210,6,3,1,1,2),_WlanMeshRouteNextHop_Type())
wlanMeshRouteNextHop.setMaxAccess(_B)
if mibBuilder.loadTexts:wlanMeshRouteNextHop.setStatus(_A)
_WlanMeshRouteHops_Type=Integer32
_WlanMeshRouteHops_Object=MibTableColumn
wlanMeshRouteHops=_WlanMeshRouteHops_Object((1,3,6,1,4,1,12325,1,210,6,3,1,1,3),_WlanMeshRouteHops_Type())
wlanMeshRouteHops.setMaxAccess(_B)
if mibBuilder.loadTexts:wlanMeshRouteHops.setStatus(_A)
_WlanMeshRouteMetric_Type=Unsigned32
_WlanMeshRouteMetric_Object=MibTableColumn
wlanMeshRouteMetric=_WlanMeshRouteMetric_Object((1,3,6,1,4,1,12325,1,210,6,3,1,1,4),_WlanMeshRouteMetric_Type())
wlanMeshRouteMetric.setMaxAccess(_B)
if mibBuilder.loadTexts:wlanMeshRouteMetric.setStatus(_A)
_WlanMeshRouteLifeTime_Type=Unsigned32
_WlanMeshRouteLifeTime_Object=MibTableColumn
wlanMeshRouteLifeTime=_WlanMeshRouteLifeTime_Object((1,3,6,1,4,1,12325,1,210,6,3,1,1,5),_WlanMeshRouteLifeTime_Type())
wlanMeshRouteLifeTime.setMaxAccess(_B)
if mibBuilder.loadTexts:wlanMeshRouteLifeTime.setStatus(_A)
if mibBuilder.loadTexts:wlanMeshRouteLifeTime.setUnits(_M)
_WlanMeshRouteLastMseq_Type=Unsigned32
_WlanMeshRouteLastMseq_Object=MibTableColumn
wlanMeshRouteLastMseq=_WlanMeshRouteLastMseq_Object((1,3,6,1,4,1,12325,1,210,6,3,1,1,6),_WlanMeshRouteLastMseq_Type())
wlanMeshRouteLastMseq.setMaxAccess(_B)
if mibBuilder.loadTexts:wlanMeshRouteLastMseq.setStatus(_A)
class _WlanMeshRouteFlags_Type(Bits):namedValues=NamedValues(*(('valid',1),('proxy',2)))
_WlanMeshRouteFlags_Type.__name__=_J
_WlanMeshRouteFlags_Object=MibTableColumn
wlanMeshRouteFlags=_WlanMeshRouteFlags_Object((1,3,6,1,4,1,12325,1,210,6,3,1,1,7),_WlanMeshRouteFlags_Type())
wlanMeshRouteFlags.setMaxAccess(_B)
if mibBuilder.loadTexts:wlanMeshRouteFlags.setStatus(_A)
_WlanMeshRouteStatus_Type=RowStatus
_WlanMeshRouteStatus_Object=MibTableColumn
wlanMeshRouteStatus=_WlanMeshRouteStatus_Object((1,3,6,1,4,1,12325,1,210,6,3,1,1,8),_WlanMeshRouteStatus_Type())
wlanMeshRouteStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:wlanMeshRouteStatus.setStatus(_A)
_WlanMeshStatistics_ObjectIdentity=ObjectIdentity
wlanMeshStatistics=_WlanMeshStatistics_ObjectIdentity((1,3,6,1,4,1,12325,1,210,6,4))
_WlanMeshStatsTable_Object=MibTable
wlanMeshStatsTable=_WlanMeshStatsTable_Object((1,3,6,1,4,1,12325,1,210,6,4,1))
if mibBuilder.loadTexts:wlanMeshStatsTable.setStatus(_A)
_WlanMeshStatsEntry_Object=MibTableRow
wlanMeshStatsEntry=_WlanMeshStatsEntry_Object((1,3,6,1,4,1,12325,1,210,6,4,1,1))
wlanMeshStatsEntry.setIndexNames((0,_F,_G))
if mibBuilder.loadTexts:wlanMeshStatsEntry.setStatus(_A)
_WlanMeshDroppedBadSta_Type=Counter32
_WlanMeshDroppedBadSta_Object=MibTableColumn
wlanMeshDroppedBadSta=_WlanMeshDroppedBadSta_Object((1,3,6,1,4,1,12325,1,210,6,4,1,1,1),_WlanMeshDroppedBadSta_Type())
wlanMeshDroppedBadSta.setMaxAccess(_B)
if mibBuilder.loadTexts:wlanMeshDroppedBadSta.setStatus(_A)
if mibBuilder.loadTexts:wlanMeshDroppedBadSta.setUnits(_C)
_WlanMeshDroppedNoLink_Type=Counter32
_WlanMeshDroppedNoLink_Object=MibTableColumn
wlanMeshDroppedNoLink=_WlanMeshDroppedNoLink_Object((1,3,6,1,4,1,12325,1,210,6,4,1,1,2),_WlanMeshDroppedNoLink_Type())
wlanMeshDroppedNoLink.setMaxAccess(_B)
if mibBuilder.loadTexts:wlanMeshDroppedNoLink.setStatus(_A)
if mibBuilder.loadTexts:wlanMeshDroppedNoLink.setUnits(_C)
_WlanMeshNoFwdTtl_Type=Counter32
_WlanMeshNoFwdTtl_Object=MibTableColumn
wlanMeshNoFwdTtl=_WlanMeshNoFwdTtl_Object((1,3,6,1,4,1,12325,1,210,6,4,1,1,3),_WlanMeshNoFwdTtl_Type())
wlanMeshNoFwdTtl.setMaxAccess(_B)
if mibBuilder.loadTexts:wlanMeshNoFwdTtl.setStatus(_A)
if mibBuilder.loadTexts:wlanMeshNoFwdTtl.setUnits(_C)
_WlanMeshNoFwdBuf_Type=Counter32
_WlanMeshNoFwdBuf_Object=MibTableColumn
wlanMeshNoFwdBuf=_WlanMeshNoFwdBuf_Object((1,3,6,1,4,1,12325,1,210,6,4,1,1,4),_WlanMeshNoFwdBuf_Type())
wlanMeshNoFwdBuf.setMaxAccess(_B)
if mibBuilder.loadTexts:wlanMeshNoFwdBuf.setStatus(_A)
if mibBuilder.loadTexts:wlanMeshNoFwdBuf.setUnits(_C)
_WlanMeshNoFwdTooShort_Type=Counter32
_WlanMeshNoFwdTooShort_Object=MibTableColumn
wlanMeshNoFwdTooShort=_WlanMeshNoFwdTooShort_Object((1,3,6,1,4,1,12325,1,210,6,4,1,1,5),_WlanMeshNoFwdTooShort_Type())
wlanMeshNoFwdTooShort.setMaxAccess(_B)
if mibBuilder.loadTexts:wlanMeshNoFwdTooShort.setStatus(_A)
if mibBuilder.loadTexts:wlanMeshNoFwdTooShort.setUnits(_C)
_WlanMeshNoFwdDisabled_Type=Counter32
_WlanMeshNoFwdDisabled_Object=MibTableColumn
wlanMeshNoFwdDisabled=_WlanMeshNoFwdDisabled_Object((1,3,6,1,4,1,12325,1,210,6,4,1,1,6),_WlanMeshNoFwdDisabled_Type())
wlanMeshNoFwdDisabled.setMaxAccess(_B)
if mibBuilder.loadTexts:wlanMeshNoFwdDisabled.setStatus(_A)
if mibBuilder.loadTexts:wlanMeshNoFwdDisabled.setUnits(_C)
_WlanMeshNoFwdPathUnknown_Type=Counter32
_WlanMeshNoFwdPathUnknown_Object=MibTableColumn
wlanMeshNoFwdPathUnknown=_WlanMeshNoFwdPathUnknown_Object((1,3,6,1,4,1,12325,1,210,6,4,1,1,7),_WlanMeshNoFwdPathUnknown_Type())
wlanMeshNoFwdPathUnknown.setMaxAccess(_B)
if mibBuilder.loadTexts:wlanMeshNoFwdPathUnknown.setStatus(_A)
if mibBuilder.loadTexts:wlanMeshNoFwdPathUnknown.setUnits(_C)
_WlanMeshDroppedBadAE_Type=Counter32
_WlanMeshDroppedBadAE_Object=MibTableColumn
wlanMeshDroppedBadAE=_WlanMeshDroppedBadAE_Object((1,3,6,1,4,1,12325,1,210,6,4,1,1,8),_WlanMeshDroppedBadAE_Type())
wlanMeshDroppedBadAE.setMaxAccess(_B)
if mibBuilder.loadTexts:wlanMeshDroppedBadAE.setStatus(_A)
if mibBuilder.loadTexts:wlanMeshDroppedBadAE.setUnits(_C)
_WlanMeshRouteAddFailed_Type=Counter32
_WlanMeshRouteAddFailed_Object=MibTableColumn
wlanMeshRouteAddFailed=_WlanMeshRouteAddFailed_Object((1,3,6,1,4,1,12325,1,210,6,4,1,1,9),_WlanMeshRouteAddFailed_Type())
wlanMeshRouteAddFailed.setMaxAccess(_B)
if mibBuilder.loadTexts:wlanMeshRouteAddFailed.setStatus(_A)
_WlanMeshDroppedNoProxy_Type=Counter32
_WlanMeshDroppedNoProxy_Object=MibTableColumn
wlanMeshDroppedNoProxy=_WlanMeshDroppedNoProxy_Object((1,3,6,1,4,1,12325,1,210,6,4,1,1,10),_WlanMeshDroppedNoProxy_Type())
wlanMeshDroppedNoProxy.setMaxAccess(_B)
if mibBuilder.loadTexts:wlanMeshDroppedNoProxy.setStatus(_A)
if mibBuilder.loadTexts:wlanMeshDroppedNoProxy.setUnits(_C)
_WlanMeshDroppedMisaligned_Type=Counter32
_WlanMeshDroppedMisaligned_Object=MibTableColumn
wlanMeshDroppedMisaligned=_WlanMeshDroppedMisaligned_Object((1,3,6,1,4,1,12325,1,210,6,4,1,1,11),_WlanMeshDroppedMisaligned_Type())
wlanMeshDroppedMisaligned.setMaxAccess(_B)
if mibBuilder.loadTexts:wlanMeshDroppedMisaligned.setStatus(_A)
if mibBuilder.loadTexts:wlanMeshDroppedMisaligned.setUnits(_C)
_WlanMeshRouteProtocols_ObjectIdentity=ObjectIdentity
wlanMeshRouteProtocols=_WlanMeshRouteProtocols_ObjectIdentity((1,3,6,1,4,1,12325,1,210,6,5))
_WlanMeshProtoHWMP_ObjectIdentity=ObjectIdentity
wlanMeshProtoHWMP=_WlanMeshProtoHWMP_ObjectIdentity((1,3,6,1,4,1,12325,1,210,6,5,1))
_WlanMeshHWMPConfig_ObjectIdentity=ObjectIdentity
wlanMeshHWMPConfig=_WlanMeshHWMPConfig_ObjectIdentity((1,3,6,1,4,1,12325,1,210,6,5,1,1))
class _WlanHWMPRouteInactiveTimeout_Type(Integer32):defaultValue=5000
_WlanHWMPRouteInactiveTimeout_Type.__name__=_E
_WlanHWMPRouteInactiveTimeout_Object=MibScalar
wlanHWMPRouteInactiveTimeout=_WlanHWMPRouteInactiveTimeout_Object((1,3,6,1,4,1,12325,1,210,6,5,1,1,1),_WlanHWMPRouteInactiveTimeout_Type())
wlanHWMPRouteInactiveTimeout.setMaxAccess(_D)
if mibBuilder.loadTexts:wlanHWMPRouteInactiveTimeout.setStatus(_A)
if mibBuilder.loadTexts:wlanHWMPRouteInactiveTimeout.setUnits(_H)
class _WlanHWMPRootAnnounceInterval_Type(Integer32):defaultValue=1000
_WlanHWMPRootAnnounceInterval_Type.__name__=_E
_WlanHWMPRootAnnounceInterval_Object=MibScalar
wlanHWMPRootAnnounceInterval=_WlanHWMPRootAnnounceInterval_Object((1,3,6,1,4,1,12325,1,210,6,5,1,1,2),_WlanHWMPRootAnnounceInterval_Type())
wlanHWMPRootAnnounceInterval.setMaxAccess(_D)
if mibBuilder.loadTexts:wlanHWMPRootAnnounceInterval.setStatus(_A)
if mibBuilder.loadTexts:wlanHWMPRootAnnounceInterval.setUnits(_H)
class _WlanHWMPRootInterval_Type(Integer32):defaultValue=2000
_WlanHWMPRootInterval_Type.__name__=_E
_WlanHWMPRootInterval_Object=MibScalar
wlanHWMPRootInterval=_WlanHWMPRootInterval_Object((1,3,6,1,4,1,12325,1,210,6,5,1,1,3),_WlanHWMPRootInterval_Type())
wlanHWMPRootInterval.setMaxAccess(_D)
if mibBuilder.loadTexts:wlanHWMPRootInterval.setStatus(_A)
if mibBuilder.loadTexts:wlanHWMPRootInterval.setUnits(_H)
class _WlanHWMPRootTimeout_Type(Integer32):defaultValue=5000
_WlanHWMPRootTimeout_Type.__name__=_E
_WlanHWMPRootTimeout_Object=MibScalar
wlanHWMPRootTimeout=_WlanHWMPRootTimeout_Object((1,3,6,1,4,1,12325,1,210,6,5,1,1,4),_WlanHWMPRootTimeout_Type())
wlanHWMPRootTimeout.setMaxAccess(_D)
if mibBuilder.loadTexts:wlanHWMPRootTimeout.setStatus(_A)
if mibBuilder.loadTexts:wlanHWMPRootTimeout.setUnits(_H)
class _WlanHWMPPathLifetime_Type(Integer32):defaultValue=500
_WlanHWMPPathLifetime_Type.__name__=_E
_WlanHWMPPathLifetime_Object=MibScalar
wlanHWMPPathLifetime=_WlanHWMPPathLifetime_Object((1,3,6,1,4,1,12325,1,210,6,5,1,1,5),_WlanHWMPPathLifetime_Type())
wlanHWMPPathLifetime.setMaxAccess(_D)
if mibBuilder.loadTexts:wlanHWMPPathLifetime.setStatus(_A)
if mibBuilder.loadTexts:wlanHWMPPathLifetime.setUnits(_H)
class _WlanHWMPReplyForwardBit_Type(Integer32):defaultValue=1
_WlanHWMPReplyForwardBit_Type.__name__=_E
_WlanHWMPReplyForwardBit_Object=MibScalar
wlanHWMPReplyForwardBit=_WlanHWMPReplyForwardBit_Object((1,3,6,1,4,1,12325,1,210,6,5,1,1,6),_WlanHWMPReplyForwardBit_Type())
wlanHWMPReplyForwardBit.setMaxAccess(_D)
if mibBuilder.loadTexts:wlanHWMPReplyForwardBit.setStatus(_A)
class _WlanHWMPTargetOnlyBit_Type(Integer32):defaultValue=0
_WlanHWMPTargetOnlyBit_Type.__name__=_E
_WlanHWMPTargetOnlyBit_Object=MibScalar
wlanHWMPTargetOnlyBit=_WlanHWMPTargetOnlyBit_Object((1,3,6,1,4,1,12325,1,210,6,5,1,1,7),_WlanHWMPTargetOnlyBit_Type())
wlanHWMPTargetOnlyBit.setMaxAccess(_D)
if mibBuilder.loadTexts:wlanHWMPTargetOnlyBit.setStatus(_A)
_WlanMeshHWMPInterface_ObjectIdentity=ObjectIdentity
wlanMeshHWMPInterface=_WlanMeshHWMPInterface_ObjectIdentity((1,3,6,1,4,1,12325,1,210,6,5,1,2))
_WlanHWMPInterfaceTable_Object=MibTable
wlanHWMPInterfaceTable=_WlanHWMPInterfaceTable_Object((1,3,6,1,4,1,12325,1,210,6,5,1,2,1))
if mibBuilder.loadTexts:wlanHWMPInterfaceTable.setStatus(_A)
_WlanHWMPInterfaceEntry_Object=MibTableRow
wlanHWMPInterfaceEntry=_WlanHWMPInterfaceEntry_Object((1,3,6,1,4,1,12325,1,210,6,5,1,2,1,1))
wlanHWMPInterfaceEntry.setIndexNames((0,_F,_G))
if mibBuilder.loadTexts:wlanHWMPInterfaceEntry.setStatus(_A)
class _WlanHWMPRootMode_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_O,1),('normal',2),('proactive',3),('rann',4)))
_WlanHWMPRootMode_Type.__name__=_E
_WlanHWMPRootMode_Object=MibTableColumn
wlanHWMPRootMode=_WlanHWMPRootMode_Object((1,3,6,1,4,1,12325,1,210,6,5,1,2,1,1,1),_WlanHWMPRootMode_Type())
wlanHWMPRootMode.setMaxAccess(_D)
if mibBuilder.loadTexts:wlanHWMPRootMode.setStatus(_A)
class _WlanHWMPMaxHops_Type(Integer32):defaultValue=31
_WlanHWMPMaxHops_Type.__name__=_E
_WlanHWMPMaxHops_Object=MibTableColumn
wlanHWMPMaxHops=_WlanHWMPMaxHops_Object((1,3,6,1,4,1,12325,1,210,6,5,1,2,1,1,2),_WlanHWMPMaxHops_Type())
wlanHWMPMaxHops.setMaxAccess(_D)
if mibBuilder.loadTexts:wlanHWMPMaxHops.setStatus(_A)
_WlanMeshHWMPStatistics_ObjectIdentity=ObjectIdentity
wlanMeshHWMPStatistics=_WlanMeshHWMPStatistics_ObjectIdentity((1,3,6,1,4,1,12325,1,210,6,5,1,3))
_WlanMeshHWMPStatsTable_Object=MibTable
wlanMeshHWMPStatsTable=_WlanMeshHWMPStatsTable_Object((1,3,6,1,4,1,12325,1,210,6,5,1,3,1))
if mibBuilder.loadTexts:wlanMeshHWMPStatsTable.setStatus(_A)
_WlanMeshHWMPStatsEntry_Object=MibTableRow
wlanMeshHWMPStatsEntry=_WlanMeshHWMPStatsEntry_Object((1,3,6,1,4,1,12325,1,210,6,5,1,3,1,1))
wlanMeshHWMPStatsEntry.setIndexNames((0,_F,_G))
if mibBuilder.loadTexts:wlanMeshHWMPStatsEntry.setStatus(_A)
_WlanMeshHWMPWrongSeqNo_Type=Counter32
_WlanMeshHWMPWrongSeqNo_Object=MibTableColumn
wlanMeshHWMPWrongSeqNo=_WlanMeshHWMPWrongSeqNo_Object((1,3,6,1,4,1,12325,1,210,6,5,1,3,1,1,1),_WlanMeshHWMPWrongSeqNo_Type())
wlanMeshHWMPWrongSeqNo.setMaxAccess(_B)
if mibBuilder.loadTexts:wlanMeshHWMPWrongSeqNo.setStatus(_A)
if mibBuilder.loadTexts:wlanMeshHWMPWrongSeqNo.setUnits(_C)
_WlanMeshHWMPTxRootPREQ_Type=Counter32
_WlanMeshHWMPTxRootPREQ_Object=MibTableColumn
wlanMeshHWMPTxRootPREQ=_WlanMeshHWMPTxRootPREQ_Object((1,3,6,1,4,1,12325,1,210,6,5,1,3,1,1,2),_WlanMeshHWMPTxRootPREQ_Type())
wlanMeshHWMPTxRootPREQ.setMaxAccess(_B)
if mibBuilder.loadTexts:wlanMeshHWMPTxRootPREQ.setStatus(_A)
if mibBuilder.loadTexts:wlanMeshHWMPTxRootPREQ.setUnits(_C)
_WlanMeshHWMPTxRootRANN_Type=Counter32
_WlanMeshHWMPTxRootRANN_Object=MibTableColumn
wlanMeshHWMPTxRootRANN=_WlanMeshHWMPTxRootRANN_Object((1,3,6,1,4,1,12325,1,210,6,5,1,3,1,1,3),_WlanMeshHWMPTxRootRANN_Type())
wlanMeshHWMPTxRootRANN.setMaxAccess(_B)
if mibBuilder.loadTexts:wlanMeshHWMPTxRootRANN.setStatus(_A)
if mibBuilder.loadTexts:wlanMeshHWMPTxRootRANN.setUnits(_C)
_WlanMeshHWMPProxy_Type=Counter32
_WlanMeshHWMPProxy_Object=MibTableColumn
wlanMeshHWMPProxy=_WlanMeshHWMPProxy_Object((1,3,6,1,4,1,12325,1,210,6,5,1,3,1,1,4),_WlanMeshHWMPProxy_Type())
wlanMeshHWMPProxy.setMaxAccess(_B)
if mibBuilder.loadTexts:wlanMeshHWMPProxy.setStatus(_A)
if mibBuilder.loadTexts:wlanMeshHWMPProxy.setUnits(_C)
wlanInterfaceEntry.registerAugmentions((_F,_s))
wlanIfParentEntry.setIndexNames(*wlanInterfaceEntry.getIndexNames())
wlanInterfaceEntry.registerAugmentions((_F,_t))
wlanIfaceConfigEntry.setIndexNames(*wlanInterfaceEntry.getIndexNames())
wlanInterfaceEntry.registerAugmentions((_F,_u))
wlanIfaceStatisticsEntry.setIndexNames(*wlanInterfaceEntry.getIndexNames())
mibBuilder.exportSymbols(_F,**{'WlanMgmtReasonCode':WlanMgmtReasonCode,'WlanMgmtMeshReasonCode':WlanMgmtMeshReasonCode,'WlanMgmtStatusCode':WlanMgmtStatusCode,'WlanRegDomainCode':WlanRegDomainCode,_R:WlanIfaceDot11nPduType,'WlanPeerCapabilityFlags':WlanPeerCapabilityFlags,'WlanIfPhyMode':WlanIfPhyMode,'begemotWlan':begemotWlan,'begemotWlanNotifications':begemotWlanNotifications,'begemotWlanInterface':begemotWlanInterface,'wlanInterfaceTable':wlanInterfaceTable,'wlanInterfaceEntry':wlanInterfaceEntry,'wlanIfaceIndex':wlanIfaceIndex,_G:wlanIfaceName,'wlanParentIfName':wlanParentIfName,'wlanIfaceOperatingMode':wlanIfaceOperatingMode,'wlanIfaceFlags':wlanIfaceFlags,'wlanIfaceBssid':wlanIfaceBssid,'wlanIfaceLocalAddress':wlanIfaceLocalAddress,'wlanIfaceStatus':wlanIfaceStatus,'wlanIfaceState':wlanIfaceState,'wlanIfParentTable':wlanIfParentTable,_s:wlanIfParentEntry,'wlanIfParentDriverCapabilities':wlanIfParentDriverCapabilities,'wlanIfParentCryptoCapabilities':wlanIfParentCryptoCapabilities,'wlanIfParentHTCapabilities':wlanIfParentHTCapabilities,'wlanIfaceConfigTable':wlanIfaceConfigTable,_t:wlanIfaceConfigEntry,'wlanIfacePacketBurst':wlanIfacePacketBurst,'wlanIfaceCountryCode':wlanIfaceCountryCode,'wlanIfaceRegDomain':wlanIfaceRegDomain,'wlanIfaceDesiredSsid':wlanIfaceDesiredSsid,'wlanIfaceDesiredChannel':wlanIfaceDesiredChannel,'wlanIfaceDynamicFreqSelection':wlanIfaceDynamicFreqSelection,'wlanIfaceFastFrames':wlanIfaceFastFrames,'wlanIfaceDturbo':wlanIfaceDturbo,'wlanIfaceTxPower':wlanIfaceTxPower,'wlanIfaceFragmentThreshold':wlanIfaceFragmentThreshold,'wlanIfaceRTSThreshold':wlanIfaceRTSThreshold,'wlanIfaceWlanPrivacySubscribe':wlanIfaceWlanPrivacySubscribe,'wlanIfaceBgScan':wlanIfaceBgScan,'wlanIfaceBgScanIdle':wlanIfaceBgScanIdle,'wlanIfaceBgScanInterval':wlanIfaceBgScanInterval,'wlanIfaceBeaconMissedThreshold':wlanIfaceBeaconMissedThreshold,'wlanIfaceDesiredBssid':wlanIfaceDesiredBssid,'wlanIfaceRoamingMode':wlanIfaceRoamingMode,'wlanIfaceDot11d':wlanIfaceDot11d,'wlanIfaceDot11h':wlanIfaceDot11h,'wlanIfaceDynamicWds':wlanIfaceDynamicWds,'wlanIfacePowerSave':wlanIfacePowerSave,'wlanIfaceApBridge':wlanIfaceApBridge,'wlanIfaceBeaconInterval':wlanIfaceBeaconInterval,'wlanIfaceDtimPeriod':wlanIfaceDtimPeriod,'wlanIfaceHideSsid':wlanIfaceHideSsid,'wlanIfaceInactivityProccess':wlanIfaceInactivityProccess,'wlanIfaceDot11gProtMode':wlanIfaceDot11gProtMode,'wlanIfaceDot11gPureMode':wlanIfaceDot11gPureMode,'wlanIfaceDot11nPureMode':wlanIfaceDot11nPureMode,'wlanIfaceDot11nAmpdu':wlanIfaceDot11nAmpdu,'wlanIfaceDot11nAmpduDensity':wlanIfaceDot11nAmpduDensity,'wlanIfaceDot11nAmpduLimit':wlanIfaceDot11nAmpduLimit,'wlanIfaceDot11nAmsdu':wlanIfaceDot11nAmsdu,'wlanIfaceDot11nAmsduLimit':wlanIfaceDot11nAmsduLimit,'wlanIfaceDot11nHighThroughput':wlanIfaceDot11nHighThroughput,'wlanIfaceDot11nHTCompatible':wlanIfaceDot11nHTCompatible,'wlanIfaceDot11nHTProtMode':wlanIfaceDot11nHTProtMode,'wlanIfaceDot11nRIFS':wlanIfaceDot11nRIFS,'wlanIfaceDot11nShortGI':wlanIfaceDot11nShortGI,'wlanIfaceDot11nSMPSMode':wlanIfaceDot11nSMPSMode,'wlanIfaceTdmaSlot':wlanIfaceTdmaSlot,'wlanIfaceTdmaSlotCount':wlanIfaceTdmaSlotCount,'wlanIfaceTdmaSlotLength':wlanIfaceTdmaSlotLength,'wlanIfaceTdmaBeaconInterval':wlanIfaceTdmaBeaconInterval,'wlanIfacePeerTable':wlanIfacePeerTable,'wlanIfacePeerEntry':wlanIfacePeerEntry,_i:wlanIfacePeerAddress,'wlanIfacePeerAssociationId':wlanIfacePeerAssociationId,'wlanIfacePeerVlanTag':wlanIfacePeerVlanTag,'wlanIfacePeerFrequency':wlanIfacePeerFrequency,'wlanIfacePeerCurrentTXRate':wlanIfacePeerCurrentTXRate,'wlanIfacePeerRxSignalStrength':wlanIfacePeerRxSignalStrength,'wlanIfacePeerIdleTimer':wlanIfacePeerIdleTimer,'wlanIfacePeerTxSequenceNo':wlanIfacePeerTxSequenceNo,'wlanIfacePeerRxSequenceNo':wlanIfacePeerRxSequenceNo,'wlanIfacePeerTxPower':wlanIfacePeerTxPower,'wlanIfacePeerCapabilities':wlanIfacePeerCapabilities,'wlanIfacePeerFlags':wlanIfacePeerFlags,'wlanIfaceChannelTable':wlanIfaceChannelTable,'wlanIfaceChannelEntry':wlanIfaceChannelEntry,_j:wlanIfaceChannelId,'wlanIfaceChannelIeeeId':wlanIfaceChannelIeeeId,'wlanIfaceChannelType':wlanIfaceChannelType,'wlanIfaceChannelFlags':wlanIfaceChannelFlags,'wlanIfaceChannelFrequency':wlanIfaceChannelFrequency,'wlanIfaceChannelMaxRegPower':wlanIfaceChannelMaxRegPower,'wlanIfaceChannelMaxTxPower':wlanIfaceChannelMaxTxPower,'wlanIfaceChannelMinTxPower':wlanIfaceChannelMinTxPower,'wlanIfaceChannelState':wlanIfaceChannelState,'wlanIfaceChannelHTExtension':wlanIfaceChannelHTExtension,'wlanIfaceChannelMaxAntennaGain':wlanIfaceChannelMaxAntennaGain,'wlanIfRoamParamsTable':wlanIfRoamParamsTable,'wlanIfRoamParamsEntry':wlanIfRoamParamsEntry,_k:wlanIfRoamPhyMode,'wlanIfRoamRxSignalStrength':wlanIfRoamRxSignalStrength,'wlanIfRoamTxRateThreshold':wlanIfRoamTxRateThreshold,'wlanIfTxParamsTable':wlanIfTxParamsTable,'wlanIfTxParamsEntry':wlanIfTxParamsEntry,_l:wlanIfTxPhyMode,'wlanIfTxUnicastRate':wlanIfTxUnicastRate,'wlanIfTxMcastRate':wlanIfTxMcastRate,'wlanIfTxMgmtRate':wlanIfTxMgmtRate,'wlanIfTxMaxRetryCount':wlanIfTxMaxRetryCount,'begemotWlanScanning':begemotWlanScanning,'wlanScanConfigTable':wlanScanConfigTable,'wlanScanConfigEntry':wlanScanConfigEntry,'wlanScanFlags':wlanScanFlags,'wlanScanDuration':wlanScanDuration,'wlanScanMinChannelDwellTime':wlanScanMinChannelDwellTime,'wlanScanMaxChannelDwellTime':wlanScanMaxChannelDwellTime,'wlanScanConfigStatus':wlanScanConfigStatus,'wlanScanResultsTable':wlanScanResultsTable,'wlanScanResultsEntry':wlanScanResultsEntry,_m:wlanScanResultID,_n:wlanScanResultBssid,'wlanScanResultChannel':wlanScanResultChannel,'wlanScanResultRate':wlanScanResultRate,'wlanScanResultNoise':wlanScanResultNoise,'wlanScanResultBeaconInterval':wlanScanResultBeaconInterval,'wlanScanResultCapabilities':wlanScanResultCapabilities,'begemotWlanStatistics':begemotWlanStatistics,'wlanIfaceStatisticsTable':wlanIfaceStatisticsTable,_u:wlanIfaceStatisticsEntry,'wlanStatsRxBadVersion':wlanStatsRxBadVersion,'wlanStatsRxTooShort':wlanStatsRxTooShort,'wlanStatsRxWrongBssid':wlanStatsRxWrongBssid,'wlanStatsRxDiscardedDups':wlanStatsRxDiscardedDups,'wlanStatsRxWrongDir':wlanStatsRxWrongDir,'wlanStatsRxDiscardMcastEcho':wlanStatsRxDiscardMcastEcho,'wlanStatsRxDiscardNoAssoc':wlanStatsRxDiscardNoAssoc,'wlanStatsRxWepNoPrivacy':wlanStatsRxWepNoPrivacy,'wlanStatsRxWepUnencrypted':wlanStatsRxWepUnencrypted,'wlanStatsRxWepFailed':wlanStatsRxWepFailed,'wlanStatsRxDecapsulationFailed':wlanStatsRxDecapsulationFailed,'wlanStatsRxDiscardMgmt':wlanStatsRxDiscardMgmt,'wlanStatsRxControl':wlanStatsRxControl,'wlanStatsRxBeacon':wlanStatsRxBeacon,'wlanStatsRxRateSetTooBig':wlanStatsRxRateSetTooBig,'wlanStatsRxElemMissing':wlanStatsRxElemMissing,'wlanStatsRxElemTooBig':wlanStatsRxElemTooBig,'wlanStatsRxElemTooSmall':wlanStatsRxElemTooSmall,'wlanStatsRxElemUnknown':wlanStatsRxElemUnknown,'wlanStatsRxChannelMismatch':wlanStatsRxChannelMismatch,'wlanStatsRxDropped':wlanStatsRxDropped,'wlanStatsRxSsidMismatch':wlanStatsRxSsidMismatch,'wlanStatsRxAuthNotSupported':wlanStatsRxAuthNotSupported,'wlanStatsRxAuthFailed':wlanStatsRxAuthFailed,'wlanStatsRxAuthCM':wlanStatsRxAuthCM,'wlanStatsRxAssocWrongBssid':wlanStatsRxAssocWrongBssid,'wlanStatsRxAssocNoAuth':wlanStatsRxAssocNoAuth,'wlanStatsRxAssocCapMismatch':wlanStatsRxAssocCapMismatch,'wlanStatsRxAssocNoRateMatch':wlanStatsRxAssocNoRateMatch,'wlanStatsRxBadWpaIE':wlanStatsRxBadWpaIE,'wlanStatsRxDeauthenticate':wlanStatsRxDeauthenticate,'wlanStatsRxDisassociate':wlanStatsRxDisassociate,'wlanStatsRxUnknownSubtype':wlanStatsRxUnknownSubtype,'wlanStatsRxFailedNoBuf':wlanStatsRxFailedNoBuf,'wlanStatsRxBadAuthRequest':wlanStatsRxBadAuthRequest,'wlanStatsRxUnAuthorized':wlanStatsRxUnAuthorized,'wlanStatsRxBadKeyId':wlanStatsRxBadKeyId,'wlanStatsRxCCMPSeqViolation':wlanStatsRxCCMPSeqViolation,'wlanStatsRxCCMPBadFormat':wlanStatsRxCCMPBadFormat,'wlanStatsRxCCMPFailedMIC':wlanStatsRxCCMPFailedMIC,'wlanStatsRxTKIPSeqViolation':wlanStatsRxTKIPSeqViolation,'wlanStatsRxTKIPBadFormat':wlanStatsRxTKIPBadFormat,'wlanStatsRxTKIPFailedMIC':wlanStatsRxTKIPFailedMIC,'wlanStatsRxTKIPFailedICV':wlanStatsRxTKIPFailedICV,'wlanStatsRxDiscardACL':wlanStatsRxDiscardACL,'wlanStatsTxFailedNoBuf':wlanStatsTxFailedNoBuf,'wlanStatsTxFailedNoNode':wlanStatsTxFailedNoNode,'wlanStatsTxUnknownMgmt':wlanStatsTxUnknownMgmt,'wlanStatsTxBadCipher':wlanStatsTxBadCipher,'wlanStatsTxNoDefKey':wlanStatsTxNoDefKey,'wlanStatsTxFragmented':wlanStatsTxFragmented,'wlanStatsTxFragmentsCreated':wlanStatsTxFragmentsCreated,'wlanStatsActiveScans':wlanStatsActiveScans,'wlanStatsPassiveScans':wlanStatsPassiveScans,'wlanStatsTimeoutInactivity':wlanStatsTimeoutInactivity,'wlanStatsCryptoNoMem':wlanStatsCryptoNoMem,'wlanStatsSwCryptoTKIP':wlanStatsSwCryptoTKIP,'wlanStatsSwCryptoTKIPEnMIC':wlanStatsSwCryptoTKIPEnMIC,'wlanStatsSwCryptoTKIPDeMIC':wlanStatsSwCryptoTKIPDeMIC,'wlanStatsCryptoTKIPCM':wlanStatsCryptoTKIPCM,'wlanStatsSwCryptoCCMP':wlanStatsSwCryptoCCMP,'wlanStatsSwCryptoWEP':wlanStatsSwCryptoWEP,'wlanStatsCryptoCipherKeyRejected':wlanStatsCryptoCipherKeyRejected,'wlanStatsCryptoNoKey':wlanStatsCryptoNoKey,'wlanStatsCryptoDeleteKeyFailed':wlanStatsCryptoDeleteKeyFailed,'wlanStatsCryptoUnknownCipher':wlanStatsCryptoUnknownCipher,'wlanStatsCryptoAttachFailed':wlanStatsCryptoAttachFailed,'wlanStatsCryptoKeyFailed':wlanStatsCryptoKeyFailed,'wlanStatsCryptoEnMICFailed':wlanStatsCryptoEnMICFailed,'wlanStatsIBSSCapMismatch':wlanStatsIBSSCapMismatch,'wlanStatsUnassocStaPSPoll':wlanStatsUnassocStaPSPoll,'wlanStatsBadAidPSPoll':wlanStatsBadAidPSPoll,'wlanStatsEmptyPSPoll':wlanStatsEmptyPSPoll,'wlanStatsRxFFBadHdr':wlanStatsRxFFBadHdr,'wlanStatsRxFFTooShort':wlanStatsRxFFTooShort,'wlanStatsRxFFSplitError':wlanStatsRxFFSplitError,'wlanStatsRxFFDecap':wlanStatsRxFFDecap,'wlanStatsTxFFEncap':wlanStatsTxFFEncap,'wlanStatsRxBadBintval':wlanStatsRxBadBintval,'wlanStatsRxDemicFailed':wlanStatsRxDemicFailed,'wlanStatsRxDefragFailed':wlanStatsRxDefragFailed,'wlanStatsRxMgmt':wlanStatsRxMgmt,'wlanStatsRxActionMgmt':wlanStatsRxActionMgmt,'wlanStatsRxAMSDUTooShort':wlanStatsRxAMSDUTooShort,'wlanStatsRxAMSDUSplitError':wlanStatsRxAMSDUSplitError,'wlanStatsRxAMSDUDecap':wlanStatsRxAMSDUDecap,'wlanStatsTxAMSDUEncap':wlanStatsTxAMSDUEncap,'wlanStatsAMPDUBadBAR':wlanStatsAMPDUBadBAR,'wlanStatsAMPDUOowBar':wlanStatsAMPDUOowBar,'wlanStatsAMPDUMovedBAR':wlanStatsAMPDUMovedBAR,'wlanStatsAMPDURxBAR':wlanStatsAMPDURxBAR,'wlanStatsAMPDURxOor':wlanStatsAMPDURxOor,'wlanStatsAMPDURxCopied':wlanStatsAMPDURxCopied,'wlanStatsAMPDURxDropped':wlanStatsAMPDURxDropped,'wlanStatsTxDiscardBadState':wlanStatsTxDiscardBadState,'wlanStatsTxFailedNoAssoc':wlanStatsTxFailedNoAssoc,'wlanStatsTxClassifyFailed':wlanStatsTxClassifyFailed,'wlanStatsDwdsMcastDiscard':wlanStatsDwdsMcastDiscard,'wlanStatsHTAssocRejectNoHT':wlanStatsHTAssocRejectNoHT,'wlanStatsHTAssocDowngrade':wlanStatsHTAssocDowngrade,'wlanStatsHTAssocRateMismatch':wlanStatsHTAssocRateMismatch,'wlanStatsAMPDURxAge':wlanStatsAMPDURxAge,'wlanStatsAMPDUMoved':wlanStatsAMPDUMoved,'wlanStatsADDBADisabledReject':wlanStatsADDBADisabledReject,'wlanStatsADDBANoRequest':wlanStatsADDBANoRequest,'wlanStatsADDBABadToken':wlanStatsADDBABadToken,'wlanStatsADDBABadPolicy':wlanStatsADDBABadPolicy,'wlanStatsAMPDUStopped':wlanStatsAMPDUStopped,'wlanStatsAMPDUStopFailed':wlanStatsAMPDUStopFailed,'wlanStatsAMPDURxReorder':wlanStatsAMPDURxReorder,'wlanStatsScansBackground':wlanStatsScansBackground,'wlanLastDeauthReason':wlanLastDeauthReason,'wlanLastDissasocReason':wlanLastDissasocReason,'wlanLastAuthFailReason':wlanLastAuthFailReason,'wlanStatsBeaconMissedEvents':wlanStatsBeaconMissedEvents,'wlanStatsRxDiscardBadStates':wlanStatsRxDiscardBadStates,'wlanStatsFFFlushed':wlanStatsFFFlushed,'wlanStatsTxControlFrames':wlanStatsTxControlFrames,'wlanStatsAMPDURexmt':wlanStatsAMPDURexmt,'wlanStatsAMPDURexmtFailed':wlanStatsAMPDURexmtFailed,'wlanStatsReset':wlanStatsReset,'begemotWlanWep':begemotWlanWep,'wlanWepInterfaceTable':wlanWepInterfaceTable,'wlanWepInterfaceEntry':wlanWepInterfaceEntry,'wlanWepMode':wlanWepMode,'wlanWepDefTxKey':wlanWepDefTxKey,'wlanWepKeyTable':wlanWepKeyTable,'wlanWepKeyEntry':wlanWepKeyEntry,_o:wlanWepKeyID,'wlanWepKeyLength':wlanWepKeyLength,'wlanWepKeySet':wlanWepKeySet,'wlanWepKeyHash':wlanWepKeyHash,'wlanWepKeyStatus':wlanWepKeyStatus,'begemotWlanMACAccessControl':begemotWlanMACAccessControl,'wlanMACAccessControlTable':wlanMACAccessControlTable,'wlanMACAccessControlEntry':wlanMACAccessControlEntry,'wlanMACAccessControlPolicy':wlanMACAccessControlPolicy,'wlanMACAccessControlNacl':wlanMACAccessControlNacl,'wlanMACAccessControlFlush':wlanMACAccessControlFlush,'wlanMACAccessControlMACTable':wlanMACAccessControlMACTable,'wlanMACAccessControlMACEntry':wlanMACAccessControlMACEntry,_p:wlanMACAccessControlMAC,'wlanMACAccessControlMACStatus':wlanMACAccessControlMACStatus,'begemotWlanMeshRouting':begemotWlanMeshRouting,'wlanMeshRoutingConfig':wlanMeshRoutingConfig,'wlanMeshMaxRetries':wlanMeshMaxRetries,'wlanMeshConfirmTimeout':wlanMeshConfirmTimeout,'wlanMeshHoldingTimeout':wlanMeshHoldingTimeout,'wlanMeshRetryTimeout':wlanMeshRetryTimeout,'wlanMeshInterface':wlanMeshInterface,'wlanMeshInterfaceTable':wlanMeshInterfaceTable,'wlanMeshInterfaceEntry':wlanMeshInterfaceEntry,'wlanMeshId':wlanMeshId,'wlanMeshTTL':wlanMeshTTL,'wlanMeshPeeringEnabled':wlanMeshPeeringEnabled,'wlanMeshForwardingEnabled':wlanMeshForwardingEnabled,'wlanMeshMetric':wlanMeshMetric,'wlanMeshPath':wlanMeshPath,'wlanMeshRoutesFlush':wlanMeshRoutesFlush,'wlanMeshNeighborTable':wlanMeshNeighborTable,'wlanMeshNeighborEntry':wlanMeshNeighborEntry,_q:wlanMeshNeighborAddress,'wlanMeshNeighborFrequency':wlanMeshNeighborFrequency,'wlanMeshNeighborLocalId':wlanMeshNeighborLocalId,'wlanMeshNeighborPeerId':wlanMeshNeighborPeerId,'wlanMeshNeighborPeerState':wlanMeshNeighborPeerState,'wlanMeshNeighborCurrentTXRate':wlanMeshNeighborCurrentTXRate,'wlanMeshNeighborRxSignalStrength':wlanMeshNeighborRxSignalStrength,'wlanMeshNeighborIdleTimer':wlanMeshNeighborIdleTimer,'wlanMeshNeighborTxSequenceNo':wlanMeshNeighborTxSequenceNo,'wlanMeshNeighborRxSequenceNo':wlanMeshNeighborRxSequenceNo,'wlanMeshRoute':wlanMeshRoute,'wlanMeshRouteTable':wlanMeshRouteTable,'wlanMeshRouteEntry':wlanMeshRouteEntry,_r:wlanMeshRouteDestination,'wlanMeshRouteNextHop':wlanMeshRouteNextHop,'wlanMeshRouteHops':wlanMeshRouteHops,'wlanMeshRouteMetric':wlanMeshRouteMetric,'wlanMeshRouteLifeTime':wlanMeshRouteLifeTime,'wlanMeshRouteLastMseq':wlanMeshRouteLastMseq,'wlanMeshRouteFlags':wlanMeshRouteFlags,'wlanMeshRouteStatus':wlanMeshRouteStatus,'wlanMeshStatistics':wlanMeshStatistics,'wlanMeshStatsTable':wlanMeshStatsTable,'wlanMeshStatsEntry':wlanMeshStatsEntry,'wlanMeshDroppedBadSta':wlanMeshDroppedBadSta,'wlanMeshDroppedNoLink':wlanMeshDroppedNoLink,'wlanMeshNoFwdTtl':wlanMeshNoFwdTtl,'wlanMeshNoFwdBuf':wlanMeshNoFwdBuf,'wlanMeshNoFwdTooShort':wlanMeshNoFwdTooShort,'wlanMeshNoFwdDisabled':wlanMeshNoFwdDisabled,'wlanMeshNoFwdPathUnknown':wlanMeshNoFwdPathUnknown,'wlanMeshDroppedBadAE':wlanMeshDroppedBadAE,'wlanMeshRouteAddFailed':wlanMeshRouteAddFailed,'wlanMeshDroppedNoProxy':wlanMeshDroppedNoProxy,'wlanMeshDroppedMisaligned':wlanMeshDroppedMisaligned,'wlanMeshRouteProtocols':wlanMeshRouteProtocols,'wlanMeshProtoHWMP':wlanMeshProtoHWMP,'wlanMeshHWMPConfig':wlanMeshHWMPConfig,'wlanHWMPRouteInactiveTimeout':wlanHWMPRouteInactiveTimeout,'wlanHWMPRootAnnounceInterval':wlanHWMPRootAnnounceInterval,'wlanHWMPRootInterval':wlanHWMPRootInterval,'wlanHWMPRootTimeout':wlanHWMPRootTimeout,'wlanHWMPPathLifetime':wlanHWMPPathLifetime,'wlanHWMPReplyForwardBit':wlanHWMPReplyForwardBit,'wlanHWMPTargetOnlyBit':wlanHWMPTargetOnlyBit,'wlanMeshHWMPInterface':wlanMeshHWMPInterface,'wlanHWMPInterfaceTable':wlanHWMPInterfaceTable,'wlanHWMPInterfaceEntry':wlanHWMPInterfaceEntry,'wlanHWMPRootMode':wlanHWMPRootMode,'wlanHWMPMaxHops':wlanHWMPMaxHops,'wlanMeshHWMPStatistics':wlanMeshHWMPStatistics,'wlanMeshHWMPStatsTable':wlanMeshHWMPStatsTable,'wlanMeshHWMPStatsEntry':wlanMeshHWMPStatsEntry,'wlanMeshHWMPWrongSeqNo':wlanMeshHWMPWrongSeqNo,'wlanMeshHWMPTxRootPREQ':wlanMeshHWMPTxRootPREQ,'wlanMeshHWMPTxRootRANN':wlanMeshHWMPTxRootRANN,'wlanMeshHWMPProxy':wlanMeshHWMPProxy})