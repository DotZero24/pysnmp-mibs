_Z='slSonetApsEnable'
_Y='slSonetApsLineFailureCodeStatus'
_X='slSonetApsLineSwitchReason'
_W='slSonetApsActiveLineRx'
_V='slSonetApsLockOut'
_U='slSonetApsRemoteRequest'
_T='slSonetApsForceSwitch'
_S='slSonetApsSignalFailure'
_R='slSonetApsSignalDegrade'
_Q='slSonetApsManual'
_P='slSonetApsOther'
_O='biDirectional'
_N='uniDirectional'
_M='slSonetApsProtectionLine'
_L='slSonetApsWorkingLine'
_K='oneToOne'
_J='onePlusOne'
_I='Unsigned32'
_H='slSonetApsRevertive'
_G='Bits'
_F='slSonetApsWorkingIndex'
_E='read-create'
_D='SL-SONET-APS-MIB'
_C='read-only'
_B='Integer32'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
InterfaceIndex,=mibBuilder.importSymbols('IF-MIB','InterfaceIndex')
PerfCurrentCount,PerfIntervalCount,PerfTotalCount=mibBuilder.importSymbols('PerfHist-TC-MIB','PerfCurrentCount','PerfIntervalCount','PerfTotalCount')
slSonetMib,=mibBuilder.importSymbols('SL-SONET-MIB','slSonetMib')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI',_G,'Counter32','Counter64','Gauge32',_B,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_I,'iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention','TruthValue')
slSonetApsMib=ModuleIdentity((1,3,6,1,4,1,4515,1,6,5))
_SlSonetApsConfig_ObjectIdentity=ObjectIdentity
slSonetApsConfig=_SlSonetApsConfig_ObjectIdentity((1,3,6,1,4,1,4515,1,6,5,1))
_SlSonetApsConfigTable_Object=MibTable
slSonetApsConfigTable=_SlSonetApsConfigTable_Object((1,3,6,1,4,1,4515,1,6,5,1,1))
if mibBuilder.loadTexts:slSonetApsConfigTable.setStatus(_A)
_SlSonetApsConfigEntry_Object=MibTableRow
slSonetApsConfigEntry=_SlSonetApsConfigEntry_Object((1,3,6,1,4,1,4515,1,6,5,1,1,1))
slSonetApsConfigEntry.setIndexNames((0,_D,_F))
if mibBuilder.loadTexts:slSonetApsConfigEntry.setStatus(_A)
_SlSonetApsWorkingIndex_Type=InterfaceIndex
_SlSonetApsWorkingIndex_Object=MibTableColumn
slSonetApsWorkingIndex=_SlSonetApsWorkingIndex_Object((1,3,6,1,4,1,4515,1,6,5,1,1,1,1),_SlSonetApsWorkingIndex_Type())
slSonetApsWorkingIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:slSonetApsWorkingIndex.setStatus(_A)
_SlSonetApsProtectionIndex_Type=InterfaceIndex
_SlSonetApsProtectionIndex_Object=MibTableColumn
slSonetApsProtectionIndex=_SlSonetApsProtectionIndex_Object((1,3,6,1,4,1,4515,1,6,5,1,1,1,2),_SlSonetApsProtectionIndex_Type())
slSonetApsProtectionIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:slSonetApsProtectionIndex.setStatus(_A)
class _SlSonetApsEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('slSonetApsDisabled',1),('slSonetApsEnabled',2)))
_SlSonetApsEnable_Type.__name__=_B
_SlSonetApsEnable_Object=MibTableColumn
slSonetApsEnable=_SlSonetApsEnable_Object((1,3,6,1,4,1,4515,1,6,5,1,1,1,3),_SlSonetApsEnable_Type())
slSonetApsEnable.setMaxAccess(_E)
if mibBuilder.loadTexts:slSonetApsEnable.setStatus(_A)
class _SlSonetApsArchMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_J,1),(_K,2)))
_SlSonetApsArchMode_Type.__name__=_B
_SlSonetApsArchMode_Object=MibTableColumn
slSonetApsArchMode=_SlSonetApsArchMode_Object((1,3,6,1,4,1,4515,1,6,5,1,1,1,4),_SlSonetApsArchMode_Type())
slSonetApsArchMode.setMaxAccess(_E)
if mibBuilder.loadTexts:slSonetApsArchMode.setStatus(_A)
class _SlSonetApsActiveLineRx_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_L,1),(_M,2)))
_SlSonetApsActiveLineRx_Type.__name__=_B
_SlSonetApsActiveLineRx_Object=MibTableColumn
slSonetApsActiveLineRx=_SlSonetApsActiveLineRx_Object((1,3,6,1,4,1,4515,1,6,5,1,1,1,5),_SlSonetApsActiveLineRx_Type())
slSonetApsActiveLineRx.setMaxAccess(_C)
if mibBuilder.loadTexts:slSonetApsActiveLineRx.setStatus(_A)
class _SlSonetApsActiveLineTx_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_L,1),(_M,2)))
_SlSonetApsActiveLineTx_Type.__name__=_B
_SlSonetApsActiveLineTx_Object=MibTableColumn
slSonetApsActiveLineTx=_SlSonetApsActiveLineTx_Object((1,3,6,1,4,1,4515,1,6,5,1,1,1,6),_SlSonetApsActiveLineTx_Type())
slSonetApsActiveLineTx.setMaxAccess(_C)
if mibBuilder.loadTexts:slSonetApsActiveLineTx.setStatus(_A)
class _SlSonetApsWaitToRestore_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,12))
_SlSonetApsWaitToRestore_Type.__name__=_I
_SlSonetApsWaitToRestore_Object=MibTableColumn
slSonetApsWaitToRestore=_SlSonetApsWaitToRestore_Object((1,3,6,1,4,1,4515,1,6,5,1,1,1,7),_SlSonetApsWaitToRestore_Type())
slSonetApsWaitToRestore.setMaxAccess(_E)
if mibBuilder.loadTexts:slSonetApsWaitToRestore.setStatus(_A)
if mibBuilder.loadTexts:slSonetApsWaitToRestore.setUnits('minutes')
class _SlSonetApsDirection_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_N,1),(_O,2)))
_SlSonetApsDirection_Type.__name__=_B
_SlSonetApsDirection_Object=MibTableColumn
slSonetApsDirection=_SlSonetApsDirection_Object((1,3,6,1,4,1,4515,1,6,5,1,1,1,8),_SlSonetApsDirection_Type())
slSonetApsDirection.setMaxAccess(_E)
if mibBuilder.loadTexts:slSonetApsDirection.setStatus(_A)
class _SlSonetApsRevertive_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('nonrevertive',1),('revertive',2)))
_SlSonetApsRevertive_Type.__name__=_B
_SlSonetApsRevertive_Object=MibTableColumn
slSonetApsRevertive=_SlSonetApsRevertive_Object((1,3,6,1,4,1,4515,1,6,5,1,1,1,9),_SlSonetApsRevertive_Type())
slSonetApsRevertive.setMaxAccess(_E)
if mibBuilder.loadTexts:slSonetApsRevertive.setStatus(_A)
class _SlSonetApsDirectionOperational_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_N,1),(_O,2)))
_SlSonetApsDirectionOperational_Type.__name__=_B
_SlSonetApsDirectionOperational_Object=MibTableColumn
slSonetApsDirectionOperational=_SlSonetApsDirectionOperational_Object((1,3,6,1,4,1,4515,1,6,5,1,1,1,10),_SlSonetApsDirectionOperational_Type())
slSonetApsDirectionOperational.setMaxAccess(_C)
if mibBuilder.loadTexts:slSonetApsDirectionOperational.setStatus(_A)
class _SlSonetApsArchModeOperational_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_J,1),(_K,2)))
_SlSonetApsArchModeOperational_Type.__name__=_B
_SlSonetApsArchModeOperational_Object=MibTableColumn
slSonetApsArchModeOperational=_SlSonetApsArchModeOperational_Object((1,3,6,1,4,1,4515,1,6,5,1,1,1,11),_SlSonetApsArchModeOperational_Type())
slSonetApsArchModeOperational.setMaxAccess(_C)
if mibBuilder.loadTexts:slSonetApsArchModeOperational.setStatus(_A)
class _SlSonetApsChanStatus_Type(Bits):namedValues=NamedValues(*(('lockedOut',0),('sdWorking',1),('sdProtecting',2),('sfWorking',3),('sfProtecting',4),('switched',5),('remoteRequest',6)))
_SlSonetApsChanStatus_Type.__name__=_G
_SlSonetApsChanStatus_Object=MibTableColumn
slSonetApsChanStatus=_SlSonetApsChanStatus_Object((1,3,6,1,4,1,4515,1,6,5,1,1,1,12),_SlSonetApsChanStatus_Type())
slSonetApsChanStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:slSonetApsChanStatus.setStatus(_A)
_SlSonetApsChanSignalDegrades_Type=Counter32
_SlSonetApsChanSignalDegrades_Object=MibTableColumn
slSonetApsChanSignalDegrades=_SlSonetApsChanSignalDegrades_Object((1,3,6,1,4,1,4515,1,6,5,1,1,1,13),_SlSonetApsChanSignalDegrades_Type())
slSonetApsChanSignalDegrades.setMaxAccess(_C)
if mibBuilder.loadTexts:slSonetApsChanSignalDegrades.setStatus(_A)
_SlSonetApsChanSignalFailures_Type=Counter32
_SlSonetApsChanSignalFailures_Object=MibTableColumn
slSonetApsChanSignalFailures=_SlSonetApsChanSignalFailures_Object((1,3,6,1,4,1,4515,1,6,5,1,1,1,14),_SlSonetApsChanSignalFailures_Type())
slSonetApsChanSignalFailures.setMaxAccess(_C)
if mibBuilder.loadTexts:slSonetApsChanSignalFailures.setStatus(_A)
_SlSonetApsChanLastSwitchover_Type=TimeTicks
_SlSonetApsChanLastSwitchover_Object=MibTableColumn
slSonetApsChanLastSwitchover=_SlSonetApsChanLastSwitchover_Object((1,3,6,1,4,1,4515,1,6,5,1,1,1,15),_SlSonetApsChanLastSwitchover_Type())
slSonetApsChanLastSwitchover.setMaxAccess(_C)
if mibBuilder.loadTexts:slSonetApsChanLastSwitchover.setStatus(_A)
class _SlSonetApsLineFailureCodeStatus_Type(Bits):namedValues=NamedValues(*(('slSonetApsChannelMismatch',0),('slSonetApsProtectionByteFail',1),('slSonetApsFEProtectionFailure',2),('slSonetApsModeMismatch',3)))
_SlSonetApsLineFailureCodeStatus_Type.__name__=_G
_SlSonetApsLineFailureCodeStatus_Object=MibTableColumn
slSonetApsLineFailureCodeStatus=_SlSonetApsLineFailureCodeStatus_Object((1,3,6,1,4,1,4515,1,6,5,1,1,1,16),_SlSonetApsLineFailureCodeStatus_Type())
slSonetApsLineFailureCodeStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:slSonetApsLineFailureCodeStatus.setStatus(_A)
class _SlSonetApsConfigSwitchCommand_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*(('clear',1),('lockoutOfProtection',2),('forcedSwitchOfWorking',3),('forcedSwitchOfProtection',4),('manualSwitchOfWorking',5),('manualSwitchOfProtection',6),('exercise',7)))
_SlSonetApsConfigSwitchCommand_Type.__name__=_B
_SlSonetApsConfigSwitchCommand_Object=MibTableColumn
slSonetApsConfigSwitchCommand=_SlSonetApsConfigSwitchCommand_Object((1,3,6,1,4,1,4515,1,6,5,1,1,1,17),_SlSonetApsConfigSwitchCommand_Type())
slSonetApsConfigSwitchCommand.setMaxAccess(_E)
if mibBuilder.loadTexts:slSonetApsConfigSwitchCommand.setStatus(_A)
class _SlSonetApsLineSwitchReason_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8)));namedValues=NamedValues(*((_P,1),(_H,2),(_Q,3),(_R,4),(_S,5),(_T,6),(_U,7),(_V,8)))
_SlSonetApsLineSwitchReason_Type.__name__=_B
_SlSonetApsLineSwitchReason_Object=MibTableColumn
slSonetApsLineSwitchReason=_SlSonetApsLineSwitchReason_Object((1,3,6,1,4,1,4515,1,6,5,1,1,1,18),_SlSonetApsLineSwitchReason_Type())
slSonetApsLineSwitchReason.setMaxAccess(_C)
if mibBuilder.loadTexts:slSonetApsLineSwitchReason.setStatus(_A)
class _SlSonetApsResetCounters_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues(('resetCounters',1))
_SlSonetApsResetCounters_Type.__name__=_B
_SlSonetApsResetCounters_Object=MibTableColumn
slSonetApsResetCounters=_SlSonetApsResetCounters_Object((1,3,6,1,4,1,4515,1,6,5,1,1,1,19),_SlSonetApsResetCounters_Type())
slSonetApsResetCounters.setMaxAccess(_E)
if mibBuilder.loadTexts:slSonetApsResetCounters.setStatus(_A)
class _SlSonetApsConfigActiveRequest_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8)));namedValues=NamedValues(*((_P,1),(_H,2),(_Q,3),(_R,4),(_S,5),(_T,6),(_U,7),(_V,8)))
_SlSonetApsConfigActiveRequest_Type.__name__=_B
_SlSonetApsConfigActiveRequest_Object=MibTableColumn
slSonetApsConfigActiveRequest=_SlSonetApsConfigActiveRequest_Object((1,3,6,1,4,1,4515,1,6,5,1,1,1,20),_SlSonetApsConfigActiveRequest_Type())
slSonetApsConfigActiveRequest.setMaxAccess('read-write')
if mibBuilder.loadTexts:slSonetApsConfigActiveRequest.setStatus(_A)
_SlSonetApsConfigExerciseResult_Type=TruthValue
_SlSonetApsConfigExerciseResult_Object=MibTableColumn
slSonetApsConfigExerciseResult=_SlSonetApsConfigExerciseResult_Object((1,3,6,1,4,1,4515,1,6,5,1,1,1,21),_SlSonetApsConfigExerciseResult_Type())
slSonetApsConfigExerciseResult.setMaxAccess(_C)
if mibBuilder.loadTexts:slSonetApsConfigExerciseResult.setStatus(_A)
_SlSonetApsTraps_ObjectIdentity=ObjectIdentity
slSonetApsTraps=_SlSonetApsTraps_ObjectIdentity((1,3,6,1,4,1,4515,1,6,5,2))
slSonetApsTrapSwitchover=NotificationType((1,3,6,1,4,1,4515,1,6,5,2,1))
slSonetApsTrapSwitchover.setObjects(*((_D,_F),(_D,_W),(_D,_X)))
if mibBuilder.loadTexts:slSonetApsTrapSwitchover.setStatus(_A)
slSonetApsTrapFailureCodeChanged=NotificationType((1,3,6,1,4,1,4515,1,6,5,2,2))
slSonetApsTrapFailureCodeChanged.setObjects(*((_D,_F),(_D,_Y)))
if mibBuilder.loadTexts:slSonetApsTrapFailureCodeChanged.setStatus(_A)
slSonetApsTrapEnabled=NotificationType((1,3,6,1,4,1,4515,1,6,5,2,3))
slSonetApsTrapEnabled.setObjects(*((_D,_F),(_D,_Z)))
if mibBuilder.loadTexts:slSonetApsTrapEnabled.setStatus(_A)
mibBuilder.exportSymbols(_D,**{'slSonetApsMib':slSonetApsMib,'slSonetApsConfig':slSonetApsConfig,'slSonetApsConfigTable':slSonetApsConfigTable,'slSonetApsConfigEntry':slSonetApsConfigEntry,_F:slSonetApsWorkingIndex,'slSonetApsProtectionIndex':slSonetApsProtectionIndex,_Z:slSonetApsEnable,'slSonetApsArchMode':slSonetApsArchMode,_W:slSonetApsActiveLineRx,'slSonetApsActiveLineTx':slSonetApsActiveLineTx,'slSonetApsWaitToRestore':slSonetApsWaitToRestore,'slSonetApsDirection':slSonetApsDirection,_H:slSonetApsRevertive,'slSonetApsDirectionOperational':slSonetApsDirectionOperational,'slSonetApsArchModeOperational':slSonetApsArchModeOperational,'slSonetApsChanStatus':slSonetApsChanStatus,'slSonetApsChanSignalDegrades':slSonetApsChanSignalDegrades,'slSonetApsChanSignalFailures':slSonetApsChanSignalFailures,'slSonetApsChanLastSwitchover':slSonetApsChanLastSwitchover,_Y:slSonetApsLineFailureCodeStatus,'slSonetApsConfigSwitchCommand':slSonetApsConfigSwitchCommand,_X:slSonetApsLineSwitchReason,'slSonetApsResetCounters':slSonetApsResetCounters,'slSonetApsConfigActiveRequest':slSonetApsConfigActiveRequest,'slSonetApsConfigExerciseResult':slSonetApsConfigExerciseResult,'slSonetApsTraps':slSonetApsTraps,'slSonetApsTrapSwitchover':slSonetApsTrapSwitchover,'slSonetApsTrapFailureCodeChanged':slSonetApsTrapFailureCodeChanged,'slSonetApsTrapEnabled':slSonetApsTrapEnabled})