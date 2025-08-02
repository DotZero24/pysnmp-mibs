_A3='wwpLeosBackupGatewayIPv6Group'
_A2='wwpLeosDefaultGatewayIPv6Group'
_A1='wwpLeosSystemFileSystemUtilizationSysfsState'
_A0='wwpLeosSystemFileSystemUtilizationSysfsCurrent'
_z='wwpLeosSystemFileSystemUtilizationTmpfsState'
_y='wwpLeosSystemFileSystemUtilizationTmpfsCurrent'
_x='wwpLeosSystemMemoryUtilizationAvailableMemoryState'
_w='wwpLeosSystemMemoryUtilizationAvailableMemoryCurrent'
_v='wwpLeosSystemCpuLoad15MinState'
_u='wwpLeosSystemCpuLoad15Min'
_t='wwpLeosSystemCpuLoad5MinState'
_s='wwpLeosSystemCpuLoad5Min'
_r='wwpLeosSystemCpuLoad1MinState'
_q='wwpLeosSystemCpuLoad1Min'
_p='wwpLeosSystemCpuUtilizationLast60SecondsState'
_o='wwpLeosSystemCpuUtilizationLast60Seconds'
_n='wwpLeosSystemCpuUtilizationLast10SecondsState'
_m='wwpLeosSystemCpuUtilizationLast10Seconds'
_l='wwpLeosSystemCpuUtilizationLast5SecondsState'
_k='wwpLeosSystemCpuUtilizationLast5Seconds'
_j='wwpLeosSystemConfigErrStr'
_i='wwpLeosSystemMemoryUsageMemoryAvailable'
_h='wwpLeosSystemMemoryUsageStatus'
_g='wwpLeosSystemMemoryUsageMemoryFree'
_f='wwpLeosSystemMemoryUsageMemoryTotal'
_e='wwpLeosSystemServiceMode'
_d='wwpLeosSystemConfigErrLinesTotal'
_c='wwpLeosSystemConfigBackupGatewayInetAddress'
_b='wwpLeosSystemConfigBackupGatewayInetAddrType'
_a='wwpLeosSystemConfigDefaultGatewayInetAddress'
_Z='wwpLeosSystemConfigDefaultGatewayInetAddrType'
_Y='wwpLeosSystemXFtpSFtpServerIndex'
_X='wwpLeosSystemXFtpFtpServerIndex'
_W='wwpLeosSystemXFtpTFtpServerIndex'
_V='wwpLeosSystemMemoryUsagePoolIndex'
_U='wwpLeosSystemConfigBackupGatewayIndex'
_T='wwpLeosSystemConfigDefaultGatewayIndex'
_S='wwpLeosSystemConfigErrLineNum'
_R='wwpLeosSystemConfigFileName'
_Q='disable'
_P='enable'
_O='wwpLeosSystemConfigFileIndex'
_N='none'
_M='DisplayString'
_L='bytes'
_K='not-accessible'
_J='faulted'
_I='degraded'
_H='warning'
_G='normal'
_F='read-create'
_E='read-write'
_D='WWP-LEOS-SYSTEM-CONFIG-MIB'
_C='read-only'
_B='Integer32'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress','InetAddressType')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_B,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DateAndTime,DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime',_M,'PhysAddress','RowStatus','TextualConvention','TruthValue')
wwpModulesLeos,=mibBuilder.importSymbols('WWP-SMI','wwpModulesLeos')
wwpLeosSystemConfigMIB=ModuleIdentity((1,3,6,1,4,1,6141,2,60,12))
if mibBuilder.loadTexts:wwpLeosSystemConfigMIB.setRevisions(('2012-09-19 00:00','2012-07-06 00:00','2012-06-27 00:00','2012-04-16 00:00','2011-11-05 00:00','2011-07-05 00:00','2002-03-16 00:00'))
class FileName(TextualConvention,OctetString):status=_A;displayHint='255a';subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,64))
_WwpLeosSystemConfigMIBObjects_ObjectIdentity=ObjectIdentity
wwpLeosSystemConfigMIBObjects=_WwpLeosSystemConfigMIBObjects_ObjectIdentity((1,3,6,1,4,1,6141,2,60,12,1))
_WwpLeosSystemConfigAttr_ObjectIdentity=ObjectIdentity
wwpLeosSystemConfigAttr=_WwpLeosSystemConfigAttr_ObjectIdentity((1,3,6,1,4,1,6141,2,60,12,1,1))
_WwpLeosSystemConfigDefaultGateway_Type=IpAddress
_WwpLeosSystemConfigDefaultGateway_Object=MibScalar
wwpLeosSystemConfigDefaultGateway=_WwpLeosSystemConfigDefaultGateway_Object((1,3,6,1,4,1,6141,2,60,12,1,1,1),_WwpLeosSystemConfigDefaultGateway_Type())
wwpLeosSystemConfigDefaultGateway.setMaxAccess(_E)
if mibBuilder.loadTexts:wwpLeosSystemConfigDefaultGateway.setStatus(_A)
_WwpLeosSystemConfigBootCmdFile_Type=FileName
_WwpLeosSystemConfigBootCmdFile_Object=MibScalar
wwpLeosSystemConfigBootCmdFile=_WwpLeosSystemConfigBootCmdFile_Object((1,3,6,1,4,1,6141,2,60,12,1,1,2),_WwpLeosSystemConfigBootCmdFile_Type())
wwpLeosSystemConfigBootCmdFile.setMaxAccess(_E)
if mibBuilder.loadTexts:wwpLeosSystemConfigBootCmdFile.setStatus(_A)
_WwpLeosSystemConfigBootCfgFile_Type=FileName
_WwpLeosSystemConfigBootCfgFile_Object=MibScalar
wwpLeosSystemConfigBootCfgFile=_WwpLeosSystemConfigBootCfgFile_Object((1,3,6,1,4,1,6141,2,60,12,1,1,3),_WwpLeosSystemConfigBootCfgFile_Type())
wwpLeosSystemConfigBootCfgFile.setMaxAccess(_E)
if mibBuilder.loadTexts:wwpLeosSystemConfigBootCfgFile.setStatus(_A)
_WwpLeosSystemClockDateTime_Type=DateAndTime
_WwpLeosSystemClockDateTime_Object=MibScalar
wwpLeosSystemClockDateTime=_WwpLeosSystemClockDateTime_Object((1,3,6,1,4,1,6141,2,60,12,1,1,4),_WwpLeosSystemClockDateTime_Type())
wwpLeosSystemClockDateTime.setMaxAccess(_E)
if mibBuilder.loadTexts:wwpLeosSystemClockDateTime.setStatus(_A)
_WwpLeosSystemConfigSavePermFile_Type=FileName
_WwpLeosSystemConfigSavePermFile_Object=MibScalar
wwpLeosSystemConfigSavePermFile=_WwpLeosSystemConfigSavePermFile_Object((1,3,6,1,4,1,6141,2,60,12,1,1,5),_WwpLeosSystemConfigSavePermFile_Type())
wwpLeosSystemConfigSavePermFile.setMaxAccess(_E)
if mibBuilder.loadTexts:wwpLeosSystemConfigSavePermFile.setStatus(_A)
_WwpLeosSystemConfigLastFileNameReset_Type=TruthValue
_WwpLeosSystemConfigLastFileNameReset_Object=MibScalar
wwpLeosSystemConfigLastFileNameReset=_WwpLeosSystemConfigLastFileNameReset_Object((1,3,6,1,4,1,6141,2,60,12,1,1,6),_WwpLeosSystemConfigLastFileNameReset_Type())
wwpLeosSystemConfigLastFileNameReset.setMaxAccess(_E)
if mibBuilder.loadTexts:wwpLeosSystemConfigLastFileNameReset.setStatus(_A)
class _WwpLeosSystemServiceMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*((_N,0),('mpls',1),('pbt',2),('aoam',3)))
_WwpLeosSystemServiceMode_Type.__name__=_B
_WwpLeosSystemServiceMode_Object=MibScalar
wwpLeosSystemServiceMode=_WwpLeosSystemServiceMode_Object((1,3,6,1,4,1,6141,2,60,12,1,1,7),_WwpLeosSystemServiceMode_Type())
wwpLeosSystemServiceMode.setMaxAccess(_E)
if mibBuilder.loadTexts:wwpLeosSystemServiceMode.setStatus(_A)
_WwpLeosSystemConfigBackupGateway_Type=IpAddress
_WwpLeosSystemConfigBackupGateway_Object=MibScalar
wwpLeosSystemConfigBackupGateway=_WwpLeosSystemConfigBackupGateway_Object((1,3,6,1,4,1,6141,2,60,12,1,1,8),_WwpLeosSystemConfigBackupGateway_Type())
wwpLeosSystemConfigBackupGateway.setMaxAccess(_E)
if mibBuilder.loadTexts:wwpLeosSystemConfigBackupGateway.setStatus(_A)
_WwpLeosSystemConfigCustomerCfgFile_Type=FileName
_WwpLeosSystemConfigCustomerCfgFile_Object=MibScalar
wwpLeosSystemConfigCustomerCfgFile=_WwpLeosSystemConfigCustomerCfgFile_Object((1,3,6,1,4,1,6141,2,60,12,1,1,9),_WwpLeosSystemConfigCustomerCfgFile_Type())
wwpLeosSystemConfigCustomerCfgFile.setMaxAccess(_E)
if mibBuilder.loadTexts:wwpLeosSystemConfigCustomerCfgFile.setStatus(_A)
_WwpLeosSystemConfigDefaultGatewayTable_Object=MibTable
wwpLeosSystemConfigDefaultGatewayTable=_WwpLeosSystemConfigDefaultGatewayTable_Object((1,3,6,1,4,1,6141,2,60,12,1,1,10))
if mibBuilder.loadTexts:wwpLeosSystemConfigDefaultGatewayTable.setStatus(_A)
_WwpLeosSystemConfigDefaultGatewayEntry_Object=MibTableRow
wwpLeosSystemConfigDefaultGatewayEntry=_WwpLeosSystemConfigDefaultGatewayEntry_Object((1,3,6,1,4,1,6141,2,60,12,1,1,10,1))
wwpLeosSystemConfigDefaultGatewayEntry.setIndexNames((0,_D,_T))
if mibBuilder.loadTexts:wwpLeosSystemConfigDefaultGatewayEntry.setStatus(_A)
class _WwpLeosSystemConfigDefaultGatewayIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,16))
_WwpLeosSystemConfigDefaultGatewayIndex_Type.__name__=_B
_WwpLeosSystemConfigDefaultGatewayIndex_Object=MibTableColumn
wwpLeosSystemConfigDefaultGatewayIndex=_WwpLeosSystemConfigDefaultGatewayIndex_Object((1,3,6,1,4,1,6141,2,60,12,1,1,10,1,1),_WwpLeosSystemConfigDefaultGatewayIndex_Type())
wwpLeosSystemConfigDefaultGatewayIndex.setMaxAccess(_K)
if mibBuilder.loadTexts:wwpLeosSystemConfigDefaultGatewayIndex.setStatus(_A)
_WwpLeosSystemConfigDefaultGatewayInetAddrType_Type=InetAddressType
_WwpLeosSystemConfigDefaultGatewayInetAddrType_Object=MibTableColumn
wwpLeosSystemConfigDefaultGatewayInetAddrType=_WwpLeosSystemConfigDefaultGatewayInetAddrType_Object((1,3,6,1,4,1,6141,2,60,12,1,1,10,1,2),_WwpLeosSystemConfigDefaultGatewayInetAddrType_Type())
wwpLeosSystemConfigDefaultGatewayInetAddrType.setMaxAccess(_F)
if mibBuilder.loadTexts:wwpLeosSystemConfigDefaultGatewayInetAddrType.setStatus(_A)
_WwpLeosSystemConfigDefaultGatewayInetAddress_Type=InetAddress
_WwpLeosSystemConfigDefaultGatewayInetAddress_Object=MibTableColumn
wwpLeosSystemConfigDefaultGatewayInetAddress=_WwpLeosSystemConfigDefaultGatewayInetAddress_Object((1,3,6,1,4,1,6141,2,60,12,1,1,10,1,3),_WwpLeosSystemConfigDefaultGatewayInetAddress_Type())
wwpLeosSystemConfigDefaultGatewayInetAddress.setMaxAccess(_F)
if mibBuilder.loadTexts:wwpLeosSystemConfigDefaultGatewayInetAddress.setStatus(_A)
_WwpLeosSystemConfigDefaultGatewayInterfaceName_Type=DisplayString
_WwpLeosSystemConfigDefaultGatewayInterfaceName_Object=MibTableColumn
wwpLeosSystemConfigDefaultGatewayInterfaceName=_WwpLeosSystemConfigDefaultGatewayInterfaceName_Object((1,3,6,1,4,1,6141,2,60,12,1,1,10,1,4),_WwpLeosSystemConfigDefaultGatewayInterfaceName_Type())
wwpLeosSystemConfigDefaultGatewayInterfaceName.setMaxAccess(_F)
if mibBuilder.loadTexts:wwpLeosSystemConfigDefaultGatewayInterfaceName.setStatus(_A)
_WwpLeosSystemConfigDefaultGatewayMetric_Type=Integer32
_WwpLeosSystemConfigDefaultGatewayMetric_Object=MibTableColumn
wwpLeosSystemConfigDefaultGatewayMetric=_WwpLeosSystemConfigDefaultGatewayMetric_Object((1,3,6,1,4,1,6141,2,60,12,1,1,10,1,5),_WwpLeosSystemConfigDefaultGatewayMetric_Type())
wwpLeosSystemConfigDefaultGatewayMetric.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosSystemConfigDefaultGatewayMetric.setStatus(_A)
_WwpLeosSystemConfigDefaultGatewayStatus_Type=RowStatus
_WwpLeosSystemConfigDefaultGatewayStatus_Object=MibTableColumn
wwpLeosSystemConfigDefaultGatewayStatus=_WwpLeosSystemConfigDefaultGatewayStatus_Object((1,3,6,1,4,1,6141,2,60,12,1,1,10,1,6),_WwpLeosSystemConfigDefaultGatewayStatus_Type())
wwpLeosSystemConfigDefaultGatewayStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:wwpLeosSystemConfigDefaultGatewayStatus.setStatus(_A)
_WwpLeosSystemConfigBackupGatewayTable_Object=MibTable
wwpLeosSystemConfigBackupGatewayTable=_WwpLeosSystemConfigBackupGatewayTable_Object((1,3,6,1,4,1,6141,2,60,12,1,1,11))
if mibBuilder.loadTexts:wwpLeosSystemConfigBackupGatewayTable.setStatus(_A)
_WwpLeosSystemConfigBackupGatewayEntry_Object=MibTableRow
wwpLeosSystemConfigBackupGatewayEntry=_WwpLeosSystemConfigBackupGatewayEntry_Object((1,3,6,1,4,1,6141,2,60,12,1,1,11,1))
wwpLeosSystemConfigBackupGatewayEntry.setIndexNames((0,_D,_U))
if mibBuilder.loadTexts:wwpLeosSystemConfigBackupGatewayEntry.setStatus(_A)
class _WwpLeosSystemConfigBackupGatewayIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,16))
_WwpLeosSystemConfigBackupGatewayIndex_Type.__name__=_B
_WwpLeosSystemConfigBackupGatewayIndex_Object=MibTableColumn
wwpLeosSystemConfigBackupGatewayIndex=_WwpLeosSystemConfigBackupGatewayIndex_Object((1,3,6,1,4,1,6141,2,60,12,1,1,11,1,1),_WwpLeosSystemConfigBackupGatewayIndex_Type())
wwpLeosSystemConfigBackupGatewayIndex.setMaxAccess(_K)
if mibBuilder.loadTexts:wwpLeosSystemConfigBackupGatewayIndex.setStatus(_A)
_WwpLeosSystemConfigBackupGatewayInetAddrType_Type=InetAddressType
_WwpLeosSystemConfigBackupGatewayInetAddrType_Object=MibTableColumn
wwpLeosSystemConfigBackupGatewayInetAddrType=_WwpLeosSystemConfigBackupGatewayInetAddrType_Object((1,3,6,1,4,1,6141,2,60,12,1,1,11,1,2),_WwpLeosSystemConfigBackupGatewayInetAddrType_Type())
wwpLeosSystemConfigBackupGatewayInetAddrType.setMaxAccess(_F)
if mibBuilder.loadTexts:wwpLeosSystemConfigBackupGatewayInetAddrType.setStatus(_A)
_WwpLeosSystemConfigBackupGatewayInetAddress_Type=InetAddress
_WwpLeosSystemConfigBackupGatewayInetAddress_Object=MibTableColumn
wwpLeosSystemConfigBackupGatewayInetAddress=_WwpLeosSystemConfigBackupGatewayInetAddress_Object((1,3,6,1,4,1,6141,2,60,12,1,1,11,1,3),_WwpLeosSystemConfigBackupGatewayInetAddress_Type())
wwpLeosSystemConfigBackupGatewayInetAddress.setMaxAccess(_F)
if mibBuilder.loadTexts:wwpLeosSystemConfigBackupGatewayInetAddress.setStatus(_A)
_WwpLeosSystemConfigBackupGatewayInterfaceName_Type=DisplayString
_WwpLeosSystemConfigBackupGatewayInterfaceName_Object=MibTableColumn
wwpLeosSystemConfigBackupGatewayInterfaceName=_WwpLeosSystemConfigBackupGatewayInterfaceName_Object((1,3,6,1,4,1,6141,2,60,12,1,1,11,1,4),_WwpLeosSystemConfigBackupGatewayInterfaceName_Type())
wwpLeosSystemConfigBackupGatewayInterfaceName.setMaxAccess(_F)
if mibBuilder.loadTexts:wwpLeosSystemConfigBackupGatewayInterfaceName.setStatus(_A)
_WwpLeosSystemConfigBackupGatewayMetric_Type=Integer32
_WwpLeosSystemConfigBackupGatewayMetric_Object=MibTableColumn
wwpLeosSystemConfigBackupGatewayMetric=_WwpLeosSystemConfigBackupGatewayMetric_Object((1,3,6,1,4,1,6141,2,60,12,1,1,11,1,5),_WwpLeosSystemConfigBackupGatewayMetric_Type())
wwpLeosSystemConfigBackupGatewayMetric.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosSystemConfigBackupGatewayMetric.setStatus(_A)
_WwpLeosSystemConfigBackupGatewayStatus_Type=RowStatus
_WwpLeosSystemConfigBackupGatewayStatus_Object=MibTableColumn
wwpLeosSystemConfigBackupGatewayStatus=_WwpLeosSystemConfigBackupGatewayStatus_Object((1,3,6,1,4,1,6141,2,60,12,1,1,11,1,6),_WwpLeosSystemConfigBackupGatewayStatus_Type())
wwpLeosSystemConfigBackupGatewayStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:wwpLeosSystemConfigBackupGatewayStatus.setStatus(_A)
_WwpLeosSystemConfig_ObjectIdentity=ObjectIdentity
wwpLeosSystemConfig=_WwpLeosSystemConfig_ObjectIdentity((1,3,6,1,4,1,6141,2,60,12,1,2))
_WwpLeosSystemConfigSaveFileName_Type=FileName
_WwpLeosSystemConfigSaveFileName_Object=MibScalar
wwpLeosSystemConfigSaveFileName=_WwpLeosSystemConfigSaveFileName_Object((1,3,6,1,4,1,6141,2,60,12,1,2,1),_WwpLeosSystemConfigSaveFileName_Type())
wwpLeosSystemConfigSaveFileName.setMaxAccess(_E)
if mibBuilder.loadTexts:wwpLeosSystemConfigSaveFileName.setStatus(_A)
class _WwpLeosSystemConfigControl_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_N,0),('save',1),('mfgDefaultCfg',2)))
_WwpLeosSystemConfigControl_Type.__name__=_B
_WwpLeosSystemConfigControl_Object=MibScalar
wwpLeosSystemConfigControl=_WwpLeosSystemConfigControl_Object((1,3,6,1,4,1,6141,2,60,12,1,2,2),_WwpLeosSystemConfigControl_Type())
wwpLeosSystemConfigControl.setMaxAccess(_E)
if mibBuilder.loadTexts:wwpLeosSystemConfigControl.setStatus(_A)
_WwpLeosSystemConfigFilepath_Type=FileName
_WwpLeosSystemConfigFilepath_Object=MibScalar
wwpLeosSystemConfigFilepath=_WwpLeosSystemConfigFilepath_Object((1,3,6,1,4,1,6141,2,60,12,1,2,3),_WwpLeosSystemConfigFilepath_Type())
wwpLeosSystemConfigFilepath.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosSystemConfigFilepath.setStatus(_A)
_WwpLeosSystemConfigFileTable_Object=MibTable
wwpLeosSystemConfigFileTable=_WwpLeosSystemConfigFileTable_Object((1,3,6,1,4,1,6141,2,60,12,1,2,4))
if mibBuilder.loadTexts:wwpLeosSystemConfigFileTable.setStatus(_A)
_WwpLeosSystemConfigFileEntry_Object=MibTableRow
wwpLeosSystemConfigFileEntry=_WwpLeosSystemConfigFileEntry_Object((1,3,6,1,4,1,6141,2,60,12,1,2,4,1))
wwpLeosSystemConfigFileEntry.setIndexNames((0,_D,_O))
if mibBuilder.loadTexts:wwpLeosSystemConfigFileEntry.setStatus(_A)
class _WwpLeosSystemConfigFileIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_WwpLeosSystemConfigFileIndex_Type.__name__=_B
_WwpLeosSystemConfigFileIndex_Object=MibTableColumn
wwpLeosSystemConfigFileIndex=_WwpLeosSystemConfigFileIndex_Object((1,3,6,1,4,1,6141,2,60,12,1,2,4,1,1),_WwpLeosSystemConfigFileIndex_Type())
wwpLeosSystemConfigFileIndex.setMaxAccess(_K)
if mibBuilder.loadTexts:wwpLeosSystemConfigFileIndex.setStatus(_A)
_WwpLeosSystemConfigFileName_Type=FileName
_WwpLeosSystemConfigFileName_Object=MibTableColumn
wwpLeosSystemConfigFileName=_WwpLeosSystemConfigFileName_Object((1,3,6,1,4,1,6141,2,60,12,1,2,4,1,2),_WwpLeosSystemConfigFileName_Type())
wwpLeosSystemConfigFileName.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosSystemConfigFileName.setStatus(_A)
class _WwpLeosSystemConfigActivateFile_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('loadCfg',1),('resetToCfg',2),(_N,3)))
_WwpLeosSystemConfigActivateFile_Type.__name__=_B
_WwpLeosSystemConfigActivateFile_Object=MibTableColumn
wwpLeosSystemConfigActivateFile=_WwpLeosSystemConfigActivateFile_Object((1,3,6,1,4,1,6141,2,60,12,1,2,4,1,3),_WwpLeosSystemConfigActivateFile_Type())
wwpLeosSystemConfigActivateFile.setMaxAccess(_E)
if mibBuilder.loadTexts:wwpLeosSystemConfigActivateFile.setStatus(_A)
_WwpLeosSystemTelnet_ObjectIdentity=ObjectIdentity
wwpLeosSystemTelnet=_WwpLeosSystemTelnet_ObjectIdentity((1,3,6,1,4,1,6141,2,60,12,1,3))
class _WwpLeosTelnetMaxBaseUserSessions_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,10))
_WwpLeosTelnetMaxBaseUserSessions_Type.__name__=_B
_WwpLeosTelnetMaxBaseUserSessions_Object=MibScalar
wwpLeosTelnetMaxBaseUserSessions=_WwpLeosTelnetMaxBaseUserSessions_Object((1,3,6,1,4,1,6141,2,60,12,1,3,1),_WwpLeosTelnetMaxBaseUserSessions_Type())
wwpLeosTelnetMaxBaseUserSessions.setMaxAccess(_E)
if mibBuilder.loadTexts:wwpLeosTelnetMaxBaseUserSessions.setStatus(_A)
class _WwpLeosTelnetMaxSuperUserSessions_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,10))
_WwpLeosTelnetMaxSuperUserSessions_Type.__name__=_B
_WwpLeosTelnetMaxSuperUserSessions_Object=MibScalar
wwpLeosTelnetMaxSuperUserSessions=_WwpLeosTelnetMaxSuperUserSessions_Object((1,3,6,1,4,1,6141,2,60,12,1,3,2),_WwpLeosTelnetMaxSuperUserSessions_Type())
wwpLeosTelnetMaxSuperUserSessions.setMaxAccess(_E)
if mibBuilder.loadTexts:wwpLeosTelnetMaxSuperUserSessions.setStatus(_A)
class _WwpLeosTelnetMaxAdminUserSessions_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,10))
_WwpLeosTelnetMaxAdminUserSessions_Type.__name__=_B
_WwpLeosTelnetMaxAdminUserSessions_Object=MibScalar
wwpLeosTelnetMaxAdminUserSessions=_WwpLeosTelnetMaxAdminUserSessions_Object((1,3,6,1,4,1,6141,2,60,12,1,3,3),_WwpLeosTelnetMaxAdminUserSessions_Type())
wwpLeosTelnetMaxAdminUserSessions.setMaxAccess(_E)
if mibBuilder.loadTexts:wwpLeosTelnetMaxAdminUserSessions.setStatus(_A)
_WwpLeosSystemCpuLoadQuery_ObjectIdentity=ObjectIdentity
wwpLeosSystemCpuLoadQuery=_WwpLeosSystemCpuLoadQuery_ObjectIdentity((1,3,6,1,4,1,6141,2,60,12,1,7))
class _WwpLeosSystemCpuLoad1Min_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_WwpLeosSystemCpuLoad1Min_Type.__name__=_B
_WwpLeosSystemCpuLoad1Min_Object=MibScalar
wwpLeosSystemCpuLoad1Min=_WwpLeosSystemCpuLoad1Min_Object((1,3,6,1,4,1,6141,2,60,12,1,7,1),_WwpLeosSystemCpuLoad1Min_Type())
wwpLeosSystemCpuLoad1Min.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosSystemCpuLoad1Min.setStatus(_A)
class _WwpLeosSystemCpuLoad10Min_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_WwpLeosSystemCpuLoad10Min_Type.__name__=_B
_WwpLeosSystemCpuLoad10Min_Object=MibScalar
wwpLeosSystemCpuLoad10Min=_WwpLeosSystemCpuLoad10Min_Object((1,3,6,1,4,1,6141,2,60,12,1,7,2),_WwpLeosSystemCpuLoad10Min_Type())
wwpLeosSystemCpuLoad10Min.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosSystemCpuLoad10Min.setStatus(_A)
class _WwpLeosSystemCpuLoad15Min_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_WwpLeosSystemCpuLoad15Min_Type.__name__=_B
_WwpLeosSystemCpuLoad15Min_Object=MibScalar
wwpLeosSystemCpuLoad15Min=_WwpLeosSystemCpuLoad15Min_Object((1,3,6,1,4,1,6141,2,60,12,1,7,3),_WwpLeosSystemCpuLoad15Min_Type())
wwpLeosSystemCpuLoad15Min.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosSystemCpuLoad15Min.setStatus(_A)
class _WwpLeosSystemCpuLoad5Min_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_WwpLeosSystemCpuLoad5Min_Type.__name__=_B
_WwpLeosSystemCpuLoad5Min_Object=MibScalar
wwpLeosSystemCpuLoad5Min=_WwpLeosSystemCpuLoad5Min_Object((1,3,6,1,4,1,6141,2,60,12,1,7,4),_WwpLeosSystemCpuLoad5Min_Type())
wwpLeosSystemCpuLoad5Min.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosSystemCpuLoad5Min.setStatus(_A)
class _WwpLeosSystemCpuLoad1MinMinimum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_WwpLeosSystemCpuLoad1MinMinimum_Type.__name__=_B
_WwpLeosSystemCpuLoad1MinMinimum_Object=MibScalar
wwpLeosSystemCpuLoad1MinMinimum=_WwpLeosSystemCpuLoad1MinMinimum_Object((1,3,6,1,4,1,6141,2,60,12,1,7,5),_WwpLeosSystemCpuLoad1MinMinimum_Type())
wwpLeosSystemCpuLoad1MinMinimum.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosSystemCpuLoad1MinMinimum.setStatus(_A)
class _WwpLeosSystemCpuLoad1MinMaximum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_WwpLeosSystemCpuLoad1MinMaximum_Type.__name__=_B
_WwpLeosSystemCpuLoad1MinMaximum_Object=MibScalar
wwpLeosSystemCpuLoad1MinMaximum=_WwpLeosSystemCpuLoad1MinMaximum_Object((1,3,6,1,4,1,6141,2,60,12,1,7,6),_WwpLeosSystemCpuLoad1MinMaximum_Type())
wwpLeosSystemCpuLoad1MinMaximum.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosSystemCpuLoad1MinMaximum.setStatus(_A)
class _WwpLeosSystemCpuLoad1MinState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_G,1),(_H,2),(_I,3),(_J,4)))
_WwpLeosSystemCpuLoad1MinState_Type.__name__=_B
_WwpLeosSystemCpuLoad1MinState_Object=MibScalar
wwpLeosSystemCpuLoad1MinState=_WwpLeosSystemCpuLoad1MinState_Object((1,3,6,1,4,1,6141,2,60,12,1,7,7),_WwpLeosSystemCpuLoad1MinState_Type())
wwpLeosSystemCpuLoad1MinState.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosSystemCpuLoad1MinState.setStatus(_A)
class _WwpLeosSystemCpuLoad15MinMinimum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_WwpLeosSystemCpuLoad15MinMinimum_Type.__name__=_B
_WwpLeosSystemCpuLoad15MinMinimum_Object=MibScalar
wwpLeosSystemCpuLoad15MinMinimum=_WwpLeosSystemCpuLoad15MinMinimum_Object((1,3,6,1,4,1,6141,2,60,12,1,7,8),_WwpLeosSystemCpuLoad15MinMinimum_Type())
wwpLeosSystemCpuLoad15MinMinimum.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosSystemCpuLoad15MinMinimum.setStatus(_A)
class _WwpLeosSystemCpuLoad15MinMaximum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_WwpLeosSystemCpuLoad15MinMaximum_Type.__name__=_B
_WwpLeosSystemCpuLoad15MinMaximum_Object=MibScalar
wwpLeosSystemCpuLoad15MinMaximum=_WwpLeosSystemCpuLoad15MinMaximum_Object((1,3,6,1,4,1,6141,2,60,12,1,7,9),_WwpLeosSystemCpuLoad15MinMaximum_Type())
wwpLeosSystemCpuLoad15MinMaximum.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosSystemCpuLoad15MinMaximum.setStatus(_A)
class _WwpLeosSystemCpuLoad15MinState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_G,1),(_H,2),(_I,3),(_J,4)))
_WwpLeosSystemCpuLoad15MinState_Type.__name__=_B
_WwpLeosSystemCpuLoad15MinState_Object=MibScalar
wwpLeosSystemCpuLoad15MinState=_WwpLeosSystemCpuLoad15MinState_Object((1,3,6,1,4,1,6141,2,60,12,1,7,10),_WwpLeosSystemCpuLoad15MinState_Type())
wwpLeosSystemCpuLoad15MinState.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosSystemCpuLoad15MinState.setStatus(_A)
class _WwpLeosSystemCpuLoad5MinMinimum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_WwpLeosSystemCpuLoad5MinMinimum_Type.__name__=_B
_WwpLeosSystemCpuLoad5MinMinimum_Object=MibScalar
wwpLeosSystemCpuLoad5MinMinimum=_WwpLeosSystemCpuLoad5MinMinimum_Object((1,3,6,1,4,1,6141,2,60,12,1,7,11),_WwpLeosSystemCpuLoad5MinMinimum_Type())
wwpLeosSystemCpuLoad5MinMinimum.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosSystemCpuLoad5MinMinimum.setStatus(_A)
class _WwpLeosSystemCpuLoad5MinMaximum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_WwpLeosSystemCpuLoad5MinMaximum_Type.__name__=_B
_WwpLeosSystemCpuLoad5MinMaximum_Object=MibScalar
wwpLeosSystemCpuLoad5MinMaximum=_WwpLeosSystemCpuLoad5MinMaximum_Object((1,3,6,1,4,1,6141,2,60,12,1,7,12),_WwpLeosSystemCpuLoad5MinMaximum_Type())
wwpLeosSystemCpuLoad5MinMaximum.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosSystemCpuLoad5MinMaximum.setStatus(_A)
class _WwpLeosSystemCpuLoad5MinState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_G,1),(_H,2),(_I,3),(_J,4)))
_WwpLeosSystemCpuLoad5MinState_Type.__name__=_B
_WwpLeosSystemCpuLoad5MinState_Object=MibScalar
wwpLeosSystemCpuLoad5MinState=_WwpLeosSystemCpuLoad5MinState_Object((1,3,6,1,4,1,6141,2,60,12,1,7,13),_WwpLeosSystemCpuLoad5MinState_Type())
wwpLeosSystemCpuLoad5MinState.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosSystemCpuLoad5MinState.setStatus(_A)
_WwpLeosSystemConfigNotif_ObjectIdentity=ObjectIdentity
wwpLeosSystemConfigNotif=_WwpLeosSystemConfigNotif_ObjectIdentity((1,3,6,1,4,1,6141,2,60,12,1,8))
_WwpLeosSystemConfigNotifTable_Object=MibTable
wwpLeosSystemConfigNotifTable=_WwpLeosSystemConfigNotifTable_Object((1,3,6,1,4,1,6141,2,60,12,1,8,1))
if mibBuilder.loadTexts:wwpLeosSystemConfigNotifTable.setStatus(_A)
_WwpLeosSystemConfigNotifEntry_Object=MibTableRow
wwpLeosSystemConfigNotifEntry=_WwpLeosSystemConfigNotifEntry_Object((1,3,6,1,4,1,6141,2,60,12,1,8,1,1))
wwpLeosSystemConfigNotifEntry.setIndexNames((0,_D,_O))
if mibBuilder.loadTexts:wwpLeosSystemConfigNotifEntry.setStatus(_A)
class _WwpLeosSystemConfigErrLineNum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,64))
_WwpLeosSystemConfigErrLineNum_Type.__name__=_B
_WwpLeosSystemConfigErrLineNum_Object=MibTableColumn
wwpLeosSystemConfigErrLineNum=_WwpLeosSystemConfigErrLineNum_Object((1,3,6,1,4,1,6141,2,60,12,1,8,1,1,1),_WwpLeosSystemConfigErrLineNum_Type())
wwpLeosSystemConfigErrLineNum.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosSystemConfigErrLineNum.setStatus(_A)
_WwpLeosSystemConfigErrStr_Type=DisplayString
_WwpLeosSystemConfigErrStr_Object=MibTableColumn
wwpLeosSystemConfigErrStr=_WwpLeosSystemConfigErrStr_Object((1,3,6,1,4,1,6141,2,60,12,1,8,1,1,2),_WwpLeosSystemConfigErrStr_Type())
wwpLeosSystemConfigErrStr.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosSystemConfigErrStr.setStatus(_A)
class _WwpLeosSystemConfigErrLinesTotal_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,64))
_WwpLeosSystemConfigErrLinesTotal_Type.__name__=_B
_WwpLeosSystemConfigErrLinesTotal_Object=MibTableColumn
wwpLeosSystemConfigErrLinesTotal=_WwpLeosSystemConfigErrLinesTotal_Object((1,3,6,1,4,1,6141,2,60,12,1,8,1,1,3),_WwpLeosSystemConfigErrLinesTotal_Type())
wwpLeosSystemConfigErrLinesTotal.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosSystemConfigErrLinesTotal.setStatus(_A)
_WwpLeosSystemMemoryUsageQuery_ObjectIdentity=ObjectIdentity
wwpLeosSystemMemoryUsageQuery=_WwpLeosSystemMemoryUsageQuery_ObjectIdentity((1,3,6,1,4,1,6141,2,60,12,1,9))
_WwpLeosSystemMemoryUsageTable_Object=MibTable
wwpLeosSystemMemoryUsageTable=_WwpLeosSystemMemoryUsageTable_Object((1,3,6,1,4,1,6141,2,60,12,1,9,1))
if mibBuilder.loadTexts:wwpLeosSystemMemoryUsageTable.setStatus(_A)
_WwpLeosSystemMemoryUsageEntry_Object=MibTableRow
wwpLeosSystemMemoryUsageEntry=_WwpLeosSystemMemoryUsageEntry_Object((1,3,6,1,4,1,6141,2,60,12,1,9,1,1))
wwpLeosSystemMemoryUsageEntry.setIndexNames((0,_D,_V))
if mibBuilder.loadTexts:wwpLeosSystemMemoryUsageEntry.setStatus(_A)
class _WwpLeosSystemMemoryUsagePoolIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('ose-pool-1',1),('global-heap',2),('malloc-heap',3)))
_WwpLeosSystemMemoryUsagePoolIndex_Type.__name__=_B
_WwpLeosSystemMemoryUsagePoolIndex_Object=MibTableColumn
wwpLeosSystemMemoryUsagePoolIndex=_WwpLeosSystemMemoryUsagePoolIndex_Object((1,3,6,1,4,1,6141,2,60,12,1,9,1,1,1),_WwpLeosSystemMemoryUsagePoolIndex_Type())
wwpLeosSystemMemoryUsagePoolIndex.setMaxAccess(_K)
if mibBuilder.loadTexts:wwpLeosSystemMemoryUsagePoolIndex.setStatus(_A)
_WwpLeosSystemMemoryUsageMemoryTotal_Type=Unsigned32
_WwpLeosSystemMemoryUsageMemoryTotal_Object=MibTableColumn
wwpLeosSystemMemoryUsageMemoryTotal=_WwpLeosSystemMemoryUsageMemoryTotal_Object((1,3,6,1,4,1,6141,2,60,12,1,9,1,1,2),_WwpLeosSystemMemoryUsageMemoryTotal_Type())
wwpLeosSystemMemoryUsageMemoryTotal.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosSystemMemoryUsageMemoryTotal.setStatus(_A)
if mibBuilder.loadTexts:wwpLeosSystemMemoryUsageMemoryTotal.setUnits(_L)
_WwpLeosSystemMemoryUsageMemoryLWM_Type=Unsigned32
_WwpLeosSystemMemoryUsageMemoryLWM_Object=MibTableColumn
wwpLeosSystemMemoryUsageMemoryLWM=_WwpLeosSystemMemoryUsageMemoryLWM_Object((1,3,6,1,4,1,6141,2,60,12,1,9,1,1,3),_WwpLeosSystemMemoryUsageMemoryLWM_Type())
wwpLeosSystemMemoryUsageMemoryLWM.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosSystemMemoryUsageMemoryLWM.setStatus(_A)
_WwpLeosSystemMemoryUsageMemoryFree_Type=Unsigned32
_WwpLeosSystemMemoryUsageMemoryFree_Object=MibTableColumn
wwpLeosSystemMemoryUsageMemoryFree=_WwpLeosSystemMemoryUsageMemoryFree_Object((1,3,6,1,4,1,6141,2,60,12,1,9,1,1,4),_WwpLeosSystemMemoryUsageMemoryFree_Type())
wwpLeosSystemMemoryUsageMemoryFree.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosSystemMemoryUsageMemoryFree.setStatus(_A)
if mibBuilder.loadTexts:wwpLeosSystemMemoryUsageMemoryFree.setUnits(_L)
class _WwpLeosSystemMemoryUsageStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_G,1),('lowMemory',2),('notSupported',3)))
_WwpLeosSystemMemoryUsageStatus_Type.__name__=_B
_WwpLeosSystemMemoryUsageStatus_Object=MibTableColumn
wwpLeosSystemMemoryUsageStatus=_WwpLeosSystemMemoryUsageStatus_Object((1,3,6,1,4,1,6141,2,60,12,1,9,1,1,5),_WwpLeosSystemMemoryUsageStatus_Type())
wwpLeosSystemMemoryUsageStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosSystemMemoryUsageStatus.setStatus(_A)
_WwpLeosSystemMemoryUsageMemoryUsed_Type=Unsigned32
_WwpLeosSystemMemoryUsageMemoryUsed_Object=MibTableColumn
wwpLeosSystemMemoryUsageMemoryUsed=_WwpLeosSystemMemoryUsageMemoryUsed_Object((1,3,6,1,4,1,6141,2,60,12,1,9,1,1,6),_WwpLeosSystemMemoryUsageMemoryUsed_Type())
wwpLeosSystemMemoryUsageMemoryUsed.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosSystemMemoryUsageMemoryUsed.setStatus(_A)
if mibBuilder.loadTexts:wwpLeosSystemMemoryUsageMemoryUsed.setUnits(_L)
_WwpLeosSystemMemoryUsageMemoryAvailable_Type=Unsigned32
_WwpLeosSystemMemoryUsageMemoryAvailable_Object=MibTableColumn
wwpLeosSystemMemoryUsageMemoryAvailable=_WwpLeosSystemMemoryUsageMemoryAvailable_Object((1,3,6,1,4,1,6141,2,60,12,1,9,1,1,7),_WwpLeosSystemMemoryUsageMemoryAvailable_Type())
wwpLeosSystemMemoryUsageMemoryAvailable.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosSystemMemoryUsageMemoryAvailable.setStatus(_A)
if mibBuilder.loadTexts:wwpLeosSystemMemoryUsageMemoryAvailable.setUnits(_L)
_WwpLeosSystemXFtp_ObjectIdentity=ObjectIdentity
wwpLeosSystemXFtp=_WwpLeosSystemXFtp_ObjectIdentity((1,3,6,1,4,1,6141,2,60,12,1,10))
class _WwpLeosSystemXFtpMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('tftp',1),('ftp',2),('sftp',3)))
_WwpLeosSystemXFtpMode_Type.__name__=_B
_WwpLeosSystemXFtpMode_Object=MibScalar
wwpLeosSystemXFtpMode=_WwpLeosSystemXFtpMode_Object((1,3,6,1,4,1,6141,2,60,12,1,10,1),_WwpLeosSystemXFtpMode_Type())
wwpLeosSystemXFtpMode.setMaxAccess(_E)
if mibBuilder.loadTexts:wwpLeosSystemXFtpMode.setStatus(_A)
_WwpLeosSystemXFtpServer_Type=DisplayString
_WwpLeosSystemXFtpServer_Object=MibScalar
wwpLeosSystemXFtpServer=_WwpLeosSystemXFtpServer_Object((1,3,6,1,4,1,6141,2,60,12,1,10,2),_WwpLeosSystemXFtpServer_Type())
wwpLeosSystemXFtpServer.setMaxAccess(_E)
if mibBuilder.loadTexts:wwpLeosSystemXFtpServer.setStatus(_A)
class _WwpLeosSystemXFtpUserName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_WwpLeosSystemXFtpUserName_Type.__name__=_M
_WwpLeosSystemXFtpUserName_Object=MibScalar
wwpLeosSystemXFtpUserName=_WwpLeosSystemXFtpUserName_Object((1,3,6,1,4,1,6141,2,60,12,1,10,3),_WwpLeosSystemXFtpUserName_Type())
wwpLeosSystemXFtpUserName.setMaxAccess(_E)
if mibBuilder.loadTexts:wwpLeosSystemXFtpUserName.setStatus(_A)
class _WwpLeosSystemXFtpPasswd_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,128))
_WwpLeosSystemXFtpPasswd_Type.__name__=_M
_WwpLeosSystemXFtpPasswd_Object=MibScalar
wwpLeosSystemXFtpPasswd=_WwpLeosSystemXFtpPasswd_Object((1,3,6,1,4,1,6141,2,60,12,1,10,4),_WwpLeosSystemXFtpPasswd_Type())
wwpLeosSystemXFtpPasswd.setMaxAccess(_E)
if mibBuilder.loadTexts:wwpLeosSystemXFtpPasswd.setStatus(_A)
class _WwpLeosSystemXFtpNumOfRetries_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,10))
_WwpLeosSystemXFtpNumOfRetries_Type.__name__=_B
_WwpLeosSystemXFtpNumOfRetries_Object=MibScalar
wwpLeosSystemXFtpNumOfRetries=_WwpLeosSystemXFtpNumOfRetries_Object((1,3,6,1,4,1,6141,2,60,12,1,10,5),_WwpLeosSystemXFtpNumOfRetries_Type())
wwpLeosSystemXFtpNumOfRetries.setMaxAccess(_E)
if mibBuilder.loadTexts:wwpLeosSystemXFtpNumOfRetries.setStatus(_A)
class _WwpLeosSystemXFtpRetryInterval_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,300))
_WwpLeosSystemXFtpRetryInterval_Type.__name__=_B
_WwpLeosSystemXFtpRetryInterval_Object=MibScalar
wwpLeosSystemXFtpRetryInterval=_WwpLeosSystemXFtpRetryInterval_Object((1,3,6,1,4,1,6141,2,60,12,1,10,6),_WwpLeosSystemXFtpRetryInterval_Type())
wwpLeosSystemXFtpRetryInterval.setMaxAccess(_E)
if mibBuilder.loadTexts:wwpLeosSystemXFtpRetryInterval.setStatus(_A)
class _WwpLeosSystemXFtpConnectionTimeout_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,100))
_WwpLeosSystemXFtpConnectionTimeout_Type.__name__=_B
_WwpLeosSystemXFtpConnectionTimeout_Object=MibScalar
wwpLeosSystemXFtpConnectionTimeout=_WwpLeosSystemXFtpConnectionTimeout_Object((1,3,6,1,4,1,6141,2,60,12,1,10,7),_WwpLeosSystemXFtpConnectionTimeout_Type())
wwpLeosSystemXFtpConnectionTimeout.setMaxAccess(_E)
if mibBuilder.loadTexts:wwpLeosSystemXFtpConnectionTimeout.setStatus(_A)
_WwpLeosSystemXFtpTFtpServerTable_Object=MibTable
wwpLeosSystemXFtpTFtpServerTable=_WwpLeosSystemXFtpTFtpServerTable_Object((1,3,6,1,4,1,6141,2,60,12,1,10,8))
if mibBuilder.loadTexts:wwpLeosSystemXFtpTFtpServerTable.setStatus(_A)
_WwpLeosSystemXFtpTFtpServerEntry_Object=MibTableRow
wwpLeosSystemXFtpTFtpServerEntry=_WwpLeosSystemXFtpTFtpServerEntry_Object((1,3,6,1,4,1,6141,2,60,12,1,10,8,1))
wwpLeosSystemXFtpTFtpServerEntry.setIndexNames((0,_D,_W))
if mibBuilder.loadTexts:wwpLeosSystemXFtpTFtpServerEntry.setStatus(_A)
class _WwpLeosSystemXFtpTFtpServerIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1))
_WwpLeosSystemXFtpTFtpServerIndex_Type.__name__=_B
_WwpLeosSystemXFtpTFtpServerIndex_Object=MibTableColumn
wwpLeosSystemXFtpTFtpServerIndex=_WwpLeosSystemXFtpTFtpServerIndex_Object((1,3,6,1,4,1,6141,2,60,12,1,10,8,1,1),_WwpLeosSystemXFtpTFtpServerIndex_Type())
wwpLeosSystemXFtpTFtpServerIndex.setMaxAccess(_K)
if mibBuilder.loadTexts:wwpLeosSystemXFtpTFtpServerIndex.setStatus(_A)
_WwpLeosSystemXFtpTFtpServerHostName_Type=DisplayString
_WwpLeosSystemXFtpTFtpServerHostName_Object=MibTableColumn
wwpLeosSystemXFtpTFtpServerHostName=_WwpLeosSystemXFtpTFtpServerHostName_Object((1,3,6,1,4,1,6141,2,60,12,1,10,8,1,2),_WwpLeosSystemXFtpTFtpServerHostName_Type())
wwpLeosSystemXFtpTFtpServerHostName.setMaxAccess(_F)
if mibBuilder.loadTexts:wwpLeosSystemXFtpTFtpServerHostName.setStatus(_A)
_WwpLeosSystemXFtpTFtpServerRowStatus_Type=RowStatus
_WwpLeosSystemXFtpTFtpServerRowStatus_Object=MibTableColumn
wwpLeosSystemXFtpTFtpServerRowStatus=_WwpLeosSystemXFtpTFtpServerRowStatus_Object((1,3,6,1,4,1,6141,2,60,12,1,10,8,1,6),_WwpLeosSystemXFtpTFtpServerRowStatus_Type())
wwpLeosSystemXFtpTFtpServerRowStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:wwpLeosSystemXFtpTFtpServerRowStatus.setStatus(_A)
_WwpLeosSystemXFtpFtpServerTable_Object=MibTable
wwpLeosSystemXFtpFtpServerTable=_WwpLeosSystemXFtpFtpServerTable_Object((1,3,6,1,4,1,6141,2,60,12,1,10,9))
if mibBuilder.loadTexts:wwpLeosSystemXFtpFtpServerTable.setStatus(_A)
_WwpLeosSystemXFtpFtpServerEntry_Object=MibTableRow
wwpLeosSystemXFtpFtpServerEntry=_WwpLeosSystemXFtpFtpServerEntry_Object((1,3,6,1,4,1,6141,2,60,12,1,10,9,1))
wwpLeosSystemXFtpFtpServerEntry.setIndexNames((0,_D,_X))
if mibBuilder.loadTexts:wwpLeosSystemXFtpFtpServerEntry.setStatus(_A)
class _WwpLeosSystemXFtpFtpServerIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1))
_WwpLeosSystemXFtpFtpServerIndex_Type.__name__=_B
_WwpLeosSystemXFtpFtpServerIndex_Object=MibTableColumn
wwpLeosSystemXFtpFtpServerIndex=_WwpLeosSystemXFtpFtpServerIndex_Object((1,3,6,1,4,1,6141,2,60,12,1,10,9,1,1),_WwpLeosSystemXFtpFtpServerIndex_Type())
wwpLeosSystemXFtpFtpServerIndex.setMaxAccess(_K)
if mibBuilder.loadTexts:wwpLeosSystemXFtpFtpServerIndex.setStatus(_A)
_WwpLeosSystemXFtpFtpServerHostName_Type=DisplayString
_WwpLeosSystemXFtpFtpServerHostName_Object=MibTableColumn
wwpLeosSystemXFtpFtpServerHostName=_WwpLeosSystemXFtpFtpServerHostName_Object((1,3,6,1,4,1,6141,2,60,12,1,10,9,1,2),_WwpLeosSystemXFtpFtpServerHostName_Type())
wwpLeosSystemXFtpFtpServerHostName.setMaxAccess(_F)
if mibBuilder.loadTexts:wwpLeosSystemXFtpFtpServerHostName.setStatus(_A)
_WwpLeosSystemXFtpFtpServerUserName_Type=DisplayString
_WwpLeosSystemXFtpFtpServerUserName_Object=MibTableColumn
wwpLeosSystemXFtpFtpServerUserName=_WwpLeosSystemXFtpFtpServerUserName_Object((1,3,6,1,4,1,6141,2,60,12,1,10,9,1,3),_WwpLeosSystemXFtpFtpServerUserName_Type())
wwpLeosSystemXFtpFtpServerUserName.setMaxAccess(_F)
if mibBuilder.loadTexts:wwpLeosSystemXFtpFtpServerUserName.setStatus(_A)
_WwpLeosSystemXFtpFtpServerPassword_Type=DisplayString
_WwpLeosSystemXFtpFtpServerPassword_Object=MibTableColumn
wwpLeosSystemXFtpFtpServerPassword=_WwpLeosSystemXFtpFtpServerPassword_Object((1,3,6,1,4,1,6141,2,60,12,1,10,9,1,4),_WwpLeosSystemXFtpFtpServerPassword_Type())
wwpLeosSystemXFtpFtpServerPassword.setMaxAccess(_F)
if mibBuilder.loadTexts:wwpLeosSystemXFtpFtpServerPassword.setStatus(_A)
_WwpLeosSystemXFtpFtpServerSecret_Type=DisplayString
_WwpLeosSystemXFtpFtpServerSecret_Object=MibTableColumn
wwpLeosSystemXFtpFtpServerSecret=_WwpLeosSystemXFtpFtpServerSecret_Object((1,3,6,1,4,1,6141,2,60,12,1,10,9,1,5),_WwpLeosSystemXFtpFtpServerSecret_Type())
wwpLeosSystemXFtpFtpServerSecret.setMaxAccess(_F)
if mibBuilder.loadTexts:wwpLeosSystemXFtpFtpServerSecret.setStatus(_A)
_WwpLeosSystemXFtpFtpServerRowStatus_Type=RowStatus
_WwpLeosSystemXFtpFtpServerRowStatus_Object=MibTableColumn
wwpLeosSystemXFtpFtpServerRowStatus=_WwpLeosSystemXFtpFtpServerRowStatus_Object((1,3,6,1,4,1,6141,2,60,12,1,10,9,1,6),_WwpLeosSystemXFtpFtpServerRowStatus_Type())
wwpLeosSystemXFtpFtpServerRowStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:wwpLeosSystemXFtpFtpServerRowStatus.setStatus(_A)
_WwpLeosSystemXFtpSFtpServerTable_Object=MibTable
wwpLeosSystemXFtpSFtpServerTable=_WwpLeosSystemXFtpSFtpServerTable_Object((1,3,6,1,4,1,6141,2,60,12,1,10,10))
if mibBuilder.loadTexts:wwpLeosSystemXFtpSFtpServerTable.setStatus(_A)
_WwpLeosSystemXFtpSFtpServerEntry_Object=MibTableRow
wwpLeosSystemXFtpSFtpServerEntry=_WwpLeosSystemXFtpSFtpServerEntry_Object((1,3,6,1,4,1,6141,2,60,12,1,10,10,1))
wwpLeosSystemXFtpSFtpServerEntry.setIndexNames((0,_D,_Y))
if mibBuilder.loadTexts:wwpLeosSystemXFtpSFtpServerEntry.setStatus(_A)
class _WwpLeosSystemXFtpSFtpServerIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1))
_WwpLeosSystemXFtpSFtpServerIndex_Type.__name__=_B
_WwpLeosSystemXFtpSFtpServerIndex_Object=MibTableColumn
wwpLeosSystemXFtpSFtpServerIndex=_WwpLeosSystemXFtpSFtpServerIndex_Object((1,3,6,1,4,1,6141,2,60,12,1,10,10,1,1),_WwpLeosSystemXFtpSFtpServerIndex_Type())
wwpLeosSystemXFtpSFtpServerIndex.setMaxAccess(_K)
if mibBuilder.loadTexts:wwpLeosSystemXFtpSFtpServerIndex.setStatus(_A)
_WwpLeosSystemXFtpSFtpServerHostName_Type=DisplayString
_WwpLeosSystemXFtpSFtpServerHostName_Object=MibTableColumn
wwpLeosSystemXFtpSFtpServerHostName=_WwpLeosSystemXFtpSFtpServerHostName_Object((1,3,6,1,4,1,6141,2,60,12,1,10,10,1,2),_WwpLeosSystemXFtpSFtpServerHostName_Type())
wwpLeosSystemXFtpSFtpServerHostName.setMaxAccess(_F)
if mibBuilder.loadTexts:wwpLeosSystemXFtpSFtpServerHostName.setStatus(_A)
_WwpLeosSystemXFtpSFtpServerUserName_Type=DisplayString
_WwpLeosSystemXFtpSFtpServerUserName_Object=MibTableColumn
wwpLeosSystemXFtpSFtpServerUserName=_WwpLeosSystemXFtpSFtpServerUserName_Object((1,3,6,1,4,1,6141,2,60,12,1,10,10,1,3),_WwpLeosSystemXFtpSFtpServerUserName_Type())
wwpLeosSystemXFtpSFtpServerUserName.setMaxAccess(_F)
if mibBuilder.loadTexts:wwpLeosSystemXFtpSFtpServerUserName.setStatus(_A)
_WwpLeosSystemXFtpSFtpServerPassword_Type=DisplayString
_WwpLeosSystemXFtpSFtpServerPassword_Object=MibTableColumn
wwpLeosSystemXFtpSFtpServerPassword=_WwpLeosSystemXFtpSFtpServerPassword_Object((1,3,6,1,4,1,6141,2,60,12,1,10,10,1,4),_WwpLeosSystemXFtpSFtpServerPassword_Type())
wwpLeosSystemXFtpSFtpServerPassword.setMaxAccess(_F)
if mibBuilder.loadTexts:wwpLeosSystemXFtpSFtpServerPassword.setStatus(_A)
_WwpLeosSystemXFtpSFtpServerSecret_Type=DisplayString
_WwpLeosSystemXFtpSFtpServerSecret_Object=MibTableColumn
wwpLeosSystemXFtpSFtpServerSecret=_WwpLeosSystemXFtpSFtpServerSecret_Object((1,3,6,1,4,1,6141,2,60,12,1,10,10,1,5),_WwpLeosSystemXFtpSFtpServerSecret_Type())
wwpLeosSystemXFtpSFtpServerSecret.setMaxAccess(_F)
if mibBuilder.loadTexts:wwpLeosSystemXFtpSFtpServerSecret.setStatus(_A)
_WwpLeosSystemXFtpSFtpServerRowStatus_Type=RowStatus
_WwpLeosSystemXFtpSFtpServerRowStatus_Object=MibTableColumn
wwpLeosSystemXFtpSFtpServerRowStatus=_WwpLeosSystemXFtpSFtpServerRowStatus_Object((1,3,6,1,4,1,6141,2,60,12,1,10,10,1,6),_WwpLeosSystemXFtpSFtpServerRowStatus_Type())
wwpLeosSystemXFtpSFtpServerRowStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:wwpLeosSystemXFtpSFtpServerRowStatus.setStatus(_A)
_WwpLeosSystemCpuUtilization_ObjectIdentity=ObjectIdentity
wwpLeosSystemCpuUtilization=_WwpLeosSystemCpuUtilization_ObjectIdentity((1,3,6,1,4,1,6141,2,60,12,1,11))
class _WwpLeosSystemCpuUtilizationLast5Seconds_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,100))
_WwpLeosSystemCpuUtilizationLast5Seconds_Type.__name__=_B
_WwpLeosSystemCpuUtilizationLast5Seconds_Object=MibScalar
wwpLeosSystemCpuUtilizationLast5Seconds=_WwpLeosSystemCpuUtilizationLast5Seconds_Object((1,3,6,1,4,1,6141,2,60,12,1,11,1),_WwpLeosSystemCpuUtilizationLast5Seconds_Type())
wwpLeosSystemCpuUtilizationLast5Seconds.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosSystemCpuUtilizationLast5Seconds.setStatus(_A)
class _WwpLeosSystemCpuUtilizationLast5SecondsMinimum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,100))
_WwpLeosSystemCpuUtilizationLast5SecondsMinimum_Type.__name__=_B
_WwpLeosSystemCpuUtilizationLast5SecondsMinimum_Object=MibScalar
wwpLeosSystemCpuUtilizationLast5SecondsMinimum=_WwpLeosSystemCpuUtilizationLast5SecondsMinimum_Object((1,3,6,1,4,1,6141,2,60,12,1,11,2),_WwpLeosSystemCpuUtilizationLast5SecondsMinimum_Type())
wwpLeosSystemCpuUtilizationLast5SecondsMinimum.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosSystemCpuUtilizationLast5SecondsMinimum.setStatus(_A)
class _WwpLeosSystemCpuUtilizationLast5SecondsMaximum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,100))
_WwpLeosSystemCpuUtilizationLast5SecondsMaximum_Type.__name__=_B
_WwpLeosSystemCpuUtilizationLast5SecondsMaximum_Object=MibScalar
wwpLeosSystemCpuUtilizationLast5SecondsMaximum=_WwpLeosSystemCpuUtilizationLast5SecondsMaximum_Object((1,3,6,1,4,1,6141,2,60,12,1,11,3),_WwpLeosSystemCpuUtilizationLast5SecondsMaximum_Type())
wwpLeosSystemCpuUtilizationLast5SecondsMaximum.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosSystemCpuUtilizationLast5SecondsMaximum.setStatus(_A)
class _WwpLeosSystemCpuUtilizationLast5SecondsState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_G,1),(_H,2),(_I,3),(_J,4)))
_WwpLeosSystemCpuUtilizationLast5SecondsState_Type.__name__=_B
_WwpLeosSystemCpuUtilizationLast5SecondsState_Object=MibScalar
wwpLeosSystemCpuUtilizationLast5SecondsState=_WwpLeosSystemCpuUtilizationLast5SecondsState_Object((1,3,6,1,4,1,6141,2,60,12,1,11,4),_WwpLeosSystemCpuUtilizationLast5SecondsState_Type())
wwpLeosSystemCpuUtilizationLast5SecondsState.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosSystemCpuUtilizationLast5SecondsState.setStatus(_A)
class _WwpLeosSystemCpuUtilizationLast10Seconds_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,100))
_WwpLeosSystemCpuUtilizationLast10Seconds_Type.__name__=_B
_WwpLeosSystemCpuUtilizationLast10Seconds_Object=MibScalar
wwpLeosSystemCpuUtilizationLast10Seconds=_WwpLeosSystemCpuUtilizationLast10Seconds_Object((1,3,6,1,4,1,6141,2,60,12,1,11,5),_WwpLeosSystemCpuUtilizationLast10Seconds_Type())
wwpLeosSystemCpuUtilizationLast10Seconds.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosSystemCpuUtilizationLast10Seconds.setStatus(_A)
class _WwpLeosSystemCpuUtilizationLast10SecondsMinimum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,100))
_WwpLeosSystemCpuUtilizationLast10SecondsMinimum_Type.__name__=_B
_WwpLeosSystemCpuUtilizationLast10SecondsMinimum_Object=MibScalar
wwpLeosSystemCpuUtilizationLast10SecondsMinimum=_WwpLeosSystemCpuUtilizationLast10SecondsMinimum_Object((1,3,6,1,4,1,6141,2,60,12,1,11,6),_WwpLeosSystemCpuUtilizationLast10SecondsMinimum_Type())
wwpLeosSystemCpuUtilizationLast10SecondsMinimum.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosSystemCpuUtilizationLast10SecondsMinimum.setStatus(_A)
class _WwpLeosSystemCpuUtilizationLast10SecondsMaximum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,100))
_WwpLeosSystemCpuUtilizationLast10SecondsMaximum_Type.__name__=_B
_WwpLeosSystemCpuUtilizationLast10SecondsMaximum_Object=MibScalar
wwpLeosSystemCpuUtilizationLast10SecondsMaximum=_WwpLeosSystemCpuUtilizationLast10SecondsMaximum_Object((1,3,6,1,4,1,6141,2,60,12,1,11,7),_WwpLeosSystemCpuUtilizationLast10SecondsMaximum_Type())
wwpLeosSystemCpuUtilizationLast10SecondsMaximum.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosSystemCpuUtilizationLast10SecondsMaximum.setStatus(_A)
class _WwpLeosSystemCpuUtilizationLast10SecondsState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_G,1),(_H,2),(_I,3),(_J,4)))
_WwpLeosSystemCpuUtilizationLast10SecondsState_Type.__name__=_B
_WwpLeosSystemCpuUtilizationLast10SecondsState_Object=MibScalar
wwpLeosSystemCpuUtilizationLast10SecondsState=_WwpLeosSystemCpuUtilizationLast10SecondsState_Object((1,3,6,1,4,1,6141,2,60,12,1,11,8),_WwpLeosSystemCpuUtilizationLast10SecondsState_Type())
wwpLeosSystemCpuUtilizationLast10SecondsState.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosSystemCpuUtilizationLast10SecondsState.setStatus(_A)
class _WwpLeosSystemCpuUtilizationLast60Seconds_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,100))
_WwpLeosSystemCpuUtilizationLast60Seconds_Type.__name__=_B
_WwpLeosSystemCpuUtilizationLast60Seconds_Object=MibScalar
wwpLeosSystemCpuUtilizationLast60Seconds=_WwpLeosSystemCpuUtilizationLast60Seconds_Object((1,3,6,1,4,1,6141,2,60,12,1,11,9),_WwpLeosSystemCpuUtilizationLast60Seconds_Type())
wwpLeosSystemCpuUtilizationLast60Seconds.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosSystemCpuUtilizationLast60Seconds.setStatus(_A)
class _WwpLeosSystemCpuUtilizationLast60SecondsMinimum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,100))
_WwpLeosSystemCpuUtilizationLast60SecondsMinimum_Type.__name__=_B
_WwpLeosSystemCpuUtilizationLast60SecondsMinimum_Object=MibScalar
wwpLeosSystemCpuUtilizationLast60SecondsMinimum=_WwpLeosSystemCpuUtilizationLast60SecondsMinimum_Object((1,3,6,1,4,1,6141,2,60,12,1,11,10),_WwpLeosSystemCpuUtilizationLast60SecondsMinimum_Type())
wwpLeosSystemCpuUtilizationLast60SecondsMinimum.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosSystemCpuUtilizationLast60SecondsMinimum.setStatus(_A)
class _WwpLeosSystemCpuUtilizationLast60SecondsMaximum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,100))
_WwpLeosSystemCpuUtilizationLast60SecondsMaximum_Type.__name__=_B
_WwpLeosSystemCpuUtilizationLast60SecondsMaximum_Object=MibScalar
wwpLeosSystemCpuUtilizationLast60SecondsMaximum=_WwpLeosSystemCpuUtilizationLast60SecondsMaximum_Object((1,3,6,1,4,1,6141,2,60,12,1,11,11),_WwpLeosSystemCpuUtilizationLast60SecondsMaximum_Type())
wwpLeosSystemCpuUtilizationLast60SecondsMaximum.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosSystemCpuUtilizationLast60SecondsMaximum.setStatus(_A)
class _WwpLeosSystemCpuUtilizationLast60SecondsState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_G,1),(_H,2),(_I,3),(_J,4)))
_WwpLeosSystemCpuUtilizationLast60SecondsState_Type.__name__=_B
_WwpLeosSystemCpuUtilizationLast60SecondsState_Object=MibScalar
wwpLeosSystemCpuUtilizationLast60SecondsState=_WwpLeosSystemCpuUtilizationLast60SecondsState_Object((1,3,6,1,4,1,6141,2,60,12,1,11,12),_WwpLeosSystemCpuUtilizationLast60SecondsState_Type())
wwpLeosSystemCpuUtilizationLast60SecondsState.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosSystemCpuUtilizationLast60SecondsState.setStatus(_A)
_WwpLeosSystemFileSystemUtilization_ObjectIdentity=ObjectIdentity
wwpLeosSystemFileSystemUtilization=_WwpLeosSystemFileSystemUtilization_ObjectIdentity((1,3,6,1,4,1,6141,2,60,12,1,12))
class _WwpLeosSystemFileSystemUtilizationTmpfsCurrent_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,100))
_WwpLeosSystemFileSystemUtilizationTmpfsCurrent_Type.__name__=_B
_WwpLeosSystemFileSystemUtilizationTmpfsCurrent_Object=MibScalar
wwpLeosSystemFileSystemUtilizationTmpfsCurrent=_WwpLeosSystemFileSystemUtilizationTmpfsCurrent_Object((1,3,6,1,4,1,6141,2,60,12,1,12,1),_WwpLeosSystemFileSystemUtilizationTmpfsCurrent_Type())
wwpLeosSystemFileSystemUtilizationTmpfsCurrent.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosSystemFileSystemUtilizationTmpfsCurrent.setStatus(_A)
class _WwpLeosSystemFileSystemUtilizationTmpfsMinimum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,100))
_WwpLeosSystemFileSystemUtilizationTmpfsMinimum_Type.__name__=_B
_WwpLeosSystemFileSystemUtilizationTmpfsMinimum_Object=MibScalar
wwpLeosSystemFileSystemUtilizationTmpfsMinimum=_WwpLeosSystemFileSystemUtilizationTmpfsMinimum_Object((1,3,6,1,4,1,6141,2,60,12,1,12,2),_WwpLeosSystemFileSystemUtilizationTmpfsMinimum_Type())
wwpLeosSystemFileSystemUtilizationTmpfsMinimum.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosSystemFileSystemUtilizationTmpfsMinimum.setStatus(_A)
class _WwpLeosSystemFileSystemUtilizationTmpfsMaximum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,100))
_WwpLeosSystemFileSystemUtilizationTmpfsMaximum_Type.__name__=_B
_WwpLeosSystemFileSystemUtilizationTmpfsMaximum_Object=MibScalar
wwpLeosSystemFileSystemUtilizationTmpfsMaximum=_WwpLeosSystemFileSystemUtilizationTmpfsMaximum_Object((1,3,6,1,4,1,6141,2,60,12,1,12,3),_WwpLeosSystemFileSystemUtilizationTmpfsMaximum_Type())
wwpLeosSystemFileSystemUtilizationTmpfsMaximum.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosSystemFileSystemUtilizationTmpfsMaximum.setStatus(_A)
class _WwpLeosSystemFileSystemUtilizationTmpfsState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_G,1),(_H,2),(_I,3),(_J,4)))
_WwpLeosSystemFileSystemUtilizationTmpfsState_Type.__name__=_B
_WwpLeosSystemFileSystemUtilizationTmpfsState_Object=MibScalar
wwpLeosSystemFileSystemUtilizationTmpfsState=_WwpLeosSystemFileSystemUtilizationTmpfsState_Object((1,3,6,1,4,1,6141,2,60,12,1,12,4),_WwpLeosSystemFileSystemUtilizationTmpfsState_Type())
wwpLeosSystemFileSystemUtilizationTmpfsState.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosSystemFileSystemUtilizationTmpfsState.setStatus(_A)
class _WwpLeosSystemFileSystemUtilizationSysfsCurrent_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,100))
_WwpLeosSystemFileSystemUtilizationSysfsCurrent_Type.__name__=_B
_WwpLeosSystemFileSystemUtilizationSysfsCurrent_Object=MibScalar
wwpLeosSystemFileSystemUtilizationSysfsCurrent=_WwpLeosSystemFileSystemUtilizationSysfsCurrent_Object((1,3,6,1,4,1,6141,2,60,12,1,12,5),_WwpLeosSystemFileSystemUtilizationSysfsCurrent_Type())
wwpLeosSystemFileSystemUtilizationSysfsCurrent.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosSystemFileSystemUtilizationSysfsCurrent.setStatus(_A)
class _WwpLeosSystemFileSystemUtilizationSysfsMinimum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,100))
_WwpLeosSystemFileSystemUtilizationSysfsMinimum_Type.__name__=_B
_WwpLeosSystemFileSystemUtilizationSysfsMinimum_Object=MibScalar
wwpLeosSystemFileSystemUtilizationSysfsMinimum=_WwpLeosSystemFileSystemUtilizationSysfsMinimum_Object((1,3,6,1,4,1,6141,2,60,12,1,12,6),_WwpLeosSystemFileSystemUtilizationSysfsMinimum_Type())
wwpLeosSystemFileSystemUtilizationSysfsMinimum.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosSystemFileSystemUtilizationSysfsMinimum.setStatus(_A)
class _WwpLeosSystemFileSystemUtilizationSysfsMaximum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,100))
_WwpLeosSystemFileSystemUtilizationSysfsMaximum_Type.__name__=_B
_WwpLeosSystemFileSystemUtilizationSysfsMaximum_Object=MibScalar
wwpLeosSystemFileSystemUtilizationSysfsMaximum=_WwpLeosSystemFileSystemUtilizationSysfsMaximum_Object((1,3,6,1,4,1,6141,2,60,12,1,12,7),_WwpLeosSystemFileSystemUtilizationSysfsMaximum_Type())
wwpLeosSystemFileSystemUtilizationSysfsMaximum.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosSystemFileSystemUtilizationSysfsMaximum.setStatus(_A)
class _WwpLeosSystemFileSystemUtilizationSysfsState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_G,1),(_H,2),(_I,3),(_J,4)))
_WwpLeosSystemFileSystemUtilizationSysfsState_Type.__name__=_B
_WwpLeosSystemFileSystemUtilizationSysfsState_Object=MibScalar
wwpLeosSystemFileSystemUtilizationSysfsState=_WwpLeosSystemFileSystemUtilizationSysfsState_Object((1,3,6,1,4,1,6141,2,60,12,1,12,8),_WwpLeosSystemFileSystemUtilizationSysfsState_Type())
wwpLeosSystemFileSystemUtilizationSysfsState.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosSystemFileSystemUtilizationSysfsState.setStatus(_A)
_WwpLeosSystemMemoryUtilization_ObjectIdentity=ObjectIdentity
wwpLeosSystemMemoryUtilization=_WwpLeosSystemMemoryUtilization_ObjectIdentity((1,3,6,1,4,1,6141,2,60,12,1,13))
_WwpLeosSystemMemoryUtilizationUsedMemoryCurrent_Type=Gauge32
_WwpLeosSystemMemoryUtilizationUsedMemoryCurrent_Object=MibScalar
wwpLeosSystemMemoryUtilizationUsedMemoryCurrent=_WwpLeosSystemMemoryUtilizationUsedMemoryCurrent_Object((1,3,6,1,4,1,6141,2,60,12,1,13,1),_WwpLeosSystemMemoryUtilizationUsedMemoryCurrent_Type())
wwpLeosSystemMemoryUtilizationUsedMemoryCurrent.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosSystemMemoryUtilizationUsedMemoryCurrent.setStatus(_A)
_WwpLeosSystemMemoryUtilizationUsedMemoryMinimum_Type=Gauge32
_WwpLeosSystemMemoryUtilizationUsedMemoryMinimum_Object=MibScalar
wwpLeosSystemMemoryUtilizationUsedMemoryMinimum=_WwpLeosSystemMemoryUtilizationUsedMemoryMinimum_Object((1,3,6,1,4,1,6141,2,60,12,1,13,2),_WwpLeosSystemMemoryUtilizationUsedMemoryMinimum_Type())
wwpLeosSystemMemoryUtilizationUsedMemoryMinimum.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosSystemMemoryUtilizationUsedMemoryMinimum.setStatus(_A)
_WwpLeosSystemMemoryUtilizationUsedMemoryMaximum_Type=Gauge32
_WwpLeosSystemMemoryUtilizationUsedMemoryMaximum_Object=MibScalar
wwpLeosSystemMemoryUtilizationUsedMemoryMaximum=_WwpLeosSystemMemoryUtilizationUsedMemoryMaximum_Object((1,3,6,1,4,1,6141,2,60,12,1,13,3),_WwpLeosSystemMemoryUtilizationUsedMemoryMaximum_Type())
wwpLeosSystemMemoryUtilizationUsedMemoryMaximum.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosSystemMemoryUtilizationUsedMemoryMaximum.setStatus(_A)
_WwpLeosSystemMemoryUtilizationAvailableMemoryCurrent_Type=Gauge32
_WwpLeosSystemMemoryUtilizationAvailableMemoryCurrent_Object=MibScalar
wwpLeosSystemMemoryUtilizationAvailableMemoryCurrent=_WwpLeosSystemMemoryUtilizationAvailableMemoryCurrent_Object((1,3,6,1,4,1,6141,2,60,12,1,13,4),_WwpLeosSystemMemoryUtilizationAvailableMemoryCurrent_Type())
wwpLeosSystemMemoryUtilizationAvailableMemoryCurrent.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosSystemMemoryUtilizationAvailableMemoryCurrent.setStatus(_A)
_WwpLeosSystemMemoryUtilizationAvailableMemoryMinimum_Type=Gauge32
_WwpLeosSystemMemoryUtilizationAvailableMemoryMinimum_Object=MibScalar
wwpLeosSystemMemoryUtilizationAvailableMemoryMinimum=_WwpLeosSystemMemoryUtilizationAvailableMemoryMinimum_Object((1,3,6,1,4,1,6141,2,60,12,1,13,5),_WwpLeosSystemMemoryUtilizationAvailableMemoryMinimum_Type())
wwpLeosSystemMemoryUtilizationAvailableMemoryMinimum.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosSystemMemoryUtilizationAvailableMemoryMinimum.setStatus(_A)
_WwpLeosSystemMemoryUtilizationAvailableMemoryMaximum_Type=Gauge32
_WwpLeosSystemMemoryUtilizationAvailableMemoryMaximum_Object=MibScalar
wwpLeosSystemMemoryUtilizationAvailableMemoryMaximum=_WwpLeosSystemMemoryUtilizationAvailableMemoryMaximum_Object((1,3,6,1,4,1,6141,2,60,12,1,13,6),_WwpLeosSystemMemoryUtilizationAvailableMemoryMaximum_Type())
wwpLeosSystemMemoryUtilizationAvailableMemoryMaximum.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosSystemMemoryUtilizationAvailableMemoryMaximum.setStatus(_A)
class _WwpLeosSystemMemoryUtilizationAvailableMemoryState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_G,1),(_H,2),(_I,3),(_J,4)))
_WwpLeosSystemMemoryUtilizationAvailableMemoryState_Type.__name__=_B
_WwpLeosSystemMemoryUtilizationAvailableMemoryState_Object=MibScalar
wwpLeosSystemMemoryUtilizationAvailableMemoryState=_WwpLeosSystemMemoryUtilizationAvailableMemoryState_Object((1,3,6,1,4,1,6141,2,60,12,1,13,7),_WwpLeosSystemMemoryUtilizationAvailableMemoryState_Type())
wwpLeosSystemMemoryUtilizationAvailableMemoryState.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosSystemMemoryUtilizationAvailableMemoryState.setStatus(_A)
_WwpLeosSystemGuardian_ObjectIdentity=ObjectIdentity
wwpLeosSystemGuardian=_WwpLeosSystemGuardian_ObjectIdentity((1,3,6,1,4,1,6141,2,60,12,1,14))
class _WwpLeosSystemGuardianAdminEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_P,1),(_Q,2)))
_WwpLeosSystemGuardianAdminEnable_Type.__name__=_B
_WwpLeosSystemGuardianAdminEnable_Object=MibScalar
wwpLeosSystemGuardianAdminEnable=_WwpLeosSystemGuardianAdminEnable_Object((1,3,6,1,4,1,6141,2,60,12,1,14,1),_WwpLeosSystemGuardianAdminEnable_Type())
wwpLeosSystemGuardianAdminEnable.setMaxAccess(_E)
if mibBuilder.loadTexts:wwpLeosSystemGuardianAdminEnable.setStatus(_A)
class _WwpLeosSystemGuardianOperEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_P,1),(_Q,2),('suspended',3)))
_WwpLeosSystemGuardianOperEnable_Type.__name__=_B
_WwpLeosSystemGuardianOperEnable_Object=MibScalar
wwpLeosSystemGuardianOperEnable=_WwpLeosSystemGuardianOperEnable_Object((1,3,6,1,4,1,6141,2,60,12,1,14,2),_WwpLeosSystemGuardianOperEnable_Type())
wwpLeosSystemGuardianOperEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosSystemGuardianOperEnable.setStatus(_A)
class _WwpLeosSystemGuardianLimitNumReboots_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('on',1),('off',2)))
_WwpLeosSystemGuardianLimitNumReboots_Type.__name__=_B
_WwpLeosSystemGuardianLimitNumReboots_Object=MibScalar
wwpLeosSystemGuardianLimitNumReboots=_WwpLeosSystemGuardianLimitNumReboots_Object((1,3,6,1,4,1,6141,2,60,12,1,14,3),_WwpLeosSystemGuardianLimitNumReboots_Type())
wwpLeosSystemGuardianLimitNumReboots.setMaxAccess(_E)
if mibBuilder.loadTexts:wwpLeosSystemGuardianLimitNumReboots.setStatus(_A)
class _WwpLeosSystemGuardianConsecutiveReboots_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_WwpLeosSystemGuardianConsecutiveReboots_Type.__name__=_B
_WwpLeosSystemGuardianConsecutiveReboots_Object=MibScalar
wwpLeosSystemGuardianConsecutiveReboots=_WwpLeosSystemGuardianConsecutiveReboots_Object((1,3,6,1,4,1,6141,2,60,12,1,14,4),_WwpLeosSystemGuardianConsecutiveReboots_Type())
wwpLeosSystemGuardianConsecutiveReboots.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosSystemGuardianConsecutiveReboots.setStatus(_A)
class _WwpLeosSystemGuardianTotalReboots_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_WwpLeosSystemGuardianTotalReboots_Type.__name__=_B
_WwpLeosSystemGuardianTotalReboots_Object=MibScalar
wwpLeosSystemGuardianTotalReboots=_WwpLeosSystemGuardianTotalReboots_Object((1,3,6,1,4,1,6141,2,60,12,1,14,5),_WwpLeosSystemGuardianTotalReboots_Type())
wwpLeosSystemGuardianTotalReboots.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosSystemGuardianTotalReboots.setStatus(_A)
_WwpLeosSystemServers_ObjectIdentity=ObjectIdentity
wwpLeosSystemServers=_WwpLeosSystemServers_ObjectIdentity((1,3,6,1,4,1,6141,2,60,12,1,15))
class _WwpLeosSystemSftpServerAdminState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_P,1),(_Q,2)))
_WwpLeosSystemSftpServerAdminState_Type.__name__=_B
_WwpLeosSystemSftpServerAdminState_Object=MibScalar
wwpLeosSystemSftpServerAdminState=_WwpLeosSystemSftpServerAdminState_Object((1,3,6,1,4,1,6141,2,60,12,1,15,1),_WwpLeosSystemSftpServerAdminState_Type())
wwpLeosSystemSftpServerAdminState.setMaxAccess(_E)
if mibBuilder.loadTexts:wwpLeosSystemSftpServerAdminState.setStatus(_A)
_WwpLeosSystemConfigMIBNotificationPrefix_ObjectIdentity=ObjectIdentity
wwpLeosSystemConfigMIBNotificationPrefix=_WwpLeosSystemConfigMIBNotificationPrefix_ObjectIdentity((1,3,6,1,4,1,6141,2,60,12,2))
_WwpLeosSystemConfigMIBNotifications_ObjectIdentity=ObjectIdentity
wwpLeosSystemConfigMIBNotifications=_WwpLeosSystemConfigMIBNotifications_ObjectIdentity((1,3,6,1,4,1,6141,2,60,12,2,0))
_WwpLeosSystemConfigMIBConformance_ObjectIdentity=ObjectIdentity
wwpLeosSystemConfigMIBConformance=_WwpLeosSystemConfigMIBConformance_ObjectIdentity((1,3,6,1,4,1,6141,2,60,12,3))
_WwpLeosSystemConfigCompliances_ObjectIdentity=ObjectIdentity
wwpLeosSystemConfigCompliances=_WwpLeosSystemConfigCompliances_ObjectIdentity((1,3,6,1,4,1,6141,2,60,12,3,1))
_WwpLeosSystemConfigMIBGroups_ObjectIdentity=ObjectIdentity
wwpLeosSystemConfigMIBGroups=_WwpLeosSystemConfigMIBGroups_ObjectIdentity((1,3,6,1,4,1,6141,2,60,12,3,2))
wwpLeosDefaultGatewayIPv6Group=ObjectGroup((1,3,6,1,4,1,6141,2,60,12,3,2,1))
wwpLeosDefaultGatewayIPv6Group.setObjects(*((_D,_Z),(_D,_a)))
if mibBuilder.loadTexts:wwpLeosDefaultGatewayIPv6Group.setStatus(_A)
wwpLeosBackupGatewayIPv6Group=ObjectGroup((1,3,6,1,4,1,6141,2,60,12,3,2,2))
wwpLeosBackupGatewayIPv6Group.setObjects(*((_D,_b),(_D,_c)))
if mibBuilder.loadTexts:wwpLeosBackupGatewayIPv6Group.setStatus(_A)
wwpLeosImproperCmdInConfigFile=NotificationType((1,3,6,1,4,1,6141,2,60,12,2,0,1))
wwpLeosImproperCmdInConfigFile.setObjects(*((_D,_R),(_D,_S),(_D,_d)))
if mibBuilder.loadTexts:wwpLeosImproperCmdInConfigFile.setStatus(_A)
wwpLeosSystemServiceModeChange=NotificationType((1,3,6,1,4,1,6141,2,60,12,2,0,2))
wwpLeosSystemServiceModeChange.setObjects((_D,_e))
if mibBuilder.loadTexts:wwpLeosSystemServiceModeChange.setStatus(_A)
wwpLeosSystemMemoryStatusNotification=NotificationType((1,3,6,1,4,1,6141,2,60,12,2,0,3))
wwpLeosSystemMemoryStatusNotification.setObjects(*((_D,_f),(_D,_g),(_D,_h),(_D,_i)))
if mibBuilder.loadTexts:wwpLeosSystemMemoryStatusNotification.setStatus(_A)
wwpLeosImproperCmdInConfigLineString=NotificationType((1,3,6,1,4,1,6141,2,60,12,2,0,4))
wwpLeosImproperCmdInConfigLineString.setObjects(*((_D,_j),(_D,_S),(_D,_R)))
if mibBuilder.loadTexts:wwpLeosImproperCmdInConfigLineString.setStatus(_A)
wwpLeosSystemCpuUtilization5SecondStatusTrap=NotificationType((1,3,6,1,4,1,6141,2,60,12,2,0,5))
wwpLeosSystemCpuUtilization5SecondStatusTrap.setObjects(*((_D,_k),(_D,_l)))
if mibBuilder.loadTexts:wwpLeosSystemCpuUtilization5SecondStatusTrap.setStatus(_A)
wwpLeosSystemCpuUtilization10SecondStatusTrap=NotificationType((1,3,6,1,4,1,6141,2,60,12,2,0,6))
wwpLeosSystemCpuUtilization10SecondStatusTrap.setObjects(*((_D,_m),(_D,_n)))
if mibBuilder.loadTexts:wwpLeosSystemCpuUtilization10SecondStatusTrap.setStatus(_A)
wwpLeosSystemCpuUtilization60SecondStatusTrap=NotificationType((1,3,6,1,4,1,6141,2,60,12,2,0,7))
wwpLeosSystemCpuUtilization60SecondStatusTrap.setObjects(*((_D,_o),(_D,_p)))
if mibBuilder.loadTexts:wwpLeosSystemCpuUtilization60SecondStatusTrap.setStatus(_A)
wwpLeosSystemCpu1MinLoadStatusTrap=NotificationType((1,3,6,1,4,1,6141,2,60,12,2,0,8))
wwpLeosSystemCpu1MinLoadStatusTrap.setObjects(*((_D,_q),(_D,_r)))
if mibBuilder.loadTexts:wwpLeosSystemCpu1MinLoadStatusTrap.setStatus(_A)
wwpLeosSystemCpu5MinLoadStatusTrap=NotificationType((1,3,6,1,4,1,6141,2,60,12,2,0,9))
wwpLeosSystemCpu5MinLoadStatusTrap.setObjects(*((_D,_s),(_D,_t)))
if mibBuilder.loadTexts:wwpLeosSystemCpu5MinLoadStatusTrap.setStatus(_A)
wwpLeosSystemCpu15MinLoadStatusTrap=NotificationType((1,3,6,1,4,1,6141,2,60,12,2,0,10))
wwpLeosSystemCpu15MinLoadStatusTrap.setObjects(*((_D,_u),(_D,_v)))
if mibBuilder.loadTexts:wwpLeosSystemCpu15MinLoadStatusTrap.setStatus(_A)
wwpLeosSystemMemoryUtilizationStatusTrap=NotificationType((1,3,6,1,4,1,6141,2,60,12,2,0,11))
wwpLeosSystemMemoryUtilizationStatusTrap.setObjects(*((_D,_w),(_D,_x)))
if mibBuilder.loadTexts:wwpLeosSystemMemoryUtilizationStatusTrap.setStatus(_A)
wwpLeosSystemFileSystemUtilizationTmpStatusTrap=NotificationType((1,3,6,1,4,1,6141,2,60,12,2,0,12))
wwpLeosSystemFileSystemUtilizationTmpStatusTrap.setObjects(*((_D,_y),(_D,_z)))
if mibBuilder.loadTexts:wwpLeosSystemFileSystemUtilizationTmpStatusTrap.setStatus(_A)
wwpLeosSystemFileSystemUtilizationSysfsStatusTrap=NotificationType((1,3,6,1,4,1,6141,2,60,12,2,0,13))
wwpLeosSystemFileSystemUtilizationSysfsStatusTrap.setObjects(*((_D,_A0),(_D,_A1)))
if mibBuilder.loadTexts:wwpLeosSystemFileSystemUtilizationSysfsStatusTrap.setStatus(_A)
wwpLeosDefaultGatewayCompliance=ModuleCompliance((1,3,6,1,4,1,6141,2,60,12,3,1,1))
wwpLeosDefaultGatewayCompliance.setObjects((_D,_A2))
if mibBuilder.loadTexts:wwpLeosDefaultGatewayCompliance.setStatus(_A)
wwpLeosBackupGatewayCompliance=ModuleCompliance((1,3,6,1,4,1,6141,2,60,12,3,1,2))
wwpLeosBackupGatewayCompliance.setObjects((_D,_A3))
if mibBuilder.loadTexts:wwpLeosBackupGatewayCompliance.setStatus(_A)
mibBuilder.exportSymbols(_D,**{'FileName':FileName,'wwpLeosSystemConfigMIB':wwpLeosSystemConfigMIB,'wwpLeosSystemConfigMIBObjects':wwpLeosSystemConfigMIBObjects,'wwpLeosSystemConfigAttr':wwpLeosSystemConfigAttr,'wwpLeosSystemConfigDefaultGateway':wwpLeosSystemConfigDefaultGateway,'wwpLeosSystemConfigBootCmdFile':wwpLeosSystemConfigBootCmdFile,'wwpLeosSystemConfigBootCfgFile':wwpLeosSystemConfigBootCfgFile,'wwpLeosSystemClockDateTime':wwpLeosSystemClockDateTime,'wwpLeosSystemConfigSavePermFile':wwpLeosSystemConfigSavePermFile,'wwpLeosSystemConfigLastFileNameReset':wwpLeosSystemConfigLastFileNameReset,_e:wwpLeosSystemServiceMode,'wwpLeosSystemConfigBackupGateway':wwpLeosSystemConfigBackupGateway,'wwpLeosSystemConfigCustomerCfgFile':wwpLeosSystemConfigCustomerCfgFile,'wwpLeosSystemConfigDefaultGatewayTable':wwpLeosSystemConfigDefaultGatewayTable,'wwpLeosSystemConfigDefaultGatewayEntry':wwpLeosSystemConfigDefaultGatewayEntry,_T:wwpLeosSystemConfigDefaultGatewayIndex,_Z:wwpLeosSystemConfigDefaultGatewayInetAddrType,_a:wwpLeosSystemConfigDefaultGatewayInetAddress,'wwpLeosSystemConfigDefaultGatewayInterfaceName':wwpLeosSystemConfigDefaultGatewayInterfaceName,'wwpLeosSystemConfigDefaultGatewayMetric':wwpLeosSystemConfigDefaultGatewayMetric,'wwpLeosSystemConfigDefaultGatewayStatus':wwpLeosSystemConfigDefaultGatewayStatus,'wwpLeosSystemConfigBackupGatewayTable':wwpLeosSystemConfigBackupGatewayTable,'wwpLeosSystemConfigBackupGatewayEntry':wwpLeosSystemConfigBackupGatewayEntry,_U:wwpLeosSystemConfigBackupGatewayIndex,_b:wwpLeosSystemConfigBackupGatewayInetAddrType,_c:wwpLeosSystemConfigBackupGatewayInetAddress,'wwpLeosSystemConfigBackupGatewayInterfaceName':wwpLeosSystemConfigBackupGatewayInterfaceName,'wwpLeosSystemConfigBackupGatewayMetric':wwpLeosSystemConfigBackupGatewayMetric,'wwpLeosSystemConfigBackupGatewayStatus':wwpLeosSystemConfigBackupGatewayStatus,'wwpLeosSystemConfig':wwpLeosSystemConfig,'wwpLeosSystemConfigSaveFileName':wwpLeosSystemConfigSaveFileName,'wwpLeosSystemConfigControl':wwpLeosSystemConfigControl,'wwpLeosSystemConfigFilepath':wwpLeosSystemConfigFilepath,'wwpLeosSystemConfigFileTable':wwpLeosSystemConfigFileTable,'wwpLeosSystemConfigFileEntry':wwpLeosSystemConfigFileEntry,_O:wwpLeosSystemConfigFileIndex,_R:wwpLeosSystemConfigFileName,'wwpLeosSystemConfigActivateFile':wwpLeosSystemConfigActivateFile,'wwpLeosSystemTelnet':wwpLeosSystemTelnet,'wwpLeosTelnetMaxBaseUserSessions':wwpLeosTelnetMaxBaseUserSessions,'wwpLeosTelnetMaxSuperUserSessions':wwpLeosTelnetMaxSuperUserSessions,'wwpLeosTelnetMaxAdminUserSessions':wwpLeosTelnetMaxAdminUserSessions,'wwpLeosSystemCpuLoadQuery':wwpLeosSystemCpuLoadQuery,_q:wwpLeosSystemCpuLoad1Min,'wwpLeosSystemCpuLoad10Min':wwpLeosSystemCpuLoad10Min,_u:wwpLeosSystemCpuLoad15Min,_s:wwpLeosSystemCpuLoad5Min,'wwpLeosSystemCpuLoad1MinMinimum':wwpLeosSystemCpuLoad1MinMinimum,'wwpLeosSystemCpuLoad1MinMaximum':wwpLeosSystemCpuLoad1MinMaximum,_r:wwpLeosSystemCpuLoad1MinState,'wwpLeosSystemCpuLoad15MinMinimum':wwpLeosSystemCpuLoad15MinMinimum,'wwpLeosSystemCpuLoad15MinMaximum':wwpLeosSystemCpuLoad15MinMaximum,_v:wwpLeosSystemCpuLoad15MinState,'wwpLeosSystemCpuLoad5MinMinimum':wwpLeosSystemCpuLoad5MinMinimum,'wwpLeosSystemCpuLoad5MinMaximum':wwpLeosSystemCpuLoad5MinMaximum,_t:wwpLeosSystemCpuLoad5MinState,'wwpLeosSystemConfigNotif':wwpLeosSystemConfigNotif,'wwpLeosSystemConfigNotifTable':wwpLeosSystemConfigNotifTable,'wwpLeosSystemConfigNotifEntry':wwpLeosSystemConfigNotifEntry,_S:wwpLeosSystemConfigErrLineNum,_j:wwpLeosSystemConfigErrStr,_d:wwpLeosSystemConfigErrLinesTotal,'wwpLeosSystemMemoryUsageQuery':wwpLeosSystemMemoryUsageQuery,'wwpLeosSystemMemoryUsageTable':wwpLeosSystemMemoryUsageTable,'wwpLeosSystemMemoryUsageEntry':wwpLeosSystemMemoryUsageEntry,_V:wwpLeosSystemMemoryUsagePoolIndex,_f:wwpLeosSystemMemoryUsageMemoryTotal,'wwpLeosSystemMemoryUsageMemoryLWM':wwpLeosSystemMemoryUsageMemoryLWM,_g:wwpLeosSystemMemoryUsageMemoryFree,_h:wwpLeosSystemMemoryUsageStatus,'wwpLeosSystemMemoryUsageMemoryUsed':wwpLeosSystemMemoryUsageMemoryUsed,_i:wwpLeosSystemMemoryUsageMemoryAvailable,'wwpLeosSystemXFtp':wwpLeosSystemXFtp,'wwpLeosSystemXFtpMode':wwpLeosSystemXFtpMode,'wwpLeosSystemXFtpServer':wwpLeosSystemXFtpServer,'wwpLeosSystemXFtpUserName':wwpLeosSystemXFtpUserName,'wwpLeosSystemXFtpPasswd':wwpLeosSystemXFtpPasswd,'wwpLeosSystemXFtpNumOfRetries':wwpLeosSystemXFtpNumOfRetries,'wwpLeosSystemXFtpRetryInterval':wwpLeosSystemXFtpRetryInterval,'wwpLeosSystemXFtpConnectionTimeout':wwpLeosSystemXFtpConnectionTimeout,'wwpLeosSystemXFtpTFtpServerTable':wwpLeosSystemXFtpTFtpServerTable,'wwpLeosSystemXFtpTFtpServerEntry':wwpLeosSystemXFtpTFtpServerEntry,_W:wwpLeosSystemXFtpTFtpServerIndex,'wwpLeosSystemXFtpTFtpServerHostName':wwpLeosSystemXFtpTFtpServerHostName,'wwpLeosSystemXFtpTFtpServerRowStatus':wwpLeosSystemXFtpTFtpServerRowStatus,'wwpLeosSystemXFtpFtpServerTable':wwpLeosSystemXFtpFtpServerTable,'wwpLeosSystemXFtpFtpServerEntry':wwpLeosSystemXFtpFtpServerEntry,_X:wwpLeosSystemXFtpFtpServerIndex,'wwpLeosSystemXFtpFtpServerHostName':wwpLeosSystemXFtpFtpServerHostName,'wwpLeosSystemXFtpFtpServerUserName':wwpLeosSystemXFtpFtpServerUserName,'wwpLeosSystemXFtpFtpServerPassword':wwpLeosSystemXFtpFtpServerPassword,'wwpLeosSystemXFtpFtpServerSecret':wwpLeosSystemXFtpFtpServerSecret,'wwpLeosSystemXFtpFtpServerRowStatus':wwpLeosSystemXFtpFtpServerRowStatus,'wwpLeosSystemXFtpSFtpServerTable':wwpLeosSystemXFtpSFtpServerTable,'wwpLeosSystemXFtpSFtpServerEntry':wwpLeosSystemXFtpSFtpServerEntry,_Y:wwpLeosSystemXFtpSFtpServerIndex,'wwpLeosSystemXFtpSFtpServerHostName':wwpLeosSystemXFtpSFtpServerHostName,'wwpLeosSystemXFtpSFtpServerUserName':wwpLeosSystemXFtpSFtpServerUserName,'wwpLeosSystemXFtpSFtpServerPassword':wwpLeosSystemXFtpSFtpServerPassword,'wwpLeosSystemXFtpSFtpServerSecret':wwpLeosSystemXFtpSFtpServerSecret,'wwpLeosSystemXFtpSFtpServerRowStatus':wwpLeosSystemXFtpSFtpServerRowStatus,'wwpLeosSystemCpuUtilization':wwpLeosSystemCpuUtilization,_k:wwpLeosSystemCpuUtilizationLast5Seconds,'wwpLeosSystemCpuUtilizationLast5SecondsMinimum':wwpLeosSystemCpuUtilizationLast5SecondsMinimum,'wwpLeosSystemCpuUtilizationLast5SecondsMaximum':wwpLeosSystemCpuUtilizationLast5SecondsMaximum,_l:wwpLeosSystemCpuUtilizationLast5SecondsState,_m:wwpLeosSystemCpuUtilizationLast10Seconds,'wwpLeosSystemCpuUtilizationLast10SecondsMinimum':wwpLeosSystemCpuUtilizationLast10SecondsMinimum,'wwpLeosSystemCpuUtilizationLast10SecondsMaximum':wwpLeosSystemCpuUtilizationLast10SecondsMaximum,_n:wwpLeosSystemCpuUtilizationLast10SecondsState,_o:wwpLeosSystemCpuUtilizationLast60Seconds,'wwpLeosSystemCpuUtilizationLast60SecondsMinimum':wwpLeosSystemCpuUtilizationLast60SecondsMinimum,'wwpLeosSystemCpuUtilizationLast60SecondsMaximum':wwpLeosSystemCpuUtilizationLast60SecondsMaximum,_p:wwpLeosSystemCpuUtilizationLast60SecondsState,'wwpLeosSystemFileSystemUtilization':wwpLeosSystemFileSystemUtilization,_y:wwpLeosSystemFileSystemUtilizationTmpfsCurrent,'wwpLeosSystemFileSystemUtilizationTmpfsMinimum':wwpLeosSystemFileSystemUtilizationTmpfsMinimum,'wwpLeosSystemFileSystemUtilizationTmpfsMaximum':wwpLeosSystemFileSystemUtilizationTmpfsMaximum,_z:wwpLeosSystemFileSystemUtilizationTmpfsState,_A0:wwpLeosSystemFileSystemUtilizationSysfsCurrent,'wwpLeosSystemFileSystemUtilizationSysfsMinimum':wwpLeosSystemFileSystemUtilizationSysfsMinimum,'wwpLeosSystemFileSystemUtilizationSysfsMaximum':wwpLeosSystemFileSystemUtilizationSysfsMaximum,_A1:wwpLeosSystemFileSystemUtilizationSysfsState,'wwpLeosSystemMemoryUtilization':wwpLeosSystemMemoryUtilization,'wwpLeosSystemMemoryUtilizationUsedMemoryCurrent':wwpLeosSystemMemoryUtilizationUsedMemoryCurrent,'wwpLeosSystemMemoryUtilizationUsedMemoryMinimum':wwpLeosSystemMemoryUtilizationUsedMemoryMinimum,'wwpLeosSystemMemoryUtilizationUsedMemoryMaximum':wwpLeosSystemMemoryUtilizationUsedMemoryMaximum,_w:wwpLeosSystemMemoryUtilizationAvailableMemoryCurrent,'wwpLeosSystemMemoryUtilizationAvailableMemoryMinimum':wwpLeosSystemMemoryUtilizationAvailableMemoryMinimum,'wwpLeosSystemMemoryUtilizationAvailableMemoryMaximum':wwpLeosSystemMemoryUtilizationAvailableMemoryMaximum,_x:wwpLeosSystemMemoryUtilizationAvailableMemoryState,'wwpLeosSystemGuardian':wwpLeosSystemGuardian,'wwpLeosSystemGuardianAdminEnable':wwpLeosSystemGuardianAdminEnable,'wwpLeosSystemGuardianOperEnable':wwpLeosSystemGuardianOperEnable,'wwpLeosSystemGuardianLimitNumReboots':wwpLeosSystemGuardianLimitNumReboots,'wwpLeosSystemGuardianConsecutiveReboots':wwpLeosSystemGuardianConsecutiveReboots,'wwpLeosSystemGuardianTotalReboots':wwpLeosSystemGuardianTotalReboots,'wwpLeosSystemServers':wwpLeosSystemServers,'wwpLeosSystemSftpServerAdminState':wwpLeosSystemSftpServerAdminState,'wwpLeosSystemConfigMIBNotificationPrefix':wwpLeosSystemConfigMIBNotificationPrefix,'wwpLeosSystemConfigMIBNotifications':wwpLeosSystemConfigMIBNotifications,'wwpLeosImproperCmdInConfigFile':wwpLeosImproperCmdInConfigFile,'wwpLeosSystemServiceModeChange':wwpLeosSystemServiceModeChange,'wwpLeosSystemMemoryStatusNotification':wwpLeosSystemMemoryStatusNotification,'wwpLeosImproperCmdInConfigLineString':wwpLeosImproperCmdInConfigLineString,'wwpLeosSystemCpuUtilization5SecondStatusTrap':wwpLeosSystemCpuUtilization5SecondStatusTrap,'wwpLeosSystemCpuUtilization10SecondStatusTrap':wwpLeosSystemCpuUtilization10SecondStatusTrap,'wwpLeosSystemCpuUtilization60SecondStatusTrap':wwpLeosSystemCpuUtilization60SecondStatusTrap,'wwpLeosSystemCpu1MinLoadStatusTrap':wwpLeosSystemCpu1MinLoadStatusTrap,'wwpLeosSystemCpu5MinLoadStatusTrap':wwpLeosSystemCpu5MinLoadStatusTrap,'wwpLeosSystemCpu15MinLoadStatusTrap':wwpLeosSystemCpu15MinLoadStatusTrap,'wwpLeosSystemMemoryUtilizationStatusTrap':wwpLeosSystemMemoryUtilizationStatusTrap,'wwpLeosSystemFileSystemUtilizationTmpStatusTrap':wwpLeosSystemFileSystemUtilizationTmpStatusTrap,'wwpLeosSystemFileSystemUtilizationSysfsStatusTrap':wwpLeosSystemFileSystemUtilizationSysfsStatusTrap,'wwpLeosSystemConfigMIBConformance':wwpLeosSystemConfigMIBConformance,'wwpLeosSystemConfigCompliances':wwpLeosSystemConfigCompliances,'wwpLeosDefaultGatewayCompliance':wwpLeosDefaultGatewayCompliance,'wwpLeosBackupGatewayCompliance':wwpLeosBackupGatewayCompliance,'wwpLeosSystemConfigMIBGroups':wwpLeosSystemConfigMIBGroups,_A2:wwpLeosDefaultGatewayIPv6Group,_A3:wwpLeosBackupGatewayIPv6Group})