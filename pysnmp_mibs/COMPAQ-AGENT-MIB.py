_h='agentSwitchTempSensorIndex'
_g='agentSwitchFanIndex'
_f='brownOut'
_e='noError'
_d='agentSwitchPowerSupplyIndex'
_c='agentSwitchCubeType'
_b='baudRate-57200'
_a='enabled'
_Z='agentIpTrapManagerIpAddr'
_Y='agentBscSwFileIndex'
_X='agentMibCapabilityIndex'
_W='degraded'
_V='disabled'
_U='baudRate-115200'
_T='baudRate-38400'
_S='baudRate-19200'
_R='baudRate-9600'
_Q='baudRate-2400'
_P='obsolete'
_O='failed'
_N='cpqRackNetConnectorRack'
_M='cpqRackNetConnectorIndex'
_L='cpqRackNetConnectorChassis'
_K='cpqRackCommonEnclosureRack'
_J='cpqRackCommonEnclosureIndex'
_I='cpqRackAssetIndex'
_H='COMPAQ-AGENT-MIB'
_G='DisplayString'
_F='other'
_E='CPQRACK-MIB'
_D='read-only'
_C='read-write'
_B='Integer32'
_A='mandatory'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
compaq_common_mgmt,=mibBuilder.importSymbols('COMPAQ-ID-REC-MIB','compaq-common-mgmt')
cpqRackAssetIndex,cpqRackCommonEnclosureIndex,cpqRackCommonEnclosureRack,cpqRackNetConnectorChassis,cpqRackNetConnectorIndex,cpqRackNetConnectorRack=mibBuilder.importSymbols(_E,_I,_J,_K,_L,_M,_N)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_B,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_G,'PhysAddress','TextualConvention')
_AgentGeneralMgmt_ObjectIdentity=ObjectIdentity
agentGeneralMgmt=_AgentGeneralMgmt_ObjectIdentity((1,3,6,1,4,1,232,161,3,1))
_AgentBasicInfo_ObjectIdentity=ObjectIdentity
agentBasicInfo=_AgentBasicInfo_ObjectIdentity((1,3,6,1,4,1,232,161,3,1,1))
class _AgentMgmtProtocolCapability_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_F,1),('snmp-ip',2),('snmp-ipx',3),('snmp-ip-ipx',4)))
_AgentMgmtProtocolCapability_Type.__name__=_B
_AgentMgmtProtocolCapability_Object=MibScalar
agentMgmtProtocolCapability=_AgentMgmtProtocolCapability_Object((1,3,6,1,4,1,232,161,3,1,1,1),_AgentMgmtProtocolCapability_Type())
agentMgmtProtocolCapability.setMaxAccess(_D)
if mibBuilder.loadTexts:agentMgmtProtocolCapability.setStatus(_A)
_AgentMibCapabilityTable_Object=MibTable
agentMibCapabilityTable=_AgentMibCapabilityTable_Object((1,3,6,1,4,1,232,161,3,1,1,2))
if mibBuilder.loadTexts:agentMibCapabilityTable.setStatus(_A)
_AgentMibCapabilityEntry_Object=MibTableRow
agentMibCapabilityEntry=_AgentMibCapabilityEntry_Object((1,3,6,1,4,1,232,161,3,1,1,2,1))
agentMibCapabilityEntry.setIndexNames((0,_H,_X))
if mibBuilder.loadTexts:agentMibCapabilityEntry.setStatus(_A)
_AgentMibCapabilityIndex_Type=Integer32
_AgentMibCapabilityIndex_Object=MibTableColumn
agentMibCapabilityIndex=_AgentMibCapabilityIndex_Object((1,3,6,1,4,1,232,161,3,1,1,2,1,1),_AgentMibCapabilityIndex_Type())
agentMibCapabilityIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:agentMibCapabilityIndex.setStatus(_A)
class _AgentMibCapabilityDescr_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,35))
_AgentMibCapabilityDescr_Type.__name__=_G
_AgentMibCapabilityDescr_Object=MibTableColumn
agentMibCapabilityDescr=_AgentMibCapabilityDescr_Object((1,3,6,1,4,1,232,161,3,1,1,2,1,2),_AgentMibCapabilityDescr_Type())
agentMibCapabilityDescr.setMaxAccess(_D)
if mibBuilder.loadTexts:agentMibCapabilityDescr.setStatus(_A)
_AgentMibCapabilityVersion_Type=Integer32
_AgentMibCapabilityVersion_Object=MibTableColumn
agentMibCapabilityVersion=_AgentMibCapabilityVersion_Object((1,3,6,1,4,1,232,161,3,1,1,2,1,3),_AgentMibCapabilityVersion_Type())
agentMibCapabilityVersion.setMaxAccess(_D)
if mibBuilder.loadTexts:agentMibCapabilityVersion.setStatus(_A)
class _AgentMibCapabilityType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_F,1),('standard',2),('proprietary',3),('experiment',4)))
_AgentMibCapabilityType_Type.__name__=_B
_AgentMibCapabilityType_Object=MibTableColumn
agentMibCapabilityType=_AgentMibCapabilityType_Object((1,3,6,1,4,1,232,161,3,1,1,2,1,4),_AgentMibCapabilityType_Type())
agentMibCapabilityType.setMaxAccess(_D)
if mibBuilder.loadTexts:agentMibCapabilityType.setStatus(_A)
class _AgentStatusConsoleInUse_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_F,1),('in-use',2),('not-in-use',3)))
_AgentStatusConsoleInUse_Type.__name__=_B
_AgentStatusConsoleInUse_Object=MibScalar
agentStatusConsoleInUse=_AgentStatusConsoleInUse_Object((1,3,6,1,4,1,232,161,3,1,1,3),_AgentStatusConsoleInUse_Type())
agentStatusConsoleInUse.setMaxAccess(_D)
if mibBuilder.loadTexts:agentStatusConsoleInUse.setStatus(_A)
class _AgentStatusSaveCfg_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_F,1),('proceeding',2),('completed',3),('changed-not-save',4),(_O,5)))
_AgentStatusSaveCfg_Type.__name__=_B
_AgentStatusSaveCfg_Object=MibScalar
agentStatusSaveCfg=_AgentStatusSaveCfg_Object((1,3,6,1,4,1,232,161,3,1,1,4),_AgentStatusSaveCfg_Type())
agentStatusSaveCfg.setMaxAccess(_D)
if mibBuilder.loadTexts:agentStatusSaveCfg.setStatus(_A)
class _AgentSwitchMfgDate_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_AgentSwitchMfgDate_Type.__name__=_G
_AgentSwitchMfgDate_Object=MibScalar
agentSwitchMfgDate=_AgentSwitchMfgDate_Object((1,3,6,1,4,1,232,161,3,1,1,5),_AgentSwitchMfgDate_Type())
agentSwitchMfgDate.setMaxAccess(_D)
if mibBuilder.loadTexts:agentSwitchMfgDate.setStatus(_A)
class _AgentSwitchFirmwareMfgDate_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_AgentSwitchFirmwareMfgDate_Type.__name__=_G
_AgentSwitchFirmwareMfgDate_Object=MibScalar
agentSwitchFirmwareMfgDate=_AgentSwitchFirmwareMfgDate_Object((1,3,6,1,4,1,232,161,3,1,1,6),_AgentSwitchFirmwareMfgDate_Type())
agentSwitchFirmwareMfgDate.setMaxAccess(_D)
if mibBuilder.loadTexts:agentSwitchFirmwareMfgDate.setStatus(_A)
_AgentBasicConfig_ObjectIdentity=ObjectIdentity
agentBasicConfig=_AgentBasicConfig_ObjectIdentity((1,3,6,1,4,1,232,161,3,1,2))
_AgentBscSwFileTable_Object=MibTable
agentBscSwFileTable=_AgentBscSwFileTable_Object((1,3,6,1,4,1,232,161,3,1,2,1))
if mibBuilder.loadTexts:agentBscSwFileTable.setStatus(_A)
_AgentBscSwFileEntry_Object=MibTableRow
agentBscSwFileEntry=_AgentBscSwFileEntry_Object((1,3,6,1,4,1,232,161,3,1,2,1,1))
agentBscSwFileEntry.setIndexNames((0,_H,_Y))
if mibBuilder.loadTexts:agentBscSwFileEntry.setStatus(_A)
_AgentBscSwFileIndex_Type=Integer32
_AgentBscSwFileIndex_Object=MibTableColumn
agentBscSwFileIndex=_AgentBscSwFileIndex_Object((1,3,6,1,4,1,232,161,3,1,2,1,1,1),_AgentBscSwFileIndex_Type())
agentBscSwFileIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:agentBscSwFileIndex.setStatus(_A)
class _AgentBscSwFileDscr_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_AgentBscSwFileDscr_Type.__name__=_G
_AgentBscSwFileDscr_Object=MibTableColumn
agentBscSwFileDscr=_AgentBscSwFileDscr_Object((1,3,6,1,4,1,232,161,3,1,2,1,1,2),_AgentBscSwFileDscr_Type())
agentBscSwFileDscr.setMaxAccess(_C)
if mibBuilder.loadTexts:agentBscSwFileDscr.setStatus(_A)
_AgentBscSwFileAddr_Type=IpAddress
_AgentBscSwFileAddr_Object=MibTableColumn
agentBscSwFileAddr=_AgentBscSwFileAddr_Object((1,3,6,1,4,1,232,161,3,1,2,1,1,3),_AgentBscSwFileAddr_Type())
agentBscSwFileAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:agentBscSwFileAddr.setStatus(_A)
class _AgentBscSwFileTransferType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_F,1),('network-load',2),('out-of-band-load',3)))
_AgentBscSwFileTransferType_Type.__name__=_B
_AgentBscSwFileTransferType_Object=MibTableColumn
agentBscSwFileTransferType=_AgentBscSwFileTransferType_Object((1,3,6,1,4,1,232,161,3,1,2,1,1,4),_AgentBscSwFileTransferType_Type())
agentBscSwFileTransferType.setMaxAccess(_C)
if mibBuilder.loadTexts:agentBscSwFileTransferType.setStatus(_A)
class _AgentBscSwFile_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,128))
_AgentBscSwFile_Type.__name__=_G
_AgentBscSwFile_Object=MibTableColumn
agentBscSwFile=_AgentBscSwFile_Object((1,3,6,1,4,1,232,161,3,1,2,1,1,5),_AgentBscSwFile_Type())
agentBscSwFile.setMaxAccess(_C)
if mibBuilder.loadTexts:agentBscSwFile.setStatus(_A)
class _AgentBscSwFileLocateId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,16))
_AgentBscSwFileLocateId_Type.__name__=_B
_AgentBscSwFileLocateId_Object=MibTableColumn
agentBscSwFileLocateId=_AgentBscSwFileLocateId_Object((1,3,6,1,4,1,232,161,3,1,2,1,1,6),_AgentBscSwFileLocateId_Type())
agentBscSwFileLocateId.setMaxAccess(_C)
if mibBuilder.loadTexts:agentBscSwFileLocateId.setStatus(_A)
class _AgentBscSwFileLoadType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_F,1),('upload',2),('download',3)))
_AgentBscSwFileLoadType_Type.__name__=_B
_AgentBscSwFileLoadType_Object=MibTableColumn
agentBscSwFileLoadType=_AgentBscSwFileLoadType_Object((1,3,6,1,4,1,232,161,3,1,2,1,1,7),_AgentBscSwFileLoadType_Type())
agentBscSwFileLoadType.setMaxAccess(_C)
if mibBuilder.loadTexts:agentBscSwFileLoadType.setStatus(_A)
class _AgentBscSwFileCtrl_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_F,1),('inactive',2),('start',3),('delete',4),('create-and-go',5)))
_AgentBscSwFileCtrl_Type.__name__=_B
_AgentBscSwFileCtrl_Object=MibTableColumn
agentBscSwFileCtrl=_AgentBscSwFileCtrl_Object((1,3,6,1,4,1,232,161,3,1,2,1,1,8),_AgentBscSwFileCtrl_Type())
agentBscSwFileCtrl.setMaxAccess(_C)
if mibBuilder.loadTexts:agentBscSwFileCtrl.setStatus(_A)
_AgentBscFileServerTftpPort_Type=Integer32
_AgentBscFileServerTftpPort_Object=MibTableColumn
agentBscFileServerTftpPort=_AgentBscFileServerTftpPort_Object((1,3,6,1,4,1,232,161,3,1,2,1,1,9),_AgentBscFileServerTftpPort_Type())
agentBscFileServerTftpPort.setMaxAccess(_C)
if mibBuilder.loadTexts:agentBscFileServerTftpPort.setStatus(_A)
class _AgentBscSwFileTime_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_AgentBscSwFileTime_Type.__name__=_G
_AgentBscSwFileTime_Object=MibTableColumn
agentBscSwFileTime=_AgentBscSwFileTime_Object((1,3,6,1,4,1,232,161,3,1,2,1,1,10),_AgentBscSwFileTime_Type())
agentBscSwFileTime.setMaxAccess(_D)
if mibBuilder.loadTexts:agentBscSwFileTime.setStatus(_A)
class _AgentBscSwFileStatus_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,256))
_AgentBscSwFileStatus_Type.__name__=_G
_AgentBscSwFileStatus_Object=MibTableColumn
agentBscSwFileStatus=_AgentBscSwFileStatus_Object((1,3,6,1,4,1,232,161,3,1,2,1,1,11),_AgentBscSwFileStatus_Type())
agentBscSwFileStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:agentBscSwFileStatus.setStatus(_A)
class _AgentFileTransfer_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_F,1),('start',2),('start-and-reset',3),('noaction',4)))
_AgentFileTransfer_Type.__name__=_B
_AgentFileTransfer_Object=MibScalar
agentFileTransfer=_AgentFileTransfer_Object((1,3,6,1,4,1,232,161,3,1,2,2),_AgentFileTransfer_Type())
agentFileTransfer.setMaxAccess(_C)
if mibBuilder.loadTexts:agentFileTransfer.setStatus(_P)
class _AgentSystemReset_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_F,1),('cold-start',2),('warm-start',3),('no-reset',4)))
_AgentSystemReset_Type.__name__=_B
_AgentSystemReset_Object=MibScalar
agentSystemReset=_AgentSystemReset_Object((1,3,6,1,4,1,232,161,3,1,2,3),_AgentSystemReset_Type())
agentSystemReset.setMaxAccess(_C)
if mibBuilder.loadTexts:agentSystemReset.setStatus(_A)
class _AgentRs232PortConfig_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_F,1),('console',2),('out-of-band',3),('notAvail',4)))
_AgentRs232PortConfig_Type.__name__=_B
_AgentRs232PortConfig_Object=MibScalar
agentRs232PortConfig=_AgentRs232PortConfig_Object((1,3,6,1,4,1,232,161,3,1,2,4),_AgentRs232PortConfig_Type())
agentRs232PortConfig.setMaxAccess(_C)
if mibBuilder.loadTexts:agentRs232PortConfig.setStatus(_A)
class _AgentOutOfBandBaudRateConfig_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*((_F,1),(_Q,2),(_R,3),(_S,4),(_T,5),(_U,6)))
_AgentOutOfBandBaudRateConfig_Type.__name__=_B
_AgentOutOfBandBaudRateConfig_Object=MibScalar
agentOutOfBandBaudRateConfig=_AgentOutOfBandBaudRateConfig_Object((1,3,6,1,4,1,232,161,3,1,2,5),_AgentOutOfBandBaudRateConfig_Type())
agentOutOfBandBaudRateConfig.setMaxAccess(_C)
if mibBuilder.loadTexts:agentOutOfBandBaudRateConfig.setStatus(_P)
class _AgentSaveCfg_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_F,1),('idle',2),('set',3)))
_AgentSaveCfg_Type.__name__=_B
_AgentSaveCfg_Object=MibScalar
agentSaveCfg=_AgentSaveCfg_Object((1,3,6,1,4,1,232,161,3,1,2,6),_AgentSaveCfg_Type())
agentSaveCfg.setMaxAccess(_C)
if mibBuilder.loadTexts:agentSaveCfg.setStatus(_A)
_AgentIpProtoConfig_ObjectIdentity=ObjectIdentity
agentIpProtoConfig=_AgentIpProtoConfig_ObjectIdentity((1,3,6,1,4,1,232,161,3,1,3))
_AgentIpNumOfIf_Type=Integer32
_AgentIpNumOfIf_Object=MibScalar
agentIpNumOfIf=_AgentIpNumOfIf_Object((1,3,6,1,4,1,232,161,3,1,3,1),_AgentIpNumOfIf_Type())
agentIpNumOfIf.setMaxAccess(_D)
if mibBuilder.loadTexts:agentIpNumOfIf.setStatus(_A)
_AgentIpTftpServerAddr_Type=IpAddress
_AgentIpTftpServerAddr_Object=MibScalar
agentIpTftpServerAddr=_AgentIpTftpServerAddr_Object((1,3,6,1,4,1,232,161,3,1,3,2),_AgentIpTftpServerAddr_Type())
agentIpTftpServerAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:agentIpTftpServerAddr.setStatus(_P)
class _AgentIpGetIpFrom_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_F,1),(_V,2),('bootp',3),('dhcp',4)))
_AgentIpGetIpFrom_Type.__name__=_B
_AgentIpGetIpFrom_Object=MibScalar
agentIpGetIpFrom=_AgentIpGetIpFrom_Object((1,3,6,1,4,1,232,161,3,1,3,3),_AgentIpGetIpFrom_Type())
agentIpGetIpFrom.setMaxAccess(_C)
if mibBuilder.loadTexts:agentIpGetIpFrom.setStatus(_A)
_AgentIpTrapManager_ObjectIdentity=ObjectIdentity
agentIpTrapManager=_AgentIpTrapManager_ObjectIdentity((1,3,6,1,4,1,232,161,3,1,4))
_AgentIpTrapManagerTable_Object=MibTable
agentIpTrapManagerTable=_AgentIpTrapManagerTable_Object((1,3,6,1,4,1,232,161,3,1,4,1))
if mibBuilder.loadTexts:agentIpTrapManagerTable.setStatus(_A)
_AgentIpTrapManagerEntry_Object=MibTableRow
agentIpTrapManagerEntry=_AgentIpTrapManagerEntry_Object((1,3,6,1,4,1,232,161,3,1,4,1,1))
agentIpTrapManagerEntry.setIndexNames((0,_H,_Z))
if mibBuilder.loadTexts:agentIpTrapManagerEntry.setStatus(_A)
_AgentIpTrapManagerIpAddr_Type=IpAddress
_AgentIpTrapManagerIpAddr_Object=MibTableColumn
agentIpTrapManagerIpAddr=_AgentIpTrapManagerIpAddr_Object((1,3,6,1,4,1,232,161,3,1,4,1,1,1),_AgentIpTrapManagerIpAddr_Type())
agentIpTrapManagerIpAddr.setMaxAccess(_D)
if mibBuilder.loadTexts:agentIpTrapManagerIpAddr.setStatus(_A)
class _AgentIpTrapManagerComm_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,20))
_AgentIpTrapManagerComm_Type.__name__=_G
_AgentIpTrapManagerComm_Object=MibTableColumn
agentIpTrapManagerComm=_AgentIpTrapManagerComm_Object((1,3,6,1,4,1,232,161,3,1,4,1,1,2),_AgentIpTrapManagerComm_Type())
agentIpTrapManagerComm.setMaxAccess(_C)
if mibBuilder.loadTexts:agentIpTrapManagerComm.setStatus(_A)
class _AgentIpTrapManagerStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_F,1),(_V,2),(_a,3)))
_AgentIpTrapManagerStatus_Type.__name__=_B
_AgentIpTrapManagerStatus_Object=MibTableColumn
agentIpTrapManagerStatus=_AgentIpTrapManagerStatus_Object((1,3,6,1,4,1,232,161,3,1,4,1,1,3),_AgentIpTrapManagerStatus_Type())
agentIpTrapManagerStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:agentIpTrapManagerStatus.setStatus(_A)
_AgentConsoleModeManager_ObjectIdentity=ObjectIdentity
agentConsoleModeManager=_AgentConsoleModeManager_ObjectIdentity((1,3,6,1,4,1,232,161,3,1,5))
class _AgentConsoleModeManagerDataBits_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_F,1),('bits-7',2),('bits-8',3)))
_AgentConsoleModeManagerDataBits_Type.__name__=_B
_AgentConsoleModeManagerDataBits_Object=MibScalar
agentConsoleModeManagerDataBits=_AgentConsoleModeManagerDataBits_Object((1,3,6,1,4,1,232,161,3,1,5,1),_AgentConsoleModeManagerDataBits_Type())
agentConsoleModeManagerDataBits.setMaxAccess(_C)
if mibBuilder.loadTexts:agentConsoleModeManagerDataBits.setStatus(_A)
class _AgentConsoleModeManagerStopBits_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_F,1),('stopbits-1',2),('stopbits-2',3)))
_AgentConsoleModeManagerStopBits_Type.__name__=_B
_AgentConsoleModeManagerStopBits_Object=MibScalar
agentConsoleModeManagerStopBits=_AgentConsoleModeManagerStopBits_Object((1,3,6,1,4,1,232,161,3,1,5,2),_AgentConsoleModeManagerStopBits_Type())
agentConsoleModeManagerStopBits.setMaxAccess(_C)
if mibBuilder.loadTexts:agentConsoleModeManagerStopBits.setStatus(_A)
class _AgentConsoleModeManagerParity_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('none',1),('odd',2),('even',3)))
_AgentConsoleModeManagerParity_Type.__name__=_B
_AgentConsoleModeManagerParity_Object=MibScalar
agentConsoleModeManagerParity=_AgentConsoleModeManagerParity_Object((1,3,6,1,4,1,232,161,3,1,5,3),_AgentConsoleModeManagerParity_Type())
agentConsoleModeManagerParity.setMaxAccess(_C)
if mibBuilder.loadTexts:agentConsoleModeManagerParity.setStatus(_A)
class _AgentConsoleModeManagerBaudRate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*((_F,1),(_Q,2),(_R,3),(_S,4),(_T,5),(_b,6),(_U,7)))
_AgentConsoleModeManagerBaudRate_Type.__name__=_B
_AgentConsoleModeManagerBaudRate_Object=MibScalar
agentConsoleModeManagerBaudRate=_AgentConsoleModeManagerBaudRate_Object((1,3,6,1,4,1,232,161,3,1,5,4),_AgentConsoleModeManagerBaudRate_Type())
agentConsoleModeManagerBaudRate.setMaxAccess(_C)
if mibBuilder.loadTexts:agentConsoleModeManagerBaudRate.setStatus(_A)
_AgentSlipModeManager_ObjectIdentity=ObjectIdentity
agentSlipModeManager=_AgentSlipModeManager_ObjectIdentity((1,3,6,1,4,1,232,161,3,1,6))
_AgentSlipModeManagerLocalIP_Type=IpAddress
_AgentSlipModeManagerLocalIP_Object=MibScalar
agentSlipModeManagerLocalIP=_AgentSlipModeManagerLocalIP_Object((1,3,6,1,4,1,232,161,3,1,6,1),_AgentSlipModeManagerLocalIP_Type())
agentSlipModeManagerLocalIP.setMaxAccess(_C)
if mibBuilder.loadTexts:agentSlipModeManagerLocalIP.setStatus(_A)
_AgentSlipModeManagerRemoteIP_Type=IpAddress
_AgentSlipModeManagerRemoteIP_Object=MibScalar
agentSlipModeManagerRemoteIP=_AgentSlipModeManagerRemoteIP_Object((1,3,6,1,4,1,232,161,3,1,6,2),_AgentSlipModeManagerRemoteIP_Type())
agentSlipModeManagerRemoteIP.setMaxAccess(_C)
if mibBuilder.loadTexts:agentSlipModeManagerRemoteIP.setStatus(_A)
class _AgentSlipModeManagerMTU_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_F,1),('mtu-1006',2),('mtu-1500',3)))
_AgentSlipModeManagerMTU_Type.__name__=_B
_AgentSlipModeManagerMTU_Object=MibScalar
agentSlipModeManagerMTU=_AgentSlipModeManagerMTU_Object((1,3,6,1,4,1,232,161,3,1,6,3),_AgentSlipModeManagerMTU_Type())
agentSlipModeManagerMTU.setMaxAccess(_C)
if mibBuilder.loadTexts:agentSlipModeManagerMTU.setStatus(_A)
class _AgentSlipModeManagerBaudRate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*((_F,1),(_Q,2),(_R,3),(_S,4),(_T,5),(_b,6),(_U,7)))
_AgentSlipModeManagerBaudRate_Type.__name__=_B
_AgentSlipModeManagerBaudRate_Object=MibScalar
agentSlipModeManagerBaudRate=_AgentSlipModeManagerBaudRate_Object((1,3,6,1,4,1,232,161,3,1,6,4),_AgentSlipModeManagerBaudRate_Type())
agentSlipModeManagerBaudRate.setMaxAccess(_C)
if mibBuilder.loadTexts:agentSlipModeManagerBaudRate.setStatus(_A)
_AgentSNTP_ObjectIdentity=ObjectIdentity
agentSNTP=_AgentSNTP_ObjectIdentity((1,3,6,1,4,1,232,161,3,1,7))
class _AgentSNTPState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_F,1),(_V,2),(_a,3)))
_AgentSNTPState_Type.__name__=_B
_AgentSNTPState_Object=MibScalar
agentSNTPState=_AgentSNTPState_Object((1,3,6,1,4,1,232,161,3,1,7,1),_AgentSNTPState_Type())
agentSNTPState.setMaxAccess(_C)
if mibBuilder.loadTexts:agentSNTPState.setStatus(_A)
class _AgentSNTPTimeSource_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('system',0),('server1',1),('server2',2)))
_AgentSNTPTimeSource_Type.__name__=_B
_AgentSNTPTimeSource_Object=MibScalar
agentSNTPTimeSource=_AgentSNTPTimeSource_Object((1,3,6,1,4,1,232,161,3,1,7,2),_AgentSNTPTimeSource_Type())
agentSNTPTimeSource.setMaxAccess(_D)
if mibBuilder.loadTexts:agentSNTPTimeSource.setStatus(_A)
_AgentSNTPServer1IPAddr_Type=IpAddress
_AgentSNTPServer1IPAddr_Object=MibScalar
agentSNTPServer1IPAddr=_AgentSNTPServer1IPAddr_Object((1,3,6,1,4,1,232,161,3,1,7,3),_AgentSNTPServer1IPAddr_Type())
agentSNTPServer1IPAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:agentSNTPServer1IPAddr.setStatus(_A)
_AgentSNTPServer2IPAddr_Type=IpAddress
_AgentSNTPServer2IPAddr_Object=MibScalar
agentSNTPServer2IPAddr=_AgentSNTPServer2IPAddr_Object((1,3,6,1,4,1,232,161,3,1,7,4),_AgentSNTPServer2IPAddr_Type())
agentSNTPServer2IPAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:agentSNTPServer2IPAddr.setStatus(_A)
class _AgentSNTPTimeZone_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-779,839))
_AgentSNTPTimeZone_Type.__name__=_B
_AgentSNTPTimeZone_Object=MibScalar
agentSNTPTimeZone=_AgentSNTPTimeZone_Object((1,3,6,1,4,1,232,161,3,1,7,5),_AgentSNTPTimeZone_Type())
agentSNTPTimeZone.setMaxAccess(_C)
if mibBuilder.loadTexts:agentSNTPTimeZone.setStatus(_A)
class _AgentSNTPPollInterval_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(30,99999))
_AgentSNTPPollInterval_Type.__name__=_B
_AgentSNTPPollInterval_Object=MibScalar
agentSNTPPollInterval=_AgentSNTPPollInterval_Object((1,3,6,1,4,1,232,161,3,1,7,6),_AgentSNTPPollInterval_Type())
agentSNTPPollInterval.setMaxAccess(_C)
if mibBuilder.loadTexts:agentSNTPPollInterval.setStatus(_A)
class _AgentSNTPCurrentTime_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_AgentSNTPCurrentTime_Type.__name__=_G
_AgentSNTPCurrentTime_Object=MibScalar
agentSNTPCurrentTime=_AgentSNTPCurrentTime_Object((1,3,6,1,4,1,232,161,3,1,7,7),_AgentSNTPCurrentTime_Type())
agentSNTPCurrentTime.setMaxAccess(_D)
if mibBuilder.loadTexts:agentSNTPCurrentTime.setStatus(_A)
_AgentSNTPUpTime_Type=Integer32
_AgentSNTPUpTime_Object=MibScalar
agentSNTPUpTime=_AgentSNTPUpTime_Object((1,3,6,1,4,1,232,161,3,1,7,8),_AgentSNTPUpTime_Type())
agentSNTPUpTime.setMaxAccess(_D)
if mibBuilder.loadTexts:agentSNTPUpTime.setStatus(_A)
class _AgentSNTPBootTime_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_AgentSNTPBootTime_Type.__name__=_G
_AgentSNTPBootTime_Object=MibScalar
agentSNTPBootTime=_AgentSNTPBootTime_Object((1,3,6,1,4,1,232,161,3,1,7,9),_AgentSNTPBootTime_Type())
agentSNTPBootTime.setMaxAccess(_D)
if mibBuilder.loadTexts:agentSNTPBootTime.setStatus(_A)
_AgentDST_ObjectIdentity=ObjectIdentity
agentDST=_AgentDST_ObjectIdentity((1,3,6,1,4,1,232,161,3,1,8))
class _AgentDSTStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('disable',1),('repeating',2),('annual',3)))
_AgentDSTStatus_Type.__name__=_B
_AgentDSTStatus_Object=MibScalar
agentDSTStatus=_AgentDSTStatus_Object((1,3,6,1,4,1,232,161,3,1,8,1),_AgentDSTStatus_Type())
agentDSTStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:agentDSTStatus.setStatus(_A)
class _AgentDSTOffset_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1440))
_AgentDSTOffset_Type.__name__=_B
_AgentDSTOffset_Object=MibScalar
agentDSTOffset=_AgentDSTOffset_Object((1,3,6,1,4,1,232,161,3,1,8,2),_AgentDSTOffset_Type())
agentDSTOffset.setMaxAccess(_C)
if mibBuilder.loadTexts:agentDSTOffset.setStatus(_A)
class _AgentDSTRepeatingStartMonth_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,12))
_AgentDSTRepeatingStartMonth_Type.__name__=_B
_AgentDSTRepeatingStartMonth_Object=MibScalar
agentDSTRepeatingStartMonth=_AgentDSTRepeatingStartMonth_Object((1,3,6,1,4,1,232,161,3,1,8,3),_AgentDSTRepeatingStartMonth_Type())
agentDSTRepeatingStartMonth.setMaxAccess(_C)
if mibBuilder.loadTexts:agentDSTRepeatingStartMonth.setStatus(_A)
class _AgentDSTRepeatingStartWhichDay_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4))
_AgentDSTRepeatingStartWhichDay_Type.__name__=_B
_AgentDSTRepeatingStartWhichDay_Object=MibScalar
agentDSTRepeatingStartWhichDay=_AgentDSTRepeatingStartWhichDay_Object((1,3,6,1,4,1,232,161,3,1,8,4),_AgentDSTRepeatingStartWhichDay_Type())
agentDSTRepeatingStartWhichDay.setMaxAccess(_C)
if mibBuilder.loadTexts:agentDSTRepeatingStartWhichDay.setStatus(_A)
class _AgentDSTRepeatingStartDayOfWeek_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,7))
_AgentDSTRepeatingStartDayOfWeek_Type.__name__=_B
_AgentDSTRepeatingStartDayOfWeek_Object=MibScalar
agentDSTRepeatingStartDayOfWeek=_AgentDSTRepeatingStartDayOfWeek_Object((1,3,6,1,4,1,232,161,3,1,8,5),_AgentDSTRepeatingStartDayOfWeek_Type())
agentDSTRepeatingStartDayOfWeek.setMaxAccess(_C)
if mibBuilder.loadTexts:agentDSTRepeatingStartDayOfWeek.setStatus(_A)
class _AgentDSTRepeatingStartHour_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,23))
_AgentDSTRepeatingStartHour_Type.__name__=_B
_AgentDSTRepeatingStartHour_Object=MibScalar
agentDSTRepeatingStartHour=_AgentDSTRepeatingStartHour_Object((1,3,6,1,4,1,232,161,3,1,8,6),_AgentDSTRepeatingStartHour_Type())
agentDSTRepeatingStartHour.setMaxAccess(_C)
if mibBuilder.loadTexts:agentDSTRepeatingStartHour.setStatus(_A)
class _AgentDSTRepeatingStartMinute_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,59))
_AgentDSTRepeatingStartMinute_Type.__name__=_B
_AgentDSTRepeatingStartMinute_Object=MibScalar
agentDSTRepeatingStartMinute=_AgentDSTRepeatingStartMinute_Object((1,3,6,1,4,1,232,161,3,1,8,7),_AgentDSTRepeatingStartMinute_Type())
agentDSTRepeatingStartMinute.setMaxAccess(_C)
if mibBuilder.loadTexts:agentDSTRepeatingStartMinute.setStatus(_A)
class _AgentDSTRepeatingEndMonth_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,12))
_AgentDSTRepeatingEndMonth_Type.__name__=_B
_AgentDSTRepeatingEndMonth_Object=MibScalar
agentDSTRepeatingEndMonth=_AgentDSTRepeatingEndMonth_Object((1,3,6,1,4,1,232,161,3,1,8,8),_AgentDSTRepeatingEndMonth_Type())
agentDSTRepeatingEndMonth.setMaxAccess(_C)
if mibBuilder.loadTexts:agentDSTRepeatingEndMonth.setStatus(_A)
class _AgentDSTRepeatingEndWhichDay_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4))
_AgentDSTRepeatingEndWhichDay_Type.__name__=_B
_AgentDSTRepeatingEndWhichDay_Object=MibScalar
agentDSTRepeatingEndWhichDay=_AgentDSTRepeatingEndWhichDay_Object((1,3,6,1,4,1,232,161,3,1,8,9),_AgentDSTRepeatingEndWhichDay_Type())
agentDSTRepeatingEndWhichDay.setMaxAccess(_C)
if mibBuilder.loadTexts:agentDSTRepeatingEndWhichDay.setStatus(_A)
class _AgentDSTRepeatingEndDayOfWeek_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,7))
_AgentDSTRepeatingEndDayOfWeek_Type.__name__=_B
_AgentDSTRepeatingEndDayOfWeek_Object=MibScalar
agentDSTRepeatingEndDayOfWeek=_AgentDSTRepeatingEndDayOfWeek_Object((1,3,6,1,4,1,232,161,3,1,8,10),_AgentDSTRepeatingEndDayOfWeek_Type())
agentDSTRepeatingEndDayOfWeek.setMaxAccess(_C)
if mibBuilder.loadTexts:agentDSTRepeatingEndDayOfWeek.setStatus(_A)
class _AgentDSTRepeatingEndHour_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,23))
_AgentDSTRepeatingEndHour_Type.__name__=_B
_AgentDSTRepeatingEndHour_Object=MibScalar
agentDSTRepeatingEndHour=_AgentDSTRepeatingEndHour_Object((1,3,6,1,4,1,232,161,3,1,8,11),_AgentDSTRepeatingEndHour_Type())
agentDSTRepeatingEndHour.setMaxAccess(_C)
if mibBuilder.loadTexts:agentDSTRepeatingEndHour.setStatus(_A)
class _AgentDSTRepeatingEndMinute_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,59))
_AgentDSTRepeatingEndMinute_Type.__name__=_B
_AgentDSTRepeatingEndMinute_Object=MibScalar
agentDSTRepeatingEndMinute=_AgentDSTRepeatingEndMinute_Object((1,3,6,1,4,1,232,161,3,1,8,12),_AgentDSTRepeatingEndMinute_Type())
agentDSTRepeatingEndMinute.setMaxAccess(_C)
if mibBuilder.loadTexts:agentDSTRepeatingEndMinute.setStatus(_A)
class _AgentDSTAnnualStartMonth_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,12))
_AgentDSTAnnualStartMonth_Type.__name__=_B
_AgentDSTAnnualStartMonth_Object=MibScalar
agentDSTAnnualStartMonth=_AgentDSTAnnualStartMonth_Object((1,3,6,1,4,1,232,161,3,1,8,13),_AgentDSTAnnualStartMonth_Type())
agentDSTAnnualStartMonth.setMaxAccess(_C)
if mibBuilder.loadTexts:agentDSTAnnualStartMonth.setStatus(_A)
class _AgentDSTAnnualStartDayOfMonth_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,31))
_AgentDSTAnnualStartDayOfMonth_Type.__name__=_B
_AgentDSTAnnualStartDayOfMonth_Object=MibScalar
agentDSTAnnualStartDayOfMonth=_AgentDSTAnnualStartDayOfMonth_Object((1,3,6,1,4,1,232,161,3,1,8,14),_AgentDSTAnnualStartDayOfMonth_Type())
agentDSTAnnualStartDayOfMonth.setMaxAccess(_C)
if mibBuilder.loadTexts:agentDSTAnnualStartDayOfMonth.setStatus(_A)
class _AgentDSTAnnualStartHour_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,23))
_AgentDSTAnnualStartHour_Type.__name__=_B
_AgentDSTAnnualStartHour_Object=MibScalar
agentDSTAnnualStartHour=_AgentDSTAnnualStartHour_Object((1,3,6,1,4,1,232,161,3,1,8,15),_AgentDSTAnnualStartHour_Type())
agentDSTAnnualStartHour.setMaxAccess(_C)
if mibBuilder.loadTexts:agentDSTAnnualStartHour.setStatus(_A)
class _AgentDSTAnnualStartMinute_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,59))
_AgentDSTAnnualStartMinute_Type.__name__=_B
_AgentDSTAnnualStartMinute_Object=MibScalar
agentDSTAnnualStartMinute=_AgentDSTAnnualStartMinute_Object((1,3,6,1,4,1,232,161,3,1,8,16),_AgentDSTAnnualStartMinute_Type())
agentDSTAnnualStartMinute.setMaxAccess(_C)
if mibBuilder.loadTexts:agentDSTAnnualStartMinute.setStatus(_A)
class _AgentDSTAnnualEndMonth_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,12))
_AgentDSTAnnualEndMonth_Type.__name__=_B
_AgentDSTAnnualEndMonth_Object=MibScalar
agentDSTAnnualEndMonth=_AgentDSTAnnualEndMonth_Object((1,3,6,1,4,1,232,161,3,1,8,17),_AgentDSTAnnualEndMonth_Type())
agentDSTAnnualEndMonth.setMaxAccess(_C)
if mibBuilder.loadTexts:agentDSTAnnualEndMonth.setStatus(_A)
class _AgentDSTAnnualEndDayOfMonth_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,31))
_AgentDSTAnnualEndDayOfMonth_Type.__name__=_B
_AgentDSTAnnualEndDayOfMonth_Object=MibScalar
agentDSTAnnualEndDayOfMonth=_AgentDSTAnnualEndDayOfMonth_Object((1,3,6,1,4,1,232,161,3,1,8,18),_AgentDSTAnnualEndDayOfMonth_Type())
agentDSTAnnualEndDayOfMonth.setMaxAccess(_C)
if mibBuilder.loadTexts:agentDSTAnnualEndDayOfMonth.setStatus(_A)
class _AgentDSTAnnualEndHour_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,23))
_AgentDSTAnnualEndHour_Type.__name__=_B
_AgentDSTAnnualEndHour_Object=MibScalar
agentDSTAnnualEndHour=_AgentDSTAnnualEndHour_Object((1,3,6,1,4,1,232,161,3,1,8,19),_AgentDSTAnnualEndHour_Type())
agentDSTAnnualEndHour.setMaxAccess(_C)
if mibBuilder.loadTexts:agentDSTAnnualEndHour.setStatus(_A)
class _AgentDSTAnnualEndMinute_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,59))
_AgentDSTAnnualEndMinute_Type.__name__=_B
_AgentDSTAnnualEndMinute_Object=MibScalar
agentDSTAnnualEndMinute=_AgentDSTAnnualEndMinute_Object((1,3,6,1,4,1,232,161,3,1,8,20),_AgentDSTAnnualEndMinute_Type())
agentDSTAnnualEndMinute.setMaxAccess(_C)
if mibBuilder.loadTexts:agentDSTAnnualEndMinute.setStatus(_A)
_AgentSwitchCommonMgmt_ObjectIdentity=ObjectIdentity
agentSwitchCommonMgmt=_AgentSwitchCommonMgmt_ObjectIdentity((1,3,6,1,4,1,232,161,3,3))
_AgentSwitchCube_ObjectIdentity=ObjectIdentity
agentSwitchCube=_AgentSwitchCube_ObjectIdentity((1,3,6,1,4,1,232,161,3,3,1))
_AgentSwitchCubeTable_Object=MibTable
agentSwitchCubeTable=_AgentSwitchCubeTable_Object((1,3,6,1,4,1,232,161,3,3,1,1))
if mibBuilder.loadTexts:agentSwitchCubeTable.setStatus(_A)
_AgentSwitchCubeEntry_Object=MibTableRow
agentSwitchCubeEntry=_AgentSwitchCubeEntry_Object((1,3,6,1,4,1,232,161,3,3,1,1,1))
agentSwitchCubeEntry.setIndexNames((0,_E,_I),(0,_E,_K),(0,_E,_J),(0,_E,_N),(0,_E,_L),(0,_E,_M),(0,_H,_c))
if mibBuilder.loadTexts:agentSwitchCubeEntry.setStatus(_A)
class _AgentSwitchCubeType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_F,1),('dualTSX',2),('quadT',3)))
_AgentSwitchCubeType_Type.__name__=_B
_AgentSwitchCubeType_Object=MibTableColumn
agentSwitchCubeType=_AgentSwitchCubeType_Object((1,3,6,1,4,1,232,161,3,3,1,1,1,1),_AgentSwitchCubeType_Type())
agentSwitchCubeType.setMaxAccess(_D)
if mibBuilder.loadTexts:agentSwitchCubeType.setStatus(_A)
class _AgentSwitchCubeSpareName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_AgentSwitchCubeSpareName_Type.__name__=_G
_AgentSwitchCubeSpareName_Object=MibTableColumn
agentSwitchCubeSpareName=_AgentSwitchCubeSpareName_Object((1,3,6,1,4,1,232,161,3,3,1,1,1,2),_AgentSwitchCubeSpareName_Type())
agentSwitchCubeSpareName.setMaxAccess(_D)
if mibBuilder.loadTexts:agentSwitchCubeSpareName.setStatus(_A)
class _AgentSwitchCubeSparePartNumber_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_AgentSwitchCubeSparePartNumber_Type.__name__=_G
_AgentSwitchCubeSparePartNumber_Object=MibTableColumn
agentSwitchCubeSparePartNumber=_AgentSwitchCubeSparePartNumber_Object((1,3,6,1,4,1,232,161,3,3,1,1,1,3),_AgentSwitchCubeSparePartNumber_Type())
agentSwitchCubeSparePartNumber.setMaxAccess(_D)
if mibBuilder.loadTexts:agentSwitchCubeSparePartNumber.setStatus(_A)
_AgentSwitchPowerSupply_ObjectIdentity=ObjectIdentity
agentSwitchPowerSupply=_AgentSwitchPowerSupply_ObjectIdentity((1,3,6,1,4,1,232,161,3,3,2))
_AgentSwitchPowerSupplyTable_Object=MibTable
agentSwitchPowerSupplyTable=_AgentSwitchPowerSupplyTable_Object((1,3,6,1,4,1,232,161,3,3,2,1))
if mibBuilder.loadTexts:agentSwitchPowerSupplyTable.setStatus(_A)
_AgentSwitchPowerSupplyEntry_Object=MibTableRow
agentSwitchPowerSupplyEntry=_AgentSwitchPowerSupplyEntry_Object((1,3,6,1,4,1,232,161,3,3,2,1,1))
agentSwitchPowerSupplyEntry.setIndexNames((0,_E,_I),(0,_E,_K),(0,_E,_J),(0,_E,_N),(0,_E,_L),(0,_E,_M),(0,_H,_d))
if mibBuilder.loadTexts:agentSwitchPowerSupplyEntry.setStatus(_A)
_AgentSwitchPowerSupplyIndex_Type=Integer32
_AgentSwitchPowerSupplyIndex_Object=MibTableColumn
agentSwitchPowerSupplyIndex=_AgentSwitchPowerSupplyIndex_Object((1,3,6,1,4,1,232,161,3,3,2,1,1,1),_AgentSwitchPowerSupplyIndex_Type())
agentSwitchPowerSupplyIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:agentSwitchPowerSupplyIndex.setStatus(_A)
_AgentSwitchPowerSupplyMaxPwrOutput_Type=Integer32
_AgentSwitchPowerSupplyMaxPwrOutput_Object=MibTableColumn
agentSwitchPowerSupplyMaxPwrOutput=_AgentSwitchPowerSupplyMaxPwrOutput_Object((1,3,6,1,4,1,232,161,3,3,2,1,1,2),_AgentSwitchPowerSupplyMaxPwrOutput_Type())
agentSwitchPowerSupplyMaxPwrOutput.setMaxAccess(_D)
if mibBuilder.loadTexts:agentSwitchPowerSupplyMaxPwrOutput.setStatus(_A)
_AgentSwitchPowerSupplyCurPwrOutput_Type=Integer32
_AgentSwitchPowerSupplyCurPwrOutput_Object=MibTableColumn
agentSwitchPowerSupplyCurPwrOutput=_AgentSwitchPowerSupplyCurPwrOutput_Object((1,3,6,1,4,1,232,161,3,3,2,1,1,3),_AgentSwitchPowerSupplyCurPwrOutput_Type())
agentSwitchPowerSupplyCurPwrOutput.setMaxAccess(_D)
if mibBuilder.loadTexts:agentSwitchPowerSupplyCurPwrOutput.setStatus(_A)
_AgentSwitchPowerSupplyIntakeTemp_Type=Integer32
_AgentSwitchPowerSupplyIntakeTemp_Object=MibTableColumn
agentSwitchPowerSupplyIntakeTemp=_AgentSwitchPowerSupplyIntakeTemp_Object((1,3,6,1,4,1,232,161,3,3,2,1,1,4),_AgentSwitchPowerSupplyIntakeTemp_Type())
agentSwitchPowerSupplyIntakeTemp.setMaxAccess(_D)
if mibBuilder.loadTexts:agentSwitchPowerSupplyIntakeTemp.setStatus(_A)
_AgentSwitchPowerSupplyExhaustTemp_Type=Integer32
_AgentSwitchPowerSupplyExhaustTemp_Object=MibTableColumn
agentSwitchPowerSupplyExhaustTemp=_AgentSwitchPowerSupplyExhaustTemp_Object((1,3,6,1,4,1,232,161,3,3,2,1,1,5),_AgentSwitchPowerSupplyExhaustTemp_Type())
agentSwitchPowerSupplyExhaustTemp.setMaxAccess(_D)
if mibBuilder.loadTexts:agentSwitchPowerSupplyExhaustTemp.setStatus(_A)
class _AgentSwitchPowerSupplyStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16)));namedValues=NamedValues(*((_e,1),('generalFailure',2),('bistFailure',3),('fanFailure',4),('tempFailure',5),('interlockOpen',6),('epromFailed',7),('vrefFailed',8),('dacFailed',9),('ramTestFailed',10),('voltageChannelFailed',11),('orringdiodeFailed',12),(_f,13),('giveupOnStartup',14),('nvramInvalid',15),('calibrationTableInvalid',16)))
_AgentSwitchPowerSupplyStatus_Type.__name__=_B
_AgentSwitchPowerSupplyStatus_Object=MibTableColumn
agentSwitchPowerSupplyStatus=_AgentSwitchPowerSupplyStatus_Object((1,3,6,1,4,1,232,161,3,3,2,1,1,6),_AgentSwitchPowerSupplyStatus_Type())
agentSwitchPowerSupplyStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:agentSwitchPowerSupplyStatus.setStatus(_A)
class _AgentSwitchPowerSupplyInputLineStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*((_e,1),('lineOverVoltage',2),('lineUnderVoltage',3),('lineHit',4),(_f,5),('linePowerLoss',6)))
_AgentSwitchPowerSupplyInputLineStatus_Type.__name__=_B
_AgentSwitchPowerSupplyInputLineStatus_Object=MibTableColumn
agentSwitchPowerSupplyInputLineStatus=_AgentSwitchPowerSupplyInputLineStatus_Object((1,3,6,1,4,1,232,161,3,3,2,1,1,7),_AgentSwitchPowerSupplyInputLineStatus_Type())
agentSwitchPowerSupplyInputLineStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:agentSwitchPowerSupplyInputLineStatus.setStatus(_A)
class _AgentSwitchPowerSupplyCondition_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_F,1),('ok',2),(_W,3),(_O,4)))
_AgentSwitchPowerSupplyCondition_Type.__name__=_B
_AgentSwitchPowerSupplyCondition_Object=MibTableColumn
agentSwitchPowerSupplyCondition=_AgentSwitchPowerSupplyCondition_Object((1,3,6,1,4,1,232,161,3,3,2,1,1,8),_AgentSwitchPowerSupplyCondition_Type())
agentSwitchPowerSupplyCondition.setMaxAccess(_D)
if mibBuilder.loadTexts:agentSwitchPowerSupplyCondition.setStatus(_A)
_AgentSwitchFan_ObjectIdentity=ObjectIdentity
agentSwitchFan=_AgentSwitchFan_ObjectIdentity((1,3,6,1,4,1,232,161,3,3,3))
_AgentSwitchFanTable_Object=MibTable
agentSwitchFanTable=_AgentSwitchFanTable_Object((1,3,6,1,4,1,232,161,3,3,3,1))
if mibBuilder.loadTexts:agentSwitchFanTable.setStatus(_A)
_AgentSwitchFanEntry_Object=MibTableRow
agentSwitchFanEntry=_AgentSwitchFanEntry_Object((1,3,6,1,4,1,232,161,3,3,3,1,1))
agentSwitchFanEntry.setIndexNames((0,_E,_I),(0,_E,_K),(0,_E,_J),(0,_E,_N),(0,_E,_L),(0,_E,_M),(0,_H,_g))
if mibBuilder.loadTexts:agentSwitchFanEntry.setStatus(_A)
_AgentSwitchFanIndex_Type=Integer32
_AgentSwitchFanIndex_Object=MibTableColumn
agentSwitchFanIndex=_AgentSwitchFanIndex_Object((1,3,6,1,4,1,232,161,3,3,3,1,1,1),_AgentSwitchFanIndex_Type())
agentSwitchFanIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:agentSwitchFanIndex.setStatus(_A)
class _AgentSwitchFanCondition_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_F,1),('ok',2),(_W,3),(_O,4)))
_AgentSwitchFanCondition_Type.__name__=_B
_AgentSwitchFanCondition_Object=MibTableColumn
agentSwitchFanCondition=_AgentSwitchFanCondition_Object((1,3,6,1,4,1,232,161,3,3,3,1,1,2),_AgentSwitchFanCondition_Type())
agentSwitchFanCondition.setMaxAccess(_D)
if mibBuilder.loadTexts:agentSwitchFanCondition.setStatus(_A)
_AgentSwitchTempSensor_ObjectIdentity=ObjectIdentity
agentSwitchTempSensor=_AgentSwitchTempSensor_ObjectIdentity((1,3,6,1,4,1,232,161,3,3,4))
_AgentSwitchTempSensorTable_Object=MibTable
agentSwitchTempSensorTable=_AgentSwitchTempSensorTable_Object((1,3,6,1,4,1,232,161,3,3,4,1))
if mibBuilder.loadTexts:agentSwitchTempSensorTable.setStatus(_A)
_AgentSwitchTempSensorEntry_Object=MibTableRow
agentSwitchTempSensorEntry=_AgentSwitchTempSensorEntry_Object((1,3,6,1,4,1,232,161,3,3,4,1,1))
agentSwitchTempSensorEntry.setIndexNames((0,_E,_I),(0,_E,_K),(0,_E,_J),(0,_E,_N),(0,_E,_L),(0,_E,_M),(0,_H,_h))
if mibBuilder.loadTexts:agentSwitchTempSensorEntry.setStatus(_A)
_AgentSwitchTempSensorIndex_Type=Integer32
_AgentSwitchTempSensorIndex_Object=MibTableColumn
agentSwitchTempSensorIndex=_AgentSwitchTempSensorIndex_Object((1,3,6,1,4,1,232,161,3,3,4,1,1,1),_AgentSwitchTempSensorIndex_Type())
agentSwitchTempSensorIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:agentSwitchTempSensorIndex.setStatus(_A)
_AgentSwitchTempSensorCurrent_Type=Integer32
_AgentSwitchTempSensorCurrent_Object=MibTableColumn
agentSwitchTempSensorCurrent=_AgentSwitchTempSensorCurrent_Object((1,3,6,1,4,1,232,161,3,3,4,1,1,2),_AgentSwitchTempSensorCurrent_Type())
agentSwitchTempSensorCurrent.setMaxAccess(_D)
if mibBuilder.loadTexts:agentSwitchTempSensorCurrent.setStatus(_A)
_AgentSwitchTempSensorThreshold_Type=Integer32
_AgentSwitchTempSensorThreshold_Object=MibTableColumn
agentSwitchTempSensorThreshold=_AgentSwitchTempSensorThreshold_Object((1,3,6,1,4,1,232,161,3,3,4,1,1,3),_AgentSwitchTempSensorThreshold_Type())
agentSwitchTempSensorThreshold.setMaxAccess(_D)
if mibBuilder.loadTexts:agentSwitchTempSensorThreshold.setStatus(_A)
class _AgentSwitchTempSensorCondition_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_F,1),('ok',2),(_W,3),(_O,4)))
_AgentSwitchTempSensorCondition_Type.__name__=_B
_AgentSwitchTempSensorCondition_Object=MibTableColumn
agentSwitchTempSensorCondition=_AgentSwitchTempSensorCondition_Object((1,3,6,1,4,1,232,161,3,3,4,1,1,4),_AgentSwitchTempSensorCondition_Type())
agentSwitchTempSensorCondition.setMaxAccess(_D)
if mibBuilder.loadTexts:agentSwitchTempSensorCondition.setStatus(_A)
class _AgentSwitchTempSensorTempType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,5,9,15)));namedValues=NamedValues(*((_F,1),('blowout',5),('caution',9),('critical',15)))
_AgentSwitchTempSensorTempType_Type.__name__=_B
_AgentSwitchTempSensorTempType_Object=MibTableColumn
agentSwitchTempSensorTempType=_AgentSwitchTempSensorTempType_Object((1,3,6,1,4,1,232,161,3,3,4,1,1,5),_AgentSwitchTempSensorTempType_Type())
agentSwitchTempSensorTempType.setMaxAccess(_D)
if mibBuilder.loadTexts:agentSwitchTempSensorTempType.setStatus(_A)
_EndOfMIB_Type=Integer32
_EndOfMIB_Object=MibScalar
endOfMIB=_EndOfMIB_Object((1,3,6,1,4,1,232,161,3,3,9999),_EndOfMIB_Type())
endOfMIB.setMaxAccess(_D)
if mibBuilder.loadTexts:endOfMIB.setStatus(_A)
mibBuilder.exportSymbols(_H,**{'agentGeneralMgmt':agentGeneralMgmt,'agentBasicInfo':agentBasicInfo,'agentMgmtProtocolCapability':agentMgmtProtocolCapability,'agentMibCapabilityTable':agentMibCapabilityTable,'agentMibCapabilityEntry':agentMibCapabilityEntry,_X:agentMibCapabilityIndex,'agentMibCapabilityDescr':agentMibCapabilityDescr,'agentMibCapabilityVersion':agentMibCapabilityVersion,'agentMibCapabilityType':agentMibCapabilityType,'agentStatusConsoleInUse':agentStatusConsoleInUse,'agentStatusSaveCfg':agentStatusSaveCfg,'agentSwitchMfgDate':agentSwitchMfgDate,'agentSwitchFirmwareMfgDate':agentSwitchFirmwareMfgDate,'agentBasicConfig':agentBasicConfig,'agentBscSwFileTable':agentBscSwFileTable,'agentBscSwFileEntry':agentBscSwFileEntry,_Y:agentBscSwFileIndex,'agentBscSwFileDscr':agentBscSwFileDscr,'agentBscSwFileAddr':agentBscSwFileAddr,'agentBscSwFileTransferType':agentBscSwFileTransferType,'agentBscSwFile':agentBscSwFile,'agentBscSwFileLocateId':agentBscSwFileLocateId,'agentBscSwFileLoadType':agentBscSwFileLoadType,'agentBscSwFileCtrl':agentBscSwFileCtrl,'agentBscFileServerTftpPort':agentBscFileServerTftpPort,'agentBscSwFileTime':agentBscSwFileTime,'agentBscSwFileStatus':agentBscSwFileStatus,'agentFileTransfer':agentFileTransfer,'agentSystemReset':agentSystemReset,'agentRs232PortConfig':agentRs232PortConfig,'agentOutOfBandBaudRateConfig':agentOutOfBandBaudRateConfig,'agentSaveCfg':agentSaveCfg,'agentIpProtoConfig':agentIpProtoConfig,'agentIpNumOfIf':agentIpNumOfIf,'agentIpTftpServerAddr':agentIpTftpServerAddr,'agentIpGetIpFrom':agentIpGetIpFrom,'agentIpTrapManager':agentIpTrapManager,'agentIpTrapManagerTable':agentIpTrapManagerTable,'agentIpTrapManagerEntry':agentIpTrapManagerEntry,_Z:agentIpTrapManagerIpAddr,'agentIpTrapManagerComm':agentIpTrapManagerComm,'agentIpTrapManagerStatus':agentIpTrapManagerStatus,'agentConsoleModeManager':agentConsoleModeManager,'agentConsoleModeManagerDataBits':agentConsoleModeManagerDataBits,'agentConsoleModeManagerStopBits':agentConsoleModeManagerStopBits,'agentConsoleModeManagerParity':agentConsoleModeManagerParity,'agentConsoleModeManagerBaudRate':agentConsoleModeManagerBaudRate,'agentSlipModeManager':agentSlipModeManager,'agentSlipModeManagerLocalIP':agentSlipModeManagerLocalIP,'agentSlipModeManagerRemoteIP':agentSlipModeManagerRemoteIP,'agentSlipModeManagerMTU':agentSlipModeManagerMTU,'agentSlipModeManagerBaudRate':agentSlipModeManagerBaudRate,'agentSNTP':agentSNTP,'agentSNTPState':agentSNTPState,'agentSNTPTimeSource':agentSNTPTimeSource,'agentSNTPServer1IPAddr':agentSNTPServer1IPAddr,'agentSNTPServer2IPAddr':agentSNTPServer2IPAddr,'agentSNTPTimeZone':agentSNTPTimeZone,'agentSNTPPollInterval':agentSNTPPollInterval,'agentSNTPCurrentTime':agentSNTPCurrentTime,'agentSNTPUpTime':agentSNTPUpTime,'agentSNTPBootTime':agentSNTPBootTime,'agentDST':agentDST,'agentDSTStatus':agentDSTStatus,'agentDSTOffset':agentDSTOffset,'agentDSTRepeatingStartMonth':agentDSTRepeatingStartMonth,'agentDSTRepeatingStartWhichDay':agentDSTRepeatingStartWhichDay,'agentDSTRepeatingStartDayOfWeek':agentDSTRepeatingStartDayOfWeek,'agentDSTRepeatingStartHour':agentDSTRepeatingStartHour,'agentDSTRepeatingStartMinute':agentDSTRepeatingStartMinute,'agentDSTRepeatingEndMonth':agentDSTRepeatingEndMonth,'agentDSTRepeatingEndWhichDay':agentDSTRepeatingEndWhichDay,'agentDSTRepeatingEndDayOfWeek':agentDSTRepeatingEndDayOfWeek,'agentDSTRepeatingEndHour':agentDSTRepeatingEndHour,'agentDSTRepeatingEndMinute':agentDSTRepeatingEndMinute,'agentDSTAnnualStartMonth':agentDSTAnnualStartMonth,'agentDSTAnnualStartDayOfMonth':agentDSTAnnualStartDayOfMonth,'agentDSTAnnualStartHour':agentDSTAnnualStartHour,'agentDSTAnnualStartMinute':agentDSTAnnualStartMinute,'agentDSTAnnualEndMonth':agentDSTAnnualEndMonth,'agentDSTAnnualEndDayOfMonth':agentDSTAnnualEndDayOfMonth,'agentDSTAnnualEndHour':agentDSTAnnualEndHour,'agentDSTAnnualEndMinute':agentDSTAnnualEndMinute,'agentSwitchCommonMgmt':agentSwitchCommonMgmt,'agentSwitchCube':agentSwitchCube,'agentSwitchCubeTable':agentSwitchCubeTable,'agentSwitchCubeEntry':agentSwitchCubeEntry,_c:agentSwitchCubeType,'agentSwitchCubeSpareName':agentSwitchCubeSpareName,'agentSwitchCubeSparePartNumber':agentSwitchCubeSparePartNumber,'agentSwitchPowerSupply':agentSwitchPowerSupply,'agentSwitchPowerSupplyTable':agentSwitchPowerSupplyTable,'agentSwitchPowerSupplyEntry':agentSwitchPowerSupplyEntry,_d:agentSwitchPowerSupplyIndex,'agentSwitchPowerSupplyMaxPwrOutput':agentSwitchPowerSupplyMaxPwrOutput,'agentSwitchPowerSupplyCurPwrOutput':agentSwitchPowerSupplyCurPwrOutput,'agentSwitchPowerSupplyIntakeTemp':agentSwitchPowerSupplyIntakeTemp,'agentSwitchPowerSupplyExhaustTemp':agentSwitchPowerSupplyExhaustTemp,'agentSwitchPowerSupplyStatus':agentSwitchPowerSupplyStatus,'agentSwitchPowerSupplyInputLineStatus':agentSwitchPowerSupplyInputLineStatus,'agentSwitchPowerSupplyCondition':agentSwitchPowerSupplyCondition,'agentSwitchFan':agentSwitchFan,'agentSwitchFanTable':agentSwitchFanTable,'agentSwitchFanEntry':agentSwitchFanEntry,_g:agentSwitchFanIndex,'agentSwitchFanCondition':agentSwitchFanCondition,'agentSwitchTempSensor':agentSwitchTempSensor,'agentSwitchTempSensorTable':agentSwitchTempSensorTable,'agentSwitchTempSensorEntry':agentSwitchTempSensorEntry,_h:agentSwitchTempSensorIndex,'agentSwitchTempSensorCurrent':agentSwitchTempSensorCurrent,'agentSwitchTempSensorThreshold':agentSwitchTempSensorThreshold,'agentSwitchTempSensorCondition':agentSwitchTempSensorCondition,'agentSwitchTempSensorTempType':agentSwitchTempSensorTempType,'endOfMIB':endOfMIB})