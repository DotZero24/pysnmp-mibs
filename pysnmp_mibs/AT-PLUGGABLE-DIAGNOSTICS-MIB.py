_U='atPluggableDiagRxLosChannel'
_T='atPluggableDiagRxLosIfIndex'
_S='atPluggableDiagRxPowerChannel'
_R='atPluggableDiagRxPowerIfIndex'
_Q='atPluggableDiagTxPowerChannel'
_P='atPluggableDiagTxPowerIfIndex'
_O='atPluggableDiagTxBiasChannel'
_N='atPluggableDiagTxBiasIfIndex'
_M='atPluggableDiagVccChannel'
_L='atPluggableDiagVccIfIndex'
_K='atPluggableDiagTempChannel'
_J='atPluggableDiagTempIfIndex'
_I='0.001 mA'
_H='0.0001 volts'
_G='0.001 degree C'
_F='Integer32'
_E='0.0001 mW'
_D='not-accessible'
_C='AT-PLUGGABLE-DIAGNOSTICS-MIB'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
DisplayStringUnsized,=mibBuilder.importSymbols('AT-SMI-MIB','DisplayStringUnsized')
sysinfo,=mibBuilder.importSymbols('AT-SYSINFO-MIB','sysinfo')
InterfaceIndex,=mibBuilder.importSymbols('IF-MIB','InterfaceIndex')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_F,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
atPluggableDiag=ModuleIdentity((1,3,6,1,4,1,207,8,4,4,3,28))
if mibBuilder.loadTexts:atPluggableDiag.setRevisions(('2015-07-17 00:00',))
_AtPluggableDiagTable_ObjectIdentity=ObjectIdentity
atPluggableDiagTable=_AtPluggableDiagTable_ObjectIdentity((1,3,6,1,4,1,207,8,4,4,3,28,1))
_AtPluggableDiagTempTable_Object=MibTable
atPluggableDiagTempTable=_AtPluggableDiagTempTable_Object((1,3,6,1,4,1,207,8,4,4,3,28,1,1))
if mibBuilder.loadTexts:atPluggableDiagTempTable.setStatus(_A)
_AtPluggableDiagTempEntry_Object=MibTableRow
atPluggableDiagTempEntry=_AtPluggableDiagTempEntry_Object((1,3,6,1,4,1,207,8,4,4,3,28,1,1,1))
atPluggableDiagTempEntry.setIndexNames((0,_C,_J),(0,_C,_K))
if mibBuilder.loadTexts:atPluggableDiagTempEntry.setStatus(_A)
_AtPluggableDiagTempIfIndex_Type=InterfaceIndex
_AtPluggableDiagTempIfIndex_Object=MibTableColumn
atPluggableDiagTempIfIndex=_AtPluggableDiagTempIfIndex_Object((1,3,6,1,4,1,207,8,4,4,3,28,1,1,1,1),_AtPluggableDiagTempIfIndex_Type())
atPluggableDiagTempIfIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:atPluggableDiagTempIfIndex.setStatus(_A)
class _AtPluggableDiagTempChannel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,16))
_AtPluggableDiagTempChannel_Type.__name__=_F
_AtPluggableDiagTempChannel_Object=MibTableColumn
atPluggableDiagTempChannel=_AtPluggableDiagTempChannel_Object((1,3,6,1,4,1,207,8,4,4,3,28,1,1,1,2),_AtPluggableDiagTempChannel_Type())
atPluggableDiagTempChannel.setMaxAccess(_D)
if mibBuilder.loadTexts:atPluggableDiagTempChannel.setStatus(_A)
_AtPluggableDiagTempStatusReading_Type=Integer32
_AtPluggableDiagTempStatusReading_Object=MibTableColumn
atPluggableDiagTempStatusReading=_AtPluggableDiagTempStatusReading_Object((1,3,6,1,4,1,207,8,4,4,3,28,1,1,1,3),_AtPluggableDiagTempStatusReading_Type())
atPluggableDiagTempStatusReading.setMaxAccess(_B)
if mibBuilder.loadTexts:atPluggableDiagTempStatusReading.setStatus(_A)
if mibBuilder.loadTexts:atPluggableDiagTempStatusReading.setUnits(_G)
_AtPluggableDiagTempCurrentAlarm_Type=OctetString
_AtPluggableDiagTempCurrentAlarm_Object=MibTableColumn
atPluggableDiagTempCurrentAlarm=_AtPluggableDiagTempCurrentAlarm_Object((1,3,6,1,4,1,207,8,4,4,3,28,1,1,1,4),_AtPluggableDiagTempCurrentAlarm_Type())
atPluggableDiagTempCurrentAlarm.setMaxAccess(_B)
if mibBuilder.loadTexts:atPluggableDiagTempCurrentAlarm.setStatus(_A)
_AtPluggableDiagTempAlarmMax_Type=Integer32
_AtPluggableDiagTempAlarmMax_Object=MibTableColumn
atPluggableDiagTempAlarmMax=_AtPluggableDiagTempAlarmMax_Object((1,3,6,1,4,1,207,8,4,4,3,28,1,1,1,5),_AtPluggableDiagTempAlarmMax_Type())
atPluggableDiagTempAlarmMax.setMaxAccess(_B)
if mibBuilder.loadTexts:atPluggableDiagTempAlarmMax.setStatus(_A)
if mibBuilder.loadTexts:atPluggableDiagTempAlarmMax.setUnits(_G)
_AtPluggableDiagTempAlarmMin_Type=Integer32
_AtPluggableDiagTempAlarmMin_Object=MibTableColumn
atPluggableDiagTempAlarmMin=_AtPluggableDiagTempAlarmMin_Object((1,3,6,1,4,1,207,8,4,4,3,28,1,1,1,6),_AtPluggableDiagTempAlarmMin_Type())
atPluggableDiagTempAlarmMin.setMaxAccess(_B)
if mibBuilder.loadTexts:atPluggableDiagTempAlarmMin.setStatus(_A)
if mibBuilder.loadTexts:atPluggableDiagTempAlarmMin.setUnits(_G)
_AtPluggableDiagTempCurrentWarning_Type=OctetString
_AtPluggableDiagTempCurrentWarning_Object=MibTableColumn
atPluggableDiagTempCurrentWarning=_AtPluggableDiagTempCurrentWarning_Object((1,3,6,1,4,1,207,8,4,4,3,28,1,1,1,7),_AtPluggableDiagTempCurrentWarning_Type())
atPluggableDiagTempCurrentWarning.setMaxAccess(_B)
if mibBuilder.loadTexts:atPluggableDiagTempCurrentWarning.setStatus(_A)
_AtPluggableDiagTempWarningMax_Type=Integer32
_AtPluggableDiagTempWarningMax_Object=MibTableColumn
atPluggableDiagTempWarningMax=_AtPluggableDiagTempWarningMax_Object((1,3,6,1,4,1,207,8,4,4,3,28,1,1,1,8),_AtPluggableDiagTempWarningMax_Type())
atPluggableDiagTempWarningMax.setMaxAccess(_B)
if mibBuilder.loadTexts:atPluggableDiagTempWarningMax.setStatus(_A)
if mibBuilder.loadTexts:atPluggableDiagTempWarningMax.setUnits(_G)
_AtPluggableDiagTempWarningMin_Type=Integer32
_AtPluggableDiagTempWarningMin_Object=MibTableColumn
atPluggableDiagTempWarningMin=_AtPluggableDiagTempWarningMin_Object((1,3,6,1,4,1,207,8,4,4,3,28,1,1,1,9),_AtPluggableDiagTempWarningMin_Type())
atPluggableDiagTempWarningMin.setMaxAccess(_B)
if mibBuilder.loadTexts:atPluggableDiagTempWarningMin.setStatus(_A)
if mibBuilder.loadTexts:atPluggableDiagTempWarningMin.setUnits(_G)
_AtPluggableDiagVccTable_Object=MibTable
atPluggableDiagVccTable=_AtPluggableDiagVccTable_Object((1,3,6,1,4,1,207,8,4,4,3,28,1,2))
if mibBuilder.loadTexts:atPluggableDiagVccTable.setStatus(_A)
_AtPluggableDiagVccEntry_Object=MibTableRow
atPluggableDiagVccEntry=_AtPluggableDiagVccEntry_Object((1,3,6,1,4,1,207,8,4,4,3,28,1,2,1))
atPluggableDiagVccEntry.setIndexNames((0,_C,_L),(0,_C,_M))
if mibBuilder.loadTexts:atPluggableDiagVccEntry.setStatus(_A)
_AtPluggableDiagVccIfIndex_Type=InterfaceIndex
_AtPluggableDiagVccIfIndex_Object=MibTableColumn
atPluggableDiagVccIfIndex=_AtPluggableDiagVccIfIndex_Object((1,3,6,1,4,1,207,8,4,4,3,28,1,2,1,1),_AtPluggableDiagVccIfIndex_Type())
atPluggableDiagVccIfIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:atPluggableDiagVccIfIndex.setStatus(_A)
class _AtPluggableDiagVccChannel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,16))
_AtPluggableDiagVccChannel_Type.__name__=_F
_AtPluggableDiagVccChannel_Object=MibTableColumn
atPluggableDiagVccChannel=_AtPluggableDiagVccChannel_Object((1,3,6,1,4,1,207,8,4,4,3,28,1,2,1,2),_AtPluggableDiagVccChannel_Type())
atPluggableDiagVccChannel.setMaxAccess(_D)
if mibBuilder.loadTexts:atPluggableDiagVccChannel.setStatus(_A)
_AtPluggableDiagVccStatusReading_Type=Integer32
_AtPluggableDiagVccStatusReading_Object=MibTableColumn
atPluggableDiagVccStatusReading=_AtPluggableDiagVccStatusReading_Object((1,3,6,1,4,1,207,8,4,4,3,28,1,2,1,3),_AtPluggableDiagVccStatusReading_Type())
atPluggableDiagVccStatusReading.setMaxAccess(_B)
if mibBuilder.loadTexts:atPluggableDiagVccStatusReading.setStatus(_A)
if mibBuilder.loadTexts:atPluggableDiagVccStatusReading.setUnits(_H)
_AtPluggableDiagVccCurrentAlarm_Type=OctetString
_AtPluggableDiagVccCurrentAlarm_Object=MibTableColumn
atPluggableDiagVccCurrentAlarm=_AtPluggableDiagVccCurrentAlarm_Object((1,3,6,1,4,1,207,8,4,4,3,28,1,2,1,4),_AtPluggableDiagVccCurrentAlarm_Type())
atPluggableDiagVccCurrentAlarm.setMaxAccess(_B)
if mibBuilder.loadTexts:atPluggableDiagVccCurrentAlarm.setStatus(_A)
_AtPluggableDiagVccAlarmMax_Type=Integer32
_AtPluggableDiagVccAlarmMax_Object=MibTableColumn
atPluggableDiagVccAlarmMax=_AtPluggableDiagVccAlarmMax_Object((1,3,6,1,4,1,207,8,4,4,3,28,1,2,1,5),_AtPluggableDiagVccAlarmMax_Type())
atPluggableDiagVccAlarmMax.setMaxAccess(_B)
if mibBuilder.loadTexts:atPluggableDiagVccAlarmMax.setStatus(_A)
if mibBuilder.loadTexts:atPluggableDiagVccAlarmMax.setUnits(_H)
_AtPluggableDiagVccAlarmMin_Type=Integer32
_AtPluggableDiagVccAlarmMin_Object=MibTableColumn
atPluggableDiagVccAlarmMin=_AtPluggableDiagVccAlarmMin_Object((1,3,6,1,4,1,207,8,4,4,3,28,1,2,1,6),_AtPluggableDiagVccAlarmMin_Type())
atPluggableDiagVccAlarmMin.setMaxAccess(_B)
if mibBuilder.loadTexts:atPluggableDiagVccAlarmMin.setStatus(_A)
if mibBuilder.loadTexts:atPluggableDiagVccAlarmMin.setUnits(_H)
_AtPluggableDiagVccCurrentWarning_Type=OctetString
_AtPluggableDiagVccCurrentWarning_Object=MibTableColumn
atPluggableDiagVccCurrentWarning=_AtPluggableDiagVccCurrentWarning_Object((1,3,6,1,4,1,207,8,4,4,3,28,1,2,1,7),_AtPluggableDiagVccCurrentWarning_Type())
atPluggableDiagVccCurrentWarning.setMaxAccess(_B)
if mibBuilder.loadTexts:atPluggableDiagVccCurrentWarning.setStatus(_A)
_AtPluggableDiagVccWarningMax_Type=Integer32
_AtPluggableDiagVccWarningMax_Object=MibTableColumn
atPluggableDiagVccWarningMax=_AtPluggableDiagVccWarningMax_Object((1,3,6,1,4,1,207,8,4,4,3,28,1,2,1,8),_AtPluggableDiagVccWarningMax_Type())
atPluggableDiagVccWarningMax.setMaxAccess(_B)
if mibBuilder.loadTexts:atPluggableDiagVccWarningMax.setStatus(_A)
if mibBuilder.loadTexts:atPluggableDiagVccWarningMax.setUnits(_H)
_AtPluggableDiagVccWarningMin_Type=Integer32
_AtPluggableDiagVccWarningMin_Object=MibTableColumn
atPluggableDiagVccWarningMin=_AtPluggableDiagVccWarningMin_Object((1,3,6,1,4,1,207,8,4,4,3,28,1,2,1,9),_AtPluggableDiagVccWarningMin_Type())
atPluggableDiagVccWarningMin.setMaxAccess(_B)
if mibBuilder.loadTexts:atPluggableDiagVccWarningMin.setStatus(_A)
if mibBuilder.loadTexts:atPluggableDiagVccWarningMin.setUnits(_H)
_AtPluggableDiagTxBiasTable_Object=MibTable
atPluggableDiagTxBiasTable=_AtPluggableDiagTxBiasTable_Object((1,3,6,1,4,1,207,8,4,4,3,28,1,3))
if mibBuilder.loadTexts:atPluggableDiagTxBiasTable.setStatus(_A)
_AtPluggableDiagTxBiasEntry_Object=MibTableRow
atPluggableDiagTxBiasEntry=_AtPluggableDiagTxBiasEntry_Object((1,3,6,1,4,1,207,8,4,4,3,28,1,3,1))
atPluggableDiagTxBiasEntry.setIndexNames((0,_C,_N),(0,_C,_O))
if mibBuilder.loadTexts:atPluggableDiagTxBiasEntry.setStatus(_A)
_AtPluggableDiagTxBiasIfIndex_Type=InterfaceIndex
_AtPluggableDiagTxBiasIfIndex_Object=MibTableColumn
atPluggableDiagTxBiasIfIndex=_AtPluggableDiagTxBiasIfIndex_Object((1,3,6,1,4,1,207,8,4,4,3,28,1,3,1,1),_AtPluggableDiagTxBiasIfIndex_Type())
atPluggableDiagTxBiasIfIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:atPluggableDiagTxBiasIfIndex.setStatus(_A)
class _AtPluggableDiagTxBiasChannel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,16))
_AtPluggableDiagTxBiasChannel_Type.__name__=_F
_AtPluggableDiagTxBiasChannel_Object=MibTableColumn
atPluggableDiagTxBiasChannel=_AtPluggableDiagTxBiasChannel_Object((1,3,6,1,4,1,207,8,4,4,3,28,1,3,1,2),_AtPluggableDiagTxBiasChannel_Type())
atPluggableDiagTxBiasChannel.setMaxAccess(_D)
if mibBuilder.loadTexts:atPluggableDiagTxBiasChannel.setStatus(_A)
_AtPluggableDiagTxBiasStatusReading_Type=Integer32
_AtPluggableDiagTxBiasStatusReading_Object=MibTableColumn
atPluggableDiagTxBiasStatusReading=_AtPluggableDiagTxBiasStatusReading_Object((1,3,6,1,4,1,207,8,4,4,3,28,1,3,1,3),_AtPluggableDiagTxBiasStatusReading_Type())
atPluggableDiagTxBiasStatusReading.setMaxAccess(_B)
if mibBuilder.loadTexts:atPluggableDiagTxBiasStatusReading.setStatus(_A)
if mibBuilder.loadTexts:atPluggableDiagTxBiasStatusReading.setUnits(_I)
_AtPluggableDiagTxBiasCurrentAlarm_Type=OctetString
_AtPluggableDiagTxBiasCurrentAlarm_Object=MibTableColumn
atPluggableDiagTxBiasCurrentAlarm=_AtPluggableDiagTxBiasCurrentAlarm_Object((1,3,6,1,4,1,207,8,4,4,3,28,1,3,1,4),_AtPluggableDiagTxBiasCurrentAlarm_Type())
atPluggableDiagTxBiasCurrentAlarm.setMaxAccess(_B)
if mibBuilder.loadTexts:atPluggableDiagTxBiasCurrentAlarm.setStatus(_A)
_AtPluggableDiagTxBiasAlarmMax_Type=Integer32
_AtPluggableDiagTxBiasAlarmMax_Object=MibTableColumn
atPluggableDiagTxBiasAlarmMax=_AtPluggableDiagTxBiasAlarmMax_Object((1,3,6,1,4,1,207,8,4,4,3,28,1,3,1,5),_AtPluggableDiagTxBiasAlarmMax_Type())
atPluggableDiagTxBiasAlarmMax.setMaxAccess(_B)
if mibBuilder.loadTexts:atPluggableDiagTxBiasAlarmMax.setStatus(_A)
if mibBuilder.loadTexts:atPluggableDiagTxBiasAlarmMax.setUnits(_I)
_AtPluggableDiagTxBiasAlarmMin_Type=Integer32
_AtPluggableDiagTxBiasAlarmMin_Object=MibTableColumn
atPluggableDiagTxBiasAlarmMin=_AtPluggableDiagTxBiasAlarmMin_Object((1,3,6,1,4,1,207,8,4,4,3,28,1,3,1,6),_AtPluggableDiagTxBiasAlarmMin_Type())
atPluggableDiagTxBiasAlarmMin.setMaxAccess(_B)
if mibBuilder.loadTexts:atPluggableDiagTxBiasAlarmMin.setStatus(_A)
if mibBuilder.loadTexts:atPluggableDiagTxBiasAlarmMin.setUnits(_I)
_AtPluggableDiagTxBiasCurrentWarning_Type=OctetString
_AtPluggableDiagTxBiasCurrentWarning_Object=MibTableColumn
atPluggableDiagTxBiasCurrentWarning=_AtPluggableDiagTxBiasCurrentWarning_Object((1,3,6,1,4,1,207,8,4,4,3,28,1,3,1,7),_AtPluggableDiagTxBiasCurrentWarning_Type())
atPluggableDiagTxBiasCurrentWarning.setMaxAccess(_B)
if mibBuilder.loadTexts:atPluggableDiagTxBiasCurrentWarning.setStatus(_A)
_AtPluggableDiagTxBiasWarningMax_Type=Integer32
_AtPluggableDiagTxBiasWarningMax_Object=MibTableColumn
atPluggableDiagTxBiasWarningMax=_AtPluggableDiagTxBiasWarningMax_Object((1,3,6,1,4,1,207,8,4,4,3,28,1,3,1,8),_AtPluggableDiagTxBiasWarningMax_Type())
atPluggableDiagTxBiasWarningMax.setMaxAccess(_B)
if mibBuilder.loadTexts:atPluggableDiagTxBiasWarningMax.setStatus(_A)
if mibBuilder.loadTexts:atPluggableDiagTxBiasWarningMax.setUnits(_I)
_AtPluggableDiagTxBiasWarningMin_Type=Integer32
_AtPluggableDiagTxBiasWarningMin_Object=MibTableColumn
atPluggableDiagTxBiasWarningMin=_AtPluggableDiagTxBiasWarningMin_Object((1,3,6,1,4,1,207,8,4,4,3,28,1,3,1,9),_AtPluggableDiagTxBiasWarningMin_Type())
atPluggableDiagTxBiasWarningMin.setMaxAccess(_B)
if mibBuilder.loadTexts:atPluggableDiagTxBiasWarningMin.setStatus(_A)
if mibBuilder.loadTexts:atPluggableDiagTxBiasWarningMin.setUnits(_I)
_AtPluggableDiagTxPowerTable_Object=MibTable
atPluggableDiagTxPowerTable=_AtPluggableDiagTxPowerTable_Object((1,3,6,1,4,1,207,8,4,4,3,28,1,4))
if mibBuilder.loadTexts:atPluggableDiagTxPowerTable.setStatus(_A)
_AtPluggableDiagTxPowerEntry_Object=MibTableRow
atPluggableDiagTxPowerEntry=_AtPluggableDiagTxPowerEntry_Object((1,3,6,1,4,1,207,8,4,4,3,28,1,4,1))
atPluggableDiagTxPowerEntry.setIndexNames((0,_C,_P),(0,_C,_Q))
if mibBuilder.loadTexts:atPluggableDiagTxPowerEntry.setStatus(_A)
_AtPluggableDiagTxPowerIfIndex_Type=InterfaceIndex
_AtPluggableDiagTxPowerIfIndex_Object=MibTableColumn
atPluggableDiagTxPowerIfIndex=_AtPluggableDiagTxPowerIfIndex_Object((1,3,6,1,4,1,207,8,4,4,3,28,1,4,1,1),_AtPluggableDiagTxPowerIfIndex_Type())
atPluggableDiagTxPowerIfIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:atPluggableDiagTxPowerIfIndex.setStatus(_A)
class _AtPluggableDiagTxPowerChannel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,16))
_AtPluggableDiagTxPowerChannel_Type.__name__=_F
_AtPluggableDiagTxPowerChannel_Object=MibTableColumn
atPluggableDiagTxPowerChannel=_AtPluggableDiagTxPowerChannel_Object((1,3,6,1,4,1,207,8,4,4,3,28,1,4,1,2),_AtPluggableDiagTxPowerChannel_Type())
atPluggableDiagTxPowerChannel.setMaxAccess(_D)
if mibBuilder.loadTexts:atPluggableDiagTxPowerChannel.setStatus(_A)
_AtPluggableDiagTxPowerStatusReading_Type=Integer32
_AtPluggableDiagTxPowerStatusReading_Object=MibTableColumn
atPluggableDiagTxPowerStatusReading=_AtPluggableDiagTxPowerStatusReading_Object((1,3,6,1,4,1,207,8,4,4,3,28,1,4,1,3),_AtPluggableDiagTxPowerStatusReading_Type())
atPluggableDiagTxPowerStatusReading.setMaxAccess(_B)
if mibBuilder.loadTexts:atPluggableDiagTxPowerStatusReading.setStatus(_A)
if mibBuilder.loadTexts:atPluggableDiagTxPowerStatusReading.setUnits(_E)
_AtPluggableDiagTxPowerCurrentAlarm_Type=OctetString
_AtPluggableDiagTxPowerCurrentAlarm_Object=MibTableColumn
atPluggableDiagTxPowerCurrentAlarm=_AtPluggableDiagTxPowerCurrentAlarm_Object((1,3,6,1,4,1,207,8,4,4,3,28,1,4,1,4),_AtPluggableDiagTxPowerCurrentAlarm_Type())
atPluggableDiagTxPowerCurrentAlarm.setMaxAccess(_B)
if mibBuilder.loadTexts:atPluggableDiagTxPowerCurrentAlarm.setStatus(_A)
_AtPluggableDiagTxPowerAlarmMax_Type=Integer32
_AtPluggableDiagTxPowerAlarmMax_Object=MibTableColumn
atPluggableDiagTxPowerAlarmMax=_AtPluggableDiagTxPowerAlarmMax_Object((1,3,6,1,4,1,207,8,4,4,3,28,1,4,1,5),_AtPluggableDiagTxPowerAlarmMax_Type())
atPluggableDiagTxPowerAlarmMax.setMaxAccess(_B)
if mibBuilder.loadTexts:atPluggableDiagTxPowerAlarmMax.setStatus(_A)
if mibBuilder.loadTexts:atPluggableDiagTxPowerAlarmMax.setUnits(_E)
_AtPluggableDiagTxPowerAlarmMin_Type=Integer32
_AtPluggableDiagTxPowerAlarmMin_Object=MibTableColumn
atPluggableDiagTxPowerAlarmMin=_AtPluggableDiagTxPowerAlarmMin_Object((1,3,6,1,4,1,207,8,4,4,3,28,1,4,1,6),_AtPluggableDiagTxPowerAlarmMin_Type())
atPluggableDiagTxPowerAlarmMin.setMaxAccess(_B)
if mibBuilder.loadTexts:atPluggableDiagTxPowerAlarmMin.setStatus(_A)
if mibBuilder.loadTexts:atPluggableDiagTxPowerAlarmMin.setUnits(_E)
_AtPluggableDiagTxPowerCurrentWarning_Type=OctetString
_AtPluggableDiagTxPowerCurrentWarning_Object=MibTableColumn
atPluggableDiagTxPowerCurrentWarning=_AtPluggableDiagTxPowerCurrentWarning_Object((1,3,6,1,4,1,207,8,4,4,3,28,1,4,1,7),_AtPluggableDiagTxPowerCurrentWarning_Type())
atPluggableDiagTxPowerCurrentWarning.setMaxAccess(_B)
if mibBuilder.loadTexts:atPluggableDiagTxPowerCurrentWarning.setStatus(_A)
_AtPluggableDiagTxPowerWarningMax_Type=Integer32
_AtPluggableDiagTxPowerWarningMax_Object=MibTableColumn
atPluggableDiagTxPowerWarningMax=_AtPluggableDiagTxPowerWarningMax_Object((1,3,6,1,4,1,207,8,4,4,3,28,1,4,1,8),_AtPluggableDiagTxPowerWarningMax_Type())
atPluggableDiagTxPowerWarningMax.setMaxAccess(_B)
if mibBuilder.loadTexts:atPluggableDiagTxPowerWarningMax.setStatus(_A)
if mibBuilder.loadTexts:atPluggableDiagTxPowerWarningMax.setUnits(_E)
_AtPluggableDiagTxPowerWarningMin_Type=Integer32
_AtPluggableDiagTxPowerWarningMin_Object=MibTableColumn
atPluggableDiagTxPowerWarningMin=_AtPluggableDiagTxPowerWarningMin_Object((1,3,6,1,4,1,207,8,4,4,3,28,1,4,1,9),_AtPluggableDiagTxPowerWarningMin_Type())
atPluggableDiagTxPowerWarningMin.setMaxAccess(_B)
if mibBuilder.loadTexts:atPluggableDiagTxPowerWarningMin.setStatus(_A)
if mibBuilder.loadTexts:atPluggableDiagTxPowerWarningMin.setUnits(_E)
_AtPluggableDiagRxPowerTable_Object=MibTable
atPluggableDiagRxPowerTable=_AtPluggableDiagRxPowerTable_Object((1,3,6,1,4,1,207,8,4,4,3,28,1,5))
if mibBuilder.loadTexts:atPluggableDiagRxPowerTable.setStatus(_A)
_AtPluggableDiagRxPowerEntry_Object=MibTableRow
atPluggableDiagRxPowerEntry=_AtPluggableDiagRxPowerEntry_Object((1,3,6,1,4,1,207,8,4,4,3,28,1,5,1))
atPluggableDiagRxPowerEntry.setIndexNames((0,_C,_R),(0,_C,_S))
if mibBuilder.loadTexts:atPluggableDiagRxPowerEntry.setStatus(_A)
_AtPluggableDiagRxPowerIfIndex_Type=InterfaceIndex
_AtPluggableDiagRxPowerIfIndex_Object=MibTableColumn
atPluggableDiagRxPowerIfIndex=_AtPluggableDiagRxPowerIfIndex_Object((1,3,6,1,4,1,207,8,4,4,3,28,1,5,1,1),_AtPluggableDiagRxPowerIfIndex_Type())
atPluggableDiagRxPowerIfIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:atPluggableDiagRxPowerIfIndex.setStatus(_A)
class _AtPluggableDiagRxPowerChannel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,16))
_AtPluggableDiagRxPowerChannel_Type.__name__=_F
_AtPluggableDiagRxPowerChannel_Object=MibTableColumn
atPluggableDiagRxPowerChannel=_AtPluggableDiagRxPowerChannel_Object((1,3,6,1,4,1,207,8,4,4,3,28,1,5,1,2),_AtPluggableDiagRxPowerChannel_Type())
atPluggableDiagRxPowerChannel.setMaxAccess(_D)
if mibBuilder.loadTexts:atPluggableDiagRxPowerChannel.setStatus(_A)
_AtPluggableDiagRxPowerStatusReading_Type=Integer32
_AtPluggableDiagRxPowerStatusReading_Object=MibTableColumn
atPluggableDiagRxPowerStatusReading=_AtPluggableDiagRxPowerStatusReading_Object((1,3,6,1,4,1,207,8,4,4,3,28,1,5,1,3),_AtPluggableDiagRxPowerStatusReading_Type())
atPluggableDiagRxPowerStatusReading.setMaxAccess(_B)
if mibBuilder.loadTexts:atPluggableDiagRxPowerStatusReading.setStatus(_A)
if mibBuilder.loadTexts:atPluggableDiagRxPowerStatusReading.setUnits(_E)
_AtPluggableDiagRxPowerCurrentAlarm_Type=OctetString
_AtPluggableDiagRxPowerCurrentAlarm_Object=MibTableColumn
atPluggableDiagRxPowerCurrentAlarm=_AtPluggableDiagRxPowerCurrentAlarm_Object((1,3,6,1,4,1,207,8,4,4,3,28,1,5,1,4),_AtPluggableDiagRxPowerCurrentAlarm_Type())
atPluggableDiagRxPowerCurrentAlarm.setMaxAccess(_B)
if mibBuilder.loadTexts:atPluggableDiagRxPowerCurrentAlarm.setStatus(_A)
_AtPluggableDiagRxPowerAlarmMax_Type=Integer32
_AtPluggableDiagRxPowerAlarmMax_Object=MibTableColumn
atPluggableDiagRxPowerAlarmMax=_AtPluggableDiagRxPowerAlarmMax_Object((1,3,6,1,4,1,207,8,4,4,3,28,1,5,1,5),_AtPluggableDiagRxPowerAlarmMax_Type())
atPluggableDiagRxPowerAlarmMax.setMaxAccess(_B)
if mibBuilder.loadTexts:atPluggableDiagRxPowerAlarmMax.setStatus(_A)
if mibBuilder.loadTexts:atPluggableDiagRxPowerAlarmMax.setUnits(_E)
_AtPluggableDiagRxPowerAlarmMin_Type=Integer32
_AtPluggableDiagRxPowerAlarmMin_Object=MibTableColumn
atPluggableDiagRxPowerAlarmMin=_AtPluggableDiagRxPowerAlarmMin_Object((1,3,6,1,4,1,207,8,4,4,3,28,1,5,1,6),_AtPluggableDiagRxPowerAlarmMin_Type())
atPluggableDiagRxPowerAlarmMin.setMaxAccess(_B)
if mibBuilder.loadTexts:atPluggableDiagRxPowerAlarmMin.setStatus(_A)
if mibBuilder.loadTexts:atPluggableDiagRxPowerAlarmMin.setUnits(_E)
_AtPluggableDiagRxPowerCurrentWarning_Type=OctetString
_AtPluggableDiagRxPowerCurrentWarning_Object=MibTableColumn
atPluggableDiagRxPowerCurrentWarning=_AtPluggableDiagRxPowerCurrentWarning_Object((1,3,6,1,4,1,207,8,4,4,3,28,1,5,1,7),_AtPluggableDiagRxPowerCurrentWarning_Type())
atPluggableDiagRxPowerCurrentWarning.setMaxAccess(_B)
if mibBuilder.loadTexts:atPluggableDiagRxPowerCurrentWarning.setStatus(_A)
_AtPluggableDiagRxPowerWarningMax_Type=Integer32
_AtPluggableDiagRxPowerWarningMax_Object=MibTableColumn
atPluggableDiagRxPowerWarningMax=_AtPluggableDiagRxPowerWarningMax_Object((1,3,6,1,4,1,207,8,4,4,3,28,1,5,1,8),_AtPluggableDiagRxPowerWarningMax_Type())
atPluggableDiagRxPowerWarningMax.setMaxAccess(_B)
if mibBuilder.loadTexts:atPluggableDiagRxPowerWarningMax.setStatus(_A)
if mibBuilder.loadTexts:atPluggableDiagRxPowerWarningMax.setUnits(_E)
_AtPluggableDiagRxPowerWarningMin_Type=Integer32
_AtPluggableDiagRxPowerWarningMin_Object=MibTableColumn
atPluggableDiagRxPowerWarningMin=_AtPluggableDiagRxPowerWarningMin_Object((1,3,6,1,4,1,207,8,4,4,3,28,1,5,1,9),_AtPluggableDiagRxPowerWarningMin_Type())
atPluggableDiagRxPowerWarningMin.setMaxAccess(_B)
if mibBuilder.loadTexts:atPluggableDiagRxPowerWarningMin.setStatus(_A)
if mibBuilder.loadTexts:atPluggableDiagRxPowerWarningMin.setUnits(_E)
_AtPluggableDiagRxLosTable_Object=MibTable
atPluggableDiagRxLosTable=_AtPluggableDiagRxLosTable_Object((1,3,6,1,4,1,207,8,4,4,3,28,1,6))
if mibBuilder.loadTexts:atPluggableDiagRxLosTable.setStatus(_A)
_AtPluggableDiagRxLosEntry_Object=MibTableRow
atPluggableDiagRxLosEntry=_AtPluggableDiagRxLosEntry_Object((1,3,6,1,4,1,207,8,4,4,3,28,1,6,1))
atPluggableDiagRxLosEntry.setIndexNames((0,_C,_T),(0,_C,_U))
if mibBuilder.loadTexts:atPluggableDiagRxLosEntry.setStatus(_A)
_AtPluggableDiagRxLosIfIndex_Type=InterfaceIndex
_AtPluggableDiagRxLosIfIndex_Object=MibTableColumn
atPluggableDiagRxLosIfIndex=_AtPluggableDiagRxLosIfIndex_Object((1,3,6,1,4,1,207,8,4,4,3,28,1,6,1,1),_AtPluggableDiagRxLosIfIndex_Type())
atPluggableDiagRxLosIfIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:atPluggableDiagRxLosIfIndex.setStatus(_A)
class _AtPluggableDiagRxLosChannel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,16))
_AtPluggableDiagRxLosChannel_Type.__name__=_F
_AtPluggableDiagRxLosChannel_Object=MibTableColumn
atPluggableDiagRxLosChannel=_AtPluggableDiagRxLosChannel_Object((1,3,6,1,4,1,207,8,4,4,3,28,1,6,1,2),_AtPluggableDiagRxLosChannel_Type())
atPluggableDiagRxLosChannel.setMaxAccess(_D)
if mibBuilder.loadTexts:atPluggableDiagRxLosChannel.setStatus(_A)
_AtPluggableDiagRxLosStatusReading_Type=OctetString
_AtPluggableDiagRxLosStatusReading_Object=MibTableColumn
atPluggableDiagRxLosStatusReading=_AtPluggableDiagRxLosStatusReading_Object((1,3,6,1,4,1,207,8,4,4,3,28,1,6,1,3),_AtPluggableDiagRxLosStatusReading_Type())
atPluggableDiagRxLosStatusReading.setMaxAccess(_B)
if mibBuilder.loadTexts:atPluggableDiagRxLosStatusReading.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'atPluggableDiag':atPluggableDiag,'atPluggableDiagTable':atPluggableDiagTable,'atPluggableDiagTempTable':atPluggableDiagTempTable,'atPluggableDiagTempEntry':atPluggableDiagTempEntry,_J:atPluggableDiagTempIfIndex,_K:atPluggableDiagTempChannel,'atPluggableDiagTempStatusReading':atPluggableDiagTempStatusReading,'atPluggableDiagTempCurrentAlarm':atPluggableDiagTempCurrentAlarm,'atPluggableDiagTempAlarmMax':atPluggableDiagTempAlarmMax,'atPluggableDiagTempAlarmMin':atPluggableDiagTempAlarmMin,'atPluggableDiagTempCurrentWarning':atPluggableDiagTempCurrentWarning,'atPluggableDiagTempWarningMax':atPluggableDiagTempWarningMax,'atPluggableDiagTempWarningMin':atPluggableDiagTempWarningMin,'atPluggableDiagVccTable':atPluggableDiagVccTable,'atPluggableDiagVccEntry':atPluggableDiagVccEntry,_L:atPluggableDiagVccIfIndex,_M:atPluggableDiagVccChannel,'atPluggableDiagVccStatusReading':atPluggableDiagVccStatusReading,'atPluggableDiagVccCurrentAlarm':atPluggableDiagVccCurrentAlarm,'atPluggableDiagVccAlarmMax':atPluggableDiagVccAlarmMax,'atPluggableDiagVccAlarmMin':atPluggableDiagVccAlarmMin,'atPluggableDiagVccCurrentWarning':atPluggableDiagVccCurrentWarning,'atPluggableDiagVccWarningMax':atPluggableDiagVccWarningMax,'atPluggableDiagVccWarningMin':atPluggableDiagVccWarningMin,'atPluggableDiagTxBiasTable':atPluggableDiagTxBiasTable,'atPluggableDiagTxBiasEntry':atPluggableDiagTxBiasEntry,_N:atPluggableDiagTxBiasIfIndex,_O:atPluggableDiagTxBiasChannel,'atPluggableDiagTxBiasStatusReading':atPluggableDiagTxBiasStatusReading,'atPluggableDiagTxBiasCurrentAlarm':atPluggableDiagTxBiasCurrentAlarm,'atPluggableDiagTxBiasAlarmMax':atPluggableDiagTxBiasAlarmMax,'atPluggableDiagTxBiasAlarmMin':atPluggableDiagTxBiasAlarmMin,'atPluggableDiagTxBiasCurrentWarning':atPluggableDiagTxBiasCurrentWarning,'atPluggableDiagTxBiasWarningMax':atPluggableDiagTxBiasWarningMax,'atPluggableDiagTxBiasWarningMin':atPluggableDiagTxBiasWarningMin,'atPluggableDiagTxPowerTable':atPluggableDiagTxPowerTable,'atPluggableDiagTxPowerEntry':atPluggableDiagTxPowerEntry,_P:atPluggableDiagTxPowerIfIndex,_Q:atPluggableDiagTxPowerChannel,'atPluggableDiagTxPowerStatusReading':atPluggableDiagTxPowerStatusReading,'atPluggableDiagTxPowerCurrentAlarm':atPluggableDiagTxPowerCurrentAlarm,'atPluggableDiagTxPowerAlarmMax':atPluggableDiagTxPowerAlarmMax,'atPluggableDiagTxPowerAlarmMin':atPluggableDiagTxPowerAlarmMin,'atPluggableDiagTxPowerCurrentWarning':atPluggableDiagTxPowerCurrentWarning,'atPluggableDiagTxPowerWarningMax':atPluggableDiagTxPowerWarningMax,'atPluggableDiagTxPowerWarningMin':atPluggableDiagTxPowerWarningMin,'atPluggableDiagRxPowerTable':atPluggableDiagRxPowerTable,'atPluggableDiagRxPowerEntry':atPluggableDiagRxPowerEntry,_R:atPluggableDiagRxPowerIfIndex,_S:atPluggableDiagRxPowerChannel,'atPluggableDiagRxPowerStatusReading':atPluggableDiagRxPowerStatusReading,'atPluggableDiagRxPowerCurrentAlarm':atPluggableDiagRxPowerCurrentAlarm,'atPluggableDiagRxPowerAlarmMax':atPluggableDiagRxPowerAlarmMax,'atPluggableDiagRxPowerAlarmMin':atPluggableDiagRxPowerAlarmMin,'atPluggableDiagRxPowerCurrentWarning':atPluggableDiagRxPowerCurrentWarning,'atPluggableDiagRxPowerWarningMax':atPluggableDiagRxPowerWarningMax,'atPluggableDiagRxPowerWarningMin':atPluggableDiagRxPowerWarningMin,'atPluggableDiagRxLosTable':atPluggableDiagRxLosTable,'atPluggableDiagRxLosEntry':atPluggableDiagRxLosEntry,_T:atPluggableDiagRxLosIfIndex,_U:atPluggableDiagRxLosChannel,'atPluggableDiagRxLosStatusReading':atPluggableDiagRxLosStatusReading})