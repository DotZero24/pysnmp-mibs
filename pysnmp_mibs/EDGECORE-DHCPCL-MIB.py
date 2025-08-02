_T='quitNoTftpOutgoingInterface'
_S='openingIndirectFile'
_R='noData'
_Q='manual'
_P='rlDhcpApprovalActionMask'
_O='rlDhcpApprovalActionAddress'
_N='rlDhcpApprovalActionIfIndex'
_M='rlDhcpApprovalWaitingIfIndex'
_L='read-create'
_K='rlDhcpClActionIfIndex'
_J='SnmpAdminString'
_I='ifIndex'
_H='IF-MIB'
_G='none'
_F='DisplayString'
_E='EDGECORE-DHCPCL-MIB'
_D='Integer32'
_C='read-write'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
rnd,=mibBuilder.importSymbols('EDGECORE-MIB','rnd')
InterfaceIndex,ifIndex=mibBuilder.importSymbols(_H,'InterfaceIndex',_I)
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB',_J)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC',_F,'PhysAddress','RowStatus','TextualConvention','TruthValue')
rlDhcpCl=ModuleIdentity((1,3,6,1,4,1,259,10,1,14,89,76))
if mibBuilder.loadTexts:rlDhcpCl.setRevisions(('2007-01-02 00:00',))
_RlDhcpClActionTable_Object=MibTable
rlDhcpClActionTable=_RlDhcpClActionTable_Object((1,3,6,1,4,1,259,10,1,14,89,76,3))
if mibBuilder.loadTexts:rlDhcpClActionTable.setStatus(_A)
_RlDhcpClActionEntry_Object=MibTableRow
rlDhcpClActionEntry=_RlDhcpClActionEntry_Object((1,3,6,1,4,1,259,10,1,14,89,76,3,1))
rlDhcpClActionEntry.setIndexNames((0,_E,_K))
if mibBuilder.loadTexts:rlDhcpClActionEntry.setStatus(_A)
_RlDhcpClActionIfIndex_Type=InterfaceIndex
_RlDhcpClActionIfIndex_Object=MibTableColumn
rlDhcpClActionIfIndex=_RlDhcpClActionIfIndex_Object((1,3,6,1,4,1,259,10,1,14,89,76,3,1,1),_RlDhcpClActionIfIndex_Type())
rlDhcpClActionIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:rlDhcpClActionIfIndex.setStatus(_A)
_RlDhcpClActionStatus_Type=RowStatus
_RlDhcpClActionStatus_Object=MibTableColumn
rlDhcpClActionStatus=_RlDhcpClActionStatus_Object((1,3,6,1,4,1,259,10,1,14,89,76,3,1,2),_RlDhcpClActionStatus_Type())
rlDhcpClActionStatus.setMaxAccess(_L)
if mibBuilder.loadTexts:rlDhcpClActionStatus.setStatus(_A)
class _RlDhcpClActionHostName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,20))
_RlDhcpClActionHostName_Type.__name__=_J
_RlDhcpClActionHostName_Object=MibTableColumn
rlDhcpClActionHostName=_RlDhcpClActionHostName_Object((1,3,6,1,4,1,259,10,1,14,89,76,3,1,3),_RlDhcpClActionHostName_Type())
rlDhcpClActionHostName.setMaxAccess(_L)
if mibBuilder.loadTexts:rlDhcpClActionHostName.setStatus(_A)
_RlDhcpApprovalEnabled_Type=TruthValue
_RlDhcpApprovalEnabled_Object=MibScalar
rlDhcpApprovalEnabled=_RlDhcpApprovalEnabled_Object((1,3,6,1,4,1,259,10,1,14,89,76,4),_RlDhcpApprovalEnabled_Type())
rlDhcpApprovalEnabled.setMaxAccess(_B)
if mibBuilder.loadTexts:rlDhcpApprovalEnabled.setStatus(_A)
_RlDhcpApprovalWaitingTable_Object=MibTable
rlDhcpApprovalWaitingTable=_RlDhcpApprovalWaitingTable_Object((1,3,6,1,4,1,259,10,1,14,89,76,5))
if mibBuilder.loadTexts:rlDhcpApprovalWaitingTable.setStatus(_A)
_RlDhcpApprovalWaitingEntry_Object=MibTableRow
rlDhcpApprovalWaitingEntry=_RlDhcpApprovalWaitingEntry_Object((1,3,6,1,4,1,259,10,1,14,89,76,5,1))
rlDhcpApprovalWaitingEntry.setIndexNames((0,_E,_M))
if mibBuilder.loadTexts:rlDhcpApprovalWaitingEntry.setStatus(_A)
_RlDhcpApprovalWaitingIfIndex_Type=InterfaceIndex
_RlDhcpApprovalWaitingIfIndex_Object=MibTableColumn
rlDhcpApprovalWaitingIfIndex=_RlDhcpApprovalWaitingIfIndex_Object((1,3,6,1,4,1,259,10,1,14,89,76,5,1,1),_RlDhcpApprovalWaitingIfIndex_Type())
rlDhcpApprovalWaitingIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:rlDhcpApprovalWaitingIfIndex.setStatus(_A)
_RlDhcpApprovalWaitingAddress_Type=IpAddress
_RlDhcpApprovalWaitingAddress_Object=MibTableColumn
rlDhcpApprovalWaitingAddress=_RlDhcpApprovalWaitingAddress_Object((1,3,6,1,4,1,259,10,1,14,89,76,5,1,2),_RlDhcpApprovalWaitingAddress_Type())
rlDhcpApprovalWaitingAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:rlDhcpApprovalWaitingAddress.setStatus(_A)
_RlDhcpApprovalWaitingMask_Type=IpAddress
_RlDhcpApprovalWaitingMask_Object=MibTableColumn
rlDhcpApprovalWaitingMask=_RlDhcpApprovalWaitingMask_Object((1,3,6,1,4,1,259,10,1,14,89,76,5,1,3),_RlDhcpApprovalWaitingMask_Type())
rlDhcpApprovalWaitingMask.setMaxAccess(_B)
if mibBuilder.loadTexts:rlDhcpApprovalWaitingMask.setStatus(_A)
_RlDhcpApprovalWaitingGateway_Type=IpAddress
_RlDhcpApprovalWaitingGateway_Object=MibTableColumn
rlDhcpApprovalWaitingGateway=_RlDhcpApprovalWaitingGateway_Object((1,3,6,1,4,1,259,10,1,14,89,76,5,1,4),_RlDhcpApprovalWaitingGateway_Type())
rlDhcpApprovalWaitingGateway.setMaxAccess(_B)
if mibBuilder.loadTexts:rlDhcpApprovalWaitingGateway.setStatus(_A)
_RlDhcpApprovalActionTable_Object=MibTable
rlDhcpApprovalActionTable=_RlDhcpApprovalActionTable_Object((1,3,6,1,4,1,259,10,1,14,89,76,6))
if mibBuilder.loadTexts:rlDhcpApprovalActionTable.setStatus(_A)
_RlDhcpApprovalActionEntry_Object=MibTableRow
rlDhcpApprovalActionEntry=_RlDhcpApprovalActionEntry_Object((1,3,6,1,4,1,259,10,1,14,89,76,6,1))
rlDhcpApprovalActionEntry.setIndexNames((0,_E,_N),(0,_E,_O),(0,_E,_P))
if mibBuilder.loadTexts:rlDhcpApprovalActionEntry.setStatus(_A)
_RlDhcpApprovalActionIfIndex_Type=InterfaceIndex
_RlDhcpApprovalActionIfIndex_Object=MibTableColumn
rlDhcpApprovalActionIfIndex=_RlDhcpApprovalActionIfIndex_Object((1,3,6,1,4,1,259,10,1,14,89,76,6,1,1),_RlDhcpApprovalActionIfIndex_Type())
rlDhcpApprovalActionIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:rlDhcpApprovalActionIfIndex.setStatus(_A)
_RlDhcpApprovalActionAddress_Type=IpAddress
_RlDhcpApprovalActionAddress_Object=MibTableColumn
rlDhcpApprovalActionAddress=_RlDhcpApprovalActionAddress_Object((1,3,6,1,4,1,259,10,1,14,89,76,6,1,2),_RlDhcpApprovalActionAddress_Type())
rlDhcpApprovalActionAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:rlDhcpApprovalActionAddress.setStatus(_A)
_RlDhcpApprovalActionMask_Type=IpAddress
_RlDhcpApprovalActionMask_Object=MibTableColumn
rlDhcpApprovalActionMask=_RlDhcpApprovalActionMask_Object((1,3,6,1,4,1,259,10,1,14,89,76,6,1,3),_RlDhcpApprovalActionMask_Type())
rlDhcpApprovalActionMask.setMaxAccess(_B)
if mibBuilder.loadTexts:rlDhcpApprovalActionMask.setStatus(_A)
_RlDhcpApprovalActionApprove_Type=TruthValue
_RlDhcpApprovalActionApprove_Object=MibTableColumn
rlDhcpApprovalActionApprove=_RlDhcpApprovalActionApprove_Object((1,3,6,1,4,1,259,10,1,14,89,76,6,1,4),_RlDhcpApprovalActionApprove_Type())
rlDhcpApprovalActionApprove.setMaxAccess(_C)
if mibBuilder.loadTexts:rlDhcpApprovalActionApprove.setStatus(_A)
_RlDhcpClCommandTable_Object=MibTable
rlDhcpClCommandTable=_RlDhcpClCommandTable_Object((1,3,6,1,4,1,259,10,1,14,89,76,7))
if mibBuilder.loadTexts:rlDhcpClCommandTable.setStatus(_A)
_RlDhcpClCommandEntry_Object=MibTableRow
rlDhcpClCommandEntry=_RlDhcpClCommandEntry_Object((1,3,6,1,4,1,259,10,1,14,89,76,7,1))
rlDhcpClCommandEntry.setIndexNames((0,_H,_I))
if mibBuilder.loadTexts:rlDhcpClCommandEntry.setStatus(_A)
class _RlDhcpClCommandAction_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_G,0),('renew',1),('renewForceAutoconfig',2)))
_RlDhcpClCommandAction_Type.__name__=_D
_RlDhcpClCommandAction_Object=MibTableColumn
rlDhcpClCommandAction=_RlDhcpClCommandAction_Object((1,3,6,1,4,1,259,10,1,14,89,76,7,1,2),_RlDhcpClCommandAction_Type())
rlDhcpClCommandAction.setMaxAccess(_C)
if mibBuilder.loadTexts:rlDhcpClCommandAction.setStatus(_A)
class _RlDhcpClConfigurationFileName_Type(DisplayString):defaultValue=OctetString('')
_RlDhcpClConfigurationFileName_Type.__name__=_F
_RlDhcpClConfigurationFileName_Object=MibScalar
rlDhcpClConfigurationFileName=_RlDhcpClConfigurationFileName_Object((1,3,6,1,4,1,259,10,1,14,89,76,8),_RlDhcpClConfigurationFileName_Type())
rlDhcpClConfigurationFileName.setMaxAccess(_C)
if mibBuilder.loadTexts:rlDhcpClConfigurationFileName.setStatus(_A)
class _RlDhcpClOption67Enable_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('enable',1),('disable',2)))
_RlDhcpClOption67Enable_Type.__name__=_D
_RlDhcpClOption67Enable_Object=MibScalar
rlDhcpClOption67Enable=_RlDhcpClOption67Enable_Object((1,3,6,1,4,1,259,10,1,14,89,76,9),_RlDhcpClOption67Enable_Type())
rlDhcpClOption67Enable.setMaxAccess(_C)
if mibBuilder.loadTexts:rlDhcpClOption67Enable.setStatus(_A)
_RlDhcpClManualTftpServerAddress_Type=IpAddress
_RlDhcpClManualTftpServerAddress_Object=MibScalar
rlDhcpClManualTftpServerAddress=_RlDhcpClManualTftpServerAddress_Object((1,3,6,1,4,1,259,10,1,14,89,76,10),_RlDhcpClManualTftpServerAddress_Type())
rlDhcpClManualTftpServerAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:rlDhcpClManualTftpServerAddress.setStatus(_A)
_RlDhcpClSelectedTftpServerAddress_Type=IpAddress
_RlDhcpClSelectedTftpServerAddress_Object=MibScalar
rlDhcpClSelectedTftpServerAddress=_RlDhcpClSelectedTftpServerAddress_Object((1,3,6,1,4,1,259,10,1,14,89,76,11),_RlDhcpClSelectedTftpServerAddress_Type())
rlDhcpClSelectedTftpServerAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:rlDhcpClSelectedTftpServerAddress.setStatus(_A)
class _RlDhcpClSelectedTftpServerAddressOrigin_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8)));namedValues=NamedValues(*(('sname',1),('option66',2),('option150',3),('option129',4),('siaddr',5),(_Q,6),('unknown',7),(_G,8)))
_RlDhcpClSelectedTftpServerAddressOrigin_Type.__name__=_D
_RlDhcpClSelectedTftpServerAddressOrigin_Object=MibScalar
rlDhcpClSelectedTftpServerAddressOrigin=_RlDhcpClSelectedTftpServerAddressOrigin_Object((1,3,6,1,4,1,259,10,1,14,89,76,12),_RlDhcpClSelectedTftpServerAddressOrigin_Type())
rlDhcpClSelectedTftpServerAddressOrigin.setMaxAccess(_B)
if mibBuilder.loadTexts:rlDhcpClSelectedTftpServerAddressOrigin.setStatus(_A)
class _RlDhcpClManualConfigurationFileName_Type(DisplayString):defaultValue=OctetString('')
_RlDhcpClManualConfigurationFileName_Type.__name__=_F
_RlDhcpClManualConfigurationFileName_Object=MibScalar
rlDhcpClManualConfigurationFileName=_RlDhcpClManualConfigurationFileName_Object((1,3,6,1,4,1,259,10,1,14,89,76,13),_RlDhcpClManualConfigurationFileName_Type())
rlDhcpClManualConfigurationFileName.setMaxAccess(_C)
if mibBuilder.loadTexts:rlDhcpClManualConfigurationFileName.setStatus(_A)
_RlDhcpClSelectedConfigurationFileName_Type=DisplayString
_RlDhcpClSelectedConfigurationFileName_Object=MibScalar
rlDhcpClSelectedConfigurationFileName=_RlDhcpClSelectedConfigurationFileName_Object((1,3,6,1,4,1,259,10,1,14,89,76,14),_RlDhcpClSelectedConfigurationFileName_Type())
rlDhcpClSelectedConfigurationFileName.setMaxAccess(_B)
if mibBuilder.loadTexts:rlDhcpClSelectedConfigurationFileName.setStatus(_A)
class _RlDhcpClSelectedConfigurationFileNameOrigin_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*(('file',1),('option67',2),(_Q,3),(_G,4),('hostname',5),('defaultConfigFile',6)))
_RlDhcpClSelectedConfigurationFileNameOrigin_Type.__name__=_D
_RlDhcpClSelectedConfigurationFileNameOrigin_Object=MibScalar
rlDhcpClSelectedConfigurationFileNameOrigin=_RlDhcpClSelectedConfigurationFileNameOrigin_Object((1,3,6,1,4,1,259,10,1,14,89,76,15),_RlDhcpClSelectedConfigurationFileNameOrigin_Type())
rlDhcpClSelectedConfigurationFileNameOrigin.setMaxAccess(_B)
if mibBuilder.loadTexts:rlDhcpClSelectedConfigurationFileNameOrigin.setStatus(_A)
class _RlDhcpClEnabledByDefaultRemovedIfindex_Type(Integer32):defaultValue=0
_RlDhcpClEnabledByDefaultRemovedIfindex_Type.__name__=_D
_RlDhcpClEnabledByDefaultRemovedIfindex_Object=MibScalar
rlDhcpClEnabledByDefaultRemovedIfindex=_RlDhcpClEnabledByDefaultRemovedIfindex_Object((1,3,6,1,4,1,259,10,1,14,89,76,16),_RlDhcpClEnabledByDefaultRemovedIfindex_Type())
rlDhcpClEnabledByDefaultRemovedIfindex.setMaxAccess(_C)
if mibBuilder.loadTexts:rlDhcpClEnabledByDefaultRemovedIfindex.setStatus(_A)
_RlDhcpClAutoUpdateEnabled_Type=TruthValue
_RlDhcpClAutoUpdateEnabled_Object=MibScalar
rlDhcpClAutoUpdateEnabled=_RlDhcpClAutoUpdateEnabled_Object((1,3,6,1,4,1,259,10,1,14,89,76,17),_RlDhcpClAutoUpdateEnabled_Type())
rlDhcpClAutoUpdateEnabled.setMaxAccess(_C)
if mibBuilder.loadTexts:rlDhcpClAutoUpdateEnabled.setStatus(_A)
class _RlDhcpClAutoUpdateStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12)));namedValues=NamedValues(*((_R,1),(_S,2),('downloadedIndirectFile',3),('startDownloadImageFile',4),('failedToDownloadImageFile',5),('quitFileContentsLenZero',6),('quitImageFileNameLenZero',7),('quitVersionAlreadyUpdated',8),('quitIndirectFileNotFound',9),('quitImageFileNotFound',10),('quitImageVersionNotSupported',11),(_T,12)))
_RlDhcpClAutoUpdateStatus_Type.__name__=_D
_RlDhcpClAutoUpdateStatus_Object=MibScalar
rlDhcpClAutoUpdateStatus=_RlDhcpClAutoUpdateStatus_Object((1,3,6,1,4,1,259,10,1,14,89,76,18),_RlDhcpClAutoUpdateStatus_Type())
rlDhcpClAutoUpdateStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:rlDhcpClAutoUpdateStatus.setStatus(_A)
_RlDhcpClAutoConfigForce_Type=TruthValue
_RlDhcpClAutoConfigForce_Object=MibScalar
rlDhcpClAutoConfigForce=_RlDhcpClAutoConfigForce_Object((1,3,6,1,4,1,259,10,1,14,89,76,19),_RlDhcpClAutoConfigForce_Type())
rlDhcpClAutoConfigForce.setMaxAccess(_C)
if mibBuilder.loadTexts:rlDhcpClAutoConfigForce.setStatus(_A)
_RlDhcpClAutoConfigAutoSave_Type=TruthValue
_RlDhcpClAutoConfigAutoSave_Object=MibScalar
rlDhcpClAutoConfigAutoSave=_RlDhcpClAutoConfigAutoSave_Object((1,3,6,1,4,1,259,10,1,14,89,76,20),_RlDhcpClAutoConfigAutoSave_Type())
rlDhcpClAutoConfigAutoSave.setMaxAccess(_C)
if mibBuilder.loadTexts:rlDhcpClAutoConfigAutoSave.setStatus(_A)
class _RlDhcpClAutoConfigStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21)));namedValues=NamedValues(*((_R,1),('openingDhcpConfigFile',2),(_S,3),('searchingHostnameInIndirectFile',4),('openingHostnameConfigFile',5),('openingHostnameCfgFile',6),('openingDefaultConfigFile',7),('downloadingConfigFile',8),('savingConfigInStartupCDB',9),('quitDhcpFileNotGivenOrNotExists',10),('quitFailedToFindAnyExistingConfigFile',11),('quitConfigFileContentsLenZero',12),('quitConfigFileDownloadFailed',13),('quitConditionsForAutoConfigChanged',14),('quitSelectedConfigFileNameUpdateFailed',15),('quitSelectedConfigFileNameOriginUpdateFailed',16),('quitSelectedTftpServerAddressUpdateFailed',17),('quitSelectedTftpServerAddressOriginUpdateFailed',18),('quitCopyRunningToStartupFailed',19),(_T,20),('finishedSuccessfully',21)))
_RlDhcpClAutoConfigStatus_Type.__name__=_D
_RlDhcpClAutoConfigStatus_Object=MibScalar
rlDhcpClAutoConfigStatus=_RlDhcpClAutoConfigStatus_Object((1,3,6,1,4,1,259,10,1,14,89,76,21),_RlDhcpClAutoConfigStatus_Type())
rlDhcpClAutoConfigStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:rlDhcpClAutoConfigStatus.setStatus(_A)
mibBuilder.exportSymbols(_E,**{'rlDhcpCl':rlDhcpCl,'rlDhcpClActionTable':rlDhcpClActionTable,'rlDhcpClActionEntry':rlDhcpClActionEntry,_K:rlDhcpClActionIfIndex,'rlDhcpClActionStatus':rlDhcpClActionStatus,'rlDhcpClActionHostName':rlDhcpClActionHostName,'rlDhcpApprovalEnabled':rlDhcpApprovalEnabled,'rlDhcpApprovalWaitingTable':rlDhcpApprovalWaitingTable,'rlDhcpApprovalWaitingEntry':rlDhcpApprovalWaitingEntry,_M:rlDhcpApprovalWaitingIfIndex,'rlDhcpApprovalWaitingAddress':rlDhcpApprovalWaitingAddress,'rlDhcpApprovalWaitingMask':rlDhcpApprovalWaitingMask,'rlDhcpApprovalWaitingGateway':rlDhcpApprovalWaitingGateway,'rlDhcpApprovalActionTable':rlDhcpApprovalActionTable,'rlDhcpApprovalActionEntry':rlDhcpApprovalActionEntry,_N:rlDhcpApprovalActionIfIndex,_O:rlDhcpApprovalActionAddress,_P:rlDhcpApprovalActionMask,'rlDhcpApprovalActionApprove':rlDhcpApprovalActionApprove,'rlDhcpClCommandTable':rlDhcpClCommandTable,'rlDhcpClCommandEntry':rlDhcpClCommandEntry,'rlDhcpClCommandAction':rlDhcpClCommandAction,'rlDhcpClConfigurationFileName':rlDhcpClConfigurationFileName,'rlDhcpClOption67Enable':rlDhcpClOption67Enable,'rlDhcpClManualTftpServerAddress':rlDhcpClManualTftpServerAddress,'rlDhcpClSelectedTftpServerAddress':rlDhcpClSelectedTftpServerAddress,'rlDhcpClSelectedTftpServerAddressOrigin':rlDhcpClSelectedTftpServerAddressOrigin,'rlDhcpClManualConfigurationFileName':rlDhcpClManualConfigurationFileName,'rlDhcpClSelectedConfigurationFileName':rlDhcpClSelectedConfigurationFileName,'rlDhcpClSelectedConfigurationFileNameOrigin':rlDhcpClSelectedConfigurationFileNameOrigin,'rlDhcpClEnabledByDefaultRemovedIfindex':rlDhcpClEnabledByDefaultRemovedIfindex,'rlDhcpClAutoUpdateEnabled':rlDhcpClAutoUpdateEnabled,'rlDhcpClAutoUpdateStatus':rlDhcpClAutoUpdateStatus,'rlDhcpClAutoConfigForce':rlDhcpClAutoConfigForce,'rlDhcpClAutoConfigAutoSave':rlDhcpClAutoConfigAutoSave,'rlDhcpClAutoConfigStatus':rlDhcpClAutoConfigStatus})