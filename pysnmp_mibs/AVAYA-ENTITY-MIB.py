_c='avEntPhyChFruPsuFltOk'
_b='avEntPhyChFruPsuFlt'
_a='avEntPhyChFruInsertion'
_Z='avEntPhyChFruRemoval'
_Y='unknown'
_X='accessible-for-notify'
_W='Integer32'
_V='entPhysicalIndex'
_U='avEntPhyUSBDevicePower'
_T='avEntPhyUSBDeviceSpeed'
_S='avEntPhyUSBDeviceUSBSupportVersion'
_R='avEntPhyChFruFault'
_Q='avEntPhyChFruOperStat'
_P='DisplayString'
_O='avEntPhySensorHiWarningClear'
_N='avEntPhySensorHiWarning'
_M='avEntPhySensorLoWarningClear'
_L='avEntPhySensorLoWarning'
_K='avEntPhySeverity'
_J='avEntPhyProductId'
_I='entPhysicalParentRelPos'
_H='entPhySensorValue'
_G='ENTITY-SENSOR-MIB'
_F='read-only'
_E='avEntPhysicalIndex'
_D='entPhysicalDescr'
_C='ENTITY-MIB'
_B='current'
_A='AVAYA-ENTITY-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
lsg,=mibBuilder.importSymbols('AVAYAGEN-MIB','lsg')
PhysicalIndex,entPhysicalDescr,entPhysicalIndex,entPhysicalParentRelPos=mibBuilder.importSymbols(_C,'PhysicalIndex',_D,_V,_I)
EntitySensorValue,entPhySensorValue=mibBuilder.importSymbols(_G,'EntitySensorValue',_H)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso,mib_2=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_W,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso','mib-2')
DisplayString,PhysAddress,TextualConvention,TimeStamp=mibBuilder.importSymbols('SNMPv2-TC',_P,'PhysAddress','TextualConvention','TimeStamp')
avayaEntity=ModuleIdentity((1,3,6,1,4,1,6889,2,1,99))
class AvEntPhyItuPerceivedSeverity(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*(('cleared',1),('indeterminate',2),('critical',3),('major',4),('minor',5),('warning',6)))
_AvEntPhySensorTable_Object=MibTable
avEntPhySensorTable=_AvEntPhySensorTable_Object((1,3,6,1,4,1,6889,2,1,99,1))
if mibBuilder.loadTexts:avEntPhySensorTable.setStatus(_B)
_AvEntPhySensorEntry_Object=MibTableRow
avEntPhySensorEntry=_AvEntPhySensorEntry_Object((1,3,6,1,4,1,6889,2,1,99,1,1))
avEntPhySensorEntry.setIndexNames((0,_C,_V))
if mibBuilder.loadTexts:avEntPhySensorEntry.setStatus(_B)
_AvEntPhySensorHiShutdown_Type=EntitySensorValue
_AvEntPhySensorHiShutdown_Object=MibTableColumn
avEntPhySensorHiShutdown=_AvEntPhySensorHiShutdown_Object((1,3,6,1,4,1,6889,2,1,99,1,1,1),_AvEntPhySensorHiShutdown_Type())
avEntPhySensorHiShutdown.setMaxAccess(_F)
if mibBuilder.loadTexts:avEntPhySensorHiShutdown.setStatus(_B)
_AvEntPhySensorHiWarning_Type=EntitySensorValue
_AvEntPhySensorHiWarning_Object=MibTableColumn
avEntPhySensorHiWarning=_AvEntPhySensorHiWarning_Object((1,3,6,1,4,1,6889,2,1,99,1,1,2),_AvEntPhySensorHiWarning_Type())
avEntPhySensorHiWarning.setMaxAccess(_F)
if mibBuilder.loadTexts:avEntPhySensorHiWarning.setStatus(_B)
_AvEntPhySensorHiWarningClear_Type=EntitySensorValue
_AvEntPhySensorHiWarningClear_Object=MibTableColumn
avEntPhySensorHiWarningClear=_AvEntPhySensorHiWarningClear_Object((1,3,6,1,4,1,6889,2,1,99,1,1,3),_AvEntPhySensorHiWarningClear_Type())
avEntPhySensorHiWarningClear.setMaxAccess(_F)
if mibBuilder.loadTexts:avEntPhySensorHiWarningClear.setStatus(_B)
_AvEntPhySensorLoWarningClear_Type=EntitySensorValue
_AvEntPhySensorLoWarningClear_Object=MibTableColumn
avEntPhySensorLoWarningClear=_AvEntPhySensorLoWarningClear_Object((1,3,6,1,4,1,6889,2,1,99,1,1,4),_AvEntPhySensorLoWarningClear_Type())
avEntPhySensorLoWarningClear.setMaxAccess(_F)
if mibBuilder.loadTexts:avEntPhySensorLoWarningClear.setStatus(_B)
_AvEntPhySensorLoWarning_Type=EntitySensorValue
_AvEntPhySensorLoWarning_Object=MibTableColumn
avEntPhySensorLoWarning=_AvEntPhySensorLoWarning_Object((1,3,6,1,4,1,6889,2,1,99,1,1,5),_AvEntPhySensorLoWarning_Type())
avEntPhySensorLoWarning.setMaxAccess(_F)
if mibBuilder.loadTexts:avEntPhySensorLoWarning.setStatus(_B)
_AvEntPhySensorLoShutdown_Type=EntitySensorValue
_AvEntPhySensorLoShutdown_Object=MibTableColumn
avEntPhySensorLoShutdown=_AvEntPhySensorLoShutdown_Object((1,3,6,1,4,1,6889,2,1,99,1,1,6),_AvEntPhySensorLoShutdown_Type())
avEntPhySensorLoShutdown.setMaxAccess(_F)
if mibBuilder.loadTexts:avEntPhySensorLoShutdown.setStatus(_B)
_AvEntPhySensorEventSupportMask_Type=OctetString
_AvEntPhySensorEventSupportMask_Object=MibTableColumn
avEntPhySensorEventSupportMask=_AvEntPhySensorEventSupportMask_Object((1,3,6,1,4,1,6889,2,1,99,1,1,7),_AvEntPhySensorEventSupportMask_Type())
avEntPhySensorEventSupportMask.setMaxAccess(_F)
if mibBuilder.loadTexts:avEntPhySensorEventSupportMask.setStatus(_B)
_AvEntTraps_ObjectIdentity=ObjectIdentity
avEntTraps=_AvEntTraps_ObjectIdentity((1,3,6,1,4,1,6889,2,1,99,2))
_AvEntTrapsV3separator_ObjectIdentity=ObjectIdentity
avEntTrapsV3separator=_AvEntTrapsV3separator_ObjectIdentity((1,3,6,1,4,1,6889,2,1,99,2,0))
_AvEntPhyUSBDevices_ObjectIdentity=ObjectIdentity
avEntPhyUSBDevices=_AvEntPhyUSBDevices_ObjectIdentity((1,3,6,1,4,1,6889,2,1,99,3))
_AvEntPhyUSBDevicesTraps_ObjectIdentity=ObjectIdentity
avEntPhyUSBDevicesTraps=_AvEntPhyUSBDevicesTraps_ObjectIdentity((1,3,6,1,4,1,6889,2,1,99,3,0))
_AvEntPhyUSBDevicesTable_Object=MibTable
avEntPhyUSBDevicesTable=_AvEntPhyUSBDevicesTable_Object((1,3,6,1,4,1,6889,2,1,99,3,1))
if mibBuilder.loadTexts:avEntPhyUSBDevicesTable.setStatus(_B)
_AvEntPhyUSBDevicesEntry_Object=MibTableRow
avEntPhyUSBDevicesEntry=_AvEntPhyUSBDevicesEntry_Object((1,3,6,1,4,1,6889,2,1,99,3,1,1))
avEntPhyUSBDevicesEntry.setIndexNames((0,_C,_V))
if mibBuilder.loadTexts:avEntPhyUSBDevicesEntry.setStatus(_B)
class _AvEntPhyUSBDeviceUSBSupportVersion_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_AvEntPhyUSBDeviceUSBSupportVersion_Type.__name__=_P
_AvEntPhyUSBDeviceUSBSupportVersion_Object=MibTableColumn
avEntPhyUSBDeviceUSBSupportVersion=_AvEntPhyUSBDeviceUSBSupportVersion_Object((1,3,6,1,4,1,6889,2,1,99,3,1,1,1),_AvEntPhyUSBDeviceUSBSupportVersion_Type())
avEntPhyUSBDeviceUSBSupportVersion.setMaxAccess(_F)
if mibBuilder.loadTexts:avEntPhyUSBDeviceUSBSupportVersion.setStatus(_B)
_AvEntPhyUSBDeviceClassCode_Type=Integer32
_AvEntPhyUSBDeviceClassCode_Object=MibTableColumn
avEntPhyUSBDeviceClassCode=_AvEntPhyUSBDeviceClassCode_Object((1,3,6,1,4,1,6889,2,1,99,3,1,1,2),_AvEntPhyUSBDeviceClassCode_Type())
avEntPhyUSBDeviceClassCode.setMaxAccess(_F)
if mibBuilder.loadTexts:avEntPhyUSBDeviceClassCode.setStatus(_B)
_AvEntPhyUSBDeviceSubClassCode_Type=Integer32
_AvEntPhyUSBDeviceSubClassCode_Object=MibTableColumn
avEntPhyUSBDeviceSubClassCode=_AvEntPhyUSBDeviceSubClassCode_Object((1,3,6,1,4,1,6889,2,1,99,3,1,1,3),_AvEntPhyUSBDeviceSubClassCode_Type())
avEntPhyUSBDeviceSubClassCode.setMaxAccess(_F)
if mibBuilder.loadTexts:avEntPhyUSBDeviceSubClassCode.setStatus(_B)
_AvEntPhyUSBDeviceProtocol_Type=Integer32
_AvEntPhyUSBDeviceProtocol_Object=MibTableColumn
avEntPhyUSBDeviceProtocol=_AvEntPhyUSBDeviceProtocol_Object((1,3,6,1,4,1,6889,2,1,99,3,1,1,4),_AvEntPhyUSBDeviceProtocol_Type())
avEntPhyUSBDeviceProtocol.setMaxAccess(_F)
if mibBuilder.loadTexts:avEntPhyUSBDeviceProtocol.setStatus(_B)
_AvEntPhyUSBDeviceVendorId_Type=OctetString
_AvEntPhyUSBDeviceVendorId_Object=MibTableColumn
avEntPhyUSBDeviceVendorId=_AvEntPhyUSBDeviceVendorId_Object((1,3,6,1,4,1,6889,2,1,99,3,1,1,5),_AvEntPhyUSBDeviceVendorId_Type())
avEntPhyUSBDeviceVendorId.setMaxAccess(_F)
if mibBuilder.loadTexts:avEntPhyUSBDeviceVendorId.setStatus(_B)
class _AvEntPhyUSBDeviceSpeed_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_AvEntPhyUSBDeviceSpeed_Type.__name__=_P
_AvEntPhyUSBDeviceSpeed_Object=MibTableColumn
avEntPhyUSBDeviceSpeed=_AvEntPhyUSBDeviceSpeed_Object((1,3,6,1,4,1,6889,2,1,99,3,1,1,6),_AvEntPhyUSBDeviceSpeed_Type())
avEntPhyUSBDeviceSpeed.setMaxAccess(_F)
if mibBuilder.loadTexts:avEntPhyUSBDeviceSpeed.setStatus(_B)
class _AvEntPhyUSBDevicePower_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_AvEntPhyUSBDevicePower_Type.__name__=_P
_AvEntPhyUSBDevicePower_Object=MibTableColumn
avEntPhyUSBDevicePower=_AvEntPhyUSBDevicePower_Object((1,3,6,1,4,1,6889,2,1,99,3,1,1,7),_AvEntPhyUSBDevicePower_Type())
avEntPhyUSBDevicePower.setMaxAccess(_F)
if mibBuilder.loadTexts:avEntPhyUSBDevicePower.setStatus(_B)
_AvEntPhyUSBDeviceCurrent_Type=Integer32
_AvEntPhyUSBDeviceCurrent_Object=MibTableColumn
avEntPhyUSBDeviceCurrent=_AvEntPhyUSBDeviceCurrent_Object((1,3,6,1,4,1,6889,2,1,99,3,1,1,8),_AvEntPhyUSBDeviceCurrent_Type())
avEntPhyUSBDeviceCurrent.setMaxAccess(_F)
if mibBuilder.loadTexts:avEntPhyUSBDeviceCurrent.setStatus(_B)
_AvEntPhyUSBMassStorageDevicesTable_Object=MibTable
avEntPhyUSBMassStorageDevicesTable=_AvEntPhyUSBMassStorageDevicesTable_Object((1,3,6,1,4,1,6889,2,1,99,3,2))
if mibBuilder.loadTexts:avEntPhyUSBMassStorageDevicesTable.setStatus(_B)
_AvEntPhyUSBMassStorageDevicesEntry_Object=MibTableRow
avEntPhyUSBMassStorageDevicesEntry=_AvEntPhyUSBMassStorageDevicesEntry_Object((1,3,6,1,4,1,6889,2,1,99,3,2,1))
avEntPhyUSBMassStorageDevicesEntry.setIndexNames((0,_C,_V))
if mibBuilder.loadTexts:avEntPhyUSBMassStorageDevicesEntry.setStatus(_B)
class _AvEntPhyUSBMassStorageDeviceFileSystemName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_AvEntPhyUSBMassStorageDeviceFileSystemName_Type.__name__=_P
_AvEntPhyUSBMassStorageDeviceFileSystemName_Object=MibTableColumn
avEntPhyUSBMassStorageDeviceFileSystemName=_AvEntPhyUSBMassStorageDeviceFileSystemName_Object((1,3,6,1,4,1,6889,2,1,99,3,2,1,1),_AvEntPhyUSBMassStorageDeviceFileSystemName_Type())
avEntPhyUSBMassStorageDeviceFileSystemName.setMaxAccess(_F)
if mibBuilder.loadTexts:avEntPhyUSBMassStorageDeviceFileSystemName.setStatus(_B)
_AvEntPhyUSBMassStorageDeviceCapacity_Type=Integer32
_AvEntPhyUSBMassStorageDeviceCapacity_Object=MibTableColumn
avEntPhyUSBMassStorageDeviceCapacity=_AvEntPhyUSBMassStorageDeviceCapacity_Object((1,3,6,1,4,1,6889,2,1,99,3,2,1,2),_AvEntPhyUSBMassStorageDeviceCapacity_Type())
avEntPhyUSBMassStorageDeviceCapacity.setMaxAccess(_F)
if mibBuilder.loadTexts:avEntPhyUSBMassStorageDeviceCapacity.setStatus(_B)
_AvEntPhyUSBMassStorageDeviceFreeMemory_Type=Integer32
_AvEntPhyUSBMassStorageDeviceFreeMemory_Object=MibTableColumn
avEntPhyUSBMassStorageDeviceFreeMemory=_AvEntPhyUSBMassStorageDeviceFreeMemory_Object((1,3,6,1,4,1,6889,2,1,99,3,2,1,3),_AvEntPhyUSBMassStorageDeviceFreeMemory_Type())
avEntPhyUSBMassStorageDeviceFreeMemory.setMaxAccess(_F)
if mibBuilder.loadTexts:avEntPhyUSBMassStorageDeviceFreeMemory.setStatus(_B)
class _AvEntPhyUSBMassStorageDeviceFs_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_AvEntPhyUSBMassStorageDeviceFs_Type.__name__=_P
_AvEntPhyUSBMassStorageDeviceFs_Object=MibTableColumn
avEntPhyUSBMassStorageDeviceFs=_AvEntPhyUSBMassStorageDeviceFs_Object((1,3,6,1,4,1,6889,2,1,99,3,2,1,4),_AvEntPhyUSBMassStorageDeviceFs_Type())
avEntPhyUSBMassStorageDeviceFs.setMaxAccess(_F)
if mibBuilder.loadTexts:avEntPhyUSBMassStorageDeviceFs.setStatus(_B)
_AvEntPhyNotificationDefinitions_ObjectIdentity=ObjectIdentity
avEntPhyNotificationDefinitions=_AvEntPhyNotificationDefinitions_ObjectIdentity((1,3,6,1,4,1,6889,2,1,99,4))
_AvEntPhySeverity_Type=AvEntPhyItuPerceivedSeverity
_AvEntPhySeverity_Object=MibScalar
avEntPhySeverity=_AvEntPhySeverity_Object((1,3,6,1,4,1,6889,2,1,99,4,1),_AvEntPhySeverity_Type())
avEntPhySeverity.setMaxAccess(_X)
if mibBuilder.loadTexts:avEntPhySeverity.setStatus(_B)
class _AvEntPhyProductId_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,10))
_AvEntPhyProductId_Type.__name__=_P
_AvEntPhyProductId_Object=MibScalar
avEntPhyProductId=_AvEntPhyProductId_Object((1,3,6,1,4,1,6889,2,1,99,4,2),_AvEntPhyProductId_Type())
avEntPhyProductId.setMaxAccess(_X)
if mibBuilder.loadTexts:avEntPhyProductId.setStatus(_B)
_AvEntPhysicalIndex_Type=PhysicalIndex
_AvEntPhysicalIndex_Object=MibScalar
avEntPhysicalIndex=_AvEntPhysicalIndex_Object((1,3,6,1,4,1,6889,2,1,99,4,3),_AvEntPhysicalIndex_Type())
avEntPhysicalIndex.setMaxAccess(_X)
if mibBuilder.loadTexts:avEntPhysicalIndex.setStatus(_B)
_AvEntPhyChFru_ObjectIdentity=ObjectIdentity
avEntPhyChFru=_AvEntPhyChFru_ObjectIdentity((1,3,6,1,4,1,6889,2,1,99,5))
_AvEntPhyChFruNotifications_ObjectIdentity=ObjectIdentity
avEntPhyChFruNotifications=_AvEntPhyChFruNotifications_ObjectIdentity((1,3,6,1,4,1,6889,2,1,99,5,0))
_AvEntPhyChFruTable_Object=MibTable
avEntPhyChFruTable=_AvEntPhyChFruTable_Object((1,3,6,1,4,1,6889,2,1,99,5,1))
if mibBuilder.loadTexts:avEntPhyChFruTable.setStatus(_B)
_AvEntPhyChFruEntry_Object=MibTableRow
avEntPhyChFruEntry=_AvEntPhyChFruEntry_Object((1,3,6,1,4,1,6889,2,1,99,5,1,1))
avEntPhyChFruEntry.setIndexNames((0,_C,_V))
if mibBuilder.loadTexts:avEntPhyChFruEntry.setStatus(_B)
class _AvEntPhyChFruOperStat_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,255)));namedValues=NamedValues(*(('ok',1),('fault',2),('notPresent',3),(_Y,255)))
_AvEntPhyChFruOperStat_Type.__name__=_W
_AvEntPhyChFruOperStat_Object=MibTableColumn
avEntPhyChFruOperStat=_AvEntPhyChFruOperStat_Object((1,3,6,1,4,1,6889,2,1,99,5,1,1,1),_AvEntPhyChFruOperStat_Type())
avEntPhyChFruOperStat.setMaxAccess(_F)
if mibBuilder.loadTexts:avEntPhyChFruOperStat.setStatus(_B)
class _AvEntPhyChFruFault_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,255)));namedValues=NamedValues(*(('none',1),('mulfunction',2),('acFault',3),('malfunctionAndAcFault',4),('singleFanFault',5),('multipleFanFault',6),('badExpansionCable',7),(_Y,255)))
_AvEntPhyChFruFault_Type.__name__=_W
_AvEntPhyChFruFault_Object=MibTableColumn
avEntPhyChFruFault=_AvEntPhyChFruFault_Object((1,3,6,1,4,1,6889,2,1,99,5,1,1,2),_AvEntPhyChFruFault_Type())
avEntPhyChFruFault.setMaxAccess(_F)
if mibBuilder.loadTexts:avEntPhyChFruFault.setStatus(_B)
avEntPhyChFruGroup=ObjectGroup((1,3,6,1,4,1,6889,2,1,99,5,2))
avEntPhyChFruGroup.setObjects(*((_A,_Q),(_A,_R)))
if mibBuilder.loadTexts:avEntPhyChFruGroup.setStatus(_B)
avEntFanFlt=NotificationType((1,3,6,1,4,1,6889,2,1,99,2,0,1))
avEntFanFlt.setObjects(*((_A,_E),(_C,_D),(_G,_H),(_A,_L)))
if mibBuilder.loadTexts:avEntFanFlt.setStatus(_B)
avEntFanOk=NotificationType((1,3,6,1,4,1,6889,2,1,99,2,0,2))
avEntFanOk.setObjects(*((_A,_E),(_C,_D),(_G,_H),(_A,_M)))
if mibBuilder.loadTexts:avEntFanOk.setStatus(_B)
avEnt48vPwrFlt=NotificationType((1,3,6,1,4,1,6889,2,1,99,2,0,4))
avEnt48vPwrFlt.setObjects(*((_A,_E),(_C,_D),(_G,_H),(_A,_N),(_A,_L),(_C,_I)))
if mibBuilder.loadTexts:avEnt48vPwrFlt.setStatus(_B)
avEnt48vPwrFltOk=NotificationType((1,3,6,1,4,1,6889,2,1,99,2,0,5))
avEnt48vPwrFltOk.setObjects(*((_A,_E),(_C,_D),(_G,_H),(_A,_O),(_A,_M),(_C,_I)))
if mibBuilder.loadTexts:avEnt48vPwrFltOk.setStatus(_B)
avEnt5vPwrFlt=NotificationType((1,3,6,1,4,1,6889,2,1,99,2,0,7))
avEnt5vPwrFlt.setObjects(*((_A,_E),(_C,_D),(_G,_H),(_A,_N),(_A,_L),(_C,_I)))
if mibBuilder.loadTexts:avEnt5vPwrFlt.setStatus(_B)
avEnt5vPwrFltOk=NotificationType((1,3,6,1,4,1,6889,2,1,99,2,0,8))
avEnt5vPwrFltOk.setObjects(*((_A,_E),(_C,_D),(_G,_H),(_A,_O),(_A,_M),(_C,_I)))
if mibBuilder.loadTexts:avEnt5vPwrFltOk.setStatus(_B)
avEnt3300mvPwrFlt=NotificationType((1,3,6,1,4,1,6889,2,1,99,2,0,10))
avEnt3300mvPwrFlt.setObjects(*((_A,_E),(_C,_D),(_G,_H),(_A,_N),(_A,_L),(_C,_I)))
if mibBuilder.loadTexts:avEnt3300mvPwrFlt.setStatus(_B)
avEnt3300mvPwrFltOk=NotificationType((1,3,6,1,4,1,6889,2,1,99,2,0,11))
avEnt3300mvPwrFltOk.setObjects(*((_A,_E),(_C,_D),(_G,_H),(_A,_O),(_A,_M),(_C,_I)))
if mibBuilder.loadTexts:avEnt3300mvPwrFltOk.setStatus(_B)
avEnt2500mvPwrFlt=NotificationType((1,3,6,1,4,1,6889,2,1,99,2,0,13))
avEnt2500mvPwrFlt.setObjects(*((_A,_E),(_C,_D),(_G,_H),(_A,_N),(_A,_L),(_C,_I)))
if mibBuilder.loadTexts:avEnt2500mvPwrFlt.setStatus(_B)
avEnt2500mvPwrFltOk=NotificationType((1,3,6,1,4,1,6889,2,1,99,2,0,14))
avEnt2500mvPwrFltOk.setObjects(*((_A,_E),(_C,_D),(_G,_H),(_A,_O),(_A,_M),(_C,_I)))
if mibBuilder.loadTexts:avEnt2500mvPwrFltOk.setStatus(_B)
avEnt1800mvPwrFlt=NotificationType((1,3,6,1,4,1,6889,2,1,99,2,0,16))
avEnt1800mvPwrFlt.setObjects(*((_A,_E),(_C,_D),(_G,_H),(_A,_N),(_A,_L),(_C,_I)))
if mibBuilder.loadTexts:avEnt1800mvPwrFlt.setStatus(_B)
avEnt1800mvPwrFltOk=NotificationType((1,3,6,1,4,1,6889,2,1,99,2,0,17))
avEnt1800mvPwrFltOk.setObjects(*((_A,_E),(_C,_D),(_G,_H),(_A,_O),(_A,_M),(_C,_I)))
if mibBuilder.loadTexts:avEnt1800mvPwrFltOk.setStatus(_B)
avEnt1600mvPwrFlt=NotificationType((1,3,6,1,4,1,6889,2,1,99,2,0,19))
avEnt1600mvPwrFlt.setObjects(*((_A,_E),(_C,_D),(_G,_H),(_A,_N),(_A,_L),(_C,_I)))
if mibBuilder.loadTexts:avEnt1600mvPwrFlt.setStatus(_B)
avEnt1600mvPwrFltOk=NotificationType((1,3,6,1,4,1,6889,2,1,99,2,0,20))
avEnt1600mvPwrFltOk.setObjects(*((_A,_E),(_C,_D),(_G,_H),(_A,_O),(_A,_M),(_C,_I)))
if mibBuilder.loadTexts:avEnt1600mvPwrFltOk.setStatus(_B)
avEntAmbientHiTempFlt=NotificationType((1,3,6,1,4,1,6889,2,1,99,2,0,22))
avEntAmbientHiTempFlt.setObjects(*((_A,_E),(_C,_D),(_G,_H),(_A,_N),(_C,_I)))
if mibBuilder.loadTexts:avEntAmbientHiTempFlt.setStatus(_B)
avEntAmbientHiTempFltOk=NotificationType((1,3,6,1,4,1,6889,2,1,99,2,0,23))
avEntAmbientHiTempFltOk.setObjects(*((_A,_E),(_C,_D),(_G,_H),(_A,_O),(_C,_I)))
if mibBuilder.loadTexts:avEntAmbientHiTempFltOk.setStatus(_B)
avEntAmbientLoTempFlt=NotificationType((1,3,6,1,4,1,6889,2,1,99,2,0,24))
avEntAmbientLoTempFlt.setObjects(*((_A,_E),(_C,_D),(_G,_H),(_A,_L),(_C,_I)))
if mibBuilder.loadTexts:avEntAmbientLoTempFlt.setStatus(_B)
avEntAmbientLoTempFltOk=NotificationType((1,3,6,1,4,1,6889,2,1,99,2,0,25))
avEntAmbientLoTempFltOk.setObjects(*((_A,_E),(_C,_D),(_G,_H),(_A,_M),(_C,_I)))
if mibBuilder.loadTexts:avEntAmbientLoTempFltOk.setStatus(_B)
avEntPhyUSBDeviceRemovalOnBackupRestoreOperation=NotificationType((1,3,6,1,4,1,6889,2,1,99,3,0,1))
avEntPhyUSBDeviceRemovalOnBackupRestoreOperation.setObjects(*((_A,_J),(_A,_K)))
if mibBuilder.loadTexts:avEntPhyUSBDeviceRemovalOnBackupRestoreOperation.setStatus(_B)
avEntPhyUSBDeviceInsecureRemoval=NotificationType((1,3,6,1,4,1,6889,2,1,99,3,0,2))
avEntPhyUSBDeviceInsecureRemoval.setObjects(*((_A,_E),(_C,_D),(_A,_S),(_A,_T),(_A,_U),(_A,_J),(_A,_K)))
if mibBuilder.loadTexts:avEntPhyUSBDeviceInsecureRemoval.setStatus(_B)
avEntPhyUSBDevicePowerFailure=NotificationType((1,3,6,1,4,1,6889,2,1,99,3,0,3))
avEntPhyUSBDevicePowerFailure.setObjects(*((_A,_E),(_C,_D),(_A,_S),(_A,_T),(_A,_U),(_A,_J),(_A,_K)))
if mibBuilder.loadTexts:avEntPhyUSBDevicePowerFailure.setStatus(_B)
avEntPhyUSBDeviceNotSupported=NotificationType((1,3,6,1,4,1,6889,2,1,99,3,0,4))
avEntPhyUSBDeviceNotSupported.setObjects(*((_A,_E),(_C,_D),(_A,_S),(_A,_T),(_A,_U),(_A,_J),(_A,_K)))
if mibBuilder.loadTexts:avEntPhyUSBDeviceNotSupported.setStatus(_B)
avEntPhyUSBDeviceExceedMaxNumber=NotificationType((1,3,6,1,4,1,6889,2,1,99,3,0,5))
avEntPhyUSBDeviceExceedMaxNumber.setObjects(*((_A,_E),(_C,_D),(_A,_S),(_A,_T),(_A,_U),(_A,_J),(_A,_K)))
if mibBuilder.loadTexts:avEntPhyUSBDeviceExceedMaxNumber.setStatus(_B)
avEntPhyUSBFileSystemNotSupported=NotificationType((1,3,6,1,4,1,6889,2,1,99,3,0,6))
avEntPhyUSBFileSystemNotSupported.setObjects(*((_A,_E),(_C,_D),(_A,_S),(_A,_T),(_A,_U),(_A,_J),(_A,_K)))
if mibBuilder.loadTexts:avEntPhyUSBFileSystemNotSupported.setStatus(_B)
avEntPhyChFruRemoval=NotificationType((1,3,6,1,4,1,6889,2,1,99,5,0,1))
avEntPhyChFruRemoval.setObjects(*((_A,_E),(_C,_D),(_A,_J),(_A,_K)))
if mibBuilder.loadTexts:avEntPhyChFruRemoval.setStatus(_B)
avEntPhyChFruInsertion=NotificationType((1,3,6,1,4,1,6889,2,1,99,5,0,2))
avEntPhyChFruInsertion.setObjects(*((_A,_E),(_C,_D),(_A,_J),(_A,_K)))
if mibBuilder.loadTexts:avEntPhyChFruInsertion.setStatus(_B)
avEntPhyChFruPsuFlt=NotificationType((1,3,6,1,4,1,6889,2,1,99,5,0,3))
avEntPhyChFruPsuFlt.setObjects(*((_A,_E),(_C,_D),(_A,_Q),(_A,_R),(_A,_J),(_A,_K)))
if mibBuilder.loadTexts:avEntPhyChFruPsuFlt.setStatus(_B)
avEntPhyChFruPsuFltOk=NotificationType((1,3,6,1,4,1,6889,2,1,99,5,0,4))
avEntPhyChFruPsuFltOk.setObjects(*((_A,_E),(_C,_D),(_A,_Q),(_A,_R),(_A,_J),(_A,_K)))
if mibBuilder.loadTexts:avEntPhyChFruPsuFltOk.setStatus(_B)
avEntPhyChFruExpansionTestFailure=NotificationType((1,3,6,1,4,1,6889,2,1,99,5,0,5))
avEntPhyChFruExpansionTestFailure.setObjects(*((_A,_E),(_C,_D),(_A,_Q),(_A,_R),(_A,_J),(_A,_K)))
if mibBuilder.loadTexts:avEntPhyChFruExpansionTestFailure.setStatus(_B)
avEntPhyChFruExpansionTestClear=NotificationType((1,3,6,1,4,1,6889,2,1,99,5,0,6))
avEntPhyChFruExpansionTestClear.setObjects(*((_A,_E),(_C,_D),(_A,_Q),(_A,_R),(_A,_J),(_A,_K)))
if mibBuilder.loadTexts:avEntPhyChFruExpansionTestClear.setStatus(_B)
avEntPhyChFruNotificationGroup=NotificationGroup((1,3,6,1,4,1,6889,2,1,99,5,3))
avEntPhyChFruNotificationGroup.setObjects(*((_A,_Z),(_A,_a),(_A,_b),(_A,_c)))
if mibBuilder.loadTexts:avEntPhyChFruNotificationGroup.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'AvEntPhyItuPerceivedSeverity':AvEntPhyItuPerceivedSeverity,'avayaEntity':avayaEntity,'avEntPhySensorTable':avEntPhySensorTable,'avEntPhySensorEntry':avEntPhySensorEntry,'avEntPhySensorHiShutdown':avEntPhySensorHiShutdown,_N:avEntPhySensorHiWarning,_O:avEntPhySensorHiWarningClear,_M:avEntPhySensorLoWarningClear,_L:avEntPhySensorLoWarning,'avEntPhySensorLoShutdown':avEntPhySensorLoShutdown,'avEntPhySensorEventSupportMask':avEntPhySensorEventSupportMask,'avEntTraps':avEntTraps,'avEntTrapsV3separator':avEntTrapsV3separator,'avEntFanFlt':avEntFanFlt,'avEntFanOk':avEntFanOk,'avEnt48vPwrFlt':avEnt48vPwrFlt,'avEnt48vPwrFltOk':avEnt48vPwrFltOk,'avEnt5vPwrFlt':avEnt5vPwrFlt,'avEnt5vPwrFltOk':avEnt5vPwrFltOk,'avEnt3300mvPwrFlt':avEnt3300mvPwrFlt,'avEnt3300mvPwrFltOk':avEnt3300mvPwrFltOk,'avEnt2500mvPwrFlt':avEnt2500mvPwrFlt,'avEnt2500mvPwrFltOk':avEnt2500mvPwrFltOk,'avEnt1800mvPwrFlt':avEnt1800mvPwrFlt,'avEnt1800mvPwrFltOk':avEnt1800mvPwrFltOk,'avEnt1600mvPwrFlt':avEnt1600mvPwrFlt,'avEnt1600mvPwrFltOk':avEnt1600mvPwrFltOk,'avEntAmbientHiTempFlt':avEntAmbientHiTempFlt,'avEntAmbientHiTempFltOk':avEntAmbientHiTempFltOk,'avEntAmbientLoTempFlt':avEntAmbientLoTempFlt,'avEntAmbientLoTempFltOk':avEntAmbientLoTempFltOk,'avEntPhyUSBDevices':avEntPhyUSBDevices,'avEntPhyUSBDevicesTraps':avEntPhyUSBDevicesTraps,'avEntPhyUSBDeviceRemovalOnBackupRestoreOperation':avEntPhyUSBDeviceRemovalOnBackupRestoreOperation,'avEntPhyUSBDeviceInsecureRemoval':avEntPhyUSBDeviceInsecureRemoval,'avEntPhyUSBDevicePowerFailure':avEntPhyUSBDevicePowerFailure,'avEntPhyUSBDeviceNotSupported':avEntPhyUSBDeviceNotSupported,'avEntPhyUSBDeviceExceedMaxNumber':avEntPhyUSBDeviceExceedMaxNumber,'avEntPhyUSBFileSystemNotSupported':avEntPhyUSBFileSystemNotSupported,'avEntPhyUSBDevicesTable':avEntPhyUSBDevicesTable,'avEntPhyUSBDevicesEntry':avEntPhyUSBDevicesEntry,_S:avEntPhyUSBDeviceUSBSupportVersion,'avEntPhyUSBDeviceClassCode':avEntPhyUSBDeviceClassCode,'avEntPhyUSBDeviceSubClassCode':avEntPhyUSBDeviceSubClassCode,'avEntPhyUSBDeviceProtocol':avEntPhyUSBDeviceProtocol,'avEntPhyUSBDeviceVendorId':avEntPhyUSBDeviceVendorId,_T:avEntPhyUSBDeviceSpeed,_U:avEntPhyUSBDevicePower,'avEntPhyUSBDeviceCurrent':avEntPhyUSBDeviceCurrent,'avEntPhyUSBMassStorageDevicesTable':avEntPhyUSBMassStorageDevicesTable,'avEntPhyUSBMassStorageDevicesEntry':avEntPhyUSBMassStorageDevicesEntry,'avEntPhyUSBMassStorageDeviceFileSystemName':avEntPhyUSBMassStorageDeviceFileSystemName,'avEntPhyUSBMassStorageDeviceCapacity':avEntPhyUSBMassStorageDeviceCapacity,'avEntPhyUSBMassStorageDeviceFreeMemory':avEntPhyUSBMassStorageDeviceFreeMemory,'avEntPhyUSBMassStorageDeviceFs':avEntPhyUSBMassStorageDeviceFs,'avEntPhyNotificationDefinitions':avEntPhyNotificationDefinitions,_K:avEntPhySeverity,_J:avEntPhyProductId,_E:avEntPhysicalIndex,'avEntPhyChFru':avEntPhyChFru,'avEntPhyChFruNotifications':avEntPhyChFruNotifications,_Z:avEntPhyChFruRemoval,_a:avEntPhyChFruInsertion,_b:avEntPhyChFruPsuFlt,_c:avEntPhyChFruPsuFltOk,'avEntPhyChFruExpansionTestFailure':avEntPhyChFruExpansionTestFailure,'avEntPhyChFruExpansionTestClear':avEntPhyChFruExpansionTestClear,'avEntPhyChFruTable':avEntPhyChFruTable,'avEntPhyChFruEntry':avEntPhyChFruEntry,_Q:avEntPhyChFruOperStat,_R:avEntPhyChFruFault,'avEntPhyChFruGroup':avEntPhyChFruGroup,'avEntPhyChFruNotificationGroup':avEntPhyChFruNotificationGroup})