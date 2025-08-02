_T='arubaWiredTempSensorTableGroup'
_S='arubaWiredTempSensorNotificationsGroup'
_R='arubaWiredTempSensorTable'
_Q='arubaWiredTempSensorStateNotification'
_P='arubaWiredTempSensorMaxTemp'
_O='arubaWiredTempSensorMinTemp'
_N='arubaWiredTempSensorTemperature'
_M='arubaWiredTempSensorIndex'
_L='arubaWiredTempSensorSlotIndex'
_K='arubaWiredTempSensorSlotTypeIndex'
_J='arubaWiredTempSensorGroupIndex'
_I='arubaWiredTempSensorState'
_H='arubaWiredTempSensorName'
_G='millidegrees Celsius'
_F='DisplayString'
_E='not-accessible'
_D='read-only'
_C='Integer32'
_B='current'
_A='ARUBAWIRED-TEMPSENSOR-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
arubaWiredChassisMIB,=mibBuilder.importSymbols('ARUBAWIRED-CHASSIS-MIB','arubaWiredChassisMIB')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_F,'PhysAddress','TextualConvention')
arubaWiredTempSensor=ModuleIdentity((1,3,6,1,4,1,47196,4,1,1,3,11,3))
if mibBuilder.loadTexts:arubaWiredTempSensor.setRevisions(('2020-02-13 00:00',))
_ArubaWiredTempSensorNotifications_ObjectIdentity=ObjectIdentity
arubaWiredTempSensorNotifications=_ArubaWiredTempSensorNotifications_ObjectIdentity((1,3,6,1,4,1,47196,4,1,1,3,11,3,0))
_ArubaWiredTempSensorTable_Object=MibTable
arubaWiredTempSensorTable=_ArubaWiredTempSensorTable_Object((1,3,6,1,4,1,47196,4,1,1,3,11,3,1))
if mibBuilder.loadTexts:arubaWiredTempSensorTable.setStatus(_B)
_ArubaWiredTempSensorEntry_Object=MibTableRow
arubaWiredTempSensorEntry=_ArubaWiredTempSensorEntry_Object((1,3,6,1,4,1,47196,4,1,1,3,11,3,1,1))
arubaWiredTempSensorEntry.setIndexNames((0,_A,_J),(0,_A,_K),(0,_A,_L),(0,_A,_M))
if mibBuilder.loadTexts:arubaWiredTempSensorEntry.setStatus(_B)
class _ArubaWiredTempSensorGroupIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_ArubaWiredTempSensorGroupIndex_Type.__name__=_C
_ArubaWiredTempSensorGroupIndex_Object=MibTableColumn
arubaWiredTempSensorGroupIndex=_ArubaWiredTempSensorGroupIndex_Object((1,3,6,1,4,1,47196,4,1,1,3,11,3,1,1,1),_ArubaWiredTempSensorGroupIndex_Type())
arubaWiredTempSensorGroupIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:arubaWiredTempSensorGroupIndex.setStatus(_B)
class _ArubaWiredTempSensorSlotTypeIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_ArubaWiredTempSensorSlotTypeIndex_Type.__name__=_C
_ArubaWiredTempSensorSlotTypeIndex_Object=MibTableColumn
arubaWiredTempSensorSlotTypeIndex=_ArubaWiredTempSensorSlotTypeIndex_Object((1,3,6,1,4,1,47196,4,1,1,3,11,3,1,1,2),_ArubaWiredTempSensorSlotTypeIndex_Type())
arubaWiredTempSensorSlotTypeIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:arubaWiredTempSensorSlotTypeIndex.setStatus(_B)
class _ArubaWiredTempSensorSlotIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_ArubaWiredTempSensorSlotIndex_Type.__name__=_C
_ArubaWiredTempSensorSlotIndex_Object=MibTableColumn
arubaWiredTempSensorSlotIndex=_ArubaWiredTempSensorSlotIndex_Object((1,3,6,1,4,1,47196,4,1,1,3,11,3,1,1,3),_ArubaWiredTempSensorSlotIndex_Type())
arubaWiredTempSensorSlotIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:arubaWiredTempSensorSlotIndex.setStatus(_B)
class _ArubaWiredTempSensorIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_ArubaWiredTempSensorIndex_Type.__name__=_C
_ArubaWiredTempSensorIndex_Object=MibTableColumn
arubaWiredTempSensorIndex=_ArubaWiredTempSensorIndex_Object((1,3,6,1,4,1,47196,4,1,1,3,11,3,1,1,4),_ArubaWiredTempSensorIndex_Type())
arubaWiredTempSensorIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:arubaWiredTempSensorIndex.setStatus(_B)
class _ArubaWiredTempSensorName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,40))
_ArubaWiredTempSensorName_Type.__name__=_F
_ArubaWiredTempSensorName_Object=MibTableColumn
arubaWiredTempSensorName=_ArubaWiredTempSensorName_Object((1,3,6,1,4,1,47196,4,1,1,3,11,3,1,1,5),_ArubaWiredTempSensorName_Type())
arubaWiredTempSensorName.setMaxAccess(_D)
if mibBuilder.loadTexts:arubaWiredTempSensorName.setStatus(_B)
class _ArubaWiredTempSensorState_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,20))
_ArubaWiredTempSensorState_Type.__name__=_F
_ArubaWiredTempSensorState_Object=MibTableColumn
arubaWiredTempSensorState=_ArubaWiredTempSensorState_Object((1,3,6,1,4,1,47196,4,1,1,3,11,3,1,1,6),_ArubaWiredTempSensorState_Type())
arubaWiredTempSensorState.setMaxAccess(_D)
if mibBuilder.loadTexts:arubaWiredTempSensorState.setStatus(_B)
_ArubaWiredTempSensorTemperature_Type=Integer32
_ArubaWiredTempSensorTemperature_Object=MibTableColumn
arubaWiredTempSensorTemperature=_ArubaWiredTempSensorTemperature_Object((1,3,6,1,4,1,47196,4,1,1,3,11,3,1,1,7),_ArubaWiredTempSensorTemperature_Type())
arubaWiredTempSensorTemperature.setMaxAccess(_D)
if mibBuilder.loadTexts:arubaWiredTempSensorTemperature.setStatus(_B)
if mibBuilder.loadTexts:arubaWiredTempSensorTemperature.setUnits(_G)
_ArubaWiredTempSensorMinTemp_Type=Integer32
_ArubaWiredTempSensorMinTemp_Object=MibTableColumn
arubaWiredTempSensorMinTemp=_ArubaWiredTempSensorMinTemp_Object((1,3,6,1,4,1,47196,4,1,1,3,11,3,1,1,8),_ArubaWiredTempSensorMinTemp_Type())
arubaWiredTempSensorMinTemp.setMaxAccess(_D)
if mibBuilder.loadTexts:arubaWiredTempSensorMinTemp.setStatus(_B)
if mibBuilder.loadTexts:arubaWiredTempSensorMinTemp.setUnits(_G)
_ArubaWiredTempSensorMaxTemp_Type=Integer32
_ArubaWiredTempSensorMaxTemp_Object=MibTableColumn
arubaWiredTempSensorMaxTemp=_ArubaWiredTempSensorMaxTemp_Object((1,3,6,1,4,1,47196,4,1,1,3,11,3,1,1,9),_ArubaWiredTempSensorMaxTemp_Type())
arubaWiredTempSensorMaxTemp.setMaxAccess(_D)
if mibBuilder.loadTexts:arubaWiredTempSensorMaxTemp.setStatus(_B)
if mibBuilder.loadTexts:arubaWiredTempSensorMaxTemp.setUnits(_G)
_ArubaWiredTempSensorConformance_ObjectIdentity=ObjectIdentity
arubaWiredTempSensorConformance=_ArubaWiredTempSensorConformance_ObjectIdentity((1,3,6,1,4,1,47196,4,1,1,3,11,3,99))
_ArubaWiredTempSensorCompliances_ObjectIdentity=ObjectIdentity
arubaWiredTempSensorCompliances=_ArubaWiredTempSensorCompliances_ObjectIdentity((1,3,6,1,4,1,47196,4,1,1,3,11,3,99,1))
_ArubaWiredTempSensorGroups_ObjectIdentity=ObjectIdentity
arubaWiredTempSensorGroups=_ArubaWiredTempSensorGroups_ObjectIdentity((1,3,6,1,4,1,47196,4,1,1,3,11,3,99,2))
arubaWiredTempSensorTableGroup=ObjectGroup((1,3,6,1,4,1,47196,4,1,1,3,11,3,99,2,1))
arubaWiredTempSensorTableGroup.setObjects(*((_A,_H),(_A,_I),(_A,_N),(_A,_O),(_A,_P)))
if mibBuilder.loadTexts:arubaWiredTempSensorTableGroup.setStatus(_B)
arubaWiredTempSensorStateNotification=NotificationType((1,3,6,1,4,1,47196,4,1,1,3,11,3,0,1))
arubaWiredTempSensorStateNotification.setObjects(*((_A,_H),(_A,_I)))
if mibBuilder.loadTexts:arubaWiredTempSensorStateNotification.setStatus(_B)
arubaWiredTempSensorNotificationsGroup=NotificationGroup((1,3,6,1,4,1,47196,4,1,1,3,11,3,99,2,2))
arubaWiredTempSensorNotificationsGroup.setObjects((_A,_Q))
if mibBuilder.loadTexts:arubaWiredTempSensorNotificationsGroup.setStatus(_B)
arubaWiredTempSensorCompliance=ModuleCompliance((1,3,6,1,4,1,47196,4,1,1,3,11,3,99,1,1))
arubaWiredTempSensorCompliance.setObjects(*((_A,_R),(_A,_S),(_A,_T)))
if mibBuilder.loadTexts:arubaWiredTempSensorCompliance.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'arubaWiredTempSensor':arubaWiredTempSensor,'arubaWiredTempSensorNotifications':arubaWiredTempSensorNotifications,_Q:arubaWiredTempSensorStateNotification,_R:arubaWiredTempSensorTable,'arubaWiredTempSensorEntry':arubaWiredTempSensorEntry,_J:arubaWiredTempSensorGroupIndex,_K:arubaWiredTempSensorSlotTypeIndex,_L:arubaWiredTempSensorSlotIndex,_M:arubaWiredTempSensorIndex,_H:arubaWiredTempSensorName,_I:arubaWiredTempSensorState,_N:arubaWiredTempSensorTemperature,_O:arubaWiredTempSensorMinTemp,_P:arubaWiredTempSensorMaxTemp,'arubaWiredTempSensorConformance':arubaWiredTempSensorConformance,'arubaWiredTempSensorCompliances':arubaWiredTempSensorCompliances,'arubaWiredTempSensorCompliance':arubaWiredTempSensorCompliance,'arubaWiredTempSensorGroups':arubaWiredTempSensorGroups,_T:arubaWiredTempSensorTableGroup,_S:arubaWiredTempSensorNotificationsGroup})