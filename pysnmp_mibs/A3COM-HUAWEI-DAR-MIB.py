_F='h3cDarStatisticsProtocolID'
_E='A3COM-HUAWEI-DAR-MIB'
_D='ifIndex'
_C='IF-MIB'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
h3cCommon,=mibBuilder.importSymbols('A3COM-HUAWEI-OID-MIB','h3cCommon')
ifIndex,=mibBuilder.importSymbols(_C,_D)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
h3cDar=ModuleIdentity((1,3,6,1,4,1,43,45,1,10,2,112))
class H3cDarProtocol(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89)));namedValues=NamedValues(*(('invalidProtocol',1),('bgp',2),('cifs',3),('citrix',4),('cuseeme',5),('dhcp',6),('dns',7),('egp',8),('eigrp',9),('exchange',10),('fasttrack',11),('finger',12),('ftp',13),('gnutella',14),('gopher',15),('gre',16),('http',17),('h323',18),('icmp',19),('igmp',20),('imap',21),('ip',22),('ipinip',23),('ipsec',24),('ipv6',25),('irc',26),('kerberos',27),('l2tp',28),('ldap',29),('mgcp',30),('napster',31),('netbios',32),('netshow',33),('nfs',34),('nntp',35),('notes',36),('novadign',37),('ntp',38),('pcanywhere',39),('pop3',40),('pptp',41),('printer',42),('rcmd',43),('rip',44),('rsvp',45),('rtcp',46),('rtp',47),('rtsp',48),('secureftp',49),('securehttp',50),('secureimap',51),('secureirc',52),('secureldap',53),('securenntp',54),('securepop3',55),('securetelnet',56),('sip',57),('skinny',58),('smtp',59),('snmp',60),('socks',61),('sqlnet',62),('sqlserver',63),('ssh',64),('streamwork',65),('sunrpc',66),('syslog',67),('tcp',68),('tcphandshake',69),('telnet',70),('tftp',71),('total',72),('udp',73),('unknownothers',74),('unknowntcp',75),('unknownudp',76),('userdefine001',77),('userdefine002',78),('userdefine003',79),('userdefine004',80),('userdefine005',81),('userdefine006',82),('userdefine007',83),('userdefine008',84),('userdefine009',85),('userdefine010',86),('vdolive',87),('winmx',88),('xwindows',89)))
_H3cDarIfObjects_ObjectIdentity=ObjectIdentity
h3cDarIfObjects=_H3cDarIfObjects_ObjectIdentity((1,3,6,1,4,1,43,45,1,10,2,112,1))
_H3cDarIfStatisticsObjects_ObjectIdentity=ObjectIdentity
h3cDarIfStatisticsObjects=_H3cDarIfStatisticsObjects_ObjectIdentity((1,3,6,1,4,1,43,45,1,10,2,112,1,1))
_H3cDarStatisticsTable_Object=MibTable
h3cDarStatisticsTable=_H3cDarStatisticsTable_Object((1,3,6,1,4,1,43,45,1,10,2,112,1,1,1))
if mibBuilder.loadTexts:h3cDarStatisticsTable.setStatus(_A)
_H3cDarStatisticsEntry_Object=MibTableRow
h3cDarStatisticsEntry=_H3cDarStatisticsEntry_Object((1,3,6,1,4,1,43,45,1,10,2,112,1,1,1,1))
h3cDarStatisticsEntry.setIndexNames((0,_C,_D),(0,_E,_F))
if mibBuilder.loadTexts:h3cDarStatisticsEntry.setStatus(_A)
_H3cDarStatisticsProtocolID_Type=H3cDarProtocol
_H3cDarStatisticsProtocolID_Object=MibTableColumn
h3cDarStatisticsProtocolID=_H3cDarStatisticsProtocolID_Object((1,3,6,1,4,1,43,45,1,10,2,112,1,1,1,1,1),_H3cDarStatisticsProtocolID_Type())
h3cDarStatisticsProtocolID.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:h3cDarStatisticsProtocolID.setStatus(_A)
_H3cDarStatisticsProtocolName_Type=OctetString
_H3cDarStatisticsProtocolName_Object=MibTableColumn
h3cDarStatisticsProtocolName=_H3cDarStatisticsProtocolName_Object((1,3,6,1,4,1,43,45,1,10,2,112,1,1,1,1,2),_H3cDarStatisticsProtocolName_Type())
h3cDarStatisticsProtocolName.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDarStatisticsProtocolName.setStatus(_A)
_H3cDarStatisticsInPkts_Type=Counter64
_H3cDarStatisticsInPkts_Object=MibTableColumn
h3cDarStatisticsInPkts=_H3cDarStatisticsInPkts_Object((1,3,6,1,4,1,43,45,1,10,2,112,1,1,1,1,3),_H3cDarStatisticsInPkts_Type())
h3cDarStatisticsInPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDarStatisticsInPkts.setStatus(_A)
_H3cDarStatisticsInBytes_Type=Counter64
_H3cDarStatisticsInBytes_Object=MibTableColumn
h3cDarStatisticsInBytes=_H3cDarStatisticsInBytes_Object((1,3,6,1,4,1,43,45,1,10,2,112,1,1,1,1,4),_H3cDarStatisticsInBytes_Type())
h3cDarStatisticsInBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDarStatisticsInBytes.setStatus(_A)
_H3cDarStatisticsInBitRate_Type=Counter64
_H3cDarStatisticsInBitRate_Object=MibTableColumn
h3cDarStatisticsInBitRate=_H3cDarStatisticsInBitRate_Object((1,3,6,1,4,1,43,45,1,10,2,112,1,1,1,1,5),_H3cDarStatisticsInBitRate_Type())
h3cDarStatisticsInBitRate.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDarStatisticsInBitRate.setStatus(_A)
_H3cDarStatisticsMaxInBitRate_Type=Counter64
_H3cDarStatisticsMaxInBitRate_Object=MibTableColumn
h3cDarStatisticsMaxInBitRate=_H3cDarStatisticsMaxInBitRate_Object((1,3,6,1,4,1,43,45,1,10,2,112,1,1,1,1,6),_H3cDarStatisticsMaxInBitRate_Type())
h3cDarStatisticsMaxInBitRate.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDarStatisticsMaxInBitRate.setStatus(_A)
_H3cDarStatisticsOutPkts_Type=Counter64
_H3cDarStatisticsOutPkts_Object=MibTableColumn
h3cDarStatisticsOutPkts=_H3cDarStatisticsOutPkts_Object((1,3,6,1,4,1,43,45,1,10,2,112,1,1,1,1,7),_H3cDarStatisticsOutPkts_Type())
h3cDarStatisticsOutPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDarStatisticsOutPkts.setStatus(_A)
_H3cDarStatisticsOutBytes_Type=Counter64
_H3cDarStatisticsOutBytes_Object=MibTableColumn
h3cDarStatisticsOutBytes=_H3cDarStatisticsOutBytes_Object((1,3,6,1,4,1,43,45,1,10,2,112,1,1,1,1,8),_H3cDarStatisticsOutBytes_Type())
h3cDarStatisticsOutBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDarStatisticsOutBytes.setStatus(_A)
_H3cDarStatisticsOutBitRate_Type=Counter64
_H3cDarStatisticsOutBitRate_Object=MibTableColumn
h3cDarStatisticsOutBitRate=_H3cDarStatisticsOutBitRate_Object((1,3,6,1,4,1,43,45,1,10,2,112,1,1,1,1,9),_H3cDarStatisticsOutBitRate_Type())
h3cDarStatisticsOutBitRate.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDarStatisticsOutBitRate.setStatus(_A)
_H3cDarStatisticsMaxOutBitRate_Type=Counter64
_H3cDarStatisticsMaxOutBitRate_Object=MibTableColumn
h3cDarStatisticsMaxOutBitRate=_H3cDarStatisticsMaxOutBitRate_Object((1,3,6,1,4,1,43,45,1,10,2,112,1,1,1,1,10),_H3cDarStatisticsMaxOutBitRate_Type())
h3cDarStatisticsMaxOutBitRate.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDarStatisticsMaxOutBitRate.setStatus(_A)
mibBuilder.exportSymbols(_E,**{'H3cDarProtocol':H3cDarProtocol,'h3cDar':h3cDar,'h3cDarIfObjects':h3cDarIfObjects,'h3cDarIfStatisticsObjects':h3cDarIfStatisticsObjects,'h3cDarStatisticsTable':h3cDarStatisticsTable,'h3cDarStatisticsEntry':h3cDarStatisticsEntry,_F:h3cDarStatisticsProtocolID,'h3cDarStatisticsProtocolName':h3cDarStatisticsProtocolName,'h3cDarStatisticsInPkts':h3cDarStatisticsInPkts,'h3cDarStatisticsInBytes':h3cDarStatisticsInBytes,'h3cDarStatisticsInBitRate':h3cDarStatisticsInBitRate,'h3cDarStatisticsMaxInBitRate':h3cDarStatisticsMaxInBitRate,'h3cDarStatisticsOutPkts':h3cDarStatisticsOutPkts,'h3cDarStatisticsOutBytes':h3cDarStatisticsOutBytes,'h3cDarStatisticsOutBitRate':h3cDarStatisticsOutBitRate,'h3cDarStatisticsMaxOutBitRate':h3cDarStatisticsMaxOutBitRate})