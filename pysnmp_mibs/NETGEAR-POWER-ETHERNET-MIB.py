_T='agentPethPseEntry'
_S='agentPethMainPseEntry'
_R='agentPethPsePortEntry'
_Q='deprecated'
_P='not-accessible'
_O='agentPethPoeMainPseSlotIndex'
_N='agentPethPoeMainPseGroupIndex'
_M='static'
_L='dynamic'
_K='Gauge32'
_J='OctetString'
_I='Watts'
_H='DisplayString'
_G='Milliwatts'
_F='NETGEAR-POWER-ETHERNET-MIB'
_E='none'
_D='read-write'
_C='Integer32'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_J,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ng7000managedswitch,=mibBuilder.importSymbols('NETGEAR-REF-MIB','ng7000managedswitch')
pethMainPseEntry,pethPsePortEntry=mibBuilder.importSymbols('POWER-ETHERNET-MIB','pethMainPseEntry','pethPsePortEntry')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64',_K,_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC',_H,'PhysAddress','TextualConvention','TruthValue')
fastPathpowerEthernetMIB=ModuleIdentity((1,3,6,1,4,1,4526,10,15))
if mibBuilder.loadTexts:fastPathpowerEthernetMIB.setRevisions(('2018-03-02 00:00','2018-01-25 00:00','2015-03-13 00:00','2014-04-16 00:00','2011-01-26 00:00','2007-08-19 12:00','2007-05-23 00:00','2003-11-10 12:00'))
_AgentPethObjects_ObjectIdentity=ObjectIdentity
agentPethObjects=_AgentPethObjects_ObjectIdentity((1,3,6,1,4,1,4526,10,15,1))
_AgentPethPsePortTable_Object=MibTable
agentPethPsePortTable=_AgentPethPsePortTable_Object((1,3,6,1,4,1,4526,10,15,1,1))
if mibBuilder.loadTexts:agentPethPsePortTable.setStatus(_A)
_AgentPethPsePortEntry_Object=MibTableRow
agentPethPsePortEntry=_AgentPethPsePortEntry_Object((1,3,6,1,4,1,4526,10,15,1,1,1))
if mibBuilder.loadTexts:agentPethPsePortEntry.setStatus(_A)
_AgentPethPowerLimit_Type=Gauge32
_AgentPethPowerLimit_Object=MibTableColumn
agentPethPowerLimit=_AgentPethPowerLimit_Object((1,3,6,1,4,1,4526,10,15,1,1,1,1),_AgentPethPowerLimit_Type())
agentPethPowerLimit.setMaxAccess(_D)
if mibBuilder.loadTexts:agentPethPowerLimit.setStatus(_A)
if mibBuilder.loadTexts:agentPethPowerLimit.setUnits(_G)
_AgentPethOutputPower_Type=Gauge32
_AgentPethOutputPower_Object=MibTableColumn
agentPethOutputPower=_AgentPethOutputPower_Object((1,3,6,1,4,1,4526,10,15,1,1,1,2),_AgentPethOutputPower_Type())
agentPethOutputPower.setMaxAccess(_B)
if mibBuilder.loadTexts:agentPethOutputPower.setStatus(_A)
if mibBuilder.loadTexts:agentPethOutputPower.setUnits(_G)
_AgentPethOutputCurrent_Type=Gauge32
_AgentPethOutputCurrent_Object=MibTableColumn
agentPethOutputCurrent=_AgentPethOutputCurrent_Object((1,3,6,1,4,1,4526,10,15,1,1,1,3),_AgentPethOutputCurrent_Type())
agentPethOutputCurrent.setMaxAccess(_B)
if mibBuilder.loadTexts:agentPethOutputCurrent.setStatus(_A)
if mibBuilder.loadTexts:agentPethOutputCurrent.setUnits('Milliamps')
_AgentPethOutputVolts_Type=Gauge32
_AgentPethOutputVolts_Object=MibTableColumn
agentPethOutputVolts=_AgentPethOutputVolts_Object((1,3,6,1,4,1,4526,10,15,1,1,1,4),_AgentPethOutputVolts_Type())
agentPethOutputVolts.setMaxAccess(_B)
if mibBuilder.loadTexts:agentPethOutputVolts.setStatus(_A)
if mibBuilder.loadTexts:agentPethOutputVolts.setUnits('Volts')
_AgentPethTemperature_Type=Gauge32
_AgentPethTemperature_Object=MibTableColumn
agentPethTemperature=_AgentPethTemperature_Object((1,3,6,1,4,1,4526,10,15,1,1,1,5),_AgentPethTemperature_Type())
agentPethTemperature.setMaxAccess(_B)
if mibBuilder.loadTexts:agentPethTemperature.setStatus('obsolete')
if mibBuilder.loadTexts:agentPethTemperature.setUnits('DEGREES')
class _AgentPethPowerLimitType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('dot3af',1),('user',2),(_E,3)))
_AgentPethPowerLimitType_Type.__name__=_C
_AgentPethPowerLimitType_Object=MibTableColumn
agentPethPowerLimitType=_AgentPethPowerLimitType_Object((1,3,6,1,4,1,4526,10,15,1,1,1,6),_AgentPethPowerLimitType_Type())
agentPethPowerLimitType.setMaxAccess(_D)
if mibBuilder.loadTexts:agentPethPowerLimitType.setStatus(_A)
_AgentPethHighPowerEnable_Type=TruthValue
_AgentPethHighPowerEnable_Object=MibTableColumn
agentPethHighPowerEnable=_AgentPethHighPowerEnable_Object((1,3,6,1,4,1,4526,10,15,1,1,1,7),_AgentPethHighPowerEnable_Type())
agentPethHighPowerEnable.setMaxAccess(_D)
if mibBuilder.loadTexts:agentPethHighPowerEnable.setStatus(_A)
class _AgentPethPowerDetectionType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5)));namedValues=NamedValues(*((_E,0),('legacy',1),('fourPtdot3afonly',2),('fourPtdot3afandlegacy',3),('twoPtdot3afonly',4),('twoPtdot3afandlegacy',5)))
_AgentPethPowerDetectionType_Type.__name__=_C
_AgentPethPowerDetectionType_Object=MibTableColumn
agentPethPowerDetectionType=_AgentPethPowerDetectionType_Object((1,3,6,1,4,1,4526,10,15,1,1,1,8),_AgentPethPowerDetectionType_Type())
agentPethPowerDetectionType.setMaxAccess(_D)
if mibBuilder.loadTexts:agentPethPowerDetectionType.setStatus(_A)
class _AgentPethFaultStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6)));namedValues=NamedValues(*((_E,0),('mpsAbsent',1),('short',2),('overload',3),('powerDenied',4),('thermalShutdown',5),('startupFailure',6)))
_AgentPethFaultStatus_Type.__name__=_C
_AgentPethFaultStatus_Object=MibTableColumn
agentPethFaultStatus=_AgentPethFaultStatus_Object((1,3,6,1,4,1,4526,10,15,1,1,1,9),_AgentPethFaultStatus_Type())
agentPethFaultStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:agentPethFaultStatus.setStatus(_A)
class _AgentPethPortReset_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),('reset',1)))
_AgentPethPortReset_Type.__name__=_C
_AgentPethPortReset_Object=MibTableColumn
agentPethPortReset=_AgentPethPortReset_Object((1,3,6,1,4,1,4526,10,15,1,1,1,10),_AgentPethPortReset_Type())
agentPethPortReset.setMaxAccess(_D)
if mibBuilder.loadTexts:agentPethPortReset.setStatus(_A)
_AgentPethPowerLimitMin_Type=Gauge32
_AgentPethPowerLimitMin_Object=MibTableColumn
agentPethPowerLimitMin=_AgentPethPowerLimitMin_Object((1,3,6,1,4,1,4526,10,15,1,1,1,11),_AgentPethPowerLimitMin_Type())
agentPethPowerLimitMin.setMaxAccess(_B)
if mibBuilder.loadTexts:agentPethPowerLimitMin.setStatus(_A)
if mibBuilder.loadTexts:agentPethPowerLimitMin.setUnits(_G)
_AgentPethPowerLimitMax_Type=Gauge32
_AgentPethPowerLimitMax_Object=MibTableColumn
agentPethPowerLimitMax=_AgentPethPowerLimitMax_Object((1,3,6,1,4,1,4526,10,15,1,1,1,12),_AgentPethPowerLimitMax_Type())
agentPethPowerLimitMax.setMaxAccess(_B)
if mibBuilder.loadTexts:agentPethPowerLimitMax.setStatus(_A)
if mibBuilder.loadTexts:agentPethPowerLimitMax.setUnits(_G)
_AgentPethMainPseObjects_ObjectIdentity=ObjectIdentity
agentPethMainPseObjects=_AgentPethMainPseObjects_ObjectIdentity((1,3,6,1,4,1,4526,10,15,1,2))
_AgentPethMainPseTable_Object=MibTable
agentPethMainPseTable=_AgentPethMainPseTable_Object((1,3,6,1,4,1,4526,10,15,1,2,1))
if mibBuilder.loadTexts:agentPethMainPseTable.setStatus(_A)
_AgentPethMainPseEntry_Object=MibTableRow
agentPethMainPseEntry=_AgentPethMainPseEntry_Object((1,3,6,1,4,1,4526,10,15,1,2,1,1))
if mibBuilder.loadTexts:agentPethMainPseEntry.setStatus(_A)
_AgentPethMainPseLegacy_Type=TruthValue
_AgentPethMainPseLegacy_Object=MibTableColumn
agentPethMainPseLegacy=_AgentPethMainPseLegacy_Object((1,3,6,1,4,1,4526,10,15,1,2,1,1,1),_AgentPethMainPseLegacy_Type())
agentPethMainPseLegacy.setMaxAccess(_D)
if mibBuilder.loadTexts:agentPethMainPseLegacy.setStatus(_A)
_AgentPethPseTable_Object=MibTable
agentPethPseTable=_AgentPethPseTable_Object((1,3,6,1,4,1,4526,10,15,1,3))
if mibBuilder.loadTexts:agentPethPseTable.setStatus(_A)
_AgentPethPseEntry_Object=MibTableRow
agentPethPseEntry=_AgentPethPseEntry_Object((1,3,6,1,4,1,4526,10,15,1,3,1))
if mibBuilder.loadTexts:agentPethPseEntry.setStatus(_A)
class _AgentPethPsePowerManagementMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_E,0),(_L,1),(_M,2)))
_AgentPethPsePowerManagementMode_Type.__name__=_C
_AgentPethPsePowerManagementMode_Object=MibTableColumn
agentPethPsePowerManagementMode=_AgentPethPsePowerManagementMode_Object((1,3,6,1,4,1,4526,10,15,1,3,1,1),_AgentPethPsePowerManagementMode_Type())
agentPethPsePowerManagementMode.setMaxAccess(_D)
if mibBuilder.loadTexts:agentPethPsePowerManagementMode.setStatus(_A)
_AgentPethPseThresholdPower_Type=Gauge32
_AgentPethPseThresholdPower_Object=MibTableColumn
agentPethPseThresholdPower=_AgentPethPseThresholdPower_Object((1,3,6,1,4,1,4526,10,15,1,3,1,6),_AgentPethPseThresholdPower_Type())
agentPethPseThresholdPower.setMaxAccess(_B)
if mibBuilder.loadTexts:agentPethPseThresholdPower.setStatus(_A)
if mibBuilder.loadTexts:agentPethPseThresholdPower.setUnits(_I)
_AgentPethPoeMainPseObjects_ObjectIdentity=ObjectIdentity
agentPethPoeMainPseObjects=_AgentPethPoeMainPseObjects_ObjectIdentity((1,3,6,1,4,1,4526,10,15,1,4))
_AgentPethPoeMainPseTable_Object=MibTable
agentPethPoeMainPseTable=_AgentPethPoeMainPseTable_Object((1,3,6,1,4,1,4526,10,15,1,4,1))
if mibBuilder.loadTexts:agentPethPoeMainPseTable.setStatus(_A)
_AgentPethPoeMainPseEntry_Object=MibTableRow
agentPethPoeMainPseEntry=_AgentPethPoeMainPseEntry_Object((1,3,6,1,4,1,4526,10,15,1,4,1,1))
agentPethPoeMainPseEntry.setIndexNames((0,_F,_N),(0,_F,_O))
if mibBuilder.loadTexts:agentPethPoeMainPseEntry.setStatus(_A)
class _AgentPethPoeMainPseGroupIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_AgentPethPoeMainPseGroupIndex_Type.__name__=_C
_AgentPethPoeMainPseGroupIndex_Object=MibTableColumn
agentPethPoeMainPseGroupIndex=_AgentPethPoeMainPseGroupIndex_Object((1,3,6,1,4,1,4526,10,15,1,4,1,1,1),_AgentPethPoeMainPseGroupIndex_Type())
agentPethPoeMainPseGroupIndex.setMaxAccess(_P)
if mibBuilder.loadTexts:agentPethPoeMainPseGroupIndex.setStatus(_A)
class _AgentPethPoeMainPseSlotIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_AgentPethPoeMainPseSlotIndex_Type.__name__=_C
_AgentPethPoeMainPseSlotIndex_Object=MibTableColumn
agentPethPoeMainPseSlotIndex=_AgentPethPoeMainPseSlotIndex_Object((1,3,6,1,4,1,4526,10,15,1,4,1,1,2),_AgentPethPoeMainPseSlotIndex_Type())
agentPethPoeMainPseSlotIndex.setMaxAccess(_P)
if mibBuilder.loadTexts:agentPethPoeMainPseSlotIndex.setStatus(_A)
class _AgentPethPoeMainPsePower_Type(Gauge32):subtypeSpec=Gauge32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_AgentPethPoeMainPsePower_Type.__name__=_K
_AgentPethPoeMainPsePower_Object=MibTableColumn
agentPethPoeMainPsePower=_AgentPethPoeMainPsePower_Object((1,3,6,1,4,1,4526,10,15,1,4,1,1,3),_AgentPethPoeMainPsePower_Type())
agentPethPoeMainPsePower.setMaxAccess(_B)
if mibBuilder.loadTexts:agentPethPoeMainPsePower.setStatus(_A)
if mibBuilder.loadTexts:agentPethPoeMainPsePower.setUnits(_I)
class _AgentPethPoeMainPseOperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('on',1),('off',2),('faulty',3)))
_AgentPethPoeMainPseOperStatus_Type.__name__=_C
_AgentPethPoeMainPseOperStatus_Object=MibTableColumn
agentPethPoeMainPseOperStatus=_AgentPethPoeMainPseOperStatus_Object((1,3,6,1,4,1,4526,10,15,1,4,1,1,4),_AgentPethPoeMainPseOperStatus_Type())
agentPethPoeMainPseOperStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:agentPethPoeMainPseOperStatus.setStatus(_A)
_AgentPethPoeMainPseThresholdPower_Type=Gauge32
_AgentPethPoeMainPseThresholdPower_Object=MibTableColumn
agentPethPoeMainPseThresholdPower=_AgentPethPoeMainPseThresholdPower_Object((1,3,6,1,4,1,4526,10,15,1,4,1,1,5),_AgentPethPoeMainPseThresholdPower_Type())
agentPethPoeMainPseThresholdPower.setMaxAccess(_B)
if mibBuilder.loadTexts:agentPethPoeMainPseThresholdPower.setStatus(_Q)
if mibBuilder.loadTexts:agentPethPoeMainPseThresholdPower.setUnits(_I)
_AgentPethPoeMainPseConsumptionPower_Type=Gauge32
_AgentPethPoeMainPseConsumptionPower_Object=MibTableColumn
agentPethPoeMainPseConsumptionPower=_AgentPethPoeMainPseConsumptionPower_Object((1,3,6,1,4,1,4526,10,15,1,4,1,1,6),_AgentPethPoeMainPseConsumptionPower_Type())
agentPethPoeMainPseConsumptionPower.setMaxAccess(_B)
if mibBuilder.loadTexts:agentPethPoeMainPseConsumptionPower.setStatus(_A)
if mibBuilder.loadTexts:agentPethPoeMainPseConsumptionPower.setUnits(_G)
class _AgentPethPoeMainPseUsageThreshold_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,99))
_AgentPethPoeMainPseUsageThreshold_Type.__name__=_C
_AgentPethPoeMainPseUsageThreshold_Object=MibTableColumn
agentPethPoeMainPseUsageThreshold=_AgentPethPoeMainPseUsageThreshold_Object((1,3,6,1,4,1,4526,10,15,1,4,1,1,7),_AgentPethPoeMainPseUsageThreshold_Type())
agentPethPoeMainPseUsageThreshold.setMaxAccess(_D)
if mibBuilder.loadTexts:agentPethPoeMainPseUsageThreshold.setStatus(_Q)
if mibBuilder.loadTexts:agentPethPoeMainPseUsageThreshold.setUnits('%')
class _AgentPethPoeMainPseFWImageVersion_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(256,256));fixedLength=256
_AgentPethPoeMainPseFWImageVersion_Type.__name__=_J
_AgentPethPoeMainPseFWImageVersion_Object=MibTableColumn
agentPethPoeMainPseFWImageVersion=_AgentPethPoeMainPseFWImageVersion_Object((1,3,6,1,4,1,4526,10,15,1,4,1,1,8),_AgentPethPoeMainPseFWImageVersion_Type())
agentPethPoeMainPseFWImageVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:agentPethPoeMainPseFWImageVersion.setStatus(_A)
class _AgentPethPoePsePowerManagementMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_E,0),(_L,1),(_M,2)))
_AgentPethPoePsePowerManagementMode_Type.__name__=_C
_AgentPethPoePsePowerManagementMode_Object=MibTableColumn
agentPethPoePsePowerManagementMode=_AgentPethPoePsePowerManagementMode_Object((1,3,6,1,4,1,4526,10,15,1,4,1,1,9),_AgentPethPoePsePowerManagementMode_Type())
agentPethPoePsePowerManagementMode.setMaxAccess(_D)
if mibBuilder.loadTexts:agentPethPoePsePowerManagementMode.setStatus(_A)
class _AgentPethPoePseCardModel_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_AgentPethPoePseCardModel_Type.__name__=_H
_AgentPethPoePseCardModel_Object=MibTableColumn
agentPethPoePseCardModel=_AgentPethPoePseCardModel_Object((1,3,6,1,4,1,4526,10,15,1,4,1,1,10),_AgentPethPoePseCardModel_Type())
agentPethPoePseCardModel.setMaxAccess(_B)
if mibBuilder.loadTexts:agentPethPoePseCardModel.setStatus(_A)
class _AgentPethPoePseCardHost_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_AgentPethPoePseCardHost_Type.__name__=_H
_AgentPethPoePseCardHost_Object=MibTableColumn
agentPethPoePseCardHost=_AgentPethPoePseCardHost_Object((1,3,6,1,4,1,4526,10,15,1,4,1,1,11),_AgentPethPoePseCardHost_Type())
agentPethPoePseCardHost.setMaxAccess(_B)
if mibBuilder.loadTexts:agentPethPoePseCardHost.setStatus(_A)
class _AgentPethPoePseCardStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('absent-or-failed',0),('running',1)))
_AgentPethPoePseCardStatus_Type.__name__=_C
_AgentPethPoePseCardStatus_Object=MibTableColumn
agentPethPoePseCardStatus=_AgentPethPoePseCardStatus_Object((1,3,6,1,4,1,4526,10,15,1,4,1,1,12),_AgentPethPoePseCardStatus_Type())
agentPethPoePseCardStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:agentPethPoePseCardStatus.setStatus(_A)
pethPsePortEntry.registerAugmentions((_F,_R))
agentPethPsePortEntry.setIndexNames(*pethPsePortEntry.getIndexNames())
pethMainPseEntry.registerAugmentions((_F,_S))
agentPethMainPseEntry.setIndexNames(*pethMainPseEntry.getIndexNames())
pethMainPseEntry.registerAugmentions((_F,_T))
agentPethPseEntry.setIndexNames(*pethMainPseEntry.getIndexNames())
mibBuilder.exportSymbols(_F,**{'fastPathpowerEthernetMIB':fastPathpowerEthernetMIB,'agentPethObjects':agentPethObjects,'agentPethPsePortTable':agentPethPsePortTable,_R:agentPethPsePortEntry,'agentPethPowerLimit':agentPethPowerLimit,'agentPethOutputPower':agentPethOutputPower,'agentPethOutputCurrent':agentPethOutputCurrent,'agentPethOutputVolts':agentPethOutputVolts,'agentPethTemperature':agentPethTemperature,'agentPethPowerLimitType':agentPethPowerLimitType,'agentPethHighPowerEnable':agentPethHighPowerEnable,'agentPethPowerDetectionType':agentPethPowerDetectionType,'agentPethFaultStatus':agentPethFaultStatus,'agentPethPortReset':agentPethPortReset,'agentPethPowerLimitMin':agentPethPowerLimitMin,'agentPethPowerLimitMax':agentPethPowerLimitMax,'agentPethMainPseObjects':agentPethMainPseObjects,'agentPethMainPseTable':agentPethMainPseTable,_S:agentPethMainPseEntry,'agentPethMainPseLegacy':agentPethMainPseLegacy,'agentPethPseTable':agentPethPseTable,_T:agentPethPseEntry,'agentPethPsePowerManagementMode':agentPethPsePowerManagementMode,'agentPethPseThresholdPower':agentPethPseThresholdPower,'agentPethPoeMainPseObjects':agentPethPoeMainPseObjects,'agentPethPoeMainPseTable':agentPethPoeMainPseTable,'agentPethPoeMainPseEntry':agentPethPoeMainPseEntry,_N:agentPethPoeMainPseGroupIndex,_O:agentPethPoeMainPseSlotIndex,'agentPethPoeMainPsePower':agentPethPoeMainPsePower,'agentPethPoeMainPseOperStatus':agentPethPoeMainPseOperStatus,'agentPethPoeMainPseThresholdPower':agentPethPoeMainPseThresholdPower,'agentPethPoeMainPseConsumptionPower':agentPethPoeMainPseConsumptionPower,'agentPethPoeMainPseUsageThreshold':agentPethPoeMainPseUsageThreshold,'agentPethPoeMainPseFWImageVersion':agentPethPoeMainPseFWImageVersion,'agentPethPoePsePowerManagementMode':agentPethPoePsePowerManagementMode,'agentPethPoePseCardModel':agentPethPoePseCardModel,'agentPethPoePseCardHost':agentPethPoePseCardHost,'agentPethPoePseCardStatus':agentPethPoePseCardStatus})