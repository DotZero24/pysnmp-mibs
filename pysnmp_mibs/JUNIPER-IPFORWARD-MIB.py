_G='jnxInetCidrRouteEntry'
_F='jnxIpCidrRouteEntry'
_E='read-only'
_D='JUNIPER-IPFORWARD-MIB'
_C='current'
_B='deprecated'
_A='SnmpAdminString'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
inetCidrRouteEntry,ipCidrRouteEntry=mibBuilder.importSymbols('IP-FORWARD-MIB','inetCidrRouteEntry','ipCidrRouteEntry')
jnxMibs,=mibBuilder.importSymbols('JUNIPER-SMI','jnxMibs')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB',_A)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
jnxIpForwardMIB=ModuleIdentity((1,3,6,1,4,1,2636,3,38))
if mibBuilder.loadTexts:jnxIpForwardMIB.setRevisions(('2011-11-13 00:00',))
_JnxIpCidrRouteTable_Object=MibTable
jnxIpCidrRouteTable=_JnxIpCidrRouteTable_Object((1,3,6,1,4,1,2636,3,38,1))
if mibBuilder.loadTexts:jnxIpCidrRouteTable.setStatus(_B)
_JnxIpCidrRouteEntry_Object=MibTableRow
jnxIpCidrRouteEntry=_JnxIpCidrRouteEntry_Object((1,3,6,1,4,1,2636,3,38,1,1))
if mibBuilder.loadTexts:jnxIpCidrRouteEntry.setStatus(_B)
class _JnxIpCidrRouteTunnelName_Type(SnmpAdminString):defaultValue=OctetString('')
_JnxIpCidrRouteTunnelName_Type.__name__=_A
_JnxIpCidrRouteTunnelName_Object=MibTableColumn
jnxIpCidrRouteTunnelName=_JnxIpCidrRouteTunnelName_Object((1,3,6,1,4,1,2636,3,38,1,1,1),_JnxIpCidrRouteTunnelName_Type())
jnxIpCidrRouteTunnelName.setMaxAccess(_E)
if mibBuilder.loadTexts:jnxIpCidrRouteTunnelName.setStatus(_B)
_JnxInetCidrRouteTable_Object=MibTable
jnxInetCidrRouteTable=_JnxInetCidrRouteTable_Object((1,3,6,1,4,1,2636,3,38,2))
if mibBuilder.loadTexts:jnxInetCidrRouteTable.setStatus(_C)
_JnxInetCidrRouteEntry_Object=MibTableRow
jnxInetCidrRouteEntry=_JnxInetCidrRouteEntry_Object((1,3,6,1,4,1,2636,3,38,2,1))
if mibBuilder.loadTexts:jnxInetCidrRouteEntry.setStatus(_C)
class _JnxInetCidrRouteTunnelName_Type(SnmpAdminString):defaultValue=OctetString('')
_JnxInetCidrRouteTunnelName_Type.__name__=_A
_JnxInetCidrRouteTunnelName_Object=MibTableColumn
jnxInetCidrRouteTunnelName=_JnxInetCidrRouteTunnelName_Object((1,3,6,1,4,1,2636,3,38,2,1,1),_JnxInetCidrRouteTunnelName_Type())
jnxInetCidrRouteTunnelName.setMaxAccess(_E)
if mibBuilder.loadTexts:jnxInetCidrRouteTunnelName.setStatus(_C)
ipCidrRouteEntry.registerAugmentions((_D,_F))
jnxIpCidrRouteEntry.setIndexNames(*ipCidrRouteEntry.getIndexNames())
inetCidrRouteEntry.registerAugmentions((_D,_G))
jnxInetCidrRouteEntry.setIndexNames(*inetCidrRouteEntry.getIndexNames())
mibBuilder.exportSymbols(_D,**{'jnxIpForwardMIB':jnxIpForwardMIB,'jnxIpCidrRouteTable':jnxIpCidrRouteTable,_F:jnxIpCidrRouteEntry,'jnxIpCidrRouteTunnelName':jnxIpCidrRouteTunnelName,'jnxInetCidrRouteTable':jnxInetCidrRouteTable,_G:jnxInetCidrRouteEntry,'jnxInetCidrRouteTunnelName':jnxInetCidrRouteTunnelName})