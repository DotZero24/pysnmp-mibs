_J='bsDdiSfpIfIndex'
_I='bsDdiSfpRxPowerValue'
_H='bsDdiSfpTxPowerValue'
_G='bsDdiSfpBiasValue'
_F='bsDdiSfpVoltageValue'
_E='bsDdiSfpTempValue'
_D='BAY-STACK-SFF-MIB'
_C='read-only'
_B='Integer32'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
InterfaceIndex,=mibBuilder.importSymbols('IF-MIB','InterfaceIndex')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_B,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
bayStackMibs,=mibBuilder.importSymbols('SYNOPTICS-ROOT-MIB','bayStackMibs')
bayStackDdiSfpMib=ModuleIdentity((1,3,6,1,4,1,45,5,29))
if mibBuilder.loadTexts:bayStackDdiSfpMib.setRevisions(('2012-06-05 00:00','2008-06-03 00:00'))
_BsDdiSfpNotifications_ObjectIdentity=ObjectIdentity
bsDdiSfpNotifications=_BsDdiSfpNotifications_ObjectIdentity((1,3,6,1,4,1,45,5,29,0))
_BsDdiSfpObjects_ObjectIdentity=ObjectIdentity
bsDdiSfpObjects=_BsDdiSfpObjects_ObjectIdentity((1,3,6,1,4,1,45,5,29,1))
_BsDdiSfpTable_Object=MibTable
bsDdiSfpTable=_BsDdiSfpTable_Object((1,3,6,1,4,1,45,5,29,1,2))
if mibBuilder.loadTexts:bsDdiSfpTable.setStatus(_A)
_BsDdiSfpEntry_Object=MibTableRow
bsDdiSfpEntry=_BsDdiSfpEntry_Object((1,3,6,1,4,1,45,5,29,1,2,1))
bsDdiSfpEntry.setIndexNames((0,_D,_J))
if mibBuilder.loadTexts:bsDdiSfpEntry.setStatus(_A)
_BsDdiSfpIfIndex_Type=InterfaceIndex
_BsDdiSfpIfIndex_Object=MibTableColumn
bsDdiSfpIfIndex=_BsDdiSfpIfIndex_Object((1,3,6,1,4,1,45,5,29,1,2,1,1),_BsDdiSfpIfIndex_Type())
bsDdiSfpIfIndex.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:bsDdiSfpIfIndex.setStatus(_A)
class _BsDdiSfpCalibration_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('internal',1),('external',2)))
_BsDdiSfpCalibration_Type.__name__=_B
_BsDdiSfpCalibration_Object=MibTableColumn
bsDdiSfpCalibration=_BsDdiSfpCalibration_Object((1,3,6,1,4,1,45,5,29,1,2,1,2),_BsDdiSfpCalibration_Type())
bsDdiSfpCalibration.setMaxAccess(_C)
if mibBuilder.loadTexts:bsDdiSfpCalibration.setStatus(_A)
class _BsDdiSfpRxPowerMeasurement_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('oma',1),('averagePower',2)))
_BsDdiSfpRxPowerMeasurement_Type.__name__=_B
_BsDdiSfpRxPowerMeasurement_Object=MibTableColumn
bsDdiSfpRxPowerMeasurement=_BsDdiSfpRxPowerMeasurement_Object((1,3,6,1,4,1,45,5,29,1,2,1,3),_BsDdiSfpRxPowerMeasurement_Type())
bsDdiSfpRxPowerMeasurement.setMaxAccess(_C)
if mibBuilder.loadTexts:bsDdiSfpRxPowerMeasurement.setStatus(_A)
class _BsDdiSfpTempValue_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1280000,1280000))
_BsDdiSfpTempValue_Type.__name__=_B
_BsDdiSfpTempValue_Object=MibTableColumn
bsDdiSfpTempValue=_BsDdiSfpTempValue_Object((1,3,6,1,4,1,45,5,29,1,2,1,4),_BsDdiSfpTempValue_Type())
bsDdiSfpTempValue.setMaxAccess(_C)
if mibBuilder.loadTexts:bsDdiSfpTempValue.setStatus(_A)
class _BsDdiSfpTempLowAlarmThreshold_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1280000,1280000))
_BsDdiSfpTempLowAlarmThreshold_Type.__name__=_B
_BsDdiSfpTempLowAlarmThreshold_Object=MibTableColumn
bsDdiSfpTempLowAlarmThreshold=_BsDdiSfpTempLowAlarmThreshold_Object((1,3,6,1,4,1,45,5,29,1,2,1,5),_BsDdiSfpTempLowAlarmThreshold_Type())
bsDdiSfpTempLowAlarmThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:bsDdiSfpTempLowAlarmThreshold.setStatus(_A)
class _BsDdiSfpTempLowWarnThreshold_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1280000,1280000))
_BsDdiSfpTempLowWarnThreshold_Type.__name__=_B
_BsDdiSfpTempLowWarnThreshold_Object=MibTableColumn
bsDdiSfpTempLowWarnThreshold=_BsDdiSfpTempLowWarnThreshold_Object((1,3,6,1,4,1,45,5,29,1,2,1,6),_BsDdiSfpTempLowWarnThreshold_Type())
bsDdiSfpTempLowWarnThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:bsDdiSfpTempLowWarnThreshold.setStatus(_A)
class _BsDdiSfpTempHighAlarmThreshold_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1280000,1280000))
_BsDdiSfpTempHighAlarmThreshold_Type.__name__=_B
_BsDdiSfpTempHighAlarmThreshold_Object=MibTableColumn
bsDdiSfpTempHighAlarmThreshold=_BsDdiSfpTempHighAlarmThreshold_Object((1,3,6,1,4,1,45,5,29,1,2,1,7),_BsDdiSfpTempHighAlarmThreshold_Type())
bsDdiSfpTempHighAlarmThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:bsDdiSfpTempHighAlarmThreshold.setStatus(_A)
class _BsDdiSfpTempHighWarnThreshold_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1280000,1280000))
_BsDdiSfpTempHighWarnThreshold_Type.__name__=_B
_BsDdiSfpTempHighWarnThreshold_Object=MibTableColumn
bsDdiSfpTempHighWarnThreshold=_BsDdiSfpTempHighWarnThreshold_Object((1,3,6,1,4,1,45,5,29,1,2,1,8),_BsDdiSfpTempHighWarnThreshold_Type())
bsDdiSfpTempHighWarnThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:bsDdiSfpTempHighWarnThreshold.setStatus(_A)
class _BsDdiSfpVoltageValue_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65500))
_BsDdiSfpVoltageValue_Type.__name__=_B
_BsDdiSfpVoltageValue_Object=MibTableColumn
bsDdiSfpVoltageValue=_BsDdiSfpVoltageValue_Object((1,3,6,1,4,1,45,5,29,1,2,1,9),_BsDdiSfpVoltageValue_Type())
bsDdiSfpVoltageValue.setMaxAccess(_C)
if mibBuilder.loadTexts:bsDdiSfpVoltageValue.setStatus(_A)
class _BsDdiSfpVoltageLowAlarmThreshold_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65500))
_BsDdiSfpVoltageLowAlarmThreshold_Type.__name__=_B
_BsDdiSfpVoltageLowAlarmThreshold_Object=MibTableColumn
bsDdiSfpVoltageLowAlarmThreshold=_BsDdiSfpVoltageLowAlarmThreshold_Object((1,3,6,1,4,1,45,5,29,1,2,1,10),_BsDdiSfpVoltageLowAlarmThreshold_Type())
bsDdiSfpVoltageLowAlarmThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:bsDdiSfpVoltageLowAlarmThreshold.setStatus(_A)
class _BsDdiSfpVoltageLowWarnThreshold_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65500))
_BsDdiSfpVoltageLowWarnThreshold_Type.__name__=_B
_BsDdiSfpVoltageLowWarnThreshold_Object=MibTableColumn
bsDdiSfpVoltageLowWarnThreshold=_BsDdiSfpVoltageLowWarnThreshold_Object((1,3,6,1,4,1,45,5,29,1,2,1,11),_BsDdiSfpVoltageLowWarnThreshold_Type())
bsDdiSfpVoltageLowWarnThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:bsDdiSfpVoltageLowWarnThreshold.setStatus(_A)
class _BsDdiSfpVoltageHighAlarmThreshold_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65500))
_BsDdiSfpVoltageHighAlarmThreshold_Type.__name__=_B
_BsDdiSfpVoltageHighAlarmThreshold_Object=MibTableColumn
bsDdiSfpVoltageHighAlarmThreshold=_BsDdiSfpVoltageHighAlarmThreshold_Object((1,3,6,1,4,1,45,5,29,1,2,1,12),_BsDdiSfpVoltageHighAlarmThreshold_Type())
bsDdiSfpVoltageHighAlarmThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:bsDdiSfpVoltageHighAlarmThreshold.setStatus(_A)
class _BsDdiSfpVoltageHighWarnThreshold_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65500))
_BsDdiSfpVoltageHighWarnThreshold_Type.__name__=_B
_BsDdiSfpVoltageHighWarnThreshold_Object=MibTableColumn
bsDdiSfpVoltageHighWarnThreshold=_BsDdiSfpVoltageHighWarnThreshold_Object((1,3,6,1,4,1,45,5,29,1,2,1,13),_BsDdiSfpVoltageHighWarnThreshold_Type())
bsDdiSfpVoltageHighWarnThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:bsDdiSfpVoltageHighWarnThreshold.setStatus(_A)
class _BsDdiSfpBiasValue_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1280000))
_BsDdiSfpBiasValue_Type.__name__=_B
_BsDdiSfpBiasValue_Object=MibTableColumn
bsDdiSfpBiasValue=_BsDdiSfpBiasValue_Object((1,3,6,1,4,1,45,5,29,1,2,1,14),_BsDdiSfpBiasValue_Type())
bsDdiSfpBiasValue.setMaxAccess(_C)
if mibBuilder.loadTexts:bsDdiSfpBiasValue.setStatus(_A)
class _BsDdiSfpBiasLowAlarmThreshold_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1280000))
_BsDdiSfpBiasLowAlarmThreshold_Type.__name__=_B
_BsDdiSfpBiasLowAlarmThreshold_Object=MibTableColumn
bsDdiSfpBiasLowAlarmThreshold=_BsDdiSfpBiasLowAlarmThreshold_Object((1,3,6,1,4,1,45,5,29,1,2,1,15),_BsDdiSfpBiasLowAlarmThreshold_Type())
bsDdiSfpBiasLowAlarmThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:bsDdiSfpBiasLowAlarmThreshold.setStatus(_A)
class _BsDdiSfpBiasLowWarnThreshold_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1280000))
_BsDdiSfpBiasLowWarnThreshold_Type.__name__=_B
_BsDdiSfpBiasLowWarnThreshold_Object=MibTableColumn
bsDdiSfpBiasLowWarnThreshold=_BsDdiSfpBiasLowWarnThreshold_Object((1,3,6,1,4,1,45,5,29,1,2,1,16),_BsDdiSfpBiasLowWarnThreshold_Type())
bsDdiSfpBiasLowWarnThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:bsDdiSfpBiasLowWarnThreshold.setStatus(_A)
class _BsDdiSfpBiasHighAlarmThreshold_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1280000))
_BsDdiSfpBiasHighAlarmThreshold_Type.__name__=_B
_BsDdiSfpBiasHighAlarmThreshold_Object=MibTableColumn
bsDdiSfpBiasHighAlarmThreshold=_BsDdiSfpBiasHighAlarmThreshold_Object((1,3,6,1,4,1,45,5,29,1,2,1,17),_BsDdiSfpBiasHighAlarmThreshold_Type())
bsDdiSfpBiasHighAlarmThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:bsDdiSfpBiasHighAlarmThreshold.setStatus(_A)
class _BsDdiSfpBiasHighWarnThreshold_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1280000))
_BsDdiSfpBiasHighWarnThreshold_Type.__name__=_B
_BsDdiSfpBiasHighWarnThreshold_Object=MibTableColumn
bsDdiSfpBiasHighWarnThreshold=_BsDdiSfpBiasHighWarnThreshold_Object((1,3,6,1,4,1,45,5,29,1,2,1,18),_BsDdiSfpBiasHighWarnThreshold_Type())
bsDdiSfpBiasHighWarnThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:bsDdiSfpBiasHighWarnThreshold.setStatus(_A)
class _BsDdiSfpTxPowerValue_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-400000,83000))
_BsDdiSfpTxPowerValue_Type.__name__=_B
_BsDdiSfpTxPowerValue_Object=MibTableColumn
bsDdiSfpTxPowerValue=_BsDdiSfpTxPowerValue_Object((1,3,6,1,4,1,45,5,29,1,2,1,19),_BsDdiSfpTxPowerValue_Type())
bsDdiSfpTxPowerValue.setMaxAccess(_C)
if mibBuilder.loadTexts:bsDdiSfpTxPowerValue.setStatus(_A)
class _BsDdiSfpTxPowerLowAlarmThreshold_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-400000,83000))
_BsDdiSfpTxPowerLowAlarmThreshold_Type.__name__=_B
_BsDdiSfpTxPowerLowAlarmThreshold_Object=MibTableColumn
bsDdiSfpTxPowerLowAlarmThreshold=_BsDdiSfpTxPowerLowAlarmThreshold_Object((1,3,6,1,4,1,45,5,29,1,2,1,20),_BsDdiSfpTxPowerLowAlarmThreshold_Type())
bsDdiSfpTxPowerLowAlarmThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:bsDdiSfpTxPowerLowAlarmThreshold.setStatus(_A)
class _BsDdiSfpTxPowerLowWarnThreshold_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-400000,83000))
_BsDdiSfpTxPowerLowWarnThreshold_Type.__name__=_B
_BsDdiSfpTxPowerLowWarnThreshold_Object=MibTableColumn
bsDdiSfpTxPowerLowWarnThreshold=_BsDdiSfpTxPowerLowWarnThreshold_Object((1,3,6,1,4,1,45,5,29,1,2,1,21),_BsDdiSfpTxPowerLowWarnThreshold_Type())
bsDdiSfpTxPowerLowWarnThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:bsDdiSfpTxPowerLowWarnThreshold.setStatus(_A)
class _BsDdiSfpTxPowerHighAlarmThreshold_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-400000,83000))
_BsDdiSfpTxPowerHighAlarmThreshold_Type.__name__=_B
_BsDdiSfpTxPowerHighAlarmThreshold_Object=MibTableColumn
bsDdiSfpTxPowerHighAlarmThreshold=_BsDdiSfpTxPowerHighAlarmThreshold_Object((1,3,6,1,4,1,45,5,29,1,2,1,22),_BsDdiSfpTxPowerHighAlarmThreshold_Type())
bsDdiSfpTxPowerHighAlarmThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:bsDdiSfpTxPowerHighAlarmThreshold.setStatus(_A)
class _BsDdiSfpTxPowerHighWarnThreshold_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-400000,83000))
_BsDdiSfpTxPowerHighWarnThreshold_Type.__name__=_B
_BsDdiSfpTxPowerHighWarnThreshold_Object=MibTableColumn
bsDdiSfpTxPowerHighWarnThreshold=_BsDdiSfpTxPowerHighWarnThreshold_Object((1,3,6,1,4,1,45,5,29,1,2,1,23),_BsDdiSfpTxPowerHighWarnThreshold_Type())
bsDdiSfpTxPowerHighWarnThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:bsDdiSfpTxPowerHighWarnThreshold.setStatus(_A)
class _BsDdiSfpRxPowerValue_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-400000,83000))
_BsDdiSfpRxPowerValue_Type.__name__=_B
_BsDdiSfpRxPowerValue_Object=MibTableColumn
bsDdiSfpRxPowerValue=_BsDdiSfpRxPowerValue_Object((1,3,6,1,4,1,45,5,29,1,2,1,24),_BsDdiSfpRxPowerValue_Type())
bsDdiSfpRxPowerValue.setMaxAccess(_C)
if mibBuilder.loadTexts:bsDdiSfpRxPowerValue.setStatus(_A)
class _BsDdiSfpRxPowerLowAlarmThreshold_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-400000,83000))
_BsDdiSfpRxPowerLowAlarmThreshold_Type.__name__=_B
_BsDdiSfpRxPowerLowAlarmThreshold_Object=MibTableColumn
bsDdiSfpRxPowerLowAlarmThreshold=_BsDdiSfpRxPowerLowAlarmThreshold_Object((1,3,6,1,4,1,45,5,29,1,2,1,25),_BsDdiSfpRxPowerLowAlarmThreshold_Type())
bsDdiSfpRxPowerLowAlarmThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:bsDdiSfpRxPowerLowAlarmThreshold.setStatus(_A)
class _BsDdiSfpRxPowerLowWarnThreshold_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-400000,83000))
_BsDdiSfpRxPowerLowWarnThreshold_Type.__name__=_B
_BsDdiSfpRxPowerLowWarnThreshold_Object=MibTableColumn
bsDdiSfpRxPowerLowWarnThreshold=_BsDdiSfpRxPowerLowWarnThreshold_Object((1,3,6,1,4,1,45,5,29,1,2,1,26),_BsDdiSfpRxPowerLowWarnThreshold_Type())
bsDdiSfpRxPowerLowWarnThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:bsDdiSfpRxPowerLowWarnThreshold.setStatus(_A)
class _BsDdiSfpRxPowerHighAlarmThreshold_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-400000,83000))
_BsDdiSfpRxPowerHighAlarmThreshold_Type.__name__=_B
_BsDdiSfpRxPowerHighAlarmThreshold_Object=MibTableColumn
bsDdiSfpRxPowerHighAlarmThreshold=_BsDdiSfpRxPowerHighAlarmThreshold_Object((1,3,6,1,4,1,45,5,29,1,2,1,27),_BsDdiSfpRxPowerHighAlarmThreshold_Type())
bsDdiSfpRxPowerHighAlarmThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:bsDdiSfpRxPowerHighAlarmThreshold.setStatus(_A)
class _BsDdiSfpRxPowerHighWarnThreshold_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-400000,83000))
_BsDdiSfpRxPowerHighWarnThreshold_Type.__name__=_B
_BsDdiSfpRxPowerHighWarnThreshold_Object=MibTableColumn
bsDdiSfpRxPowerHighWarnThreshold=_BsDdiSfpRxPowerHighWarnThreshold_Object((1,3,6,1,4,1,45,5,29,1,2,1,28),_BsDdiSfpRxPowerHighWarnThreshold_Type())
bsDdiSfpRxPowerHighWarnThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:bsDdiSfpRxPowerHighWarnThreshold.setStatus(_A)
bsDdiSfpTempAlarm=NotificationType((1,3,6,1,4,1,45,5,29,0,1))
bsDdiSfpTempAlarm.setObjects((_D,_E))
if mibBuilder.loadTexts:bsDdiSfpTempAlarm.setStatus(_A)
bsDdiSfpTempWarn=NotificationType((1,3,6,1,4,1,45,5,29,0,2))
bsDdiSfpTempWarn.setObjects((_D,_E))
if mibBuilder.loadTexts:bsDdiSfpTempWarn.setStatus(_A)
bsDdiSfpTempNormal=NotificationType((1,3,6,1,4,1,45,5,29,0,3))
bsDdiSfpTempNormal.setObjects((_D,_E))
if mibBuilder.loadTexts:bsDdiSfpTempNormal.setStatus(_A)
bsDdiSfpVoltageAlarm=NotificationType((1,3,6,1,4,1,45,5,29,0,4))
bsDdiSfpVoltageAlarm.setObjects((_D,_F))
if mibBuilder.loadTexts:bsDdiSfpVoltageAlarm.setStatus(_A)
bsDdiSfpVoltageWarn=NotificationType((1,3,6,1,4,1,45,5,29,0,5))
bsDdiSfpVoltageWarn.setObjects((_D,_F))
if mibBuilder.loadTexts:bsDdiSfpVoltageWarn.setStatus(_A)
bsDdiSfpVoltageNormal=NotificationType((1,3,6,1,4,1,45,5,29,0,6))
bsDdiSfpVoltageNormal.setObjects((_D,_F))
if mibBuilder.loadTexts:bsDdiSfpVoltageNormal.setStatus(_A)
bsDdiSfpBiasAlarm=NotificationType((1,3,6,1,4,1,45,5,29,0,7))
bsDdiSfpBiasAlarm.setObjects((_D,_G))
if mibBuilder.loadTexts:bsDdiSfpBiasAlarm.setStatus(_A)
bsDdiSfpBiasWarn=NotificationType((1,3,6,1,4,1,45,5,29,0,8))
bsDdiSfpBiasWarn.setObjects((_D,_G))
if mibBuilder.loadTexts:bsDdiSfpBiasWarn.setStatus(_A)
bsDdiSfpBiasNormal=NotificationType((1,3,6,1,4,1,45,5,29,0,9))
bsDdiSfpBiasNormal.setObjects((_D,_G))
if mibBuilder.loadTexts:bsDdiSfpBiasNormal.setStatus(_A)
bsDdiSfpTxAlarm=NotificationType((1,3,6,1,4,1,45,5,29,0,10))
bsDdiSfpTxAlarm.setObjects((_D,_H))
if mibBuilder.loadTexts:bsDdiSfpTxAlarm.setStatus(_A)
bsDdiSfpTxWarn=NotificationType((1,3,6,1,4,1,45,5,29,0,11))
bsDdiSfpTxWarn.setObjects((_D,_H))
if mibBuilder.loadTexts:bsDdiSfpTxWarn.setStatus(_A)
bsDdiSfpTxNormal=NotificationType((1,3,6,1,4,1,45,5,29,0,12))
bsDdiSfpTxNormal.setObjects((_D,_H))
if mibBuilder.loadTexts:bsDdiSfpTxNormal.setStatus(_A)
bsDdiSfpRxAlarm=NotificationType((1,3,6,1,4,1,45,5,29,0,13))
bsDdiSfpRxAlarm.setObjects((_D,_I))
if mibBuilder.loadTexts:bsDdiSfpRxAlarm.setStatus(_A)
bsDdiSfpRxWarn=NotificationType((1,3,6,1,4,1,45,5,29,0,14))
bsDdiSfpRxWarn.setObjects((_D,_I))
if mibBuilder.loadTexts:bsDdiSfpRxWarn.setStatus(_A)
bsDdiSfpRxNormal=NotificationType((1,3,6,1,4,1,45,5,29,0,15))
bsDdiSfpRxNormal.setObjects((_D,_I))
if mibBuilder.loadTexts:bsDdiSfpRxNormal.setStatus(_A)
mibBuilder.exportSymbols(_D,**{'bayStackDdiSfpMib':bayStackDdiSfpMib,'bsDdiSfpNotifications':bsDdiSfpNotifications,'bsDdiSfpTempAlarm':bsDdiSfpTempAlarm,'bsDdiSfpTempWarn':bsDdiSfpTempWarn,'bsDdiSfpTempNormal':bsDdiSfpTempNormal,'bsDdiSfpVoltageAlarm':bsDdiSfpVoltageAlarm,'bsDdiSfpVoltageWarn':bsDdiSfpVoltageWarn,'bsDdiSfpVoltageNormal':bsDdiSfpVoltageNormal,'bsDdiSfpBiasAlarm':bsDdiSfpBiasAlarm,'bsDdiSfpBiasWarn':bsDdiSfpBiasWarn,'bsDdiSfpBiasNormal':bsDdiSfpBiasNormal,'bsDdiSfpTxAlarm':bsDdiSfpTxAlarm,'bsDdiSfpTxWarn':bsDdiSfpTxWarn,'bsDdiSfpTxNormal':bsDdiSfpTxNormal,'bsDdiSfpRxAlarm':bsDdiSfpRxAlarm,'bsDdiSfpRxWarn':bsDdiSfpRxWarn,'bsDdiSfpRxNormal':bsDdiSfpRxNormal,'bsDdiSfpObjects':bsDdiSfpObjects,'bsDdiSfpTable':bsDdiSfpTable,'bsDdiSfpEntry':bsDdiSfpEntry,_J:bsDdiSfpIfIndex,'bsDdiSfpCalibration':bsDdiSfpCalibration,'bsDdiSfpRxPowerMeasurement':bsDdiSfpRxPowerMeasurement,_E:bsDdiSfpTempValue,'bsDdiSfpTempLowAlarmThreshold':bsDdiSfpTempLowAlarmThreshold,'bsDdiSfpTempLowWarnThreshold':bsDdiSfpTempLowWarnThreshold,'bsDdiSfpTempHighAlarmThreshold':bsDdiSfpTempHighAlarmThreshold,'bsDdiSfpTempHighWarnThreshold':bsDdiSfpTempHighWarnThreshold,_F:bsDdiSfpVoltageValue,'bsDdiSfpVoltageLowAlarmThreshold':bsDdiSfpVoltageLowAlarmThreshold,'bsDdiSfpVoltageLowWarnThreshold':bsDdiSfpVoltageLowWarnThreshold,'bsDdiSfpVoltageHighAlarmThreshold':bsDdiSfpVoltageHighAlarmThreshold,'bsDdiSfpVoltageHighWarnThreshold':bsDdiSfpVoltageHighWarnThreshold,_G:bsDdiSfpBiasValue,'bsDdiSfpBiasLowAlarmThreshold':bsDdiSfpBiasLowAlarmThreshold,'bsDdiSfpBiasLowWarnThreshold':bsDdiSfpBiasLowWarnThreshold,'bsDdiSfpBiasHighAlarmThreshold':bsDdiSfpBiasHighAlarmThreshold,'bsDdiSfpBiasHighWarnThreshold':bsDdiSfpBiasHighWarnThreshold,_H:bsDdiSfpTxPowerValue,'bsDdiSfpTxPowerLowAlarmThreshold':bsDdiSfpTxPowerLowAlarmThreshold,'bsDdiSfpTxPowerLowWarnThreshold':bsDdiSfpTxPowerLowWarnThreshold,'bsDdiSfpTxPowerHighAlarmThreshold':bsDdiSfpTxPowerHighAlarmThreshold,'bsDdiSfpTxPowerHighWarnThreshold':bsDdiSfpTxPowerHighWarnThreshold,_I:bsDdiSfpRxPowerValue,'bsDdiSfpRxPowerLowAlarmThreshold':bsDdiSfpRxPowerLowAlarmThreshold,'bsDdiSfpRxPowerLowWarnThreshold':bsDdiSfpRxPowerLowWarnThreshold,'bsDdiSfpRxPowerHighAlarmThreshold':bsDdiSfpRxPowerHighAlarmThreshold,'bsDdiSfpRxPowerHighWarnThreshold':bsDdiSfpRxPowerHighWarnThreshold})