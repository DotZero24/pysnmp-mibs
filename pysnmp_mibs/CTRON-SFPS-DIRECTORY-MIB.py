_A4='sfpsDirFilterAliasHashIndex'
_A3='sfpsDirFilterAliasBaseHash'
_A2='sfpsDirFilterAliasAliasHash'
_A1='sfpsDirFilterAliasLockCount'
_A0='locked-to-node'
_z='locked-to-port'
_y='sfpsDirFilterNodeLinkIndex'
_x='sfpsDirFilterNodeNodeIndex'
_w='sfpsDirFilterNodeLockCount'
_v='sfpsDirAliasStatsAliasType'
_u='sfpsDAPITestOutputIndex'
_t='delete'
_s='unlock'
_r='sfpsAliasDeltaTableIndex'
_q='inherited'
_p='sfpsAliasTableHashIndex'
_o='sfpsAliasTableBaseHash'
_n='sfpsAliasTableAliasHash'
_m='sfpsNodeTableHashIndex'
_l='sfpsNodeTableBaseHash'
_k='sfpsServiceCenterDirectoryHashLeaf'
_j='locked'
_i='hidden'
_h='local'
_g='remote'
_f='static'
_e='ipxRipEnet'
_d='ipxRipSnap'
_c='ipxRip8022'
_b='ipxSapEnet'
_a='ipxSapSnap'
_Z='ipxSap8022'
_Y='inetIPMask'
_X='netBiosName'
_W='hostName'
_V='vlan'
_U='empty'
_T='atDDP'
_S='macDXMcast'
_R='inetRIP'
_Q='inetRPC'
_P='inetIP'
_O='ipxIpx'
_N='inetUDP'
_M='inetYP'
_L='ipxRIP'
_K='ipxSap'
_J='macDX'
_I='true'
_H='false'
_G='unlocked'
_F='other'
_E='CTRON-SFPS-DIRECTORY-MIB'
_D='read-write'
_C='Integer32'
_B='read-only'
_A='mandatory'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
sfpsDirFilterAPI,sfpsServiceCenter,sfpsTopologyAliases,sfpsTopologyDAPI,sfpsTopologyDAPITest,sfpsTopologyDirStats,sfpsTopologyNodes,sfpsTopologyRemoteNodes=mibBuilder.importSymbols('CTRON-SFPS-INCLUDE-MIB','sfpsDirFilterAPI','sfpsServiceCenter','sfpsTopologyAliases','sfpsTopologyDAPI','sfpsTopologyDAPITest','sfpsTopologyDirStats','sfpsTopologyNodes','sfpsTopologyRemoteNodes')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
class SfpsSwitchPort(Integer32):0
class SfpsAddress(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(6,6));fixedLength=6
class HexInteger(Integer32):0
_SfpsServiceCenterDirectoryTable_Object=MibTable
sfpsServiceCenterDirectoryTable=_SfpsServiceCenterDirectoryTable_Object((1,3,6,1,4,1,52,4,2,4,2,2,2,4,3))
if mibBuilder.loadTexts:sfpsServiceCenterDirectoryTable.setStatus(_A)
_SfpsServiceCenterDirectoryEntry_Object=MibTableRow
sfpsServiceCenterDirectoryEntry=_SfpsServiceCenterDirectoryEntry_Object((1,3,6,1,4,1,52,4,2,4,2,2,2,4,3,1))
sfpsServiceCenterDirectoryEntry.setIndexNames((0,_E,_k))
if mibBuilder.loadTexts:sfpsServiceCenterDirectoryEntry.setStatus(_A)
_SfpsServiceCenterDirectoryHashLeaf_Type=HexInteger
_SfpsServiceCenterDirectoryHashLeaf_Object=MibTableColumn
sfpsServiceCenterDirectoryHashLeaf=_SfpsServiceCenterDirectoryHashLeaf_Object((1,3,6,1,4,1,52,4,2,4,2,2,2,4,3,1,1),_SfpsServiceCenterDirectoryHashLeaf_Type())
sfpsServiceCenterDirectoryHashLeaf.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsServiceCenterDirectoryHashLeaf.setStatus(_A)
_SfpsServiceCenterDirectoryMetric_Type=Integer32
_SfpsServiceCenterDirectoryMetric_Object=MibTableColumn
sfpsServiceCenterDirectoryMetric=_SfpsServiceCenterDirectoryMetric_Object((1,3,6,1,4,1,52,4,2,4,2,2,2,4,3,1,2),_SfpsServiceCenterDirectoryMetric_Type())
sfpsServiceCenterDirectoryMetric.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsServiceCenterDirectoryMetric.setStatus(_A)
_SfpsServiceCenterDirectoryName_Type=DisplayString
_SfpsServiceCenterDirectoryName_Object=MibTableColumn
sfpsServiceCenterDirectoryName=_SfpsServiceCenterDirectoryName_Object((1,3,6,1,4,1,52,4,2,4,2,2,2,4,3,1,3),_SfpsServiceCenterDirectoryName_Type())
sfpsServiceCenterDirectoryName.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsServiceCenterDirectoryName.setStatus(_A)
class _SfpsServiceCenterDirectoryOperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('kStatusRunning',1),('kStatusHalted',2),('kStatusPending',3),('kStatusFaulted',4),('kStatusNotStarted',5)))
_SfpsServiceCenterDirectoryOperStatus_Type.__name__=_C
_SfpsServiceCenterDirectoryOperStatus_Object=MibTableColumn
sfpsServiceCenterDirectoryOperStatus=_SfpsServiceCenterDirectoryOperStatus_Object((1,3,6,1,4,1,52,4,2,4,2,2,2,4,3,1,4),_SfpsServiceCenterDirectoryOperStatus_Type())
sfpsServiceCenterDirectoryOperStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsServiceCenterDirectoryOperStatus.setStatus(_A)
class _SfpsServiceCenterDirectoryAdminStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_F,1),('disable',2),('enable',3)))
_SfpsServiceCenterDirectoryAdminStatus_Type.__name__=_C
_SfpsServiceCenterDirectoryAdminStatus_Object=MibTableColumn
sfpsServiceCenterDirectoryAdminStatus=_SfpsServiceCenterDirectoryAdminStatus_Object((1,3,6,1,4,1,52,4,2,4,2,2,2,4,3,1,5),_SfpsServiceCenterDirectoryAdminStatus_Type())
sfpsServiceCenterDirectoryAdminStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:sfpsServiceCenterDirectoryAdminStatus.setStatus(_A)
_SfpsServiceCenterDirectoryStatusTime_Type=TimeTicks
_SfpsServiceCenterDirectoryStatusTime_Object=MibTableColumn
sfpsServiceCenterDirectoryStatusTime=_SfpsServiceCenterDirectoryStatusTime_Object((1,3,6,1,4,1,52,4,2,4,2,2,2,4,3,1,6),_SfpsServiceCenterDirectoryStatusTime_Type())
sfpsServiceCenterDirectoryStatusTime.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsServiceCenterDirectoryStatusTime.setStatus(_A)
_SfpsServiceCenterDirectoryRequests_Type=Integer32
_SfpsServiceCenterDirectoryRequests_Object=MibTableColumn
sfpsServiceCenterDirectoryRequests=_SfpsServiceCenterDirectoryRequests_Object((1,3,6,1,4,1,52,4,2,4,2,2,2,4,3,1,7),_SfpsServiceCenterDirectoryRequests_Type())
sfpsServiceCenterDirectoryRequests.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsServiceCenterDirectoryRequests.setStatus(_A)
_SfpsServiceCenterDirectoryResponses_Type=Integer32
_SfpsServiceCenterDirectoryResponses_Object=MibTableColumn
sfpsServiceCenterDirectoryResponses=_SfpsServiceCenterDirectoryResponses_Object((1,3,6,1,4,1,52,4,2,4,2,2,2,4,3,1,8),_SfpsServiceCenterDirectoryResponses_Type())
sfpsServiceCenterDirectoryResponses.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsServiceCenterDirectoryResponses.setStatus(_A)
_SfpsNodeTable_Object=MibTable
sfpsNodeTable=_SfpsNodeTable_Object((1,3,6,1,4,1,52,4,2,4,2,2,3,5,1))
if mibBuilder.loadTexts:sfpsNodeTable.setStatus(_A)
_SfpsNodeTableEntry_Object=MibTableRow
sfpsNodeTableEntry=_SfpsNodeTableEntry_Object((1,3,6,1,4,1,52,4,2,4,2,2,3,5,1,1))
sfpsNodeTableEntry.setIndexNames((0,_E,_l),(0,_E,_m))
if mibBuilder.loadTexts:sfpsNodeTableEntry.setStatus(_A)
_SfpsNodeTableBaseHash_Type=Integer32
_SfpsNodeTableBaseHash_Object=MibTableColumn
sfpsNodeTableBaseHash=_SfpsNodeTableBaseHash_Object((1,3,6,1,4,1,52,4,2,4,2,2,3,5,1,1,1),_SfpsNodeTableBaseHash_Type())
sfpsNodeTableBaseHash.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsNodeTableBaseHash.setStatus(_A)
_SfpsNodeTableHashIndex_Type=Integer32
_SfpsNodeTableHashIndex_Object=MibTableColumn
sfpsNodeTableHashIndex=_SfpsNodeTableHashIndex_Object((1,3,6,1,4,1,52,4,2,4,2,2,3,5,1,1,2),_SfpsNodeTableHashIndex_Type())
sfpsNodeTableHashIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsNodeTableHashIndex.setStatus(_A)
_SfpsNodeTableSwitchType_Type=DisplayString
_SfpsNodeTableSwitchType_Object=MibTableColumn
sfpsNodeTableSwitchType=_SfpsNodeTableSwitchType_Object((1,3,6,1,4,1,52,4,2,4,2,2,3,5,1,1,3),_SfpsNodeTableSwitchType_Type())
sfpsNodeTableSwitchType.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsNodeTableSwitchType.setStatus(_A)
_SfpsNodeTableSwitchAddress_Type=DisplayString
_SfpsNodeTableSwitchAddress_Object=MibTableColumn
sfpsNodeTableSwitchAddress=_SfpsNodeTableSwitchAddress_Object((1,3,6,1,4,1,52,4,2,4,2,2,3,5,1,1,4),_SfpsNodeTableSwitchAddress_Type())
sfpsNodeTableSwitchAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsNodeTableSwitchAddress.setStatus(_A)
_SfpsNodeTablePort_Type=Integer32
_SfpsNodeTablePort_Object=MibTableColumn
sfpsNodeTablePort=_SfpsNodeTablePort_Object((1,3,6,1,4,1,52,4,2,4,2,2,3,5,1,1,5),_SfpsNodeTablePort_Type())
sfpsNodeTablePort.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsNodeTablePort.setStatus(_A)
_SfpsNodeTableBaseType_Type=DisplayString
_SfpsNodeTableBaseType_Object=MibTableColumn
sfpsNodeTableBaseType=_SfpsNodeTableBaseType_Object((1,3,6,1,4,1,52,4,2,4,2,2,3,5,1,1,6),_SfpsNodeTableBaseType_Type())
sfpsNodeTableBaseType.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsNodeTableBaseType.setStatus(_A)
_SfpsNodeTableBaseAddress_Type=DisplayString
_SfpsNodeTableBaseAddress_Object=MibTableColumn
sfpsNodeTableBaseAddress=_SfpsNodeTableBaseAddress_Object((1,3,6,1,4,1,52,4,2,4,2,2,3,5,1,1,7),_SfpsNodeTableBaseAddress_Type())
sfpsNodeTableBaseAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsNodeTableBaseAddress.setStatus(_A)
_SfpsNodeTableEntryType_Type=DisplayString
_SfpsNodeTableEntryType_Object=MibTableColumn
sfpsNodeTableEntryType=_SfpsNodeTableEntryType_Object((1,3,6,1,4,1,52,4,2,4,2,2,3,5,1,1,8),_SfpsNodeTableEntryType_Type())
sfpsNodeTableEntryType.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsNodeTableEntryType.setStatus(_A)
_SfpsNodeTableCallTag_Type=HexInteger
_SfpsNodeTableCallTag_Object=MibTableColumn
sfpsNodeTableCallTag=_SfpsNodeTableCallTag_Object((1,3,6,1,4,1,52,4,2,4,2,2,3,5,1,1,9),_SfpsNodeTableCallTag_Type())
sfpsNodeTableCallTag.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsNodeTableCallTag.setStatus(_A)
_SfpsNodeTableLastHeard_Type=TimeTicks
_SfpsNodeTableLastHeard_Object=MibTableColumn
sfpsNodeTableLastHeard=_SfpsNodeTableLastHeard_Object((1,3,6,1,4,1,52,4,2,4,2,2,3,5,1,1,10),_SfpsNodeTableLastHeard_Type())
sfpsNodeTableLastHeard.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsNodeTableLastHeard.setStatus(_A)
_SfpsNodeTableAge_Type=TimeTicks
_SfpsNodeTableAge_Object=MibTableColumn
sfpsNodeTableAge=_SfpsNodeTableAge_Object((1,3,6,1,4,1,52,4,2,4,2,2,3,5,1,1,11),_SfpsNodeTableAge_Type())
sfpsNodeTableAge.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsNodeTableAge.setStatus(_A)
_SfpsNodeTableAliasCount_Type=Integer32
_SfpsNodeTableAliasCount_Object=MibTableColumn
sfpsNodeTableAliasCount=_SfpsNodeTableAliasCount_Object((1,3,6,1,4,1,52,4,2,4,2,2,3,5,1,1,12),_SfpsNodeTableAliasCount_Type())
sfpsNodeTableAliasCount.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsNodeTableAliasCount.setStatus(_A)
_SfpsNodeTableVlanCount_Type=Integer32
_SfpsNodeTableVlanCount_Object=MibTableColumn
sfpsNodeTableVlanCount=_SfpsNodeTableVlanCount_Object((1,3,6,1,4,1,52,4,2,4,2,2,3,5,1,1,13),_SfpsNodeTableVlanCount_Type())
sfpsNodeTableVlanCount.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsNodeTableVlanCount.setStatus(_A)
class _SfpsNodeTableNodeLocked_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_I,2)))
_SfpsNodeTableNodeLocked_Type.__name__=_C
_SfpsNodeTableNodeLocked_Object=MibTableColumn
sfpsNodeTableNodeLocked=_SfpsNodeTableNodeLocked_Object((1,3,6,1,4,1,52,4,2,4,2,2,3,5,1,1,14),_SfpsNodeTableNodeLocked_Type())
sfpsNodeTableNodeLocked.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsNodeTableNodeLocked.setStatus(_A)
class _SfpsNodeTableNodeLocal_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_I,2)))
_SfpsNodeTableNodeLocal_Type.__name__=_C
_SfpsNodeTableNodeLocal_Object=MibTableColumn
sfpsNodeTableNodeLocal=_SfpsNodeTableNodeLocal_Object((1,3,6,1,4,1,52,4,2,4,2,2,3,5,1,1,15),_SfpsNodeTableNodeLocal_Type())
sfpsNodeTableNodeLocal.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsNodeTableNodeLocal.setStatus(_A)
_SfpsNodeTableSelf_Type=Integer32
_SfpsNodeTableSelf_Object=MibTableColumn
sfpsNodeTableSelf=_SfpsNodeTableSelf_Object((1,3,6,1,4,1,52,4,2,4,2,2,3,5,1,1,16),_SfpsNodeTableSelf_Type())
sfpsNodeTableSelf.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsNodeTableSelf.setStatus(_A)
_SfpsNodeTableNext_Type=Integer32
_SfpsNodeTableNext_Object=MibTableColumn
sfpsNodeTableNext=_SfpsNodeTableNext_Object((1,3,6,1,4,1,52,4,2,4,2,2,3,5,1,1,17),_SfpsNodeTableNext_Type())
sfpsNodeTableNext.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsNodeTableNext.setStatus(_A)
_SfpsNodeTablePrev_Type=Integer32
_SfpsNodeTablePrev_Object=MibTableColumn
sfpsNodeTablePrev=_SfpsNodeTablePrev_Object((1,3,6,1,4,1,52,4,2,4,2,2,3,5,1,1,18),_SfpsNodeTablePrev_Type())
sfpsNodeTablePrev.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsNodeTablePrev.setStatus(_A)
_SfpsAliasTable_Object=MibTable
sfpsAliasTable=_SfpsAliasTable_Object((1,3,6,1,4,1,52,4,2,4,2,2,3,6,1))
if mibBuilder.loadTexts:sfpsAliasTable.setStatus(_A)
_SfpsAliasTableEntry_Object=MibTableRow
sfpsAliasTableEntry=_SfpsAliasTableEntry_Object((1,3,6,1,4,1,52,4,2,4,2,2,3,6,1,1))
sfpsAliasTableEntry.setIndexNames((0,_E,_n),(0,_E,_o),(0,_E,_p))
if mibBuilder.loadTexts:sfpsAliasTableEntry.setStatus(_A)
_SfpsAliasTableAliasHash_Type=Integer32
_SfpsAliasTableAliasHash_Object=MibTableColumn
sfpsAliasTableAliasHash=_SfpsAliasTableAliasHash_Object((1,3,6,1,4,1,52,4,2,4,2,2,3,6,1,1,1),_SfpsAliasTableAliasHash_Type())
sfpsAliasTableAliasHash.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsAliasTableAliasHash.setStatus(_A)
_SfpsAliasTableBaseHash_Type=Integer32
_SfpsAliasTableBaseHash_Object=MibTableColumn
sfpsAliasTableBaseHash=_SfpsAliasTableBaseHash_Object((1,3,6,1,4,1,52,4,2,4,2,2,3,6,1,1,2),_SfpsAliasTableBaseHash_Type())
sfpsAliasTableBaseHash.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsAliasTableBaseHash.setStatus(_A)
_SfpsAliasTableHashIndex_Type=Integer32
_SfpsAliasTableHashIndex_Object=MibTableColumn
sfpsAliasTableHashIndex=_SfpsAliasTableHashIndex_Object((1,3,6,1,4,1,52,4,2,4,2,2,3,6,1,1,3),_SfpsAliasTableHashIndex_Type())
sfpsAliasTableHashIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsAliasTableHashIndex.setStatus(_A)
_SfpsAliasTableSwitchType_Type=DisplayString
_SfpsAliasTableSwitchType_Object=MibTableColumn
sfpsAliasTableSwitchType=_SfpsAliasTableSwitchType_Object((1,3,6,1,4,1,52,4,2,4,2,2,3,6,1,1,4),_SfpsAliasTableSwitchType_Type())
sfpsAliasTableSwitchType.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsAliasTableSwitchType.setStatus(_A)
_SfpsAliasTableSwitchAddress_Type=DisplayString
_SfpsAliasTableSwitchAddress_Object=MibTableColumn
sfpsAliasTableSwitchAddress=_SfpsAliasTableSwitchAddress_Object((1,3,6,1,4,1,52,4,2,4,2,2,3,6,1,1,5),_SfpsAliasTableSwitchAddress_Type())
sfpsAliasTableSwitchAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsAliasTableSwitchAddress.setStatus(_A)
_SfpsAliasTablePort_Type=Integer32
_SfpsAliasTablePort_Object=MibTableColumn
sfpsAliasTablePort=_SfpsAliasTablePort_Object((1,3,6,1,4,1,52,4,2,4,2,2,3,6,1,1,6),_SfpsAliasTablePort_Type())
sfpsAliasTablePort.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsAliasTablePort.setStatus(_A)
_SfpsAliasTableBaseType_Type=DisplayString
_SfpsAliasTableBaseType_Object=MibTableColumn
sfpsAliasTableBaseType=_SfpsAliasTableBaseType_Object((1,3,6,1,4,1,52,4,2,4,2,2,3,6,1,1,7),_SfpsAliasTableBaseType_Type())
sfpsAliasTableBaseType.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsAliasTableBaseType.setStatus(_A)
_SfpsAliasTableBaseAddress_Type=DisplayString
_SfpsAliasTableBaseAddress_Object=MibTableColumn
sfpsAliasTableBaseAddress=_SfpsAliasTableBaseAddress_Object((1,3,6,1,4,1,52,4,2,4,2,2,3,6,1,1,8),_SfpsAliasTableBaseAddress_Type())
sfpsAliasTableBaseAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsAliasTableBaseAddress.setStatus(_A)
_SfpsAliasTableAliasType_Type=DisplayString
_SfpsAliasTableAliasType_Object=MibTableColumn
sfpsAliasTableAliasType=_SfpsAliasTableAliasType_Object((1,3,6,1,4,1,52,4,2,4,2,2,3,6,1,1,9),_SfpsAliasTableAliasType_Type())
sfpsAliasTableAliasType.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsAliasTableAliasType.setStatus(_A)
_SfpsAliasTableAliasAddress_Type=DisplayString
_SfpsAliasTableAliasAddress_Object=MibTableColumn
sfpsAliasTableAliasAddress=_SfpsAliasTableAliasAddress_Object((1,3,6,1,4,1,52,4,2,4,2,2,3,6,1,1,10),_SfpsAliasTableAliasAddress_Type())
sfpsAliasTableAliasAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsAliasTableAliasAddress.setStatus(_A)
_SfpsAliasTableAliasAge_Type=TimeTicks
_SfpsAliasTableAliasAge_Object=MibTableColumn
sfpsAliasTableAliasAge=_SfpsAliasTableAliasAge_Object((1,3,6,1,4,1,52,4,2,4,2,2,3,6,1,1,11),_SfpsAliasTableAliasAge_Type())
sfpsAliasTableAliasAge.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsAliasTableAliasAge.setStatus(_A)
_SfpsAliasTableSwitchOctets_Type=OctetString
_SfpsAliasTableSwitchOctets_Object=MibTableColumn
sfpsAliasTableSwitchOctets=_SfpsAliasTableSwitchOctets_Object((1,3,6,1,4,1,52,4,2,4,2,2,3,6,1,1,12),_SfpsAliasTableSwitchOctets_Type())
sfpsAliasTableSwitchOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsAliasTableSwitchOctets.setStatus(_A)
_SfpsAliasTableBaseOctets_Type=OctetString
_SfpsAliasTableBaseOctets_Object=MibTableColumn
sfpsAliasTableBaseOctets=_SfpsAliasTableBaseOctets_Object((1,3,6,1,4,1,52,4,2,4,2,2,3,6,1,1,13),_SfpsAliasTableBaseOctets_Type())
sfpsAliasTableBaseOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsAliasTableBaseOctets.setStatus(_A)
_SfpsAliasTableAliasOctets_Type=OctetString
_SfpsAliasTableAliasOctets_Object=MibTableColumn
sfpsAliasTableAliasOctets=_SfpsAliasTableAliasOctets_Object((1,3,6,1,4,1,52,4,2,4,2,2,3,6,1,1,14),_SfpsAliasTableAliasOctets_Type())
sfpsAliasTableAliasOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsAliasTableAliasOctets.setStatus(_A)
_SfpsAliasTableOpaqueTag_Type=OctetString
_SfpsAliasTableOpaqueTag_Object=MibTableColumn
sfpsAliasTableOpaqueTag=_SfpsAliasTableOpaqueTag_Object((1,3,6,1,4,1,52,4,2,4,2,2,3,6,1,1,15),_SfpsAliasTableOpaqueTag_Type())
sfpsAliasTableOpaqueTag.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsAliasTableOpaqueTag.setStatus(_A)
class _SfpsAliasTableVlanPolicy_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_F,1),(_q,2),('autoRegistered',3),(_f,4)))
_SfpsAliasTableVlanPolicy_Type.__name__=_C
_SfpsAliasTableVlanPolicy_Object=MibTableColumn
sfpsAliasTableVlanPolicy=_SfpsAliasTableVlanPolicy_Object((1,3,6,1,4,1,52,4,2,4,2,2,3,6,1,1,16),_SfpsAliasTableVlanPolicy_Type())
sfpsAliasTableVlanPolicy.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsAliasTableVlanPolicy.setStatus(_A)
class _SfpsAliasTableBaseLock_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_I,2)))
_SfpsAliasTableBaseLock_Type.__name__=_C
_SfpsAliasTableBaseLock_Object=MibTableColumn
sfpsAliasTableBaseLock=_SfpsAliasTableBaseLock_Object((1,3,6,1,4,1,52,4,2,4,2,2,3,6,1,1,17),_SfpsAliasTableBaseLock_Type())
sfpsAliasTableBaseLock.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsAliasTableBaseLock.setStatus(_A)
class _SfpsAliasTableAliasLock_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_I,2)))
_SfpsAliasTableAliasLock_Type.__name__=_C
_SfpsAliasTableAliasLock_Object=MibTableColumn
sfpsAliasTableAliasLock=_SfpsAliasTableAliasLock_Object((1,3,6,1,4,1,52,4,2,4,2,2,3,6,1,1,18),_SfpsAliasTableAliasLock_Type())
sfpsAliasTableAliasLock.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsAliasTableAliasLock.setStatus(_A)
class _SfpsAliasTableAliasState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_F,1),(_g,2),(_h,3),(_i,4)))
_SfpsAliasTableAliasState_Type.__name__=_C
_SfpsAliasTableAliasState_Object=MibTableColumn
sfpsAliasTableAliasState=_SfpsAliasTableAliasState_Object((1,3,6,1,4,1,52,4,2,4,2,2,3,6,1,1,19),_SfpsAliasTableAliasState_Type())
sfpsAliasTableAliasState.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsAliasTableAliasState.setStatus(_A)
_SfpsAliasTableSelf_Type=Integer32
_SfpsAliasTableSelf_Object=MibTableColumn
sfpsAliasTableSelf=_SfpsAliasTableSelf_Object((1,3,6,1,4,1,52,4,2,4,2,2,3,6,1,1,20),_SfpsAliasTableSelf_Type())
sfpsAliasTableSelf.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsAliasTableSelf.setStatus(_A)
_SfpsAliasTableNext_Type=Integer32
_SfpsAliasTableNext_Object=MibTableColumn
sfpsAliasTableNext=_SfpsAliasTableNext_Object((1,3,6,1,4,1,52,4,2,4,2,2,3,6,1,1,21),_SfpsAliasTableNext_Type())
sfpsAliasTableNext.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsAliasTableNext.setStatus(_A)
_SfpsAliasTablePrev_Type=Integer32
_SfpsAliasTablePrev_Object=MibTableColumn
sfpsAliasTablePrev=_SfpsAliasTablePrev_Object((1,3,6,1,4,1,52,4,2,4,2,2,3,6,1,1,22),_SfpsAliasTablePrev_Type())
sfpsAliasTablePrev.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsAliasTablePrev.setStatus(_A)
_SfpsAliasDeltaTable_Object=MibTable
sfpsAliasDeltaTable=_SfpsAliasDeltaTable_Object((1,3,6,1,4,1,52,4,2,4,2,2,3,6,2))
if mibBuilder.loadTexts:sfpsAliasDeltaTable.setStatus(_A)
_SfpsAliasDeltaTableEntry_Object=MibTableRow
sfpsAliasDeltaTableEntry=_SfpsAliasDeltaTableEntry_Object((1,3,6,1,4,1,52,4,2,4,2,2,3,6,2,1))
sfpsAliasDeltaTableEntry.setIndexNames((0,_E,_r))
if mibBuilder.loadTexts:sfpsAliasDeltaTableEntry.setStatus(_A)
_SfpsAliasDeltaTableIndex_Type=Integer32
_SfpsAliasDeltaTableIndex_Object=MibTableColumn
sfpsAliasDeltaTableIndex=_SfpsAliasDeltaTableIndex_Object((1,3,6,1,4,1,52,4,2,4,2,2,3,6,2,1,1),_SfpsAliasDeltaTableIndex_Type())
sfpsAliasDeltaTableIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsAliasDeltaTableIndex.setStatus(_A)
_SfpsAliasDeltaTablePort_Type=Integer32
_SfpsAliasDeltaTablePort_Object=MibTableColumn
sfpsAliasDeltaTablePort=_SfpsAliasDeltaTablePort_Object((1,3,6,1,4,1,52,4,2,4,2,2,3,6,2,1,2),_SfpsAliasDeltaTablePort_Type())
sfpsAliasDeltaTablePort.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsAliasDeltaTablePort.setStatus(_A)
_SfpsAliasDeltaTableBase_Type=SfpsAddress
_SfpsAliasDeltaTableBase_Object=MibTableColumn
sfpsAliasDeltaTableBase=_SfpsAliasDeltaTableBase_Object((1,3,6,1,4,1,52,4,2,4,2,2,3,6,2,1,3),_SfpsAliasDeltaTableBase_Type())
sfpsAliasDeltaTableBase.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsAliasDeltaTableBase.setStatus(_A)
_SfpsAliasDeltaTableAlias_Type=OctetString
_SfpsAliasDeltaTableAlias_Object=MibTableColumn
sfpsAliasDeltaTableAlias=_SfpsAliasDeltaTableAlias_Object((1,3,6,1,4,1,52,4,2,4,2,2,3,6,2,1,4),_SfpsAliasDeltaTableAlias_Type())
sfpsAliasDeltaTableAlias.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsAliasDeltaTableAlias.setStatus(_A)
_SfpsAliasDeltaTableAliasLength_Type=Integer32
_SfpsAliasDeltaTableAliasLength_Object=MibTableColumn
sfpsAliasDeltaTableAliasLength=_SfpsAliasDeltaTableAliasLength_Object((1,3,6,1,4,1,52,4,2,4,2,2,3,6,2,1,5),_SfpsAliasDeltaTableAliasLength_Type())
sfpsAliasDeltaTableAliasLength.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsAliasDeltaTableAliasLength.setStatus(_A)
_SfpsAliasDeltaTableOpaqueTag_Type=OctetString
_SfpsAliasDeltaTableOpaqueTag_Object=MibTableColumn
sfpsAliasDeltaTableOpaqueTag=_SfpsAliasDeltaTableOpaqueTag_Object((1,3,6,1,4,1,52,4,2,4,2,2,3,6,2,1,6),_SfpsAliasDeltaTableOpaqueTag_Type())
sfpsAliasDeltaTableOpaqueTag.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsAliasDeltaTableOpaqueTag.setStatus(_A)
class _SfpsAliasDeltaTableAliasState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_F,1),('added',2),('deleted',3)))
_SfpsAliasDeltaTableAliasState_Type.__name__=_C
_SfpsAliasDeltaTableAliasState_Object=MibTableColumn
sfpsAliasDeltaTableAliasState=_SfpsAliasDeltaTableAliasState_Object((1,3,6,1,4,1,52,4,2,4,2,2,3,6,2,1,7),_SfpsAliasDeltaTableAliasState_Type())
sfpsAliasDeltaTableAliasState.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsAliasDeltaTableAliasState.setStatus(_A)
class _SfpsAliasDeltaTableNodeLock_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_j,2)))
_SfpsAliasDeltaTableNodeLock_Type.__name__=_C
_SfpsAliasDeltaTableNodeLock_Object=MibTableColumn
sfpsAliasDeltaTableNodeLock=_SfpsAliasDeltaTableNodeLock_Object((1,3,6,1,4,1,52,4,2,4,2,2,3,6,2,1,8),_SfpsAliasDeltaTableNodeLock_Type())
sfpsAliasDeltaTableNodeLock.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsAliasDeltaTableNodeLock.setStatus(_A)
class _SfpsAliasDeltaTableAliasLock_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_j,2)))
_SfpsAliasDeltaTableAliasLock_Type.__name__=_C
_SfpsAliasDeltaTableAliasLock_Object=MibTableColumn
sfpsAliasDeltaTableAliasLock=_SfpsAliasDeltaTableAliasLock_Object((1,3,6,1,4,1,52,4,2,4,2,2,3,6,2,1,9),_SfpsAliasDeltaTableAliasLock_Type())
sfpsAliasDeltaTableAliasLock.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsAliasDeltaTableAliasLock.setStatus(_A)
_SfpsAliasDeltaTableTimestamp_Type=TimeTicks
_SfpsAliasDeltaTableTimestamp_Object=MibTableColumn
sfpsAliasDeltaTableTimestamp=_SfpsAliasDeltaTableTimestamp_Object((1,3,6,1,4,1,52,4,2,4,2,2,3,6,2,1,10),_SfpsAliasDeltaTableTimestamp_Type())
sfpsAliasDeltaTableTimestamp.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsAliasDeltaTableTimestamp.setStatus(_A)
_SfpsAliasDeltaCount_Type=Integer32
_SfpsAliasDeltaCount_Object=MibScalar
sfpsAliasDeltaCount=_SfpsAliasDeltaCount_Object((1,3,6,1,4,1,52,4,2,4,2,2,3,6,3),_SfpsAliasDeltaCount_Type())
sfpsAliasDeltaCount.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsAliasDeltaCount.setStatus(_A)
class _SfpsAliasDeltaSetBack_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('lock',1),(_s,2)))
_SfpsAliasDeltaSetBack_Type.__name__=_C
_SfpsAliasDeltaSetBack_Object=MibScalar
sfpsAliasDeltaSetBack=_SfpsAliasDeltaSetBack_Object((1,3,6,1,4,1,52,4,2,4,2,2,3,6,4),_SfpsAliasDeltaSetBack_Type())
sfpsAliasDeltaSetBack.setMaxAccess(_D)
if mibBuilder.loadTexts:sfpsAliasDeltaSetBack.setStatus(_A)
class _SfpsAliasDeltaFullFlag_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('full',1),('unfull',2)))
_SfpsAliasDeltaFullFlag_Type.__name__=_C
_SfpsAliasDeltaFullFlag_Object=MibScalar
sfpsAliasDeltaFullFlag=_SfpsAliasDeltaFullFlag_Object((1,3,6,1,4,1,52,4,2,4,2,2,3,6,5),_SfpsAliasDeltaFullFlag_Type())
sfpsAliasDeltaFullFlag.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsAliasDeltaFullFlag.setStatus(_A)
class _SfpsDAPITestVerb_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9)));namedValues=NamedValues(*((_F,1),('add',2),(_t,3),('resolve',4),('multiResolve',5),('fillDirectory',6),('ageDirectory',7),('mapVlanOnPort',8),('mapVlanOffPort',9)))
_SfpsDAPITestVerb_Type.__name__=_C
_SfpsDAPITestVerb_Object=MibScalar
sfpsDAPITestVerb=_SfpsDAPITestVerb_Object((1,3,6,1,4,1,52,4,2,4,2,2,3,9,1),_SfpsDAPITestVerb_Type())
sfpsDAPITestVerb.setMaxAccess(_D)
if mibBuilder.loadTexts:sfpsDAPITestVerb.setStatus(_A)
_SfpsDAPITestSwitchMac_Type=SfpsAddress
_SfpsDAPITestSwitchMac_Object=MibScalar
sfpsDAPITestSwitchMac=_SfpsDAPITestSwitchMac_Object((1,3,6,1,4,1,52,4,2,4,2,2,3,9,2),_SfpsDAPITestSwitchMac_Type())
sfpsDAPITestSwitchMac.setMaxAccess(_D)
if mibBuilder.loadTexts:sfpsDAPITestSwitchMac.setStatus(_A)
_SfpsDAPITestPort_Type=SfpsSwitchPort
_SfpsDAPITestPort_Object=MibScalar
sfpsDAPITestPort=_SfpsDAPITestPort_Object((1,3,6,1,4,1,52,4,2,4,2,2,3,9,3),_SfpsDAPITestPort_Type())
sfpsDAPITestPort.setMaxAccess(_D)
if mibBuilder.loadTexts:sfpsDAPITestPort.setStatus(_A)
class _SfpsDAPITestAddrOneTag_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22)));namedValues=NamedValues(*((_J,1),(_K,2),(_L,3),(_M,4),(_N,5),(_O,6),(_P,7),(_Q,8),(_R,9),(_S,10),(_T,11),(_U,12),(_V,13),(_W,14),(_X,15),(_Y,16),(_Z,17),(_a,18),(_b,19),(_c,20),(_d,21),(_e,22)))
_SfpsDAPITestAddrOneTag_Type.__name__=_C
_SfpsDAPITestAddrOneTag_Object=MibScalar
sfpsDAPITestAddrOneTag=_SfpsDAPITestAddrOneTag_Object((1,3,6,1,4,1,52,4,2,4,2,2,3,9,4),_SfpsDAPITestAddrOneTag_Type())
sfpsDAPITestAddrOneTag.setMaxAccess(_D)
if mibBuilder.loadTexts:sfpsDAPITestAddrOneTag.setStatus(_A)
_SfpsDAPITestAddrOneValue_Type=DisplayString
_SfpsDAPITestAddrOneValue_Object=MibScalar
sfpsDAPITestAddrOneValue=_SfpsDAPITestAddrOneValue_Object((1,3,6,1,4,1,52,4,2,4,2,2,3,9,5),_SfpsDAPITestAddrOneValue_Type())
sfpsDAPITestAddrOneValue.setMaxAccess(_D)
if mibBuilder.loadTexts:sfpsDAPITestAddrOneValue.setStatus(_A)
class _SfpsDAPITestAddrTwoTag_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22)));namedValues=NamedValues(*((_J,1),(_K,2),(_L,3),(_M,4),(_N,5),(_O,6),(_P,7),(_Q,8),(_R,9),(_S,10),(_T,11),(_U,12),(_V,13),(_W,14),(_X,15),(_Y,16),(_Z,17),(_a,18),(_b,19),(_c,20),(_d,21),(_e,22)))
_SfpsDAPITestAddrTwoTag_Type.__name__=_C
_SfpsDAPITestAddrTwoTag_Object=MibScalar
sfpsDAPITestAddrTwoTag=_SfpsDAPITestAddrTwoTag_Object((1,3,6,1,4,1,52,4,2,4,2,2,3,9,6),_SfpsDAPITestAddrTwoTag_Type())
sfpsDAPITestAddrTwoTag.setMaxAccess(_D)
if mibBuilder.loadTexts:sfpsDAPITestAddrTwoTag.setStatus(_A)
_SfpsDAPITestAddrTwoValue_Type=DisplayString
_SfpsDAPITestAddrTwoValue_Object=MibScalar
sfpsDAPITestAddrTwoValue=_SfpsDAPITestAddrTwoValue_Object((1,3,6,1,4,1,52,4,2,4,2,2,3,9,7),_SfpsDAPITestAddrTwoValue_Type())
sfpsDAPITestAddrTwoValue.setMaxAccess(_D)
if mibBuilder.loadTexts:sfpsDAPITestAddrTwoValue.setStatus(_A)
_SfpsDAPITestCallTag_Type=Integer32
_SfpsDAPITestCallTag_Object=MibScalar
sfpsDAPITestCallTag=_SfpsDAPITestCallTag_Object((1,3,6,1,4,1,52,4,2,4,2,2,3,9,8),_SfpsDAPITestCallTag_Type())
sfpsDAPITestCallTag.setMaxAccess(_D)
if mibBuilder.loadTexts:sfpsDAPITestCallTag.setStatus(_A)
_SfpsDAPITestOutputTable_Object=MibTable
sfpsDAPITestOutputTable=_SfpsDAPITestOutputTable_Object((1,3,6,1,4,1,52,4,2,4,2,2,3,9,9))
if mibBuilder.loadTexts:sfpsDAPITestOutputTable.setStatus(_A)
_SfpsDAPITestOutputEntry_Object=MibTableRow
sfpsDAPITestOutputEntry=_SfpsDAPITestOutputEntry_Object((1,3,6,1,4,1,52,4,2,4,2,2,3,9,9,1))
sfpsDAPITestOutputEntry.setIndexNames((0,_E,_u))
if mibBuilder.loadTexts:sfpsDAPITestOutputEntry.setStatus(_A)
_SfpsDAPITestOutputIndex_Type=Integer32
_SfpsDAPITestOutputIndex_Object=MibTableColumn
sfpsDAPITestOutputIndex=_SfpsDAPITestOutputIndex_Object((1,3,6,1,4,1,52,4,2,4,2,2,3,9,9,1,1),_SfpsDAPITestOutputIndex_Type())
sfpsDAPITestOutputIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsDAPITestOutputIndex.setStatus(_A)
_SfpsDAPITestOutputSwitchMac_Type=SfpsAddress
_SfpsDAPITestOutputSwitchMac_Object=MibTableColumn
sfpsDAPITestOutputSwitchMac=_SfpsDAPITestOutputSwitchMac_Object((1,3,6,1,4,1,52,4,2,4,2,2,3,9,9,1,2),_SfpsDAPITestOutputSwitchMac_Type())
sfpsDAPITestOutputSwitchMac.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsDAPITestOutputSwitchMac.setStatus(_A)
_SfpsDAPITestOutputPort_Type=Integer32
_SfpsDAPITestOutputPort_Object=MibTableColumn
sfpsDAPITestOutputPort=_SfpsDAPITestOutputPort_Object((1,3,6,1,4,1,52,4,2,4,2,2,3,9,9,1,3),_SfpsDAPITestOutputPort_Type())
sfpsDAPITestOutputPort.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsDAPITestOutputPort.setStatus(_A)
class _SfpsDAPITestOutputAddrOneTag_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22)));namedValues=NamedValues(*((_J,1),(_K,2),(_L,3),(_M,4),(_N,5),(_O,6),(_P,7),(_Q,8),(_R,9),(_S,10),(_T,11),(_U,12),(_V,13),(_W,14),(_X,15),(_Y,16),(_Z,17),(_a,18),(_b,19),(_c,20),(_d,21),(_e,22)))
_SfpsDAPITestOutputAddrOneTag_Type.__name__=_C
_SfpsDAPITestOutputAddrOneTag_Object=MibTableColumn
sfpsDAPITestOutputAddrOneTag=_SfpsDAPITestOutputAddrOneTag_Object((1,3,6,1,4,1,52,4,2,4,2,2,3,9,9,1,4),_SfpsDAPITestOutputAddrOneTag_Type())
sfpsDAPITestOutputAddrOneTag.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsDAPITestOutputAddrOneTag.setStatus(_A)
_SfpsDAPITestOutputAddrOneValue_Type=DisplayString
_SfpsDAPITestOutputAddrOneValue_Object=MibTableColumn
sfpsDAPITestOutputAddrOneValue=_SfpsDAPITestOutputAddrOneValue_Object((1,3,6,1,4,1,52,4,2,4,2,2,3,9,9,1,5),_SfpsDAPITestOutputAddrOneValue_Type())
sfpsDAPITestOutputAddrOneValue.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsDAPITestOutputAddrOneValue.setStatus(_A)
class _SfpsDAPITestOutputAddrTwoTag_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22)));namedValues=NamedValues(*((_J,1),(_K,2),(_L,3),(_M,4),(_N,5),(_O,6),(_P,7),(_Q,8),(_R,9),(_S,10),(_T,11),(_U,12),(_V,13),(_W,14),(_X,15),(_Y,16),(_Z,17),(_a,18),(_b,19),(_c,20),(_d,21),(_e,22)))
_SfpsDAPITestOutputAddrTwoTag_Type.__name__=_C
_SfpsDAPITestOutputAddrTwoTag_Object=MibTableColumn
sfpsDAPITestOutputAddrTwoTag=_SfpsDAPITestOutputAddrTwoTag_Object((1,3,6,1,4,1,52,4,2,4,2,2,3,9,9,1,6),_SfpsDAPITestOutputAddrTwoTag_Type())
sfpsDAPITestOutputAddrTwoTag.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsDAPITestOutputAddrTwoTag.setStatus(_A)
_SfpsDAPITestOutputAddrTwoValue_Type=DisplayString
_SfpsDAPITestOutputAddrTwoValue_Object=MibTableColumn
sfpsDAPITestOutputAddrTwoValue=_SfpsDAPITestOutputAddrTwoValue_Object((1,3,6,1,4,1,52,4,2,4,2,2,3,9,9,1,7),_SfpsDAPITestOutputAddrTwoValue_Type())
sfpsDAPITestOutputAddrTwoValue.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsDAPITestOutputAddrTwoValue.setStatus(_A)
_SfpsDAPITestOutputCallTag_Type=Integer32
_SfpsDAPITestOutputCallTag_Object=MibTableColumn
sfpsDAPITestOutputCallTag=_SfpsDAPITestOutputCallTag_Object((1,3,6,1,4,1,52,4,2,4,2,2,3,9,9,1,8),_SfpsDAPITestOutputCallTag_Type())
sfpsDAPITestOutputCallTag.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsDAPITestOutputCallTag.setStatus(_A)
class _SfpsDAPIVerb_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12)));namedValues=NamedValues(*((_F,1),('add',2),(_t,3),('clearPort',4),('clearPortLocals',5),('clearSwitchRefs',6),('lockNode',7),('unlockNode',8),('restrictPort',9),('unrestrictPort',10),('ageNodes',11),('ageAliases',12)))
_SfpsDAPIVerb_Type.__name__=_C
_SfpsDAPIVerb_Object=MibScalar
sfpsDAPIVerb=_SfpsDAPIVerb_Object((1,3,6,1,4,1,52,4,2,4,2,2,3,10,1),_SfpsDAPIVerb_Type())
sfpsDAPIVerb.setMaxAccess(_D)
if mibBuilder.loadTexts:sfpsDAPIVerb.setStatus(_A)
_SfpsDAPIPort_Type=Integer32
_SfpsDAPIPort_Object=MibScalar
sfpsDAPIPort=_SfpsDAPIPort_Object((1,3,6,1,4,1,52,4,2,4,2,2,3,10,2),_SfpsDAPIPort_Type())
sfpsDAPIPort.setMaxAccess(_D)
if mibBuilder.loadTexts:sfpsDAPIPort.setStatus(_A)
_SfpsDAPINodeType_Type=OctetString
_SfpsDAPINodeType_Object=MibScalar
sfpsDAPINodeType=_SfpsDAPINodeType_Object((1,3,6,1,4,1,52,4,2,4,2,2,3,10,3),_SfpsDAPINodeType_Type())
sfpsDAPINodeType.setMaxAccess(_D)
if mibBuilder.loadTexts:sfpsDAPINodeType.setStatus(_A)
_SfpsDAPINodeValue_Type=OctetString
_SfpsDAPINodeValue_Object=MibScalar
sfpsDAPINodeValue=_SfpsDAPINodeValue_Object((1,3,6,1,4,1,52,4,2,4,2,2,3,10,4),_SfpsDAPINodeValue_Type())
sfpsDAPINodeValue.setMaxAccess(_D)
if mibBuilder.loadTexts:sfpsDAPINodeValue.setStatus(_A)
_SfpsDAPIAliasType_Type=OctetString
_SfpsDAPIAliasType_Object=MibScalar
sfpsDAPIAliasType=_SfpsDAPIAliasType_Object((1,3,6,1,4,1,52,4,2,4,2,2,3,10,5),_SfpsDAPIAliasType_Type())
sfpsDAPIAliasType.setMaxAccess(_D)
if mibBuilder.loadTexts:sfpsDAPIAliasType.setStatus(_A)
_SfpsDAPIAliasValue_Type=OctetString
_SfpsDAPIAliasValue_Object=MibScalar
sfpsDAPIAliasValue=_SfpsDAPIAliasValue_Object((1,3,6,1,4,1,52,4,2,4,2,2,3,10,6),_SfpsDAPIAliasValue_Type())
sfpsDAPIAliasValue.setMaxAccess(_D)
if mibBuilder.loadTexts:sfpsDAPIAliasValue.setStatus(_A)
_SfpsDAPIAge_Type=Integer32
_SfpsDAPIAge_Object=MibScalar
sfpsDAPIAge=_SfpsDAPIAge_Object((1,3,6,1,4,1,52,4,2,4,2,2,3,10,7),_SfpsDAPIAge_Type())
sfpsDAPIAge.setMaxAccess(_D)
if mibBuilder.loadTexts:sfpsDAPIAge.setStatus(_A)
_SfpsTopologyDirStatsTotalUsage_Type=Integer32
_SfpsTopologyDirStatsTotalUsage_Object=MibScalar
sfpsTopologyDirStatsTotalUsage=_SfpsTopologyDirStatsTotalUsage_Object((1,3,6,1,4,1,52,4,2,4,2,2,3,11,1),_SfpsTopologyDirStatsTotalUsage_Type())
sfpsTopologyDirStatsTotalUsage.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsTopologyDirStatsTotalUsage.setStatus(_A)
_SfpsTopologyDirStatsDynamicUsage_Type=Integer32
_SfpsTopologyDirStatsDynamicUsage_Object=MibScalar
sfpsTopologyDirStatsDynamicUsage=_SfpsTopologyDirStatsDynamicUsage_Object((1,3,6,1,4,1,52,4,2,4,2,2,3,11,2),_SfpsTopologyDirStatsDynamicUsage_Type())
sfpsTopologyDirStatsDynamicUsage.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsTopologyDirStatsDynamicUsage.setStatus(_A)
_SfpsTopologyDirStatsNumOfNodes_Type=Integer32
_SfpsTopologyDirStatsNumOfNodes_Object=MibScalar
sfpsTopologyDirStatsNumOfNodes=_SfpsTopologyDirStatsNumOfNodes_Object((1,3,6,1,4,1,52,4,2,4,2,2,3,11,3),_SfpsTopologyDirStatsNumOfNodes_Type())
sfpsTopologyDirStatsNumOfNodes.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsTopologyDirStatsNumOfNodes.setStatus(_A)
_SfpsTopologyDirStatsNodeUsage_Type=Integer32
_SfpsTopologyDirStatsNodeUsage_Object=MibScalar
sfpsTopologyDirStatsNodeUsage=_SfpsTopologyDirStatsNodeUsage_Object((1,3,6,1,4,1,52,4,2,4,2,2,3,11,4),_SfpsTopologyDirStatsNodeUsage_Type())
sfpsTopologyDirStatsNodeUsage.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsTopologyDirStatsNodeUsage.setStatus(_A)
_SfpsTopologyDirStatsNumLocalNodes_Type=Integer32
_SfpsTopologyDirStatsNumLocalNodes_Object=MibScalar
sfpsTopologyDirStatsNumLocalNodes=_SfpsTopologyDirStatsNumLocalNodes_Object((1,3,6,1,4,1,52,4,2,4,2,2,3,11,5),_SfpsTopologyDirStatsNumLocalNodes_Type())
sfpsTopologyDirStatsNumLocalNodes.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsTopologyDirStatsNumLocalNodes.setStatus(_A)
_SfpsTopologyDirStatsLocalNodeUsage_Type=Integer32
_SfpsTopologyDirStatsLocalNodeUsage_Object=MibScalar
sfpsTopologyDirStatsLocalNodeUsage=_SfpsTopologyDirStatsLocalNodeUsage_Object((1,3,6,1,4,1,52,4,2,4,2,2,3,11,6),_SfpsTopologyDirStatsLocalNodeUsage_Type())
sfpsTopologyDirStatsLocalNodeUsage.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsTopologyDirStatsLocalNodeUsage.setStatus(_A)
_SfpsTopologyDirStatsMaxLocalNodes_Type=Integer32
_SfpsTopologyDirStatsMaxLocalNodes_Object=MibScalar
sfpsTopologyDirStatsMaxLocalNodes=_SfpsTopologyDirStatsMaxLocalNodes_Object((1,3,6,1,4,1,52,4,2,4,2,2,3,11,7),_SfpsTopologyDirStatsMaxLocalNodes_Type())
sfpsTopologyDirStatsMaxLocalNodes.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsTopologyDirStatsMaxLocalNodes.setStatus(_A)
_SfpsTopologyDirStatsNumRemoteNodes_Type=Integer32
_SfpsTopologyDirStatsNumRemoteNodes_Object=MibScalar
sfpsTopologyDirStatsNumRemoteNodes=_SfpsTopologyDirStatsNumRemoteNodes_Object((1,3,6,1,4,1,52,4,2,4,2,2,3,11,8),_SfpsTopologyDirStatsNumRemoteNodes_Type())
sfpsTopologyDirStatsNumRemoteNodes.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsTopologyDirStatsNumRemoteNodes.setStatus(_A)
_SfpsTopologyDirStatsRemoteNodeUsage_Type=Integer32
_SfpsTopologyDirStatsRemoteNodeUsage_Object=MibScalar
sfpsTopologyDirStatsRemoteNodeUsage=_SfpsTopologyDirStatsRemoteNodeUsage_Object((1,3,6,1,4,1,52,4,2,4,2,2,3,11,9),_SfpsTopologyDirStatsRemoteNodeUsage_Type())
sfpsTopologyDirStatsRemoteNodeUsage.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsTopologyDirStatsRemoteNodeUsage.setStatus(_A)
_SfpsTopologyDirStatsMaxRemoteNodes_Type=Integer32
_SfpsTopologyDirStatsMaxRemoteNodes_Object=MibScalar
sfpsTopologyDirStatsMaxRemoteNodes=_SfpsTopologyDirStatsMaxRemoteNodes_Object((1,3,6,1,4,1,52,4,2,4,2,2,3,11,10),_SfpsTopologyDirStatsMaxRemoteNodes_Type())
sfpsTopologyDirStatsMaxRemoteNodes.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsTopologyDirStatsMaxRemoteNodes.setStatus(_A)
_SfpsTopologyDirStatsNumOfAliases_Type=Integer32
_SfpsTopologyDirStatsNumOfAliases_Object=MibScalar
sfpsTopologyDirStatsNumOfAliases=_SfpsTopologyDirStatsNumOfAliases_Object((1,3,6,1,4,1,52,4,2,4,2,2,3,11,11),_SfpsTopologyDirStatsNumOfAliases_Type())
sfpsTopologyDirStatsNumOfAliases.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsTopologyDirStatsNumOfAliases.setStatus(_A)
_SfpsTopologyDirStatsAliasUsage_Type=Integer32
_SfpsTopologyDirStatsAliasUsage_Object=MibScalar
sfpsTopologyDirStatsAliasUsage=_SfpsTopologyDirStatsAliasUsage_Object((1,3,6,1,4,1,52,4,2,4,2,2,3,11,12),_SfpsTopologyDirStatsAliasUsage_Type())
sfpsTopologyDirStatsAliasUsage.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsTopologyDirStatsAliasUsage.setStatus(_A)
_SfpsDirAliasStatsTable_Object=MibTable
sfpsDirAliasStatsTable=_SfpsDirAliasStatsTable_Object((1,3,6,1,4,1,52,4,2,4,2,2,3,11,13))
if mibBuilder.loadTexts:sfpsDirAliasStatsTable.setStatus(_A)
_SfpsDirAliasStatsEntry_Object=MibTableRow
sfpsDirAliasStatsEntry=_SfpsDirAliasStatsEntry_Object((1,3,6,1,4,1,52,4,2,4,2,2,3,11,13,1))
sfpsDirAliasStatsEntry.setIndexNames((0,_E,_v))
if mibBuilder.loadTexts:sfpsDirAliasStatsEntry.setStatus(_A)
_SfpsDirAliasStatsAliasType_Type=Integer32
_SfpsDirAliasStatsAliasType_Object=MibTableColumn
sfpsDirAliasStatsAliasType=_SfpsDirAliasStatsAliasType_Object((1,3,6,1,4,1,52,4,2,4,2,2,3,11,13,1,1),_SfpsDirAliasStatsAliasType_Type())
sfpsDirAliasStatsAliasType.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsDirAliasStatsAliasType.setStatus(_A)
_SfpsDirAliasStatsAliasName_Type=DisplayString
_SfpsDirAliasStatsAliasName_Object=MibTableColumn
sfpsDirAliasStatsAliasName=_SfpsDirAliasStatsAliasName_Object((1,3,6,1,4,1,52,4,2,4,2,2,3,11,13,1,2),_SfpsDirAliasStatsAliasName_Type())
sfpsDirAliasStatsAliasName.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsDirAliasStatsAliasName.setStatus(_A)
_SfpsDirAliasStatsNumOfAliases_Type=Integer32
_SfpsDirAliasStatsNumOfAliases_Object=MibTableColumn
sfpsDirAliasStatsNumOfAliases=_SfpsDirAliasStatsNumOfAliases_Object((1,3,6,1,4,1,52,4,2,4,2,2,3,11,13,1,3),_SfpsDirAliasStatsNumOfAliases_Type())
sfpsDirAliasStatsNumOfAliases.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsDirAliasStatsNumOfAliases.setStatus(_A)
_SfpsDirAliasStatsAliasUsage_Type=Integer32
_SfpsDirAliasStatsAliasUsage_Object=MibTableColumn
sfpsDirAliasStatsAliasUsage=_SfpsDirAliasStatsAliasUsage_Object((1,3,6,1,4,1,52,4,2,4,2,2,3,11,13,1,4),_SfpsDirAliasStatsAliasUsage_Type())
sfpsDirAliasStatsAliasUsage.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsDirAliasStatsAliasUsage.setStatus(_A)
_SfpsDirAliasStatsMaxAliases_Type=Integer32
_SfpsDirAliasStatsMaxAliases_Object=MibTableColumn
sfpsDirAliasStatsMaxAliases=_SfpsDirAliasStatsMaxAliases_Object((1,3,6,1,4,1,52,4,2,4,2,2,3,11,13,1,5),_SfpsDirAliasStatsMaxAliases_Type())
sfpsDirAliasStatsMaxAliases.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsDirAliasStatsMaxAliases.setStatus(_A)
_SfpsTopologyDirStatsStaticUsage_Type=Integer32
_SfpsTopologyDirStatsStaticUsage_Object=MibScalar
sfpsTopologyDirStatsStaticUsage=_SfpsTopologyDirStatsStaticUsage_Object((1,3,6,1,4,1,52,4,2,4,2,2,3,11,14),_SfpsTopologyDirStatsStaticUsage_Type())
sfpsTopologyDirStatsStaticUsage.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsTopologyDirStatsStaticUsage.setStatus(_A)
_SfpsTopologyDirStatsObjectsUsage_Type=Integer32
_SfpsTopologyDirStatsObjectsUsage_Object=MibScalar
sfpsTopologyDirStatsObjectsUsage=_SfpsTopologyDirStatsObjectsUsage_Object((1,3,6,1,4,1,52,4,2,4,2,2,3,11,15),_SfpsTopologyDirStatsObjectsUsage_Type())
sfpsTopologyDirStatsObjectsUsage.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsTopologyDirStatsObjectsUsage.setStatus(_A)
_SfpsTopologyDirStatsNodeTableSize_Type=Integer32
_SfpsTopologyDirStatsNodeTableSize_Object=MibScalar
sfpsTopologyDirStatsNodeTableSize=_SfpsTopologyDirStatsNodeTableSize_Object((1,3,6,1,4,1,52,4,2,4,2,2,3,11,16),_SfpsTopologyDirStatsNodeTableSize_Type())
sfpsTopologyDirStatsNodeTableSize.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsTopologyDirStatsNodeTableSize.setStatus(_A)
_SfpsTopologyDirStatsNodeTableUsage_Type=Integer32
_SfpsTopologyDirStatsNodeTableUsage_Object=MibScalar
sfpsTopologyDirStatsNodeTableUsage=_SfpsTopologyDirStatsNodeTableUsage_Object((1,3,6,1,4,1,52,4,2,4,2,2,3,11,17),_SfpsTopologyDirStatsNodeTableUsage_Type())
sfpsTopologyDirStatsNodeTableUsage.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsTopologyDirStatsNodeTableUsage.setStatus(_A)
_SfpsTopologyDirStatsAliasTableSize_Type=Integer32
_SfpsTopologyDirStatsAliasTableSize_Object=MibScalar
sfpsTopologyDirStatsAliasTableSize=_SfpsTopologyDirStatsAliasTableSize_Object((1,3,6,1,4,1,52,4,2,4,2,2,3,11,18),_SfpsTopologyDirStatsAliasTableSize_Type())
sfpsTopologyDirStatsAliasTableSize.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsTopologyDirStatsAliasTableSize.setStatus(_A)
_SfpsTopologyDirStatsAliasTableUsage_Type=Integer32
_SfpsTopologyDirStatsAliasTableUsage_Object=MibScalar
sfpsTopologyDirStatsAliasTableUsage=_SfpsTopologyDirStatsAliasTableUsage_Object((1,3,6,1,4,1,52,4,2,4,2,2,3,11,19),_SfpsTopologyDirStatsAliasTableUsage_Type())
sfpsTopologyDirStatsAliasTableUsage.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsTopologyDirStatsAliasTableUsage.setStatus(_A)
_SfpsTopologyDirStatsNodeCollisions_Type=Integer32
_SfpsTopologyDirStatsNodeCollisions_Object=MibScalar
sfpsTopologyDirStatsNodeCollisions=_SfpsTopologyDirStatsNodeCollisions_Object((1,3,6,1,4,1,52,4,2,4,2,2,3,11,20),_SfpsTopologyDirStatsNodeCollisions_Type())
sfpsTopologyDirStatsNodeCollisions.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsTopologyDirStatsNodeCollisions.setStatus(_A)
_SfpsTopologyDirStatsNodeLongestChain_Type=Integer32
_SfpsTopologyDirStatsNodeLongestChain_Object=MibScalar
sfpsTopologyDirStatsNodeLongestChain=_SfpsTopologyDirStatsNodeLongestChain_Object((1,3,6,1,4,1,52,4,2,4,2,2,3,11,21),_SfpsTopologyDirStatsNodeLongestChain_Type())
sfpsTopologyDirStatsNodeLongestChain.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsTopologyDirStatsNodeLongestChain.setStatus(_A)
_SfpsTopologyDirStatsAliasCollisions_Type=Integer32
_SfpsTopologyDirStatsAliasCollisions_Object=MibScalar
sfpsTopologyDirStatsAliasCollisions=_SfpsTopologyDirStatsAliasCollisions_Object((1,3,6,1,4,1,52,4,2,4,2,2,3,11,22),_SfpsTopologyDirStatsAliasCollisions_Type())
sfpsTopologyDirStatsAliasCollisions.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsTopologyDirStatsAliasCollisions.setStatus(_A)
_SfpsTopologyDirStatsAliasLongestChain_Type=Integer32
_SfpsTopologyDirStatsAliasLongestChain_Object=MibScalar
sfpsTopologyDirStatsAliasLongestChain=_SfpsTopologyDirStatsAliasLongestChain_Object((1,3,6,1,4,1,52,4,2,4,2,2,3,11,23),_SfpsTopologyDirStatsAliasLongestChain_Type())
sfpsTopologyDirStatsAliasLongestChain.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsTopologyDirStatsAliasLongestChain.setStatus(_A)
_SfpsTopologyDirStatsLocalAddsRefused_Type=Integer32
_SfpsTopologyDirStatsLocalAddsRefused_Object=MibScalar
sfpsTopologyDirStatsLocalAddsRefused=_SfpsTopologyDirStatsLocalAddsRefused_Object((1,3,6,1,4,1,52,4,2,4,2,2,3,11,24),_SfpsTopologyDirStatsLocalAddsRefused_Type())
sfpsTopologyDirStatsLocalAddsRefused.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsTopologyDirStatsLocalAddsRefused.setStatus(_A)
_SfpsTopologyDirStatsAliasRemotesReplaced_Type=Integer32
_SfpsTopologyDirStatsAliasRemotesReplaced_Object=MibScalar
sfpsTopologyDirStatsAliasRemotesReplaced=_SfpsTopologyDirStatsAliasRemotesReplaced_Object((1,3,6,1,4,1,52,4,2,4,2,2,3,11,25),_SfpsTopologyDirStatsAliasRemotesReplaced_Type())
sfpsTopologyDirStatsAliasRemotesReplaced.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsTopologyDirStatsAliasRemotesReplaced.setStatus(_A)
_SfpsTopologyDirStatsAliasMultiPortClears_Type=Integer32
_SfpsTopologyDirStatsAliasMultiPortClears_Object=MibScalar
sfpsTopologyDirStatsAliasMultiPortClears=_SfpsTopologyDirStatsAliasMultiPortClears_Object((1,3,6,1,4,1,52,4,2,4,2,2,3,11,26),_SfpsTopologyDirStatsAliasMultiPortClears_Type())
sfpsTopologyDirStatsAliasMultiPortClears.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsTopologyDirStatsAliasMultiPortClears.setStatus(_A)
_SfpsTopologyDirStatsReservedForRemoteNodes_Type=Integer32
_SfpsTopologyDirStatsReservedForRemoteNodes_Object=MibScalar
sfpsTopologyDirStatsReservedForRemoteNodes=_SfpsTopologyDirStatsReservedForRemoteNodes_Object((1,3,6,1,4,1,52,4,2,4,2,2,3,11,27),_SfpsTopologyDirStatsReservedForRemoteNodes_Type())
sfpsTopologyDirStatsReservedForRemoteNodes.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsTopologyDirStatsReservedForRemoteNodes.setStatus(_A)
_SfpsTopologyDirStatsNumSwitches_Type=Integer32
_SfpsTopologyDirStatsNumSwitches_Object=MibScalar
sfpsTopologyDirStatsNumSwitches=_SfpsTopologyDirStatsNumSwitches_Object((1,3,6,1,4,1,52,4,2,4,2,2,3,11,28),_SfpsTopologyDirStatsNumSwitches_Type())
sfpsTopologyDirStatsNumSwitches.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsTopologyDirStatsNumSwitches.setStatus(_A)
_SfpsTopologyDirStatsSwitchUsage_Type=Integer32
_SfpsTopologyDirStatsSwitchUsage_Object=MibScalar
sfpsTopologyDirStatsSwitchUsage=_SfpsTopologyDirStatsSwitchUsage_Object((1,3,6,1,4,1,52,4,2,4,2,2,3,11,29),_SfpsTopologyDirStatsSwitchUsage_Type())
sfpsTopologyDirStatsSwitchUsage.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsTopologyDirStatsSwitchUsage.setStatus(_A)
_SfpsTopologyDirStatsMaxSwitches_Type=Integer32
_SfpsTopologyDirStatsMaxSwitches_Object=MibScalar
sfpsTopologyDirStatsMaxSwitches=_SfpsTopologyDirStatsMaxSwitches_Object((1,3,6,1,4,1,52,4,2,4,2,2,3,11,30),_SfpsTopologyDirStatsMaxSwitches_Type())
sfpsTopologyDirStatsMaxSwitches.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsTopologyDirStatsMaxSwitches.setStatus(_A)
_SfpsTopologyDirStatsSwitchTableSize_Type=Integer32
_SfpsTopologyDirStatsSwitchTableSize_Object=MibScalar
sfpsTopologyDirStatsSwitchTableSize=_SfpsTopologyDirStatsSwitchTableSize_Object((1,3,6,1,4,1,52,4,2,4,2,2,3,11,31),_SfpsTopologyDirStatsSwitchTableSize_Type())
sfpsTopologyDirStatsSwitchTableSize.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsTopologyDirStatsSwitchTableSize.setStatus(_A)
_SfpsTopologyDirStatsSwitchTableUsage_Type=Integer32
_SfpsTopologyDirStatsSwitchTableUsage_Object=MibScalar
sfpsTopologyDirStatsSwitchTableUsage=_SfpsTopologyDirStatsSwitchTableUsage_Object((1,3,6,1,4,1,52,4,2,4,2,2,3,11,32),_SfpsTopologyDirStatsSwitchTableUsage_Type())
sfpsTopologyDirStatsSwitchTableUsage.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsTopologyDirStatsSwitchTableUsage.setStatus(_A)
_SfpsTopologyDirStatsSwitchLookups_Type=Integer32
_SfpsTopologyDirStatsSwitchLookups_Object=MibScalar
sfpsTopologyDirStatsSwitchLookups=_SfpsTopologyDirStatsSwitchLookups_Object((1,3,6,1,4,1,52,4,2,4,2,2,3,11,33),_SfpsTopologyDirStatsSwitchLookups_Type())
sfpsTopologyDirStatsSwitchLookups.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsTopologyDirStatsSwitchLookups.setStatus(_A)
_SfpsTopologyDirStatsSwitchCacheHits_Type=Integer32
_SfpsTopologyDirStatsSwitchCacheHits_Object=MibScalar
sfpsTopologyDirStatsSwitchCacheHits=_SfpsTopologyDirStatsSwitchCacheHits_Object((1,3,6,1,4,1,52,4,2,4,2,2,3,11,34),_SfpsTopologyDirStatsSwitchCacheHits_Type())
sfpsTopologyDirStatsSwitchCacheHits.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsTopologyDirStatsSwitchCacheHits.setStatus(_A)
_SfpsTopologyDirStatsNumVlans_Type=Integer32
_SfpsTopologyDirStatsNumVlans_Object=MibScalar
sfpsTopologyDirStatsNumVlans=_SfpsTopologyDirStatsNumVlans_Object((1,3,6,1,4,1,52,4,2,4,2,2,3,11,35),_SfpsTopologyDirStatsNumVlans_Type())
sfpsTopologyDirStatsNumVlans.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsTopologyDirStatsNumVlans.setStatus(_A)
_SfpsTopologyDirStatsVlanUsage_Type=Integer32
_SfpsTopologyDirStatsVlanUsage_Object=MibScalar
sfpsTopologyDirStatsVlanUsage=_SfpsTopologyDirStatsVlanUsage_Object((1,3,6,1,4,1,52,4,2,4,2,2,3,11,36),_SfpsTopologyDirStatsVlanUsage_Type())
sfpsTopologyDirStatsVlanUsage.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsTopologyDirStatsVlanUsage.setStatus(_A)
_SfpsTopologyDirStatsMaxVlans_Type=Integer32
_SfpsTopologyDirStatsMaxVlans_Object=MibScalar
sfpsTopologyDirStatsMaxVlans=_SfpsTopologyDirStatsMaxVlans_Object((1,3,6,1,4,1,52,4,2,4,2,2,3,11,37),_SfpsTopologyDirStatsMaxVlans_Type())
sfpsTopologyDirStatsMaxVlans.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsTopologyDirStatsMaxVlans.setStatus(_A)
_SfpsTopologyDirStatsVlanTableSize_Type=Integer32
_SfpsTopologyDirStatsVlanTableSize_Object=MibScalar
sfpsTopologyDirStatsVlanTableSize=_SfpsTopologyDirStatsVlanTableSize_Object((1,3,6,1,4,1,52,4,2,4,2,2,3,11,38),_SfpsTopologyDirStatsVlanTableSize_Type())
sfpsTopologyDirStatsVlanTableSize.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsTopologyDirStatsVlanTableSize.setStatus(_A)
_SfpsTopologyDirStatsVlanTableUsage_Type=Integer32
_SfpsTopologyDirStatsVlanTableUsage_Object=MibScalar
sfpsTopologyDirStatsVlanTableUsage=_SfpsTopologyDirStatsVlanTableUsage_Object((1,3,6,1,4,1,52,4,2,4,2,2,3,11,39),_SfpsTopologyDirStatsVlanTableUsage_Type())
sfpsTopologyDirStatsVlanTableUsage.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsTopologyDirStatsVlanTableUsage.setStatus(_A)
_SfpsTopologyDirStatsVlanLookups_Type=Integer32
_SfpsTopologyDirStatsVlanLookups_Object=MibScalar
sfpsTopologyDirStatsVlanLookups=_SfpsTopologyDirStatsVlanLookups_Object((1,3,6,1,4,1,52,4,2,4,2,2,3,11,40),_SfpsTopologyDirStatsVlanLookups_Type())
sfpsTopologyDirStatsVlanLookups.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsTopologyDirStatsVlanLookups.setStatus(_A)
_SfpsTopologyDirStatsVlanCacheHits_Type=Integer32
_SfpsTopologyDirStatsVlanCacheHits_Object=MibScalar
sfpsTopologyDirStatsVlanCacheHits=_SfpsTopologyDirStatsVlanCacheHits_Object((1,3,6,1,4,1,52,4,2,4,2,2,3,11,41),_SfpsTopologyDirStatsVlanCacheHits_Type())
sfpsTopologyDirStatsVlanCacheHits.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsTopologyDirStatsVlanCacheHits.setStatus(_A)
_SfpsTopologyDirStatsNodeAliasMax_Type=Integer32
_SfpsTopologyDirStatsNodeAliasMax_Object=MibScalar
sfpsTopologyDirStatsNodeAliasMax=_SfpsTopologyDirStatsNodeAliasMax_Object((1,3,6,1,4,1,52,4,2,4,2,2,3,11,42),_SfpsTopologyDirStatsNodeAliasMax_Type())
sfpsTopologyDirStatsNodeAliasMax.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsTopologyDirStatsNodeAliasMax.setStatus(_A)
_SfpsTopologyDirStatsLocalAliasRefused_Type=Integer32
_SfpsTopologyDirStatsLocalAliasRefused_Object=MibScalar
sfpsTopologyDirStatsLocalAliasRefused=_SfpsTopologyDirStatsLocalAliasRefused_Object((1,3,6,1,4,1,52,4,2,4,2,2,3,11,43),_SfpsTopologyDirStatsLocalAliasRefused_Type())
sfpsTopologyDirStatsLocalAliasRefused.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsTopologyDirStatsLocalAliasRefused.setStatus(_A)
_SfpsTopologyDirStatsRemoteAliasRemoved_Type=Integer32
_SfpsTopologyDirStatsRemoteAliasRemoved_Object=MibScalar
sfpsTopologyDirStatsRemoteAliasRemoved=_SfpsTopologyDirStatsRemoteAliasRemoved_Object((1,3,6,1,4,1,52,4,2,4,2,2,3,11,44),_SfpsTopologyDirStatsRemoteAliasRemoved_Type())
sfpsTopologyDirStatsRemoteAliasRemoved.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsTopologyDirStatsRemoteAliasRemoved.setStatus(_A)
class _SfpsDirFilterAPILockAdmin_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_F,1),('lock',2),(_s,3)))
_SfpsDirFilterAPILockAdmin_Type.__name__=_C
_SfpsDirFilterAPILockAdmin_Object=MibScalar
sfpsDirFilterAPILockAdmin=_SfpsDirFilterAPILockAdmin_Object((1,3,6,1,4,1,52,4,2,4,2,2,3,13,1,1),_SfpsDirFilterAPILockAdmin_Type())
sfpsDirFilterAPILockAdmin.setMaxAccess(_D)
if mibBuilder.loadTexts:sfpsDirFilterAPILockAdmin.setStatus(_A)
class _SfpsDirFilterAPILockStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_F,1),(_j,2),(_G,3)))
_SfpsDirFilterAPILockStatus_Type.__name__=_C
_SfpsDirFilterAPILockStatus_Object=MibScalar
sfpsDirFilterAPILockStatus=_SfpsDirFilterAPILockStatus_Object((1,3,6,1,4,1,52,4,2,4,2,2,3,13,1,2),_SfpsDirFilterAPILockStatus_Type())
sfpsDirFilterAPILockStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsDirFilterAPILockStatus.setStatus(_A)
_SfpsDirFilterAPILockCount_Type=Integer32
_SfpsDirFilterAPILockCount_Object=MibScalar
sfpsDirFilterAPILockCount=_SfpsDirFilterAPILockCount_Object((1,3,6,1,4,1,52,4,2,4,2,2,3,13,1,3),_SfpsDirFilterAPILockCount_Type())
sfpsDirFilterAPILockCount.setMaxAccess(_D)
if mibBuilder.loadTexts:sfpsDirFilterAPILockCount.setStatus(_A)
_SfpsDirFilterAPIValueType_Type=DisplayString
_SfpsDirFilterAPIValueType_Object=MibScalar
sfpsDirFilterAPIValueType=_SfpsDirFilterAPIValueType_Object((1,3,6,1,4,1,52,4,2,4,2,2,3,13,1,4),_SfpsDirFilterAPIValueType_Type())
sfpsDirFilterAPIValueType.setMaxAccess(_D)
if mibBuilder.loadTexts:sfpsDirFilterAPIValueType.setStatus(_A)
_SfpsDirFilterAPIValue_Type=DisplayString
_SfpsDirFilterAPIValue_Object=MibScalar
sfpsDirFilterAPIValue=_SfpsDirFilterAPIValue_Object((1,3,6,1,4,1,52,4,2,4,2,2,3,13,1,5),_SfpsDirFilterAPIValue_Type())
sfpsDirFilterAPIValue.setMaxAccess(_D)
if mibBuilder.loadTexts:sfpsDirFilterAPIValue.setStatus(_A)
_SfpsDirFilterAPILockTimeOut_Type=Integer32
_SfpsDirFilterAPILockTimeOut_Object=MibScalar
sfpsDirFilterAPILockTimeOut=_SfpsDirFilterAPILockTimeOut_Object((1,3,6,1,4,1,52,4,2,4,2,2,3,13,1,6),_SfpsDirFilterAPILockTimeOut_Type())
sfpsDirFilterAPILockTimeOut.setMaxAccess(_D)
if mibBuilder.loadTexts:sfpsDirFilterAPILockTimeOut.setStatus(_A)
_SfpsDirFilterAPILockTimeElapsed_Type=Integer32
_SfpsDirFilterAPILockTimeElapsed_Object=MibScalar
sfpsDirFilterAPILockTimeElapsed=_SfpsDirFilterAPILockTimeElapsed_Object((1,3,6,1,4,1,52,4,2,4,2,2,3,13,1,7),_SfpsDirFilterAPILockTimeElapsed_Type())
sfpsDirFilterAPILockTimeElapsed.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsDirFilterAPILockTimeElapsed.setStatus(_A)
_SfpsDirFilterNodeTable_Object=MibTable
sfpsDirFilterNodeTable=_SfpsDirFilterNodeTable_Object((1,3,6,1,4,1,52,4,2,4,2,2,3,13,2))
if mibBuilder.loadTexts:sfpsDirFilterNodeTable.setStatus(_A)
_SfpsDirFilterNodeEntry_Object=MibTableRow
sfpsDirFilterNodeEntry=_SfpsDirFilterNodeEntry_Object((1,3,6,1,4,1,52,4,2,4,2,2,3,13,2,1))
sfpsDirFilterNodeEntry.setIndexNames((0,_E,_w),(0,_E,_x),(0,_E,_y))
if mibBuilder.loadTexts:sfpsDirFilterNodeEntry.setStatus(_A)
_SfpsDirFilterNodeLockCount_Type=Integer32
_SfpsDirFilterNodeLockCount_Object=MibTableColumn
sfpsDirFilterNodeLockCount=_SfpsDirFilterNodeLockCount_Object((1,3,6,1,4,1,52,4,2,4,2,2,3,13,2,1,1),_SfpsDirFilterNodeLockCount_Type())
sfpsDirFilterNodeLockCount.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsDirFilterNodeLockCount.setStatus(_A)
_SfpsDirFilterNodeNodeIndex_Type=Integer32
_SfpsDirFilterNodeNodeIndex_Object=MibTableColumn
sfpsDirFilterNodeNodeIndex=_SfpsDirFilterNodeNodeIndex_Object((1,3,6,1,4,1,52,4,2,4,2,2,3,13,2,1,2),_SfpsDirFilterNodeNodeIndex_Type())
sfpsDirFilterNodeNodeIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsDirFilterNodeNodeIndex.setStatus(_A)
_SfpsDirFilterNodeLinkIndex_Type=Integer32
_SfpsDirFilterNodeLinkIndex_Object=MibTableColumn
sfpsDirFilterNodeLinkIndex=_SfpsDirFilterNodeLinkIndex_Object((1,3,6,1,4,1,52,4,2,4,2,2,3,13,2,1,3),_SfpsDirFilterNodeLinkIndex_Type())
sfpsDirFilterNodeLinkIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsDirFilterNodeLinkIndex.setStatus(_A)
_SfpsDirFilterNodeNodeCount_Type=Integer32
_SfpsDirFilterNodeNodeCount_Object=MibTableColumn
sfpsDirFilterNodeNodeCount=_SfpsDirFilterNodeNodeCount_Object((1,3,6,1,4,1,52,4,2,4,2,2,3,13,2,1,4),_SfpsDirFilterNodeNodeCount_Type())
sfpsDirFilterNodeNodeCount.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsDirFilterNodeNodeCount.setStatus(_A)
_SfpsDirFilterNodeLinkCount_Type=Integer32
_SfpsDirFilterNodeLinkCount_Object=MibTableColumn
sfpsDirFilterNodeLinkCount=_SfpsDirFilterNodeLinkCount_Object((1,3,6,1,4,1,52,4,2,4,2,2,3,13,2,1,5),_SfpsDirFilterNodeLinkCount_Type())
sfpsDirFilterNodeLinkCount.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsDirFilterNodeLinkCount.setStatus(_A)
_SfpsDirFilterNodeDomainName_Type=DisplayString
_SfpsDirFilterNodeDomainName_Object=MibTableColumn
sfpsDirFilterNodeDomainName=_SfpsDirFilterNodeDomainName_Object((1,3,6,1,4,1,52,4,2,4,2,2,3,13,2,1,6),_SfpsDirFilterNodeDomainName_Type())
sfpsDirFilterNodeDomainName.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsDirFilterNodeDomainName.setStatus(_A)
_SfpsDirFilterNodeChassisType_Type=DisplayString
_SfpsDirFilterNodeChassisType_Object=MibTableColumn
sfpsDirFilterNodeChassisType=_SfpsDirFilterNodeChassisType_Object((1,3,6,1,4,1,52,4,2,4,2,2,3,13,2,1,7),_SfpsDirFilterNodeChassisType_Type())
sfpsDirFilterNodeChassisType.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsDirFilterNodeChassisType.setStatus(_A)
_SfpsDirFilterNodeChassisLoad_Type=DisplayString
_SfpsDirFilterNodeChassisLoad_Object=MibTableColumn
sfpsDirFilterNodeChassisLoad=_SfpsDirFilterNodeChassisLoad_Object((1,3,6,1,4,1,52,4,2,4,2,2,3,13,2,1,8),_SfpsDirFilterNodeChassisLoad_Type())
sfpsDirFilterNodeChassisLoad.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsDirFilterNodeChassisLoad.setStatus(_A)
_SfpsDirFilterNodeSwitchType_Type=DisplayString
_SfpsDirFilterNodeSwitchType_Object=MibTableColumn
sfpsDirFilterNodeSwitchType=_SfpsDirFilterNodeSwitchType_Object((1,3,6,1,4,1,52,4,2,4,2,2,3,13,2,1,9),_SfpsDirFilterNodeSwitchType_Type())
sfpsDirFilterNodeSwitchType.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsDirFilterNodeSwitchType.setStatus(_A)
_SfpsDirFilterNodeSwitchLoad_Type=DisplayString
_SfpsDirFilterNodeSwitchLoad_Object=MibTableColumn
sfpsDirFilterNodeSwitchLoad=_SfpsDirFilterNodeSwitchLoad_Object((1,3,6,1,4,1,52,4,2,4,2,2,3,13,2,1,10),_SfpsDirFilterNodeSwitchLoad_Type())
sfpsDirFilterNodeSwitchLoad.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsDirFilterNodeSwitchLoad.setStatus(_A)
_SfpsDirFilterNodeInPort_Type=Integer32
_SfpsDirFilterNodeInPort_Object=MibTableColumn
sfpsDirFilterNodeInPort=_SfpsDirFilterNodeInPort_Object((1,3,6,1,4,1,52,4,2,4,2,2,3,13,2,1,11),_SfpsDirFilterNodeInPort_Type())
sfpsDirFilterNodeInPort.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsDirFilterNodeInPort.setStatus(_A)
_SfpsDirFilterNodeBaseType_Type=DisplayString
_SfpsDirFilterNodeBaseType_Object=MibTableColumn
sfpsDirFilterNodeBaseType=_SfpsDirFilterNodeBaseType_Object((1,3,6,1,4,1,52,4,2,4,2,2,3,13,2,1,12),_SfpsDirFilterNodeBaseType_Type())
sfpsDirFilterNodeBaseType.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsDirFilterNodeBaseType.setStatus(_A)
_SfpsDirFilterNodeBaseLoad_Type=DisplayString
_SfpsDirFilterNodeBaseLoad_Object=MibTableColumn
sfpsDirFilterNodeBaseLoad=_SfpsDirFilterNodeBaseLoad_Object((1,3,6,1,4,1,52,4,2,4,2,2,3,13,2,1,13),_SfpsDirFilterNodeBaseLoad_Type())
sfpsDirFilterNodeBaseLoad.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsDirFilterNodeBaseLoad.setStatus(_A)
_SfpsDirFilterNodeNodeState_Type=Integer32
_SfpsDirFilterNodeNodeState_Object=MibTableColumn
sfpsDirFilterNodeNodeState=_SfpsDirFilterNodeNodeState_Object((1,3,6,1,4,1,52,4,2,4,2,2,3,13,2,1,14),_SfpsDirFilterNodeNodeState_Type())
sfpsDirFilterNodeNodeState.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsDirFilterNodeNodeState.setStatus(_A)
_SfpsDirFilterNodeNodeAge_Type=TimeTicks
_SfpsDirFilterNodeNodeAge_Object=MibTableColumn
sfpsDirFilterNodeNodeAge=_SfpsDirFilterNodeNodeAge_Object((1,3,6,1,4,1,52,4,2,4,2,2,3,13,2,1,15),_SfpsDirFilterNodeNodeAge_Type())
sfpsDirFilterNodeNodeAge.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsDirFilterNodeNodeAge.setStatus(_A)
class _SfpsDirFilterNodeNodeLock_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_z,2)))
_SfpsDirFilterNodeNodeLock_Type.__name__=_C
_SfpsDirFilterNodeNodeLock_Object=MibTableColumn
sfpsDirFilterNodeNodeLock=_SfpsDirFilterNodeNodeLock_Object((1,3,6,1,4,1,52,4,2,4,2,2,3,13,2,1,16),_SfpsDirFilterNodeNodeLock_Type())
sfpsDirFilterNodeNodeLock.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsDirFilterNodeNodeLock.setStatus(_A)
_SfpsDirFilterNodeLinkType_Type=DisplayString
_SfpsDirFilterNodeLinkType_Object=MibTableColumn
sfpsDirFilterNodeLinkType=_SfpsDirFilterNodeLinkType_Object((1,3,6,1,4,1,52,4,2,4,2,2,3,13,2,1,17),_SfpsDirFilterNodeLinkType_Type())
sfpsDirFilterNodeLinkType.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsDirFilterNodeLinkType.setStatus(_A)
_SfpsDirFilterNodeLinkLoad_Type=DisplayString
_SfpsDirFilterNodeLinkLoad_Object=MibTableColumn
sfpsDirFilterNodeLinkLoad=_SfpsDirFilterNodeLinkLoad_Object((1,3,6,1,4,1,52,4,2,4,2,2,3,13,2,1,18),_SfpsDirFilterNodeLinkLoad_Type())
sfpsDirFilterNodeLinkLoad.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsDirFilterNodeLinkLoad.setStatus(_A)
_SfpsDirFilterNodeLinkAge_Type=TimeTicks
_SfpsDirFilterNodeLinkAge_Object=MibTableColumn
sfpsDirFilterNodeLinkAge=_SfpsDirFilterNodeLinkAge_Object((1,3,6,1,4,1,52,4,2,4,2,2,3,13,2,1,19),_SfpsDirFilterNodeLinkAge_Type())
sfpsDirFilterNodeLinkAge.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsDirFilterNodeLinkAge.setStatus(_A)
class _SfpsDirFilterNodeLinkLock_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_A0,2)))
_SfpsDirFilterNodeLinkLock_Type.__name__=_C
_SfpsDirFilterNodeLinkLock_Object=MibTableColumn
sfpsDirFilterNodeLinkLock=_SfpsDirFilterNodeLinkLock_Object((1,3,6,1,4,1,52,4,2,4,2,2,3,13,2,1,20),_SfpsDirFilterNodeLinkLock_Type())
sfpsDirFilterNodeLinkLock.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsDirFilterNodeLinkLock.setStatus(_A)
class _SfpsDirFilterNodeVlanLearned_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_F,1),('inherit',2),('autoReg',3),(_f,4)))
_SfpsDirFilterNodeVlanLearned_Type.__name__=_C
_SfpsDirFilterNodeVlanLearned_Object=MibTableColumn
sfpsDirFilterNodeVlanLearned=_SfpsDirFilterNodeVlanLearned_Object((1,3,6,1,4,1,52,4,2,4,2,2,3,13,2,1,21),_SfpsDirFilterNodeVlanLearned_Type())
sfpsDirFilterNodeVlanLearned.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsDirFilterNodeVlanLearned.setStatus(_A)
_SfpsDirFilterNodeOpaqueTag_Type=OctetString
_SfpsDirFilterNodeOpaqueTag_Object=MibTableColumn
sfpsDirFilterNodeOpaqueTag=_SfpsDirFilterNodeOpaqueTag_Object((1,3,6,1,4,1,52,4,2,4,2,2,3,13,2,1,22),_SfpsDirFilterNodeOpaqueTag_Type())
sfpsDirFilterNodeOpaqueTag.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsDirFilterNodeOpaqueTag.setStatus(_A)
_SfpsDirFilterNodeChassisOctets_Type=OctetString
_SfpsDirFilterNodeChassisOctets_Object=MibTableColumn
sfpsDirFilterNodeChassisOctets=_SfpsDirFilterNodeChassisOctets_Object((1,3,6,1,4,1,52,4,2,4,2,2,3,13,2,1,23),_SfpsDirFilterNodeChassisOctets_Type())
sfpsDirFilterNodeChassisOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsDirFilterNodeChassisOctets.setStatus(_A)
_SfpsDirFilterNodeSwitchOctets_Type=OctetString
_SfpsDirFilterNodeSwitchOctets_Object=MibTableColumn
sfpsDirFilterNodeSwitchOctets=_SfpsDirFilterNodeSwitchOctets_Object((1,3,6,1,4,1,52,4,2,4,2,2,3,13,2,1,24),_SfpsDirFilterNodeSwitchOctets_Type())
sfpsDirFilterNodeSwitchOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsDirFilterNodeSwitchOctets.setStatus(_A)
_SfpsDirFilterNodeNodeOctets_Type=OctetString
_SfpsDirFilterNodeNodeOctets_Object=MibTableColumn
sfpsDirFilterNodeNodeOctets=_SfpsDirFilterNodeNodeOctets_Object((1,3,6,1,4,1,52,4,2,4,2,2,3,13,2,1,25),_SfpsDirFilterNodeNodeOctets_Type())
sfpsDirFilterNodeNodeOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsDirFilterNodeNodeOctets.setStatus(_A)
_SfpsDirFilterNodeLinkOctets_Type=OctetString
_SfpsDirFilterNodeLinkOctets_Object=MibTableColumn
sfpsDirFilterNodeLinkOctets=_SfpsDirFilterNodeLinkOctets_Object((1,3,6,1,4,1,52,4,2,4,2,2,3,13,2,1,26),_SfpsDirFilterNodeLinkOctets_Type())
sfpsDirFilterNodeLinkOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsDirFilterNodeLinkOctets.setStatus(_A)
class _SfpsDirFilterNodeNodeLocal_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_I,2)))
_SfpsDirFilterNodeNodeLocal_Type.__name__=_C
_SfpsDirFilterNodeNodeLocal_Object=MibTableColumn
sfpsDirFilterNodeNodeLocal=_SfpsDirFilterNodeNodeLocal_Object((1,3,6,1,4,1,52,4,2,4,2,2,3,13,2,1,27),_SfpsDirFilterNodeNodeLocal_Type())
sfpsDirFilterNodeNodeLocal.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsDirFilterNodeNodeLocal.setStatus(_A)
class _SfpsDirFilterNodeLinkState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_F,1),(_g,2),(_h,3),(_i,4)))
_SfpsDirFilterNodeLinkState_Type.__name__=_C
_SfpsDirFilterNodeLinkState_Object=MibTableColumn
sfpsDirFilterNodeLinkState=_SfpsDirFilterNodeLinkState_Object((1,3,6,1,4,1,52,4,2,4,2,2,3,13,2,1,28),_SfpsDirFilterNodeLinkState_Type())
sfpsDirFilterNodeLinkState.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsDirFilterNodeLinkState.setStatus(_A)
_SfpsDirFilterAliasTable_Object=MibTable
sfpsDirFilterAliasTable=_SfpsDirFilterAliasTable_Object((1,3,6,1,4,1,52,4,2,4,2,2,3,13,3))
if mibBuilder.loadTexts:sfpsDirFilterAliasTable.setStatus(_A)
_SfpsDirFilterAliasEntry_Object=MibTableRow
sfpsDirFilterAliasEntry=_SfpsDirFilterAliasEntry_Object((1,3,6,1,4,1,52,4,2,4,2,2,3,13,3,1))
sfpsDirFilterAliasEntry.setIndexNames((0,_E,_A1),(0,_E,_A2),(0,_E,_A3),(0,_E,_A4))
if mibBuilder.loadTexts:sfpsDirFilterAliasEntry.setStatus(_A)
_SfpsDirFilterAliasLockCount_Type=Integer32
_SfpsDirFilterAliasLockCount_Object=MibTableColumn
sfpsDirFilterAliasLockCount=_SfpsDirFilterAliasLockCount_Object((1,3,6,1,4,1,52,4,2,4,2,2,3,13,3,1,1),_SfpsDirFilterAliasLockCount_Type())
sfpsDirFilterAliasLockCount.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsDirFilterAliasLockCount.setStatus(_A)
_SfpsDirFilterAliasAliasHash_Type=Integer32
_SfpsDirFilterAliasAliasHash_Object=MibTableColumn
sfpsDirFilterAliasAliasHash=_SfpsDirFilterAliasAliasHash_Object((1,3,6,1,4,1,52,4,2,4,2,2,3,13,3,1,2),_SfpsDirFilterAliasAliasHash_Type())
sfpsDirFilterAliasAliasHash.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsDirFilterAliasAliasHash.setStatus(_A)
_SfpsDirFilterAliasBaseHash_Type=Integer32
_SfpsDirFilterAliasBaseHash_Object=MibTableColumn
sfpsDirFilterAliasBaseHash=_SfpsDirFilterAliasBaseHash_Object((1,3,6,1,4,1,52,4,2,4,2,2,3,13,3,1,3),_SfpsDirFilterAliasBaseHash_Type())
sfpsDirFilterAliasBaseHash.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsDirFilterAliasBaseHash.setStatus(_A)
_SfpsDirFilterAliasHashIndex_Type=Integer32
_SfpsDirFilterAliasHashIndex_Object=MibTableColumn
sfpsDirFilterAliasHashIndex=_SfpsDirFilterAliasHashIndex_Object((1,3,6,1,4,1,52,4,2,4,2,2,3,13,3,1,4),_SfpsDirFilterAliasHashIndex_Type())
sfpsDirFilterAliasHashIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsDirFilterAliasHashIndex.setStatus(_A)
_SfpsDirFilterAliasDomain_Type=DisplayString
_SfpsDirFilterAliasDomain_Object=MibTableColumn
sfpsDirFilterAliasDomain=_SfpsDirFilterAliasDomain_Object((1,3,6,1,4,1,52,4,2,4,2,2,3,13,3,1,5),_SfpsDirFilterAliasDomain_Type())
sfpsDirFilterAliasDomain.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsDirFilterAliasDomain.setStatus(_A)
_SfpsDirFilterAliasChassisType_Type=DisplayString
_SfpsDirFilterAliasChassisType_Object=MibTableColumn
sfpsDirFilterAliasChassisType=_SfpsDirFilterAliasChassisType_Object((1,3,6,1,4,1,52,4,2,4,2,2,3,13,3,1,6),_SfpsDirFilterAliasChassisType_Type())
sfpsDirFilterAliasChassisType.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsDirFilterAliasChassisType.setStatus(_A)
_SfpsDirFilterAliasChassisLoad_Type=DisplayString
_SfpsDirFilterAliasChassisLoad_Object=MibTableColumn
sfpsDirFilterAliasChassisLoad=_SfpsDirFilterAliasChassisLoad_Object((1,3,6,1,4,1,52,4,2,4,2,2,3,13,3,1,7),_SfpsDirFilterAliasChassisLoad_Type())
sfpsDirFilterAliasChassisLoad.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsDirFilterAliasChassisLoad.setStatus(_A)
_SfpsDirFilterAliasSwitchType_Type=DisplayString
_SfpsDirFilterAliasSwitchType_Object=MibTableColumn
sfpsDirFilterAliasSwitchType=_SfpsDirFilterAliasSwitchType_Object((1,3,6,1,4,1,52,4,2,4,2,2,3,13,3,1,8),_SfpsDirFilterAliasSwitchType_Type())
sfpsDirFilterAliasSwitchType.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsDirFilterAliasSwitchType.setStatus(_A)
_SfpsDirFilterAliasSwitchLoad_Type=DisplayString
_SfpsDirFilterAliasSwitchLoad_Object=MibTableColumn
sfpsDirFilterAliasSwitchLoad=_SfpsDirFilterAliasSwitchLoad_Object((1,3,6,1,4,1,52,4,2,4,2,2,3,13,3,1,9),_SfpsDirFilterAliasSwitchLoad_Type())
sfpsDirFilterAliasSwitchLoad.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsDirFilterAliasSwitchLoad.setStatus(_A)
_SfpsDirFilterAliasInPort_Type=Integer32
_SfpsDirFilterAliasInPort_Object=MibTableColumn
sfpsDirFilterAliasInPort=_SfpsDirFilterAliasInPort_Object((1,3,6,1,4,1,52,4,2,4,2,2,3,13,3,1,10),_SfpsDirFilterAliasInPort_Type())
sfpsDirFilterAliasInPort.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsDirFilterAliasInPort.setStatus(_A)
_SfpsDirFilterAliasBaseType_Type=DisplayString
_SfpsDirFilterAliasBaseType_Object=MibTableColumn
sfpsDirFilterAliasBaseType=_SfpsDirFilterAliasBaseType_Object((1,3,6,1,4,1,52,4,2,4,2,2,3,13,3,1,11),_SfpsDirFilterAliasBaseType_Type())
sfpsDirFilterAliasBaseType.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsDirFilterAliasBaseType.setStatus(_A)
_SfpsDirFilterAliasBaseLoad_Type=DisplayString
_SfpsDirFilterAliasBaseLoad_Object=MibTableColumn
sfpsDirFilterAliasBaseLoad=_SfpsDirFilterAliasBaseLoad_Object((1,3,6,1,4,1,52,4,2,4,2,2,3,13,3,1,12),_SfpsDirFilterAliasBaseLoad_Type())
sfpsDirFilterAliasBaseLoad.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsDirFilterAliasBaseLoad.setStatus(_A)
_SfpsDirFilterAliasNodeState_Type=Integer32
_SfpsDirFilterAliasNodeState_Object=MibTableColumn
sfpsDirFilterAliasNodeState=_SfpsDirFilterAliasNodeState_Object((1,3,6,1,4,1,52,4,2,4,2,2,3,13,3,1,13),_SfpsDirFilterAliasNodeState_Type())
sfpsDirFilterAliasNodeState.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsDirFilterAliasNodeState.setStatus(_A)
_SfpsDirFilterAliasNodeAge_Type=TimeTicks
_SfpsDirFilterAliasNodeAge_Object=MibTableColumn
sfpsDirFilterAliasNodeAge=_SfpsDirFilterAliasNodeAge_Object((1,3,6,1,4,1,52,4,2,4,2,2,3,13,3,1,14),_SfpsDirFilterAliasNodeAge_Type())
sfpsDirFilterAliasNodeAge.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsDirFilterAliasNodeAge.setStatus(_A)
class _SfpsDirFilterAliasNodeLock_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_z,2)))
_SfpsDirFilterAliasNodeLock_Type.__name__=_C
_SfpsDirFilterAliasNodeLock_Object=MibTableColumn
sfpsDirFilterAliasNodeLock=_SfpsDirFilterAliasNodeLock_Object((1,3,6,1,4,1,52,4,2,4,2,2,3,13,3,1,15),_SfpsDirFilterAliasNodeLock_Type())
sfpsDirFilterAliasNodeLock.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsDirFilterAliasNodeLock.setStatus(_A)
_SfpsDirFilterAliasLinkType_Type=DisplayString
_SfpsDirFilterAliasLinkType_Object=MibTableColumn
sfpsDirFilterAliasLinkType=_SfpsDirFilterAliasLinkType_Object((1,3,6,1,4,1,52,4,2,4,2,2,3,13,3,1,16),_SfpsDirFilterAliasLinkType_Type())
sfpsDirFilterAliasLinkType.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsDirFilterAliasLinkType.setStatus(_A)
_SfpsDirFilterAliasLinkLoad_Type=DisplayString
_SfpsDirFilterAliasLinkLoad_Object=MibTableColumn
sfpsDirFilterAliasLinkLoad=_SfpsDirFilterAliasLinkLoad_Object((1,3,6,1,4,1,52,4,2,4,2,2,3,13,3,1,17),_SfpsDirFilterAliasLinkLoad_Type())
sfpsDirFilterAliasLinkLoad.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsDirFilterAliasLinkLoad.setStatus(_A)
_SfpsDirFilterAliasLinkAge_Type=TimeTicks
_SfpsDirFilterAliasLinkAge_Object=MibTableColumn
sfpsDirFilterAliasLinkAge=_SfpsDirFilterAliasLinkAge_Object((1,3,6,1,4,1,52,4,2,4,2,2,3,13,3,1,18),_SfpsDirFilterAliasLinkAge_Type())
sfpsDirFilterAliasLinkAge.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsDirFilterAliasLinkAge.setStatus(_A)
class _SfpsDirFilterAliasLinkLock_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_A0,2)))
_SfpsDirFilterAliasLinkLock_Type.__name__=_C
_SfpsDirFilterAliasLinkLock_Object=MibTableColumn
sfpsDirFilterAliasLinkLock=_SfpsDirFilterAliasLinkLock_Object((1,3,6,1,4,1,52,4,2,4,2,2,3,13,3,1,19),_SfpsDirFilterAliasLinkLock_Type())
sfpsDirFilterAliasLinkLock.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsDirFilterAliasLinkLock.setStatus(_A)
class _SfpsDirFilterAliasVlanLearned_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_F,1),(_q,2),('amr',3),(_f,4)))
_SfpsDirFilterAliasVlanLearned_Type.__name__=_C
_SfpsDirFilterAliasVlanLearned_Object=MibTableColumn
sfpsDirFilterAliasVlanLearned=_SfpsDirFilterAliasVlanLearned_Object((1,3,6,1,4,1,52,4,2,4,2,2,3,13,3,1,20),_SfpsDirFilterAliasVlanLearned_Type())
sfpsDirFilterAliasVlanLearned.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsDirFilterAliasVlanLearned.setStatus(_A)
_SfpsDirFilterAliasOpaqueTag_Type=OctetString
_SfpsDirFilterAliasOpaqueTag_Object=MibTableColumn
sfpsDirFilterAliasOpaqueTag=_SfpsDirFilterAliasOpaqueTag_Object((1,3,6,1,4,1,52,4,2,4,2,2,3,13,3,1,21),_SfpsDirFilterAliasOpaqueTag_Type())
sfpsDirFilterAliasOpaqueTag.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsDirFilterAliasOpaqueTag.setStatus(_A)
_SfpsDirFilterAliasChassisOctets_Type=OctetString
_SfpsDirFilterAliasChassisOctets_Object=MibTableColumn
sfpsDirFilterAliasChassisOctets=_SfpsDirFilterAliasChassisOctets_Object((1,3,6,1,4,1,52,4,2,4,2,2,3,13,3,1,22),_SfpsDirFilterAliasChassisOctets_Type())
sfpsDirFilterAliasChassisOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsDirFilterAliasChassisOctets.setStatus(_A)
_SfpsDirFilterAliasSwitchOctets_Type=OctetString
_SfpsDirFilterAliasSwitchOctets_Object=MibTableColumn
sfpsDirFilterAliasSwitchOctets=_SfpsDirFilterAliasSwitchOctets_Object((1,3,6,1,4,1,52,4,2,4,2,2,3,13,3,1,23),_SfpsDirFilterAliasSwitchOctets_Type())
sfpsDirFilterAliasSwitchOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsDirFilterAliasSwitchOctets.setStatus(_A)
_SfpsDirFilterAliasNodeOctets_Type=OctetString
_SfpsDirFilterAliasNodeOctets_Object=MibTableColumn
sfpsDirFilterAliasNodeOctets=_SfpsDirFilterAliasNodeOctets_Object((1,3,6,1,4,1,52,4,2,4,2,2,3,13,3,1,24),_SfpsDirFilterAliasNodeOctets_Type())
sfpsDirFilterAliasNodeOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsDirFilterAliasNodeOctets.setStatus(_A)
_SfpsDirFilterAliasLinkOctets_Type=OctetString
_SfpsDirFilterAliasLinkOctets_Object=MibTableColumn
sfpsDirFilterAliasLinkOctets=_SfpsDirFilterAliasLinkOctets_Object((1,3,6,1,4,1,52,4,2,4,2,2,3,13,3,1,25),_SfpsDirFilterAliasLinkOctets_Type())
sfpsDirFilterAliasLinkOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsDirFilterAliasLinkOctets.setStatus(_A)
class _SfpsDirFilterAliasNodeLocal_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_I,2)))
_SfpsDirFilterAliasNodeLocal_Type.__name__=_C
_SfpsDirFilterAliasNodeLocal_Object=MibTableColumn
sfpsDirFilterAliasNodeLocal=_SfpsDirFilterAliasNodeLocal_Object((1,3,6,1,4,1,52,4,2,4,2,2,3,13,3,1,26),_SfpsDirFilterAliasNodeLocal_Type())
sfpsDirFilterAliasNodeLocal.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsDirFilterAliasNodeLocal.setStatus(_A)
class _SfpsDirFilterAliasLinkState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_F,1),(_g,2),(_h,3),(_i,4)))
_SfpsDirFilterAliasLinkState_Type.__name__=_C
_SfpsDirFilterAliasLinkState_Object=MibTableColumn
sfpsDirFilterAliasLinkState=_SfpsDirFilterAliasLinkState_Object((1,3,6,1,4,1,52,4,2,4,2,2,3,13,3,1,27),_SfpsDirFilterAliasLinkState_Type())
sfpsDirFilterAliasLinkState.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsDirFilterAliasLinkState.setStatus(_A)
mibBuilder.exportSymbols(_E,**{'SfpsSwitchPort':SfpsSwitchPort,'SfpsAddress':SfpsAddress,'HexInteger':HexInteger,'sfpsServiceCenterDirectoryTable':sfpsServiceCenterDirectoryTable,'sfpsServiceCenterDirectoryEntry':sfpsServiceCenterDirectoryEntry,_k:sfpsServiceCenterDirectoryHashLeaf,'sfpsServiceCenterDirectoryMetric':sfpsServiceCenterDirectoryMetric,'sfpsServiceCenterDirectoryName':sfpsServiceCenterDirectoryName,'sfpsServiceCenterDirectoryOperStatus':sfpsServiceCenterDirectoryOperStatus,'sfpsServiceCenterDirectoryAdminStatus':sfpsServiceCenterDirectoryAdminStatus,'sfpsServiceCenterDirectoryStatusTime':sfpsServiceCenterDirectoryStatusTime,'sfpsServiceCenterDirectoryRequests':sfpsServiceCenterDirectoryRequests,'sfpsServiceCenterDirectoryResponses':sfpsServiceCenterDirectoryResponses,'sfpsNodeTable':sfpsNodeTable,'sfpsNodeTableEntry':sfpsNodeTableEntry,_l:sfpsNodeTableBaseHash,_m:sfpsNodeTableHashIndex,'sfpsNodeTableSwitchType':sfpsNodeTableSwitchType,'sfpsNodeTableSwitchAddress':sfpsNodeTableSwitchAddress,'sfpsNodeTablePort':sfpsNodeTablePort,'sfpsNodeTableBaseType':sfpsNodeTableBaseType,'sfpsNodeTableBaseAddress':sfpsNodeTableBaseAddress,'sfpsNodeTableEntryType':sfpsNodeTableEntryType,'sfpsNodeTableCallTag':sfpsNodeTableCallTag,'sfpsNodeTableLastHeard':sfpsNodeTableLastHeard,'sfpsNodeTableAge':sfpsNodeTableAge,'sfpsNodeTableAliasCount':sfpsNodeTableAliasCount,'sfpsNodeTableVlanCount':sfpsNodeTableVlanCount,'sfpsNodeTableNodeLocked':sfpsNodeTableNodeLocked,'sfpsNodeTableNodeLocal':sfpsNodeTableNodeLocal,'sfpsNodeTableSelf':sfpsNodeTableSelf,'sfpsNodeTableNext':sfpsNodeTableNext,'sfpsNodeTablePrev':sfpsNodeTablePrev,'sfpsAliasTable':sfpsAliasTable,'sfpsAliasTableEntry':sfpsAliasTableEntry,_n:sfpsAliasTableAliasHash,_o:sfpsAliasTableBaseHash,_p:sfpsAliasTableHashIndex,'sfpsAliasTableSwitchType':sfpsAliasTableSwitchType,'sfpsAliasTableSwitchAddress':sfpsAliasTableSwitchAddress,'sfpsAliasTablePort':sfpsAliasTablePort,'sfpsAliasTableBaseType':sfpsAliasTableBaseType,'sfpsAliasTableBaseAddress':sfpsAliasTableBaseAddress,'sfpsAliasTableAliasType':sfpsAliasTableAliasType,'sfpsAliasTableAliasAddress':sfpsAliasTableAliasAddress,'sfpsAliasTableAliasAge':sfpsAliasTableAliasAge,'sfpsAliasTableSwitchOctets':sfpsAliasTableSwitchOctets,'sfpsAliasTableBaseOctets':sfpsAliasTableBaseOctets,'sfpsAliasTableAliasOctets':sfpsAliasTableAliasOctets,'sfpsAliasTableOpaqueTag':sfpsAliasTableOpaqueTag,'sfpsAliasTableVlanPolicy':sfpsAliasTableVlanPolicy,'sfpsAliasTableBaseLock':sfpsAliasTableBaseLock,'sfpsAliasTableAliasLock':sfpsAliasTableAliasLock,'sfpsAliasTableAliasState':sfpsAliasTableAliasState,'sfpsAliasTableSelf':sfpsAliasTableSelf,'sfpsAliasTableNext':sfpsAliasTableNext,'sfpsAliasTablePrev':sfpsAliasTablePrev,'sfpsAliasDeltaTable':sfpsAliasDeltaTable,'sfpsAliasDeltaTableEntry':sfpsAliasDeltaTableEntry,_r:sfpsAliasDeltaTableIndex,'sfpsAliasDeltaTablePort':sfpsAliasDeltaTablePort,'sfpsAliasDeltaTableBase':sfpsAliasDeltaTableBase,'sfpsAliasDeltaTableAlias':sfpsAliasDeltaTableAlias,'sfpsAliasDeltaTableAliasLength':sfpsAliasDeltaTableAliasLength,'sfpsAliasDeltaTableOpaqueTag':sfpsAliasDeltaTableOpaqueTag,'sfpsAliasDeltaTableAliasState':sfpsAliasDeltaTableAliasState,'sfpsAliasDeltaTableNodeLock':sfpsAliasDeltaTableNodeLock,'sfpsAliasDeltaTableAliasLock':sfpsAliasDeltaTableAliasLock,'sfpsAliasDeltaTableTimestamp':sfpsAliasDeltaTableTimestamp,'sfpsAliasDeltaCount':sfpsAliasDeltaCount,'sfpsAliasDeltaSetBack':sfpsAliasDeltaSetBack,'sfpsAliasDeltaFullFlag':sfpsAliasDeltaFullFlag,'sfpsDAPITestVerb':sfpsDAPITestVerb,'sfpsDAPITestSwitchMac':sfpsDAPITestSwitchMac,'sfpsDAPITestPort':sfpsDAPITestPort,'sfpsDAPITestAddrOneTag':sfpsDAPITestAddrOneTag,'sfpsDAPITestAddrOneValue':sfpsDAPITestAddrOneValue,'sfpsDAPITestAddrTwoTag':sfpsDAPITestAddrTwoTag,'sfpsDAPITestAddrTwoValue':sfpsDAPITestAddrTwoValue,'sfpsDAPITestCallTag':sfpsDAPITestCallTag,'sfpsDAPITestOutputTable':sfpsDAPITestOutputTable,'sfpsDAPITestOutputEntry':sfpsDAPITestOutputEntry,_u:sfpsDAPITestOutputIndex,'sfpsDAPITestOutputSwitchMac':sfpsDAPITestOutputSwitchMac,'sfpsDAPITestOutputPort':sfpsDAPITestOutputPort,'sfpsDAPITestOutputAddrOneTag':sfpsDAPITestOutputAddrOneTag,'sfpsDAPITestOutputAddrOneValue':sfpsDAPITestOutputAddrOneValue,'sfpsDAPITestOutputAddrTwoTag':sfpsDAPITestOutputAddrTwoTag,'sfpsDAPITestOutputAddrTwoValue':sfpsDAPITestOutputAddrTwoValue,'sfpsDAPITestOutputCallTag':sfpsDAPITestOutputCallTag,'sfpsDAPIVerb':sfpsDAPIVerb,'sfpsDAPIPort':sfpsDAPIPort,'sfpsDAPINodeType':sfpsDAPINodeType,'sfpsDAPINodeValue':sfpsDAPINodeValue,'sfpsDAPIAliasType':sfpsDAPIAliasType,'sfpsDAPIAliasValue':sfpsDAPIAliasValue,'sfpsDAPIAge':sfpsDAPIAge,'sfpsTopologyDirStatsTotalUsage':sfpsTopologyDirStatsTotalUsage,'sfpsTopologyDirStatsDynamicUsage':sfpsTopologyDirStatsDynamicUsage,'sfpsTopologyDirStatsNumOfNodes':sfpsTopologyDirStatsNumOfNodes,'sfpsTopologyDirStatsNodeUsage':sfpsTopologyDirStatsNodeUsage,'sfpsTopologyDirStatsNumLocalNodes':sfpsTopologyDirStatsNumLocalNodes,'sfpsTopologyDirStatsLocalNodeUsage':sfpsTopologyDirStatsLocalNodeUsage,'sfpsTopologyDirStatsMaxLocalNodes':sfpsTopologyDirStatsMaxLocalNodes,'sfpsTopologyDirStatsNumRemoteNodes':sfpsTopologyDirStatsNumRemoteNodes,'sfpsTopologyDirStatsRemoteNodeUsage':sfpsTopologyDirStatsRemoteNodeUsage,'sfpsTopologyDirStatsMaxRemoteNodes':sfpsTopologyDirStatsMaxRemoteNodes,'sfpsTopologyDirStatsNumOfAliases':sfpsTopologyDirStatsNumOfAliases,'sfpsTopologyDirStatsAliasUsage':sfpsTopologyDirStatsAliasUsage,'sfpsDirAliasStatsTable':sfpsDirAliasStatsTable,'sfpsDirAliasStatsEntry':sfpsDirAliasStatsEntry,_v:sfpsDirAliasStatsAliasType,'sfpsDirAliasStatsAliasName':sfpsDirAliasStatsAliasName,'sfpsDirAliasStatsNumOfAliases':sfpsDirAliasStatsNumOfAliases,'sfpsDirAliasStatsAliasUsage':sfpsDirAliasStatsAliasUsage,'sfpsDirAliasStatsMaxAliases':sfpsDirAliasStatsMaxAliases,'sfpsTopologyDirStatsStaticUsage':sfpsTopologyDirStatsStaticUsage,'sfpsTopologyDirStatsObjectsUsage':sfpsTopologyDirStatsObjectsUsage,'sfpsTopologyDirStatsNodeTableSize':sfpsTopologyDirStatsNodeTableSize,'sfpsTopologyDirStatsNodeTableUsage':sfpsTopologyDirStatsNodeTableUsage,'sfpsTopologyDirStatsAliasTableSize':sfpsTopologyDirStatsAliasTableSize,'sfpsTopologyDirStatsAliasTableUsage':sfpsTopologyDirStatsAliasTableUsage,'sfpsTopologyDirStatsNodeCollisions':sfpsTopologyDirStatsNodeCollisions,'sfpsTopologyDirStatsNodeLongestChain':sfpsTopologyDirStatsNodeLongestChain,'sfpsTopologyDirStatsAliasCollisions':sfpsTopologyDirStatsAliasCollisions,'sfpsTopologyDirStatsAliasLongestChain':sfpsTopologyDirStatsAliasLongestChain,'sfpsTopologyDirStatsLocalAddsRefused':sfpsTopologyDirStatsLocalAddsRefused,'sfpsTopologyDirStatsAliasRemotesReplaced':sfpsTopologyDirStatsAliasRemotesReplaced,'sfpsTopologyDirStatsAliasMultiPortClears':sfpsTopologyDirStatsAliasMultiPortClears,'sfpsTopologyDirStatsReservedForRemoteNodes':sfpsTopologyDirStatsReservedForRemoteNodes,'sfpsTopologyDirStatsNumSwitches':sfpsTopologyDirStatsNumSwitches,'sfpsTopologyDirStatsSwitchUsage':sfpsTopologyDirStatsSwitchUsage,'sfpsTopologyDirStatsMaxSwitches':sfpsTopologyDirStatsMaxSwitches,'sfpsTopologyDirStatsSwitchTableSize':sfpsTopologyDirStatsSwitchTableSize,'sfpsTopologyDirStatsSwitchTableUsage':sfpsTopologyDirStatsSwitchTableUsage,'sfpsTopologyDirStatsSwitchLookups':sfpsTopologyDirStatsSwitchLookups,'sfpsTopologyDirStatsSwitchCacheHits':sfpsTopologyDirStatsSwitchCacheHits,'sfpsTopologyDirStatsNumVlans':sfpsTopologyDirStatsNumVlans,'sfpsTopologyDirStatsVlanUsage':sfpsTopologyDirStatsVlanUsage,'sfpsTopologyDirStatsMaxVlans':sfpsTopologyDirStatsMaxVlans,'sfpsTopologyDirStatsVlanTableSize':sfpsTopologyDirStatsVlanTableSize,'sfpsTopologyDirStatsVlanTableUsage':sfpsTopologyDirStatsVlanTableUsage,'sfpsTopologyDirStatsVlanLookups':sfpsTopologyDirStatsVlanLookups,'sfpsTopologyDirStatsVlanCacheHits':sfpsTopologyDirStatsVlanCacheHits,'sfpsTopologyDirStatsNodeAliasMax':sfpsTopologyDirStatsNodeAliasMax,'sfpsTopologyDirStatsLocalAliasRefused':sfpsTopologyDirStatsLocalAliasRefused,'sfpsTopologyDirStatsRemoteAliasRemoved':sfpsTopologyDirStatsRemoteAliasRemoved,'sfpsDirFilterAPILockAdmin':sfpsDirFilterAPILockAdmin,'sfpsDirFilterAPILockStatus':sfpsDirFilterAPILockStatus,'sfpsDirFilterAPILockCount':sfpsDirFilterAPILockCount,'sfpsDirFilterAPIValueType':sfpsDirFilterAPIValueType,'sfpsDirFilterAPIValue':sfpsDirFilterAPIValue,'sfpsDirFilterAPILockTimeOut':sfpsDirFilterAPILockTimeOut,'sfpsDirFilterAPILockTimeElapsed':sfpsDirFilterAPILockTimeElapsed,'sfpsDirFilterNodeTable':sfpsDirFilterNodeTable,'sfpsDirFilterNodeEntry':sfpsDirFilterNodeEntry,_w:sfpsDirFilterNodeLockCount,_x:sfpsDirFilterNodeNodeIndex,_y:sfpsDirFilterNodeLinkIndex,'sfpsDirFilterNodeNodeCount':sfpsDirFilterNodeNodeCount,'sfpsDirFilterNodeLinkCount':sfpsDirFilterNodeLinkCount,'sfpsDirFilterNodeDomainName':sfpsDirFilterNodeDomainName,'sfpsDirFilterNodeChassisType':sfpsDirFilterNodeChassisType,'sfpsDirFilterNodeChassisLoad':sfpsDirFilterNodeChassisLoad,'sfpsDirFilterNodeSwitchType':sfpsDirFilterNodeSwitchType,'sfpsDirFilterNodeSwitchLoad':sfpsDirFilterNodeSwitchLoad,'sfpsDirFilterNodeInPort':sfpsDirFilterNodeInPort,'sfpsDirFilterNodeBaseType':sfpsDirFilterNodeBaseType,'sfpsDirFilterNodeBaseLoad':sfpsDirFilterNodeBaseLoad,'sfpsDirFilterNodeNodeState':sfpsDirFilterNodeNodeState,'sfpsDirFilterNodeNodeAge':sfpsDirFilterNodeNodeAge,'sfpsDirFilterNodeNodeLock':sfpsDirFilterNodeNodeLock,'sfpsDirFilterNodeLinkType':sfpsDirFilterNodeLinkType,'sfpsDirFilterNodeLinkLoad':sfpsDirFilterNodeLinkLoad,'sfpsDirFilterNodeLinkAge':sfpsDirFilterNodeLinkAge,'sfpsDirFilterNodeLinkLock':sfpsDirFilterNodeLinkLock,'sfpsDirFilterNodeVlanLearned':sfpsDirFilterNodeVlanLearned,'sfpsDirFilterNodeOpaqueTag':sfpsDirFilterNodeOpaqueTag,'sfpsDirFilterNodeChassisOctets':sfpsDirFilterNodeChassisOctets,'sfpsDirFilterNodeSwitchOctets':sfpsDirFilterNodeSwitchOctets,'sfpsDirFilterNodeNodeOctets':sfpsDirFilterNodeNodeOctets,'sfpsDirFilterNodeLinkOctets':sfpsDirFilterNodeLinkOctets,'sfpsDirFilterNodeNodeLocal':sfpsDirFilterNodeNodeLocal,'sfpsDirFilterNodeLinkState':sfpsDirFilterNodeLinkState,'sfpsDirFilterAliasTable':sfpsDirFilterAliasTable,'sfpsDirFilterAliasEntry':sfpsDirFilterAliasEntry,_A1:sfpsDirFilterAliasLockCount,_A2:sfpsDirFilterAliasAliasHash,_A3:sfpsDirFilterAliasBaseHash,_A4:sfpsDirFilterAliasHashIndex,'sfpsDirFilterAliasDomain':sfpsDirFilterAliasDomain,'sfpsDirFilterAliasChassisType':sfpsDirFilterAliasChassisType,'sfpsDirFilterAliasChassisLoad':sfpsDirFilterAliasChassisLoad,'sfpsDirFilterAliasSwitchType':sfpsDirFilterAliasSwitchType,'sfpsDirFilterAliasSwitchLoad':sfpsDirFilterAliasSwitchLoad,'sfpsDirFilterAliasInPort':sfpsDirFilterAliasInPort,'sfpsDirFilterAliasBaseType':sfpsDirFilterAliasBaseType,'sfpsDirFilterAliasBaseLoad':sfpsDirFilterAliasBaseLoad,'sfpsDirFilterAliasNodeState':sfpsDirFilterAliasNodeState,'sfpsDirFilterAliasNodeAge':sfpsDirFilterAliasNodeAge,'sfpsDirFilterAliasNodeLock':sfpsDirFilterAliasNodeLock,'sfpsDirFilterAliasLinkType':sfpsDirFilterAliasLinkType,'sfpsDirFilterAliasLinkLoad':sfpsDirFilterAliasLinkLoad,'sfpsDirFilterAliasLinkAge':sfpsDirFilterAliasLinkAge,'sfpsDirFilterAliasLinkLock':sfpsDirFilterAliasLinkLock,'sfpsDirFilterAliasVlanLearned':sfpsDirFilterAliasVlanLearned,'sfpsDirFilterAliasOpaqueTag':sfpsDirFilterAliasOpaqueTag,'sfpsDirFilterAliasChassisOctets':sfpsDirFilterAliasChassisOctets,'sfpsDirFilterAliasSwitchOctets':sfpsDirFilterAliasSwitchOctets,'sfpsDirFilterAliasNodeOctets':sfpsDirFilterAliasNodeOctets,'sfpsDirFilterAliasLinkOctets':sfpsDirFilterAliasLinkOctets,'sfpsDirFilterAliasNodeLocal':sfpsDirFilterAliasNodeLocal,'sfpsDirFilterAliasLinkState':sfpsDirFilterAliasLinkState})