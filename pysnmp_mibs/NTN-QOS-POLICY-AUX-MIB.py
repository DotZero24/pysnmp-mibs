_p='ntnQosInterfaceIdGroup'
_o='ntnQosConfigGroup'
_n='ntnQosTargetStatsHCShapingQDrops'
_m='ntnQosTargetStatsOverflowShapingQDrops'
_l='ntnQosTargetStatsShapingQDrops'
_k='ntnQosTargetStatsTrackStatistics'
_j='ntnQosTargetStatsOutProfHCOctets'
_i='ntnQosTargetStatsOutProfOverflowOctets'
_h='ntnQosTargetStatsOutProfOctets'
_g='ntnQosTargetStatsInProfHCOctets'
_f='ntnQosTargetStatsInProfOverflowOctets'
_e='ntnQosTargetStatsInProfOctets'
_d='ntnQosTargetStatsTotalHCOctets'
_c='ntnQosTargetStatsTotalOverflowOctets'
_b='ntnQosTargetStatsTotalOctets'
_a='ntnQosTargetStatsHCPktHits'
_Z='ntnQosTargetStatsOverflowPktHits'
_Y='ntnQosTargetStatsPktHits'
_X='ntnQosInterfaceIdQueueSet'
_W='ntnQosInterfaceIdStatus'
_V='ntnQosInterfaceIdStorageType'
_U='ntnQosInterfaceIdRoleCombination'
_T='ntnQosConfigPolicyCfgRestrictionMode'
_S='ntnQosConfigDefaultOutOfProfileAction'
_R='ntnQosConfigIfcClassRestrictions'
_Q='ntnQosConfigMaintainPolicingStats'
_P='ntnQosConfigAllowPacketReordering'
_O='ntnQosConfigQpaRetryTimer'
_N='ntnQosConfigQpaState'
_M='ntnQosConfigDynamicMgmt'
_L='ntnQosTargetStatsEntry'
_K='ntnQosInterfaceIdIfIndex'
_J='StorageType'
_I='TruthValue'
_H='read-create'
_G='packets'
_F='Integer32'
_E='octets'
_D='read-write'
_C='read-only'
_B='NTN-QOS-POLICY-AUX-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
InterfaceIndex,=mibBuilder.importSymbols('IF-MIB','InterfaceIndex')
ntnQosIfParametersExt,=mibBuilder.importSymbols('NTN-QOS-POLICY-EXT-PIB','ntnQosIfParametersExt')
PolicyInstanceId,RoleCombination=mibBuilder.importSymbols('POLICY-FRAMEWORK-PIB','PolicyInstanceId','RoleCombination')
qosTargetEntry,=mibBuilder.importSymbols('QOS-POLICY-IP-PIB','qosTargetEntry')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_F,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,StorageType,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus',_J,'TextualConvention',_I)
policy,=mibBuilder.importSymbols('SYNOPTICS-ROOT-MIB','policy')
ntnQosPolicyAuxMib=ModuleIdentity((1,3,6,1,4,1,45,4,5))
if mibBuilder.loadTexts:ntnQosPolicyAuxMib.setRevisions(('2004-07-20 00:00',))
_NtnQosInterfaceIdTable_Object=MibTable
ntnQosInterfaceIdTable=_NtnQosInterfaceIdTable_Object((1,3,6,1,4,1,45,4,4,1,1,4))
if mibBuilder.loadTexts:ntnQosInterfaceIdTable.setStatus(_A)
_NtnQosInterfaceIdEntry_Object=MibTableRow
ntnQosInterfaceIdEntry=_NtnQosInterfaceIdEntry_Object((1,3,6,1,4,1,45,4,4,1,1,4,1))
ntnQosInterfaceIdEntry.setIndexNames((0,_B,_K))
if mibBuilder.loadTexts:ntnQosInterfaceIdEntry.setStatus(_A)
_NtnQosInterfaceIdIfIndex_Type=InterfaceIndex
_NtnQosInterfaceIdIfIndex_Object=MibTableColumn
ntnQosInterfaceIdIfIndex=_NtnQosInterfaceIdIfIndex_Object((1,3,6,1,4,1,45,4,4,1,1,4,1,1),_NtnQosInterfaceIdIfIndex_Type())
ntnQosInterfaceIdIfIndex.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:ntnQosInterfaceIdIfIndex.setStatus(_A)
_NtnQosInterfaceIdRoleCombination_Type=RoleCombination
_NtnQosInterfaceIdRoleCombination_Object=MibTableColumn
ntnQosInterfaceIdRoleCombination=_NtnQosInterfaceIdRoleCombination_Object((1,3,6,1,4,1,45,4,4,1,1,4,1,2),_NtnQosInterfaceIdRoleCombination_Type())
ntnQosInterfaceIdRoleCombination.setMaxAccess(_H)
if mibBuilder.loadTexts:ntnQosInterfaceIdRoleCombination.setStatus(_A)
class _NtnQosInterfaceIdStorageType_Type(StorageType):defaultValue=2
_NtnQosInterfaceIdStorageType_Type.__name__=_J
_NtnQosInterfaceIdStorageType_Object=MibTableColumn
ntnQosInterfaceIdStorageType=_NtnQosInterfaceIdStorageType_Object((1,3,6,1,4,1,45,4,4,1,1,4,1,3),_NtnQosInterfaceIdStorageType_Type())
ntnQosInterfaceIdStorageType.setMaxAccess(_H)
if mibBuilder.loadTexts:ntnQosInterfaceIdStorageType.setStatus(_A)
_NtnQosInterfaceIdStatus_Type=RowStatus
_NtnQosInterfaceIdStatus_Object=MibTableColumn
ntnQosInterfaceIdStatus=_NtnQosInterfaceIdStatus_Object((1,3,6,1,4,1,45,4,4,1,1,4,1,4),_NtnQosInterfaceIdStatus_Type())
ntnQosInterfaceIdStatus.setMaxAccess(_H)
if mibBuilder.loadTexts:ntnQosInterfaceIdStatus.setStatus(_A)
_NtnQosInterfaceIdQueueSet_Type=PolicyInstanceId
_NtnQosInterfaceIdQueueSet_Object=MibTableColumn
ntnQosInterfaceIdQueueSet=_NtnQosInterfaceIdQueueSet_Object((1,3,6,1,4,1,45,4,4,1,1,4,1,5),_NtnQosInterfaceIdQueueSet_Type())
ntnQosInterfaceIdQueueSet.setMaxAccess(_H)
if mibBuilder.loadTexts:ntnQosInterfaceIdQueueSet.setStatus(_A)
_NtnQosPolicyAuxObjects_ObjectIdentity=ObjectIdentity
ntnQosPolicyAuxObjects=_NtnQosPolicyAuxObjects_ObjectIdentity((1,3,6,1,4,1,45,4,5,1))
_NtnQosConfig_ObjectIdentity=ObjectIdentity
ntnQosConfig=_NtnQosConfig_ObjectIdentity((1,3,6,1,4,1,45,4,5,1,1))
class _NtnQosConfigDynamicMgmt_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('enabled',1),('disabled',2)))
_NtnQosConfigDynamicMgmt_Type.__name__=_F
_NtnQosConfigDynamicMgmt_Object=MibScalar
ntnQosConfigDynamicMgmt=_NtnQosConfigDynamicMgmt_Object((1,3,6,1,4,1,45,4,5,1,1,1),_NtnQosConfigDynamicMgmt_Type())
ntnQosConfigDynamicMgmt.setMaxAccess(_D)
if mibBuilder.loadTexts:ntnQosConfigDynamicMgmt.setStatus(_A)
class _NtnQosConfigQpaState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('running',1),('initializing',2),('resetToDefault',3)))
_NtnQosConfigQpaState_Type.__name__=_F
_NtnQosConfigQpaState_Object=MibScalar
ntnQosConfigQpaState=_NtnQosConfigQpaState_Object((1,3,6,1,4,1,45,4,5,1,1,2),_NtnQosConfigQpaState_Type())
ntnQosConfigQpaState.setMaxAccess(_D)
if mibBuilder.loadTexts:ntnQosConfigQpaState.setStatus(_A)
class _NtnQosConfigQpaRetryTimer_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,-1),ValueRangeConstraint(1,86400))
_NtnQosConfigQpaRetryTimer_Type.__name__=_F
_NtnQosConfigQpaRetryTimer_Object=MibScalar
ntnQosConfigQpaRetryTimer=_NtnQosConfigQpaRetryTimer_Object((1,3,6,1,4,1,45,4,5,1,1,3),_NtnQosConfigQpaRetryTimer_Type())
ntnQosConfigQpaRetryTimer.setMaxAccess(_D)
if mibBuilder.loadTexts:ntnQosConfigQpaRetryTimer.setStatus(_A)
if mibBuilder.loadTexts:ntnQosConfigQpaRetryTimer.setUnits('seconds')
class _NtnQosConfigAllowPacketReordering_Type(TruthValue):defaultValue=1
_NtnQosConfigAllowPacketReordering_Type.__name__=_I
_NtnQosConfigAllowPacketReordering_Object=MibScalar
ntnQosConfigAllowPacketReordering=_NtnQosConfigAllowPacketReordering_Object((1,3,6,1,4,1,45,4,5,1,1,4),_NtnQosConfigAllowPacketReordering_Type())
ntnQosConfigAllowPacketReordering.setMaxAccess(_D)
if mibBuilder.loadTexts:ntnQosConfigAllowPacketReordering.setStatus(_A)
class _NtnQosConfigMaintainPolicingStats_Type(TruthValue):defaultValue=1
_NtnQosConfigMaintainPolicingStats_Type.__name__=_I
_NtnQosConfigMaintainPolicingStats_Object=MibScalar
ntnQosConfigMaintainPolicingStats=_NtnQosConfigMaintainPolicingStats_Object((1,3,6,1,4,1,45,4,5,1,1,5),_NtnQosConfigMaintainPolicingStats_Type())
ntnQosConfigMaintainPolicingStats.setMaxAccess(_D)
if mibBuilder.loadTexts:ntnQosConfigMaintainPolicingStats.setStatus(_A)
class _NtnQosConfigIfcClassRestrictions_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('unrestrictedOnly',1),('unrestrictedAndTrusted',2),('allowAllIfcClasses',3)))
_NtnQosConfigIfcClassRestrictions_Type.__name__=_F
_NtnQosConfigIfcClassRestrictions_Object=MibScalar
ntnQosConfigIfcClassRestrictions=_NtnQosConfigIfcClassRestrictions_Object((1,3,6,1,4,1,45,4,5,1,1,6),_NtnQosConfigIfcClassRestrictions_Type())
ntnQosConfigIfcClassRestrictions.setMaxAccess(_D)
if mibBuilder.loadTexts:ntnQosConfigIfcClassRestrictions.setStatus(_A)
_NtnQosConfigDefaultOutOfProfileAction_Type=PolicyInstanceId
_NtnQosConfigDefaultOutOfProfileAction_Object=MibScalar
ntnQosConfigDefaultOutOfProfileAction=_NtnQosConfigDefaultOutOfProfileAction_Object((1,3,6,1,4,1,45,4,5,1,1,7),_NtnQosConfigDefaultOutOfProfileAction_Type())
ntnQosConfigDefaultOutOfProfileAction.setMaxAccess(_D)
if mibBuilder.loadTexts:ntnQosConfigDefaultOutOfProfileAction.setStatus(_A)
class _NtnQosConfigPolicyCfgRestrictionMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('noPolicyRestrictions',1),('l3PolicyRestrictions',2)))
_NtnQosConfigPolicyCfgRestrictionMode_Type.__name__=_F
_NtnQosConfigPolicyCfgRestrictionMode_Object=MibScalar
ntnQosConfigPolicyCfgRestrictionMode=_NtnQosConfigPolicyCfgRestrictionMode_Object((1,3,6,1,4,1,45,4,5,1,1,8),_NtnQosConfigPolicyCfgRestrictionMode_Type())
ntnQosConfigPolicyCfgRestrictionMode.setMaxAccess(_D)
if mibBuilder.loadTexts:ntnQosConfigPolicyCfgRestrictionMode.setStatus(_A)
_NtnQosStatistics_ObjectIdentity=ObjectIdentity
ntnQosStatistics=_NtnQosStatistics_ObjectIdentity((1,3,6,1,4,1,45,4,5,1,2))
_NtnQosTargetStatsTable_Object=MibTable
ntnQosTargetStatsTable=_NtnQosTargetStatsTable_Object((1,3,6,1,4,1,45,4,5,1,2,1))
if mibBuilder.loadTexts:ntnQosTargetStatsTable.setStatus(_A)
_NtnQosTargetStatsEntry_Object=MibTableRow
ntnQosTargetStatsEntry=_NtnQosTargetStatsEntry_Object((1,3,6,1,4,1,45,4,5,1,2,1,1))
if mibBuilder.loadTexts:ntnQosTargetStatsEntry.setStatus(_A)
_NtnQosTargetStatsPktHits_Type=Counter32
_NtnQosTargetStatsPktHits_Object=MibTableColumn
ntnQosTargetStatsPktHits=_NtnQosTargetStatsPktHits_Object((1,3,6,1,4,1,45,4,5,1,2,1,1,1),_NtnQosTargetStatsPktHits_Type())
ntnQosTargetStatsPktHits.setMaxAccess(_C)
if mibBuilder.loadTexts:ntnQosTargetStatsPktHits.setStatus(_A)
if mibBuilder.loadTexts:ntnQosTargetStatsPktHits.setUnits(_G)
_NtnQosTargetStatsOverflowPktHits_Type=Counter32
_NtnQosTargetStatsOverflowPktHits_Object=MibTableColumn
ntnQosTargetStatsOverflowPktHits=_NtnQosTargetStatsOverflowPktHits_Object((1,3,6,1,4,1,45,4,5,1,2,1,1,2),_NtnQosTargetStatsOverflowPktHits_Type())
ntnQosTargetStatsOverflowPktHits.setMaxAccess(_C)
if mibBuilder.loadTexts:ntnQosTargetStatsOverflowPktHits.setStatus(_A)
if mibBuilder.loadTexts:ntnQosTargetStatsOverflowPktHits.setUnits(_G)
_NtnQosTargetStatsHCPktHits_Type=Counter64
_NtnQosTargetStatsHCPktHits_Object=MibTableColumn
ntnQosTargetStatsHCPktHits=_NtnQosTargetStatsHCPktHits_Object((1,3,6,1,4,1,45,4,5,1,2,1,1,3),_NtnQosTargetStatsHCPktHits_Type())
ntnQosTargetStatsHCPktHits.setMaxAccess(_C)
if mibBuilder.loadTexts:ntnQosTargetStatsHCPktHits.setStatus(_A)
if mibBuilder.loadTexts:ntnQosTargetStatsHCPktHits.setUnits(_G)
_NtnQosTargetStatsTotalOctets_Type=Counter32
_NtnQosTargetStatsTotalOctets_Object=MibTableColumn
ntnQosTargetStatsTotalOctets=_NtnQosTargetStatsTotalOctets_Object((1,3,6,1,4,1,45,4,5,1,2,1,1,4),_NtnQosTargetStatsTotalOctets_Type())
ntnQosTargetStatsTotalOctets.setMaxAccess(_C)
if mibBuilder.loadTexts:ntnQosTargetStatsTotalOctets.setStatus(_A)
if mibBuilder.loadTexts:ntnQosTargetStatsTotalOctets.setUnits(_E)
_NtnQosTargetStatsTotalOverflowOctets_Type=Counter32
_NtnQosTargetStatsTotalOverflowOctets_Object=MibTableColumn
ntnQosTargetStatsTotalOverflowOctets=_NtnQosTargetStatsTotalOverflowOctets_Object((1,3,6,1,4,1,45,4,5,1,2,1,1,5),_NtnQosTargetStatsTotalOverflowOctets_Type())
ntnQosTargetStatsTotalOverflowOctets.setMaxAccess(_C)
if mibBuilder.loadTexts:ntnQosTargetStatsTotalOverflowOctets.setStatus(_A)
if mibBuilder.loadTexts:ntnQosTargetStatsTotalOverflowOctets.setUnits(_E)
_NtnQosTargetStatsTotalHCOctets_Type=Counter64
_NtnQosTargetStatsTotalHCOctets_Object=MibTableColumn
ntnQosTargetStatsTotalHCOctets=_NtnQosTargetStatsTotalHCOctets_Object((1,3,6,1,4,1,45,4,5,1,2,1,1,6),_NtnQosTargetStatsTotalHCOctets_Type())
ntnQosTargetStatsTotalHCOctets.setMaxAccess(_C)
if mibBuilder.loadTexts:ntnQosTargetStatsTotalHCOctets.setStatus(_A)
if mibBuilder.loadTexts:ntnQosTargetStatsTotalHCOctets.setUnits(_E)
_NtnQosTargetStatsInProfOctets_Type=Counter32
_NtnQosTargetStatsInProfOctets_Object=MibTableColumn
ntnQosTargetStatsInProfOctets=_NtnQosTargetStatsInProfOctets_Object((1,3,6,1,4,1,45,4,5,1,2,1,1,7),_NtnQosTargetStatsInProfOctets_Type())
ntnQosTargetStatsInProfOctets.setMaxAccess(_C)
if mibBuilder.loadTexts:ntnQosTargetStatsInProfOctets.setStatus(_A)
if mibBuilder.loadTexts:ntnQosTargetStatsInProfOctets.setUnits(_E)
_NtnQosTargetStatsInProfOverflowOctets_Type=Counter32
_NtnQosTargetStatsInProfOverflowOctets_Object=MibTableColumn
ntnQosTargetStatsInProfOverflowOctets=_NtnQosTargetStatsInProfOverflowOctets_Object((1,3,6,1,4,1,45,4,5,1,2,1,1,8),_NtnQosTargetStatsInProfOverflowOctets_Type())
ntnQosTargetStatsInProfOverflowOctets.setMaxAccess(_C)
if mibBuilder.loadTexts:ntnQosTargetStatsInProfOverflowOctets.setStatus(_A)
if mibBuilder.loadTexts:ntnQosTargetStatsInProfOverflowOctets.setUnits(_E)
_NtnQosTargetStatsInProfHCOctets_Type=Counter64
_NtnQosTargetStatsInProfHCOctets_Object=MibTableColumn
ntnQosTargetStatsInProfHCOctets=_NtnQosTargetStatsInProfHCOctets_Object((1,3,6,1,4,1,45,4,5,1,2,1,1,9),_NtnQosTargetStatsInProfHCOctets_Type())
ntnQosTargetStatsInProfHCOctets.setMaxAccess(_C)
if mibBuilder.loadTexts:ntnQosTargetStatsInProfHCOctets.setStatus(_A)
if mibBuilder.loadTexts:ntnQosTargetStatsInProfHCOctets.setUnits(_E)
_NtnQosTargetStatsOutProfOctets_Type=Counter32
_NtnQosTargetStatsOutProfOctets_Object=MibTableColumn
ntnQosTargetStatsOutProfOctets=_NtnQosTargetStatsOutProfOctets_Object((1,3,6,1,4,1,45,4,5,1,2,1,1,10),_NtnQosTargetStatsOutProfOctets_Type())
ntnQosTargetStatsOutProfOctets.setMaxAccess(_C)
if mibBuilder.loadTexts:ntnQosTargetStatsOutProfOctets.setStatus(_A)
if mibBuilder.loadTexts:ntnQosTargetStatsOutProfOctets.setUnits(_E)
_NtnQosTargetStatsOutProfOverflowOctets_Type=Counter32
_NtnQosTargetStatsOutProfOverflowOctets_Object=MibTableColumn
ntnQosTargetStatsOutProfOverflowOctets=_NtnQosTargetStatsOutProfOverflowOctets_Object((1,3,6,1,4,1,45,4,5,1,2,1,1,11),_NtnQosTargetStatsOutProfOverflowOctets_Type())
ntnQosTargetStatsOutProfOverflowOctets.setMaxAccess(_C)
if mibBuilder.loadTexts:ntnQosTargetStatsOutProfOverflowOctets.setStatus(_A)
if mibBuilder.loadTexts:ntnQosTargetStatsOutProfOverflowOctets.setUnits(_E)
_NtnQosTargetStatsOutProfHCOctets_Type=Counter64
_NtnQosTargetStatsOutProfHCOctets_Object=MibTableColumn
ntnQosTargetStatsOutProfHCOctets=_NtnQosTargetStatsOutProfHCOctets_Object((1,3,6,1,4,1,45,4,5,1,2,1,1,12),_NtnQosTargetStatsOutProfHCOctets_Type())
ntnQosTargetStatsOutProfHCOctets.setMaxAccess(_C)
if mibBuilder.loadTexts:ntnQosTargetStatsOutProfHCOctets.setStatus(_A)
if mibBuilder.loadTexts:ntnQosTargetStatsOutProfHCOctets.setUnits(_E)
_NtnQosTargetStatsTrackStatistics_Type=TruthValue
_NtnQosTargetStatsTrackStatistics_Object=MibTableColumn
ntnQosTargetStatsTrackStatistics=_NtnQosTargetStatsTrackStatistics_Object((1,3,6,1,4,1,45,4,5,1,2,1,1,13),_NtnQosTargetStatsTrackStatistics_Type())
ntnQosTargetStatsTrackStatistics.setMaxAccess(_D)
if mibBuilder.loadTexts:ntnQosTargetStatsTrackStatistics.setStatus(_A)
_NtnQosTargetStatsShapingQDrops_Type=Counter32
_NtnQosTargetStatsShapingQDrops_Object=MibTableColumn
ntnQosTargetStatsShapingQDrops=_NtnQosTargetStatsShapingQDrops_Object((1,3,6,1,4,1,45,4,5,1,2,1,1,14),_NtnQosTargetStatsShapingQDrops_Type())
ntnQosTargetStatsShapingQDrops.setMaxAccess(_C)
if mibBuilder.loadTexts:ntnQosTargetStatsShapingQDrops.setStatus(_A)
if mibBuilder.loadTexts:ntnQosTargetStatsShapingQDrops.setUnits(_G)
_NtnQosTargetStatsOverflowShapingQDrops_Type=Counter32
_NtnQosTargetStatsOverflowShapingQDrops_Object=MibTableColumn
ntnQosTargetStatsOverflowShapingQDrops=_NtnQosTargetStatsOverflowShapingQDrops_Object((1,3,6,1,4,1,45,4,5,1,2,1,1,15),_NtnQosTargetStatsOverflowShapingQDrops_Type())
ntnQosTargetStatsOverflowShapingQDrops.setMaxAccess(_C)
if mibBuilder.loadTexts:ntnQosTargetStatsOverflowShapingQDrops.setStatus(_A)
if mibBuilder.loadTexts:ntnQosTargetStatsOverflowShapingQDrops.setUnits(_G)
_NtnQosTargetStatsHCShapingQDrops_Type=Counter64
_NtnQosTargetStatsHCShapingQDrops_Object=MibTableColumn
ntnQosTargetStatsHCShapingQDrops=_NtnQosTargetStatsHCShapingQDrops_Object((1,3,6,1,4,1,45,4,5,1,2,1,1,16),_NtnQosTargetStatsHCShapingQDrops_Type())
ntnQosTargetStatsHCShapingQDrops.setMaxAccess(_C)
if mibBuilder.loadTexts:ntnQosTargetStatsHCShapingQDrops.setStatus(_A)
if mibBuilder.loadTexts:ntnQosTargetStatsHCShapingQDrops.setUnits(_G)
_NtnQosPolicyAuxConformance_ObjectIdentity=ObjectIdentity
ntnQosPolicyAuxConformance=_NtnQosPolicyAuxConformance_ObjectIdentity((1,3,6,1,4,1,45,4,5,2))
_NtnQosCompliances_ObjectIdentity=ObjectIdentity
ntnQosCompliances=_NtnQosCompliances_ObjectIdentity((1,3,6,1,4,1,45,4,5,2,1))
_NtnQosGroups_ObjectIdentity=ObjectIdentity
ntnQosGroups=_NtnQosGroups_ObjectIdentity((1,3,6,1,4,1,45,4,5,2,2))
qosTargetEntry.registerAugmentions((_B,_L))
ntnQosTargetStatsEntry.setIndexNames(*qosTargetEntry.getIndexNames())
ntnQosConfigGroup=ObjectGroup((1,3,6,1,4,1,45,4,5,2,2,1))
ntnQosConfigGroup.setObjects(*((_B,_M),(_B,_N),(_B,_O),(_B,_P),(_B,_Q),(_B,_R),(_B,_S),(_B,_T)))
if mibBuilder.loadTexts:ntnQosConfigGroup.setStatus(_A)
ntnQosInterfaceIdGroup=ObjectGroup((1,3,6,1,4,1,45,4,5,2,2,2))
ntnQosInterfaceIdGroup.setObjects(*((_B,_U),(_B,_V),(_B,_W),(_B,_X)))
if mibBuilder.loadTexts:ntnQosInterfaceIdGroup.setStatus(_A)
ntnQosTargetStatsGroup=ObjectGroup((1,3,6,1,4,1,45,4,5,2,2,3))
ntnQosTargetStatsGroup.setObjects(*((_B,_Y),(_B,_Z),(_B,_a),(_B,_b),(_B,_c),(_B,_d),(_B,_e),(_B,_f),(_B,_g),(_B,_h),(_B,_i),(_B,_j),(_B,_k),(_B,_l),(_B,_m),(_B,_n)))
if mibBuilder.loadTexts:ntnQosTargetStatsGroup.setStatus(_A)
ntnQosCompliance=ModuleCompliance((1,3,6,1,4,1,45,4,5,2,1,1))
ntnQosCompliance.setObjects(*((_B,_o),(_B,_p)))
if mibBuilder.loadTexts:ntnQosCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'ntnQosInterfaceIdTable':ntnQosInterfaceIdTable,'ntnQosInterfaceIdEntry':ntnQosInterfaceIdEntry,_K:ntnQosInterfaceIdIfIndex,_U:ntnQosInterfaceIdRoleCombination,_V:ntnQosInterfaceIdStorageType,_W:ntnQosInterfaceIdStatus,_X:ntnQosInterfaceIdQueueSet,'ntnQosPolicyAuxMib':ntnQosPolicyAuxMib,'ntnQosPolicyAuxObjects':ntnQosPolicyAuxObjects,'ntnQosConfig':ntnQosConfig,_M:ntnQosConfigDynamicMgmt,_N:ntnQosConfigQpaState,_O:ntnQosConfigQpaRetryTimer,_P:ntnQosConfigAllowPacketReordering,_Q:ntnQosConfigMaintainPolicingStats,_R:ntnQosConfigIfcClassRestrictions,_S:ntnQosConfigDefaultOutOfProfileAction,_T:ntnQosConfigPolicyCfgRestrictionMode,'ntnQosStatistics':ntnQosStatistics,'ntnQosTargetStatsTable':ntnQosTargetStatsTable,_L:ntnQosTargetStatsEntry,_Y:ntnQosTargetStatsPktHits,_Z:ntnQosTargetStatsOverflowPktHits,_a:ntnQosTargetStatsHCPktHits,_b:ntnQosTargetStatsTotalOctets,_c:ntnQosTargetStatsTotalOverflowOctets,_d:ntnQosTargetStatsTotalHCOctets,_e:ntnQosTargetStatsInProfOctets,_f:ntnQosTargetStatsInProfOverflowOctets,_g:ntnQosTargetStatsInProfHCOctets,_h:ntnQosTargetStatsOutProfOctets,_i:ntnQosTargetStatsOutProfOverflowOctets,_j:ntnQosTargetStatsOutProfHCOctets,_k:ntnQosTargetStatsTrackStatistics,_l:ntnQosTargetStatsShapingQDrops,_m:ntnQosTargetStatsOverflowShapingQDrops,_n:ntnQosTargetStatsHCShapingQDrops,'ntnQosPolicyAuxConformance':ntnQosPolicyAuxConformance,'ntnQosCompliances':ntnQosCompliances,'ntnQosCompliance':ntnQosCompliance,'ntnQosGroups':ntnQosGroups,_o:ntnQosConfigGroup,_p:ntnQosInterfaceIdGroup,'ntnQosTargetStatsGroup':ntnQosTargetStatsGroup})