_F='gwnClientMACAddress'
_E='gwnWlanIndex'
_D='gwnRadioIndex'
_C='GRANDSTREAM-GWN-MIB'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,MacAddress,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress','TextualConvention')
gwnMIB=ModuleIdentity((1,3,6,1,4,1,42397,1,1))
_Grandstream_ObjectIdentity=ObjectIdentity
grandstream=_Grandstream_ObjectIdentity((1,3,6,1,4,1,42397))
_Gwn_ObjectIdentity=ObjectIdentity
gwn=_Gwn_ObjectIdentity((1,3,6,1,4,1,42397,1))
_GwnApSystemInfo_ObjectIdentity=ObjectIdentity
gwnApSystemInfo=_GwnApSystemInfo_ObjectIdentity((1,3,6,1,4,1,42397,1,1,2))
_GwnDeviceModel_Type=DisplayString
_GwnDeviceModel_Object=MibScalar
gwnDeviceModel=_GwnDeviceModel_Object((1,3,6,1,4,1,42397,1,1,2,1),_GwnDeviceModel_Type())
gwnDeviceModel.setMaxAccess(_B)
if mibBuilder.loadTexts:gwnDeviceModel.setStatus(_A)
_GwnDeviceName_Type=DisplayString
_GwnDeviceName_Object=MibScalar
gwnDeviceName=_GwnDeviceName_Object((1,3,6,1,4,1,42397,1,1,2,2),_GwnDeviceName_Type())
gwnDeviceName.setMaxAccess(_B)
if mibBuilder.loadTexts:gwnDeviceName.setStatus(_A)
_GwnDeviceMac_Type=MacAddress
_GwnDeviceMac_Object=MibScalar
gwnDeviceMac=_GwnDeviceMac_Object((1,3,6,1,4,1,42397,1,1,2,3),_GwnDeviceMac_Type())
gwnDeviceMac.setMaxAccess(_B)
if mibBuilder.loadTexts:gwnDeviceMac.setStatus(_A)
_GwnDeviceVersion_Type=DisplayString
_GwnDeviceVersion_Object=MibScalar
gwnDeviceVersion=_GwnDeviceVersion_Object((1,3,6,1,4,1,42397,1,1,2,4),_GwnDeviceVersion_Type())
gwnDeviceVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:gwnDeviceVersion.setStatus(_A)
_GwnDeviceIPAddress_Type=IpAddress
_GwnDeviceIPAddress_Object=MibScalar
gwnDeviceIPAddress=_GwnDeviceIPAddress_Object((1,3,6,1,4,1,42397,1,1,2,5),_GwnDeviceIPAddress_Type())
gwnDeviceIPAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:gwnDeviceIPAddress.setStatus(_A)
_GwnDeviceUptime_Type=Counter32
_GwnDeviceUptime_Object=MibScalar
gwnDeviceUptime=_GwnDeviceUptime_Object((1,3,6,1,4,1,42397,1,1,2,6),_GwnDeviceUptime_Type())
gwnDeviceUptime.setMaxAccess(_B)
if mibBuilder.loadTexts:gwnDeviceUptime.setStatus(_A)
_GwnApWireless_ObjectIdentity=ObjectIdentity
gwnApWireless=_GwnApWireless_ObjectIdentity((1,3,6,1,4,1,42397,1,1,3))
_GwnRadioTable_Object=MibTable
gwnRadioTable=_GwnRadioTable_Object((1,3,6,1,4,1,42397,1,1,3,1))
if mibBuilder.loadTexts:gwnRadioTable.setStatus(_A)
_GwnRadioEntry_Object=MibTableRow
gwnRadioEntry=_GwnRadioEntry_Object((1,3,6,1,4,1,42397,1,1,3,1,1))
gwnRadioEntry.setIndexNames((0,_C,_D))
if mibBuilder.loadTexts:gwnRadioEntry.setStatus(_A)
_GwnRadioIndex_Type=Integer32
_GwnRadioIndex_Object=MibTableColumn
gwnRadioIndex=_GwnRadioIndex_Object((1,3,6,1,4,1,42397,1,1,3,1,1,1),_GwnRadioIndex_Type())
gwnRadioIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:gwnRadioIndex.setStatus(_A)
_GwnRadioName_Type=DisplayString
_GwnRadioName_Object=MibTableColumn
gwnRadioName=_GwnRadioName_Object((1,3,6,1,4,1,42397,1,1,3,1,1,2),_GwnRadioName_Type())
gwnRadioName.setMaxAccess(_B)
if mibBuilder.loadTexts:gwnRadioName.setStatus(_A)
_GwnRadioStatus_Type=Integer32
_GwnRadioStatus_Object=MibTableColumn
gwnRadioStatus=_GwnRadioStatus_Object((1,3,6,1,4,1,42397,1,1,3,1,1,3),_GwnRadioStatus_Type())
gwnRadioStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:gwnRadioStatus.setStatus(_A)
_GwnRadioChannel_Type=Integer32
_GwnRadioChannel_Object=MibTableColumn
gwnRadioChannel=_GwnRadioChannel_Object((1,3,6,1,4,1,42397,1,1,3,1,1,4),_GwnRadioChannel_Type())
gwnRadioChannel.setMaxAccess(_B)
if mibBuilder.loadTexts:gwnRadioChannel.setStatus(_A)
_GwnRadioTransmitPower_Type=Integer32
_GwnRadioTransmitPower_Object=MibTableColumn
gwnRadioTransmitPower=_GwnRadioTransmitPower_Object((1,3,6,1,4,1,42397,1,1,3,1,1,5),_GwnRadioTransmitPower_Type())
gwnRadioTransmitPower.setMaxAccess(_B)
if mibBuilder.loadTexts:gwnRadioTransmitPower.setStatus(_A)
_GwnRadioTxTotalFrames_Type=Counter32
_GwnRadioTxTotalFrames_Object=MibTableColumn
gwnRadioTxTotalFrames=_GwnRadioTxTotalFrames_Object((1,3,6,1,4,1,42397,1,1,3,1,1,6),_GwnRadioTxTotalFrames_Type())
gwnRadioTxTotalFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:gwnRadioTxTotalFrames.setStatus(_A)
_GwnRadioTxMgmtFrames_Type=Counter32
_GwnRadioTxMgmtFrames_Object=MibTableColumn
gwnRadioTxMgmtFrames=_GwnRadioTxMgmtFrames_Object((1,3,6,1,4,1,42397,1,1,3,1,1,7),_GwnRadioTxMgmtFrames_Type())
gwnRadioTxMgmtFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:gwnRadioTxMgmtFrames.setStatus(_A)
_GwnRadioTxDataFrames_Type=Counter32
_GwnRadioTxDataFrames_Object=MibTableColumn
gwnRadioTxDataFrames=_GwnRadioTxDataFrames_Object((1,3,6,1,4,1,42397,1,1,3,1,1,8),_GwnRadioTxDataFrames_Type())
gwnRadioTxDataFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:gwnRadioTxDataFrames.setStatus(_A)
_GwnRadioTxDataBytes_Type=Counter32
_GwnRadioTxDataBytes_Object=MibTableColumn
gwnRadioTxDataBytes=_GwnRadioTxDataBytes_Object((1,3,6,1,4,1,42397,1,1,3,1,1,9),_GwnRadioTxDataBytes_Type())
gwnRadioTxDataBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:gwnRadioTxDataBytes.setStatus(_A)
_GwnRadioTxDrops_Type=Counter32
_GwnRadioTxDrops_Object=MibTableColumn
gwnRadioTxDrops=_GwnRadioTxDrops_Object((1,3,6,1,4,1,42397,1,1,3,1,1,10),_GwnRadioTxDrops_Type())
gwnRadioTxDrops.setMaxAccess(_B)
if mibBuilder.loadTexts:gwnRadioTxDrops.setStatus(_A)
_GwnRadioRxTotalFrames_Type=Counter32
_GwnRadioRxTotalFrames_Object=MibTableColumn
gwnRadioRxTotalFrames=_GwnRadioRxTotalFrames_Object((1,3,6,1,4,1,42397,1,1,3,1,1,11),_GwnRadioRxTotalFrames_Type())
gwnRadioRxTotalFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:gwnRadioRxTotalFrames.setStatus(_A)
_GwnRadioRxDataFrames_Type=Counter32
_GwnRadioRxDataFrames_Object=MibTableColumn
gwnRadioRxDataFrames=_GwnRadioRxDataFrames_Object((1,3,6,1,4,1,42397,1,1,3,1,1,12),_GwnRadioRxDataFrames_Type())
gwnRadioRxDataFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:gwnRadioRxDataFrames.setStatus(_A)
_GwnRadioRxDataBytes_Type=Counter32
_GwnRadioRxDataBytes_Object=MibTableColumn
gwnRadioRxDataBytes=_GwnRadioRxDataBytes_Object((1,3,6,1,4,1,42397,1,1,3,1,1,13),_GwnRadioRxDataBytes_Type())
gwnRadioRxDataBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:gwnRadioRxDataBytes.setStatus(_A)
_GwnRadioRxMgmtFrames_Type=Counter32
_GwnRadioRxMgmtFrames_Object=MibTableColumn
gwnRadioRxMgmtFrames=_GwnRadioRxMgmtFrames_Object((1,3,6,1,4,1,42397,1,1,3,1,1,14),_GwnRadioRxMgmtFrames_Type())
gwnRadioRxMgmtFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:gwnRadioRxMgmtFrames.setStatus(_A)
_GwnRadioRxBad_Type=Counter32
_GwnRadioRxBad_Object=MibTableColumn
gwnRadioRxBad=_GwnRadioRxBad_Object((1,3,6,1,4,1,42397,1,1,3,1,1,15),_GwnRadioRxBad_Type())
gwnRadioRxBad.setMaxAccess(_B)
if mibBuilder.loadTexts:gwnRadioRxBad.setStatus(_A)
_GwnWlanTable_Object=MibTable
gwnWlanTable=_GwnWlanTable_Object((1,3,6,1,4,1,42397,1,1,3,2))
if mibBuilder.loadTexts:gwnWlanTable.setStatus(_A)
_GwnWlanEntry_Object=MibTableRow
gwnWlanEntry=_GwnWlanEntry_Object((1,3,6,1,4,1,42397,1,1,3,2,1))
gwnWlanEntry.setIndexNames((0,_C,_E))
if mibBuilder.loadTexts:gwnWlanEntry.setStatus(_A)
_GwnWlanIndex_Type=Integer32
_GwnWlanIndex_Object=MibTableColumn
gwnWlanIndex=_GwnWlanIndex_Object((1,3,6,1,4,1,42397,1,1,3,2,1,1),_GwnWlanIndex_Type())
gwnWlanIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:gwnWlanIndex.setStatus(_A)
_GwnWlanESSID_Type=DisplayString
_GwnWlanESSID_Object=MibTableColumn
gwnWlanESSID=_GwnWlanESSID_Object((1,3,6,1,4,1,42397,1,1,3,2,1,2),_GwnWlanESSID_Type())
gwnWlanESSID.setMaxAccess(_B)
if mibBuilder.loadTexts:gwnWlanESSID.setStatus(_A)
_GwnWlanBSSID_Type=MacAddress
_GwnWlanBSSID_Object=MibTableColumn
gwnWlanBSSID=_GwnWlanBSSID_Object((1,3,6,1,4,1,42397,1,1,3,2,1,3),_GwnWlanBSSID_Type())
gwnWlanBSSID.setMaxAccess(_B)
if mibBuilder.loadTexts:gwnWlanBSSID.setStatus(_A)
_GwnWlanTxTotalFrames_Type=Counter32
_GwnWlanTxTotalFrames_Object=MibTableColumn
gwnWlanTxTotalFrames=_GwnWlanTxTotalFrames_Object((1,3,6,1,4,1,42397,1,1,3,2,1,4),_GwnWlanTxTotalFrames_Type())
gwnWlanTxTotalFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:gwnWlanTxTotalFrames.setStatus(_A)
_GwnWlanTxDataFrames_Type=Counter32
_GwnWlanTxDataFrames_Object=MibTableColumn
gwnWlanTxDataFrames=_GwnWlanTxDataFrames_Object((1,3,6,1,4,1,42397,1,1,3,2,1,5),_GwnWlanTxDataFrames_Type())
gwnWlanTxDataFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:gwnWlanTxDataFrames.setStatus(_A)
_GwnWlanTxDataBytes_Type=Counter32
_GwnWlanTxDataBytes_Object=MibTableColumn
gwnWlanTxDataBytes=_GwnWlanTxDataBytes_Object((1,3,6,1,4,1,42397,1,1,3,2,1,6),_GwnWlanTxDataBytes_Type())
gwnWlanTxDataBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:gwnWlanTxDataBytes.setStatus(_A)
_GwnWlanRxTotalFrames_Type=Counter32
_GwnWlanRxTotalFrames_Object=MibTableColumn
gwnWlanRxTotalFrames=_GwnWlanRxTotalFrames_Object((1,3,6,1,4,1,42397,1,1,3,2,1,7),_GwnWlanRxTotalFrames_Type())
gwnWlanRxTotalFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:gwnWlanRxTotalFrames.setStatus(_A)
_GwnWlanRxDataFrames_Type=Counter32
_GwnWlanRxDataFrames_Object=MibTableColumn
gwnWlanRxDataFrames=_GwnWlanRxDataFrames_Object((1,3,6,1,4,1,42397,1,1,3,2,1,8),_GwnWlanRxDataFrames_Type())
gwnWlanRxDataFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:gwnWlanRxDataFrames.setStatus(_A)
_GwnWlanRxDataBytes_Type=Counter32
_GwnWlanRxDataBytes_Object=MibTableColumn
gwnWlanRxDataBytes=_GwnWlanRxDataBytes_Object((1,3,6,1,4,1,42397,1,1,3,2,1,9),_GwnWlanRxDataBytes_Type())
gwnWlanRxDataBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:gwnWlanRxDataBytes.setStatus(_A)
_GwnClientTable_Object=MibTable
gwnClientTable=_GwnClientTable_Object((1,3,6,1,4,1,42397,1,1,3,3))
if mibBuilder.loadTexts:gwnClientTable.setStatus(_A)
_GwnClientEntry_Object=MibTableRow
gwnClientEntry=_GwnClientEntry_Object((1,3,6,1,4,1,42397,1,1,3,3,1))
gwnClientEntry.setIndexNames((0,_C,_F))
if mibBuilder.loadTexts:gwnClientEntry.setStatus(_A)
_GwnClientMACAddress_Type=MacAddress
_GwnClientMACAddress_Object=MibTableColumn
gwnClientMACAddress=_GwnClientMACAddress_Object((1,3,6,1,4,1,42397,1,1,3,3,1,1),_GwnClientMACAddress_Type())
gwnClientMACAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:gwnClientMACAddress.setStatus(_A)
_GwnClienttIPAddress_Type=IpAddress
_GwnClienttIPAddress_Object=MibTableColumn
gwnClienttIPAddress=_GwnClienttIPAddress_Object((1,3,6,1,4,1,42397,1,1,3,3,1,2),_GwnClienttIPAddress_Type())
gwnClienttIPAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:gwnClienttIPAddress.setStatus(_A)
_GwnClientWlanMACAddress_Type=MacAddress
_GwnClientWlanMACAddress_Object=MibTableColumn
gwnClientWlanMACAddress=_GwnClientWlanMACAddress_Object((1,3,6,1,4,1,42397,1,1,3,3,1,3),_GwnClientWlanMACAddress_Type())
gwnClientWlanMACAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:gwnClientWlanMACAddress.setStatus(_A)
_GwnClientESSID_Type=DisplayString
_GwnClientESSID_Object=MibTableColumn
gwnClientESSID=_GwnClientESSID_Object((1,3,6,1,4,1,42397,1,1,3,3,1,4),_GwnClientESSID_Type())
gwnClientESSID.setMaxAccess(_B)
if mibBuilder.loadTexts:gwnClientESSID.setStatus(_A)
_GwnClientRSSI_Type=Integer32
_GwnClientRSSI_Object=MibTableColumn
gwnClientRSSI=_GwnClientRSSI_Object((1,3,6,1,4,1,42397,1,1,3,3,1,5),_GwnClientRSSI_Type())
gwnClientRSSI.setMaxAccess(_B)
if mibBuilder.loadTexts:gwnClientRSSI.setStatus(_A)
_GwnClientAssoctime_Type=TimeTicks
_GwnClientAssoctime_Object=MibTableColumn
gwnClientAssoctime=_GwnClientAssoctime_Object((1,3,6,1,4,1,42397,1,1,3,3,1,6),_GwnClientAssoctime_Type())
gwnClientAssoctime.setMaxAccess(_B)
if mibBuilder.loadTexts:gwnClientAssoctime.setStatus(_A)
_GwnClientManufacture_Type=DisplayString
_GwnClientManufacture_Object=MibTableColumn
gwnClientManufacture=_GwnClientManufacture_Object((1,3,6,1,4,1,42397,1,1,3,3,1,7),_GwnClientManufacture_Type())
gwnClientManufacture.setMaxAccess(_B)
if mibBuilder.loadTexts:gwnClientManufacture.setStatus(_A)
_GwnClientHostname_Type=DisplayString
_GwnClientHostname_Object=MibTableColumn
gwnClientHostname=_GwnClientHostname_Object((1,3,6,1,4,1,42397,1,1,3,3,1,8),_GwnClientHostname_Type())
gwnClientHostname.setMaxAccess(_B)
if mibBuilder.loadTexts:gwnClientHostname.setStatus(_A)
_GwnClientOS_Type=DisplayString
_GwnClientOS_Object=MibTableColumn
gwnClientOS=_GwnClientOS_Object((1,3,6,1,4,1,42397,1,1,3,3,1,9),_GwnClientOS_Type())
gwnClientOS.setMaxAccess(_B)
if mibBuilder.loadTexts:gwnClientOS.setStatus(_A)
_GwnClientTxRate_Type=Integer32
_GwnClientTxRate_Object=MibTableColumn
gwnClientTxRate=_GwnClientTxRate_Object((1,3,6,1,4,1,42397,1,1,3,3,1,10),_GwnClientTxRate_Type())
gwnClientTxRate.setMaxAccess(_B)
if mibBuilder.loadTexts:gwnClientTxRate.setStatus(_A)
_GwnClientTxDataFrames_Type=Counter32
_GwnClientTxDataFrames_Object=MibTableColumn
gwnClientTxDataFrames=_GwnClientTxDataFrames_Object((1,3,6,1,4,1,42397,1,1,3,3,1,11),_GwnClientTxDataFrames_Type())
gwnClientTxDataFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:gwnClientTxDataFrames.setStatus(_A)
_GwnClientTxDataBytes_Type=Counter32
_GwnClientTxDataBytes_Object=MibTableColumn
gwnClientTxDataBytes=_GwnClientTxDataBytes_Object((1,3,6,1,4,1,42397,1,1,3,3,1,12),_GwnClientTxDataBytes_Type())
gwnClientTxDataBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:gwnClientTxDataBytes.setStatus(_A)
_GwnClientRxRate_Type=Integer32
_GwnClientRxRate_Object=MibTableColumn
gwnClientRxRate=_GwnClientRxRate_Object((1,3,6,1,4,1,42397,1,1,3,3,1,13),_GwnClientRxRate_Type())
gwnClientRxRate.setMaxAccess(_B)
if mibBuilder.loadTexts:gwnClientRxRate.setStatus(_A)
_GwnClientRxDataFrames_Type=Counter32
_GwnClientRxDataFrames_Object=MibTableColumn
gwnClientRxDataFrames=_GwnClientRxDataFrames_Object((1,3,6,1,4,1,42397,1,1,3,3,1,14),_GwnClientRxDataFrames_Type())
gwnClientRxDataFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:gwnClientRxDataFrames.setStatus(_A)
_GwnClientRxDataBytes_Type=Counter32
_GwnClientRxDataBytes_Object=MibTableColumn
gwnClientRxDataBytes=_GwnClientRxDataBytes_Object((1,3,6,1,4,1,42397,1,1,3,3,1,15),_GwnClientRxDataBytes_Type())
gwnClientRxDataBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:gwnClientRxDataBytes.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'grandstream':grandstream,'gwn':gwn,'gwnMIB':gwnMIB,'gwnApSystemInfo':gwnApSystemInfo,'gwnDeviceModel':gwnDeviceModel,'gwnDeviceName':gwnDeviceName,'gwnDeviceMac':gwnDeviceMac,'gwnDeviceVersion':gwnDeviceVersion,'gwnDeviceIPAddress':gwnDeviceIPAddress,'gwnDeviceUptime':gwnDeviceUptime,'gwnApWireless':gwnApWireless,'gwnRadioTable':gwnRadioTable,'gwnRadioEntry':gwnRadioEntry,_D:gwnRadioIndex,'gwnRadioName':gwnRadioName,'gwnRadioStatus':gwnRadioStatus,'gwnRadioChannel':gwnRadioChannel,'gwnRadioTransmitPower':gwnRadioTransmitPower,'gwnRadioTxTotalFrames':gwnRadioTxTotalFrames,'gwnRadioTxMgmtFrames':gwnRadioTxMgmtFrames,'gwnRadioTxDataFrames':gwnRadioTxDataFrames,'gwnRadioTxDataBytes':gwnRadioTxDataBytes,'gwnRadioTxDrops':gwnRadioTxDrops,'gwnRadioRxTotalFrames':gwnRadioRxTotalFrames,'gwnRadioRxDataFrames':gwnRadioRxDataFrames,'gwnRadioRxDataBytes':gwnRadioRxDataBytes,'gwnRadioRxMgmtFrames':gwnRadioRxMgmtFrames,'gwnRadioRxBad':gwnRadioRxBad,'gwnWlanTable':gwnWlanTable,'gwnWlanEntry':gwnWlanEntry,_E:gwnWlanIndex,'gwnWlanESSID':gwnWlanESSID,'gwnWlanBSSID':gwnWlanBSSID,'gwnWlanTxTotalFrames':gwnWlanTxTotalFrames,'gwnWlanTxDataFrames':gwnWlanTxDataFrames,'gwnWlanTxDataBytes':gwnWlanTxDataBytes,'gwnWlanRxTotalFrames':gwnWlanRxTotalFrames,'gwnWlanRxDataFrames':gwnWlanRxDataFrames,'gwnWlanRxDataBytes':gwnWlanRxDataBytes,'gwnClientTable':gwnClientTable,'gwnClientEntry':gwnClientEntry,_F:gwnClientMACAddress,'gwnClienttIPAddress':gwnClienttIPAddress,'gwnClientWlanMACAddress':gwnClientWlanMACAddress,'gwnClientESSID':gwnClientESSID,'gwnClientRSSI':gwnClientRSSI,'gwnClientAssoctime':gwnClientAssoctime,'gwnClientManufacture':gwnClientManufacture,'gwnClientHostname':gwnClientHostname,'gwnClientOS':gwnClientOS,'gwnClientTxRate':gwnClientTxRate,'gwnClientTxDataFrames':gwnClientTxDataFrames,'gwnClientTxDataBytes':gwnClientTxDataBytes,'gwnClientRxRate':gwnClientRxRate,'gwnClientRxDataFrames':gwnClientRxDataFrames,'gwnClientRxDataBytes':gwnClientRxDataBytes})