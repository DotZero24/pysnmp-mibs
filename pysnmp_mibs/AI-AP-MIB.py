_B3='wlsxTrapApConductorStatus'
_B2='wlsxTrapStationDenyListReason'
_B1='wlsxTrapStationDenyListReasonStr'
_B0='wlsxTrapAuthFailureReason'
_A_='wlsxTrapAPUSBStatus'
_Az='wlsxTrapVcMacAddress'
_Ay='wlsxTrapVcIpAddress'
_Ax='wlsxTrapPortalServerDownReason'
_Aw='wlsxTrapAPManagedModeConfigFailure'
_Av='wlsxTrapAPUplinkChangeReason'
_Au='wlsxTrapAPActiveUplinkType'
_At='wlsxTrapAPPreviousUplinkActiveTime'
_As='wlsxTrapAPPreviousUplinkType'
_Ar='wlsxTrapApMasterStatus'
_Aq='wlsxTrapUserAttributeChangeType'
_Ap='wlsxTrapCardSlot'
_Ao='wlsxTrapAPPrevMode'
_An='wlsxTrapAPCurMode'
_Am='wlsxTrapAPPrevTxPower'
_Al='wlsxTrapAPPrevPhyType'
_Ak='wlsxTrapAPPrevHTMode'
_Aj='wlsxTrapAPARMChangeReason'
_Ai='wlsxTrapAPPrevChannelSec'
_Ah='wlsxTrapAPPrevChannel'
_Ag='wlsxTrapAPChannelSec'
_Af='wlsxTrapAssociationType'
_Ae='wlsxTrapESIServerGrpName'
_Ad='wlsxTrapInterferingAPInfoURL'
_Ac='wlsxTrapMatchedIpv6'
_Ab='wlsxTrapAPSecChannel'
_Aa='wlsxTrapAPIpAddress'
_AZ='wlsxTrapStationBlackListReasonStr'
_AY='wlsxTrapStationBlackListReason'
_AX='wlsxTrapAuthServerTimeout'
_AW='wlsxTrapUserRole'
_AV='wlsxTrapUserAuthenticationMethod'
_AU='aiClientMac'
_AT='aiClientMACAddress'
_AS='aiWlanIndex'
_AR='aiWlanAPMACAddress'
_AQ='aiRadioIndex'
_AP='aiRadioAPMACAddress'
_AO='aiAPMACAddress'
_AN='aiMeshIndex'
_AM='aiInterferAPIndex'
_AL='aiSSIDIndex'
_AK='notPresent'
_AJ='ipSpoofing'
_AI='sessionFlood'
_AH='pingFlood'
_AG='authFailure'
_AF='mitmAttack'
_AE='userDefined'
_AD='notApplicable'
_AC='interfering'
_AB='wpa3-sae-aes'
_AA='wpa3-cnsa'
_A9='wpa2-psk-aes'
_A8='wpa2-psk-tkip'
_A7='wpa-psk-aes'
_A6='dynamic-wep'
_A5='static-wep'
_A4='wlsxTrapEssid'
_A3='wlsxTrapUSBVendorProductID'
_A2='wlsxTrapPortalServerAddress'
_A1='wlsxTrapPortalServerName'
_A0='wlsxTrapApControllerIp'
_z='wlsxTrapVlanId'
_y='wlsxTrapTargetAPBand'
_x='wlsxTrapSpoofedFrameType'
_w='wlsxTrapConfidenceLevel'
_v='wlsxTrapAddressType'
_u='wlsxTrapMatchedIp'
_t='wlsxTrapMatchedMac'
_s='wlsxTrapAPHTMode'
_r='wlsxTrapAPPhyType'
_q='wlsxTrapAPTxPower'
_p='enabled'
_o='OctetString'
_n='wlsxTrapPortNumber'
_m='wlsxTrapRogueInfoURL'
_l='wlsxTrapDeviceMac'
_k='wlsxTrapDeviceIpAddress'
_j='wlsxTrapTargetAPChannel'
_i='other'
_h='disabled'
_g='wlsxTrapUserName'
_f='Integer32'
_e='wlsxTrapAuthServerAddress'
_d='down'
_c='up'
_b='none'
_a='unknown'
_Z='wlsxTrapAuthServerName'
_Y='wlsxTrapAPBSSID'
_X='wlsxTrapFrameType'
_W='wlsxTrapTransmitterMac'
_V='wlsxTrapUserIpAddress'
_U='obsolete'
_T='wlsxTrapUserPhyAddress'
_S='wlsxTrapAPName'
_R='wlsxTrapReceiverMac'
_Q='wlsxTrapSignatureName'
_P='wlsxTrapNodeMac'
_O='wlsxTrapSourceMac'
_N='DisplayString'
_M='wlsxTrapSnr'
_L='wlsxTrapTargetAPSSID'
_K='wlsxTrapAPBand'
_J='read-only'
_I='wlsxTrapAPChannel'
_H='wlsxTrapTargetAPBSSID'
_G='wlsxTrapAPLocation'
_F='wlsxTrapAPRadioNumber'
_E='accessible-for-notify'
_D='wlsxTrapAPMacAddress'
_C='wlsxTrapTime'
_B='current'
_A='AI-AP-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_o,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
aiEnterpriseMibModules,=mibBuilder.importSymbols('ARUBA-MIB','aiEnterpriseMibModules')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso,snmpModules=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_f,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso','snmpModules')
DateAndTime,DisplayString,MacAddress,PhysAddress,RowStatus,StorageType,TextualConvention,TestAndIncr,TimeInterval,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime',_N,'MacAddress','PhysAddress','RowStatus','StorageType','TextualConvention','TestAndIncr','TimeInterval','TruthValue')
aiMIB=ModuleIdentity((1,3,6,1,4,1,14823,2,3,3,1))
if mibBuilder.loadTexts:aiMIB.setRevisions(('2020-08-14 17:45',))
class ArubaEnableValue(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_p,1),(_h,2)))
class ArubaFrameType(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,8,9,10,11,12)));namedValues=NamedValues(*(('associateRequest',0),('associateResponse',1),('reassociateRequest',2),('reassociateResponse',3),('probeRequest',4),('probeResponse',5),('beacon',8),('atim',9),('disassociate',10),('auth',11),('deauth',12)))
class ArubaPhyType(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*(('dot11a',1),('dot11b',2),('dot11g',3),('dot11ag',4),('wired',5),('dot11ax6ghz',6)))
class ArubaHTMode(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13)));namedValues=NamedValues(*((_b,1),('ht20',2),('ht40',3),('vht20',4),('vht40',5),('vht80',6),('vht160',7),('vht80plus80',8),('he20',9),('he40',10),('he80',11),('he160',12),('he80plus80',13)))
class ArubaHTExtChannel(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_b,1),('above',2),('below',3)))
class ArubaMonEncryptionType(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4)));namedValues=NamedValues(*(('open',0),('wep',1),('wpa',2),('wpa2',3),('wpa3',4)))
class ArubaMonEncryptionCipher(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6)));namedValues=NamedValues(*((_b,0),('wep40',1),('wep104',2),('tkip',3),('aesccmp',4),(_i,5),('gcm256',6)))
class ArubaMonAuthAlgorithm(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7,8,9,10,11,12)));namedValues=NamedValues(*((_b,0),('psk',1),('dot1x',2),('ft8021x',3),('ftpsk',4),('dot1x256',5),('psk256',6),('tdls',7),('sae',8),('ftsae',9),(_i,10),('suiteb',11),('owe',12)))
class ArubaSwitchRole(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('conductor',1),('local',2),('backupconductor',3)))
class ArubaSupportStatus(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('unsupported',1),('supported',2)))
class ArubaActiveState(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('active',1),('inactive',2)))
class ArubaACLDomain(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('alias',1),('any',2),('user',3),('host',4),('network',5)))
class ArubaACLNetworkServiceType(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('alias',1),('any',2),('tcp',3),('udp',4),('protocol',5)))
class ArubaACLAction(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('deny',1),('permit',2),('srcNAT',3),('dstNAT',4),('redirect',5)))
class ArubaDaysOfWeek(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*(('sun',1),('mon',2),('tue',3),('wed',4),('thu',5),('fri',6),('sat',7)))
class ArubaAuthenticationMethods(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,7,15,16,17,28,255)));namedValues=NamedValues(*((_b,0),('web',1),('mac',2),('vpn',3),('dot1x',4),('kerberos',5),('secureId',7),('pubcookie',15),('xSec',16),('xSecMachine',17),('via-vpn',28),(_i,255)))
class ArubaSubAuthenticationMethods(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9)));namedValues=NamedValues(*(('authPAP',1),('authCHAP',2),('authMSCHAP',3),('authMSCHAPv2',4),('eapTLS',5),('eapTTLS',6),('eapLEAP',7),('eapMD5',8),('eapPEAP',9)))
class ArubaEncryptionType(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,20,21,22)));namedValues=NamedValues(*((_b,0),(_A5,1),(_A6,2),('wpa-psk-tkip',3),('wpa-tkip',4),(_A7,5),('wpa-aes',6),(_A8,7),('wpa2-tkip',8),(_A9,9),('wpa2-aes',10),('xSec',11),('bSec-128',12),('bSec-256',13),('aes-128-cmac',14),(_a,15),('ft-psk',16),('ft-8021x',17),(_AA,18),('owe-aes',20),(_AB,21),('wpa3-aes-gcmp-256',22)))
class ArubaUserForwardMode(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*(('tunnel-encrypted',0),('bridge',1),('tunnel-decrypted',2),('split-tunnel',3)))
class ArubaRogueApType(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*(('valid',1),(_AC,2),('unsecure',3),('dos',4),(_a,5),('knownInterfering',6),('suspectedUnsecure',7)))
class ArubaAPMatchType(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7,8,9,10,11,12,13,14)));namedValues=NamedValues(*((_a,0),('configuredWiredMac',1),('ethernetWiredMac',2),('apWiredMac',3),('externalWiredMac',4),('manual',5),('baseBSSIDOverride',6),('mms',7),('ethernetGatewayWiredMac',8),('classificationDisabled',9),('apBSSID',10),('propagatedEthernetWiredMac',11),('apRule',12),('systemWiredMac',13),('systemGatewayMac',14)))
class ArubaAPMatchMethod(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4)));namedValues=NamedValues(*((_AD,0),('exactMatch',1),('plusOneMatch',2),('minusOneMatch',3),('ouiMatch',4)))
class ArubaStationType(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('valid',1),(_AC,2),('dos',3)))
class ArubaEncryptionMethods(TextualConvention,Bits):status=_B;namedValues=NamedValues(*((_h,0),(_A5,1),(_A6,2),('static-wpa',3),('dynamic-wpa',4),(_A9,5),('wpa2-8021x-aes',6),('wpa2PreAuth',7),('xsec',8),(_A7,9),('wpa-aes',10),(_A8,11),('wpa2-8021x-tkip',12),('bSec-128',13),('bSec-256',14),('owe-aes',16),(_AB,17),(_AA,18),('wpa3-aes-ccm-128',19),('mpsk-aes',21),('wpa3-aes-gcm-256',22)))
class ArubaHashAlgorithms(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('md5',1),('sha',2)))
class ArubaVlanValidRange(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4095))
class ArubaPortMode(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('access',1),('dot1q',2)))
class ArubaDot1dState(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_h,1),('blocked',2),('listening',3),('learning',4),('forwarding',5)))
class ArubaPoeState(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_h,1),(_p,2),('enabledCisco',3),('notAvailable',4)))
class ArubaCardType(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16)));namedValues=NamedValues(*(('lc1',1),('lc2',2),('sc1',3),('sc2',4),('sw2400',5),('sw800',6),('sw200',7),('m3mk1',8),('sw3200',9),('sw3400',10),('sw3600',11),('sw650',12),('sw651',13),('reserved1',14),('reserved2',15),('sw620',16)))
class ArubaESIServerMode(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('bridged',1),('routed',2),('nat',3)))
class ArubaESIServerStatus(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_c,1),(_d,2)))
class ArubaIfType(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('port',1),('vlan',2),('tunnel',3),('loopback',4)))
class ArubaVoipProtocolType(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,10)));namedValues=NamedValues(*(('sccp',1),('svp',2),('vocera',3),('sip',4),(_a,10)))
class ArubaAccessPointMode(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*(('airMonitor',1),('accessPoint',2),('accessPointAndMonitor',3),('meshPortal',4),('meshPoint',5),('rfprotectSensor',6),('spectrumSensor',7)))
class ArubaAuthServerType(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('internaldb',1),('radius',2),('ldap',3),('kerberos',4),('tacacs',5)))
class ArubaAddressType(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('srcAddress',1),('dstAddress',2),('bssid',3)))
class ArubaBlackListReason(TextualConvention,Integer32):status=_U;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,100)));namedValues=NamedValues(*((_AE,1),(_AF,2),(_AG,3),(_AH,4),(_AI,5),('synFlood',6),('sessionBlacklist',7),(_AJ,8),('esiBlacklist',9),(_i,100)))
class ArubaDBType(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('mssql',1),('mysql',2)))
class ArubaVrrpState(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('initialize',1),('backup',2),('master',3)))
class ArubaOperStateValue(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_c,1),(_d,2),('testing',3)))
class ArubaAntennaSetting(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_AK,1),(_p,2),(_h,3)))
class ArubaAPStatus(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_c,1),(_d,2)))
class ArubaPortSpeed(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('speed10Mbps',1),('speed100Mbps',2),('speed1000Mbps',3),('speedAuto',4),('speed10Gbps',5)))
class ArubaPortDuplex(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('half',1),('full',2),('auto',3)))
class ArubaPortType(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('fastethernet',1),('gigabitethernet',2),('xgigabitethernet',3)))
class ArubaEnet1Mode(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('activeStandby',1),('tunnel',2),('bridge',3),(_AD,4),('split',5)))
class ArubaUnprovisionedStatus(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('yes',1),('no',2)))
class ArubaMonitorMode(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*((_a,0),('all',1),(_b,2),('mixed',3)))
class ArubaConfigurationState(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('success',1),('error',2)))
class ArubaConfigurationChangeType(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('create',1),('delete',2),('modify',3)))
class ArubaCallStates(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15)));namedValues=NamedValues(*(('idle',0),('initiated',1),('connecting',2),('delivered',3),('connected',4),('offered',5),('alerting',6),('releasing',7),('cancelling',8),('challenging',9),('transient',10),('blockwait',11),('succ',12),('fail',13),('aborted',14),('blocked',15)))
class ArubaVoipProtocol(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,9,11)));namedValues=NamedValues(*(('sccp',1),('svp',2),('vocera',3),('sip',9),('ua',11)))
class ArubaVoipRegState(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5)));namedValues=NamedValues(*((_a,0),('registering',1),('unregistering',2),('challenge',3),('registered',4),('unregistered',5)))
class ArubaVoiceCdrDirection(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('og',0),('ic',1)))
class ArubaVoiceCacBit(TextualConvention,Bits):status=_B;namedValues=NamedValues(*(('cacActiveLoadBalancing',0),('cacHighCapThresholdReached',1),('cacHandRsrvThresholdReached',2),('cacPeakCapacityReached',3)))
class ArubaMeshRole(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('nonmesh',0),('point',1),('portal',2)))
class ArubaHTRate(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34)));namedValues=NamedValues(*((_a,0),('ht6dot5',1),('ht13',2),('ht13dot5',3),('ht15',4),('ht19dot5',5),('ht26',6),('ht27',7),('ht30',8),('ht39',9),('ht40dot5',10),('ht45',11),('ht52',12),('ht54',13),('ht58dot5',14),('ht60',15),('ht65',16),('ht78',17),('ht81',18),('ht90',19),('ht104',20),('ht108',21),('ht117',22),('ht120',23),('ht121dot5',24),('ht130',25),('ht135',26),('ht150',27),('ht162',28),('ht180',29),('ht216',30),('ht240',31),('ht243',32),('ht270',33),('ht300',34)))
class ArubaUSBStatus(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*((_a,0),(_AK,1),('inactive',2),('active',3)))
class ArubaARMChangeReason(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17)));namedValues=NamedValues(*(('radarDetected',1),('radarCleared',2),('txHang',3),('txHangClear',4),('fortyMhzIntol',5),('cancel40mhzIntol',6),('fortyMhzAlign',7),('armInterference',8),('armInvalidCh',9),('armErrorThresh',10),('armNoiseThresh',11),('armEmptyCh',12),('armRogueCont',13),('armDecreasePower',14),('armIncreasePower',15),('armTurnOffRadio',16),('armTurnOnRadio',17)))
class ArubaAPMasterStatus(TextualConvention,Integer32):status=_U;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_c,1),(_d,2),('move',3)))
class ArubaAPUplinkType(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('ethernet',1),('usb',2),('pppoe',3),('wifi',4)))
class ArubaAPUplinkChangeReason(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('linkFailure',1),('vpnFailure',2),('preemption',3),('internetFailover',4)))
class ArubaPortalServerDownReason(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues(('connectFail',1))
class ArubaDenyListReason(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,100)));namedValues=NamedValues(*((_AE,1),(_AF,2),(_AG,3),(_AH,4),(_AI,5),('synFlood',6),('sessionDenylist',7),(_AJ,8),('esiDenylist',9),(_i,100)))
class ArubaAPConductorStatus(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_c,1),(_d,2),('move',3)))
_AiInfoGroup_ObjectIdentity=ObjectIdentity
aiInfoGroup=_AiInfoGroup_ObjectIdentity((1,3,6,1,4,1,14823,2,3,3,1,1))
_AiVirtualControllerKey_Type=DisplayString
_AiVirtualControllerKey_Object=MibScalar
aiVirtualControllerKey=_AiVirtualControllerKey_Object((1,3,6,1,4,1,14823,2,3,3,1,1,1),_AiVirtualControllerKey_Type())
aiVirtualControllerKey.setMaxAccess(_J)
if mibBuilder.loadTexts:aiVirtualControllerKey.setStatus(_B)
_AiVirtualControllerName_Type=DisplayString
_AiVirtualControllerName_Object=MibScalar
aiVirtualControllerName=_AiVirtualControllerName_Object((1,3,6,1,4,1,14823,2,3,3,1,1,2),_AiVirtualControllerName_Type())
aiVirtualControllerName.setMaxAccess(_J)
if mibBuilder.loadTexts:aiVirtualControllerName.setStatus(_B)
_AiVirtualControllerOrganization_Type=DisplayString
_AiVirtualControllerOrganization_Object=MibScalar
aiVirtualControllerOrganization=_AiVirtualControllerOrganization_Object((1,3,6,1,4,1,14823,2,3,3,1,1,3),_AiVirtualControllerOrganization_Type())
aiVirtualControllerOrganization.setMaxAccess(_J)
if mibBuilder.loadTexts:aiVirtualControllerOrganization.setStatus(_B)
_AiVirtualControllerVersion_Type=DisplayString
_AiVirtualControllerVersion_Object=MibScalar
aiVirtualControllerVersion=_AiVirtualControllerVersion_Object((1,3,6,1,4,1,14823,2,3,3,1,1,4),_AiVirtualControllerVersion_Type())
aiVirtualControllerVersion.setMaxAccess(_J)
if mibBuilder.loadTexts:aiVirtualControllerVersion.setStatus(_B)
_AiVirtualControllerIPAddress_Type=IpAddress
_AiVirtualControllerIPAddress_Object=MibScalar
aiVirtualControllerIPAddress=_AiVirtualControllerIPAddress_Object((1,3,6,1,4,1,14823,2,3,3,1,1,5),_AiVirtualControllerIPAddress_Type())
aiVirtualControllerIPAddress.setMaxAccess(_J)
if mibBuilder.loadTexts:aiVirtualControllerIPAddress.setStatus(_B)
_AiMasterIPAddress_Type=IpAddress
_AiMasterIPAddress_Object=MibScalar
aiMasterIPAddress=_AiMasterIPAddress_Object((1,3,6,1,4,1,14823,2,3,3,1,1,6),_AiMasterIPAddress_Type())
aiMasterIPAddress.setMaxAccess(_J)
if mibBuilder.loadTexts:aiMasterIPAddress.setStatus(_U)
_AiWlanSSIDTable_Object=MibTable
aiWlanSSIDTable=_AiWlanSSIDTable_Object((1,3,6,1,4,1,14823,2,3,3,1,1,7))
if mibBuilder.loadTexts:aiWlanSSIDTable.setStatus(_B)
_AiWlanSSIDEntry_Object=MibTableRow
aiWlanSSIDEntry=_AiWlanSSIDEntry_Object((1,3,6,1,4,1,14823,2,3,3,1,1,7,1))
aiWlanSSIDEntry.setIndexNames((0,_A,_AL))
if mibBuilder.loadTexts:aiWlanSSIDEntry.setStatus(_B)
_AiSSIDIndex_Type=Integer32
_AiSSIDIndex_Object=MibTableColumn
aiSSIDIndex=_AiSSIDIndex_Object((1,3,6,1,4,1,14823,2,3,3,1,1,7,1,1),_AiSSIDIndex_Type())
aiSSIDIndex.setMaxAccess(_J)
if mibBuilder.loadTexts:aiSSIDIndex.setStatus(_B)
class _AiSSID_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_AiSSID_Type.__name__=_o
_AiSSID_Object=MibTableColumn
aiSSID=_AiSSID_Object((1,3,6,1,4,1,14823,2,3,3,1,1,7,1,2),_AiSSID_Type())
aiSSID.setMaxAccess(_J)
if mibBuilder.loadTexts:aiSSID.setStatus(_B)
class _AiSSIDStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('enable',0),('disable',1)))
_AiSSIDStatus_Type.__name__=_f
_AiSSIDStatus_Object=MibTableColumn
aiSSIDStatus=_AiSSIDStatus_Object((1,3,6,1,4,1,14823,2,3,3,1,1,7,1,3),_AiSSIDStatus_Type())
aiSSIDStatus.setMaxAccess(_J)
if mibBuilder.loadTexts:aiSSIDStatus.setStatus(_B)
_AiSSIDClientNum_Type=Integer32
_AiSSIDClientNum_Object=MibTableColumn
aiSSIDClientNum=_AiSSIDClientNum_Object((1,3,6,1,4,1,14823,2,3,3,1,1,7,1,4),_AiSSIDClientNum_Type())
aiSSIDClientNum.setMaxAccess(_J)
if mibBuilder.loadTexts:aiSSIDClientNum.setStatus(_B)
class _AiSSIDHide_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('disable',0),('enable',1)))
_AiSSIDHide_Type.__name__=_f
_AiSSIDHide_Object=MibTableColumn
aiSSIDHide=_AiSSIDHide_Object((1,3,6,1,4,1,14823,2,3,3,1,1,7,1,5),_AiSSIDHide_Type())
aiSSIDHide.setMaxAccess(_J)
if mibBuilder.loadTexts:aiSSIDHide.setStatus(_B)
_AiInterferAccessPointTable_Object=MibTable
aiInterferAccessPointTable=_AiInterferAccessPointTable_Object((1,3,6,1,4,1,14823,2,3,3,1,1,8))
if mibBuilder.loadTexts:aiInterferAccessPointTable.setStatus(_B)
_AiInterferAccessPointEntry_Object=MibTableRow
aiInterferAccessPointEntry=_AiInterferAccessPointEntry_Object((1,3,6,1,4,1,14823,2,3,3,1,1,8,1))
aiInterferAccessPointEntry.setIndexNames((0,_A,_AM))
if mibBuilder.loadTexts:aiInterferAccessPointEntry.setStatus(_B)
_AiInterferAPIndex_Type=Integer32
_AiInterferAPIndex_Object=MibTableColumn
aiInterferAPIndex=_AiInterferAPIndex_Object((1,3,6,1,4,1,14823,2,3,3,1,1,8,1,1),_AiInterferAPIndex_Type())
aiInterferAPIndex.setMaxAccess(_J)
if mibBuilder.loadTexts:aiInterferAPIndex.setStatus(_B)
_AiInterferAPBSSID_Type=MacAddress
_AiInterferAPBSSID_Object=MibTableColumn
aiInterferAPBSSID=_AiInterferAPBSSID_Object((1,3,6,1,4,1,14823,2,3,3,1,1,8,1,2),_AiInterferAPBSSID_Type())
aiInterferAPBSSID.setMaxAccess(_J)
if mibBuilder.loadTexts:aiInterferAPBSSID.setStatus(_B)
class _AiInterferAPESSID_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_AiInterferAPESSID_Type.__name__=_o
_AiInterferAPESSID_Object=MibTableColumn
aiInterferAPESSID=_AiInterferAPESSID_Object((1,3,6,1,4,1,14823,2,3,3,1,1,8,1,3),_AiInterferAPESSID_Type())
aiInterferAPESSID.setMaxAccess(_J)
if mibBuilder.loadTexts:aiInterferAPESSID.setStatus(_B)
_AiInterferAPChannel_Type=DisplayString
_AiInterferAPChannel_Object=MibTableColumn
aiInterferAPChannel=_AiInterferAPChannel_Object((1,3,6,1,4,1,14823,2,3,3,1,1,8,1,4),_AiInterferAPChannel_Type())
aiInterferAPChannel.setMaxAccess(_J)
if mibBuilder.loadTexts:aiInterferAPChannel.setStatus(_B)
_AiInterferAPPhyType_Type=DisplayString
_AiInterferAPPhyType_Object=MibTableColumn
aiInterferAPPhyType=_AiInterferAPPhyType_Object((1,3,6,1,4,1,14823,2,3,3,1,1,8,1,5),_AiInterferAPPhyType_Type())
aiInterferAPPhyType.setMaxAccess(_J)
if mibBuilder.loadTexts:aiInterferAPPhyType.setStatus(_B)
_AiInterferAPEncr_Type=DisplayString
_AiInterferAPEncr_Object=MibTableColumn
aiInterferAPEncr=_AiInterferAPEncr_Object((1,3,6,1,4,1,14823,2,3,3,1,1,8,1,6),_AiInterferAPEncr_Type())
aiInterferAPEncr.setMaxAccess(_J)
if mibBuilder.loadTexts:aiInterferAPEncr.setStatus(_B)
_AiInterferAPAvgSnr_Type=Integer32
_AiInterferAPAvgSnr_Object=MibTableColumn
aiInterferAPAvgSnr=_AiInterferAPAvgSnr_Object((1,3,6,1,4,1,14823,2,3,3,1,1,8,1,7),_AiInterferAPAvgSnr_Type())
aiInterferAPAvgSnr.setMaxAccess(_J)
if mibBuilder.loadTexts:aiInterferAPAvgSnr.setStatus(_B)
_AiInterferAPType_Type=DisplayString
_AiInterferAPType_Object=MibTableColumn
aiInterferAPType=_AiInterferAPType_Object((1,3,6,1,4,1,14823,2,3,3,1,1,8,1,8),_AiInterferAPType_Type())
aiInterferAPType.setMaxAccess(_J)
if mibBuilder.loadTexts:aiInterferAPType.setStatus(_B)
_AiMeshTable_Object=MibTable
aiMeshTable=_AiMeshTable_Object((1,3,6,1,4,1,14823,2,3,3,1,1,15))
if mibBuilder.loadTexts:aiMeshTable.setStatus(_B)
_AiMeshEntry_Object=MibTableRow
aiMeshEntry=_AiMeshEntry_Object((1,3,6,1,4,1,14823,2,3,3,1,1,15,1))
aiMeshEntry.setIndexNames((0,_A,_AN))
if mibBuilder.loadTexts:aiMeshEntry.setStatus(_B)
_AiMeshIndex_Type=Integer32
_AiMeshIndex_Object=MibTableColumn
aiMeshIndex=_AiMeshIndex_Object((1,3,6,1,4,1,14823,2,3,3,1,1,15,1,1),_AiMeshIndex_Type())
aiMeshIndex.setMaxAccess(_J)
if mibBuilder.loadTexts:aiMeshIndex.setStatus(_B)
_AiMeshPointMac_Type=MacAddress
_AiMeshPointMac_Object=MibTableColumn
aiMeshPointMac=_AiMeshPointMac_Object((1,3,6,1,4,1,14823,2,3,3,1,1,15,1,2),_AiMeshPointMac_Type())
aiMeshPointMac.setMaxAccess(_J)
if mibBuilder.loadTexts:aiMeshPointMac.setStatus(_B)
_AiMeshPortalMac_Type=DisplayString
_AiMeshPortalMac_Object=MibTableColumn
aiMeshPortalMac=_AiMeshPortalMac_Object((1,3,6,1,4,1,14823,2,3,3,1,1,15,1,3),_AiMeshPortalMac_Type())
aiMeshPortalMac.setMaxAccess(_J)
if mibBuilder.loadTexts:aiMeshPortalMac.setStatus(_B)
_AiMeshChannel_Type=DisplayString
_AiMeshChannel_Object=MibTableColumn
aiMeshChannel=_AiMeshChannel_Object((1,3,6,1,4,1,14823,2,3,3,1,1,15,1,4),_AiMeshChannel_Type())
aiMeshChannel.setMaxAccess(_J)
if mibBuilder.loadTexts:aiMeshChannel.setStatus(_B)
_AiMeshAvgRssi_Type=Integer32
_AiMeshAvgRssi_Object=MibTableColumn
aiMeshAvgRssi=_AiMeshAvgRssi_Object((1,3,6,1,4,1,14823,2,3,3,1,1,15,1,5),_AiMeshAvgRssi_Type())
aiMeshAvgRssi.setMaxAccess(_J)
if mibBuilder.loadTexts:aiMeshAvgRssi.setStatus(_B)
_AiMeshHops_Type=Integer32
_AiMeshHops_Object=MibTableColumn
aiMeshHops=_AiMeshHops_Object((1,3,6,1,4,1,14823,2,3,3,1,1,15,1,6),_AiMeshHops_Type())
aiMeshHops.setMaxAccess(_J)
if mibBuilder.loadTexts:aiMeshHops.setStatus(_B)
_AiMeshAge_Type=Integer32
_AiMeshAge_Object=MibTableColumn
aiMeshAge=_AiMeshAge_Object((1,3,6,1,4,1,14823,2,3,3,1,1,15,1,7),_AiMeshAge_Type())
aiMeshAge.setMaxAccess(_J)
if mibBuilder.loadTexts:aiMeshAge.setStatus(_B)
_AiMeshCost_Type=DisplayString
_AiMeshCost_Object=MibTableColumn
aiMeshCost=_AiMeshCost_Object((1,3,6,1,4,1,14823,2,3,3,1,1,15,1,8),_AiMeshCost_Type())
aiMeshCost.setMaxAccess(_J)
if mibBuilder.loadTexts:aiMeshCost.setStatus(_B)
_AiMeshRelation_Type=DisplayString
_AiMeshRelation_Object=MibTableColumn
aiMeshRelation=_AiMeshRelation_Object((1,3,6,1,4,1,14823,2,3,3,1,1,15,1,9),_AiMeshRelation_Type())
aiMeshRelation.setMaxAccess(_J)
if mibBuilder.loadTexts:aiMeshRelation.setStatus(_B)
_AiConductorIPAddress_Type=IpAddress
_AiConductorIPAddress_Object=MibScalar
aiConductorIPAddress=_AiConductorIPAddress_Object((1,3,6,1,4,1,14823,2,3,3,1,1,16),_AiConductorIPAddress_Type())
aiConductorIPAddress.setMaxAccess(_J)
if mibBuilder.loadTexts:aiConductorIPAddress.setStatus(_B)
_AiStateGroup_ObjectIdentity=ObjectIdentity
aiStateGroup=_AiStateGroup_ObjectIdentity((1,3,6,1,4,1,14823,2,3,3,1,2))
_AiAccessPointTable_Object=MibTable
aiAccessPointTable=_AiAccessPointTable_Object((1,3,6,1,4,1,14823,2,3,3,1,2,1))
if mibBuilder.loadTexts:aiAccessPointTable.setStatus(_B)
_AiAccessPointEntry_Object=MibTableRow
aiAccessPointEntry=_AiAccessPointEntry_Object((1,3,6,1,4,1,14823,2,3,3,1,2,1,1))
aiAccessPointEntry.setIndexNames((0,_A,_AO))
if mibBuilder.loadTexts:aiAccessPointEntry.setStatus(_B)
_AiAPMACAddress_Type=MacAddress
_AiAPMACAddress_Object=MibTableColumn
aiAPMACAddress=_AiAPMACAddress_Object((1,3,6,1,4,1,14823,2,3,3,1,2,1,1,1),_AiAPMACAddress_Type())
aiAPMACAddress.setMaxAccess(_J)
if mibBuilder.loadTexts:aiAPMACAddress.setStatus(_B)
class _AiAPName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_AiAPName_Type.__name__=_N
_AiAPName_Object=MibTableColumn
aiAPName=_AiAPName_Object((1,3,6,1,4,1,14823,2,3,3,1,2,1,1,2),_AiAPName_Type())
aiAPName.setMaxAccess(_J)
if mibBuilder.loadTexts:aiAPName.setStatus(_B)
_AiAPIPAddress_Type=IpAddress
_AiAPIPAddress_Object=MibTableColumn
aiAPIPAddress=_AiAPIPAddress_Object((1,3,6,1,4,1,14823,2,3,3,1,2,1,1,3),_AiAPIPAddress_Type())
aiAPIPAddress.setMaxAccess(_J)
if mibBuilder.loadTexts:aiAPIPAddress.setStatus(_B)
class _AiAPSerialNum_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_AiAPSerialNum_Type.__name__=_N
_AiAPSerialNum_Object=MibTableColumn
aiAPSerialNum=_AiAPSerialNum_Object((1,3,6,1,4,1,14823,2,3,3,1,2,1,1,4),_AiAPSerialNum_Type())
aiAPSerialNum.setMaxAccess(_J)
if mibBuilder.loadTexts:aiAPSerialNum.setStatus(_B)
_AiAPModel_Type=ObjectIdentifier
_AiAPModel_Object=MibTableColumn
aiAPModel=_AiAPModel_Object((1,3,6,1,4,1,14823,2,3,3,1,2,1,1,5),_AiAPModel_Type())
aiAPModel.setMaxAccess(_J)
if mibBuilder.loadTexts:aiAPModel.setStatus(_B)
class _AiAPModelName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_AiAPModelName_Type.__name__=_N
_AiAPModelName_Object=MibTableColumn
aiAPModelName=_AiAPModelName_Object((1,3,6,1,4,1,14823,2,3,3,1,2,1,1,6),_AiAPModelName_Type())
aiAPModelName.setMaxAccess(_J)
if mibBuilder.loadTexts:aiAPModelName.setStatus(_B)
_AiAPCPUUtilization_Type=Integer32
_AiAPCPUUtilization_Object=MibTableColumn
aiAPCPUUtilization=_AiAPCPUUtilization_Object((1,3,6,1,4,1,14823,2,3,3,1,2,1,1,7),_AiAPCPUUtilization_Type())
aiAPCPUUtilization.setMaxAccess(_J)
if mibBuilder.loadTexts:aiAPCPUUtilization.setStatus(_B)
_AiAPMemoryFree_Type=Integer32
_AiAPMemoryFree_Object=MibTableColumn
aiAPMemoryFree=_AiAPMemoryFree_Object((1,3,6,1,4,1,14823,2,3,3,1,2,1,1,8),_AiAPMemoryFree_Type())
aiAPMemoryFree.setMaxAccess(_J)
if mibBuilder.loadTexts:aiAPMemoryFree.setStatus(_B)
_AiAPUptime_Type=TimeTicks
_AiAPUptime_Object=MibTableColumn
aiAPUptime=_AiAPUptime_Object((1,3,6,1,4,1,14823,2,3,3,1,2,1,1,9),_AiAPUptime_Type())
aiAPUptime.setMaxAccess(_J)
if mibBuilder.loadTexts:aiAPUptime.setStatus(_B)
_AiAPTotalMemory_Type=Integer32
_AiAPTotalMemory_Object=MibTableColumn
aiAPTotalMemory=_AiAPTotalMemory_Object((1,3,6,1,4,1,14823,2,3,3,1,2,1,1,10),_AiAPTotalMemory_Type())
aiAPTotalMemory.setMaxAccess(_J)
if mibBuilder.loadTexts:aiAPTotalMemory.setStatus(_B)
class _AiAPStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_c,1),(_d,2)))
_AiAPStatus_Type.__name__=_f
_AiAPStatus_Object=MibTableColumn
aiAPStatus=_AiAPStatus_Object((1,3,6,1,4,1,14823,2,3,3,1,2,1,1,11),_AiAPStatus_Type())
aiAPStatus.setMaxAccess(_J)
if mibBuilder.loadTexts:aiAPStatus.setStatus(_B)
class _AiAPHwopmode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7)));namedValues=NamedValues(*(('default',0),('rsdbsplit',1),('rsdb5g',2),('rsdb2g',3),('dual5gon',4),('dual5goff',5),('split5goff',6),('split5gon',7)))
_AiAPHwopmode_Type.__name__=_f
_AiAPHwopmode_Object=MibTableColumn
aiAPHwopmode=_AiAPHwopmode_Object((1,3,6,1,4,1,14823,2,3,3,1,2,1,1,12),_AiAPHwopmode_Type())
aiAPHwopmode.setMaxAccess(_J)
if mibBuilder.loadTexts:aiAPHwopmode.setStatus(_B)
_AiAPRole_Type=DisplayString
_AiAPRole_Object=MibTableColumn
aiAPRole=_AiAPRole_Object((1,3,6,1,4,1,14823,2,3,3,1,2,1,1,13),_AiAPRole_Type())
aiAPRole.setMaxAccess(_J)
if mibBuilder.loadTexts:aiAPRole.setStatus(_B)
_AiRadioTable_Object=MibTable
aiRadioTable=_AiRadioTable_Object((1,3,6,1,4,1,14823,2,3,3,1,2,2))
if mibBuilder.loadTexts:aiRadioTable.setStatus(_B)
_AiRadioEntry_Object=MibTableRow
aiRadioEntry=_AiRadioEntry_Object((1,3,6,1,4,1,14823,2,3,3,1,2,2,1))
aiRadioEntry.setIndexNames((0,_A,_AP),(0,_A,_AQ))
if mibBuilder.loadTexts:aiRadioEntry.setStatus(_B)
_AiRadioAPMACAddress_Type=MacAddress
_AiRadioAPMACAddress_Object=MibTableColumn
aiRadioAPMACAddress=_AiRadioAPMACAddress_Object((1,3,6,1,4,1,14823,2,3,3,1,2,2,1,1),_AiRadioAPMACAddress_Type())
aiRadioAPMACAddress.setMaxAccess(_J)
if mibBuilder.loadTexts:aiRadioAPMACAddress.setStatus(_B)
_AiRadioIndex_Type=Integer32
_AiRadioIndex_Object=MibTableColumn
aiRadioIndex=_AiRadioIndex_Object((1,3,6,1,4,1,14823,2,3,3,1,2,2,1,2),_AiRadioIndex_Type())
aiRadioIndex.setMaxAccess(_J)
if mibBuilder.loadTexts:aiRadioIndex.setStatus(_B)
_AiRadioMACAddress_Type=MacAddress
_AiRadioMACAddress_Object=MibTableColumn
aiRadioMACAddress=_AiRadioMACAddress_Object((1,3,6,1,4,1,14823,2,3,3,1,2,2,1,3),_AiRadioMACAddress_Type())
aiRadioMACAddress.setMaxAccess(_J)
if mibBuilder.loadTexts:aiRadioMACAddress.setStatus(_B)
_AiRadioChannel_Type=DisplayString
_AiRadioChannel_Object=MibTableColumn
aiRadioChannel=_AiRadioChannel_Object((1,3,6,1,4,1,14823,2,3,3,1,2,2,1,4),_AiRadioChannel_Type())
aiRadioChannel.setMaxAccess(_J)
if mibBuilder.loadTexts:aiRadioChannel.setStatus(_B)
_AiRadioTransmitPower_Type=Integer32
_AiRadioTransmitPower_Object=MibTableColumn
aiRadioTransmitPower=_AiRadioTransmitPower_Object((1,3,6,1,4,1,14823,2,3,3,1,2,2,1,5),_AiRadioTransmitPower_Type())
aiRadioTransmitPower.setMaxAccess(_J)
if mibBuilder.loadTexts:aiRadioTransmitPower.setStatus(_B)
_AiRadioNoiseFloor_Type=Integer32
_AiRadioNoiseFloor_Object=MibTableColumn
aiRadioNoiseFloor=_AiRadioNoiseFloor_Object((1,3,6,1,4,1,14823,2,3,3,1,2,2,1,6),_AiRadioNoiseFloor_Type())
aiRadioNoiseFloor.setMaxAccess(_J)
if mibBuilder.loadTexts:aiRadioNoiseFloor.setStatus(_B)
_AiRadioUtilization4_Type=Integer32
_AiRadioUtilization4_Object=MibTableColumn
aiRadioUtilization4=_AiRadioUtilization4_Object((1,3,6,1,4,1,14823,2,3,3,1,2,2,1,7),_AiRadioUtilization4_Type())
aiRadioUtilization4.setMaxAccess(_J)
if mibBuilder.loadTexts:aiRadioUtilization4.setStatus(_B)
_AiRadioUtilization64_Type=Integer32
_AiRadioUtilization64_Object=MibTableColumn
aiRadioUtilization64=_AiRadioUtilization64_Object((1,3,6,1,4,1,14823,2,3,3,1,2,2,1,8),_AiRadioUtilization64_Type())
aiRadioUtilization64.setMaxAccess(_J)
if mibBuilder.loadTexts:aiRadioUtilization64.setStatus(_B)
_AiRadioTxTotalFrames_Type=Counter32
_AiRadioTxTotalFrames_Object=MibTableColumn
aiRadioTxTotalFrames=_AiRadioTxTotalFrames_Object((1,3,6,1,4,1,14823,2,3,3,1,2,2,1,9),_AiRadioTxTotalFrames_Type())
aiRadioTxTotalFrames.setMaxAccess(_J)
if mibBuilder.loadTexts:aiRadioTxTotalFrames.setStatus(_B)
_AiRadioTxMgmtFrames_Type=Counter32
_AiRadioTxMgmtFrames_Object=MibTableColumn
aiRadioTxMgmtFrames=_AiRadioTxMgmtFrames_Object((1,3,6,1,4,1,14823,2,3,3,1,2,2,1,10),_AiRadioTxMgmtFrames_Type())
aiRadioTxMgmtFrames.setMaxAccess(_J)
if mibBuilder.loadTexts:aiRadioTxMgmtFrames.setStatus(_B)
_AiRadioTxDataFrames_Type=Counter32
_AiRadioTxDataFrames_Object=MibTableColumn
aiRadioTxDataFrames=_AiRadioTxDataFrames_Object((1,3,6,1,4,1,14823,2,3,3,1,2,2,1,11),_AiRadioTxDataFrames_Type())
aiRadioTxDataFrames.setMaxAccess(_J)
if mibBuilder.loadTexts:aiRadioTxDataFrames.setStatus(_B)
_AiRadioTxDataBytes_Type=Counter32
_AiRadioTxDataBytes_Object=MibTableColumn
aiRadioTxDataBytes=_AiRadioTxDataBytes_Object((1,3,6,1,4,1,14823,2,3,3,1,2,2,1,12),_AiRadioTxDataBytes_Type())
aiRadioTxDataBytes.setMaxAccess(_J)
if mibBuilder.loadTexts:aiRadioTxDataBytes.setStatus(_B)
_AiRadioTxDrops_Type=Counter32
_AiRadioTxDrops_Object=MibTableColumn
aiRadioTxDrops=_AiRadioTxDrops_Object((1,3,6,1,4,1,14823,2,3,3,1,2,2,1,13),_AiRadioTxDrops_Type())
aiRadioTxDrops.setMaxAccess(_J)
if mibBuilder.loadTexts:aiRadioTxDrops.setStatus(_B)
_AiRadioRxTotalFrames_Type=Counter32
_AiRadioRxTotalFrames_Object=MibTableColumn
aiRadioRxTotalFrames=_AiRadioRxTotalFrames_Object((1,3,6,1,4,1,14823,2,3,3,1,2,2,1,14),_AiRadioRxTotalFrames_Type())
aiRadioRxTotalFrames.setMaxAccess(_J)
if mibBuilder.loadTexts:aiRadioRxTotalFrames.setStatus(_B)
_AiRadioRxDataFrames_Type=Counter32
_AiRadioRxDataFrames_Object=MibTableColumn
aiRadioRxDataFrames=_AiRadioRxDataFrames_Object((1,3,6,1,4,1,14823,2,3,3,1,2,2,1,15),_AiRadioRxDataFrames_Type())
aiRadioRxDataFrames.setMaxAccess(_J)
if mibBuilder.loadTexts:aiRadioRxDataFrames.setStatus(_B)
_AiRadioRxDataBytes_Type=Counter32
_AiRadioRxDataBytes_Object=MibTableColumn
aiRadioRxDataBytes=_AiRadioRxDataBytes_Object((1,3,6,1,4,1,14823,2,3,3,1,2,2,1,16),_AiRadioRxDataBytes_Type())
aiRadioRxDataBytes.setMaxAccess(_J)
if mibBuilder.loadTexts:aiRadioRxDataBytes.setStatus(_B)
_AiRadioRxMgmtFrames_Type=Counter32
_AiRadioRxMgmtFrames_Object=MibTableColumn
aiRadioRxMgmtFrames=_AiRadioRxMgmtFrames_Object((1,3,6,1,4,1,14823,2,3,3,1,2,2,1,17),_AiRadioRxMgmtFrames_Type())
aiRadioRxMgmtFrames.setMaxAccess(_J)
if mibBuilder.loadTexts:aiRadioRxMgmtFrames.setStatus(_B)
_AiRadioRxBad_Type=Counter32
_AiRadioRxBad_Object=MibTableColumn
aiRadioRxBad=_AiRadioRxBad_Object((1,3,6,1,4,1,14823,2,3,3,1,2,2,1,18),_AiRadioRxBad_Type())
aiRadioRxBad.setMaxAccess(_J)
if mibBuilder.loadTexts:aiRadioRxBad.setStatus(_B)
_AiRadioPhyEvents_Type=Counter32
_AiRadioPhyEvents_Object=MibTableColumn
aiRadioPhyEvents=_AiRadioPhyEvents_Object((1,3,6,1,4,1,14823,2,3,3,1,2,2,1,19),_AiRadioPhyEvents_Type())
aiRadioPhyEvents.setMaxAccess(_J)
if mibBuilder.loadTexts:aiRadioPhyEvents.setStatus(_B)
class _AiRadioStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_c,1),(_d,2)))
_AiRadioStatus_Type.__name__=_f
_AiRadioStatus_Object=MibTableColumn
aiRadioStatus=_AiRadioStatus_Object((1,3,6,1,4,1,14823,2,3,3,1,2,2,1,20),_AiRadioStatus_Type())
aiRadioStatus.setMaxAccess(_J)
if mibBuilder.loadTexts:aiRadioStatus.setStatus(_B)
_AiRadioClientNum_Type=Integer32
_AiRadioClientNum_Object=MibTableColumn
aiRadioClientNum=_AiRadioClientNum_Object((1,3,6,1,4,1,14823,2,3,3,1,2,2,1,21),_AiRadioClientNum_Type())
aiRadioClientNum.setMaxAccess(_J)
if mibBuilder.loadTexts:aiRadioClientNum.setStatus(_B)
_AiRadioMode_Type=DisplayString
_AiRadioMode_Object=MibTableColumn
aiRadioMode=_AiRadioMode_Object((1,3,6,1,4,1,14823,2,3,3,1,2,2,1,22),_AiRadioMode_Type())
aiRadioMode.setMaxAccess(_J)
if mibBuilder.loadTexts:aiRadioMode.setStatus(_B)
_AiWlanTable_Object=MibTable
aiWlanTable=_AiWlanTable_Object((1,3,6,1,4,1,14823,2,3,3,1,2,3))
if mibBuilder.loadTexts:aiWlanTable.setStatus(_B)
_AiWlanEntry_Object=MibTableRow
aiWlanEntry=_AiWlanEntry_Object((1,3,6,1,4,1,14823,2,3,3,1,2,3,1))
aiWlanEntry.setIndexNames((0,_A,_AR),(0,_A,_AS))
if mibBuilder.loadTexts:aiWlanEntry.setStatus(_B)
_AiWlanAPMACAddress_Type=MacAddress
_AiWlanAPMACAddress_Object=MibTableColumn
aiWlanAPMACAddress=_AiWlanAPMACAddress_Object((1,3,6,1,4,1,14823,2,3,3,1,2,3,1,1),_AiWlanAPMACAddress_Type())
aiWlanAPMACAddress.setMaxAccess(_J)
if mibBuilder.loadTexts:aiWlanAPMACAddress.setStatus(_B)
_AiWlanIndex_Type=Integer32
_AiWlanIndex_Object=MibTableColumn
aiWlanIndex=_AiWlanIndex_Object((1,3,6,1,4,1,14823,2,3,3,1,2,3,1,2),_AiWlanIndex_Type())
aiWlanIndex.setMaxAccess(_J)
if mibBuilder.loadTexts:aiWlanIndex.setStatus(_B)
_AiWlanESSID_Type=DisplayString
_AiWlanESSID_Object=MibTableColumn
aiWlanESSID=_AiWlanESSID_Object((1,3,6,1,4,1,14823,2,3,3,1,2,3,1,3),_AiWlanESSID_Type())
aiWlanESSID.setMaxAccess(_J)
if mibBuilder.loadTexts:aiWlanESSID.setStatus(_B)
_AiWlanMACAddress_Type=MacAddress
_AiWlanMACAddress_Object=MibTableColumn
aiWlanMACAddress=_AiWlanMACAddress_Object((1,3,6,1,4,1,14823,2,3,3,1,2,3,1,4),_AiWlanMACAddress_Type())
aiWlanMACAddress.setMaxAccess(_J)
if mibBuilder.loadTexts:aiWlanMACAddress.setStatus(_B)
_AiWlanTxTotalFrames_Type=Counter32
_AiWlanTxTotalFrames_Object=MibTableColumn
aiWlanTxTotalFrames=_AiWlanTxTotalFrames_Object((1,3,6,1,4,1,14823,2,3,3,1,2,3,1,5),_AiWlanTxTotalFrames_Type())
aiWlanTxTotalFrames.setMaxAccess(_J)
if mibBuilder.loadTexts:aiWlanTxTotalFrames.setStatus(_B)
_AiWlanTxDataFrames_Type=Counter32
_AiWlanTxDataFrames_Object=MibTableColumn
aiWlanTxDataFrames=_AiWlanTxDataFrames_Object((1,3,6,1,4,1,14823,2,3,3,1,2,3,1,6),_AiWlanTxDataFrames_Type())
aiWlanTxDataFrames.setMaxAccess(_J)
if mibBuilder.loadTexts:aiWlanTxDataFrames.setStatus(_B)
_AiWlanTxDataBytes_Type=Counter32
_AiWlanTxDataBytes_Object=MibTableColumn
aiWlanTxDataBytes=_AiWlanTxDataBytes_Object((1,3,6,1,4,1,14823,2,3,3,1,2,3,1,7),_AiWlanTxDataBytes_Type())
aiWlanTxDataBytes.setMaxAccess(_J)
if mibBuilder.loadTexts:aiWlanTxDataBytes.setStatus(_B)
_AiWlanRxTotalFrames_Type=Counter32
_AiWlanRxTotalFrames_Object=MibTableColumn
aiWlanRxTotalFrames=_AiWlanRxTotalFrames_Object((1,3,6,1,4,1,14823,2,3,3,1,2,3,1,8),_AiWlanRxTotalFrames_Type())
aiWlanRxTotalFrames.setMaxAccess(_J)
if mibBuilder.loadTexts:aiWlanRxTotalFrames.setStatus(_B)
_AiWlanRxDataFrames_Type=Counter32
_AiWlanRxDataFrames_Object=MibTableColumn
aiWlanRxDataFrames=_AiWlanRxDataFrames_Object((1,3,6,1,4,1,14823,2,3,3,1,2,3,1,9),_AiWlanRxDataFrames_Type())
aiWlanRxDataFrames.setMaxAccess(_J)
if mibBuilder.loadTexts:aiWlanRxDataFrames.setStatus(_B)
_AiWlanRxDataBytes_Type=Counter32
_AiWlanRxDataBytes_Object=MibTableColumn
aiWlanRxDataBytes=_AiWlanRxDataBytes_Object((1,3,6,1,4,1,14823,2,3,3,1,2,3,1,10),_AiWlanRxDataBytes_Type())
aiWlanRxDataBytes.setMaxAccess(_J)
if mibBuilder.loadTexts:aiWlanRxDataBytes.setStatus(_B)
_AiClientTable_Object=MibTable
aiClientTable=_AiClientTable_Object((1,3,6,1,4,1,14823,2,3,3,1,2,4))
if mibBuilder.loadTexts:aiClientTable.setStatus(_B)
_AiClientEntry_Object=MibTableRow
aiClientEntry=_AiClientEntry_Object((1,3,6,1,4,1,14823,2,3,3,1,2,4,1))
aiClientEntry.setIndexNames((0,_A,_AT))
if mibBuilder.loadTexts:aiClientEntry.setStatus(_B)
_AiClientMACAddress_Type=MacAddress
_AiClientMACAddress_Object=MibTableColumn
aiClientMACAddress=_AiClientMACAddress_Object((1,3,6,1,4,1,14823,2,3,3,1,2,4,1,1),_AiClientMACAddress_Type())
aiClientMACAddress.setMaxAccess(_J)
if mibBuilder.loadTexts:aiClientMACAddress.setStatus(_B)
_AiClientWlanMACAddress_Type=MacAddress
_AiClientWlanMACAddress_Object=MibTableColumn
aiClientWlanMACAddress=_AiClientWlanMACAddress_Object((1,3,6,1,4,1,14823,2,3,3,1,2,4,1,2),_AiClientWlanMACAddress_Type())
aiClientWlanMACAddress.setMaxAccess(_J)
if mibBuilder.loadTexts:aiClientWlanMACAddress.setStatus(_B)
_AiClientIPAddress_Type=IpAddress
_AiClientIPAddress_Object=MibTableColumn
aiClientIPAddress=_AiClientIPAddress_Object((1,3,6,1,4,1,14823,2,3,3,1,2,4,1,3),_AiClientIPAddress_Type())
aiClientIPAddress.setMaxAccess(_J)
if mibBuilder.loadTexts:aiClientIPAddress.setStatus(_B)
_AiClientAPIPAddress_Type=IpAddress
_AiClientAPIPAddress_Object=MibTableColumn
aiClientAPIPAddress=_AiClientAPIPAddress_Object((1,3,6,1,4,1,14823,2,3,3,1,2,4,1,4),_AiClientAPIPAddress_Type())
aiClientAPIPAddress.setMaxAccess(_J)
if mibBuilder.loadTexts:aiClientAPIPAddress.setStatus(_B)
_AiClientName_Type=DisplayString
_AiClientName_Object=MibTableColumn
aiClientName=_AiClientName_Object((1,3,6,1,4,1,14823,2,3,3,1,2,4,1,5),_AiClientName_Type())
aiClientName.setMaxAccess(_J)
if mibBuilder.loadTexts:aiClientName.setStatus(_B)
_AiClientOperatingSystem_Type=DisplayString
_AiClientOperatingSystem_Object=MibTableColumn
aiClientOperatingSystem=_AiClientOperatingSystem_Object((1,3,6,1,4,1,14823,2,3,3,1,2,4,1,6),_AiClientOperatingSystem_Type())
aiClientOperatingSystem.setMaxAccess(_J)
if mibBuilder.loadTexts:aiClientOperatingSystem.setStatus(_B)
_AiClientSNR_Type=Integer32
_AiClientSNR_Object=MibTableColumn
aiClientSNR=_AiClientSNR_Object((1,3,6,1,4,1,14823,2,3,3,1,2,4,1,7),_AiClientSNR_Type())
aiClientSNR.setMaxAccess(_J)
if mibBuilder.loadTexts:aiClientSNR.setStatus(_B)
_AiClientTxDataFrames_Type=Counter32
_AiClientTxDataFrames_Object=MibTableColumn
aiClientTxDataFrames=_AiClientTxDataFrames_Object((1,3,6,1,4,1,14823,2,3,3,1,2,4,1,8),_AiClientTxDataFrames_Type())
aiClientTxDataFrames.setMaxAccess(_J)
if mibBuilder.loadTexts:aiClientTxDataFrames.setStatus(_B)
_AiClientTxDataBytes_Type=Counter32
_AiClientTxDataBytes_Object=MibTableColumn
aiClientTxDataBytes=_AiClientTxDataBytes_Object((1,3,6,1,4,1,14823,2,3,3,1,2,4,1,9),_AiClientTxDataBytes_Type())
aiClientTxDataBytes.setMaxAccess(_J)
if mibBuilder.loadTexts:aiClientTxDataBytes.setStatus(_B)
_AiClientTxRetries_Type=Counter32
_AiClientTxRetries_Object=MibTableColumn
aiClientTxRetries=_AiClientTxRetries_Object((1,3,6,1,4,1,14823,2,3,3,1,2,4,1,10),_AiClientTxRetries_Type())
aiClientTxRetries.setMaxAccess(_J)
if mibBuilder.loadTexts:aiClientTxRetries.setStatus(_B)
_AiClientTxRate_Type=Integer32
_AiClientTxRate_Object=MibTableColumn
aiClientTxRate=_AiClientTxRate_Object((1,3,6,1,4,1,14823,2,3,3,1,2,4,1,11),_AiClientTxRate_Type())
aiClientTxRate.setMaxAccess(_J)
if mibBuilder.loadTexts:aiClientTxRate.setStatus(_B)
_AiClientRxDataFrames_Type=Counter32
_AiClientRxDataFrames_Object=MibTableColumn
aiClientRxDataFrames=_AiClientRxDataFrames_Object((1,3,6,1,4,1,14823,2,3,3,1,2,4,1,12),_AiClientRxDataFrames_Type())
aiClientRxDataFrames.setMaxAccess(_J)
if mibBuilder.loadTexts:aiClientRxDataFrames.setStatus(_B)
_AiClientRxDataBytes_Type=Counter32
_AiClientRxDataBytes_Object=MibTableColumn
aiClientRxDataBytes=_AiClientRxDataBytes_Object((1,3,6,1,4,1,14823,2,3,3,1,2,4,1,13),_AiClientRxDataBytes_Type())
aiClientRxDataBytes.setMaxAccess(_J)
if mibBuilder.loadTexts:aiClientRxDataBytes.setStatus(_B)
_AiClientRxRetries_Type=Counter32
_AiClientRxRetries_Object=MibTableColumn
aiClientRxRetries=_AiClientRxRetries_Object((1,3,6,1,4,1,14823,2,3,3,1,2,4,1,14),_AiClientRxRetries_Type())
aiClientRxRetries.setMaxAccess(_J)
if mibBuilder.loadTexts:aiClientRxRetries.setStatus(_B)
_AiClientRxRate_Type=Integer32
_AiClientRxRate_Object=MibTableColumn
aiClientRxRate=_AiClientRxRate_Object((1,3,6,1,4,1,14823,2,3,3,1,2,4,1,15),_AiClientRxRate_Type())
aiClientRxRate.setMaxAccess(_J)
if mibBuilder.loadTexts:aiClientRxRate.setStatus(_B)
_AiClientUptime_Type=TimeTicks
_AiClientUptime_Object=MibTableColumn
aiClientUptime=_AiClientUptime_Object((1,3,6,1,4,1,14823,2,3,3,1,2,4,1,16),_AiClientUptime_Type())
aiClientUptime.setMaxAccess(_J)
if mibBuilder.loadTexts:aiClientUptime.setStatus(_B)
_AiClientPhyType_Type=ArubaPhyType
_AiClientPhyType_Object=MibTableColumn
aiClientPhyType=_AiClientPhyType_Object((1,3,6,1,4,1,14823,2,3,3,1,2,4,1,17),_AiClientPhyType_Type())
aiClientPhyType.setMaxAccess(_J)
if mibBuilder.loadTexts:aiClientPhyType.setStatus(_B)
_AiClientHtMode_Type=ArubaHTMode
_AiClientHtMode_Object=MibTableColumn
aiClientHtMode=_AiClientHtMode_Object((1,3,6,1,4,1,14823,2,3,3,1,2,4,1,18),_AiClientHtMode_Type())
aiClientHtMode.setMaxAccess(_J)
if mibBuilder.loadTexts:aiClientHtMode.setStatus(_B)
_AiVoiceClientTable_Object=MibTable
aiVoiceClientTable=_AiVoiceClientTable_Object((1,3,6,1,4,1,14823,2,3,3,1,2,5))
if mibBuilder.loadTexts:aiVoiceClientTable.setStatus(_B)
_AiVoiceClientEntry_Object=MibTableRow
aiVoiceClientEntry=_AiVoiceClientEntry_Object((1,3,6,1,4,1,14823,2,3,3,1,2,5,1))
aiVoiceClientEntry.setIndexNames((0,_A,_AU))
if mibBuilder.loadTexts:aiVoiceClientEntry.setStatus(_B)
_AiClientMac_Type=MacAddress
_AiClientMac_Object=MibTableColumn
aiClientMac=_AiClientMac_Object((1,3,6,1,4,1,14823,2,3,3,1,2,5,1,1),_AiClientMac_Type())
aiClientMac.setMaxAccess(_J)
if mibBuilder.loadTexts:aiClientMac.setStatus(_B)
_AiClientIP_Type=IpAddress
_AiClientIP_Object=MibTableColumn
aiClientIP=_AiClientIP_Object((1,3,6,1,4,1,14823,2,3,3,1,2,5,1,2),_AiClientIP_Type())
aiClientIP.setMaxAccess(_J)
if mibBuilder.loadTexts:aiClientIP.setStatus(_B)
_AiClientAPMac_Type=MacAddress
_AiClientAPMac_Object=MibTableColumn
aiClientAPMac=_AiClientAPMac_Object((1,3,6,1,4,1,14823,2,3,3,1,2,5,1,3),_AiClientAPMac_Type())
aiClientAPMac.setMaxAccess(_J)
if mibBuilder.loadTexts:aiClientAPMac.setStatus(_B)
_AiClientAPName_Type=DisplayString
_AiClientAPName_Object=MibTableColumn
aiClientAPName=_AiClientAPName_Object((1,3,6,1,4,1,14823,2,3,3,1,2,5,1,4),_AiClientAPName_Type())
aiClientAPName.setMaxAccess(_J)
if mibBuilder.loadTexts:aiClientAPName.setStatus(_B)
_AiManagedInfoGroup_ObjectIdentity=ObjectIdentity
aiManagedInfoGroup=_AiManagedInfoGroup_ObjectIdentity((1,3,6,1,4,1,14823,2,3,3,1,3))
_AiManagedModeSinceLastSync_Type=DisplayString
_AiManagedModeSinceLastSync_Object=MibScalar
aiManagedModeSinceLastSync=_AiManagedModeSinceLastSync_Object((1,3,6,1,4,1,14823,2,3,3,1,3,1),_AiManagedModeSinceLastSync_Type())
aiManagedModeSinceLastSync.setMaxAccess(_J)
if mibBuilder.loadTexts:aiManagedModeSinceLastSync.setStatus(_B)
_AiTrapsGroup_ObjectIdentity=ObjectIdentity
aiTrapsGroup=_AiTrapsGroup_ObjectIdentity((1,3,6,1,4,1,14823,2,3,3,1,200))
_AiTrapObjectsGroup_ObjectIdentity=ObjectIdentity
aiTrapObjectsGroup=_AiTrapObjectsGroup_ObjectIdentity((1,3,6,1,4,1,14823,2,3,3,1,200,1))
_WlsxTrapAPMacAddress_Type=MacAddress
_WlsxTrapAPMacAddress_Object=MibScalar
wlsxTrapAPMacAddress=_WlsxTrapAPMacAddress_Object((1,3,6,1,4,1,14823,2,3,3,1,200,1,1),_WlsxTrapAPMacAddress_Type())
wlsxTrapAPMacAddress.setMaxAccess(_E)
if mibBuilder.loadTexts:wlsxTrapAPMacAddress.setStatus(_B)
_WlsxTrapAPIpAddress_Type=IpAddress
_WlsxTrapAPIpAddress_Object=MibScalar
wlsxTrapAPIpAddress=_WlsxTrapAPIpAddress_Object((1,3,6,1,4,1,14823,2,3,3,1,200,1,2),_WlsxTrapAPIpAddress_Type())
wlsxTrapAPIpAddress.setMaxAccess(_E)
if mibBuilder.loadTexts:wlsxTrapAPIpAddress.setStatus(_B)
_WlsxTrapAPBSSID_Type=MacAddress
_WlsxTrapAPBSSID_Object=MibScalar
wlsxTrapAPBSSID=_WlsxTrapAPBSSID_Object((1,3,6,1,4,1,14823,2,3,3,1,200,1,3),_WlsxTrapAPBSSID_Type())
wlsxTrapAPBSSID.setMaxAccess(_E)
if mibBuilder.loadTexts:wlsxTrapAPBSSID.setStatus(_B)
class _WlsxTrapEssid_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_WlsxTrapEssid_Type.__name__=_N
_WlsxTrapEssid_Object=MibScalar
wlsxTrapEssid=_WlsxTrapEssid_Object((1,3,6,1,4,1,14823,2,3,3,1,200,1,4),_WlsxTrapEssid_Type())
wlsxTrapEssid.setMaxAccess(_E)
if mibBuilder.loadTexts:wlsxTrapEssid.setStatus(_B)
_WlsxTrapTargetAPBSSID_Type=MacAddress
_WlsxTrapTargetAPBSSID_Object=MibScalar
wlsxTrapTargetAPBSSID=_WlsxTrapTargetAPBSSID_Object((1,3,6,1,4,1,14823,2,3,3,1,200,1,5),_WlsxTrapTargetAPBSSID_Type())
wlsxTrapTargetAPBSSID.setMaxAccess(_E)
if mibBuilder.loadTexts:wlsxTrapTargetAPBSSID.setStatus(_B)
class _WlsxTrapTargetAPSSID_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_WlsxTrapTargetAPSSID_Type.__name__=_N
_WlsxTrapTargetAPSSID_Object=MibScalar
wlsxTrapTargetAPSSID=_WlsxTrapTargetAPSSID_Object((1,3,6,1,4,1,14823,2,3,3,1,200,1,6),_WlsxTrapTargetAPSSID_Type())
wlsxTrapTargetAPSSID.setMaxAccess(_E)
if mibBuilder.loadTexts:wlsxTrapTargetAPSSID.setStatus(_B)
_WlsxTrapTargetAPChannel_Type=Integer32
_WlsxTrapTargetAPChannel_Object=MibScalar
wlsxTrapTargetAPChannel=_WlsxTrapTargetAPChannel_Object((1,3,6,1,4,1,14823,2,3,3,1,200,1,7),_WlsxTrapTargetAPChannel_Type())
wlsxTrapTargetAPChannel.setMaxAccess(_E)
if mibBuilder.loadTexts:wlsxTrapTargetAPChannel.setStatus(_B)
_WlsxTrapNodeMac_Type=MacAddress
_WlsxTrapNodeMac_Object=MibScalar
wlsxTrapNodeMac=_WlsxTrapNodeMac_Object((1,3,6,1,4,1,14823,2,3,3,1,200,1,8),_WlsxTrapNodeMac_Type())
wlsxTrapNodeMac.setMaxAccess(_E)
if mibBuilder.loadTexts:wlsxTrapNodeMac.setStatus(_B)
_WlsxTrapSourceMac_Type=MacAddress
_WlsxTrapSourceMac_Object=MibScalar
wlsxTrapSourceMac=_WlsxTrapSourceMac_Object((1,3,6,1,4,1,14823,2,3,3,1,200,1,9),_WlsxTrapSourceMac_Type())
wlsxTrapSourceMac.setMaxAccess(_E)
if mibBuilder.loadTexts:wlsxTrapSourceMac.setStatus(_B)
_WlsxReceiverMac_Type=MacAddress
_WlsxReceiverMac_Object=MibScalar
wlsxReceiverMac=_WlsxReceiverMac_Object((1,3,6,1,4,1,14823,2,3,3,1,200,1,10),_WlsxReceiverMac_Type())
wlsxReceiverMac.setMaxAccess(_E)
if mibBuilder.loadTexts:wlsxReceiverMac.setStatus(_B)
_WlsxTrapTransmitterMac_Type=MacAddress
_WlsxTrapTransmitterMac_Object=MibScalar
wlsxTrapTransmitterMac=_WlsxTrapTransmitterMac_Object((1,3,6,1,4,1,14823,2,3,3,1,200,1,11),_WlsxTrapTransmitterMac_Type())
wlsxTrapTransmitterMac.setMaxAccess(_E)
if mibBuilder.loadTexts:wlsxTrapTransmitterMac.setStatus(_B)
_WlsxTrapReceiverMac_Type=MacAddress
_WlsxTrapReceiverMac_Object=MibScalar
wlsxTrapReceiverMac=_WlsxTrapReceiverMac_Object((1,3,6,1,4,1,14823,2,3,3,1,200,1,12),_WlsxTrapReceiverMac_Type())
wlsxTrapReceiverMac.setMaxAccess(_E)
if mibBuilder.loadTexts:wlsxTrapReceiverMac.setStatus(_B)
_WlsxTrapSnr_Type=Integer32
_WlsxTrapSnr_Object=MibScalar
wlsxTrapSnr=_WlsxTrapSnr_Object((1,3,6,1,4,1,14823,2,3,3,1,200,1,13),_WlsxTrapSnr_Type())
wlsxTrapSnr.setMaxAccess(_E)
if mibBuilder.loadTexts:wlsxTrapSnr.setStatus(_B)
class _WlsxTrapSignatureName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_WlsxTrapSignatureName_Type.__name__=_N
_WlsxTrapSignatureName_Object=MibScalar
wlsxTrapSignatureName=_WlsxTrapSignatureName_Object((1,3,6,1,4,1,14823,2,3,3,1,200,1,14),_WlsxTrapSignatureName_Type())
wlsxTrapSignatureName.setMaxAccess(_E)
if mibBuilder.loadTexts:wlsxTrapSignatureName.setStatus(_B)
_WlsxTrapFrameType_Type=ArubaFrameType
_WlsxTrapFrameType_Object=MibScalar
wlsxTrapFrameType=_WlsxTrapFrameType_Object((1,3,6,1,4,1,14823,2,3,3,1,200,1,15),_WlsxTrapFrameType_Type())
wlsxTrapFrameType.setMaxAccess(_E)
if mibBuilder.loadTexts:wlsxTrapFrameType.setStatus(_B)
_WlsxTrapAddressType_Type=ArubaAddressType
_WlsxTrapAddressType_Object=MibScalar
wlsxTrapAddressType=_WlsxTrapAddressType_Object((1,3,6,1,4,1,14823,2,3,3,1,200,1,16),_WlsxTrapAddressType_Type())
wlsxTrapAddressType.setMaxAccess(_E)
if mibBuilder.loadTexts:wlsxTrapAddressType.setStatus(_B)
class _WlsxTrapAPLocation_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_WlsxTrapAPLocation_Type.__name__=_N
_WlsxTrapAPLocation_Object=MibScalar
wlsxTrapAPLocation=_WlsxTrapAPLocation_Object((1,3,6,1,4,1,14823,2,3,3,1,200,1,17),_WlsxTrapAPLocation_Type())
wlsxTrapAPLocation.setMaxAccess(_E)
if mibBuilder.loadTexts:wlsxTrapAPLocation.setStatus(_B)
_WlsxTrapAPChannel_Type=Integer32
_WlsxTrapAPChannel_Object=MibScalar
wlsxTrapAPChannel=_WlsxTrapAPChannel_Object((1,3,6,1,4,1,14823,2,3,3,1,200,1,18),_WlsxTrapAPChannel_Type())
wlsxTrapAPChannel.setMaxAccess(_E)
if mibBuilder.loadTexts:wlsxTrapAPChannel.setStatus(_B)
_WlsxTrapAPTxPower_Type=Integer32
_WlsxTrapAPTxPower_Object=MibScalar
wlsxTrapAPTxPower=_WlsxTrapAPTxPower_Object((1,3,6,1,4,1,14823,2,3,3,1,200,1,19),_WlsxTrapAPTxPower_Type())
wlsxTrapAPTxPower.setMaxAccess(_E)
if mibBuilder.loadTexts:wlsxTrapAPTxPower.setStatus(_B)
_WlsxTrapMatchedMac_Type=MacAddress
_WlsxTrapMatchedMac_Object=MibScalar
wlsxTrapMatchedMac=_WlsxTrapMatchedMac_Object((1,3,6,1,4,1,14823,2,3,3,1,200,1,20),_WlsxTrapMatchedMac_Type())
wlsxTrapMatchedMac.setMaxAccess(_E)
if mibBuilder.loadTexts:wlsxTrapMatchedMac.setStatus(_B)
_WlsxTrapMatchedIp_Type=IpAddress
_WlsxTrapMatchedIp_Object=MibScalar
wlsxTrapMatchedIp=_WlsxTrapMatchedIp_Object((1,3,6,1,4,1,14823,2,3,3,1,200,1,21),_WlsxTrapMatchedIp_Type())
wlsxTrapMatchedIp.setMaxAccess(_E)
if mibBuilder.loadTexts:wlsxTrapMatchedIp.setStatus(_B)
class _WlsxTrapRogueIfoURL_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_WlsxTrapRogueIfoURL_Type.__name__=_N
_WlsxTrapRogueIfoURL_Object=MibScalar
wlsxTrapRogueIfoURL=_WlsxTrapRogueIfoURL_Object((1,3,6,1,4,1,14823,2,3,3,1,200,1,22),_WlsxTrapRogueIfoURL_Type())
wlsxTrapRogueIfoURL.setMaxAccess(_E)
if mibBuilder.loadTexts:wlsxTrapRogueIfoURL.setStatus(_B)
_WlsxTrapVlanId_Type=Integer32
_WlsxTrapVlanId_Object=MibScalar
wlsxTrapVlanId=_WlsxTrapVlanId_Object((1,3,6,1,4,1,14823,2,3,3,1,200,1,23),_WlsxTrapVlanId_Type())
wlsxTrapVlanId.setMaxAccess(_E)
if mibBuilder.loadTexts:wlsxTrapVlanId.setStatus(_B)
_WlsxTrapAdminStatus_Type=ArubaEnableValue
_WlsxTrapAdminStatus_Object=MibScalar
wlsxTrapAdminStatus=_WlsxTrapAdminStatus_Object((1,3,6,1,4,1,14823,2,3,3,1,200,1,24),_WlsxTrapAdminStatus_Type())
wlsxTrapAdminStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:wlsxTrapAdminStatus.setStatus(_B)
_WlsxTrapOperStatus_Type=ArubaOperStateValue
_WlsxTrapOperStatus_Object=MibScalar
wlsxTrapOperStatus=_WlsxTrapOperStatus_Object((1,3,6,1,4,1,14823,2,3,3,1,200,1,25),_WlsxTrapOperStatus_Type())
wlsxTrapOperStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:wlsxTrapOperStatus.setStatus(_B)
class _WlsxTrapAuthServerName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_WlsxTrapAuthServerName_Type.__name__=_N
_WlsxTrapAuthServerName_Object=MibScalar
wlsxTrapAuthServerName=_WlsxTrapAuthServerName_Object((1,3,6,1,4,1,14823,2,3,3,1,200,1,26),_WlsxTrapAuthServerName_Type())
wlsxTrapAuthServerName.setMaxAccess(_E)
if mibBuilder.loadTexts:wlsxTrapAuthServerName.setStatus(_B)
_WlsxTrapAuthServerTimeout_Type=Integer32
_WlsxTrapAuthServerTimeout_Object=MibScalar
wlsxTrapAuthServerTimeout=_WlsxTrapAuthServerTimeout_Object((1,3,6,1,4,1,14823,2,3,3,1,200,1,27),_WlsxTrapAuthServerTimeout_Type())
wlsxTrapAuthServerTimeout.setMaxAccess(_E)
if mibBuilder.loadTexts:wlsxTrapAuthServerTimeout.setStatus(_B)
_WlsxTrapCardSlot_Type=Integer32
_WlsxTrapCardSlot_Object=MibScalar
wlsxTrapCardSlot=_WlsxTrapCardSlot_Object((1,3,6,1,4,1,14823,2,3,3,1,200,1,28),_WlsxTrapCardSlot_Type())
wlsxTrapCardSlot.setMaxAccess(_E)
if mibBuilder.loadTexts:wlsxTrapCardSlot.setStatus(_B)
class _WlsxTrapTemperatureValue_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_WlsxTrapTemperatureValue_Type.__name__=_N
_WlsxTrapTemperatureValue_Object=MibScalar
wlsxTrapTemperatureValue=_WlsxTrapTemperatureValue_Object((1,3,6,1,4,1,14823,2,3,3,1,200,1,29),_WlsxTrapTemperatureValue_Type())
wlsxTrapTemperatureValue.setMaxAccess(_E)
if mibBuilder.loadTexts:wlsxTrapTemperatureValue.setStatus(_B)
class _WlsxTrapProcessName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_WlsxTrapProcessName_Type.__name__=_N
_WlsxTrapProcessName_Object=MibScalar
wlsxTrapProcessName=_WlsxTrapProcessName_Object((1,3,6,1,4,1,14823,2,3,3,1,200,1,30),_WlsxTrapProcessName_Type())
wlsxTrapProcessName.setMaxAccess(_E)
if mibBuilder.loadTexts:wlsxTrapProcessName.setStatus(_B)
_WlsxTrapFanNumber_Type=Integer32
_WlsxTrapFanNumber_Object=MibScalar
wlsxTrapFanNumber=_WlsxTrapFanNumber_Object((1,3,6,1,4,1,14823,2,3,3,1,200,1,31),_WlsxTrapFanNumber_Type())
wlsxTrapFanNumber.setMaxAccess(_E)
if mibBuilder.loadTexts:wlsxTrapFanNumber.setStatus(_B)
class _WlsxTrapVoltageType_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_WlsxTrapVoltageType_Type.__name__=_N
_WlsxTrapVoltageType_Object=MibScalar
wlsxTrapVoltageType=_WlsxTrapVoltageType_Object((1,3,6,1,4,1,14823,2,3,3,1,200,1,32),_WlsxTrapVoltageType_Type())
wlsxTrapVoltageType.setMaxAccess(_E)
if mibBuilder.loadTexts:wlsxTrapVoltageType.setStatus(_B)
class _WlsxTrapVoltageValue_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_WlsxTrapVoltageValue_Type.__name__=_N
_WlsxTrapVoltageValue_Object=MibScalar
wlsxTrapVoltageValue=_WlsxTrapVoltageValue_Object((1,3,6,1,4,1,14823,2,3,3,1,200,1,33),_WlsxTrapVoltageValue_Type())
wlsxTrapVoltageValue.setMaxAccess(_E)
if mibBuilder.loadTexts:wlsxTrapVoltageValue.setStatus(_B)
_WlsxTrapStationBlackListReason_Type=ArubaBlackListReason
_WlsxTrapStationBlackListReason_Object=MibScalar
wlsxTrapStationBlackListReason=_WlsxTrapStationBlackListReason_Object((1,3,6,1,4,1,14823,2,3,3,1,200,1,34),_WlsxTrapStationBlackListReason_Type())
wlsxTrapStationBlackListReason.setMaxAccess(_E)
if mibBuilder.loadTexts:wlsxTrapStationBlackListReason.setStatus(_U)
_WlsxTrapSpoofedIpAddress_Type=IpAddress
_WlsxTrapSpoofedIpAddress_Object=MibScalar
wlsxTrapSpoofedIpAddress=_WlsxTrapSpoofedIpAddress_Object((1,3,6,1,4,1,14823,2,3,3,1,200,1,35),_WlsxTrapSpoofedIpAddress_Type())
wlsxTrapSpoofedIpAddress.setMaxAccess(_E)
if mibBuilder.loadTexts:wlsxTrapSpoofedIpAddress.setStatus(_B)
_WlsxTrapSpoofedOldPhyAddress_Type=MacAddress
_WlsxTrapSpoofedOldPhyAddress_Object=MibScalar
wlsxTrapSpoofedOldPhyAddress=_WlsxTrapSpoofedOldPhyAddress_Object((1,3,6,1,4,1,14823,2,3,3,1,200,1,36),_WlsxTrapSpoofedOldPhyAddress_Type())
wlsxTrapSpoofedOldPhyAddress.setMaxAccess(_E)
if mibBuilder.loadTexts:wlsxTrapSpoofedOldPhyAddress.setStatus(_B)
_WlsxTrapSpoofedNewPhyAddress_Type=MacAddress
_WlsxTrapSpoofedNewPhyAddress_Object=MibScalar
wlsxTrapSpoofedNewPhyAddress=_WlsxTrapSpoofedNewPhyAddress_Object((1,3,6,1,4,1,14823,2,3,3,1,200,1,37),_WlsxTrapSpoofedNewPhyAddress_Type())
wlsxTrapSpoofedNewPhyAddress.setMaxAccess(_E)
if mibBuilder.loadTexts:wlsxTrapSpoofedNewPhyAddress.setStatus(_B)
class _WlsxTrapDBName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_WlsxTrapDBName_Type.__name__=_N
_WlsxTrapDBName_Object=MibScalar
wlsxTrapDBName=_WlsxTrapDBName_Object((1,3,6,1,4,1,14823,2,3,3,1,200,1,38),_WlsxTrapDBName_Type())
wlsxTrapDBName.setMaxAccess(_E)
if mibBuilder.loadTexts:wlsxTrapDBName.setStatus(_B)
class _WlsxTrapDBUserName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_WlsxTrapDBUserName_Type.__name__=_N
_WlsxTrapDBUserName_Object=MibScalar
wlsxTrapDBUserName=_WlsxTrapDBUserName_Object((1,3,6,1,4,1,14823,2,3,3,1,200,1,39),_WlsxTrapDBUserName_Type())
wlsxTrapDBUserName.setMaxAccess(_E)
if mibBuilder.loadTexts:wlsxTrapDBUserName.setStatus(_B)
class _WlsxTrapDBIpAddress_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_WlsxTrapDBIpAddress_Type.__name__=_N
_WlsxTrapDBIpAddress_Object=MibScalar
wlsxTrapDBIpAddress=_WlsxTrapDBIpAddress_Object((1,3,6,1,4,1,14823,2,3,3,1,200,1,40),_WlsxTrapDBIpAddress_Type())
wlsxTrapDBIpAddress.setMaxAccess(_E)
if mibBuilder.loadTexts:wlsxTrapDBIpAddress.setStatus(_B)
_WlsxTrapDBType_Type=ArubaDBType
_WlsxTrapDBType_Object=MibScalar
wlsxTrapDBType=_WlsxTrapDBType_Object((1,3,6,1,4,1,14823,2,3,3,1,200,1,41),_WlsxTrapDBType_Type())
wlsxTrapDBType.setMaxAccess(_E)
if mibBuilder.loadTexts:wlsxTrapDBType.setStatus(_B)
_WlsxTrapVrrpID_Type=Integer32
_WlsxTrapVrrpID_Object=MibScalar
wlsxTrapVrrpID=_WlsxTrapVrrpID_Object((1,3,6,1,4,1,14823,2,3,3,1,200,1,42),_WlsxTrapVrrpID_Type())
wlsxTrapVrrpID.setMaxAccess(_E)
if mibBuilder.loadTexts:wlsxTrapVrrpID.setStatus(_B)
_WlsxTrapVrrpMasterIp_Type=IpAddress
_WlsxTrapVrrpMasterIp_Object=MibScalar
wlsxTrapVrrpMasterIp=_WlsxTrapVrrpMasterIp_Object((1,3,6,1,4,1,14823,2,3,3,1,200,1,43),_WlsxTrapVrrpMasterIp_Type())
wlsxTrapVrrpMasterIp.setMaxAccess(_E)
if mibBuilder.loadTexts:wlsxTrapVrrpMasterIp.setStatus(_B)
_WlsxTrapVrrpOperState_Type=ArubaVrrpState
_WlsxTrapVrrpOperState_Object=MibScalar
wlsxTrapVrrpOperState=_WlsxTrapVrrpOperState_Object((1,3,6,1,4,1,14823,2,3,3,1,200,1,44),_WlsxTrapVrrpOperState_Type())
wlsxTrapVrrpOperState.setMaxAccess(_E)
if mibBuilder.loadTexts:wlsxTrapVrrpOperState.setStatus(_B)
class _WlsxTrapESIServerGrpName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_WlsxTrapESIServerGrpName_Type.__name__=_N
_WlsxTrapESIServerGrpName_Object=MibScalar
wlsxTrapESIServerGrpName=_WlsxTrapESIServerGrpName_Object((1,3,6,1,4,1,14823,2,3,3,1,200,1,45),_WlsxTrapESIServerGrpName_Type())
wlsxTrapESIServerGrpName.setMaxAccess(_E)
if mibBuilder.loadTexts:wlsxTrapESIServerGrpName.setStatus(_B)
class _WlsxTrapESIServerName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_WlsxTrapESIServerName_Type.__name__=_N
_WlsxTrapESIServerName_Object=MibScalar
wlsxTrapESIServerName=_WlsxTrapESIServerName_Object((1,3,6,1,4,1,14823,2,3,3,1,200,1,46),_WlsxTrapESIServerName_Type())
wlsxTrapESIServerName.setMaxAccess(_E)
if mibBuilder.loadTexts:wlsxTrapESIServerName.setStatus(_B)
_WlsxTrapESIServerIpAddress_Type=IpAddress
_WlsxTrapESIServerIpAddress_Object=MibScalar
wlsxTrapESIServerIpAddress=_WlsxTrapESIServerIpAddress_Object((1,3,6,1,4,1,14823,2,3,3,1,200,1,47),_WlsxTrapESIServerIpAddress_Type())
wlsxTrapESIServerIpAddress.setMaxAccess(_E)
if mibBuilder.loadTexts:wlsxTrapESIServerIpAddress.setStatus(_B)
_WlsxTrapLicenseDaysRemaining_Type=Integer32
_WlsxTrapLicenseDaysRemaining_Object=MibScalar
wlsxTrapLicenseDaysRemaining=_WlsxTrapLicenseDaysRemaining_Object((1,3,6,1,4,1,14823,2,3,3,1,200,1,48),_WlsxTrapLicenseDaysRemaining_Type())
wlsxTrapLicenseDaysRemaining.setMaxAccess(_E)
if mibBuilder.loadTexts:wlsxTrapLicenseDaysRemaining.setStatus(_B)
_WlsxTrapSwitchIp_Type=IpAddress
_WlsxTrapSwitchIp_Object=MibScalar
wlsxTrapSwitchIp=_WlsxTrapSwitchIp_Object((1,3,6,1,4,1,14823,2,3,3,1,200,1,49),_WlsxTrapSwitchIp_Type())
wlsxTrapSwitchIp.setMaxAccess(_E)
if mibBuilder.loadTexts:wlsxTrapSwitchIp.setStatus(_B)
_WlsxTrapSwitchRole_Type=ArubaSwitchRole
_WlsxTrapSwitchRole_Object=MibScalar
wlsxTrapSwitchRole=_WlsxTrapSwitchRole_Object((1,3,6,1,4,1,14823,2,3,3,1,200,1,50),_WlsxTrapSwitchRole_Type())
wlsxTrapSwitchRole.setMaxAccess(_E)
if mibBuilder.loadTexts:wlsxTrapSwitchRole.setStatus(_B)
_WlsxTrapUserIpAddress_Type=IpAddress
_WlsxTrapUserIpAddress_Object=MibScalar
wlsxTrapUserIpAddress=_WlsxTrapUserIpAddress_Object((1,3,6,1,4,1,14823,2,3,3,1,200,1,51),_WlsxTrapUserIpAddress_Type())
wlsxTrapUserIpAddress.setMaxAccess(_E)
if mibBuilder.loadTexts:wlsxTrapUserIpAddress.setStatus(_B)
_WlsxTrapUserPhyAddress_Type=MacAddress
_WlsxTrapUserPhyAddress_Object=MibScalar
wlsxTrapUserPhyAddress=_WlsxTrapUserPhyAddress_Object((1,3,6,1,4,1,14823,2,3,3,1,200,1,52),_WlsxTrapUserPhyAddress_Type())
wlsxTrapUserPhyAddress.setMaxAccess(_E)
if mibBuilder.loadTexts:wlsxTrapUserPhyAddress.setStatus(_B)
class _WlsxTrapUserName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_WlsxTrapUserName_Type.__name__=_N
_WlsxTrapUserName_Object=MibScalar
wlsxTrapUserName=_WlsxTrapUserName_Object((1,3,6,1,4,1,14823,2,3,3,1,200,1,53),_WlsxTrapUserName_Type())
wlsxTrapUserName.setMaxAccess(_E)
if mibBuilder.loadTexts:wlsxTrapUserName.setStatus(_B)
class _WlsxTrapUserRole_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_WlsxTrapUserRole_Type.__name__=_N
_WlsxTrapUserRole_Object=MibScalar
wlsxTrapUserRole=_WlsxTrapUserRole_Object((1,3,6,1,4,1,14823,2,3,3,1,200,1,54),_WlsxTrapUserRole_Type())
wlsxTrapUserRole.setMaxAccess(_E)
if mibBuilder.loadTexts:wlsxTrapUserRole.setStatus(_B)
_WlsxTrapUserAuthenticationMethod_Type=ArubaAuthenticationMethods
_WlsxTrapUserAuthenticationMethod_Object=MibScalar
wlsxTrapUserAuthenticationMethod=_WlsxTrapUserAuthenticationMethod_Object((1,3,6,1,4,1,14823,2,3,3,1,200,1,55),_WlsxTrapUserAuthenticationMethod_Type())
wlsxTrapUserAuthenticationMethod.setMaxAccess(_E)
if mibBuilder.loadTexts:wlsxTrapUserAuthenticationMethod.setStatus(_B)
_WlsxTrapAPRadioNumber_Type=Integer32
_WlsxTrapAPRadioNumber_Object=MibScalar
wlsxTrapAPRadioNumber=_WlsxTrapAPRadioNumber_Object((1,3,6,1,4,1,14823,2,3,3,1,200,1,56),_WlsxTrapAPRadioNumber_Type())
wlsxTrapAPRadioNumber.setMaxAccess(_E)
if mibBuilder.loadTexts:wlsxTrapAPRadioNumber.setStatus(_B)
class _WlsxTrapRogueInfoURL_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_WlsxTrapRogueInfoURL_Type.__name__=_N
_WlsxTrapRogueInfoURL_Object=MibScalar
wlsxTrapRogueInfoURL=_WlsxTrapRogueInfoURL_Object((1,3,6,1,4,1,14823,2,3,3,1,200,1,57),_WlsxTrapRogueInfoURL_Type())
wlsxTrapRogueInfoURL.setMaxAccess(_E)
if mibBuilder.loadTexts:wlsxTrapRogueInfoURL.setStatus(_B)
class _WlsxTrapInterferingAPInfoURL_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_WlsxTrapInterferingAPInfoURL_Type.__name__=_N
_WlsxTrapInterferingAPInfoURL_Object=MibScalar
wlsxTrapInterferingAPInfoURL=_WlsxTrapInterferingAPInfoURL_Object((1,3,6,1,4,1,14823,2,3,3,1,200,1,58),_WlsxTrapInterferingAPInfoURL_Type())
wlsxTrapInterferingAPInfoURL.setMaxAccess(_E)
if mibBuilder.loadTexts:wlsxTrapInterferingAPInfoURL.setStatus(_B)
_WlsxTrapPortNumber_Type=Integer32
_WlsxTrapPortNumber_Object=MibScalar
wlsxTrapPortNumber=_WlsxTrapPortNumber_Object((1,3,6,1,4,1,14823,2,3,3,1,200,1,59),_WlsxTrapPortNumber_Type())
wlsxTrapPortNumber.setMaxAccess(_E)
if mibBuilder.loadTexts:wlsxTrapPortNumber.setStatus(_B)
_WlsxTrapTime_Type=DateAndTime
_WlsxTrapTime_Object=MibScalar
wlsxTrapTime=_WlsxTrapTime_Object((1,3,6,1,4,1,14823,2,3,3,1,200,1,60),_WlsxTrapTime_Type())
wlsxTrapTime.setMaxAccess(_E)
if mibBuilder.loadTexts:wlsxTrapTime.setStatus(_B)
_WlsxTrapHostIp_Type=IpAddress
_WlsxTrapHostIp_Object=MibScalar
wlsxTrapHostIp=_WlsxTrapHostIp_Object((1,3,6,1,4,1,14823,2,3,3,1,200,1,61),_WlsxTrapHostIp_Type())
wlsxTrapHostIp.setMaxAccess(_E)
if mibBuilder.loadTexts:wlsxTrapHostIp.setStatus(_B)
_WlsxTrapHostPort_Type=Integer32
_WlsxTrapHostPort_Object=MibScalar
wlsxTrapHostPort=_WlsxTrapHostPort_Object((1,3,6,1,4,1,14823,2,3,3,1,200,1,62),_WlsxTrapHostPort_Type())
wlsxTrapHostPort.setMaxAccess(_E)
if mibBuilder.loadTexts:wlsxTrapHostPort.setStatus(_B)
_WlsxTrapConfigurationId_Type=Integer32
_WlsxTrapConfigurationId_Object=MibScalar
wlsxTrapConfigurationId=_WlsxTrapConfigurationId_Object((1,3,6,1,4,1,14823,2,3,3,1,200,1,63),_WlsxTrapConfigurationId_Type())
wlsxTrapConfigurationId.setMaxAccess(_E)
if mibBuilder.loadTexts:wlsxTrapConfigurationId.setStatus(_B)
class _WlsxTrapCTSURL_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_WlsxTrapCTSURL_Type.__name__=_N
_WlsxTrapCTSURL_Object=MibScalar
wlsxTrapCTSURL=_WlsxTrapCTSURL_Object((1,3,6,1,4,1,14823,2,3,3,1,200,1,64),_WlsxTrapCTSURL_Type())
wlsxTrapCTSURL.setMaxAccess(_E)
if mibBuilder.loadTexts:wlsxTrapCTSURL.setStatus(_B)
class _WlsxTrapCTSTransferType_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_WlsxTrapCTSTransferType_Type.__name__=_N
_WlsxTrapCTSTransferType_Object=MibScalar
wlsxTrapCTSTransferType=_WlsxTrapCTSTransferType_Object((1,3,6,1,4,1,14823,2,3,3,1,200,1,65),_WlsxTrapCTSTransferType_Type())
wlsxTrapCTSTransferType.setMaxAccess(_E)
if mibBuilder.loadTexts:wlsxTrapCTSTransferType.setStatus(_B)
_WlsxTrapConfigurationState_Type=ArubaConfigurationState
_WlsxTrapConfigurationState_Object=MibScalar
wlsxTrapConfigurationState=_WlsxTrapConfigurationState_Object((1,3,6,1,4,1,14823,2,3,3,1,200,1,66),_WlsxTrapConfigurationState_Type())
wlsxTrapConfigurationState.setMaxAccess(_E)
if mibBuilder.loadTexts:wlsxTrapConfigurationState.setStatus(_B)
class _WlsxTrapUpdateFailureReason_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_WlsxTrapUpdateFailureReason_Type.__name__=_N
_WlsxTrapUpdateFailureReason_Object=MibScalar
wlsxTrapUpdateFailureReason=_WlsxTrapUpdateFailureReason_Object((1,3,6,1,4,1,14823,2,3,3,1,200,1,67),_WlsxTrapUpdateFailureReason_Type())
wlsxTrapUpdateFailureReason.setMaxAccess(_E)
if mibBuilder.loadTexts:wlsxTrapUpdateFailureReason.setStatus(_B)
class _WlsxTrapUpdateFailedObj_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_WlsxTrapUpdateFailedObj_Type.__name__=_N
_WlsxTrapUpdateFailedObj_Object=MibScalar
wlsxTrapUpdateFailedObj=_WlsxTrapUpdateFailedObj_Object((1,3,6,1,4,1,14823,2,3,3,1,200,1,68),_WlsxTrapUpdateFailedObj_Type())
wlsxTrapUpdateFailedObj.setMaxAccess(_E)
if mibBuilder.loadTexts:wlsxTrapUpdateFailedObj.setStatus(_B)
_WlsxTrapTableEntryChangeType_Type=ArubaConfigurationChangeType
_WlsxTrapTableEntryChangeType_Object=MibScalar
wlsxTrapTableEntryChangeType=_WlsxTrapTableEntryChangeType_Object((1,3,6,1,4,1,14823,2,3,3,1,200,1,69),_WlsxTrapTableEntryChangeType_Type())
wlsxTrapTableEntryChangeType.setMaxAccess(_E)
if mibBuilder.loadTexts:wlsxTrapTableEntryChangeType.setStatus(_B)
class _WlsxTrapGlobalConfigObj_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_WlsxTrapGlobalConfigObj_Type.__name__=_N
_WlsxTrapGlobalConfigObj_Object=MibScalar
wlsxTrapGlobalConfigObj=_WlsxTrapGlobalConfigObj_Object((1,3,6,1,4,1,14823,2,3,3,1,200,1,70),_WlsxTrapGlobalConfigObj_Type())
wlsxTrapGlobalConfigObj.setMaxAccess(_E)
if mibBuilder.loadTexts:wlsxTrapGlobalConfigObj.setStatus(_B)
_WlsxTrapTableGenNumber_Type=Integer32
_WlsxTrapTableGenNumber_Object=MibScalar
wlsxTrapTableGenNumber=_WlsxTrapTableGenNumber_Object((1,3,6,1,4,1,14823,2,3,3,1,200,1,71),_WlsxTrapTableGenNumber_Type())
wlsxTrapTableGenNumber.setMaxAccess(_E)
if mibBuilder.loadTexts:wlsxTrapTableGenNumber.setStatus(_B)
_WlsxTrapLicenseId_Type=Integer32
_WlsxTrapLicenseId_Object=MibScalar
wlsxTrapLicenseId=_WlsxTrapLicenseId_Object((1,3,6,1,4,1,14823,2,3,3,1,200,1,72),_WlsxTrapLicenseId_Type())
wlsxTrapLicenseId.setMaxAccess(_E)
if mibBuilder.loadTexts:wlsxTrapLicenseId.setStatus(_B)
_WlsxTrapConfidenceLevel_Type=Integer32
_WlsxTrapConfidenceLevel_Object=MibScalar
wlsxTrapConfidenceLevel=_WlsxTrapConfidenceLevel_Object((1,3,6,1,4,1,14823,2,3,3,1,200,1,73),_WlsxTrapConfidenceLevel_Type())
wlsxTrapConfidenceLevel.setMaxAccess(_E)
if mibBuilder.loadTexts:wlsxTrapConfidenceLevel.setStatus(_B)
class _WlsxTrapMissingLicenses_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_WlsxTrapMissingLicenses_Type.__name__=_N
_WlsxTrapMissingLicenses_Object=MibScalar
wlsxTrapMissingLicenses=_WlsxTrapMissingLicenses_Object((1,3,6,1,4,1,14823,2,3,3,1,200,1,74),_WlsxTrapMissingLicenses_Type())
wlsxTrapMissingLicenses.setMaxAccess(_E)
if mibBuilder.loadTexts:wlsxTrapMissingLicenses.setStatus(_B)
_WlsxVoiceCurrentNumCdr_Type=Integer32
_WlsxVoiceCurrentNumCdr_Object=MibScalar
wlsxVoiceCurrentNumCdr=_WlsxVoiceCurrentNumCdr_Object((1,3,6,1,4,1,14823,2,3,3,1,200,1,75),_WlsxVoiceCurrentNumCdr_Type())
wlsxVoiceCurrentNumCdr.setMaxAccess(_E)
if mibBuilder.loadTexts:wlsxVoiceCurrentNumCdr.setStatus(_B)
_WlsxTrapTunnelId_Type=Integer32
_WlsxTrapTunnelId_Object=MibScalar
wlsxTrapTunnelId=_WlsxTrapTunnelId_Object((1,3,6,1,4,1,14823,2,3,3,1,200,1,76),_WlsxTrapTunnelId_Type())
wlsxTrapTunnelId.setMaxAccess(_E)
if mibBuilder.loadTexts:wlsxTrapTunnelId.setStatus(_B)
_WlsxTrapTunnelStatus_Type=Integer32
_WlsxTrapTunnelStatus_Object=MibScalar
wlsxTrapTunnelStatus=_WlsxTrapTunnelStatus_Object((1,3,6,1,4,1,14823,2,3,3,1,200,1,77),_WlsxTrapTunnelStatus_Type())
wlsxTrapTunnelStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:wlsxTrapTunnelStatus.setStatus(_B)
class _WlsxTrapTunnelUpReason_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_WlsxTrapTunnelUpReason_Type.__name__=_N
_WlsxTrapTunnelUpReason_Object=MibScalar
wlsxTrapTunnelUpReason=_WlsxTrapTunnelUpReason_Object((1,3,6,1,4,1,14823,2,3,3,1,200,1,78),_WlsxTrapTunnelUpReason_Type())
wlsxTrapTunnelUpReason.setMaxAccess(_E)
if mibBuilder.loadTexts:wlsxTrapTunnelUpReason.setStatus(_B)
class _WlsxTrapTunnelDownReason_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_WlsxTrapTunnelDownReason_Type.__name__=_N
_WlsxTrapTunnelDownReason_Object=MibScalar
wlsxTrapTunnelDownReason=_WlsxTrapTunnelDownReason_Object((1,3,6,1,4,1,14823,2,3,3,1,200,1,79),_WlsxTrapTunnelDownReason_Type())
wlsxTrapTunnelDownReason.setMaxAccess(_E)
if mibBuilder.loadTexts:wlsxTrapTunnelDownReason.setStatus(_B)
class _WlsxTrapApSerialNumber_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_WlsxTrapApSerialNumber_Type.__name__=_N
_WlsxTrapApSerialNumber_Object=MibScalar
wlsxTrapApSerialNumber=_WlsxTrapApSerialNumber_Object((1,3,6,1,4,1,14823,2,3,3,1,200,1,80),_WlsxTrapApSerialNumber_Type())
wlsxTrapApSerialNumber.setMaxAccess(_E)
if mibBuilder.loadTexts:wlsxTrapApSerialNumber.setStatus(_B)
class _WlsxTrapTimeStr_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_WlsxTrapTimeStr_Type.__name__=_N
_WlsxTrapTimeStr_Object=MibScalar
wlsxTrapTimeStr=_WlsxTrapTimeStr_Object((1,3,6,1,4,1,14823,2,3,3,1,200,1,81),_WlsxTrapTimeStr_Type())
wlsxTrapTimeStr.setMaxAccess(_E)
if mibBuilder.loadTexts:wlsxTrapTimeStr.setStatus(_B)
_WlsxTrapMasterIp_Type=IpAddress
_WlsxTrapMasterIp_Object=MibScalar
wlsxTrapMasterIp=_WlsxTrapMasterIp_Object((1,3,6,1,4,1,14823,2,3,3,1,200,1,82),_WlsxTrapMasterIp_Type())
wlsxTrapMasterIp.setMaxAccess(_E)
if mibBuilder.loadTexts:wlsxTrapMasterIp.setStatus(_U)
_WlsxTrapLocalIp_Type=IpAddress
_WlsxTrapLocalIp_Object=MibScalar
wlsxTrapLocalIp=_WlsxTrapLocalIp_Object((1,3,6,1,4,1,14823,2,3,3,1,200,1,83),_WlsxTrapLocalIp_Type())
wlsxTrapLocalIp.setMaxAccess(_E)
if mibBuilder.loadTexts:wlsxTrapLocalIp.setStatus(_B)
class _WlsxTrapMasterName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_WlsxTrapMasterName_Type.__name__=_N
_WlsxTrapMasterName_Object=MibScalar
wlsxTrapMasterName=_WlsxTrapMasterName_Object((1,3,6,1,4,1,14823,2,3,3,1,200,1,84),_WlsxTrapMasterName_Type())
wlsxTrapMasterName.setMaxAccess(_E)
if mibBuilder.loadTexts:wlsxTrapMasterName.setStatus(_U)
class _WlsxTrapLocalName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_WlsxTrapLocalName_Type.__name__=_N
_WlsxTrapLocalName_Object=MibScalar
wlsxTrapLocalName=_WlsxTrapLocalName_Object((1,3,6,1,4,1,14823,2,3,3,1,200,1,85),_WlsxTrapLocalName_Type())
wlsxTrapLocalName.setMaxAccess(_E)
if mibBuilder.loadTexts:wlsxTrapLocalName.setStatus(_B)
_WlsxTrapPrimaryControllerIp_Type=IpAddress
_WlsxTrapPrimaryControllerIp_Object=MibScalar
wlsxTrapPrimaryControllerIp=_WlsxTrapPrimaryControllerIp_Object((1,3,6,1,4,1,14823,2,3,3,1,200,1,86),_WlsxTrapPrimaryControllerIp_Type())
wlsxTrapPrimaryControllerIp.setMaxAccess(_E)
if mibBuilder.loadTexts:wlsxTrapPrimaryControllerIp.setStatus(_B)
_WlsxTrapBackupControllerIp_Type=IpAddress
_WlsxTrapBackupControllerIp_Object=MibScalar
wlsxTrapBackupControllerIp=_WlsxTrapBackupControllerIp_Object((1,3,6,1,4,1,14823,2,3,3,1,200,1,87),_WlsxTrapBackupControllerIp_Type())
wlsxTrapBackupControllerIp.setMaxAccess(_E)
if mibBuilder.loadTexts:wlsxTrapBackupControllerIp.setStatus(_B)
class _WlsxTrapSpoofedFrameType_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_WlsxTrapSpoofedFrameType_Type.__name__=_N
_WlsxTrapSpoofedFrameType_Object=MibScalar
wlsxTrapSpoofedFrameType=_WlsxTrapSpoofedFrameType_Object((1,3,6,1,4,1,14823,2,3,3,1,200,1,88),_WlsxTrapSpoofedFrameType_Type())
wlsxTrapSpoofedFrameType.setMaxAccess(_E)
if mibBuilder.loadTexts:wlsxTrapSpoofedFrameType.setStatus(_B)
class _WlsxTrapAssociationType_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_WlsxTrapAssociationType_Type.__name__=_N
_WlsxTrapAssociationType_Object=MibScalar
wlsxTrapAssociationType=_WlsxTrapAssociationType_Object((1,3,6,1,4,1,14823,2,3,3,1,200,1,89),_WlsxTrapAssociationType_Type())
wlsxTrapAssociationType.setMaxAccess(_E)
if mibBuilder.loadTexts:wlsxTrapAssociationType.setStatus(_B)
_WlsxTrapDeviceIpAddress_Type=IpAddress
_WlsxTrapDeviceIpAddress_Object=MibScalar
wlsxTrapDeviceIpAddress=_WlsxTrapDeviceIpAddress_Object((1,3,6,1,4,1,14823,2,3,3,1,200,1,90),_WlsxTrapDeviceIpAddress_Type())
wlsxTrapDeviceIpAddress.setMaxAccess(_E)
if mibBuilder.loadTexts:wlsxTrapDeviceIpAddress.setStatus(_B)
_WlsxTrapDeviceMac_Type=MacAddress
_WlsxTrapDeviceMac_Object=MibScalar
wlsxTrapDeviceMac=_WlsxTrapDeviceMac_Object((1,3,6,1,4,1,14823,2,3,3,1,200,1,91),_WlsxTrapDeviceMac_Type())
wlsxTrapDeviceMac.setMaxAccess(_E)
if mibBuilder.loadTexts:wlsxTrapDeviceMac.setStatus(_B)
_WlsxTrapVcIpAddress_Type=IpAddress
_WlsxTrapVcIpAddress_Object=MibScalar
wlsxTrapVcIpAddress=_WlsxTrapVcIpAddress_Object((1,3,6,1,4,1,14823,2,3,3,1,200,1,92),_WlsxTrapVcIpAddress_Type())
wlsxTrapVcIpAddress.setMaxAccess(_E)
if mibBuilder.loadTexts:wlsxTrapVcIpAddress.setStatus(_B)
_WlsxTrapVcMacAddress_Type=MacAddress
_WlsxTrapVcMacAddress_Object=MibScalar
wlsxTrapVcMacAddress=_WlsxTrapVcMacAddress_Object((1,3,6,1,4,1,14823,2,3,3,1,200,1,93),_WlsxTrapVcMacAddress_Type())
wlsxTrapVcMacAddress.setMaxAccess(_E)
if mibBuilder.loadTexts:wlsxTrapVcMacAddress.setStatus(_B)
class _WlsxTrapAPName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_WlsxTrapAPName_Type.__name__=_N
_WlsxTrapAPName_Object=MibScalar
wlsxTrapAPName=_WlsxTrapAPName_Object((1,3,6,1,4,1,14823,2,3,3,1,200,1,94),_WlsxTrapAPName_Type())
wlsxTrapAPName.setMaxAccess(_E)
if mibBuilder.loadTexts:wlsxTrapAPName.setStatus(_B)
_WlsxTrapApMode_Type=Integer32
_WlsxTrapApMode_Object=MibScalar
wlsxTrapApMode=_WlsxTrapApMode_Object((1,3,6,1,4,1,14823,2,3,3,1,200,1,95),_WlsxTrapApMode_Type())
wlsxTrapApMode.setMaxAccess(_E)
if mibBuilder.loadTexts:wlsxTrapApMode.setStatus(_B)
_WlsxTrapAPPrevChannel_Type=Integer32
_WlsxTrapAPPrevChannel_Object=MibScalar
wlsxTrapAPPrevChannel=_WlsxTrapAPPrevChannel_Object((1,3,6,1,4,1,14823,2,3,3,1,200,1,96),_WlsxTrapAPPrevChannel_Type())
wlsxTrapAPPrevChannel.setMaxAccess(_E)
if mibBuilder.loadTexts:wlsxTrapAPPrevChannel.setStatus(_B)
_WlsxTrapAPPrevChannelSec_Type=ArubaHTExtChannel
_WlsxTrapAPPrevChannelSec_Object=MibScalar
wlsxTrapAPPrevChannelSec=_WlsxTrapAPPrevChannelSec_Object((1,3,6,1,4,1,14823,2,3,3,1,200,1,97),_WlsxTrapAPPrevChannelSec_Type())
wlsxTrapAPPrevChannelSec.setMaxAccess(_E)
if mibBuilder.loadTexts:wlsxTrapAPPrevChannelSec.setStatus(_B)
_WlsxTrapAPPrevTxPower_Type=Integer32
_WlsxTrapAPPrevTxPower_Object=MibScalar
wlsxTrapAPPrevTxPower=_WlsxTrapAPPrevTxPower_Object((1,3,6,1,4,1,14823,2,3,3,1,200,1,98),_WlsxTrapAPPrevTxPower_Type())
wlsxTrapAPPrevTxPower.setMaxAccess(_E)
if mibBuilder.loadTexts:wlsxTrapAPPrevTxPower.setStatus(_B)
_WlsxTrapAPCurMode_Type=ArubaAccessPointMode
_WlsxTrapAPCurMode_Object=MibScalar
wlsxTrapAPCurMode=_WlsxTrapAPCurMode_Object((1,3,6,1,4,1,14823,2,3,3,1,200,1,99),_WlsxTrapAPCurMode_Type())
wlsxTrapAPCurMode.setMaxAccess(_E)
if mibBuilder.loadTexts:wlsxTrapAPCurMode.setStatus(_B)
_WlsxTrapAPPrevMode_Type=ArubaAccessPointMode
_WlsxTrapAPPrevMode_Object=MibScalar
wlsxTrapAPPrevMode=_WlsxTrapAPPrevMode_Object((1,3,6,1,4,1,14823,2,3,3,1,200,1,100),_WlsxTrapAPPrevMode_Type())
wlsxTrapAPPrevMode.setMaxAccess(_E)
if mibBuilder.loadTexts:wlsxTrapAPPrevMode.setStatus(_B)
_WlsxTrapAPARMChangeReason_Type=ArubaARMChangeReason
_WlsxTrapAPARMChangeReason_Object=MibScalar
wlsxTrapAPARMChangeReason=_WlsxTrapAPARMChangeReason_Object((1,3,6,1,4,1,14823,2,3,3,1,200,1,101),_WlsxTrapAPARMChangeReason_Type())
wlsxTrapAPARMChangeReason.setMaxAccess(_E)
if mibBuilder.loadTexts:wlsxTrapAPARMChangeReason.setStatus(_B)
_WlsxTrapAPChannelSec_Type=ArubaHTExtChannel
_WlsxTrapAPChannelSec_Object=MibScalar
wlsxTrapAPChannelSec=_WlsxTrapAPChannelSec_Object((1,3,6,1,4,1,14823,2,3,3,1,200,1,102),_WlsxTrapAPChannelSec_Type())
wlsxTrapAPChannelSec.setMaxAccess(_E)
if mibBuilder.loadTexts:wlsxTrapAPChannelSec.setStatus(_B)
_WlsxTrapUserAttributeChangeType_Type=ArubaConfigurationChangeType
_WlsxTrapUserAttributeChangeType_Object=MibScalar
wlsxTrapUserAttributeChangeType=_WlsxTrapUserAttributeChangeType_Object((1,3,6,1,4,1,14823,2,3,3,1,200,1,103),_WlsxTrapUserAttributeChangeType_Type())
wlsxTrapUserAttributeChangeType.setMaxAccess(_E)
if mibBuilder.loadTexts:wlsxTrapUserAttributeChangeType.setStatus(_B)
_WlsxTrapApControllerIp_Type=IpAddress
_WlsxTrapApControllerIp_Object=MibScalar
wlsxTrapApControllerIp=_WlsxTrapApControllerIp_Object((1,3,6,1,4,1,14823,2,3,3,1,200,1,104),_WlsxTrapApControllerIp_Type())
wlsxTrapApControllerIp.setMaxAccess(_E)
if mibBuilder.loadTexts:wlsxTrapApControllerIp.setStatus(_B)
_WlsxTrapApMasterStatus_Type=ArubaAPMasterStatus
_WlsxTrapApMasterStatus_Object=MibScalar
wlsxTrapApMasterStatus=_WlsxTrapApMasterStatus_Object((1,3,6,1,4,1,14823,2,3,3,1,200,1,105),_WlsxTrapApMasterStatus_Type())
wlsxTrapApMasterStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:wlsxTrapApMasterStatus.setStatus(_U)
class _WlsxTrapCaName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_WlsxTrapCaName_Type.__name__=_N
_WlsxTrapCaName_Object=MibScalar
wlsxTrapCaName=_WlsxTrapCaName_Object((1,3,6,1,4,1,14823,2,3,3,1,200,1,106),_WlsxTrapCaName_Type())
wlsxTrapCaName.setMaxAccess(_E)
if mibBuilder.loadTexts:wlsxTrapCaName.setStatus(_B)
class _WlsxTrapCrlName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_WlsxTrapCrlName_Type.__name__=_N
_WlsxTrapCrlName_Object=MibScalar
wlsxTrapCrlName=_WlsxTrapCrlName_Object((1,3,6,1,4,1,14823,2,3,3,1,200,1,107),_WlsxTrapCrlName_Type())
wlsxTrapCrlName.setMaxAccess(_E)
if mibBuilder.loadTexts:wlsxTrapCrlName.setStatus(_B)
_WlsxTrapCount_Type=Integer32
_WlsxTrapCount_Object=MibScalar
wlsxTrapCount=_WlsxTrapCount_Object((1,3,6,1,4,1,14823,2,3,3,1,200,1,108),_WlsxTrapCount_Type())
wlsxTrapCount.setMaxAccess(_E)
if mibBuilder.loadTexts:wlsxTrapCount.setStatus(_B)
_WlsxTrapAPPreviousUplinkType_Type=ArubaAPUplinkType
_WlsxTrapAPPreviousUplinkType_Object=MibScalar
wlsxTrapAPPreviousUplinkType=_WlsxTrapAPPreviousUplinkType_Object((1,3,6,1,4,1,14823,2,3,3,1,200,1,130),_WlsxTrapAPPreviousUplinkType_Type())
wlsxTrapAPPreviousUplinkType.setMaxAccess(_E)
if mibBuilder.loadTexts:wlsxTrapAPPreviousUplinkType.setStatus(_B)
_WlsxTrapAPPreviousUplinkActiveTime_Type=TimeTicks
_WlsxTrapAPPreviousUplinkActiveTime_Object=MibScalar
wlsxTrapAPPreviousUplinkActiveTime=_WlsxTrapAPPreviousUplinkActiveTime_Object((1,3,6,1,4,1,14823,2,3,3,1,200,1,131),_WlsxTrapAPPreviousUplinkActiveTime_Type())
wlsxTrapAPPreviousUplinkActiveTime.setMaxAccess(_E)
if mibBuilder.loadTexts:wlsxTrapAPPreviousUplinkActiveTime.setStatus(_B)
_WlsxTrapAPActiveUplinkType_Type=ArubaAPUplinkType
_WlsxTrapAPActiveUplinkType_Object=MibScalar
wlsxTrapAPActiveUplinkType=_WlsxTrapAPActiveUplinkType_Object((1,3,6,1,4,1,14823,2,3,3,1,200,1,132),_WlsxTrapAPActiveUplinkType_Type())
wlsxTrapAPActiveUplinkType.setMaxAccess(_E)
if mibBuilder.loadTexts:wlsxTrapAPActiveUplinkType.setStatus(_B)
_WlsxTrapAPUplinkChangeReason_Type=ArubaAPUplinkChangeReason
_WlsxTrapAPUplinkChangeReason_Object=MibScalar
wlsxTrapAPUplinkChangeReason=_WlsxTrapAPUplinkChangeReason_Object((1,3,6,1,4,1,14823,2,3,3,1,200,1,133),_WlsxTrapAPUplinkChangeReason_Type())
wlsxTrapAPUplinkChangeReason.setMaxAccess(_E)
if mibBuilder.loadTexts:wlsxTrapAPUplinkChangeReason.setStatus(_B)
class _WlsxTrapAPManagedModeConfigFailure_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_WlsxTrapAPManagedModeConfigFailure_Type.__name__=_N
_WlsxTrapAPManagedModeConfigFailure_Object=MibScalar
wlsxTrapAPManagedModeConfigFailure=_WlsxTrapAPManagedModeConfigFailure_Object((1,3,6,1,4,1,14823,2,3,3,1,200,1,138),_WlsxTrapAPManagedModeConfigFailure_Type())
wlsxTrapAPManagedModeConfigFailure.setMaxAccess(_E)
if mibBuilder.loadTexts:wlsxTrapAPManagedModeConfigFailure.setStatus(_B)
_WlsxTrapAuthServerAddress_Type=IpAddress
_WlsxTrapAuthServerAddress_Object=MibScalar
wlsxTrapAuthServerAddress=_WlsxTrapAuthServerAddress_Object((1,3,6,1,4,1,14823,2,3,3,1,200,1,139),_WlsxTrapAuthServerAddress_Type())
wlsxTrapAuthServerAddress.setMaxAccess(_E)
if mibBuilder.loadTexts:wlsxTrapAuthServerAddress.setStatus(_B)
class _WlsxTrapPortalServerName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_WlsxTrapPortalServerName_Type.__name__=_N
_WlsxTrapPortalServerName_Object=MibScalar
wlsxTrapPortalServerName=_WlsxTrapPortalServerName_Object((1,3,6,1,4,1,14823,2,3,3,1,200,1,140),_WlsxTrapPortalServerName_Type())
wlsxTrapPortalServerName.setMaxAccess(_E)
if mibBuilder.loadTexts:wlsxTrapPortalServerName.setStatus(_B)
class _WlsxTrapPortalServerAddress_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_WlsxTrapPortalServerAddress_Type.__name__=_N
_WlsxTrapPortalServerAddress_Object=MibScalar
wlsxTrapPortalServerAddress=_WlsxTrapPortalServerAddress_Object((1,3,6,1,4,1,14823,2,3,3,1,200,1,141),_WlsxTrapPortalServerAddress_Type())
wlsxTrapPortalServerAddress.setMaxAccess(_E)
if mibBuilder.loadTexts:wlsxTrapPortalServerAddress.setStatus(_B)
_WlsxTrapPortalServerDownReason_Type=ArubaPortalServerDownReason
_WlsxTrapPortalServerDownReason_Object=MibScalar
wlsxTrapPortalServerDownReason=_WlsxTrapPortalServerDownReason_Object((1,3,6,1,4,1,14823,2,3,3,1,200,1,142),_WlsxTrapPortalServerDownReason_Type())
wlsxTrapPortalServerDownReason.setMaxAccess(_E)
if mibBuilder.loadTexts:wlsxTrapPortalServerDownReason.setStatus(_B)
class _WlsxTrapStationBlackListReasonStr_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_WlsxTrapStationBlackListReasonStr_Type.__name__=_N
_WlsxTrapStationBlackListReasonStr_Object=MibScalar
wlsxTrapStationBlackListReasonStr=_WlsxTrapStationBlackListReasonStr_Object((1,3,6,1,4,1,14823,2,3,3,1,200,1,144),_WlsxTrapStationBlackListReasonStr_Type())
wlsxTrapStationBlackListReasonStr.setMaxAccess(_E)
if mibBuilder.loadTexts:wlsxTrapStationBlackListReasonStr.setStatus(_U)
class _WlsxTrapAPUSBStatus_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_WlsxTrapAPUSBStatus_Type.__name__=_N
_WlsxTrapAPUSBStatus_Object=MibScalar
wlsxTrapAPUSBStatus=_WlsxTrapAPUSBStatus_Object((1,3,6,1,4,1,14823,2,3,3,1,200,1,147),_WlsxTrapAPUSBStatus_Type())
wlsxTrapAPUSBStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:wlsxTrapAPUSBStatus.setStatus(_B)
class _WlsxTrapUSBVendorProductID_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_WlsxTrapUSBVendorProductID_Type.__name__=_N
_WlsxTrapUSBVendorProductID_Object=MibScalar
wlsxTrapUSBVendorProductID=_WlsxTrapUSBVendorProductID_Object((1,3,6,1,4,1,14823,2,3,3,1,200,1,148),_WlsxTrapUSBVendorProductID_Type())
wlsxTrapUSBVendorProductID.setMaxAccess(_E)
if mibBuilder.loadTexts:wlsxTrapUSBVendorProductID.setStatus(_B)
class _WlsxTrapAuthFailureReason_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_WlsxTrapAuthFailureReason_Type.__name__=_N
_WlsxTrapAuthFailureReason_Object=MibScalar
wlsxTrapAuthFailureReason=_WlsxTrapAuthFailureReason_Object((1,3,6,1,4,1,14823,2,3,3,1,200,1,155),_WlsxTrapAuthFailureReason_Type())
wlsxTrapAuthFailureReason.setMaxAccess(_E)
if mibBuilder.loadTexts:wlsxTrapAuthFailureReason.setStatus(_B)
_WlsxTrapStationDenyListReason_Type=ArubaDenyListReason
_WlsxTrapStationDenyListReason_Object=MibScalar
wlsxTrapStationDenyListReason=_WlsxTrapStationDenyListReason_Object((1,3,6,1,4,1,14823,2,3,3,1,200,1,156),_WlsxTrapStationDenyListReason_Type())
wlsxTrapStationDenyListReason.setMaxAccess(_E)
if mibBuilder.loadTexts:wlsxTrapStationDenyListReason.setStatus(_B)
class _WlsxTrapStationDenyListReasonStr_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_WlsxTrapStationDenyListReasonStr_Type.__name__=_N
_WlsxTrapStationDenyListReasonStr_Object=MibScalar
wlsxTrapStationDenyListReasonStr=_WlsxTrapStationDenyListReasonStr_Object((1,3,6,1,4,1,14823,2,3,3,1,200,1,157),_WlsxTrapStationDenyListReasonStr_Type())
wlsxTrapStationDenyListReasonStr.setMaxAccess(_E)
if mibBuilder.loadTexts:wlsxTrapStationDenyListReasonStr.setStatus(_B)
_WlsxTrapConductorIp_Type=IpAddress
_WlsxTrapConductorIp_Object=MibScalar
wlsxTrapConductorIp=_WlsxTrapConductorIp_Object((1,3,6,1,4,1,14823,2,3,3,1,200,1,158),_WlsxTrapConductorIp_Type())
wlsxTrapConductorIp.setMaxAccess(_E)
if mibBuilder.loadTexts:wlsxTrapConductorIp.setStatus(_B)
class _WlsxTrapConductorName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_WlsxTrapConductorName_Type.__name__=_N
_WlsxTrapConductorName_Object=MibScalar
wlsxTrapConductorName=_WlsxTrapConductorName_Object((1,3,6,1,4,1,14823,2,3,3,1,200,1,159),_WlsxTrapConductorName_Type())
wlsxTrapConductorName.setMaxAccess(_E)
if mibBuilder.loadTexts:wlsxTrapConductorName.setStatus(_B)
_WlsxTrapApConductorStatus_Type=ArubaAPConductorStatus
_WlsxTrapApConductorStatus_Object=MibScalar
wlsxTrapApConductorStatus=_WlsxTrapApConductorStatus_Object((1,3,6,1,4,1,14823,2,3,3,1,200,1,160),_WlsxTrapApConductorStatus_Type())
wlsxTrapApConductorStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:wlsxTrapApConductorStatus.setStatus(_B)
_WlsxTrapAPHTMode_Type=ArubaHTMode
_WlsxTrapAPHTMode_Object=MibScalar
wlsxTrapAPHTMode=_WlsxTrapAPHTMode_Object((1,3,6,1,4,1,14823,2,3,3,1,200,1,161),_WlsxTrapAPHTMode_Type())
wlsxTrapAPHTMode.setMaxAccess(_E)
if mibBuilder.loadTexts:wlsxTrapAPHTMode.setStatus(_B)
_WlsxTrapAPPhyType_Type=ArubaPhyType
_WlsxTrapAPPhyType_Object=MibScalar
wlsxTrapAPPhyType=_WlsxTrapAPPhyType_Object((1,3,6,1,4,1,14823,2,3,3,1,200,1,162),_WlsxTrapAPPhyType_Type())
wlsxTrapAPPhyType.setMaxAccess(_E)
if mibBuilder.loadTexts:wlsxTrapAPPhyType.setStatus(_B)
_WlsxTrapAPPrevHTMode_Type=ArubaHTMode
_WlsxTrapAPPrevHTMode_Object=MibScalar
wlsxTrapAPPrevHTMode=_WlsxTrapAPPrevHTMode_Object((1,3,6,1,4,1,14823,2,3,3,1,200,1,163),_WlsxTrapAPPrevHTMode_Type())
wlsxTrapAPPrevHTMode.setMaxAccess(_E)
if mibBuilder.loadTexts:wlsxTrapAPPrevHTMode.setStatus(_B)
_WlsxTrapAPPrevPhyType_Type=ArubaPhyType
_WlsxTrapAPPrevPhyType_Object=MibScalar
wlsxTrapAPPrevPhyType=_WlsxTrapAPPrevPhyType_Object((1,3,6,1,4,1,14823,2,3,3,1,200,1,164),_WlsxTrapAPPrevPhyType_Type())
wlsxTrapAPPrevPhyType.setMaxAccess(_E)
if mibBuilder.loadTexts:wlsxTrapAPPrevPhyType.setStatus(_B)
_WlsxTrapAPSecChannel_Type=Integer32
_WlsxTrapAPSecChannel_Object=MibScalar
wlsxTrapAPSecChannel=_WlsxTrapAPSecChannel_Object((1,3,6,1,4,1,14823,2,3,3,1,200,1,165),_WlsxTrapAPSecChannel_Type())
wlsxTrapAPSecChannel.setMaxAccess(_E)
if mibBuilder.loadTexts:wlsxTrapAPSecChannel.setStatus(_B)
class _WlsxTrapAPBand_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_WlsxTrapAPBand_Type.__name__=_N
_WlsxTrapAPBand_Object=MibScalar
wlsxTrapAPBand=_WlsxTrapAPBand_Object((1,3,6,1,4,1,14823,2,3,3,1,200,1,166),_WlsxTrapAPBand_Type())
wlsxTrapAPBand.setMaxAccess(_E)
if mibBuilder.loadTexts:wlsxTrapAPBand.setStatus(_B)
class _WlsxTrapTargetAPBand_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_WlsxTrapTargetAPBand_Type.__name__=_N
_WlsxTrapTargetAPBand_Object=MibScalar
wlsxTrapTargetAPBand=_WlsxTrapTargetAPBand_Object((1,3,6,1,4,1,14823,2,3,3,1,200,1,167),_WlsxTrapTargetAPBand_Type())
wlsxTrapTargetAPBand.setMaxAccess(_E)
if mibBuilder.loadTexts:wlsxTrapTargetAPBand.setStatus(_B)
class _WlsxTrapMatchedIpv6_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,128))
_WlsxTrapMatchedIpv6_Type.__name__=_N
_WlsxTrapMatchedIpv6_Object=MibScalar
wlsxTrapMatchedIpv6=_WlsxTrapMatchedIpv6_Object((1,3,6,1,4,1,14823,2,3,3,1,200,1,168),_WlsxTrapMatchedIpv6_Type())
wlsxTrapMatchedIpv6.setMaxAccess(_E)
if mibBuilder.loadTexts:wlsxTrapMatchedIpv6.setStatus(_B)
_AiTrapDefinitionsGroup_ObjectIdentity=ObjectIdentity
aiTrapDefinitionsGroup=_AiTrapDefinitionsGroup_ObjectIdentity((1,3,6,1,4,1,14823,2,3,3,1,200,2))
wlsxNodeRateAnomaly=NotificationType((1,3,6,1,4,1,14823,2,3,3,1,200,2,1003))
wlsxNodeRateAnomaly.setObjects(*((_A,_C),(_A,_X),(_A,_P),(_A,_M),(_A,_Y),(_A,_G)))
if mibBuilder.loadTexts:wlsxNodeRateAnomaly.setStatus(_B)
wlsxNUserEntryCreated=NotificationType((1,3,6,1,4,1,14823,2,3,3,1,200,2,1014))
wlsxNUserEntryCreated.setObjects(*((_A,_C),(_A,_V),(_A,_T)))
if mibBuilder.loadTexts:wlsxNUserEntryCreated.setStatus(_B)
wlsxNUserEntryDeleted=NotificationType((1,3,6,1,4,1,14823,2,3,3,1,200,2,1015))
wlsxNUserEntryDeleted.setObjects(*((_A,_C),(_A,_V),(_A,_T)))
if mibBuilder.loadTexts:wlsxNUserEntryDeleted.setStatus(_B)
wlsxNUserEntryAuthenticated=NotificationType((1,3,6,1,4,1,14823,2,3,3,1,200,2,1016))
wlsxNUserEntryAuthenticated.setObjects(*((_A,_C),(_A,_V),(_A,_T),(_A,_g),(_A,_AV),(_A,_AW)))
if mibBuilder.loadTexts:wlsxNUserEntryAuthenticated.setStatus(_B)
wlsxNUserEntryDeAuthenticated=NotificationType((1,3,6,1,4,1,14823,2,3,3,1,200,2,1017))
wlsxNUserEntryDeAuthenticated.setObjects(*((_A,_C),(_A,_V),(_A,_T)))
if mibBuilder.loadTexts:wlsxNUserEntryDeAuthenticated.setStatus(_B)
wlsxNUserAuthenticationFailed=NotificationType((1,3,6,1,4,1,14823,2,3,3,1,200,2,1018))
wlsxNUserAuthenticationFailed.setObjects(*((_A,_C),(_A,_g),(_A,_V),(_A,_T),(_A,_Z),(_A,_e),(_A,_Y),(_A,_S)))
if mibBuilder.loadTexts:wlsxNUserAuthenticationFailed.setStatus(_B)
wlsxNAuthServerReqTimedOut=NotificationType((1,3,6,1,4,1,14823,2,3,3,1,200,2,1019))
wlsxNAuthServerReqTimedOut.setObjects(*((_A,_C),(_A,_g),(_A,_V),(_A,_T),(_A,_Z),(_A,_e),(_A,_Y),(_A,_S)))
if mibBuilder.loadTexts:wlsxNAuthServerReqTimedOut.setStatus(_B)
wlsxNAuthServerTimedOut=NotificationType((1,3,6,1,4,1,14823,2,3,3,1,200,2,1020))
wlsxNAuthServerTimedOut.setObjects(*((_A,_C),(_A,_Z),(_A,_AX)))
if mibBuilder.loadTexts:wlsxNAuthServerTimedOut.setStatus(_B)
wlsxNAuthServerIsUp=NotificationType((1,3,6,1,4,1,14823,2,3,3,1,200,2,1021))
wlsxNAuthServerIsUp.setObjects(*((_A,_C),(_A,_Z),(_A,_e)))
if mibBuilder.loadTexts:wlsxNAuthServerIsUp.setStatus(_B)
wlsxNAccessPointIsUp=NotificationType((1,3,6,1,4,1,14823,2,3,3,1,200,2,1040))
wlsxNAccessPointIsUp.setObjects(*((_A,_C),(_A,_D)))
if mibBuilder.loadTexts:wlsxNAccessPointIsUp.setStatus(_B)
wlsxNAccessPointIsDown=NotificationType((1,3,6,1,4,1,14823,2,3,3,1,200,2,1041))
wlsxNAccessPointIsDown.setObjects(*((_A,_C),(_A,_D)))
if mibBuilder.loadTexts:wlsxNAccessPointIsDown.setStatus(_B)
wlsxNChannelChanged=NotificationType((1,3,6,1,4,1,14823,2,3,3,1,200,2,1043))
wlsxNChannelChanged.setObjects(*((_A,_C),(_A,_Y),(_A,_G),(_A,_I)))
if mibBuilder.loadTexts:wlsxNChannelChanged.setStatus(_B)
wlsxNStationAddedToBlackList=NotificationType((1,3,6,1,4,1,14823,2,3,3,1,200,2,1044))
wlsxNStationAddedToBlackList.setObjects(*((_A,_C),(_A,_P),(_A,_AY),(_A,_AZ)))
if mibBuilder.loadTexts:wlsxNStationAddedToBlackList.setStatus(_U)
wlsxNStationRemovedFromBlackList=NotificationType((1,3,6,1,4,1,14823,2,3,3,1,200,2,1045))
wlsxNStationRemovedFromBlackList.setObjects(*((_A,_C),(_A,_P)))
if mibBuilder.loadTexts:wlsxNStationRemovedFromBlackList.setStatus(_U)
wlsxNRadioAttributesChanged=NotificationType((1,3,6,1,4,1,14823,2,3,3,1,200,2,1049))
wlsxNRadioAttributesChanged.setObjects(*((_A,_C),(_A,_D),(_A,_F),(_A,_Aa),(_A,_I),(_A,_q),(_A,_Ab),(_A,_r),(_A,_s)))
if mibBuilder.loadTexts:wlsxNRadioAttributesChanged.setStatus(_B)
wlsxUnsecureAPDetected=NotificationType((1,3,6,1,4,1,14823,2,3,3,1,200,2,1053))
wlsxUnsecureAPDetected.setObjects(*((_A,_C),(_A,_H),(_A,_L),(_A,_D),(_A,_F),(_A,_G),(_A,_I),(_A,_t),(_A,_u),(_A,_m),(_A,_Ac),(_A,_K)))
if mibBuilder.loadTexts:wlsxUnsecureAPDetected.setStatus(_B)
wlsxUnsecureAPResolved=NotificationType((1,3,6,1,4,1,14823,2,3,3,1,200,2,1054))
wlsxUnsecureAPResolved.setObjects(*((_A,_C),(_A,_H),(_A,_L),(_A,_D),(_A,_F),(_A,_G),(_A,_I),(_A,_K)))
if mibBuilder.loadTexts:wlsxUnsecureAPResolved.setStatus(_B)
wlsxStaImpersonation=NotificationType((1,3,6,1,4,1,14823,2,3,3,1,200,2,1055))
wlsxStaImpersonation.setObjects(*((_A,_C),(_A,_P),(_A,_D),(_A,_F),(_A,_G)))
if mibBuilder.loadTexts:wlsxStaImpersonation.setStatus(_B)
wlsxReservedChannelViolation=NotificationType((1,3,6,1,4,1,14823,2,3,3,1,200,2,1056))
wlsxReservedChannelViolation.setObjects(*((_A,_C),(_A,_H),(_A,_L),(_A,_D),(_A,_F),(_A,_G),(_A,_I),(_A,_K)))
if mibBuilder.loadTexts:wlsxReservedChannelViolation.setStatus(_B)
wlsxValidSSIDViolation=NotificationType((1,3,6,1,4,1,14823,2,3,3,1,200,2,1057))
wlsxValidSSIDViolation.setObjects(*((_A,_C),(_A,_H),(_A,_L),(_A,_D),(_A,_F),(_A,_G),(_A,_I),(_A,_K)))
if mibBuilder.loadTexts:wlsxValidSSIDViolation.setStatus(_B)
wlsxChannelMisconfiguration=NotificationType((1,3,6,1,4,1,14823,2,3,3,1,200,2,1058))
wlsxChannelMisconfiguration.setObjects(*((_A,_C),(_A,_H),(_A,_L),(_A,_D),(_A,_F),(_A,_G),(_A,_I),(_A,_K)))
if mibBuilder.loadTexts:wlsxChannelMisconfiguration.setStatus(_B)
wlsxOUIMisconfiguration=NotificationType((1,3,6,1,4,1,14823,2,3,3,1,200,2,1059))
wlsxOUIMisconfiguration.setObjects(*((_A,_C),(_A,_H),(_A,_L),(_A,_D),(_A,_F),(_A,_G),(_A,_I),(_A,_K)))
if mibBuilder.loadTexts:wlsxOUIMisconfiguration.setStatus(_B)
wlsxSSIDMisconfiguration=NotificationType((1,3,6,1,4,1,14823,2,3,3,1,200,2,1060))
wlsxSSIDMisconfiguration.setObjects(*((_A,_C),(_A,_H),(_A,_L),(_A,_D),(_A,_F),(_A,_G),(_A,_I),(_A,_K)))
if mibBuilder.loadTexts:wlsxSSIDMisconfiguration.setStatus(_B)
wlsxShortPreableMisconfiguration=NotificationType((1,3,6,1,4,1,14823,2,3,3,1,200,2,1061))
wlsxShortPreableMisconfiguration.setObjects(*((_A,_C),(_A,_H),(_A,_L),(_A,_D),(_A,_F),(_A,_G),(_A,_I)))
if mibBuilder.loadTexts:wlsxShortPreableMisconfiguration.setStatus(_B)
wlsxWPAMisconfiguration=NotificationType((1,3,6,1,4,1,14823,2,3,3,1,200,2,1062))
wlsxWPAMisconfiguration.setObjects(*((_A,_C),(_A,_H),(_A,_L),(_A,_D),(_A,_F),(_A,_G),(_A,_I),(_A,_K)))
if mibBuilder.loadTexts:wlsxWPAMisconfiguration.setStatus(_B)
wlsxAdhocNetworkDetected=NotificationType((1,3,6,1,4,1,14823,2,3,3,1,200,2,1063))
wlsxAdhocNetworkDetected.setObjects(*((_A,_C),(_A,_H),(_A,_L),(_A,_D),(_A,_F),(_A,_G),(_A,_I)))
if mibBuilder.loadTexts:wlsxAdhocNetworkDetected.setStatus(_B)
wlsxAdhocNetworkRemoved=NotificationType((1,3,6,1,4,1,14823,2,3,3,1,200,2,1064))
wlsxAdhocNetworkRemoved.setObjects(*((_A,_C),(_A,_H),(_A,_L),(_A,_D),(_A,_F),(_A,_G),(_A,_I)))
if mibBuilder.loadTexts:wlsxAdhocNetworkRemoved.setStatus(_B)
wlsxStaPolicyViolation=NotificationType((1,3,6,1,4,1,14823,2,3,3,1,200,2,1065))
wlsxStaPolicyViolation.setObjects(*((_A,_C),(_A,_H),(_A,_P),(_A,_D),(_A,_F),(_A,_G),(_A,_I),(_A,_K)))
if mibBuilder.loadTexts:wlsxStaPolicyViolation.setStatus(_B)
wlsxRepeatWEPIVViolation=NotificationType((1,3,6,1,4,1,14823,2,3,3,1,200,2,1066))
wlsxRepeatWEPIVViolation.setObjects(*((_A,_C),(_A,_H),(_A,_L),(_A,_D),(_A,_F),(_A,_G),(_A,_I),(_A,_K)))
if mibBuilder.loadTexts:wlsxRepeatWEPIVViolation.setStatus(_B)
wlsxWeakWEPIVViolation=NotificationType((1,3,6,1,4,1,14823,2,3,3,1,200,2,1067))
wlsxWeakWEPIVViolation.setObjects(*((_A,_C),(_A,_H),(_A,_L),(_A,_D),(_A,_F),(_A,_G),(_A,_I),(_A,_K)))
if mibBuilder.loadTexts:wlsxWeakWEPIVViolation.setStatus(_B)
wlsxChannelInterferenceDetected=NotificationType((1,3,6,1,4,1,14823,2,3,3,1,200,2,1068))
wlsxChannelInterferenceDetected.setObjects(*((_A,_C),(_A,_D),(_A,_F),(_A,_G),(_A,_I)))
if mibBuilder.loadTexts:wlsxChannelInterferenceDetected.setStatus(_B)
wlsxChannelInterferenceCleared=NotificationType((1,3,6,1,4,1,14823,2,3,3,1,200,2,1069))
wlsxChannelInterferenceCleared.setObjects(*((_A,_C),(_A,_D),(_A,_F),(_A,_G),(_A,_I)))
if mibBuilder.loadTexts:wlsxChannelInterferenceCleared.setStatus(_B)
wlsxAPInterferenceDetected=NotificationType((1,3,6,1,4,1,14823,2,3,3,1,200,2,1070))
wlsxAPInterferenceDetected.setObjects(*((_A,_C),(_A,_H),(_A,_L),(_A,_D),(_A,_F),(_A,_G),(_A,_I),(_A,_K)))
if mibBuilder.loadTexts:wlsxAPInterferenceDetected.setStatus(_B)
wlsxAPInterferenceCleared=NotificationType((1,3,6,1,4,1,14823,2,3,3,1,200,2,1071))
wlsxAPInterferenceCleared.setObjects(*((_A,_C),(_A,_H),(_A,_L),(_A,_D),(_A,_F),(_A,_G),(_A,_I),(_A,_K)))
if mibBuilder.loadTexts:wlsxAPInterferenceCleared.setStatus(_B)
wlsxStaInterferenceDetected=NotificationType((1,3,6,1,4,1,14823,2,3,3,1,200,2,1072))
wlsxStaInterferenceDetected.setObjects(*((_A,_C),(_A,_H),(_A,_L),(_A,_D),(_A,_F),(_A,_P),(_A,_G),(_A,_I),(_A,_K)))
if mibBuilder.loadTexts:wlsxStaInterferenceDetected.setStatus(_B)
wlsxStaInterferenceCleared=NotificationType((1,3,6,1,4,1,14823,2,3,3,1,200,2,1073))
wlsxStaInterferenceCleared.setObjects(*((_A,_C),(_A,_H),(_A,_L),(_A,_D),(_A,_F),(_A,_P),(_A,_G),(_A,_I),(_A,_K)))
if mibBuilder.loadTexts:wlsxStaInterferenceCleared.setStatus(_B)
wlsxFrameRetryRateExceeded=NotificationType((1,3,6,1,4,1,14823,2,3,3,1,200,2,1074))
wlsxFrameRetryRateExceeded.setObjects(*((_A,_C),(_A,_H),(_A,_L),(_A,_D),(_A,_F),(_A,_G),(_A,_I),(_A,_K)))
if mibBuilder.loadTexts:wlsxFrameRetryRateExceeded.setStatus(_B)
wlsxFrameReceiveErrorRateExceeded=NotificationType((1,3,6,1,4,1,14823,2,3,3,1,200,2,1075))
wlsxFrameReceiveErrorRateExceeded.setObjects(*((_A,_C),(_A,_H),(_A,_L),(_A,_D),(_A,_F),(_A,_j),(_A,_G),(_A,_K)))
if mibBuilder.loadTexts:wlsxFrameReceiveErrorRateExceeded.setStatus(_B)
wlsxFrameFragmentationRateExceeded=NotificationType((1,3,6,1,4,1,14823,2,3,3,1,200,2,1076))
wlsxFrameFragmentationRateExceeded.setObjects(*((_A,_C),(_A,_H),(_A,_L),(_A,_D),(_A,_F),(_A,_j),(_A,_G),(_A,_K)))
if mibBuilder.loadTexts:wlsxFrameFragmentationRateExceeded.setStatus(_B)
wlsxFrameBandWidthRateExceeded=NotificationType((1,3,6,1,4,1,14823,2,3,3,1,200,2,1077))
wlsxFrameBandWidthRateExceeded.setObjects(*((_A,_C),(_A,_P),(_A,_H),(_A,_L),(_A,_D),(_A,_F),(_A,_G),(_A,_I),(_A,_K)))
if mibBuilder.loadTexts:wlsxFrameBandWidthRateExceeded.setStatus(_B)
wlsxFrameLowSpeedRateExceeded=NotificationType((1,3,6,1,4,1,14823,2,3,3,1,200,2,1078))
wlsxFrameLowSpeedRateExceeded.setObjects(*((_A,_C),(_A,_P),(_A,_H),(_A,_L),(_A,_D),(_A,_F),(_A,_G),(_A,_I),(_A,_K)))
if mibBuilder.loadTexts:wlsxFrameLowSpeedRateExceeded.setStatus(_B)
wlsxFrameNonUnicastRateExceeded=NotificationType((1,3,6,1,4,1,14823,2,3,3,1,200,2,1079))
wlsxFrameNonUnicastRateExceeded.setObjects(*((_A,_C),(_A,_P),(_A,_H),(_A,_L),(_A,_D),(_A,_F),(_A,_G),(_A,_I),(_A,_K)))
if mibBuilder.loadTexts:wlsxFrameNonUnicastRateExceeded.setStatus(_B)
wlsxLoadbalancingEnabled=NotificationType((1,3,6,1,4,1,14823,2,3,3,1,200,2,1080))
wlsxLoadbalancingEnabled.setObjects(*((_A,_C),(_A,_H),(_A,_L),(_A,_D),(_A,_F),(_A,_G),(_A,_I)))
if mibBuilder.loadTexts:wlsxLoadbalancingEnabled.setStatus(_B)
wlsxLoadbalancingDisabled=NotificationType((1,3,6,1,4,1,14823,2,3,3,1,200,2,1081))
wlsxLoadbalancingDisabled.setObjects(*((_A,_C),(_A,_H),(_A,_L),(_A,_D),(_A,_F),(_A,_G),(_A,_I)))
if mibBuilder.loadTexts:wlsxLoadbalancingDisabled.setStatus(_B)
wlsxChannelFrameRetryRateExceeded=NotificationType((1,3,6,1,4,1,14823,2,3,3,1,200,2,1082))
wlsxChannelFrameRetryRateExceeded.setObjects(*((_A,_C),(_A,_D),(_A,_F),(_A,_G),(_A,_I),(_A,_K)))
if mibBuilder.loadTexts:wlsxChannelFrameRetryRateExceeded.setStatus(_B)
wlsxChannelFrameFragmentationRateExceeded=NotificationType((1,3,6,1,4,1,14823,2,3,3,1,200,2,1083))
wlsxChannelFrameFragmentationRateExceeded.setObjects(*((_A,_C),(_A,_D),(_A,_F),(_A,_G),(_A,_I),(_A,_K)))
if mibBuilder.loadTexts:wlsxChannelFrameFragmentationRateExceeded.setStatus(_B)
wlsxChannelFrameErrorRateExceeded=NotificationType((1,3,6,1,4,1,14823,2,3,3,1,200,2,1084))
wlsxChannelFrameErrorRateExceeded.setObjects(*((_A,_C),(_A,_D),(_A,_F),(_A,_G),(_A,_I),(_A,_K)))
if mibBuilder.loadTexts:wlsxChannelFrameErrorRateExceeded.setStatus(_B)
wlsxSignatureMatchAP=NotificationType((1,3,6,1,4,1,14823,2,3,3,1,200,2,1085))
wlsxSignatureMatchAP.setObjects(*((_A,_C),(_A,_Q),(_A,_H),(_A,_L),(_A,_M),(_A,_D),(_A,_F),(_A,_G)))
if mibBuilder.loadTexts:wlsxSignatureMatchAP.setStatus(_B)
wlsxSignatureMatchSta=NotificationType((1,3,6,1,4,1,14823,2,3,3,1,200,2,1086))
wlsxSignatureMatchSta.setObjects(*((_A,_C),(_A,_Q),(_A,_O),(_A,_M),(_A,_D),(_A,_F),(_A,_G)))
if mibBuilder.loadTexts:wlsxSignatureMatchSta.setStatus(_B)
wlsxChannelRateAnomaly=NotificationType((1,3,6,1,4,1,14823,2,3,3,1,200,2,1087))
wlsxChannelRateAnomaly.setObjects(*((_A,_C),(_A,_X),(_A,_D),(_A,_F),(_A,_G),(_A,_I),(_A,_K)))
if mibBuilder.loadTexts:wlsxChannelRateAnomaly.setStatus(_B)
wlsxNodeRateAnomalyAP=NotificationType((1,3,6,1,4,1,14823,2,3,3,1,200,2,1088))
wlsxNodeRateAnomalyAP.setObjects(*((_A,_C),(_A,_X),(_A,_H),(_A,_L),(_A,_M),(_A,_D),(_A,_F),(_A,_G)))
if mibBuilder.loadTexts:wlsxNodeRateAnomalyAP.setStatus(_B)
wlsxNodeRateAnomalySta=NotificationType((1,3,6,1,4,1,14823,2,3,3,1,200,2,1089))
wlsxNodeRateAnomalySta.setObjects(*((_A,_C),(_A,_X),(_A,_P),(_A,_M),(_A,_D),(_A,_F),(_A,_G)))
if mibBuilder.loadTexts:wlsxNodeRateAnomalySta.setStatus(_B)
wlsxEAPRateAnomaly=NotificationType((1,3,6,1,4,1,14823,2,3,3,1,200,2,1090))
wlsxEAPRateAnomaly.setObjects(*((_A,_C),(_A,_D),(_A,_F),(_A,_G),(_A,_I),(_A,_K)))
if mibBuilder.loadTexts:wlsxEAPRateAnomaly.setStatus(_B)
wlsxSignalAnomaly=NotificationType((1,3,6,1,4,1,14823,2,3,3,1,200,2,1091))
wlsxSignalAnomaly.setObjects(*((_A,_C),(_A,_D),(_A,_F),(_A,_G),(_A,_I)))
if mibBuilder.loadTexts:wlsxSignalAnomaly.setStatus(_B)
wlsxSequenceNumberAnomalyAP=NotificationType((1,3,6,1,4,1,14823,2,3,3,1,200,2,1092))
wlsxSequenceNumberAnomalyAP.setObjects(*((_A,_C),(_A,_H),(_A,_L),(_A,_M),(_A,_D),(_A,_F),(_A,_G)))
if mibBuilder.loadTexts:wlsxSequenceNumberAnomalyAP.setStatus(_B)
wlsxSequenceNumberAnomalySta=NotificationType((1,3,6,1,4,1,14823,2,3,3,1,200,2,1093))
wlsxSequenceNumberAnomalySta.setObjects(*((_A,_C),(_A,_O),(_A,_M),(_A,_D),(_A,_F),(_A,_G)))
if mibBuilder.loadTexts:wlsxSequenceNumberAnomalySta.setStatus(_B)
wlsxDisconnectStationAttack=NotificationType((1,3,6,1,4,1,14823,2,3,3,1,200,2,1094))
wlsxDisconnectStationAttack.setObjects(*((_A,_C),(_A,_X),(_A,_O),(_A,_M),(_A,_D),(_A,_F),(_A,_G)))
if mibBuilder.loadTexts:wlsxDisconnectStationAttack.setStatus(_B)
wlsxApFloodAttack=NotificationType((1,3,6,1,4,1,14823,2,3,3,1,200,2,1095))
wlsxApFloodAttack.setObjects(*((_A,_C),(_A,_D),(_A,_F),(_A,_G)))
if mibBuilder.loadTexts:wlsxApFloodAttack.setStatus(_B)
wlsxAdhocNetwork=NotificationType((1,3,6,1,4,1,14823,2,3,3,1,200,2,1096))
wlsxAdhocNetwork.setObjects(*((_A,_C),(_A,_O),(_A,_H),(_A,_L),(_A,_M),(_A,_D),(_A,_F),(_A,_G)))
if mibBuilder.loadTexts:wlsxAdhocNetwork.setStatus(_B)
wlsxWirelessBridge=NotificationType((1,3,6,1,4,1,14823,2,3,3,1,200,2,1097))
wlsxWirelessBridge.setObjects(*((_A,_C),(_A,_W),(_A,_R),(_A,_M),(_A,_D),(_A,_F),(_A,_G)))
if mibBuilder.loadTexts:wlsxWirelessBridge.setStatus(_B)
wlsxInvalidMacOUIAP=NotificationType((1,3,6,1,4,1,14823,2,3,3,1,200,2,1098))
wlsxInvalidMacOUIAP.setObjects(*((_A,_C),(_A,_v),(_A,_H),(_A,_L),(_A,_M),(_A,_D),(_A,_F),(_A,_G)))
if mibBuilder.loadTexts:wlsxInvalidMacOUIAP.setStatus(_B)
wlsxInvalidMacOUISta=NotificationType((1,3,6,1,4,1,14823,2,3,3,1,200,2,1099))
wlsxInvalidMacOUISta.setObjects(*((_A,_C),(_A,_v),(_A,_P),(_A,_M),(_A,_D),(_A,_F),(_A,_G)))
if mibBuilder.loadTexts:wlsxInvalidMacOUISta.setStatus(_B)
wlsxWEPMisconfiguration=NotificationType((1,3,6,1,4,1,14823,2,3,3,1,200,2,1100))
wlsxWEPMisconfiguration.setObjects(*((_A,_C),(_A,_H),(_A,_L),(_A,_D),(_A,_F),(_A,_G),(_A,_I),(_A,_K)))
if mibBuilder.loadTexts:wlsxWEPMisconfiguration.setStatus(_B)
wlsxStaRepeatWEPIVViolation=NotificationType((1,3,6,1,4,1,14823,2,3,3,1,200,2,1101))
wlsxStaRepeatWEPIVViolation.setObjects(*((_A,_C),(_A,_H),(_A,_L),(_A,_P),(_A,_D),(_A,_F),(_A,_G),(_A,_I),(_A,_K)))
if mibBuilder.loadTexts:wlsxStaRepeatWEPIVViolation.setStatus(_B)
wlsxStaWeakWEPIVViolation=NotificationType((1,3,6,1,4,1,14823,2,3,3,1,200,2,1102))
wlsxStaWeakWEPIVViolation.setObjects(*((_A,_C),(_A,_H),(_A,_L),(_A,_P),(_A,_D),(_A,_F),(_A,_G),(_A,_I),(_A,_K)))
if mibBuilder.loadTexts:wlsxStaWeakWEPIVViolation.setStatus(_B)
wlsxStaAssociatedToUnsecureAP=NotificationType((1,3,6,1,4,1,14823,2,3,3,1,200,2,1103))
wlsxStaAssociatedToUnsecureAP.setObjects(*((_A,_C),(_A,_H),(_A,_L),(_A,_D),(_A,_F),(_A,_P),(_A,_G),(_A,_I),(_A,_m),(_A,_K)))
if mibBuilder.loadTexts:wlsxStaAssociatedToUnsecureAP.setStatus(_B)
wlsxStaUnAssociatedFromUnsecureAP=NotificationType((1,3,6,1,4,1,14823,2,3,3,1,200,2,1104))
wlsxStaUnAssociatedFromUnsecureAP.setObjects(*((_A,_C),(_A,_H),(_A,_L),(_A,_D),(_A,_F),(_A,_P)))
if mibBuilder.loadTexts:wlsxStaUnAssociatedFromUnsecureAP.setStatus(_B)
wlsxAdhocNetworkBridgeDetected=NotificationType((1,3,6,1,4,1,14823,2,3,3,1,200,2,1105))
wlsxAdhocNetworkBridgeDetected.setObjects(*((_A,_C),(_A,_O),(_A,_H),(_A,_L),(_A,_D),(_A,_F),(_A,_G),(_A,_I)))
if mibBuilder.loadTexts:wlsxAdhocNetworkBridgeDetected.setStatus(_B)
wlsxInterferingApDetected=NotificationType((1,3,6,1,4,1,14823,2,3,3,1,200,2,1106))
wlsxInterferingApDetected.setObjects(*((_A,_C),(_A,_H),(_A,_L),(_A,_D),(_A,_F),(_A,_G),(_A,_I),(_A,_Ad),(_A,_K)))
if mibBuilder.loadTexts:wlsxInterferingApDetected.setStatus(_B)
wlsxColdStart=NotificationType((1,3,6,1,4,1,14823,2,3,3,1,200,2,1111))
wlsxColdStart.setObjects((_A,_C))
if mibBuilder.loadTexts:wlsxColdStart.setStatus(_B)
wlsxWarmStart=NotificationType((1,3,6,1,4,1,14823,2,3,3,1,200,2,1112))
wlsxWarmStart.setObjects((_A,_C))
if mibBuilder.loadTexts:wlsxWarmStart.setStatus(_B)
wlsxAPImpersonation=NotificationType((1,3,6,1,4,1,14823,2,3,3,1,200,2,1113))
wlsxAPImpersonation.setObjects(*((_A,_C),(_A,_H),(_A,_L),(_A,_D),(_A,_F),(_A,_G),(_A,_I),(_A,_K)))
if mibBuilder.loadTexts:wlsxAPImpersonation.setStatus(_B)
wlsxNAuthServerIsDown=NotificationType((1,3,6,1,4,1,14823,2,3,3,1,200,2,1115))
wlsxNAuthServerIsDown.setObjects(*((_A,_C),(_A,_Z),(_A,_e)))
if mibBuilder.loadTexts:wlsxNAuthServerIsDown.setStatus(_B)
wlsxWindowsBridgeDetected=NotificationType((1,3,6,1,4,1,14823,2,3,3,1,200,2,1129))
wlsxWindowsBridgeDetected.setObjects(*((_A,_C),(_A,_O),(_A,_H),(_A,_L),(_A,_D),(_A,_F),(_A,_G),(_A,_I),(_A,_K)))
if mibBuilder.loadTexts:wlsxWindowsBridgeDetected.setStatus(_B)
wlsxSignAPNetstumbler=NotificationType((1,3,6,1,4,1,14823,2,3,3,1,200,2,1134))
wlsxSignAPNetstumbler.setObjects(*((_A,_C),(_A,_Q),(_A,_H),(_A,_L),(_A,_M),(_A,_D),(_A,_F),(_A,_G)))
if mibBuilder.loadTexts:wlsxSignAPNetstumbler.setStatus(_B)
wlsxSignStaNetstumbler=NotificationType((1,3,6,1,4,1,14823,2,3,3,1,200,2,1135))
wlsxSignStaNetstumbler.setObjects(*((_A,_C),(_A,_Q),(_A,_O),(_A,_M),(_A,_D),(_A,_F),(_A,_G)))
if mibBuilder.loadTexts:wlsxSignStaNetstumbler.setStatus(_B)
wlsxSignAPAsleap=NotificationType((1,3,6,1,4,1,14823,2,3,3,1,200,2,1136))
wlsxSignAPAsleap.setObjects(*((_A,_C),(_A,_Q),(_A,_H),(_A,_L),(_A,_M),(_A,_D),(_A,_F),(_A,_G)))
if mibBuilder.loadTexts:wlsxSignAPAsleap.setStatus(_B)
wlsxSignStaAsleap=NotificationType((1,3,6,1,4,1,14823,2,3,3,1,200,2,1137))
wlsxSignStaAsleap.setObjects(*((_A,_C),(_A,_Q),(_A,_O),(_A,_M),(_A,_D),(_A,_F),(_A,_G)))
if mibBuilder.loadTexts:wlsxSignStaAsleap.setStatus(_B)
wlsxSignAPAirjack=NotificationType((1,3,6,1,4,1,14823,2,3,3,1,200,2,1138))
wlsxSignAPAirjack.setObjects(*((_A,_C),(_A,_Q),(_A,_H),(_A,_L),(_A,_M),(_A,_D),(_A,_F),(_A,_G)))
if mibBuilder.loadTexts:wlsxSignAPAirjack.setStatus(_B)
wlsxSignStaAirjack=NotificationType((1,3,6,1,4,1,14823,2,3,3,1,200,2,1139))
wlsxSignStaAirjack.setObjects(*((_A,_C),(_A,_Q),(_A,_O),(_A,_M),(_A,_D),(_A,_F),(_A,_G)))
if mibBuilder.loadTexts:wlsxSignStaAirjack.setStatus(_B)
wlsxSignAPNullProbeResp=NotificationType((1,3,6,1,4,1,14823,2,3,3,1,200,2,1140))
wlsxSignAPNullProbeResp.setObjects(*((_A,_C),(_A,_Q),(_A,_H),(_A,_L),(_A,_M),(_A,_D),(_A,_F),(_A,_G)))
if mibBuilder.loadTexts:wlsxSignAPNullProbeResp.setStatus(_B)
wlsxSignStaNullProbeResp=NotificationType((1,3,6,1,4,1,14823,2,3,3,1,200,2,1141))
wlsxSignStaNullProbeResp.setObjects(*((_A,_C),(_A,_Q),(_A,_O),(_A,_M),(_A,_D),(_A,_F),(_A,_G)))
if mibBuilder.loadTexts:wlsxSignStaNullProbeResp.setStatus(_B)
wlsxSignAPDeauthBcast=NotificationType((1,3,6,1,4,1,14823,2,3,3,1,200,2,1142))
wlsxSignAPDeauthBcast.setObjects(*((_A,_C),(_A,_Q),(_A,_H),(_A,_L),(_A,_M),(_A,_D),(_A,_F),(_A,_G)))
if mibBuilder.loadTexts:wlsxSignAPDeauthBcast.setStatus(_B)
wlsxSignStaDeauthBcast=NotificationType((1,3,6,1,4,1,14823,2,3,3,1,200,2,1143))
wlsxSignStaDeauthBcast.setObjects(*((_A,_C),(_A,_Q),(_A,_O),(_A,_M),(_A,_D),(_A,_F),(_A,_G)))
if mibBuilder.loadTexts:wlsxSignStaDeauthBcast.setStatus(_B)
wlsxWindowsBridgeDetectedAP=NotificationType((1,3,6,1,4,1,14823,2,3,3,1,200,2,1144))
wlsxWindowsBridgeDetectedAP.setObjects(*((_A,_C),(_A,_H),(_A,_L),(_A,_D),(_A,_F),(_A,_G),(_A,_I),(_A,_K)))
if mibBuilder.loadTexts:wlsxWindowsBridgeDetectedAP.setStatus(_B)
wlsxWindowsBridgeDetectedSta=NotificationType((1,3,6,1,4,1,14823,2,3,3,1,200,2,1145))
wlsxWindowsBridgeDetectedSta.setObjects(*((_A,_C),(_A,_O),(_A,_H),(_A,_L),(_A,_D),(_A,_F),(_A,_G),(_A,_I),(_A,_K)))
if mibBuilder.loadTexts:wlsxWindowsBridgeDetectedSta.setStatus(_B)
wlsxAdhocNetworkBridgeDetectedAP=NotificationType((1,3,6,1,4,1,14823,2,3,3,1,200,2,1146))
wlsxAdhocNetworkBridgeDetectedAP.setObjects(*((_A,_C),(_A,_H),(_A,_L),(_A,_D),(_A,_F),(_A,_G),(_A,_I)))
if mibBuilder.loadTexts:wlsxAdhocNetworkBridgeDetectedAP.setStatus(_B)
wlsxAdhocNetworkBridgeDetectedSta=NotificationType((1,3,6,1,4,1,14823,2,3,3,1,200,2,1147))
wlsxAdhocNetworkBridgeDetectedSta.setObjects(*((_A,_C),(_A,_O),(_A,_H),(_A,_L),(_A,_D),(_A,_F),(_A,_G),(_A,_I)))
if mibBuilder.loadTexts:wlsxAdhocNetworkBridgeDetectedSta.setStatus(_B)
wlsxDisconnectStationAttackAP=NotificationType((1,3,6,1,4,1,14823,2,3,3,1,200,2,1148))
wlsxDisconnectStationAttackAP.setObjects(*((_A,_C),(_A,_X),(_A,_H),(_A,_L),(_A,_M),(_A,_D),(_A,_F),(_A,_G)))
if mibBuilder.loadTexts:wlsxDisconnectStationAttackAP.setStatus(_B)
wlsxDisconnectStationAttackSta=NotificationType((1,3,6,1,4,1,14823,2,3,3,1,200,2,1149))
wlsxDisconnectStationAttackSta.setObjects(*((_A,_C),(_A,_X),(_A,_O),(_A,_M),(_A,_D),(_A,_F),(_A,_G)))
if mibBuilder.loadTexts:wlsxDisconnectStationAttackSta.setStatus(_B)
wlsxSuspectUnsecureAPDetected=NotificationType((1,3,6,1,4,1,14823,2,3,3,1,200,2,1150))
wlsxSuspectUnsecureAPDetected.setObjects(*((_A,_C),(_A,_H),(_A,_L),(_A,_F),(_A,_t),(_A,_u),(_A,_w),(_A,_G),(_A,_m)))
if mibBuilder.loadTexts:wlsxSuspectUnsecureAPDetected.setStatus(_B)
wlsxSuspectUnsecureAPResolved=NotificationType((1,3,6,1,4,1,14823,2,3,3,1,200,2,1151))
wlsxSuspectUnsecureAPResolved.setObjects(*((_A,_C),(_A,_H),(_A,_L),(_A,_F)))
if mibBuilder.loadTexts:wlsxSuspectUnsecureAPResolved.setStatus(_B)
wlsxHtGreenfieldSupported=NotificationType((1,3,6,1,4,1,14823,2,3,3,1,200,2,1157))
wlsxHtGreenfieldSupported.setObjects(*((_A,_C),(_A,_H),(_A,_L),(_A,_D),(_A,_F),(_A,_G),(_A,_I),(_A,_K)))
if mibBuilder.loadTexts:wlsxHtGreenfieldSupported.setStatus(_B)
wlsxHT40MHzIntoleranceAP=NotificationType((1,3,6,1,4,1,14823,2,3,3,1,200,2,1158))
wlsxHT40MHzIntoleranceAP.setObjects(*((_A,_C),(_A,_H),(_A,_L),(_A,_D),(_A,_F),(_A,_G),(_A,_I),(_A,_K)))
if mibBuilder.loadTexts:wlsxHT40MHzIntoleranceAP.setStatus(_B)
wlsxHT40MHzIntoleranceSta=NotificationType((1,3,6,1,4,1,14823,2,3,3,1,200,2,1159))
wlsxHT40MHzIntoleranceSta.setObjects(*((_A,_C),(_A,_O),(_A,_M),(_A,_I),(_A,_X),(_A,_D),(_A,_F),(_A,_G),(_A,_K)))
if mibBuilder.loadTexts:wlsxHT40MHzIntoleranceSta.setStatus(_B)
wlsxNAuthServerAllInService=NotificationType((1,3,6,1,4,1,14823,2,3,3,1,200,2,1160))
wlsxNAuthServerAllInService.setObjects(*((_A,_C),(_A,_Ae)))
if mibBuilder.loadTexts:wlsxNAuthServerAllInService.setStatus(_B)
wlsxNAdhocNetwork=NotificationType((1,3,6,1,4,1,14823,2,3,3,1,200,2,1161))
wlsxNAdhocNetwork.setObjects(*((_A,_C),(_A,_O),(_A,_H),(_A,_L),(_A,_M),(_A,_D),(_A,_F),(_A,_G),(_A,_I),(_A,_K)))
if mibBuilder.loadTexts:wlsxNAdhocNetwork.setStatus(_B)
wlsxNAdhocNetworkBridgeDetectedAP=NotificationType((1,3,6,1,4,1,14823,2,3,3,1,200,2,1162))
wlsxNAdhocNetworkBridgeDetectedAP.setObjects(*((_A,_C),(_A,_H),(_A,_L),(_A,_M),(_A,_D),(_A,_F),(_A,_G),(_A,_I),(_A,_K)))
if mibBuilder.loadTexts:wlsxNAdhocNetworkBridgeDetectedAP.setStatus(_B)
wlsxNAdhocNetworkBridgeDetectedSta=NotificationType((1,3,6,1,4,1,14823,2,3,3,1,200,2,1163))
wlsxNAdhocNetworkBridgeDetectedSta.setObjects(*((_A,_C),(_A,_O),(_A,_H),(_A,_L),(_A,_M),(_A,_D),(_A,_F),(_A,_G),(_A,_I),(_A,_K)))
if mibBuilder.loadTexts:wlsxNAdhocNetworkBridgeDetectedSta.setStatus(_B)
wlsxClientFloodAttack=NotificationType((1,3,6,1,4,1,14823,2,3,3,1,200,2,1170))
wlsxClientFloodAttack.setObjects(*((_A,_C),(_A,_D),(_A,_F),(_A,_G)))
if mibBuilder.loadTexts:wlsxClientFloodAttack.setStatus(_B)
wlsxValidClientNotUsingEncryption=NotificationType((1,3,6,1,4,1,14823,2,3,3,1,200,2,1171))
wlsxValidClientNotUsingEncryption.setObjects(*((_A,_C),(_A,_H),(_A,_O),(_A,_R),(_A,_P),(_A,_M),(_A,_D),(_A,_F),(_A,_G),(_A,_I)))
if mibBuilder.loadTexts:wlsxValidClientNotUsingEncryption.setStatus(_B)
wlsxAdhocUsingValidSSID=NotificationType((1,3,6,1,4,1,14823,2,3,3,1,200,2,1172))
wlsxAdhocUsingValidSSID.setObjects(*((_A,_C),(_A,_H),(_A,_L),(_A,_M),(_A,_D),(_A,_F),(_A,_G),(_A,_I)))
if mibBuilder.loadTexts:wlsxAdhocUsingValidSSID.setStatus(_B)
wlsxAPSpoofingDetected=NotificationType((1,3,6,1,4,1,14823,2,3,3,1,200,2,1173))
wlsxAPSpoofingDetected.setObjects(*((_A,_C),(_A,_H),(_A,_O),(_A,_R),(_A,_x),(_A,_M),(_A,_D),(_A,_F),(_A,_G),(_A,_I),(_A,_K)))
if mibBuilder.loadTexts:wlsxAPSpoofingDetected.setStatus(_B)
wlsxClientAssociatingOnWrongChannel=NotificationType((1,3,6,1,4,1,14823,2,3,3,1,200,2,1174))
wlsxClientAssociatingOnWrongChannel.setObjects(*((_A,_C),(_A,_H),(_A,_O),(_A,_R),(_A,_x),(_A,_M),(_A,_D),(_A,_F),(_A,_G),(_A,_I),(_A,_K)))
if mibBuilder.loadTexts:wlsxClientAssociatingOnWrongChannel.setStatus(_B)
wlsxNDisconnectStationAttack=NotificationType((1,3,6,1,4,1,14823,2,3,3,1,200,2,1175))
wlsxNDisconnectStationAttack.setObjects(*((_A,_C),(_A,_H),(_A,_L),(_A,_O),(_A,_M),(_A,_D),(_A,_F),(_A,_G),(_A,_I),(_A,_K)))
if mibBuilder.loadTexts:wlsxNDisconnectStationAttack.setStatus(_B)
wlsxNStaUnAssociatedFromUnsecureAP=NotificationType((1,3,6,1,4,1,14823,2,3,3,1,200,2,1176))
wlsxNStaUnAssociatedFromUnsecureAP.setObjects(*((_A,_C),(_A,_H),(_A,_L),(_A,_D),(_A,_F),(_A,_P),(_A,_G),(_A,_I),(_A,_K)))
if mibBuilder.loadTexts:wlsxNStaUnAssociatedFromUnsecureAP.setStatus(_B)
wlsxOmertaAttack=NotificationType((1,3,6,1,4,1,14823,2,3,3,1,200,2,1177))
wlsxOmertaAttack.setObjects(*((_A,_C),(_A,_H),(_A,_L),(_A,_P),(_A,_M),(_A,_D),(_A,_F),(_A,_G),(_A,_I),(_A,_K)))
if mibBuilder.loadTexts:wlsxOmertaAttack.setStatus(_B)
wlsxTKIPReplayAttack=NotificationType((1,3,6,1,4,1,14823,2,3,3,1,200,2,1178))
wlsxTKIPReplayAttack.setObjects(*((_A,_C),(_A,_D),(_A,_F),(_A,_G),(_A,_O),(_A,_R),(_A,_H),(_A,_I),(_A,_M),(_A,_K)))
if mibBuilder.loadTexts:wlsxTKIPReplayAttack.setStatus(_B)
wlsxChopChopAttack=NotificationType((1,3,6,1,4,1,14823,2,3,3,1,200,2,1179))
wlsxChopChopAttack.setObjects(*((_A,_C),(_A,_D),(_A,_F),(_A,_G),(_A,_O),(_A,_R),(_A,_H),(_A,_I),(_A,_M),(_A,_K)))
if mibBuilder.loadTexts:wlsxChopChopAttack.setStatus(_B)
wlsxFataJackAttack=NotificationType((1,3,6,1,4,1,14823,2,3,3,1,200,2,1180))
wlsxFataJackAttack.setObjects(*((_A,_C),(_A,_H),(_A,_L),(_A,_P),(_A,_M),(_A,_D),(_A,_F),(_A,_G),(_A,_I),(_A,_K)))
if mibBuilder.loadTexts:wlsxFataJackAttack.setStatus(_B)
wlsxInvalidAddressCombination=NotificationType((1,3,6,1,4,1,14823,2,3,3,1,200,2,1181))
wlsxInvalidAddressCombination.setObjects(*((_A,_C),(_A,_D),(_A,_F),(_A,_G),(_A,_O),(_A,_R),(_A,_I),(_A,_M),(_A,_K)))
if mibBuilder.loadTexts:wlsxInvalidAddressCombination.setStatus(_B)
wlsxValidClientMisassociation=NotificationType((1,3,6,1,4,1,14823,2,3,3,1,200,2,1182))
wlsxValidClientMisassociation.setObjects(*((_A,_C),(_A,_H),(_A,_L),(_A,_P),(_A,_Af),(_A,_M),(_A,_D),(_A,_F),(_A,_G),(_A,_I),(_A,_K)))
if mibBuilder.loadTexts:wlsxValidClientMisassociation.setStatus(_B)
wlsxMalformedHTIEDetected=NotificationType((1,3,6,1,4,1,14823,2,3,3,1,200,2,1183))
wlsxMalformedHTIEDetected.setObjects(*((_A,_C),(_A,_D),(_A,_F),(_A,_G),(_A,_O),(_A,_R),(_A,_H),(_A,_I),(_A,_M),(_A,_K)))
if mibBuilder.loadTexts:wlsxMalformedHTIEDetected.setStatus(_B)
wlsxMalformedAssocReqDetected=NotificationType((1,3,6,1,4,1,14823,2,3,3,1,200,2,1184))
wlsxMalformedAssocReqDetected.setObjects(*((_A,_C),(_A,_D),(_A,_F),(_A,_G),(_A,_O),(_A,_R),(_A,_H),(_A,_I),(_A,_M),(_A,_K)))
if mibBuilder.loadTexts:wlsxMalformedAssocReqDetected.setStatus(_B)
wlsxOverflowIEDetected=NotificationType((1,3,6,1,4,1,14823,2,3,3,1,200,2,1185))
wlsxOverflowIEDetected.setObjects(*((_A,_C),(_A,_D),(_A,_F),(_A,_G),(_A,_O),(_A,_R),(_A,_H),(_A,_I),(_A,_M),(_A,_K)))
if mibBuilder.loadTexts:wlsxOverflowIEDetected.setStatus(_B)
wlsxOverflowEAPOLKeyDetected=NotificationType((1,3,6,1,4,1,14823,2,3,3,1,200,2,1186))
wlsxOverflowEAPOLKeyDetected.setObjects(*((_A,_C),(_A,_D),(_A,_F),(_A,_G),(_A,_O),(_A,_R),(_A,_H),(_A,_I),(_A,_M),(_A,_K)))
if mibBuilder.loadTexts:wlsxOverflowEAPOLKeyDetected.setStatus(_B)
wlsxMalformedFrameLargeDurationDetected=NotificationType((1,3,6,1,4,1,14823,2,3,3,1,200,2,1187))
wlsxMalformedFrameLargeDurationDetected.setObjects(*((_A,_C),(_A,_D),(_A,_F),(_A,_G),(_A,_O),(_A,_I),(_A,_M),(_A,_K)))
if mibBuilder.loadTexts:wlsxMalformedFrameLargeDurationDetected.setStatus(_B)
wlsxMalformedFrameWrongChannelDetected=NotificationType((1,3,6,1,4,1,14823,2,3,3,1,200,2,1188))
wlsxMalformedFrameWrongChannelDetected.setObjects(*((_A,_C),(_A,_D),(_A,_F),(_A,_G),(_A,_O),(_A,_H),(_A,_L),(_A,_j),(_A,_I),(_A,_M),(_A,_K),(_A,_y)))
if mibBuilder.loadTexts:wlsxMalformedFrameWrongChannelDetected.setStatus(_B)
wlsxMalformedAuthFrame=NotificationType((1,3,6,1,4,1,14823,2,3,3,1,200,2,1189))
wlsxMalformedAuthFrame.setObjects(*((_A,_C),(_A,_H),(_A,_L),(_A,_P),(_A,_M),(_A,_D),(_A,_F),(_A,_G),(_A,_I),(_A,_K)))
if mibBuilder.loadTexts:wlsxMalformedAuthFrame.setStatus(_B)
wlsxCTSRateAnomaly=NotificationType((1,3,6,1,4,1,14823,2,3,3,1,200,2,1190))
wlsxCTSRateAnomaly.setObjects(*((_A,_C),(_A,_D),(_A,_F),(_A,_G),(_A,_I),(_A,_K)))
if mibBuilder.loadTexts:wlsxCTSRateAnomaly.setStatus(_B)
wlsxRTSRateAnomaly=NotificationType((1,3,6,1,4,1,14823,2,3,3,1,200,2,1191))
wlsxRTSRateAnomaly.setObjects(*((_A,_C),(_A,_D),(_A,_F),(_A,_G),(_A,_I),(_A,_K)))
if mibBuilder.loadTexts:wlsxRTSRateAnomaly.setStatus(_B)
wlsxNRogueAPDetected=NotificationType((1,3,6,1,4,1,14823,2,3,3,1,200,2,1192))
wlsxNRogueAPDetected.setObjects(*((_A,_C),(_A,_H),(_A,_L),(_A,_I),(_A,_K)))
if mibBuilder.loadTexts:wlsxNRogueAPDetected.setStatus(_B)
wlsxNRogueAPResolved=NotificationType((1,3,6,1,4,1,14823,2,3,3,1,200,2,1193))
wlsxNRogueAPResolved.setObjects(*((_A,_C),(_A,_H),(_A,_L),(_A,_I),(_A,_K)))
if mibBuilder.loadTexts:wlsxNRogueAPResolved.setStatus(_B)
wlsxNeighborAPDetected=NotificationType((1,3,6,1,4,1,14823,2,3,3,1,200,2,1194))
wlsxNeighborAPDetected.setObjects(*((_A,_C),(_A,_H),(_A,_L),(_A,_I),(_A,_K)))
if mibBuilder.loadTexts:wlsxNeighborAPDetected.setStatus(_B)
wlsxNInterferingAPDetected=NotificationType((1,3,6,1,4,1,14823,2,3,3,1,200,2,1195))
wlsxNInterferingAPDetected.setObjects(*((_A,_C),(_A,_H),(_A,_L),(_A,_I),(_A,_K)))
if mibBuilder.loadTexts:wlsxNInterferingAPDetected.setStatus(_B)
wlsxNSuspectRogueAPDetected=NotificationType((1,3,6,1,4,1,14823,2,3,3,1,200,2,1196))
wlsxNSuspectRogueAPDetected.setObjects(*((_A,_C),(_A,_H),(_A,_L),(_A,_I),(_A,_w),(_A,_K)))
if mibBuilder.loadTexts:wlsxNSuspectRogueAPDetected.setStatus(_B)
wlsxNSuspectRogueAPResolved=NotificationType((1,3,6,1,4,1,14823,2,3,3,1,200,2,1197))
wlsxNSuspectRogueAPResolved.setObjects(*((_A,_C),(_A,_H),(_A,_L),(_A,_I),(_A,_K)))
if mibBuilder.loadTexts:wlsxNSuspectRogueAPResolved.setStatus(_B)
wlsxBlockAckAttackDetected=NotificationType((1,3,6,1,4,1,14823,2,3,3,1,200,2,1198))
wlsxBlockAckAttackDetected.setObjects(*((_A,_C),(_A,_D),(_A,_F),(_A,_G),(_A,_O),(_A,_R),(_A,_H),(_A,_I),(_A,_M),(_A,_K)))
if mibBuilder.loadTexts:wlsxBlockAckAttackDetected.setStatus(_B)
wlsxHotspotterAttackDetected=NotificationType((1,3,6,1,4,1,14823,2,3,3,1,200,2,1199))
wlsxHotspotterAttackDetected.setObjects(*((_A,_C),(_A,_D),(_A,_F),(_A,_G),(_A,_P),(_A,_O),(_A,_H),(_A,_I),(_A,_M),(_A,_L),(_A,_K)))
if mibBuilder.loadTexts:wlsxHotspotterAttackDetected.setStatus(_B)
wlsxNSignatureMatch=NotificationType((1,3,6,1,4,1,14823,2,3,3,1,200,2,1200))
wlsxNSignatureMatch.setObjects(*((_A,_C),(_A,_H),(_A,_W),(_A,_R),(_A,_Q),(_A,_M),(_A,_D),(_A,_F),(_A,_G),(_A,_I),(_A,_K)))
if mibBuilder.loadTexts:wlsxNSignatureMatch.setStatus(_B)
wlsxNSignatureMatchNetstumbler=NotificationType((1,3,6,1,4,1,14823,2,3,3,1,200,2,1201))
wlsxNSignatureMatchNetstumbler.setObjects(*((_A,_C),(_A,_H),(_A,_W),(_A,_R),(_A,_Q),(_A,_M),(_A,_D),(_A,_F),(_A,_G),(_A,_I),(_A,_K)))
if mibBuilder.loadTexts:wlsxNSignatureMatchNetstumbler.setStatus(_B)
wlsxNSignatureMatchAsleap=NotificationType((1,3,6,1,4,1,14823,2,3,3,1,200,2,1202))
wlsxNSignatureMatchAsleap.setObjects(*((_A,_C),(_A,_H),(_A,_W),(_A,_R),(_A,_Q),(_A,_M),(_A,_D),(_A,_F),(_A,_G),(_A,_I),(_A,_K)))
if mibBuilder.loadTexts:wlsxNSignatureMatchAsleap.setStatus(_B)
wlsxNSignatureMatchAirjack=NotificationType((1,3,6,1,4,1,14823,2,3,3,1,200,2,1203))
wlsxNSignatureMatchAirjack.setObjects(*((_A,_C),(_A,_H),(_A,_W),(_A,_R),(_A,_Q),(_A,_M),(_A,_D),(_A,_F),(_A,_G),(_A,_I),(_A,_K)))
if mibBuilder.loadTexts:wlsxNSignatureMatchAirjack.setStatus(_B)
wlsxNSignatureMatchNullProbeResp=NotificationType((1,3,6,1,4,1,14823,2,3,3,1,200,2,1204))
wlsxNSignatureMatchNullProbeResp.setObjects(*((_A,_C),(_A,_H),(_A,_W),(_A,_R),(_A,_Q),(_A,_M),(_A,_D),(_A,_F),(_A,_G),(_A,_I),(_A,_K)))
if mibBuilder.loadTexts:wlsxNSignatureMatchNullProbeResp.setStatus(_B)
wlsxNSignatureMatchDeauthBcast=NotificationType((1,3,6,1,4,1,14823,2,3,3,1,200,2,1205))
wlsxNSignatureMatchDeauthBcast.setObjects(*((_A,_C),(_A,_H),(_A,_W),(_A,_R),(_A,_Q),(_A,_M),(_A,_D),(_A,_F),(_A,_G),(_A,_I),(_A,_K)))
if mibBuilder.loadTexts:wlsxNSignatureMatchDeauthBcast.setStatus(_B)
wlsxNSignatureMatchDisassocBcast=NotificationType((1,3,6,1,4,1,14823,2,3,3,1,200,2,1206))
wlsxNSignatureMatchDisassocBcast.setObjects(*((_A,_C),(_A,_H),(_A,_W),(_A,_R),(_A,_Q),(_A,_M),(_A,_D),(_A,_F),(_A,_G),(_A,_I),(_A,_K)))
if mibBuilder.loadTexts:wlsxNSignatureMatchDisassocBcast.setStatus(_B)
wlsxNSignatureMatchWellenreiter=NotificationType((1,3,6,1,4,1,14823,2,3,3,1,200,2,1207))
wlsxNSignatureMatchWellenreiter.setObjects(*((_A,_C),(_A,_H),(_A,_W),(_A,_R),(_A,_Q),(_A,_M),(_A,_D),(_A,_F),(_A,_G),(_A,_I),(_A,_K)))
if mibBuilder.loadTexts:wlsxNSignatureMatchWellenreiter.setStatus(_B)
wlsxAPDeauthContainment=NotificationType((1,3,6,1,4,1,14823,2,3,3,1,200,2,1208))
wlsxAPDeauthContainment.setObjects(*((_A,_C),(_A,_H),(_A,_P),(_A,_I),(_A,_D),(_A,_F),(_A,_G),(_A,_K)))
if mibBuilder.loadTexts:wlsxAPDeauthContainment.setStatus(_B)
wlsxClientDeauthContainment=NotificationType((1,3,6,1,4,1,14823,2,3,3,1,200,2,1209))
wlsxClientDeauthContainment.setObjects(*((_A,_C),(_A,_P),(_A,_H),(_A,_I),(_A,_D),(_A,_F),(_A,_G),(_A,_K)))
if mibBuilder.loadTexts:wlsxClientDeauthContainment.setStatus(_B)
wlsxAPWiredContainment=NotificationType((1,3,6,1,4,1,14823,2,3,3,1,200,2,1210))
wlsxAPWiredContainment.setObjects(*((_A,_C),(_A,_H),(_A,_P),(_A,_k),(_A,_l),(_A,_D),(_A,_F),(_A,_G)))
if mibBuilder.loadTexts:wlsxAPWiredContainment.setStatus(_B)
wlsxClientWiredContainment=NotificationType((1,3,6,1,4,1,14823,2,3,3,1,200,2,1211))
wlsxClientWiredContainment.setObjects(*((_A,_C),(_A,_P),(_A,_H),(_A,_k),(_A,_l),(_A,_D),(_A,_F),(_A,_G)))
if mibBuilder.loadTexts:wlsxClientWiredContainment.setStatus(_B)
wlsxAPTaggedWiredContainment=NotificationType((1,3,6,1,4,1,14823,2,3,3,1,200,2,1212))
wlsxAPTaggedWiredContainment.setObjects(*((_A,_C),(_A,_H),(_A,_P),(_A,_k),(_A,_l),(_A,_z),(_A,_D),(_A,_F),(_A,_G)))
if mibBuilder.loadTexts:wlsxAPTaggedWiredContainment.setStatus(_B)
wlsxClientTaggedWiredContainment=NotificationType((1,3,6,1,4,1,14823,2,3,3,1,200,2,1213))
wlsxClientTaggedWiredContainment.setObjects(*((_A,_C),(_A,_P),(_A,_H),(_A,_k),(_A,_l),(_A,_z),(_A,_D),(_A,_F),(_A,_G)))
if mibBuilder.loadTexts:wlsxClientTaggedWiredContainment.setStatus(_B)
wlsxTarpitContainment=NotificationType((1,3,6,1,4,1,14823,2,3,3,1,200,2,1214))
wlsxTarpitContainment.setObjects(*((_A,_C),(_A,_H),(_A,_P),(_A,_I),(_A,_j),(_A,_O),(_A,_D),(_A,_F),(_A,_G),(_A,_K),(_A,_y)))
if mibBuilder.loadTexts:wlsxTarpitContainment.setStatus(_B)
wlsxAPChannelChange=NotificationType((1,3,6,1,4,1,14823,2,3,3,1,200,2,1216))
wlsxAPChannelChange.setObjects(*((_A,_C),(_A,_I),(_A,_Ag),(_A,_Ah),(_A,_Ai),(_A,_D),(_A,_F),(_A,_G),(_A,_Aj),(_A,_s),(_A,_r),(_A,_Ak),(_A,_Al)))
if mibBuilder.loadTexts:wlsxAPChannelChange.setStatus(_B)
wlsxAPPowerChange=NotificationType((1,3,6,1,4,1,14823,2,3,3,1,200,2,1217))
wlsxAPPowerChange.setObjects(*((_A,_C),(_A,_q),(_A,_Am),(_A,_D),(_A,_F),(_A,_G)))
if mibBuilder.loadTexts:wlsxAPPowerChange.setStatus(_B)
wlsxAPModeChange=NotificationType((1,3,6,1,4,1,14823,2,3,3,1,200,2,1218))
wlsxAPModeChange.setObjects(*((_A,_C),(_A,_An),(_A,_Ao),(_A,_D),(_A,_F),(_A,_G)))
if mibBuilder.loadTexts:wlsxAPModeChange.setStatus(_B)
wlsxUserEntryAttributesChanged=NotificationType((1,3,6,1,4,1,14823,2,3,3,1,200,2,1219))
wlsxUserEntryAttributesChanged.setObjects(*((_A,_C),(_A,_V),(_A,_T),(_A,_Y),(_A,_S),(_A,_Ap),(_A,_n),(_A,_Aq)))
if mibBuilder.loadTexts:wlsxUserEntryAttributesChanged.setStatus(_B)
wlsxPowerSaveDosAttack=NotificationType((1,3,6,1,4,1,14823,2,3,3,1,200,2,1220))
wlsxPowerSaveDosAttack.setObjects(*((_A,_C),(_A,_H),(_A,_L),(_A,_P),(_A,_M),(_A,_D),(_A,_F),(_A,_G),(_A,_I),(_A,_K)))
if mibBuilder.loadTexts:wlsxPowerSaveDosAttack.setStatus(_B)
wlsxNAPMasterStatusChange=NotificationType((1,3,6,1,4,1,14823,2,3,3,1,200,2,1221))
wlsxNAPMasterStatusChange.setObjects(*((_A,_C),(_A,_D),(_A,_A0),(_A,_Ar)))
if mibBuilder.loadTexts:wlsxNAPMasterStatusChange.setStatus(_U)
wlsxNAdhocUsingValidSSID=NotificationType((1,3,6,1,4,1,14823,2,3,3,1,200,2,1222))
wlsxNAdhocUsingValidSSID.setObjects(*((_A,_C),(_A,_H),(_A,_L),(_A,_O),(_A,_M),(_A,_D),(_A,_F),(_A,_G),(_A,_I),(_A,_K)))
if mibBuilder.loadTexts:wlsxNAdhocUsingValidSSID.setStatus(_B)
wlsxMgmtUserAuthenticationFailed=NotificationType((1,3,6,1,4,1,14823,2,3,3,1,200,2,1224))
wlsxMgmtUserAuthenticationFailed.setObjects(*((_A,_C),(_A,_g),(_A,_V),(_A,_T),(_A,_Z),(_A,_e)))
if mibBuilder.loadTexts:wlsxMgmtUserAuthenticationFailed.setStatus(_B)
wlsxAPActiveUplinkChanged=NotificationType((1,3,6,1,4,1,14823,2,3,3,1,200,2,1252))
wlsxAPActiveUplinkChanged.setObjects(*((_A,_C),(_A,_D),(_A,_As),(_A,_At),(_A,_Au),(_A,_Av)))
if mibBuilder.loadTexts:wlsxAPActiveUplinkChanged.setStatus(_B)
wlsxAPManagedModeConfigFailureTrap=NotificationType((1,3,6,1,4,1,14823,2,3,3,1,200,2,1255))
wlsxAPManagedModeConfigFailureTrap.setObjects(*((_A,_C),(_A,_Aw)))
if mibBuilder.loadTexts:wlsxAPManagedModeConfigFailureTrap.setStatus(_B)
wlsxNAuthServerAcctTimedOut=NotificationType((1,3,6,1,4,1,14823,2,3,3,1,200,2,1256))
wlsxNAuthServerAcctTimedOut.setObjects(*((_A,_C),(_A,_g),(_A,_V),(_A,_T),(_A,_Z),(_A,_e),(_A,_Y),(_A,_S)))
if mibBuilder.loadTexts:wlsxNAuthServerAcctTimedOut.setStatus(_B)
wlsxPortalServerDown=NotificationType((1,3,6,1,4,1,14823,2,3,3,1,200,2,1259))
wlsxPortalServerDown.setObjects(*((_A,_C),(_A,_A1),(_A,_A2),(_A,_S),(_A,_Ax)))
if mibBuilder.loadTexts:wlsxPortalServerDown.setStatus(_B)
wlsxPortalServerUp=NotificationType((1,3,6,1,4,1,14823,2,3,3,1,200,2,1260))
wlsxPortalServerUp.setObjects(*((_A,_C),(_A,_A1),(_A,_A2),(_A,_S)))
if mibBuilder.loadTexts:wlsxPortalServerUp.setStatus(_B)
wlsxIAPVoiceClientLocationUpdate=NotificationType((1,3,6,1,4,1,14823,2,3,3,1,200,2,1262))
wlsxIAPVoiceClientLocationUpdate.setObjects(*((_A,_C),(_A,_Ay),(_A,_Az),(_A,_D),(_A,_S)))
if mibBuilder.loadTexts:wlsxIAPVoiceClientLocationUpdate.setStatus(_B)
wlsxWPAFTAttack=NotificationType((1,3,6,1,4,1,14823,2,3,3,1,200,2,1267))
wlsxWPAFTAttack.setObjects(*((_A,_C),(_A,_D),(_A,_F),(_A,_G),(_A,_P),(_A,_I),(_A,_H),(_A,_K)))
if mibBuilder.loadTexts:wlsxWPAFTAttack.setStatus(_B)
wlsxMitMDetected=NotificationType((1,3,6,1,4,1,14823,2,3,3,1,200,2,1268))
wlsxMitMDetected.setObjects(*((_A,_C),(_A,_G),(_A,_D),(_A,_F),(_A,_O),(_A,_H),(_A,_I),(_A,_M),(_A,_K)))
if mibBuilder.loadTexts:wlsxMitMDetected.setStatus(_B)
wlsxAPLoopDetected=NotificationType((1,3,6,1,4,1,14823,2,3,3,1,200,2,1271))
wlsxAPLoopDetected.setObjects(*((_A,_C),(_A,_D),(_A,_S),(_A,_n)))
if mibBuilder.loadTexts:wlsxAPLoopDetected.setStatus(_B)
wlsxAPBROADCASTSTORM=NotificationType((1,3,6,1,4,1,14823,2,3,3,1,200,2,1272))
wlsxAPBROADCASTSTORM.setObjects(*((_A,_C),(_A,_D),(_A,_S),(_A,_n)))
if mibBuilder.loadTexts:wlsxAPBROADCASTSTORM.setStatus(_B)
wlsxCLEARPASSSERVERINVALID=NotificationType((1,3,6,1,4,1,14823,2,3,3,1,200,2,1274))
wlsxCLEARPASSSERVERINVALID.setObjects(*((_A,_C),(_A,_Z)))
if mibBuilder.loadTexts:wlsxCLEARPASSSERVERINVALID.setStatus(_B)
wlsxAPUSBPLUGALARM=NotificationType((1,3,6,1,4,1,14823,2,3,3,1,200,2,1277))
wlsxAPUSBPLUGALARM.setObjects(*((_A,_C),(_A,_D),(_A,_S),(_A,_A3),(_A,_A3),(_A,_A_)))
if mibBuilder.loadTexts:wlsxAPUSBPLUGALARM.setStatus(_B)
wlsxClientRejectedByMaxClientCount=NotificationType((1,3,6,1,4,1,14823,2,3,3,1,200,2,1284))
wlsxClientRejectedByMaxClientCount.setObjects(*((_A,_C),(_A,_T),(_A,_Y),(_A,_D),(_A,_S),(_A,_A4)))
if mibBuilder.loadTexts:wlsxClientRejectedByMaxClientCount.setStatus(_B)
wlsxClientPskAuthenticationFailed=NotificationType((1,3,6,1,4,1,14823,2,3,3,1,200,2,1285))
wlsxClientPskAuthenticationFailed.setObjects(*((_A,_C),(_A,_T),(_A,_B0),(_A,_Y),(_A,_D),(_A,_S),(_A,_A4)))
if mibBuilder.loadTexts:wlsxClientPskAuthenticationFailed.setStatus(_B)
wlsxNStationAddedToDenyList=NotificationType((1,3,6,1,4,1,14823,2,3,3,1,200,2,1286))
wlsxNStationAddedToDenyList.setObjects(*((_A,_C),(_A,_P),(_A,_B1),(_A,_B2)))
if mibBuilder.loadTexts:wlsxNStationAddedToDenyList.setStatus(_B)
wlsxNStationRemovedFromDenyList=NotificationType((1,3,6,1,4,1,14823,2,3,3,1,200,2,1287))
wlsxNStationRemovedFromDenyList.setObjects(*((_A,_C),(_A,_P)))
if mibBuilder.loadTexts:wlsxNStationRemovedFromDenyList.setStatus(_B)
wlsxNAPConductorStatusChange=NotificationType((1,3,6,1,4,1,14823,2,3,3,1,200,2,1288))
wlsxNAPConductorStatusChange.setObjects(*((_A,_C),(_A,_D),(_A,_A0),(_A,_B3)))
if mibBuilder.loadTexts:wlsxNAPConductorStatusChange.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'ArubaEnableValue':ArubaEnableValue,'ArubaFrameType':ArubaFrameType,'ArubaPhyType':ArubaPhyType,'ArubaHTMode':ArubaHTMode,'ArubaHTExtChannel':ArubaHTExtChannel,'ArubaMonEncryptionType':ArubaMonEncryptionType,'ArubaMonEncryptionCipher':ArubaMonEncryptionCipher,'ArubaMonAuthAlgorithm':ArubaMonAuthAlgorithm,'ArubaSwitchRole':ArubaSwitchRole,'ArubaSupportStatus':ArubaSupportStatus,'ArubaActiveState':ArubaActiveState,'ArubaACLDomain':ArubaACLDomain,'ArubaACLNetworkServiceType':ArubaACLNetworkServiceType,'ArubaACLAction':ArubaACLAction,'ArubaDaysOfWeek':ArubaDaysOfWeek,'ArubaAuthenticationMethods':ArubaAuthenticationMethods,'ArubaSubAuthenticationMethods':ArubaSubAuthenticationMethods,'ArubaEncryptionType':ArubaEncryptionType,'ArubaUserForwardMode':ArubaUserForwardMode,'ArubaRogueApType':ArubaRogueApType,'ArubaAPMatchType':ArubaAPMatchType,'ArubaAPMatchMethod':ArubaAPMatchMethod,'ArubaStationType':ArubaStationType,'ArubaEncryptionMethods':ArubaEncryptionMethods,'ArubaHashAlgorithms':ArubaHashAlgorithms,'ArubaVlanValidRange':ArubaVlanValidRange,'ArubaPortMode':ArubaPortMode,'ArubaDot1dState':ArubaDot1dState,'ArubaPoeState':ArubaPoeState,'ArubaCardType':ArubaCardType,'ArubaESIServerMode':ArubaESIServerMode,'ArubaESIServerStatus':ArubaESIServerStatus,'ArubaIfType':ArubaIfType,'ArubaVoipProtocolType':ArubaVoipProtocolType,'ArubaAccessPointMode':ArubaAccessPointMode,'ArubaAuthServerType':ArubaAuthServerType,'ArubaAddressType':ArubaAddressType,'ArubaBlackListReason':ArubaBlackListReason,'ArubaDBType':ArubaDBType,'ArubaVrrpState':ArubaVrrpState,'ArubaOperStateValue':ArubaOperStateValue,'ArubaAntennaSetting':ArubaAntennaSetting,'ArubaAPStatus':ArubaAPStatus,'ArubaPortSpeed':ArubaPortSpeed,'ArubaPortDuplex':ArubaPortDuplex,'ArubaPortType':ArubaPortType,'ArubaEnet1Mode':ArubaEnet1Mode,'ArubaUnprovisionedStatus':ArubaUnprovisionedStatus,'ArubaMonitorMode':ArubaMonitorMode,'ArubaConfigurationState':ArubaConfigurationState,'ArubaConfigurationChangeType':ArubaConfigurationChangeType,'ArubaCallStates':ArubaCallStates,'ArubaVoipProtocol':ArubaVoipProtocol,'ArubaVoipRegState':ArubaVoipRegState,'ArubaVoiceCdrDirection':ArubaVoiceCdrDirection,'ArubaVoiceCacBit':ArubaVoiceCacBit,'ArubaMeshRole':ArubaMeshRole,'ArubaHTRate':ArubaHTRate,'ArubaUSBStatus':ArubaUSBStatus,'ArubaARMChangeReason':ArubaARMChangeReason,'ArubaAPMasterStatus':ArubaAPMasterStatus,'ArubaAPUplinkType':ArubaAPUplinkType,'ArubaAPUplinkChangeReason':ArubaAPUplinkChangeReason,'ArubaPortalServerDownReason':ArubaPortalServerDownReason,'ArubaDenyListReason':ArubaDenyListReason,'ArubaAPConductorStatus':ArubaAPConductorStatus,'aiMIB':aiMIB,'aiInfoGroup':aiInfoGroup,'aiVirtualControllerKey':aiVirtualControllerKey,'aiVirtualControllerName':aiVirtualControllerName,'aiVirtualControllerOrganization':aiVirtualControllerOrganization,'aiVirtualControllerVersion':aiVirtualControllerVersion,'aiVirtualControllerIPAddress':aiVirtualControllerIPAddress,'aiMasterIPAddress':aiMasterIPAddress,'aiWlanSSIDTable':aiWlanSSIDTable,'aiWlanSSIDEntry':aiWlanSSIDEntry,_AL:aiSSIDIndex,'aiSSID':aiSSID,'aiSSIDStatus':aiSSIDStatus,'aiSSIDClientNum':aiSSIDClientNum,'aiSSIDHide':aiSSIDHide,'aiInterferAccessPointTable':aiInterferAccessPointTable,'aiInterferAccessPointEntry':aiInterferAccessPointEntry,_AM:aiInterferAPIndex,'aiInterferAPBSSID':aiInterferAPBSSID,'aiInterferAPESSID':aiInterferAPESSID,'aiInterferAPChannel':aiInterferAPChannel,'aiInterferAPPhyType':aiInterferAPPhyType,'aiInterferAPEncr':aiInterferAPEncr,'aiInterferAPAvgSnr':aiInterferAPAvgSnr,'aiInterferAPType':aiInterferAPType,'aiMeshTable':aiMeshTable,'aiMeshEntry':aiMeshEntry,_AN:aiMeshIndex,'aiMeshPointMac':aiMeshPointMac,'aiMeshPortalMac':aiMeshPortalMac,'aiMeshChannel':aiMeshChannel,'aiMeshAvgRssi':aiMeshAvgRssi,'aiMeshHops':aiMeshHops,'aiMeshAge':aiMeshAge,'aiMeshCost':aiMeshCost,'aiMeshRelation':aiMeshRelation,'aiConductorIPAddress':aiConductorIPAddress,'aiStateGroup':aiStateGroup,'aiAccessPointTable':aiAccessPointTable,'aiAccessPointEntry':aiAccessPointEntry,_AO:aiAPMACAddress,'aiAPName':aiAPName,'aiAPIPAddress':aiAPIPAddress,'aiAPSerialNum':aiAPSerialNum,'aiAPModel':aiAPModel,'aiAPModelName':aiAPModelName,'aiAPCPUUtilization':aiAPCPUUtilization,'aiAPMemoryFree':aiAPMemoryFree,'aiAPUptime':aiAPUptime,'aiAPTotalMemory':aiAPTotalMemory,'aiAPStatus':aiAPStatus,'aiAPHwopmode':aiAPHwopmode,'aiAPRole':aiAPRole,'aiRadioTable':aiRadioTable,'aiRadioEntry':aiRadioEntry,_AP:aiRadioAPMACAddress,_AQ:aiRadioIndex,'aiRadioMACAddress':aiRadioMACAddress,'aiRadioChannel':aiRadioChannel,'aiRadioTransmitPower':aiRadioTransmitPower,'aiRadioNoiseFloor':aiRadioNoiseFloor,'aiRadioUtilization4':aiRadioUtilization4,'aiRadioUtilization64':aiRadioUtilization64,'aiRadioTxTotalFrames':aiRadioTxTotalFrames,'aiRadioTxMgmtFrames':aiRadioTxMgmtFrames,'aiRadioTxDataFrames':aiRadioTxDataFrames,'aiRadioTxDataBytes':aiRadioTxDataBytes,'aiRadioTxDrops':aiRadioTxDrops,'aiRadioRxTotalFrames':aiRadioRxTotalFrames,'aiRadioRxDataFrames':aiRadioRxDataFrames,'aiRadioRxDataBytes':aiRadioRxDataBytes,'aiRadioRxMgmtFrames':aiRadioRxMgmtFrames,'aiRadioRxBad':aiRadioRxBad,'aiRadioPhyEvents':aiRadioPhyEvents,'aiRadioStatus':aiRadioStatus,'aiRadioClientNum':aiRadioClientNum,'aiRadioMode':aiRadioMode,'aiWlanTable':aiWlanTable,'aiWlanEntry':aiWlanEntry,_AR:aiWlanAPMACAddress,_AS:aiWlanIndex,'aiWlanESSID':aiWlanESSID,'aiWlanMACAddress':aiWlanMACAddress,'aiWlanTxTotalFrames':aiWlanTxTotalFrames,'aiWlanTxDataFrames':aiWlanTxDataFrames,'aiWlanTxDataBytes':aiWlanTxDataBytes,'aiWlanRxTotalFrames':aiWlanRxTotalFrames,'aiWlanRxDataFrames':aiWlanRxDataFrames,'aiWlanRxDataBytes':aiWlanRxDataBytes,'aiClientTable':aiClientTable,'aiClientEntry':aiClientEntry,_AT:aiClientMACAddress,'aiClientWlanMACAddress':aiClientWlanMACAddress,'aiClientIPAddress':aiClientIPAddress,'aiClientAPIPAddress':aiClientAPIPAddress,'aiClientName':aiClientName,'aiClientOperatingSystem':aiClientOperatingSystem,'aiClientSNR':aiClientSNR,'aiClientTxDataFrames':aiClientTxDataFrames,'aiClientTxDataBytes':aiClientTxDataBytes,'aiClientTxRetries':aiClientTxRetries,'aiClientTxRate':aiClientTxRate,'aiClientRxDataFrames':aiClientRxDataFrames,'aiClientRxDataBytes':aiClientRxDataBytes,'aiClientRxRetries':aiClientRxRetries,'aiClientRxRate':aiClientRxRate,'aiClientUptime':aiClientUptime,'aiClientPhyType':aiClientPhyType,'aiClientHtMode':aiClientHtMode,'aiVoiceClientTable':aiVoiceClientTable,'aiVoiceClientEntry':aiVoiceClientEntry,_AU:aiClientMac,'aiClientIP':aiClientIP,'aiClientAPMac':aiClientAPMac,'aiClientAPName':aiClientAPName,'aiManagedInfoGroup':aiManagedInfoGroup,'aiManagedModeSinceLastSync':aiManagedModeSinceLastSync,'aiTrapsGroup':aiTrapsGroup,'aiTrapObjectsGroup':aiTrapObjectsGroup,_D:wlsxTrapAPMacAddress,_Aa:wlsxTrapAPIpAddress,_Y:wlsxTrapAPBSSID,_A4:wlsxTrapEssid,_H:wlsxTrapTargetAPBSSID,_L:wlsxTrapTargetAPSSID,_j:wlsxTrapTargetAPChannel,_P:wlsxTrapNodeMac,_O:wlsxTrapSourceMac,'wlsxReceiverMac':wlsxReceiverMac,_W:wlsxTrapTransmitterMac,_R:wlsxTrapReceiverMac,_M:wlsxTrapSnr,_Q:wlsxTrapSignatureName,_X:wlsxTrapFrameType,_v:wlsxTrapAddressType,_G:wlsxTrapAPLocation,_I:wlsxTrapAPChannel,_q:wlsxTrapAPTxPower,_t:wlsxTrapMatchedMac,_u:wlsxTrapMatchedIp,'wlsxTrapRogueIfoURL':wlsxTrapRogueIfoURL,_z:wlsxTrapVlanId,'wlsxTrapAdminStatus':wlsxTrapAdminStatus,'wlsxTrapOperStatus':wlsxTrapOperStatus,_Z:wlsxTrapAuthServerName,_AX:wlsxTrapAuthServerTimeout,_Ap:wlsxTrapCardSlot,'wlsxTrapTemperatureValue':wlsxTrapTemperatureValue,'wlsxTrapProcessName':wlsxTrapProcessName,'wlsxTrapFanNumber':wlsxTrapFanNumber,'wlsxTrapVoltageType':wlsxTrapVoltageType,'wlsxTrapVoltageValue':wlsxTrapVoltageValue,_AY:wlsxTrapStationBlackListReason,'wlsxTrapSpoofedIpAddress':wlsxTrapSpoofedIpAddress,'wlsxTrapSpoofedOldPhyAddress':wlsxTrapSpoofedOldPhyAddress,'wlsxTrapSpoofedNewPhyAddress':wlsxTrapSpoofedNewPhyAddress,'wlsxTrapDBName':wlsxTrapDBName,'wlsxTrapDBUserName':wlsxTrapDBUserName,'wlsxTrapDBIpAddress':wlsxTrapDBIpAddress,'wlsxTrapDBType':wlsxTrapDBType,'wlsxTrapVrrpID':wlsxTrapVrrpID,'wlsxTrapVrrpMasterIp':wlsxTrapVrrpMasterIp,'wlsxTrapVrrpOperState':wlsxTrapVrrpOperState,_Ae:wlsxTrapESIServerGrpName,'wlsxTrapESIServerName':wlsxTrapESIServerName,'wlsxTrapESIServerIpAddress':wlsxTrapESIServerIpAddress,'wlsxTrapLicenseDaysRemaining':wlsxTrapLicenseDaysRemaining,'wlsxTrapSwitchIp':wlsxTrapSwitchIp,'wlsxTrapSwitchRole':wlsxTrapSwitchRole,_V:wlsxTrapUserIpAddress,_T:wlsxTrapUserPhyAddress,_g:wlsxTrapUserName,_AW:wlsxTrapUserRole,_AV:wlsxTrapUserAuthenticationMethod,_F:wlsxTrapAPRadioNumber,_m:wlsxTrapRogueInfoURL,_Ad:wlsxTrapInterferingAPInfoURL,_n:wlsxTrapPortNumber,_C:wlsxTrapTime,'wlsxTrapHostIp':wlsxTrapHostIp,'wlsxTrapHostPort':wlsxTrapHostPort,'wlsxTrapConfigurationId':wlsxTrapConfigurationId,'wlsxTrapCTSURL':wlsxTrapCTSURL,'wlsxTrapCTSTransferType':wlsxTrapCTSTransferType,'wlsxTrapConfigurationState':wlsxTrapConfigurationState,'wlsxTrapUpdateFailureReason':wlsxTrapUpdateFailureReason,'wlsxTrapUpdateFailedObj':wlsxTrapUpdateFailedObj,'wlsxTrapTableEntryChangeType':wlsxTrapTableEntryChangeType,'wlsxTrapGlobalConfigObj':wlsxTrapGlobalConfigObj,'wlsxTrapTableGenNumber':wlsxTrapTableGenNumber,'wlsxTrapLicenseId':wlsxTrapLicenseId,_w:wlsxTrapConfidenceLevel,'wlsxTrapMissingLicenses':wlsxTrapMissingLicenses,'wlsxVoiceCurrentNumCdr':wlsxVoiceCurrentNumCdr,'wlsxTrapTunnelId':wlsxTrapTunnelId,'wlsxTrapTunnelStatus':wlsxTrapTunnelStatus,'wlsxTrapTunnelUpReason':wlsxTrapTunnelUpReason,'wlsxTrapTunnelDownReason':wlsxTrapTunnelDownReason,'wlsxTrapApSerialNumber':wlsxTrapApSerialNumber,'wlsxTrapTimeStr':wlsxTrapTimeStr,'wlsxTrapMasterIp':wlsxTrapMasterIp,'wlsxTrapLocalIp':wlsxTrapLocalIp,'wlsxTrapMasterName':wlsxTrapMasterName,'wlsxTrapLocalName':wlsxTrapLocalName,'wlsxTrapPrimaryControllerIp':wlsxTrapPrimaryControllerIp,'wlsxTrapBackupControllerIp':wlsxTrapBackupControllerIp,_x:wlsxTrapSpoofedFrameType,_Af:wlsxTrapAssociationType,_k:wlsxTrapDeviceIpAddress,_l:wlsxTrapDeviceMac,_Ay:wlsxTrapVcIpAddress,_Az:wlsxTrapVcMacAddress,_S:wlsxTrapAPName,'wlsxTrapApMode':wlsxTrapApMode,_Ah:wlsxTrapAPPrevChannel,_Ai:wlsxTrapAPPrevChannelSec,_Am:wlsxTrapAPPrevTxPower,_An:wlsxTrapAPCurMode,_Ao:wlsxTrapAPPrevMode,_Aj:wlsxTrapAPARMChangeReason,_Ag:wlsxTrapAPChannelSec,_Aq:wlsxTrapUserAttributeChangeType,_A0:wlsxTrapApControllerIp,_Ar:wlsxTrapApMasterStatus,'wlsxTrapCaName':wlsxTrapCaName,'wlsxTrapCrlName':wlsxTrapCrlName,'wlsxTrapCount':wlsxTrapCount,_As:wlsxTrapAPPreviousUplinkType,_At:wlsxTrapAPPreviousUplinkActiveTime,_Au:wlsxTrapAPActiveUplinkType,_Av:wlsxTrapAPUplinkChangeReason,_Aw:wlsxTrapAPManagedModeConfigFailure,_e:wlsxTrapAuthServerAddress,_A1:wlsxTrapPortalServerName,_A2:wlsxTrapPortalServerAddress,_Ax:wlsxTrapPortalServerDownReason,_AZ:wlsxTrapStationBlackListReasonStr,_A_:wlsxTrapAPUSBStatus,_A3:wlsxTrapUSBVendorProductID,_B0:wlsxTrapAuthFailureReason,_B2:wlsxTrapStationDenyListReason,_B1:wlsxTrapStationDenyListReasonStr,'wlsxTrapConductorIp':wlsxTrapConductorIp,'wlsxTrapConductorName':wlsxTrapConductorName,_B3:wlsxTrapApConductorStatus,_s:wlsxTrapAPHTMode,_r:wlsxTrapAPPhyType,_Ak:wlsxTrapAPPrevHTMode,_Al:wlsxTrapAPPrevPhyType,_Ab:wlsxTrapAPSecChannel,_K:wlsxTrapAPBand,_y:wlsxTrapTargetAPBand,_Ac:wlsxTrapMatchedIpv6,'aiTrapDefinitionsGroup':aiTrapDefinitionsGroup,'wlsxNodeRateAnomaly':wlsxNodeRateAnomaly,'wlsxNUserEntryCreated':wlsxNUserEntryCreated,'wlsxNUserEntryDeleted':wlsxNUserEntryDeleted,'wlsxNUserEntryAuthenticated':wlsxNUserEntryAuthenticated,'wlsxNUserEntryDeAuthenticated':wlsxNUserEntryDeAuthenticated,'wlsxNUserAuthenticationFailed':wlsxNUserAuthenticationFailed,'wlsxNAuthServerReqTimedOut':wlsxNAuthServerReqTimedOut,'wlsxNAuthServerTimedOut':wlsxNAuthServerTimedOut,'wlsxNAuthServerIsUp':wlsxNAuthServerIsUp,'wlsxNAccessPointIsUp':wlsxNAccessPointIsUp,'wlsxNAccessPointIsDown':wlsxNAccessPointIsDown,'wlsxNChannelChanged':wlsxNChannelChanged,'wlsxNStationAddedToBlackList':wlsxNStationAddedToBlackList,'wlsxNStationRemovedFromBlackList':wlsxNStationRemovedFromBlackList,'wlsxNRadioAttributesChanged':wlsxNRadioAttributesChanged,'wlsxUnsecureAPDetected':wlsxUnsecureAPDetected,'wlsxUnsecureAPResolved':wlsxUnsecureAPResolved,'wlsxStaImpersonation':wlsxStaImpersonation,'wlsxReservedChannelViolation':wlsxReservedChannelViolation,'wlsxValidSSIDViolation':wlsxValidSSIDViolation,'wlsxChannelMisconfiguration':wlsxChannelMisconfiguration,'wlsxOUIMisconfiguration':wlsxOUIMisconfiguration,'wlsxSSIDMisconfiguration':wlsxSSIDMisconfiguration,'wlsxShortPreableMisconfiguration':wlsxShortPreableMisconfiguration,'wlsxWPAMisconfiguration':wlsxWPAMisconfiguration,'wlsxAdhocNetworkDetected':wlsxAdhocNetworkDetected,'wlsxAdhocNetworkRemoved':wlsxAdhocNetworkRemoved,'wlsxStaPolicyViolation':wlsxStaPolicyViolation,'wlsxRepeatWEPIVViolation':wlsxRepeatWEPIVViolation,'wlsxWeakWEPIVViolation':wlsxWeakWEPIVViolation,'wlsxChannelInterferenceDetected':wlsxChannelInterferenceDetected,'wlsxChannelInterferenceCleared':wlsxChannelInterferenceCleared,'wlsxAPInterferenceDetected':wlsxAPInterferenceDetected,'wlsxAPInterferenceCleared':wlsxAPInterferenceCleared,'wlsxStaInterferenceDetected':wlsxStaInterferenceDetected,'wlsxStaInterferenceCleared':wlsxStaInterferenceCleared,'wlsxFrameRetryRateExceeded':wlsxFrameRetryRateExceeded,'wlsxFrameReceiveErrorRateExceeded':wlsxFrameReceiveErrorRateExceeded,'wlsxFrameFragmentationRateExceeded':wlsxFrameFragmentationRateExceeded,'wlsxFrameBandWidthRateExceeded':wlsxFrameBandWidthRateExceeded,'wlsxFrameLowSpeedRateExceeded':wlsxFrameLowSpeedRateExceeded,'wlsxFrameNonUnicastRateExceeded':wlsxFrameNonUnicastRateExceeded,'wlsxLoadbalancingEnabled':wlsxLoadbalancingEnabled,'wlsxLoadbalancingDisabled':wlsxLoadbalancingDisabled,'wlsxChannelFrameRetryRateExceeded':wlsxChannelFrameRetryRateExceeded,'wlsxChannelFrameFragmentationRateExceeded':wlsxChannelFrameFragmentationRateExceeded,'wlsxChannelFrameErrorRateExceeded':wlsxChannelFrameErrorRateExceeded,'wlsxSignatureMatchAP':wlsxSignatureMatchAP,'wlsxSignatureMatchSta':wlsxSignatureMatchSta,'wlsxChannelRateAnomaly':wlsxChannelRateAnomaly,'wlsxNodeRateAnomalyAP':wlsxNodeRateAnomalyAP,'wlsxNodeRateAnomalySta':wlsxNodeRateAnomalySta,'wlsxEAPRateAnomaly':wlsxEAPRateAnomaly,'wlsxSignalAnomaly':wlsxSignalAnomaly,'wlsxSequenceNumberAnomalyAP':wlsxSequenceNumberAnomalyAP,'wlsxSequenceNumberAnomalySta':wlsxSequenceNumberAnomalySta,'wlsxDisconnectStationAttack':wlsxDisconnectStationAttack,'wlsxApFloodAttack':wlsxApFloodAttack,'wlsxAdhocNetwork':wlsxAdhocNetwork,'wlsxWirelessBridge':wlsxWirelessBridge,'wlsxInvalidMacOUIAP':wlsxInvalidMacOUIAP,'wlsxInvalidMacOUISta':wlsxInvalidMacOUISta,'wlsxWEPMisconfiguration':wlsxWEPMisconfiguration,'wlsxStaRepeatWEPIVViolation':wlsxStaRepeatWEPIVViolation,'wlsxStaWeakWEPIVViolation':wlsxStaWeakWEPIVViolation,'wlsxStaAssociatedToUnsecureAP':wlsxStaAssociatedToUnsecureAP,'wlsxStaUnAssociatedFromUnsecureAP':wlsxStaUnAssociatedFromUnsecureAP,'wlsxAdhocNetworkBridgeDetected':wlsxAdhocNetworkBridgeDetected,'wlsxInterferingApDetected':wlsxInterferingApDetected,'wlsxColdStart':wlsxColdStart,'wlsxWarmStart':wlsxWarmStart,'wlsxAPImpersonation':wlsxAPImpersonation,'wlsxNAuthServerIsDown':wlsxNAuthServerIsDown,'wlsxWindowsBridgeDetected':wlsxWindowsBridgeDetected,'wlsxSignAPNetstumbler':wlsxSignAPNetstumbler,'wlsxSignStaNetstumbler':wlsxSignStaNetstumbler,'wlsxSignAPAsleap':wlsxSignAPAsleap,'wlsxSignStaAsleap':wlsxSignStaAsleap,'wlsxSignAPAirjack':wlsxSignAPAirjack,'wlsxSignStaAirjack':wlsxSignStaAirjack,'wlsxSignAPNullProbeResp':wlsxSignAPNullProbeResp,'wlsxSignStaNullProbeResp':wlsxSignStaNullProbeResp,'wlsxSignAPDeauthBcast':wlsxSignAPDeauthBcast,'wlsxSignStaDeauthBcast':wlsxSignStaDeauthBcast,'wlsxWindowsBridgeDetectedAP':wlsxWindowsBridgeDetectedAP,'wlsxWindowsBridgeDetectedSta':wlsxWindowsBridgeDetectedSta,'wlsxAdhocNetworkBridgeDetectedAP':wlsxAdhocNetworkBridgeDetectedAP,'wlsxAdhocNetworkBridgeDetectedSta':wlsxAdhocNetworkBridgeDetectedSta,'wlsxDisconnectStationAttackAP':wlsxDisconnectStationAttackAP,'wlsxDisconnectStationAttackSta':wlsxDisconnectStationAttackSta,'wlsxSuspectUnsecureAPDetected':wlsxSuspectUnsecureAPDetected,'wlsxSuspectUnsecureAPResolved':wlsxSuspectUnsecureAPResolved,'wlsxHtGreenfieldSupported':wlsxHtGreenfieldSupported,'wlsxHT40MHzIntoleranceAP':wlsxHT40MHzIntoleranceAP,'wlsxHT40MHzIntoleranceSta':wlsxHT40MHzIntoleranceSta,'wlsxNAuthServerAllInService':wlsxNAuthServerAllInService,'wlsxNAdhocNetwork':wlsxNAdhocNetwork,'wlsxNAdhocNetworkBridgeDetectedAP':wlsxNAdhocNetworkBridgeDetectedAP,'wlsxNAdhocNetworkBridgeDetectedSta':wlsxNAdhocNetworkBridgeDetectedSta,'wlsxClientFloodAttack':wlsxClientFloodAttack,'wlsxValidClientNotUsingEncryption':wlsxValidClientNotUsingEncryption,'wlsxAdhocUsingValidSSID':wlsxAdhocUsingValidSSID,'wlsxAPSpoofingDetected':wlsxAPSpoofingDetected,'wlsxClientAssociatingOnWrongChannel':wlsxClientAssociatingOnWrongChannel,'wlsxNDisconnectStationAttack':wlsxNDisconnectStationAttack,'wlsxNStaUnAssociatedFromUnsecureAP':wlsxNStaUnAssociatedFromUnsecureAP,'wlsxOmertaAttack':wlsxOmertaAttack,'wlsxTKIPReplayAttack':wlsxTKIPReplayAttack,'wlsxChopChopAttack':wlsxChopChopAttack,'wlsxFataJackAttack':wlsxFataJackAttack,'wlsxInvalidAddressCombination':wlsxInvalidAddressCombination,'wlsxValidClientMisassociation':wlsxValidClientMisassociation,'wlsxMalformedHTIEDetected':wlsxMalformedHTIEDetected,'wlsxMalformedAssocReqDetected':wlsxMalformedAssocReqDetected,'wlsxOverflowIEDetected':wlsxOverflowIEDetected,'wlsxOverflowEAPOLKeyDetected':wlsxOverflowEAPOLKeyDetected,'wlsxMalformedFrameLargeDurationDetected':wlsxMalformedFrameLargeDurationDetected,'wlsxMalformedFrameWrongChannelDetected':wlsxMalformedFrameWrongChannelDetected,'wlsxMalformedAuthFrame':wlsxMalformedAuthFrame,'wlsxCTSRateAnomaly':wlsxCTSRateAnomaly,'wlsxRTSRateAnomaly':wlsxRTSRateAnomaly,'wlsxNRogueAPDetected':wlsxNRogueAPDetected,'wlsxNRogueAPResolved':wlsxNRogueAPResolved,'wlsxNeighborAPDetected':wlsxNeighborAPDetected,'wlsxNInterferingAPDetected':wlsxNInterferingAPDetected,'wlsxNSuspectRogueAPDetected':wlsxNSuspectRogueAPDetected,'wlsxNSuspectRogueAPResolved':wlsxNSuspectRogueAPResolved,'wlsxBlockAckAttackDetected':wlsxBlockAckAttackDetected,'wlsxHotspotterAttackDetected':wlsxHotspotterAttackDetected,'wlsxNSignatureMatch':wlsxNSignatureMatch,'wlsxNSignatureMatchNetstumbler':wlsxNSignatureMatchNetstumbler,'wlsxNSignatureMatchAsleap':wlsxNSignatureMatchAsleap,'wlsxNSignatureMatchAirjack':wlsxNSignatureMatchAirjack,'wlsxNSignatureMatchNullProbeResp':wlsxNSignatureMatchNullProbeResp,'wlsxNSignatureMatchDeauthBcast':wlsxNSignatureMatchDeauthBcast,'wlsxNSignatureMatchDisassocBcast':wlsxNSignatureMatchDisassocBcast,'wlsxNSignatureMatchWellenreiter':wlsxNSignatureMatchWellenreiter,'wlsxAPDeauthContainment':wlsxAPDeauthContainment,'wlsxClientDeauthContainment':wlsxClientDeauthContainment,'wlsxAPWiredContainment':wlsxAPWiredContainment,'wlsxClientWiredContainment':wlsxClientWiredContainment,'wlsxAPTaggedWiredContainment':wlsxAPTaggedWiredContainment,'wlsxClientTaggedWiredContainment':wlsxClientTaggedWiredContainment,'wlsxTarpitContainment':wlsxTarpitContainment,'wlsxAPChannelChange':wlsxAPChannelChange,'wlsxAPPowerChange':wlsxAPPowerChange,'wlsxAPModeChange':wlsxAPModeChange,'wlsxUserEntryAttributesChanged':wlsxUserEntryAttributesChanged,'wlsxPowerSaveDosAttack':wlsxPowerSaveDosAttack,'wlsxNAPMasterStatusChange':wlsxNAPMasterStatusChange,'wlsxNAdhocUsingValidSSID':wlsxNAdhocUsingValidSSID,'wlsxMgmtUserAuthenticationFailed':wlsxMgmtUserAuthenticationFailed,'wlsxAPActiveUplinkChanged':wlsxAPActiveUplinkChanged,'wlsxAPManagedModeConfigFailureTrap':wlsxAPManagedModeConfigFailureTrap,'wlsxNAuthServerAcctTimedOut':wlsxNAuthServerAcctTimedOut,'wlsxPortalServerDown':wlsxPortalServerDown,'wlsxPortalServerUp':wlsxPortalServerUp,'wlsxIAPVoiceClientLocationUpdate':wlsxIAPVoiceClientLocationUpdate,'wlsxWPAFTAttack':wlsxWPAFTAttack,'wlsxMitMDetected':wlsxMitMDetected,'wlsxAPLoopDetected':wlsxAPLoopDetected,'wlsxAPBROADCASTSTORM':wlsxAPBROADCASTSTORM,'wlsxCLEARPASSSERVERINVALID':wlsxCLEARPASSSERVERINVALID,'wlsxAPUSBPLUGALARM':wlsxAPUSBPLUGALARM,'wlsxClientRejectedByMaxClientCount':wlsxClientRejectedByMaxClientCount,'wlsxClientPskAuthenticationFailed':wlsxClientPskAuthenticationFailed,'wlsxNStationAddedToDenyList':wlsxNStationAddedToDenyList,'wlsxNStationRemovedFromDenyList':wlsxNStationRemovedFromDenyList,'wlsxNAPConductorStatusChange':wlsxNAPConductorStatusChange})