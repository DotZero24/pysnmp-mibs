_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
xediaRegistrations=ModuleIdentity((1,3,6,1,4,1,838,2))
class LongDisplayString(TextualConvention,OctetString):status=_A;subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,2048))
_Xedia_ObjectIdentity=ObjectIdentity
xedia=_Xedia_ObjectIdentity((1,3,6,1,4,1,838))
if mibBuilder.loadTexts:xedia.setStatus(_A)
_XediaMibs_ObjectIdentity=ObjectIdentity
xediaMibs=_XediaMibs_ObjectIdentity((1,3,6,1,4,1,838,3))
if mibBuilder.loadTexts:xediaMibs.setStatus(_A)
_XediaClasses_ObjectIdentity=ObjectIdentity
xediaClasses=_XediaClasses_ObjectIdentity((1,3,6,1,4,1,838,4))
if mibBuilder.loadTexts:xediaClasses.setStatus(_A)
_XediaProducts_ObjectIdentity=ObjectIdentity
xediaProducts=_XediaProducts_ObjectIdentity((1,3,6,1,4,1,838,5))
if mibBuilder.loadTexts:xediaProducts.setStatus(_A)
mibBuilder.exportSymbols('XEDIA-REG',**{'LongDisplayString':LongDisplayString,'xedia':xedia,'xediaRegistrations':xediaRegistrations,'xediaMibs':xediaMibs,'xediaClasses':xediaClasses,'xediaProducts':xediaProducts})