_p='gtSensorsBasicNotificationsGroup'
_o='gtSensorsSetGroup'
_n='gtSensorsTrapGroup'
_m='gtSensorsStatsGroup'
_l='gtSensorsSystemGroup'
_k='gtSensorsV1Group'
_j='gtSensorsNotifyPSUTemperature'
_i='gtSensorsNotifyPSUVoltage'
_h='gtSensorsNotifyPSUCurrent'
_g='gtSensorsNotifyFanSpeed'
_f='gtSensorsNotifyTemperature'
_e='gtSensorsNotifyPSUPlugout'
_d='gtSensorsNotifyPSUPlugin'
_c='gtSensorsNotifyFanPlugout'
_b='gtSensorsNotifyFanPlugin'
_a='gtNumPSUs'
_Z='gtFanLifetime'
_Y='gtFanUptime'
_X='gtNumFans'
_W='gtNumTemps'
_V='gtTemp'
_U='gtModule'
_T='WISI-GTMODULES-MIB'
_S='gtPSUTemperature'
_R='gtPSUVoltageExt'
_Q='gtPSUVoltageOR'
_P='gtPSUPower'
_O='gtPSUName'
_N='gtFanName'
_M='gtTempName'
_L='not-accessible'
_K='Integer32'
_J='gtPSUVoltageInt'
_I='gtPSUCurrent'
_H='gtFanSpeed'
_G='gtFanControl'
_F='gtTempValue'
_E='DisplayString'
_D='Unsigned32'
_C='read-only'
_B='current'
_A='WISI-GTSENSORS-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_K,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_D,'iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_E,'PhysAddress','TextualConvention')
gtModule,=mibBuilder.importSymbols(_T,_U)
gtUnit,=mibBuilder.importSymbols('WISI-TANGRAM-MIB','gtUnit')
gtSensorsMIB=ModuleIdentity((1,3,6,1,4,1,7465,20,2,9,1,3))
if mibBuilder.loadTexts:gtSensorsMIB.setRevisions(('2016-09-08 00:00','2013-07-01 14:00','2013-06-27 14:00','2013-06-26 14:00','2012-12-12 13:20','2011-12-15 12:00'))
_GtSensorsNotifications_ObjectIdentity=ObjectIdentity
gtSensorsNotifications=_GtSensorsNotifications_ObjectIdentity((1,3,6,1,4,1,7465,20,2,9,1,3,0))
_GtSensorsObjects_ObjectIdentity=ObjectIdentity
gtSensorsObjects=_GtSensorsObjects_ObjectIdentity((1,3,6,1,4,1,7465,20,2,9,1,3,1))
class _GtNumTemps_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_GtNumTemps_Type.__name__=_D
_GtNumTemps_Object=MibScalar
gtNumTemps=_GtNumTemps_Object((1,3,6,1,4,1,7465,20,2,9,1,3,1,1),_GtNumTemps_Type())
gtNumTemps.setMaxAccess(_C)
if mibBuilder.loadTexts:gtNumTemps.setStatus(_B)
_GtTempsTable_Object=MibTable
gtTempsTable=_GtTempsTable_Object((1,3,6,1,4,1,7465,20,2,9,1,3,1,2))
if mibBuilder.loadTexts:gtTempsTable.setStatus(_B)
_GtTempsEntry_Object=MibTableRow
gtTempsEntry=_GtTempsEntry_Object((1,3,6,1,4,1,7465,20,2,9,1,3,1,2,1))
gtTempsEntry.setIndexNames((0,_T,_U),(0,_A,_V))
if mibBuilder.loadTexts:gtTempsEntry.setStatus(_B)
class _GtTemp_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,15))
_GtTemp_Type.__name__=_D
_GtTemp_Object=MibTableColumn
gtTemp=_GtTemp_Object((1,3,6,1,4,1,7465,20,2,9,1,3,1,2,1,1),_GtTemp_Type())
gtTemp.setMaxAccess(_L)
if mibBuilder.loadTexts:gtTemp.setStatus(_B)
class _GtTempName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(16,16));fixedLength=16
_GtTempName_Type.__name__=_E
_GtTempName_Object=MibTableColumn
gtTempName=_GtTempName_Object((1,3,6,1,4,1,7465,20,2,9,1,3,1,2,1,2),_GtTempName_Type())
gtTempName.setMaxAccess(_C)
if mibBuilder.loadTexts:gtTempName.setStatus(_B)
class _GtTempValue_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-60,195))
_GtTempValue_Type.__name__=_K
_GtTempValue_Object=MibTableColumn
gtTempValue=_GtTempValue_Object((1,3,6,1,4,1,7465,20,2,9,1,3,1,2,1,3),_GtTempValue_Type())
gtTempValue.setMaxAccess(_C)
if mibBuilder.loadTexts:gtTempValue.setStatus(_B)
if mibBuilder.loadTexts:gtTempValue.setUnits("'C")
class _GtNumFans_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_GtNumFans_Type.__name__=_D
_GtNumFans_Object=MibScalar
gtNumFans=_GtNumFans_Object((1,3,6,1,4,1,7465,20,2,9,1,3,1,3),_GtNumFans_Type())
gtNumFans.setMaxAccess(_C)
if mibBuilder.loadTexts:gtNumFans.setStatus(_B)
_GtFansTable_Object=MibTable
gtFansTable=_GtFansTable_Object((1,3,6,1,4,1,7465,20,2,9,1,3,1,4))
if mibBuilder.loadTexts:gtFansTable.setStatus(_B)
_GtFansEntry_Object=MibTableRow
gtFansEntry=_GtFansEntry_Object((1,3,6,1,4,1,7465,20,2,9,1,3,1,4,1))
gtFansEntry.setIndexNames((0,_A,'gtFan'))
if mibBuilder.loadTexts:gtFansEntry.setStatus(_B)
class _GtFan_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,15))
_GtFan_Type.__name__=_D
_GtFan_Object=MibTableColumn
gtFan=_GtFan_Object((1,3,6,1,4,1,7465,20,2,9,1,3,1,4,1,1),_GtFan_Type())
gtFan.setMaxAccess(_L)
if mibBuilder.loadTexts:gtFan.setStatus(_B)
class _GtFanName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(16,16));fixedLength=16
_GtFanName_Type.__name__=_E
_GtFanName_Object=MibTableColumn
gtFanName=_GtFanName_Object((1,3,6,1,4,1,7465,20,2,9,1,3,1,4,1,2),_GtFanName_Type())
gtFanName.setMaxAccess(_C)
if mibBuilder.loadTexts:gtFanName.setStatus(_B)
class _GtFanControl_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,15000))
_GtFanControl_Type.__name__=_D
_GtFanControl_Object=MibTableColumn
gtFanControl=_GtFanControl_Object((1,3,6,1,4,1,7465,20,2,9,1,3,1,4,1,3),_GtFanControl_Type())
gtFanControl.setMaxAccess(_C)
if mibBuilder.loadTexts:gtFanControl.setStatus(_B)
if mibBuilder.loadTexts:gtFanControl.setUnits('rpm')
class _GtFanSpeed_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,15000))
_GtFanSpeed_Type.__name__=_D
_GtFanSpeed_Object=MibTableColumn
gtFanSpeed=_GtFanSpeed_Object((1,3,6,1,4,1,7465,20,2,9,1,3,1,4,1,4),_GtFanSpeed_Type())
gtFanSpeed.setMaxAccess(_C)
if mibBuilder.loadTexts:gtFanSpeed.setStatus(_B)
if mibBuilder.loadTexts:gtFanSpeed.setUnits('rpm')
_GtFanUptime_Type=Counter32
_GtFanUptime_Object=MibTableColumn
gtFanUptime=_GtFanUptime_Object((1,3,6,1,4,1,7465,20,2,9,1,3,1,4,1,5),_GtFanUptime_Type())
gtFanUptime.setMaxAccess(_C)
if mibBuilder.loadTexts:gtFanUptime.setStatus(_B)
if mibBuilder.loadTexts:gtFanUptime.setUnits('s')
_GtFanLifetime_Type=Counter32
_GtFanLifetime_Object=MibTableColumn
gtFanLifetime=_GtFanLifetime_Object((1,3,6,1,4,1,7465,20,2,9,1,3,1,4,1,6),_GtFanLifetime_Type())
gtFanLifetime.setMaxAccess(_C)
if mibBuilder.loadTexts:gtFanLifetime.setStatus(_B)
if mibBuilder.loadTexts:gtFanLifetime.setUnits('s')
class _GtNumPSUs_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_GtNumPSUs_Type.__name__=_D
_GtNumPSUs_Object=MibScalar
gtNumPSUs=_GtNumPSUs_Object((1,3,6,1,4,1,7465,20,2,9,1,3,1,5),_GtNumPSUs_Type())
gtNumPSUs.setMaxAccess(_C)
if mibBuilder.loadTexts:gtNumPSUs.setStatus(_B)
_GtPSUsTable_Object=MibTable
gtPSUsTable=_GtPSUsTable_Object((1,3,6,1,4,1,7465,20,2,9,1,3,1,6))
if mibBuilder.loadTexts:gtPSUsTable.setStatus(_B)
_GtPSUsEntry_Object=MibTableRow
gtPSUsEntry=_GtPSUsEntry_Object((1,3,6,1,4,1,7465,20,2,9,1,3,1,6,1))
gtPSUsEntry.setIndexNames((0,_A,'gtPSU'))
if mibBuilder.loadTexts:gtPSUsEntry.setStatus(_B)
class _GtPSU_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,15))
_GtPSU_Type.__name__=_D
_GtPSU_Object=MibTableColumn
gtPSU=_GtPSU_Object((1,3,6,1,4,1,7465,20,2,9,1,3,1,6,1,1),_GtPSU_Type())
gtPSU.setMaxAccess(_L)
if mibBuilder.loadTexts:gtPSU.setStatus(_B)
class _GtPSUName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(16,16));fixedLength=16
_GtPSUName_Type.__name__=_E
_GtPSUName_Object=MibTableColumn
gtPSUName=_GtPSUName_Object((1,3,6,1,4,1,7465,20,2,9,1,3,1,6,1,2),_GtPSUName_Type())
gtPSUName.setMaxAccess(_C)
if mibBuilder.loadTexts:gtPSUName.setStatus(_B)
class _GtPSUPower_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,300000))
_GtPSUPower_Type.__name__=_D
_GtPSUPower_Object=MibTableColumn
gtPSUPower=_GtPSUPower_Object((1,3,6,1,4,1,7465,20,2,9,1,3,1,6,1,3),_GtPSUPower_Type())
gtPSUPower.setMaxAccess(_C)
if mibBuilder.loadTexts:gtPSUPower.setStatus(_B)
if mibBuilder.loadTexts:gtPSUPower.setUnits('mW')
class _GtPSUCurrent_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,25000))
_GtPSUCurrent_Type.__name__=_D
_GtPSUCurrent_Object=MibTableColumn
gtPSUCurrent=_GtPSUCurrent_Object((1,3,6,1,4,1,7465,20,2,9,1,3,1,6,1,4),_GtPSUCurrent_Type())
gtPSUCurrent.setMaxAccess(_C)
if mibBuilder.loadTexts:gtPSUCurrent.setStatus(_B)
if mibBuilder.loadTexts:gtPSUCurrent.setUnits('mA')
class _GtPSUVoltageInt_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,16000))
_GtPSUVoltageInt_Type.__name__=_D
_GtPSUVoltageInt_Object=MibTableColumn
gtPSUVoltageInt=_GtPSUVoltageInt_Object((1,3,6,1,4,1,7465,20,2,9,1,3,1,6,1,5),_GtPSUVoltageInt_Type())
gtPSUVoltageInt.setMaxAccess(_C)
if mibBuilder.loadTexts:gtPSUVoltageInt.setStatus(_B)
if mibBuilder.loadTexts:gtPSUVoltageInt.setUnits('mV')
class _GtPSUVoltageOR_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,16000))
_GtPSUVoltageOR_Type.__name__=_D
_GtPSUVoltageOR_Object=MibTableColumn
gtPSUVoltageOR=_GtPSUVoltageOR_Object((1,3,6,1,4,1,7465,20,2,9,1,3,1,6,1,6),_GtPSUVoltageOR_Type())
gtPSUVoltageOR.setMaxAccess(_C)
if mibBuilder.loadTexts:gtPSUVoltageOR.setStatus(_B)
if mibBuilder.loadTexts:gtPSUVoltageOR.setUnits('mV')
class _GtPSUVoltageExt_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,16000))
_GtPSUVoltageExt_Type.__name__=_D
_GtPSUVoltageExt_Object=MibTableColumn
gtPSUVoltageExt=_GtPSUVoltageExt_Object((1,3,6,1,4,1,7465,20,2,9,1,3,1,6,1,7),_GtPSUVoltageExt_Type())
gtPSUVoltageExt.setMaxAccess(_C)
if mibBuilder.loadTexts:gtPSUVoltageExt.setStatus(_B)
if mibBuilder.loadTexts:gtPSUVoltageExt.setUnits('mV')
class _GtPSUTemperature_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-60,195))
_GtPSUTemperature_Type.__name__=_K
_GtPSUTemperature_Object=MibTableColumn
gtPSUTemperature=_GtPSUTemperature_Object((1,3,6,1,4,1,7465,20,2,9,1,3,1,6,1,8),_GtPSUTemperature_Type())
gtPSUTemperature.setMaxAccess(_C)
if mibBuilder.loadTexts:gtPSUTemperature.setStatus(_B)
if mibBuilder.loadTexts:gtPSUTemperature.setUnits("'C")
_GtSensorsConformance_ObjectIdentity=ObjectIdentity
gtSensorsConformance=_GtSensorsConformance_ObjectIdentity((1,3,6,1,4,1,7465,20,2,9,1,3,2))
_GtSensorsCompliances_ObjectIdentity=ObjectIdentity
gtSensorsCompliances=_GtSensorsCompliances_ObjectIdentity((1,3,6,1,4,1,7465,20,2,9,1,3,2,1))
_GtSensorsGroups_ObjectIdentity=ObjectIdentity
gtSensorsGroups=_GtSensorsGroups_ObjectIdentity((1,3,6,1,4,1,7465,20,2,9,1,3,2,2))
gtSensorsV1Group=ObjectGroup((1,3,6,1,4,1,7465,20,2,9,1,3,2,2,1))
gtSensorsV1Group.setObjects(*((_A,_M),(_A,_F),(_A,_N),(_A,_G),(_A,_H),(_A,_O),(_A,_P),(_A,_I),(_A,_J),(_A,_Q),(_A,_R),(_A,_S)))
if mibBuilder.loadTexts:gtSensorsV1Group.setStatus(_B)
gtSensorsSystemGroup=ObjectGroup((1,3,6,1,4,1,7465,20,2,9,1,3,2,2,2))
gtSensorsSystemGroup.setObjects(*((_A,_M),(_A,_F),(_A,_N),(_A,_H),(_A,_O),(_A,_P),(_A,_I),(_A,_J),(_A,_Q),(_A,_R),(_A,_S)))
if mibBuilder.loadTexts:gtSensorsSystemGroup.setStatus(_B)
gtSensorsStatsGroup=ObjectGroup((1,3,6,1,4,1,7465,20,2,9,1,3,2,2,3))
gtSensorsStatsGroup.setObjects(*((_A,_W),(_A,_X),(_A,_Y),(_A,_Z),(_A,_a)))
if mibBuilder.loadTexts:gtSensorsStatsGroup.setStatus(_B)
gtSensorsTrapGroup=ObjectGroup((1,3,6,1,4,1,7465,20,2,9,1,3,2,2,4))
gtSensorsTrapGroup.setObjects(*((_A,_F),(_A,_G),(_A,_H),(_A,_I),(_A,_J)))
if mibBuilder.loadTexts:gtSensorsTrapGroup.setStatus(_B)
gtSensorsSetGroup=ObjectGroup((1,3,6,1,4,1,7465,20,2,9,1,3,2,2,5))
gtSensorsSetGroup.setObjects((_A,_G))
if mibBuilder.loadTexts:gtSensorsSetGroup.setStatus(_B)
gtSensorsNotifyFanPlugin=NotificationType((1,3,6,1,4,1,7465,20,2,9,1,3,0,1))
if mibBuilder.loadTexts:gtSensorsNotifyFanPlugin.setStatus(_B)
gtSensorsNotifyFanPlugout=NotificationType((1,3,6,1,4,1,7465,20,2,9,1,3,0,2))
if mibBuilder.loadTexts:gtSensorsNotifyFanPlugout.setStatus(_B)
gtSensorsNotifyPSUPlugin=NotificationType((1,3,6,1,4,1,7465,20,2,9,1,3,0,3))
if mibBuilder.loadTexts:gtSensorsNotifyPSUPlugin.setStatus(_B)
gtSensorsNotifyPSUPlugout=NotificationType((1,3,6,1,4,1,7465,20,2,9,1,3,0,4))
if mibBuilder.loadTexts:gtSensorsNotifyPSUPlugout.setStatus(_B)
gtSensorsNotifyTemperature=NotificationType((1,3,6,1,4,1,7465,20,2,9,1,3,0,5))
if mibBuilder.loadTexts:gtSensorsNotifyTemperature.setStatus(_B)
gtSensorsNotifyFanSpeed=NotificationType((1,3,6,1,4,1,7465,20,2,9,1,3,0,6))
if mibBuilder.loadTexts:gtSensorsNotifyFanSpeed.setStatus(_B)
gtSensorsNotifyPSUCurrent=NotificationType((1,3,6,1,4,1,7465,20,2,9,1,3,0,7))
if mibBuilder.loadTexts:gtSensorsNotifyPSUCurrent.setStatus(_B)
gtSensorsNotifyPSUVoltage=NotificationType((1,3,6,1,4,1,7465,20,2,9,1,3,0,8))
if mibBuilder.loadTexts:gtSensorsNotifyPSUVoltage.setStatus(_B)
gtSensorsNotifyPSUTemperature=NotificationType((1,3,6,1,4,1,7465,20,2,9,1,3,0,9))
if mibBuilder.loadTexts:gtSensorsNotifyPSUTemperature.setStatus(_B)
gtSensorsNotifyPSUTemperatureClear=NotificationType((1,3,6,1,4,1,7465,20,2,9,1,3,0,10))
if mibBuilder.loadTexts:gtSensorsNotifyPSUTemperatureClear.setStatus(_B)
gtSensorsNotifyBOARDTemperatureClear=NotificationType((1,3,6,1,4,1,7465,20,2,9,1,3,0,11))
if mibBuilder.loadTexts:gtSensorsNotifyBOARDTemperatureClear.setStatus(_B)
gtSensorsNotifyPSUFailure=NotificationType((1,3,6,1,4,1,7465,20,2,9,1,3,0,12))
if mibBuilder.loadTexts:gtSensorsNotifyPSUFailure.setStatus(_B)
gtSensorsNotifyPSUFailureClear=NotificationType((1,3,6,1,4,1,7465,20,2,9,1,3,0,13))
if mibBuilder.loadTexts:gtSensorsNotifyPSUFailureClear.setStatus(_B)
gtSensorsBasicNotificationsGroup=NotificationGroup((1,3,6,1,4,1,7465,20,2,9,1,3,2,2,6))
gtSensorsBasicNotificationsGroup.setObjects(*((_A,_b),(_A,_c),(_A,_d),(_A,_e),(_A,_f),(_A,_g),(_A,_h),(_A,_i),(_A,_j)))
if mibBuilder.loadTexts:gtSensorsBasicNotificationsGroup.setStatus(_B)
gtSensorsMIBCompliance=ModuleCompliance((1,3,6,1,4,1,7465,20,2,9,1,3,2,1,1))
gtSensorsMIBCompliance.setObjects(*((_A,_k),(_A,_l),(_A,_m),(_A,_n),(_A,_o),(_A,_p)))
if mibBuilder.loadTexts:gtSensorsMIBCompliance.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'gtSensorsMIB':gtSensorsMIB,'gtSensorsNotifications':gtSensorsNotifications,_b:gtSensorsNotifyFanPlugin,_c:gtSensorsNotifyFanPlugout,_d:gtSensorsNotifyPSUPlugin,_e:gtSensorsNotifyPSUPlugout,_f:gtSensorsNotifyTemperature,_g:gtSensorsNotifyFanSpeed,_h:gtSensorsNotifyPSUCurrent,_i:gtSensorsNotifyPSUVoltage,_j:gtSensorsNotifyPSUTemperature,'gtSensorsNotifyPSUTemperatureClear':gtSensorsNotifyPSUTemperatureClear,'gtSensorsNotifyBOARDTemperatureClear':gtSensorsNotifyBOARDTemperatureClear,'gtSensorsNotifyPSUFailure':gtSensorsNotifyPSUFailure,'gtSensorsNotifyPSUFailureClear':gtSensorsNotifyPSUFailureClear,'gtSensorsObjects':gtSensorsObjects,_W:gtNumTemps,'gtTempsTable':gtTempsTable,'gtTempsEntry':gtTempsEntry,_V:gtTemp,_M:gtTempName,_F:gtTempValue,_X:gtNumFans,'gtFansTable':gtFansTable,'gtFansEntry':gtFansEntry,'gtFan':gtFan,_N:gtFanName,_G:gtFanControl,_H:gtFanSpeed,_Y:gtFanUptime,_Z:gtFanLifetime,_a:gtNumPSUs,'gtPSUsTable':gtPSUsTable,'gtPSUsEntry':gtPSUsEntry,'gtPSU':gtPSU,_O:gtPSUName,_P:gtPSUPower,_I:gtPSUCurrent,_J:gtPSUVoltageInt,_Q:gtPSUVoltageOR,_R:gtPSUVoltageExt,_S:gtPSUTemperature,'gtSensorsConformance':gtSensorsConformance,'gtSensorsCompliances':gtSensorsCompliances,'gtSensorsMIBCompliance':gtSensorsMIBCompliance,'gtSensorsGroups':gtSensorsGroups,_k:gtSensorsV1Group,_l:gtSensorsSystemGroup,_m:gtSensorsStatsGroup,_n:gtSensorsTrapGroup,_o:gtSensorsSetGroup,_p:gtSensorsBasicNotificationsGroup})