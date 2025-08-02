_Y='sfpsBlockSourceExcludeIndex'
_X='sfpsBlockSourcePortPort'
_W='sfpsBlockSourceOnlyIndex'
_V='sfpsBlockSourceIndex'
_U='sfpsCSPControlTableIndex'
_T='sfpsServiceCenterFacilityHashLeaf'
_S='enabled'
_R='disabled'
_Q='kStatusNotStarted'
_P='kStatusFaulted'
_O='kStatusPending'
_N='kStatusHalted'
_M='kStatusRunning'
_L='sfpsCPResourcesTableId'
_K='wouldBeBlocked'
_J='blocked'
_I='enable'
_H='disable'
_G='unblockable'
_F='other'
_E='CTRON-SFPS-BASE-MIB'
_D='read-write'
_C='Integer32'
_B='read-only'
_A='mandatory'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
sfpsATalkAMRVLANControl,sfpsBlockSource,sfpsBlockSourceAPI,sfpsBlockSourceExclude,sfpsBlockSourceOnly,sfpsBlockSourcePort,sfpsBlockSourceStats,sfpsCPResources,sfpsCSPControl,sfpsDHCPServerVLAN,sfpsServiceCenter=mibBuilder.importSymbols('CTRON-SFPS-INCLUDE-MIB','sfpsATalkAMRVLANControl','sfpsBlockSource','sfpsBlockSourceAPI','sfpsBlockSourceExclude','sfpsBlockSourceOnly','sfpsBlockSourcePort','sfpsBlockSourceStats','sfpsCPResources','sfpsCSPControl','sfpsDHCPServerVLAN','sfpsServiceCenter')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
class HexInteger(Integer32):0
class SfpsAddress(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(6,6));fixedLength=6
_SfpsCPResourcesTable_Object=MibTable
sfpsCPResourcesTable=_SfpsCPResourcesTable_Object((1,3,6,1,4,1,52,4,2,4,2,2,2,3,1))
if mibBuilder.loadTexts:sfpsCPResourcesTable.setStatus(_A)
_SfpsCPResourcesTableEntry_Object=MibTableRow
sfpsCPResourcesTableEntry=_SfpsCPResourcesTableEntry_Object((1,3,6,1,4,1,52,4,2,4,2,2,2,3,1,1))
sfpsCPResourcesTableEntry.setIndexNames((0,_E,_L))
if mibBuilder.loadTexts:sfpsCPResourcesTableEntry.setStatus(_A)
_SfpsCPResourcesTableId_Type=Integer32
_SfpsCPResourcesTableId_Object=MibTableColumn
sfpsCPResourcesTableId=_SfpsCPResourcesTableId_Object((1,3,6,1,4,1,52,4,2,4,2,2,2,3,1,1,1),_SfpsCPResourcesTableId_Type())
sfpsCPResourcesTableId.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsCPResourcesTableId.setStatus(_A)
_SfpsCPResourcesTableName_Type=DisplayString
_SfpsCPResourcesTableName_Object=MibTableColumn
sfpsCPResourcesTableName=_SfpsCPResourcesTableName_Object((1,3,6,1,4,1,52,4,2,4,2,2,2,3,1,1,2),_SfpsCPResourcesTableName_Type())
sfpsCPResourcesTableName.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsCPResourcesTableName.setStatus(_A)
class _SfpsCPResourcesTableOperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_M,1),(_N,2),(_O,3),(_P,4),(_Q,5)))
_SfpsCPResourcesTableOperStatus_Type.__name__=_C
_SfpsCPResourcesTableOperStatus_Object=MibTableColumn
sfpsCPResourcesTableOperStatus=_SfpsCPResourcesTableOperStatus_Object((1,3,6,1,4,1,52,4,2,4,2,2,2,3,1,1,3),_SfpsCPResourcesTableOperStatus_Type())
sfpsCPResourcesTableOperStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsCPResourcesTableOperStatus.setStatus(_A)
class _SfpsCPResourcesTableAdminStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_F,1),(_R,2),(_S,3)))
_SfpsCPResourcesTableAdminStatus_Type.__name__=_C
_SfpsCPResourcesTableAdminStatus_Object=MibTableColumn
sfpsCPResourcesTableAdminStatus=_SfpsCPResourcesTableAdminStatus_Object((1,3,6,1,4,1,52,4,2,4,2,2,2,3,1,1,4),_SfpsCPResourcesTableAdminStatus_Type())
sfpsCPResourcesTableAdminStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsCPResourcesTableAdminStatus.setStatus(_A)
_SfpsCPResourcesTableStateTime_Type=TimeTicks
_SfpsCPResourcesTableStateTime_Object=MibTableColumn
sfpsCPResourcesTableStateTime=_SfpsCPResourcesTableStateTime_Object((1,3,6,1,4,1,52,4,2,4,2,2,2,3,1,1,5),_SfpsCPResourcesTableStateTime_Type())
sfpsCPResourcesTableStateTime.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsCPResourcesTableStateTime.setStatus(_A)
_SfpsCPResourcesTablePtsIn_Type=Integer32
_SfpsCPResourcesTablePtsIn_Object=MibTableColumn
sfpsCPResourcesTablePtsIn=_SfpsCPResourcesTablePtsIn_Object((1,3,6,1,4,1,52,4,2,4,2,2,2,3,1,1,6),_SfpsCPResourcesTablePtsIn_Type())
sfpsCPResourcesTablePtsIn.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsCPResourcesTablePtsIn.setStatus(_A)
_SfpsCPResourcesTablePtsUsed_Type=Integer32
_SfpsCPResourcesTablePtsUsed_Object=MibTableColumn
sfpsCPResourcesTablePtsUsed=_SfpsCPResourcesTablePtsUsed_Object((1,3,6,1,4,1,52,4,2,4,2,2,2,3,1,1,7),_SfpsCPResourcesTablePtsUsed_Type())
sfpsCPResourcesTablePtsUsed.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsCPResourcesTablePtsUsed.setStatus(_A)
_SfpsCPResourcesTablePolicyFlood_Type=Integer32
_SfpsCPResourcesTablePolicyFlood_Object=MibTableColumn
sfpsCPResourcesTablePolicyFlood=_SfpsCPResourcesTablePolicyFlood_Object((1,3,6,1,4,1,52,4,2,4,2,2,2,3,1,1,8),_SfpsCPResourcesTablePolicyFlood_Type())
sfpsCPResourcesTablePolicyFlood.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsCPResourcesTablePolicyFlood.setStatus(_A)
_SfpsCPResourcesResolveFlood_Type=Integer32
_SfpsCPResourcesResolveFlood_Object=MibTableColumn
sfpsCPResourcesResolveFlood=_SfpsCPResourcesResolveFlood_Object((1,3,6,1,4,1,52,4,2,4,2,2,2,3,1,1,9),_SfpsCPResourcesResolveFlood_Type())
sfpsCPResourcesResolveFlood.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsCPResourcesResolveFlood.setStatus(_A)
_SfpsCPResourcesConnectOK_Type=Integer32
_SfpsCPResourcesConnectOK_Object=MibTableColumn
sfpsCPResourcesConnectOK=_SfpsCPResourcesConnectOK_Object((1,3,6,1,4,1,52,4,2,4,2,2,2,3,1,1,10),_SfpsCPResourcesConnectOK_Type())
sfpsCPResourcesConnectOK.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsCPResourcesConnectOK.setStatus(_A)
_SfpsCPResourcesDuplicate_Type=Integer32
_SfpsCPResourcesDuplicate_Object=MibTableColumn
sfpsCPResourcesDuplicate=_SfpsCPResourcesDuplicate_Object((1,3,6,1,4,1,52,4,2,4,2,2,2,3,1,1,11),_SfpsCPResourcesDuplicate_Type())
sfpsCPResourcesDuplicate.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsCPResourcesDuplicate.setStatus(_A)
_SfpsCPResourcesDiscoverOnly_Type=Integer32
_SfpsCPResourcesDiscoverOnly_Object=MibTableColumn
sfpsCPResourcesDiscoverOnly=_SfpsCPResourcesDiscoverOnly_Object((1,3,6,1,4,1,52,4,2,4,2,2,2,3,1,1,12),_SfpsCPResourcesDiscoverOnly_Type())
sfpsCPResourcesDiscoverOnly.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsCPResourcesDiscoverOnly.setStatus(_A)
_SfpsCPResourcesDiscoverError_Type=Integer32
_SfpsCPResourcesDiscoverError_Object=MibTableColumn
sfpsCPResourcesDiscoverError=_SfpsCPResourcesDiscoverError_Object((1,3,6,1,4,1,52,4,2,4,2,2,2,3,1,1,13),_SfpsCPResourcesDiscoverError_Type())
sfpsCPResourcesDiscoverError.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsCPResourcesDiscoverError.setStatus(_A)
_SfpsCPResourcesResolveFail_Type=Integer32
_SfpsCPResourcesResolveFail_Object=MibTableColumn
sfpsCPResourcesResolveFail=_SfpsCPResourcesResolveFail_Object((1,3,6,1,4,1,52,4,2,4,2,2,2,3,1,1,14),_SfpsCPResourcesResolveFail_Type())
sfpsCPResourcesResolveFail.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsCPResourcesResolveFail.setStatus(_A)
_SfpsCPResourcesResolveError_Type=Integer32
_SfpsCPResourcesResolveError_Object=MibTableColumn
sfpsCPResourcesResolveError=_SfpsCPResourcesResolveError_Object((1,3,6,1,4,1,52,4,2,4,2,2,2,3,1,1,15),_SfpsCPResourcesResolveError_Type())
sfpsCPResourcesResolveError.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsCPResourcesResolveError.setStatus(_A)
_SfpsCPResourcesPolicyFail_Type=Integer32
_SfpsCPResourcesPolicyFail_Object=MibTableColumn
sfpsCPResourcesPolicyFail=_SfpsCPResourcesPolicyFail_Object((1,3,6,1,4,1,52,4,2,4,2,2,2,3,1,1,16),_SfpsCPResourcesPolicyFail_Type())
sfpsCPResourcesPolicyFail.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsCPResourcesPolicyFail.setStatus(_A)
_SfpsCPResourcesPolicyError_Type=Integer32
_SfpsCPResourcesPolicyError_Object=MibTableColumn
sfpsCPResourcesPolicyError=_SfpsCPResourcesPolicyError_Object((1,3,6,1,4,1,52,4,2,4,2,2,2,3,1,1,17),_SfpsCPResourcesPolicyError_Type())
sfpsCPResourcesPolicyError.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsCPResourcesPolicyError.setStatus(_A)
_SfpsCPResourcesConnectFail_Type=Integer32
_SfpsCPResourcesConnectFail_Object=MibTableColumn
sfpsCPResourcesConnectFail=_SfpsCPResourcesConnectFail_Object((1,3,6,1,4,1,52,4,2,4,2,2,2,3,1,1,18),_SfpsCPResourcesConnectFail_Type())
sfpsCPResourcesConnectFail.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsCPResourcesConnectFail.setStatus(_A)
_SfpsCPResourcesConnectFlood_Type=Integer32
_SfpsCPResourcesConnectFlood_Object=MibTableColumn
sfpsCPResourcesConnectFlood=_SfpsCPResourcesConnectFlood_Object((1,3,6,1,4,1,52,4,2,4,2,2,2,3,1,1,19),_SfpsCPResourcesConnectFlood_Type())
sfpsCPResourcesConnectFlood.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsCPResourcesConnectFlood.setStatus(_A)
_SfpsCPResourcesConnectError_Type=Integer32
_SfpsCPResourcesConnectError_Object=MibTableColumn
sfpsCPResourcesConnectError=_SfpsCPResourcesConnectError_Object((1,3,6,1,4,1,52,4,2,4,2,2,2,3,1,1,20),_SfpsCPResourcesConnectError_Type())
sfpsCPResourcesConnectError.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsCPResourcesConnectError.setStatus(_A)
_SfpsCPResourcesConfigTime_Type=TimeTicks
_SfpsCPResourcesConfigTime_Object=MibTableColumn
sfpsCPResourcesConfigTime=_SfpsCPResourcesConfigTime_Object((1,3,6,1,4,1,52,4,2,4,2,2,2,3,1,1,21),_SfpsCPResourcesConfigTime_Type())
sfpsCPResourcesConfigTime.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsCPResourcesConfigTime.setStatus(_A)
_SfpsCPResourcesNeedFlood_Type=Integer32
_SfpsCPResourcesNeedFlood_Object=MibTableColumn
sfpsCPResourcesNeedFlood=_SfpsCPResourcesNeedFlood_Object((1,3,6,1,4,1,52,4,2,4,2,2,2,3,1,1,22),_SfpsCPResourcesNeedFlood_Type())
sfpsCPResourcesNeedFlood.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsCPResourcesNeedFlood.setStatus(_A)
_SfpsCPResourcesNeedResolve_Type=Integer32
_SfpsCPResourcesNeedResolve_Object=MibTableColumn
sfpsCPResourcesNeedResolve=_SfpsCPResourcesNeedResolve_Object((1,3,6,1,4,1,52,4,2,4,2,2,2,3,1,1,23),_SfpsCPResourcesNeedResolve_Type())
sfpsCPResourcesNeedResolve.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsCPResourcesNeedResolve.setStatus(_A)
_SfpsCPResourcesNeedDiscover_Type=Integer32
_SfpsCPResourcesNeedDiscover_Object=MibTableColumn
sfpsCPResourcesNeedDiscover=_SfpsCPResourcesNeedDiscover_Object((1,3,6,1,4,1,52,4,2,4,2,2,2,3,1,1,24),_SfpsCPResourcesNeedDiscover_Type())
sfpsCPResourcesNeedDiscover.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsCPResourcesNeedDiscover.setStatus(_A)
_SfpsCPResourcesDiscoverAll_Type=Integer32
_SfpsCPResourcesDiscoverAll_Object=MibTableColumn
sfpsCPResourcesDiscoverAll=_SfpsCPResourcesDiscoverAll_Object((1,3,6,1,4,1,52,4,2,4,2,2,2,3,1,1,25),_SfpsCPResourcesDiscoverAll_Type())
sfpsCPResourcesDiscoverAll.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsCPResourcesDiscoverAll.setStatus(_A)
_SfpsCPResourcesNeedProxyOut_Type=Integer32
_SfpsCPResourcesNeedProxyOut_Object=MibTableColumn
sfpsCPResourcesNeedProxyOut=_SfpsCPResourcesNeedProxyOut_Object((1,3,6,1,4,1,52,4,2,4,2,2,2,3,1,1,26),_SfpsCPResourcesNeedProxyOut_Type())
sfpsCPResourcesNeedProxyOut.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsCPResourcesNeedProxyOut.setStatus(_A)
_SfpsCPResourcesNeedProxyIn_Type=Integer32
_SfpsCPResourcesNeedProxyIn_Object=MibTableColumn
sfpsCPResourcesNeedProxyIn=_SfpsCPResourcesNeedProxyIn_Object((1,3,6,1,4,1,52,4,2,4,2,2,2,3,1,1,27),_SfpsCPResourcesNeedProxyIn_Type())
sfpsCPResourcesNeedProxyIn.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsCPResourcesNeedProxyIn.setStatus(_A)
_SfpsCPResourcesNeedFilter_Type=Integer32
_SfpsCPResourcesNeedFilter_Object=MibTableColumn
sfpsCPResourcesNeedFilter=_SfpsCPResourcesNeedFilter_Object((1,3,6,1,4,1,52,4,2,4,2,2,2,3,1,1,28),_SfpsCPResourcesNeedFilter_Type())
sfpsCPResourcesNeedFilter.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsCPResourcesNeedFilter.setStatus(_A)
_SfpsCPResourcesAcceptRate_Type=Integer32
_SfpsCPResourcesAcceptRate_Object=MibTableColumn
sfpsCPResourcesAcceptRate=_SfpsCPResourcesAcceptRate_Object((1,3,6,1,4,1,52,4,2,4,2,2,2,3,1,1,29),_SfpsCPResourcesAcceptRate_Type())
sfpsCPResourcesAcceptRate.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsCPResourcesAcceptRate.setStatus(_A)
_SfpsCPResourcesTotalRate_Type=Integer32
_SfpsCPResourcesTotalRate_Object=MibTableColumn
sfpsCPResourcesTotalRate=_SfpsCPResourcesTotalRate_Object((1,3,6,1,4,1,52,4,2,4,2,2,2,3,1,1,30),_SfpsCPResourcesTotalRate_Type())
sfpsCPResourcesTotalRate.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsCPResourcesTotalRate.setStatus(_A)
_SfpsCPResourcesSingleFlood_Type=Integer32
_SfpsCPResourcesSingleFlood_Object=MibTableColumn
sfpsCPResourcesSingleFlood=_SfpsCPResourcesSingleFlood_Object((1,3,6,1,4,1,52,4,2,4,2,2,2,3,1,1,34),_SfpsCPResourcesSingleFlood_Type())
sfpsCPResourcesSingleFlood.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsCPResourcesSingleFlood.setStatus(_A)
_SfpsCPResourcesNeedValidNet_Type=Integer32
_SfpsCPResourcesNeedValidNet_Object=MibTableColumn
sfpsCPResourcesNeedValidNet=_SfpsCPResourcesNeedValidNet_Object((1,3,6,1,4,1,52,4,2,4,2,2,2,3,1,1,35),_SfpsCPResourcesNeedValidNet_Type())
sfpsCPResourcesNeedValidNet.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsCPResourcesNeedValidNet.setStatus(_A)
_SfpsCPResourcesInvalidNetDrops_Type=Integer32
_SfpsCPResourcesInvalidNetDrops_Object=MibTableColumn
sfpsCPResourcesInvalidNetDrops=_SfpsCPResourcesInvalidNetDrops_Object((1,3,6,1,4,1,52,4,2,4,2,2,2,3,1,1,36),_SfpsCPResourcesInvalidNetDrops_Type())
sfpsCPResourcesInvalidNetDrops.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsCPResourcesInvalidNetDrops.setStatus(_A)
_SfpsCPResourcesPersistMask_Type=Integer32
_SfpsCPResourcesPersistMask_Object=MibTableColumn
sfpsCPResourcesPersistMask=_SfpsCPResourcesPersistMask_Object((1,3,6,1,4,1,52,4,2,4,2,2,2,3,1,1,37),_SfpsCPResourcesPersistMask_Type())
sfpsCPResourcesPersistMask.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsCPResourcesPersistMask.setStatus(_A)
_SfpsCPResourcesAPI_ObjectIdentity=ObjectIdentity
sfpsCPResourcesAPI=_SfpsCPResourcesAPI_ObjectIdentity((1,3,6,1,4,1,52,4,2,4,2,2,2,3,2))
_SfpsCPResourcesAPIID_Type=Integer32
_SfpsCPResourcesAPIID_Object=MibScalar
sfpsCPResourcesAPIID=_SfpsCPResourcesAPIID_Object((1,3,6,1,4,1,52,4,2,4,2,2,2,3,2,1),_SfpsCPResourcesAPIID_Type())
sfpsCPResourcesAPIID.setMaxAccess(_D)
if mibBuilder.loadTexts:sfpsCPResourcesAPIID.setStatus(_A)
class _SfpsCPResourcesAPIAdminStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_F,1),(_R,2),(_S,3)))
_SfpsCPResourcesAPIAdminStatus_Type.__name__=_C
_SfpsCPResourcesAPIAdminStatus_Object=MibScalar
sfpsCPResourcesAPIAdminStatus=_SfpsCPResourcesAPIAdminStatus_Object((1,3,6,1,4,1,52,4,2,4,2,2,2,3,2,2),_SfpsCPResourcesAPIAdminStatus_Type())
sfpsCPResourcesAPIAdminStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:sfpsCPResourcesAPIAdminStatus.setStatus(_A)
class _SfpsCPResourcesAPIAttribute_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17)));namedValues=NamedValues(*(('none',1),('noFlood',2),('flood',3),('noResolve',4),('resolve',5),('noDiscover',6),('discover',7),('noDiscoverAll',8),('discoverAll',9),('noProxyIn',10),('proxyIn',11),('noProxyOut',12),('proxyOut',13),('nofilter',14),('filter',15),('noValidateNet',16),('validNet',17)))
_SfpsCPResourcesAPIAttribute_Type.__name__=_C
_SfpsCPResourcesAPIAttribute_Object=MibScalar
sfpsCPResourcesAPIAttribute=_SfpsCPResourcesAPIAttribute_Object((1,3,6,1,4,1,52,4,2,4,2,2,2,3,2,3),_SfpsCPResourcesAPIAttribute_Type())
sfpsCPResourcesAPIAttribute.setMaxAccess(_D)
if mibBuilder.loadTexts:sfpsCPResourcesAPIAttribute.setStatus(_A)
class _SfpsCPResourcesAPIScope_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('switch',1),('port',2)))
_SfpsCPResourcesAPIScope_Type.__name__=_C
_SfpsCPResourcesAPIScope_Object=MibScalar
sfpsCPResourcesAPIScope=_SfpsCPResourcesAPIScope_Object((1,3,6,1,4,1,52,4,2,4,2,2,2,3,2,4),_SfpsCPResourcesAPIScope_Type())
sfpsCPResourcesAPIScope.setMaxAccess(_D)
if mibBuilder.loadTexts:sfpsCPResourcesAPIScope.setStatus(_A)
class _SfpsCPResourcesAPIPersistance_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('persistOther',1),('persistDisabled',2),('persistEnabled',3)))
_SfpsCPResourcesAPIPersistance_Type.__name__=_C
_SfpsCPResourcesAPIPersistance_Object=MibScalar
sfpsCPResourcesAPIPersistance=_SfpsCPResourcesAPIPersistance_Object((1,3,6,1,4,1,52,4,2,4,2,2,2,3,2,5),_SfpsCPResourcesAPIPersistance_Type())
sfpsCPResourcesAPIPersistance.setMaxAccess(_D)
if mibBuilder.loadTexts:sfpsCPResourcesAPIPersistance.setStatus(_A)
class _SfpsCPResourcesAPIVerb_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),('set',2)))
_SfpsCPResourcesAPIVerb_Type.__name__=_C
_SfpsCPResourcesAPIVerb_Object=MibScalar
sfpsCPResourcesAPIVerb=_SfpsCPResourcesAPIVerb_Object((1,3,6,1,4,1,52,4,2,4,2,2,2,3,2,6),_SfpsCPResourcesAPIVerb_Type())
sfpsCPResourcesAPIVerb.setMaxAccess(_D)
if mibBuilder.loadTexts:sfpsCPResourcesAPIVerb.setStatus(_A)
_SfpsServiceCenterFacilityTable_Object=MibTable
sfpsServiceCenterFacilityTable=_SfpsServiceCenterFacilityTable_Object((1,3,6,1,4,1,52,4,2,4,2,2,2,4,9))
if mibBuilder.loadTexts:sfpsServiceCenterFacilityTable.setStatus(_A)
_SfpsServiceCenterFacilityEntry_Object=MibTableRow
sfpsServiceCenterFacilityEntry=_SfpsServiceCenterFacilityEntry_Object((1,3,6,1,4,1,52,4,2,4,2,2,2,4,9,1))
sfpsServiceCenterFacilityEntry.setIndexNames((0,_E,_T))
if mibBuilder.loadTexts:sfpsServiceCenterFacilityEntry.setStatus(_A)
_SfpsServiceCenterFacilityHashLeaf_Type=HexInteger
_SfpsServiceCenterFacilityHashLeaf_Object=MibTableColumn
sfpsServiceCenterFacilityHashLeaf=_SfpsServiceCenterFacilityHashLeaf_Object((1,3,6,1,4,1,52,4,2,4,2,2,2,4,9,1,1),_SfpsServiceCenterFacilityHashLeaf_Type())
sfpsServiceCenterFacilityHashLeaf.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsServiceCenterFacilityHashLeaf.setStatus(_A)
_SfpsServiceCenterFacilityMetric_Type=Integer32
_SfpsServiceCenterFacilityMetric_Object=MibTableColumn
sfpsServiceCenterFacilityMetric=_SfpsServiceCenterFacilityMetric_Object((1,3,6,1,4,1,52,4,2,4,2,2,2,4,9,1,2),_SfpsServiceCenterFacilityMetric_Type())
sfpsServiceCenterFacilityMetric.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsServiceCenterFacilityMetric.setStatus(_A)
_SfpsServiceCenterFacilityName_Type=DisplayString
_SfpsServiceCenterFacilityName_Object=MibTableColumn
sfpsServiceCenterFacilityName=_SfpsServiceCenterFacilityName_Object((1,3,6,1,4,1,52,4,2,4,2,2,2,4,9,1,3),_SfpsServiceCenterFacilityName_Type())
sfpsServiceCenterFacilityName.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsServiceCenterFacilityName.setStatus(_A)
class _SfpsServiceCenterFacilityOperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_M,1),(_N,2),(_O,3),(_P,4),(_Q,5)))
_SfpsServiceCenterFacilityOperStatus_Type.__name__=_C
_SfpsServiceCenterFacilityOperStatus_Object=MibTableColumn
sfpsServiceCenterFacilityOperStatus=_SfpsServiceCenterFacilityOperStatus_Object((1,3,6,1,4,1,52,4,2,4,2,2,2,4,9,1,4),_SfpsServiceCenterFacilityOperStatus_Type())
sfpsServiceCenterFacilityOperStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsServiceCenterFacilityOperStatus.setStatus(_A)
class _SfpsServiceCenterFacilityAdminStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_F,1),(_H,2),(_I,3)))
_SfpsServiceCenterFacilityAdminStatus_Type.__name__=_C
_SfpsServiceCenterFacilityAdminStatus_Object=MibTableColumn
sfpsServiceCenterFacilityAdminStatus=_SfpsServiceCenterFacilityAdminStatus_Object((1,3,6,1,4,1,52,4,2,4,2,2,2,4,9,1,5),_SfpsServiceCenterFacilityAdminStatus_Type())
sfpsServiceCenterFacilityAdminStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:sfpsServiceCenterFacilityAdminStatus.setStatus(_A)
_SfpsServiceCenterFacilityStatusTime_Type=TimeTicks
_SfpsServiceCenterFacilityStatusTime_Object=MibTableColumn
sfpsServiceCenterFacilityStatusTime=_SfpsServiceCenterFacilityStatusTime_Object((1,3,6,1,4,1,52,4,2,4,2,2,2,4,9,1,6),_SfpsServiceCenterFacilityStatusTime_Type())
sfpsServiceCenterFacilityStatusTime.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsServiceCenterFacilityStatusTime.setStatus(_A)
_SfpsServiceCenterFacilityRequests_Type=Integer32
_SfpsServiceCenterFacilityRequests_Object=MibTableColumn
sfpsServiceCenterFacilityRequests=_SfpsServiceCenterFacilityRequests_Object((1,3,6,1,4,1,52,4,2,4,2,2,2,4,9,1,7),_SfpsServiceCenterFacilityRequests_Type())
sfpsServiceCenterFacilityRequests.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsServiceCenterFacilityRequests.setStatus(_A)
_SfpsServiceCenterFacilityReply_Type=Integer32
_SfpsServiceCenterFacilityReply_Object=MibTableColumn
sfpsServiceCenterFacilityReply=_SfpsServiceCenterFacilityReply_Object((1,3,6,1,4,1,52,4,2,4,2,2,2,4,9,1,8),_SfpsServiceCenterFacilityReply_Type())
sfpsServiceCenterFacilityReply.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsServiceCenterFacilityReply.setStatus(_A)
_SfpsCSPControlTable_Object=MibTable
sfpsCSPControlTable=_SfpsCSPControlTable_Object((1,3,6,1,4,1,52,4,2,4,2,2,2,5,1))
if mibBuilder.loadTexts:sfpsCSPControlTable.setStatus(_A)
_SfpsCSPControlTableEntry_Object=MibTableRow
sfpsCSPControlTableEntry=_SfpsCSPControlTableEntry_Object((1,3,6,1,4,1,52,4,2,4,2,2,2,5,1,1))
sfpsCSPControlTableEntry.setIndexNames((0,_E,_U))
if mibBuilder.loadTexts:sfpsCSPControlTableEntry.setStatus(_A)
_SfpsCSPControlTableIndex_Type=Integer32
_SfpsCSPControlTableIndex_Object=MibTableColumn
sfpsCSPControlTableIndex=_SfpsCSPControlTableIndex_Object((1,3,6,1,4,1,52,4,2,4,2,2,2,5,1,1,1),_SfpsCSPControlTableIndex_Type())
sfpsCSPControlTableIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsCSPControlTableIndex.setStatus(_A)
_SfpsCSPControlTableCSPType_Type=Integer32
_SfpsCSPControlTableCSPType_Object=MibTableColumn
sfpsCSPControlTableCSPType=_SfpsCSPControlTableCSPType_Object((1,3,6,1,4,1,52,4,2,4,2,2,2,5,1,1,2),_SfpsCSPControlTableCSPType_Type())
sfpsCSPControlTableCSPType.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsCSPControlTableCSPType.setStatus(_A)
_SfpsCSPControlTableCSPName_Type=DisplayString
_SfpsCSPControlTableCSPName_Object=MibTableColumn
sfpsCSPControlTableCSPName=_SfpsCSPControlTableCSPName_Object((1,3,6,1,4,1,52,4,2,4,2,2,2,5,1,1,3),_SfpsCSPControlTableCSPName_Type())
sfpsCSPControlTableCSPName.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsCSPControlTableCSPName.setStatus(_A)
class _SfpsCSPControlTableAdminStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_F,1),(_H,2),(_I,3)))
_SfpsCSPControlTableAdminStatus_Type.__name__=_C
_SfpsCSPControlTableAdminStatus_Object=MibTableColumn
sfpsCSPControlTableAdminStatus=_SfpsCSPControlTableAdminStatus_Object((1,3,6,1,4,1,52,4,2,4,2,2,2,5,1,1,4),_SfpsCSPControlTableAdminStatus_Type())
sfpsCSPControlTableAdminStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:sfpsCSPControlTableAdminStatus.setStatus(_A)
class _SfpsCSPControlTableSwitchToCallProc_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_F,1),(_H,2),(_I,3)))
_SfpsCSPControlTableSwitchToCallProc_Type.__name__=_C
_SfpsCSPControlTableSwitchToCallProc_Object=MibTableColumn
sfpsCSPControlTableSwitchToCallProc=_SfpsCSPControlTableSwitchToCallProc_Object((1,3,6,1,4,1,52,4,2,4,2,2,2,5,1,1,5),_SfpsCSPControlTableSwitchToCallProc_Type())
sfpsCSPControlTableSwitchToCallProc.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsCSPControlTableSwitchToCallProc.setStatus(_A)
_SfpsCSPControlTablePktsProcessed_Type=Integer32
_SfpsCSPControlTablePktsProcessed_Object=MibTableColumn
sfpsCSPControlTablePktsProcessed=_SfpsCSPControlTablePktsProcessed_Object((1,3,6,1,4,1,52,4,2,4,2,2,2,5,1,1,6),_SfpsCSPControlTablePktsProcessed_Type())
sfpsCSPControlTablePktsProcessed.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsCSPControlTablePktsProcessed.setStatus(_A)
_SfpsCSPControlTablePktRate_Type=Integer32
_SfpsCSPControlTablePktRate_Object=MibTableColumn
sfpsCSPControlTablePktRate=_SfpsCSPControlTablePktRate_Object((1,3,6,1,4,1,52,4,2,4,2,2,2,5,1,1,7),_SfpsCSPControlTablePktRate_Type())
sfpsCSPControlTablePktRate.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsCSPControlTablePktRate.setStatus(_A)
_SfpsBlockSourceTable_Object=MibTable
sfpsBlockSourceTable=_SfpsBlockSourceTable_Object((1,3,6,1,4,1,52,4,2,4,2,2,14,1,1))
if mibBuilder.loadTexts:sfpsBlockSourceTable.setStatus(_A)
_SfpsBlockSourceEntry_Object=MibTableRow
sfpsBlockSourceEntry=_SfpsBlockSourceEntry_Object((1,3,6,1,4,1,52,4,2,4,2,2,14,1,1,1))
sfpsBlockSourceEntry.setIndexNames((0,_E,_V))
if mibBuilder.loadTexts:sfpsBlockSourceEntry.setStatus(_A)
_SfpsBlockSourceIndex_Type=Integer32
_SfpsBlockSourceIndex_Object=MibTableColumn
sfpsBlockSourceIndex=_SfpsBlockSourceIndex_Object((1,3,6,1,4,1,52,4,2,4,2,2,14,1,1,1,1),_SfpsBlockSourceIndex_Type())
sfpsBlockSourceIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsBlockSourceIndex.setStatus(_A)
_SfpsBlockSourceMAC_Type=SfpsAddress
_SfpsBlockSourceMAC_Object=MibTableColumn
sfpsBlockSourceMAC=_SfpsBlockSourceMAC_Object((1,3,6,1,4,1,52,4,2,4,2,2,14,1,1,1,2),_SfpsBlockSourceMAC_Type())
sfpsBlockSourceMAC.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsBlockSourceMAC.setStatus(_A)
_SfpsBlockSourceElapTimeShort_Type=TimeTicks
_SfpsBlockSourceElapTimeShort_Object=MibTableColumn
sfpsBlockSourceElapTimeShort=_SfpsBlockSourceElapTimeShort_Object((1,3,6,1,4,1,52,4,2,4,2,2,14,1,1,1,3),_SfpsBlockSourceElapTimeShort_Type())
sfpsBlockSourceElapTimeShort.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsBlockSourceElapTimeShort.setStatus(_A)
_SfpsBlockSourceNumCallsShort_Type=Integer32
_SfpsBlockSourceNumCallsShort_Object=MibTableColumn
sfpsBlockSourceNumCallsShort=_SfpsBlockSourceNumCallsShort_Object((1,3,6,1,4,1,52,4,2,4,2,2,14,1,1,1,4),_SfpsBlockSourceNumCallsShort_Type())
sfpsBlockSourceNumCallsShort.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsBlockSourceNumCallsShort.setStatus(_A)
_SfpsBlockSourceElapTimeLong_Type=TimeTicks
_SfpsBlockSourceElapTimeLong_Object=MibTableColumn
sfpsBlockSourceElapTimeLong=_SfpsBlockSourceElapTimeLong_Object((1,3,6,1,4,1,52,4,2,4,2,2,14,1,1,1,5),_SfpsBlockSourceElapTimeLong_Type())
sfpsBlockSourceElapTimeLong.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsBlockSourceElapTimeLong.setStatus(_A)
_SfpsBlockSourceNumCallLong_Type=Integer32
_SfpsBlockSourceNumCallLong_Object=MibTableColumn
sfpsBlockSourceNumCallLong=_SfpsBlockSourceNumCallLong_Object((1,3,6,1,4,1,52,4,2,4,2,2,14,1,1,1,6),_SfpsBlockSourceNumCallLong_Type())
sfpsBlockSourceNumCallLong.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsBlockSourceNumCallLong.setStatus(_A)
class _SfpsBlockSourceBlockFlag_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_J,1),(_K,2)))
_SfpsBlockSourceBlockFlag_Type.__name__=_C
_SfpsBlockSourceBlockFlag_Object=MibTableColumn
sfpsBlockSourceBlockFlag=_SfpsBlockSourceBlockFlag_Object((1,3,6,1,4,1,52,4,2,4,2,2,14,1,1,1,7),_SfpsBlockSourceBlockFlag_Type())
sfpsBlockSourceBlockFlag.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsBlockSourceBlockFlag.setStatus(_A)
class _SfpsBlockSourceUnBlockableFlag_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues((_G,1))
_SfpsBlockSourceUnBlockableFlag_Type.__name__=_C
_SfpsBlockSourceUnBlockableFlag_Object=MibTableColumn
sfpsBlockSourceUnBlockableFlag=_SfpsBlockSourceUnBlockableFlag_Object((1,3,6,1,4,1,52,4,2,4,2,2,14,1,1,1,8),_SfpsBlockSourceUnBlockableFlag_Type())
sfpsBlockSourceUnBlockableFlag.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsBlockSourceUnBlockableFlag.setStatus(_A)
_SfpsBlockSourceFilterPresent_Type=Integer32
_SfpsBlockSourceFilterPresent_Object=MibTableColumn
sfpsBlockSourceFilterPresent=_SfpsBlockSourceFilterPresent_Object((1,3,6,1,4,1,52,4,2,4,2,2,14,1,1,1,9),_SfpsBlockSourceFilterPresent_Type())
sfpsBlockSourceFilterPresent.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsBlockSourceFilterPresent.setStatus(_A)
_SfpsBlockSourceNext_Type=Integer32
_SfpsBlockSourceNext_Object=MibTableColumn
sfpsBlockSourceNext=_SfpsBlockSourceNext_Object((1,3,6,1,4,1,52,4,2,4,2,2,14,1,1,1,10),_SfpsBlockSourceNext_Type())
sfpsBlockSourceNext.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsBlockSourceNext.setStatus(_A)
_SfpsBlockSourceBlocksOnlyIndex_Type=Integer32
_SfpsBlockSourceBlocksOnlyIndex_Object=MibTableColumn
sfpsBlockSourceBlocksOnlyIndex=_SfpsBlockSourceBlocksOnlyIndex_Object((1,3,6,1,4,1,52,4,2,4,2,2,14,1,1,1,11),_SfpsBlockSourceBlocksOnlyIndex_Type())
sfpsBlockSourceBlocksOnlyIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsBlockSourceBlocksOnlyIndex.setStatus(_A)
_SfpsBlockSourceOnlyTable_Object=MibTable
sfpsBlockSourceOnlyTable=_SfpsBlockSourceOnlyTable_Object((1,3,6,1,4,1,52,4,2,4,2,2,14,2,1))
if mibBuilder.loadTexts:sfpsBlockSourceOnlyTable.setStatus(_A)
_SfpsBlockSourceOnlyEntry_Object=MibTableRow
sfpsBlockSourceOnlyEntry=_SfpsBlockSourceOnlyEntry_Object((1,3,6,1,4,1,52,4,2,4,2,2,14,2,1,1))
sfpsBlockSourceOnlyEntry.setIndexNames((0,_E,_W))
if mibBuilder.loadTexts:sfpsBlockSourceOnlyEntry.setStatus(_A)
_SfpsBlockSourceOnlyIndex_Type=Integer32
_SfpsBlockSourceOnlyIndex_Object=MibTableColumn
sfpsBlockSourceOnlyIndex=_SfpsBlockSourceOnlyIndex_Object((1,3,6,1,4,1,52,4,2,4,2,2,14,2,1,1,1),_SfpsBlockSourceOnlyIndex_Type())
sfpsBlockSourceOnlyIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsBlockSourceOnlyIndex.setStatus(_A)
_SfpsBlockSourceOnlyMAC_Type=SfpsAddress
_SfpsBlockSourceOnlyMAC_Object=MibTableColumn
sfpsBlockSourceOnlyMAC=_SfpsBlockSourceOnlyMAC_Object((1,3,6,1,4,1,52,4,2,4,2,2,14,2,1,1,2),_SfpsBlockSourceOnlyMAC_Type())
sfpsBlockSourceOnlyMAC.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsBlockSourceOnlyMAC.setStatus(_A)
_SfpsBlockSourceOnlyElapTimeShort_Type=TimeTicks
_SfpsBlockSourceOnlyElapTimeShort_Object=MibTableColumn
sfpsBlockSourceOnlyElapTimeShort=_SfpsBlockSourceOnlyElapTimeShort_Object((1,3,6,1,4,1,52,4,2,4,2,2,14,2,1,1,3),_SfpsBlockSourceOnlyElapTimeShort_Type())
sfpsBlockSourceOnlyElapTimeShort.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsBlockSourceOnlyElapTimeShort.setStatus(_A)
_SfpsBlockSourceOnlyNumCallsShort_Type=Integer32
_SfpsBlockSourceOnlyNumCallsShort_Object=MibTableColumn
sfpsBlockSourceOnlyNumCallsShort=_SfpsBlockSourceOnlyNumCallsShort_Object((1,3,6,1,4,1,52,4,2,4,2,2,14,2,1,1,4),_SfpsBlockSourceOnlyNumCallsShort_Type())
sfpsBlockSourceOnlyNumCallsShort.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsBlockSourceOnlyNumCallsShort.setStatus(_A)
_SfpsBlockSourceOnlyElapTimeLong_Type=TimeTicks
_SfpsBlockSourceOnlyElapTimeLong_Object=MibTableColumn
sfpsBlockSourceOnlyElapTimeLong=_SfpsBlockSourceOnlyElapTimeLong_Object((1,3,6,1,4,1,52,4,2,4,2,2,14,2,1,1,5),_SfpsBlockSourceOnlyElapTimeLong_Type())
sfpsBlockSourceOnlyElapTimeLong.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsBlockSourceOnlyElapTimeLong.setStatus(_A)
_SfpsBlockSourceOnlyNumCallLong_Type=Integer32
_SfpsBlockSourceOnlyNumCallLong_Object=MibTableColumn
sfpsBlockSourceOnlyNumCallLong=_SfpsBlockSourceOnlyNumCallLong_Object((1,3,6,1,4,1,52,4,2,4,2,2,14,2,1,1,6),_SfpsBlockSourceOnlyNumCallLong_Type())
sfpsBlockSourceOnlyNumCallLong.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsBlockSourceOnlyNumCallLong.setStatus(_A)
class _SfpsBlockSourceOnlyBlockFlag_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_J,1),(_K,2)))
_SfpsBlockSourceOnlyBlockFlag_Type.__name__=_C
_SfpsBlockSourceOnlyBlockFlag_Object=MibTableColumn
sfpsBlockSourceOnlyBlockFlag=_SfpsBlockSourceOnlyBlockFlag_Object((1,3,6,1,4,1,52,4,2,4,2,2,14,2,1,1,7),_SfpsBlockSourceOnlyBlockFlag_Type())
sfpsBlockSourceOnlyBlockFlag.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsBlockSourceOnlyBlockFlag.setStatus(_A)
class _SfpsBlockSourceOnlyUnBlockableFlag_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues((_G,1))
_SfpsBlockSourceOnlyUnBlockableFlag_Type.__name__=_C
_SfpsBlockSourceOnlyUnBlockableFlag_Object=MibTableColumn
sfpsBlockSourceOnlyUnBlockableFlag=_SfpsBlockSourceOnlyUnBlockableFlag_Object((1,3,6,1,4,1,52,4,2,4,2,2,14,2,1,1,8),_SfpsBlockSourceOnlyUnBlockableFlag_Type())
sfpsBlockSourceOnlyUnBlockableFlag.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsBlockSourceOnlyUnBlockableFlag.setStatus(_A)
_SfpsBlockSourceOnlyFilterPresent_Type=Integer32
_SfpsBlockSourceOnlyFilterPresent_Object=MibTableColumn
sfpsBlockSourceOnlyFilterPresent=_SfpsBlockSourceOnlyFilterPresent_Object((1,3,6,1,4,1,52,4,2,4,2,2,14,2,1,1,9),_SfpsBlockSourceOnlyFilterPresent_Type())
sfpsBlockSourceOnlyFilterPresent.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsBlockSourceOnlyFilterPresent.setStatus(_A)
_SfpsBlockSourceOnlyNext_Type=Integer32
_SfpsBlockSourceOnlyNext_Object=MibTableColumn
sfpsBlockSourceOnlyNext=_SfpsBlockSourceOnlyNext_Object((1,3,6,1,4,1,52,4,2,4,2,2,14,2,1,1,10),_SfpsBlockSourceOnlyNext_Type())
sfpsBlockSourceOnlyNext.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsBlockSourceOnlyNext.setStatus(_A)
_SfpsBlockSourceOnlyBlocksOnlyIndex_Type=Integer32
_SfpsBlockSourceOnlyBlocksOnlyIndex_Object=MibTableColumn
sfpsBlockSourceOnlyBlocksOnlyIndex=_SfpsBlockSourceOnlyBlocksOnlyIndex_Object((1,3,6,1,4,1,52,4,2,4,2,2,14,2,1,1,11),_SfpsBlockSourceOnlyBlocksOnlyIndex_Type())
sfpsBlockSourceOnlyBlocksOnlyIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsBlockSourceOnlyBlocksOnlyIndex.setStatus(_A)
_SfpsBlockSourcePortTable_Object=MibTable
sfpsBlockSourcePortTable=_SfpsBlockSourcePortTable_Object((1,3,6,1,4,1,52,4,2,4,2,2,14,3,1))
if mibBuilder.loadTexts:sfpsBlockSourcePortTable.setStatus(_A)
_SfpsBlockSourcePortEntry_Object=MibTableRow
sfpsBlockSourcePortEntry=_SfpsBlockSourcePortEntry_Object((1,3,6,1,4,1,52,4,2,4,2,2,14,3,1,1))
sfpsBlockSourcePortEntry.setIndexNames((0,_E,_X))
if mibBuilder.loadTexts:sfpsBlockSourcePortEntry.setStatus(_A)
_SfpsBlockSourcePortPort_Type=Integer32
_SfpsBlockSourcePortPort_Object=MibTableColumn
sfpsBlockSourcePortPort=_SfpsBlockSourcePortPort_Object((1,3,6,1,4,1,52,4,2,4,2,2,14,3,1,1,1),_SfpsBlockSourcePortPort_Type())
sfpsBlockSourcePortPort.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsBlockSourcePortPort.setStatus(_A)
class _SfpsBlockSourcePortBlockability_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues((_G,1))
_SfpsBlockSourcePortBlockability_Type.__name__=_C
_SfpsBlockSourcePortBlockability_Object=MibTableColumn
sfpsBlockSourcePortBlockability=_SfpsBlockSourcePortBlockability_Object((1,3,6,1,4,1,52,4,2,4,2,2,14,3,1,1,2),_SfpsBlockSourcePortBlockability_Type())
sfpsBlockSourcePortBlockability.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsBlockSourcePortBlockability.setStatus(_A)
class _SfpsBlockSourceAPIVerb_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15)));namedValues=NamedValues(*((_F,1),('switchToLearning',2),('switchToBlocking',3),('setShortThreshold',4),('setShortPeriod',5),('setLongThreshold',6),('setLongPeriod',7),('clearAll',8),('blockMac',9),('unblockMac',10),('setMacUnblockable',11),('setMacBlockable',12),('setPortUnblockable',13),('setPortBlockable',14),('setReapUserCnx',15)))
_SfpsBlockSourceAPIVerb_Type.__name__=_C
_SfpsBlockSourceAPIVerb_Object=MibScalar
sfpsBlockSourceAPIVerb=_SfpsBlockSourceAPIVerb_Object((1,3,6,1,4,1,52,4,2,4,2,2,14,4,1),_SfpsBlockSourceAPIVerb_Type())
sfpsBlockSourceAPIVerb.setMaxAccess(_D)
if mibBuilder.loadTexts:sfpsBlockSourceAPIVerb.setStatus(_A)
_SfpsBlockSourceAPIInputValue_Type=Integer32
_SfpsBlockSourceAPIInputValue_Object=MibScalar
sfpsBlockSourceAPIInputValue=_SfpsBlockSourceAPIInputValue_Object((1,3,6,1,4,1,52,4,2,4,2,2,14,4,2),_SfpsBlockSourceAPIInputValue_Type())
sfpsBlockSourceAPIInputValue.setMaxAccess(_D)
if mibBuilder.loadTexts:sfpsBlockSourceAPIInputValue.setStatus(_A)
_SfpsBlockSourceAPIPort_Type=Integer32
_SfpsBlockSourceAPIPort_Object=MibScalar
sfpsBlockSourceAPIPort=_SfpsBlockSourceAPIPort_Object((1,3,6,1,4,1,52,4,2,4,2,2,14,4,3),_SfpsBlockSourceAPIPort_Type())
sfpsBlockSourceAPIPort.setMaxAccess(_D)
if mibBuilder.loadTexts:sfpsBlockSourceAPIPort.setStatus(_A)
_SfpsBlockSourceAPIMAC_Type=SfpsAddress
_SfpsBlockSourceAPIMAC_Object=MibScalar
sfpsBlockSourceAPIMAC=_SfpsBlockSourceAPIMAC_Object((1,3,6,1,4,1,52,4,2,4,2,2,14,4,4),_SfpsBlockSourceAPIMAC_Type())
sfpsBlockSourceAPIMAC.setMaxAccess(_D)
if mibBuilder.loadTexts:sfpsBlockSourceAPIMAC.setStatus(_A)
class _SfpsBlockSourceAPIBlockStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_F,1),('learning',2),('blocking',3)))
_SfpsBlockSourceAPIBlockStatus_Type.__name__=_C
_SfpsBlockSourceAPIBlockStatus_Object=MibScalar
sfpsBlockSourceAPIBlockStatus=_SfpsBlockSourceAPIBlockStatus_Object((1,3,6,1,4,1,52,4,2,4,2,2,14,4,5),_SfpsBlockSourceAPIBlockStatus_Type())
sfpsBlockSourceAPIBlockStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:sfpsBlockSourceAPIBlockStatus.setStatus(_A)
_SfpsBlockSourceAPIShortThreshold_Type=Integer32
_SfpsBlockSourceAPIShortThreshold_Object=MibScalar
sfpsBlockSourceAPIShortThreshold=_SfpsBlockSourceAPIShortThreshold_Object((1,3,6,1,4,1,52,4,2,4,2,2,14,4,6),_SfpsBlockSourceAPIShortThreshold_Type())
sfpsBlockSourceAPIShortThreshold.setMaxAccess(_D)
if mibBuilder.loadTexts:sfpsBlockSourceAPIShortThreshold.setStatus(_A)
_SfpsBlockSourceAPIShortPeriod_Type=Integer32
_SfpsBlockSourceAPIShortPeriod_Object=MibScalar
sfpsBlockSourceAPIShortPeriod=_SfpsBlockSourceAPIShortPeriod_Object((1,3,6,1,4,1,52,4,2,4,2,2,14,4,7),_SfpsBlockSourceAPIShortPeriod_Type())
sfpsBlockSourceAPIShortPeriod.setMaxAccess(_D)
if mibBuilder.loadTexts:sfpsBlockSourceAPIShortPeriod.setStatus(_A)
_SfpsBlockSourceAPILongThreshold_Type=Integer32
_SfpsBlockSourceAPILongThreshold_Object=MibScalar
sfpsBlockSourceAPILongThreshold=_SfpsBlockSourceAPILongThreshold_Object((1,3,6,1,4,1,52,4,2,4,2,2,14,4,8),_SfpsBlockSourceAPILongThreshold_Type())
sfpsBlockSourceAPILongThreshold.setMaxAccess(_D)
if mibBuilder.loadTexts:sfpsBlockSourceAPILongThreshold.setStatus(_A)
_SfpsBlockSourceAPILongPeriod_Type=Integer32
_SfpsBlockSourceAPILongPeriod_Object=MibScalar
sfpsBlockSourceAPILongPeriod=_SfpsBlockSourceAPILongPeriod_Object((1,3,6,1,4,1,52,4,2,4,2,2,14,4,9),_SfpsBlockSourceAPILongPeriod_Type())
sfpsBlockSourceAPILongPeriod.setMaxAccess(_D)
if mibBuilder.loadTexts:sfpsBlockSourceAPILongPeriod.setStatus(_A)
_SfpsBlockSourceAPIReapUserCnxs_Type=Integer32
_SfpsBlockSourceAPIReapUserCnxs_Object=MibScalar
sfpsBlockSourceAPIReapUserCnxs=_SfpsBlockSourceAPIReapUserCnxs_Object((1,3,6,1,4,1,52,4,2,4,2,2,14,4,10),_SfpsBlockSourceAPIReapUserCnxs_Type())
sfpsBlockSourceAPIReapUserCnxs.setMaxAccess(_D)
if mibBuilder.loadTexts:sfpsBlockSourceAPIReapUserCnxs.setStatus(_A)
_SfpsBlockSourceExcludeTable_Object=MibTable
sfpsBlockSourceExcludeTable=_SfpsBlockSourceExcludeTable_Object((1,3,6,1,4,1,52,4,2,4,2,2,14,5,1))
if mibBuilder.loadTexts:sfpsBlockSourceExcludeTable.setStatus(_A)
_SfpsBlockSourceExcludeEntry_Object=MibTableRow
sfpsBlockSourceExcludeEntry=_SfpsBlockSourceExcludeEntry_Object((1,3,6,1,4,1,52,4,2,4,2,2,14,5,1,1))
sfpsBlockSourceExcludeEntry.setIndexNames((0,_E,_Y))
if mibBuilder.loadTexts:sfpsBlockSourceExcludeEntry.setStatus(_A)
_SfpsBlockSourceExcludeIndex_Type=Integer32
_SfpsBlockSourceExcludeIndex_Object=MibTableColumn
sfpsBlockSourceExcludeIndex=_SfpsBlockSourceExcludeIndex_Object((1,3,6,1,4,1,52,4,2,4,2,2,14,5,1,1,1),_SfpsBlockSourceExcludeIndex_Type())
sfpsBlockSourceExcludeIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsBlockSourceExcludeIndex.setStatus(_A)
_SfpsBlockSourceExcludeMAC_Type=SfpsAddress
_SfpsBlockSourceExcludeMAC_Object=MibTableColumn
sfpsBlockSourceExcludeMAC=_SfpsBlockSourceExcludeMAC_Object((1,3,6,1,4,1,52,4,2,4,2,2,14,5,1,1,2),_SfpsBlockSourceExcludeMAC_Type())
sfpsBlockSourceExcludeMAC.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsBlockSourceExcludeMAC.setStatus(_A)
_SfpsBlockSourceExcludeElapTimeShort_Type=TimeTicks
_SfpsBlockSourceExcludeElapTimeShort_Object=MibTableColumn
sfpsBlockSourceExcludeElapTimeShort=_SfpsBlockSourceExcludeElapTimeShort_Object((1,3,6,1,4,1,52,4,2,4,2,2,14,5,1,1,3),_SfpsBlockSourceExcludeElapTimeShort_Type())
sfpsBlockSourceExcludeElapTimeShort.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsBlockSourceExcludeElapTimeShort.setStatus(_A)
_SfpsBlockSourceExcludeNumCallsShort_Type=Integer32
_SfpsBlockSourceExcludeNumCallsShort_Object=MibTableColumn
sfpsBlockSourceExcludeNumCallsShort=_SfpsBlockSourceExcludeNumCallsShort_Object((1,3,6,1,4,1,52,4,2,4,2,2,14,5,1,1,4),_SfpsBlockSourceExcludeNumCallsShort_Type())
sfpsBlockSourceExcludeNumCallsShort.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsBlockSourceExcludeNumCallsShort.setStatus(_A)
_SfpsBlockSourceExcludeElapTimeLong_Type=TimeTicks
_SfpsBlockSourceExcludeElapTimeLong_Object=MibTableColumn
sfpsBlockSourceExcludeElapTimeLong=_SfpsBlockSourceExcludeElapTimeLong_Object((1,3,6,1,4,1,52,4,2,4,2,2,14,5,1,1,5),_SfpsBlockSourceExcludeElapTimeLong_Type())
sfpsBlockSourceExcludeElapTimeLong.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsBlockSourceExcludeElapTimeLong.setStatus(_A)
_SfpsBlockSourceExcludeNumCallLong_Type=Integer32
_SfpsBlockSourceExcludeNumCallLong_Object=MibTableColumn
sfpsBlockSourceExcludeNumCallLong=_SfpsBlockSourceExcludeNumCallLong_Object((1,3,6,1,4,1,52,4,2,4,2,2,14,5,1,1,6),_SfpsBlockSourceExcludeNumCallLong_Type())
sfpsBlockSourceExcludeNumCallLong.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsBlockSourceExcludeNumCallLong.setStatus(_A)
class _SfpsBlockSourceExcludeBlockFlag_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_J,1),(_K,2)))
_SfpsBlockSourceExcludeBlockFlag_Type.__name__=_C
_SfpsBlockSourceExcludeBlockFlag_Object=MibTableColumn
sfpsBlockSourceExcludeBlockFlag=_SfpsBlockSourceExcludeBlockFlag_Object((1,3,6,1,4,1,52,4,2,4,2,2,14,5,1,1,7),_SfpsBlockSourceExcludeBlockFlag_Type())
sfpsBlockSourceExcludeBlockFlag.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsBlockSourceExcludeBlockFlag.setStatus(_A)
class _SfpsBlockSourceExcludeUnBlockableFlag_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues((_G,1))
_SfpsBlockSourceExcludeUnBlockableFlag_Type.__name__=_C
_SfpsBlockSourceExcludeUnBlockableFlag_Object=MibTableColumn
sfpsBlockSourceExcludeUnBlockableFlag=_SfpsBlockSourceExcludeUnBlockableFlag_Object((1,3,6,1,4,1,52,4,2,4,2,2,14,5,1,1,8),_SfpsBlockSourceExcludeUnBlockableFlag_Type())
sfpsBlockSourceExcludeUnBlockableFlag.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsBlockSourceExcludeUnBlockableFlag.setStatus(_A)
_SfpsBlockSourceExcludeFilterPresent_Type=Integer32
_SfpsBlockSourceExcludeFilterPresent_Object=MibTableColumn
sfpsBlockSourceExcludeFilterPresent=_SfpsBlockSourceExcludeFilterPresent_Object((1,3,6,1,4,1,52,4,2,4,2,2,14,5,1,1,9),_SfpsBlockSourceExcludeFilterPresent_Type())
sfpsBlockSourceExcludeFilterPresent.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsBlockSourceExcludeFilterPresent.setStatus(_A)
_SfpsBlockSourceExcludeNext_Type=Integer32
_SfpsBlockSourceExcludeNext_Object=MibTableColumn
sfpsBlockSourceExcludeNext=_SfpsBlockSourceExcludeNext_Object((1,3,6,1,4,1,52,4,2,4,2,2,14,5,1,1,10),_SfpsBlockSourceExcludeNext_Type())
sfpsBlockSourceExcludeNext.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsBlockSourceExcludeNext.setStatus(_A)
_SfpsBlockSourceExcludeBlockSourceOnlyIndex_Type=Integer32
_SfpsBlockSourceExcludeBlockSourceOnlyIndex_Object=MibTableColumn
sfpsBlockSourceExcludeBlockSourceOnlyIndex=_SfpsBlockSourceExcludeBlockSourceOnlyIndex_Object((1,3,6,1,4,1,52,4,2,4,2,2,14,5,1,1,11),_SfpsBlockSourceExcludeBlockSourceOnlyIndex_Type())
sfpsBlockSourceExcludeBlockSourceOnlyIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsBlockSourceExcludeBlockSourceOnlyIndex.setStatus(_A)
_SfpsBlockSourceStatsNumBlocks_Type=Integer32
_SfpsBlockSourceStatsNumBlocks_Object=MibScalar
sfpsBlockSourceStatsNumBlocks=_SfpsBlockSourceStatsNumBlocks_Object((1,3,6,1,4,1,52,4,2,4,2,2,14,6,1),_SfpsBlockSourceStatsNumBlocks_Type())
sfpsBlockSourceStatsNumBlocks.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsBlockSourceStatsNumBlocks.setStatus(_A)
_SfpsBlockSourceStatsNumCollisions_Type=Integer32
_SfpsBlockSourceStatsNumCollisions_Object=MibScalar
sfpsBlockSourceStatsNumCollisions=_SfpsBlockSourceStatsNumCollisions_Object((1,3,6,1,4,1,52,4,2,4,2,2,14,6,2),_SfpsBlockSourceStatsNumCollisions_Type())
sfpsBlockSourceStatsNumCollisions.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsBlockSourceStatsNumCollisions.setStatus(_A)
_SfpsBlockSourceStatsLongestChain_Type=Integer32
_SfpsBlockSourceStatsLongestChain_Object=MibScalar
sfpsBlockSourceStatsLongestChain=_SfpsBlockSourceStatsLongestChain_Object((1,3,6,1,4,1,52,4,2,4,2,2,14,6,3),_SfpsBlockSourceStatsLongestChain_Type())
sfpsBlockSourceStatsLongestChain.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsBlockSourceStatsLongestChain.setStatus(_A)
_SfpsBlockSourceStatsNumEntries_Type=Integer32
_SfpsBlockSourceStatsNumEntries_Object=MibScalar
sfpsBlockSourceStatsNumEntries=_SfpsBlockSourceStatsNumEntries_Object((1,3,6,1,4,1,52,4,2,4,2,2,14,6,4),_SfpsBlockSourceStatsNumEntries_Type())
sfpsBlockSourceStatsNumEntries.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsBlockSourceStatsNumEntries.setStatus(_A)
_SfpsBlockSourceStatsMaxNumEntries_Type=Integer32
_SfpsBlockSourceStatsMaxNumEntries_Object=MibScalar
sfpsBlockSourceStatsMaxNumEntries=_SfpsBlockSourceStatsMaxNumEntries_Object((1,3,6,1,4,1,52,4,2,4,2,2,14,6,5),_SfpsBlockSourceStatsMaxNumEntries_Type())
sfpsBlockSourceStatsMaxNumEntries.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsBlockSourceStatsMaxNumEntries.setStatus(_A)
_SfpsBlockSourceStatsSizeOfObj_Type=Integer32
_SfpsBlockSourceStatsSizeOfObj_Object=MibScalar
sfpsBlockSourceStatsSizeOfObj=_SfpsBlockSourceStatsSizeOfObj_Object((1,3,6,1,4,1,52,4,2,4,2,2,14,6,6),_SfpsBlockSourceStatsSizeOfObj_Type())
sfpsBlockSourceStatsSizeOfObj.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsBlockSourceStatsSizeOfObj.setStatus(_A)
_SfpsBlockSourceStatsHashModValue_Type=Integer32
_SfpsBlockSourceStatsHashModValue_Object=MibScalar
sfpsBlockSourceStatsHashModValue=_SfpsBlockSourceStatsHashModValue_Object((1,3,6,1,4,1,52,4,2,4,2,2,14,6,7),_SfpsBlockSourceStatsHashModValue_Type())
sfpsBlockSourceStatsHashModValue.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsBlockSourceStatsHashModValue.setStatus(_A)
_SfpsBlockSourceStatsHashSlotsSize_Type=Integer32
_SfpsBlockSourceStatsHashSlotsSize_Object=MibScalar
sfpsBlockSourceStatsHashSlotsSize=_SfpsBlockSourceStatsHashSlotsSize_Object((1,3,6,1,4,1,52,4,2,4,2,2,14,6,8),_SfpsBlockSourceStatsHashSlotsSize_Type())
sfpsBlockSourceStatsHashSlotsSize.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsBlockSourceStatsHashSlotsSize.setStatus(_A)
_SfpsBlockSourceStatsTableSize_Type=Integer32
_SfpsBlockSourceStatsTableSize_Object=MibScalar
sfpsBlockSourceStatsTableSize=_SfpsBlockSourceStatsTableSize_Object((1,3,6,1,4,1,52,4,2,4,2,2,14,6,9),_SfpsBlockSourceStatsTableSize_Type())
sfpsBlockSourceStatsTableSize.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsBlockSourceStatsTableSize.setStatus(_A)
_SfpsBlockSourceStatsBlockSourceOnlySize_Type=Integer32
_SfpsBlockSourceStatsBlockSourceOnlySize_Object=MibScalar
sfpsBlockSourceStatsBlockSourceOnlySize=_SfpsBlockSourceStatsBlockSourceOnlySize_Object((1,3,6,1,4,1,52,4,2,4,2,2,14,6,10),_SfpsBlockSourceStatsBlockSourceOnlySize_Type())
sfpsBlockSourceStatsBlockSourceOnlySize.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsBlockSourceStatsBlockSourceOnlySize.setStatus(_A)
_SfpsBlockSourceStatsUnblockableSize_Type=Integer32
_SfpsBlockSourceStatsUnblockableSize_Object=MibScalar
sfpsBlockSourceStatsUnblockableSize=_SfpsBlockSourceStatsUnblockableSize_Object((1,3,6,1,4,1,52,4,2,4,2,2,14,6,11),_SfpsBlockSourceStatsUnblockableSize_Type())
sfpsBlockSourceStatsUnblockableSize.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsBlockSourceStatsUnblockableSize.setStatus(_A)
_SfpsBlockSourceStatsPortMaskSize_Type=Integer32
_SfpsBlockSourceStatsPortMaskSize_Object=MibScalar
sfpsBlockSourceStatsPortMaskSize=_SfpsBlockSourceStatsPortMaskSize_Object((1,3,6,1,4,1,52,4,2,4,2,2,14,6,12),_SfpsBlockSourceStatsPortMaskSize_Type())
sfpsBlockSourceStatsPortMaskSize.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsBlockSourceStatsPortMaskSize.setStatus(_A)
_SfpsBlockSourceStatsTotalHeapBytes_Type=Integer32
_SfpsBlockSourceStatsTotalHeapBytes_Object=MibScalar
sfpsBlockSourceStatsTotalHeapBytes=_SfpsBlockSourceStatsTotalHeapBytes_Object((1,3,6,1,4,1,52,4,2,4,2,2,14,6,13),_SfpsBlockSourceStatsTotalHeapBytes_Type())
sfpsBlockSourceStatsTotalHeapBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsBlockSourceStatsTotalHeapBytes.setStatus(_A)
_SfpsDHCPServerVLANName_Type=OctetString
_SfpsDHCPServerVLANName_Object=MibScalar
sfpsDHCPServerVLANName=_SfpsDHCPServerVLANName_Object((1,3,6,1,4,1,52,4,2,4,2,2,15,1),_SfpsDHCPServerVLANName_Type())
sfpsDHCPServerVLANName.setMaxAccess(_D)
if mibBuilder.loadTexts:sfpsDHCPServerVLANName.setStatus(_A)
class _SfpsDHCPServerVLANSingleFloodStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('on',1),('off',2)))
_SfpsDHCPServerVLANSingleFloodStatus_Type.__name__=_C
_SfpsDHCPServerVLANSingleFloodStatus_Object=MibScalar
sfpsDHCPServerVLANSingleFloodStatus=_SfpsDHCPServerVLANSingleFloodStatus_Object((1,3,6,1,4,1,52,4,2,4,2,2,15,2),_SfpsDHCPServerVLANSingleFloodStatus_Type())
sfpsDHCPServerVLANSingleFloodStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:sfpsDHCPServerVLANSingleFloodStatus.setStatus(_A)
_SfpsDHCPServerVLANVersion_Type=Integer32
_SfpsDHCPServerVLANVersion_Object=MibScalar
sfpsDHCPServerVLANVersion=_SfpsDHCPServerVLANVersion_Object((1,3,6,1,4,1,52,4,2,4,2,2,15,3),_SfpsDHCPServerVLANVersion_Type())
sfpsDHCPServerVLANVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsDHCPServerVLANVersion.setStatus(_A)
_SfpsATalkAMRVLANControlName_Type=OctetString
_SfpsATalkAMRVLANControlName_Object=MibScalar
sfpsATalkAMRVLANControlName=_SfpsATalkAMRVLANControlName_Object((1,3,6,1,4,1,52,4,2,4,2,2,16,1),_SfpsATalkAMRVLANControlName_Type())
sfpsATalkAMRVLANControlName.setMaxAccess(_D)
if mibBuilder.loadTexts:sfpsATalkAMRVLANControlName.setStatus(_A)
_SfpsATalkAMRVLANControlVersion_Type=Integer32
_SfpsATalkAMRVLANControlVersion_Object=MibScalar
sfpsATalkAMRVLANControlVersion=_SfpsATalkAMRVLANControlVersion_Object((1,3,6,1,4,1,52,4,2,4,2,2,16,2),_SfpsATalkAMRVLANControlVersion_Type())
sfpsATalkAMRVLANControlVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsATalkAMRVLANControlVersion.setStatus(_A)
mibBuilder.exportSymbols(_E,**{'HexInteger':HexInteger,'SfpsAddress':SfpsAddress,'sfpsCPResourcesTable':sfpsCPResourcesTable,'sfpsCPResourcesTableEntry':sfpsCPResourcesTableEntry,_L:sfpsCPResourcesTableId,'sfpsCPResourcesTableName':sfpsCPResourcesTableName,'sfpsCPResourcesTableOperStatus':sfpsCPResourcesTableOperStatus,'sfpsCPResourcesTableAdminStatus':sfpsCPResourcesTableAdminStatus,'sfpsCPResourcesTableStateTime':sfpsCPResourcesTableStateTime,'sfpsCPResourcesTablePtsIn':sfpsCPResourcesTablePtsIn,'sfpsCPResourcesTablePtsUsed':sfpsCPResourcesTablePtsUsed,'sfpsCPResourcesTablePolicyFlood':sfpsCPResourcesTablePolicyFlood,'sfpsCPResourcesResolveFlood':sfpsCPResourcesResolveFlood,'sfpsCPResourcesConnectOK':sfpsCPResourcesConnectOK,'sfpsCPResourcesDuplicate':sfpsCPResourcesDuplicate,'sfpsCPResourcesDiscoverOnly':sfpsCPResourcesDiscoverOnly,'sfpsCPResourcesDiscoverError':sfpsCPResourcesDiscoverError,'sfpsCPResourcesResolveFail':sfpsCPResourcesResolveFail,'sfpsCPResourcesResolveError':sfpsCPResourcesResolveError,'sfpsCPResourcesPolicyFail':sfpsCPResourcesPolicyFail,'sfpsCPResourcesPolicyError':sfpsCPResourcesPolicyError,'sfpsCPResourcesConnectFail':sfpsCPResourcesConnectFail,'sfpsCPResourcesConnectFlood':sfpsCPResourcesConnectFlood,'sfpsCPResourcesConnectError':sfpsCPResourcesConnectError,'sfpsCPResourcesConfigTime':sfpsCPResourcesConfigTime,'sfpsCPResourcesNeedFlood':sfpsCPResourcesNeedFlood,'sfpsCPResourcesNeedResolve':sfpsCPResourcesNeedResolve,'sfpsCPResourcesNeedDiscover':sfpsCPResourcesNeedDiscover,'sfpsCPResourcesDiscoverAll':sfpsCPResourcesDiscoverAll,'sfpsCPResourcesNeedProxyOut':sfpsCPResourcesNeedProxyOut,'sfpsCPResourcesNeedProxyIn':sfpsCPResourcesNeedProxyIn,'sfpsCPResourcesNeedFilter':sfpsCPResourcesNeedFilter,'sfpsCPResourcesAcceptRate':sfpsCPResourcesAcceptRate,'sfpsCPResourcesTotalRate':sfpsCPResourcesTotalRate,'sfpsCPResourcesSingleFlood':sfpsCPResourcesSingleFlood,'sfpsCPResourcesNeedValidNet':sfpsCPResourcesNeedValidNet,'sfpsCPResourcesInvalidNetDrops':sfpsCPResourcesInvalidNetDrops,'sfpsCPResourcesPersistMask':sfpsCPResourcesPersistMask,'sfpsCPResourcesAPI':sfpsCPResourcesAPI,'sfpsCPResourcesAPIID':sfpsCPResourcesAPIID,'sfpsCPResourcesAPIAdminStatus':sfpsCPResourcesAPIAdminStatus,'sfpsCPResourcesAPIAttribute':sfpsCPResourcesAPIAttribute,'sfpsCPResourcesAPIScope':sfpsCPResourcesAPIScope,'sfpsCPResourcesAPIPersistance':sfpsCPResourcesAPIPersistance,'sfpsCPResourcesAPIVerb':sfpsCPResourcesAPIVerb,'sfpsServiceCenterFacilityTable':sfpsServiceCenterFacilityTable,'sfpsServiceCenterFacilityEntry':sfpsServiceCenterFacilityEntry,_T:sfpsServiceCenterFacilityHashLeaf,'sfpsServiceCenterFacilityMetric':sfpsServiceCenterFacilityMetric,'sfpsServiceCenterFacilityName':sfpsServiceCenterFacilityName,'sfpsServiceCenterFacilityOperStatus':sfpsServiceCenterFacilityOperStatus,'sfpsServiceCenterFacilityAdminStatus':sfpsServiceCenterFacilityAdminStatus,'sfpsServiceCenterFacilityStatusTime':sfpsServiceCenterFacilityStatusTime,'sfpsServiceCenterFacilityRequests':sfpsServiceCenterFacilityRequests,'sfpsServiceCenterFacilityReply':sfpsServiceCenterFacilityReply,'sfpsCSPControlTable':sfpsCSPControlTable,'sfpsCSPControlTableEntry':sfpsCSPControlTableEntry,_U:sfpsCSPControlTableIndex,'sfpsCSPControlTableCSPType':sfpsCSPControlTableCSPType,'sfpsCSPControlTableCSPName':sfpsCSPControlTableCSPName,'sfpsCSPControlTableAdminStatus':sfpsCSPControlTableAdminStatus,'sfpsCSPControlTableSwitchToCallProc':sfpsCSPControlTableSwitchToCallProc,'sfpsCSPControlTablePktsProcessed':sfpsCSPControlTablePktsProcessed,'sfpsCSPControlTablePktRate':sfpsCSPControlTablePktRate,'sfpsBlockSourceTable':sfpsBlockSourceTable,'sfpsBlockSourceEntry':sfpsBlockSourceEntry,_V:sfpsBlockSourceIndex,'sfpsBlockSourceMAC':sfpsBlockSourceMAC,'sfpsBlockSourceElapTimeShort':sfpsBlockSourceElapTimeShort,'sfpsBlockSourceNumCallsShort':sfpsBlockSourceNumCallsShort,'sfpsBlockSourceElapTimeLong':sfpsBlockSourceElapTimeLong,'sfpsBlockSourceNumCallLong':sfpsBlockSourceNumCallLong,'sfpsBlockSourceBlockFlag':sfpsBlockSourceBlockFlag,'sfpsBlockSourceUnBlockableFlag':sfpsBlockSourceUnBlockableFlag,'sfpsBlockSourceFilterPresent':sfpsBlockSourceFilterPresent,'sfpsBlockSourceNext':sfpsBlockSourceNext,'sfpsBlockSourceBlocksOnlyIndex':sfpsBlockSourceBlocksOnlyIndex,'sfpsBlockSourceOnlyTable':sfpsBlockSourceOnlyTable,'sfpsBlockSourceOnlyEntry':sfpsBlockSourceOnlyEntry,_W:sfpsBlockSourceOnlyIndex,'sfpsBlockSourceOnlyMAC':sfpsBlockSourceOnlyMAC,'sfpsBlockSourceOnlyElapTimeShort':sfpsBlockSourceOnlyElapTimeShort,'sfpsBlockSourceOnlyNumCallsShort':sfpsBlockSourceOnlyNumCallsShort,'sfpsBlockSourceOnlyElapTimeLong':sfpsBlockSourceOnlyElapTimeLong,'sfpsBlockSourceOnlyNumCallLong':sfpsBlockSourceOnlyNumCallLong,'sfpsBlockSourceOnlyBlockFlag':sfpsBlockSourceOnlyBlockFlag,'sfpsBlockSourceOnlyUnBlockableFlag':sfpsBlockSourceOnlyUnBlockableFlag,'sfpsBlockSourceOnlyFilterPresent':sfpsBlockSourceOnlyFilterPresent,'sfpsBlockSourceOnlyNext':sfpsBlockSourceOnlyNext,'sfpsBlockSourceOnlyBlocksOnlyIndex':sfpsBlockSourceOnlyBlocksOnlyIndex,'sfpsBlockSourcePortTable':sfpsBlockSourcePortTable,'sfpsBlockSourcePortEntry':sfpsBlockSourcePortEntry,_X:sfpsBlockSourcePortPort,'sfpsBlockSourcePortBlockability':sfpsBlockSourcePortBlockability,'sfpsBlockSourceAPIVerb':sfpsBlockSourceAPIVerb,'sfpsBlockSourceAPIInputValue':sfpsBlockSourceAPIInputValue,'sfpsBlockSourceAPIPort':sfpsBlockSourceAPIPort,'sfpsBlockSourceAPIMAC':sfpsBlockSourceAPIMAC,'sfpsBlockSourceAPIBlockStatus':sfpsBlockSourceAPIBlockStatus,'sfpsBlockSourceAPIShortThreshold':sfpsBlockSourceAPIShortThreshold,'sfpsBlockSourceAPIShortPeriod':sfpsBlockSourceAPIShortPeriod,'sfpsBlockSourceAPILongThreshold':sfpsBlockSourceAPILongThreshold,'sfpsBlockSourceAPILongPeriod':sfpsBlockSourceAPILongPeriod,'sfpsBlockSourceAPIReapUserCnxs':sfpsBlockSourceAPIReapUserCnxs,'sfpsBlockSourceExcludeTable':sfpsBlockSourceExcludeTable,'sfpsBlockSourceExcludeEntry':sfpsBlockSourceExcludeEntry,_Y:sfpsBlockSourceExcludeIndex,'sfpsBlockSourceExcludeMAC':sfpsBlockSourceExcludeMAC,'sfpsBlockSourceExcludeElapTimeShort':sfpsBlockSourceExcludeElapTimeShort,'sfpsBlockSourceExcludeNumCallsShort':sfpsBlockSourceExcludeNumCallsShort,'sfpsBlockSourceExcludeElapTimeLong':sfpsBlockSourceExcludeElapTimeLong,'sfpsBlockSourceExcludeNumCallLong':sfpsBlockSourceExcludeNumCallLong,'sfpsBlockSourceExcludeBlockFlag':sfpsBlockSourceExcludeBlockFlag,'sfpsBlockSourceExcludeUnBlockableFlag':sfpsBlockSourceExcludeUnBlockableFlag,'sfpsBlockSourceExcludeFilterPresent':sfpsBlockSourceExcludeFilterPresent,'sfpsBlockSourceExcludeNext':sfpsBlockSourceExcludeNext,'sfpsBlockSourceExcludeBlockSourceOnlyIndex':sfpsBlockSourceExcludeBlockSourceOnlyIndex,'sfpsBlockSourceStatsNumBlocks':sfpsBlockSourceStatsNumBlocks,'sfpsBlockSourceStatsNumCollisions':sfpsBlockSourceStatsNumCollisions,'sfpsBlockSourceStatsLongestChain':sfpsBlockSourceStatsLongestChain,'sfpsBlockSourceStatsNumEntries':sfpsBlockSourceStatsNumEntries,'sfpsBlockSourceStatsMaxNumEntries':sfpsBlockSourceStatsMaxNumEntries,'sfpsBlockSourceStatsSizeOfObj':sfpsBlockSourceStatsSizeOfObj,'sfpsBlockSourceStatsHashModValue':sfpsBlockSourceStatsHashModValue,'sfpsBlockSourceStatsHashSlotsSize':sfpsBlockSourceStatsHashSlotsSize,'sfpsBlockSourceStatsTableSize':sfpsBlockSourceStatsTableSize,'sfpsBlockSourceStatsBlockSourceOnlySize':sfpsBlockSourceStatsBlockSourceOnlySize,'sfpsBlockSourceStatsUnblockableSize':sfpsBlockSourceStatsUnblockableSize,'sfpsBlockSourceStatsPortMaskSize':sfpsBlockSourceStatsPortMaskSize,'sfpsBlockSourceStatsTotalHeapBytes':sfpsBlockSourceStatsTotalHeapBytes,'sfpsDHCPServerVLANName':sfpsDHCPServerVLANName,'sfpsDHCPServerVLANSingleFloodStatus':sfpsDHCPServerVLANSingleFloodStatus,'sfpsDHCPServerVLANVersion':sfpsDHCPServerVLANVersion,'sfpsATalkAMRVLANControlName':sfpsATalkAMRVLANControlName,'sfpsATalkAMRVLANControlVersion':sfpsATalkAMRVLANControlVersion})