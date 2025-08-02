_I='rlMgmdInterfaceExtEntry'
_H='CISCOSB-MGMD-ROUTER-MIB'
_G='AdminStatus'
_F='read-create'
_E='read-write'
_D='DisplayString'
_C='Integer32'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
switch001,=mibBuilder.importSymbols('CISCOSB-MIB','switch001')
NpgOperStatus,=mibBuilder.importSymbols('CISCOSB-PIM-MIB','NpgOperStatus')
InterfaceIndex,InterfaceIndexOrZero=mibBuilder.importSymbols('IF-MIB','InterfaceIndex','InterfaceIndexOrZero')
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress','InetAddressType')
mgmdRouterInterfaceEntry,=mibBuilder.importSymbols('MGMD-STD-MIB','mgmdRouterInterfaceEntry')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso,mib_2=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso','mib-2')
DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC',_D,'PhysAddress','RowStatus','TextualConvention','TruthValue')
rlIgmp=ModuleIdentity((1,3,6,1,4,1,9,6,1,101,225))
if mibBuilder.loadTexts:rlIgmp.setRevisions(('2011-07-21 00:00',))
class AdminStatus(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('adminStatusUp',1),('adminStatusDown',2)))
_RlMgmdInterfaceExtTable_Object=MibTable
rlMgmdInterfaceExtTable=_RlMgmdInterfaceExtTable_Object((1,3,6,1,4,1,9,6,1,101,225,1))
if mibBuilder.loadTexts:rlMgmdInterfaceExtTable.setStatus(_A)
_RlMgmdInterfaceExtEntry_Object=MibTableRow
rlMgmdInterfaceExtEntry=_RlMgmdInterfaceExtEntry_Object((1,3,6,1,4,1,9,6,1,101,225,1,1))
if mibBuilder.loadTexts:rlMgmdInterfaceExtEntry.setStatus(_A)
_RlMgmdRouterInterfaceExtStatsUpTime_Type=TimeTicks
_RlMgmdRouterInterfaceExtStatsUpTime_Object=MibTableColumn
rlMgmdRouterInterfaceExtStatsUpTime=_RlMgmdRouterInterfaceExtStatsUpTime_Object((1,3,6,1,4,1,9,6,1,101,225,1,1,1),_RlMgmdRouterInterfaceExtStatsUpTime_Type())
rlMgmdRouterInterfaceExtStatsUpTime.setMaxAccess(_B)
if mibBuilder.loadTexts:rlMgmdRouterInterfaceExtStatsUpTime.setStatus(_A)
_RlMgmdRouterInterfaceExtEnableStats_Type=TruthValue
_RlMgmdRouterInterfaceExtEnableStats_Object=MibTableColumn
rlMgmdRouterInterfaceExtEnableStats=_RlMgmdRouterInterfaceExtEnableStats_Object((1,3,6,1,4,1,9,6,1,101,225,1,1,2),_RlMgmdRouterInterfaceExtEnableStats_Type())
rlMgmdRouterInterfaceExtEnableStats.setMaxAccess(_E)
if mibBuilder.loadTexts:rlMgmdRouterInterfaceExtEnableStats.setStatus(_A)
_RlMgmdRouterInterfaceExtNumFailedJoins_Type=Unsigned32
_RlMgmdRouterInterfaceExtNumFailedJoins_Object=MibTableColumn
rlMgmdRouterInterfaceExtNumFailedJoins=_RlMgmdRouterInterfaceExtNumFailedJoins_Object((1,3,6,1,4,1,9,6,1,101,225,1,1,3),_RlMgmdRouterInterfaceExtNumFailedJoins_Type())
rlMgmdRouterInterfaceExtNumFailedJoins.setMaxAccess(_B)
if mibBuilder.loadTexts:rlMgmdRouterInterfaceExtNumFailedJoins.setStatus(_A)
_RlMgmdRouterInterfaceExtNumIgmpV1Msgs_Type=Unsigned32
_RlMgmdRouterInterfaceExtNumIgmpV1Msgs_Object=MibTableColumn
rlMgmdRouterInterfaceExtNumIgmpV1Msgs=_RlMgmdRouterInterfaceExtNumIgmpV1Msgs_Object((1,3,6,1,4,1,9,6,1,101,225,1,1,4),_RlMgmdRouterInterfaceExtNumIgmpV1Msgs_Type())
rlMgmdRouterInterfaceExtNumIgmpV1Msgs.setMaxAccess(_B)
if mibBuilder.loadTexts:rlMgmdRouterInterfaceExtNumIgmpV1Msgs.setStatus(_A)
_RlMgmdRouterInterfaceExtNumIgmpV2MldV1Msgs_Type=Unsigned32
_RlMgmdRouterInterfaceExtNumIgmpV2MldV1Msgs_Object=MibTableColumn
rlMgmdRouterInterfaceExtNumIgmpV2MldV1Msgs=_RlMgmdRouterInterfaceExtNumIgmpV2MldV1Msgs_Object((1,3,6,1,4,1,9,6,1,101,225,1,1,5),_RlMgmdRouterInterfaceExtNumIgmpV2MldV1Msgs_Type())
rlMgmdRouterInterfaceExtNumIgmpV2MldV1Msgs.setMaxAccess(_B)
if mibBuilder.loadTexts:rlMgmdRouterInterfaceExtNumIgmpV2MldV1Msgs.setStatus(_A)
_RlMgmdRouterInterfaceExtNumIgmpV3MldV2Msgs_Type=Unsigned32
_RlMgmdRouterInterfaceExtNumIgmpV3MldV2Msgs_Object=MibTableColumn
rlMgmdRouterInterfaceExtNumIgmpV3MldV2Msgs=_RlMgmdRouterInterfaceExtNumIgmpV3MldV2Msgs_Object((1,3,6,1,4,1,9,6,1,101,225,1,1,6),_RlMgmdRouterInterfaceExtNumIgmpV3MldV2Msgs_Type())
rlMgmdRouterInterfaceExtNumIgmpV3MldV2Msgs.setMaxAccess(_B)
if mibBuilder.loadTexts:rlMgmdRouterInterfaceExtNumIgmpV3MldV2Msgs.setStatus(_A)
_RlMgmdRouterInterfaceExtNumInvalidMsgsRcvd_Type=Unsigned32
_RlMgmdRouterInterfaceExtNumInvalidMsgsRcvd_Object=MibTableColumn
rlMgmdRouterInterfaceExtNumInvalidMsgsRcvd=_RlMgmdRouterInterfaceExtNumInvalidMsgsRcvd_Object((1,3,6,1,4,1,9,6,1,101,225,1,1,7),_RlMgmdRouterInterfaceExtNumInvalidMsgsRcvd_Type())
rlMgmdRouterInterfaceExtNumInvalidMsgsRcvd.setMaxAccess(_B)
if mibBuilder.loadTexts:rlMgmdRouterInterfaceExtNumInvalidMsgsRcvd.setStatus(_A)
_RlMgmdRouterInterfaceExtNumGenQueriesSent_Type=Unsigned32
_RlMgmdRouterInterfaceExtNumGenQueriesSent_Object=MibTableColumn
rlMgmdRouterInterfaceExtNumGenQueriesSent=_RlMgmdRouterInterfaceExtNumGenQueriesSent_Object((1,3,6,1,4,1,9,6,1,101,225,1,1,8),_RlMgmdRouterInterfaceExtNumGenQueriesSent_Type())
rlMgmdRouterInterfaceExtNumGenQueriesSent.setMaxAccess(_B)
if mibBuilder.loadTexts:rlMgmdRouterInterfaceExtNumGenQueriesSent.setStatus(_A)
_RlMgmdRouterInterfaceExtNumSpecQueriesSent_Type=Unsigned32
_RlMgmdRouterInterfaceExtNumSpecQueriesSent_Object=MibTableColumn
rlMgmdRouterInterfaceExtNumSpecQueriesSent=_RlMgmdRouterInterfaceExtNumSpecQueriesSent_Object((1,3,6,1,4,1,9,6,1,101,225,1,1,9),_RlMgmdRouterInterfaceExtNumSpecQueriesSent_Type())
rlMgmdRouterInterfaceExtNumSpecQueriesSent.setMaxAccess(_B)
if mibBuilder.loadTexts:rlMgmdRouterInterfaceExtNumSpecQueriesSent.setStatus(_A)
_RlmgmdRouterInterfaceQrRobustness_Type=Unsigned32
_RlmgmdRouterInterfaceQrRobustness_Object=MibTableColumn
rlmgmdRouterInterfaceQrRobustness=_RlmgmdRouterInterfaceQrRobustness_Object((1,3,6,1,4,1,9,6,1,101,225,1,1,10),_RlmgmdRouterInterfaceQrRobustness_Type())
rlmgmdRouterInterfaceQrRobustness.setMaxAccess(_B)
if mibBuilder.loadTexts:rlmgmdRouterInterfaceQrRobustness.setStatus(_A)
_RlmgmdRouterInterfaceQrQueryInterval_Type=Unsigned32
_RlmgmdRouterInterfaceQrQueryInterval_Object=MibTableColumn
rlmgmdRouterInterfaceQrQueryInterval=_RlmgmdRouterInterfaceQrQueryInterval_Object((1,3,6,1,4,1,9,6,1,101,225,1,1,11),_RlmgmdRouterInterfaceQrQueryInterval_Type())
rlmgmdRouterInterfaceQrQueryInterval.setMaxAccess(_B)
if mibBuilder.loadTexts:rlmgmdRouterInterfaceQrQueryInterval.setStatus(_A)
_RlmgmdRouterInterfaceQrQueryMaxResponseTime_Type=Unsigned32
_RlmgmdRouterInterfaceQrQueryMaxResponseTime_Object=MibTableColumn
rlmgmdRouterInterfaceQrQueryMaxResponseTime=_RlmgmdRouterInterfaceQrQueryMaxResponseTime_Object((1,3,6,1,4,1,9,6,1,101,225,1,1,12),_RlmgmdRouterInterfaceQrQueryMaxResponseTime_Type())
rlmgmdRouterInterfaceQrQueryMaxResponseTime.setMaxAccess(_B)
if mibBuilder.loadTexts:rlmgmdRouterInterfaceQrQueryMaxResponseTime.setStatus(_A)
_RlmgmdRouterInterfaceQrLastMembQueryIntvl_Type=Unsigned32
_RlmgmdRouterInterfaceQrLastMembQueryIntvl_Object=MibTableColumn
rlmgmdRouterInterfaceQrLastMembQueryIntvl=_RlmgmdRouterInterfaceQrLastMembQueryIntvl_Object((1,3,6,1,4,1,9,6,1,101,225,1,1,13),_RlmgmdRouterInterfaceQrLastMembQueryIntvl_Type())
rlmgmdRouterInterfaceQrLastMembQueryIntvl.setMaxAccess(_B)
if mibBuilder.loadTexts:rlmgmdRouterInterfaceQrLastMembQueryIntvl.setStatus(_A)
class _RlmgmdRouterInterfaceExtSrcAndGrpFilter_Type(DisplayString):defaultValue=OctetString('')
_RlmgmdRouterInterfaceExtSrcAndGrpFilter_Type.__name__=_D
_RlmgmdRouterInterfaceExtSrcAndGrpFilter_Object=MibTableColumn
rlmgmdRouterInterfaceExtSrcAndGrpFilter=_RlmgmdRouterInterfaceExtSrcAndGrpFilter_Object((1,3,6,1,4,1,9,6,1,101,225,1,1,14),_RlmgmdRouterInterfaceExtSrcAndGrpFilter_Type())
rlmgmdRouterInterfaceExtSrcAndGrpFilter.setMaxAccess(_F)
if mibBuilder.loadTexts:rlmgmdRouterInterfaceExtSrcAndGrpFilter.setStatus(_A)
class _RlMgmdRouterInterfaceExtAdminStatus_Type(AdminStatus):defaultValue=2
_RlMgmdRouterInterfaceExtAdminStatus_Type.__name__=_G
_RlMgmdRouterInterfaceExtAdminStatus_Object=MibTableColumn
rlMgmdRouterInterfaceExtAdminStatus=_RlMgmdRouterInterfaceExtAdminStatus_Object((1,3,6,1,4,1,9,6,1,101,225,1,1,15),_RlMgmdRouterInterfaceExtAdminStatus_Type())
rlMgmdRouterInterfaceExtAdminStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:rlMgmdRouterInterfaceExtAdminStatus.setStatus(_A)
_RlMgmdRouterInterfaceExtOperStatus_Type=NpgOperStatus
_RlMgmdRouterInterfaceExtOperStatus_Object=MibTableColumn
rlMgmdRouterInterfaceExtOperStatus=_RlMgmdRouterInterfaceExtOperStatus_Object((1,3,6,1,4,1,9,6,1,101,225,1,1,16),_RlMgmdRouterInterfaceExtOperStatus_Type())
rlMgmdRouterInterfaceExtOperStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:rlMgmdRouterInterfaceExtOperStatus.setStatus(_A)
_RlMgmdRouterInterfaceExtIsQuerier_Type=TruthValue
_RlMgmdRouterInterfaceExtIsQuerier_Object=MibTableColumn
rlMgmdRouterInterfaceExtIsQuerier=_RlMgmdRouterInterfaceExtIsQuerier_Object((1,3,6,1,4,1,9,6,1,101,225,1,1,17),_RlMgmdRouterInterfaceExtIsQuerier_Type())
rlMgmdRouterInterfaceExtIsQuerier.setMaxAccess(_B)
if mibBuilder.loadTexts:rlMgmdRouterInterfaceExtIsQuerier.setStatus(_A)
class _RlMgmdRouterInterfaceExtProxyDownProtected_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(-1,1,2)));namedValues=NamedValues(*(('unspecified',-1),('enabled',1),('disabled',2)))
_RlMgmdRouterInterfaceExtProxyDownProtected_Type.__name__=_C
_RlMgmdRouterInterfaceExtProxyDownProtected_Object=MibTableColumn
rlMgmdRouterInterfaceExtProxyDownProtected=_RlMgmdRouterInterfaceExtProxyDownProtected_Object((1,3,6,1,4,1,9,6,1,101,225,1,1,18),_RlMgmdRouterInterfaceExtProxyDownProtected_Type())
rlMgmdRouterInterfaceExtProxyDownProtected.setMaxAccess(_E)
if mibBuilder.loadTexts:rlMgmdRouterInterfaceExtProxyDownProtected.setStatus(_A)
mgmdRouterInterfaceEntry.registerAugmentions((_H,_I))
rlMgmdInterfaceExtEntry.setIndexNames(*mgmdRouterInterfaceEntry.getIndexNames())
mibBuilder.exportSymbols(_H,**{_G:AdminStatus,'rlIgmp':rlIgmp,'rlMgmdInterfaceExtTable':rlMgmdInterfaceExtTable,_I:rlMgmdInterfaceExtEntry,'rlMgmdRouterInterfaceExtStatsUpTime':rlMgmdRouterInterfaceExtStatsUpTime,'rlMgmdRouterInterfaceExtEnableStats':rlMgmdRouterInterfaceExtEnableStats,'rlMgmdRouterInterfaceExtNumFailedJoins':rlMgmdRouterInterfaceExtNumFailedJoins,'rlMgmdRouterInterfaceExtNumIgmpV1Msgs':rlMgmdRouterInterfaceExtNumIgmpV1Msgs,'rlMgmdRouterInterfaceExtNumIgmpV2MldV1Msgs':rlMgmdRouterInterfaceExtNumIgmpV2MldV1Msgs,'rlMgmdRouterInterfaceExtNumIgmpV3MldV2Msgs':rlMgmdRouterInterfaceExtNumIgmpV3MldV2Msgs,'rlMgmdRouterInterfaceExtNumInvalidMsgsRcvd':rlMgmdRouterInterfaceExtNumInvalidMsgsRcvd,'rlMgmdRouterInterfaceExtNumGenQueriesSent':rlMgmdRouterInterfaceExtNumGenQueriesSent,'rlMgmdRouterInterfaceExtNumSpecQueriesSent':rlMgmdRouterInterfaceExtNumSpecQueriesSent,'rlmgmdRouterInterfaceQrRobustness':rlmgmdRouterInterfaceQrRobustness,'rlmgmdRouterInterfaceQrQueryInterval':rlmgmdRouterInterfaceQrQueryInterval,'rlmgmdRouterInterfaceQrQueryMaxResponseTime':rlmgmdRouterInterfaceQrQueryMaxResponseTime,'rlmgmdRouterInterfaceQrLastMembQueryIntvl':rlmgmdRouterInterfaceQrLastMembQueryIntvl,'rlmgmdRouterInterfaceExtSrcAndGrpFilter':rlmgmdRouterInterfaceExtSrcAndGrpFilter,'rlMgmdRouterInterfaceExtAdminStatus':rlMgmdRouterInterfaceExtAdminStatus,'rlMgmdRouterInterfaceExtOperStatus':rlMgmdRouterInterfaceExtOperStatus,'rlMgmdRouterInterfaceExtIsQuerier':rlMgmdRouterInterfaceExtIsQuerier,'rlMgmdRouterInterfaceExtProxyDownProtected':rlMgmdRouterInterfaceExtProxyDownProtected})