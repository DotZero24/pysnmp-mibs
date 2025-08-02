_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
gnomeProducts,=mibBuilder.importSymbols('GNOME-SMI','gnomeProducts')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
zebra=ModuleIdentity((1,3,6,1,4,1,3319,1,2))
_Zserv_ObjectIdentity=ObjectIdentity
zserv=_Zserv_ObjectIdentity((1,3,6,1,4,1,3319,1,2,1))
if mibBuilder.loadTexts:zserv.setStatus(_A)
_Bgpd_ObjectIdentity=ObjectIdentity
bgpd=_Bgpd_ObjectIdentity((1,3,6,1,4,1,3319,1,2,2))
if mibBuilder.loadTexts:bgpd.setStatus(_A)
_Ripd_ObjectIdentity=ObjectIdentity
ripd=_Ripd_ObjectIdentity((1,3,6,1,4,1,3319,1,2,3))
if mibBuilder.loadTexts:ripd.setStatus(_A)
_Ripngd_ObjectIdentity=ObjectIdentity
ripngd=_Ripngd_ObjectIdentity((1,3,6,1,4,1,3319,1,2,4))
if mibBuilder.loadTexts:ripngd.setStatus(_A)
_Ospfd_ObjectIdentity=ObjectIdentity
ospfd=_Ospfd_ObjectIdentity((1,3,6,1,4,1,3319,1,2,5))
if mibBuilder.loadTexts:ospfd.setStatus(_A)
_Ospf6d_ObjectIdentity=ObjectIdentity
ospf6d=_Ospf6d_ObjectIdentity((1,3,6,1,4,1,3319,1,2,6))
if mibBuilder.loadTexts:ospf6d.setStatus(_A)
mibBuilder.exportSymbols('GNOME-PRODUCT-ZEBRA-MIB',**{'zebra':zebra,'zserv':zserv,'bgpd':bgpd,'ripd':ripd,'ripngd':ripngd,'ospfd':ospfd,'ospf6d':ospf6d})