_e='raisecomLogHistTimestamp'
_d='raisecomLogHistMsgbody'
_c='raisecomLogHistMnemonics'
_b='raisecomLogHistSeverity'
_a='raisecomLogHistFacility'
_Z='raisecomDebugIndex'
_Y='raisecomLogServerIpAddress'
_X='raisecomLogHistIndex'
_W='raisecomLogDiscriminatorIndex'
_V='raisecomLogDestIndex'
_U='SyslogSeverity'
_T='up-timestamp'
_S='date-timestamp'
_R='no-timestamp'
_Q='deprecated'
_P='MibTableColumn'
_O='MibTableRow'
_N='MibTable'
_M='MibScalar'
_L='ModuleIdentity'
_K='includes'
_J='drops'
_I='read-create'
_H='none'
_G='not-accessible'
_F='OctetString'
_E='RAISECOM-SYSLOG-SERVICE-MIB'
_D='read-only'
_C='Integer32'
_B='read-write'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_F,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
InetAddress,ModuleIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress',_L,_M,_N,_O,_P)
raisecomAgent,=mibBuilder.importSymbols('RAISECOM-BASE-MIB','raisecomAgent')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress',_L,'MibIdentifier','NotificationType','ObjectIdentity',_M,_N,_O,_P,'TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention','TruthValue')
EnableVar,=mibBuilder.importSymbols('SWITCH-TC','EnableVar')
raisecomSyslogService=ModuleIdentity((1,3,6,1,4,1,8886,1,4))
class SyslogSeverity(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8)));namedValues=NamedValues(*(('emergency',1),('alert',2),('critical',3),('error',4),('warning',5),('notice',6),('info',7),('debug',8)))
class LogFacility(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24)));namedValues=NamedValues(*(('kern',1),('user',2),('mail',3),('daemon',4),('auth',5),('syslog',6),('lpr',7),('news',8),('uucp',9),('cron',10),('security',11),('ftp',12),('ntp',13),('audit',14),('alert',15),('clock',16),('local0',17),('local1',18),('local2',19),('local3',20),('local4',21),('local5',22),('local6',23),('local7',24)))
_RaisecomSyslogMibObjects_ObjectIdentity=ObjectIdentity
raisecomSyslogMibObjects=_RaisecomSyslogMibObjects_ObjectIdentity((1,3,6,1,4,1,8886,1,4,1))
_RaisecomLogBasic_ObjectIdentity=ObjectIdentity
raisecomLogBasic=_RaisecomLogBasic_ObjectIdentity((1,3,6,1,4,1,8886,1,4,1,1))
_RaisecomLogEnable_Type=EnableVar
_RaisecomLogEnable_Object=MibScalar
raisecomLogEnable=_RaisecomLogEnable_Object((1,3,6,1,4,1,8886,1,4,1,1,1),_RaisecomLogEnable_Type())
raisecomLogEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomLogEnable.setStatus(_A)
class _RaisecomLogRateLimit_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,10000))
_RaisecomLogRateLimit_Type.__name__=_C
_RaisecomLogRateLimit_Object=MibScalar
raisecomLogRateLimit=_RaisecomLogRateLimit_Object((1,3,6,1,4,1,8886,1,4,1,1,2),_RaisecomLogRateLimit_Type())
raisecomLogRateLimit.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomLogRateLimit.setStatus(_A)
class _RaisecomLogDropMessages_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_RaisecomLogDropMessages_Type.__name__=_C
_RaisecomLogDropMessages_Object=MibScalar
raisecomLogDropMessages=_RaisecomLogDropMessages_Object((1,3,6,1,4,1,8886,1,4,1,1,3),_RaisecomLogDropMessages_Type())
raisecomLogDropMessages.setMaxAccess(_D)
if mibBuilder.loadTexts:raisecomLogDropMessages.setStatus(_A)
class _RaisecomLogConsoleLogedMessages_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_RaisecomLogConsoleLogedMessages_Type.__name__=_C
_RaisecomLogConsoleLogedMessages_Object=MibScalar
raisecomLogConsoleLogedMessages=_RaisecomLogConsoleLogedMessages_Object((1,3,6,1,4,1,8886,1,4,1,1,4),_RaisecomLogConsoleLogedMessages_Type())
raisecomLogConsoleLogedMessages.setMaxAccess(_D)
if mibBuilder.loadTexts:raisecomLogConsoleLogedMessages.setStatus(_Q)
class _RaisecomLogMonitorMessages_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_RaisecomLogMonitorMessages_Type.__name__=_C
_RaisecomLogMonitorMessages_Object=MibScalar
raisecomLogMonitorMessages=_RaisecomLogMonitorMessages_Object((1,3,6,1,4,1,8886,1,4,1,1,5),_RaisecomLogMonitorMessages_Type())
raisecomLogMonitorMessages.setMaxAccess(_D)
if mibBuilder.loadTexts:raisecomLogMonitorMessages.setStatus(_Q)
class _RaisecomLogTimeStamp_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_R,1),(_S,2),(_T,3)))
_RaisecomLogTimeStamp_Type.__name__=_C
_RaisecomLogTimeStamp_Object=MibScalar
raisecomLogTimeStamp=_RaisecomLogTimeStamp_Object((1,3,6,1,4,1,8886,1,4,1,1,6),_RaisecomLogTimeStamp_Type())
raisecomLogTimeStamp.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomLogTimeStamp.setStatus(_A)
class _RaisecomLogDebugTimeStamp_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_R,1),(_S,2),(_T,3)))
_RaisecomLogDebugTimeStamp_Type.__name__=_C
_RaisecomLogDebugTimeStamp_Object=MibScalar
raisecomLogDebugTimeStamp=_RaisecomLogDebugTimeStamp_Object((1,3,6,1,4,1,8886,1,4,1,1,7),_RaisecomLogDebugTimeStamp_Type())
raisecomLogDebugTimeStamp.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomLogDebugTimeStamp.setStatus(_A)
_RaisecomLogHistoryEnable_Type=EnableVar
_RaisecomLogHistoryEnable_Object=MibScalar
raisecomLogHistoryEnable=_RaisecomLogHistoryEnable_Object((1,3,6,1,4,1,8886,1,4,1,1,8),_RaisecomLogHistoryEnable_Type())
raisecomLogHistoryEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomLogHistoryEnable.setStatus(_A)
class _RaisecomLogHistorySize_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,500))
_RaisecomLogHistorySize_Type.__name__=_C
_RaisecomLogHistorySize_Object=MibScalar
raisecomLogHistorySize=_RaisecomLogHistorySize_Object((1,3,6,1,4,1,8886,1,4,1,1,9),_RaisecomLogHistorySize_Type())
raisecomLogHistorySize.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomLogHistorySize.setStatus(_A)
class _RaisecomLogBufferSize_Type(Integer32):defaultValue=4;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(4,256))
_RaisecomLogBufferSize_Type.__name__=_C
_RaisecomLogBufferSize_Object=MibScalar
raisecomLogBufferSize=_RaisecomLogBufferSize_Object((1,3,6,1,4,1,8886,1,4,1,1,10),_RaisecomLogBufferSize_Type())
raisecomLogBufferSize.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomLogBufferSize.setStatus(_A)
_RaisecomLogSequenceNumEnable_Type=EnableVar
_RaisecomLogSequenceNumEnable_Object=MibScalar
raisecomLogSequenceNumEnable=_RaisecomLogSequenceNumEnable_Object((1,3,6,1,4,1,8886,1,4,1,1,11),_RaisecomLogSequenceNumEnable_Type())
raisecomLogSequenceNumEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomLogSequenceNumEnable.setStatus(_A)
class _RaisecomDebugModuleLevel_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_H,1),('high',2),('normal',3),('low',4)))
_RaisecomDebugModuleLevel_Type.__name__=_C
_RaisecomDebugModuleLevel_Object=MibScalar
raisecomDebugModuleLevel=_RaisecomDebugModuleLevel_Object((1,3,6,1,4,1,8886,1,4,1,1,12),_RaisecomDebugModuleLevel_Type())
raisecomDebugModuleLevel.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomDebugModuleLevel.setStatus(_A)
class _RaisecomLogDebugDropMessages_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_RaisecomLogDebugDropMessages_Type.__name__=_C
_RaisecomLogDebugDropMessages_Object=MibScalar
raisecomLogDebugDropMessages=_RaisecomLogDebugDropMessages_Object((1,3,6,1,4,1,8886,1,4,1,1,13),_RaisecomLogDebugDropMessages_Type())
raisecomLogDebugDropMessages.setMaxAccess(_D)
if mibBuilder.loadTexts:raisecomLogDebugDropMessages.setStatus(_A)
_RaisecomLogBufferClear_Type=TruthValue
_RaisecomLogBufferClear_Object=MibScalar
raisecomLogBufferClear=_RaisecomLogBufferClear_Object((1,3,6,1,4,1,8886,1,4,1,1,14),_RaisecomLogBufferClear_Type())
raisecomLogBufferClear.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomLogBufferClear.setStatus(_A)
_RaisecomLogConfig_Type=EnableVar
_RaisecomLogConfig_Object=MibScalar
raisecomLogConfig=_RaisecomLogConfig_Object((1,3,6,1,4,1,8886,1,4,1,1,15),_RaisecomLogConfig_Type())
raisecomLogConfig.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomLogConfig.setStatus(_A)
class _RaisecomLogConfigLevel_Type(SyslogSeverity):defaultValue=7
_RaisecomLogConfigLevel_Type.__name__=_U
_RaisecomLogConfigLevel_Object=MibScalar
raisecomLogConfigLevel=_RaisecomLogConfigLevel_Object((1,3,6,1,4,1,8886,1,4,1,1,16),_RaisecomLogConfigLevel_Type())
raisecomLogConfigLevel.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomLogConfigLevel.setStatus(_A)
_RaisecomLogDestinationTable_Object=MibTable
raisecomLogDestinationTable=_RaisecomLogDestinationTable_Object((1,3,6,1,4,1,8886,1,4,1,1,17))
if mibBuilder.loadTexts:raisecomLogDestinationTable.setStatus(_A)
_RaisecomLogDestinationEntry_Object=MibTableRow
raisecomLogDestinationEntry=_RaisecomLogDestinationEntry_Object((1,3,6,1,4,1,8886,1,4,1,1,17,1))
raisecomLogDestinationEntry.setIndexNames((0,_E,_V))
if mibBuilder.loadTexts:raisecomLogDestinationEntry.setStatus(_A)
class _RaisecomLogDestIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('buffer',1),('console',2),('trap',3),('file',4)))
_RaisecomLogDestIndex_Type.__name__=_C
_RaisecomLogDestIndex_Object=MibTableColumn
raisecomLogDestIndex=_RaisecomLogDestIndex_Object((1,3,6,1,4,1,8886,1,4,1,1,17,1,1),_RaisecomLogDestIndex_Type())
raisecomLogDestIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:raisecomLogDestIndex.setStatus(_A)
_RaisecomLogDestEnable_Type=EnableVar
_RaisecomLogDestEnable_Object=MibTableColumn
raisecomLogDestEnable=_RaisecomLogDestEnable_Object((1,3,6,1,4,1,8886,1,4,1,1,17,1,2),_RaisecomLogDestEnable_Type())
raisecomLogDestEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomLogDestEnable.setStatus(_A)
_RaisecomLogDestServrity_Type=SyslogSeverity
_RaisecomLogDestServrity_Object=MibTableColumn
raisecomLogDestServrity=_RaisecomLogDestServrity_Object((1,3,6,1,4,1,8886,1,4,1,1,17,1,3),_RaisecomLogDestServrity_Type())
raisecomLogDestServrity.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomLogDestServrity.setStatus(_A)
class _RaisecomLogDestDiscriminator_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,5))
_RaisecomLogDestDiscriminator_Type.__name__=_C
_RaisecomLogDestDiscriminator_Object=MibTableColumn
raisecomLogDestDiscriminator=_RaisecomLogDestDiscriminator_Object((1,3,6,1,4,1,8886,1,4,1,1,17,1,4),_RaisecomLogDestDiscriminator_Type())
raisecomLogDestDiscriminator.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomLogDestDiscriminator.setStatus(_A)
_RaisecomLogDestLoggedMessages_Type=Integer32
_RaisecomLogDestLoggedMessages_Object=MibTableColumn
raisecomLogDestLoggedMessages=_RaisecomLogDestLoggedMessages_Object((1,3,6,1,4,1,8886,1,4,1,1,17,1,5),_RaisecomLogDestLoggedMessages_Type())
raisecomLogDestLoggedMessages.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomLogDestLoggedMessages.setStatus(_A)
_RaisecomLogDestDropMessages_Type=Integer32
_RaisecomLogDestDropMessages_Object=MibTableColumn
raisecomLogDestDropMessages=_RaisecomLogDestDropMessages_Object((1,3,6,1,4,1,8886,1,4,1,1,17,1,6),_RaisecomLogDestDropMessages_Type())
raisecomLogDestDropMessages.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomLogDestDropMessages.setStatus(_A)
_RaisecomLogDiscriminatorTable_Object=MibTable
raisecomLogDiscriminatorTable=_RaisecomLogDiscriminatorTable_Object((1,3,6,1,4,1,8886,1,4,1,1,18))
if mibBuilder.loadTexts:raisecomLogDiscriminatorTable.setStatus(_A)
_RaisecomLogDiscriminatorEntry_Object=MibTableRow
raisecomLogDiscriminatorEntry=_RaisecomLogDiscriminatorEntry_Object((1,3,6,1,4,1,8886,1,4,1,1,18,1))
raisecomLogDiscriminatorEntry.setIndexNames((0,_E,_W))
if mibBuilder.loadTexts:raisecomLogDiscriminatorEntry.setStatus(_A)
class _RaisecomLogDiscriminatorIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,5))
_RaisecomLogDiscriminatorIndex_Type.__name__=_C
_RaisecomLogDiscriminatorIndex_Object=MibTableColumn
raisecomLogDiscriminatorIndex=_RaisecomLogDiscriminatorIndex_Object((1,3,6,1,4,1,8886,1,4,1,1,18,1,1),_RaisecomLogDiscriminatorIndex_Type())
raisecomLogDiscriminatorIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:raisecomLogDiscriminatorIndex.setStatus(_A)
class _RaisecomLogDiscriminatorFacilityAct_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_H,1),(_J,2),(_K,3)))
_RaisecomLogDiscriminatorFacilityAct_Type.__name__=_C
_RaisecomLogDiscriminatorFacilityAct_Object=MibTableColumn
raisecomLogDiscriminatorFacilityAct=_RaisecomLogDiscriminatorFacilityAct_Object((1,3,6,1,4,1,8886,1,4,1,1,18,1,2),_RaisecomLogDiscriminatorFacilityAct_Type())
raisecomLogDiscriminatorFacilityAct.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomLogDiscriminatorFacilityAct.setStatus(_A)
class _RaisecomLogDiscriminatorFacilityStr_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,20))
_RaisecomLogDiscriminatorFacilityStr_Type.__name__=_F
_RaisecomLogDiscriminatorFacilityStr_Object=MibTableColumn
raisecomLogDiscriminatorFacilityStr=_RaisecomLogDiscriminatorFacilityStr_Object((1,3,6,1,4,1,8886,1,4,1,1,18,1,3),_RaisecomLogDiscriminatorFacilityStr_Type())
raisecomLogDiscriminatorFacilityStr.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomLogDiscriminatorFacilityStr.setStatus(_A)
class _RaisecomLogDiscriminatorMnemonicsAct_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_H,1),(_J,2),(_K,3)))
_RaisecomLogDiscriminatorMnemonicsAct_Type.__name__=_C
_RaisecomLogDiscriminatorMnemonicsAct_Object=MibTableColumn
raisecomLogDiscriminatorMnemonicsAct=_RaisecomLogDiscriminatorMnemonicsAct_Object((1,3,6,1,4,1,8886,1,4,1,1,18,1,4),_RaisecomLogDiscriminatorMnemonicsAct_Type())
raisecomLogDiscriminatorMnemonicsAct.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomLogDiscriminatorMnemonicsAct.setStatus(_A)
class _RaisecomLogDiscriminatorMnemonicsStr_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,30))
_RaisecomLogDiscriminatorMnemonicsStr_Type.__name__=_F
_RaisecomLogDiscriminatorMnemonicsStr_Object=MibTableColumn
raisecomLogDiscriminatorMnemonicsStr=_RaisecomLogDiscriminatorMnemonicsStr_Object((1,3,6,1,4,1,8886,1,4,1,1,18,1,5),_RaisecomLogDiscriminatorMnemonicsStr_Type())
raisecomLogDiscriminatorMnemonicsStr.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomLogDiscriminatorMnemonicsStr.setStatus(_A)
class _RaisecomLogDiscriminatorMsgbodyAct_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_H,1),(_J,2),(_K,3)))
_RaisecomLogDiscriminatorMsgbodyAct_Type.__name__=_C
_RaisecomLogDiscriminatorMsgbodyAct_Object=MibTableColumn
raisecomLogDiscriminatorMsgbodyAct=_RaisecomLogDiscriminatorMsgbodyAct_Object((1,3,6,1,4,1,8886,1,4,1,1,18,1,6),_RaisecomLogDiscriminatorMsgbodyAct_Type())
raisecomLogDiscriminatorMsgbodyAct.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomLogDiscriminatorMsgbodyAct.setStatus(_A)
class _RaisecomLogDiscriminatorMsgbodyStr_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,64))
_RaisecomLogDiscriminatorMsgbodyStr_Type.__name__=_F
_RaisecomLogDiscriminatorMsgbodyStr_Object=MibTableColumn
raisecomLogDiscriminatorMsgbodyStr=_RaisecomLogDiscriminatorMsgbodyStr_Object((1,3,6,1,4,1,8886,1,4,1,1,18,1,7),_RaisecomLogDiscriminatorMsgbodyStr_Type())
raisecomLogDiscriminatorMsgbodyStr.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomLogDiscriminatorMsgbodyStr.setStatus(_A)
_RaisecomLogHistoryTable_Object=MibTable
raisecomLogHistoryTable=_RaisecomLogHistoryTable_Object((1,3,6,1,4,1,8886,1,4,1,1,19))
if mibBuilder.loadTexts:raisecomLogHistoryTable.setStatus(_A)
_RaisecomLogHistoryEntry_Object=MibTableRow
raisecomLogHistoryEntry=_RaisecomLogHistoryEntry_Object((1,3,6,1,4,1,8886,1,4,1,1,19,1))
raisecomLogHistoryEntry.setIndexNames((0,_E,_X))
if mibBuilder.loadTexts:raisecomLogHistoryEntry.setStatus(_A)
_RaisecomLogHistIndex_Type=Integer32
_RaisecomLogHistIndex_Object=MibTableColumn
raisecomLogHistIndex=_RaisecomLogHistIndex_Object((1,3,6,1,4,1,8886,1,4,1,1,19,1,1),_RaisecomLogHistIndex_Type())
raisecomLogHistIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:raisecomLogHistIndex.setStatus(_A)
class _RaisecomLogHistFacility_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,20))
_RaisecomLogHistFacility_Type.__name__=_F
_RaisecomLogHistFacility_Object=MibTableColumn
raisecomLogHistFacility=_RaisecomLogHistFacility_Object((1,3,6,1,4,1,8886,1,4,1,1,19,1,2),_RaisecomLogHistFacility_Type())
raisecomLogHistFacility.setMaxAccess(_D)
if mibBuilder.loadTexts:raisecomLogHistFacility.setStatus(_A)
_RaisecomLogHistSeverity_Type=SyslogSeverity
_RaisecomLogHistSeverity_Object=MibTableColumn
raisecomLogHistSeverity=_RaisecomLogHistSeverity_Object((1,3,6,1,4,1,8886,1,4,1,1,19,1,3),_RaisecomLogHistSeverity_Type())
raisecomLogHistSeverity.setMaxAccess(_D)
if mibBuilder.loadTexts:raisecomLogHistSeverity.setStatus(_A)
class _RaisecomLogHistMnemonics_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,30))
_RaisecomLogHistMnemonics_Type.__name__=_F
_RaisecomLogHistMnemonics_Object=MibTableColumn
raisecomLogHistMnemonics=_RaisecomLogHistMnemonics_Object((1,3,6,1,4,1,8886,1,4,1,1,19,1,4),_RaisecomLogHistMnemonics_Type())
raisecomLogHistMnemonics.setMaxAccess(_D)
if mibBuilder.loadTexts:raisecomLogHistMnemonics.setStatus(_A)
class _RaisecomLogHistMsgbody_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,255))
_RaisecomLogHistMsgbody_Type.__name__=_F
_RaisecomLogHistMsgbody_Object=MibTableColumn
raisecomLogHistMsgbody=_RaisecomLogHistMsgbody_Object((1,3,6,1,4,1,8886,1,4,1,1,19,1,5),_RaisecomLogHistMsgbody_Type())
raisecomLogHistMsgbody.setMaxAccess(_D)
if mibBuilder.loadTexts:raisecomLogHistMsgbody.setStatus(_A)
_RaisecomLogHistTimestamp_Type=Integer32
_RaisecomLogHistTimestamp_Object=MibTableColumn
raisecomLogHistTimestamp=_RaisecomLogHistTimestamp_Object((1,3,6,1,4,1,8886,1,4,1,1,19,1,6),_RaisecomLogHistTimestamp_Type())
raisecomLogHistTimestamp.setMaxAccess(_D)
if mibBuilder.loadTexts:raisecomLogHistTimestamp.setStatus(_A)
_RaisecomLogServer_ObjectIdentity=ObjectIdentity
raisecomLogServer=_RaisecomLogServer_ObjectIdentity((1,3,6,1,4,1,8886,1,4,1,2))
_RaisecomLogMaxNumberOfLogServer_Type=Integer32
_RaisecomLogMaxNumberOfLogServer_Object=MibScalar
raisecomLogMaxNumberOfLogServer=_RaisecomLogMaxNumberOfLogServer_Object((1,3,6,1,4,1,8886,1,4,1,2,1),_RaisecomLogMaxNumberOfLogServer_Type())
raisecomLogMaxNumberOfLogServer.setMaxAccess(_D)
if mibBuilder.loadTexts:raisecomLogMaxNumberOfLogServer.setStatus(_A)
_RaisecomLogServerNumber_Type=Integer32
_RaisecomLogServerNumber_Object=MibScalar
raisecomLogServerNumber=_RaisecomLogServerNumber_Object((1,3,6,1,4,1,8886,1,4,1,2,2),_RaisecomLogServerNumber_Type())
raisecomLogServerNumber.setMaxAccess(_D)
if mibBuilder.loadTexts:raisecomLogServerNumber.setStatus(_A)
_RaisecomLogServerTable_Object=MibTable
raisecomLogServerTable=_RaisecomLogServerTable_Object((1,3,6,1,4,1,8886,1,4,1,2,3))
if mibBuilder.loadTexts:raisecomLogServerTable.setStatus(_A)
_RaisecomLogServerEntry_Object=MibTableRow
raisecomLogServerEntry=_RaisecomLogServerEntry_Object((1,3,6,1,4,1,8886,1,4,1,2,3,1))
raisecomLogServerEntry.setIndexNames((0,_E,_Y))
if mibBuilder.loadTexts:raisecomLogServerEntry.setStatus(_A)
_RaisecomLogServerIpAddress_Type=InetAddress
_RaisecomLogServerIpAddress_Object=MibTableColumn
raisecomLogServerIpAddress=_RaisecomLogServerIpAddress_Object((1,3,6,1,4,1,8886,1,4,1,2,3,1,1),_RaisecomLogServerIpAddress_Type())
raisecomLogServerIpAddress.setMaxAccess(_G)
if mibBuilder.loadTexts:raisecomLogServerIpAddress.setStatus(_A)
class _RaisecomLogServerPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_RaisecomLogServerPort_Type.__name__=_C
_RaisecomLogServerPort_Object=MibTableColumn
raisecomLogServerPort=_RaisecomLogServerPort_Object((1,3,6,1,4,1,8886,1,4,1,2,3,1,2),_RaisecomLogServerPort_Type())
raisecomLogServerPort.setMaxAccess(_D)
if mibBuilder.loadTexts:raisecomLogServerPort.setStatus(_A)
_RaisecomLogFacility_Type=LogFacility
_RaisecomLogFacility_Object=MibTableColumn
raisecomLogFacility=_RaisecomLogFacility_Object((1,3,6,1,4,1,8886,1,4,1,2,3,1,3),_RaisecomLogFacility_Type())
raisecomLogFacility.setMaxAccess(_I)
if mibBuilder.loadTexts:raisecomLogFacility.setStatus(_A)
_RaisecomLogServerMaxSeverity_Type=SyslogSeverity
_RaisecomLogServerMaxSeverity_Object=MibTableColumn
raisecomLogServerMaxSeverity=_RaisecomLogServerMaxSeverity_Object((1,3,6,1,4,1,8886,1,4,1,2,3,1,4),_RaisecomLogServerMaxSeverity_Type())
raisecomLogServerMaxSeverity.setMaxAccess(_I)
if mibBuilder.loadTexts:raisecomLogServerMaxSeverity.setStatus(_A)
_RaisecomLogServerRowStatus_Type=RowStatus
_RaisecomLogServerRowStatus_Object=MibTableColumn
raisecomLogServerRowStatus=_RaisecomLogServerRowStatus_Object((1,3,6,1,4,1,8886,1,4,1,2,3,1,5),_RaisecomLogServerRowStatus_Type())
raisecomLogServerRowStatus.setMaxAccess(_I)
if mibBuilder.loadTexts:raisecomLogServerRowStatus.setStatus(_A)
_RaisecomLogServerLoggedMessages_Type=Integer32
_RaisecomLogServerLoggedMessages_Object=MibTableColumn
raisecomLogServerLoggedMessages=_RaisecomLogServerLoggedMessages_Object((1,3,6,1,4,1,8886,1,4,1,2,3,1,6),_RaisecomLogServerLoggedMessages_Type())
raisecomLogServerLoggedMessages.setMaxAccess(_D)
if mibBuilder.loadTexts:raisecomLogServerLoggedMessages.setStatus(_A)
_RaisecomLogServerDropMessages_Type=Integer32
_RaisecomLogServerDropMessages_Object=MibTableColumn
raisecomLogServerDropMessages=_RaisecomLogServerDropMessages_Object((1,3,6,1,4,1,8886,1,4,1,2,3,1,7),_RaisecomLogServerDropMessages_Type())
raisecomLogServerDropMessages.setMaxAccess(_D)
if mibBuilder.loadTexts:raisecomLogServerDropMessages.setStatus(_A)
_RaisecomLogServerDiscriminator_Type=Integer32
_RaisecomLogServerDiscriminator_Object=MibTableColumn
raisecomLogServerDiscriminator=_RaisecomLogServerDiscriminator_Object((1,3,6,1,4,1,8886,1,4,1,2,3,1,8),_RaisecomLogServerDiscriminator_Type())
raisecomLogServerDiscriminator.setMaxAccess(_I)
if mibBuilder.loadTexts:raisecomLogServerDiscriminator.setStatus(_A)
_RaisecomDebug_ObjectIdentity=ObjectIdentity
raisecomDebug=_RaisecomDebug_ObjectIdentity((1,3,6,1,4,1,8886,1,4,1,3))
_RaisecomDebugTable_Object=MibTable
raisecomDebugTable=_RaisecomDebugTable_Object((1,3,6,1,4,1,8886,1,4,1,3,1))
if mibBuilder.loadTexts:raisecomDebugTable.setStatus(_A)
_RaisecomDebugEntry_Object=MibTableRow
raisecomDebugEntry=_RaisecomDebugEntry_Object((1,3,6,1,4,1,8886,1,4,1,3,1,1))
raisecomDebugEntry.setIndexNames((0,_E,_Z))
if mibBuilder.loadTexts:raisecomDebugEntry.setStatus(_A)
_RaisecomDebugIndex_Type=Integer32
_RaisecomDebugIndex_Object=MibTableColumn
raisecomDebugIndex=_RaisecomDebugIndex_Object((1,3,6,1,4,1,8886,1,4,1,3,1,1,1),_RaisecomDebugIndex_Type())
raisecomDebugIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:raisecomDebugIndex.setStatus(_A)
class _RaisecomDebugModuleName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_RaisecomDebugModuleName_Type.__name__=_F
_RaisecomDebugModuleName_Object=MibTableColumn
raisecomDebugModuleName=_RaisecomDebugModuleName_Object((1,3,6,1,4,1,8886,1,4,1,3,1,1,2),_RaisecomDebugModuleName_Type())
raisecomDebugModuleName.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomDebugModuleName.setStatus(_A)
_RaisecomDebugModuleEnable_Type=EnableVar
_RaisecomDebugModuleEnable_Object=MibTableColumn
raisecomDebugModuleEnable=_RaisecomDebugModuleEnable_Object((1,3,6,1,4,1,8886,1,4,1,3,1,1,3),_RaisecomDebugModuleEnable_Type())
raisecomDebugModuleEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomDebugModuleEnable.setStatus(_A)
class _RaisecomDebugMsgName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,30))
_RaisecomDebugMsgName_Type.__name__=_F
_RaisecomDebugMsgName_Object=MibTableColumn
raisecomDebugMsgName=_RaisecomDebugMsgName_Object((1,3,6,1,4,1,8886,1,4,1,3,1,1,4),_RaisecomDebugMsgName_Type())
raisecomDebugMsgName.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomDebugMsgName.setStatus(_A)
_RaisecomLogTrapGroup_ObjectIdentity=ObjectIdentity
raisecomLogTrapGroup=_RaisecomLogTrapGroup_ObjectIdentity((1,3,6,1,4,1,8886,1,4,1,4))
raisecomLogTrap=NotificationType((1,3,6,1,4,1,8886,1,4,1,4,1))
raisecomLogTrap.setObjects(*((_E,_a),(_E,_b),(_E,_c),(_E,_d),(_E,_e)))
if mibBuilder.loadTexts:raisecomLogTrap.setStatus(_A)
mibBuilder.exportSymbols(_E,**{_U:SyslogSeverity,'LogFacility':LogFacility,'raisecomSyslogService':raisecomSyslogService,'raisecomSyslogMibObjects':raisecomSyslogMibObjects,'raisecomLogBasic':raisecomLogBasic,'raisecomLogEnable':raisecomLogEnable,'raisecomLogRateLimit':raisecomLogRateLimit,'raisecomLogDropMessages':raisecomLogDropMessages,'raisecomLogConsoleLogedMessages':raisecomLogConsoleLogedMessages,'raisecomLogMonitorMessages':raisecomLogMonitorMessages,'raisecomLogTimeStamp':raisecomLogTimeStamp,'raisecomLogDebugTimeStamp':raisecomLogDebugTimeStamp,'raisecomLogHistoryEnable':raisecomLogHistoryEnable,'raisecomLogHistorySize':raisecomLogHistorySize,'raisecomLogBufferSize':raisecomLogBufferSize,'raisecomLogSequenceNumEnable':raisecomLogSequenceNumEnable,'raisecomDebugModuleLevel':raisecomDebugModuleLevel,'raisecomLogDebugDropMessages':raisecomLogDebugDropMessages,'raisecomLogBufferClear':raisecomLogBufferClear,'raisecomLogConfig':raisecomLogConfig,'raisecomLogConfigLevel':raisecomLogConfigLevel,'raisecomLogDestinationTable':raisecomLogDestinationTable,'raisecomLogDestinationEntry':raisecomLogDestinationEntry,_V:raisecomLogDestIndex,'raisecomLogDestEnable':raisecomLogDestEnable,'raisecomLogDestServrity':raisecomLogDestServrity,'raisecomLogDestDiscriminator':raisecomLogDestDiscriminator,'raisecomLogDestLoggedMessages':raisecomLogDestLoggedMessages,'raisecomLogDestDropMessages':raisecomLogDestDropMessages,'raisecomLogDiscriminatorTable':raisecomLogDiscriminatorTable,'raisecomLogDiscriminatorEntry':raisecomLogDiscriminatorEntry,_W:raisecomLogDiscriminatorIndex,'raisecomLogDiscriminatorFacilityAct':raisecomLogDiscriminatorFacilityAct,'raisecomLogDiscriminatorFacilityStr':raisecomLogDiscriminatorFacilityStr,'raisecomLogDiscriminatorMnemonicsAct':raisecomLogDiscriminatorMnemonicsAct,'raisecomLogDiscriminatorMnemonicsStr':raisecomLogDiscriminatorMnemonicsStr,'raisecomLogDiscriminatorMsgbodyAct':raisecomLogDiscriminatorMsgbodyAct,'raisecomLogDiscriminatorMsgbodyStr':raisecomLogDiscriminatorMsgbodyStr,'raisecomLogHistoryTable':raisecomLogHistoryTable,'raisecomLogHistoryEntry':raisecomLogHistoryEntry,_X:raisecomLogHistIndex,_a:raisecomLogHistFacility,_b:raisecomLogHistSeverity,_c:raisecomLogHistMnemonics,_d:raisecomLogHistMsgbody,_e:raisecomLogHistTimestamp,'raisecomLogServer':raisecomLogServer,'raisecomLogMaxNumberOfLogServer':raisecomLogMaxNumberOfLogServer,'raisecomLogServerNumber':raisecomLogServerNumber,'raisecomLogServerTable':raisecomLogServerTable,'raisecomLogServerEntry':raisecomLogServerEntry,_Y:raisecomLogServerIpAddress,'raisecomLogServerPort':raisecomLogServerPort,'raisecomLogFacility':raisecomLogFacility,'raisecomLogServerMaxSeverity':raisecomLogServerMaxSeverity,'raisecomLogServerRowStatus':raisecomLogServerRowStatus,'raisecomLogServerLoggedMessages':raisecomLogServerLoggedMessages,'raisecomLogServerDropMessages':raisecomLogServerDropMessages,'raisecomLogServerDiscriminator':raisecomLogServerDiscriminator,'raisecomDebug':raisecomDebug,'raisecomDebugTable':raisecomDebugTable,'raisecomDebugEntry':raisecomDebugEntry,_Z:raisecomDebugIndex,'raisecomDebugModuleName':raisecomDebugModuleName,'raisecomDebugModuleEnable':raisecomDebugModuleEnable,'raisecomDebugMsgName':raisecomDebugMsgName,'raisecomLogTrapGroup':raisecomLogTrapGroup,'raisecomLogTrap':raisecomLogTrap})