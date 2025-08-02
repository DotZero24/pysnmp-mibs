_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
switchMib=ModuleIdentity((1,3,6,1,4,1,27514,1,1,10))
if mibBuilder.loadTexts:switchMib.setRevisions(('2002-03-19 00:00',))
_Qtech_ObjectIdentity=ObjectIdentity
qtech=_Qtech_ObjectIdentity((1,3,6,1,4,1,27514))
_Products_ObjectIdentity=ObjectIdentity
products=_Products_ObjectIdentity((1,3,6,1,4,1,27514,1))
_Switch_ObjectIdentity=ObjectIdentity
switch=_Switch_ObjectIdentity((1,3,6,1,4,1,27514,1,1))
_QtechSwitchProducts_ObjectIdentity=ObjectIdentity
qtechSwitchProducts=_QtechSwitchProducts_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,1))
if mibBuilder.loadTexts:qtechSwitchProducts.setStatus(_A)
_QtechMgmt_ObjectIdentity=ObjectIdentity
qtechMgmt=_QtechMgmt_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2))
if mibBuilder.loadTexts:qtechMgmt.setStatus(_A)
_QtechAgentCapability_ObjectIdentity=ObjectIdentity
qtechAgentCapability=_QtechAgentCapability_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,3))
if mibBuilder.loadTexts:qtechAgentCapability.setStatus(_A)
_QtechModules_ObjectIdentity=ObjectIdentity
qtechModules=_QtechModules_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,4))
if mibBuilder.loadTexts:qtechModules.setStatus(_A)
_QtechExperiment_ObjectIdentity=ObjectIdentity
qtechExperiment=_QtechExperiment_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,5))
if mibBuilder.loadTexts:qtechExperiment.setStatus(_A)
mibBuilder.exportSymbols('QTECH-SMI',**{'qtech':qtech,'products':products,'switch':switch,'switchMib':switchMib,'qtechSwitchProducts':qtechSwitchProducts,'qtechMgmt':qtechMgmt,'qtechAgentCapability':qtechAgentCapability,'qtechModules':qtechModules,'qtechExperiment':qtechExperiment})