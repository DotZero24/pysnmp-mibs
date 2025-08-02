_H='ibNode2ServiceName'
_G='ibNode1ServiceName'
_F='ibServiceName'
_E='ibNodeIPAddress'
_D='Integer32'
_C='IB-PLATFORMONE-MIB'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
IbIpAddr,IbString,ibPlatformOne=mibBuilder.importSymbols('IB-SMI-MIB','IbIpAddr','IbString','ibPlatformOne')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
ibPlatformModule=ModuleIdentity((1,3,6,1,4,1,7779,3,1,1,2,1))
if mibBuilder.loadTexts:ibPlatformModule.setRevisions(('2010-11-15 00:00','2010-10-19 00:00','2010-07-28 00:00','2009-06-05 00:00','2008-09-29 00:00','2005-01-10 00:00','2004-05-21 00:00'))
class IbServiceStates(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('working',1),('warning',2),('failed',3),('inactive',4),('unknown',5)))
class IbServiceNames(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36)));namedValues=NamedValues(*(('dhcp',1),('dns',2),('ntp',3),('radius',4),('tftp',5),('http-file-dist',6),('ftp',7),('bloxtools-move',8),('bloxtools',9),('node-status',10),('disk-usage',11),('enet-lan',12),('enet-lan2',13),('enet-ha',14),('enet-mgmt',15),('lcd',16),('memory',17),('replication',18),('db-object',19),('raid-summary',20),('raid-disk1',21),('raid-disk2',22),('raid-disk3',23),('raid-disk4',24),('fan1',25),('fan2',26),('fan3',27),('power-supply',28),('ntp-sync',29),('cpu1-temp',30),('cpu2-temp',31),('sys-temp',32),('raid-battery',33),('cpu-usage',34),('ospf',35),('bgp',36)))
_IbCPUTemperature_Type=IbString
_IbCPUTemperature_Object=MibScalar
ibCPUTemperature=_IbCPUTemperature_Object((1,3,6,1,4,1,7779,3,1,1,2,1,1),_IbCPUTemperature_Type())
ibCPUTemperature.setMaxAccess(_B)
if mibBuilder.loadTexts:ibCPUTemperature.setStatus(_A)
_IbClusterReplicationStatusTable_Object=MibTable
ibClusterReplicationStatusTable=_IbClusterReplicationStatusTable_Object((1,3,6,1,4,1,7779,3,1,1,2,1,2))
if mibBuilder.loadTexts:ibClusterReplicationStatusTable.setStatus(_A)
_IbClusterReplicationStatusEntry_Object=MibTableRow
ibClusterReplicationStatusEntry=_IbClusterReplicationStatusEntry_Object((1,3,6,1,4,1,7779,3,1,1,2,1,2,1))
ibClusterReplicationStatusEntry.setIndexNames((0,_C,_E))
if mibBuilder.loadTexts:ibClusterReplicationStatusEntry.setStatus(_A)
_IbNodeIPAddress_Type=IbIpAddr
_IbNodeIPAddress_Object=MibTableColumn
ibNodeIPAddress=_IbNodeIPAddress_Object((1,3,6,1,4,1,7779,3,1,1,2,1,2,1,1),_IbNodeIPAddress_Type())
ibNodeIPAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:ibNodeIPAddress.setStatus(_A)
_IbNodeReplicationStatus_Type=IbString
_IbNodeReplicationStatus_Object=MibTableColumn
ibNodeReplicationStatus=_IbNodeReplicationStatus_Object((1,3,6,1,4,1,7779,3,1,1,2,1,2,1,2),_IbNodeReplicationStatus_Type())
ibNodeReplicationStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:ibNodeReplicationStatus.setStatus(_A)
_IbNodeQueueFromMaster_Type=Integer32
_IbNodeQueueFromMaster_Object=MibTableColumn
ibNodeQueueFromMaster=_IbNodeQueueFromMaster_Object((1,3,6,1,4,1,7779,3,1,1,2,1,2,1,3),_IbNodeQueueFromMaster_Type())
ibNodeQueueFromMaster.setMaxAccess(_B)
if mibBuilder.loadTexts:ibNodeQueueFromMaster.setStatus(_A)
_IbNodeLastRepTimeFromMaster_Type=IbString
_IbNodeLastRepTimeFromMaster_Object=MibTableColumn
ibNodeLastRepTimeFromMaster=_IbNodeLastRepTimeFromMaster_Object((1,3,6,1,4,1,7779,3,1,1,2,1,2,1,4),_IbNodeLastRepTimeFromMaster_Type())
ibNodeLastRepTimeFromMaster.setMaxAccess(_B)
if mibBuilder.loadTexts:ibNodeLastRepTimeFromMaster.setStatus(_A)
_IbNodeQueueToMaster_Type=Integer32
_IbNodeQueueToMaster_Object=MibTableColumn
ibNodeQueueToMaster=_IbNodeQueueToMaster_Object((1,3,6,1,4,1,7779,3,1,1,2,1,2,1,5),_IbNodeQueueToMaster_Type())
ibNodeQueueToMaster.setMaxAccess(_B)
if mibBuilder.loadTexts:ibNodeQueueToMaster.setStatus(_A)
_IbNodeLastRepTimeToMaster_Type=IbString
_IbNodeLastRepTimeToMaster_Object=MibTableColumn
ibNodeLastRepTimeToMaster=_IbNodeLastRepTimeToMaster_Object((1,3,6,1,4,1,7779,3,1,1,2,1,2,1,6),_IbNodeLastRepTimeToMaster_Type())
ibNodeLastRepTimeToMaster.setMaxAccess(_B)
if mibBuilder.loadTexts:ibNodeLastRepTimeToMaster.setStatus(_A)
_IbNetworkMonitor_ObjectIdentity=ObjectIdentity
ibNetworkMonitor=_IbNetworkMonitor_ObjectIdentity((1,3,6,1,4,1,7779,3,1,1,2,1,3))
_IbNetworkMonitorDNS_ObjectIdentity=ObjectIdentity
ibNetworkMonitorDNS=_IbNetworkMonitorDNS_ObjectIdentity((1,3,6,1,4,1,7779,3,1,1,2,1,3,1))
class _IbNetworkMonitorDNSActive_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('nonactive',0),('active',1)))
_IbNetworkMonitorDNSActive_Type.__name__=_D
_IbNetworkMonitorDNSActive_Object=MibScalar
ibNetworkMonitorDNSActive=_IbNetworkMonitorDNSActive_Object((1,3,6,1,4,1,7779,3,1,1,2,1,3,1,1),_IbNetworkMonitorDNSActive_Type())
ibNetworkMonitorDNSActive.setMaxAccess(_B)
if mibBuilder.loadTexts:ibNetworkMonitorDNSActive.setStatus(_A)
_IbNetworkMonitorDNSNonAA_ObjectIdentity=ObjectIdentity
ibNetworkMonitorDNSNonAA=_IbNetworkMonitorDNSNonAA_ObjectIdentity((1,3,6,1,4,1,7779,3,1,1,2,1,3,1,2))
_IbNetworkMonitorDNSNonAAT1_ObjectIdentity=ObjectIdentity
ibNetworkMonitorDNSNonAAT1=_IbNetworkMonitorDNSNonAAT1_ObjectIdentity((1,3,6,1,4,1,7779,3,1,1,2,1,3,1,2,1))
_IbNetworkMonitorDNSNonAAT1AvgLatency_Type=Integer32
_IbNetworkMonitorDNSNonAAT1AvgLatency_Object=MibScalar
ibNetworkMonitorDNSNonAAT1AvgLatency=_IbNetworkMonitorDNSNonAAT1AvgLatency_Object((1,3,6,1,4,1,7779,3,1,1,2,1,3,1,2,1,1),_IbNetworkMonitorDNSNonAAT1AvgLatency_Type())
ibNetworkMonitorDNSNonAAT1AvgLatency.setMaxAccess(_B)
if mibBuilder.loadTexts:ibNetworkMonitorDNSNonAAT1AvgLatency.setStatus(_A)
_IbNetworkMonitorDNSNonAAT1Count_Type=Integer32
_IbNetworkMonitorDNSNonAAT1Count_Object=MibScalar
ibNetworkMonitorDNSNonAAT1Count=_IbNetworkMonitorDNSNonAAT1Count_Object((1,3,6,1,4,1,7779,3,1,1,2,1,3,1,2,1,2),_IbNetworkMonitorDNSNonAAT1Count_Type())
ibNetworkMonitorDNSNonAAT1Count.setMaxAccess(_B)
if mibBuilder.loadTexts:ibNetworkMonitorDNSNonAAT1Count.setStatus(_A)
_IbNetworkMonitorDNSNonAAT5_ObjectIdentity=ObjectIdentity
ibNetworkMonitorDNSNonAAT5=_IbNetworkMonitorDNSNonAAT5_ObjectIdentity((1,3,6,1,4,1,7779,3,1,1,2,1,3,1,2,2))
_IbNetworkMonitorDNSNonAAT5AvgLatency_Type=Integer32
_IbNetworkMonitorDNSNonAAT5AvgLatency_Object=MibScalar
ibNetworkMonitorDNSNonAAT5AvgLatency=_IbNetworkMonitorDNSNonAAT5AvgLatency_Object((1,3,6,1,4,1,7779,3,1,1,2,1,3,1,2,2,1),_IbNetworkMonitorDNSNonAAT5AvgLatency_Type())
ibNetworkMonitorDNSNonAAT5AvgLatency.setMaxAccess(_B)
if mibBuilder.loadTexts:ibNetworkMonitorDNSNonAAT5AvgLatency.setStatus(_A)
_IbNetworkMonitorDNSNonAAT5Count_Type=Integer32
_IbNetworkMonitorDNSNonAAT5Count_Object=MibScalar
ibNetworkMonitorDNSNonAAT5Count=_IbNetworkMonitorDNSNonAAT5Count_Object((1,3,6,1,4,1,7779,3,1,1,2,1,3,1,2,2,2),_IbNetworkMonitorDNSNonAAT5Count_Type())
ibNetworkMonitorDNSNonAAT5Count.setMaxAccess(_B)
if mibBuilder.loadTexts:ibNetworkMonitorDNSNonAAT5Count.setStatus(_A)
_IbNetworkMonitorDNSNonAAT15_ObjectIdentity=ObjectIdentity
ibNetworkMonitorDNSNonAAT15=_IbNetworkMonitorDNSNonAAT15_ObjectIdentity((1,3,6,1,4,1,7779,3,1,1,2,1,3,1,2,3))
_IbNetworkMonitorDNSNonAAT15AvgLatency_Type=Integer32
_IbNetworkMonitorDNSNonAAT15AvgLatency_Object=MibScalar
ibNetworkMonitorDNSNonAAT15AvgLatency=_IbNetworkMonitorDNSNonAAT15AvgLatency_Object((1,3,6,1,4,1,7779,3,1,1,2,1,3,1,2,3,1),_IbNetworkMonitorDNSNonAAT15AvgLatency_Type())
ibNetworkMonitorDNSNonAAT15AvgLatency.setMaxAccess(_B)
if mibBuilder.loadTexts:ibNetworkMonitorDNSNonAAT15AvgLatency.setStatus(_A)
_IbNetworkMonitorDNSNonAAT15Count_Type=Integer32
_IbNetworkMonitorDNSNonAAT15Count_Object=MibScalar
ibNetworkMonitorDNSNonAAT15Count=_IbNetworkMonitorDNSNonAAT15Count_Object((1,3,6,1,4,1,7779,3,1,1,2,1,3,1,2,3,2),_IbNetworkMonitorDNSNonAAT15Count_Type())
ibNetworkMonitorDNSNonAAT15Count.setMaxAccess(_B)
if mibBuilder.loadTexts:ibNetworkMonitorDNSNonAAT15Count.setStatus(_A)
_IbNetworkMonitorDNSNonAAT60_ObjectIdentity=ObjectIdentity
ibNetworkMonitorDNSNonAAT60=_IbNetworkMonitorDNSNonAAT60_ObjectIdentity((1,3,6,1,4,1,7779,3,1,1,2,1,3,1,2,4))
_IbNetworkMonitorDNSNonAAT60AvgLatency_Type=Integer32
_IbNetworkMonitorDNSNonAAT60AvgLatency_Object=MibScalar
ibNetworkMonitorDNSNonAAT60AvgLatency=_IbNetworkMonitorDNSNonAAT60AvgLatency_Object((1,3,6,1,4,1,7779,3,1,1,2,1,3,1,2,4,1),_IbNetworkMonitorDNSNonAAT60AvgLatency_Type())
ibNetworkMonitorDNSNonAAT60AvgLatency.setMaxAccess(_B)
if mibBuilder.loadTexts:ibNetworkMonitorDNSNonAAT60AvgLatency.setStatus(_A)
_IbNetworkMonitorDNSNonAAT60Count_Type=Integer32
_IbNetworkMonitorDNSNonAAT60Count_Object=MibScalar
ibNetworkMonitorDNSNonAAT60Count=_IbNetworkMonitorDNSNonAAT60Count_Object((1,3,6,1,4,1,7779,3,1,1,2,1,3,1,2,4,2),_IbNetworkMonitorDNSNonAAT60Count_Type())
ibNetworkMonitorDNSNonAAT60Count.setMaxAccess(_B)
if mibBuilder.loadTexts:ibNetworkMonitorDNSNonAAT60Count.setStatus(_A)
_IbNetworkMonitorDNSNonAAT1440_ObjectIdentity=ObjectIdentity
ibNetworkMonitorDNSNonAAT1440=_IbNetworkMonitorDNSNonAAT1440_ObjectIdentity((1,3,6,1,4,1,7779,3,1,1,2,1,3,1,2,5))
_IbNetworkMonitorDNSNonAAT1440AvgLatency_Type=Integer32
_IbNetworkMonitorDNSNonAAT1440AvgLatency_Object=MibScalar
ibNetworkMonitorDNSNonAAT1440AvgLatency=_IbNetworkMonitorDNSNonAAT1440AvgLatency_Object((1,3,6,1,4,1,7779,3,1,1,2,1,3,1,2,5,1),_IbNetworkMonitorDNSNonAAT1440AvgLatency_Type())
ibNetworkMonitorDNSNonAAT1440AvgLatency.setMaxAccess(_B)
if mibBuilder.loadTexts:ibNetworkMonitorDNSNonAAT1440AvgLatency.setStatus(_A)
_IbNetworkMonitorDNSNonAAT1440Count_Type=Integer32
_IbNetworkMonitorDNSNonAAT1440Count_Object=MibScalar
ibNetworkMonitorDNSNonAAT1440Count=_IbNetworkMonitorDNSNonAAT1440Count_Object((1,3,6,1,4,1,7779,3,1,1,2,1,3,1,2,5,2),_IbNetworkMonitorDNSNonAAT1440Count_Type())
ibNetworkMonitorDNSNonAAT1440Count.setMaxAccess(_B)
if mibBuilder.loadTexts:ibNetworkMonitorDNSNonAAT1440Count.setStatus(_A)
_IbNetworkMonitorDNSAA_ObjectIdentity=ObjectIdentity
ibNetworkMonitorDNSAA=_IbNetworkMonitorDNSAA_ObjectIdentity((1,3,6,1,4,1,7779,3,1,1,2,1,3,1,3))
_IbNetworkMonitorDNSAAT1_ObjectIdentity=ObjectIdentity
ibNetworkMonitorDNSAAT1=_IbNetworkMonitorDNSAAT1_ObjectIdentity((1,3,6,1,4,1,7779,3,1,1,2,1,3,1,3,1))
_IbNetworkMonitorDNSAAT1AvgLatency_Type=Integer32
_IbNetworkMonitorDNSAAT1AvgLatency_Object=MibScalar
ibNetworkMonitorDNSAAT1AvgLatency=_IbNetworkMonitorDNSAAT1AvgLatency_Object((1,3,6,1,4,1,7779,3,1,1,2,1,3,1,3,1,1),_IbNetworkMonitorDNSAAT1AvgLatency_Type())
ibNetworkMonitorDNSAAT1AvgLatency.setMaxAccess(_B)
if mibBuilder.loadTexts:ibNetworkMonitorDNSAAT1AvgLatency.setStatus(_A)
_IbNetworkMonitorDNSAAT1Count_Type=Integer32
_IbNetworkMonitorDNSAAT1Count_Object=MibScalar
ibNetworkMonitorDNSAAT1Count=_IbNetworkMonitorDNSAAT1Count_Object((1,3,6,1,4,1,7779,3,1,1,2,1,3,1,3,1,2),_IbNetworkMonitorDNSAAT1Count_Type())
ibNetworkMonitorDNSAAT1Count.setMaxAccess(_B)
if mibBuilder.loadTexts:ibNetworkMonitorDNSAAT1Count.setStatus(_A)
_IbNetworkMonitorDNSAAT5_ObjectIdentity=ObjectIdentity
ibNetworkMonitorDNSAAT5=_IbNetworkMonitorDNSAAT5_ObjectIdentity((1,3,6,1,4,1,7779,3,1,1,2,1,3,1,3,2))
_IbNetworkMonitorDNSAAT5AvgLatency_Type=Integer32
_IbNetworkMonitorDNSAAT5AvgLatency_Object=MibScalar
ibNetworkMonitorDNSAAT5AvgLatency=_IbNetworkMonitorDNSAAT5AvgLatency_Object((1,3,6,1,4,1,7779,3,1,1,2,1,3,1,3,2,1),_IbNetworkMonitorDNSAAT5AvgLatency_Type())
ibNetworkMonitorDNSAAT5AvgLatency.setMaxAccess(_B)
if mibBuilder.loadTexts:ibNetworkMonitorDNSAAT5AvgLatency.setStatus(_A)
_IbNetworkMonitorDNSAAT5Count_Type=Integer32
_IbNetworkMonitorDNSAAT5Count_Object=MibScalar
ibNetworkMonitorDNSAAT5Count=_IbNetworkMonitorDNSAAT5Count_Object((1,3,6,1,4,1,7779,3,1,1,2,1,3,1,3,2,2),_IbNetworkMonitorDNSAAT5Count_Type())
ibNetworkMonitorDNSAAT5Count.setMaxAccess(_B)
if mibBuilder.loadTexts:ibNetworkMonitorDNSAAT5Count.setStatus(_A)
_IbNetworkMonitorDNSAAT15_ObjectIdentity=ObjectIdentity
ibNetworkMonitorDNSAAT15=_IbNetworkMonitorDNSAAT15_ObjectIdentity((1,3,6,1,4,1,7779,3,1,1,2,1,3,1,3,3))
_IbNetworkMonitorDNSAAT15AvgLatency_Type=Integer32
_IbNetworkMonitorDNSAAT15AvgLatency_Object=MibScalar
ibNetworkMonitorDNSAAT15AvgLatency=_IbNetworkMonitorDNSAAT15AvgLatency_Object((1,3,6,1,4,1,7779,3,1,1,2,1,3,1,3,3,1),_IbNetworkMonitorDNSAAT15AvgLatency_Type())
ibNetworkMonitorDNSAAT15AvgLatency.setMaxAccess(_B)
if mibBuilder.loadTexts:ibNetworkMonitorDNSAAT15AvgLatency.setStatus(_A)
_IbNetworkMonitorDNSAAT15Count_Type=Integer32
_IbNetworkMonitorDNSAAT15Count_Object=MibScalar
ibNetworkMonitorDNSAAT15Count=_IbNetworkMonitorDNSAAT15Count_Object((1,3,6,1,4,1,7779,3,1,1,2,1,3,1,3,3,2),_IbNetworkMonitorDNSAAT15Count_Type())
ibNetworkMonitorDNSAAT15Count.setMaxAccess(_B)
if mibBuilder.loadTexts:ibNetworkMonitorDNSAAT15Count.setStatus(_A)
_IbNetworkMonitorDNSAAT60_ObjectIdentity=ObjectIdentity
ibNetworkMonitorDNSAAT60=_IbNetworkMonitorDNSAAT60_ObjectIdentity((1,3,6,1,4,1,7779,3,1,1,2,1,3,1,3,4))
_IbNetworkMonitorDNSAAT60AvgLatency_Type=Integer32
_IbNetworkMonitorDNSAAT60AvgLatency_Object=MibScalar
ibNetworkMonitorDNSAAT60AvgLatency=_IbNetworkMonitorDNSAAT60AvgLatency_Object((1,3,6,1,4,1,7779,3,1,1,2,1,3,1,3,4,1),_IbNetworkMonitorDNSAAT60AvgLatency_Type())
ibNetworkMonitorDNSAAT60AvgLatency.setMaxAccess(_B)
if mibBuilder.loadTexts:ibNetworkMonitorDNSAAT60AvgLatency.setStatus(_A)
_IbNetworkMonitorDNSAAT60Count_Type=Integer32
_IbNetworkMonitorDNSAAT60Count_Object=MibScalar
ibNetworkMonitorDNSAAT60Count=_IbNetworkMonitorDNSAAT60Count_Object((1,3,6,1,4,1,7779,3,1,1,2,1,3,1,3,4,2),_IbNetworkMonitorDNSAAT60Count_Type())
ibNetworkMonitorDNSAAT60Count.setMaxAccess(_B)
if mibBuilder.loadTexts:ibNetworkMonitorDNSAAT60Count.setStatus(_A)
_IbNetworkMonitorDNSAAT1440_ObjectIdentity=ObjectIdentity
ibNetworkMonitorDNSAAT1440=_IbNetworkMonitorDNSAAT1440_ObjectIdentity((1,3,6,1,4,1,7779,3,1,1,2,1,3,1,3,5))
_IbNetworkMonitorDNSAAT1440AvgLatency_Type=Integer32
_IbNetworkMonitorDNSAAT1440AvgLatency_Object=MibScalar
ibNetworkMonitorDNSAAT1440AvgLatency=_IbNetworkMonitorDNSAAT1440AvgLatency_Object((1,3,6,1,4,1,7779,3,1,1,2,1,3,1,3,5,1),_IbNetworkMonitorDNSAAT1440AvgLatency_Type())
ibNetworkMonitorDNSAAT1440AvgLatency.setMaxAccess(_B)
if mibBuilder.loadTexts:ibNetworkMonitorDNSAAT1440AvgLatency.setStatus(_A)
_IbNetworkMonitorDNSAAT1440Count_Type=Integer32
_IbNetworkMonitorDNSAAT1440Count_Object=MibScalar
ibNetworkMonitorDNSAAT1440Count=_IbNetworkMonitorDNSAAT1440Count_Object((1,3,6,1,4,1,7779,3,1,1,2,1,3,1,3,5,2),_IbNetworkMonitorDNSAAT1440Count_Type())
ibNetworkMonitorDNSAAT1440Count.setMaxAccess(_B)
if mibBuilder.loadTexts:ibNetworkMonitorDNSAAT1440Count.setStatus(_A)
_IbNetworkMonitorDNSSecurity_ObjectIdentity=ObjectIdentity
ibNetworkMonitorDNSSecurity=_IbNetworkMonitorDNSSecurity_ObjectIdentity((1,3,6,1,4,1,7779,3,1,1,2,1,3,1,4))
_IbNetworkMonitorDNSSecurityInvalidPort_ObjectIdentity=ObjectIdentity
ibNetworkMonitorDNSSecurityInvalidPort=_IbNetworkMonitorDNSSecurityInvalidPort_ObjectIdentity((1,3,6,1,4,1,7779,3,1,1,2,1,3,1,4,1))
_IbNetworkMonitorDNSSecurityInvalidPort1_Type=Integer32
_IbNetworkMonitorDNSSecurityInvalidPort1_Object=MibScalar
ibNetworkMonitorDNSSecurityInvalidPort1=_IbNetworkMonitorDNSSecurityInvalidPort1_Object((1,3,6,1,4,1,7779,3,1,1,2,1,3,1,4,1,1),_IbNetworkMonitorDNSSecurityInvalidPort1_Type())
ibNetworkMonitorDNSSecurityInvalidPort1.setMaxAccess(_B)
if mibBuilder.loadTexts:ibNetworkMonitorDNSSecurityInvalidPort1.setStatus(_A)
_IbNetworkMonitorDNSSecurityInvalidPort5_Type=Integer32
_IbNetworkMonitorDNSSecurityInvalidPort5_Object=MibScalar
ibNetworkMonitorDNSSecurityInvalidPort5=_IbNetworkMonitorDNSSecurityInvalidPort5_Object((1,3,6,1,4,1,7779,3,1,1,2,1,3,1,4,1,2),_IbNetworkMonitorDNSSecurityInvalidPort5_Type())
ibNetworkMonitorDNSSecurityInvalidPort5.setMaxAccess(_B)
if mibBuilder.loadTexts:ibNetworkMonitorDNSSecurityInvalidPort5.setStatus(_A)
_IbNetworkMonitorDNSSecurityInvalidPort15_Type=Integer32
_IbNetworkMonitorDNSSecurityInvalidPort15_Object=MibScalar
ibNetworkMonitorDNSSecurityInvalidPort15=_IbNetworkMonitorDNSSecurityInvalidPort15_Object((1,3,6,1,4,1,7779,3,1,1,2,1,3,1,4,1,3),_IbNetworkMonitorDNSSecurityInvalidPort15_Type())
ibNetworkMonitorDNSSecurityInvalidPort15.setMaxAccess(_B)
if mibBuilder.loadTexts:ibNetworkMonitorDNSSecurityInvalidPort15.setStatus(_A)
_IbNetworkMonitorDNSSecurityInvalidPort60_Type=Integer32
_IbNetworkMonitorDNSSecurityInvalidPort60_Object=MibScalar
ibNetworkMonitorDNSSecurityInvalidPort60=_IbNetworkMonitorDNSSecurityInvalidPort60_Object((1,3,6,1,4,1,7779,3,1,1,2,1,3,1,4,1,4),_IbNetworkMonitorDNSSecurityInvalidPort60_Type())
ibNetworkMonitorDNSSecurityInvalidPort60.setMaxAccess(_B)
if mibBuilder.loadTexts:ibNetworkMonitorDNSSecurityInvalidPort60.setStatus(_A)
_IbNetworkMonitorDNSSecurityInvalidPort1440_Type=Integer32
_IbNetworkMonitorDNSSecurityInvalidPort1440_Object=MibScalar
ibNetworkMonitorDNSSecurityInvalidPort1440=_IbNetworkMonitorDNSSecurityInvalidPort1440_Object((1,3,6,1,4,1,7779,3,1,1,2,1,3,1,4,1,5),_IbNetworkMonitorDNSSecurityInvalidPort1440_Type())
ibNetworkMonitorDNSSecurityInvalidPort1440.setMaxAccess(_B)
if mibBuilder.loadTexts:ibNetworkMonitorDNSSecurityInvalidPort1440.setStatus(_A)
_IbNetworkMonitorDNSSecurityInvalidPortCount_Type=Counter32
_IbNetworkMonitorDNSSecurityInvalidPortCount_Object=MibScalar
ibNetworkMonitorDNSSecurityInvalidPortCount=_IbNetworkMonitorDNSSecurityInvalidPortCount_Object((1,3,6,1,4,1,7779,3,1,1,2,1,3,1,4,1,6),_IbNetworkMonitorDNSSecurityInvalidPortCount_Type())
ibNetworkMonitorDNSSecurityInvalidPortCount.setMaxAccess(_B)
if mibBuilder.loadTexts:ibNetworkMonitorDNSSecurityInvalidPortCount.setStatus(_A)
_IbNetworkMonitorDNSSecurityInvalidTxid_ObjectIdentity=ObjectIdentity
ibNetworkMonitorDNSSecurityInvalidTxid=_IbNetworkMonitorDNSSecurityInvalidTxid_ObjectIdentity((1,3,6,1,4,1,7779,3,1,1,2,1,3,1,4,2))
_IbNetworkMonitorDNSSecurityInvalidTxid1_Type=Integer32
_IbNetworkMonitorDNSSecurityInvalidTxid1_Object=MibScalar
ibNetworkMonitorDNSSecurityInvalidTxid1=_IbNetworkMonitorDNSSecurityInvalidTxid1_Object((1,3,6,1,4,1,7779,3,1,1,2,1,3,1,4,2,1),_IbNetworkMonitorDNSSecurityInvalidTxid1_Type())
ibNetworkMonitorDNSSecurityInvalidTxid1.setMaxAccess(_B)
if mibBuilder.loadTexts:ibNetworkMonitorDNSSecurityInvalidTxid1.setStatus(_A)
_IbNetworkMonitorDNSSecurityInvalidTxid5_Type=Integer32
_IbNetworkMonitorDNSSecurityInvalidTxid5_Object=MibScalar
ibNetworkMonitorDNSSecurityInvalidTxid5=_IbNetworkMonitorDNSSecurityInvalidTxid5_Object((1,3,6,1,4,1,7779,3,1,1,2,1,3,1,4,2,2),_IbNetworkMonitorDNSSecurityInvalidTxid5_Type())
ibNetworkMonitorDNSSecurityInvalidTxid5.setMaxAccess(_B)
if mibBuilder.loadTexts:ibNetworkMonitorDNSSecurityInvalidTxid5.setStatus(_A)
_IbNetworkMonitorDNSSecurityInvalidTxid15_Type=Integer32
_IbNetworkMonitorDNSSecurityInvalidTxid15_Object=MibScalar
ibNetworkMonitorDNSSecurityInvalidTxid15=_IbNetworkMonitorDNSSecurityInvalidTxid15_Object((1,3,6,1,4,1,7779,3,1,1,2,1,3,1,4,2,3),_IbNetworkMonitorDNSSecurityInvalidTxid15_Type())
ibNetworkMonitorDNSSecurityInvalidTxid15.setMaxAccess(_B)
if mibBuilder.loadTexts:ibNetworkMonitorDNSSecurityInvalidTxid15.setStatus(_A)
_IbNetworkMonitorDNSSecurityInvalidTxid60_Type=Integer32
_IbNetworkMonitorDNSSecurityInvalidTxid60_Object=MibScalar
ibNetworkMonitorDNSSecurityInvalidTxid60=_IbNetworkMonitorDNSSecurityInvalidTxid60_Object((1,3,6,1,4,1,7779,3,1,1,2,1,3,1,4,2,4),_IbNetworkMonitorDNSSecurityInvalidTxid60_Type())
ibNetworkMonitorDNSSecurityInvalidTxid60.setMaxAccess(_B)
if mibBuilder.loadTexts:ibNetworkMonitorDNSSecurityInvalidTxid60.setStatus(_A)
_IbNetworkMonitorDNSSecurityInvalidTxid1440_Type=Integer32
_IbNetworkMonitorDNSSecurityInvalidTxid1440_Object=MibScalar
ibNetworkMonitorDNSSecurityInvalidTxid1440=_IbNetworkMonitorDNSSecurityInvalidTxid1440_Object((1,3,6,1,4,1,7779,3,1,1,2,1,3,1,4,2,5),_IbNetworkMonitorDNSSecurityInvalidTxid1440_Type())
ibNetworkMonitorDNSSecurityInvalidTxid1440.setMaxAccess(_B)
if mibBuilder.loadTexts:ibNetworkMonitorDNSSecurityInvalidTxid1440.setStatus(_A)
_IbNetworkMonitorDNSSecurityInvalidTxidCount_Type=Counter32
_IbNetworkMonitorDNSSecurityInvalidTxidCount_Object=MibScalar
ibNetworkMonitorDNSSecurityInvalidTxidCount=_IbNetworkMonitorDNSSecurityInvalidTxidCount_Object((1,3,6,1,4,1,7779,3,1,1,2,1,3,1,4,2,6),_IbNetworkMonitorDNSSecurityInvalidTxidCount_Type())
ibNetworkMonitorDNSSecurityInvalidTxidCount.setMaxAccess(_B)
if mibBuilder.loadTexts:ibNetworkMonitorDNSSecurityInvalidTxidCount.setStatus(_A)
_IbNetworkMonitorDNSSecurityInvalidPortOnly_Type=Counter32
_IbNetworkMonitorDNSSecurityInvalidPortOnly_Object=MibScalar
ibNetworkMonitorDNSSecurityInvalidPortOnly=_IbNetworkMonitorDNSSecurityInvalidPortOnly_Object((1,3,6,1,4,1,7779,3,1,1,2,1,3,1,4,3),_IbNetworkMonitorDNSSecurityInvalidPortOnly_Type())
ibNetworkMonitorDNSSecurityInvalidPortOnly.setMaxAccess(_B)
if mibBuilder.loadTexts:ibNetworkMonitorDNSSecurityInvalidPortOnly.setStatus(_A)
_IbNetworkMonitorDNSSecurityInvalidTxidOnly_Type=Counter32
_IbNetworkMonitorDNSSecurityInvalidTxidOnly_Object=MibScalar
ibNetworkMonitorDNSSecurityInvalidTxidOnly=_IbNetworkMonitorDNSSecurityInvalidTxidOnly_Object((1,3,6,1,4,1,7779,3,1,1,2,1,3,1,4,4),_IbNetworkMonitorDNSSecurityInvalidTxidOnly_Type())
ibNetworkMonitorDNSSecurityInvalidTxidOnly.setMaxAccess(_B)
if mibBuilder.loadTexts:ibNetworkMonitorDNSSecurityInvalidTxidOnly.setStatus(_A)
_IbNetworkMonitorDNSSecurityInvalidTxidAndPort_Type=Counter32
_IbNetworkMonitorDNSSecurityInvalidTxidAndPort_Object=MibScalar
ibNetworkMonitorDNSSecurityInvalidTxidAndPort=_IbNetworkMonitorDNSSecurityInvalidTxidAndPort_Object((1,3,6,1,4,1,7779,3,1,1,2,1,3,1,4,5),_IbNetworkMonitorDNSSecurityInvalidTxidAndPort_Type())
ibNetworkMonitorDNSSecurityInvalidTxidAndPort.setMaxAccess(_B)
if mibBuilder.loadTexts:ibNetworkMonitorDNSSecurityInvalidTxidAndPort.setStatus(_A)
_IbHardwareType_Type=IbString
_IbHardwareType_Object=MibScalar
ibHardwareType=_IbHardwareType_Object((1,3,6,1,4,1,7779,3,1,1,2,1,4),_IbHardwareType_Type())
ibHardwareType.setMaxAccess(_B)
if mibBuilder.loadTexts:ibHardwareType.setStatus(_A)
_IbHardwareId_Type=IbString
_IbHardwareId_Object=MibScalar
ibHardwareId=_IbHardwareId_Object((1,3,6,1,4,1,7779,3,1,1,2,1,5),_IbHardwareId_Type())
ibHardwareId.setMaxAccess(_B)
if mibBuilder.loadTexts:ibHardwareId.setStatus(_A)
_IbSerialNumber_Type=IbString
_IbSerialNumber_Object=MibScalar
ibSerialNumber=_IbSerialNumber_Object((1,3,6,1,4,1,7779,3,1,1,2,1,6),_IbSerialNumber_Type())
ibSerialNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:ibSerialNumber.setStatus(_A)
_IbNiosVersion_Type=IbString
_IbNiosVersion_Object=MibScalar
ibNiosVersion=_IbNiosVersion_Object((1,3,6,1,4,1,7779,3,1,1,2,1,7),_IbNiosVersion_Type())
ibNiosVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:ibNiosVersion.setStatus(_A)
_IbSystemMonitor_ObjectIdentity=ObjectIdentity
ibSystemMonitor=_IbSystemMonitor_ObjectIdentity((1,3,6,1,4,1,7779,3,1,1,2,1,8))
_IbSystemMonitorCpu_ObjectIdentity=ObjectIdentity
ibSystemMonitorCpu=_IbSystemMonitorCpu_ObjectIdentity((1,3,6,1,4,1,7779,3,1,1,2,1,8,1))
_IbSystemMonitorCpuUsage_Type=Integer32
_IbSystemMonitorCpuUsage_Object=MibScalar
ibSystemMonitorCpuUsage=_IbSystemMonitorCpuUsage_Object((1,3,6,1,4,1,7779,3,1,1,2,1,8,1,1),_IbSystemMonitorCpuUsage_Type())
ibSystemMonitorCpuUsage.setMaxAccess(_B)
if mibBuilder.loadTexts:ibSystemMonitorCpuUsage.setStatus(_A)
_IbSystemMonitorMem_ObjectIdentity=ObjectIdentity
ibSystemMonitorMem=_IbSystemMonitorMem_ObjectIdentity((1,3,6,1,4,1,7779,3,1,1,2,1,8,2))
_IbSystemMonitorMemUsage_Type=Integer32
_IbSystemMonitorMemUsage_Object=MibScalar
ibSystemMonitorMemUsage=_IbSystemMonitorMemUsage_Object((1,3,6,1,4,1,7779,3,1,1,2,1,8,2,1),_IbSystemMonitorMemUsage_Type())
ibSystemMonitorMemUsage.setMaxAccess(_B)
if mibBuilder.loadTexts:ibSystemMonitorMemUsage.setStatus(_A)
_IbMemberServiceStatusTable_Object=MibTable
ibMemberServiceStatusTable=_IbMemberServiceStatusTable_Object((1,3,6,1,4,1,7779,3,1,1,2,1,9))
if mibBuilder.loadTexts:ibMemberServiceStatusTable.setStatus(_A)
_IbMemberServiceStatusEntry_Object=MibTableRow
ibMemberServiceStatusEntry=_IbMemberServiceStatusEntry_Object((1,3,6,1,4,1,7779,3,1,1,2,1,9,1))
ibMemberServiceStatusEntry.setIndexNames((0,_C,_F))
if mibBuilder.loadTexts:ibMemberServiceStatusEntry.setStatus(_A)
_IbServiceName_Type=IbServiceNames
_IbServiceName_Object=MibTableColumn
ibServiceName=_IbServiceName_Object((1,3,6,1,4,1,7779,3,1,1,2,1,9,1,1),_IbServiceName_Type())
ibServiceName.setMaxAccess(_B)
if mibBuilder.loadTexts:ibServiceName.setStatus(_A)
_IbServiceStatus_Type=IbServiceStates
_IbServiceStatus_Object=MibTableColumn
ibServiceStatus=_IbServiceStatus_Object((1,3,6,1,4,1,7779,3,1,1,2,1,9,1,2),_IbServiceStatus_Type())
ibServiceStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:ibServiceStatus.setStatus(_A)
_IbServiceDesc_Type=IbString
_IbServiceDesc_Object=MibTableColumn
ibServiceDesc=_IbServiceDesc_Object((1,3,6,1,4,1,7779,3,1,1,2,1,9,1,3),_IbServiceDesc_Type())
ibServiceDesc.setMaxAccess(_B)
if mibBuilder.loadTexts:ibServiceDesc.setStatus(_A)
_IbMemberNode1ServiceStatusTable_Object=MibTable
ibMemberNode1ServiceStatusTable=_IbMemberNode1ServiceStatusTable_Object((1,3,6,1,4,1,7779,3,1,1,2,1,10))
if mibBuilder.loadTexts:ibMemberNode1ServiceStatusTable.setStatus(_A)
_IbMemberNode1ServiceStatusEntry_Object=MibTableRow
ibMemberNode1ServiceStatusEntry=_IbMemberNode1ServiceStatusEntry_Object((1,3,6,1,4,1,7779,3,1,1,2,1,10,1))
ibMemberNode1ServiceStatusEntry.setIndexNames((0,_C,_G))
if mibBuilder.loadTexts:ibMemberNode1ServiceStatusEntry.setStatus(_A)
_IbNode1ServiceName_Type=IbServiceNames
_IbNode1ServiceName_Object=MibTableColumn
ibNode1ServiceName=_IbNode1ServiceName_Object((1,3,6,1,4,1,7779,3,1,1,2,1,10,1,1),_IbNode1ServiceName_Type())
ibNode1ServiceName.setMaxAccess(_B)
if mibBuilder.loadTexts:ibNode1ServiceName.setStatus(_A)
_IbNode1ServiceStatus_Type=IbServiceStates
_IbNode1ServiceStatus_Object=MibTableColumn
ibNode1ServiceStatus=_IbNode1ServiceStatus_Object((1,3,6,1,4,1,7779,3,1,1,2,1,10,1,2),_IbNode1ServiceStatus_Type())
ibNode1ServiceStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:ibNode1ServiceStatus.setStatus(_A)
_IbNode1ServiceDesc_Type=IbString
_IbNode1ServiceDesc_Object=MibTableColumn
ibNode1ServiceDesc=_IbNode1ServiceDesc_Object((1,3,6,1,4,1,7779,3,1,1,2,1,10,1,3),_IbNode1ServiceDesc_Type())
ibNode1ServiceDesc.setMaxAccess(_B)
if mibBuilder.loadTexts:ibNode1ServiceDesc.setStatus(_A)
_IbMemberNode2ServiceStatusTable_Object=MibTable
ibMemberNode2ServiceStatusTable=_IbMemberNode2ServiceStatusTable_Object((1,3,6,1,4,1,7779,3,1,1,2,1,11))
if mibBuilder.loadTexts:ibMemberNode2ServiceStatusTable.setStatus(_A)
_IbMemberNode2ServiceStatusEntry_Object=MibTableRow
ibMemberNode2ServiceStatusEntry=_IbMemberNode2ServiceStatusEntry_Object((1,3,6,1,4,1,7779,3,1,1,2,1,11,1))
ibMemberNode2ServiceStatusEntry.setIndexNames((0,_C,_H))
if mibBuilder.loadTexts:ibMemberNode2ServiceStatusEntry.setStatus(_A)
_IbNode2ServiceName_Type=IbServiceNames
_IbNode2ServiceName_Object=MibTableColumn
ibNode2ServiceName=_IbNode2ServiceName_Object((1,3,6,1,4,1,7779,3,1,1,2,1,11,1,1),_IbNode2ServiceName_Type())
ibNode2ServiceName.setMaxAccess(_B)
if mibBuilder.loadTexts:ibNode2ServiceName.setStatus(_A)
_IbNode2ServiceStatus_Type=IbServiceStates
_IbNode2ServiceStatus_Object=MibTableColumn
ibNode2ServiceStatus=_IbNode2ServiceStatus_Object((1,3,6,1,4,1,7779,3,1,1,2,1,11,1,2),_IbNode2ServiceStatus_Type())
ibNode2ServiceStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:ibNode2ServiceStatus.setStatus(_A)
_IbNode2ServiceDesc_Type=IbString
_IbNode2ServiceDesc_Object=MibTableColumn
ibNode2ServiceDesc=_IbNode2ServiceDesc_Object((1,3,6,1,4,1,7779,3,1,1,2,1,11,1,3),_IbNode2ServiceDesc_Type())
ibNode2ServiceDesc.setMaxAccess(_B)
if mibBuilder.loadTexts:ibNode2ServiceDesc.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'IbServiceStates':IbServiceStates,'IbServiceNames':IbServiceNames,'ibPlatformModule':ibPlatformModule,'ibCPUTemperature':ibCPUTemperature,'ibClusterReplicationStatusTable':ibClusterReplicationStatusTable,'ibClusterReplicationStatusEntry':ibClusterReplicationStatusEntry,_E:ibNodeIPAddress,'ibNodeReplicationStatus':ibNodeReplicationStatus,'ibNodeQueueFromMaster':ibNodeQueueFromMaster,'ibNodeLastRepTimeFromMaster':ibNodeLastRepTimeFromMaster,'ibNodeQueueToMaster':ibNodeQueueToMaster,'ibNodeLastRepTimeToMaster':ibNodeLastRepTimeToMaster,'ibNetworkMonitor':ibNetworkMonitor,'ibNetworkMonitorDNS':ibNetworkMonitorDNS,'ibNetworkMonitorDNSActive':ibNetworkMonitorDNSActive,'ibNetworkMonitorDNSNonAA':ibNetworkMonitorDNSNonAA,'ibNetworkMonitorDNSNonAAT1':ibNetworkMonitorDNSNonAAT1,'ibNetworkMonitorDNSNonAAT1AvgLatency':ibNetworkMonitorDNSNonAAT1AvgLatency,'ibNetworkMonitorDNSNonAAT1Count':ibNetworkMonitorDNSNonAAT1Count,'ibNetworkMonitorDNSNonAAT5':ibNetworkMonitorDNSNonAAT5,'ibNetworkMonitorDNSNonAAT5AvgLatency':ibNetworkMonitorDNSNonAAT5AvgLatency,'ibNetworkMonitorDNSNonAAT5Count':ibNetworkMonitorDNSNonAAT5Count,'ibNetworkMonitorDNSNonAAT15':ibNetworkMonitorDNSNonAAT15,'ibNetworkMonitorDNSNonAAT15AvgLatency':ibNetworkMonitorDNSNonAAT15AvgLatency,'ibNetworkMonitorDNSNonAAT15Count':ibNetworkMonitorDNSNonAAT15Count,'ibNetworkMonitorDNSNonAAT60':ibNetworkMonitorDNSNonAAT60,'ibNetworkMonitorDNSNonAAT60AvgLatency':ibNetworkMonitorDNSNonAAT60AvgLatency,'ibNetworkMonitorDNSNonAAT60Count':ibNetworkMonitorDNSNonAAT60Count,'ibNetworkMonitorDNSNonAAT1440':ibNetworkMonitorDNSNonAAT1440,'ibNetworkMonitorDNSNonAAT1440AvgLatency':ibNetworkMonitorDNSNonAAT1440AvgLatency,'ibNetworkMonitorDNSNonAAT1440Count':ibNetworkMonitorDNSNonAAT1440Count,'ibNetworkMonitorDNSAA':ibNetworkMonitorDNSAA,'ibNetworkMonitorDNSAAT1':ibNetworkMonitorDNSAAT1,'ibNetworkMonitorDNSAAT1AvgLatency':ibNetworkMonitorDNSAAT1AvgLatency,'ibNetworkMonitorDNSAAT1Count':ibNetworkMonitorDNSAAT1Count,'ibNetworkMonitorDNSAAT5':ibNetworkMonitorDNSAAT5,'ibNetworkMonitorDNSAAT5AvgLatency':ibNetworkMonitorDNSAAT5AvgLatency,'ibNetworkMonitorDNSAAT5Count':ibNetworkMonitorDNSAAT5Count,'ibNetworkMonitorDNSAAT15':ibNetworkMonitorDNSAAT15,'ibNetworkMonitorDNSAAT15AvgLatency':ibNetworkMonitorDNSAAT15AvgLatency,'ibNetworkMonitorDNSAAT15Count':ibNetworkMonitorDNSAAT15Count,'ibNetworkMonitorDNSAAT60':ibNetworkMonitorDNSAAT60,'ibNetworkMonitorDNSAAT60AvgLatency':ibNetworkMonitorDNSAAT60AvgLatency,'ibNetworkMonitorDNSAAT60Count':ibNetworkMonitorDNSAAT60Count,'ibNetworkMonitorDNSAAT1440':ibNetworkMonitorDNSAAT1440,'ibNetworkMonitorDNSAAT1440AvgLatency':ibNetworkMonitorDNSAAT1440AvgLatency,'ibNetworkMonitorDNSAAT1440Count':ibNetworkMonitorDNSAAT1440Count,'ibNetworkMonitorDNSSecurity':ibNetworkMonitorDNSSecurity,'ibNetworkMonitorDNSSecurityInvalidPort':ibNetworkMonitorDNSSecurityInvalidPort,'ibNetworkMonitorDNSSecurityInvalidPort1':ibNetworkMonitorDNSSecurityInvalidPort1,'ibNetworkMonitorDNSSecurityInvalidPort5':ibNetworkMonitorDNSSecurityInvalidPort5,'ibNetworkMonitorDNSSecurityInvalidPort15':ibNetworkMonitorDNSSecurityInvalidPort15,'ibNetworkMonitorDNSSecurityInvalidPort60':ibNetworkMonitorDNSSecurityInvalidPort60,'ibNetworkMonitorDNSSecurityInvalidPort1440':ibNetworkMonitorDNSSecurityInvalidPort1440,'ibNetworkMonitorDNSSecurityInvalidPortCount':ibNetworkMonitorDNSSecurityInvalidPortCount,'ibNetworkMonitorDNSSecurityInvalidTxid':ibNetworkMonitorDNSSecurityInvalidTxid,'ibNetworkMonitorDNSSecurityInvalidTxid1':ibNetworkMonitorDNSSecurityInvalidTxid1,'ibNetworkMonitorDNSSecurityInvalidTxid5':ibNetworkMonitorDNSSecurityInvalidTxid5,'ibNetworkMonitorDNSSecurityInvalidTxid15':ibNetworkMonitorDNSSecurityInvalidTxid15,'ibNetworkMonitorDNSSecurityInvalidTxid60':ibNetworkMonitorDNSSecurityInvalidTxid60,'ibNetworkMonitorDNSSecurityInvalidTxid1440':ibNetworkMonitorDNSSecurityInvalidTxid1440,'ibNetworkMonitorDNSSecurityInvalidTxidCount':ibNetworkMonitorDNSSecurityInvalidTxidCount,'ibNetworkMonitorDNSSecurityInvalidPortOnly':ibNetworkMonitorDNSSecurityInvalidPortOnly,'ibNetworkMonitorDNSSecurityInvalidTxidOnly':ibNetworkMonitorDNSSecurityInvalidTxidOnly,'ibNetworkMonitorDNSSecurityInvalidTxidAndPort':ibNetworkMonitorDNSSecurityInvalidTxidAndPort,'ibHardwareType':ibHardwareType,'ibHardwareId':ibHardwareId,'ibSerialNumber':ibSerialNumber,'ibNiosVersion':ibNiosVersion,'ibSystemMonitor':ibSystemMonitor,'ibSystemMonitorCpu':ibSystemMonitorCpu,'ibSystemMonitorCpuUsage':ibSystemMonitorCpuUsage,'ibSystemMonitorMem':ibSystemMonitorMem,'ibSystemMonitorMemUsage':ibSystemMonitorMemUsage,'ibMemberServiceStatusTable':ibMemberServiceStatusTable,'ibMemberServiceStatusEntry':ibMemberServiceStatusEntry,_F:ibServiceName,'ibServiceStatus':ibServiceStatus,'ibServiceDesc':ibServiceDesc,'ibMemberNode1ServiceStatusTable':ibMemberNode1ServiceStatusTable,'ibMemberNode1ServiceStatusEntry':ibMemberNode1ServiceStatusEntry,_G:ibNode1ServiceName,'ibNode1ServiceStatus':ibNode1ServiceStatus,'ibNode1ServiceDesc':ibNode1ServiceDesc,'ibMemberNode2ServiceStatusTable':ibMemberNode2ServiceStatusTable,'ibMemberNode2ServiceStatusEntry':ibMemberNode2ServiceStatusEntry,_H:ibNode2ServiceName,'ibNode2ServiceStatus':ibNode2ServiceStatus,'ibNode2ServiceDesc':ibNode2ServiceDesc})