_U='madgeVersionIndex'
_T='not-supported'
_S='madgeSecureTrapDestIndex'
_R='madgeSecureAllowedIndex'
_Q='madgeSecureCurrentIndex'
_P='identify'
_O='reboot'
_N='mac-address'
_M='ipx-address'
_L='ip-address'
_K='not-used'
_J='normal'
_I='disabled'
_H='enabled'
_G='MADGEBOX-MIB'
_F='OctetString'
_E='DisplayString'
_D='Integer32'
_C='read-write'
_B='read-only'
_A='mandatory'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_F,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_E,'PhysAddress','TextualConvention')
class DisplayString(OctetString):0
class MacAddress(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(6,6));fixedLength=6
_Madge_ObjectIdentity=ObjectIdentity
madge=_Madge_ObjectIdentity((1,3,6,1,4,1,494))
_MadgeBox_ObjectIdentity=ObjectIdentity
madgeBox=_MadgeBox_ObjectIdentity((1,3,6,1,4,1,494,10))
_MadgeConfig_ObjectIdentity=ObjectIdentity
madgeConfig=_MadgeConfig_ObjectIdentity((1,3,6,1,4,1,494,10,1))
_MadgeConfigIPAddress_Type=IpAddress
_MadgeConfigIPAddress_Object=MibScalar
madgeConfigIPAddress=_MadgeConfigIPAddress_Object((1,3,6,1,4,1,494,10,1,1),_MadgeConfigIPAddress_Type())
madgeConfigIPAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:madgeConfigIPAddress.setStatus(_A)
_MadgeConfigIPGateway_Type=IpAddress
_MadgeConfigIPGateway_Object=MibScalar
madgeConfigIPGateway=_MadgeConfigIPGateway_Object((1,3,6,1,4,1,494,10,1,2),_MadgeConfigIPGateway_Type())
madgeConfigIPGateway.setMaxAccess(_C)
if mibBuilder.loadTexts:madgeConfigIPGateway.setStatus(_A)
_MadgeConfigIPSubnetMask_Type=IpAddress
_MadgeConfigIPSubnetMask_Object=MibScalar
madgeConfigIPSubnetMask=_MadgeConfigIPSubnetMask_Object((1,3,6,1,4,1,494,10,1,3),_MadgeConfigIPSubnetMask_Type())
madgeConfigIPSubnetMask.setMaxAccess(_C)
if mibBuilder.loadTexts:madgeConfigIPSubnetMask.setStatus(_A)
_MadgeConfigSerialNumber_Type=MacAddress
_MadgeConfigSerialNumber_Object=MibScalar
madgeConfigSerialNumber=_MadgeConfigSerialNumber_Object((1,3,6,1,4,1,494,10,1,4),_MadgeConfigSerialNumber_Type())
madgeConfigSerialNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:madgeConfigSerialNumber.setStatus(_A)
class _MadgeConfigMCodeVersion_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,4));fixedLength=4
_MadgeConfigMCodeVersion_Type.__name__=_F
_MadgeConfigMCodeVersion_Object=MibScalar
madgeConfigMCodeVersion=_MadgeConfigMCodeVersion_Object((1,3,6,1,4,1,494,10,1,5),_MadgeConfigMCodeVersion_Type())
madgeConfigMCodeVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:madgeConfigMCodeVersion.setStatus(_A)
class _MadgeConfigBCodeVersion_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,4));fixedLength=4
_MadgeConfigBCodeVersion_Type.__name__=_F
_MadgeConfigBCodeVersion_Object=MibScalar
madgeConfigBCodeVersion=_MadgeConfigBCodeVersion_Object((1,3,6,1,4,1,494,10,1,6),_MadgeConfigBCodeVersion_Type())
madgeConfigBCodeVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:madgeConfigBCodeVersion.setStatus(_A)
_MadgeConfigMCodeFilename_Type=DisplayString
_MadgeConfigMCodeFilename_Object=MibScalar
madgeConfigMCodeFilename=_MadgeConfigMCodeFilename_Object((1,3,6,1,4,1,494,10,1,7),_MadgeConfigMCodeFilename_Type())
madgeConfigMCodeFilename.setMaxAccess(_B)
if mibBuilder.loadTexts:madgeConfigMCodeFilename.setStatus(_A)
class _MadgeConfigDeviceHealth_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_J,1),('warning',2),('degraded',3),('critical',4)))
_MadgeConfigDeviceHealth_Type.__name__=_D
_MadgeConfigDeviceHealth_Object=MibScalar
madgeConfigDeviceHealth=_MadgeConfigDeviceHealth_Object((1,3,6,1,4,1,494,10,1,8),_MadgeConfigDeviceHealth_Type())
madgeConfigDeviceHealth.setMaxAccess(_B)
if mibBuilder.loadTexts:madgeConfigDeviceHealth.setStatus(_A)
class _MadgeConfigAdminStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10)));namedValues=NamedValues(*((_J,1),(_O,2),(_P,3),('test',4),('erase-config',5),('erase-flash',6),('tftp-ip',7),('tftp-ipx',8),('rpl-ipx',9),('rpl-llc',10)))
_MadgeConfigAdminStatus_Type.__name__=_D
_MadgeConfigAdminStatus_Object=MibScalar
madgeConfigAdminStatus=_MadgeConfigAdminStatus_Object((1,3,6,1,4,1,494,10,1,9),_MadgeConfigAdminStatus_Type())
madgeConfigAdminStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:madgeConfigAdminStatus.setStatus(_A)
class _MadgeConfigPassword_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_MadgeConfigPassword_Type.__name__=_E
_MadgeConfigPassword_Object=MibScalar
madgeConfigPassword=_MadgeConfigPassword_Object((1,3,6,1,4,1,494,10,1,10),_MadgeConfigPassword_Type())
madgeConfigPassword.setMaxAccess(_C)
if mibBuilder.loadTexts:madgeConfigPassword.setStatus(_A)
_MadgeConfigLinkTest_Type=Integer32
_MadgeConfigLinkTest_Object=MibScalar
madgeConfigLinkTest=_MadgeConfigLinkTest_Object((1,3,6,1,4,1,494,10,1,11),_MadgeConfigLinkTest_Type())
madgeConfigLinkTest.setMaxAccess(_C)
if mibBuilder.loadTexts:madgeConfigLinkTest.setStatus(_A)
class _MadgeConfigOperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_J,1),(_O,2),(_P,3),('test',4),('downloading',5)))
_MadgeConfigOperStatus_Type.__name__=_D
_MadgeConfigOperStatus_Object=MibScalar
madgeConfigOperStatus=_MadgeConfigOperStatus_Object((1,3,6,1,4,1,494,10,1,12),_MadgeConfigOperStatus_Type())
madgeConfigOperStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:madgeConfigOperStatus.setStatus(_A)
_MadgeConfigEraseFlashVersion_Type=Integer32
_MadgeConfigEraseFlashVersion_Object=MibScalar
madgeConfigEraseFlashVersion=_MadgeConfigEraseFlashVersion_Object((1,3,6,1,4,1,494,10,1,13),_MadgeConfigEraseFlashVersion_Type())
madgeConfigEraseFlashVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:madgeConfigEraseFlashVersion.setStatus(_A)
_MadgeConfigDefaultFlashVersion_Type=Integer32
_MadgeConfigDefaultFlashVersion_Object=MibScalar
madgeConfigDefaultFlashVersion=_MadgeConfigDefaultFlashVersion_Object((1,3,6,1,4,1,494,10,1,14),_MadgeConfigDefaultFlashVersion_Type())
madgeConfigDefaultFlashVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:madgeConfigDefaultFlashVersion.setStatus(_A)
_MadgeSecure_ObjectIdentity=ObjectIdentity
madgeSecure=_MadgeSecure_ObjectIdentity((1,3,6,1,4,1,494,10,2))
_MadgeSecureCurrentTableSize_Type=Integer32
_MadgeSecureCurrentTableSize_Object=MibScalar
madgeSecureCurrentTableSize=_MadgeSecureCurrentTableSize_Object((1,3,6,1,4,1,494,10,2,1),_MadgeSecureCurrentTableSize_Type())
madgeSecureCurrentTableSize.setMaxAccess(_B)
if mibBuilder.loadTexts:madgeSecureCurrentTableSize.setStatus(_A)
_MadgeSecureCurrentTimeout_Type=Integer32
_MadgeSecureCurrentTimeout_Object=MibScalar
madgeSecureCurrentTimeout=_MadgeSecureCurrentTimeout_Object((1,3,6,1,4,1,494,10,2,2),_MadgeSecureCurrentTimeout_Type())
madgeSecureCurrentTimeout.setMaxAccess(_C)
if mibBuilder.loadTexts:madgeSecureCurrentTimeout.setStatus(_A)
_MadgeSecureCurrentTable_Object=MibTable
madgeSecureCurrentTable=_MadgeSecureCurrentTable_Object((1,3,6,1,4,1,494,10,2,3))
if mibBuilder.loadTexts:madgeSecureCurrentTable.setStatus(_A)
_MadgeSecureCurrentEntry_Object=MibTableRow
madgeSecureCurrentEntry=_MadgeSecureCurrentEntry_Object((1,3,6,1,4,1,494,10,2,3,1))
madgeSecureCurrentEntry.setIndexNames((0,_G,_Q))
if mibBuilder.loadTexts:madgeSecureCurrentEntry.setStatus(_A)
_MadgeSecureCurrentIndex_Type=Integer32
_MadgeSecureCurrentIndex_Object=MibTableColumn
madgeSecureCurrentIndex=_MadgeSecureCurrentIndex_Object((1,3,6,1,4,1,494,10,2,3,1,1),_MadgeSecureCurrentIndex_Type())
madgeSecureCurrentIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:madgeSecureCurrentIndex.setStatus(_A)
class _MadgeSecureCurrentType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_K,1),(_L,2),(_M,3),(_N,4)))
_MadgeSecureCurrentType_Type.__name__=_D
_MadgeSecureCurrentType_Object=MibTableColumn
madgeSecureCurrentType=_MadgeSecureCurrentType_Object((1,3,6,1,4,1,494,10,2,3,1,2),_MadgeSecureCurrentType_Type())
madgeSecureCurrentType.setMaxAccess(_B)
if mibBuilder.loadTexts:madgeSecureCurrentType.setStatus(_A)
_MadgeSecureCurrentAddress_Type=OctetString
_MadgeSecureCurrentAddress_Object=MibTableColumn
madgeSecureCurrentAddress=_MadgeSecureCurrentAddress_Object((1,3,6,1,4,1,494,10,2,3,1,3),_MadgeSecureCurrentAddress_Type())
madgeSecureCurrentAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:madgeSecureCurrentAddress.setStatus(_A)
_MadgeSecureCurrentUpdateTime_Type=Integer32
_MadgeSecureCurrentUpdateTime_Object=MibTableColumn
madgeSecureCurrentUpdateTime=_MadgeSecureCurrentUpdateTime_Object((1,3,6,1,4,1,494,10,2,3,1,4),_MadgeSecureCurrentUpdateTime_Type())
madgeSecureCurrentUpdateTime.setMaxAccess(_B)
if mibBuilder.loadTexts:madgeSecureCurrentUpdateTime.setStatus(_A)
_MadgeSecureCurrentIPAddress_Type=IpAddress
_MadgeSecureCurrentIPAddress_Object=MibTableColumn
madgeSecureCurrentIPAddress=_MadgeSecureCurrentIPAddress_Object((1,3,6,1,4,1,494,10,2,3,1,5),_MadgeSecureCurrentIPAddress_Type())
madgeSecureCurrentIPAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:madgeSecureCurrentIPAddress.setStatus(_A)
class _MadgeSecureAllowedEnabled_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_I,2)))
_MadgeSecureAllowedEnabled_Type.__name__=_D
_MadgeSecureAllowedEnabled_Object=MibScalar
madgeSecureAllowedEnabled=_MadgeSecureAllowedEnabled_Object((1,3,6,1,4,1,494,10,2,4),_MadgeSecureAllowedEnabled_Type())
madgeSecureAllowedEnabled.setMaxAccess(_C)
if mibBuilder.loadTexts:madgeSecureAllowedEnabled.setStatus(_A)
_MadgeSecureAllowedTableSize_Type=Integer32
_MadgeSecureAllowedTableSize_Object=MibScalar
madgeSecureAllowedTableSize=_MadgeSecureAllowedTableSize_Object((1,3,6,1,4,1,494,10,2,5),_MadgeSecureAllowedTableSize_Type())
madgeSecureAllowedTableSize.setMaxAccess(_B)
if mibBuilder.loadTexts:madgeSecureAllowedTableSize.setStatus(_A)
_MadgeSecureAllowedTable_Object=MibTable
madgeSecureAllowedTable=_MadgeSecureAllowedTable_Object((1,3,6,1,4,1,494,10,2,6))
if mibBuilder.loadTexts:madgeSecureAllowedTable.setStatus(_A)
_MadgeSecureAllowedEntry_Object=MibTableRow
madgeSecureAllowedEntry=_MadgeSecureAllowedEntry_Object((1,3,6,1,4,1,494,10,2,6,1))
madgeSecureAllowedEntry.setIndexNames((0,_G,_R))
if mibBuilder.loadTexts:madgeSecureAllowedEntry.setStatus(_A)
_MadgeSecureAllowedIndex_Type=Integer32
_MadgeSecureAllowedIndex_Object=MibTableColumn
madgeSecureAllowedIndex=_MadgeSecureAllowedIndex_Object((1,3,6,1,4,1,494,10,2,6,1,1),_MadgeSecureAllowedIndex_Type())
madgeSecureAllowedIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:madgeSecureAllowedIndex.setStatus(_A)
class _MadgeSecureAllowedType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_K,1),(_L,2),(_M,3),(_N,4)))
_MadgeSecureAllowedType_Type.__name__=_D
_MadgeSecureAllowedType_Object=MibTableColumn
madgeSecureAllowedType=_MadgeSecureAllowedType_Object((1,3,6,1,4,1,494,10,2,6,1,2),_MadgeSecureAllowedType_Type())
madgeSecureAllowedType.setMaxAccess(_C)
if mibBuilder.loadTexts:madgeSecureAllowedType.setStatus(_A)
_MadgeSecureAllowedAddress_Type=OctetString
_MadgeSecureAllowedAddress_Object=MibTableColumn
madgeSecureAllowedAddress=_MadgeSecureAllowedAddress_Object((1,3,6,1,4,1,494,10,2,6,1,3),_MadgeSecureAllowedAddress_Type())
madgeSecureAllowedAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:madgeSecureAllowedAddress.setStatus(_A)
_MadgeSecureAllowedIPAddress_Type=IpAddress
_MadgeSecureAllowedIPAddress_Object=MibTableColumn
madgeSecureAllowedIPAddress=_MadgeSecureAllowedIPAddress_Object((1,3,6,1,4,1,494,10,2,6,1,4),_MadgeSecureAllowedIPAddress_Type())
madgeSecureAllowedIPAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:madgeSecureAllowedIPAddress.setStatus(_A)
class _MadgeSecureTrapDestEnabled_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_I,2)))
_MadgeSecureTrapDestEnabled_Type.__name__=_D
_MadgeSecureTrapDestEnabled_Object=MibScalar
madgeSecureTrapDestEnabled=_MadgeSecureTrapDestEnabled_Object((1,3,6,1,4,1,494,10,2,7),_MadgeSecureTrapDestEnabled_Type())
madgeSecureTrapDestEnabled.setMaxAccess(_C)
if mibBuilder.loadTexts:madgeSecureTrapDestEnabled.setStatus(_A)
_MadgeSecureTrapDestTableSize_Type=Integer32
_MadgeSecureTrapDestTableSize_Object=MibScalar
madgeSecureTrapDestTableSize=_MadgeSecureTrapDestTableSize_Object((1,3,6,1,4,1,494,10,2,8),_MadgeSecureTrapDestTableSize_Type())
madgeSecureTrapDestTableSize.setMaxAccess(_B)
if mibBuilder.loadTexts:madgeSecureTrapDestTableSize.setStatus(_A)
_MadgeSecureTrapDestTable_Object=MibTable
madgeSecureTrapDestTable=_MadgeSecureTrapDestTable_Object((1,3,6,1,4,1,494,10,2,9))
if mibBuilder.loadTexts:madgeSecureTrapDestTable.setStatus(_A)
_MadgeSecureTrapDestEntry_Object=MibTableRow
madgeSecureTrapDestEntry=_MadgeSecureTrapDestEntry_Object((1,3,6,1,4,1,494,10,2,9,1))
madgeSecureTrapDestEntry.setIndexNames((0,_G,_S))
if mibBuilder.loadTexts:madgeSecureTrapDestEntry.setStatus(_A)
_MadgeSecureTrapDestIndex_Type=Integer32
_MadgeSecureTrapDestIndex_Object=MibTableColumn
madgeSecureTrapDestIndex=_MadgeSecureTrapDestIndex_Object((1,3,6,1,4,1,494,10,2,9,1,1),_MadgeSecureTrapDestIndex_Type())
madgeSecureTrapDestIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:madgeSecureTrapDestIndex.setStatus(_A)
class _MadgeSecureTrapDestType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_K,1),(_L,2),(_M,3),(_N,4)))
_MadgeSecureTrapDestType_Type.__name__=_D
_MadgeSecureTrapDestType_Object=MibTableColumn
madgeSecureTrapDestType=_MadgeSecureTrapDestType_Object((1,3,6,1,4,1,494,10,2,9,1,2),_MadgeSecureTrapDestType_Type())
madgeSecureTrapDestType.setMaxAccess(_C)
if mibBuilder.loadTexts:madgeSecureTrapDestType.setStatus(_A)
_MadgeSecureTrapDestAddress_Type=OctetString
_MadgeSecureTrapDestAddress_Object=MibTableColumn
madgeSecureTrapDestAddress=_MadgeSecureTrapDestAddress_Object((1,3,6,1,4,1,494,10,2,9,1,3),_MadgeSecureTrapDestAddress_Type())
madgeSecureTrapDestAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:madgeSecureTrapDestAddress.setStatus(_A)
_MadgeSecureTrapDestIPAddress_Type=IpAddress
_MadgeSecureTrapDestIPAddress_Object=MibTableColumn
madgeSecureTrapDestIPAddress=_MadgeSecureTrapDestIPAddress_Object((1,3,6,1,4,1,494,10,2,9,1,4),_MadgeSecureTrapDestIPAddress_Type())
madgeSecureTrapDestIPAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:madgeSecureTrapDestIPAddress.setStatus(_A)
_MadgeDownload_ObjectIdentity=ObjectIdentity
madgeDownload=_MadgeDownload_ObjectIdentity((1,3,6,1,4,1,494,10,3))
_MadgeDownloadIPAddress_Type=IpAddress
_MadgeDownloadIPAddress_Object=MibScalar
madgeDownloadIPAddress=_MadgeDownloadIPAddress_Object((1,3,6,1,4,1,494,10,3,1),_MadgeDownloadIPAddress_Type())
madgeDownloadIPAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:madgeDownloadIPAddress.setStatus(_A)
_MadgeDownloadIPGateway_Type=IpAddress
_MadgeDownloadIPGateway_Object=MibScalar
madgeDownloadIPGateway=_MadgeDownloadIPGateway_Object((1,3,6,1,4,1,494,10,3,2),_MadgeDownloadIPGateway_Type())
madgeDownloadIPGateway.setMaxAccess(_C)
if mibBuilder.loadTexts:madgeDownloadIPGateway.setStatus(_A)
class _MadgeDownloadIPXAddress_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(12,12));fixedLength=12
_MadgeDownloadIPXAddress_Type.__name__=_F
_MadgeDownloadIPXAddress_Object=MibScalar
madgeDownloadIPXAddress=_MadgeDownloadIPXAddress_Object((1,3,6,1,4,1,494,10,3,3),_MadgeDownloadIPXAddress_Type())
madgeDownloadIPXAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:madgeDownloadIPXAddress.setStatus(_A)
_MadgeDownloadNodeAddress_Type=MacAddress
_MadgeDownloadNodeAddress_Object=MibScalar
madgeDownloadNodeAddress=_MadgeDownloadNodeAddress_Object((1,3,6,1,4,1,494,10,3,4),_MadgeDownloadNodeAddress_Type())
madgeDownloadNodeAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:madgeDownloadNodeAddress.setStatus(_A)
_MadgeDownloadFileName_Type=DisplayString
_MadgeDownloadFileName_Object=MibScalar
madgeDownloadFileName=_MadgeDownloadFileName_Object((1,3,6,1,4,1,494,10,3,5),_MadgeDownloadFileName_Type())
madgeDownloadFileName.setMaxAccess(_C)
if mibBuilder.loadTexts:madgeDownloadFileName.setStatus(_A)
_MadgeDownloadDestination_Type=Integer32
_MadgeDownloadDestination_Object=MibScalar
madgeDownloadDestination=_MadgeDownloadDestination_Object((1,3,6,1,4,1,494,10,3,6),_MadgeDownloadDestination_Type())
madgeDownloadDestination.setMaxAccess(_C)
if mibBuilder.loadTexts:madgeDownloadDestination.setStatus(_A)
class _MadgeDownloadState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11)));namedValues=NamedValues(*(('idle',1),('tftp-waiting-ip',2),('tftp-running-ip',3),('tftp-waiting-ipx',4),('tftp-running-ipx',5),('waiting-xmodem',6),('running-xmodem',7),('rpl-waiting-ipx',8),('rpl-running-ipx',9),('rpl-waiting-llc',10),('rpl-running-llc',11)))
_MadgeDownloadState_Type.__name__=_D
_MadgeDownloadState_Object=MibScalar
madgeDownloadState=_MadgeDownloadState_Object((1,3,6,1,4,1,494,10,3,7),_MadgeDownloadState_Type())
madgeDownloadState.setMaxAccess(_B)
if mibBuilder.loadTexts:madgeDownloadState.setStatus(_A)
class _MadgeDownloadFailureCode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,100,101,102,103,104,105,106,107)));namedValues=NamedValues(*(('no-error',1),('config-error',2),('busy',3),('timeout',4),('cancelled',5),('incompatible-file',6),('file-too-big',7),('protocol-error',8),('undefined-error',100),('file-not-found',101),('access-violation',102),('out-of-memory',103),('illegal-operation',104),('unknown-transfer-id',105),('file-already-exists',106),('no-such-user',107)))
_MadgeDownloadFailureCode_Type.__name__=_D
_MadgeDownloadFailureCode_Object=MibScalar
madgeDownloadFailureCode=_MadgeDownloadFailureCode_Object((1,3,6,1,4,1,494,10,3,8),_MadgeDownloadFailureCode_Type())
madgeDownloadFailureCode.setMaxAccess(_B)
if mibBuilder.loadTexts:madgeDownloadFailureCode.setStatus(_A)
class _MadgeDownloadStatusText_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_MadgeDownloadStatusText_Type.__name__=_E
_MadgeDownloadStatusText_Object=MibScalar
madgeDownloadStatusText=_MadgeDownloadStatusText_Object((1,3,6,1,4,1,494,10,3,9),_MadgeDownloadStatusText_Type())
madgeDownloadStatusText.setMaxAccess(_B)
if mibBuilder.loadTexts:madgeDownloadStatusText.setStatus(_A)
_MadgeDownloadSize_Type=Integer32
_MadgeDownloadSize_Object=MibScalar
madgeDownloadSize=_MadgeDownloadSize_Object((1,3,6,1,4,1,494,10,3,10),_MadgeDownloadSize_Type())
madgeDownloadSize.setMaxAccess(_B)
if mibBuilder.loadTexts:madgeDownloadSize.setStatus(_A)
_MadgeIP_ObjectIdentity=ObjectIdentity
madgeIP=_MadgeIP_ObjectIdentity((1,3,6,1,4,1,494,10,4))
_MadgeIPCurrentAddress_Type=IpAddress
_MadgeIPCurrentAddress_Object=MibScalar
madgeIPCurrentAddress=_MadgeIPCurrentAddress_Object((1,3,6,1,4,1,494,10,4,1),_MadgeIPCurrentAddress_Type())
madgeIPCurrentAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:madgeIPCurrentAddress.setStatus(_A)
_MadgeIPCurrentGateway_Type=IpAddress
_MadgeIPCurrentGateway_Object=MibScalar
madgeIPCurrentGateway=_MadgeIPCurrentGateway_Object((1,3,6,1,4,1,494,10,4,2),_MadgeIPCurrentGateway_Type())
madgeIPCurrentGateway.setMaxAccess(_B)
if mibBuilder.loadTexts:madgeIPCurrentGateway.setStatus(_A)
_MadgeIPCurrentSubnetMask_Type=IpAddress
_MadgeIPCurrentSubnetMask_Object=MibScalar
madgeIPCurrentSubnetMask=_MadgeIPCurrentSubnetMask_Object((1,3,6,1,4,1,494,10,4,3),_MadgeIPCurrentSubnetMask_Type())
madgeIPCurrentSubnetMask.setMaxAccess(_B)
if mibBuilder.loadTexts:madgeIPCurrentSubnetMask.setStatus(_A)
class _MadgeIPDiscoveryMethod_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('not-discovered',1),('via-config',2),('via-bootp',3),('via-rarp',4)))
_MadgeIPDiscoveryMethod_Type.__name__=_D
_MadgeIPDiscoveryMethod_Object=MibScalar
madgeIPDiscoveryMethod=_MadgeIPDiscoveryMethod_Object((1,3,6,1,4,1,494,10,4,4),_MadgeIPDiscoveryMethod_Type())
madgeIPDiscoveryMethod.setMaxAccess(_B)
if mibBuilder.loadTexts:madgeIPDiscoveryMethod.setStatus(_A)
class _MadgeIPBootpEnabled_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_H,1),(_I,2),(_T,3)))
_MadgeIPBootpEnabled_Type.__name__=_D
_MadgeIPBootpEnabled_Object=MibScalar
madgeIPBootpEnabled=_MadgeIPBootpEnabled_Object((1,3,6,1,4,1,494,10,4,5),_MadgeIPBootpEnabled_Type())
madgeIPBootpEnabled.setMaxAccess(_C)
if mibBuilder.loadTexts:madgeIPBootpEnabled.setStatus(_A)
class _MadgeIPRarpEnabled_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_H,1),(_I,2),(_T,3)))
_MadgeIPRarpEnabled_Type.__name__=_D
_MadgeIPRarpEnabled_Object=MibScalar
madgeIPRarpEnabled=_MadgeIPRarpEnabled_Object((1,3,6,1,4,1,494,10,4,6),_MadgeIPRarpEnabled_Type())
madgeIPRarpEnabled.setMaxAccess(_C)
if mibBuilder.loadTexts:madgeIPRarpEnabled.setStatus(_A)
_MadgeVersion_ObjectIdentity=ObjectIdentity
madgeVersion=_MadgeVersion_ObjectIdentity((1,3,6,1,4,1,494,10,5))
_MadgeVersionTable_Object=MibTable
madgeVersionTable=_MadgeVersionTable_Object((1,3,6,1,4,1,494,10,5,1))
if mibBuilder.loadTexts:madgeVersionTable.setStatus(_A)
_MadgeVersionEntry_Object=MibTableRow
madgeVersionEntry=_MadgeVersionEntry_Object((1,3,6,1,4,1,494,10,5,1,1))
madgeVersionEntry.setIndexNames((0,_G,_U))
if mibBuilder.loadTexts:madgeVersionEntry.setStatus(_A)
_MadgeVersionIndex_Type=Integer32
_MadgeVersionIndex_Object=MibTableColumn
madgeVersionIndex=_MadgeVersionIndex_Object((1,3,6,1,4,1,494,10,5,1,1,1),_MadgeVersionIndex_Type())
madgeVersionIndex.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:madgeVersionIndex.setStatus(_A)
class _MadgeVersionDescription_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_MadgeVersionDescription_Type.__name__=_E
_MadgeVersionDescription_Object=MibTableColumn
madgeVersionDescription=_MadgeVersionDescription_Object((1,3,6,1,4,1,494,10,5,1,1,2),_MadgeVersionDescription_Type())
madgeVersionDescription.setMaxAccess(_B)
if mibBuilder.loadTexts:madgeVersionDescription.setStatus(_A)
class _MadgeVersionLocation_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_MadgeVersionLocation_Type.__name__=_E
_MadgeVersionLocation_Object=MibTableColumn
madgeVersionLocation=_MadgeVersionLocation_Object((1,3,6,1,4,1,494,10,5,1,1,3),_MadgeVersionLocation_Type())
madgeVersionLocation.setMaxAccess(_B)
if mibBuilder.loadTexts:madgeVersionLocation.setStatus(_A)
class _MadgeVersionNumber_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(3,3));fixedLength=3
_MadgeVersionNumber_Type.__name__=_F
_MadgeVersionNumber_Object=MibTableColumn
madgeVersionNumber=_MadgeVersionNumber_Object((1,3,6,1,4,1,494,10,5,1,1,4),_MadgeVersionNumber_Type())
madgeVersionNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:madgeVersionNumber.setStatus(_A)
class _MadgeVersionType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*(('flash',1),('boot-fixed',2),('boot-updateable',3),('hardware-fixed',4),('hardware-upgradeable',5),('other',6)))
_MadgeVersionType_Type.__name__=_D
_MadgeVersionType_Object=MibTableColumn
madgeVersionType=_MadgeVersionType_Object((1,3,6,1,4,1,494,10,5,1,1,5),_MadgeVersionType_Type())
madgeVersionType.setMaxAccess(_B)
if mibBuilder.loadTexts:madgeVersionType.setStatus(_A)
_MadgeVersionCount_Type=Integer32
_MadgeVersionCount_Object=MibScalar
madgeVersionCount=_MadgeVersionCount_Object((1,3,6,1,4,1,494,10,5,2),_MadgeVersionCount_Type())
madgeVersionCount.setMaxAccess(_B)
if mibBuilder.loadTexts:madgeVersionCount.setStatus(_A)
mibBuilder.exportSymbols(_G,**{_E:DisplayString,'MacAddress':MacAddress,'madge':madge,'madgeBox':madgeBox,'madgeConfig':madgeConfig,'madgeConfigIPAddress':madgeConfigIPAddress,'madgeConfigIPGateway':madgeConfigIPGateway,'madgeConfigIPSubnetMask':madgeConfigIPSubnetMask,'madgeConfigSerialNumber':madgeConfigSerialNumber,'madgeConfigMCodeVersion':madgeConfigMCodeVersion,'madgeConfigBCodeVersion':madgeConfigBCodeVersion,'madgeConfigMCodeFilename':madgeConfigMCodeFilename,'madgeConfigDeviceHealth':madgeConfigDeviceHealth,'madgeConfigAdminStatus':madgeConfigAdminStatus,'madgeConfigPassword':madgeConfigPassword,'madgeConfigLinkTest':madgeConfigLinkTest,'madgeConfigOperStatus':madgeConfigOperStatus,'madgeConfigEraseFlashVersion':madgeConfigEraseFlashVersion,'madgeConfigDefaultFlashVersion':madgeConfigDefaultFlashVersion,'madgeSecure':madgeSecure,'madgeSecureCurrentTableSize':madgeSecureCurrentTableSize,'madgeSecureCurrentTimeout':madgeSecureCurrentTimeout,'madgeSecureCurrentTable':madgeSecureCurrentTable,'madgeSecureCurrentEntry':madgeSecureCurrentEntry,_Q:madgeSecureCurrentIndex,'madgeSecureCurrentType':madgeSecureCurrentType,'madgeSecureCurrentAddress':madgeSecureCurrentAddress,'madgeSecureCurrentUpdateTime':madgeSecureCurrentUpdateTime,'madgeSecureCurrentIPAddress':madgeSecureCurrentIPAddress,'madgeSecureAllowedEnabled':madgeSecureAllowedEnabled,'madgeSecureAllowedTableSize':madgeSecureAllowedTableSize,'madgeSecureAllowedTable':madgeSecureAllowedTable,'madgeSecureAllowedEntry':madgeSecureAllowedEntry,_R:madgeSecureAllowedIndex,'madgeSecureAllowedType':madgeSecureAllowedType,'madgeSecureAllowedAddress':madgeSecureAllowedAddress,'madgeSecureAllowedIPAddress':madgeSecureAllowedIPAddress,'madgeSecureTrapDestEnabled':madgeSecureTrapDestEnabled,'madgeSecureTrapDestTableSize':madgeSecureTrapDestTableSize,'madgeSecureTrapDestTable':madgeSecureTrapDestTable,'madgeSecureTrapDestEntry':madgeSecureTrapDestEntry,_S:madgeSecureTrapDestIndex,'madgeSecureTrapDestType':madgeSecureTrapDestType,'madgeSecureTrapDestAddress':madgeSecureTrapDestAddress,'madgeSecureTrapDestIPAddress':madgeSecureTrapDestIPAddress,'madgeDownload':madgeDownload,'madgeDownloadIPAddress':madgeDownloadIPAddress,'madgeDownloadIPGateway':madgeDownloadIPGateway,'madgeDownloadIPXAddress':madgeDownloadIPXAddress,'madgeDownloadNodeAddress':madgeDownloadNodeAddress,'madgeDownloadFileName':madgeDownloadFileName,'madgeDownloadDestination':madgeDownloadDestination,'madgeDownloadState':madgeDownloadState,'madgeDownloadFailureCode':madgeDownloadFailureCode,'madgeDownloadStatusText':madgeDownloadStatusText,'madgeDownloadSize':madgeDownloadSize,'madgeIP':madgeIP,'madgeIPCurrentAddress':madgeIPCurrentAddress,'madgeIPCurrentGateway':madgeIPCurrentGateway,'madgeIPCurrentSubnetMask':madgeIPCurrentSubnetMask,'madgeIPDiscoveryMethod':madgeIPDiscoveryMethod,'madgeIPBootpEnabled':madgeIPBootpEnabled,'madgeIPRarpEnabled':madgeIPRarpEnabled,'madgeVersion':madgeVersion,'madgeVersionTable':madgeVersionTable,'madgeVersionEntry':madgeVersionEntry,_U:madgeVersionIndex,'madgeVersionDescription':madgeVersionDescription,'madgeVersionLocation':madgeVersionLocation,'madgeVersionNumber':madgeVersionNumber,'madgeVersionType':madgeVersionType,'madgeVersionCount':madgeVersionCount})