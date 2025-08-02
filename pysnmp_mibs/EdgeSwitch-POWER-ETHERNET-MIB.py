_J='agentPethPseEntry'
_I='agentPethMainPseEntry'
_H='agentPethPsePortEntry'
_G='EdgeSwitch-POWER-ETHERNET-MIB'
_F='Milliwatts'
_E='none'
_D='Integer32'
_C='read-only'
_B='read-write'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
fastPath,=mibBuilder.importSymbols('EdgeSwitch-REF-MIB','fastPath')
pethMainPseEntry,pethPsePortEntry=mibBuilder.importSymbols('POWER-ETHERNET-MIB','pethMainPseEntry','pethPsePortEntry')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention','TruthValue')
fastPathpowerEthernetMIB=ModuleIdentity((1,3,6,1,4,1,4413,1,1,15))
if mibBuilder.loadTexts:fastPathpowerEthernetMIB.setRevisions(('2015-03-13 00:00','2014-04-16 00:00','2011-01-26 00:00','2007-08-19 12:00','2007-05-23 00:00','2003-11-10 12:00'))
_AgentPethObjects_ObjectIdentity=ObjectIdentity
agentPethObjects=_AgentPethObjects_ObjectIdentity((1,3,6,1,4,1,4413,1,1,15,1))
_AgentPethPsePortTable_Object=MibTable
agentPethPsePortTable=_AgentPethPsePortTable_Object((1,3,6,1,4,1,4413,1,1,15,1,1))
if mibBuilder.loadTexts:agentPethPsePortTable.setStatus(_A)
_AgentPethPsePortEntry_Object=MibTableRow
agentPethPsePortEntry=_AgentPethPsePortEntry_Object((1,3,6,1,4,1,4413,1,1,15,1,1,1))
if mibBuilder.loadTexts:agentPethPsePortEntry.setStatus(_A)
_AgentPethPowerLimit_Type=Gauge32
_AgentPethPowerLimit_Object=MibTableColumn
agentPethPowerLimit=_AgentPethPowerLimit_Object((1,3,6,1,4,1,4413,1,1,15,1,1,1,1),_AgentPethPowerLimit_Type())
agentPethPowerLimit.setMaxAccess(_B)
if mibBuilder.loadTexts:agentPethPowerLimit.setStatus(_A)
if mibBuilder.loadTexts:agentPethPowerLimit.setUnits(_F)
_AgentPethOutputPower_Type=Gauge32
_AgentPethOutputPower_Object=MibTableColumn
agentPethOutputPower=_AgentPethOutputPower_Object((1,3,6,1,4,1,4413,1,1,15,1,1,1,2),_AgentPethOutputPower_Type())
agentPethOutputPower.setMaxAccess(_C)
if mibBuilder.loadTexts:agentPethOutputPower.setStatus(_A)
if mibBuilder.loadTexts:agentPethOutputPower.setUnits(_F)
_AgentPethOutputCurrent_Type=Gauge32
_AgentPethOutputCurrent_Object=MibTableColumn
agentPethOutputCurrent=_AgentPethOutputCurrent_Object((1,3,6,1,4,1,4413,1,1,15,1,1,1,3),_AgentPethOutputCurrent_Type())
agentPethOutputCurrent.setMaxAccess(_C)
if mibBuilder.loadTexts:agentPethOutputCurrent.setStatus(_A)
if mibBuilder.loadTexts:agentPethOutputCurrent.setUnits('Milliamps')
_AgentPethOutputVolts_Type=Gauge32
_AgentPethOutputVolts_Object=MibTableColumn
agentPethOutputVolts=_AgentPethOutputVolts_Object((1,3,6,1,4,1,4413,1,1,15,1,1,1,4),_AgentPethOutputVolts_Type())
agentPethOutputVolts.setMaxAccess(_C)
if mibBuilder.loadTexts:agentPethOutputVolts.setStatus(_A)
if mibBuilder.loadTexts:agentPethOutputVolts.setUnits('Volts')
_AgentPethTemperature_Type=Gauge32
_AgentPethTemperature_Object=MibTableColumn
agentPethTemperature=_AgentPethTemperature_Object((1,3,6,1,4,1,4413,1,1,15,1,1,1,5),_AgentPethTemperature_Type())
agentPethTemperature.setMaxAccess(_C)
if mibBuilder.loadTexts:agentPethTemperature.setStatus('obsolete')
if mibBuilder.loadTexts:agentPethTemperature.setUnits('DEGREES')
class _AgentPethPowerLimitType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('dot3af',1),('user',2),(_E,3)))
_AgentPethPowerLimitType_Type.__name__=_D
_AgentPethPowerLimitType_Object=MibTableColumn
agentPethPowerLimitType=_AgentPethPowerLimitType_Object((1,3,6,1,4,1,4413,1,1,15,1,1,1,6),_AgentPethPowerLimitType_Type())
agentPethPowerLimitType.setMaxAccess(_B)
if mibBuilder.loadTexts:agentPethPowerLimitType.setStatus(_A)
_AgentPethHighPowerEnable_Type=TruthValue
_AgentPethHighPowerEnable_Object=MibTableColumn
agentPethHighPowerEnable=_AgentPethHighPowerEnable_Object((1,3,6,1,4,1,4413,1,1,15,1,1,1,7),_AgentPethHighPowerEnable_Type())
agentPethHighPowerEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:agentPethHighPowerEnable.setStatus(_A)
class _AgentPethPowerDetectionType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5)));namedValues=NamedValues(*((_E,0),('legacy',1),('fourPtdot3afonly',2),('fourPtdot3afandlegacy',3),('twoPtdot3afonly',4),('twoPtdot3afandlegacy',5)))
_AgentPethPowerDetectionType_Type.__name__=_D
_AgentPethPowerDetectionType_Object=MibTableColumn
agentPethPowerDetectionType=_AgentPethPowerDetectionType_Object((1,3,6,1,4,1,4413,1,1,15,1,1,1,8),_AgentPethPowerDetectionType_Type())
agentPethPowerDetectionType.setMaxAccess(_B)
if mibBuilder.loadTexts:agentPethPowerDetectionType.setStatus(_A)
class _AgentPethFaultStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6)));namedValues=NamedValues(*((_E,0),('mpsAbsent',1),('short',2),('overload',3),('powerDenied',4),('thermalShutdown',5),('startupFailure',6)))
_AgentPethFaultStatus_Type.__name__=_D
_AgentPethFaultStatus_Object=MibTableColumn
agentPethFaultStatus=_AgentPethFaultStatus_Object((1,3,6,1,4,1,4413,1,1,15,1,1,1,9),_AgentPethFaultStatus_Type())
agentPethFaultStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:agentPethFaultStatus.setStatus(_A)
class _AgentPethPortReset_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),('reset',1)))
_AgentPethPortReset_Type.__name__=_D
_AgentPethPortReset_Object=MibTableColumn
agentPethPortReset=_AgentPethPortReset_Object((1,3,6,1,4,1,4413,1,1,15,1,1,1,10),_AgentPethPortReset_Type())
agentPethPortReset.setMaxAccess(_B)
if mibBuilder.loadTexts:agentPethPortReset.setStatus(_A)
_AgentPethPowerLimitMin_Type=Gauge32
_AgentPethPowerLimitMin_Object=MibTableColumn
agentPethPowerLimitMin=_AgentPethPowerLimitMin_Object((1,3,6,1,4,1,4413,1,1,15,1,1,1,11),_AgentPethPowerLimitMin_Type())
agentPethPowerLimitMin.setMaxAccess(_C)
if mibBuilder.loadTexts:agentPethPowerLimitMin.setStatus(_A)
if mibBuilder.loadTexts:agentPethPowerLimitMin.setUnits(_F)
_AgentPethPowerLimitMax_Type=Gauge32
_AgentPethPowerLimitMax_Object=MibTableColumn
agentPethPowerLimitMax=_AgentPethPowerLimitMax_Object((1,3,6,1,4,1,4413,1,1,15,1,1,1,12),_AgentPethPowerLimitMax_Type())
agentPethPowerLimitMax.setMaxAccess(_C)
if mibBuilder.loadTexts:agentPethPowerLimitMax.setStatus(_A)
if mibBuilder.loadTexts:agentPethPowerLimitMax.setUnits(_F)
_AgentPethMainPseObjects_ObjectIdentity=ObjectIdentity
agentPethMainPseObjects=_AgentPethMainPseObjects_ObjectIdentity((1,3,6,1,4,1,4413,1,1,15,1,2))
_AgentPethMainPseTable_Object=MibTable
agentPethMainPseTable=_AgentPethMainPseTable_Object((1,3,6,1,4,1,4413,1,1,15,1,2,1))
if mibBuilder.loadTexts:agentPethMainPseTable.setStatus(_A)
_AgentPethMainPseEntry_Object=MibTableRow
agentPethMainPseEntry=_AgentPethMainPseEntry_Object((1,3,6,1,4,1,4413,1,1,15,1,2,1,1))
if mibBuilder.loadTexts:agentPethMainPseEntry.setStatus(_A)
_AgentPethMainPseLegacy_Type=TruthValue
_AgentPethMainPseLegacy_Object=MibTableColumn
agentPethMainPseLegacy=_AgentPethMainPseLegacy_Object((1,3,6,1,4,1,4413,1,1,15,1,2,1,1,1),_AgentPethMainPseLegacy_Type())
agentPethMainPseLegacy.setMaxAccess(_B)
if mibBuilder.loadTexts:agentPethMainPseLegacy.setStatus(_A)
_AgentPethPseTable_Object=MibTable
agentPethPseTable=_AgentPethPseTable_Object((1,3,6,1,4,1,4413,1,1,15,1,3))
if mibBuilder.loadTexts:agentPethPseTable.setStatus(_A)
_AgentPethPseEntry_Object=MibTableRow
agentPethPseEntry=_AgentPethPseEntry_Object((1,3,6,1,4,1,4413,1,1,15,1,3,1))
if mibBuilder.loadTexts:agentPethPseEntry.setStatus(_A)
class _AgentPethPsePowerManagementMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_E,0),('dynamic',1),('static',2)))
_AgentPethPsePowerManagementMode_Type.__name__=_D
_AgentPethPsePowerManagementMode_Object=MibTableColumn
agentPethPsePowerManagementMode=_AgentPethPsePowerManagementMode_Object((1,3,6,1,4,1,4413,1,1,15,1,3,1,1),_AgentPethPsePowerManagementMode_Type())
agentPethPsePowerManagementMode.setMaxAccess(_B)
if mibBuilder.loadTexts:agentPethPsePowerManagementMode.setStatus(_A)
pethPsePortEntry.registerAugmentions((_G,_H))
agentPethPsePortEntry.setIndexNames(*pethPsePortEntry.getIndexNames())
pethMainPseEntry.registerAugmentions((_G,_I))
agentPethMainPseEntry.setIndexNames(*pethMainPseEntry.getIndexNames())
pethMainPseEntry.registerAugmentions((_G,_J))
agentPethPseEntry.setIndexNames(*pethMainPseEntry.getIndexNames())
mibBuilder.exportSymbols(_G,**{'fastPathpowerEthernetMIB':fastPathpowerEthernetMIB,'agentPethObjects':agentPethObjects,'agentPethPsePortTable':agentPethPsePortTable,_H:agentPethPsePortEntry,'agentPethPowerLimit':agentPethPowerLimit,'agentPethOutputPower':agentPethOutputPower,'agentPethOutputCurrent':agentPethOutputCurrent,'agentPethOutputVolts':agentPethOutputVolts,'agentPethTemperature':agentPethTemperature,'agentPethPowerLimitType':agentPethPowerLimitType,'agentPethHighPowerEnable':agentPethHighPowerEnable,'agentPethPowerDetectionType':agentPethPowerDetectionType,'agentPethFaultStatus':agentPethFaultStatus,'agentPethPortReset':agentPethPortReset,'agentPethPowerLimitMin':agentPethPowerLimitMin,'agentPethPowerLimitMax':agentPethPowerLimitMax,'agentPethMainPseObjects':agentPethMainPseObjects,'agentPethMainPseTable':agentPethMainPseTable,_I:agentPethMainPseEntry,'agentPethMainPseLegacy':agentPethMainPseLegacy,'agentPethPseTable':agentPethPseTable,_J:agentPethPseEntry,'agentPethPsePowerManagementMode':agentPethPsePowerManagementMode})