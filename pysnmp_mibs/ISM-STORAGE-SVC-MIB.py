_Af='currentObjectGroup'
_Ae='hwStorageControllerHealthStatus'
_Ad='hwStorageLunPrefetchStrategy'
_Ac='hwStorageISCSIPortLogicType'
_Ab='hwStorageSASPortSpeedRate'
_Aa='hwStorageSASPortLogicType'
_AZ='hwStorageFCPortSpeedRate'
_AY='hwStorageFCPortLogicType'
_AX='hwStorageSASPortWWN'
_AW='hwStorageControllerVoltage'
_AV='hwStorageControllerCPUInfo'
_AU='hwStorageControllerMemorySize'
_AT='hwStorageControllerBIOSVer'
_AS='hwStorageControllerLogicVer'
_AR='hwStorageControllerBMCVer'
_AQ='hwStorageControllerPCBVer'
_AP='hwStorageControllerELabel'
_AO='hwStorageControllerIsMaster'
_AN='hwStorageControllerTemperature'
_AM='hwStorageControllerSoftVer'
_AL='hwStorageControllerRunningStatus'
_AK='hwStorageControllerLocation'
_AJ='hwStorageControllerName'
_AI='hwStorageNodeRowStatus'
_AH='hwStorageNodeIsMaster'
_AG='hwStorageNodeStatus'
_AF='hwStorageNodeIPAddress'
_AE='hwStorageCacheRowStatus'
_AD='hwStorageCacheLowWaterLevel'
_AC='hwStorageCacheHighWaterLevel'
_AB='hwStorageCacheTotalCapacity'
_AA='hwStorageFrontEndHostPortDescription'
_A9='hwStorageFrontEndHostPortPhysAddress'
_A8='hwStorageFrontEndHostPortStatus'
_A7='hwStorageFrontEndHostPortType'
_A6='hwStorageSASPortConfigRate'
_A5='hwStorageSASPortStatus'
_A4='hwStorageSASPortID'
_A3='hwStorageSASPortBoardIfIndex'
_A2='deviceType'
_A1='usedCapacity'
_A0='totalCapacity'
_z='hwStorageLunRowStatus'
_y='hwStorageLunStatus'
_x='hwStorageLunPrefetchValue'
_w='hwStorageLunWriteStrategy'
_v='hwStorageLunStripDepth'
_u='hwStorageLunOwningController'
_t='hwStorageLunCapacity'
_s='hwStorageLunPoolID'
_r='hwStorageLunWWN'
_q='hwStorageLunName'
_p='hwStorageISCSIPortBindMode'
_o='hwStorageISCSIPortNetMask'
_n='hwStorageISCSIPortIP'
_m='hwStorageISCSIPortStatus'
_l='hwStorageISCSIPortID'
_k='hwStorageISCSIPortBoardIfIndex'
_j='hwStorageFCPortWWN'
_i='hwStorageFCPortMode'
_h='hwStorageFCPortConfigRate'
_g='hwStorageFCPortStatus'
_f='hwStorageFCPortID'
_e='hwStorageFCPortBoardIfIndex'
_d='formatting'
_c='consistent'
_b='gbps60'
_a='gbps30'
_Z='gbps15'
_Y='gbps16'
_X='hwStorageNodeIfIndex'
_W='hwStorageLunID'
_V='hwStorageCacheID'
_U='normal'
_T='hwStorageControllerID'
_S='hwStorageFrontEndHostPortIfIndex'
_R='hwStorageISCSIPortIfIndex'
_Q='hwStorageSASPortIfIndex'
_P='maintenance'
_O='upsmanagement'
_N='management'
_M='ibs'
_L='ibc'
_K='service'
_J='hwStorageFCPortIfIndex'
_I='expansion'
_H='linkup'
_G='linkdown'
_F='fault'
_E='read-write'
_D='Integer32'
_C='read-only'
_B='ISM-STORAGE-SVC-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention')
huaweistorage=ModuleIdentity((1,3,6,1,4,1,34774))
if mibBuilder.loadTexts:huaweistorage.setRevisions(('2013-04-07 19:15',))
class NodeCodeString(TextualConvention,OctetString):status=_A;displayHint='255a';subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(15,17))
_HwStorage_ObjectIdentity=ObjectIdentity
hwStorage=_HwStorage_ObjectIdentity((1,3,6,1,4,1,34774,4))
_HwISM_ObjectIdentity=ObjectIdentity
hwISM=_HwISM_ObjectIdentity((1,3,6,1,4,1,34774,4,1))
_Common_ObjectIdentity=ObjectIdentity
common=_Common_ObjectIdentity((1,3,6,1,4,1,34774,4,1,1))
_DeviceId_Type=DisplayString
_DeviceId_Object=MibScalar
deviceId=_DeviceId_Object((1,3,6,1,4,1,34774,4,1,1,1),_DeviceId_Type())
deviceId.setMaxAccess(_C)
if mibBuilder.loadTexts:deviceId.setStatus(_A)
_DeviceType_Type=Integer32
_DeviceType_Object=MibScalar
deviceType=_DeviceType_Object((1,3,6,1,4,1,34774,4,1,1,2),_DeviceType_Type())
deviceType.setMaxAccess(_C)
if mibBuilder.loadTexts:deviceType.setStatus(_A)
_Status_Type=Integer32
_Status_Object=MibScalar
status=_Status_Object((1,3,6,1,4,1,34774,4,1,1,3),_Status_Type())
status.setMaxAccess(_C)
if mibBuilder.loadTexts:status.setStatus(_A)
_UsedCapacity_Type=Counter64
_UsedCapacity_Object=MibScalar
usedCapacity=_UsedCapacity_Object((1,3,6,1,4,1,34774,4,1,1,4),_UsedCapacity_Type())
usedCapacity.setMaxAccess(_C)
if mibBuilder.loadTexts:usedCapacity.setStatus(_A)
_TotalCapacity_Type=Counter64
_TotalCapacity_Object=MibScalar
totalCapacity=_TotalCapacity_Object((1,3,6,1,4,1,34774,4,1,1,5),_TotalCapacity_Type())
totalCapacity.setMaxAccess(_C)
if mibBuilder.loadTexts:totalCapacity.setStatus(_A)
_Version_Type=DisplayString
_Version_Object=MibScalar
version=_Version_Object((1,3,6,1,4,1,34774,4,1,1,6),_Version_Type())
version.setMaxAccess(_C)
if mibBuilder.loadTexts:version.setStatus(_A)
_Hardware_Type=DisplayString
_Hardware_Object=MibScalar
hardware=_Hardware_Object((1,3,6,1,4,1,34774,4,1,1,7),_Hardware_Type())
hardware.setMaxAccess(_C)
if mibBuilder.loadTexts:hardware.setStatus(_A)
_HwStorageService_ObjectIdentity=ObjectIdentity
hwStorageService=_HwStorageService_ObjectIdentity((1,3,6,1,4,1,34774,4,1,19))
_HwStoragePhysicalModule_ObjectIdentity=ObjectIdentity
hwStoragePhysicalModule=_HwStoragePhysicalModule_ObjectIdentity((1,3,6,1,4,1,34774,4,1,19,8))
_HwStorageFCPortTable_Object=MibTable
hwStorageFCPortTable=_HwStorageFCPortTable_Object((1,3,6,1,4,1,34774,4,1,19,8,7))
if mibBuilder.loadTexts:hwStorageFCPortTable.setStatus(_A)
_HwStorageFCPortEntry_Object=MibTableRow
hwStorageFCPortEntry=_HwStorageFCPortEntry_Object((1,3,6,1,4,1,34774,4,1,19,8,7,1))
hwStorageFCPortEntry.setIndexNames((0,_B,_J))
if mibBuilder.loadTexts:hwStorageFCPortEntry.setStatus(_A)
_HwStorageFCPortIfIndex_Type=Unsigned32
_HwStorageFCPortIfIndex_Object=MibTableColumn
hwStorageFCPortIfIndex=_HwStorageFCPortIfIndex_Object((1,3,6,1,4,1,34774,4,1,19,8,7,1,1),_HwStorageFCPortIfIndex_Type())
hwStorageFCPortIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:hwStorageFCPortIfIndex.setStatus(_A)
_HwStorageFCPortBoardIfIndex_Type=Unsigned32
_HwStorageFCPortBoardIfIndex_Object=MibTableColumn
hwStorageFCPortBoardIfIndex=_HwStorageFCPortBoardIfIndex_Object((1,3,6,1,4,1,34774,4,1,19,8,7,1,2),_HwStorageFCPortBoardIfIndex_Type())
hwStorageFCPortBoardIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:hwStorageFCPortBoardIfIndex.setStatus(_A)
_HwStorageFCPortID_Type=Unsigned32
_HwStorageFCPortID_Object=MibTableColumn
hwStorageFCPortID=_HwStorageFCPortID_Object((1,3,6,1,4,1,34774,4,1,19,8,7,1,3),_HwStorageFCPortID_Type())
hwStorageFCPortID.setMaxAccess(_C)
if mibBuilder.loadTexts:hwStorageFCPortID.setStatus(_A)
class _HwStorageFCPortStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_G,0),(_H,1),(_F,2)))
_HwStorageFCPortStatus_Type.__name__=_D
_HwStorageFCPortStatus_Object=MibTableColumn
hwStorageFCPortStatus=_HwStorageFCPortStatus_Object((1,3,6,1,4,1,34774,4,1,19,8,7,1,4),_HwStorageFCPortStatus_Type())
hwStorageFCPortStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:hwStorageFCPortStatus.setStatus(_A)
class _HwStorageFCPortConfigRate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,4,8,16)));namedValues=NamedValues(*(('auto',0),('gbps1',1),('gbps2',2),('gbps4',4),('gbps8',8),(_Y,16)))
_HwStorageFCPortConfigRate_Type.__name__=_D
_HwStorageFCPortConfigRate_Object=MibTableColumn
hwStorageFCPortConfigRate=_HwStorageFCPortConfigRate_Object((1,3,6,1,4,1,34774,4,1,19,8,7,1,5),_HwStorageFCPortConfigRate_Type())
hwStorageFCPortConfigRate.setMaxAccess(_E)
if mibBuilder.loadTexts:hwStorageFCPortConfigRate.setStatus(_A)
class _HwStorageFCPortMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('fabric',1),('publicloop',2),('pointtopoint',3)))
_HwStorageFCPortMode_Type.__name__=_D
_HwStorageFCPortMode_Object=MibTableColumn
hwStorageFCPortMode=_HwStorageFCPortMode_Object((1,3,6,1,4,1,34774,4,1,19,8,7,1,6),_HwStorageFCPortMode_Type())
hwStorageFCPortMode.setMaxAccess(_E)
if mibBuilder.loadTexts:hwStorageFCPortMode.setStatus(_A)
_HwStorageFCPortWWN_Type=OctetString
_HwStorageFCPortWWN_Object=MibTableColumn
hwStorageFCPortWWN=_HwStorageFCPortWWN_Object((1,3,6,1,4,1,34774,4,1,19,8,7,1,7),_HwStorageFCPortWWN_Type())
hwStorageFCPortWWN.setMaxAccess(_C)
if mibBuilder.loadTexts:hwStorageFCPortWWN.setStatus(_A)
class _HwStorageFCPortLogicType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,8)));namedValues=NamedValues(*((_K,1),(_L,2),(_M,3),(_I,4),(_N,5),(_O,6),(_P,8)))
_HwStorageFCPortLogicType_Type.__name__=_D
_HwStorageFCPortLogicType_Object=MibTableColumn
hwStorageFCPortLogicType=_HwStorageFCPortLogicType_Object((1,3,6,1,4,1,34774,4,1,19,8,7,1,8),_HwStorageFCPortLogicType_Type())
hwStorageFCPortLogicType.setMaxAccess(_C)
if mibBuilder.loadTexts:hwStorageFCPortLogicType.setStatus(_A)
class _HwStorageFCPortSpeedRate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,4,8,16)));namedValues=NamedValues(*(('auto',0),('gbps1',1),('gbps2',2),('gbps4',4),('gbps8',8),(_Y,16)))
_HwStorageFCPortSpeedRate_Type.__name__=_D
_HwStorageFCPortSpeedRate_Object=MibTableColumn
hwStorageFCPortSpeedRate=_HwStorageFCPortSpeedRate_Object((1,3,6,1,4,1,34774,4,1,19,8,7,1,9),_HwStorageFCPortSpeedRate_Type())
hwStorageFCPortSpeedRate.setMaxAccess(_C)
if mibBuilder.loadTexts:hwStorageFCPortSpeedRate.setStatus(_A)
_HwStorageSASPortTable_Object=MibTable
hwStorageSASPortTable=_HwStorageSASPortTable_Object((1,3,6,1,4,1,34774,4,1,19,8,8))
if mibBuilder.loadTexts:hwStorageSASPortTable.setStatus(_A)
_HwStorageSASPortEntry_Object=MibTableRow
hwStorageSASPortEntry=_HwStorageSASPortEntry_Object((1,3,6,1,4,1,34774,4,1,19,8,8,1))
hwStorageSASPortEntry.setIndexNames((0,_B,_Q))
if mibBuilder.loadTexts:hwStorageSASPortEntry.setStatus(_A)
_HwStorageSASPortIfIndex_Type=Unsigned32
_HwStorageSASPortIfIndex_Object=MibTableColumn
hwStorageSASPortIfIndex=_HwStorageSASPortIfIndex_Object((1,3,6,1,4,1,34774,4,1,19,8,8,1,1),_HwStorageSASPortIfIndex_Type())
hwStorageSASPortIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:hwStorageSASPortIfIndex.setStatus(_A)
_HwStorageSASPortBoardIfIndex_Type=Unsigned32
_HwStorageSASPortBoardIfIndex_Object=MibTableColumn
hwStorageSASPortBoardIfIndex=_HwStorageSASPortBoardIfIndex_Object((1,3,6,1,4,1,34774,4,1,19,8,8,1,2),_HwStorageSASPortBoardIfIndex_Type())
hwStorageSASPortBoardIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:hwStorageSASPortBoardIfIndex.setStatus(_A)
_HwStorageSASPortID_Type=Unsigned32
_HwStorageSASPortID_Object=MibTableColumn
hwStorageSASPortID=_HwStorageSASPortID_Object((1,3,6,1,4,1,34774,4,1,19,8,8,1,3),_HwStorageSASPortID_Type())
hwStorageSASPortID.setMaxAccess(_C)
if mibBuilder.loadTexts:hwStorageSASPortID.setStatus(_A)
class _HwStorageSASPortStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_G,0),(_H,1),(_F,2)))
_HwStorageSASPortStatus_Type.__name__=_D
_HwStorageSASPortStatus_Object=MibTableColumn
hwStorageSASPortStatus=_HwStorageSASPortStatus_Object((1,3,6,1,4,1,34774,4,1,19,8,8,1,4),_HwStorageSASPortStatus_Type())
hwStorageSASPortStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:hwStorageSASPortStatus.setStatus(_A)
class _HwStorageSASPortConfigRate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1500,3000,6000)));namedValues=NamedValues(*((_Z,1500),(_a,3000),(_b,6000)))
_HwStorageSASPortConfigRate_Type.__name__=_D
_HwStorageSASPortConfigRate_Object=MibTableColumn
hwStorageSASPortConfigRate=_HwStorageSASPortConfigRate_Object((1,3,6,1,4,1,34774,4,1,19,8,8,1,5),_HwStorageSASPortConfigRate_Type())
hwStorageSASPortConfigRate.setMaxAccess(_C)
if mibBuilder.loadTexts:hwStorageSASPortConfigRate.setStatus(_A)
_HwStorageSASPortWWN_Type=OctetString
_HwStorageSASPortWWN_Object=MibTableColumn
hwStorageSASPortWWN=_HwStorageSASPortWWN_Object((1,3,6,1,4,1,34774,4,1,19,8,8,1,6),_HwStorageSASPortWWN_Type())
hwStorageSASPortWWN.setMaxAccess(_C)
if mibBuilder.loadTexts:hwStorageSASPortWWN.setStatus(_A)
class _HwStorageSASPortLogicType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,8)));namedValues=NamedValues(*((_K,1),(_L,2),(_M,3),(_I,4),(_N,5),(_O,6),(_P,8)))
_HwStorageSASPortLogicType_Type.__name__=_D
_HwStorageSASPortLogicType_Object=MibTableColumn
hwStorageSASPortLogicType=_HwStorageSASPortLogicType_Object((1,3,6,1,4,1,34774,4,1,19,8,8,1,7),_HwStorageSASPortLogicType_Type())
hwStorageSASPortLogicType.setMaxAccess(_C)
if mibBuilder.loadTexts:hwStorageSASPortLogicType.setStatus(_A)
class _HwStorageSASPortSpeedRate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1500,3000,6000)));namedValues=NamedValues(*((_Z,1500),(_a,3000),(_b,6000)))
_HwStorageSASPortSpeedRate_Type.__name__=_D
_HwStorageSASPortSpeedRate_Object=MibTableColumn
hwStorageSASPortSpeedRate=_HwStorageSASPortSpeedRate_Object((1,3,6,1,4,1,34774,4,1,19,8,8,1,8),_HwStorageSASPortSpeedRate_Type())
hwStorageSASPortSpeedRate.setMaxAccess(_C)
if mibBuilder.loadTexts:hwStorageSASPortSpeedRate.setStatus(_A)
_HwStorageISCSIPortTable_Object=MibTable
hwStorageISCSIPortTable=_HwStorageISCSIPortTable_Object((1,3,6,1,4,1,34774,4,1,19,8,9))
if mibBuilder.loadTexts:hwStorageISCSIPortTable.setStatus(_A)
_HwStorageISCSIPortEntry_Object=MibTableRow
hwStorageISCSIPortEntry=_HwStorageISCSIPortEntry_Object((1,3,6,1,4,1,34774,4,1,19,8,9,1))
hwStorageISCSIPortEntry.setIndexNames((0,_B,_R))
if mibBuilder.loadTexts:hwStorageISCSIPortEntry.setStatus(_A)
_HwStorageISCSIPortIfIndex_Type=Unsigned32
_HwStorageISCSIPortIfIndex_Object=MibTableColumn
hwStorageISCSIPortIfIndex=_HwStorageISCSIPortIfIndex_Object((1,3,6,1,4,1,34774,4,1,19,8,9,1,1),_HwStorageISCSIPortIfIndex_Type())
hwStorageISCSIPortIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:hwStorageISCSIPortIfIndex.setStatus(_A)
_HwStorageISCSIPortBoardIfIndex_Type=Unsigned32
_HwStorageISCSIPortBoardIfIndex_Object=MibTableColumn
hwStorageISCSIPortBoardIfIndex=_HwStorageISCSIPortBoardIfIndex_Object((1,3,6,1,4,1,34774,4,1,19,8,9,1,2),_HwStorageISCSIPortBoardIfIndex_Type())
hwStorageISCSIPortBoardIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:hwStorageISCSIPortBoardIfIndex.setStatus(_A)
_HwStorageISCSIPortID_Type=Unsigned32
_HwStorageISCSIPortID_Object=MibTableColumn
hwStorageISCSIPortID=_HwStorageISCSIPortID_Object((1,3,6,1,4,1,34774,4,1,19,8,9,1,3),_HwStorageISCSIPortID_Type())
hwStorageISCSIPortID.setMaxAccess(_C)
if mibBuilder.loadTexts:hwStorageISCSIPortID.setStatus(_A)
class _HwStorageISCSIPortStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_G,0),(_H,1),(_F,2)))
_HwStorageISCSIPortStatus_Type.__name__=_D
_HwStorageISCSIPortStatus_Object=MibTableColumn
hwStorageISCSIPortStatus=_HwStorageISCSIPortStatus_Object((1,3,6,1,4,1,34774,4,1,19,8,9,1,4),_HwStorageISCSIPortStatus_Type())
hwStorageISCSIPortStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:hwStorageISCSIPortStatus.setStatus(_A)
_HwStorageISCSIPortIP_Type=IpAddress
_HwStorageISCSIPortIP_Object=MibTableColumn
hwStorageISCSIPortIP=_HwStorageISCSIPortIP_Object((1,3,6,1,4,1,34774,4,1,19,8,9,1,5),_HwStorageISCSIPortIP_Type())
hwStorageISCSIPortIP.setMaxAccess(_E)
if mibBuilder.loadTexts:hwStorageISCSIPortIP.setStatus(_A)
_HwStorageISCSIPortNetMask_Type=IpAddress
_HwStorageISCSIPortNetMask_Object=MibTableColumn
hwStorageISCSIPortNetMask=_HwStorageISCSIPortNetMask_Object((1,3,6,1,4,1,34774,4,1,19,8,9,1,6),_HwStorageISCSIPortNetMask_Type())
hwStorageISCSIPortNetMask.setMaxAccess(_E)
if mibBuilder.loadTexts:hwStorageISCSIPortNetMask.setStatus(_A)
_HwStorageISCSIPortBindMode_Type=Integer32
_HwStorageISCSIPortBindMode_Object=MibTableColumn
hwStorageISCSIPortBindMode=_HwStorageISCSIPortBindMode_Object((1,3,6,1,4,1,34774,4,1,19,8,9,1,7),_HwStorageISCSIPortBindMode_Type())
hwStorageISCSIPortBindMode.setMaxAccess(_C)
if mibBuilder.loadTexts:hwStorageISCSIPortBindMode.setStatus(_A)
class _HwStorageISCSIPortLogicType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,8)));namedValues=NamedValues(*((_K,1),(_L,2),(_M,3),(_I,4),(_N,5),(_O,6),(_P,8)))
_HwStorageISCSIPortLogicType_Type.__name__=_D
_HwStorageISCSIPortLogicType_Object=MibTableColumn
hwStorageISCSIPortLogicType=_HwStorageISCSIPortLogicType_Object((1,3,6,1,4,1,34774,4,1,19,8,9,1,8),_HwStorageISCSIPortLogicType_Type())
hwStorageISCSIPortLogicType.setMaxAccess(_C)
if mibBuilder.loadTexts:hwStorageISCSIPortLogicType.setStatus(_A)
_HwStorageFrontEndHostPortTable_Object=MibTable
hwStorageFrontEndHostPortTable=_HwStorageFrontEndHostPortTable_Object((1,3,6,1,4,1,34774,4,1,19,8,11))
if mibBuilder.loadTexts:hwStorageFrontEndHostPortTable.setStatus(_A)
_HwStorageFrontEndHostPortEntry_Object=MibTableRow
hwStorageFrontEndHostPortEntry=_HwStorageFrontEndHostPortEntry_Object((1,3,6,1,4,1,34774,4,1,19,8,11,1))
hwStorageFrontEndHostPortEntry.setIndexNames((0,_B,_S))
if mibBuilder.loadTexts:hwStorageFrontEndHostPortEntry.setStatus(_A)
_HwStorageFrontEndHostPortIfIndex_Type=Unsigned32
_HwStorageFrontEndHostPortIfIndex_Object=MibTableColumn
hwStorageFrontEndHostPortIfIndex=_HwStorageFrontEndHostPortIfIndex_Object((1,3,6,1,4,1,34774,4,1,19,8,11,1,1),_HwStorageFrontEndHostPortIfIndex_Type())
hwStorageFrontEndHostPortIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:hwStorageFrontEndHostPortIfIndex.setStatus(_A)
class _HwStorageFrontEndHostPortType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,5)));namedValues=NamedValues(*(('sas',0),('fc',1),('iscsi',5)))
_HwStorageFrontEndHostPortType_Type.__name__=_D
_HwStorageFrontEndHostPortType_Object=MibTableColumn
hwStorageFrontEndHostPortType=_HwStorageFrontEndHostPortType_Object((1,3,6,1,4,1,34774,4,1,19,8,11,1,2),_HwStorageFrontEndHostPortType_Type())
hwStorageFrontEndHostPortType.setMaxAccess(_C)
if mibBuilder.loadTexts:hwStorageFrontEndHostPortType.setStatus(_A)
class _HwStorageFrontEndHostPortStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*((_G,0),(_H,1),(_F,2),('unknown',3)))
_HwStorageFrontEndHostPortStatus_Type.__name__=_D
_HwStorageFrontEndHostPortStatus_Object=MibTableColumn
hwStorageFrontEndHostPortStatus=_HwStorageFrontEndHostPortStatus_Object((1,3,6,1,4,1,34774,4,1,19,8,11,1,3),_HwStorageFrontEndHostPortStatus_Type())
hwStorageFrontEndHostPortStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:hwStorageFrontEndHostPortStatus.setStatus(_A)
_HwStorageFrontEndHostPortPhysAddress_Type=OctetString
_HwStorageFrontEndHostPortPhysAddress_Object=MibTableColumn
hwStorageFrontEndHostPortPhysAddress=_HwStorageFrontEndHostPortPhysAddress_Object((1,3,6,1,4,1,34774,4,1,19,8,11,1,4),_HwStorageFrontEndHostPortPhysAddress_Type())
hwStorageFrontEndHostPortPhysAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:hwStorageFrontEndHostPortPhysAddress.setStatus(_A)
_HwStorageFrontEndHostPortDescription_Type=OctetString
_HwStorageFrontEndHostPortDescription_Object=MibTableColumn
hwStorageFrontEndHostPortDescription=_HwStorageFrontEndHostPortDescription_Object((1,3,6,1,4,1,34774,4,1,19,8,11,1,5),_HwStorageFrontEndHostPortDescription_Type())
hwStorageFrontEndHostPortDescription.setMaxAccess(_C)
if mibBuilder.loadTexts:hwStorageFrontEndHostPortDescription.setStatus(_A)
_HwStorageControllerTable_Object=MibTable
hwStorageControllerTable=_HwStorageControllerTable_Object((1,3,6,1,4,1,34774,4,1,19,8,12))
if mibBuilder.loadTexts:hwStorageControllerTable.setStatus(_A)
_HwStorageControllerEntry_Object=MibTableRow
hwStorageControllerEntry=_HwStorageControllerEntry_Object((1,3,6,1,4,1,34774,4,1,19,8,12,1))
hwStorageControllerEntry.setIndexNames((0,_B,_T))
if mibBuilder.loadTexts:hwStorageControllerEntry.setStatus(_A)
_HwStorageControllerID_Type=Unsigned32
_HwStorageControllerID_Object=MibTableColumn
hwStorageControllerID=_HwStorageControllerID_Object((1,3,6,1,4,1,34774,4,1,19,8,12,1,1),_HwStorageControllerID_Type())
hwStorageControllerID.setMaxAccess(_C)
if mibBuilder.loadTexts:hwStorageControllerID.setStatus(_A)
_HwStorageControllerName_Type=OctetString
_HwStorageControllerName_Object=MibTableColumn
hwStorageControllerName=_HwStorageControllerName_Object((1,3,6,1,4,1,34774,4,1,19,8,12,1,2),_HwStorageControllerName_Type())
hwStorageControllerName.setMaxAccess(_C)
if mibBuilder.loadTexts:hwStorageControllerName.setStatus(_A)
_HwStorageControllerLocation_Type=OctetString
_HwStorageControllerLocation_Object=MibTableColumn
hwStorageControllerLocation=_HwStorageControllerLocation_Object((1,3,6,1,4,1,34774,4,1,19,8,12,1,3),_HwStorageControllerLocation_Type())
hwStorageControllerLocation.setMaxAccess(_C)
if mibBuilder.loadTexts:hwStorageControllerLocation.setStatus(_A)
class _HwStorageControllerHealthStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13)));namedValues=NamedValues(*((_U,1),(_F,2),('preFail',3),('partiallyBroken',4),('degraded',5),('badSectorsFound',6),('bitErrorsFound',7),(_c,8),('inconsistent',9),('busy',10),('noInput',11),('lowBattery',12),('singleLinkFault',13)))
_HwStorageControllerHealthStatus_Type.__name__=_D
_HwStorageControllerHealthStatus_Object=MibTableColumn
hwStorageControllerHealthStatus=_HwStorageControllerHealthStatus_Object((1,3,6,1,4,1,34774,4,1,19,8,12,1,4),_HwStorageControllerHealthStatus_Type())
hwStorageControllerHealthStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:hwStorageControllerHealthStatus.setStatus(_A)
class _HwStorageControllerRunningStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,63,64)));namedValues=NamedValues(*((_U,1),('running',2),('notRunning',3),('notExisted',4),('sleepInHighTemperature',5),('starting',6),('powerFailureProtecting',7),('spinDown',8),('started',9),('linkUp',10),('linkDown',11),('poweringOn',12),('poweredOff',13),('precopy',14),('copyback',15),('reconstruction',16),(_I,17),('unformatted',18),(_d,19),('unmapped',20),('initialSynchronizing',21),(_c,22),('synchronizing',23),('synchronized',24),('unsynchronized',25),('splited',26),('online',27),('offline',28),('locked',29),('enabled',30),('disabled',31),('balancing',32),('toBeRecoverd',33),('interrupted',34),('invalid',35),('notStart',36),('queuing',37),('stopped',38),('copying',39),('completed',40),('paused',41),('reverseSynchronizing',42),('activated',43),('restore',44),('inactive',45),('idle',46),('poweringOff',47),('charging',48),('chargingCompleted',49),('discharging',50),('upgrading',51),('runningNormal',63),('runningFail',64)))
_HwStorageControllerRunningStatus_Type.__name__=_D
_HwStorageControllerRunningStatus_Object=MibTableColumn
hwStorageControllerRunningStatus=_HwStorageControllerRunningStatus_Object((1,3,6,1,4,1,34774,4,1,19,8,12,1,5),_HwStorageControllerRunningStatus_Type())
hwStorageControllerRunningStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:hwStorageControllerRunningStatus.setStatus(_A)
_HwStorageControllerSoftVer_Type=OctetString
_HwStorageControllerSoftVer_Object=MibTableColumn
hwStorageControllerSoftVer=_HwStorageControllerSoftVer_Object((1,3,6,1,4,1,34774,4,1,19,8,12,1,6),_HwStorageControllerSoftVer_Type())
hwStorageControllerSoftVer.setMaxAccess(_C)
if mibBuilder.loadTexts:hwStorageControllerSoftVer.setStatus(_A)
_HwStorageControllerTemperature_Type=Integer32
_HwStorageControllerTemperature_Object=MibTableColumn
hwStorageControllerTemperature=_HwStorageControllerTemperature_Object((1,3,6,1,4,1,34774,4,1,19,8,12,1,7),_HwStorageControllerTemperature_Type())
hwStorageControllerTemperature.setMaxAccess(_C)
if mibBuilder.loadTexts:hwStorageControllerTemperature.setStatus(_A)
_HwStorageControllerIsMaster_Type=Unsigned32
_HwStorageControllerIsMaster_Object=MibTableColumn
hwStorageControllerIsMaster=_HwStorageControllerIsMaster_Object((1,3,6,1,4,1,34774,4,1,19,8,12,1,8),_HwStorageControllerIsMaster_Type())
hwStorageControllerIsMaster.setMaxAccess(_C)
if mibBuilder.loadTexts:hwStorageControllerIsMaster.setStatus(_A)
_HwStorageControllerELabel_Type=OctetString
_HwStorageControllerELabel_Object=MibTableColumn
hwStorageControllerELabel=_HwStorageControllerELabel_Object((1,3,6,1,4,1,34774,4,1,19,8,12,1,9),_HwStorageControllerELabel_Type())
hwStorageControllerELabel.setMaxAccess(_C)
if mibBuilder.loadTexts:hwStorageControllerELabel.setStatus(_A)
_HwStorageControllerPCBVer_Type=OctetString
_HwStorageControllerPCBVer_Object=MibTableColumn
hwStorageControllerPCBVer=_HwStorageControllerPCBVer_Object((1,3,6,1,4,1,34774,4,1,19,8,12,1,10),_HwStorageControllerPCBVer_Type())
hwStorageControllerPCBVer.setMaxAccess(_C)
if mibBuilder.loadTexts:hwStorageControllerPCBVer.setStatus(_A)
_HwStorageControllerBMCVer_Type=OctetString
_HwStorageControllerBMCVer_Object=MibTableColumn
hwStorageControllerBMCVer=_HwStorageControllerBMCVer_Object((1,3,6,1,4,1,34774,4,1,19,8,12,1,11),_HwStorageControllerBMCVer_Type())
hwStorageControllerBMCVer.setMaxAccess(_C)
if mibBuilder.loadTexts:hwStorageControllerBMCVer.setStatus(_A)
_HwStorageControllerLogicVer_Type=OctetString
_HwStorageControllerLogicVer_Object=MibTableColumn
hwStorageControllerLogicVer=_HwStorageControllerLogicVer_Object((1,3,6,1,4,1,34774,4,1,19,8,12,1,12),_HwStorageControllerLogicVer_Type())
hwStorageControllerLogicVer.setMaxAccess(_C)
if mibBuilder.loadTexts:hwStorageControllerLogicVer.setStatus(_A)
_HwStorageControllerBIOSVer_Type=OctetString
_HwStorageControllerBIOSVer_Object=MibTableColumn
hwStorageControllerBIOSVer=_HwStorageControllerBIOSVer_Object((1,3,6,1,4,1,34774,4,1,19,8,12,1,13),_HwStorageControllerBIOSVer_Type())
hwStorageControllerBIOSVer.setMaxAccess(_C)
if mibBuilder.loadTexts:hwStorageControllerBIOSVer.setStatus(_A)
_HwStorageControllerMemorySize_Type=Unsigned32
_HwStorageControllerMemorySize_Object=MibTableColumn
hwStorageControllerMemorySize=_HwStorageControllerMemorySize_Object((1,3,6,1,4,1,34774,4,1,19,8,12,1,14),_HwStorageControllerMemorySize_Type())
hwStorageControllerMemorySize.setMaxAccess(_C)
if mibBuilder.loadTexts:hwStorageControllerMemorySize.setStatus(_A)
_HwStorageControllerCPUInfo_Type=OctetString
_HwStorageControllerCPUInfo_Object=MibTableColumn
hwStorageControllerCPUInfo=_HwStorageControllerCPUInfo_Object((1,3,6,1,4,1,34774,4,1,19,8,12,1,15),_HwStorageControllerCPUInfo_Type())
hwStorageControllerCPUInfo.setMaxAccess(_C)
if mibBuilder.loadTexts:hwStorageControllerCPUInfo.setStatus(_A)
_HwStorageControllerVoltage_Type=Unsigned32
_HwStorageControllerVoltage_Object=MibTableColumn
hwStorageControllerVoltage=_HwStorageControllerVoltage_Object((1,3,6,1,4,1,34774,4,1,19,8,12,1,16),_HwStorageControllerVoltage_Type())
hwStorageControllerVoltage.setMaxAccess(_C)
if mibBuilder.loadTexts:hwStorageControllerVoltage.setStatus(_A)
_HwStorageLogicModule_ObjectIdentity=ObjectIdentity
hwStorageLogicModule=_HwStorageLogicModule_ObjectIdentity((1,3,6,1,4,1,34774,4,1,19,9))
_HwStorageCacheTable_Object=MibTable
hwStorageCacheTable=_HwStorageCacheTable_Object((1,3,6,1,4,1,34774,4,1,19,9,1))
if mibBuilder.loadTexts:hwStorageCacheTable.setStatus(_A)
_HwStorageCacheEntry_Object=MibTableRow
hwStorageCacheEntry=_HwStorageCacheEntry_Object((1,3,6,1,4,1,34774,4,1,19,9,1,1))
hwStorageCacheEntry.setIndexNames((0,_B,_V))
if mibBuilder.loadTexts:hwStorageCacheEntry.setStatus(_A)
_HwStorageCacheID_Type=Unsigned32
_HwStorageCacheID_Object=MibTableColumn
hwStorageCacheID=_HwStorageCacheID_Object((1,3,6,1,4,1,34774,4,1,19,9,1,1,1),_HwStorageCacheID_Type())
hwStorageCacheID.setMaxAccess(_C)
if mibBuilder.loadTexts:hwStorageCacheID.setStatus(_A)
_HwStorageCacheTotalCapacity_Type=Unsigned32
_HwStorageCacheTotalCapacity_Object=MibTableColumn
hwStorageCacheTotalCapacity=_HwStorageCacheTotalCapacity_Object((1,3,6,1,4,1,34774,4,1,19,9,1,1,2),_HwStorageCacheTotalCapacity_Type())
hwStorageCacheTotalCapacity.setMaxAccess(_C)
if mibBuilder.loadTexts:hwStorageCacheTotalCapacity.setStatus(_A)
if mibBuilder.loadTexts:hwStorageCacheTotalCapacity.setUnits('MB')
_HwStorageCacheHighWaterLevel_Type=Unsigned32
_HwStorageCacheHighWaterLevel_Object=MibTableColumn
hwStorageCacheHighWaterLevel=_HwStorageCacheHighWaterLevel_Object((1,3,6,1,4,1,34774,4,1,19,9,1,1,3),_HwStorageCacheHighWaterLevel_Type())
hwStorageCacheHighWaterLevel.setMaxAccess(_E)
if mibBuilder.loadTexts:hwStorageCacheHighWaterLevel.setStatus(_A)
_HwStorageCacheLowWaterLevel_Type=Unsigned32
_HwStorageCacheLowWaterLevel_Object=MibTableColumn
hwStorageCacheLowWaterLevel=_HwStorageCacheLowWaterLevel_Object((1,3,6,1,4,1,34774,4,1,19,9,1,1,4),_HwStorageCacheLowWaterLevel_Type())
hwStorageCacheLowWaterLevel.setMaxAccess(_E)
if mibBuilder.loadTexts:hwStorageCacheLowWaterLevel.setStatus(_A)
_HwStorageCacheRowStatus_Type=RowStatus
_HwStorageCacheRowStatus_Object=MibTableColumn
hwStorageCacheRowStatus=_HwStorageCacheRowStatus_Object((1,3,6,1,4,1,34774,4,1,19,9,1,1,5),_HwStorageCacheRowStatus_Type())
hwStorageCacheRowStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:hwStorageCacheRowStatus.setStatus(_A)
_HwStorageLunTable_Object=MibTable
hwStorageLunTable=_HwStorageLunTable_Object((1,3,6,1,4,1,34774,4,1,19,9,4))
if mibBuilder.loadTexts:hwStorageLunTable.setStatus(_A)
_HwStorageLunEntry_Object=MibTableRow
hwStorageLunEntry=_HwStorageLunEntry_Object((1,3,6,1,4,1,34774,4,1,19,9,4,1))
hwStorageLunEntry.setIndexNames((0,_B,_W))
if mibBuilder.loadTexts:hwStorageLunEntry.setStatus(_A)
_HwStorageLunID_Type=Unsigned32
_HwStorageLunID_Object=MibTableColumn
hwStorageLunID=_HwStorageLunID_Object((1,3,6,1,4,1,34774,4,1,19,9,4,1,1),_HwStorageLunID_Type())
hwStorageLunID.setMaxAccess(_C)
if mibBuilder.loadTexts:hwStorageLunID.setStatus(_A)
_HwStorageLunName_Type=OctetString
_HwStorageLunName_Object=MibTableColumn
hwStorageLunName=_HwStorageLunName_Object((1,3,6,1,4,1,34774,4,1,19,9,4,1,2),_HwStorageLunName_Type())
hwStorageLunName.setMaxAccess(_C)
if mibBuilder.loadTexts:hwStorageLunName.setStatus(_A)
_HwStorageLunWWN_Type=OctetString
_HwStorageLunWWN_Object=MibTableColumn
hwStorageLunWWN=_HwStorageLunWWN_Object((1,3,6,1,4,1,34774,4,1,19,9,4,1,3),_HwStorageLunWWN_Type())
hwStorageLunWWN.setMaxAccess(_C)
if mibBuilder.loadTexts:hwStorageLunWWN.setStatus(_A)
_HwStorageLunPoolID_Type=Unsigned32
_HwStorageLunPoolID_Object=MibTableColumn
hwStorageLunPoolID=_HwStorageLunPoolID_Object((1,3,6,1,4,1,34774,4,1,19,9,4,1,4),_HwStorageLunPoolID_Type())
hwStorageLunPoolID.setMaxAccess(_C)
if mibBuilder.loadTexts:hwStorageLunPoolID.setStatus(_A)
_HwStorageLunCapacity_Type=Counter64
_HwStorageLunCapacity_Object=MibTableColumn
hwStorageLunCapacity=_HwStorageLunCapacity_Object((1,3,6,1,4,1,34774,4,1,19,9,4,1,5),_HwStorageLunCapacity_Type())
hwStorageLunCapacity.setMaxAccess(_C)
if mibBuilder.loadTexts:hwStorageLunCapacity.setStatus(_A)
_HwStorageLunOwningController_Type=Unsigned32
_HwStorageLunOwningController_Object=MibTableColumn
hwStorageLunOwningController=_HwStorageLunOwningController_Object((1,3,6,1,4,1,34774,4,1,19,9,4,1,6),_HwStorageLunOwningController_Type())
hwStorageLunOwningController.setMaxAccess(_C)
if mibBuilder.loadTexts:hwStorageLunOwningController.setStatus(_A)
_HwStorageLunStripDepth_Type=Unsigned32
_HwStorageLunStripDepth_Object=MibTableColumn
hwStorageLunStripDepth=_HwStorageLunStripDepth_Object((1,3,6,1,4,1,34774,4,1,19,9,4,1,7),_HwStorageLunStripDepth_Type())
hwStorageLunStripDepth.setMaxAccess(_C)
if mibBuilder.loadTexts:hwStorageLunStripDepth.setStatus(_A)
class _HwStorageLunWriteStrategy_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('writethrough',1),('writebacknomirroring',2),('writebackmirroring',3),('writebackmandatorynomirroring',4),('writebackmandatorymirroring',5)))
_HwStorageLunWriteStrategy_Type.__name__=_D
_HwStorageLunWriteStrategy_Object=MibTableColumn
hwStorageLunWriteStrategy=_HwStorageLunWriteStrategy_Object((1,3,6,1,4,1,34774,4,1,19,9,4,1,8),_HwStorageLunWriteStrategy_Type())
hwStorageLunWriteStrategy.setMaxAccess(_C)
if mibBuilder.loadTexts:hwStorageLunWriteStrategy.setStatus(_A)
class _HwStorageLunPrefetchStrategy_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*(('none',0),('constant',1),('variable',2),('intelligent',3)))
_HwStorageLunPrefetchStrategy_Type.__name__=_D
_HwStorageLunPrefetchStrategy_Object=MibTableColumn
hwStorageLunPrefetchStrategy=_HwStorageLunPrefetchStrategy_Object((1,3,6,1,4,1,34774,4,1,19,9,4,1,9),_HwStorageLunPrefetchStrategy_Type())
hwStorageLunPrefetchStrategy.setMaxAccess(_C)
if mibBuilder.loadTexts:hwStorageLunPrefetchStrategy.setStatus(_A)
_HwStorageLunPrefetchValue_Type=Unsigned32
_HwStorageLunPrefetchValue_Object=MibTableColumn
hwStorageLunPrefetchValue=_HwStorageLunPrefetchValue_Object((1,3,6,1,4,1,34774,4,1,19,9,4,1,10),_HwStorageLunPrefetchValue_Type())
hwStorageLunPrefetchValue.setMaxAccess(_C)
if mibBuilder.loadTexts:hwStorageLunPrefetchValue.setStatus(_A)
class _HwStorageLunStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_U,1),(_F,2),('notformat',3),(_d,4)))
_HwStorageLunStatus_Type.__name__=_D
_HwStorageLunStatus_Object=MibTableColumn
hwStorageLunStatus=_HwStorageLunStatus_Object((1,3,6,1,4,1,34774,4,1,19,9,4,1,11),_HwStorageLunStatus_Type())
hwStorageLunStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:hwStorageLunStatus.setStatus(_A)
_HwStorageLunRowStatus_Type=RowStatus
_HwStorageLunRowStatus_Object=MibTableColumn
hwStorageLunRowStatus=_HwStorageLunRowStatus_Object((1,3,6,1,4,1,34774,4,1,19,9,4,1,50),_HwStorageLunRowStatus_Type())
hwStorageLunRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:hwStorageLunRowStatus.setStatus(_A)
_HwStorageNodeTable_Object=MibTable
hwStorageNodeTable=_HwStorageNodeTable_Object((1,3,6,1,4,1,34774,4,1,19,9,6))
if mibBuilder.loadTexts:hwStorageNodeTable.setStatus(_A)
_HwStorageNodeEntry_Object=MibTableRow
hwStorageNodeEntry=_HwStorageNodeEntry_Object((1,3,6,1,4,1,34774,4,1,19,9,6,1))
hwStorageNodeEntry.setIndexNames((0,_B,_X))
if mibBuilder.loadTexts:hwStorageNodeEntry.setStatus(_A)
_HwStorageNodeIfIndex_Type=Unsigned32
_HwStorageNodeIfIndex_Object=MibTableColumn
hwStorageNodeIfIndex=_HwStorageNodeIfIndex_Object((1,3,6,1,4,1,34774,4,1,19,9,6,1,1),_HwStorageNodeIfIndex_Type())
hwStorageNodeIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:hwStorageNodeIfIndex.setStatus(_A)
_HwStorageNodeIPAddress_Type=IpAddress
_HwStorageNodeIPAddress_Object=MibTableColumn
hwStorageNodeIPAddress=_HwStorageNodeIPAddress_Object((1,3,6,1,4,1,34774,4,1,19,9,6,1,2),_HwStorageNodeIPAddress_Type())
hwStorageNodeIPAddress.setMaxAccess(_E)
if mibBuilder.loadTexts:hwStorageNodeIPAddress.setStatus(_A)
_HwStorageNodeStatus_Type=Unsigned32
_HwStorageNodeStatus_Object=MibTableColumn
hwStorageNodeStatus=_HwStorageNodeStatus_Object((1,3,6,1,4,1,34774,4,1,19,9,6,1,3),_HwStorageNodeStatus_Type())
hwStorageNodeStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:hwStorageNodeStatus.setStatus(_A)
_HwStorageNodeIsMaster_Type=Unsigned32
_HwStorageNodeIsMaster_Object=MibTableColumn
hwStorageNodeIsMaster=_HwStorageNodeIsMaster_Object((1,3,6,1,4,1,34774,4,1,19,9,6,1,4),_HwStorageNodeIsMaster_Type())
hwStorageNodeIsMaster.setMaxAccess(_E)
if mibBuilder.loadTexts:hwStorageNodeIsMaster.setStatus(_A)
_HwStorageNodeRowStatus_Type=RowStatus
_HwStorageNodeRowStatus_Object=MibTableColumn
hwStorageNodeRowStatus=_HwStorageNodeRowStatus_Object((1,3,6,1,4,1,34774,4,1,19,9,6,1,20),_HwStorageNodeRowStatus_Type())
hwStorageNodeRowStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:hwStorageNodeRowStatus.setStatus(_A)
_IsoConformance_ObjectIdentity=ObjectIdentity
isoConformance=_IsoConformance_ObjectIdentity((1,6))
_IsoGroups_ObjectIdentity=ObjectIdentity
isoGroups=_IsoGroups_ObjectIdentity((1,6,1))
_IsoCompliances_ObjectIdentity=ObjectIdentity
isoCompliances=_IsoCompliances_ObjectIdentity((1,6,2))
currentObjectGroup=ObjectGroup((1,6,1,1))
currentObjectGroup.setObjects(*((_B,_J),(_B,_e),(_B,_f),(_B,_g),(_B,_h),(_B,_i),(_B,_j),(_B,_R),(_B,_k),(_B,_l),(_B,_m),(_B,_n),(_B,_o),(_B,_p),(_B,_W),(_B,_q),(_B,_r),(_B,_s),(_B,_t),(_B,_u),(_B,_v),(_B,_w),(_B,_x),(_B,_y),(_B,_z),(_B,'version'),(_B,_A0),(_B,_A1),(_B,_A2),(_B,'deviceId'),(_B,_Q),(_B,_A3),(_B,_A4),(_B,_A5),(_B,_A6),(_B,_S),(_B,_A7),(_B,_A8),(_B,_A9),(_B,_AA),(_B,_V),(_B,_AB),(_B,_AC),(_B,_AD),(_B,_AE),(_B,_X),(_B,_AF),(_B,_AG),(_B,_AH),(_B,_AI),(_B,_T),(_B,_AJ),(_B,_AK),(_B,_AL),(_B,_AM),(_B,_AN),(_B,_AO),(_B,_AP),(_B,_AQ),(_B,_AR),(_B,_AS),(_B,_AT),(_B,_AU),(_B,_AV),(_B,_AW),(_B,_AX),(_B,_AY),(_B,_AZ),(_B,_Aa),(_B,_Ab),(_B,_Ac),(_B,_Ad),(_B,'status'),(_B,_Ae)))
if mibBuilder.loadTexts:currentObjectGroup.setStatus(_A)
basicCompliance=ModuleCompliance((1,6,2,1))
basicCompliance.setObjects((_B,_Af))
if mibBuilder.loadTexts:basicCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'NodeCodeString':NodeCodeString,'huaweistorage':huaweistorage,'hwStorage':hwStorage,'hwISM':hwISM,'common':common,'deviceId':deviceId,_A2:deviceType,'status':status,_A1:usedCapacity,_A0:totalCapacity,'version':version,'hardware':hardware,'hwStorageService':hwStorageService,'hwStoragePhysicalModule':hwStoragePhysicalModule,'hwStorageFCPortTable':hwStorageFCPortTable,'hwStorageFCPortEntry':hwStorageFCPortEntry,_J:hwStorageFCPortIfIndex,_e:hwStorageFCPortBoardIfIndex,_f:hwStorageFCPortID,_g:hwStorageFCPortStatus,_h:hwStorageFCPortConfigRate,_i:hwStorageFCPortMode,_j:hwStorageFCPortWWN,_AY:hwStorageFCPortLogicType,_AZ:hwStorageFCPortSpeedRate,'hwStorageSASPortTable':hwStorageSASPortTable,'hwStorageSASPortEntry':hwStorageSASPortEntry,_Q:hwStorageSASPortIfIndex,_A3:hwStorageSASPortBoardIfIndex,_A4:hwStorageSASPortID,_A5:hwStorageSASPortStatus,_A6:hwStorageSASPortConfigRate,_AX:hwStorageSASPortWWN,_Aa:hwStorageSASPortLogicType,_Ab:hwStorageSASPortSpeedRate,'hwStorageISCSIPortTable':hwStorageISCSIPortTable,'hwStorageISCSIPortEntry':hwStorageISCSIPortEntry,_R:hwStorageISCSIPortIfIndex,_k:hwStorageISCSIPortBoardIfIndex,_l:hwStorageISCSIPortID,_m:hwStorageISCSIPortStatus,_n:hwStorageISCSIPortIP,_o:hwStorageISCSIPortNetMask,_p:hwStorageISCSIPortBindMode,_Ac:hwStorageISCSIPortLogicType,'hwStorageFrontEndHostPortTable':hwStorageFrontEndHostPortTable,'hwStorageFrontEndHostPortEntry':hwStorageFrontEndHostPortEntry,_S:hwStorageFrontEndHostPortIfIndex,_A7:hwStorageFrontEndHostPortType,_A8:hwStorageFrontEndHostPortStatus,_A9:hwStorageFrontEndHostPortPhysAddress,_AA:hwStorageFrontEndHostPortDescription,'hwStorageControllerTable':hwStorageControllerTable,'hwStorageControllerEntry':hwStorageControllerEntry,_T:hwStorageControllerID,_AJ:hwStorageControllerName,_AK:hwStorageControllerLocation,_Ae:hwStorageControllerHealthStatus,_AL:hwStorageControllerRunningStatus,_AM:hwStorageControllerSoftVer,_AN:hwStorageControllerTemperature,_AO:hwStorageControllerIsMaster,_AP:hwStorageControllerELabel,_AQ:hwStorageControllerPCBVer,_AR:hwStorageControllerBMCVer,_AS:hwStorageControllerLogicVer,_AT:hwStorageControllerBIOSVer,_AU:hwStorageControllerMemorySize,_AV:hwStorageControllerCPUInfo,_AW:hwStorageControllerVoltage,'hwStorageLogicModule':hwStorageLogicModule,'hwStorageCacheTable':hwStorageCacheTable,'hwStorageCacheEntry':hwStorageCacheEntry,_V:hwStorageCacheID,_AB:hwStorageCacheTotalCapacity,_AC:hwStorageCacheHighWaterLevel,_AD:hwStorageCacheLowWaterLevel,_AE:hwStorageCacheRowStatus,'hwStorageLunTable':hwStorageLunTable,'hwStorageLunEntry':hwStorageLunEntry,_W:hwStorageLunID,_q:hwStorageLunName,_r:hwStorageLunWWN,_s:hwStorageLunPoolID,_t:hwStorageLunCapacity,_u:hwStorageLunOwningController,_v:hwStorageLunStripDepth,_w:hwStorageLunWriteStrategy,_Ad:hwStorageLunPrefetchStrategy,_x:hwStorageLunPrefetchValue,_y:hwStorageLunStatus,_z:hwStorageLunRowStatus,'hwStorageNodeTable':hwStorageNodeTable,'hwStorageNodeEntry':hwStorageNodeEntry,_X:hwStorageNodeIfIndex,_AF:hwStorageNodeIPAddress,_AG:hwStorageNodeStatus,_AH:hwStorageNodeIsMaster,_AI:hwStorageNodeRowStatus,'isoConformance':isoConformance,'isoGroups':isoGroups,_Af:currentObjectGroup,'isoCompliances':isoCompliances,'basicCompliance':basicCompliance})