_b='rlDhcpClInformationTftpServerListPriority'
_a='rlDhcpClInformationTftpServerListIfIndex'
_Z='rlDhcpClInformationDnsServerListPriority'
_Y='rlDhcpClInformationDnsServerListIfIndex'
_X='rlDhcpClInformationIfIndex'
_W='rlDhcpClManualAutoConfigDataIndex'
_V='quitNoTftpOutgoingInterface'
_U='openingIndirectFile'
_T='noData'
_S='manual'
_R='rlDhcpApprovalActionMask'
_Q='rlDhcpApprovalActionAddress'
_P='rlDhcpApprovalActionIfIndex'
_O='rlDhcpApprovalWaitingIfIndex'
_N='read-create'
_M='rlDhcpClActionIfIndex'
_L='ifIndex'
_K='IF-MIB'
_J='none'
_I='SnmpAdminString'
_H='scp'
_G='not-accessible'
_F='DisplayString'
_E='Integer32'
_D='Dell-DHCPCL-MIB'
_C='read-write'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
rnd,=mibBuilder.importSymbols('Dell-MIB','rnd')
InterfaceIndex,ifIndex=mibBuilder.importSymbols(_K,'InterfaceIndex',_L)
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress','InetAddressType')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB',_I)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC',_F,'PhysAddress','RowStatus','TextualConvention','TruthValue')
rlDhcpCl=ModuleIdentity((1,3,6,1,4,1,89,76))
if mibBuilder.loadTexts:rlDhcpCl.setRevisions(('2007-01-02 00:00',))
_RlDhcpClActionTable_Object=MibTable
rlDhcpClActionTable=_RlDhcpClActionTable_Object((1,3,6,1,4,1,89,76,3))
if mibBuilder.loadTexts:rlDhcpClActionTable.setStatus(_A)
_RlDhcpClActionEntry_Object=MibTableRow
rlDhcpClActionEntry=_RlDhcpClActionEntry_Object((1,3,6,1,4,1,89,76,3,1))
rlDhcpClActionEntry.setIndexNames((0,_D,_M))
if mibBuilder.loadTexts:rlDhcpClActionEntry.setStatus(_A)
_RlDhcpClActionIfIndex_Type=InterfaceIndex
_RlDhcpClActionIfIndex_Object=MibTableColumn
rlDhcpClActionIfIndex=_RlDhcpClActionIfIndex_Object((1,3,6,1,4,1,89,76,3,1,1),_RlDhcpClActionIfIndex_Type())
rlDhcpClActionIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:rlDhcpClActionIfIndex.setStatus(_A)
_RlDhcpClActionStatus_Type=RowStatus
_RlDhcpClActionStatus_Object=MibTableColumn
rlDhcpClActionStatus=_RlDhcpClActionStatus_Object((1,3,6,1,4,1,89,76,3,1,2),_RlDhcpClActionStatus_Type())
rlDhcpClActionStatus.setMaxAccess(_N)
if mibBuilder.loadTexts:rlDhcpClActionStatus.setStatus(_A)
class _RlDhcpClActionHostName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,20))
_RlDhcpClActionHostName_Type.__name__=_I
_RlDhcpClActionHostName_Object=MibTableColumn
rlDhcpClActionHostName=_RlDhcpClActionHostName_Object((1,3,6,1,4,1,89,76,3,1,3),_RlDhcpClActionHostName_Type())
rlDhcpClActionHostName.setMaxAccess(_N)
if mibBuilder.loadTexts:rlDhcpClActionHostName.setStatus(_A)
_RlDhcpApprovalEnabled_Type=TruthValue
_RlDhcpApprovalEnabled_Object=MibScalar
rlDhcpApprovalEnabled=_RlDhcpApprovalEnabled_Object((1,3,6,1,4,1,89,76,4),_RlDhcpApprovalEnabled_Type())
rlDhcpApprovalEnabled.setMaxAccess(_B)
if mibBuilder.loadTexts:rlDhcpApprovalEnabled.setStatus(_A)
_RlDhcpApprovalWaitingTable_Object=MibTable
rlDhcpApprovalWaitingTable=_RlDhcpApprovalWaitingTable_Object((1,3,6,1,4,1,89,76,5))
if mibBuilder.loadTexts:rlDhcpApprovalWaitingTable.setStatus(_A)
_RlDhcpApprovalWaitingEntry_Object=MibTableRow
rlDhcpApprovalWaitingEntry=_RlDhcpApprovalWaitingEntry_Object((1,3,6,1,4,1,89,76,5,1))
rlDhcpApprovalWaitingEntry.setIndexNames((0,_D,_O))
if mibBuilder.loadTexts:rlDhcpApprovalWaitingEntry.setStatus(_A)
_RlDhcpApprovalWaitingIfIndex_Type=InterfaceIndex
_RlDhcpApprovalWaitingIfIndex_Object=MibTableColumn
rlDhcpApprovalWaitingIfIndex=_RlDhcpApprovalWaitingIfIndex_Object((1,3,6,1,4,1,89,76,5,1,1),_RlDhcpApprovalWaitingIfIndex_Type())
rlDhcpApprovalWaitingIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:rlDhcpApprovalWaitingIfIndex.setStatus(_A)
_RlDhcpApprovalWaitingAddress_Type=IpAddress
_RlDhcpApprovalWaitingAddress_Object=MibTableColumn
rlDhcpApprovalWaitingAddress=_RlDhcpApprovalWaitingAddress_Object((1,3,6,1,4,1,89,76,5,1,2),_RlDhcpApprovalWaitingAddress_Type())
rlDhcpApprovalWaitingAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:rlDhcpApprovalWaitingAddress.setStatus(_A)
_RlDhcpApprovalWaitingMask_Type=IpAddress
_RlDhcpApprovalWaitingMask_Object=MibTableColumn
rlDhcpApprovalWaitingMask=_RlDhcpApprovalWaitingMask_Object((1,3,6,1,4,1,89,76,5,1,3),_RlDhcpApprovalWaitingMask_Type())
rlDhcpApprovalWaitingMask.setMaxAccess(_B)
if mibBuilder.loadTexts:rlDhcpApprovalWaitingMask.setStatus(_A)
_RlDhcpApprovalWaitingGateway_Type=IpAddress
_RlDhcpApprovalWaitingGateway_Object=MibTableColumn
rlDhcpApprovalWaitingGateway=_RlDhcpApprovalWaitingGateway_Object((1,3,6,1,4,1,89,76,5,1,4),_RlDhcpApprovalWaitingGateway_Type())
rlDhcpApprovalWaitingGateway.setMaxAccess(_B)
if mibBuilder.loadTexts:rlDhcpApprovalWaitingGateway.setStatus(_A)
_RlDhcpApprovalActionTable_Object=MibTable
rlDhcpApprovalActionTable=_RlDhcpApprovalActionTable_Object((1,3,6,1,4,1,89,76,6))
if mibBuilder.loadTexts:rlDhcpApprovalActionTable.setStatus(_A)
_RlDhcpApprovalActionEntry_Object=MibTableRow
rlDhcpApprovalActionEntry=_RlDhcpApprovalActionEntry_Object((1,3,6,1,4,1,89,76,6,1))
rlDhcpApprovalActionEntry.setIndexNames((0,_D,_P),(0,_D,_Q),(0,_D,_R))
if mibBuilder.loadTexts:rlDhcpApprovalActionEntry.setStatus(_A)
_RlDhcpApprovalActionIfIndex_Type=InterfaceIndex
_RlDhcpApprovalActionIfIndex_Object=MibTableColumn
rlDhcpApprovalActionIfIndex=_RlDhcpApprovalActionIfIndex_Object((1,3,6,1,4,1,89,76,6,1,1),_RlDhcpApprovalActionIfIndex_Type())
rlDhcpApprovalActionIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:rlDhcpApprovalActionIfIndex.setStatus(_A)
_RlDhcpApprovalActionAddress_Type=IpAddress
_RlDhcpApprovalActionAddress_Object=MibTableColumn
rlDhcpApprovalActionAddress=_RlDhcpApprovalActionAddress_Object((1,3,6,1,4,1,89,76,6,1,2),_RlDhcpApprovalActionAddress_Type())
rlDhcpApprovalActionAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:rlDhcpApprovalActionAddress.setStatus(_A)
_RlDhcpApprovalActionMask_Type=IpAddress
_RlDhcpApprovalActionMask_Object=MibTableColumn
rlDhcpApprovalActionMask=_RlDhcpApprovalActionMask_Object((1,3,6,1,4,1,89,76,6,1,3),_RlDhcpApprovalActionMask_Type())
rlDhcpApprovalActionMask.setMaxAccess(_B)
if mibBuilder.loadTexts:rlDhcpApprovalActionMask.setStatus(_A)
_RlDhcpApprovalActionApprove_Type=TruthValue
_RlDhcpApprovalActionApprove_Object=MibTableColumn
rlDhcpApprovalActionApprove=_RlDhcpApprovalActionApprove_Object((1,3,6,1,4,1,89,76,6,1,4),_RlDhcpApprovalActionApprove_Type())
rlDhcpApprovalActionApprove.setMaxAccess(_C)
if mibBuilder.loadTexts:rlDhcpApprovalActionApprove.setStatus(_A)
_RlDhcpClCommandTable_Object=MibTable
rlDhcpClCommandTable=_RlDhcpClCommandTable_Object((1,3,6,1,4,1,89,76,7))
if mibBuilder.loadTexts:rlDhcpClCommandTable.setStatus(_A)
_RlDhcpClCommandEntry_Object=MibTableRow
rlDhcpClCommandEntry=_RlDhcpClCommandEntry_Object((1,3,6,1,4,1,89,76,7,1))
rlDhcpClCommandEntry.setIndexNames((0,_K,_L))
if mibBuilder.loadTexts:rlDhcpClCommandEntry.setStatus(_A)
class _RlDhcpClCommandAction_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_J,0),('renew',1),('renewForceAutoconfig',2)))
_RlDhcpClCommandAction_Type.__name__=_E
_RlDhcpClCommandAction_Object=MibTableColumn
rlDhcpClCommandAction=_RlDhcpClCommandAction_Object((1,3,6,1,4,1,89,76,7,1,2),_RlDhcpClCommandAction_Type())
rlDhcpClCommandAction.setMaxAccess(_C)
if mibBuilder.loadTexts:rlDhcpClCommandAction.setStatus(_A)
class _RlDhcpClConfigurationFileName_Type(DisplayString):defaultValue=OctetString('')
_RlDhcpClConfigurationFileName_Type.__name__=_F
_RlDhcpClConfigurationFileName_Object=MibScalar
rlDhcpClConfigurationFileName=_RlDhcpClConfigurationFileName_Object((1,3,6,1,4,1,89,76,8),_RlDhcpClConfigurationFileName_Type())
rlDhcpClConfigurationFileName.setMaxAccess(_C)
if mibBuilder.loadTexts:rlDhcpClConfigurationFileName.setStatus(_A)
class _RlDhcpClOption67Enable_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('enable',1),('disable',2)))
_RlDhcpClOption67Enable_Type.__name__=_E
_RlDhcpClOption67Enable_Object=MibScalar
rlDhcpClOption67Enable=_RlDhcpClOption67Enable_Object((1,3,6,1,4,1,89,76,9),_RlDhcpClOption67Enable_Type())
rlDhcpClOption67Enable.setMaxAccess(_C)
if mibBuilder.loadTexts:rlDhcpClOption67Enable.setStatus(_A)
_RlDhcpClManualTftpServerAddress_Type=IpAddress
_RlDhcpClManualTftpServerAddress_Object=MibScalar
rlDhcpClManualTftpServerAddress=_RlDhcpClManualTftpServerAddress_Object((1,3,6,1,4,1,89,76,10),_RlDhcpClManualTftpServerAddress_Type())
rlDhcpClManualTftpServerAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:rlDhcpClManualTftpServerAddress.setStatus(_A)
_RlDhcpClSelectedTftpServerAddress_Type=IpAddress
_RlDhcpClSelectedTftpServerAddress_Object=MibScalar
rlDhcpClSelectedTftpServerAddress=_RlDhcpClSelectedTftpServerAddress_Object((1,3,6,1,4,1,89,76,11),_RlDhcpClSelectedTftpServerAddress_Type())
rlDhcpClSelectedTftpServerAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:rlDhcpClSelectedTftpServerAddress.setStatus(_A)
class _RlDhcpClSelectedTftpServerAddressOrigin_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10)));namedValues=NamedValues(*(('sname',1),('option66',2),('option150',3),('option129',4),('siaddr',5),(_S,6),('unknown',7),(_J,8),('optionv6-59',9),('broadcastReply',10)))
_RlDhcpClSelectedTftpServerAddressOrigin_Type.__name__=_E
_RlDhcpClSelectedTftpServerAddressOrigin_Object=MibScalar
rlDhcpClSelectedTftpServerAddressOrigin=_RlDhcpClSelectedTftpServerAddressOrigin_Object((1,3,6,1,4,1,89,76,12),_RlDhcpClSelectedTftpServerAddressOrigin_Type())
rlDhcpClSelectedTftpServerAddressOrigin.setMaxAccess(_B)
if mibBuilder.loadTexts:rlDhcpClSelectedTftpServerAddressOrigin.setStatus(_A)
class _RlDhcpClManualConfigurationFileName_Type(DisplayString):defaultValue=OctetString('')
_RlDhcpClManualConfigurationFileName_Type.__name__=_F
_RlDhcpClManualConfigurationFileName_Object=MibScalar
rlDhcpClManualConfigurationFileName=_RlDhcpClManualConfigurationFileName_Object((1,3,6,1,4,1,89,76,13),_RlDhcpClManualConfigurationFileName_Type())
rlDhcpClManualConfigurationFileName.setMaxAccess(_C)
if mibBuilder.loadTexts:rlDhcpClManualConfigurationFileName.setStatus(_A)
_RlDhcpClSelectedConfigurationFileName_Type=DisplayString
_RlDhcpClSelectedConfigurationFileName_Object=MibScalar
rlDhcpClSelectedConfigurationFileName=_RlDhcpClSelectedConfigurationFileName_Object((1,3,6,1,4,1,89,76,14),_RlDhcpClSelectedConfigurationFileName_Type())
rlDhcpClSelectedConfigurationFileName.setMaxAccess(_B)
if mibBuilder.loadTexts:rlDhcpClSelectedConfigurationFileName.setStatus(_A)
class _RlDhcpClSelectedConfigurationFileNameOrigin_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*(('file',1),('option67',2),(_S,3),(_J,4),('hostname',5),('defaultConfigFile',6),('optionv6-60',7)))
_RlDhcpClSelectedConfigurationFileNameOrigin_Type.__name__=_E
_RlDhcpClSelectedConfigurationFileNameOrigin_Object=MibScalar
rlDhcpClSelectedConfigurationFileNameOrigin=_RlDhcpClSelectedConfigurationFileNameOrigin_Object((1,3,6,1,4,1,89,76,15),_RlDhcpClSelectedConfigurationFileNameOrigin_Type())
rlDhcpClSelectedConfigurationFileNameOrigin.setMaxAccess(_B)
if mibBuilder.loadTexts:rlDhcpClSelectedConfigurationFileNameOrigin.setStatus(_A)
class _RlDhcpClEnabledByDefaultRemovedIfindex_Type(Integer32):defaultValue=0
_RlDhcpClEnabledByDefaultRemovedIfindex_Type.__name__=_E
_RlDhcpClEnabledByDefaultRemovedIfindex_Object=MibScalar
rlDhcpClEnabledByDefaultRemovedIfindex=_RlDhcpClEnabledByDefaultRemovedIfindex_Object((1,3,6,1,4,1,89,76,16),_RlDhcpClEnabledByDefaultRemovedIfindex_Type())
rlDhcpClEnabledByDefaultRemovedIfindex.setMaxAccess(_C)
if mibBuilder.loadTexts:rlDhcpClEnabledByDefaultRemovedIfindex.setStatus(_A)
_RlDhcpClAutoUpdateEnabled_Type=TruthValue
_RlDhcpClAutoUpdateEnabled_Object=MibScalar
rlDhcpClAutoUpdateEnabled=_RlDhcpClAutoUpdateEnabled_Object((1,3,6,1,4,1,89,76,17),_RlDhcpClAutoUpdateEnabled_Type())
rlDhcpClAutoUpdateEnabled.setMaxAccess(_C)
if mibBuilder.loadTexts:rlDhcpClAutoUpdateEnabled.setStatus(_A)
class _RlDhcpClAutoUpdateStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18)));namedValues=NamedValues(*((_T,1),(_U,2),('downloadedIndirectFile',3),('startDownloadImageFile',4),('failedToDownloadImageFile',5),('quitFileContentsLenZero',6),('quitImageFileNameLenZero',7),('quitVersionAlreadyUpdated',8),('quitIndirectFileNotFound',9),('quitImageFileNotFound',10),('quitImageVersionNotSupported',11),(_V,12),('quitUsbSetupFileOpenError',13),('quitUsbSetupFileFormatError',14),('quitUsbSetupFileReadWriteError',15),('quitUsbSetupFileSetIpAddrError',16),('quitUsbSetupFileImageFileNotExist',17),('quitUsbSetupFileConfigFileNotExist',18)))
_RlDhcpClAutoUpdateStatus_Type.__name__=_E
_RlDhcpClAutoUpdateStatus_Object=MibScalar
rlDhcpClAutoUpdateStatus=_RlDhcpClAutoUpdateStatus_Object((1,3,6,1,4,1,89,76,18),_RlDhcpClAutoUpdateStatus_Type())
rlDhcpClAutoUpdateStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:rlDhcpClAutoUpdateStatus.setStatus(_A)
_RlDhcpClAutoConfigForce_Type=TruthValue
_RlDhcpClAutoConfigForce_Object=MibScalar
rlDhcpClAutoConfigForce=_RlDhcpClAutoConfigForce_Object((1,3,6,1,4,1,89,76,19),_RlDhcpClAutoConfigForce_Type())
rlDhcpClAutoConfigForce.setMaxAccess(_C)
if mibBuilder.loadTexts:rlDhcpClAutoConfigForce.setStatus(_A)
_RlDhcpClAutoConfigAutoSave_Type=TruthValue
_RlDhcpClAutoConfigAutoSave_Object=MibScalar
rlDhcpClAutoConfigAutoSave=_RlDhcpClAutoConfigAutoSave_Object((1,3,6,1,4,1,89,76,20),_RlDhcpClAutoConfigAutoSave_Type())
rlDhcpClAutoConfigAutoSave.setMaxAccess(_C)
if mibBuilder.loadTexts:rlDhcpClAutoConfigAutoSave.setStatus(_A)
class _RlDhcpClAutoConfigStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21)));namedValues=NamedValues(*((_T,1),('openingDhcpConfigFile',2),(_U,3),('searchingHostnameInIndirectFile',4),('openingHostnameConfigFile',5),('openingHostnameCfgFile',6),('openingDefaultConfigFile',7),('downloadingConfigFile',8),('savingConfigInStartupCDB',9),('quitDhcpFileNotGivenOrNotExists',10),('quitFailedToFindAnyExistingConfigFile',11),('quitConfigFileContentsLenZero',12),('quitConfigFileDownloadFailed',13),('quitConditionsForAutoConfigChanged',14),('quitSelectedConfigFileNameUpdateFailed',15),('quitSelectedConfigFileNameOriginUpdateFailed',16),('quitSelectedTftpServerAddressUpdateFailed',17),('quitSelectedTftpServerAddressOriginUpdateFailed',18),('quitCopyRunningToStartupFailed',19),(_V,20),('finishedSuccessfully',21)))
_RlDhcpClAutoConfigStatus_Type.__name__=_E
_RlDhcpClAutoConfigStatus_Object=MibScalar
rlDhcpClAutoConfigStatus=_RlDhcpClAutoConfigStatus_Object((1,3,6,1,4,1,89,76,21),_RlDhcpClAutoConfigStatus_Type())
rlDhcpClAutoConfigStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:rlDhcpClAutoConfigStatus.setStatus(_A)
class _RlDhcpClAutoConfigProtocol_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('tftp',1),(_H,2),('auto',3)))
_RlDhcpClAutoConfigProtocol_Type.__name__=_E
_RlDhcpClAutoConfigProtocol_Object=MibScalar
rlDhcpClAutoConfigProtocol=_RlDhcpClAutoConfigProtocol_Object((1,3,6,1,4,1,89,76,22),_RlDhcpClAutoConfigProtocol_Type())
rlDhcpClAutoConfigProtocol.setMaxAccess(_C)
if mibBuilder.loadTexts:rlDhcpClAutoConfigProtocol.setStatus(_A)
class _RlDhcpClAutoConfigScpFileExtention_Type(DisplayString):defaultValue=OctetString(_H);subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,128))
_RlDhcpClAutoConfigScpFileExtention_Type.__name__=_F
_RlDhcpClAutoConfigScpFileExtention_Object=MibScalar
rlDhcpClAutoConfigScpFileExtention=_RlDhcpClAutoConfigScpFileExtention_Object((1,3,6,1,4,1,89,76,23),_RlDhcpClAutoConfigScpFileExtention_Type())
rlDhcpClAutoConfigScpFileExtention.setMaxAccess(_C)
if mibBuilder.loadTexts:rlDhcpClAutoConfigScpFileExtention.setStatus(_A)
_RlDhcpClSelectedTftpServerInetAddressType_Type=InetAddressType
_RlDhcpClSelectedTftpServerInetAddressType_Object=MibScalar
rlDhcpClSelectedTftpServerInetAddressType=_RlDhcpClSelectedTftpServerInetAddressType_Object((1,3,6,1,4,1,89,76,24),_RlDhcpClSelectedTftpServerInetAddressType_Type())
rlDhcpClSelectedTftpServerInetAddressType.setMaxAccess(_B)
if mibBuilder.loadTexts:rlDhcpClSelectedTftpServerInetAddressType.setStatus(_A)
_RlDhcpClSelectedTftpServerInetAddress_Type=InetAddress
_RlDhcpClSelectedTftpServerInetAddress_Object=MibScalar
rlDhcpClSelectedTftpServerInetAddress=_RlDhcpClSelectedTftpServerInetAddress_Object((1,3,6,1,4,1,89,76,25),_RlDhcpClSelectedTftpServerInetAddress_Type())
rlDhcpClSelectedTftpServerInetAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:rlDhcpClSelectedTftpServerInetAddress.setStatus(_A)
_RlDhcpClManualAutoConfigDataTable_Object=MibTable
rlDhcpClManualAutoConfigDataTable=_RlDhcpClManualAutoConfigDataTable_Object((1,3,6,1,4,1,89,76,26))
if mibBuilder.loadTexts:rlDhcpClManualAutoConfigDataTable.setStatus(_A)
_RlDhcpClManualAutoConfigDataEntry_Object=MibTableRow
rlDhcpClManualAutoConfigDataEntry=_RlDhcpClManualAutoConfigDataEntry_Object((1,3,6,1,4,1,89,76,26,1))
rlDhcpClManualAutoConfigDataEntry.setIndexNames((0,_D,_W))
if mibBuilder.loadTexts:rlDhcpClManualAutoConfigDataEntry.setStatus(_A)
_RlDhcpClManualAutoConfigDataIndex_Type=Integer32
_RlDhcpClManualAutoConfigDataIndex_Object=MibTableColumn
rlDhcpClManualAutoConfigDataIndex=_RlDhcpClManualAutoConfigDataIndex_Object((1,3,6,1,4,1,89,76,26,1,1),_RlDhcpClManualAutoConfigDataIndex_Type())
rlDhcpClManualAutoConfigDataIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:rlDhcpClManualAutoConfigDataIndex.setStatus(_A)
_RlDhcpClManualServerInetAddressType_Type=InetAddressType
_RlDhcpClManualServerInetAddressType_Object=MibTableColumn
rlDhcpClManualServerInetAddressType=_RlDhcpClManualServerInetAddressType_Object((1,3,6,1,4,1,89,76,26,1,2),_RlDhcpClManualServerInetAddressType_Type())
rlDhcpClManualServerInetAddressType.setMaxAccess(_C)
if mibBuilder.loadTexts:rlDhcpClManualServerInetAddressType.setStatus(_A)
_RlDhcpClManualServerInetAddress_Type=InetAddress
_RlDhcpClManualServerInetAddress_Object=MibTableColumn
rlDhcpClManualServerInetAddress=_RlDhcpClManualServerInetAddress_Object((1,3,6,1,4,1,89,76,26,1,3),_RlDhcpClManualServerInetAddress_Type())
rlDhcpClManualServerInetAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:rlDhcpClManualServerInetAddress.setStatus(_A)
_RlDhcpClManualImageIndirectFileName_Type=DisplayString
_RlDhcpClManualImageIndirectFileName_Object=MibTableColumn
rlDhcpClManualImageIndirectFileName=_RlDhcpClManualImageIndirectFileName_Object((1,3,6,1,4,1,89,76,26,1,4),_RlDhcpClManualImageIndirectFileName_Type())
rlDhcpClManualImageIndirectFileName.setMaxAccess(_C)
if mibBuilder.loadTexts:rlDhcpClManualImageIndirectFileName.setStatus(_A)
_RlDhcpClInformationTable_Object=MibTable
rlDhcpClInformationTable=_RlDhcpClInformationTable_Object((1,3,6,1,4,1,89,76,27))
if mibBuilder.loadTexts:rlDhcpClInformationTable.setStatus(_A)
_RlDhcpClInformationEntry_Object=MibTableRow
rlDhcpClInformationEntry=_RlDhcpClInformationEntry_Object((1,3,6,1,4,1,89,76,27,1))
rlDhcpClInformationEntry.setIndexNames((0,_D,_X))
if mibBuilder.loadTexts:rlDhcpClInformationEntry.setStatus(_A)
_RlDhcpClInformationIfIndex_Type=InterfaceIndex
_RlDhcpClInformationIfIndex_Object=MibTableColumn
rlDhcpClInformationIfIndex=_RlDhcpClInformationIfIndex_Object((1,3,6,1,4,1,89,76,27,1,1),_RlDhcpClInformationIfIndex_Type())
rlDhcpClInformationIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:rlDhcpClInformationIfIndex.setStatus(_A)
_RlDhcpClInformationIpAddress_Type=IpAddress
_RlDhcpClInformationIpAddress_Object=MibTableColumn
rlDhcpClInformationIpAddress=_RlDhcpClInformationIpAddress_Object((1,3,6,1,4,1,89,76,27,1,2),_RlDhcpClInformationIpAddress_Type())
rlDhcpClInformationIpAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:rlDhcpClInformationIpAddress.setStatus(_A)
_RlDhcpClInformationIpMask_Type=IpAddress
_RlDhcpClInformationIpMask_Object=MibTableColumn
rlDhcpClInformationIpMask=_RlDhcpClInformationIpMask_Object((1,3,6,1,4,1,89,76,27,1,3),_RlDhcpClInformationIpMask_Type())
rlDhcpClInformationIpMask.setMaxAccess(_B)
if mibBuilder.loadTexts:rlDhcpClInformationIpMask.setStatus(_A)
_RlDhcpClInformationT1_Type=Unsigned32
_RlDhcpClInformationT1_Object=MibTableColumn
rlDhcpClInformationT1=_RlDhcpClInformationT1_Object((1,3,6,1,4,1,89,76,27,1,4),_RlDhcpClInformationT1_Type())
rlDhcpClInformationT1.setMaxAccess(_B)
if mibBuilder.loadTexts:rlDhcpClInformationT1.setStatus(_A)
_RlDhcpClInformationT2_Type=Unsigned32
_RlDhcpClInformationT2_Object=MibTableColumn
rlDhcpClInformationT2=_RlDhcpClInformationT2_Object((1,3,6,1,4,1,89,76,27,1,5),_RlDhcpClInformationT2_Type())
rlDhcpClInformationT2.setMaxAccess(_B)
if mibBuilder.loadTexts:rlDhcpClInformationT2.setStatus(_A)
_RlDhcpClInformationDefaultGateway_Type=IpAddress
_RlDhcpClInformationDefaultGateway_Object=MibTableColumn
rlDhcpClInformationDefaultGateway=_RlDhcpClInformationDefaultGateway_Object((1,3,6,1,4,1,89,76,27,1,6),_RlDhcpClInformationDefaultGateway_Type())
rlDhcpClInformationDefaultGateway.setMaxAccess(_B)
if mibBuilder.loadTexts:rlDhcpClInformationDefaultGateway.setStatus(_A)
class _RlDhcpClInformationHostName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,160))
_RlDhcpClInformationHostName_Type.__name__=_I
_RlDhcpClInformationHostName_Object=MibTableColumn
rlDhcpClInformationHostName=_RlDhcpClInformationHostName_Object((1,3,6,1,4,1,89,76,27,1,7),_RlDhcpClInformationHostName_Type())
rlDhcpClInformationHostName.setMaxAccess(_B)
if mibBuilder.loadTexts:rlDhcpClInformationHostName.setStatus(_A)
class _RlDhcpClInformationDomainName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,160))
_RlDhcpClInformationDomainName_Type.__name__=_F
_RlDhcpClInformationDomainName_Object=MibTableColumn
rlDhcpClInformationDomainName=_RlDhcpClInformationDomainName_Object((1,3,6,1,4,1,89,76,27,1,8),_RlDhcpClInformationDomainName_Type())
rlDhcpClInformationDomainName.setMaxAccess(_B)
if mibBuilder.loadTexts:rlDhcpClInformationDomainName.setStatus(_A)
class _RlDhcpClInformationTftpServerName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,160))
_RlDhcpClInformationTftpServerName_Type.__name__=_F
_RlDhcpClInformationTftpServerName_Object=MibTableColumn
rlDhcpClInformationTftpServerName=_RlDhcpClInformationTftpServerName_Object((1,3,6,1,4,1,89,76,27,1,9),_RlDhcpClInformationTftpServerName_Type())
rlDhcpClInformationTftpServerName.setMaxAccess(_B)
if mibBuilder.loadTexts:rlDhcpClInformationTftpServerName.setStatus(_A)
class _RlDhcpClInformationTftpFileName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,160))
_RlDhcpClInformationTftpFileName_Type.__name__=_F
_RlDhcpClInformationTftpFileName_Object=MibTableColumn
rlDhcpClInformationTftpFileName=_RlDhcpClInformationTftpFileName_Object((1,3,6,1,4,1,89,76,27,1,10),_RlDhcpClInformationTftpFileName_Type())
rlDhcpClInformationTftpFileName.setMaxAccess(_B)
if mibBuilder.loadTexts:rlDhcpClInformationTftpFileName.setStatus(_A)
class _RlDhcpClInformationTimeZone_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_RlDhcpClInformationTimeZone_Type.__name__=_F
_RlDhcpClInformationTimeZone_Object=MibTableColumn
rlDhcpClInformationTimeZone=_RlDhcpClInformationTimeZone_Object((1,3,6,1,4,1,89,76,27,1,11),_RlDhcpClInformationTimeZone_Type())
rlDhcpClInformationTimeZone.setMaxAccess(_B)
if mibBuilder.loadTexts:rlDhcpClInformationTimeZone.setStatus(_A)
class _RlDhcpClInformationTftpImageName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,160))
_RlDhcpClInformationTftpImageName_Type.__name__=_F
_RlDhcpClInformationTftpImageName_Object=MibTableColumn
rlDhcpClInformationTftpImageName=_RlDhcpClInformationTftpImageName_Object((1,3,6,1,4,1,89,76,27,1,12),_RlDhcpClInformationTftpImageName_Type())
rlDhcpClInformationTftpImageName.setMaxAccess(_B)
if mibBuilder.loadTexts:rlDhcpClInformationTftpImageName.setStatus(_A)
_RlDhcpClInformationDnsServerListTable_Object=MibTable
rlDhcpClInformationDnsServerListTable=_RlDhcpClInformationDnsServerListTable_Object((1,3,6,1,4,1,89,76,28))
if mibBuilder.loadTexts:rlDhcpClInformationDnsServerListTable.setStatus(_A)
_RlDhcpClInformationDnsServerListEntry_Object=MibTableRow
rlDhcpClInformationDnsServerListEntry=_RlDhcpClInformationDnsServerListEntry_Object((1,3,6,1,4,1,89,76,28,1))
rlDhcpClInformationDnsServerListEntry.setIndexNames((0,_D,_Y),(0,_D,_Z))
if mibBuilder.loadTexts:rlDhcpClInformationDnsServerListEntry.setStatus(_A)
_RlDhcpClInformationDnsServerListIfIndex_Type=InterfaceIndex
_RlDhcpClInformationDnsServerListIfIndex_Object=MibTableColumn
rlDhcpClInformationDnsServerListIfIndex=_RlDhcpClInformationDnsServerListIfIndex_Object((1,3,6,1,4,1,89,76,28,1,1),_RlDhcpClInformationDnsServerListIfIndex_Type())
rlDhcpClInformationDnsServerListIfIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:rlDhcpClInformationDnsServerListIfIndex.setStatus(_A)
_RlDhcpClInformationDnsServerListPriority_Type=Integer32
_RlDhcpClInformationDnsServerListPriority_Object=MibTableColumn
rlDhcpClInformationDnsServerListPriority=_RlDhcpClInformationDnsServerListPriority_Object((1,3,6,1,4,1,89,76,28,1,2),_RlDhcpClInformationDnsServerListPriority_Type())
rlDhcpClInformationDnsServerListPriority.setMaxAccess(_G)
if mibBuilder.loadTexts:rlDhcpClInformationDnsServerListPriority.setStatus(_A)
_RlDhcpClInformationDnsServerListAddress_Type=IpAddress
_RlDhcpClInformationDnsServerListAddress_Object=MibTableColumn
rlDhcpClInformationDnsServerListAddress=_RlDhcpClInformationDnsServerListAddress_Object((1,3,6,1,4,1,89,76,28,1,3),_RlDhcpClInformationDnsServerListAddress_Type())
rlDhcpClInformationDnsServerListAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:rlDhcpClInformationDnsServerListAddress.setStatus(_A)
_RlDhcpClInformationTftpServerListTable_Object=MibTable
rlDhcpClInformationTftpServerListTable=_RlDhcpClInformationTftpServerListTable_Object((1,3,6,1,4,1,89,76,29))
if mibBuilder.loadTexts:rlDhcpClInformationTftpServerListTable.setStatus(_A)
_RlDhcpClInformationTftpServerListEntry_Object=MibTableRow
rlDhcpClInformationTftpServerListEntry=_RlDhcpClInformationTftpServerListEntry_Object((1,3,6,1,4,1,89,76,29,1))
rlDhcpClInformationTftpServerListEntry.setIndexNames((0,_D,_a),(0,_D,_b))
if mibBuilder.loadTexts:rlDhcpClInformationTftpServerListEntry.setStatus(_A)
_RlDhcpClInformationTftpServerListIfIndex_Type=InterfaceIndex
_RlDhcpClInformationTftpServerListIfIndex_Object=MibTableColumn
rlDhcpClInformationTftpServerListIfIndex=_RlDhcpClInformationTftpServerListIfIndex_Object((1,3,6,1,4,1,89,76,29,1,1),_RlDhcpClInformationTftpServerListIfIndex_Type())
rlDhcpClInformationTftpServerListIfIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:rlDhcpClInformationTftpServerListIfIndex.setStatus(_A)
_RlDhcpClInformationTftpServerListPriority_Type=Integer32
_RlDhcpClInformationTftpServerListPriority_Object=MibTableColumn
rlDhcpClInformationTftpServerListPriority=_RlDhcpClInformationTftpServerListPriority_Object((1,3,6,1,4,1,89,76,29,1,2),_RlDhcpClInformationTftpServerListPriority_Type())
rlDhcpClInformationTftpServerListPriority.setMaxAccess(_G)
if mibBuilder.loadTexts:rlDhcpClInformationTftpServerListPriority.setStatus(_A)
_RlDhcpClInformationTftpServerListAddress_Type=IpAddress
_RlDhcpClInformationTftpServerListAddress_Object=MibTableColumn
rlDhcpClInformationTftpServerListAddress=_RlDhcpClInformationTftpServerListAddress_Object((1,3,6,1,4,1,89,76,29,1,3),_RlDhcpClInformationTftpServerListAddress_Type())
rlDhcpClInformationTftpServerListAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:rlDhcpClInformationTftpServerListAddress.setStatus(_A)
class _RlDhcpClAutoUpdateProtocol_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('tftp',1),(_H,2),('auto',3)))
_RlDhcpClAutoUpdateProtocol_Type.__name__=_E
_RlDhcpClAutoUpdateProtocol_Object=MibScalar
rlDhcpClAutoUpdateProtocol=_RlDhcpClAutoUpdateProtocol_Object((1,3,6,1,4,1,89,76,30),_RlDhcpClAutoUpdateProtocol_Type())
rlDhcpClAutoUpdateProtocol.setMaxAccess(_C)
if mibBuilder.loadTexts:rlDhcpClAutoUpdateProtocol.setStatus(_A)
class _RlDhcpClAutoUpdateScpFileExtention_Type(DisplayString):defaultValue=OctetString(_H);subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,128))
_RlDhcpClAutoUpdateScpFileExtention_Type.__name__=_F
_RlDhcpClAutoUpdateScpFileExtention_Object=MibScalar
rlDhcpClAutoUpdateScpFileExtention=_RlDhcpClAutoUpdateScpFileExtention_Object((1,3,6,1,4,1,89,76,31),_RlDhcpClAutoUpdateScpFileExtention_Type())
rlDhcpClAutoUpdateScpFileExtention.setMaxAccess(_C)
if mibBuilder.loadTexts:rlDhcpClAutoUpdateScpFileExtention.setStatus(_A)
mibBuilder.exportSymbols(_D,**{'rlDhcpCl':rlDhcpCl,'rlDhcpClActionTable':rlDhcpClActionTable,'rlDhcpClActionEntry':rlDhcpClActionEntry,_M:rlDhcpClActionIfIndex,'rlDhcpClActionStatus':rlDhcpClActionStatus,'rlDhcpClActionHostName':rlDhcpClActionHostName,'rlDhcpApprovalEnabled':rlDhcpApprovalEnabled,'rlDhcpApprovalWaitingTable':rlDhcpApprovalWaitingTable,'rlDhcpApprovalWaitingEntry':rlDhcpApprovalWaitingEntry,_O:rlDhcpApprovalWaitingIfIndex,'rlDhcpApprovalWaitingAddress':rlDhcpApprovalWaitingAddress,'rlDhcpApprovalWaitingMask':rlDhcpApprovalWaitingMask,'rlDhcpApprovalWaitingGateway':rlDhcpApprovalWaitingGateway,'rlDhcpApprovalActionTable':rlDhcpApprovalActionTable,'rlDhcpApprovalActionEntry':rlDhcpApprovalActionEntry,_P:rlDhcpApprovalActionIfIndex,_Q:rlDhcpApprovalActionAddress,_R:rlDhcpApprovalActionMask,'rlDhcpApprovalActionApprove':rlDhcpApprovalActionApprove,'rlDhcpClCommandTable':rlDhcpClCommandTable,'rlDhcpClCommandEntry':rlDhcpClCommandEntry,'rlDhcpClCommandAction':rlDhcpClCommandAction,'rlDhcpClConfigurationFileName':rlDhcpClConfigurationFileName,'rlDhcpClOption67Enable':rlDhcpClOption67Enable,'rlDhcpClManualTftpServerAddress':rlDhcpClManualTftpServerAddress,'rlDhcpClSelectedTftpServerAddress':rlDhcpClSelectedTftpServerAddress,'rlDhcpClSelectedTftpServerAddressOrigin':rlDhcpClSelectedTftpServerAddressOrigin,'rlDhcpClManualConfigurationFileName':rlDhcpClManualConfigurationFileName,'rlDhcpClSelectedConfigurationFileName':rlDhcpClSelectedConfigurationFileName,'rlDhcpClSelectedConfigurationFileNameOrigin':rlDhcpClSelectedConfigurationFileNameOrigin,'rlDhcpClEnabledByDefaultRemovedIfindex':rlDhcpClEnabledByDefaultRemovedIfindex,'rlDhcpClAutoUpdateEnabled':rlDhcpClAutoUpdateEnabled,'rlDhcpClAutoUpdateStatus':rlDhcpClAutoUpdateStatus,'rlDhcpClAutoConfigForce':rlDhcpClAutoConfigForce,'rlDhcpClAutoConfigAutoSave':rlDhcpClAutoConfigAutoSave,'rlDhcpClAutoConfigStatus':rlDhcpClAutoConfigStatus,'rlDhcpClAutoConfigProtocol':rlDhcpClAutoConfigProtocol,'rlDhcpClAutoConfigScpFileExtention':rlDhcpClAutoConfigScpFileExtention,'rlDhcpClSelectedTftpServerInetAddressType':rlDhcpClSelectedTftpServerInetAddressType,'rlDhcpClSelectedTftpServerInetAddress':rlDhcpClSelectedTftpServerInetAddress,'rlDhcpClManualAutoConfigDataTable':rlDhcpClManualAutoConfigDataTable,'rlDhcpClManualAutoConfigDataEntry':rlDhcpClManualAutoConfigDataEntry,_W:rlDhcpClManualAutoConfigDataIndex,'rlDhcpClManualServerInetAddressType':rlDhcpClManualServerInetAddressType,'rlDhcpClManualServerInetAddress':rlDhcpClManualServerInetAddress,'rlDhcpClManualImageIndirectFileName':rlDhcpClManualImageIndirectFileName,'rlDhcpClInformationTable':rlDhcpClInformationTable,'rlDhcpClInformationEntry':rlDhcpClInformationEntry,_X:rlDhcpClInformationIfIndex,'rlDhcpClInformationIpAddress':rlDhcpClInformationIpAddress,'rlDhcpClInformationIpMask':rlDhcpClInformationIpMask,'rlDhcpClInformationT1':rlDhcpClInformationT1,'rlDhcpClInformationT2':rlDhcpClInformationT2,'rlDhcpClInformationDefaultGateway':rlDhcpClInformationDefaultGateway,'rlDhcpClInformationHostName':rlDhcpClInformationHostName,'rlDhcpClInformationDomainName':rlDhcpClInformationDomainName,'rlDhcpClInformationTftpServerName':rlDhcpClInformationTftpServerName,'rlDhcpClInformationTftpFileName':rlDhcpClInformationTftpFileName,'rlDhcpClInformationTimeZone':rlDhcpClInformationTimeZone,'rlDhcpClInformationTftpImageName':rlDhcpClInformationTftpImageName,'rlDhcpClInformationDnsServerListTable':rlDhcpClInformationDnsServerListTable,'rlDhcpClInformationDnsServerListEntry':rlDhcpClInformationDnsServerListEntry,_Y:rlDhcpClInformationDnsServerListIfIndex,_Z:rlDhcpClInformationDnsServerListPriority,'rlDhcpClInformationDnsServerListAddress':rlDhcpClInformationDnsServerListAddress,'rlDhcpClInformationTftpServerListTable':rlDhcpClInformationTftpServerListTable,'rlDhcpClInformationTftpServerListEntry':rlDhcpClInformationTftpServerListEntry,_a:rlDhcpClInformationTftpServerListIfIndex,_b:rlDhcpClInformationTftpServerListPriority,'rlDhcpClInformationTftpServerListAddress':rlDhcpClInformationTftpServerListAddress,'rlDhcpClAutoUpdateProtocol':rlDhcpClAutoUpdateProtocol,'rlDhcpClAutoUpdateScpFileExtention':rlDhcpClAutoUpdateScpFileExtention})