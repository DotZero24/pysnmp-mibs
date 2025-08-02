_Z='fsWssUserUsedTime'
_Y='fsWssUserUsedVolume'
_X='accessible-for-notify'
_W='fsWssUserStaMac'
_V='fsWssUserName'
_U='fsWssUserMappingStaMac'
_T='fsWssUserMappingName'
_S='fsWssUserMacAccessListStaMac'
_R='fsWssUserNameAccessListUserName'
_Q='fsWssUserRoleWlanIndex'
_P='fsWssUserRoleName'
_O='fsWssUserGroupId'
_N='disable'
_M='enable'
_L='fsWssUserStationMacAddress'
_K='fsWssNtfUserName'
_J='fsWssUserWlanIndex'
_I='Integer32'
_H='OctetString'
_G='read-create'
_F='read-only'
_E='not-accessible'
_D='read-write'
_C='ARICENT-WSSUSERMGM-MIB'
_B='Unsigned32'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_H,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_I,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_B,'enterprises','iso')
DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress','RowStatus','TextualConvention')
fsWssUser=ModuleIdentity((1,3,6,1,4,1,29601,2,90))
if mibBuilder.loadTexts:fsWssUser.setRevisions(('2014-09-15 00:00',))
class FsWssUserStationMac(TextualConvention,OctetString):status=_A;displayHint='1x:';subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(6,6),ValueSizeConstraint(8,8))
class FsWssUserIdName(TextualConvention,OctetString):status=_A;displayHint='1x:';subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_FsWssUserScalars_ObjectIdentity=ObjectIdentity
fsWssUserScalars=_FsWssUserScalars_ObjectIdentity((1,3,6,1,4,1,29601,2,90,1))
class _FsWssUserRoleStatus_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_M,1),(_N,2)))
_FsWssUserRoleStatus_Type.__name__=_I
_FsWssUserRoleStatus_Object=MibScalar
fsWssUserRoleStatus=_FsWssUserRoleStatus_Object((1,3,6,1,4,1,29601,2,90,1,1),_FsWssUserRoleStatus_Type())
fsWssUserRoleStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:fsWssUserRoleStatus.setStatus(_A)
class _FsWssUserBlockedCount_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_FsWssUserBlockedCount_Type.__name__=_B
_FsWssUserBlockedCount_Object=MibScalar
fsWssUserBlockedCount=_FsWssUserBlockedCount_Object((1,3,6,1,4,1,29601,2,90,1,2),_FsWssUserBlockedCount_Type())
fsWssUserBlockedCount.setMaxAccess(_D)
if mibBuilder.loadTexts:fsWssUserBlockedCount.setStatus(_A)
class _FsWssUserLoggedCount_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_FsWssUserLoggedCount_Type.__name__=_B
_FsWssUserLoggedCount_Object=MibScalar
fsWssUserLoggedCount=_FsWssUserLoggedCount_Object((1,3,6,1,4,1,29601,2,90,1,3),_FsWssUserLoggedCount_Type())
fsWssUserLoggedCount.setMaxAccess(_D)
if mibBuilder.loadTexts:fsWssUserLoggedCount.setStatus(_A)
class _FsWssUserTraceOption_Type(Integer32):defaultValue=0
_FsWssUserTraceOption_Type.__name__=_I
_FsWssUserTraceOption_Object=MibScalar
fsWssUserTraceOption=_FsWssUserTraceOption_Object((1,3,6,1,4,1,29601,2,90,1,4),_FsWssUserTraceOption_Type())
fsWssUserTraceOption.setMaxAccess(_D)
if mibBuilder.loadTexts:fsWssUserTraceOption.setStatus(_A)
class _FsWssUserRoleTrapStatus_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_M,1),(_N,2)))
_FsWssUserRoleTrapStatus_Type.__name__=_I
_FsWssUserRoleTrapStatus_Object=MibScalar
fsWssUserRoleTrapStatus=_FsWssUserRoleTrapStatus_Object((1,3,6,1,4,1,29601,2,90,1,5),_FsWssUserRoleTrapStatus_Type())
fsWssUserRoleTrapStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:fsWssUserRoleTrapStatus.setStatus(_A)
_FsWssUserRole_ObjectIdentity=ObjectIdentity
fsWssUserRole=_FsWssUserRole_ObjectIdentity((1,3,6,1,4,1,29601,2,90,2))
_FsWssUserGroupTable_Object=MibTable
fsWssUserGroupTable=_FsWssUserGroupTable_Object((1,3,6,1,4,1,29601,2,90,2,1))
if mibBuilder.loadTexts:fsWssUserGroupTable.setStatus(_A)
_FsWssUserGroupEntry_Object=MibTableRow
fsWssUserGroupEntry=_FsWssUserGroupEntry_Object((1,3,6,1,4,1,29601,2,90,2,1,1))
fsWssUserGroupEntry.setIndexNames((0,_C,_O))
if mibBuilder.loadTexts:fsWssUserGroupEntry.setStatus(_A)
class _FsWssUserGroupId_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1024))
_FsWssUserGroupId_Type.__name__=_B
_FsWssUserGroupId_Object=MibTableColumn
fsWssUserGroupId=_FsWssUserGroupId_Object((1,3,6,1,4,1,29601,2,90,2,1,1,1),_FsWssUserGroupId_Type())
fsWssUserGroupId.setMaxAccess(_E)
if mibBuilder.loadTexts:fsWssUserGroupId.setStatus(_A)
_FsWssUserGroupName_Type=OctetString
_FsWssUserGroupName_Object=MibTableColumn
fsWssUserGroupName=_FsWssUserGroupName_Object((1,3,6,1,4,1,29601,2,90,2,1,1,2),_FsWssUserGroupName_Type())
fsWssUserGroupName.setMaxAccess(_D)
if mibBuilder.loadTexts:fsWssUserGroupName.setStatus(_A)
class _FsWssUserGroupBandWidth_Type(Unsigned32):defaultValue=256;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_FsWssUserGroupBandWidth_Type.__name__=_B
_FsWssUserGroupBandWidth_Object=MibTableColumn
fsWssUserGroupBandWidth=_FsWssUserGroupBandWidth_Object((1,3,6,1,4,1,29601,2,90,2,1,1,3),_FsWssUserGroupBandWidth_Type())
fsWssUserGroupBandWidth.setMaxAccess(_D)
if mibBuilder.loadTexts:fsWssUserGroupBandWidth.setStatus(_A)
class _FsWssUserGroupVolume_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_FsWssUserGroupVolume_Type.__name__=_B
_FsWssUserGroupVolume_Object=MibTableColumn
fsWssUserGroupVolume=_FsWssUserGroupVolume_Object((1,3,6,1,4,1,29601,2,90,2,1,1,4),_FsWssUserGroupVolume_Type())
fsWssUserGroupVolume.setMaxAccess(_D)
if mibBuilder.loadTexts:fsWssUserGroupVolume.setStatus(_A)
class _FsWssUserGroupTime_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,31536000))
_FsWssUserGroupTime_Type.__name__=_B
_FsWssUserGroupTime_Object=MibTableColumn
fsWssUserGroupTime=_FsWssUserGroupTime_Object((1,3,6,1,4,1,29601,2,90,2,1,1,5),_FsWssUserGroupTime_Type())
fsWssUserGroupTime.setMaxAccess(_D)
if mibBuilder.loadTexts:fsWssUserGroupTime.setStatus(_A)
_FsWssUserGroupRowStatus_Type=RowStatus
_FsWssUserGroupRowStatus_Object=MibTableColumn
fsWssUserGroupRowStatus=_FsWssUserGroupRowStatus_Object((1,3,6,1,4,1,29601,2,90,2,1,1,6),_FsWssUserGroupRowStatus_Type())
fsWssUserGroupRowStatus.setMaxAccess(_G)
if mibBuilder.loadTexts:fsWssUserGroupRowStatus.setStatus(_A)
class _FsWssUserGroupDLBandWidth_Type(Unsigned32):defaultValue=256;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_FsWssUserGroupDLBandWidth_Type.__name__=_B
_FsWssUserGroupDLBandWidth_Object=MibTableColumn
fsWssUserGroupDLBandWidth=_FsWssUserGroupDLBandWidth_Object((1,3,6,1,4,1,29601,2,90,2,1,1,7),_FsWssUserGroupDLBandWidth_Type())
fsWssUserGroupDLBandWidth.setMaxAccess(_D)
if mibBuilder.loadTexts:fsWssUserGroupDLBandWidth.setStatus(_A)
class _FsWssUserGroupULBandWidth_Type(Unsigned32):defaultValue=256;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_FsWssUserGroupULBandWidth_Type.__name__=_B
_FsWssUserGroupULBandWidth_Object=MibTableColumn
fsWssUserGroupULBandWidth=_FsWssUserGroupULBandWidth_Object((1,3,6,1,4,1,29601,2,90,2,1,1,8),_FsWssUserGroupULBandWidth_Type())
fsWssUserGroupULBandWidth.setMaxAccess(_D)
if mibBuilder.loadTexts:fsWssUserGroupULBandWidth.setStatus(_A)
_FsWssUserRoleTable_Object=MibTable
fsWssUserRoleTable=_FsWssUserRoleTable_Object((1,3,6,1,4,1,29601,2,90,2,2))
if mibBuilder.loadTexts:fsWssUserRoleTable.setStatus(_A)
_FsWssUserRoleEntry_Object=MibTableRow
fsWssUserRoleEntry=_FsWssUserRoleEntry_Object((1,3,6,1,4,1,29601,2,90,2,2,1))
fsWssUserRoleEntry.setIndexNames((0,_C,_P),(0,_C,_Q))
if mibBuilder.loadTexts:fsWssUserRoleEntry.setStatus(_A)
class _FsWssUserRoleName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_FsWssUserRoleName_Type.__name__=_H
_FsWssUserRoleName_Object=MibTableColumn
fsWssUserRoleName=_FsWssUserRoleName_Object((1,3,6,1,4,1,29601,2,90,2,2,1,1),_FsWssUserRoleName_Type())
fsWssUserRoleName.setMaxAccess(_E)
if mibBuilder.loadTexts:fsWssUserRoleName.setStatus(_A)
class _FsWssUserRoleWlanIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,512))
_FsWssUserRoleWlanIndex_Type.__name__=_B
_FsWssUserRoleWlanIndex_Object=MibTableColumn
fsWssUserRoleWlanIndex=_FsWssUserRoleWlanIndex_Object((1,3,6,1,4,1,29601,2,90,2,2,1,2),_FsWssUserRoleWlanIndex_Type())
fsWssUserRoleWlanIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:fsWssUserRoleWlanIndex.setStatus(_A)
class _FsWssUserRoleGroupId_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1024))
_FsWssUserRoleGroupId_Type.__name__=_B
_FsWssUserRoleGroupId_Object=MibTableColumn
fsWssUserRoleGroupId=_FsWssUserRoleGroupId_Object((1,3,6,1,4,1,29601,2,90,2,2,1,3),_FsWssUserRoleGroupId_Type())
fsWssUserRoleGroupId.setMaxAccess(_D)
if mibBuilder.loadTexts:fsWssUserRoleGroupId.setStatus(_A)
_FsWssUserRoleRowStatus_Type=RowStatus
_FsWssUserRoleRowStatus_Object=MibTableColumn
fsWssUserRoleRowStatus=_FsWssUserRoleRowStatus_Object((1,3,6,1,4,1,29601,2,90,2,2,1,4),_FsWssUserRoleRowStatus_Type())
fsWssUserRoleRowStatus.setMaxAccess(_G)
if mibBuilder.loadTexts:fsWssUserRoleRowStatus.setStatus(_A)
_FsWssUserNameAccessListTable_Object=MibTable
fsWssUserNameAccessListTable=_FsWssUserNameAccessListTable_Object((1,3,6,1,4,1,29601,2,90,2,3))
if mibBuilder.loadTexts:fsWssUserNameAccessListTable.setStatus(_A)
_FsWssUserNameAccessListEntry_Object=MibTableRow
fsWssUserNameAccessListEntry=_FsWssUserNameAccessListEntry_Object((1,3,6,1,4,1,29601,2,90,2,3,1))
fsWssUserNameAccessListEntry.setIndexNames((0,_C,_R))
if mibBuilder.loadTexts:fsWssUserNameAccessListEntry.setStatus(_A)
class _FsWssUserNameAccessListUserName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_FsWssUserNameAccessListUserName_Type.__name__=_H
_FsWssUserNameAccessListUserName_Object=MibTableColumn
fsWssUserNameAccessListUserName=_FsWssUserNameAccessListUserName_Object((1,3,6,1,4,1,29601,2,90,2,3,1,1),_FsWssUserNameAccessListUserName_Type())
fsWssUserNameAccessListUserName.setMaxAccess(_E)
if mibBuilder.loadTexts:fsWssUserNameAccessListUserName.setStatus(_A)
_FsWssUserNameAccessListRowStatus_Type=RowStatus
_FsWssUserNameAccessListRowStatus_Object=MibTableColumn
fsWssUserNameAccessListRowStatus=_FsWssUserNameAccessListRowStatus_Object((1,3,6,1,4,1,29601,2,90,2,3,1,2),_FsWssUserNameAccessListRowStatus_Type())
fsWssUserNameAccessListRowStatus.setMaxAccess(_G)
if mibBuilder.loadTexts:fsWssUserNameAccessListRowStatus.setStatus(_A)
_FsWssUserMacAccessListTable_Object=MibTable
fsWssUserMacAccessListTable=_FsWssUserMacAccessListTable_Object((1,3,6,1,4,1,29601,2,90,2,4))
if mibBuilder.loadTexts:fsWssUserMacAccessListTable.setStatus(_A)
_FsWssUserMacAccessListEntry_Object=MibTableRow
fsWssUserMacAccessListEntry=_FsWssUserMacAccessListEntry_Object((1,3,6,1,4,1,29601,2,90,2,4,1))
fsWssUserMacAccessListEntry.setIndexNames((0,_C,_S))
if mibBuilder.loadTexts:fsWssUserMacAccessListEntry.setStatus(_A)
_FsWssUserMacAccessListStaMac_Type=MacAddress
_FsWssUserMacAccessListStaMac_Object=MibTableColumn
fsWssUserMacAccessListStaMac=_FsWssUserMacAccessListStaMac_Object((1,3,6,1,4,1,29601,2,90,2,4,1,1),_FsWssUserMacAccessListStaMac_Type())
fsWssUserMacAccessListStaMac.setMaxAccess(_E)
if mibBuilder.loadTexts:fsWssUserMacAccessListStaMac.setStatus(_A)
_FsWssUserMacAccessListRowStatus_Type=RowStatus
_FsWssUserMacAccessListRowStatus_Object=MibTableColumn
fsWssUserMacAccessListRowStatus=_FsWssUserMacAccessListRowStatus_Object((1,3,6,1,4,1,29601,2,90,2,4,1,2),_FsWssUserMacAccessListRowStatus_Type())
fsWssUserMacAccessListRowStatus.setMaxAccess(_G)
if mibBuilder.loadTexts:fsWssUserMacAccessListRowStatus.setStatus(_A)
_FsWssUserMappingTable_Object=MibTable
fsWssUserMappingTable=_FsWssUserMappingTable_Object((1,3,6,1,4,1,29601,2,90,2,5))
if mibBuilder.loadTexts:fsWssUserMappingTable.setStatus(_A)
_FsWssUserMappingEntry_Object=MibTableRow
fsWssUserMappingEntry=_FsWssUserMappingEntry_Object((1,3,6,1,4,1,29601,2,90,2,5,1))
fsWssUserMappingEntry.setIndexNames((0,_C,_T),(0,_C,_U))
if mibBuilder.loadTexts:fsWssUserMappingEntry.setStatus(_A)
class _FsWssUserMappingName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_FsWssUserMappingName_Type.__name__=_H
_FsWssUserMappingName_Object=MibTableColumn
fsWssUserMappingName=_FsWssUserMappingName_Object((1,3,6,1,4,1,29601,2,90,2,5,1,1),_FsWssUserMappingName_Type())
fsWssUserMappingName.setMaxAccess(_E)
if mibBuilder.loadTexts:fsWssUserMappingName.setStatus(_A)
_FsWssUserMappingStaMac_Type=MacAddress
_FsWssUserMappingStaMac_Object=MibTableColumn
fsWssUserMappingStaMac=_FsWssUserMappingStaMac_Object((1,3,6,1,4,1,29601,2,90,2,5,1,2),_FsWssUserMappingStaMac_Type())
fsWssUserMappingStaMac.setMaxAccess(_E)
if mibBuilder.loadTexts:fsWssUserMappingStaMac.setStatus(_A)
_FsWssUserMappingRowStatus_Type=RowStatus
_FsWssUserMappingRowStatus_Object=MibTableColumn
fsWssUserMappingRowStatus=_FsWssUserMappingRowStatus_Object((1,3,6,1,4,1,29601,2,90,2,5,1,3),_FsWssUserMappingRowStatus_Type())
fsWssUserMappingRowStatus.setMaxAccess(_G)
if mibBuilder.loadTexts:fsWssUserMappingRowStatus.setStatus(_A)
_FsWssUserStats_ObjectIdentity=ObjectIdentity
fsWssUserStats=_FsWssUserStats_ObjectIdentity((1,3,6,1,4,1,29601,2,90,3))
_FsWssUserSessionTable_Object=MibTable
fsWssUserSessionTable=_FsWssUserSessionTable_Object((1,3,6,1,4,1,29601,2,90,3,1))
if mibBuilder.loadTexts:fsWssUserSessionTable.setStatus(_A)
_FsWssUserSessionEntry_Object=MibTableRow
fsWssUserSessionEntry=_FsWssUserSessionEntry_Object((1,3,6,1,4,1,29601,2,90,3,1,1))
fsWssUserSessionEntry.setIndexNames((0,_C,_V),(0,_C,_W))
if mibBuilder.loadTexts:fsWssUserSessionEntry.setStatus(_A)
_FsWssUserName_Type=FsWssUserIdName
_FsWssUserName_Object=MibTableColumn
fsWssUserName=_FsWssUserName_Object((1,3,6,1,4,1,29601,2,90,3,1,1,1),_FsWssUserName_Type())
fsWssUserName.setMaxAccess(_E)
if mibBuilder.loadTexts:fsWssUserName.setStatus(_A)
_FsWssUserStaMac_Type=FsWssUserStationMac
_FsWssUserStaMac_Object=MibTableColumn
fsWssUserStaMac=_FsWssUserStaMac_Object((1,3,6,1,4,1,29601,2,90,3,1,1,2),_FsWssUserStaMac_Type())
fsWssUserStaMac.setMaxAccess(_E)
if mibBuilder.loadTexts:fsWssUserStaMac.setStatus(_A)
class _FsWssUserWlanIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,512))
_FsWssUserWlanIndex_Type.__name__=_B
_FsWssUserWlanIndex_Object=MibTableColumn
fsWssUserWlanIndex=_FsWssUserWlanIndex_Object((1,3,6,1,4,1,29601,2,90,3,1,1,3),_FsWssUserWlanIndex_Type())
fsWssUserWlanIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:fsWssUserWlanIndex.setStatus(_A)
class _FsWssUserAllotedBandWidth_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_FsWssUserAllotedBandWidth_Type.__name__=_B
_FsWssUserAllotedBandWidth_Object=MibTableColumn
fsWssUserAllotedBandWidth=_FsWssUserAllotedBandWidth_Object((1,3,6,1,4,1,29601,2,90,3,1,1,4),_FsWssUserAllotedBandWidth_Type())
fsWssUserAllotedBandWidth.setMaxAccess(_F)
if mibBuilder.loadTexts:fsWssUserAllotedBandWidth.setStatus(_A)
class _FsWssUserAllotedVolume_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_FsWssUserAllotedVolume_Type.__name__=_B
_FsWssUserAllotedVolume_Object=MibTableColumn
fsWssUserAllotedVolume=_FsWssUserAllotedVolume_Object((1,3,6,1,4,1,29601,2,90,3,1,1,5),_FsWssUserAllotedVolume_Type())
fsWssUserAllotedVolume.setMaxAccess(_F)
if mibBuilder.loadTexts:fsWssUserAllotedVolume.setStatus(_A)
class _FsWssUserAllotedTime_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,31536000))
_FsWssUserAllotedTime_Type.__name__=_B
_FsWssUserAllotedTime_Object=MibTableColumn
fsWssUserAllotedTime=_FsWssUserAllotedTime_Object((1,3,6,1,4,1,29601,2,90,3,1,1,6),_FsWssUserAllotedTime_Type())
fsWssUserAllotedTime.setMaxAccess(_F)
if mibBuilder.loadTexts:fsWssUserAllotedTime.setStatus(_A)
class _FsWssUserUsedVolume_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_FsWssUserUsedVolume_Type.__name__=_B
_FsWssUserUsedVolume_Object=MibTableColumn
fsWssUserUsedVolume=_FsWssUserUsedVolume_Object((1,3,6,1,4,1,29601,2,90,3,1,1,7),_FsWssUserUsedVolume_Type())
fsWssUserUsedVolume.setMaxAccess(_F)
if mibBuilder.loadTexts:fsWssUserUsedVolume.setStatus(_A)
class _FsWssUserUsedTime_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,31536000))
_FsWssUserUsedTime_Type.__name__=_B
_FsWssUserUsedTime_Object=MibTableColumn
fsWssUserUsedTime=_FsWssUserUsedTime_Object((1,3,6,1,4,1,29601,2,90,3,1,1,8),_FsWssUserUsedTime_Type())
fsWssUserUsedTime.setMaxAccess(_F)
if mibBuilder.loadTexts:fsWssUserUsedTime.setStatus(_A)
class _FsWssUserAllotedDLBandWidth_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_FsWssUserAllotedDLBandWidth_Type.__name__=_B
_FsWssUserAllotedDLBandWidth_Object=MibTableColumn
fsWssUserAllotedDLBandWidth=_FsWssUserAllotedDLBandWidth_Object((1,3,6,1,4,1,29601,2,90,3,1,1,9),_FsWssUserAllotedDLBandWidth_Type())
fsWssUserAllotedDLBandWidth.setMaxAccess(_F)
if mibBuilder.loadTexts:fsWssUserAllotedDLBandWidth.setStatus(_A)
class _FsWssUserAllotedULBandWidth_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_FsWssUserAllotedULBandWidth_Type.__name__=_B
_FsWssUserAllotedULBandWidth_Object=MibTableColumn
fsWssUserAllotedULBandWidth=_FsWssUserAllotedULBandWidth_Object((1,3,6,1,4,1,29601,2,90,3,1,1,10),_FsWssUserAllotedULBandWidth_Type())
fsWssUserAllotedULBandWidth.setMaxAccess(_F)
if mibBuilder.loadTexts:fsWssUserAllotedULBandWidth.setStatus(_A)
_FsWssUserNotifyObjects_ObjectIdentity=ObjectIdentity
fsWssUserNotifyObjects=_FsWssUserNotifyObjects_ObjectIdentity((1,3,6,1,4,1,29601,2,90,4))
_FsWssUserTrapObjects_ObjectIdentity=ObjectIdentity
fsWssUserTrapObjects=_FsWssUserTrapObjects_ObjectIdentity((1,3,6,1,4,1,29601,2,90,4,1))
_FsWssUserStationMacAddress_Type=FsWssUserStationMac
_FsWssUserStationMacAddress_Object=MibScalar
fsWssUserStationMacAddress=_FsWssUserStationMacAddress_Object((1,3,6,1,4,1,29601,2,90,4,1,1),_FsWssUserStationMacAddress_Type())
fsWssUserStationMacAddress.setMaxAccess(_X)
if mibBuilder.loadTexts:fsWssUserStationMacAddress.setStatus(_A)
_FsWssNtfUserName_Type=FsWssUserIdName
_FsWssNtfUserName_Object=MibScalar
fsWssNtfUserName=_FsWssNtfUserName_Object((1,3,6,1,4,1,29601,2,90,4,1,2),_FsWssNtfUserName_Type())
fsWssNtfUserName.setMaxAccess(_X)
if mibBuilder.loadTexts:fsWssNtfUserName.setStatus(_A)
_FsWssUserNotifications_ObjectIdentity=ObjectIdentity
fsWssUserNotifications=_FsWssUserNotifications_ObjectIdentity((1,3,6,1,4,1,29601,2,90,5))
_FsWssUserTraps_ObjectIdentity=ObjectIdentity
fsWssUserTraps=_FsWssUserTraps_ObjectIdentity((1,3,6,1,4,1,29601,2,90,5,0))
fsWssUserVolumeExceeded=NotificationType((1,3,6,1,4,1,29601,2,90,5,0,1))
fsWssUserVolumeExceeded.setObjects(*((_C,_J),(_C,_K),(_C,_L),(_C,_Y)))
if mibBuilder.loadTexts:fsWssUserVolumeExceeded.setStatus(_A)
fsWssUserTimeExceeded=NotificationType((1,3,6,1,4,1,29601,2,90,5,0,2))
fsWssUserTimeExceeded.setObjects(*((_C,_J),(_C,_K),(_C,_L),(_C,_Z)))
if mibBuilder.loadTexts:fsWssUserTimeExceeded.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'FsWssUserStationMac':FsWssUserStationMac,'FsWssUserIdName':FsWssUserIdName,'fsWssUser':fsWssUser,'fsWssUserScalars':fsWssUserScalars,'fsWssUserRoleStatus':fsWssUserRoleStatus,'fsWssUserBlockedCount':fsWssUserBlockedCount,'fsWssUserLoggedCount':fsWssUserLoggedCount,'fsWssUserTraceOption':fsWssUserTraceOption,'fsWssUserRoleTrapStatus':fsWssUserRoleTrapStatus,'fsWssUserRole':fsWssUserRole,'fsWssUserGroupTable':fsWssUserGroupTable,'fsWssUserGroupEntry':fsWssUserGroupEntry,_O:fsWssUserGroupId,'fsWssUserGroupName':fsWssUserGroupName,'fsWssUserGroupBandWidth':fsWssUserGroupBandWidth,'fsWssUserGroupVolume':fsWssUserGroupVolume,'fsWssUserGroupTime':fsWssUserGroupTime,'fsWssUserGroupRowStatus':fsWssUserGroupRowStatus,'fsWssUserGroupDLBandWidth':fsWssUserGroupDLBandWidth,'fsWssUserGroupULBandWidth':fsWssUserGroupULBandWidth,'fsWssUserRoleTable':fsWssUserRoleTable,'fsWssUserRoleEntry':fsWssUserRoleEntry,_P:fsWssUserRoleName,_Q:fsWssUserRoleWlanIndex,'fsWssUserRoleGroupId':fsWssUserRoleGroupId,'fsWssUserRoleRowStatus':fsWssUserRoleRowStatus,'fsWssUserNameAccessListTable':fsWssUserNameAccessListTable,'fsWssUserNameAccessListEntry':fsWssUserNameAccessListEntry,_R:fsWssUserNameAccessListUserName,'fsWssUserNameAccessListRowStatus':fsWssUserNameAccessListRowStatus,'fsWssUserMacAccessListTable':fsWssUserMacAccessListTable,'fsWssUserMacAccessListEntry':fsWssUserMacAccessListEntry,_S:fsWssUserMacAccessListStaMac,'fsWssUserMacAccessListRowStatus':fsWssUserMacAccessListRowStatus,'fsWssUserMappingTable':fsWssUserMappingTable,'fsWssUserMappingEntry':fsWssUserMappingEntry,_T:fsWssUserMappingName,_U:fsWssUserMappingStaMac,'fsWssUserMappingRowStatus':fsWssUserMappingRowStatus,'fsWssUserStats':fsWssUserStats,'fsWssUserSessionTable':fsWssUserSessionTable,'fsWssUserSessionEntry':fsWssUserSessionEntry,_V:fsWssUserName,_W:fsWssUserStaMac,_J:fsWssUserWlanIndex,'fsWssUserAllotedBandWidth':fsWssUserAllotedBandWidth,'fsWssUserAllotedVolume':fsWssUserAllotedVolume,'fsWssUserAllotedTime':fsWssUserAllotedTime,_Y:fsWssUserUsedVolume,_Z:fsWssUserUsedTime,'fsWssUserAllotedDLBandWidth':fsWssUserAllotedDLBandWidth,'fsWssUserAllotedULBandWidth':fsWssUserAllotedULBandWidth,'fsWssUserNotifyObjects':fsWssUserNotifyObjects,'fsWssUserTrapObjects':fsWssUserTrapObjects,_L:fsWssUserStationMacAddress,_K:fsWssNtfUserName,'fsWssUserNotifications':fsWssUserNotifications,'fsWssUserTraps':fsWssUserTraps,'fsWssUserVolumeExceeded':fsWssUserVolumeExceeded,'fsWssUserTimeExceeded':fsWssUserTimeExceeded})