_P='tsBitRateNormalDeviceName'
_O='tsIDRightDeviceName'
_N='tsIDErrorDeviceName'
_M='tsOverflowDeviceName'
_L='signalChangeDeviceName'
_K='signalOnDeviceName'
_J='signalOffDeviceName'
_I='fanFailedDeviceName'
_H='deviceOnDeviceName'
_G='deviceOffDeviceName'
_F='DisplayString'
_E='Integer32'
_D='PBI-MGSYSTEM-MIB'
_C='read-write'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
mg,=mibBuilder.importSymbols('PBI-MAIN-MIB','mg')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC',_F,'PhysAddress','RowStatus','TextualConvention','TruthValue')
mgSystem=ModuleIdentity((1,3,6,1,4,1,1070,3,1))
if mibBuilder.loadTexts:mgSystem.setRevisions(('2006-09-13 10:23',))
_BasicInfo_ObjectIdentity=ObjectIdentity
basicInfo=_BasicInfo_ObjectIdentity((1,3,6,1,4,1,1070,3,1,1))
class _UnitName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_UnitName_Type.__name__=_F
_UnitName_Object=MibScalar
unitName=_UnitName_Object((1,3,6,1,4,1,1070,3,1,1,1),_UnitName_Type())
unitName.setMaxAccess(_C)
if mibBuilder.loadTexts:unitName.setStatus(_A)
_SerialNumber_Type=DisplayString
_SerialNumber_Object=MibScalar
serialNumber=_SerialNumber_Object((1,3,6,1,4,1,1070,3,1,1,2),_SerialNumber_Type())
serialNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:serialNumber.setStatus(_A)
_FpgaVersion_Type=DisplayString
_FpgaVersion_Object=MibScalar
fpgaVersion=_FpgaVersion_Object((1,3,6,1,4,1,1070,3,1,1,3),_FpgaVersion_Type())
fpgaVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:fpgaVersion.setStatus(_A)
_McuVersion_Type=DisplayString
_McuVersion_Object=MibScalar
mcuVersion=_McuVersion_Object((1,3,6,1,4,1,1070,3,1,1,4),_McuVersion_Type())
mcuVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:mcuVersion.setStatus(_A)
class _MacAddress_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_MacAddress_Type.__name__=_F
_MacAddress_Object=MibScalar
macAddress=_MacAddress_Object((1,3,6,1,4,1,1070,3,1,1,5),_MacAddress_Type())
macAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:macAddress.setStatus(_A)
_Gateway_Type=IpAddress
_Gateway_Object=MibScalar
gateway=_Gateway_Object((1,3,6,1,4,1,1070,3,1,1,6),_Gateway_Type())
gateway.setMaxAccess(_C)
if mibBuilder.loadTexts:gateway.setStatus(_A)
_DeviceIP_Type=IpAddress
_DeviceIP_Object=MibScalar
deviceIP=_DeviceIP_Object((1,3,6,1,4,1,1070,3,1,1,7),_DeviceIP_Type())
deviceIP.setMaxAccess(_C)
if mibBuilder.loadTexts:deviceIP.setStatus(_A)
_SubnetMask_Type=IpAddress
_SubnetMask_Object=MibScalar
subnetMask=_SubnetMask_Object((1,3,6,1,4,1,1070,3,1,1,8),_SubnetMask_Type())
subnetMask.setMaxAccess(_C)
if mibBuilder.loadTexts:subnetMask.setStatus(_A)
_TrapIpAddress_Type=IpAddress
_TrapIpAddress_Object=MibScalar
trapIpAddress=_TrapIpAddress_Object((1,3,6,1,4,1,1070,3,1,1,9),_TrapIpAddress_Type())
trapIpAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:trapIpAddress.setStatus(_A)
class _Upgrade_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-2147483648,2147483647))
_Upgrade_Type.__name__=_E
_Upgrade_Object=MibScalar
upgrade=_Upgrade_Object((1,3,6,1,4,1,1070,3,1,1,10),_Upgrade_Type())
upgrade.setMaxAccess(_C)
if mibBuilder.loadTexts:upgrade.setStatus(_A)
_UpgradeIP_Type=IpAddress
_UpgradeIP_Object=MibScalar
upgradeIP=_UpgradeIP_Object((1,3,6,1,4,1,1070,3,1,1,11),_UpgradeIP_Type())
upgradeIP.setMaxAccess(_C)
if mibBuilder.loadTexts:upgradeIP.setStatus(_A)
class _Default_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-2147483648,2147483647))
_Default_Type.__name__=_E
_Default_Object=MibScalar
default=_Default_Object((1,3,6,1,4,1,1070,3,1,1,12),_Default_Type())
default.setMaxAccess(_C)
if mibBuilder.loadTexts:default.setStatus(_A)
_DeviceType_Type=Integer32
_DeviceType_Object=MibScalar
deviceType=_DeviceType_Object((1,3,6,1,4,1,1070,3,1,1,13),_DeviceType_Type())
deviceType.setMaxAccess(_C)
if mibBuilder.loadTexts:deviceType.setStatus(_A)
_HardwareVersion_Type=DisplayString
_HardwareVersion_Object=MibScalar
hardwareVersion=_HardwareVersion_Object((1,3,6,1,4,1,1070,3,1,1,14),_HardwareVersion_Type())
hardwareVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:hardwareVersion.setStatus(_A)
_ExterndBoard_Type=TruthValue
_ExterndBoard_Object=MibScalar
externdBoard=_ExterndBoard_Object((1,3,6,1,4,1,1070,3,1,1,15),_ExterndBoard_Type())
externdBoard.setMaxAccess(_C)
if mibBuilder.loadTexts:externdBoard.setStatus(_A)
_TrapDeviceOffTable_Object=MibTable
trapDeviceOffTable=_TrapDeviceOffTable_Object((1,3,6,1,4,1,1070,3,1,1,16))
if mibBuilder.loadTexts:trapDeviceOffTable.setStatus(_A)
_TrapDeviceOffEntry_Object=MibTableRow
trapDeviceOffEntry=_TrapDeviceOffEntry_Object((1,3,6,1,4,1,1070,3,1,1,16,1))
trapDeviceOffEntry.setIndexNames((0,_D,_G))
if mibBuilder.loadTexts:trapDeviceOffEntry.setStatus(_A)
_DeviceOffDeviceName_Type=DisplayString
_DeviceOffDeviceName_Object=MibTableColumn
deviceOffDeviceName=_DeviceOffDeviceName_Object((1,3,6,1,4,1,1070,3,1,1,16,1,1),_DeviceOffDeviceName_Type())
deviceOffDeviceName.setMaxAccess(_B)
if mibBuilder.loadTexts:deviceOffDeviceName.setStatus(_A)
_DeviceOffDeviceIP_Type=DisplayString
_DeviceOffDeviceIP_Object=MibTableColumn
deviceOffDeviceIP=_DeviceOffDeviceIP_Object((1,3,6,1,4,1,1070,3,1,1,16,1,2),_DeviceOffDeviceIP_Type())
deviceOffDeviceIP.setMaxAccess(_B)
if mibBuilder.loadTexts:deviceOffDeviceIP.setStatus(_A)
_DeviceOffReserve_Type=DisplayString
_DeviceOffReserve_Object=MibTableColumn
deviceOffReserve=_DeviceOffReserve_Object((1,3,6,1,4,1,1070,3,1,1,16,1,3),_DeviceOffReserve_Type())
deviceOffReserve.setMaxAccess(_B)
if mibBuilder.loadTexts:deviceOffReserve.setStatus(_A)
_DeviceOffLevel_Type=DisplayString
_DeviceOffLevel_Object=MibTableColumn
deviceOffLevel=_DeviceOffLevel_Object((1,3,6,1,4,1,1070,3,1,1,16,1,4),_DeviceOffLevel_Type())
deviceOffLevel.setMaxAccess(_B)
if mibBuilder.loadTexts:deviceOffLevel.setStatus(_A)
_DeviceOffTriggerTime_Type=DisplayString
_DeviceOffTriggerTime_Object=MibTableColumn
deviceOffTriggerTime=_DeviceOffTriggerTime_Object((1,3,6,1,4,1,1070,3,1,1,16,1,5),_DeviceOffTriggerTime_Type())
deviceOffTriggerTime.setMaxAccess(_B)
if mibBuilder.loadTexts:deviceOffTriggerTime.setStatus(_A)
_DeviceOffDescription_Type=DisplayString
_DeviceOffDescription_Object=MibTableColumn
deviceOffDescription=_DeviceOffDescription_Object((1,3,6,1,4,1,1070,3,1,1,16,1,6),_DeviceOffDescription_Type())
deviceOffDescription.setMaxAccess(_B)
if mibBuilder.loadTexts:deviceOffDescription.setStatus(_A)
_TrapDeviceOnTable_Object=MibTable
trapDeviceOnTable=_TrapDeviceOnTable_Object((1,3,6,1,4,1,1070,3,1,1,17))
if mibBuilder.loadTexts:trapDeviceOnTable.setStatus(_A)
_TrapDeviceOnEntry_Object=MibTableRow
trapDeviceOnEntry=_TrapDeviceOnEntry_Object((1,3,6,1,4,1,1070,3,1,1,17,1))
trapDeviceOnEntry.setIndexNames((0,_D,_H))
if mibBuilder.loadTexts:trapDeviceOnEntry.setStatus(_A)
_DeviceOnDeviceName_Type=DisplayString
_DeviceOnDeviceName_Object=MibTableColumn
deviceOnDeviceName=_DeviceOnDeviceName_Object((1,3,6,1,4,1,1070,3,1,1,17,1,1),_DeviceOnDeviceName_Type())
deviceOnDeviceName.setMaxAccess(_B)
if mibBuilder.loadTexts:deviceOnDeviceName.setStatus(_A)
_DeviceOnDeviceIP_Type=DisplayString
_DeviceOnDeviceIP_Object=MibTableColumn
deviceOnDeviceIP=_DeviceOnDeviceIP_Object((1,3,6,1,4,1,1070,3,1,1,17,1,2),_DeviceOnDeviceIP_Type())
deviceOnDeviceIP.setMaxAccess(_B)
if mibBuilder.loadTexts:deviceOnDeviceIP.setStatus(_A)
_DeviceOnReserve_Type=DisplayString
_DeviceOnReserve_Object=MibTableColumn
deviceOnReserve=_DeviceOnReserve_Object((1,3,6,1,4,1,1070,3,1,1,17,1,3),_DeviceOnReserve_Type())
deviceOnReserve.setMaxAccess(_B)
if mibBuilder.loadTexts:deviceOnReserve.setStatus(_A)
_DeviceOnLevel_Type=DisplayString
_DeviceOnLevel_Object=MibTableColumn
deviceOnLevel=_DeviceOnLevel_Object((1,3,6,1,4,1,1070,3,1,1,17,1,4),_DeviceOnLevel_Type())
deviceOnLevel.setMaxAccess(_B)
if mibBuilder.loadTexts:deviceOnLevel.setStatus(_A)
_DeviceOnTriggerTime_Type=DisplayString
_DeviceOnTriggerTime_Object=MibTableColumn
deviceOnTriggerTime=_DeviceOnTriggerTime_Object((1,3,6,1,4,1,1070,3,1,1,17,1,5),_DeviceOnTriggerTime_Type())
deviceOnTriggerTime.setMaxAccess(_B)
if mibBuilder.loadTexts:deviceOnTriggerTime.setStatus(_A)
_DeviceOnDescription_Type=DisplayString
_DeviceOnDescription_Object=MibTableColumn
deviceOnDescription=_DeviceOnDescription_Object((1,3,6,1,4,1,1070,3,1,1,17,1,6),_DeviceOnDescription_Type())
deviceOnDescription.setMaxAccess(_B)
if mibBuilder.loadTexts:deviceOnDescription.setStatus(_A)
_TrapFanFailedTable_Object=MibTable
trapFanFailedTable=_TrapFanFailedTable_Object((1,3,6,1,4,1,1070,3,1,1,18))
if mibBuilder.loadTexts:trapFanFailedTable.setStatus(_A)
_TrapFanFailedEntry_Object=MibTableRow
trapFanFailedEntry=_TrapFanFailedEntry_Object((1,3,6,1,4,1,1070,3,1,1,18,1))
trapFanFailedEntry.setIndexNames((0,_D,_I))
if mibBuilder.loadTexts:trapFanFailedEntry.setStatus(_A)
_FanFailedDeviceName_Type=DisplayString
_FanFailedDeviceName_Object=MibTableColumn
fanFailedDeviceName=_FanFailedDeviceName_Object((1,3,6,1,4,1,1070,3,1,1,18,1,1),_FanFailedDeviceName_Type())
fanFailedDeviceName.setMaxAccess(_B)
if mibBuilder.loadTexts:fanFailedDeviceName.setStatus(_A)
_FanFailedDeviceIP_Type=DisplayString
_FanFailedDeviceIP_Object=MibTableColumn
fanFailedDeviceIP=_FanFailedDeviceIP_Object((1,3,6,1,4,1,1070,3,1,1,18,1,2),_FanFailedDeviceIP_Type())
fanFailedDeviceIP.setMaxAccess(_B)
if mibBuilder.loadTexts:fanFailedDeviceIP.setStatus(_A)
_FanFailedReserve_Type=DisplayString
_FanFailedReserve_Object=MibTableColumn
fanFailedReserve=_FanFailedReserve_Object((1,3,6,1,4,1,1070,3,1,1,18,1,3),_FanFailedReserve_Type())
fanFailedReserve.setMaxAccess(_B)
if mibBuilder.loadTexts:fanFailedReserve.setStatus(_A)
_FanFailedLevel_Type=DisplayString
_FanFailedLevel_Object=MibTableColumn
fanFailedLevel=_FanFailedLevel_Object((1,3,6,1,4,1,1070,3,1,1,18,1,4),_FanFailedLevel_Type())
fanFailedLevel.setMaxAccess(_B)
if mibBuilder.loadTexts:fanFailedLevel.setStatus(_A)
_FanFailedTriggerTime_Type=DisplayString
_FanFailedTriggerTime_Object=MibTableColumn
fanFailedTriggerTime=_FanFailedTriggerTime_Object((1,3,6,1,4,1,1070,3,1,1,18,1,5),_FanFailedTriggerTime_Type())
fanFailedTriggerTime.setMaxAccess(_B)
if mibBuilder.loadTexts:fanFailedTriggerTime.setStatus(_A)
_FanFailedDescription_Type=DisplayString
_FanFailedDescription_Object=MibTableColumn
fanFailedDescription=_FanFailedDescription_Object((1,3,6,1,4,1,1070,3,1,1,18,1,6),_FanFailedDescription_Type())
fanFailedDescription.setMaxAccess(_B)
if mibBuilder.loadTexts:fanFailedDescription.setStatus(_A)
_TrapSignalOffTable_Object=MibTable
trapSignalOffTable=_TrapSignalOffTable_Object((1,3,6,1,4,1,1070,3,1,1,19))
if mibBuilder.loadTexts:trapSignalOffTable.setStatus(_A)
_TrapSignalOffEntry_Object=MibTableRow
trapSignalOffEntry=_TrapSignalOffEntry_Object((1,3,6,1,4,1,1070,3,1,1,19,1))
trapSignalOffEntry.setIndexNames((0,_D,_J))
if mibBuilder.loadTexts:trapSignalOffEntry.setStatus(_A)
_SignalOffDeviceName_Type=DisplayString
_SignalOffDeviceName_Object=MibTableColumn
signalOffDeviceName=_SignalOffDeviceName_Object((1,3,6,1,4,1,1070,3,1,1,19,1,1),_SignalOffDeviceName_Type())
signalOffDeviceName.setMaxAccess(_B)
if mibBuilder.loadTexts:signalOffDeviceName.setStatus(_A)
_SignalOffDeviceIP_Type=DisplayString
_SignalOffDeviceIP_Object=MibTableColumn
signalOffDeviceIP=_SignalOffDeviceIP_Object((1,3,6,1,4,1,1070,3,1,1,19,1,2),_SignalOffDeviceIP_Type())
signalOffDeviceIP.setMaxAccess(_B)
if mibBuilder.loadTexts:signalOffDeviceIP.setStatus(_A)
_SignalOffChannel_Type=DisplayString
_SignalOffChannel_Object=MibTableColumn
signalOffChannel=_SignalOffChannel_Object((1,3,6,1,4,1,1070,3,1,1,19,1,3),_SignalOffChannel_Type())
signalOffChannel.setMaxAccess(_B)
if mibBuilder.loadTexts:signalOffChannel.setStatus(_A)
_SignalOffLevel_Type=DisplayString
_SignalOffLevel_Object=MibTableColumn
signalOffLevel=_SignalOffLevel_Object((1,3,6,1,4,1,1070,3,1,1,19,1,4),_SignalOffLevel_Type())
signalOffLevel.setMaxAccess(_B)
if mibBuilder.loadTexts:signalOffLevel.setStatus(_A)
_SignalOffTriggerTime_Type=DisplayString
_SignalOffTriggerTime_Object=MibTableColumn
signalOffTriggerTime=_SignalOffTriggerTime_Object((1,3,6,1,4,1,1070,3,1,1,19,1,5),_SignalOffTriggerTime_Type())
signalOffTriggerTime.setMaxAccess(_B)
if mibBuilder.loadTexts:signalOffTriggerTime.setStatus(_A)
_SignalOffDescription_Type=DisplayString
_SignalOffDescription_Object=MibTableColumn
signalOffDescription=_SignalOffDescription_Object((1,3,6,1,4,1,1070,3,1,1,19,1,6),_SignalOffDescription_Type())
signalOffDescription.setMaxAccess(_B)
if mibBuilder.loadTexts:signalOffDescription.setStatus(_A)
_SignalOffSlot_Type=DisplayString
_SignalOffSlot_Object=MibTableColumn
signalOffSlot=_SignalOffSlot_Object((1,3,6,1,4,1,1070,3,1,1,19,1,7),_SignalOffSlot_Type())
signalOffSlot.setMaxAccess(_B)
if mibBuilder.loadTexts:signalOffSlot.setStatus(_A)
_TrapSignalOnTable_Object=MibTable
trapSignalOnTable=_TrapSignalOnTable_Object((1,3,6,1,4,1,1070,3,1,1,20))
if mibBuilder.loadTexts:trapSignalOnTable.setStatus(_A)
_TrapSignalOnEntry_Object=MibTableRow
trapSignalOnEntry=_TrapSignalOnEntry_Object((1,3,6,1,4,1,1070,3,1,1,20,1))
trapSignalOnEntry.setIndexNames((0,_D,_K))
if mibBuilder.loadTexts:trapSignalOnEntry.setStatus(_A)
_SignalOnDeviceName_Type=DisplayString
_SignalOnDeviceName_Object=MibTableColumn
signalOnDeviceName=_SignalOnDeviceName_Object((1,3,6,1,4,1,1070,3,1,1,20,1,1),_SignalOnDeviceName_Type())
signalOnDeviceName.setMaxAccess(_B)
if mibBuilder.loadTexts:signalOnDeviceName.setStatus(_A)
_SignalOnDeviceIP_Type=DisplayString
_SignalOnDeviceIP_Object=MibTableColumn
signalOnDeviceIP=_SignalOnDeviceIP_Object((1,3,6,1,4,1,1070,3,1,1,20,1,2),_SignalOnDeviceIP_Type())
signalOnDeviceIP.setMaxAccess(_B)
if mibBuilder.loadTexts:signalOnDeviceIP.setStatus(_A)
_SignalOnChannel_Type=DisplayString
_SignalOnChannel_Object=MibTableColumn
signalOnChannel=_SignalOnChannel_Object((1,3,6,1,4,1,1070,3,1,1,20,1,3),_SignalOnChannel_Type())
signalOnChannel.setMaxAccess(_B)
if mibBuilder.loadTexts:signalOnChannel.setStatus(_A)
_SignalOnLevel_Type=DisplayString
_SignalOnLevel_Object=MibTableColumn
signalOnLevel=_SignalOnLevel_Object((1,3,6,1,4,1,1070,3,1,1,20,1,4),_SignalOnLevel_Type())
signalOnLevel.setMaxAccess(_B)
if mibBuilder.loadTexts:signalOnLevel.setStatus(_A)
_SignalOnTriggerTime_Type=DisplayString
_SignalOnTriggerTime_Object=MibTableColumn
signalOnTriggerTime=_SignalOnTriggerTime_Object((1,3,6,1,4,1,1070,3,1,1,20,1,5),_SignalOnTriggerTime_Type())
signalOnTriggerTime.setMaxAccess(_B)
if mibBuilder.loadTexts:signalOnTriggerTime.setStatus(_A)
_SignalOnDescription_Type=DisplayString
_SignalOnDescription_Object=MibTableColumn
signalOnDescription=_SignalOnDescription_Object((1,3,6,1,4,1,1070,3,1,1,20,1,6),_SignalOnDescription_Type())
signalOnDescription.setMaxAccess(_B)
if mibBuilder.loadTexts:signalOnDescription.setStatus(_A)
_SignalOnSlot_Type=DisplayString
_SignalOnSlot_Object=MibTableColumn
signalOnSlot=_SignalOnSlot_Object((1,3,6,1,4,1,1070,3,1,1,20,1,7),_SignalOnSlot_Type())
signalOnSlot.setMaxAccess(_B)
if mibBuilder.loadTexts:signalOnSlot.setStatus(_A)
_TrapSignalChangeTable_Object=MibTable
trapSignalChangeTable=_TrapSignalChangeTable_Object((1,3,6,1,4,1,1070,3,1,1,21))
if mibBuilder.loadTexts:trapSignalChangeTable.setStatus(_A)
_TrapSignalChangeEntry_Object=MibTableRow
trapSignalChangeEntry=_TrapSignalChangeEntry_Object((1,3,6,1,4,1,1070,3,1,1,21,1))
trapSignalChangeEntry.setIndexNames((0,_D,_L))
if mibBuilder.loadTexts:trapSignalChangeEntry.setStatus(_A)
_SignalChangeDeviceName_Type=DisplayString
_SignalChangeDeviceName_Object=MibTableColumn
signalChangeDeviceName=_SignalChangeDeviceName_Object((1,3,6,1,4,1,1070,3,1,1,21,1,1),_SignalChangeDeviceName_Type())
signalChangeDeviceName.setMaxAccess(_B)
if mibBuilder.loadTexts:signalChangeDeviceName.setStatus(_A)
_SignalChangeDeviceIP_Type=DisplayString
_SignalChangeDeviceIP_Object=MibTableColumn
signalChangeDeviceIP=_SignalChangeDeviceIP_Object((1,3,6,1,4,1,1070,3,1,1,21,1,2),_SignalChangeDeviceIP_Type())
signalChangeDeviceIP.setMaxAccess(_B)
if mibBuilder.loadTexts:signalChangeDeviceIP.setStatus(_A)
_SignalChangeChannel_Type=DisplayString
_SignalChangeChannel_Object=MibTableColumn
signalChangeChannel=_SignalChangeChannel_Object((1,3,6,1,4,1,1070,3,1,1,21,1,3),_SignalChangeChannel_Type())
signalChangeChannel.setMaxAccess(_B)
if mibBuilder.loadTexts:signalChangeChannel.setStatus(_A)
_SignalChangeLevel_Type=DisplayString
_SignalChangeLevel_Object=MibTableColumn
signalChangeLevel=_SignalChangeLevel_Object((1,3,6,1,4,1,1070,3,1,1,21,1,4),_SignalChangeLevel_Type())
signalChangeLevel.setMaxAccess(_B)
if mibBuilder.loadTexts:signalChangeLevel.setStatus(_A)
_SignalChangeTriggerTime_Type=DisplayString
_SignalChangeTriggerTime_Object=MibTableColumn
signalChangeTriggerTime=_SignalChangeTriggerTime_Object((1,3,6,1,4,1,1070,3,1,1,21,1,5),_SignalChangeTriggerTime_Type())
signalChangeTriggerTime.setMaxAccess(_B)
if mibBuilder.loadTexts:signalChangeTriggerTime.setStatus(_A)
_SignalChangeDescription_Type=DisplayString
_SignalChangeDescription_Object=MibTableColumn
signalChangeDescription=_SignalChangeDescription_Object((1,3,6,1,4,1,1070,3,1,1,21,1,6),_SignalChangeDescription_Type())
signalChangeDescription.setMaxAccess(_B)
if mibBuilder.loadTexts:signalChangeDescription.setStatus(_A)
_SignalChangeSlot_Type=DisplayString
_SignalChangeSlot_Object=MibTableColumn
signalChangeSlot=_SignalChangeSlot_Object((1,3,6,1,4,1,1070,3,1,1,21,1,7),_SignalChangeSlot_Type())
signalChangeSlot.setMaxAccess(_B)
if mibBuilder.loadTexts:signalChangeSlot.setStatus(_A)
_TrapTSOverflowTable_Object=MibTable
trapTSOverflowTable=_TrapTSOverflowTable_Object((1,3,6,1,4,1,1070,3,1,1,22))
if mibBuilder.loadTexts:trapTSOverflowTable.setStatus(_A)
_TrapTSOverflowEntry_Object=MibTableRow
trapTSOverflowEntry=_TrapTSOverflowEntry_Object((1,3,6,1,4,1,1070,3,1,1,22,1))
trapTSOverflowEntry.setIndexNames((0,_D,_M))
if mibBuilder.loadTexts:trapTSOverflowEntry.setStatus(_A)
_TsOverflowDeviceName_Type=DisplayString
_TsOverflowDeviceName_Object=MibTableColumn
tsOverflowDeviceName=_TsOverflowDeviceName_Object((1,3,6,1,4,1,1070,3,1,1,22,1,1),_TsOverflowDeviceName_Type())
tsOverflowDeviceName.setMaxAccess(_B)
if mibBuilder.loadTexts:tsOverflowDeviceName.setStatus(_A)
_TsOverflowDeviceIP_Type=DisplayString
_TsOverflowDeviceIP_Object=MibTableColumn
tsOverflowDeviceIP=_TsOverflowDeviceIP_Object((1,3,6,1,4,1,1070,3,1,1,22,1,2),_TsOverflowDeviceIP_Type())
tsOverflowDeviceIP.setMaxAccess(_B)
if mibBuilder.loadTexts:tsOverflowDeviceIP.setStatus(_A)
_TsOverflowChannel_Type=DisplayString
_TsOverflowChannel_Object=MibTableColumn
tsOverflowChannel=_TsOverflowChannel_Object((1,3,6,1,4,1,1070,3,1,1,22,1,3),_TsOverflowChannel_Type())
tsOverflowChannel.setMaxAccess(_B)
if mibBuilder.loadTexts:tsOverflowChannel.setStatus(_A)
_TsOverflowLevel_Type=DisplayString
_TsOverflowLevel_Object=MibTableColumn
tsOverflowLevel=_TsOverflowLevel_Object((1,3,6,1,4,1,1070,3,1,1,22,1,4),_TsOverflowLevel_Type())
tsOverflowLevel.setMaxAccess(_B)
if mibBuilder.loadTexts:tsOverflowLevel.setStatus(_A)
_TsOverflowTriggerTime_Type=DisplayString
_TsOverflowTriggerTime_Object=MibTableColumn
tsOverflowTriggerTime=_TsOverflowTriggerTime_Object((1,3,6,1,4,1,1070,3,1,1,22,1,5),_TsOverflowTriggerTime_Type())
tsOverflowTriggerTime.setMaxAccess(_B)
if mibBuilder.loadTexts:tsOverflowTriggerTime.setStatus(_A)
_TsOverflowDescription_Type=DisplayString
_TsOverflowDescription_Object=MibTableColumn
tsOverflowDescription=_TsOverflowDescription_Object((1,3,6,1,4,1,1070,3,1,1,22,1,6),_TsOverflowDescription_Type())
tsOverflowDescription.setMaxAccess(_B)
if mibBuilder.loadTexts:tsOverflowDescription.setStatus(_A)
_TsOverflowSlot_Type=DisplayString
_TsOverflowSlot_Object=MibTableColumn
tsOverflowSlot=_TsOverflowSlot_Object((1,3,6,1,4,1,1070,3,1,1,22,1,7),_TsOverflowSlot_Type())
tsOverflowSlot.setMaxAccess(_B)
if mibBuilder.loadTexts:tsOverflowSlot.setStatus(_A)
_RebootCommand_Type=Integer32
_RebootCommand_Object=MibScalar
rebootCommand=_RebootCommand_Object((1,3,6,1,4,1,1070,3,1,1,23),_RebootCommand_Type())
rebootCommand.setMaxAccess(_C)
if mibBuilder.loadTexts:rebootCommand.setStatus(_A)
_TrapTSIDErrorTable_Object=MibTable
trapTSIDErrorTable=_TrapTSIDErrorTable_Object((1,3,6,1,4,1,1070,3,1,1,24))
if mibBuilder.loadTexts:trapTSIDErrorTable.setStatus(_A)
_TrapTSIDErrorEntry_Object=MibTableRow
trapTSIDErrorEntry=_TrapTSIDErrorEntry_Object((1,3,6,1,4,1,1070,3,1,1,24,1))
trapTSIDErrorEntry.setIndexNames((0,_D,_N))
if mibBuilder.loadTexts:trapTSIDErrorEntry.setStatus(_A)
_TsIDErrorDeviceName_Type=DisplayString
_TsIDErrorDeviceName_Object=MibTableColumn
tsIDErrorDeviceName=_TsIDErrorDeviceName_Object((1,3,6,1,4,1,1070,3,1,1,24,1,1),_TsIDErrorDeviceName_Type())
tsIDErrorDeviceName.setMaxAccess(_B)
if mibBuilder.loadTexts:tsIDErrorDeviceName.setStatus(_A)
_TsIDErrorDeviceIP_Type=DisplayString
_TsIDErrorDeviceIP_Object=MibTableColumn
tsIDErrorDeviceIP=_TsIDErrorDeviceIP_Object((1,3,6,1,4,1,1070,3,1,1,24,1,2),_TsIDErrorDeviceIP_Type())
tsIDErrorDeviceIP.setMaxAccess(_B)
if mibBuilder.loadTexts:tsIDErrorDeviceIP.setStatus(_A)
_TsIDErrorTsID_Type=DisplayString
_TsIDErrorTsID_Object=MibTableColumn
tsIDErrorTsID=_TsIDErrorTsID_Object((1,3,6,1,4,1,1070,3,1,1,24,1,3),_TsIDErrorTsID_Type())
tsIDErrorTsID.setMaxAccess(_B)
if mibBuilder.loadTexts:tsIDErrorTsID.setStatus(_A)
_TsIDErrorLevel_Type=DisplayString
_TsIDErrorLevel_Object=MibTableColumn
tsIDErrorLevel=_TsIDErrorLevel_Object((1,3,6,1,4,1,1070,3,1,1,24,1,4),_TsIDErrorLevel_Type())
tsIDErrorLevel.setMaxAccess(_B)
if mibBuilder.loadTexts:tsIDErrorLevel.setStatus(_A)
_TsIDErrorTriggerTime_Type=DisplayString
_TsIDErrorTriggerTime_Object=MibTableColumn
tsIDErrorTriggerTime=_TsIDErrorTriggerTime_Object((1,3,6,1,4,1,1070,3,1,1,24,1,5),_TsIDErrorTriggerTime_Type())
tsIDErrorTriggerTime.setMaxAccess(_B)
if mibBuilder.loadTexts:tsIDErrorTriggerTime.setStatus(_A)
_TsIDErrorDescription_Type=DisplayString
_TsIDErrorDescription_Object=MibTableColumn
tsIDErrorDescription=_TsIDErrorDescription_Object((1,3,6,1,4,1,1070,3,1,1,24,1,6),_TsIDErrorDescription_Type())
tsIDErrorDescription.setMaxAccess(_B)
if mibBuilder.loadTexts:tsIDErrorDescription.setStatus(_A)
_TsIDErrorSlot_Type=DisplayString
_TsIDErrorSlot_Object=MibTableColumn
tsIDErrorSlot=_TsIDErrorSlot_Object((1,3,6,1,4,1,1070,3,1,1,24,1,7),_TsIDErrorSlot_Type())
tsIDErrorSlot.setMaxAccess(_B)
if mibBuilder.loadTexts:tsIDErrorSlot.setStatus(_A)
_TrapTSIDRightTable_Object=MibTable
trapTSIDRightTable=_TrapTSIDRightTable_Object((1,3,6,1,4,1,1070,3,1,1,25))
if mibBuilder.loadTexts:trapTSIDRightTable.setStatus(_A)
_TrapTSIDRightEntry_Object=MibTableRow
trapTSIDRightEntry=_TrapTSIDRightEntry_Object((1,3,6,1,4,1,1070,3,1,1,25,1))
trapTSIDRightEntry.setIndexNames((0,_D,_O))
if mibBuilder.loadTexts:trapTSIDRightEntry.setStatus(_A)
_TsIDRightDeviceName_Type=DisplayString
_TsIDRightDeviceName_Object=MibTableColumn
tsIDRightDeviceName=_TsIDRightDeviceName_Object((1,3,6,1,4,1,1070,3,1,1,25,1,1),_TsIDRightDeviceName_Type())
tsIDRightDeviceName.setMaxAccess(_B)
if mibBuilder.loadTexts:tsIDRightDeviceName.setStatus(_A)
_TsIDRightDeviceIP_Type=DisplayString
_TsIDRightDeviceIP_Object=MibTableColumn
tsIDRightDeviceIP=_TsIDRightDeviceIP_Object((1,3,6,1,4,1,1070,3,1,1,25,1,2),_TsIDRightDeviceIP_Type())
tsIDRightDeviceIP.setMaxAccess(_B)
if mibBuilder.loadTexts:tsIDRightDeviceIP.setStatus(_A)
_TsIDRightTSID_Type=DisplayString
_TsIDRightTSID_Object=MibTableColumn
tsIDRightTSID=_TsIDRightTSID_Object((1,3,6,1,4,1,1070,3,1,1,25,1,3),_TsIDRightTSID_Type())
tsIDRightTSID.setMaxAccess(_B)
if mibBuilder.loadTexts:tsIDRightTSID.setStatus(_A)
_TsIDRightLevel_Type=DisplayString
_TsIDRightLevel_Object=MibTableColumn
tsIDRightLevel=_TsIDRightLevel_Object((1,3,6,1,4,1,1070,3,1,1,25,1,4),_TsIDRightLevel_Type())
tsIDRightLevel.setMaxAccess(_B)
if mibBuilder.loadTexts:tsIDRightLevel.setStatus(_A)
_TsIDRightTriggerTime_Type=DisplayString
_TsIDRightTriggerTime_Object=MibTableColumn
tsIDRightTriggerTime=_TsIDRightTriggerTime_Object((1,3,6,1,4,1,1070,3,1,1,25,1,5),_TsIDRightTriggerTime_Type())
tsIDRightTriggerTime.setMaxAccess(_B)
if mibBuilder.loadTexts:tsIDRightTriggerTime.setStatus(_A)
_TsIDRightDescription_Type=DisplayString
_TsIDRightDescription_Object=MibTableColumn
tsIDRightDescription=_TsIDRightDescription_Object((1,3,6,1,4,1,1070,3,1,1,25,1,6),_TsIDRightDescription_Type())
tsIDRightDescription.setMaxAccess(_B)
if mibBuilder.loadTexts:tsIDRightDescription.setStatus(_A)
_TsIDRightSlot_Type=DisplayString
_TsIDRightSlot_Object=MibTableColumn
tsIDRightSlot=_TsIDRightSlot_Object((1,3,6,1,4,1,1070,3,1,1,25,1,7),_TsIDRightSlot_Type())
tsIDRightSlot.setMaxAccess(_B)
if mibBuilder.loadTexts:tsIDRightSlot.setStatus(_A)
_TrapTSBitRateNormalTable_Object=MibTable
trapTSBitRateNormalTable=_TrapTSBitRateNormalTable_Object((1,3,6,1,4,1,1070,3,1,1,26))
if mibBuilder.loadTexts:trapTSBitRateNormalTable.setStatus(_A)
_TrapTSBitRateNormalEntry_Object=MibTableRow
trapTSBitRateNormalEntry=_TrapTSBitRateNormalEntry_Object((1,3,6,1,4,1,1070,3,1,1,26,1))
trapTSBitRateNormalEntry.setIndexNames((0,_D,_P))
if mibBuilder.loadTexts:trapTSBitRateNormalEntry.setStatus(_A)
_TsBitRateNormalDeviceName_Type=DisplayString
_TsBitRateNormalDeviceName_Object=MibTableColumn
tsBitRateNormalDeviceName=_TsBitRateNormalDeviceName_Object((1,3,6,1,4,1,1070,3,1,1,26,1,1),_TsBitRateNormalDeviceName_Type())
tsBitRateNormalDeviceName.setMaxAccess(_B)
if mibBuilder.loadTexts:tsBitRateNormalDeviceName.setStatus(_A)
_TsBitRateNormalDeviceIP_Type=DisplayString
_TsBitRateNormalDeviceIP_Object=MibTableColumn
tsBitRateNormalDeviceIP=_TsBitRateNormalDeviceIP_Object((1,3,6,1,4,1,1070,3,1,1,26,1,2),_TsBitRateNormalDeviceIP_Type())
tsBitRateNormalDeviceIP.setMaxAccess(_B)
if mibBuilder.loadTexts:tsBitRateNormalDeviceIP.setStatus(_A)
_TsBitRateNormalChannel_Type=DisplayString
_TsBitRateNormalChannel_Object=MibTableColumn
tsBitRateNormalChannel=_TsBitRateNormalChannel_Object((1,3,6,1,4,1,1070,3,1,1,26,1,3),_TsBitRateNormalChannel_Type())
tsBitRateNormalChannel.setMaxAccess(_B)
if mibBuilder.loadTexts:tsBitRateNormalChannel.setStatus(_A)
_TsBitRateNormalLevel_Type=DisplayString
_TsBitRateNormalLevel_Object=MibTableColumn
tsBitRateNormalLevel=_TsBitRateNormalLevel_Object((1,3,6,1,4,1,1070,3,1,1,26,1,4),_TsBitRateNormalLevel_Type())
tsBitRateNormalLevel.setMaxAccess(_B)
if mibBuilder.loadTexts:tsBitRateNormalLevel.setStatus(_A)
_TsBitRateNormalTriggerTime_Type=DisplayString
_TsBitRateNormalTriggerTime_Object=MibTableColumn
tsBitRateNormalTriggerTime=_TsBitRateNormalTriggerTime_Object((1,3,6,1,4,1,1070,3,1,1,26,1,5),_TsBitRateNormalTriggerTime_Type())
tsBitRateNormalTriggerTime.setMaxAccess(_B)
if mibBuilder.loadTexts:tsBitRateNormalTriggerTime.setStatus(_A)
_TsBitRateNormalDescription_Type=DisplayString
_TsBitRateNormalDescription_Object=MibTableColumn
tsBitRateNormalDescription=_TsBitRateNormalDescription_Object((1,3,6,1,4,1,1070,3,1,1,26,1,6),_TsBitRateNormalDescription_Type())
tsBitRateNormalDescription.setMaxAccess(_B)
if mibBuilder.loadTexts:tsBitRateNormalDescription.setStatus(_A)
_TsBitRateNormalSlot_Type=DisplayString
_TsBitRateNormalSlot_Object=MibTableColumn
tsBitRateNormalSlot=_TsBitRateNormalSlot_Object((1,3,6,1,4,1,1070,3,1,1,26,1,7),_TsBitRateNormalSlot_Type())
tsBitRateNormalSlot.setMaxAccess(_B)
if mibBuilder.loadTexts:tsBitRateNormalSlot.setStatus(_A)
_VirtualGroupInfo_Type=DisplayString
_VirtualGroupInfo_Object=MibScalar
virtualGroupInfo=_VirtualGroupInfo_Object((1,3,6,1,4,1,1070,3,1,1,27),_VirtualGroupInfo_Type())
virtualGroupInfo.setMaxAccess(_C)
if mibBuilder.loadTexts:virtualGroupInfo.setStatus(_A)
_ModuleNumber_Type=Integer32
_ModuleNumber_Object=MibScalar
moduleNumber=_ModuleNumber_Object((1,3,6,1,4,1,1070,3,1,1,28),_ModuleNumber_Type())
moduleNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:moduleNumber.setStatus(_A)
_ChestTemp_Type=Integer32
_ChestTemp_Object=MibScalar
chestTemp=_ChestTemp_Object((1,3,6,1,4,1,1070,3,1,1,29),_ChestTemp_Type())
chestTemp.setMaxAccess(_B)
if mibBuilder.loadTexts:chestTemp.setStatus(_A)
class _LcdSwitch_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('alwaysOn',0),('time',1)))
_LcdSwitch_Type.__name__=_E
_LcdSwitch_Object=MibScalar
lcdSwitch=_LcdSwitch_Object((1,3,6,1,4,1,1070,3,1,1,35),_LcdSwitch_Type())
lcdSwitch.setMaxAccess(_C)
if mibBuilder.loadTexts:lcdSwitch.setStatus(_A)
mibBuilder.exportSymbols(_D,**{'mgSystem':mgSystem,'basicInfo':basicInfo,'unitName':unitName,'serialNumber':serialNumber,'fpgaVersion':fpgaVersion,'mcuVersion':mcuVersion,'macAddress':macAddress,'gateway':gateway,'deviceIP':deviceIP,'subnetMask':subnetMask,'trapIpAddress':trapIpAddress,'upgrade':upgrade,'upgradeIP':upgradeIP,'default':default,'deviceType':deviceType,'hardwareVersion':hardwareVersion,'externdBoard':externdBoard,'trapDeviceOffTable':trapDeviceOffTable,'trapDeviceOffEntry':trapDeviceOffEntry,_G:deviceOffDeviceName,'deviceOffDeviceIP':deviceOffDeviceIP,'deviceOffReserve':deviceOffReserve,'deviceOffLevel':deviceOffLevel,'deviceOffTriggerTime':deviceOffTriggerTime,'deviceOffDescription':deviceOffDescription,'trapDeviceOnTable':trapDeviceOnTable,'trapDeviceOnEntry':trapDeviceOnEntry,_H:deviceOnDeviceName,'deviceOnDeviceIP':deviceOnDeviceIP,'deviceOnReserve':deviceOnReserve,'deviceOnLevel':deviceOnLevel,'deviceOnTriggerTime':deviceOnTriggerTime,'deviceOnDescription':deviceOnDescription,'trapFanFailedTable':trapFanFailedTable,'trapFanFailedEntry':trapFanFailedEntry,_I:fanFailedDeviceName,'fanFailedDeviceIP':fanFailedDeviceIP,'fanFailedReserve':fanFailedReserve,'fanFailedLevel':fanFailedLevel,'fanFailedTriggerTime':fanFailedTriggerTime,'fanFailedDescription':fanFailedDescription,'trapSignalOffTable':trapSignalOffTable,'trapSignalOffEntry':trapSignalOffEntry,_J:signalOffDeviceName,'signalOffDeviceIP':signalOffDeviceIP,'signalOffChannel':signalOffChannel,'signalOffLevel':signalOffLevel,'signalOffTriggerTime':signalOffTriggerTime,'signalOffDescription':signalOffDescription,'signalOffSlot':signalOffSlot,'trapSignalOnTable':trapSignalOnTable,'trapSignalOnEntry':trapSignalOnEntry,_K:signalOnDeviceName,'signalOnDeviceIP':signalOnDeviceIP,'signalOnChannel':signalOnChannel,'signalOnLevel':signalOnLevel,'signalOnTriggerTime':signalOnTriggerTime,'signalOnDescription':signalOnDescription,'signalOnSlot':signalOnSlot,'trapSignalChangeTable':trapSignalChangeTable,'trapSignalChangeEntry':trapSignalChangeEntry,_L:signalChangeDeviceName,'signalChangeDeviceIP':signalChangeDeviceIP,'signalChangeChannel':signalChangeChannel,'signalChangeLevel':signalChangeLevel,'signalChangeTriggerTime':signalChangeTriggerTime,'signalChangeDescription':signalChangeDescription,'signalChangeSlot':signalChangeSlot,'trapTSOverflowTable':trapTSOverflowTable,'trapTSOverflowEntry':trapTSOverflowEntry,_M:tsOverflowDeviceName,'tsOverflowDeviceIP':tsOverflowDeviceIP,'tsOverflowChannel':tsOverflowChannel,'tsOverflowLevel':tsOverflowLevel,'tsOverflowTriggerTime':tsOverflowTriggerTime,'tsOverflowDescription':tsOverflowDescription,'tsOverflowSlot':tsOverflowSlot,'rebootCommand':rebootCommand,'trapTSIDErrorTable':trapTSIDErrorTable,'trapTSIDErrorEntry':trapTSIDErrorEntry,_N:tsIDErrorDeviceName,'tsIDErrorDeviceIP':tsIDErrorDeviceIP,'tsIDErrorTsID':tsIDErrorTsID,'tsIDErrorLevel':tsIDErrorLevel,'tsIDErrorTriggerTime':tsIDErrorTriggerTime,'tsIDErrorDescription':tsIDErrorDescription,'tsIDErrorSlot':tsIDErrorSlot,'trapTSIDRightTable':trapTSIDRightTable,'trapTSIDRightEntry':trapTSIDRightEntry,_O:tsIDRightDeviceName,'tsIDRightDeviceIP':tsIDRightDeviceIP,'tsIDRightTSID':tsIDRightTSID,'tsIDRightLevel':tsIDRightLevel,'tsIDRightTriggerTime':tsIDRightTriggerTime,'tsIDRightDescription':tsIDRightDescription,'tsIDRightSlot':tsIDRightSlot,'trapTSBitRateNormalTable':trapTSBitRateNormalTable,'trapTSBitRateNormalEntry':trapTSBitRateNormalEntry,_P:tsBitRateNormalDeviceName,'tsBitRateNormalDeviceIP':tsBitRateNormalDeviceIP,'tsBitRateNormalChannel':tsBitRateNormalChannel,'tsBitRateNormalLevel':tsBitRateNormalLevel,'tsBitRateNormalTriggerTime':tsBitRateNormalTriggerTime,'tsBitRateNormalDescription':tsBitRateNormalDescription,'tsBitRateNormalSlot':tsBitRateNormalSlot,'virtualGroupInfo':virtualGroupInfo,'moduleNumber':moduleNumber,'chestTemp':chestTemp,'lcdSwitch':lcdSwitch})