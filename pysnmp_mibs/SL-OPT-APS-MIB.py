_R='optApsLockOut'
_Q='optApsForceSwitch'
_P='optApsSignalFailure'
_O='optApsManual'
_N='optApsRevertive'
_M='optApsOther'
_L='optApsProtectionConnection'
_K='optApsWorkingConnection'
_J='Unsigned32'
_I='slmTrapLogId'
_H='SL-MAIN-MIB'
_G='optApsConfigActiveConnectionRx'
_F='optApsConfigUserWorkingIndex'
_E='read-only'
_D='SL-OPT-APS-MIB'
_C='read-create'
_B='Integer32'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
InterfaceIndex,=mibBuilder.importSymbols('IF-MIB','InterfaceIndex')
PerfCurrentCount,PerfIntervalCount,PerfTotalCount=mibBuilder.importSymbols('PerfHist-TC-MIB','PerfCurrentCount','PerfIntervalCount','PerfTotalCount')
slmTrapLogId,=mibBuilder.importSymbols(_H,_I)
sitelight,=mibBuilder.importSymbols('SL-NE-MIB','sitelight')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_B,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_J,'iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention','TruthValue')
slOptApsMib=ModuleIdentity((1,3,6,1,4,1,4515,1,11))
_SlOptApsConfig_ObjectIdentity=ObjectIdentity
slOptApsConfig=_SlOptApsConfig_ObjectIdentity((1,3,6,1,4,1,4515,1,11,1))
_OptApsConfigTable_Object=MibTable
optApsConfigTable=_OptApsConfigTable_Object((1,3,6,1,4,1,4515,1,11,1,1))
if mibBuilder.loadTexts:optApsConfigTable.setStatus(_A)
_OptApsConfigEntry_Object=MibTableRow
optApsConfigEntry=_OptApsConfigEntry_Object((1,3,6,1,4,1,4515,1,11,1,1,1))
optApsConfigEntry.setIndexNames((0,_D,_F))
if mibBuilder.loadTexts:optApsConfigEntry.setStatus(_A)
_OptApsConfigUserWorkingIndex_Type=InterfaceIndex
_OptApsConfigUserWorkingIndex_Object=MibTableColumn
optApsConfigUserWorkingIndex=_OptApsConfigUserWorkingIndex_Object((1,3,6,1,4,1,4515,1,11,1,1,1,1),_OptApsConfigUserWorkingIndex_Type())
optApsConfigUserWorkingIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:optApsConfigUserWorkingIndex.setStatus(_A)
_OptApsConfigNetWorkingIndex_Type=InterfaceIndex
_OptApsConfigNetWorkingIndex_Object=MibTableColumn
optApsConfigNetWorkingIndex=_OptApsConfigNetWorkingIndex_Object((1,3,6,1,4,1,4515,1,11,1,1,1,2),_OptApsConfigNetWorkingIndex_Type())
optApsConfigNetWorkingIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:optApsConfigNetWorkingIndex.setStatus(_A)
_OptApsConfigUserProtectingIndex_Type=InterfaceIndex
_OptApsConfigUserProtectingIndex_Object=MibTableColumn
optApsConfigUserProtectingIndex=_OptApsConfigUserProtectingIndex_Object((1,3,6,1,4,1,4515,1,11,1,1,1,3),_OptApsConfigUserProtectingIndex_Type())
optApsConfigUserProtectingIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:optApsConfigUserProtectingIndex.setStatus(_A)
_OptApsConfigNetProtectingIndex_Type=InterfaceIndex
_OptApsConfigNetProtectingIndex_Object=MibTableColumn
optApsConfigNetProtectingIndex=_OptApsConfigNetProtectingIndex_Object((1,3,6,1,4,1,4515,1,11,1,1,1,4),_OptApsConfigNetProtectingIndex_Type())
optApsConfigNetProtectingIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:optApsConfigNetProtectingIndex.setStatus(_A)
class _OptApsConfigScheme_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('equipment',1),('facility',2)))
_OptApsConfigScheme_Type.__name__=_B
_OptApsConfigScheme_Object=MibTableColumn
optApsConfigScheme=_OptApsConfigScheme_Object((1,3,6,1,4,1,4515,1,11,1,1,1,5),_OptApsConfigScheme_Type())
optApsConfigScheme.setMaxAccess(_C)
if mibBuilder.loadTexts:optApsConfigScheme.setStatus(_A)
class _OptApsConfigEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('optApsDisabled',1),('optApsEnabled',2)))
_OptApsConfigEnable_Type.__name__=_B
_OptApsConfigEnable_Object=MibTableColumn
optApsConfigEnable=_OptApsConfigEnable_Object((1,3,6,1,4,1,4515,1,11,1,1,1,6),_OptApsConfigEnable_Type())
optApsConfigEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:optApsConfigEnable.setStatus(_A)
class _OptApsConfigArchMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('onePlusOne',1),('oneToOne',2)))
_OptApsConfigArchMode_Type.__name__=_B
_OptApsConfigArchMode_Object=MibTableColumn
optApsConfigArchMode=_OptApsConfigArchMode_Object((1,3,6,1,4,1,4515,1,11,1,1,1,7),_OptApsConfigArchMode_Type())
optApsConfigArchMode.setMaxAccess(_C)
if mibBuilder.loadTexts:optApsConfigArchMode.setStatus(_A)
class _OptApsConfigActiveConnectionRx_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_K,1),(_L,2)))
_OptApsConfigActiveConnectionRx_Type.__name__=_B
_OptApsConfigActiveConnectionRx_Object=MibTableColumn
optApsConfigActiveConnectionRx=_OptApsConfigActiveConnectionRx_Object((1,3,6,1,4,1,4515,1,11,1,1,1,8),_OptApsConfigActiveConnectionRx_Type())
optApsConfigActiveConnectionRx.setMaxAccess(_E)
if mibBuilder.loadTexts:optApsConfigActiveConnectionRx.setStatus(_A)
class _OptApsConfigActiveConnectionTx_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_K,1),(_L,2)))
_OptApsConfigActiveConnectionTx_Type.__name__=_B
_OptApsConfigActiveConnectionTx_Object=MibTableColumn
optApsConfigActiveConnectionTx=_OptApsConfigActiveConnectionTx_Object((1,3,6,1,4,1,4515,1,11,1,1,1,9),_OptApsConfigActiveConnectionTx_Type())
optApsConfigActiveConnectionTx.setMaxAccess(_E)
if mibBuilder.loadTexts:optApsConfigActiveConnectionTx.setStatus(_A)
class _OptApsConfigWaitToRestore_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,12))
_OptApsConfigWaitToRestore_Type.__name__=_J
_OptApsConfigWaitToRestore_Object=MibTableColumn
optApsConfigWaitToRestore=_OptApsConfigWaitToRestore_Object((1,3,6,1,4,1,4515,1,11,1,1,1,10),_OptApsConfigWaitToRestore_Type())
optApsConfigWaitToRestore.setMaxAccess(_C)
if mibBuilder.loadTexts:optApsConfigWaitToRestore.setStatus(_A)
if mibBuilder.loadTexts:optApsConfigWaitToRestore.setUnits('minutes')
class _OptApsConfigDirection_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('uniDirectional',1),('biDirectional',2)))
_OptApsConfigDirection_Type.__name__=_B
_OptApsConfigDirection_Object=MibTableColumn
optApsConfigDirection=_OptApsConfigDirection_Object((1,3,6,1,4,1,4515,1,11,1,1,1,11),_OptApsConfigDirection_Type())
optApsConfigDirection.setMaxAccess(_C)
if mibBuilder.loadTexts:optApsConfigDirection.setStatus(_A)
class _OptApsConfigRevertive_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('nonrevertive',1),('revertive',2)))
_OptApsConfigRevertive_Type.__name__=_B
_OptApsConfigRevertive_Object=MibTableColumn
optApsConfigRevertive=_OptApsConfigRevertive_Object((1,3,6,1,4,1,4515,1,11,1,1,1,12),_OptApsConfigRevertive_Type())
optApsConfigRevertive.setMaxAccess(_C)
if mibBuilder.loadTexts:optApsConfigRevertive.setStatus(_A)
class _OptApsConfigChanStatus_Type(Bits):namedValues=NamedValues(*(('lockedOut',0),('sfWorking',1),('sfProtecting',2),('switched',3),('lockedOutRemote',4)))
_OptApsConfigChanStatus_Type.__name__='Bits'
_OptApsConfigChanStatus_Object=MibTableColumn
optApsConfigChanStatus=_OptApsConfigChanStatus_Object((1,3,6,1,4,1,4515,1,11,1,1,1,13),_OptApsConfigChanStatus_Type())
optApsConfigChanStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:optApsConfigChanStatus.setStatus(_A)
_OptApsConfigChanSignalFailures_Type=Counter32
_OptApsConfigChanSignalFailures_Object=MibTableColumn
optApsConfigChanSignalFailures=_OptApsConfigChanSignalFailures_Object((1,3,6,1,4,1,4515,1,11,1,1,1,14),_OptApsConfigChanSignalFailures_Type())
optApsConfigChanSignalFailures.setMaxAccess(_E)
if mibBuilder.loadTexts:optApsConfigChanSignalFailures.setStatus(_A)
_OptApsConfigChanSwitchovers_Type=Counter32
_OptApsConfigChanSwitchovers_Object=MibTableColumn
optApsConfigChanSwitchovers=_OptApsConfigChanSwitchovers_Object((1,3,6,1,4,1,4515,1,11,1,1,1,15),_OptApsConfigChanSwitchovers_Type())
optApsConfigChanSwitchovers.setMaxAccess(_E)
if mibBuilder.loadTexts:optApsConfigChanSwitchovers.setStatus(_A)
_OptApsConfigChanLastSwitchover_Type=TimeTicks
_OptApsConfigChanLastSwitchover_Object=MibTableColumn
optApsConfigChanLastSwitchover=_OptApsConfigChanLastSwitchover_Object((1,3,6,1,4,1,4515,1,11,1,1,1,16),_OptApsConfigChanLastSwitchover_Type())
optApsConfigChanLastSwitchover.setMaxAccess(_E)
if mibBuilder.loadTexts:optApsConfigChanLastSwitchover.setStatus(_A)
class _OptApsConfigSwitchCommand_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*(('clear',1),('lockoutOfProtection',2),('forcedSwitchOfWorking',3),('forcedSwitchOfProtection',4),('manualSwitchOfWorking',5),('manualSwitchOfProtection',6)))
_OptApsConfigSwitchCommand_Type.__name__=_B
_OptApsConfigSwitchCommand_Object=MibTableColumn
optApsConfigSwitchCommand=_OptApsConfigSwitchCommand_Object((1,3,6,1,4,1,4515,1,11,1,1,1,17),_OptApsConfigSwitchCommand_Type())
optApsConfigSwitchCommand.setMaxAccess(_C)
if mibBuilder.loadTexts:optApsConfigSwitchCommand.setStatus(_A)
class _OptApsConfigSwitchReason_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*((_M,1),(_N,2),(_O,3),(_P,4),(_Q,5),(_R,6)))
_OptApsConfigSwitchReason_Type.__name__=_B
_OptApsConfigSwitchReason_Object=MibTableColumn
optApsConfigSwitchReason=_OptApsConfigSwitchReason_Object((1,3,6,1,4,1,4515,1,11,1,1,1,18),_OptApsConfigSwitchReason_Type())
optApsConfigSwitchReason.setMaxAccess(_E)
if mibBuilder.loadTexts:optApsConfigSwitchReason.setStatus(_A)
class _OptApsConfigResetCounters_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues(('resetCounters',1))
_OptApsConfigResetCounters_Type.__name__=_B
_OptApsConfigResetCounters_Object=MibTableColumn
optApsConfigResetCounters=_OptApsConfigResetCounters_Object((1,3,6,1,4,1,4515,1,11,1,1,1,19),_OptApsConfigResetCounters_Type())
optApsConfigResetCounters.setMaxAccess(_C)
if mibBuilder.loadTexts:optApsConfigResetCounters.setStatus(_A)
class _OptApsConfigActiveRequest_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*((_M,1),(_N,2),(_O,3),(_P,4),(_Q,5),(_R,6)))
_OptApsConfigActiveRequest_Type.__name__=_B
_OptApsConfigActiveRequest_Object=MibTableColumn
optApsConfigActiveRequest=_OptApsConfigActiveRequest_Object((1,3,6,1,4,1,4515,1,11,1,1,1,20),_OptApsConfigActiveRequest_Type())
optApsConfigActiveRequest.setMaxAccess(_E)
if mibBuilder.loadTexts:optApsConfigActiveRequest.setStatus(_A)
_OptApsConfigStatus_Type=RowStatus
_OptApsConfigStatus_Object=MibTableColumn
optApsConfigStatus=_OptApsConfigStatus_Object((1,3,6,1,4,1,4515,1,11,1,1,1,21),_OptApsConfigStatus_Type())
optApsConfigStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:optApsConfigStatus.setStatus(_A)
class _OptApsConfigLosThreshold_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_OptApsConfigLosThreshold_Type.__name__=_B
_OptApsConfigLosThreshold_Object=MibTableColumn
optApsConfigLosThreshold=_OptApsConfigLosThreshold_Object((1,3,6,1,4,1,4515,1,11,1,1,1,22),_OptApsConfigLosThreshold_Type())
optApsConfigLosThreshold.setMaxAccess('read-write')
if mibBuilder.loadTexts:optApsConfigLosThreshold.setStatus(_A)
_SlOptApsTraps_ObjectIdentity=ObjectIdentity
slOptApsTraps=_SlOptApsTraps_ObjectIdentity((1,3,6,1,4,1,4515,1,11,2))
_SlOptApsTraps0_ObjectIdentity=ObjectIdentity
slOptApsTraps0=_SlOptApsTraps0_ObjectIdentity((1,3,6,1,4,1,4515,1,11,2,0))
optApsTrapSwitchover0=NotificationType((1,3,6,1,4,1,4515,1,11,2,0,1))
optApsTrapSwitchover0.setObjects(*((_D,_F),(_D,_G),(_H,_I)))
if mibBuilder.loadTexts:optApsTrapSwitchover0.setStatus(_A)
optApsConfigTableChanged0=NotificationType((1,3,6,1,4,1,4515,1,11,2,0,2))
optApsConfigTableChanged0.setObjects(*((_D,_F),(_D,_G),(_H,_I)))
if mibBuilder.loadTexts:optApsConfigTableChanged0.setStatus(_A)
optApsTrapSwitchover=NotificationType((1,3,6,1,4,1,4515,1,11,2,1))
optApsTrapSwitchover.setObjects(*((_D,_F),(_D,_G)))
if mibBuilder.loadTexts:optApsTrapSwitchover.setStatus(_A)
optApsConfigTableChanged=NotificationType((1,3,6,1,4,1,4515,1,11,2,2))
optApsConfigTableChanged.setObjects((_D,_F))
if mibBuilder.loadTexts:optApsConfigTableChanged.setStatus(_A)
mibBuilder.exportSymbols(_D,**{'slOptApsMib':slOptApsMib,'slOptApsConfig':slOptApsConfig,'optApsConfigTable':optApsConfigTable,'optApsConfigEntry':optApsConfigEntry,_F:optApsConfigUserWorkingIndex,'optApsConfigNetWorkingIndex':optApsConfigNetWorkingIndex,'optApsConfigUserProtectingIndex':optApsConfigUserProtectingIndex,'optApsConfigNetProtectingIndex':optApsConfigNetProtectingIndex,'optApsConfigScheme':optApsConfigScheme,'optApsConfigEnable':optApsConfigEnable,'optApsConfigArchMode':optApsConfigArchMode,_G:optApsConfigActiveConnectionRx,'optApsConfigActiveConnectionTx':optApsConfigActiveConnectionTx,'optApsConfigWaitToRestore':optApsConfigWaitToRestore,'optApsConfigDirection':optApsConfigDirection,'optApsConfigRevertive':optApsConfigRevertive,'optApsConfigChanStatus':optApsConfigChanStatus,'optApsConfigChanSignalFailures':optApsConfigChanSignalFailures,'optApsConfigChanSwitchovers':optApsConfigChanSwitchovers,'optApsConfigChanLastSwitchover':optApsConfigChanLastSwitchover,'optApsConfigSwitchCommand':optApsConfigSwitchCommand,'optApsConfigSwitchReason':optApsConfigSwitchReason,'optApsConfigResetCounters':optApsConfigResetCounters,'optApsConfigActiveRequest':optApsConfigActiveRequest,'optApsConfigStatus':optApsConfigStatus,'optApsConfigLosThreshold':optApsConfigLosThreshold,'slOptApsTraps':slOptApsTraps,'slOptApsTraps0':slOptApsTraps0,'optApsTrapSwitchover0':optApsTrapSwitchover0,'optApsConfigTableChanged0':optApsConfigTableChanged0,'optApsTrapSwitchover':optApsTrapSwitchover,'optApsConfigTableChanged':optApsConfigTableChanged})