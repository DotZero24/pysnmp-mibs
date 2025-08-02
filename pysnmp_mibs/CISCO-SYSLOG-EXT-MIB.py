_v='ciscoSyslogProtocolGroup'
_u='cseSyslogServerProtocolFallback'
_t='cseSyslogServerPort'
_s='cseSyslogServerProtocol'
_r='cseSyslogLinecardMsgSeverity'
_q='cseSyslogLinecardEnable'
_p='cseSyslogTerminalMsgSeverity'
_o='cseSyslogTerminalEnable'
_n='cseSyslogMessageSeverity'
_m='cseSyslogServerFacility'
_l='cseSyslogServerStatus'
_k='cseSyslogServerMsgSeverity'
_j='cseSyslogServerAddressType'
_i='cseSyslogServerAddress'
_h='cseSyslogServerTableMaxEntries'
_g='cseSyslogLogFileMsgSeverity'
_f='cseSyslogConsoleMsgSeverity'
_e='cseSyslogFileLoggingDisable'
_d='cseSyslogLogFileName'
_c='cseSyslogConsoleEnable'
_b='cseSyslogMessageFacility'
_a='SyslogFacility'
_Z='not-accessible'
_Y='cseSyslogServerIndex'
_X='local7'
_W='local6'
_V='local5'
_U='local4'
_T='local3'
_S='local2'
_R='local1'
_Q='local0'
_P='authPriv'
_O='syslog'
_N='daemon'
_M='kernel'
_L='Integer32'
_K='SnmpAdminString'
_J='InetPortNumber'
_I='ciscoSyslogExtGroup'
_H='SyslogProtocol'
_G='Unsigned32'
_F='TruthValue'
_E='SyslogSeverity'
_D='read-create'
_C='read-write'
_B='CISCO-SYSLOG-EXT-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
SyslogSeverity,=mibBuilder.importSymbols('CISCO-SYSLOG-MIB',_E)
InetAddress,InetAddressType,InetPortNumber=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress','InetAddressType',_J)
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB',_K)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_L,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_G,'iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention',_F)
ciscoSyslogExtMIB=ModuleIdentity((1,3,6,1,4,1,9,9,301))
if mibBuilder.loadTexts:ciscoSyslogExtMIB.setRevisions(('2019-04-02 00:00','2019-03-18 00:00','2015-06-08 00:00','2015-03-02 00:00','2014-11-05 00:00','2014-08-13 00:00','2014-06-02 00:00','2014-05-30 00:00','2013-11-23 00:00','2013-09-11 00:00','2013-06-14 00:00','2013-06-11 00:00','2013-01-08 00:00','2012-08-24 00:00','2011-06-09 00:00','2011-06-08 00:00','2011-05-20 00:00','2010-02-05 00:00','2009-08-16 00:00','2009-07-01 00:00','2009-06-17 00:00','2009-06-08 00:00','2008-04-28 00:00','2006-11-09 00:00','2005-01-30 00:00','2004-09-20 00:00','2003-12-15 00:00','2002-11-13 00:00','2002-10-04 00:00'))
class SyslogFacility(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,8,16,24,32,40,48,56,64,72,80,88,128,136,144,152,160,168,176,184)));namedValues=NamedValues(*((_M,0),('user',8),('mail',16),(_N,24),('auth',32),(_O,40),('lpr',48),('news',56),('uucp',64),('cron',72),(_P,80),('ftp',88),(_Q,128),(_R,136),(_S,144),(_T,152),(_U,160),(_V,168),(_W,176),(_X,184)))
class SyslogExFacility(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,8,16,24,32,40,48,56,64,72,80,88,128,136,144,152,160,168,176,184,200,208,216,224,232,240,248,256,264,272,280,288,296,304,312,320,328,336,344,352,360,368,376,384,392,400,408,416,424,432,440,448,456,464,472,480,488,496,504,512,520,536,552,576,584,592,608,648,656,672,688,704,736,816,848,920,928,960,976,992,1016,1064,1072,1096,1128,1136,1152,1160,1168,1192,1232,1240,1248,1256,1320,1328,1336,1344,1352,1360,1376,1392,1408,1432,1448,1456,1480,1488,1504,1512,1520,1536,1712,1720,1752,1768,1784,1792,1816,1872,1936,2048,2072,2080,2088,2112,2120,2144,2160,2176,2184,2240,2248,2368,2376,2384,2392,2400,2416,2440,2448,2528,2592,2600,2608,2616,2648,2656,2704,2728,2760,2800,2840,2848,2888,2896,2904,2920,2936,2944,2952,2960,2976,3048,3056,3080,3096,3112,3144,3152,3160,3168,3200,3216,3248,3296,3336,3360,3448,3496,3512,3544,3576,3680,3872,3888,3904,3920,3952,3960,3984,4008,4024,4032,4040,4048,4056,4064,4072,4088,4096,4104,4112,4120,4128,4136,4144,4152,4168,4192,4208,4224,4320,4368,4552,4592,4880,5168,5320,5328,5640,5744,5752,5776,5784,5808,5840,5848,5864,5920,5960,6016,6048,6168,6368,6592,6824,7128,7272)));namedValues=NamedValues(*((_M,0),('user',8),('mail',16),(_N,24),('auth',32),(_O,40),('lpr',48),('news',56),('uucp',64),('cron',72),(_P,80),('ftp',88),(_Q,128),(_R,136),(_S,144),(_T,152),(_U,160),(_V,168),(_W,176),(_X,184),('vsanMgr',200),('fspf',208),('domainMgr',216),('mtsDaemon',224),('linecardMgr',232),('sysMgr',240),('sysMgrLib',248),('zoneServer',256),('virtualIfMgr',264),('ipConfMgr',272),('ipfc',280),('xBarMgr',288),('fcDns',296),('fabricConfMgr',304),('aclMgr',312),('tlPortMgr',320),('portMgr',328),('fportServer',336),('portChMgr',344),('mpls',352),('tftpLib',360),('wwnMgr',368),('fcc',376),('qosMgr',384),('vhba',392),('procMgr',400),('fcRedirect',408),('span',416),('vrrpMgr',424),('fcfwd',432),('ntp',440),('pltmfmMgr',448),('xbarClient',456),('vrrpEngine',464),('callhome',472),('ipsMgr',480),('fc2',488),('debugLib',496),('vpm',504),('mcast',512),('rdl',520),('rscn',536),('bootvar',552),('pss',576),('snmp',584),('security',592),('vhbad',608),('dns',648),('rib',656),('vshd',672),('fvpd',688),('prefpath',704),('avm',736),('mplsTunnel',816),('cdpd',848),('ohmsd',920),('migd',928),('portSec',960),('ethPortMgr',976),('zbm',992),('ipaclMgr',1016),('ficonMgr',1064),('fsDaemon',1072),('ficonContDev',1096),('rlir',1128),('fdmi',1136),('licmgr',1152),('fcspmgr',1160),('epp',1168),('confCheck',1192),('ivr',1232),('aaad',1240),('tacacsd',1248),('radiusd',1256),('fc2d',1320),('cimServer',1328),('lcohmsd',1336),('isns',1344),('ficonStat',1352),('featureMgr',1360),('lttd',1376),('fccLc',1392),('ilcHelper',1408),('cfs',1432),('dstats',1448),('ipsec',1456),('dpvm',1480),('ike',1488),('ddas',1504),('scheduler',1512),('sanExtTuner',1520),('fscm',1536),('cloud',1712),('smartCard',1720),('certEnroll',1752),('stp',1768),('ethpm',1784),('pixm',1792),('ifMgr',1816),('plugin',1872),('acl',1936),('ldap',2048),('portResources',2072),('aclqos',2080),('portSecurity',2088),('eltm',2112),('udld',2120),('svi',2144),('mfdm',2160),('vlanMgr',2176),('ufdm',2184),('aclmgr',2240),('dot1x',2248),('nfm',2368),('hsrpEngine',2376),('bgp',2384),('l2fm',2392),('evms',2400),('evmc',2416),('monitor',2440),('lacp',2448),('vdcMgr',2528),('sdv',2592),('glbp',2600),('dhcpSnooping',2608),('xmlma',2616),('diagclient',2648),('diagmgr',2656),('vedbMgr',2704),('cluster',2728),('ipv6Conf',2760),('ipqosMgr',2800),('ethPortChannel',2840),('otm',2848),('l3vm',2888),('m6rib',2896),('mrib',2904),('pim',2920),('rpm',2936),('u6rib',2944),('urib',2952),('smm',2960),('resMgr',2976),('ip',3048),('ipv6',3056),('arp',3080),('diagportlb',3096),('vmm',3112),('tm',3144),('npv',3152),('deviceTest',3160),('cts',3168),('sal',3200),('copp',3216),('sme',3248),('mvsh',3296),('pltfmCfg',3336),('acllog',3360),('orib',3448),('m2rib',3496),('vpc',3512),('u2rib',3544),('lldp',3576),('aam',3680),('spm',3872),('sifMgr',3888),('fwm',3904),('zschk',3920),('afm',3952),('gatosUsd',3960),('pfm',3984),('nicmgr',4008),('qd',4024),('nqosm',4032),('ethpc',4040),('fcpc',4048),('enm',4056),('dcbx',4064),('altos',4072),('nohms',4088),('satMgr',4096),('satCtrl',4104),('redwoodUsd',4112),('fwmCtrl',4120),('qosCtrl',4128),('nppm',4136),('satSyslog',4144),('fcoeMgr',4152),('ioa',4168),('ppm',4192),('bfd',4208),('wccp',4224),('vntagMgr',4320),('assocMgr',4368),('l2pt',4552),('clkmgr',4592),('cmond',4880),('evc',5168),('slaSender',5320),('slaResponder',5328),('iscm',5640),('pixmgl',5744),('pixmvl',5752),('blogger',5776),('snmpmib',5784),('plsm',5808),('giscm',5840),('sim',5848),('vman',5864),('fpOam',5920),('lim',5960),('ecp',6016),('adbm',6048),('plcmgr',6168),('patchd',6368),('nxapi',6592),('analytics',6824),('vmis',7128),('telemetry',7272)))
class SyslogProtocol(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(6,17)));namedValues=NamedValues(*(('tcp',6),('udp',17)))
_CiscoSyslogExtMIBObjects_ObjectIdentity=ObjectIdentity
ciscoSyslogExtMIBObjects=_CiscoSyslogExtMIBObjects_ObjectIdentity((1,3,6,1,4,1,9,9,301,1))
_CseSyslogConfigurationGroup_ObjectIdentity=ObjectIdentity
cseSyslogConfigurationGroup=_CseSyslogConfigurationGroup_ObjectIdentity((1,3,6,1,4,1,9,9,301,1,1))
class _CseSyslogConsoleEnable_Type(TruthValue):defaultValue=2
_CseSyslogConsoleEnable_Type.__name__=_F
_CseSyslogConsoleEnable_Object=MibScalar
cseSyslogConsoleEnable=_CseSyslogConsoleEnable_Object((1,3,6,1,4,1,9,9,301,1,1,1),_CseSyslogConsoleEnable_Type())
cseSyslogConsoleEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:cseSyslogConsoleEnable.setStatus(_A)
class _CseSyslogConsoleMsgSeverity_Type(SyslogSeverity):defaultValue=8
_CseSyslogConsoleMsgSeverity_Type.__name__=_E
_CseSyslogConsoleMsgSeverity_Object=MibScalar
cseSyslogConsoleMsgSeverity=_CseSyslogConsoleMsgSeverity_Object((1,3,6,1,4,1,9,9,301,1,1,2),_CseSyslogConsoleMsgSeverity_Type())
cseSyslogConsoleMsgSeverity.setMaxAccess(_C)
if mibBuilder.loadTexts:cseSyslogConsoleMsgSeverity.setStatus(_A)
class _CseSyslogLogFileName_Type(SnmpAdminString):defaultValue=OctetString('messages');subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_CseSyslogLogFileName_Type.__name__=_K
_CseSyslogLogFileName_Object=MibScalar
cseSyslogLogFileName=_CseSyslogLogFileName_Object((1,3,6,1,4,1,9,9,301,1,1,3),_CseSyslogLogFileName_Type())
cseSyslogLogFileName.setMaxAccess(_C)
if mibBuilder.loadTexts:cseSyslogLogFileName.setStatus(_A)
class _CseSyslogLogFileMsgSeverity_Type(SyslogSeverity):defaultValue=8
_CseSyslogLogFileMsgSeverity_Type.__name__=_E
_CseSyslogLogFileMsgSeverity_Object=MibScalar
cseSyslogLogFileMsgSeverity=_CseSyslogLogFileMsgSeverity_Object((1,3,6,1,4,1,9,9,301,1,1,4),_CseSyslogLogFileMsgSeverity_Type())
cseSyslogLogFileMsgSeverity.setMaxAccess(_C)
if mibBuilder.loadTexts:cseSyslogLogFileMsgSeverity.setStatus(_A)
class _CseSyslogFileLoggingDisable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('true',1),('noOp',2)))
_CseSyslogFileLoggingDisable_Type.__name__=_L
_CseSyslogFileLoggingDisable_Object=MibScalar
cseSyslogFileLoggingDisable=_CseSyslogFileLoggingDisable_Object((1,3,6,1,4,1,9,9,301,1,1,5),_CseSyslogFileLoggingDisable_Type())
cseSyslogFileLoggingDisable.setMaxAccess(_C)
if mibBuilder.loadTexts:cseSyslogFileLoggingDisable.setStatus(_A)
class _CseSyslogServerTableMaxEntries_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_CseSyslogServerTableMaxEntries_Type.__name__=_G
_CseSyslogServerTableMaxEntries_Object=MibScalar
cseSyslogServerTableMaxEntries=_CseSyslogServerTableMaxEntries_Object((1,3,6,1,4,1,9,9,301,1,1,6),_CseSyslogServerTableMaxEntries_Type())
cseSyslogServerTableMaxEntries.setMaxAccess('read-only')
if mibBuilder.loadTexts:cseSyslogServerTableMaxEntries.setStatus(_A)
_CseSyslogServerTable_Object=MibTable
cseSyslogServerTable=_CseSyslogServerTable_Object((1,3,6,1,4,1,9,9,301,1,1,7))
if mibBuilder.loadTexts:cseSyslogServerTable.setStatus(_A)
_CseSyslogServerEntry_Object=MibTableRow
cseSyslogServerEntry=_CseSyslogServerEntry_Object((1,3,6,1,4,1,9,9,301,1,1,7,1))
cseSyslogServerEntry.setIndexNames((0,_B,_Y))
if mibBuilder.loadTexts:cseSyslogServerEntry.setStatus(_A)
class _CseSyslogServerIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_CseSyslogServerIndex_Type.__name__=_G
_CseSyslogServerIndex_Object=MibTableColumn
cseSyslogServerIndex=_CseSyslogServerIndex_Object((1,3,6,1,4,1,9,9,301,1,1,7,1,1),_CseSyslogServerIndex_Type())
cseSyslogServerIndex.setMaxAccess(_Z)
if mibBuilder.loadTexts:cseSyslogServerIndex.setStatus(_A)
_CseSyslogServerAddressType_Type=InetAddressType
_CseSyslogServerAddressType_Object=MibTableColumn
cseSyslogServerAddressType=_CseSyslogServerAddressType_Object((1,3,6,1,4,1,9,9,301,1,1,7,1,2),_CseSyslogServerAddressType_Type())
cseSyslogServerAddressType.setMaxAccess(_D)
if mibBuilder.loadTexts:cseSyslogServerAddressType.setStatus(_A)
_CseSyslogServerAddress_Type=InetAddress
_CseSyslogServerAddress_Object=MibTableColumn
cseSyslogServerAddress=_CseSyslogServerAddress_Object((1,3,6,1,4,1,9,9,301,1,1,7,1,3),_CseSyslogServerAddress_Type())
cseSyslogServerAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:cseSyslogServerAddress.setStatus(_A)
class _CseSyslogServerMsgSeverity_Type(SyslogSeverity):defaultValue=8
_CseSyslogServerMsgSeverity_Type.__name__=_E
_CseSyslogServerMsgSeverity_Object=MibTableColumn
cseSyslogServerMsgSeverity=_CseSyslogServerMsgSeverity_Object((1,3,6,1,4,1,9,9,301,1,1,7,1,4),_CseSyslogServerMsgSeverity_Type())
cseSyslogServerMsgSeverity.setMaxAccess(_D)
if mibBuilder.loadTexts:cseSyslogServerMsgSeverity.setStatus(_A)
_CseSyslogServerStatus_Type=RowStatus
_CseSyslogServerStatus_Object=MibTableColumn
cseSyslogServerStatus=_CseSyslogServerStatus_Object((1,3,6,1,4,1,9,9,301,1,1,7,1,5),_CseSyslogServerStatus_Type())
cseSyslogServerStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:cseSyslogServerStatus.setStatus(_A)
class _CseSyslogServerFacility_Type(SyslogFacility):defaultValue=184
_CseSyslogServerFacility_Type.__name__=_a
_CseSyslogServerFacility_Object=MibTableColumn
cseSyslogServerFacility=_CseSyslogServerFacility_Object((1,3,6,1,4,1,9,9,301,1,1,7,1,6),_CseSyslogServerFacility_Type())
cseSyslogServerFacility.setMaxAccess(_D)
if mibBuilder.loadTexts:cseSyslogServerFacility.setStatus(_A)
class _CseSyslogServerProtocol_Type(SyslogProtocol):defaultValue=17
_CseSyslogServerProtocol_Type.__name__=_H
_CseSyslogServerProtocol_Object=MibTableColumn
cseSyslogServerProtocol=_CseSyslogServerProtocol_Object((1,3,6,1,4,1,9,9,301,1,1,7,1,7),_CseSyslogServerProtocol_Type())
cseSyslogServerProtocol.setMaxAccess(_D)
if mibBuilder.loadTexts:cseSyslogServerProtocol.setStatus(_A)
class _CseSyslogServerPort_Type(InetPortNumber):subtypeSpec=InetPortNumber.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_CseSyslogServerPort_Type.__name__=_J
_CseSyslogServerPort_Object=MibTableColumn
cseSyslogServerPort=_CseSyslogServerPort_Object((1,3,6,1,4,1,9,9,301,1,1,7,1,8),_CseSyslogServerPort_Type())
cseSyslogServerPort.setMaxAccess(_D)
if mibBuilder.loadTexts:cseSyslogServerPort.setStatus(_A)
class _CseSyslogServerProtocolFallback_Type(SyslogProtocol):defaultValue=17
_CseSyslogServerProtocolFallback_Type.__name__=_H
_CseSyslogServerProtocolFallback_Object=MibTableColumn
cseSyslogServerProtocolFallback=_CseSyslogServerProtocolFallback_Object((1,3,6,1,4,1,9,9,301,1,1,7,1,9),_CseSyslogServerProtocolFallback_Type())
cseSyslogServerProtocolFallback.setMaxAccess(_D)
if mibBuilder.loadTexts:cseSyslogServerProtocolFallback.setStatus(_A)
_CseSyslogMessageControlTable_Object=MibTable
cseSyslogMessageControlTable=_CseSyslogMessageControlTable_Object((1,3,6,1,4,1,9,9,301,1,1,8))
if mibBuilder.loadTexts:cseSyslogMessageControlTable.setStatus(_A)
_CseSyslogMessageControlEntry_Object=MibTableRow
cseSyslogMessageControlEntry=_CseSyslogMessageControlEntry_Object((1,3,6,1,4,1,9,9,301,1,1,8,1))
cseSyslogMessageControlEntry.setIndexNames((0,_B,_b))
if mibBuilder.loadTexts:cseSyslogMessageControlEntry.setStatus(_A)
_CseSyslogMessageFacility_Type=SyslogExFacility
_CseSyslogMessageFacility_Object=MibTableColumn
cseSyslogMessageFacility=_CseSyslogMessageFacility_Object((1,3,6,1,4,1,9,9,301,1,1,8,1,1),_CseSyslogMessageFacility_Type())
cseSyslogMessageFacility.setMaxAccess(_Z)
if mibBuilder.loadTexts:cseSyslogMessageFacility.setStatus(_A)
_CseSyslogMessageSeverity_Type=SyslogSeverity
_CseSyslogMessageSeverity_Object=MibTableColumn
cseSyslogMessageSeverity=_CseSyslogMessageSeverity_Object((1,3,6,1,4,1,9,9,301,1,1,8,1,2),_CseSyslogMessageSeverity_Type())
cseSyslogMessageSeverity.setMaxAccess(_C)
if mibBuilder.loadTexts:cseSyslogMessageSeverity.setStatus(_A)
class _CseSyslogTerminalEnable_Type(TruthValue):defaultValue=2
_CseSyslogTerminalEnable_Type.__name__=_F
_CseSyslogTerminalEnable_Object=MibScalar
cseSyslogTerminalEnable=_CseSyslogTerminalEnable_Object((1,3,6,1,4,1,9,9,301,1,1,9),_CseSyslogTerminalEnable_Type())
cseSyslogTerminalEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:cseSyslogTerminalEnable.setStatus(_A)
class _CseSyslogTerminalMsgSeverity_Type(SyslogSeverity):defaultValue=8
_CseSyslogTerminalMsgSeverity_Type.__name__=_E
_CseSyslogTerminalMsgSeverity_Object=MibScalar
cseSyslogTerminalMsgSeverity=_CseSyslogTerminalMsgSeverity_Object((1,3,6,1,4,1,9,9,301,1,1,10),_CseSyslogTerminalMsgSeverity_Type())
cseSyslogTerminalMsgSeverity.setMaxAccess(_C)
if mibBuilder.loadTexts:cseSyslogTerminalMsgSeverity.setStatus(_A)
class _CseSyslogLinecardEnable_Type(TruthValue):defaultValue=2
_CseSyslogLinecardEnable_Type.__name__=_F
_CseSyslogLinecardEnable_Object=MibScalar
cseSyslogLinecardEnable=_CseSyslogLinecardEnable_Object((1,3,6,1,4,1,9,9,301,1,1,11),_CseSyslogLinecardEnable_Type())
cseSyslogLinecardEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:cseSyslogLinecardEnable.setStatus(_A)
class _CseSyslogLinecardMsgSeverity_Type(SyslogSeverity):defaultValue=8
_CseSyslogLinecardMsgSeverity_Type.__name__=_E
_CseSyslogLinecardMsgSeverity_Object=MibScalar
cseSyslogLinecardMsgSeverity=_CseSyslogLinecardMsgSeverity_Object((1,3,6,1,4,1,9,9,301,1,1,12),_CseSyslogLinecardMsgSeverity_Type())
cseSyslogLinecardMsgSeverity.setMaxAccess(_C)
if mibBuilder.loadTexts:cseSyslogLinecardMsgSeverity.setStatus(_A)
_CiscoSyslogExtMIBConformance_ObjectIdentity=ObjectIdentity
ciscoSyslogExtMIBConformance=_CiscoSyslogExtMIBConformance_ObjectIdentity((1,3,6,1,4,1,9,9,301,2))
_CiscoSyslogExtMIBCompliances_ObjectIdentity=ObjectIdentity
ciscoSyslogExtMIBCompliances=_CiscoSyslogExtMIBCompliances_ObjectIdentity((1,3,6,1,4,1,9,9,301,2,1))
_CiscoSyslogExtMIBGroups_ObjectIdentity=ObjectIdentity
ciscoSyslogExtMIBGroups=_CiscoSyslogExtMIBGroups_ObjectIdentity((1,3,6,1,4,1,9,9,301,2,2))
ciscoSyslogExtGroup=ObjectGroup((1,3,6,1,4,1,9,9,301,2,2,1))
ciscoSyslogExtGroup.setObjects(*((_B,_c),(_B,_d),(_B,_e),(_B,_f),(_B,_g),(_B,_h),(_B,_i),(_B,_j),(_B,_k),(_B,_l),(_B,_m),(_B,_n),(_B,_o),(_B,_p),(_B,_q),(_B,_r)))
if mibBuilder.loadTexts:ciscoSyslogExtGroup.setStatus(_A)
ciscoSyslogProtocolGroup=ObjectGroup((1,3,6,1,4,1,9,9,301,2,2,2))
ciscoSyslogProtocolGroup.setObjects(*((_B,_s),(_B,_t),(_B,_u)))
if mibBuilder.loadTexts:ciscoSyslogProtocolGroup.setStatus(_A)
ciscoSyslogExtMIBCompliance=ModuleCompliance((1,3,6,1,4,1,9,9,301,2,1,1))
ciscoSyslogExtMIBCompliance.setObjects((_B,_I))
if mibBuilder.loadTexts:ciscoSyslogExtMIBCompliance.setStatus('deprecated')
ciscoSyslogExtMIBComplianceRev2=ModuleCompliance((1,3,6,1,4,1,9,9,301,2,1,2))
ciscoSyslogExtMIBComplianceRev2.setObjects(*((_B,_I),(_B,_v)))
if mibBuilder.loadTexts:ciscoSyslogExtMIBComplianceRev2.setStatus(_A)
mibBuilder.exportSymbols(_B,**{_a:SyslogFacility,'SyslogExFacility':SyslogExFacility,_H:SyslogProtocol,'ciscoSyslogExtMIB':ciscoSyslogExtMIB,'ciscoSyslogExtMIBObjects':ciscoSyslogExtMIBObjects,'cseSyslogConfigurationGroup':cseSyslogConfigurationGroup,_c:cseSyslogConsoleEnable,_f:cseSyslogConsoleMsgSeverity,_d:cseSyslogLogFileName,_g:cseSyslogLogFileMsgSeverity,_e:cseSyslogFileLoggingDisable,_h:cseSyslogServerTableMaxEntries,'cseSyslogServerTable':cseSyslogServerTable,'cseSyslogServerEntry':cseSyslogServerEntry,_Y:cseSyslogServerIndex,_j:cseSyslogServerAddressType,_i:cseSyslogServerAddress,_k:cseSyslogServerMsgSeverity,_l:cseSyslogServerStatus,_m:cseSyslogServerFacility,_s:cseSyslogServerProtocol,_t:cseSyslogServerPort,_u:cseSyslogServerProtocolFallback,'cseSyslogMessageControlTable':cseSyslogMessageControlTable,'cseSyslogMessageControlEntry':cseSyslogMessageControlEntry,_b:cseSyslogMessageFacility,_n:cseSyslogMessageSeverity,_o:cseSyslogTerminalEnable,_p:cseSyslogTerminalMsgSeverity,_q:cseSyslogLinecardEnable,_r:cseSyslogLinecardMsgSeverity,'ciscoSyslogExtMIBConformance':ciscoSyslogExtMIBConformance,'ciscoSyslogExtMIBCompliances':ciscoSyslogExtMIBCompliances,'ciscoSyslogExtMIBCompliance':ciscoSyslogExtMIBCompliance,'ciscoSyslogExtMIBComplianceRev2':ciscoSyslogExtMIBComplianceRev2,'ciscoSyslogExtMIBGroups':ciscoSyslogExtMIBGroups,_I:ciscoSyslogExtGroup,_v:ciscoSyslogProtocolGroup})