if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
hmWanMgmt,=mibBuilder.importSymbols('HIRSCHMANN-WAN-MIB','hmWanMgmt')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
hmWanProductsMib=ModuleIdentity((1,3,6,1,4,1,248,40,1,1))
if mibBuilder.loadTexts:hmWanProductsMib.setRevisions(('2016-08-09 00:00',))
_Owl_3g_ObjectIdentity=ObjectIdentity
owl_3g=_Owl_3g_ObjectIdentity((1,3,6,1,4,1,248,40,1,1,1))
_Owl_LTE_ObjectIdentity=ObjectIdentity
owl_LTE=_Owl_LTE_ObjectIdentity((1,3,6,1,4,1,248,40,1,1,2))
_Owl_LTE_M12_ObjectIdentity=ObjectIdentity
owl_LTE_M12=_Owl_LTE_M12_ObjectIdentity((1,3,6,1,4,1,248,40,1,1,3))
mibBuilder.exportSymbols('HIRSCHMANN-WAN-PRODUCTS-MIB',**{'hmWanProductsMib':hmWanProductsMib,'owl-3g':owl_3g,'owl-LTE':owl_LTE,'owl-LTE-M12':owl_LTE_M12})