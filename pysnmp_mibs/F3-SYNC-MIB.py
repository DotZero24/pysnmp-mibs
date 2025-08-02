_AQ='f3SyncObjectGroup'
_AP='f3TimeClockRefRowStatus'
_AO='f3TimeClockRefStorageType'
_AN='f3TimeClockRefOperationType'
_AM='f3TimeClockRefState'
_AL='f3TimeClockRefStatus'
_AK='f3TimeClockRefPriority'
_AJ='f3TimeClockRefReference'
_AI='f3TimeClockRefAlias'
_AH='f3TimeClockCurrentTimeOfDay'
_AG='f3TimeClockUtcOffset'
_AF='f3TimeClockTimeHoldoverPerformance'
_AE='f3TimeClockSyncRefCandidate'
_AD='f3TimeClockCurrentQL'
_AC='f3TimeClockExpectedQL'
_AB='f3TimeClockTimeTraceAbilityStatus'
_AA='f3TimeClockLeap61'
_A9='f3TimeClockLeap59'
_A8='f3TimeClockOperationType'
_A7='f3TimeClockOperationTimeClockRef'
_A6='f3TimeClockWaitToRestoreTime'
_A5='f3TimeClockSelectionMode'
_A4='f3TimeClockClockClass'
_A3='f3TimeClockClockMode'
_A2='f3TimeClockSelectedReference'
_A1='f3TimeClockSecondaryState'
_A0='f3TimeClockOperationalState'
_z='f3TimeClockAdminState'
_y='f3TimeClockAlias'
_x='f3SyncRefOperationType'
_w='f3SyncRefEffectiveQL'
_v='f3SyncRefAlias'
_u='f3SyncRefRowStatus'
_t='f3SyncRefStorageType'
_s='f3SyncRefReceivedQL'
_r='f3SyncRefState'
_q='f3SyncRefStatus'
_p='f3SyncRefPriority'
_o='f3SyncRefReference'
_n='f3SyncOperationType'
_m='f3SyncOperationSyncRef'
_l='f3SyncWaitToRestoreTime'
_k='f3SyncSelectionMode'
_j='f3SyncDomain'
_i='f3SyncAlias'
_h='f3SyncQL'
_g='f3SyncClockMode'
_f='f3SyncSelectedReference'
_e='f3SyncNetworkClockType'
_d='f3SyncSecondaryState'
_c='f3SyncOperationalState'
_b='f3SyncAdminState'
_a='not-accessible'
_Z='time-10000ns'
_Y='time-5000ns'
_X='time-1500ns'
_W='time-1000ns'
_V='time-500ns'
_U='locked'
_T='tracking'
_S='freerun'
_R='f3TimeClockRefIndex'
_Q='f3SyncRefIndex'
_P='not-applicable'
_O='holdover'
_N='DisplayString'
_M='F3DisplayString'
_L='f3TimeClockIndex'
_K='f3SyncIndex'
_J='Integer32'
_I='slotIndex'
_H='shelfIndex'
_G='neIndex'
_F='read-create'
_E='CM-ENTITY-MIB'
_D='read-write'
_C='read-only'
_B='F3-SYNC-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
fsp150cm,=mibBuilder.importSymbols('ADVA-MIB','fsp150cm')
AdminState,F3DisplayString,OperationalState,SecondaryState=mibBuilder.importSymbols('CM-COMMON-MIB','AdminState',_M,'OperationalState','SecondaryState')
neIndex,shelfIndex,slotIndex=mibBuilder.importSymbols(_E,_G,_H,_I)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_J,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DateAndTime,DisplayString,PhysAddress,RowStatus,StorageType,TextualConvention,TruthValue,VariablePointer=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime',_N,'PhysAddress','RowStatus','StorageType','TextualConvention','TruthValue','VariablePointer')
f3SyncMIB=ModuleIdentity((1,3,6,1,4,1,2544,1,12,12))
if mibBuilder.loadTexts:f3SyncMIB.setRevisions(('2010-03-25 00:00',))
class NetworkClockType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('option1',1),('option2',2)))
class ClockMode(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6)));namedValues=NamedValues(*(('notAvailable',0),(_S,1),(_O,2),(_T,3),('lossoflock',4),(_U,5),('bypass',6)))
class SSMQualityLevel(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34)));namedValues=NamedValues(*((_P,0),('ql-dnu',1),('ql-eec1',2),('ql-eec2',3),('ql-inv',4),('ql-inv0',5),('ql-inv1',6),('ql-inv2',7),('ql-inv3',8),('ql-inv5',9),('ql-inv7',10),('ql-inv8',11),('ql-inv9',12),('ql-inv10',13),('ql-inv11',14),('ql-inv12',15),('ql-none',16),('ql-nsupp',17),('ql-prc',18),('ql-prov',19),('ql-prs',20),('ql-smc',21),('ql-ssu-a',22),('ql-ssu-b',23),('ql-st2',24),('ql-st3e',25),('ql-stu',26),('ql-tnc',27),('ql-unc',28),('ql-failed',29),('ql-inv6',30),('ql-inv13',31),('ql-inv14',32),('ql-dus',33),('ql-na',34)))
class SyncRefStatus(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*((_P,0),('ref-ok',1),('ref-failed',2),('ref-freq-ok',3)))
class SyncRefState(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4)));namedValues=NamedValues(*((_P,0),('active',1),('standby',2),('unavailable',3),('lockedout',4)))
class SyncDomainType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('chassis',1),('linecard',2)))
class SyncOperationType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*(('none',1),('forcedswitch',2),('manualswitch',3),('lockout',4),('clearwtr',5),('clearlockout',6),('clearswitch',7)))
class SyncSelectionMode(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('ql-mode',1),('priority-mode',2)))
class SquelchControl(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('never',1),(_O,2),('lock',3),('squelch-ql',4)))
class TimeClockMode(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*((_S,1),('warmup',2),(_T,3),('transition',4),(_O,5),(_U,6)))
class TimeTraceAbilityStatus(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('notTraceAble',1),('timeLocked',2),('timeFreqLock',3),('timeHoldover',4)))
class HoldoverAccuracy(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_V,1),(_W,2),(_X,3),(_Y,4),(_Z,5)))
class TimeHoldoverPerformance(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*((_V,1),(_W,2),(_X,3),(_Y,4),(_Z,5),('time-0ns',6),('time-100ns',7)))
class TimeSource(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('atomic',1),('gps',2),('ptp',3),('internal',4),('other',5)))
_F3SyncObjects_ObjectIdentity=ObjectIdentity
f3SyncObjects=_F3SyncObjects_ObjectIdentity((1,3,6,1,4,1,2544,1,12,12,1))
_F3SyncTable_Object=MibTable
f3SyncTable=_F3SyncTable_Object((1,3,6,1,4,1,2544,1,12,12,1,1))
if mibBuilder.loadTexts:f3SyncTable.setStatus(_A)
_F3SyncEntry_Object=MibTableRow
f3SyncEntry=_F3SyncEntry_Object((1,3,6,1,4,1,2544,1,12,12,1,1,1))
f3SyncEntry.setIndexNames((0,_E,_G),(0,_E,_H),(0,_E,_I),(0,_B,_K))
if mibBuilder.loadTexts:f3SyncEntry.setStatus(_A)
_F3SyncIndex_Type=Integer32
_F3SyncIndex_Object=MibTableColumn
f3SyncIndex=_F3SyncIndex_Object((1,3,6,1,4,1,2544,1,12,12,1,1,1,1),_F3SyncIndex_Type())
f3SyncIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:f3SyncIndex.setStatus(_A)
_F3SyncAdminState_Type=AdminState
_F3SyncAdminState_Object=MibTableColumn
f3SyncAdminState=_F3SyncAdminState_Object((1,3,6,1,4,1,2544,1,12,12,1,1,1,2),_F3SyncAdminState_Type())
f3SyncAdminState.setMaxAccess(_D)
if mibBuilder.loadTexts:f3SyncAdminState.setStatus(_A)
_F3SyncOperationalState_Type=OperationalState
_F3SyncOperationalState_Object=MibTableColumn
f3SyncOperationalState=_F3SyncOperationalState_Object((1,3,6,1,4,1,2544,1,12,12,1,1,1,3),_F3SyncOperationalState_Type())
f3SyncOperationalState.setMaxAccess(_C)
if mibBuilder.loadTexts:f3SyncOperationalState.setStatus(_A)
_F3SyncSecondaryState_Type=SecondaryState
_F3SyncSecondaryState_Object=MibTableColumn
f3SyncSecondaryState=_F3SyncSecondaryState_Object((1,3,6,1,4,1,2544,1,12,12,1,1,1,4),_F3SyncSecondaryState_Type())
f3SyncSecondaryState.setMaxAccess(_C)
if mibBuilder.loadTexts:f3SyncSecondaryState.setStatus(_A)
_F3SyncNetworkClockType_Type=NetworkClockType
_F3SyncNetworkClockType_Object=MibTableColumn
f3SyncNetworkClockType=_F3SyncNetworkClockType_Object((1,3,6,1,4,1,2544,1,12,12,1,1,1,5),_F3SyncNetworkClockType_Type())
f3SyncNetworkClockType.setMaxAccess(_D)
if mibBuilder.loadTexts:f3SyncNetworkClockType.setStatus(_A)
_F3SyncSelectedReference_Type=VariablePointer
_F3SyncSelectedReference_Object=MibTableColumn
f3SyncSelectedReference=_F3SyncSelectedReference_Object((1,3,6,1,4,1,2544,1,12,12,1,1,1,6),_F3SyncSelectedReference_Type())
f3SyncSelectedReference.setMaxAccess(_C)
if mibBuilder.loadTexts:f3SyncSelectedReference.setStatus(_A)
_F3SyncClockMode_Type=ClockMode
_F3SyncClockMode_Object=MibTableColumn
f3SyncClockMode=_F3SyncClockMode_Object((1,3,6,1,4,1,2544,1,12,12,1,1,1,7),_F3SyncClockMode_Type())
f3SyncClockMode.setMaxAccess(_C)
if mibBuilder.loadTexts:f3SyncClockMode.setStatus(_A)
_F3SyncQL_Type=SSMQualityLevel
_F3SyncQL_Object=MibTableColumn
f3SyncQL=_F3SyncQL_Object((1,3,6,1,4,1,2544,1,12,12,1,1,1,8),_F3SyncQL_Type())
f3SyncQL.setMaxAccess(_C)
if mibBuilder.loadTexts:f3SyncQL.setStatus(_A)
class _F3SyncAlias_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,256))
_F3SyncAlias_Type.__name__=_N
_F3SyncAlias_Object=MibTableColumn
f3SyncAlias=_F3SyncAlias_Object((1,3,6,1,4,1,2544,1,12,12,1,1,1,9),_F3SyncAlias_Type())
f3SyncAlias.setMaxAccess(_F)
if mibBuilder.loadTexts:f3SyncAlias.setStatus(_A)
_F3SyncDomain_Type=SyncDomainType
_F3SyncDomain_Object=MibTableColumn
f3SyncDomain=_F3SyncDomain_Object((1,3,6,1,4,1,2544,1,12,12,1,1,1,10),_F3SyncDomain_Type())
f3SyncDomain.setMaxAccess(_D)
if mibBuilder.loadTexts:f3SyncDomain.setStatus(_A)
_F3SyncSelectionMode_Type=SyncSelectionMode
_F3SyncSelectionMode_Object=MibTableColumn
f3SyncSelectionMode=_F3SyncSelectionMode_Object((1,3,6,1,4,1,2544,1,12,12,1,1,1,11),_F3SyncSelectionMode_Type())
f3SyncSelectionMode.setMaxAccess(_D)
if mibBuilder.loadTexts:f3SyncSelectionMode.setStatus(_A)
class _F3SyncWaitToRestoreTime_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,12))
_F3SyncWaitToRestoreTime_Type.__name__=_J
_F3SyncWaitToRestoreTime_Object=MibTableColumn
f3SyncWaitToRestoreTime=_F3SyncWaitToRestoreTime_Object((1,3,6,1,4,1,2544,1,12,12,1,1,1,12),_F3SyncWaitToRestoreTime_Type())
f3SyncWaitToRestoreTime.setMaxAccess(_D)
if mibBuilder.loadTexts:f3SyncWaitToRestoreTime.setStatus(_A)
_F3SyncOperationSyncRef_Type=VariablePointer
_F3SyncOperationSyncRef_Object=MibTableColumn
f3SyncOperationSyncRef=_F3SyncOperationSyncRef_Object((1,3,6,1,4,1,2544,1,12,12,1,1,1,13),_F3SyncOperationSyncRef_Type())
f3SyncOperationSyncRef.setMaxAccess(_D)
if mibBuilder.loadTexts:f3SyncOperationSyncRef.setStatus(_A)
_F3SyncOperationType_Type=SyncOperationType
_F3SyncOperationType_Object=MibTableColumn
f3SyncOperationType=_F3SyncOperationType_Object((1,3,6,1,4,1,2544,1,12,12,1,1,1,14),_F3SyncOperationType_Type())
f3SyncOperationType.setMaxAccess(_D)
if mibBuilder.loadTexts:f3SyncOperationType.setStatus(_A)
_F3SyncRefTable_Object=MibTable
f3SyncRefTable=_F3SyncRefTable_Object((1,3,6,1,4,1,2544,1,12,12,1,2))
if mibBuilder.loadTexts:f3SyncRefTable.setStatus(_A)
_F3SyncRefEntry_Object=MibTableRow
f3SyncRefEntry=_F3SyncRefEntry_Object((1,3,6,1,4,1,2544,1,12,12,1,2,1))
f3SyncRefEntry.setIndexNames((0,_E,_G),(0,_E,_H),(0,_E,_I),(0,_B,_K),(0,_B,_Q))
if mibBuilder.loadTexts:f3SyncRefEntry.setStatus(_A)
_F3SyncRefIndex_Type=Integer32
_F3SyncRefIndex_Object=MibTableColumn
f3SyncRefIndex=_F3SyncRefIndex_Object((1,3,6,1,4,1,2544,1,12,12,1,2,1,1),_F3SyncRefIndex_Type())
f3SyncRefIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:f3SyncRefIndex.setStatus(_A)
_F3SyncRefReference_Type=VariablePointer
_F3SyncRefReference_Object=MibTableColumn
f3SyncRefReference=_F3SyncRefReference_Object((1,3,6,1,4,1,2544,1,12,12,1,2,1,2),_F3SyncRefReference_Type())
f3SyncRefReference.setMaxAccess(_F)
if mibBuilder.loadTexts:f3SyncRefReference.setStatus(_A)
class _F3SyncRefPriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,10))
_F3SyncRefPriority_Type.__name__=_J
_F3SyncRefPriority_Object=MibTableColumn
f3SyncRefPriority=_F3SyncRefPriority_Object((1,3,6,1,4,1,2544,1,12,12,1,2,1,3),_F3SyncRefPriority_Type())
f3SyncRefPriority.setMaxAccess(_F)
if mibBuilder.loadTexts:f3SyncRefPriority.setStatus(_A)
_F3SyncRefStatus_Type=SyncRefStatus
_F3SyncRefStatus_Object=MibTableColumn
f3SyncRefStatus=_F3SyncRefStatus_Object((1,3,6,1,4,1,2544,1,12,12,1,2,1,4),_F3SyncRefStatus_Type())
f3SyncRefStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:f3SyncRefStatus.setStatus(_A)
_F3SyncRefState_Type=SyncRefState
_F3SyncRefState_Object=MibTableColumn
f3SyncRefState=_F3SyncRefState_Object((1,3,6,1,4,1,2544,1,12,12,1,2,1,5),_F3SyncRefState_Type())
f3SyncRefState.setMaxAccess(_C)
if mibBuilder.loadTexts:f3SyncRefState.setStatus(_A)
_F3SyncRefReceivedQL_Type=SSMQualityLevel
_F3SyncRefReceivedQL_Object=MibTableColumn
f3SyncRefReceivedQL=_F3SyncRefReceivedQL_Object((1,3,6,1,4,1,2544,1,12,12,1,2,1,6),_F3SyncRefReceivedQL_Type())
f3SyncRefReceivedQL.setMaxAccess(_C)
if mibBuilder.loadTexts:f3SyncRefReceivedQL.setStatus(_A)
_F3SyncRefStorageType_Type=StorageType
_F3SyncRefStorageType_Object=MibTableColumn
f3SyncRefStorageType=_F3SyncRefStorageType_Object((1,3,6,1,4,1,2544,1,12,12,1,2,1,7),_F3SyncRefStorageType_Type())
f3SyncRefStorageType.setMaxAccess(_F)
if mibBuilder.loadTexts:f3SyncRefStorageType.setStatus(_A)
_F3SyncRefRowStatus_Type=RowStatus
_F3SyncRefRowStatus_Object=MibTableColumn
f3SyncRefRowStatus=_F3SyncRefRowStatus_Object((1,3,6,1,4,1,2544,1,12,12,1,2,1,8),_F3SyncRefRowStatus_Type())
f3SyncRefRowStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:f3SyncRefRowStatus.setStatus(_A)
class _F3SyncRefAlias_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,256))
_F3SyncRefAlias_Type.__name__=_N
_F3SyncRefAlias_Object=MibTableColumn
f3SyncRefAlias=_F3SyncRefAlias_Object((1,3,6,1,4,1,2544,1,12,12,1,2,1,9),_F3SyncRefAlias_Type())
f3SyncRefAlias.setMaxAccess(_F)
if mibBuilder.loadTexts:f3SyncRefAlias.setStatus(_A)
_F3SyncRefEffectiveQL_Type=SSMQualityLevel
_F3SyncRefEffectiveQL_Object=MibTableColumn
f3SyncRefEffectiveQL=_F3SyncRefEffectiveQL_Object((1,3,6,1,4,1,2544,1,12,12,1,2,1,10),_F3SyncRefEffectiveQL_Type())
f3SyncRefEffectiveQL.setMaxAccess(_C)
if mibBuilder.loadTexts:f3SyncRefEffectiveQL.setStatus(_A)
_F3SyncRefOperationType_Type=SyncOperationType
_F3SyncRefOperationType_Object=MibTableColumn
f3SyncRefOperationType=_F3SyncRefOperationType_Object((1,3,6,1,4,1,2544,1,12,12,1,2,1,11),_F3SyncRefOperationType_Type())
f3SyncRefOperationType.setMaxAccess(_C)
if mibBuilder.loadTexts:f3SyncRefOperationType.setStatus(_A)
_F3TimeClockTable_Object=MibTable
f3TimeClockTable=_F3TimeClockTable_Object((1,3,6,1,4,1,2544,1,12,12,1,3))
if mibBuilder.loadTexts:f3TimeClockTable.setStatus(_A)
_F3TimeClockEntry_Object=MibTableRow
f3TimeClockEntry=_F3TimeClockEntry_Object((1,3,6,1,4,1,2544,1,12,12,1,3,1))
f3TimeClockEntry.setIndexNames((0,_E,_G),(0,_E,_H),(0,_E,_I),(0,_B,_L))
if mibBuilder.loadTexts:f3TimeClockEntry.setStatus(_A)
_F3TimeClockIndex_Type=Integer32
_F3TimeClockIndex_Object=MibTableColumn
f3TimeClockIndex=_F3TimeClockIndex_Object((1,3,6,1,4,1,2544,1,12,12,1,3,1,1),_F3TimeClockIndex_Type())
f3TimeClockIndex.setMaxAccess(_a)
if mibBuilder.loadTexts:f3TimeClockIndex.setStatus(_A)
class _F3TimeClockAlias_Type(F3DisplayString):subtypeSpec=F3DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,256))
_F3TimeClockAlias_Type.__name__=_M
_F3TimeClockAlias_Object=MibTableColumn
f3TimeClockAlias=_F3TimeClockAlias_Object((1,3,6,1,4,1,2544,1,12,12,1,3,1,2),_F3TimeClockAlias_Type())
f3TimeClockAlias.setMaxAccess(_D)
if mibBuilder.loadTexts:f3TimeClockAlias.setStatus(_A)
_F3TimeClockAdminState_Type=AdminState
_F3TimeClockAdminState_Object=MibTableColumn
f3TimeClockAdminState=_F3TimeClockAdminState_Object((1,3,6,1,4,1,2544,1,12,12,1,3,1,3),_F3TimeClockAdminState_Type())
f3TimeClockAdminState.setMaxAccess(_D)
if mibBuilder.loadTexts:f3TimeClockAdminState.setStatus(_A)
_F3TimeClockOperationalState_Type=OperationalState
_F3TimeClockOperationalState_Object=MibTableColumn
f3TimeClockOperationalState=_F3TimeClockOperationalState_Object((1,3,6,1,4,1,2544,1,12,12,1,3,1,4),_F3TimeClockOperationalState_Type())
f3TimeClockOperationalState.setMaxAccess(_C)
if mibBuilder.loadTexts:f3TimeClockOperationalState.setStatus(_A)
_F3TimeClockSecondaryState_Type=SecondaryState
_F3TimeClockSecondaryState_Object=MibTableColumn
f3TimeClockSecondaryState=_F3TimeClockSecondaryState_Object((1,3,6,1,4,1,2544,1,12,12,1,3,1,5),_F3TimeClockSecondaryState_Type())
f3TimeClockSecondaryState.setMaxAccess(_C)
if mibBuilder.loadTexts:f3TimeClockSecondaryState.setStatus(_A)
_F3TimeClockSelectedReference_Type=VariablePointer
_F3TimeClockSelectedReference_Object=MibTableColumn
f3TimeClockSelectedReference=_F3TimeClockSelectedReference_Object((1,3,6,1,4,1,2544,1,12,12,1,3,1,6),_F3TimeClockSelectedReference_Type())
f3TimeClockSelectedReference.setMaxAccess(_C)
if mibBuilder.loadTexts:f3TimeClockSelectedReference.setStatus(_A)
_F3TimeClockClockMode_Type=TimeClockMode
_F3TimeClockClockMode_Object=MibTableColumn
f3TimeClockClockMode=_F3TimeClockClockMode_Object((1,3,6,1,4,1,2544,1,12,12,1,3,1,7),_F3TimeClockClockMode_Type())
f3TimeClockClockMode.setMaxAccess(_C)
if mibBuilder.loadTexts:f3TimeClockClockMode.setStatus(_A)
_F3TimeClockClockClass_Type=Unsigned32
_F3TimeClockClockClass_Object=MibTableColumn
f3TimeClockClockClass=_F3TimeClockClockClass_Object((1,3,6,1,4,1,2544,1,12,12,1,3,1,8),_F3TimeClockClockClass_Type())
f3TimeClockClockClass.setMaxAccess(_C)
if mibBuilder.loadTexts:f3TimeClockClockClass.setStatus('deprecated')
_F3TimeClockSelectionMode_Type=SyncSelectionMode
_F3TimeClockSelectionMode_Object=MibTableColumn
f3TimeClockSelectionMode=_F3TimeClockSelectionMode_Object((1,3,6,1,4,1,2544,1,12,12,1,3,1,9),_F3TimeClockSelectionMode_Type())
f3TimeClockSelectionMode.setMaxAccess(_D)
if mibBuilder.loadTexts:f3TimeClockSelectionMode.setStatus(_A)
class _F3TimeClockWaitToRestoreTime_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,12))
_F3TimeClockWaitToRestoreTime_Type.__name__=_J
_F3TimeClockWaitToRestoreTime_Object=MibTableColumn
f3TimeClockWaitToRestoreTime=_F3TimeClockWaitToRestoreTime_Object((1,3,6,1,4,1,2544,1,12,12,1,3,1,10),_F3TimeClockWaitToRestoreTime_Type())
f3TimeClockWaitToRestoreTime.setMaxAccess(_D)
if mibBuilder.loadTexts:f3TimeClockWaitToRestoreTime.setStatus(_A)
_F3TimeClockOperationTimeClockRef_Type=VariablePointer
_F3TimeClockOperationTimeClockRef_Object=MibTableColumn
f3TimeClockOperationTimeClockRef=_F3TimeClockOperationTimeClockRef_Object((1,3,6,1,4,1,2544,1,12,12,1,3,1,11),_F3TimeClockOperationTimeClockRef_Type())
f3TimeClockOperationTimeClockRef.setMaxAccess(_D)
if mibBuilder.loadTexts:f3TimeClockOperationTimeClockRef.setStatus(_A)
_F3TimeClockOperationType_Type=SyncOperationType
_F3TimeClockOperationType_Object=MibTableColumn
f3TimeClockOperationType=_F3TimeClockOperationType_Object((1,3,6,1,4,1,2544,1,12,12,1,3,1,12),_F3TimeClockOperationType_Type())
f3TimeClockOperationType.setMaxAccess(_D)
if mibBuilder.loadTexts:f3TimeClockOperationType.setStatus(_A)
_F3TimeClockLeap59_Type=TruthValue
_F3TimeClockLeap59_Object=MibTableColumn
f3TimeClockLeap59=_F3TimeClockLeap59_Object((1,3,6,1,4,1,2544,1,12,12,1,3,1,13),_F3TimeClockLeap59_Type())
f3TimeClockLeap59.setMaxAccess(_C)
if mibBuilder.loadTexts:f3TimeClockLeap59.setStatus(_A)
_F3TimeClockLeap61_Type=TruthValue
_F3TimeClockLeap61_Object=MibTableColumn
f3TimeClockLeap61=_F3TimeClockLeap61_Object((1,3,6,1,4,1,2544,1,12,12,1,3,1,14),_F3TimeClockLeap61_Type())
f3TimeClockLeap61.setMaxAccess(_C)
if mibBuilder.loadTexts:f3TimeClockLeap61.setStatus(_A)
_F3TimeClockTimeTraceAbilityStatus_Type=TimeTraceAbilityStatus
_F3TimeClockTimeTraceAbilityStatus_Object=MibTableColumn
f3TimeClockTimeTraceAbilityStatus=_F3TimeClockTimeTraceAbilityStatus_Object((1,3,6,1,4,1,2544,1,12,12,1,3,1,15),_F3TimeClockTimeTraceAbilityStatus_Type())
f3TimeClockTimeTraceAbilityStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:f3TimeClockTimeTraceAbilityStatus.setStatus(_A)
_F3TimeClockExpectedQL_Type=SSMQualityLevel
_F3TimeClockExpectedQL_Object=MibTableColumn
f3TimeClockExpectedQL=_F3TimeClockExpectedQL_Object((1,3,6,1,4,1,2544,1,12,12,1,3,1,16),_F3TimeClockExpectedQL_Type())
f3TimeClockExpectedQL.setMaxAccess(_D)
if mibBuilder.loadTexts:f3TimeClockExpectedQL.setStatus(_A)
_F3TimeClockCurrentQL_Type=SSMQualityLevel
_F3TimeClockCurrentQL_Object=MibTableColumn
f3TimeClockCurrentQL=_F3TimeClockCurrentQL_Object((1,3,6,1,4,1,2544,1,12,12,1,3,1,17),_F3TimeClockCurrentQL_Type())
f3TimeClockCurrentQL.setMaxAccess(_C)
if mibBuilder.loadTexts:f3TimeClockCurrentQL.setStatus(_A)
_F3TimeClockSyncRefCandidate_Type=TruthValue
_F3TimeClockSyncRefCandidate_Object=MibTableColumn
f3TimeClockSyncRefCandidate=_F3TimeClockSyncRefCandidate_Object((1,3,6,1,4,1,2544,1,12,12,1,3,1,18),_F3TimeClockSyncRefCandidate_Type())
f3TimeClockSyncRefCandidate.setMaxAccess(_D)
if mibBuilder.loadTexts:f3TimeClockSyncRefCandidate.setStatus(_A)
_F3TimeClockTimeHoldoverPerformance_Type=TimeHoldoverPerformance
_F3TimeClockTimeHoldoverPerformance_Object=MibTableColumn
f3TimeClockTimeHoldoverPerformance=_F3TimeClockTimeHoldoverPerformance_Object((1,3,6,1,4,1,2544,1,12,12,1,3,1,19),_F3TimeClockTimeHoldoverPerformance_Type())
f3TimeClockTimeHoldoverPerformance.setMaxAccess(_D)
if mibBuilder.loadTexts:f3TimeClockTimeHoldoverPerformance.setStatus(_A)
_F3TimeClockUtcOffset_Type=Unsigned32
_F3TimeClockUtcOffset_Object=MibTableColumn
f3TimeClockUtcOffset=_F3TimeClockUtcOffset_Object((1,3,6,1,4,1,2544,1,12,12,1,3,1,20),_F3TimeClockUtcOffset_Type())
f3TimeClockUtcOffset.setMaxAccess(_C)
if mibBuilder.loadTexts:f3TimeClockUtcOffset.setStatus(_A)
_F3TimeClockCurrentTimeOfDay_Type=DateAndTime
_F3TimeClockCurrentTimeOfDay_Object=MibTableColumn
f3TimeClockCurrentTimeOfDay=_F3TimeClockCurrentTimeOfDay_Object((1,3,6,1,4,1,2544,1,12,12,1,3,1,21),_F3TimeClockCurrentTimeOfDay_Type())
f3TimeClockCurrentTimeOfDay.setMaxAccess(_C)
if mibBuilder.loadTexts:f3TimeClockCurrentTimeOfDay.setStatus(_A)
_F3TimeClockFrequencyReference_Type=VariablePointer
_F3TimeClockFrequencyReference_Object=MibTableColumn
f3TimeClockFrequencyReference=_F3TimeClockFrequencyReference_Object((1,3,6,1,4,1,2544,1,12,12,1,3,1,22),_F3TimeClockFrequencyReference_Type())
f3TimeClockFrequencyReference.setMaxAccess(_D)
if mibBuilder.loadTexts:f3TimeClockFrequencyReference.setStatus(_A)
_F3TimeClockFrequencyClockMode_Type=TimeClockMode
_F3TimeClockFrequencyClockMode_Object=MibTableColumn
f3TimeClockFrequencyClockMode=_F3TimeClockFrequencyClockMode_Object((1,3,6,1,4,1,2544,1,12,12,1,3,1,23),_F3TimeClockFrequencyClockMode_Type())
f3TimeClockFrequencyClockMode.setMaxAccess(_C)
if mibBuilder.loadTexts:f3TimeClockFrequencyClockMode.setStatus(_A)
_F3TimeClockRefTable_Object=MibTable
f3TimeClockRefTable=_F3TimeClockRefTable_Object((1,3,6,1,4,1,2544,1,12,12,1,4))
if mibBuilder.loadTexts:f3TimeClockRefTable.setStatus(_A)
_F3TimeClockRefEntry_Object=MibTableRow
f3TimeClockRefEntry=_F3TimeClockRefEntry_Object((1,3,6,1,4,1,2544,1,12,12,1,4,1))
f3TimeClockRefEntry.setIndexNames((0,_E,_G),(0,_E,_H),(0,_E,_I),(0,_B,_L),(0,_B,_R))
if mibBuilder.loadTexts:f3TimeClockRefEntry.setStatus(_A)
_F3TimeClockRefIndex_Type=Integer32
_F3TimeClockRefIndex_Object=MibTableColumn
f3TimeClockRefIndex=_F3TimeClockRefIndex_Object((1,3,6,1,4,1,2544,1,12,12,1,4,1,1),_F3TimeClockRefIndex_Type())
f3TimeClockRefIndex.setMaxAccess(_a)
if mibBuilder.loadTexts:f3TimeClockRefIndex.setStatus(_A)
class _F3TimeClockRefAlias_Type(F3DisplayString):subtypeSpec=F3DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,256))
_F3TimeClockRefAlias_Type.__name__=_M
_F3TimeClockRefAlias_Object=MibTableColumn
f3TimeClockRefAlias=_F3TimeClockRefAlias_Object((1,3,6,1,4,1,2544,1,12,12,1,4,1,2),_F3TimeClockRefAlias_Type())
f3TimeClockRefAlias.setMaxAccess(_F)
if mibBuilder.loadTexts:f3TimeClockRefAlias.setStatus(_A)
_F3TimeClockRefReference_Type=VariablePointer
_F3TimeClockRefReference_Object=MibTableColumn
f3TimeClockRefReference=_F3TimeClockRefReference_Object((1,3,6,1,4,1,2544,1,12,12,1,4,1,3),_F3TimeClockRefReference_Type())
f3TimeClockRefReference.setMaxAccess(_F)
if mibBuilder.loadTexts:f3TimeClockRefReference.setStatus(_A)
class _F3TimeClockRefPriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,10))
_F3TimeClockRefPriority_Type.__name__=_J
_F3TimeClockRefPriority_Object=MibTableColumn
f3TimeClockRefPriority=_F3TimeClockRefPriority_Object((1,3,6,1,4,1,2544,1,12,12,1,4,1,4),_F3TimeClockRefPriority_Type())
f3TimeClockRefPriority.setMaxAccess(_F)
if mibBuilder.loadTexts:f3TimeClockRefPriority.setStatus(_A)
_F3TimeClockRefStatus_Type=SyncRefStatus
_F3TimeClockRefStatus_Object=MibTableColumn
f3TimeClockRefStatus=_F3TimeClockRefStatus_Object((1,3,6,1,4,1,2544,1,12,12,1,4,1,5),_F3TimeClockRefStatus_Type())
f3TimeClockRefStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:f3TimeClockRefStatus.setStatus(_A)
_F3TimeClockRefState_Type=SyncRefState
_F3TimeClockRefState_Object=MibTableColumn
f3TimeClockRefState=_F3TimeClockRefState_Object((1,3,6,1,4,1,2544,1,12,12,1,4,1,6),_F3TimeClockRefState_Type())
f3TimeClockRefState.setMaxAccess(_C)
if mibBuilder.loadTexts:f3TimeClockRefState.setStatus(_A)
_F3TimeClockRefOperationType_Type=SyncOperationType
_F3TimeClockRefOperationType_Object=MibTableColumn
f3TimeClockRefOperationType=_F3TimeClockRefOperationType_Object((1,3,6,1,4,1,2544,1,12,12,1,4,1,7),_F3TimeClockRefOperationType_Type())
f3TimeClockRefOperationType.setMaxAccess(_C)
if mibBuilder.loadTexts:f3TimeClockRefOperationType.setStatus(_A)
_F3TimeClockRefStorageType_Type=StorageType
_F3TimeClockRefStorageType_Object=MibTableColumn
f3TimeClockRefStorageType=_F3TimeClockRefStorageType_Object((1,3,6,1,4,1,2544,1,12,12,1,4,1,8),_F3TimeClockRefStorageType_Type())
f3TimeClockRefStorageType.setMaxAccess(_F)
if mibBuilder.loadTexts:f3TimeClockRefStorageType.setStatus(_A)
_F3TimeClockRefRowStatus_Type=RowStatus
_F3TimeClockRefRowStatus_Object=MibTableColumn
f3TimeClockRefRowStatus=_F3TimeClockRefRowStatus_Object((1,3,6,1,4,1,2544,1,12,12,1,4,1,9),_F3TimeClockRefRowStatus_Type())
f3TimeClockRefRowStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:f3TimeClockRefRowStatus.setStatus(_A)
_F3SyncConformance_ObjectIdentity=ObjectIdentity
f3SyncConformance=_F3SyncConformance_ObjectIdentity((1,3,6,1,4,1,2544,1,12,12,2))
_F3SyncCompliances_ObjectIdentity=ObjectIdentity
f3SyncCompliances=_F3SyncCompliances_ObjectIdentity((1,3,6,1,4,1,2544,1,12,12,2,1))
_F3SyncGroups_ObjectIdentity=ObjectIdentity
f3SyncGroups=_F3SyncGroups_ObjectIdentity((1,3,6,1,4,1,2544,1,12,12,2,2))
f3SyncObjectGroup=ObjectGroup((1,3,6,1,4,1,2544,1,12,12,2,2,1))
f3SyncObjectGroup.setObjects(*((_B,_K),(_B,_b),(_B,_c),(_B,_d),(_B,_e),(_B,_f),(_B,_g),(_B,_h),(_B,_i),(_B,_j),(_B,_k),(_B,_l),(_B,_m),(_B,_n),(_B,_Q),(_B,_o),(_B,_p),(_B,_q),(_B,_r),(_B,_s),(_B,_t),(_B,_u),(_B,_v),(_B,_w),(_B,_x)))
if mibBuilder.loadTexts:f3SyncObjectGroup.setStatus(_A)
f3TimeClockObjectGroup=ObjectGroup((1,3,6,1,4,1,2544,1,12,12,2,2,2))
f3TimeClockObjectGroup.setObjects(*((_B,_L),(_B,_y),(_B,_z),(_B,_A0),(_B,_A1),(_B,_A2),(_B,_A3),(_B,_A4),(_B,_A5),(_B,_A6),(_B,_A7),(_B,_A8),(_B,_A9),(_B,_AA),(_B,_AB),(_B,_AC),(_B,_AD),(_B,_AE),(_B,_AF),(_B,_AG),(_B,_AH),(_B,_R),(_B,_AI),(_B,_AJ),(_B,_AK),(_B,_AL),(_B,_AM),(_B,_AN),(_B,_AO),(_B,_AP)))
if mibBuilder.loadTexts:f3TimeClockObjectGroup.setStatus(_A)
f3SyncCompliance=ModuleCompliance((1,3,6,1,4,1,2544,1,12,12,2,1,1))
f3SyncCompliance.setObjects((_B,_AQ))
if mibBuilder.loadTexts:f3SyncCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'NetworkClockType':NetworkClockType,'ClockMode':ClockMode,'SSMQualityLevel':SSMQualityLevel,'SyncRefStatus':SyncRefStatus,'SyncRefState':SyncRefState,'SyncDomainType':SyncDomainType,'SyncOperationType':SyncOperationType,'SyncSelectionMode':SyncSelectionMode,'SquelchControl':SquelchControl,'TimeClockMode':TimeClockMode,'TimeTraceAbilityStatus':TimeTraceAbilityStatus,'HoldoverAccuracy':HoldoverAccuracy,'TimeHoldoverPerformance':TimeHoldoverPerformance,'TimeSource':TimeSource,'f3SyncMIB':f3SyncMIB,'f3SyncObjects':f3SyncObjects,'f3SyncTable':f3SyncTable,'f3SyncEntry':f3SyncEntry,_K:f3SyncIndex,_b:f3SyncAdminState,_c:f3SyncOperationalState,_d:f3SyncSecondaryState,_e:f3SyncNetworkClockType,_f:f3SyncSelectedReference,_g:f3SyncClockMode,_h:f3SyncQL,_i:f3SyncAlias,_j:f3SyncDomain,_k:f3SyncSelectionMode,_l:f3SyncWaitToRestoreTime,_m:f3SyncOperationSyncRef,_n:f3SyncOperationType,'f3SyncRefTable':f3SyncRefTable,'f3SyncRefEntry':f3SyncRefEntry,_Q:f3SyncRefIndex,_o:f3SyncRefReference,_p:f3SyncRefPriority,_q:f3SyncRefStatus,_r:f3SyncRefState,_s:f3SyncRefReceivedQL,_t:f3SyncRefStorageType,_u:f3SyncRefRowStatus,_v:f3SyncRefAlias,_w:f3SyncRefEffectiveQL,_x:f3SyncRefOperationType,'f3TimeClockTable':f3TimeClockTable,'f3TimeClockEntry':f3TimeClockEntry,_L:f3TimeClockIndex,_y:f3TimeClockAlias,_z:f3TimeClockAdminState,_A0:f3TimeClockOperationalState,_A1:f3TimeClockSecondaryState,_A2:f3TimeClockSelectedReference,_A3:f3TimeClockClockMode,_A4:f3TimeClockClockClass,_A5:f3TimeClockSelectionMode,_A6:f3TimeClockWaitToRestoreTime,_A7:f3TimeClockOperationTimeClockRef,_A8:f3TimeClockOperationType,_A9:f3TimeClockLeap59,_AA:f3TimeClockLeap61,_AB:f3TimeClockTimeTraceAbilityStatus,_AC:f3TimeClockExpectedQL,_AD:f3TimeClockCurrentQL,_AE:f3TimeClockSyncRefCandidate,_AF:f3TimeClockTimeHoldoverPerformance,_AG:f3TimeClockUtcOffset,_AH:f3TimeClockCurrentTimeOfDay,'f3TimeClockFrequencyReference':f3TimeClockFrequencyReference,'f3TimeClockFrequencyClockMode':f3TimeClockFrequencyClockMode,'f3TimeClockRefTable':f3TimeClockRefTable,'f3TimeClockRefEntry':f3TimeClockRefEntry,_R:f3TimeClockRefIndex,_AI:f3TimeClockRefAlias,_AJ:f3TimeClockRefReference,_AK:f3TimeClockRefPriority,_AL:f3TimeClockRefStatus,_AM:f3TimeClockRefState,_AN:f3TimeClockRefOperationType,_AO:f3TimeClockRefStorageType,_AP:f3TimeClockRefRowStatus,'f3SyncConformance':f3SyncConformance,'f3SyncCompliances':f3SyncCompliances,'f3SyncCompliance':f3SyncCompliance,'f3SyncGroups':f3SyncGroups,_AQ:f3SyncObjectGroup,'f3TimeClockObjectGroup':f3TimeClockObjectGroup})