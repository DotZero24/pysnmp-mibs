_x='juniIgmpGroupsGroup2'
_w='juniIgmpInterfaceGroup'
_v='juniIgmpGroupsMaxGroups2'
_u='juniIgmpIfLocationType'
_t='juniIgmpAdminState'
_s='juniIgmpGroupsMaxGroups'
_r='juniIgmpProxyStatus'
_q='juniIgmpProxyInterfaceLeaveReportCount'
_p='juniIgmpProxyInterfaceV2JoinReportCount'
_o='juniIgmpProxyInterfaceV1JoinReportCount'
_n='juniIgmpProxyInterfaceV2ReportReceiveCount'
_m='juniIgmpProxyInterfaceV1ReportReceiveCount'
_l='juniIgmpProxyInterfaceV2QueryReceiveCount'
_k='juniIgmpProxyInterfaceV1QueryReceiveCount'
_j='juniIgmpProxyInterfaceWrongVersionCount'
_i='juniIgmpProxyInterfaceTotalGroupCount'
_h='juniIgmpProxyInterfaceUnsolicitedReportInterval'
_g='juniIgmpProxyInterfaceV1RoutePresentTimeout'
_f='juniIgmpProxyInterfaceVersion'
_e='juniIgmpProxyInterfaceStatus'
_d='juniIgmpProxyInterfaceState'
_c='juniIgmpProxyInterfaceMask'
_b='juniIgmpProxyInterfaceAddress'
_a='juniIgmpIfLocationIndex'
_Z='juniIgmpGroupsPort'
_Y='juniIgmpGroupsSlot'
_X='juniIgmpProxyAddress'
_W='juniIgmpProxyIfIndex'
_V='juniIgmpProxyInterfaceIfIndex'
_U='juniIgmpInterfaceIfIndex'
_T='juniIgmpInterfaceGroup2'
_S='juniIgmpGroupsGroup'
_R='obsolete'
_Q='juniIgmpRouterPromiscuous'
_P='juniIgmpInterfaceMaxGroups'
_O='juniIgmpInterfacePromiscuous'
_N='juniIgmpInterfaceAccessGroup'
_M='juniIgmpInterfaceImmediateLeave'
_L='juniIgmpInterfaceQuerierTimeout'
_K='read-create'
_J='seconds'
_I='juniIgmpProxyCacheGroup'
_H='juniIgmpProxyInterfaceGroup'
_G='deprecated'
_F='not-accessible'
_E='read-write'
_D='Integer32'
_C='read-only'
_B='current'
_A='Juniper-IGMP-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
InterfaceIndex,=mibBuilder.importSymbols('IF-MIB','InterfaceIndex')
juniMibs,=mibBuilder.importSymbols('Juniper-MIBs','juniMibs')
JuniInterfaceLocationType,JuniInterfaceLocationValue=mibBuilder.importSymbols('Juniper-TC','JuniInterfaceLocationType','JuniInterfaceLocationValue')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention','TruthValue')
juniIgmpMIB=ModuleIdentity((1,3,6,1,4,1,4874,2,2,40))
if mibBuilder.loadTexts:juniIgmpMIB.setRevisions(('2006-08-25 05:40','2003-09-29 18:39','2002-10-28 14:55','2000-09-26 18:50'))
class JuniIgmpProxyGroupState(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('juniIgmpProxyGroupUnknown',0),('juniIgmpProxyGroupIdleMember',1),('juniIgmpProxyGroupDelayingMember',2)))
class JuniIgmpProxyInterfaceState(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('juniIgmpProxyInterfaceUnknown',0),('juniIgmpProxyInterfaceStateV1RouterPresent',1),('juniIgmpProxyInterfaceStateNonV1RouterPresent',2)))
_JuniIgmpMIBObject_ObjectIdentity=ObjectIdentity
juniIgmpMIBObject=_JuniIgmpMIBObject_ObjectIdentity((1,3,6,1,4,1,4874,2,2,40,1))
_JuniIgmpProtocol_ObjectIdentity=ObjectIdentity
juniIgmpProtocol=_JuniIgmpProtocol_ObjectIdentity((1,3,6,1,4,1,4874,2,2,40,1,1))
_JuniIgmpInterfaceTable_Object=MibTable
juniIgmpInterfaceTable=_JuniIgmpInterfaceTable_Object((1,3,6,1,4,1,4874,2,2,40,1,1,1))
if mibBuilder.loadTexts:juniIgmpInterfaceTable.setStatus(_B)
_JuniIgmpInterfaceEntry_Object=MibTableRow
juniIgmpInterfaceEntry=_JuniIgmpInterfaceEntry_Object((1,3,6,1,4,1,4874,2,2,40,1,1,1,1))
juniIgmpInterfaceEntry.setIndexNames((0,_A,_U))
if mibBuilder.loadTexts:juniIgmpInterfaceEntry.setStatus(_B)
_JuniIgmpInterfaceIfIndex_Type=InterfaceIndex
_JuniIgmpInterfaceIfIndex_Object=MibTableColumn
juniIgmpInterfaceIfIndex=_JuniIgmpInterfaceIfIndex_Object((1,3,6,1,4,1,4874,2,2,40,1,1,1,1,1),_JuniIgmpInterfaceIfIndex_Type())
juniIgmpInterfaceIfIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:juniIgmpInterfaceIfIndex.setStatus(_B)
class _JuniIgmpInterfaceQuerierTimeout_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,399))
_JuniIgmpInterfaceQuerierTimeout_Type.__name__=_D
_JuniIgmpInterfaceQuerierTimeout_Object=MibTableColumn
juniIgmpInterfaceQuerierTimeout=_JuniIgmpInterfaceQuerierTimeout_Object((1,3,6,1,4,1,4874,2,2,40,1,1,1,1,2),_JuniIgmpInterfaceQuerierTimeout_Type())
juniIgmpInterfaceQuerierTimeout.setMaxAccess(_E)
if mibBuilder.loadTexts:juniIgmpInterfaceQuerierTimeout.setStatus(_B)
if mibBuilder.loadTexts:juniIgmpInterfaceQuerierTimeout.setUnits(_J)
_JuniIgmpInterfaceImmediateLeave_Type=TruthValue
_JuniIgmpInterfaceImmediateLeave_Object=MibTableColumn
juniIgmpInterfaceImmediateLeave=_JuniIgmpInterfaceImmediateLeave_Object((1,3,6,1,4,1,4874,2,2,40,1,1,1,1,3),_JuniIgmpInterfaceImmediateLeave_Type())
juniIgmpInterfaceImmediateLeave.setMaxAccess(_E)
if mibBuilder.loadTexts:juniIgmpInterfaceImmediateLeave.setStatus(_B)
_JuniIgmpInterfaceAccessGroup_Type=DisplayString
_JuniIgmpInterfaceAccessGroup_Object=MibTableColumn
juniIgmpInterfaceAccessGroup=_JuniIgmpInterfaceAccessGroup_Object((1,3,6,1,4,1,4874,2,2,40,1,1,1,1,4),_JuniIgmpInterfaceAccessGroup_Type())
juniIgmpInterfaceAccessGroup.setMaxAccess(_E)
if mibBuilder.loadTexts:juniIgmpInterfaceAccessGroup.setStatus(_B)
_JuniIgmpInterfacePromiscuous_Type=TruthValue
_JuniIgmpInterfacePromiscuous_Object=MibTableColumn
juniIgmpInterfacePromiscuous=_JuniIgmpInterfacePromiscuous_Object((1,3,6,1,4,1,4874,2,2,40,1,1,1,1,5),_JuniIgmpInterfacePromiscuous_Type())
juniIgmpInterfacePromiscuous.setMaxAccess(_E)
if mibBuilder.loadTexts:juniIgmpInterfacePromiscuous.setStatus(_B)
class _JuniIgmpInterfaceMaxGroups_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,65535))
_JuniIgmpInterfaceMaxGroups_Type.__name__=_D
_JuniIgmpInterfaceMaxGroups_Object=MibTableColumn
juniIgmpInterfaceMaxGroups=_JuniIgmpInterfaceMaxGroups_Object((1,3,6,1,4,1,4874,2,2,40,1,1,1,1,6),_JuniIgmpInterfaceMaxGroups_Type())
juniIgmpInterfaceMaxGroups.setMaxAccess(_E)
if mibBuilder.loadTexts:juniIgmpInterfaceMaxGroups.setStatus(_B)
_JuniIgmpInterfaceIoaPacketReplIfIndex_Type=InterfaceIndex
_JuniIgmpInterfaceIoaPacketReplIfIndex_Object=MibTableColumn
juniIgmpInterfaceIoaPacketReplIfIndex=_JuniIgmpInterfaceIoaPacketReplIfIndex_Object((1,3,6,1,4,1,4874,2,2,40,1,1,1,1,7),_JuniIgmpInterfaceIoaPacketReplIfIndex_Type())
juniIgmpInterfaceIoaPacketReplIfIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:juniIgmpInterfaceIoaPacketReplIfIndex.setStatus(_B)
_JuniIgmpRouterPromiscuous_Type=TruthValue
_JuniIgmpRouterPromiscuous_Object=MibScalar
juniIgmpRouterPromiscuous=_JuniIgmpRouterPromiscuous_Object((1,3,6,1,4,1,4874,2,2,40,1,1,2),_JuniIgmpRouterPromiscuous_Type())
juniIgmpRouterPromiscuous.setMaxAccess(_E)
if mibBuilder.loadTexts:juniIgmpRouterPromiscuous.setStatus(_B)
class _JuniIgmpAdminState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('disable',0),('enable',1)))
_JuniIgmpAdminState_Type.__name__=_D
_JuniIgmpAdminState_Object=MibScalar
juniIgmpAdminState=_JuniIgmpAdminState_Object((1,3,6,1,4,1,4874,2,2,40,1,1,3),_JuniIgmpAdminState_Type())
juniIgmpAdminState.setMaxAccess(_E)
if mibBuilder.loadTexts:juniIgmpAdminState.setStatus(_B)
_JuniIgmpProxy_ObjectIdentity=ObjectIdentity
juniIgmpProxy=_JuniIgmpProxy_ObjectIdentity((1,3,6,1,4,1,4874,2,2,40,1,2))
_JuniIgmpProxyInterfaceTable_Object=MibTable
juniIgmpProxyInterfaceTable=_JuniIgmpProxyInterfaceTable_Object((1,3,6,1,4,1,4874,2,2,40,1,2,1))
if mibBuilder.loadTexts:juniIgmpProxyInterfaceTable.setStatus(_B)
_JuniIgmpProxyInterfaceEntry_Object=MibTableRow
juniIgmpProxyInterfaceEntry=_JuniIgmpProxyInterfaceEntry_Object((1,3,6,1,4,1,4874,2,2,40,1,2,1,1))
juniIgmpProxyInterfaceEntry.setIndexNames((0,_A,_V))
if mibBuilder.loadTexts:juniIgmpProxyInterfaceEntry.setStatus(_B)
_JuniIgmpProxyInterfaceIfIndex_Type=InterfaceIndex
_JuniIgmpProxyInterfaceIfIndex_Object=MibTableColumn
juniIgmpProxyInterfaceIfIndex=_JuniIgmpProxyInterfaceIfIndex_Object((1,3,6,1,4,1,4874,2,2,40,1,2,1,1,1),_JuniIgmpProxyInterfaceIfIndex_Type())
juniIgmpProxyInterfaceIfIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:juniIgmpProxyInterfaceIfIndex.setStatus(_B)
_JuniIgmpProxyInterfaceAddress_Type=IpAddress
_JuniIgmpProxyInterfaceAddress_Object=MibTableColumn
juniIgmpProxyInterfaceAddress=_JuniIgmpProxyInterfaceAddress_Object((1,3,6,1,4,1,4874,2,2,40,1,2,1,1,2),_JuniIgmpProxyInterfaceAddress_Type())
juniIgmpProxyInterfaceAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:juniIgmpProxyInterfaceAddress.setStatus(_B)
_JuniIgmpProxyInterfaceMask_Type=IpAddress
_JuniIgmpProxyInterfaceMask_Object=MibTableColumn
juniIgmpProxyInterfaceMask=_JuniIgmpProxyInterfaceMask_Object((1,3,6,1,4,1,4874,2,2,40,1,2,1,1,3),_JuniIgmpProxyInterfaceMask_Type())
juniIgmpProxyInterfaceMask.setMaxAccess(_C)
if mibBuilder.loadTexts:juniIgmpProxyInterfaceMask.setStatus(_B)
_JuniIgmpProxyInterfaceState_Type=JuniIgmpProxyInterfaceState
_JuniIgmpProxyInterfaceState_Object=MibTableColumn
juniIgmpProxyInterfaceState=_JuniIgmpProxyInterfaceState_Object((1,3,6,1,4,1,4874,2,2,40,1,2,1,1,4),_JuniIgmpProxyInterfaceState_Type())
juniIgmpProxyInterfaceState.setMaxAccess(_C)
if mibBuilder.loadTexts:juniIgmpProxyInterfaceState.setStatus(_B)
_JuniIgmpProxyInterfaceStatus_Type=RowStatus
_JuniIgmpProxyInterfaceStatus_Object=MibTableColumn
juniIgmpProxyInterfaceStatus=_JuniIgmpProxyInterfaceStatus_Object((1,3,6,1,4,1,4874,2,2,40,1,2,1,1,5),_JuniIgmpProxyInterfaceStatus_Type())
juniIgmpProxyInterfaceStatus.setMaxAccess(_K)
if mibBuilder.loadTexts:juniIgmpProxyInterfaceStatus.setStatus(_B)
_JuniIgmpProxyInterfaceVersion_Type=Integer32
_JuniIgmpProxyInterfaceVersion_Object=MibTableColumn
juniIgmpProxyInterfaceVersion=_JuniIgmpProxyInterfaceVersion_Object((1,3,6,1,4,1,4874,2,2,40,1,2,1,1,6),_JuniIgmpProxyInterfaceVersion_Type())
juniIgmpProxyInterfaceVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:juniIgmpProxyInterfaceVersion.setStatus(_B)
class _JuniIgmpProxyInterfaceV1RoutePresentTimeout_Type(Integer32):defaultValue=400;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1000))
_JuniIgmpProxyInterfaceV1RoutePresentTimeout_Type.__name__=_D
_JuniIgmpProxyInterfaceV1RoutePresentTimeout_Object=MibTableColumn
juniIgmpProxyInterfaceV1RoutePresentTimeout=_JuniIgmpProxyInterfaceV1RoutePresentTimeout_Object((1,3,6,1,4,1,4874,2,2,40,1,2,1,1,7),_JuniIgmpProxyInterfaceV1RoutePresentTimeout_Type())
juniIgmpProxyInterfaceV1RoutePresentTimeout.setMaxAccess(_K)
if mibBuilder.loadTexts:juniIgmpProxyInterfaceV1RoutePresentTimeout.setStatus(_B)
if mibBuilder.loadTexts:juniIgmpProxyInterfaceV1RoutePresentTimeout.setUnits(_J)
class _JuniIgmpProxyInterfaceUnsolicitedReportInterval_Type(Integer32):defaultValue=10;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1000))
_JuniIgmpProxyInterfaceUnsolicitedReportInterval_Type.__name__=_D
_JuniIgmpProxyInterfaceUnsolicitedReportInterval_Object=MibTableColumn
juniIgmpProxyInterfaceUnsolicitedReportInterval=_JuniIgmpProxyInterfaceUnsolicitedReportInterval_Object((1,3,6,1,4,1,4874,2,2,40,1,2,1,1,8),_JuniIgmpProxyInterfaceUnsolicitedReportInterval_Type())
juniIgmpProxyInterfaceUnsolicitedReportInterval.setMaxAccess(_K)
if mibBuilder.loadTexts:juniIgmpProxyInterfaceUnsolicitedReportInterval.setStatus(_B)
if mibBuilder.loadTexts:juniIgmpProxyInterfaceUnsolicitedReportInterval.setUnits(_J)
_JuniIgmpProxyInterfaceTotalGroupCount_Type=Counter32
_JuniIgmpProxyInterfaceTotalGroupCount_Object=MibTableColumn
juniIgmpProxyInterfaceTotalGroupCount=_JuniIgmpProxyInterfaceTotalGroupCount_Object((1,3,6,1,4,1,4874,2,2,40,1,2,1,1,9),_JuniIgmpProxyInterfaceTotalGroupCount_Type())
juniIgmpProxyInterfaceTotalGroupCount.setMaxAccess(_C)
if mibBuilder.loadTexts:juniIgmpProxyInterfaceTotalGroupCount.setStatus(_B)
_JuniIgmpProxyInterfaceWrongVersionCount_Type=Counter32
_JuniIgmpProxyInterfaceWrongVersionCount_Object=MibTableColumn
juniIgmpProxyInterfaceWrongVersionCount=_JuniIgmpProxyInterfaceWrongVersionCount_Object((1,3,6,1,4,1,4874,2,2,40,1,2,1,1,10),_JuniIgmpProxyInterfaceWrongVersionCount_Type())
juniIgmpProxyInterfaceWrongVersionCount.setMaxAccess(_C)
if mibBuilder.loadTexts:juniIgmpProxyInterfaceWrongVersionCount.setStatus(_B)
_JuniIgmpProxyInterfaceV1QueryReceiveCount_Type=Counter32
_JuniIgmpProxyInterfaceV1QueryReceiveCount_Object=MibTableColumn
juniIgmpProxyInterfaceV1QueryReceiveCount=_JuniIgmpProxyInterfaceV1QueryReceiveCount_Object((1,3,6,1,4,1,4874,2,2,40,1,2,1,1,11),_JuniIgmpProxyInterfaceV1QueryReceiveCount_Type())
juniIgmpProxyInterfaceV1QueryReceiveCount.setMaxAccess(_C)
if mibBuilder.loadTexts:juniIgmpProxyInterfaceV1QueryReceiveCount.setStatus(_B)
_JuniIgmpProxyInterfaceV2QueryReceiveCount_Type=Counter32
_JuniIgmpProxyInterfaceV2QueryReceiveCount_Object=MibTableColumn
juniIgmpProxyInterfaceV2QueryReceiveCount=_JuniIgmpProxyInterfaceV2QueryReceiveCount_Object((1,3,6,1,4,1,4874,2,2,40,1,2,1,1,12),_JuniIgmpProxyInterfaceV2QueryReceiveCount_Type())
juniIgmpProxyInterfaceV2QueryReceiveCount.setMaxAccess(_C)
if mibBuilder.loadTexts:juniIgmpProxyInterfaceV2QueryReceiveCount.setStatus(_B)
_JuniIgmpProxyInterfaceV1ReportReceiveCount_Type=Counter32
_JuniIgmpProxyInterfaceV1ReportReceiveCount_Object=MibTableColumn
juniIgmpProxyInterfaceV1ReportReceiveCount=_JuniIgmpProxyInterfaceV1ReportReceiveCount_Object((1,3,6,1,4,1,4874,2,2,40,1,2,1,1,13),_JuniIgmpProxyInterfaceV1ReportReceiveCount_Type())
juniIgmpProxyInterfaceV1ReportReceiveCount.setMaxAccess(_C)
if mibBuilder.loadTexts:juniIgmpProxyInterfaceV1ReportReceiveCount.setStatus(_B)
_JuniIgmpProxyInterfaceV2ReportReceiveCount_Type=Counter32
_JuniIgmpProxyInterfaceV2ReportReceiveCount_Object=MibTableColumn
juniIgmpProxyInterfaceV2ReportReceiveCount=_JuniIgmpProxyInterfaceV2ReportReceiveCount_Object((1,3,6,1,4,1,4874,2,2,40,1,2,1,1,14),_JuniIgmpProxyInterfaceV2ReportReceiveCount_Type())
juniIgmpProxyInterfaceV2ReportReceiveCount.setMaxAccess(_C)
if mibBuilder.loadTexts:juniIgmpProxyInterfaceV2ReportReceiveCount.setStatus(_B)
_JuniIgmpProxyInterfaceV1JoinReportCount_Type=Counter32
_JuniIgmpProxyInterfaceV1JoinReportCount_Object=MibTableColumn
juniIgmpProxyInterfaceV1JoinReportCount=_JuniIgmpProxyInterfaceV1JoinReportCount_Object((1,3,6,1,4,1,4874,2,2,40,1,2,1,1,15),_JuniIgmpProxyInterfaceV1JoinReportCount_Type())
juniIgmpProxyInterfaceV1JoinReportCount.setMaxAccess(_C)
if mibBuilder.loadTexts:juniIgmpProxyInterfaceV1JoinReportCount.setStatus(_B)
_JuniIgmpProxyInterfaceV2JoinReportCount_Type=Counter32
_JuniIgmpProxyInterfaceV2JoinReportCount_Object=MibTableColumn
juniIgmpProxyInterfaceV2JoinReportCount=_JuniIgmpProxyInterfaceV2JoinReportCount_Object((1,3,6,1,4,1,4874,2,2,40,1,2,1,1,16),_JuniIgmpProxyInterfaceV2JoinReportCount_Type())
juniIgmpProxyInterfaceV2JoinReportCount.setMaxAccess(_C)
if mibBuilder.loadTexts:juniIgmpProxyInterfaceV2JoinReportCount.setStatus(_B)
_JuniIgmpProxyInterfaceLeaveReportCount_Type=Counter32
_JuniIgmpProxyInterfaceLeaveReportCount_Object=MibTableColumn
juniIgmpProxyInterfaceLeaveReportCount=_JuniIgmpProxyInterfaceLeaveReportCount_Object((1,3,6,1,4,1,4874,2,2,40,1,2,1,1,17),_JuniIgmpProxyInterfaceLeaveReportCount_Type())
juniIgmpProxyInterfaceLeaveReportCount.setMaxAccess(_C)
if mibBuilder.loadTexts:juniIgmpProxyInterfaceLeaveReportCount.setStatus(_B)
_JuniIgmpProxyCacheTable_Object=MibTable
juniIgmpProxyCacheTable=_JuniIgmpProxyCacheTable_Object((1,3,6,1,4,1,4874,2,2,40,1,2,2))
if mibBuilder.loadTexts:juniIgmpProxyCacheTable.setStatus(_B)
_JuniIgmpProxyCacheEntry_Object=MibTableRow
juniIgmpProxyCacheEntry=_JuniIgmpProxyCacheEntry_Object((1,3,6,1,4,1,4874,2,2,40,1,2,2,1))
juniIgmpProxyCacheEntry.setIndexNames((0,_A,_W),(0,_A,_X))
if mibBuilder.loadTexts:juniIgmpProxyCacheEntry.setStatus(_B)
_JuniIgmpProxyIfIndex_Type=InterfaceIndex
_JuniIgmpProxyIfIndex_Object=MibTableColumn
juniIgmpProxyIfIndex=_JuniIgmpProxyIfIndex_Object((1,3,6,1,4,1,4874,2,2,40,1,2,2,1,1),_JuniIgmpProxyIfIndex_Type())
juniIgmpProxyIfIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:juniIgmpProxyIfIndex.setStatus(_B)
_JuniIgmpProxyAddress_Type=IpAddress
_JuniIgmpProxyAddress_Object=MibTableColumn
juniIgmpProxyAddress=_JuniIgmpProxyAddress_Object((1,3,6,1,4,1,4874,2,2,40,1,2,2,1,2),_JuniIgmpProxyAddress_Type())
juniIgmpProxyAddress.setMaxAccess(_F)
if mibBuilder.loadTexts:juniIgmpProxyAddress.setStatus(_B)
_JuniIgmpProxyStatus_Type=JuniIgmpProxyGroupState
_JuniIgmpProxyStatus_Object=MibTableColumn
juniIgmpProxyStatus=_JuniIgmpProxyStatus_Object((1,3,6,1,4,1,4874,2,2,40,1,2,2,1,3),_JuniIgmpProxyStatus_Type())
juniIgmpProxyStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:juniIgmpProxyStatus.setStatus(_B)
_JuniIgmpGlobal_ObjectIdentity=ObjectIdentity
juniIgmpGlobal=_JuniIgmpGlobal_ObjectIdentity((1,3,6,1,4,1,4874,2,2,40,1,3))
_JuniIgmpGroupsTable_Object=MibTable
juniIgmpGroupsTable=_JuniIgmpGroupsTable_Object((1,3,6,1,4,1,4874,2,2,40,1,3,1))
if mibBuilder.loadTexts:juniIgmpGroupsTable.setStatus(_G)
_JuniIgmpGroupsEntry_Object=MibTableRow
juniIgmpGroupsEntry=_JuniIgmpGroupsEntry_Object((1,3,6,1,4,1,4874,2,2,40,1,3,1,1))
juniIgmpGroupsEntry.setIndexNames((0,_A,_Y),(0,_A,_Z))
if mibBuilder.loadTexts:juniIgmpGroupsEntry.setStatus(_G)
class _JuniIgmpGroupsSlot_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_JuniIgmpGroupsSlot_Type.__name__=_D
_JuniIgmpGroupsSlot_Object=MibTableColumn
juniIgmpGroupsSlot=_JuniIgmpGroupsSlot_Object((1,3,6,1,4,1,4874,2,2,40,1,3,1,1,1),_JuniIgmpGroupsSlot_Type())
juniIgmpGroupsSlot.setMaxAccess(_F)
if mibBuilder.loadTexts:juniIgmpGroupsSlot.setStatus(_G)
class _JuniIgmpGroupsPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_JuniIgmpGroupsPort_Type.__name__=_D
_JuniIgmpGroupsPort_Object=MibTableColumn
juniIgmpGroupsPort=_JuniIgmpGroupsPort_Object((1,3,6,1,4,1,4874,2,2,40,1,3,1,1,2),_JuniIgmpGroupsPort_Type())
juniIgmpGroupsPort.setMaxAccess(_F)
if mibBuilder.loadTexts:juniIgmpGroupsPort.setStatus(_G)
class _JuniIgmpGroupsMaxGroups_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,65535))
_JuniIgmpGroupsMaxGroups_Type.__name__=_D
_JuniIgmpGroupsMaxGroups_Object=MibTableColumn
juniIgmpGroupsMaxGroups=_JuniIgmpGroupsMaxGroups_Object((1,3,6,1,4,1,4874,2,2,40,1,3,1,1,3),_JuniIgmpGroupsMaxGroups_Type())
juniIgmpGroupsMaxGroups.setMaxAccess(_E)
if mibBuilder.loadTexts:juniIgmpGroupsMaxGroups.setStatus(_G)
_JuniIgmpIfLocationType_Type=JuniInterfaceLocationType
_JuniIgmpIfLocationType_Object=MibScalar
juniIgmpIfLocationType=_JuniIgmpIfLocationType_Object((1,3,6,1,4,1,4874,2,2,40,1,3,2),_JuniIgmpIfLocationType_Type())
juniIgmpIfLocationType.setMaxAccess(_C)
if mibBuilder.loadTexts:juniIgmpIfLocationType.setStatus(_B)
_JuniIgmpGroupsTable2_Object=MibTable
juniIgmpGroupsTable2=_JuniIgmpGroupsTable2_Object((1,3,6,1,4,1,4874,2,2,40,1,3,3))
if mibBuilder.loadTexts:juniIgmpGroupsTable2.setStatus(_B)
_JuniIgmpGroupsEntry2_Object=MibTableRow
juniIgmpGroupsEntry2=_JuniIgmpGroupsEntry2_Object((1,3,6,1,4,1,4874,2,2,40,1,3,3,1))
juniIgmpGroupsEntry2.setIndexNames((0,_A,_a))
if mibBuilder.loadTexts:juniIgmpGroupsEntry2.setStatus(_B)
_JuniIgmpIfLocationIndex_Type=JuniInterfaceLocationValue
_JuniIgmpIfLocationIndex_Object=MibTableColumn
juniIgmpIfLocationIndex=_JuniIgmpIfLocationIndex_Object((1,3,6,1,4,1,4874,2,2,40,1,3,3,1,1),_JuniIgmpIfLocationIndex_Type())
juniIgmpIfLocationIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:juniIgmpIfLocationIndex.setStatus(_B)
class _JuniIgmpGroupsMaxGroups2_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,65535))
_JuniIgmpGroupsMaxGroups2_Type.__name__=_D
_JuniIgmpGroupsMaxGroups2_Object=MibTableColumn
juniIgmpGroupsMaxGroups2=_JuniIgmpGroupsMaxGroups2_Object((1,3,6,1,4,1,4874,2,2,40,1,3,3,1,2),_JuniIgmpGroupsMaxGroups2_Type())
juniIgmpGroupsMaxGroups2.setMaxAccess(_E)
if mibBuilder.loadTexts:juniIgmpGroupsMaxGroups2.setStatus(_B)
_JuniIgmpConformance_ObjectIdentity=ObjectIdentity
juniIgmpConformance=_JuniIgmpConformance_ObjectIdentity((1,3,6,1,4,1,4874,2,2,40,4))
_JuniIgmpCompliances_ObjectIdentity=ObjectIdentity
juniIgmpCompliances=_JuniIgmpCompliances_ObjectIdentity((1,3,6,1,4,1,4874,2,2,40,4,1))
_JuniIgmpGroups_ObjectIdentity=ObjectIdentity
juniIgmpGroups=_JuniIgmpGroups_ObjectIdentity((1,3,6,1,4,1,4874,2,2,40,4,2))
juniIgmpProxyInterfaceGroup=ObjectGroup((1,3,6,1,4,1,4874,2,2,40,4,2,1))
juniIgmpProxyInterfaceGroup.setObjects(*((_A,_b),(_A,_c),(_A,_d),(_A,_e),(_A,_f),(_A,_g),(_A,_h),(_A,_i),(_A,_j),(_A,_k),(_A,_l),(_A,_m),(_A,_n),(_A,_o),(_A,_p),(_A,_q)))
if mibBuilder.loadTexts:juniIgmpProxyInterfaceGroup.setStatus(_B)
juniIgmpProxyCacheGroup=ObjectGroup((1,3,6,1,4,1,4874,2,2,40,4,2,2))
juniIgmpProxyCacheGroup.setObjects((_A,_r))
if mibBuilder.loadTexts:juniIgmpProxyCacheGroup.setStatus(_B)
juniIgmpInterfaceGroup=ObjectGroup((1,3,6,1,4,1,4874,2,2,40,4,2,3))
juniIgmpInterfaceGroup.setObjects(*((_A,_L),(_A,_M),(_A,_N),(_A,_O),(_A,_P),(_A,_Q)))
if mibBuilder.loadTexts:juniIgmpInterfaceGroup.setStatus(_R)
juniIgmpGroupsGroup=ObjectGroup((1,3,6,1,4,1,4874,2,2,40,4,2,4))
juniIgmpGroupsGroup.setObjects((_A,_s))
if mibBuilder.loadTexts:juniIgmpGroupsGroup.setStatus(_G)
juniIgmpInterfaceGroup2=ObjectGroup((1,3,6,1,4,1,4874,2,2,40,4,2,5))
juniIgmpInterfaceGroup2.setObjects(*((_A,_L),(_A,_M),(_A,_N),(_A,_O),(_A,_P),(_A,_Q),(_A,_t)))
if mibBuilder.loadTexts:juniIgmpInterfaceGroup2.setStatus(_B)
juniIgmpGroupsGroup2=ObjectGroup((1,3,6,1,4,1,4874,2,2,40,4,2,6))
juniIgmpGroupsGroup2.setObjects(*((_A,_u),(_A,_v)))
if mibBuilder.loadTexts:juniIgmpGroupsGroup2.setStatus(_B)
juniIgmpCompliance=ModuleCompliance((1,3,6,1,4,1,4874,2,2,40,4,1,1))
juniIgmpCompliance.setObjects(*((_A,_H),(_A,_I)))
if mibBuilder.loadTexts:juniIgmpCompliance.setStatus(_R)
juniIgmpCompliance2=ModuleCompliance((1,3,6,1,4,1,4874,2,2,40,4,1,2))
juniIgmpCompliance2.setObjects(*((_A,_H),(_A,_I),(_A,_w),(_A,_S)))
if mibBuilder.loadTexts:juniIgmpCompliance2.setStatus(_R)
juniIgmpCompliance3=ModuleCompliance((1,3,6,1,4,1,4874,2,2,40,4,1,3))
juniIgmpCompliance3.setObjects(*((_A,_H),(_A,_I),(_A,_T),(_A,_S)))
if mibBuilder.loadTexts:juniIgmpCompliance3.setStatus(_G)
juniIgmpCompliance4=ModuleCompliance((1,3,6,1,4,1,4874,2,2,40,4,1,4))
juniIgmpCompliance4.setObjects(*((_A,_H),(_A,_I),(_A,_T),(_A,_x)))
if mibBuilder.loadTexts:juniIgmpCompliance4.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'JuniIgmpProxyGroupState':JuniIgmpProxyGroupState,'JuniIgmpProxyInterfaceState':JuniIgmpProxyInterfaceState,'juniIgmpMIB':juniIgmpMIB,'juniIgmpMIBObject':juniIgmpMIBObject,'juniIgmpProtocol':juniIgmpProtocol,'juniIgmpInterfaceTable':juniIgmpInterfaceTable,'juniIgmpInterfaceEntry':juniIgmpInterfaceEntry,_U:juniIgmpInterfaceIfIndex,_L:juniIgmpInterfaceQuerierTimeout,_M:juniIgmpInterfaceImmediateLeave,_N:juniIgmpInterfaceAccessGroup,_O:juniIgmpInterfacePromiscuous,_P:juniIgmpInterfaceMaxGroups,'juniIgmpInterfaceIoaPacketReplIfIndex':juniIgmpInterfaceIoaPacketReplIfIndex,_Q:juniIgmpRouterPromiscuous,_t:juniIgmpAdminState,'juniIgmpProxy':juniIgmpProxy,'juniIgmpProxyInterfaceTable':juniIgmpProxyInterfaceTable,'juniIgmpProxyInterfaceEntry':juniIgmpProxyInterfaceEntry,_V:juniIgmpProxyInterfaceIfIndex,_b:juniIgmpProxyInterfaceAddress,_c:juniIgmpProxyInterfaceMask,_d:juniIgmpProxyInterfaceState,_e:juniIgmpProxyInterfaceStatus,_f:juniIgmpProxyInterfaceVersion,_g:juniIgmpProxyInterfaceV1RoutePresentTimeout,_h:juniIgmpProxyInterfaceUnsolicitedReportInterval,_i:juniIgmpProxyInterfaceTotalGroupCount,_j:juniIgmpProxyInterfaceWrongVersionCount,_k:juniIgmpProxyInterfaceV1QueryReceiveCount,_l:juniIgmpProxyInterfaceV2QueryReceiveCount,_m:juniIgmpProxyInterfaceV1ReportReceiveCount,_n:juniIgmpProxyInterfaceV2ReportReceiveCount,_o:juniIgmpProxyInterfaceV1JoinReportCount,_p:juniIgmpProxyInterfaceV2JoinReportCount,_q:juniIgmpProxyInterfaceLeaveReportCount,'juniIgmpProxyCacheTable':juniIgmpProxyCacheTable,'juniIgmpProxyCacheEntry':juniIgmpProxyCacheEntry,_W:juniIgmpProxyIfIndex,_X:juniIgmpProxyAddress,_r:juniIgmpProxyStatus,'juniIgmpGlobal':juniIgmpGlobal,'juniIgmpGroupsTable':juniIgmpGroupsTable,'juniIgmpGroupsEntry':juniIgmpGroupsEntry,_Y:juniIgmpGroupsSlot,_Z:juniIgmpGroupsPort,_s:juniIgmpGroupsMaxGroups,_u:juniIgmpIfLocationType,'juniIgmpGroupsTable2':juniIgmpGroupsTable2,'juniIgmpGroupsEntry2':juniIgmpGroupsEntry2,_a:juniIgmpIfLocationIndex,_v:juniIgmpGroupsMaxGroups2,'juniIgmpConformance':juniIgmpConformance,'juniIgmpCompliances':juniIgmpCompliances,'juniIgmpCompliance':juniIgmpCompliance,'juniIgmpCompliance2':juniIgmpCompliance2,'juniIgmpCompliance3':juniIgmpCompliance3,'juniIgmpCompliance4':juniIgmpCompliance4,'juniIgmpGroups':juniIgmpGroups,_H:juniIgmpProxyInterfaceGroup,_I:juniIgmpProxyCacheGroup,_w:juniIgmpInterfaceGroup,_S:juniIgmpGroupsGroup,_T:juniIgmpInterfaceGroup2,_x:juniIgmpGroupsGroup2})