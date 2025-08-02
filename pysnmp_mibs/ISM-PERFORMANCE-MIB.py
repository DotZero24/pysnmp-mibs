_AE='currentObjectGroup'
_AD='hwPerfControllerSMBV1Bps'
_AC='hwPerfPortLocation'
_AB='hwPerfFileSystemAvWrOPSRspTime'
_AA='hwPerfFileSystemAvRdOPSRspTime'
_A9='hwPerformanceSwitch'
_A8='hwPerfFileSystemWriteBandwidth'
_A7='hwPerfFileSystemWriteOPS'
_A6='hwPerfFileSystemReadBandwidth'
_A5='hwPerfFileSystemReadOPS'
_A4='hwPerfFileSystemServiceTime'
_A3='hwPerfFileSystemOPS'
_A2='hwPerfControllerSMBV2Bps'
_A1='hwPerfControllerSMBV2OPS'
_A0='hwPerfControllerSMBV1OPS'
_z='hwPerfControllerNFSV4Bps'
_y='hwPerfControllerNFSV4OPS'
_x='hwPerfControllerNFSV3OPS'
_w='hwPerfControllerNFSV3Bps'
_v='hwPerfNodeFileOPS'
_u='hwPerfNodeFileBandwidth'
_t='hwPerfPortMaxIOPS'
_s='hwPerfPortMaxTraffic'
_r='hwPerfLunMaxIOPS'
_q='hwPerfLunMaxTraffic'
_p='hwPerfCacheHitRatio'
_o='hwPerfCacheMirrorWriteUtilization'
_n='hwPerfCacheWriteUtilization'
_m='hwPerfCacheReadUtilization'
_l='hwPerfLunReadIORate'
_k='hwPerfLunWriteIORate'
_j='hwPerfNodeWriteTraffic'
_i='hwPerfNodeReadTraffic'
_h='hwPerfNodeTotalTraffic'
_g='hwPerfNodeWriteIOPS'
_f='hwPerfNodeReadIOPS'
_e='hwPerfNodeTotalIOPS'
_d='hwPerfNodeDelay'
_c='hwPerfPortWriteTraffic'
_b='hwPerfPortReadTraffic'
_a='hwPerfPortTotalTraffic'
_Z='hwPerfPortWriteIOPS'
_Y='hwPerfPortReadIOPS'
_X='hwPerfPortTotalIOPS'
_W='hwPerfPortDelay'
_V='hwPerfLunWriteTraffic'
_U='hwPerfLunReadTraffic'
_T='hwPerfLunTotalTraffic'
_S='hwPerfLunWriteIOPS'
_R='hwPerfLunReadIOPS'
_Q='hwPerfLunHitRate'
_P='hwPerfLunTotalIOPS'
_O='hwPerfNodeAvgCacheUsage'
_N='hwPerfNodeCPUUsage'
_M='Integer32'
_L='hwPerfFileSystemID'
_K='hwPerfControllerSMBV2ID'
_J='hwPerfControllerSMBV1ID'
_I='hwPerfControllerNFSV4ID'
_H='hwPerfControllerNFSV3ID'
_G='hwPerfCacheID'
_F='hwPerfPortIfIndex'
_E='hwPerfLunID'
_D='hwPerfNodeIfIndex'
_C='read-only'
_B='ISM-PERFORMANCE-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_M,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
hwStorage=ModuleIdentity((1,3,6,1,4,1,34774,4))
if mibBuilder.loadTexts:hwStorage.setRevisions(('2013-04-07 17:16',))
class NodeCodeString(TextualConvention,OctetString):status=_A;displayHint='255a';subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(15,17))
_Huaweistorage_ObjectIdentity=ObjectIdentity
huaweistorage=_Huaweistorage_ObjectIdentity((1,3,6,1,4,1,34774))
_HwISM_ObjectIdentity=ObjectIdentity
hwISM=_HwISM_ObjectIdentity((1,3,6,1,4,1,34774,4,1))
_HwPerformance_ObjectIdentity=ObjectIdentity
hwPerformance=_HwPerformance_ObjectIdentity((1,3,6,1,4,1,34774,4,1,21))
class _HwPerformanceSwitch_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_HwPerformanceSwitch_Type.__name__=_M
_HwPerformanceSwitch_Object=MibScalar
hwPerformanceSwitch=_HwPerformanceSwitch_Object((1,3,6,1,4,1,34774,4,1,21,1),_HwPerformanceSwitch_Type())
hwPerformanceSwitch.setMaxAccess('read-write')
if mibBuilder.loadTexts:hwPerformanceSwitch.setStatus(_A)
_HwPerfNodeTable_Object=MibTable
hwPerfNodeTable=_HwPerfNodeTable_Object((1,3,6,1,4,1,34774,4,1,21,3))
if mibBuilder.loadTexts:hwPerfNodeTable.setStatus(_A)
_HwPerfNodeEntry_Object=MibTableRow
hwPerfNodeEntry=_HwPerfNodeEntry_Object((1,3,6,1,4,1,34774,4,1,21,3,1))
hwPerfNodeEntry.setIndexNames((0,_B,_D))
if mibBuilder.loadTexts:hwPerfNodeEntry.setStatus(_A)
_HwPerfNodeIfIndex_Type=Unsigned32
_HwPerfNodeIfIndex_Object=MibTableColumn
hwPerfNodeIfIndex=_HwPerfNodeIfIndex_Object((1,3,6,1,4,1,34774,4,1,21,3,1,1),_HwPerfNodeIfIndex_Type())
hwPerfNodeIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:hwPerfNodeIfIndex.setStatus(_A)
_HwPerfNodeCPUUsage_Type=Unsigned32
_HwPerfNodeCPUUsage_Object=MibTableColumn
hwPerfNodeCPUUsage=_HwPerfNodeCPUUsage_Object((1,3,6,1,4,1,34774,4,1,21,3,1,2),_HwPerfNodeCPUUsage_Type())
hwPerfNodeCPUUsage.setMaxAccess(_C)
if mibBuilder.loadTexts:hwPerfNodeCPUUsage.setStatus(_A)
_HwPerfNodeAvgCacheUsage_Type=Unsigned32
_HwPerfNodeAvgCacheUsage_Object=MibTableColumn
hwPerfNodeAvgCacheUsage=_HwPerfNodeAvgCacheUsage_Object((1,3,6,1,4,1,34774,4,1,21,3,1,3),_HwPerfNodeAvgCacheUsage_Type())
hwPerfNodeAvgCacheUsage.setMaxAccess(_C)
if mibBuilder.loadTexts:hwPerfNodeAvgCacheUsage.setStatus(_A)
_HwPerfNodeDelay_Type=Unsigned32
_HwPerfNodeDelay_Object=MibTableColumn
hwPerfNodeDelay=_HwPerfNodeDelay_Object((1,3,6,1,4,1,34774,4,1,21,3,1,4),_HwPerfNodeDelay_Type())
hwPerfNodeDelay.setMaxAccess(_C)
if mibBuilder.loadTexts:hwPerfNodeDelay.setStatus(_A)
_HwPerfNodeTotalIOPS_Type=Unsigned32
_HwPerfNodeTotalIOPS_Object=MibTableColumn
hwPerfNodeTotalIOPS=_HwPerfNodeTotalIOPS_Object((1,3,6,1,4,1,34774,4,1,21,3,1,5),_HwPerfNodeTotalIOPS_Type())
hwPerfNodeTotalIOPS.setMaxAccess(_C)
if mibBuilder.loadTexts:hwPerfNodeTotalIOPS.setStatus(_A)
_HwPerfNodeReadIOPS_Type=Unsigned32
_HwPerfNodeReadIOPS_Object=MibTableColumn
hwPerfNodeReadIOPS=_HwPerfNodeReadIOPS_Object((1,3,6,1,4,1,34774,4,1,21,3,1,6),_HwPerfNodeReadIOPS_Type())
hwPerfNodeReadIOPS.setMaxAccess(_C)
if mibBuilder.loadTexts:hwPerfNodeReadIOPS.setStatus(_A)
_HwPerfNodeWriteIOPS_Type=Unsigned32
_HwPerfNodeWriteIOPS_Object=MibTableColumn
hwPerfNodeWriteIOPS=_HwPerfNodeWriteIOPS_Object((1,3,6,1,4,1,34774,4,1,21,3,1,7),_HwPerfNodeWriteIOPS_Type())
hwPerfNodeWriteIOPS.setMaxAccess(_C)
if mibBuilder.loadTexts:hwPerfNodeWriteIOPS.setStatus(_A)
_HwPerfNodeTotalTraffic_Type=Unsigned32
_HwPerfNodeTotalTraffic_Object=MibTableColumn
hwPerfNodeTotalTraffic=_HwPerfNodeTotalTraffic_Object((1,3,6,1,4,1,34774,4,1,21,3,1,8),_HwPerfNodeTotalTraffic_Type())
hwPerfNodeTotalTraffic.setMaxAccess(_C)
if mibBuilder.loadTexts:hwPerfNodeTotalTraffic.setStatus(_A)
_HwPerfNodeReadTraffic_Type=Unsigned32
_HwPerfNodeReadTraffic_Object=MibTableColumn
hwPerfNodeReadTraffic=_HwPerfNodeReadTraffic_Object((1,3,6,1,4,1,34774,4,1,21,3,1,9),_HwPerfNodeReadTraffic_Type())
hwPerfNodeReadTraffic.setMaxAccess(_C)
if mibBuilder.loadTexts:hwPerfNodeReadTraffic.setStatus(_A)
_HwPerfNodeWriteTraffic_Type=Unsigned32
_HwPerfNodeWriteTraffic_Object=MibTableColumn
hwPerfNodeWriteTraffic=_HwPerfNodeWriteTraffic_Object((1,3,6,1,4,1,34774,4,1,21,3,1,10),_HwPerfNodeWriteTraffic_Type())
hwPerfNodeWriteTraffic.setMaxAccess(_C)
if mibBuilder.loadTexts:hwPerfNodeWriteTraffic.setStatus(_A)
_HwPerfNodeFileBandwidth_Type=Counter64
_HwPerfNodeFileBandwidth_Object=MibTableColumn
hwPerfNodeFileBandwidth=_HwPerfNodeFileBandwidth_Object((1,3,6,1,4,1,34774,4,1,21,3,1,11),_HwPerfNodeFileBandwidth_Type())
hwPerfNodeFileBandwidth.setMaxAccess(_C)
if mibBuilder.loadTexts:hwPerfNodeFileBandwidth.setStatus(_A)
_HwPerfNodeFileOPS_Type=Counter64
_HwPerfNodeFileOPS_Object=MibTableColumn
hwPerfNodeFileOPS=_HwPerfNodeFileOPS_Object((1,3,6,1,4,1,34774,4,1,21,3,1,12),_HwPerfNodeFileOPS_Type())
hwPerfNodeFileOPS.setMaxAccess(_C)
if mibBuilder.loadTexts:hwPerfNodeFileOPS.setStatus(_A)
_HwPerfLunTable_Object=MibTable
hwPerfLunTable=_HwPerfLunTable_Object((1,3,6,1,4,1,34774,4,1,21,4))
if mibBuilder.loadTexts:hwPerfLunTable.setStatus(_A)
_HwPerfLunEntry_Object=MibTableRow
hwPerfLunEntry=_HwPerfLunEntry_Object((1,3,6,1,4,1,34774,4,1,21,4,1))
hwPerfLunEntry.setIndexNames((0,_B,_E))
if mibBuilder.loadTexts:hwPerfLunEntry.setStatus(_A)
_HwPerfLunID_Type=Unsigned32
_HwPerfLunID_Object=MibTableColumn
hwPerfLunID=_HwPerfLunID_Object((1,3,6,1,4,1,34774,4,1,21,4,1,1),_HwPerfLunID_Type())
hwPerfLunID.setMaxAccess(_C)
if mibBuilder.loadTexts:hwPerfLunID.setStatus(_A)
_HwPerfLunHitRate_Type=Unsigned32
_HwPerfLunHitRate_Object=MibTableColumn
hwPerfLunHitRate=_HwPerfLunHitRate_Object((1,3,6,1,4,1,34774,4,1,21,4,1,2),_HwPerfLunHitRate_Type())
hwPerfLunHitRate.setMaxAccess(_C)
if mibBuilder.loadTexts:hwPerfLunHitRate.setStatus(_A)
_HwPerfLunTotalIOPS_Type=Unsigned32
_HwPerfLunTotalIOPS_Object=MibTableColumn
hwPerfLunTotalIOPS=_HwPerfLunTotalIOPS_Object((1,3,6,1,4,1,34774,4,1,21,4,1,3),_HwPerfLunTotalIOPS_Type())
hwPerfLunTotalIOPS.setMaxAccess(_C)
if mibBuilder.loadTexts:hwPerfLunTotalIOPS.setStatus(_A)
_HwPerfLunReadIOPS_Type=Unsigned32
_HwPerfLunReadIOPS_Object=MibTableColumn
hwPerfLunReadIOPS=_HwPerfLunReadIOPS_Object((1,3,6,1,4,1,34774,4,1,21,4,1,4),_HwPerfLunReadIOPS_Type())
hwPerfLunReadIOPS.setMaxAccess(_C)
if mibBuilder.loadTexts:hwPerfLunReadIOPS.setStatus(_A)
_HwPerfLunWriteIOPS_Type=Unsigned32
_HwPerfLunWriteIOPS_Object=MibTableColumn
hwPerfLunWriteIOPS=_HwPerfLunWriteIOPS_Object((1,3,6,1,4,1,34774,4,1,21,4,1,5),_HwPerfLunWriteIOPS_Type())
hwPerfLunWriteIOPS.setMaxAccess(_C)
if mibBuilder.loadTexts:hwPerfLunWriteIOPS.setStatus(_A)
_HwPerfLunTotalTraffic_Type=Unsigned32
_HwPerfLunTotalTraffic_Object=MibTableColumn
hwPerfLunTotalTraffic=_HwPerfLunTotalTraffic_Object((1,3,6,1,4,1,34774,4,1,21,4,1,6),_HwPerfLunTotalTraffic_Type())
hwPerfLunTotalTraffic.setMaxAccess(_C)
if mibBuilder.loadTexts:hwPerfLunTotalTraffic.setStatus(_A)
_HwPerfLunReadTraffic_Type=Unsigned32
_HwPerfLunReadTraffic_Object=MibTableColumn
hwPerfLunReadTraffic=_HwPerfLunReadTraffic_Object((1,3,6,1,4,1,34774,4,1,21,4,1,7),_HwPerfLunReadTraffic_Type())
hwPerfLunReadTraffic.setMaxAccess(_C)
if mibBuilder.loadTexts:hwPerfLunReadTraffic.setStatus(_A)
_HwPerfLunWriteTraffic_Type=Unsigned32
_HwPerfLunWriteTraffic_Object=MibTableColumn
hwPerfLunWriteTraffic=_HwPerfLunWriteTraffic_Object((1,3,6,1,4,1,34774,4,1,21,4,1,8),_HwPerfLunWriteTraffic_Type())
hwPerfLunWriteTraffic.setMaxAccess(_C)
if mibBuilder.loadTexts:hwPerfLunWriteTraffic.setStatus(_A)
_HwPerfLunReadIORate_Type=Unsigned32
_HwPerfLunReadIORate_Object=MibTableColumn
hwPerfLunReadIORate=_HwPerfLunReadIORate_Object((1,3,6,1,4,1,34774,4,1,21,4,1,9),_HwPerfLunReadIORate_Type())
hwPerfLunReadIORate.setMaxAccess(_C)
if mibBuilder.loadTexts:hwPerfLunReadIORate.setStatus(_A)
_HwPerfLunWriteIORate_Type=Unsigned32
_HwPerfLunWriteIORate_Object=MibTableColumn
hwPerfLunWriteIORate=_HwPerfLunWriteIORate_Object((1,3,6,1,4,1,34774,4,1,21,4,1,10),_HwPerfLunWriteIORate_Type())
hwPerfLunWriteIORate.setMaxAccess(_C)
if mibBuilder.loadTexts:hwPerfLunWriteIORate.setStatus(_A)
_HwPerfLunMaxTraffic_Type=Unsigned32
_HwPerfLunMaxTraffic_Object=MibTableColumn
hwPerfLunMaxTraffic=_HwPerfLunMaxTraffic_Object((1,3,6,1,4,1,34774,4,1,21,4,1,11),_HwPerfLunMaxTraffic_Type())
hwPerfLunMaxTraffic.setMaxAccess(_C)
if mibBuilder.loadTexts:hwPerfLunMaxTraffic.setStatus(_A)
_HwPerfLunMaxIOPS_Type=Unsigned32
_HwPerfLunMaxIOPS_Object=MibTableColumn
hwPerfLunMaxIOPS=_HwPerfLunMaxIOPS_Object((1,3,6,1,4,1,34774,4,1,21,4,1,12),_HwPerfLunMaxIOPS_Type())
hwPerfLunMaxIOPS.setMaxAccess(_C)
if mibBuilder.loadTexts:hwPerfLunMaxIOPS.setStatus(_A)
_HwPerfPortTable_Object=MibTable
hwPerfPortTable=_HwPerfPortTable_Object((1,3,6,1,4,1,34774,4,1,21,5))
if mibBuilder.loadTexts:hwPerfPortTable.setStatus(_A)
_HwPerfPortEntry_Object=MibTableRow
hwPerfPortEntry=_HwPerfPortEntry_Object((1,3,6,1,4,1,34774,4,1,21,5,1))
hwPerfPortEntry.setIndexNames((0,_B,_F))
if mibBuilder.loadTexts:hwPerfPortEntry.setStatus(_A)
_HwPerfPortIfIndex_Type=Unsigned32
_HwPerfPortIfIndex_Object=MibTableColumn
hwPerfPortIfIndex=_HwPerfPortIfIndex_Object((1,3,6,1,4,1,34774,4,1,21,5,1,1),_HwPerfPortIfIndex_Type())
hwPerfPortIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:hwPerfPortIfIndex.setStatus(_A)
_HwPerfPortDelay_Type=Unsigned32
_HwPerfPortDelay_Object=MibTableColumn
hwPerfPortDelay=_HwPerfPortDelay_Object((1,3,6,1,4,1,34774,4,1,21,5,1,2),_HwPerfPortDelay_Type())
hwPerfPortDelay.setMaxAccess(_C)
if mibBuilder.loadTexts:hwPerfPortDelay.setStatus(_A)
_HwPerfPortTotalIOPS_Type=Unsigned32
_HwPerfPortTotalIOPS_Object=MibTableColumn
hwPerfPortTotalIOPS=_HwPerfPortTotalIOPS_Object((1,3,6,1,4,1,34774,4,1,21,5,1,3),_HwPerfPortTotalIOPS_Type())
hwPerfPortTotalIOPS.setMaxAccess(_C)
if mibBuilder.loadTexts:hwPerfPortTotalIOPS.setStatus(_A)
_HwPerfPortReadIOPS_Type=Unsigned32
_HwPerfPortReadIOPS_Object=MibTableColumn
hwPerfPortReadIOPS=_HwPerfPortReadIOPS_Object((1,3,6,1,4,1,34774,4,1,21,5,1,4),_HwPerfPortReadIOPS_Type())
hwPerfPortReadIOPS.setMaxAccess(_C)
if mibBuilder.loadTexts:hwPerfPortReadIOPS.setStatus(_A)
_HwPerfPortWriteIOPS_Type=Unsigned32
_HwPerfPortWriteIOPS_Object=MibTableColumn
hwPerfPortWriteIOPS=_HwPerfPortWriteIOPS_Object((1,3,6,1,4,1,34774,4,1,21,5,1,5),_HwPerfPortWriteIOPS_Type())
hwPerfPortWriteIOPS.setMaxAccess(_C)
if mibBuilder.loadTexts:hwPerfPortWriteIOPS.setStatus(_A)
_HwPerfPortTotalTraffic_Type=Unsigned32
_HwPerfPortTotalTraffic_Object=MibTableColumn
hwPerfPortTotalTraffic=_HwPerfPortTotalTraffic_Object((1,3,6,1,4,1,34774,4,1,21,5,1,6),_HwPerfPortTotalTraffic_Type())
hwPerfPortTotalTraffic.setMaxAccess(_C)
if mibBuilder.loadTexts:hwPerfPortTotalTraffic.setStatus(_A)
_HwPerfPortReadTraffic_Type=Unsigned32
_HwPerfPortReadTraffic_Object=MibTableColumn
hwPerfPortReadTraffic=_HwPerfPortReadTraffic_Object((1,3,6,1,4,1,34774,4,1,21,5,1,7),_HwPerfPortReadTraffic_Type())
hwPerfPortReadTraffic.setMaxAccess(_C)
if mibBuilder.loadTexts:hwPerfPortReadTraffic.setStatus(_A)
_HwPerfPortWriteTraffic_Type=Unsigned32
_HwPerfPortWriteTraffic_Object=MibTableColumn
hwPerfPortWriteTraffic=_HwPerfPortWriteTraffic_Object((1,3,6,1,4,1,34774,4,1,21,5,1,8),_HwPerfPortWriteTraffic_Type())
hwPerfPortWriteTraffic.setMaxAccess(_C)
if mibBuilder.loadTexts:hwPerfPortWriteTraffic.setStatus(_A)
_HwPerfPortMaxTraffic_Type=Unsigned32
_HwPerfPortMaxTraffic_Object=MibTableColumn
hwPerfPortMaxTraffic=_HwPerfPortMaxTraffic_Object((1,3,6,1,4,1,34774,4,1,21,5,1,9),_HwPerfPortMaxTraffic_Type())
hwPerfPortMaxTraffic.setMaxAccess(_C)
if mibBuilder.loadTexts:hwPerfPortMaxTraffic.setStatus(_A)
_HwPerfPortMaxIOPS_Type=Unsigned32
_HwPerfPortMaxIOPS_Object=MibTableColumn
hwPerfPortMaxIOPS=_HwPerfPortMaxIOPS_Object((1,3,6,1,4,1,34774,4,1,21,5,1,10),_HwPerfPortMaxIOPS_Type())
hwPerfPortMaxIOPS.setMaxAccess(_C)
if mibBuilder.loadTexts:hwPerfPortMaxIOPS.setStatus(_A)
_HwPerfPortLocation_Type=OctetString
_HwPerfPortLocation_Object=MibTableColumn
hwPerfPortLocation=_HwPerfPortLocation_Object((1,3,6,1,4,1,34774,4,1,21,5,1,11),_HwPerfPortLocation_Type())
hwPerfPortLocation.setMaxAccess(_C)
if mibBuilder.loadTexts:hwPerfPortLocation.setStatus(_A)
_HwPerfCacheTable_Object=MibTable
hwPerfCacheTable=_HwPerfCacheTable_Object((1,3,6,1,4,1,34774,4,1,21,7))
if mibBuilder.loadTexts:hwPerfCacheTable.setStatus(_A)
_HwPerfCacheEntry_Object=MibTableRow
hwPerfCacheEntry=_HwPerfCacheEntry_Object((1,3,6,1,4,1,34774,4,1,21,7,1))
hwPerfCacheEntry.setIndexNames((0,_B,_G))
if mibBuilder.loadTexts:hwPerfCacheEntry.setStatus(_A)
_HwPerfCacheID_Type=Unsigned32
_HwPerfCacheID_Object=MibTableColumn
hwPerfCacheID=_HwPerfCacheID_Object((1,3,6,1,4,1,34774,4,1,21,7,1,1),_HwPerfCacheID_Type())
hwPerfCacheID.setMaxAccess(_C)
if mibBuilder.loadTexts:hwPerfCacheID.setStatus(_A)
_HwPerfCacheReadUtilization_Type=Integer32
_HwPerfCacheReadUtilization_Object=MibTableColumn
hwPerfCacheReadUtilization=_HwPerfCacheReadUtilization_Object((1,3,6,1,4,1,34774,4,1,21,7,1,2),_HwPerfCacheReadUtilization_Type())
hwPerfCacheReadUtilization.setMaxAccess(_C)
if mibBuilder.loadTexts:hwPerfCacheReadUtilization.setStatus(_A)
_HwPerfCacheWriteUtilization_Type=Integer32
_HwPerfCacheWriteUtilization_Object=MibTableColumn
hwPerfCacheWriteUtilization=_HwPerfCacheWriteUtilization_Object((1,3,6,1,4,1,34774,4,1,21,7,1,3),_HwPerfCacheWriteUtilization_Type())
hwPerfCacheWriteUtilization.setMaxAccess(_C)
if mibBuilder.loadTexts:hwPerfCacheWriteUtilization.setStatus(_A)
_HwPerfCacheMirrorWriteUtilization_Type=Integer32
_HwPerfCacheMirrorWriteUtilization_Object=MibTableColumn
hwPerfCacheMirrorWriteUtilization=_HwPerfCacheMirrorWriteUtilization_Object((1,3,6,1,4,1,34774,4,1,21,7,1,4),_HwPerfCacheMirrorWriteUtilization_Type())
hwPerfCacheMirrorWriteUtilization.setMaxAccess(_C)
if mibBuilder.loadTexts:hwPerfCacheMirrorWriteUtilization.setStatus(_A)
_HwPerfCacheHitRatio_Type=Integer32
_HwPerfCacheHitRatio_Object=MibTableColumn
hwPerfCacheHitRatio=_HwPerfCacheHitRatio_Object((1,3,6,1,4,1,34774,4,1,21,7,1,5),_HwPerfCacheHitRatio_Type())
hwPerfCacheHitRatio.setMaxAccess(_C)
if mibBuilder.loadTexts:hwPerfCacheHitRatio.setStatus(_A)
_HwPerfControllerNFSV3Table_Object=MibTable
hwPerfControllerNFSV3Table=_HwPerfControllerNFSV3Table_Object((1,3,6,1,4,1,34774,4,1,21,10))
if mibBuilder.loadTexts:hwPerfControllerNFSV3Table.setStatus(_A)
_HwPerfControllerNFSV3Entry_Object=MibTableRow
hwPerfControllerNFSV3Entry=_HwPerfControllerNFSV3Entry_Object((1,3,6,1,4,1,34774,4,1,21,10,1))
hwPerfControllerNFSV3Entry.setIndexNames((0,_B,_H))
if mibBuilder.loadTexts:hwPerfControllerNFSV3Entry.setStatus(_A)
_HwPerfControllerNFSV3ID_Type=OctetString
_HwPerfControllerNFSV3ID_Object=MibTableColumn
hwPerfControllerNFSV3ID=_HwPerfControllerNFSV3ID_Object((1,3,6,1,4,1,34774,4,1,21,10,1,1),_HwPerfControllerNFSV3ID_Type())
hwPerfControllerNFSV3ID.setMaxAccess(_C)
if mibBuilder.loadTexts:hwPerfControllerNFSV3ID.setStatus(_A)
_HwPerfControllerNFSV3OPS_Type=Counter64
_HwPerfControllerNFSV3OPS_Object=MibTableColumn
hwPerfControllerNFSV3OPS=_HwPerfControllerNFSV3OPS_Object((1,3,6,1,4,1,34774,4,1,21,10,1,2),_HwPerfControllerNFSV3OPS_Type())
hwPerfControllerNFSV3OPS.setMaxAccess(_C)
if mibBuilder.loadTexts:hwPerfControllerNFSV3OPS.setStatus(_A)
_HwPerfControllerNFSV3Bps_Type=Counter64
_HwPerfControllerNFSV3Bps_Object=MibTableColumn
hwPerfControllerNFSV3Bps=_HwPerfControllerNFSV3Bps_Object((1,3,6,1,4,1,34774,4,1,21,10,1,3),_HwPerfControllerNFSV3Bps_Type())
hwPerfControllerNFSV3Bps.setMaxAccess(_C)
if mibBuilder.loadTexts:hwPerfControllerNFSV3Bps.setStatus(_A)
_HwPerfControllerNFSV4Table_Object=MibTable
hwPerfControllerNFSV4Table=_HwPerfControllerNFSV4Table_Object((1,3,6,1,4,1,34774,4,1,21,11))
if mibBuilder.loadTexts:hwPerfControllerNFSV4Table.setStatus(_A)
_HwPerfControllerNFSV4Entry_Object=MibTableRow
hwPerfControllerNFSV4Entry=_HwPerfControllerNFSV4Entry_Object((1,3,6,1,4,1,34774,4,1,21,11,1))
hwPerfControllerNFSV4Entry.setIndexNames((0,_B,_I))
if mibBuilder.loadTexts:hwPerfControllerNFSV4Entry.setStatus(_A)
_HwPerfControllerNFSV4ID_Type=OctetString
_HwPerfControllerNFSV4ID_Object=MibTableColumn
hwPerfControllerNFSV4ID=_HwPerfControllerNFSV4ID_Object((1,3,6,1,4,1,34774,4,1,21,11,1,1),_HwPerfControllerNFSV4ID_Type())
hwPerfControllerNFSV4ID.setMaxAccess(_C)
if mibBuilder.loadTexts:hwPerfControllerNFSV4ID.setStatus(_A)
_HwPerfControllerNFSV4OPS_Type=Counter64
_HwPerfControllerNFSV4OPS_Object=MibTableColumn
hwPerfControllerNFSV4OPS=_HwPerfControllerNFSV4OPS_Object((1,3,6,1,4,1,34774,4,1,21,11,1,2),_HwPerfControllerNFSV4OPS_Type())
hwPerfControllerNFSV4OPS.setMaxAccess(_C)
if mibBuilder.loadTexts:hwPerfControllerNFSV4OPS.setStatus(_A)
_HwPerfControllerNFSV4Bps_Type=Counter64
_HwPerfControllerNFSV4Bps_Object=MibTableColumn
hwPerfControllerNFSV4Bps=_HwPerfControllerNFSV4Bps_Object((1,3,6,1,4,1,34774,4,1,21,11,1,3),_HwPerfControllerNFSV4Bps_Type())
hwPerfControllerNFSV4Bps.setMaxAccess(_C)
if mibBuilder.loadTexts:hwPerfControllerNFSV4Bps.setStatus(_A)
_HwPerfControllerSMBV1Table_Object=MibTable
hwPerfControllerSMBV1Table=_HwPerfControllerSMBV1Table_Object((1,3,6,1,4,1,34774,4,1,21,12))
if mibBuilder.loadTexts:hwPerfControllerSMBV1Table.setStatus(_A)
_HwPerfControllerSMBV1Entry_Object=MibTableRow
hwPerfControllerSMBV1Entry=_HwPerfControllerSMBV1Entry_Object((1,3,6,1,4,1,34774,4,1,21,12,1))
hwPerfControllerSMBV1Entry.setIndexNames((0,_B,_J))
if mibBuilder.loadTexts:hwPerfControllerSMBV1Entry.setStatus(_A)
_HwPerfControllerSMBV1ID_Type=OctetString
_HwPerfControllerSMBV1ID_Object=MibTableColumn
hwPerfControllerSMBV1ID=_HwPerfControllerSMBV1ID_Object((1,3,6,1,4,1,34774,4,1,21,12,1,1),_HwPerfControllerSMBV1ID_Type())
hwPerfControllerSMBV1ID.setMaxAccess(_C)
if mibBuilder.loadTexts:hwPerfControllerSMBV1ID.setStatus(_A)
_HwPerfControllerSMBV1OPS_Type=Counter64
_HwPerfControllerSMBV1OPS_Object=MibTableColumn
hwPerfControllerSMBV1OPS=_HwPerfControllerSMBV1OPS_Object((1,3,6,1,4,1,34774,4,1,21,12,1,2),_HwPerfControllerSMBV1OPS_Type())
hwPerfControllerSMBV1OPS.setMaxAccess(_C)
if mibBuilder.loadTexts:hwPerfControllerSMBV1OPS.setStatus(_A)
_HwPerfControllerSMBV1Bps_Type=Counter64
_HwPerfControllerSMBV1Bps_Object=MibTableColumn
hwPerfControllerSMBV1Bps=_HwPerfControllerSMBV1Bps_Object((1,3,6,1,4,1,34774,4,1,21,12,1,3),_HwPerfControllerSMBV1Bps_Type())
hwPerfControllerSMBV1Bps.setMaxAccess(_C)
if mibBuilder.loadTexts:hwPerfControllerSMBV1Bps.setStatus(_A)
_HwPerfControllerSMBV2Table_Object=MibTable
hwPerfControllerSMBV2Table=_HwPerfControllerSMBV2Table_Object((1,3,6,1,4,1,34774,4,1,21,13))
if mibBuilder.loadTexts:hwPerfControllerSMBV2Table.setStatus(_A)
_HwPerfControllerSMBV2Entry_Object=MibTableRow
hwPerfControllerSMBV2Entry=_HwPerfControllerSMBV2Entry_Object((1,3,6,1,4,1,34774,4,1,21,13,1))
hwPerfControllerSMBV2Entry.setIndexNames((0,_B,_K))
if mibBuilder.loadTexts:hwPerfControllerSMBV2Entry.setStatus(_A)
_HwPerfControllerSMBV2ID_Type=OctetString
_HwPerfControllerSMBV2ID_Object=MibTableColumn
hwPerfControllerSMBV2ID=_HwPerfControllerSMBV2ID_Object((1,3,6,1,4,1,34774,4,1,21,13,1,1),_HwPerfControllerSMBV2ID_Type())
hwPerfControllerSMBV2ID.setMaxAccess(_C)
if mibBuilder.loadTexts:hwPerfControllerSMBV2ID.setStatus(_A)
_HwPerfControllerSMBV2OPS_Type=Counter64
_HwPerfControllerSMBV2OPS_Object=MibTableColumn
hwPerfControllerSMBV2OPS=_HwPerfControllerSMBV2OPS_Object((1,3,6,1,4,1,34774,4,1,21,13,1,2),_HwPerfControllerSMBV2OPS_Type())
hwPerfControllerSMBV2OPS.setMaxAccess(_C)
if mibBuilder.loadTexts:hwPerfControllerSMBV2OPS.setStatus(_A)
_HwPerfControllerSMBV2Bps_Type=Counter64
_HwPerfControllerSMBV2Bps_Object=MibTableColumn
hwPerfControllerSMBV2Bps=_HwPerfControllerSMBV2Bps_Object((1,3,6,1,4,1,34774,4,1,21,13,1,3),_HwPerfControllerSMBV2Bps_Type())
hwPerfControllerSMBV2Bps.setMaxAccess(_C)
if mibBuilder.loadTexts:hwPerfControllerSMBV2Bps.setStatus(_A)
_HwPerfFileSystemTable_Object=MibTable
hwPerfFileSystemTable=_HwPerfFileSystemTable_Object((1,3,6,1,4,1,34774,4,1,21,14))
if mibBuilder.loadTexts:hwPerfFileSystemTable.setStatus(_A)
_HwPerfFileSystemEntry_Object=MibTableRow
hwPerfFileSystemEntry=_HwPerfFileSystemEntry_Object((1,3,6,1,4,1,34774,4,1,21,14,1))
hwPerfFileSystemEntry.setIndexNames((0,_B,_L))
if mibBuilder.loadTexts:hwPerfFileSystemEntry.setStatus(_A)
_HwPerfFileSystemID_Type=OctetString
_HwPerfFileSystemID_Object=MibTableColumn
hwPerfFileSystemID=_HwPerfFileSystemID_Object((1,3,6,1,4,1,34774,4,1,21,14,1,1),_HwPerfFileSystemID_Type())
hwPerfFileSystemID.setMaxAccess(_C)
if mibBuilder.loadTexts:hwPerfFileSystemID.setStatus(_A)
_HwPerfFileSystemOPS_Type=Counter64
_HwPerfFileSystemOPS_Object=MibTableColumn
hwPerfFileSystemOPS=_HwPerfFileSystemOPS_Object((1,3,6,1,4,1,34774,4,1,21,14,1,2),_HwPerfFileSystemOPS_Type())
hwPerfFileSystemOPS.setMaxAccess(_C)
if mibBuilder.loadTexts:hwPerfFileSystemOPS.setStatus(_A)
_HwPerfFileSystemServiceTime_Type=Counter64
_HwPerfFileSystemServiceTime_Object=MibTableColumn
hwPerfFileSystemServiceTime=_HwPerfFileSystemServiceTime_Object((1,3,6,1,4,1,34774,4,1,21,14,1,3),_HwPerfFileSystemServiceTime_Type())
hwPerfFileSystemServiceTime.setMaxAccess(_C)
if mibBuilder.loadTexts:hwPerfFileSystemServiceTime.setStatus(_A)
_HwPerfFileSystemReadOPS_Type=Counter64
_HwPerfFileSystemReadOPS_Object=MibTableColumn
hwPerfFileSystemReadOPS=_HwPerfFileSystemReadOPS_Object((1,3,6,1,4,1,34774,4,1,21,14,1,4),_HwPerfFileSystemReadOPS_Type())
hwPerfFileSystemReadOPS.setMaxAccess(_C)
if mibBuilder.loadTexts:hwPerfFileSystemReadOPS.setStatus(_A)
_HwPerfFileSystemReadBandwidth_Type=Counter64
_HwPerfFileSystemReadBandwidth_Object=MibTableColumn
hwPerfFileSystemReadBandwidth=_HwPerfFileSystemReadBandwidth_Object((1,3,6,1,4,1,34774,4,1,21,14,1,5),_HwPerfFileSystemReadBandwidth_Type())
hwPerfFileSystemReadBandwidth.setMaxAccess(_C)
if mibBuilder.loadTexts:hwPerfFileSystemReadBandwidth.setStatus(_A)
_HwPerfFileSystemAvRdOPSRspTime_Type=Counter64
_HwPerfFileSystemAvRdOPSRspTime_Object=MibTableColumn
hwPerfFileSystemAvRdOPSRspTime=_HwPerfFileSystemAvRdOPSRspTime_Object((1,3,6,1,4,1,34774,4,1,21,14,1,6),_HwPerfFileSystemAvRdOPSRspTime_Type())
hwPerfFileSystemAvRdOPSRspTime.setMaxAccess(_C)
if mibBuilder.loadTexts:hwPerfFileSystemAvRdOPSRspTime.setStatus(_A)
_HwPerfFileSystemAvWrOPSRspTime_Type=Counter64
_HwPerfFileSystemAvWrOPSRspTime_Object=MibTableColumn
hwPerfFileSystemAvWrOPSRspTime=_HwPerfFileSystemAvWrOPSRspTime_Object((1,3,6,1,4,1,34774,4,1,21,14,1,7),_HwPerfFileSystemAvWrOPSRspTime_Type())
hwPerfFileSystemAvWrOPSRspTime.setMaxAccess(_C)
if mibBuilder.loadTexts:hwPerfFileSystemAvWrOPSRspTime.setStatus(_A)
_HwPerfFileSystemWriteOPS_Type=Counter64
_HwPerfFileSystemWriteOPS_Object=MibTableColumn
hwPerfFileSystemWriteOPS=_HwPerfFileSystemWriteOPS_Object((1,3,6,1,4,1,34774,4,1,21,14,1,8),_HwPerfFileSystemWriteOPS_Type())
hwPerfFileSystemWriteOPS.setMaxAccess(_C)
if mibBuilder.loadTexts:hwPerfFileSystemWriteOPS.setStatus(_A)
_HwPerfFileSystemWriteBandwidth_Type=Counter64
_HwPerfFileSystemWriteBandwidth_Object=MibTableColumn
hwPerfFileSystemWriteBandwidth=_HwPerfFileSystemWriteBandwidth_Object((1,3,6,1,4,1,34774,4,1,21,14,1,9),_HwPerfFileSystemWriteBandwidth_Type())
hwPerfFileSystemWriteBandwidth.setMaxAccess(_C)
if mibBuilder.loadTexts:hwPerfFileSystemWriteBandwidth.setStatus(_A)
_IsoConformance_ObjectIdentity=ObjectIdentity
isoConformance=_IsoConformance_ObjectIdentity((1,6))
_IsoGroups_ObjectIdentity=ObjectIdentity
isoGroups=_IsoGroups_ObjectIdentity((1,6,1))
_IsoCompliances_ObjectIdentity=ObjectIdentity
isoCompliances=_IsoCompliances_ObjectIdentity((1,6,2))
currentObjectGroup=ObjectGroup((1,6,1,1))
currentObjectGroup.setObjects(*((_B,_H),(_B,_I),(_B,_J),(_B,_K),(_B,_L),(_B,_N),(_B,_O),(_B,_P),(_B,_Q),(_B,_R),(_B,_S),(_B,_T),(_B,_U),(_B,_V),(_B,_W),(_B,_X),(_B,_Y),(_B,_Z),(_B,_a),(_B,_b),(_B,_c),(_B,_d),(_B,_e),(_B,_f),(_B,_g),(_B,_h),(_B,_i),(_B,_j),(_B,_E),(_B,_F),(_B,_k),(_B,_l),(_B,_G),(_B,_m),(_B,_n),(_B,_o),(_B,_p),(_B,_q),(_B,_r),(_B,_s),(_B,_t),(_B,_u),(_B,_v),(_B,_w),(_B,_x),(_B,_y),(_B,_z),(_B,_A0),(_B,_A1),(_B,_A2),(_B,_A3),(_B,_A4),(_B,_A5),(_B,_A6),(_B,_A7),(_B,_A8),(_B,_A9),(_B,_AA),(_B,_AB),(_B,_AC),(_B,_AD),(_B,_D)))
if mibBuilder.loadTexts:currentObjectGroup.setStatus(_A)
basicCompliance=ModuleCompliance((1,6,2,1))
basicCompliance.setObjects((_B,_AE))
if mibBuilder.loadTexts:basicCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'NodeCodeString':NodeCodeString,'huaweistorage':huaweistorage,'hwStorage':hwStorage,'hwISM':hwISM,'hwPerformance':hwPerformance,_A9:hwPerformanceSwitch,'hwPerfNodeTable':hwPerfNodeTable,'hwPerfNodeEntry':hwPerfNodeEntry,_D:hwPerfNodeIfIndex,_N:hwPerfNodeCPUUsage,_O:hwPerfNodeAvgCacheUsage,_d:hwPerfNodeDelay,_e:hwPerfNodeTotalIOPS,_f:hwPerfNodeReadIOPS,_g:hwPerfNodeWriteIOPS,_h:hwPerfNodeTotalTraffic,_i:hwPerfNodeReadTraffic,_j:hwPerfNodeWriteTraffic,_u:hwPerfNodeFileBandwidth,_v:hwPerfNodeFileOPS,'hwPerfLunTable':hwPerfLunTable,'hwPerfLunEntry':hwPerfLunEntry,_E:hwPerfLunID,_Q:hwPerfLunHitRate,_P:hwPerfLunTotalIOPS,_R:hwPerfLunReadIOPS,_S:hwPerfLunWriteIOPS,_T:hwPerfLunTotalTraffic,_U:hwPerfLunReadTraffic,_V:hwPerfLunWriteTraffic,_l:hwPerfLunReadIORate,_k:hwPerfLunWriteIORate,_q:hwPerfLunMaxTraffic,_r:hwPerfLunMaxIOPS,'hwPerfPortTable':hwPerfPortTable,'hwPerfPortEntry':hwPerfPortEntry,_F:hwPerfPortIfIndex,_W:hwPerfPortDelay,_X:hwPerfPortTotalIOPS,_Y:hwPerfPortReadIOPS,_Z:hwPerfPortWriteIOPS,_a:hwPerfPortTotalTraffic,_b:hwPerfPortReadTraffic,_c:hwPerfPortWriteTraffic,_s:hwPerfPortMaxTraffic,_t:hwPerfPortMaxIOPS,_AC:hwPerfPortLocation,'hwPerfCacheTable':hwPerfCacheTable,'hwPerfCacheEntry':hwPerfCacheEntry,_G:hwPerfCacheID,_m:hwPerfCacheReadUtilization,_n:hwPerfCacheWriteUtilization,_o:hwPerfCacheMirrorWriteUtilization,_p:hwPerfCacheHitRatio,'hwPerfControllerNFSV3Table':hwPerfControllerNFSV3Table,'hwPerfControllerNFSV3Entry':hwPerfControllerNFSV3Entry,_H:hwPerfControllerNFSV3ID,_x:hwPerfControllerNFSV3OPS,_w:hwPerfControllerNFSV3Bps,'hwPerfControllerNFSV4Table':hwPerfControllerNFSV4Table,'hwPerfControllerNFSV4Entry':hwPerfControllerNFSV4Entry,_I:hwPerfControllerNFSV4ID,_y:hwPerfControllerNFSV4OPS,_z:hwPerfControllerNFSV4Bps,'hwPerfControllerSMBV1Table':hwPerfControllerSMBV1Table,'hwPerfControllerSMBV1Entry':hwPerfControllerSMBV1Entry,_J:hwPerfControllerSMBV1ID,_A0:hwPerfControllerSMBV1OPS,_AD:hwPerfControllerSMBV1Bps,'hwPerfControllerSMBV2Table':hwPerfControllerSMBV2Table,'hwPerfControllerSMBV2Entry':hwPerfControllerSMBV2Entry,_K:hwPerfControllerSMBV2ID,_A1:hwPerfControllerSMBV2OPS,_A2:hwPerfControllerSMBV2Bps,'hwPerfFileSystemTable':hwPerfFileSystemTable,'hwPerfFileSystemEntry':hwPerfFileSystemEntry,_L:hwPerfFileSystemID,_A3:hwPerfFileSystemOPS,_A4:hwPerfFileSystemServiceTime,_A5:hwPerfFileSystemReadOPS,_A6:hwPerfFileSystemReadBandwidth,_AA:hwPerfFileSystemAvRdOPSRspTime,_AB:hwPerfFileSystemAvWrOPSRspTime,_A7:hwPerfFileSystemWriteOPS,_A8:hwPerfFileSystemWriteBandwidth,'isoConformance':isoConformance,'isoGroups':isoGroups,_AE:currentObjectGroup,'isoCompliances':isoCompliances,'basicCompliance':basicCompliance})