_A0='cLLinkTestStatusGroup'
_z='cLLinkTestRunsGroup'
_y='cLLinkTestConfigGroup'
_x='cLLtClientLtRateUplinkPktsSent'
_w='cLLtClientLtRateDownlinkPktsSent'
_v='cLLtClientLtRowStatus'
_u='cLLtClientLtStatus'
_t='cLLtClientLtMaxTxRetriesClient'
_s='cLLtClientLtTotalTxRetriesClient'
_r='cLLtClientLtMaxTxRetriesAP'
_q='cLLtClientLtTotalTxRetriesAP'
_p='cLLtClientLtDownlinkAvgSNR'
_o='cLLtClientLtDownlinkMaxSNR'
_n='cLLtClientLtDownlinkMinSNR'
_m='cLLtClientLtUplinkAvgSNR'
_l='cLLtClientLtUplinkMaxSNR'
_k='cLLtClientLtUplinkMinSNR'
_j='cLLtClientLtDownlinkAvgRSSI'
_i='cLLtClientLtDownlinkMaxRSSI'
_h='cLLtClientLtDownlinkMinRSSI'
_g='cLLtClientLtUplinkAvgRSSI'
_f='cLLtClientLtUplinkMaxRSSI'
_e='cLLtClientLtUplinkMinRSSI'
_d='cLLtClientLtAvgRoundTripTime'
_c='cLLtClientLtMaxRoundTripTime'
_b='cLLtClientLtMinRoundTripTime'
_a='cLLtClientLtClientToApPktsLost'
_Z='cLLtClientLtApToClientPktsLost'
_Y='cLLtClientLtTotalPacketsLost'
_X='cLLtClientLtPacketsRx'
_W='cLLtClientLtPacketsSent'
_V='cLLtClientLtMacAddress'
_U='cLLtTestPurgeTime'
_T='cLLtNumberOfPackets'
_S='cLLtPacketSize'
_R='cLLtResponder'
_Q='cLLtClientLtDataRate'
_P='read-create'
_O='not-accessible'
_N='TruthValue'
_M='Integer32'
_L='OctetString'
_K='hundredths-seconds'
_J='retries'
_I='cLLtClientLtIndex'
_H='read-write'
_G='Unsigned32'
_F='dB'
_E='dBm'
_D='packets'
_C='read-only'
_B='CISCO-LWAPP-LINKTEST-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_L,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_M,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_G,'iso')
DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention,TimeInterval,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress','RowStatus','TextualConvention','TimeInterval',_N)
ciscoLwappLinkTestMIB=ModuleIdentity((1,3,6,1,4,1,9,9,516))
if mibBuilder.loadTexts:ciscoLwappLinkTestMIB.setRevisions(('2006-04-06 00:00',))
_CiscoLwappLinkTestMIBNotifs_ObjectIdentity=ObjectIdentity
ciscoLwappLinkTestMIBNotifs=_CiscoLwappLinkTestMIBNotifs_ObjectIdentity((1,3,6,1,4,1,9,9,516,0))
_CiscoLwappLinkTestMIBObjects_ObjectIdentity=ObjectIdentity
ciscoLwappLinkTestMIBObjects=_CiscoLwappLinkTestMIBObjects_ObjectIdentity((1,3,6,1,4,1,9,9,516,1))
_CiscoLwappLinkTestConfig_ObjectIdentity=ObjectIdentity
ciscoLwappLinkTestConfig=_CiscoLwappLinkTestConfig_ObjectIdentity((1,3,6,1,4,1,9,9,516,1,1))
class _CLLtResponder_Type(TruthValue):defaultValue=1
_CLLtResponder_Type.__name__=_N
_CLLtResponder_Object=MibScalar
cLLtResponder=_CLLtResponder_Object((1,3,6,1,4,1,9,9,516,1,1,1),_CLLtResponder_Type())
cLLtResponder.setMaxAccess(_H)
if mibBuilder.loadTexts:cLLtResponder.setStatus(_A)
class _CLLtPacketSize_Type(Unsigned32):defaultValue=50;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1500))
_CLLtPacketSize_Type.__name__=_G
_CLLtPacketSize_Object=MibScalar
cLLtPacketSize=_CLLtPacketSize_Object((1,3,6,1,4,1,9,9,516,1,1,2),_CLLtPacketSize_Type())
cLLtPacketSize.setMaxAccess(_H)
if mibBuilder.loadTexts:cLLtPacketSize.setStatus(_A)
class _CLLtNumberOfPackets_Type(Unsigned32):defaultValue=20;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,100))
_CLLtNumberOfPackets_Type.__name__=_G
_CLLtNumberOfPackets_Object=MibScalar
cLLtNumberOfPackets=_CLLtNumberOfPackets_Object((1,3,6,1,4,1,9,9,516,1,1,3),_CLLtNumberOfPackets_Type())
cLLtNumberOfPackets.setMaxAccess(_H)
if mibBuilder.loadTexts:cLLtNumberOfPackets.setStatus(_A)
class _CLLtTestPurgeTime_Type(Unsigned32):defaultValue=15;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(15,1800))
_CLLtTestPurgeTime_Type.__name__=_G
_CLLtTestPurgeTime_Object=MibScalar
cLLtTestPurgeTime=_CLLtTestPurgeTime_Object((1,3,6,1,4,1,9,9,516,1,1,4),_CLLtTestPurgeTime_Type())
cLLtTestPurgeTime.setMaxAccess(_H)
if mibBuilder.loadTexts:cLLtTestPurgeTime.setStatus(_A)
if mibBuilder.loadTexts:cLLtTestPurgeTime.setUnits('seconds')
_CiscoLwappLinkTestRun_ObjectIdentity=ObjectIdentity
ciscoLwappLinkTestRun=_CiscoLwappLinkTestRun_ObjectIdentity((1,3,6,1,4,1,9,9,516,1,2))
_CLLtClientLinkTestTable_Object=MibTable
cLLtClientLinkTestTable=_CLLtClientLinkTestTable_Object((1,3,6,1,4,1,9,9,516,1,2,1))
if mibBuilder.loadTexts:cLLtClientLinkTestTable.setStatus(_A)
_CLLtClientLinkTestEntry_Object=MibTableRow
cLLtClientLinkTestEntry=_CLLtClientLinkTestEntry_Object((1,3,6,1,4,1,9,9,516,1,2,1,1))
cLLtClientLinkTestEntry.setIndexNames((0,_B,_I))
if mibBuilder.loadTexts:cLLtClientLinkTestEntry.setStatus(_A)
class _CLLtClientLtIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,32))
_CLLtClientLtIndex_Type.__name__=_G
_CLLtClientLtIndex_Object=MibTableColumn
cLLtClientLtIndex=_CLLtClientLtIndex_Object((1,3,6,1,4,1,9,9,516,1,2,1,1,1),_CLLtClientLtIndex_Type())
cLLtClientLtIndex.setMaxAccess(_O)
if mibBuilder.loadTexts:cLLtClientLtIndex.setStatus(_A)
_CLLtClientLtMacAddress_Type=MacAddress
_CLLtClientLtMacAddress_Object=MibTableColumn
cLLtClientLtMacAddress=_CLLtClientLtMacAddress_Object((1,3,6,1,4,1,9,9,516,1,2,1,1,2),_CLLtClientLtMacAddress_Type())
cLLtClientLtMacAddress.setMaxAccess(_P)
if mibBuilder.loadTexts:cLLtClientLtMacAddress.setStatus(_A)
_CLLtClientLtRowStatus_Type=RowStatus
_CLLtClientLtRowStatus_Object=MibTableColumn
cLLtClientLtRowStatus=_CLLtClientLtRowStatus_Object((1,3,6,1,4,1,9,9,516,1,2,1,1,3),_CLLtClientLtRowStatus_Type())
cLLtClientLtRowStatus.setMaxAccess(_P)
if mibBuilder.loadTexts:cLLtClientLtRowStatus.setStatus(_A)
_CLLtClientLTResultsTable_Object=MibTable
cLLtClientLTResultsTable=_CLLtClientLTResultsTable_Object((1,3,6,1,4,1,9,9,516,1,2,2))
if mibBuilder.loadTexts:cLLtClientLTResultsTable.setStatus(_A)
_CLLtClientLTResultsEntry_Object=MibTableRow
cLLtClientLTResultsEntry=_CLLtClientLTResultsEntry_Object((1,3,6,1,4,1,9,9,516,1,2,2,1))
cLLtClientLTResultsEntry.setIndexNames((0,_B,_I))
if mibBuilder.loadTexts:cLLtClientLTResultsEntry.setStatus(_A)
_CLLtClientLtPacketsSent_Type=Counter32
_CLLtClientLtPacketsSent_Object=MibTableColumn
cLLtClientLtPacketsSent=_CLLtClientLtPacketsSent_Object((1,3,6,1,4,1,9,9,516,1,2,2,1,1),_CLLtClientLtPacketsSent_Type())
cLLtClientLtPacketsSent.setMaxAccess(_C)
if mibBuilder.loadTexts:cLLtClientLtPacketsSent.setStatus(_A)
if mibBuilder.loadTexts:cLLtClientLtPacketsSent.setUnits(_D)
_CLLtClientLtPacketsRx_Type=Counter32
_CLLtClientLtPacketsRx_Object=MibTableColumn
cLLtClientLtPacketsRx=_CLLtClientLtPacketsRx_Object((1,3,6,1,4,1,9,9,516,1,2,2,1,2),_CLLtClientLtPacketsRx_Type())
cLLtClientLtPacketsRx.setMaxAccess(_C)
if mibBuilder.loadTexts:cLLtClientLtPacketsRx.setStatus(_A)
if mibBuilder.loadTexts:cLLtClientLtPacketsRx.setUnits(_D)
_CLLtClientLtTotalPacketsLost_Type=Counter32
_CLLtClientLtTotalPacketsLost_Object=MibTableColumn
cLLtClientLtTotalPacketsLost=_CLLtClientLtTotalPacketsLost_Object((1,3,6,1,4,1,9,9,516,1,2,2,1,3),_CLLtClientLtTotalPacketsLost_Type())
cLLtClientLtTotalPacketsLost.setMaxAccess(_C)
if mibBuilder.loadTexts:cLLtClientLtTotalPacketsLost.setStatus(_A)
if mibBuilder.loadTexts:cLLtClientLtTotalPacketsLost.setUnits(_D)
_CLLtClientLtApToClientPktsLost_Type=Counter32
_CLLtClientLtApToClientPktsLost_Object=MibTableColumn
cLLtClientLtApToClientPktsLost=_CLLtClientLtApToClientPktsLost_Object((1,3,6,1,4,1,9,9,516,1,2,2,1,4),_CLLtClientLtApToClientPktsLost_Type())
cLLtClientLtApToClientPktsLost.setMaxAccess(_C)
if mibBuilder.loadTexts:cLLtClientLtApToClientPktsLost.setStatus(_A)
if mibBuilder.loadTexts:cLLtClientLtApToClientPktsLost.setUnits(_D)
_CLLtClientLtClientToApPktsLost_Type=Counter32
_CLLtClientLtClientToApPktsLost_Object=MibTableColumn
cLLtClientLtClientToApPktsLost=_CLLtClientLtClientToApPktsLost_Object((1,3,6,1,4,1,9,9,516,1,2,2,1,5),_CLLtClientLtClientToApPktsLost_Type())
cLLtClientLtClientToApPktsLost.setMaxAccess(_C)
if mibBuilder.loadTexts:cLLtClientLtClientToApPktsLost.setStatus(_A)
if mibBuilder.loadTexts:cLLtClientLtClientToApPktsLost.setUnits(_D)
_CLLtClientLtMinRoundTripTime_Type=TimeInterval
_CLLtClientLtMinRoundTripTime_Object=MibTableColumn
cLLtClientLtMinRoundTripTime=_CLLtClientLtMinRoundTripTime_Object((1,3,6,1,4,1,9,9,516,1,2,2,1,6),_CLLtClientLtMinRoundTripTime_Type())
cLLtClientLtMinRoundTripTime.setMaxAccess(_C)
if mibBuilder.loadTexts:cLLtClientLtMinRoundTripTime.setStatus(_A)
if mibBuilder.loadTexts:cLLtClientLtMinRoundTripTime.setUnits(_K)
_CLLtClientLtMaxRoundTripTime_Type=TimeInterval
_CLLtClientLtMaxRoundTripTime_Object=MibTableColumn
cLLtClientLtMaxRoundTripTime=_CLLtClientLtMaxRoundTripTime_Object((1,3,6,1,4,1,9,9,516,1,2,2,1,7),_CLLtClientLtMaxRoundTripTime_Type())
cLLtClientLtMaxRoundTripTime.setMaxAccess(_C)
if mibBuilder.loadTexts:cLLtClientLtMaxRoundTripTime.setStatus(_A)
if mibBuilder.loadTexts:cLLtClientLtMaxRoundTripTime.setUnits(_K)
_CLLtClientLtAvgRoundTripTime_Type=TimeInterval
_CLLtClientLtAvgRoundTripTime_Object=MibTableColumn
cLLtClientLtAvgRoundTripTime=_CLLtClientLtAvgRoundTripTime_Object((1,3,6,1,4,1,9,9,516,1,2,2,1,8),_CLLtClientLtAvgRoundTripTime_Type())
cLLtClientLtAvgRoundTripTime.setMaxAccess(_C)
if mibBuilder.loadTexts:cLLtClientLtAvgRoundTripTime.setStatus(_A)
if mibBuilder.loadTexts:cLLtClientLtAvgRoundTripTime.setUnits(_K)
_CLLtClientLtUplinkMinRSSI_Type=Integer32
_CLLtClientLtUplinkMinRSSI_Object=MibTableColumn
cLLtClientLtUplinkMinRSSI=_CLLtClientLtUplinkMinRSSI_Object((1,3,6,1,4,1,9,9,516,1,2,2,1,9),_CLLtClientLtUplinkMinRSSI_Type())
cLLtClientLtUplinkMinRSSI.setMaxAccess(_C)
if mibBuilder.loadTexts:cLLtClientLtUplinkMinRSSI.setStatus(_A)
if mibBuilder.loadTexts:cLLtClientLtUplinkMinRSSI.setUnits(_E)
_CLLtClientLtUplinkMaxRSSI_Type=Integer32
_CLLtClientLtUplinkMaxRSSI_Object=MibTableColumn
cLLtClientLtUplinkMaxRSSI=_CLLtClientLtUplinkMaxRSSI_Object((1,3,6,1,4,1,9,9,516,1,2,2,1,10),_CLLtClientLtUplinkMaxRSSI_Type())
cLLtClientLtUplinkMaxRSSI.setMaxAccess(_C)
if mibBuilder.loadTexts:cLLtClientLtUplinkMaxRSSI.setStatus(_A)
if mibBuilder.loadTexts:cLLtClientLtUplinkMaxRSSI.setUnits(_E)
_CLLtClientLtUplinkAvgRSSI_Type=Integer32
_CLLtClientLtUplinkAvgRSSI_Object=MibTableColumn
cLLtClientLtUplinkAvgRSSI=_CLLtClientLtUplinkAvgRSSI_Object((1,3,6,1,4,1,9,9,516,1,2,2,1,11),_CLLtClientLtUplinkAvgRSSI_Type())
cLLtClientLtUplinkAvgRSSI.setMaxAccess(_C)
if mibBuilder.loadTexts:cLLtClientLtUplinkAvgRSSI.setStatus(_A)
if mibBuilder.loadTexts:cLLtClientLtUplinkAvgRSSI.setUnits(_E)
_CLLtClientLtDownlinkMinRSSI_Type=Integer32
_CLLtClientLtDownlinkMinRSSI_Object=MibTableColumn
cLLtClientLtDownlinkMinRSSI=_CLLtClientLtDownlinkMinRSSI_Object((1,3,6,1,4,1,9,9,516,1,2,2,1,12),_CLLtClientLtDownlinkMinRSSI_Type())
cLLtClientLtDownlinkMinRSSI.setMaxAccess(_C)
if mibBuilder.loadTexts:cLLtClientLtDownlinkMinRSSI.setStatus(_A)
if mibBuilder.loadTexts:cLLtClientLtDownlinkMinRSSI.setUnits(_E)
_CLLtClientLtDownlinkMaxRSSI_Type=Integer32
_CLLtClientLtDownlinkMaxRSSI_Object=MibTableColumn
cLLtClientLtDownlinkMaxRSSI=_CLLtClientLtDownlinkMaxRSSI_Object((1,3,6,1,4,1,9,9,516,1,2,2,1,13),_CLLtClientLtDownlinkMaxRSSI_Type())
cLLtClientLtDownlinkMaxRSSI.setMaxAccess(_C)
if mibBuilder.loadTexts:cLLtClientLtDownlinkMaxRSSI.setStatus(_A)
if mibBuilder.loadTexts:cLLtClientLtDownlinkMaxRSSI.setUnits(_E)
_CLLtClientLtDownlinkAvgRSSI_Type=Integer32
_CLLtClientLtDownlinkAvgRSSI_Object=MibTableColumn
cLLtClientLtDownlinkAvgRSSI=_CLLtClientLtDownlinkAvgRSSI_Object((1,3,6,1,4,1,9,9,516,1,2,2,1,14),_CLLtClientLtDownlinkAvgRSSI_Type())
cLLtClientLtDownlinkAvgRSSI.setMaxAccess(_C)
if mibBuilder.loadTexts:cLLtClientLtDownlinkAvgRSSI.setStatus(_A)
if mibBuilder.loadTexts:cLLtClientLtDownlinkAvgRSSI.setUnits(_E)
_CLLtClientLtUplinkMinSNR_Type=Integer32
_CLLtClientLtUplinkMinSNR_Object=MibTableColumn
cLLtClientLtUplinkMinSNR=_CLLtClientLtUplinkMinSNR_Object((1,3,6,1,4,1,9,9,516,1,2,2,1,15),_CLLtClientLtUplinkMinSNR_Type())
cLLtClientLtUplinkMinSNR.setMaxAccess(_C)
if mibBuilder.loadTexts:cLLtClientLtUplinkMinSNR.setStatus(_A)
if mibBuilder.loadTexts:cLLtClientLtUplinkMinSNR.setUnits(_F)
_CLLtClientLtUplinkMaxSNR_Type=Integer32
_CLLtClientLtUplinkMaxSNR_Object=MibTableColumn
cLLtClientLtUplinkMaxSNR=_CLLtClientLtUplinkMaxSNR_Object((1,3,6,1,4,1,9,9,516,1,2,2,1,16),_CLLtClientLtUplinkMaxSNR_Type())
cLLtClientLtUplinkMaxSNR.setMaxAccess(_C)
if mibBuilder.loadTexts:cLLtClientLtUplinkMaxSNR.setStatus(_A)
if mibBuilder.loadTexts:cLLtClientLtUplinkMaxSNR.setUnits(_F)
_CLLtClientLtUplinkAvgSNR_Type=Integer32
_CLLtClientLtUplinkAvgSNR_Object=MibTableColumn
cLLtClientLtUplinkAvgSNR=_CLLtClientLtUplinkAvgSNR_Object((1,3,6,1,4,1,9,9,516,1,2,2,1,17),_CLLtClientLtUplinkAvgSNR_Type())
cLLtClientLtUplinkAvgSNR.setMaxAccess(_C)
if mibBuilder.loadTexts:cLLtClientLtUplinkAvgSNR.setStatus(_A)
if mibBuilder.loadTexts:cLLtClientLtUplinkAvgSNR.setUnits(_F)
_CLLtClientLtDownlinkMinSNR_Type=Integer32
_CLLtClientLtDownlinkMinSNR_Object=MibTableColumn
cLLtClientLtDownlinkMinSNR=_CLLtClientLtDownlinkMinSNR_Object((1,3,6,1,4,1,9,9,516,1,2,2,1,18),_CLLtClientLtDownlinkMinSNR_Type())
cLLtClientLtDownlinkMinSNR.setMaxAccess(_C)
if mibBuilder.loadTexts:cLLtClientLtDownlinkMinSNR.setStatus(_A)
if mibBuilder.loadTexts:cLLtClientLtDownlinkMinSNR.setUnits(_F)
_CLLtClientLtDownlinkMaxSNR_Type=Integer32
_CLLtClientLtDownlinkMaxSNR_Object=MibTableColumn
cLLtClientLtDownlinkMaxSNR=_CLLtClientLtDownlinkMaxSNR_Object((1,3,6,1,4,1,9,9,516,1,2,2,1,19),_CLLtClientLtDownlinkMaxSNR_Type())
cLLtClientLtDownlinkMaxSNR.setMaxAccess(_C)
if mibBuilder.loadTexts:cLLtClientLtDownlinkMaxSNR.setStatus(_A)
if mibBuilder.loadTexts:cLLtClientLtDownlinkMaxSNR.setUnits(_F)
_CLLtClientLtDownlinkAvgSNR_Type=Integer32
_CLLtClientLtDownlinkAvgSNR_Object=MibTableColumn
cLLtClientLtDownlinkAvgSNR=_CLLtClientLtDownlinkAvgSNR_Object((1,3,6,1,4,1,9,9,516,1,2,2,1,20),_CLLtClientLtDownlinkAvgSNR_Type())
cLLtClientLtDownlinkAvgSNR.setMaxAccess(_C)
if mibBuilder.loadTexts:cLLtClientLtDownlinkAvgSNR.setStatus(_A)
if mibBuilder.loadTexts:cLLtClientLtDownlinkAvgSNR.setUnits(_F)
_CLLtClientLtTotalTxRetriesAP_Type=Counter32
_CLLtClientLtTotalTxRetriesAP_Object=MibTableColumn
cLLtClientLtTotalTxRetriesAP=_CLLtClientLtTotalTxRetriesAP_Object((1,3,6,1,4,1,9,9,516,1,2,2,1,21),_CLLtClientLtTotalTxRetriesAP_Type())
cLLtClientLtTotalTxRetriesAP.setMaxAccess(_C)
if mibBuilder.loadTexts:cLLtClientLtTotalTxRetriesAP.setStatus(_A)
if mibBuilder.loadTexts:cLLtClientLtTotalTxRetriesAP.setUnits(_J)
_CLLtClientLtMaxTxRetriesAP_Type=Counter32
_CLLtClientLtMaxTxRetriesAP_Object=MibTableColumn
cLLtClientLtMaxTxRetriesAP=_CLLtClientLtMaxTxRetriesAP_Object((1,3,6,1,4,1,9,9,516,1,2,2,1,22),_CLLtClientLtMaxTxRetriesAP_Type())
cLLtClientLtMaxTxRetriesAP.setMaxAccess(_C)
if mibBuilder.loadTexts:cLLtClientLtMaxTxRetriesAP.setStatus(_A)
if mibBuilder.loadTexts:cLLtClientLtMaxTxRetriesAP.setUnits(_J)
_CLLtClientLtTotalTxRetriesClient_Type=Counter32
_CLLtClientLtTotalTxRetriesClient_Object=MibTableColumn
cLLtClientLtTotalTxRetriesClient=_CLLtClientLtTotalTxRetriesClient_Object((1,3,6,1,4,1,9,9,516,1,2,2,1,23),_CLLtClientLtTotalTxRetriesClient_Type())
cLLtClientLtTotalTxRetriesClient.setMaxAccess(_C)
if mibBuilder.loadTexts:cLLtClientLtTotalTxRetriesClient.setStatus(_A)
if mibBuilder.loadTexts:cLLtClientLtTotalTxRetriesClient.setUnits(_J)
_CLLtClientLtMaxTxRetriesClient_Type=Counter32
_CLLtClientLtMaxTxRetriesClient_Object=MibTableColumn
cLLtClientLtMaxTxRetriesClient=_CLLtClientLtMaxTxRetriesClient_Object((1,3,6,1,4,1,9,9,516,1,2,2,1,24),_CLLtClientLtMaxTxRetriesClient_Type())
cLLtClientLtMaxTxRetriesClient.setMaxAccess(_C)
if mibBuilder.loadTexts:cLLtClientLtMaxTxRetriesClient.setStatus(_A)
if mibBuilder.loadTexts:cLLtClientLtMaxTxRetriesClient.setUnits(_J)
class _CLLtClientLtStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4)));namedValues=NamedValues(*(('cLLtClientLtStatusFailed',0),('cLLtClientLtStatusCcxInProgress',1),('cLLtClientLtStatusPngInProgress',2),('cLLtClientLtStatusPingSuccess',3),('cLLtClientLtStatusCcxLtSuccess',4)))
_CLLtClientLtStatus_Type.__name__=_M
_CLLtClientLtStatus_Object=MibTableColumn
cLLtClientLtStatus=_CLLtClientLtStatus_Object((1,3,6,1,4,1,9,9,516,1,2,2,1,25),_CLLtClientLtStatus_Type())
cLLtClientLtStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:cLLtClientLtStatus.setStatus(_A)
_CiscoLwappLinkTestStatus_ObjectIdentity=ObjectIdentity
ciscoLwappLinkTestStatus=_CiscoLwappLinkTestStatus_ObjectIdentity((1,3,6,1,4,1,9,9,516,1,3))
_CLLtClientLtDataRateTable_Object=MibTable
cLLtClientLtDataRateTable=_CLLtClientLtDataRateTable_Object((1,3,6,1,4,1,9,9,516,1,3,1))
if mibBuilder.loadTexts:cLLtClientLtDataRateTable.setStatus(_A)
_CLLtClientLtDataRateEntry_Object=MibTableRow
cLLtClientLtDataRateEntry=_CLLtClientLtDataRateEntry_Object((1,3,6,1,4,1,9,9,516,1,3,1,1))
cLLtClientLtDataRateEntry.setIndexNames((0,_B,_I),(0,_B,_Q))
if mibBuilder.loadTexts:cLLtClientLtDataRateEntry.setStatus(_A)
class _CLLtClientLtDataRate_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,255))
_CLLtClientLtDataRate_Type.__name__=_L
_CLLtClientLtDataRate_Object=MibTableColumn
cLLtClientLtDataRate=_CLLtClientLtDataRate_Object((1,3,6,1,4,1,9,9,516,1,3,1,1,1),_CLLtClientLtDataRate_Type())
cLLtClientLtDataRate.setMaxAccess(_O)
if mibBuilder.loadTexts:cLLtClientLtDataRate.setStatus(_A)
_CLLtClientLtRateDownlinkPktsSent_Type=Counter32
_CLLtClientLtRateDownlinkPktsSent_Object=MibTableColumn
cLLtClientLtRateDownlinkPktsSent=_CLLtClientLtRateDownlinkPktsSent_Object((1,3,6,1,4,1,9,9,516,1,3,1,1,2),_CLLtClientLtRateDownlinkPktsSent_Type())
cLLtClientLtRateDownlinkPktsSent.setMaxAccess(_C)
if mibBuilder.loadTexts:cLLtClientLtRateDownlinkPktsSent.setStatus(_A)
if mibBuilder.loadTexts:cLLtClientLtRateDownlinkPktsSent.setUnits(_D)
_CLLtClientLtRateUplinkPktsSent_Type=Counter32
_CLLtClientLtRateUplinkPktsSent_Object=MibTableColumn
cLLtClientLtRateUplinkPktsSent=_CLLtClientLtRateUplinkPktsSent_Object((1,3,6,1,4,1,9,9,516,1,3,1,1,3),_CLLtClientLtRateUplinkPktsSent_Type())
cLLtClientLtRateUplinkPktsSent.setMaxAccess(_C)
if mibBuilder.loadTexts:cLLtClientLtRateUplinkPktsSent.setStatus(_A)
if mibBuilder.loadTexts:cLLtClientLtRateUplinkPktsSent.setUnits(_D)
_CiscoLwappLinkTestMIBConform_ObjectIdentity=ObjectIdentity
ciscoLwappLinkTestMIBConform=_CiscoLwappLinkTestMIBConform_ObjectIdentity((1,3,6,1,4,1,9,9,516,2))
_CiscoLwappLinkTestMIBCompliances_ObjectIdentity=ObjectIdentity
ciscoLwappLinkTestMIBCompliances=_CiscoLwappLinkTestMIBCompliances_ObjectIdentity((1,3,6,1,4,1,9,9,516,2,1))
_CiscoLwappLinkTestMIBGroups_ObjectIdentity=ObjectIdentity
ciscoLwappLinkTestMIBGroups=_CiscoLwappLinkTestMIBGroups_ObjectIdentity((1,3,6,1,4,1,9,9,516,2,2))
cLLinkTestConfigGroup=ObjectGroup((1,3,6,1,4,1,9,9,516,2,2,1))
cLLinkTestConfigGroup.setObjects(*((_B,_R),(_B,_S),(_B,_T),(_B,_U)))
if mibBuilder.loadTexts:cLLinkTestConfigGroup.setStatus(_A)
cLLinkTestRunsGroup=ObjectGroup((1,3,6,1,4,1,9,9,516,2,2,2))
cLLinkTestRunsGroup.setObjects(*((_B,_V),(_B,_W),(_B,_X),(_B,_Y),(_B,_Z),(_B,_a),(_B,_b),(_B,_c),(_B,_d),(_B,_e),(_B,_f),(_B,_g),(_B,_h),(_B,_i),(_B,_j),(_B,_k),(_B,_l),(_B,_m),(_B,_n),(_B,_o),(_B,_p),(_B,_q),(_B,_r),(_B,_s),(_B,_t),(_B,_u),(_B,_v)))
if mibBuilder.loadTexts:cLLinkTestRunsGroup.setStatus(_A)
cLLinkTestStatusGroup=ObjectGroup((1,3,6,1,4,1,9,9,516,2,2,3))
cLLinkTestStatusGroup.setObjects(*((_B,_w),(_B,_x)))
if mibBuilder.loadTexts:cLLinkTestStatusGroup.setStatus(_A)
ciscoLwappLinkTestMIBCompliance=ModuleCompliance((1,3,6,1,4,1,9,9,516,2,1,1))
ciscoLwappLinkTestMIBCompliance.setObjects(*((_B,_y),(_B,_z),(_B,_A0)))
if mibBuilder.loadTexts:ciscoLwappLinkTestMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'ciscoLwappLinkTestMIB':ciscoLwappLinkTestMIB,'ciscoLwappLinkTestMIBNotifs':ciscoLwappLinkTestMIBNotifs,'ciscoLwappLinkTestMIBObjects':ciscoLwappLinkTestMIBObjects,'ciscoLwappLinkTestConfig':ciscoLwappLinkTestConfig,_R:cLLtResponder,_S:cLLtPacketSize,_T:cLLtNumberOfPackets,_U:cLLtTestPurgeTime,'ciscoLwappLinkTestRun':ciscoLwappLinkTestRun,'cLLtClientLinkTestTable':cLLtClientLinkTestTable,'cLLtClientLinkTestEntry':cLLtClientLinkTestEntry,_I:cLLtClientLtIndex,_V:cLLtClientLtMacAddress,_v:cLLtClientLtRowStatus,'cLLtClientLTResultsTable':cLLtClientLTResultsTable,'cLLtClientLTResultsEntry':cLLtClientLTResultsEntry,_W:cLLtClientLtPacketsSent,_X:cLLtClientLtPacketsRx,_Y:cLLtClientLtTotalPacketsLost,_Z:cLLtClientLtApToClientPktsLost,_a:cLLtClientLtClientToApPktsLost,_b:cLLtClientLtMinRoundTripTime,_c:cLLtClientLtMaxRoundTripTime,_d:cLLtClientLtAvgRoundTripTime,_e:cLLtClientLtUplinkMinRSSI,_f:cLLtClientLtUplinkMaxRSSI,_g:cLLtClientLtUplinkAvgRSSI,_h:cLLtClientLtDownlinkMinRSSI,_i:cLLtClientLtDownlinkMaxRSSI,_j:cLLtClientLtDownlinkAvgRSSI,_k:cLLtClientLtUplinkMinSNR,_l:cLLtClientLtUplinkMaxSNR,_m:cLLtClientLtUplinkAvgSNR,_n:cLLtClientLtDownlinkMinSNR,_o:cLLtClientLtDownlinkMaxSNR,_p:cLLtClientLtDownlinkAvgSNR,_q:cLLtClientLtTotalTxRetriesAP,_r:cLLtClientLtMaxTxRetriesAP,_s:cLLtClientLtTotalTxRetriesClient,_t:cLLtClientLtMaxTxRetriesClient,_u:cLLtClientLtStatus,'ciscoLwappLinkTestStatus':ciscoLwappLinkTestStatus,'cLLtClientLtDataRateTable':cLLtClientLtDataRateTable,'cLLtClientLtDataRateEntry':cLLtClientLtDataRateEntry,_Q:cLLtClientLtDataRate,_w:cLLtClientLtRateDownlinkPktsSent,_x:cLLtClientLtRateUplinkPktsSent,'ciscoLwappLinkTestMIBConform':ciscoLwappLinkTestMIBConform,'ciscoLwappLinkTestMIBCompliances':ciscoLwappLinkTestMIBCompliances,'ciscoLwappLinkTestMIBCompliance':ciscoLwappLinkTestMIBCompliance,'ciscoLwappLinkTestMIBGroups':ciscoLwappLinkTestMIBGroups,_y:cLLinkTestConfigGroup,_z:cLLinkTestRunsGroup,_A0:cLLinkTestStatusGroup})