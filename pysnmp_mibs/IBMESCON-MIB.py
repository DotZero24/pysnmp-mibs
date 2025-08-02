_P='esconStationDeviceAddress'
_O='esconStationPartitionNumber'
_N='esconStationHostLinkAddress'
_M='esconLinkPartitionNumber'
_L='esconLinkHostLinkAddress'
_K='IpAddress'
_J='Counter32'
_I='read-write'
_H='ifIndex'
_G='IF-MIB'
_F='not-accessible'
_E='IBMESCON-MIB'
_D='OctetString'
_C='Integer32'
_B='read-only'
_A='mandatory'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_D,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ifIndex,=mibBuilder.importSymbols(_G,_H)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits',_J,'Counter64','Gauge32',_C,_K,'ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
Counter32,Integer32,IpAddress,enterprises=mibBuilder.importSymbols('SNMPv2-SMI-v1',_J,_C,_K,'enterprises')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
MacAddress,=mibBuilder.importSymbols('SNMPv2-TC-v1','MacAddress')
_Ibm_ObjectIdentity=ObjectIdentity
ibm=_Ibm_ObjectIdentity((1,3,6,1,4,1,2))
_IbmArchitecture_ObjectIdentity=ObjectIdentity
ibmArchitecture=_IbmArchitecture_ObjectIdentity((1,3,6,1,4,1,2,5))
_IbmESCON_ObjectIdentity=ObjectIdentity
ibmESCON=_IbmESCON_ObjectIdentity((1,3,6,1,4,1,2,5,17))
_EsconPortData_ObjectIdentity=ObjectIdentity
esconPortData=_EsconPortData_ObjectIdentity((1,3,6,1,4,1,2,5,17,1))
_EsconPortTable_Object=MibTable
esconPortTable=_EsconPortTable_Object((1,3,6,1,4,1,2,5,17,1,1))
if mibBuilder.loadTexts:esconPortTable.setStatus(_A)
_EsconPortEntry_Object=MibTableRow
esconPortEntry=_EsconPortEntry_Object((1,3,6,1,4,1,2,5,17,1,1,1))
esconPortEntry.setIndexNames((0,_G,_H))
if mibBuilder.loadTexts:esconPortEntry.setStatus(_A)
class _EsconPortControlUnitLinkAddress_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(2,2));fixedLength=2
_EsconPortControlUnitLinkAddress_Type.__name__=_D
_EsconPortControlUnitLinkAddress_Object=MibTableColumn
esconPortControlUnitLinkAddress=_EsconPortControlUnitLinkAddress_Object((1,3,6,1,4,1,2,5,17,1,1,1,1),_EsconPortControlUnitLinkAddress_Type())
esconPortControlUnitLinkAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:esconPortControlUnitLinkAddress.setStatus(_A)
class _EsconPortInFiberStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('inLoff',1),('inOls',2),('inIdle',3),('inUnknown',4)))
_EsconPortInFiberStatus_Type.__name__=_C
_EsconPortInFiberStatus_Object=MibTableColumn
esconPortInFiberStatus=_EsconPortInFiberStatus_Object((1,3,6,1,4,1,2,5,17,1,1,1,2),_EsconPortInFiberStatus_Type())
esconPortInFiberStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:esconPortInFiberStatus.setStatus(_A)
class _EsconPortOutFiberStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*(('outDisableReq',1),('outDisableForced',2),('outLoffForced',3),('outOls',4),('outOlsForced',5),('outEnable',6),('outError',7)))
_EsconPortOutFiberStatus_Type.__name__=_C
_EsconPortOutFiberStatus_Object=MibTableColumn
esconPortOutFiberStatus=_EsconPortOutFiberStatus_Object((1,3,6,1,4,1,2,5,17,1,1,1,3),_EsconPortOutFiberStatus_Type())
esconPortOutFiberStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:esconPortOutFiberStatus.setStatus(_A)
_EsconLinkData_ObjectIdentity=ObjectIdentity
esconLinkData=_EsconLinkData_ObjectIdentity((1,3,6,1,4,1,2,5,17,2))
_EsconLinkTable_Object=MibTable
esconLinkTable=_EsconLinkTable_Object((1,3,6,1,4,1,2,5,17,2,1))
if mibBuilder.loadTexts:esconLinkTable.setStatus(_A)
_EsconLinkEntry_Object=MibTableRow
esconLinkEntry=_EsconLinkEntry_Object((1,3,6,1,4,1,2,5,17,2,1,1))
esconLinkEntry.setIndexNames((0,_G,_H),(0,_E,_L),(0,_E,_M))
if mibBuilder.loadTexts:esconLinkEntry.setStatus(_A)
class _EsconLinkHostLinkAddress_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,1));fixedLength=1
_EsconLinkHostLinkAddress_Type.__name__=_D
_EsconLinkHostLinkAddress_Object=MibTableColumn
esconLinkHostLinkAddress=_EsconLinkHostLinkAddress_Object((1,3,6,1,4,1,2,5,17,2,1,1,1),_EsconLinkHostLinkAddress_Type())
esconLinkHostLinkAddress.setMaxAccess(_F)
if mibBuilder.loadTexts:esconLinkHostLinkAddress.setStatus(_A)
class _EsconLinkPartitionNumber_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,1));fixedLength=1
_EsconLinkPartitionNumber_Type.__name__=_D
_EsconLinkPartitionNumber_Object=MibTableColumn
esconLinkPartitionNumber=_EsconLinkPartitionNumber_Object((1,3,6,1,4,1,2,5,17,2,1,1,2),_EsconLinkPartitionNumber_Type())
esconLinkPartitionNumber.setMaxAccess(_F)
if mibBuilder.loadTexts:esconLinkPartitionNumber.setStatus(_A)
class _EsconLinkStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('hlpNotEstab',1),('hlpEstab',2),('hlpError',3)))
_EsconLinkStatus_Type.__name__=_C
_EsconLinkStatus_Object=MibTableColumn
esconLinkStatus=_EsconLinkStatus_Object((1,3,6,1,4,1,2,5,17,2,1,1,3),_EsconLinkStatus_Type())
esconLinkStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:esconLinkStatus.setStatus(_A)
_EsconStationData_ObjectIdentity=ObjectIdentity
esconStationData=_EsconStationData_ObjectIdentity((1,3,6,1,4,1,2,5,17,3))
_EsconStationTable_Object=MibTable
esconStationTable=_EsconStationTable_Object((1,3,6,1,4,1,2,5,17,3,1))
if mibBuilder.loadTexts:esconStationTable.setStatus(_A)
_EsconStationEntry_Object=MibTableRow
esconStationEntry=_EsconStationEntry_Object((1,3,6,1,4,1,2,5,17,3,1,1))
esconStationEntry.setIndexNames((0,_G,_H),(0,_E,_N),(0,_E,_O),(0,_E,_P))
if mibBuilder.loadTexts:esconStationEntry.setStatus(_A)
class _EsconStationHostLinkAddress_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,1));fixedLength=1
_EsconStationHostLinkAddress_Type.__name__=_D
_EsconStationHostLinkAddress_Object=MibTableColumn
esconStationHostLinkAddress=_EsconStationHostLinkAddress_Object((1,3,6,1,4,1,2,5,17,3,1,1,1),_EsconStationHostLinkAddress_Type())
esconStationHostLinkAddress.setMaxAccess(_F)
if mibBuilder.loadTexts:esconStationHostLinkAddress.setStatus(_A)
class _EsconStationPartitionNumber_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,1));fixedLength=1
_EsconStationPartitionNumber_Type.__name__=_D
_EsconStationPartitionNumber_Object=MibTableColumn
esconStationPartitionNumber=_EsconStationPartitionNumber_Object((1,3,6,1,4,1,2,5,17,3,1,1,2),_EsconStationPartitionNumber_Type())
esconStationPartitionNumber.setMaxAccess(_F)
if mibBuilder.loadTexts:esconStationPartitionNumber.setStatus(_A)
class _EsconStationDeviceAddress_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,1));fixedLength=1
_EsconStationDeviceAddress_Type.__name__=_D
_EsconStationDeviceAddress_Object=MibTableColumn
esconStationDeviceAddress=_EsconStationDeviceAddress_Object((1,3,6,1,4,1,2,5,17,3,1,1,3),_EsconStationDeviceAddress_Type())
esconStationDeviceAddress.setMaxAccess(_F)
if mibBuilder.loadTexts:esconStationDeviceAddress.setStatus(_A)
class _EsconStationState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14)));namedValues=NamedValues(*(('idle',1),('cpDefined',2),('cpReset',3),('cpActive',4),('cpDelete',5),('cpAbend',6),('cldpWait',7),('cldpDefinedl',8),('cldpError',9),('cldpLoad',10),('cldpDump',11),('deletePending',12),('deleted',13),('cpXidExpected',14)))
_EsconStationState_Type.__name__=_C
_EsconStationState_Object=MibTableColumn
esconStationState=_EsconStationState_Object((1,3,6,1,4,1,2,5,17,3,1,1,4),_EsconStationState_Type())
esconStationState.setMaxAccess(_B)
if mibBuilder.loadTexts:esconStationState.setStatus(_A)
class _EsconStationAttentionDelay_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,420))
_EsconStationAttentionDelay_Type.__name__=_C
_EsconStationAttentionDelay_Object=MibTableColumn
esconStationAttentionDelay=_EsconStationAttentionDelay_Object((1,3,6,1,4,1,2,5,17,3,1,1,5),_EsconStationAttentionDelay_Type())
esconStationAttentionDelay.setMaxAccess(_I)
if mibBuilder.loadTexts:esconStationAttentionDelay.setStatus(_A)
class _EsconStationAttentionTimeOut_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(10,840))
_EsconStationAttentionTimeOut_Type.__name__=_C
_EsconStationAttentionTimeOut_Object=MibTableColumn
esconStationAttentionTimeOut=_EsconStationAttentionTimeOut_Object((1,3,6,1,4,1,2,5,17,3,1,1,6),_EsconStationAttentionTimeOut_Type())
esconStationAttentionTimeOut.setMaxAccess(_I)
if mibBuilder.loadTexts:esconStationAttentionTimeOut.setStatus(_A)
class _EsconStationMaxBfru_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_EsconStationMaxBfru_Type.__name__=_C
_EsconStationMaxBfru_Object=MibTableColumn
esconStationMaxBfru=_EsconStationMaxBfru_Object((1,3,6,1,4,1,2,5,17,3,1,1,7),_EsconStationMaxBfru_Type())
esconStationMaxBfru.setMaxAccess(_B)
if mibBuilder.loadTexts:esconStationMaxBfru.setStatus(_A)
class _EsconStationUnitSize_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(64,4000))
_EsconStationUnitSize_Type.__name__=_C
_EsconStationUnitSize_Object=MibTableColumn
esconStationUnitSize=_EsconStationUnitSize_Object((1,3,6,1,4,1,2,5,17,3,1,1,8),_EsconStationUnitSize_Type())
esconStationUnitSize.setMaxAccess(_B)
if mibBuilder.loadTexts:esconStationUnitSize.setStatus(_A)
class _EsconStationMaxMsgSizeReceived_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_EsconStationMaxMsgSizeReceived_Type.__name__=_C
_EsconStationMaxMsgSizeReceived_Object=MibTableColumn
esconStationMaxMsgSizeReceived=_EsconStationMaxMsgSizeReceived_Object((1,3,6,1,4,1,2,5,17,3,1,1,9),_EsconStationMaxMsgSizeReceived_Type())
esconStationMaxMsgSizeReceived.setMaxAccess(_I)
if mibBuilder.loadTexts:esconStationMaxMsgSizeReceived.setStatus(_A)
class _EsconStationMaxMsgSizeSent_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_EsconStationMaxMsgSizeSent_Type.__name__=_C
_EsconStationMaxMsgSizeSent_Object=MibTableColumn
esconStationMaxMsgSizeSent=_EsconStationMaxMsgSizeSent_Object((1,3,6,1,4,1,2,5,17,3,1,1,10),_EsconStationMaxMsgSizeSent_Type())
esconStationMaxMsgSizeSent.setMaxAccess(_I)
if mibBuilder.loadTexts:esconStationMaxMsgSizeSent.setStatus(_A)
_EsconStationDataPacketsOkReceived_Type=Counter32
_EsconStationDataPacketsOkReceived_Object=MibTableColumn
esconStationDataPacketsOkReceived=_EsconStationDataPacketsOkReceived_Object((1,3,6,1,4,1,2,5,17,3,1,1,11),_EsconStationDataPacketsOkReceived_Type())
esconStationDataPacketsOkReceived.setMaxAccess(_B)
if mibBuilder.loadTexts:esconStationDataPacketsOkReceived.setStatus(_A)
_EsconStationDataPacketsKoReceived_Type=Counter32
_EsconStationDataPacketsKoReceived_Object=MibTableColumn
esconStationDataPacketsKoReceived=_EsconStationDataPacketsKoReceived_Object((1,3,6,1,4,1,2,5,17,3,1,1,12),_EsconStationDataPacketsKoReceived_Type())
esconStationDataPacketsKoReceived.setMaxAccess(_B)
if mibBuilder.loadTexts:esconStationDataPacketsKoReceived.setStatus(_A)
_EsconStationDataPacketsSent_Type=Counter32
_EsconStationDataPacketsSent_Object=MibTableColumn
esconStationDataPacketsSent=_EsconStationDataPacketsSent_Object((1,3,6,1,4,1,2,5,17,3,1,1,13),_EsconStationDataPacketsSent_Type())
esconStationDataPacketsSent.setMaxAccess(_B)
if mibBuilder.loadTexts:esconStationDataPacketsSent.setStatus(_A)
_EsconStationTotalFramesSent_Type=Counter32
_EsconStationTotalFramesSent_Object=MibTableColumn
esconStationTotalFramesSent=_EsconStationTotalFramesSent_Object((1,3,6,1,4,1,2,5,17,3,1,1,14),_EsconStationTotalFramesSent_Type())
esconStationTotalFramesSent.setMaxAccess(_B)
if mibBuilder.loadTexts:esconStationTotalFramesSent.setStatus(_A)
_EsconStationDataPacketsRetransmitted_Type=Counter32
_EsconStationDataPacketsRetransmitted_Object=MibTableColumn
esconStationDataPacketsRetransmitted=_EsconStationDataPacketsRetransmitted_Object((1,3,6,1,4,1,2,5,17,3,1,1,15),_EsconStationDataPacketsRetransmitted_Type())
esconStationDataPacketsRetransmitted.setMaxAccess(_B)
if mibBuilder.loadTexts:esconStationDataPacketsRetransmitted.setStatus(_A)
_EsconStationPositiveAckDataPackets_Type=Counter32
_EsconStationPositiveAckDataPackets_Object=MibTableColumn
esconStationPositiveAckDataPackets=_EsconStationPositiveAckDataPackets_Object((1,3,6,1,4,1,2,5,17,3,1,1,16),_EsconStationPositiveAckDataPackets_Type())
esconStationPositiveAckDataPackets.setMaxAccess(_B)
if mibBuilder.loadTexts:esconStationPositiveAckDataPackets.setStatus(_A)
_EsconStationSecondChanceAttentions_Type=Counter32
_EsconStationSecondChanceAttentions_Object=MibTableColumn
esconStationSecondChanceAttentions=_EsconStationSecondChanceAttentions_Object((1,3,6,1,4,1,2,5,17,3,1,1,17),_EsconStationSecondChanceAttentions_Type())
esconStationSecondChanceAttentions.setMaxAccess(_B)
if mibBuilder.loadTexts:esconStationSecondChanceAttentions.setStatus(_A)
_EsconStationCommandsRetried_Type=Counter32
_EsconStationCommandsRetried_Object=MibTableColumn
esconStationCommandsRetried=_EsconStationCommandsRetried_Object((1,3,6,1,4,1,2,5,17,3,1,1,18),_EsconStationCommandsRetried_Type())
esconStationCommandsRetried.setMaxAccess(_B)
if mibBuilder.loadTexts:esconStationCommandsRetried.setStatus(_A)
_EsconConformance_ObjectIdentity=ObjectIdentity
esconConformance=_EsconConformance_ObjectIdentity((1,3,6,1,4,1,2,5,17,4))
_EsconMibCompliances_ObjectIdentity=ObjectIdentity
esconMibCompliances=_EsconMibCompliances_ObjectIdentity((1,3,6,1,4,1,2,5,17,4,1))
_EsconMibCompliance_ObjectIdentity=ObjectIdentity
esconMibCompliance=_EsconMibCompliance_ObjectIdentity((1,3,6,1,4,1,2,5,17,4,1,1))
_EsconMibGroups_ObjectIdentity=ObjectIdentity
esconMibGroups=_EsconMibGroups_ObjectIdentity((1,3,6,1,4,1,2,5,17,4,2))
_EsconPortGroup_ObjectIdentity=ObjectIdentity
esconPortGroup=_EsconPortGroup_ObjectIdentity((1,3,6,1,4,1,2,5,17,4,2,1))
_EsconLinkGroup_ObjectIdentity=ObjectIdentity
esconLinkGroup=_EsconLinkGroup_ObjectIdentity((1,3,6,1,4,1,2,5,17,4,2,2))
_EsconStationGroup_ObjectIdentity=ObjectIdentity
esconStationGroup=_EsconStationGroup_ObjectIdentity((1,3,6,1,4,1,2,5,17,4,2,3))
mibBuilder.exportSymbols(_E,**{'ibm':ibm,'ibmArchitecture':ibmArchitecture,'ibmESCON':ibmESCON,'esconPortData':esconPortData,'esconPortTable':esconPortTable,'esconPortEntry':esconPortEntry,'esconPortControlUnitLinkAddress':esconPortControlUnitLinkAddress,'esconPortInFiberStatus':esconPortInFiberStatus,'esconPortOutFiberStatus':esconPortOutFiberStatus,'esconLinkData':esconLinkData,'esconLinkTable':esconLinkTable,'esconLinkEntry':esconLinkEntry,_L:esconLinkHostLinkAddress,_M:esconLinkPartitionNumber,'esconLinkStatus':esconLinkStatus,'esconStationData':esconStationData,'esconStationTable':esconStationTable,'esconStationEntry':esconStationEntry,_N:esconStationHostLinkAddress,_O:esconStationPartitionNumber,_P:esconStationDeviceAddress,'esconStationState':esconStationState,'esconStationAttentionDelay':esconStationAttentionDelay,'esconStationAttentionTimeOut':esconStationAttentionTimeOut,'esconStationMaxBfru':esconStationMaxBfru,'esconStationUnitSize':esconStationUnitSize,'esconStationMaxMsgSizeReceived':esconStationMaxMsgSizeReceived,'esconStationMaxMsgSizeSent':esconStationMaxMsgSizeSent,'esconStationDataPacketsOkReceived':esconStationDataPacketsOkReceived,'esconStationDataPacketsKoReceived':esconStationDataPacketsKoReceived,'esconStationDataPacketsSent':esconStationDataPacketsSent,'esconStationTotalFramesSent':esconStationTotalFramesSent,'esconStationDataPacketsRetransmitted':esconStationDataPacketsRetransmitted,'esconStationPositiveAckDataPackets':esconStationPositiveAckDataPackets,'esconStationSecondChanceAttentions':esconStationSecondChanceAttentions,'esconStationCommandsRetried':esconStationCommandsRetried,'esconConformance':esconConformance,'esconMibCompliances':esconMibCompliances,'esconMibCompliance':esconMibCompliance,'esconMibGroups':esconMibGroups,'esconPortGroup':esconPortGroup,'esconLinkGroup':esconLinkGroup,'esconStationGroup':esconStationGroup})