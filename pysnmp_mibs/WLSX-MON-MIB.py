_L='monEventID'
_K='deprecated'
_J='monHTRate'
_I='Integer32'
_H='not-accessible'
_G='monitoredStaPhyAddress'
_F='monitoredApBSSID'
_E='monRadioNumber'
_D='monPhyAddress'
_C='WLSX-MON-MIB'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
wlsxEnterpriseMibModules,=mibBuilder.importSymbols('ARUBA-MIB','wlsxEnterpriseMibModules')
ArubaAPMatchMethod,ArubaAPMatchType,ArubaEnableValue,ArubaFrameType,ArubaHTMode,ArubaHTRate,ArubaMonAuthAlgorithm,ArubaMonEncryptionCipher,ArubaMonEncryptionType,ArubaPhyType,ArubaRogueApType,ArubaStationType=mibBuilder.importSymbols('ARUBA-TC','ArubaAPMatchMethod','ArubaAPMatchType','ArubaEnableValue','ArubaFrameType','ArubaHTMode','ArubaHTRate','ArubaMonAuthAlgorithm','ArubaMonEncryptionCipher','ArubaMonEncryptionType','ArubaPhyType','ArubaRogueApType','ArubaStationType')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso,snmpModules=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_I,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso','snmpModules')
DisplayString,MacAddress,PhysAddress,RowStatus,StorageType,TAddress,TDomain,TextualConvention,TestAndIncr,TimeInterval,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress','RowStatus','StorageType','TAddress','TDomain','TextualConvention','TestAndIncr','TimeInterval','TruthValue')
wlsxMonMIB=ModuleIdentity((1,3,6,1,4,1,14823,2,2,1,6))
if mibBuilder.loadTexts:wlsxMonMIB.setRevisions(('2020-08-14 17:45',))
_WlsxMonStatsGroup_ObjectIdentity=ObjectIdentity
wlsxMonStatsGroup=_WlsxMonStatsGroup_ObjectIdentity((1,3,6,1,4,1,14823,2,2,1,6,6))
_WlsxMonAccessPointStatsGroup_ObjectIdentity=ObjectIdentity
wlsxMonAccessPointStatsGroup=_WlsxMonAccessPointStatsGroup_ObjectIdentity((1,3,6,1,4,1,14823,2,2,1,6,6,1))
_WlsxMonAPStatsTable_Object=MibTable
wlsxMonAPStatsTable=_WlsxMonAPStatsTable_Object((1,3,6,1,4,1,14823,2,2,1,6,6,1,1))
if mibBuilder.loadTexts:wlsxMonAPStatsTable.setStatus(_A)
_WlsxMonAPStatsEntry_Object=MibTableRow
wlsxMonAPStatsEntry=_WlsxMonAPStatsEntry_Object((1,3,6,1,4,1,14823,2,2,1,6,6,1,1,1))
wlsxMonAPStatsEntry.setIndexNames((0,_C,_D),(0,_C,_E),(0,_C,_F))
if mibBuilder.loadTexts:wlsxMonAPStatsEntry.setStatus(_A)
_MonPhyAddress_Type=MacAddress
_MonPhyAddress_Object=MibTableColumn
monPhyAddress=_MonPhyAddress_Object((1,3,6,1,4,1,14823,2,2,1,6,6,1,1,1,1),_MonPhyAddress_Type())
monPhyAddress.setMaxAccess(_H)
if mibBuilder.loadTexts:monPhyAddress.setStatus(_A)
_MonRadioNumber_Type=Integer32
_MonRadioNumber_Object=MibTableColumn
monRadioNumber=_MonRadioNumber_Object((1,3,6,1,4,1,14823,2,2,1,6,6,1,1,1,2),_MonRadioNumber_Type())
monRadioNumber.setMaxAccess(_H)
if mibBuilder.loadTexts:monRadioNumber.setStatus(_A)
_MonitoredApBSSID_Type=MacAddress
_MonitoredApBSSID_Object=MibTableColumn
monitoredApBSSID=_MonitoredApBSSID_Object((1,3,6,1,4,1,14823,2,2,1,6,6,1,1,1,3),_MonitoredApBSSID_Type())
monitoredApBSSID.setMaxAccess(_H)
if mibBuilder.loadTexts:monitoredApBSSID.setStatus(_A)
_MonPhyType_Type=ArubaPhyType
_MonPhyType_Object=MibTableColumn
monPhyType=_MonPhyType_Object((1,3,6,1,4,1,14823,2,2,1,6,6,1,1,1,4),_MonPhyType_Type())
monPhyType.setMaxAccess(_B)
if mibBuilder.loadTexts:monPhyType.setStatus(_A)
_MonAPCurrentChannel_Type=Unsigned32
_MonAPCurrentChannel_Object=MibTableColumn
monAPCurrentChannel=_MonAPCurrentChannel_Object((1,3,6,1,4,1,14823,2,2,1,6,6,1,1,1,5),_MonAPCurrentChannel_Type())
monAPCurrentChannel.setMaxAccess(_B)
if mibBuilder.loadTexts:monAPCurrentChannel.setStatus(_A)
_MonAPNumClients_Type=Integer32
_MonAPNumClients_Object=MibTableColumn
monAPNumClients=_MonAPNumClients_Object((1,3,6,1,4,1,14823,2,2,1,6,6,1,1,1,6),_MonAPNumClients_Type())
monAPNumClients.setMaxAccess(_B)
if mibBuilder.loadTexts:monAPNumClients.setStatus(_A)
_MonAPTxPkts_Type=Counter32
_MonAPTxPkts_Object=MibTableColumn
monAPTxPkts=_MonAPTxPkts_Object((1,3,6,1,4,1,14823,2,2,1,6,6,1,1,1,7),_MonAPTxPkts_Type())
monAPTxPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:monAPTxPkts.setStatus(_A)
_MonAPTxBytes_Type=Counter32
_MonAPTxBytes_Object=MibTableColumn
monAPTxBytes=_MonAPTxBytes_Object((1,3,6,1,4,1,14823,2,2,1,6,6,1,1,1,8),_MonAPTxBytes_Type())
monAPTxBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:monAPTxBytes.setStatus(_A)
_MonAPRxPkts_Type=Counter32
_MonAPRxPkts_Object=MibTableColumn
monAPRxPkts=_MonAPRxPkts_Object((1,3,6,1,4,1,14823,2,2,1,6,6,1,1,1,9),_MonAPRxPkts_Type())
monAPRxPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:monAPRxPkts.setStatus(_A)
_MonAPRxBytes_Type=Counter32
_MonAPRxBytes_Object=MibTableColumn
monAPRxBytes=_MonAPRxBytes_Object((1,3,6,1,4,1,14823,2,2,1,6,6,1,1,1,10),_MonAPRxBytes_Type())
monAPRxBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:monAPRxBytes.setStatus(_A)
_MonAPTxDeauthentications_Type=Counter32
_MonAPTxDeauthentications_Object=MibTableColumn
monAPTxDeauthentications=_MonAPTxDeauthentications_Object((1,3,6,1,4,1,14823,2,2,1,6,6,1,1,1,11),_MonAPTxDeauthentications_Type())
monAPTxDeauthentications.setMaxAccess(_B)
if mibBuilder.loadTexts:monAPTxDeauthentications.setStatus(_A)
_MonAPRxDeauthentications_Type=Counter32
_MonAPRxDeauthentications_Object=MibTableColumn
monAPRxDeauthentications=_MonAPRxDeauthentications_Object((1,3,6,1,4,1,14823,2,2,1,6,6,1,1,1,12),_MonAPRxDeauthentications_Type())
monAPRxDeauthentications.setMaxAccess(_B)
if mibBuilder.loadTexts:monAPRxDeauthentications.setStatus(_A)
_MonAPChannelThroughput_Type=Integer32
_MonAPChannelThroughput_Object=MibTableColumn
monAPChannelThroughput=_MonAPChannelThroughput_Object((1,3,6,1,4,1,14823,2,2,1,6,6,1,1,1,13),_MonAPChannelThroughput_Type())
monAPChannelThroughput.setMaxAccess(_B)
if mibBuilder.loadTexts:monAPChannelThroughput.setStatus(_A)
_MonAPFrameRetryRate_Type=Integer32
_MonAPFrameRetryRate_Object=MibTableColumn
monAPFrameRetryRate=_MonAPFrameRetryRate_Object((1,3,6,1,4,1,14823,2,2,1,6,6,1,1,1,14),_MonAPFrameRetryRate_Type())
monAPFrameRetryRate.setMaxAccess(_B)
if mibBuilder.loadTexts:monAPFrameRetryRate.setStatus(_A)
_MonAPFrameLowSpeedRate_Type=Integer32
_MonAPFrameLowSpeedRate_Object=MibTableColumn
monAPFrameLowSpeedRate=_MonAPFrameLowSpeedRate_Object((1,3,6,1,4,1,14823,2,2,1,6,6,1,1,1,15),_MonAPFrameLowSpeedRate_Type())
monAPFrameLowSpeedRate.setMaxAccess(_B)
if mibBuilder.loadTexts:monAPFrameLowSpeedRate.setStatus(_A)
_MonAPFrameNonUnicastRate_Type=Integer32
_MonAPFrameNonUnicastRate_Object=MibTableColumn
monAPFrameNonUnicastRate=_MonAPFrameNonUnicastRate_Object((1,3,6,1,4,1,14823,2,2,1,6,6,1,1,1,16),_MonAPFrameNonUnicastRate_Type())
monAPFrameNonUnicastRate.setMaxAccess(_B)
if mibBuilder.loadTexts:monAPFrameNonUnicastRate.setStatus(_A)
_MonAPFrameFragmentationRate_Type=Integer32
_MonAPFrameFragmentationRate_Object=MibTableColumn
monAPFrameFragmentationRate=_MonAPFrameFragmentationRate_Object((1,3,6,1,4,1,14823,2,2,1,6,6,1,1,1,17),_MonAPFrameFragmentationRate_Type())
monAPFrameFragmentationRate.setMaxAccess(_B)
if mibBuilder.loadTexts:monAPFrameFragmentationRate.setStatus(_A)
_MonAPFrameBandwidthRate_Type=Integer32
_MonAPFrameBandwidthRate_Object=MibTableColumn
monAPFrameBandwidthRate=_MonAPFrameBandwidthRate_Object((1,3,6,1,4,1,14823,2,2,1,6,6,1,1,1,18),_MonAPFrameBandwidthRate_Type())
monAPFrameBandwidthRate.setMaxAccess(_B)
if mibBuilder.loadTexts:monAPFrameBandwidthRate.setStatus(_A)
_MonAPFrameRetryErrorRate_Type=Integer32
_MonAPFrameRetryErrorRate_Object=MibTableColumn
monAPFrameRetryErrorRate=_MonAPFrameRetryErrorRate_Object((1,3,6,1,4,1,14823,2,2,1,6,6,1,1,1,19),_MonAPFrameRetryErrorRate_Type())
monAPFrameRetryErrorRate.setMaxAccess(_B)
if mibBuilder.loadTexts:monAPFrameRetryErrorRate.setStatus(_K)
_MonAPChannelErrorRate_Type=Integer32
_MonAPChannelErrorRate_Object=MibTableColumn
monAPChannelErrorRate=_MonAPChannelErrorRate_Object((1,3,6,1,4,1,14823,2,2,1,6,6,1,1,1,20),_MonAPChannelErrorRate_Type())
monAPChannelErrorRate.setMaxAccess(_B)
if mibBuilder.loadTexts:monAPChannelErrorRate.setStatus(_A)
_MonAPESSID_Type=DisplayString
_MonAPESSID_Object=MibTableColumn
monAPESSID=_MonAPESSID_Object((1,3,6,1,4,1,14823,2,2,1,6,6,1,1,1,21),_MonAPESSID_Type())
monAPESSID.setMaxAccess(_B)
if mibBuilder.loadTexts:monAPESSID.setStatus(_A)
_MonAPRSSI_Type=Integer32
_MonAPRSSI_Object=MibTableColumn
monAPRSSI=_MonAPRSSI_Object((1,3,6,1,4,1,14823,2,2,1,6,6,1,1,1,22),_MonAPRSSI_Type())
monAPRSSI.setMaxAccess(_B)
if mibBuilder.loadTexts:monAPRSSI.setStatus(_A)
_MonAPFrameReceiveErrorRate_Type=Integer32
_MonAPFrameReceiveErrorRate_Object=MibTableColumn
monAPFrameReceiveErrorRate=_MonAPFrameReceiveErrorRate_Object((1,3,6,1,4,1,14823,2,2,1,6,6,1,1,1,23),_MonAPFrameReceiveErrorRate_Type())
monAPFrameReceiveErrorRate.setMaxAccess(_B)
if mibBuilder.loadTexts:monAPFrameReceiveErrorRate.setStatus(_A)
_WlsxMonAPRateStatsTable_Object=MibTable
wlsxMonAPRateStatsTable=_WlsxMonAPRateStatsTable_Object((1,3,6,1,4,1,14823,2,2,1,6,6,1,2))
if mibBuilder.loadTexts:wlsxMonAPRateStatsTable.setStatus(_A)
_WlsxMonAPRateStatsEntry_Object=MibTableRow
wlsxMonAPRateStatsEntry=_WlsxMonAPRateStatsEntry_Object((1,3,6,1,4,1,14823,2,2,1,6,6,1,2,1))
wlsxMonAPRateStatsEntry.setIndexNames((0,_C,_D),(0,_C,_E),(0,_C,_F))
if mibBuilder.loadTexts:wlsxMonAPRateStatsEntry.setStatus(_A)
_MonAPStatsTotPktsAt1Mbps_Type=Counter32
_MonAPStatsTotPktsAt1Mbps_Object=MibTableColumn
monAPStatsTotPktsAt1Mbps=_MonAPStatsTotPktsAt1Mbps_Object((1,3,6,1,4,1,14823,2,2,1,6,6,1,2,1,1),_MonAPStatsTotPktsAt1Mbps_Type())
monAPStatsTotPktsAt1Mbps.setMaxAccess(_B)
if mibBuilder.loadTexts:monAPStatsTotPktsAt1Mbps.setStatus(_A)
_MonAPStatsTotBytesAt1Mbps_Type=Counter32
_MonAPStatsTotBytesAt1Mbps_Object=MibTableColumn
monAPStatsTotBytesAt1Mbps=_MonAPStatsTotBytesAt1Mbps_Object((1,3,6,1,4,1,14823,2,2,1,6,6,1,2,1,2),_MonAPStatsTotBytesAt1Mbps_Type())
monAPStatsTotBytesAt1Mbps.setMaxAccess(_B)
if mibBuilder.loadTexts:monAPStatsTotBytesAt1Mbps.setStatus(_A)
_MonAPStatsTotPktsAt2Mbps_Type=Counter32
_MonAPStatsTotPktsAt2Mbps_Object=MibTableColumn
monAPStatsTotPktsAt2Mbps=_MonAPStatsTotPktsAt2Mbps_Object((1,3,6,1,4,1,14823,2,2,1,6,6,1,2,1,3),_MonAPStatsTotPktsAt2Mbps_Type())
monAPStatsTotPktsAt2Mbps.setMaxAccess(_B)
if mibBuilder.loadTexts:monAPStatsTotPktsAt2Mbps.setStatus(_A)
_MonAPStatsTotBytesAt2Mbps_Type=Counter32
_MonAPStatsTotBytesAt2Mbps_Object=MibTableColumn
monAPStatsTotBytesAt2Mbps=_MonAPStatsTotBytesAt2Mbps_Object((1,3,6,1,4,1,14823,2,2,1,6,6,1,2,1,4),_MonAPStatsTotBytesAt2Mbps_Type())
monAPStatsTotBytesAt2Mbps.setMaxAccess(_B)
if mibBuilder.loadTexts:monAPStatsTotBytesAt2Mbps.setStatus(_A)
_MonAPStatsTotPktsAt5Mbps_Type=Counter32
_MonAPStatsTotPktsAt5Mbps_Object=MibTableColumn
monAPStatsTotPktsAt5Mbps=_MonAPStatsTotPktsAt5Mbps_Object((1,3,6,1,4,1,14823,2,2,1,6,6,1,2,1,5),_MonAPStatsTotPktsAt5Mbps_Type())
monAPStatsTotPktsAt5Mbps.setMaxAccess(_B)
if mibBuilder.loadTexts:monAPStatsTotPktsAt5Mbps.setStatus(_A)
_MonAPStatsTotBytesAt5Mbps_Type=Counter32
_MonAPStatsTotBytesAt5Mbps_Object=MibTableColumn
monAPStatsTotBytesAt5Mbps=_MonAPStatsTotBytesAt5Mbps_Object((1,3,6,1,4,1,14823,2,2,1,6,6,1,2,1,6),_MonAPStatsTotBytesAt5Mbps_Type())
monAPStatsTotBytesAt5Mbps.setMaxAccess(_B)
if mibBuilder.loadTexts:monAPStatsTotBytesAt5Mbps.setStatus(_A)
_MonAPStatsTotPktsAt11Mbps_Type=Counter32
_MonAPStatsTotPktsAt11Mbps_Object=MibTableColumn
monAPStatsTotPktsAt11Mbps=_MonAPStatsTotPktsAt11Mbps_Object((1,3,6,1,4,1,14823,2,2,1,6,6,1,2,1,7),_MonAPStatsTotPktsAt11Mbps_Type())
monAPStatsTotPktsAt11Mbps.setMaxAccess(_B)
if mibBuilder.loadTexts:monAPStatsTotPktsAt11Mbps.setStatus(_A)
_MonAPStatsTotBytesAt11Mbps_Type=Counter32
_MonAPStatsTotBytesAt11Mbps_Object=MibTableColumn
monAPStatsTotBytesAt11Mbps=_MonAPStatsTotBytesAt11Mbps_Object((1,3,6,1,4,1,14823,2,2,1,6,6,1,2,1,8),_MonAPStatsTotBytesAt11Mbps_Type())
monAPStatsTotBytesAt11Mbps.setMaxAccess(_B)
if mibBuilder.loadTexts:monAPStatsTotBytesAt11Mbps.setStatus(_A)
_MonAPStatsTotPktsAt6Mbps_Type=Counter32
_MonAPStatsTotPktsAt6Mbps_Object=MibTableColumn
monAPStatsTotPktsAt6Mbps=_MonAPStatsTotPktsAt6Mbps_Object((1,3,6,1,4,1,14823,2,2,1,6,6,1,2,1,9),_MonAPStatsTotPktsAt6Mbps_Type())
monAPStatsTotPktsAt6Mbps.setMaxAccess(_B)
if mibBuilder.loadTexts:monAPStatsTotPktsAt6Mbps.setStatus(_A)
_MonAPStatsTotBytesAt6Mbps_Type=Counter32
_MonAPStatsTotBytesAt6Mbps_Object=MibTableColumn
monAPStatsTotBytesAt6Mbps=_MonAPStatsTotBytesAt6Mbps_Object((1,3,6,1,4,1,14823,2,2,1,6,6,1,2,1,10),_MonAPStatsTotBytesAt6Mbps_Type())
monAPStatsTotBytesAt6Mbps.setMaxAccess(_B)
if mibBuilder.loadTexts:monAPStatsTotBytesAt6Mbps.setStatus(_A)
_MonAPStatsTotPktsAt12Mbps_Type=Counter32
_MonAPStatsTotPktsAt12Mbps_Object=MibTableColumn
monAPStatsTotPktsAt12Mbps=_MonAPStatsTotPktsAt12Mbps_Object((1,3,6,1,4,1,14823,2,2,1,6,6,1,2,1,11),_MonAPStatsTotPktsAt12Mbps_Type())
monAPStatsTotPktsAt12Mbps.setMaxAccess(_B)
if mibBuilder.loadTexts:monAPStatsTotPktsAt12Mbps.setStatus(_A)
_MonAPStatsTotBytesAt12Mbps_Type=Counter32
_MonAPStatsTotBytesAt12Mbps_Object=MibTableColumn
monAPStatsTotBytesAt12Mbps=_MonAPStatsTotBytesAt12Mbps_Object((1,3,6,1,4,1,14823,2,2,1,6,6,1,2,1,12),_MonAPStatsTotBytesAt12Mbps_Type())
monAPStatsTotBytesAt12Mbps.setMaxAccess(_B)
if mibBuilder.loadTexts:monAPStatsTotBytesAt12Mbps.setStatus(_A)
_MonAPStatsTotPktsAt18Mbps_Type=Counter32
_MonAPStatsTotPktsAt18Mbps_Object=MibTableColumn
monAPStatsTotPktsAt18Mbps=_MonAPStatsTotPktsAt18Mbps_Object((1,3,6,1,4,1,14823,2,2,1,6,6,1,2,1,13),_MonAPStatsTotPktsAt18Mbps_Type())
monAPStatsTotPktsAt18Mbps.setMaxAccess(_B)
if mibBuilder.loadTexts:monAPStatsTotPktsAt18Mbps.setStatus(_A)
_MonAPStatsTotBytesAt18Mbps_Type=Counter32
_MonAPStatsTotBytesAt18Mbps_Object=MibTableColumn
monAPStatsTotBytesAt18Mbps=_MonAPStatsTotBytesAt18Mbps_Object((1,3,6,1,4,1,14823,2,2,1,6,6,1,2,1,14),_MonAPStatsTotBytesAt18Mbps_Type())
monAPStatsTotBytesAt18Mbps.setMaxAccess(_B)
if mibBuilder.loadTexts:monAPStatsTotBytesAt18Mbps.setStatus(_A)
_MonAPStatsTotPktsAt24Mbps_Type=Counter32
_MonAPStatsTotPktsAt24Mbps_Object=MibTableColumn
monAPStatsTotPktsAt24Mbps=_MonAPStatsTotPktsAt24Mbps_Object((1,3,6,1,4,1,14823,2,2,1,6,6,1,2,1,15),_MonAPStatsTotPktsAt24Mbps_Type())
monAPStatsTotPktsAt24Mbps.setMaxAccess(_B)
if mibBuilder.loadTexts:monAPStatsTotPktsAt24Mbps.setStatus(_A)
_MonAPStatsTotBytesAt24Mbps_Type=Counter32
_MonAPStatsTotBytesAt24Mbps_Object=MibTableColumn
monAPStatsTotBytesAt24Mbps=_MonAPStatsTotBytesAt24Mbps_Object((1,3,6,1,4,1,14823,2,2,1,6,6,1,2,1,16),_MonAPStatsTotBytesAt24Mbps_Type())
monAPStatsTotBytesAt24Mbps.setMaxAccess(_B)
if mibBuilder.loadTexts:monAPStatsTotBytesAt24Mbps.setStatus(_A)
_MonAPStatsTotPktsAt36Mbps_Type=Counter32
_MonAPStatsTotPktsAt36Mbps_Object=MibTableColumn
monAPStatsTotPktsAt36Mbps=_MonAPStatsTotPktsAt36Mbps_Object((1,3,6,1,4,1,14823,2,2,1,6,6,1,2,1,17),_MonAPStatsTotPktsAt36Mbps_Type())
monAPStatsTotPktsAt36Mbps.setMaxAccess(_B)
if mibBuilder.loadTexts:monAPStatsTotPktsAt36Mbps.setStatus(_A)
_MonAPStatsTotBytesAt36Mbps_Type=Counter32
_MonAPStatsTotBytesAt36Mbps_Object=MibTableColumn
monAPStatsTotBytesAt36Mbps=_MonAPStatsTotBytesAt36Mbps_Object((1,3,6,1,4,1,14823,2,2,1,6,6,1,2,1,18),_MonAPStatsTotBytesAt36Mbps_Type())
monAPStatsTotBytesAt36Mbps.setMaxAccess(_B)
if mibBuilder.loadTexts:monAPStatsTotBytesAt36Mbps.setStatus(_A)
_MonAPStatsTotPktsAt48Mbps_Type=Counter32
_MonAPStatsTotPktsAt48Mbps_Object=MibTableColumn
monAPStatsTotPktsAt48Mbps=_MonAPStatsTotPktsAt48Mbps_Object((1,3,6,1,4,1,14823,2,2,1,6,6,1,2,1,19),_MonAPStatsTotPktsAt48Mbps_Type())
monAPStatsTotPktsAt48Mbps.setMaxAccess(_B)
if mibBuilder.loadTexts:monAPStatsTotPktsAt48Mbps.setStatus(_A)
_MonAPStatsTotBytesAt48Mbps_Type=Counter32
_MonAPStatsTotBytesAt48Mbps_Object=MibTableColumn
monAPStatsTotBytesAt48Mbps=_MonAPStatsTotBytesAt48Mbps_Object((1,3,6,1,4,1,14823,2,2,1,6,6,1,2,1,20),_MonAPStatsTotBytesAt48Mbps_Type())
monAPStatsTotBytesAt48Mbps.setMaxAccess(_B)
if mibBuilder.loadTexts:monAPStatsTotBytesAt48Mbps.setStatus(_A)
_MonAPStatsTotPktsAt54Mbps_Type=Counter32
_MonAPStatsTotPktsAt54Mbps_Object=MibTableColumn
monAPStatsTotPktsAt54Mbps=_MonAPStatsTotPktsAt54Mbps_Object((1,3,6,1,4,1,14823,2,2,1,6,6,1,2,1,21),_MonAPStatsTotPktsAt54Mbps_Type())
monAPStatsTotPktsAt54Mbps.setMaxAccess(_B)
if mibBuilder.loadTexts:monAPStatsTotPktsAt54Mbps.setStatus(_A)
_MonAPStatsTotBytesAt54Mbps_Type=Counter32
_MonAPStatsTotBytesAt54Mbps_Object=MibTableColumn
monAPStatsTotBytesAt54Mbps=_MonAPStatsTotBytesAt54Mbps_Object((1,3,6,1,4,1,14823,2,2,1,6,6,1,2,1,22),_MonAPStatsTotBytesAt54Mbps_Type())
monAPStatsTotBytesAt54Mbps.setMaxAccess(_B)
if mibBuilder.loadTexts:monAPStatsTotBytesAt54Mbps.setStatus(_A)
_MonAPStatsTotPktsAt9Mbps_Type=Counter32
_MonAPStatsTotPktsAt9Mbps_Object=MibTableColumn
monAPStatsTotPktsAt9Mbps=_MonAPStatsTotPktsAt9Mbps_Object((1,3,6,1,4,1,14823,2,2,1,6,6,1,2,1,23),_MonAPStatsTotPktsAt9Mbps_Type())
monAPStatsTotPktsAt9Mbps.setMaxAccess(_B)
if mibBuilder.loadTexts:monAPStatsTotPktsAt9Mbps.setStatus(_A)
_MonAPStatsTotBytesAt9Mbps_Type=Counter32
_MonAPStatsTotBytesAt9Mbps_Object=MibTableColumn
monAPStatsTotBytesAt9Mbps=_MonAPStatsTotBytesAt9Mbps_Object((1,3,6,1,4,1,14823,2,2,1,6,6,1,2,1,24),_MonAPStatsTotBytesAt9Mbps_Type())
monAPStatsTotBytesAt9Mbps.setMaxAccess(_B)
if mibBuilder.loadTexts:monAPStatsTotBytesAt9Mbps.setStatus(_A)
_WlsxMonAPDATypeStatsTable_Object=MibTable
wlsxMonAPDATypeStatsTable=_WlsxMonAPDATypeStatsTable_Object((1,3,6,1,4,1,14823,2,2,1,6,6,1,3))
if mibBuilder.loadTexts:wlsxMonAPDATypeStatsTable.setStatus(_A)
_WlsxMonAPDATypeStatsEntry_Object=MibTableRow
wlsxMonAPDATypeStatsEntry=_WlsxMonAPDATypeStatsEntry_Object((1,3,6,1,4,1,14823,2,2,1,6,6,1,3,1))
wlsxMonAPDATypeStatsEntry.setIndexNames((0,_C,_D),(0,_C,_E),(0,_C,_F))
if mibBuilder.loadTexts:wlsxMonAPDATypeStatsEntry.setStatus(_A)
_MonAPStatsTotDABroadcastPkts_Type=Counter32
_MonAPStatsTotDABroadcastPkts_Object=MibTableColumn
monAPStatsTotDABroadcastPkts=_MonAPStatsTotDABroadcastPkts_Object((1,3,6,1,4,1,14823,2,2,1,6,6,1,3,1,1),_MonAPStatsTotDABroadcastPkts_Type())
monAPStatsTotDABroadcastPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:monAPStatsTotDABroadcastPkts.setStatus(_A)
_MonAPStatsTotDABroadcastBytes_Type=Counter32
_MonAPStatsTotDABroadcastBytes_Object=MibTableColumn
monAPStatsTotDABroadcastBytes=_MonAPStatsTotDABroadcastBytes_Object((1,3,6,1,4,1,14823,2,2,1,6,6,1,3,1,2),_MonAPStatsTotDABroadcastBytes_Type())
monAPStatsTotDABroadcastBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:monAPStatsTotDABroadcastBytes.setStatus(_A)
_MonAPStatsTotDAMulticastPkts_Type=Counter32
_MonAPStatsTotDAMulticastPkts_Object=MibTableColumn
monAPStatsTotDAMulticastPkts=_MonAPStatsTotDAMulticastPkts_Object((1,3,6,1,4,1,14823,2,2,1,6,6,1,3,1,3),_MonAPStatsTotDAMulticastPkts_Type())
monAPStatsTotDAMulticastPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:monAPStatsTotDAMulticastPkts.setStatus(_A)
_MonAPStatsTotDAMulticastBytes_Type=Counter32
_MonAPStatsTotDAMulticastBytes_Object=MibTableColumn
monAPStatsTotDAMulticastBytes=_MonAPStatsTotDAMulticastBytes_Object((1,3,6,1,4,1,14823,2,2,1,6,6,1,3,1,4),_MonAPStatsTotDAMulticastBytes_Type())
monAPStatsTotDAMulticastBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:monAPStatsTotDAMulticastBytes.setStatus(_A)
_MonAPStatsTotDAUnicastPkts_Type=Counter32
_MonAPStatsTotDAUnicastPkts_Object=MibTableColumn
monAPStatsTotDAUnicastPkts=_MonAPStatsTotDAUnicastPkts_Object((1,3,6,1,4,1,14823,2,2,1,6,6,1,3,1,5),_MonAPStatsTotDAUnicastPkts_Type())
monAPStatsTotDAUnicastPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:monAPStatsTotDAUnicastPkts.setStatus(_A)
_MonAPStatsTotDAUnicastBytes_Type=Counter32
_MonAPStatsTotDAUnicastBytes_Object=MibTableColumn
monAPStatsTotDAUnicastBytes=_MonAPStatsTotDAUnicastBytes_Object((1,3,6,1,4,1,14823,2,2,1,6,6,1,3,1,6),_MonAPStatsTotDAUnicastBytes_Type())
monAPStatsTotDAUnicastBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:monAPStatsTotDAUnicastBytes.setStatus(_A)
_WlsxMonAPFrameTypeStatsTable_Object=MibTable
wlsxMonAPFrameTypeStatsTable=_WlsxMonAPFrameTypeStatsTable_Object((1,3,6,1,4,1,14823,2,2,1,6,6,1,4))
if mibBuilder.loadTexts:wlsxMonAPFrameTypeStatsTable.setStatus(_A)
_WlsxMonAPFrameTypeStatsEntry_Object=MibTableRow
wlsxMonAPFrameTypeStatsEntry=_WlsxMonAPFrameTypeStatsEntry_Object((1,3,6,1,4,1,14823,2,2,1,6,6,1,4,1))
wlsxMonAPFrameTypeStatsEntry.setIndexNames((0,_C,_D),(0,_C,_E),(0,_C,_F))
if mibBuilder.loadTexts:wlsxMonAPFrameTypeStatsEntry.setStatus(_A)
_MonAPStatsTotMgmtPkts_Type=Counter32
_MonAPStatsTotMgmtPkts_Object=MibTableColumn
monAPStatsTotMgmtPkts=_MonAPStatsTotMgmtPkts_Object((1,3,6,1,4,1,14823,2,2,1,6,6,1,4,1,1),_MonAPStatsTotMgmtPkts_Type())
monAPStatsTotMgmtPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:monAPStatsTotMgmtPkts.setStatus(_A)
_MonAPStatsTotMgmtBytes_Type=Counter32
_MonAPStatsTotMgmtBytes_Object=MibTableColumn
monAPStatsTotMgmtBytes=_MonAPStatsTotMgmtBytes_Object((1,3,6,1,4,1,14823,2,2,1,6,6,1,4,1,2),_MonAPStatsTotMgmtBytes_Type())
monAPStatsTotMgmtBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:monAPStatsTotMgmtBytes.setStatus(_A)
_MonAPStatsTotCtrlPkts_Type=Counter32
_MonAPStatsTotCtrlPkts_Object=MibTableColumn
monAPStatsTotCtrlPkts=_MonAPStatsTotCtrlPkts_Object((1,3,6,1,4,1,14823,2,2,1,6,6,1,4,1,3),_MonAPStatsTotCtrlPkts_Type())
monAPStatsTotCtrlPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:monAPStatsTotCtrlPkts.setStatus(_A)
_MonAPStatsTotCtrlBytes_Type=Counter32
_MonAPStatsTotCtrlBytes_Object=MibTableColumn
monAPStatsTotCtrlBytes=_MonAPStatsTotCtrlBytes_Object((1,3,6,1,4,1,14823,2,2,1,6,6,1,4,1,4),_MonAPStatsTotCtrlBytes_Type())
monAPStatsTotCtrlBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:monAPStatsTotCtrlBytes.setStatus(_A)
_MonAPStatsTotDataPkts_Type=Counter32
_MonAPStatsTotDataPkts_Object=MibTableColumn
monAPStatsTotDataPkts=_MonAPStatsTotDataPkts_Object((1,3,6,1,4,1,14823,2,2,1,6,6,1,4,1,5),_MonAPStatsTotDataPkts_Type())
monAPStatsTotDataPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:monAPStatsTotDataPkts.setStatus(_A)
_MonAPStatsTotDataBytes_Type=Counter32
_MonAPStatsTotDataBytes_Object=MibTableColumn
monAPStatsTotDataBytes=_MonAPStatsTotDataBytes_Object((1,3,6,1,4,1,14823,2,2,1,6,6,1,4,1,6),_MonAPStatsTotDataBytes_Type())
monAPStatsTotDataBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:monAPStatsTotDataBytes.setStatus(_A)
_WlsxMonAPPktSizeStatsTable_Object=MibTable
wlsxMonAPPktSizeStatsTable=_WlsxMonAPPktSizeStatsTable_Object((1,3,6,1,4,1,14823,2,2,1,6,6,1,5))
if mibBuilder.loadTexts:wlsxMonAPPktSizeStatsTable.setStatus(_A)
_WlsxMonAPPktSizeStatsEntry_Object=MibTableRow
wlsxMonAPPktSizeStatsEntry=_WlsxMonAPPktSizeStatsEntry_Object((1,3,6,1,4,1,14823,2,2,1,6,6,1,5,1))
wlsxMonAPPktSizeStatsEntry.setIndexNames((0,_C,_D),(0,_C,_E),(0,_C,_F))
if mibBuilder.loadTexts:wlsxMonAPPktSizeStatsEntry.setStatus(_A)
_MonAPStatsPkts63Bytes_Type=Counter32
_MonAPStatsPkts63Bytes_Object=MibTableColumn
monAPStatsPkts63Bytes=_MonAPStatsPkts63Bytes_Object((1,3,6,1,4,1,14823,2,2,1,6,6,1,5,1,1),_MonAPStatsPkts63Bytes_Type())
monAPStatsPkts63Bytes.setMaxAccess(_B)
if mibBuilder.loadTexts:monAPStatsPkts63Bytes.setStatus(_A)
_MonAPStatsPkts64To127_Type=Counter32
_MonAPStatsPkts64To127_Object=MibTableColumn
monAPStatsPkts64To127=_MonAPStatsPkts64To127_Object((1,3,6,1,4,1,14823,2,2,1,6,6,1,5,1,2),_MonAPStatsPkts64To127_Type())
monAPStatsPkts64To127.setMaxAccess(_B)
if mibBuilder.loadTexts:monAPStatsPkts64To127.setStatus(_A)
_MonAPStatsPkts128To255_Type=Counter32
_MonAPStatsPkts128To255_Object=MibTableColumn
monAPStatsPkts128To255=_MonAPStatsPkts128To255_Object((1,3,6,1,4,1,14823,2,2,1,6,6,1,5,1,3),_MonAPStatsPkts128To255_Type())
monAPStatsPkts128To255.setMaxAccess(_B)
if mibBuilder.loadTexts:monAPStatsPkts128To255.setStatus(_A)
_MonAPStatsPkts256To511_Type=Counter32
_MonAPStatsPkts256To511_Object=MibTableColumn
monAPStatsPkts256To511=_MonAPStatsPkts256To511_Object((1,3,6,1,4,1,14823,2,2,1,6,6,1,5,1,4),_MonAPStatsPkts256To511_Type())
monAPStatsPkts256To511.setMaxAccess(_B)
if mibBuilder.loadTexts:monAPStatsPkts256To511.setStatus(_A)
_MonAPStatsPkts512To1023_Type=Counter32
_MonAPStatsPkts512To1023_Object=MibTableColumn
monAPStatsPkts512To1023=_MonAPStatsPkts512To1023_Object((1,3,6,1,4,1,14823,2,2,1,6,6,1,5,1,5),_MonAPStatsPkts512To1023_Type())
monAPStatsPkts512To1023.setMaxAccess(_B)
if mibBuilder.loadTexts:monAPStatsPkts512To1023.setStatus(_A)
_MonAPStatsPkts1024To1518_Type=Counter32
_MonAPStatsPkts1024To1518_Object=MibTableColumn
monAPStatsPkts1024To1518=_MonAPStatsPkts1024To1518_Object((1,3,6,1,4,1,14823,2,2,1,6,6,1,5,1,6),_MonAPStatsPkts1024To1518_Type())
monAPStatsPkts1024To1518.setMaxAccess(_B)
if mibBuilder.loadTexts:monAPStatsPkts1024To1518.setStatus(_A)
_WlsxMonAPHTRateStatsTable_Object=MibTable
wlsxMonAPHTRateStatsTable=_WlsxMonAPHTRateStatsTable_Object((1,3,6,1,4,1,14823,2,2,1,6,6,1,6))
if mibBuilder.loadTexts:wlsxMonAPHTRateStatsTable.setStatus(_A)
_WlsxMonAPHTRateStatsEntry_Object=MibTableRow
wlsxMonAPHTRateStatsEntry=_WlsxMonAPHTRateStatsEntry_Object((1,3,6,1,4,1,14823,2,2,1,6,6,1,6,1))
wlsxMonAPHTRateStatsEntry.setIndexNames((0,_C,_D),(0,_C,_E),(0,_C,_F),(0,_C,_J))
if mibBuilder.loadTexts:wlsxMonAPHTRateStatsEntry.setStatus(_A)
_MonHTRate_Type=ArubaHTRate
_MonHTRate_Object=MibTableColumn
monHTRate=_MonHTRate_Object((1,3,6,1,4,1,14823,2,2,1,6,6,1,6,1,1),_MonHTRate_Type())
monHTRate.setMaxAccess(_B)
if mibBuilder.loadTexts:monHTRate.setStatus(_A)
_MonAPStatsTotHTPkts_Type=Counter32
_MonAPStatsTotHTPkts_Object=MibTableColumn
monAPStatsTotHTPkts=_MonAPStatsTotHTPkts_Object((1,3,6,1,4,1,14823,2,2,1,6,6,1,6,1,2),_MonAPStatsTotHTPkts_Type())
monAPStatsTotHTPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:monAPStatsTotHTPkts.setStatus(_A)
_MonAPStatsTotHTBytes_Type=Counter32
_MonAPStatsTotHTBytes_Object=MibTableColumn
monAPStatsTotHTBytes=_MonAPStatsTotHTBytes_Object((1,3,6,1,4,1,14823,2,2,1,6,6,1,6,1,3),_MonAPStatsTotHTBytes_Type())
monAPStatsTotHTBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:monAPStatsTotHTBytes.setStatus(_A)
_WlsxMonStationStatsGroup_ObjectIdentity=ObjectIdentity
wlsxMonStationStatsGroup=_WlsxMonStationStatsGroup_ObjectIdentity((1,3,6,1,4,1,14823,2,2,1,6,6,2))
_WlsxMonStationStatsTable_Object=MibTable
wlsxMonStationStatsTable=_WlsxMonStationStatsTable_Object((1,3,6,1,4,1,14823,2,2,1,6,6,2,1))
if mibBuilder.loadTexts:wlsxMonStationStatsTable.setStatus(_A)
_WlsxMonStationStatsEntry_Object=MibTableRow
wlsxMonStationStatsEntry=_WlsxMonStationStatsEntry_Object((1,3,6,1,4,1,14823,2,2,1,6,6,2,1,1))
wlsxMonStationStatsEntry.setIndexNames((0,_C,_D),(0,_C,_E),(0,_C,_G))
if mibBuilder.loadTexts:wlsxMonStationStatsEntry.setStatus(_A)
_MonitoredStaPhyAddress_Type=MacAddress
_MonitoredStaPhyAddress_Object=MibTableColumn
monitoredStaPhyAddress=_MonitoredStaPhyAddress_Object((1,3,6,1,4,1,14823,2,2,1,6,6,2,1,1,1),_MonitoredStaPhyAddress_Type())
monitoredStaPhyAddress.setMaxAccess(_H)
if mibBuilder.loadTexts:monitoredStaPhyAddress.setStatus(_A)
_MonStaChannelNum_Type=Unsigned32
_MonStaChannelNum_Object=MibTableColumn
monStaChannelNum=_MonStaChannelNum_Object((1,3,6,1,4,1,14823,2,2,1,6,6,2,1,1,2),_MonStaChannelNum_Type())
monStaChannelNum.setMaxAccess(_B)
if mibBuilder.loadTexts:monStaChannelNum.setStatus(_A)
_MonStaTxPkts_Type=Counter32
_MonStaTxPkts_Object=MibTableColumn
monStaTxPkts=_MonStaTxPkts_Object((1,3,6,1,4,1,14823,2,2,1,6,6,2,1,1,3),_MonStaTxPkts_Type())
monStaTxPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:monStaTxPkts.setStatus(_A)
_MonStaTxBytes_Type=Counter32
_MonStaTxBytes_Object=MibTableColumn
monStaTxBytes=_MonStaTxBytes_Object((1,3,6,1,4,1,14823,2,2,1,6,6,2,1,1,4),_MonStaTxBytes_Type())
monStaTxBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:monStaTxBytes.setStatus(_A)
_MonStaRxPkts_Type=Counter32
_MonStaRxPkts_Object=MibTableColumn
monStaRxPkts=_MonStaRxPkts_Object((1,3,6,1,4,1,14823,2,2,1,6,6,2,1,1,5),_MonStaRxPkts_Type())
monStaRxPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:monStaRxPkts.setStatus(_A)
_MonStaRxBytes_Type=Counter32
_MonStaRxBytes_Object=MibTableColumn
monStaRxBytes=_MonStaRxBytes_Object((1,3,6,1,4,1,14823,2,2,1,6,6,2,1,1,6),_MonStaRxBytes_Type())
monStaRxBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:monStaRxBytes.setStatus(_A)
_MonStaTxBCastPkts_Type=Counter32
_MonStaTxBCastPkts_Object=MibTableColumn
monStaTxBCastPkts=_MonStaTxBCastPkts_Object((1,3,6,1,4,1,14823,2,2,1,6,6,2,1,1,7),_MonStaTxBCastPkts_Type())
monStaTxBCastPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:monStaTxBCastPkts.setStatus(_A)
_MonStaTxBCastBytes_Type=Counter32
_MonStaTxBCastBytes_Object=MibTableColumn
monStaTxBCastBytes=_MonStaTxBCastBytes_Object((1,3,6,1,4,1,14823,2,2,1,6,6,2,1,1,8),_MonStaTxBCastBytes_Type())
monStaTxBCastBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:monStaTxBCastBytes.setStatus(_A)
_MonStaTxMCastPkts_Type=Counter32
_MonStaTxMCastPkts_Object=MibTableColumn
monStaTxMCastPkts=_MonStaTxMCastPkts_Object((1,3,6,1,4,1,14823,2,2,1,6,6,2,1,1,9),_MonStaTxMCastPkts_Type())
monStaTxMCastPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:monStaTxMCastPkts.setStatus(_A)
_MonStaTxMCastBytes_Type=Counter32
_MonStaTxMCastBytes_Object=MibTableColumn
monStaTxMCastBytes=_MonStaTxMCastBytes_Object((1,3,6,1,4,1,14823,2,2,1,6,6,2,1,1,10),_MonStaTxMCastBytes_Type())
monStaTxMCastBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:monStaTxMCastBytes.setStatus(_A)
_MonStaDataPkts_Type=Counter32
_MonStaDataPkts_Object=MibTableColumn
monStaDataPkts=_MonStaDataPkts_Object((1,3,6,1,4,1,14823,2,2,1,6,6,2,1,1,11),_MonStaDataPkts_Type())
monStaDataPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:monStaDataPkts.setStatus(_A)
_MonStaCtrlPkts_Type=Counter32
_MonStaCtrlPkts_Object=MibTableColumn
monStaCtrlPkts=_MonStaCtrlPkts_Object((1,3,6,1,4,1,14823,2,2,1,6,6,2,1,1,12),_MonStaCtrlPkts_Type())
monStaCtrlPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:monStaCtrlPkts.setStatus(_A)
_MonStaNumAssocRequests_Type=Counter32
_MonStaNumAssocRequests_Object=MibTableColumn
monStaNumAssocRequests=_MonStaNumAssocRequests_Object((1,3,6,1,4,1,14823,2,2,1,6,6,2,1,1,13),_MonStaNumAssocRequests_Type())
monStaNumAssocRequests.setMaxAccess(_B)
if mibBuilder.loadTexts:monStaNumAssocRequests.setStatus(_A)
_MonStaNumAuthRequests_Type=Counter32
_MonStaNumAuthRequests_Object=MibTableColumn
monStaNumAuthRequests=_MonStaNumAuthRequests_Object((1,3,6,1,4,1,14823,2,2,1,6,6,2,1,1,14),_MonStaNumAuthRequests_Type())
monStaNumAuthRequests.setMaxAccess(_B)
if mibBuilder.loadTexts:monStaNumAuthRequests.setStatus(_A)
_MonStaTxDeauthentications_Type=Counter32
_MonStaTxDeauthentications_Object=MibTableColumn
monStaTxDeauthentications=_MonStaTxDeauthentications_Object((1,3,6,1,4,1,14823,2,2,1,6,6,2,1,1,15),_MonStaTxDeauthentications_Type())
monStaTxDeauthentications.setMaxAccess(_B)
if mibBuilder.loadTexts:monStaTxDeauthentications.setStatus(_A)
_MonStaRxDeauthentications_Type=Counter32
_MonStaRxDeauthentications_Object=MibTableColumn
monStaRxDeauthentications=_MonStaRxDeauthentications_Object((1,3,6,1,4,1,14823,2,2,1,6,6,2,1,1,16),_MonStaRxDeauthentications_Type())
monStaRxDeauthentications.setMaxAccess(_B)
if mibBuilder.loadTexts:monStaRxDeauthentications.setStatus(_A)
_MonStaFrameRetryRate_Type=Integer32
_MonStaFrameRetryRate_Object=MibTableColumn
monStaFrameRetryRate=_MonStaFrameRetryRate_Object((1,3,6,1,4,1,14823,2,2,1,6,6,2,1,1,17),_MonStaFrameRetryRate_Type())
monStaFrameRetryRate.setMaxAccess(_B)
if mibBuilder.loadTexts:monStaFrameRetryRate.setStatus(_A)
_MonStaFrameLowSpeedRate_Type=Integer32
_MonStaFrameLowSpeedRate_Object=MibTableColumn
monStaFrameLowSpeedRate=_MonStaFrameLowSpeedRate_Object((1,3,6,1,4,1,14823,2,2,1,6,6,2,1,1,18),_MonStaFrameLowSpeedRate_Type())
monStaFrameLowSpeedRate.setMaxAccess(_B)
if mibBuilder.loadTexts:monStaFrameLowSpeedRate.setStatus(_A)
_MonStaFrameNonUnicastRate_Type=Integer32
_MonStaFrameNonUnicastRate_Object=MibTableColumn
monStaFrameNonUnicastRate=_MonStaFrameNonUnicastRate_Object((1,3,6,1,4,1,14823,2,2,1,6,6,2,1,1,19),_MonStaFrameNonUnicastRate_Type())
monStaFrameNonUnicastRate.setMaxAccess(_B)
if mibBuilder.loadTexts:monStaFrameNonUnicastRate.setStatus(_A)
_MonStaFrameFragmentationRate_Type=Integer32
_MonStaFrameFragmentationRate_Object=MibTableColumn
monStaFrameFragmentationRate=_MonStaFrameFragmentationRate_Object((1,3,6,1,4,1,14823,2,2,1,6,6,2,1,1,20),_MonStaFrameFragmentationRate_Type())
monStaFrameFragmentationRate.setMaxAccess(_B)
if mibBuilder.loadTexts:monStaFrameFragmentationRate.setStatus(_A)
_MonStaFrameBandwidthRate_Type=Integer32
_MonStaFrameBandwidthRate_Object=MibTableColumn
monStaFrameBandwidthRate=_MonStaFrameBandwidthRate_Object((1,3,6,1,4,1,14823,2,2,1,6,6,2,1,1,21),_MonStaFrameBandwidthRate_Type())
monStaFrameBandwidthRate.setMaxAccess(_B)
if mibBuilder.loadTexts:monStaFrameBandwidthRate.setStatus(_A)
_MonStaFrameRetryErrorRate_Type=Integer32
_MonStaFrameRetryErrorRate_Object=MibTableColumn
monStaFrameRetryErrorRate=_MonStaFrameRetryErrorRate_Object((1,3,6,1,4,1,14823,2,2,1,6,6,2,1,1,22),_MonStaFrameRetryErrorRate_Type())
monStaFrameRetryErrorRate.setMaxAccess(_B)
if mibBuilder.loadTexts:monStaFrameRetryErrorRate.setStatus(_K)
_MonStaBSSID_Type=MacAddress
_MonStaBSSID_Object=MibTableColumn
monStaBSSID=_MonStaBSSID_Object((1,3,6,1,4,1,14823,2,2,1,6,6,2,1,1,23),_MonStaBSSID_Type())
monStaBSSID.setMaxAccess(_B)
if mibBuilder.loadTexts:monStaBSSID.setStatus(_A)
_MonStaESSID_Type=DisplayString
_MonStaESSID_Object=MibTableColumn
monStaESSID=_MonStaESSID_Object((1,3,6,1,4,1,14823,2,2,1,6,6,2,1,1,24),_MonStaESSID_Type())
monStaESSID.setMaxAccess(_B)
if mibBuilder.loadTexts:monStaESSID.setStatus(_A)
_MonStaPhyType_Type=ArubaPhyType
_MonStaPhyType_Object=MibTableColumn
monStaPhyType=_MonStaPhyType_Object((1,3,6,1,4,1,14823,2,2,1,6,6,2,1,1,25),_MonStaPhyType_Type())
monStaPhyType.setMaxAccess(_B)
if mibBuilder.loadTexts:monStaPhyType.setStatus(_A)
_MonStaRSSI_Type=Integer32
_MonStaRSSI_Object=MibTableColumn
monStaRSSI=_MonStaRSSI_Object((1,3,6,1,4,1,14823,2,2,1,6,6,2,1,1,26),_MonStaRSSI_Type())
monStaRSSI.setMaxAccess(_B)
if mibBuilder.loadTexts:monStaRSSI.setStatus(_A)
_MonStaFrameReceiveErrorRate_Type=Integer32
_MonStaFrameReceiveErrorRate_Object=MibTableColumn
monStaFrameReceiveErrorRate=_MonStaFrameReceiveErrorRate_Object((1,3,6,1,4,1,14823,2,2,1,6,6,2,1,1,27),_MonStaFrameReceiveErrorRate_Type())
monStaFrameReceiveErrorRate.setMaxAccess(_B)
if mibBuilder.loadTexts:monStaFrameReceiveErrorRate.setStatus(_A)
_WlsxMonStaRateStatsTable_Object=MibTable
wlsxMonStaRateStatsTable=_WlsxMonStaRateStatsTable_Object((1,3,6,1,4,1,14823,2,2,1,6,6,2,2))
if mibBuilder.loadTexts:wlsxMonStaRateStatsTable.setStatus(_A)
_WlsxMonStaRateStatsEntry_Object=MibTableRow
wlsxMonStaRateStatsEntry=_WlsxMonStaRateStatsEntry_Object((1,3,6,1,4,1,14823,2,2,1,6,6,2,2,1))
wlsxMonStaRateStatsEntry.setIndexNames((0,_C,_D),(0,_C,_E),(0,_C,_G))
if mibBuilder.loadTexts:wlsxMonStaRateStatsEntry.setStatus(_A)
_MonStaTxPktsAt1Mbps_Type=Counter32
_MonStaTxPktsAt1Mbps_Object=MibTableColumn
monStaTxPktsAt1Mbps=_MonStaTxPktsAt1Mbps_Object((1,3,6,1,4,1,14823,2,2,1,6,6,2,2,1,1),_MonStaTxPktsAt1Mbps_Type())
monStaTxPktsAt1Mbps.setMaxAccess(_B)
if mibBuilder.loadTexts:monStaTxPktsAt1Mbps.setStatus(_A)
_MonStaTxBytesAt1Mbps_Type=Counter32
_MonStaTxBytesAt1Mbps_Object=MibTableColumn
monStaTxBytesAt1Mbps=_MonStaTxBytesAt1Mbps_Object((1,3,6,1,4,1,14823,2,2,1,6,6,2,2,1,2),_MonStaTxBytesAt1Mbps_Type())
monStaTxBytesAt1Mbps.setMaxAccess(_B)
if mibBuilder.loadTexts:monStaTxBytesAt1Mbps.setStatus(_A)
_MonStaTxPktsAt2Mbps_Type=Counter32
_MonStaTxPktsAt2Mbps_Object=MibTableColumn
monStaTxPktsAt2Mbps=_MonStaTxPktsAt2Mbps_Object((1,3,6,1,4,1,14823,2,2,1,6,6,2,2,1,3),_MonStaTxPktsAt2Mbps_Type())
monStaTxPktsAt2Mbps.setMaxAccess(_B)
if mibBuilder.loadTexts:monStaTxPktsAt2Mbps.setStatus(_A)
_MonStaTxBytesAt2Mbps_Type=Counter32
_MonStaTxBytesAt2Mbps_Object=MibTableColumn
monStaTxBytesAt2Mbps=_MonStaTxBytesAt2Mbps_Object((1,3,6,1,4,1,14823,2,2,1,6,6,2,2,1,4),_MonStaTxBytesAt2Mbps_Type())
monStaTxBytesAt2Mbps.setMaxAccess(_B)
if mibBuilder.loadTexts:monStaTxBytesAt2Mbps.setStatus(_A)
_MonStaTxPktsAt5Mbps_Type=Counter32
_MonStaTxPktsAt5Mbps_Object=MibTableColumn
monStaTxPktsAt5Mbps=_MonStaTxPktsAt5Mbps_Object((1,3,6,1,4,1,14823,2,2,1,6,6,2,2,1,5),_MonStaTxPktsAt5Mbps_Type())
monStaTxPktsAt5Mbps.setMaxAccess(_B)
if mibBuilder.loadTexts:monStaTxPktsAt5Mbps.setStatus(_A)
_MonStaTxBytesAt5Mbps_Type=Counter32
_MonStaTxBytesAt5Mbps_Object=MibTableColumn
monStaTxBytesAt5Mbps=_MonStaTxBytesAt5Mbps_Object((1,3,6,1,4,1,14823,2,2,1,6,6,2,2,1,6),_MonStaTxBytesAt5Mbps_Type())
monStaTxBytesAt5Mbps.setMaxAccess(_B)
if mibBuilder.loadTexts:monStaTxBytesAt5Mbps.setStatus(_A)
_MonStaTxPktsAt11Mbps_Type=Counter32
_MonStaTxPktsAt11Mbps_Object=MibTableColumn
monStaTxPktsAt11Mbps=_MonStaTxPktsAt11Mbps_Object((1,3,6,1,4,1,14823,2,2,1,6,6,2,2,1,7),_MonStaTxPktsAt11Mbps_Type())
monStaTxPktsAt11Mbps.setMaxAccess(_B)
if mibBuilder.loadTexts:monStaTxPktsAt11Mbps.setStatus(_A)
_MonStaTxBytesAt11Mbps_Type=Counter32
_MonStaTxBytesAt11Mbps_Object=MibTableColumn
monStaTxBytesAt11Mbps=_MonStaTxBytesAt11Mbps_Object((1,3,6,1,4,1,14823,2,2,1,6,6,2,2,1,8),_MonStaTxBytesAt11Mbps_Type())
monStaTxBytesAt11Mbps.setMaxAccess(_B)
if mibBuilder.loadTexts:monStaTxBytesAt11Mbps.setStatus(_A)
_MonStaTxPktsAt6Mbps_Type=Counter32
_MonStaTxPktsAt6Mbps_Object=MibTableColumn
monStaTxPktsAt6Mbps=_MonStaTxPktsAt6Mbps_Object((1,3,6,1,4,1,14823,2,2,1,6,6,2,2,1,9),_MonStaTxPktsAt6Mbps_Type())
monStaTxPktsAt6Mbps.setMaxAccess(_B)
if mibBuilder.loadTexts:monStaTxPktsAt6Mbps.setStatus(_A)
_MonStaTxBytesAt6Mbps_Type=Counter32
_MonStaTxBytesAt6Mbps_Object=MibTableColumn
monStaTxBytesAt6Mbps=_MonStaTxBytesAt6Mbps_Object((1,3,6,1,4,1,14823,2,2,1,6,6,2,2,1,10),_MonStaTxBytesAt6Mbps_Type())
monStaTxBytesAt6Mbps.setMaxAccess(_B)
if mibBuilder.loadTexts:monStaTxBytesAt6Mbps.setStatus(_A)
_MonStaTxPktsAt12Mbps_Type=Counter32
_MonStaTxPktsAt12Mbps_Object=MibTableColumn
monStaTxPktsAt12Mbps=_MonStaTxPktsAt12Mbps_Object((1,3,6,1,4,1,14823,2,2,1,6,6,2,2,1,11),_MonStaTxPktsAt12Mbps_Type())
monStaTxPktsAt12Mbps.setMaxAccess(_B)
if mibBuilder.loadTexts:monStaTxPktsAt12Mbps.setStatus(_A)
_MonStaTxBytesAt12Mbps_Type=Counter32
_MonStaTxBytesAt12Mbps_Object=MibTableColumn
monStaTxBytesAt12Mbps=_MonStaTxBytesAt12Mbps_Object((1,3,6,1,4,1,14823,2,2,1,6,6,2,2,1,12),_MonStaTxBytesAt12Mbps_Type())
monStaTxBytesAt12Mbps.setMaxAccess(_B)
if mibBuilder.loadTexts:monStaTxBytesAt12Mbps.setStatus(_A)
_MonStaTxPktsAt18Mbps_Type=Counter32
_MonStaTxPktsAt18Mbps_Object=MibTableColumn
monStaTxPktsAt18Mbps=_MonStaTxPktsAt18Mbps_Object((1,3,6,1,4,1,14823,2,2,1,6,6,2,2,1,13),_MonStaTxPktsAt18Mbps_Type())
monStaTxPktsAt18Mbps.setMaxAccess(_B)
if mibBuilder.loadTexts:monStaTxPktsAt18Mbps.setStatus(_A)
_MonStaTxBytesAt18Mbps_Type=Counter32
_MonStaTxBytesAt18Mbps_Object=MibTableColumn
monStaTxBytesAt18Mbps=_MonStaTxBytesAt18Mbps_Object((1,3,6,1,4,1,14823,2,2,1,6,6,2,2,1,14),_MonStaTxBytesAt18Mbps_Type())
monStaTxBytesAt18Mbps.setMaxAccess(_B)
if mibBuilder.loadTexts:monStaTxBytesAt18Mbps.setStatus(_A)
_MonStaTxPktsAt24Mbps_Type=Counter32
_MonStaTxPktsAt24Mbps_Object=MibTableColumn
monStaTxPktsAt24Mbps=_MonStaTxPktsAt24Mbps_Object((1,3,6,1,4,1,14823,2,2,1,6,6,2,2,1,15),_MonStaTxPktsAt24Mbps_Type())
monStaTxPktsAt24Mbps.setMaxAccess(_B)
if mibBuilder.loadTexts:monStaTxPktsAt24Mbps.setStatus(_A)
_MonStaTxBytesAt24Mbps_Type=Counter32
_MonStaTxBytesAt24Mbps_Object=MibTableColumn
monStaTxBytesAt24Mbps=_MonStaTxBytesAt24Mbps_Object((1,3,6,1,4,1,14823,2,2,1,6,6,2,2,1,16),_MonStaTxBytesAt24Mbps_Type())
monStaTxBytesAt24Mbps.setMaxAccess(_B)
if mibBuilder.loadTexts:monStaTxBytesAt24Mbps.setStatus(_A)
_MonStaTxPktsAt36Mbps_Type=Counter32
_MonStaTxPktsAt36Mbps_Object=MibTableColumn
monStaTxPktsAt36Mbps=_MonStaTxPktsAt36Mbps_Object((1,3,6,1,4,1,14823,2,2,1,6,6,2,2,1,17),_MonStaTxPktsAt36Mbps_Type())
monStaTxPktsAt36Mbps.setMaxAccess(_B)
if mibBuilder.loadTexts:monStaTxPktsAt36Mbps.setStatus(_A)
_MonStaTxBytesAt36Mbps_Type=Counter32
_MonStaTxBytesAt36Mbps_Object=MibTableColumn
monStaTxBytesAt36Mbps=_MonStaTxBytesAt36Mbps_Object((1,3,6,1,4,1,14823,2,2,1,6,6,2,2,1,18),_MonStaTxBytesAt36Mbps_Type())
monStaTxBytesAt36Mbps.setMaxAccess(_B)
if mibBuilder.loadTexts:monStaTxBytesAt36Mbps.setStatus(_A)
_MonStaTxPktsAt48Mbps_Type=Counter32
_MonStaTxPktsAt48Mbps_Object=MibTableColumn
monStaTxPktsAt48Mbps=_MonStaTxPktsAt48Mbps_Object((1,3,6,1,4,1,14823,2,2,1,6,6,2,2,1,19),_MonStaTxPktsAt48Mbps_Type())
monStaTxPktsAt48Mbps.setMaxAccess(_B)
if mibBuilder.loadTexts:monStaTxPktsAt48Mbps.setStatus(_A)
_MonStaTxBytesAt48Mbps_Type=Counter32
_MonStaTxBytesAt48Mbps_Object=MibTableColumn
monStaTxBytesAt48Mbps=_MonStaTxBytesAt48Mbps_Object((1,3,6,1,4,1,14823,2,2,1,6,6,2,2,1,20),_MonStaTxBytesAt48Mbps_Type())
monStaTxBytesAt48Mbps.setMaxAccess(_B)
if mibBuilder.loadTexts:monStaTxBytesAt48Mbps.setStatus(_A)
_MonStaTxPktsAt54Mbps_Type=Counter32
_MonStaTxPktsAt54Mbps_Object=MibTableColumn
monStaTxPktsAt54Mbps=_MonStaTxPktsAt54Mbps_Object((1,3,6,1,4,1,14823,2,2,1,6,6,2,2,1,21),_MonStaTxPktsAt54Mbps_Type())
monStaTxPktsAt54Mbps.setMaxAccess(_B)
if mibBuilder.loadTexts:monStaTxPktsAt54Mbps.setStatus(_A)
_MonStaTxBytesAt54Mbps_Type=Counter32
_MonStaTxBytesAt54Mbps_Object=MibTableColumn
monStaTxBytesAt54Mbps=_MonStaTxBytesAt54Mbps_Object((1,3,6,1,4,1,14823,2,2,1,6,6,2,2,1,22),_MonStaTxBytesAt54Mbps_Type())
monStaTxBytesAt54Mbps.setMaxAccess(_B)
if mibBuilder.loadTexts:monStaTxBytesAt54Mbps.setStatus(_A)
_MonStaRxPktsAt1Mbps_Type=Counter32
_MonStaRxPktsAt1Mbps_Object=MibTableColumn
monStaRxPktsAt1Mbps=_MonStaRxPktsAt1Mbps_Object((1,3,6,1,4,1,14823,2,2,1,6,6,2,2,1,23),_MonStaRxPktsAt1Mbps_Type())
monStaRxPktsAt1Mbps.setMaxAccess(_B)
if mibBuilder.loadTexts:monStaRxPktsAt1Mbps.setStatus(_A)
_MonStaRxBytesAt1Mbps_Type=Counter32
_MonStaRxBytesAt1Mbps_Object=MibTableColumn
monStaRxBytesAt1Mbps=_MonStaRxBytesAt1Mbps_Object((1,3,6,1,4,1,14823,2,2,1,6,6,2,2,1,24),_MonStaRxBytesAt1Mbps_Type())
monStaRxBytesAt1Mbps.setMaxAccess(_B)
if mibBuilder.loadTexts:monStaRxBytesAt1Mbps.setStatus(_A)
_MonStaRxPktsAt2Mbps_Type=Counter32
_MonStaRxPktsAt2Mbps_Object=MibTableColumn
monStaRxPktsAt2Mbps=_MonStaRxPktsAt2Mbps_Object((1,3,6,1,4,1,14823,2,2,1,6,6,2,2,1,25),_MonStaRxPktsAt2Mbps_Type())
monStaRxPktsAt2Mbps.setMaxAccess(_B)
if mibBuilder.loadTexts:monStaRxPktsAt2Mbps.setStatus(_A)
_MonStaRxBytesAt2Mbps_Type=Counter32
_MonStaRxBytesAt2Mbps_Object=MibTableColumn
monStaRxBytesAt2Mbps=_MonStaRxBytesAt2Mbps_Object((1,3,6,1,4,1,14823,2,2,1,6,6,2,2,1,26),_MonStaRxBytesAt2Mbps_Type())
monStaRxBytesAt2Mbps.setMaxAccess(_B)
if mibBuilder.loadTexts:monStaRxBytesAt2Mbps.setStatus(_A)
_MonStaRxPktsAt5Mbps_Type=Counter32
_MonStaRxPktsAt5Mbps_Object=MibTableColumn
monStaRxPktsAt5Mbps=_MonStaRxPktsAt5Mbps_Object((1,3,6,1,4,1,14823,2,2,1,6,6,2,2,1,27),_MonStaRxPktsAt5Mbps_Type())
monStaRxPktsAt5Mbps.setMaxAccess(_B)
if mibBuilder.loadTexts:monStaRxPktsAt5Mbps.setStatus(_A)
_MonStaRxBytesAt5Mbps_Type=Counter32
_MonStaRxBytesAt5Mbps_Object=MibTableColumn
monStaRxBytesAt5Mbps=_MonStaRxBytesAt5Mbps_Object((1,3,6,1,4,1,14823,2,2,1,6,6,2,2,1,28),_MonStaRxBytesAt5Mbps_Type())
monStaRxBytesAt5Mbps.setMaxAccess(_B)
if mibBuilder.loadTexts:monStaRxBytesAt5Mbps.setStatus(_A)
_MonStaRxPktsAt11Mbps_Type=Counter32
_MonStaRxPktsAt11Mbps_Object=MibTableColumn
monStaRxPktsAt11Mbps=_MonStaRxPktsAt11Mbps_Object((1,3,6,1,4,1,14823,2,2,1,6,6,2,2,1,29),_MonStaRxPktsAt11Mbps_Type())
monStaRxPktsAt11Mbps.setMaxAccess(_B)
if mibBuilder.loadTexts:monStaRxPktsAt11Mbps.setStatus(_A)
_MonStaRxBytesAt11Mbps_Type=Counter32
_MonStaRxBytesAt11Mbps_Object=MibTableColumn
monStaRxBytesAt11Mbps=_MonStaRxBytesAt11Mbps_Object((1,3,6,1,4,1,14823,2,2,1,6,6,2,2,1,30),_MonStaRxBytesAt11Mbps_Type())
monStaRxBytesAt11Mbps.setMaxAccess(_B)
if mibBuilder.loadTexts:monStaRxBytesAt11Mbps.setStatus(_A)
_MonStaRxPktsAt6Mbps_Type=Counter32
_MonStaRxPktsAt6Mbps_Object=MibTableColumn
monStaRxPktsAt6Mbps=_MonStaRxPktsAt6Mbps_Object((1,3,6,1,4,1,14823,2,2,1,6,6,2,2,1,31),_MonStaRxPktsAt6Mbps_Type())
monStaRxPktsAt6Mbps.setMaxAccess(_B)
if mibBuilder.loadTexts:monStaRxPktsAt6Mbps.setStatus(_A)
_MonStaRxBytesAt6Mbps_Type=Counter32
_MonStaRxBytesAt6Mbps_Object=MibTableColumn
monStaRxBytesAt6Mbps=_MonStaRxBytesAt6Mbps_Object((1,3,6,1,4,1,14823,2,2,1,6,6,2,2,1,32),_MonStaRxBytesAt6Mbps_Type())
monStaRxBytesAt6Mbps.setMaxAccess(_B)
if mibBuilder.loadTexts:monStaRxBytesAt6Mbps.setStatus(_A)
_MonStaRxPktsAt12Mbps_Type=Counter32
_MonStaRxPktsAt12Mbps_Object=MibTableColumn
monStaRxPktsAt12Mbps=_MonStaRxPktsAt12Mbps_Object((1,3,6,1,4,1,14823,2,2,1,6,6,2,2,1,33),_MonStaRxPktsAt12Mbps_Type())
monStaRxPktsAt12Mbps.setMaxAccess(_B)
if mibBuilder.loadTexts:monStaRxPktsAt12Mbps.setStatus(_A)
_MonStaRxBytesAt12Mbps_Type=Counter32
_MonStaRxBytesAt12Mbps_Object=MibTableColumn
monStaRxBytesAt12Mbps=_MonStaRxBytesAt12Mbps_Object((1,3,6,1,4,1,14823,2,2,1,6,6,2,2,1,34),_MonStaRxBytesAt12Mbps_Type())
monStaRxBytesAt12Mbps.setMaxAccess(_B)
if mibBuilder.loadTexts:monStaRxBytesAt12Mbps.setStatus(_A)
_MonStaRxPktsAt18Mbps_Type=Counter32
_MonStaRxPktsAt18Mbps_Object=MibTableColumn
monStaRxPktsAt18Mbps=_MonStaRxPktsAt18Mbps_Object((1,3,6,1,4,1,14823,2,2,1,6,6,2,2,1,35),_MonStaRxPktsAt18Mbps_Type())
monStaRxPktsAt18Mbps.setMaxAccess(_B)
if mibBuilder.loadTexts:monStaRxPktsAt18Mbps.setStatus(_A)
_MonStaRxBytesAt18Mbps_Type=Counter32
_MonStaRxBytesAt18Mbps_Object=MibTableColumn
monStaRxBytesAt18Mbps=_MonStaRxBytesAt18Mbps_Object((1,3,6,1,4,1,14823,2,2,1,6,6,2,2,1,36),_MonStaRxBytesAt18Mbps_Type())
monStaRxBytesAt18Mbps.setMaxAccess(_B)
if mibBuilder.loadTexts:monStaRxBytesAt18Mbps.setStatus(_A)
_MonStaRxPktsAt24Mbps_Type=Counter32
_MonStaRxPktsAt24Mbps_Object=MibTableColumn
monStaRxPktsAt24Mbps=_MonStaRxPktsAt24Mbps_Object((1,3,6,1,4,1,14823,2,2,1,6,6,2,2,1,37),_MonStaRxPktsAt24Mbps_Type())
monStaRxPktsAt24Mbps.setMaxAccess(_B)
if mibBuilder.loadTexts:monStaRxPktsAt24Mbps.setStatus(_A)
_MonStaRxBytesAt24Mbps_Type=Counter32
_MonStaRxBytesAt24Mbps_Object=MibTableColumn
monStaRxBytesAt24Mbps=_MonStaRxBytesAt24Mbps_Object((1,3,6,1,4,1,14823,2,2,1,6,6,2,2,1,38),_MonStaRxBytesAt24Mbps_Type())
monStaRxBytesAt24Mbps.setMaxAccess(_B)
if mibBuilder.loadTexts:monStaRxBytesAt24Mbps.setStatus(_A)
_MonStaRxPktsAt36Mbps_Type=Counter32
_MonStaRxPktsAt36Mbps_Object=MibTableColumn
monStaRxPktsAt36Mbps=_MonStaRxPktsAt36Mbps_Object((1,3,6,1,4,1,14823,2,2,1,6,6,2,2,1,39),_MonStaRxPktsAt36Mbps_Type())
monStaRxPktsAt36Mbps.setMaxAccess(_B)
if mibBuilder.loadTexts:monStaRxPktsAt36Mbps.setStatus(_A)
_MonStaRxBytesAt36Mbps_Type=Counter32
_MonStaRxBytesAt36Mbps_Object=MibTableColumn
monStaRxBytesAt36Mbps=_MonStaRxBytesAt36Mbps_Object((1,3,6,1,4,1,14823,2,2,1,6,6,2,2,1,40),_MonStaRxBytesAt36Mbps_Type())
monStaRxBytesAt36Mbps.setMaxAccess(_B)
if mibBuilder.loadTexts:monStaRxBytesAt36Mbps.setStatus(_A)
_MonStaRxPktsAt48Mbps_Type=Counter32
_MonStaRxPktsAt48Mbps_Object=MibTableColumn
monStaRxPktsAt48Mbps=_MonStaRxPktsAt48Mbps_Object((1,3,6,1,4,1,14823,2,2,1,6,6,2,2,1,41),_MonStaRxPktsAt48Mbps_Type())
monStaRxPktsAt48Mbps.setMaxAccess(_B)
if mibBuilder.loadTexts:monStaRxPktsAt48Mbps.setStatus(_A)
_MonStaRxBytesAt48Mbps_Type=Counter32
_MonStaRxBytesAt48Mbps_Object=MibTableColumn
monStaRxBytesAt48Mbps=_MonStaRxBytesAt48Mbps_Object((1,3,6,1,4,1,14823,2,2,1,6,6,2,2,1,42),_MonStaRxBytesAt48Mbps_Type())
monStaRxBytesAt48Mbps.setMaxAccess(_B)
if mibBuilder.loadTexts:monStaRxBytesAt48Mbps.setStatus(_A)
_MonStaRxPktsAt54Mbps_Type=Counter32
_MonStaRxPktsAt54Mbps_Object=MibTableColumn
monStaRxPktsAt54Mbps=_MonStaRxPktsAt54Mbps_Object((1,3,6,1,4,1,14823,2,2,1,6,6,2,2,1,43),_MonStaRxPktsAt54Mbps_Type())
monStaRxPktsAt54Mbps.setMaxAccess(_B)
if mibBuilder.loadTexts:monStaRxPktsAt54Mbps.setStatus(_A)
_MonStaRxBytesAt54Mbps_Type=Counter32
_MonStaRxBytesAt54Mbps_Object=MibTableColumn
monStaRxBytesAt54Mbps=_MonStaRxBytesAt54Mbps_Object((1,3,6,1,4,1,14823,2,2,1,6,6,2,2,1,44),_MonStaRxBytesAt54Mbps_Type())
monStaRxBytesAt54Mbps.setMaxAccess(_B)
if mibBuilder.loadTexts:monStaRxBytesAt54Mbps.setStatus(_A)
_MonStaTxPktsAt9Mbps_Type=Counter32
_MonStaTxPktsAt9Mbps_Object=MibTableColumn
monStaTxPktsAt9Mbps=_MonStaTxPktsAt9Mbps_Object((1,3,6,1,4,1,14823,2,2,1,6,6,2,2,1,45),_MonStaTxPktsAt9Mbps_Type())
monStaTxPktsAt9Mbps.setMaxAccess(_B)
if mibBuilder.loadTexts:monStaTxPktsAt9Mbps.setStatus(_A)
_MonStaTxBytesAt9Mbps_Type=Counter32
_MonStaTxBytesAt9Mbps_Object=MibTableColumn
monStaTxBytesAt9Mbps=_MonStaTxBytesAt9Mbps_Object((1,3,6,1,4,1,14823,2,2,1,6,6,2,2,1,46),_MonStaTxBytesAt9Mbps_Type())
monStaTxBytesAt9Mbps.setMaxAccess(_B)
if mibBuilder.loadTexts:monStaTxBytesAt9Mbps.setStatus(_A)
_MonStaRxPktsAt9Mbps_Type=Counter32
_MonStaRxPktsAt9Mbps_Object=MibTableColumn
monStaRxPktsAt9Mbps=_MonStaRxPktsAt9Mbps_Object((1,3,6,1,4,1,14823,2,2,1,6,6,2,2,1,47),_MonStaRxPktsAt9Mbps_Type())
monStaRxPktsAt9Mbps.setMaxAccess(_B)
if mibBuilder.loadTexts:monStaRxPktsAt9Mbps.setStatus(_A)
_MonStaRxBytesAt9Mbps_Type=Counter32
_MonStaRxBytesAt9Mbps_Object=MibTableColumn
monStaRxBytesAt9Mbps=_MonStaRxBytesAt9Mbps_Object((1,3,6,1,4,1,14823,2,2,1,6,6,2,2,1,48),_MonStaRxBytesAt9Mbps_Type())
monStaRxBytesAt9Mbps.setMaxAccess(_B)
if mibBuilder.loadTexts:monStaRxBytesAt9Mbps.setStatus(_A)
_WlsxMonStaDATypeStatsTable_Object=MibTable
wlsxMonStaDATypeStatsTable=_WlsxMonStaDATypeStatsTable_Object((1,3,6,1,4,1,14823,2,2,1,6,6,2,3))
if mibBuilder.loadTexts:wlsxMonStaDATypeStatsTable.setStatus(_A)
_WlsxMonStaDATypeStatsEntry_Object=MibTableRow
wlsxMonStaDATypeStatsEntry=_WlsxMonStaDATypeStatsEntry_Object((1,3,6,1,4,1,14823,2,2,1,6,6,2,3,1))
wlsxMonStaDATypeStatsEntry.setIndexNames((0,_C,_D),(0,_C,_E),(0,_C,_G))
if mibBuilder.loadTexts:wlsxMonStaDATypeStatsEntry.setStatus(_A)
_MonStaTxDABroadcastPkts_Type=Counter32
_MonStaTxDABroadcastPkts_Object=MibTableColumn
monStaTxDABroadcastPkts=_MonStaTxDABroadcastPkts_Object((1,3,6,1,4,1,14823,2,2,1,6,6,2,3,1,1),_MonStaTxDABroadcastPkts_Type())
monStaTxDABroadcastPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:monStaTxDABroadcastPkts.setStatus(_A)
_MonStaTxDABroadcastBytes_Type=Counter32
_MonStaTxDABroadcastBytes_Object=MibTableColumn
monStaTxDABroadcastBytes=_MonStaTxDABroadcastBytes_Object((1,3,6,1,4,1,14823,2,2,1,6,6,2,3,1,2),_MonStaTxDABroadcastBytes_Type())
monStaTxDABroadcastBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:monStaTxDABroadcastBytes.setStatus(_A)
_MonStaTxDAMulticastPkts_Type=Counter32
_MonStaTxDAMulticastPkts_Object=MibTableColumn
monStaTxDAMulticastPkts=_MonStaTxDAMulticastPkts_Object((1,3,6,1,4,1,14823,2,2,1,6,6,2,3,1,3),_MonStaTxDAMulticastPkts_Type())
monStaTxDAMulticastPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:monStaTxDAMulticastPkts.setStatus(_A)
_MonStaTxDAMulticastBytes_Type=Counter32
_MonStaTxDAMulticastBytes_Object=MibTableColumn
monStaTxDAMulticastBytes=_MonStaTxDAMulticastBytes_Object((1,3,6,1,4,1,14823,2,2,1,6,6,2,3,1,4),_MonStaTxDAMulticastBytes_Type())
monStaTxDAMulticastBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:monStaTxDAMulticastBytes.setStatus(_A)
_MonStaTxDAUnicastPkts_Type=Counter32
_MonStaTxDAUnicastPkts_Object=MibTableColumn
monStaTxDAUnicastPkts=_MonStaTxDAUnicastPkts_Object((1,3,6,1,4,1,14823,2,2,1,6,6,2,3,1,5),_MonStaTxDAUnicastPkts_Type())
monStaTxDAUnicastPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:monStaTxDAUnicastPkts.setStatus(_A)
_MonStaTxDAUnicastBytes_Type=Counter32
_MonStaTxDAUnicastBytes_Object=MibTableColumn
monStaTxDAUnicastBytes=_MonStaTxDAUnicastBytes_Object((1,3,6,1,4,1,14823,2,2,1,6,6,2,3,1,6),_MonStaTxDAUnicastBytes_Type())
monStaTxDAUnicastBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:monStaTxDAUnicastBytes.setStatus(_A)
_WlsxMonStaFrameTypeStatsTable_Object=MibTable
wlsxMonStaFrameTypeStatsTable=_WlsxMonStaFrameTypeStatsTable_Object((1,3,6,1,4,1,14823,2,2,1,6,6,2,4))
if mibBuilder.loadTexts:wlsxMonStaFrameTypeStatsTable.setStatus(_A)
_WlsxMonStaFrameTypeStatsEntry_Object=MibTableRow
wlsxMonStaFrameTypeStatsEntry=_WlsxMonStaFrameTypeStatsEntry_Object((1,3,6,1,4,1,14823,2,2,1,6,6,2,4,1))
wlsxMonStaFrameTypeStatsEntry.setIndexNames((0,_C,_D),(0,_C,_E),(0,_C,_G))
if mibBuilder.loadTexts:wlsxMonStaFrameTypeStatsEntry.setStatus(_A)
_MonStaTxMgmtPkts_Type=Counter32
_MonStaTxMgmtPkts_Object=MibTableColumn
monStaTxMgmtPkts=_MonStaTxMgmtPkts_Object((1,3,6,1,4,1,14823,2,2,1,6,6,2,4,1,1),_MonStaTxMgmtPkts_Type())
monStaTxMgmtPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:monStaTxMgmtPkts.setStatus(_A)
_MonStaTxMgmtBytes_Type=Counter32
_MonStaTxMgmtBytes_Object=MibTableColumn
monStaTxMgmtBytes=_MonStaTxMgmtBytes_Object((1,3,6,1,4,1,14823,2,2,1,6,6,2,4,1,2),_MonStaTxMgmtBytes_Type())
monStaTxMgmtBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:monStaTxMgmtBytes.setStatus(_A)
_MonStaTxCtrlPkts_Type=Counter32
_MonStaTxCtrlPkts_Object=MibTableColumn
monStaTxCtrlPkts=_MonStaTxCtrlPkts_Object((1,3,6,1,4,1,14823,2,2,1,6,6,2,4,1,3),_MonStaTxCtrlPkts_Type())
monStaTxCtrlPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:monStaTxCtrlPkts.setStatus(_A)
_MonStaTxCtrlBytes_Type=Counter32
_MonStaTxCtrlBytes_Object=MibTableColumn
monStaTxCtrlBytes=_MonStaTxCtrlBytes_Object((1,3,6,1,4,1,14823,2,2,1,6,6,2,4,1,4),_MonStaTxCtrlBytes_Type())
monStaTxCtrlBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:monStaTxCtrlBytes.setStatus(_A)
_MonStaTxDataPkts_Type=Counter32
_MonStaTxDataPkts_Object=MibTableColumn
monStaTxDataPkts=_MonStaTxDataPkts_Object((1,3,6,1,4,1,14823,2,2,1,6,6,2,4,1,5),_MonStaTxDataPkts_Type())
monStaTxDataPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:monStaTxDataPkts.setStatus(_A)
_MonStaTxDataBytes_Type=Counter32
_MonStaTxDataBytes_Object=MibTableColumn
monStaTxDataBytes=_MonStaTxDataBytes_Object((1,3,6,1,4,1,14823,2,2,1,6,6,2,4,1,6),_MonStaTxDataBytes_Type())
monStaTxDataBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:monStaTxDataBytes.setStatus(_A)
_MonStaRxMgmtPkts_Type=Counter32
_MonStaRxMgmtPkts_Object=MibTableColumn
monStaRxMgmtPkts=_MonStaRxMgmtPkts_Object((1,3,6,1,4,1,14823,2,2,1,6,6,2,4,1,7),_MonStaRxMgmtPkts_Type())
monStaRxMgmtPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:monStaRxMgmtPkts.setStatus(_A)
_MonStaRxMgmtBytes_Type=Counter32
_MonStaRxMgmtBytes_Object=MibTableColumn
monStaRxMgmtBytes=_MonStaRxMgmtBytes_Object((1,3,6,1,4,1,14823,2,2,1,6,6,2,4,1,8),_MonStaRxMgmtBytes_Type())
monStaRxMgmtBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:monStaRxMgmtBytes.setStatus(_A)
_MonStaRxCtrlPkts_Type=Counter32
_MonStaRxCtrlPkts_Object=MibTableColumn
monStaRxCtrlPkts=_MonStaRxCtrlPkts_Object((1,3,6,1,4,1,14823,2,2,1,6,6,2,4,1,9),_MonStaRxCtrlPkts_Type())
monStaRxCtrlPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:monStaRxCtrlPkts.setStatus(_A)
_MonStaRxCtrlBytes_Type=Counter32
_MonStaRxCtrlBytes_Object=MibTableColumn
monStaRxCtrlBytes=_MonStaRxCtrlBytes_Object((1,3,6,1,4,1,14823,2,2,1,6,6,2,4,1,10),_MonStaRxCtrlBytes_Type())
monStaRxCtrlBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:monStaRxCtrlBytes.setStatus(_A)
_MonStaRxDataPkts_Type=Counter32
_MonStaRxDataPkts_Object=MibTableColumn
monStaRxDataPkts=_MonStaRxDataPkts_Object((1,3,6,1,4,1,14823,2,2,1,6,6,2,4,1,11),_MonStaRxDataPkts_Type())
monStaRxDataPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:monStaRxDataPkts.setStatus(_A)
_MonStaRxDataBytes_Type=Counter32
_MonStaRxDataBytes_Object=MibTableColumn
monStaRxDataBytes=_MonStaRxDataBytes_Object((1,3,6,1,4,1,14823,2,2,1,6,6,2,4,1,12),_MonStaRxDataBytes_Type())
monStaRxDataBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:monStaRxDataBytes.setStatus(_A)
_WlsxMonStaPktSizeStatsTable_Object=MibTable
wlsxMonStaPktSizeStatsTable=_WlsxMonStaPktSizeStatsTable_Object((1,3,6,1,4,1,14823,2,2,1,6,6,2,5))
if mibBuilder.loadTexts:wlsxMonStaPktSizeStatsTable.setStatus(_A)
_WlsxMonStaPktSizeStatsEntry_Object=MibTableRow
wlsxMonStaPktSizeStatsEntry=_WlsxMonStaPktSizeStatsEntry_Object((1,3,6,1,4,1,14823,2,2,1,6,6,2,5,1))
wlsxMonStaPktSizeStatsEntry.setIndexNames((0,_C,_D),(0,_C,_E),(0,_C,_G))
if mibBuilder.loadTexts:wlsxMonStaPktSizeStatsEntry.setStatus(_A)
_MonStaTxPkts63Bytes_Type=Counter32
_MonStaTxPkts63Bytes_Object=MibTableColumn
monStaTxPkts63Bytes=_MonStaTxPkts63Bytes_Object((1,3,6,1,4,1,14823,2,2,1,6,6,2,5,1,1),_MonStaTxPkts63Bytes_Type())
monStaTxPkts63Bytes.setMaxAccess(_B)
if mibBuilder.loadTexts:monStaTxPkts63Bytes.setStatus(_A)
_MonStaTxPkts64To127_Type=Counter32
_MonStaTxPkts64To127_Object=MibTableColumn
monStaTxPkts64To127=_MonStaTxPkts64To127_Object((1,3,6,1,4,1,14823,2,2,1,6,6,2,5,1,2),_MonStaTxPkts64To127_Type())
monStaTxPkts64To127.setMaxAccess(_B)
if mibBuilder.loadTexts:monStaTxPkts64To127.setStatus(_A)
_MonStaTxPkts128To255_Type=Counter32
_MonStaTxPkts128To255_Object=MibTableColumn
monStaTxPkts128To255=_MonStaTxPkts128To255_Object((1,3,6,1,4,1,14823,2,2,1,6,6,2,5,1,3),_MonStaTxPkts128To255_Type())
monStaTxPkts128To255.setMaxAccess(_B)
if mibBuilder.loadTexts:monStaTxPkts128To255.setStatus(_A)
_MonStaTxPkts256To511_Type=Counter32
_MonStaTxPkts256To511_Object=MibTableColumn
monStaTxPkts256To511=_MonStaTxPkts256To511_Object((1,3,6,1,4,1,14823,2,2,1,6,6,2,5,1,4),_MonStaTxPkts256To511_Type())
monStaTxPkts256To511.setMaxAccess(_B)
if mibBuilder.loadTexts:monStaTxPkts256To511.setStatus(_A)
_MonStaTxPkts512To1023_Type=Counter32
_MonStaTxPkts512To1023_Object=MibTableColumn
monStaTxPkts512To1023=_MonStaTxPkts512To1023_Object((1,3,6,1,4,1,14823,2,2,1,6,6,2,5,1,5),_MonStaTxPkts512To1023_Type())
monStaTxPkts512To1023.setMaxAccess(_B)
if mibBuilder.loadTexts:monStaTxPkts512To1023.setStatus(_A)
_MonStaTxPkts1024To1518_Type=Counter32
_MonStaTxPkts1024To1518_Object=MibTableColumn
monStaTxPkts1024To1518=_MonStaTxPkts1024To1518_Object((1,3,6,1,4,1,14823,2,2,1,6,6,2,5,1,6),_MonStaTxPkts1024To1518_Type())
monStaTxPkts1024To1518.setMaxAccess(_B)
if mibBuilder.loadTexts:monStaTxPkts1024To1518.setStatus(_A)
_MonStaRxPkts63Bytes_Type=Counter32
_MonStaRxPkts63Bytes_Object=MibTableColumn
monStaRxPkts63Bytes=_MonStaRxPkts63Bytes_Object((1,3,6,1,4,1,14823,2,2,1,6,6,2,5,1,7),_MonStaRxPkts63Bytes_Type())
monStaRxPkts63Bytes.setMaxAccess(_B)
if mibBuilder.loadTexts:monStaRxPkts63Bytes.setStatus(_A)
_MonStaRxPkts64To127_Type=Counter32
_MonStaRxPkts64To127_Object=MibTableColumn
monStaRxPkts64To127=_MonStaRxPkts64To127_Object((1,3,6,1,4,1,14823,2,2,1,6,6,2,5,1,8),_MonStaRxPkts64To127_Type())
monStaRxPkts64To127.setMaxAccess(_B)
if mibBuilder.loadTexts:monStaRxPkts64To127.setStatus(_A)
_MonStaRxPkts128To255_Type=Counter32
_MonStaRxPkts128To255_Object=MibTableColumn
monStaRxPkts128To255=_MonStaRxPkts128To255_Object((1,3,6,1,4,1,14823,2,2,1,6,6,2,5,1,9),_MonStaRxPkts128To255_Type())
monStaRxPkts128To255.setMaxAccess(_B)
if mibBuilder.loadTexts:monStaRxPkts128To255.setStatus(_A)
_MonStaRxPkts256To511_Type=Counter32
_MonStaRxPkts256To511_Object=MibTableColumn
monStaRxPkts256To511=_MonStaRxPkts256To511_Object((1,3,6,1,4,1,14823,2,2,1,6,6,2,5,1,10),_MonStaRxPkts256To511_Type())
monStaRxPkts256To511.setMaxAccess(_B)
if mibBuilder.loadTexts:monStaRxPkts256To511.setStatus(_A)
_MonStaRxPkts512To1023_Type=Counter32
_MonStaRxPkts512To1023_Object=MibTableColumn
monStaRxPkts512To1023=_MonStaRxPkts512To1023_Object((1,3,6,1,4,1,14823,2,2,1,6,6,2,5,1,11),_MonStaRxPkts512To1023_Type())
monStaRxPkts512To1023.setMaxAccess(_B)
if mibBuilder.loadTexts:monStaRxPkts512To1023.setStatus(_A)
_MonStaRxPkts1024To1518_Type=Counter32
_MonStaRxPkts1024To1518_Object=MibTableColumn
monStaRxPkts1024To1518=_MonStaRxPkts1024To1518_Object((1,3,6,1,4,1,14823,2,2,1,6,6,2,5,1,12),_MonStaRxPkts1024To1518_Type())
monStaRxPkts1024To1518.setMaxAccess(_B)
if mibBuilder.loadTexts:monStaRxPkts1024To1518.setStatus(_A)
_WlsxMonEventCountTable_Object=MibTable
wlsxMonEventCountTable=_WlsxMonEventCountTable_Object((1,3,6,1,4,1,14823,2,2,1,6,6,2,6))
if mibBuilder.loadTexts:wlsxMonEventCountTable.setStatus(_A)
_WlsxMonEventCountEntry_Object=MibTableRow
wlsxMonEventCountEntry=_WlsxMonEventCountEntry_Object((1,3,6,1,4,1,14823,2,2,1,6,6,2,6,1))
wlsxMonEventCountEntry.setIndexNames((0,_C,_L))
if mibBuilder.loadTexts:wlsxMonEventCountEntry.setStatus(_A)
_MonEventID_Type=Unsigned32
_MonEventID_Object=MibTableColumn
monEventID=_MonEventID_Object((1,3,6,1,4,1,14823,2,2,1,6,6,2,6,1,1),_MonEventID_Type())
monEventID.setMaxAccess(_B)
if mibBuilder.loadTexts:monEventID.setStatus(_A)
_MonEventCount_Type=Unsigned32
_MonEventCount_Object=MibTableColumn
monEventCount=_MonEventCount_Object((1,3,6,1,4,1,14823,2,2,1,6,6,2,6,1,2),_MonEventCount_Type())
monEventCount.setMaxAccess(_B)
if mibBuilder.loadTexts:monEventCount.setStatus(_A)
_WlsxMonStationHTRateStatsTable_Object=MibTable
wlsxMonStationHTRateStatsTable=_WlsxMonStationHTRateStatsTable_Object((1,3,6,1,4,1,14823,2,2,1,6,6,2,7))
if mibBuilder.loadTexts:wlsxMonStationHTRateStatsTable.setStatus(_A)
_WlsxMonStationHTRateStatsEntry_Object=MibTableRow
wlsxMonStationHTRateStatsEntry=_WlsxMonStationHTRateStatsEntry_Object((1,3,6,1,4,1,14823,2,2,1,6,6,2,7,1))
wlsxMonStationHTRateStatsEntry.setIndexNames((0,_C,_D),(0,_C,_E),(0,_C,_G),(0,_C,_J))
if mibBuilder.loadTexts:wlsxMonStationHTRateStatsEntry.setStatus(_A)
_MonStaTxHTPkts_Type=Counter32
_MonStaTxHTPkts_Object=MibTableColumn
monStaTxHTPkts=_MonStaTxHTPkts_Object((1,3,6,1,4,1,14823,2,2,1,6,6,2,7,1,1),_MonStaTxHTPkts_Type())
monStaTxHTPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:monStaTxHTPkts.setStatus(_A)
_MonStaTxHTBytes_Type=Counter32
_MonStaTxHTBytes_Object=MibTableColumn
monStaTxHTBytes=_MonStaTxHTBytes_Object((1,3,6,1,4,1,14823,2,2,1,6,6,2,7,1,2),_MonStaTxHTBytes_Type())
monStaTxHTBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:monStaTxHTBytes.setStatus(_A)
_MonStaRxHTPkts_Type=Counter32
_MonStaRxHTPkts_Object=MibTableColumn
monStaRxHTPkts=_MonStaRxHTPkts_Object((1,3,6,1,4,1,14823,2,2,1,6,6,2,7,1,3),_MonStaRxHTPkts_Type())
monStaRxHTPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:monStaRxHTPkts.setStatus(_A)
_MonStaRxHTBytes_Type=Counter32
_MonStaRxHTBytes_Object=MibTableColumn
monStaRxHTBytes=_MonStaRxHTBytes_Object((1,3,6,1,4,1,14823,2,2,1,6,6,2,7,1,4),_MonStaRxHTBytes_Type())
monStaRxHTBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:monStaRxHTBytes.setStatus(_A)
_WlsxMonInfoGroup_ObjectIdentity=ObjectIdentity
wlsxMonInfoGroup=_WlsxMonInfoGroup_ObjectIdentity((1,3,6,1,4,1,14823,2,2,1,6,7))
_WlsxMonAccessPointInfoGroup_ObjectIdentity=ObjectIdentity
wlsxMonAccessPointInfoGroup=_WlsxMonAccessPointInfoGroup_ObjectIdentity((1,3,6,1,4,1,14823,2,2,1,6,7,1))
_WlsxMonAPInfoTable_Object=MibTable
wlsxMonAPInfoTable=_WlsxMonAPInfoTable_Object((1,3,6,1,4,1,14823,2,2,1,6,7,1,1))
if mibBuilder.loadTexts:wlsxMonAPInfoTable.setStatus(_A)
_WlsxMonAPInfoEntry_Object=MibTableRow
wlsxMonAPInfoEntry=_WlsxMonAPInfoEntry_Object((1,3,6,1,4,1,14823,2,2,1,6,7,1,1,1))
wlsxMonAPInfoEntry.setIndexNames((0,_C,_D),(0,_C,_E),(0,_C,_F))
if mibBuilder.loadTexts:wlsxMonAPInfoEntry.setStatus(_A)
_MonAPInfoPhyType_Type=ArubaPhyType
_MonAPInfoPhyType_Object=MibTableColumn
monAPInfoPhyType=_MonAPInfoPhyType_Object((1,3,6,1,4,1,14823,2,2,1,6,7,1,1,1,1),_MonAPInfoPhyType_Type())
monAPInfoPhyType.setMaxAccess(_B)
if mibBuilder.loadTexts:monAPInfoPhyType.setStatus(_A)
_MonAPInfoCurrentChannel_Type=Unsigned32
_MonAPInfoCurrentChannel_Object=MibTableColumn
monAPInfoCurrentChannel=_MonAPInfoCurrentChannel_Object((1,3,6,1,4,1,14823,2,2,1,6,7,1,1,1,2),_MonAPInfoCurrentChannel_Type())
monAPInfoCurrentChannel.setMaxAccess(_B)
if mibBuilder.loadTexts:monAPInfoCurrentChannel.setStatus(_A)
_MonAPInfoClassification_Type=ArubaRogueApType
_MonAPInfoClassification_Object=MibTableColumn
monAPInfoClassification=_MonAPInfoClassification_Object((1,3,6,1,4,1,14823,2,2,1,6,7,1,1,1,3),_MonAPInfoClassification_Type())
monAPInfoClassification.setMaxAccess(_B)
if mibBuilder.loadTexts:monAPInfoClassification.setStatus(_A)
_MonAPInfoESSID_Type=DisplayString
_MonAPInfoESSID_Object=MibTableColumn
monAPInfoESSID=_MonAPInfoESSID_Object((1,3,6,1,4,1,14823,2,2,1,6,7,1,1,1,4),_MonAPInfoESSID_Type())
monAPInfoESSID.setMaxAccess(_B)
if mibBuilder.loadTexts:monAPInfoESSID.setStatus(_A)
_MonAPInfoRSSI_Type=Integer32
_MonAPInfoRSSI_Object=MibTableColumn
monAPInfoRSSI=_MonAPInfoRSSI_Object((1,3,6,1,4,1,14823,2,2,1,6,7,1,1,1,5),_MonAPInfoRSSI_Type())
monAPInfoRSSI.setMaxAccess(_B)
if mibBuilder.loadTexts:monAPInfoRSSI.setStatus(_A)
_MonAPInfoMonitorTime_Type=TimeTicks
_MonAPInfoMonitorTime_Object=MibTableColumn
monAPInfoMonitorTime=_MonAPInfoMonitorTime_Object((1,3,6,1,4,1,14823,2,2,1,6,7,1,1,1,6),_MonAPInfoMonitorTime_Type())
monAPInfoMonitorTime.setMaxAccess(_B)
if mibBuilder.loadTexts:monAPInfoMonitorTime.setStatus(_A)
_MonAPInfoInactivityTime_Type=TimeTicks
_MonAPInfoInactivityTime_Object=MibTableColumn
monAPInfoInactivityTime=_MonAPInfoInactivityTime_Object((1,3,6,1,4,1,14823,2,2,1,6,7,1,1,1,7),_MonAPInfoInactivityTime_Type())
monAPInfoInactivityTime.setMaxAccess(_B)
if mibBuilder.loadTexts:monAPInfoInactivityTime.setStatus(_A)
_MonAPInfoSnrSignalPkts_Type=Integer32
_MonAPInfoSnrSignalPkts_Object=MibTableColumn
monAPInfoSnrSignalPkts=_MonAPInfoSnrSignalPkts_Object((1,3,6,1,4,1,14823,2,2,1,6,7,1,1,1,8),_MonAPInfoSnrSignalPkts_Type())
monAPInfoSnrSignalPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:monAPInfoSnrSignalPkts.setStatus(_A)
_MonAPInfoSnrSampleTime_Type=Integer32
_MonAPInfoSnrSampleTime_Object=MibTableColumn
monAPInfoSnrSampleTime=_MonAPInfoSnrSampleTime_Object((1,3,6,1,4,1,14823,2,2,1,6,7,1,1,1,9),_MonAPInfoSnrSampleTime_Type())
monAPInfoSnrSampleTime.setMaxAccess(_B)
if mibBuilder.loadTexts:monAPInfoSnrSampleTime.setStatus(_A)
class _MonAPInfoStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('up',1),('down',2)))
_MonAPInfoStatus_Type.__name__=_I
_MonAPInfoStatus_Object=MibTableColumn
monAPInfoStatus=_MonAPInfoStatus_Object((1,3,6,1,4,1,14823,2,2,1,6,7,1,1,1,10),_MonAPInfoStatus_Type())
monAPInfoStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:monAPInfoStatus.setStatus(_A)
_MonAPInfoConfidence_Type=Integer32
_MonAPInfoConfidence_Object=MibTableColumn
monAPInfoConfidence=_MonAPInfoConfidence_Object((1,3,6,1,4,1,14823,2,2,1,6,7,1,1,1,11),_MonAPInfoConfidence_Type())
monAPInfoConfidence.setMaxAccess(_B)
if mibBuilder.loadTexts:monAPInfoConfidence.setStatus(_A)
_MonAPInfoMatchType_Type=ArubaAPMatchType
_MonAPInfoMatchType_Object=MibTableColumn
monAPInfoMatchType=_MonAPInfoMatchType_Object((1,3,6,1,4,1,14823,2,2,1,6,7,1,1,1,12),_MonAPInfoMatchType_Type())
monAPInfoMatchType.setMaxAccess(_B)
if mibBuilder.loadTexts:monAPInfoMatchType.setStatus(_A)
_MonAPInfoMatchMethod_Type=ArubaAPMatchMethod
_MonAPInfoMatchMethod_Object=MibTableColumn
monAPInfoMatchMethod=_MonAPInfoMatchMethod_Object((1,3,6,1,4,1,14823,2,2,1,6,7,1,1,1,13),_MonAPInfoMatchMethod_Type())
monAPInfoMatchMethod.setMaxAccess(_B)
if mibBuilder.loadTexts:monAPInfoMatchMethod.setStatus(_A)
_MonAPInfoHTMode_Type=ArubaHTMode
_MonAPInfoHTMode_Object=MibTableColumn
monAPInfoHTMode=_MonAPInfoHTMode_Object((1,3,6,1,4,1,14823,2,2,1,6,7,1,1,1,14),_MonAPInfoHTMode_Type())
monAPInfoHTMode.setMaxAccess(_B)
if mibBuilder.loadTexts:monAPInfoHTMode.setStatus(_A)
_MonAPInfoEncryptionType_Type=ArubaMonEncryptionType
_MonAPInfoEncryptionType_Object=MibTableColumn
monAPInfoEncryptionType=_MonAPInfoEncryptionType_Object((1,3,6,1,4,1,14823,2,2,1,6,7,1,1,1,15),_MonAPInfoEncryptionType_Type())
monAPInfoEncryptionType.setMaxAccess(_B)
if mibBuilder.loadTexts:monAPInfoEncryptionType.setStatus(_A)
_MonAPInfoWPAUnicastCipher_Type=ArubaMonEncryptionCipher
_MonAPInfoWPAUnicastCipher_Object=MibTableColumn
monAPInfoWPAUnicastCipher=_MonAPInfoWPAUnicastCipher_Object((1,3,6,1,4,1,14823,2,2,1,6,7,1,1,1,16),_MonAPInfoWPAUnicastCipher_Type())
monAPInfoWPAUnicastCipher.setMaxAccess(_B)
if mibBuilder.loadTexts:monAPInfoWPAUnicastCipher.setStatus(_A)
_MonAPInfoWPAAuthAlgorithm_Type=ArubaMonAuthAlgorithm
_MonAPInfoWPAAuthAlgorithm_Object=MibTableColumn
monAPInfoWPAAuthAlgorithm=_MonAPInfoWPAAuthAlgorithm_Object((1,3,6,1,4,1,14823,2,2,1,6,7,1,1,1,17),_MonAPInfoWPAAuthAlgorithm_Type())
monAPInfoWPAAuthAlgorithm.setMaxAccess(_B)
if mibBuilder.loadTexts:monAPInfoWPAAuthAlgorithm.setStatus(_A)
_MonAPInfoIBSS_Type=TruthValue
_MonAPInfoIBSS_Object=MibTableColumn
monAPInfoIBSS=_MonAPInfoIBSS_Object((1,3,6,1,4,1,14823,2,2,1,6,7,1,1,1,18),_MonAPInfoIBSS_Type())
monAPInfoIBSS.setMaxAccess(_B)
if mibBuilder.loadTexts:monAPInfoIBSS.setStatus(_A)
_WlsxMonStationInfoGroup_ObjectIdentity=ObjectIdentity
wlsxMonStationInfoGroup=_WlsxMonStationInfoGroup_ObjectIdentity((1,3,6,1,4,1,14823,2,2,1,6,7,2))
_WlsxMonStationInfoTable_Object=MibTable
wlsxMonStationInfoTable=_WlsxMonStationInfoTable_Object((1,3,6,1,4,1,14823,2,2,1,6,7,2,1))
if mibBuilder.loadTexts:wlsxMonStationInfoTable.setStatus(_A)
_WlsxMonStationInfoEntry_Object=MibTableRow
wlsxMonStationInfoEntry=_WlsxMonStationInfoEntry_Object((1,3,6,1,4,1,14823,2,2,1,6,7,2,1,1))
wlsxMonStationInfoEntry.setIndexNames((0,_C,_D),(0,_C,_E),(0,_C,_G))
if mibBuilder.loadTexts:wlsxMonStationInfoEntry.setStatus(_A)
_MonStaInfoChannelNum_Type=Unsigned32
_MonStaInfoChannelNum_Object=MibTableColumn
monStaInfoChannelNum=_MonStaInfoChannelNum_Object((1,3,6,1,4,1,14823,2,2,1,6,7,2,1,1,1),_MonStaInfoChannelNum_Type())
monStaInfoChannelNum.setMaxAccess(_B)
if mibBuilder.loadTexts:monStaInfoChannelNum.setStatus(_A)
_MonStaInfoBSSID_Type=MacAddress
_MonStaInfoBSSID_Object=MibTableColumn
monStaInfoBSSID=_MonStaInfoBSSID_Object((1,3,6,1,4,1,14823,2,2,1,6,7,2,1,1,2),_MonStaInfoBSSID_Type())
monStaInfoBSSID.setMaxAccess(_B)
if mibBuilder.loadTexts:monStaInfoBSSID.setStatus(_A)
_MonStaInfoESSID_Type=DisplayString
_MonStaInfoESSID_Object=MibTableColumn
monStaInfoESSID=_MonStaInfoESSID_Object((1,3,6,1,4,1,14823,2,2,1,6,7,2,1,1,3),_MonStaInfoESSID_Type())
monStaInfoESSID.setMaxAccess(_B)
if mibBuilder.loadTexts:monStaInfoESSID.setStatus(_A)
_MonStaInfoPhyType_Type=ArubaPhyType
_MonStaInfoPhyType_Object=MibTableColumn
monStaInfoPhyType=_MonStaInfoPhyType_Object((1,3,6,1,4,1,14823,2,2,1,6,7,2,1,1,4),_MonStaInfoPhyType_Type())
monStaInfoPhyType.setMaxAccess(_B)
if mibBuilder.loadTexts:monStaInfoPhyType.setStatus(_A)
_MonStaInfoRSSI_Type=Integer32
_MonStaInfoRSSI_Object=MibTableColumn
monStaInfoRSSI=_MonStaInfoRSSI_Object((1,3,6,1,4,1,14823,2,2,1,6,7,2,1,1,5),_MonStaInfoRSSI_Type())
monStaInfoRSSI.setMaxAccess(_B)
if mibBuilder.loadTexts:monStaInfoRSSI.setStatus(_A)
_MonStaInfoClassification_Type=ArubaStationType
_MonStaInfoClassification_Object=MibTableColumn
monStaInfoClassification=_MonStaInfoClassification_Object((1,3,6,1,4,1,14823,2,2,1,6,7,2,1,1,6),_MonStaInfoClassification_Type())
monStaInfoClassification.setMaxAccess(_B)
if mibBuilder.loadTexts:monStaInfoClassification.setStatus(_A)
_MonStaInfoMonitorTime_Type=TimeTicks
_MonStaInfoMonitorTime_Object=MibTableColumn
monStaInfoMonitorTime=_MonStaInfoMonitorTime_Object((1,3,6,1,4,1,14823,2,2,1,6,7,2,1,1,7),_MonStaInfoMonitorTime_Type())
monStaInfoMonitorTime.setMaxAccess(_B)
if mibBuilder.loadTexts:monStaInfoMonitorTime.setStatus(_A)
_MonStaInfoInactivityTime_Type=TimeTicks
_MonStaInfoInactivityTime_Object=MibTableColumn
monStaInfoInactivityTime=_MonStaInfoInactivityTime_Object((1,3,6,1,4,1,14823,2,2,1,6,7,2,1,1,8),_MonStaInfoInactivityTime_Type())
monStaInfoInactivityTime.setMaxAccess(_B)
if mibBuilder.loadTexts:monStaInfoInactivityTime.setStatus(_A)
_MonStaInfoSnrSignalPkts_Type=Integer32
_MonStaInfoSnrSignalPkts_Object=MibTableColumn
monStaInfoSnrSignalPkts=_MonStaInfoSnrSignalPkts_Object((1,3,6,1,4,1,14823,2,2,1,6,7,2,1,1,9),_MonStaInfoSnrSignalPkts_Type())
monStaInfoSnrSignalPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:monStaInfoSnrSignalPkts.setStatus(_A)
_MonStaInfoSnrSampleTime_Type=Integer32
_MonStaInfoSnrSampleTime_Object=MibTableColumn
monStaInfoSnrSampleTime=_MonStaInfoSnrSampleTime_Object((1,3,6,1,4,1,14823,2,2,1,6,7,2,1,1,10),_MonStaInfoSnrSampleTime_Type())
monStaInfoSnrSampleTime.setMaxAccess(_B)
if mibBuilder.loadTexts:monStaInfoSnrSampleTime.setStatus(_A)
class _MonStaInfoStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('up',1),('down',2)))
_MonStaInfoStatus_Type.__name__=_I
_MonStaInfoStatus_Object=MibTableColumn
monStaInfoStatus=_MonStaInfoStatus_Object((1,3,6,1,4,1,14823,2,2,1,6,7,2,1,1,11),_MonStaInfoStatus_Type())
monStaInfoStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:monStaInfoStatus.setStatus(_A)
_MonStaInfoHTMode_Type=ArubaHTMode
_MonStaInfoHTMode_Object=MibTableColumn
monStaInfoHTMode=_MonStaInfoHTMode_Object((1,3,6,1,4,1,14823,2,2,1,6,7,2,1,1,12),_MonStaInfoHTMode_Type())
monStaInfoHTMode.setMaxAccess(_B)
if mibBuilder.loadTexts:monStaInfoHTMode.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'wlsxMonMIB':wlsxMonMIB,'wlsxMonStatsGroup':wlsxMonStatsGroup,'wlsxMonAccessPointStatsGroup':wlsxMonAccessPointStatsGroup,'wlsxMonAPStatsTable':wlsxMonAPStatsTable,'wlsxMonAPStatsEntry':wlsxMonAPStatsEntry,_D:monPhyAddress,_E:monRadioNumber,_F:monitoredApBSSID,'monPhyType':monPhyType,'monAPCurrentChannel':monAPCurrentChannel,'monAPNumClients':monAPNumClients,'monAPTxPkts':monAPTxPkts,'monAPTxBytes':monAPTxBytes,'monAPRxPkts':monAPRxPkts,'monAPRxBytes':monAPRxBytes,'monAPTxDeauthentications':monAPTxDeauthentications,'monAPRxDeauthentications':monAPRxDeauthentications,'monAPChannelThroughput':monAPChannelThroughput,'monAPFrameRetryRate':monAPFrameRetryRate,'monAPFrameLowSpeedRate':monAPFrameLowSpeedRate,'monAPFrameNonUnicastRate':monAPFrameNonUnicastRate,'monAPFrameFragmentationRate':monAPFrameFragmentationRate,'monAPFrameBandwidthRate':monAPFrameBandwidthRate,'monAPFrameRetryErrorRate':monAPFrameRetryErrorRate,'monAPChannelErrorRate':monAPChannelErrorRate,'monAPESSID':monAPESSID,'monAPRSSI':monAPRSSI,'monAPFrameReceiveErrorRate':monAPFrameReceiveErrorRate,'wlsxMonAPRateStatsTable':wlsxMonAPRateStatsTable,'wlsxMonAPRateStatsEntry':wlsxMonAPRateStatsEntry,'monAPStatsTotPktsAt1Mbps':monAPStatsTotPktsAt1Mbps,'monAPStatsTotBytesAt1Mbps':monAPStatsTotBytesAt1Mbps,'monAPStatsTotPktsAt2Mbps':monAPStatsTotPktsAt2Mbps,'monAPStatsTotBytesAt2Mbps':monAPStatsTotBytesAt2Mbps,'monAPStatsTotPktsAt5Mbps':monAPStatsTotPktsAt5Mbps,'monAPStatsTotBytesAt5Mbps':monAPStatsTotBytesAt5Mbps,'monAPStatsTotPktsAt11Mbps':monAPStatsTotPktsAt11Mbps,'monAPStatsTotBytesAt11Mbps':monAPStatsTotBytesAt11Mbps,'monAPStatsTotPktsAt6Mbps':monAPStatsTotPktsAt6Mbps,'monAPStatsTotBytesAt6Mbps':monAPStatsTotBytesAt6Mbps,'monAPStatsTotPktsAt12Mbps':monAPStatsTotPktsAt12Mbps,'monAPStatsTotBytesAt12Mbps':monAPStatsTotBytesAt12Mbps,'monAPStatsTotPktsAt18Mbps':monAPStatsTotPktsAt18Mbps,'monAPStatsTotBytesAt18Mbps':monAPStatsTotBytesAt18Mbps,'monAPStatsTotPktsAt24Mbps':monAPStatsTotPktsAt24Mbps,'monAPStatsTotBytesAt24Mbps':monAPStatsTotBytesAt24Mbps,'monAPStatsTotPktsAt36Mbps':monAPStatsTotPktsAt36Mbps,'monAPStatsTotBytesAt36Mbps':monAPStatsTotBytesAt36Mbps,'monAPStatsTotPktsAt48Mbps':monAPStatsTotPktsAt48Mbps,'monAPStatsTotBytesAt48Mbps':monAPStatsTotBytesAt48Mbps,'monAPStatsTotPktsAt54Mbps':monAPStatsTotPktsAt54Mbps,'monAPStatsTotBytesAt54Mbps':monAPStatsTotBytesAt54Mbps,'monAPStatsTotPktsAt9Mbps':monAPStatsTotPktsAt9Mbps,'monAPStatsTotBytesAt9Mbps':monAPStatsTotBytesAt9Mbps,'wlsxMonAPDATypeStatsTable':wlsxMonAPDATypeStatsTable,'wlsxMonAPDATypeStatsEntry':wlsxMonAPDATypeStatsEntry,'monAPStatsTotDABroadcastPkts':monAPStatsTotDABroadcastPkts,'monAPStatsTotDABroadcastBytes':monAPStatsTotDABroadcastBytes,'monAPStatsTotDAMulticastPkts':monAPStatsTotDAMulticastPkts,'monAPStatsTotDAMulticastBytes':monAPStatsTotDAMulticastBytes,'monAPStatsTotDAUnicastPkts':monAPStatsTotDAUnicastPkts,'monAPStatsTotDAUnicastBytes':monAPStatsTotDAUnicastBytes,'wlsxMonAPFrameTypeStatsTable':wlsxMonAPFrameTypeStatsTable,'wlsxMonAPFrameTypeStatsEntry':wlsxMonAPFrameTypeStatsEntry,'monAPStatsTotMgmtPkts':monAPStatsTotMgmtPkts,'monAPStatsTotMgmtBytes':monAPStatsTotMgmtBytes,'monAPStatsTotCtrlPkts':monAPStatsTotCtrlPkts,'monAPStatsTotCtrlBytes':monAPStatsTotCtrlBytes,'monAPStatsTotDataPkts':monAPStatsTotDataPkts,'monAPStatsTotDataBytes':monAPStatsTotDataBytes,'wlsxMonAPPktSizeStatsTable':wlsxMonAPPktSizeStatsTable,'wlsxMonAPPktSizeStatsEntry':wlsxMonAPPktSizeStatsEntry,'monAPStatsPkts63Bytes':monAPStatsPkts63Bytes,'monAPStatsPkts64To127':monAPStatsPkts64To127,'monAPStatsPkts128To255':monAPStatsPkts128To255,'monAPStatsPkts256To511':monAPStatsPkts256To511,'monAPStatsPkts512To1023':monAPStatsPkts512To1023,'monAPStatsPkts1024To1518':monAPStatsPkts1024To1518,'wlsxMonAPHTRateStatsTable':wlsxMonAPHTRateStatsTable,'wlsxMonAPHTRateStatsEntry':wlsxMonAPHTRateStatsEntry,_J:monHTRate,'monAPStatsTotHTPkts':monAPStatsTotHTPkts,'monAPStatsTotHTBytes':monAPStatsTotHTBytes,'wlsxMonStationStatsGroup':wlsxMonStationStatsGroup,'wlsxMonStationStatsTable':wlsxMonStationStatsTable,'wlsxMonStationStatsEntry':wlsxMonStationStatsEntry,_G:monitoredStaPhyAddress,'monStaChannelNum':monStaChannelNum,'monStaTxPkts':monStaTxPkts,'monStaTxBytes':monStaTxBytes,'monStaRxPkts':monStaRxPkts,'monStaRxBytes':monStaRxBytes,'monStaTxBCastPkts':monStaTxBCastPkts,'monStaTxBCastBytes':monStaTxBCastBytes,'monStaTxMCastPkts':monStaTxMCastPkts,'monStaTxMCastBytes':monStaTxMCastBytes,'monStaDataPkts':monStaDataPkts,'monStaCtrlPkts':monStaCtrlPkts,'monStaNumAssocRequests':monStaNumAssocRequests,'monStaNumAuthRequests':monStaNumAuthRequests,'monStaTxDeauthentications':monStaTxDeauthentications,'monStaRxDeauthentications':monStaRxDeauthentications,'monStaFrameRetryRate':monStaFrameRetryRate,'monStaFrameLowSpeedRate':monStaFrameLowSpeedRate,'monStaFrameNonUnicastRate':monStaFrameNonUnicastRate,'monStaFrameFragmentationRate':monStaFrameFragmentationRate,'monStaFrameBandwidthRate':monStaFrameBandwidthRate,'monStaFrameRetryErrorRate':monStaFrameRetryErrorRate,'monStaBSSID':monStaBSSID,'monStaESSID':monStaESSID,'monStaPhyType':monStaPhyType,'monStaRSSI':monStaRSSI,'monStaFrameReceiveErrorRate':monStaFrameReceiveErrorRate,'wlsxMonStaRateStatsTable':wlsxMonStaRateStatsTable,'wlsxMonStaRateStatsEntry':wlsxMonStaRateStatsEntry,'monStaTxPktsAt1Mbps':monStaTxPktsAt1Mbps,'monStaTxBytesAt1Mbps':monStaTxBytesAt1Mbps,'monStaTxPktsAt2Mbps':monStaTxPktsAt2Mbps,'monStaTxBytesAt2Mbps':monStaTxBytesAt2Mbps,'monStaTxPktsAt5Mbps':monStaTxPktsAt5Mbps,'monStaTxBytesAt5Mbps':monStaTxBytesAt5Mbps,'monStaTxPktsAt11Mbps':monStaTxPktsAt11Mbps,'monStaTxBytesAt11Mbps':monStaTxBytesAt11Mbps,'monStaTxPktsAt6Mbps':monStaTxPktsAt6Mbps,'monStaTxBytesAt6Mbps':monStaTxBytesAt6Mbps,'monStaTxPktsAt12Mbps':monStaTxPktsAt12Mbps,'monStaTxBytesAt12Mbps':monStaTxBytesAt12Mbps,'monStaTxPktsAt18Mbps':monStaTxPktsAt18Mbps,'monStaTxBytesAt18Mbps':monStaTxBytesAt18Mbps,'monStaTxPktsAt24Mbps':monStaTxPktsAt24Mbps,'monStaTxBytesAt24Mbps':monStaTxBytesAt24Mbps,'monStaTxPktsAt36Mbps':monStaTxPktsAt36Mbps,'monStaTxBytesAt36Mbps':monStaTxBytesAt36Mbps,'monStaTxPktsAt48Mbps':monStaTxPktsAt48Mbps,'monStaTxBytesAt48Mbps':monStaTxBytesAt48Mbps,'monStaTxPktsAt54Mbps':monStaTxPktsAt54Mbps,'monStaTxBytesAt54Mbps':monStaTxBytesAt54Mbps,'monStaRxPktsAt1Mbps':monStaRxPktsAt1Mbps,'monStaRxBytesAt1Mbps':monStaRxBytesAt1Mbps,'monStaRxPktsAt2Mbps':monStaRxPktsAt2Mbps,'monStaRxBytesAt2Mbps':monStaRxBytesAt2Mbps,'monStaRxPktsAt5Mbps':monStaRxPktsAt5Mbps,'monStaRxBytesAt5Mbps':monStaRxBytesAt5Mbps,'monStaRxPktsAt11Mbps':monStaRxPktsAt11Mbps,'monStaRxBytesAt11Mbps':monStaRxBytesAt11Mbps,'monStaRxPktsAt6Mbps':monStaRxPktsAt6Mbps,'monStaRxBytesAt6Mbps':monStaRxBytesAt6Mbps,'monStaRxPktsAt12Mbps':monStaRxPktsAt12Mbps,'monStaRxBytesAt12Mbps':monStaRxBytesAt12Mbps,'monStaRxPktsAt18Mbps':monStaRxPktsAt18Mbps,'monStaRxBytesAt18Mbps':monStaRxBytesAt18Mbps,'monStaRxPktsAt24Mbps':monStaRxPktsAt24Mbps,'monStaRxBytesAt24Mbps':monStaRxBytesAt24Mbps,'monStaRxPktsAt36Mbps':monStaRxPktsAt36Mbps,'monStaRxBytesAt36Mbps':monStaRxBytesAt36Mbps,'monStaRxPktsAt48Mbps':monStaRxPktsAt48Mbps,'monStaRxBytesAt48Mbps':monStaRxBytesAt48Mbps,'monStaRxPktsAt54Mbps':monStaRxPktsAt54Mbps,'monStaRxBytesAt54Mbps':monStaRxBytesAt54Mbps,'monStaTxPktsAt9Mbps':monStaTxPktsAt9Mbps,'monStaTxBytesAt9Mbps':monStaTxBytesAt9Mbps,'monStaRxPktsAt9Mbps':monStaRxPktsAt9Mbps,'monStaRxBytesAt9Mbps':monStaRxBytesAt9Mbps,'wlsxMonStaDATypeStatsTable':wlsxMonStaDATypeStatsTable,'wlsxMonStaDATypeStatsEntry':wlsxMonStaDATypeStatsEntry,'monStaTxDABroadcastPkts':monStaTxDABroadcastPkts,'monStaTxDABroadcastBytes':monStaTxDABroadcastBytes,'monStaTxDAMulticastPkts':monStaTxDAMulticastPkts,'monStaTxDAMulticastBytes':monStaTxDAMulticastBytes,'monStaTxDAUnicastPkts':monStaTxDAUnicastPkts,'monStaTxDAUnicastBytes':monStaTxDAUnicastBytes,'wlsxMonStaFrameTypeStatsTable':wlsxMonStaFrameTypeStatsTable,'wlsxMonStaFrameTypeStatsEntry':wlsxMonStaFrameTypeStatsEntry,'monStaTxMgmtPkts':monStaTxMgmtPkts,'monStaTxMgmtBytes':monStaTxMgmtBytes,'monStaTxCtrlPkts':monStaTxCtrlPkts,'monStaTxCtrlBytes':monStaTxCtrlBytes,'monStaTxDataPkts':monStaTxDataPkts,'monStaTxDataBytes':monStaTxDataBytes,'monStaRxMgmtPkts':monStaRxMgmtPkts,'monStaRxMgmtBytes':monStaRxMgmtBytes,'monStaRxCtrlPkts':monStaRxCtrlPkts,'monStaRxCtrlBytes':monStaRxCtrlBytes,'monStaRxDataPkts':monStaRxDataPkts,'monStaRxDataBytes':monStaRxDataBytes,'wlsxMonStaPktSizeStatsTable':wlsxMonStaPktSizeStatsTable,'wlsxMonStaPktSizeStatsEntry':wlsxMonStaPktSizeStatsEntry,'monStaTxPkts63Bytes':monStaTxPkts63Bytes,'monStaTxPkts64To127':monStaTxPkts64To127,'monStaTxPkts128To255':monStaTxPkts128To255,'monStaTxPkts256To511':monStaTxPkts256To511,'monStaTxPkts512To1023':monStaTxPkts512To1023,'monStaTxPkts1024To1518':monStaTxPkts1024To1518,'monStaRxPkts63Bytes':monStaRxPkts63Bytes,'monStaRxPkts64To127':monStaRxPkts64To127,'monStaRxPkts128To255':monStaRxPkts128To255,'monStaRxPkts256To511':monStaRxPkts256To511,'monStaRxPkts512To1023':monStaRxPkts512To1023,'monStaRxPkts1024To1518':monStaRxPkts1024To1518,'wlsxMonEventCountTable':wlsxMonEventCountTable,'wlsxMonEventCountEntry':wlsxMonEventCountEntry,_L:monEventID,'monEventCount':monEventCount,'wlsxMonStationHTRateStatsTable':wlsxMonStationHTRateStatsTable,'wlsxMonStationHTRateStatsEntry':wlsxMonStationHTRateStatsEntry,'monStaTxHTPkts':monStaTxHTPkts,'monStaTxHTBytes':monStaTxHTBytes,'monStaRxHTPkts':monStaRxHTPkts,'monStaRxHTBytes':monStaRxHTBytes,'wlsxMonInfoGroup':wlsxMonInfoGroup,'wlsxMonAccessPointInfoGroup':wlsxMonAccessPointInfoGroup,'wlsxMonAPInfoTable':wlsxMonAPInfoTable,'wlsxMonAPInfoEntry':wlsxMonAPInfoEntry,'monAPInfoPhyType':monAPInfoPhyType,'monAPInfoCurrentChannel':monAPInfoCurrentChannel,'monAPInfoClassification':monAPInfoClassification,'monAPInfoESSID':monAPInfoESSID,'monAPInfoRSSI':monAPInfoRSSI,'monAPInfoMonitorTime':monAPInfoMonitorTime,'monAPInfoInactivityTime':monAPInfoInactivityTime,'monAPInfoSnrSignalPkts':monAPInfoSnrSignalPkts,'monAPInfoSnrSampleTime':monAPInfoSnrSampleTime,'monAPInfoStatus':monAPInfoStatus,'monAPInfoConfidence':monAPInfoConfidence,'monAPInfoMatchType':monAPInfoMatchType,'monAPInfoMatchMethod':monAPInfoMatchMethod,'monAPInfoHTMode':monAPInfoHTMode,'monAPInfoEncryptionType':monAPInfoEncryptionType,'monAPInfoWPAUnicastCipher':monAPInfoWPAUnicastCipher,'monAPInfoWPAAuthAlgorithm':monAPInfoWPAAuthAlgorithm,'monAPInfoIBSS':monAPInfoIBSS,'wlsxMonStationInfoGroup':wlsxMonStationInfoGroup,'wlsxMonStationInfoTable':wlsxMonStationInfoTable,'wlsxMonStationInfoEntry':wlsxMonStationInfoEntry,'monStaInfoChannelNum':monStaInfoChannelNum,'monStaInfoBSSID':monStaInfoBSSID,'monStaInfoESSID':monStaInfoESSID,'monStaInfoPhyType':monStaInfoPhyType,'monStaInfoRSSI':monStaInfoRSSI,'monStaInfoClassification':monStaInfoClassification,'monStaInfoMonitorTime':monStaInfoMonitorTime,'monStaInfoInactivityTime':monStaInfoInactivityTime,'monStaInfoSnrSignalPkts':monStaInfoSnrSignalPkts,'monStaInfoSnrSampleTime':monStaInfoSnrSampleTime,'monStaInfoStatus':monStaInfoStatus,'monStaInfoHTMode':monStaInfoHTMode})