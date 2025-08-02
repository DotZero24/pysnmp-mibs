_k='f3PbbStatsGroup'
_j='f3PbbConfigGroup'
_i='f3PbbEthernetNetPortHistoryStatsPbbGroupBdaDiscard'
_h='f3PbbEthernetNetPortHistoryStatsPbbUniBdaDiscard'
_g='f3PbbEthernetNetPortStatsPbbGroupBdaDiscard'
_f='f3PbbEthernetNetPortStatsPbbUniBdaDiscard'
_e='f3PbbIpManagementTunnelBackboneMacDestinationAddress'
_d='f3PbbIpManagementTunnelBackboneMacDestinationEnabled'
_c='f3PbbIpManagementTunnelIPriority'
_b='f3PbbIpManagementTunnelISID'
_a='f3PbbIpManagementTunnelItagEnabled'
_Z='f3PbbFlowA2NPbbCapableFlag'
_Y='f3PbbFlowBackboneMacDestinationAddress'
_X='f3PbbFlowBackboneMacDestinationEnabled'
_W='f3PbbFlowITagPriority'
_V='f3PbbFlowITagISID'
_U='f3PbbFlowITagControl'
_T='f3PbbEthernetNetPortITagLoopback3'
_S='f3PbbEthernetNetPortITagLoopback2'
_R='f3PbbEthernetNetPortITagLoopback1'
_Q='f3PbbEthernetNetPortITagLoopbackMask'
_P='f3PbbEthernetNetPortBackboneMacAddress'
_O='f3PbbEthernetAccPortITagLoopback3'
_N='f3PbbEthernetAccPortITagLoopback2'
_M='f3PbbEthernetAccPortITagLoopback1'
_L='f3PbbEthernetAccPortITagLoopbackMask'
_K='f3PbbEthernetNetPortHistoryStatsEntry'
_J='f3PbbEthernetNetPortStatsEntry'
_I='f3PbbIpManagementTunnelEntry'
_H='f3PbbFlowEntry'
_G='f3PbbEthernetNetPortEntry'
_F='f3PbbEthernetAccPortEntry'
_E='read-only'
_D='Integer32'
_C='read-write'
_B='F3-PBB-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
fsp150cm,=mibBuilder.importSymbols('ADVA-MIB','fsp150cm')
PerfCounter64,=mibBuilder.importSymbols('CM-COMMON-MIB','PerfCounter64')
FlowTagControl,cmEthernetAccPortEntry,cmEthernetNetPortEntry,cmFlowEntry=mibBuilder.importSymbols('CM-FACILITY-MIB','FlowTagControl','cmEthernetAccPortEntry','cmEthernetNetPortEntry','cmFlowEntry')
ipManagementTunnelEntry,=mibBuilder.importSymbols('CM-IP-MIB','ipManagementTunnelEntry')
cmEthernetNetPortHistoryEntry,cmEthernetNetPortStatsEntry=mibBuilder.importSymbols('CM-PERFORMANCE-MIB','cmEthernetNetPortHistoryEntry','cmEthernetNetPortStatsEntry')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,MacAddress,PhysAddress,TextualConvention,TruthValue,VariablePointer=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress','TextualConvention','TruthValue','VariablePointer')
f3PBBMIB=ModuleIdentity((1,3,6,1,4,1,2544,1,12,21))
if mibBuilder.loadTexts:f3PBBMIB.setRevisions(('2012-10-08 00:00',))
_F3PBBConfigObjects_ObjectIdentity=ObjectIdentity
f3PBBConfigObjects=_F3PBBConfigObjects_ObjectIdentity((1,3,6,1,4,1,2544,1,12,21,1))
_F3PbbEthernetAccPortTable_Object=MibTable
f3PbbEthernetAccPortTable=_F3PbbEthernetAccPortTable_Object((1,3,6,1,4,1,2544,1,12,21,1,1))
if mibBuilder.loadTexts:f3PbbEthernetAccPortTable.setStatus(_A)
_F3PbbEthernetAccPortEntry_Object=MibTableRow
f3PbbEthernetAccPortEntry=_F3PbbEthernetAccPortEntry_Object((1,3,6,1,4,1,2544,1,12,21,1,1,1))
if mibBuilder.loadTexts:f3PbbEthernetAccPortEntry.setStatus(_A)
_F3PbbEthernetAccPortITagLoopbackMask_Type=Integer32
_F3PbbEthernetAccPortITagLoopbackMask_Object=MibTableColumn
f3PbbEthernetAccPortITagLoopbackMask=_F3PbbEthernetAccPortITagLoopbackMask_Object((1,3,6,1,4,1,2544,1,12,21,1,1,1,1),_F3PbbEthernetAccPortITagLoopbackMask_Type())
f3PbbEthernetAccPortITagLoopbackMask.setMaxAccess(_C)
if mibBuilder.loadTexts:f3PbbEthernetAccPortITagLoopbackMask.setStatus(_A)
_F3PbbEthernetAccPortITagLoopback1_Type=DisplayString
_F3PbbEthernetAccPortITagLoopback1_Object=MibTableColumn
f3PbbEthernetAccPortITagLoopback1=_F3PbbEthernetAccPortITagLoopback1_Object((1,3,6,1,4,1,2544,1,12,21,1,1,1,2),_F3PbbEthernetAccPortITagLoopback1_Type())
f3PbbEthernetAccPortITagLoopback1.setMaxAccess(_C)
if mibBuilder.loadTexts:f3PbbEthernetAccPortITagLoopback1.setStatus(_A)
_F3PbbEthernetAccPortITagLoopback2_Type=DisplayString
_F3PbbEthernetAccPortITagLoopback2_Object=MibTableColumn
f3PbbEthernetAccPortITagLoopback2=_F3PbbEthernetAccPortITagLoopback2_Object((1,3,6,1,4,1,2544,1,12,21,1,1,1,3),_F3PbbEthernetAccPortITagLoopback2_Type())
f3PbbEthernetAccPortITagLoopback2.setMaxAccess(_C)
if mibBuilder.loadTexts:f3PbbEthernetAccPortITagLoopback2.setStatus(_A)
_F3PbbEthernetAccPortITagLoopback3_Type=DisplayString
_F3PbbEthernetAccPortITagLoopback3_Object=MibTableColumn
f3PbbEthernetAccPortITagLoopback3=_F3PbbEthernetAccPortITagLoopback3_Object((1,3,6,1,4,1,2544,1,12,21,1,1,1,4),_F3PbbEthernetAccPortITagLoopback3_Type())
f3PbbEthernetAccPortITagLoopback3.setMaxAccess(_C)
if mibBuilder.loadTexts:f3PbbEthernetAccPortITagLoopback3.setStatus(_A)
_F3PbbEthernetNetPortTable_Object=MibTable
f3PbbEthernetNetPortTable=_F3PbbEthernetNetPortTable_Object((1,3,6,1,4,1,2544,1,12,21,1,2))
if mibBuilder.loadTexts:f3PbbEthernetNetPortTable.setStatus(_A)
_F3PbbEthernetNetPortEntry_Object=MibTableRow
f3PbbEthernetNetPortEntry=_F3PbbEthernetNetPortEntry_Object((1,3,6,1,4,1,2544,1,12,21,1,2,1))
if mibBuilder.loadTexts:f3PbbEthernetNetPortEntry.setStatus(_A)
_F3PbbEthernetNetPortBackboneMacAddress_Type=MacAddress
_F3PbbEthernetNetPortBackboneMacAddress_Object=MibTableColumn
f3PbbEthernetNetPortBackboneMacAddress=_F3PbbEthernetNetPortBackboneMacAddress_Object((1,3,6,1,4,1,2544,1,12,21,1,2,1,1),_F3PbbEthernetNetPortBackboneMacAddress_Type())
f3PbbEthernetNetPortBackboneMacAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:f3PbbEthernetNetPortBackboneMacAddress.setStatus(_A)
_F3PbbEthernetNetPortITagLoopbackMask_Type=Integer32
_F3PbbEthernetNetPortITagLoopbackMask_Object=MibTableColumn
f3PbbEthernetNetPortITagLoopbackMask=_F3PbbEthernetNetPortITagLoopbackMask_Object((1,3,6,1,4,1,2544,1,12,21,1,2,1,2),_F3PbbEthernetNetPortITagLoopbackMask_Type())
f3PbbEthernetNetPortITagLoopbackMask.setMaxAccess(_C)
if mibBuilder.loadTexts:f3PbbEthernetNetPortITagLoopbackMask.setStatus(_A)
_F3PbbEthernetNetPortITagLoopback1_Type=DisplayString
_F3PbbEthernetNetPortITagLoopback1_Object=MibTableColumn
f3PbbEthernetNetPortITagLoopback1=_F3PbbEthernetNetPortITagLoopback1_Object((1,3,6,1,4,1,2544,1,12,21,1,2,1,3),_F3PbbEthernetNetPortITagLoopback1_Type())
f3PbbEthernetNetPortITagLoopback1.setMaxAccess(_C)
if mibBuilder.loadTexts:f3PbbEthernetNetPortITagLoopback1.setStatus(_A)
_F3PbbEthernetNetPortITagLoopback2_Type=DisplayString
_F3PbbEthernetNetPortITagLoopback2_Object=MibTableColumn
f3PbbEthernetNetPortITagLoopback2=_F3PbbEthernetNetPortITagLoopback2_Object((1,3,6,1,4,1,2544,1,12,21,1,2,1,4),_F3PbbEthernetNetPortITagLoopback2_Type())
f3PbbEthernetNetPortITagLoopback2.setMaxAccess(_C)
if mibBuilder.loadTexts:f3PbbEthernetNetPortITagLoopback2.setStatus(_A)
_F3PbbEthernetNetPortITagLoopback3_Type=DisplayString
_F3PbbEthernetNetPortITagLoopback3_Object=MibTableColumn
f3PbbEthernetNetPortITagLoopback3=_F3PbbEthernetNetPortITagLoopback3_Object((1,3,6,1,4,1,2544,1,12,21,1,2,1,5),_F3PbbEthernetNetPortITagLoopback3_Type())
f3PbbEthernetNetPortITagLoopback3.setMaxAccess(_C)
if mibBuilder.loadTexts:f3PbbEthernetNetPortITagLoopback3.setStatus(_A)
_F3PbbFlowTable_Object=MibTable
f3PbbFlowTable=_F3PbbFlowTable_Object((1,3,6,1,4,1,2544,1,12,21,1,3))
if mibBuilder.loadTexts:f3PbbFlowTable.setStatus(_A)
_F3PbbFlowEntry_Object=MibTableRow
f3PbbFlowEntry=_F3PbbFlowEntry_Object((1,3,6,1,4,1,2544,1,12,21,1,3,1))
if mibBuilder.loadTexts:f3PbbFlowEntry.setStatus(_A)
_F3PbbFlowITagControl_Type=FlowTagControl
_F3PbbFlowITagControl_Object=MibTableColumn
f3PbbFlowITagControl=_F3PbbFlowITagControl_Object((1,3,6,1,4,1,2544,1,12,21,1,3,1,1),_F3PbbFlowITagControl_Type())
f3PbbFlowITagControl.setMaxAccess(_C)
if mibBuilder.loadTexts:f3PbbFlowITagControl.setStatus(_A)
class _F3PbbFlowITagISID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(256,16777214))
_F3PbbFlowITagISID_Type.__name__=_D
_F3PbbFlowITagISID_Object=MibTableColumn
f3PbbFlowITagISID=_F3PbbFlowITagISID_Object((1,3,6,1,4,1,2544,1,12,21,1,3,1,2),_F3PbbFlowITagISID_Type())
f3PbbFlowITagISID.setMaxAccess(_C)
if mibBuilder.loadTexts:f3PbbFlowITagISID.setStatus(_A)
class _F3PbbFlowITagPriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_F3PbbFlowITagPriority_Type.__name__=_D
_F3PbbFlowITagPriority_Object=MibTableColumn
f3PbbFlowITagPriority=_F3PbbFlowITagPriority_Object((1,3,6,1,4,1,2544,1,12,21,1,3,1,3),_F3PbbFlowITagPriority_Type())
f3PbbFlowITagPriority.setMaxAccess(_C)
if mibBuilder.loadTexts:f3PbbFlowITagPriority.setStatus(_A)
_F3PbbFlowBackboneMacDestinationEnabled_Type=TruthValue
_F3PbbFlowBackboneMacDestinationEnabled_Object=MibTableColumn
f3PbbFlowBackboneMacDestinationEnabled=_F3PbbFlowBackboneMacDestinationEnabled_Object((1,3,6,1,4,1,2544,1,12,21,1,3,1,4),_F3PbbFlowBackboneMacDestinationEnabled_Type())
f3PbbFlowBackboneMacDestinationEnabled.setMaxAccess(_C)
if mibBuilder.loadTexts:f3PbbFlowBackboneMacDestinationEnabled.setStatus(_A)
_F3PbbFlowBackboneMacDestinationAddress_Type=MacAddress
_F3PbbFlowBackboneMacDestinationAddress_Object=MibTableColumn
f3PbbFlowBackboneMacDestinationAddress=_F3PbbFlowBackboneMacDestinationAddress_Object((1,3,6,1,4,1,2544,1,12,21,1,3,1,5),_F3PbbFlowBackboneMacDestinationAddress_Type())
f3PbbFlowBackboneMacDestinationAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:f3PbbFlowBackboneMacDestinationAddress.setStatus(_A)
_F3PbbFlowA2NPbbCapableFlag_Type=TruthValue
_F3PbbFlowA2NPbbCapableFlag_Object=MibTableColumn
f3PbbFlowA2NPbbCapableFlag=_F3PbbFlowA2NPbbCapableFlag_Object((1,3,6,1,4,1,2544,1,12,21,1,3,1,6),_F3PbbFlowA2NPbbCapableFlag_Type())
f3PbbFlowA2NPbbCapableFlag.setMaxAccess(_C)
if mibBuilder.loadTexts:f3PbbFlowA2NPbbCapableFlag.setStatus(_A)
_F3PbbIpManagementTunnelTable_Object=MibTable
f3PbbIpManagementTunnelTable=_F3PbbIpManagementTunnelTable_Object((1,3,6,1,4,1,2544,1,12,21,1,4))
if mibBuilder.loadTexts:f3PbbIpManagementTunnelTable.setStatus(_A)
_F3PbbIpManagementTunnelEntry_Object=MibTableRow
f3PbbIpManagementTunnelEntry=_F3PbbIpManagementTunnelEntry_Object((1,3,6,1,4,1,2544,1,12,21,1,4,1))
if mibBuilder.loadTexts:f3PbbIpManagementTunnelEntry.setStatus(_A)
_F3PbbIpManagementTunnelItagEnabled_Type=TruthValue
_F3PbbIpManagementTunnelItagEnabled_Object=MibTableColumn
f3PbbIpManagementTunnelItagEnabled=_F3PbbIpManagementTunnelItagEnabled_Object((1,3,6,1,4,1,2544,1,12,21,1,4,1,1),_F3PbbIpManagementTunnelItagEnabled_Type())
f3PbbIpManagementTunnelItagEnabled.setMaxAccess(_C)
if mibBuilder.loadTexts:f3PbbIpManagementTunnelItagEnabled.setStatus(_A)
class _F3PbbIpManagementTunnelISID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(256,16777214))
_F3PbbIpManagementTunnelISID_Type.__name__=_D
_F3PbbIpManagementTunnelISID_Object=MibTableColumn
f3PbbIpManagementTunnelISID=_F3PbbIpManagementTunnelISID_Object((1,3,6,1,4,1,2544,1,12,21,1,4,1,2),_F3PbbIpManagementTunnelISID_Type())
f3PbbIpManagementTunnelISID.setMaxAccess(_C)
if mibBuilder.loadTexts:f3PbbIpManagementTunnelISID.setStatus(_A)
class _F3PbbIpManagementTunnelIPriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_F3PbbIpManagementTunnelIPriority_Type.__name__=_D
_F3PbbIpManagementTunnelIPriority_Object=MibTableColumn
f3PbbIpManagementTunnelIPriority=_F3PbbIpManagementTunnelIPriority_Object((1,3,6,1,4,1,2544,1,12,21,1,4,1,3),_F3PbbIpManagementTunnelIPriority_Type())
f3PbbIpManagementTunnelIPriority.setMaxAccess(_C)
if mibBuilder.loadTexts:f3PbbIpManagementTunnelIPriority.setStatus(_A)
_F3PbbIpManagementTunnelBackboneMacDestinationEnabled_Type=TruthValue
_F3PbbIpManagementTunnelBackboneMacDestinationEnabled_Object=MibTableColumn
f3PbbIpManagementTunnelBackboneMacDestinationEnabled=_F3PbbIpManagementTunnelBackboneMacDestinationEnabled_Object((1,3,6,1,4,1,2544,1,12,21,1,4,1,4),_F3PbbIpManagementTunnelBackboneMacDestinationEnabled_Type())
f3PbbIpManagementTunnelBackboneMacDestinationEnabled.setMaxAccess(_C)
if mibBuilder.loadTexts:f3PbbIpManagementTunnelBackboneMacDestinationEnabled.setStatus(_A)
_F3PbbIpManagementTunnelBackboneMacDestinationAddress_Type=MacAddress
_F3PbbIpManagementTunnelBackboneMacDestinationAddress_Object=MibTableColumn
f3PbbIpManagementTunnelBackboneMacDestinationAddress=_F3PbbIpManagementTunnelBackboneMacDestinationAddress_Object((1,3,6,1,4,1,2544,1,12,21,1,4,1,5),_F3PbbIpManagementTunnelBackboneMacDestinationAddress_Type())
f3PbbIpManagementTunnelBackboneMacDestinationAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:f3PbbIpManagementTunnelBackboneMacDestinationAddress.setStatus(_A)
_F3PBBPerformanceObjects_ObjectIdentity=ObjectIdentity
f3PBBPerformanceObjects=_F3PBBPerformanceObjects_ObjectIdentity((1,3,6,1,4,1,2544,1,12,21,2))
_F3PbbEthernetNetPortStatsTable_Object=MibTable
f3PbbEthernetNetPortStatsTable=_F3PbbEthernetNetPortStatsTable_Object((1,3,6,1,4,1,2544,1,12,21,2,1))
if mibBuilder.loadTexts:f3PbbEthernetNetPortStatsTable.setStatus(_A)
_F3PbbEthernetNetPortStatsEntry_Object=MibTableRow
f3PbbEthernetNetPortStatsEntry=_F3PbbEthernetNetPortStatsEntry_Object((1,3,6,1,4,1,2544,1,12,21,2,1,1))
if mibBuilder.loadTexts:f3PbbEthernetNetPortStatsEntry.setStatus(_A)
_F3PbbEthernetNetPortStatsPbbUniBdaDiscard_Type=PerfCounter64
_F3PbbEthernetNetPortStatsPbbUniBdaDiscard_Object=MibTableColumn
f3PbbEthernetNetPortStatsPbbUniBdaDiscard=_F3PbbEthernetNetPortStatsPbbUniBdaDiscard_Object((1,3,6,1,4,1,2544,1,12,21,2,1,1,1),_F3PbbEthernetNetPortStatsPbbUniBdaDiscard_Type())
f3PbbEthernetNetPortStatsPbbUniBdaDiscard.setMaxAccess(_E)
if mibBuilder.loadTexts:f3PbbEthernetNetPortStatsPbbUniBdaDiscard.setStatus(_A)
_F3PbbEthernetNetPortStatsPbbGroupBdaDiscard_Type=PerfCounter64
_F3PbbEthernetNetPortStatsPbbGroupBdaDiscard_Object=MibTableColumn
f3PbbEthernetNetPortStatsPbbGroupBdaDiscard=_F3PbbEthernetNetPortStatsPbbGroupBdaDiscard_Object((1,3,6,1,4,1,2544,1,12,21,2,1,1,2),_F3PbbEthernetNetPortStatsPbbGroupBdaDiscard_Type())
f3PbbEthernetNetPortStatsPbbGroupBdaDiscard.setMaxAccess(_E)
if mibBuilder.loadTexts:f3PbbEthernetNetPortStatsPbbGroupBdaDiscard.setStatus(_A)
_F3PbbEthernetNetPortHistoryStatsTable_Object=MibTable
f3PbbEthernetNetPortHistoryStatsTable=_F3PbbEthernetNetPortHistoryStatsTable_Object((1,3,6,1,4,1,2544,1,12,21,2,2))
if mibBuilder.loadTexts:f3PbbEthernetNetPortHistoryStatsTable.setStatus(_A)
_F3PbbEthernetNetPortHistoryStatsEntry_Object=MibTableRow
f3PbbEthernetNetPortHistoryStatsEntry=_F3PbbEthernetNetPortHistoryStatsEntry_Object((1,3,6,1,4,1,2544,1,12,21,2,2,1))
if mibBuilder.loadTexts:f3PbbEthernetNetPortHistoryStatsEntry.setStatus(_A)
_F3PbbEthernetNetPortHistoryStatsPbbUniBdaDiscard_Type=PerfCounter64
_F3PbbEthernetNetPortHistoryStatsPbbUniBdaDiscard_Object=MibTableColumn
f3PbbEthernetNetPortHistoryStatsPbbUniBdaDiscard=_F3PbbEthernetNetPortHistoryStatsPbbUniBdaDiscard_Object((1,3,6,1,4,1,2544,1,12,21,2,2,1,1),_F3PbbEthernetNetPortHistoryStatsPbbUniBdaDiscard_Type())
f3PbbEthernetNetPortHistoryStatsPbbUniBdaDiscard.setMaxAccess(_E)
if mibBuilder.loadTexts:f3PbbEthernetNetPortHistoryStatsPbbUniBdaDiscard.setStatus(_A)
_F3PbbEthernetNetPortHistoryStatsPbbGroupBdaDiscard_Type=PerfCounter64
_F3PbbEthernetNetPortHistoryStatsPbbGroupBdaDiscard_Object=MibTableColumn
f3PbbEthernetNetPortHistoryStatsPbbGroupBdaDiscard=_F3PbbEthernetNetPortHistoryStatsPbbGroupBdaDiscard_Object((1,3,6,1,4,1,2544,1,12,21,2,2,1,2),_F3PbbEthernetNetPortHistoryStatsPbbGroupBdaDiscard_Type())
f3PbbEthernetNetPortHistoryStatsPbbGroupBdaDiscard.setMaxAccess(_E)
if mibBuilder.loadTexts:f3PbbEthernetNetPortHistoryStatsPbbGroupBdaDiscard.setStatus(_A)
_F3PBBConformance_ObjectIdentity=ObjectIdentity
f3PBBConformance=_F3PBBConformance_ObjectIdentity((1,3,6,1,4,1,2544,1,12,21,3))
_F3PBBCompliances_ObjectIdentity=ObjectIdentity
f3PBBCompliances=_F3PBBCompliances_ObjectIdentity((1,3,6,1,4,1,2544,1,12,21,3,1))
_F3PBBGroups_ObjectIdentity=ObjectIdentity
f3PBBGroups=_F3PBBGroups_ObjectIdentity((1,3,6,1,4,1,2544,1,12,21,3,2))
cmEthernetAccPortEntry.registerAugmentions((_B,_F))
f3PbbEthernetAccPortEntry.setIndexNames(*cmEthernetAccPortEntry.getIndexNames())
cmEthernetNetPortEntry.registerAugmentions((_B,_G))
f3PbbEthernetNetPortEntry.setIndexNames(*cmEthernetNetPortEntry.getIndexNames())
cmFlowEntry.registerAugmentions((_B,_H))
f3PbbFlowEntry.setIndexNames(*cmFlowEntry.getIndexNames())
ipManagementTunnelEntry.registerAugmentions((_B,_I))
f3PbbIpManagementTunnelEntry.setIndexNames(*ipManagementTunnelEntry.getIndexNames())
cmEthernetNetPortStatsEntry.registerAugmentions((_B,_J))
f3PbbEthernetNetPortStatsEntry.setIndexNames(*cmEthernetNetPortStatsEntry.getIndexNames())
cmEthernetNetPortHistoryEntry.registerAugmentions((_B,_K))
f3PbbEthernetNetPortHistoryStatsEntry.setIndexNames(*cmEthernetNetPortHistoryEntry.getIndexNames())
f3PbbConfigGroup=ObjectGroup((1,3,6,1,4,1,2544,1,12,21,3,2,1))
f3PbbConfigGroup.setObjects(*((_B,_L),(_B,_M),(_B,_N),(_B,_O),(_B,_P),(_B,_Q),(_B,_R),(_B,_S),(_B,_T),(_B,_U),(_B,_V),(_B,_W),(_B,_X),(_B,_Y),(_B,_Z),(_B,_a),(_B,_b),(_B,_c),(_B,_d),(_B,_e)))
if mibBuilder.loadTexts:f3PbbConfigGroup.setStatus(_A)
f3PbbStatsGroup=ObjectGroup((1,3,6,1,4,1,2544,1,12,21,3,2,2))
f3PbbStatsGroup.setObjects(*((_B,_f),(_B,_g),(_B,_h),(_B,_i)))
if mibBuilder.loadTexts:f3PbbStatsGroup.setStatus(_A)
f3PBBCompliance=ModuleCompliance((1,3,6,1,4,1,2544,1,12,21,3,1,1))
f3PBBCompliance.setObjects(*((_B,_j),(_B,_k)))
if mibBuilder.loadTexts:f3PBBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'f3PBBMIB':f3PBBMIB,'f3PBBConfigObjects':f3PBBConfigObjects,'f3PbbEthernetAccPortTable':f3PbbEthernetAccPortTable,_F:f3PbbEthernetAccPortEntry,_L:f3PbbEthernetAccPortITagLoopbackMask,_M:f3PbbEthernetAccPortITagLoopback1,_N:f3PbbEthernetAccPortITagLoopback2,_O:f3PbbEthernetAccPortITagLoopback3,'f3PbbEthernetNetPortTable':f3PbbEthernetNetPortTable,_G:f3PbbEthernetNetPortEntry,_P:f3PbbEthernetNetPortBackboneMacAddress,_Q:f3PbbEthernetNetPortITagLoopbackMask,_R:f3PbbEthernetNetPortITagLoopback1,_S:f3PbbEthernetNetPortITagLoopback2,_T:f3PbbEthernetNetPortITagLoopback3,'f3PbbFlowTable':f3PbbFlowTable,_H:f3PbbFlowEntry,_U:f3PbbFlowITagControl,_V:f3PbbFlowITagISID,_W:f3PbbFlowITagPriority,_X:f3PbbFlowBackboneMacDestinationEnabled,_Y:f3PbbFlowBackboneMacDestinationAddress,_Z:f3PbbFlowA2NPbbCapableFlag,'f3PbbIpManagementTunnelTable':f3PbbIpManagementTunnelTable,_I:f3PbbIpManagementTunnelEntry,_a:f3PbbIpManagementTunnelItagEnabled,_b:f3PbbIpManagementTunnelISID,_c:f3PbbIpManagementTunnelIPriority,_d:f3PbbIpManagementTunnelBackboneMacDestinationEnabled,_e:f3PbbIpManagementTunnelBackboneMacDestinationAddress,'f3PBBPerformanceObjects':f3PBBPerformanceObjects,'f3PbbEthernetNetPortStatsTable':f3PbbEthernetNetPortStatsTable,_J:f3PbbEthernetNetPortStatsEntry,_f:f3PbbEthernetNetPortStatsPbbUniBdaDiscard,_g:f3PbbEthernetNetPortStatsPbbGroupBdaDiscard,'f3PbbEthernetNetPortHistoryStatsTable':f3PbbEthernetNetPortHistoryStatsTable,_K:f3PbbEthernetNetPortHistoryStatsEntry,_h:f3PbbEthernetNetPortHistoryStatsPbbUniBdaDiscard,_i:f3PbbEthernetNetPortHistoryStatsPbbGroupBdaDiscard,'f3PBBConformance':f3PBBConformance,'f3PBBCompliances':f3PBBCompliances,'f3PBBCompliance':f3PBBCompliance,'f3PBBGroups':f3PBBGroups,_j:f3PbbConfigGroup,_k:f3PbbStatsGroup})