_E='agentPethPsePortEntry'
_D='FSM7326-POWER-ETHERNET-MIB'
_C='Gauge32'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
fsm7326,=mibBuilder.importSymbols('FSM7326-REF-MIB','fsm7326')
pethPsePortEntry,=mibBuilder.importSymbols('POWER-ETHERNET-MIB','pethPsePortEntry')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64',_C,'Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
fsm7326powerEthernetMIB=ModuleIdentity((1,3,6,1,4,1,4526,1,9,15))
if mibBuilder.loadTexts:fsm7326powerEthernetMIB.setRevisions(('2003-11-10 12:00',))
_AgentPethObjects_ObjectIdentity=ObjectIdentity
agentPethObjects=_AgentPethObjects_ObjectIdentity((1,3,6,1,4,1,4526,1,9,15,1))
_AgentPethPsePortTable_Object=MibTable
agentPethPsePortTable=_AgentPethPsePortTable_Object((1,3,6,1,4,1,4526,1,9,15,1,1))
if mibBuilder.loadTexts:agentPethPsePortTable.setStatus(_A)
_AgentPethPsePortEntry_Object=MibTableRow
agentPethPsePortEntry=_AgentPethPsePortEntry_Object((1,3,6,1,4,1,4526,1,9,15,1,1,1))
if mibBuilder.loadTexts:agentPethPsePortEntry.setStatus(_A)
class _AgentPethPowerLimit_Type(Gauge32):subtypeSpec=Gauge32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(3,16))
_AgentPethPowerLimit_Type.__name__=_C
_AgentPethPowerLimit_Object=MibTableColumn
agentPethPowerLimit=_AgentPethPowerLimit_Object((1,3,6,1,4,1,4526,1,9,15,1,1,1,1),_AgentPethPowerLimit_Type())
agentPethPowerLimit.setMaxAccess('read-write')
if mibBuilder.loadTexts:agentPethPowerLimit.setStatus(_A)
if mibBuilder.loadTexts:agentPethPowerLimit.setUnits('Watts')
_AgentPethOutputPower_Type=Gauge32
_AgentPethOutputPower_Object=MibTableColumn
agentPethOutputPower=_AgentPethOutputPower_Object((1,3,6,1,4,1,4526,1,9,15,1,1,1,2),_AgentPethOutputPower_Type())
agentPethOutputPower.setMaxAccess(_B)
if mibBuilder.loadTexts:agentPethOutputPower.setStatus(_A)
if mibBuilder.loadTexts:agentPethOutputPower.setUnits('Milliwatts')
_AgentPethOutputCurrent_Type=Gauge32
_AgentPethOutputCurrent_Object=MibTableColumn
agentPethOutputCurrent=_AgentPethOutputCurrent_Object((1,3,6,1,4,1,4526,1,9,15,1,1,1,3),_AgentPethOutputCurrent_Type())
agentPethOutputCurrent.setMaxAccess(_B)
if mibBuilder.loadTexts:agentPethOutputCurrent.setStatus(_A)
if mibBuilder.loadTexts:agentPethOutputCurrent.setUnits('Milliamps')
_AgentPethOutputVolts_Type=Gauge32
_AgentPethOutputVolts_Object=MibTableColumn
agentPethOutputVolts=_AgentPethOutputVolts_Object((1,3,6,1,4,1,4526,1,9,15,1,1,1,4),_AgentPethOutputVolts_Type())
agentPethOutputVolts.setMaxAccess(_B)
if mibBuilder.loadTexts:agentPethOutputVolts.setStatus(_A)
if mibBuilder.loadTexts:agentPethOutputVolts.setUnits('Volts')
pethPsePortEntry.registerAugmentions((_D,_E))
agentPethPsePortEntry.setIndexNames(*pethPsePortEntry.getIndexNames())
mibBuilder.exportSymbols(_D,**{'fsm7326powerEthernetMIB':fsm7326powerEthernetMIB,'agentPethObjects':agentPethObjects,'agentPethPsePortTable':agentPethPsePortTable,_E:agentPethPsePortEntry,'agentPethPowerLimit':agentPethPowerLimit,'agentPethOutputPower':agentPethOutputPower,'agentPethOutputCurrent':agentPethOutputCurrent,'agentPethOutputVolts':agentPethOutputVolts})