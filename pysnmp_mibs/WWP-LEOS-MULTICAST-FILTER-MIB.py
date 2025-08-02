_T='wwpLeosMcastPortId'
_S='wwpLeosMcastChannelStreamExPortId'
_R='wwpLeosMcastChanelStreamStartGroupAddr'
_Q='enable'
_P='disable'
_O='wwpLeosMcastServerPortId'
_N='wwpLeosMcastGroupAddr'
_M='disabled'
_L='enabled'
_K='read-create'
_J='TruthValue'
_I='seconds'
_H='drop'
_G='flood'
_F='wwpLeosMcastVlanId'
_E='WWP-LEOS-MULTICAST-FILTER-MIB'
_D='read-only'
_C='read-write'
_B='Integer32'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_B,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress','RowStatus','TextualConvention',_J)
wwpModulesLeos,=mibBuilder.importSymbols('WWP-SMI','wwpModulesLeos')
wwpLeosMcastFilterMIB=ModuleIdentity((1,3,6,1,4,1,6141,2,60,7))
if mibBuilder.loadTexts:wwpLeosMcastFilterMIB.setRevisions(('2008-10-02 19:00','2008-06-19 00:00','2003-02-10 17:00'))
class VlanId(TextualConvention,Integer32):status=_A;displayHint='d';subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,24576))
_WwpLeosMcastFilterMIBObjects_ObjectIdentity=ObjectIdentity
wwpLeosMcastFilterMIBObjects=_WwpLeosMcastFilterMIBObjects_ObjectIdentity((1,3,6,1,4,1,6141,2,60,7,1))
_WwpLeosMcastFilterConfig_ObjectIdentity=ObjectIdentity
wwpLeosMcastFilterConfig=_WwpLeosMcastFilterConfig_ObjectIdentity((1,3,6,1,4,1,6141,2,60,7,1,1))
class _WwpLeosMcastConfigState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_L,1),(_M,2)))
_WwpLeosMcastConfigState_Type.__name__=_B
_WwpLeosMcastConfigState_Object=MibScalar
wwpLeosMcastConfigState=_WwpLeosMcastConfigState_Object((1,3,6,1,4,1,6141,2,60,7,1,1,1),_WwpLeosMcastConfigState_Type())
wwpLeosMcastConfigState.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosMcastConfigState.setStatus(_A)
_WwpLeosMcastFilterActivationTable_Object=MibTable
wwpLeosMcastFilterActivationTable=_WwpLeosMcastFilterActivationTable_Object((1,3,6,1,4,1,6141,2,60,7,1,1,2))
if mibBuilder.loadTexts:wwpLeosMcastFilterActivationTable.setStatus(_A)
_WwpLeosMcastFilterActivationEntry_Object=MibTableRow
wwpLeosMcastFilterActivationEntry=_WwpLeosMcastFilterActivationEntry_Object((1,3,6,1,4,1,6141,2,60,7,1,1,2,1))
wwpLeosMcastFilterActivationEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:wwpLeosMcastFilterActivationEntry.setStatus(_A)
_WwpLeosMcastVlanId_Type=VlanId
_WwpLeosMcastVlanId_Object=MibTableColumn
wwpLeosMcastVlanId=_WwpLeosMcastVlanId_Object((1,3,6,1,4,1,6141,2,60,7,1,1,2,1,1),_WwpLeosMcastVlanId_Type())
wwpLeosMcastVlanId.setMaxAccess(_D)
if mibBuilder.loadTexts:wwpLeosMcastVlanId.setStatus(_A)
class _WwpLeosMcastFilterAdminState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_L,1),(_M,2)))
_WwpLeosMcastFilterAdminState_Type.__name__=_B
_WwpLeosMcastFilterAdminState_Object=MibTableColumn
wwpLeosMcastFilterAdminState=_WwpLeosMcastFilterAdminState_Object((1,3,6,1,4,1,6141,2,60,7,1,1,2,1,2),_WwpLeosMcastFilterAdminState_Type())
wwpLeosMcastFilterAdminState.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosMcastFilterAdminState.setStatus(_A)
class _WwpLeosMcastFilterOperState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_L,1),(_M,2)))
_WwpLeosMcastFilterOperState_Type.__name__=_B
_WwpLeosMcastFilterOperState_Object=MibTableColumn
wwpLeosMcastFilterOperState=_WwpLeosMcastFilterOperState_Object((1,3,6,1,4,1,6141,2,60,7,1,1,2,1,3),_WwpLeosMcastFilterOperState_Type())
wwpLeosMcastFilterOperState.setMaxAccess(_D)
if mibBuilder.loadTexts:wwpLeosMcastFilterOperState.setStatus(_A)
_WwpLeosMcastFilterState_Type=RowStatus
_WwpLeosMcastFilterState_Object=MibTableColumn
wwpLeosMcastFilterState=_WwpLeosMcastFilterState_Object((1,3,6,1,4,1,6141,2,60,7,1,1,2,1,4),_WwpLeosMcastFilterState_Type())
wwpLeosMcastFilterState.setMaxAccess(_K)
if mibBuilder.loadTexts:wwpLeosMcastFilterState.setStatus(_A)
_WwpLeosMcastFilterServerPortTable_Object=MibTable
wwpLeosMcastFilterServerPortTable=_WwpLeosMcastFilterServerPortTable_Object((1,3,6,1,4,1,6141,2,60,7,1,1,3))
if mibBuilder.loadTexts:wwpLeosMcastFilterServerPortTable.setStatus(_A)
_WwpLeosMcastFilterServerPortEntry_Object=MibTableRow
wwpLeosMcastFilterServerPortEntry=_WwpLeosMcastFilterServerPortEntry_Object((1,3,6,1,4,1,6141,2,60,7,1,1,3,1))
wwpLeosMcastFilterServerPortEntry.setIndexNames((0,_E,_F),(0,_E,_O))
if mibBuilder.loadTexts:wwpLeosMcastFilterServerPortEntry.setStatus(_A)
class _WwpLeosMcastServerPortId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_WwpLeosMcastServerPortId_Type.__name__=_B
_WwpLeosMcastServerPortId_Object=MibTableColumn
wwpLeosMcastServerPortId=_WwpLeosMcastServerPortId_Object((1,3,6,1,4,1,6141,2,60,7,1,1,3,1,1),_WwpLeosMcastServerPortId_Type())
wwpLeosMcastServerPortId.setMaxAccess(_D)
if mibBuilder.loadTexts:wwpLeosMcastServerPortId.setStatus(_A)
_WwpLeosMcastServerPortStatus_Type=RowStatus
_WwpLeosMcastServerPortStatus_Object=MibTableColumn
wwpLeosMcastServerPortStatus=_WwpLeosMcastServerPortStatus_Object((1,3,6,1,4,1,6141,2,60,7,1,1,3,1,2),_WwpLeosMcastServerPortStatus_Type())
wwpLeosMcastServerPortStatus.setMaxAccess(_K)
if mibBuilder.loadTexts:wwpLeosMcastServerPortStatus.setStatus(_A)
_WwpLeosMcastIgmpSnoopTable_Object=MibTable
wwpLeosMcastIgmpSnoopTable=_WwpLeosMcastIgmpSnoopTable_Object((1,3,6,1,4,1,6141,2,60,7,1,1,4))
if mibBuilder.loadTexts:wwpLeosMcastIgmpSnoopTable.setStatus(_A)
_WwpLeosMcastIgmpSnoopEntry_Object=MibTableRow
wwpLeosMcastIgmpSnoopEntry=_WwpLeosMcastIgmpSnoopEntry_Object((1,3,6,1,4,1,6141,2,60,7,1,1,4,1))
wwpLeosMcastIgmpSnoopEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:wwpLeosMcastIgmpSnoopEntry.setStatus(_A)
class _WwpLeosMcastIgmpSnoopEnable_Type(TruthValue):defaultValue=2
_WwpLeosMcastIgmpSnoopEnable_Type.__name__=_J
_WwpLeosMcastIgmpSnoopEnable_Object=MibTableColumn
wwpLeosMcastIgmpSnoopEnable=_WwpLeosMcastIgmpSnoopEnable_Object((1,3,6,1,4,1,6141,2,60,7,1,1,4,1,1),_WwpLeosMcastIgmpSnoopEnable_Type())
wwpLeosMcastIgmpSnoopEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosMcastIgmpSnoopEnable.setStatus(_A)
class _WwpLeosMcastIgmpSnoopRobustness_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2))
_WwpLeosMcastIgmpSnoopRobustness_Type.__name__=_B
_WwpLeosMcastIgmpSnoopRobustness_Object=MibTableColumn
wwpLeosMcastIgmpSnoopRobustness=_WwpLeosMcastIgmpSnoopRobustness_Object((1,3,6,1,4,1,6141,2,60,7,1,1,4,1,2),_WwpLeosMcastIgmpSnoopRobustness_Type())
wwpLeosMcastIgmpSnoopRobustness.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosMcastIgmpSnoopRobustness.setStatus(_A)
class _WwpLeosMcastIgmpSnoopProxyQueryInterval_Type(Integer32):defaultValue=125;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(10,999999))
_WwpLeosMcastIgmpSnoopProxyQueryInterval_Type.__name__=_B
_WwpLeosMcastIgmpSnoopProxyQueryInterval_Object=MibTableColumn
wwpLeosMcastIgmpSnoopProxyQueryInterval=_WwpLeosMcastIgmpSnoopProxyQueryInterval_Object((1,3,6,1,4,1,6141,2,60,7,1,1,4,1,3),_WwpLeosMcastIgmpSnoopProxyQueryInterval_Type())
wwpLeosMcastIgmpSnoopProxyQueryInterval.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosMcastIgmpSnoopProxyQueryInterval.setStatus(_A)
if mibBuilder.loadTexts:wwpLeosMcastIgmpSnoopProxyQueryInterval.setUnits(_I)
class _WwpLeosMcastIgmpSnoopProxyQueryReplyTmo_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(10,255))
_WwpLeosMcastIgmpSnoopProxyQueryReplyTmo_Type.__name__=_B
_WwpLeosMcastIgmpSnoopProxyQueryReplyTmo_Object=MibTableColumn
wwpLeosMcastIgmpSnoopProxyQueryReplyTmo=_WwpLeosMcastIgmpSnoopProxyQueryReplyTmo_Object((1,3,6,1,4,1,6141,2,60,7,1,1,4,1,4),_WwpLeosMcastIgmpSnoopProxyQueryReplyTmo_Type())
wwpLeosMcastIgmpSnoopProxyQueryReplyTmo.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosMcastIgmpSnoopProxyQueryReplyTmo.setStatus(_A)
if mibBuilder.loadTexts:wwpLeosMcastIgmpSnoopProxyQueryReplyTmo.setUnits(_I)
class _WwpLeosMcastIgmpSnoopProxyQueryDelay_Type(Integer32):defaultValue=50;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,100))
_WwpLeosMcastIgmpSnoopProxyQueryDelay_Type.__name__=_B
_WwpLeosMcastIgmpSnoopProxyQueryDelay_Object=MibTableColumn
wwpLeosMcastIgmpSnoopProxyQueryDelay=_WwpLeosMcastIgmpSnoopProxyQueryDelay_Object((1,3,6,1,4,1,6141,2,60,7,1,1,4,1,5),_WwpLeosMcastIgmpSnoopProxyQueryDelay_Type())
wwpLeosMcastIgmpSnoopProxyQueryDelay.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosMcastIgmpSnoopProxyQueryDelay.setStatus(_A)
if mibBuilder.loadTexts:wwpLeosMcastIgmpSnoopProxyQueryDelay.setUnits(_I)
class _WwpLeosMcastIgmpSnoopLingerTmo_Type(Integer32):defaultValue=125;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(10,300))
_WwpLeosMcastIgmpSnoopLingerTmo_Type.__name__=_B
_WwpLeosMcastIgmpSnoopLingerTmo_Object=MibTableColumn
wwpLeosMcastIgmpSnoopLingerTmo=_WwpLeosMcastIgmpSnoopLingerTmo_Object((1,3,6,1,4,1,6141,2,60,7,1,1,4,1,6),_WwpLeosMcastIgmpSnoopLingerTmo_Type())
wwpLeosMcastIgmpSnoopLingerTmo.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosMcastIgmpSnoopLingerTmo.setStatus(_A)
if mibBuilder.loadTexts:wwpLeosMcastIgmpSnoopLingerTmo.setUnits(_I)
class _WwpLeosMcastIgmpQueryEngineState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_P,1),(_Q,2)))
_WwpLeosMcastIgmpQueryEngineState_Type.__name__=_B
_WwpLeosMcastIgmpQueryEngineState_Object=MibTableColumn
wwpLeosMcastIgmpQueryEngineState=_WwpLeosMcastIgmpQueryEngineState_Object((1,3,6,1,4,1,6141,2,60,7,1,1,4,1,7),_WwpLeosMcastIgmpQueryEngineState_Type())
wwpLeosMcastIgmpQueryEngineState.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosMcastIgmpQueryEngineState.setStatus(_A)
_WwpLeosMcastIgmpProxyQuerySrcIp_Type=IpAddress
_WwpLeosMcastIgmpProxyQuerySrcIp_Object=MibTableColumn
wwpLeosMcastIgmpProxyQuerySrcIp=_WwpLeosMcastIgmpProxyQuerySrcIp_Object((1,3,6,1,4,1,6141,2,60,7,1,1,4,1,8),_WwpLeosMcastIgmpProxyQuerySrcIp_Type())
wwpLeosMcastIgmpProxyQuerySrcIp.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosMcastIgmpProxyQuerySrcIp.setStatus(_A)
class _WwpLeosMcastIgmpRouterQueryInterval_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(10,999999))
_WwpLeosMcastIgmpRouterQueryInterval_Type.__name__=_B
_WwpLeosMcastIgmpRouterQueryInterval_Object=MibTableColumn
wwpLeosMcastIgmpRouterQueryInterval=_WwpLeosMcastIgmpRouterQueryInterval_Object((1,3,6,1,4,1,6141,2,60,7,1,1,4,1,9),_WwpLeosMcastIgmpRouterQueryInterval_Type())
wwpLeosMcastIgmpRouterQueryInterval.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosMcastIgmpRouterQueryInterval.setStatus(_A)
class _WwpLeosMcastIgmpMinResponseTime_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(50,600))
_WwpLeosMcastIgmpMinResponseTime_Type.__name__=_B
_WwpLeosMcastIgmpMinResponseTime_Object=MibTableColumn
wwpLeosMcastIgmpMinResponseTime=_WwpLeosMcastIgmpMinResponseTime_Object((1,3,6,1,4,1,6141,2,60,7,1,1,4,1,10),_WwpLeosMcastIgmpMinResponseTime_Type())
wwpLeosMcastIgmpMinResponseTime.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosMcastIgmpMinResponseTime.setStatus(_A)
class _WwpLeosMcastIgmpDefaultRouterPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_WwpLeosMcastIgmpDefaultRouterPort_Type.__name__=_B
_WwpLeosMcastIgmpDefaultRouterPort_Object=MibTableColumn
wwpLeosMcastIgmpDefaultRouterPort=_WwpLeosMcastIgmpDefaultRouterPort_Object((1,3,6,1,4,1,6141,2,60,7,1,1,4,1,11),_WwpLeosMcastIgmpDefaultRouterPort_Type())
wwpLeosMcastIgmpDefaultRouterPort.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosMcastIgmpDefaultRouterPort.setStatus(_A)
class _WwpLeosMcastIgmpInquisitiveLeaveState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_P,1),(_Q,2)))
_WwpLeosMcastIgmpInquisitiveLeaveState_Type.__name__=_B
_WwpLeosMcastIgmpInquisitiveLeaveState_Object=MibTableColumn
wwpLeosMcastIgmpInquisitiveLeaveState=_WwpLeosMcastIgmpInquisitiveLeaveState_Object((1,3,6,1,4,1,6141,2,60,7,1,1,4,1,12),_WwpLeosMcastIgmpInquisitiveLeaveState_Type())
wwpLeosMcastIgmpInquisitiveLeaveState.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosMcastIgmpInquisitiveLeaveState.setStatus(_A)
class _WwpLeosMcastIgmpLastMemberQueryInterval_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(10,100))
_WwpLeosMcastIgmpLastMemberQueryInterval_Type.__name__=_B
_WwpLeosMcastIgmpLastMemberQueryInterval_Object=MibTableColumn
wwpLeosMcastIgmpLastMemberQueryInterval=_WwpLeosMcastIgmpLastMemberQueryInterval_Object((1,3,6,1,4,1,6141,2,60,7,1,1,4,1,13),_WwpLeosMcastIgmpLastMemberQueryInterval_Type())
wwpLeosMcastIgmpLastMemberQueryInterval.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosMcastIgmpLastMemberQueryInterval.setStatus(_A)
class _WwpLeosMcastIgmpPriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_WwpLeosMcastIgmpPriority_Type.__name__=_B
_WwpLeosMcastIgmpPriority_Object=MibTableColumn
wwpLeosMcastIgmpPriority=_WwpLeosMcastIgmpPriority_Object((1,3,6,1,4,1,6141,2,60,7,1,1,4,1,14),_WwpLeosMcastIgmpPriority_Type())
wwpLeosMcastIgmpPriority.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosMcastIgmpPriority.setStatus(_A)
_WwpLeosMcastIgmpSnoopRouterRangeStartIpAddr_Type=IpAddress
_WwpLeosMcastIgmpSnoopRouterRangeStartIpAddr_Object=MibTableColumn
wwpLeosMcastIgmpSnoopRouterRangeStartIpAddr=_WwpLeosMcastIgmpSnoopRouterRangeStartIpAddr_Object((1,3,6,1,4,1,6141,2,60,7,1,1,4,1,15),_WwpLeosMcastIgmpSnoopRouterRangeStartIpAddr_Type())
wwpLeosMcastIgmpSnoopRouterRangeStartIpAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosMcastIgmpSnoopRouterRangeStartIpAddr.setStatus(_A)
_WwpLeosMcastIgmpSnoopRouterRangeEndIpAddr_Type=IpAddress
_WwpLeosMcastIgmpSnoopRouterRangeEndIpAddr_Object=MibTableColumn
wwpLeosMcastIgmpSnoopRouterRangeEndIpAddr=_WwpLeosMcastIgmpSnoopRouterRangeEndIpAddr_Object((1,3,6,1,4,1,6141,2,60,7,1,1,4,1,16),_WwpLeosMcastIgmpSnoopRouterRangeEndIpAddr_Type())
wwpLeosMcastIgmpSnoopRouterRangeEndIpAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosMcastIgmpSnoopRouterRangeEndIpAddr.setStatus(_A)
class _WwpLeosMcastIgmpSnoopActiveLingerTimeout_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,300))
_WwpLeosMcastIgmpSnoopActiveLingerTimeout_Type.__name__=_B
_WwpLeosMcastIgmpSnoopActiveLingerTimeout_Object=MibTableColumn
wwpLeosMcastIgmpSnoopActiveLingerTimeout=_WwpLeosMcastIgmpSnoopActiveLingerTimeout_Object((1,3,6,1,4,1,6141,2,60,7,1,1,4,1,17),_WwpLeosMcastIgmpSnoopActiveLingerTimeout_Type())
wwpLeosMcastIgmpSnoopActiveLingerTimeout.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosMcastIgmpSnoopActiveLingerTimeout.setStatus(_A)
if mibBuilder.loadTexts:wwpLeosMcastIgmpSnoopActiveLingerTimeout.setUnits(_I)
class _WwpLeosMcastIgmpSnoopServerTopology_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('centralized',1),('distributed',2)))
_WwpLeosMcastIgmpSnoopServerTopology_Type.__name__=_B
_WwpLeosMcastIgmpSnoopServerTopology_Object=MibTableColumn
wwpLeosMcastIgmpSnoopServerTopology=_WwpLeosMcastIgmpSnoopServerTopology_Object((1,3,6,1,4,1,6141,2,60,7,1,1,4,1,18),_WwpLeosMcastIgmpSnoopServerTopology_Type())
wwpLeosMcastIgmpSnoopServerTopology.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosMcastIgmpSnoopServerTopology.setStatus(_A)
class _WwpLeosMcastIgmpSnoopRapidRecoveryMode_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('on',1),('off',2)))
_WwpLeosMcastIgmpSnoopRapidRecoveryMode_Type.__name__=_B
_WwpLeosMcastIgmpSnoopRapidRecoveryMode_Object=MibTableColumn
wwpLeosMcastIgmpSnoopRapidRecoveryMode=_WwpLeosMcastIgmpSnoopRapidRecoveryMode_Object((1,3,6,1,4,1,6141,2,60,7,1,1,4,1,19),_WwpLeosMcastIgmpSnoopRapidRecoveryMode_Type())
wwpLeosMcastIgmpSnoopRapidRecoveryMode.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosMcastIgmpSnoopRapidRecoveryMode.setStatus(_A)
_WwpLeosMcastChannelStreamTable_Object=MibTable
wwpLeosMcastChannelStreamTable=_WwpLeosMcastChannelStreamTable_Object((1,3,6,1,4,1,6141,2,60,7,1,1,5))
if mibBuilder.loadTexts:wwpLeosMcastChannelStreamTable.setStatus(_A)
_WwpLeosMcastChannelStreamEntry_Object=MibTableRow
wwpLeosMcastChannelStreamEntry=_WwpLeosMcastChannelStreamEntry_Object((1,3,6,1,4,1,6141,2,60,7,1,1,5,1))
wwpLeosMcastChannelStreamEntry.setIndexNames((0,_E,_F),(0,_E,_R))
if mibBuilder.loadTexts:wwpLeosMcastChannelStreamEntry.setStatus(_A)
_WwpLeosMcastChanelStreamStartGroupAddr_Type=IpAddress
_WwpLeosMcastChanelStreamStartGroupAddr_Object=MibTableColumn
wwpLeosMcastChanelStreamStartGroupAddr=_WwpLeosMcastChanelStreamStartGroupAddr_Object((1,3,6,1,4,1,6141,2,60,7,1,1,5,1,1),_WwpLeosMcastChanelStreamStartGroupAddr_Type())
wwpLeosMcastChanelStreamStartGroupAddr.setMaxAccess(_D)
if mibBuilder.loadTexts:wwpLeosMcastChanelStreamStartGroupAddr.setStatus(_A)
_WwpLeosMcastChanelStreamEndGroupAddr_Type=IpAddress
_WwpLeosMcastChanelStreamEndGroupAddr_Object=MibTableColumn
wwpLeosMcastChanelStreamEndGroupAddr=_WwpLeosMcastChanelStreamEndGroupAddr_Object((1,3,6,1,4,1,6141,2,60,7,1,1,5,1,2),_WwpLeosMcastChanelStreamEndGroupAddr_Type())
wwpLeosMcastChanelStreamEndGroupAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosMcastChanelStreamEndGroupAddr.setStatus(_A)
_WwpLeosMcastChannelStreamStatus_Type=RowStatus
_WwpLeosMcastChannelStreamStatus_Object=MibTableColumn
wwpLeosMcastChannelStreamStatus=_WwpLeosMcastChannelStreamStatus_Object((1,3,6,1,4,1,6141,2,60,7,1,1,5,1,3),_WwpLeosMcastChannelStreamStatus_Type())
wwpLeosMcastChannelStreamStatus.setMaxAccess(_K)
if mibBuilder.loadTexts:wwpLeosMcastChannelStreamStatus.setStatus(_A)
_WwpLeosMcastFilterConfigTable_Object=MibTable
wwpLeosMcastFilterConfigTable=_WwpLeosMcastFilterConfigTable_Object((1,3,6,1,4,1,6141,2,60,7,1,1,6))
if mibBuilder.loadTexts:wwpLeosMcastFilterConfigTable.setStatus(_A)
_WwpLeosMcastFilterConfigEntry_Object=MibTableRow
wwpLeosMcastFilterConfigEntry=_WwpLeosMcastFilterConfigEntry_Object((1,3,6,1,4,1,6141,2,60,7,1,1,6,1))
wwpLeosMcastFilterConfigEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:wwpLeosMcastFilterConfigEntry.setStatus(_A)
class _WwpLeosMcastFilterUPFActivate_Type(TruthValue):defaultValue=2
_WwpLeosMcastFilterUPFActivate_Type.__name__=_J
_WwpLeosMcastFilterUPFActivate_Object=MibTableColumn
wwpLeosMcastFilterUPFActivate=_WwpLeosMcastFilterUPFActivate_Object((1,3,6,1,4,1,6141,2,60,7,1,1,6,1,1),_WwpLeosMcastFilterUPFActivate_Type())
wwpLeosMcastFilterUPFActivate.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosMcastFilterUPFActivate.setStatus(_A)
class _WwpLeosMcastUnresolvedAction_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_WwpLeosMcastUnresolvedAction_Type.__name__=_B
_WwpLeosMcastUnresolvedAction_Object=MibTableColumn
wwpLeosMcastUnresolvedAction=_WwpLeosMcastUnresolvedAction_Object((1,3,6,1,4,1,6141,2,60,7,1,1,6,1,2),_WwpLeosMcastUnresolvedAction_Type())
wwpLeosMcastUnresolvedAction.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosMcastUnresolvedAction.setStatus(_A)
class _WwpLeosMcastFilterWKMFLocalActivate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_WwpLeosMcastFilterWKMFLocalActivate_Type.__name__=_B
_WwpLeosMcastFilterWKMFLocalActivate_Object=MibTableColumn
wwpLeosMcastFilterWKMFLocalActivate=_WwpLeosMcastFilterWKMFLocalActivate_Object((1,3,6,1,4,1,6141,2,60,7,1,1,6,1,3),_WwpLeosMcastFilterWKMFLocalActivate_Type())
wwpLeosMcastFilterWKMFLocalActivate.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosMcastFilterWKMFLocalActivate.setStatus(_A)
class _WwpLeosMcastFilterWKMFInternetActivate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_WwpLeosMcastFilterWKMFInternetActivate_Type.__name__=_B
_WwpLeosMcastFilterWKMFInternetActivate_Object=MibTableColumn
wwpLeosMcastFilterWKMFInternetActivate=_WwpLeosMcastFilterWKMFInternetActivate_Object((1,3,6,1,4,1,6141,2,60,7,1,1,6,1,4),_WwpLeosMcastFilterWKMFInternetActivate_Type())
wwpLeosMcastFilterWKMFInternetActivate.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosMcastFilterWKMFInternetActivate.setStatus(_A)
class _WwpLeosMcastFilterWKMFAdhocActivate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_WwpLeosMcastFilterWKMFAdhocActivate_Type.__name__=_B
_WwpLeosMcastFilterWKMFAdhocActivate_Object=MibTableColumn
wwpLeosMcastFilterWKMFAdhocActivate=_WwpLeosMcastFilterWKMFAdhocActivate_Object((1,3,6,1,4,1,6141,2,60,7,1,1,6,1,5),_WwpLeosMcastFilterWKMFAdhocActivate_Type())
wwpLeosMcastFilterWKMFAdhocActivate.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosMcastFilterWKMFAdhocActivate.setStatus(_A)
class _WwpLeosMcastFilterWKMFStMulticastActivate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_WwpLeosMcastFilterWKMFStMulticastActivate_Type.__name__=_B
_WwpLeosMcastFilterWKMFStMulticastActivate_Object=MibTableColumn
wwpLeosMcastFilterWKMFStMulticastActivate=_WwpLeosMcastFilterWKMFStMulticastActivate_Object((1,3,6,1,4,1,6141,2,60,7,1,1,6,1,6),_WwpLeosMcastFilterWKMFStMulticastActivate_Type())
wwpLeosMcastFilterWKMFStMulticastActivate.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosMcastFilterWKMFStMulticastActivate.setStatus(_A)
class _WwpLeosMcastFilterWKMFSdpSapActivate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_WwpLeosMcastFilterWKMFSdpSapActivate_Type.__name__=_B
_WwpLeosMcastFilterWKMFSdpSapActivate_Object=MibTableColumn
wwpLeosMcastFilterWKMFSdpSapActivate=_WwpLeosMcastFilterWKMFSdpSapActivate_Object((1,3,6,1,4,1,6141,2,60,7,1,1,6,1,7),_WwpLeosMcastFilterWKMFSdpSapActivate_Type())
wwpLeosMcastFilterWKMFSdpSapActivate.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosMcastFilterWKMFSdpSapActivate.setStatus(_A)
_WwpLeosMcastChannelStreamExPortMemTable_Object=MibTable
wwpLeosMcastChannelStreamExPortMemTable=_WwpLeosMcastChannelStreamExPortMemTable_Object((1,3,6,1,4,1,6141,2,60,7,1,1,7))
if mibBuilder.loadTexts:wwpLeosMcastChannelStreamExPortMemTable.setStatus(_A)
_WwpLeosMcastChannelStreamExPortMemEntry_Object=MibTableRow
wwpLeosMcastChannelStreamExPortMemEntry=_WwpLeosMcastChannelStreamExPortMemEntry_Object((1,3,6,1,4,1,6141,2,60,7,1,1,7,1))
wwpLeosMcastChannelStreamExPortMemEntry.setIndexNames((0,_E,_F),(0,_E,_S))
if mibBuilder.loadTexts:wwpLeosMcastChannelStreamExPortMemEntry.setStatus(_A)
class _WwpLeosMcastChannelStreamExPortId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_WwpLeosMcastChannelStreamExPortId_Type.__name__=_B
_WwpLeosMcastChannelStreamExPortId_Object=MibTableColumn
wwpLeosMcastChannelStreamExPortId=_WwpLeosMcastChannelStreamExPortId_Object((1,3,6,1,4,1,6141,2,60,7,1,1,7,1,1),_WwpLeosMcastChannelStreamExPortId_Type())
wwpLeosMcastChannelStreamExPortId.setMaxAccess(_D)
if mibBuilder.loadTexts:wwpLeosMcastChannelStreamExPortId.setStatus(_A)
_WwpLeosMcastChannelStreamExPortMemStatus_Type=RowStatus
_WwpLeosMcastChannelStreamExPortMemStatus_Object=MibTableColumn
wwpLeosMcastChannelStreamExPortMemStatus=_WwpLeosMcastChannelStreamExPortMemStatus_Object((1,3,6,1,4,1,6141,2,60,7,1,1,7,1,2),_WwpLeosMcastChannelStreamExPortMemStatus_Type())
wwpLeosMcastChannelStreamExPortMemStatus.setMaxAccess(_K)
if mibBuilder.loadTexts:wwpLeosMcastChannelStreamExPortMemStatus.setStatus(_A)
class _WwpLeosMcastSnoopState_Type(TruthValue):defaultValue=2
_WwpLeosMcastSnoopState_Type.__name__=_J
_WwpLeosMcastSnoopState_Object=MibScalar
wwpLeosMcastSnoopState=_WwpLeosMcastSnoopState_Object((1,3,6,1,4,1,6141,2,60,7,1,1,8),_WwpLeosMcastSnoopState_Type())
wwpLeosMcastSnoopState.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosMcastSnoopState.setStatus(_A)
class _WwpLeosMcastGlobalStatsClear_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('clear',1),('none',2)))
_WwpLeosMcastGlobalStatsClear_Type.__name__=_B
_WwpLeosMcastGlobalStatsClear_Object=MibScalar
wwpLeosMcastGlobalStatsClear=_WwpLeosMcastGlobalStatsClear_Object((1,3,6,1,4,1,6141,2,60,7,1,1,10),_WwpLeosMcastGlobalStatsClear_Type())
wwpLeosMcastGlobalStatsClear.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosMcastGlobalStatsClear.setStatus(_A)
_WwpLeosMcastFilterStatus_ObjectIdentity=ObjectIdentity
wwpLeosMcastFilterStatus=_WwpLeosMcastFilterStatus_ObjectIdentity((1,3,6,1,4,1,6141,2,60,7,1,2))
_WwpLeosMcastGroupTable_Object=MibTable
wwpLeosMcastGroupTable=_WwpLeosMcastGroupTable_Object((1,3,6,1,4,1,6141,2,60,7,1,2,1))
if mibBuilder.loadTexts:wwpLeosMcastGroupTable.setStatus(_A)
_WwpLeosMcastGroupEntry_Object=MibTableRow
wwpLeosMcastGroupEntry=_WwpLeosMcastGroupEntry_Object((1,3,6,1,4,1,6141,2,60,7,1,2,1,1))
wwpLeosMcastGroupEntry.setIndexNames((0,_E,_F),(0,_E,_N))
if mibBuilder.loadTexts:wwpLeosMcastGroupEntry.setStatus(_A)
_WwpLeosMcastGroupAddr_Type=IpAddress
_WwpLeosMcastGroupAddr_Object=MibTableColumn
wwpLeosMcastGroupAddr=_WwpLeosMcastGroupAddr_Object((1,3,6,1,4,1,6141,2,60,7,1,2,1,1,1),_WwpLeosMcastGroupAddr_Type())
wwpLeosMcastGroupAddr.setMaxAccess(_D)
if mibBuilder.loadTexts:wwpLeosMcastGroupAddr.setStatus(_A)
class _WwpLeosMcastState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('active',1),('query',2),('linger',3)))
_WwpLeosMcastState_Type.__name__=_B
_WwpLeosMcastState_Object=MibTableColumn
wwpLeosMcastState=_WwpLeosMcastState_Object((1,3,6,1,4,1,6141,2,60,7,1,2,1,1,2),_WwpLeosMcastState_Type())
wwpLeosMcastState.setMaxAccess(_D)
if mibBuilder.loadTexts:wwpLeosMcastState.setStatus(_A)
class _WwpLeosMcastType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('static',1),('dynamic',2)))
_WwpLeosMcastType_Type.__name__=_B
_WwpLeosMcastType_Object=MibTableColumn
wwpLeosMcastType=_WwpLeosMcastType_Object((1,3,6,1,4,1,6141,2,60,7,1,2,1,1,3),_WwpLeosMcastType_Type())
wwpLeosMcastType.setMaxAccess(_D)
if mibBuilder.loadTexts:wwpLeosMcastType.setStatus(_A)
class _WwpLeosMcastSource_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('router',1),('server',2)))
_WwpLeosMcastSource_Type.__name__=_B
_WwpLeosMcastSource_Object=MibTableColumn
wwpLeosMcastSource=_WwpLeosMcastSource_Object((1,3,6,1,4,1,6141,2,60,7,1,2,1,1,4),_WwpLeosMcastSource_Type())
wwpLeosMcastSource.setMaxAccess(_D)
if mibBuilder.loadTexts:wwpLeosMcastSource.setStatus(_A)
_WwpLeosMcastMemberCount_Type=Counter32
_WwpLeosMcastMemberCount_Object=MibTableColumn
wwpLeosMcastMemberCount=_WwpLeosMcastMemberCount_Object((1,3,6,1,4,1,6141,2,60,7,1,2,1,1,5),_WwpLeosMcastMemberCount_Type())
wwpLeosMcastMemberCount.setMaxAccess(_D)
if mibBuilder.loadTexts:wwpLeosMcastMemberCount.setStatus(_A)
_WwpLeosMcastGroupMemberTable_Object=MibTable
wwpLeosMcastGroupMemberTable=_WwpLeosMcastGroupMemberTable_Object((1,3,6,1,4,1,6141,2,60,7,1,2,2))
if mibBuilder.loadTexts:wwpLeosMcastGroupMemberTable.setStatus(_A)
_WwpLeosMcastGroupMemberEntry_Object=MibTableRow
wwpLeosMcastGroupMemberEntry=_WwpLeosMcastGroupMemberEntry_Object((1,3,6,1,4,1,6141,2,60,7,1,2,2,1))
wwpLeosMcastGroupMemberEntry.setIndexNames((0,_E,_F),(0,_E,_N),(0,_E,_T))
if mibBuilder.loadTexts:wwpLeosMcastGroupMemberEntry.setStatus(_A)
class _WwpLeosMcastPortId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_WwpLeosMcastPortId_Type.__name__=_B
_WwpLeosMcastPortId_Object=MibTableColumn
wwpLeosMcastPortId=_WwpLeosMcastPortId_Object((1,3,6,1,4,1,6141,2,60,7,1,2,2,1,1),_WwpLeosMcastPortId_Type())
wwpLeosMcastPortId.setMaxAccess(_D)
if mibBuilder.loadTexts:wwpLeosMcastPortId.setStatus(_A)
class _WwpLeosMcastPortTagId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094))
_WwpLeosMcastPortTagId_Type.__name__=_B
_WwpLeosMcastPortTagId_Object=MibTableColumn
wwpLeosMcastPortTagId=_WwpLeosMcastPortTagId_Object((1,3,6,1,4,1,6141,2,60,7,1,2,2,1,2),_WwpLeosMcastPortTagId_Type())
wwpLeosMcastPortTagId.setMaxAccess(_D)
if mibBuilder.loadTexts:wwpLeosMcastPortTagId.setStatus(_A)
_WwpLeosMcastFilterStats_ObjectIdentity=ObjectIdentity
wwpLeosMcastFilterStats=_WwpLeosMcastFilterStats_ObjectIdentity((1,3,6,1,4,1,6141,2,60,7,1,3))
_WwpLeosMcastFilterStatsTable_Object=MibTable
wwpLeosMcastFilterStatsTable=_WwpLeosMcastFilterStatsTable_Object((1,3,6,1,4,1,6141,2,60,7,1,3,1))
if mibBuilder.loadTexts:wwpLeosMcastFilterStatsTable.setStatus(_A)
_WwpLeosMcastFilterStatsEntry_Object=MibTableRow
wwpLeosMcastFilterStatsEntry=_WwpLeosMcastFilterStatsEntry_Object((1,3,6,1,4,1,6141,2,60,7,1,3,1,1))
wwpLeosMcastFilterStatsEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:wwpLeosMcastFilterStatsEntry.setStatus(_A)
class _WwpLeosMcastStaticGrpCount_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_WwpLeosMcastStaticGrpCount_Type.__name__=_B
_WwpLeosMcastStaticGrpCount_Object=MibTableColumn
wwpLeosMcastStaticGrpCount=_WwpLeosMcastStaticGrpCount_Object((1,3,6,1,4,1,6141,2,60,7,1,3,1,1,1),_WwpLeosMcastStaticGrpCount_Type())
wwpLeosMcastStaticGrpCount.setMaxAccess(_D)
if mibBuilder.loadTexts:wwpLeosMcastStaticGrpCount.setStatus(_A)
class _WwpLeosMcastDynamicGrpCount_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_WwpLeosMcastDynamicGrpCount_Type.__name__=_B
_WwpLeosMcastDynamicGrpCount_Object=MibTableColumn
wwpLeosMcastDynamicGrpCount=_WwpLeosMcastDynamicGrpCount_Object((1,3,6,1,4,1,6141,2,60,7,1,3,1,1,2),_WwpLeosMcastDynamicGrpCount_Type())
wwpLeosMcastDynamicGrpCount.setMaxAccess(_D)
if mibBuilder.loadTexts:wwpLeosMcastDynamicGrpCount.setStatus(_A)
_WwpLeosMcastJoinMessages_Type=Counter32
_WwpLeosMcastJoinMessages_Object=MibTableColumn
wwpLeosMcastJoinMessages=_WwpLeosMcastJoinMessages_Object((1,3,6,1,4,1,6141,2,60,7,1,3,1,1,3),_WwpLeosMcastJoinMessages_Type())
wwpLeosMcastJoinMessages.setMaxAccess(_D)
if mibBuilder.loadTexts:wwpLeosMcastJoinMessages.setStatus(_A)
_WwpLeosMcastLeaveMessages_Type=Counter32
_WwpLeosMcastLeaveMessages_Object=MibTableColumn
wwpLeosMcastLeaveMessages=_WwpLeosMcastLeaveMessages_Object((1,3,6,1,4,1,6141,2,60,7,1,3,1,1,4),_WwpLeosMcastLeaveMessages_Type())
wwpLeosMcastLeaveMessages.setMaxAccess(_D)
if mibBuilder.loadTexts:wwpLeosMcastLeaveMessages.setStatus(_A)
_WwpLeosMcastQueryMessages_Type=Counter32
_WwpLeosMcastQueryMessages_Object=MibTableColumn
wwpLeosMcastQueryMessages=_WwpLeosMcastQueryMessages_Object((1,3,6,1,4,1,6141,2,60,7,1,3,1,1,5),_WwpLeosMcastQueryMessages_Type())
wwpLeosMcastQueryMessages.setMaxAccess(_D)
if mibBuilder.loadTexts:wwpLeosMcastQueryMessages.setStatus(_A)
_WwpLeosMcastQueryDiscards_Type=Counter32
_WwpLeosMcastQueryDiscards_Object=MibTableColumn
wwpLeosMcastQueryDiscards=_WwpLeosMcastQueryDiscards_Object((1,3,6,1,4,1,6141,2,60,7,1,3,1,1,6),_WwpLeosMcastQueryDiscards_Type())
wwpLeosMcastQueryDiscards.setMaxAccess(_D)
if mibBuilder.loadTexts:wwpLeosMcastQueryDiscards.setStatus(_A)
_WwpLeosMcastQueryTimeouts_Type=Counter32
_WwpLeosMcastQueryTimeouts_Object=MibTableColumn
wwpLeosMcastQueryTimeouts=_WwpLeosMcastQueryTimeouts_Object((1,3,6,1,4,1,6141,2,60,7,1,3,1,1,7),_WwpLeosMcastQueryTimeouts_Type())
wwpLeosMcastQueryTimeouts.setMaxAccess(_D)
if mibBuilder.loadTexts:wwpLeosMcastQueryTimeouts.setStatus(_A)
_WwpLeosMcastUnknownPktType_Type=Counter32
_WwpLeosMcastUnknownPktType_Object=MibTableColumn
wwpLeosMcastUnknownPktType=_WwpLeosMcastUnknownPktType_Object((1,3,6,1,4,1,6141,2,60,7,1,3,1,1,8),_WwpLeosMcastUnknownPktType_Type())
wwpLeosMcastUnknownPktType.setMaxAccess(_D)
if mibBuilder.loadTexts:wwpLeosMcastUnknownPktType.setStatus(_A)
_WwpLeosMcastRouterDiscards_Type=Counter32
_WwpLeosMcastRouterDiscards_Object=MibTableColumn
wwpLeosMcastRouterDiscards=_WwpLeosMcastRouterDiscards_Object((1,3,6,1,4,1,6141,2,60,7,1,3,1,1,9),_WwpLeosMcastRouterDiscards_Type())
wwpLeosMcastRouterDiscards.setMaxAccess(_D)
if mibBuilder.loadTexts:wwpLeosMcastRouterDiscards.setStatus(_A)
_WwpLeosMcastHostDiscards_Type=Counter32
_WwpLeosMcastHostDiscards_Object=MibTableColumn
wwpLeosMcastHostDiscards=_WwpLeosMcastHostDiscards_Object((1,3,6,1,4,1,6141,2,60,7,1,3,1,1,10),_WwpLeosMcastHostDiscards_Type())
wwpLeosMcastHostDiscards.setMaxAccess(_D)
if mibBuilder.loadTexts:wwpLeosMcastHostDiscards.setStatus(_A)
_WwpLeosMcastBadChecksum_Type=Counter32
_WwpLeosMcastBadChecksum_Object=MibTableColumn
wwpLeosMcastBadChecksum=_WwpLeosMcastBadChecksum_Object((1,3,6,1,4,1,6141,2,60,7,1,3,1,1,11),_WwpLeosMcastBadChecksum_Type())
wwpLeosMcastBadChecksum.setMaxAccess(_D)
if mibBuilder.loadTexts:wwpLeosMcastBadChecksum.setStatus(_A)
_WwpLeosMcastL2L3Mismatch_Type=Counter32
_WwpLeosMcastL2L3Mismatch_Object=MibTableColumn
wwpLeosMcastL2L3Mismatch=_WwpLeosMcastL2L3Mismatch_Object((1,3,6,1,4,1,6141,2,60,7,1,3,1,1,12),_WwpLeosMcastL2L3Mismatch_Type())
wwpLeosMcastL2L3Mismatch.setMaxAccess(_D)
if mibBuilder.loadTexts:wwpLeosMcastL2L3Mismatch.setStatus(_A)
_WwpLeosMcastTotalMembers_Type=Counter32
_WwpLeosMcastTotalMembers_Object=MibTableColumn
wwpLeosMcastTotalMembers=_WwpLeosMcastTotalMembers_Object((1,3,6,1,4,1,6141,2,60,7,1,3,1,1,13),_WwpLeosMcastTotalMembers_Type())
wwpLeosMcastTotalMembers.setMaxAccess(_D)
if mibBuilder.loadTexts:wwpLeosMcastTotalMembers.setStatus(_A)
_WwpLeosMcastLingerCount_Type=Counter32
_WwpLeosMcastLingerCount_Object=MibTableColumn
wwpLeosMcastLingerCount=_WwpLeosMcastLingerCount_Object((1,3,6,1,4,1,6141,2,60,7,1,3,1,1,14),_WwpLeosMcastLingerCount_Type())
wwpLeosMcastLingerCount.setMaxAccess(_D)
if mibBuilder.loadTexts:wwpLeosMcastLingerCount.setStatus(_A)
_WwpLeosMcastRouterSrcMacAddr_Type=MacAddress
_WwpLeosMcastRouterSrcMacAddr_Object=MibTableColumn
wwpLeosMcastRouterSrcMacAddr=_WwpLeosMcastRouterSrcMacAddr_Object((1,3,6,1,4,1,6141,2,60,7,1,3,1,1,15),_WwpLeosMcastRouterSrcMacAddr_Type())
wwpLeosMcastRouterSrcMacAddr.setMaxAccess(_D)
if mibBuilder.loadTexts:wwpLeosMcastRouterSrcMacAddr.setStatus(_A)
_WwpLeosMcastRouterSrcIpAddr_Type=IpAddress
_WwpLeosMcastRouterSrcIpAddr_Object=MibTableColumn
wwpLeosMcastRouterSrcIpAddr=_WwpLeosMcastRouterSrcIpAddr_Object((1,3,6,1,4,1,6141,2,60,7,1,3,1,1,16),_WwpLeosMcastRouterSrcIpAddr_Type())
wwpLeosMcastRouterSrcIpAddr.setMaxAccess(_D)
if mibBuilder.loadTexts:wwpLeosMcastRouterSrcIpAddr.setStatus(_A)
class _WwpLeosMcastRouterPortId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_WwpLeosMcastRouterPortId_Type.__name__=_B
_WwpLeosMcastRouterPortId_Object=MibTableColumn
wwpLeosMcastRouterPortId=_WwpLeosMcastRouterPortId_Object((1,3,6,1,4,1,6141,2,60,7,1,3,1,1,17),_WwpLeosMcastRouterPortId_Type())
wwpLeosMcastRouterPortId.setMaxAccess(_D)
if mibBuilder.loadTexts:wwpLeosMcastRouterPortId.setStatus(_A)
class _WwpLeosMcastReportSendPortId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_WwpLeosMcastReportSendPortId_Type.__name__=_B
_WwpLeosMcastReportSendPortId_Object=MibTableColumn
wwpLeosMcastReportSendPortId=_WwpLeosMcastReportSendPortId_Object((1,3,6,1,4,1,6141,2,60,7,1,3,1,1,18),_WwpLeosMcastReportSendPortId_Type())
wwpLeosMcastReportSendPortId.setMaxAccess(_D)
if mibBuilder.loadTexts:wwpLeosMcastReportSendPortId.setStatus(_A)
class _WwpLeosMcastStatsClear_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('clear',1),('none',2)))
_WwpLeosMcastStatsClear_Type.__name__=_B
_WwpLeosMcastStatsClear_Object=MibTableColumn
wwpLeosMcastStatsClear=_WwpLeosMcastStatsClear_Object((1,3,6,1,4,1,6141,2,60,7,1,3,1,1,19),_WwpLeosMcastStatsClear_Type())
wwpLeosMcastStatsClear.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosMcastStatsClear.setStatus(_A)
_WwpLeosMcastStatsQuerySrcIpZeroDiscard_Type=Counter32
_WwpLeosMcastStatsQuerySrcIpZeroDiscard_Object=MibTableColumn
wwpLeosMcastStatsQuerySrcIpZeroDiscard=_WwpLeosMcastStatsQuerySrcIpZeroDiscard_Object((1,3,6,1,4,1,6141,2,60,7,1,3,1,1,20),_WwpLeosMcastStatsQuerySrcIpZeroDiscard_Type())
wwpLeosMcastStatsQuerySrcIpZeroDiscard.setMaxAccess(_D)
if mibBuilder.loadTexts:wwpLeosMcastStatsQuerySrcIpZeroDiscard.setStatus(_A)
_WwpLeosMcastFilterMIBNotificationPrefix_ObjectIdentity=ObjectIdentity
wwpLeosMcastFilterMIBNotificationPrefix=_WwpLeosMcastFilterMIBNotificationPrefix_ObjectIdentity((1,3,6,1,4,1,6141,2,60,7,2))
_WwpLeosMcastFilterMIBNotifications_ObjectIdentity=ObjectIdentity
wwpLeosMcastFilterMIBNotifications=_WwpLeosMcastFilterMIBNotifications_ObjectIdentity((1,3,6,1,4,1,6141,2,60,7,2,0))
_WwpLeosMcastFilterMIBConformance_ObjectIdentity=ObjectIdentity
wwpLeosMcastFilterMIBConformance=_WwpLeosMcastFilterMIBConformance_ObjectIdentity((1,3,6,1,4,1,6141,2,60,7,3))
_WwpLeosMcastFilterMIBCompliances_ObjectIdentity=ObjectIdentity
wwpLeosMcastFilterMIBCompliances=_WwpLeosMcastFilterMIBCompliances_ObjectIdentity((1,3,6,1,4,1,6141,2,60,7,3,1))
_WwpLeosMcastFilterMIBGroups_ObjectIdentity=ObjectIdentity
wwpLeosMcastFilterMIBGroups=_WwpLeosMcastFilterMIBGroups_ObjectIdentity((1,3,6,1,4,1,6141,2,60,7,3,2))
wwpLeosMcastAddrOverlapNotification=NotificationType((1,3,6,1,4,1,6141,2,60,7,2,0,1))
if mibBuilder.loadTexts:wwpLeosMcastAddrOverlapNotification.setStatus(_A)
mibBuilder.exportSymbols(_E,**{'VlanId':VlanId,'wwpLeosMcastFilterMIB':wwpLeosMcastFilterMIB,'wwpLeosMcastFilterMIBObjects':wwpLeosMcastFilterMIBObjects,'wwpLeosMcastFilterConfig':wwpLeosMcastFilterConfig,'wwpLeosMcastConfigState':wwpLeosMcastConfigState,'wwpLeosMcastFilterActivationTable':wwpLeosMcastFilterActivationTable,'wwpLeosMcastFilterActivationEntry':wwpLeosMcastFilterActivationEntry,_F:wwpLeosMcastVlanId,'wwpLeosMcastFilterAdminState':wwpLeosMcastFilterAdminState,'wwpLeosMcastFilterOperState':wwpLeosMcastFilterOperState,'wwpLeosMcastFilterState':wwpLeosMcastFilterState,'wwpLeosMcastFilterServerPortTable':wwpLeosMcastFilterServerPortTable,'wwpLeosMcastFilterServerPortEntry':wwpLeosMcastFilterServerPortEntry,_O:wwpLeosMcastServerPortId,'wwpLeosMcastServerPortStatus':wwpLeosMcastServerPortStatus,'wwpLeosMcastIgmpSnoopTable':wwpLeosMcastIgmpSnoopTable,'wwpLeosMcastIgmpSnoopEntry':wwpLeosMcastIgmpSnoopEntry,'wwpLeosMcastIgmpSnoopEnable':wwpLeosMcastIgmpSnoopEnable,'wwpLeosMcastIgmpSnoopRobustness':wwpLeosMcastIgmpSnoopRobustness,'wwpLeosMcastIgmpSnoopProxyQueryInterval':wwpLeosMcastIgmpSnoopProxyQueryInterval,'wwpLeosMcastIgmpSnoopProxyQueryReplyTmo':wwpLeosMcastIgmpSnoopProxyQueryReplyTmo,'wwpLeosMcastIgmpSnoopProxyQueryDelay':wwpLeosMcastIgmpSnoopProxyQueryDelay,'wwpLeosMcastIgmpSnoopLingerTmo':wwpLeosMcastIgmpSnoopLingerTmo,'wwpLeosMcastIgmpQueryEngineState':wwpLeosMcastIgmpQueryEngineState,'wwpLeosMcastIgmpProxyQuerySrcIp':wwpLeosMcastIgmpProxyQuerySrcIp,'wwpLeosMcastIgmpRouterQueryInterval':wwpLeosMcastIgmpRouterQueryInterval,'wwpLeosMcastIgmpMinResponseTime':wwpLeosMcastIgmpMinResponseTime,'wwpLeosMcastIgmpDefaultRouterPort':wwpLeosMcastIgmpDefaultRouterPort,'wwpLeosMcastIgmpInquisitiveLeaveState':wwpLeosMcastIgmpInquisitiveLeaveState,'wwpLeosMcastIgmpLastMemberQueryInterval':wwpLeosMcastIgmpLastMemberQueryInterval,'wwpLeosMcastIgmpPriority':wwpLeosMcastIgmpPriority,'wwpLeosMcastIgmpSnoopRouterRangeStartIpAddr':wwpLeosMcastIgmpSnoopRouterRangeStartIpAddr,'wwpLeosMcastIgmpSnoopRouterRangeEndIpAddr':wwpLeosMcastIgmpSnoopRouterRangeEndIpAddr,'wwpLeosMcastIgmpSnoopActiveLingerTimeout':wwpLeosMcastIgmpSnoopActiveLingerTimeout,'wwpLeosMcastIgmpSnoopServerTopology':wwpLeosMcastIgmpSnoopServerTopology,'wwpLeosMcastIgmpSnoopRapidRecoveryMode':wwpLeosMcastIgmpSnoopRapidRecoveryMode,'wwpLeosMcastChannelStreamTable':wwpLeosMcastChannelStreamTable,'wwpLeosMcastChannelStreamEntry':wwpLeosMcastChannelStreamEntry,_R:wwpLeosMcastChanelStreamStartGroupAddr,'wwpLeosMcastChanelStreamEndGroupAddr':wwpLeosMcastChanelStreamEndGroupAddr,'wwpLeosMcastChannelStreamStatus':wwpLeosMcastChannelStreamStatus,'wwpLeosMcastFilterConfigTable':wwpLeosMcastFilterConfigTable,'wwpLeosMcastFilterConfigEntry':wwpLeosMcastFilterConfigEntry,'wwpLeosMcastFilterUPFActivate':wwpLeosMcastFilterUPFActivate,'wwpLeosMcastUnresolvedAction':wwpLeosMcastUnresolvedAction,'wwpLeosMcastFilterWKMFLocalActivate':wwpLeosMcastFilterWKMFLocalActivate,'wwpLeosMcastFilterWKMFInternetActivate':wwpLeosMcastFilterWKMFInternetActivate,'wwpLeosMcastFilterWKMFAdhocActivate':wwpLeosMcastFilterWKMFAdhocActivate,'wwpLeosMcastFilterWKMFStMulticastActivate':wwpLeosMcastFilterWKMFStMulticastActivate,'wwpLeosMcastFilterWKMFSdpSapActivate':wwpLeosMcastFilterWKMFSdpSapActivate,'wwpLeosMcastChannelStreamExPortMemTable':wwpLeosMcastChannelStreamExPortMemTable,'wwpLeosMcastChannelStreamExPortMemEntry':wwpLeosMcastChannelStreamExPortMemEntry,_S:wwpLeosMcastChannelStreamExPortId,'wwpLeosMcastChannelStreamExPortMemStatus':wwpLeosMcastChannelStreamExPortMemStatus,'wwpLeosMcastSnoopState':wwpLeosMcastSnoopState,'wwpLeosMcastGlobalStatsClear':wwpLeosMcastGlobalStatsClear,'wwpLeosMcastFilterStatus':wwpLeosMcastFilterStatus,'wwpLeosMcastGroupTable':wwpLeosMcastGroupTable,'wwpLeosMcastGroupEntry':wwpLeosMcastGroupEntry,_N:wwpLeosMcastGroupAddr,'wwpLeosMcastState':wwpLeosMcastState,'wwpLeosMcastType':wwpLeosMcastType,'wwpLeosMcastSource':wwpLeosMcastSource,'wwpLeosMcastMemberCount':wwpLeosMcastMemberCount,'wwpLeosMcastGroupMemberTable':wwpLeosMcastGroupMemberTable,'wwpLeosMcastGroupMemberEntry':wwpLeosMcastGroupMemberEntry,_T:wwpLeosMcastPortId,'wwpLeosMcastPortTagId':wwpLeosMcastPortTagId,'wwpLeosMcastFilterStats':wwpLeosMcastFilterStats,'wwpLeosMcastFilterStatsTable':wwpLeosMcastFilterStatsTable,'wwpLeosMcastFilterStatsEntry':wwpLeosMcastFilterStatsEntry,'wwpLeosMcastStaticGrpCount':wwpLeosMcastStaticGrpCount,'wwpLeosMcastDynamicGrpCount':wwpLeosMcastDynamicGrpCount,'wwpLeosMcastJoinMessages':wwpLeosMcastJoinMessages,'wwpLeosMcastLeaveMessages':wwpLeosMcastLeaveMessages,'wwpLeosMcastQueryMessages':wwpLeosMcastQueryMessages,'wwpLeosMcastQueryDiscards':wwpLeosMcastQueryDiscards,'wwpLeosMcastQueryTimeouts':wwpLeosMcastQueryTimeouts,'wwpLeosMcastUnknownPktType':wwpLeosMcastUnknownPktType,'wwpLeosMcastRouterDiscards':wwpLeosMcastRouterDiscards,'wwpLeosMcastHostDiscards':wwpLeosMcastHostDiscards,'wwpLeosMcastBadChecksum':wwpLeosMcastBadChecksum,'wwpLeosMcastL2L3Mismatch':wwpLeosMcastL2L3Mismatch,'wwpLeosMcastTotalMembers':wwpLeosMcastTotalMembers,'wwpLeosMcastLingerCount':wwpLeosMcastLingerCount,'wwpLeosMcastRouterSrcMacAddr':wwpLeosMcastRouterSrcMacAddr,'wwpLeosMcastRouterSrcIpAddr':wwpLeosMcastRouterSrcIpAddr,'wwpLeosMcastRouterPortId':wwpLeosMcastRouterPortId,'wwpLeosMcastReportSendPortId':wwpLeosMcastReportSendPortId,'wwpLeosMcastStatsClear':wwpLeosMcastStatsClear,'wwpLeosMcastStatsQuerySrcIpZeroDiscard':wwpLeosMcastStatsQuerySrcIpZeroDiscard,'wwpLeosMcastFilterMIBNotificationPrefix':wwpLeosMcastFilterMIBNotificationPrefix,'wwpLeosMcastFilterMIBNotifications':wwpLeosMcastFilterMIBNotifications,'wwpLeosMcastAddrOverlapNotification':wwpLeosMcastAddrOverlapNotification,'wwpLeosMcastFilterMIBConformance':wwpLeosMcastFilterMIBConformance,'wwpLeosMcastFilterMIBCompliances':wwpLeosMcastFilterMIBCompliances,'wwpLeosMcastFilterMIBGroups':wwpLeosMcastFilterMIBGroups})