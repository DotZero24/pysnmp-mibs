_AC='hpnicfCfgManNotificationGroup'
_AB='hpnicfCfgOperateGroup'
_AA='hpnicfCfgManLogGroup'
_A9='hpnicfCfgInvalidConfigFile'
_A8='hpnicfCfgOperateCompletion'
_A7='hpnicfCfgManEventlog'
_A6='hpnicfCfgFirstTrapTime'
_A5='hpnicfCfgOperateServerPort'
_A4='hpnicfCfgOperateResultOpType'
_A3='hpnicfCfgOperateResultOptIndex'
_A2='hpnicfCfgOperateRowStatus'
_A1='hpnicfCfgOperateResultGlobalEntryLimit'
_A0='hpnicfCfgOperateEndNotificationSwitch'
_z='hpnicfCfgOperateUserPassword'
_y='hpnicfCfgOperateUserName'
_x='hpnicfCfgOperateServerAddress'
_w='hpnicfCfgOperateProtocol'
_v='hpnicfCfgOperateEntryAgeOutTime'
_u='hpnicfCfgOperateGlobalEntryLimit'
_t='hpnicfCfgLogWantBackup'
_s='hpnicfCfgLogUserName'
_r='hpnicfCfgLogFile'
_q='hpnicfCfgLogServerAddress'
_p='hpnicfCfgLogVirHost'
_o='hpnicfCfgLogCmdSrcAddress'
_n='hpnicfCfgLogTerminalLocation'
_m='hpnicfCfgLogTerminalUser'
_l='hpnicfCfgLogTerminalNum'
_k='hpnicfCfgLogTerminalType'
_j='hpnicfCfgLogTime'
_i='hpnicfCfgLogDeletedEntries'
_h='hpnicfCfgLogLimitedEntries'
_g='hpnicfCfgStartModifiedLast'
_f='hpnicfCfgRunSavedLast'
_e='hpnicfCfgRunModifiedLast'
_d='normal'
_c='hpnicfCfgExecuteResultIndex'
_b='hpnicfCfgOperateResultIndex'
_a='hpnicfCfgOperateIndex'
_Z='unknown'
_Y='hotPlugging'
_X='netFtp'
_W='startupData'
_V='commandSource'
_U='runningData'
_T='hpnicfCfgLogIndex'
_S='hpnicfCfgOperFailReason'
_R='hpnicfCfgOperateEndTime'
_Q='hpnicfCfgOperateState'
_P='hpnicfCfgOperateTime'
_O='hpnicfCfgOperateFileName'
_N='hpnicfCfgLogDesData'
_M='hpnicfCfgLogSrcData'
_L='hpnicfCfgLogSrcCmd'
_K='deprecated'
_J='TruthValue'
_I='hpnicfCfgOperateType'
_H='not-accessible'
_G='read-write'
_F='DisplayString'
_E='read-create'
_D='Integer32'
_C='read-only'
_B='HPN-ICF-CONFIG-MAN-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
hpnicfCommon,=mibBuilder.importSymbols('HPN-ICF-OID-MIB','hpnicfCommon')
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress','InetAddressType')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC',_F,'PhysAddress','RowStatus','TextualConvention',_J)
hpnicfConfig=ModuleIdentity((1,3,6,1,4,1,11,2,14,11,15,2,4))
if mibBuilder.loadTexts:hpnicfConfig.setRevisions(('2011-11-26 00:00',))
class ConfigOperationType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*(('running2Startup',1),('startup2Running',2),('running2Net',3),('net2Running',4),('net2Startup',5),('startup2Net',6)))
class ConfigOperationStateType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22)));namedValues=NamedValues(*(('opInProgress',1),('opSuccess',2),('opInvalidOperation',3),('opInvalidProtocol',4),('opInvalidSourceName',5),('opInvalidDestName',6),('opInvalidServerAddress',7),('opDeviceBusy',8),('opDeviceOpenError',9),('opDeviceError',10),('opDeviceNotProgrammable',11),('opDeviceFull',12),('opFileOpenError',13),('opFileTransferError',14),('opFileChecksumError',15),('opNoMemory',16),('opAuthFail',17),('opTimeOut',18),('opUnknownFailure',19),('opInvalidConfigFile',20),('opSlaveFull',21),('opCopyToSlaveFailure',22)))
_HpnicfConfigManObjects_ObjectIdentity=ObjectIdentity
hpnicfConfigManObjects=_HpnicfConfigManObjects_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,4,1))
_HpnicfCfgLog_ObjectIdentity=ObjectIdentity
hpnicfCfgLog=_HpnicfCfgLog_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,4,1,1))
_HpnicfCfgRunModifiedLast_Type=TimeTicks
_HpnicfCfgRunModifiedLast_Object=MibScalar
hpnicfCfgRunModifiedLast=_HpnicfCfgRunModifiedLast_Object((1,3,6,1,4,1,11,2,14,11,15,2,4,1,1,1),_HpnicfCfgRunModifiedLast_Type())
hpnicfCfgRunModifiedLast.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfCfgRunModifiedLast.setStatus(_A)
_HpnicfCfgRunSavedLast_Type=TimeTicks
_HpnicfCfgRunSavedLast_Object=MibScalar
hpnicfCfgRunSavedLast=_HpnicfCfgRunSavedLast_Object((1,3,6,1,4,1,11,2,14,11,15,2,4,1,1,2),_HpnicfCfgRunSavedLast_Type())
hpnicfCfgRunSavedLast.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfCfgRunSavedLast.setStatus(_A)
_HpnicfCfgStartModifiedLast_Type=TimeTicks
_HpnicfCfgStartModifiedLast_Object=MibScalar
hpnicfCfgStartModifiedLast=_HpnicfCfgStartModifiedLast_Object((1,3,6,1,4,1,11,2,14,11,15,2,4,1,1,3),_HpnicfCfgStartModifiedLast_Type())
hpnicfCfgStartModifiedLast.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfCfgStartModifiedLast.setStatus(_A)
class _HpnicfCfgLogLimitedEntries_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_HpnicfCfgLogLimitedEntries_Type.__name__=_D
_HpnicfCfgLogLimitedEntries_Object=MibScalar
hpnicfCfgLogLimitedEntries=_HpnicfCfgLogLimitedEntries_Object((1,3,6,1,4,1,11,2,14,11,15,2,4,1,1,4),_HpnicfCfgLogLimitedEntries_Type())
hpnicfCfgLogLimitedEntries.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfCfgLogLimitedEntries.setStatus(_A)
_HpnicfCfgLogDeletedEntries_Type=Counter32
_HpnicfCfgLogDeletedEntries_Object=MibScalar
hpnicfCfgLogDeletedEntries=_HpnicfCfgLogDeletedEntries_Object((1,3,6,1,4,1,11,2,14,11,15,2,4,1,1,5),_HpnicfCfgLogDeletedEntries_Type())
hpnicfCfgLogDeletedEntries.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfCfgLogDeletedEntries.setStatus(_A)
class _HpnicfCfgLogWantBackup_Type(TruthValue):defaultValue=1
_HpnicfCfgLogWantBackup_Type.__name__=_J
_HpnicfCfgLogWantBackup_Object=MibScalar
hpnicfCfgLogWantBackup=_HpnicfCfgLogWantBackup_Object((1,3,6,1,4,1,11,2,14,11,15,2,4,1,1,6),_HpnicfCfgLogWantBackup_Type())
hpnicfCfgLogWantBackup.setMaxAccess(_G)
if mibBuilder.loadTexts:hpnicfCfgLogWantBackup.setStatus(_A)
_HpnicfCfgLogTable_Object=MibTable
hpnicfCfgLogTable=_HpnicfCfgLogTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,4,1,1,7))
if mibBuilder.loadTexts:hpnicfCfgLogTable.setStatus(_A)
_HpnicfCfgLogEntry_Object=MibTableRow
hpnicfCfgLogEntry=_HpnicfCfgLogEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,4,1,1,7,1))
hpnicfCfgLogEntry.setIndexNames((0,_B,_T))
if mibBuilder.loadTexts:hpnicfCfgLogEntry.setStatus(_A)
class _HpnicfCfgLogIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_HpnicfCfgLogIndex_Type.__name__=_D
_HpnicfCfgLogIndex_Object=MibTableColumn
hpnicfCfgLogIndex=_HpnicfCfgLogIndex_Object((1,3,6,1,4,1,11,2,14,11,15,2,4,1,1,7,1,1),_HpnicfCfgLogIndex_Type())
hpnicfCfgLogIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:hpnicfCfgLogIndex.setStatus(_A)
_HpnicfCfgLogTime_Type=TimeTicks
_HpnicfCfgLogTime_Object=MibTableColumn
hpnicfCfgLogTime=_HpnicfCfgLogTime_Object((1,3,6,1,4,1,11,2,14,11,15,2,4,1,1,7,1,2),_HpnicfCfgLogTime_Type())
hpnicfCfgLogTime.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfCfgLogTime.setStatus(_A)
class _HpnicfCfgLogSrcCmd_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('cmdLine',1),('snmp',2),('other',3)))
_HpnicfCfgLogSrcCmd_Type.__name__=_D
_HpnicfCfgLogSrcCmd_Object=MibTableColumn
hpnicfCfgLogSrcCmd=_HpnicfCfgLogSrcCmd_Object((1,3,6,1,4,1,11,2,14,11,15,2,4,1,1,7,1,3),_HpnicfCfgLogSrcCmd_Type())
hpnicfCfgLogSrcCmd.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfCfgLogSrcCmd.setStatus(_A)
class _HpnicfCfgLogSrcData_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*(('erase',1),(_U,2),(_V,3),(_W,4),('local',5),(_X,6),(_Y,7)))
_HpnicfCfgLogSrcData_Type.__name__=_D
_HpnicfCfgLogSrcData_Object=MibTableColumn
hpnicfCfgLogSrcData=_HpnicfCfgLogSrcData_Object((1,3,6,1,4,1,11,2,14,11,15,2,4,1,1,7,1,4),_HpnicfCfgLogSrcData_Type())
hpnicfCfgLogSrcData.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfCfgLogSrcData.setStatus(_A)
class _HpnicfCfgLogDesData_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*((_Z,1),(_U,2),(_V,3),(_W,4),('local',5),(_X,6),(_Y,7)))
_HpnicfCfgLogDesData_Type.__name__=_D
_HpnicfCfgLogDesData_Object=MibTableColumn
hpnicfCfgLogDesData=_HpnicfCfgLogDesData_Object((1,3,6,1,4,1,11,2,14,11,15,2,4,1,1,7,1,5),_HpnicfCfgLogDesData_Type())
hpnicfCfgLogDesData.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfCfgLogDesData.setStatus(_A)
class _HpnicfCfgLogTerminalType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*(('notApplicable',1),(_Z,2),('console',3),('terminal',4),('virtual',5),('auxiliary',6)))
_HpnicfCfgLogTerminalType_Type.__name__=_D
_HpnicfCfgLogTerminalType_Object=MibTableColumn
hpnicfCfgLogTerminalType=_HpnicfCfgLogTerminalType_Object((1,3,6,1,4,1,11,2,14,11,15,2,4,1,1,7,1,6),_HpnicfCfgLogTerminalType_Type())
hpnicfCfgLogTerminalType.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfCfgLogTerminalType.setStatus(_A)
class _HpnicfCfgLogTerminalUser_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_HpnicfCfgLogTerminalUser_Type.__name__=_F
_HpnicfCfgLogTerminalUser_Object=MibTableColumn
hpnicfCfgLogTerminalUser=_HpnicfCfgLogTerminalUser_Object((1,3,6,1,4,1,11,2,14,11,15,2,4,1,1,7,1,7),_HpnicfCfgLogTerminalUser_Type())
hpnicfCfgLogTerminalUser.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfCfgLogTerminalUser.setStatus(_A)
_HpnicfCfgLogTerminalNum_Type=Integer32
_HpnicfCfgLogTerminalNum_Object=MibTableColumn
hpnicfCfgLogTerminalNum=_HpnicfCfgLogTerminalNum_Object((1,3,6,1,4,1,11,2,14,11,15,2,4,1,1,7,1,8),_HpnicfCfgLogTerminalNum_Type())
hpnicfCfgLogTerminalNum.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfCfgLogTerminalNum.setStatus(_A)
class _HpnicfCfgLogTerminalLocation_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_HpnicfCfgLogTerminalLocation_Type.__name__=_F
_HpnicfCfgLogTerminalLocation_Object=MibTableColumn
hpnicfCfgLogTerminalLocation=_HpnicfCfgLogTerminalLocation_Object((1,3,6,1,4,1,11,2,14,11,15,2,4,1,1,7,1,9),_HpnicfCfgLogTerminalLocation_Type())
hpnicfCfgLogTerminalLocation.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfCfgLogTerminalLocation.setStatus(_A)
_HpnicfCfgLogCmdSrcAddress_Type=IpAddress
_HpnicfCfgLogCmdSrcAddress_Object=MibTableColumn
hpnicfCfgLogCmdSrcAddress=_HpnicfCfgLogCmdSrcAddress_Object((1,3,6,1,4,1,11,2,14,11,15,2,4,1,1,7,1,10),_HpnicfCfgLogCmdSrcAddress_Type())
hpnicfCfgLogCmdSrcAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfCfgLogCmdSrcAddress.setStatus(_K)
class _HpnicfCfgLogVirHost_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_HpnicfCfgLogVirHost_Type.__name__=_F
_HpnicfCfgLogVirHost_Object=MibTableColumn
hpnicfCfgLogVirHost=_HpnicfCfgLogVirHost_Object((1,3,6,1,4,1,11,2,14,11,15,2,4,1,1,7,1,11),_HpnicfCfgLogVirHost_Type())
hpnicfCfgLogVirHost.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfCfgLogVirHost.setStatus(_A)
class _HpnicfCfgLogUserName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_HpnicfCfgLogUserName_Type.__name__=_F
_HpnicfCfgLogUserName_Object=MibTableColumn
hpnicfCfgLogUserName=_HpnicfCfgLogUserName_Object((1,3,6,1,4,1,11,2,14,11,15,2,4,1,1,7,1,12),_HpnicfCfgLogUserName_Type())
hpnicfCfgLogUserName.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfCfgLogUserName.setStatus(_A)
_HpnicfCfgLogServerAddress_Type=IpAddress
_HpnicfCfgLogServerAddress_Object=MibTableColumn
hpnicfCfgLogServerAddress=_HpnicfCfgLogServerAddress_Object((1,3,6,1,4,1,11,2,14,11,15,2,4,1,1,7,1,13),_HpnicfCfgLogServerAddress_Type())
hpnicfCfgLogServerAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfCfgLogServerAddress.setStatus(_K)
class _HpnicfCfgLogFile_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_HpnicfCfgLogFile_Type.__name__=_F
_HpnicfCfgLogFile_Object=MibTableColumn
hpnicfCfgLogFile=_HpnicfCfgLogFile_Object((1,3,6,1,4,1,11,2,14,11,15,2,4,1,1,7,1,14),_HpnicfCfgLogFile_Type())
hpnicfCfgLogFile.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfCfgLogFile.setStatus(_A)
_HpnicfCfgLogCmdSrcAddrType_Type=InetAddressType
_HpnicfCfgLogCmdSrcAddrType_Object=MibTableColumn
hpnicfCfgLogCmdSrcAddrType=_HpnicfCfgLogCmdSrcAddrType_Object((1,3,6,1,4,1,11,2,14,11,15,2,4,1,1,7,1,15),_HpnicfCfgLogCmdSrcAddrType_Type())
hpnicfCfgLogCmdSrcAddrType.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfCfgLogCmdSrcAddrType.setStatus(_A)
_HpnicfCfgLogCmdSrcAddrRev_Type=InetAddress
_HpnicfCfgLogCmdSrcAddrRev_Object=MibTableColumn
hpnicfCfgLogCmdSrcAddrRev=_HpnicfCfgLogCmdSrcAddrRev_Object((1,3,6,1,4,1,11,2,14,11,15,2,4,1,1,7,1,16),_HpnicfCfgLogCmdSrcAddrRev_Type())
hpnicfCfgLogCmdSrcAddrRev.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfCfgLogCmdSrcAddrRev.setStatus(_A)
_HpnicfCfgLogCmdSrcAddrVPNName_Type=DisplayString
_HpnicfCfgLogCmdSrcAddrVPNName_Object=MibTableColumn
hpnicfCfgLogCmdSrcAddrVPNName=_HpnicfCfgLogCmdSrcAddrVPNName_Object((1,3,6,1,4,1,11,2,14,11,15,2,4,1,1,7,1,17),_HpnicfCfgLogCmdSrcAddrVPNName_Type())
hpnicfCfgLogCmdSrcAddrVPNName.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfCfgLogCmdSrcAddrVPNName.setStatus(_A)
_HpnicfCfgLogServerAddrType_Type=InetAddressType
_HpnicfCfgLogServerAddrType_Object=MibTableColumn
hpnicfCfgLogServerAddrType=_HpnicfCfgLogServerAddrType_Object((1,3,6,1,4,1,11,2,14,11,15,2,4,1,1,7,1,18),_HpnicfCfgLogServerAddrType_Type())
hpnicfCfgLogServerAddrType.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfCfgLogServerAddrType.setStatus(_A)
_HpnicfCfgLogServerAddrRev_Type=InetAddress
_HpnicfCfgLogServerAddrRev_Object=MibTableColumn
hpnicfCfgLogServerAddrRev=_HpnicfCfgLogServerAddrRev_Object((1,3,6,1,4,1,11,2,14,11,15,2,4,1,1,7,1,19),_HpnicfCfgLogServerAddrRev_Type())
hpnicfCfgLogServerAddrRev.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfCfgLogServerAddrRev.setStatus(_A)
_HpnicfCfgLogServerAddrVPNName_Type=DisplayString
_HpnicfCfgLogServerAddrVPNName_Object=MibTableColumn
hpnicfCfgLogServerAddrVPNName=_HpnicfCfgLogServerAddrVPNName_Object((1,3,6,1,4,1,11,2,14,11,15,2,4,1,1,7,1,20),_HpnicfCfgLogServerAddrVPNName_Type())
hpnicfCfgLogServerAddrVPNName.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfCfgLogServerAddrVPNName.setStatus(_A)
_HpnicfCfgFirstTrapTime_Type=TimeTicks
_HpnicfCfgFirstTrapTime_Object=MibScalar
hpnicfCfgFirstTrapTime=_HpnicfCfgFirstTrapTime_Object((1,3,6,1,4,1,11,2,14,11,15,2,4,1,1,8),_HpnicfCfgFirstTrapTime_Type())
hpnicfCfgFirstTrapTime.setMaxAccess('accessible-for-notify')
if mibBuilder.loadTexts:hpnicfCfgFirstTrapTime.setStatus(_A)
_HpnicfCfgOperate_ObjectIdentity=ObjectIdentity
hpnicfCfgOperate=_HpnicfCfgOperate_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,4,1,2))
class _HpnicfCfgOperateGlobalEntryLimit_Type(Integer32):defaultValue=5;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,10))
_HpnicfCfgOperateGlobalEntryLimit_Type.__name__=_D
_HpnicfCfgOperateGlobalEntryLimit_Object=MibScalar
hpnicfCfgOperateGlobalEntryLimit=_HpnicfCfgOperateGlobalEntryLimit_Object((1,3,6,1,4,1,11,2,14,11,15,2,4,1,2,1),_HpnicfCfgOperateGlobalEntryLimit_Type())
hpnicfCfgOperateGlobalEntryLimit.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfCfgOperateGlobalEntryLimit.setStatus(_A)
class _HpnicfCfgOperateEntryAgeOutTime_Type(Integer32):defaultValue=5;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,60))
_HpnicfCfgOperateEntryAgeOutTime_Type.__name__=_D
_HpnicfCfgOperateEntryAgeOutTime_Object=MibScalar
hpnicfCfgOperateEntryAgeOutTime=_HpnicfCfgOperateEntryAgeOutTime_Object((1,3,6,1,4,1,11,2,14,11,15,2,4,1,2,2),_HpnicfCfgOperateEntryAgeOutTime_Type())
hpnicfCfgOperateEntryAgeOutTime.setMaxAccess(_G)
if mibBuilder.loadTexts:hpnicfCfgOperateEntryAgeOutTime.setStatus(_A)
if mibBuilder.loadTexts:hpnicfCfgOperateEntryAgeOutTime.setUnits('minute')
class _HpnicfCfgOperateResultGlobalEntryLimit_Type(Integer32):defaultValue=5;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,50))
_HpnicfCfgOperateResultGlobalEntryLimit_Type.__name__=_D
_HpnicfCfgOperateResultGlobalEntryLimit_Object=MibScalar
hpnicfCfgOperateResultGlobalEntryLimit=_HpnicfCfgOperateResultGlobalEntryLimit_Object((1,3,6,1,4,1,11,2,14,11,15,2,4,1,2,3),_HpnicfCfgOperateResultGlobalEntryLimit_Type())
hpnicfCfgOperateResultGlobalEntryLimit.setMaxAccess(_G)
if mibBuilder.loadTexts:hpnicfCfgOperateResultGlobalEntryLimit.setStatus(_A)
_HpnicfCfgOperateTable_Object=MibTable
hpnicfCfgOperateTable=_HpnicfCfgOperateTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,4,1,2,4))
if mibBuilder.loadTexts:hpnicfCfgOperateTable.setStatus(_A)
_HpnicfCfgOperateEntry_Object=MibTableRow
hpnicfCfgOperateEntry=_HpnicfCfgOperateEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,4,1,2,4,1))
hpnicfCfgOperateEntry.setIndexNames((0,_B,_a))
if mibBuilder.loadTexts:hpnicfCfgOperateEntry.setStatus(_A)
class _HpnicfCfgOperateIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_HpnicfCfgOperateIndex_Type.__name__=_D
_HpnicfCfgOperateIndex_Object=MibTableColumn
hpnicfCfgOperateIndex=_HpnicfCfgOperateIndex_Object((1,3,6,1,4,1,11,2,14,11,15,2,4,1,2,4,1,1),_HpnicfCfgOperateIndex_Type())
hpnicfCfgOperateIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:hpnicfCfgOperateIndex.setStatus(_A)
_HpnicfCfgOperateType_Type=ConfigOperationType
_HpnicfCfgOperateType_Object=MibTableColumn
hpnicfCfgOperateType=_HpnicfCfgOperateType_Object((1,3,6,1,4,1,11,2,14,11,15,2,4,1,2,4,1,2),_HpnicfCfgOperateType_Type())
hpnicfCfgOperateType.setMaxAccess(_E)
if mibBuilder.loadTexts:hpnicfCfgOperateType.setStatus(_A)
class _HpnicfCfgOperateProtocol_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('ftp',1),('tftp',2),('clusterftp',3),('clustertftp',4)))
_HpnicfCfgOperateProtocol_Type.__name__=_D
_HpnicfCfgOperateProtocol_Object=MibTableColumn
hpnicfCfgOperateProtocol=_HpnicfCfgOperateProtocol_Object((1,3,6,1,4,1,11,2,14,11,15,2,4,1,2,4,1,3),_HpnicfCfgOperateProtocol_Type())
hpnicfCfgOperateProtocol.setMaxAccess(_E)
if mibBuilder.loadTexts:hpnicfCfgOperateProtocol.setStatus(_A)
class _HpnicfCfgOperateFileName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,128))
_HpnicfCfgOperateFileName_Type.__name__=_F
_HpnicfCfgOperateFileName_Object=MibTableColumn
hpnicfCfgOperateFileName=_HpnicfCfgOperateFileName_Object((1,3,6,1,4,1,11,2,14,11,15,2,4,1,2,4,1,4),_HpnicfCfgOperateFileName_Type())
hpnicfCfgOperateFileName.setMaxAccess(_E)
if mibBuilder.loadTexts:hpnicfCfgOperateFileName.setStatus(_A)
_HpnicfCfgOperateServerAddress_Type=IpAddress
_HpnicfCfgOperateServerAddress_Object=MibTableColumn
hpnicfCfgOperateServerAddress=_HpnicfCfgOperateServerAddress_Object((1,3,6,1,4,1,11,2,14,11,15,2,4,1,2,4,1,5),_HpnicfCfgOperateServerAddress_Type())
hpnicfCfgOperateServerAddress.setMaxAccess(_E)
if mibBuilder.loadTexts:hpnicfCfgOperateServerAddress.setStatus(_K)
class _HpnicfCfgOperateUserName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,40))
_HpnicfCfgOperateUserName_Type.__name__=_F
_HpnicfCfgOperateUserName_Object=MibTableColumn
hpnicfCfgOperateUserName=_HpnicfCfgOperateUserName_Object((1,3,6,1,4,1,11,2,14,11,15,2,4,1,2,4,1,6),_HpnicfCfgOperateUserName_Type())
hpnicfCfgOperateUserName.setMaxAccess(_E)
if mibBuilder.loadTexts:hpnicfCfgOperateUserName.setStatus(_A)
class _HpnicfCfgOperateUserPassword_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,40))
_HpnicfCfgOperateUserPassword_Type.__name__=_F
_HpnicfCfgOperateUserPassword_Object=MibTableColumn
hpnicfCfgOperateUserPassword=_HpnicfCfgOperateUserPassword_Object((1,3,6,1,4,1,11,2,14,11,15,2,4,1,2,4,1,7),_HpnicfCfgOperateUserPassword_Type())
hpnicfCfgOperateUserPassword.setMaxAccess(_E)
if mibBuilder.loadTexts:hpnicfCfgOperateUserPassword.setStatus(_A)
class _HpnicfCfgOperateEndNotificationSwitch_Type(TruthValue):defaultValue=2
_HpnicfCfgOperateEndNotificationSwitch_Type.__name__=_J
_HpnicfCfgOperateEndNotificationSwitch_Object=MibTableColumn
hpnicfCfgOperateEndNotificationSwitch=_HpnicfCfgOperateEndNotificationSwitch_Object((1,3,6,1,4,1,11,2,14,11,15,2,4,1,2,4,1,8),_HpnicfCfgOperateEndNotificationSwitch_Type())
hpnicfCfgOperateEndNotificationSwitch.setMaxAccess(_E)
if mibBuilder.loadTexts:hpnicfCfgOperateEndNotificationSwitch.setStatus(_A)
_HpnicfCfgOperateRowStatus_Type=RowStatus
_HpnicfCfgOperateRowStatus_Object=MibTableColumn
hpnicfCfgOperateRowStatus=_HpnicfCfgOperateRowStatus_Object((1,3,6,1,4,1,11,2,14,11,15,2,4,1,2,4,1,9),_HpnicfCfgOperateRowStatus_Type())
hpnicfCfgOperateRowStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:hpnicfCfgOperateRowStatus.setStatus(_A)
class _HpnicfCfgOperateServerPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_HpnicfCfgOperateServerPort_Type.__name__=_D
_HpnicfCfgOperateServerPort_Object=MibTableColumn
hpnicfCfgOperateServerPort=_HpnicfCfgOperateServerPort_Object((1,3,6,1,4,1,11,2,14,11,15,2,4,1,2,4,1,10),_HpnicfCfgOperateServerPort_Type())
hpnicfCfgOperateServerPort.setMaxAccess(_E)
if mibBuilder.loadTexts:hpnicfCfgOperateServerPort.setStatus(_A)
_HpnicfCfgOperateSrvAddrType_Type=InetAddressType
_HpnicfCfgOperateSrvAddrType_Object=MibTableColumn
hpnicfCfgOperateSrvAddrType=_HpnicfCfgOperateSrvAddrType_Object((1,3,6,1,4,1,11,2,14,11,15,2,4,1,2,4,1,11),_HpnicfCfgOperateSrvAddrType_Type())
hpnicfCfgOperateSrvAddrType.setMaxAccess(_E)
if mibBuilder.loadTexts:hpnicfCfgOperateSrvAddrType.setStatus(_A)
_HpnicfCfgOperateSrvAddrRev_Type=InetAddress
_HpnicfCfgOperateSrvAddrRev_Object=MibTableColumn
hpnicfCfgOperateSrvAddrRev=_HpnicfCfgOperateSrvAddrRev_Object((1,3,6,1,4,1,11,2,14,11,15,2,4,1,2,4,1,12),_HpnicfCfgOperateSrvAddrRev_Type())
hpnicfCfgOperateSrvAddrRev.setMaxAccess(_E)
if mibBuilder.loadTexts:hpnicfCfgOperateSrvAddrRev.setStatus(_A)
_HpnicfCfgOperateSrvVPNName_Type=DisplayString
_HpnicfCfgOperateSrvVPNName_Object=MibTableColumn
hpnicfCfgOperateSrvVPNName=_HpnicfCfgOperateSrvVPNName_Object((1,3,6,1,4,1,11,2,14,11,15,2,4,1,2,4,1,13),_HpnicfCfgOperateSrvVPNName_Type())
hpnicfCfgOperateSrvVPNName.setMaxAccess(_E)
if mibBuilder.loadTexts:hpnicfCfgOperateSrvVPNName.setStatus(_A)
_HpnicfCfgOperateResultTable_Object=MibTable
hpnicfCfgOperateResultTable=_HpnicfCfgOperateResultTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,4,1,2,5))
if mibBuilder.loadTexts:hpnicfCfgOperateResultTable.setStatus(_A)
_HpnicfCfgOperateResultEntry_Object=MibTableRow
hpnicfCfgOperateResultEntry=_HpnicfCfgOperateResultEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,4,1,2,5,1))
hpnicfCfgOperateResultEntry.setIndexNames((0,_B,_b))
if mibBuilder.loadTexts:hpnicfCfgOperateResultEntry.setStatus(_A)
class _HpnicfCfgOperateResultIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_HpnicfCfgOperateResultIndex_Type.__name__=_D
_HpnicfCfgOperateResultIndex_Object=MibTableColumn
hpnicfCfgOperateResultIndex=_HpnicfCfgOperateResultIndex_Object((1,3,6,1,4,1,11,2,14,11,15,2,4,1,2,5,1,1),_HpnicfCfgOperateResultIndex_Type())
hpnicfCfgOperateResultIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:hpnicfCfgOperateResultIndex.setStatus(_A)
class _HpnicfCfgOperateResultOptIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_HpnicfCfgOperateResultOptIndex_Type.__name__=_D
_HpnicfCfgOperateResultOptIndex_Object=MibTableColumn
hpnicfCfgOperateResultOptIndex=_HpnicfCfgOperateResultOptIndex_Object((1,3,6,1,4,1,11,2,14,11,15,2,4,1,2,5,1,2),_HpnicfCfgOperateResultOptIndex_Type())
hpnicfCfgOperateResultOptIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfCfgOperateResultOptIndex.setStatus(_A)
_HpnicfCfgOperateResultOpType_Type=ConfigOperationType
_HpnicfCfgOperateResultOpType_Object=MibTableColumn
hpnicfCfgOperateResultOpType=_HpnicfCfgOperateResultOpType_Object((1,3,6,1,4,1,11,2,14,11,15,2,4,1,2,5,1,3),_HpnicfCfgOperateResultOpType_Type())
hpnicfCfgOperateResultOpType.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfCfgOperateResultOpType.setStatus(_A)
_HpnicfCfgOperateState_Type=ConfigOperationStateType
_HpnicfCfgOperateState_Object=MibTableColumn
hpnicfCfgOperateState=_HpnicfCfgOperateState_Object((1,3,6,1,4,1,11,2,14,11,15,2,4,1,2,5,1,4),_HpnicfCfgOperateState_Type())
hpnicfCfgOperateState.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfCfgOperateState.setStatus(_A)
_HpnicfCfgOperateTime_Type=TimeTicks
_HpnicfCfgOperateTime_Object=MibTableColumn
hpnicfCfgOperateTime=_HpnicfCfgOperateTime_Object((1,3,6,1,4,1,11,2,14,11,15,2,4,1,2,5,1,5),_HpnicfCfgOperateTime_Type())
hpnicfCfgOperateTime.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfCfgOperateTime.setStatus(_A)
_HpnicfCfgOperateEndTime_Type=TimeTicks
_HpnicfCfgOperateEndTime_Object=MibTableColumn
hpnicfCfgOperateEndTime=_HpnicfCfgOperateEndTime_Object((1,3,6,1,4,1,11,2,14,11,15,2,4,1,2,5,1,6),_HpnicfCfgOperateEndTime_Type())
hpnicfCfgOperateEndTime.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfCfgOperateEndTime.setStatus(_A)
_HpnicfCfgOperFailReason_Type=DisplayString
_HpnicfCfgOperFailReason_Object=MibTableColumn
hpnicfCfgOperFailReason=_HpnicfCfgOperFailReason_Object((1,3,6,1,4,1,11,2,14,11,15,2,4,1,2,5,1,7),_HpnicfCfgOperFailReason_Type())
hpnicfCfgOperFailReason.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfCfgOperFailReason.setStatus(_A)
_HpnicfCfgExecuteOperate_ObjectIdentity=ObjectIdentity
hpnicfCfgExecuteOperate=_HpnicfCfgExecuteOperate_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,4,1,2,6))
class _HpnicfCfgExecuteOperateResultEntryLimit_Type(Integer32):defaultValue=5;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(5,20))
_HpnicfCfgExecuteOperateResultEntryLimit_Type.__name__=_D
_HpnicfCfgExecuteOperateResultEntryLimit_Object=MibScalar
hpnicfCfgExecuteOperateResultEntryLimit=_HpnicfCfgExecuteOperateResultEntryLimit_Object((1,3,6,1,4,1,11,2,14,11,15,2,4,1,2,6,1),_HpnicfCfgExecuteOperateResultEntryLimit_Type())
hpnicfCfgExecuteOperateResultEntryLimit.setMaxAccess(_G)
if mibBuilder.loadTexts:hpnicfCfgExecuteOperateResultEntryLimit.setStatus(_A)
_HpnicfCfgExecuteResultTable_Object=MibTable
hpnicfCfgExecuteResultTable=_HpnicfCfgExecuteResultTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,4,1,2,6,2))
if mibBuilder.loadTexts:hpnicfCfgExecuteResultTable.setStatus(_A)
_HpnicfCfgExecuteResultEntry_Object=MibTableRow
hpnicfCfgExecuteResultEntry=_HpnicfCfgExecuteResultEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,4,1,2,6,2,1))
hpnicfCfgExecuteResultEntry.setIndexNames((0,_B,_c))
if mibBuilder.loadTexts:hpnicfCfgExecuteResultEntry.setStatus(_A)
class _HpnicfCfgExecuteResultIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_HpnicfCfgExecuteResultIndex_Type.__name__=_D
_HpnicfCfgExecuteResultIndex_Object=MibTableColumn
hpnicfCfgExecuteResultIndex=_HpnicfCfgExecuteResultIndex_Object((1,3,6,1,4,1,11,2,14,11,15,2,4,1,2,6,2,1,1),_HpnicfCfgExecuteResultIndex_Type())
hpnicfCfgExecuteResultIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:hpnicfCfgExecuteResultIndex.setStatus(_A)
class _HpnicfCfgExecuteResultOptIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_HpnicfCfgExecuteResultOptIndex_Type.__name__=_D
_HpnicfCfgExecuteResultOptIndex_Object=MibTableColumn
hpnicfCfgExecuteResultOptIndex=_HpnicfCfgExecuteResultOptIndex_Object((1,3,6,1,4,1,11,2,14,11,15,2,4,1,2,6,2,1,2),_HpnicfCfgExecuteResultOptIndex_Type())
hpnicfCfgExecuteResultOptIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfCfgExecuteResultOptIndex.setStatus(_A)
_HpnicfCfgExecuteResultOpType_Type=ConfigOperationType
_HpnicfCfgExecuteResultOpType_Object=MibTableColumn
hpnicfCfgExecuteResultOpType=_HpnicfCfgExecuteResultOpType_Object((1,3,6,1,4,1,11,2,14,11,15,2,4,1,2,6,2,1,3),_HpnicfCfgExecuteResultOpType_Type())
hpnicfCfgExecuteResultOpType.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfCfgExecuteResultOpType.setStatus(_A)
_HpnicfCfgExecuteState_Type=ConfigOperationStateType
_HpnicfCfgExecuteState_Object=MibTableColumn
hpnicfCfgExecuteState=_HpnicfCfgExecuteState_Object((1,3,6,1,4,1,11,2,14,11,15,2,4,1,2,6,2,1,4),_HpnicfCfgExecuteState_Type())
hpnicfCfgExecuteState.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfCfgExecuteState.setStatus(_A)
_HpnicfCfgExecuteTime_Type=TimeTicks
_HpnicfCfgExecuteTime_Object=MibTableColumn
hpnicfCfgExecuteTime=_HpnicfCfgExecuteTime_Object((1,3,6,1,4,1,11,2,14,11,15,2,4,1,2,6,2,1,5),_HpnicfCfgExecuteTime_Type())
hpnicfCfgExecuteTime.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfCfgExecuteTime.setStatus(_A)
_HpnicfCfgExecuteEndTime_Type=TimeTicks
_HpnicfCfgExecuteEndTime_Object=MibTableColumn
hpnicfCfgExecuteEndTime=_HpnicfCfgExecuteEndTime_Object((1,3,6,1,4,1,11,2,14,11,15,2,4,1,2,6,2,1,6),_HpnicfCfgExecuteEndTime_Type())
hpnicfCfgExecuteEndTime.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfCfgExecuteEndTime.setStatus(_A)
class _HpnicfCfgReset_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_d,1),('reset',2)))
_HpnicfCfgReset_Type.__name__=_D
_HpnicfCfgReset_Object=MibScalar
hpnicfCfgReset=_HpnicfCfgReset_Object((1,3,6,1,4,1,11,2,14,11,15,2,4,1,2,7),_HpnicfCfgReset_Type())
hpnicfCfgReset.setMaxAccess(_G)
if mibBuilder.loadTexts:hpnicfCfgReset.setStatus(_A)
class _HpnicfCfgReset2_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_d,0),('reset',1)))
_HpnicfCfgReset2_Type.__name__=_D
_HpnicfCfgReset2_Object=MibScalar
hpnicfCfgReset2=_HpnicfCfgReset2_Object((1,3,6,1,4,1,11,2,14,11,15,2,4,1,2,8),_HpnicfCfgReset2_Type())
hpnicfCfgReset2.setMaxAccess(_G)
if mibBuilder.loadTexts:hpnicfCfgReset2.setStatus(_A)
_HpnicfConfigManNotifications_ObjectIdentity=ObjectIdentity
hpnicfConfigManNotifications=_HpnicfConfigManNotifications_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,4,2))
_HpnicfConfigManConformance_ObjectIdentity=ObjectIdentity
hpnicfConfigManConformance=_HpnicfConfigManConformance_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,4,3))
_HpnicfConfigManCompliances_ObjectIdentity=ObjectIdentity
hpnicfConfigManCompliances=_HpnicfConfigManCompliances_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,4,3,1))
_HpnicfConfigManGroups_ObjectIdentity=ObjectIdentity
hpnicfConfigManGroups=_HpnicfConfigManGroups_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,4,3,2))
hpnicfCfgManLogGroup=ObjectGroup((1,3,6,1,4,1,11,2,14,11,15,2,4,3,2,1))
hpnicfCfgManLogGroup.setObjects(*((_B,_e),(_B,_f),(_B,_g),(_B,_h),(_B,_i),(_B,_j),(_B,_L),(_B,_k),(_B,_l),(_B,_m),(_B,_n),(_B,_o),(_B,_p),(_B,_q),(_B,_r),(_B,_s),(_B,_t),(_B,_M),(_B,_N)))
if mibBuilder.loadTexts:hpnicfCfgManLogGroup.setStatus(_A)
hpnicfCfgOperateGroup=ObjectGroup((1,3,6,1,4,1,11,2,14,11,15,2,4,3,2,2))
hpnicfCfgOperateGroup.setObjects(*((_B,_u),(_B,_v),(_B,_I),(_B,_w),(_B,_O),(_B,_x),(_B,_y),(_B,_z),(_B,_P),(_B,_A0),(_B,_A1),(_B,_Q),(_B,_A2),(_B,_A3),(_B,_A4),(_B,_R),(_B,_S),(_B,_A5)))
if mibBuilder.loadTexts:hpnicfCfgOperateGroup.setStatus(_A)
hpnicfCfgManEventlog=NotificationType((1,3,6,1,4,1,11,2,14,11,15,2,4,2,1))
hpnicfCfgManEventlog.setObjects(*((_B,_L),(_B,_M),(_B,_N)))
if mibBuilder.loadTexts:hpnicfCfgManEventlog.setStatus(_A)
hpnicfCfgOperateCompletion=NotificationType((1,3,6,1,4,1,11,2,14,11,15,2,4,2,2))
hpnicfCfgOperateCompletion.setObjects(*((_B,_I),(_B,_P),(_B,_Q),(_B,_R),(_B,_S)))
if mibBuilder.loadTexts:hpnicfCfgOperateCompletion.setStatus(_A)
hpnicfCfgInvalidConfigFile=NotificationType((1,3,6,1,4,1,11,2,14,11,15,2,4,2,3))
hpnicfCfgInvalidConfigFile.setObjects(*((_B,_I),(_B,_O),(_B,_A6)))
if mibBuilder.loadTexts:hpnicfCfgInvalidConfigFile.setStatus(_A)
hpnicfCfgManNotificationGroup=NotificationGroup((1,3,6,1,4,1,11,2,14,11,15,2,4,3,2,3))
hpnicfCfgManNotificationGroup.setObjects(*((_B,_A7),(_B,_A8),(_B,_A9)))
if mibBuilder.loadTexts:hpnicfCfgManNotificationGroup.setStatus(_A)
hpnicfConfigManCompliance=ModuleCompliance((1,3,6,1,4,1,11,2,14,11,15,2,4,3,1,1))
hpnicfConfigManCompliance.setObjects(*((_B,_AA),(_B,_AB),(_B,_AC)))
if mibBuilder.loadTexts:hpnicfConfigManCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'ConfigOperationType':ConfigOperationType,'ConfigOperationStateType':ConfigOperationStateType,'hpnicfConfig':hpnicfConfig,'hpnicfConfigManObjects':hpnicfConfigManObjects,'hpnicfCfgLog':hpnicfCfgLog,_e:hpnicfCfgRunModifiedLast,_f:hpnicfCfgRunSavedLast,_g:hpnicfCfgStartModifiedLast,_h:hpnicfCfgLogLimitedEntries,_i:hpnicfCfgLogDeletedEntries,_t:hpnicfCfgLogWantBackup,'hpnicfCfgLogTable':hpnicfCfgLogTable,'hpnicfCfgLogEntry':hpnicfCfgLogEntry,_T:hpnicfCfgLogIndex,_j:hpnicfCfgLogTime,_L:hpnicfCfgLogSrcCmd,_M:hpnicfCfgLogSrcData,_N:hpnicfCfgLogDesData,_k:hpnicfCfgLogTerminalType,_m:hpnicfCfgLogTerminalUser,_l:hpnicfCfgLogTerminalNum,_n:hpnicfCfgLogTerminalLocation,_o:hpnicfCfgLogCmdSrcAddress,_p:hpnicfCfgLogVirHost,_s:hpnicfCfgLogUserName,_q:hpnicfCfgLogServerAddress,_r:hpnicfCfgLogFile,'hpnicfCfgLogCmdSrcAddrType':hpnicfCfgLogCmdSrcAddrType,'hpnicfCfgLogCmdSrcAddrRev':hpnicfCfgLogCmdSrcAddrRev,'hpnicfCfgLogCmdSrcAddrVPNName':hpnicfCfgLogCmdSrcAddrVPNName,'hpnicfCfgLogServerAddrType':hpnicfCfgLogServerAddrType,'hpnicfCfgLogServerAddrRev':hpnicfCfgLogServerAddrRev,'hpnicfCfgLogServerAddrVPNName':hpnicfCfgLogServerAddrVPNName,_A6:hpnicfCfgFirstTrapTime,'hpnicfCfgOperate':hpnicfCfgOperate,_u:hpnicfCfgOperateGlobalEntryLimit,_v:hpnicfCfgOperateEntryAgeOutTime,_A1:hpnicfCfgOperateResultGlobalEntryLimit,'hpnicfCfgOperateTable':hpnicfCfgOperateTable,'hpnicfCfgOperateEntry':hpnicfCfgOperateEntry,_a:hpnicfCfgOperateIndex,_I:hpnicfCfgOperateType,_w:hpnicfCfgOperateProtocol,_O:hpnicfCfgOperateFileName,_x:hpnicfCfgOperateServerAddress,_y:hpnicfCfgOperateUserName,_z:hpnicfCfgOperateUserPassword,_A0:hpnicfCfgOperateEndNotificationSwitch,_A2:hpnicfCfgOperateRowStatus,_A5:hpnicfCfgOperateServerPort,'hpnicfCfgOperateSrvAddrType':hpnicfCfgOperateSrvAddrType,'hpnicfCfgOperateSrvAddrRev':hpnicfCfgOperateSrvAddrRev,'hpnicfCfgOperateSrvVPNName':hpnicfCfgOperateSrvVPNName,'hpnicfCfgOperateResultTable':hpnicfCfgOperateResultTable,'hpnicfCfgOperateResultEntry':hpnicfCfgOperateResultEntry,_b:hpnicfCfgOperateResultIndex,_A3:hpnicfCfgOperateResultOptIndex,_A4:hpnicfCfgOperateResultOpType,_Q:hpnicfCfgOperateState,_P:hpnicfCfgOperateTime,_R:hpnicfCfgOperateEndTime,_S:hpnicfCfgOperFailReason,'hpnicfCfgExecuteOperate':hpnicfCfgExecuteOperate,'hpnicfCfgExecuteOperateResultEntryLimit':hpnicfCfgExecuteOperateResultEntryLimit,'hpnicfCfgExecuteResultTable':hpnicfCfgExecuteResultTable,'hpnicfCfgExecuteResultEntry':hpnicfCfgExecuteResultEntry,_c:hpnicfCfgExecuteResultIndex,'hpnicfCfgExecuteResultOptIndex':hpnicfCfgExecuteResultOptIndex,'hpnicfCfgExecuteResultOpType':hpnicfCfgExecuteResultOpType,'hpnicfCfgExecuteState':hpnicfCfgExecuteState,'hpnicfCfgExecuteTime':hpnicfCfgExecuteTime,'hpnicfCfgExecuteEndTime':hpnicfCfgExecuteEndTime,'hpnicfCfgReset':hpnicfCfgReset,'hpnicfCfgReset2':hpnicfCfgReset2,'hpnicfConfigManNotifications':hpnicfConfigManNotifications,_A7:hpnicfCfgManEventlog,_A8:hpnicfCfgOperateCompletion,_A9:hpnicfCfgInvalidConfigFile,'hpnicfConfigManConformance':hpnicfConfigManConformance,'hpnicfConfigManCompliances':hpnicfConfigManCompliances,'hpnicfConfigManCompliance':hpnicfConfigManCompliance,'hpnicfConfigManGroups':hpnicfConfigManGroups,_AA:hpnicfCfgManLogGroup,_AB:hpnicfCfgOperateGroup,_AC:hpnicfCfgManNotificationGroup})