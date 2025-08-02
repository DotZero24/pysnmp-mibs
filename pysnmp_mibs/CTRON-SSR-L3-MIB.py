_b='l3ConfGroupV10'
_a='l3FlowPriority'
_Z='l3FlowPriorityInterface'
_Y='l3FlowPriorityProtocol'
_X='l3FlowPriorityTOS'
_W='l3FlowPriorityDstPort'
_V='l3FlowPriorityDstIpAddress'
_U='l3FlowPrioritySrcPort'
_T='l3FlowPrioritySrcIpAddress'
_S='l3FlowPriorityName'
_R='l3FlowOctets'
_Q='l3FlowPkts'
_P='l3FlowPriorityIndex'
_O='l3FlowDstPort'
_N='l3FlowSrcPort'
_M='l3FlowProtocol'
_L='l3FlowTOS'
_K='l3FlowDstIpAddress'
_J='l3FlowSrcIpAddress'
_I='l3FlowPortOfEntry'
_H='l3FlowFilterId'
_G='l3FlowIndex'
_F='OctetString'
_E='read-write'
_D='read-only'
_C='Integer32'
_B='obsolete'
_A='CTRON-SSR-L3-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_F,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ssrMibs,=mibBuilder.importSymbols('CTRON-SSR-SMI-MIB','ssrMibs')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
l3MIB=ModuleIdentity((1,3,6,1,4,1,52,2501,1,600))
if mibBuilder.loadTexts:l3MIB.setRevisions(('1999-09-22 00:00',))
class SSRProtocols(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,255)));namedValues=NamedValues(*(('hopopt',0),('icmp',1),('igmp',2),('ggp',3),('ipip',4),('stream',5),('tcp',6),('cbt',7),('egp',8),('igp',9),('bbnrccmon',10),('nvpii',11),('pup',12),('argus',13),('emcon',14),('xnet',15),('chaos',16),('udp',17),('mux',18),('dcn',19),('hmp',20),('prm',21),('xnsidp',22),('trunk1',23),('trunk2',24),('leaf1',25),('leaf2',26),('rdp',27),('irtp',28),('isotp4',29),('netblt',30),('mfe',31),('meritInp',32),('sep',33),('tpc',34),('idpr',35),('xtp',36),('ddp',37),('idprCmtp',38),('tppp',39),('il',40),('ipv6',41),('sdrp',42),('ipv6r',43),('ipv6f',44),('idrp',45),('rsvp',46),('gre',47),('mhrp',48),('bna',49),('esp',50),('ah',51),('inlsp',52),('swipe',53),('narp',54),('mobile',55),('tlsp',56),('skip',57),('ipv6Icmp',58),('ipv6Nonxt',59),('ipv6Opts',60),('hostInternal',61),('cftp',62),('any',63),('satExpak',64),('kryptolan',65),('rvd',66),('ippc',67),('adfs',68),('satMon',69),('visa',70),('ipcv',71),('cpnx',72),('cphb',73),('wsn',74),('pvp',75),('brSatMon',76),('sunNd',77),('wbMon',78),('wbExpak',79),('isoIp',80),('vmtp',81),('secureVmtp',82),('vines',83),('ttp',84),('nsfnetIgp',85),('dgp',86),('tcf',87),('eigrp',88),('ospfigp',89),('spriteRpc',90),('larp',91),('mtp',92),('ax25',93),('ipipep',94),('micp',95),('sccSp',96),('etherip',97),('encap',98),('anyEncrpyt',99),('gmtp',100),('ifmp',101),('pnni',102),('pim',103),('aris',104),('scps',105),('qnx',106),('an',107),('ippcp',108),('snp',109),('cpqP',110),('ipxIp',111),('vrrp',112),('reserved',255)))
_L3Group_ObjectIdentity=ObjectIdentity
l3Group=_L3Group_ObjectIdentity((1,3,6,1,4,1,52,2501,1,3))
_L3FlowTable_Object=MibTable
l3FlowTable=_L3FlowTable_Object((1,3,6,1,4,1,52,2501,1,3,1))
if mibBuilder.loadTexts:l3FlowTable.setStatus(_B)
_L3FlowEntry_Object=MibTableRow
l3FlowEntry=_L3FlowEntry_Object((1,3,6,1,4,1,52,2501,1,3,1,1))
l3FlowEntry.setIndexNames((0,_A,_G),(0,_A,_H),(0,_A,_I),(0,_A,_J),(0,_A,_K),(0,_A,_L),(0,_A,_M),(0,_A,_N),(0,_A,_O))
if mibBuilder.loadTexts:l3FlowEntry.setStatus(_B)
class _L3FlowIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_L3FlowIndex_Type.__name__=_C
_L3FlowIndex_Object=MibTableColumn
l3FlowIndex=_L3FlowIndex_Object((1,3,6,1,4,1,52,2501,1,3,1,1,1),_L3FlowIndex_Type())
l3FlowIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:l3FlowIndex.setStatus(_B)
class _L3FlowFilterId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,254))
_L3FlowFilterId_Type.__name__=_C
_L3FlowFilterId_Object=MibTableColumn
l3FlowFilterId=_L3FlowFilterId_Object((1,3,6,1,4,1,52,2501,1,3,1,1,2),_L3FlowFilterId_Type())
l3FlowFilterId.setMaxAccess(_D)
if mibBuilder.loadTexts:l3FlowFilterId.setStatus(_B)
class _L3FlowPortOfEntry_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1024))
_L3FlowPortOfEntry_Type.__name__=_C
_L3FlowPortOfEntry_Object=MibTableColumn
l3FlowPortOfEntry=_L3FlowPortOfEntry_Object((1,3,6,1,4,1,52,2501,1,3,1,1,3),_L3FlowPortOfEntry_Type())
l3FlowPortOfEntry.setMaxAccess(_D)
if mibBuilder.loadTexts:l3FlowPortOfEntry.setStatus(_B)
_L3FlowSrcIpAddress_Type=IpAddress
_L3FlowSrcIpAddress_Object=MibTableColumn
l3FlowSrcIpAddress=_L3FlowSrcIpAddress_Object((1,3,6,1,4,1,52,2501,1,3,1,1,4),_L3FlowSrcIpAddress_Type())
l3FlowSrcIpAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:l3FlowSrcIpAddress.setStatus(_B)
_L3FlowDstIpAddress_Type=IpAddress
_L3FlowDstIpAddress_Object=MibTableColumn
l3FlowDstIpAddress=_L3FlowDstIpAddress_Object((1,3,6,1,4,1,52,2501,1,3,1,1,5),_L3FlowDstIpAddress_Type())
l3FlowDstIpAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:l3FlowDstIpAddress.setStatus(_B)
class _L3FlowTOS_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,15))
_L3FlowTOS_Type.__name__=_C
_L3FlowTOS_Object=MibTableColumn
l3FlowTOS=_L3FlowTOS_Object((1,3,6,1,4,1,52,2501,1,3,1,1,6),_L3FlowTOS_Type())
l3FlowTOS.setMaxAccess(_D)
if mibBuilder.loadTexts:l3FlowTOS.setStatus(_B)
_L3FlowProtocol_Type=SSRProtocols
_L3FlowProtocol_Object=MibTableColumn
l3FlowProtocol=_L3FlowProtocol_Object((1,3,6,1,4,1,52,2501,1,3,1,1,7),_L3FlowProtocol_Type())
l3FlowProtocol.setMaxAccess(_D)
if mibBuilder.loadTexts:l3FlowProtocol.setStatus(_B)
class _L3FlowSrcPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_L3FlowSrcPort_Type.__name__=_C
_L3FlowSrcPort_Object=MibTableColumn
l3FlowSrcPort=_L3FlowSrcPort_Object((1,3,6,1,4,1,52,2501,1,3,1,1,8),_L3FlowSrcPort_Type())
l3FlowSrcPort.setMaxAccess(_D)
if mibBuilder.loadTexts:l3FlowSrcPort.setStatus(_B)
class _L3FlowDstPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_L3FlowDstPort_Type.__name__=_C
_L3FlowDstPort_Object=MibTableColumn
l3FlowDstPort=_L3FlowDstPort_Object((1,3,6,1,4,1,52,2501,1,3,1,1,9),_L3FlowDstPort_Type())
l3FlowDstPort.setMaxAccess(_D)
if mibBuilder.loadTexts:l3FlowDstPort.setStatus(_B)
_L3FlowPkts_Type=Counter32
_L3FlowPkts_Object=MibTableColumn
l3FlowPkts=_L3FlowPkts_Object((1,3,6,1,4,1,52,2501,1,3,1,1,10),_L3FlowPkts_Type())
l3FlowPkts.setMaxAccess(_D)
if mibBuilder.loadTexts:l3FlowPkts.setStatus(_B)
_L3FlowOctets_Type=Counter32
_L3FlowOctets_Object=MibTableColumn
l3FlowOctets=_L3FlowOctets_Object((1,3,6,1,4,1,52,2501,1,3,1,1,11),_L3FlowOctets_Type())
l3FlowOctets.setMaxAccess(_D)
if mibBuilder.loadTexts:l3FlowOctets.setStatus(_B)
_L3FlowPriorityTable_Object=MibTable
l3FlowPriorityTable=_L3FlowPriorityTable_Object((1,3,6,1,4,1,52,2501,1,3,2))
if mibBuilder.loadTexts:l3FlowPriorityTable.setStatus(_B)
_L3FlowPriorityEntry_Object=MibTableRow
l3FlowPriorityEntry=_L3FlowPriorityEntry_Object((1,3,6,1,4,1,52,2501,1,3,2,1))
l3FlowPriorityEntry.setIndexNames((0,_A,_P))
if mibBuilder.loadTexts:l3FlowPriorityEntry.setStatus(_B)
class _L3FlowPriorityIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_L3FlowPriorityIndex_Type.__name__=_C
_L3FlowPriorityIndex_Object=MibTableColumn
l3FlowPriorityIndex=_L3FlowPriorityIndex_Object((1,3,6,1,4,1,52,2501,1,3,2,1,1),_L3FlowPriorityIndex_Type())
l3FlowPriorityIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:l3FlowPriorityIndex.setStatus(_B)
class _L3FlowPriorityName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,20))
_L3FlowPriorityName_Type.__name__=_F
_L3FlowPriorityName_Object=MibTableColumn
l3FlowPriorityName=_L3FlowPriorityName_Object((1,3,6,1,4,1,52,2501,1,3,2,1,2),_L3FlowPriorityName_Type())
l3FlowPriorityName.setMaxAccess(_E)
if mibBuilder.loadTexts:l3FlowPriorityName.setStatus(_B)
_L3FlowPrioritySrcIpAddress_Type=IpAddress
_L3FlowPrioritySrcIpAddress_Object=MibTableColumn
l3FlowPrioritySrcIpAddress=_L3FlowPrioritySrcIpAddress_Object((1,3,6,1,4,1,52,2501,1,3,2,1,3),_L3FlowPrioritySrcIpAddress_Type())
l3FlowPrioritySrcIpAddress.setMaxAccess(_E)
if mibBuilder.loadTexts:l3FlowPrioritySrcIpAddress.setStatus(_B)
class _L3FlowPrioritySrcPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_L3FlowPrioritySrcPort_Type.__name__=_C
_L3FlowPrioritySrcPort_Object=MibTableColumn
l3FlowPrioritySrcPort=_L3FlowPrioritySrcPort_Object((1,3,6,1,4,1,52,2501,1,3,2,1,4),_L3FlowPrioritySrcPort_Type())
l3FlowPrioritySrcPort.setMaxAccess(_E)
if mibBuilder.loadTexts:l3FlowPrioritySrcPort.setStatus(_B)
_L3FlowPriorityDstIpAddress_Type=IpAddress
_L3FlowPriorityDstIpAddress_Object=MibTableColumn
l3FlowPriorityDstIpAddress=_L3FlowPriorityDstIpAddress_Object((1,3,6,1,4,1,52,2501,1,3,2,1,5),_L3FlowPriorityDstIpAddress_Type())
l3FlowPriorityDstIpAddress.setMaxAccess(_E)
if mibBuilder.loadTexts:l3FlowPriorityDstIpAddress.setStatus(_B)
class _L3FlowPriorityDstPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_L3FlowPriorityDstPort_Type.__name__=_C
_L3FlowPriorityDstPort_Object=MibTableColumn
l3FlowPriorityDstPort=_L3FlowPriorityDstPort_Object((1,3,6,1,4,1,52,2501,1,3,2,1,6),_L3FlowPriorityDstPort_Type())
l3FlowPriorityDstPort.setMaxAccess(_E)
if mibBuilder.loadTexts:l3FlowPriorityDstPort.setStatus(_B)
class _L3FlowPriorityTOS_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,15))
_L3FlowPriorityTOS_Type.__name__=_C
_L3FlowPriorityTOS_Object=MibTableColumn
l3FlowPriorityTOS=_L3FlowPriorityTOS_Object((1,3,6,1,4,1,52,2501,1,3,2,1,7),_L3FlowPriorityTOS_Type())
l3FlowPriorityTOS.setMaxAccess(_E)
if mibBuilder.loadTexts:l3FlowPriorityTOS.setStatus(_B)
_L3FlowPriorityProtocol_Type=SSRProtocols
_L3FlowPriorityProtocol_Object=MibTableColumn
l3FlowPriorityProtocol=_L3FlowPriorityProtocol_Object((1,3,6,1,4,1,52,2501,1,3,2,1,8),_L3FlowPriorityProtocol_Type())
l3FlowPriorityProtocol.setMaxAccess(_E)
if mibBuilder.loadTexts:l3FlowPriorityProtocol.setStatus(_B)
class _L3FlowPriorityInterface_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_L3FlowPriorityInterface_Type.__name__=_F
_L3FlowPriorityInterface_Object=MibTableColumn
l3FlowPriorityInterface=_L3FlowPriorityInterface_Object((1,3,6,1,4,1,52,2501,1,3,2,1,9),_L3FlowPriorityInterface_Type())
l3FlowPriorityInterface.setMaxAccess(_E)
if mibBuilder.loadTexts:l3FlowPriorityInterface.setStatus(_B)
class _L3FlowPriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('low',1),('medium',2),('high',3),('control',4)))
_L3FlowPriority_Type.__name__=_C
_L3FlowPriority_Object=MibTableColumn
l3FlowPriority=_L3FlowPriority_Object((1,3,6,1,4,1,52,2501,1,3,2,1,10),_L3FlowPriority_Type())
l3FlowPriority.setMaxAccess(_E)
if mibBuilder.loadTexts:l3FlowPriority.setStatus(_B)
_L3Conformance_ObjectIdentity=ObjectIdentity
l3Conformance=_L3Conformance_ObjectIdentity((1,3,6,1,4,1,52,2501,1,600,2))
_L3Compliances_ObjectIdentity=ObjectIdentity
l3Compliances=_L3Compliances_ObjectIdentity((1,3,6,1,4,1,52,2501,1,600,2,1))
_L3Groups_ObjectIdentity=ObjectIdentity
l3Groups=_L3Groups_ObjectIdentity((1,3,6,1,4,1,52,2501,1,600,2,2))
l3ConfGroupV10=ObjectGroup((1,3,6,1,4,1,52,2501,1,600,2,2,1))
l3ConfGroupV10.setObjects(*((_A,_G),(_A,_H),(_A,_I),(_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_N),(_A,_O),(_A,_Q),(_A,_R),(_A,_P),(_A,_S),(_A,_T),(_A,_U),(_A,_V),(_A,_W),(_A,_X),(_A,_Y),(_A,_Z),(_A,_a)))
if mibBuilder.loadTexts:l3ConfGroupV10.setStatus(_B)
l3ComplianceV10=ModuleCompliance((1,3,6,1,4,1,52,2501,1,600,2,2,1,1))
l3ComplianceV10.setObjects((_A,_b))
if mibBuilder.loadTexts:l3ComplianceV10.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'SSRProtocols':SSRProtocols,'l3Group':l3Group,'l3FlowTable':l3FlowTable,'l3FlowEntry':l3FlowEntry,_G:l3FlowIndex,_H:l3FlowFilterId,_I:l3FlowPortOfEntry,_J:l3FlowSrcIpAddress,_K:l3FlowDstIpAddress,_L:l3FlowTOS,_M:l3FlowProtocol,_N:l3FlowSrcPort,_O:l3FlowDstPort,_Q:l3FlowPkts,_R:l3FlowOctets,'l3FlowPriorityTable':l3FlowPriorityTable,'l3FlowPriorityEntry':l3FlowPriorityEntry,_P:l3FlowPriorityIndex,_S:l3FlowPriorityName,_T:l3FlowPrioritySrcIpAddress,_U:l3FlowPrioritySrcPort,_V:l3FlowPriorityDstIpAddress,_W:l3FlowPriorityDstPort,_X:l3FlowPriorityTOS,_Y:l3FlowPriorityProtocol,_Z:l3FlowPriorityInterface,_a:l3FlowPriority,'l3MIB':l3MIB,'l3Conformance':l3Conformance,'l3Compliances':l3Compliances,'l3Groups':l3Groups,_b:l3ConfGroupV10,'l3ComplianceV10':l3ComplianceV10})