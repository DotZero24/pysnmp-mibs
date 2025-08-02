_G='ahXIfEntry'
_F='ahClientMac'
_E='AH-INTERFACE-MIB'
_D='ifIndex'
_C='IF-MIB'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
AhInterfaceMode,AhInterfaceType,AhMACProtocol,AhNodeID,AhString,ahAPInterface=mibBuilder.importSymbols('AH-SMI-MIB','AhInterfaceMode','AhInterfaceType','AhMACProtocol','AhNodeID','AhString','ahAPInterface')
ifEntry,ifIndex=mibBuilder.importSymbols(_C,'ifEntry',_D)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention','TruthValue')
ahInterface=ModuleIdentity((1,3,6,1,4,1,26928,1,1,1,2,1))
class AhAuthenticationMethod(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7,8,9,10)));namedValues=NamedValues(*(('cwp',0),('open',1),('wep-open',2),('wep-shared',3),('wpa-psk',4),('wpa2-psk',5),('wpa-8021x',6),('wpa2-8021X',7),('wpa-auto-psk',8),('wpa-auto-8021x',9),('dynamic-wep',10)))
class AhEncrytionMethod(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*(('AES',0),('TKIP',1),('WEP',2),('Non',3)))
_AhXIfTable_Object=MibTable
ahXIfTable=_AhXIfTable_Object((1,3,6,1,4,1,26928,1,1,1,2,1,1))
if mibBuilder.loadTexts:ahXIfTable.setStatus(_A)
_AhXIfEntry_Object=MibTableRow
ahXIfEntry=_AhXIfEntry_Object((1,3,6,1,4,1,26928,1,1,1,2,1,1,1))
if mibBuilder.loadTexts:ahXIfEntry.setStatus(_A)
_AhIfName_Type=AhString
_AhIfName_Object=MibTableColumn
ahIfName=_AhIfName_Object((1,3,6,1,4,1,26928,1,1,1,2,1,1,1,1),_AhIfName_Type())
ahIfName.setMaxAccess(_B)
if mibBuilder.loadTexts:ahIfName.setStatus(_A)
_AhSSIDName_Type=AhString
_AhSSIDName_Object=MibTableColumn
ahSSIDName=_AhSSIDName_Object((1,3,6,1,4,1,26928,1,1,1,2,1,1,1,2),_AhSSIDName_Type())
ahSSIDName.setMaxAccess(_B)
if mibBuilder.loadTexts:ahSSIDName.setStatus(_A)
_AhIfPromiscuous_Type=TruthValue
_AhIfPromiscuous_Object=MibTableColumn
ahIfPromiscuous=_AhIfPromiscuous_Object((1,3,6,1,4,1,26928,1,1,1,2,1,1,1,3),_AhIfPromiscuous_Type())
ahIfPromiscuous.setMaxAccess(_B)
if mibBuilder.loadTexts:ahIfPromiscuous.setStatus(_A)
_AhIfType_Type=AhInterfaceType
_AhIfType_Object=MibTableColumn
ahIfType=_AhIfType_Object((1,3,6,1,4,1,26928,1,1,1,2,1,1,1,4),_AhIfType_Type())
ahIfType.setMaxAccess(_B)
if mibBuilder.loadTexts:ahIfType.setStatus(_A)
_AhIfMode_Type=AhInterfaceMode
_AhIfMode_Object=MibTableColumn
ahIfMode=_AhIfMode_Object((1,3,6,1,4,1,26928,1,1,1,2,1,1,1,5),_AhIfMode_Type())
ahIfMode.setMaxAccess(_B)
if mibBuilder.loadTexts:ahIfMode.setStatus(_A)
_AhIfConfMode_Type=AhInterfaceMode
_AhIfConfMode_Object=MibTableColumn
ahIfConfMode=_AhIfConfMode_Object((1,3,6,1,4,1,26928,1,1,1,2,1,1,1,6),_AhIfConfMode_Type())
ahIfConfMode.setMaxAccess(_B)
if mibBuilder.loadTexts:ahIfConfMode.setStatus(_A)
_AhAssociationTable_Object=MibTable
ahAssociationTable=_AhAssociationTable_Object((1,3,6,1,4,1,26928,1,1,1,2,1,2))
if mibBuilder.loadTexts:ahAssociationTable.setStatus(_A)
_AhAssociationEntry_Object=MibTableRow
ahAssociationEntry=_AhAssociationEntry_Object((1,3,6,1,4,1,26928,1,1,1,2,1,2,1))
ahAssociationEntry.setIndexNames((0,_C,_D),(0,_E,_F))
if mibBuilder.loadTexts:ahAssociationEntry.setStatus(_A)
_AhClientMac_Type=AhNodeID
_AhClientMac_Object=MibTableColumn
ahClientMac=_AhClientMac_Object((1,3,6,1,4,1,26928,1,1,1,2,1,2,1,1),_AhClientMac_Type())
ahClientMac.setMaxAccess(_B)
if mibBuilder.loadTexts:ahClientMac.setStatus(_A)
_AhClientIP_Type=IpAddress
_AhClientIP_Object=MibTableColumn
ahClientIP=_AhClientIP_Object((1,3,6,1,4,1,26928,1,1,1,2,1,2,1,2),_AhClientIP_Type())
ahClientIP.setMaxAccess(_B)
if mibBuilder.loadTexts:ahClientIP.setStatus(_A)
_AhClientHostname_Type=AhString
_AhClientHostname_Object=MibTableColumn
ahClientHostname=_AhClientHostname_Object((1,3,6,1,4,1,26928,1,1,1,2,1,2,1,3),_AhClientHostname_Type())
ahClientHostname.setMaxAccess(_B)
if mibBuilder.loadTexts:ahClientHostname.setStatus(_A)
_AhClientRSSI_Type=Integer32
_AhClientRSSI_Object=MibTableColumn
ahClientRSSI=_AhClientRSSI_Object((1,3,6,1,4,1,26928,1,1,1,2,1,2,1,4),_AhClientRSSI_Type())
ahClientRSSI.setMaxAccess(_B)
if mibBuilder.loadTexts:ahClientRSSI.setStatus(_A)
_AhClientLinkUptime_Type=Counter32
_AhClientLinkUptime_Object=MibTableColumn
ahClientLinkUptime=_AhClientLinkUptime_Object((1,3,6,1,4,1,26928,1,1,1,2,1,2,1,5),_AhClientLinkUptime_Type())
ahClientLinkUptime.setMaxAccess(_B)
if mibBuilder.loadTexts:ahClientLinkUptime.setStatus(_A)
_AhClientCWPUsed_Type=TruthValue
_AhClientCWPUsed_Object=MibTableColumn
ahClientCWPUsed=_AhClientCWPUsed_Object((1,3,6,1,4,1,26928,1,1,1,2,1,2,1,6),_AhClientCWPUsed_Type())
ahClientCWPUsed.setMaxAccess(_B)
if mibBuilder.loadTexts:ahClientCWPUsed.setStatus(_A)
_AhClientAuthMethod_Type=AhAuthenticationMethod
_AhClientAuthMethod_Object=MibTableColumn
ahClientAuthMethod=_AhClientAuthMethod_Object((1,3,6,1,4,1,26928,1,1,1,2,1,2,1,7),_AhClientAuthMethod_Type())
ahClientAuthMethod.setMaxAccess(_B)
if mibBuilder.loadTexts:ahClientAuthMethod.setStatus(_A)
_AhClientEncryptionMethod_Type=AhEncrytionMethod
_AhClientEncryptionMethod_Object=MibTableColumn
ahClientEncryptionMethod=_AhClientEncryptionMethod_Object((1,3,6,1,4,1,26928,1,1,1,2,1,2,1,8),_AhClientEncryptionMethod_Type())
ahClientEncryptionMethod.setMaxAccess(_B)
if mibBuilder.loadTexts:ahClientEncryptionMethod.setStatus(_A)
_AhClientMACProtocol_Type=AhMACProtocol
_AhClientMACProtocol_Object=MibTableColumn
ahClientMACProtocol=_AhClientMACProtocol_Object((1,3,6,1,4,1,26928,1,1,1,2,1,2,1,9),_AhClientMACProtocol_Type())
ahClientMACProtocol.setMaxAccess(_B)
if mibBuilder.loadTexts:ahClientMACProtocol.setStatus(_A)
_AhClientSSID_Type=AhString
_AhClientSSID_Object=MibTableColumn
ahClientSSID=_AhClientSSID_Object((1,3,6,1,4,1,26928,1,1,1,2,1,2,1,10),_AhClientSSID_Type())
ahClientSSID.setMaxAccess(_B)
if mibBuilder.loadTexts:ahClientSSID.setStatus(_A)
_AhClientVLAN_Type=Integer32
_AhClientVLAN_Object=MibTableColumn
ahClientVLAN=_AhClientVLAN_Object((1,3,6,1,4,1,26928,1,1,1,2,1,2,1,11),_AhClientVLAN_Type())
ahClientVLAN.setMaxAccess(_B)
if mibBuilder.loadTexts:ahClientVLAN.setStatus(_A)
_AhClientUserProfId_Type=Integer32
_AhClientUserProfId_Object=MibTableColumn
ahClientUserProfId=_AhClientUserProfId_Object((1,3,6,1,4,1,26928,1,1,1,2,1,2,1,12),_AhClientUserProfId_Type())
ahClientUserProfId.setMaxAccess(_B)
if mibBuilder.loadTexts:ahClientUserProfId.setStatus(_A)
_AhClientChannel_Type=Integer32
_AhClientChannel_Object=MibTableColumn
ahClientChannel=_AhClientChannel_Object((1,3,6,1,4,1,26928,1,1,1,2,1,2,1,13),_AhClientChannel_Type())
ahClientChannel.setMaxAccess(_B)
if mibBuilder.loadTexts:ahClientChannel.setStatus(_A)
_AhClientLastTxRate_Type=Integer32
_AhClientLastTxRate_Object=MibTableColumn
ahClientLastTxRate=_AhClientLastTxRate_Object((1,3,6,1,4,1,26928,1,1,1,2,1,2,1,14),_AhClientLastTxRate_Type())
ahClientLastTxRate.setMaxAccess(_B)
if mibBuilder.loadTexts:ahClientLastTxRate.setStatus(_A)
_AhClientUsername_Type=AhString
_AhClientUsername_Object=MibTableColumn
ahClientUsername=_AhClientUsername_Object((1,3,6,1,4,1,26928,1,1,1,2,1,2,1,15),_AhClientUsername_Type())
ahClientUsername.setMaxAccess(_B)
if mibBuilder.loadTexts:ahClientUsername.setStatus(_A)
_AhClientRxDataFrames_Type=Counter32
_AhClientRxDataFrames_Object=MibTableColumn
ahClientRxDataFrames=_AhClientRxDataFrames_Object((1,3,6,1,4,1,26928,1,1,1,2,1,2,1,16),_AhClientRxDataFrames_Type())
ahClientRxDataFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:ahClientRxDataFrames.setStatus(_A)
_AhClientRxDataOctets_Type=Counter32
_AhClientRxDataOctets_Object=MibTableColumn
ahClientRxDataOctets=_AhClientRxDataOctets_Object((1,3,6,1,4,1,26928,1,1,1,2,1,2,1,17),_AhClientRxDataOctets_Type())
ahClientRxDataOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:ahClientRxDataOctets.setStatus(_A)
_AhClientRxMgtFrames_Type=Counter32
_AhClientRxMgtFrames_Object=MibTableColumn
ahClientRxMgtFrames=_AhClientRxMgtFrames_Object((1,3,6,1,4,1,26928,1,1,1,2,1,2,1,18),_AhClientRxMgtFrames_Type())
ahClientRxMgtFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:ahClientRxMgtFrames.setStatus(_A)
_AhClientRxUnicastFrames_Type=Counter32
_AhClientRxUnicastFrames_Object=MibTableColumn
ahClientRxUnicastFrames=_AhClientRxUnicastFrames_Object((1,3,6,1,4,1,26928,1,1,1,2,1,2,1,19),_AhClientRxUnicastFrames_Type())
ahClientRxUnicastFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:ahClientRxUnicastFrames.setStatus(_A)
_AhClientRxMulticastFrames_Type=Counter32
_AhClientRxMulticastFrames_Object=MibScalar
ahClientRxMulticastFrames=_AhClientRxMulticastFrames_Object((1,3,6,1,4,1,26928,1,1,1,2,1,2,1,20),_AhClientRxMulticastFrames_Type())
ahClientRxMulticastFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:ahClientRxMulticastFrames.setStatus(_A)
_AhClientRxBroadcastFrames_Type=Counter32
_AhClientRxBroadcastFrames_Object=MibScalar
ahClientRxBroadcastFrames=_AhClientRxBroadcastFrames_Object((1,3,6,1,4,1,26928,1,1,1,2,1,2,1,21),_AhClientRxBroadcastFrames_Type())
ahClientRxBroadcastFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:ahClientRxBroadcastFrames.setStatus(_A)
_AhClientRxMICFailures_Type=Counter32
_AhClientRxMICFailures_Object=MibTableColumn
ahClientRxMICFailures=_AhClientRxMICFailures_Object((1,3,6,1,4,1,26928,1,1,1,2,1,2,1,22),_AhClientRxMICFailures_Type())
ahClientRxMICFailures.setMaxAccess(_B)
if mibBuilder.loadTexts:ahClientRxMICFailures.setStatus(_A)
_AhClientTxDataFrames_Type=Counter32
_AhClientTxDataFrames_Object=MibTableColumn
ahClientTxDataFrames=_AhClientTxDataFrames_Object((1,3,6,1,4,1,26928,1,1,1,2,1,2,1,23),_AhClientTxDataFrames_Type())
ahClientTxDataFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:ahClientTxDataFrames.setStatus(_A)
_AhClientTxMgtFrames_Type=Counter32
_AhClientTxMgtFrames_Object=MibTableColumn
ahClientTxMgtFrames=_AhClientTxMgtFrames_Object((1,3,6,1,4,1,26928,1,1,1,2,1,2,1,24),_AhClientTxMgtFrames_Type())
ahClientTxMgtFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:ahClientTxMgtFrames.setStatus(_A)
_AhClientTxDataOctets_Type=Counter32
_AhClientTxDataOctets_Object=MibTableColumn
ahClientTxDataOctets=_AhClientTxDataOctets_Object((1,3,6,1,4,1,26928,1,1,1,2,1,2,1,25),_AhClientTxDataOctets_Type())
ahClientTxDataOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:ahClientTxDataOctets.setStatus(_A)
_AhClientTxUnicastFrames_Type=Counter32
_AhClientTxUnicastFrames_Object=MibTableColumn
ahClientTxUnicastFrames=_AhClientTxUnicastFrames_Object((1,3,6,1,4,1,26928,1,1,1,2,1,2,1,26),_AhClientTxUnicastFrames_Type())
ahClientTxUnicastFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:ahClientTxUnicastFrames.setStatus(_A)
_AhClientTxMulticastFrames_Type=Counter32
_AhClientTxMulticastFrames_Object=MibTableColumn
ahClientTxMulticastFrames=_AhClientTxMulticastFrames_Object((1,3,6,1,4,1,26928,1,1,1,2,1,2,1,27),_AhClientTxMulticastFrames_Type())
ahClientTxMulticastFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:ahClientTxMulticastFrames.setStatus(_A)
_AhClientTxBroadcastFrames_Type=Counter32
_AhClientTxBroadcastFrames_Object=MibTableColumn
ahClientTxBroadcastFrames=_AhClientTxBroadcastFrames_Object((1,3,6,1,4,1,26928,1,1,1,2,1,2,1,28),_AhClientTxBroadcastFrames_Type())
ahClientTxBroadcastFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:ahClientTxBroadcastFrames.setStatus(_A)
_AhClientLastRxRate_Type=Integer32
_AhClientLastRxRate_Object=MibTableColumn
ahClientLastRxRate=_AhClientLastRxRate_Object((1,3,6,1,4,1,26928,1,1,1,2,1,2,1,29),_AhClientLastRxRate_Type())
ahClientLastRxRate.setMaxAccess(_B)
if mibBuilder.loadTexts:ahClientLastRxRate.setStatus(_A)
_AhClientTxBeDataFrames_Type=Counter32
_AhClientTxBeDataFrames_Object=MibTableColumn
ahClientTxBeDataFrames=_AhClientTxBeDataFrames_Object((1,3,6,1,4,1,26928,1,1,1,2,1,2,1,30),_AhClientTxBeDataFrames_Type())
ahClientTxBeDataFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:ahClientTxBeDataFrames.setStatus(_A)
_AhClientTxBgDataFrames_Type=Counter32
_AhClientTxBgDataFrames_Object=MibTableColumn
ahClientTxBgDataFrames=_AhClientTxBgDataFrames_Object((1,3,6,1,4,1,26928,1,1,1,2,1,2,1,31),_AhClientTxBgDataFrames_Type())
ahClientTxBgDataFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:ahClientTxBgDataFrames.setStatus(_A)
_AhClientTxViDataFrames_Type=Counter32
_AhClientTxViDataFrames_Object=MibTableColumn
ahClientTxViDataFrames=_AhClientTxViDataFrames_Object((1,3,6,1,4,1,26928,1,1,1,2,1,2,1,32),_AhClientTxViDataFrames_Type())
ahClientTxViDataFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:ahClientTxViDataFrames.setStatus(_A)
_AhClientTxVoDataFrames_Type=Counter32
_AhClientTxVoDataFrames_Object=MibTableColumn
ahClientTxVoDataFrames=_AhClientTxVoDataFrames_Object((1,3,6,1,4,1,26928,1,1,1,2,1,2,1,33),_AhClientTxVoDataFrames_Type())
ahClientTxVoDataFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:ahClientTxVoDataFrames.setStatus(_A)
_AhClientTxAirtime_Type=Counter64
_AhClientTxAirtime_Object=MibTableColumn
ahClientTxAirtime=_AhClientTxAirtime_Object((1,3,6,1,4,1,26928,1,1,1,2,1,2,1,34),_AhClientTxAirtime_Type())
ahClientTxAirtime.setMaxAccess(_B)
if mibBuilder.loadTexts:ahClientTxAirtime.setStatus(_A)
_AhClientRxAirtime_Type=Counter64
_AhClientRxAirtime_Object=MibTableColumn
ahClientRxAirtime=_AhClientRxAirtime_Object((1,3,6,1,4,1,26928,1,1,1,2,1,2,1,35),_AhClientRxAirtime_Type())
ahClientRxAirtime.setMaxAccess(_B)
if mibBuilder.loadTexts:ahClientRxAirtime.setStatus(_A)
_AhClientAssociationTime_Type=Counter32
_AhClientAssociationTime_Object=MibTableColumn
ahClientAssociationTime=_AhClientAssociationTime_Object((1,3,6,1,4,1,26928,1,1,1,2,1,2,1,36),_AhClientAssociationTime_Type())
ahClientAssociationTime.setMaxAccess(_B)
if mibBuilder.loadTexts:ahClientAssociationTime.setStatus(_A)
_AhClientBSSID_Type=AhNodeID
_AhClientBSSID_Object=MibTableColumn
ahClientBSSID=_AhClientBSSID_Object((1,3,6,1,4,1,26928,1,1,1,2,1,2,1,37),_AhClientBSSID_Type())
ahClientBSSID.setMaxAccess(_B)
if mibBuilder.loadTexts:ahClientBSSID.setStatus(_A)
_AhRadioStatsTable_Object=MibTable
ahRadioStatsTable=_AhRadioStatsTable_Object((1,3,6,1,4,1,26928,1,1,1,2,1,3))
if mibBuilder.loadTexts:ahRadioStatsTable.setStatus(_A)
_AhRadioStatsEntry_Object=MibTableRow
ahRadioStatsEntry=_AhRadioStatsEntry_Object((1,3,6,1,4,1,26928,1,1,1,2,1,3,1))
ahRadioStatsEntry.setIndexNames((0,_C,_D))
if mibBuilder.loadTexts:ahRadioStatsEntry.setStatus(_A)
_AhRadioTxDataFrames_Type=Counter32
_AhRadioTxDataFrames_Object=MibTableColumn
ahRadioTxDataFrames=_AhRadioTxDataFrames_Object((1,3,6,1,4,1,26928,1,1,1,2,1,3,1,1),_AhRadioTxDataFrames_Type())
ahRadioTxDataFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:ahRadioTxDataFrames.setStatus(_A)
_AhRadioTxUnicastDataFrames_Type=Counter32
_AhRadioTxUnicastDataFrames_Object=MibTableColumn
ahRadioTxUnicastDataFrames=_AhRadioTxUnicastDataFrames_Object((1,3,6,1,4,1,26928,1,1,1,2,1,3,1,2),_AhRadioTxUnicastDataFrames_Type())
ahRadioTxUnicastDataFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:ahRadioTxUnicastDataFrames.setStatus(_A)
_AhRadioTxMulticastDataFrames_Type=Counter32
_AhRadioTxMulticastDataFrames_Object=MibTableColumn
ahRadioTxMulticastDataFrames=_AhRadioTxMulticastDataFrames_Object((1,3,6,1,4,1,26928,1,1,1,2,1,3,1,3),_AhRadioTxMulticastDataFrames_Type())
ahRadioTxMulticastDataFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:ahRadioTxMulticastDataFrames.setStatus(_A)
_AhRadioTxBroadcastDataFrames_Type=Counter32
_AhRadioTxBroadcastDataFrames_Object=MibTableColumn
ahRadioTxBroadcastDataFrames=_AhRadioTxBroadcastDataFrames_Object((1,3,6,1,4,1,26928,1,1,1,2,1,3,1,4),_AhRadioTxBroadcastDataFrames_Type())
ahRadioTxBroadcastDataFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:ahRadioTxBroadcastDataFrames.setStatus(_A)
_AhRadioTxNonBeaconMgtFrames_Type=Counter32
_AhRadioTxNonBeaconMgtFrames_Object=MibTableColumn
ahRadioTxNonBeaconMgtFrames=_AhRadioTxNonBeaconMgtFrames_Object((1,3,6,1,4,1,26928,1,1,1,2,1,3,1,5),_AhRadioTxNonBeaconMgtFrames_Type())
ahRadioTxNonBeaconMgtFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:ahRadioTxNonBeaconMgtFrames.setStatus(_A)
_AhRadioTxBeaconFrames_Type=Counter32
_AhRadioTxBeaconFrames_Object=MibTableColumn
ahRadioTxBeaconFrames=_AhRadioTxBeaconFrames_Object((1,3,6,1,4,1,26928,1,1,1,2,1,3,1,6),_AhRadioTxBeaconFrames_Type())
ahRadioTxBeaconFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:ahRadioTxBeaconFrames.setStatus(_A)
_AhRadioTxTotalRetries_Type=Counter32
_AhRadioTxTotalRetries_Object=MibTableColumn
ahRadioTxTotalRetries=_AhRadioTxTotalRetries_Object((1,3,6,1,4,1,26928,1,1,1,2,1,3,1,7),_AhRadioTxTotalRetries_Type())
ahRadioTxTotalRetries.setMaxAccess(_B)
if mibBuilder.loadTexts:ahRadioTxTotalRetries.setStatus(_A)
_AhRadioTxTotalFramesDropped_Type=Counter32
_AhRadioTxTotalFramesDropped_Object=MibTableColumn
ahRadioTxTotalFramesDropped=_AhRadioTxTotalFramesDropped_Object((1,3,6,1,4,1,26928,1,1,1,2,1,3,1,8),_AhRadioTxTotalFramesDropped_Type())
ahRadioTxTotalFramesDropped.setMaxAccess(_B)
if mibBuilder.loadTexts:ahRadioTxTotalFramesDropped.setStatus(_A)
_AhRadioTxTotalFrameErrors_Type=Counter32
_AhRadioTxTotalFrameErrors_Object=MibTableColumn
ahRadioTxTotalFrameErrors=_AhRadioTxTotalFrameErrors_Object((1,3,6,1,4,1,26928,1,1,1,2,1,3,1,9),_AhRadioTxTotalFrameErrors_Type())
ahRadioTxTotalFrameErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:ahRadioTxTotalFrameErrors.setStatus(_A)
_AhRadioTxFEForExcessiveHWRetries_Type=Counter32
_AhRadioTxFEForExcessiveHWRetries_Object=MibTableColumn
ahRadioTxFEForExcessiveHWRetries=_AhRadioTxFEForExcessiveHWRetries_Object((1,3,6,1,4,1,26928,1,1,1,2,1,3,1,10),_AhRadioTxFEForExcessiveHWRetries_Type())
ahRadioTxFEForExcessiveHWRetries.setMaxAccess(_B)
if mibBuilder.loadTexts:ahRadioTxFEForExcessiveHWRetries.setStatus(_A)
_AhRadioRxTotalDataFrames_Type=Counter32
_AhRadioRxTotalDataFrames_Object=MibTableColumn
ahRadioRxTotalDataFrames=_AhRadioRxTotalDataFrames_Object((1,3,6,1,4,1,26928,1,1,1,2,1,3,1,11),_AhRadioRxTotalDataFrames_Type())
ahRadioRxTotalDataFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:ahRadioRxTotalDataFrames.setStatus(_A)
_AhRadioRxUnicastDataFrames_Type=Counter32
_AhRadioRxUnicastDataFrames_Object=MibTableColumn
ahRadioRxUnicastDataFrames=_AhRadioRxUnicastDataFrames_Object((1,3,6,1,4,1,26928,1,1,1,2,1,3,1,12),_AhRadioRxUnicastDataFrames_Type())
ahRadioRxUnicastDataFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:ahRadioRxUnicastDataFrames.setStatus(_A)
_AhRadioRxMulticastDataFrames_Type=Counter32
_AhRadioRxMulticastDataFrames_Object=MibTableColumn
ahRadioRxMulticastDataFrames=_AhRadioRxMulticastDataFrames_Object((1,3,6,1,4,1,26928,1,1,1,2,1,3,1,13),_AhRadioRxMulticastDataFrames_Type())
ahRadioRxMulticastDataFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:ahRadioRxMulticastDataFrames.setStatus(_A)
_AhRadioRxBroadcastDataFrames_Type=Counter32
_AhRadioRxBroadcastDataFrames_Object=MibTableColumn
ahRadioRxBroadcastDataFrames=_AhRadioRxBroadcastDataFrames_Object((1,3,6,1,4,1,26928,1,1,1,2,1,3,1,14),_AhRadioRxBroadcastDataFrames_Type())
ahRadioRxBroadcastDataFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:ahRadioRxBroadcastDataFrames.setStatus(_A)
_AhRadioRxMgtFrames_Type=Counter32
_AhRadioRxMgtFrames_Object=MibTableColumn
ahRadioRxMgtFrames=_AhRadioRxMgtFrames_Object((1,3,6,1,4,1,26928,1,1,1,2,1,3,1,15),_AhRadioRxMgtFrames_Type())
ahRadioRxMgtFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:ahRadioRxMgtFrames.setStatus(_A)
_AhRadioRxTotalFrameDropped_Type=Counter32
_AhRadioRxTotalFrameDropped_Object=MibTableColumn
ahRadioRxTotalFrameDropped=_AhRadioRxTotalFrameDropped_Object((1,3,6,1,4,1,26928,1,1,1,2,1,3,1,16),_AhRadioRxTotalFrameDropped_Type())
ahRadioRxTotalFrameDropped.setMaxAccess(_B)
if mibBuilder.loadTexts:ahRadioRxTotalFrameDropped.setStatus(_A)
_AhRadioTxBeDataFrames_Type=Counter32
_AhRadioTxBeDataFrames_Object=MibTableColumn
ahRadioTxBeDataFrames=_AhRadioTxBeDataFrames_Object((1,3,6,1,4,1,26928,1,1,1,2,1,3,1,17),_AhRadioTxBeDataFrames_Type())
ahRadioTxBeDataFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:ahRadioTxBeDataFrames.setStatus(_A)
_AhRadioTxBgDataFrames_Type=Counter32
_AhRadioTxBgDataFrames_Object=MibTableColumn
ahRadioTxBgDataFrames=_AhRadioTxBgDataFrames_Object((1,3,6,1,4,1,26928,1,1,1,2,1,3,1,18),_AhRadioTxBgDataFrames_Type())
ahRadioTxBgDataFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:ahRadioTxBgDataFrames.setStatus(_A)
_AhRadioTxViDataFrames_Type=Counter32
_AhRadioTxViDataFrames_Object=MibTableColumn
ahRadioTxViDataFrames=_AhRadioTxViDataFrames_Object((1,3,6,1,4,1,26928,1,1,1,2,1,3,1,19),_AhRadioTxViDataFrames_Type())
ahRadioTxViDataFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:ahRadioTxViDataFrames.setStatus(_A)
_AhRadioTxVoDataFrames_Type=Counter32
_AhRadioTxVoDataFrames_Object=MibTableColumn
ahRadioTxVoDataFrames=_AhRadioTxVoDataFrames_Object((1,3,6,1,4,1,26928,1,1,1,2,1,3,1,20),_AhRadioTxVoDataFrames_Type())
ahRadioTxVoDataFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:ahRadioTxVoDataFrames.setStatus(_A)
_AhRadioTXRTSFailures_Type=Counter32
_AhRadioTXRTSFailures_Object=MibTableColumn
ahRadioTXRTSFailures=_AhRadioTXRTSFailures_Object((1,3,6,1,4,1,26928,1,1,1,2,1,3,1,21),_AhRadioTXRTSFailures_Type())
ahRadioTXRTSFailures.setMaxAccess(_B)
if mibBuilder.loadTexts:ahRadioTXRTSFailures.setStatus(_A)
_AhRadioTxAirtime_Type=Counter64
_AhRadioTxAirtime_Object=MibTableColumn
ahRadioTxAirtime=_AhRadioTxAirtime_Object((1,3,6,1,4,1,26928,1,1,1,2,1,3,1,22),_AhRadioTxAirtime_Type())
ahRadioTxAirtime.setMaxAccess(_B)
if mibBuilder.loadTexts:ahRadioTxAirtime.setStatus(_A)
_AhRadioRxAirtime_Type=Counter64
_AhRadioRxAirtime_Object=MibTableColumn
ahRadioRxAirtime=_AhRadioRxAirtime_Object((1,3,6,1,4,1,26928,1,1,1,2,1,3,1,23),_AhRadioRxAirtime_Type())
ahRadioRxAirtime.setMaxAccess(_B)
if mibBuilder.loadTexts:ahRadioRxAirtime.setStatus(_A)
_AhVIfStatsTable_Object=MibTable
ahVIfStatsTable=_AhVIfStatsTable_Object((1,3,6,1,4,1,26928,1,1,1,2,1,4))
if mibBuilder.loadTexts:ahVIfStatsTable.setStatus(_A)
_AhVIfStatsEntry_Object=MibTableRow
ahVIfStatsEntry=_AhVIfStatsEntry_Object((1,3,6,1,4,1,26928,1,1,1,2,1,4,1))
ahVIfStatsEntry.setIndexNames((0,_C,_D))
if mibBuilder.loadTexts:ahVIfStatsEntry.setStatus(_A)
_AhVIfRxDataFrames_Type=Counter32
_AhVIfRxDataFrames_Object=MibTableColumn
ahVIfRxDataFrames=_AhVIfRxDataFrames_Object((1,3,6,1,4,1,26928,1,1,1,2,1,4,1,1),_AhVIfRxDataFrames_Type())
ahVIfRxDataFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:ahVIfRxDataFrames.setStatus(_A)
_AhVIfRxUnicastDataFrames_Type=Counter32
_AhVIfRxUnicastDataFrames_Object=MibTableColumn
ahVIfRxUnicastDataFrames=_AhVIfRxUnicastDataFrames_Object((1,3,6,1,4,1,26928,1,1,1,2,1,4,1,2),_AhVIfRxUnicastDataFrames_Type())
ahVIfRxUnicastDataFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:ahVIfRxUnicastDataFrames.setStatus(_A)
_AhVIfRxMulticastDataFrames_Type=Counter32
_AhVIfRxMulticastDataFrames_Object=MibTableColumn
ahVIfRxMulticastDataFrames=_AhVIfRxMulticastDataFrames_Object((1,3,6,1,4,1,26928,1,1,1,2,1,4,1,3),_AhVIfRxMulticastDataFrames_Type())
ahVIfRxMulticastDataFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:ahVIfRxMulticastDataFrames.setStatus(_A)
_AhVIfRxBroadcastDataFrames_Type=Counter32
_AhVIfRxBroadcastDataFrames_Object=MibTableColumn
ahVIfRxBroadcastDataFrames=_AhVIfRxBroadcastDataFrames_Object((1,3,6,1,4,1,26928,1,1,1,2,1,4,1,4),_AhVIfRxBroadcastDataFrames_Type())
ahVIfRxBroadcastDataFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:ahVIfRxBroadcastDataFrames.setStatus(_A)
_AhVIfRxErrorFrames_Type=Counter32
_AhVIfRxErrorFrames_Object=MibTableColumn
ahVIfRxErrorFrames=_AhVIfRxErrorFrames_Object((1,3,6,1,4,1,26928,1,1,1,2,1,4,1,5),_AhVIfRxErrorFrames_Type())
ahVIfRxErrorFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:ahVIfRxErrorFrames.setStatus(_A)
_AhVIfRxDroppedFrames_Type=Counter32
_AhVIfRxDroppedFrames_Object=MibTableColumn
ahVIfRxDroppedFrames=_AhVIfRxDroppedFrames_Object((1,3,6,1,4,1,26928,1,1,1,2,1,4,1,6),_AhVIfRxDroppedFrames_Type())
ahVIfRxDroppedFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:ahVIfRxDroppedFrames.setStatus(_A)
_AhVIfTxDataFrames_Type=Counter32
_AhVIfTxDataFrames_Object=MibTableColumn
ahVIfTxDataFrames=_AhVIfTxDataFrames_Object((1,3,6,1,4,1,26928,1,1,1,2,1,4,1,7),_AhVIfTxDataFrames_Type())
ahVIfTxDataFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:ahVIfTxDataFrames.setStatus(_A)
_AhVIfTxUnicastDataFrames_Type=Counter32
_AhVIfTxUnicastDataFrames_Object=MibTableColumn
ahVIfTxUnicastDataFrames=_AhVIfTxUnicastDataFrames_Object((1,3,6,1,4,1,26928,1,1,1,2,1,4,1,8),_AhVIfTxUnicastDataFrames_Type())
ahVIfTxUnicastDataFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:ahVIfTxUnicastDataFrames.setStatus(_A)
_AhVIfTxMulticastDataFrames_Type=Counter32
_AhVIfTxMulticastDataFrames_Object=MibTableColumn
ahVIfTxMulticastDataFrames=_AhVIfTxMulticastDataFrames_Object((1,3,6,1,4,1,26928,1,1,1,2,1,4,1,9),_AhVIfTxMulticastDataFrames_Type())
ahVIfTxMulticastDataFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:ahVIfTxMulticastDataFrames.setStatus(_A)
_AhVIfTxBroadcastDataFrames_Type=Counter32
_AhVIfTxBroadcastDataFrames_Object=MibTableColumn
ahVIfTxBroadcastDataFrames=_AhVIfTxBroadcastDataFrames_Object((1,3,6,1,4,1,26928,1,1,1,2,1,4,1,10),_AhVIfTxBroadcastDataFrames_Type())
ahVIfTxBroadcastDataFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:ahVIfTxBroadcastDataFrames.setStatus(_A)
_AhVIfTxErrorFrames_Type=Counter32
_AhVIfTxErrorFrames_Object=MibTableColumn
ahVIfTxErrorFrames=_AhVIfTxErrorFrames_Object((1,3,6,1,4,1,26928,1,1,1,2,1,4,1,11),_AhVIfTxErrorFrames_Type())
ahVIfTxErrorFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:ahVIfTxErrorFrames.setStatus(_A)
_AhVIfTxDroppedFrames_Type=Counter32
_AhVIfTxDroppedFrames_Object=MibTableColumn
ahVIfTxDroppedFrames=_AhVIfTxDroppedFrames_Object((1,3,6,1,4,1,26928,1,1,1,2,1,4,1,12),_AhVIfTxDroppedFrames_Type())
ahVIfTxDroppedFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:ahVIfTxDroppedFrames.setStatus(_A)
_AhVIfTxBeDataFrames_Type=Counter32
_AhVIfTxBeDataFrames_Object=MibTableColumn
ahVIfTxBeDataFrames=_AhVIfTxBeDataFrames_Object((1,3,6,1,4,1,26928,1,1,1,2,1,4,1,13),_AhVIfTxBeDataFrames_Type())
ahVIfTxBeDataFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:ahVIfTxBeDataFrames.setStatus(_A)
_AhVIfTxBgDataFrames_Type=Counter32
_AhVIfTxBgDataFrames_Object=MibTableColumn
ahVIfTxBgDataFrames=_AhVIfTxBgDataFrames_Object((1,3,6,1,4,1,26928,1,1,1,2,1,4,1,14),_AhVIfTxBgDataFrames_Type())
ahVIfTxBgDataFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:ahVIfTxBgDataFrames.setStatus(_A)
_AhVIfTxViDataFrames_Type=Counter32
_AhVIfTxViDataFrames_Object=MibTableColumn
ahVIfTxViDataFrames=_AhVIfTxViDataFrames_Object((1,3,6,1,4,1,26928,1,1,1,2,1,4,1,15),_AhVIfTxViDataFrames_Type())
ahVIfTxViDataFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:ahVIfTxViDataFrames.setStatus(_A)
_AhVIfTxVoDataFrames_Type=Counter32
_AhVIfTxVoDataFrames_Object=MibTableColumn
ahVIfTxVoDataFrames=_AhVIfTxVoDataFrames_Object((1,3,6,1,4,1,26928,1,1,1,2,1,4,1,16),_AhVIfTxVoDataFrames_Type())
ahVIfTxVoDataFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:ahVIfTxVoDataFrames.setStatus(_A)
_AhVifTxAirtime_Type=Counter64
_AhVifTxAirtime_Object=MibTableColumn
ahVifTxAirtime=_AhVifTxAirtime_Object((1,3,6,1,4,1,26928,1,1,1,2,1,4,1,17),_AhVifTxAirtime_Type())
ahVifTxAirtime.setMaxAccess(_B)
if mibBuilder.loadTexts:ahVifTxAirtime.setStatus(_A)
_AhVifRxAirtime_Type=Counter64
_AhVifRxAirtime_Object=MibTableColumn
ahVifRxAirtime=_AhVifRxAirtime_Object((1,3,6,1,4,1,26928,1,1,1,2,1,4,1,18),_AhVifRxAirtime_Type())
ahVifRxAirtime.setMaxAccess(_B)
if mibBuilder.loadTexts:ahVifRxAirtime.setStatus(_A)
_AhRadioAttributeTable_Object=MibTable
ahRadioAttributeTable=_AhRadioAttributeTable_Object((1,3,6,1,4,1,26928,1,1,1,2,1,5))
if mibBuilder.loadTexts:ahRadioAttributeTable.setStatus(_A)
_AhRadioAttributeEntry_Object=MibTableRow
ahRadioAttributeEntry=_AhRadioAttributeEntry_Object((1,3,6,1,4,1,26928,1,1,1,2,1,5,1))
ahRadioAttributeEntry.setIndexNames((0,_C,_D))
if mibBuilder.loadTexts:ahRadioAttributeEntry.setStatus(_A)
_AhRadioChannel_Type=Integer32
_AhRadioChannel_Object=MibTableColumn
ahRadioChannel=_AhRadioChannel_Object((1,3,6,1,4,1,26928,1,1,1,2,1,5,1,1),_AhRadioChannel_Type())
ahRadioChannel.setMaxAccess(_B)
if mibBuilder.loadTexts:ahRadioChannel.setStatus(_A)
_AhRadioTxPower_Type=Integer32
_AhRadioTxPower_Object=MibTableColumn
ahRadioTxPower=_AhRadioTxPower_Object((1,3,6,1,4,1,26928,1,1,1,2,1,5,1,2),_AhRadioTxPower_Type())
ahRadioTxPower.setMaxAccess(_B)
if mibBuilder.loadTexts:ahRadioTxPower.setStatus(_A)
_AhRadioNoiseFloor_Type=Integer32
_AhRadioNoiseFloor_Object=MibTableColumn
ahRadioNoiseFloor=_AhRadioNoiseFloor_Object((1,3,6,1,4,1,26928,1,1,1,2,1,5,1,3),_AhRadioNoiseFloor_Type())
ahRadioNoiseFloor.setMaxAccess(_B)
if mibBuilder.loadTexts:ahRadioNoiseFloor.setStatus(_A)
ifEntry.registerAugmentions((_E,_G))
ahXIfEntry.setIndexNames(*ifEntry.getIndexNames())
mibBuilder.exportSymbols(_E,**{'AhAuthenticationMethod':AhAuthenticationMethod,'AhEncrytionMethod':AhEncrytionMethod,'ahInterface':ahInterface,'ahXIfTable':ahXIfTable,_G:ahXIfEntry,'ahIfName':ahIfName,'ahSSIDName':ahSSIDName,'ahIfPromiscuous':ahIfPromiscuous,'ahIfType':ahIfType,'ahIfMode':ahIfMode,'ahIfConfMode':ahIfConfMode,'ahAssociationTable':ahAssociationTable,'ahAssociationEntry':ahAssociationEntry,_F:ahClientMac,'ahClientIP':ahClientIP,'ahClientHostname':ahClientHostname,'ahClientRSSI':ahClientRSSI,'ahClientLinkUptime':ahClientLinkUptime,'ahClientCWPUsed':ahClientCWPUsed,'ahClientAuthMethod':ahClientAuthMethod,'ahClientEncryptionMethod':ahClientEncryptionMethod,'ahClientMACProtocol':ahClientMACProtocol,'ahClientSSID':ahClientSSID,'ahClientVLAN':ahClientVLAN,'ahClientUserProfId':ahClientUserProfId,'ahClientChannel':ahClientChannel,'ahClientLastTxRate':ahClientLastTxRate,'ahClientUsername':ahClientUsername,'ahClientRxDataFrames':ahClientRxDataFrames,'ahClientRxDataOctets':ahClientRxDataOctets,'ahClientRxMgtFrames':ahClientRxMgtFrames,'ahClientRxUnicastFrames':ahClientRxUnicastFrames,'ahClientRxMulticastFrames':ahClientRxMulticastFrames,'ahClientRxBroadcastFrames':ahClientRxBroadcastFrames,'ahClientRxMICFailures':ahClientRxMICFailures,'ahClientTxDataFrames':ahClientTxDataFrames,'ahClientTxMgtFrames':ahClientTxMgtFrames,'ahClientTxDataOctets':ahClientTxDataOctets,'ahClientTxUnicastFrames':ahClientTxUnicastFrames,'ahClientTxMulticastFrames':ahClientTxMulticastFrames,'ahClientTxBroadcastFrames':ahClientTxBroadcastFrames,'ahClientLastRxRate':ahClientLastRxRate,'ahClientTxBeDataFrames':ahClientTxBeDataFrames,'ahClientTxBgDataFrames':ahClientTxBgDataFrames,'ahClientTxViDataFrames':ahClientTxViDataFrames,'ahClientTxVoDataFrames':ahClientTxVoDataFrames,'ahClientTxAirtime':ahClientTxAirtime,'ahClientRxAirtime':ahClientRxAirtime,'ahClientAssociationTime':ahClientAssociationTime,'ahClientBSSID':ahClientBSSID,'ahRadioStatsTable':ahRadioStatsTable,'ahRadioStatsEntry':ahRadioStatsEntry,'ahRadioTxDataFrames':ahRadioTxDataFrames,'ahRadioTxUnicastDataFrames':ahRadioTxUnicastDataFrames,'ahRadioTxMulticastDataFrames':ahRadioTxMulticastDataFrames,'ahRadioTxBroadcastDataFrames':ahRadioTxBroadcastDataFrames,'ahRadioTxNonBeaconMgtFrames':ahRadioTxNonBeaconMgtFrames,'ahRadioTxBeaconFrames':ahRadioTxBeaconFrames,'ahRadioTxTotalRetries':ahRadioTxTotalRetries,'ahRadioTxTotalFramesDropped':ahRadioTxTotalFramesDropped,'ahRadioTxTotalFrameErrors':ahRadioTxTotalFrameErrors,'ahRadioTxFEForExcessiveHWRetries':ahRadioTxFEForExcessiveHWRetries,'ahRadioRxTotalDataFrames':ahRadioRxTotalDataFrames,'ahRadioRxUnicastDataFrames':ahRadioRxUnicastDataFrames,'ahRadioRxMulticastDataFrames':ahRadioRxMulticastDataFrames,'ahRadioRxBroadcastDataFrames':ahRadioRxBroadcastDataFrames,'ahRadioRxMgtFrames':ahRadioRxMgtFrames,'ahRadioRxTotalFrameDropped':ahRadioRxTotalFrameDropped,'ahRadioTxBeDataFrames':ahRadioTxBeDataFrames,'ahRadioTxBgDataFrames':ahRadioTxBgDataFrames,'ahRadioTxViDataFrames':ahRadioTxViDataFrames,'ahRadioTxVoDataFrames':ahRadioTxVoDataFrames,'ahRadioTXRTSFailures':ahRadioTXRTSFailures,'ahRadioTxAirtime':ahRadioTxAirtime,'ahRadioRxAirtime':ahRadioRxAirtime,'ahVIfStatsTable':ahVIfStatsTable,'ahVIfStatsEntry':ahVIfStatsEntry,'ahVIfRxDataFrames':ahVIfRxDataFrames,'ahVIfRxUnicastDataFrames':ahVIfRxUnicastDataFrames,'ahVIfRxMulticastDataFrames':ahVIfRxMulticastDataFrames,'ahVIfRxBroadcastDataFrames':ahVIfRxBroadcastDataFrames,'ahVIfRxErrorFrames':ahVIfRxErrorFrames,'ahVIfRxDroppedFrames':ahVIfRxDroppedFrames,'ahVIfTxDataFrames':ahVIfTxDataFrames,'ahVIfTxUnicastDataFrames':ahVIfTxUnicastDataFrames,'ahVIfTxMulticastDataFrames':ahVIfTxMulticastDataFrames,'ahVIfTxBroadcastDataFrames':ahVIfTxBroadcastDataFrames,'ahVIfTxErrorFrames':ahVIfTxErrorFrames,'ahVIfTxDroppedFrames':ahVIfTxDroppedFrames,'ahVIfTxBeDataFrames':ahVIfTxBeDataFrames,'ahVIfTxBgDataFrames':ahVIfTxBgDataFrames,'ahVIfTxViDataFrames':ahVIfTxViDataFrames,'ahVIfTxVoDataFrames':ahVIfTxVoDataFrames,'ahVifTxAirtime':ahVifTxAirtime,'ahVifRxAirtime':ahVifRxAirtime,'ahRadioAttributeTable':ahRadioAttributeTable,'ahRadioAttributeEntry':ahRadioAttributeEntry,'ahRadioChannel':ahRadioChannel,'ahRadioTxPower':ahRadioTxPower,'ahRadioNoiseFloor':ahRadioNoiseFloor})