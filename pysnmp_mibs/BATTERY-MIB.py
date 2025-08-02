_x='batteryAdminGroup'
_w='batteryPerCellNotificationsGroup'
_v='batteryNotificationsGroup'
_u='batteryAlarmThresholdsGroup'
_t='batteryStatusGroup'
_s='batteryDescriptionGroup'
_r='batteryDisconnectedNotification'
_q='batteryConnectedNotification'
_p='batteryTemperatureNotification'
_o='batteryAgingNotification'
_n='batteryCriticalNotification'
_m='batteryLowNotification'
_l='batteryChargingStateNotification'
_k='batteryAlarmLowTemperature'
_j='batteryAlarmHighTemperature'
_i='batteryAlarmHighCycleCount'
_h='batteryAlarmLowCapacity'
_g='batteryAlarmLowVoltage'
_f='batteryAlarmLowCharge'
_e='batteryChargingAdminState'
_d='batteryActualCurrent'
_c='batteryLastChargingCycleTime'
_b='batteryTrickleChargingCurrent'
_a='batteryMaxChargingCurrent'
_Z='batteryDesignCapacity'
_Y='batteryNumberOfCells'
_X='batteryDesignVoltage'
_W='batteryTechnology'
_V='batteryType'
_U='batteryFirmwareVersion'
_T='unknown'
_S='entPhysicalIndex'
_R='ENTITY-MIB'
_Q='batteryTemperature'
_P='batteryChargingOperState'
_O='batteryChargingCycleCount'
_N='batteryActualCapacity'
_M='batteryIdentifier'
_L='deci-degrees Celsius'
_K='milliampere'
_J='millivolt'
_I='batteryActualVoltage'
_H='batteryActualCharge'
_G='Integer32'
_F='milliampere hours'
_E='batteryCellIdentifier'
_D='read-write'
_C='read-only'
_B='current'
_A='BATTERY-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
entPhysicalIndex,=mibBuilder.importSymbols(_R,_S)
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB','SnmpAdminString')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso,mib_2=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_G,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso','mib-2')
DateAndTime,DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime','DisplayString','PhysAddress','TextualConvention')
batteryMIB=ModuleIdentity((1,3,6,1,2,1,233))
if mibBuilder.loadTexts:batteryMIB.setRevisions(('2015-06-15 00:00',))
_BatteryNotifications_ObjectIdentity=ObjectIdentity
batteryNotifications=_BatteryNotifications_ObjectIdentity((1,3,6,1,2,1,233,0))
_BatteryObjects_ObjectIdentity=ObjectIdentity
batteryObjects=_BatteryObjects_ObjectIdentity((1,3,6,1,2,1,233,1))
_BatteryTable_Object=MibTable
batteryTable=_BatteryTable_Object((1,3,6,1,2,1,233,1,1))
if mibBuilder.loadTexts:batteryTable.setStatus(_B)
_BatteryEntry_Object=MibTableRow
batteryEntry=_BatteryEntry_Object((1,3,6,1,2,1,233,1,1,1))
batteryEntry.setIndexNames((0,_R,_S))
if mibBuilder.loadTexts:batteryEntry.setStatus(_B)
_BatteryIdentifier_Type=SnmpAdminString
_BatteryIdentifier_Object=MibTableColumn
batteryIdentifier=_BatteryIdentifier_Object((1,3,6,1,2,1,233,1,1,1,1),_BatteryIdentifier_Type())
batteryIdentifier.setMaxAccess(_C)
if mibBuilder.loadTexts:batteryIdentifier.setStatus(_B)
_BatteryFirmwareVersion_Type=SnmpAdminString
_BatteryFirmwareVersion_Object=MibTableColumn
batteryFirmwareVersion=_BatteryFirmwareVersion_Object((1,3,6,1,2,1,233,1,1,1,2),_BatteryFirmwareVersion_Type())
batteryFirmwareVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:batteryFirmwareVersion.setStatus(_B)
class _BatteryType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_T,1),('other',2),('primary',3),('rechargeable',4),('capacitor',5)))
_BatteryType_Type.__name__=_G
_BatteryType_Object=MibTableColumn
batteryType=_BatteryType_Object((1,3,6,1,2,1,233,1,1,1,3),_BatteryType_Type())
batteryType.setMaxAccess(_C)
if mibBuilder.loadTexts:batteryType.setStatus(_B)
_BatteryTechnology_Type=Unsigned32
_BatteryTechnology_Object=MibTableColumn
batteryTechnology=_BatteryTechnology_Object((1,3,6,1,2,1,233,1,1,1,4),_BatteryTechnology_Type())
batteryTechnology.setMaxAccess(_C)
if mibBuilder.loadTexts:batteryTechnology.setStatus(_B)
_BatteryDesignVoltage_Type=Unsigned32
_BatteryDesignVoltage_Object=MibTableColumn
batteryDesignVoltage=_BatteryDesignVoltage_Object((1,3,6,1,2,1,233,1,1,1,5),_BatteryDesignVoltage_Type())
batteryDesignVoltage.setMaxAccess(_C)
if mibBuilder.loadTexts:batteryDesignVoltage.setStatus(_B)
if mibBuilder.loadTexts:batteryDesignVoltage.setUnits(_J)
_BatteryNumberOfCells_Type=Unsigned32
_BatteryNumberOfCells_Object=MibTableColumn
batteryNumberOfCells=_BatteryNumberOfCells_Object((1,3,6,1,2,1,233,1,1,1,6),_BatteryNumberOfCells_Type())
batteryNumberOfCells.setMaxAccess(_C)
if mibBuilder.loadTexts:batteryNumberOfCells.setStatus(_B)
_BatteryDesignCapacity_Type=Unsigned32
_BatteryDesignCapacity_Object=MibTableColumn
batteryDesignCapacity=_BatteryDesignCapacity_Object((1,3,6,1,2,1,233,1,1,1,7),_BatteryDesignCapacity_Type())
batteryDesignCapacity.setMaxAccess(_C)
if mibBuilder.loadTexts:batteryDesignCapacity.setStatus(_B)
if mibBuilder.loadTexts:batteryDesignCapacity.setUnits(_F)
_BatteryMaxChargingCurrent_Type=Unsigned32
_BatteryMaxChargingCurrent_Object=MibTableColumn
batteryMaxChargingCurrent=_BatteryMaxChargingCurrent_Object((1,3,6,1,2,1,233,1,1,1,8),_BatteryMaxChargingCurrent_Type())
batteryMaxChargingCurrent.setMaxAccess(_C)
if mibBuilder.loadTexts:batteryMaxChargingCurrent.setStatus(_B)
if mibBuilder.loadTexts:batteryMaxChargingCurrent.setUnits(_K)
_BatteryTrickleChargingCurrent_Type=Unsigned32
_BatteryTrickleChargingCurrent_Object=MibTableColumn
batteryTrickleChargingCurrent=_BatteryTrickleChargingCurrent_Object((1,3,6,1,2,1,233,1,1,1,9),_BatteryTrickleChargingCurrent_Type())
batteryTrickleChargingCurrent.setMaxAccess(_C)
if mibBuilder.loadTexts:batteryTrickleChargingCurrent.setStatus(_B)
if mibBuilder.loadTexts:batteryTrickleChargingCurrent.setUnits(_K)
_BatteryActualCapacity_Type=Unsigned32
_BatteryActualCapacity_Object=MibTableColumn
batteryActualCapacity=_BatteryActualCapacity_Object((1,3,6,1,2,1,233,1,1,1,10),_BatteryActualCapacity_Type())
batteryActualCapacity.setMaxAccess(_C)
if mibBuilder.loadTexts:batteryActualCapacity.setStatus(_B)
if mibBuilder.loadTexts:batteryActualCapacity.setUnits(_F)
_BatteryChargingCycleCount_Type=Unsigned32
_BatteryChargingCycleCount_Object=MibTableColumn
batteryChargingCycleCount=_BatteryChargingCycleCount_Object((1,3,6,1,2,1,233,1,1,1,11),_BatteryChargingCycleCount_Type())
batteryChargingCycleCount.setMaxAccess(_C)
if mibBuilder.loadTexts:batteryChargingCycleCount.setStatus(_B)
_BatteryLastChargingCycleTime_Type=DateAndTime
_BatteryLastChargingCycleTime_Object=MibTableColumn
batteryLastChargingCycleTime=_BatteryLastChargingCycleTime_Object((1,3,6,1,2,1,233,1,1,1,12),_BatteryLastChargingCycleTime_Type())
batteryLastChargingCycleTime.setMaxAccess(_C)
if mibBuilder.loadTexts:batteryLastChargingCycleTime.setStatus(_B)
class _BatteryChargingOperState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_T,1),('charging',2),('maintainingCharge',3),('noCharging',4),('discharging',5)))
_BatteryChargingOperState_Type.__name__=_G
_BatteryChargingOperState_Object=MibTableColumn
batteryChargingOperState=_BatteryChargingOperState_Object((1,3,6,1,2,1,233,1,1,1,13),_BatteryChargingOperState_Type())
batteryChargingOperState.setMaxAccess(_C)
if mibBuilder.loadTexts:batteryChargingOperState.setStatus(_B)
class _BatteryChargingAdminState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('notSet',1),('charge',2),('doNotCharge',3),('discharge',4)))
_BatteryChargingAdminState_Type.__name__=_G
_BatteryChargingAdminState_Object=MibTableColumn
batteryChargingAdminState=_BatteryChargingAdminState_Object((1,3,6,1,2,1,233,1,1,1,14),_BatteryChargingAdminState_Type())
batteryChargingAdminState.setMaxAccess(_D)
if mibBuilder.loadTexts:batteryChargingAdminState.setStatus(_B)
_BatteryActualCharge_Type=Unsigned32
_BatteryActualCharge_Object=MibTableColumn
batteryActualCharge=_BatteryActualCharge_Object((1,3,6,1,2,1,233,1,1,1,15),_BatteryActualCharge_Type())
batteryActualCharge.setMaxAccess(_C)
if mibBuilder.loadTexts:batteryActualCharge.setStatus(_B)
if mibBuilder.loadTexts:batteryActualCharge.setUnits(_F)
_BatteryActualVoltage_Type=Unsigned32
_BatteryActualVoltage_Object=MibTableColumn
batteryActualVoltage=_BatteryActualVoltage_Object((1,3,6,1,2,1,233,1,1,1,16),_BatteryActualVoltage_Type())
batteryActualVoltage.setMaxAccess(_C)
if mibBuilder.loadTexts:batteryActualVoltage.setStatus(_B)
if mibBuilder.loadTexts:batteryActualVoltage.setUnits(_J)
_BatteryActualCurrent_Type=Integer32
_BatteryActualCurrent_Object=MibTableColumn
batteryActualCurrent=_BatteryActualCurrent_Object((1,3,6,1,2,1,233,1,1,1,17),_BatteryActualCurrent_Type())
batteryActualCurrent.setMaxAccess(_C)
if mibBuilder.loadTexts:batteryActualCurrent.setStatus(_B)
if mibBuilder.loadTexts:batteryActualCurrent.setUnits(_K)
_BatteryTemperature_Type=Integer32
_BatteryTemperature_Object=MibTableColumn
batteryTemperature=_BatteryTemperature_Object((1,3,6,1,2,1,233,1,1,1,18),_BatteryTemperature_Type())
batteryTemperature.setMaxAccess(_C)
if mibBuilder.loadTexts:batteryTemperature.setStatus(_B)
if mibBuilder.loadTexts:batteryTemperature.setUnits(_L)
_BatteryAlarmLowCharge_Type=Unsigned32
_BatteryAlarmLowCharge_Object=MibTableColumn
batteryAlarmLowCharge=_BatteryAlarmLowCharge_Object((1,3,6,1,2,1,233,1,1,1,19),_BatteryAlarmLowCharge_Type())
batteryAlarmLowCharge.setMaxAccess(_D)
if mibBuilder.loadTexts:batteryAlarmLowCharge.setStatus(_B)
if mibBuilder.loadTexts:batteryAlarmLowCharge.setUnits(_F)
_BatteryAlarmLowVoltage_Type=Unsigned32
_BatteryAlarmLowVoltage_Object=MibTableColumn
batteryAlarmLowVoltage=_BatteryAlarmLowVoltage_Object((1,3,6,1,2,1,233,1,1,1,20),_BatteryAlarmLowVoltage_Type())
batteryAlarmLowVoltage.setMaxAccess(_D)
if mibBuilder.loadTexts:batteryAlarmLowVoltage.setStatus(_B)
if mibBuilder.loadTexts:batteryAlarmLowVoltage.setUnits(_J)
_BatteryAlarmLowCapacity_Type=Unsigned32
_BatteryAlarmLowCapacity_Object=MibTableColumn
batteryAlarmLowCapacity=_BatteryAlarmLowCapacity_Object((1,3,6,1,2,1,233,1,1,1,21),_BatteryAlarmLowCapacity_Type())
batteryAlarmLowCapacity.setMaxAccess(_D)
if mibBuilder.loadTexts:batteryAlarmLowCapacity.setStatus(_B)
if mibBuilder.loadTexts:batteryAlarmLowCapacity.setUnits(_F)
_BatteryAlarmHighCycleCount_Type=Unsigned32
_BatteryAlarmHighCycleCount_Object=MibTableColumn
batteryAlarmHighCycleCount=_BatteryAlarmHighCycleCount_Object((1,3,6,1,2,1,233,1,1,1,22),_BatteryAlarmHighCycleCount_Type())
batteryAlarmHighCycleCount.setMaxAccess(_D)
if mibBuilder.loadTexts:batteryAlarmHighCycleCount.setStatus(_B)
_BatteryAlarmHighTemperature_Type=Integer32
_BatteryAlarmHighTemperature_Object=MibTableColumn
batteryAlarmHighTemperature=_BatteryAlarmHighTemperature_Object((1,3,6,1,2,1,233,1,1,1,23),_BatteryAlarmHighTemperature_Type())
batteryAlarmHighTemperature.setMaxAccess(_D)
if mibBuilder.loadTexts:batteryAlarmHighTemperature.setStatus(_B)
if mibBuilder.loadTexts:batteryAlarmHighTemperature.setUnits(_L)
_BatteryAlarmLowTemperature_Type=Integer32
_BatteryAlarmLowTemperature_Object=MibTableColumn
batteryAlarmLowTemperature=_BatteryAlarmLowTemperature_Object((1,3,6,1,2,1,233,1,1,1,24),_BatteryAlarmLowTemperature_Type())
batteryAlarmLowTemperature.setMaxAccess(_D)
if mibBuilder.loadTexts:batteryAlarmLowTemperature.setStatus(_B)
if mibBuilder.loadTexts:batteryAlarmLowTemperature.setUnits(_L)
_BatteryCellIdentifier_Type=SnmpAdminString
_BatteryCellIdentifier_Object=MibTableColumn
batteryCellIdentifier=_BatteryCellIdentifier_Object((1,3,6,1,2,1,233,1,1,1,25),_BatteryCellIdentifier_Type())
batteryCellIdentifier.setMaxAccess(_C)
if mibBuilder.loadTexts:batteryCellIdentifier.setStatus(_B)
_BatteryConformance_ObjectIdentity=ObjectIdentity
batteryConformance=_BatteryConformance_ObjectIdentity((1,3,6,1,2,1,233,2))
_BatteryCompliances_ObjectIdentity=ObjectIdentity
batteryCompliances=_BatteryCompliances_ObjectIdentity((1,3,6,1,2,1,233,2,1))
_BatteryGroups_ObjectIdentity=ObjectIdentity
batteryGroups=_BatteryGroups_ObjectIdentity((1,3,6,1,2,1,233,2,2))
batteryDescriptionGroup=ObjectGroup((1,3,6,1,2,1,233,2,2,1))
batteryDescriptionGroup.setObjects(*((_A,_M),(_A,_U),(_A,_V),(_A,_W),(_A,_X),(_A,_Y),(_A,_Z),(_A,_a),(_A,_b)))
if mibBuilder.loadTexts:batteryDescriptionGroup.setStatus(_B)
batteryStatusGroup=ObjectGroup((1,3,6,1,2,1,233,2,2,2))
batteryStatusGroup.setObjects(*((_A,_N),(_A,_O),(_A,_c),(_A,_P),(_A,_H),(_A,_I),(_A,_d),(_A,_Q)))
if mibBuilder.loadTexts:batteryStatusGroup.setStatus(_B)
batteryAdminGroup=ObjectGroup((1,3,6,1,2,1,233,2,2,3))
batteryAdminGroup.setObjects((_A,_e))
if mibBuilder.loadTexts:batteryAdminGroup.setStatus(_B)
batteryAlarmThresholdsGroup=ObjectGroup((1,3,6,1,2,1,233,2,2,4))
batteryAlarmThresholdsGroup.setObjects(*((_A,_f),(_A,_g),(_A,_h),(_A,_i),(_A,_j),(_A,_k)))
if mibBuilder.loadTexts:batteryAlarmThresholdsGroup.setStatus(_B)
batteryPerCellNotificationsGroup=ObjectGroup((1,3,6,1,2,1,233,2,2,6))
batteryPerCellNotificationsGroup.setObjects((_A,_E))
if mibBuilder.loadTexts:batteryPerCellNotificationsGroup.setStatus(_B)
batteryChargingStateNotification=NotificationType((1,3,6,1,2,1,233,0,1))
batteryChargingStateNotification.setObjects((_A,_P))
if mibBuilder.loadTexts:batteryChargingStateNotification.setStatus(_B)
batteryLowNotification=NotificationType((1,3,6,1,2,1,233,0,2))
batteryLowNotification.setObjects(*((_A,_H),(_A,_I),(_A,_E)))
if mibBuilder.loadTexts:batteryLowNotification.setStatus(_B)
batteryCriticalNotification=NotificationType((1,3,6,1,2,1,233,0,3))
batteryCriticalNotification.setObjects(*((_A,_H),(_A,_I),(_A,_E)))
if mibBuilder.loadTexts:batteryCriticalNotification.setStatus(_B)
batteryTemperatureNotification=NotificationType((1,3,6,1,2,1,233,0,4))
batteryTemperatureNotification.setObjects(*((_A,_Q),(_A,_E)))
if mibBuilder.loadTexts:batteryTemperatureNotification.setStatus(_B)
batteryAgingNotification=NotificationType((1,3,6,1,2,1,233,0,5))
batteryAgingNotification.setObjects(*((_A,_N),(_A,_O),(_A,_E)))
if mibBuilder.loadTexts:batteryAgingNotification.setStatus(_B)
batteryConnectedNotification=NotificationType((1,3,6,1,2,1,233,0,6))
batteryConnectedNotification.setObjects((_A,_M))
if mibBuilder.loadTexts:batteryConnectedNotification.setStatus(_B)
batteryDisconnectedNotification=NotificationType((1,3,6,1,2,1,233,0,7))
if mibBuilder.loadTexts:batteryDisconnectedNotification.setStatus(_B)
batteryNotificationsGroup=NotificationGroup((1,3,6,1,2,1,233,2,2,5))
batteryNotificationsGroup.setObjects(*((_A,_l),(_A,_m),(_A,_n),(_A,_o),(_A,_p),(_A,_q),(_A,_r)))
if mibBuilder.loadTexts:batteryNotificationsGroup.setStatus(_B)
batteryCompliance=ModuleCompliance((1,3,6,1,2,1,233,2,1,1))
batteryCompliance.setObjects(*((_A,_s),(_A,_t),(_A,_u),(_A,_v),(_A,_w),(_A,_x)))
if mibBuilder.loadTexts:batteryCompliance.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'batteryMIB':batteryMIB,'batteryNotifications':batteryNotifications,_l:batteryChargingStateNotification,_m:batteryLowNotification,_n:batteryCriticalNotification,_p:batteryTemperatureNotification,_o:batteryAgingNotification,_q:batteryConnectedNotification,_r:batteryDisconnectedNotification,'batteryObjects':batteryObjects,'batteryTable':batteryTable,'batteryEntry':batteryEntry,_M:batteryIdentifier,_U:batteryFirmwareVersion,_V:batteryType,_W:batteryTechnology,_X:batteryDesignVoltage,_Y:batteryNumberOfCells,_Z:batteryDesignCapacity,_a:batteryMaxChargingCurrent,_b:batteryTrickleChargingCurrent,_N:batteryActualCapacity,_O:batteryChargingCycleCount,_c:batteryLastChargingCycleTime,_P:batteryChargingOperState,_e:batteryChargingAdminState,_H:batteryActualCharge,_I:batteryActualVoltage,_d:batteryActualCurrent,_Q:batteryTemperature,_f:batteryAlarmLowCharge,_g:batteryAlarmLowVoltage,_h:batteryAlarmLowCapacity,_i:batteryAlarmHighCycleCount,_j:batteryAlarmHighTemperature,_k:batteryAlarmLowTemperature,_E:batteryCellIdentifier,'batteryConformance':batteryConformance,'batteryCompliances':batteryCompliances,'batteryCompliance':batteryCompliance,'batteryGroups':batteryGroups,_s:batteryDescriptionGroup,_t:batteryStatusGroup,_x:batteryAdminGroup,_u:batteryAlarmThresholdsGroup,_v:batteryNotificationsGroup,_w:batteryPerCellNotificationsGroup})