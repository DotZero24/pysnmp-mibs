_AZ='hpicfSyslogPrefixStringGroup1'
_AY='hpicfSyslogControlFilterNameGroup'
_AX='hpicfSyslogLogMsgOptionsGroup2'
_AW='hpicfSyslogCommandLoggingGroup1'
_AV='hpicfSyslogLogMsgOptionsGroup1'
_AU='hpicfSyslogOriginIdGroup1'
_AT='hpicfSyslogAlertsGroup'
_AS='hpicfSyslogServerStatisticsGroup'
_AR='hpicfSyslogPriorityGroup1'
_AQ='hpicfSyslogControlTransportGroup'
_AP='hpicfSyslogLogMsgOptionsGroup'
_AO='hpicfSyslogFacilityStatisticsGroup'
_AN='hpicfSyslogSeverityStatisticsGroup'
_AM='hpicfSyslogGeneralStatisticsGroup'
_AL='hpicfSyslogControlGroupOobm'
_AK='hpicfSyslogStatusChanged'
_AJ='hpicfSyslogPrefixString'
_AI='hpicfSyslogControlFilterName'
_AH='hpicfSyslogCmdClearLog'
_AG='hpicfSyslogCommandLogging'
_AF='hpicfSyslogOriginId'
_AE='hpicfSyslogAlertTransmitInterval'
_AD='hpicfSyslogAlertAdminStatus'
_AC='hpicfSyslogServerLogBuffered'
_AB='hpicfSyslogServerResendError'
_AA='hpicfSyslogServerLogResend'
_A9='hpicfSyslogServerSendError'
_A8='hpicfSyslogServerLogRelay'
_A7='hpicfSyslogServerLogRecv'
_A6='hpicfSyslogServerLogSent'
_A5='hpicfSyslogControlDestinationPort'
_A4='hpicfSyslogControlTransportProtocol'
_A3='hpicfSyslogControlSmmLog'
_A2='hpicfSyslogfacilityCounter'
_A1='hpicfSyslogfacilityType'
_A0='hpicfSyslogSeverityCounter'
_z='hpicfSyslogSeverityType'
_y='hpicfSyslogGeneralLogBuffered'
_x='hpicfSyslogGeneralResendError'
_w='hpicfSyslogGeneralLogResend'
_v='hpicfSyslogGeneralSendError'
_u='hpicfSyslogGeneralLogRelay'
_t='hpicfSyslogGeneralLogRecv'
_s='hpicfSyslogGeneralLogSent'
_r='hpicfSyslogControlBindAddrIsOobm'
_q='hpicfSyslogOperationsCounterDiscontinuityTime'
_p='hpicfSyslogOperationsLastErrorTime'
_o='hpicfSyslogOperationsLastError'
_n='hpicfSyslogOperationsStartTime'
_m='hpicfSyslogOperationsLastMsgTransmittedTime'
_l='hpicfSyslogOperationsMsgsDropped'
_k='hpicfSyslogOperationsMsgsTransmitted'
_j='hpicfSyslogAlertIndex'
_i='hpicfSyslogfacilityCounterIndex'
_h='hpicfSyslogSeverityTypeIndex'
_g='HpicfSyslogOriginId'
_f='HpicfSyslogSystemModule'
_e='HpicfSyslogSeverity'
_d='HpicfSyslogFacility'
_c='2015-05-09 00:00'
_b='DisplayString'
_a='Unsigned32'
_Z='hpicfSyslogSecClearLog'
_Y='hpicfSyslogSystemModule'
_X='hpicfSyslogPrioritySeverity'
_W='hpicfSyslogPriorityFacility'
_V='hpicfSyslogPriorityDescr'
_U='hpicfSyslogControlRowStatus'
_T='hpicfSyslogControlBindAddrType'
_S='hpicfSyslogControlDescr'
_R='hpicfSyslogOperationsStatus'
_Q='TruthValue'
_P='hpicfSyslogControlGroupSmm'
_O='hpicfSyslogNotificationGroup'
_N='hpicfSyslogClearLog'
_M='not-accessible'
_L='hpicfSyslogControlIndex'
_K='hpicfSyslogPriorityGroup'
_J='hpicfSyslogControlGroup'
_I='hpicfSyslogOperationsGroup'
_H='hpicfSyslogControlBindAddr'
_G='deprecated'
_F='read-create'
_E='Integer32'
_D='read-write'
_C='read-only'
_B='current'
_A='HP-ICF-SYSLOG-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
hpicfSyslog,=mibBuilder.importSymbols('HP-ICF-OID','hpicfSyslog')
InetAddress,InetAddressType,InetPortNumber=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress','InetAddressType','InetPortNumber')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB','SnmpAdminString')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_a,'iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TimeStamp,TruthValue=mibBuilder.importSymbols('SNMPv2-TC',_b,'PhysAddress','RowStatus','TextualConvention','TimeStamp',_Q)
hpicfSyslogMIB=ModuleIdentity((1,3,6,1,4,1,11,2,14,14,1))
if mibBuilder.loadTexts:hpicfSyslogMIB.setRevisions(('2019-01-08 00:00','2018-07-10 00:00','2018-08-22 00:00','2018-02-14 00:00','2017-12-11 00:00','2017-10-17 00:00','2017-10-12 00:00','2017-09-05 00:00','2017-07-03 00:00','2016-07-13 00:00','2016-06-14 00:00','2016-05-12 00:00','2016-04-01 00:00','2016-03-23 00:00','2016-03-10 00:00','2016-01-21 05:26','2015-09-11 05:26','2015-09-04 00:00','2015-09-03 00:00','2015-08-31 00:00','2015-08-28 00:00','2015-08-07 00:00','2015-05-20 00:00',_c,_c,'2015-05-08 00:00','2015-04-16 00:00','2014-11-13 00:00','2014-07-17 00:00','2013-11-06 00:00','2013-09-24 00:00','2013-09-14 00:00','2013-09-05 00:00','2013-06-25 00:00','2013-08-07 00:00','2012-03-15 00:00','2012-01-30 00:00','2011-10-11 00:00','2011-08-24 00:00','2011-07-19 00:00','2011-06-13 00:00','2011-05-27 00:00','2011-03-21 00:00','2011-03-05 00:00','2010-11-09 00:00','2010-10-25 00:00','2010-08-11 00:00','2010-06-20 00:00','2010-03-20 00:00','2010-03-12 00:00','2010-01-27 00:00','2009-08-19 00:00','2009-02-18 00:00','2009-01-30 00:00','2008-11-18 00:00','2008-07-09 00:00','2008-06-26 00:00','2008-06-25 00:00','2008-01-25 00:00','2008-01-01 11:21'))
class HpicfSyslogFacility(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23)));namedValues=NamedValues(*(('kern',0),('user',1),('mail',2),('daemon',3),('auth',4),('syslog',5),('lpr',6),('news',7),('uucp',8),('sys9',9),('sys10',10),('sys11',11),('sys12',12),('sys13',13),('sys14',14),('cron',15),('local0',16),('local1',17),('local2',18),('local3',19),('local4',20),('local5',21),('local6',22),('local7',23)))
class HpicfSyslogSeverity(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7)));namedValues=NamedValues(*(('major',0),('alert',1),('critical',2),('error',3),('warning',4),('notice',5),('info',6),('debug',7)))
class HpicfSyslogSystemModule(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,120,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,143,144,145,146,147,148,149)));namedValues=NamedValues(*(('all-pass',0),('vlan',1),('ip',2),('igmp',3),('ipx',4),('stp',5),('system',6),('chassis',7),('console',8),('ports',9),('dhcp',10),('download',11),('tcp',12),('telnet',13),('timep',14),('tftp',15),('xmodem',16),('update',17),('mgr',18),('bridge',19),('snmp',20),('addrmgr',21),('agp',22),('fault',23),('ldbal',24),('garp',25),('gvrp',26),('cos',27),('lacp',28),('dhcpr',29),('stack',30),('dma',31),('sntp',32),('ieee8021x',33),('cdp',34),('auth',35),('tacacs',36),('radius',37),('ssh',38),('netinet',39),('ospf',40),('xrrp',41),('ssl',42),('ipaddrmgr',43),('macauth',44),('kms',45),('pim',46),('maclock',47),('acl',48),('udpf',49),('inst-mon',50),('udld',51),('hpesp',52),('lldp',53),('connfilt',54),('ratelim',55),('idm',56),('iplock',57),('dhcp-snoop',58),('vrrp',59),('usb',60),('licensing',61),('loop-protect',62),('sflow',63),('arp-protect',64),('dhcpv6c',65),('mtm',66),('mld',67),('dca',68),('qinq',69),('autorun',70),('ffi',71),('wsm',72),('dipld',73),('hpsm',74),('srcip',75),('policy',76),('oobm',77),('trmode',78),('ospf3',79),('dhcpv6r',80),('bgp',81),('ufd',82),('fips',83),('dt',84),('dcbx',85),('sftp',86),('stacking',87),('rfs',88),('testmode',89),('crypto',90),('slp',91),('ra-guard',92),('ecm',93),('hpespip',94),('mobility-agent',95),('securemode',96),('mSatProxy',97),('eSatProxy',98),('hpespcm',99),('openflow',100),('smart-link',101),('insysprog',102),('dhcp-server',103),('job',104),('dsnoopv6',105),('dipldv6',106),('servicetunnel',107),('tr069',108),('http',109),('vxlantunnel',110),('bpdu',111),('byod-redirect',112),('dldp',113),('macsec',114),('acct',115),('tls',116),('ripng',117),('arpthrottle',120),('ndsnoop',122),('ntp',123),('ipsla',124),('psDetect',125),('mdns',126),('mvrp',127),('rip',128),('bfd',129),('lldpmad',130),('captive-portal',131),('profile-manager',132),('vsf',133),('tunneledNode',134),('amp-server',135),('activate',136),('central',137),('ztpIpsec',138),('greTunnel',139),('userTnode',140),('vlanMad',141),('cfgRestore',143),('devOnboard',144),('httpProxy',145),('dfp',146),('authOrder',147),('caDownload',148),('estc',149)))
class HpicfSyslogOriginId(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('ip-address',1),('hostname',2),('none',3)))
_HpicfSyslogNotifications_ObjectIdentity=ObjectIdentity
hpicfSyslogNotifications=_HpicfSyslogNotifications_ObjectIdentity((1,3,6,1,4,1,11,2,14,14,1,0))
_HpicfSyslogObjects_ObjectIdentity=ObjectIdentity
hpicfSyslogObjects=_HpicfSyslogObjects_ObjectIdentity((1,3,6,1,4,1,11,2,14,14,1,1))
_HpicfSyslogControlTable_Object=MibTable
hpicfSyslogControlTable=_HpicfSyslogControlTable_Object((1,3,6,1,4,1,11,2,14,14,1,1,1))
if mibBuilder.loadTexts:hpicfSyslogControlTable.setStatus(_B)
_HpicfSyslogControlEntry_Object=MibTableRow
hpicfSyslogControlEntry=_HpicfSyslogControlEntry_Object((1,3,6,1,4,1,11,2,14,14,1,1,1,1))
hpicfSyslogControlEntry.setIndexNames((0,_A,_L))
if mibBuilder.loadTexts:hpicfSyslogControlEntry.setStatus(_B)
_HpicfSyslogControlIndex_Type=Integer32
_HpicfSyslogControlIndex_Object=MibTableColumn
hpicfSyslogControlIndex=_HpicfSyslogControlIndex_Object((1,3,6,1,4,1,11,2,14,14,1,1,1,1,1),_HpicfSyslogControlIndex_Type())
hpicfSyslogControlIndex.setMaxAccess(_M)
if mibBuilder.loadTexts:hpicfSyslogControlIndex.setStatus(_B)
_HpicfSyslogControlDescr_Type=SnmpAdminString
_HpicfSyslogControlDescr_Object=MibTableColumn
hpicfSyslogControlDescr=_HpicfSyslogControlDescr_Object((1,3,6,1,4,1,11,2,14,14,1,1,1,1,2),_HpicfSyslogControlDescr_Type())
hpicfSyslogControlDescr.setMaxAccess(_F)
if mibBuilder.loadTexts:hpicfSyslogControlDescr.setStatus(_B)
_HpicfSyslogControlBindAddrType_Type=InetAddressType
_HpicfSyslogControlBindAddrType_Object=MibTableColumn
hpicfSyslogControlBindAddrType=_HpicfSyslogControlBindAddrType_Object((1,3,6,1,4,1,11,2,14,14,1,1,1,1,3),_HpicfSyslogControlBindAddrType_Type())
hpicfSyslogControlBindAddrType.setMaxAccess(_F)
if mibBuilder.loadTexts:hpicfSyslogControlBindAddrType.setStatus(_B)
_HpicfSyslogControlBindAddr_Type=InetAddress
_HpicfSyslogControlBindAddr_Object=MibTableColumn
hpicfSyslogControlBindAddr=_HpicfSyslogControlBindAddr_Object((1,3,6,1,4,1,11,2,14,14,1,1,1,1,4),_HpicfSyslogControlBindAddr_Type())
hpicfSyslogControlBindAddr.setMaxAccess(_F)
if mibBuilder.loadTexts:hpicfSyslogControlBindAddr.setStatus(_B)
_HpicfSyslogControlRowStatus_Type=RowStatus
_HpicfSyslogControlRowStatus_Object=MibTableColumn
hpicfSyslogControlRowStatus=_HpicfSyslogControlRowStatus_Object((1,3,6,1,4,1,11,2,14,14,1,1,1,1,5),_HpicfSyslogControlRowStatus_Type())
hpicfSyslogControlRowStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:hpicfSyslogControlRowStatus.setStatus(_B)
class _HpicfSyslogControlBindAddrIsOobm_Type(TruthValue):defaultValue=2
_HpicfSyslogControlBindAddrIsOobm_Type.__name__=_Q
_HpicfSyslogControlBindAddrIsOobm_Object=MibTableColumn
hpicfSyslogControlBindAddrIsOobm=_HpicfSyslogControlBindAddrIsOobm_Object((1,3,6,1,4,1,11,2,14,14,1,1,1,1,6),_HpicfSyslogControlBindAddrIsOobm_Type())
hpicfSyslogControlBindAddrIsOobm.setMaxAccess(_F)
if mibBuilder.loadTexts:hpicfSyslogControlBindAddrIsOobm.setStatus(_B)
class _HpicfSyslogControlSmmLog_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('enabled',1),('disabled',2)))
_HpicfSyslogControlSmmLog_Type.__name__=_E
_HpicfSyslogControlSmmLog_Object=MibTableColumn
hpicfSyslogControlSmmLog=_HpicfSyslogControlSmmLog_Object((1,3,6,1,4,1,11,2,14,14,1,1,1,1,7),_HpicfSyslogControlSmmLog_Type())
hpicfSyslogControlSmmLog.setMaxAccess(_F)
if mibBuilder.loadTexts:hpicfSyslogControlSmmLog.setStatus(_B)
class _HpicfSyslogControlTransportProtocol_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('udp',1),('tcp',2),('tls',3)))
_HpicfSyslogControlTransportProtocol_Type.__name__=_E
_HpicfSyslogControlTransportProtocol_Object=MibTableColumn
hpicfSyslogControlTransportProtocol=_HpicfSyslogControlTransportProtocol_Object((1,3,6,1,4,1,11,2,14,14,1,1,1,1,8),_HpicfSyslogControlTransportProtocol_Type())
hpicfSyslogControlTransportProtocol.setMaxAccess(_D)
if mibBuilder.loadTexts:hpicfSyslogControlTransportProtocol.setStatus(_B)
_HpicfSyslogControlDestinationPort_Type=InetPortNumber
_HpicfSyslogControlDestinationPort_Object=MibTableColumn
hpicfSyslogControlDestinationPort=_HpicfSyslogControlDestinationPort_Object((1,3,6,1,4,1,11,2,14,14,1,1,1,1,9),_HpicfSyslogControlDestinationPort_Type())
hpicfSyslogControlDestinationPort.setMaxAccess(_D)
if mibBuilder.loadTexts:hpicfSyslogControlDestinationPort.setStatus(_B)
_HpicfSyslogControlFilterName_Type=SnmpAdminString
_HpicfSyslogControlFilterName_Object=MibTableColumn
hpicfSyslogControlFilterName=_HpicfSyslogControlFilterName_Object((1,3,6,1,4,1,11,2,14,14,1,1,1,1,10),_HpicfSyslogControlFilterName_Type())
hpicfSyslogControlFilterName.setMaxAccess(_D)
if mibBuilder.loadTexts:hpicfSyslogControlFilterName.setStatus(_B)
_HpicfSyslogOperations_ObjectIdentity=ObjectIdentity
hpicfSyslogOperations=_HpicfSyslogOperations_ObjectIdentity((1,3,6,1,4,1,11,2,14,14,1,1,2))
_HpicfSyslogOperationsMsgsTransmitted_Type=Counter32
_HpicfSyslogOperationsMsgsTransmitted_Object=MibScalar
hpicfSyslogOperationsMsgsTransmitted=_HpicfSyslogOperationsMsgsTransmitted_Object((1,3,6,1,4,1,11,2,14,14,1,1,2,1),_HpicfSyslogOperationsMsgsTransmitted_Type())
hpicfSyslogOperationsMsgsTransmitted.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfSyslogOperationsMsgsTransmitted.setStatus(_B)
_HpicfSyslogOperationsMsgsDropped_Type=Counter32
_HpicfSyslogOperationsMsgsDropped_Object=MibScalar
hpicfSyslogOperationsMsgsDropped=_HpicfSyslogOperationsMsgsDropped_Object((1,3,6,1,4,1,11,2,14,14,1,1,2,2),_HpicfSyslogOperationsMsgsDropped_Type())
hpicfSyslogOperationsMsgsDropped.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfSyslogOperationsMsgsDropped.setStatus(_B)
_HpicfSyslogOperationsLastMsgTransmittedTime_Type=TimeStamp
_HpicfSyslogOperationsLastMsgTransmittedTime_Object=MibScalar
hpicfSyslogOperationsLastMsgTransmittedTime=_HpicfSyslogOperationsLastMsgTransmittedTime_Object((1,3,6,1,4,1,11,2,14,14,1,1,2,3),_HpicfSyslogOperationsLastMsgTransmittedTime_Type())
hpicfSyslogOperationsLastMsgTransmittedTime.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfSyslogOperationsLastMsgTransmittedTime.setStatus(_B)
_HpicfSyslogOperationsStartTime_Type=TimeStamp
_HpicfSyslogOperationsStartTime_Object=MibScalar
hpicfSyslogOperationsStartTime=_HpicfSyslogOperationsStartTime_Object((1,3,6,1,4,1,11,2,14,14,1,1,2,4),_HpicfSyslogOperationsStartTime_Type())
hpicfSyslogOperationsStartTime.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfSyslogOperationsStartTime.setStatus(_B)
_HpicfSyslogOperationsLastError_Type=SnmpAdminString
_HpicfSyslogOperationsLastError_Object=MibScalar
hpicfSyslogOperationsLastError=_HpicfSyslogOperationsLastError_Object((1,3,6,1,4,1,11,2,14,14,1,1,2,5),_HpicfSyslogOperationsLastError_Type())
hpicfSyslogOperationsLastError.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfSyslogOperationsLastError.setStatus(_B)
_HpicfSyslogOperationsLastErrorTime_Type=TimeStamp
_HpicfSyslogOperationsLastErrorTime_Object=MibScalar
hpicfSyslogOperationsLastErrorTime=_HpicfSyslogOperationsLastErrorTime_Object((1,3,6,1,4,1,11,2,14,14,1,1,2,6),_HpicfSyslogOperationsLastErrorTime_Type())
hpicfSyslogOperationsLastErrorTime.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfSyslogOperationsLastErrorTime.setStatus(_B)
_HpicfSyslogOperationsCounterDiscontinuityTime_Type=TimeStamp
_HpicfSyslogOperationsCounterDiscontinuityTime_Object=MibScalar
hpicfSyslogOperationsCounterDiscontinuityTime=_HpicfSyslogOperationsCounterDiscontinuityTime_Object((1,3,6,1,4,1,11,2,14,14,1,1,2,7),_HpicfSyslogOperationsCounterDiscontinuityTime_Type())
hpicfSyslogOperationsCounterDiscontinuityTime.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfSyslogOperationsCounterDiscontinuityTime.setStatus(_B)
class _HpicfSyslogOperationsStatus_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('unknown',1),('started',2),('suspended',3),('stopped',4)))
_HpicfSyslogOperationsStatus_Type.__name__=_E
_HpicfSyslogOperationsStatus_Object=MibScalar
hpicfSyslogOperationsStatus=_HpicfSyslogOperationsStatus_Object((1,3,6,1,4,1,11,2,14,14,1,1,2,8),_HpicfSyslogOperationsStatus_Type())
hpicfSyslogOperationsStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfSyslogOperationsStatus.setStatus(_B)
_HpicfSyslogPriority_ObjectIdentity=ObjectIdentity
hpicfSyslogPriority=_HpicfSyslogPriority_ObjectIdentity((1,3,6,1,4,1,11,2,14,14,1,1,3))
class _HpicfSyslogPriorityFacility_Type(HpicfSyslogFacility):defaultValue=1
_HpicfSyslogPriorityFacility_Type.__name__=_d
_HpicfSyslogPriorityFacility_Object=MibScalar
hpicfSyslogPriorityFacility=_HpicfSyslogPriorityFacility_Object((1,3,6,1,4,1,11,2,14,14,1,1,3,1),_HpicfSyslogPriorityFacility_Type())
hpicfSyslogPriorityFacility.setMaxAccess(_D)
if mibBuilder.loadTexts:hpicfSyslogPriorityFacility.setStatus(_B)
class _HpicfSyslogPrioritySeverity_Type(HpicfSyslogSeverity):defaultValue=7
_HpicfSyslogPrioritySeverity_Type.__name__=_e
_HpicfSyslogPrioritySeverity_Object=MibScalar
hpicfSyslogPrioritySeverity=_HpicfSyslogPrioritySeverity_Object((1,3,6,1,4,1,11,2,14,14,1,1,3,2),_HpicfSyslogPrioritySeverity_Type())
hpicfSyslogPrioritySeverity.setMaxAccess(_D)
if mibBuilder.loadTexts:hpicfSyslogPrioritySeverity.setStatus(_B)
_HpicfSyslogPriorityDescr_Type=SnmpAdminString
_HpicfSyslogPriorityDescr_Object=MibScalar
hpicfSyslogPriorityDescr=_HpicfSyslogPriorityDescr_Object((1,3,6,1,4,1,11,2,14,14,1,1,3,3),_HpicfSyslogPriorityDescr_Type())
hpicfSyslogPriorityDescr.setMaxAccess(_D)
if mibBuilder.loadTexts:hpicfSyslogPriorityDescr.setStatus(_B)
class _HpicfSyslogSystemModule_Type(HpicfSyslogSystemModule):defaultValue=0
_HpicfSyslogSystemModule_Type.__name__=_f
_HpicfSyslogSystemModule_Object=MibScalar
hpicfSyslogSystemModule=_HpicfSyslogSystemModule_Object((1,3,6,1,4,1,11,2,14,14,1,1,3,4),_HpicfSyslogSystemModule_Type())
hpicfSyslogSystemModule.setMaxAccess(_D)
if mibBuilder.loadTexts:hpicfSyslogSystemModule.setStatus(_B)
class _HpicfSyslogOriginId_Type(HpicfSyslogOriginId):defaultValue=1
_HpicfSyslogOriginId_Type.__name__=_g
_HpicfSyslogOriginId_Object=MibScalar
hpicfSyslogOriginId=_HpicfSyslogOriginId_Object((1,3,6,1,4,1,11,2,14,14,1,1,3,5),_HpicfSyslogOriginId_Type())
hpicfSyslogOriginId.setMaxAccess(_D)
if mibBuilder.loadTexts:hpicfSyslogOriginId.setStatus(_B)
class _HpicfSyslogPrefixString_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,48))
_HpicfSyslogPrefixString_Type.__name__=_b
_HpicfSyslogPrefixString_Object=MibScalar
hpicfSyslogPrefixString=_HpicfSyslogPrefixString_Object((1,3,6,1,4,1,11,2,14,14,1,1,3,6),_HpicfSyslogPrefixString_Type())
hpicfSyslogPrefixString.setMaxAccess(_D)
if mibBuilder.loadTexts:hpicfSyslogPrefixString.setStatus(_B)
_HpicfSyslogStatistics_ObjectIdentity=ObjectIdentity
hpicfSyslogStatistics=_HpicfSyslogStatistics_ObjectIdentity((1,3,6,1,4,1,11,2,14,14,1,1,4))
_HpicfSyslogGeneralStatistics_ObjectIdentity=ObjectIdentity
hpicfSyslogGeneralStatistics=_HpicfSyslogGeneralStatistics_ObjectIdentity((1,3,6,1,4,1,11,2,14,14,1,1,4,1))
_HpicfSyslogGeneralLogSent_Type=Counter32
_HpicfSyslogGeneralLogSent_Object=MibScalar
hpicfSyslogGeneralLogSent=_HpicfSyslogGeneralLogSent_Object((1,3,6,1,4,1,11,2,14,14,1,1,4,1,1),_HpicfSyslogGeneralLogSent_Type())
hpicfSyslogGeneralLogSent.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfSyslogGeneralLogSent.setStatus(_B)
_HpicfSyslogGeneralLogRecv_Type=Counter32
_HpicfSyslogGeneralLogRecv_Object=MibScalar
hpicfSyslogGeneralLogRecv=_HpicfSyslogGeneralLogRecv_Object((1,3,6,1,4,1,11,2,14,14,1,1,4,1,2),_HpicfSyslogGeneralLogRecv_Type())
hpicfSyslogGeneralLogRecv.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfSyslogGeneralLogRecv.setStatus(_B)
_HpicfSyslogGeneralLogRelay_Type=Counter32
_HpicfSyslogGeneralLogRelay_Object=MibScalar
hpicfSyslogGeneralLogRelay=_HpicfSyslogGeneralLogRelay_Object((1,3,6,1,4,1,11,2,14,14,1,1,4,1,3),_HpicfSyslogGeneralLogRelay_Type())
hpicfSyslogGeneralLogRelay.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfSyslogGeneralLogRelay.setStatus(_B)
_HpicfSyslogGeneralSendError_Type=Counter32
_HpicfSyslogGeneralSendError_Object=MibScalar
hpicfSyslogGeneralSendError=_HpicfSyslogGeneralSendError_Object((1,3,6,1,4,1,11,2,14,14,1,1,4,1,4),_HpicfSyslogGeneralSendError_Type())
hpicfSyslogGeneralSendError.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfSyslogGeneralSendError.setStatus(_B)
_HpicfSyslogGeneralLogResend_Type=Counter32
_HpicfSyslogGeneralLogResend_Object=MibScalar
hpicfSyslogGeneralLogResend=_HpicfSyslogGeneralLogResend_Object((1,3,6,1,4,1,11,2,14,14,1,1,4,1,5),_HpicfSyslogGeneralLogResend_Type())
hpicfSyslogGeneralLogResend.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfSyslogGeneralLogResend.setStatus(_B)
_HpicfSyslogGeneralResendError_Type=Counter32
_HpicfSyslogGeneralResendError_Object=MibScalar
hpicfSyslogGeneralResendError=_HpicfSyslogGeneralResendError_Object((1,3,6,1,4,1,11,2,14,14,1,1,4,1,6),_HpicfSyslogGeneralResendError_Type())
hpicfSyslogGeneralResendError.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfSyslogGeneralResendError.setStatus(_B)
_HpicfSyslogGeneralLogBuffered_Type=Counter32
_HpicfSyslogGeneralLogBuffered_Object=MibScalar
hpicfSyslogGeneralLogBuffered=_HpicfSyslogGeneralLogBuffered_Object((1,3,6,1,4,1,11,2,14,14,1,1,4,1,7),_HpicfSyslogGeneralLogBuffered_Type())
hpicfSyslogGeneralLogBuffered.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfSyslogGeneralLogBuffered.setStatus(_B)
_HpicfSyslogSeverityStatistics_ObjectIdentity=ObjectIdentity
hpicfSyslogSeverityStatistics=_HpicfSyslogSeverityStatistics_ObjectIdentity((1,3,6,1,4,1,11,2,14,14,1,1,4,2))
_HpicfSyslogSeverityCounterInfoTable_Object=MibTable
hpicfSyslogSeverityCounterInfoTable=_HpicfSyslogSeverityCounterInfoTable_Object((1,3,6,1,4,1,11,2,14,14,1,1,4,2,1))
if mibBuilder.loadTexts:hpicfSyslogSeverityCounterInfoTable.setStatus(_B)
_HpicfSyslogSeverityCounterInfoEntry_Object=MibTableRow
hpicfSyslogSeverityCounterInfoEntry=_HpicfSyslogSeverityCounterInfoEntry_Object((1,3,6,1,4,1,11,2,14,14,1,1,4,2,1,1))
hpicfSyslogSeverityCounterInfoEntry.setIndexNames((0,_A,_h))
if mibBuilder.loadTexts:hpicfSyslogSeverityCounterInfoEntry.setStatus(_B)
_HpicfSyslogSeverityTypeIndex_Type=Integer32
_HpicfSyslogSeverityTypeIndex_Object=MibTableColumn
hpicfSyslogSeverityTypeIndex=_HpicfSyslogSeverityTypeIndex_Object((1,3,6,1,4,1,11,2,14,14,1,1,4,2,1,1,1),_HpicfSyslogSeverityTypeIndex_Type())
hpicfSyslogSeverityTypeIndex.setMaxAccess(_M)
if mibBuilder.loadTexts:hpicfSyslogSeverityTypeIndex.setStatus(_B)
_HpicfSyslogSeverityType_Type=HpicfSyslogSeverity
_HpicfSyslogSeverityType_Object=MibTableColumn
hpicfSyslogSeverityType=_HpicfSyslogSeverityType_Object((1,3,6,1,4,1,11,2,14,14,1,1,4,2,1,1,2),_HpicfSyslogSeverityType_Type())
hpicfSyslogSeverityType.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfSyslogSeverityType.setStatus(_B)
_HpicfSyslogSeverityCounter_Type=Counter32
_HpicfSyslogSeverityCounter_Object=MibTableColumn
hpicfSyslogSeverityCounter=_HpicfSyslogSeverityCounter_Object((1,3,6,1,4,1,11,2,14,14,1,1,4,2,1,1,3),_HpicfSyslogSeverityCounter_Type())
hpicfSyslogSeverityCounter.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfSyslogSeverityCounter.setStatus(_B)
_HpicfSyslogFacilityStatistics_ObjectIdentity=ObjectIdentity
hpicfSyslogFacilityStatistics=_HpicfSyslogFacilityStatistics_ObjectIdentity((1,3,6,1,4,1,11,2,14,14,1,1,4,3))
_HpicfSyslogFacilityCounterInfoTable_Object=MibTable
hpicfSyslogFacilityCounterInfoTable=_HpicfSyslogFacilityCounterInfoTable_Object((1,3,6,1,4,1,11,2,14,14,1,1,4,3,1))
if mibBuilder.loadTexts:hpicfSyslogFacilityCounterInfoTable.setStatus(_B)
_HpicfSyslogFacilityCounterInfoEntry_Object=MibTableRow
hpicfSyslogFacilityCounterInfoEntry=_HpicfSyslogFacilityCounterInfoEntry_Object((1,3,6,1,4,1,11,2,14,14,1,1,4,3,1,1))
hpicfSyslogFacilityCounterInfoEntry.setIndexNames((0,_A,_i))
if mibBuilder.loadTexts:hpicfSyslogFacilityCounterInfoEntry.setStatus(_B)
_HpicfSyslogfacilityCounterIndex_Type=Integer32
_HpicfSyslogfacilityCounterIndex_Object=MibTableColumn
hpicfSyslogfacilityCounterIndex=_HpicfSyslogfacilityCounterIndex_Object((1,3,6,1,4,1,11,2,14,14,1,1,4,3,1,1,1),_HpicfSyslogfacilityCounterIndex_Type())
hpicfSyslogfacilityCounterIndex.setMaxAccess(_M)
if mibBuilder.loadTexts:hpicfSyslogfacilityCounterIndex.setStatus(_B)
_HpicfSyslogfacilityType_Type=HpicfSyslogFacility
_HpicfSyslogfacilityType_Object=MibTableColumn
hpicfSyslogfacilityType=_HpicfSyslogfacilityType_Object((1,3,6,1,4,1,11,2,14,14,1,1,4,3,1,1,2),_HpicfSyslogfacilityType_Type())
hpicfSyslogfacilityType.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfSyslogfacilityType.setStatus(_B)
_HpicfSyslogfacilityCounter_Type=Counter32
_HpicfSyslogfacilityCounter_Object=MibTableColumn
hpicfSyslogfacilityCounter=_HpicfSyslogfacilityCounter_Object((1,3,6,1,4,1,11,2,14,14,1,1,4,3,1,1,3),_HpicfSyslogfacilityCounter_Type())
hpicfSyslogfacilityCounter.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfSyslogfacilityCounter.setStatus(_B)
_HpicfSyslogLogMsgOptions_ObjectIdentity=ObjectIdentity
hpicfSyslogLogMsgOptions=_HpicfSyslogLogMsgOptions_ObjectIdentity((1,3,6,1,4,1,11,2,14,14,1,1,5))
_HpicfSyslogClearLog_Type=TruthValue
_HpicfSyslogClearLog_Object=MibScalar
hpicfSyslogClearLog=_HpicfSyslogClearLog_Object((1,3,6,1,4,1,11,2,14,14,1,1,5,1),_HpicfSyslogClearLog_Type())
hpicfSyslogClearLog.setMaxAccess(_D)
if mibBuilder.loadTexts:hpicfSyslogClearLog.setStatus(_B)
_HpicfSyslogSecClearLog_Type=TruthValue
_HpicfSyslogSecClearLog_Object=MibScalar
hpicfSyslogSecClearLog=_HpicfSyslogSecClearLog_Object((1,3,6,1,4,1,11,2,14,14,1,1,5,2),_HpicfSyslogSecClearLog_Type())
hpicfSyslogSecClearLog.setMaxAccess(_D)
if mibBuilder.loadTexts:hpicfSyslogSecClearLog.setStatus(_B)
_HpicfSyslogCmdClearLog_Type=TruthValue
_HpicfSyslogCmdClearLog_Object=MibScalar
hpicfSyslogCmdClearLog=_HpicfSyslogCmdClearLog_Object((1,3,6,1,4,1,11,2,14,14,1,1,5,3),_HpicfSyslogCmdClearLog_Type())
hpicfSyslogCmdClearLog.setMaxAccess(_D)
if mibBuilder.loadTexts:hpicfSyslogCmdClearLog.setStatus(_B)
_HpicfSyslogServerStatisticsTable_Object=MibTable
hpicfSyslogServerStatisticsTable=_HpicfSyslogServerStatisticsTable_Object((1,3,6,1,4,1,11,2,14,14,1,1,6))
if mibBuilder.loadTexts:hpicfSyslogServerStatisticsTable.setStatus(_B)
_HpicfSyslogServerStatisticsEntry_Object=MibTableRow
hpicfSyslogServerStatisticsEntry=_HpicfSyslogServerStatisticsEntry_Object((1,3,6,1,4,1,11,2,14,14,1,1,6,1))
hpicfSyslogServerStatisticsEntry.setIndexNames((0,_A,_L))
if mibBuilder.loadTexts:hpicfSyslogServerStatisticsEntry.setStatus(_B)
_HpicfSyslogServerLogSent_Type=Counter32
_HpicfSyslogServerLogSent_Object=MibTableColumn
hpicfSyslogServerLogSent=_HpicfSyslogServerLogSent_Object((1,3,6,1,4,1,11,2,14,14,1,1,6,1,1),_HpicfSyslogServerLogSent_Type())
hpicfSyslogServerLogSent.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfSyslogServerLogSent.setStatus(_B)
_HpicfSyslogServerLogRecv_Type=Counter32
_HpicfSyslogServerLogRecv_Object=MibTableColumn
hpicfSyslogServerLogRecv=_HpicfSyslogServerLogRecv_Object((1,3,6,1,4,1,11,2,14,14,1,1,6,1,2),_HpicfSyslogServerLogRecv_Type())
hpicfSyslogServerLogRecv.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfSyslogServerLogRecv.setStatus(_B)
_HpicfSyslogServerLogRelay_Type=Counter32
_HpicfSyslogServerLogRelay_Object=MibTableColumn
hpicfSyslogServerLogRelay=_HpicfSyslogServerLogRelay_Object((1,3,6,1,4,1,11,2,14,14,1,1,6,1,3),_HpicfSyslogServerLogRelay_Type())
hpicfSyslogServerLogRelay.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfSyslogServerLogRelay.setStatus(_B)
_HpicfSyslogServerSendError_Type=Counter32
_HpicfSyslogServerSendError_Object=MibTableColumn
hpicfSyslogServerSendError=_HpicfSyslogServerSendError_Object((1,3,6,1,4,1,11,2,14,14,1,1,6,1,4),_HpicfSyslogServerSendError_Type())
hpicfSyslogServerSendError.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfSyslogServerSendError.setStatus(_B)
_HpicfSyslogServerLogResend_Type=Counter32
_HpicfSyslogServerLogResend_Object=MibTableColumn
hpicfSyslogServerLogResend=_HpicfSyslogServerLogResend_Object((1,3,6,1,4,1,11,2,14,14,1,1,6,1,5),_HpicfSyslogServerLogResend_Type())
hpicfSyslogServerLogResend.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfSyslogServerLogResend.setStatus(_B)
_HpicfSyslogServerResendError_Type=Counter32
_HpicfSyslogServerResendError_Object=MibTableColumn
hpicfSyslogServerResendError=_HpicfSyslogServerResendError_Object((1,3,6,1,4,1,11,2,14,14,1,1,6,1,6),_HpicfSyslogServerResendError_Type())
hpicfSyslogServerResendError.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfSyslogServerResendError.setStatus(_B)
_HpicfSyslogServerLogBuffered_Type=Counter32
_HpicfSyslogServerLogBuffered_Object=MibTableColumn
hpicfSyslogServerLogBuffered=_HpicfSyslogServerLogBuffered_Object((1,3,6,1,4,1,11,2,14,14,1,1,6,1,7),_HpicfSyslogServerLogBuffered_Type())
hpicfSyslogServerLogBuffered.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfSyslogServerLogBuffered.setStatus(_B)
_HpicfSyslogAlerts_ObjectIdentity=ObjectIdentity
hpicfSyslogAlerts=_HpicfSyslogAlerts_ObjectIdentity((1,3,6,1,4,1,11,2,14,14,1,1,7))
_HpicfSyslogAlertsTable_Object=MibTable
hpicfSyslogAlertsTable=_HpicfSyslogAlertsTable_Object((1,3,6,1,4,1,11,2,14,14,1,1,7,1))
if mibBuilder.loadTexts:hpicfSyslogAlertsTable.setStatus(_B)
_HpicfSyslogAlertsEntry_Object=MibTableRow
hpicfSyslogAlertsEntry=_HpicfSyslogAlertsEntry_Object((1,3,6,1,4,1,11,2,14,14,1,1,7,1,1))
hpicfSyslogAlertsEntry.setIndexNames((0,_A,_j))
if mibBuilder.loadTexts:hpicfSyslogAlertsEntry.setStatus(_B)
class _HpicfSyslogAlertIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues(('runningCfgChg',1))
_HpicfSyslogAlertIndex_Type.__name__=_E
_HpicfSyslogAlertIndex_Object=MibTableColumn
hpicfSyslogAlertIndex=_HpicfSyslogAlertIndex_Object((1,3,6,1,4,1,11,2,14,14,1,1,7,1,1,1),_HpicfSyslogAlertIndex_Type())
hpicfSyslogAlertIndex.setMaxAccess(_M)
if mibBuilder.loadTexts:hpicfSyslogAlertIndex.setStatus(_B)
class _HpicfSyslogAlertAdminStatus_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('enable',1),('disable',2)))
_HpicfSyslogAlertAdminStatus_Type.__name__=_E
_HpicfSyslogAlertAdminStatus_Object=MibTableColumn
hpicfSyslogAlertAdminStatus=_HpicfSyslogAlertAdminStatus_Object((1,3,6,1,4,1,11,2,14,14,1,1,7,1,1,2),_HpicfSyslogAlertAdminStatus_Type())
hpicfSyslogAlertAdminStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:hpicfSyslogAlertAdminStatus.setStatus(_B)
class _HpicfSyslogAlertTransmitInterval_Type(Unsigned32):defaultValue=0
_HpicfSyslogAlertTransmitInterval_Type.__name__=_a
_HpicfSyslogAlertTransmitInterval_Object=MibTableColumn
hpicfSyslogAlertTransmitInterval=_HpicfSyslogAlertTransmitInterval_Object((1,3,6,1,4,1,11,2,14,14,1,1,7,1,1,3),_HpicfSyslogAlertTransmitInterval_Type())
hpicfSyslogAlertTransmitInterval.setMaxAccess(_D)
if mibBuilder.loadTexts:hpicfSyslogAlertTransmitInterval.setStatus(_B)
if mibBuilder.loadTexts:hpicfSyslogAlertTransmitInterval.setUnits('seconds')
_HpicfSyslogLogging_ObjectIdentity=ObjectIdentity
hpicfSyslogLogging=_HpicfSyslogLogging_ObjectIdentity((1,3,6,1,4,1,11,2,14,14,1,1,8))
class _HpicfSyslogCommandLogging_Type(TruthValue):defaultValue=2
_HpicfSyslogCommandLogging_Type.__name__=_Q
_HpicfSyslogCommandLogging_Object=MibScalar
hpicfSyslogCommandLogging=_HpicfSyslogCommandLogging_Object((1,3,6,1,4,1,11,2,14,14,1,1,8,1),_HpicfSyslogCommandLogging_Type())
hpicfSyslogCommandLogging.setMaxAccess(_D)
if mibBuilder.loadTexts:hpicfSyslogCommandLogging.setStatus(_B)
_HpicfSyslogConformance_ObjectIdentity=ObjectIdentity
hpicfSyslogConformance=_HpicfSyslogConformance_ObjectIdentity((1,3,6,1,4,1,11,2,14,14,1,3))
_HpicfSyslogGroups_ObjectIdentity=ObjectIdentity
hpicfSyslogGroups=_HpicfSyslogGroups_ObjectIdentity((1,3,6,1,4,1,11,2,14,14,1,3,1))
_HpicfSyslogCompliances_ObjectIdentity=ObjectIdentity
hpicfSyslogCompliances=_HpicfSyslogCompliances_ObjectIdentity((1,3,6,1,4,1,11,2,14,14,1,3,2))
hpicfSyslogOperationsGroup=ObjectGroup((1,3,6,1,4,1,11,2,14,14,1,3,1,1))
hpicfSyslogOperationsGroup.setObjects(*((_A,_k),(_A,_l),(_A,_m),(_A,_n),(_A,_o),(_A,_p),(_A,_q),(_A,_R)))
if mibBuilder.loadTexts:hpicfSyslogOperationsGroup.setStatus(_B)
hpicfSyslogControlGroup=ObjectGroup((1,3,6,1,4,1,11,2,14,14,1,3,1,2))
hpicfSyslogControlGroup.setObjects(*((_A,_S),(_A,_T),(_A,_H),(_A,_U)))
if mibBuilder.loadTexts:hpicfSyslogControlGroup.setStatus(_B)
hpicfSyslogPriorityGroup=ObjectGroup((1,3,6,1,4,1,11,2,14,14,1,3,1,3))
hpicfSyslogPriorityGroup.setObjects((_A,_V))
if mibBuilder.loadTexts:hpicfSyslogPriorityGroup.setStatus(_B)
hpicfSyslogControlGroupOobm=ObjectGroup((1,3,6,1,4,1,11,2,14,14,1,3,1,6))
hpicfSyslogControlGroupOobm.setObjects(*((_A,_H),(_A,_r)))
if mibBuilder.loadTexts:hpicfSyslogControlGroupOobm.setStatus(_B)
hpicfSyslogGeneralStatisticsGroup=ObjectGroup((1,3,6,1,4,1,11,2,14,14,1,3,1,7))
hpicfSyslogGeneralStatisticsGroup.setObjects(*((_A,_s),(_A,_t),(_A,_u),(_A,_v),(_A,_w),(_A,_x),(_A,_y)))
if mibBuilder.loadTexts:hpicfSyslogGeneralStatisticsGroup.setStatus(_B)
hpicfSyslogSeverityStatisticsGroup=ObjectGroup((1,3,6,1,4,1,11,2,14,14,1,3,1,8))
hpicfSyslogSeverityStatisticsGroup.setObjects(*((_A,_z),(_A,_A0)))
if mibBuilder.loadTexts:hpicfSyslogSeverityStatisticsGroup.setStatus(_B)
hpicfSyslogFacilityStatisticsGroup=ObjectGroup((1,3,6,1,4,1,11,2,14,14,1,3,1,9))
hpicfSyslogFacilityStatisticsGroup.setObjects(*((_A,_A1),(_A,_A2)))
if mibBuilder.loadTexts:hpicfSyslogFacilityStatisticsGroup.setStatus(_B)
hpicfSyslogControlGroupSmm=ObjectGroup((1,3,6,1,4,1,11,2,14,14,1,3,1,10))
hpicfSyslogControlGroupSmm.setObjects(*((_A,_H),(_A,_A3)))
if mibBuilder.loadTexts:hpicfSyslogControlGroupSmm.setStatus(_B)
hpicfSyslogLogMsgOptionsGroup=ObjectGroup((1,3,6,1,4,1,11,2,14,14,1,3,1,11))
hpicfSyslogLogMsgOptionsGroup.setObjects((_A,_N))
if mibBuilder.loadTexts:hpicfSyslogLogMsgOptionsGroup.setStatus(_G)
hpicfSyslogControlTransportGroup=ObjectGroup((1,3,6,1,4,1,11,2,14,14,1,3,1,12))
hpicfSyslogControlTransportGroup.setObjects(*((_A,_A4),(_A,_A5)))
if mibBuilder.loadTexts:hpicfSyslogControlTransportGroup.setStatus(_B)
hpicfSyslogServerStatisticsGroup=ObjectGroup((1,3,6,1,4,1,11,2,14,14,1,3,1,13))
hpicfSyslogServerStatisticsGroup.setObjects(*((_A,_A6),(_A,_A7),(_A,_A8),(_A,_A9),(_A,_AA),(_A,_AB),(_A,_AC)))
if mibBuilder.loadTexts:hpicfSyslogServerStatisticsGroup.setStatus(_B)
hpicfSyslogPriorityGroup1=ObjectGroup((1,3,6,1,4,1,11,2,14,14,1,3,1,14))
hpicfSyslogPriorityGroup1.setObjects(*((_A,_W),(_A,_X),(_A,_Y)))
if mibBuilder.loadTexts:hpicfSyslogPriorityGroup1.setStatus(_B)
hpicfSyslogAlertsGroup=ObjectGroup((1,3,6,1,4,1,11,2,14,14,1,3,1,15))
hpicfSyslogAlertsGroup.setObjects(*((_A,_AD),(_A,_AE)))
if mibBuilder.loadTexts:hpicfSyslogAlertsGroup.setStatus(_B)
hpicfSyslogOriginIdGroup1=ObjectGroup((1,3,6,1,4,1,11,2,14,14,1,3,1,16))
hpicfSyslogOriginIdGroup1.setObjects((_A,_AF))
if mibBuilder.loadTexts:hpicfSyslogOriginIdGroup1.setStatus(_B)
hpicfSyslogLogMsgOptionsGroup1=ObjectGroup((1,3,6,1,4,1,11,2,14,14,1,3,1,17))
hpicfSyslogLogMsgOptionsGroup1.setObjects(*((_A,_N),(_A,_Z)))
if mibBuilder.loadTexts:hpicfSyslogLogMsgOptionsGroup1.setStatus(_G)
hpicfSyslogCommandLoggingGroup1=ObjectGroup((1,3,6,1,4,1,11,2,14,14,1,3,1,18))
hpicfSyslogCommandLoggingGroup1.setObjects((_A,_AG))
if mibBuilder.loadTexts:hpicfSyslogCommandLoggingGroup1.setStatus(_G)
hpicfSyslogLogMsgOptionsGroup2=ObjectGroup((1,3,6,1,4,1,11,2,14,14,1,3,1,19))
hpicfSyslogLogMsgOptionsGroup2.setObjects(*((_A,_N),(_A,_Z),(_A,_AH)))
if mibBuilder.loadTexts:hpicfSyslogLogMsgOptionsGroup2.setStatus(_B)
hpicfSyslogControlFilterNameGroup=ObjectGroup((1,3,6,1,4,1,11,2,14,14,1,3,1,20))
hpicfSyslogControlFilterNameGroup.setObjects((_A,_AI))
if mibBuilder.loadTexts:hpicfSyslogControlFilterNameGroup.setStatus(_B)
hpicfSyslogPrefixStringGroup1=ObjectGroup((1,3,6,1,4,1,11,2,14,14,1,3,1,23))
hpicfSyslogPrefixStringGroup1.setObjects((_A,_AJ))
if mibBuilder.loadTexts:hpicfSyslogPrefixStringGroup1.setStatus(_B)
hpicfSyslogStatusChanged=NotificationType((1,3,6,1,4,1,11,2,14,14,1,0,1))
hpicfSyslogStatusChanged.setObjects(*((_A,_L),(_A,_S),(_A,_T),(_A,_H),(_A,_U),(_A,_V),(_A,_X),(_A,_W),(_A,_Y),(_A,_R)))
if mibBuilder.loadTexts:hpicfSyslogStatusChanged.setStatus(_B)
hpicfSyslogNotificationGroup=NotificationGroup((1,3,6,1,4,1,11,2,14,14,1,3,1,5))
hpicfSyslogNotificationGroup.setObjects((_A,_AK))
if mibBuilder.loadTexts:hpicfSyslogNotificationGroup.setStatus(_B)
hpicfSyslogFullCompliance1=ModuleCompliance((1,3,6,1,4,1,11,2,14,14,1,3,2,1))
hpicfSyslogFullCompliance1.setObjects(*((_A,_O),(_A,_I),(_A,_J),(_A,_K)))
if mibBuilder.loadTexts:hpicfSyslogFullCompliance1.setStatus(_B)
hpicfSyslogFullCompliance2=ModuleCompliance((1,3,6,1,4,1,11,2,14,14,1,3,2,2))
hpicfSyslogFullCompliance2.setObjects(*((_A,_I),(_A,_J),(_A,_K)))
if mibBuilder.loadTexts:hpicfSyslogFullCompliance2.setStatus(_B)
hpicfSyslogReadOnlyCompliance1=ModuleCompliance((1,3,6,1,4,1,11,2,14,14,1,3,2,4))
hpicfSyslogReadOnlyCompliance1.setObjects(*((_A,_O),(_A,_I),(_A,_J),(_A,_K)))
if mibBuilder.loadTexts:hpicfSyslogReadOnlyCompliance1.setStatus(_B)
hpicfSyslogReadOnlyCompliance2=ModuleCompliance((1,3,6,1,4,1,11,2,14,14,1,3,2,5))
hpicfSyslogReadOnlyCompliance2.setObjects(*((_A,_I),(_A,_J),(_A,_K)))
if mibBuilder.loadTexts:hpicfSyslogReadOnlyCompliance2.setStatus(_B)
hpicfSyslogNotificationCompliance=ModuleCompliance((1,3,6,1,4,1,11,2,14,14,1,3,2,7))
hpicfSyslogNotificationCompliance.setObjects((_A,_O))
if mibBuilder.loadTexts:hpicfSyslogNotificationCompliance.setStatus(_B)
hpicfSyslogFullComplianceOobm=ModuleCompliance((1,3,6,1,4,1,11,2,14,14,1,3,2,8))
hpicfSyslogFullComplianceOobm.setObjects((_A,_AL))
if mibBuilder.loadTexts:hpicfSyslogFullComplianceOobm.setStatus(_B)
hpicfSyslogStatisticsCompliance=ModuleCompliance((1,3,6,1,4,1,11,2,14,14,1,3,2,9))
hpicfSyslogStatisticsCompliance.setObjects(*((_A,_AM),(_A,_AN),(_A,_AO)))
if mibBuilder.loadTexts:hpicfSyslogStatisticsCompliance.setStatus(_B)
hpicfSyslogSmmLogMsgCompliance=ModuleCompliance((1,3,6,1,4,1,11,2,14,14,1,3,2,10))
hpicfSyslogSmmLogMsgCompliance.setObjects(*((_A,_P),(_A,_AP)))
if mibBuilder.loadTexts:hpicfSyslogSmmLogMsgCompliance.setStatus(_G)
hpicfSyslogTransportCompliance=ModuleCompliance((1,3,6,1,4,1,11,2,14,14,1,3,2,11))
hpicfSyslogTransportCompliance.setObjects((_A,_AQ))
if mibBuilder.loadTexts:hpicfSyslogTransportCompliance.setStatus(_B)
hpicfSyslogPriorityCompliance=ModuleCompliance((1,3,6,1,4,1,11,2,14,14,1,3,2,12))
hpicfSyslogPriorityCompliance.setObjects((_A,_AR))
if mibBuilder.loadTexts:hpicfSyslogPriorityCompliance.setStatus(_B)
hpicfSyslogServerStatisticsCompliance=ModuleCompliance((1,3,6,1,4,1,11,2,14,14,1,3,2,13))
hpicfSyslogServerStatisticsCompliance.setObjects((_A,_AS))
if mibBuilder.loadTexts:hpicfSyslogServerStatisticsCompliance.setStatus(_B)
hpicfSyslogAlertsCompliance=ModuleCompliance((1,3,6,1,4,1,11,2,14,14,1,3,2,14))
hpicfSyslogAlertsCompliance.setObjects((_A,_AT))
if mibBuilder.loadTexts:hpicfSyslogAlertsCompliance.setStatus(_B)
hpicfSyslogOriginIdCompliance=ModuleCompliance((1,3,6,1,4,1,11,2,14,14,1,3,2,15))
hpicfSyslogOriginIdCompliance.setObjects((_A,_AU))
if mibBuilder.loadTexts:hpicfSyslogOriginIdCompliance.setStatus(_B)
hpicfSyslogSmmLogMsgCompliance1=ModuleCompliance((1,3,6,1,4,1,11,2,14,14,1,3,2,16))
hpicfSyslogSmmLogMsgCompliance1.setObjects(*((_A,_P),(_A,_AV)))
if mibBuilder.loadTexts:hpicfSyslogSmmLogMsgCompliance1.setStatus(_G)
hpicfSyslogCommandLoggingCompliance=ModuleCompliance((1,3,6,1,4,1,11,2,14,14,1,3,2,17))
hpicfSyslogCommandLoggingCompliance.setObjects((_A,_AW))
if mibBuilder.loadTexts:hpicfSyslogCommandLoggingCompliance.setStatus(_G)
hpicfSyslogSmmLogMsgCompliance2=ModuleCompliance((1,3,6,1,4,1,11,2,14,14,1,3,2,18))
hpicfSyslogSmmLogMsgCompliance2.setObjects(*((_A,_P),(_A,_AX)))
if mibBuilder.loadTexts:hpicfSyslogSmmLogMsgCompliance2.setStatus(_B)
hpicfSyslogTransportFilterNameCompliance=ModuleCompliance((1,3,6,1,4,1,11,2,14,14,1,3,2,19))
hpicfSyslogTransportFilterNameCompliance.setObjects((_A,_AY))
if mibBuilder.loadTexts:hpicfSyslogTransportFilterNameCompliance.setStatus(_B)
hpicfSyslogPrefixStringCompliance=ModuleCompliance((1,3,6,1,4,1,11,2,14,14,1,3,2,22))
hpicfSyslogPrefixStringCompliance.setObjects((_A,_AZ))
if mibBuilder.loadTexts:hpicfSyslogPrefixStringCompliance.setStatus(_B)
mibBuilder.exportSymbols(_A,**{_d:HpicfSyslogFacility,_e:HpicfSyslogSeverity,_f:HpicfSyslogSystemModule,_g:HpicfSyslogOriginId,'hpicfSyslogMIB':hpicfSyslogMIB,'hpicfSyslogNotifications':hpicfSyslogNotifications,_AK:hpicfSyslogStatusChanged,'hpicfSyslogObjects':hpicfSyslogObjects,'hpicfSyslogControlTable':hpicfSyslogControlTable,'hpicfSyslogControlEntry':hpicfSyslogControlEntry,_L:hpicfSyslogControlIndex,_S:hpicfSyslogControlDescr,_T:hpicfSyslogControlBindAddrType,_H:hpicfSyslogControlBindAddr,_U:hpicfSyslogControlRowStatus,_r:hpicfSyslogControlBindAddrIsOobm,_A3:hpicfSyslogControlSmmLog,_A4:hpicfSyslogControlTransportProtocol,_A5:hpicfSyslogControlDestinationPort,_AI:hpicfSyslogControlFilterName,'hpicfSyslogOperations':hpicfSyslogOperations,_k:hpicfSyslogOperationsMsgsTransmitted,_l:hpicfSyslogOperationsMsgsDropped,_m:hpicfSyslogOperationsLastMsgTransmittedTime,_n:hpicfSyslogOperationsStartTime,_o:hpicfSyslogOperationsLastError,_p:hpicfSyslogOperationsLastErrorTime,_q:hpicfSyslogOperationsCounterDiscontinuityTime,_R:hpicfSyslogOperationsStatus,'hpicfSyslogPriority':hpicfSyslogPriority,_W:hpicfSyslogPriorityFacility,_X:hpicfSyslogPrioritySeverity,_V:hpicfSyslogPriorityDescr,_Y:hpicfSyslogSystemModule,_AF:hpicfSyslogOriginId,_AJ:hpicfSyslogPrefixString,'hpicfSyslogStatistics':hpicfSyslogStatistics,'hpicfSyslogGeneralStatistics':hpicfSyslogGeneralStatistics,_s:hpicfSyslogGeneralLogSent,_t:hpicfSyslogGeneralLogRecv,_u:hpicfSyslogGeneralLogRelay,_v:hpicfSyslogGeneralSendError,_w:hpicfSyslogGeneralLogResend,_x:hpicfSyslogGeneralResendError,_y:hpicfSyslogGeneralLogBuffered,'hpicfSyslogSeverityStatistics':hpicfSyslogSeverityStatistics,'hpicfSyslogSeverityCounterInfoTable':hpicfSyslogSeverityCounterInfoTable,'hpicfSyslogSeverityCounterInfoEntry':hpicfSyslogSeverityCounterInfoEntry,_h:hpicfSyslogSeverityTypeIndex,_z:hpicfSyslogSeverityType,_A0:hpicfSyslogSeverityCounter,'hpicfSyslogFacilityStatistics':hpicfSyslogFacilityStatistics,'hpicfSyslogFacilityCounterInfoTable':hpicfSyslogFacilityCounterInfoTable,'hpicfSyslogFacilityCounterInfoEntry':hpicfSyslogFacilityCounterInfoEntry,_i:hpicfSyslogfacilityCounterIndex,_A1:hpicfSyslogfacilityType,_A2:hpicfSyslogfacilityCounter,'hpicfSyslogLogMsgOptions':hpicfSyslogLogMsgOptions,_N:hpicfSyslogClearLog,_Z:hpicfSyslogSecClearLog,_AH:hpicfSyslogCmdClearLog,'hpicfSyslogServerStatisticsTable':hpicfSyslogServerStatisticsTable,'hpicfSyslogServerStatisticsEntry':hpicfSyslogServerStatisticsEntry,_A6:hpicfSyslogServerLogSent,_A7:hpicfSyslogServerLogRecv,_A8:hpicfSyslogServerLogRelay,_A9:hpicfSyslogServerSendError,_AA:hpicfSyslogServerLogResend,_AB:hpicfSyslogServerResendError,_AC:hpicfSyslogServerLogBuffered,'hpicfSyslogAlerts':hpicfSyslogAlerts,'hpicfSyslogAlertsTable':hpicfSyslogAlertsTable,'hpicfSyslogAlertsEntry':hpicfSyslogAlertsEntry,_j:hpicfSyslogAlertIndex,_AD:hpicfSyslogAlertAdminStatus,_AE:hpicfSyslogAlertTransmitInterval,'hpicfSyslogLogging':hpicfSyslogLogging,_AG:hpicfSyslogCommandLogging,'hpicfSyslogConformance':hpicfSyslogConformance,'hpicfSyslogGroups':hpicfSyslogGroups,_I:hpicfSyslogOperationsGroup,_J:hpicfSyslogControlGroup,_K:hpicfSyslogPriorityGroup,_O:hpicfSyslogNotificationGroup,_AL:hpicfSyslogControlGroupOobm,_AM:hpicfSyslogGeneralStatisticsGroup,_AN:hpicfSyslogSeverityStatisticsGroup,_AO:hpicfSyslogFacilityStatisticsGroup,_P:hpicfSyslogControlGroupSmm,_AP:hpicfSyslogLogMsgOptionsGroup,_AQ:hpicfSyslogControlTransportGroup,_AS:hpicfSyslogServerStatisticsGroup,_AR:hpicfSyslogPriorityGroup1,_AT:hpicfSyslogAlertsGroup,_AU:hpicfSyslogOriginIdGroup1,_AV:hpicfSyslogLogMsgOptionsGroup1,_AW:hpicfSyslogCommandLoggingGroup1,_AX:hpicfSyslogLogMsgOptionsGroup2,_AY:hpicfSyslogControlFilterNameGroup,_AZ:hpicfSyslogPrefixStringGroup1,'hpicfSyslogCompliances':hpicfSyslogCompliances,'hpicfSyslogFullCompliance1':hpicfSyslogFullCompliance1,'hpicfSyslogFullCompliance2':hpicfSyslogFullCompliance2,'hpicfSyslogReadOnlyCompliance1':hpicfSyslogReadOnlyCompliance1,'hpicfSyslogReadOnlyCompliance2':hpicfSyslogReadOnlyCompliance2,'hpicfSyslogNotificationCompliance':hpicfSyslogNotificationCompliance,'hpicfSyslogFullComplianceOobm':hpicfSyslogFullComplianceOobm,'hpicfSyslogStatisticsCompliance':hpicfSyslogStatisticsCompliance,'hpicfSyslogSmmLogMsgCompliance':hpicfSyslogSmmLogMsgCompliance,'hpicfSyslogTransportCompliance':hpicfSyslogTransportCompliance,'hpicfSyslogPriorityCompliance':hpicfSyslogPriorityCompliance,'hpicfSyslogServerStatisticsCompliance':hpicfSyslogServerStatisticsCompliance,'hpicfSyslogAlertsCompliance':hpicfSyslogAlertsCompliance,'hpicfSyslogOriginIdCompliance':hpicfSyslogOriginIdCompliance,'hpicfSyslogSmmLogMsgCompliance1':hpicfSyslogSmmLogMsgCompliance1,'hpicfSyslogCommandLoggingCompliance':hpicfSyslogCommandLoggingCompliance,'hpicfSyslogSmmLogMsgCompliance2':hpicfSyslogSmmLogMsgCompliance2,'hpicfSyslogTransportFilterNameCompliance':hpicfSyslogTransportFilterNameCompliance,'hpicfSyslogPrefixStringCompliance':hpicfSyslogPrefixStringCompliance})