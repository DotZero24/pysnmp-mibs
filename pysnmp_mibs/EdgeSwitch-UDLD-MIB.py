_H='seconds'
_G='disable'
_F='enable'
_E='ifIndex'
_D='IF-MIB'
_C='read-write'
_B='Integer32'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
fastPath,=mibBuilder.importSymbols('EdgeSwitch-REF-MIB','fastPath')
ifIndex,=mibBuilder.importSymbols(_D,_E)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_B,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention','TruthValue')
fastPathUdld=ModuleIdentity((1,3,6,1,4,1,4413,1,1,54))
if mibBuilder.loadTexts:fastPathUdld.setRevisions(('2008-02-24 00:00',))
_AgentUdldMIBObjects_ObjectIdentity=ObjectIdentity
agentUdldMIBObjects=_AgentUdldMIBObjects_ObjectIdentity((1,3,6,1,4,1,4413,1,1,54,1))
_AgentUdldGlobal_ObjectIdentity=ObjectIdentity
agentUdldGlobal=_AgentUdldGlobal_ObjectIdentity((1,3,6,1,4,1,4413,1,1,54,1,1))
class _AgentUdldGlobalMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_AgentUdldGlobalMode_Type.__name__=_B
_AgentUdldGlobalMode_Object=MibScalar
agentUdldGlobalMode=_AgentUdldGlobalMode_Object((1,3,6,1,4,1,4413,1,1,54,1,1,1),_AgentUdldGlobalMode_Type())
agentUdldGlobalMode.setMaxAccess(_C)
if mibBuilder.loadTexts:agentUdldGlobalMode.setStatus(_A)
class _AgentUdldMessageInterval_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(7,90))
_AgentUdldMessageInterval_Type.__name__=_B
_AgentUdldMessageInterval_Object=MibScalar
agentUdldMessageInterval=_AgentUdldMessageInterval_Object((1,3,6,1,4,1,4413,1,1,54,1,1,2),_AgentUdldMessageInterval_Type())
agentUdldMessageInterval.setMaxAccess(_C)
if mibBuilder.loadTexts:agentUdldMessageInterval.setStatus(_A)
if mibBuilder.loadTexts:agentUdldMessageInterval.setUnits(_H)
class _AgentUdldTimeoutInterval_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(5,60))
_AgentUdldTimeoutInterval_Type.__name__=_B
_AgentUdldTimeoutInterval_Object=MibScalar
agentUdldTimeoutInterval=_AgentUdldTimeoutInterval_Object((1,3,6,1,4,1,4413,1,1,54,1,1,3),_AgentUdldTimeoutInterval_Type())
agentUdldTimeoutInterval.setMaxAccess(_C)
if mibBuilder.loadTexts:agentUdldTimeoutInterval.setStatus(_A)
if mibBuilder.loadTexts:agentUdldTimeoutInterval.setUnits(_H)
class _AgentUdldReset_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('normalOperation',0),('reset',1)))
_AgentUdldReset_Type.__name__=_B
_AgentUdldReset_Object=MibScalar
agentUdldReset=_AgentUdldReset_Object((1,3,6,1,4,1,4413,1,1,54,1,1,4),_AgentUdldReset_Type())
agentUdldReset.setMaxAccess(_C)
if mibBuilder.loadTexts:agentUdldReset.setStatus(_A)
_AgentUdldInterface_ObjectIdentity=ObjectIdentity
agentUdldInterface=_AgentUdldInterface_ObjectIdentity((1,3,6,1,4,1,4413,1,1,54,1,2))
_AgentUdldInterfaceTable_Object=MibTable
agentUdldInterfaceTable=_AgentUdldInterfaceTable_Object((1,3,6,1,4,1,4413,1,1,54,1,2,1))
if mibBuilder.loadTexts:agentUdldInterfaceTable.setStatus(_A)
_AgentUdldInterfaceEntry_Object=MibTableRow
agentUdldInterfaceEntry=_AgentUdldInterfaceEntry_Object((1,3,6,1,4,1,4413,1,1,54,1,2,1,1))
agentUdldInterfaceEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:agentUdldInterfaceEntry.setStatus(_A)
class _AgentUdldInterfaceOperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('shutdown',1),('undetermined',2),('biDirectional',3),('notApplicable',4),('undetermined-LinkDown',5)))
_AgentUdldInterfaceOperStatus_Type.__name__=_B
_AgentUdldInterfaceOperStatus_Object=MibTableColumn
agentUdldInterfaceOperStatus=_AgentUdldInterfaceOperStatus_Object((1,3,6,1,4,1,4413,1,1,54,1,2,1,1,1),_AgentUdldInterfaceOperStatus_Type())
agentUdldInterfaceOperStatus.setMaxAccess('read-only')
if mibBuilder.loadTexts:agentUdldInterfaceOperStatus.setStatus(_A)
class _AgentUdldInterfaceAdminMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_AgentUdldInterfaceAdminMode_Type.__name__=_B
_AgentUdldInterfaceAdminMode_Object=MibTableColumn
agentUdldInterfaceAdminMode=_AgentUdldInterfaceAdminMode_Object((1,3,6,1,4,1,4413,1,1,54,1,2,1,1,2),_AgentUdldInterfaceAdminMode_Type())
agentUdldInterfaceAdminMode.setMaxAccess(_C)
if mibBuilder.loadTexts:agentUdldInterfaceAdminMode.setStatus(_A)
_AgentUdldInterfaceAggresiveMode_Type=TruthValue
_AgentUdldInterfaceAggresiveMode_Object=MibTableColumn
agentUdldInterfaceAggresiveMode=_AgentUdldInterfaceAggresiveMode_Object((1,3,6,1,4,1,4413,1,1,54,1,2,1,1,3),_AgentUdldInterfaceAggresiveMode_Type())
agentUdldInterfaceAggresiveMode.setMaxAccess(_C)
if mibBuilder.loadTexts:agentUdldInterfaceAggresiveMode.setStatus(_A)
mibBuilder.exportSymbols('EdgeSwitch-UDLD-MIB',**{'fastPathUdld':fastPathUdld,'agentUdldMIBObjects':agentUdldMIBObjects,'agentUdldGlobal':agentUdldGlobal,'agentUdldGlobalMode':agentUdldGlobalMode,'agentUdldMessageInterval':agentUdldMessageInterval,'agentUdldTimeoutInterval':agentUdldTimeoutInterval,'agentUdldReset':agentUdldReset,'agentUdldInterface':agentUdldInterface,'agentUdldInterfaceTable':agentUdldInterfaceTable,'agentUdldInterfaceEntry':agentUdldInterfaceEntry,'agentUdldInterfaceOperStatus':agentUdldInterfaceOperStatus,'agentUdldInterfaceAdminMode':agentUdldInterfaceAdminMode,'agentUdldInterfaceAggresiveMode':agentUdldInterfaceAggresiveMode})