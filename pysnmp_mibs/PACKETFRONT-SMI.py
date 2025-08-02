_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
packetfront=ModuleIdentity((1,3,6,1,4,1,9303))
if mibBuilder.loadTexts:packetfront.setRevisions(('2009-03-23 10:39','2008-01-17 14:05','2007-05-11 12:28'))
_PfProduct_ObjectIdentity=ObjectIdentity
pfProduct=_PfProduct_ObjectIdentity((1,3,6,1,4,1,9303,1))
if mibBuilder.loadTexts:pfProduct.setStatus(_A)
_PfConfig_ObjectIdentity=ObjectIdentity
pfConfig=_PfConfig_ObjectIdentity((1,3,6,1,4,1,9303,2))
if mibBuilder.loadTexts:pfConfig.setStatus(_A)
_IpdConfig_ObjectIdentity=ObjectIdentity
ipdConfig=_IpdConfig_ObjectIdentity((1,3,6,1,4,1,9303,2,1))
if mibBuilder.loadTexts:ipdConfig.setStatus(_A)
_PfExperiment_ObjectIdentity=ObjectIdentity
pfExperiment=_PfExperiment_ObjectIdentity((1,3,6,1,4,1,9303,3))
if mibBuilder.loadTexts:pfExperiment.setStatus(_A)
_PfMgmt_ObjectIdentity=ObjectIdentity
pfMgmt=_PfMgmt_ObjectIdentity((1,3,6,1,4,1,9303,4))
if mibBuilder.loadTexts:pfMgmt.setStatus(_A)
_PfModules_ObjectIdentity=ObjectIdentity
pfModules=_PfModules_ObjectIdentity((1,3,6,1,4,1,9303,5))
if mibBuilder.loadTexts:pfModules.setStatus(_A)
mibBuilder.exportSymbols('PACKETFRONT-SMI',**{'packetfront':packetfront,'pfProduct':pfProduct,'pfConfig':pfConfig,'ipdConfig':ipdConfig,'pfExperiment':pfExperiment,'pfMgmt':pfMgmt,'pfModules':pfModules})