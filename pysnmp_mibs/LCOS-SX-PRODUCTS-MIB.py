if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
lcosSX2,=mibBuilder.importSymbols('LANCOM-REF-MIB','lcosSX2')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
lcosSxProducts=ModuleIdentity((1,3,6,1,4,1,2356,16,8))
if mibBuilder.loadTexts:lcosSxProducts.setRevisions(('2021-11-19 00:00',))
_LcosSxProductsGS4530X_ObjectIdentity=ObjectIdentity
lcosSxProductsGS4530X=_LcosSxProductsGS4530X_ObjectIdentity((1,3,6,1,4,1,2356,16,8,4530))
_LcosSxProductsGS4530XP_ObjectIdentity=ObjectIdentity
lcosSxProductsGS4530XP=_LcosSxProductsGS4530XP_ObjectIdentity((1,3,6,1,4,1,2356,16,8,4531))
_LcosSxProductsGS4554X_ObjectIdentity=ObjectIdentity
lcosSxProductsGS4554X=_LcosSxProductsGS4554X_ObjectIdentity((1,3,6,1,4,1,2356,16,8,4554))
_LcosSxProductsGS4554XP_ObjectIdentity=ObjectIdentity
lcosSxProductsGS4554XP=_LcosSxProductsGS4554XP_ObjectIdentity((1,3,6,1,4,1,2356,16,8,4555))
_LcosSxProductsXS5110F_ObjectIdentity=ObjectIdentity
lcosSxProductsXS5110F=_LcosSxProductsXS5110F_ObjectIdentity((1,3,6,1,4,1,2356,16,8,5110))
_LcosSxProductsXS5116QF_ObjectIdentity=ObjectIdentity
lcosSxProductsXS5116QF=_LcosSxProductsXS5116QF_ObjectIdentity((1,3,6,1,4,1,2356,16,8,5116))
_LcosSxProductsXS6128QF_ObjectIdentity=ObjectIdentity
lcosSxProductsXS6128QF=_LcosSxProductsXS6128QF_ObjectIdentity((1,3,6,1,4,1,2356,16,8,6128))
mibBuilder.exportSymbols('LCOS-SX-PRODUCTS-MIB',**{'lcosSxProducts':lcosSxProducts,'lcosSxProductsGS4530X':lcosSxProductsGS4530X,'lcosSxProductsGS4530XP':lcosSxProductsGS4530XP,'lcosSxProductsGS4554X':lcosSxProductsGS4554X,'lcosSxProductsGS4554XP':lcosSxProductsGS4554XP,'lcosSxProductsXS5110F':lcosSxProductsXS5110F,'lcosSxProductsXS5116QF':lcosSxProductsXS5116QF,'lcosSxProductsXS6128QF':lcosSxProductsXS6128QF})