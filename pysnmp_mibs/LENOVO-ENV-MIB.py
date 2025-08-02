_S='lenovoEnvMibFanRPM'
_R='lenovoEnvMibTempSensorIndex'
_Q='lenovoEnvMibFanIndex'
_P='lenovoEnvMibPowerSupplyIndex'
_O='absent'
_N='lenovoEnvMibTempSensorThreshold'
_M='lenovoEnvMibTempSensorTemperature'
_L='lenovoEnvMibTempSensorState'
_K='lenovoEnvMibTempSensorName'
_J='lenovoEnvMibTempSensorID'
_I='lenovoEnvMibFanState'
_H='lenovoEnvMibFanName'
_G='lenovoEnvMibFanID'
_F='lenovoEnvMibPowerSupplyState'
_E='lenovoEnvMibPowerSupplyName'
_D='lenovoEnvMibPowerSupplyID'
_C='read-only'
_B='LENOVO-ENV-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
PhysicalIndex,=mibBuilder.importSymbols('ENTITY-MIB','PhysicalIndex')
network_mibs,=mibBuilder.importSymbols('LENOVO-SMI-MIB','network-mibs')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB','SnmpAdminString')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
lenovoEnvMIB=ModuleIdentity((1,3,6,1,4,1,19046,2,3,11))
if mibBuilder.loadTexts:lenovoEnvMIB.setRevisions(('2016-09-23 00:00',))
class LenovoEnvMibPowerSupplyState(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*(('off',0),('on',1),(_O,2),('outputFault',3)))
class LenovoEnvMibFanState(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('ok',0),(_O,1),('fault',2)))
class LenovoEnvMibTempSensorState(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('ok',0),('fault',1)))
class LenovoEnvMibTempSensorThreshold(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('warning',0),('failure',1),('ok',2)))
class LenovoEnvMibFanAirFlow(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('front2back',0),('back2front',1),('notinstalled',2)))
_LenovoEnvMibObjects_ObjectIdentity=ObjectIdentity
lenovoEnvMibObjects=_LenovoEnvMibObjects_ObjectIdentity((1,3,6,1,4,1,19046,2,3,11,1))
_LenovoEnvMibPowerSupplyTable_Object=MibTable
lenovoEnvMibPowerSupplyTable=_LenovoEnvMibPowerSupplyTable_Object((1,3,6,1,4,1,19046,2,3,11,1,1))
if mibBuilder.loadTexts:lenovoEnvMibPowerSupplyTable.setStatus(_A)
_LenovoEnvMibPowerSupplyEntry_Object=MibTableRow
lenovoEnvMibPowerSupplyEntry=_LenovoEnvMibPowerSupplyEntry_Object((1,3,6,1,4,1,19046,2,3,11,1,1,1))
lenovoEnvMibPowerSupplyEntry.setIndexNames((0,_B,_P))
if mibBuilder.loadTexts:lenovoEnvMibPowerSupplyEntry.setStatus(_A)
_LenovoEnvMibPowerSupplyIndex_Type=PhysicalIndex
_LenovoEnvMibPowerSupplyIndex_Object=MibTableColumn
lenovoEnvMibPowerSupplyIndex=_LenovoEnvMibPowerSupplyIndex_Object((1,3,6,1,4,1,19046,2,3,11,1,1,1,1),_LenovoEnvMibPowerSupplyIndex_Type())
lenovoEnvMibPowerSupplyIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:lenovoEnvMibPowerSupplyIndex.setStatus(_A)
_LenovoEnvMibPowerSupplyID_Type=Integer32
_LenovoEnvMibPowerSupplyID_Object=MibTableColumn
lenovoEnvMibPowerSupplyID=_LenovoEnvMibPowerSupplyID_Object((1,3,6,1,4,1,19046,2,3,11,1,1,1,2),_LenovoEnvMibPowerSupplyID_Type())
lenovoEnvMibPowerSupplyID.setMaxAccess(_C)
if mibBuilder.loadTexts:lenovoEnvMibPowerSupplyID.setStatus(_A)
_LenovoEnvMibPowerSupplyDesc_Type=SnmpAdminString
_LenovoEnvMibPowerSupplyDesc_Object=MibTableColumn
lenovoEnvMibPowerSupplyDesc=_LenovoEnvMibPowerSupplyDesc_Object((1,3,6,1,4,1,19046,2,3,11,1,1,1,3),_LenovoEnvMibPowerSupplyDesc_Type())
lenovoEnvMibPowerSupplyDesc.setMaxAccess(_C)
if mibBuilder.loadTexts:lenovoEnvMibPowerSupplyDesc.setStatus(_A)
_LenovoEnvMibPowerSupplyName_Type=SnmpAdminString
_LenovoEnvMibPowerSupplyName_Object=MibTableColumn
lenovoEnvMibPowerSupplyName=_LenovoEnvMibPowerSupplyName_Object((1,3,6,1,4,1,19046,2,3,11,1,1,1,4),_LenovoEnvMibPowerSupplyName_Type())
lenovoEnvMibPowerSupplyName.setMaxAccess(_C)
if mibBuilder.loadTexts:lenovoEnvMibPowerSupplyName.setStatus(_A)
_LenovoEnvMibPowerSupplyState_Type=LenovoEnvMibPowerSupplyState
_LenovoEnvMibPowerSupplyState_Object=MibTableColumn
lenovoEnvMibPowerSupplyState=_LenovoEnvMibPowerSupplyState_Object((1,3,6,1,4,1,19046,2,3,11,1,1,1,5),_LenovoEnvMibPowerSupplyState_Type())
lenovoEnvMibPowerSupplyState.setMaxAccess(_C)
if mibBuilder.loadTexts:lenovoEnvMibPowerSupplyState.setStatus(_A)
_LenovoEnvMibFanTable_Object=MibTable
lenovoEnvMibFanTable=_LenovoEnvMibFanTable_Object((1,3,6,1,4,1,19046,2,3,11,1,2))
if mibBuilder.loadTexts:lenovoEnvMibFanTable.setStatus(_A)
_LenovoEnvMibFanEntry_Object=MibTableRow
lenovoEnvMibFanEntry=_LenovoEnvMibFanEntry_Object((1,3,6,1,4,1,19046,2,3,11,1,2,1))
lenovoEnvMibFanEntry.setIndexNames((0,_B,_Q))
if mibBuilder.loadTexts:lenovoEnvMibFanEntry.setStatus(_A)
_LenovoEnvMibFanIndex_Type=PhysicalIndex
_LenovoEnvMibFanIndex_Object=MibTableColumn
lenovoEnvMibFanIndex=_LenovoEnvMibFanIndex_Object((1,3,6,1,4,1,19046,2,3,11,1,2,1,1),_LenovoEnvMibFanIndex_Type())
lenovoEnvMibFanIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:lenovoEnvMibFanIndex.setStatus(_A)
_LenovoEnvMibFanID_Type=Integer32
_LenovoEnvMibFanID_Object=MibTableColumn
lenovoEnvMibFanID=_LenovoEnvMibFanID_Object((1,3,6,1,4,1,19046,2,3,11,1,2,1,2),_LenovoEnvMibFanID_Type())
lenovoEnvMibFanID.setMaxAccess(_C)
if mibBuilder.loadTexts:lenovoEnvMibFanID.setStatus(_A)
_LenovoEnvMibFanDesc_Type=SnmpAdminString
_LenovoEnvMibFanDesc_Object=MibTableColumn
lenovoEnvMibFanDesc=_LenovoEnvMibFanDesc_Object((1,3,6,1,4,1,19046,2,3,11,1,2,1,3),_LenovoEnvMibFanDesc_Type())
lenovoEnvMibFanDesc.setMaxAccess(_C)
if mibBuilder.loadTexts:lenovoEnvMibFanDesc.setStatus(_A)
_LenovoEnvMibFanName_Type=SnmpAdminString
_LenovoEnvMibFanName_Object=MibTableColumn
lenovoEnvMibFanName=_LenovoEnvMibFanName_Object((1,3,6,1,4,1,19046,2,3,11,1,2,1,4),_LenovoEnvMibFanName_Type())
lenovoEnvMibFanName.setMaxAccess(_C)
if mibBuilder.loadTexts:lenovoEnvMibFanName.setStatus(_A)
_LenovoEnvMibFanState_Type=LenovoEnvMibFanState
_LenovoEnvMibFanState_Object=MibTableColumn
lenovoEnvMibFanState=_LenovoEnvMibFanState_Object((1,3,6,1,4,1,19046,2,3,11,1,2,1,5),_LenovoEnvMibFanState_Type())
lenovoEnvMibFanState.setMaxAccess(_C)
if mibBuilder.loadTexts:lenovoEnvMibFanState.setStatus(_A)
_LenovoEnvMibFanAirFlow_Type=LenovoEnvMibFanAirFlow
_LenovoEnvMibFanAirFlow_Object=MibTableColumn
lenovoEnvMibFanAirFlow=_LenovoEnvMibFanAirFlow_Object((1,3,6,1,4,1,19046,2,3,11,1,2,1,6),_LenovoEnvMibFanAirFlow_Type())
lenovoEnvMibFanAirFlow.setMaxAccess(_C)
if mibBuilder.loadTexts:lenovoEnvMibFanAirFlow.setStatus(_A)
_LenovoEnvMibFanModule_Type=Integer32
_LenovoEnvMibFanModule_Object=MibTableColumn
lenovoEnvMibFanModule=_LenovoEnvMibFanModule_Object((1,3,6,1,4,1,19046,2,3,11,1,2,1,7),_LenovoEnvMibFanModule_Type())
lenovoEnvMibFanModule.setMaxAccess(_C)
if mibBuilder.loadTexts:lenovoEnvMibFanModule.setStatus(_A)
_LenovoEnvMibFanSpeedRPM_Type=Integer32
_LenovoEnvMibFanSpeedRPM_Object=MibTableColumn
lenovoEnvMibFanSpeedRPM=_LenovoEnvMibFanSpeedRPM_Object((1,3,6,1,4,1,19046,2,3,11,1,2,1,8),_LenovoEnvMibFanSpeedRPM_Type())
lenovoEnvMibFanSpeedRPM.setMaxAccess(_C)
if mibBuilder.loadTexts:lenovoEnvMibFanSpeedRPM.setStatus(_A)
_LenovoEnvMibFanSpeedPercent_Type=Gauge32
_LenovoEnvMibFanSpeedPercent_Object=MibTableColumn
lenovoEnvMibFanSpeedPercent=_LenovoEnvMibFanSpeedPercent_Object((1,3,6,1,4,1,19046,2,3,11,1,2,1,9),_LenovoEnvMibFanSpeedPercent_Type())
lenovoEnvMibFanSpeedPercent.setMaxAccess(_C)
if mibBuilder.loadTexts:lenovoEnvMibFanSpeedPercent.setStatus(_A)
_LenovoEnvMibTempSensorTable_Object=MibTable
lenovoEnvMibTempSensorTable=_LenovoEnvMibTempSensorTable_Object((1,3,6,1,4,1,19046,2,3,11,1,3))
if mibBuilder.loadTexts:lenovoEnvMibTempSensorTable.setStatus(_A)
_LenovoEnvMibTempSensorEntry_Object=MibTableRow
lenovoEnvMibTempSensorEntry=_LenovoEnvMibTempSensorEntry_Object((1,3,6,1,4,1,19046,2,3,11,1,3,1))
lenovoEnvMibTempSensorEntry.setIndexNames((0,_B,_R))
if mibBuilder.loadTexts:lenovoEnvMibTempSensorEntry.setStatus(_A)
_LenovoEnvMibTempSensorIndex_Type=PhysicalIndex
_LenovoEnvMibTempSensorIndex_Object=MibTableColumn
lenovoEnvMibTempSensorIndex=_LenovoEnvMibTempSensorIndex_Object((1,3,6,1,4,1,19046,2,3,11,1,3,1,1),_LenovoEnvMibTempSensorIndex_Type())
lenovoEnvMibTempSensorIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:lenovoEnvMibTempSensorIndex.setStatus(_A)
_LenovoEnvMibTempSensorID_Type=Integer32
_LenovoEnvMibTempSensorID_Object=MibTableColumn
lenovoEnvMibTempSensorID=_LenovoEnvMibTempSensorID_Object((1,3,6,1,4,1,19046,2,3,11,1,3,1,2),_LenovoEnvMibTempSensorID_Type())
lenovoEnvMibTempSensorID.setMaxAccess(_C)
if mibBuilder.loadTexts:lenovoEnvMibTempSensorID.setStatus(_A)
_LenovoEnvMibTempSensorDesc_Type=SnmpAdminString
_LenovoEnvMibTempSensorDesc_Object=MibTableColumn
lenovoEnvMibTempSensorDesc=_LenovoEnvMibTempSensorDesc_Object((1,3,6,1,4,1,19046,2,3,11,1,3,1,3),_LenovoEnvMibTempSensorDesc_Type())
lenovoEnvMibTempSensorDesc.setMaxAccess(_C)
if mibBuilder.loadTexts:lenovoEnvMibTempSensorDesc.setStatus(_A)
_LenovoEnvMibTempSensorName_Type=SnmpAdminString
_LenovoEnvMibTempSensorName_Object=MibTableColumn
lenovoEnvMibTempSensorName=_LenovoEnvMibTempSensorName_Object((1,3,6,1,4,1,19046,2,3,11,1,3,1,4),_LenovoEnvMibTempSensorName_Type())
lenovoEnvMibTempSensorName.setMaxAccess(_C)
if mibBuilder.loadTexts:lenovoEnvMibTempSensorName.setStatus(_A)
_LenovoEnvMibTempSensorState_Type=LenovoEnvMibTempSensorState
_LenovoEnvMibTempSensorState_Object=MibTableColumn
lenovoEnvMibTempSensorState=_LenovoEnvMibTempSensorState_Object((1,3,6,1,4,1,19046,2,3,11,1,3,1,5),_LenovoEnvMibTempSensorState_Type())
lenovoEnvMibTempSensorState.setMaxAccess(_C)
if mibBuilder.loadTexts:lenovoEnvMibTempSensorState.setStatus(_A)
_LenovoEnvMibTempSensorTemperature_Type=Integer32
_LenovoEnvMibTempSensorTemperature_Object=MibTableColumn
lenovoEnvMibTempSensorTemperature=_LenovoEnvMibTempSensorTemperature_Object((1,3,6,1,4,1,19046,2,3,11,1,3,1,6),_LenovoEnvMibTempSensorTemperature_Type())
lenovoEnvMibTempSensorTemperature.setMaxAccess(_C)
if mibBuilder.loadTexts:lenovoEnvMibTempSensorTemperature.setStatus(_A)
_LenovoEnvMibTempSensorThresholds_ObjectIdentity=ObjectIdentity
lenovoEnvMibTempSensorThresholds=_LenovoEnvMibTempSensorThresholds_ObjectIdentity((1,3,6,1,4,1,19046,2,3,11,1,4))
_LenovoEnvMIBTempSensorWarning_Type=Integer32
_LenovoEnvMIBTempSensorWarning_Object=MibScalar
lenovoEnvMIBTempSensorWarning=_LenovoEnvMIBTempSensorWarning_Object((1,3,6,1,4,1,19046,2,3,11,1,4,1),_LenovoEnvMIBTempSensorWarning_Type())
lenovoEnvMIBTempSensorWarning.setMaxAccess(_C)
if mibBuilder.loadTexts:lenovoEnvMIBTempSensorWarning.setStatus(_A)
_LenovoEnvMIBTempSensorShutdown_Type=Integer32
_LenovoEnvMIBTempSensorShutdown_Object=MibScalar
lenovoEnvMIBTempSensorShutdown=_LenovoEnvMIBTempSensorShutdown_Object((1,3,6,1,4,1,19046,2,3,11,1,4,2),_LenovoEnvMIBTempSensorShutdown_Type())
lenovoEnvMIBTempSensorShutdown.setMaxAccess(_C)
if mibBuilder.loadTexts:lenovoEnvMIBTempSensorShutdown.setStatus(_A)
_LenovoEnvMIBTempSensorSetPoint_Type=Integer32
_LenovoEnvMIBTempSensorSetPoint_Object=MibScalar
lenovoEnvMIBTempSensorSetPoint=_LenovoEnvMIBTempSensorSetPoint_Object((1,3,6,1,4,1,19046,2,3,11,1,4,3),_LenovoEnvMIBTempSensorSetPoint_Type())
lenovoEnvMIBTempSensorSetPoint.setMaxAccess(_C)
if mibBuilder.loadTexts:lenovoEnvMIBTempSensorSetPoint.setStatus(_A)
_LenovoEnvMibNotificationPrefix_ObjectIdentity=ObjectIdentity
lenovoEnvMibNotificationPrefix=_LenovoEnvMibNotificationPrefix_ObjectIdentity((1,3,6,1,4,1,19046,2,3,11,3))
_LenovoEnvMibNotifications_ObjectIdentity=ObjectIdentity
lenovoEnvMibNotifications=_LenovoEnvMibNotifications_ObjectIdentity((1,3,6,1,4,1,19046,2,3,11,3,0))
_LenovoEnvMibNotificationObjects_ObjectIdentity=ObjectIdentity
lenovoEnvMibNotificationObjects=_LenovoEnvMibNotificationObjects_ObjectIdentity((1,3,6,1,4,1,19046,2,3,11,3,1))
_LenovoEnvMibTempSensorThreshold_Type=LenovoEnvMibTempSensorThreshold
_LenovoEnvMibTempSensorThreshold_Object=MibScalar
lenovoEnvMibTempSensorThreshold=_LenovoEnvMibTempSensorThreshold_Object((1,3,6,1,4,1,19046,2,3,11,3,1,1),_LenovoEnvMibTempSensorThreshold_Type())
lenovoEnvMibTempSensorThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:lenovoEnvMibTempSensorThreshold.setStatus(_A)
lenovoEnvMibPowerSupplyFailure=NotificationType((1,3,6,1,4,1,19046,2,3,11,3,0,1))
lenovoEnvMibPowerSupplyFailure.setObjects(*((_B,_D),(_B,_E),(_B,_F)))
if mibBuilder.loadTexts:lenovoEnvMibPowerSupplyFailure.setStatus(_A)
lenovoEnvMibPowerSupplyFixed=NotificationType((1,3,6,1,4,1,19046,2,3,11,3,0,2))
lenovoEnvMibPowerSupplyFixed.setObjects(*((_B,_D),(_B,_E),(_B,_F)))
if mibBuilder.loadTexts:lenovoEnvMibPowerSupplyFixed.setStatus(_A)
lenovoEnvMibFanFailure=NotificationType((1,3,6,1,4,1,19046,2,3,11,3,0,3))
lenovoEnvMibFanFailure.setObjects(*((_B,_G),(_B,_H),(_B,_I),(_B,_S)))
if mibBuilder.loadTexts:lenovoEnvMibFanFailure.setStatus(_A)
lenovoEnvMibFanFixed=NotificationType((1,3,6,1,4,1,19046,2,3,11,3,0,4))
lenovoEnvMibFanFixed.setObjects(*((_B,_G),(_B,_H),(_B,_I),(_B,_S)))
if mibBuilder.loadTexts:lenovoEnvMibFanFixed.setStatus(_A)
lenovoEnvMibTempSensorFailure=NotificationType((1,3,6,1,4,1,19046,2,3,11,3,0,5))
lenovoEnvMibTempSensorFailure.setObjects(*((_B,_J),(_B,_K),(_B,_L),(_B,_M),(_B,_N)))
if mibBuilder.loadTexts:lenovoEnvMibTempSensorFailure.setStatus(_A)
lenovoEnvMibTempSensorFixed=NotificationType((1,3,6,1,4,1,19046,2,3,11,3,0,6))
lenovoEnvMibTempSensorFixed.setObjects(*((_B,_J),(_B,_K),(_B,_L),(_B,_M),(_B,_N)))
if mibBuilder.loadTexts:lenovoEnvMibTempSensorFixed.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'LenovoEnvMibPowerSupplyState':LenovoEnvMibPowerSupplyState,'LenovoEnvMibFanState':LenovoEnvMibFanState,'LenovoEnvMibTempSensorState':LenovoEnvMibTempSensorState,'LenovoEnvMibTempSensorThreshold':LenovoEnvMibTempSensorThreshold,'LenovoEnvMibFanAirFlow':LenovoEnvMibFanAirFlow,'lenovoEnvMIB':lenovoEnvMIB,'lenovoEnvMibObjects':lenovoEnvMibObjects,'lenovoEnvMibPowerSupplyTable':lenovoEnvMibPowerSupplyTable,'lenovoEnvMibPowerSupplyEntry':lenovoEnvMibPowerSupplyEntry,_P:lenovoEnvMibPowerSupplyIndex,_D:lenovoEnvMibPowerSupplyID,'lenovoEnvMibPowerSupplyDesc':lenovoEnvMibPowerSupplyDesc,_E:lenovoEnvMibPowerSupplyName,_F:lenovoEnvMibPowerSupplyState,'lenovoEnvMibFanTable':lenovoEnvMibFanTable,'lenovoEnvMibFanEntry':lenovoEnvMibFanEntry,_Q:lenovoEnvMibFanIndex,_G:lenovoEnvMibFanID,'lenovoEnvMibFanDesc':lenovoEnvMibFanDesc,_H:lenovoEnvMibFanName,_I:lenovoEnvMibFanState,'lenovoEnvMibFanAirFlow':lenovoEnvMibFanAirFlow,'lenovoEnvMibFanModule':lenovoEnvMibFanModule,'lenovoEnvMibFanSpeedRPM':lenovoEnvMibFanSpeedRPM,'lenovoEnvMibFanSpeedPercent':lenovoEnvMibFanSpeedPercent,'lenovoEnvMibTempSensorTable':lenovoEnvMibTempSensorTable,'lenovoEnvMibTempSensorEntry':lenovoEnvMibTempSensorEntry,_R:lenovoEnvMibTempSensorIndex,_J:lenovoEnvMibTempSensorID,'lenovoEnvMibTempSensorDesc':lenovoEnvMibTempSensorDesc,_K:lenovoEnvMibTempSensorName,_L:lenovoEnvMibTempSensorState,_M:lenovoEnvMibTempSensorTemperature,'lenovoEnvMibTempSensorThresholds':lenovoEnvMibTempSensorThresholds,'lenovoEnvMIBTempSensorWarning':lenovoEnvMIBTempSensorWarning,'lenovoEnvMIBTempSensorShutdown':lenovoEnvMIBTempSensorShutdown,'lenovoEnvMIBTempSensorSetPoint':lenovoEnvMIBTempSensorSetPoint,'lenovoEnvMibNotificationPrefix':lenovoEnvMibNotificationPrefix,'lenovoEnvMibNotifications':lenovoEnvMibNotifications,'lenovoEnvMibPowerSupplyFailure':lenovoEnvMibPowerSupplyFailure,'lenovoEnvMibPowerSupplyFixed':lenovoEnvMibPowerSupplyFixed,'lenovoEnvMibFanFailure':lenovoEnvMibFanFailure,'lenovoEnvMibFanFixed':lenovoEnvMibFanFixed,'lenovoEnvMibTempSensorFailure':lenovoEnvMibTempSensorFailure,'lenovoEnvMibTempSensorFixed':lenovoEnvMibTempSensorFixed,'lenovoEnvMibNotificationObjects':lenovoEnvMibNotificationObjects,_N:lenovoEnvMibTempSensorThreshold})