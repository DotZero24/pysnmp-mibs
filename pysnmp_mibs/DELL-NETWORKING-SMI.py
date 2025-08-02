_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
dellNet=ModuleIdentity((1,3,6,1,4,1,6027))
if mibBuilder.loadTexts:dellNet.setRevisions(('2007-06-15 12:00','1900-10-10 00:00'))
_DellNetProducts_ObjectIdentity=ObjectIdentity
dellNetProducts=_DellNetProducts_ObjectIdentity((1,3,6,1,4,1,6027,1))
if mibBuilder.loadTexts:dellNetProducts.setStatus(_A)
_DellNetCommon_ObjectIdentity=ObjectIdentity
dellNetCommon=_DellNetCommon_ObjectIdentity((1,3,6,1,4,1,6027,2))
if mibBuilder.loadTexts:dellNetCommon.setStatus(_A)
_DellNetMgmt_ObjectIdentity=ObjectIdentity
dellNetMgmt=_DellNetMgmt_ObjectIdentity((1,3,6,1,4,1,6027,3))
if mibBuilder.loadTexts:dellNetMgmt.setStatus(_A)
_DellNetModules_ObjectIdentity=ObjectIdentity
dellNetModules=_DellNetModules_ObjectIdentity((1,3,6,1,4,1,6027,4))
if mibBuilder.loadTexts:dellNetModules.setStatus(_A)
_DellNetExperiment_ObjectIdentity=ObjectIdentity
dellNetExperiment=_DellNetExperiment_ObjectIdentity((1,3,6,1,4,1,6027,20))
if mibBuilder.loadTexts:dellNetExperiment.setStatus(_A)
mibBuilder.exportSymbols('DELL-NETWORKING-SMI',**{'dellNet':dellNet,'dellNetProducts':dellNetProducts,'dellNetCommon':dellNetCommon,'dellNetMgmt':dellNetMgmt,'dellNetModules':dellNetModules,'dellNetExperiment':dellNetExperiment})