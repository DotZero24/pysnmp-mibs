_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
schleifenbauer=ModuleIdentity((1,3,6,1,4,1,31034))
if mibBuilder.loadTexts:schleifenbauer.setRevisions(('2015-10-23 00:00',))
_SchleifenbauerProducts_ObjectIdentity=ObjectIdentity
schleifenbauerProducts=_SchleifenbauerProducts_ObjectIdentity((1,3,6,1,4,1,31034,11))
if mibBuilder.loadTexts:schleifenbauerProducts.setStatus(_A)
_SchleifenbauerMgmt_ObjectIdentity=ObjectIdentity
schleifenbauerMgmt=_SchleifenbauerMgmt_ObjectIdentity((1,3,6,1,4,1,31034,12))
if mibBuilder.loadTexts:schleifenbauerMgmt.setStatus(_A)
_SchleifenbauerModules_ObjectIdentity=ObjectIdentity
schleifenbauerModules=_SchleifenbauerModules_ObjectIdentity((1,3,6,1,4,1,31034,13))
if mibBuilder.loadTexts:schleifenbauerModules.setStatus(_A)
mibBuilder.exportSymbols('SCHLEIFENBAUER-SMI',**{'schleifenbauer':schleifenbauer,'schleifenbauerProducts':schleifenbauerProducts,'schleifenbauerMgmt':schleifenbauerMgmt,'schleifenbauerModules':schleifenbauerModules})