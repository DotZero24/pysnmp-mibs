_l='cpqSmAlertDestPagerId'
_k='cpqSmAlertDestPhoneNumber'
_j='cpqSmAlertDestType'
_i='cpqSmMonItemTimeStamp'
_h='cpqSmMonItemLogicalOperator'
_g='cpqSmMonItemOptional'
_f='cpqSmMonItemLimit'
_e='cpqSmMonItemSeverity'
_d='cpqSmMonItemDataType'
_c='cpqSmMonItemLabel'
_b='cpqSmObjectLabel'
_a='cpqSmMonItemCurVal'
_Z='cpqSmAlertDestinationBlacklisted'
_Y='cpqSmBoardTimeout'
_X='cpqSmBatteryFailed'
_W='cpqSmCommFailed'
_V='cpqSmServerManagerAlert'
_U='cpqSmBoardReset'
_T='cpqSmBoardFailed'
_S='cpqSmTrapLogIndex'
_R='cpqSmAlertDestPriorityIndex'
_Q='cpqSmModemSettingsIndex'
_P='cpqSmMonItemIndex'
_O='cpqSmMonItemInstIndex'
_N='cpqSmMonItemObjIndex'
_M='cpqSmObjectInstIndex'
_L='cpqSmObjectIndex'
_K='failed'
_J='NotificationType'
_I='OctetString'
_H='enabled'
_G='disabled'
_F='DisplayString'
_E='CPQSRVMN-MIB'
_D='other'
_C='Integer32'
_B='read-only'
_A='mandatory'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_I,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
compaq,=mibBuilder.importSymbols('CPQHOST-MIB','compaq')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,NotificationType,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier',_J,'ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn',_J,'TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_F,'PhysAddress','TextualConvention')
_CpqServerManager_ObjectIdentity=ObjectIdentity
cpqServerManager=_CpqServerManager_ObjectIdentity((1,3,6,1,4,1,232,4))
_CpqSmMibRev_ObjectIdentity=ObjectIdentity
cpqSmMibRev=_CpqSmMibRev_ObjectIdentity((1,3,6,1,4,1,232,4,1))
class _CpqSmMibRevMajor_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_CpqSmMibRevMajor_Type.__name__=_C
_CpqSmMibRevMajor_Object=MibScalar
cpqSmMibRevMajor=_CpqSmMibRevMajor_Object((1,3,6,1,4,1,232,4,1,1),_CpqSmMibRevMajor_Type())
cpqSmMibRevMajor.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqSmMibRevMajor.setStatus(_A)
class _CpqSmMibRevMinor_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_CpqSmMibRevMinor_Type.__name__=_C
_CpqSmMibRevMinor_Object=MibScalar
cpqSmMibRevMinor=_CpqSmMibRevMinor_Object((1,3,6,1,4,1,232,4,1,2),_CpqSmMibRevMinor_Type())
cpqSmMibRevMinor.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqSmMibRevMinor.setStatus(_A)
_CpqSmComponent_ObjectIdentity=ObjectIdentity
cpqSmComponent=_CpqSmComponent_ObjectIdentity((1,3,6,1,4,1,232,4,2))
_CpqSmInterface_ObjectIdentity=ObjectIdentity
cpqSmInterface=_CpqSmInterface_ObjectIdentity((1,3,6,1,4,1,232,4,2,1))
_CpqSmOsNetWare3x_ObjectIdentity=ObjectIdentity
cpqSmOsNetWare3x=_CpqSmOsNetWare3x_ObjectIdentity((1,3,6,1,4,1,232,4,2,1,1))
class _CpqSmNw3xDriverName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_CpqSmNw3xDriverName_Type.__name__=_F
_CpqSmNw3xDriverName_Object=MibScalar
cpqSmNw3xDriverName=_CpqSmNw3xDriverName_Object((1,3,6,1,4,1,232,4,2,1,1,1),_CpqSmNw3xDriverName_Type())
cpqSmNw3xDriverName.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqSmNw3xDriverName.setStatus(_A)
class _CpqSmNw3xDriverDate_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(8,8));fixedLength=8
_CpqSmNw3xDriverDate_Type.__name__=_F
_CpqSmNw3xDriverDate_Object=MibScalar
cpqSmNw3xDriverDate=_CpqSmNw3xDriverDate_Object((1,3,6,1,4,1,232,4,2,1,1,2),_CpqSmNw3xDriverDate_Type())
cpqSmNw3xDriverDate.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqSmNw3xDriverDate.setStatus(_A)
class _CpqSmNw3xDriverVersion_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,5))
_CpqSmNw3xDriverVersion_Type.__name__=_F
_CpqSmNw3xDriverVersion_Object=MibScalar
cpqSmNw3xDriverVersion=_CpqSmNw3xDriverVersion_Object((1,3,6,1,4,1,232,4,2,1,1,3),_CpqSmNw3xDriverVersion_Type())
cpqSmNw3xDriverVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqSmNw3xDriverVersion.setStatus(_A)
_CpqSmNw3xDriverIssuedCommands_Type=Counter32
_CpqSmNw3xDriverIssuedCommands_Object=MibScalar
cpqSmNw3xDriverIssuedCommands=_CpqSmNw3xDriverIssuedCommands_Object((1,3,6,1,4,1,232,4,2,1,1,4),_CpqSmNw3xDriverIssuedCommands_Type())
cpqSmNw3xDriverIssuedCommands.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqSmNw3xDriverIssuedCommands.setStatus(_A)
_CpqSmNw3xDriverReceivedCommands_Type=Counter32
_CpqSmNw3xDriverReceivedCommands_Object=MibScalar
cpqSmNw3xDriverReceivedCommands=_CpqSmNw3xDriverReceivedCommands_Object((1,3,6,1,4,1,232,4,2,1,1,5),_CpqSmNw3xDriverReceivedCommands_Type())
cpqSmNw3xDriverReceivedCommands.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqSmNw3xDriverReceivedCommands.setStatus(_A)
class _CpqSmNw3xDriverWatchdogFrequency_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_CpqSmNw3xDriverWatchdogFrequency_Type.__name__=_C
_CpqSmNw3xDriverWatchdogFrequency_Object=MibScalar
cpqSmNw3xDriverWatchdogFrequency=_CpqSmNw3xDriverWatchdogFrequency_Object((1,3,6,1,4,1,232,4,2,1,1,6),_CpqSmNw3xDriverWatchdogFrequency_Type())
cpqSmNw3xDriverWatchdogFrequency.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqSmNw3xDriverWatchdogFrequency.setStatus(_A)
class _CpqSmNw3xDriverClockSyncFrequency_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_CpqSmNw3xDriverClockSyncFrequency_Type.__name__=_C
_CpqSmNw3xDriverClockSyncFrequency_Object=MibScalar
cpqSmNw3xDriverClockSyncFrequency=_CpqSmNw3xDriverClockSyncFrequency_Object((1,3,6,1,4,1,232,4,2,1,1,7),_CpqSmNw3xDriverClockSyncFrequency_Type())
cpqSmNw3xDriverClockSyncFrequency.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqSmNw3xDriverClockSyncFrequency.setStatus(_A)
_CpqSmNw3xDriverIssuedWatchdogs_Type=Counter32
_CpqSmNw3xDriverIssuedWatchdogs_Object=MibScalar
cpqSmNw3xDriverIssuedWatchdogs=_CpqSmNw3xDriverIssuedWatchdogs_Object((1,3,6,1,4,1,232,4,2,1,1,8),_CpqSmNw3xDriverIssuedWatchdogs_Type())
cpqSmNw3xDriverIssuedWatchdogs.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqSmNw3xDriverIssuedWatchdogs.setStatus(_A)
_CpqSmNw3xDriverIssuedClockSyncs_Type=Counter32
_CpqSmNw3xDriverIssuedClockSyncs_Object=MibScalar
cpqSmNw3xDriverIssuedClockSyncs=_CpqSmNw3xDriverIssuedClockSyncs_Object((1,3,6,1,4,1,232,4,2,1,1,9),_CpqSmNw3xDriverIssuedClockSyncs_Type())
cpqSmNw3xDriverIssuedClockSyncs.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqSmNw3xDriverIssuedClockSyncs.setStatus(_A)
_CpqSmNw3xDriverMemoryAllocationFailedErrs_Type=Counter32
_CpqSmNw3xDriverMemoryAllocationFailedErrs_Object=MibScalar
cpqSmNw3xDriverMemoryAllocationFailedErrs=_CpqSmNw3xDriverMemoryAllocationFailedErrs_Object((1,3,6,1,4,1,232,4,2,1,1,10),_CpqSmNw3xDriverMemoryAllocationFailedErrs_Type())
cpqSmNw3xDriverMemoryAllocationFailedErrs.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqSmNw3xDriverMemoryAllocationFailedErrs.setStatus(_A)
_CpqSmNw3xDriverBoardResets_Type=Counter32
_CpqSmNw3xDriverBoardResets_Object=MibScalar
cpqSmNw3xDriverBoardResets=_CpqSmNw3xDriverBoardResets_Object((1,3,6,1,4,1,232,4,2,1,1,11),_CpqSmNw3xDriverBoardResets_Type())
cpqSmNw3xDriverBoardResets.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqSmNw3xDriverBoardResets.setStatus(_A)
class _CpqSmNw3xBoardState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_D,1),('ok',2),(_K,3)))
_CpqSmNw3xBoardState_Type.__name__=_C
_CpqSmNw3xBoardState_Object=MibScalar
cpqSmNw3xBoardState=_CpqSmNw3xBoardState_Object((1,3,6,1,4,1,232,4,2,1,1,12),_CpqSmNw3xBoardState_Type())
cpqSmNw3xBoardState.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqSmNw3xBoardState.setStatus(_A)
_CpqSmCntlr_ObjectIdentity=ObjectIdentity
cpqSmCntlr=_CpqSmCntlr_ObjectIdentity((1,3,6,1,4,1,232,4,2,2))
class _CpqSmCntlrBoardName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,15))
_CpqSmCntlrBoardName_Type.__name__=_F
_CpqSmCntlrBoardName_Object=MibScalar
cpqSmCntlrBoardName=_CpqSmCntlrBoardName_Object((1,3,6,1,4,1,232,4,2,2,1),_CpqSmCntlrBoardName_Type())
cpqSmCntlrBoardName.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqSmCntlrBoardName.setStatus(_A)
class _CpqSmCntlrBoardId_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,5))
_CpqSmCntlrBoardId_Type.__name__=_F
_CpqSmCntlrBoardId_Object=MibScalar
cpqSmCntlrBoardId=_CpqSmCntlrBoardId_Object((1,3,6,1,4,1,232,4,2,2,2),_CpqSmCntlrBoardId_Type())
cpqSmCntlrBoardId.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqSmCntlrBoardId.setStatus(_A)
class _CpqSmCntlrRomDate_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(8,8));fixedLength=8
_CpqSmCntlrRomDate_Type.__name__=_F
_CpqSmCntlrRomDate_Object=MibScalar
cpqSmCntlrRomDate=_CpqSmCntlrRomDate_Object((1,3,6,1,4,1,232,4,2,2,3),_CpqSmCntlrRomDate_Type())
cpqSmCntlrRomDate.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqSmCntlrRomDate.setStatus(_A)
class _CpqSmCntlrCountryCode_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(2,2));fixedLength=2
_CpqSmCntlrCountryCode_Type.__name__=_F
_CpqSmCntlrCountryCode_Object=MibScalar
cpqSmCntlrCountryCode=_CpqSmCntlrCountryCode_Object((1,3,6,1,4,1,232,4,2,2,4),_CpqSmCntlrCountryCode_Type())
cpqSmCntlrCountryCode.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqSmCntlrCountryCode.setStatus(_A)
class _CpqSmCntlrVoiceRomStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_D,1),('notInstalled',2),('installed',3)))
_CpqSmCntlrVoiceRomStatus_Type.__name__=_C
_CpqSmCntlrVoiceRomStatus_Object=MibScalar
cpqSmCntlrVoiceRomStatus=_CpqSmCntlrVoiceRomStatus_Object((1,3,6,1,4,1,232,4,2,2,5),_CpqSmCntlrVoiceRomStatus_Type())
cpqSmCntlrVoiceRomStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqSmCntlrVoiceRomStatus.setStatus(_A)
class _CpqSmCntlrBatteryStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_D,1),('connected',2),('disconnected',3)))
_CpqSmCntlrBatteryStatus_Type.__name__=_C
_CpqSmCntlrBatteryStatus_Object=MibScalar
cpqSmCntlrBatteryStatus=_CpqSmCntlrBatteryStatus_Object((1,3,6,1,4,1,232,4,2,2,6),_CpqSmCntlrBatteryStatus_Type())
cpqSmCntlrBatteryStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqSmCntlrBatteryStatus.setStatus(_A)
class _CpqSmCntlrDormantModeStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_D,1),('normal',2),('dormantOnPowerDown',3)))
_CpqSmCntlrDormantModeStatus_Type.__name__=_C
_CpqSmCntlrDormantModeStatus_Object=MibScalar
cpqSmCntlrDormantModeStatus=_CpqSmCntlrDormantModeStatus_Object((1,3,6,1,4,1,232,4,2,2,7),_CpqSmCntlrDormantModeStatus_Type())
cpqSmCntlrDormantModeStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqSmCntlrDormantModeStatus.setStatus(_A)
class _CpqSmCntlrSelfTestErrorCode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_CpqSmCntlrSelfTestErrorCode_Type.__name__=_C
_CpqSmCntlrSelfTestErrorCode_Object=MibScalar
cpqSmCntlrSelfTestErrorCode=_CpqSmCntlrSelfTestErrorCode_Object((1,3,6,1,4,1,232,4,2,2,8),_CpqSmCntlrSelfTestErrorCode_Type())
cpqSmCntlrSelfTestErrorCode.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqSmCntlrSelfTestErrorCode.setStatus(_A)
class _CpqSmCntlrOsId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,177,178,179,180,181,182)));namedValues=NamedValues(*((_D,1),('netware286',177),('netware386',178),('os2LanManager',179),('unix',180),('banyan',181),('dos',182)))
_CpqSmCntlrOsId_Type.__name__=_C
_CpqSmCntlrOsId_Object=MibScalar
cpqSmCntlrOsId=_CpqSmCntlrOsId_Object((1,3,6,1,4,1,232,4,2,2,9),_CpqSmCntlrOsId_Type())
cpqSmCntlrOsId.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqSmCntlrOsId.setStatus(_A)
class _CpqSmCntlrOsMajorRev_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_CpqSmCntlrOsMajorRev_Type.__name__=_C
_CpqSmCntlrOsMajorRev_Object=MibScalar
cpqSmCntlrOsMajorRev=_CpqSmCntlrOsMajorRev_Object((1,3,6,1,4,1,232,4,2,2,10),_CpqSmCntlrOsMajorRev_Type())
cpqSmCntlrOsMajorRev.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqSmCntlrOsMajorRev.setStatus(_A)
class _CpqSmCntlrOsMinorRev_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_CpqSmCntlrOsMinorRev_Type.__name__=_C
_CpqSmCntlrOsMinorRev_Object=MibScalar
cpqSmCntlrOsMinorRev=_CpqSmCntlrOsMinorRev_Object((1,3,6,1,4,1,232,4,2,2,11),_CpqSmCntlrOsMinorRev_Type())
cpqSmCntlrOsMinorRev.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqSmCntlrOsMinorRev.setStatus(_A)
class _CpqSmCntlrPostTimeout_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,60))
_CpqSmCntlrPostTimeout_Type.__name__=_C
_CpqSmCntlrPostTimeout_Object=MibScalar
cpqSmCntlrPostTimeout=_CpqSmCntlrPostTimeout_Object((1,3,6,1,4,1,232,4,2,2,12),_CpqSmCntlrPostTimeout_Type())
cpqSmCntlrPostTimeout.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqSmCntlrPostTimeout.setStatus(_A)
class _CpqSmCntlrCondition_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_D,1),('ok',2),('degraded',3),(_K,4)))
_CpqSmCntlrCondition_Type.__name__=_C
_CpqSmCntlrCondition_Object=MibScalar
cpqSmCntlrCondition=_CpqSmCntlrCondition_Object((1,3,6,1,4,1,232,4,2,2,13),_CpqSmCntlrCondition_Type())
cpqSmCntlrCondition.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqSmCntlrCondition.setStatus(_A)
_CpqSmObjData_ObjectIdentity=ObjectIdentity
cpqSmObjData=_CpqSmObjData_ObjectIdentity((1,3,6,1,4,1,232,4,2,3))
class _CpqSmObjDataTotalObjects_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_CpqSmObjDataTotalObjects_Type.__name__=_C
_CpqSmObjDataTotalObjects_Object=MibScalar
cpqSmObjDataTotalObjects=_CpqSmObjDataTotalObjects_Object((1,3,6,1,4,1,232,4,2,3,1),_CpqSmObjDataTotalObjects_Type())
cpqSmObjDataTotalObjects.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqSmObjDataTotalObjects.setStatus(_A)
class _CpqSmObjDataObjectTotalSpace_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_CpqSmObjDataObjectTotalSpace_Type.__name__=_C
_CpqSmObjDataObjectTotalSpace_Object=MibScalar
cpqSmObjDataObjectTotalSpace=_CpqSmObjDataObjectTotalSpace_Object((1,3,6,1,4,1,232,4,2,3,2),_CpqSmObjDataObjectTotalSpace_Type())
cpqSmObjDataObjectTotalSpace.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqSmObjDataObjectTotalSpace.setStatus(_A)
class _CpqSmObjDataObjectSpaceAvailable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_CpqSmObjDataObjectSpaceAvailable_Type.__name__=_C
_CpqSmObjDataObjectSpaceAvailable_Object=MibScalar
cpqSmObjDataObjectSpaceAvailable=_CpqSmObjDataObjectSpaceAvailable_Object((1,3,6,1,4,1,232,4,2,3,3),_CpqSmObjDataObjectSpaceAvailable_Type())
cpqSmObjDataObjectSpaceAvailable.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqSmObjDataObjectSpaceAvailable.setStatus(_A)
class _CpqSmObjDataInnateMonitoringStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_D,1),(_G,2),(_H,3)))
_CpqSmObjDataInnateMonitoringStatus_Type.__name__=_C
_CpqSmObjDataInnateMonitoringStatus_Object=MibScalar
cpqSmObjDataInnateMonitoringStatus=_CpqSmObjDataInnateMonitoringStatus_Object((1,3,6,1,4,1,232,4,2,3,4),_CpqSmObjDataInnateMonitoringStatus_Type())
cpqSmObjDataInnateMonitoringStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqSmObjDataInnateMonitoringStatus.setStatus(_A)
_CpqSmObjectTable_Object=MibTable
cpqSmObjectTable=_CpqSmObjectTable_Object((1,3,6,1,4,1,232,4,2,3,5))
if mibBuilder.loadTexts:cpqSmObjectTable.setStatus(_A)
_CpqSmObjectEntry_Object=MibTableRow
cpqSmObjectEntry=_CpqSmObjectEntry_Object((1,3,6,1,4,1,232,4,2,3,5,1))
cpqSmObjectEntry.setIndexNames((0,_E,_L),(0,_E,_M))
if mibBuilder.loadTexts:cpqSmObjectEntry.setStatus(_A)
class _CpqSmObjectIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_CpqSmObjectIndex_Type.__name__=_C
_CpqSmObjectIndex_Object=MibTableColumn
cpqSmObjectIndex=_CpqSmObjectIndex_Object((1,3,6,1,4,1,232,4,2,3,5,1,1),_CpqSmObjectIndex_Type())
cpqSmObjectIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqSmObjectIndex.setStatus(_A)
class _CpqSmObjectInstIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_CpqSmObjectInstIndex_Type.__name__=_C
_CpqSmObjectInstIndex_Object=MibTableColumn
cpqSmObjectInstIndex=_CpqSmObjectInstIndex_Object((1,3,6,1,4,1,232,4,2,3,5,1,2),_CpqSmObjectInstIndex_Type())
cpqSmObjectInstIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqSmObjectInstIndex.setStatus(_A)
_CpqSmObjectClass_Type=Integer32
_CpqSmObjectClass_Object=MibTableColumn
cpqSmObjectClass=_CpqSmObjectClass_Object((1,3,6,1,4,1,232,4,2,3,5,1,3),_CpqSmObjectClass_Type())
cpqSmObjectClass.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqSmObjectClass.setStatus(_A)
class _CpqSmObjectLabel_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,15))
_CpqSmObjectLabel_Type.__name__=_F
_CpqSmObjectLabel_Object=MibTableColumn
cpqSmObjectLabel=_CpqSmObjectLabel_Object((1,3,6,1,4,1,232,4,2,3,5,1,4),_CpqSmObjectLabel_Type())
cpqSmObjectLabel.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqSmObjectLabel.setStatus(_A)
_CpqSmMonItemTable_Object=MibTable
cpqSmMonItemTable=_CpqSmMonItemTable_Object((1,3,6,1,4,1,232,4,2,3,6))
if mibBuilder.loadTexts:cpqSmMonItemTable.setStatus(_A)
_CpqSmMonItemEntry_Object=MibTableRow
cpqSmMonItemEntry=_CpqSmMonItemEntry_Object((1,3,6,1,4,1,232,4,2,3,6,1))
cpqSmMonItemEntry.setIndexNames((0,_E,_N),(0,_E,_O),(0,_E,_P))
if mibBuilder.loadTexts:cpqSmMonItemEntry.setStatus(_A)
class _CpqSmMonItemObjIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_CpqSmMonItemObjIndex_Type.__name__=_C
_CpqSmMonItemObjIndex_Object=MibTableColumn
cpqSmMonItemObjIndex=_CpqSmMonItemObjIndex_Object((1,3,6,1,4,1,232,4,2,3,6,1,1),_CpqSmMonItemObjIndex_Type())
cpqSmMonItemObjIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqSmMonItemObjIndex.setStatus(_A)
class _CpqSmMonItemInstIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_CpqSmMonItemInstIndex_Type.__name__=_C
_CpqSmMonItemInstIndex_Object=MibTableColumn
cpqSmMonItemInstIndex=_CpqSmMonItemInstIndex_Object((1,3,6,1,4,1,232,4,2,3,6,1,2),_CpqSmMonItemInstIndex_Type())
cpqSmMonItemInstIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqSmMonItemInstIndex.setStatus(_A)
class _CpqSmMonItemIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_CpqSmMonItemIndex_Type.__name__=_C
_CpqSmMonItemIndex_Object=MibTableColumn
cpqSmMonItemIndex=_CpqSmMonItemIndex_Object((1,3,6,1,4,1,232,4,2,3,6,1,3),_CpqSmMonItemIndex_Type())
cpqSmMonItemIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqSmMonItemIndex.setStatus(_A)
class _CpqSmMonItemOnNetAlertStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_D,1),(_G,2),(_H,3)))
_CpqSmMonItemOnNetAlertStatus_Type.__name__=_C
_CpqSmMonItemOnNetAlertStatus_Object=MibTableColumn
cpqSmMonItemOnNetAlertStatus=_CpqSmMonItemOnNetAlertStatus_Object((1,3,6,1,4,1,232,4,2,3,6,1,4),_CpqSmMonItemOnNetAlertStatus_Type())
cpqSmMonItemOnNetAlertStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqSmMonItemOnNetAlertStatus.setStatus(_A)
class _CpqSmMonItemRemoteAlertStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_D,1),(_G,2),(_H,3)))
_CpqSmMonItemRemoteAlertStatus_Type.__name__=_C
_CpqSmMonItemRemoteAlertStatus_Object=MibTableColumn
cpqSmMonItemRemoteAlertStatus=_CpqSmMonItemRemoteAlertStatus_Object((1,3,6,1,4,1,232,4,2,3,6,1,5),_CpqSmMonItemRemoteAlertStatus_Type())
cpqSmMonItemRemoteAlertStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqSmMonItemRemoteAlertStatus.setStatus(_A)
class _CpqSmMonItemInnateStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_D,1),('externallyManaged',2),('innate',3)))
_CpqSmMonItemInnateStatus_Type.__name__=_C
_CpqSmMonItemInnateStatus_Object=MibTableColumn
cpqSmMonItemInnateStatus=_CpqSmMonItemInnateStatus_Object((1,3,6,1,4,1,232,4,2,3,6,1,6),_CpqSmMonItemInnateStatus_Type())
cpqSmMonItemInnateStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqSmMonItemInnateStatus.setStatus(_A)
class _CpqSmMonItemHostNotify_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_D,1),(_G,2),(_H,3)))
_CpqSmMonItemHostNotify_Type.__name__=_C
_CpqSmMonItemHostNotify_Object=MibTableColumn
cpqSmMonItemHostNotify=_CpqSmMonItemHostNotify_Object((1,3,6,1,4,1,232,4,2,3,6,1,7),_CpqSmMonItemHostNotify_Type())
cpqSmMonItemHostNotify.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqSmMonItemHostNotify.setStatus(_A)
class _CpqSmMonItemLogicalOperator_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9)));namedValues=NamedValues(*((_D,1),('equal',2),('notEqual',3),('lessThan',4),('greaterThan',5),('lessThanOrEqual',6),('greaterThanOrEqual',7),('inside',8),('outside',9)))
_CpqSmMonItemLogicalOperator_Type.__name__=_C
_CpqSmMonItemLogicalOperator_Object=MibTableColumn
cpqSmMonItemLogicalOperator=_CpqSmMonItemLogicalOperator_Object((1,3,6,1,4,1,232,4,2,3,6,1,8),_CpqSmMonItemLogicalOperator_Type())
cpqSmMonItemLogicalOperator.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqSmMonItemLogicalOperator.setStatus(_A)
class _CpqSmMonItemSeverity_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_D,1),('status',2),('warning',3),('critical',4),('catastrophic',5)))
_CpqSmMonItemSeverity_Type.__name__=_C
_CpqSmMonItemSeverity_Object=MibTableColumn
cpqSmMonItemSeverity=_CpqSmMonItemSeverity_Object((1,3,6,1,4,1,232,4,2,3,6,1,9),_CpqSmMonItemSeverity_Type())
cpqSmMonItemSeverity.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqSmMonItemSeverity.setStatus(_A)
class _CpqSmMonItemDataType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*((_D,1),('counter',2),('state',3),('range',4),('string',5),('data',6),('queue',7)))
_CpqSmMonItemDataType_Type.__name__=_C
_CpqSmMonItemDataType_Object=MibTableColumn
cpqSmMonItemDataType=_CpqSmMonItemDataType_Object((1,3,6,1,4,1,232,4,2,3,6,1,10),_CpqSmMonItemDataType_Type())
cpqSmMonItemDataType.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqSmMonItemDataType.setStatus(_A)
class _CpqSmMonItemVoiceMsgNum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,511))
_CpqSmMonItemVoiceMsgNum_Type.__name__=_C
_CpqSmMonItemVoiceMsgNum_Object=MibTableColumn
cpqSmMonItemVoiceMsgNum=_CpqSmMonItemVoiceMsgNum_Object((1,3,6,1,4,1,232,4,2,3,6,1,11),_CpqSmMonItemVoiceMsgNum_Type())
cpqSmMonItemVoiceMsgNum.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqSmMonItemVoiceMsgNum.setStatus(_A)
class _CpqSmMonItemLabel_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,15))
_CpqSmMonItemLabel_Type.__name__=_F
_CpqSmMonItemLabel_Object=MibTableColumn
cpqSmMonItemLabel=_CpqSmMonItemLabel_Object((1,3,6,1,4,1,232,4,2,3,6,1,12),_CpqSmMonItemLabel_Type())
cpqSmMonItemLabel.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqSmMonItemLabel.setStatus(_A)
_CpqSmMonItemLimit_Type=Integer32
_CpqSmMonItemLimit_Object=MibTableColumn
cpqSmMonItemLimit=_CpqSmMonItemLimit_Object((1,3,6,1,4,1,232,4,2,3,6,1,13),_CpqSmMonItemLimit_Type())
cpqSmMonItemLimit.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqSmMonItemLimit.setStatus(_A)
_CpqSmMonItemOptional_Type=Integer32
_CpqSmMonItemOptional_Object=MibTableColumn
cpqSmMonItemOptional=_CpqSmMonItemOptional_Object((1,3,6,1,4,1,232,4,2,3,6,1,14),_CpqSmMonItemOptional_Type())
cpqSmMonItemOptional.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqSmMonItemOptional.setStatus(_A)
_CpqSmMonItemDefVal_Type=Integer32
_CpqSmMonItemDefVal_Object=MibTableColumn
cpqSmMonItemDefVal=_CpqSmMonItemDefVal_Object((1,3,6,1,4,1,232,4,2,3,6,1,15),_CpqSmMonItemDefVal_Type())
cpqSmMonItemDefVal.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqSmMonItemDefVal.setStatus(_A)
_CpqSmMonItemCurVal_Type=Integer32
_CpqSmMonItemCurVal_Object=MibTableColumn
cpqSmMonItemCurVal=_CpqSmMonItemCurVal_Object((1,3,6,1,4,1,232,4,2,3,6,1,16),_CpqSmMonItemCurVal_Type())
cpqSmMonItemCurVal.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqSmMonItemCurVal.setStatus(_A)
class _CpqSmMonItemCurString_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_CpqSmMonItemCurString_Type.__name__=_F
_CpqSmMonItemCurString_Object=MibTableColumn
cpqSmMonItemCurString=_CpqSmMonItemCurString_Object((1,3,6,1,4,1,232,4,2,3,6,1,17),_CpqSmMonItemCurString_Type())
cpqSmMonItemCurString.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqSmMonItemCurString.setStatus(_A)
class _CpqSmMonItemCurContents_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,256))
_CpqSmMonItemCurContents_Type.__name__=_I
_CpqSmMonItemCurContents_Object=MibTableColumn
cpqSmMonItemCurContents=_CpqSmMonItemCurContents_Object((1,3,6,1,4,1,232,4,2,3,6,1,18),_CpqSmMonItemCurContents_Type())
cpqSmMonItemCurContents.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqSmMonItemCurContents.setStatus(_A)
class _CpqSmMonItemTimeStamp_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(6,6));fixedLength=6
_CpqSmMonItemTimeStamp_Type.__name__=_I
_CpqSmMonItemTimeStamp_Object=MibTableColumn
cpqSmMonItemTimeStamp=_CpqSmMonItemTimeStamp_Object((1,3,6,1,4,1,232,4,2,3,6,1,19),_CpqSmMonItemTimeStamp_Type())
cpqSmMonItemTimeStamp.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqSmMonItemTimeStamp.setStatus(_A)
_CpqSmAsyncComm_ObjectIdentity=ObjectIdentity
cpqSmAsyncComm=_CpqSmAsyncComm_ObjectIdentity((1,3,6,1,4,1,232,4,2,4))
class _CpqSmCommAsyncCommunicationStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_D,1),(_G,2),(_H,3)))
_CpqSmCommAsyncCommunicationStatus_Type.__name__=_C
_CpqSmCommAsyncCommunicationStatus_Object=MibScalar
cpqSmCommAsyncCommunicationStatus=_CpqSmCommAsyncCommunicationStatus_Object((1,3,6,1,4,1,232,4,2,4,1),_CpqSmCommAsyncCommunicationStatus_Type())
cpqSmCommAsyncCommunicationStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqSmCommAsyncCommunicationStatus.setStatus(_A)
class _CpqSmCommInternalModemMaxBaudRate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_CpqSmCommInternalModemMaxBaudRate_Type.__name__=_C
_CpqSmCommInternalModemMaxBaudRate_Object=MibScalar
cpqSmCommInternalModemMaxBaudRate=_CpqSmCommInternalModemMaxBaudRate_Object((1,3,6,1,4,1,232,4,2,4,2),_CpqSmCommInternalModemMaxBaudRate_Type())
cpqSmCommInternalModemMaxBaudRate.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqSmCommInternalModemMaxBaudRate.setStatus(_A)
class _CpqSmCommAudibleIndicatorStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_D,1),(_G,2),(_H,3)))
_CpqSmCommAudibleIndicatorStatus_Type.__name__=_C
_CpqSmCommAudibleIndicatorStatus_Object=MibScalar
cpqSmCommAudibleIndicatorStatus=_CpqSmCommAudibleIndicatorStatus_Object((1,3,6,1,4,1,232,4,2,4,3),_CpqSmCommAudibleIndicatorStatus_Type())
cpqSmCommAudibleIndicatorStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqSmCommAudibleIndicatorStatus.setStatus(_A)
class _CpqSmCommRemoteSessionStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*((_D,1),('notSupported',2),('noSessionActive',3),('remoteSessionActive',4),('pgrVoiceSessionActive',5),('remoteConsoleActive',6)))
_CpqSmCommRemoteSessionStatus_Type.__name__=_C
_CpqSmCommRemoteSessionStatus_Object=MibScalar
cpqSmCommRemoteSessionStatus=_CpqSmCommRemoteSessionStatus_Object((1,3,6,1,4,1,232,4,2,4,4),_CpqSmCommRemoteSessionStatus_Type())
cpqSmCommRemoteSessionStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqSmCommRemoteSessionStatus.setStatus(_A)
class _CpqSmCommCallbackStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_D,1),(_G,2),(_H,3)))
_CpqSmCommCallbackStatus_Type.__name__=_C
_CpqSmCommCallbackStatus_Object=MibScalar
cpqSmCommCallbackStatus=_CpqSmCommCallbackStatus_Object((1,3,6,1,4,1,232,4,2,4,5),_CpqSmCommCallbackStatus_Type())
cpqSmCommCallbackStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqSmCommCallbackStatus.setStatus(_A)
_CpqSmModemSettingsTable_Object=MibTable
cpqSmModemSettingsTable=_CpqSmModemSettingsTable_Object((1,3,6,1,4,1,232,4,2,4,6))
if mibBuilder.loadTexts:cpqSmModemSettingsTable.setStatus(_A)
_CpqSmModemSettingsEntry_Object=MibTableRow
cpqSmModemSettingsEntry=_CpqSmModemSettingsEntry_Object((1,3,6,1,4,1,232,4,2,4,6,1))
cpqSmModemSettingsEntry.setIndexNames((0,_E,_Q))
if mibBuilder.loadTexts:cpqSmModemSettingsEntry.setStatus(_A)
class _CpqSmModemSettingsIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(48,49,50)));namedValues=NamedValues(*(('internalModem',48),('externalModem',49),('pager',50)))
_CpqSmModemSettingsIndex_Type.__name__=_C
_CpqSmModemSettingsIndex_Object=MibTableColumn
cpqSmModemSettingsIndex=_CpqSmModemSettingsIndex_Object((1,3,6,1,4,1,232,4,2,4,6,1,1),_CpqSmModemSettingsIndex_Type())
cpqSmModemSettingsIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqSmModemSettingsIndex.setStatus(_A)
class _CpqSmModemSettingsStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8)));namedValues=NamedValues(*((_D,1),('noInternalModem',2),('internalUSModem',3),('internalIntnlModem',4),('serialPortNotSetup',5),('serialDirectConnect',6),('serialExternalModem',7),('pagerInformationData',8)))
_CpqSmModemSettingsStatus_Type.__name__=_C
_CpqSmModemSettingsStatus_Object=MibTableColumn
cpqSmModemSettingsStatus=_CpqSmModemSettingsStatus_Object((1,3,6,1,4,1,232,4,2,4,6,1,2),_CpqSmModemSettingsStatus_Type())
cpqSmModemSettingsStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqSmModemSettingsStatus.setStatus(_A)
class _CpqSmModemSettingsBaudRate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_CpqSmModemSettingsBaudRate_Type.__name__=_C
_CpqSmModemSettingsBaudRate_Object=MibTableColumn
cpqSmModemSettingsBaudRate=_CpqSmModemSettingsBaudRate_Object((1,3,6,1,4,1,232,4,2,4,6,1,3),_CpqSmModemSettingsBaudRate_Type())
cpqSmModemSettingsBaudRate.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqSmModemSettingsBaudRate.setStatus(_A)
class _CpqSmModemSettingsParity_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_D,1),('none',2),('odd',3),('even',4)))
_CpqSmModemSettingsParity_Type.__name__=_C
_CpqSmModemSettingsParity_Object=MibTableColumn
cpqSmModemSettingsParity=_CpqSmModemSettingsParity_Object((1,3,6,1,4,1,232,4,2,4,6,1,4),_CpqSmModemSettingsParity_Type())
cpqSmModemSettingsParity.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqSmModemSettingsParity.setStatus(_A)
class _CpqSmModemSettingsDataLength_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_CpqSmModemSettingsDataLength_Type.__name__=_C
_CpqSmModemSettingsDataLength_Object=MibTableColumn
cpqSmModemSettingsDataLength=_CpqSmModemSettingsDataLength_Object((1,3,6,1,4,1,232,4,2,4,6,1,5),_CpqSmModemSettingsDataLength_Type())
cpqSmModemSettingsDataLength.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqSmModemSettingsDataLength.setStatus(_A)
class _CpqSmModemSettingsStopBits_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2))
_CpqSmModemSettingsStopBits_Type.__name__=_C
_CpqSmModemSettingsStopBits_Object=MibTableColumn
cpqSmModemSettingsStopBits=_CpqSmModemSettingsStopBits_Object((1,3,6,1,4,1,232,4,2,4,6,1,6),_CpqSmModemSettingsStopBits_Type())
cpqSmModemSettingsStopBits.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqSmModemSettingsStopBits.setStatus(_A)
class _CpqSmModemSettingsDialString_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,24))
_CpqSmModemSettingsDialString_Type.__name__=_F
_CpqSmModemSettingsDialString_Object=MibTableColumn
cpqSmModemSettingsDialString=_CpqSmModemSettingsDialString_Object((1,3,6,1,4,1,232,4,2,4,6,1,7),_CpqSmModemSettingsDialString_Type())
cpqSmModemSettingsDialString.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqSmModemSettingsDialString.setStatus(_A)
class _CpqSmModemSettingsHangUpString_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,24))
_CpqSmModemSettingsHangUpString_Type.__name__=_F
_CpqSmModemSettingsHangUpString_Object=MibTableColumn
cpqSmModemSettingsHangUpString=_CpqSmModemSettingsHangUpString_Object((1,3,6,1,4,1,232,4,2,4,6,1,8),_CpqSmModemSettingsHangUpString_Type())
cpqSmModemSettingsHangUpString.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqSmModemSettingsHangUpString.setStatus(_A)
class _CpqSmModemSettingsAnswerString_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,24))
_CpqSmModemSettingsAnswerString_Type.__name__=_F
_CpqSmModemSettingsAnswerString_Object=MibTableColumn
cpqSmModemSettingsAnswerString=_CpqSmModemSettingsAnswerString_Object((1,3,6,1,4,1,232,4,2,4,6,1,9),_CpqSmModemSettingsAnswerString_Type())
cpqSmModemSettingsAnswerString.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqSmModemSettingsAnswerString.setStatus(_A)
class _CpqSmModemSettingsOriginateString_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,24))
_CpqSmModemSettingsOriginateString_Type.__name__=_F
_CpqSmModemSettingsOriginateString_Object=MibTableColumn
cpqSmModemSettingsOriginateString=_CpqSmModemSettingsOriginateString_Object((1,3,6,1,4,1,232,4,2,4,6,1,10),_CpqSmModemSettingsOriginateString_Type())
cpqSmModemSettingsOriginateString.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqSmModemSettingsOriginateString.setStatus(_A)
_CpqSmAlert_ObjectIdentity=ObjectIdentity
cpqSmAlert=_CpqSmAlert_ObjectIdentity((1,3,6,1,4,1,232,4,2,5))
class _CpqSmAlertStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_D,1),(_G,2),(_H,3)))
_CpqSmAlertStatus_Type.__name__=_C
_CpqSmAlertStatus_Object=MibScalar
cpqSmAlertStatus=_CpqSmAlertStatus_Object((1,3,6,1,4,1,232,4,2,5,1),_CpqSmAlertStatus_Type())
cpqSmAlertStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqSmAlertStatus.setStatus(_A)
_CpqSmAlertDestTable_Object=MibTable
cpqSmAlertDestTable=_CpqSmAlertDestTable_Object((1,3,6,1,4,1,232,4,2,5,2))
if mibBuilder.loadTexts:cpqSmAlertDestTable.setStatus(_A)
_CpqSmAlertDestEntry_Object=MibTableRow
cpqSmAlertDestEntry=_CpqSmAlertDestEntry_Object((1,3,6,1,4,1,232,4,2,5,2,1))
cpqSmAlertDestEntry.setIndexNames((0,_E,_R))
if mibBuilder.loadTexts:cpqSmAlertDestEntry.setStatus(_A)
class _CpqSmAlertDestPriorityIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_CpqSmAlertDestPriorityIndex_Type.__name__=_C
_CpqSmAlertDestPriorityIndex_Object=MibTableColumn
cpqSmAlertDestPriorityIndex=_CpqSmAlertDestPriorityIndex_Object((1,3,6,1,4,1,232,4,2,5,2,1,1),_CpqSmAlertDestPriorityIndex_Type())
cpqSmAlertDestPriorityIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqSmAlertDestPriorityIndex.setStatus(_A)
class _CpqSmAlertDestType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,161,162,163,164,165,166)));namedValues=NamedValues(*((_D,1),('internalModemToSmf',161),('internalModemToPager',162),('internalModemToVoice',163),('externalModemToSmf',164),('externalModemToPager',165),('externalDirectToSmf',166)))
_CpqSmAlertDestType_Type.__name__=_C
_CpqSmAlertDestType_Object=MibTableColumn
cpqSmAlertDestType=_CpqSmAlertDestType_Object((1,3,6,1,4,1,232,4,2,5,2,1,2),_CpqSmAlertDestType_Type())
cpqSmAlertDestType.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqSmAlertDestType.setStatus(_A)
class _CpqSmAlertDestRetries_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,31))
_CpqSmAlertDestRetries_Type.__name__=_C
_CpqSmAlertDestRetries_Object=MibTableColumn
cpqSmAlertDestRetries=_CpqSmAlertDestRetries_Object((1,3,6,1,4,1,232,4,2,5,2,1,3),_CpqSmAlertDestRetries_Type())
cpqSmAlertDestRetries.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqSmAlertDestRetries.setStatus(_A)
class _CpqSmAlertDestConnectFlags_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_D,1),('alertOnly',2),('callbackOnly',3),('alertAndCallback',4)))
_CpqSmAlertDestConnectFlags_Type.__name__=_C
_CpqSmAlertDestConnectFlags_Object=MibTableColumn
cpqSmAlertDestConnectFlags=_CpqSmAlertDestConnectFlags_Object((1,3,6,1,4,1,232,4,2,5,2,1,4),_CpqSmAlertDestConnectFlags_Type())
cpqSmAlertDestConnectFlags.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqSmAlertDestConnectFlags.setStatus(_A)
class _CpqSmAlertDestPhoneNumber_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,24))
_CpqSmAlertDestPhoneNumber_Type.__name__=_F
_CpqSmAlertDestPhoneNumber_Object=MibTableColumn
cpqSmAlertDestPhoneNumber=_CpqSmAlertDestPhoneNumber_Object((1,3,6,1,4,1,232,4,2,5,2,1,5),_CpqSmAlertDestPhoneNumber_Type())
cpqSmAlertDestPhoneNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqSmAlertDestPhoneNumber.setStatus(_A)
class _CpqSmAlertDestTimeMask_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(21,21));fixedLength=21
_CpqSmAlertDestTimeMask_Type.__name__=_I
_CpqSmAlertDestTimeMask_Object=MibTableColumn
cpqSmAlertDestTimeMask=_CpqSmAlertDestTimeMask_Object((1,3,6,1,4,1,232,4,2,5,2,1,6),_CpqSmAlertDestTimeMask_Type())
cpqSmAlertDestTimeMask.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqSmAlertDestTimeMask.setStatus(_A)
class _CpqSmAlertDestPagerType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_D,1),('numericOnly',2),('alphanumeric',3)))
_CpqSmAlertDestPagerType_Type.__name__=_C
_CpqSmAlertDestPagerType_Object=MibTableColumn
cpqSmAlertDestPagerType=_CpqSmAlertDestPagerType_Object((1,3,6,1,4,1,232,4,2,5,2,1,7),_CpqSmAlertDestPagerType_Type())
cpqSmAlertDestPagerType.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqSmAlertDestPagerType.setStatus(_A)
class _CpqSmAlertDestPagerId_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,15))
_CpqSmAlertDestPagerId_Type.__name__=_F
_CpqSmAlertDestPagerId_Object=MibTableColumn
cpqSmAlertDestPagerId=_CpqSmAlertDestPagerId_Object((1,3,6,1,4,1,232,4,2,5,2,1,8),_CpqSmAlertDestPagerId_Type())
cpqSmAlertDestPagerId.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqSmAlertDestPagerId.setStatus(_A)
class _CpqSmAlertDestPagerDisplayLength_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,80))
_CpqSmAlertDestPagerDisplayLength_Type.__name__=_C
_CpqSmAlertDestPagerDisplayLength_Object=MibTableColumn
cpqSmAlertDestPagerDisplayLength=_CpqSmAlertDestPagerDisplayLength_Object((1,3,6,1,4,1,232,4,2,5,2,1,9),_CpqSmAlertDestPagerDisplayLength_Type())
cpqSmAlertDestPagerDisplayLength.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqSmAlertDestPagerDisplayLength.setStatus(_A)
_CpqSmTrap_ObjectIdentity=ObjectIdentity
cpqSmTrap=_CpqSmTrap_ObjectIdentity((1,3,6,1,4,1,232,4,3))
_CpqSmTrapPkts_Type=Counter32
_CpqSmTrapPkts_Object=MibScalar
cpqSmTrapPkts=_CpqSmTrapPkts_Object((1,3,6,1,4,1,232,4,3,1),_CpqSmTrapPkts_Type())
cpqSmTrapPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqSmTrapPkts.setStatus(_A)
class _CpqSmTrapLogMaxSize_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_CpqSmTrapLogMaxSize_Type.__name__=_C
_CpqSmTrapLogMaxSize_Object=MibScalar
cpqSmTrapLogMaxSize=_CpqSmTrapLogMaxSize_Object((1,3,6,1,4,1,232,4,3,2),_CpqSmTrapLogMaxSize_Type())
cpqSmTrapLogMaxSize.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqSmTrapLogMaxSize.setStatus(_A)
_CpqSmTrapLogTable_Object=MibTable
cpqSmTrapLogTable=_CpqSmTrapLogTable_Object((1,3,6,1,4,1,232,4,3,3))
if mibBuilder.loadTexts:cpqSmTrapLogTable.setStatus(_A)
_CpqSmTrapLogEntry_Object=MibTableRow
cpqSmTrapLogEntry=_CpqSmTrapLogEntry_Object((1,3,6,1,4,1,232,4,3,3,1))
cpqSmTrapLogEntry.setIndexNames((0,_E,_S))
if mibBuilder.loadTexts:cpqSmTrapLogEntry.setStatus(_A)
class _CpqSmTrapLogIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_CpqSmTrapLogIndex_Type.__name__=_C
_CpqSmTrapLogIndex_Object=MibTableColumn
cpqSmTrapLogIndex=_CpqSmTrapLogIndex_Object((1,3,6,1,4,1,232,4,3,3,1,1),_CpqSmTrapLogIndex_Type())
cpqSmTrapLogIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqSmTrapLogIndex.setStatus(_A)
class _CpqSmTrapType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*((_T,1),(_U,2),(_V,3),(_W,4),(_X,5),(_Y,6),(_Z,7)))
_CpqSmTrapType_Type.__name__=_C
_CpqSmTrapType_Object=MibTableColumn
cpqSmTrapType=_CpqSmTrapType_Object((1,3,6,1,4,1,232,4,3,3,1,2),_CpqSmTrapType_Type())
cpqSmTrapType.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqSmTrapType.setStatus(_A)
class _CpqSmTrapTime_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(6,6));fixedLength=6
_CpqSmTrapTime_Type.__name__=_I
_CpqSmTrapTime_Object=MibTableColumn
cpqSmTrapTime=_CpqSmTrapTime_Object((1,3,6,1,4,1,232,4,3,3,1,3),_CpqSmTrapTime_Type())
cpqSmTrapTime.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqSmTrapTime.setStatus(_A)
cpqSmBoardFailed=NotificationType((1,3,6,1,4,1,232,4,0,1))
if mibBuilder.loadTexts:cpqSmBoardFailed.setStatus('')
cpqSmBoardReset=NotificationType((1,3,6,1,4,1,232,4,0,2))
if mibBuilder.loadTexts:cpqSmBoardReset.setStatus('')
cpqSmServerManagerAlert=NotificationType((1,3,6,1,4,1,232,4,0,3))
cpqSmServerManagerAlert.setObjects(*((_E,_a),(_E,_b),(_E,_c),(_E,_d),(_E,_e),(_E,_f),(_E,_g),(_E,_h),(_E,_i)))
if mibBuilder.loadTexts:cpqSmServerManagerAlert.setStatus('')
cpqSmCommFailed=NotificationType((1,3,6,1,4,1,232,4,0,4))
if mibBuilder.loadTexts:cpqSmCommFailed.setStatus('')
cpqSmBatteryFailed=NotificationType((1,3,6,1,4,1,232,4,0,5))
if mibBuilder.loadTexts:cpqSmBatteryFailed.setStatus('')
cpqSmBoardTimeout=NotificationType((1,3,6,1,4,1,232,4,0,6))
if mibBuilder.loadTexts:cpqSmBoardTimeout.setStatus('')
cpqSmAlertDestinationBlacklisted=NotificationType((1,3,6,1,4,1,232,4,0,7))
cpqSmAlertDestinationBlacklisted.setObjects(*((_E,_j),(_E,_k),(_E,_l)))
if mibBuilder.loadTexts:cpqSmAlertDestinationBlacklisted.setStatus('')
mibBuilder.exportSymbols(_E,**{'cpqServerManager':cpqServerManager,_T:cpqSmBoardFailed,_U:cpqSmBoardReset,_V:cpqSmServerManagerAlert,_W:cpqSmCommFailed,_X:cpqSmBatteryFailed,_Y:cpqSmBoardTimeout,_Z:cpqSmAlertDestinationBlacklisted,'cpqSmMibRev':cpqSmMibRev,'cpqSmMibRevMajor':cpqSmMibRevMajor,'cpqSmMibRevMinor':cpqSmMibRevMinor,'cpqSmComponent':cpqSmComponent,'cpqSmInterface':cpqSmInterface,'cpqSmOsNetWare3x':cpqSmOsNetWare3x,'cpqSmNw3xDriverName':cpqSmNw3xDriverName,'cpqSmNw3xDriverDate':cpqSmNw3xDriverDate,'cpqSmNw3xDriverVersion':cpqSmNw3xDriverVersion,'cpqSmNw3xDriverIssuedCommands':cpqSmNw3xDriverIssuedCommands,'cpqSmNw3xDriverReceivedCommands':cpqSmNw3xDriverReceivedCommands,'cpqSmNw3xDriverWatchdogFrequency':cpqSmNw3xDriverWatchdogFrequency,'cpqSmNw3xDriverClockSyncFrequency':cpqSmNw3xDriverClockSyncFrequency,'cpqSmNw3xDriverIssuedWatchdogs':cpqSmNw3xDriverIssuedWatchdogs,'cpqSmNw3xDriverIssuedClockSyncs':cpqSmNw3xDriverIssuedClockSyncs,'cpqSmNw3xDriverMemoryAllocationFailedErrs':cpqSmNw3xDriverMemoryAllocationFailedErrs,'cpqSmNw3xDriverBoardResets':cpqSmNw3xDriverBoardResets,'cpqSmNw3xBoardState':cpqSmNw3xBoardState,'cpqSmCntlr':cpqSmCntlr,'cpqSmCntlrBoardName':cpqSmCntlrBoardName,'cpqSmCntlrBoardId':cpqSmCntlrBoardId,'cpqSmCntlrRomDate':cpqSmCntlrRomDate,'cpqSmCntlrCountryCode':cpqSmCntlrCountryCode,'cpqSmCntlrVoiceRomStatus':cpqSmCntlrVoiceRomStatus,'cpqSmCntlrBatteryStatus':cpqSmCntlrBatteryStatus,'cpqSmCntlrDormantModeStatus':cpqSmCntlrDormantModeStatus,'cpqSmCntlrSelfTestErrorCode':cpqSmCntlrSelfTestErrorCode,'cpqSmCntlrOsId':cpqSmCntlrOsId,'cpqSmCntlrOsMajorRev':cpqSmCntlrOsMajorRev,'cpqSmCntlrOsMinorRev':cpqSmCntlrOsMinorRev,'cpqSmCntlrPostTimeout':cpqSmCntlrPostTimeout,'cpqSmCntlrCondition':cpqSmCntlrCondition,'cpqSmObjData':cpqSmObjData,'cpqSmObjDataTotalObjects':cpqSmObjDataTotalObjects,'cpqSmObjDataObjectTotalSpace':cpqSmObjDataObjectTotalSpace,'cpqSmObjDataObjectSpaceAvailable':cpqSmObjDataObjectSpaceAvailable,'cpqSmObjDataInnateMonitoringStatus':cpqSmObjDataInnateMonitoringStatus,'cpqSmObjectTable':cpqSmObjectTable,'cpqSmObjectEntry':cpqSmObjectEntry,_L:cpqSmObjectIndex,_M:cpqSmObjectInstIndex,'cpqSmObjectClass':cpqSmObjectClass,_b:cpqSmObjectLabel,'cpqSmMonItemTable':cpqSmMonItemTable,'cpqSmMonItemEntry':cpqSmMonItemEntry,_N:cpqSmMonItemObjIndex,_O:cpqSmMonItemInstIndex,_P:cpqSmMonItemIndex,'cpqSmMonItemOnNetAlertStatus':cpqSmMonItemOnNetAlertStatus,'cpqSmMonItemRemoteAlertStatus':cpqSmMonItemRemoteAlertStatus,'cpqSmMonItemInnateStatus':cpqSmMonItemInnateStatus,'cpqSmMonItemHostNotify':cpqSmMonItemHostNotify,_h:cpqSmMonItemLogicalOperator,_e:cpqSmMonItemSeverity,_d:cpqSmMonItemDataType,'cpqSmMonItemVoiceMsgNum':cpqSmMonItemVoiceMsgNum,_c:cpqSmMonItemLabel,_f:cpqSmMonItemLimit,_g:cpqSmMonItemOptional,'cpqSmMonItemDefVal':cpqSmMonItemDefVal,_a:cpqSmMonItemCurVal,'cpqSmMonItemCurString':cpqSmMonItemCurString,'cpqSmMonItemCurContents':cpqSmMonItemCurContents,_i:cpqSmMonItemTimeStamp,'cpqSmAsyncComm':cpqSmAsyncComm,'cpqSmCommAsyncCommunicationStatus':cpqSmCommAsyncCommunicationStatus,'cpqSmCommInternalModemMaxBaudRate':cpqSmCommInternalModemMaxBaudRate,'cpqSmCommAudibleIndicatorStatus':cpqSmCommAudibleIndicatorStatus,'cpqSmCommRemoteSessionStatus':cpqSmCommRemoteSessionStatus,'cpqSmCommCallbackStatus':cpqSmCommCallbackStatus,'cpqSmModemSettingsTable':cpqSmModemSettingsTable,'cpqSmModemSettingsEntry':cpqSmModemSettingsEntry,_Q:cpqSmModemSettingsIndex,'cpqSmModemSettingsStatus':cpqSmModemSettingsStatus,'cpqSmModemSettingsBaudRate':cpqSmModemSettingsBaudRate,'cpqSmModemSettingsParity':cpqSmModemSettingsParity,'cpqSmModemSettingsDataLength':cpqSmModemSettingsDataLength,'cpqSmModemSettingsStopBits':cpqSmModemSettingsStopBits,'cpqSmModemSettingsDialString':cpqSmModemSettingsDialString,'cpqSmModemSettingsHangUpString':cpqSmModemSettingsHangUpString,'cpqSmModemSettingsAnswerString':cpqSmModemSettingsAnswerString,'cpqSmModemSettingsOriginateString':cpqSmModemSettingsOriginateString,'cpqSmAlert':cpqSmAlert,'cpqSmAlertStatus':cpqSmAlertStatus,'cpqSmAlertDestTable':cpqSmAlertDestTable,'cpqSmAlertDestEntry':cpqSmAlertDestEntry,_R:cpqSmAlertDestPriorityIndex,_j:cpqSmAlertDestType,'cpqSmAlertDestRetries':cpqSmAlertDestRetries,'cpqSmAlertDestConnectFlags':cpqSmAlertDestConnectFlags,_k:cpqSmAlertDestPhoneNumber,'cpqSmAlertDestTimeMask':cpqSmAlertDestTimeMask,'cpqSmAlertDestPagerType':cpqSmAlertDestPagerType,_l:cpqSmAlertDestPagerId,'cpqSmAlertDestPagerDisplayLength':cpqSmAlertDestPagerDisplayLength,'cpqSmTrap':cpqSmTrap,'cpqSmTrapPkts':cpqSmTrapPkts,'cpqSmTrapLogMaxSize':cpqSmTrapLogMaxSize,'cpqSmTrapLogTable':cpqSmTrapLogTable,'cpqSmTrapLogEntry':cpqSmTrapLogEntry,_S:cpqSmTrapLogIndex,'cpqSmTrapType':cpqSmTrapType,'cpqSmTrapTime':cpqSmTrapTime})