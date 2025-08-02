_X='boxsTemperatureChangeEvent'
_W='boxServicesStackTempSensorIndex'
_V='boxServicesUnitIndex'
_U='notoperational'
_T='shutdown'
_S='critical'
_R='warning'
_Q='normal'
_P='failed'
_O='operational'
_N='boxsItemStateChangeEvent'
_M='boxServicesTempSensorIndex'
_L='boxServicesPowSupplyIndex'
_K='boxServicesFansIndex'
_J='disable'
_I='enable'
_H='notpresent'
_G='removable'
_F='fixed'
_E='read-write'
_D='FASTPATH-BOXSERVICES-PRIVATE-MIB'
_C='read-only'
_B='Integer32'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
fastPath,=mibBuilder.importSymbols('BROADCOM-REF-MIB','fastPath')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_B,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
fastPathBoxServices=ModuleIdentity((1,3,6,1,4,1,4413,1,1,43))
if mibBuilder.loadTexts:fastPathBoxServices.setRevisions(('2008-02-22 00:00',))
_FastPathBoxServicesTraps_ObjectIdentity=ObjectIdentity
fastPathBoxServicesTraps=_FastPathBoxServicesTraps_ObjectIdentity((1,3,6,1,4,1,4413,1,1,43,0))
_BoxServicesGroup_ObjectIdentity=ObjectIdentity
boxServicesGroup=_BoxServicesGroup_ObjectIdentity((1,3,6,1,4,1,4413,1,1,43,1))
class _BoxServicesNormalTempRangeMin_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-100,100))
_BoxServicesNormalTempRangeMin_Type.__name__=_B
_BoxServicesNormalTempRangeMin_Object=MibScalar
boxServicesNormalTempRangeMin=_BoxServicesNormalTempRangeMin_Object((1,3,6,1,4,1,4413,1,1,43,1,1),_BoxServicesNormalTempRangeMin_Type())
boxServicesNormalTempRangeMin.setMaxAccess(_E)
if mibBuilder.loadTexts:boxServicesNormalTempRangeMin.setStatus(_A)
class _BoxServicesNormalTempRangeMax_Type(Integer32):defaultValue=45;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-100,100))
_BoxServicesNormalTempRangeMax_Type.__name__=_B
_BoxServicesNormalTempRangeMax_Object=MibScalar
boxServicesNormalTempRangeMax=_BoxServicesNormalTempRangeMax_Object((1,3,6,1,4,1,4413,1,1,43,1,2),_BoxServicesNormalTempRangeMax_Type())
boxServicesNormalTempRangeMax.setMaxAccess(_E)
if mibBuilder.loadTexts:boxServicesNormalTempRangeMax.setStatus(_A)
class _BoxServicesTemperatureTrapEnable_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_I,1),(_J,2)))
_BoxServicesTemperatureTrapEnable_Type.__name__=_B
_BoxServicesTemperatureTrapEnable_Object=MibScalar
boxServicesTemperatureTrapEnable=_BoxServicesTemperatureTrapEnable_Object((1,3,6,1,4,1,4413,1,1,43,1,3),_BoxServicesTemperatureTrapEnable_Type())
boxServicesTemperatureTrapEnable.setMaxAccess(_E)
if mibBuilder.loadTexts:boxServicesTemperatureTrapEnable.setStatus(_A)
class _BoxServicesPSMStateTrapEnable_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_I,1),(_J,2)))
_BoxServicesPSMStateTrapEnable_Type.__name__=_B
_BoxServicesPSMStateTrapEnable_Object=MibScalar
boxServicesPSMStateTrapEnable=_BoxServicesPSMStateTrapEnable_Object((1,3,6,1,4,1,4413,1,1,43,1,4),_BoxServicesPSMStateTrapEnable_Type())
boxServicesPSMStateTrapEnable.setMaxAccess(_E)
if mibBuilder.loadTexts:boxServicesPSMStateTrapEnable.setStatus(_A)
class _BoxServicesFanStateTrapEnable_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_I,1),(_J,2)))
_BoxServicesFanStateTrapEnable_Type.__name__=_B
_BoxServicesFanStateTrapEnable_Object=MibScalar
boxServicesFanStateTrapEnable=_BoxServicesFanStateTrapEnable_Object((1,3,6,1,4,1,4413,1,1,43,1,5),_BoxServicesFanStateTrapEnable_Type())
boxServicesFanStateTrapEnable.setMaxAccess(_E)
if mibBuilder.loadTexts:boxServicesFanStateTrapEnable.setStatus(_A)
_BoxServicesFansTable_Object=MibTable
boxServicesFansTable=_BoxServicesFansTable_Object((1,3,6,1,4,1,4413,1,1,43,1,6))
if mibBuilder.loadTexts:boxServicesFansTable.setStatus(_A)
_BoxServicesFansEntry_Object=MibTableRow
boxServicesFansEntry=_BoxServicesFansEntry_Object((1,3,6,1,4,1,4413,1,1,43,1,6,1))
boxServicesFansEntry.setIndexNames((0,_D,_K))
if mibBuilder.loadTexts:boxServicesFansEntry.setStatus(_A)
class _BoxServicesFansIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_BoxServicesFansIndex_Type.__name__=_B
_BoxServicesFansIndex_Object=MibTableColumn
boxServicesFansIndex=_BoxServicesFansIndex_Object((1,3,6,1,4,1,4413,1,1,43,1,6,1,1),_BoxServicesFansIndex_Type())
boxServicesFansIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:boxServicesFansIndex.setStatus(_A)
class _BoxServicesFanItemType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_BoxServicesFanItemType_Type.__name__=_B
_BoxServicesFanItemType_Object=MibTableColumn
boxServicesFanItemType=_BoxServicesFanItemType_Object((1,3,6,1,4,1,4413,1,1,43,1,6,1,2),_BoxServicesFanItemType_Type())
boxServicesFanItemType.setMaxAccess(_C)
if mibBuilder.loadTexts:boxServicesFanItemType.setStatus(_A)
class _BoxServicesFanItemState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_H,1),(_O,2),(_P,3)))
_BoxServicesFanItemState_Type.__name__=_B
_BoxServicesFanItemState_Object=MibTableColumn
boxServicesFanItemState=_BoxServicesFanItemState_Object((1,3,6,1,4,1,4413,1,1,43,1,6,1,3),_BoxServicesFanItemState_Type())
boxServicesFanItemState.setMaxAccess(_C)
if mibBuilder.loadTexts:boxServicesFanItemState.setStatus(_A)
_BoxServicesFanSpeed_Type=Integer32
_BoxServicesFanSpeed_Object=MibTableColumn
boxServicesFanSpeed=_BoxServicesFanSpeed_Object((1,3,6,1,4,1,4413,1,1,43,1,6,1,4),_BoxServicesFanSpeed_Type())
boxServicesFanSpeed.setMaxAccess(_C)
if mibBuilder.loadTexts:boxServicesFanSpeed.setStatus(_A)
_BoxServicesFanDutyLevel_Type=Integer32
_BoxServicesFanDutyLevel_Object=MibTableColumn
boxServicesFanDutyLevel=_BoxServicesFanDutyLevel_Object((1,3,6,1,4,1,4413,1,1,43,1,6,1,5),_BoxServicesFanDutyLevel_Type())
boxServicesFanDutyLevel.setMaxAccess(_C)
if mibBuilder.loadTexts:boxServicesFanDutyLevel.setStatus(_A)
_BoxServicesPowSuppliesTable_Object=MibTable
boxServicesPowSuppliesTable=_BoxServicesPowSuppliesTable_Object((1,3,6,1,4,1,4413,1,1,43,1,7))
if mibBuilder.loadTexts:boxServicesPowSuppliesTable.setStatus(_A)
_BoxServicesPowSuppliesEntry_Object=MibTableRow
boxServicesPowSuppliesEntry=_BoxServicesPowSuppliesEntry_Object((1,3,6,1,4,1,4413,1,1,43,1,7,1))
boxServicesPowSuppliesEntry.setIndexNames((0,_D,_L))
if mibBuilder.loadTexts:boxServicesPowSuppliesEntry.setStatus(_A)
class _BoxServicesPowSupplyIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_BoxServicesPowSupplyIndex_Type.__name__=_B
_BoxServicesPowSupplyIndex_Object=MibTableColumn
boxServicesPowSupplyIndex=_BoxServicesPowSupplyIndex_Object((1,3,6,1,4,1,4413,1,1,43,1,7,1,1),_BoxServicesPowSupplyIndex_Type())
boxServicesPowSupplyIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:boxServicesPowSupplyIndex.setStatus(_A)
class _BoxServicesPowSupplyItemType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_BoxServicesPowSupplyItemType_Type.__name__=_B
_BoxServicesPowSupplyItemType_Object=MibTableColumn
boxServicesPowSupplyItemType=_BoxServicesPowSupplyItemType_Object((1,3,6,1,4,1,4413,1,1,43,1,7,1,2),_BoxServicesPowSupplyItemType_Type())
boxServicesPowSupplyItemType.setMaxAccess(_C)
if mibBuilder.loadTexts:boxServicesPowSupplyItemType.setStatus(_A)
class _BoxServicesPowSupplyItemState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_H,1),(_O,2),(_P,3)))
_BoxServicesPowSupplyItemState_Type.__name__=_B
_BoxServicesPowSupplyItemState_Object=MibTableColumn
boxServicesPowSupplyItemState=_BoxServicesPowSupplyItemState_Object((1,3,6,1,4,1,4413,1,1,43,1,7,1,3),_BoxServicesPowSupplyItemState_Type())
boxServicesPowSupplyItemState.setMaxAccess(_C)
if mibBuilder.loadTexts:boxServicesPowSupplyItemState.setStatus(_A)
_BoxServicesTempSensorsTable_Object=MibTable
boxServicesTempSensorsTable=_BoxServicesTempSensorsTable_Object((1,3,6,1,4,1,4413,1,1,43,1,8))
if mibBuilder.loadTexts:boxServicesTempSensorsTable.setStatus('obsolete')
_BoxServicesTempSensorsEntry_Object=MibTableRow
boxServicesTempSensorsEntry=_BoxServicesTempSensorsEntry_Object((1,3,6,1,4,1,4413,1,1,43,1,8,1))
boxServicesTempSensorsEntry.setIndexNames((0,_D,_M))
if mibBuilder.loadTexts:boxServicesTempSensorsEntry.setStatus(_A)
class _BoxServicesTempSensorIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_BoxServicesTempSensorIndex_Type.__name__=_B
_BoxServicesTempSensorIndex_Object=MibTableColumn
boxServicesTempSensorIndex=_BoxServicesTempSensorIndex_Object((1,3,6,1,4,1,4413,1,1,43,1,8,1,1),_BoxServicesTempSensorIndex_Type())
boxServicesTempSensorIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:boxServicesTempSensorIndex.setStatus(_A)
class _BoxServicesTempSensorType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_BoxServicesTempSensorType_Type.__name__=_B
_BoxServicesTempSensorType_Object=MibTableColumn
boxServicesTempSensorType=_BoxServicesTempSensorType_Object((1,3,6,1,4,1,4413,1,1,43,1,8,1,2),_BoxServicesTempSensorType_Type())
boxServicesTempSensorType.setMaxAccess(_C)
if mibBuilder.loadTexts:boxServicesTempSensorType.setStatus(_A)
class _BoxServicesTempSensorState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*((_Q,1),(_R,2),(_S,3),(_T,4),(_H,5),(_U,6)))
_BoxServicesTempSensorState_Type.__name__=_B
_BoxServicesTempSensorState_Object=MibTableColumn
boxServicesTempSensorState=_BoxServicesTempSensorState_Object((1,3,6,1,4,1,4413,1,1,43,1,8,1,3),_BoxServicesTempSensorState_Type())
boxServicesTempSensorState.setMaxAccess(_C)
if mibBuilder.loadTexts:boxServicesTempSensorState.setStatus(_A)
_BoxServicesTempSensorTemperature_Type=Integer32
_BoxServicesTempSensorTemperature_Object=MibTableColumn
boxServicesTempSensorTemperature=_BoxServicesTempSensorTemperature_Object((1,3,6,1,4,1,4413,1,1,43,1,8,1,4),_BoxServicesTempSensorTemperature_Type())
boxServicesTempSensorTemperature.setMaxAccess(_C)
if mibBuilder.loadTexts:boxServicesTempSensorTemperature.setStatus(_A)
_BoxServicesStackTempSensorsTable_Object=MibTable
boxServicesStackTempSensorsTable=_BoxServicesStackTempSensorsTable_Object((1,3,6,1,4,1,4413,1,1,43,1,9))
if mibBuilder.loadTexts:boxServicesStackTempSensorsTable.setStatus(_A)
_BoxServicesStackTempSensorsEntry_Object=MibTableRow
boxServicesStackTempSensorsEntry=_BoxServicesStackTempSensorsEntry_Object((1,3,6,1,4,1,4413,1,1,43,1,9,1))
boxServicesStackTempSensorsEntry.setIndexNames((0,_D,_V),(0,_D,_W))
if mibBuilder.loadTexts:boxServicesStackTempSensorsEntry.setStatus(_A)
class _BoxServicesUnitIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,8))
_BoxServicesUnitIndex_Type.__name__=_B
_BoxServicesUnitIndex_Object=MibTableColumn
boxServicesUnitIndex=_BoxServicesUnitIndex_Object((1,3,6,1,4,1,4413,1,1,43,1,9,1,1),_BoxServicesUnitIndex_Type())
boxServicesUnitIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:boxServicesUnitIndex.setStatus(_A)
class _BoxServicesStackTempSensorIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_BoxServicesStackTempSensorIndex_Type.__name__=_B
_BoxServicesStackTempSensorIndex_Object=MibTableColumn
boxServicesStackTempSensorIndex=_BoxServicesStackTempSensorIndex_Object((1,3,6,1,4,1,4413,1,1,43,1,9,1,2),_BoxServicesStackTempSensorIndex_Type())
boxServicesStackTempSensorIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:boxServicesStackTempSensorIndex.setStatus(_A)
class _BoxServicesStackTempSensorType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_BoxServicesStackTempSensorType_Type.__name__=_B
_BoxServicesStackTempSensorType_Object=MibTableColumn
boxServicesStackTempSensorType=_BoxServicesStackTempSensorType_Object((1,3,6,1,4,1,4413,1,1,43,1,9,1,3),_BoxServicesStackTempSensorType_Type())
boxServicesStackTempSensorType.setMaxAccess(_C)
if mibBuilder.loadTexts:boxServicesStackTempSensorType.setStatus(_A)
class _BoxServicesStackTempSensorState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*((_Q,1),(_R,2),(_S,3),(_T,4),(_H,5),(_U,6)))
_BoxServicesStackTempSensorState_Type.__name__=_B
_BoxServicesStackTempSensorState_Object=MibTableColumn
boxServicesStackTempSensorState=_BoxServicesStackTempSensorState_Object((1,3,6,1,4,1,4413,1,1,43,1,9,1,4),_BoxServicesStackTempSensorState_Type())
boxServicesStackTempSensorState.setMaxAccess(_C)
if mibBuilder.loadTexts:boxServicesStackTempSensorState.setStatus(_A)
_BoxServicesStackTempSensorTemperature_Type=Integer32
_BoxServicesStackTempSensorTemperature_Object=MibTableColumn
boxServicesStackTempSensorTemperature=_BoxServicesStackTempSensorTemperature_Object((1,3,6,1,4,1,4413,1,1,43,1,9,1,5),_BoxServicesStackTempSensorTemperature_Type())
boxServicesStackTempSensorTemperature.setMaxAccess(_C)
if mibBuilder.loadTexts:boxServicesStackTempSensorTemperature.setStatus(_A)
_BoxServicesNotificationsGroup_ObjectIdentity=ObjectIdentity
boxServicesNotificationsGroup=_BoxServicesNotificationsGroup_ObjectIdentity((1,3,6,1,4,1,4413,1,1,43,2))
class _BoxsItemStateChangeEvent_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('insertion',1),('removal',2),('becomeoperational',3),('failure',4)))
_BoxsItemStateChangeEvent_Type.__name__=_B
_BoxsItemStateChangeEvent_Object=MibScalar
boxsItemStateChangeEvent=_BoxsItemStateChangeEvent_Object((1,3,6,1,4,1,4413,1,1,43,2,1),_BoxsItemStateChangeEvent_Type())
boxsItemStateChangeEvent.setMaxAccess(_C)
if mibBuilder.loadTexts:boxsItemStateChangeEvent.setStatus(_A)
class _BoxsTemperatureChangeEvent_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('abovethreshold',1),('belowthreshold',2),('withinnormalrange',3)))
_BoxsTemperatureChangeEvent_Type.__name__=_B
_BoxsTemperatureChangeEvent_Object=MibScalar
boxsTemperatureChangeEvent=_BoxsTemperatureChangeEvent_Object((1,3,6,1,4,1,4413,1,1,43,2,2),_BoxsTemperatureChangeEvent_Type())
boxsTemperatureChangeEvent.setMaxAccess(_C)
if mibBuilder.loadTexts:boxsTemperatureChangeEvent.setStatus(_A)
boxsFanStateChange=NotificationType((1,3,6,1,4,1,4413,1,1,43,0,1))
boxsFanStateChange.setObjects(*((_D,_K),(_D,_N)))
if mibBuilder.loadTexts:boxsFanStateChange.setStatus(_A)
boxsPowSupplyStateChange=NotificationType((1,3,6,1,4,1,4413,1,1,43,0,2))
boxsPowSupplyStateChange.setObjects(*((_D,_L),(_D,_N)))
if mibBuilder.loadTexts:boxsPowSupplyStateChange.setStatus(_A)
boxsTemperatureChange=NotificationType((1,3,6,1,4,1,4413,1,1,43,0,3))
boxsTemperatureChange.setObjects(*((_D,_M),(_D,_X)))
if mibBuilder.loadTexts:boxsTemperatureChange.setStatus(_A)
mibBuilder.exportSymbols(_D,**{'fastPathBoxServices':fastPathBoxServices,'fastPathBoxServicesTraps':fastPathBoxServicesTraps,'boxsFanStateChange':boxsFanStateChange,'boxsPowSupplyStateChange':boxsPowSupplyStateChange,'boxsTemperatureChange':boxsTemperatureChange,'boxServicesGroup':boxServicesGroup,'boxServicesNormalTempRangeMin':boxServicesNormalTempRangeMin,'boxServicesNormalTempRangeMax':boxServicesNormalTempRangeMax,'boxServicesTemperatureTrapEnable':boxServicesTemperatureTrapEnable,'boxServicesPSMStateTrapEnable':boxServicesPSMStateTrapEnable,'boxServicesFanStateTrapEnable':boxServicesFanStateTrapEnable,'boxServicesFansTable':boxServicesFansTable,'boxServicesFansEntry':boxServicesFansEntry,_K:boxServicesFansIndex,'boxServicesFanItemType':boxServicesFanItemType,'boxServicesFanItemState':boxServicesFanItemState,'boxServicesFanSpeed':boxServicesFanSpeed,'boxServicesFanDutyLevel':boxServicesFanDutyLevel,'boxServicesPowSuppliesTable':boxServicesPowSuppliesTable,'boxServicesPowSuppliesEntry':boxServicesPowSuppliesEntry,_L:boxServicesPowSupplyIndex,'boxServicesPowSupplyItemType':boxServicesPowSupplyItemType,'boxServicesPowSupplyItemState':boxServicesPowSupplyItemState,'boxServicesTempSensorsTable':boxServicesTempSensorsTable,'boxServicesTempSensorsEntry':boxServicesTempSensorsEntry,_M:boxServicesTempSensorIndex,'boxServicesTempSensorType':boxServicesTempSensorType,'boxServicesTempSensorState':boxServicesTempSensorState,'boxServicesTempSensorTemperature':boxServicesTempSensorTemperature,'boxServicesStackTempSensorsTable':boxServicesStackTempSensorsTable,'boxServicesStackTempSensorsEntry':boxServicesStackTempSensorsEntry,_V:boxServicesUnitIndex,_W:boxServicesStackTempSensorIndex,'boxServicesStackTempSensorType':boxServicesStackTempSensorType,'boxServicesStackTempSensorState':boxServicesStackTempSensorState,'boxServicesStackTempSensorTemperature':boxServicesStackTempSensorTemperature,'boxServicesNotificationsGroup':boxServicesNotificationsGroup,_N:boxsItemStateChangeEvent,_X:boxsTemperatureChangeEvent})