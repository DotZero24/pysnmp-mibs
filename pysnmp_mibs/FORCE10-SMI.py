_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
force10=ModuleIdentity((1,3,6,1,4,1,6027))
if mibBuilder.loadTexts:force10.setRevisions(('2007-06-15 12:00','1900-10-10 00:00'))
_F10Products_ObjectIdentity=ObjectIdentity
f10Products=_F10Products_ObjectIdentity((1,3,6,1,4,1,6027,1))
if mibBuilder.loadTexts:f10Products.setStatus(_A)
_F10Common_ObjectIdentity=ObjectIdentity
f10Common=_F10Common_ObjectIdentity((1,3,6,1,4,1,6027,2))
if mibBuilder.loadTexts:f10Common.setStatus(_A)
_F10Mgmt_ObjectIdentity=ObjectIdentity
f10Mgmt=_F10Mgmt_ObjectIdentity((1,3,6,1,4,1,6027,3))
if mibBuilder.loadTexts:f10Mgmt.setStatus(_A)
_F10Modules_ObjectIdentity=ObjectIdentity
f10Modules=_F10Modules_ObjectIdentity((1,3,6,1,4,1,6027,4))
if mibBuilder.loadTexts:f10Modules.setStatus(_A)
_F10Experiment_ObjectIdentity=ObjectIdentity
f10Experiment=_F10Experiment_ObjectIdentity((1,3,6,1,4,1,6027,20))
if mibBuilder.loadTexts:f10Experiment.setStatus(_A)
mibBuilder.exportSymbols('FORCE10-SMI',**{'force10':force10,'f10Products':f10Products,'f10Common':f10Common,'f10Mgmt':f10Mgmt,'f10Modules':f10Modules,'f10Experiment':f10Experiment})