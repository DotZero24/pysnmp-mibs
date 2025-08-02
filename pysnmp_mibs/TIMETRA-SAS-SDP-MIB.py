_J='tmnxSASSdpV3v0Group'
_I='sdpBindIngressExtraVlanTagDroppedOctets'
_H='sdpBindIngressExtraVlanTagDroppedPackets'
_G='sdpBindIngressExtraVlanTagDropCount'
_F='sdpBindBaseStatsExtnEntry'
_E='sdpBindExtnEntry'
_D='read-only'
_C='TruthValue'
_B='TIMETRA-SAS-SDP-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress','InetAddressType')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention,TimeStamp,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress','RowStatus','TextualConvention','TimeStamp',_C)
tmnxCardSlotNum,tmnxChassisIndex,tmnxMDASlotNum=mibBuilder.importSymbols('TIMETRA-CHASSIS-MIB','tmnxCardSlotNum','tmnxChassisIndex','tmnxMDASlotNum')
TFilterID,=mibBuilder.importSymbols('TIMETRA-FILTER-MIB','TFilterID')
timetraSRMIBModules,=mibBuilder.importSymbols('TIMETRA-GLOBAL-MIB','timetraSRMIBModules')
timetraSASConfs,timetraSASModules,timetraSASNotifyPrefix,timetraSASObjs=mibBuilder.importSymbols('TIMETRA-SAS-GLOBAL-MIB','timetraSASConfs','timetraSASModules','timetraSASNotifyPrefix','timetraSASObjs')
tmnxSASServConformance,=mibBuilder.importSymbols('TIMETRA-SAS-SERV-MIB','tmnxSASServConformance')
sdpBindBaseStatsEntry,sdpBindEntry=mibBuilder.importSymbols('TIMETRA-SDP-MIB','sdpBindBaseStatsEntry','sdpBindEntry')
BridgeId,ConfigStatus,L2ptProtocols,LspIdList,MvplsPruneState,PWTemplateId,SdpBFHundredthsOfPercent,SdpBindBandwidth,SdpBindVcType,SdpId,ServObjDesc,ServObjName,StpExceptionCondition,StpPortRole,StpProtocol,TStpPortState,TdmOptionsCasTrunkFraming,TdmOptionsSigPkts,TlsLimitMacMove,TlsLimitMacMoveLevel,VpnId,custId,svcDhcpClientLease,svcDhcpCoAError,svcDhcpLseStateNewChAddr,svcDhcpLseStateNewCiAddr,svcDhcpLseStateOldChAddr,svcDhcpLseStateOldCiAddr,svcDhcpLseStatePopulateError,svcDhcpPacketProblem,svcDhcpProxyError,svcDhcpSubAuthError,svcId,svcTlsMacMoveMaxRate,svcTlsStpDesignatedRoot,svcVpnId,tlsDhcpPacketProblem,tmnxCustomerBridgeId,tmnxCustomerRootBridgeId,tmnxOldSdpBindTlsStpPortState,tmnxOtherBridgeId,tmnxServConformance,tmnxServNotifications,tmnxServObjs,tmnxSvcObjs,tstpTraps=mibBuilder.importSymbols('TIMETRA-SERV-MIB','BridgeId','ConfigStatus','L2ptProtocols','LspIdList','MvplsPruneState','PWTemplateId','SdpBFHundredthsOfPercent','SdpBindBandwidth','SdpBindVcType','SdpId','ServObjDesc','ServObjName','StpExceptionCondition','StpPortRole','StpProtocol','TStpPortState','TdmOptionsCasTrunkFraming','TdmOptionsSigPkts','TlsLimitMacMove','TlsLimitMacMoveLevel','VpnId','custId','svcDhcpClientLease','svcDhcpCoAError','svcDhcpLseStateNewChAddr','svcDhcpLseStateNewCiAddr','svcDhcpLseStateOldChAddr','svcDhcpLseStateOldCiAddr','svcDhcpLseStatePopulateError','svcDhcpPacketProblem','svcDhcpProxyError','svcDhcpSubAuthError','svcId','svcTlsMacMoveMaxRate','svcTlsStpDesignatedRoot','svcVpnId','tlsDhcpPacketProblem','tmnxCustomerBridgeId','tmnxCustomerRootBridgeId','tmnxOldSdpBindTlsStpPortState','tmnxOtherBridgeId','tmnxServConformance','tmnxServNotifications','tmnxServObjs','tmnxSvcObjs','tstpTraps')
SdpBindId,ServiceAdminStatus,TItemDescription,TNamedItem,TNamedItemOrEmpty,TPolicyStatementNameOrEmpty,TmnxActionType,TmnxCustId,TmnxEnabledDisabled,TmnxIgmpVersion,TmnxOperState,TmnxServId,TmnxVPNRouteDistinguisher,TmnxVRtrMplsLspID=mibBuilder.importSymbols('TIMETRA-TC-MIB','SdpBindId','ServiceAdminStatus','TItemDescription','TNamedItem','TNamedItemOrEmpty','TPolicyStatementNameOrEmpty','TmnxActionType','TmnxCustId','TmnxEnabledDisabled','TmnxIgmpVersion','TmnxOperState','TmnxServId','TmnxVPNRouteDistinguisher','TmnxVRtrMplsLspID')
timetraSASServicesSdpMIBModule=ModuleIdentity((1,3,6,1,4,1,6527,6,2,1,1,12))
if mibBuilder.loadTexts:timetraSASServicesSdpMIBModule.setRevisions(('1907-10-01 00:00',))
_TmnxSASSdpConformance_ObjectIdentity=ObjectIdentity
tmnxSASSdpConformance=_TmnxSASSdpConformance_ObjectIdentity((1,3,6,1,4,1,6527,6,2,2,1,13))
_TmnxSASSdpCompliances_ObjectIdentity=ObjectIdentity
tmnxSASSdpCompliances=_TmnxSASSdpCompliances_ObjectIdentity((1,3,6,1,4,1,6527,6,2,2,1,13,1))
_TmnxSASSdpGroups_ObjectIdentity=ObjectIdentity
tmnxSASSdpGroups=_TmnxSASSdpGroups_ObjectIdentity((1,3,6,1,4,1,6527,6,2,2,1,13,2))
_TmnxSASSdpObjs_ObjectIdentity=ObjectIdentity
tmnxSASSdpObjs=_TmnxSASSdpObjs_ObjectIdentity((1,3,6,1,4,1,6527,6,2,2,2,12))
_SdpBindExtnTable_Object=MibTable
sdpBindExtnTable=_SdpBindExtnTable_Object((1,3,6,1,4,1,6527,6,2,2,2,12,4))
if mibBuilder.loadTexts:sdpBindExtnTable.setStatus(_A)
_SdpBindExtnEntry_Object=MibTableRow
sdpBindExtnEntry=_SdpBindExtnEntry_Object((1,3,6,1,4,1,6527,6,2,2,2,12,4,1))
if mibBuilder.loadTexts:sdpBindExtnEntry.setStatus(_A)
class _SdpBindIngressExtraVlanTagDropCount_Type(TruthValue):defaultValue=2
_SdpBindIngressExtraVlanTagDropCount_Type.__name__=_C
_SdpBindIngressExtraVlanTagDropCount_Object=MibTableColumn
sdpBindIngressExtraVlanTagDropCount=_SdpBindIngressExtraVlanTagDropCount_Object((1,3,6,1,4,1,6527,6,2,2,2,12,4,1,1),_SdpBindIngressExtraVlanTagDropCount_Type())
sdpBindIngressExtraVlanTagDropCount.setMaxAccess('read-create')
if mibBuilder.loadTexts:sdpBindIngressExtraVlanTagDropCount.setStatus(_A)
_SdpBindBaseStatsExtnTable_Object=MibTable
sdpBindBaseStatsExtnTable=_SdpBindBaseStatsExtnTable_Object((1,3,6,1,4,1,6527,6,2,2,2,12,5))
if mibBuilder.loadTexts:sdpBindBaseStatsExtnTable.setStatus(_A)
_SdpBindBaseStatsExtnEntry_Object=MibTableRow
sdpBindBaseStatsExtnEntry=_SdpBindBaseStatsExtnEntry_Object((1,3,6,1,4,1,6527,6,2,2,2,12,5,1))
if mibBuilder.loadTexts:sdpBindBaseStatsExtnEntry.setStatus(_A)
_SdpBindIngressExtraVlanTagDroppedPackets_Type=Counter64
_SdpBindIngressExtraVlanTagDroppedPackets_Object=MibTableColumn
sdpBindIngressExtraVlanTagDroppedPackets=_SdpBindIngressExtraVlanTagDroppedPackets_Object((1,3,6,1,4,1,6527,6,2,2,2,12,5,1,1),_SdpBindIngressExtraVlanTagDroppedPackets_Type())
sdpBindIngressExtraVlanTagDroppedPackets.setMaxAccess(_D)
if mibBuilder.loadTexts:sdpBindIngressExtraVlanTagDroppedPackets.setStatus(_A)
_SdpBindIngressExtraVlanTagDroppedOctets_Type=Counter64
_SdpBindIngressExtraVlanTagDroppedOctets_Object=MibTableColumn
sdpBindIngressExtraVlanTagDroppedOctets=_SdpBindIngressExtraVlanTagDroppedOctets_Object((1,3,6,1,4,1,6527,6,2,2,2,12,5,1,2),_SdpBindIngressExtraVlanTagDroppedOctets_Type())
sdpBindIngressExtraVlanTagDroppedOctets.setMaxAccess(_D)
if mibBuilder.loadTexts:sdpBindIngressExtraVlanTagDroppedOctets.setStatus(_A)
sdpBindEntry.registerAugmentions((_B,_E))
sdpBindExtnEntry.setIndexNames(*sdpBindEntry.getIndexNames())
sdpBindBaseStatsEntry.registerAugmentions((_B,_F))
sdpBindBaseStatsExtnEntry.setIndexNames(*sdpBindBaseStatsEntry.getIndexNames())
tmnxSASSdpV3v0Group=ObjectGroup((1,3,6,1,4,1,6527,6,2,2,1,13,2,1))
tmnxSASSdpV3v0Group.setObjects(*((_B,_G),(_B,_H),(_B,_I)))
if mibBuilder.loadTexts:tmnxSASSdpV3v0Group.setStatus(_A)
tmnxSASSdp7210V3v0Compliance=ModuleCompliance((1,3,6,1,4,1,6527,6,2,2,1,13,1,1))
tmnxSASSdp7210V3v0Compliance.setObjects((_B,_J))
if mibBuilder.loadTexts:tmnxSASSdp7210V3v0Compliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'timetraSASServicesSdpMIBModule':timetraSASServicesSdpMIBModule,'tmnxSASSdpConformance':tmnxSASSdpConformance,'tmnxSASSdpCompliances':tmnxSASSdpCompliances,'tmnxSASSdp7210V3v0Compliance':tmnxSASSdp7210V3v0Compliance,'tmnxSASSdpGroups':tmnxSASSdpGroups,_J:tmnxSASSdpV3v0Group,'tmnxSASSdpObjs':tmnxSASSdpObjs,'sdpBindExtnTable':sdpBindExtnTable,_E:sdpBindExtnEntry,_G:sdpBindIngressExtraVlanTagDropCount,'sdpBindBaseStatsExtnTable':sdpBindBaseStatsExtnTable,_F:sdpBindBaseStatsExtnEntry,_H:sdpBindIngressExtraVlanTagDroppedPackets,_I:sdpBindIngressExtraVlanTagDroppedOctets})