_S='boxsTemperatureChangeEvent'
_R='notpowering'
_Q='powering'
_P='failed'
_O='operational'
_N='boxsItemStateChangeEvent'
_M='boxServicesTempSensorIndex'
_L='boxServicesPowSupplyIndex'
_K='notpresent'
_J='removable'
_I='fixed'
_H='boxServicesFansIndex'
_G='disable'
_F='enable'
_E='read-write'
_D='NETGEAR-BOXSERVICES-OLD-MIB'
_C='read-only'
_B='Integer32'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ng7000managedswitch,=mibBuilder.importSymbols('NETGEAR-REF-MIB','ng7000managedswitch')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_B,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
fastPathBoxServices=ModuleIdentity((1,3,6,1,4,1,4526,10,43))
if mibBuilder.loadTexts:fastPathBoxServices.setRevisions(('2008-02-22 00:00',))
_FastPathBoxServicesTraps_ObjectIdentity=ObjectIdentity
fastPathBoxServicesTraps=_FastPathBoxServicesTraps_ObjectIdentity((1,3,6,1,4,1,4526,10,43,0))
_BoxServicesGroup_ObjectIdentity=ObjectIdentity
boxServicesGroup=_BoxServicesGroup_ObjectIdentity((1,3,6,1,4,1,4526,10,43,1))
class _BoxServicesNormalTempRangeMin_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-100,100))
_BoxServicesNormalTempRangeMin_Type.__name__=_B
_BoxServicesNormalTempRangeMin_Object=MibScalar
boxServicesNormalTempRangeMin=_BoxServicesNormalTempRangeMin_Object((1,3,6,1,4,1,4526,10,43,1,1),_BoxServicesNormalTempRangeMin_Type())
boxServicesNormalTempRangeMin.setMaxAccess(_E)
if mibBuilder.loadTexts:boxServicesNormalTempRangeMin.setStatus(_A)
class _BoxServicesNormalTempRangeMax_Type(Integer32):defaultValue=45;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-100,100))
_BoxServicesNormalTempRangeMax_Type.__name__=_B
_BoxServicesNormalTempRangeMax_Object=MibScalar
boxServicesNormalTempRangeMax=_BoxServicesNormalTempRangeMax_Object((1,3,6,1,4,1,4526,10,43,1,2),_BoxServicesNormalTempRangeMax_Type())
boxServicesNormalTempRangeMax.setMaxAccess(_E)
if mibBuilder.loadTexts:boxServicesNormalTempRangeMax.setStatus(_A)
class _BoxServicesTemperatureTrapEnable_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_BoxServicesTemperatureTrapEnable_Type.__name__=_B
_BoxServicesTemperatureTrapEnable_Object=MibScalar
boxServicesTemperatureTrapEnable=_BoxServicesTemperatureTrapEnable_Object((1,3,6,1,4,1,4526,10,43,1,3),_BoxServicesTemperatureTrapEnable_Type())
boxServicesTemperatureTrapEnable.setMaxAccess(_E)
if mibBuilder.loadTexts:boxServicesTemperatureTrapEnable.setStatus(_A)
class _BoxServicesPSMStateTrapEnable_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_BoxServicesPSMStateTrapEnable_Type.__name__=_B
_BoxServicesPSMStateTrapEnable_Object=MibScalar
boxServicesPSMStateTrapEnable=_BoxServicesPSMStateTrapEnable_Object((1,3,6,1,4,1,4526,10,43,1,4),_BoxServicesPSMStateTrapEnable_Type())
boxServicesPSMStateTrapEnable.setMaxAccess(_E)
if mibBuilder.loadTexts:boxServicesPSMStateTrapEnable.setStatus(_A)
class _BoxServicesFanStateTrapEnable_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_BoxServicesFanStateTrapEnable_Type.__name__=_B
_BoxServicesFanStateTrapEnable_Object=MibScalar
boxServicesFanStateTrapEnable=_BoxServicesFanStateTrapEnable_Object((1,3,6,1,4,1,4526,10,43,1,5),_BoxServicesFanStateTrapEnable_Type())
boxServicesFanStateTrapEnable.setMaxAccess(_E)
if mibBuilder.loadTexts:boxServicesFanStateTrapEnable.setStatus(_A)
_BoxServicesFansTable_Object=MibTable
boxServicesFansTable=_BoxServicesFansTable_Object((1,3,6,1,4,1,4526,10,43,1,6))
if mibBuilder.loadTexts:boxServicesFansTable.setStatus(_A)
_BoxServicesFansEntry_Object=MibTableRow
boxServicesFansEntry=_BoxServicesFansEntry_Object((1,3,6,1,4,1,4526,10,43,1,6,1))
boxServicesFansEntry.setIndexNames((0,_D,_H))
if mibBuilder.loadTexts:boxServicesFansEntry.setStatus(_A)
class _BoxServicesFansIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_BoxServicesFansIndex_Type.__name__=_B
_BoxServicesFansIndex_Object=MibTableColumn
boxServicesFansIndex=_BoxServicesFansIndex_Object((1,3,6,1,4,1,4526,10,43,1,6,1,1),_BoxServicesFansIndex_Type())
boxServicesFansIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:boxServicesFansIndex.setStatus(_A)
class _BoxServicesFanItemType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_I,1),(_J,2)))
_BoxServicesFanItemType_Type.__name__=_B
_BoxServicesFanItemType_Object=MibTableColumn
boxServicesFanItemType=_BoxServicesFanItemType_Object((1,3,6,1,4,1,4526,10,43,1,6,1,2),_BoxServicesFanItemType_Type())
boxServicesFanItemType.setMaxAccess(_C)
if mibBuilder.loadTexts:boxServicesFanItemType.setStatus(_A)
class _BoxServicesFanItemState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_O,1),(_P,2),(_Q,3),(_R,4),(_K,5)))
_BoxServicesFanItemState_Type.__name__=_B
_BoxServicesFanItemState_Object=MibTableColumn
boxServicesFanItemState=_BoxServicesFanItemState_Object((1,3,6,1,4,1,4526,10,43,1,6,1,3),_BoxServicesFanItemState_Type())
boxServicesFanItemState.setMaxAccess(_C)
if mibBuilder.loadTexts:boxServicesFanItemState.setStatus(_A)
_BoxServicesFanSpeed_Type=Integer32
_BoxServicesFanSpeed_Object=MibTableColumn
boxServicesFanSpeed=_BoxServicesFanSpeed_Object((1,3,6,1,4,1,4526,10,43,1,6,1,4),_BoxServicesFanSpeed_Type())
boxServicesFanSpeed.setMaxAccess(_C)
if mibBuilder.loadTexts:boxServicesFanSpeed.setStatus(_A)
_BoxServicesFanDutyLevel_Type=Integer32
_BoxServicesFanDutyLevel_Object=MibTableColumn
boxServicesFanDutyLevel=_BoxServicesFanDutyLevel_Object((1,3,6,1,4,1,4526,10,43,1,6,1,5),_BoxServicesFanDutyLevel_Type())
boxServicesFanDutyLevel.setMaxAccess(_C)
if mibBuilder.loadTexts:boxServicesFanDutyLevel.setStatus(_A)
_BoxServicesPowSuppliesTable_Object=MibTable
boxServicesPowSuppliesTable=_BoxServicesPowSuppliesTable_Object((1,3,6,1,4,1,4526,10,43,1,7))
if mibBuilder.loadTexts:boxServicesPowSuppliesTable.setStatus(_A)
_BoxServicesPowSuppliesEntry_Object=MibTableRow
boxServicesPowSuppliesEntry=_BoxServicesPowSuppliesEntry_Object((1,3,6,1,4,1,4526,10,43,1,7,1))
boxServicesPowSuppliesEntry.setIndexNames((0,_D,_L))
if mibBuilder.loadTexts:boxServicesPowSuppliesEntry.setStatus(_A)
class _BoxServicesPowSupplyIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_BoxServicesPowSupplyIndex_Type.__name__=_B
_BoxServicesPowSupplyIndex_Object=MibTableColumn
boxServicesPowSupplyIndex=_BoxServicesPowSupplyIndex_Object((1,3,6,1,4,1,4526,10,43,1,7,1,1),_BoxServicesPowSupplyIndex_Type())
boxServicesPowSupplyIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:boxServicesPowSupplyIndex.setStatus(_A)
class _BoxServicesPowSupplyItemType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_I,1),(_J,2)))
_BoxServicesPowSupplyItemType_Type.__name__=_B
_BoxServicesPowSupplyItemType_Object=MibTableColumn
boxServicesPowSupplyItemType=_BoxServicesPowSupplyItemType_Object((1,3,6,1,4,1,4526,10,43,1,7,1,2),_BoxServicesPowSupplyItemType_Type())
boxServicesPowSupplyItemType.setMaxAccess(_C)
if mibBuilder.loadTexts:boxServicesPowSupplyItemType.setStatus(_A)
class _BoxServicesPowSupplyItemState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_O,1),(_P,2),(_Q,3),(_R,4),(_K,5)))
_BoxServicesPowSupplyItemState_Type.__name__=_B
_BoxServicesPowSupplyItemState_Object=MibTableColumn
boxServicesPowSupplyItemState=_BoxServicesPowSupplyItemState_Object((1,3,6,1,4,1,4526,10,43,1,7,1,3),_BoxServicesPowSupplyItemState_Type())
boxServicesPowSupplyItemState.setMaxAccess(_C)
if mibBuilder.loadTexts:boxServicesPowSupplyItemState.setStatus(_A)
_BoxServicesTempSensorsTable_Object=MibTable
boxServicesTempSensorsTable=_BoxServicesTempSensorsTable_Object((1,3,6,1,4,1,4526,10,43,1,8))
if mibBuilder.loadTexts:boxServicesTempSensorsTable.setStatus(_A)
_BoxServicesTempSensorsEntry_Object=MibTableRow
boxServicesTempSensorsEntry=_BoxServicesTempSensorsEntry_Object((1,3,6,1,4,1,4526,10,43,1,8,1))
boxServicesTempSensorsEntry.setIndexNames((0,_D,_M))
if mibBuilder.loadTexts:boxServicesTempSensorsEntry.setStatus(_A)
class _BoxServicesTempSensorIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_BoxServicesTempSensorIndex_Type.__name__=_B
_BoxServicesTempSensorIndex_Object=MibTableColumn
boxServicesTempSensorIndex=_BoxServicesTempSensorIndex_Object((1,3,6,1,4,1,4526,10,43,1,8,1,1),_BoxServicesTempSensorIndex_Type())
boxServicesTempSensorIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:boxServicesTempSensorIndex.setStatus(_A)
class _BoxServicesTempSensorType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_I,1),(_J,2)))
_BoxServicesTempSensorType_Type.__name__=_B
_BoxServicesTempSensorType_Object=MibTableColumn
boxServicesTempSensorType=_BoxServicesTempSensorType_Object((1,3,6,1,4,1,4526,10,43,1,8,1,2),_BoxServicesTempSensorType_Type())
boxServicesTempSensorType.setMaxAccess(_C)
if mibBuilder.loadTexts:boxServicesTempSensorType.setStatus(_A)
class _BoxServicesTempSensorState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*(('normal',1),('warning',2),('critical',3),('shutdown',4),(_K,5),('notoperational',6)))
_BoxServicesTempSensorState_Type.__name__=_B
_BoxServicesTempSensorState_Object=MibTableColumn
boxServicesTempSensorState=_BoxServicesTempSensorState_Object((1,3,6,1,4,1,4526,10,43,1,8,1,3),_BoxServicesTempSensorState_Type())
boxServicesTempSensorState.setMaxAccess(_C)
if mibBuilder.loadTexts:boxServicesTempSensorState.setStatus(_A)
_BoxServicesTempSensorTemperature_Type=Integer32
_BoxServicesTempSensorTemperature_Object=MibTableColumn
boxServicesTempSensorTemperature=_BoxServicesTempSensorTemperature_Object((1,3,6,1,4,1,4526,10,43,1,8,1,4),_BoxServicesTempSensorTemperature_Type())
boxServicesTempSensorTemperature.setMaxAccess(_C)
if mibBuilder.loadTexts:boxServicesTempSensorTemperature.setStatus(_A)
_BoxServicesCPLDCodeVersion_Type=Integer32
_BoxServicesCPLDCodeVersion_Object=MibScalar
boxServicesCPLDCodeVersion=_BoxServicesCPLDCodeVersion_Object((1,3,6,1,4,1,4526,10,43,1,9),_BoxServicesCPLDCodeVersion_Type())
boxServicesCPLDCodeVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:boxServicesCPLDCodeVersion.setStatus(_A)
_BoxServicesNotificationsGroup_ObjectIdentity=ObjectIdentity
boxServicesNotificationsGroup=_BoxServicesNotificationsGroup_ObjectIdentity((1,3,6,1,4,1,4526,10,43,2))
class _BoxsItemStateChangeEvent_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('insertion',1),('removal',2),('becomeoperational',3),('failure',4)))
_BoxsItemStateChangeEvent_Type.__name__=_B
_BoxsItemStateChangeEvent_Object=MibScalar
boxsItemStateChangeEvent=_BoxsItemStateChangeEvent_Object((1,3,6,1,4,1,4526,10,43,2,1),_BoxsItemStateChangeEvent_Type())
boxsItemStateChangeEvent.setMaxAccess(_C)
if mibBuilder.loadTexts:boxsItemStateChangeEvent.setStatus(_A)
class _BoxsTemperatureChangeEvent_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('abovethreshold',1),('belowthreshold',2),('withinnormalrange',3)))
_BoxsTemperatureChangeEvent_Type.__name__=_B
_BoxsTemperatureChangeEvent_Object=MibScalar
boxsTemperatureChangeEvent=_BoxsTemperatureChangeEvent_Object((1,3,6,1,4,1,4526,10,43,2,2),_BoxsTemperatureChangeEvent_Type())
boxsTemperatureChangeEvent.setMaxAccess(_C)
if mibBuilder.loadTexts:boxsTemperatureChangeEvent.setStatus(_A)
boxsFanStateChange=NotificationType((1,3,6,1,4,1,4526,10,43,0,1))
boxsFanStateChange.setObjects(*((_D,_H),(_D,_N)))
if mibBuilder.loadTexts:boxsFanStateChange.setStatus(_A)
boxsPowSupplyStateChange=NotificationType((1,3,6,1,4,1,4526,10,43,0,2))
boxsPowSupplyStateChange.setObjects(*((_D,_L),(_D,_N)))
if mibBuilder.loadTexts:boxsPowSupplyStateChange.setStatus(_A)
boxsTemperatureChange=NotificationType((1,3,6,1,4,1,4526,10,43,0,3))
boxsTemperatureChange.setObjects(*((_D,_M),(_D,_S)))
if mibBuilder.loadTexts:boxsTemperatureChange.setStatus(_A)
mibBuilder.exportSymbols(_D,**{'fastPathBoxServices':fastPathBoxServices,'fastPathBoxServicesTraps':fastPathBoxServicesTraps,'boxsFanStateChange':boxsFanStateChange,'boxsPowSupplyStateChange':boxsPowSupplyStateChange,'boxsTemperatureChange':boxsTemperatureChange,'boxServicesGroup':boxServicesGroup,'boxServicesNormalTempRangeMin':boxServicesNormalTempRangeMin,'boxServicesNormalTempRangeMax':boxServicesNormalTempRangeMax,'boxServicesTemperatureTrapEnable':boxServicesTemperatureTrapEnable,'boxServicesPSMStateTrapEnable':boxServicesPSMStateTrapEnable,'boxServicesFanStateTrapEnable':boxServicesFanStateTrapEnable,'boxServicesFansTable':boxServicesFansTable,'boxServicesFansEntry':boxServicesFansEntry,_H:boxServicesFansIndex,'boxServicesFanItemType':boxServicesFanItemType,'boxServicesFanItemState':boxServicesFanItemState,'boxServicesFanSpeed':boxServicesFanSpeed,'boxServicesFanDutyLevel':boxServicesFanDutyLevel,'boxServicesPowSuppliesTable':boxServicesPowSuppliesTable,'boxServicesPowSuppliesEntry':boxServicesPowSuppliesEntry,_L:boxServicesPowSupplyIndex,'boxServicesPowSupplyItemType':boxServicesPowSupplyItemType,'boxServicesPowSupplyItemState':boxServicesPowSupplyItemState,'boxServicesTempSensorsTable':boxServicesTempSensorsTable,'boxServicesTempSensorsEntry':boxServicesTempSensorsEntry,_M:boxServicesTempSensorIndex,'boxServicesTempSensorType':boxServicesTempSensorType,'boxServicesTempSensorState':boxServicesTempSensorState,'boxServicesTempSensorTemperature':boxServicesTempSensorTemperature,'boxServicesCPLDCodeVersion':boxServicesCPLDCodeVersion,'boxServicesNotificationsGroup':boxServicesNotificationsGroup,_N:boxsItemStateChangeEvent,_S:boxsTemperatureChangeEvent})