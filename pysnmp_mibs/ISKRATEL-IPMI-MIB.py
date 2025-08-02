_e='minutes'
_d='msanShMCEventIndex'
_c='msanShMCChassisId'
_b='msanShMCShelfManagerSlotNumber'
_a='msanShMCPowerSupplySlotNumber'
_Z='msanShMCFanTraySlotNumber'
_Y='msanShMCBoardVariablesBoardBasicSlotNumber'
_X='msanShMCFruInfoIndex'
_W='msanShMCPefConfigurationAlertStringIndex'
_V='msanShMCPefConfigurationEventFilterIndex'
_U='msanShMCShelfIndex'
_T='msanShMCSelIndex'
_S='msanShMCBoardsIndex'
_R='msanShMCSensorIndex'
_Q='msanShMCFruDeviceIndex'
_P='msanShMCImpControllerIndex'
_O='cold'
_N='none'
_M='present'
_L='absent'
_K='OctetString'
_J='yes'
_I='no'
_H='off'
_G='ISKRATEL-IPMI-MIB'
_F='on'
_E='read-write'
_D='DisplayString'
_C='Integer32'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_K,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
msanAdditionalConf,=mibBuilder.importSymbols('ISKRATEL-MSAN-MIB','msanAdditionalConf')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_D,'PhysAddress','TextualConvention')
msanShMC=ModuleIdentity((1,3,6,1,4,1,1332,1,1,5,3,33))
_MsanShMCImpControllerVariablesTable_Object=MibTable
msanShMCImpControllerVariablesTable=_MsanShMCImpControllerVariablesTable_Object((1,3,6,1,4,1,1332,1,1,5,3,33,1))
if mibBuilder.loadTexts:msanShMCImpControllerVariablesTable.setStatus(_A)
_MsanShMCImpControllerVariablesEntry_Object=MibTableRow
msanShMCImpControllerVariablesEntry=_MsanShMCImpControllerVariablesEntry_Object((1,3,6,1,4,1,1332,1,1,5,3,33,1,1))
msanShMCImpControllerVariablesEntry.setIndexNames((0,_G,_P))
if mibBuilder.loadTexts:msanShMCImpControllerVariablesEntry.setStatus(_A)
class _MsanShMCImpControllerIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_MsanShMCImpControllerIndex_Type.__name__=_C
_MsanShMCImpControllerIndex_Object=MibTableColumn
msanShMCImpControllerIndex=_MsanShMCImpControllerIndex_Object((1,3,6,1,4,1,1332,1,1,5,3,33,1,1,1),_MsanShMCImpControllerIndex_Type())
msanShMCImpControllerIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:msanShMCImpControllerIndex.setStatus(_A)
class _MsanShMCImpControllerSdrVersion_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_MsanShMCImpControllerSdrVersion_Type.__name__=_C
_MsanShMCImpControllerSdrVersion_Object=MibTableColumn
msanShMCImpControllerSdrVersion=_MsanShMCImpControllerSdrVersion_Object((1,3,6,1,4,1,1332,1,1,5,3,33,1,1,2),_MsanShMCImpControllerSdrVersion_Type())
msanShMCImpControllerSdrVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:msanShMCImpControllerSdrVersion.setStatus(_A)
class _MsanShMCImpControllerPicmgVersion_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_MsanShMCImpControllerPicmgVersion_Type.__name__=_C
_MsanShMCImpControllerPicmgVersion_Object=MibTableColumn
msanShMCImpControllerPicmgVersion=_MsanShMCImpControllerPicmgVersion_Object((1,3,6,1,4,1,1332,1,1,5,3,33,1,1,3),_MsanShMCImpControllerPicmgVersion_Type())
msanShMCImpControllerPicmgVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:msanShMCImpControllerPicmgVersion.setStatus(_A)
class _MsanShMCImpControllerSlaveAddress_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_MsanShMCImpControllerSlaveAddress_Type.__name__=_C
_MsanShMCImpControllerSlaveAddress_Object=MibTableColumn
msanShMCImpControllerSlaveAddress=_MsanShMCImpControllerSlaveAddress_Object((1,3,6,1,4,1,1332,1,1,5,3,33,1,1,4),_MsanShMCImpControllerSlaveAddress_Type())
msanShMCImpControllerSlaveAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:msanShMCImpControllerSlaveAddress.setStatus(_A)
class _MsanShMCImpControllerChannelNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_MsanShMCImpControllerChannelNumber_Type.__name__=_C
_MsanShMCImpControllerChannelNumber_Object=MibTableColumn
msanShMCImpControllerChannelNumber=_MsanShMCImpControllerChannelNumber_Object((1,3,6,1,4,1,1332,1,1,5,3,33,1,1,5),_MsanShMCImpControllerChannelNumber_Type())
msanShMCImpControllerChannelNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:msanShMCImpControllerChannelNumber.setStatus(_A)
class _MsanShMCImpControllerPowerStateNotification_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_MsanShMCImpControllerPowerStateNotification_Type.__name__=_C
_MsanShMCImpControllerPowerStateNotification_Object=MibTableColumn
msanShMCImpControllerPowerStateNotification=_MsanShMCImpControllerPowerStateNotification_Object((1,3,6,1,4,1,1332,1,1,5,3,33,1,1,6),_MsanShMCImpControllerPowerStateNotification_Type())
msanShMCImpControllerPowerStateNotification.setMaxAccess(_B)
if mibBuilder.loadTexts:msanShMCImpControllerPowerStateNotification.setStatus(_A)
class _MsanShMCImpControllerGlobalInitialisation_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_MsanShMCImpControllerGlobalInitialisation_Type.__name__=_C
_MsanShMCImpControllerGlobalInitialisation_Object=MibTableColumn
msanShMCImpControllerGlobalInitialisation=_MsanShMCImpControllerGlobalInitialisation_Object((1,3,6,1,4,1,1332,1,1,5,3,33,1,1,7),_MsanShMCImpControllerGlobalInitialisation_Type())
msanShMCImpControllerGlobalInitialisation.setMaxAccess(_B)
if mibBuilder.loadTexts:msanShMCImpControllerGlobalInitialisation.setStatus(_A)
class _MsanShMCImpControllerCapabilities_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_MsanShMCImpControllerCapabilities_Type.__name__=_C
_MsanShMCImpControllerCapabilities_Object=MibTableColumn
msanShMCImpControllerCapabilities=_MsanShMCImpControllerCapabilities_Object((1,3,6,1,4,1,1332,1,1,5,3,33,1,1,8),_MsanShMCImpControllerCapabilities_Type())
msanShMCImpControllerCapabilities.setMaxAccess(_B)
if mibBuilder.loadTexts:msanShMCImpControllerCapabilities.setStatus(_A)
class _MsanShMCImpControllerIdString_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_MsanShMCImpControllerIdString_Type.__name__=_D
_MsanShMCImpControllerIdString_Object=MibTableColumn
msanShMCImpControllerIdString=_MsanShMCImpControllerIdString_Object((1,3,6,1,4,1,1332,1,1,5,3,33,1,1,9),_MsanShMCImpControllerIdString_Type())
msanShMCImpControllerIdString.setMaxAccess(_B)
if mibBuilder.loadTexts:msanShMCImpControllerIdString.setStatus(_A)
class _MsanShMCImpControllerMaximumFru_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_MsanShMCImpControllerMaximumFru_Type.__name__=_C
_MsanShMCImpControllerMaximumFru_Object=MibTableColumn
msanShMCImpControllerMaximumFru=_MsanShMCImpControllerMaximumFru_Object((1,3,6,1,4,1,1332,1,1,5,3,33,1,1,10),_MsanShMCImpControllerMaximumFru_Type())
msanShMCImpControllerMaximumFru.setMaxAccess(_B)
if mibBuilder.loadTexts:msanShMCImpControllerMaximumFru.setStatus(_A)
class _MsanShMCImpControllerOwnFruId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_MsanShMCImpControllerOwnFruId_Type.__name__=_C
_MsanShMCImpControllerOwnFruId_Object=MibTableColumn
msanShMCImpControllerOwnFruId=_MsanShMCImpControllerOwnFruId_Object((1,3,6,1,4,1,1332,1,1,5,3,33,1,1,11),_MsanShMCImpControllerOwnFruId_Type())
msanShMCImpControllerOwnFruId.setMaxAccess(_B)
if mibBuilder.loadTexts:msanShMCImpControllerOwnFruId.setStatus(_A)
_MsanShMCFruDeviceVariablesTable_Object=MibTable
msanShMCFruDeviceVariablesTable=_MsanShMCFruDeviceVariablesTable_Object((1,3,6,1,4,1,1332,1,1,5,3,33,2))
if mibBuilder.loadTexts:msanShMCFruDeviceVariablesTable.setStatus(_A)
_MsanShMCFruDeviceVariablesEntry_Object=MibTableRow
msanShMCFruDeviceVariablesEntry=_MsanShMCFruDeviceVariablesEntry_Object((1,3,6,1,4,1,1332,1,1,5,3,33,2,1))
msanShMCFruDeviceVariablesEntry.setIndexNames((0,_G,_Q))
if mibBuilder.loadTexts:msanShMCFruDeviceVariablesEntry.setStatus(_A)
class _MsanShMCFruDeviceIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,-1))
_MsanShMCFruDeviceIndex_Type.__name__=_C
_MsanShMCFruDeviceIndex_Object=MibTableColumn
msanShMCFruDeviceIndex=_MsanShMCFruDeviceIndex_Object((1,3,6,1,4,1,1332,1,1,5,3,33,2,1,1),_MsanShMCFruDeviceIndex_Type())
msanShMCFruDeviceIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:msanShMCFruDeviceIndex.setStatus(_A)
class _MsanShMCFruDeviceSdrVersion_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_MsanShMCFruDeviceSdrVersion_Type.__name__=_C
_MsanShMCFruDeviceSdrVersion_Object=MibTableColumn
msanShMCFruDeviceSdrVersion=_MsanShMCFruDeviceSdrVersion_Object((1,3,6,1,4,1,1332,1,1,5,3,33,2,1,2),_MsanShMCFruDeviceSdrVersion_Type())
msanShMCFruDeviceSdrVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:msanShMCFruDeviceSdrVersion.setStatus(_A)
class _MsanShMCFruDeviceSlaveAddress_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_MsanShMCFruDeviceSlaveAddress_Type.__name__=_C
_MsanShMCFruDeviceSlaveAddress_Object=MibTableColumn
msanShMCFruDeviceSlaveAddress=_MsanShMCFruDeviceSlaveAddress_Object((1,3,6,1,4,1,1332,1,1,5,3,33,2,1,3),_MsanShMCFruDeviceSlaveAddress_Type())
msanShMCFruDeviceSlaveAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:msanShMCFruDeviceSlaveAddress.setStatus(_A)
class _MsanShMCFruDeviceSFruDeviceId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_MsanShMCFruDeviceSFruDeviceId_Type.__name__=_C
_MsanShMCFruDeviceSFruDeviceId_Object=MibTableColumn
msanShMCFruDeviceSFruDeviceId=_MsanShMCFruDeviceSFruDeviceId_Object((1,3,6,1,4,1,1332,1,1,5,3,33,2,1,4),_MsanShMCFruDeviceSFruDeviceId_Type())
msanShMCFruDeviceSFruDeviceId.setMaxAccess(_B)
if mibBuilder.loadTexts:msanShMCFruDeviceSFruDeviceId.setStatus(_A)
class _MsanShMCFruDeviceChannelNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_MsanShMCFruDeviceChannelNumber_Type.__name__=_C
_MsanShMCFruDeviceChannelNumber_Object=MibTableColumn
msanShMCFruDeviceChannelNumber=_MsanShMCFruDeviceChannelNumber_Object((1,3,6,1,4,1,1332,1,1,5,3,33,2,1,5),_MsanShMCFruDeviceChannelNumber_Type())
msanShMCFruDeviceChannelNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:msanShMCFruDeviceChannelNumber.setStatus(_A)
class _MsanShMCFruDeviceDeviceType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_MsanShMCFruDeviceDeviceType_Type.__name__=_C
_MsanShMCFruDeviceDeviceType_Object=MibTableColumn
msanShMCFruDeviceDeviceType=_MsanShMCFruDeviceDeviceType_Object((1,3,6,1,4,1,1332,1,1,5,3,33,2,1,6),_MsanShMCFruDeviceDeviceType_Type())
msanShMCFruDeviceDeviceType.setMaxAccess(_B)
if mibBuilder.loadTexts:msanShMCFruDeviceDeviceType.setStatus(_A)
class _MsanShMCFruDeviceDeviceTypeModifier_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_MsanShMCFruDeviceDeviceTypeModifier_Type.__name__=_C
_MsanShMCFruDeviceDeviceTypeModifier_Object=MibTableColumn
msanShMCFruDeviceDeviceTypeModifier=_MsanShMCFruDeviceDeviceTypeModifier_Object((1,3,6,1,4,1,1332,1,1,5,3,33,2,1,7),_MsanShMCFruDeviceDeviceTypeModifier_Type())
msanShMCFruDeviceDeviceTypeModifier.setMaxAccess(_B)
if mibBuilder.loadTexts:msanShMCFruDeviceDeviceTypeModifier.setStatus(_A)
class _MsanShMCFruDeviceFruEntityId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_MsanShMCFruDeviceFruEntityId_Type.__name__=_C
_MsanShMCFruDeviceFruEntityId_Object=MibTableColumn
msanShMCFruDeviceFruEntityId=_MsanShMCFruDeviceFruEntityId_Object((1,3,6,1,4,1,1332,1,1,5,3,33,2,1,8),_MsanShMCFruDeviceFruEntityId_Type())
msanShMCFruDeviceFruEntityId.setMaxAccess(_B)
if mibBuilder.loadTexts:msanShMCFruDeviceFruEntityId.setStatus(_A)
class _MsanShMCFruDeviceFruEntityInstance_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_MsanShMCFruDeviceFruEntityInstance_Type.__name__=_C
_MsanShMCFruDeviceFruEntityInstance_Object=MibTableColumn
msanShMCFruDeviceFruEntityInstance=_MsanShMCFruDeviceFruEntityInstance_Object((1,3,6,1,4,1,1332,1,1,5,3,33,2,1,9),_MsanShMCFruDeviceFruEntityInstance_Type())
msanShMCFruDeviceFruEntityInstance.setMaxAccess(_B)
if mibBuilder.loadTexts:msanShMCFruDeviceFruEntityInstance.setStatus(_A)
class _MsanShMCFruDeviceIdString_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_MsanShMCFruDeviceIdString_Type.__name__=_D
_MsanShMCFruDeviceIdString_Object=MibTableColumn
msanShMCFruDeviceIdString=_MsanShMCFruDeviceIdString_Object((1,3,6,1,4,1,1332,1,1,5,3,33,2,1,10),_MsanShMCFruDeviceIdString_Type())
msanShMCFruDeviceIdString.setMaxAccess(_B)
if mibBuilder.loadTexts:msanShMCFruDeviceIdString.setStatus(_A)
class _MsanShMCFruDeviceHotSwapState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_MsanShMCFruDeviceHotSwapState_Type.__name__=_C
_MsanShMCFruDeviceHotSwapState_Object=MibTableColumn
msanShMCFruDeviceHotSwapState=_MsanShMCFruDeviceHotSwapState_Object((1,3,6,1,4,1,1332,1,1,5,3,33,2,1,11),_MsanShMCFruDeviceHotSwapState_Type())
msanShMCFruDeviceHotSwapState.setMaxAccess(_B)
if mibBuilder.loadTexts:msanShMCFruDeviceHotSwapState.setStatus(_A)
class _MsanShMCFruDeviceActivated_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_MsanShMCFruDeviceActivated_Type.__name__=_C
_MsanShMCFruDeviceActivated_Object=MibTableColumn
msanShMCFruDeviceActivated=_MsanShMCFruDeviceActivated_Object((1,3,6,1,4,1,1332,1,1,5,3,33,2,1,12),_MsanShMCFruDeviceActivated_Type())
msanShMCFruDeviceActivated.setMaxAccess(_E)
if mibBuilder.loadTexts:msanShMCFruDeviceActivated.setStatus(_A)
_MsanShMCSensorVariablesTable_Object=MibTable
msanShMCSensorVariablesTable=_MsanShMCSensorVariablesTable_Object((1,3,6,1,4,1,1332,1,1,5,3,33,3))
if mibBuilder.loadTexts:msanShMCSensorVariablesTable.setStatus(_A)
_MsanShMCSensorVariablesEntry_Object=MibTableRow
msanShMCSensorVariablesEntry=_MsanShMCSensorVariablesEntry_Object((1,3,6,1,4,1,1332,1,1,5,3,33,3,1))
msanShMCSensorVariablesEntry.setIndexNames((0,_G,_R))
if mibBuilder.loadTexts:msanShMCSensorVariablesEntry.setStatus(_A)
class _MsanShMCSensorIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,-1))
_MsanShMCSensorIndex_Type.__name__=_C
_MsanShMCSensorIndex_Object=MibTableColumn
msanShMCSensorIndex=_MsanShMCSensorIndex_Object((1,3,6,1,4,1,1332,1,1,5,3,33,3,1,1),_MsanShMCSensorIndex_Type())
msanShMCSensorIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:msanShMCSensorIndex.setStatus(_A)
class _MsanShMCSensorSdrVersion_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_MsanShMCSensorSdrVersion_Type.__name__=_C
_MsanShMCSensorSdrVersion_Object=MibTableColumn
msanShMCSensorSdrVersion=_MsanShMCSensorSdrVersion_Object((1,3,6,1,4,1,1332,1,1,5,3,33,3,1,2),_MsanShMCSensorSdrVersion_Type())
msanShMCSensorSdrVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:msanShMCSensorSdrVersion.setStatus(_A)
class _MsanShMCSensorRecordType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_MsanShMCSensorRecordType_Type.__name__=_C
_MsanShMCSensorRecordType_Object=MibTableColumn
msanShMCSensorRecordType=_MsanShMCSensorRecordType_Object((1,3,6,1,4,1,1332,1,1,5,3,33,3,1,3),_MsanShMCSensorRecordType_Type())
msanShMCSensorRecordType.setMaxAccess(_B)
if mibBuilder.loadTexts:msanShMCSensorRecordType.setStatus(_A)
class _MsanShMCSensorOwnerId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_MsanShMCSensorOwnerId_Type.__name__=_C
_MsanShMCSensorOwnerId_Object=MibTableColumn
msanShMCSensorOwnerId=_MsanShMCSensorOwnerId_Object((1,3,6,1,4,1,1332,1,1,5,3,33,3,1,4),_MsanShMCSensorOwnerId_Type())
msanShMCSensorOwnerId.setMaxAccess(_B)
if mibBuilder.loadTexts:msanShMCSensorOwnerId.setStatus(_A)
class _MsanShMCSensorOwnerLun_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_MsanShMCSensorOwnerLun_Type.__name__=_C
_MsanShMCSensorOwnerLun_Object=MibTableColumn
msanShMCSensorOwnerLun=_MsanShMCSensorOwnerLun_Object((1,3,6,1,4,1,1332,1,1,5,3,33,3,1,5),_MsanShMCSensorOwnerLun_Type())
msanShMCSensorOwnerLun.setMaxAccess(_B)
if mibBuilder.loadTexts:msanShMCSensorOwnerLun.setStatus(_A)
class _MsanShMCSensorNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_MsanShMCSensorNumber_Type.__name__=_C
_MsanShMCSensorNumber_Object=MibTableColumn
msanShMCSensorNumber=_MsanShMCSensorNumber_Object((1,3,6,1,4,1,1332,1,1,5,3,33,3,1,6),_MsanShMCSensorNumber_Type())
msanShMCSensorNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:msanShMCSensorNumber.setStatus(_A)
class _MsanShMCSensorEntityInstance_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_MsanShMCSensorEntityInstance_Type.__name__=_C
_MsanShMCSensorEntityInstance_Object=MibTableColumn
msanShMCSensorEntityInstance=_MsanShMCSensorEntityInstance_Object((1,3,6,1,4,1,1332,1,1,5,3,33,3,1,7),_MsanShMCSensorEntityInstance_Type())
msanShMCSensorEntityInstance.setMaxAccess(_B)
if mibBuilder.loadTexts:msanShMCSensorEntityInstance.setStatus(_A)
class _MsanShMCSensorEntityId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_MsanShMCSensorEntityId_Type.__name__=_C
_MsanShMCSensorEntityId_Object=MibTableColumn
msanShMCSensorEntityId=_MsanShMCSensorEntityId_Object((1,3,6,1,4,1,1332,1,1,5,3,33,3,1,8),_MsanShMCSensorEntityId_Type())
msanShMCSensorEntityId.setMaxAccess(_B)
if mibBuilder.loadTexts:msanShMCSensorEntityId.setStatus(_A)
class _MsanShMCSensorInitialisation_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_MsanShMCSensorInitialisation_Type.__name__=_C
_MsanShMCSensorInitialisation_Object=MibTableColumn
msanShMCSensorInitialisation=_MsanShMCSensorInitialisation_Object((1,3,6,1,4,1,1332,1,1,5,3,33,3,1,9),_MsanShMCSensorInitialisation_Type())
msanShMCSensorInitialisation.setMaxAccess(_B)
if mibBuilder.loadTexts:msanShMCSensorInitialisation.setStatus(_A)
class _MsanShMCSensorCapabilities_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_MsanShMCSensorCapabilities_Type.__name__=_C
_MsanShMCSensorCapabilities_Object=MibTableColumn
msanShMCSensorCapabilities=_MsanShMCSensorCapabilities_Object((1,3,6,1,4,1,1332,1,1,5,3,33,3,1,10),_MsanShMCSensorCapabilities_Type())
msanShMCSensorCapabilities.setMaxAccess(_B)
if mibBuilder.loadTexts:msanShMCSensorCapabilities.setStatus(_A)
class _MsanShMCSensorType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_MsanShMCSensorType_Type.__name__=_C
_MsanShMCSensorType_Object=MibTableColumn
msanShMCSensorType=_MsanShMCSensorType_Object((1,3,6,1,4,1,1332,1,1,5,3,33,3,1,11),_MsanShMCSensorType_Type())
msanShMCSensorType.setMaxAccess(_B)
if mibBuilder.loadTexts:msanShMCSensorType.setStatus(_A)
class _MsanShMCSensorEvent_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_MsanShMCSensorEvent_Type.__name__=_C
_MsanShMCSensorEvent_Object=MibTableColumn
msanShMCSensorEvent=_MsanShMCSensorEvent_Object((1,3,6,1,4,1,1332,1,1,5,3,33,3,1,12),_MsanShMCSensorEvent_Type())
msanShMCSensorEvent.setMaxAccess(_B)
if mibBuilder.loadTexts:msanShMCSensorEvent.setStatus(_A)
class _MsanShMCSensorAssertionEventMask_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_MsanShMCSensorAssertionEventMask_Type.__name__=_C
_MsanShMCSensorAssertionEventMask_Object=MibTableColumn
msanShMCSensorAssertionEventMask=_MsanShMCSensorAssertionEventMask_Object((1,3,6,1,4,1,1332,1,1,5,3,33,3,1,13),_MsanShMCSensorAssertionEventMask_Type())
msanShMCSensorAssertionEventMask.setMaxAccess(_B)
if mibBuilder.loadTexts:msanShMCSensorAssertionEventMask.setStatus(_A)
class _MsanShMCSensorDeassertionEventMask_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_MsanShMCSensorDeassertionEventMask_Type.__name__=_C
_MsanShMCSensorDeassertionEventMask_Object=MibTableColumn
msanShMCSensorDeassertionEventMask=_MsanShMCSensorDeassertionEventMask_Object((1,3,6,1,4,1,1332,1,1,5,3,33,3,1,14),_MsanShMCSensorDeassertionEventMask_Type())
msanShMCSensorDeassertionEventMask.setMaxAccess(_B)
if mibBuilder.loadTexts:msanShMCSensorDeassertionEventMask.setStatus(_A)
class _MsanShMCSensorMask_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_MsanShMCSensorMask_Type.__name__=_C
_MsanShMCSensorMask_Object=MibTableColumn
msanShMCSensorMask=_MsanShMCSensorMask_Object((1,3,6,1,4,1,1332,1,1,5,3,33,3,1,15),_MsanShMCSensorMask_Type())
msanShMCSensorMask.setMaxAccess(_B)
if mibBuilder.loadTexts:msanShMCSensorMask.setStatus(_A)
class _MsanShMCSensorUnit1_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_MsanShMCSensorUnit1_Type.__name__=_C
_MsanShMCSensorUnit1_Object=MibTableColumn
msanShMCSensorUnit1=_MsanShMCSensorUnit1_Object((1,3,6,1,4,1,1332,1,1,5,3,33,3,1,16),_MsanShMCSensorUnit1_Type())
msanShMCSensorUnit1.setMaxAccess(_B)
if mibBuilder.loadTexts:msanShMCSensorUnit1.setStatus(_A)
class _MsanShMCSensorUnit2_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_MsanShMCSensorUnit2_Type.__name__=_C
_MsanShMCSensorUnit2_Object=MibTableColumn
msanShMCSensorUnit2=_MsanShMCSensorUnit2_Object((1,3,6,1,4,1,1332,1,1,5,3,33,3,1,17),_MsanShMCSensorUnit2_Type())
msanShMCSensorUnit2.setMaxAccess(_B)
if mibBuilder.loadTexts:msanShMCSensorUnit2.setStatus(_A)
class _MsanShMCSensorUnit3_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_MsanShMCSensorUnit3_Type.__name__=_C
_MsanShMCSensorUnit3_Object=MibTableColumn
msanShMCSensorUnit3=_MsanShMCSensorUnit3_Object((1,3,6,1,4,1,1332,1,1,5,3,33,3,1,18),_MsanShMCSensorUnit3_Type())
msanShMCSensorUnit3.setMaxAccess(_B)
if mibBuilder.loadTexts:msanShMCSensorUnit3.setStatus(_A)
class _MsanShMCSensorLinearization_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_MsanShMCSensorLinearization_Type.__name__=_C
_MsanShMCSensorLinearization_Object=MibTableColumn
msanShMCSensorLinearization=_MsanShMCSensorLinearization_Object((1,3,6,1,4,1,1332,1,1,5,3,33,3,1,19),_MsanShMCSensorLinearization_Type())
msanShMCSensorLinearization.setMaxAccess(_B)
if mibBuilder.loadTexts:msanShMCSensorLinearization.setStatus(_A)
class _MsanShMCSensorM_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_MsanShMCSensorM_Type.__name__=_C
_MsanShMCSensorM_Object=MibTableColumn
msanShMCSensorM=_MsanShMCSensorM_Object((1,3,6,1,4,1,1332,1,1,5,3,33,3,1,20),_MsanShMCSensorM_Type())
msanShMCSensorM.setMaxAccess(_B)
if mibBuilder.loadTexts:msanShMCSensorM.setStatus(_A)
class _MsanShMCSensorTolerance_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_MsanShMCSensorTolerance_Type.__name__=_C
_MsanShMCSensorTolerance_Object=MibTableColumn
msanShMCSensorTolerance=_MsanShMCSensorTolerance_Object((1,3,6,1,4,1,1332,1,1,5,3,33,3,1,21),_MsanShMCSensorTolerance_Type())
msanShMCSensorTolerance.setMaxAccess(_B)
if mibBuilder.loadTexts:msanShMCSensorTolerance.setStatus(_A)
class _MsanShMCSensorB_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_MsanShMCSensorB_Type.__name__=_C
_MsanShMCSensorB_Object=MibTableColumn
msanShMCSensorB=_MsanShMCSensorB_Object((1,3,6,1,4,1,1332,1,1,5,3,33,3,1,22),_MsanShMCSensorB_Type())
msanShMCSensorB.setMaxAccess(_B)
if mibBuilder.loadTexts:msanShMCSensorB.setStatus(_A)
class _MsanShMCSensorAccuracy_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_MsanShMCSensorAccuracy_Type.__name__=_C
_MsanShMCSensorAccuracy_Object=MibTableColumn
msanShMCSensorAccuracy=_MsanShMCSensorAccuracy_Object((1,3,6,1,4,1,1332,1,1,5,3,33,3,1,23),_MsanShMCSensorAccuracy_Type())
msanShMCSensorAccuracy.setMaxAccess(_B)
if mibBuilder.loadTexts:msanShMCSensorAccuracy.setStatus(_A)
class _MsanShMCSensorAccuracyExp_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_MsanShMCSensorAccuracyExp_Type.__name__=_C
_MsanShMCSensorAccuracyExp_Object=MibTableColumn
msanShMCSensorAccuracyExp=_MsanShMCSensorAccuracyExp_Object((1,3,6,1,4,1,1332,1,1,5,3,33,3,1,24),_MsanShMCSensorAccuracyExp_Type())
msanShMCSensorAccuracyExp.setMaxAccess(_B)
if mibBuilder.loadTexts:msanShMCSensorAccuracyExp.setStatus(_A)
class _MsanShMCSensorRexp_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_MsanShMCSensorRexp_Type.__name__=_C
_MsanShMCSensorRexp_Object=MibTableColumn
msanShMCSensorRexp=_MsanShMCSensorRexp_Object((1,3,6,1,4,1,1332,1,1,5,3,33,3,1,25),_MsanShMCSensorRexp_Type())
msanShMCSensorRexp.setMaxAccess(_B)
if mibBuilder.loadTexts:msanShMCSensorRexp.setStatus(_A)
class _MsanShMCSensorBexp_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_MsanShMCSensorBexp_Type.__name__=_C
_MsanShMCSensorBexp_Object=MibTableColumn
msanShMCSensorBexp=_MsanShMCSensorBexp_Object((1,3,6,1,4,1,1332,1,1,5,3,33,3,1,26),_MsanShMCSensorBexp_Type())
msanShMCSensorBexp.setMaxAccess(_B)
if mibBuilder.loadTexts:msanShMCSensorBexp.setStatus(_A)
class _MsanShMCSensorCharacteristicFlags_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_MsanShMCSensorCharacteristicFlags_Type.__name__=_C
_MsanShMCSensorCharacteristicFlags_Object=MibTableColumn
msanShMCSensorCharacteristicFlags=_MsanShMCSensorCharacteristicFlags_Object((1,3,6,1,4,1,1332,1,1,5,3,33,3,1,27),_MsanShMCSensorCharacteristicFlags_Type())
msanShMCSensorCharacteristicFlags.setMaxAccess(_B)
if mibBuilder.loadTexts:msanShMCSensorCharacteristicFlags.setStatus(_A)
class _MsanShMCSensorReading_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_MsanShMCSensorReading_Type.__name__=_C
_MsanShMCSensorReading_Object=MibTableColumn
msanShMCSensorReading=_MsanShMCSensorReading_Object((1,3,6,1,4,1,1332,1,1,5,3,33,3,1,28),_MsanShMCSensorReading_Type())
msanShMCSensorReading.setMaxAccess(_B)
if mibBuilder.loadTexts:msanShMCSensorReading.setStatus(_A)
class _MsanShMCSensorProcessedReading_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_MsanShMCSensorProcessedReading_Type.__name__=_D
_MsanShMCSensorProcessedReading_Object=MibTableColumn
msanShMCSensorProcessedReading=_MsanShMCSensorProcessedReading_Object((1,3,6,1,4,1,1332,1,1,5,3,33,3,1,29),_MsanShMCSensorProcessedReading_Type())
msanShMCSensorProcessedReading.setMaxAccess(_B)
if mibBuilder.loadTexts:msanShMCSensorProcessedReading.setStatus(_A)
class _MsanShMCSensorNominalReading_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_MsanShMCSensorNominalReading_Type.__name__=_C
_MsanShMCSensorNominalReading_Object=MibTableColumn
msanShMCSensorNominalReading=_MsanShMCSensorNominalReading_Object((1,3,6,1,4,1,1332,1,1,5,3,33,3,1,30),_MsanShMCSensorNominalReading_Type())
msanShMCSensorNominalReading.setMaxAccess(_B)
if mibBuilder.loadTexts:msanShMCSensorNominalReading.setStatus(_A)
class _MsanShMCSensorNormalMaximum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_MsanShMCSensorNormalMaximum_Type.__name__=_C
_MsanShMCSensorNormalMaximum_Object=MibTableColumn
msanShMCSensorNormalMaximum=_MsanShMCSensorNormalMaximum_Object((1,3,6,1,4,1,1332,1,1,5,3,33,3,1,31),_MsanShMCSensorNormalMaximum_Type())
msanShMCSensorNormalMaximum.setMaxAccess(_B)
if mibBuilder.loadTexts:msanShMCSensorNormalMaximum.setStatus(_A)
class _MsanShMCSensorNormalMinimum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_MsanShMCSensorNormalMinimum_Type.__name__=_C
_MsanShMCSensorNormalMinimum_Object=MibTableColumn
msanShMCSensorNormalMinimum=_MsanShMCSensorNormalMinimum_Object((1,3,6,1,4,1,1332,1,1,5,3,33,3,1,32),_MsanShMCSensorNormalMinimum_Type())
msanShMCSensorNormalMinimum.setMaxAccess(_B)
if mibBuilder.loadTexts:msanShMCSensorNormalMinimum.setStatus(_A)
class _MsanShMCSensorMaximumReading_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_MsanShMCSensorMaximumReading_Type.__name__=_C
_MsanShMCSensorMaximumReading_Object=MibTableColumn
msanShMCSensorMaximumReading=_MsanShMCSensorMaximumReading_Object((1,3,6,1,4,1,1332,1,1,5,3,33,3,1,33),_MsanShMCSensorMaximumReading_Type())
msanShMCSensorMaximumReading.setMaxAccess(_B)
if mibBuilder.loadTexts:msanShMCSensorMaximumReading.setStatus(_A)
class _MsanShMCSensorMinimumReading_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_MsanShMCSensorMinimumReading_Type.__name__=_C
_MsanShMCSensorMinimumReading_Object=MibTableColumn
msanShMCSensorMinimumReading=_MsanShMCSensorMinimumReading_Object((1,3,6,1,4,1,1332,1,1,5,3,33,3,1,34),_MsanShMCSensorMinimumReading_Type())
msanShMCSensorMinimumReading.setMaxAccess(_B)
if mibBuilder.loadTexts:msanShMCSensorMinimumReading.setStatus(_A)
class _MsanShMCSensorUpperNonRecoverableThr_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_MsanShMCSensorUpperNonRecoverableThr_Type.__name__=_C
_MsanShMCSensorUpperNonRecoverableThr_Object=MibTableColumn
msanShMCSensorUpperNonRecoverableThr=_MsanShMCSensorUpperNonRecoverableThr_Object((1,3,6,1,4,1,1332,1,1,5,3,33,3,1,35),_MsanShMCSensorUpperNonRecoverableThr_Type())
msanShMCSensorUpperNonRecoverableThr.setMaxAccess(_B)
if mibBuilder.loadTexts:msanShMCSensorUpperNonRecoverableThr.setStatus(_A)
class _MsanShMCSensorUpperCriticalThr_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_MsanShMCSensorUpperCriticalThr_Type.__name__=_C
_MsanShMCSensorUpperCriticalThr_Object=MibTableColumn
msanShMCSensorUpperCriticalThr=_MsanShMCSensorUpperCriticalThr_Object((1,3,6,1,4,1,1332,1,1,5,3,33,3,1,36),_MsanShMCSensorUpperCriticalThr_Type())
msanShMCSensorUpperCriticalThr.setMaxAccess(_B)
if mibBuilder.loadTexts:msanShMCSensorUpperCriticalThr.setStatus(_A)
class _MsanShMCSensorUpperNonCriticalThr_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_MsanShMCSensorUpperNonCriticalThr_Type.__name__=_C
_MsanShMCSensorUpperNonCriticalThr_Object=MibTableColumn
msanShMCSensorUpperNonCriticalThr=_MsanShMCSensorUpperNonCriticalThr_Object((1,3,6,1,4,1,1332,1,1,5,3,33,3,1,37),_MsanShMCSensorUpperNonCriticalThr_Type())
msanShMCSensorUpperNonCriticalThr.setMaxAccess(_B)
if mibBuilder.loadTexts:msanShMCSensorUpperNonCriticalThr.setStatus(_A)
class _MsanShMCSensorLowerNonRecoverableThr_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_MsanShMCSensorLowerNonRecoverableThr_Type.__name__=_C
_MsanShMCSensorLowerNonRecoverableThr_Object=MibTableColumn
msanShMCSensorLowerNonRecoverableThr=_MsanShMCSensorLowerNonRecoverableThr_Object((1,3,6,1,4,1,1332,1,1,5,3,33,3,1,38),_MsanShMCSensorLowerNonRecoverableThr_Type())
msanShMCSensorLowerNonRecoverableThr.setMaxAccess(_B)
if mibBuilder.loadTexts:msanShMCSensorLowerNonRecoverableThr.setStatus(_A)
class _MsanShMCSensorLowerCriticalThr_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_MsanShMCSensorLowerCriticalThr_Type.__name__=_C
_MsanShMCSensorLowerCriticalThr_Object=MibTableColumn
msanShMCSensorLowerCriticalThr=_MsanShMCSensorLowerCriticalThr_Object((1,3,6,1,4,1,1332,1,1,5,3,33,3,1,39),_MsanShMCSensorLowerCriticalThr_Type())
msanShMCSensorLowerCriticalThr.setMaxAccess(_B)
if mibBuilder.loadTexts:msanShMCSensorLowerCriticalThr.setStatus(_A)
class _MsanShMCSensorLowerNonCriticalThr_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_MsanShMCSensorLowerNonCriticalThr_Type.__name__=_C
_MsanShMCSensorLowerNonCriticalThr_Object=MibTableColumn
msanShMCSensorLowerNonCriticalThr=_MsanShMCSensorLowerNonCriticalThr_Object((1,3,6,1,4,1,1332,1,1,5,3,33,3,1,40),_MsanShMCSensorLowerNonCriticalThr_Type())
msanShMCSensorLowerNonCriticalThr.setMaxAccess(_B)
if mibBuilder.loadTexts:msanShMCSensorLowerNonCriticalThr.setStatus(_A)
class _MsanShMCSensorPositiveGoingThrHysteresis_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_MsanShMCSensorPositiveGoingThrHysteresis_Type.__name__=_C
_MsanShMCSensorPositiveGoingThrHysteresis_Object=MibTableColumn
msanShMCSensorPositiveGoingThrHysteresis=_MsanShMCSensorPositiveGoingThrHysteresis_Object((1,3,6,1,4,1,1332,1,1,5,3,33,3,1,41),_MsanShMCSensorPositiveGoingThrHysteresis_Type())
msanShMCSensorPositiveGoingThrHysteresis.setMaxAccess(_B)
if mibBuilder.loadTexts:msanShMCSensorPositiveGoingThrHysteresis.setStatus(_A)
class _MsanShMCSensorNegativeGoingThrHysteresis_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_MsanShMCSensorNegativeGoingThrHysteresis_Type.__name__=_C
_MsanShMCSensorNegativeGoingThrHysteresis_Object=MibTableColumn
msanShMCSensorNegativeGoingThrHysteresis=_MsanShMCSensorNegativeGoingThrHysteresis_Object((1,3,6,1,4,1,1332,1,1,5,3,33,3,1,42),_MsanShMCSensorNegativeGoingThrHysteresis_Type())
msanShMCSensorNegativeGoingThrHysteresis.setMaxAccess(_B)
if mibBuilder.loadTexts:msanShMCSensorNegativeGoingThrHysteresis.setStatus(_A)
class _MsanShMCSensorIdString_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_MsanShMCSensorIdString_Type.__name__=_D
_MsanShMCSensorIdString_Object=MibTableColumn
msanShMCSensorIdString=_MsanShMCSensorIdString_Object((1,3,6,1,4,1,1332,1,1,5,3,33,3,1,43),_MsanShMCSensorIdString_Type())
msanShMCSensorIdString.setMaxAccess(_B)
if mibBuilder.loadTexts:msanShMCSensorIdString.setStatus(_A)
class _MsanShMCSensorEntireSensorData_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_MsanShMCSensorEntireSensorData_Type.__name__=_K
_MsanShMCSensorEntireSensorData_Object=MibTableColumn
msanShMCSensorEntireSensorData=_MsanShMCSensorEntireSensorData_Object((1,3,6,1,4,1,1332,1,1,5,3,33,3,1,44),_MsanShMCSensorEntireSensorData_Type())
msanShMCSensorEntireSensorData.setMaxAccess(_B)
if mibBuilder.loadTexts:msanShMCSensorEntireSensorData.setStatus(_A)
_MsanShMCBoardsTable_Object=MibTable
msanShMCBoardsTable=_MsanShMCBoardsTable_Object((1,3,6,1,4,1,1332,1,1,5,3,33,4))
if mibBuilder.loadTexts:msanShMCBoardsTable.setStatus(_A)
_MsanShMCBoardsEntry_Object=MibTableRow
msanShMCBoardsEntry=_MsanShMCBoardsEntry_Object((1,3,6,1,4,1,1332,1,1,5,3,33,4,1))
msanShMCBoardsEntry.setIndexNames((0,_G,_S))
if mibBuilder.loadTexts:msanShMCBoardsEntry.setStatus(_A)
class _MsanShMCBoardsIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_MsanShMCBoardsIndex_Type.__name__=_C
_MsanShMCBoardsIndex_Object=MibTableColumn
msanShMCBoardsIndex=_MsanShMCBoardsIndex_Object((1,3,6,1,4,1,1332,1,1,5,3,33,4,1,1),_MsanShMCBoardsIndex_Type())
msanShMCBoardsIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:msanShMCBoardsIndex.setStatus(_A)
class _MsanShMCBoardsBoardBasicPresent_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_L,0),(_M,1)))
_MsanShMCBoardsBoardBasicPresent_Type.__name__=_C
_MsanShMCBoardsBoardBasicPresent_Object=MibTableColumn
msanShMCBoardsBoardBasicPresent=_MsanShMCBoardsBoardBasicPresent_Object((1,3,6,1,4,1,1332,1,1,5,3,33,4,1,2),_MsanShMCBoardsBoardBasicPresent_Type())
msanShMCBoardsBoardBasicPresent.setMaxAccess(_B)
if mibBuilder.loadTexts:msanShMCBoardsBoardBasicPresent.setStatus(_A)
class _MsanShMCBoardsBoardBasicHealthy_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_H,0),(_F,1)))
_MsanShMCBoardsBoardBasicHealthy_Type.__name__=_C
_MsanShMCBoardsBoardBasicHealthy_Object=MibTableColumn
msanShMCBoardsBoardBasicHealthy=_MsanShMCBoardsBoardBasicHealthy_Object((1,3,6,1,4,1,1332,1,1,5,3,33,4,1,3),_MsanShMCBoardsBoardBasicHealthy_Type())
msanShMCBoardsBoardBasicHealthy.setMaxAccess(_B)
if mibBuilder.loadTexts:msanShMCBoardsBoardBasicHealthy.setStatus(_A)
class _MsanShMCBoardsBoardBasicReset_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_N,0),(_O,1)))
_MsanShMCBoardsBoardBasicReset_Type.__name__=_C
_MsanShMCBoardsBoardBasicReset_Object=MibTableColumn
msanShMCBoardsBoardBasicReset=_MsanShMCBoardsBoardBasicReset_Object((1,3,6,1,4,1,1332,1,1,5,3,33,4,1,4),_MsanShMCBoardsBoardBasicReset_Type())
msanShMCBoardsBoardBasicReset.setMaxAccess(_E)
if mibBuilder.loadTexts:msanShMCBoardsBoardBasicReset.setStatus(_A)
class _MsanShMCBoardsBoardBasicSlaveAddress_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_MsanShMCBoardsBoardBasicSlaveAddress_Type.__name__=_C
_MsanShMCBoardsBoardBasicSlaveAddress_Object=MibTableColumn
msanShMCBoardsBoardBasicSlaveAddress=_MsanShMCBoardsBoardBasicSlaveAddress_Object((1,3,6,1,4,1,1332,1,1,5,3,33,4,1,5),_MsanShMCBoardsBoardBasicSlaveAddress_Type())
msanShMCBoardsBoardBasicSlaveAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:msanShMCBoardsBoardBasicSlaveAddress.setStatus(_A)
class _MsanShMCBoardsBoardBasicFruDeviceId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_MsanShMCBoardsBoardBasicFruDeviceId_Type.__name__=_C
_MsanShMCBoardsBoardBasicFruDeviceId_Object=MibTableColumn
msanShMCBoardsBoardBasicFruDeviceId=_MsanShMCBoardsBoardBasicFruDeviceId_Object((1,3,6,1,4,1,1332,1,1,5,3,33,4,1,7),_MsanShMCBoardsBoardBasicFruDeviceId_Type())
msanShMCBoardsBoardBasicFruDeviceId.setMaxAccess(_B)
if mibBuilder.loadTexts:msanShMCBoardsBoardBasicFruDeviceId.setStatus(_A)
_MsanShMCSelTable_Object=MibTable
msanShMCSelTable=_MsanShMCSelTable_Object((1,3,6,1,4,1,1332,1,1,5,3,33,5))
if mibBuilder.loadTexts:msanShMCSelTable.setStatus(_A)
_MsanShMCSelEntry_Object=MibTableRow
msanShMCSelEntry=_MsanShMCSelEntry_Object((1,3,6,1,4,1,1332,1,1,5,3,33,5,1))
msanShMCSelEntry.setIndexNames((0,_G,_T))
if mibBuilder.loadTexts:msanShMCSelEntry.setStatus(_A)
class _MsanShMCSelIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_MsanShMCSelIndex_Type.__name__=_C
_MsanShMCSelIndex_Object=MibTableColumn
msanShMCSelIndex=_MsanShMCSelIndex_Object((1,3,6,1,4,1,1332,1,1,5,3,33,5,1,1),_MsanShMCSelIndex_Type())
msanShMCSelIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:msanShMCSelIndex.setStatus(_A)
class _MsanShMCSelcontents_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_MsanShMCSelcontents_Type.__name__=_K
_MsanShMCSelcontents_Object=MibTableColumn
msanShMCSelcontents=_MsanShMCSelcontents_Object((1,3,6,1,4,1,1332,1,1,5,3,33,5,1,2),_MsanShMCSelcontents_Type())
msanShMCSelcontents.setMaxAccess(_B)
if mibBuilder.loadTexts:msanShMCSelcontents.setStatus(_A)
_MsanShMCShelfTable_Object=MibTable
msanShMCShelfTable=_MsanShMCShelfTable_Object((1,3,6,1,4,1,1332,1,1,5,3,33,6))
if mibBuilder.loadTexts:msanShMCShelfTable.setStatus(_A)
_MsanShMCShelfEntry_Object=MibTableRow
msanShMCShelfEntry=_MsanShMCShelfEntry_Object((1,3,6,1,4,1,1332,1,1,5,3,33,6,1))
msanShMCShelfEntry.setIndexNames((0,_G,_U))
if mibBuilder.loadTexts:msanShMCShelfEntry.setStatus(_A)
class _MsanShMCShelfIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_MsanShMCShelfIndex_Type.__name__=_C
_MsanShMCShelfIndex_Object=MibTableColumn
msanShMCShelfIndex=_MsanShMCShelfIndex_Object((1,3,6,1,4,1,1332,1,1,5,3,33,6,1,1),_MsanShMCShelfIndex_Type())
msanShMCShelfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:msanShMCShelfIndex.setStatus(_A)
class _MsanShMCShelfHealthy_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_MsanShMCShelfHealthy_Type.__name__=_C
_MsanShMCShelfHealthy_Object=MibTableColumn
msanShMCShelfHealthy=_MsanShMCShelfHealthy_Object((1,3,6,1,4,1,1332,1,1,5,3,33,6,1,2),_MsanShMCShelfHealthy_Type())
msanShMCShelfHealthy.setMaxAccess(_B)
if mibBuilder.loadTexts:msanShMCShelfHealthy.setStatus(_A)
_MsanShMCPefConfiguration_ObjectIdentity=ObjectIdentity
msanShMCPefConfiguration=_MsanShMCPefConfiguration_ObjectIdentity((1,3,6,1,4,1,1332,1,1,5,3,33,8))
class _MsanShMCPefConfigurationSetInProgress_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_H,0),(_F,1)))
_MsanShMCPefConfigurationSetInProgress_Type.__name__=_C
_MsanShMCPefConfigurationSetInProgress_Object=MibScalar
msanShMCPefConfigurationSetInProgress=_MsanShMCPefConfigurationSetInProgress_Object((1,3,6,1,4,1,1332,1,1,5,3,33,8,1),_MsanShMCPefConfigurationSetInProgress_Type())
msanShMCPefConfigurationSetInProgress.setMaxAccess(_B)
if mibBuilder.loadTexts:msanShMCPefConfigurationSetInProgress.setStatus(_A)
class _MsanShMCPefConfigurationControl_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_H,0),(_F,1)))
_MsanShMCPefConfigurationControl_Type.__name__=_C
_MsanShMCPefConfigurationControl_Object=MibScalar
msanShMCPefConfigurationControl=_MsanShMCPefConfigurationControl_Object((1,3,6,1,4,1,1332,1,1,5,3,33,8,2),_MsanShMCPefConfigurationControl_Type())
msanShMCPefConfigurationControl.setMaxAccess(_E)
if mibBuilder.loadTexts:msanShMCPefConfigurationControl.setStatus(_A)
class _MsanShMCPefConfigurationActionGlobalControl_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_H,0),(_F,1)))
_MsanShMCPefConfigurationActionGlobalControl_Type.__name__=_C
_MsanShMCPefConfigurationActionGlobalControl_Object=MibScalar
msanShMCPefConfigurationActionGlobalControl=_MsanShMCPefConfigurationActionGlobalControl_Object((1,3,6,1,4,1,1332,1,1,5,3,33,8,3),_MsanShMCPefConfigurationActionGlobalControl_Type())
msanShMCPefConfigurationActionGlobalControl.setMaxAccess(_E)
if mibBuilder.loadTexts:msanShMCPefConfigurationActionGlobalControl.setStatus(_A)
class _MsanShMCPefConfigurationStartupDelay_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_H,0),(_F,1)))
_MsanShMCPefConfigurationStartupDelay_Type.__name__=_C
_MsanShMCPefConfigurationStartupDelay_Object=MibScalar
msanShMCPefConfigurationStartupDelay=_MsanShMCPefConfigurationStartupDelay_Object((1,3,6,1,4,1,1332,1,1,5,3,33,8,4),_MsanShMCPefConfigurationStartupDelay_Type())
msanShMCPefConfigurationStartupDelay.setMaxAccess(_E)
if mibBuilder.loadTexts:msanShMCPefConfigurationStartupDelay.setStatus(_A)
class _MsanShMCPefConfigurationAlertStartupDelay_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_H,0),(_F,1)))
_MsanShMCPefConfigurationAlertStartupDelay_Type.__name__=_C
_MsanShMCPefConfigurationAlertStartupDelay_Object=MibScalar
msanShMCPefConfigurationAlertStartupDelay=_MsanShMCPefConfigurationAlertStartupDelay_Object((1,3,6,1,4,1,1332,1,1,5,3,33,8,5),_MsanShMCPefConfigurationAlertStartupDelay_Type())
msanShMCPefConfigurationAlertStartupDelay.setMaxAccess(_B)
if mibBuilder.loadTexts:msanShMCPefConfigurationAlertStartupDelay.setStatus(_A)
class _MsanShMCPefConfigurationNumberOfEventFilters_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_H,0),(_F,1)))
_MsanShMCPefConfigurationNumberOfEventFilters_Type.__name__=_C
_MsanShMCPefConfigurationNumberOfEventFilters_Object=MibScalar
msanShMCPefConfigurationNumberOfEventFilters=_MsanShMCPefConfigurationNumberOfEventFilters_Object((1,3,6,1,4,1,1332,1,1,5,3,33,8,6),_MsanShMCPefConfigurationNumberOfEventFilters_Type())
msanShMCPefConfigurationNumberOfEventFilters.setMaxAccess(_B)
if mibBuilder.loadTexts:msanShMCPefConfigurationNumberOfEventFilters.setStatus(_A)
class _MsanShMCPefConfigurationNumberOfAlertPoliciEntries_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_H,0),(_F,1)))
_MsanShMCPefConfigurationNumberOfAlertPoliciEntries_Type.__name__=_C
_MsanShMCPefConfigurationNumberOfAlertPoliciEntries_Object=MibScalar
msanShMCPefConfigurationNumberOfAlertPoliciEntries=_MsanShMCPefConfigurationNumberOfAlertPoliciEntries_Object((1,3,6,1,4,1,1332,1,1,5,3,33,8,7),_MsanShMCPefConfigurationNumberOfAlertPoliciEntries_Type())
msanShMCPefConfigurationNumberOfAlertPoliciEntries.setMaxAccess(_B)
if mibBuilder.loadTexts:msanShMCPefConfigurationNumberOfAlertPoliciEntries.setStatus(_A)
class _MsanShMCPefConfigurationSystemGuid_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_H,0),(_F,1)))
_MsanShMCPefConfigurationSystemGuid_Type.__name__=_C
_MsanShMCPefConfigurationSystemGuid_Object=MibScalar
msanShMCPefConfigurationSystemGuid=_MsanShMCPefConfigurationSystemGuid_Object((1,3,6,1,4,1,1332,1,1,5,3,33,8,8),_MsanShMCPefConfigurationSystemGuid_Type())
msanShMCPefConfigurationSystemGuid.setMaxAccess(_E)
if mibBuilder.loadTexts:msanShMCPefConfigurationSystemGuid.setStatus(_A)
class _MsanShMCPefConfigurationNumberOfAlertStrings_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_H,0),(_F,1)))
_MsanShMCPefConfigurationNumberOfAlertStrings_Type.__name__=_C
_MsanShMCPefConfigurationNumberOfAlertStrings_Object=MibScalar
msanShMCPefConfigurationNumberOfAlertStrings=_MsanShMCPefConfigurationNumberOfAlertStrings_Object((1,3,6,1,4,1,1332,1,1,5,3,33,8,9),_MsanShMCPefConfigurationNumberOfAlertStrings_Type())
msanShMCPefConfigurationNumberOfAlertStrings.setMaxAccess(_B)
if mibBuilder.loadTexts:msanShMCPefConfigurationNumberOfAlertStrings.setStatus(_A)
_MsanShMCPefConfigurationEventFilterTable_Object=MibTable
msanShMCPefConfigurationEventFilterTable=_MsanShMCPefConfigurationEventFilterTable_Object((1,3,6,1,4,1,1332,1,1,5,3,33,14))
if mibBuilder.loadTexts:msanShMCPefConfigurationEventFilterTable.setStatus(_A)
_MsanShMCPefConfigurationEventFilterEntry_Object=MibTableRow
msanShMCPefConfigurationEventFilterEntry=_MsanShMCPefConfigurationEventFilterEntry_Object((1,3,6,1,4,1,1332,1,1,5,3,33,14,1))
msanShMCPefConfigurationEventFilterEntry.setIndexNames((0,_G,_V))
if mibBuilder.loadTexts:msanShMCPefConfigurationEventFilterEntry.setStatus(_A)
class _MsanShMCPefConfigurationEventFilterIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_MsanShMCPefConfigurationEventFilterIndex_Type.__name__=_C
_MsanShMCPefConfigurationEventFilterIndex_Object=MibTableColumn
msanShMCPefConfigurationEventFilterIndex=_MsanShMCPefConfigurationEventFilterIndex_Object((1,3,6,1,4,1,1332,1,1,5,3,33,14,1,1),_MsanShMCPefConfigurationEventFilterIndex_Type())
msanShMCPefConfigurationEventFilterIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:msanShMCPefConfigurationEventFilterIndex.setStatus(_A)
class _MsanShMCPefConfigurationEventFilterData_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(20,20));fixedLength=20
_MsanShMCPefConfigurationEventFilterData_Type.__name__=_K
_MsanShMCPefConfigurationEventFilterData_Object=MibTableColumn
msanShMCPefConfigurationEventFilterData=_MsanShMCPefConfigurationEventFilterData_Object((1,3,6,1,4,1,1332,1,1,5,3,33,14,1,2),_MsanShMCPefConfigurationEventFilterData_Type())
msanShMCPefConfigurationEventFilterData.setMaxAccess(_E)
if mibBuilder.loadTexts:msanShMCPefConfigurationEventFilterData.setStatus(_A)
_MsanShMCPefConfigurationAlertStringTable_Object=MibTable
msanShMCPefConfigurationAlertStringTable=_MsanShMCPefConfigurationAlertStringTable_Object((1,3,6,1,4,1,1332,1,1,5,3,33,19))
if mibBuilder.loadTexts:msanShMCPefConfigurationAlertStringTable.setStatus(_A)
_MsanShMCPefConfigurationAlertStringEntry_Object=MibTableRow
msanShMCPefConfigurationAlertStringEntry=_MsanShMCPefConfigurationAlertStringEntry_Object((1,3,6,1,4,1,1332,1,1,5,3,33,19,1))
msanShMCPefConfigurationAlertStringEntry.setIndexNames((0,_G,_W))
if mibBuilder.loadTexts:msanShMCPefConfigurationAlertStringEntry.setStatus(_A)
class _MsanShMCPefConfigurationAlertStringIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_MsanShMCPefConfigurationAlertStringIndex_Type.__name__=_C
_MsanShMCPefConfigurationAlertStringIndex_Object=MibTableColumn
msanShMCPefConfigurationAlertStringIndex=_MsanShMCPefConfigurationAlertStringIndex_Object((1,3,6,1,4,1,1332,1,1,5,3,33,19,1,1),_MsanShMCPefConfigurationAlertStringIndex_Type())
msanShMCPefConfigurationAlertStringIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:msanShMCPefConfigurationAlertStringIndex.setStatus(_A)
class _MsanShMCPefConfigurationAlertStringKey_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(2,2));fixedLength=2
_MsanShMCPefConfigurationAlertStringKey_Type.__name__=_K
_MsanShMCPefConfigurationAlertStringKey_Object=MibTableColumn
msanShMCPefConfigurationAlertStringKey=_MsanShMCPefConfigurationAlertStringKey_Object((1,3,6,1,4,1,1332,1,1,5,3,33,19,1,2),_MsanShMCPefConfigurationAlertStringKey_Type())
msanShMCPefConfigurationAlertStringKey.setMaxAccess(_B)
if mibBuilder.loadTexts:msanShMCPefConfigurationAlertStringKey.setStatus(_A)
class _MsanShMCPefConfigurationAlertString_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(255,255));fixedLength=255
_MsanShMCPefConfigurationAlertString_Type.__name__=_D
_MsanShMCPefConfigurationAlertString_Object=MibTableColumn
msanShMCPefConfigurationAlertString=_MsanShMCPefConfigurationAlertString_Object((1,3,6,1,4,1,1332,1,1,5,3,33,19,1,3),_MsanShMCPefConfigurationAlertString_Type())
msanShMCPefConfigurationAlertString.setMaxAccess(_B)
if mibBuilder.loadTexts:msanShMCPefConfigurationAlertString.setStatus(_A)
_MsanShMCFruInfoTable_Object=MibTable
msanShMCFruInfoTable=_MsanShMCFruInfoTable_Object((1,3,6,1,4,1,1332,1,1,5,3,33,20))
if mibBuilder.loadTexts:msanShMCFruInfoTable.setStatus(_A)
_MsanShMCFruInfoEntry_Object=MibTableRow
msanShMCFruInfoEntry=_MsanShMCFruInfoEntry_Object((1,3,6,1,4,1,1332,1,1,5,3,33,20,1))
msanShMCFruInfoEntry.setIndexNames((0,_G,_X))
if mibBuilder.loadTexts:msanShMCFruInfoEntry.setStatus(_A)
class _MsanShMCFruInfoIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_MsanShMCFruInfoIndex_Type.__name__=_C
_MsanShMCFruInfoIndex_Object=MibTableColumn
msanShMCFruInfoIndex=_MsanShMCFruInfoIndex_Object((1,3,6,1,4,1,1332,1,1,5,3,33,20,1,1),_MsanShMCFruInfoIndex_Type())
msanShMCFruInfoIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:msanShMCFruInfoIndex.setStatus(_A)
class _MsanShMCFruInfoData_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_MsanShMCFruInfoData_Type.__name__=_K
_MsanShMCFruInfoData_Object=MibTableColumn
msanShMCFruInfoData=_MsanShMCFruInfoData_Object((1,3,6,1,4,1,1332,1,1,5,3,33,20,1,2),_MsanShMCFruInfoData_Type())
msanShMCFruInfoData.setMaxAccess(_B)
if mibBuilder.loadTexts:msanShMCFruInfoData.setStatus(_A)
class _MsanShMCFruInfoDataWo_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_MsanShMCFruInfoDataWo_Type.__name__=_K
_MsanShMCFruInfoDataWo_Object=MibTableColumn
msanShMCFruInfoDataWo=_MsanShMCFruInfoDataWo_Object((1,3,6,1,4,1,1332,1,1,5,3,33,20,1,3),_MsanShMCFruInfoDataWo_Type())
msanShMCFruInfoDataWo.setMaxAccess(_E)
if mibBuilder.loadTexts:msanShMCFruInfoDataWo.setStatus(_A)
_MsanShMCBoardVariablesTable_Object=MibTable
msanShMCBoardVariablesTable=_MsanShMCBoardVariablesTable_Object((1,3,6,1,4,1,1332,1,1,5,3,33,32))
if mibBuilder.loadTexts:msanShMCBoardVariablesTable.setStatus(_A)
_MsanShMCBoardVariablesEntry_Object=MibTableRow
msanShMCBoardVariablesEntry=_MsanShMCBoardVariablesEntry_Object((1,3,6,1,4,1,1332,1,1,5,3,33,32,1))
msanShMCBoardVariablesEntry.setIndexNames((0,_G,_Y))
if mibBuilder.loadTexts:msanShMCBoardVariablesEntry.setStatus(_A)
class _MsanShMCBoardVariablesBoardBasicSlotNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_MsanShMCBoardVariablesBoardBasicSlotNumber_Type.__name__=_C
_MsanShMCBoardVariablesBoardBasicSlotNumber_Object=MibTableColumn
msanShMCBoardVariablesBoardBasicSlotNumber=_MsanShMCBoardVariablesBoardBasicSlotNumber_Object((1,3,6,1,4,1,1332,1,1,5,3,33,32,1,1),_MsanShMCBoardVariablesBoardBasicSlotNumber_Type())
msanShMCBoardVariablesBoardBasicSlotNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:msanShMCBoardVariablesBoardBasicSlotNumber.setStatus(_A)
class _MsanShMCBoardVariablesBoardBasicPresent_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_L,0),(_M,1)))
_MsanShMCBoardVariablesBoardBasicPresent_Type.__name__=_C
_MsanShMCBoardVariablesBoardBasicPresent_Object=MibTableColumn
msanShMCBoardVariablesBoardBasicPresent=_MsanShMCBoardVariablesBoardBasicPresent_Object((1,3,6,1,4,1,1332,1,1,5,3,33,32,1,2),_MsanShMCBoardVariablesBoardBasicPresent_Type())
msanShMCBoardVariablesBoardBasicPresent.setMaxAccess(_B)
if mibBuilder.loadTexts:msanShMCBoardVariablesBoardBasicPresent.setStatus(_A)
class _MsanShMCBoardVariablesBoardBasicHealthy_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_H,0),(_F,1)))
_MsanShMCBoardVariablesBoardBasicHealthy_Type.__name__=_C
_MsanShMCBoardVariablesBoardBasicHealthy_Object=MibTableColumn
msanShMCBoardVariablesBoardBasicHealthy=_MsanShMCBoardVariablesBoardBasicHealthy_Object((1,3,6,1,4,1,1332,1,1,5,3,33,32,1,3),_MsanShMCBoardVariablesBoardBasicHealthy_Type())
msanShMCBoardVariablesBoardBasicHealthy.setMaxAccess(_B)
if mibBuilder.loadTexts:msanShMCBoardVariablesBoardBasicHealthy.setStatus(_A)
class _MsanShMCBoardVariablesBoardBasicReset_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_N,0),(_O,1)))
_MsanShMCBoardVariablesBoardBasicReset_Type.__name__=_C
_MsanShMCBoardVariablesBoardBasicReset_Object=MibTableColumn
msanShMCBoardVariablesBoardBasicReset=_MsanShMCBoardVariablesBoardBasicReset_Object((1,3,6,1,4,1,1332,1,1,5,3,33,32,1,4),_MsanShMCBoardVariablesBoardBasicReset_Type())
msanShMCBoardVariablesBoardBasicReset.setMaxAccess(_E)
if mibBuilder.loadTexts:msanShMCBoardVariablesBoardBasicReset.setStatus(_A)
class _MsanShMCBoardVariablesBoardBasicPowered_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_N,0),('powered',1)))
_MsanShMCBoardVariablesBoardBasicPowered_Type.__name__=_C
_MsanShMCBoardVariablesBoardBasicPowered_Object=MibTableColumn
msanShMCBoardVariablesBoardBasicPowered=_MsanShMCBoardVariablesBoardBasicPowered_Object((1,3,6,1,4,1,1332,1,1,5,3,33,32,1,5),_MsanShMCBoardVariablesBoardBasicPowered_Type())
msanShMCBoardVariablesBoardBasicPowered.setMaxAccess(_B)
if mibBuilder.loadTexts:msanShMCBoardVariablesBoardBasicPowered.setStatus(_A)
class _MsanShMCBoardVariablesBoardBasicSlaveAddress_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_MsanShMCBoardVariablesBoardBasicSlaveAddress_Type.__name__=_C
_MsanShMCBoardVariablesBoardBasicSlaveAddress_Object=MibTableColumn
msanShMCBoardVariablesBoardBasicSlaveAddress=_MsanShMCBoardVariablesBoardBasicSlaveAddress_Object((1,3,6,1,4,1,1332,1,1,5,3,33,32,1,6),_MsanShMCBoardVariablesBoardBasicSlaveAddress_Type())
msanShMCBoardVariablesBoardBasicSlaveAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:msanShMCBoardVariablesBoardBasicSlaveAddress.setStatus(_A)
class _MsanShMCBoardVariablesBoardBasicFruDeviceId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_MsanShMCBoardVariablesBoardBasicFruDeviceId_Type.__name__=_C
_MsanShMCBoardVariablesBoardBasicFruDeviceId_Object=MibTableColumn
msanShMCBoardVariablesBoardBasicFruDeviceId=_MsanShMCBoardVariablesBoardBasicFruDeviceId_Object((1,3,6,1,4,1,1332,1,1,5,3,33,32,1,7),_MsanShMCBoardVariablesBoardBasicFruDeviceId_Type())
msanShMCBoardVariablesBoardBasicFruDeviceId.setMaxAccess(_B)
if mibBuilder.loadTexts:msanShMCBoardVariablesBoardBasicFruDeviceId.setStatus(_A)
class _MsanShMCBoardVariablesBoardBasicFruinfoProductAreaPresent_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_I,0),(_J,1)))
_MsanShMCBoardVariablesBoardBasicFruinfoProductAreaPresent_Type.__name__=_C
_MsanShMCBoardVariablesBoardBasicFruinfoProductAreaPresent_Object=MibTableColumn
msanShMCBoardVariablesBoardBasicFruinfoProductAreaPresent=_MsanShMCBoardVariablesBoardBasicFruinfoProductAreaPresent_Object((1,3,6,1,4,1,1332,1,1,5,3,33,32,1,8),_MsanShMCBoardVariablesBoardBasicFruinfoProductAreaPresent_Type())
msanShMCBoardVariablesBoardBasicFruinfoProductAreaPresent.setMaxAccess(_B)
if mibBuilder.loadTexts:msanShMCBoardVariablesBoardBasicFruinfoProductAreaPresent.setStatus(_A)
class _MsanShMCBoardVariablesBoardBasicProductManufacturer_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_MsanShMCBoardVariablesBoardBasicProductManufacturer_Type.__name__=_D
_MsanShMCBoardVariablesBoardBasicProductManufacturer_Object=MibTableColumn
msanShMCBoardVariablesBoardBasicProductManufacturer=_MsanShMCBoardVariablesBoardBasicProductManufacturer_Object((1,3,6,1,4,1,1332,1,1,5,3,33,32,1,9),_MsanShMCBoardVariablesBoardBasicProductManufacturer_Type())
msanShMCBoardVariablesBoardBasicProductManufacturer.setMaxAccess(_B)
if mibBuilder.loadTexts:msanShMCBoardVariablesBoardBasicProductManufacturer.setStatus(_A)
class _MsanShMCBoardVariablesBoardBasicProductName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_MsanShMCBoardVariablesBoardBasicProductName_Type.__name__=_D
_MsanShMCBoardVariablesBoardBasicProductName_Object=MibTableColumn
msanShMCBoardVariablesBoardBasicProductName=_MsanShMCBoardVariablesBoardBasicProductName_Object((1,3,6,1,4,1,1332,1,1,5,3,33,32,1,10),_MsanShMCBoardVariablesBoardBasicProductName_Type())
msanShMCBoardVariablesBoardBasicProductName.setMaxAccess(_B)
if mibBuilder.loadTexts:msanShMCBoardVariablesBoardBasicProductName.setStatus(_A)
class _MsanShMCBoardVariablesBoardBasicProductPartModelNumber_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_MsanShMCBoardVariablesBoardBasicProductPartModelNumber_Type.__name__=_D
_MsanShMCBoardVariablesBoardBasicProductPartModelNumber_Object=MibTableColumn
msanShMCBoardVariablesBoardBasicProductPartModelNumber=_MsanShMCBoardVariablesBoardBasicProductPartModelNumber_Object((1,3,6,1,4,1,1332,1,1,5,3,33,32,1,11),_MsanShMCBoardVariablesBoardBasicProductPartModelNumber_Type())
msanShMCBoardVariablesBoardBasicProductPartModelNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:msanShMCBoardVariablesBoardBasicProductPartModelNumber.setStatus(_A)
class _MsanShMCBoardVariablesBoardBasicProductVersionNumber_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_MsanShMCBoardVariablesBoardBasicProductVersionNumber_Type.__name__=_D
_MsanShMCBoardVariablesBoardBasicProductVersionNumber_Object=MibTableColumn
msanShMCBoardVariablesBoardBasicProductVersionNumber=_MsanShMCBoardVariablesBoardBasicProductVersionNumber_Object((1,3,6,1,4,1,1332,1,1,5,3,33,32,1,12),_MsanShMCBoardVariablesBoardBasicProductVersionNumber_Type())
msanShMCBoardVariablesBoardBasicProductVersionNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:msanShMCBoardVariablesBoardBasicProductVersionNumber.setStatus(_A)
class _MsanShMCBoardVariablesBoardBasicProductSerialNumber_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_MsanShMCBoardVariablesBoardBasicProductSerialNumber_Type.__name__=_D
_MsanShMCBoardVariablesBoardBasicProductSerialNumber_Object=MibTableColumn
msanShMCBoardVariablesBoardBasicProductSerialNumber=_MsanShMCBoardVariablesBoardBasicProductSerialNumber_Object((1,3,6,1,4,1,1332,1,1,5,3,33,32,1,13),_MsanShMCBoardVariablesBoardBasicProductSerialNumber_Type())
msanShMCBoardVariablesBoardBasicProductSerialNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:msanShMCBoardVariablesBoardBasicProductSerialNumber.setStatus(_A)
class _MsanShMCBoardVariablesBoardBasicBoardAreaPresent_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_I,0),(_J,1)))
_MsanShMCBoardVariablesBoardBasicBoardAreaPresent_Type.__name__=_C
_MsanShMCBoardVariablesBoardBasicBoardAreaPresent_Object=MibTableColumn
msanShMCBoardVariablesBoardBasicBoardAreaPresent=_MsanShMCBoardVariablesBoardBasicBoardAreaPresent_Object((1,3,6,1,4,1,1332,1,1,5,3,33,32,1,14),_MsanShMCBoardVariablesBoardBasicBoardAreaPresent_Type())
msanShMCBoardVariablesBoardBasicBoardAreaPresent.setMaxAccess(_B)
if mibBuilder.loadTexts:msanShMCBoardVariablesBoardBasicBoardAreaPresent.setStatus(_A)
class _MsanShMCBoardVariablesBoardBasicBoardManufacturer_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_MsanShMCBoardVariablesBoardBasicBoardManufacturer_Type.__name__=_D
_MsanShMCBoardVariablesBoardBasicBoardManufacturer_Object=MibTableColumn
msanShMCBoardVariablesBoardBasicBoardManufacturer=_MsanShMCBoardVariablesBoardBasicBoardManufacturer_Object((1,3,6,1,4,1,1332,1,1,5,3,33,32,1,15),_MsanShMCBoardVariablesBoardBasicBoardManufacturer_Type())
msanShMCBoardVariablesBoardBasicBoardManufacturer.setMaxAccess(_B)
if mibBuilder.loadTexts:msanShMCBoardVariablesBoardBasicBoardManufacturer.setStatus(_A)
class _MsanShMCBoardVariablesBoardBasicBoardProductName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_MsanShMCBoardVariablesBoardBasicBoardProductName_Type.__name__=_D
_MsanShMCBoardVariablesBoardBasicBoardProductName_Object=MibTableColumn
msanShMCBoardVariablesBoardBasicBoardProductName=_MsanShMCBoardVariablesBoardBasicBoardProductName_Object((1,3,6,1,4,1,1332,1,1,5,3,33,32,1,16),_MsanShMCBoardVariablesBoardBasicBoardProductName_Type())
msanShMCBoardVariablesBoardBasicBoardProductName.setMaxAccess(_B)
if mibBuilder.loadTexts:msanShMCBoardVariablesBoardBasicBoardProductName.setStatus(_A)
class _MsanShMCBoardVariablesBoardBasicBoardSerialNumber_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_MsanShMCBoardVariablesBoardBasicBoardSerialNumber_Type.__name__=_D
_MsanShMCBoardVariablesBoardBasicBoardSerialNumber_Object=MibTableColumn
msanShMCBoardVariablesBoardBasicBoardSerialNumber=_MsanShMCBoardVariablesBoardBasicBoardSerialNumber_Object((1,3,6,1,4,1,1332,1,1,5,3,33,32,1,17),_MsanShMCBoardVariablesBoardBasicBoardSerialNumber_Type())
msanShMCBoardVariablesBoardBasicBoardSerialNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:msanShMCBoardVariablesBoardBasicBoardSerialNumber.setStatus(_A)
class _MsanShMCBoardVariablesBoardBasicBoardPartNumber_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_MsanShMCBoardVariablesBoardBasicBoardPartNumber_Type.__name__=_D
_MsanShMCBoardVariablesBoardBasicBoardPartNumber_Object=MibTableColumn
msanShMCBoardVariablesBoardBasicBoardPartNumber=_MsanShMCBoardVariablesBoardBasicBoardPartNumber_Object((1,3,6,1,4,1,1332,1,1,5,3,33,32,1,18),_MsanShMCBoardVariablesBoardBasicBoardPartNumber_Type())
msanShMCBoardVariablesBoardBasicBoardPartNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:msanShMCBoardVariablesBoardBasicBoardPartNumber.setStatus(_A)
class _MsanShMCBoardVariablesBoardBasicBoardManufactureTime_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_MsanShMCBoardVariablesBoardBasicBoardManufactureTime_Type.__name__=_C
_MsanShMCBoardVariablesBoardBasicBoardManufactureTime_Object=MibTableColumn
msanShMCBoardVariablesBoardBasicBoardManufactureTime=_MsanShMCBoardVariablesBoardBasicBoardManufactureTime_Object((1,3,6,1,4,1,1332,1,1,5,3,33,32,1,19),_MsanShMCBoardVariablesBoardBasicBoardManufactureTime_Type())
msanShMCBoardVariablesBoardBasicBoardManufactureTime.setMaxAccess(_B)
if mibBuilder.loadTexts:msanShMCBoardVariablesBoardBasicBoardManufactureTime.setStatus(_A)
class _MsanShMCBoardVariablesSelectivePowerOffSwitchOffType_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('automatic',1),('switchOff',2),('switchOn',3)))
_MsanShMCBoardVariablesSelectivePowerOffSwitchOffType_Type.__name__=_C
_MsanShMCBoardVariablesSelectivePowerOffSwitchOffType_Object=MibTableColumn
msanShMCBoardVariablesSelectivePowerOffSwitchOffType=_MsanShMCBoardVariablesSelectivePowerOffSwitchOffType_Object((1,3,6,1,4,1,1332,1,1,5,3,33,32,1,20),_MsanShMCBoardVariablesSelectivePowerOffSwitchOffType_Type())
msanShMCBoardVariablesSelectivePowerOffSwitchOffType.setMaxAccess(_E)
if mibBuilder.loadTexts:msanShMCBoardVariablesSelectivePowerOffSwitchOffType.setStatus(_A)
_MsanShMCFanTrayVariablesTable_Object=MibTable
msanShMCFanTrayVariablesTable=_MsanShMCFanTrayVariablesTable_Object((1,3,6,1,4,1,1332,1,1,5,3,33,33))
if mibBuilder.loadTexts:msanShMCFanTrayVariablesTable.setStatus(_A)
_MsanShMCFanTrayVariablesEntry_Object=MibTableRow
msanShMCFanTrayVariablesEntry=_MsanShMCFanTrayVariablesEntry_Object((1,3,6,1,4,1,1332,1,1,5,3,33,33,1))
msanShMCFanTrayVariablesEntry.setIndexNames((0,_G,_Z))
if mibBuilder.loadTexts:msanShMCFanTrayVariablesEntry.setStatus(_A)
class _MsanShMCFanTraySlotNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_MsanShMCFanTraySlotNumber_Type.__name__=_C
_MsanShMCFanTraySlotNumber_Object=MibTableColumn
msanShMCFanTraySlotNumber=_MsanShMCFanTraySlotNumber_Object((1,3,6,1,4,1,1332,1,1,5,3,33,33,1,1),_MsanShMCFanTraySlotNumber_Type())
msanShMCFanTraySlotNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:msanShMCFanTraySlotNumber.setStatus(_A)
class _MsanShMCFanTrayPresent_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_L,0),(_M,1)))
_MsanShMCFanTrayPresent_Type.__name__=_C
_MsanShMCFanTrayPresent_Object=MibTableColumn
msanShMCFanTrayPresent=_MsanShMCFanTrayPresent_Object((1,3,6,1,4,1,1332,1,1,5,3,33,33,1,2),_MsanShMCFanTrayPresent_Type())
msanShMCFanTrayPresent.setMaxAccess(_B)
if mibBuilder.loadTexts:msanShMCFanTrayPresent.setStatus(_A)
class _MsanShMCFanTrayHealthy_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_H,0),(_F,1)))
_MsanShMCFanTrayHealthy_Type.__name__=_C
_MsanShMCFanTrayHealthy_Object=MibTableColumn
msanShMCFanTrayHealthy=_MsanShMCFanTrayHealthy_Object((1,3,6,1,4,1,1332,1,1,5,3,33,33,1,3),_MsanShMCFanTrayHealthy_Type())
msanShMCFanTrayHealthy.setMaxAccess(_B)
if mibBuilder.loadTexts:msanShMCFanTrayHealthy.setStatus(_A)
class _MsanShMCFanTrayHealthLed_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_H,0),(_F,1)))
_MsanShMCFanTrayHealthLed_Type.__name__=_C
_MsanShMCFanTrayHealthLed_Object=MibTableColumn
msanShMCFanTrayHealthLed=_MsanShMCFanTrayHealthLed_Object((1,3,6,1,4,1,1332,1,1,5,3,33,33,1,4),_MsanShMCFanTrayHealthLed_Type())
msanShMCFanTrayHealthLed.setMaxAccess(_E)
if mibBuilder.loadTexts:msanShMCFanTrayHealthLed.setStatus(_A)
class _MsanShMCFanTraySlaveAddress_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_MsanShMCFanTraySlaveAddress_Type.__name__=_C
_MsanShMCFanTraySlaveAddress_Object=MibTableColumn
msanShMCFanTraySlaveAddress=_MsanShMCFanTraySlaveAddress_Object((1,3,6,1,4,1,1332,1,1,5,3,33,33,1,5),_MsanShMCFanTraySlaveAddress_Type())
msanShMCFanTraySlaveAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:msanShMCFanTraySlaveAddress.setStatus(_A)
class _MsanShMCFanTrayFruDeviceId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_MsanShMCFanTrayFruDeviceId_Type.__name__=_C
_MsanShMCFanTrayFruDeviceId_Object=MibTableColumn
msanShMCFanTrayFruDeviceId=_MsanShMCFanTrayFruDeviceId_Object((1,3,6,1,4,1,1332,1,1,5,3,33,33,1,6),_MsanShMCFanTrayFruDeviceId_Type())
msanShMCFanTrayFruDeviceId.setMaxAccess(_B)
if mibBuilder.loadTexts:msanShMCFanTrayFruDeviceId.setStatus(_A)
class _MsanShMCFanTrayFruinfoProductAreaPresent_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_I,0),(_J,1)))
_MsanShMCFanTrayFruinfoProductAreaPresent_Type.__name__=_C
_MsanShMCFanTrayFruinfoProductAreaPresent_Object=MibTableColumn
msanShMCFanTrayFruinfoProductAreaPresent=_MsanShMCFanTrayFruinfoProductAreaPresent_Object((1,3,6,1,4,1,1332,1,1,5,3,33,33,1,7),_MsanShMCFanTrayFruinfoProductAreaPresent_Type())
msanShMCFanTrayFruinfoProductAreaPresent.setMaxAccess(_B)
if mibBuilder.loadTexts:msanShMCFanTrayFruinfoProductAreaPresent.setStatus(_A)
class _MsanShMCFanTrayFruinfoProductManufacturer_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_MsanShMCFanTrayFruinfoProductManufacturer_Type.__name__=_D
_MsanShMCFanTrayFruinfoProductManufacturer_Object=MibTableColumn
msanShMCFanTrayFruinfoProductManufacturer=_MsanShMCFanTrayFruinfoProductManufacturer_Object((1,3,6,1,4,1,1332,1,1,5,3,33,33,1,8),_MsanShMCFanTrayFruinfoProductManufacturer_Type())
msanShMCFanTrayFruinfoProductManufacturer.setMaxAccess(_B)
if mibBuilder.loadTexts:msanShMCFanTrayFruinfoProductManufacturer.setStatus(_A)
class _MsanShMCFanTrayFruinfoProductName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_MsanShMCFanTrayFruinfoProductName_Type.__name__=_D
_MsanShMCFanTrayFruinfoProductName_Object=MibTableColumn
msanShMCFanTrayFruinfoProductName=_MsanShMCFanTrayFruinfoProductName_Object((1,3,6,1,4,1,1332,1,1,5,3,33,33,1,9),_MsanShMCFanTrayFruinfoProductName_Type())
msanShMCFanTrayFruinfoProductName.setMaxAccess(_B)
if mibBuilder.loadTexts:msanShMCFanTrayFruinfoProductName.setStatus(_A)
class _MsanShMCFanTrayFruinfoProductPartModelNumber_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_MsanShMCFanTrayFruinfoProductPartModelNumber_Type.__name__=_D
_MsanShMCFanTrayFruinfoProductPartModelNumber_Object=MibTableColumn
msanShMCFanTrayFruinfoProductPartModelNumber=_MsanShMCFanTrayFruinfoProductPartModelNumber_Object((1,3,6,1,4,1,1332,1,1,5,3,33,33,1,10),_MsanShMCFanTrayFruinfoProductPartModelNumber_Type())
msanShMCFanTrayFruinfoProductPartModelNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:msanShMCFanTrayFruinfoProductPartModelNumber.setStatus(_A)
class _MsanShMCFanTrayFruinfoProductVersionNumber_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_MsanShMCFanTrayFruinfoProductVersionNumber_Type.__name__=_D
_MsanShMCFanTrayFruinfoProductVersionNumber_Object=MibTableColumn
msanShMCFanTrayFruinfoProductVersionNumber=_MsanShMCFanTrayFruinfoProductVersionNumber_Object((1,3,6,1,4,1,1332,1,1,5,3,33,33,1,11),_MsanShMCFanTrayFruinfoProductVersionNumber_Type())
msanShMCFanTrayFruinfoProductVersionNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:msanShMCFanTrayFruinfoProductVersionNumber.setStatus(_A)
class _MsanShMCFanTrayFruinfoProductSerialNumber_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_MsanShMCFanTrayFruinfoProductSerialNumber_Type.__name__=_D
_MsanShMCFanTrayFruinfoProductSerialNumber_Object=MibTableColumn
msanShMCFanTrayFruinfoProductSerialNumber=_MsanShMCFanTrayFruinfoProductSerialNumber_Object((1,3,6,1,4,1,1332,1,1,5,3,33,33,1,12),_MsanShMCFanTrayFruinfoProductSerialNumber_Type())
msanShMCFanTrayFruinfoProductSerialNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:msanShMCFanTrayFruinfoProductSerialNumber.setStatus(_A)
class _MsanShMCFanTrayFruinfoBoardAreaPresent_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_I,0),(_J,1)))
_MsanShMCFanTrayFruinfoBoardAreaPresent_Type.__name__=_C
_MsanShMCFanTrayFruinfoBoardAreaPresent_Object=MibTableColumn
msanShMCFanTrayFruinfoBoardAreaPresent=_MsanShMCFanTrayFruinfoBoardAreaPresent_Object((1,3,6,1,4,1,1332,1,1,5,3,33,33,1,13),_MsanShMCFanTrayFruinfoBoardAreaPresent_Type())
msanShMCFanTrayFruinfoBoardAreaPresent.setMaxAccess(_B)
if mibBuilder.loadTexts:msanShMCFanTrayFruinfoBoardAreaPresent.setStatus(_A)
class _MsanShMCFanTrayFruinfoBoardManufacturer_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_MsanShMCFanTrayFruinfoBoardManufacturer_Type.__name__=_D
_MsanShMCFanTrayFruinfoBoardManufacturer_Object=MibTableColumn
msanShMCFanTrayFruinfoBoardManufacturer=_MsanShMCFanTrayFruinfoBoardManufacturer_Object((1,3,6,1,4,1,1332,1,1,5,3,33,33,1,14),_MsanShMCFanTrayFruinfoBoardManufacturer_Type())
msanShMCFanTrayFruinfoBoardManufacturer.setMaxAccess(_B)
if mibBuilder.loadTexts:msanShMCFanTrayFruinfoBoardManufacturer.setStatus(_A)
class _MsanShMCFanTrayFruinfoBoardProductName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_MsanShMCFanTrayFruinfoBoardProductName_Type.__name__=_D
_MsanShMCFanTrayFruinfoBoardProductName_Object=MibTableColumn
msanShMCFanTrayFruinfoBoardProductName=_MsanShMCFanTrayFruinfoBoardProductName_Object((1,3,6,1,4,1,1332,1,1,5,3,33,33,1,15),_MsanShMCFanTrayFruinfoBoardProductName_Type())
msanShMCFanTrayFruinfoBoardProductName.setMaxAccess(_B)
if mibBuilder.loadTexts:msanShMCFanTrayFruinfoBoardProductName.setStatus(_A)
class _MsanShMCFanTrayFruinfoBoardSerialNumber_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_MsanShMCFanTrayFruinfoBoardSerialNumber_Type.__name__=_D
_MsanShMCFanTrayFruinfoBoardSerialNumber_Object=MibTableColumn
msanShMCFanTrayFruinfoBoardSerialNumber=_MsanShMCFanTrayFruinfoBoardSerialNumber_Object((1,3,6,1,4,1,1332,1,1,5,3,33,33,1,16),_MsanShMCFanTrayFruinfoBoardSerialNumber_Type())
msanShMCFanTrayFruinfoBoardSerialNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:msanShMCFanTrayFruinfoBoardSerialNumber.setStatus(_A)
class _MsanShMCFanTrayFruinfoBoardPartNumber_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_MsanShMCFanTrayFruinfoBoardPartNumber_Type.__name__=_D
_MsanShMCFanTrayFruinfoBoardPartNumber_Object=MibTableColumn
msanShMCFanTrayFruinfoBoardPartNumber=_MsanShMCFanTrayFruinfoBoardPartNumber_Object((1,3,6,1,4,1,1332,1,1,5,3,33,33,1,17),_MsanShMCFanTrayFruinfoBoardPartNumber_Type())
msanShMCFanTrayFruinfoBoardPartNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:msanShMCFanTrayFruinfoBoardPartNumber.setStatus(_A)
class _MsanShMCFanTrayFruinfoBoardManufactureTime_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_MsanShMCFanTrayFruinfoBoardManufactureTime_Type.__name__=_C
_MsanShMCFanTrayFruinfoBoardManufactureTime_Object=MibTableColumn
msanShMCFanTrayFruinfoBoardManufactureTime=_MsanShMCFanTrayFruinfoBoardManufactureTime_Object((1,3,6,1,4,1,1332,1,1,5,3,33,33,1,18),_MsanShMCFanTrayFruinfoBoardManufactureTime_Type())
msanShMCFanTrayFruinfoBoardManufactureTime.setMaxAccess(_B)
if mibBuilder.loadTexts:msanShMCFanTrayFruinfoBoardManufactureTime.setStatus(_A)
_MsanShMCPowerSupplyVariablesTable_Object=MibTable
msanShMCPowerSupplyVariablesTable=_MsanShMCPowerSupplyVariablesTable_Object((1,3,6,1,4,1,1332,1,1,5,3,33,34))
if mibBuilder.loadTexts:msanShMCPowerSupplyVariablesTable.setStatus(_A)
_MsanShMCPowerSupplyVariablesEntry_Object=MibTableRow
msanShMCPowerSupplyVariablesEntry=_MsanShMCPowerSupplyVariablesEntry_Object((1,3,6,1,4,1,1332,1,1,5,3,33,34,1))
msanShMCPowerSupplyVariablesEntry.setIndexNames((0,_G,_a))
if mibBuilder.loadTexts:msanShMCPowerSupplyVariablesEntry.setStatus(_A)
class _MsanShMCPowerSupplySlotNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_MsanShMCPowerSupplySlotNumber_Type.__name__=_C
_MsanShMCPowerSupplySlotNumber_Object=MibTableColumn
msanShMCPowerSupplySlotNumber=_MsanShMCPowerSupplySlotNumber_Object((1,3,6,1,4,1,1332,1,1,5,3,33,34,1,1),_MsanShMCPowerSupplySlotNumber_Type())
msanShMCPowerSupplySlotNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:msanShMCPowerSupplySlotNumber.setStatus(_A)
class _MsanShMCPowerSupplyDegrade_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_L,0),(_M,1)))
_MsanShMCPowerSupplyDegrade_Type.__name__=_C
_MsanShMCPowerSupplyDegrade_Object=MibTableColumn
msanShMCPowerSupplyDegrade=_MsanShMCPowerSupplyDegrade_Object((1,3,6,1,4,1,1332,1,1,5,3,33,34,1,2),_MsanShMCPowerSupplyDegrade_Type())
msanShMCPowerSupplyDegrade.setMaxAccess(_B)
if mibBuilder.loadTexts:msanShMCPowerSupplyDegrade.setStatus(_A)
class _MsanShMCPowerSupplyFail_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_H,0),(_F,1)))
_MsanShMCPowerSupplyFail_Type.__name__=_C
_MsanShMCPowerSupplyFail_Object=MibTableColumn
msanShMCPowerSupplyFail=_MsanShMCPowerSupplyFail_Object((1,3,6,1,4,1,1332,1,1,5,3,33,34,1,3),_MsanShMCPowerSupplyFail_Type())
msanShMCPowerSupplyFail.setMaxAccess(_B)
if mibBuilder.loadTexts:msanShMCPowerSupplyFail.setStatus(_A)
class _MsanShMCPowerSupplyInhibit_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_F,0),('inhibit',1)))
_MsanShMCPowerSupplyInhibit_Type.__name__=_C
_MsanShMCPowerSupplyInhibit_Object=MibTableColumn
msanShMCPowerSupplyInhibit=_MsanShMCPowerSupplyInhibit_Object((1,3,6,1,4,1,1332,1,1,5,3,33,34,1,4),_MsanShMCPowerSupplyInhibit_Type())
msanShMCPowerSupplyInhibit.setMaxAccess(_E)
if mibBuilder.loadTexts:msanShMCPowerSupplyInhibit.setStatus(_A)
class _MsanShMCPowerSupplyHealthy_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_H,0),(_F,1)))
_MsanShMCPowerSupplyHealthy_Type.__name__=_C
_MsanShMCPowerSupplyHealthy_Object=MibTableColumn
msanShMCPowerSupplyHealthy=_MsanShMCPowerSupplyHealthy_Object((1,3,6,1,4,1,1332,1,1,5,3,33,34,1,5),_MsanShMCPowerSupplyHealthy_Type())
msanShMCPowerSupplyHealthy.setMaxAccess(_E)
if mibBuilder.loadTexts:msanShMCPowerSupplyHealthy.setStatus(_A)
class _MsanShMCPowerSupplySlaveAddress_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_MsanShMCPowerSupplySlaveAddress_Type.__name__=_C
_MsanShMCPowerSupplySlaveAddress_Object=MibTableColumn
msanShMCPowerSupplySlaveAddress=_MsanShMCPowerSupplySlaveAddress_Object((1,3,6,1,4,1,1332,1,1,5,3,33,34,1,6),_MsanShMCPowerSupplySlaveAddress_Type())
msanShMCPowerSupplySlaveAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:msanShMCPowerSupplySlaveAddress.setStatus(_A)
class _MsanShMCPowerSupplyFruDeviceId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_MsanShMCPowerSupplyFruDeviceId_Type.__name__=_C
_MsanShMCPowerSupplyFruDeviceId_Object=MibTableColumn
msanShMCPowerSupplyFruDeviceId=_MsanShMCPowerSupplyFruDeviceId_Object((1,3,6,1,4,1,1332,1,1,5,3,33,34,1,7),_MsanShMCPowerSupplyFruDeviceId_Type())
msanShMCPowerSupplyFruDeviceId.setMaxAccess(_B)
if mibBuilder.loadTexts:msanShMCPowerSupplyFruDeviceId.setStatus(_A)
class _MsanShMCPowerSupplyFruinfoProductAreaPresent_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_I,0),(_J,1)))
_MsanShMCPowerSupplyFruinfoProductAreaPresent_Type.__name__=_C
_MsanShMCPowerSupplyFruinfoProductAreaPresent_Object=MibTableColumn
msanShMCPowerSupplyFruinfoProductAreaPresent=_MsanShMCPowerSupplyFruinfoProductAreaPresent_Object((1,3,6,1,4,1,1332,1,1,5,3,33,34,1,8),_MsanShMCPowerSupplyFruinfoProductAreaPresent_Type())
msanShMCPowerSupplyFruinfoProductAreaPresent.setMaxAccess(_B)
if mibBuilder.loadTexts:msanShMCPowerSupplyFruinfoProductAreaPresent.setStatus(_A)
class _MsanShMCPowerSupplyFruinfoProductManufacturer_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_MsanShMCPowerSupplyFruinfoProductManufacturer_Type.__name__=_D
_MsanShMCPowerSupplyFruinfoProductManufacturer_Object=MibTableColumn
msanShMCPowerSupplyFruinfoProductManufacturer=_MsanShMCPowerSupplyFruinfoProductManufacturer_Object((1,3,6,1,4,1,1332,1,1,5,3,33,34,1,9),_MsanShMCPowerSupplyFruinfoProductManufacturer_Type())
msanShMCPowerSupplyFruinfoProductManufacturer.setMaxAccess(_B)
if mibBuilder.loadTexts:msanShMCPowerSupplyFruinfoProductManufacturer.setStatus(_A)
class _MsanShMCPowerSupplyFruinfoProductName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_MsanShMCPowerSupplyFruinfoProductName_Type.__name__=_D
_MsanShMCPowerSupplyFruinfoProductName_Object=MibTableColumn
msanShMCPowerSupplyFruinfoProductName=_MsanShMCPowerSupplyFruinfoProductName_Object((1,3,6,1,4,1,1332,1,1,5,3,33,34,1,10),_MsanShMCPowerSupplyFruinfoProductName_Type())
msanShMCPowerSupplyFruinfoProductName.setMaxAccess(_B)
if mibBuilder.loadTexts:msanShMCPowerSupplyFruinfoProductName.setStatus(_A)
class _MsanShMCPowerSupplyFruinfoProductPartModelNumber_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_MsanShMCPowerSupplyFruinfoProductPartModelNumber_Type.__name__=_D
_MsanShMCPowerSupplyFruinfoProductPartModelNumber_Object=MibTableColumn
msanShMCPowerSupplyFruinfoProductPartModelNumber=_MsanShMCPowerSupplyFruinfoProductPartModelNumber_Object((1,3,6,1,4,1,1332,1,1,5,3,33,34,1,11),_MsanShMCPowerSupplyFruinfoProductPartModelNumber_Type())
msanShMCPowerSupplyFruinfoProductPartModelNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:msanShMCPowerSupplyFruinfoProductPartModelNumber.setStatus(_A)
class _MsanShMCPowerSupplyFruinfoProductVersionNumber_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_MsanShMCPowerSupplyFruinfoProductVersionNumber_Type.__name__=_D
_MsanShMCPowerSupplyFruinfoProductVersionNumber_Object=MibTableColumn
msanShMCPowerSupplyFruinfoProductVersionNumber=_MsanShMCPowerSupplyFruinfoProductVersionNumber_Object((1,3,6,1,4,1,1332,1,1,5,3,33,34,1,12),_MsanShMCPowerSupplyFruinfoProductVersionNumber_Type())
msanShMCPowerSupplyFruinfoProductVersionNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:msanShMCPowerSupplyFruinfoProductVersionNumber.setStatus(_A)
class _MsanShMCPowerSupplyFruinfoProductSerialNumber_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_MsanShMCPowerSupplyFruinfoProductSerialNumber_Type.__name__=_D
_MsanShMCPowerSupplyFruinfoProductSerialNumber_Object=MibTableColumn
msanShMCPowerSupplyFruinfoProductSerialNumber=_MsanShMCPowerSupplyFruinfoProductSerialNumber_Object((1,3,6,1,4,1,1332,1,1,5,3,33,34,1,13),_MsanShMCPowerSupplyFruinfoProductSerialNumber_Type())
msanShMCPowerSupplyFruinfoProductSerialNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:msanShMCPowerSupplyFruinfoProductSerialNumber.setStatus(_A)
class _MsanShMCPowerSupplyFruinfoBoardAreaPresent_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_I,0),(_J,1)))
_MsanShMCPowerSupplyFruinfoBoardAreaPresent_Type.__name__=_C
_MsanShMCPowerSupplyFruinfoBoardAreaPresent_Object=MibTableColumn
msanShMCPowerSupplyFruinfoBoardAreaPresent=_MsanShMCPowerSupplyFruinfoBoardAreaPresent_Object((1,3,6,1,4,1,1332,1,1,5,3,33,34,1,14),_MsanShMCPowerSupplyFruinfoBoardAreaPresent_Type())
msanShMCPowerSupplyFruinfoBoardAreaPresent.setMaxAccess(_B)
if mibBuilder.loadTexts:msanShMCPowerSupplyFruinfoBoardAreaPresent.setStatus(_A)
class _MsanShMCPowerSupplyFruinfoBoardManufacturer_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_MsanShMCPowerSupplyFruinfoBoardManufacturer_Type.__name__=_D
_MsanShMCPowerSupplyFruinfoBoardManufacturer_Object=MibTableColumn
msanShMCPowerSupplyFruinfoBoardManufacturer=_MsanShMCPowerSupplyFruinfoBoardManufacturer_Object((1,3,6,1,4,1,1332,1,1,5,3,33,34,1,15),_MsanShMCPowerSupplyFruinfoBoardManufacturer_Type())
msanShMCPowerSupplyFruinfoBoardManufacturer.setMaxAccess(_B)
if mibBuilder.loadTexts:msanShMCPowerSupplyFruinfoBoardManufacturer.setStatus(_A)
class _MsanShMCPowerSupplyFruinfoBoardProductName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_MsanShMCPowerSupplyFruinfoBoardProductName_Type.__name__=_D
_MsanShMCPowerSupplyFruinfoBoardProductName_Object=MibTableColumn
msanShMCPowerSupplyFruinfoBoardProductName=_MsanShMCPowerSupplyFruinfoBoardProductName_Object((1,3,6,1,4,1,1332,1,1,5,3,33,34,1,16),_MsanShMCPowerSupplyFruinfoBoardProductName_Type())
msanShMCPowerSupplyFruinfoBoardProductName.setMaxAccess(_B)
if mibBuilder.loadTexts:msanShMCPowerSupplyFruinfoBoardProductName.setStatus(_A)
class _MsanShMCPowerSupplyFruinfoBoardSerialNumber_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_MsanShMCPowerSupplyFruinfoBoardSerialNumber_Type.__name__=_D
_MsanShMCPowerSupplyFruinfoBoardSerialNumber_Object=MibTableColumn
msanShMCPowerSupplyFruinfoBoardSerialNumber=_MsanShMCPowerSupplyFruinfoBoardSerialNumber_Object((1,3,6,1,4,1,1332,1,1,5,3,33,34,1,17),_MsanShMCPowerSupplyFruinfoBoardSerialNumber_Type())
msanShMCPowerSupplyFruinfoBoardSerialNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:msanShMCPowerSupplyFruinfoBoardSerialNumber.setStatus(_A)
class _MsanShMCPowerSupplyFruinfoBoardPartNumber_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_MsanShMCPowerSupplyFruinfoBoardPartNumber_Type.__name__=_D
_MsanShMCPowerSupplyFruinfoBoardPartNumber_Object=MibTableColumn
msanShMCPowerSupplyFruinfoBoardPartNumber=_MsanShMCPowerSupplyFruinfoBoardPartNumber_Object((1,3,6,1,4,1,1332,1,1,5,3,33,34,1,18),_MsanShMCPowerSupplyFruinfoBoardPartNumber_Type())
msanShMCPowerSupplyFruinfoBoardPartNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:msanShMCPowerSupplyFruinfoBoardPartNumber.setStatus(_A)
class _MsanShMCPowerSupplyFruinfoBoardmanufactureTime_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_MsanShMCPowerSupplyFruinfoBoardmanufactureTime_Type.__name__=_C
_MsanShMCPowerSupplyFruinfoBoardmanufactureTime_Object=MibTableColumn
msanShMCPowerSupplyFruinfoBoardmanufactureTime=_MsanShMCPowerSupplyFruinfoBoardmanufactureTime_Object((1,3,6,1,4,1,1332,1,1,5,3,33,34,1,19),_MsanShMCPowerSupplyFruinfoBoardmanufactureTime_Type())
msanShMCPowerSupplyFruinfoBoardmanufactureTime.setMaxAccess(_B)
if mibBuilder.loadTexts:msanShMCPowerSupplyFruinfoBoardmanufactureTime.setStatus(_A)
_MsanShMCShelfManagerVariablesTable_Object=MibTable
msanShMCShelfManagerVariablesTable=_MsanShMCShelfManagerVariablesTable_Object((1,3,6,1,4,1,1332,1,1,5,3,33,35))
if mibBuilder.loadTexts:msanShMCShelfManagerVariablesTable.setStatus(_A)
_MsanShMCShelfManagerVariablesEntry_Object=MibTableRow
msanShMCShelfManagerVariablesEntry=_MsanShMCShelfManagerVariablesEntry_Object((1,3,6,1,4,1,1332,1,1,5,3,33,35,1))
msanShMCShelfManagerVariablesEntry.setIndexNames((0,_G,_b))
if mibBuilder.loadTexts:msanShMCShelfManagerVariablesEntry.setStatus(_A)
class _MsanShMCShelfManagerSlotNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_MsanShMCShelfManagerSlotNumber_Type.__name__=_C
_MsanShMCShelfManagerSlotNumber_Object=MibTableColumn
msanShMCShelfManagerSlotNumber=_MsanShMCShelfManagerSlotNumber_Object((1,3,6,1,4,1,1332,1,1,5,3,33,35,1,1),_MsanShMCShelfManagerSlotNumber_Type())
msanShMCShelfManagerSlotNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:msanShMCShelfManagerSlotNumber.setStatus(_A)
class _MsanShMCShelfManagerSlaveAddress_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_MsanShMCShelfManagerSlaveAddress_Type.__name__=_C
_MsanShMCShelfManagerSlaveAddress_Object=MibTableColumn
msanShMCShelfManagerSlaveAddress=_MsanShMCShelfManagerSlaveAddress_Object((1,3,6,1,4,1,1332,1,1,5,3,33,35,1,2),_MsanShMCShelfManagerSlaveAddress_Type())
msanShMCShelfManagerSlaveAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:msanShMCShelfManagerSlaveAddress.setStatus(_A)
class _MsanShMCShelfManagerPresent_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_L,0),(_M,1)))
_MsanShMCShelfManagerPresent_Type.__name__=_C
_MsanShMCShelfManagerPresent_Object=MibTableColumn
msanShMCShelfManagerPresent=_MsanShMCShelfManagerPresent_Object((1,3,6,1,4,1,1332,1,1,5,3,33,35,1,3),_MsanShMCShelfManagerPresent_Type())
msanShMCShelfManagerPresent.setMaxAccess(_B)
if mibBuilder.loadTexts:msanShMCShelfManagerPresent.setStatus(_A)
class _MsanShMCShelfManagerHealthy_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_H,0),(_F,1)))
_MsanShMCShelfManagerHealthy_Type.__name__=_C
_MsanShMCShelfManagerHealthy_Object=MibTableColumn
msanShMCShelfManagerHealthy=_MsanShMCShelfManagerHealthy_Object((1,3,6,1,4,1,1332,1,1,5,3,33,35,1,4),_MsanShMCShelfManagerHealthy_Type())
msanShMCShelfManagerHealthy.setMaxAccess(_B)
if mibBuilder.loadTexts:msanShMCShelfManagerHealthy.setStatus(_A)
class _MsanShMCShelfManagerActive_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('standby',0),('active',1)))
_MsanShMCShelfManagerActive_Type.__name__=_C
_MsanShMCShelfManagerActive_Object=MibTableColumn
msanShMCShelfManagerActive=_MsanShMCShelfManagerActive_Object((1,3,6,1,4,1,1332,1,1,5,3,33,35,1,5),_MsanShMCShelfManagerActive_Type())
msanShMCShelfManagerActive.setMaxAccess(_E)
if mibBuilder.loadTexts:msanShMCShelfManagerActive.setStatus(_A)
class _MsanShMCShelfManagerReset_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_N,0),(_O,1)))
_MsanShMCShelfManagerReset_Type.__name__=_C
_MsanShMCShelfManagerReset_Object=MibTableColumn
msanShMCShelfManagerReset=_MsanShMCShelfManagerReset_Object((1,3,6,1,4,1,1332,1,1,5,3,33,35,1,6),_MsanShMCShelfManagerReset_Type())
msanShMCShelfManagerReset.setMaxAccess(_E)
if mibBuilder.loadTexts:msanShMCShelfManagerReset.setStatus(_A)
class _MsanShMCShelfManagerFruinfoProductAreaPresent_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_I,0),(_J,1)))
_MsanShMCShelfManagerFruinfoProductAreaPresent_Type.__name__=_C
_MsanShMCShelfManagerFruinfoProductAreaPresent_Object=MibTableColumn
msanShMCShelfManagerFruinfoProductAreaPresent=_MsanShMCShelfManagerFruinfoProductAreaPresent_Object((1,3,6,1,4,1,1332,1,1,5,3,33,35,1,7),_MsanShMCShelfManagerFruinfoProductAreaPresent_Type())
msanShMCShelfManagerFruinfoProductAreaPresent.setMaxAccess(_B)
if mibBuilder.loadTexts:msanShMCShelfManagerFruinfoProductAreaPresent.setStatus(_A)
class _MsanShMCShelfManagerFruinfoProductManufacturer_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_MsanShMCShelfManagerFruinfoProductManufacturer_Type.__name__=_D
_MsanShMCShelfManagerFruinfoProductManufacturer_Object=MibTableColumn
msanShMCShelfManagerFruinfoProductManufacturer=_MsanShMCShelfManagerFruinfoProductManufacturer_Object((1,3,6,1,4,1,1332,1,1,5,3,33,35,1,8),_MsanShMCShelfManagerFruinfoProductManufacturer_Type())
msanShMCShelfManagerFruinfoProductManufacturer.setMaxAccess(_B)
if mibBuilder.loadTexts:msanShMCShelfManagerFruinfoProductManufacturer.setStatus(_A)
class _MsanShMCShelfManagerFruinfoProductName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_MsanShMCShelfManagerFruinfoProductName_Type.__name__=_D
_MsanShMCShelfManagerFruinfoProductName_Object=MibTableColumn
msanShMCShelfManagerFruinfoProductName=_MsanShMCShelfManagerFruinfoProductName_Object((1,3,6,1,4,1,1332,1,1,5,3,33,35,1,9),_MsanShMCShelfManagerFruinfoProductName_Type())
msanShMCShelfManagerFruinfoProductName.setMaxAccess(_B)
if mibBuilder.loadTexts:msanShMCShelfManagerFruinfoProductName.setStatus(_A)
class _MsanShMCShelfManagerFruinfoProductPartModelNumber_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_MsanShMCShelfManagerFruinfoProductPartModelNumber_Type.__name__=_D
_MsanShMCShelfManagerFruinfoProductPartModelNumber_Object=MibTableColumn
msanShMCShelfManagerFruinfoProductPartModelNumber=_MsanShMCShelfManagerFruinfoProductPartModelNumber_Object((1,3,6,1,4,1,1332,1,1,5,3,33,35,1,10),_MsanShMCShelfManagerFruinfoProductPartModelNumber_Type())
msanShMCShelfManagerFruinfoProductPartModelNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:msanShMCShelfManagerFruinfoProductPartModelNumber.setStatus(_A)
class _MsanShMCShelfManagerFruinfoProductVersionNumber_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_MsanShMCShelfManagerFruinfoProductVersionNumber_Type.__name__=_D
_MsanShMCShelfManagerFruinfoProductVersionNumber_Object=MibTableColumn
msanShMCShelfManagerFruinfoProductVersionNumber=_MsanShMCShelfManagerFruinfoProductVersionNumber_Object((1,3,6,1,4,1,1332,1,1,5,3,33,35,1,11),_MsanShMCShelfManagerFruinfoProductVersionNumber_Type())
msanShMCShelfManagerFruinfoProductVersionNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:msanShMCShelfManagerFruinfoProductVersionNumber.setStatus(_A)
class _MsanShMCShelfManagerFruinfoProductSerialNumber_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_MsanShMCShelfManagerFruinfoProductSerialNumber_Type.__name__=_D
_MsanShMCShelfManagerFruinfoProductSerialNumber_Object=MibTableColumn
msanShMCShelfManagerFruinfoProductSerialNumber=_MsanShMCShelfManagerFruinfoProductSerialNumber_Object((1,3,6,1,4,1,1332,1,1,5,3,33,35,1,12),_MsanShMCShelfManagerFruinfoProductSerialNumber_Type())
msanShMCShelfManagerFruinfoProductSerialNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:msanShMCShelfManagerFruinfoProductSerialNumber.setStatus(_A)
class _MsanShMCShelfManagerFruinfoBoardAreaPresent_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_I,0),(_J,1)))
_MsanShMCShelfManagerFruinfoBoardAreaPresent_Type.__name__=_C
_MsanShMCShelfManagerFruinfoBoardAreaPresent_Object=MibTableColumn
msanShMCShelfManagerFruinfoBoardAreaPresent=_MsanShMCShelfManagerFruinfoBoardAreaPresent_Object((1,3,6,1,4,1,1332,1,1,5,3,33,35,1,13),_MsanShMCShelfManagerFruinfoBoardAreaPresent_Type())
msanShMCShelfManagerFruinfoBoardAreaPresent.setMaxAccess(_B)
if mibBuilder.loadTexts:msanShMCShelfManagerFruinfoBoardAreaPresent.setStatus(_A)
class _MsanShMCShelfManagerFruinfoBoardManufacturer_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_MsanShMCShelfManagerFruinfoBoardManufacturer_Type.__name__=_D
_MsanShMCShelfManagerFruinfoBoardManufacturer_Object=MibTableColumn
msanShMCShelfManagerFruinfoBoardManufacturer=_MsanShMCShelfManagerFruinfoBoardManufacturer_Object((1,3,6,1,4,1,1332,1,1,5,3,33,35,1,14),_MsanShMCShelfManagerFruinfoBoardManufacturer_Type())
msanShMCShelfManagerFruinfoBoardManufacturer.setMaxAccess(_B)
if mibBuilder.loadTexts:msanShMCShelfManagerFruinfoBoardManufacturer.setStatus(_A)
class _MsanShMCShelfManagerFruinfoBoardProductName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_MsanShMCShelfManagerFruinfoBoardProductName_Type.__name__=_D
_MsanShMCShelfManagerFruinfoBoardProductName_Object=MibTableColumn
msanShMCShelfManagerFruinfoBoardProductName=_MsanShMCShelfManagerFruinfoBoardProductName_Object((1,3,6,1,4,1,1332,1,1,5,3,33,35,1,15),_MsanShMCShelfManagerFruinfoBoardProductName_Type())
msanShMCShelfManagerFruinfoBoardProductName.setMaxAccess(_B)
if mibBuilder.loadTexts:msanShMCShelfManagerFruinfoBoardProductName.setStatus(_A)
class _MsanShMCShelfManagerFruinfoBoardSerialNumber_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_MsanShMCShelfManagerFruinfoBoardSerialNumber_Type.__name__=_D
_MsanShMCShelfManagerFruinfoBoardSerialNumber_Object=MibTableColumn
msanShMCShelfManagerFruinfoBoardSerialNumber=_MsanShMCShelfManagerFruinfoBoardSerialNumber_Object((1,3,6,1,4,1,1332,1,1,5,3,33,35,1,16),_MsanShMCShelfManagerFruinfoBoardSerialNumber_Type())
msanShMCShelfManagerFruinfoBoardSerialNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:msanShMCShelfManagerFruinfoBoardSerialNumber.setStatus(_A)
class _MsanShMCShelfManagerFruinfoBoardPartNumber_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_MsanShMCShelfManagerFruinfoBoardPartNumber_Type.__name__=_D
_MsanShMCShelfManagerFruinfoBoardPartNumber_Object=MibTableColumn
msanShMCShelfManagerFruinfoBoardPartNumber=_MsanShMCShelfManagerFruinfoBoardPartNumber_Object((1,3,6,1,4,1,1332,1,1,5,3,33,35,1,17),_MsanShMCShelfManagerFruinfoBoardPartNumber_Type())
msanShMCShelfManagerFruinfoBoardPartNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:msanShMCShelfManagerFruinfoBoardPartNumber.setStatus(_A)
class _MsanShMCShelfManagerFruinfoBoardmanufactureTime_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_MsanShMCShelfManagerFruinfoBoardmanufactureTime_Type.__name__=_C
_MsanShMCShelfManagerFruinfoBoardmanufactureTime_Object=MibTableColumn
msanShMCShelfManagerFruinfoBoardmanufactureTime=_MsanShMCShelfManagerFruinfoBoardmanufactureTime_Object((1,3,6,1,4,1,1332,1,1,5,3,33,35,1,18),_MsanShMCShelfManagerFruinfoBoardmanufactureTime_Type())
msanShMCShelfManagerFruinfoBoardmanufactureTime.setMaxAccess(_B)
if mibBuilder.loadTexts:msanShMCShelfManagerFruinfoBoardmanufactureTime.setStatus(_A)
_MsanShMCChassisVariablesTable_Object=MibTable
msanShMCChassisVariablesTable=_MsanShMCChassisVariablesTable_Object((1,3,6,1,4,1,1332,1,1,5,3,33,36))
if mibBuilder.loadTexts:msanShMCChassisVariablesTable.setStatus(_A)
_MsanShMCChassisVariablesEntry_Object=MibTableRow
msanShMCChassisVariablesEntry=_MsanShMCChassisVariablesEntry_Object((1,3,6,1,4,1,1332,1,1,5,3,33,36,1))
msanShMCChassisVariablesEntry.setIndexNames((0,_G,_c))
if mibBuilder.loadTexts:msanShMCChassisVariablesEntry.setStatus(_A)
class _MsanShMCChassisId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_MsanShMCChassisId_Type.__name__=_C
_MsanShMCChassisId_Object=MibTableColumn
msanShMCChassisId=_MsanShMCChassisId_Object((1,3,6,1,4,1,1332,1,1,5,3,33,36,1,1),_MsanShMCChassisId_Type())
msanShMCChassisId.setMaxAccess(_B)
if mibBuilder.loadTexts:msanShMCChassisId.setStatus(_A)
class _MsanShMCChassisType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_MsanShMCChassisType_Type.__name__=_C
_MsanShMCChassisType_Object=MibTableColumn
msanShMCChassisType=_MsanShMCChassisType_Object((1,3,6,1,4,1,1332,1,1,5,3,33,36,1,2),_MsanShMCChassisType_Type())
msanShMCChassisType.setMaxAccess(_B)
if mibBuilder.loadTexts:msanShMCChassisType.setStatus(_A)
class _MsanShMCChassisPartNumber_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_MsanShMCChassisPartNumber_Type.__name__=_D
_MsanShMCChassisPartNumber_Object=MibTableColumn
msanShMCChassisPartNumber=_MsanShMCChassisPartNumber_Object((1,3,6,1,4,1,1332,1,1,5,3,33,36,1,3),_MsanShMCChassisPartNumber_Type())
msanShMCChassisPartNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:msanShMCChassisPartNumber.setStatus(_A)
class _MsanShMCChassisSerialNumber_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_MsanShMCChassisSerialNumber_Type.__name__=_D
_MsanShMCChassisSerialNumber_Object=MibTableColumn
msanShMCChassisSerialNumber=_MsanShMCChassisSerialNumber_Object((1,3,6,1,4,1,1332,1,1,5,3,33,36,1,4),_MsanShMCChassisSerialNumber_Type())
msanShMCChassisSerialNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:msanShMCChassisSerialNumber.setStatus(_A)
class _MsanShMCChassisProductAreaPresent_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_I,0),(_J,1)))
_MsanShMCChassisProductAreaPresent_Type.__name__=_C
_MsanShMCChassisProductAreaPresent_Object=MibTableColumn
msanShMCChassisProductAreaPresent=_MsanShMCChassisProductAreaPresent_Object((1,3,6,1,4,1,1332,1,1,5,3,33,36,1,5),_MsanShMCChassisProductAreaPresent_Type())
msanShMCChassisProductAreaPresent.setMaxAccess(_B)
if mibBuilder.loadTexts:msanShMCChassisProductAreaPresent.setStatus(_A)
class _MsanShMCChassisProductManufacturer_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_MsanShMCChassisProductManufacturer_Type.__name__=_D
_MsanShMCChassisProductManufacturer_Object=MibTableColumn
msanShMCChassisProductManufacturer=_MsanShMCChassisProductManufacturer_Object((1,3,6,1,4,1,1332,1,1,5,3,33,36,1,6),_MsanShMCChassisProductManufacturer_Type())
msanShMCChassisProductManufacturer.setMaxAccess(_B)
if mibBuilder.loadTexts:msanShMCChassisProductManufacturer.setStatus(_A)
class _MsanShMCChassisProductName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_MsanShMCChassisProductName_Type.__name__=_D
_MsanShMCChassisProductName_Object=MibTableColumn
msanShMCChassisProductName=_MsanShMCChassisProductName_Object((1,3,6,1,4,1,1332,1,1,5,3,33,36,1,7),_MsanShMCChassisProductName_Type())
msanShMCChassisProductName.setMaxAccess(_B)
if mibBuilder.loadTexts:msanShMCChassisProductName.setStatus(_A)
class _MsanShMCChassisProductPartModelNumber_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_MsanShMCChassisProductPartModelNumber_Type.__name__=_D
_MsanShMCChassisProductPartModelNumber_Object=MibTableColumn
msanShMCChassisProductPartModelNumber=_MsanShMCChassisProductPartModelNumber_Object((1,3,6,1,4,1,1332,1,1,5,3,33,36,1,8),_MsanShMCChassisProductPartModelNumber_Type())
msanShMCChassisProductPartModelNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:msanShMCChassisProductPartModelNumber.setStatus(_A)
class _MsanShMCChassisProductVersionNumber_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_MsanShMCChassisProductVersionNumber_Type.__name__=_D
_MsanShMCChassisProductVersionNumber_Object=MibTableColumn
msanShMCChassisProductVersionNumber=_MsanShMCChassisProductVersionNumber_Object((1,3,6,1,4,1,1332,1,1,5,3,33,36,1,9),_MsanShMCChassisProductVersionNumber_Type())
msanShMCChassisProductVersionNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:msanShMCChassisProductVersionNumber.setStatus(_A)
class _MsanShMCChassisProductSerialNumber_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_MsanShMCChassisProductSerialNumber_Type.__name__=_D
_MsanShMCChassisProductSerialNumber_Object=MibTableColumn
msanShMCChassisProductSerialNumber=_MsanShMCChassisProductSerialNumber_Object((1,3,6,1,4,1,1332,1,1,5,3,33,36,1,10),_MsanShMCChassisProductSerialNumber_Type())
msanShMCChassisProductSerialNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:msanShMCChassisProductSerialNumber.setStatus(_A)
class _MsanShMCChassisBoardAreaPresent_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_I,0),(_J,1)))
_MsanShMCChassisBoardAreaPresent_Type.__name__=_C
_MsanShMCChassisBoardAreaPresent_Object=MibTableColumn
msanShMCChassisBoardAreaPresent=_MsanShMCChassisBoardAreaPresent_Object((1,3,6,1,4,1,1332,1,1,5,3,33,36,1,11),_MsanShMCChassisBoardAreaPresent_Type())
msanShMCChassisBoardAreaPresent.setMaxAccess(_B)
if mibBuilder.loadTexts:msanShMCChassisBoardAreaPresent.setStatus(_A)
class _MsanShMCChassisBoardManufacturer_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_MsanShMCChassisBoardManufacturer_Type.__name__=_D
_MsanShMCChassisBoardManufacturer_Object=MibTableColumn
msanShMCChassisBoardManufacturer=_MsanShMCChassisBoardManufacturer_Object((1,3,6,1,4,1,1332,1,1,5,3,33,36,1,12),_MsanShMCChassisBoardManufacturer_Type())
msanShMCChassisBoardManufacturer.setMaxAccess(_B)
if mibBuilder.loadTexts:msanShMCChassisBoardManufacturer.setStatus(_A)
class _MsanShMCChassisBoardProductName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_MsanShMCChassisBoardProductName_Type.__name__=_D
_MsanShMCChassisBoardProductName_Object=MibTableColumn
msanShMCChassisBoardProductName=_MsanShMCChassisBoardProductName_Object((1,3,6,1,4,1,1332,1,1,5,3,33,36,1,13),_MsanShMCChassisBoardProductName_Type())
msanShMCChassisBoardProductName.setMaxAccess(_B)
if mibBuilder.loadTexts:msanShMCChassisBoardProductName.setStatus(_A)
class _MsanShMCChassisBoardSerialNumber_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_MsanShMCChassisBoardSerialNumber_Type.__name__=_D
_MsanShMCChassisBoardSerialNumber_Object=MibTableColumn
msanShMCChassisBoardSerialNumber=_MsanShMCChassisBoardSerialNumber_Object((1,3,6,1,4,1,1332,1,1,5,3,33,36,1,14),_MsanShMCChassisBoardSerialNumber_Type())
msanShMCChassisBoardSerialNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:msanShMCChassisBoardSerialNumber.setStatus(_A)
class _MsanShMCChassisBoardPartNumber_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_MsanShMCChassisBoardPartNumber_Type.__name__=_D
_MsanShMCChassisBoardPartNumber_Object=MibTableColumn
msanShMCChassisBoardPartNumber=_MsanShMCChassisBoardPartNumber_Object((1,3,6,1,4,1,1332,1,1,5,3,33,36,1,15),_MsanShMCChassisBoardPartNumber_Type())
msanShMCChassisBoardPartNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:msanShMCChassisBoardPartNumber.setStatus(_A)
class _MsanShMCChassisBoardmanufactureTime_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_MsanShMCChassisBoardmanufactureTime_Type.__name__=_C
_MsanShMCChassisBoardmanufactureTime_Object=MibTableColumn
msanShMCChassisBoardmanufactureTime=_MsanShMCChassisBoardmanufactureTime_Object((1,3,6,1,4,1,1332,1,1,5,3,33,36,1,16),_MsanShMCChassisBoardmanufactureTime_Type())
msanShMCChassisBoardmanufactureTime.setMaxAccess(_B)
if mibBuilder.loadTexts:msanShMCChassisBoardmanufactureTime.setStatus(_A)
_MsanShMCEventVariablesTable_Object=MibTable
msanShMCEventVariablesTable=_MsanShMCEventVariablesTable_Object((1,3,6,1,4,1,1332,1,1,5,3,33,37))
if mibBuilder.loadTexts:msanShMCEventVariablesTable.setStatus(_A)
_MsanShMCEventVariablesEntry_Object=MibTableRow
msanShMCEventVariablesEntry=_MsanShMCEventVariablesEntry_Object((1,3,6,1,4,1,1332,1,1,5,3,33,37,1))
msanShMCEventVariablesEntry.setIndexNames((0,_G,_d))
if mibBuilder.loadTexts:msanShMCEventVariablesEntry.setStatus(_A)
class _MsanShMCEventIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_MsanShMCEventIndex_Type.__name__=_C
_MsanShMCEventIndex_Object=MibTableColumn
msanShMCEventIndex=_MsanShMCEventIndex_Object((1,3,6,1,4,1,1332,1,1,5,3,33,37,1,1),_MsanShMCEventIndex_Type())
msanShMCEventIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:msanShMCEventIndex.setStatus(_A)
class _MsanShMCEventDelete_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_MsanShMCEventDelete_Type.__name__=_C
_MsanShMCEventDelete_Object=MibTableColumn
msanShMCEventDelete=_MsanShMCEventDelete_Object((1,3,6,1,4,1,1332,1,1,5,3,33,37,1,2),_MsanShMCEventDelete_Type())
msanShMCEventDelete.setMaxAccess(_E)
if mibBuilder.loadTexts:msanShMCEventDelete.setStatus(_A)
class _MsanShMCEventTimeStamp_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_MsanShMCEventTimeStamp_Type.__name__=_C
_MsanShMCEventTimeStamp_Object=MibTableColumn
msanShMCEventTimeStamp=_MsanShMCEventTimeStamp_Object((1,3,6,1,4,1,1332,1,1,5,3,33,37,1,3),_MsanShMCEventTimeStamp_Type())
msanShMCEventTimeStamp.setMaxAccess(_B)
if mibBuilder.loadTexts:msanShMCEventTimeStamp.setStatus(_A)
class _MsanShMCEventClass_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,225,240)));namedValues=NamedValues(*(('other',0),('temperature',1),('voltage',2),(_A,3),('fan',4),('powerstate',225),('hotswap',240)))
_MsanShMCEventClass_Type.__name__=_C
_MsanShMCEventClass_Object=MibTableColumn
msanShMCEventClass=_MsanShMCEventClass_Object((1,3,6,1,4,1,1332,1,1,5,3,33,37,1,4),_MsanShMCEventClass_Type())
msanShMCEventClass.setMaxAccess(_B)
if mibBuilder.loadTexts:msanShMCEventClass.setStatus(_A)
class _MsanShMCEventType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15)));namedValues=NamedValues(*(('other',0),('aboveUpperNonRecoverable',1),('aboveUpperCritical',2),('aboveUpperNonCritical',3),('belowLowerNonrecoverable',4),('belowLowerCritical',5),('belowLowerNonCritical',6),('inserted',7),('activated',8),('communicationLost',9),('communicationRestored',10),('deactivated',11),('extracted',12),('powerDegrade',13),('powerFail',14),('powerInhibit',15)))
_MsanShMCEventType_Type.__name__=_C
_MsanShMCEventType_Object=MibTableColumn
msanShMCEventType=_MsanShMCEventType_Object((1,3,6,1,4,1,1332,1,1,5,3,33,37,1,5),_MsanShMCEventType_Type())
msanShMCEventType.setMaxAccess(_B)
if mibBuilder.loadTexts:msanShMCEventType.setStatus(_A)
class _MsanShMCEventAsserted_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('deasserted',0),('asserted',1)))
_MsanShMCEventAsserted_Type.__name__=_C
_MsanShMCEventAsserted_Object=MibTableColumn
msanShMCEventAsserted=_MsanShMCEventAsserted_Object((1,3,6,1,4,1,1332,1,1,5,3,33,37,1,6),_MsanShMCEventAsserted_Type())
msanShMCEventAsserted.setMaxAccess(_B)
if mibBuilder.loadTexts:msanShMCEventAsserted.setStatus(_A)
class _MsanShMCEventOriginSiteType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_MsanShMCEventOriginSiteType_Type.__name__=_C
_MsanShMCEventOriginSiteType_Object=MibTableColumn
msanShMCEventOriginSiteType=_MsanShMCEventOriginSiteType_Object((1,3,6,1,4,1,1332,1,1,5,3,33,37,1,7),_MsanShMCEventOriginSiteType_Type())
msanShMCEventOriginSiteType.setMaxAccess(_B)
if mibBuilder.loadTexts:msanShMCEventOriginSiteType.setStatus(_A)
class _MsanShMCEventOriginSiteNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_MsanShMCEventOriginSiteNumber_Type.__name__=_C
_MsanShMCEventOriginSiteNumber_Object=MibTableColumn
msanShMCEventOriginSiteNumber=_MsanShMCEventOriginSiteNumber_Object((1,3,6,1,4,1,1332,1,1,5,3,33,37,1,8),_MsanShMCEventOriginSiteNumber_Type())
msanShMCEventOriginSiteNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:msanShMCEventOriginSiteNumber.setStatus(_A)
class _MsanShMCEventOriginSlaveAddress_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_MsanShMCEventOriginSlaveAddress_Type.__name__=_C
_MsanShMCEventOriginSlaveAddress_Object=MibTableColumn
msanShMCEventOriginSlaveAddress=_MsanShMCEventOriginSlaveAddress_Object((1,3,6,1,4,1,1332,1,1,5,3,33,37,1,9),_MsanShMCEventOriginSlaveAddress_Type())
msanShMCEventOriginSlaveAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:msanShMCEventOriginSlaveAddress.setStatus(_A)
class _MsanShMCEventOriginFruId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_MsanShMCEventOriginFruId_Type.__name__=_C
_MsanShMCEventOriginFruId_Object=MibTableColumn
msanShMCEventOriginFruId=_MsanShMCEventOriginFruId_Object((1,3,6,1,4,1,1332,1,1,5,3,33,37,1,10),_MsanShMCEventOriginFruId_Type())
msanShMCEventOriginFruId.setMaxAccess(_B)
if mibBuilder.loadTexts:msanShMCEventOriginFruId.setStatus(_A)
class _MsanShMCEventOriginSensorNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_MsanShMCEventOriginSensorNumber_Type.__name__=_C
_MsanShMCEventOriginSensorNumber_Object=MibTableColumn
msanShMCEventOriginSensorNumber=_MsanShMCEventOriginSensorNumber_Object((1,3,6,1,4,1,1332,1,1,5,3,33,37,1,11),_MsanShMCEventOriginSensorNumber_Type())
msanShMCEventOriginSensorNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:msanShMCEventOriginSensorNumber.setStatus(_A)
_MsanShMCGlobal_ObjectIdentity=ObjectIdentity
msanShMCGlobal=_MsanShMCGlobal_ObjectIdentity((1,3,6,1,4,1,1332,1,1,5,3,33,38))
class _MsanShMCSelectivePowerOffAdminMode_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('enable',1),('disable',2)))
_MsanShMCSelectivePowerOffAdminMode_Type.__name__=_C
_MsanShMCSelectivePowerOffAdminMode_Object=MibScalar
msanShMCSelectivePowerOffAdminMode=_MsanShMCSelectivePowerOffAdminMode_Object((1,3,6,1,4,1,1332,1,1,5,3,33,38,1),_MsanShMCSelectivePowerOffAdminMode_Type())
msanShMCSelectivePowerOffAdminMode.setMaxAccess(_E)
if mibBuilder.loadTexts:msanShMCSelectivePowerOffAdminMode.setStatus(_A)
class _MsanSHMCSelectivePowerOffOffDelay_Type(Integer32):defaultValue=5;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,10))
_MsanSHMCSelectivePowerOffOffDelay_Type.__name__=_C
_MsanSHMCSelectivePowerOffOffDelay_Object=MibScalar
msanSHMCSelectivePowerOffOffDelay=_MsanSHMCSelectivePowerOffOffDelay_Object((1,3,6,1,4,1,1332,1,1,5,3,33,38,2),_MsanSHMCSelectivePowerOffOffDelay_Type())
msanSHMCSelectivePowerOffOffDelay.setMaxAccess(_E)
if mibBuilder.loadTexts:msanSHMCSelectivePowerOffOffDelay.setStatus(_A)
if mibBuilder.loadTexts:msanSHMCSelectivePowerOffOffDelay.setUnits(_e)
class _MsanSHMCSelectivePowerOffOnDelay_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,10))
_MsanSHMCSelectivePowerOffOnDelay_Type.__name__=_C
_MsanSHMCSelectivePowerOffOnDelay_Object=MibScalar
msanSHMCSelectivePowerOffOnDelay=_MsanSHMCSelectivePowerOffOnDelay_Object((1,3,6,1,4,1,1332,1,1,5,3,33,38,3),_MsanSHMCSelectivePowerOffOnDelay_Type())
msanSHMCSelectivePowerOffOnDelay.setMaxAccess(_E)
if mibBuilder.loadTexts:msanSHMCSelectivePowerOffOnDelay.setStatus(_A)
if mibBuilder.loadTexts:msanSHMCSelectivePowerOffOnDelay.setUnits(_e)
mibBuilder.exportSymbols(_G,**{'msanShMC':msanShMC,'msanShMCImpControllerVariablesTable':msanShMCImpControllerVariablesTable,'msanShMCImpControllerVariablesEntry':msanShMCImpControllerVariablesEntry,_P:msanShMCImpControllerIndex,'msanShMCImpControllerSdrVersion':msanShMCImpControllerSdrVersion,'msanShMCImpControllerPicmgVersion':msanShMCImpControllerPicmgVersion,'msanShMCImpControllerSlaveAddress':msanShMCImpControllerSlaveAddress,'msanShMCImpControllerChannelNumber':msanShMCImpControllerChannelNumber,'msanShMCImpControllerPowerStateNotification':msanShMCImpControllerPowerStateNotification,'msanShMCImpControllerGlobalInitialisation':msanShMCImpControllerGlobalInitialisation,'msanShMCImpControllerCapabilities':msanShMCImpControllerCapabilities,'msanShMCImpControllerIdString':msanShMCImpControllerIdString,'msanShMCImpControllerMaximumFru':msanShMCImpControllerMaximumFru,'msanShMCImpControllerOwnFruId':msanShMCImpControllerOwnFruId,'msanShMCFruDeviceVariablesTable':msanShMCFruDeviceVariablesTable,'msanShMCFruDeviceVariablesEntry':msanShMCFruDeviceVariablesEntry,_Q:msanShMCFruDeviceIndex,'msanShMCFruDeviceSdrVersion':msanShMCFruDeviceSdrVersion,'msanShMCFruDeviceSlaveAddress':msanShMCFruDeviceSlaveAddress,'msanShMCFruDeviceSFruDeviceId':msanShMCFruDeviceSFruDeviceId,'msanShMCFruDeviceChannelNumber':msanShMCFruDeviceChannelNumber,'msanShMCFruDeviceDeviceType':msanShMCFruDeviceDeviceType,'msanShMCFruDeviceDeviceTypeModifier':msanShMCFruDeviceDeviceTypeModifier,'msanShMCFruDeviceFruEntityId':msanShMCFruDeviceFruEntityId,'msanShMCFruDeviceFruEntityInstance':msanShMCFruDeviceFruEntityInstance,'msanShMCFruDeviceIdString':msanShMCFruDeviceIdString,'msanShMCFruDeviceHotSwapState':msanShMCFruDeviceHotSwapState,'msanShMCFruDeviceActivated':msanShMCFruDeviceActivated,'msanShMCSensorVariablesTable':msanShMCSensorVariablesTable,'msanShMCSensorVariablesEntry':msanShMCSensorVariablesEntry,_R:msanShMCSensorIndex,'msanShMCSensorSdrVersion':msanShMCSensorSdrVersion,'msanShMCSensorRecordType':msanShMCSensorRecordType,'msanShMCSensorOwnerId':msanShMCSensorOwnerId,'msanShMCSensorOwnerLun':msanShMCSensorOwnerLun,'msanShMCSensorNumber':msanShMCSensorNumber,'msanShMCSensorEntityInstance':msanShMCSensorEntityInstance,'msanShMCSensorEntityId':msanShMCSensorEntityId,'msanShMCSensorInitialisation':msanShMCSensorInitialisation,'msanShMCSensorCapabilities':msanShMCSensorCapabilities,'msanShMCSensorType':msanShMCSensorType,'msanShMCSensorEvent':msanShMCSensorEvent,'msanShMCSensorAssertionEventMask':msanShMCSensorAssertionEventMask,'msanShMCSensorDeassertionEventMask':msanShMCSensorDeassertionEventMask,'msanShMCSensorMask':msanShMCSensorMask,'msanShMCSensorUnit1':msanShMCSensorUnit1,'msanShMCSensorUnit2':msanShMCSensorUnit2,'msanShMCSensorUnit3':msanShMCSensorUnit3,'msanShMCSensorLinearization':msanShMCSensorLinearization,'msanShMCSensorM':msanShMCSensorM,'msanShMCSensorTolerance':msanShMCSensorTolerance,'msanShMCSensorB':msanShMCSensorB,'msanShMCSensorAccuracy':msanShMCSensorAccuracy,'msanShMCSensorAccuracyExp':msanShMCSensorAccuracyExp,'msanShMCSensorRexp':msanShMCSensorRexp,'msanShMCSensorBexp':msanShMCSensorBexp,'msanShMCSensorCharacteristicFlags':msanShMCSensorCharacteristicFlags,'msanShMCSensorReading':msanShMCSensorReading,'msanShMCSensorProcessedReading':msanShMCSensorProcessedReading,'msanShMCSensorNominalReading':msanShMCSensorNominalReading,'msanShMCSensorNormalMaximum':msanShMCSensorNormalMaximum,'msanShMCSensorNormalMinimum':msanShMCSensorNormalMinimum,'msanShMCSensorMaximumReading':msanShMCSensorMaximumReading,'msanShMCSensorMinimumReading':msanShMCSensorMinimumReading,'msanShMCSensorUpperNonRecoverableThr':msanShMCSensorUpperNonRecoverableThr,'msanShMCSensorUpperCriticalThr':msanShMCSensorUpperCriticalThr,'msanShMCSensorUpperNonCriticalThr':msanShMCSensorUpperNonCriticalThr,'msanShMCSensorLowerNonRecoverableThr':msanShMCSensorLowerNonRecoverableThr,'msanShMCSensorLowerCriticalThr':msanShMCSensorLowerCriticalThr,'msanShMCSensorLowerNonCriticalThr':msanShMCSensorLowerNonCriticalThr,'msanShMCSensorPositiveGoingThrHysteresis':msanShMCSensorPositiveGoingThrHysteresis,'msanShMCSensorNegativeGoingThrHysteresis':msanShMCSensorNegativeGoingThrHysteresis,'msanShMCSensorIdString':msanShMCSensorIdString,'msanShMCSensorEntireSensorData':msanShMCSensorEntireSensorData,'msanShMCBoardsTable':msanShMCBoardsTable,'msanShMCBoardsEntry':msanShMCBoardsEntry,_S:msanShMCBoardsIndex,'msanShMCBoardsBoardBasicPresent':msanShMCBoardsBoardBasicPresent,'msanShMCBoardsBoardBasicHealthy':msanShMCBoardsBoardBasicHealthy,'msanShMCBoardsBoardBasicReset':msanShMCBoardsBoardBasicReset,'msanShMCBoardsBoardBasicSlaveAddress':msanShMCBoardsBoardBasicSlaveAddress,'msanShMCBoardsBoardBasicFruDeviceId':msanShMCBoardsBoardBasicFruDeviceId,'msanShMCSelTable':msanShMCSelTable,'msanShMCSelEntry':msanShMCSelEntry,_T:msanShMCSelIndex,'msanShMCSelcontents':msanShMCSelcontents,'msanShMCShelfTable':msanShMCShelfTable,'msanShMCShelfEntry':msanShMCShelfEntry,_U:msanShMCShelfIndex,'msanShMCShelfHealthy':msanShMCShelfHealthy,'msanShMCPefConfiguration':msanShMCPefConfiguration,'msanShMCPefConfigurationSetInProgress':msanShMCPefConfigurationSetInProgress,'msanShMCPefConfigurationControl':msanShMCPefConfigurationControl,'msanShMCPefConfigurationActionGlobalControl':msanShMCPefConfigurationActionGlobalControl,'msanShMCPefConfigurationStartupDelay':msanShMCPefConfigurationStartupDelay,'msanShMCPefConfigurationAlertStartupDelay':msanShMCPefConfigurationAlertStartupDelay,'msanShMCPefConfigurationNumberOfEventFilters':msanShMCPefConfigurationNumberOfEventFilters,'msanShMCPefConfigurationNumberOfAlertPoliciEntries':msanShMCPefConfigurationNumberOfAlertPoliciEntries,'msanShMCPefConfigurationSystemGuid':msanShMCPefConfigurationSystemGuid,'msanShMCPefConfigurationNumberOfAlertStrings':msanShMCPefConfigurationNumberOfAlertStrings,'msanShMCPefConfigurationEventFilterTable':msanShMCPefConfigurationEventFilterTable,'msanShMCPefConfigurationEventFilterEntry':msanShMCPefConfigurationEventFilterEntry,_V:msanShMCPefConfigurationEventFilterIndex,'msanShMCPefConfigurationEventFilterData':msanShMCPefConfigurationEventFilterData,'msanShMCPefConfigurationAlertStringTable':msanShMCPefConfigurationAlertStringTable,'msanShMCPefConfigurationAlertStringEntry':msanShMCPefConfigurationAlertStringEntry,_W:msanShMCPefConfigurationAlertStringIndex,'msanShMCPefConfigurationAlertStringKey':msanShMCPefConfigurationAlertStringKey,'msanShMCPefConfigurationAlertString':msanShMCPefConfigurationAlertString,'msanShMCFruInfoTable':msanShMCFruInfoTable,'msanShMCFruInfoEntry':msanShMCFruInfoEntry,_X:msanShMCFruInfoIndex,'msanShMCFruInfoData':msanShMCFruInfoData,'msanShMCFruInfoDataWo':msanShMCFruInfoDataWo,'msanShMCBoardVariablesTable':msanShMCBoardVariablesTable,'msanShMCBoardVariablesEntry':msanShMCBoardVariablesEntry,_Y:msanShMCBoardVariablesBoardBasicSlotNumber,'msanShMCBoardVariablesBoardBasicPresent':msanShMCBoardVariablesBoardBasicPresent,'msanShMCBoardVariablesBoardBasicHealthy':msanShMCBoardVariablesBoardBasicHealthy,'msanShMCBoardVariablesBoardBasicReset':msanShMCBoardVariablesBoardBasicReset,'msanShMCBoardVariablesBoardBasicPowered':msanShMCBoardVariablesBoardBasicPowered,'msanShMCBoardVariablesBoardBasicSlaveAddress':msanShMCBoardVariablesBoardBasicSlaveAddress,'msanShMCBoardVariablesBoardBasicFruDeviceId':msanShMCBoardVariablesBoardBasicFruDeviceId,'msanShMCBoardVariablesBoardBasicFruinfoProductAreaPresent':msanShMCBoardVariablesBoardBasicFruinfoProductAreaPresent,'msanShMCBoardVariablesBoardBasicProductManufacturer':msanShMCBoardVariablesBoardBasicProductManufacturer,'msanShMCBoardVariablesBoardBasicProductName':msanShMCBoardVariablesBoardBasicProductName,'msanShMCBoardVariablesBoardBasicProductPartModelNumber':msanShMCBoardVariablesBoardBasicProductPartModelNumber,'msanShMCBoardVariablesBoardBasicProductVersionNumber':msanShMCBoardVariablesBoardBasicProductVersionNumber,'msanShMCBoardVariablesBoardBasicProductSerialNumber':msanShMCBoardVariablesBoardBasicProductSerialNumber,'msanShMCBoardVariablesBoardBasicBoardAreaPresent':msanShMCBoardVariablesBoardBasicBoardAreaPresent,'msanShMCBoardVariablesBoardBasicBoardManufacturer':msanShMCBoardVariablesBoardBasicBoardManufacturer,'msanShMCBoardVariablesBoardBasicBoardProductName':msanShMCBoardVariablesBoardBasicBoardProductName,'msanShMCBoardVariablesBoardBasicBoardSerialNumber':msanShMCBoardVariablesBoardBasicBoardSerialNumber,'msanShMCBoardVariablesBoardBasicBoardPartNumber':msanShMCBoardVariablesBoardBasicBoardPartNumber,'msanShMCBoardVariablesBoardBasicBoardManufactureTime':msanShMCBoardVariablesBoardBasicBoardManufactureTime,'msanShMCBoardVariablesSelectivePowerOffSwitchOffType':msanShMCBoardVariablesSelectivePowerOffSwitchOffType,'msanShMCFanTrayVariablesTable':msanShMCFanTrayVariablesTable,'msanShMCFanTrayVariablesEntry':msanShMCFanTrayVariablesEntry,_Z:msanShMCFanTraySlotNumber,'msanShMCFanTrayPresent':msanShMCFanTrayPresent,'msanShMCFanTrayHealthy':msanShMCFanTrayHealthy,'msanShMCFanTrayHealthLed':msanShMCFanTrayHealthLed,'msanShMCFanTraySlaveAddress':msanShMCFanTraySlaveAddress,'msanShMCFanTrayFruDeviceId':msanShMCFanTrayFruDeviceId,'msanShMCFanTrayFruinfoProductAreaPresent':msanShMCFanTrayFruinfoProductAreaPresent,'msanShMCFanTrayFruinfoProductManufacturer':msanShMCFanTrayFruinfoProductManufacturer,'msanShMCFanTrayFruinfoProductName':msanShMCFanTrayFruinfoProductName,'msanShMCFanTrayFruinfoProductPartModelNumber':msanShMCFanTrayFruinfoProductPartModelNumber,'msanShMCFanTrayFruinfoProductVersionNumber':msanShMCFanTrayFruinfoProductVersionNumber,'msanShMCFanTrayFruinfoProductSerialNumber':msanShMCFanTrayFruinfoProductSerialNumber,'msanShMCFanTrayFruinfoBoardAreaPresent':msanShMCFanTrayFruinfoBoardAreaPresent,'msanShMCFanTrayFruinfoBoardManufacturer':msanShMCFanTrayFruinfoBoardManufacturer,'msanShMCFanTrayFruinfoBoardProductName':msanShMCFanTrayFruinfoBoardProductName,'msanShMCFanTrayFruinfoBoardSerialNumber':msanShMCFanTrayFruinfoBoardSerialNumber,'msanShMCFanTrayFruinfoBoardPartNumber':msanShMCFanTrayFruinfoBoardPartNumber,'msanShMCFanTrayFruinfoBoardManufactureTime':msanShMCFanTrayFruinfoBoardManufactureTime,'msanShMCPowerSupplyVariablesTable':msanShMCPowerSupplyVariablesTable,'msanShMCPowerSupplyVariablesEntry':msanShMCPowerSupplyVariablesEntry,_a:msanShMCPowerSupplySlotNumber,'msanShMCPowerSupplyDegrade':msanShMCPowerSupplyDegrade,'msanShMCPowerSupplyFail':msanShMCPowerSupplyFail,'msanShMCPowerSupplyInhibit':msanShMCPowerSupplyInhibit,'msanShMCPowerSupplyHealthy':msanShMCPowerSupplyHealthy,'msanShMCPowerSupplySlaveAddress':msanShMCPowerSupplySlaveAddress,'msanShMCPowerSupplyFruDeviceId':msanShMCPowerSupplyFruDeviceId,'msanShMCPowerSupplyFruinfoProductAreaPresent':msanShMCPowerSupplyFruinfoProductAreaPresent,'msanShMCPowerSupplyFruinfoProductManufacturer':msanShMCPowerSupplyFruinfoProductManufacturer,'msanShMCPowerSupplyFruinfoProductName':msanShMCPowerSupplyFruinfoProductName,'msanShMCPowerSupplyFruinfoProductPartModelNumber':msanShMCPowerSupplyFruinfoProductPartModelNumber,'msanShMCPowerSupplyFruinfoProductVersionNumber':msanShMCPowerSupplyFruinfoProductVersionNumber,'msanShMCPowerSupplyFruinfoProductSerialNumber':msanShMCPowerSupplyFruinfoProductSerialNumber,'msanShMCPowerSupplyFruinfoBoardAreaPresent':msanShMCPowerSupplyFruinfoBoardAreaPresent,'msanShMCPowerSupplyFruinfoBoardManufacturer':msanShMCPowerSupplyFruinfoBoardManufacturer,'msanShMCPowerSupplyFruinfoBoardProductName':msanShMCPowerSupplyFruinfoBoardProductName,'msanShMCPowerSupplyFruinfoBoardSerialNumber':msanShMCPowerSupplyFruinfoBoardSerialNumber,'msanShMCPowerSupplyFruinfoBoardPartNumber':msanShMCPowerSupplyFruinfoBoardPartNumber,'msanShMCPowerSupplyFruinfoBoardmanufactureTime':msanShMCPowerSupplyFruinfoBoardmanufactureTime,'msanShMCShelfManagerVariablesTable':msanShMCShelfManagerVariablesTable,'msanShMCShelfManagerVariablesEntry':msanShMCShelfManagerVariablesEntry,_b:msanShMCShelfManagerSlotNumber,'msanShMCShelfManagerSlaveAddress':msanShMCShelfManagerSlaveAddress,'msanShMCShelfManagerPresent':msanShMCShelfManagerPresent,'msanShMCShelfManagerHealthy':msanShMCShelfManagerHealthy,'msanShMCShelfManagerActive':msanShMCShelfManagerActive,'msanShMCShelfManagerReset':msanShMCShelfManagerReset,'msanShMCShelfManagerFruinfoProductAreaPresent':msanShMCShelfManagerFruinfoProductAreaPresent,'msanShMCShelfManagerFruinfoProductManufacturer':msanShMCShelfManagerFruinfoProductManufacturer,'msanShMCShelfManagerFruinfoProductName':msanShMCShelfManagerFruinfoProductName,'msanShMCShelfManagerFruinfoProductPartModelNumber':msanShMCShelfManagerFruinfoProductPartModelNumber,'msanShMCShelfManagerFruinfoProductVersionNumber':msanShMCShelfManagerFruinfoProductVersionNumber,'msanShMCShelfManagerFruinfoProductSerialNumber':msanShMCShelfManagerFruinfoProductSerialNumber,'msanShMCShelfManagerFruinfoBoardAreaPresent':msanShMCShelfManagerFruinfoBoardAreaPresent,'msanShMCShelfManagerFruinfoBoardManufacturer':msanShMCShelfManagerFruinfoBoardManufacturer,'msanShMCShelfManagerFruinfoBoardProductName':msanShMCShelfManagerFruinfoBoardProductName,'msanShMCShelfManagerFruinfoBoardSerialNumber':msanShMCShelfManagerFruinfoBoardSerialNumber,'msanShMCShelfManagerFruinfoBoardPartNumber':msanShMCShelfManagerFruinfoBoardPartNumber,'msanShMCShelfManagerFruinfoBoardmanufactureTime':msanShMCShelfManagerFruinfoBoardmanufactureTime,'msanShMCChassisVariablesTable':msanShMCChassisVariablesTable,'msanShMCChassisVariablesEntry':msanShMCChassisVariablesEntry,_c:msanShMCChassisId,'msanShMCChassisType':msanShMCChassisType,'msanShMCChassisPartNumber':msanShMCChassisPartNumber,'msanShMCChassisSerialNumber':msanShMCChassisSerialNumber,'msanShMCChassisProductAreaPresent':msanShMCChassisProductAreaPresent,'msanShMCChassisProductManufacturer':msanShMCChassisProductManufacturer,'msanShMCChassisProductName':msanShMCChassisProductName,'msanShMCChassisProductPartModelNumber':msanShMCChassisProductPartModelNumber,'msanShMCChassisProductVersionNumber':msanShMCChassisProductVersionNumber,'msanShMCChassisProductSerialNumber':msanShMCChassisProductSerialNumber,'msanShMCChassisBoardAreaPresent':msanShMCChassisBoardAreaPresent,'msanShMCChassisBoardManufacturer':msanShMCChassisBoardManufacturer,'msanShMCChassisBoardProductName':msanShMCChassisBoardProductName,'msanShMCChassisBoardSerialNumber':msanShMCChassisBoardSerialNumber,'msanShMCChassisBoardPartNumber':msanShMCChassisBoardPartNumber,'msanShMCChassisBoardmanufactureTime':msanShMCChassisBoardmanufactureTime,'msanShMCEventVariablesTable':msanShMCEventVariablesTable,'msanShMCEventVariablesEntry':msanShMCEventVariablesEntry,_d:msanShMCEventIndex,'msanShMCEventDelete':msanShMCEventDelete,'msanShMCEventTimeStamp':msanShMCEventTimeStamp,'msanShMCEventClass':msanShMCEventClass,'msanShMCEventType':msanShMCEventType,'msanShMCEventAsserted':msanShMCEventAsserted,'msanShMCEventOriginSiteType':msanShMCEventOriginSiteType,'msanShMCEventOriginSiteNumber':msanShMCEventOriginSiteNumber,'msanShMCEventOriginSlaveAddress':msanShMCEventOriginSlaveAddress,'msanShMCEventOriginFruId':msanShMCEventOriginFruId,'msanShMCEventOriginSensorNumber':msanShMCEventOriginSensorNumber,'msanShMCGlobal':msanShMCGlobal,'msanShMCSelectivePowerOffAdminMode':msanShMCSelectivePowerOffAdminMode,'msanSHMCSelectivePowerOffOffDelay':msanSHMCSelectivePowerOffOffDelay,'msanSHMCSelectivePowerOffOnDelay':msanSHMCSelectivePowerOffOnDelay})