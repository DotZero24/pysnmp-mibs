_AP='ciscoVdcSharedInterfaceGroup'
_AO='ciscoVdcFCoEVlansGroup'
_AN='ciscoVdcIfMembershipGroup'
_AM='ciscoVdcGlobalGroup'
_AL='ciscoVdcResTemplateGroup'
_AK='ciscoVdcResUsageGroup'
_AJ='ciscoVdcGlobalResUsageGroup'
_AI='ciscoVdcExtGroup'
_AH='ciscoVdcSharedInterfaceStorageType'
_AG='ciscoVdcSharedInterfaceRowStatus'
_AF='ciscoVdcFCoEVlansFromVdc'
_AE='ciscoVdcFCoEVlansSecond2K'
_AD='ciscoVdcFCoEVlansFirst2K'
_AC='ciscoVdcIfMembershipStorageType'
_AB='ciscoVdcIfMembershipStatus'
_AA='ciscoVdcCombinedHostnameEnabled'
_A9='ciscoVdcMaxNumberVdcAllowed'
_A8='ciscoVdcResTemplateStorageType'
_A7='ciscoVdcResTemplateStatus'
_A6='ciscoVdcResTemplateMax'
_A5='ciscoVdcResTemplateMin'
_A4='ciscoVdcResAvail'
_A3='ciscoVdcResUnused'
_A2='ciscoVdcResUsed'
_A1='ciscoVdcResMax'
_A0='ciscoVdcResMin'
_z='ciscoVdcGlobalResTotal'
_y='ciscoVdcGlobalResAvail'
_x='ciscoVdcGlobalResFree'
_w='ciscoVdcGlobalResUnused'
_v='ciscoVdcGlobalResUsed'
_u='ciscoVdcGlobalResName'
_t='ciscoVdcCpuSharePercent'
_s='ciscoVdcCpuPriority'
_r='ciscoVdcModuleCapList'
_q='ciscoVdcResourceTemplate'
_p='ciscoVdcFeatureSetList'
_o='ciscoVdcFromUnallocatedIntf'
_n='ciscoVdcAdminStatus'
_m='ciscoVdcType'
_l='ciscoVdcRestartReason'
_k='ciscoVdcRestartTime'
_j='ciscoVdcRestartCount'
_i='ciscoVdcReloadCount'
_h='ciscoVdcTimeCreated'
_g='ciscoVdcBootOrder'
_f='ciscoVdcDualSupHaPolicy'
_e='ciscoVdcSingleSupHaPolicy'
_d='ciscoVdcStorageType'
_c='ciscoVdcRowStatus'
_b='ciscoVdcSwitchId'
_a='ciscoVdcMac'
_Z='ciscoVdcFcoeCapable'
_Y='ciscoVdcState'
_X='ciscoVdcName'
_W='ciscoVdcSharedInterfaceifIndex'
_V='ciscoVdcIfMembershipifIndex'
_U='ciscoVdcResTemplateResID'
_T='ciscoVdcResTemplateName'
_S='ciscoVdcResID'
_R='ciscoVdcGlobalResID'
_Q='ethernet'
_P='suspended'
_O='active'
_N='Unsigned32'
_M='SnmpAdminString'
_L='ciscoVdcGroup'
_K='CiscoVdcHaPolicy'
_J='Bits'
_I='StorageType'
_H='not-accessible'
_G='ciscoVdcId'
_F='Integer32'
_E='read-create'
_D='read-write'
_C='read-only'
_B='CISCO-VDC-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
Cisco2KVlanList,=mibBuilder.importSymbols('CISCO-TC','Cisco2KVlanList')
InterfaceIndex,=mibBuilder.importSymbols('IF-MIB','InterfaceIndex')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB',_M)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI',_J,'Counter32','Counter64','Gauge32',_F,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_N,'iso')
DateAndTime,DisplayString,MacAddress,PhysAddress,RowStatus,StorageType,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime','DisplayString','MacAddress','PhysAddress','RowStatus',_I,'TextualConvention','TruthValue')
ciscoVdcMIB=ModuleIdentity((1,3,6,1,4,1,9,9,774))
if mibBuilder.loadTexts:ciscoVdcMIB.setRevisions(('2016-11-03 00:00','2016-01-19 00:00','2013-09-24 00:00','2013-07-02 00:00','2013-06-08 00:00','2011-05-19 00:00'))
class CiscoVdcHaPolicy(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*(('reload',0),('restart',1),('bringDown',2),('switchOver',3)))
class CiscoVdcPercentOrMinusOne(TextualConvention,Integer32):status=_A;displayHint='d';subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,-1),ValueRangeConstraint(0,100))
_CiscoVdcMIBNotifs_ObjectIdentity=ObjectIdentity
ciscoVdcMIBNotifs=_CiscoVdcMIBNotifs_ObjectIdentity((1,3,6,1,4,1,9,9,774,0))
_CiscoVdcMIBObjects_ObjectIdentity=ObjectIdentity
ciscoVdcMIBObjects=_CiscoVdcMIBObjects_ObjectIdentity((1,3,6,1,4,1,9,9,774,1))
_CiscoVdcTable_Object=MibTable
ciscoVdcTable=_CiscoVdcTable_Object((1,3,6,1,4,1,9,9,774,1,1))
if mibBuilder.loadTexts:ciscoVdcTable.setStatus(_A)
_CiscoVdcEntry_Object=MibTableRow
ciscoVdcEntry=_CiscoVdcEntry_Object((1,3,6,1,4,1,9,9,774,1,1,1))
ciscoVdcEntry.setIndexNames((0,_B,_G))
if mibBuilder.loadTexts:ciscoVdcEntry.setStatus(_A)
class _CiscoVdcId_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4096))
_CiscoVdcId_Type.__name__=_N
_CiscoVdcId_Object=MibTableColumn
ciscoVdcId=_CiscoVdcId_Object((1,3,6,1,4,1,9,9,774,1,1,1,1),_CiscoVdcId_Type())
ciscoVdcId.setMaxAccess(_H)
if mibBuilder.loadTexts:ciscoVdcId.setStatus(_A)
class _CiscoVdcName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_CiscoVdcName_Type.__name__=_M
_CiscoVdcName_Object=MibTableColumn
ciscoVdcName=_CiscoVdcName_Object((1,3,6,1,4,1,9,9,774,1,1,1,2),_CiscoVdcName_Type())
ciscoVdcName.setMaxAccess(_D)
if mibBuilder.loadTexts:ciscoVdcName.setStatus(_A)
class _CiscoVdcState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13)));namedValues=NamedValues(*((_O,1),(_P,2),('nonconfigured',3),('configured',4),('creating',5),('deleting',6),('failed',7),('pending',8),('updating',9),('restarting',10),('suspending',11),('resuming',12),('failing',13)))
_CiscoVdcState_Type.__name__=_F
_CiscoVdcState_Object=MibTableColumn
ciscoVdcState=_CiscoVdcState_Object((1,3,6,1,4,1,9,9,774,1,1,1,3),_CiscoVdcState_Type())
ciscoVdcState.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoVdcState.setStatus(_A)
class _CiscoVdcFcoeCapable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('disallowed',1),('allowed',2),('installed',3)))
_CiscoVdcFcoeCapable_Type.__name__=_F
_CiscoVdcFcoeCapable_Object=MibTableColumn
ciscoVdcFcoeCapable=_CiscoVdcFcoeCapable_Object((1,3,6,1,4,1,9,9,774,1,1,1,4),_CiscoVdcFcoeCapable_Type())
ciscoVdcFcoeCapable.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoVdcFcoeCapable.setStatus(_A)
_CiscoVdcMac_Type=MacAddress
_CiscoVdcMac_Object=MibTableColumn
ciscoVdcMac=_CiscoVdcMac_Object((1,3,6,1,4,1,9,9,774,1,1,1,5),_CiscoVdcMac_Type())
ciscoVdcMac.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoVdcMac.setStatus(_A)
_CiscoVdcSwitchId_Type=MacAddress
_CiscoVdcSwitchId_Object=MibTableColumn
ciscoVdcSwitchId=_CiscoVdcSwitchId_Object((1,3,6,1,4,1,9,9,774,1,1,1,6),_CiscoVdcSwitchId_Type())
ciscoVdcSwitchId.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoVdcSwitchId.setStatus(_A)
_CiscoVdcRowStatus_Type=RowStatus
_CiscoVdcRowStatus_Object=MibTableColumn
ciscoVdcRowStatus=_CiscoVdcRowStatus_Object((1,3,6,1,4,1,9,9,774,1,1,1,7),_CiscoVdcRowStatus_Type())
ciscoVdcRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:ciscoVdcRowStatus.setStatus(_A)
_CiscoVdcStorageType_Type=StorageType
_CiscoVdcStorageType_Object=MibTableColumn
ciscoVdcStorageType=_CiscoVdcStorageType_Object((1,3,6,1,4,1,9,9,774,1,1,1,8),_CiscoVdcStorageType_Type())
ciscoVdcStorageType.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoVdcStorageType.setStatus(_A)
_CiscoVdcGlobal_ObjectIdentity=ObjectIdentity
ciscoVdcGlobal=_CiscoVdcGlobal_ObjectIdentity((1,3,6,1,4,1,9,9,774,1,2))
_CiscoVdcMaxNumberVdcAllowed_Type=Integer32
_CiscoVdcMaxNumberVdcAllowed_Object=MibScalar
ciscoVdcMaxNumberVdcAllowed=_CiscoVdcMaxNumberVdcAllowed_Object((1,3,6,1,4,1,9,9,774,1,2,1),_CiscoVdcMaxNumberVdcAllowed_Type())
ciscoVdcMaxNumberVdcAllowed.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoVdcMaxNumberVdcAllowed.setStatus(_A)
_CiscoVdcCombinedHostnameEnabled_Type=TruthValue
_CiscoVdcCombinedHostnameEnabled_Object=MibScalar
ciscoVdcCombinedHostnameEnabled=_CiscoVdcCombinedHostnameEnabled_Object((1,3,6,1,4,1,9,9,774,1,2,2),_CiscoVdcCombinedHostnameEnabled_Type())
ciscoVdcCombinedHostnameEnabled.setMaxAccess(_D)
if mibBuilder.loadTexts:ciscoVdcCombinedHostnameEnabled.setStatus(_A)
_CiscoVdcExt_ObjectIdentity=ObjectIdentity
ciscoVdcExt=_CiscoVdcExt_ObjectIdentity((1,3,6,1,4,1,9,9,774,1,3))
_CiscoVdcExtTable_Object=MibTable
ciscoVdcExtTable=_CiscoVdcExtTable_Object((1,3,6,1,4,1,9,9,774,1,3,1))
if mibBuilder.loadTexts:ciscoVdcExtTable.setStatus(_A)
_CiscoVdcExtEntry_Object=MibTableRow
ciscoVdcExtEntry=_CiscoVdcExtEntry_Object((1,3,6,1,4,1,9,9,774,1,3,1,1))
ciscoVdcExtEntry.setIndexNames((0,_B,_G))
if mibBuilder.loadTexts:ciscoVdcExtEntry.setStatus(_A)
class _CiscoVdcSingleSupHaPolicy_Type(CiscoVdcHaPolicy):defaultValue=1
_CiscoVdcSingleSupHaPolicy_Type.__name__=_K
_CiscoVdcSingleSupHaPolicy_Object=MibTableColumn
ciscoVdcSingleSupHaPolicy=_CiscoVdcSingleSupHaPolicy_Object((1,3,6,1,4,1,9,9,774,1,3,1,1,1),_CiscoVdcSingleSupHaPolicy_Type())
ciscoVdcSingleSupHaPolicy.setMaxAccess(_D)
if mibBuilder.loadTexts:ciscoVdcSingleSupHaPolicy.setStatus(_A)
class _CiscoVdcDualSupHaPolicy_Type(CiscoVdcHaPolicy):defaultValue=3
_CiscoVdcDualSupHaPolicy_Type.__name__=_K
_CiscoVdcDualSupHaPolicy_Object=MibTableColumn
ciscoVdcDualSupHaPolicy=_CiscoVdcDualSupHaPolicy_Object((1,3,6,1,4,1,9,9,774,1,3,1,1,2),_CiscoVdcDualSupHaPolicy_Type())
ciscoVdcDualSupHaPolicy.setMaxAccess(_D)
if mibBuilder.loadTexts:ciscoVdcDualSupHaPolicy.setStatus(_A)
_CiscoVdcBootOrder_Type=Unsigned32
_CiscoVdcBootOrder_Object=MibTableColumn
ciscoVdcBootOrder=_CiscoVdcBootOrder_Object((1,3,6,1,4,1,9,9,774,1,3,1,1,3),_CiscoVdcBootOrder_Type())
ciscoVdcBootOrder.setMaxAccess(_D)
if mibBuilder.loadTexts:ciscoVdcBootOrder.setStatus(_A)
_CiscoVdcTimeCreated_Type=DateAndTime
_CiscoVdcTimeCreated_Object=MibTableColumn
ciscoVdcTimeCreated=_CiscoVdcTimeCreated_Object((1,3,6,1,4,1,9,9,774,1,3,1,1,4),_CiscoVdcTimeCreated_Type())
ciscoVdcTimeCreated.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoVdcTimeCreated.setStatus(_A)
_CiscoVdcReloadCount_Type=Gauge32
_CiscoVdcReloadCount_Object=MibTableColumn
ciscoVdcReloadCount=_CiscoVdcReloadCount_Object((1,3,6,1,4,1,9,9,774,1,3,1,1,5),_CiscoVdcReloadCount_Type())
ciscoVdcReloadCount.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoVdcReloadCount.setStatus(_A)
_CiscoVdcRestartCount_Type=Gauge32
_CiscoVdcRestartCount_Object=MibTableColumn
ciscoVdcRestartCount=_CiscoVdcRestartCount_Object((1,3,6,1,4,1,9,9,774,1,3,1,1,6),_CiscoVdcRestartCount_Type())
ciscoVdcRestartCount.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoVdcRestartCount.setStatus(_A)
_CiscoVdcRestartTime_Type=DateAndTime
_CiscoVdcRestartTime_Object=MibTableColumn
ciscoVdcRestartTime=_CiscoVdcRestartTime_Object((1,3,6,1,4,1,9,9,774,1,3,1,1,7),_CiscoVdcRestartTime_Type())
ciscoVdcRestartTime.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoVdcRestartTime.setStatus(_A)
_CiscoVdcRestartReason_Type=SnmpAdminString
_CiscoVdcRestartReason_Object=MibTableColumn
ciscoVdcRestartReason=_CiscoVdcRestartReason_Object((1,3,6,1,4,1,9,9,774,1,3,1,1,8),_CiscoVdcRestartReason_Type())
ciscoVdcRestartReason.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoVdcRestartReason.setStatus(_A)
class _CiscoVdcType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('admin',1),(_Q,2),('storage',3)))
_CiscoVdcType_Type.__name__=_F
_CiscoVdcType_Object=MibTableColumn
ciscoVdcType=_CiscoVdcType_Object((1,3,6,1,4,1,9,9,774,1,3,1,1,9),_CiscoVdcType_Type())
ciscoVdcType.setMaxAccess(_D)
if mibBuilder.loadTexts:ciscoVdcType.setStatus(_A)
class _CiscoVdcAdminStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_O,1),(_P,2)))
_CiscoVdcAdminStatus_Type.__name__=_F
_CiscoVdcAdminStatus_Object=MibTableColumn
ciscoVdcAdminStatus=_CiscoVdcAdminStatus_Object((1,3,6,1,4,1,9,9,774,1,3,1,1,10),_CiscoVdcAdminStatus_Type())
ciscoVdcAdminStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:ciscoVdcAdminStatus.setStatus(_A)
class _CiscoVdcFromUnallocatedIntf_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('noOp',1),('allocate',2)))
_CiscoVdcFromUnallocatedIntf_Type.__name__=_F
_CiscoVdcFromUnallocatedIntf_Object=MibTableColumn
ciscoVdcFromUnallocatedIntf=_CiscoVdcFromUnallocatedIntf_Object((1,3,6,1,4,1,9,9,774,1,3,1,1,11),_CiscoVdcFromUnallocatedIntf_Type())
ciscoVdcFromUnallocatedIntf.setMaxAccess(_D)
if mibBuilder.loadTexts:ciscoVdcFromUnallocatedIntf.setStatus(_A)
class _CiscoVdcFeatureSetList_Type(Bits):namedValues=NamedValues(*(('fcoe',0),('fabricPath',1),('fex',2),('mpls',3),(_Q,4),('virtualization',5),('fabric',6),('fcoeNpv',7)))
_CiscoVdcFeatureSetList_Type.__name__=_J
_CiscoVdcFeatureSetList_Object=MibTableColumn
ciscoVdcFeatureSetList=_CiscoVdcFeatureSetList_Object((1,3,6,1,4,1,9,9,774,1,3,1,1,12),_CiscoVdcFeatureSetList_Type())
ciscoVdcFeatureSetList.setMaxAccess(_D)
if mibBuilder.loadTexts:ciscoVdcFeatureSetList.setStatus(_A)
_CiscoVdcResourceTemplate_Type=SnmpAdminString
_CiscoVdcResourceTemplate_Object=MibTableColumn
ciscoVdcResourceTemplate=_CiscoVdcResourceTemplate_Object((1,3,6,1,4,1,9,9,774,1,3,1,1,13),_CiscoVdcResourceTemplate_Type())
ciscoVdcResourceTemplate.setMaxAccess(_D)
if mibBuilder.loadTexts:ciscoVdcResourceTemplate.setStatus(_A)
class _CiscoVdcModuleCapList_Type(Bits):namedValues=NamedValues(*(('m1',0),('f1',1),('m1xl',2),('f2',3),('m2xl',4),('fc',5),('f2e',6),('f3',7),('m3',8)))
_CiscoVdcModuleCapList_Type.__name__=_J
_CiscoVdcModuleCapList_Object=MibTableColumn
ciscoVdcModuleCapList=_CiscoVdcModuleCapList_Object((1,3,6,1,4,1,9,9,774,1,3,1,1,14),_CiscoVdcModuleCapList_Type())
ciscoVdcModuleCapList.setMaxAccess(_D)
if mibBuilder.loadTexts:ciscoVdcModuleCapList.setStatus(_A)
class _CiscoVdcCpuPriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,65535))
_CiscoVdcCpuPriority_Type.__name__=_F
_CiscoVdcCpuPriority_Object=MibTableColumn
ciscoVdcCpuPriority=_CiscoVdcCpuPriority_Object((1,3,6,1,4,1,9,9,774,1,3,1,1,15),_CiscoVdcCpuPriority_Type())
ciscoVdcCpuPriority.setMaxAccess(_D)
if mibBuilder.loadTexts:ciscoVdcCpuPriority.setStatus(_A)
_CiscoVdcCpuSharePercent_Type=CiscoVdcPercentOrMinusOne
_CiscoVdcCpuSharePercent_Object=MibTableColumn
ciscoVdcCpuSharePercent=_CiscoVdcCpuSharePercent_Object((1,3,6,1,4,1,9,9,774,1,3,1,1,16),_CiscoVdcCpuSharePercent_Type())
ciscoVdcCpuSharePercent.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoVdcCpuSharePercent.setStatus(_A)
_CiscoVdcResource_ObjectIdentity=ObjectIdentity
ciscoVdcResource=_CiscoVdcResource_ObjectIdentity((1,3,6,1,4,1,9,9,774,1,4))
_CiscoVdcGlobalResUsageTable_Object=MibTable
ciscoVdcGlobalResUsageTable=_CiscoVdcGlobalResUsageTable_Object((1,3,6,1,4,1,9,9,774,1,4,1))
if mibBuilder.loadTexts:ciscoVdcGlobalResUsageTable.setStatus(_A)
_CiscoVdcGlobalResUsageEntry_Object=MibTableRow
ciscoVdcGlobalResUsageEntry=_CiscoVdcGlobalResUsageEntry_Object((1,3,6,1,4,1,9,9,774,1,4,1,1))
ciscoVdcGlobalResUsageEntry.setIndexNames((0,_B,_R))
if mibBuilder.loadTexts:ciscoVdcGlobalResUsageEntry.setStatus(_A)
_CiscoVdcGlobalResID_Type=Unsigned32
_CiscoVdcGlobalResID_Object=MibTableColumn
ciscoVdcGlobalResID=_CiscoVdcGlobalResID_Object((1,3,6,1,4,1,9,9,774,1,4,1,1,1),_CiscoVdcGlobalResID_Type())
ciscoVdcGlobalResID.setMaxAccess(_H)
if mibBuilder.loadTexts:ciscoVdcGlobalResID.setStatus(_A)
_CiscoVdcGlobalResName_Type=SnmpAdminString
_CiscoVdcGlobalResName_Object=MibTableColumn
ciscoVdcGlobalResName=_CiscoVdcGlobalResName_Object((1,3,6,1,4,1,9,9,774,1,4,1,1,2),_CiscoVdcGlobalResName_Type())
ciscoVdcGlobalResName.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoVdcGlobalResName.setStatus(_A)
_CiscoVdcGlobalResUsed_Type=Unsigned32
_CiscoVdcGlobalResUsed_Object=MibTableColumn
ciscoVdcGlobalResUsed=_CiscoVdcGlobalResUsed_Object((1,3,6,1,4,1,9,9,774,1,4,1,1,3),_CiscoVdcGlobalResUsed_Type())
ciscoVdcGlobalResUsed.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoVdcGlobalResUsed.setStatus(_A)
_CiscoVdcGlobalResUnused_Type=Unsigned32
_CiscoVdcGlobalResUnused_Object=MibTableColumn
ciscoVdcGlobalResUnused=_CiscoVdcGlobalResUnused_Object((1,3,6,1,4,1,9,9,774,1,4,1,1,4),_CiscoVdcGlobalResUnused_Type())
ciscoVdcGlobalResUnused.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoVdcGlobalResUnused.setStatus(_A)
_CiscoVdcGlobalResFree_Type=Unsigned32
_CiscoVdcGlobalResFree_Object=MibTableColumn
ciscoVdcGlobalResFree=_CiscoVdcGlobalResFree_Object((1,3,6,1,4,1,9,9,774,1,4,1,1,5),_CiscoVdcGlobalResFree_Type())
ciscoVdcGlobalResFree.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoVdcGlobalResFree.setStatus(_A)
_CiscoVdcGlobalResAvail_Type=Unsigned32
_CiscoVdcGlobalResAvail_Object=MibTableColumn
ciscoVdcGlobalResAvail=_CiscoVdcGlobalResAvail_Object((1,3,6,1,4,1,9,9,774,1,4,1,1,6),_CiscoVdcGlobalResAvail_Type())
ciscoVdcGlobalResAvail.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoVdcGlobalResAvail.setStatus(_A)
_CiscoVdcGlobalResTotal_Type=Unsigned32
_CiscoVdcGlobalResTotal_Object=MibTableColumn
ciscoVdcGlobalResTotal=_CiscoVdcGlobalResTotal_Object((1,3,6,1,4,1,9,9,774,1,4,1,1,7),_CiscoVdcGlobalResTotal_Type())
ciscoVdcGlobalResTotal.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoVdcGlobalResTotal.setStatus(_A)
_CiscoVdcResUsageTable_Object=MibTable
ciscoVdcResUsageTable=_CiscoVdcResUsageTable_Object((1,3,6,1,4,1,9,9,774,1,4,2))
if mibBuilder.loadTexts:ciscoVdcResUsageTable.setStatus(_A)
_CiscoVdcResUsageEntry_Object=MibTableRow
ciscoVdcResUsageEntry=_CiscoVdcResUsageEntry_Object((1,3,6,1,4,1,9,9,774,1,4,2,1))
ciscoVdcResUsageEntry.setIndexNames((0,_B,_G),(0,_B,_S))
if mibBuilder.loadTexts:ciscoVdcResUsageEntry.setStatus(_A)
_CiscoVdcResID_Type=Unsigned32
_CiscoVdcResID_Object=MibTableColumn
ciscoVdcResID=_CiscoVdcResID_Object((1,3,6,1,4,1,9,9,774,1,4,2,1,1),_CiscoVdcResID_Type())
ciscoVdcResID.setMaxAccess(_H)
if mibBuilder.loadTexts:ciscoVdcResID.setStatus(_A)
_CiscoVdcResMin_Type=Unsigned32
_CiscoVdcResMin_Object=MibTableColumn
ciscoVdcResMin=_CiscoVdcResMin_Object((1,3,6,1,4,1,9,9,774,1,4,2,1,2),_CiscoVdcResMin_Type())
ciscoVdcResMin.setMaxAccess(_D)
if mibBuilder.loadTexts:ciscoVdcResMin.setStatus(_A)
_CiscoVdcResMax_Type=Unsigned32
_CiscoVdcResMax_Object=MibTableColumn
ciscoVdcResMax=_CiscoVdcResMax_Object((1,3,6,1,4,1,9,9,774,1,4,2,1,3),_CiscoVdcResMax_Type())
ciscoVdcResMax.setMaxAccess(_D)
if mibBuilder.loadTexts:ciscoVdcResMax.setStatus(_A)
_CiscoVdcResUsed_Type=Unsigned32
_CiscoVdcResUsed_Object=MibTableColumn
ciscoVdcResUsed=_CiscoVdcResUsed_Object((1,3,6,1,4,1,9,9,774,1,4,2,1,4),_CiscoVdcResUsed_Type())
ciscoVdcResUsed.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoVdcResUsed.setStatus(_A)
_CiscoVdcResUnused_Type=Unsigned32
_CiscoVdcResUnused_Object=MibTableColumn
ciscoVdcResUnused=_CiscoVdcResUnused_Object((1,3,6,1,4,1,9,9,774,1,4,2,1,5),_CiscoVdcResUnused_Type())
ciscoVdcResUnused.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoVdcResUnused.setStatus(_A)
_CiscoVdcResAvail_Type=Unsigned32
_CiscoVdcResAvail_Object=MibTableColumn
ciscoVdcResAvail=_CiscoVdcResAvail_Object((1,3,6,1,4,1,9,9,774,1,4,2,1,6),_CiscoVdcResAvail_Type())
ciscoVdcResAvail.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoVdcResAvail.setStatus(_A)
_CiscoVdcResTemplateTable_Object=MibTable
ciscoVdcResTemplateTable=_CiscoVdcResTemplateTable_Object((1,3,6,1,4,1,9,9,774,1,4,3))
if mibBuilder.loadTexts:ciscoVdcResTemplateTable.setStatus(_A)
_CiscoVdcResTemplateEntry_Object=MibTableRow
ciscoVdcResTemplateEntry=_CiscoVdcResTemplateEntry_Object((1,3,6,1,4,1,9,9,774,1,4,3,1))
ciscoVdcResTemplateEntry.setIndexNames((0,_B,_T),(0,_B,_U))
if mibBuilder.loadTexts:ciscoVdcResTemplateEntry.setStatus(_A)
_CiscoVdcResTemplateName_Type=SnmpAdminString
_CiscoVdcResTemplateName_Object=MibTableColumn
ciscoVdcResTemplateName=_CiscoVdcResTemplateName_Object((1,3,6,1,4,1,9,9,774,1,4,3,1,1),_CiscoVdcResTemplateName_Type())
ciscoVdcResTemplateName.setMaxAccess(_H)
if mibBuilder.loadTexts:ciscoVdcResTemplateName.setStatus(_A)
_CiscoVdcResTemplateResID_Type=Unsigned32
_CiscoVdcResTemplateResID_Object=MibTableColumn
ciscoVdcResTemplateResID=_CiscoVdcResTemplateResID_Object((1,3,6,1,4,1,9,9,774,1,4,3,1,2),_CiscoVdcResTemplateResID_Type())
ciscoVdcResTemplateResID.setMaxAccess(_H)
if mibBuilder.loadTexts:ciscoVdcResTemplateResID.setStatus(_A)
_CiscoVdcResTemplateMin_Type=Unsigned32
_CiscoVdcResTemplateMin_Object=MibTableColumn
ciscoVdcResTemplateMin=_CiscoVdcResTemplateMin_Object((1,3,6,1,4,1,9,9,774,1,4,3,1,3),_CiscoVdcResTemplateMin_Type())
ciscoVdcResTemplateMin.setMaxAccess(_E)
if mibBuilder.loadTexts:ciscoVdcResTemplateMin.setStatus(_A)
_CiscoVdcResTemplateMax_Type=Unsigned32
_CiscoVdcResTemplateMax_Object=MibTableColumn
ciscoVdcResTemplateMax=_CiscoVdcResTemplateMax_Object((1,3,6,1,4,1,9,9,774,1,4,3,1,4),_CiscoVdcResTemplateMax_Type())
ciscoVdcResTemplateMax.setMaxAccess(_E)
if mibBuilder.loadTexts:ciscoVdcResTemplateMax.setStatus(_A)
class _CiscoVdcResTemplateStorageType_Type(StorageType):defaultValue=2
_CiscoVdcResTemplateStorageType_Type.__name__=_I
_CiscoVdcResTemplateStorageType_Object=MibTableColumn
ciscoVdcResTemplateStorageType=_CiscoVdcResTemplateStorageType_Object((1,3,6,1,4,1,9,9,774,1,4,3,1,5),_CiscoVdcResTemplateStorageType_Type())
ciscoVdcResTemplateStorageType.setMaxAccess(_E)
if mibBuilder.loadTexts:ciscoVdcResTemplateStorageType.setStatus(_A)
_CiscoVdcResTemplateStatus_Type=RowStatus
_CiscoVdcResTemplateStatus_Object=MibTableColumn
ciscoVdcResTemplateStatus=_CiscoVdcResTemplateStatus_Object((1,3,6,1,4,1,9,9,774,1,4,3,1,6),_CiscoVdcResTemplateStatus_Type())
ciscoVdcResTemplateStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:ciscoVdcResTemplateStatus.setStatus(_A)
_CiscoVdcInterface_ObjectIdentity=ObjectIdentity
ciscoVdcInterface=_CiscoVdcInterface_ObjectIdentity((1,3,6,1,4,1,9,9,774,1,5))
_CiscoVdcIfMembershipTable_Object=MibTable
ciscoVdcIfMembershipTable=_CiscoVdcIfMembershipTable_Object((1,3,6,1,4,1,9,9,774,1,5,1))
if mibBuilder.loadTexts:ciscoVdcIfMembershipTable.setStatus(_A)
_CiscoVdcIfMembershipEntry_Object=MibTableRow
ciscoVdcIfMembershipEntry=_CiscoVdcIfMembershipEntry_Object((1,3,6,1,4,1,9,9,774,1,5,1,1))
ciscoVdcIfMembershipEntry.setIndexNames((0,_B,_G),(0,_B,_V))
if mibBuilder.loadTexts:ciscoVdcIfMembershipEntry.setStatus(_A)
_CiscoVdcIfMembershipifIndex_Type=InterfaceIndex
_CiscoVdcIfMembershipifIndex_Object=MibTableColumn
ciscoVdcIfMembershipifIndex=_CiscoVdcIfMembershipifIndex_Object((1,3,6,1,4,1,9,9,774,1,5,1,1,1),_CiscoVdcIfMembershipifIndex_Type())
ciscoVdcIfMembershipifIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:ciscoVdcIfMembershipifIndex.setStatus(_A)
class _CiscoVdcIfMembershipStorageType_Type(StorageType):defaultValue=2
_CiscoVdcIfMembershipStorageType_Type.__name__=_I
_CiscoVdcIfMembershipStorageType_Object=MibTableColumn
ciscoVdcIfMembershipStorageType=_CiscoVdcIfMembershipStorageType_Object((1,3,6,1,4,1,9,9,774,1,5,1,1,2),_CiscoVdcIfMembershipStorageType_Type())
ciscoVdcIfMembershipStorageType.setMaxAccess(_E)
if mibBuilder.loadTexts:ciscoVdcIfMembershipStorageType.setStatus(_A)
_CiscoVdcIfMembershipStatus_Type=RowStatus
_CiscoVdcIfMembershipStatus_Object=MibTableColumn
ciscoVdcIfMembershipStatus=_CiscoVdcIfMembershipStatus_Object((1,3,6,1,4,1,9,9,774,1,5,1,1,3),_CiscoVdcIfMembershipStatus_Type())
ciscoVdcIfMembershipStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:ciscoVdcIfMembershipStatus.setStatus(_A)
_CiscoVdcFCoEVlansTable_Object=MibTable
ciscoVdcFCoEVlansTable=_CiscoVdcFCoEVlansTable_Object((1,3,6,1,4,1,9,9,774,1,5,2))
if mibBuilder.loadTexts:ciscoVdcFCoEVlansTable.setStatus(_A)
_CiscoVdcFCoEVlansEntry_Object=MibTableRow
ciscoVdcFCoEVlansEntry=_CiscoVdcFCoEVlansEntry_Object((1,3,6,1,4,1,9,9,774,1,5,2,1))
ciscoVdcFCoEVlansEntry.setIndexNames((0,_B,_G))
if mibBuilder.loadTexts:ciscoVdcFCoEVlansEntry.setStatus(_A)
_CiscoVdcFCoEVlansFirst2K_Type=Cisco2KVlanList
_CiscoVdcFCoEVlansFirst2K_Object=MibTableColumn
ciscoVdcFCoEVlansFirst2K=_CiscoVdcFCoEVlansFirst2K_Object((1,3,6,1,4,1,9,9,774,1,5,2,1,1),_CiscoVdcFCoEVlansFirst2K_Type())
ciscoVdcFCoEVlansFirst2K.setMaxAccess(_D)
if mibBuilder.loadTexts:ciscoVdcFCoEVlansFirst2K.setStatus(_A)
_CiscoVdcFCoEVlansSecond2K_Type=Cisco2KVlanList
_CiscoVdcFCoEVlansSecond2K_Object=MibTableColumn
ciscoVdcFCoEVlansSecond2K=_CiscoVdcFCoEVlansSecond2K_Object((1,3,6,1,4,1,9,9,774,1,5,2,1,2),_CiscoVdcFCoEVlansSecond2K_Type())
ciscoVdcFCoEVlansSecond2K.setMaxAccess(_D)
if mibBuilder.loadTexts:ciscoVdcFCoEVlansSecond2K.setStatus(_A)
_CiscoVdcFCoEVlansFromVdc_Type=Unsigned32
_CiscoVdcFCoEVlansFromVdc_Object=MibTableColumn
ciscoVdcFCoEVlansFromVdc=_CiscoVdcFCoEVlansFromVdc_Object((1,3,6,1,4,1,9,9,774,1,5,2,1,3),_CiscoVdcFCoEVlansFromVdc_Type())
ciscoVdcFCoEVlansFromVdc.setMaxAccess(_D)
if mibBuilder.loadTexts:ciscoVdcFCoEVlansFromVdc.setStatus(_A)
_CiscoVdcSharedInterfaceTable_Object=MibTable
ciscoVdcSharedInterfaceTable=_CiscoVdcSharedInterfaceTable_Object((1,3,6,1,4,1,9,9,774,1,5,3))
if mibBuilder.loadTexts:ciscoVdcSharedInterfaceTable.setStatus(_A)
_CiscoVdcSharedInterfaceEntry_Object=MibTableRow
ciscoVdcSharedInterfaceEntry=_CiscoVdcSharedInterfaceEntry_Object((1,3,6,1,4,1,9,9,774,1,5,3,1))
ciscoVdcSharedInterfaceEntry.setIndexNames((0,_B,_G),(0,_B,_W))
if mibBuilder.loadTexts:ciscoVdcSharedInterfaceEntry.setStatus(_A)
_CiscoVdcSharedInterfaceifIndex_Type=InterfaceIndex
_CiscoVdcSharedInterfaceifIndex_Object=MibTableColumn
ciscoVdcSharedInterfaceifIndex=_CiscoVdcSharedInterfaceifIndex_Object((1,3,6,1,4,1,9,9,774,1,5,3,1,1),_CiscoVdcSharedInterfaceifIndex_Type())
ciscoVdcSharedInterfaceifIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:ciscoVdcSharedInterfaceifIndex.setStatus(_A)
class _CiscoVdcSharedInterfaceStorageType_Type(StorageType):defaultValue=2
_CiscoVdcSharedInterfaceStorageType_Type.__name__=_I
_CiscoVdcSharedInterfaceStorageType_Object=MibTableColumn
ciscoVdcSharedInterfaceStorageType=_CiscoVdcSharedInterfaceStorageType_Object((1,3,6,1,4,1,9,9,774,1,5,3,1,2),_CiscoVdcSharedInterfaceStorageType_Type())
ciscoVdcSharedInterfaceStorageType.setMaxAccess(_E)
if mibBuilder.loadTexts:ciscoVdcSharedInterfaceStorageType.setStatus(_A)
_CiscoVdcSharedInterfaceRowStatus_Type=RowStatus
_CiscoVdcSharedInterfaceRowStatus_Object=MibTableColumn
ciscoVdcSharedInterfaceRowStatus=_CiscoVdcSharedInterfaceRowStatus_Object((1,3,6,1,4,1,9,9,774,1,5,3,1,3),_CiscoVdcSharedInterfaceRowStatus_Type())
ciscoVdcSharedInterfaceRowStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:ciscoVdcSharedInterfaceRowStatus.setStatus(_A)
_CiscoVdcMIBConform_ObjectIdentity=ObjectIdentity
ciscoVdcMIBConform=_CiscoVdcMIBConform_ObjectIdentity((1,3,6,1,4,1,9,9,774,2))
_CiscoVdcMIBCompliances_ObjectIdentity=ObjectIdentity
ciscoVdcMIBCompliances=_CiscoVdcMIBCompliances_ObjectIdentity((1,3,6,1,4,1,9,9,774,2,1))
_CiscoVdcMIBGroups_ObjectIdentity=ObjectIdentity
ciscoVdcMIBGroups=_CiscoVdcMIBGroups_ObjectIdentity((1,3,6,1,4,1,9,9,774,2,2))
ciscoVdcGroup=ObjectGroup((1,3,6,1,4,1,9,9,774,2,2,1))
ciscoVdcGroup.setObjects(*((_B,_X),(_B,_Y),(_B,_Z),(_B,_a),(_B,_b),(_B,_c),(_B,_d)))
if mibBuilder.loadTexts:ciscoVdcGroup.setStatus(_A)
ciscoVdcExtGroup=ObjectGroup((1,3,6,1,4,1,9,9,774,2,2,2))
ciscoVdcExtGroup.setObjects(*((_B,_e),(_B,_f),(_B,_g),(_B,_h),(_B,_i),(_B,_j),(_B,_k),(_B,_l),(_B,_m),(_B,_n),(_B,_o),(_B,_p),(_B,_q),(_B,_r),(_B,_s),(_B,_t)))
if mibBuilder.loadTexts:ciscoVdcExtGroup.setStatus(_A)
ciscoVdcGlobalResUsageGroup=ObjectGroup((1,3,6,1,4,1,9,9,774,2,2,3))
ciscoVdcGlobalResUsageGroup.setObjects(*((_B,_u),(_B,_v),(_B,_w),(_B,_x),(_B,_y),(_B,_z)))
if mibBuilder.loadTexts:ciscoVdcGlobalResUsageGroup.setStatus(_A)
ciscoVdcResUsageGroup=ObjectGroup((1,3,6,1,4,1,9,9,774,2,2,4))
ciscoVdcResUsageGroup.setObjects(*((_B,_A0),(_B,_A1),(_B,_A2),(_B,_A3),(_B,_A4)))
if mibBuilder.loadTexts:ciscoVdcResUsageGroup.setStatus(_A)
ciscoVdcResTemplateGroup=ObjectGroup((1,3,6,1,4,1,9,9,774,2,2,5))
ciscoVdcResTemplateGroup.setObjects(*((_B,_A5),(_B,_A6),(_B,_A7),(_B,_A8)))
if mibBuilder.loadTexts:ciscoVdcResTemplateGroup.setStatus(_A)
ciscoVdcGlobalGroup=ObjectGroup((1,3,6,1,4,1,9,9,774,2,2,6))
ciscoVdcGlobalGroup.setObjects(*((_B,_A9),(_B,_AA)))
if mibBuilder.loadTexts:ciscoVdcGlobalGroup.setStatus(_A)
ciscoVdcIfMembershipGroup=ObjectGroup((1,3,6,1,4,1,9,9,774,2,2,7))
ciscoVdcIfMembershipGroup.setObjects(*((_B,_AB),(_B,_AC)))
if mibBuilder.loadTexts:ciscoVdcIfMembershipGroup.setStatus(_A)
ciscoVdcFCoEVlansGroup=ObjectGroup((1,3,6,1,4,1,9,9,774,2,2,8))
ciscoVdcFCoEVlansGroup.setObjects(*((_B,_AD),(_B,_AE),(_B,_AF)))
if mibBuilder.loadTexts:ciscoVdcFCoEVlansGroup.setStatus(_A)
ciscoVdcSharedInterfaceGroup=ObjectGroup((1,3,6,1,4,1,9,9,774,2,2,9))
ciscoVdcSharedInterfaceGroup.setObjects(*((_B,_AG),(_B,_AH)))
if mibBuilder.loadTexts:ciscoVdcSharedInterfaceGroup.setStatus(_A)
ciscoVdcMIBCompliance=ModuleCompliance((1,3,6,1,4,1,9,9,774,2,1,1))
ciscoVdcMIBCompliance.setObjects((_B,_L))
if mibBuilder.loadTexts:ciscoVdcMIBCompliance.setStatus('deprecated')
ciscoVdcMIBCompliance1=ModuleCompliance((1,3,6,1,4,1,9,9,774,2,1,2))
ciscoVdcMIBCompliance1.setObjects(*((_B,_L),(_B,_AI),(_B,_AJ),(_B,_AK),(_B,_AL),(_B,_AM),(_B,_AN),(_B,_AO),(_B,_AP)))
if mibBuilder.loadTexts:ciscoVdcMIBCompliance1.setStatus(_A)
mibBuilder.exportSymbols(_B,**{_K:CiscoVdcHaPolicy,'CiscoVdcPercentOrMinusOne':CiscoVdcPercentOrMinusOne,'ciscoVdcMIB':ciscoVdcMIB,'ciscoVdcMIBNotifs':ciscoVdcMIBNotifs,'ciscoVdcMIBObjects':ciscoVdcMIBObjects,'ciscoVdcTable':ciscoVdcTable,'ciscoVdcEntry':ciscoVdcEntry,_G:ciscoVdcId,_X:ciscoVdcName,_Y:ciscoVdcState,_Z:ciscoVdcFcoeCapable,_a:ciscoVdcMac,_b:ciscoVdcSwitchId,_c:ciscoVdcRowStatus,_d:ciscoVdcStorageType,'ciscoVdcGlobal':ciscoVdcGlobal,_A9:ciscoVdcMaxNumberVdcAllowed,_AA:ciscoVdcCombinedHostnameEnabled,'ciscoVdcExt':ciscoVdcExt,'ciscoVdcExtTable':ciscoVdcExtTable,'ciscoVdcExtEntry':ciscoVdcExtEntry,_e:ciscoVdcSingleSupHaPolicy,_f:ciscoVdcDualSupHaPolicy,_g:ciscoVdcBootOrder,_h:ciscoVdcTimeCreated,_i:ciscoVdcReloadCount,_j:ciscoVdcRestartCount,_k:ciscoVdcRestartTime,_l:ciscoVdcRestartReason,_m:ciscoVdcType,_n:ciscoVdcAdminStatus,_o:ciscoVdcFromUnallocatedIntf,_p:ciscoVdcFeatureSetList,_q:ciscoVdcResourceTemplate,_r:ciscoVdcModuleCapList,_s:ciscoVdcCpuPriority,_t:ciscoVdcCpuSharePercent,'ciscoVdcResource':ciscoVdcResource,'ciscoVdcGlobalResUsageTable':ciscoVdcGlobalResUsageTable,'ciscoVdcGlobalResUsageEntry':ciscoVdcGlobalResUsageEntry,_R:ciscoVdcGlobalResID,_u:ciscoVdcGlobalResName,_v:ciscoVdcGlobalResUsed,_w:ciscoVdcGlobalResUnused,_x:ciscoVdcGlobalResFree,_y:ciscoVdcGlobalResAvail,_z:ciscoVdcGlobalResTotal,'ciscoVdcResUsageTable':ciscoVdcResUsageTable,'ciscoVdcResUsageEntry':ciscoVdcResUsageEntry,_S:ciscoVdcResID,_A0:ciscoVdcResMin,_A1:ciscoVdcResMax,_A2:ciscoVdcResUsed,_A3:ciscoVdcResUnused,_A4:ciscoVdcResAvail,'ciscoVdcResTemplateTable':ciscoVdcResTemplateTable,'ciscoVdcResTemplateEntry':ciscoVdcResTemplateEntry,_T:ciscoVdcResTemplateName,_U:ciscoVdcResTemplateResID,_A5:ciscoVdcResTemplateMin,_A6:ciscoVdcResTemplateMax,_A8:ciscoVdcResTemplateStorageType,_A7:ciscoVdcResTemplateStatus,'ciscoVdcInterface':ciscoVdcInterface,'ciscoVdcIfMembershipTable':ciscoVdcIfMembershipTable,'ciscoVdcIfMembershipEntry':ciscoVdcIfMembershipEntry,_V:ciscoVdcIfMembershipifIndex,_AC:ciscoVdcIfMembershipStorageType,_AB:ciscoVdcIfMembershipStatus,'ciscoVdcFCoEVlansTable':ciscoVdcFCoEVlansTable,'ciscoVdcFCoEVlansEntry':ciscoVdcFCoEVlansEntry,_AD:ciscoVdcFCoEVlansFirst2K,_AE:ciscoVdcFCoEVlansSecond2K,_AF:ciscoVdcFCoEVlansFromVdc,'ciscoVdcSharedInterfaceTable':ciscoVdcSharedInterfaceTable,'ciscoVdcSharedInterfaceEntry':ciscoVdcSharedInterfaceEntry,_W:ciscoVdcSharedInterfaceifIndex,_AH:ciscoVdcSharedInterfaceStorageType,_AG:ciscoVdcSharedInterfaceRowStatus,'ciscoVdcMIBConform':ciscoVdcMIBConform,'ciscoVdcMIBCompliances':ciscoVdcMIBCompliances,'ciscoVdcMIBCompliance':ciscoVdcMIBCompliance,'ciscoVdcMIBCompliance1':ciscoVdcMIBCompliance1,'ciscoVdcMIBGroups':ciscoVdcMIBGroups,_L:ciscoVdcGroup,_AI:ciscoVdcExtGroup,_AJ:ciscoVdcGlobalResUsageGroup,_AK:ciscoVdcResUsageGroup,_AL:ciscoVdcResTemplateGroup,_AM:ciscoVdcGlobalGroup,_AN:ciscoVdcIfMembershipGroup,_AO:ciscoVdcFCoEVlansGroup,_AP:ciscoVdcSharedInterfaceGroup})