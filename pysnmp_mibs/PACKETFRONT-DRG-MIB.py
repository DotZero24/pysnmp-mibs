_X='productFunctionIdentity'
_W='productOpDefRev'
_V='productHardwareRev'
_U='productSwImageRev'
_T='vlanStaticIndex'
_S='vlanTpFdbAddress'
_R='not-accessible'
_Q='snmpTrapDestName'
_P='snmpTrapDestIndex'
_O='hostIfIndex'
_N='always'
_M='running'
_L='downloadResultCode'
_K='vlanFdbId'
_J='silent'
_I='productIdentity'
_H='productMacAddress'
_G='read-create'
_F='PACKETFRONT-DRG-MIB'
_E='OctetString'
_D='read-only'
_C='Integer32'
_B='read-write'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_E,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
pfMgmt,=mibBuilder.importSymbols('PACKETFRONT-SMI','pfMgmt')
PortList,=mibBuilder.importSymbols('PACKETFRONT-TC','PortList')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress','RowStatus','TextualConvention')
pfDrgMib=ModuleIdentity((1,3,6,1,4,1,9303,4,3))
if mibBuilder.loadTexts:pfDrgMib.setRevisions(('2009-03-23 15:38','2008-04-11 00:00'))
_DrgNotification_ObjectIdentity=ObjectIdentity
drgNotification=_DrgNotification_ObjectIdentity((1,3,6,1,4,1,9303,4,3,0))
_DrgConfig_ObjectIdentity=ObjectIdentity
drgConfig=_DrgConfig_ObjectIdentity((1,3,6,1,4,1,9303,4,3,1))
_ProductInfo_ObjectIdentity=ObjectIdentity
productInfo=_ProductInfo_ObjectIdentity((1,3,6,1,4,1,9303,4,3,1,1))
class _ProductName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_ProductName_Type.__name__=_E
_ProductName_Object=MibScalar
productName=_ProductName_Object((1,3,6,1,4,1,9303,4,3,1,1,1),_ProductName_Type())
productName.setMaxAccess(_D)
if mibBuilder.loadTexts:productName.setStatus(_A)
class _ProductSerialNo_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,10))
_ProductSerialNo_Type.__name__=_E
_ProductSerialNo_Object=MibScalar
productSerialNo=_ProductSerialNo_Object((1,3,6,1,4,1,9303,4,3,1,1,2),_ProductSerialNo_Type())
productSerialNo.setMaxAccess(_D)
if mibBuilder.loadTexts:productSerialNo.setStatus(_A)
class _ProductProductionWeek_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,8))
_ProductProductionWeek_Type.__name__=_E
_ProductProductionWeek_Object=MibScalar
productProductionWeek=_ProductProductionWeek_Object((1,3,6,1,4,1,9303,4,3,1,1,3),_ProductProductionWeek_Type())
productProductionWeek.setMaxAccess(_D)
if mibBuilder.loadTexts:productProductionWeek.setStatus(_A)
class _ProductSwImageRev_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_ProductSwImageRev_Type.__name__=_E
_ProductSwImageRev_Object=MibScalar
productSwImageRev=_ProductSwImageRev_Object((1,3,6,1,4,1,9303,4,3,1,1,4),_ProductSwImageRev_Type())
productSwImageRev.setMaxAccess(_D)
if mibBuilder.loadTexts:productSwImageRev.setStatus(_A)
class _ProductFwImageRev_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_ProductFwImageRev_Type.__name__=_E
_ProductFwImageRev_Object=MibScalar
productFwImageRev=_ProductFwImageRev_Object((1,3,6,1,4,1,9303,4,3,1,1,5),_ProductFwImageRev_Type())
productFwImageRev.setMaxAccess(_D)
if mibBuilder.loadTexts:productFwImageRev.setStatus(_A)
class _ProductDefaultRevision_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,8))
_ProductDefaultRevision_Type.__name__=_E
_ProductDefaultRevision_Object=MibScalar
productDefaultRevision=_ProductDefaultRevision_Object((1,3,6,1,4,1,9303,4,3,1,1,6),_ProductDefaultRevision_Type())
productDefaultRevision.setMaxAccess(_D)
if mibBuilder.loadTexts:productDefaultRevision.setStatus(_A)
class _ProductOpDefRev_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_ProductOpDefRev_Type.__name__=_E
_ProductOpDefRev_Object=MibScalar
productOpDefRev=_ProductOpDefRev_Object((1,3,6,1,4,1,9303,4,3,1,1,7),_ProductOpDefRev_Type())
productOpDefRev.setMaxAccess(_D)
if mibBuilder.loadTexts:productOpDefRev.setStatus(_A)
class _ProductHardwareRev_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_ProductHardwareRev_Type.__name__=_E
_ProductHardwareRev_Object=MibScalar
productHardwareRev=_ProductHardwareRev_Object((1,3,6,1,4,1,9303,4,3,1,1,8),_ProductHardwareRev_Type())
productHardwareRev.setMaxAccess(_D)
if mibBuilder.loadTexts:productHardwareRev.setStatus(_A)
class _ProductPlatform_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_ProductPlatform_Type.__name__=_E
_ProductPlatform_Object=MibScalar
productPlatform=_ProductPlatform_Object((1,3,6,1,4,1,9303,4,3,1,1,9),_ProductPlatform_Type())
productPlatform.setMaxAccess(_D)
if mibBuilder.loadTexts:productPlatform.setStatus(_A)
_ProductHardwarePCBARevision_Type=Integer32
_ProductHardwarePCBARevision_Object=MibScalar
productHardwarePCBARevision=_ProductHardwarePCBARevision_Object((1,3,6,1,4,1,9303,4,3,1,1,10),_ProductHardwarePCBARevision_Type())
productHardwarePCBARevision.setMaxAccess(_D)
if mibBuilder.loadTexts:productHardwarePCBARevision.setStatus(_A)
class _ProductFunctionIdentity_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_ProductFunctionIdentity_Type.__name__=_E
_ProductFunctionIdentity_Object=MibScalar
productFunctionIdentity=_ProductFunctionIdentity_Object((1,3,6,1,4,1,9303,4,3,1,1,11),_ProductFunctionIdentity_Type())
productFunctionIdentity.setMaxAccess(_D)
if mibBuilder.loadTexts:productFunctionIdentity.setStatus(_A)
_ProductMacAddress_Type=MacAddress
_ProductMacAddress_Object=MibScalar
productMacAddress=_ProductMacAddress_Object((1,3,6,1,4,1,9303,4,3,1,1,12),_ProductMacAddress_Type())
productMacAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:productMacAddress.setStatus(_A)
class _ProductIdentity_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_ProductIdentity_Type.__name__=_E
_ProductIdentity_Object=MibScalar
productIdentity=_ProductIdentity_Object((1,3,6,1,4,1,9303,4,3,1,1,13),_ProductIdentity_Type())
productIdentity.setMaxAccess(_D)
if mibBuilder.loadTexts:productIdentity.setStatus(_A)
_SystemConfig_ObjectIdentity=ObjectIdentity
systemConfig=_SystemConfig_ObjectIdentity((1,3,6,1,4,1,9303,4,3,1,2))
class _SystemConfigRestartControl_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_M,1),('restartNow',2)))
_SystemConfigRestartControl_Type.__name__=_C
_SystemConfigRestartControl_Object=MibScalar
systemConfigRestartControl=_SystemConfigRestartControl_Object((1,3,6,1,4,1,9303,4,3,1,2,1),_SystemConfigRestartControl_Type())
systemConfigRestartControl.setMaxAccess(_B)
if mibBuilder.loadTexts:systemConfigRestartControl.setStatus(_A)
class _SystemConfigRestartControlNotify_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_J,1),('notifying',2)))
_SystemConfigRestartControlNotify_Type.__name__=_C
_SystemConfigRestartControlNotify_Object=MibScalar
systemConfigRestartControlNotify=_SystemConfigRestartControlNotify_Object((1,3,6,1,4,1,9303,4,3,1,2,2),_SystemConfigRestartControlNotify_Type())
systemConfigRestartControlNotify.setMaxAccess(_B)
if mibBuilder.loadTexts:systemConfigRestartControlNotify.setStatus(_A)
class _SystemConfigSave_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('save',1),('changed',2),('notChanged',3)))
_SystemConfigSave_Type.__name__=_C
_SystemConfigSave_Object=MibScalar
systemConfigSave=_SystemConfigSave_Object((1,3,6,1,4,1,9303,4,3,1,2,3),_SystemConfigSave_Type())
systemConfigSave.setMaxAccess(_B)
if mibBuilder.loadTexts:systemConfigSave.setStatus(_A)
class _SystemConfigFactoryReset_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_M,1),('factoryReset',2)))
_SystemConfigFactoryReset_Type.__name__=_C
_SystemConfigFactoryReset_Object=MibScalar
systemConfigFactoryReset=_SystemConfigFactoryReset_Object((1,3,6,1,4,1,9303,4,3,1,2,4),_SystemConfigFactoryReset_Type())
systemConfigFactoryReset.setMaxAccess(_B)
if mibBuilder.loadTexts:systemConfigFactoryReset.setStatus(_A)
class _SystemConfigSaveNotify_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_J,1),(_N,2),('onlyErrors',3)))
_SystemConfigSaveNotify_Type.__name__=_C
_SystemConfigSaveNotify_Object=MibScalar
systemConfigSaveNotify=_SystemConfigSaveNotify_Object((1,3,6,1,4,1,9303,4,3,1,2,5),_SystemConfigSaveNotify_Type())
systemConfigSaveNotify.setMaxAccess(_B)
if mibBuilder.loadTexts:systemConfigSaveNotify.setStatus(_A)
_DownloadConfig_ObjectIdentity=ObjectIdentity
downloadConfig=_DownloadConfig_ObjectIdentity((1,3,6,1,4,1,9303,4,3,1,3))
class _DownloadServer_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_DownloadServer_Type.__name__=_E
_DownloadServer_Object=MibScalar
downloadServer=_DownloadServer_Object((1,3,6,1,4,1,9303,4,3,1,3,1),_DownloadServer_Type())
downloadServer.setMaxAccess(_B)
if mibBuilder.loadTexts:downloadServer.setStatus(_A)
class _DownloadFile_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,80))
_DownloadFile_Type.__name__=_E
_DownloadFile_Object=MibScalar
downloadFile=_DownloadFile_Object((1,3,6,1,4,1,9303,4,3,1,3,2),_DownloadFile_Type())
downloadFile.setMaxAccess(_B)
if mibBuilder.loadTexts:downloadFile.setStatus(_A)
class _DownloadAction_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('notDownloading',1),('startDownload',2)))
_DownloadAction_Type.__name__=_C
_DownloadAction_Object=MibScalar
downloadAction=_DownloadAction_Object((1,3,6,1,4,1,9303,4,3,1,3,3),_DownloadAction_Type())
downloadAction.setMaxAccess(_B)
if mibBuilder.loadTexts:downloadAction.setStatus(_A)
class _DownloadMethod_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('tftp',1),('http',2),('auto',3)))
_DownloadMethod_Type.__name__=_C
_DownloadMethod_Object=MibScalar
downloadMethod=_DownloadMethod_Object((1,3,6,1,4,1,9303,4,3,1,3,4),_DownloadMethod_Type())
downloadMethod.setMaxAccess(_B)
if mibBuilder.loadTexts:downloadMethod.setStatus(_A)
class _DownloadRetryCount_Type(Integer32):defaultValue=5;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,10))
_DownloadRetryCount_Type.__name__=_C
_DownloadRetryCount_Object=MibScalar
downloadRetryCount=_DownloadRetryCount_Object((1,3,6,1,4,1,9303,4,3,1,3,5),_DownloadRetryCount_Type())
downloadRetryCount.setMaxAccess(_B)
if mibBuilder.loadTexts:downloadRetryCount.setStatus(_A)
class _DownloadResultCode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7,8)));namedValues=NamedValues(*(('none',0),('inProgress',1),('success',2),('failureHostNotFound',3),('failureFileNotFound',4),('failureFileIncorrectSize',5),('failureFileVerifyFailure',6),('failureFileIncompatible',7),('failureUnknownError',8)))
_DownloadResultCode_Type.__name__=_C
_DownloadResultCode_Object=MibScalar
downloadResultCode=_DownloadResultCode_Object((1,3,6,1,4,1,9303,4,3,1,3,6),_DownloadResultCode_Type())
downloadResultCode.setMaxAccess(_D)
if mibBuilder.loadTexts:downloadResultCode.setStatus(_A)
class _DownloadResultNotify_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_J,1),(_N,2),('onError',3)))
_DownloadResultNotify_Type.__name__=_C
_DownloadResultNotify_Object=MibScalar
downloadResultNotify=_DownloadResultNotify_Object((1,3,6,1,4,1,9303,4,3,1,3,7),_DownloadResultNotify_Type())
downloadResultNotify.setMaxAccess(_B)
if mibBuilder.loadTexts:downloadResultNotify.setStatus(_A)
_HostConfig_ObjectIdentity=ObjectIdentity
hostConfig=_HostConfig_ObjectIdentity((1,3,6,1,4,1,9303,4,3,1,4))
_HostIfMax_Type=Integer32
_HostIfMax_Object=MibScalar
hostIfMax=_HostIfMax_Object((1,3,6,1,4,1,9303,4,3,1,4,1),_HostIfMax_Type())
hostIfMax.setMaxAccess(_D)
if mibBuilder.loadTexts:hostIfMax.setStatus(_A)
_HostIfDefined_Type=Integer32
_HostIfDefined_Object=MibScalar
hostIfDefined=_HostIfDefined_Object((1,3,6,1,4,1,9303,4,3,1,4,2),_HostIfDefined_Type())
hostIfDefined.setMaxAccess(_D)
if mibBuilder.loadTexts:hostIfDefined.setStatus(_A)
_HostIfTable_Object=MibTable
hostIfTable=_HostIfTable_Object((1,3,6,1,4,1,9303,4,3,1,4,3))
if mibBuilder.loadTexts:hostIfTable.setStatus(_A)
_HostIfEntry_Object=MibTableRow
hostIfEntry=_HostIfEntry_Object((1,3,6,1,4,1,9303,4,3,1,4,3,1))
hostIfEntry.setIndexNames((0,_F,_O))
if mibBuilder.loadTexts:hostIfEntry.setStatus(_A)
class _HostIfIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4))
_HostIfIndex_Type.__name__=_C
_HostIfIndex_Object=MibTableColumn
hostIfIndex=_HostIfIndex_Object((1,3,6,1,4,1,9303,4,3,1,4,3,1,1),_HostIfIndex_Type())
hostIfIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:hostIfIndex.setStatus(_A)
class _HostIfMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('dhcp',1),('static',2),('pppoe',3),('pppoeFixed',4)))
_HostIfMode_Type.__name__=_C
_HostIfMode_Object=MibTableColumn
hostIfMode=_HostIfMode_Object((1,3,6,1,4,1,9303,4,3,1,4,3,1,2),_HostIfMode_Type())
hostIfMode.setMaxAccess(_B)
if mibBuilder.loadTexts:hostIfMode.setStatus(_A)
class _HostIfHostName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_HostIfHostName_Type.__name__=_E
_HostIfHostName_Object=MibTableColumn
hostIfHostName=_HostIfHostName_Object((1,3,6,1,4,1,9303,4,3,1,4,3,1,3),_HostIfHostName_Type())
hostIfHostName.setMaxAccess(_B)
if mibBuilder.loadTexts:hostIfHostName.setStatus(_A)
_HostIfAddress_Type=IpAddress
_HostIfAddress_Object=MibTableColumn
hostIfAddress=_HostIfAddress_Object((1,3,6,1,4,1,9303,4,3,1,4,3,1,4),_HostIfAddress_Type())
hostIfAddress.setMaxAccess(_G)
if mibBuilder.loadTexts:hostIfAddress.setStatus(_A)
_HostIfSubnetMask_Type=IpAddress
_HostIfSubnetMask_Object=MibTableColumn
hostIfSubnetMask=_HostIfSubnetMask_Object((1,3,6,1,4,1,9303,4,3,1,4,3,1,5),_HostIfSubnetMask_Type())
hostIfSubnetMask.setMaxAccess(_B)
if mibBuilder.loadTexts:hostIfSubnetMask.setStatus(_A)
_HostIfDefaultRouter_Type=IpAddress
_HostIfDefaultRouter_Object=MibTableColumn
hostIfDefaultRouter=_HostIfDefaultRouter_Object((1,3,6,1,4,1,9303,4,3,1,4,3,1,6),_HostIfDefaultRouter_Type())
hostIfDefaultRouter.setMaxAccess(_B)
if mibBuilder.loadTexts:hostIfDefaultRouter.setStatus(_A)
class _HostIfDomainName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_HostIfDomainName_Type.__name__=_E
_HostIfDomainName_Object=MibTableColumn
hostIfDomainName=_HostIfDomainName_Object((1,3,6,1,4,1,9303,4,3,1,4,3,1,7),_HostIfDomainName_Type())
hostIfDomainName.setMaxAccess(_B)
if mibBuilder.loadTexts:hostIfDomainName.setStatus(_A)
_HostIfDnsServer1_Type=IpAddress
_HostIfDnsServer1_Object=MibTableColumn
hostIfDnsServer1=_HostIfDnsServer1_Object((1,3,6,1,4,1,9303,4,3,1,4,3,1,8),_HostIfDnsServer1_Type())
hostIfDnsServer1.setMaxAccess(_B)
if mibBuilder.loadTexts:hostIfDnsServer1.setStatus(_A)
_HostIfDnsServer2_Type=IpAddress
_HostIfDnsServer2_Object=MibTableColumn
hostIfDnsServer2=_HostIfDnsServer2_Object((1,3,6,1,4,1,9303,4,3,1,4,3,1,9),_HostIfDnsServer2_Type())
hostIfDnsServer2.setMaxAccess(_B)
if mibBuilder.loadTexts:hostIfDnsServer2.setStatus(_A)
class _HostIfDhcpClientID_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_HostIfDhcpClientID_Type.__name__=_E
_HostIfDhcpClientID_Object=MibTableColumn
hostIfDhcpClientID=_HostIfDhcpClientID_Object((1,3,6,1,4,1,9303,4,3,1,4,3,1,10),_HostIfDhcpClientID_Type())
hostIfDhcpClientID.setMaxAccess(_B)
if mibBuilder.loadTexts:hostIfDhcpClientID.setStatus(_A)
class _HostIfDhcpVendorClassID_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,48))
_HostIfDhcpVendorClassID_Type.__name__=_E
_HostIfDhcpVendorClassID_Object=MibTableColumn
hostIfDhcpVendorClassID=_HostIfDhcpVendorClassID_Object((1,3,6,1,4,1,9303,4,3,1,4,3,1,11),_HostIfDhcpVendorClassID_Type())
hostIfDhcpVendorClassID.setMaxAccess(_B)
if mibBuilder.loadTexts:hostIfDhcpVendorClassID.setStatus(_A)
class _HostIfDiffservCodePoint_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,63))
_HostIfDiffservCodePoint_Type.__name__=_C
_HostIfDiffservCodePoint_Object=MibTableColumn
hostIfDiffservCodePoint=_HostIfDiffservCodePoint_Object((1,3,6,1,4,1,9303,4,3,1,4,3,1,12),_HostIfDiffservCodePoint_Type())
hostIfDiffservCodePoint.setMaxAccess(_B)
if mibBuilder.loadTexts:hostIfDiffservCodePoint.setStatus(_A)
class _HostIfVlan_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4094))
_HostIfVlan_Type.__name__=_C
_HostIfVlan_Object=MibTableColumn
hostIfVlan=_HostIfVlan_Object((1,3,6,1,4,1,9303,4,3,1,4,3,1,13),_HostIfVlan_Type())
hostIfVlan.setMaxAccess(_B)
if mibBuilder.loadTexts:hostIfVlan.setStatus(_A)
class _HostIfVlanPriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_HostIfVlanPriority_Type.__name__=_C
_HostIfVlanPriority_Object=MibTableColumn
hostIfVlanPriority=_HostIfVlanPriority_Object((1,3,6,1,4,1,9303,4,3,1,4,3,1,14),_HostIfVlanPriority_Type())
hostIfVlanPriority.setMaxAccess(_B)
if mibBuilder.loadTexts:hostIfVlanPriority.setStatus(_A)
class _HostIfSecurePing_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('enabled',1),('disabled',2)))
_HostIfSecurePing_Type.__name__=_C
_HostIfSecurePing_Object=MibTableColumn
hostIfSecurePing=_HostIfSecurePing_Object((1,3,6,1,4,1,9303,4,3,1,4,3,1,15),_HostIfSecurePing_Type())
hostIfSecurePing.setMaxAccess(_B)
if mibBuilder.loadTexts:hostIfSecurePing.setStatus(_A)
_SnmpConfig_ObjectIdentity=ObjectIdentity
snmpConfig=_SnmpConfig_ObjectIdentity((1,3,6,1,4,1,9303,4,3,1,7))
_SnmpTrapDestHostsMax_Type=Integer32
_SnmpTrapDestHostsMax_Object=MibScalar
snmpTrapDestHostsMax=_SnmpTrapDestHostsMax_Object((1,3,6,1,4,1,9303,4,3,1,7,1),_SnmpTrapDestHostsMax_Type())
snmpTrapDestHostsMax.setMaxAccess(_D)
if mibBuilder.loadTexts:snmpTrapDestHostsMax.setStatus(_A)
_SnmpTrapDestHostsDefined_Type=Integer32
_SnmpTrapDestHostsDefined_Object=MibScalar
snmpTrapDestHostsDefined=_SnmpTrapDestHostsDefined_Object((1,3,6,1,4,1,9303,4,3,1,7,2),_SnmpTrapDestHostsDefined_Type())
snmpTrapDestHostsDefined.setMaxAccess(_D)
if mibBuilder.loadTexts:snmpTrapDestHostsDefined.setStatus(_A)
_SnmpTrapDestinationTable_Object=MibTable
snmpTrapDestinationTable=_SnmpTrapDestinationTable_Object((1,3,6,1,4,1,9303,4,3,1,7,3))
if mibBuilder.loadTexts:snmpTrapDestinationTable.setStatus(_A)
_SnmpTrapDestinationEntry_Object=MibTableRow
snmpTrapDestinationEntry=_SnmpTrapDestinationEntry_Object((1,3,6,1,4,1,9303,4,3,1,7,3,1))
snmpTrapDestinationEntry.setIndexNames((0,_F,_P),(0,_F,_Q))
if mibBuilder.loadTexts:snmpTrapDestinationEntry.setStatus(_A)
class _SnmpTrapDestIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,6))
_SnmpTrapDestIndex_Type.__name__=_C
_SnmpTrapDestIndex_Object=MibTableColumn
snmpTrapDestIndex=_SnmpTrapDestIndex_Object((1,3,6,1,4,1,9303,4,3,1,7,3,1,1),_SnmpTrapDestIndex_Type())
snmpTrapDestIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:snmpTrapDestIndex.setStatus(_A)
class _SnmpTrapDestName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_SnmpTrapDestName_Type.__name__=_E
_SnmpTrapDestName_Object=MibTableColumn
snmpTrapDestName=_SnmpTrapDestName_Object((1,3,6,1,4,1,9303,4,3,1,7,3,1,2),_SnmpTrapDestName_Type())
snmpTrapDestName.setMaxAccess(_G)
if mibBuilder.loadTexts:snmpTrapDestName.setStatus(_A)
_SnmpTrapDestAddress_Type=IpAddress
_SnmpTrapDestAddress_Object=MibTableColumn
snmpTrapDestAddress=_SnmpTrapDestAddress_Object((1,3,6,1,4,1,9303,4,3,1,7,3,1,3),_SnmpTrapDestAddress_Type())
snmpTrapDestAddress.setMaxAccess(_G)
if mibBuilder.loadTexts:snmpTrapDestAddress.setStatus(_A)
class _SnmpTrapDestTagList_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_SnmpTrapDestTagList_Type.__name__=_E
_SnmpTrapDestTagList_Object=MibTableColumn
snmpTrapDestTagList=_SnmpTrapDestTagList_Object((1,3,6,1,4,1,9303,4,3,1,7,3,1,4),_SnmpTrapDestTagList_Type())
snmpTrapDestTagList.setMaxAccess(_G)
if mibBuilder.loadTexts:snmpTrapDestTagList.setStatus(_A)
_SnmpTrapDestRowStatus_Type=RowStatus
_SnmpTrapDestRowStatus_Object=MibTableColumn
snmpTrapDestRowStatus=_SnmpTrapDestRowStatus_Object((1,3,6,1,4,1,9303,4,3,1,7,3,1,5),_SnmpTrapDestRowStatus_Type())
snmpTrapDestRowStatus.setMaxAccess(_G)
if mibBuilder.loadTexts:snmpTrapDestRowStatus.setStatus(_A)
class _SnmpReadCommunityName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,16))
_SnmpReadCommunityName_Type.__name__=_E
_SnmpReadCommunityName_Object=MibScalar
snmpReadCommunityName=_SnmpReadCommunityName_Object((1,3,6,1,4,1,9303,4,3,1,7,4),_SnmpReadCommunityName_Type())
snmpReadCommunityName.setMaxAccess(_B)
if mibBuilder.loadTexts:snmpReadCommunityName.setStatus(_A)
class _SnmpWriteCommunityName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,16))
_SnmpWriteCommunityName_Type.__name__=_E
_SnmpWriteCommunityName_Object=MibScalar
snmpWriteCommunityName=_SnmpWriteCommunityName_Object((1,3,6,1,4,1,9303,4,3,1,7,5),_SnmpWriteCommunityName_Type())
snmpWriteCommunityName.setMaxAccess(_B)
if mibBuilder.loadTexts:snmpWriteCommunityName.setStatus(_A)
class _SnmpTrapCommunityName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,16))
_SnmpTrapCommunityName_Type.__name__=_E
_SnmpTrapCommunityName_Object=MibScalar
snmpTrapCommunityName=_SnmpTrapCommunityName_Object((1,3,6,1,4,1,9303,4,3,1,7,6),_SnmpTrapCommunityName_Type())
snmpTrapCommunityName.setMaxAccess(_B)
if mibBuilder.loadTexts:snmpTrapCommunityName.setStatus(_A)
class _SnmpDiffservCodePoint_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,63))
_SnmpDiffservCodePoint_Type.__name__=_C
_SnmpDiffservCodePoint_Object=MibScalar
snmpDiffservCodePoint=_SnmpDiffservCodePoint_Object((1,3,6,1,4,1,9303,4,3,1,7,7),_SnmpDiffservCodePoint_Type())
snmpDiffservCodePoint.setMaxAccess(_B)
if mibBuilder.loadTexts:snmpDiffservCodePoint.setStatus(_A)
class _SnmpAtomicSet_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('idle',1),('stage',2),('apply',3)))
_SnmpAtomicSet_Type.__name__=_C
_SnmpAtomicSet_Object=MibScalar
snmpAtomicSet=_SnmpAtomicSet_Object((1,3,6,1,4,1,9303,4,3,1,7,8),_SnmpAtomicSet_Type())
snmpAtomicSet.setMaxAccess(_B)
if mibBuilder.loadTexts:snmpAtomicSet.setStatus(_A)
_VlanConfig_ObjectIdentity=ObjectIdentity
vlanConfig=_VlanConfig_ObjectIdentity((1,3,6,1,4,1,9303,4,3,1,8))
_VlanBase_ObjectIdentity=ObjectIdentity
vlanBase=_VlanBase_ObjectIdentity((1,3,6,1,4,1,9303,4,3,1,8,1))
class _VlanVersionNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('version1',1),('version2',2)))
_VlanVersionNumber_Type.__name__=_C
_VlanVersionNumber_Object=MibScalar
vlanVersionNumber=_VlanVersionNumber_Object((1,3,6,1,4,1,9303,4,3,1,8,1,1),_VlanVersionNumber_Type())
vlanVersionNumber.setMaxAccess(_D)
if mibBuilder.loadTexts:vlanVersionNumber.setStatus(_A)
class _VlanMaxVlanId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094))
_VlanMaxVlanId_Type.__name__=_C
_VlanMaxVlanId_Object=MibScalar
vlanMaxVlanId=_VlanMaxVlanId_Object((1,3,6,1,4,1,9303,4,3,1,8,1,2),_VlanMaxVlanId_Type())
vlanMaxVlanId.setMaxAccess(_D)
if mibBuilder.loadTexts:vlanMaxVlanId.setStatus(_A)
_VlanMaxSupportedVlans_Type=Unsigned32
_VlanMaxSupportedVlans_Object=MibScalar
vlanMaxSupportedVlans=_VlanMaxSupportedVlans_Object((1,3,6,1,4,1,9303,4,3,1,8,1,3),_VlanMaxSupportedVlans_Type())
vlanMaxSupportedVlans.setMaxAccess(_D)
if mibBuilder.loadTexts:vlanMaxSupportedVlans.setStatus(_A)
_VlanNumVlans_Type=Unsigned32
_VlanNumVlans_Object=MibScalar
vlanNumVlans=_VlanNumVlans_Object((1,3,6,1,4,1,9303,4,3,1,8,1,4),_VlanNumVlans_Type())
vlanNumVlans.setMaxAccess(_D)
if mibBuilder.loadTexts:vlanNumVlans.setStatus(_A)
_VlanTp_ObjectIdentity=ObjectIdentity
vlanTp=_VlanTp_ObjectIdentity((1,3,6,1,4,1,9303,4,3,1,8,2))
_VlanFdbTable_Object=MibTable
vlanFdbTable=_VlanFdbTable_Object((1,3,6,1,4,1,9303,4,3,1,8,2,1))
if mibBuilder.loadTexts:vlanFdbTable.setStatus(_A)
_VlanFdbEntry_Object=MibTableRow
vlanFdbEntry=_VlanFdbEntry_Object((1,3,6,1,4,1,9303,4,3,1,8,2,1,1))
vlanFdbEntry.setIndexNames((0,_F,_K))
if mibBuilder.loadTexts:vlanFdbEntry.setStatus(_A)
_VlanFdbId_Type=Unsigned32
_VlanFdbId_Object=MibTableColumn
vlanFdbId=_VlanFdbId_Object((1,3,6,1,4,1,9303,4,3,1,8,2,1,1,1),_VlanFdbId_Type())
vlanFdbId.setMaxAccess(_R)
if mibBuilder.loadTexts:vlanFdbId.setStatus(_A)
_VlanFdbDynamicCount_Type=Counter32
_VlanFdbDynamicCount_Object=MibTableColumn
vlanFdbDynamicCount=_VlanFdbDynamicCount_Object((1,3,6,1,4,1,9303,4,3,1,8,2,1,1,2),_VlanFdbDynamicCount_Type())
vlanFdbDynamicCount.setMaxAccess(_D)
if mibBuilder.loadTexts:vlanFdbDynamicCount.setStatus(_A)
_VlanTpFdbTable_Object=MibTable
vlanTpFdbTable=_VlanTpFdbTable_Object((1,3,6,1,4,1,9303,4,3,1,8,2,2))
if mibBuilder.loadTexts:vlanTpFdbTable.setStatus(_A)
_VlanTpFdbEntry_Object=MibTableRow
vlanTpFdbEntry=_VlanTpFdbEntry_Object((1,3,6,1,4,1,9303,4,3,1,8,2,2,1))
vlanTpFdbEntry.setIndexNames((0,_F,_K),(0,_F,_S))
if mibBuilder.loadTexts:vlanTpFdbEntry.setStatus(_A)
_VlanTpFdbAddress_Type=MacAddress
_VlanTpFdbAddress_Object=MibTableColumn
vlanTpFdbAddress=_VlanTpFdbAddress_Object((1,3,6,1,4,1,9303,4,3,1,8,2,2,1,1),_VlanTpFdbAddress_Type())
vlanTpFdbAddress.setMaxAccess(_R)
if mibBuilder.loadTexts:vlanTpFdbAddress.setStatus(_A)
class _VlanTpFdbPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_VlanTpFdbPort_Type.__name__=_C
_VlanTpFdbPort_Object=MibTableColumn
vlanTpFdbPort=_VlanTpFdbPort_Object((1,3,6,1,4,1,9303,4,3,1,8,2,2,1,2),_VlanTpFdbPort_Type())
vlanTpFdbPort.setMaxAccess(_D)
if mibBuilder.loadTexts:vlanTpFdbPort.setStatus(_A)
class _VlanTpFdbStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('other',1),('invalid',2),('learned',3),('self',4),('mgmt',5)))
_VlanTpFdbStatus_Type.__name__=_C
_VlanTpFdbStatus_Object=MibTableColumn
vlanTpFdbStatus=_VlanTpFdbStatus_Object((1,3,6,1,4,1,9303,4,3,1,8,2,2,1,3),_VlanTpFdbStatus_Type())
vlanTpFdbStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:vlanTpFdbStatus.setStatus(_A)
_VlanStatic_ObjectIdentity=ObjectIdentity
vlanStatic=_VlanStatic_ObjectIdentity((1,3,6,1,4,1,9303,4,3,1,8,3))
_VlanStaticTable_Object=MibTable
vlanStaticTable=_VlanStaticTable_Object((1,3,6,1,4,1,9303,4,3,1,8,3,1))
if mibBuilder.loadTexts:vlanStaticTable.setStatus(_A)
_VlanStaticEntry_Object=MibTableRow
vlanStaticEntry=_VlanStaticEntry_Object((1,3,6,1,4,1,9303,4,3,1,8,3,1,1))
vlanStaticEntry.setIndexNames((0,_F,_T))
if mibBuilder.loadTexts:vlanStaticEntry.setStatus(_A)
class _VlanStaticIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,16))
_VlanStaticIndex_Type.__name__=_C
_VlanStaticIndex_Object=MibTableColumn
vlanStaticIndex=_VlanStaticIndex_Object((1,3,6,1,4,1,9303,4,3,1,8,3,1,1,1),_VlanStaticIndex_Type())
vlanStaticIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:vlanStaticIndex.setStatus(_A)
class _VlanStaticName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_VlanStaticName_Type.__name__=_E
_VlanStaticName_Object=MibTableColumn
vlanStaticName=_VlanStaticName_Object((1,3,6,1,4,1,9303,4,3,1,8,3,1,1,2),_VlanStaticName_Type())
vlanStaticName.setMaxAccess(_B)
if mibBuilder.loadTexts:vlanStaticName.setStatus(_A)
class _VlanStaticVlanId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094))
_VlanStaticVlanId_Type.__name__=_C
_VlanStaticVlanId_Object=MibTableColumn
vlanStaticVlanId=_VlanStaticVlanId_Object((1,3,6,1,4,1,9303,4,3,1,8,3,1,1,3),_VlanStaticVlanId_Type())
vlanStaticVlanId.setMaxAccess(_B)
if mibBuilder.loadTexts:vlanStaticVlanId.setStatus(_A)
class _VlanStaticPriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_VlanStaticPriority_Type.__name__=_C
_VlanStaticPriority_Object=MibTableColumn
vlanStaticPriority=_VlanStaticPriority_Object((1,3,6,1,4,1,9303,4,3,1,8,3,1,1,4),_VlanStaticPriority_Type())
vlanStaticPriority.setMaxAccess(_B)
if mibBuilder.loadTexts:vlanStaticPriority.setStatus(_A)
_VlanStaticEgressPorts_Type=PortList
_VlanStaticEgressPorts_Object=MibTableColumn
vlanStaticEgressPorts=_VlanStaticEgressPorts_Object((1,3,6,1,4,1,9303,4,3,1,8,3,1,1,5),_VlanStaticEgressPorts_Type())
vlanStaticEgressPorts.setMaxAccess(_B)
if mibBuilder.loadTexts:vlanStaticEgressPorts.setStatus(_A)
_VlanStaticUntaggedPorts_Type=PortList
_VlanStaticUntaggedPorts_Object=MibTableColumn
vlanStaticUntaggedPorts=_VlanStaticUntaggedPorts_Object((1,3,6,1,4,1,9303,4,3,1,8,3,1,1,6),_VlanStaticUntaggedPorts_Type())
vlanStaticUntaggedPorts.setMaxAccess(_B)
if mibBuilder.loadTexts:vlanStaticUntaggedPorts.setStatus(_A)
_VlanStaticUnmodifiedPorts_Type=PortList
_VlanStaticUnmodifiedPorts_Object=MibTableColumn
vlanStaticUnmodifiedPorts=_VlanStaticUnmodifiedPorts_Object((1,3,6,1,4,1,9303,4,3,1,8,3,1,1,7),_VlanStaticUnmodifiedPorts_Type())
vlanStaticUnmodifiedPorts.setMaxAccess(_B)
if mibBuilder.loadTexts:vlanStaticUnmodifiedPorts.setStatus(_A)
_VlanStaticRowStatus_Type=RowStatus
_VlanStaticRowStatus_Object=MibTableColumn
vlanStaticRowStatus=_VlanStaticRowStatus_Object((1,3,6,1,4,1,9303,4,3,1,8,3,1,1,8),_VlanStaticRowStatus_Type())
vlanStaticRowStatus.setMaxAccess(_G)
if mibBuilder.loadTexts:vlanStaticRowStatus.setStatus(_A)
_DrgConformance_ObjectIdentity=ObjectIdentity
drgConformance=_DrgConformance_ObjectIdentity((1,3,6,1,4,1,9303,4,3,2))
_DrgGroups_ObjectIdentity=ObjectIdentity
drgGroups=_DrgGroups_ObjectIdentity((1,3,6,1,4,1,9303,4,3,2,1))
_DrgCompliance_ObjectIdentity=ObjectIdentity
drgCompliance=_DrgCompliance_ObjectIdentity((1,3,6,1,4,1,9303,4,3,2,2))
_DrgCompatibility_ObjectIdentity=ObjectIdentity
drgCompatibility=_DrgCompatibility_ObjectIdentity((1,3,6,1,4,1,9303,4,3,2,3))
notifyRestart=NotificationType((1,3,6,1,4,1,9303,4,3,0,1))
notifyRestart.setObjects(*((_F,_H),(_F,_I),(_F,_U),(_F,_V),(_F,_W),(_F,_X)))
if mibBuilder.loadTexts:notifyRestart.setStatus(_A)
notifyDownloadResult=NotificationType((1,3,6,1,4,1,9303,4,3,0,2))
notifyDownloadResult.setObjects(*((_F,_H),(_F,_I),(_F,_L)))
if mibBuilder.loadTexts:notifyDownloadResult.setStatus(_A)
notifyConfigSaveResult=NotificationType((1,3,6,1,4,1,9303,4,3,0,3))
notifyConfigSaveResult.setObjects(*((_F,_H),(_F,_I),(_F,_L)))
if mibBuilder.loadTexts:notifyConfigSaveResult.setStatus(_A)
mibBuilder.exportSymbols(_F,**{'pfDrgMib':pfDrgMib,'drgNotification':drgNotification,'notifyRestart':notifyRestart,'notifyDownloadResult':notifyDownloadResult,'notifyConfigSaveResult':notifyConfigSaveResult,'drgConfig':drgConfig,'productInfo':productInfo,'productName':productName,'productSerialNo':productSerialNo,'productProductionWeek':productProductionWeek,_U:productSwImageRev,'productFwImageRev':productFwImageRev,'productDefaultRevision':productDefaultRevision,_W:productOpDefRev,_V:productHardwareRev,'productPlatform':productPlatform,'productHardwarePCBARevision':productHardwarePCBARevision,_X:productFunctionIdentity,_H:productMacAddress,_I:productIdentity,'systemConfig':systemConfig,'systemConfigRestartControl':systemConfigRestartControl,'systemConfigRestartControlNotify':systemConfigRestartControlNotify,'systemConfigSave':systemConfigSave,'systemConfigFactoryReset':systemConfigFactoryReset,'systemConfigSaveNotify':systemConfigSaveNotify,'downloadConfig':downloadConfig,'downloadServer':downloadServer,'downloadFile':downloadFile,'downloadAction':downloadAction,'downloadMethod':downloadMethod,'downloadRetryCount':downloadRetryCount,_L:downloadResultCode,'downloadResultNotify':downloadResultNotify,'hostConfig':hostConfig,'hostIfMax':hostIfMax,'hostIfDefined':hostIfDefined,'hostIfTable':hostIfTable,'hostIfEntry':hostIfEntry,_O:hostIfIndex,'hostIfMode':hostIfMode,'hostIfHostName':hostIfHostName,'hostIfAddress':hostIfAddress,'hostIfSubnetMask':hostIfSubnetMask,'hostIfDefaultRouter':hostIfDefaultRouter,'hostIfDomainName':hostIfDomainName,'hostIfDnsServer1':hostIfDnsServer1,'hostIfDnsServer2':hostIfDnsServer2,'hostIfDhcpClientID':hostIfDhcpClientID,'hostIfDhcpVendorClassID':hostIfDhcpVendorClassID,'hostIfDiffservCodePoint':hostIfDiffservCodePoint,'hostIfVlan':hostIfVlan,'hostIfVlanPriority':hostIfVlanPriority,'hostIfSecurePing':hostIfSecurePing,'snmpConfig':snmpConfig,'snmpTrapDestHostsMax':snmpTrapDestHostsMax,'snmpTrapDestHostsDefined':snmpTrapDestHostsDefined,'snmpTrapDestinationTable':snmpTrapDestinationTable,'snmpTrapDestinationEntry':snmpTrapDestinationEntry,_P:snmpTrapDestIndex,_Q:snmpTrapDestName,'snmpTrapDestAddress':snmpTrapDestAddress,'snmpTrapDestTagList':snmpTrapDestTagList,'snmpTrapDestRowStatus':snmpTrapDestRowStatus,'snmpReadCommunityName':snmpReadCommunityName,'snmpWriteCommunityName':snmpWriteCommunityName,'snmpTrapCommunityName':snmpTrapCommunityName,'snmpDiffservCodePoint':snmpDiffservCodePoint,'snmpAtomicSet':snmpAtomicSet,'vlanConfig':vlanConfig,'vlanBase':vlanBase,'vlanVersionNumber':vlanVersionNumber,'vlanMaxVlanId':vlanMaxVlanId,'vlanMaxSupportedVlans':vlanMaxSupportedVlans,'vlanNumVlans':vlanNumVlans,'vlanTp':vlanTp,'vlanFdbTable':vlanFdbTable,'vlanFdbEntry':vlanFdbEntry,_K:vlanFdbId,'vlanFdbDynamicCount':vlanFdbDynamicCount,'vlanTpFdbTable':vlanTpFdbTable,'vlanTpFdbEntry':vlanTpFdbEntry,_S:vlanTpFdbAddress,'vlanTpFdbPort':vlanTpFdbPort,'vlanTpFdbStatus':vlanTpFdbStatus,'vlanStatic':vlanStatic,'vlanStaticTable':vlanStaticTable,'vlanStaticEntry':vlanStaticEntry,_T:vlanStaticIndex,'vlanStaticName':vlanStaticName,'vlanStaticVlanId':vlanStaticVlanId,'vlanStaticPriority':vlanStaticPriority,'vlanStaticEgressPorts':vlanStaticEgressPorts,'vlanStaticUntaggedPorts':vlanStaticUntaggedPorts,'vlanStaticUnmodifiedPorts':vlanStaticUnmodifiedPorts,'vlanStaticRowStatus':vlanStaticRowStatus,'drgConformance':drgConformance,'drgGroups':drgGroups,'drgCompliance':drgCompliance,'drgCompatibility':drgCompatibility})