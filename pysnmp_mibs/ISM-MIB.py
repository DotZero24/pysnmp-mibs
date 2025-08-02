_BZ='currentObjectGroup'
_BY='hwInfoCacheWhetherDirtyDataExists'
_BX='hwInfoCacheMirroringWriteCacheUtility'
_BW='hwInfoCacheWriteCacheUtililty'
_BV='hwInfoCacheReadCacheUtility'
_BU='hwInfoCacheCacheLowWaterLevel'
_BT='hwInfoCacheCacheHighWaterLevel'
_BS='hwInfoCacheCurrentCacheWaterLevel'
_BR='hwInfoCacheCacheHitRatio'
_BQ='hwInfoCacheCacheUtilization'
_BP='hwInfoCacheCacheCapacity'
_BO='hwInfoCacheSystemMemoryCapacity'
_BN='hwInfoCacheTotalMemoryCapacity'
_BM='hwPerfControllerMemoryUsage'
_BL='hwInfoNasControllerDescription'
_BK='hwInfoNasControllerFirmwareVersion'
_BJ='hwInfoNasControllerBarCode'
_BI='hwInfoClusterNodesIP'
_BH='hwInfoClusterNodesRuningStatus'
_BG='hwInfoClusterNodesStatus'
_BF='hwInfoClusterNodesIsMaster'
_BE='hwInfoClusterNodesName'
_BD='hwInfoFileSystemPoolList'
_BC='hwInfoFileSystemSecondaryTier'
_BB='hwInfoFileSystemCIFSShared'
_BA='hwInfoFileSystemNFSShared'
_B9='hwInfoFileSystemUsage'
_B8='hwInfoFileSystemColumns'
_B7='hwInfoFileSystemMirrors'
_B6='hwInfoFileSystemLayout'
_B5='hwInfoFileSystemSize'
_B4='hwInfoFileSystemStatus'
_B3='hwInfoInterfaceDescription'
_B2='hwInfoFanDescription'
_B1='hwInfoPowerDescription'
_B0='hwInfoControllerDescription'
_A_='hwPerfNASPortDescription'
_Az='hwInfoRAIDTotalSize'
_Ay='hwInfoFanELable'
_Ax='hwInfoPowerDisplayID'
_Aw='hwPerfControllerCPUUsage'
_Av='hwPerfControllerWriteThroughput'
_Au='hwPerfControllerWriteBandwidth'
_At='hwPerfControllerReadThroughput'
_As='hwPerfControllerReadBandwidth'
_Ar='hwPerfControllerThroughput'
_Aq='hwPerfControllerCacheHit'
_Ap='hwInfoInterfaceStatus'
_Ao='hwInfoInterfaceType'
_An='hwInfoBBUCurrentVoltage'
_Am='hwInfoBBUStatus'
_Al='hwInfoPowerType'
_Ak='hwInfoPowerVendor'
_Aj='hwInfoPowerStatus'
_Ai='hwInfoInterfaceVendorInfo'
_Ah='hwInfoInterfacePCBVersion'
_Ag='hwInfoInterfaceLogicVersion'
_Af='hwInfoExpBoardType'
_Ae='hwInfoExpBoardProduceInfo'
_Ad='hwInfoExpBoardPCBversion'
_Ac='hwInfoExpBoardLogicVersion'
_Ab='hwInfoExpBoardStatus'
_Aa='hwInfoBBUChargeState'
_AZ='hwInfoBBUELable'
_AY='hwInfoBBUFWVersion'
_AX='hwInfoBBURemainLife'
_AW='hwInfoBBUDischargeTime'
_AV='hwInfoBBUIsChargeFull'
_AU='hwInfoBBUPresentStatus'
_AT='hwInfoPowerSN'
_AS='hwInfoPowerDate'
_AR='hwInfoPowerVersion'
_AQ='hwInfoPowerModle'
_AP='hwInfoPowerTemperature'
_AO='hwInfoControllerStatus'
_AN='hwInfoControllerVersion'
_AM='hwInfoControllerMemoryUsingRatio'
_AL='hwInfoControllerCpuUsingRatio'
_AK='hwInfoControllerIsMaster'
_AJ='hwInfoControllerIP'
_AI='hwInfoFanRunningSection'
_AH='hwInfoFanRunningLevel'
_AG='hwInfoFanRunningStatus'
_AF='hwPerfRAIDWriteThroughput'
_AE='hwPerfRAIDWriteBandwidth'
_AD='hwPerfRAIDReadThroughput'
_AC='hwPerfRAIDReadBandwidth'
_AB='hwPerfRAIDThroughput'
_AA='hwPerfRAIDCurrentBandwidth'
_A9='hwInfoRAIDDiskList'
_A8='hwInfoRAIDStatus'
_A7='hwInfoRAIDFreeCapacity'
_A6='hwInfoRAIDLevel'
_A5='hwInfoRAIDName'
_A4='hwInfoLogicDiskSize'
_A3='hwInfoLogicDiskLogicType'
_A2='hwInfoLogicDiskLogicStatus'
_A1='hwInfoPhysicDiskRawCapacity'
_A0='hwInfoPhysicDiskCurrentSpeed'
_z='hwInfoPhysicDiskSpinSpeed'
_y='hwInfoPhysicDiskSZFirmware'
_x='hwInfoPhysicDiskSZSerial'
_w='hwInfoPhysicDiskSZModel'
_v='hwInfoPhysicDiskSZVendor'
_u='hwInfoPhysicDiskSZType'
_t='hwInfoPhysicDiskStatus'
_s='hwPerfNASPortOutboundPackages'
_r='hwPerfNASPortInboundPackages'
_q='hwPerfNASPortTotalPackages'
_p='hwPerfNASPortWriteBandwidth'
_o='hwPerfNASPortReadBandwidth'
_n='hwPerfNASPortCurrentBandwidth'
_m='hwInfoControllerBoardELabel'
_l='hwInfoControllerBoardBIOSVer'
_k='hwInfoControllerBoardPCBVer'
_j='hwInfoControllerBoardLogicVer'
_i='hwInfoControllerBoardStatus'
_h='hwInfoControllerBoardType'
_g='Degrees Celsius'
_f='hwInfoNasControllerName'
_e='hwInfoClusterNodesID'
_d='hwInfoFileSystemName'
_c='hwInfoControllerBoardID'
_b='Packets/s'
_a='hwPerfNASPortIndex'
_Z='hwPerfControllerID'
_Y='hwPerfRAIDID'
_X='hwInfoCacheID'
_W='hwInfoRAIDID'
_V='hwInfoInterfaceControllerID'
_U='hwInfoInterfaceID'
_T='hwInfoExpBoardSubrackID'
_S='hwInfoExpBoardID'
_R='hwInfoFanSubrackId'
_Q='hwInfoFanID'
_P='hwInfoBBUControllerID'
_O='hwInfoBBUID'
_N='hwInfoPowerSubrackID'
_M='hwInfoPowerID'
_L='hwInfoLogicDiskSlotID'
_K='hwInfoLogicDiskFrameID'
_J='hwInfoPhysicDiskSlotID'
_I='hwInfoPhysicDiskFrameID'
_H='hwInfoControllerID'
_G='MB'
_F='IO/s'
_E='MB/s'
_D='%'
_C='read-only'
_B='ISM-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DateAndTime,DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime','DisplayString','PhysAddress','RowStatus','TextualConvention')
hwStorage=ModuleIdentity((1,3,6,1,4,1,34774,4))
if mibBuilder.loadTexts:hwStorage.setRevisions(('2013-04-06 13:54',))
class NodeCodeString(TextualConvention,OctetString):status=_A;displayHint='255a';subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(15,17))
_Huaweistorage_ObjectIdentity=ObjectIdentity
huaweistorage=_Huaweistorage_ObjectIdentity((1,3,6,1,4,1,34774))
_HwISM_ObjectIdentity=ObjectIdentity
hwISM=_HwISM_ObjectIdentity((1,3,6,1,4,1,34774,4,1))
_HwMIB_ObjectIdentity=ObjectIdentity
hwMIB=_HwMIB_ObjectIdentity((1,3,6,1,4,1,34774,4,1,22))
_HwInfoControllerTable_Object=MibTable
hwInfoControllerTable=_HwInfoControllerTable_Object((1,3,6,1,4,1,34774,4,1,22,1))
if mibBuilder.loadTexts:hwInfoControllerTable.setStatus(_A)
_HwInfoControllerEntry_Object=MibTableRow
hwInfoControllerEntry=_HwInfoControllerEntry_Object((1,3,6,1,4,1,34774,4,1,22,1,1))
hwInfoControllerEntry.setIndexNames((0,_B,_H))
if mibBuilder.loadTexts:hwInfoControllerEntry.setStatus(_A)
_HwInfoControllerID_Type=Unsigned32
_HwInfoControllerID_Object=MibTableColumn
hwInfoControllerID=_HwInfoControllerID_Object((1,3,6,1,4,1,34774,4,1,22,1,1,1),_HwInfoControllerID_Type())
hwInfoControllerID.setMaxAccess(_C)
if mibBuilder.loadTexts:hwInfoControllerID.setStatus(_A)
_HwInfoControllerIP_Type=OctetString
_HwInfoControllerIP_Object=MibTableColumn
hwInfoControllerIP=_HwInfoControllerIP_Object((1,3,6,1,4,1,34774,4,1,22,1,1,2),_HwInfoControllerIP_Type())
hwInfoControllerIP.setMaxAccess(_C)
if mibBuilder.loadTexts:hwInfoControllerIP.setStatus(_A)
_HwInfoControllerIsMaster_Type=Unsigned32
_HwInfoControllerIsMaster_Object=MibTableColumn
hwInfoControllerIsMaster=_HwInfoControllerIsMaster_Object((1,3,6,1,4,1,34774,4,1,22,1,1,3),_HwInfoControllerIsMaster_Type())
hwInfoControllerIsMaster.setMaxAccess(_C)
if mibBuilder.loadTexts:hwInfoControllerIsMaster.setStatus(_A)
_HwInfoControllerCpuUsingRatio_Type=Unsigned32
_HwInfoControllerCpuUsingRatio_Object=MibTableColumn
hwInfoControllerCpuUsingRatio=_HwInfoControllerCpuUsingRatio_Object((1,3,6,1,4,1,34774,4,1,22,1,1,4),_HwInfoControllerCpuUsingRatio_Type())
hwInfoControllerCpuUsingRatio.setMaxAccess(_C)
if mibBuilder.loadTexts:hwInfoControllerCpuUsingRatio.setStatus(_A)
if mibBuilder.loadTexts:hwInfoControllerCpuUsingRatio.setUnits(_D)
_HwInfoControllerMemoryUsingRatio_Type=Unsigned32
_HwInfoControllerMemoryUsingRatio_Object=MibTableColumn
hwInfoControllerMemoryUsingRatio=_HwInfoControllerMemoryUsingRatio_Object((1,3,6,1,4,1,34774,4,1,22,1,1,5),_HwInfoControllerMemoryUsingRatio_Type())
hwInfoControllerMemoryUsingRatio.setMaxAccess(_C)
if mibBuilder.loadTexts:hwInfoControllerMemoryUsingRatio.setStatus(_A)
if mibBuilder.loadTexts:hwInfoControllerMemoryUsingRatio.setUnits(_D)
_HwInfoControllerVersion_Type=OctetString
_HwInfoControllerVersion_Object=MibTableColumn
hwInfoControllerVersion=_HwInfoControllerVersion_Object((1,3,6,1,4,1,34774,4,1,22,1,1,6),_HwInfoControllerVersion_Type())
hwInfoControllerVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:hwInfoControllerVersion.setStatus(_A)
_HwInfoControllerStatus_Type=Unsigned32
_HwInfoControllerStatus_Object=MibTableColumn
hwInfoControllerStatus=_HwInfoControllerStatus_Object((1,3,6,1,4,1,34774,4,1,22,1,1,7),_HwInfoControllerStatus_Type())
hwInfoControllerStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:hwInfoControllerStatus.setStatus(_A)
_HwInfoControllerDescription_Type=OctetString
_HwInfoControllerDescription_Object=MibTableColumn
hwInfoControllerDescription=_HwInfoControllerDescription_Object((1,3,6,1,4,1,34774,4,1,22,1,1,8),_HwInfoControllerDescription_Type())
hwInfoControllerDescription.setMaxAccess(_C)
if mibBuilder.loadTexts:hwInfoControllerDescription.setStatus(_A)
_HwInfoPhysicDiskTable_Object=MibTable
hwInfoPhysicDiskTable=_HwInfoPhysicDiskTable_Object((1,3,6,1,4,1,34774,4,1,22,2))
if mibBuilder.loadTexts:hwInfoPhysicDiskTable.setStatus(_A)
_HwInfoPhysicDiskEntry_Object=MibTableRow
hwInfoPhysicDiskEntry=_HwInfoPhysicDiskEntry_Object((1,3,6,1,4,1,34774,4,1,22,2,1))
hwInfoPhysicDiskEntry.setIndexNames((0,_B,_I),(0,_B,_J))
if mibBuilder.loadTexts:hwInfoPhysicDiskEntry.setStatus(_A)
_HwInfoPhysicDiskFrameID_Type=Unsigned32
_HwInfoPhysicDiskFrameID_Object=MibTableColumn
hwInfoPhysicDiskFrameID=_HwInfoPhysicDiskFrameID_Object((1,3,6,1,4,1,34774,4,1,22,2,1,1),_HwInfoPhysicDiskFrameID_Type())
hwInfoPhysicDiskFrameID.setMaxAccess(_C)
if mibBuilder.loadTexts:hwInfoPhysicDiskFrameID.setStatus(_A)
_HwInfoPhysicDiskSlotID_Type=Unsigned32
_HwInfoPhysicDiskSlotID_Object=MibTableColumn
hwInfoPhysicDiskSlotID=_HwInfoPhysicDiskSlotID_Object((1,3,6,1,4,1,34774,4,1,22,2,1,2),_HwInfoPhysicDiskSlotID_Type())
hwInfoPhysicDiskSlotID.setMaxAccess(_C)
if mibBuilder.loadTexts:hwInfoPhysicDiskSlotID.setStatus(_A)
_HwInfoPhysicDiskStatus_Type=Unsigned32
_HwInfoPhysicDiskStatus_Object=MibTableColumn
hwInfoPhysicDiskStatus=_HwInfoPhysicDiskStatus_Object((1,3,6,1,4,1,34774,4,1,22,2,1,3),_HwInfoPhysicDiskStatus_Type())
hwInfoPhysicDiskStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:hwInfoPhysicDiskStatus.setStatus(_A)
_HwInfoPhysicDiskSZType_Type=Unsigned32
_HwInfoPhysicDiskSZType_Object=MibTableColumn
hwInfoPhysicDiskSZType=_HwInfoPhysicDiskSZType_Object((1,3,6,1,4,1,34774,4,1,22,2,1,4),_HwInfoPhysicDiskSZType_Type())
hwInfoPhysicDiskSZType.setMaxAccess(_C)
if mibBuilder.loadTexts:hwInfoPhysicDiskSZType.setStatus(_A)
_HwInfoPhysicDiskSZVendor_Type=OctetString
_HwInfoPhysicDiskSZVendor_Object=MibTableColumn
hwInfoPhysicDiskSZVendor=_HwInfoPhysicDiskSZVendor_Object((1,3,6,1,4,1,34774,4,1,22,2,1,5),_HwInfoPhysicDiskSZVendor_Type())
hwInfoPhysicDiskSZVendor.setMaxAccess(_C)
if mibBuilder.loadTexts:hwInfoPhysicDiskSZVendor.setStatus(_A)
_HwInfoPhysicDiskSZModel_Type=OctetString
_HwInfoPhysicDiskSZModel_Object=MibTableColumn
hwInfoPhysicDiskSZModel=_HwInfoPhysicDiskSZModel_Object((1,3,6,1,4,1,34774,4,1,22,2,1,6),_HwInfoPhysicDiskSZModel_Type())
hwInfoPhysicDiskSZModel.setMaxAccess(_C)
if mibBuilder.loadTexts:hwInfoPhysicDiskSZModel.setStatus(_A)
_HwInfoPhysicDiskSZSerial_Type=OctetString
_HwInfoPhysicDiskSZSerial_Object=MibTableColumn
hwInfoPhysicDiskSZSerial=_HwInfoPhysicDiskSZSerial_Object((1,3,6,1,4,1,34774,4,1,22,2,1,7),_HwInfoPhysicDiskSZSerial_Type())
hwInfoPhysicDiskSZSerial.setMaxAccess(_C)
if mibBuilder.loadTexts:hwInfoPhysicDiskSZSerial.setStatus(_A)
if mibBuilder.loadTexts:hwInfoPhysicDiskSZSerial.setUnits('GB')
_HwInfoPhysicDiskSZFirmware_Type=OctetString
_HwInfoPhysicDiskSZFirmware_Object=MibTableColumn
hwInfoPhysicDiskSZFirmware=_HwInfoPhysicDiskSZFirmware_Object((1,3,6,1,4,1,34774,4,1,22,2,1,8),_HwInfoPhysicDiskSZFirmware_Type())
hwInfoPhysicDiskSZFirmware.setMaxAccess(_C)
if mibBuilder.loadTexts:hwInfoPhysicDiskSZFirmware.setStatus(_A)
_HwInfoPhysicDiskSpinSpeed_Type=Unsigned32
_HwInfoPhysicDiskSpinSpeed_Object=MibTableColumn
hwInfoPhysicDiskSpinSpeed=_HwInfoPhysicDiskSpinSpeed_Object((1,3,6,1,4,1,34774,4,1,22,2,1,9),_HwInfoPhysicDiskSpinSpeed_Type())
hwInfoPhysicDiskSpinSpeed.setMaxAccess(_C)
if mibBuilder.loadTexts:hwInfoPhysicDiskSpinSpeed.setStatus(_A)
if mibBuilder.loadTexts:hwInfoPhysicDiskSpinSpeed.setUnits('RPM')
_HwInfoPhysicDiskCurrentSpeed_Type=Unsigned32
_HwInfoPhysicDiskCurrentSpeed_Object=MibTableColumn
hwInfoPhysicDiskCurrentSpeed=_HwInfoPhysicDiskCurrentSpeed_Object((1,3,6,1,4,1,34774,4,1,22,2,1,10),_HwInfoPhysicDiskCurrentSpeed_Type())
hwInfoPhysicDiskCurrentSpeed.setMaxAccess(_C)
if mibBuilder.loadTexts:hwInfoPhysicDiskCurrentSpeed.setStatus(_A)
if mibBuilder.loadTexts:hwInfoPhysicDiskCurrentSpeed.setUnits('0.1Gpbs')
_HwInfoPhysicDiskRawCapacity_Type=Unsigned32
_HwInfoPhysicDiskRawCapacity_Object=MibTableColumn
hwInfoPhysicDiskRawCapacity=_HwInfoPhysicDiskRawCapacity_Object((1,3,6,1,4,1,34774,4,1,22,2,1,11),_HwInfoPhysicDiskRawCapacity_Type())
hwInfoPhysicDiskRawCapacity.setMaxAccess(_C)
if mibBuilder.loadTexts:hwInfoPhysicDiskRawCapacity.setStatus(_A)
if mibBuilder.loadTexts:hwInfoPhysicDiskRawCapacity.setUnits('GB')
_HwInfoLogicDiskTable_Object=MibTable
hwInfoLogicDiskTable=_HwInfoLogicDiskTable_Object((1,3,6,1,4,1,34774,4,1,22,3))
if mibBuilder.loadTexts:hwInfoLogicDiskTable.setStatus(_A)
_HwInfoLogicDiskEntry_Object=MibTableRow
hwInfoLogicDiskEntry=_HwInfoLogicDiskEntry_Object((1,3,6,1,4,1,34774,4,1,22,3,1))
hwInfoLogicDiskEntry.setIndexNames((0,_B,_K),(0,_B,_L))
if mibBuilder.loadTexts:hwInfoLogicDiskEntry.setStatus(_A)
_HwInfoLogicDiskFrameID_Type=Unsigned32
_HwInfoLogicDiskFrameID_Object=MibTableColumn
hwInfoLogicDiskFrameID=_HwInfoLogicDiskFrameID_Object((1,3,6,1,4,1,34774,4,1,22,3,1,1),_HwInfoLogicDiskFrameID_Type())
hwInfoLogicDiskFrameID.setMaxAccess(_C)
if mibBuilder.loadTexts:hwInfoLogicDiskFrameID.setStatus(_A)
_HwInfoLogicDiskSlotID_Type=Unsigned32
_HwInfoLogicDiskSlotID_Object=MibTableColumn
hwInfoLogicDiskSlotID=_HwInfoLogicDiskSlotID_Object((1,3,6,1,4,1,34774,4,1,22,3,1,2),_HwInfoLogicDiskSlotID_Type())
hwInfoLogicDiskSlotID.setMaxAccess(_C)
if mibBuilder.loadTexts:hwInfoLogicDiskSlotID.setStatus(_A)
_HwInfoLogicDiskLogicStatus_Type=Unsigned32
_HwInfoLogicDiskLogicStatus_Object=MibTableColumn
hwInfoLogicDiskLogicStatus=_HwInfoLogicDiskLogicStatus_Object((1,3,6,1,4,1,34774,4,1,22,3,1,3),_HwInfoLogicDiskLogicStatus_Type())
hwInfoLogicDiskLogicStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:hwInfoLogicDiskLogicStatus.setStatus(_A)
_HwInfoLogicDiskLogicType_Type=Unsigned32
_HwInfoLogicDiskLogicType_Object=MibTableColumn
hwInfoLogicDiskLogicType=_HwInfoLogicDiskLogicType_Object((1,3,6,1,4,1,34774,4,1,22,3,1,4),_HwInfoLogicDiskLogicType_Type())
hwInfoLogicDiskLogicType.setMaxAccess(_C)
if mibBuilder.loadTexts:hwInfoLogicDiskLogicType.setStatus(_A)
_HwInfoLogicDiskSize_Type=Unsigned32
_HwInfoLogicDiskSize_Object=MibTableColumn
hwInfoLogicDiskSize=_HwInfoLogicDiskSize_Object((1,3,6,1,4,1,34774,4,1,22,3,1,5),_HwInfoLogicDiskSize_Type())
hwInfoLogicDiskSize.setMaxAccess(_C)
if mibBuilder.loadTexts:hwInfoLogicDiskSize.setStatus(_A)
if mibBuilder.loadTexts:hwInfoLogicDiskSize.setUnits('GB')
_HwInfoPowerTable_Object=MibTable
hwInfoPowerTable=_HwInfoPowerTable_Object((1,3,6,1,4,1,34774,4,1,22,4))
if mibBuilder.loadTexts:hwInfoPowerTable.setStatus(_A)
_HwInfoPowerEntry_Object=MibTableRow
hwInfoPowerEntry=_HwInfoPowerEntry_Object((1,3,6,1,4,1,34774,4,1,22,4,1))
hwInfoPowerEntry.setIndexNames((0,_B,_M),(0,_B,_N))
if mibBuilder.loadTexts:hwInfoPowerEntry.setStatus(_A)
_HwInfoPowerID_Type=Unsigned32
_HwInfoPowerID_Object=MibTableColumn
hwInfoPowerID=_HwInfoPowerID_Object((1,3,6,1,4,1,34774,4,1,22,4,1,1),_HwInfoPowerID_Type())
hwInfoPowerID.setMaxAccess(_C)
if mibBuilder.loadTexts:hwInfoPowerID.setStatus(_A)
_HwInfoPowerSubrackID_Type=Unsigned32
_HwInfoPowerSubrackID_Object=MibTableColumn
hwInfoPowerSubrackID=_HwInfoPowerSubrackID_Object((1,3,6,1,4,1,34774,4,1,22,4,1,2),_HwInfoPowerSubrackID_Type())
hwInfoPowerSubrackID.setMaxAccess(_C)
if mibBuilder.loadTexts:hwInfoPowerSubrackID.setStatus(_A)
_HwInfoPowerStatus_Type=Unsigned32
_HwInfoPowerStatus_Object=MibTableColumn
hwInfoPowerStatus=_HwInfoPowerStatus_Object((1,3,6,1,4,1,34774,4,1,22,4,1,3),_HwInfoPowerStatus_Type())
hwInfoPowerStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:hwInfoPowerStatus.setStatus(_A)
_HwInfoPowerTemperature_Type=Unsigned32
_HwInfoPowerTemperature_Object=MibTableColumn
hwInfoPowerTemperature=_HwInfoPowerTemperature_Object((1,3,6,1,4,1,34774,4,1,22,4,1,4),_HwInfoPowerTemperature_Type())
hwInfoPowerTemperature.setMaxAccess(_C)
if mibBuilder.loadTexts:hwInfoPowerTemperature.setStatus(_A)
if mibBuilder.loadTexts:hwInfoPowerTemperature.setUnits(_g)
_HwInfoPowerVendor_Type=OctetString
_HwInfoPowerVendor_Object=MibTableColumn
hwInfoPowerVendor=_HwInfoPowerVendor_Object((1,3,6,1,4,1,34774,4,1,22,4,1,5),_HwInfoPowerVendor_Type())
hwInfoPowerVendor.setMaxAccess(_C)
if mibBuilder.loadTexts:hwInfoPowerVendor.setStatus(_A)
_HwInfoPowerModle_Type=OctetString
_HwInfoPowerModle_Object=MibTableColumn
hwInfoPowerModle=_HwInfoPowerModle_Object((1,3,6,1,4,1,34774,4,1,22,4,1,6),_HwInfoPowerModle_Type())
hwInfoPowerModle.setMaxAccess(_C)
if mibBuilder.loadTexts:hwInfoPowerModle.setStatus(_A)
_HwInfoPowerVersion_Type=OctetString
_HwInfoPowerVersion_Object=MibTableColumn
hwInfoPowerVersion=_HwInfoPowerVersion_Object((1,3,6,1,4,1,34774,4,1,22,4,1,7),_HwInfoPowerVersion_Type())
hwInfoPowerVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:hwInfoPowerVersion.setStatus(_A)
_HwInfoPowerDate_Type=OctetString
_HwInfoPowerDate_Object=MibTableColumn
hwInfoPowerDate=_HwInfoPowerDate_Object((1,3,6,1,4,1,34774,4,1,22,4,1,8),_HwInfoPowerDate_Type())
hwInfoPowerDate.setMaxAccess(_C)
if mibBuilder.loadTexts:hwInfoPowerDate.setStatus(_A)
_HwInfoPowerType_Type=Unsigned32
_HwInfoPowerType_Object=MibTableColumn
hwInfoPowerType=_HwInfoPowerType_Object((1,3,6,1,4,1,34774,4,1,22,4,1,9),_HwInfoPowerType_Type())
hwInfoPowerType.setMaxAccess(_C)
if mibBuilder.loadTexts:hwInfoPowerType.setStatus(_A)
_HwInfoPowerSN_Type=OctetString
_HwInfoPowerSN_Object=MibTableColumn
hwInfoPowerSN=_HwInfoPowerSN_Object((1,3,6,1,4,1,34774,4,1,22,4,1,10),_HwInfoPowerSN_Type())
hwInfoPowerSN.setMaxAccess(_C)
if mibBuilder.loadTexts:hwInfoPowerSN.setStatus(_A)
_HwInfoPowerDisplayID_Type=OctetString
_HwInfoPowerDisplayID_Object=MibTableColumn
hwInfoPowerDisplayID=_HwInfoPowerDisplayID_Object((1,3,6,1,4,1,34774,4,1,22,4,1,11),_HwInfoPowerDisplayID_Type())
hwInfoPowerDisplayID.setMaxAccess(_C)
if mibBuilder.loadTexts:hwInfoPowerDisplayID.setStatus(_A)
_HwInfoPowerDescription_Type=OctetString
_HwInfoPowerDescription_Object=MibTableColumn
hwInfoPowerDescription=_HwInfoPowerDescription_Object((1,3,6,1,4,1,34774,4,1,22,4,1,12),_HwInfoPowerDescription_Type())
hwInfoPowerDescription.setMaxAccess(_C)
if mibBuilder.loadTexts:hwInfoPowerDescription.setStatus(_A)
_HwInfoBBUTable_Object=MibTable
hwInfoBBUTable=_HwInfoBBUTable_Object((1,3,6,1,4,1,34774,4,1,22,5))
if mibBuilder.loadTexts:hwInfoBBUTable.setStatus(_A)
_HwInfoBBUEntry_Object=MibTableRow
hwInfoBBUEntry=_HwInfoBBUEntry_Object((1,3,6,1,4,1,34774,4,1,22,5,1))
hwInfoBBUEntry.setIndexNames((0,_B,_O),(0,_B,_P))
if mibBuilder.loadTexts:hwInfoBBUEntry.setStatus(_A)
_HwInfoBBUID_Type=Unsigned32
_HwInfoBBUID_Object=MibTableColumn
hwInfoBBUID=_HwInfoBBUID_Object((1,3,6,1,4,1,34774,4,1,22,5,1,1),_HwInfoBBUID_Type())
hwInfoBBUID.setMaxAccess(_C)
if mibBuilder.loadTexts:hwInfoBBUID.setStatus(_A)
_HwInfoBBUControllerID_Type=Unsigned32
_HwInfoBBUControllerID_Object=MibTableColumn
hwInfoBBUControllerID=_HwInfoBBUControllerID_Object((1,3,6,1,4,1,34774,4,1,22,5,1,2),_HwInfoBBUControllerID_Type())
hwInfoBBUControllerID.setMaxAccess(_C)
if mibBuilder.loadTexts:hwInfoBBUControllerID.setStatus(_A)
_HwInfoBBUPresentStatus_Type=Unsigned32
_HwInfoBBUPresentStatus_Object=MibTableColumn
hwInfoBBUPresentStatus=_HwInfoBBUPresentStatus_Object((1,3,6,1,4,1,34774,4,1,22,5,1,3),_HwInfoBBUPresentStatus_Type())
hwInfoBBUPresentStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:hwInfoBBUPresentStatus.setStatus(_A)
_HwInfoBBUStatus_Type=Unsigned32
_HwInfoBBUStatus_Object=MibTableColumn
hwInfoBBUStatus=_HwInfoBBUStatus_Object((1,3,6,1,4,1,34774,4,1,22,5,1,4),_HwInfoBBUStatus_Type())
hwInfoBBUStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:hwInfoBBUStatus.setStatus(_A)
_HwInfoBBUCurrentVoltage_Type=Unsigned32
_HwInfoBBUCurrentVoltage_Object=MibTableColumn
hwInfoBBUCurrentVoltage=_HwInfoBBUCurrentVoltage_Object((1,3,6,1,4,1,34774,4,1,22,5,1,5),_HwInfoBBUCurrentVoltage_Type())
hwInfoBBUCurrentVoltage.setMaxAccess(_C)
if mibBuilder.loadTexts:hwInfoBBUCurrentVoltage.setStatus(_A)
if mibBuilder.loadTexts:hwInfoBBUCurrentVoltage.setUnits('0.1V')
_HwInfoBBUIsChargeFull_Type=Unsigned32
_HwInfoBBUIsChargeFull_Object=MibTableColumn
hwInfoBBUIsChargeFull=_HwInfoBBUIsChargeFull_Object((1,3,6,1,4,1,34774,4,1,22,5,1,6),_HwInfoBBUIsChargeFull_Type())
hwInfoBBUIsChargeFull.setMaxAccess(_C)
if mibBuilder.loadTexts:hwInfoBBUIsChargeFull.setStatus(_A)
_HwInfoBBUDischargeTime_Type=Unsigned32
_HwInfoBBUDischargeTime_Object=MibTableColumn
hwInfoBBUDischargeTime=_HwInfoBBUDischargeTime_Object((1,3,6,1,4,1,34774,4,1,22,5,1,7),_HwInfoBBUDischargeTime_Type())
hwInfoBBUDischargeTime.setMaxAccess(_C)
if mibBuilder.loadTexts:hwInfoBBUDischargeTime.setStatus(_A)
if mibBuilder.loadTexts:hwInfoBBUDischargeTime.setUnits('number of times')
_HwInfoBBURemainLife_Type=Unsigned32
_HwInfoBBURemainLife_Object=MibTableColumn
hwInfoBBURemainLife=_HwInfoBBURemainLife_Object((1,3,6,1,4,1,34774,4,1,22,5,1,8),_HwInfoBBURemainLife_Type())
hwInfoBBURemainLife.setMaxAccess(_C)
if mibBuilder.loadTexts:hwInfoBBURemainLife.setStatus(_A)
if mibBuilder.loadTexts:hwInfoBBURemainLife.setUnits('days')
_HwInfoBBUFWVersion_Type=OctetString
_HwInfoBBUFWVersion_Object=MibTableColumn
hwInfoBBUFWVersion=_HwInfoBBUFWVersion_Object((1,3,6,1,4,1,34774,4,1,22,5,1,9),_HwInfoBBUFWVersion_Type())
hwInfoBBUFWVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:hwInfoBBUFWVersion.setStatus(_A)
_HwInfoBBUELable_Type=OctetString
_HwInfoBBUELable_Object=MibTableColumn
hwInfoBBUELable=_HwInfoBBUELable_Object((1,3,6,1,4,1,34774,4,1,22,5,1,10),_HwInfoBBUELable_Type())
hwInfoBBUELable.setMaxAccess(_C)
if mibBuilder.loadTexts:hwInfoBBUELable.setStatus(_A)
_HwInfoBBUChargeState_Type=Unsigned32
_HwInfoBBUChargeState_Object=MibTableColumn
hwInfoBBUChargeState=_HwInfoBBUChargeState_Object((1,3,6,1,4,1,34774,4,1,22,5,1,11),_HwInfoBBUChargeState_Type())
hwInfoBBUChargeState.setMaxAccess(_C)
if mibBuilder.loadTexts:hwInfoBBUChargeState.setStatus(_A)
_HwInfoFanTable_Object=MibTable
hwInfoFanTable=_HwInfoFanTable_Object((1,3,6,1,4,1,34774,4,1,22,6))
if mibBuilder.loadTexts:hwInfoFanTable.setStatus(_A)
_HwInfoFanEntry_Object=MibTableRow
hwInfoFanEntry=_HwInfoFanEntry_Object((1,3,6,1,4,1,34774,4,1,22,6,1))
hwInfoFanEntry.setIndexNames((0,_B,_Q),(0,_B,_R))
if mibBuilder.loadTexts:hwInfoFanEntry.setStatus(_A)
_HwInfoFanID_Type=Unsigned32
_HwInfoFanID_Object=MibTableColumn
hwInfoFanID=_HwInfoFanID_Object((1,3,6,1,4,1,34774,4,1,22,6,1,1),_HwInfoFanID_Type())
hwInfoFanID.setMaxAccess(_C)
if mibBuilder.loadTexts:hwInfoFanID.setStatus(_A)
_HwInfoFanSubrackId_Type=Unsigned32
_HwInfoFanSubrackId_Object=MibTableColumn
hwInfoFanSubrackId=_HwInfoFanSubrackId_Object((1,3,6,1,4,1,34774,4,1,22,6,1,2),_HwInfoFanSubrackId_Type())
hwInfoFanSubrackId.setMaxAccess(_C)
if mibBuilder.loadTexts:hwInfoFanSubrackId.setStatus(_A)
_HwInfoFanRunningStatus_Type=Unsigned32
_HwInfoFanRunningStatus_Object=MibTableColumn
hwInfoFanRunningStatus=_HwInfoFanRunningStatus_Object((1,3,6,1,4,1,34774,4,1,22,6,1,3),_HwInfoFanRunningStatus_Type())
hwInfoFanRunningStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:hwInfoFanRunningStatus.setStatus(_A)
_HwInfoFanRunningLevel_Type=Unsigned32
_HwInfoFanRunningLevel_Object=MibTableColumn
hwInfoFanRunningLevel=_HwInfoFanRunningLevel_Object((1,3,6,1,4,1,34774,4,1,22,6,1,4),_HwInfoFanRunningLevel_Type())
hwInfoFanRunningLevel.setMaxAccess(_C)
if mibBuilder.loadTexts:hwInfoFanRunningLevel.setStatus(_A)
_HwInfoFanRunningSection_Type=Unsigned32
_HwInfoFanRunningSection_Object=MibTableColumn
hwInfoFanRunningSection=_HwInfoFanRunningSection_Object((1,3,6,1,4,1,34774,4,1,22,6,1,5),_HwInfoFanRunningSection_Type())
hwInfoFanRunningSection.setMaxAccess(_C)
if mibBuilder.loadTexts:hwInfoFanRunningSection.setStatus(_A)
_HwInfoFanELable_Type=OctetString
_HwInfoFanELable_Object=MibTableColumn
hwInfoFanELable=_HwInfoFanELable_Object((1,3,6,1,4,1,34774,4,1,22,6,1,6),_HwInfoFanELable_Type())
hwInfoFanELable.setMaxAccess(_C)
if mibBuilder.loadTexts:hwInfoFanELable.setStatus(_A)
_HwInfoFanDescription_Type=OctetString
_HwInfoFanDescription_Object=MibTableColumn
hwInfoFanDescription=_HwInfoFanDescription_Object((1,3,6,1,4,1,34774,4,1,22,6,1,7),_HwInfoFanDescription_Type())
hwInfoFanDescription.setMaxAccess(_C)
if mibBuilder.loadTexts:hwInfoFanDescription.setStatus(_A)
_HwInfoExpBoardTable_Object=MibTable
hwInfoExpBoardTable=_HwInfoExpBoardTable_Object((1,3,6,1,4,1,34774,4,1,22,7))
if mibBuilder.loadTexts:hwInfoExpBoardTable.setStatus(_A)
_HwInfoExpBoardEntry_Object=MibTableRow
hwInfoExpBoardEntry=_HwInfoExpBoardEntry_Object((1,3,6,1,4,1,34774,4,1,22,7,1))
hwInfoExpBoardEntry.setIndexNames((0,_B,_S),(0,_B,_T))
if mibBuilder.loadTexts:hwInfoExpBoardEntry.setStatus(_A)
_HwInfoExpBoardSubrackID_Type=Unsigned32
_HwInfoExpBoardSubrackID_Object=MibTableColumn
hwInfoExpBoardSubrackID=_HwInfoExpBoardSubrackID_Object((1,3,6,1,4,1,34774,4,1,22,7,1,1),_HwInfoExpBoardSubrackID_Type())
hwInfoExpBoardSubrackID.setMaxAccess(_C)
if mibBuilder.loadTexts:hwInfoExpBoardSubrackID.setStatus(_A)
_HwInfoExpBoardID_Type=Unsigned32
_HwInfoExpBoardID_Object=MibTableColumn
hwInfoExpBoardID=_HwInfoExpBoardID_Object((1,3,6,1,4,1,34774,4,1,22,7,1,2),_HwInfoExpBoardID_Type())
hwInfoExpBoardID.setMaxAccess(_C)
if mibBuilder.loadTexts:hwInfoExpBoardID.setStatus(_A)
_HwInfoExpBoardStatus_Type=Unsigned32
_HwInfoExpBoardStatus_Object=MibTableColumn
hwInfoExpBoardStatus=_HwInfoExpBoardStatus_Object((1,3,6,1,4,1,34774,4,1,22,7,1,3),_HwInfoExpBoardStatus_Type())
hwInfoExpBoardStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:hwInfoExpBoardStatus.setStatus(_A)
_HwInfoExpBoardLogicVersion_Type=OctetString
_HwInfoExpBoardLogicVersion_Object=MibTableColumn
hwInfoExpBoardLogicVersion=_HwInfoExpBoardLogicVersion_Object((1,3,6,1,4,1,34774,4,1,22,7,1,4),_HwInfoExpBoardLogicVersion_Type())
hwInfoExpBoardLogicVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:hwInfoExpBoardLogicVersion.setStatus(_A)
_HwInfoExpBoardPCBversion_Type=OctetString
_HwInfoExpBoardPCBversion_Object=MibTableColumn
hwInfoExpBoardPCBversion=_HwInfoExpBoardPCBversion_Object((1,3,6,1,4,1,34774,4,1,22,7,1,5),_HwInfoExpBoardPCBversion_Type())
hwInfoExpBoardPCBversion.setMaxAccess(_C)
if mibBuilder.loadTexts:hwInfoExpBoardPCBversion.setStatus(_A)
_HwInfoExpBoardProduceInfo_Type=OctetString
_HwInfoExpBoardProduceInfo_Object=MibTableColumn
hwInfoExpBoardProduceInfo=_HwInfoExpBoardProduceInfo_Object((1,3,6,1,4,1,34774,4,1,22,7,1,6),_HwInfoExpBoardProduceInfo_Type())
hwInfoExpBoardProduceInfo.setMaxAccess(_C)
if mibBuilder.loadTexts:hwInfoExpBoardProduceInfo.setStatus(_A)
_HwInfoExpBoardType_Type=Unsigned32
_HwInfoExpBoardType_Object=MibTableColumn
hwInfoExpBoardType=_HwInfoExpBoardType_Object((1,3,6,1,4,1,34774,4,1,22,7,1,7),_HwInfoExpBoardType_Type())
hwInfoExpBoardType.setMaxAccess(_C)
if mibBuilder.loadTexts:hwInfoExpBoardType.setStatus(_A)
_HwInfoInterfaceTable_Object=MibTable
hwInfoInterfaceTable=_HwInfoInterfaceTable_Object((1,3,6,1,4,1,34774,4,1,22,8))
if mibBuilder.loadTexts:hwInfoInterfaceTable.setStatus(_A)
_HwInfoInterfaceEntry_Object=MibTableRow
hwInfoInterfaceEntry=_HwInfoInterfaceEntry_Object((1,3,6,1,4,1,34774,4,1,22,8,1))
hwInfoInterfaceEntry.setIndexNames((0,_B,_U),(0,_B,_V))
if mibBuilder.loadTexts:hwInfoInterfaceEntry.setStatus(_A)
_HwInfoInterfaceID_Type=Unsigned32
_HwInfoInterfaceID_Object=MibTableColumn
hwInfoInterfaceID=_HwInfoInterfaceID_Object((1,3,6,1,4,1,34774,4,1,22,8,1,1),_HwInfoInterfaceID_Type())
hwInfoInterfaceID.setMaxAccess(_C)
if mibBuilder.loadTexts:hwInfoInterfaceID.setStatus(_A)
_HwInfoInterfaceControllerID_Type=Unsigned32
_HwInfoInterfaceControllerID_Object=MibTableColumn
hwInfoInterfaceControllerID=_HwInfoInterfaceControllerID_Object((1,3,6,1,4,1,34774,4,1,22,8,1,2),_HwInfoInterfaceControllerID_Type())
hwInfoInterfaceControllerID.setMaxAccess(_C)
if mibBuilder.loadTexts:hwInfoInterfaceControllerID.setStatus(_A)
_HwInfoInterfaceType_Type=Unsigned32
_HwInfoInterfaceType_Object=MibTableColumn
hwInfoInterfaceType=_HwInfoInterfaceType_Object((1,3,6,1,4,1,34774,4,1,22,8,1,3),_HwInfoInterfaceType_Type())
hwInfoInterfaceType.setMaxAccess(_C)
if mibBuilder.loadTexts:hwInfoInterfaceType.setStatus(_A)
_HwInfoInterfaceStatus_Type=Unsigned32
_HwInfoInterfaceStatus_Object=MibTableColumn
hwInfoInterfaceStatus=_HwInfoInterfaceStatus_Object((1,3,6,1,4,1,34774,4,1,22,8,1,4),_HwInfoInterfaceStatus_Type())
hwInfoInterfaceStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:hwInfoInterfaceStatus.setStatus(_A)
_HwInfoInterfaceLogicVersion_Type=OctetString
_HwInfoInterfaceLogicVersion_Object=MibTableColumn
hwInfoInterfaceLogicVersion=_HwInfoInterfaceLogicVersion_Object((1,3,6,1,4,1,34774,4,1,22,8,1,5),_HwInfoInterfaceLogicVersion_Type())
hwInfoInterfaceLogicVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:hwInfoInterfaceLogicVersion.setStatus(_A)
_HwInfoInterfacePCBVersion_Type=OctetString
_HwInfoInterfacePCBVersion_Object=MibTableColumn
hwInfoInterfacePCBVersion=_HwInfoInterfacePCBVersion_Object((1,3,6,1,4,1,34774,4,1,22,8,1,6),_HwInfoInterfacePCBVersion_Type())
hwInfoInterfacePCBVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:hwInfoInterfacePCBVersion.setStatus(_A)
_HwInfoInterfaceVendorInfo_Type=OctetString
_HwInfoInterfaceVendorInfo_Object=MibTableColumn
hwInfoInterfaceVendorInfo=_HwInfoInterfaceVendorInfo_Object((1,3,6,1,4,1,34774,4,1,22,8,1,7),_HwInfoInterfaceVendorInfo_Type())
hwInfoInterfaceVendorInfo.setMaxAccess(_C)
if mibBuilder.loadTexts:hwInfoInterfaceVendorInfo.setStatus(_A)
_HwInfoInterfaceDescription_Type=OctetString
_HwInfoInterfaceDescription_Object=MibTableColumn
hwInfoInterfaceDescription=_HwInfoInterfaceDescription_Object((1,3,6,1,4,1,34774,4,1,22,8,1,8),_HwInfoInterfaceDescription_Type())
hwInfoInterfaceDescription.setMaxAccess(_C)
if mibBuilder.loadTexts:hwInfoInterfaceDescription.setStatus(_A)
_HwInfoRAIDTable_Object=MibTable
hwInfoRAIDTable=_HwInfoRAIDTable_Object((1,3,6,1,4,1,34774,4,1,22,9))
if mibBuilder.loadTexts:hwInfoRAIDTable.setStatus(_A)
_HwInfoRAIDEntry_Object=MibTableRow
hwInfoRAIDEntry=_HwInfoRAIDEntry_Object((1,3,6,1,4,1,34774,4,1,22,9,1))
hwInfoRAIDEntry.setIndexNames((0,_B,_W))
if mibBuilder.loadTexts:hwInfoRAIDEntry.setStatus(_A)
_HwInfoRAIDID_Type=Unsigned32
_HwInfoRAIDID_Object=MibTableColumn
hwInfoRAIDID=_HwInfoRAIDID_Object((1,3,6,1,4,1,34774,4,1,22,9,1,1),_HwInfoRAIDID_Type())
hwInfoRAIDID.setMaxAccess(_C)
if mibBuilder.loadTexts:hwInfoRAIDID.setStatus(_A)
_HwInfoRAIDName_Type=OctetString
_HwInfoRAIDName_Object=MibTableColumn
hwInfoRAIDName=_HwInfoRAIDName_Object((1,3,6,1,4,1,34774,4,1,22,9,1,2),_HwInfoRAIDName_Type())
hwInfoRAIDName.setMaxAccess(_C)
if mibBuilder.loadTexts:hwInfoRAIDName.setStatus(_A)
_HwInfoRAIDLevel_Type=Unsigned32
_HwInfoRAIDLevel_Object=MibTableColumn
hwInfoRAIDLevel=_HwInfoRAIDLevel_Object((1,3,6,1,4,1,34774,4,1,22,9,1,3),_HwInfoRAIDLevel_Type())
hwInfoRAIDLevel.setMaxAccess(_C)
if mibBuilder.loadTexts:hwInfoRAIDLevel.setStatus(_A)
_HwInfoRAIDFreeCapacity_Type=Unsigned32
_HwInfoRAIDFreeCapacity_Object=MibTableColumn
hwInfoRAIDFreeCapacity=_HwInfoRAIDFreeCapacity_Object((1,3,6,1,4,1,34774,4,1,22,9,1,4),_HwInfoRAIDFreeCapacity_Type())
hwInfoRAIDFreeCapacity.setMaxAccess(_C)
if mibBuilder.loadTexts:hwInfoRAIDFreeCapacity.setStatus(_A)
if mibBuilder.loadTexts:hwInfoRAIDFreeCapacity.setUnits(_G)
_HwInfoRAIDStatus_Type=Unsigned32
_HwInfoRAIDStatus_Object=MibTableColumn
hwInfoRAIDStatus=_HwInfoRAIDStatus_Object((1,3,6,1,4,1,34774,4,1,22,9,1,5),_HwInfoRAIDStatus_Type())
hwInfoRAIDStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:hwInfoRAIDStatus.setStatus(_A)
_HwInfoRAIDDiskList_Type=OctetString
_HwInfoRAIDDiskList_Object=MibTableColumn
hwInfoRAIDDiskList=_HwInfoRAIDDiskList_Object((1,3,6,1,4,1,34774,4,1,22,9,1,6),_HwInfoRAIDDiskList_Type())
hwInfoRAIDDiskList.setMaxAccess(_C)
if mibBuilder.loadTexts:hwInfoRAIDDiskList.setStatus(_A)
_HwInfoRAIDTotalSize_Type=Unsigned32
_HwInfoRAIDTotalSize_Object=MibTableColumn
hwInfoRAIDTotalSize=_HwInfoRAIDTotalSize_Object((1,3,6,1,4,1,34774,4,1,22,9,1,7),_HwInfoRAIDTotalSize_Type())
hwInfoRAIDTotalSize.setMaxAccess(_C)
if mibBuilder.loadTexts:hwInfoRAIDTotalSize.setStatus(_A)
if mibBuilder.loadTexts:hwInfoRAIDTotalSize.setUnits(_G)
_HwInfoCacheTable_Object=MibTable
hwInfoCacheTable=_HwInfoCacheTable_Object((1,3,6,1,4,1,34774,4,1,22,10))
if mibBuilder.loadTexts:hwInfoCacheTable.setStatus(_A)
_HwInfoCacheEntry_Object=MibTableRow
hwInfoCacheEntry=_HwInfoCacheEntry_Object((1,3,6,1,4,1,34774,4,1,22,10,1))
hwInfoCacheEntry.setIndexNames((0,_B,_X))
if mibBuilder.loadTexts:hwInfoCacheEntry.setStatus(_A)
_HwInfoCacheID_Type=Unsigned32
_HwInfoCacheID_Object=MibTableColumn
hwInfoCacheID=_HwInfoCacheID_Object((1,3,6,1,4,1,34774,4,1,22,10,1,1),_HwInfoCacheID_Type())
hwInfoCacheID.setMaxAccess(_C)
if mibBuilder.loadTexts:hwInfoCacheID.setStatus(_A)
_HwInfoCacheTotalMemoryCapacity_Type=Unsigned32
_HwInfoCacheTotalMemoryCapacity_Object=MibTableColumn
hwInfoCacheTotalMemoryCapacity=_HwInfoCacheTotalMemoryCapacity_Object((1,3,6,1,4,1,34774,4,1,22,10,1,2),_HwInfoCacheTotalMemoryCapacity_Type())
hwInfoCacheTotalMemoryCapacity.setMaxAccess(_C)
if mibBuilder.loadTexts:hwInfoCacheTotalMemoryCapacity.setStatus(_A)
if mibBuilder.loadTexts:hwInfoCacheTotalMemoryCapacity.setUnits(_G)
_HwInfoCacheSystemMemoryCapacity_Type=Unsigned32
_HwInfoCacheSystemMemoryCapacity_Object=MibTableColumn
hwInfoCacheSystemMemoryCapacity=_HwInfoCacheSystemMemoryCapacity_Object((1,3,6,1,4,1,34774,4,1,22,10,1,3),_HwInfoCacheSystemMemoryCapacity_Type())
hwInfoCacheSystemMemoryCapacity.setMaxAccess(_C)
if mibBuilder.loadTexts:hwInfoCacheSystemMemoryCapacity.setStatus(_A)
if mibBuilder.loadTexts:hwInfoCacheSystemMemoryCapacity.setUnits(_G)
_HwInfoCacheCacheCapacity_Type=Unsigned32
_HwInfoCacheCacheCapacity_Object=MibTableColumn
hwInfoCacheCacheCapacity=_HwInfoCacheCacheCapacity_Object((1,3,6,1,4,1,34774,4,1,22,10,1,4),_HwInfoCacheCacheCapacity_Type())
hwInfoCacheCacheCapacity.setMaxAccess(_C)
if mibBuilder.loadTexts:hwInfoCacheCacheCapacity.setStatus(_A)
if mibBuilder.loadTexts:hwInfoCacheCacheCapacity.setUnits(_G)
_HwInfoCacheCacheUtilization_Type=Unsigned32
_HwInfoCacheCacheUtilization_Object=MibTableColumn
hwInfoCacheCacheUtilization=_HwInfoCacheCacheUtilization_Object((1,3,6,1,4,1,34774,4,1,22,10,1,5),_HwInfoCacheCacheUtilization_Type())
hwInfoCacheCacheUtilization.setMaxAccess(_C)
if mibBuilder.loadTexts:hwInfoCacheCacheUtilization.setStatus(_A)
if mibBuilder.loadTexts:hwInfoCacheCacheUtilization.setUnits(_D)
_HwInfoCacheCacheHitRatio_Type=Unsigned32
_HwInfoCacheCacheHitRatio_Object=MibTableColumn
hwInfoCacheCacheHitRatio=_HwInfoCacheCacheHitRatio_Object((1,3,6,1,4,1,34774,4,1,22,10,1,6),_HwInfoCacheCacheHitRatio_Type())
hwInfoCacheCacheHitRatio.setMaxAccess(_C)
if mibBuilder.loadTexts:hwInfoCacheCacheHitRatio.setStatus(_A)
if mibBuilder.loadTexts:hwInfoCacheCacheHitRatio.setUnits(_D)
_HwInfoCacheCurrentCacheWaterLevel_Type=Unsigned32
_HwInfoCacheCurrentCacheWaterLevel_Object=MibTableColumn
hwInfoCacheCurrentCacheWaterLevel=_HwInfoCacheCurrentCacheWaterLevel_Object((1,3,6,1,4,1,34774,4,1,22,10,1,7),_HwInfoCacheCurrentCacheWaterLevel_Type())
hwInfoCacheCurrentCacheWaterLevel.setMaxAccess(_C)
if mibBuilder.loadTexts:hwInfoCacheCurrentCacheWaterLevel.setStatus(_A)
if mibBuilder.loadTexts:hwInfoCacheCurrentCacheWaterLevel.setUnits(_D)
_HwInfoCacheCacheHighWaterLevel_Type=Unsigned32
_HwInfoCacheCacheHighWaterLevel_Object=MibTableColumn
hwInfoCacheCacheHighWaterLevel=_HwInfoCacheCacheHighWaterLevel_Object((1,3,6,1,4,1,34774,4,1,22,10,1,8),_HwInfoCacheCacheHighWaterLevel_Type())
hwInfoCacheCacheHighWaterLevel.setMaxAccess(_C)
if mibBuilder.loadTexts:hwInfoCacheCacheHighWaterLevel.setStatus(_A)
if mibBuilder.loadTexts:hwInfoCacheCacheHighWaterLevel.setUnits(_D)
_HwInfoCacheCacheLowWaterLevel_Type=Unsigned32
_HwInfoCacheCacheLowWaterLevel_Object=MibTableColumn
hwInfoCacheCacheLowWaterLevel=_HwInfoCacheCacheLowWaterLevel_Object((1,3,6,1,4,1,34774,4,1,22,10,1,9),_HwInfoCacheCacheLowWaterLevel_Type())
hwInfoCacheCacheLowWaterLevel.setMaxAccess(_C)
if mibBuilder.loadTexts:hwInfoCacheCacheLowWaterLevel.setStatus(_A)
if mibBuilder.loadTexts:hwInfoCacheCacheLowWaterLevel.setUnits(_D)
_HwInfoCacheReadCacheUtility_Type=Unsigned32
_HwInfoCacheReadCacheUtility_Object=MibTableColumn
hwInfoCacheReadCacheUtility=_HwInfoCacheReadCacheUtility_Object((1,3,6,1,4,1,34774,4,1,22,10,1,10),_HwInfoCacheReadCacheUtility_Type())
hwInfoCacheReadCacheUtility.setMaxAccess(_C)
if mibBuilder.loadTexts:hwInfoCacheReadCacheUtility.setStatus(_A)
if mibBuilder.loadTexts:hwInfoCacheReadCacheUtility.setUnits(_D)
_HwInfoCacheWriteCacheUtililty_Type=Unsigned32
_HwInfoCacheWriteCacheUtililty_Object=MibTableColumn
hwInfoCacheWriteCacheUtililty=_HwInfoCacheWriteCacheUtililty_Object((1,3,6,1,4,1,34774,4,1,22,10,1,11),_HwInfoCacheWriteCacheUtililty_Type())
hwInfoCacheWriteCacheUtililty.setMaxAccess(_C)
if mibBuilder.loadTexts:hwInfoCacheWriteCacheUtililty.setStatus(_A)
if mibBuilder.loadTexts:hwInfoCacheWriteCacheUtililty.setUnits(_D)
_HwInfoCacheMirroringWriteCacheUtility_Type=Unsigned32
_HwInfoCacheMirroringWriteCacheUtility_Object=MibTableColumn
hwInfoCacheMirroringWriteCacheUtility=_HwInfoCacheMirroringWriteCacheUtility_Object((1,3,6,1,4,1,34774,4,1,22,10,1,12),_HwInfoCacheMirroringWriteCacheUtility_Type())
hwInfoCacheMirroringWriteCacheUtility.setMaxAccess(_C)
if mibBuilder.loadTexts:hwInfoCacheMirroringWriteCacheUtility.setStatus(_A)
if mibBuilder.loadTexts:hwInfoCacheMirroringWriteCacheUtility.setUnits(_D)
_HwInfoCacheWhetherDirtyDataExists_Type=Unsigned32
_HwInfoCacheWhetherDirtyDataExists_Object=MibTableColumn
hwInfoCacheWhetherDirtyDataExists=_HwInfoCacheWhetherDirtyDataExists_Object((1,3,6,1,4,1,34774,4,1,22,10,1,13),_HwInfoCacheWhetherDirtyDataExists_Type())
hwInfoCacheWhetherDirtyDataExists.setMaxAccess(_C)
if mibBuilder.loadTexts:hwInfoCacheWhetherDirtyDataExists.setStatus(_A)
_HwPerfRAIDTable_Object=MibTable
hwPerfRAIDTable=_HwPerfRAIDTable_Object((1,3,6,1,4,1,34774,4,1,22,11))
if mibBuilder.loadTexts:hwPerfRAIDTable.setStatus(_A)
_HwPerfRAIDEntry_Object=MibTableRow
hwPerfRAIDEntry=_HwPerfRAIDEntry_Object((1,3,6,1,4,1,34774,4,1,22,11,1))
hwPerfRAIDEntry.setIndexNames((0,_B,_Y))
if mibBuilder.loadTexts:hwPerfRAIDEntry.setStatus(_A)
_HwPerfRAIDID_Type=Unsigned32
_HwPerfRAIDID_Object=MibTableColumn
hwPerfRAIDID=_HwPerfRAIDID_Object((1,3,6,1,4,1,34774,4,1,22,11,1,1),_HwPerfRAIDID_Type())
hwPerfRAIDID.setMaxAccess(_C)
if mibBuilder.loadTexts:hwPerfRAIDID.setStatus(_A)
_HwPerfRAIDCurrentBandwidth_Type=Unsigned32
_HwPerfRAIDCurrentBandwidth_Object=MibTableColumn
hwPerfRAIDCurrentBandwidth=_HwPerfRAIDCurrentBandwidth_Object((1,3,6,1,4,1,34774,4,1,22,11,1,2),_HwPerfRAIDCurrentBandwidth_Type())
hwPerfRAIDCurrentBandwidth.setMaxAccess(_C)
if mibBuilder.loadTexts:hwPerfRAIDCurrentBandwidth.setStatus(_A)
if mibBuilder.loadTexts:hwPerfRAIDCurrentBandwidth.setUnits(_E)
_HwPerfRAIDThroughput_Type=Unsigned32
_HwPerfRAIDThroughput_Object=MibTableColumn
hwPerfRAIDThroughput=_HwPerfRAIDThroughput_Object((1,3,6,1,4,1,34774,4,1,22,11,1,3),_HwPerfRAIDThroughput_Type())
hwPerfRAIDThroughput.setMaxAccess(_C)
if mibBuilder.loadTexts:hwPerfRAIDThroughput.setStatus(_A)
if mibBuilder.loadTexts:hwPerfRAIDThroughput.setUnits(_F)
_HwPerfRAIDReadBandwidth_Type=Unsigned32
_HwPerfRAIDReadBandwidth_Object=MibTableColumn
hwPerfRAIDReadBandwidth=_HwPerfRAIDReadBandwidth_Object((1,3,6,1,4,1,34774,4,1,22,11,1,4),_HwPerfRAIDReadBandwidth_Type())
hwPerfRAIDReadBandwidth.setMaxAccess(_C)
if mibBuilder.loadTexts:hwPerfRAIDReadBandwidth.setStatus(_A)
if mibBuilder.loadTexts:hwPerfRAIDReadBandwidth.setUnits(_E)
_HwPerfRAIDReadThroughput_Type=Unsigned32
_HwPerfRAIDReadThroughput_Object=MibTableColumn
hwPerfRAIDReadThroughput=_HwPerfRAIDReadThroughput_Object((1,3,6,1,4,1,34774,4,1,22,11,1,5),_HwPerfRAIDReadThroughput_Type())
hwPerfRAIDReadThroughput.setMaxAccess(_C)
if mibBuilder.loadTexts:hwPerfRAIDReadThroughput.setStatus(_A)
if mibBuilder.loadTexts:hwPerfRAIDReadThroughput.setUnits(_F)
_HwPerfRAIDWriteBandwidth_Type=Unsigned32
_HwPerfRAIDWriteBandwidth_Object=MibTableColumn
hwPerfRAIDWriteBandwidth=_HwPerfRAIDWriteBandwidth_Object((1,3,6,1,4,1,34774,4,1,22,11,1,6),_HwPerfRAIDWriteBandwidth_Type())
hwPerfRAIDWriteBandwidth.setMaxAccess(_C)
if mibBuilder.loadTexts:hwPerfRAIDWriteBandwidth.setStatus(_A)
if mibBuilder.loadTexts:hwPerfRAIDWriteBandwidth.setUnits(_E)
_HwPerfRAIDWriteThroughput_Type=Unsigned32
_HwPerfRAIDWriteThroughput_Object=MibTableColumn
hwPerfRAIDWriteThroughput=_HwPerfRAIDWriteThroughput_Object((1,3,6,1,4,1,34774,4,1,22,11,1,7),_HwPerfRAIDWriteThroughput_Type())
hwPerfRAIDWriteThroughput.setMaxAccess(_C)
if mibBuilder.loadTexts:hwPerfRAIDWriteThroughput.setStatus(_A)
if mibBuilder.loadTexts:hwPerfRAIDWriteThroughput.setUnits(_F)
_HwPerfControllerTable_Object=MibTable
hwPerfControllerTable=_HwPerfControllerTable_Object((1,3,6,1,4,1,34774,4,1,22,12))
if mibBuilder.loadTexts:hwPerfControllerTable.setStatus(_A)
_HwPerfControllerEntry_Object=MibTableRow
hwPerfControllerEntry=_HwPerfControllerEntry_Object((1,3,6,1,4,1,34774,4,1,22,12,1))
hwPerfControllerEntry.setIndexNames((0,_B,_Z))
if mibBuilder.loadTexts:hwPerfControllerEntry.setStatus(_A)
_HwPerfControllerID_Type=Unsigned32
_HwPerfControllerID_Object=MibTableColumn
hwPerfControllerID=_HwPerfControllerID_Object((1,3,6,1,4,1,34774,4,1,22,12,1,1),_HwPerfControllerID_Type())
hwPerfControllerID.setMaxAccess(_C)
if mibBuilder.loadTexts:hwPerfControllerID.setStatus(_A)
_HwPerfControllerCacheHit_Type=Unsigned32
_HwPerfControllerCacheHit_Object=MibTableColumn
hwPerfControllerCacheHit=_HwPerfControllerCacheHit_Object((1,3,6,1,4,1,34774,4,1,22,12,1,2),_HwPerfControllerCacheHit_Type())
hwPerfControllerCacheHit.setMaxAccess(_C)
if mibBuilder.loadTexts:hwPerfControllerCacheHit.setStatus(_A)
if mibBuilder.loadTexts:hwPerfControllerCacheHit.setUnits(_D)
_HwPerfControllerThroughput_Type=Unsigned32
_HwPerfControllerThroughput_Object=MibTableColumn
hwPerfControllerThroughput=_HwPerfControllerThroughput_Object((1,3,6,1,4,1,34774,4,1,22,12,1,3),_HwPerfControllerThroughput_Type())
hwPerfControllerThroughput.setMaxAccess(_C)
if mibBuilder.loadTexts:hwPerfControllerThroughput.setStatus(_A)
if mibBuilder.loadTexts:hwPerfControllerThroughput.setUnits(_F)
_HwPerfControllerReadBandwidth_Type=Unsigned32
_HwPerfControllerReadBandwidth_Object=MibTableColumn
hwPerfControllerReadBandwidth=_HwPerfControllerReadBandwidth_Object((1,3,6,1,4,1,34774,4,1,22,12,1,4),_HwPerfControllerReadBandwidth_Type())
hwPerfControllerReadBandwidth.setMaxAccess(_C)
if mibBuilder.loadTexts:hwPerfControllerReadBandwidth.setStatus(_A)
if mibBuilder.loadTexts:hwPerfControllerReadBandwidth.setUnits(_E)
_HwPerfControllerReadThroughput_Type=Unsigned32
_HwPerfControllerReadThroughput_Object=MibTableColumn
hwPerfControllerReadThroughput=_HwPerfControllerReadThroughput_Object((1,3,6,1,4,1,34774,4,1,22,12,1,5),_HwPerfControllerReadThroughput_Type())
hwPerfControllerReadThroughput.setMaxAccess(_C)
if mibBuilder.loadTexts:hwPerfControllerReadThroughput.setStatus(_A)
if mibBuilder.loadTexts:hwPerfControllerReadThroughput.setUnits(_F)
_HwPerfControllerWriteBandwidth_Type=Unsigned32
_HwPerfControllerWriteBandwidth_Object=MibTableColumn
hwPerfControllerWriteBandwidth=_HwPerfControllerWriteBandwidth_Object((1,3,6,1,4,1,34774,4,1,22,12,1,6),_HwPerfControllerWriteBandwidth_Type())
hwPerfControllerWriteBandwidth.setMaxAccess(_C)
if mibBuilder.loadTexts:hwPerfControllerWriteBandwidth.setStatus(_A)
if mibBuilder.loadTexts:hwPerfControllerWriteBandwidth.setUnits(_E)
_HwPerfControllerWriteThroughput_Type=Unsigned32
_HwPerfControllerWriteThroughput_Object=MibTableColumn
hwPerfControllerWriteThroughput=_HwPerfControllerWriteThroughput_Object((1,3,6,1,4,1,34774,4,1,22,12,1,7),_HwPerfControllerWriteThroughput_Type())
hwPerfControllerWriteThroughput.setMaxAccess(_C)
if mibBuilder.loadTexts:hwPerfControllerWriteThroughput.setStatus(_A)
if mibBuilder.loadTexts:hwPerfControllerWriteThroughput.setUnits(_F)
_HwPerfControllerCPUUsage_Type=Unsigned32
_HwPerfControllerCPUUsage_Object=MibTableColumn
hwPerfControllerCPUUsage=_HwPerfControllerCPUUsage_Object((1,3,6,1,4,1,34774,4,1,22,12,1,8),_HwPerfControllerCPUUsage_Type())
hwPerfControllerCPUUsage.setMaxAccess(_C)
if mibBuilder.loadTexts:hwPerfControllerCPUUsage.setStatus(_A)
if mibBuilder.loadTexts:hwPerfControllerCPUUsage.setUnits(_D)
_HwPerfControllerMemoryUsage_Type=Unsigned32
_HwPerfControllerMemoryUsage_Object=MibTableColumn
hwPerfControllerMemoryUsage=_HwPerfControllerMemoryUsage_Object((1,3,6,1,4,1,34774,4,1,22,12,1,9),_HwPerfControllerMemoryUsage_Type())
hwPerfControllerMemoryUsage.setMaxAccess(_C)
if mibBuilder.loadTexts:hwPerfControllerMemoryUsage.setStatus(_A)
if mibBuilder.loadTexts:hwPerfControllerMemoryUsage.setUnits(_D)
_HwPerfNASPortTable_Object=MibTable
hwPerfNASPortTable=_HwPerfNASPortTable_Object((1,3,6,1,4,1,34774,4,1,22,13))
if mibBuilder.loadTexts:hwPerfNASPortTable.setStatus(_A)
_HwPerfNASPortEntry_Object=MibTableRow
hwPerfNASPortEntry=_HwPerfNASPortEntry_Object((1,3,6,1,4,1,34774,4,1,22,13,1))
hwPerfNASPortEntry.setIndexNames((0,_B,_a))
if mibBuilder.loadTexts:hwPerfNASPortEntry.setStatus(_A)
_HwPerfNASPortIndex_Type=Unsigned32
_HwPerfNASPortIndex_Object=MibTableColumn
hwPerfNASPortIndex=_HwPerfNASPortIndex_Object((1,3,6,1,4,1,34774,4,1,22,13,1,1),_HwPerfNASPortIndex_Type())
hwPerfNASPortIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:hwPerfNASPortIndex.setStatus(_A)
_HwPerfNASPortCurrentBandwidth_Type=Unsigned32
_HwPerfNASPortCurrentBandwidth_Object=MibTableColumn
hwPerfNASPortCurrentBandwidth=_HwPerfNASPortCurrentBandwidth_Object((1,3,6,1,4,1,34774,4,1,22,13,1,2),_HwPerfNASPortCurrentBandwidth_Type())
hwPerfNASPortCurrentBandwidth.setMaxAccess(_C)
if mibBuilder.loadTexts:hwPerfNASPortCurrentBandwidth.setStatus(_A)
if mibBuilder.loadTexts:hwPerfNASPortCurrentBandwidth.setUnits(_E)
_HwPerfNASPortReadBandwidth_Type=Unsigned32
_HwPerfNASPortReadBandwidth_Object=MibTableColumn
hwPerfNASPortReadBandwidth=_HwPerfNASPortReadBandwidth_Object((1,3,6,1,4,1,34774,4,1,22,13,1,3),_HwPerfNASPortReadBandwidth_Type())
hwPerfNASPortReadBandwidth.setMaxAccess(_C)
if mibBuilder.loadTexts:hwPerfNASPortReadBandwidth.setStatus(_A)
if mibBuilder.loadTexts:hwPerfNASPortReadBandwidth.setUnits(_E)
_HwPerfNASPortWriteBandwidth_Type=Unsigned32
_HwPerfNASPortWriteBandwidth_Object=MibTableColumn
hwPerfNASPortWriteBandwidth=_HwPerfNASPortWriteBandwidth_Object((1,3,6,1,4,1,34774,4,1,22,13,1,4),_HwPerfNASPortWriteBandwidth_Type())
hwPerfNASPortWriteBandwidth.setMaxAccess(_C)
if mibBuilder.loadTexts:hwPerfNASPortWriteBandwidth.setStatus(_A)
if mibBuilder.loadTexts:hwPerfNASPortWriteBandwidth.setUnits(_E)
_HwPerfNASPortTotalPackages_Type=Unsigned32
_HwPerfNASPortTotalPackages_Object=MibTableColumn
hwPerfNASPortTotalPackages=_HwPerfNASPortTotalPackages_Object((1,3,6,1,4,1,34774,4,1,22,13,1,5),_HwPerfNASPortTotalPackages_Type())
hwPerfNASPortTotalPackages.setMaxAccess(_C)
if mibBuilder.loadTexts:hwPerfNASPortTotalPackages.setStatus(_A)
if mibBuilder.loadTexts:hwPerfNASPortTotalPackages.setUnits(_b)
_HwPerfNASPortInboundPackages_Type=Unsigned32
_HwPerfNASPortInboundPackages_Object=MibTableColumn
hwPerfNASPortInboundPackages=_HwPerfNASPortInboundPackages_Object((1,3,6,1,4,1,34774,4,1,22,13,1,6),_HwPerfNASPortInboundPackages_Type())
hwPerfNASPortInboundPackages.setMaxAccess(_C)
if mibBuilder.loadTexts:hwPerfNASPortInboundPackages.setStatus(_A)
if mibBuilder.loadTexts:hwPerfNASPortInboundPackages.setUnits(_b)
_HwPerfNASPortOutboundPackages_Type=Unsigned32
_HwPerfNASPortOutboundPackages_Object=MibTableColumn
hwPerfNASPortOutboundPackages=_HwPerfNASPortOutboundPackages_Object((1,3,6,1,4,1,34774,4,1,22,13,1,7),_HwPerfNASPortOutboundPackages_Type())
hwPerfNASPortOutboundPackages.setMaxAccess(_C)
if mibBuilder.loadTexts:hwPerfNASPortOutboundPackages.setStatus(_A)
if mibBuilder.loadTexts:hwPerfNASPortOutboundPackages.setUnits(_b)
_HwPerfNASPortDescription_Type=OctetString
_HwPerfNASPortDescription_Object=MibTableColumn
hwPerfNASPortDescription=_HwPerfNASPortDescription_Object((1,3,6,1,4,1,34774,4,1,22,13,1,8),_HwPerfNASPortDescription_Type())
hwPerfNASPortDescription.setMaxAccess(_C)
if mibBuilder.loadTexts:hwPerfNASPortDescription.setStatus(_A)
_HwInfoControllerBoardTable_Object=MibTable
hwInfoControllerBoardTable=_HwInfoControllerBoardTable_Object((1,3,6,1,4,1,34774,4,1,22,14))
if mibBuilder.loadTexts:hwInfoControllerBoardTable.setStatus(_A)
_HwInfoControllerBoardEntry_Object=MibTableRow
hwInfoControllerBoardEntry=_HwInfoControllerBoardEntry_Object((1,3,6,1,4,1,34774,4,1,22,14,1))
hwInfoControllerBoardEntry.setIndexNames((0,_B,_c))
if mibBuilder.loadTexts:hwInfoControllerBoardEntry.setStatus(_A)
_HwInfoControllerBoardID_Type=Unsigned32
_HwInfoControllerBoardID_Object=MibTableColumn
hwInfoControllerBoardID=_HwInfoControllerBoardID_Object((1,3,6,1,4,1,34774,4,1,22,14,1,1),_HwInfoControllerBoardID_Type())
hwInfoControllerBoardID.setMaxAccess(_C)
if mibBuilder.loadTexts:hwInfoControllerBoardID.setStatus(_A)
_HwInfoControllerBoardStatus_Type=Unsigned32
_HwInfoControllerBoardStatus_Object=MibTableColumn
hwInfoControllerBoardStatus=_HwInfoControllerBoardStatus_Object((1,3,6,1,4,1,34774,4,1,22,14,1,2),_HwInfoControllerBoardStatus_Type())
hwInfoControllerBoardStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:hwInfoControllerBoardStatus.setStatus(_A)
_HwInfoControllerBoardLogicVer_Type=OctetString
_HwInfoControllerBoardLogicVer_Object=MibTableColumn
hwInfoControllerBoardLogicVer=_HwInfoControllerBoardLogicVer_Object((1,3,6,1,4,1,34774,4,1,22,14,1,3),_HwInfoControllerBoardLogicVer_Type())
hwInfoControllerBoardLogicVer.setMaxAccess(_C)
if mibBuilder.loadTexts:hwInfoControllerBoardLogicVer.setStatus(_A)
_HwInfoControllerBoardPCBVer_Type=OctetString
_HwInfoControllerBoardPCBVer_Object=MibTableColumn
hwInfoControllerBoardPCBVer=_HwInfoControllerBoardPCBVer_Object((1,3,6,1,4,1,34774,4,1,22,14,1,4),_HwInfoControllerBoardPCBVer_Type())
hwInfoControllerBoardPCBVer.setMaxAccess(_C)
if mibBuilder.loadTexts:hwInfoControllerBoardPCBVer.setStatus(_A)
_HwInfoControllerBoardBIOSVer_Type=OctetString
_HwInfoControllerBoardBIOSVer_Object=MibTableColumn
hwInfoControllerBoardBIOSVer=_HwInfoControllerBoardBIOSVer_Object((1,3,6,1,4,1,34774,4,1,22,14,1,5),_HwInfoControllerBoardBIOSVer_Type())
hwInfoControllerBoardBIOSVer.setMaxAccess(_C)
if mibBuilder.loadTexts:hwInfoControllerBoardBIOSVer.setStatus(_A)
_HwInfoControllerBoardELabel_Type=OctetString
_HwInfoControllerBoardELabel_Object=MibTableColumn
hwInfoControllerBoardELabel=_HwInfoControllerBoardELabel_Object((1,3,6,1,4,1,34774,4,1,22,14,1,6),_HwInfoControllerBoardELabel_Type())
hwInfoControllerBoardELabel.setMaxAccess(_C)
if mibBuilder.loadTexts:hwInfoControllerBoardELabel.setStatus(_A)
_HwInfoControllerBoardType_Type=Unsigned32
_HwInfoControllerBoardType_Object=MibTableColumn
hwInfoControllerBoardType=_HwInfoControllerBoardType_Object((1,3,6,1,4,1,34774,4,1,22,14,1,7),_HwInfoControllerBoardType_Type())
hwInfoControllerBoardType.setMaxAccess(_C)
if mibBuilder.loadTexts:hwInfoControllerBoardType.setStatus(_A)
_HwInfoFileSystemTable_Object=MibTable
hwInfoFileSystemTable=_HwInfoFileSystemTable_Object((1,3,6,1,4,1,34774,4,1,22,15))
if mibBuilder.loadTexts:hwInfoFileSystemTable.setStatus(_A)
_HwInfoFileSystemEntry_Object=MibTableRow
hwInfoFileSystemEntry=_HwInfoFileSystemEntry_Object((1,3,6,1,4,1,34774,4,1,22,15,1))
hwInfoFileSystemEntry.setIndexNames((0,_B,_d))
if mibBuilder.loadTexts:hwInfoFileSystemEntry.setStatus(_A)
_HwInfoFileSystemName_Type=OctetString
_HwInfoFileSystemName_Object=MibTableColumn
hwInfoFileSystemName=_HwInfoFileSystemName_Object((1,3,6,1,4,1,34774,4,1,22,15,1,1),_HwInfoFileSystemName_Type())
hwInfoFileSystemName.setMaxAccess(_C)
if mibBuilder.loadTexts:hwInfoFileSystemName.setStatus(_A)
_HwInfoFileSystemStatus_Type=OctetString
_HwInfoFileSystemStatus_Object=MibTableColumn
hwInfoFileSystemStatus=_HwInfoFileSystemStatus_Object((1,3,6,1,4,1,34774,4,1,22,15,1,2),_HwInfoFileSystemStatus_Type())
hwInfoFileSystemStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:hwInfoFileSystemStatus.setStatus(_A)
_HwInfoFileSystemSize_Type=OctetString
_HwInfoFileSystemSize_Object=MibTableColumn
hwInfoFileSystemSize=_HwInfoFileSystemSize_Object((1,3,6,1,4,1,34774,4,1,22,15,1,3),_HwInfoFileSystemSize_Type())
hwInfoFileSystemSize.setMaxAccess(_C)
if mibBuilder.loadTexts:hwInfoFileSystemSize.setStatus(_A)
_HwInfoFileSystemLayout_Type=OctetString
_HwInfoFileSystemLayout_Object=MibTableColumn
hwInfoFileSystemLayout=_HwInfoFileSystemLayout_Object((1,3,6,1,4,1,34774,4,1,22,15,1,4),_HwInfoFileSystemLayout_Type())
hwInfoFileSystemLayout.setMaxAccess(_C)
if mibBuilder.loadTexts:hwInfoFileSystemLayout.setStatus(_A)
if mibBuilder.loadTexts:hwInfoFileSystemLayout.setUnits(_g)
_HwInfoFileSystemMirrors_Type=Unsigned32
_HwInfoFileSystemMirrors_Object=MibTableColumn
hwInfoFileSystemMirrors=_HwInfoFileSystemMirrors_Object((1,3,6,1,4,1,34774,4,1,22,15,1,5),_HwInfoFileSystemMirrors_Type())
hwInfoFileSystemMirrors.setMaxAccess(_C)
if mibBuilder.loadTexts:hwInfoFileSystemMirrors.setStatus(_A)
_HwInfoFileSystemColumns_Type=Unsigned32
_HwInfoFileSystemColumns_Object=MibTableColumn
hwInfoFileSystemColumns=_HwInfoFileSystemColumns_Object((1,3,6,1,4,1,34774,4,1,22,15,1,6),_HwInfoFileSystemColumns_Type())
hwInfoFileSystemColumns.setMaxAccess(_C)
if mibBuilder.loadTexts:hwInfoFileSystemColumns.setStatus(_A)
_HwInfoFileSystemUsage_Type=OctetString
_HwInfoFileSystemUsage_Object=MibTableColumn
hwInfoFileSystemUsage=_HwInfoFileSystemUsage_Object((1,3,6,1,4,1,34774,4,1,22,15,1,7),_HwInfoFileSystemUsage_Type())
hwInfoFileSystemUsage.setMaxAccess(_C)
if mibBuilder.loadTexts:hwInfoFileSystemUsage.setStatus(_A)
_HwInfoFileSystemNFSShared_Type=OctetString
_HwInfoFileSystemNFSShared_Object=MibTableColumn
hwInfoFileSystemNFSShared=_HwInfoFileSystemNFSShared_Object((1,3,6,1,4,1,34774,4,1,22,15,1,8),_HwInfoFileSystemNFSShared_Type())
hwInfoFileSystemNFSShared.setMaxAccess(_C)
if mibBuilder.loadTexts:hwInfoFileSystemNFSShared.setStatus(_A)
_HwInfoFileSystemCIFSShared_Type=OctetString
_HwInfoFileSystemCIFSShared_Object=MibTableColumn
hwInfoFileSystemCIFSShared=_HwInfoFileSystemCIFSShared_Object((1,3,6,1,4,1,34774,4,1,22,15,1,9),_HwInfoFileSystemCIFSShared_Type())
hwInfoFileSystemCIFSShared.setMaxAccess(_C)
if mibBuilder.loadTexts:hwInfoFileSystemCIFSShared.setStatus(_A)
_HwInfoFileSystemSecondaryTier_Type=OctetString
_HwInfoFileSystemSecondaryTier_Object=MibTableColumn
hwInfoFileSystemSecondaryTier=_HwInfoFileSystemSecondaryTier_Object((1,3,6,1,4,1,34774,4,1,22,15,1,10),_HwInfoFileSystemSecondaryTier_Type())
hwInfoFileSystemSecondaryTier.setMaxAccess(_C)
if mibBuilder.loadTexts:hwInfoFileSystemSecondaryTier.setStatus(_A)
_HwInfoFileSystemPoolList_Type=OctetString
_HwInfoFileSystemPoolList_Object=MibTableColumn
hwInfoFileSystemPoolList=_HwInfoFileSystemPoolList_Object((1,3,6,1,4,1,34774,4,1,22,15,1,11),_HwInfoFileSystemPoolList_Type())
hwInfoFileSystemPoolList.setMaxAccess(_C)
if mibBuilder.loadTexts:hwInfoFileSystemPoolList.setStatus(_A)
_HwInfoClusterNodesTable_Object=MibTable
hwInfoClusterNodesTable=_HwInfoClusterNodesTable_Object((1,3,6,1,4,1,34774,4,1,22,16))
if mibBuilder.loadTexts:hwInfoClusterNodesTable.setStatus(_A)
_HwInfoClusterNodesEntry_Object=MibTableRow
hwInfoClusterNodesEntry=_HwInfoClusterNodesEntry_Object((1,3,6,1,4,1,34774,4,1,22,16,1))
hwInfoClusterNodesEntry.setIndexNames((0,_B,_e))
if mibBuilder.loadTexts:hwInfoClusterNodesEntry.setStatus(_A)
_HwInfoClusterNodesID_Type=Unsigned32
_HwInfoClusterNodesID_Object=MibTableColumn
hwInfoClusterNodesID=_HwInfoClusterNodesID_Object((1,3,6,1,4,1,34774,4,1,22,16,1,1),_HwInfoClusterNodesID_Type())
hwInfoClusterNodesID.setMaxAccess(_C)
if mibBuilder.loadTexts:hwInfoClusterNodesID.setStatus(_A)
_HwInfoClusterNodesName_Type=OctetString
_HwInfoClusterNodesName_Object=MibTableColumn
hwInfoClusterNodesName=_HwInfoClusterNodesName_Object((1,3,6,1,4,1,34774,4,1,22,16,1,2),_HwInfoClusterNodesName_Type())
hwInfoClusterNodesName.setMaxAccess(_C)
if mibBuilder.loadTexts:hwInfoClusterNodesName.setStatus(_A)
_HwInfoClusterNodesIsMaster_Type=Unsigned32
_HwInfoClusterNodesIsMaster_Object=MibTableColumn
hwInfoClusterNodesIsMaster=_HwInfoClusterNodesIsMaster_Object((1,3,6,1,4,1,34774,4,1,22,16,1,3),_HwInfoClusterNodesIsMaster_Type())
hwInfoClusterNodesIsMaster.setMaxAccess(_C)
if mibBuilder.loadTexts:hwInfoClusterNodesIsMaster.setStatus(_A)
_HwInfoClusterNodesStatus_Type=Unsigned32
_HwInfoClusterNodesStatus_Object=MibTableColumn
hwInfoClusterNodesStatus=_HwInfoClusterNodesStatus_Object((1,3,6,1,4,1,34774,4,1,22,16,1,4),_HwInfoClusterNodesStatus_Type())
hwInfoClusterNodesStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:hwInfoClusterNodesStatus.setStatus(_A)
_HwInfoClusterNodesRuningStatus_Type=Unsigned32
_HwInfoClusterNodesRuningStatus_Object=MibTableColumn
hwInfoClusterNodesRuningStatus=_HwInfoClusterNodesRuningStatus_Object((1,3,6,1,4,1,34774,4,1,22,16,1,5),_HwInfoClusterNodesRuningStatus_Type())
hwInfoClusterNodesRuningStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:hwInfoClusterNodesRuningStatus.setStatus(_A)
if mibBuilder.loadTexts:hwInfoClusterNodesRuningStatus.setUnits('0.1V')
_HwInfoClusterNodesIP_Type=OctetString
_HwInfoClusterNodesIP_Object=MibTableColumn
hwInfoClusterNodesIP=_HwInfoClusterNodesIP_Object((1,3,6,1,4,1,34774,4,1,22,16,1,6),_HwInfoClusterNodesIP_Type())
hwInfoClusterNodesIP.setMaxAccess(_C)
if mibBuilder.loadTexts:hwInfoClusterNodesIP.setStatus(_A)
_HwInfoNasControllerTable_Object=MibTable
hwInfoNasControllerTable=_HwInfoNasControllerTable_Object((1,3,6,1,4,1,34774,4,1,22,17))
if mibBuilder.loadTexts:hwInfoNasControllerTable.setStatus(_A)
_HwInfoNasControllerEntry_Object=MibTableRow
hwInfoNasControllerEntry=_HwInfoNasControllerEntry_Object((1,3,6,1,4,1,34774,4,1,22,17,1))
hwInfoNasControllerEntry.setIndexNames((0,_B,_f))
if mibBuilder.loadTexts:hwInfoNasControllerEntry.setStatus(_A)
_HwInfoNasControllerName_Type=OctetString
_HwInfoNasControllerName_Object=MibTableColumn
hwInfoNasControllerName=_HwInfoNasControllerName_Object((1,3,6,1,4,1,34774,4,1,22,17,1,1),_HwInfoNasControllerName_Type())
hwInfoNasControllerName.setMaxAccess(_C)
if mibBuilder.loadTexts:hwInfoNasControllerName.setStatus(_A)
_HwInfoNasControllerBarCode_Type=OctetString
_HwInfoNasControllerBarCode_Object=MibTableColumn
hwInfoNasControllerBarCode=_HwInfoNasControllerBarCode_Object((1,3,6,1,4,1,34774,4,1,22,17,1,2),_HwInfoNasControllerBarCode_Type())
hwInfoNasControllerBarCode.setMaxAccess(_C)
if mibBuilder.loadTexts:hwInfoNasControllerBarCode.setStatus(_A)
_HwInfoNasControllerFirmwareVersion_Type=OctetString
_HwInfoNasControllerFirmwareVersion_Object=MibTableColumn
hwInfoNasControllerFirmwareVersion=_HwInfoNasControllerFirmwareVersion_Object((1,3,6,1,4,1,34774,4,1,22,17,1,3),_HwInfoNasControllerFirmwareVersion_Type())
hwInfoNasControllerFirmwareVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:hwInfoNasControllerFirmwareVersion.setStatus(_A)
_HwInfoNasControllerDescription_Type=OctetString
_HwInfoNasControllerDescription_Object=MibTableColumn
hwInfoNasControllerDescription=_HwInfoNasControllerDescription_Object((1,3,6,1,4,1,34774,4,1,22,17,1,4),_HwInfoNasControllerDescription_Type())
hwInfoNasControllerDescription.setMaxAccess(_C)
if mibBuilder.loadTexts:hwInfoNasControllerDescription.setStatus(_A)
_IsoConformance_ObjectIdentity=ObjectIdentity
isoConformance=_IsoConformance_ObjectIdentity((1,6))
_IsoGroups_ObjectIdentity=ObjectIdentity
isoGroups=_IsoGroups_ObjectIdentity((1,6,1))
_IsoCompliances_ObjectIdentity=ObjectIdentity
isoCompliances=_IsoCompliances_ObjectIdentity((1,6,2))
currentObjectGroup=ObjectGroup((1,6,1,1))
currentObjectGroup.setObjects(*((_B,_c),(_B,_h),(_B,_i),(_B,_j),(_B,_k),(_B,_l),(_B,_m),(_B,_a),(_B,_n),(_B,_o),(_B,_p),(_B,_q),(_B,_r),(_B,_s),(_B,_I),(_B,_J),(_B,_t),(_B,_u),(_B,_v),(_B,_w),(_B,_x),(_B,_y),(_B,_z),(_B,_A0),(_B,_A1),(_B,_K),(_B,_L),(_B,_A2),(_B,_A3),(_B,_A4),(_B,_W),(_B,_A5),(_B,_A6),(_B,_A7),(_B,_A8),(_B,_A9),(_B,_Y),(_B,_AA),(_B,_AB),(_B,_AC),(_B,_AD),(_B,_AE),(_B,_AF),(_B,_AG),(_B,_AH),(_B,_AI),(_B,_AJ),(_B,_AK),(_B,_AL),(_B,_AM),(_B,_AN),(_B,_AO),(_B,_N),(_B,_AP),(_B,_AQ),(_B,_AR),(_B,_AS),(_B,_AT),(_B,_P),(_B,_AU),(_B,_AV),(_B,_AW),(_B,_AX),(_B,_AY),(_B,_AZ),(_B,_Aa),(_B,_R),(_B,_S),(_B,_T),(_B,_Ab),(_B,_Ac),(_B,_Ad),(_B,_Ae),(_B,_Af),(_B,_Ag),(_B,_Ah),(_B,_Ai),(_B,_H),(_B,_M),(_B,_Aj),(_B,_Ak),(_B,_Al),(_B,_O),(_B,_Am),(_B,_An),(_B,_Q),(_B,_U),(_B,_V),(_B,_Ao),(_B,_Ap),(_B,_Z),(_B,_Aq),(_B,_Ar),(_B,_As),(_B,_At),(_B,_Au),(_B,_Av),(_B,_Aw),(_B,_Ax),(_B,_Ay),(_B,_Az),(_B,_A_),(_B,_B0),(_B,_B1),(_B,_B2),(_B,_B3),(_B,_d),(_B,_B4),(_B,_B5),(_B,_B6),(_B,_B7),(_B,_B8),(_B,_B9),(_B,_BA),(_B,_BB),(_B,_BC),(_B,_BD),(_B,_e),(_B,_BE),(_B,_BF),(_B,_BG),(_B,_BH),(_B,_BI),(_B,_f),(_B,_BJ),(_B,_BK),(_B,_BL),(_B,_BM),(_B,_X),(_B,_BN),(_B,_BO),(_B,_BP),(_B,_BQ),(_B,_BR),(_B,_BS),(_B,_BT),(_B,_BU),(_B,_BV),(_B,_BW),(_B,_BX),(_B,_BY)))
if mibBuilder.loadTexts:currentObjectGroup.setStatus(_A)
basicCompliance=ModuleCompliance((1,6,2,1))
basicCompliance.setObjects((_B,_BZ))
if mibBuilder.loadTexts:basicCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'NodeCodeString':NodeCodeString,'huaweistorage':huaweistorage,'hwStorage':hwStorage,'hwISM':hwISM,'hwMIB':hwMIB,'hwInfoControllerTable':hwInfoControllerTable,'hwInfoControllerEntry':hwInfoControllerEntry,_H:hwInfoControllerID,_AJ:hwInfoControllerIP,_AK:hwInfoControllerIsMaster,_AL:hwInfoControllerCpuUsingRatio,_AM:hwInfoControllerMemoryUsingRatio,_AN:hwInfoControllerVersion,_AO:hwInfoControllerStatus,_B0:hwInfoControllerDescription,'hwInfoPhysicDiskTable':hwInfoPhysicDiskTable,'hwInfoPhysicDiskEntry':hwInfoPhysicDiskEntry,_I:hwInfoPhysicDiskFrameID,_J:hwInfoPhysicDiskSlotID,_t:hwInfoPhysicDiskStatus,_u:hwInfoPhysicDiskSZType,_v:hwInfoPhysicDiskSZVendor,_w:hwInfoPhysicDiskSZModel,_x:hwInfoPhysicDiskSZSerial,_y:hwInfoPhysicDiskSZFirmware,_z:hwInfoPhysicDiskSpinSpeed,_A0:hwInfoPhysicDiskCurrentSpeed,_A1:hwInfoPhysicDiskRawCapacity,'hwInfoLogicDiskTable':hwInfoLogicDiskTable,'hwInfoLogicDiskEntry':hwInfoLogicDiskEntry,_K:hwInfoLogicDiskFrameID,_L:hwInfoLogicDiskSlotID,_A2:hwInfoLogicDiskLogicStatus,_A3:hwInfoLogicDiskLogicType,_A4:hwInfoLogicDiskSize,'hwInfoPowerTable':hwInfoPowerTable,'hwInfoPowerEntry':hwInfoPowerEntry,_M:hwInfoPowerID,_N:hwInfoPowerSubrackID,_Aj:hwInfoPowerStatus,_AP:hwInfoPowerTemperature,_Ak:hwInfoPowerVendor,_AQ:hwInfoPowerModle,_AR:hwInfoPowerVersion,_AS:hwInfoPowerDate,_Al:hwInfoPowerType,_AT:hwInfoPowerSN,_Ax:hwInfoPowerDisplayID,_B1:hwInfoPowerDescription,'hwInfoBBUTable':hwInfoBBUTable,'hwInfoBBUEntry':hwInfoBBUEntry,_O:hwInfoBBUID,_P:hwInfoBBUControllerID,_AU:hwInfoBBUPresentStatus,_Am:hwInfoBBUStatus,_An:hwInfoBBUCurrentVoltage,_AV:hwInfoBBUIsChargeFull,_AW:hwInfoBBUDischargeTime,_AX:hwInfoBBURemainLife,_AY:hwInfoBBUFWVersion,_AZ:hwInfoBBUELable,_Aa:hwInfoBBUChargeState,'hwInfoFanTable':hwInfoFanTable,'hwInfoFanEntry':hwInfoFanEntry,_Q:hwInfoFanID,_R:hwInfoFanSubrackId,_AG:hwInfoFanRunningStatus,_AH:hwInfoFanRunningLevel,_AI:hwInfoFanRunningSection,_Ay:hwInfoFanELable,_B2:hwInfoFanDescription,'hwInfoExpBoardTable':hwInfoExpBoardTable,'hwInfoExpBoardEntry':hwInfoExpBoardEntry,_T:hwInfoExpBoardSubrackID,_S:hwInfoExpBoardID,_Ab:hwInfoExpBoardStatus,_Ac:hwInfoExpBoardLogicVersion,_Ad:hwInfoExpBoardPCBversion,_Ae:hwInfoExpBoardProduceInfo,_Af:hwInfoExpBoardType,'hwInfoInterfaceTable':hwInfoInterfaceTable,'hwInfoInterfaceEntry':hwInfoInterfaceEntry,_U:hwInfoInterfaceID,_V:hwInfoInterfaceControllerID,_Ao:hwInfoInterfaceType,_Ap:hwInfoInterfaceStatus,_Ag:hwInfoInterfaceLogicVersion,_Ah:hwInfoInterfacePCBVersion,_Ai:hwInfoInterfaceVendorInfo,_B3:hwInfoInterfaceDescription,'hwInfoRAIDTable':hwInfoRAIDTable,'hwInfoRAIDEntry':hwInfoRAIDEntry,_W:hwInfoRAIDID,_A5:hwInfoRAIDName,_A6:hwInfoRAIDLevel,_A7:hwInfoRAIDFreeCapacity,_A8:hwInfoRAIDStatus,_A9:hwInfoRAIDDiskList,_Az:hwInfoRAIDTotalSize,'hwInfoCacheTable':hwInfoCacheTable,'hwInfoCacheEntry':hwInfoCacheEntry,_X:hwInfoCacheID,_BN:hwInfoCacheTotalMemoryCapacity,_BO:hwInfoCacheSystemMemoryCapacity,_BP:hwInfoCacheCacheCapacity,_BQ:hwInfoCacheCacheUtilization,_BR:hwInfoCacheCacheHitRatio,_BS:hwInfoCacheCurrentCacheWaterLevel,_BT:hwInfoCacheCacheHighWaterLevel,_BU:hwInfoCacheCacheLowWaterLevel,_BV:hwInfoCacheReadCacheUtility,_BW:hwInfoCacheWriteCacheUtililty,_BX:hwInfoCacheMirroringWriteCacheUtility,_BY:hwInfoCacheWhetherDirtyDataExists,'hwPerfRAIDTable':hwPerfRAIDTable,'hwPerfRAIDEntry':hwPerfRAIDEntry,_Y:hwPerfRAIDID,_AA:hwPerfRAIDCurrentBandwidth,_AB:hwPerfRAIDThroughput,_AC:hwPerfRAIDReadBandwidth,_AD:hwPerfRAIDReadThroughput,_AE:hwPerfRAIDWriteBandwidth,_AF:hwPerfRAIDWriteThroughput,'hwPerfControllerTable':hwPerfControllerTable,'hwPerfControllerEntry':hwPerfControllerEntry,_Z:hwPerfControllerID,_Aq:hwPerfControllerCacheHit,_Ar:hwPerfControllerThroughput,_As:hwPerfControllerReadBandwidth,_At:hwPerfControllerReadThroughput,_Au:hwPerfControllerWriteBandwidth,_Av:hwPerfControllerWriteThroughput,_Aw:hwPerfControllerCPUUsage,_BM:hwPerfControllerMemoryUsage,'hwPerfNASPortTable':hwPerfNASPortTable,'hwPerfNASPortEntry':hwPerfNASPortEntry,_a:hwPerfNASPortIndex,_n:hwPerfNASPortCurrentBandwidth,_o:hwPerfNASPortReadBandwidth,_p:hwPerfNASPortWriteBandwidth,_q:hwPerfNASPortTotalPackages,_r:hwPerfNASPortInboundPackages,_s:hwPerfNASPortOutboundPackages,_A_:hwPerfNASPortDescription,'hwInfoControllerBoardTable':hwInfoControllerBoardTable,'hwInfoControllerBoardEntry':hwInfoControllerBoardEntry,_c:hwInfoControllerBoardID,_i:hwInfoControllerBoardStatus,_j:hwInfoControllerBoardLogicVer,_k:hwInfoControllerBoardPCBVer,_l:hwInfoControllerBoardBIOSVer,_m:hwInfoControllerBoardELabel,_h:hwInfoControllerBoardType,'hwInfoFileSystemTable':hwInfoFileSystemTable,'hwInfoFileSystemEntry':hwInfoFileSystemEntry,_d:hwInfoFileSystemName,_B4:hwInfoFileSystemStatus,_B5:hwInfoFileSystemSize,_B6:hwInfoFileSystemLayout,_B7:hwInfoFileSystemMirrors,_B8:hwInfoFileSystemColumns,_B9:hwInfoFileSystemUsage,_BA:hwInfoFileSystemNFSShared,_BB:hwInfoFileSystemCIFSShared,_BC:hwInfoFileSystemSecondaryTier,_BD:hwInfoFileSystemPoolList,'hwInfoClusterNodesTable':hwInfoClusterNodesTable,'hwInfoClusterNodesEntry':hwInfoClusterNodesEntry,_e:hwInfoClusterNodesID,_BE:hwInfoClusterNodesName,_BF:hwInfoClusterNodesIsMaster,_BG:hwInfoClusterNodesStatus,_BH:hwInfoClusterNodesRuningStatus,_BI:hwInfoClusterNodesIP,'hwInfoNasControllerTable':hwInfoNasControllerTable,'hwInfoNasControllerEntry':hwInfoNasControllerEntry,_f:hwInfoNasControllerName,_BJ:hwInfoNasControllerBarCode,_BK:hwInfoNasControllerFirmwareVersion,_BL:hwInfoNasControllerDescription,'isoConformance':isoConformance,'isoGroups':isoGroups,_BZ:currentObjectGroup,'isoCompliances':isoCompliances,'basicCompliance':basicCompliance})