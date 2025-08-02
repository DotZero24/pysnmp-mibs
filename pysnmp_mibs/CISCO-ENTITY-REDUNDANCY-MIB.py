_AC='ceRedunMemberStatus'
_AB='ceRedunMemberConfig'
_AA='ceRedunGroupObjects'
_A9='ceRedunGroupTypeGroup'
_A8='ceRedunProtectStatusChange'
_A7='ceRedunEventSwitchover'
_A6='ceRedunEnableStatusChangeNotifs'
_A5='ceRedunEnableSwitchoverNotifs'
_A4='ceRedunCommandSwitch'
_A3='ceRedunCommandMbrNumber'
_A2='ceRedunMbrSwitchoverSeconds'
_A1='ceRedunMbrSwitchoverReason'
_A0='ceRedunMbrInternalState'
_z='ceRedunMbrLastSwitchover'
_y='ceRedunMbrSwitchoverCounts'
_x='ceRedunMbrStatusLastChanged'
_w='ceRedunMbrPriority'
_v='ceRedunMbrRemoteAddress'
_u='ceRedunMbrAddressType'
_t='ceRedunMbrRowStatus'
_s='ceRedunMbrStorageType'
_r='ceRedunMbrMode'
_q='ceRedunMbrPhysIndex'
_p='ceRedunMbrLastChanged'
_o='ceRedunGroupDirection'
_n='ceRedunGroupWaitToRestore'
_m='ceRedunGroupRevert'
_l='ceRedunGroupRowStatus'
_k='ceRedunGroupStorageType'
_j='ceRedunGroupArch'
_i='ceRedunGroupScope'
_h='ceRedunGroupRedunType'
_g='ceRedunGroupString'
_f='ceRedunGroupLastChanged'
_e='ceRedunSwitchoverReasonDescr'
_d='ceRedunReasonCategory'
_c='ceRedunInternalStateDescr'
_b='ceRedunStateCategory'
_a='ceRedunGroupCounts'
_Z='ceRedunGroupTypeName'
_Y='ceRedunGroupDefinitionChanged'
_X='ceRedunUsesGroupName'
_W='ceRedunMaxMbrsInGroup'
_V='ceRedunNextUnusedGroupIndex'
_U='ceRedunMbrStatusEntry'
_T='ceRedunMbrNumber'
_S='ceRedunSwitchoverReasonIndex'
_R='ceRedunInternalStateIndex'
_Q='ceRedunVendorType'
_P='Unsigned32'
_O='CeRedunScope'
_N='CeRedunArch'
_M='ceRedunMbrProtectingMbr'
_L='TruthValue'
_K='StorageType'
_J='ceRedunMbrStatusCurrent'
_I='read-write'
_H='ceRedunGroupIndex'
_G='not-accessible'
_F='Integer32'
_E='ceRedunGroupTypeIndex'
_D='read-create'
_C='read-only'
_B='CISCO-ENTITY-REDUNDANCY-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
CeRedunArch,CeRedunMbrStatus,CeRedunMode,CeRedunReasonCategories,CeRedunScope,CeRedunStateCategories,CeRedunSwitchCommand,CeRedunType=mibBuilder.importSymbols('CISCO-ENTITY-REDUNDANCY-TC-MIB',_N,'CeRedunMbrStatus','CeRedunMode','CeRedunReasonCategories',_O,'CeRedunStateCategories','CeRedunSwitchCommand','CeRedunType')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
PhysicalIndex,=mibBuilder.importSymbols('ENTITY-MIB','PhysicalIndex')
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress','InetAddressType')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB','SnmpAdminString')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_F,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_P,'iso')
AutonomousType,DisplayString,PhysAddress,RowStatus,StorageType,TextualConvention,TimeStamp,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','AutonomousType','DisplayString','PhysAddress','RowStatus',_K,'TextualConvention','TimeStamp',_L)
ciscoEntityRedunMIB=ModuleIdentity((1,3,6,1,4,1,9,9,498))
if mibBuilder.loadTexts:ciscoEntityRedunMIB.setRevisions(('2005-10-01 00:00',))
_CiscoEntityRedunMIBNotifs_ObjectIdentity=ObjectIdentity
ciscoEntityRedunMIBNotifs=_CiscoEntityRedunMIBNotifs_ObjectIdentity((1,3,6,1,4,1,9,9,498,0))
_CiscoEntityRedunMIBObjects_ObjectIdentity=ObjectIdentity
ciscoEntityRedunMIBObjects=_CiscoEntityRedunMIBObjects_ObjectIdentity((1,3,6,1,4,1,9,9,498,1))
_CeRedunGroup_ObjectIdentity=ObjectIdentity
ceRedunGroup=_CeRedunGroup_ObjectIdentity((1,3,6,1,4,1,9,9,498,1,1))
_CeRedunGroupTypesTable_Object=MibTable
ceRedunGroupTypesTable=_CeRedunGroupTypesTable_Object((1,3,6,1,4,1,9,9,498,1,1,1))
if mibBuilder.loadTexts:ceRedunGroupTypesTable.setStatus(_A)
_CeRedunGroupTypesEntry_Object=MibTableRow
ceRedunGroupTypesEntry=_CeRedunGroupTypesEntry_Object((1,3,6,1,4,1,9,9,498,1,1,1,1))
ceRedunGroupTypesEntry.setIndexNames((0,_B,_E))
if mibBuilder.loadTexts:ceRedunGroupTypesEntry.setStatus(_A)
_CeRedunGroupTypeIndex_Type=Unsigned32
_CeRedunGroupTypeIndex_Object=MibTableColumn
ceRedunGroupTypeIndex=_CeRedunGroupTypeIndex_Object((1,3,6,1,4,1,9,9,498,1,1,1,1,1),_CeRedunGroupTypeIndex_Type())
ceRedunGroupTypeIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:ceRedunGroupTypeIndex.setStatus(_A)
_CeRedunGroupTypeName_Type=SnmpAdminString
_CeRedunGroupTypeName_Object=MibTableColumn
ceRedunGroupTypeName=_CeRedunGroupTypeName_Object((1,3,6,1,4,1,9,9,498,1,1,1,1,2),_CeRedunGroupTypeName_Type())
ceRedunGroupTypeName.setMaxAccess(_C)
if mibBuilder.loadTexts:ceRedunGroupTypeName.setStatus(_A)
_CeRedunGroupCounts_Type=Gauge32
_CeRedunGroupCounts_Object=MibTableColumn
ceRedunGroupCounts=_CeRedunGroupCounts_Object((1,3,6,1,4,1,9,9,498,1,1,1,1,3),_CeRedunGroupCounts_Type())
ceRedunGroupCounts.setMaxAccess(_C)
if mibBuilder.loadTexts:ceRedunGroupCounts.setStatus(_A)
_CeRedunNextUnusedGroupIndex_Type=Unsigned32
_CeRedunNextUnusedGroupIndex_Object=MibTableColumn
ceRedunNextUnusedGroupIndex=_CeRedunNextUnusedGroupIndex_Object((1,3,6,1,4,1,9,9,498,1,1,1,1,4),_CeRedunNextUnusedGroupIndex_Type())
ceRedunNextUnusedGroupIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:ceRedunNextUnusedGroupIndex.setStatus(_A)
_CeRedunMaxMbrsInGroup_Type=Unsigned32
_CeRedunMaxMbrsInGroup_Object=MibTableColumn
ceRedunMaxMbrsInGroup=_CeRedunMaxMbrsInGroup_Object((1,3,6,1,4,1,9,9,498,1,1,1,1,5),_CeRedunMaxMbrsInGroup_Type())
ceRedunMaxMbrsInGroup.setMaxAccess(_C)
if mibBuilder.loadTexts:ceRedunMaxMbrsInGroup.setStatus(_A)
_CeRedunUsesGroupName_Type=TruthValue
_CeRedunUsesGroupName_Object=MibTableColumn
ceRedunUsesGroupName=_CeRedunUsesGroupName_Object((1,3,6,1,4,1,9,9,498,1,1,1,1,6),_CeRedunUsesGroupName_Type())
ceRedunUsesGroupName.setMaxAccess(_C)
if mibBuilder.loadTexts:ceRedunUsesGroupName.setStatus(_A)
_CeRedunGroupDefinitionChanged_Type=TimeStamp
_CeRedunGroupDefinitionChanged_Object=MibTableColumn
ceRedunGroupDefinitionChanged=_CeRedunGroupDefinitionChanged_Object((1,3,6,1,4,1,9,9,498,1,1,1,1,7),_CeRedunGroupDefinitionChanged_Type())
ceRedunGroupDefinitionChanged.setMaxAccess(_C)
if mibBuilder.loadTexts:ceRedunGroupDefinitionChanged.setStatus(_A)
_CeRedunVendorTypesTable_Object=MibTable
ceRedunVendorTypesTable=_CeRedunVendorTypesTable_Object((1,3,6,1,4,1,9,9,498,1,1,2))
if mibBuilder.loadTexts:ceRedunVendorTypesTable.setStatus(_A)
_CeRedunVendorTypesEntry_Object=MibTableRow
ceRedunVendorTypesEntry=_CeRedunVendorTypesEntry_Object((1,3,6,1,4,1,9,9,498,1,1,2,1))
ceRedunVendorTypesEntry.setIndexNames((0,_B,_E),(0,_B,_Q))
if mibBuilder.loadTexts:ceRedunVendorTypesEntry.setStatus(_A)
_CeRedunVendorType_Type=AutonomousType
_CeRedunVendorType_Object=MibTableColumn
ceRedunVendorType=_CeRedunVendorType_Object((1,3,6,1,4,1,9,9,498,1,1,2,1,1),_CeRedunVendorType_Type())
ceRedunVendorType.setMaxAccess(_C)
if mibBuilder.loadTexts:ceRedunVendorType.setStatus(_A)
_CeRedunInternalStatesTable_Object=MibTable
ceRedunInternalStatesTable=_CeRedunInternalStatesTable_Object((1,3,6,1,4,1,9,9,498,1,1,3))
if mibBuilder.loadTexts:ceRedunInternalStatesTable.setStatus(_A)
_CeRedunInternalStatesEntry_Object=MibTableRow
ceRedunInternalStatesEntry=_CeRedunInternalStatesEntry_Object((1,3,6,1,4,1,9,9,498,1,1,3,1))
ceRedunInternalStatesEntry.setIndexNames((0,_B,_E),(0,_B,_R))
if mibBuilder.loadTexts:ceRedunInternalStatesEntry.setStatus(_A)
_CeRedunInternalStateIndex_Type=Unsigned32
_CeRedunInternalStateIndex_Object=MibTableColumn
ceRedunInternalStateIndex=_CeRedunInternalStateIndex_Object((1,3,6,1,4,1,9,9,498,1,1,3,1,1),_CeRedunInternalStateIndex_Type())
ceRedunInternalStateIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:ceRedunInternalStateIndex.setStatus(_A)
_CeRedunStateCategory_Type=CeRedunStateCategories
_CeRedunStateCategory_Object=MibTableColumn
ceRedunStateCategory=_CeRedunStateCategory_Object((1,3,6,1,4,1,9,9,498,1,1,3,1,2),_CeRedunStateCategory_Type())
ceRedunStateCategory.setMaxAccess(_C)
if mibBuilder.loadTexts:ceRedunStateCategory.setStatus(_A)
_CeRedunInternalStateDescr_Type=SnmpAdminString
_CeRedunInternalStateDescr_Object=MibTableColumn
ceRedunInternalStateDescr=_CeRedunInternalStateDescr_Object((1,3,6,1,4,1,9,9,498,1,1,3,1,3),_CeRedunInternalStateDescr_Type())
ceRedunInternalStateDescr.setMaxAccess(_C)
if mibBuilder.loadTexts:ceRedunInternalStateDescr.setStatus(_A)
_CeRedunSwitchoverReasonTable_Object=MibTable
ceRedunSwitchoverReasonTable=_CeRedunSwitchoverReasonTable_Object((1,3,6,1,4,1,9,9,498,1,1,4))
if mibBuilder.loadTexts:ceRedunSwitchoverReasonTable.setStatus(_A)
_CeRedunSwitchoverReasonEntry_Object=MibTableRow
ceRedunSwitchoverReasonEntry=_CeRedunSwitchoverReasonEntry_Object((1,3,6,1,4,1,9,9,498,1,1,4,1))
ceRedunSwitchoverReasonEntry.setIndexNames((0,_B,_E),(0,_B,_S))
if mibBuilder.loadTexts:ceRedunSwitchoverReasonEntry.setStatus(_A)
_CeRedunSwitchoverReasonIndex_Type=Unsigned32
_CeRedunSwitchoverReasonIndex_Object=MibTableColumn
ceRedunSwitchoverReasonIndex=_CeRedunSwitchoverReasonIndex_Object((1,3,6,1,4,1,9,9,498,1,1,4,1,1),_CeRedunSwitchoverReasonIndex_Type())
ceRedunSwitchoverReasonIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:ceRedunSwitchoverReasonIndex.setStatus(_A)
_CeRedunReasonCategory_Type=CeRedunReasonCategories
_CeRedunReasonCategory_Object=MibTableColumn
ceRedunReasonCategory=_CeRedunReasonCategory_Object((1,3,6,1,4,1,9,9,498,1,1,4,1,2),_CeRedunReasonCategory_Type())
ceRedunReasonCategory.setMaxAccess(_C)
if mibBuilder.loadTexts:ceRedunReasonCategory.setStatus(_A)
_CeRedunSwitchoverReasonDescr_Type=SnmpAdminString
_CeRedunSwitchoverReasonDescr_Object=MibTableColumn
ceRedunSwitchoverReasonDescr=_CeRedunSwitchoverReasonDescr_Object((1,3,6,1,4,1,9,9,498,1,1,4,1,3),_CeRedunSwitchoverReasonDescr_Type())
ceRedunSwitchoverReasonDescr.setMaxAccess(_C)
if mibBuilder.loadTexts:ceRedunSwitchoverReasonDescr.setStatus(_A)
_CeRedunGroupLastChanged_Type=TimeStamp
_CeRedunGroupLastChanged_Object=MibScalar
ceRedunGroupLastChanged=_CeRedunGroupLastChanged_Object((1,3,6,1,4,1,9,9,498,1,1,5),_CeRedunGroupLastChanged_Type())
ceRedunGroupLastChanged.setMaxAccess(_C)
if mibBuilder.loadTexts:ceRedunGroupLastChanged.setStatus(_A)
_CeRedunGroupTable_Object=MibTable
ceRedunGroupTable=_CeRedunGroupTable_Object((1,3,6,1,4,1,9,9,498,1,1,6))
if mibBuilder.loadTexts:ceRedunGroupTable.setStatus(_A)
_CeRedunGroupEntry_Object=MibTableRow
ceRedunGroupEntry=_CeRedunGroupEntry_Object((1,3,6,1,4,1,9,9,498,1,1,6,1))
ceRedunGroupEntry.setIndexNames((0,_B,_E),(0,_B,_H))
if mibBuilder.loadTexts:ceRedunGroupEntry.setStatus(_A)
_CeRedunGroupIndex_Type=Unsigned32
_CeRedunGroupIndex_Object=MibTableColumn
ceRedunGroupIndex=_CeRedunGroupIndex_Object((1,3,6,1,4,1,9,9,498,1,1,6,1,1),_CeRedunGroupIndex_Type())
ceRedunGroupIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:ceRedunGroupIndex.setStatus(_A)
_CeRedunGroupString_Type=SnmpAdminString
_CeRedunGroupString_Object=MibTableColumn
ceRedunGroupString=_CeRedunGroupString_Object((1,3,6,1,4,1,9,9,498,1,1,6,1,2),_CeRedunGroupString_Type())
ceRedunGroupString.setMaxAccess(_D)
if mibBuilder.loadTexts:ceRedunGroupString.setStatus(_A)
_CeRedunGroupRedunType_Type=CeRedunType
_CeRedunGroupRedunType_Object=MibTableColumn
ceRedunGroupRedunType=_CeRedunGroupRedunType_Object((1,3,6,1,4,1,9,9,498,1,1,6,1,3),_CeRedunGroupRedunType_Type())
ceRedunGroupRedunType.setMaxAccess(_D)
if mibBuilder.loadTexts:ceRedunGroupRedunType.setStatus(_A)
class _CeRedunGroupScope_Type(CeRedunScope):defaultValue=2
_CeRedunGroupScope_Type.__name__=_O
_CeRedunGroupScope_Object=MibTableColumn
ceRedunGroupScope=_CeRedunGroupScope_Object((1,3,6,1,4,1,9,9,498,1,1,6,1,4),_CeRedunGroupScope_Type())
ceRedunGroupScope.setMaxAccess(_D)
if mibBuilder.loadTexts:ceRedunGroupScope.setStatus(_A)
class _CeRedunGroupArch_Type(CeRedunArch):defaultValue=3
_CeRedunGroupArch_Type.__name__=_N
_CeRedunGroupArch_Object=MibTableColumn
ceRedunGroupArch=_CeRedunGroupArch_Object((1,3,6,1,4,1,9,9,498,1,1,6,1,5),_CeRedunGroupArch_Type())
ceRedunGroupArch.setMaxAccess(_D)
if mibBuilder.loadTexts:ceRedunGroupArch.setStatus(_A)
class _CeRedunGroupRevert_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('nonrevertive',1),('revertive',2)))
_CeRedunGroupRevert_Type.__name__=_F
_CeRedunGroupRevert_Object=MibTableColumn
ceRedunGroupRevert=_CeRedunGroupRevert_Object((1,3,6,1,4,1,9,9,498,1,1,6,1,6),_CeRedunGroupRevert_Type())
ceRedunGroupRevert.setMaxAccess(_D)
if mibBuilder.loadTexts:ceRedunGroupRevert.setStatus(_A)
class _CeRedunGroupWaitToRestore_Type(Unsigned32):defaultValue=300
_CeRedunGroupWaitToRestore_Type.__name__=_P
_CeRedunGroupWaitToRestore_Object=MibTableColumn
ceRedunGroupWaitToRestore=_CeRedunGroupWaitToRestore_Object((1,3,6,1,4,1,9,9,498,1,1,6,1,7),_CeRedunGroupWaitToRestore_Type())
ceRedunGroupWaitToRestore.setMaxAccess(_D)
if mibBuilder.loadTexts:ceRedunGroupWaitToRestore.setStatus(_A)
if mibBuilder.loadTexts:ceRedunGroupWaitToRestore.setUnits('seconds')
class _CeRedunGroupDirection_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('unidirectional',1),('bidirectional',2)))
_CeRedunGroupDirection_Type.__name__=_F
_CeRedunGroupDirection_Object=MibTableColumn
ceRedunGroupDirection=_CeRedunGroupDirection_Object((1,3,6,1,4,1,9,9,498,1,1,6,1,8),_CeRedunGroupDirection_Type())
ceRedunGroupDirection.setMaxAccess(_D)
if mibBuilder.loadTexts:ceRedunGroupDirection.setStatus(_A)
class _CeRedunGroupStorageType_Type(StorageType):defaultValue=2
_CeRedunGroupStorageType_Type.__name__=_K
_CeRedunGroupStorageType_Object=MibTableColumn
ceRedunGroupStorageType=_CeRedunGroupStorageType_Object((1,3,6,1,4,1,9,9,498,1,1,6,1,9),_CeRedunGroupStorageType_Type())
ceRedunGroupStorageType.setMaxAccess(_D)
if mibBuilder.loadTexts:ceRedunGroupStorageType.setStatus(_A)
_CeRedunGroupRowStatus_Type=RowStatus
_CeRedunGroupRowStatus_Object=MibTableColumn
ceRedunGroupRowStatus=_CeRedunGroupRowStatus_Object((1,3,6,1,4,1,9,9,498,1,1,6,1,10),_CeRedunGroupRowStatus_Type())
ceRedunGroupRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:ceRedunGroupRowStatus.setStatus(_A)
_CeRedunMembers_ObjectIdentity=ObjectIdentity
ceRedunMembers=_CeRedunMembers_ObjectIdentity((1,3,6,1,4,1,9,9,498,1,2))
_CeRedunMbrLastChanged_Type=TimeStamp
_CeRedunMbrLastChanged_Object=MibScalar
ceRedunMbrLastChanged=_CeRedunMbrLastChanged_Object((1,3,6,1,4,1,9,9,498,1,2,1),_CeRedunMbrLastChanged_Type())
ceRedunMbrLastChanged.setMaxAccess(_C)
if mibBuilder.loadTexts:ceRedunMbrLastChanged.setStatus(_A)
_CeRedunMbrConfigTable_Object=MibTable
ceRedunMbrConfigTable=_CeRedunMbrConfigTable_Object((1,3,6,1,4,1,9,9,498,1,2,2))
if mibBuilder.loadTexts:ceRedunMbrConfigTable.setStatus(_A)
_CeRedunMbrConfigEntry_Object=MibTableRow
ceRedunMbrConfigEntry=_CeRedunMbrConfigEntry_Object((1,3,6,1,4,1,9,9,498,1,2,2,1))
ceRedunMbrConfigEntry.setIndexNames((0,_B,_E),(0,_B,_H),(0,_B,_T))
if mibBuilder.loadTexts:ceRedunMbrConfigEntry.setStatus(_A)
_CeRedunMbrNumber_Type=Unsigned32
_CeRedunMbrNumber_Object=MibTableColumn
ceRedunMbrNumber=_CeRedunMbrNumber_Object((1,3,6,1,4,1,9,9,498,1,2,2,1,1),_CeRedunMbrNumber_Type())
ceRedunMbrNumber.setMaxAccess(_G)
if mibBuilder.loadTexts:ceRedunMbrNumber.setStatus(_A)
_CeRedunMbrPhysIndex_Type=PhysicalIndex
_CeRedunMbrPhysIndex_Object=MibTableColumn
ceRedunMbrPhysIndex=_CeRedunMbrPhysIndex_Object((1,3,6,1,4,1,9,9,498,1,2,2,1,2),_CeRedunMbrPhysIndex_Type())
ceRedunMbrPhysIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:ceRedunMbrPhysIndex.setStatus(_A)
_CeRedunMbrMode_Type=CeRedunMode
_CeRedunMbrMode_Object=MibTableColumn
ceRedunMbrMode=_CeRedunMbrMode_Object((1,3,6,1,4,1,9,9,498,1,2,2,1,3),_CeRedunMbrMode_Type())
ceRedunMbrMode.setMaxAccess(_D)
if mibBuilder.loadTexts:ceRedunMbrMode.setStatus(_A)
_CeRedunMbrAddressType_Type=InetAddressType
_CeRedunMbrAddressType_Object=MibTableColumn
ceRedunMbrAddressType=_CeRedunMbrAddressType_Object((1,3,6,1,4,1,9,9,498,1,2,2,1,4),_CeRedunMbrAddressType_Type())
ceRedunMbrAddressType.setMaxAccess(_D)
if mibBuilder.loadTexts:ceRedunMbrAddressType.setStatus(_A)
_CeRedunMbrRemoteAddress_Type=InetAddress
_CeRedunMbrRemoteAddress_Object=MibTableColumn
ceRedunMbrRemoteAddress=_CeRedunMbrRemoteAddress_Object((1,3,6,1,4,1,9,9,498,1,2,2,1,5),_CeRedunMbrRemoteAddress_Type())
ceRedunMbrRemoteAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:ceRedunMbrRemoteAddress.setStatus(_A)
class _CeRedunMbrPriority_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('low',1),('high',2)))
_CeRedunMbrPriority_Type.__name__=_F
_CeRedunMbrPriority_Object=MibTableColumn
ceRedunMbrPriority=_CeRedunMbrPriority_Object((1,3,6,1,4,1,9,9,498,1,2,2,1,6),_CeRedunMbrPriority_Type())
ceRedunMbrPriority.setMaxAccess(_D)
if mibBuilder.loadTexts:ceRedunMbrPriority.setStatus(_A)
class _CeRedunMbrStorageType_Type(StorageType):defaultValue=2
_CeRedunMbrStorageType_Type.__name__=_K
_CeRedunMbrStorageType_Object=MibTableColumn
ceRedunMbrStorageType=_CeRedunMbrStorageType_Object((1,3,6,1,4,1,9,9,498,1,2,2,1,8),_CeRedunMbrStorageType_Type())
ceRedunMbrStorageType.setMaxAccess(_D)
if mibBuilder.loadTexts:ceRedunMbrStorageType.setStatus(_A)
_CeRedunMbrRowStatus_Type=RowStatus
_CeRedunMbrRowStatus_Object=MibTableColumn
ceRedunMbrRowStatus=_CeRedunMbrRowStatus_Object((1,3,6,1,4,1,9,9,498,1,2,2,1,9),_CeRedunMbrRowStatus_Type())
ceRedunMbrRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:ceRedunMbrRowStatus.setStatus(_A)
_CeRedunMbrStatusLastChanged_Type=TimeStamp
_CeRedunMbrStatusLastChanged_Object=MibScalar
ceRedunMbrStatusLastChanged=_CeRedunMbrStatusLastChanged_Object((1,3,6,1,4,1,9,9,498,1,2,3),_CeRedunMbrStatusLastChanged_Type())
ceRedunMbrStatusLastChanged.setMaxAccess(_C)
if mibBuilder.loadTexts:ceRedunMbrStatusLastChanged.setStatus(_A)
_CeRedunMbrStatusTable_Object=MibTable
ceRedunMbrStatusTable=_CeRedunMbrStatusTable_Object((1,3,6,1,4,1,9,9,498,1,2,4))
if mibBuilder.loadTexts:ceRedunMbrStatusTable.setStatus(_A)
_CeRedunMbrStatusEntry_Object=MibTableRow
ceRedunMbrStatusEntry=_CeRedunMbrStatusEntry_Object((1,3,6,1,4,1,9,9,498,1,2,4,1))
if mibBuilder.loadTexts:ceRedunMbrStatusEntry.setStatus(_A)
_CeRedunMbrStatusCurrent_Type=CeRedunMbrStatus
_CeRedunMbrStatusCurrent_Object=MibTableColumn
ceRedunMbrStatusCurrent=_CeRedunMbrStatusCurrent_Object((1,3,6,1,4,1,9,9,498,1,2,4,1,1),_CeRedunMbrStatusCurrent_Type())
ceRedunMbrStatusCurrent.setMaxAccess(_C)
if mibBuilder.loadTexts:ceRedunMbrStatusCurrent.setStatus(_A)
_CeRedunMbrProtectingMbr_Type=Unsigned32
_CeRedunMbrProtectingMbr_Object=MibTableColumn
ceRedunMbrProtectingMbr=_CeRedunMbrProtectingMbr_Object((1,3,6,1,4,1,9,9,498,1,2,4,1,2),_CeRedunMbrProtectingMbr_Type())
ceRedunMbrProtectingMbr.setMaxAccess(_C)
if mibBuilder.loadTexts:ceRedunMbrProtectingMbr.setStatus(_A)
_CeRedunMbrInternalState_Type=Unsigned32
_CeRedunMbrInternalState_Object=MibTableColumn
ceRedunMbrInternalState=_CeRedunMbrInternalState_Object((1,3,6,1,4,1,9,9,498,1,2,4,1,3),_CeRedunMbrInternalState_Type())
ceRedunMbrInternalState.setMaxAccess(_C)
if mibBuilder.loadTexts:ceRedunMbrInternalState.setStatus(_A)
_CeRedunMbrSwitchoverCounts_Type=Gauge32
_CeRedunMbrSwitchoverCounts_Object=MibTableColumn
ceRedunMbrSwitchoverCounts=_CeRedunMbrSwitchoverCounts_Object((1,3,6,1,4,1,9,9,498,1,2,4,1,4),_CeRedunMbrSwitchoverCounts_Type())
ceRedunMbrSwitchoverCounts.setMaxAccess(_C)
if mibBuilder.loadTexts:ceRedunMbrSwitchoverCounts.setStatus(_A)
_CeRedunMbrLastSwitchover_Type=TimeStamp
_CeRedunMbrLastSwitchover_Object=MibTableColumn
ceRedunMbrLastSwitchover=_CeRedunMbrLastSwitchover_Object((1,3,6,1,4,1,9,9,498,1,2,4,1,5),_CeRedunMbrLastSwitchover_Type())
ceRedunMbrLastSwitchover.setMaxAccess(_C)
if mibBuilder.loadTexts:ceRedunMbrLastSwitchover.setStatus(_A)
_CeRedunMbrSwitchoverReason_Type=Unsigned32
_CeRedunMbrSwitchoverReason_Object=MibTableColumn
ceRedunMbrSwitchoverReason=_CeRedunMbrSwitchoverReason_Object((1,3,6,1,4,1,9,9,498,1,2,4,1,6),_CeRedunMbrSwitchoverReason_Type())
ceRedunMbrSwitchoverReason.setMaxAccess(_C)
if mibBuilder.loadTexts:ceRedunMbrSwitchoverReason.setStatus(_A)
_CeRedunMbrSwitchoverSeconds_Type=Counter64
_CeRedunMbrSwitchoverSeconds_Object=MibTableColumn
ceRedunMbrSwitchoverSeconds=_CeRedunMbrSwitchoverSeconds_Object((1,3,6,1,4,1,9,9,498,1,2,4,1,8),_CeRedunMbrSwitchoverSeconds_Type())
ceRedunMbrSwitchoverSeconds.setMaxAccess(_C)
if mibBuilder.loadTexts:ceRedunMbrSwitchoverSeconds.setStatus(_A)
_CeRedunCommandTable_Object=MibTable
ceRedunCommandTable=_CeRedunCommandTable_Object((1,3,6,1,4,1,9,9,498,1,3))
if mibBuilder.loadTexts:ceRedunCommandTable.setStatus(_A)
_CeRedunCommandEntry_Object=MibTableRow
ceRedunCommandEntry=_CeRedunCommandEntry_Object((1,3,6,1,4,1,9,9,498,1,3,1))
ceRedunCommandEntry.setIndexNames((0,_B,_E),(0,_B,_H))
if mibBuilder.loadTexts:ceRedunCommandEntry.setStatus(_A)
class _CeRedunCommandMbrNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,2147483647))
_CeRedunCommandMbrNumber_Type.__name__=_F
_CeRedunCommandMbrNumber_Object=MibTableColumn
ceRedunCommandMbrNumber=_CeRedunCommandMbrNumber_Object((1,3,6,1,4,1,9,9,498,1,3,1,1),_CeRedunCommandMbrNumber_Type())
ceRedunCommandMbrNumber.setMaxAccess(_I)
if mibBuilder.loadTexts:ceRedunCommandMbrNumber.setStatus(_A)
_CeRedunCommandSwitch_Type=CeRedunSwitchCommand
_CeRedunCommandSwitch_Object=MibTableColumn
ceRedunCommandSwitch=_CeRedunCommandSwitch_Object((1,3,6,1,4,1,9,9,498,1,3,1,2),_CeRedunCommandSwitch_Type())
ceRedunCommandSwitch.setMaxAccess(_I)
if mibBuilder.loadTexts:ceRedunCommandSwitch.setStatus(_A)
class _CeRedunEnableSwitchoverNotifs_Type(TruthValue):defaultValue=2
_CeRedunEnableSwitchoverNotifs_Type.__name__=_L
_CeRedunEnableSwitchoverNotifs_Object=MibScalar
ceRedunEnableSwitchoverNotifs=_CeRedunEnableSwitchoverNotifs_Object((1,3,6,1,4,1,9,9,498,1,4),_CeRedunEnableSwitchoverNotifs_Type())
ceRedunEnableSwitchoverNotifs.setMaxAccess(_I)
if mibBuilder.loadTexts:ceRedunEnableSwitchoverNotifs.setStatus(_A)
class _CeRedunEnableStatusChangeNotifs_Type(TruthValue):defaultValue=2
_CeRedunEnableStatusChangeNotifs_Type.__name__=_L
_CeRedunEnableStatusChangeNotifs_Object=MibScalar
ceRedunEnableStatusChangeNotifs=_CeRedunEnableStatusChangeNotifs_Object((1,3,6,1,4,1,9,9,498,1,5),_CeRedunEnableStatusChangeNotifs_Type())
ceRedunEnableStatusChangeNotifs.setMaxAccess(_I)
if mibBuilder.loadTexts:ceRedunEnableStatusChangeNotifs.setStatus(_A)
_CiscoEntityRedunMIBConform_ObjectIdentity=ObjectIdentity
ciscoEntityRedunMIBConform=_CiscoEntityRedunMIBConform_ObjectIdentity((1,3,6,1,4,1,9,9,498,2))
_CeRedunCompliances_ObjectIdentity=ObjectIdentity
ceRedunCompliances=_CeRedunCompliances_ObjectIdentity((1,3,6,1,4,1,9,9,498,2,1))
_CeRedunGroups_ObjectIdentity=ObjectIdentity
ceRedunGroups=_CeRedunGroups_ObjectIdentity((1,3,6,1,4,1,9,9,498,2,2))
ceRedunMbrConfigEntry.registerAugmentions((_B,_U))
ceRedunMbrStatusEntry.setIndexNames(*ceRedunMbrConfigEntry.getIndexNames())
ceRedunGroupTypeGroup=ObjectGroup((1,3,6,1,4,1,9,9,498,2,2,1))
ceRedunGroupTypeGroup.setObjects(*((_B,_V),(_B,_W),(_B,_X),(_B,_Y)))
if mibBuilder.loadTexts:ceRedunGroupTypeGroup.setStatus(_A)
ceRedunOptionalGroupTypes=ObjectGroup((1,3,6,1,4,1,9,9,498,2,2,2))
ceRedunOptionalGroupTypes.setObjects(*((_B,_Z),(_B,_a)))
if mibBuilder.loadTexts:ceRedunOptionalGroupTypes.setStatus(_A)
ceRedunInternalStates=ObjectGroup((1,3,6,1,4,1,9,9,498,2,2,3))
ceRedunInternalStates.setObjects(*((_B,_b),(_B,_c)))
if mibBuilder.loadTexts:ceRedunInternalStates.setStatus(_A)
ceRedunSwitchoverReason=ObjectGroup((1,3,6,1,4,1,9,9,498,2,2,4))
ceRedunSwitchoverReason.setObjects(*((_B,_d),(_B,_e)))
if mibBuilder.loadTexts:ceRedunSwitchoverReason.setStatus(_A)
ceRedunGroupObjects=ObjectGroup((1,3,6,1,4,1,9,9,498,2,2,5))
ceRedunGroupObjects.setObjects(*((_B,_f),(_B,_g),(_B,_h),(_B,_i),(_B,_j),(_B,_k),(_B,_l)))
if mibBuilder.loadTexts:ceRedunGroupObjects.setStatus(_A)
ceRedunRevertiveGroup=ObjectGroup((1,3,6,1,4,1,9,9,498,2,2,6))
ceRedunRevertiveGroup.setObjects(*((_B,_m),(_B,_n)))
if mibBuilder.loadTexts:ceRedunRevertiveGroup.setStatus(_A)
ceRedunBidirectional=ObjectGroup((1,3,6,1,4,1,9,9,498,2,2,7))
ceRedunBidirectional.setObjects((_B,_o))
if mibBuilder.loadTexts:ceRedunBidirectional.setStatus(_A)
ceRedunMemberConfig=ObjectGroup((1,3,6,1,4,1,9,9,498,2,2,8))
ceRedunMemberConfig.setObjects(*((_B,_p),(_B,_q),(_B,_r),(_B,_s),(_B,_t)))
if mibBuilder.loadTexts:ceRedunMemberConfig.setStatus(_A)
ceRedunRemoteSystem=ObjectGroup((1,3,6,1,4,1,9,9,498,2,2,9))
ceRedunRemoteSystem.setObjects(*((_B,_u),(_B,_v)))
if mibBuilder.loadTexts:ceRedunRemoteSystem.setStatus(_A)
ceRedunOneToN=ObjectGroup((1,3,6,1,4,1,9,9,498,2,2,10))
ceRedunOneToN.setObjects((_B,_w))
if mibBuilder.loadTexts:ceRedunOneToN.setStatus(_A)
ceRedunMemberStatus=ObjectGroup((1,3,6,1,4,1,9,9,498,2,2,11))
ceRedunMemberStatus.setObjects(*((_B,_x),(_B,_J),(_B,_M),(_B,_y),(_B,_z)))
if mibBuilder.loadTexts:ceRedunMemberStatus.setStatus(_A)
ceRedunOptionalMbrStatus=ObjectGroup((1,3,6,1,4,1,9,9,498,2,2,12))
ceRedunOptionalMbrStatus.setObjects(*((_B,_A0),(_B,_A1),(_B,_A2)))
if mibBuilder.loadTexts:ceRedunOptionalMbrStatus.setStatus(_A)
ceRedunCommandsGroup=ObjectGroup((1,3,6,1,4,1,9,9,498,2,2,13))
ceRedunCommandsGroup.setObjects(*((_B,_A3),(_B,_A4)))
if mibBuilder.loadTexts:ceRedunCommandsGroup.setStatus(_A)
ceRedunNotifEnables=ObjectGroup((1,3,6,1,4,1,9,9,498,2,2,14))
ceRedunNotifEnables.setObjects(*((_B,_A5),(_B,_A6)))
if mibBuilder.loadTexts:ceRedunNotifEnables.setStatus(_A)
ceRedunEventSwitchover=NotificationType((1,3,6,1,4,1,9,9,498,0,1))
ceRedunEventSwitchover.setObjects(*((_B,_M),(_B,_J)))
if mibBuilder.loadTexts:ceRedunEventSwitchover.setStatus(_A)
ceRedunProtectStatusChange=NotificationType((1,3,6,1,4,1,9,9,498,0,2))
ceRedunProtectStatusChange.setObjects((_B,_J))
if mibBuilder.loadTexts:ceRedunProtectStatusChange.setStatus(_A)
ceRedunSwitchNotifGroup=NotificationGroup((1,3,6,1,4,1,9,9,498,2,2,15))
ceRedunSwitchNotifGroup.setObjects((_B,_A7))
if mibBuilder.loadTexts:ceRedunSwitchNotifGroup.setStatus(_A)
ceRedunProtectStatusNotifGroup=NotificationGroup((1,3,6,1,4,1,9,9,498,2,2,16))
ceRedunProtectStatusNotifGroup.setObjects((_B,_A8))
if mibBuilder.loadTexts:ceRedunProtectStatusNotifGroup.setStatus(_A)
ceRedunCompliance=ModuleCompliance((1,3,6,1,4,1,9,9,498,2,1,1))
ceRedunCompliance.setObjects(*((_B,_A9),(_B,_AA),(_B,_AB),(_B,_AC)))
if mibBuilder.loadTexts:ceRedunCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'ciscoEntityRedunMIB':ciscoEntityRedunMIB,'ciscoEntityRedunMIBNotifs':ciscoEntityRedunMIBNotifs,_A7:ceRedunEventSwitchover,_A8:ceRedunProtectStatusChange,'ciscoEntityRedunMIBObjects':ciscoEntityRedunMIBObjects,'ceRedunGroup':ceRedunGroup,'ceRedunGroupTypesTable':ceRedunGroupTypesTable,'ceRedunGroupTypesEntry':ceRedunGroupTypesEntry,_E:ceRedunGroupTypeIndex,_Z:ceRedunGroupTypeName,_a:ceRedunGroupCounts,_V:ceRedunNextUnusedGroupIndex,_W:ceRedunMaxMbrsInGroup,_X:ceRedunUsesGroupName,_Y:ceRedunGroupDefinitionChanged,'ceRedunVendorTypesTable':ceRedunVendorTypesTable,'ceRedunVendorTypesEntry':ceRedunVendorTypesEntry,_Q:ceRedunVendorType,'ceRedunInternalStatesTable':ceRedunInternalStatesTable,'ceRedunInternalStatesEntry':ceRedunInternalStatesEntry,_R:ceRedunInternalStateIndex,_b:ceRedunStateCategory,_c:ceRedunInternalStateDescr,'ceRedunSwitchoverReasonTable':ceRedunSwitchoverReasonTable,'ceRedunSwitchoverReasonEntry':ceRedunSwitchoverReasonEntry,_S:ceRedunSwitchoverReasonIndex,_d:ceRedunReasonCategory,_e:ceRedunSwitchoverReasonDescr,_f:ceRedunGroupLastChanged,'ceRedunGroupTable':ceRedunGroupTable,'ceRedunGroupEntry':ceRedunGroupEntry,_H:ceRedunGroupIndex,_g:ceRedunGroupString,_h:ceRedunGroupRedunType,_i:ceRedunGroupScope,_j:ceRedunGroupArch,_m:ceRedunGroupRevert,_n:ceRedunGroupWaitToRestore,_o:ceRedunGroupDirection,_k:ceRedunGroupStorageType,_l:ceRedunGroupRowStatus,'ceRedunMembers':ceRedunMembers,_p:ceRedunMbrLastChanged,'ceRedunMbrConfigTable':ceRedunMbrConfigTable,'ceRedunMbrConfigEntry':ceRedunMbrConfigEntry,_T:ceRedunMbrNumber,_q:ceRedunMbrPhysIndex,_r:ceRedunMbrMode,_u:ceRedunMbrAddressType,_v:ceRedunMbrRemoteAddress,_w:ceRedunMbrPriority,_s:ceRedunMbrStorageType,_t:ceRedunMbrRowStatus,_x:ceRedunMbrStatusLastChanged,'ceRedunMbrStatusTable':ceRedunMbrStatusTable,_U:ceRedunMbrStatusEntry,_J:ceRedunMbrStatusCurrent,_M:ceRedunMbrProtectingMbr,_A0:ceRedunMbrInternalState,_y:ceRedunMbrSwitchoverCounts,_z:ceRedunMbrLastSwitchover,_A1:ceRedunMbrSwitchoverReason,_A2:ceRedunMbrSwitchoverSeconds,'ceRedunCommandTable':ceRedunCommandTable,'ceRedunCommandEntry':ceRedunCommandEntry,_A3:ceRedunCommandMbrNumber,_A4:ceRedunCommandSwitch,_A5:ceRedunEnableSwitchoverNotifs,_A6:ceRedunEnableStatusChangeNotifs,'ciscoEntityRedunMIBConform':ciscoEntityRedunMIBConform,'ceRedunCompliances':ceRedunCompliances,'ceRedunCompliance':ceRedunCompliance,'ceRedunGroups':ceRedunGroups,_A9:ceRedunGroupTypeGroup,'ceRedunOptionalGroupTypes':ceRedunOptionalGroupTypes,'ceRedunInternalStates':ceRedunInternalStates,'ceRedunSwitchoverReason':ceRedunSwitchoverReason,_AA:ceRedunGroupObjects,'ceRedunRevertiveGroup':ceRedunRevertiveGroup,'ceRedunBidirectional':ceRedunBidirectional,_AB:ceRedunMemberConfig,'ceRedunRemoteSystem':ceRedunRemoteSystem,'ceRedunOneToN':ceRedunOneToN,_AC:ceRedunMemberStatus,'ceRedunOptionalMbrStatus':ceRedunOptionalMbrStatus,'ceRedunCommandsGroup':ceRedunCommandsGroup,'ceRedunNotifEnables':ceRedunNotifEnables,'ceRedunSwitchNotifGroup':ceRedunSwitchNotifGroup,'ceRedunProtectStatusNotifGroup':ceRedunProtectStatusNotifGroup})