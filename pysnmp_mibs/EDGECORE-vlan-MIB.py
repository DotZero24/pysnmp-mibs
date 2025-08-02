_h='vlanPrivateMapSecondaryVid'
_g='vlanPrivateMapPrimaryVid'
_f='vlanPrivateVid'
_e='vlanInetTriplePlayInetAddressType'
_d='vlanVoiceOUIPrefix'
_c='vlanSubnetPortGroupId'
_b='vlanSubnetRangeMask'
_a='vlanSubnetRangeAddr'
_Z='vlanPrivateEdgeGroupSource'
_Y='vlanMacBaseVlanPortGroupId'
_X='vlanMacBaseVlanMacMask'
_W='vlanMacBaseVlanMacAddress'
_V='vlanPrivateCommunityVlanTag'
_U='vlanDynamicVlanMacAddress'
_T='vlanNameName'
_S='vlanTriplePlayMulticastTvMulticastTvVID'
_R='vlanTriplePlayInnerVID'
_Q='DisplayString'
_P='dot1dBasePort'
_O='BRIDGE-MIB'
_N='dot1qVlanIndex'
_M='Q-BRIDGE-MIB'
_L='VlanIndex'
_K='TruthValue'
_J='OctetString'
_I='not-accessible'
_H='ifIndex'
_G='IF-MIB'
_F='read-create'
_E='EDGECORE-vlan-MIB'
_D='Integer32'
_C='read-only'
_B='read-write'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_J,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
dot1dBasePort,=mibBuilder.importSymbols(_O,_P)
rnd,=mibBuilder.importSymbols('EDGECORE-MIB','rnd')
ifIndex,=mibBuilder.importSymbols(_G,_H)
InetAddressType,=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddressType')
PortList,VlanIndex,dot1qVlanIndex=mibBuilder.importSymbols(_M,'PortList',_L,_N)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC',_Q,'MacAddress','PhysAddress','RowStatus','TextualConvention',_K)
vlan=ModuleIdentity((1,3,6,1,4,1,259,10,1,14,89,48))
if mibBuilder.loadTexts:vlan.setRevisions(('2006-02-12 00:00','2004-04-19 00:00'))
_VlanMibVersion_Type=Integer32
_VlanMibVersion_Object=MibScalar
vlanMibVersion=_VlanMibVersion_Object((1,3,6,1,4,1,259,10,1,14,89,48,1),_VlanMibVersion_Type())
vlanMibVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:vlanMibVersion.setStatus(_A)
_VlanMaxTableNumber_Type=Integer32
_VlanMaxTableNumber_Object=MibScalar
vlanMaxTableNumber=_VlanMaxTableNumber_Object((1,3,6,1,4,1,259,10,1,14,89,48,2),_VlanMaxTableNumber_Type())
vlanMaxTableNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:vlanMaxTableNumber.setStatus(_A)
_VlanNameTable_Object=MibTable
vlanNameTable=_VlanNameTable_Object((1,3,6,1,4,1,259,10,1,14,89,48,21))
if mibBuilder.loadTexts:vlanNameTable.setStatus(_A)
_VlanNameEntry_Object=MibTableRow
vlanNameEntry=_VlanNameEntry_Object((1,3,6,1,4,1,259,10,1,14,89,48,21,1))
vlanNameEntry.setIndexNames((0,_E,_T))
if mibBuilder.loadTexts:vlanNameEntry.setStatus(_A)
class _VlanNameName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_VlanNameName_Type.__name__=_Q
_VlanNameName_Object=MibTableColumn
vlanNameName=_VlanNameName_Object((1,3,6,1,4,1,259,10,1,14,89,48,21,1,1),_VlanNameName_Type())
vlanNameName.setMaxAccess(_C)
if mibBuilder.loadTexts:vlanNameName.setStatus(_A)
_VlanNameTag_Type=Integer32
_VlanNameTag_Object=MibTableColumn
vlanNameTag=_VlanNameTag_Object((1,3,6,1,4,1,259,10,1,14,89,48,21,1,2),_VlanNameTag_Type())
vlanNameTag.setMaxAccess(_C)
if mibBuilder.loadTexts:vlanNameTag.setStatus(_A)
_VlanNameIfIndex_Type=Integer32
_VlanNameIfIndex_Object=MibTableColumn
vlanNameIfIndex=_VlanNameIfIndex_Object((1,3,6,1,4,1,259,10,1,14,89,48,21,1,3),_VlanNameIfIndex_Type())
vlanNameIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:vlanNameIfIndex.setStatus(_A)
_VlanPortModeTable_Object=MibTable
vlanPortModeTable=_VlanPortModeTable_Object((1,3,6,1,4,1,259,10,1,14,89,48,22))
if mibBuilder.loadTexts:vlanPortModeTable.setStatus(_A)
_VlanPortModeEntry_Object=MibTableRow
vlanPortModeEntry=_VlanPortModeEntry_Object((1,3,6,1,4,1,259,10,1,14,89,48,22,1))
vlanPortModeEntry.setIndexNames((0,_G,_H))
if mibBuilder.loadTexts:vlanPortModeEntry.setStatus(_A)
_VlanPortModeState_Type=Integer32
_VlanPortModeState_Object=MibTableColumn
vlanPortModeState=_VlanPortModeState_Object((1,3,6,1,4,1,259,10,1,14,89,48,22,1,1),_VlanPortModeState_Type())
vlanPortModeState.setMaxAccess(_B)
if mibBuilder.loadTexts:vlanPortModeState.setStatus(_A)
class _VlanSendUnknownToAllPorts_Type(TruthValue):defaultValue=1
_VlanSendUnknownToAllPorts_Type.__name__=_K
_VlanSendUnknownToAllPorts_Object=MibScalar
vlanSendUnknownToAllPorts=_VlanSendUnknownToAllPorts_Object((1,3,6,1,4,1,259,10,1,14,89,48,27),_VlanSendUnknownToAllPorts_Type())
vlanSendUnknownToAllPorts.setMaxAccess(_B)
if mibBuilder.loadTexts:vlanSendUnknownToAllPorts.setStatus(_A)
_VlanDefaultSupported_Type=TruthValue
_VlanDefaultSupported_Object=MibScalar
vlanDefaultSupported=_VlanDefaultSupported_Object((1,3,6,1,4,1,259,10,1,14,89,48,29),_VlanDefaultSupported_Type())
vlanDefaultSupported.setMaxAccess(_C)
if mibBuilder.loadTexts:vlanDefaultSupported.setStatus(_A)
_VlanDot1vSupported_Type=TruthValue
_VlanDot1vSupported_Object=MibScalar
vlanDot1vSupported=_VlanDot1vSupported_Object((1,3,6,1,4,1,259,10,1,14,89,48,31),_VlanDot1vSupported_Type())
vlanDot1vSupported.setMaxAccess(_C)
if mibBuilder.loadTexts:vlanDot1vSupported.setStatus(_A)
_VlanDefaultEnabled_Type=TruthValue
_VlanDefaultEnabled_Object=MibScalar
vlanDefaultEnabled=_VlanDefaultEnabled_Object((1,3,6,1,4,1,259,10,1,14,89,48,32),_VlanDefaultEnabled_Type())
vlanDefaultEnabled.setMaxAccess(_B)
if mibBuilder.loadTexts:vlanDefaultEnabled.setStatus(_A)
_VlanSpecialTagTable_Object=MibTable
vlanSpecialTagTable=_VlanSpecialTagTable_Object((1,3,6,1,4,1,259,10,1,14,89,48,33))
if mibBuilder.loadTexts:vlanSpecialTagTable.setStatus(_A)
_VlanSpecialTagEntry_Object=MibTableRow
vlanSpecialTagEntry=_VlanSpecialTagEntry_Object((1,3,6,1,4,1,259,10,1,14,89,48,33,1))
vlanSpecialTagEntry.setIndexNames((0,_G,_H))
if mibBuilder.loadTexts:vlanSpecialTagEntry.setStatus(_A)
_VlanSpecialTagVID_Type=VlanIndex
_VlanSpecialTagVID_Object=MibTableColumn
vlanSpecialTagVID=_VlanSpecialTagVID_Object((1,3,6,1,4,1,259,10,1,14,89,48,33,1,1),_VlanSpecialTagVID_Type())
vlanSpecialTagVID.setMaxAccess(_B)
if mibBuilder.loadTexts:vlanSpecialTagVID.setStatus(_A)
_VlanSpecialTagStatus_Type=RowStatus
_VlanSpecialTagStatus_Object=MibTableColumn
vlanSpecialTagStatus=_VlanSpecialTagStatus_Object((1,3,6,1,4,1,259,10,1,14,89,48,33,1,2),_VlanSpecialTagStatus_Type())
vlanSpecialTagStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:vlanSpecialTagStatus.setStatus(_A)
_VlanSpecialTagCurrentTable_Object=MibTable
vlanSpecialTagCurrentTable=_VlanSpecialTagCurrentTable_Object((1,3,6,1,4,1,259,10,1,14,89,48,34))
if mibBuilder.loadTexts:vlanSpecialTagCurrentTable.setStatus(_A)
_VlanSpecialTagCurrentEntry_Object=MibTableRow
vlanSpecialTagCurrentEntry=_VlanSpecialTagCurrentEntry_Object((1,3,6,1,4,1,259,10,1,14,89,48,34,1))
vlanSpecialTagCurrentEntry.setIndexNames((0,_G,_H))
if mibBuilder.loadTexts:vlanSpecialTagCurrentEntry.setStatus(_A)
_VlanSpecialTagCurrentVID_Type=VlanIndex
_VlanSpecialTagCurrentVID_Object=MibTableColumn
vlanSpecialTagCurrentVID=_VlanSpecialTagCurrentVID_Object((1,3,6,1,4,1,259,10,1,14,89,48,34,1,1),_VlanSpecialTagCurrentVID_Type())
vlanSpecialTagCurrentVID.setMaxAccess(_C)
if mibBuilder.loadTexts:vlanSpecialTagCurrentVID.setStatus(_A)
_VlanSpecialTagCurrentReserved_Type=TruthValue
_VlanSpecialTagCurrentReserved_Object=MibTableColumn
vlanSpecialTagCurrentReserved=_VlanSpecialTagCurrentReserved_Object((1,3,6,1,4,1,259,10,1,14,89,48,34,1,2),_VlanSpecialTagCurrentReserved_Type())
vlanSpecialTagCurrentReserved.setMaxAccess(_C)
if mibBuilder.loadTexts:vlanSpecialTagCurrentReserved.setStatus(_A)
_VlanSpecialTagCurrentActive_Type=TruthValue
_VlanSpecialTagCurrentActive_Object=MibTableColumn
vlanSpecialTagCurrentActive=_VlanSpecialTagCurrentActive_Object((1,3,6,1,4,1,259,10,1,14,89,48,34,1,3),_VlanSpecialTagCurrentActive_Type())
vlanSpecialTagCurrentActive.setMaxAccess(_C)
if mibBuilder.loadTexts:vlanSpecialTagCurrentActive.setStatus(_A)
_VlanPrivateEdgeSupported_Type=TruthValue
_VlanPrivateEdgeSupported_Object=MibScalar
vlanPrivateEdgeSupported=_VlanPrivateEdgeSupported_Object((1,3,6,1,4,1,259,10,1,14,89,48,35),_VlanPrivateEdgeSupported_Type())
vlanPrivateEdgeSupported.setMaxAccess(_C)
if mibBuilder.loadTexts:vlanPrivateEdgeSupported.setStatus(_A)
_VlanPrivateEdgeVersion_Type=Integer32
_VlanPrivateEdgeVersion_Object=MibScalar
vlanPrivateEdgeVersion=_VlanPrivateEdgeVersion_Object((1,3,6,1,4,1,259,10,1,14,89,48,36),_VlanPrivateEdgeVersion_Type())
vlanPrivateEdgeVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:vlanPrivateEdgeVersion.setStatus(_A)
_VlanPrivateEdgeTable_Object=MibTable
vlanPrivateEdgeTable=_VlanPrivateEdgeTable_Object((1,3,6,1,4,1,259,10,1,14,89,48,37))
if mibBuilder.loadTexts:vlanPrivateEdgeTable.setStatus(_A)
_VlanPrivateEdgeEntry_Object=MibTableRow
vlanPrivateEdgeEntry=_VlanPrivateEdgeEntry_Object((1,3,6,1,4,1,259,10,1,14,89,48,37,1))
vlanPrivateEdgeEntry.setIndexNames((0,_G,_H))
if mibBuilder.loadTexts:vlanPrivateEdgeEntry.setStatus(_A)
class _VlanPrivateEdgeUplink_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_VlanPrivateEdgeUplink_Type.__name__=_D
_VlanPrivateEdgeUplink_Object=MibTableColumn
vlanPrivateEdgeUplink=_VlanPrivateEdgeUplink_Object((1,3,6,1,4,1,259,10,1,14,89,48,37,1,1),_VlanPrivateEdgeUplink_Type())
vlanPrivateEdgeUplink.setMaxAccess(_B)
if mibBuilder.loadTexts:vlanPrivateEdgeUplink.setStatus(_A)
_VlanPrivateEdgeStatus_Type=RowStatus
_VlanPrivateEdgeStatus_Object=MibTableColumn
vlanPrivateEdgeStatus=_VlanPrivateEdgeStatus_Object((1,3,6,1,4,1,259,10,1,14,89,48,37,1,2),_VlanPrivateEdgeStatus_Type())
vlanPrivateEdgeStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:vlanPrivateEdgeStatus.setStatus(_A)
_VlanDynamicVlanSupported_Type=TruthValue
_VlanDynamicVlanSupported_Object=MibScalar
vlanDynamicVlanSupported=_VlanDynamicVlanSupported_Object((1,3,6,1,4,1,259,10,1,14,89,48,38),_VlanDynamicVlanSupported_Type())
vlanDynamicVlanSupported.setMaxAccess(_C)
if mibBuilder.loadTexts:vlanDynamicVlanSupported.setStatus(_A)
_VlanDynamicVlanTable_Object=MibTable
vlanDynamicVlanTable=_VlanDynamicVlanTable_Object((1,3,6,1,4,1,259,10,1,14,89,48,39))
if mibBuilder.loadTexts:vlanDynamicVlanTable.setStatus(_A)
_VlanDynamicVlanEntry_Object=MibTableRow
vlanDynamicVlanEntry=_VlanDynamicVlanEntry_Object((1,3,6,1,4,1,259,10,1,14,89,48,39,1))
vlanDynamicVlanEntry.setIndexNames((0,_E,_U))
if mibBuilder.loadTexts:vlanDynamicVlanEntry.setStatus(_A)
_VlanDynamicVlanMacAddress_Type=MacAddress
_VlanDynamicVlanMacAddress_Object=MibTableColumn
vlanDynamicVlanMacAddress=_VlanDynamicVlanMacAddress_Object((1,3,6,1,4,1,259,10,1,14,89,48,39,1,1),_VlanDynamicVlanMacAddress_Type())
vlanDynamicVlanMacAddress.setMaxAccess(_I)
if mibBuilder.loadTexts:vlanDynamicVlanMacAddress.setStatus(_A)
_VlanDynamicVlanTag_Type=VlanIndex
_VlanDynamicVlanTag_Object=MibTableColumn
vlanDynamicVlanTag=_VlanDynamicVlanTag_Object((1,3,6,1,4,1,259,10,1,14,89,48,39,1,2),_VlanDynamicVlanTag_Type())
vlanDynamicVlanTag.setMaxAccess(_B)
if mibBuilder.loadTexts:vlanDynamicVlanTag.setStatus(_A)
_VlanDynamicVlanStatus_Type=RowStatus
_VlanDynamicVlanStatus_Object=MibTableColumn
vlanDynamicVlanStatus=_VlanDynamicVlanStatus_Object((1,3,6,1,4,1,259,10,1,14,89,48,39,1,3),_VlanDynamicVlanStatus_Type())
vlanDynamicVlanStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:vlanDynamicVlanStatus.setStatus(_A)
_VlanPortModeExtTable_Object=MibTable
vlanPortModeExtTable=_VlanPortModeExtTable_Object((1,3,6,1,4,1,259,10,1,14,89,48,40))
if mibBuilder.loadTexts:vlanPortModeExtTable.setStatus(_A)
_VlanPortModeExtEntry_Object=MibTableRow
vlanPortModeExtEntry=_VlanPortModeExtEntry_Object((1,3,6,1,4,1,259,10,1,14,89,48,40,1))
vlanPortModeExtEntry.setIndexNames((0,_G,_H))
if mibBuilder.loadTexts:vlanPortModeExtEntry.setStatus(_A)
_VlanPortModeExtState_Type=Integer32
_VlanPortModeExtState_Object=MibTableColumn
vlanPortModeExtState=_VlanPortModeExtState_Object((1,3,6,1,4,1,259,10,1,14,89,48,40,1,1),_VlanPortModeExtState_Type())
vlanPortModeExtState.setMaxAccess(_B)
if mibBuilder.loadTexts:vlanPortModeExtState.setStatus(_A)
_VlanPortModeExtStatus_Type=RowStatus
_VlanPortModeExtStatus_Object=MibTableColumn
vlanPortModeExtStatus=_VlanPortModeExtStatus_Object((1,3,6,1,4,1,259,10,1,14,89,48,40,1,2),_VlanPortModeExtStatus_Type())
vlanPortModeExtStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:vlanPortModeExtStatus.setStatus(_A)
_VlanPrivateSupported_Type=TruthValue
_VlanPrivateSupported_Object=MibScalar
vlanPrivateSupported=_VlanPrivateSupported_Object((1,3,6,1,4,1,259,10,1,14,89,48,41),_VlanPrivateSupported_Type())
vlanPrivateSupported.setMaxAccess(_C)
if mibBuilder.loadTexts:vlanPrivateSupported.setStatus(_A)
_VlanPrivateTableOld_Object=MibTable
vlanPrivateTableOld=_VlanPrivateTableOld_Object((1,3,6,1,4,1,259,10,1,14,89,48,42))
if mibBuilder.loadTexts:vlanPrivateTableOld.setStatus(_A)
_VlanPrivateEntryOld_Object=MibTableRow
vlanPrivateEntryOld=_VlanPrivateEntryOld_Object((1,3,6,1,4,1,259,10,1,14,89,48,42,1))
vlanPrivateEntryOld.setIndexNames((0,_M,_N))
if mibBuilder.loadTexts:vlanPrivateEntryOld.setStatus(_A)
class _VlanPrivateOldIsolatedVlanTag_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4094))
_VlanPrivateOldIsolatedVlanTag_Type.__name__=_D
_VlanPrivateOldIsolatedVlanTag_Object=MibTableColumn
vlanPrivateOldIsolatedVlanTag=_VlanPrivateOldIsolatedVlanTag_Object((1,3,6,1,4,1,259,10,1,14,89,48,42,1,1),_VlanPrivateOldIsolatedVlanTag_Type())
vlanPrivateOldIsolatedVlanTag.setMaxAccess(_B)
if mibBuilder.loadTexts:vlanPrivateOldIsolatedVlanTag.setStatus(_A)
_VlanPrivateOldStatus_Type=RowStatus
_VlanPrivateOldStatus_Object=MibTableColumn
vlanPrivateOldStatus=_VlanPrivateOldStatus_Object((1,3,6,1,4,1,259,10,1,14,89,48,42,1,2),_VlanPrivateOldStatus_Type())
vlanPrivateOldStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:vlanPrivateOldStatus.setStatus(_A)
_VlanPrivateCommunityTable_Object=MibTable
vlanPrivateCommunityTable=_VlanPrivateCommunityTable_Object((1,3,6,1,4,1,259,10,1,14,89,48,43))
if mibBuilder.loadTexts:vlanPrivateCommunityTable.setStatus(_A)
_VlanPrivateCommunityEntry_Object=MibTableRow
vlanPrivateCommunityEntry=_VlanPrivateCommunityEntry_Object((1,3,6,1,4,1,259,10,1,14,89,48,43,1))
vlanPrivateCommunityEntry.setIndexNames((0,_M,_N),(0,_E,_V))
if mibBuilder.loadTexts:vlanPrivateCommunityEntry.setStatus(_A)
_VlanPrivateCommunityVlanTag_Type=VlanIndex
_VlanPrivateCommunityVlanTag_Object=MibTableColumn
vlanPrivateCommunityVlanTag=_VlanPrivateCommunityVlanTag_Object((1,3,6,1,4,1,259,10,1,14,89,48,43,1,1),_VlanPrivateCommunityVlanTag_Type())
vlanPrivateCommunityVlanTag.setMaxAccess(_I)
if mibBuilder.loadTexts:vlanPrivateCommunityVlanTag.setStatus(_A)
_VlanPrivateCommunityStatus_Type=RowStatus
_VlanPrivateCommunityStatus_Object=MibTableColumn
vlanPrivateCommunityStatus=_VlanPrivateCommunityStatus_Object((1,3,6,1,4,1,259,10,1,14,89,48,43,1,2),_VlanPrivateCommunityStatus_Type())
vlanPrivateCommunityStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:vlanPrivateCommunityStatus.setStatus(_A)
_VlanMulticastTvTable_Object=MibTable
vlanMulticastTvTable=_VlanMulticastTvTable_Object((1,3,6,1,4,1,259,10,1,14,89,48,44))
if mibBuilder.loadTexts:vlanMulticastTvTable.setStatus(_A)
_VlanMulticastTvEntry_Object=MibTableRow
vlanMulticastTvEntry=_VlanMulticastTvEntry_Object((1,3,6,1,4,1,259,10,1,14,89,48,44,1))
vlanMulticastTvEntry.setIndexNames((0,_G,_H))
if mibBuilder.loadTexts:vlanMulticastTvEntry.setStatus(_A)
_VlanMulticastTvVID_Type=VlanIndex
_VlanMulticastTvVID_Object=MibTableColumn
vlanMulticastTvVID=_VlanMulticastTvVID_Object((1,3,6,1,4,1,259,10,1,14,89,48,44,1,1),_VlanMulticastTvVID_Type())
vlanMulticastTvVID.setMaxAccess(_B)
if mibBuilder.loadTexts:vlanMulticastTvVID.setStatus(_A)
_VlanMulticastTvStatus_Type=RowStatus
_VlanMulticastTvStatus_Object=MibTableColumn
vlanMulticastTvStatus=_VlanMulticastTvStatus_Object((1,3,6,1,4,1,259,10,1,14,89,48,44,1,2),_VlanMulticastTvStatus_Type())
vlanMulticastTvStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:vlanMulticastTvStatus.setStatus(_A)
_VlanMacBaseVlanGroupTable_Object=MibTable
vlanMacBaseVlanGroupTable=_VlanMacBaseVlanGroupTable_Object((1,3,6,1,4,1,259,10,1,14,89,48,45))
if mibBuilder.loadTexts:vlanMacBaseVlanGroupTable.setStatus(_A)
_VlanMacBaseVlanGroupEntry_Object=MibTableRow
vlanMacBaseVlanGroupEntry=_VlanMacBaseVlanGroupEntry_Object((1,3,6,1,4,1,259,10,1,14,89,48,45,1))
vlanMacBaseVlanGroupEntry.setIndexNames((0,_E,_W),(0,_E,_X))
if mibBuilder.loadTexts:vlanMacBaseVlanGroupEntry.setStatus(_A)
_VlanMacBaseVlanMacAddress_Type=MacAddress
_VlanMacBaseVlanMacAddress_Object=MibTableColumn
vlanMacBaseVlanMacAddress=_VlanMacBaseVlanMacAddress_Object((1,3,6,1,4,1,259,10,1,14,89,48,45,1,1),_VlanMacBaseVlanMacAddress_Type())
vlanMacBaseVlanMacAddress.setMaxAccess(_I)
if mibBuilder.loadTexts:vlanMacBaseVlanMacAddress.setStatus(_A)
class _VlanMacBaseVlanMacMask_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(9,48))
_VlanMacBaseVlanMacMask_Type.__name__=_D
_VlanMacBaseVlanMacMask_Object=MibTableColumn
vlanMacBaseVlanMacMask=_VlanMacBaseVlanMacMask_Object((1,3,6,1,4,1,259,10,1,14,89,48,45,1,2),_VlanMacBaseVlanMacMask_Type())
vlanMacBaseVlanMacMask.setMaxAccess(_I)
if mibBuilder.loadTexts:vlanMacBaseVlanMacMask.setStatus(_A)
class _VlanMacBaseVlanGroupId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_VlanMacBaseVlanGroupId_Type.__name__=_D
_VlanMacBaseVlanGroupId_Object=MibTableColumn
vlanMacBaseVlanGroupId=_VlanMacBaseVlanGroupId_Object((1,3,6,1,4,1,259,10,1,14,89,48,45,1,3),_VlanMacBaseVlanGroupId_Type())
vlanMacBaseVlanGroupId.setMaxAccess(_F)
if mibBuilder.loadTexts:vlanMacBaseVlanGroupId.setStatus(_A)
_VlanMacBaseVlanGroupRowStatus_Type=RowStatus
_VlanMacBaseVlanGroupRowStatus_Object=MibTableColumn
vlanMacBaseVlanGroupRowStatus=_VlanMacBaseVlanGroupRowStatus_Object((1,3,6,1,4,1,259,10,1,14,89,48,45,1,4),_VlanMacBaseVlanGroupRowStatus_Type())
vlanMacBaseVlanGroupRowStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:vlanMacBaseVlanGroupRowStatus.setStatus(_A)
_VlanMacBaseVlanPortTable_Object=MibTable
vlanMacBaseVlanPortTable=_VlanMacBaseVlanPortTable_Object((1,3,6,1,4,1,259,10,1,14,89,48,46))
if mibBuilder.loadTexts:vlanMacBaseVlanPortTable.setStatus(_A)
_VlanMacBaseVlanPortEntry_Object=MibTableRow
vlanMacBaseVlanPortEntry=_VlanMacBaseVlanPortEntry_Object((1,3,6,1,4,1,259,10,1,14,89,48,46,1))
vlanMacBaseVlanPortEntry.setIndexNames((0,_O,_P),(0,_E,_Y))
if mibBuilder.loadTexts:vlanMacBaseVlanPortEntry.setStatus(_A)
class _VlanMacBaseVlanPortGroupId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_VlanMacBaseVlanPortGroupId_Type.__name__=_D
_VlanMacBaseVlanPortGroupId_Object=MibTableColumn
vlanMacBaseVlanPortGroupId=_VlanMacBaseVlanPortGroupId_Object((1,3,6,1,4,1,259,10,1,14,89,48,46,1,1),_VlanMacBaseVlanPortGroupId_Type())
vlanMacBaseVlanPortGroupId.setMaxAccess(_I)
if mibBuilder.loadTexts:vlanMacBaseVlanPortGroupId.setStatus(_A)
_VlanMacBaseVlanPortGroupVid_Type=VlanIndex
_VlanMacBaseVlanPortGroupVid_Object=MibTableColumn
vlanMacBaseVlanPortGroupVid=_VlanMacBaseVlanPortGroupVid_Object((1,3,6,1,4,1,259,10,1,14,89,48,46,1,2),_VlanMacBaseVlanPortGroupVid_Type())
vlanMacBaseVlanPortGroupVid.setMaxAccess(_F)
if mibBuilder.loadTexts:vlanMacBaseVlanPortGroupVid.setStatus(_A)
_VlanMacBaseVlanPortRowStatus_Type=RowStatus
_VlanMacBaseVlanPortRowStatus_Object=MibTableColumn
vlanMacBaseVlanPortRowStatus=_VlanMacBaseVlanPortRowStatus_Object((1,3,6,1,4,1,259,10,1,14,89,48,46,1,3),_VlanMacBaseVlanPortRowStatus_Type())
vlanMacBaseVlanPortRowStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:vlanMacBaseVlanPortRowStatus.setStatus(_A)
_VlanPrivateEdgeGroupTable_Object=MibTable
vlanPrivateEdgeGroupTable=_VlanPrivateEdgeGroupTable_Object((1,3,6,1,4,1,259,10,1,14,89,48,47))
if mibBuilder.loadTexts:vlanPrivateEdgeGroupTable.setStatus(_A)
_VlanPrivateEdgeGroupEntry_Object=MibTableRow
vlanPrivateEdgeGroupEntry=_VlanPrivateEdgeGroupEntry_Object((1,3,6,1,4,1,259,10,1,14,89,48,47,1))
vlanPrivateEdgeGroupEntry.setIndexNames((0,_E,_Z))
if mibBuilder.loadTexts:vlanPrivateEdgeGroupEntry.setStatus(_A)
class _VlanPrivateEdgeGroupSource_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_VlanPrivateEdgeGroupSource_Type.__name__=_D
_VlanPrivateEdgeGroupSource_Object=MibTableColumn
vlanPrivateEdgeGroupSource=_VlanPrivateEdgeGroupSource_Object((1,3,6,1,4,1,259,10,1,14,89,48,47,1,1),_VlanPrivateEdgeGroupSource_Type())
vlanPrivateEdgeGroupSource.setMaxAccess(_C)
if mibBuilder.loadTexts:vlanPrivateEdgeGroupSource.setStatus(_A)
class _VlanPrivateEdgeGroupUplink_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_VlanPrivateEdgeGroupUplink_Type.__name__=_D
_VlanPrivateEdgeGroupUplink_Object=MibTableColumn
vlanPrivateEdgeGroupUplink=_VlanPrivateEdgeGroupUplink_Object((1,3,6,1,4,1,259,10,1,14,89,48,47,1,2),_VlanPrivateEdgeGroupUplink_Type())
vlanPrivateEdgeGroupUplink.setMaxAccess(_B)
if mibBuilder.loadTexts:vlanPrivateEdgeGroupUplink.setStatus(_A)
_VlanPrivateEdgeGroupStatus_Type=RowStatus
_VlanPrivateEdgeGroupStatus_Object=MibTableColumn
vlanPrivateEdgeGroupStatus=_VlanPrivateEdgeGroupStatus_Object((1,3,6,1,4,1,259,10,1,14,89,48,47,1,3),_VlanPrivateEdgeGroupStatus_Type())
vlanPrivateEdgeGroupStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:vlanPrivateEdgeGroupStatus.setStatus(_A)
_VlanPrivateEdgeGroupIfIndexTable_Object=MibTable
vlanPrivateEdgeGroupIfIndexTable=_VlanPrivateEdgeGroupIfIndexTable_Object((1,3,6,1,4,1,259,10,1,14,89,48,48))
if mibBuilder.loadTexts:vlanPrivateEdgeGroupIfIndexTable.setStatus(_A)
_VlanPrivateEdgeGroupIfIndexEntry_Object=MibTableRow
vlanPrivateEdgeGroupIfIndexEntry=_VlanPrivateEdgeGroupIfIndexEntry_Object((1,3,6,1,4,1,259,10,1,14,89,48,48,1))
vlanPrivateEdgeGroupIfIndexEntry.setIndexNames((0,_G,_H))
if mibBuilder.loadTexts:vlanPrivateEdgeGroupIfIndexEntry.setStatus(_A)
class _VlanPrivateEdgeGroupIfIndexID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_VlanPrivateEdgeGroupIfIndexID_Type.__name__=_D
_VlanPrivateEdgeGroupIfIndexID_Object=MibTableColumn
vlanPrivateEdgeGroupIfIndexID=_VlanPrivateEdgeGroupIfIndexID_Object((1,3,6,1,4,1,259,10,1,14,89,48,48,1,1),_VlanPrivateEdgeGroupIfIndexID_Type())
vlanPrivateEdgeGroupIfIndexID.setMaxAccess(_C)
if mibBuilder.loadTexts:vlanPrivateEdgeGroupIfIndexID.setStatus(_A)
class _VlanPrivateEdgeGroupIfIndexDomainID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_VlanPrivateEdgeGroupIfIndexDomainID_Type.__name__=_D
_VlanPrivateEdgeGroupIfIndexDomainID_Object=MibTableColumn
vlanPrivateEdgeGroupIfIndexDomainID=_VlanPrivateEdgeGroupIfIndexDomainID_Object((1,3,6,1,4,1,259,10,1,14,89,48,48,1,2),_VlanPrivateEdgeGroupIfIndexDomainID_Type())
vlanPrivateEdgeGroupIfIndexDomainID.setMaxAccess(_C)
if mibBuilder.loadTexts:vlanPrivateEdgeGroupIfIndexDomainID.setStatus(_A)
_VlanSubnetRangeTable_Object=MibTable
vlanSubnetRangeTable=_VlanSubnetRangeTable_Object((1,3,6,1,4,1,259,10,1,14,89,48,49))
if mibBuilder.loadTexts:vlanSubnetRangeTable.setStatus(_A)
_VlanSubnetRangeEntry_Object=MibTableRow
vlanSubnetRangeEntry=_VlanSubnetRangeEntry_Object((1,3,6,1,4,1,259,10,1,14,89,48,49,1))
vlanSubnetRangeEntry.setIndexNames((0,_E,_a),(0,_E,_b))
if mibBuilder.loadTexts:vlanSubnetRangeEntry.setStatus(_A)
_VlanSubnetRangeAddr_Type=IpAddress
_VlanSubnetRangeAddr_Object=MibTableColumn
vlanSubnetRangeAddr=_VlanSubnetRangeAddr_Object((1,3,6,1,4,1,259,10,1,14,89,48,49,1,1),_VlanSubnetRangeAddr_Type())
vlanSubnetRangeAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:vlanSubnetRangeAddr.setStatus(_A)
class _VlanSubnetRangeMask_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,32))
_VlanSubnetRangeMask_Type.__name__=_D
_VlanSubnetRangeMask_Object=MibTableColumn
vlanSubnetRangeMask=_VlanSubnetRangeMask_Object((1,3,6,1,4,1,259,10,1,14,89,48,49,1,2),_VlanSubnetRangeMask_Type())
vlanSubnetRangeMask.setMaxAccess(_C)
if mibBuilder.loadTexts:vlanSubnetRangeMask.setStatus(_A)
class _VlanSubnetRangeGroupId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_VlanSubnetRangeGroupId_Type.__name__=_D
_VlanSubnetRangeGroupId_Object=MibTableColumn
vlanSubnetRangeGroupId=_VlanSubnetRangeGroupId_Object((1,3,6,1,4,1,259,10,1,14,89,48,49,1,3),_VlanSubnetRangeGroupId_Type())
vlanSubnetRangeGroupId.setMaxAccess(_F)
if mibBuilder.loadTexts:vlanSubnetRangeGroupId.setStatus(_A)
_VlanSubnetRangeRowStatus_Type=RowStatus
_VlanSubnetRangeRowStatus_Object=MibTableColumn
vlanSubnetRangeRowStatus=_VlanSubnetRangeRowStatus_Object((1,3,6,1,4,1,259,10,1,14,89,48,49,1,4),_VlanSubnetRangeRowStatus_Type())
vlanSubnetRangeRowStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:vlanSubnetRangeRowStatus.setStatus(_A)
_VlanSubnetPortTable_Object=MibTable
vlanSubnetPortTable=_VlanSubnetPortTable_Object((1,3,6,1,4,1,259,10,1,14,89,48,50))
if mibBuilder.loadTexts:vlanSubnetPortTable.setStatus(_A)
_VlanSubnetPortEntry_Object=MibTableRow
vlanSubnetPortEntry=_VlanSubnetPortEntry_Object((1,3,6,1,4,1,259,10,1,14,89,48,50,1))
vlanSubnetPortEntry.setIndexNames((0,_O,_P),(0,_E,_c))
if mibBuilder.loadTexts:vlanSubnetPortEntry.setStatus(_A)
class _VlanSubnetPortGroupId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_VlanSubnetPortGroupId_Type.__name__=_D
_VlanSubnetPortGroupId_Object=MibTableColumn
vlanSubnetPortGroupId=_VlanSubnetPortGroupId_Object((1,3,6,1,4,1,259,10,1,14,89,48,50,1,1),_VlanSubnetPortGroupId_Type())
vlanSubnetPortGroupId.setMaxAccess(_I)
if mibBuilder.loadTexts:vlanSubnetPortGroupId.setStatus(_A)
class _VlanSubnetPortGroupVid_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094))
_VlanSubnetPortGroupVid_Type.__name__=_D
_VlanSubnetPortGroupVid_Object=MibTableColumn
vlanSubnetPortGroupVid=_VlanSubnetPortGroupVid_Object((1,3,6,1,4,1,259,10,1,14,89,48,50,1,2),_VlanSubnetPortGroupVid_Type())
vlanSubnetPortGroupVid.setMaxAccess(_F)
if mibBuilder.loadTexts:vlanSubnetPortGroupVid.setStatus(_A)
_VlanSubnetPortRowStatus_Type=RowStatus
_VlanSubnetPortRowStatus_Object=MibTableColumn
vlanSubnetPortRowStatus=_VlanSubnetPortRowStatus_Object((1,3,6,1,4,1,259,10,1,14,89,48,50,1,3),_VlanSubnetPortRowStatus_Type())
vlanSubnetPortRowStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:vlanSubnetPortRowStatus.setStatus(_A)
_VlanTriplePlayTable_Object=MibTable
vlanTriplePlayTable=_VlanTriplePlayTable_Object((1,3,6,1,4,1,259,10,1,14,89,48,51))
if mibBuilder.loadTexts:vlanTriplePlayTable.setStatus(_A)
_VlanTriplePlayEntry_Object=MibTableRow
vlanTriplePlayEntry=_VlanTriplePlayEntry_Object((1,3,6,1,4,1,259,10,1,14,89,48,51,1))
vlanTriplePlayEntry.setIndexNames((0,_E,_R))
if mibBuilder.loadTexts:vlanTriplePlayEntry.setStatus(_A)
_VlanTriplePlayInnerVID_Type=VlanIndex
_VlanTriplePlayInnerVID_Object=MibTableColumn
vlanTriplePlayInnerVID=_VlanTriplePlayInnerVID_Object((1,3,6,1,4,1,259,10,1,14,89,48,51,1,1),_VlanTriplePlayInnerVID_Type())
vlanTriplePlayInnerVID.setMaxAccess(_I)
if mibBuilder.loadTexts:vlanTriplePlayInnerVID.setStatus(_A)
_VlanTriplePlayMulticastTvVID_Type=VlanIndex
_VlanTriplePlayMulticastTvVID_Object=MibTableColumn
vlanTriplePlayMulticastTvVID=_VlanTriplePlayMulticastTvVID_Object((1,3,6,1,4,1,259,10,1,14,89,48,51,1,2),_VlanTriplePlayMulticastTvVID_Type())
vlanTriplePlayMulticastTvVID.setMaxAccess(_F)
if mibBuilder.loadTexts:vlanTriplePlayMulticastTvVID.setStatus(_A)
_VlanTriplePlayRowStatus_Type=RowStatus
_VlanTriplePlayRowStatus_Object=MibTableColumn
vlanTriplePlayRowStatus=_VlanTriplePlayRowStatus_Object((1,3,6,1,4,1,259,10,1,14,89,48,51,1,3),_VlanTriplePlayRowStatus_Type())
vlanTriplePlayRowStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:vlanTriplePlayRowStatus.setStatus(_A)
_VlanTriplePlayMulticastTvTable_Object=MibTable
vlanTriplePlayMulticastTvTable=_VlanTriplePlayMulticastTvTable_Object((1,3,6,1,4,1,259,10,1,14,89,48,52))
if mibBuilder.loadTexts:vlanTriplePlayMulticastTvTable.setStatus(_A)
_VlanTriplePlayMulticatTvEntry_Object=MibTableRow
vlanTriplePlayMulticatTvEntry=_VlanTriplePlayMulticatTvEntry_Object((1,3,6,1,4,1,259,10,1,14,89,48,52,1))
vlanTriplePlayMulticatTvEntry.setIndexNames((0,_E,_S))
if mibBuilder.loadTexts:vlanTriplePlayMulticatTvEntry.setStatus(_A)
_VlanTriplePlayMulticastTvMulticastTvVID_Type=VlanIndex
_VlanTriplePlayMulticastTvMulticastTvVID_Object=MibTableColumn
vlanTriplePlayMulticastTvMulticastTvVID=_VlanTriplePlayMulticastTvMulticastTvVID_Object((1,3,6,1,4,1,259,10,1,14,89,48,52,1,1),_VlanTriplePlayMulticastTvMulticastTvVID_Type())
vlanTriplePlayMulticastTvMulticastTvVID.setMaxAccess(_C)
if mibBuilder.loadTexts:vlanTriplePlayMulticastTvMulticastTvVID.setStatus(_A)
_VlanTriplePlayMulticastTvMulticastTvPortList_Type=PortList
_VlanTriplePlayMulticastTvMulticastTvPortList_Object=MibTableColumn
vlanTriplePlayMulticastTvMulticastTvPortList=_VlanTriplePlayMulticastTvMulticastTvPortList_Object((1,3,6,1,4,1,259,10,1,14,89,48,52,1,2),_VlanTriplePlayMulticastTvMulticastTvPortList_Type())
vlanTriplePlayMulticastTvMulticastTvPortList.setMaxAccess(_B)
if mibBuilder.loadTexts:vlanTriplePlayMulticastTvMulticastTvPortList.setStatus(_A)
_VlanDefaultExtManagment_Type=TruthValue
_VlanDefaultExtManagment_Object=MibScalar
vlanDefaultExtManagment=_VlanDefaultExtManagment_Object((1,3,6,1,4,1,259,10,1,14,89,48,53),_VlanDefaultExtManagment_Type())
vlanDefaultExtManagment.setMaxAccess(_B)
if mibBuilder.loadTexts:vlanDefaultExtManagment.setStatus(_A)
_VlanVoice_ObjectIdentity=ObjectIdentity
vlanVoice=_VlanVoice_ObjectIdentity((1,3,6,1,4,1,259,10,1,14,89,48,54))
class _VlanVoiceAgingTimeout_Type(Integer32):defaultValue=1440;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,43200))
_VlanVoiceAgingTimeout_Type.__name__=_D
_VlanVoiceAgingTimeout_Object=MibScalar
vlanVoiceAgingTimeout=_VlanVoiceAgingTimeout_Object((1,3,6,1,4,1,259,10,1,14,89,48,54,1),_VlanVoiceAgingTimeout_Type())
vlanVoiceAgingTimeout.setMaxAccess(_B)
if mibBuilder.loadTexts:vlanVoiceAgingTimeout.setStatus(_A)
if mibBuilder.loadTexts:vlanVoiceAgingTimeout.setUnits('minutes')
_VlanVoiceTable_Object=MibTable
vlanVoiceTable=_VlanVoiceTable_Object((1,3,6,1,4,1,259,10,1,14,89,48,54,2))
if mibBuilder.loadTexts:vlanVoiceTable.setStatus(_A)
_VlanVoiceEntry_Object=MibTableRow
vlanVoiceEntry=_VlanVoiceEntry_Object((1,3,6,1,4,1,259,10,1,14,89,48,54,2,1))
vlanVoiceEntry.setIndexNames((0,_M,_N))
if mibBuilder.loadTexts:vlanVoiceEntry.setStatus(_A)
class _VlanVoicePriority_Type(Integer32):defaultValue=6;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_VlanVoicePriority_Type.__name__=_D
_VlanVoicePriority_Object=MibTableColumn
vlanVoicePriority=_VlanVoicePriority_Object((1,3,6,1,4,1,259,10,1,14,89,48,54,2,1,1),_VlanVoicePriority_Type())
vlanVoicePriority.setMaxAccess(_B)
if mibBuilder.loadTexts:vlanVoicePriority.setStatus(_A)
class _VlanVoicePriorityRemark_Type(TruthValue):defaultValue=2
_VlanVoicePriorityRemark_Type.__name__=_K
_VlanVoicePriorityRemark_Object=MibTableColumn
vlanVoicePriorityRemark=_VlanVoicePriorityRemark_Object((1,3,6,1,4,1,259,10,1,14,89,48,54,2,1,2),_VlanVoicePriorityRemark_Type())
vlanVoicePriorityRemark.setMaxAccess(_F)
if mibBuilder.loadTexts:vlanVoicePriorityRemark.setStatus(_A)
_VlanVoiceRowStatus_Type=RowStatus
_VlanVoiceRowStatus_Object=MibTableColumn
vlanVoiceRowStatus=_VlanVoiceRowStatus_Object((1,3,6,1,4,1,259,10,1,14,89,48,54,2,1,3),_VlanVoiceRowStatus_Type())
vlanVoiceRowStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:vlanVoiceRowStatus.setStatus(_A)
_VlanVoiceOUITable_Object=MibTable
vlanVoiceOUITable=_VlanVoiceOUITable_Object((1,3,6,1,4,1,259,10,1,14,89,48,54,3))
if mibBuilder.loadTexts:vlanVoiceOUITable.setStatus(_A)
_VlanVoiceOUIEntry_Object=MibTableRow
vlanVoiceOUIEntry=_VlanVoiceOUIEntry_Object((1,3,6,1,4,1,259,10,1,14,89,48,54,3,1))
vlanVoiceOUIEntry.setIndexNames((0,_E,_d))
if mibBuilder.loadTexts:vlanVoiceOUIEntry.setStatus(_A)
class _VlanVoiceOUIPrefix_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(3,3));fixedLength=3
_VlanVoiceOUIPrefix_Type.__name__=_J
_VlanVoiceOUIPrefix_Object=MibTableColumn
vlanVoiceOUIPrefix=_VlanVoiceOUIPrefix_Object((1,3,6,1,4,1,259,10,1,14,89,48,54,3,1,1),_VlanVoiceOUIPrefix_Type())
vlanVoiceOUIPrefix.setMaxAccess(_I)
if mibBuilder.loadTexts:vlanVoiceOUIPrefix.setStatus(_A)
class _VlanVoiceOUIDescription_Type(DisplayString):defaultValue=OctetString('');subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_VlanVoiceOUIDescription_Type.__name__=_Q
_VlanVoiceOUIDescription_Object=MibTableColumn
vlanVoiceOUIDescription=_VlanVoiceOUIDescription_Object((1,3,6,1,4,1,259,10,1,14,89,48,54,3,1,2),_VlanVoiceOUIDescription_Type())
vlanVoiceOUIDescription.setMaxAccess(_B)
if mibBuilder.loadTexts:vlanVoiceOUIDescription.setStatus(_A)
_VlanVoiceOUIEntryRowStatus_Type=RowStatus
_VlanVoiceOUIEntryRowStatus_Object=MibTableColumn
vlanVoiceOUIEntryRowStatus=_VlanVoiceOUIEntryRowStatus_Object((1,3,6,1,4,1,259,10,1,14,89,48,54,3,1,3),_VlanVoiceOUIEntryRowStatus_Type())
vlanVoiceOUIEntryRowStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:vlanVoiceOUIEntryRowStatus.setStatus(_A)
_VlanVoicePortTable_Object=MibTable
vlanVoicePortTable=_VlanVoicePortTable_Object((1,3,6,1,4,1,259,10,1,14,89,48,54,4))
if mibBuilder.loadTexts:vlanVoicePortTable.setStatus(_A)
_VlanVoicePortEntry_Object=MibTableRow
vlanVoicePortEntry=_VlanVoicePortEntry_Object((1,3,6,1,4,1,259,10,1,14,89,48,54,4,1))
vlanVoicePortEntry.setIndexNames((0,_G,_H))
if mibBuilder.loadTexts:vlanVoicePortEntry.setStatus(_A)
class _VlanVoicePortEnable_Type(TruthValue):defaultValue=2
_VlanVoicePortEnable_Type.__name__=_K
_VlanVoicePortEnable_Object=MibTableColumn
vlanVoicePortEnable=_VlanVoicePortEnable_Object((1,3,6,1,4,1,259,10,1,14,89,48,54,4,1,1),_VlanVoicePortEnable_Type())
vlanVoicePortEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:vlanVoicePortEnable.setStatus(_A)
class _VlanVoicePortVlanIndex_Type(VlanIndex):defaultValue=4095
_VlanVoicePortVlanIndex_Type.__name__=_L
_VlanVoicePortVlanIndex_Object=MibTableColumn
vlanVoicePortVlanIndex=_VlanVoicePortVlanIndex_Object((1,3,6,1,4,1,259,10,1,14,89,48,54,4,1,2),_VlanVoicePortVlanIndex_Type())
vlanVoicePortVlanIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:vlanVoicePortVlanIndex.setStatus(_A)
class _VlanVoicePortSecure_Type(TruthValue):defaultValue=2
_VlanVoicePortSecure_Type.__name__=_K
_VlanVoicePortSecure_Object=MibTableColumn
vlanVoicePortSecure=_VlanVoicePortSecure_Object((1,3,6,1,4,1,259,10,1,14,89,48,54,4,1,3),_VlanVoicePortSecure_Type())
vlanVoicePortSecure.setMaxAccess(_B)
if mibBuilder.loadTexts:vlanVoicePortSecure.setStatus(_A)
class _VlanVoicePortCurrentMembership_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('active',1),('notActive',2)))
_VlanVoicePortCurrentMembership_Type.__name__=_D
_VlanVoicePortCurrentMembership_Object=MibTableColumn
vlanVoicePortCurrentMembership=_VlanVoicePortCurrentMembership_Object((1,3,6,1,4,1,259,10,1,14,89,48,54,4,1,4),_VlanVoicePortCurrentMembership_Type())
vlanVoicePortCurrentMembership.setMaxAccess(_C)
if mibBuilder.loadTexts:vlanVoicePortCurrentMembership.setStatus(_A)
class _VlanVoicePortQosMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('src',1),('all',2)))
_VlanVoicePortQosMode_Type.__name__=_D
_VlanVoicePortQosMode_Object=MibTableColumn
vlanVoicePortQosMode=_VlanVoicePortQosMode_Object((1,3,6,1,4,1,259,10,1,14,89,48,54,4,1,5),_VlanVoicePortQosMode_Type())
vlanVoicePortQosMode.setMaxAccess(_B)
if mibBuilder.loadTexts:vlanVoicePortQosMode.setStatus(_A)
class _VlanVoiceOUISetToDefault_Type(TruthValue):defaultValue=2
_VlanVoiceOUISetToDefault_Type.__name__=_K
_VlanVoiceOUISetToDefault_Object=MibScalar
vlanVoiceOUISetToDefault=_VlanVoiceOUISetToDefault_Object((1,3,6,1,4,1,259,10,1,14,89,48,54,5),_VlanVoiceOUISetToDefault_Type())
vlanVoiceOUISetToDefault.setMaxAccess(_B)
if mibBuilder.loadTexts:vlanVoiceOUISetToDefault.setStatus(_A)
_VlanDefault_ObjectIdentity=ObjectIdentity
vlanDefault=_VlanDefault_ObjectIdentity((1,3,6,1,4,1,259,10,1,14,89,48,55))
_VlanDefaultTaggedPorts_Type=PortList
_VlanDefaultTaggedPorts_Object=MibScalar
vlanDefaultTaggedPorts=_VlanDefaultTaggedPorts_Object((1,3,6,1,4,1,259,10,1,14,89,48,55,1),_VlanDefaultTaggedPorts_Type())
vlanDefaultTaggedPorts.setMaxAccess(_B)
if mibBuilder.loadTexts:vlanDefaultTaggedPorts.setStatus(_A)
_VlanDefaultEnabledPorts_Type=PortList
_VlanDefaultEnabledPorts_Object=MibScalar
vlanDefaultEnabledPorts=_VlanDefaultEnabledPorts_Object((1,3,6,1,4,1,259,10,1,14,89,48,55,2),_VlanDefaultEnabledPorts_Type())
vlanDefaultEnabledPorts.setMaxAccess(_B)
if mibBuilder.loadTexts:vlanDefaultEnabledPorts.setStatus(_A)
_VlanInetTriplePlayTable_Object=MibTable
vlanInetTriplePlayTable=_VlanInetTriplePlayTable_Object((1,3,6,1,4,1,259,10,1,14,89,48,56))
if mibBuilder.loadTexts:vlanInetTriplePlayTable.setStatus(_A)
_VlanInetTriplePlayEntry_Object=MibTableRow
vlanInetTriplePlayEntry=_VlanInetTriplePlayEntry_Object((1,3,6,1,4,1,259,10,1,14,89,48,56,1))
vlanInetTriplePlayEntry.setIndexNames((0,_E,_e),(0,_E,_R))
if mibBuilder.loadTexts:vlanInetTriplePlayEntry.setStatus(_A)
_VlanInetTriplePlayInetAddressType_Type=InetAddressType
_VlanInetTriplePlayInetAddressType_Object=MibTableColumn
vlanInetTriplePlayInetAddressType=_VlanInetTriplePlayInetAddressType_Object((1,3,6,1,4,1,259,10,1,14,89,48,56,1,1),_VlanInetTriplePlayInetAddressType_Type())
vlanInetTriplePlayInetAddressType.setMaxAccess(_C)
if mibBuilder.loadTexts:vlanInetTriplePlayInetAddressType.setStatus(_A)
_VlanInetTriplePlayInnerVID_Type=VlanIndex
_VlanInetTriplePlayInnerVID_Object=MibTableColumn
vlanInetTriplePlayInnerVID=_VlanInetTriplePlayInnerVID_Object((1,3,6,1,4,1,259,10,1,14,89,48,56,1,2),_VlanInetTriplePlayInnerVID_Type())
vlanInetTriplePlayInnerVID.setMaxAccess(_I)
if mibBuilder.loadTexts:vlanInetTriplePlayInnerVID.setStatus(_A)
_VlanInetTriplePlayMulticastTvVID_Type=VlanIndex
_VlanInetTriplePlayMulticastTvVID_Object=MibTableColumn
vlanInetTriplePlayMulticastTvVID=_VlanInetTriplePlayMulticastTvVID_Object((1,3,6,1,4,1,259,10,1,14,89,48,56,1,3),_VlanInetTriplePlayMulticastTvVID_Type())
vlanInetTriplePlayMulticastTvVID.setMaxAccess(_F)
if mibBuilder.loadTexts:vlanInetTriplePlayMulticastTvVID.setStatus(_A)
_VlanInetTriplePlayRowStatus_Type=RowStatus
_VlanInetTriplePlayRowStatus_Object=MibTableColumn
vlanInetTriplePlayRowStatus=_VlanInetTriplePlayRowStatus_Object((1,3,6,1,4,1,259,10,1,14,89,48,56,1,4),_VlanInetTriplePlayRowStatus_Type())
vlanInetTriplePlayRowStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:vlanInetTriplePlayRowStatus.setStatus(_A)
_VlanInetTriplePlayMulticastTvTable_Object=MibTable
vlanInetTriplePlayMulticastTvTable=_VlanInetTriplePlayMulticastTvTable_Object((1,3,6,1,4,1,259,10,1,14,89,48,57))
if mibBuilder.loadTexts:vlanInetTriplePlayMulticastTvTable.setStatus(_A)
_VlanInetTriplePlayMulticatTvEntry_Object=MibTableRow
vlanInetTriplePlayMulticatTvEntry=_VlanInetTriplePlayMulticatTvEntry_Object((1,3,6,1,4,1,259,10,1,14,89,48,57,1))
vlanInetTriplePlayMulticatTvEntry.setIndexNames((0,_E,_S))
if mibBuilder.loadTexts:vlanInetTriplePlayMulticatTvEntry.setStatus(_A)
_VlanInetTriplePlayMulticastTvMulticastTvVID_Type=VlanIndex
_VlanInetTriplePlayMulticastTvMulticastTvVID_Object=MibTableColumn
vlanInetTriplePlayMulticastTvMulticastTvVID=_VlanInetTriplePlayMulticastTvMulticastTvVID_Object((1,3,6,1,4,1,259,10,1,14,89,48,57,1,1),_VlanInetTriplePlayMulticastTvMulticastTvVID_Type())
vlanInetTriplePlayMulticastTvMulticastTvVID.setMaxAccess(_C)
if mibBuilder.loadTexts:vlanInetTriplePlayMulticastTvMulticastTvVID.setStatus(_A)
_VlanInetTriplePlayMulticastTvMulticastTvPortList_Type=PortList
_VlanInetTriplePlayMulticastTvMulticastTvPortList_Object=MibTableColumn
vlanInetTriplePlayMulticastTvMulticastTvPortList=_VlanInetTriplePlayMulticastTvMulticastTvPortList_Object((1,3,6,1,4,1,259,10,1,14,89,48,57,1,2),_VlanInetTriplePlayMulticastTvMulticastTvPortList_Type())
vlanInetTriplePlayMulticastTvMulticastTvPortList.setMaxAccess(_B)
if mibBuilder.loadTexts:vlanInetTriplePlayMulticastTvMulticastTvPortList.setStatus(_A)
_VlanAsymmetricEnabled_Type=TruthValue
_VlanAsymmetricEnabled_Object=MibScalar
vlanAsymmetricEnabled=_VlanAsymmetricEnabled_Object((1,3,6,1,4,1,259,10,1,14,89,48,58),_VlanAsymmetricEnabled_Type())
vlanAsymmetricEnabled.setMaxAccess(_B)
if mibBuilder.loadTexts:vlanAsymmetricEnabled.setStatus(_A)
_VlanPrivateTable_Object=MibTable
vlanPrivateTable=_VlanPrivateTable_Object((1,3,6,1,4,1,259,10,1,14,89,48,59))
if mibBuilder.loadTexts:vlanPrivateTable.setStatus(_A)
_VlanPrivateEntry_Object=MibTableRow
vlanPrivateEntry=_VlanPrivateEntry_Object((1,3,6,1,4,1,259,10,1,14,89,48,59,1))
vlanPrivateEntry.setIndexNames((0,_E,_f))
if mibBuilder.loadTexts:vlanPrivateEntry.setStatus(_A)
_VlanPrivateVid_Type=VlanIndex
_VlanPrivateVid_Object=MibTableColumn
vlanPrivateVid=_VlanPrivateVid_Object((1,3,6,1,4,1,259,10,1,14,89,48,59,1,1),_VlanPrivateVid_Type())
vlanPrivateVid.setMaxAccess(_I)
if mibBuilder.loadTexts:vlanPrivateVid.setStatus(_A)
class _VlanPrivateType_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('primary',1),('isolated',2),('community',3)))
_VlanPrivateType_Type.__name__=_D
_VlanPrivateType_Object=MibTableColumn
vlanPrivateType=_VlanPrivateType_Object((1,3,6,1,4,1,259,10,1,14,89,48,59,1,2),_VlanPrivateType_Type())
vlanPrivateType.setMaxAccess(_B)
if mibBuilder.loadTexts:vlanPrivateType.setStatus(_A)
_VlanPrivatePrimaryVid_Type=VlanIndex
_VlanPrivatePrimaryVid_Object=MibTableColumn
vlanPrivatePrimaryVid=_VlanPrivatePrimaryVid_Object((1,3,6,1,4,1,259,10,1,14,89,48,59,1,3),_VlanPrivatePrimaryVid_Type())
vlanPrivatePrimaryVid.setMaxAccess(_C)
if mibBuilder.loadTexts:vlanPrivatePrimaryVid.setStatus(_A)
_VlanPrivateStatus_Type=RowStatus
_VlanPrivateStatus_Object=MibTableColumn
vlanPrivateStatus=_VlanPrivateStatus_Object((1,3,6,1,4,1,259,10,1,14,89,48,59,1,4),_VlanPrivateStatus_Type())
vlanPrivateStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:vlanPrivateStatus.setStatus(_A)
_VlanPrivateMapTable_Object=MibTable
vlanPrivateMapTable=_VlanPrivateMapTable_Object((1,3,6,1,4,1,259,10,1,14,89,48,60))
if mibBuilder.loadTexts:vlanPrivateMapTable.setStatus(_A)
_VlanPrivateMapEntry_Object=MibTableRow
vlanPrivateMapEntry=_VlanPrivateMapEntry_Object((1,3,6,1,4,1,259,10,1,14,89,48,60,1))
vlanPrivateMapEntry.setIndexNames((0,_E,_g),(0,_E,_h))
if mibBuilder.loadTexts:vlanPrivateMapEntry.setStatus(_A)
_VlanPrivateMapPrimaryVid_Type=VlanIndex
_VlanPrivateMapPrimaryVid_Object=MibTableColumn
vlanPrivateMapPrimaryVid=_VlanPrivateMapPrimaryVid_Object((1,3,6,1,4,1,259,10,1,14,89,48,60,1,1),_VlanPrivateMapPrimaryVid_Type())
vlanPrivateMapPrimaryVid.setMaxAccess(_I)
if mibBuilder.loadTexts:vlanPrivateMapPrimaryVid.setStatus(_A)
_VlanPrivateMapSecondaryVid_Type=VlanIndex
_VlanPrivateMapSecondaryVid_Object=MibTableColumn
vlanPrivateMapSecondaryVid=_VlanPrivateMapSecondaryVid_Object((1,3,6,1,4,1,259,10,1,14,89,48,60,1,2),_VlanPrivateMapSecondaryVid_Type())
vlanPrivateMapSecondaryVid.setMaxAccess(_I)
if mibBuilder.loadTexts:vlanPrivateMapSecondaryVid.setStatus(_A)
_VlanPrivateMapPrimaryPorts_Type=PortList
_VlanPrivateMapPrimaryPorts_Object=MibTableColumn
vlanPrivateMapPrimaryPorts=_VlanPrivateMapPrimaryPorts_Object((1,3,6,1,4,1,259,10,1,14,89,48,60,1,3),_VlanPrivateMapPrimaryPorts_Type())
vlanPrivateMapPrimaryPorts.setMaxAccess(_B)
if mibBuilder.loadTexts:vlanPrivateMapPrimaryPorts.setStatus(_A)
_VlanPrivateMapSecondaryPorts_Type=PortList
_VlanPrivateMapSecondaryPorts_Object=MibTableColumn
vlanPrivateMapSecondaryPorts=_VlanPrivateMapSecondaryPorts_Object((1,3,6,1,4,1,259,10,1,14,89,48,60,1,4),_VlanPrivateMapSecondaryPorts_Type())
vlanPrivateMapSecondaryPorts.setMaxAccess(_B)
if mibBuilder.loadTexts:vlanPrivateMapSecondaryPorts.setStatus(_A)
_VlanPrivateMapStatus_Type=RowStatus
_VlanPrivateMapStatus_Object=MibTableColumn
vlanPrivateMapStatus=_VlanPrivateMapStatus_Object((1,3,6,1,4,1,259,10,1,14,89,48,60,1,5),_VlanPrivateMapStatus_Type())
vlanPrivateMapStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:vlanPrivateMapStatus.setStatus(_A)
_VlanTrunkPortModeTable_Object=MibTable
vlanTrunkPortModeTable=_VlanTrunkPortModeTable_Object((1,3,6,1,4,1,259,10,1,14,89,48,61))
if mibBuilder.loadTexts:vlanTrunkPortModeTable.setStatus(_A)
_VlanTrunkPortModeEntry_Object=MibTableRow
vlanTrunkPortModeEntry=_VlanTrunkPortModeEntry_Object((1,3,6,1,4,1,259,10,1,14,89,48,61,1))
vlanTrunkPortModeEntry.setIndexNames((0,_G,_H))
if mibBuilder.loadTexts:vlanTrunkPortModeEntry.setStatus(_A)
class _VlanTrunkPortModeNativeVlanId_Type(VlanIndex):defaultValue=0
_VlanTrunkPortModeNativeVlanId_Type.__name__=_L
_VlanTrunkPortModeNativeVlanId_Object=MibTableColumn
vlanTrunkPortModeNativeVlanId=_VlanTrunkPortModeNativeVlanId_Object((1,3,6,1,4,1,259,10,1,14,89,48,61,1,1),_VlanTrunkPortModeNativeVlanId_Type())
vlanTrunkPortModeNativeVlanId.setMaxAccess(_B)
if mibBuilder.loadTexts:vlanTrunkPortModeNativeVlanId.setStatus(_A)
class _VlanTrunkModeList1to1024_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,128))
_VlanTrunkModeList1to1024_Type.__name__=_J
_VlanTrunkModeList1to1024_Object=MibTableColumn
vlanTrunkModeList1to1024=_VlanTrunkModeList1to1024_Object((1,3,6,1,4,1,259,10,1,14,89,48,61,1,2),_VlanTrunkModeList1to1024_Type())
vlanTrunkModeList1to1024.setMaxAccess(_B)
if mibBuilder.loadTexts:vlanTrunkModeList1to1024.setStatus(_A)
class _VlanTrunkModeList1025to2048_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,128))
_VlanTrunkModeList1025to2048_Type.__name__=_J
_VlanTrunkModeList1025to2048_Object=MibTableColumn
vlanTrunkModeList1025to2048=_VlanTrunkModeList1025to2048_Object((1,3,6,1,4,1,259,10,1,14,89,48,61,1,3),_VlanTrunkModeList1025to2048_Type())
vlanTrunkModeList1025to2048.setMaxAccess(_B)
if mibBuilder.loadTexts:vlanTrunkModeList1025to2048.setStatus(_A)
class _VlanTrunkModeList2049to3072_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,128))
_VlanTrunkModeList2049to3072_Type.__name__=_J
_VlanTrunkModeList2049to3072_Object=MibTableColumn
vlanTrunkModeList2049to3072=_VlanTrunkModeList2049to3072_Object((1,3,6,1,4,1,259,10,1,14,89,48,61,1,4),_VlanTrunkModeList2049to3072_Type())
vlanTrunkModeList2049to3072.setMaxAccess(_B)
if mibBuilder.loadTexts:vlanTrunkModeList2049to3072.setStatus(_A)
class _VlanTrunkModeList3073to4094_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,128))
_VlanTrunkModeList3073to4094_Type.__name__=_J
_VlanTrunkModeList3073to4094_Object=MibTableColumn
vlanTrunkModeList3073to4094=_VlanTrunkModeList3073to4094_Object((1,3,6,1,4,1,259,10,1,14,89,48,61,1,5),_VlanTrunkModeList3073to4094_Type())
vlanTrunkModeList3073to4094.setMaxAccess(_B)
if mibBuilder.loadTexts:vlanTrunkModeList3073to4094.setStatus(_A)
_VlanAccessPortModeTable_Object=MibTable
vlanAccessPortModeTable=_VlanAccessPortModeTable_Object((1,3,6,1,4,1,259,10,1,14,89,48,62))
if mibBuilder.loadTexts:vlanAccessPortModeTable.setStatus(_A)
_VlanAccessPortModeEntry_Object=MibTableRow
vlanAccessPortModeEntry=_VlanAccessPortModeEntry_Object((1,3,6,1,4,1,259,10,1,14,89,48,62,1))
vlanAccessPortModeEntry.setIndexNames((0,_G,_H))
if mibBuilder.loadTexts:vlanAccessPortModeEntry.setStatus(_A)
class _VlanAccessPortModeVlanId_Type(VlanIndex):defaultValue=0
_VlanAccessPortModeVlanId_Type.__name__=_L
_VlanAccessPortModeVlanId_Object=MibTableColumn
vlanAccessPortModeVlanId=_VlanAccessPortModeVlanId_Object((1,3,6,1,4,1,259,10,1,14,89,48,62,1,1),_VlanAccessPortModeVlanId_Type())
vlanAccessPortModeVlanId.setMaxAccess(_B)
if mibBuilder.loadTexts:vlanAccessPortModeVlanId.setStatus(_A)
_VlanAccessPortModeMcstTvVlanId_Type=VlanIndex
_VlanAccessPortModeMcstTvVlanId_Object=MibTableColumn
vlanAccessPortModeMcstTvVlanId=_VlanAccessPortModeMcstTvVlanId_Object((1,3,6,1,4,1,259,10,1,14,89,48,62,1,2),_VlanAccessPortModeMcstTvVlanId_Type())
vlanAccessPortModeMcstTvVlanId.setMaxAccess(_B)
if mibBuilder.loadTexts:vlanAccessPortModeMcstTvVlanId.setStatus(_A)
_VlanCustomerPortModeTable_Object=MibTable
vlanCustomerPortModeTable=_VlanCustomerPortModeTable_Object((1,3,6,1,4,1,259,10,1,14,89,48,63))
if mibBuilder.loadTexts:vlanCustomerPortModeTable.setStatus(_A)
_VlanCustomerPortModeEntry_Object=MibTableRow
vlanCustomerPortModeEntry=_VlanCustomerPortModeEntry_Object((1,3,6,1,4,1,259,10,1,14,89,48,63,1))
vlanCustomerPortModeEntry.setIndexNames((0,_G,_H))
if mibBuilder.loadTexts:vlanCustomerPortModeEntry.setStatus(_A)
class _VlanCustomerPortModeVlanId_Type(VlanIndex):defaultValue=0
_VlanCustomerPortModeVlanId_Type.__name__=_L
_VlanCustomerPortModeVlanId_Object=MibTableColumn
vlanCustomerPortModeVlanId=_VlanCustomerPortModeVlanId_Object((1,3,6,1,4,1,259,10,1,14,89,48,63,1,1),_VlanCustomerPortModeVlanId_Type())
vlanCustomerPortModeVlanId.setMaxAccess(_B)
if mibBuilder.loadTexts:vlanCustomerPortModeVlanId.setStatus(_A)
class _VlanCustomerPortModeMtvList1to1024_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,128))
_VlanCustomerPortModeMtvList1to1024_Type.__name__=_J
_VlanCustomerPortModeMtvList1to1024_Object=MibTableColumn
vlanCustomerPortModeMtvList1to1024=_VlanCustomerPortModeMtvList1to1024_Object((1,3,6,1,4,1,259,10,1,14,89,48,63,1,2),_VlanCustomerPortModeMtvList1to1024_Type())
vlanCustomerPortModeMtvList1to1024.setMaxAccess(_C)
if mibBuilder.loadTexts:vlanCustomerPortModeMtvList1to1024.setStatus(_A)
class _VlanCustomerPortModeMtvList1025to2048_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,128))
_VlanCustomerPortModeMtvList1025to2048_Type.__name__=_J
_VlanCustomerPortModeMtvList1025to2048_Object=MibTableColumn
vlanCustomerPortModeMtvList1025to2048=_VlanCustomerPortModeMtvList1025to2048_Object((1,3,6,1,4,1,259,10,1,14,89,48,63,1,3),_VlanCustomerPortModeMtvList1025to2048_Type())
vlanCustomerPortModeMtvList1025to2048.setMaxAccess(_C)
if mibBuilder.loadTexts:vlanCustomerPortModeMtvList1025to2048.setStatus(_A)
class _VlanCustomerPortModeMtvList2049to3072_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,128))
_VlanCustomerPortModeMtvList2049to3072_Type.__name__=_J
_VlanCustomerPortModeMtvList2049to3072_Object=MibTableColumn
vlanCustomerPortModeMtvList2049to3072=_VlanCustomerPortModeMtvList2049to3072_Object((1,3,6,1,4,1,259,10,1,14,89,48,63,1,4),_VlanCustomerPortModeMtvList2049to3072_Type())
vlanCustomerPortModeMtvList2049to3072.setMaxAccess(_C)
if mibBuilder.loadTexts:vlanCustomerPortModeMtvList2049to3072.setStatus(_A)
class _VlanCustomerPortModeMtvList3073to4094_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,128))
_VlanCustomerPortModeMtvList3073to4094_Type.__name__=_J
_VlanCustomerPortModeMtvList3073to4094_Object=MibTableColumn
vlanCustomerPortModeMtvList3073to4094=_VlanCustomerPortModeMtvList3073to4094_Object((1,3,6,1,4,1,259,10,1,14,89,48,63,1,5),_VlanCustomerPortModeMtvList3073to4094_Type())
vlanCustomerPortModeMtvList3073to4094.setMaxAccess(_C)
if mibBuilder.loadTexts:vlanCustomerPortModeMtvList3073to4094.setStatus(_A)
_VlanSwitchPortModeTable_Object=MibTable
vlanSwitchPortModeTable=_VlanSwitchPortModeTable_Object((1,3,6,1,4,1,259,10,1,14,89,48,64))
if mibBuilder.loadTexts:vlanSwitchPortModeTable.setStatus(_A)
_VlanSwitchPortModeEntry_Object=MibTableRow
vlanSwitchPortModeEntry=_VlanSwitchPortModeEntry_Object((1,3,6,1,4,1,259,10,1,14,89,48,64,1))
vlanSwitchPortModeEntry.setIndexNames((0,_G,_H))
if mibBuilder.loadTexts:vlanSwitchPortModeEntry.setStatus(_A)
class _VlanSwitchPortModeCategory_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('l2',1),('l3',2)))
_VlanSwitchPortModeCategory_Type.__name__=_D
_VlanSwitchPortModeCategory_Object=MibTableColumn
vlanSwitchPortModeCategory=_VlanSwitchPortModeCategory_Object((1,3,6,1,4,1,259,10,1,14,89,48,64,1,1),_VlanSwitchPortModeCategory_Type())
vlanSwitchPortModeCategory.setMaxAccess(_B)
if mibBuilder.loadTexts:vlanSwitchPortModeCategory.setStatus(_A)
_VlanPortModeContextTable_Object=MibTable
vlanPortModeContextTable=_VlanPortModeContextTable_Object((1,3,6,1,4,1,259,10,1,14,89,48,65))
if mibBuilder.loadTexts:vlanPortModeContextTable.setStatus(_A)
_VlanPortModeContextEntry_Object=MibTableRow
vlanPortModeContextEntry=_VlanPortModeContextEntry_Object((1,3,6,1,4,1,259,10,1,14,89,48,65,1))
vlanPortModeContextEntry.setIndexNames((0,_G,_H))
if mibBuilder.loadTexts:vlanPortModeContextEntry.setStatus(_A)
_VlanPortModeContextValue_Type=Integer32
_VlanPortModeContextValue_Object=MibTableColumn
vlanPortModeContextValue=_VlanPortModeContextValue_Object((1,3,6,1,4,1,259,10,1,14,89,48,65,1,1),_VlanPortModeContextValue_Type())
vlanPortModeContextValue.setMaxAccess(_B)
if mibBuilder.loadTexts:vlanPortModeContextValue.setStatus(_A)
mibBuilder.exportSymbols(_E,**{'vlan':vlan,'vlanMibVersion':vlanMibVersion,'vlanMaxTableNumber':vlanMaxTableNumber,'vlanNameTable':vlanNameTable,'vlanNameEntry':vlanNameEntry,_T:vlanNameName,'vlanNameTag':vlanNameTag,'vlanNameIfIndex':vlanNameIfIndex,'vlanPortModeTable':vlanPortModeTable,'vlanPortModeEntry':vlanPortModeEntry,'vlanPortModeState':vlanPortModeState,'vlanSendUnknownToAllPorts':vlanSendUnknownToAllPorts,'vlanDefaultSupported':vlanDefaultSupported,'vlanDot1vSupported':vlanDot1vSupported,'vlanDefaultEnabled':vlanDefaultEnabled,'vlanSpecialTagTable':vlanSpecialTagTable,'vlanSpecialTagEntry':vlanSpecialTagEntry,'vlanSpecialTagVID':vlanSpecialTagVID,'vlanSpecialTagStatus':vlanSpecialTagStatus,'vlanSpecialTagCurrentTable':vlanSpecialTagCurrentTable,'vlanSpecialTagCurrentEntry':vlanSpecialTagCurrentEntry,'vlanSpecialTagCurrentVID':vlanSpecialTagCurrentVID,'vlanSpecialTagCurrentReserved':vlanSpecialTagCurrentReserved,'vlanSpecialTagCurrentActive':vlanSpecialTagCurrentActive,'vlanPrivateEdgeSupported':vlanPrivateEdgeSupported,'vlanPrivateEdgeVersion':vlanPrivateEdgeVersion,'vlanPrivateEdgeTable':vlanPrivateEdgeTable,'vlanPrivateEdgeEntry':vlanPrivateEdgeEntry,'vlanPrivateEdgeUplink':vlanPrivateEdgeUplink,'vlanPrivateEdgeStatus':vlanPrivateEdgeStatus,'vlanDynamicVlanSupported':vlanDynamicVlanSupported,'vlanDynamicVlanTable':vlanDynamicVlanTable,'vlanDynamicVlanEntry':vlanDynamicVlanEntry,_U:vlanDynamicVlanMacAddress,'vlanDynamicVlanTag':vlanDynamicVlanTag,'vlanDynamicVlanStatus':vlanDynamicVlanStatus,'vlanPortModeExtTable':vlanPortModeExtTable,'vlanPortModeExtEntry':vlanPortModeExtEntry,'vlanPortModeExtState':vlanPortModeExtState,'vlanPortModeExtStatus':vlanPortModeExtStatus,'vlanPrivateSupported':vlanPrivateSupported,'vlanPrivateTableOld':vlanPrivateTableOld,'vlanPrivateEntryOld':vlanPrivateEntryOld,'vlanPrivateOldIsolatedVlanTag':vlanPrivateOldIsolatedVlanTag,'vlanPrivateOldStatus':vlanPrivateOldStatus,'vlanPrivateCommunityTable':vlanPrivateCommunityTable,'vlanPrivateCommunityEntry':vlanPrivateCommunityEntry,_V:vlanPrivateCommunityVlanTag,'vlanPrivateCommunityStatus':vlanPrivateCommunityStatus,'vlanMulticastTvTable':vlanMulticastTvTable,'vlanMulticastTvEntry':vlanMulticastTvEntry,'vlanMulticastTvVID':vlanMulticastTvVID,'vlanMulticastTvStatus':vlanMulticastTvStatus,'vlanMacBaseVlanGroupTable':vlanMacBaseVlanGroupTable,'vlanMacBaseVlanGroupEntry':vlanMacBaseVlanGroupEntry,_W:vlanMacBaseVlanMacAddress,_X:vlanMacBaseVlanMacMask,'vlanMacBaseVlanGroupId':vlanMacBaseVlanGroupId,'vlanMacBaseVlanGroupRowStatus':vlanMacBaseVlanGroupRowStatus,'vlanMacBaseVlanPortTable':vlanMacBaseVlanPortTable,'vlanMacBaseVlanPortEntry':vlanMacBaseVlanPortEntry,_Y:vlanMacBaseVlanPortGroupId,'vlanMacBaseVlanPortGroupVid':vlanMacBaseVlanPortGroupVid,'vlanMacBaseVlanPortRowStatus':vlanMacBaseVlanPortRowStatus,'vlanPrivateEdgeGroupTable':vlanPrivateEdgeGroupTable,'vlanPrivateEdgeGroupEntry':vlanPrivateEdgeGroupEntry,_Z:vlanPrivateEdgeGroupSource,'vlanPrivateEdgeGroupUplink':vlanPrivateEdgeGroupUplink,'vlanPrivateEdgeGroupStatus':vlanPrivateEdgeGroupStatus,'vlanPrivateEdgeGroupIfIndexTable':vlanPrivateEdgeGroupIfIndexTable,'vlanPrivateEdgeGroupIfIndexEntry':vlanPrivateEdgeGroupIfIndexEntry,'vlanPrivateEdgeGroupIfIndexID':vlanPrivateEdgeGroupIfIndexID,'vlanPrivateEdgeGroupIfIndexDomainID':vlanPrivateEdgeGroupIfIndexDomainID,'vlanSubnetRangeTable':vlanSubnetRangeTable,'vlanSubnetRangeEntry':vlanSubnetRangeEntry,_a:vlanSubnetRangeAddr,_b:vlanSubnetRangeMask,'vlanSubnetRangeGroupId':vlanSubnetRangeGroupId,'vlanSubnetRangeRowStatus':vlanSubnetRangeRowStatus,'vlanSubnetPortTable':vlanSubnetPortTable,'vlanSubnetPortEntry':vlanSubnetPortEntry,_c:vlanSubnetPortGroupId,'vlanSubnetPortGroupVid':vlanSubnetPortGroupVid,'vlanSubnetPortRowStatus':vlanSubnetPortRowStatus,'vlanTriplePlayTable':vlanTriplePlayTable,'vlanTriplePlayEntry':vlanTriplePlayEntry,_R:vlanTriplePlayInnerVID,'vlanTriplePlayMulticastTvVID':vlanTriplePlayMulticastTvVID,'vlanTriplePlayRowStatus':vlanTriplePlayRowStatus,'vlanTriplePlayMulticastTvTable':vlanTriplePlayMulticastTvTable,'vlanTriplePlayMulticatTvEntry':vlanTriplePlayMulticatTvEntry,_S:vlanTriplePlayMulticastTvMulticastTvVID,'vlanTriplePlayMulticastTvMulticastTvPortList':vlanTriplePlayMulticastTvMulticastTvPortList,'vlanDefaultExtManagment':vlanDefaultExtManagment,'vlanVoice':vlanVoice,'vlanVoiceAgingTimeout':vlanVoiceAgingTimeout,'vlanVoiceTable':vlanVoiceTable,'vlanVoiceEntry':vlanVoiceEntry,'vlanVoicePriority':vlanVoicePriority,'vlanVoicePriorityRemark':vlanVoicePriorityRemark,'vlanVoiceRowStatus':vlanVoiceRowStatus,'vlanVoiceOUITable':vlanVoiceOUITable,'vlanVoiceOUIEntry':vlanVoiceOUIEntry,_d:vlanVoiceOUIPrefix,'vlanVoiceOUIDescription':vlanVoiceOUIDescription,'vlanVoiceOUIEntryRowStatus':vlanVoiceOUIEntryRowStatus,'vlanVoicePortTable':vlanVoicePortTable,'vlanVoicePortEntry':vlanVoicePortEntry,'vlanVoicePortEnable':vlanVoicePortEnable,'vlanVoicePortVlanIndex':vlanVoicePortVlanIndex,'vlanVoicePortSecure':vlanVoicePortSecure,'vlanVoicePortCurrentMembership':vlanVoicePortCurrentMembership,'vlanVoicePortQosMode':vlanVoicePortQosMode,'vlanVoiceOUISetToDefault':vlanVoiceOUISetToDefault,'vlanDefault':vlanDefault,'vlanDefaultTaggedPorts':vlanDefaultTaggedPorts,'vlanDefaultEnabledPorts':vlanDefaultEnabledPorts,'vlanInetTriplePlayTable':vlanInetTriplePlayTable,'vlanInetTriplePlayEntry':vlanInetTriplePlayEntry,_e:vlanInetTriplePlayInetAddressType,'vlanInetTriplePlayInnerVID':vlanInetTriplePlayInnerVID,'vlanInetTriplePlayMulticastTvVID':vlanInetTriplePlayMulticastTvVID,'vlanInetTriplePlayRowStatus':vlanInetTriplePlayRowStatus,'vlanInetTriplePlayMulticastTvTable':vlanInetTriplePlayMulticastTvTable,'vlanInetTriplePlayMulticatTvEntry':vlanInetTriplePlayMulticatTvEntry,'vlanInetTriplePlayMulticastTvMulticastTvVID':vlanInetTriplePlayMulticastTvMulticastTvVID,'vlanInetTriplePlayMulticastTvMulticastTvPortList':vlanInetTriplePlayMulticastTvMulticastTvPortList,'vlanAsymmetricEnabled':vlanAsymmetricEnabled,'vlanPrivateTable':vlanPrivateTable,'vlanPrivateEntry':vlanPrivateEntry,_f:vlanPrivateVid,'vlanPrivateType':vlanPrivateType,'vlanPrivatePrimaryVid':vlanPrivatePrimaryVid,'vlanPrivateStatus':vlanPrivateStatus,'vlanPrivateMapTable':vlanPrivateMapTable,'vlanPrivateMapEntry':vlanPrivateMapEntry,_g:vlanPrivateMapPrimaryVid,_h:vlanPrivateMapSecondaryVid,'vlanPrivateMapPrimaryPorts':vlanPrivateMapPrimaryPorts,'vlanPrivateMapSecondaryPorts':vlanPrivateMapSecondaryPorts,'vlanPrivateMapStatus':vlanPrivateMapStatus,'vlanTrunkPortModeTable':vlanTrunkPortModeTable,'vlanTrunkPortModeEntry':vlanTrunkPortModeEntry,'vlanTrunkPortModeNativeVlanId':vlanTrunkPortModeNativeVlanId,'vlanTrunkModeList1to1024':vlanTrunkModeList1to1024,'vlanTrunkModeList1025to2048':vlanTrunkModeList1025to2048,'vlanTrunkModeList2049to3072':vlanTrunkModeList2049to3072,'vlanTrunkModeList3073to4094':vlanTrunkModeList3073to4094,'vlanAccessPortModeTable':vlanAccessPortModeTable,'vlanAccessPortModeEntry':vlanAccessPortModeEntry,'vlanAccessPortModeVlanId':vlanAccessPortModeVlanId,'vlanAccessPortModeMcstTvVlanId':vlanAccessPortModeMcstTvVlanId,'vlanCustomerPortModeTable':vlanCustomerPortModeTable,'vlanCustomerPortModeEntry':vlanCustomerPortModeEntry,'vlanCustomerPortModeVlanId':vlanCustomerPortModeVlanId,'vlanCustomerPortModeMtvList1to1024':vlanCustomerPortModeMtvList1to1024,'vlanCustomerPortModeMtvList1025to2048':vlanCustomerPortModeMtvList1025to2048,'vlanCustomerPortModeMtvList2049to3072':vlanCustomerPortModeMtvList2049to3072,'vlanCustomerPortModeMtvList3073to4094':vlanCustomerPortModeMtvList3073to4094,'vlanSwitchPortModeTable':vlanSwitchPortModeTable,'vlanSwitchPortModeEntry':vlanSwitchPortModeEntry,'vlanSwitchPortModeCategory':vlanSwitchPortModeCategory,'vlanPortModeContextTable':vlanPortModeContextTable,'vlanPortModeContextEntry':vlanPortModeContextEntry,'vlanPortModeContextValue':vlanPortModeContextValue})