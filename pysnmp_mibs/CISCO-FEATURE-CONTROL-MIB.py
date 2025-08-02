_s='cfcFeatureSetNotificationGroup'
_r='cfcFeatureSetNotificationCtrlGroup'
_q='cfcFeatureSetGroup'
_p='cfcNotificationGroup'
_o='cfcFeatureGroup'
_n='ciscoFeatureSetOpStatusChange'
_m='ciscoFeatOpStatusChange'
_l='ciscoFeatureOpStatusChange'
_k='cfcFeatureSetNotifEnable'
_j='cfcFeatureSetOpStatusReason'
_i='cfcFeatureSetLastFailureReason'
_h='cfcFeatureSetLastActionResult'
_g='cfcFeatureSetLastAction'
_f='cfcFeatureSetAction'
_e='cfcFeatureSetName'
_d='cfcFeatureCtrlOpStatusReason2'
_c='cfcFeatureCtrlLastFailureReason2'
_b='cfcFeatureCtrlLastActionResult2'
_a='cfcFeatureCtrlLastAction2'
_Z='cfcFeatureCtrlAction2'
_Y='cfcFeatureCtrlTag2'
_X='cfcFeatureCtrlName2'
_W='cfcFeatureCtrlOpStatusReason'
_V='cfcFeatureCtrlLastFailureReason'
_U='cfcFeatureCtrlLastActionResult'
_T='cfcFeatureCtrlLastAction'
_S='cfcFeatureCtrlAction'
_R='cfcFeatureCtrlName'
_Q='cfcFeatureSetIndex'
_P='cfcFeatureCtrlInstanceNum2'
_O='cfcFeatureCtrlIndex2'
_N='cfcFeatureCtrlIndex'
_M='TruthValue'
_L='cfcNotificationGroupRev'
_K='cfcFeatureGroupRev'
_J='cfcFeatureSetOpStatus'
_I='cfcFeatureCtrlOpStatus2'
_H='cfcFeatureCtrlOpStatus'
_G='not-accessible'
_F='SnmpAdminString'
_E='read-write'
_D='deprecated'
_C='read-only'
_B='current'
_A='CISCO-FEATURE-CONTROL-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB',_F)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention',_M)
ciscoFeatureCtrlMIB=ModuleIdentity((1,3,6,1,4,1,9,9,377))
if mibBuilder.loadTexts:ciscoFeatureCtrlMIB.setRevisions(('2021-09-21 00:00','2020-03-17 00:00','2016-11-16 00:00','2016-10-25 00:00','2016-03-11 00:00','2015-10-09 00:00','2014-12-24 00:00','2014-04-09 00:00','2013-07-29 00:00','2013-05-28 00:00','2012-03-22 00:00','2011-06-09 00:00','2009-08-11 00:00','2008-12-05 00:00','2008-06-27 00:00','2008-06-12 00:00','2008-03-13 00:00','2007-05-04 00:00','2007-01-22 00:00','2005-12-27 00:00','2004-12-28 00:00','2004-07-06 00:00','2003-11-22 00:00'))
class CiscoOptionalFeature(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,134,135,136,137,138,139,140,141,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,165,166,167,168,169,170,171,172,173,174,175,176,177,200,211,212,215,216,217,218,219,220,221,225,226,262,264,265,9875)));namedValues=NamedValues(*(('ivr',1),('fcip',2),('fcsp',3),('ficon',4),('iscsi',5),('tacacs',6),('qosManager',7),('portSecurity',8),('fabricBinding',9),('iscsiInterfaceVsanMembership',10),('ike',11),('isns',12),('ipSec',13),('portTracker',14),('scheduler',15),('npiv',16),('sanExtTuner',17),('dpvm',18),('extenedCredit',19),('cloudDiscovery',20),('isis',21),('ospf',22),('ospfV3',23),('rip',24),('bgp',25),('pim',26),('igmp',27),('msdp',28),('pim6',29),('eigrp',30),('sdv',31),('cluster',32),('sme',33),('lacp',34),('amt',35),('dot1x',36),('npv',37),('l2nac',38),('glbp',39),('dhcpSnooping',40),('hsrp',41),('svi',42),('vmm',43),('pvlan',44),('tunnelManager',45),('ethPortSec',46),('lisp',47),('trustSec',48),('copp',49),('udld',50),('mcecm',51),('pbr',52),('nfm',53),('isapi',54),('vrrp',55),('netSift',56),('isisL2',57),('cimServer',58),('otv',59),('sanTap',60),('nasb',61),('dmm',62),('u2rib',63),('isisOtv',64),('orib',65),('fcoe',66),('siaServiceBroker',67),('evfp',68),('vtp',69),('splitter',70),('sfm',71),('ioa',72),('telnetServer',73),('sshServer',74),('httpServer',75),('wccp',76),('siaSve',77),('xcvrFreq',78),('assocMgr',79),('lldp',80),('rsvp',81),('ldp',82),('te',83),('mplsOam',84),('l2vpn',85),('drap',86),('bfd',87),('bfdApp',88),('fex',89),('pong',90),('rtp',91),('ldap',92),('privilege',93),('oim',94),('mplsMgr',95),('ulib',96),('scp',97),('sftp',98),('l3vpn',99),('mvpn',101),('ipPool',102),('uufb',103),('umfb',104),('ethernetNpv',105),('wccpClient',106),('scadaGw',107),('poe',108),('flexlink',109),('niv',110),('vem',111),('ewise',112),('onep',113),('slaS',114),('slaR',115),('rise',116),('pppManager',117),('itronMcastAgent',118),('vsmAggregation',119),('segmentation',120),('vrrpv3',121),('vTracker',122),('fdmi',123),('cmm',124),('ntp',125),('fabricAccess',126),('nat',127),('vlanVnSeg',128),('bulkStat',129),('bbu',130),('vnSegment',131),('evb',132),('ngMvpn',134),('hmm',135),('vxlan',136),('mvrp',137),('evmed',138),('nSegMgr',139),('vff',140),('sol',141),('nxapi',143),('itd',144),('vmTracker',145),('xosFeatureTest',146),('xosMIFeatureTest',147),('nxschema',148),('mplsStatic',149),('imp',150),('evc',151),('ptp',152),('bashShell',153),('nxdb',154),('ngoam',155),('mld',156),('evpn',157),('smartChannel',158),('openFlow',159),('mplsSegmentRouting',160),('analytics',161),('ipp',162),('licenseSmart',163),('pmn',164),('dpt',165),('ngmvpn',166),('dciTunnelInterop',167),('fabricTelemetry',168),('plb',169),('vmis',170),('ldbmgr',171),('icam',172),('catena',173),('licensePlr',174),('containerTracker',175),('mka',176),('nxsdkMgr',177),('poap',200),('bench',211),('pnp',212),('netconf',215),('restconf',216),('grpc',217),('slaTwamp',218),('mldx',219),('lispMs',220),('srv6',221),('tem',225),('fpm',226),('telemetry',262),('sflow',264),('hwTelemetry',265),('elo',9875)))
class CiscoOptionalFeatureSet(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,7,8)));namedValues=NamedValues(*(('fcoe',1),('l2mp',2),('fex',3),('mpls',4),('fabric',7),('fcoenpv',8)))
class CiscoFeatureAction(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*(('noOp',1),('enable',2),('disable',3),('install',4),('uninstall',5),('allow',6),('disallow',7)))
class CiscoFeatureStatus(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*(('unknown',1),('enabled',2),('disabled',3),('installed',4),('uninstalled',5),('enabledNotRunning',6)))
class CiscoFeatureActionResult(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('none',1),('actionSuccess',2),('actionFailed',3),('actionInProgress',4)))
_CiscoFeatureCtrlMIBNotifs_ObjectIdentity=ObjectIdentity
ciscoFeatureCtrlMIBNotifs=_CiscoFeatureCtrlMIBNotifs_ObjectIdentity((1,3,6,1,4,1,9,9,377,0))
_CiscoFeatureCtrlMIBObjects_ObjectIdentity=ObjectIdentity
ciscoFeatureCtrlMIBObjects=_CiscoFeatureCtrlMIBObjects_ObjectIdentity((1,3,6,1,4,1,9,9,377,1))
_CfcFeature_ObjectIdentity=ObjectIdentity
cfcFeature=_CfcFeature_ObjectIdentity((1,3,6,1,4,1,9,9,377,1,1))
_CfcFeatureCtrlTable_Object=MibTable
cfcFeatureCtrlTable=_CfcFeatureCtrlTable_Object((1,3,6,1,4,1,9,9,377,1,1,1))
if mibBuilder.loadTexts:cfcFeatureCtrlTable.setStatus(_D)
_CfcFeatureCtrlEntry_Object=MibTableRow
cfcFeatureCtrlEntry=_CfcFeatureCtrlEntry_Object((1,3,6,1,4,1,9,9,377,1,1,1,1))
cfcFeatureCtrlEntry.setIndexNames((0,_A,_N))
if mibBuilder.loadTexts:cfcFeatureCtrlEntry.setStatus(_D)
_CfcFeatureCtrlIndex_Type=CiscoOptionalFeature
_CfcFeatureCtrlIndex_Object=MibTableColumn
cfcFeatureCtrlIndex=_CfcFeatureCtrlIndex_Object((1,3,6,1,4,1,9,9,377,1,1,1,1,1),_CfcFeatureCtrlIndex_Type())
cfcFeatureCtrlIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:cfcFeatureCtrlIndex.setStatus(_D)
class _CfcFeatureCtrlName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_CfcFeatureCtrlName_Type.__name__=_F
_CfcFeatureCtrlName_Object=MibTableColumn
cfcFeatureCtrlName=_CfcFeatureCtrlName_Object((1,3,6,1,4,1,9,9,377,1,1,1,1,2),_CfcFeatureCtrlName_Type())
cfcFeatureCtrlName.setMaxAccess(_C)
if mibBuilder.loadTexts:cfcFeatureCtrlName.setStatus(_D)
_CfcFeatureCtrlAction_Type=CiscoFeatureAction
_CfcFeatureCtrlAction_Object=MibTableColumn
cfcFeatureCtrlAction=_CfcFeatureCtrlAction_Object((1,3,6,1,4,1,9,9,377,1,1,1,1,3),_CfcFeatureCtrlAction_Type())
cfcFeatureCtrlAction.setMaxAccess(_E)
if mibBuilder.loadTexts:cfcFeatureCtrlAction.setStatus(_D)
_CfcFeatureCtrlLastAction_Type=CiscoFeatureAction
_CfcFeatureCtrlLastAction_Object=MibTableColumn
cfcFeatureCtrlLastAction=_CfcFeatureCtrlLastAction_Object((1,3,6,1,4,1,9,9,377,1,1,1,1,4),_CfcFeatureCtrlLastAction_Type())
cfcFeatureCtrlLastAction.setMaxAccess(_C)
if mibBuilder.loadTexts:cfcFeatureCtrlLastAction.setStatus(_D)
_CfcFeatureCtrlLastActionResult_Type=CiscoFeatureActionResult
_CfcFeatureCtrlLastActionResult_Object=MibTableColumn
cfcFeatureCtrlLastActionResult=_CfcFeatureCtrlLastActionResult_Object((1,3,6,1,4,1,9,9,377,1,1,1,1,5),_CfcFeatureCtrlLastActionResult_Type())
cfcFeatureCtrlLastActionResult.setMaxAccess(_C)
if mibBuilder.loadTexts:cfcFeatureCtrlLastActionResult.setStatus(_D)
_CfcFeatureCtrlLastFailureReason_Type=SnmpAdminString
_CfcFeatureCtrlLastFailureReason_Object=MibTableColumn
cfcFeatureCtrlLastFailureReason=_CfcFeatureCtrlLastFailureReason_Object((1,3,6,1,4,1,9,9,377,1,1,1,1,6),_CfcFeatureCtrlLastFailureReason_Type())
cfcFeatureCtrlLastFailureReason.setMaxAccess(_C)
if mibBuilder.loadTexts:cfcFeatureCtrlLastFailureReason.setStatus(_D)
_CfcFeatureCtrlOpStatus_Type=CiscoFeatureStatus
_CfcFeatureCtrlOpStatus_Object=MibTableColumn
cfcFeatureCtrlOpStatus=_CfcFeatureCtrlOpStatus_Object((1,3,6,1,4,1,9,9,377,1,1,1,1,7),_CfcFeatureCtrlOpStatus_Type())
cfcFeatureCtrlOpStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:cfcFeatureCtrlOpStatus.setStatus(_D)
_CfcFeatureCtrlOpStatusReason_Type=SnmpAdminString
_CfcFeatureCtrlOpStatusReason_Object=MibTableColumn
cfcFeatureCtrlOpStatusReason=_CfcFeatureCtrlOpStatusReason_Object((1,3,6,1,4,1,9,9,377,1,1,1,1,8),_CfcFeatureCtrlOpStatusReason_Type())
cfcFeatureCtrlOpStatusReason.setMaxAccess(_C)
if mibBuilder.loadTexts:cfcFeatureCtrlOpStatusReason.setStatus(_D)
_CfcFeatureCtrl2Table_Object=MibTable
cfcFeatureCtrl2Table=_CfcFeatureCtrl2Table_Object((1,3,6,1,4,1,9,9,377,1,1,2))
if mibBuilder.loadTexts:cfcFeatureCtrl2Table.setStatus(_B)
_CfcFeatureCtrl2Entry_Object=MibTableRow
cfcFeatureCtrl2Entry=_CfcFeatureCtrl2Entry_Object((1,3,6,1,4,1,9,9,377,1,1,2,1))
cfcFeatureCtrl2Entry.setIndexNames((0,_A,_O),(0,_A,_P))
if mibBuilder.loadTexts:cfcFeatureCtrl2Entry.setStatus(_B)
_CfcFeatureCtrlIndex2_Type=CiscoOptionalFeature
_CfcFeatureCtrlIndex2_Object=MibTableColumn
cfcFeatureCtrlIndex2=_CfcFeatureCtrlIndex2_Object((1,3,6,1,4,1,9,9,377,1,1,2,1,1),_CfcFeatureCtrlIndex2_Type())
cfcFeatureCtrlIndex2.setMaxAccess(_G)
if mibBuilder.loadTexts:cfcFeatureCtrlIndex2.setStatus(_B)
_CfcFeatureCtrlInstanceNum2_Type=Unsigned32
_CfcFeatureCtrlInstanceNum2_Object=MibTableColumn
cfcFeatureCtrlInstanceNum2=_CfcFeatureCtrlInstanceNum2_Object((1,3,6,1,4,1,9,9,377,1,1,2,1,2),_CfcFeatureCtrlInstanceNum2_Type())
cfcFeatureCtrlInstanceNum2.setMaxAccess(_G)
if mibBuilder.loadTexts:cfcFeatureCtrlInstanceNum2.setStatus(_B)
class _CfcFeatureCtrlName2_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_CfcFeatureCtrlName2_Type.__name__=_F
_CfcFeatureCtrlName2_Object=MibTableColumn
cfcFeatureCtrlName2=_CfcFeatureCtrlName2_Object((1,3,6,1,4,1,9,9,377,1,1,2,1,3),_CfcFeatureCtrlName2_Type())
cfcFeatureCtrlName2.setMaxAccess(_C)
if mibBuilder.loadTexts:cfcFeatureCtrlName2.setStatus(_B)
_CfcFeatureCtrlAction2_Type=CiscoFeatureAction
_CfcFeatureCtrlAction2_Object=MibTableColumn
cfcFeatureCtrlAction2=_CfcFeatureCtrlAction2_Object((1,3,6,1,4,1,9,9,377,1,1,2,1,4),_CfcFeatureCtrlAction2_Type())
cfcFeatureCtrlAction2.setMaxAccess(_E)
if mibBuilder.loadTexts:cfcFeatureCtrlAction2.setStatus(_B)
_CfcFeatureCtrlLastAction2_Type=CiscoFeatureAction
_CfcFeatureCtrlLastAction2_Object=MibTableColumn
cfcFeatureCtrlLastAction2=_CfcFeatureCtrlLastAction2_Object((1,3,6,1,4,1,9,9,377,1,1,2,1,5),_CfcFeatureCtrlLastAction2_Type())
cfcFeatureCtrlLastAction2.setMaxAccess(_C)
if mibBuilder.loadTexts:cfcFeatureCtrlLastAction2.setStatus(_B)
_CfcFeatureCtrlLastActionResult2_Type=CiscoFeatureActionResult
_CfcFeatureCtrlLastActionResult2_Object=MibTableColumn
cfcFeatureCtrlLastActionResult2=_CfcFeatureCtrlLastActionResult2_Object((1,3,6,1,4,1,9,9,377,1,1,2,1,6),_CfcFeatureCtrlLastActionResult2_Type())
cfcFeatureCtrlLastActionResult2.setMaxAccess(_C)
if mibBuilder.loadTexts:cfcFeatureCtrlLastActionResult2.setStatus(_B)
_CfcFeatureCtrlLastFailureReason2_Type=SnmpAdminString
_CfcFeatureCtrlLastFailureReason2_Object=MibTableColumn
cfcFeatureCtrlLastFailureReason2=_CfcFeatureCtrlLastFailureReason2_Object((1,3,6,1,4,1,9,9,377,1,1,2,1,7),_CfcFeatureCtrlLastFailureReason2_Type())
cfcFeatureCtrlLastFailureReason2.setMaxAccess(_C)
if mibBuilder.loadTexts:cfcFeatureCtrlLastFailureReason2.setStatus(_B)
_CfcFeatureCtrlOpStatus2_Type=CiscoFeatureStatus
_CfcFeatureCtrlOpStatus2_Object=MibTableColumn
cfcFeatureCtrlOpStatus2=_CfcFeatureCtrlOpStatus2_Object((1,3,6,1,4,1,9,9,377,1,1,2,1,8),_CfcFeatureCtrlOpStatus2_Type())
cfcFeatureCtrlOpStatus2.setMaxAccess(_C)
if mibBuilder.loadTexts:cfcFeatureCtrlOpStatus2.setStatus(_B)
_CfcFeatureCtrlOpStatusReason2_Type=SnmpAdminString
_CfcFeatureCtrlOpStatusReason2_Object=MibTableColumn
cfcFeatureCtrlOpStatusReason2=_CfcFeatureCtrlOpStatusReason2_Object((1,3,6,1,4,1,9,9,377,1,1,2,1,9),_CfcFeatureCtrlOpStatusReason2_Type())
cfcFeatureCtrlOpStatusReason2.setMaxAccess(_C)
if mibBuilder.loadTexts:cfcFeatureCtrlOpStatusReason2.setStatus(_B)
class _CfcFeatureCtrlTag2_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_CfcFeatureCtrlTag2_Type.__name__=_F
_CfcFeatureCtrlTag2_Object=MibTableColumn
cfcFeatureCtrlTag2=_CfcFeatureCtrlTag2_Object((1,3,6,1,4,1,9,9,377,1,1,2,1,10),_CfcFeatureCtrlTag2_Type())
cfcFeatureCtrlTag2.setMaxAccess(_E)
if mibBuilder.loadTexts:cfcFeatureCtrlTag2.setStatus(_B)
_CfcFeatureSetTable_Object=MibTable
cfcFeatureSetTable=_CfcFeatureSetTable_Object((1,3,6,1,4,1,9,9,377,1,1,3))
if mibBuilder.loadTexts:cfcFeatureSetTable.setStatus(_B)
_CfcFeatureSetEntry_Object=MibTableRow
cfcFeatureSetEntry=_CfcFeatureSetEntry_Object((1,3,6,1,4,1,9,9,377,1,1,3,1))
cfcFeatureSetEntry.setIndexNames((0,_A,_Q))
if mibBuilder.loadTexts:cfcFeatureSetEntry.setStatus(_B)
_CfcFeatureSetIndex_Type=CiscoOptionalFeatureSet
_CfcFeatureSetIndex_Object=MibTableColumn
cfcFeatureSetIndex=_CfcFeatureSetIndex_Object((1,3,6,1,4,1,9,9,377,1,1,3,1,1),_CfcFeatureSetIndex_Type())
cfcFeatureSetIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:cfcFeatureSetIndex.setStatus(_B)
_CfcFeatureSetName_Type=SnmpAdminString
_CfcFeatureSetName_Object=MibTableColumn
cfcFeatureSetName=_CfcFeatureSetName_Object((1,3,6,1,4,1,9,9,377,1,1,3,1,2),_CfcFeatureSetName_Type())
cfcFeatureSetName.setMaxAccess(_C)
if mibBuilder.loadTexts:cfcFeatureSetName.setStatus(_B)
_CfcFeatureSetAction_Type=CiscoFeatureAction
_CfcFeatureSetAction_Object=MibTableColumn
cfcFeatureSetAction=_CfcFeatureSetAction_Object((1,3,6,1,4,1,9,9,377,1,1,3,1,3),_CfcFeatureSetAction_Type())
cfcFeatureSetAction.setMaxAccess(_E)
if mibBuilder.loadTexts:cfcFeatureSetAction.setStatus(_B)
_CfcFeatureSetLastAction_Type=CiscoFeatureAction
_CfcFeatureSetLastAction_Object=MibTableColumn
cfcFeatureSetLastAction=_CfcFeatureSetLastAction_Object((1,3,6,1,4,1,9,9,377,1,1,3,1,4),_CfcFeatureSetLastAction_Type())
cfcFeatureSetLastAction.setMaxAccess(_C)
if mibBuilder.loadTexts:cfcFeatureSetLastAction.setStatus(_B)
_CfcFeatureSetLastActionResult_Type=CiscoFeatureActionResult
_CfcFeatureSetLastActionResult_Object=MibTableColumn
cfcFeatureSetLastActionResult=_CfcFeatureSetLastActionResult_Object((1,3,6,1,4,1,9,9,377,1,1,3,1,5),_CfcFeatureSetLastActionResult_Type())
cfcFeatureSetLastActionResult.setMaxAccess(_C)
if mibBuilder.loadTexts:cfcFeatureSetLastActionResult.setStatus(_B)
_CfcFeatureSetLastFailureReason_Type=SnmpAdminString
_CfcFeatureSetLastFailureReason_Object=MibTableColumn
cfcFeatureSetLastFailureReason=_CfcFeatureSetLastFailureReason_Object((1,3,6,1,4,1,9,9,377,1,1,3,1,6),_CfcFeatureSetLastFailureReason_Type())
cfcFeatureSetLastFailureReason.setMaxAccess(_C)
if mibBuilder.loadTexts:cfcFeatureSetLastFailureReason.setStatus(_B)
_CfcFeatureSetOpStatus_Type=CiscoFeatureStatus
_CfcFeatureSetOpStatus_Object=MibTableColumn
cfcFeatureSetOpStatus=_CfcFeatureSetOpStatus_Object((1,3,6,1,4,1,9,9,377,1,1,3,1,7),_CfcFeatureSetOpStatus_Type())
cfcFeatureSetOpStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:cfcFeatureSetOpStatus.setStatus(_B)
_CfcFeatureSetOpStatusReason_Type=SnmpAdminString
_CfcFeatureSetOpStatusReason_Object=MibTableColumn
cfcFeatureSetOpStatusReason=_CfcFeatureSetOpStatusReason_Object((1,3,6,1,4,1,9,9,377,1,1,3,1,8),_CfcFeatureSetOpStatusReason_Type())
cfcFeatureSetOpStatusReason.setMaxAccess(_C)
if mibBuilder.loadTexts:cfcFeatureSetOpStatusReason.setStatus(_B)
_CfcNotifControl_ObjectIdentity=ObjectIdentity
cfcNotifControl=_CfcNotifControl_ObjectIdentity((1,3,6,1,4,1,9,9,377,1,2))
class _CfcFeatureSetNotifEnable_Type(TruthValue):defaultValue=2
_CfcFeatureSetNotifEnable_Type.__name__=_M
_CfcFeatureSetNotifEnable_Object=MibScalar
cfcFeatureSetNotifEnable=_CfcFeatureSetNotifEnable_Object((1,3,6,1,4,1,9,9,377,1,2,1),_CfcFeatureSetNotifEnable_Type())
cfcFeatureSetNotifEnable.setMaxAccess(_E)
if mibBuilder.loadTexts:cfcFeatureSetNotifEnable.setStatus(_B)
_CiscoFeatureCtrlMIBConformance_ObjectIdentity=ObjectIdentity
ciscoFeatureCtrlMIBConformance=_CiscoFeatureCtrlMIBConformance_ObjectIdentity((1,3,6,1,4,1,9,9,377,2))
_CiscoFeatureCtrlMIBCompliances_ObjectIdentity=ObjectIdentity
ciscoFeatureCtrlMIBCompliances=_CiscoFeatureCtrlMIBCompliances_ObjectIdentity((1,3,6,1,4,1,9,9,377,2,1))
_CiscoFeatureCtrlMIBGroups_ObjectIdentity=ObjectIdentity
ciscoFeatureCtrlMIBGroups=_CiscoFeatureCtrlMIBGroups_ObjectIdentity((1,3,6,1,4,1,9,9,377,2,2))
cfcFeatureGroup=ObjectGroup((1,3,6,1,4,1,9,9,377,2,2,1))
cfcFeatureGroup.setObjects(*((_A,_R),(_A,_S),(_A,_T),(_A,_U),(_A,_V),(_A,_H),(_A,_W)))
if mibBuilder.loadTexts:cfcFeatureGroup.setStatus(_D)
cfcFeatureGroupRev=ObjectGroup((1,3,6,1,4,1,9,9,377,2,2,3))
cfcFeatureGroupRev.setObjects(*((_A,_X),(_A,_Y),(_A,_Z),(_A,_a),(_A,_b),(_A,_c),(_A,_I),(_A,_d)))
if mibBuilder.loadTexts:cfcFeatureGroupRev.setStatus(_B)
cfcFeatureSetGroup=ObjectGroup((1,3,6,1,4,1,9,9,377,2,2,5))
cfcFeatureSetGroup.setObjects(*((_A,_e),(_A,_f),(_A,_g),(_A,_h),(_A,_i),(_A,_J),(_A,_j)))
if mibBuilder.loadTexts:cfcFeatureSetGroup.setStatus(_B)
cfcFeatureSetNotificationCtrlGroup=ObjectGroup((1,3,6,1,4,1,9,9,377,2,2,6))
cfcFeatureSetNotificationCtrlGroup.setObjects((_A,_k))
if mibBuilder.loadTexts:cfcFeatureSetNotificationCtrlGroup.setStatus(_B)
ciscoFeatureOpStatusChange=NotificationType((1,3,6,1,4,1,9,9,377,0,1))
ciscoFeatureOpStatusChange.setObjects((_A,_H))
if mibBuilder.loadTexts:ciscoFeatureOpStatusChange.setStatus(_D)
ciscoFeatOpStatusChange=NotificationType((1,3,6,1,4,1,9,9,377,0,2))
ciscoFeatOpStatusChange.setObjects((_A,_I))
if mibBuilder.loadTexts:ciscoFeatOpStatusChange.setStatus(_B)
ciscoFeatureSetOpStatusChange=NotificationType((1,3,6,1,4,1,9,9,377,0,3))
ciscoFeatureSetOpStatusChange.setObjects((_A,_J))
if mibBuilder.loadTexts:ciscoFeatureSetOpStatusChange.setStatus(_B)
cfcNotificationGroup=NotificationGroup((1,3,6,1,4,1,9,9,377,2,2,2))
cfcNotificationGroup.setObjects((_A,_l))
if mibBuilder.loadTexts:cfcNotificationGroup.setStatus(_D)
cfcNotificationGroupRev=NotificationGroup((1,3,6,1,4,1,9,9,377,2,2,4))
cfcNotificationGroupRev.setObjects((_A,_m))
if mibBuilder.loadTexts:cfcNotificationGroupRev.setStatus(_B)
cfcFeatureSetNotificationGroup=NotificationGroup((1,3,6,1,4,1,9,9,377,2,2,7))
cfcFeatureSetNotificationGroup.setObjects((_A,_n))
if mibBuilder.loadTexts:cfcFeatureSetNotificationGroup.setStatus(_B)
ciscoFeatureCtrlMIBCompliance=ModuleCompliance((1,3,6,1,4,1,9,9,377,2,1,1))
ciscoFeatureCtrlMIBCompliance.setObjects(*((_A,_o),(_A,_p)))
if mibBuilder.loadTexts:ciscoFeatureCtrlMIBCompliance.setStatus(_D)
ciscoFeatureCtrlMIBComplianceRev=ModuleCompliance((1,3,6,1,4,1,9,9,377,2,1,2))
ciscoFeatureCtrlMIBComplianceRev.setObjects(*((_A,_K),(_A,_L)))
if mibBuilder.loadTexts:ciscoFeatureCtrlMIBComplianceRev.setStatus(_D)
ciscoFeatureSetCtrlMIBComplianceRev1=ModuleCompliance((1,3,6,1,4,1,9,9,377,2,1,3))
ciscoFeatureSetCtrlMIBComplianceRev1.setObjects(*((_A,_q),(_A,_r),(_A,_s),(_A,_K),(_A,_L)))
if mibBuilder.loadTexts:ciscoFeatureSetCtrlMIBComplianceRev1.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'CiscoOptionalFeature':CiscoOptionalFeature,'CiscoOptionalFeatureSet':CiscoOptionalFeatureSet,'CiscoFeatureAction':CiscoFeatureAction,'CiscoFeatureStatus':CiscoFeatureStatus,'CiscoFeatureActionResult':CiscoFeatureActionResult,'ciscoFeatureCtrlMIB':ciscoFeatureCtrlMIB,'ciscoFeatureCtrlMIBNotifs':ciscoFeatureCtrlMIBNotifs,_l:ciscoFeatureOpStatusChange,_m:ciscoFeatOpStatusChange,_n:ciscoFeatureSetOpStatusChange,'ciscoFeatureCtrlMIBObjects':ciscoFeatureCtrlMIBObjects,'cfcFeature':cfcFeature,'cfcFeatureCtrlTable':cfcFeatureCtrlTable,'cfcFeatureCtrlEntry':cfcFeatureCtrlEntry,_N:cfcFeatureCtrlIndex,_R:cfcFeatureCtrlName,_S:cfcFeatureCtrlAction,_T:cfcFeatureCtrlLastAction,_U:cfcFeatureCtrlLastActionResult,_V:cfcFeatureCtrlLastFailureReason,_H:cfcFeatureCtrlOpStatus,_W:cfcFeatureCtrlOpStatusReason,'cfcFeatureCtrl2Table':cfcFeatureCtrl2Table,'cfcFeatureCtrl2Entry':cfcFeatureCtrl2Entry,_O:cfcFeatureCtrlIndex2,_P:cfcFeatureCtrlInstanceNum2,_X:cfcFeatureCtrlName2,_Z:cfcFeatureCtrlAction2,_a:cfcFeatureCtrlLastAction2,_b:cfcFeatureCtrlLastActionResult2,_c:cfcFeatureCtrlLastFailureReason2,_I:cfcFeatureCtrlOpStatus2,_d:cfcFeatureCtrlOpStatusReason2,_Y:cfcFeatureCtrlTag2,'cfcFeatureSetTable':cfcFeatureSetTable,'cfcFeatureSetEntry':cfcFeatureSetEntry,_Q:cfcFeatureSetIndex,_e:cfcFeatureSetName,_f:cfcFeatureSetAction,_g:cfcFeatureSetLastAction,_h:cfcFeatureSetLastActionResult,_i:cfcFeatureSetLastFailureReason,_J:cfcFeatureSetOpStatus,_j:cfcFeatureSetOpStatusReason,'cfcNotifControl':cfcNotifControl,_k:cfcFeatureSetNotifEnable,'ciscoFeatureCtrlMIBConformance':ciscoFeatureCtrlMIBConformance,'ciscoFeatureCtrlMIBCompliances':ciscoFeatureCtrlMIBCompliances,'ciscoFeatureCtrlMIBCompliance':ciscoFeatureCtrlMIBCompliance,'ciscoFeatureCtrlMIBComplianceRev':ciscoFeatureCtrlMIBComplianceRev,'ciscoFeatureSetCtrlMIBComplianceRev1':ciscoFeatureSetCtrlMIBComplianceRev1,'ciscoFeatureCtrlMIBGroups':ciscoFeatureCtrlMIBGroups,_o:cfcFeatureGroup,_p:cfcNotificationGroup,_K:cfcFeatureGroupRev,_L:cfcNotificationGroupRev,_q:cfcFeatureSetGroup,_r:cfcFeatureSetNotificationCtrlGroup,_s:cfcFeatureSetNotificationGroup})