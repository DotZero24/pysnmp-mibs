_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
watchguard=ModuleIdentity((1,3,6,1,4,1,3097))
if mibBuilder.loadTexts:watchguard.setRevisions(('2008-11-10 00:00',))
_WgProducts_ObjectIdentity=ObjectIdentity
wgProducts=_WgProducts_ObjectIdentity((1,3,6,1,4,1,3097,1))
if mibBuilder.loadTexts:wgProducts.setStatus(_A)
_WgSystemConfigMIB_ObjectIdentity=ObjectIdentity
wgSystemConfigMIB=_WgSystemConfigMIB_ObjectIdentity((1,3,6,1,4,1,3097,2))
if mibBuilder.loadTexts:wgSystemConfigMIB.setStatus(_A)
mibBuilder.exportSymbols('WATCHGUARD-SMI',**{'watchguard':watchguard,'wgProducts':wgProducts,'wgSystemConfigMIB':wgSystemConfigMIB})