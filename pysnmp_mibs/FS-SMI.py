_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
switchMib=ModuleIdentity((1,3,6,1,4,1,52642,1,1,10))
if mibBuilder.loadTexts:switchMib.setRevisions(('2002-03-19 00:00',))
_Fs_ObjectIdentity=ObjectIdentity
fs=_Fs_ObjectIdentity((1,3,6,1,4,1,52642))
_Products_ObjectIdentity=ObjectIdentity
products=_Products_ObjectIdentity((1,3,6,1,4,1,52642,1))
_Switch_ObjectIdentity=ObjectIdentity
switch=_Switch_ObjectIdentity((1,3,6,1,4,1,52642,1,1))
_FsSwitchProducts_ObjectIdentity=ObjectIdentity
fsSwitchProducts=_FsSwitchProducts_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,1))
if mibBuilder.loadTexts:fsSwitchProducts.setStatus(_A)
_FsMgmt_ObjectIdentity=ObjectIdentity
fsMgmt=_FsMgmt_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2))
if mibBuilder.loadTexts:fsMgmt.setStatus(_A)
_FsAgentCapability_ObjectIdentity=ObjectIdentity
fsAgentCapability=_FsAgentCapability_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,3))
if mibBuilder.loadTexts:fsAgentCapability.setStatus(_A)
_FsModules_ObjectIdentity=ObjectIdentity
fsModules=_FsModules_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,4))
if mibBuilder.loadTexts:fsModules.setStatus(_A)
_FsExperiment_ObjectIdentity=ObjectIdentity
fsExperiment=_FsExperiment_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,5))
if mibBuilder.loadTexts:fsExperiment.setStatus(_A)
mibBuilder.exportSymbols('FS-SMI',**{'fs':fs,'products':products,'switch':switch,'switchMib':switchMib,'fsSwitchProducts':fsSwitchProducts,'fsMgmt':fsMgmt,'fsAgentCapability':fsAgentCapability,'fsModules':fsModules,'fsExperiment':fsExperiment})