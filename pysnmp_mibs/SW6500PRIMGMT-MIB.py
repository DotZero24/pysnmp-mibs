if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
dlink_mgmt,dlink_products=mibBuilder.importSymbols('DLINK-ID-REC-MIB','dlink-mgmt','dlink-products')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
_Dlink_Des6500SeriesProd_ObjectIdentity=ObjectIdentity
dlink_Des6500SeriesProd=_Dlink_Des6500SeriesProd_ObjectIdentity((1,3,6,1,4,1,171,10,78))
_Dlink_Des6500_ObjectIdentity=ObjectIdentity
dlink_Des6500=_Dlink_Des6500_ObjectIdentity((1,3,6,1,4,1,171,10,78,1))
_Des6500SeriesProd_ObjectIdentity=ObjectIdentity
des6500SeriesProd=_Des6500SeriesProd_ObjectIdentity((1,3,6,1,4,1,171,11,78))
_Des6500_ObjectIdentity=ObjectIdentity
des6500=_Des6500_ObjectIdentity((1,3,6,1,4,1,171,11,78,1))
mibBuilder.exportSymbols('SW6500PRIMGMT-MIB',**{'dlink-Des6500SeriesProd':dlink_Des6500SeriesProd,'dlink-Des6500':dlink_Des6500,'des6500SeriesProd':des6500SeriesProd,'des6500':des6500})