_m='ciceCfmMacEnableGroup'
_l='ciceCfmMipGroup'
_k='ciceCfmMaNetGroup'
_j='ciceCfmLtrConfigGroup'
_i='ciceCfmInterfaceGroup'
_h='ciceCfmGlobalObjectsGroup'
_g='ciceCfmMacEnableRowStatus'
_f='ciceCfmMacEnableStorageType'
_e='ciceCfmMipRowStatus'
_d='ciceCfmMipStorageType'
_c='ciceCfmMipMdLevel'
_b='ciceCfmIfState'
_a='ciceCfmMaNetLossThreshold'
_Z='ciceCfmMaNetCciDirection'
_Y='ciceCfmMaNetCciEnable'
_X='ciceCfmLtrSize'
_W='ciceCfmLtrHoldTime'
_V='ciceCfmLtrEnable'
_U='ciceCfmEnableFaultAlarm'
_T='ciceCfmLtmMulticastAddress'
_S='ciceCfmCcMulticastAddress'
_R='ciceCfmBrainAddress'
_Q='ciceCfmMaxMdLevel'
_P='ciceCfmEnable'
_O='ciceCfmMacEnableVlanIndex'
_N='ciceCfmMipVlanIndex'
_M='Unsigned32'
_L='Integer32'
_K='dot1agCfmMdIndex'
_J='dot1agCfmMaIndex'
_I='not-accessible'
_H='StorageType'
_G='IEEE8021-CFM-MIB'
_F='ciceCfmIfIndex'
_E='read-only'
_D='read-create'
_C='read-write'
_B='CISCO-IEEE8021-CFM-EXT-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
Dot1agCfmMpDirection,dot1agCfmMaIndex,dot1agCfmMdIndex=mibBuilder.importSymbols(_G,'Dot1agCfmMpDirection',_J,_K)
InterfaceIndex,=mibBuilder.importSymbols('IF-MIB','InterfaceIndex')
VlanId,=mibBuilder.importSymbols('Q-BRIDGE-MIB','VlanId')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_L,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_M,'iso')
DisplayString,MacAddress,PhysAddress,RowStatus,StorageType,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress','RowStatus',_H,'TextualConvention','TruthValue')
ciscoIeee8021CfmExtMIB=ModuleIdentity((1,3,6,1,4,1,9,9,679))
if mibBuilder.loadTexts:ciscoIeee8021CfmExtMIB.setRevisions(('2008-11-13 00:00',))
_CIeeeCfmExtMIBNotifs_ObjectIdentity=ObjectIdentity
cIeeeCfmExtMIBNotifs=_CIeeeCfmExtMIBNotifs_ObjectIdentity((1,3,6,1,4,1,9,9,679,0))
_CIeeeCfmExtMIBObjects_ObjectIdentity=ObjectIdentity
cIeeeCfmExtMIBObjects=_CIeeeCfmExtMIBObjects_ObjectIdentity((1,3,6,1,4,1,9,9,679,1))
_CiceCfmGlobal_ObjectIdentity=ObjectIdentity
ciceCfmGlobal=_CiceCfmGlobal_ObjectIdentity((1,3,6,1,4,1,9,9,679,1,1))
_CiceCfmEnable_Type=TruthValue
_CiceCfmEnable_Object=MibScalar
ciceCfmEnable=_CiceCfmEnable_Object((1,3,6,1,4,1,9,9,679,1,1,1),_CiceCfmEnable_Type())
ciceCfmEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:ciceCfmEnable.setStatus(_A)
_CiceCfmMaxMdLevel_Type=Unsigned32
_CiceCfmMaxMdLevel_Object=MibScalar
ciceCfmMaxMdLevel=_CiceCfmMaxMdLevel_Object((1,3,6,1,4,1,9,9,679,1,1,2),_CiceCfmMaxMdLevel_Type())
ciceCfmMaxMdLevel.setMaxAccess(_E)
if mibBuilder.loadTexts:ciceCfmMaxMdLevel.setStatus(_A)
_CiceCfmBrainAddress_Type=MacAddress
_CiceCfmBrainAddress_Object=MibScalar
ciceCfmBrainAddress=_CiceCfmBrainAddress_Object((1,3,6,1,4,1,9,9,679,1,1,3),_CiceCfmBrainAddress_Type())
ciceCfmBrainAddress.setMaxAccess(_E)
if mibBuilder.loadTexts:ciceCfmBrainAddress.setStatus(_A)
_CiceCfmCcMulticastAddress_Type=MacAddress
_CiceCfmCcMulticastAddress_Object=MibScalar
ciceCfmCcMulticastAddress=_CiceCfmCcMulticastAddress_Object((1,3,6,1,4,1,9,9,679,1,1,4),_CiceCfmCcMulticastAddress_Type())
ciceCfmCcMulticastAddress.setMaxAccess(_E)
if mibBuilder.loadTexts:ciceCfmCcMulticastAddress.setStatus(_A)
_CiceCfmLtmMulticastAddress_Type=MacAddress
_CiceCfmLtmMulticastAddress_Object=MibScalar
ciceCfmLtmMulticastAddress=_CiceCfmLtmMulticastAddress_Object((1,3,6,1,4,1,9,9,679,1,1,5),_CiceCfmLtmMulticastAddress_Type())
ciceCfmLtmMulticastAddress.setMaxAccess(_E)
if mibBuilder.loadTexts:ciceCfmLtmMulticastAddress.setStatus(_A)
_CiceCfmEnableFaultAlarm_Type=TruthValue
_CiceCfmEnableFaultAlarm_Object=MibScalar
ciceCfmEnableFaultAlarm=_CiceCfmEnableFaultAlarm_Object((1,3,6,1,4,1,9,9,679,1,1,6),_CiceCfmEnableFaultAlarm_Type())
ciceCfmEnableFaultAlarm.setMaxAccess(_C)
if mibBuilder.loadTexts:ciceCfmEnableFaultAlarm.setStatus(_A)
_CiceCfmLtr_ObjectIdentity=ObjectIdentity
ciceCfmLtr=_CiceCfmLtr_ObjectIdentity((1,3,6,1,4,1,9,9,679,1,2))
_CiceCfmLtrEnable_Type=TruthValue
_CiceCfmLtrEnable_Object=MibScalar
ciceCfmLtrEnable=_CiceCfmLtrEnable_Object((1,3,6,1,4,1,9,9,679,1,2,1),_CiceCfmLtrEnable_Type())
ciceCfmLtrEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:ciceCfmLtrEnable.setStatus(_A)
class _CiceCfmLtrHoldTime_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_CiceCfmLtrHoldTime_Type.__name__=_M
_CiceCfmLtrHoldTime_Object=MibScalar
ciceCfmLtrHoldTime=_CiceCfmLtrHoldTime_Object((1,3,6,1,4,1,9,9,679,1,2,2),_CiceCfmLtrHoldTime_Type())
ciceCfmLtrHoldTime.setMaxAccess(_C)
if mibBuilder.loadTexts:ciceCfmLtrHoldTime.setStatus(_A)
if mibBuilder.loadTexts:ciceCfmLtrHoldTime.setUnits('minutes')
_CiceCfmLtrSize_Type=Unsigned32
_CiceCfmLtrSize_Object=MibScalar
ciceCfmLtrSize=_CiceCfmLtrSize_Object((1,3,6,1,4,1,9,9,679,1,2,3),_CiceCfmLtrSize_Type())
ciceCfmLtrSize.setMaxAccess(_C)
if mibBuilder.loadTexts:ciceCfmLtrSize.setStatus(_A)
_CiceCfmMa_ObjectIdentity=ObjectIdentity
ciceCfmMa=_CiceCfmMa_ObjectIdentity((1,3,6,1,4,1,9,9,679,1,3))
_CiceCfmMaNetTable_Object=MibTable
ciceCfmMaNetTable=_CiceCfmMaNetTable_Object((1,3,6,1,4,1,9,9,679,1,3,1))
if mibBuilder.loadTexts:ciceCfmMaNetTable.setStatus(_A)
_CiceCfmMaNetEntry_Object=MibTableRow
ciceCfmMaNetEntry=_CiceCfmMaNetEntry_Object((1,3,6,1,4,1,9,9,679,1,3,1,1))
ciceCfmMaNetEntry.setIndexNames((0,_G,_K),(0,_G,_J))
if mibBuilder.loadTexts:ciceCfmMaNetEntry.setStatus(_A)
_CiceCfmMaNetCciEnable_Type=TruthValue
_CiceCfmMaNetCciEnable_Object=MibTableColumn
ciceCfmMaNetCciEnable=_CiceCfmMaNetCciEnable_Object((1,3,6,1,4,1,9,9,679,1,3,1,1,1),_CiceCfmMaNetCciEnable_Type())
ciceCfmMaNetCciEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:ciceCfmMaNetCciEnable.setStatus(_A)
_CiceCfmMaNetCciDirection_Type=Dot1agCfmMpDirection
_CiceCfmMaNetCciDirection_Object=MibTableColumn
ciceCfmMaNetCciDirection=_CiceCfmMaNetCciDirection_Object((1,3,6,1,4,1,9,9,679,1,3,1,1,2),_CiceCfmMaNetCciDirection_Type())
ciceCfmMaNetCciDirection.setMaxAccess(_C)
if mibBuilder.loadTexts:ciceCfmMaNetCciDirection.setStatus(_A)
_CiceCfmMaNetLossThreshold_Type=Unsigned32
_CiceCfmMaNetLossThreshold_Object=MibTableColumn
ciceCfmMaNetLossThreshold=_CiceCfmMaNetLossThreshold_Object((1,3,6,1,4,1,9,9,679,1,3,1,1,3),_CiceCfmMaNetLossThreshold_Type())
ciceCfmMaNetLossThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:ciceCfmMaNetLossThreshold.setStatus(_A)
_CiceCfmIfObjects_ObjectIdentity=ObjectIdentity
ciceCfmIfObjects=_CiceCfmIfObjects_ObjectIdentity((1,3,6,1,4,1,9,9,679,1,4))
_CiceCfmInterfaceTable_Object=MibTable
ciceCfmInterfaceTable=_CiceCfmInterfaceTable_Object((1,3,6,1,4,1,9,9,679,1,4,1))
if mibBuilder.loadTexts:ciceCfmInterfaceTable.setStatus(_A)
_CiceCfmInterfaceEntry_Object=MibTableRow
ciceCfmInterfaceEntry=_CiceCfmInterfaceEntry_Object((1,3,6,1,4,1,9,9,679,1,4,1,1))
ciceCfmInterfaceEntry.setIndexNames((0,_B,_F))
if mibBuilder.loadTexts:ciceCfmInterfaceEntry.setStatus(_A)
_CiceCfmIfIndex_Type=InterfaceIndex
_CiceCfmIfIndex_Object=MibTableColumn
ciceCfmIfIndex=_CiceCfmIfIndex_Object((1,3,6,1,4,1,9,9,679,1,4,1,1,1),_CiceCfmIfIndex_Type())
ciceCfmIfIndex.setMaxAccess(_I)
if mibBuilder.loadTexts:ciceCfmIfIndex.setStatus(_A)
class _CiceCfmIfState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('enable',1),('disable',2),('transparent',3)))
_CiceCfmIfState_Type.__name__=_L
_CiceCfmIfState_Object=MibTableColumn
ciceCfmIfState=_CiceCfmIfState_Object((1,3,6,1,4,1,9,9,679,1,4,1,1,2),_CiceCfmIfState_Type())
ciceCfmIfState.setMaxAccess(_C)
if mibBuilder.loadTexts:ciceCfmIfState.setStatus(_A)
_CiceCfmMipTable_Object=MibTable
ciceCfmMipTable=_CiceCfmMipTable_Object((1,3,6,1,4,1,9,9,679,1,4,2))
if mibBuilder.loadTexts:ciceCfmMipTable.setStatus(_A)
_CiceCfmMipEntry_Object=MibTableRow
ciceCfmMipEntry=_CiceCfmMipEntry_Object((1,3,6,1,4,1,9,9,679,1,4,2,1))
ciceCfmMipEntry.setIndexNames((0,_B,_F),(0,_B,_N))
if mibBuilder.loadTexts:ciceCfmMipEntry.setStatus(_A)
_CiceCfmMipVlanIndex_Type=VlanId
_CiceCfmMipVlanIndex_Object=MibTableColumn
ciceCfmMipVlanIndex=_CiceCfmMipVlanIndex_Object((1,3,6,1,4,1,9,9,679,1,4,2,1,1),_CiceCfmMipVlanIndex_Type())
ciceCfmMipVlanIndex.setMaxAccess(_I)
if mibBuilder.loadTexts:ciceCfmMipVlanIndex.setStatus(_A)
_CiceCfmMipMdLevel_Type=Unsigned32
_CiceCfmMipMdLevel_Object=MibTableColumn
ciceCfmMipMdLevel=_CiceCfmMipMdLevel_Object((1,3,6,1,4,1,9,9,679,1,4,2,1,2),_CiceCfmMipMdLevel_Type())
ciceCfmMipMdLevel.setMaxAccess(_D)
if mibBuilder.loadTexts:ciceCfmMipMdLevel.setStatus(_A)
class _CiceCfmMipStorageType_Type(StorageType):defaultValue=3
_CiceCfmMipStorageType_Type.__name__=_H
_CiceCfmMipStorageType_Object=MibTableColumn
ciceCfmMipStorageType=_CiceCfmMipStorageType_Object((1,3,6,1,4,1,9,9,679,1,4,2,1,3),_CiceCfmMipStorageType_Type())
ciceCfmMipStorageType.setMaxAccess(_D)
if mibBuilder.loadTexts:ciceCfmMipStorageType.setStatus(_A)
_CiceCfmMipRowStatus_Type=RowStatus
_CiceCfmMipRowStatus_Object=MibTableColumn
ciceCfmMipRowStatus=_CiceCfmMipRowStatus_Object((1,3,6,1,4,1,9,9,679,1,4,2,1,4),_CiceCfmMipRowStatus_Type())
ciceCfmMipRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:ciceCfmMipRowStatus.setStatus(_A)
_CiceCfmMacEnableIfTable_Object=MibTable
ciceCfmMacEnableIfTable=_CiceCfmMacEnableIfTable_Object((1,3,6,1,4,1,9,9,679,1,4,3))
if mibBuilder.loadTexts:ciceCfmMacEnableIfTable.setStatus(_A)
_CiceCfmMacEnableIfEntry_Object=MibTableRow
ciceCfmMacEnableIfEntry=_CiceCfmMacEnableIfEntry_Object((1,3,6,1,4,1,9,9,679,1,4,3,1))
ciceCfmMacEnableIfEntry.setIndexNames((0,_B,_F),(0,_B,_O))
if mibBuilder.loadTexts:ciceCfmMacEnableIfEntry.setStatus(_A)
_CiceCfmMacEnableVlanIndex_Type=VlanId
_CiceCfmMacEnableVlanIndex_Object=MibTableColumn
ciceCfmMacEnableVlanIndex=_CiceCfmMacEnableVlanIndex_Object((1,3,6,1,4,1,9,9,679,1,4,3,1,1),_CiceCfmMacEnableVlanIndex_Type())
ciceCfmMacEnableVlanIndex.setMaxAccess(_I)
if mibBuilder.loadTexts:ciceCfmMacEnableVlanIndex.setStatus(_A)
class _CiceCfmMacEnableStorageType_Type(StorageType):defaultValue=3
_CiceCfmMacEnableStorageType_Type.__name__=_H
_CiceCfmMacEnableStorageType_Object=MibTableColumn
ciceCfmMacEnableStorageType=_CiceCfmMacEnableStorageType_Object((1,3,6,1,4,1,9,9,679,1,4,3,1,2),_CiceCfmMacEnableStorageType_Type())
ciceCfmMacEnableStorageType.setMaxAccess(_D)
if mibBuilder.loadTexts:ciceCfmMacEnableStorageType.setStatus(_A)
_CiceCfmMacEnableRowStatus_Type=RowStatus
_CiceCfmMacEnableRowStatus_Object=MibTableColumn
ciceCfmMacEnableRowStatus=_CiceCfmMacEnableRowStatus_Object((1,3,6,1,4,1,9,9,679,1,4,3,1,3),_CiceCfmMacEnableRowStatus_Type())
ciceCfmMacEnableRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:ciceCfmMacEnableRowStatus.setStatus(_A)
_CiceCfmMep_ObjectIdentity=ObjectIdentity
ciceCfmMep=_CiceCfmMep_ObjectIdentity((1,3,6,1,4,1,9,9,679,1,5))
_CIeeeCfmExtMIBConformance_ObjectIdentity=ObjectIdentity
cIeeeCfmExtMIBConformance=_CIeeeCfmExtMIBConformance_ObjectIdentity((1,3,6,1,4,1,9,9,679,2))
_CiceCfmMIBCompliances_ObjectIdentity=ObjectIdentity
ciceCfmMIBCompliances=_CiceCfmMIBCompliances_ObjectIdentity((1,3,6,1,4,1,9,9,679,2,1))
_CiceCfmMIBGroups_ObjectIdentity=ObjectIdentity
ciceCfmMIBGroups=_CiceCfmMIBGroups_ObjectIdentity((1,3,6,1,4,1,9,9,679,2,2))
ciceCfmGlobalObjectsGroup=ObjectGroup((1,3,6,1,4,1,9,9,679,2,2,1))
ciceCfmGlobalObjectsGroup.setObjects(*((_B,_P),(_B,_Q),(_B,_R),(_B,_S),(_B,_T),(_B,_U)))
if mibBuilder.loadTexts:ciceCfmGlobalObjectsGroup.setStatus(_A)
ciceCfmLtrConfigGroup=ObjectGroup((1,3,6,1,4,1,9,9,679,2,2,2))
ciceCfmLtrConfigGroup.setObjects(*((_B,_V),(_B,_W),(_B,_X)))
if mibBuilder.loadTexts:ciceCfmLtrConfigGroup.setStatus(_A)
ciceCfmMaNetGroup=ObjectGroup((1,3,6,1,4,1,9,9,679,2,2,3))
ciceCfmMaNetGroup.setObjects(*((_B,_Y),(_B,_Z),(_B,_a)))
if mibBuilder.loadTexts:ciceCfmMaNetGroup.setStatus(_A)
ciceCfmInterfaceGroup=ObjectGroup((1,3,6,1,4,1,9,9,679,2,2,4))
ciceCfmInterfaceGroup.setObjects((_B,_b))
if mibBuilder.loadTexts:ciceCfmInterfaceGroup.setStatus(_A)
ciceCfmMipGroup=ObjectGroup((1,3,6,1,4,1,9,9,679,2,2,5))
ciceCfmMipGroup.setObjects(*((_B,_c),(_B,_d),(_B,_e)))
if mibBuilder.loadTexts:ciceCfmMipGroup.setStatus(_A)
ciceCfmMacEnableGroup=ObjectGroup((1,3,6,1,4,1,9,9,679,2,2,6))
ciceCfmMacEnableGroup.setObjects(*((_B,_f),(_B,_g)))
if mibBuilder.loadTexts:ciceCfmMacEnableGroup.setStatus(_A)
ciceCfmMIBCompliance=ModuleCompliance((1,3,6,1,4,1,9,9,679,2,1,1))
ciceCfmMIBCompliance.setObjects(*((_B,_h),(_B,_i),(_B,_j),(_B,_k),(_B,_l),(_B,_m)))
if mibBuilder.loadTexts:ciceCfmMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'ciscoIeee8021CfmExtMIB':ciscoIeee8021CfmExtMIB,'cIeeeCfmExtMIBNotifs':cIeeeCfmExtMIBNotifs,'cIeeeCfmExtMIBObjects':cIeeeCfmExtMIBObjects,'ciceCfmGlobal':ciceCfmGlobal,_P:ciceCfmEnable,_Q:ciceCfmMaxMdLevel,_R:ciceCfmBrainAddress,_S:ciceCfmCcMulticastAddress,_T:ciceCfmLtmMulticastAddress,_U:ciceCfmEnableFaultAlarm,'ciceCfmLtr':ciceCfmLtr,_V:ciceCfmLtrEnable,_W:ciceCfmLtrHoldTime,_X:ciceCfmLtrSize,'ciceCfmMa':ciceCfmMa,'ciceCfmMaNetTable':ciceCfmMaNetTable,'ciceCfmMaNetEntry':ciceCfmMaNetEntry,_Y:ciceCfmMaNetCciEnable,_Z:ciceCfmMaNetCciDirection,_a:ciceCfmMaNetLossThreshold,'ciceCfmIfObjects':ciceCfmIfObjects,'ciceCfmInterfaceTable':ciceCfmInterfaceTable,'ciceCfmInterfaceEntry':ciceCfmInterfaceEntry,_F:ciceCfmIfIndex,_b:ciceCfmIfState,'ciceCfmMipTable':ciceCfmMipTable,'ciceCfmMipEntry':ciceCfmMipEntry,_N:ciceCfmMipVlanIndex,_c:ciceCfmMipMdLevel,_d:ciceCfmMipStorageType,_e:ciceCfmMipRowStatus,'ciceCfmMacEnableIfTable':ciceCfmMacEnableIfTable,'ciceCfmMacEnableIfEntry':ciceCfmMacEnableIfEntry,_O:ciceCfmMacEnableVlanIndex,_f:ciceCfmMacEnableStorageType,_g:ciceCfmMacEnableRowStatus,'ciceCfmMep':ciceCfmMep,'cIeeeCfmExtMIBConformance':cIeeeCfmExtMIBConformance,'ciceCfmMIBCompliances':ciceCfmMIBCompliances,'ciceCfmMIBCompliance':ciceCfmMIBCompliance,'ciceCfmMIBGroups':ciceCfmMIBGroups,_h:ciceCfmGlobalObjectsGroup,_j:ciceCfmLtrConfigGroup,_k:ciceCfmMaNetGroup,_i:ciceCfmInterfaceGroup,_l:ciceCfmMipGroup,_m:ciceCfmMacEnableGroup})