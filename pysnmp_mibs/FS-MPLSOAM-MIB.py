_t='fsMplsPsGroup'
_s='fsMplsPsSwitchWtoP'
_r='fsMplsPsSwitchPtoW'
_q='fsMplsOamEgrEnable'
_p='fsMplsOamEgrDetFreq'
_o='fsMplsOamEgrDetType'
_n='fsMplsPsRowStatus'
_m='fsMplsPsProtLspState'
_l='fsMplsPsWorkLspState'
_k='fsMplsPsSwitchCondition'
_j='fsMplsPsHoldOff'
_i='fsMplsPsWTR'
_h='fsMplsPsRevertiveMode'
_g='fsMplsPsType'
_f='fsMplsPsGroupName'
_e='private'
_d='fsMplsPsIndex'
_c='enable'
_b='disable'
_a='ffd500ms5'
_Z='ffd200ms4'
_Y='ffd100ms3'
_X='ffd50ms2'
_W='cv1000ms'
_V='read-write'
_U='fsMplsPsSwitchResult'
_T='fsMplsPsProtectLspId'
_S='fsMplsPsProtectLspName'
_R='fsMplsPsWorkLspId'
_Q='fsMplsPsWorkLspName'
_P='Unsigned32'
_O='fsMplsOamEgrDefectType'
_N='fsMplsOamEgrAvaState'
_M='fsMplsOamIgrDefectType'
_L='fsMplsOamIgrAvaState'
_K='fsMplsOamIgrLspName'
_J='fsMplsOamIgrIndex'
_I='fsMplsOamEgrLspId'
_H='fsMplsOamEgrLsrId'
_G='fsMplsOamEgrLspName'
_F='fsMplsOamEgrIndex'
_E='read-create'
_D='read-only'
_C='Integer32'
_B='current'
_A='FS-MPLSOAM-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
fsMgmt,=mibBuilder.importSymbols('FS-SMI','fsMgmt')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_P,'iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TimeStamp,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention','TimeStamp','TruthValue')
fsMplsOam=ModuleIdentity((1,3,6,1,4,1,52642,1,1,10,2,93))
_FsMplsOamPs_ObjectIdentity=ObjectIdentity
fsMplsOamPs=_FsMplsOamPs_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,93,1))
_FsMplsOamObjects_ObjectIdentity=ObjectIdentity
fsMplsOamObjects=_FsMplsOamObjects_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,93,1,1))
class _FsMplsOamCapability_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_FsMplsOamCapability_Type.__name__=_P
_FsMplsOamCapability_Object=MibScalar
fsMplsOamCapability=_FsMplsOamCapability_Object((1,3,6,1,4,1,52642,1,1,10,2,93,1,1,1),_FsMplsOamCapability_Type())
fsMplsOamCapability.setMaxAccess(_V)
if mibBuilder.loadTexts:fsMplsOamCapability.setStatus(_B)
_FsMplsOamIgrTable_Object=MibTable
fsMplsOamIgrTable=_FsMplsOamIgrTable_Object((1,3,6,1,4,1,52642,1,1,10,2,93,1,1,2))
if mibBuilder.loadTexts:fsMplsOamIgrTable.setStatus(_B)
_FsMplsOamIgrEntry_Object=MibTableRow
fsMplsOamIgrEntry=_FsMplsOamIgrEntry_Object((1,3,6,1,4,1,52642,1,1,10,2,93,1,1,2,1))
fsMplsOamIgrEntry.setIndexNames((0,_A,_J))
if mibBuilder.loadTexts:fsMplsOamIgrEntry.setStatus(_B)
_FsMplsOamIgrIndex_Type=Unsigned32
_FsMplsOamIgrIndex_Object=MibTableColumn
fsMplsOamIgrIndex=_FsMplsOamIgrIndex_Object((1,3,6,1,4,1,52642,1,1,10,2,93,1,1,2,1,1),_FsMplsOamIgrIndex_Type())
fsMplsOamIgrIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:fsMplsOamIgrIndex.setStatus(_B)
_FsMplsOamIgrLspName_Type=OctetString
_FsMplsOamIgrLspName_Object=MibTableColumn
fsMplsOamIgrLspName=_FsMplsOamIgrLspName_Object((1,3,6,1,4,1,52642,1,1,10,2,93,1,1,2,1,2),_FsMplsOamIgrLspName_Type())
fsMplsOamIgrLspName.setMaxAccess(_E)
if mibBuilder.loadTexts:fsMplsOamIgrLspName.setStatus(_B)
class _FsMplsOamIgrLspId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_FsMplsOamIgrLspId_Type.__name__=_C
_FsMplsOamIgrLspId_Object=MibTableColumn
fsMplsOamIgrLspId=_FsMplsOamIgrLspId_Object((1,3,6,1,4,1,52642,1,1,10,2,93,1,1,2,1,3),_FsMplsOamIgrLspId_Type())
fsMplsOamIgrLspId.setMaxAccess(_E)
if mibBuilder.loadTexts:fsMplsOamIgrLspId.setStatus(_B)
class _FsMplsOamIgrDetType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('cv',1),('ffd',2)))
_FsMplsOamIgrDetType_Type.__name__=_C
_FsMplsOamIgrDetType_Object=MibTableColumn
fsMplsOamIgrDetType=_FsMplsOamIgrDetType_Object((1,3,6,1,4,1,52642,1,1,10,2,93,1,1,2,1,4),_FsMplsOamIgrDetType_Type())
fsMplsOamIgrDetType.setMaxAccess(_E)
if mibBuilder.loadTexts:fsMplsOamIgrDetType.setStatus(_B)
class _FsMplsOamIgrDetFreq_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4)));namedValues=NamedValues(*((_W,0),(_X,1),(_Y,2),(_Z,3),(_a,4)))
_FsMplsOamIgrDetFreq_Type.__name__=_C
_FsMplsOamIgrDetFreq_Object=MibTableColumn
fsMplsOamIgrDetFreq=_FsMplsOamIgrDetFreq_Object((1,3,6,1,4,1,52642,1,1,10,2,93,1,1,2,1,5),_FsMplsOamIgrDetFreq_Type())
fsMplsOamIgrDetFreq.setMaxAccess(_E)
if mibBuilder.loadTexts:fsMplsOamIgrDetFreq.setStatus(_B)
class _FsMplsOamIgrRevType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_e,1),('share',2)))
_FsMplsOamIgrRevType_Type.__name__=_C
_FsMplsOamIgrRevType_Object=MibTableColumn
fsMplsOamIgrRevType=_FsMplsOamIgrRevType_Object((1,3,6,1,4,1,52642,1,1,10,2,93,1,1,2,1,6),_FsMplsOamIgrRevType_Type())
fsMplsOamIgrRevType.setMaxAccess(_E)
if mibBuilder.loadTexts:fsMplsOamIgrRevType.setStatus(_B)
_FsMplsOamIgrRevLspName_Type=OctetString
_FsMplsOamIgrRevLspName_Object=MibTableColumn
fsMplsOamIgrRevLspName=_FsMplsOamIgrRevLspName_Object((1,3,6,1,4,1,52642,1,1,10,2,93,1,1,2,1,7),_FsMplsOamIgrRevLspName_Type())
fsMplsOamIgrRevLspName.setMaxAccess(_E)
if mibBuilder.loadTexts:fsMplsOamIgrRevLspName.setStatus(_B)
class _FsMplsOamIgrEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_b,0),(_c,1)))
_FsMplsOamIgrEnable_Type.__name__=_C
_FsMplsOamIgrEnable_Object=MibTableColumn
fsMplsOamIgrEnable=_FsMplsOamIgrEnable_Object((1,3,6,1,4,1,52642,1,1,10,2,93,1,1,2,1,8),_FsMplsOamIgrEnable_Type())
fsMplsOamIgrEnable.setMaxAccess(_E)
if mibBuilder.loadTexts:fsMplsOamIgrEnable.setStatus(_B)
class _FsMplsOamIgrValid_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_FsMplsOamIgrValid_Type.__name__=_C
_FsMplsOamIgrValid_Object=MibTableColumn
fsMplsOamIgrValid=_FsMplsOamIgrValid_Object((1,3,6,1,4,1,52642,1,1,10,2,93,1,1,2,1,9),_FsMplsOamIgrValid_Type())
fsMplsOamIgrValid.setMaxAccess(_D)
if mibBuilder.loadTexts:fsMplsOamIgrValid.setStatus(_B)
class _FsMplsOamIgrAvaState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_FsMplsOamIgrAvaState_Type.__name__=_C
_FsMplsOamIgrAvaState_Object=MibTableColumn
fsMplsOamIgrAvaState=_FsMplsOamIgrAvaState_Object((1,3,6,1,4,1,52642,1,1,10,2,93,1,1,2,1,10),_FsMplsOamIgrAvaState_Type())
fsMplsOamIgrAvaState.setMaxAccess(_D)
if mibBuilder.loadTexts:fsMplsOamIgrAvaState.setStatus(_B)
class _FsMplsOamIgrDefectType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_FsMplsOamIgrDefectType_Type.__name__=_C
_FsMplsOamIgrDefectType_Object=MibTableColumn
fsMplsOamIgrDefectType=_FsMplsOamIgrDefectType_Object((1,3,6,1,4,1,52642,1,1,10,2,93,1,1,2,1,11),_FsMplsOamIgrDefectType_Type())
fsMplsOamIgrDefectType.setMaxAccess(_D)
if mibBuilder.loadTexts:fsMplsOamIgrDefectType.setStatus(_B)
_FsMplsOamIgrRowStatus_Type=RowStatus
_FsMplsOamIgrRowStatus_Object=MibTableColumn
fsMplsOamIgrRowStatus=_FsMplsOamIgrRowStatus_Object((1,3,6,1,4,1,52642,1,1,10,2,93,1,1,2,1,12),_FsMplsOamIgrRowStatus_Type())
fsMplsOamIgrRowStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:fsMplsOamIgrRowStatus.setStatus(_B)
_FsMplsOamEgrTable_Object=MibTable
fsMplsOamEgrTable=_FsMplsOamEgrTable_Object((1,3,6,1,4,1,52642,1,1,10,2,93,1,1,3))
if mibBuilder.loadTexts:fsMplsOamEgrTable.setStatus(_B)
_FsMplsOamEgrEntry_Object=MibTableRow
fsMplsOamEgrEntry=_FsMplsOamEgrEntry_Object((1,3,6,1,4,1,52642,1,1,10,2,93,1,1,3,1))
fsMplsOamEgrEntry.setIndexNames((0,_A,_F))
if mibBuilder.loadTexts:fsMplsOamEgrEntry.setStatus(_B)
_FsMplsOamEgrIndex_Type=Unsigned32
_FsMplsOamEgrIndex_Object=MibTableColumn
fsMplsOamEgrIndex=_FsMplsOamEgrIndex_Object((1,3,6,1,4,1,52642,1,1,10,2,93,1,1,3,1,1),_FsMplsOamEgrIndex_Type())
fsMplsOamEgrIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:fsMplsOamEgrIndex.setStatus(_B)
_FsMplsOamEgrLspName_Type=OctetString
_FsMplsOamEgrLspName_Object=MibTableColumn
fsMplsOamEgrLspName=_FsMplsOamEgrLspName_Object((1,3,6,1,4,1,52642,1,1,10,2,93,1,1,3,1,2),_FsMplsOamEgrLspName_Type())
fsMplsOamEgrLspName.setMaxAccess(_E)
if mibBuilder.loadTexts:fsMplsOamEgrLspName.setStatus(_B)
_FsMplsOamEgrLsrId_Type=IpAddress
_FsMplsOamEgrLsrId_Object=MibTableColumn
fsMplsOamEgrLsrId=_FsMplsOamEgrLsrId_Object((1,3,6,1,4,1,52642,1,1,10,2,93,1,1,3,1,3),_FsMplsOamEgrLsrId_Type())
fsMplsOamEgrLsrId.setMaxAccess(_E)
if mibBuilder.loadTexts:fsMplsOamEgrLsrId.setStatus(_B)
class _FsMplsOamEgrLspId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_FsMplsOamEgrLspId_Type.__name__=_C
_FsMplsOamEgrLspId_Object=MibTableColumn
fsMplsOamEgrLspId=_FsMplsOamEgrLspId_Object((1,3,6,1,4,1,52642,1,1,10,2,93,1,1,3,1,4),_FsMplsOamEgrLspId_Type())
fsMplsOamEgrLspId.setMaxAccess(_E)
if mibBuilder.loadTexts:fsMplsOamEgrLspId.setStatus(_B)
class _FsMplsOamEgrDetType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('adaptability',0),('cv',1),('ffd',2)))
_FsMplsOamEgrDetType_Type.__name__=_C
_FsMplsOamEgrDetType_Object=MibTableColumn
fsMplsOamEgrDetType=_FsMplsOamEgrDetType_Object((1,3,6,1,4,1,52642,1,1,10,2,93,1,1,3,1,5),_FsMplsOamEgrDetType_Type())
fsMplsOamEgrDetType.setMaxAccess(_E)
if mibBuilder.loadTexts:fsMplsOamEgrDetType.setStatus(_B)
class _FsMplsOamEgrDetFreq_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5)));namedValues=NamedValues(*((_W,0),(_X,1),(_Y,2),(_Z,3),(_a,4),('invalid6',5)))
_FsMplsOamEgrDetFreq_Type.__name__=_C
_FsMplsOamEgrDetFreq_Object=MibTableColumn
fsMplsOamEgrDetFreq=_FsMplsOamEgrDetFreq_Object((1,3,6,1,4,1,52642,1,1,10,2,93,1,1,3,1,6),_FsMplsOamEgrDetFreq_Type())
fsMplsOamEgrDetFreq.setMaxAccess(_E)
if mibBuilder.loadTexts:fsMplsOamEgrDetFreq.setStatus(_B)
class _FsMplsOamEgrRevType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_e,0),('share',1)))
_FsMplsOamEgrRevType_Type.__name__=_C
_FsMplsOamEgrRevType_Object=MibTableColumn
fsMplsOamEgrRevType=_FsMplsOamEgrRevType_Object((1,3,6,1,4,1,52642,1,1,10,2,93,1,1,3,1,7),_FsMplsOamEgrRevType_Type())
fsMplsOamEgrRevType.setMaxAccess(_E)
if mibBuilder.loadTexts:fsMplsOamEgrRevType.setStatus(_B)
_FsMplsOamEgrRevLspName_Type=OctetString
_FsMplsOamEgrRevLspName_Object=MibTableColumn
fsMplsOamEgrRevLspName=_FsMplsOamEgrRevLspName_Object((1,3,6,1,4,1,52642,1,1,10,2,93,1,1,3,1,8),_FsMplsOamEgrRevLspName_Type())
fsMplsOamEgrRevLspName.setMaxAccess(_E)
if mibBuilder.loadTexts:fsMplsOamEgrRevLspName.setStatus(_B)
class _FsMplsOamEgrAutoEn_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_b,0),(_c,1)))
_FsMplsOamEgrAutoEn_Type.__name__=_C
_FsMplsOamEgrAutoEn_Object=MibTableColumn
fsMplsOamEgrAutoEn=_FsMplsOamEgrAutoEn_Object((1,3,6,1,4,1,52642,1,1,10,2,93,1,1,3,1,9),_FsMplsOamEgrAutoEn_Type())
fsMplsOamEgrAutoEn.setMaxAccess(_E)
if mibBuilder.loadTexts:fsMplsOamEgrAutoEn.setStatus(_B)
class _FsMplsOamEgrAutoOvertime_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_FsMplsOamEgrAutoOvertime_Type.__name__=_C
_FsMplsOamEgrAutoOvertime_Object=MibTableColumn
fsMplsOamEgrAutoOvertime=_FsMplsOamEgrAutoOvertime_Object((1,3,6,1,4,1,52642,1,1,10,2,93,1,1,3,1,10),_FsMplsOamEgrAutoOvertime_Type())
fsMplsOamEgrAutoOvertime.setMaxAccess(_E)
if mibBuilder.loadTexts:fsMplsOamEgrAutoOvertime.setStatus(_B)
class _FsMplsOamEgrBDIFreq_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4)));namedValues=NamedValues(*((_W,0),(_X,1),(_Y,2),(_Z,3),(_a,4)))
_FsMplsOamEgrBDIFreq_Type.__name__=_C
_FsMplsOamEgrBDIFreq_Object=MibTableColumn
fsMplsOamEgrBDIFreq=_FsMplsOamEgrBDIFreq_Object((1,3,6,1,4,1,52642,1,1,10,2,93,1,1,3,1,11),_FsMplsOamEgrBDIFreq_Type())
fsMplsOamEgrBDIFreq.setMaxAccess(_E)
if mibBuilder.loadTexts:fsMplsOamEgrBDIFreq.setStatus(_B)
class _FsMplsOamEgrEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_b,0),(_c,1)))
_FsMplsOamEgrEnable_Type.__name__=_C
_FsMplsOamEgrEnable_Object=MibTableColumn
fsMplsOamEgrEnable=_FsMplsOamEgrEnable_Object((1,3,6,1,4,1,52642,1,1,10,2,93,1,1,3,1,12),_FsMplsOamEgrEnable_Type())
fsMplsOamEgrEnable.setMaxAccess(_E)
if mibBuilder.loadTexts:fsMplsOamEgrEnable.setStatus(_B)
class _FsMplsOamEgrValid_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('stop',1),('start',2)))
_FsMplsOamEgrValid_Type.__name__=_C
_FsMplsOamEgrValid_Object=MibTableColumn
fsMplsOamEgrValid=_FsMplsOamEgrValid_Object((1,3,6,1,4,1,52642,1,1,10,2,93,1,1,3,1,13),_FsMplsOamEgrValid_Type())
fsMplsOamEgrValid.setMaxAccess(_D)
if mibBuilder.loadTexts:fsMplsOamEgrValid.setStatus(_B)
class _FsMplsOamEgrAvaState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_FsMplsOamEgrAvaState_Type.__name__=_C
_FsMplsOamEgrAvaState_Object=MibTableColumn
fsMplsOamEgrAvaState=_FsMplsOamEgrAvaState_Object((1,3,6,1,4,1,52642,1,1,10,2,93,1,1,3,1,14),_FsMplsOamEgrAvaState_Type())
fsMplsOamEgrAvaState.setMaxAccess(_D)
if mibBuilder.loadTexts:fsMplsOamEgrAvaState.setStatus(_B)
class _FsMplsOamEgrDefectType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_FsMplsOamEgrDefectType_Type.__name__=_C
_FsMplsOamEgrDefectType_Object=MibTableColumn
fsMplsOamEgrDefectType=_FsMplsOamEgrDefectType_Object((1,3,6,1,4,1,52642,1,1,10,2,93,1,1,3,1,15),_FsMplsOamEgrDefectType_Type())
fsMplsOamEgrDefectType.setMaxAccess(_D)
if mibBuilder.loadTexts:fsMplsOamEgrDefectType.setStatus(_B)
_FsMplsOamEgrRowStatus_Type=RowStatus
_FsMplsOamEgrRowStatus_Object=MibTableColumn
fsMplsOamEgrRowStatus=_FsMplsOamEgrRowStatus_Object((1,3,6,1,4,1,52642,1,1,10,2,93,1,1,3,1,16),_FsMplsOamEgrRowStatus_Type())
fsMplsOamEgrRowStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:fsMplsOamEgrRowStatus.setStatus(_B)
class _FsMplsOamTrapOpen_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_FsMplsOamTrapOpen_Type.__name__=_P
_FsMplsOamTrapOpen_Object=MibScalar
fsMplsOamTrapOpen=_FsMplsOamTrapOpen_Object((1,3,6,1,4,1,52642,1,1,10,2,93,1,1,4),_FsMplsOamTrapOpen_Type())
fsMplsOamTrapOpen.setMaxAccess(_V)
if mibBuilder.loadTexts:fsMplsOamTrapOpen.setStatus(_B)
_FsMplsOamNotifications_ObjectIdentity=ObjectIdentity
fsMplsOamNotifications=_FsMplsOamNotifications_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,93,1,2))
_FsMplsPsObjects_ObjectIdentity=ObjectIdentity
fsMplsPsObjects=_FsMplsPsObjects_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,93,1,3))
_FsMplsPsTable_Object=MibTable
fsMplsPsTable=_FsMplsPsTable_Object((1,3,6,1,4,1,52642,1,1,10,2,93,1,3,1))
if mibBuilder.loadTexts:fsMplsPsTable.setStatus(_B)
_FsMplsPsEntry_Object=MibTableRow
fsMplsPsEntry=_FsMplsPsEntry_Object((1,3,6,1,4,1,52642,1,1,10,2,93,1,3,1,1))
fsMplsPsEntry.setIndexNames((0,_A,_d))
if mibBuilder.loadTexts:fsMplsPsEntry.setStatus(_B)
_FsMplsPsIndex_Type=Unsigned32
_FsMplsPsIndex_Object=MibTableColumn
fsMplsPsIndex=_FsMplsPsIndex_Object((1,3,6,1,4,1,52642,1,1,10,2,93,1,3,1,1,1),_FsMplsPsIndex_Type())
fsMplsPsIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:fsMplsPsIndex.setStatus(_B)
_FsMplsPsGroupName_Type=OctetString
_FsMplsPsGroupName_Object=MibTableColumn
fsMplsPsGroupName=_FsMplsPsGroupName_Object((1,3,6,1,4,1,52642,1,1,10,2,93,1,3,1,1,2),_FsMplsPsGroupName_Type())
fsMplsPsGroupName.setMaxAccess(_D)
if mibBuilder.loadTexts:fsMplsPsGroupName.setStatus(_B)
class _FsMplsPsType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4))
_FsMplsPsType_Type.__name__=_C
_FsMplsPsType_Object=MibTableColumn
fsMplsPsType=_FsMplsPsType_Object((1,3,6,1,4,1,52642,1,1,10,2,93,1,3,1,1,3),_FsMplsPsType_Type())
fsMplsPsType.setMaxAccess(_D)
if mibBuilder.loadTexts:fsMplsPsType.setStatus(_B)
_FsMplsPsWorkLspName_Type=OctetString
_FsMplsPsWorkLspName_Object=MibTableColumn
fsMplsPsWorkLspName=_FsMplsPsWorkLspName_Object((1,3,6,1,4,1,52642,1,1,10,2,93,1,3,1,1,4),_FsMplsPsWorkLspName_Type())
fsMplsPsWorkLspName.setMaxAccess(_D)
if mibBuilder.loadTexts:fsMplsPsWorkLspName.setStatus(_B)
class _FsMplsPsWorkLspId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_FsMplsPsWorkLspId_Type.__name__=_C
_FsMplsPsWorkLspId_Object=MibTableColumn
fsMplsPsWorkLspId=_FsMplsPsWorkLspId_Object((1,3,6,1,4,1,52642,1,1,10,2,93,1,3,1,1,5),_FsMplsPsWorkLspId_Type())
fsMplsPsWorkLspId.setMaxAccess(_D)
if mibBuilder.loadTexts:fsMplsPsWorkLspId.setStatus(_B)
_FsMplsPsProtectLspName_Type=OctetString
_FsMplsPsProtectLspName_Object=MibTableColumn
fsMplsPsProtectLspName=_FsMplsPsProtectLspName_Object((1,3,6,1,4,1,52642,1,1,10,2,93,1,3,1,1,6),_FsMplsPsProtectLspName_Type())
fsMplsPsProtectLspName.setMaxAccess(_D)
if mibBuilder.loadTexts:fsMplsPsProtectLspName.setStatus(_B)
class _FsMplsPsProtectLspId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_FsMplsPsProtectLspId_Type.__name__=_C
_FsMplsPsProtectLspId_Object=MibTableColumn
fsMplsPsProtectLspId=_FsMplsPsProtectLspId_Object((1,3,6,1,4,1,52642,1,1,10,2,93,1,3,1,1,7),_FsMplsPsProtectLspId_Type())
fsMplsPsProtectLspId.setMaxAccess(_D)
if mibBuilder.loadTexts:fsMplsPsProtectLspId.setStatus(_B)
class _FsMplsPsRevertiveMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2))
_FsMplsPsRevertiveMode_Type.__name__=_C
_FsMplsPsRevertiveMode_Object=MibTableColumn
fsMplsPsRevertiveMode=_FsMplsPsRevertiveMode_Object((1,3,6,1,4,1,52642,1,1,10,2,93,1,3,1,1,8),_FsMplsPsRevertiveMode_Type())
fsMplsPsRevertiveMode.setMaxAccess(_D)
if mibBuilder.loadTexts:fsMplsPsRevertiveMode.setStatus(_B)
class _FsMplsPsWTR_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,60))
_FsMplsPsWTR_Type.__name__=_C
_FsMplsPsWTR_Object=MibTableColumn
fsMplsPsWTR=_FsMplsPsWTR_Object((1,3,6,1,4,1,52642,1,1,10,2,93,1,3,1,1,9),_FsMplsPsWTR_Type())
fsMplsPsWTR.setMaxAccess(_D)
if mibBuilder.loadTexts:fsMplsPsWTR.setStatus(_B)
class _FsMplsPsHoldOff_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_FsMplsPsHoldOff_Type.__name__=_C
_FsMplsPsHoldOff_Object=MibTableColumn
fsMplsPsHoldOff=_FsMplsPsHoldOff_Object((1,3,6,1,4,1,52642,1,1,10,2,93,1,3,1,1,10),_FsMplsPsHoldOff_Type())
fsMplsPsHoldOff.setMaxAccess(_D)
if mibBuilder.loadTexts:fsMplsPsHoldOff.setStatus(_B)
class _FsMplsPsSwitchCondition_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,9))
_FsMplsPsSwitchCondition_Type.__name__=_C
_FsMplsPsSwitchCondition_Object=MibTableColumn
fsMplsPsSwitchCondition=_FsMplsPsSwitchCondition_Object((1,3,6,1,4,1,52642,1,1,10,2,93,1,3,1,1,11),_FsMplsPsSwitchCondition_Type())
fsMplsPsSwitchCondition.setMaxAccess(_D)
if mibBuilder.loadTexts:fsMplsPsSwitchCondition.setStatus(_B)
class _FsMplsPsWorkLspState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2))
_FsMplsPsWorkLspState_Type.__name__=_C
_FsMplsPsWorkLspState_Object=MibTableColumn
fsMplsPsWorkLspState=_FsMplsPsWorkLspState_Object((1,3,6,1,4,1,52642,1,1,10,2,93,1,3,1,1,12),_FsMplsPsWorkLspState_Type())
fsMplsPsWorkLspState.setMaxAccess(_D)
if mibBuilder.loadTexts:fsMplsPsWorkLspState.setStatus(_B)
class _FsMplsPsProtLspState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2))
_FsMplsPsProtLspState_Type.__name__=_C
_FsMplsPsProtLspState_Object=MibTableColumn
fsMplsPsProtLspState=_FsMplsPsProtLspState_Object((1,3,6,1,4,1,52642,1,1,10,2,93,1,3,1,1,13),_FsMplsPsProtLspState_Type())
fsMplsPsProtLspState.setMaxAccess(_D)
if mibBuilder.loadTexts:fsMplsPsProtLspState.setStatus(_B)
class _FsMplsPsSwitchResult_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2))
_FsMplsPsSwitchResult_Type.__name__=_C
_FsMplsPsSwitchResult_Object=MibTableColumn
fsMplsPsSwitchResult=_FsMplsPsSwitchResult_Object((1,3,6,1,4,1,52642,1,1,10,2,93,1,3,1,1,14),_FsMplsPsSwitchResult_Type())
fsMplsPsSwitchResult.setMaxAccess(_D)
if mibBuilder.loadTexts:fsMplsPsSwitchResult.setStatus(_B)
_FsMplsPsRowStatus_Type=RowStatus
_FsMplsPsRowStatus_Object=MibTableColumn
fsMplsPsRowStatus=_FsMplsPsRowStatus_Object((1,3,6,1,4,1,52642,1,1,10,2,93,1,3,1,1,15),_FsMplsPsRowStatus_Type())
fsMplsPsRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:fsMplsPsRowStatus.setStatus(_B)
class _FsMplsPsTrapOpen_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2))
_FsMplsPsTrapOpen_Type.__name__=_P
_FsMplsPsTrapOpen_Object=MibScalar
fsMplsPsTrapOpen=_FsMplsPsTrapOpen_Object((1,3,6,1,4,1,52642,1,1,10,2,93,1,3,2),_FsMplsPsTrapOpen_Type())
fsMplsPsTrapOpen.setMaxAccess(_V)
if mibBuilder.loadTexts:fsMplsPsTrapOpen.setStatus(_B)
_FsMplsPsNotifications_ObjectIdentity=ObjectIdentity
fsMplsPsNotifications=_FsMplsPsNotifications_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,93,1,4))
_FsMplsOamPsConformance_ObjectIdentity=ObjectIdentity
fsMplsOamPsConformance=_FsMplsOamPsConformance_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,93,1,5))
_FsMplsOamPsCompliances_ObjectIdentity=ObjectIdentity
fsMplsOamPsCompliances=_FsMplsOamPsCompliances_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,93,1,5,1))
_FsMplsOamPsGroups_ObjectIdentity=ObjectIdentity
fsMplsOamPsGroups=_FsMplsOamPsGroups_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,93,1,5,2))
fsMplsPsGroup=ObjectGroup((1,3,6,1,4,1,52642,1,1,10,2,93,1,5,2,1))
fsMplsPsGroup.setObjects(*((_A,_f),(_A,_g),(_A,_Q),(_A,_R),(_A,_S),(_A,_T),(_A,_h),(_A,_i),(_A,_j),(_A,_k),(_A,_l),(_A,_m),(_A,_U),(_A,_n),(_A,_d)))
if mibBuilder.loadTexts:fsMplsPsGroup.setStatus(_B)
fsMplsOamIgrLSPOutDefect=NotificationType((1,3,6,1,4,1,52642,1,1,10,2,93,1,2,1))
fsMplsOamIgrLSPOutDefect.setObjects(*((_A,_J),(_A,_K),(_A,_L),(_A,_M)))
if mibBuilder.loadTexts:fsMplsOamIgrLSPOutDefect.setStatus(_B)
fsMplsOamIgrLSPInDefect=NotificationType((1,3,6,1,4,1,52642,1,1,10,2,93,1,2,2))
fsMplsOamIgrLSPInDefect.setObjects(*((_A,_J),(_A,_K),(_A,_L),(_A,_M)))
if mibBuilder.loadTexts:fsMplsOamIgrLSPInDefect.setStatus(_B)
fsMplsOamIgrLSPAva=NotificationType((1,3,6,1,4,1,52642,1,1,10,2,93,1,2,3))
fsMplsOamIgrLSPAva.setObjects(*((_A,_J),(_A,_K),(_A,_L),(_A,_M)))
if mibBuilder.loadTexts:fsMplsOamIgrLSPAva.setStatus(_B)
fsMplsOamIgrLSPUnAva=NotificationType((1,3,6,1,4,1,52642,1,1,10,2,93,1,2,4))
fsMplsOamIgrLSPUnAva.setObjects(*((_A,_J),(_A,_K),(_A,_L),(_A,_M)))
if mibBuilder.loadTexts:fsMplsOamIgrLSPUnAva.setStatus(_B)
fsMplsOamEgrLSPOutDefect=NotificationType((1,3,6,1,4,1,52642,1,1,10,2,93,1,2,5))
fsMplsOamEgrLSPOutDefect.setObjects(*((_A,_F),(_A,_G),(_A,_H),(_A,_I),(_A,_N),(_A,_O)))
if mibBuilder.loadTexts:fsMplsOamEgrLSPOutDefect.setStatus(_B)
fsMplsOamEgrLSPInDefect=NotificationType((1,3,6,1,4,1,52642,1,1,10,2,93,1,2,6))
fsMplsOamEgrLSPInDefect.setObjects(*((_A,_F),(_A,_G),(_A,_H),(_A,_I),(_A,_N),(_A,_O)))
if mibBuilder.loadTexts:fsMplsOamEgrLSPInDefect.setStatus(_B)
fsMplsOamEgrLSPAva=NotificationType((1,3,6,1,4,1,52642,1,1,10,2,93,1,2,7))
fsMplsOamEgrLSPAva.setObjects(*((_A,_F),(_A,_G),(_A,_H),(_A,_I),(_A,_N),(_A,_O)))
if mibBuilder.loadTexts:fsMplsOamEgrLSPAva.setStatus(_B)
fsMplsOamEgrLSPUnAva=NotificationType((1,3,6,1,4,1,52642,1,1,10,2,93,1,2,8))
fsMplsOamEgrLSPUnAva.setObjects(*((_A,_F),(_A,_G),(_A,_H),(_A,_I),(_A,_N),(_A,_O)))
if mibBuilder.loadTexts:fsMplsOamEgrLSPUnAva.setStatus(_B)
fsMplsOamEgrFirstPkt=NotificationType((1,3,6,1,4,1,52642,1,1,10,2,93,1,2,9))
fsMplsOamEgrFirstPkt.setObjects(*((_A,_F),(_A,_G),(_A,_H),(_A,_I),(_A,_o),(_A,_p)))
if mibBuilder.loadTexts:fsMplsOamEgrFirstPkt.setStatus(_B)
fsMplsOamEgrAutoProFDI=NotificationType((1,3,6,1,4,1,52642,1,1,10,2,93,1,2,10))
fsMplsOamEgrAutoProFDI.setObjects(*((_A,_F),(_A,_G),(_A,_H),(_A,_I),(_A,_q)))
if mibBuilder.loadTexts:fsMplsOamEgrAutoProFDI.setStatus(_B)
fsMplsPsSwitchPtoW=NotificationType((1,3,6,1,4,1,52642,1,1,10,2,93,1,4,1))
fsMplsPsSwitchPtoW.setObjects(*((_A,_Q),(_A,_R),(_A,_S),(_A,_T),(_A,_U)))
if mibBuilder.loadTexts:fsMplsPsSwitchPtoW.setStatus(_B)
fsMplsPsSwitchWtoP=NotificationType((1,3,6,1,4,1,52642,1,1,10,2,93,1,4,2))
fsMplsPsSwitchWtoP.setObjects(*((_A,_Q),(_A,_R),(_A,_S),(_A,_T),(_A,_U)))
if mibBuilder.loadTexts:fsMplsPsSwitchWtoP.setStatus(_B)
fsMplsPsNotificationGroup=NotificationGroup((1,3,6,1,4,1,52642,1,1,10,2,93,1,5,2,2))
fsMplsPsNotificationGroup.setObjects(*((_A,_r),(_A,_s)))
if mibBuilder.loadTexts:fsMplsPsNotificationGroup.setStatus(_B)
fsMplsOamPsGroupCompliance=ModuleCompliance((1,3,6,1,4,1,52642,1,1,10,2,93,1,5,1,1))
fsMplsOamPsGroupCompliance.setObjects((_A,_t))
if mibBuilder.loadTexts:fsMplsOamPsGroupCompliance.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'fsMplsOam':fsMplsOam,'fsMplsOamPs':fsMplsOamPs,'fsMplsOamObjects':fsMplsOamObjects,'fsMplsOamCapability':fsMplsOamCapability,'fsMplsOamIgrTable':fsMplsOamIgrTable,'fsMplsOamIgrEntry':fsMplsOamIgrEntry,_J:fsMplsOamIgrIndex,_K:fsMplsOamIgrLspName,'fsMplsOamIgrLspId':fsMplsOamIgrLspId,'fsMplsOamIgrDetType':fsMplsOamIgrDetType,'fsMplsOamIgrDetFreq':fsMplsOamIgrDetFreq,'fsMplsOamIgrRevType':fsMplsOamIgrRevType,'fsMplsOamIgrRevLspName':fsMplsOamIgrRevLspName,'fsMplsOamIgrEnable':fsMplsOamIgrEnable,'fsMplsOamIgrValid':fsMplsOamIgrValid,_L:fsMplsOamIgrAvaState,_M:fsMplsOamIgrDefectType,'fsMplsOamIgrRowStatus':fsMplsOamIgrRowStatus,'fsMplsOamEgrTable':fsMplsOamEgrTable,'fsMplsOamEgrEntry':fsMplsOamEgrEntry,_F:fsMplsOamEgrIndex,_G:fsMplsOamEgrLspName,_H:fsMplsOamEgrLsrId,_I:fsMplsOamEgrLspId,_o:fsMplsOamEgrDetType,_p:fsMplsOamEgrDetFreq,'fsMplsOamEgrRevType':fsMplsOamEgrRevType,'fsMplsOamEgrRevLspName':fsMplsOamEgrRevLspName,'fsMplsOamEgrAutoEn':fsMplsOamEgrAutoEn,'fsMplsOamEgrAutoOvertime':fsMplsOamEgrAutoOvertime,'fsMplsOamEgrBDIFreq':fsMplsOamEgrBDIFreq,_q:fsMplsOamEgrEnable,'fsMplsOamEgrValid':fsMplsOamEgrValid,_N:fsMplsOamEgrAvaState,_O:fsMplsOamEgrDefectType,'fsMplsOamEgrRowStatus':fsMplsOamEgrRowStatus,'fsMplsOamTrapOpen':fsMplsOamTrapOpen,'fsMplsOamNotifications':fsMplsOamNotifications,'fsMplsOamIgrLSPOutDefect':fsMplsOamIgrLSPOutDefect,'fsMplsOamIgrLSPInDefect':fsMplsOamIgrLSPInDefect,'fsMplsOamIgrLSPAva':fsMplsOamIgrLSPAva,'fsMplsOamIgrLSPUnAva':fsMplsOamIgrLSPUnAva,'fsMplsOamEgrLSPOutDefect':fsMplsOamEgrLSPOutDefect,'fsMplsOamEgrLSPInDefect':fsMplsOamEgrLSPInDefect,'fsMplsOamEgrLSPAva':fsMplsOamEgrLSPAva,'fsMplsOamEgrLSPUnAva':fsMplsOamEgrLSPUnAva,'fsMplsOamEgrFirstPkt':fsMplsOamEgrFirstPkt,'fsMplsOamEgrAutoProFDI':fsMplsOamEgrAutoProFDI,'fsMplsPsObjects':fsMplsPsObjects,'fsMplsPsTable':fsMplsPsTable,'fsMplsPsEntry':fsMplsPsEntry,_d:fsMplsPsIndex,_f:fsMplsPsGroupName,_g:fsMplsPsType,_Q:fsMplsPsWorkLspName,_R:fsMplsPsWorkLspId,_S:fsMplsPsProtectLspName,_T:fsMplsPsProtectLspId,_h:fsMplsPsRevertiveMode,_i:fsMplsPsWTR,_j:fsMplsPsHoldOff,_k:fsMplsPsSwitchCondition,_l:fsMplsPsWorkLspState,_m:fsMplsPsProtLspState,_U:fsMplsPsSwitchResult,_n:fsMplsPsRowStatus,'fsMplsPsTrapOpen':fsMplsPsTrapOpen,'fsMplsPsNotifications':fsMplsPsNotifications,_r:fsMplsPsSwitchPtoW,_s:fsMplsPsSwitchWtoP,'fsMplsOamPsConformance':fsMplsOamPsConformance,'fsMplsOamPsCompliances':fsMplsOamPsCompliances,'fsMplsOamPsGroupCompliance':fsMplsOamPsGroupCompliance,'fsMplsOamPsGroups':fsMplsOamPsGroups,_t:fsMplsPsGroup,'fsMplsPsNotificationGroup':fsMplsPsNotificationGroup})