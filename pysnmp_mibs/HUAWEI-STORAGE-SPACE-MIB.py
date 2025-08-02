_AI='currentObjectGroup'
_AH='hwInfoLunUsageType'
_AG='hwInfoLunGroupLunList'
_AF='hwInfoHostGroupHostList'
_AE='hwInfoPortGroupPortList'
_AD='hwInfoPortGroupName'
_AC='hwInfoStoragePoolDiskDomainName'
_AB='hwInfoLunRemoteLUNWWN'
_AA='hwInfoLunDIFSwitch'
_A9='hwInfoLunIsAddToLunGroup'
_A8='hwInfoLunWorkController'
_A7='hwInfoLunOwnerController'
_A6='hwInfoLunPrefetchValue'
_A5='hwInfoLunPrefetchPolicy'
_A4='hwInfoLunRunningWritePolicy'
_A3='hwInfoLunWritePolicy'
_A2='hwInfoLunExposedToInitiator'
_A1='hwInfoLunWWN'
_A0='hwInfoLunIOPriority'
_z='hwInfoLunType'
_y='hwInfoLunRunningStatus'
_x='hwInfoLunHealthStatus'
_w='hwInfoLunSectorSize'
_v='hwInfoLunProtectionCapacity'
_u='hwInfoLunSubscribedCapacity'
_t='hwInfoLunCapacity'
_s='hwInfoLunPoolName'
_r='hwInfoLunPoolID'
_q='hwInfoLunName'
_p='hwInfoLunGroupName'
_o='hwInfoHostGroupName'
_n='hwInfoHostNetworkName'
_m='hwInfoHostModel'
_l='hwInfoHostIPAddress'
_k='hwInfoHostOperatingSystem'
_j='hwInfoHostRunningStatus'
_i='hwInfoHostHealthStatus'
_h='hwInfoHostLocation'
_g='hwInfoHostName'
_f='hwInfoStoragePoolFullThreshold'
_e='hwInfoStoragePoolTier0Capacity'
_d='hwInfoStoragePoolFreeCapacity'
_c='hwInfoStoragePoolSubscribedCapacity'
_b='hwInfoStoragePoolTotalCapacity'
_a='hwInfoStoragePoolRunningStatus'
_Z='hwInfoStoragePoolHealthStatus'
_Y='hwInfoStoragePoolDiskDomainID'
_X='hwInfoStoragePoolName'
_W='hwInfoDiskDomainTier0HotSpareStrategy'
_V='hwInfoDiskDomainTier0UsedHotSpareCapacity'
_U='hwInfoDiskDomainTier0HotSpareCapacity'
_T='hwInfoDiskDomainTier0FreeCapacity'
_S='hwInfoDiskDomainTier0TotalCapacity'
_R='hwInfoDiskDomainTier0DiskNumber'
_Q='hwInfoDiskDomainUsedHotSpareCapacity'
_P='hwInfoDiskDomainHotSpareCapacity'
_O='hwInfoDiskDomainFreeCapacity'
_N='hwInfoDiskDomainTotalCapacity'
_M='hwInfoDiskDomainRunningStatus'
_L='hwInfoDiskDomainHealthStatus'
_K='hwInfoDiskDomainName'
_J='hwInfoLunID'
_I='hwInfoLunGroupID'
_H='hwInfoHostGroupID'
_G='hwInfoHostID'
_F='hwInfoPortGroupID'
_E='hwInfoStoragePoolID'
_D='hwInfoDiskDomainID'
_C='read-only'
_B='HUAWEI-STORAGE-SPACE-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
hwStorage=ModuleIdentity((1,3,6,1,4,1,34774,4))
if mibBuilder.loadTexts:hwStorage.setRevisions(('2013-04-06 13:54',))
class NodeCodeString(TextualConvention,OctetString):status=_A;displayHint='255a';subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(15,17))
_Huaweistorage_ObjectIdentity=ObjectIdentity
huaweistorage=_Huaweistorage_ObjectIdentity((1,3,6,1,4,1,34774))
_HwISM_ObjectIdentity=ObjectIdentity
hwISM=_HwISM_ObjectIdentity((1,3,6,1,4,1,34774,4,1))
_HwStorageDevice_ObjectIdentity=ObjectIdentity
hwStorageDevice=_HwStorageDevice_ObjectIdentity((1,3,6,1,4,1,34774,4,1,23))
_HwSpaceInfo_ObjectIdentity=ObjectIdentity
hwSpaceInfo=_HwSpaceInfo_ObjectIdentity((1,3,6,1,4,1,34774,4,1,23,4))
_HwInfoDiskDomainTable_Object=MibTable
hwInfoDiskDomainTable=_HwInfoDiskDomainTable_Object((1,3,6,1,4,1,34774,4,1,23,4,1))
if mibBuilder.loadTexts:hwInfoDiskDomainTable.setStatus(_A)
_HwInfoDiskDomainEntry_Object=MibTableRow
hwInfoDiskDomainEntry=_HwInfoDiskDomainEntry_Object((1,3,6,1,4,1,34774,4,1,23,4,1,1))
hwInfoDiskDomainEntry.setIndexNames((0,_B,_D))
if mibBuilder.loadTexts:hwInfoDiskDomainEntry.setStatus(_A)
_HwInfoDiskDomainID_Type=OctetString
_HwInfoDiskDomainID_Object=MibTableColumn
hwInfoDiskDomainID=_HwInfoDiskDomainID_Object((1,3,6,1,4,1,34774,4,1,23,4,1,1,1),_HwInfoDiskDomainID_Type())
hwInfoDiskDomainID.setMaxAccess(_C)
if mibBuilder.loadTexts:hwInfoDiskDomainID.setStatus(_A)
_HwInfoDiskDomainName_Type=OctetString
_HwInfoDiskDomainName_Object=MibTableColumn
hwInfoDiskDomainName=_HwInfoDiskDomainName_Object((1,3,6,1,4,1,34774,4,1,23,4,1,1,2),_HwInfoDiskDomainName_Type())
hwInfoDiskDomainName.setMaxAccess(_C)
if mibBuilder.loadTexts:hwInfoDiskDomainName.setStatus(_A)
_HwInfoDiskDomainHealthStatus_Type=Unsigned32
_HwInfoDiskDomainHealthStatus_Object=MibTableColumn
hwInfoDiskDomainHealthStatus=_HwInfoDiskDomainHealthStatus_Object((1,3,6,1,4,1,34774,4,1,23,4,1,1,3),_HwInfoDiskDomainHealthStatus_Type())
hwInfoDiskDomainHealthStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:hwInfoDiskDomainHealthStatus.setStatus(_A)
_HwInfoDiskDomainRunningStatus_Type=Unsigned32
_HwInfoDiskDomainRunningStatus_Object=MibTableColumn
hwInfoDiskDomainRunningStatus=_HwInfoDiskDomainRunningStatus_Object((1,3,6,1,4,1,34774,4,1,23,4,1,1,4),_HwInfoDiskDomainRunningStatus_Type())
hwInfoDiskDomainRunningStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:hwInfoDiskDomainRunningStatus.setStatus(_A)
_HwInfoDiskDomainTotalCapacity_Type=Counter64
_HwInfoDiskDomainTotalCapacity_Object=MibTableColumn
hwInfoDiskDomainTotalCapacity=_HwInfoDiskDomainTotalCapacity_Object((1,3,6,1,4,1,34774,4,1,23,4,1,1,5),_HwInfoDiskDomainTotalCapacity_Type())
hwInfoDiskDomainTotalCapacity.setMaxAccess(_C)
if mibBuilder.loadTexts:hwInfoDiskDomainTotalCapacity.setStatus(_A)
_HwInfoDiskDomainFreeCapacity_Type=Counter64
_HwInfoDiskDomainFreeCapacity_Object=MibTableColumn
hwInfoDiskDomainFreeCapacity=_HwInfoDiskDomainFreeCapacity_Object((1,3,6,1,4,1,34774,4,1,23,4,1,1,6),_HwInfoDiskDomainFreeCapacity_Type())
hwInfoDiskDomainFreeCapacity.setMaxAccess(_C)
if mibBuilder.loadTexts:hwInfoDiskDomainFreeCapacity.setStatus(_A)
_HwInfoDiskDomainHotSpareCapacity_Type=Counter64
_HwInfoDiskDomainHotSpareCapacity_Object=MibTableColumn
hwInfoDiskDomainHotSpareCapacity=_HwInfoDiskDomainHotSpareCapacity_Object((1,3,6,1,4,1,34774,4,1,23,4,1,1,7),_HwInfoDiskDomainHotSpareCapacity_Type())
hwInfoDiskDomainHotSpareCapacity.setMaxAccess(_C)
if mibBuilder.loadTexts:hwInfoDiskDomainHotSpareCapacity.setStatus(_A)
_HwInfoDiskDomainUsedHotSpareCapacity_Type=Counter64
_HwInfoDiskDomainUsedHotSpareCapacity_Object=MibTableColumn
hwInfoDiskDomainUsedHotSpareCapacity=_HwInfoDiskDomainUsedHotSpareCapacity_Object((1,3,6,1,4,1,34774,4,1,23,4,1,1,8),_HwInfoDiskDomainUsedHotSpareCapacity_Type())
hwInfoDiskDomainUsedHotSpareCapacity.setMaxAccess(_C)
if mibBuilder.loadTexts:hwInfoDiskDomainUsedHotSpareCapacity.setStatus(_A)
_HwInfoDiskDomainTier0DiskNumber_Type=Unsigned32
_HwInfoDiskDomainTier0DiskNumber_Object=MibTableColumn
hwInfoDiskDomainTier0DiskNumber=_HwInfoDiskDomainTier0DiskNumber_Object((1,3,6,1,4,1,34774,4,1,23,4,1,1,9),_HwInfoDiskDomainTier0DiskNumber_Type())
hwInfoDiskDomainTier0DiskNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:hwInfoDiskDomainTier0DiskNumber.setStatus(_A)
_HwInfoDiskDomainTier0TotalCapacity_Type=Counter64
_HwInfoDiskDomainTier0TotalCapacity_Object=MibTableColumn
hwInfoDiskDomainTier0TotalCapacity=_HwInfoDiskDomainTier0TotalCapacity_Object((1,3,6,1,4,1,34774,4,1,23,4,1,1,10),_HwInfoDiskDomainTier0TotalCapacity_Type())
hwInfoDiskDomainTier0TotalCapacity.setMaxAccess(_C)
if mibBuilder.loadTexts:hwInfoDiskDomainTier0TotalCapacity.setStatus(_A)
_HwInfoDiskDomainTier0FreeCapacity_Type=Counter64
_HwInfoDiskDomainTier0FreeCapacity_Object=MibTableColumn
hwInfoDiskDomainTier0FreeCapacity=_HwInfoDiskDomainTier0FreeCapacity_Object((1,3,6,1,4,1,34774,4,1,23,4,1,1,11),_HwInfoDiskDomainTier0FreeCapacity_Type())
hwInfoDiskDomainTier0FreeCapacity.setMaxAccess(_C)
if mibBuilder.loadTexts:hwInfoDiskDomainTier0FreeCapacity.setStatus(_A)
_HwInfoDiskDomainTier0HotSpareCapacity_Type=Counter64
_HwInfoDiskDomainTier0HotSpareCapacity_Object=MibTableColumn
hwInfoDiskDomainTier0HotSpareCapacity=_HwInfoDiskDomainTier0HotSpareCapacity_Object((1,3,6,1,4,1,34774,4,1,23,4,1,1,12),_HwInfoDiskDomainTier0HotSpareCapacity_Type())
hwInfoDiskDomainTier0HotSpareCapacity.setMaxAccess(_C)
if mibBuilder.loadTexts:hwInfoDiskDomainTier0HotSpareCapacity.setStatus(_A)
_HwInfoDiskDomainTier0UsedHotSpareCapacity_Type=Counter64
_HwInfoDiskDomainTier0UsedHotSpareCapacity_Object=MibTableColumn
hwInfoDiskDomainTier0UsedHotSpareCapacity=_HwInfoDiskDomainTier0UsedHotSpareCapacity_Object((1,3,6,1,4,1,34774,4,1,23,4,1,1,13),_HwInfoDiskDomainTier0UsedHotSpareCapacity_Type())
hwInfoDiskDomainTier0UsedHotSpareCapacity.setMaxAccess(_C)
if mibBuilder.loadTexts:hwInfoDiskDomainTier0UsedHotSpareCapacity.setStatus(_A)
_HwInfoDiskDomainTier0HotSpareStrategy_Type=Unsigned32
_HwInfoDiskDomainTier0HotSpareStrategy_Object=MibTableColumn
hwInfoDiskDomainTier0HotSpareStrategy=_HwInfoDiskDomainTier0HotSpareStrategy_Object((1,3,6,1,4,1,34774,4,1,23,4,1,1,14),_HwInfoDiskDomainTier0HotSpareStrategy_Type())
hwInfoDiskDomainTier0HotSpareStrategy.setMaxAccess(_C)
if mibBuilder.loadTexts:hwInfoDiskDomainTier0HotSpareStrategy.setStatus(_A)
_HwInfoStoragePoolTable_Object=MibTable
hwInfoStoragePoolTable=_HwInfoStoragePoolTable_Object((1,3,6,1,4,1,34774,4,1,23,4,2))
if mibBuilder.loadTexts:hwInfoStoragePoolTable.setStatus(_A)
_HwInfoStoragePoolEntry_Object=MibTableRow
hwInfoStoragePoolEntry=_HwInfoStoragePoolEntry_Object((1,3,6,1,4,1,34774,4,1,23,4,2,1))
hwInfoStoragePoolEntry.setIndexNames((0,_B,_E))
if mibBuilder.loadTexts:hwInfoStoragePoolEntry.setStatus(_A)
_HwInfoStoragePoolID_Type=OctetString
_HwInfoStoragePoolID_Object=MibTableColumn
hwInfoStoragePoolID=_HwInfoStoragePoolID_Object((1,3,6,1,4,1,34774,4,1,23,4,2,1,1),_HwInfoStoragePoolID_Type())
hwInfoStoragePoolID.setMaxAccess(_C)
if mibBuilder.loadTexts:hwInfoStoragePoolID.setStatus(_A)
_HwInfoStoragePoolName_Type=OctetString
_HwInfoStoragePoolName_Object=MibTableColumn
hwInfoStoragePoolName=_HwInfoStoragePoolName_Object((1,3,6,1,4,1,34774,4,1,23,4,2,1,2),_HwInfoStoragePoolName_Type())
hwInfoStoragePoolName.setMaxAccess(_C)
if mibBuilder.loadTexts:hwInfoStoragePoolName.setStatus(_A)
_HwInfoStoragePoolDiskDomainID_Type=OctetString
_HwInfoStoragePoolDiskDomainID_Object=MibTableColumn
hwInfoStoragePoolDiskDomainID=_HwInfoStoragePoolDiskDomainID_Object((1,3,6,1,4,1,34774,4,1,23,4,2,1,3),_HwInfoStoragePoolDiskDomainID_Type())
hwInfoStoragePoolDiskDomainID.setMaxAccess(_C)
if mibBuilder.loadTexts:hwInfoStoragePoolDiskDomainID.setStatus(_A)
_HwInfoStoragePoolDiskDomainName_Type=OctetString
_HwInfoStoragePoolDiskDomainName_Object=MibTableColumn
hwInfoStoragePoolDiskDomainName=_HwInfoStoragePoolDiskDomainName_Object((1,3,6,1,4,1,34774,4,1,23,4,2,1,4),_HwInfoStoragePoolDiskDomainName_Type())
hwInfoStoragePoolDiskDomainName.setMaxAccess(_C)
if mibBuilder.loadTexts:hwInfoStoragePoolDiskDomainName.setStatus(_A)
_HwInfoStoragePoolHealthStatus_Type=Unsigned32
_HwInfoStoragePoolHealthStatus_Object=MibTableColumn
hwInfoStoragePoolHealthStatus=_HwInfoStoragePoolHealthStatus_Object((1,3,6,1,4,1,34774,4,1,23,4,2,1,5),_HwInfoStoragePoolHealthStatus_Type())
hwInfoStoragePoolHealthStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:hwInfoStoragePoolHealthStatus.setStatus(_A)
_HwInfoStoragePoolRunningStatus_Type=Unsigned32
_HwInfoStoragePoolRunningStatus_Object=MibTableColumn
hwInfoStoragePoolRunningStatus=_HwInfoStoragePoolRunningStatus_Object((1,3,6,1,4,1,34774,4,1,23,4,2,1,6),_HwInfoStoragePoolRunningStatus_Type())
hwInfoStoragePoolRunningStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:hwInfoStoragePoolRunningStatus.setStatus(_A)
_HwInfoStoragePoolTotalCapacity_Type=Counter64
_HwInfoStoragePoolTotalCapacity_Object=MibTableColumn
hwInfoStoragePoolTotalCapacity=_HwInfoStoragePoolTotalCapacity_Object((1,3,6,1,4,1,34774,4,1,23,4,2,1,7),_HwInfoStoragePoolTotalCapacity_Type())
hwInfoStoragePoolTotalCapacity.setMaxAccess(_C)
if mibBuilder.loadTexts:hwInfoStoragePoolTotalCapacity.setStatus(_A)
_HwInfoStoragePoolSubscribedCapacity_Type=Counter64
_HwInfoStoragePoolSubscribedCapacity_Object=MibTableColumn
hwInfoStoragePoolSubscribedCapacity=_HwInfoStoragePoolSubscribedCapacity_Object((1,3,6,1,4,1,34774,4,1,23,4,2,1,8),_HwInfoStoragePoolSubscribedCapacity_Type())
hwInfoStoragePoolSubscribedCapacity.setMaxAccess(_C)
if mibBuilder.loadTexts:hwInfoStoragePoolSubscribedCapacity.setStatus(_A)
_HwInfoStoragePoolFreeCapacity_Type=Counter64
_HwInfoStoragePoolFreeCapacity_Object=MibTableColumn
hwInfoStoragePoolFreeCapacity=_HwInfoStoragePoolFreeCapacity_Object((1,3,6,1,4,1,34774,4,1,23,4,2,1,9),_HwInfoStoragePoolFreeCapacity_Type())
hwInfoStoragePoolFreeCapacity.setMaxAccess(_C)
if mibBuilder.loadTexts:hwInfoStoragePoolFreeCapacity.setStatus(_A)
_HwInfoStoragePoolTier0Capacity_Type=Counter64
_HwInfoStoragePoolTier0Capacity_Object=MibTableColumn
hwInfoStoragePoolTier0Capacity=_HwInfoStoragePoolTier0Capacity_Object((1,3,6,1,4,1,34774,4,1,23,4,2,1,11),_HwInfoStoragePoolTier0Capacity_Type())
hwInfoStoragePoolTier0Capacity.setMaxAccess(_C)
if mibBuilder.loadTexts:hwInfoStoragePoolTier0Capacity.setStatus(_A)
_HwInfoStoragePoolFullThreshold_Type=Unsigned32
_HwInfoStoragePoolFullThreshold_Object=MibTableColumn
hwInfoStoragePoolFullThreshold=_HwInfoStoragePoolFullThreshold_Object((1,3,6,1,4,1,34774,4,1,23,4,2,1,14),_HwInfoStoragePoolFullThreshold_Type())
hwInfoStoragePoolFullThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:hwInfoStoragePoolFullThreshold.setStatus(_A)
_HwInfoPortGroupTable_Object=MibTable
hwInfoPortGroupTable=_HwInfoPortGroupTable_Object((1,3,6,1,4,1,34774,4,1,23,4,4))
if mibBuilder.loadTexts:hwInfoPortGroupTable.setStatus(_A)
_HwInfoPortGroupEntry_Object=MibTableRow
hwInfoPortGroupEntry=_HwInfoPortGroupEntry_Object((1,3,6,1,4,1,34774,4,1,23,4,4,1))
hwInfoPortGroupEntry.setIndexNames((0,_B,_F))
if mibBuilder.loadTexts:hwInfoPortGroupEntry.setStatus(_A)
_HwInfoPortGroupID_Type=OctetString
_HwInfoPortGroupID_Object=MibTableColumn
hwInfoPortGroupID=_HwInfoPortGroupID_Object((1,3,6,1,4,1,34774,4,1,23,4,4,1,1),_HwInfoPortGroupID_Type())
hwInfoPortGroupID.setMaxAccess(_C)
if mibBuilder.loadTexts:hwInfoPortGroupID.setStatus(_A)
_HwInfoPortGroupName_Type=OctetString
_HwInfoPortGroupName_Object=MibTableColumn
hwInfoPortGroupName=_HwInfoPortGroupName_Object((1,3,6,1,4,1,34774,4,1,23,4,4,1,2),_HwInfoPortGroupName_Type())
hwInfoPortGroupName.setMaxAccess(_C)
if mibBuilder.loadTexts:hwInfoPortGroupName.setStatus(_A)
_HwInfoPortGroupPortList_Type=OctetString
_HwInfoPortGroupPortList_Object=MibTableColumn
hwInfoPortGroupPortList=_HwInfoPortGroupPortList_Object((1,3,6,1,4,1,34774,4,1,23,4,4,1,3),_HwInfoPortGroupPortList_Type())
hwInfoPortGroupPortList.setMaxAccess(_C)
if mibBuilder.loadTexts:hwInfoPortGroupPortList.setStatus(_A)
_HwInfoHostTable_Object=MibTable
hwInfoHostTable=_HwInfoHostTable_Object((1,3,6,1,4,1,34774,4,1,23,4,5))
if mibBuilder.loadTexts:hwInfoHostTable.setStatus(_A)
_HwInfoHostEntry_Object=MibTableRow
hwInfoHostEntry=_HwInfoHostEntry_Object((1,3,6,1,4,1,34774,4,1,23,4,5,1))
hwInfoHostEntry.setIndexNames((0,_B,_G))
if mibBuilder.loadTexts:hwInfoHostEntry.setStatus(_A)
_HwInfoHostID_Type=OctetString
_HwInfoHostID_Object=MibTableColumn
hwInfoHostID=_HwInfoHostID_Object((1,3,6,1,4,1,34774,4,1,23,4,5,1,1),_HwInfoHostID_Type())
hwInfoHostID.setMaxAccess(_C)
if mibBuilder.loadTexts:hwInfoHostID.setStatus(_A)
_HwInfoHostName_Type=OctetString
_HwInfoHostName_Object=MibTableColumn
hwInfoHostName=_HwInfoHostName_Object((1,3,6,1,4,1,34774,4,1,23,4,5,1,2),_HwInfoHostName_Type())
hwInfoHostName.setMaxAccess(_C)
if mibBuilder.loadTexts:hwInfoHostName.setStatus(_A)
_HwInfoHostLocation_Type=OctetString
_HwInfoHostLocation_Object=MibTableColumn
hwInfoHostLocation=_HwInfoHostLocation_Object((1,3,6,1,4,1,34774,4,1,23,4,5,1,3),_HwInfoHostLocation_Type())
hwInfoHostLocation.setMaxAccess(_C)
if mibBuilder.loadTexts:hwInfoHostLocation.setStatus(_A)
_HwInfoHostHealthStatus_Type=Unsigned32
_HwInfoHostHealthStatus_Object=MibTableColumn
hwInfoHostHealthStatus=_HwInfoHostHealthStatus_Object((1,3,6,1,4,1,34774,4,1,23,4,5,1,4),_HwInfoHostHealthStatus_Type())
hwInfoHostHealthStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:hwInfoHostHealthStatus.setStatus(_A)
_HwInfoHostRunningStatus_Type=Unsigned32
_HwInfoHostRunningStatus_Object=MibTableColumn
hwInfoHostRunningStatus=_HwInfoHostRunningStatus_Object((1,3,6,1,4,1,34774,4,1,23,4,5,1,5),_HwInfoHostRunningStatus_Type())
hwInfoHostRunningStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:hwInfoHostRunningStatus.setStatus(_A)
_HwInfoHostOperatingSystem_Type=Unsigned32
_HwInfoHostOperatingSystem_Object=MibTableColumn
hwInfoHostOperatingSystem=_HwInfoHostOperatingSystem_Object((1,3,6,1,4,1,34774,4,1,23,4,5,1,6),_HwInfoHostOperatingSystem_Type())
hwInfoHostOperatingSystem.setMaxAccess(_C)
if mibBuilder.loadTexts:hwInfoHostOperatingSystem.setStatus(_A)
_HwInfoHostIPAddress_Type=OctetString
_HwInfoHostIPAddress_Object=MibTableColumn
hwInfoHostIPAddress=_HwInfoHostIPAddress_Object((1,3,6,1,4,1,34774,4,1,23,4,5,1,7),_HwInfoHostIPAddress_Type())
hwInfoHostIPAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:hwInfoHostIPAddress.setStatus(_A)
_HwInfoHostNetworkName_Type=OctetString
_HwInfoHostNetworkName_Object=MibTableColumn
hwInfoHostNetworkName=_HwInfoHostNetworkName_Object((1,3,6,1,4,1,34774,4,1,23,4,5,1,8),_HwInfoHostNetworkName_Type())
hwInfoHostNetworkName.setMaxAccess(_C)
if mibBuilder.loadTexts:hwInfoHostNetworkName.setStatus(_A)
_HwInfoHostModel_Type=OctetString
_HwInfoHostModel_Object=MibTableColumn
hwInfoHostModel=_HwInfoHostModel_Object((1,3,6,1,4,1,34774,4,1,23,4,5,1,9),_HwInfoHostModel_Type())
hwInfoHostModel.setMaxAccess(_C)
if mibBuilder.loadTexts:hwInfoHostModel.setStatus(_A)
_HwInfoHostGroupTable_Object=MibTable
hwInfoHostGroupTable=_HwInfoHostGroupTable_Object((1,3,6,1,4,1,34774,4,1,23,4,6))
if mibBuilder.loadTexts:hwInfoHostGroupTable.setStatus(_A)
_HwInfoHostGroupEntry_Object=MibTableRow
hwInfoHostGroupEntry=_HwInfoHostGroupEntry_Object((1,3,6,1,4,1,34774,4,1,23,4,6,1))
hwInfoHostGroupEntry.setIndexNames((0,_B,_H))
if mibBuilder.loadTexts:hwInfoHostGroupEntry.setStatus(_A)
_HwInfoHostGroupID_Type=OctetString
_HwInfoHostGroupID_Object=MibTableColumn
hwInfoHostGroupID=_HwInfoHostGroupID_Object((1,3,6,1,4,1,34774,4,1,23,4,6,1,1),_HwInfoHostGroupID_Type())
hwInfoHostGroupID.setMaxAccess(_C)
if mibBuilder.loadTexts:hwInfoHostGroupID.setStatus(_A)
_HwInfoHostGroupName_Type=OctetString
_HwInfoHostGroupName_Object=MibTableColumn
hwInfoHostGroupName=_HwInfoHostGroupName_Object((1,3,6,1,4,1,34774,4,1,23,4,6,1,2),_HwInfoHostGroupName_Type())
hwInfoHostGroupName.setMaxAccess(_C)
if mibBuilder.loadTexts:hwInfoHostGroupName.setStatus(_A)
_HwInfoHostGroupHostList_Type=OctetString
_HwInfoHostGroupHostList_Object=MibTableColumn
hwInfoHostGroupHostList=_HwInfoHostGroupHostList_Object((1,3,6,1,4,1,34774,4,1,23,4,6,1,3),_HwInfoHostGroupHostList_Type())
hwInfoHostGroupHostList.setMaxAccess(_C)
if mibBuilder.loadTexts:hwInfoHostGroupHostList.setStatus(_A)
_HwInfoLunGroupTable_Object=MibTable
hwInfoLunGroupTable=_HwInfoLunGroupTable_Object((1,3,6,1,4,1,34774,4,1,23,4,7))
if mibBuilder.loadTexts:hwInfoLunGroupTable.setStatus(_A)
_HwInfoLunGroupEntry_Object=MibTableRow
hwInfoLunGroupEntry=_HwInfoLunGroupEntry_Object((1,3,6,1,4,1,34774,4,1,23,4,7,1))
hwInfoLunGroupEntry.setIndexNames((0,_B,_I))
if mibBuilder.loadTexts:hwInfoLunGroupEntry.setStatus(_A)
_HwInfoLunGroupID_Type=OctetString
_HwInfoLunGroupID_Object=MibTableColumn
hwInfoLunGroupID=_HwInfoLunGroupID_Object((1,3,6,1,4,1,34774,4,1,23,4,7,1,1),_HwInfoLunGroupID_Type())
hwInfoLunGroupID.setMaxAccess(_C)
if mibBuilder.loadTexts:hwInfoLunGroupID.setStatus(_A)
_HwInfoLunGroupName_Type=OctetString
_HwInfoLunGroupName_Object=MibTableColumn
hwInfoLunGroupName=_HwInfoLunGroupName_Object((1,3,6,1,4,1,34774,4,1,23,4,7,1,2),_HwInfoLunGroupName_Type())
hwInfoLunGroupName.setMaxAccess(_C)
if mibBuilder.loadTexts:hwInfoLunGroupName.setStatus(_A)
_HwInfoLunGroupLunList_Type=OctetString
_HwInfoLunGroupLunList_Object=MibTableColumn
hwInfoLunGroupLunList=_HwInfoLunGroupLunList_Object((1,3,6,1,4,1,34774,4,1,23,4,7,1,3),_HwInfoLunGroupLunList_Type())
hwInfoLunGroupLunList.setMaxAccess(_C)
if mibBuilder.loadTexts:hwInfoLunGroupLunList.setStatus(_A)
_HwInfoLunTable_Object=MibTable
hwInfoLunTable=_HwInfoLunTable_Object((1,3,6,1,4,1,34774,4,1,23,4,8))
if mibBuilder.loadTexts:hwInfoLunTable.setStatus(_A)
_HwInfoLunEntry_Object=MibTableRow
hwInfoLunEntry=_HwInfoLunEntry_Object((1,3,6,1,4,1,34774,4,1,23,4,8,1))
hwInfoLunEntry.setIndexNames((0,_B,_J))
if mibBuilder.loadTexts:hwInfoLunEntry.setStatus(_A)
_HwInfoLunID_Type=OctetString
_HwInfoLunID_Object=MibTableColumn
hwInfoLunID=_HwInfoLunID_Object((1,3,6,1,4,1,34774,4,1,23,4,8,1,1),_HwInfoLunID_Type())
hwInfoLunID.setMaxAccess(_C)
if mibBuilder.loadTexts:hwInfoLunID.setStatus(_A)
_HwInfoLunName_Type=OctetString
_HwInfoLunName_Object=MibTableColumn
hwInfoLunName=_HwInfoLunName_Object((1,3,6,1,4,1,34774,4,1,23,4,8,1,2),_HwInfoLunName_Type())
hwInfoLunName.setMaxAccess(_C)
if mibBuilder.loadTexts:hwInfoLunName.setStatus(_A)
_HwInfoLunPoolID_Type=OctetString
_HwInfoLunPoolID_Object=MibTableColumn
hwInfoLunPoolID=_HwInfoLunPoolID_Object((1,3,6,1,4,1,34774,4,1,23,4,8,1,3),_HwInfoLunPoolID_Type())
hwInfoLunPoolID.setMaxAccess(_C)
if mibBuilder.loadTexts:hwInfoLunPoolID.setStatus(_A)
_HwInfoLunPoolName_Type=OctetString
_HwInfoLunPoolName_Object=MibTableColumn
hwInfoLunPoolName=_HwInfoLunPoolName_Object((1,3,6,1,4,1,34774,4,1,23,4,8,1,4),_HwInfoLunPoolName_Type())
hwInfoLunPoolName.setMaxAccess(_C)
if mibBuilder.loadTexts:hwInfoLunPoolName.setStatus(_A)
_HwInfoLunCapacity_Type=Counter64
_HwInfoLunCapacity_Object=MibTableColumn
hwInfoLunCapacity=_HwInfoLunCapacity_Object((1,3,6,1,4,1,34774,4,1,23,4,8,1,5),_HwInfoLunCapacity_Type())
hwInfoLunCapacity.setMaxAccess(_C)
if mibBuilder.loadTexts:hwInfoLunCapacity.setStatus(_A)
_HwInfoLunSubscribedCapacity_Type=Counter64
_HwInfoLunSubscribedCapacity_Object=MibTableColumn
hwInfoLunSubscribedCapacity=_HwInfoLunSubscribedCapacity_Object((1,3,6,1,4,1,34774,4,1,23,4,8,1,6),_HwInfoLunSubscribedCapacity_Type())
hwInfoLunSubscribedCapacity.setMaxAccess(_C)
if mibBuilder.loadTexts:hwInfoLunSubscribedCapacity.setStatus(_A)
_HwInfoLunProtectionCapacity_Type=Counter64
_HwInfoLunProtectionCapacity_Object=MibTableColumn
hwInfoLunProtectionCapacity=_HwInfoLunProtectionCapacity_Object((1,3,6,1,4,1,34774,4,1,23,4,8,1,7),_HwInfoLunProtectionCapacity_Type())
hwInfoLunProtectionCapacity.setMaxAccess(_C)
if mibBuilder.loadTexts:hwInfoLunProtectionCapacity.setStatus(_A)
_HwInfoLunSectorSize_Type=Unsigned32
_HwInfoLunSectorSize_Object=MibTableColumn
hwInfoLunSectorSize=_HwInfoLunSectorSize_Object((1,3,6,1,4,1,34774,4,1,23,4,8,1,8),_HwInfoLunSectorSize_Type())
hwInfoLunSectorSize.setMaxAccess(_C)
if mibBuilder.loadTexts:hwInfoLunSectorSize.setStatus(_A)
_HwInfoLunHealthStatus_Type=Unsigned32
_HwInfoLunHealthStatus_Object=MibTableColumn
hwInfoLunHealthStatus=_HwInfoLunHealthStatus_Object((1,3,6,1,4,1,34774,4,1,23,4,8,1,9),_HwInfoLunHealthStatus_Type())
hwInfoLunHealthStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:hwInfoLunHealthStatus.setStatus(_A)
_HwInfoLunRunningStatus_Type=Unsigned32
_HwInfoLunRunningStatus_Object=MibTableColumn
hwInfoLunRunningStatus=_HwInfoLunRunningStatus_Object((1,3,6,1,4,1,34774,4,1,23,4,8,1,10),_HwInfoLunRunningStatus_Type())
hwInfoLunRunningStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:hwInfoLunRunningStatus.setStatus(_A)
_HwInfoLunType_Type=Unsigned32
_HwInfoLunType_Object=MibTableColumn
hwInfoLunType=_HwInfoLunType_Object((1,3,6,1,4,1,34774,4,1,23,4,8,1,11),_HwInfoLunType_Type())
hwInfoLunType.setMaxAccess(_C)
if mibBuilder.loadTexts:hwInfoLunType.setStatus(_A)
_HwInfoLunIOPriority_Type=Unsigned32
_HwInfoLunIOPriority_Object=MibTableColumn
hwInfoLunIOPriority=_HwInfoLunIOPriority_Object((1,3,6,1,4,1,34774,4,1,23,4,8,1,12),_HwInfoLunIOPriority_Type())
hwInfoLunIOPriority.setMaxAccess(_C)
if mibBuilder.loadTexts:hwInfoLunIOPriority.setStatus(_A)
_HwInfoLunWWN_Type=OctetString
_HwInfoLunWWN_Object=MibTableColumn
hwInfoLunWWN=_HwInfoLunWWN_Object((1,3,6,1,4,1,34774,4,1,23,4,8,1,13),_HwInfoLunWWN_Type())
hwInfoLunWWN.setMaxAccess(_C)
if mibBuilder.loadTexts:hwInfoLunWWN.setStatus(_A)
_HwInfoLunExposedToInitiator_Type=Unsigned32
_HwInfoLunExposedToInitiator_Object=MibTableColumn
hwInfoLunExposedToInitiator=_HwInfoLunExposedToInitiator_Object((1,3,6,1,4,1,34774,4,1,23,4,8,1,14),_HwInfoLunExposedToInitiator_Type())
hwInfoLunExposedToInitiator.setMaxAccess(_C)
if mibBuilder.loadTexts:hwInfoLunExposedToInitiator.setStatus(_A)
_HwInfoLunWritePolicy_Type=Unsigned32
_HwInfoLunWritePolicy_Object=MibTableColumn
hwInfoLunWritePolicy=_HwInfoLunWritePolicy_Object((1,3,6,1,4,1,34774,4,1,23,4,8,1,15),_HwInfoLunWritePolicy_Type())
hwInfoLunWritePolicy.setMaxAccess(_C)
if mibBuilder.loadTexts:hwInfoLunWritePolicy.setStatus(_A)
_HwInfoLunRunningWritePolicy_Type=Unsigned32
_HwInfoLunRunningWritePolicy_Object=MibTableColumn
hwInfoLunRunningWritePolicy=_HwInfoLunRunningWritePolicy_Object((1,3,6,1,4,1,34774,4,1,23,4,8,1,16),_HwInfoLunRunningWritePolicy_Type())
hwInfoLunRunningWritePolicy.setMaxAccess(_C)
if mibBuilder.loadTexts:hwInfoLunRunningWritePolicy.setStatus(_A)
_HwInfoLunPrefetchPolicy_Type=Unsigned32
_HwInfoLunPrefetchPolicy_Object=MibTableColumn
hwInfoLunPrefetchPolicy=_HwInfoLunPrefetchPolicy_Object((1,3,6,1,4,1,34774,4,1,23,4,8,1,17),_HwInfoLunPrefetchPolicy_Type())
hwInfoLunPrefetchPolicy.setMaxAccess(_C)
if mibBuilder.loadTexts:hwInfoLunPrefetchPolicy.setStatus(_A)
_HwInfoLunPrefetchValue_Type=Unsigned32
_HwInfoLunPrefetchValue_Object=MibTableColumn
hwInfoLunPrefetchValue=_HwInfoLunPrefetchValue_Object((1,3,6,1,4,1,34774,4,1,23,4,8,1,20),_HwInfoLunPrefetchValue_Type())
hwInfoLunPrefetchValue.setMaxAccess(_C)
if mibBuilder.loadTexts:hwInfoLunPrefetchValue.setStatus(_A)
_HwInfoLunOwnerController_Type=OctetString
_HwInfoLunOwnerController_Object=MibTableColumn
hwInfoLunOwnerController=_HwInfoLunOwnerController_Object((1,3,6,1,4,1,34774,4,1,23,4,8,1,21),_HwInfoLunOwnerController_Type())
hwInfoLunOwnerController.setMaxAccess(_C)
if mibBuilder.loadTexts:hwInfoLunOwnerController.setStatus(_A)
_HwInfoLunWorkController_Type=OctetString
_HwInfoLunWorkController_Object=MibTableColumn
hwInfoLunWorkController=_HwInfoLunWorkController_Object((1,3,6,1,4,1,34774,4,1,23,4,8,1,22),_HwInfoLunWorkController_Type())
hwInfoLunWorkController.setMaxAccess(_C)
if mibBuilder.loadTexts:hwInfoLunWorkController.setStatus(_A)
_HwInfoLunIsAddToLunGroup_Type=Unsigned32
_HwInfoLunIsAddToLunGroup_Object=MibTableColumn
hwInfoLunIsAddToLunGroup=_HwInfoLunIsAddToLunGroup_Object((1,3,6,1,4,1,34774,4,1,23,4,8,1,25),_HwInfoLunIsAddToLunGroup_Type())
hwInfoLunIsAddToLunGroup.setMaxAccess(_C)
if mibBuilder.loadTexts:hwInfoLunIsAddToLunGroup.setStatus(_A)
_HwInfoLunDIFSwitch_Type=Unsigned32
_HwInfoLunDIFSwitch_Object=MibTableColumn
hwInfoLunDIFSwitch=_HwInfoLunDIFSwitch_Object((1,3,6,1,4,1,34774,4,1,23,4,8,1,26),_HwInfoLunDIFSwitch_Type())
hwInfoLunDIFSwitch.setMaxAccess(_C)
if mibBuilder.loadTexts:hwInfoLunDIFSwitch.setStatus(_A)
_HwInfoLunRemoteLUNWWN_Type=OctetString
_HwInfoLunRemoteLUNWWN_Object=MibTableColumn
hwInfoLunRemoteLUNWWN=_HwInfoLunRemoteLUNWWN_Object((1,3,6,1,4,1,34774,4,1,23,4,8,1,27),_HwInfoLunRemoteLUNWWN_Type())
hwInfoLunRemoteLUNWWN.setMaxAccess(_C)
if mibBuilder.loadTexts:hwInfoLunRemoteLUNWWN.setStatus(_A)
_HwInfoLunUsageType_Type=Unsigned32
_HwInfoLunUsageType_Object=MibTableColumn
hwInfoLunUsageType=_HwInfoLunUsageType_Object((1,3,6,1,4,1,34774,4,1,23,4,8,1,28),_HwInfoLunUsageType_Type())
hwInfoLunUsageType.setMaxAccess(_C)
if mibBuilder.loadTexts:hwInfoLunUsageType.setStatus(_A)
_IsoConformance_ObjectIdentity=ObjectIdentity
isoConformance=_IsoConformance_ObjectIdentity((1,6))
_IsoGroups_ObjectIdentity=ObjectIdentity
isoGroups=_IsoGroups_ObjectIdentity((1,6,1))
_IsoCompliances_ObjectIdentity=ObjectIdentity
isoCompliances=_IsoCompliances_ObjectIdentity((1,6,2))
currentObjectGroup=ObjectGroup((1,6,1,1))
currentObjectGroup.setObjects(*((_B,_D),(_B,_K),(_B,_L),(_B,_M),(_B,_N),(_B,_O),(_B,_P),(_B,_Q),(_B,_R),(_B,_S),(_B,_T),(_B,_U),(_B,_V),(_B,_W),(_B,_E),(_B,_X),(_B,_Y),(_B,_Z),(_B,_a),(_B,_b),(_B,_c),(_B,_d),(_B,_e),(_B,_f),(_B,_G),(_B,_g),(_B,_h),(_B,_i),(_B,_j),(_B,_k),(_B,_l),(_B,_m),(_B,_n),(_B,_H),(_B,_o),(_B,_I),(_B,_p),(_B,_J),(_B,_q),(_B,_r),(_B,_s),(_B,_t),(_B,_u),(_B,_v),(_B,_w),(_B,_x),(_B,_y),(_B,_z),(_B,_A0),(_B,_A1),(_B,_A2),(_B,_A3),(_B,_A4),(_B,_A5),(_B,_A6),(_B,_A7),(_B,_A8),(_B,_A9),(_B,_AA),(_B,_AB),(_B,_AC),(_B,_F),(_B,_AD),(_B,_AE),(_B,_AF),(_B,_AG),(_B,_AH)))
if mibBuilder.loadTexts:currentObjectGroup.setStatus(_A)
basicCompliance=ModuleCompliance((1,6,2,1))
basicCompliance.setObjects((_B,_AI))
if mibBuilder.loadTexts:basicCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'NodeCodeString':NodeCodeString,'huaweistorage':huaweistorage,'hwStorage':hwStorage,'hwISM':hwISM,'hwStorageDevice':hwStorageDevice,'hwSpaceInfo':hwSpaceInfo,'hwInfoDiskDomainTable':hwInfoDiskDomainTable,'hwInfoDiskDomainEntry':hwInfoDiskDomainEntry,_D:hwInfoDiskDomainID,_K:hwInfoDiskDomainName,_L:hwInfoDiskDomainHealthStatus,_M:hwInfoDiskDomainRunningStatus,_N:hwInfoDiskDomainTotalCapacity,_O:hwInfoDiskDomainFreeCapacity,_P:hwInfoDiskDomainHotSpareCapacity,_Q:hwInfoDiskDomainUsedHotSpareCapacity,_R:hwInfoDiskDomainTier0DiskNumber,_S:hwInfoDiskDomainTier0TotalCapacity,_T:hwInfoDiskDomainTier0FreeCapacity,_U:hwInfoDiskDomainTier0HotSpareCapacity,_V:hwInfoDiskDomainTier0UsedHotSpareCapacity,_W:hwInfoDiskDomainTier0HotSpareStrategy,'hwInfoStoragePoolTable':hwInfoStoragePoolTable,'hwInfoStoragePoolEntry':hwInfoStoragePoolEntry,_E:hwInfoStoragePoolID,_X:hwInfoStoragePoolName,_Y:hwInfoStoragePoolDiskDomainID,_AC:hwInfoStoragePoolDiskDomainName,_Z:hwInfoStoragePoolHealthStatus,_a:hwInfoStoragePoolRunningStatus,_b:hwInfoStoragePoolTotalCapacity,_c:hwInfoStoragePoolSubscribedCapacity,_d:hwInfoStoragePoolFreeCapacity,_e:hwInfoStoragePoolTier0Capacity,_f:hwInfoStoragePoolFullThreshold,'hwInfoPortGroupTable':hwInfoPortGroupTable,'hwInfoPortGroupEntry':hwInfoPortGroupEntry,_F:hwInfoPortGroupID,_AD:hwInfoPortGroupName,_AE:hwInfoPortGroupPortList,'hwInfoHostTable':hwInfoHostTable,'hwInfoHostEntry':hwInfoHostEntry,_G:hwInfoHostID,_g:hwInfoHostName,_h:hwInfoHostLocation,_i:hwInfoHostHealthStatus,_j:hwInfoHostRunningStatus,_k:hwInfoHostOperatingSystem,_l:hwInfoHostIPAddress,_n:hwInfoHostNetworkName,_m:hwInfoHostModel,'hwInfoHostGroupTable':hwInfoHostGroupTable,'hwInfoHostGroupEntry':hwInfoHostGroupEntry,_H:hwInfoHostGroupID,_o:hwInfoHostGroupName,_AF:hwInfoHostGroupHostList,'hwInfoLunGroupTable':hwInfoLunGroupTable,'hwInfoLunGroupEntry':hwInfoLunGroupEntry,_I:hwInfoLunGroupID,_p:hwInfoLunGroupName,_AG:hwInfoLunGroupLunList,'hwInfoLunTable':hwInfoLunTable,'hwInfoLunEntry':hwInfoLunEntry,_J:hwInfoLunID,_q:hwInfoLunName,_r:hwInfoLunPoolID,_s:hwInfoLunPoolName,_t:hwInfoLunCapacity,_u:hwInfoLunSubscribedCapacity,_v:hwInfoLunProtectionCapacity,_w:hwInfoLunSectorSize,_x:hwInfoLunHealthStatus,_y:hwInfoLunRunningStatus,_z:hwInfoLunType,_A0:hwInfoLunIOPriority,_A1:hwInfoLunWWN,_A2:hwInfoLunExposedToInitiator,_A3:hwInfoLunWritePolicy,_A4:hwInfoLunRunningWritePolicy,_A5:hwInfoLunPrefetchPolicy,_A6:hwInfoLunPrefetchValue,_A7:hwInfoLunOwnerController,_A8:hwInfoLunWorkController,_A9:hwInfoLunIsAddToLunGroup,_AA:hwInfoLunDIFSwitch,_AB:hwInfoLunRemoteLUNWWN,_AH:hwInfoLunUsageType,'isoConformance':isoConformance,'isoGroups':isoGroups,_AI:currentObjectGroup,'isoCompliances':isoCompliances,'basicCompliance':basicCompliance})