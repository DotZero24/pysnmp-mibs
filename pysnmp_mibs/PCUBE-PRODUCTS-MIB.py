if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
pcubeModules,pcubeProducts=mibBuilder.importSymbols('PCUBE-SMI','pcubeModules','pcubeProducts')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
pcubeProductsMIB=ModuleIdentity((1,3,6,1,4,1,5655,2,2))
if mibBuilder.loadTexts:pcubeProductsMIB.setRevisions(('2002-01-14 20:00',))
_Sce100_ObjectIdentity=ObjectIdentity
sce100=_Sce100_ObjectIdentity((1,3,6,1,4,1,5655,1,1))
_Sce1000_ObjectIdentity=ObjectIdentity
sce1000=_Sce1000_ObjectIdentity((1,3,6,1,4,1,5655,1,2))
_Sce2000_ObjectIdentity=ObjectIdentity
sce2000=_Sce2000_ObjectIdentity((1,3,6,1,4,1,5655,1,3))
mibBuilder.exportSymbols('PCUBE-PRODUCTS-MIB',**{'sce100':sce100,'sce1000':sce1000,'sce2000':sce2000,'pcubeProductsMIB':pcubeProductsMIB})