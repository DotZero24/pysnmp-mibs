_L='dhcpClientIfIndex'
_K='dhcpClientOptType'
_J='dhcpClientOptIfIndex'
_I='dhcpClientConfigIfIndex'
_H='not-accessible'
_G='notset'
_F='set'
_E='SUPERMICRO-DHCP-CLIENT-MIB'
_D='read-write'
_C='Integer32'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
InterfaceIndex,=mibBuilder.importSymbols('IF-MIB','InterfaceIndex')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention')
futureDhcpClientMIB=ModuleIdentity((1,3,6,1,4,1,10876,101,1,87))
if mibBuilder.loadTexts:futureDhcpClientMIB.setRevisions(('2012-09-05 00:00',))
_DhcpClientConfig_ObjectIdentity=ObjectIdentity
dhcpClientConfig=_DhcpClientConfig_ObjectIdentity((1,3,6,1,4,1,10876,101,1,87,1))
_DhcpClientConfigTable_Object=MibTable
dhcpClientConfigTable=_DhcpClientConfigTable_Object((1,3,6,1,4,1,10876,101,1,87,1,1))
if mibBuilder.loadTexts:dhcpClientConfigTable.setStatus(_A)
_DhcpClientConfigEntry_Object=MibTableRow
dhcpClientConfigEntry=_DhcpClientConfigEntry_Object((1,3,6,1,4,1,10876,101,1,87,1,1,1))
dhcpClientConfigEntry.setIndexNames((0,_E,_I))
if mibBuilder.loadTexts:dhcpClientConfigEntry.setStatus(_A)
class _DhcpClientConfigIfIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_DhcpClientConfigIfIndex_Type.__name__=_C
_DhcpClientConfigIfIndex_Object=MibTableColumn
dhcpClientConfigIfIndex=_DhcpClientConfigIfIndex_Object((1,3,6,1,4,1,10876,101,1,87,1,1,1,1),_DhcpClientConfigIfIndex_Type())
dhcpClientConfigIfIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:dhcpClientConfigIfIndex.setStatus(_A)
class _DhcpClientRenew_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_DhcpClientRenew_Type.__name__=_C
_DhcpClientRenew_Object=MibTableColumn
dhcpClientRenew=_DhcpClientRenew_Object((1,3,6,1,4,1,10876,101,1,87,1,1,1,2),_DhcpClientRenew_Type())
dhcpClientRenew.setMaxAccess(_D)
if mibBuilder.loadTexts:dhcpClientRenew.setStatus(_A)
class _DhcpClientRebind_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_DhcpClientRebind_Type.__name__=_C
_DhcpClientRebind_Object=MibTableColumn
dhcpClientRebind=_DhcpClientRebind_Object((1,3,6,1,4,1,10876,101,1,87,1,1,1,3),_DhcpClientRebind_Type())
dhcpClientRebind.setMaxAccess(_D)
if mibBuilder.loadTexts:dhcpClientRebind.setStatus(_A)
class _DhcpClientInform_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_DhcpClientInform_Type.__name__=_C
_DhcpClientInform_Object=MibTableColumn
dhcpClientInform=_DhcpClientInform_Object((1,3,6,1,4,1,10876,101,1,87,1,1,1,4),_DhcpClientInform_Type())
dhcpClientInform.setMaxAccess(_D)
if mibBuilder.loadTexts:dhcpClientInform.setStatus(_A)
class _DhcpClientRelease_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_DhcpClientRelease_Type.__name__=_C
_DhcpClientRelease_Object=MibTableColumn
dhcpClientRelease=_DhcpClientRelease_Object((1,3,6,1,4,1,10876,101,1,87,1,1,1,5),_DhcpClientRelease_Type())
dhcpClientRelease.setMaxAccess(_D)
if mibBuilder.loadTexts:dhcpClientRelease.setStatus(_A)
_DhcpClientIdentifier_Type=OctetString
_DhcpClientIdentifier_Object=MibTableColumn
dhcpClientIdentifier=_DhcpClientIdentifier_Object((1,3,6,1,4,1,10876,101,1,87,1,1,1,6),_DhcpClientIdentifier_Type())
dhcpClientIdentifier.setMaxAccess(_D)
if mibBuilder.loadTexts:dhcpClientIdentifier.setStatus(_A)
class _DhcpClientDebugTrace_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_DhcpClientDebugTrace_Type.__name__=_C
_DhcpClientDebugTrace_Object=MibScalar
dhcpClientDebugTrace=_DhcpClientDebugTrace_Object((1,3,6,1,4,1,10876,101,1,87,1,2),_DhcpClientDebugTrace_Type())
dhcpClientDebugTrace.setMaxAccess(_D)
if mibBuilder.loadTexts:dhcpClientDebugTrace.setStatus(_A)
_DhcpClientOptTable_Object=MibTable
dhcpClientOptTable=_DhcpClientOptTable_Object((1,3,6,1,4,1,10876,101,1,87,1,3))
if mibBuilder.loadTexts:dhcpClientOptTable.setStatus(_A)
_DhcpClientOptEntry_Object=MibTableRow
dhcpClientOptEntry=_DhcpClientOptEntry_Object((1,3,6,1,4,1,10876,101,1,87,1,3,1))
dhcpClientOptEntry.setIndexNames((0,_E,_J),(0,_E,_K))
if mibBuilder.loadTexts:dhcpClientOptEntry.setStatus(_A)
_DhcpClientOptIfIndex_Type=InterfaceIndex
_DhcpClientOptIfIndex_Object=MibTableColumn
dhcpClientOptIfIndex=_DhcpClientOptIfIndex_Object((1,3,6,1,4,1,10876,101,1,87,1,3,1,1),_DhcpClientOptIfIndex_Type())
dhcpClientOptIfIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:dhcpClientOptIfIndex.setStatus(_A)
class _DhcpClientOptType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,254))
_DhcpClientOptType_Type.__name__=_C
_DhcpClientOptType_Object=MibTableColumn
dhcpClientOptType=_DhcpClientOptType_Object((1,3,6,1,4,1,10876,101,1,87,1,3,1,2),_DhcpClientOptType_Type())
dhcpClientOptType.setMaxAccess(_H)
if mibBuilder.loadTexts:dhcpClientOptType.setStatus(_A)
class _DhcpClientOptLen_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_DhcpClientOptLen_Type.__name__=_C
_DhcpClientOptLen_Object=MibTableColumn
dhcpClientOptLen=_DhcpClientOptLen_Object((1,3,6,1,4,1,10876,101,1,87,1,3,1,3),_DhcpClientOptLen_Type())
dhcpClientOptLen.setMaxAccess(_B)
if mibBuilder.loadTexts:dhcpClientOptLen.setStatus(_A)
_DhcpClientOptVal_Type=OctetString
_DhcpClientOptVal_Object=MibTableColumn
dhcpClientOptVal=_DhcpClientOptVal_Object((1,3,6,1,4,1,10876,101,1,87,1,3,1,4),_DhcpClientOptVal_Type())
dhcpClientOptVal.setMaxAccess(_B)
if mibBuilder.loadTexts:dhcpClientOptVal.setStatus(_A)
_DhcpClientOptRowStatus_Type=RowStatus
_DhcpClientOptRowStatus_Object=MibTableColumn
dhcpClientOptRowStatus=_DhcpClientOptRowStatus_Object((1,3,6,1,4,1,10876,101,1,87,1,3,1,5),_DhcpClientOptRowStatus_Type())
dhcpClientOptRowStatus.setMaxAccess('read-create')
if mibBuilder.loadTexts:dhcpClientOptRowStatus.setStatus(_A)
class _DhcpClientFastAccess_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('enable',1),('disable',2)))
_DhcpClientFastAccess_Type.__name__=_C
_DhcpClientFastAccess_Object=MibScalar
dhcpClientFastAccess=_DhcpClientFastAccess_Object((1,3,6,1,4,1,10876,101,1,87,1,4),_DhcpClientFastAccess_Type())
dhcpClientFastAccess.setMaxAccess(_D)
if mibBuilder.loadTexts:dhcpClientFastAccess.setStatus(_A)
class _DhcpClientFastAccessDiscoverTimeOut_Type(Integer32):defaultValue=15;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_DhcpClientFastAccessDiscoverTimeOut_Type.__name__=_C
_DhcpClientFastAccessDiscoverTimeOut_Object=MibScalar
dhcpClientFastAccessDiscoverTimeOut=_DhcpClientFastAccessDiscoverTimeOut_Object((1,3,6,1,4,1,10876,101,1,87,1,5),_DhcpClientFastAccessDiscoverTimeOut_Type())
dhcpClientFastAccessDiscoverTimeOut.setMaxAccess(_D)
if mibBuilder.loadTexts:dhcpClientFastAccessDiscoverTimeOut.setStatus(_A)
class _DhcpClientFastAccessNullStateTimeOut_Type(Integer32):defaultValue=180;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_DhcpClientFastAccessNullStateTimeOut_Type.__name__=_C
_DhcpClientFastAccessNullStateTimeOut_Object=MibScalar
dhcpClientFastAccessNullStateTimeOut=_DhcpClientFastAccessNullStateTimeOut_Object((1,3,6,1,4,1,10876,101,1,87,1,6),_DhcpClientFastAccessNullStateTimeOut_Type())
dhcpClientFastAccessNullStateTimeOut.setMaxAccess(_D)
if mibBuilder.loadTexts:dhcpClientFastAccessNullStateTimeOut.setStatus(_A)
class _DhcpClientFastAccessArpCheckTimeOut_Type(Integer32):defaultValue=20;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,20))
_DhcpClientFastAccessArpCheckTimeOut_Type.__name__=_C
_DhcpClientFastAccessArpCheckTimeOut_Object=MibScalar
dhcpClientFastAccessArpCheckTimeOut=_DhcpClientFastAccessArpCheckTimeOut_Object((1,3,6,1,4,1,10876,101,1,87,1,7),_DhcpClientFastAccessArpCheckTimeOut_Type())
dhcpClientFastAccessArpCheckTimeOut.setMaxAccess(_D)
if mibBuilder.loadTexts:dhcpClientFastAccessArpCheckTimeOut.setStatus(_A)
_DhcpClientCounters_ObjectIdentity=ObjectIdentity
dhcpClientCounters=_DhcpClientCounters_ObjectIdentity((1,3,6,1,4,1,10876,101,1,87,2))
_DhcpClientCounterTable_Object=MibTable
dhcpClientCounterTable=_DhcpClientCounterTable_Object((1,3,6,1,4,1,10876,101,1,87,2,1))
if mibBuilder.loadTexts:dhcpClientCounterTable.setStatus(_A)
_DhcpClientCounterEntry_Object=MibTableRow
dhcpClientCounterEntry=_DhcpClientCounterEntry_Object((1,3,6,1,4,1,10876,101,1,87,2,1,1))
dhcpClientCounterEntry.setIndexNames((0,_E,_L))
if mibBuilder.loadTexts:dhcpClientCounterEntry.setStatus(_A)
class _DhcpClientIfIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_DhcpClientIfIndex_Type.__name__=_C
_DhcpClientIfIndex_Object=MibTableColumn
dhcpClientIfIndex=_DhcpClientIfIndex_Object((1,3,6,1,4,1,10876,101,1,87,2,1,1,1),_DhcpClientIfIndex_Type())
dhcpClientIfIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:dhcpClientIfIndex.setStatus(_A)
_DhcpClientCountDiscovers_Type=Counter32
_DhcpClientCountDiscovers_Object=MibTableColumn
dhcpClientCountDiscovers=_DhcpClientCountDiscovers_Object((1,3,6,1,4,1,10876,101,1,87,2,1,1,2),_DhcpClientCountDiscovers_Type())
dhcpClientCountDiscovers.setMaxAccess(_B)
if mibBuilder.loadTexts:dhcpClientCountDiscovers.setStatus(_A)
_DhcpClientCountRequests_Type=Counter32
_DhcpClientCountRequests_Object=MibTableColumn
dhcpClientCountRequests=_DhcpClientCountRequests_Object((1,3,6,1,4,1,10876,101,1,87,2,1,1,3),_DhcpClientCountRequests_Type())
dhcpClientCountRequests.setMaxAccess(_B)
if mibBuilder.loadTexts:dhcpClientCountRequests.setStatus(_A)
_DhcpClientCountReleases_Type=Counter32
_DhcpClientCountReleases_Object=MibTableColumn
dhcpClientCountReleases=_DhcpClientCountReleases_Object((1,3,6,1,4,1,10876,101,1,87,2,1,1,4),_DhcpClientCountReleases_Type())
dhcpClientCountReleases.setMaxAccess(_B)
if mibBuilder.loadTexts:dhcpClientCountReleases.setStatus(_A)
_DhcpClientCountDeclines_Type=Counter32
_DhcpClientCountDeclines_Object=MibTableColumn
dhcpClientCountDeclines=_DhcpClientCountDeclines_Object((1,3,6,1,4,1,10876,101,1,87,2,1,1,5),_DhcpClientCountDeclines_Type())
dhcpClientCountDeclines.setMaxAccess(_B)
if mibBuilder.loadTexts:dhcpClientCountDeclines.setStatus(_A)
_DhcpClientCountInforms_Type=Counter32
_DhcpClientCountInforms_Object=MibTableColumn
dhcpClientCountInforms=_DhcpClientCountInforms_Object((1,3,6,1,4,1,10876,101,1,87,2,1,1,6),_DhcpClientCountInforms_Type())
dhcpClientCountInforms.setMaxAccess(_B)
if mibBuilder.loadTexts:dhcpClientCountInforms.setStatus(_A)
_DhcpClientCountOffers_Type=Counter32
_DhcpClientCountOffers_Object=MibTableColumn
dhcpClientCountOffers=_DhcpClientCountOffers_Object((1,3,6,1,4,1,10876,101,1,87,2,1,1,7),_DhcpClientCountOffers_Type())
dhcpClientCountOffers.setMaxAccess(_B)
if mibBuilder.loadTexts:dhcpClientCountOffers.setStatus(_A)
_DhcpCountAcksInReqState_Type=Counter32
_DhcpCountAcksInReqState_Object=MibTableColumn
dhcpCountAcksInReqState=_DhcpCountAcksInReqState_Object((1,3,6,1,4,1,10876,101,1,87,2,1,1,8),_DhcpCountAcksInReqState_Type())
dhcpCountAcksInReqState.setMaxAccess(_B)
if mibBuilder.loadTexts:dhcpCountAcksInReqState.setStatus(_A)
_DhcpCountNacksInReqState_Type=Counter32
_DhcpCountNacksInReqState_Object=MibTableColumn
dhcpCountNacksInReqState=_DhcpCountNacksInReqState_Object((1,3,6,1,4,1,10876,101,1,87,2,1,1,9),_DhcpCountNacksInReqState_Type())
dhcpCountNacksInReqState.setMaxAccess(_B)
if mibBuilder.loadTexts:dhcpCountNacksInReqState.setStatus(_A)
_DhcpCountAcksInRenewState_Type=Counter32
_DhcpCountAcksInRenewState_Object=MibTableColumn
dhcpCountAcksInRenewState=_DhcpCountAcksInRenewState_Object((1,3,6,1,4,1,10876,101,1,87,2,1,1,10),_DhcpCountAcksInRenewState_Type())
dhcpCountAcksInRenewState.setMaxAccess(_B)
if mibBuilder.loadTexts:dhcpCountAcksInRenewState.setStatus(_A)
_DhcpCountNacksInRenewState_Type=Counter32
_DhcpCountNacksInRenewState_Object=MibTableColumn
dhcpCountNacksInRenewState=_DhcpCountNacksInRenewState_Object((1,3,6,1,4,1,10876,101,1,87,2,1,1,11),_DhcpCountNacksInRenewState_Type())
dhcpCountNacksInRenewState.setMaxAccess(_B)
if mibBuilder.loadTexts:dhcpCountNacksInRenewState.setStatus(_A)
_DhcpCountAcksInRebindState_Type=Counter32
_DhcpCountAcksInRebindState_Object=MibTableColumn
dhcpCountAcksInRebindState=_DhcpCountAcksInRebindState_Object((1,3,6,1,4,1,10876,101,1,87,2,1,1,12),_DhcpCountAcksInRebindState_Type())
dhcpCountAcksInRebindState.setMaxAccess(_B)
if mibBuilder.loadTexts:dhcpCountAcksInRebindState.setStatus(_A)
_DhcpCountNacksInRebindState_Type=Counter32
_DhcpCountNacksInRebindState_Object=MibTableColumn
dhcpCountNacksInRebindState=_DhcpCountNacksInRebindState_Object((1,3,6,1,4,1,10876,101,1,87,2,1,1,13),_DhcpCountNacksInRebindState_Type())
dhcpCountNacksInRebindState.setMaxAccess(_B)
if mibBuilder.loadTexts:dhcpCountNacksInRebindState.setStatus(_A)
_DhcpCountAcksInRebootState_Type=Counter32
_DhcpCountAcksInRebootState_Object=MibTableColumn
dhcpCountAcksInRebootState=_DhcpCountAcksInRebootState_Object((1,3,6,1,4,1,10876,101,1,87,2,1,1,14),_DhcpCountAcksInRebootState_Type())
dhcpCountAcksInRebootState.setMaxAccess(_B)
if mibBuilder.loadTexts:dhcpCountAcksInRebootState.setStatus(_A)
_DhcpCountNacksInRebootState_Type=Counter32
_DhcpCountNacksInRebootState_Object=MibTableColumn
dhcpCountNacksInRebootState=_DhcpCountNacksInRebootState_Object((1,3,6,1,4,1,10876,101,1,87,2,1,1,15),_DhcpCountNacksInRebootState_Type())
dhcpCountNacksInRebootState.setMaxAccess(_B)
if mibBuilder.loadTexts:dhcpCountNacksInRebootState.setStatus(_A)
_DhcpCountErrorInHeader_Type=Counter32
_DhcpCountErrorInHeader_Object=MibTableColumn
dhcpCountErrorInHeader=_DhcpCountErrorInHeader_Object((1,3,6,1,4,1,10876,101,1,87,2,1,1,16),_DhcpCountErrorInHeader_Type())
dhcpCountErrorInHeader.setMaxAccess(_B)
if mibBuilder.loadTexts:dhcpCountErrorInHeader.setStatus(_A)
_DhcpCountErrorInXid_Type=Counter32
_DhcpCountErrorInXid_Object=MibTableColumn
dhcpCountErrorInXid=_DhcpCountErrorInXid_Object((1,3,6,1,4,1,10876,101,1,87,2,1,1,17),_DhcpCountErrorInXid_Type())
dhcpCountErrorInXid.setMaxAccess(_B)
if mibBuilder.loadTexts:dhcpCountErrorInXid.setStatus(_A)
_DhcpCountErrorInOptions_Type=Counter32
_DhcpCountErrorInOptions_Object=MibTableColumn
dhcpCountErrorInOptions=_DhcpCountErrorInOptions_Object((1,3,6,1,4,1,10876,101,1,87,2,1,1,18),_DhcpCountErrorInOptions_Type())
dhcpCountErrorInOptions.setMaxAccess(_B)
if mibBuilder.loadTexts:dhcpCountErrorInOptions.setStatus(_A)
_DhcpClientIpAddress_Type=IpAddress
_DhcpClientIpAddress_Object=MibTableColumn
dhcpClientIpAddress=_DhcpClientIpAddress_Object((1,3,6,1,4,1,10876,101,1,87,2,1,1,19),_DhcpClientIpAddress_Type())
dhcpClientIpAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:dhcpClientIpAddress.setStatus(_A)
_DhcpClientLeaseTime_Type=Integer32
_DhcpClientLeaseTime_Object=MibTableColumn
dhcpClientLeaseTime=_DhcpClientLeaseTime_Object((1,3,6,1,4,1,10876,101,1,87,2,1,1,20),_DhcpClientLeaseTime_Type())
dhcpClientLeaseTime.setMaxAccess(_B)
if mibBuilder.loadTexts:dhcpClientLeaseTime.setStatus(_A)
class _DhcpClientCounterReset_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_DhcpClientCounterReset_Type.__name__=_C
_DhcpClientCounterReset_Object=MibTableColumn
dhcpClientCounterReset=_DhcpClientCounterReset_Object((1,3,6,1,4,1,10876,101,1,87,2,1,1,21),_DhcpClientCounterReset_Type())
dhcpClientCounterReset.setMaxAccess(_D)
if mibBuilder.loadTexts:dhcpClientCounterReset.setStatus(_A)
_DhcpClientRemainLeaseTime_Type=Integer32
_DhcpClientRemainLeaseTime_Object=MibTableColumn
dhcpClientRemainLeaseTime=_DhcpClientRemainLeaseTime_Object((1,3,6,1,4,1,10876,101,1,87,2,1,1,22),_DhcpClientRemainLeaseTime_Type())
dhcpClientRemainLeaseTime.setMaxAccess(_B)
if mibBuilder.loadTexts:dhcpClientRemainLeaseTime.setStatus(_A)
mibBuilder.exportSymbols(_E,**{'futureDhcpClientMIB':futureDhcpClientMIB,'dhcpClientConfig':dhcpClientConfig,'dhcpClientConfigTable':dhcpClientConfigTable,'dhcpClientConfigEntry':dhcpClientConfigEntry,_I:dhcpClientConfigIfIndex,'dhcpClientRenew':dhcpClientRenew,'dhcpClientRebind':dhcpClientRebind,'dhcpClientInform':dhcpClientInform,'dhcpClientRelease':dhcpClientRelease,'dhcpClientIdentifier':dhcpClientIdentifier,'dhcpClientDebugTrace':dhcpClientDebugTrace,'dhcpClientOptTable':dhcpClientOptTable,'dhcpClientOptEntry':dhcpClientOptEntry,_J:dhcpClientOptIfIndex,_K:dhcpClientOptType,'dhcpClientOptLen':dhcpClientOptLen,'dhcpClientOptVal':dhcpClientOptVal,'dhcpClientOptRowStatus':dhcpClientOptRowStatus,'dhcpClientFastAccess':dhcpClientFastAccess,'dhcpClientFastAccessDiscoverTimeOut':dhcpClientFastAccessDiscoverTimeOut,'dhcpClientFastAccessNullStateTimeOut':dhcpClientFastAccessNullStateTimeOut,'dhcpClientFastAccessArpCheckTimeOut':dhcpClientFastAccessArpCheckTimeOut,'dhcpClientCounters':dhcpClientCounters,'dhcpClientCounterTable':dhcpClientCounterTable,'dhcpClientCounterEntry':dhcpClientCounterEntry,_L:dhcpClientIfIndex,'dhcpClientCountDiscovers':dhcpClientCountDiscovers,'dhcpClientCountRequests':dhcpClientCountRequests,'dhcpClientCountReleases':dhcpClientCountReleases,'dhcpClientCountDeclines':dhcpClientCountDeclines,'dhcpClientCountInforms':dhcpClientCountInforms,'dhcpClientCountOffers':dhcpClientCountOffers,'dhcpCountAcksInReqState':dhcpCountAcksInReqState,'dhcpCountNacksInReqState':dhcpCountNacksInReqState,'dhcpCountAcksInRenewState':dhcpCountAcksInRenewState,'dhcpCountNacksInRenewState':dhcpCountNacksInRenewState,'dhcpCountAcksInRebindState':dhcpCountAcksInRebindState,'dhcpCountNacksInRebindState':dhcpCountNacksInRebindState,'dhcpCountAcksInRebootState':dhcpCountAcksInRebootState,'dhcpCountNacksInRebootState':dhcpCountNacksInRebootState,'dhcpCountErrorInHeader':dhcpCountErrorInHeader,'dhcpCountErrorInXid':dhcpCountErrorInXid,'dhcpCountErrorInOptions':dhcpCountErrorInOptions,'dhcpClientIpAddress':dhcpClientIpAddress,'dhcpClientLeaseTime':dhcpClientLeaseTime,'dhcpClientCounterReset':dhcpClientCounterReset,'dhcpClientRemainLeaseTime':dhcpClientRemainLeaseTime})