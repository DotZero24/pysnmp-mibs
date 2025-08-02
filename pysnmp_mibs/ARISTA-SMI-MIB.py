_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
arista=ModuleIdentity((1,3,6,1,4,1,30065))
if mibBuilder.loadTexts:arista.setRevisions(('2014-08-15 00:00','2011-03-31 13:00','2008-10-27 18:30'))
_AristaProducts_ObjectIdentity=ObjectIdentity
aristaProducts=_AristaProducts_ObjectIdentity((1,3,6,1,4,1,30065,1))
if mibBuilder.loadTexts:aristaProducts.setStatus(_A)
_AristaModules_ObjectIdentity=ObjectIdentity
aristaModules=_AristaModules_ObjectIdentity((1,3,6,1,4,1,30065,2))
if mibBuilder.loadTexts:aristaModules.setStatus(_A)
_AristaMibs_ObjectIdentity=ObjectIdentity
aristaMibs=_AristaMibs_ObjectIdentity((1,3,6,1,4,1,30065,3))
if mibBuilder.loadTexts:aristaMibs.setStatus(_A)
_AristaExperiment_ObjectIdentity=ObjectIdentity
aristaExperiment=_AristaExperiment_ObjectIdentity((1,3,6,1,4,1,30065,4))
if mibBuilder.loadTexts:aristaExperiment.setStatus(_A)
mibBuilder.exportSymbols('ARISTA-SMI-MIB',**{'arista':arista,'aristaProducts':aristaProducts,'aristaModules':aristaModules,'aristaMibs':aristaMibs,'aristaExperiment':aristaExperiment})