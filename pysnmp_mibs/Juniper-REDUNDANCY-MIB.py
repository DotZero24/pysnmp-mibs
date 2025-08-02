_A4='juniRedundancyNotificationGroup'
_A3='juniRedundancyHistoryGroup'
_A2='juniRedundancyCfgGroup'
_A1='juniRedundancyStatusGroup'
_A0='juniLcRedundancyStateDisabledNotification'
_z='juniLcRedundancyStateEnabledNotification'
_y='juniLcRedundancySwitchoverNotification'
_x='juniRedundancyModeNotification'
_w='juniRedundancyStatePendingNotification'
_v='juniRedundancyStateDisabledNotification'
_u='juniRedundancyStateEnabledNotification'
_t='juniRedundancyWarmSwitchoverNotification'
_s='juniRedundancyColdSwitchoverNotification'
_r='juniLcRedundancySwitchoverTime'
_q='juniLcRedundancyLastResetReason'
_p='juniLcRedundancyActivationType'
_o='juniRedundancyHistoryWarmSwitchovers'
_n='juniRedundancyHistoryColdSwitchovers'
_m='juniRedundancyHistoryReloads'
_l='juniRedundancyHistoryActivationTime'
_k='juniRedundancyHistoryResetReason'
_j='juniRedundancyHistoryCurrActiveRelease'
_i='juniRedundancyHistoryCurrActiveSlot'
_h='juniRedundancyHistoryPrevActiveRelease'
_g='juniRedundancyHistoryPrevActiveSlot'
_f='juniRedundancyHistoryActivationType'
_e='juniRedundancyHistoryResetType'
_d='juniRedundancySystemActivationHistoryCommand'
_c='juniRedundancySystemActivationHistoryTableMaxLength'
_b='juniRedundancyNotifsEnabled'
_a='juniRedundancyHaActiveTime'
_Z='juniRedundancyLastSystemActivationType'
_Y='juniRedundancyLastSystemActivationTime'
_X='juniRedundancyStandbySlotState'
_W='juniRedundancyStandbySlot'
_V='juniRedundancyActiveSlotState'
_U='juniRedundancySystemActivationHistoryIndex'
_T='JuniRedundancyHistoryCommand'
_S='JuniRedundancyMode'
_R='warmSwitch'
_Q='coldSwitch'
_P='reload'
_O='userInitiated'
_N='TruthValue'
_M='juniLcRedundancyHaActiveTime'
_L='juniRedundancyCfgRedundancyMode'
_K='juniLcRedundancyStandbySlot'
_J='juniLcRedundancyActiveSlot'
_I='juniRedundancyLastResetReason'
_H='read-write'
_G='notKnown'
_F='accessible-for-notify'
_E='juniRedundancyActiveSlot'
_D='Integer32'
_C='read-only'
_B='current'
_A='Juniper-REDUNDANCY-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
juniMibs,=mibBuilder.importSymbols('Juniper-MIBs','juniMibs')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
sysUpTime,=mibBuilder.importSymbols('SNMPv2-MIB','sysUpTime')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DateAndTime,DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime','DisplayString','PhysAddress','RowStatus','TextualConvention',_N)
juniRedundancyMIB=ModuleIdentity((1,3,6,1,4,1,4874,2,2,74))
if mibBuilder.loadTexts:juniRedundancyMIB.setRevisions(('2010-03-19 12:31','2003-12-12 00:00'))
class JuniRedundancyState(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*((_G,1),('fileSystemSyncing',2),('disabled',3),('initializing',4),('pending',5),('active',6)))
class JuniRedundancyMode(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('fileSystemSynchronization',1),('highAvailability',2)))
class JuniRedundancyResetReason(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('none',1),(_G,2),(_O,3)))
class JuniRedundancySystemActivationType(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_P,1),(_Q,2),(_R,3)))
class JuniRedundancyResetType(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_G,1),('srpReload',2),('srpSwitchover',3),('linecardReload',4),('linecardSwitchover',5)))
class JuniRedundancyHistoryCommand(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('keep',1),('clear',2)))
class JuniLcRedundancySystemActivationType(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_P,1),(_Q,2),(_R,3)))
class JuniLcRedundancyResetReason(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('poweron',1),(_G,2),(_O,3),('hardware',4),('software',5)))
_JuniRedundancyNotifications_ObjectIdentity=ObjectIdentity
juniRedundancyNotifications=_JuniRedundancyNotifications_ObjectIdentity((1,3,6,1,4,1,4874,2,2,74,0))
_JuniRedundancyObjects_ObjectIdentity=ObjectIdentity
juniRedundancyObjects=_JuniRedundancyObjects_ObjectIdentity((1,3,6,1,4,1,4874,2,2,74,1))
_JuniRedundancyStatus_ObjectIdentity=ObjectIdentity
juniRedundancyStatus=_JuniRedundancyStatus_ObjectIdentity((1,3,6,1,4,1,4874,2,2,74,1,1))
class _JuniRedundancyActiveSlot_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_JuniRedundancyActiveSlot_Type.__name__=_D
_JuniRedundancyActiveSlot_Object=MibScalar
juniRedundancyActiveSlot=_JuniRedundancyActiveSlot_Object((1,3,6,1,4,1,4874,2,2,74,1,1,1),_JuniRedundancyActiveSlot_Type())
juniRedundancyActiveSlot.setMaxAccess(_C)
if mibBuilder.loadTexts:juniRedundancyActiveSlot.setStatus(_B)
_JuniRedundancyActiveSlotState_Type=JuniRedundancyState
_JuniRedundancyActiveSlotState_Object=MibScalar
juniRedundancyActiveSlotState=_JuniRedundancyActiveSlotState_Object((1,3,6,1,4,1,4874,2,2,74,1,1,2),_JuniRedundancyActiveSlotState_Type())
juniRedundancyActiveSlotState.setMaxAccess(_C)
if mibBuilder.loadTexts:juniRedundancyActiveSlotState.setStatus(_B)
class _JuniRedundancyStandbySlot_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_JuniRedundancyStandbySlot_Type.__name__=_D
_JuniRedundancyStandbySlot_Object=MibScalar
juniRedundancyStandbySlot=_JuniRedundancyStandbySlot_Object((1,3,6,1,4,1,4874,2,2,74,1,1,3),_JuniRedundancyStandbySlot_Type())
juniRedundancyStandbySlot.setMaxAccess(_C)
if mibBuilder.loadTexts:juniRedundancyStandbySlot.setStatus(_B)
_JuniRedundancyStandbySlotState_Type=JuniRedundancyState
_JuniRedundancyStandbySlotState_Object=MibScalar
juniRedundancyStandbySlotState=_JuniRedundancyStandbySlotState_Object((1,3,6,1,4,1,4874,2,2,74,1,1,4),_JuniRedundancyStandbySlotState_Type())
juniRedundancyStandbySlotState.setMaxAccess(_C)
if mibBuilder.loadTexts:juniRedundancyStandbySlotState.setStatus(_B)
_JuniRedundancyLastResetReason_Type=JuniRedundancyResetReason
_JuniRedundancyLastResetReason_Object=MibScalar
juniRedundancyLastResetReason=_JuniRedundancyLastResetReason_Object((1,3,6,1,4,1,4874,2,2,74,1,1,5),_JuniRedundancyLastResetReason_Type())
juniRedundancyLastResetReason.setMaxAccess(_C)
if mibBuilder.loadTexts:juniRedundancyLastResetReason.setStatus(_B)
_JuniRedundancyLastSystemActivationTime_Type=TimeTicks
_JuniRedundancyLastSystemActivationTime_Object=MibScalar
juniRedundancyLastSystemActivationTime=_JuniRedundancyLastSystemActivationTime_Object((1,3,6,1,4,1,4874,2,2,74,1,1,6),_JuniRedundancyLastSystemActivationTime_Type())
juniRedundancyLastSystemActivationTime.setMaxAccess(_C)
if mibBuilder.loadTexts:juniRedundancyLastSystemActivationTime.setStatus(_B)
_JuniRedundancyLastSystemActivationType_Type=JuniRedundancySystemActivationType
_JuniRedundancyLastSystemActivationType_Object=MibScalar
juniRedundancyLastSystemActivationType=_JuniRedundancyLastSystemActivationType_Object((1,3,6,1,4,1,4874,2,2,74,1,1,7),_JuniRedundancyLastSystemActivationType_Type())
juniRedundancyLastSystemActivationType.setMaxAccess(_C)
if mibBuilder.loadTexts:juniRedundancyLastSystemActivationType.setStatus(_B)
_JuniRedundancyHaActiveTime_Type=TimeTicks
_JuniRedundancyHaActiveTime_Object=MibScalar
juniRedundancyHaActiveTime=_JuniRedundancyHaActiveTime_Object((1,3,6,1,4,1,4874,2,2,74,1,1,8),_JuniRedundancyHaActiveTime_Type())
juniRedundancyHaActiveTime.setMaxAccess(_C)
if mibBuilder.loadTexts:juniRedundancyHaActiveTime.setStatus(_B)
_JuniRedundancyCfg_ObjectIdentity=ObjectIdentity
juniRedundancyCfg=_JuniRedundancyCfg_ObjectIdentity((1,3,6,1,4,1,4874,2,2,74,1,2))
class _JuniRedundancyNotifsEnabled_Type(TruthValue):defaultValue=1
_JuniRedundancyNotifsEnabled_Type.__name__=_N
_JuniRedundancyNotifsEnabled_Object=MibScalar
juniRedundancyNotifsEnabled=_JuniRedundancyNotifsEnabled_Object((1,3,6,1,4,1,4874,2,2,74,1,2,1),_JuniRedundancyNotifsEnabled_Type())
juniRedundancyNotifsEnabled.setMaxAccess(_H)
if mibBuilder.loadTexts:juniRedundancyNotifsEnabled.setStatus(_B)
class _JuniRedundancyCfgRedundancyMode_Type(JuniRedundancyMode):defaultValue=1
_JuniRedundancyCfgRedundancyMode_Type.__name__=_S
_JuniRedundancyCfgRedundancyMode_Object=MibScalar
juniRedundancyCfgRedundancyMode=_JuniRedundancyCfgRedundancyMode_Object((1,3,6,1,4,1,4874,2,2,74,1,2,2),_JuniRedundancyCfgRedundancyMode_Type())
juniRedundancyCfgRedundancyMode.setMaxAccess(_H)
if mibBuilder.loadTexts:juniRedundancyCfgRedundancyMode.setStatus(_B)
_JuniRedundancyHistory_ObjectIdentity=ObjectIdentity
juniRedundancyHistory=_JuniRedundancyHistory_ObjectIdentity((1,3,6,1,4,1,4874,2,2,74,1,3))
class _JuniRedundancySystemActivationHistoryTableMaxLength_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,50))
_JuniRedundancySystemActivationHistoryTableMaxLength_Type.__name__=_D
_JuniRedundancySystemActivationHistoryTableMaxLength_Object=MibScalar
juniRedundancySystemActivationHistoryTableMaxLength=_JuniRedundancySystemActivationHistoryTableMaxLength_Object((1,3,6,1,4,1,4874,2,2,74,1,3,1),_JuniRedundancySystemActivationHistoryTableMaxLength_Type())
juniRedundancySystemActivationHistoryTableMaxLength.setMaxAccess(_H)
if mibBuilder.loadTexts:juniRedundancySystemActivationHistoryTableMaxLength.setStatus(_B)
class _JuniRedundancySystemActivationHistoryCommand_Type(JuniRedundancyHistoryCommand):defaultValue=1
_JuniRedundancySystemActivationHistoryCommand_Type.__name__=_T
_JuniRedundancySystemActivationHistoryCommand_Object=MibScalar
juniRedundancySystemActivationHistoryCommand=_JuniRedundancySystemActivationHistoryCommand_Object((1,3,6,1,4,1,4874,2,2,74,1,3,2),_JuniRedundancySystemActivationHistoryCommand_Type())
juniRedundancySystemActivationHistoryCommand.setMaxAccess(_H)
if mibBuilder.loadTexts:juniRedundancySystemActivationHistoryCommand.setStatus(_B)
_JuniRedundancySystemActivationHistoryTable_Object=MibTable
juniRedundancySystemActivationHistoryTable=_JuniRedundancySystemActivationHistoryTable_Object((1,3,6,1,4,1,4874,2,2,74,1,3,3))
if mibBuilder.loadTexts:juniRedundancySystemActivationHistoryTable.setStatus(_B)
_JuniRedundancySystemActivationHistoryEntry_Object=MibTableRow
juniRedundancySystemActivationHistoryEntry=_JuniRedundancySystemActivationHistoryEntry_Object((1,3,6,1,4,1,4874,2,2,74,1,3,3,1))
juniRedundancySystemActivationHistoryEntry.setIndexNames((0,_A,_U))
if mibBuilder.loadTexts:juniRedundancySystemActivationHistoryEntry.setStatus(_B)
_JuniRedundancySystemActivationHistoryIndex_Type=Integer32
_JuniRedundancySystemActivationHistoryIndex_Object=MibTableColumn
juniRedundancySystemActivationHistoryIndex=_JuniRedundancySystemActivationHistoryIndex_Object((1,3,6,1,4,1,4874,2,2,74,1,3,3,1,1),_JuniRedundancySystemActivationHistoryIndex_Type())
juniRedundancySystemActivationHistoryIndex.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:juniRedundancySystemActivationHistoryIndex.setStatus(_B)
_JuniRedundancyHistoryResetType_Type=JuniRedundancyResetType
_JuniRedundancyHistoryResetType_Object=MibTableColumn
juniRedundancyHistoryResetType=_JuniRedundancyHistoryResetType_Object((1,3,6,1,4,1,4874,2,2,74,1,3,3,1,2),_JuniRedundancyHistoryResetType_Type())
juniRedundancyHistoryResetType.setMaxAccess(_C)
if mibBuilder.loadTexts:juniRedundancyHistoryResetType.setStatus(_B)
_JuniRedundancyHistoryActivationType_Type=JuniRedundancySystemActivationType
_JuniRedundancyHistoryActivationType_Object=MibTableColumn
juniRedundancyHistoryActivationType=_JuniRedundancyHistoryActivationType_Object((1,3,6,1,4,1,4874,2,2,74,1,3,3,1,3),_JuniRedundancyHistoryActivationType_Type())
juniRedundancyHistoryActivationType.setMaxAccess(_C)
if mibBuilder.loadTexts:juniRedundancyHistoryActivationType.setStatus(_B)
class _JuniRedundancyHistoryPrevActiveSlot_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_JuniRedundancyHistoryPrevActiveSlot_Type.__name__=_D
_JuniRedundancyHistoryPrevActiveSlot_Object=MibTableColumn
juniRedundancyHistoryPrevActiveSlot=_JuniRedundancyHistoryPrevActiveSlot_Object((1,3,6,1,4,1,4874,2,2,74,1,3,3,1,4),_JuniRedundancyHistoryPrevActiveSlot_Type())
juniRedundancyHistoryPrevActiveSlot.setMaxAccess(_C)
if mibBuilder.loadTexts:juniRedundancyHistoryPrevActiveSlot.setStatus(_B)
_JuniRedundancyHistoryPrevActiveRelease_Type=DisplayString
_JuniRedundancyHistoryPrevActiveRelease_Object=MibTableColumn
juniRedundancyHistoryPrevActiveRelease=_JuniRedundancyHistoryPrevActiveRelease_Object((1,3,6,1,4,1,4874,2,2,74,1,3,3,1,5),_JuniRedundancyHistoryPrevActiveRelease_Type())
juniRedundancyHistoryPrevActiveRelease.setMaxAccess(_C)
if mibBuilder.loadTexts:juniRedundancyHistoryPrevActiveRelease.setStatus(_B)
class _JuniRedundancyHistoryCurrActiveSlot_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_JuniRedundancyHistoryCurrActiveSlot_Type.__name__=_D
_JuniRedundancyHistoryCurrActiveSlot_Object=MibTableColumn
juniRedundancyHistoryCurrActiveSlot=_JuniRedundancyHistoryCurrActiveSlot_Object((1,3,6,1,4,1,4874,2,2,74,1,3,3,1,6),_JuniRedundancyHistoryCurrActiveSlot_Type())
juniRedundancyHistoryCurrActiveSlot.setMaxAccess(_C)
if mibBuilder.loadTexts:juniRedundancyHistoryCurrActiveSlot.setStatus(_B)
_JuniRedundancyHistoryCurrActiveRelease_Type=DisplayString
_JuniRedundancyHistoryCurrActiveRelease_Object=MibTableColumn
juniRedundancyHistoryCurrActiveRelease=_JuniRedundancyHistoryCurrActiveRelease_Object((1,3,6,1,4,1,4874,2,2,74,1,3,3,1,7),_JuniRedundancyHistoryCurrActiveRelease_Type())
juniRedundancyHistoryCurrActiveRelease.setMaxAccess(_C)
if mibBuilder.loadTexts:juniRedundancyHistoryCurrActiveRelease.setStatus(_B)
_JuniRedundancyHistoryResetReason_Type=JuniRedundancyResetReason
_JuniRedundancyHistoryResetReason_Object=MibTableColumn
juniRedundancyHistoryResetReason=_JuniRedundancyHistoryResetReason_Object((1,3,6,1,4,1,4874,2,2,74,1,3,3,1,8),_JuniRedundancyHistoryResetReason_Type())
juniRedundancyHistoryResetReason.setMaxAccess(_C)
if mibBuilder.loadTexts:juniRedundancyHistoryResetReason.setStatus(_B)
_JuniRedundancyHistoryActivationTime_Type=DateAndTime
_JuniRedundancyHistoryActivationTime_Object=MibTableColumn
juniRedundancyHistoryActivationTime=_JuniRedundancyHistoryActivationTime_Object((1,3,6,1,4,1,4874,2,2,74,1,3,3,1,9),_JuniRedundancyHistoryActivationTime_Type())
juniRedundancyHistoryActivationTime.setMaxAccess(_C)
if mibBuilder.loadTexts:juniRedundancyHistoryActivationTime.setStatus(_B)
_JuniRedundancyHistoryReloads_Type=Integer32
_JuniRedundancyHistoryReloads_Object=MibScalar
juniRedundancyHistoryReloads=_JuniRedundancyHistoryReloads_Object((1,3,6,1,4,1,4874,2,2,74,1,3,4),_JuniRedundancyHistoryReloads_Type())
juniRedundancyHistoryReloads.setMaxAccess(_C)
if mibBuilder.loadTexts:juniRedundancyHistoryReloads.setStatus(_B)
_JuniRedundancyHistoryColdSwitchovers_Type=Integer32
_JuniRedundancyHistoryColdSwitchovers_Object=MibScalar
juniRedundancyHistoryColdSwitchovers=_JuniRedundancyHistoryColdSwitchovers_Object((1,3,6,1,4,1,4874,2,2,74,1,3,5),_JuniRedundancyHistoryColdSwitchovers_Type())
juniRedundancyHistoryColdSwitchovers.setMaxAccess(_C)
if mibBuilder.loadTexts:juniRedundancyHistoryColdSwitchovers.setStatus(_B)
_JuniRedundancyHistoryWarmSwitchovers_Type=Integer32
_JuniRedundancyHistoryWarmSwitchovers_Object=MibScalar
juniRedundancyHistoryWarmSwitchovers=_JuniRedundancyHistoryWarmSwitchovers_Object((1,3,6,1,4,1,4874,2,2,74,1,3,6),_JuniRedundancyHistoryWarmSwitchovers_Type())
juniRedundancyHistoryWarmSwitchovers.setMaxAccess(_C)
if mibBuilder.loadTexts:juniRedundancyHistoryWarmSwitchovers.setStatus(_B)
_JuniLcRedundancyStatus_ObjectIdentity=ObjectIdentity
juniLcRedundancyStatus=_JuniLcRedundancyStatus_ObjectIdentity((1,3,6,1,4,1,4874,2,2,74,1,4))
class _JuniLcRedundancyActiveSlot_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_JuniLcRedundancyActiveSlot_Type.__name__=_D
_JuniLcRedundancyActiveSlot_Object=MibScalar
juniLcRedundancyActiveSlot=_JuniLcRedundancyActiveSlot_Object((1,3,6,1,4,1,4874,2,2,74,1,4,1),_JuniLcRedundancyActiveSlot_Type())
juniLcRedundancyActiveSlot.setMaxAccess(_F)
if mibBuilder.loadTexts:juniLcRedundancyActiveSlot.setStatus(_B)
class _JuniLcRedundancyStandbySlot_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_JuniLcRedundancyStandbySlot_Type.__name__=_D
_JuniLcRedundancyStandbySlot_Object=MibScalar
juniLcRedundancyStandbySlot=_JuniLcRedundancyStandbySlot_Object((1,3,6,1,4,1,4874,2,2,74,1,4,2),_JuniLcRedundancyStandbySlot_Type())
juniLcRedundancyStandbySlot.setMaxAccess(_F)
if mibBuilder.loadTexts:juniLcRedundancyStandbySlot.setStatus(_B)
_JuniLcRedundancyLastResetReason_Type=JuniLcRedundancyResetReason
_JuniLcRedundancyLastResetReason_Object=MibScalar
juniLcRedundancyLastResetReason=_JuniLcRedundancyLastResetReason_Object((1,3,6,1,4,1,4874,2,2,74,1,4,3),_JuniLcRedundancyLastResetReason_Type())
juniLcRedundancyLastResetReason.setMaxAccess(_F)
if mibBuilder.loadTexts:juniLcRedundancyLastResetReason.setStatus(_B)
_JuniLcRedundancyActivationType_Type=JuniLcRedundancySystemActivationType
_JuniLcRedundancyActivationType_Object=MibScalar
juniLcRedundancyActivationType=_JuniLcRedundancyActivationType_Object((1,3,6,1,4,1,4874,2,2,74,1,4,4),_JuniLcRedundancyActivationType_Type())
juniLcRedundancyActivationType.setMaxAccess(_F)
if mibBuilder.loadTexts:juniLcRedundancyActivationType.setStatus(_B)
_JuniLcRedundancyHaActiveTime_Type=TimeTicks
_JuniLcRedundancyHaActiveTime_Object=MibScalar
juniLcRedundancyHaActiveTime=_JuniLcRedundancyHaActiveTime_Object((1,3,6,1,4,1,4874,2,2,74,1,4,5),_JuniLcRedundancyHaActiveTime_Type())
juniLcRedundancyHaActiveTime.setMaxAccess(_F)
if mibBuilder.loadTexts:juniLcRedundancyHaActiveTime.setStatus(_B)
_JuniLcRedundancySwitchoverTime_Type=TimeTicks
_JuniLcRedundancySwitchoverTime_Object=MibScalar
juniLcRedundancySwitchoverTime=_JuniLcRedundancySwitchoverTime_Object((1,3,6,1,4,1,4874,2,2,74,1,4,6),_JuniLcRedundancySwitchoverTime_Type())
juniLcRedundancySwitchoverTime.setMaxAccess(_F)
if mibBuilder.loadTexts:juniLcRedundancySwitchoverTime.setStatus(_B)
_JuniRedundancyMIBConformance_ObjectIdentity=ObjectIdentity
juniRedundancyMIBConformance=_JuniRedundancyMIBConformance_ObjectIdentity((1,3,6,1,4,1,4874,2,2,74,2))
_JuniRedundancyMIBCompliances_ObjectIdentity=ObjectIdentity
juniRedundancyMIBCompliances=_JuniRedundancyMIBCompliances_ObjectIdentity((1,3,6,1,4,1,4874,2,2,74,2,1))
_JuniRedundancyMIBGroups_ObjectIdentity=ObjectIdentity
juniRedundancyMIBGroups=_JuniRedundancyMIBGroups_ObjectIdentity((1,3,6,1,4,1,4874,2,2,74,2,2))
juniRedundancyStatusGroup=ObjectGroup((1,3,6,1,4,1,4874,2,2,74,2,2,1))
juniRedundancyStatusGroup.setObjects(*((_A,_E),(_A,_V),(_A,_W),(_A,_X),(_A,_I),(_A,_Y),(_A,_Z),(_A,_a)))
if mibBuilder.loadTexts:juniRedundancyStatusGroup.setStatus(_B)
juniRedundancyCfgGroup=ObjectGroup((1,3,6,1,4,1,4874,2,2,74,2,2,2))
juniRedundancyCfgGroup.setObjects(*((_A,_b),(_A,_L)))
if mibBuilder.loadTexts:juniRedundancyCfgGroup.setStatus(_B)
juniRedundancyHistoryGroup=ObjectGroup((1,3,6,1,4,1,4874,2,2,74,2,2,3))
juniRedundancyHistoryGroup.setObjects(*((_A,_c),(_A,_d),(_A,_e),(_A,_f),(_A,_g),(_A,_h),(_A,_i),(_A,_j),(_A,_k),(_A,_l),(_A,_m),(_A,_n),(_A,_o)))
if mibBuilder.loadTexts:juniRedundancyHistoryGroup.setStatus(_B)
juniRedundancyColdSwitchoverNotification=NotificationType((1,3,6,1,4,1,4874,2,2,74,0,1))
juniRedundancyColdSwitchoverNotification.setObjects(*((_A,_E),(_A,_I)))
if mibBuilder.loadTexts:juniRedundancyColdSwitchoverNotification.setStatus(_B)
juniRedundancyWarmSwitchoverNotification=NotificationType((1,3,6,1,4,1,4874,2,2,74,0,2))
juniRedundancyWarmSwitchoverNotification.setObjects(*((_A,_E),(_A,_I)))
if mibBuilder.loadTexts:juniRedundancyWarmSwitchoverNotification.setStatus(_B)
juniRedundancyStateEnabledNotification=NotificationType((1,3,6,1,4,1,4874,2,2,74,0,3))
juniRedundancyStateEnabledNotification.setObjects((_A,_E))
if mibBuilder.loadTexts:juniRedundancyStateEnabledNotification.setStatus(_B)
juniRedundancyStateDisabledNotification=NotificationType((1,3,6,1,4,1,4874,2,2,74,0,4))
juniRedundancyStateDisabledNotification.setObjects((_A,_E))
if mibBuilder.loadTexts:juniRedundancyStateDisabledNotification.setStatus(_B)
juniRedundancyStatePendingNotification=NotificationType((1,3,6,1,4,1,4874,2,2,74,0,5))
juniRedundancyStatePendingNotification.setObjects((_A,_E))
if mibBuilder.loadTexts:juniRedundancyStatePendingNotification.setStatus(_B)
juniRedundancyModeNotification=NotificationType((1,3,6,1,4,1,4874,2,2,74,0,6))
juniRedundancyModeNotification.setObjects(*((_A,_E),(_A,_L)))
if mibBuilder.loadTexts:juniRedundancyModeNotification.setStatus(_B)
juniLcRedundancySwitchoverNotification=NotificationType((1,3,6,1,4,1,4874,2,2,74,0,7))
juniLcRedundancySwitchoverNotification.setObjects(*((_A,_p),(_A,_J),(_A,_q),(_A,_K),(_A,_r)))
if mibBuilder.loadTexts:juniLcRedundancySwitchoverNotification.setStatus(_B)
juniLcRedundancyStateEnabledNotification=NotificationType((1,3,6,1,4,1,4874,2,2,74,0,8))
juniLcRedundancyStateEnabledNotification.setObjects(*((_A,_J),(_A,_K),(_A,_M)))
if mibBuilder.loadTexts:juniLcRedundancyStateEnabledNotification.setStatus(_B)
juniLcRedundancyStateDisabledNotification=NotificationType((1,3,6,1,4,1,4874,2,2,74,0,9))
juniLcRedundancyStateDisabledNotification.setObjects(*((_A,_J),(_A,_K),(_A,_M)))
if mibBuilder.loadTexts:juniLcRedundancyStateDisabledNotification.setStatus(_B)
juniRedundancyNotificationGroup=NotificationGroup((1,3,6,1,4,1,4874,2,2,74,2,2,4))
juniRedundancyNotificationGroup.setObjects(*((_A,_s),(_A,_t),(_A,_u),(_A,_v),(_A,_w),(_A,_x),(_A,_y),(_A,_z),(_A,_A0)))
if mibBuilder.loadTexts:juniRedundancyNotificationGroup.setStatus(_B)
juniRedundancyMIBCompliance=ModuleCompliance((1,3,6,1,4,1,4874,2,2,74,2,1,1))
juniRedundancyMIBCompliance.setObjects(*((_A,_A1),(_A,_A2),(_A,_A3),(_A,_A4)))
if mibBuilder.loadTexts:juniRedundancyMIBCompliance.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'JuniRedundancyState':JuniRedundancyState,_S:JuniRedundancyMode,'JuniRedundancyResetReason':JuniRedundancyResetReason,'JuniRedundancySystemActivationType':JuniRedundancySystemActivationType,'JuniRedundancyResetType':JuniRedundancyResetType,_T:JuniRedundancyHistoryCommand,'JuniLcRedundancySystemActivationType':JuniLcRedundancySystemActivationType,'JuniLcRedundancyResetReason':JuniLcRedundancyResetReason,'juniRedundancyMIB':juniRedundancyMIB,'juniRedundancyNotifications':juniRedundancyNotifications,_s:juniRedundancyColdSwitchoverNotification,_t:juniRedundancyWarmSwitchoverNotification,_u:juniRedundancyStateEnabledNotification,_v:juniRedundancyStateDisabledNotification,_w:juniRedundancyStatePendingNotification,_x:juniRedundancyModeNotification,_y:juniLcRedundancySwitchoverNotification,_z:juniLcRedundancyStateEnabledNotification,_A0:juniLcRedundancyStateDisabledNotification,'juniRedundancyObjects':juniRedundancyObjects,'juniRedundancyStatus':juniRedundancyStatus,_E:juniRedundancyActiveSlot,_V:juniRedundancyActiveSlotState,_W:juniRedundancyStandbySlot,_X:juniRedundancyStandbySlotState,_I:juniRedundancyLastResetReason,_Y:juniRedundancyLastSystemActivationTime,_Z:juniRedundancyLastSystemActivationType,_a:juniRedundancyHaActiveTime,'juniRedundancyCfg':juniRedundancyCfg,_b:juniRedundancyNotifsEnabled,_L:juniRedundancyCfgRedundancyMode,'juniRedundancyHistory':juniRedundancyHistory,_c:juniRedundancySystemActivationHistoryTableMaxLength,_d:juniRedundancySystemActivationHistoryCommand,'juniRedundancySystemActivationHistoryTable':juniRedundancySystemActivationHistoryTable,'juniRedundancySystemActivationHistoryEntry':juniRedundancySystemActivationHistoryEntry,_U:juniRedundancySystemActivationHistoryIndex,_e:juniRedundancyHistoryResetType,_f:juniRedundancyHistoryActivationType,_g:juniRedundancyHistoryPrevActiveSlot,_h:juniRedundancyHistoryPrevActiveRelease,_i:juniRedundancyHistoryCurrActiveSlot,_j:juniRedundancyHistoryCurrActiveRelease,_k:juniRedundancyHistoryResetReason,_l:juniRedundancyHistoryActivationTime,_m:juniRedundancyHistoryReloads,_n:juniRedundancyHistoryColdSwitchovers,_o:juniRedundancyHistoryWarmSwitchovers,'juniLcRedundancyStatus':juniLcRedundancyStatus,_J:juniLcRedundancyActiveSlot,_K:juniLcRedundancyStandbySlot,_q:juniLcRedundancyLastResetReason,_p:juniLcRedundancyActivationType,_M:juniLcRedundancyHaActiveTime,_r:juniLcRedundancySwitchoverTime,'juniRedundancyMIBConformance':juniRedundancyMIBConformance,'juniRedundancyMIBCompliances':juniRedundancyMIBCompliances,'juniRedundancyMIBCompliance':juniRedundancyMIBCompliance,'juniRedundancyMIBGroups':juniRedundancyMIBGroups,_A1:juniRedundancyStatusGroup,_A2:juniRedundancyCfgGroup,_A3:juniRedundancyHistoryGroup,_A4:juniRedundancyNotificationGroup})