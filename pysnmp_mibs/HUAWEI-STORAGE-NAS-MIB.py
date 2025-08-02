_AL='currentObjectGroup'
_AK='hwInfoLogicalPortFailOVGName'
_AJ='hwInfoLogicalPortFailOVEnable'
_AI='hwInfoLogicalPortFailOVGID'
_AH='hwInfoLogicalPortIsPrivate'
_AG='hwInfoLogicalPortAddrFamily'
_AF='hwInfoLogicalPortActState'
_AE='hwInfoLogicalPortWorkCtrlID'
_AD='hwInfoLogicalPortCurrPortID'
_AC='hwInfoLogicalPortCurrPortType'
_AB='hwInfoLogicalPortOwnerCtrlID'
_AA='hwInfoLogicalPortHomePortID'
_A9='hwInfoLogicalPortRole'
_A8='hwInfoLogicalPortIPv6Gateway'
_A7='hwInfoLogicalPortIPv6Mask'
_A6='hwInfoLogicalPortIPv6Addr'
_A5='hwInfoLogicalPortIPv4Gateway'
_A4='hwInfoLogicalPortIPv4Mask'
_A3='hwInfoLogicalPortIPv4Addr'
_A2='hwInfoLogicalPortRunStatus'
_A1='hwInfoLogicalPorttName'
_A0='hwInfoShareCIFSNotifyEnabled'
_z='hwInfoShareCIFSOplockEnabled'
_y='hwInfoShareCIFSLocalPath'
_x='hwInfoShareCIFSName'
_w='hwInfoShareNFSLocalPath'
_v='hwInfoShareCIFSDescription'
_u='hwInfoShareCIFSFileSystemID'
_t='hwInfoShareNFSDescription'
_s='hwInfoShareNFSFileSystemID'
_r='hwInfoFileSysCompressSavedRatio'
_q='hwInfoFileSysSCHitRage'
_p='hwInfoFileSysSCCachedSize'
_o='hwInfoFileSysAvAndAllcCapRatio'
_n='hwInfoFileSysAvailableCapacity'
_m='hwInfoFileSysIsShowSnapDir'
_l='hwInfoFileSysCompression'
_k='hwInfoFileSysEnableCompression'
_j='hwInfoFileSysIOPriotiry'
_i='hwInfoFileSysWorkingController'
_h='hwInfoFileSysOwningContrller'
_g='hwInfoFileSysSectorSize'
_f='hwInfoFileSysSnapshotUseCapacity'
_e='hwInfoFileSysSnapshotReservePer'
_d='hwInfoFileSysCapacity'
_c='hwInfoFileSysAllocType'
_b='hwInfoFileSysSubType'
_a='hwInfoFileSysDescription'
_Z='hwInfoFileSysRunningStatus'
_Y='hwInfoFileSysHeathStatus'
_X='hwInfoFileSysName'
_W='hwInfoLogicalPortFailBackMode'
_V='hwInfoLogicalPortHomePortType'
_U='hwInfoLogicalPortSupportProt'
_T='hwInfoSharePermsCIFSPermsType'
_S='hwInfoSharePermsCIFSDomainType'
_R='hwInfoSharePermsCIFSShareID'
_Q='hwInfoSharePermsCIFSAccessName'
_P='hwInfoSharePermsNFSRootSquashEna'
_O='hwInfoSharePermsNFSAllSquashEna'
_N='hwInfoSharePermsNFSSyncEnabled'
_M='hwInfoSharePermsNFSAccessType'
_L='hwInfoSharePermsNFSShareID'
_K='hwInfoSharePermsNFSAccessName'
_J='hwInfoShareCIFSContAvailableEna'
_I='hwInfoFileSysID'
_H='hwInfoLogicalPortID'
_G='hwInfoSharePermsCIFSID'
_F='hwInfoSharePermsNFSID'
_E='hwInfoShareCIFSID'
_D='hwInfoShareNFSShareID'
_C='read-only'
_B='HUAWEI-STORAGE-NAS-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
hwStorage=ModuleIdentity((1,3,6,1,4,1,34774,4))
if mibBuilder.loadTexts:hwStorage.setRevisions(('2014-11-06 15:32',))
class NodeCodeString(TextualConvention,OctetString):status=_A;displayHint='255a';subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(15,17))
_Huaweistorage_ObjectIdentity=ObjectIdentity
huaweistorage=_Huaweistorage_ObjectIdentity((1,3,6,1,4,1,34774))
_HwISM_ObjectIdentity=ObjectIdentity
hwISM=_HwISM_ObjectIdentity((1,3,6,1,4,1,34774,4,1))
_HwStorageDevice_ObjectIdentity=ObjectIdentity
hwStorageDevice=_HwStorageDevice_ObjectIdentity((1,3,6,1,4,1,34774,4,1,23))
_HwNasInfo_ObjectIdentity=ObjectIdentity
hwNasInfo=_HwNasInfo_ObjectIdentity((1,3,6,1,4,1,34774,4,1,23,7))
_HwInfoShareNFSTable_Object=MibTable
hwInfoShareNFSTable=_HwInfoShareNFSTable_Object((1,3,6,1,4,1,34774,4,1,23,7,1))
if mibBuilder.loadTexts:hwInfoShareNFSTable.setStatus(_A)
_HwInfoShareNFSEntry_Object=MibTableRow
hwInfoShareNFSEntry=_HwInfoShareNFSEntry_Object((1,3,6,1,4,1,34774,4,1,23,7,1,1))
hwInfoShareNFSEntry.setIndexNames((0,_B,_D))
if mibBuilder.loadTexts:hwInfoShareNFSEntry.setStatus(_A)
_HwInfoShareNFSShareID_Type=OctetString
_HwInfoShareNFSShareID_Object=MibTableColumn
hwInfoShareNFSShareID=_HwInfoShareNFSShareID_Object((1,3,6,1,4,1,34774,4,1,23,7,1,1,1),_HwInfoShareNFSShareID_Type())
hwInfoShareNFSShareID.setMaxAccess(_C)
if mibBuilder.loadTexts:hwInfoShareNFSShareID.setStatus(_A)
_HwInfoShareNFSFileSystemID_Type=OctetString
_HwInfoShareNFSFileSystemID_Object=MibTableColumn
hwInfoShareNFSFileSystemID=_HwInfoShareNFSFileSystemID_Object((1,3,6,1,4,1,34774,4,1,23,7,1,1,2),_HwInfoShareNFSFileSystemID_Type())
hwInfoShareNFSFileSystemID.setMaxAccess(_C)
if mibBuilder.loadTexts:hwInfoShareNFSFileSystemID.setStatus(_A)
_HwInfoShareNFSDescription_Type=OctetString
_HwInfoShareNFSDescription_Object=MibTableColumn
hwInfoShareNFSDescription=_HwInfoShareNFSDescription_Object((1,3,6,1,4,1,34774,4,1,23,7,1,1,3),_HwInfoShareNFSDescription_Type())
hwInfoShareNFSDescription.setMaxAccess(_C)
if mibBuilder.loadTexts:hwInfoShareNFSDescription.setStatus(_A)
_HwInfoShareNFSLocalPath_Type=OctetString
_HwInfoShareNFSLocalPath_Object=MibTableColumn
hwInfoShareNFSLocalPath=_HwInfoShareNFSLocalPath_Object((1,3,6,1,4,1,34774,4,1,23,7,1,1,4),_HwInfoShareNFSLocalPath_Type())
hwInfoShareNFSLocalPath.setMaxAccess(_C)
if mibBuilder.loadTexts:hwInfoShareNFSLocalPath.setStatus(_A)
_HwInfoShareCIFSTable_Object=MibTable
hwInfoShareCIFSTable=_HwInfoShareCIFSTable_Object((1,3,6,1,4,1,34774,4,1,23,7,2))
if mibBuilder.loadTexts:hwInfoShareCIFSTable.setStatus(_A)
_HwInfoShareCIFSEntry_Object=MibTableRow
hwInfoShareCIFSEntry=_HwInfoShareCIFSEntry_Object((1,3,6,1,4,1,34774,4,1,23,7,2,1))
hwInfoShareCIFSEntry.setIndexNames((0,_B,_E))
if mibBuilder.loadTexts:hwInfoShareCIFSEntry.setStatus(_A)
_HwInfoShareCIFSID_Type=OctetString
_HwInfoShareCIFSID_Object=MibTableColumn
hwInfoShareCIFSID=_HwInfoShareCIFSID_Object((1,3,6,1,4,1,34774,4,1,23,7,2,1,1),_HwInfoShareCIFSID_Type())
hwInfoShareCIFSID.setMaxAccess(_C)
if mibBuilder.loadTexts:hwInfoShareCIFSID.setStatus(_A)
_HwInfoShareCIFSName_Type=OctetString
_HwInfoShareCIFSName_Object=MibTableColumn
hwInfoShareCIFSName=_HwInfoShareCIFSName_Object((1,3,6,1,4,1,34774,4,1,23,7,2,1,2),_HwInfoShareCIFSName_Type())
hwInfoShareCIFSName.setMaxAccess(_C)
if mibBuilder.loadTexts:hwInfoShareCIFSName.setStatus(_A)
_HwInfoShareCIFSFileSystemID_Type=OctetString
_HwInfoShareCIFSFileSystemID_Object=MibTableColumn
hwInfoShareCIFSFileSystemID=_HwInfoShareCIFSFileSystemID_Object((1,3,6,1,4,1,34774,4,1,23,7,2,1,3),_HwInfoShareCIFSFileSystemID_Type())
hwInfoShareCIFSFileSystemID.setMaxAccess(_C)
if mibBuilder.loadTexts:hwInfoShareCIFSFileSystemID.setStatus(_A)
_HwInfoShareCIFSDescription_Type=OctetString
_HwInfoShareCIFSDescription_Object=MibTableColumn
hwInfoShareCIFSDescription=_HwInfoShareCIFSDescription_Object((1,3,6,1,4,1,34774,4,1,23,7,2,1,4),_HwInfoShareCIFSDescription_Type())
hwInfoShareCIFSDescription.setMaxAccess(_C)
if mibBuilder.loadTexts:hwInfoShareCIFSDescription.setStatus(_A)
_HwInfoShareCIFSLocalPath_Type=OctetString
_HwInfoShareCIFSLocalPath_Object=MibTableColumn
hwInfoShareCIFSLocalPath=_HwInfoShareCIFSLocalPath_Object((1,3,6,1,4,1,34774,4,1,23,7,2,1,5),_HwInfoShareCIFSLocalPath_Type())
hwInfoShareCIFSLocalPath.setMaxAccess(_C)
if mibBuilder.loadTexts:hwInfoShareCIFSLocalPath.setStatus(_A)
_HwInfoShareCIFSOplockEnabled_Type=Unsigned32
_HwInfoShareCIFSOplockEnabled_Object=MibTableColumn
hwInfoShareCIFSOplockEnabled=_HwInfoShareCIFSOplockEnabled_Object((1,3,6,1,4,1,34774,4,1,23,7,2,1,6),_HwInfoShareCIFSOplockEnabled_Type())
hwInfoShareCIFSOplockEnabled.setMaxAccess(_C)
if mibBuilder.loadTexts:hwInfoShareCIFSOplockEnabled.setStatus(_A)
_HwInfoShareCIFSNotifyEnabled_Type=Unsigned32
_HwInfoShareCIFSNotifyEnabled_Object=MibTableColumn
hwInfoShareCIFSNotifyEnabled=_HwInfoShareCIFSNotifyEnabled_Object((1,3,6,1,4,1,34774,4,1,23,7,2,1,7),_HwInfoShareCIFSNotifyEnabled_Type())
hwInfoShareCIFSNotifyEnabled.setMaxAccess(_C)
if mibBuilder.loadTexts:hwInfoShareCIFSNotifyEnabled.setStatus(_A)
_HwInfoShareCIFSContAvailableEna_Type=Unsigned32
_HwInfoShareCIFSContAvailableEna_Object=MibTableColumn
hwInfoShareCIFSContAvailableEna=_HwInfoShareCIFSContAvailableEna_Object((1,3,6,1,4,1,34774,4,1,23,7,2,1,8),_HwInfoShareCIFSContAvailableEna_Type())
hwInfoShareCIFSContAvailableEna.setMaxAccess(_C)
if mibBuilder.loadTexts:hwInfoShareCIFSContAvailableEna.setStatus(_A)
_HwInfoSharePermsNFSTable_Object=MibTable
hwInfoSharePermsNFSTable=_HwInfoSharePermsNFSTable_Object((1,3,6,1,4,1,34774,4,1,23,7,3))
if mibBuilder.loadTexts:hwInfoSharePermsNFSTable.setStatus(_A)
_HwInfoSharePermsNFSEntry_Object=MibTableRow
hwInfoSharePermsNFSEntry=_HwInfoSharePermsNFSEntry_Object((1,3,6,1,4,1,34774,4,1,23,7,3,1))
hwInfoSharePermsNFSEntry.setIndexNames((0,_B,_F))
if mibBuilder.loadTexts:hwInfoSharePermsNFSEntry.setStatus(_A)
_HwInfoSharePermsNFSID_Type=OctetString
_HwInfoSharePermsNFSID_Object=MibTableColumn
hwInfoSharePermsNFSID=_HwInfoSharePermsNFSID_Object((1,3,6,1,4,1,34774,4,1,23,7,3,1,1),_HwInfoSharePermsNFSID_Type())
hwInfoSharePermsNFSID.setMaxAccess(_C)
if mibBuilder.loadTexts:hwInfoSharePermsNFSID.setStatus(_A)
_HwInfoSharePermsNFSAccessName_Type=OctetString
_HwInfoSharePermsNFSAccessName_Object=MibTableColumn
hwInfoSharePermsNFSAccessName=_HwInfoSharePermsNFSAccessName_Object((1,3,6,1,4,1,34774,4,1,23,7,3,1,2),_HwInfoSharePermsNFSAccessName_Type())
hwInfoSharePermsNFSAccessName.setMaxAccess(_C)
if mibBuilder.loadTexts:hwInfoSharePermsNFSAccessName.setStatus(_A)
_HwInfoSharePermsNFSShareID_Type=OctetString
_HwInfoSharePermsNFSShareID_Object=MibTableColumn
hwInfoSharePermsNFSShareID=_HwInfoSharePermsNFSShareID_Object((1,3,6,1,4,1,34774,4,1,23,7,3,1,3),_HwInfoSharePermsNFSShareID_Type())
hwInfoSharePermsNFSShareID.setMaxAccess(_C)
if mibBuilder.loadTexts:hwInfoSharePermsNFSShareID.setStatus(_A)
_HwInfoSharePermsNFSAccessType_Type=Unsigned32
_HwInfoSharePermsNFSAccessType_Object=MibTableColumn
hwInfoSharePermsNFSAccessType=_HwInfoSharePermsNFSAccessType_Object((1,3,6,1,4,1,34774,4,1,23,7,3,1,4),_HwInfoSharePermsNFSAccessType_Type())
hwInfoSharePermsNFSAccessType.setMaxAccess(_C)
if mibBuilder.loadTexts:hwInfoSharePermsNFSAccessType.setStatus(_A)
_HwInfoSharePermsNFSSyncEnabled_Type=Unsigned32
_HwInfoSharePermsNFSSyncEnabled_Object=MibTableColumn
hwInfoSharePermsNFSSyncEnabled=_HwInfoSharePermsNFSSyncEnabled_Object((1,3,6,1,4,1,34774,4,1,23,7,3,1,5),_HwInfoSharePermsNFSSyncEnabled_Type())
hwInfoSharePermsNFSSyncEnabled.setMaxAccess(_C)
if mibBuilder.loadTexts:hwInfoSharePermsNFSSyncEnabled.setStatus(_A)
_HwInfoSharePermsNFSAllSquashEna_Type=Unsigned32
_HwInfoSharePermsNFSAllSquashEna_Object=MibTableColumn
hwInfoSharePermsNFSAllSquashEna=_HwInfoSharePermsNFSAllSquashEna_Object((1,3,6,1,4,1,34774,4,1,23,7,3,1,6),_HwInfoSharePermsNFSAllSquashEna_Type())
hwInfoSharePermsNFSAllSquashEna.setMaxAccess(_C)
if mibBuilder.loadTexts:hwInfoSharePermsNFSAllSquashEna.setStatus(_A)
_HwInfoSharePermsNFSRootSquashEna_Type=Unsigned32
_HwInfoSharePermsNFSRootSquashEna_Object=MibTableColumn
hwInfoSharePermsNFSRootSquashEna=_HwInfoSharePermsNFSRootSquashEna_Object((1,3,6,1,4,1,34774,4,1,23,7,3,1,7),_HwInfoSharePermsNFSRootSquashEna_Type())
hwInfoSharePermsNFSRootSquashEna.setMaxAccess(_C)
if mibBuilder.loadTexts:hwInfoSharePermsNFSRootSquashEna.setStatus(_A)
_HwInfoSharePermsCIFSTable_Object=MibTable
hwInfoSharePermsCIFSTable=_HwInfoSharePermsCIFSTable_Object((1,3,6,1,4,1,34774,4,1,23,7,4))
if mibBuilder.loadTexts:hwInfoSharePermsCIFSTable.setStatus(_A)
_HwInfoSharePermsCIFSEntry_Object=MibTableRow
hwInfoSharePermsCIFSEntry=_HwInfoSharePermsCIFSEntry_Object((1,3,6,1,4,1,34774,4,1,23,7,4,1))
hwInfoSharePermsCIFSEntry.setIndexNames((0,_B,_G))
if mibBuilder.loadTexts:hwInfoSharePermsCIFSEntry.setStatus(_A)
_HwInfoSharePermsCIFSID_Type=OctetString
_HwInfoSharePermsCIFSID_Object=MibTableColumn
hwInfoSharePermsCIFSID=_HwInfoSharePermsCIFSID_Object((1,3,6,1,4,1,34774,4,1,23,7,4,1,1),_HwInfoSharePermsCIFSID_Type())
hwInfoSharePermsCIFSID.setMaxAccess(_C)
if mibBuilder.loadTexts:hwInfoSharePermsCIFSID.setStatus(_A)
_HwInfoSharePermsCIFSAccessName_Type=OctetString
_HwInfoSharePermsCIFSAccessName_Object=MibTableColumn
hwInfoSharePermsCIFSAccessName=_HwInfoSharePermsCIFSAccessName_Object((1,3,6,1,4,1,34774,4,1,23,7,4,1,2),_HwInfoSharePermsCIFSAccessName_Type())
hwInfoSharePermsCIFSAccessName.setMaxAccess(_C)
if mibBuilder.loadTexts:hwInfoSharePermsCIFSAccessName.setStatus(_A)
_HwInfoSharePermsCIFSShareID_Type=OctetString
_HwInfoSharePermsCIFSShareID_Object=MibTableColumn
hwInfoSharePermsCIFSShareID=_HwInfoSharePermsCIFSShareID_Object((1,3,6,1,4,1,34774,4,1,23,7,4,1,3),_HwInfoSharePermsCIFSShareID_Type())
hwInfoSharePermsCIFSShareID.setMaxAccess(_C)
if mibBuilder.loadTexts:hwInfoSharePermsCIFSShareID.setStatus(_A)
_HwInfoSharePermsCIFSDomainType_Type=Unsigned32
_HwInfoSharePermsCIFSDomainType_Object=MibTableColumn
hwInfoSharePermsCIFSDomainType=_HwInfoSharePermsCIFSDomainType_Object((1,3,6,1,4,1,34774,4,1,23,7,4,1,4),_HwInfoSharePermsCIFSDomainType_Type())
hwInfoSharePermsCIFSDomainType.setMaxAccess(_C)
if mibBuilder.loadTexts:hwInfoSharePermsCIFSDomainType.setStatus(_A)
_HwInfoSharePermsCIFSPermsType_Type=Unsigned32
_HwInfoSharePermsCIFSPermsType_Object=MibTableColumn
hwInfoSharePermsCIFSPermsType=_HwInfoSharePermsCIFSPermsType_Object((1,3,6,1,4,1,34774,4,1,23,7,4,1,5),_HwInfoSharePermsCIFSPermsType_Type())
hwInfoSharePermsCIFSPermsType.setMaxAccess(_C)
if mibBuilder.loadTexts:hwInfoSharePermsCIFSPermsType.setStatus(_A)
_HwInfoLogicalPortTable_Object=MibTable
hwInfoLogicalPortTable=_HwInfoLogicalPortTable_Object((1,3,6,1,4,1,34774,4,1,23,7,5))
if mibBuilder.loadTexts:hwInfoLogicalPortTable.setStatus(_A)
_HwInfoLogicalPortEntry_Object=MibTableRow
hwInfoLogicalPortEntry=_HwInfoLogicalPortEntry_Object((1,3,6,1,4,1,34774,4,1,23,7,5,1))
hwInfoLogicalPortEntry.setIndexNames((0,_B,_H))
if mibBuilder.loadTexts:hwInfoLogicalPortEntry.setStatus(_A)
_HwInfoLogicalPortID_Type=OctetString
_HwInfoLogicalPortID_Object=MibTableColumn
hwInfoLogicalPortID=_HwInfoLogicalPortID_Object((1,3,6,1,4,1,34774,4,1,23,7,5,1,1),_HwInfoLogicalPortID_Type())
hwInfoLogicalPortID.setMaxAccess(_C)
if mibBuilder.loadTexts:hwInfoLogicalPortID.setStatus(_A)
_HwInfoLogicalPorttName_Type=OctetString
_HwInfoLogicalPorttName_Object=MibTableColumn
hwInfoLogicalPorttName=_HwInfoLogicalPorttName_Object((1,3,6,1,4,1,34774,4,1,23,7,5,1,2),_HwInfoLogicalPorttName_Type())
hwInfoLogicalPorttName.setMaxAccess(_C)
if mibBuilder.loadTexts:hwInfoLogicalPorttName.setStatus(_A)
_HwInfoLogicalPortRunStatus_Type=Unsigned32
_HwInfoLogicalPortRunStatus_Object=MibTableColumn
hwInfoLogicalPortRunStatus=_HwInfoLogicalPortRunStatus_Object((1,3,6,1,4,1,34774,4,1,23,7,5,1,3),_HwInfoLogicalPortRunStatus_Type())
hwInfoLogicalPortRunStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:hwInfoLogicalPortRunStatus.setStatus(_A)
_HwInfoLogicalPortIPv4Addr_Type=OctetString
_HwInfoLogicalPortIPv4Addr_Object=MibTableColumn
hwInfoLogicalPortIPv4Addr=_HwInfoLogicalPortIPv4Addr_Object((1,3,6,1,4,1,34774,4,1,23,7,5,1,4),_HwInfoLogicalPortIPv4Addr_Type())
hwInfoLogicalPortIPv4Addr.setMaxAccess(_C)
if mibBuilder.loadTexts:hwInfoLogicalPortIPv4Addr.setStatus(_A)
_HwInfoLogicalPortIPv4Mask_Type=OctetString
_HwInfoLogicalPortIPv4Mask_Object=MibTableColumn
hwInfoLogicalPortIPv4Mask=_HwInfoLogicalPortIPv4Mask_Object((1,3,6,1,4,1,34774,4,1,23,7,5,1,5),_HwInfoLogicalPortIPv4Mask_Type())
hwInfoLogicalPortIPv4Mask.setMaxAccess(_C)
if mibBuilder.loadTexts:hwInfoLogicalPortIPv4Mask.setStatus(_A)
_HwInfoLogicalPortIPv4Gateway_Type=OctetString
_HwInfoLogicalPortIPv4Gateway_Object=MibTableColumn
hwInfoLogicalPortIPv4Gateway=_HwInfoLogicalPortIPv4Gateway_Object((1,3,6,1,4,1,34774,4,1,23,7,5,1,6),_HwInfoLogicalPortIPv4Gateway_Type())
hwInfoLogicalPortIPv4Gateway.setMaxAccess(_C)
if mibBuilder.loadTexts:hwInfoLogicalPortIPv4Gateway.setStatus(_A)
_HwInfoLogicalPortIPv6Addr_Type=OctetString
_HwInfoLogicalPortIPv6Addr_Object=MibTableColumn
hwInfoLogicalPortIPv6Addr=_HwInfoLogicalPortIPv6Addr_Object((1,3,6,1,4,1,34774,4,1,23,7,5,1,7),_HwInfoLogicalPortIPv6Addr_Type())
hwInfoLogicalPortIPv6Addr.setMaxAccess(_C)
if mibBuilder.loadTexts:hwInfoLogicalPortIPv6Addr.setStatus(_A)
_HwInfoLogicalPortIPv6Mask_Type=OctetString
_HwInfoLogicalPortIPv6Mask_Object=MibTableColumn
hwInfoLogicalPortIPv6Mask=_HwInfoLogicalPortIPv6Mask_Object((1,3,6,1,4,1,34774,4,1,23,7,5,1,8),_HwInfoLogicalPortIPv6Mask_Type())
hwInfoLogicalPortIPv6Mask.setMaxAccess(_C)
if mibBuilder.loadTexts:hwInfoLogicalPortIPv6Mask.setStatus(_A)
_HwInfoLogicalPortIPv6Gateway_Type=OctetString
_HwInfoLogicalPortIPv6Gateway_Object=MibTableColumn
hwInfoLogicalPortIPv6Gateway=_HwInfoLogicalPortIPv6Gateway_Object((1,3,6,1,4,1,34774,4,1,23,7,5,1,9),_HwInfoLogicalPortIPv6Gateway_Type())
hwInfoLogicalPortIPv6Gateway.setMaxAccess(_C)
if mibBuilder.loadTexts:hwInfoLogicalPortIPv6Gateway.setStatus(_A)
_HwInfoLogicalPortRole_Type=Unsigned32
_HwInfoLogicalPortRole_Object=MibTableColumn
hwInfoLogicalPortRole=_HwInfoLogicalPortRole_Object((1,3,6,1,4,1,34774,4,1,23,7,5,1,10),_HwInfoLogicalPortRole_Type())
hwInfoLogicalPortRole.setMaxAccess(_C)
if mibBuilder.loadTexts:hwInfoLogicalPortRole.setStatus(_A)
_HwInfoLogicalPortSupportProt_Type=Unsigned32
_HwInfoLogicalPortSupportProt_Object=MibTableColumn
hwInfoLogicalPortSupportProt=_HwInfoLogicalPortSupportProt_Object((1,3,6,1,4,1,34774,4,1,23,7,5,1,11),_HwInfoLogicalPortSupportProt_Type())
hwInfoLogicalPortSupportProt.setMaxAccess(_C)
if mibBuilder.loadTexts:hwInfoLogicalPortSupportProt.setStatus(_A)
_HwInfoLogicalPortHomePortType_Type=Unsigned32
_HwInfoLogicalPortHomePortType_Object=MibTableColumn
hwInfoLogicalPortHomePortType=_HwInfoLogicalPortHomePortType_Object((1,3,6,1,4,1,34774,4,1,23,7,5,1,12),_HwInfoLogicalPortHomePortType_Type())
hwInfoLogicalPortHomePortType.setMaxAccess(_C)
if mibBuilder.loadTexts:hwInfoLogicalPortHomePortType.setStatus(_A)
_HwInfoLogicalPortHomePortID_Type=OctetString
_HwInfoLogicalPortHomePortID_Object=MibTableColumn
hwInfoLogicalPortHomePortID=_HwInfoLogicalPortHomePortID_Object((1,3,6,1,4,1,34774,4,1,23,7,5,1,13),_HwInfoLogicalPortHomePortID_Type())
hwInfoLogicalPortHomePortID.setMaxAccess(_C)
if mibBuilder.loadTexts:hwInfoLogicalPortHomePortID.setStatus(_A)
_HwInfoLogicalPortOwnerCtrlID_Type=OctetString
_HwInfoLogicalPortOwnerCtrlID_Object=MibTableColumn
hwInfoLogicalPortOwnerCtrlID=_HwInfoLogicalPortOwnerCtrlID_Object((1,3,6,1,4,1,34774,4,1,23,7,5,1,14),_HwInfoLogicalPortOwnerCtrlID_Type())
hwInfoLogicalPortOwnerCtrlID.setMaxAccess(_C)
if mibBuilder.loadTexts:hwInfoLogicalPortOwnerCtrlID.setStatus(_A)
_HwInfoLogicalPortCurrPortType_Type=Unsigned32
_HwInfoLogicalPortCurrPortType_Object=MibTableColumn
hwInfoLogicalPortCurrPortType=_HwInfoLogicalPortCurrPortType_Object((1,3,6,1,4,1,34774,4,1,23,7,5,1,15),_HwInfoLogicalPortCurrPortType_Type())
hwInfoLogicalPortCurrPortType.setMaxAccess(_C)
if mibBuilder.loadTexts:hwInfoLogicalPortCurrPortType.setStatus(_A)
_HwInfoLogicalPortCurrPortID_Type=OctetString
_HwInfoLogicalPortCurrPortID_Object=MibTableColumn
hwInfoLogicalPortCurrPortID=_HwInfoLogicalPortCurrPortID_Object((1,3,6,1,4,1,34774,4,1,23,7,5,1,16),_HwInfoLogicalPortCurrPortID_Type())
hwInfoLogicalPortCurrPortID.setMaxAccess(_C)
if mibBuilder.loadTexts:hwInfoLogicalPortCurrPortID.setStatus(_A)
_HwInfoLogicalPortWorkCtrlID_Type=OctetString
_HwInfoLogicalPortWorkCtrlID_Object=MibTableColumn
hwInfoLogicalPortWorkCtrlID=_HwInfoLogicalPortWorkCtrlID_Object((1,3,6,1,4,1,34774,4,1,23,7,5,1,17),_HwInfoLogicalPortWorkCtrlID_Type())
hwInfoLogicalPortWorkCtrlID.setMaxAccess(_C)
if mibBuilder.loadTexts:hwInfoLogicalPortWorkCtrlID.setStatus(_A)
_HwInfoLogicalPortActState_Type=Unsigned32
_HwInfoLogicalPortActState_Object=MibTableColumn
hwInfoLogicalPortActState=_HwInfoLogicalPortActState_Object((1,3,6,1,4,1,34774,4,1,23,7,5,1,18),_HwInfoLogicalPortActState_Type())
hwInfoLogicalPortActState.setMaxAccess(_C)
if mibBuilder.loadTexts:hwInfoLogicalPortActState.setStatus(_A)
_HwInfoLogicalPortAddrFamily_Type=Unsigned32
_HwInfoLogicalPortAddrFamily_Object=MibTableColumn
hwInfoLogicalPortAddrFamily=_HwInfoLogicalPortAddrFamily_Object((1,3,6,1,4,1,34774,4,1,23,7,5,1,19),_HwInfoLogicalPortAddrFamily_Type())
hwInfoLogicalPortAddrFamily.setMaxAccess(_C)
if mibBuilder.loadTexts:hwInfoLogicalPortAddrFamily.setStatus(_A)
_HwInfoLogicalPortIsPrivate_Type=Unsigned32
_HwInfoLogicalPortIsPrivate_Object=MibTableColumn
hwInfoLogicalPortIsPrivate=_HwInfoLogicalPortIsPrivate_Object((1,3,6,1,4,1,34774,4,1,23,7,5,1,20),_HwInfoLogicalPortIsPrivate_Type())
hwInfoLogicalPortIsPrivate.setMaxAccess(_C)
if mibBuilder.loadTexts:hwInfoLogicalPortIsPrivate.setStatus(_A)
_HwInfoLogicalPortFailOVGID_Type=OctetString
_HwInfoLogicalPortFailOVGID_Object=MibTableColumn
hwInfoLogicalPortFailOVGID=_HwInfoLogicalPortFailOVGID_Object((1,3,6,1,4,1,34774,4,1,23,7,5,1,21),_HwInfoLogicalPortFailOVGID_Type())
hwInfoLogicalPortFailOVGID.setMaxAccess(_C)
if mibBuilder.loadTexts:hwInfoLogicalPortFailOVGID.setStatus(_A)
_HwInfoLogicalPortFailOVEnable_Type=Unsigned32
_HwInfoLogicalPortFailOVEnable_Object=MibTableColumn
hwInfoLogicalPortFailOVEnable=_HwInfoLogicalPortFailOVEnable_Object((1,3,6,1,4,1,34774,4,1,23,7,5,1,22),_HwInfoLogicalPortFailOVEnable_Type())
hwInfoLogicalPortFailOVEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:hwInfoLogicalPortFailOVEnable.setStatus(_A)
_HwInfoLogicalPortFailBackMode_Type=Unsigned32
_HwInfoLogicalPortFailBackMode_Object=MibTableColumn
hwInfoLogicalPortFailBackMode=_HwInfoLogicalPortFailBackMode_Object((1,3,6,1,4,1,34774,4,1,23,7,5,1,23),_HwInfoLogicalPortFailBackMode_Type())
hwInfoLogicalPortFailBackMode.setMaxAccess(_C)
if mibBuilder.loadTexts:hwInfoLogicalPortFailBackMode.setStatus(_A)
_HwInfoLogicalPortFailOVGName_Type=OctetString
_HwInfoLogicalPortFailOVGName_Object=MibTableColumn
hwInfoLogicalPortFailOVGName=_HwInfoLogicalPortFailOVGName_Object((1,3,6,1,4,1,34774,4,1,23,7,5,1,24),_HwInfoLogicalPortFailOVGName_Type())
hwInfoLogicalPortFailOVGName.setMaxAccess(_C)
if mibBuilder.loadTexts:hwInfoLogicalPortFailOVGName.setStatus(_A)
_HwInfoFileSysTable_Object=MibTable
hwInfoFileSysTable=_HwInfoFileSysTable_Object((1,3,6,1,4,1,34774,4,1,23,7,6))
if mibBuilder.loadTexts:hwInfoFileSysTable.setStatus(_A)
_HwInfoFileSysEntry_Object=MibTableRow
hwInfoFileSysEntry=_HwInfoFileSysEntry_Object((1,3,6,1,4,1,34774,4,1,23,7,6,1))
hwInfoFileSysEntry.setIndexNames((0,_B,_I))
if mibBuilder.loadTexts:hwInfoFileSysEntry.setStatus(_A)
_HwInfoFileSysID_Type=OctetString
_HwInfoFileSysID_Object=MibTableColumn
hwInfoFileSysID=_HwInfoFileSysID_Object((1,3,6,1,4,1,34774,4,1,23,7,6,1,1),_HwInfoFileSysID_Type())
hwInfoFileSysID.setMaxAccess(_C)
if mibBuilder.loadTexts:hwInfoFileSysID.setStatus(_A)
_HwInfoFileSysName_Type=OctetString
_HwInfoFileSysName_Object=MibTableColumn
hwInfoFileSysName=_HwInfoFileSysName_Object((1,3,6,1,4,1,34774,4,1,23,7,6,1,2),_HwInfoFileSysName_Type())
hwInfoFileSysName.setMaxAccess(_C)
if mibBuilder.loadTexts:hwInfoFileSysName.setStatus(_A)
_HwInfoFileSysHeathStatus_Type=Unsigned32
_HwInfoFileSysHeathStatus_Object=MibTableColumn
hwInfoFileSysHeathStatus=_HwInfoFileSysHeathStatus_Object((1,3,6,1,4,1,34774,4,1,23,7,6,1,3),_HwInfoFileSysHeathStatus_Type())
hwInfoFileSysHeathStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:hwInfoFileSysHeathStatus.setStatus(_A)
_HwInfoFileSysRunningStatus_Type=Unsigned32
_HwInfoFileSysRunningStatus_Object=MibTableColumn
hwInfoFileSysRunningStatus=_HwInfoFileSysRunningStatus_Object((1,3,6,1,4,1,34774,4,1,23,7,6,1,4),_HwInfoFileSysRunningStatus_Type())
hwInfoFileSysRunningStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:hwInfoFileSysRunningStatus.setStatus(_A)
_HwInfoFileSysDescription_Type=OctetString
_HwInfoFileSysDescription_Object=MibTableColumn
hwInfoFileSysDescription=_HwInfoFileSysDescription_Object((1,3,6,1,4,1,34774,4,1,23,7,6,1,5),_HwInfoFileSysDescription_Type())
hwInfoFileSysDescription.setMaxAccess(_C)
if mibBuilder.loadTexts:hwInfoFileSysDescription.setStatus(_A)
_HwInfoFileSysSubType_Type=Unsigned32
_HwInfoFileSysSubType_Object=MibTableColumn
hwInfoFileSysSubType=_HwInfoFileSysSubType_Object((1,3,6,1,4,1,34774,4,1,23,7,6,1,6),_HwInfoFileSysSubType_Type())
hwInfoFileSysSubType.setMaxAccess(_C)
if mibBuilder.loadTexts:hwInfoFileSysSubType.setStatus(_A)
_HwInfoFileSysAllocType_Type=Unsigned32
_HwInfoFileSysAllocType_Object=MibTableColumn
hwInfoFileSysAllocType=_HwInfoFileSysAllocType_Object((1,3,6,1,4,1,34774,4,1,23,7,6,1,7),_HwInfoFileSysAllocType_Type())
hwInfoFileSysAllocType.setMaxAccess(_C)
if mibBuilder.loadTexts:hwInfoFileSysAllocType.setStatus(_A)
_HwInfoFileSysCapacity_Type=Counter64
_HwInfoFileSysCapacity_Object=MibTableColumn
hwInfoFileSysCapacity=_HwInfoFileSysCapacity_Object((1,3,6,1,4,1,34774,4,1,23,7,6,1,8),_HwInfoFileSysCapacity_Type())
hwInfoFileSysCapacity.setMaxAccess(_C)
if mibBuilder.loadTexts:hwInfoFileSysCapacity.setStatus(_A)
_HwInfoFileSysSnapshotReservePer_Type=Unsigned32
_HwInfoFileSysSnapshotReservePer_Object=MibTableColumn
hwInfoFileSysSnapshotReservePer=_HwInfoFileSysSnapshotReservePer_Object((1,3,6,1,4,1,34774,4,1,23,7,6,1,9),_HwInfoFileSysSnapshotReservePer_Type())
hwInfoFileSysSnapshotReservePer.setMaxAccess(_C)
if mibBuilder.loadTexts:hwInfoFileSysSnapshotReservePer.setStatus(_A)
_HwInfoFileSysSnapshotUseCapacity_Type=Counter64
_HwInfoFileSysSnapshotUseCapacity_Object=MibTableColumn
hwInfoFileSysSnapshotUseCapacity=_HwInfoFileSysSnapshotUseCapacity_Object((1,3,6,1,4,1,34774,4,1,23,7,6,1,10),_HwInfoFileSysSnapshotUseCapacity_Type())
hwInfoFileSysSnapshotUseCapacity.setMaxAccess(_C)
if mibBuilder.loadTexts:hwInfoFileSysSnapshotUseCapacity.setStatus(_A)
_HwInfoFileSysSectorSize_Type=Unsigned32
_HwInfoFileSysSectorSize_Object=MibTableColumn
hwInfoFileSysSectorSize=_HwInfoFileSysSectorSize_Object((1,3,6,1,4,1,34774,4,1,23,7,6,1,11),_HwInfoFileSysSectorSize_Type())
hwInfoFileSysSectorSize.setMaxAccess(_C)
if mibBuilder.loadTexts:hwInfoFileSysSectorSize.setStatus(_A)
_HwInfoFileSysOwningContrller_Type=OctetString
_HwInfoFileSysOwningContrller_Object=MibTableColumn
hwInfoFileSysOwningContrller=_HwInfoFileSysOwningContrller_Object((1,3,6,1,4,1,34774,4,1,23,7,6,1,12),_HwInfoFileSysOwningContrller_Type())
hwInfoFileSysOwningContrller.setMaxAccess(_C)
if mibBuilder.loadTexts:hwInfoFileSysOwningContrller.setStatus(_A)
_HwInfoFileSysWorkingController_Type=OctetString
_HwInfoFileSysWorkingController_Object=MibTableColumn
hwInfoFileSysWorkingController=_HwInfoFileSysWorkingController_Object((1,3,6,1,4,1,34774,4,1,23,7,6,1,13),_HwInfoFileSysWorkingController_Type())
hwInfoFileSysWorkingController.setMaxAccess(_C)
if mibBuilder.loadTexts:hwInfoFileSysWorkingController.setStatus(_A)
_HwInfoFileSysIOPriotiry_Type=Unsigned32
_HwInfoFileSysIOPriotiry_Object=MibTableColumn
hwInfoFileSysIOPriotiry=_HwInfoFileSysIOPriotiry_Object((1,3,6,1,4,1,34774,4,1,23,7,6,1,14),_HwInfoFileSysIOPriotiry_Type())
hwInfoFileSysIOPriotiry.setMaxAccess(_C)
if mibBuilder.loadTexts:hwInfoFileSysIOPriotiry.setStatus(_A)
_HwInfoFileSysEnableCompression_Type=Unsigned32
_HwInfoFileSysEnableCompression_Object=MibTableColumn
hwInfoFileSysEnableCompression=_HwInfoFileSysEnableCompression_Object((1,3,6,1,4,1,34774,4,1,23,7,6,1,15),_HwInfoFileSysEnableCompression_Type())
hwInfoFileSysEnableCompression.setMaxAccess(_C)
if mibBuilder.loadTexts:hwInfoFileSysEnableCompression.setStatus(_A)
_HwInfoFileSysCompression_Type=Unsigned32
_HwInfoFileSysCompression_Object=MibTableColumn
hwInfoFileSysCompression=_HwInfoFileSysCompression_Object((1,3,6,1,4,1,34774,4,1,23,7,6,1,16),_HwInfoFileSysCompression_Type())
hwInfoFileSysCompression.setMaxAccess(_C)
if mibBuilder.loadTexts:hwInfoFileSysCompression.setStatus(_A)
_HwInfoFileSysIsShowSnapDir_Type=Unsigned32
_HwInfoFileSysIsShowSnapDir_Object=MibTableColumn
hwInfoFileSysIsShowSnapDir=_HwInfoFileSysIsShowSnapDir_Object((1,3,6,1,4,1,34774,4,1,23,7,6,1,17),_HwInfoFileSysIsShowSnapDir_Type())
hwInfoFileSysIsShowSnapDir.setMaxAccess(_C)
if mibBuilder.loadTexts:hwInfoFileSysIsShowSnapDir.setStatus(_A)
_HwInfoFileSysAvailableCapacity_Type=Counter64
_HwInfoFileSysAvailableCapacity_Object=MibTableColumn
hwInfoFileSysAvailableCapacity=_HwInfoFileSysAvailableCapacity_Object((1,3,6,1,4,1,34774,4,1,23,7,6,1,18),_HwInfoFileSysAvailableCapacity_Type())
hwInfoFileSysAvailableCapacity.setMaxAccess(_C)
if mibBuilder.loadTexts:hwInfoFileSysAvailableCapacity.setStatus(_A)
_HwInfoFileSysAvAndAllcCapRatio_Type=Unsigned32
_HwInfoFileSysAvAndAllcCapRatio_Object=MibTableColumn
hwInfoFileSysAvAndAllcCapRatio=_HwInfoFileSysAvAndAllcCapRatio_Object((1,3,6,1,4,1,34774,4,1,23,7,6,1,19),_HwInfoFileSysAvAndAllcCapRatio_Type())
hwInfoFileSysAvAndAllcCapRatio.setMaxAccess(_C)
if mibBuilder.loadTexts:hwInfoFileSysAvAndAllcCapRatio.setStatus(_A)
_HwInfoFileSysSCCachedSize_Type=Counter64
_HwInfoFileSysSCCachedSize_Object=MibTableColumn
hwInfoFileSysSCCachedSize=_HwInfoFileSysSCCachedSize_Object((1,3,6,1,4,1,34774,4,1,23,7,6,1,20),_HwInfoFileSysSCCachedSize_Type())
hwInfoFileSysSCCachedSize.setMaxAccess(_C)
if mibBuilder.loadTexts:hwInfoFileSysSCCachedSize.setStatus(_A)
_HwInfoFileSysSCHitRage_Type=Unsigned32
_HwInfoFileSysSCHitRage_Object=MibTableColumn
hwInfoFileSysSCHitRage=_HwInfoFileSysSCHitRage_Object((1,3,6,1,4,1,34774,4,1,23,7,6,1,21),_HwInfoFileSysSCHitRage_Type())
hwInfoFileSysSCHitRage.setMaxAccess(_C)
if mibBuilder.loadTexts:hwInfoFileSysSCHitRage.setStatus(_A)
_HwInfoFileSysCompressSavedRatio_Type=Unsigned32
_HwInfoFileSysCompressSavedRatio_Object=MibTableColumn
hwInfoFileSysCompressSavedRatio=_HwInfoFileSysCompressSavedRatio_Object((1,3,6,1,4,1,34774,4,1,23,7,6,1,22),_HwInfoFileSysCompressSavedRatio_Type())
hwInfoFileSysCompressSavedRatio.setMaxAccess(_C)
if mibBuilder.loadTexts:hwInfoFileSysCompressSavedRatio.setStatus(_A)
_IsoConformance_ObjectIdentity=ObjectIdentity
isoConformance=_IsoConformance_ObjectIdentity((1,6))
_IsoGroups_ObjectIdentity=ObjectIdentity
isoGroups=_IsoGroups_ObjectIdentity((1,6,1))
_IsoCompliances_ObjectIdentity=ObjectIdentity
isoCompliances=_IsoCompliances_ObjectIdentity((1,6,2))
currentObjectGroup=ObjectGroup((1,6,1,1))
currentObjectGroup.setObjects(*((_B,_J),(_B,_F),(_B,_K),(_B,_L),(_B,_M),(_B,_N),(_B,_O),(_B,_P),(_B,_G),(_B,_Q),(_B,_R),(_B,_S),(_B,_T),(_B,_U),(_B,_V),(_B,_W),(_B,_I),(_B,_X),(_B,_Y),(_B,_Z),(_B,_a),(_B,_b),(_B,_c),(_B,_d),(_B,_e),(_B,_f),(_B,_g),(_B,_h),(_B,_i),(_B,_j),(_B,_k),(_B,_l),(_B,_m),(_B,_n),(_B,_o),(_B,_p),(_B,_q),(_B,_r),(_B,_D),(_B,_s),(_B,_t),(_B,_E),(_B,_u),(_B,_v),(_B,_H),(_B,_w),(_B,_x),(_B,_y),(_B,_z),(_B,_A0),(_B,_A1),(_B,_A2),(_B,_A3),(_B,_A4),(_B,_A5),(_B,_A6),(_B,_A7),(_B,_A8),(_B,_A9),(_B,_AA),(_B,_AB),(_B,_AC),(_B,_AD),(_B,_AE),(_B,_AF),(_B,_AG),(_B,_AH),(_B,_AI),(_B,_AJ),(_B,_AK)))
if mibBuilder.loadTexts:currentObjectGroup.setStatus(_A)
basicCompliance=ModuleCompliance((1,6,2,1))
basicCompliance.setObjects((_B,_AL))
if mibBuilder.loadTexts:basicCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'NodeCodeString':NodeCodeString,'huaweistorage':huaweistorage,'hwStorage':hwStorage,'hwISM':hwISM,'hwStorageDevice':hwStorageDevice,'hwNasInfo':hwNasInfo,'hwInfoShareNFSTable':hwInfoShareNFSTable,'hwInfoShareNFSEntry':hwInfoShareNFSEntry,_D:hwInfoShareNFSShareID,_s:hwInfoShareNFSFileSystemID,_t:hwInfoShareNFSDescription,_w:hwInfoShareNFSLocalPath,'hwInfoShareCIFSTable':hwInfoShareCIFSTable,'hwInfoShareCIFSEntry':hwInfoShareCIFSEntry,_E:hwInfoShareCIFSID,_x:hwInfoShareCIFSName,_u:hwInfoShareCIFSFileSystemID,_v:hwInfoShareCIFSDescription,_y:hwInfoShareCIFSLocalPath,_z:hwInfoShareCIFSOplockEnabled,_A0:hwInfoShareCIFSNotifyEnabled,_J:hwInfoShareCIFSContAvailableEna,'hwInfoSharePermsNFSTable':hwInfoSharePermsNFSTable,'hwInfoSharePermsNFSEntry':hwInfoSharePermsNFSEntry,_F:hwInfoSharePermsNFSID,_K:hwInfoSharePermsNFSAccessName,_L:hwInfoSharePermsNFSShareID,_M:hwInfoSharePermsNFSAccessType,_N:hwInfoSharePermsNFSSyncEnabled,_O:hwInfoSharePermsNFSAllSquashEna,_P:hwInfoSharePermsNFSRootSquashEna,'hwInfoSharePermsCIFSTable':hwInfoSharePermsCIFSTable,'hwInfoSharePermsCIFSEntry':hwInfoSharePermsCIFSEntry,_G:hwInfoSharePermsCIFSID,_Q:hwInfoSharePermsCIFSAccessName,_R:hwInfoSharePermsCIFSShareID,_S:hwInfoSharePermsCIFSDomainType,_T:hwInfoSharePermsCIFSPermsType,'hwInfoLogicalPortTable':hwInfoLogicalPortTable,'hwInfoLogicalPortEntry':hwInfoLogicalPortEntry,_H:hwInfoLogicalPortID,_A1:hwInfoLogicalPorttName,_A2:hwInfoLogicalPortRunStatus,_A3:hwInfoLogicalPortIPv4Addr,_A4:hwInfoLogicalPortIPv4Mask,_A5:hwInfoLogicalPortIPv4Gateway,_A6:hwInfoLogicalPortIPv6Addr,_A7:hwInfoLogicalPortIPv6Mask,_A8:hwInfoLogicalPortIPv6Gateway,_A9:hwInfoLogicalPortRole,_U:hwInfoLogicalPortSupportProt,_V:hwInfoLogicalPortHomePortType,_AA:hwInfoLogicalPortHomePortID,_AB:hwInfoLogicalPortOwnerCtrlID,_AC:hwInfoLogicalPortCurrPortType,_AD:hwInfoLogicalPortCurrPortID,_AE:hwInfoLogicalPortWorkCtrlID,_AF:hwInfoLogicalPortActState,_AG:hwInfoLogicalPortAddrFamily,_AH:hwInfoLogicalPortIsPrivate,_AI:hwInfoLogicalPortFailOVGID,_AJ:hwInfoLogicalPortFailOVEnable,_W:hwInfoLogicalPortFailBackMode,_AK:hwInfoLogicalPortFailOVGName,'hwInfoFileSysTable':hwInfoFileSysTable,'hwInfoFileSysEntry':hwInfoFileSysEntry,_I:hwInfoFileSysID,_X:hwInfoFileSysName,_Y:hwInfoFileSysHeathStatus,_Z:hwInfoFileSysRunningStatus,_a:hwInfoFileSysDescription,_b:hwInfoFileSysSubType,_c:hwInfoFileSysAllocType,_d:hwInfoFileSysCapacity,_e:hwInfoFileSysSnapshotReservePer,_f:hwInfoFileSysSnapshotUseCapacity,_g:hwInfoFileSysSectorSize,_h:hwInfoFileSysOwningContrller,_i:hwInfoFileSysWorkingController,_j:hwInfoFileSysIOPriotiry,_k:hwInfoFileSysEnableCompression,_l:hwInfoFileSysCompression,_m:hwInfoFileSysIsShowSnapDir,_n:hwInfoFileSysAvailableCapacity,_o:hwInfoFileSysAvAndAllcCapRatio,_p:hwInfoFileSysSCCachedSize,_q:hwInfoFileSysSCHitRage,_r:hwInfoFileSysCompressSavedRatio,'isoConformance':isoConformance,'isoGroups':isoGroups,_AL:currentObjectGroup,'isoCompliances':isoCompliances,'basicCompliance':basicCompliance})