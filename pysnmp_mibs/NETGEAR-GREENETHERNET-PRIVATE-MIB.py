_N='agentGreenUnitIndex'
_M='agentGreenEeeLpiHistoryIntfSampleIndex'
_L='agentGreenEeeLpiHistoryIntfIndex'
_K='not-applicable'
_J='enable'
_I='disable'
_H='agentEthernetIntfIndex'
_G='not-accessible'
_F='DisplayString'
_E='NETGEAR-GREENETHERNET-PRIVATE-MIB'
_D='read-write'
_C='read-only'
_B='Integer32'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
InterfaceIndexOrZero,=mibBuilder.importSymbols('IF-MIB','InterfaceIndexOrZero')
ng7000managedswitch,=mibBuilder.importSymbols('NETGEAR-REF-MIB','ng7000managedswitch')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_B,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_F,'PhysAddress','TextualConvention')
fastPathGreenEthernet=ModuleIdentity((1,3,6,1,4,1,4526,10,55))
if mibBuilder.loadTexts:fastPathGreenEthernet.setRevisions(('2011-01-26 00:00',))
_AgentGreenEthernet_ObjectIdentity=ObjectIdentity
agentGreenEthernet=_AgentGreenEthernet_ObjectIdentity((1,3,6,1,4,1,4526,10,55,1))
_AgentGreenEthernetTable_Object=MibTable
agentGreenEthernetTable=_AgentGreenEthernetTable_Object((1,3,6,1,4,1,4526,10,55,1,1))
if mibBuilder.loadTexts:agentGreenEthernetTable.setStatus(_A)
_AgentGreenEthernetEntry_Object=MibTableRow
agentGreenEthernetEntry=_AgentGreenEthernetEntry_Object((1,3,6,1,4,1,4526,10,55,1,1,1))
agentGreenEthernetEntry.setIndexNames((0,_E,_H))
if mibBuilder.loadTexts:agentGreenEthernetEntry.setStatus(_A)
class _AgentEthernetIntfIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4096))
_AgentEthernetIntfIndex_Type.__name__=_B
_AgentEthernetIntfIndex_Object=MibTableColumn
agentEthernetIntfIndex=_AgentEthernetIntfIndex_Object((1,3,6,1,4,1,4526,10,55,1,1,1,1),_AgentEthernetIntfIndex_Type())
agentEthernetIntfIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:agentEthernetIntfIndex.setStatus(_A)
class _AgentGreenEnergyDetectMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_I,0),(_J,1),(_K,2)))
_AgentGreenEnergyDetectMode_Type.__name__=_B
_AgentGreenEnergyDetectMode_Object=MibTableColumn
agentGreenEnergyDetectMode=_AgentGreenEnergyDetectMode_Object((1,3,6,1,4,1,4526,10,55,1,1,1,2),_AgentGreenEnergyDetectMode_Type())
agentGreenEnergyDetectMode.setMaxAccess(_D)
if mibBuilder.loadTexts:agentGreenEnergyDetectMode.setStatus(_A)
class _AgentGreenEnergyDetectOperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('in-active',0),('active',1)))
_AgentGreenEnergyDetectOperStatus_Type.__name__=_B
_AgentGreenEnergyDetectOperStatus_Object=MibTableColumn
agentGreenEnergyDetectOperStatus=_AgentGreenEnergyDetectOperStatus_Object((1,3,6,1,4,1,4526,10,55,1,1,1,3),_AgentGreenEnergyDetectOperStatus_Type())
agentGreenEnergyDetectOperStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:agentGreenEnergyDetectOperStatus.setStatus(_A)
class _AgentGreenEnergyDetectOperReason_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_AgentGreenEnergyDetectOperReason_Type.__name__=_F
_AgentGreenEnergyDetectOperReason_Object=MibTableColumn
agentGreenEnergyDetectOperReason=_AgentGreenEnergyDetectOperReason_Object((1,3,6,1,4,1,4526,10,55,1,1,1,4),_AgentGreenEnergyDetectOperReason_Type())
agentGreenEnergyDetectOperReason.setMaxAccess(_C)
if mibBuilder.loadTexts:agentGreenEnergyDetectOperReason.setStatus(_A)
class _AgentGreenEeeMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_I,0),(_J,1),(_K,2)))
_AgentGreenEeeMode_Type.__name__=_B
_AgentGreenEeeMode_Object=MibTableColumn
agentGreenEeeMode=_AgentGreenEeeMode_Object((1,3,6,1,4,1,4526,10,55,1,1,1,9),_AgentGreenEeeMode_Type())
agentGreenEeeMode.setMaxAccess(_D)
if mibBuilder.loadTexts:agentGreenEeeMode.setStatus(_A)
class _AgentGreenEeeTxWakeTime_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(8,65535))
_AgentGreenEeeTxWakeTime_Type.__name__=_B
_AgentGreenEeeTxWakeTime_Object=MibTableColumn
agentGreenEeeTxWakeTime=_AgentGreenEeeTxWakeTime_Object((1,3,6,1,4,1,4526,10,55,1,1,1,10),_AgentGreenEeeTxWakeTime_Type())
agentGreenEeeTxWakeTime.setMaxAccess(_D)
if mibBuilder.loadTexts:agentGreenEeeTxWakeTime.setStatus(_A)
_AgentGreenEeeTxIdleTime_Type=Unsigned32
_AgentGreenEeeTxIdleTime_Object=MibTableColumn
agentGreenEeeTxIdleTime=_AgentGreenEeeTxIdleTime_Object((1,3,6,1,4,1,4526,10,55,1,1,1,11),_AgentGreenEeeTxIdleTime_Type())
agentGreenEeeTxIdleTime.setMaxAccess(_D)
if mibBuilder.loadTexts:agentGreenEeeTxIdleTime.setStatus(_A)
_AgentGreenCumEnergySaving_Type=Integer32
_AgentGreenCumEnergySaving_Object=MibTableColumn
agentGreenCumEnergySaving=_AgentGreenCumEnergySaving_Object((1,3,6,1,4,1,4526,10,55,1,1,1,12),_AgentGreenCumEnergySaving_Type())
agentGreenCumEnergySaving.setMaxAccess(_C)
if mibBuilder.loadTexts:agentGreenCumEnergySaving.setStatus(_A)
_AgentGreenIntfEeeLpiHistoryTable_Object=MibTable
agentGreenIntfEeeLpiHistoryTable=_AgentGreenIntfEeeLpiHistoryTable_Object((1,3,6,1,4,1,4526,10,55,1,2))
if mibBuilder.loadTexts:agentGreenIntfEeeLpiHistoryTable.setStatus(_A)
_AgentGreenIntfEeeLpiHistoryEntry_Object=MibTableRow
agentGreenIntfEeeLpiHistoryEntry=_AgentGreenIntfEeeLpiHistoryEntry_Object((1,3,6,1,4,1,4526,10,55,1,2,1))
agentGreenIntfEeeLpiHistoryEntry.setIndexNames((0,_E,_L),(0,_E,_M))
if mibBuilder.loadTexts:agentGreenIntfEeeLpiHistoryEntry.setStatus(_A)
class _AgentGreenEeeLpiHistoryIntfIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4096))
_AgentGreenEeeLpiHistoryIntfIndex_Type.__name__=_B
_AgentGreenEeeLpiHistoryIntfIndex_Object=MibTableColumn
agentGreenEeeLpiHistoryIntfIndex=_AgentGreenEeeLpiHistoryIntfIndex_Object((1,3,6,1,4,1,4526,10,55,1,2,1,1),_AgentGreenEeeLpiHistoryIntfIndex_Type())
agentGreenEeeLpiHistoryIntfIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:agentGreenEeeLpiHistoryIntfIndex.setStatus(_A)
class _AgentGreenEeeLpiHistoryIntfSampleIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_AgentGreenEeeLpiHistoryIntfSampleIndex_Type.__name__=_B
_AgentGreenEeeLpiHistoryIntfSampleIndex_Object=MibTableColumn
agentGreenEeeLpiHistoryIntfSampleIndex=_AgentGreenEeeLpiHistoryIntfSampleIndex_Object((1,3,6,1,4,1,4526,10,55,1,2,1,2),_AgentGreenEeeLpiHistoryIntfSampleIndex_Type())
agentGreenEeeLpiHistoryIntfSampleIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:agentGreenEeeLpiHistoryIntfSampleIndex.setStatus(_A)
class _AgentGreenEeeLpiHistoryIntfSampleTime_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_AgentGreenEeeLpiHistoryIntfSampleTime_Type.__name__=_F
_AgentGreenEeeLpiHistoryIntfSampleTime_Object=MibTableColumn
agentGreenEeeLpiHistoryIntfSampleTime=_AgentGreenEeeLpiHistoryIntfSampleTime_Object((1,3,6,1,4,1,4526,10,55,1,2,1,3),_AgentGreenEeeLpiHistoryIntfSampleTime_Type())
agentGreenEeeLpiHistoryIntfSampleTime.setMaxAccess(_C)
if mibBuilder.loadTexts:agentGreenEeeLpiHistoryIntfSampleTime.setStatus(_A)
_AgentGreenEeeLpiHistoryIntfPercentLpiTime_Type=Integer32
_AgentGreenEeeLpiHistoryIntfPercentLpiTime_Object=MibTableColumn
agentGreenEeeLpiHistoryIntfPercentLpiTime=_AgentGreenEeeLpiHistoryIntfPercentLpiTime_Object((1,3,6,1,4,1,4526,10,55,1,2,1,4),_AgentGreenEeeLpiHistoryIntfPercentLpiTime_Type())
agentGreenEeeLpiHistoryIntfPercentLpiTime.setMaxAccess(_C)
if mibBuilder.loadTexts:agentGreenEeeLpiHistoryIntfPercentLpiTime.setStatus(_A)
_AgentGreenEeeLpiHistoryIntfPercentLpiTimeTotal_Type=Integer32
_AgentGreenEeeLpiHistoryIntfPercentLpiTimeTotal_Object=MibTableColumn
agentGreenEeeLpiHistoryIntfPercentLpiTimeTotal=_AgentGreenEeeLpiHistoryIntfPercentLpiTimeTotal_Object((1,3,6,1,4,1,4526,10,55,1,2,1,5),_AgentGreenEeeLpiHistoryIntfPercentLpiTimeTotal_Type())
agentGreenEeeLpiHistoryIntfPercentLpiTimeTotal.setMaxAccess(_C)
if mibBuilder.loadTexts:agentGreenEeeLpiHistoryIntfPercentLpiTimeTotal.setStatus(_A)
_AgentGreenUnitFeatureTable_Object=MibTable
agentGreenUnitFeatureTable=_AgentGreenUnitFeatureTable_Object((1,3,6,1,4,1,4526,10,55,1,3))
if mibBuilder.loadTexts:agentGreenUnitFeatureTable.setStatus(_A)
_AgentGreenUnitFeatureEntry_Object=MibTableRow
agentGreenUnitFeatureEntry=_AgentGreenUnitFeatureEntry_Object((1,3,6,1,4,1,4526,10,55,1,3,1))
agentGreenUnitFeatureEntry.setIndexNames((0,_E,_N))
if mibBuilder.loadTexts:agentGreenUnitFeatureEntry.setStatus(_A)
class _AgentGreenUnitIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,8))
_AgentGreenUnitIndex_Type.__name__=_B
_AgentGreenUnitIndex_Object=MibTableColumn
agentGreenUnitIndex=_AgentGreenUnitIndex_Object((1,3,6,1,4,1,4526,10,55,1,3,1,1),_AgentGreenUnitIndex_Type())
agentGreenUnitIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:agentGreenUnitIndex.setStatus(_A)
class _AgentGreenFeatureList_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,128))
_AgentGreenFeatureList_Type.__name__=_F
_AgentGreenFeatureList_Object=MibTableColumn
agentGreenFeatureList=_AgentGreenFeatureList_Object((1,3,6,1,4,1,4526,10,55,1,3,1,2),_AgentGreenFeatureList_Type())
agentGreenFeatureList.setMaxAccess(_C)
if mibBuilder.loadTexts:agentGreenFeatureList.setStatus(_A)
class _AgentGreenEeeLpiHistoryIntfSampleInterval_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(30,36000))
_AgentGreenEeeLpiHistoryIntfSampleInterval_Type.__name__=_B
_AgentGreenEeeLpiHistoryIntfSampleInterval_Object=MibScalar
agentGreenEeeLpiHistoryIntfSampleInterval=_AgentGreenEeeLpiHistoryIntfSampleInterval_Object((1,3,6,1,4,1,4526,10,55,1,4),_AgentGreenEeeLpiHistoryIntfSampleInterval_Type())
agentGreenEeeLpiHistoryIntfSampleInterval.setMaxAccess(_D)
if mibBuilder.loadTexts:agentGreenEeeLpiHistoryIntfSampleInterval.setStatus(_A)
class _AgentGreenEeeLpiHistoryIntfMaxSamples_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,168))
_AgentGreenEeeLpiHistoryIntfMaxSamples_Type.__name__=_B
_AgentGreenEeeLpiHistoryIntfMaxSamples_Object=MibScalar
agentGreenEeeLpiHistoryIntfMaxSamples=_AgentGreenEeeLpiHistoryIntfMaxSamples_Object((1,3,6,1,4,1,4526,10,55,1,5),_AgentGreenEeeLpiHistoryIntfMaxSamples_Type())
agentGreenEeeLpiHistoryIntfMaxSamples.setMaxAccess(_D)
if mibBuilder.loadTexts:agentGreenEeeLpiHistoryIntfMaxSamples.setStatus(_A)
class _AgentGreenEeeLpiHistoryLpiTimePerStack_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,100))
_AgentGreenEeeLpiHistoryLpiTimePerStack_Type.__name__=_B
_AgentGreenEeeLpiHistoryLpiTimePerStack_Object=MibScalar
agentGreenEeeLpiHistoryLpiTimePerStack=_AgentGreenEeeLpiHistoryLpiTimePerStack_Object((1,3,6,1,4,1,4526,10,55,1,6),_AgentGreenEeeLpiHistoryLpiTimePerStack_Type())
agentGreenEeeLpiHistoryLpiTimePerStack.setMaxAccess(_C)
if mibBuilder.loadTexts:agentGreenEeeLpiHistoryLpiTimePerStack.setStatus(_A)
_AgentGreenStackCumEnergySaving_Type=Integer32
_AgentGreenStackCumEnergySaving_Object=MibScalar
agentGreenStackCumEnergySaving=_AgentGreenStackCumEnergySaving_Object((1,3,6,1,4,1,4526,10,55,1,7),_AgentGreenStackCumEnergySaving_Type())
agentGreenStackCumEnergySaving.setMaxAccess(_C)
if mibBuilder.loadTexts:agentGreenStackCumEnergySaving.setStatus(_A)
_AgentGreenStackCurPowerConsumption_Type=Integer32
_AgentGreenStackCurPowerConsumption_Object=MibScalar
agentGreenStackCurPowerConsumption=_AgentGreenStackCurPowerConsumption_Object((1,3,6,1,4,1,4526,10,55,1,8),_AgentGreenStackCurPowerConsumption_Type())
agentGreenStackCurPowerConsumption.setMaxAccess(_C)
if mibBuilder.loadTexts:agentGreenStackCurPowerConsumption.setStatus(_A)
_AgentGreenStackPowerSaving_Type=Integer32
_AgentGreenStackPowerSaving_Object=MibScalar
agentGreenStackPowerSaving=_AgentGreenStackPowerSaving_Object((1,3,6,1,4,1,4526,10,55,1,9),_AgentGreenStackPowerSaving_Type())
agentGreenStackPowerSaving.setMaxAccess(_C)
if mibBuilder.loadTexts:agentGreenStackPowerSaving.setStatus(_A)
mibBuilder.exportSymbols(_E,**{'fastPathGreenEthernet':fastPathGreenEthernet,'agentGreenEthernet':agentGreenEthernet,'agentGreenEthernetTable':agentGreenEthernetTable,'agentGreenEthernetEntry':agentGreenEthernetEntry,_H:agentEthernetIntfIndex,'agentGreenEnergyDetectMode':agentGreenEnergyDetectMode,'agentGreenEnergyDetectOperStatus':agentGreenEnergyDetectOperStatus,'agentGreenEnergyDetectOperReason':agentGreenEnergyDetectOperReason,'agentGreenEeeMode':agentGreenEeeMode,'agentGreenEeeTxWakeTime':agentGreenEeeTxWakeTime,'agentGreenEeeTxIdleTime':agentGreenEeeTxIdleTime,'agentGreenCumEnergySaving':agentGreenCumEnergySaving,'agentGreenIntfEeeLpiHistoryTable':agentGreenIntfEeeLpiHistoryTable,'agentGreenIntfEeeLpiHistoryEntry':agentGreenIntfEeeLpiHistoryEntry,_L:agentGreenEeeLpiHistoryIntfIndex,_M:agentGreenEeeLpiHistoryIntfSampleIndex,'agentGreenEeeLpiHistoryIntfSampleTime':agentGreenEeeLpiHistoryIntfSampleTime,'agentGreenEeeLpiHistoryIntfPercentLpiTime':agentGreenEeeLpiHistoryIntfPercentLpiTime,'agentGreenEeeLpiHistoryIntfPercentLpiTimeTotal':agentGreenEeeLpiHistoryIntfPercentLpiTimeTotal,'agentGreenUnitFeatureTable':agentGreenUnitFeatureTable,'agentGreenUnitFeatureEntry':agentGreenUnitFeatureEntry,_N:agentGreenUnitIndex,'agentGreenFeatureList':agentGreenFeatureList,'agentGreenEeeLpiHistoryIntfSampleInterval':agentGreenEeeLpiHistoryIntfSampleInterval,'agentGreenEeeLpiHistoryIntfMaxSamples':agentGreenEeeLpiHistoryIntfMaxSamples,'agentGreenEeeLpiHistoryLpiTimePerStack':agentGreenEeeLpiHistoryLpiTimePerStack,'agentGreenStackCumEnergySaving':agentGreenStackCumEnergySaving,'agentGreenStackCurPowerConsumption':agentGreenStackCurPowerConsumption,'agentGreenStackPowerSaving':agentGreenStackPowerSaving})