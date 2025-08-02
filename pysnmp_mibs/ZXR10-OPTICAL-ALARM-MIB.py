_N='zxr10optLowAlarmValue'
_M='zxr10optLowWarnValue'
_L='zxr10optHighWarnValue'
_K='zxr10optHighAlarmValue'
_J='zxr10optAlarmOverCurValue'
_I='zxr10optAlarmOverType'
_H='zxr10optAlarmType'
_G='zxr10optIfName'
_F='zxr10optIfIndex'
_E='zxr10opticalIfIndex'
_D='zxr10optAlarmIndex'
_C='ZXR10-OPTICAL-ALARM-MIB'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
zxr10,=mibBuilder.importSymbols('ZXR10-SMI','zxr10')
zxr10OpticalAlarmMIB=ModuleIdentity((1,3,6,1,4,1,3902,3,126))
if mibBuilder.loadTexts:zxr10OpticalAlarmMIB.setRevisions(('2008-04-18 00:00',))
class OptStatType(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('sfpOffline',1),('sfpNotSupportDom',2),('sfpOnlineAndHaveData',3),('sfpOnlineButNoData',4)))
class Zxr10optAlarmType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4)));namedValues=NamedValues(*(('alarmTemperature',0),('alarmVoltage',1),('alarmCurrent',2),('alarmTxPower',3),('alarmRxPower',4)))
class Zxr10optAlarmOverType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('highAlarm',1),('highWarning',2),('lowWarning',3),('lowAlarm',4)))
_Zxr10Notifications_ObjectIdentity=ObjectIdentity
zxr10Notifications=_Zxr10Notifications_ObjectIdentity((1,3,6,1,4,1,3902,3,126,0))
_Zxr10MIBObjects_ObjectIdentity=ObjectIdentity
zxr10MIBObjects=_Zxr10MIBObjects_ObjectIdentity((1,3,6,1,4,1,3902,3,126,1))
_Zxr10optAlarmTable_Object=MibTable
zxr10optAlarmTable=_Zxr10optAlarmTable_Object((1,3,6,1,4,1,3902,3,126,1,1))
if mibBuilder.loadTexts:zxr10optAlarmTable.setStatus(_A)
_Zxr10optAlarmEntry_Object=MibTableRow
zxr10optAlarmEntry=_Zxr10optAlarmEntry_Object((1,3,6,1,4,1,3902,3,126,1,1,1))
zxr10optAlarmEntry.setIndexNames((0,_C,_D))
if mibBuilder.loadTexts:zxr10optAlarmEntry.setStatus(_A)
_Zxr10optAlarmIndex_Type=Unsigned32
_Zxr10optAlarmIndex_Object=MibTableColumn
zxr10optAlarmIndex=_Zxr10optAlarmIndex_Object((1,3,6,1,4,1,3902,3,126,1,1,1,1),_Zxr10optAlarmIndex_Type())
zxr10optAlarmIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:zxr10optAlarmIndex.setStatus(_A)
_Zxr10optIfIndex_Type=Unsigned32
_Zxr10optIfIndex_Object=MibTableColumn
zxr10optIfIndex=_Zxr10optIfIndex_Object((1,3,6,1,4,1,3902,3,126,1,1,1,2),_Zxr10optIfIndex_Type())
zxr10optIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:zxr10optIfIndex.setStatus(_A)
_Zxr10optIfName_Type=DisplayString
_Zxr10optIfName_Object=MibTableColumn
zxr10optIfName=_Zxr10optIfName_Object((1,3,6,1,4,1,3902,3,126,1,1,1,3),_Zxr10optIfName_Type())
zxr10optIfName.setMaxAccess(_B)
if mibBuilder.loadTexts:zxr10optIfName.setStatus(_A)
_Zxr10optAlarmType_Type=Zxr10optAlarmType
_Zxr10optAlarmType_Object=MibTableColumn
zxr10optAlarmType=_Zxr10optAlarmType_Object((1,3,6,1,4,1,3902,3,126,1,1,1,4),_Zxr10optAlarmType_Type())
zxr10optAlarmType.setMaxAccess(_B)
if mibBuilder.loadTexts:zxr10optAlarmType.setStatus(_A)
_Zxr10optAlarmOverType_Type=Zxr10optAlarmOverType
_Zxr10optAlarmOverType_Object=MibTableColumn
zxr10optAlarmOverType=_Zxr10optAlarmOverType_Object((1,3,6,1,4,1,3902,3,126,1,1,1,5),_Zxr10optAlarmOverType_Type())
zxr10optAlarmOverType.setMaxAccess(_B)
if mibBuilder.loadTexts:zxr10optAlarmOverType.setStatus(_A)
_Zxr10optAlarmOverCurValue_Type=DisplayString
_Zxr10optAlarmOverCurValue_Object=MibTableColumn
zxr10optAlarmOverCurValue=_Zxr10optAlarmOverCurValue_Object((1,3,6,1,4,1,3902,3,126,1,1,1,6),_Zxr10optAlarmOverCurValue_Type())
zxr10optAlarmOverCurValue.setMaxAccess(_B)
if mibBuilder.loadTexts:zxr10optAlarmOverCurValue.setStatus(_A)
_Zxr10optHighAlarmValue_Type=DisplayString
_Zxr10optHighAlarmValue_Object=MibTableColumn
zxr10optHighAlarmValue=_Zxr10optHighAlarmValue_Object((1,3,6,1,4,1,3902,3,126,1,1,1,7),_Zxr10optHighAlarmValue_Type())
zxr10optHighAlarmValue.setMaxAccess(_B)
if mibBuilder.loadTexts:zxr10optHighAlarmValue.setStatus(_A)
_Zxr10optHighWarnValue_Type=DisplayString
_Zxr10optHighWarnValue_Object=MibTableColumn
zxr10optHighWarnValue=_Zxr10optHighWarnValue_Object((1,3,6,1,4,1,3902,3,126,1,1,1,8),_Zxr10optHighWarnValue_Type())
zxr10optHighWarnValue.setMaxAccess(_B)
if mibBuilder.loadTexts:zxr10optHighWarnValue.setStatus(_A)
_Zxr10optLowWarnValue_Type=DisplayString
_Zxr10optLowWarnValue_Object=MibTableColumn
zxr10optLowWarnValue=_Zxr10optLowWarnValue_Object((1,3,6,1,4,1,3902,3,126,1,1,1,9),_Zxr10optLowWarnValue_Type())
zxr10optLowWarnValue.setMaxAccess(_B)
if mibBuilder.loadTexts:zxr10optLowWarnValue.setStatus(_A)
_Zxr10optLowAlarmValue_Type=DisplayString
_Zxr10optLowAlarmValue_Object=MibTableColumn
zxr10optLowAlarmValue=_Zxr10optLowAlarmValue_Object((1,3,6,1,4,1,3902,3,126,1,1,1,10),_Zxr10optLowAlarmValue_Type())
zxr10optLowAlarmValue.setMaxAccess(_B)
if mibBuilder.loadTexts:zxr10optLowAlarmValue.setStatus(_A)
_Zxr10opticalTable_Object=MibTable
zxr10opticalTable=_Zxr10opticalTable_Object((1,3,6,1,4,1,3902,3,126,1,2))
if mibBuilder.loadTexts:zxr10opticalTable.setStatus(_A)
_Zxr10opticalEntry_Object=MibTableRow
zxr10opticalEntry=_Zxr10opticalEntry_Object((1,3,6,1,4,1,3902,3,126,1,2,1))
zxr10opticalEntry.setIndexNames((0,_C,_E))
if mibBuilder.loadTexts:zxr10opticalEntry.setStatus(_A)
_Zxr10opticalIfIndex_Type=Unsigned32
_Zxr10opticalIfIndex_Object=MibTableColumn
zxr10opticalIfIndex=_Zxr10opticalIfIndex_Object((1,3,6,1,4,1,3902,3,126,1,2,1,1),_Zxr10opticalIfIndex_Type())
zxr10opticalIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:zxr10opticalIfIndex.setStatus(_A)
_Zxr10opticalState_Type=OptStatType
_Zxr10opticalState_Object=MibTableColumn
zxr10opticalState=_Zxr10opticalState_Object((1,3,6,1,4,1,3902,3,126,1,2,1,2),_Zxr10opticalState_Type())
zxr10opticalState.setMaxAccess(_B)
if mibBuilder.loadTexts:zxr10opticalState.setStatus(_A)
_Zxr10opticalTxPower_Type=DisplayString
_Zxr10opticalTxPower_Object=MibTableColumn
zxr10opticalTxPower=_Zxr10opticalTxPower_Object((1,3,6,1,4,1,3902,3,126,1,2,1,3),_Zxr10opticalTxPower_Type())
zxr10opticalTxPower.setMaxAccess(_B)
if mibBuilder.loadTexts:zxr10opticalTxPower.setStatus(_A)
_Zxr10opticalRxPower_Type=DisplayString
_Zxr10opticalRxPower_Object=MibTableColumn
zxr10opticalRxPower=_Zxr10opticalRxPower_Object((1,3,6,1,4,1,3902,3,126,1,2,1,4),_Zxr10opticalRxPower_Type())
zxr10opticalRxPower.setMaxAccess(_B)
if mibBuilder.loadTexts:zxr10opticalRxPower.setStatus(_A)
_Zxr10opticalTxCurrent_Type=DisplayString
_Zxr10opticalTxCurrent_Object=MibTableColumn
zxr10opticalTxCurrent=_Zxr10opticalTxCurrent_Object((1,3,6,1,4,1,3902,3,126,1,2,1,5),_Zxr10opticalTxCurrent_Type())
zxr10opticalTxCurrent.setMaxAccess(_B)
if mibBuilder.loadTexts:zxr10opticalTxCurrent.setStatus(_A)
_Zxr10opticalVoltage_Type=DisplayString
_Zxr10opticalVoltage_Object=MibTableColumn
zxr10opticalVoltage=_Zxr10opticalVoltage_Object((1,3,6,1,4,1,3902,3,126,1,2,1,6),_Zxr10opticalVoltage_Type())
zxr10opticalVoltage.setMaxAccess(_B)
if mibBuilder.loadTexts:zxr10opticalVoltage.setStatus(_A)
_Zxr10opticalTemperature_Type=DisplayString
_Zxr10opticalTemperature_Object=MibTableColumn
zxr10opticalTemperature=_Zxr10opticalTemperature_Object((1,3,6,1,4,1,3902,3,126,1,2,1,7),_Zxr10opticalTemperature_Type())
zxr10opticalTemperature.setMaxAccess(_B)
if mibBuilder.loadTexts:zxr10opticalTemperature.setStatus(_A)
zxr10optAlarmTrap=NotificationType((1,3,6,1,4,1,3902,3,126,0,1))
zxr10optAlarmTrap.setObjects(*((_C,_D),(_C,_F),(_C,_G),(_C,_H),(_C,_I),(_C,_J),(_C,_K),(_C,_L),(_C,_M),(_C,_N)))
if mibBuilder.loadTexts:zxr10optAlarmTrap.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'Zxr10optAlarmType':Zxr10optAlarmType,'Zxr10optAlarmOverType':Zxr10optAlarmOverType,'OptStatType':OptStatType,'zxr10OpticalAlarmMIB':zxr10OpticalAlarmMIB,'zxr10Notifications':zxr10Notifications,'zxr10optAlarmTrap':zxr10optAlarmTrap,'zxr10MIBObjects':zxr10MIBObjects,'zxr10optAlarmTable':zxr10optAlarmTable,'zxr10optAlarmEntry':zxr10optAlarmEntry,_D:zxr10optAlarmIndex,_F:zxr10optIfIndex,_G:zxr10optIfName,_H:zxr10optAlarmType,_I:zxr10optAlarmOverType,_J:zxr10optAlarmOverCurValue,_K:zxr10optHighAlarmValue,_L:zxr10optHighWarnValue,_M:zxr10optLowWarnValue,_N:zxr10optLowAlarmValue,'zxr10opticalTable':zxr10opticalTable,'zxr10opticalEntry':zxr10opticalEntry,_E:zxr10opticalIfIndex,'zxr10opticalState':zxr10opticalState,'zxr10opticalTxPower':zxr10opticalTxPower,'zxr10opticalRxPower':zxr10opticalRxPower,'zxr10opticalTxCurrent':zxr10opticalTxCurrent,'zxr10opticalVoltage':zxr10opticalVoltage,'zxr10opticalTemperature':zxr10opticalTemperature})