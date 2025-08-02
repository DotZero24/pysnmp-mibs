if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
tplinkClusterMIBObjects,=mibBuilder.importSymbols('TPLINK-CLUSTERTREE-MIB','tplinkClusterMIBObjects')
tplinkClusterMIB=ModuleIdentity((1,3,6,1,4,1,11863,6,33,1,1))
if mibBuilder.loadTexts:tplinkClusterMIB.setRevisions(('2009-08-27 00:00',))
_NdpManage_ObjectIdentity=ObjectIdentity
ndpManage=_NdpManage_ObjectIdentity((1,3,6,1,4,1,11863,6,33,1,1,1))
_NtdpManage_ObjectIdentity=ObjectIdentity
ntdpManage=_NtdpManage_ObjectIdentity((1,3,6,1,4,1,11863,6,33,1,1,2))
_ClusterManage_ObjectIdentity=ObjectIdentity
clusterManage=_ClusterManage_ObjectIdentity((1,3,6,1,4,1,11863,6,33,1,1,3))
mibBuilder.exportSymbols('TPLINK-CLUSTER-MIB',**{'tplinkClusterMIB':tplinkClusterMIB,'ndpManage':ndpManage,'ntdpManage':ntdpManage,'clusterManage':clusterManage})