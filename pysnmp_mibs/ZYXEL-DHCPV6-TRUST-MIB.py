_D='read-write'
_C='dot1dBasePort'
_B='BRIDGE-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
dot1dBasePort,=mibBuilder.importSymbols(_B,_C)
EnabledStatus,=mibBuilder.importSymbols('P-BRIDGE-MIB','EnabledStatus')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
esMgmt,=mibBuilder.importSymbols('ZYXEL-ES-SMI','esMgmt')
zyxelDhcpv6Trust=ModuleIdentity((1,3,6,1,4,1,890,1,15,3,107))
_ZyxelDhcpv6TrustSetup_ObjectIdentity=ObjectIdentity
zyxelDhcpv6TrustSetup=_ZyxelDhcpv6TrustSetup_ObjectIdentity((1,3,6,1,4,1,890,1,15,3,107,1))
_ZyDhcpv6TrustState_Type=EnabledStatus
_ZyDhcpv6TrustState_Object=MibScalar
zyDhcpv6TrustState=_ZyDhcpv6TrustState_Object((1,3,6,1,4,1,890,1,15,3,107,1,1),_ZyDhcpv6TrustState_Type())
zyDhcpv6TrustState.setMaxAccess(_D)
if mibBuilder.loadTexts:zyDhcpv6TrustState.setStatus(_A)
_ZyxelDhcpv6TrustPortTable_Object=MibTable
zyxelDhcpv6TrustPortTable=_ZyxelDhcpv6TrustPortTable_Object((1,3,6,1,4,1,890,1,15,3,107,1,2))
if mibBuilder.loadTexts:zyxelDhcpv6TrustPortTable.setStatus(_A)
_ZyxelDhcpv6TrustPortEntry_Object=MibTableRow
zyxelDhcpv6TrustPortEntry=_ZyxelDhcpv6TrustPortEntry_Object((1,3,6,1,4,1,890,1,15,3,107,1,2,1))
zyxelDhcpv6TrustPortEntry.setIndexNames((0,_B,_C))
if mibBuilder.loadTexts:zyxelDhcpv6TrustPortEntry.setStatus(_A)
_ZyDhcpv6TrustPortState_Type=EnabledStatus
_ZyDhcpv6TrustPortState_Object=MibTableColumn
zyDhcpv6TrustPortState=_ZyDhcpv6TrustPortState_Object((1,3,6,1,4,1,890,1,15,3,107,1,2,1,1),_ZyDhcpv6TrustPortState_Type())
zyDhcpv6TrustPortState.setMaxAccess(_D)
if mibBuilder.loadTexts:zyDhcpv6TrustPortState.setStatus(_A)
mibBuilder.exportSymbols('ZYXEL-DHCPV6-TRUST-MIB',**{'zyxelDhcpv6Trust':zyxelDhcpv6Trust,'zyxelDhcpv6TrustSetup':zyxelDhcpv6TrustSetup,'zyDhcpv6TrustState':zyDhcpv6TrustState,'zyxelDhcpv6TrustPortTable':zyxelDhcpv6TrustPortTable,'zyxelDhcpv6TrustPortEntry':zyxelDhcpv6TrustPortEntry,'zyDhcpv6TrustPortState':zyDhcpv6TrustPortState})