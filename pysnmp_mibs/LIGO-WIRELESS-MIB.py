_R='ligoWiIfTxRetries'
_Q='ligoWiIfRxErrors'
_P='ligoWiIfLinkQuality'
_O='ligoWiIfNoiseLevel'
_N='ligoWiIfFrequency'
_M='ligoWiIfMacAddress'
_L='Integer32'
_K='ifPhysAddress'
_J='ligoWiRmtNodeMacAddress'
_I='OctetString'
_H='dBm'
_G='sysLocation'
_F='SNMPv2-MIB'
_E='LIGO-WIRELESS-MIB'
_D='ifIndex'
_C='IF-MIB'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_I,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ifIndex,ifPhysAddress=mibBuilder.importSymbols(_C,_D,_K)
ligoMgmt,=mibBuilder.importSymbols('LIGOWAVE-MIB','ligoMgmt')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
sysLocation,=mibBuilder.importSymbols(_F,_G)
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_L,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,MacAddress,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress','TextualConvention','TruthValue')
ligoWirelessMIB=ModuleIdentity((1,3,6,1,4,1,32750,3,10))
if mibBuilder.loadTexts:ligoWirelessMIB.setRevisions(('2011-11-11 11:11',))
_LigoWirelessMIBObjects_ObjectIdentity=ObjectIdentity
ligoWirelessMIBObjects=_LigoWirelessMIBObjects_ObjectIdentity((1,3,6,1,4,1,32750,3,10,1))
_LigoWiNotifs_ObjectIdentity=ObjectIdentity
ligoWiNotifs=_LigoWiNotifs_ObjectIdentity((1,3,6,1,4,1,32750,3,10,1,0))
_LigoWiInfo_ObjectIdentity=ObjectIdentity
ligoWiInfo=_LigoWiInfo_ObjectIdentity((1,3,6,1,4,1,32750,3,10,1,1))
_LigoWiConf_ObjectIdentity=ObjectIdentity
ligoWiConf=_LigoWiConf_ObjectIdentity((1,3,6,1,4,1,32750,3,10,1,2))
_LigoWiIfConfTable_Object=MibTable
ligoWiIfConfTable=_LigoWiIfConfTable_Object((1,3,6,1,4,1,32750,3,10,1,2,1))
if mibBuilder.loadTexts:ligoWiIfConfTable.setStatus(_A)
_LigoWiIfConfEntry_Object=MibTableRow
ligoWiIfConfEntry=_LigoWiIfConfEntry_Object((1,3,6,1,4,1,32750,3,10,1,2,1,1))
ligoWiIfConfEntry.setIndexNames((0,_C,_D))
if mibBuilder.loadTexts:ligoWiIfConfEntry.setStatus(_A)
_LigoWiIfMacAddress_Type=MacAddress
_LigoWiIfMacAddress_Object=MibTableColumn
ligoWiIfMacAddress=_LigoWiIfMacAddress_Object((1,3,6,1,4,1,32750,3,10,1,2,1,1,1),_LigoWiIfMacAddress_Type())
ligoWiIfMacAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:ligoWiIfMacAddress.setStatus(_A)
class _LigoWiIfProtocol_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,15))
_LigoWiIfProtocol_Type.__name__=_I
_LigoWiIfProtocol_Object=MibTableColumn
ligoWiIfProtocol=_LigoWiIfProtocol_Object((1,3,6,1,4,1,32750,3,10,1,2,1,1,2),_LigoWiIfProtocol_Type())
ligoWiIfProtocol.setMaxAccess(_B)
if mibBuilder.loadTexts:ligoWiIfProtocol.setStatus(_A)
class _LigoWiIfMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6)));namedValues=NamedValues(*(('auto',0),('adhoc',1),('managed',2),('master',3),('repeater',4),('secondary',5),('monitor',6)))
_LigoWiIfMode_Type.__name__=_L
_LigoWiIfMode_Object=MibTableColumn
ligoWiIfMode=_LigoWiIfMode_Object((1,3,6,1,4,1,32750,3,10,1,2,1,1,3),_LigoWiIfMode_Type())
ligoWiIfMode.setMaxAccess(_B)
if mibBuilder.loadTexts:ligoWiIfMode.setStatus(_A)
class _LigoWiIfESSID_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_LigoWiIfESSID_Type.__name__=_I
_LigoWiIfESSID_Object=MibTableColumn
ligoWiIfESSID=_LigoWiIfESSID_Object((1,3,6,1,4,1,32750,3,10,1,2,1,1,4),_LigoWiIfESSID_Type())
ligoWiIfESSID.setMaxAccess(_B)
if mibBuilder.loadTexts:ligoWiIfESSID.setStatus(_A)
class _LigoWiIfCountryCode_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(2,3))
_LigoWiIfCountryCode_Type.__name__=_I
_LigoWiIfCountryCode_Object=MibTableColumn
ligoWiIfCountryCode=_LigoWiIfCountryCode_Object((1,3,6,1,4,1,32750,3,10,1,2,1,1,5),_LigoWiIfCountryCode_Type())
ligoWiIfCountryCode.setMaxAccess(_B)
if mibBuilder.loadTexts:ligoWiIfCountryCode.setStatus(_A)
_LigoWiIfFrequency_Type=Integer32
_LigoWiIfFrequency_Object=MibTableColumn
ligoWiIfFrequency=_LigoWiIfFrequency_Object((1,3,6,1,4,1,32750,3,10,1,2,1,1,6),_LigoWiIfFrequency_Type())
ligoWiIfFrequency.setMaxAccess(_B)
if mibBuilder.loadTexts:ligoWiIfFrequency.setStatus(_A)
if mibBuilder.loadTexts:ligoWiIfFrequency.setUnits('MHz')
_LigoWiIfChannel_Type=Integer32
_LigoWiIfChannel_Object=MibTableColumn
ligoWiIfChannel=_LigoWiIfChannel_Object((1,3,6,1,4,1,32750,3,10,1,2,1,1,7),_LigoWiIfChannel_Type())
ligoWiIfChannel.setMaxAccess(_B)
if mibBuilder.loadTexts:ligoWiIfChannel.setStatus(_A)
_LigoWiIfChannelBandwidth_Type=Integer32
_LigoWiIfChannelBandwidth_Object=MibTableColumn
ligoWiIfChannelBandwidth=_LigoWiIfChannelBandwidth_Object((1,3,6,1,4,1,32750,3,10,1,2,1,1,8),_LigoWiIfChannelBandwidth_Type())
ligoWiIfChannelBandwidth.setMaxAccess(_B)
if mibBuilder.loadTexts:ligoWiIfChannelBandwidth.setStatus(_A)
if mibBuilder.loadTexts:ligoWiIfChannelBandwidth.setUnits('MHz')
class _LigoWiIfEncryption_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7,8,9,10)));namedValues=NamedValues(*(('unknown',0),('open',1),('wep64bit',2),('wep128bit',3),('wep',4),('enterpriseWpa',5),('personalWpa',6),('enterpriseWpa2',7),('personalWpa2',8),('enterpriseWpaOrWpa2',9),('personalWpaOrWpa2',10)))
_LigoWiIfEncryption_Type.__name__=_L
_LigoWiIfEncryption_Object=MibTableColumn
ligoWiIfEncryption=_LigoWiIfEncryption_Object((1,3,6,1,4,1,32750,3,10,1,2,1,1,9),_LigoWiIfEncryption_Type())
ligoWiIfEncryption.setMaxAccess(_B)
if mibBuilder.loadTexts:ligoWiIfEncryption.setStatus(_A)
_LigoWiIfTxPower_Type=Gauge32
_LigoWiIfTxPower_Object=MibTableColumn
ligoWiIfTxPower=_LigoWiIfTxPower_Object((1,3,6,1,4,1,32750,3,10,1,2,1,1,10),_LigoWiIfTxPower_Type())
ligoWiIfTxPower.setMaxAccess(_B)
if mibBuilder.loadTexts:ligoWiIfTxPower.setStatus(_A)
if mibBuilder.loadTexts:ligoWiIfTxPower.setUnits(_H)
_LigoWiIfBitRate_Type=Gauge32
_LigoWiIfBitRate_Object=MibTableColumn
ligoWiIfBitRate=_LigoWiIfBitRate_Object((1,3,6,1,4,1,32750,3,10,1,2,1,1,11),_LigoWiIfBitRate_Type())
ligoWiIfBitRate.setMaxAccess(_B)
if mibBuilder.loadTexts:ligoWiIfBitRate.setStatus(_A)
if mibBuilder.loadTexts:ligoWiIfBitRate.setUnits('kbit/s')
_LigoWiIfLinkQuality_Type=Gauge32
_LigoWiIfLinkQuality_Object=MibTableColumn
ligoWiIfLinkQuality=_LigoWiIfLinkQuality_Object((1,3,6,1,4,1,32750,3,10,1,2,1,1,12),_LigoWiIfLinkQuality_Type())
ligoWiIfLinkQuality.setMaxAccess(_B)
if mibBuilder.loadTexts:ligoWiIfLinkQuality.setStatus(_A)
_LigoWiIfMaxLinkQuality_Type=Gauge32
_LigoWiIfMaxLinkQuality_Object=MibTableColumn
ligoWiIfMaxLinkQuality=_LigoWiIfMaxLinkQuality_Object((1,3,6,1,4,1,32750,3,10,1,2,1,1,13),_LigoWiIfMaxLinkQuality_Type())
ligoWiIfMaxLinkQuality.setMaxAccess(_B)
if mibBuilder.loadTexts:ligoWiIfMaxLinkQuality.setStatus(_A)
_LigoWiIfSignalLevel_Type=Integer32
_LigoWiIfSignalLevel_Object=MibTableColumn
ligoWiIfSignalLevel=_LigoWiIfSignalLevel_Object((1,3,6,1,4,1,32750,3,10,1,2,1,1,14),_LigoWiIfSignalLevel_Type())
ligoWiIfSignalLevel.setMaxAccess(_B)
if mibBuilder.loadTexts:ligoWiIfSignalLevel.setStatus(_A)
if mibBuilder.loadTexts:ligoWiIfSignalLevel.setUnits(_H)
_LigoWiIfNoiseLevel_Type=Integer32
_LigoWiIfNoiseLevel_Object=MibTableColumn
ligoWiIfNoiseLevel=_LigoWiIfNoiseLevel_Object((1,3,6,1,4,1,32750,3,10,1,2,1,1,15),_LigoWiIfNoiseLevel_Type())
ligoWiIfNoiseLevel.setMaxAccess(_B)
if mibBuilder.loadTexts:ligoWiIfNoiseLevel.setStatus(_A)
if mibBuilder.loadTexts:ligoWiIfNoiseLevel.setUnits(_H)
_LigoWiIfAssocNodeCount_Type=Gauge32
_LigoWiIfAssocNodeCount_Object=MibTableColumn
ligoWiIfAssocNodeCount=_LigoWiIfAssocNodeCount_Object((1,3,6,1,4,1,32750,3,10,1,2,1,1,16),_LigoWiIfAssocNodeCount_Type())
ligoWiIfAssocNodeCount.setMaxAccess(_B)
if mibBuilder.loadTexts:ligoWiIfAssocNodeCount.setStatus(_A)
_LigoWiStats_ObjectIdentity=ObjectIdentity
ligoWiStats=_LigoWiStats_ObjectIdentity((1,3,6,1,4,1,32750,3,10,1,3))
_LigoWiIfStatsTable_Object=MibTable
ligoWiIfStatsTable=_LigoWiIfStatsTable_Object((1,3,6,1,4,1,32750,3,10,1,3,1))
if mibBuilder.loadTexts:ligoWiIfStatsTable.setStatus(_A)
_LigoWiIfStatsEntry_Object=MibTableRow
ligoWiIfStatsEntry=_LigoWiIfStatsEntry_Object((1,3,6,1,4,1,32750,3,10,1,3,1,1))
ligoWiIfStatsEntry.setIndexNames((0,_C,_D))
if mibBuilder.loadTexts:ligoWiIfStatsEntry.setStatus(_A)
_LigoWiIfRxTotal_Type=Counter32
_LigoWiIfRxTotal_Object=MibTableColumn
ligoWiIfRxTotal=_LigoWiIfRxTotal_Object((1,3,6,1,4,1,32750,3,10,1,3,1,1,1),_LigoWiIfRxTotal_Type())
ligoWiIfRxTotal.setMaxAccess(_B)
if mibBuilder.loadTexts:ligoWiIfRxTotal.setStatus(_A)
_LigoWiIfRxErrors_Type=Counter32
_LigoWiIfRxErrors_Object=MibTableColumn
ligoWiIfRxErrors=_LigoWiIfRxErrors_Object((1,3,6,1,4,1,32750,3,10,1,3,1,1,2),_LigoWiIfRxErrors_Type())
ligoWiIfRxErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:ligoWiIfRxErrors.setStatus(_A)
_LigoWiIfTxTotal_Type=Counter32
_LigoWiIfTxTotal_Object=MibTableColumn
ligoWiIfTxTotal=_LigoWiIfTxTotal_Object((1,3,6,1,4,1,32750,3,10,1,3,1,1,3),_LigoWiIfTxTotal_Type())
ligoWiIfTxTotal.setMaxAccess(_B)
if mibBuilder.loadTexts:ligoWiIfTxTotal.setStatus(_A)
_LigoWiIfTxRetries_Type=Counter32
_LigoWiIfTxRetries_Object=MibTableColumn
ligoWiIfTxRetries=_LigoWiIfTxRetries_Object((1,3,6,1,4,1,32750,3,10,1,3,1,1,4),_LigoWiIfTxRetries_Type())
ligoWiIfTxRetries.setMaxAccess(_B)
if mibBuilder.loadTexts:ligoWiIfTxRetries.setStatus(_A)
_LigoWiRemoteNodeStatsTable_Object=MibTable
ligoWiRemoteNodeStatsTable=_LigoWiRemoteNodeStatsTable_Object((1,3,6,1,4,1,32750,3,10,1,3,2))
if mibBuilder.loadTexts:ligoWiRemoteNodeStatsTable.setStatus(_A)
_LigoWiRemoteNodeStatsEntry_Object=MibTableRow
ligoWiRemoteNodeStatsEntry=_LigoWiRemoteNodeStatsEntry_Object((1,3,6,1,4,1,32750,3,10,1,3,2,1))
ligoWiRemoteNodeStatsEntry.setIndexNames((0,_C,_D),(0,_E,_J))
if mibBuilder.loadTexts:ligoWiRemoteNodeStatsEntry.setStatus(_A)
_LigoWiRmtNodeMacAddress_Type=MacAddress
_LigoWiRmtNodeMacAddress_Object=MibTableColumn
ligoWiRmtNodeMacAddress=_LigoWiRmtNodeMacAddress_Object((1,3,6,1,4,1,32750,3,10,1,3,2,1,1),_LigoWiRmtNodeMacAddress_Type())
ligoWiRmtNodeMacAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:ligoWiRmtNodeMacAddress.setStatus(_A)
_LigoWiRmtNodeAssociated_Type=TruthValue
_LigoWiRmtNodeAssociated_Object=MibTableColumn
ligoWiRmtNodeAssociated=_LigoWiRmtNodeAssociated_Object((1,3,6,1,4,1,32750,3,10,1,3,2,1,2),_LigoWiRmtNodeAssociated_Type())
ligoWiRmtNodeAssociated.setMaxAccess(_B)
if mibBuilder.loadTexts:ligoWiRmtNodeAssociated.setStatus(_A)
_LigoWiRmtNodeTxBytes_Type=Counter32
_LigoWiRmtNodeTxBytes_Object=MibTableColumn
ligoWiRmtNodeTxBytes=_LigoWiRmtNodeTxBytes_Object((1,3,6,1,4,1,32750,3,10,1,3,2,1,3),_LigoWiRmtNodeTxBytes_Type())
ligoWiRmtNodeTxBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:ligoWiRmtNodeTxBytes.setStatus(_A)
if mibBuilder.loadTexts:ligoWiRmtNodeTxBytes.setUnits('bytes')
_LigoWiRmtNodeRxBytes_Type=Counter32
_LigoWiRmtNodeRxBytes_Object=MibTableColumn
ligoWiRmtNodeRxBytes=_LigoWiRmtNodeRxBytes_Object((1,3,6,1,4,1,32750,3,10,1,3,2,1,4),_LigoWiRmtNodeRxBytes_Type())
ligoWiRmtNodeRxBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:ligoWiRmtNodeRxBytes.setStatus(_A)
if mibBuilder.loadTexts:ligoWiRmtNodeRxBytes.setUnits('bytes')
_LigoWiRmtNodeSignalLevel_Type=Integer32
_LigoWiRmtNodeSignalLevel_Object=MibTableColumn
ligoWiRmtNodeSignalLevel=_LigoWiRmtNodeSignalLevel_Object((1,3,6,1,4,1,32750,3,10,1,3,2,1,5),_LigoWiRmtNodeSignalLevel_Type())
ligoWiRmtNodeSignalLevel.setMaxAccess(_B)
if mibBuilder.loadTexts:ligoWiRmtNodeSignalLevel.setStatus(_A)
if mibBuilder.loadTexts:ligoWiRmtNodeSignalLevel.setUnits(_H)
_LigoWiRmtNodeNoiseLevel_Type=Integer32
_LigoWiRmtNodeNoiseLevel_Object=MibTableColumn
ligoWiRmtNodeNoiseLevel=_LigoWiRmtNodeNoiseLevel_Object((1,3,6,1,4,1,32750,3,10,1,3,2,1,6),_LigoWiRmtNodeNoiseLevel_Type())
ligoWiRmtNodeNoiseLevel.setMaxAccess(_B)
if mibBuilder.loadTexts:ligoWiRmtNodeNoiseLevel.setStatus(_A)
if mibBuilder.loadTexts:ligoWiRmtNodeNoiseLevel.setUnits(_H)
ligoWiFrequencyChange=NotificationType((1,3,6,1,4,1,32750,3,10,1,0,1))
ligoWiFrequencyChange.setObjects(*((_F,_G),(_C,_D),(_E,_N)))
if mibBuilder.loadTexts:ligoWiFrequencyChange.setStatus(_A)
ligoWiNoiseThresholdReached=NotificationType((1,3,6,1,4,1,32750,3,10,1,0,2))
ligoWiNoiseThresholdReached.setObjects(*((_F,_G),(_C,_D),(_E,_O)))
if mibBuilder.loadTexts:ligoWiNoiseThresholdReached.setStatus(_A)
ligoWiRemoteNodeConnected=NotificationType((1,3,6,1,4,1,32750,3,10,1,0,3))
ligoWiRemoteNodeConnected.setObjects(*((_F,_G),(_C,_K),(_C,_D),(_E,_J)))
if mibBuilder.loadTexts:ligoWiRemoteNodeConnected.setStatus(_A)
ligoWiRemoteNodeDisconnected=NotificationType((1,3,6,1,4,1,32750,3,10,1,0,4))
ligoWiRemoteNodeDisconnected.setObjects(*((_F,_G),(_C,_K),(_C,_D),(_E,_J)))
if mibBuilder.loadTexts:ligoWiRemoteNodeDisconnected.setStatus(_A)
ligoWiLinkQualThresholdReached=NotificationType((1,3,6,1,4,1,32750,3,10,1,0,5))
ligoWiLinkQualThresholdReached.setObjects(*((_F,_G),(_C,_D),(_E,_P)))
if mibBuilder.loadTexts:ligoWiLinkQualThresholdReached.setStatus(_A)
ligoWiRxErrorsThreshold=NotificationType((1,3,6,1,4,1,32750,3,10,1,0,6))
ligoWiRxErrorsThreshold.setObjects(*((_F,_G),(_C,_D),(_E,_M),(_E,_Q)))
if mibBuilder.loadTexts:ligoWiRxErrorsThreshold.setStatus(_A)
ligoWiTxRetriesThreshold=NotificationType((1,3,6,1,4,1,32750,3,10,1,0,7))
ligoWiTxRetriesThreshold.setObjects(*((_F,_G),(_C,_D),(_E,_M),(_E,_R)))
if mibBuilder.loadTexts:ligoWiTxRetriesThreshold.setStatus(_A)
mibBuilder.exportSymbols(_E,**{'ligoWirelessMIB':ligoWirelessMIB,'ligoWirelessMIBObjects':ligoWirelessMIBObjects,'ligoWiNotifs':ligoWiNotifs,'ligoWiFrequencyChange':ligoWiFrequencyChange,'ligoWiNoiseThresholdReached':ligoWiNoiseThresholdReached,'ligoWiRemoteNodeConnected':ligoWiRemoteNodeConnected,'ligoWiRemoteNodeDisconnected':ligoWiRemoteNodeDisconnected,'ligoWiLinkQualThresholdReached':ligoWiLinkQualThresholdReached,'ligoWiRxErrorsThreshold':ligoWiRxErrorsThreshold,'ligoWiTxRetriesThreshold':ligoWiTxRetriesThreshold,'ligoWiInfo':ligoWiInfo,'ligoWiConf':ligoWiConf,'ligoWiIfConfTable':ligoWiIfConfTable,'ligoWiIfConfEntry':ligoWiIfConfEntry,_M:ligoWiIfMacAddress,'ligoWiIfProtocol':ligoWiIfProtocol,'ligoWiIfMode':ligoWiIfMode,'ligoWiIfESSID':ligoWiIfESSID,'ligoWiIfCountryCode':ligoWiIfCountryCode,_N:ligoWiIfFrequency,'ligoWiIfChannel':ligoWiIfChannel,'ligoWiIfChannelBandwidth':ligoWiIfChannelBandwidth,'ligoWiIfEncryption':ligoWiIfEncryption,'ligoWiIfTxPower':ligoWiIfTxPower,'ligoWiIfBitRate':ligoWiIfBitRate,_P:ligoWiIfLinkQuality,'ligoWiIfMaxLinkQuality':ligoWiIfMaxLinkQuality,'ligoWiIfSignalLevel':ligoWiIfSignalLevel,_O:ligoWiIfNoiseLevel,'ligoWiIfAssocNodeCount':ligoWiIfAssocNodeCount,'ligoWiStats':ligoWiStats,'ligoWiIfStatsTable':ligoWiIfStatsTable,'ligoWiIfStatsEntry':ligoWiIfStatsEntry,'ligoWiIfRxTotal':ligoWiIfRxTotal,_Q:ligoWiIfRxErrors,'ligoWiIfTxTotal':ligoWiIfTxTotal,_R:ligoWiIfTxRetries,'ligoWiRemoteNodeStatsTable':ligoWiRemoteNodeStatsTable,'ligoWiRemoteNodeStatsEntry':ligoWiRemoteNodeStatsEntry,_J:ligoWiRmtNodeMacAddress,'ligoWiRmtNodeAssociated':ligoWiRmtNodeAssociated,'ligoWiRmtNodeTxBytes':ligoWiRmtNodeTxBytes,'ligoWiRmtNodeRxBytes':ligoWiRmtNodeRxBytes,'ligoWiRmtNodeSignalLevel':ligoWiRmtNodeSignalLevel,'ligoWiRmtNodeNoiseLevel':ligoWiRmtNodeNoiseLevel})