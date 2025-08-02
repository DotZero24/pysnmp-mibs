_t='qtechMplsPsGroup'
_s='qtechMplsPsSwitchWtoP'
_r='qtechMplsPsSwitchPtoW'
_q='qtechMplsOamEgrEnable'
_p='qtechMplsOamEgrDetFreq'
_o='qtechMplsOamEgrDetType'
_n='qtechMplsPsRowStatus'
_m='qtechMplsPsProtLspState'
_l='qtechMplsPsWorkLspState'
_k='qtechMplsPsSwitchCondition'
_j='qtechMplsPsHoldOff'
_i='qtechMplsPsWTR'
_h='qtechMplsPsRevertiveMode'
_g='qtechMplsPsType'
_f='qtechMplsPsGroupName'
_e='private'
_d='qtechMplsPsIndex'
_c='enable'
_b='disable'
_a='ffd500ms5'
_Z='ffd200ms4'
_Y='ffd100ms3'
_X='ffd50ms2'
_W='cv1000ms'
_V='read-write'
_U='qtechMplsPsSwitchResult'
_T='qtechMplsPsProtectLspId'
_S='qtechMplsPsProtectLspName'
_R='qtechMplsPsWorkLspId'
_Q='qtechMplsPsWorkLspName'
_P='Unsigned32'
_O='qtechMplsOamEgrDefectType'
_N='qtechMplsOamEgrAvaState'
_M='qtechMplsOamIgrDefectType'
_L='qtechMplsOamIgrAvaState'
_K='qtechMplsOamIgrLspName'
_J='qtechMplsOamIgrIndex'
_I='qtechMplsOamEgrLspId'
_H='qtechMplsOamEgrLsrId'
_G='qtechMplsOamEgrLspName'
_F='qtechMplsOamEgrIndex'
_E='read-create'
_D='read-only'
_C='Integer32'
_B='current'
_A='QTECH-MPLSOAM-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
qtechMgmt,=mibBuilder.importSymbols('QTECH-SMI','qtechMgmt')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_P,'iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TimeStamp,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention','TimeStamp','TruthValue')
qtechMplsOam=ModuleIdentity((1,3,6,1,4,1,27514,1,1,10,2,93))
_QtechMplsOamPs_ObjectIdentity=ObjectIdentity
qtechMplsOamPs=_QtechMplsOamPs_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,93,1))
_QtechMplsOamObjects_ObjectIdentity=ObjectIdentity
qtechMplsOamObjects=_QtechMplsOamObjects_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,93,1,1))
class _QtechMplsOamCapability_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_QtechMplsOamCapability_Type.__name__=_P
_QtechMplsOamCapability_Object=MibScalar
qtechMplsOamCapability=_QtechMplsOamCapability_Object((1,3,6,1,4,1,27514,1,1,10,2,93,1,1,1),_QtechMplsOamCapability_Type())
qtechMplsOamCapability.setMaxAccess(_V)
if mibBuilder.loadTexts:qtechMplsOamCapability.setStatus(_B)
_QtechMplsOamIgrTable_Object=MibTable
qtechMplsOamIgrTable=_QtechMplsOamIgrTable_Object((1,3,6,1,4,1,27514,1,1,10,2,93,1,1,2))
if mibBuilder.loadTexts:qtechMplsOamIgrTable.setStatus(_B)
_QtechMplsOamIgrEntry_Object=MibTableRow
qtechMplsOamIgrEntry=_QtechMplsOamIgrEntry_Object((1,3,6,1,4,1,27514,1,1,10,2,93,1,1,2,1))
qtechMplsOamIgrEntry.setIndexNames((0,_A,_J))
if mibBuilder.loadTexts:qtechMplsOamIgrEntry.setStatus(_B)
_QtechMplsOamIgrIndex_Type=Unsigned32
_QtechMplsOamIgrIndex_Object=MibTableColumn
qtechMplsOamIgrIndex=_QtechMplsOamIgrIndex_Object((1,3,6,1,4,1,27514,1,1,10,2,93,1,1,2,1,1),_QtechMplsOamIgrIndex_Type())
qtechMplsOamIgrIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechMplsOamIgrIndex.setStatus(_B)
_QtechMplsOamIgrLspName_Type=OctetString
_QtechMplsOamIgrLspName_Object=MibTableColumn
qtechMplsOamIgrLspName=_QtechMplsOamIgrLspName_Object((1,3,6,1,4,1,27514,1,1,10,2,93,1,1,2,1,2),_QtechMplsOamIgrLspName_Type())
qtechMplsOamIgrLspName.setMaxAccess(_E)
if mibBuilder.loadTexts:qtechMplsOamIgrLspName.setStatus(_B)
class _QtechMplsOamIgrLspId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_QtechMplsOamIgrLspId_Type.__name__=_C
_QtechMplsOamIgrLspId_Object=MibTableColumn
qtechMplsOamIgrLspId=_QtechMplsOamIgrLspId_Object((1,3,6,1,4,1,27514,1,1,10,2,93,1,1,2,1,3),_QtechMplsOamIgrLspId_Type())
qtechMplsOamIgrLspId.setMaxAccess(_E)
if mibBuilder.loadTexts:qtechMplsOamIgrLspId.setStatus(_B)
class _QtechMplsOamIgrDetType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('cv',1),('ffd',2)))
_QtechMplsOamIgrDetType_Type.__name__=_C
_QtechMplsOamIgrDetType_Object=MibTableColumn
qtechMplsOamIgrDetType=_QtechMplsOamIgrDetType_Object((1,3,6,1,4,1,27514,1,1,10,2,93,1,1,2,1,4),_QtechMplsOamIgrDetType_Type())
qtechMplsOamIgrDetType.setMaxAccess(_E)
if mibBuilder.loadTexts:qtechMplsOamIgrDetType.setStatus(_B)
class _QtechMplsOamIgrDetFreq_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4)));namedValues=NamedValues(*((_W,0),(_X,1),(_Y,2),(_Z,3),(_a,4)))
_QtechMplsOamIgrDetFreq_Type.__name__=_C
_QtechMplsOamIgrDetFreq_Object=MibTableColumn
qtechMplsOamIgrDetFreq=_QtechMplsOamIgrDetFreq_Object((1,3,6,1,4,1,27514,1,1,10,2,93,1,1,2,1,5),_QtechMplsOamIgrDetFreq_Type())
qtechMplsOamIgrDetFreq.setMaxAccess(_E)
if mibBuilder.loadTexts:qtechMplsOamIgrDetFreq.setStatus(_B)
class _QtechMplsOamIgrRevType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_e,1),('share',2)))
_QtechMplsOamIgrRevType_Type.__name__=_C
_QtechMplsOamIgrRevType_Object=MibTableColumn
qtechMplsOamIgrRevType=_QtechMplsOamIgrRevType_Object((1,3,6,1,4,1,27514,1,1,10,2,93,1,1,2,1,6),_QtechMplsOamIgrRevType_Type())
qtechMplsOamIgrRevType.setMaxAccess(_E)
if mibBuilder.loadTexts:qtechMplsOamIgrRevType.setStatus(_B)
_QtechMplsOamIgrRevLspName_Type=OctetString
_QtechMplsOamIgrRevLspName_Object=MibTableColumn
qtechMplsOamIgrRevLspName=_QtechMplsOamIgrRevLspName_Object((1,3,6,1,4,1,27514,1,1,10,2,93,1,1,2,1,7),_QtechMplsOamIgrRevLspName_Type())
qtechMplsOamIgrRevLspName.setMaxAccess(_E)
if mibBuilder.loadTexts:qtechMplsOamIgrRevLspName.setStatus(_B)
class _QtechMplsOamIgrEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_b,0),(_c,1)))
_QtechMplsOamIgrEnable_Type.__name__=_C
_QtechMplsOamIgrEnable_Object=MibTableColumn
qtechMplsOamIgrEnable=_QtechMplsOamIgrEnable_Object((1,3,6,1,4,1,27514,1,1,10,2,93,1,1,2,1,8),_QtechMplsOamIgrEnable_Type())
qtechMplsOamIgrEnable.setMaxAccess(_E)
if mibBuilder.loadTexts:qtechMplsOamIgrEnable.setStatus(_B)
class _QtechMplsOamIgrValid_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_QtechMplsOamIgrValid_Type.__name__=_C
_QtechMplsOamIgrValid_Object=MibTableColumn
qtechMplsOamIgrValid=_QtechMplsOamIgrValid_Object((1,3,6,1,4,1,27514,1,1,10,2,93,1,1,2,1,9),_QtechMplsOamIgrValid_Type())
qtechMplsOamIgrValid.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechMplsOamIgrValid.setStatus(_B)
class _QtechMplsOamIgrAvaState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_QtechMplsOamIgrAvaState_Type.__name__=_C
_QtechMplsOamIgrAvaState_Object=MibTableColumn
qtechMplsOamIgrAvaState=_QtechMplsOamIgrAvaState_Object((1,3,6,1,4,1,27514,1,1,10,2,93,1,1,2,1,10),_QtechMplsOamIgrAvaState_Type())
qtechMplsOamIgrAvaState.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechMplsOamIgrAvaState.setStatus(_B)
class _QtechMplsOamIgrDefectType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_QtechMplsOamIgrDefectType_Type.__name__=_C
_QtechMplsOamIgrDefectType_Object=MibTableColumn
qtechMplsOamIgrDefectType=_QtechMplsOamIgrDefectType_Object((1,3,6,1,4,1,27514,1,1,10,2,93,1,1,2,1,11),_QtechMplsOamIgrDefectType_Type())
qtechMplsOamIgrDefectType.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechMplsOamIgrDefectType.setStatus(_B)
_QtechMplsOamIgrRowStatus_Type=RowStatus
_QtechMplsOamIgrRowStatus_Object=MibTableColumn
qtechMplsOamIgrRowStatus=_QtechMplsOamIgrRowStatus_Object((1,3,6,1,4,1,27514,1,1,10,2,93,1,1,2,1,12),_QtechMplsOamIgrRowStatus_Type())
qtechMplsOamIgrRowStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:qtechMplsOamIgrRowStatus.setStatus(_B)
_QtechMplsOamEgrTable_Object=MibTable
qtechMplsOamEgrTable=_QtechMplsOamEgrTable_Object((1,3,6,1,4,1,27514,1,1,10,2,93,1,1,3))
if mibBuilder.loadTexts:qtechMplsOamEgrTable.setStatus(_B)
_QtechMplsOamEgrEntry_Object=MibTableRow
qtechMplsOamEgrEntry=_QtechMplsOamEgrEntry_Object((1,3,6,1,4,1,27514,1,1,10,2,93,1,1,3,1))
qtechMplsOamEgrEntry.setIndexNames((0,_A,_F))
if mibBuilder.loadTexts:qtechMplsOamEgrEntry.setStatus(_B)
_QtechMplsOamEgrIndex_Type=Unsigned32
_QtechMplsOamEgrIndex_Object=MibTableColumn
qtechMplsOamEgrIndex=_QtechMplsOamEgrIndex_Object((1,3,6,1,4,1,27514,1,1,10,2,93,1,1,3,1,1),_QtechMplsOamEgrIndex_Type())
qtechMplsOamEgrIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechMplsOamEgrIndex.setStatus(_B)
_QtechMplsOamEgrLspName_Type=OctetString
_QtechMplsOamEgrLspName_Object=MibTableColumn
qtechMplsOamEgrLspName=_QtechMplsOamEgrLspName_Object((1,3,6,1,4,1,27514,1,1,10,2,93,1,1,3,1,2),_QtechMplsOamEgrLspName_Type())
qtechMplsOamEgrLspName.setMaxAccess(_E)
if mibBuilder.loadTexts:qtechMplsOamEgrLspName.setStatus(_B)
_QtechMplsOamEgrLsrId_Type=IpAddress
_QtechMplsOamEgrLsrId_Object=MibTableColumn
qtechMplsOamEgrLsrId=_QtechMplsOamEgrLsrId_Object((1,3,6,1,4,1,27514,1,1,10,2,93,1,1,3,1,3),_QtechMplsOamEgrLsrId_Type())
qtechMplsOamEgrLsrId.setMaxAccess(_E)
if mibBuilder.loadTexts:qtechMplsOamEgrLsrId.setStatus(_B)
class _QtechMplsOamEgrLspId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_QtechMplsOamEgrLspId_Type.__name__=_C
_QtechMplsOamEgrLspId_Object=MibTableColumn
qtechMplsOamEgrLspId=_QtechMplsOamEgrLspId_Object((1,3,6,1,4,1,27514,1,1,10,2,93,1,1,3,1,4),_QtechMplsOamEgrLspId_Type())
qtechMplsOamEgrLspId.setMaxAccess(_E)
if mibBuilder.loadTexts:qtechMplsOamEgrLspId.setStatus(_B)
class _QtechMplsOamEgrDetType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('adaptability',0),('cv',1),('ffd',2)))
_QtechMplsOamEgrDetType_Type.__name__=_C
_QtechMplsOamEgrDetType_Object=MibTableColumn
qtechMplsOamEgrDetType=_QtechMplsOamEgrDetType_Object((1,3,6,1,4,1,27514,1,1,10,2,93,1,1,3,1,5),_QtechMplsOamEgrDetType_Type())
qtechMplsOamEgrDetType.setMaxAccess(_E)
if mibBuilder.loadTexts:qtechMplsOamEgrDetType.setStatus(_B)
class _QtechMplsOamEgrDetFreq_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5)));namedValues=NamedValues(*((_W,0),(_X,1),(_Y,2),(_Z,3),(_a,4),('invalid6',5)))
_QtechMplsOamEgrDetFreq_Type.__name__=_C
_QtechMplsOamEgrDetFreq_Object=MibTableColumn
qtechMplsOamEgrDetFreq=_QtechMplsOamEgrDetFreq_Object((1,3,6,1,4,1,27514,1,1,10,2,93,1,1,3,1,6),_QtechMplsOamEgrDetFreq_Type())
qtechMplsOamEgrDetFreq.setMaxAccess(_E)
if mibBuilder.loadTexts:qtechMplsOamEgrDetFreq.setStatus(_B)
class _QtechMplsOamEgrRevType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_e,0),('share',1)))
_QtechMplsOamEgrRevType_Type.__name__=_C
_QtechMplsOamEgrRevType_Object=MibTableColumn
qtechMplsOamEgrRevType=_QtechMplsOamEgrRevType_Object((1,3,6,1,4,1,27514,1,1,10,2,93,1,1,3,1,7),_QtechMplsOamEgrRevType_Type())
qtechMplsOamEgrRevType.setMaxAccess(_E)
if mibBuilder.loadTexts:qtechMplsOamEgrRevType.setStatus(_B)
_QtechMplsOamEgrRevLspName_Type=OctetString
_QtechMplsOamEgrRevLspName_Object=MibTableColumn
qtechMplsOamEgrRevLspName=_QtechMplsOamEgrRevLspName_Object((1,3,6,1,4,1,27514,1,1,10,2,93,1,1,3,1,8),_QtechMplsOamEgrRevLspName_Type())
qtechMplsOamEgrRevLspName.setMaxAccess(_E)
if mibBuilder.loadTexts:qtechMplsOamEgrRevLspName.setStatus(_B)
class _QtechMplsOamEgrAutoEn_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_b,0),(_c,1)))
_QtechMplsOamEgrAutoEn_Type.__name__=_C
_QtechMplsOamEgrAutoEn_Object=MibTableColumn
qtechMplsOamEgrAutoEn=_QtechMplsOamEgrAutoEn_Object((1,3,6,1,4,1,27514,1,1,10,2,93,1,1,3,1,9),_QtechMplsOamEgrAutoEn_Type())
qtechMplsOamEgrAutoEn.setMaxAccess(_E)
if mibBuilder.loadTexts:qtechMplsOamEgrAutoEn.setStatus(_B)
class _QtechMplsOamEgrAutoOvertime_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_QtechMplsOamEgrAutoOvertime_Type.__name__=_C
_QtechMplsOamEgrAutoOvertime_Object=MibTableColumn
qtechMplsOamEgrAutoOvertime=_QtechMplsOamEgrAutoOvertime_Object((1,3,6,1,4,1,27514,1,1,10,2,93,1,1,3,1,10),_QtechMplsOamEgrAutoOvertime_Type())
qtechMplsOamEgrAutoOvertime.setMaxAccess(_E)
if mibBuilder.loadTexts:qtechMplsOamEgrAutoOvertime.setStatus(_B)
class _QtechMplsOamEgrBDIFreq_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4)));namedValues=NamedValues(*((_W,0),(_X,1),(_Y,2),(_Z,3),(_a,4)))
_QtechMplsOamEgrBDIFreq_Type.__name__=_C
_QtechMplsOamEgrBDIFreq_Object=MibTableColumn
qtechMplsOamEgrBDIFreq=_QtechMplsOamEgrBDIFreq_Object((1,3,6,1,4,1,27514,1,1,10,2,93,1,1,3,1,11),_QtechMplsOamEgrBDIFreq_Type())
qtechMplsOamEgrBDIFreq.setMaxAccess(_E)
if mibBuilder.loadTexts:qtechMplsOamEgrBDIFreq.setStatus(_B)
class _QtechMplsOamEgrEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_b,0),(_c,1)))
_QtechMplsOamEgrEnable_Type.__name__=_C
_QtechMplsOamEgrEnable_Object=MibTableColumn
qtechMplsOamEgrEnable=_QtechMplsOamEgrEnable_Object((1,3,6,1,4,1,27514,1,1,10,2,93,1,1,3,1,12),_QtechMplsOamEgrEnable_Type())
qtechMplsOamEgrEnable.setMaxAccess(_E)
if mibBuilder.loadTexts:qtechMplsOamEgrEnable.setStatus(_B)
class _QtechMplsOamEgrValid_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('stop',1),('start',2)))
_QtechMplsOamEgrValid_Type.__name__=_C
_QtechMplsOamEgrValid_Object=MibTableColumn
qtechMplsOamEgrValid=_QtechMplsOamEgrValid_Object((1,3,6,1,4,1,27514,1,1,10,2,93,1,1,3,1,13),_QtechMplsOamEgrValid_Type())
qtechMplsOamEgrValid.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechMplsOamEgrValid.setStatus(_B)
class _QtechMplsOamEgrAvaState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_QtechMplsOamEgrAvaState_Type.__name__=_C
_QtechMplsOamEgrAvaState_Object=MibTableColumn
qtechMplsOamEgrAvaState=_QtechMplsOamEgrAvaState_Object((1,3,6,1,4,1,27514,1,1,10,2,93,1,1,3,1,14),_QtechMplsOamEgrAvaState_Type())
qtechMplsOamEgrAvaState.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechMplsOamEgrAvaState.setStatus(_B)
class _QtechMplsOamEgrDefectType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_QtechMplsOamEgrDefectType_Type.__name__=_C
_QtechMplsOamEgrDefectType_Object=MibTableColumn
qtechMplsOamEgrDefectType=_QtechMplsOamEgrDefectType_Object((1,3,6,1,4,1,27514,1,1,10,2,93,1,1,3,1,15),_QtechMplsOamEgrDefectType_Type())
qtechMplsOamEgrDefectType.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechMplsOamEgrDefectType.setStatus(_B)
_QtechMplsOamEgrRowStatus_Type=RowStatus
_QtechMplsOamEgrRowStatus_Object=MibTableColumn
qtechMplsOamEgrRowStatus=_QtechMplsOamEgrRowStatus_Object((1,3,6,1,4,1,27514,1,1,10,2,93,1,1,3,1,16),_QtechMplsOamEgrRowStatus_Type())
qtechMplsOamEgrRowStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:qtechMplsOamEgrRowStatus.setStatus(_B)
class _QtechMplsOamTrapOpen_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_QtechMplsOamTrapOpen_Type.__name__=_P
_QtechMplsOamTrapOpen_Object=MibScalar
qtechMplsOamTrapOpen=_QtechMplsOamTrapOpen_Object((1,3,6,1,4,1,27514,1,1,10,2,93,1,1,4),_QtechMplsOamTrapOpen_Type())
qtechMplsOamTrapOpen.setMaxAccess(_V)
if mibBuilder.loadTexts:qtechMplsOamTrapOpen.setStatus(_B)
_QtechMplsOamNotifications_ObjectIdentity=ObjectIdentity
qtechMplsOamNotifications=_QtechMplsOamNotifications_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,93,1,2))
_QtechMplsPsObjects_ObjectIdentity=ObjectIdentity
qtechMplsPsObjects=_QtechMplsPsObjects_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,93,1,3))
_QtechMplsPsTable_Object=MibTable
qtechMplsPsTable=_QtechMplsPsTable_Object((1,3,6,1,4,1,27514,1,1,10,2,93,1,3,1))
if mibBuilder.loadTexts:qtechMplsPsTable.setStatus(_B)
_QtechMplsPsEntry_Object=MibTableRow
qtechMplsPsEntry=_QtechMplsPsEntry_Object((1,3,6,1,4,1,27514,1,1,10,2,93,1,3,1,1))
qtechMplsPsEntry.setIndexNames((0,_A,_d))
if mibBuilder.loadTexts:qtechMplsPsEntry.setStatus(_B)
_QtechMplsPsIndex_Type=Unsigned32
_QtechMplsPsIndex_Object=MibTableColumn
qtechMplsPsIndex=_QtechMplsPsIndex_Object((1,3,6,1,4,1,27514,1,1,10,2,93,1,3,1,1,1),_QtechMplsPsIndex_Type())
qtechMplsPsIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechMplsPsIndex.setStatus(_B)
_QtechMplsPsGroupName_Type=OctetString
_QtechMplsPsGroupName_Object=MibTableColumn
qtechMplsPsGroupName=_QtechMplsPsGroupName_Object((1,3,6,1,4,1,27514,1,1,10,2,93,1,3,1,1,2),_QtechMplsPsGroupName_Type())
qtechMplsPsGroupName.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechMplsPsGroupName.setStatus(_B)
class _QtechMplsPsType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4))
_QtechMplsPsType_Type.__name__=_C
_QtechMplsPsType_Object=MibTableColumn
qtechMplsPsType=_QtechMplsPsType_Object((1,3,6,1,4,1,27514,1,1,10,2,93,1,3,1,1,3),_QtechMplsPsType_Type())
qtechMplsPsType.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechMplsPsType.setStatus(_B)
_QtechMplsPsWorkLspName_Type=OctetString
_QtechMplsPsWorkLspName_Object=MibTableColumn
qtechMplsPsWorkLspName=_QtechMplsPsWorkLspName_Object((1,3,6,1,4,1,27514,1,1,10,2,93,1,3,1,1,4),_QtechMplsPsWorkLspName_Type())
qtechMplsPsWorkLspName.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechMplsPsWorkLspName.setStatus(_B)
class _QtechMplsPsWorkLspId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_QtechMplsPsWorkLspId_Type.__name__=_C
_QtechMplsPsWorkLspId_Object=MibTableColumn
qtechMplsPsWorkLspId=_QtechMplsPsWorkLspId_Object((1,3,6,1,4,1,27514,1,1,10,2,93,1,3,1,1,5),_QtechMplsPsWorkLspId_Type())
qtechMplsPsWorkLspId.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechMplsPsWorkLspId.setStatus(_B)
_QtechMplsPsProtectLspName_Type=OctetString
_QtechMplsPsProtectLspName_Object=MibTableColumn
qtechMplsPsProtectLspName=_QtechMplsPsProtectLspName_Object((1,3,6,1,4,1,27514,1,1,10,2,93,1,3,1,1,6),_QtechMplsPsProtectLspName_Type())
qtechMplsPsProtectLspName.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechMplsPsProtectLspName.setStatus(_B)
class _QtechMplsPsProtectLspId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_QtechMplsPsProtectLspId_Type.__name__=_C
_QtechMplsPsProtectLspId_Object=MibTableColumn
qtechMplsPsProtectLspId=_QtechMplsPsProtectLspId_Object((1,3,6,1,4,1,27514,1,1,10,2,93,1,3,1,1,7),_QtechMplsPsProtectLspId_Type())
qtechMplsPsProtectLspId.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechMplsPsProtectLspId.setStatus(_B)
class _QtechMplsPsRevertiveMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2))
_QtechMplsPsRevertiveMode_Type.__name__=_C
_QtechMplsPsRevertiveMode_Object=MibTableColumn
qtechMplsPsRevertiveMode=_QtechMplsPsRevertiveMode_Object((1,3,6,1,4,1,27514,1,1,10,2,93,1,3,1,1,8),_QtechMplsPsRevertiveMode_Type())
qtechMplsPsRevertiveMode.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechMplsPsRevertiveMode.setStatus(_B)
class _QtechMplsPsWTR_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,60))
_QtechMplsPsWTR_Type.__name__=_C
_QtechMplsPsWTR_Object=MibTableColumn
qtechMplsPsWTR=_QtechMplsPsWTR_Object((1,3,6,1,4,1,27514,1,1,10,2,93,1,3,1,1,9),_QtechMplsPsWTR_Type())
qtechMplsPsWTR.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechMplsPsWTR.setStatus(_B)
class _QtechMplsPsHoldOff_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_QtechMplsPsHoldOff_Type.__name__=_C
_QtechMplsPsHoldOff_Object=MibTableColumn
qtechMplsPsHoldOff=_QtechMplsPsHoldOff_Object((1,3,6,1,4,1,27514,1,1,10,2,93,1,3,1,1,10),_QtechMplsPsHoldOff_Type())
qtechMplsPsHoldOff.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechMplsPsHoldOff.setStatus(_B)
class _QtechMplsPsSwitchCondition_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,9))
_QtechMplsPsSwitchCondition_Type.__name__=_C
_QtechMplsPsSwitchCondition_Object=MibTableColumn
qtechMplsPsSwitchCondition=_QtechMplsPsSwitchCondition_Object((1,3,6,1,4,1,27514,1,1,10,2,93,1,3,1,1,11),_QtechMplsPsSwitchCondition_Type())
qtechMplsPsSwitchCondition.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechMplsPsSwitchCondition.setStatus(_B)
class _QtechMplsPsWorkLspState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2))
_QtechMplsPsWorkLspState_Type.__name__=_C
_QtechMplsPsWorkLspState_Object=MibTableColumn
qtechMplsPsWorkLspState=_QtechMplsPsWorkLspState_Object((1,3,6,1,4,1,27514,1,1,10,2,93,1,3,1,1,12),_QtechMplsPsWorkLspState_Type())
qtechMplsPsWorkLspState.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechMplsPsWorkLspState.setStatus(_B)
class _QtechMplsPsProtLspState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2))
_QtechMplsPsProtLspState_Type.__name__=_C
_QtechMplsPsProtLspState_Object=MibTableColumn
qtechMplsPsProtLspState=_QtechMplsPsProtLspState_Object((1,3,6,1,4,1,27514,1,1,10,2,93,1,3,1,1,13),_QtechMplsPsProtLspState_Type())
qtechMplsPsProtLspState.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechMplsPsProtLspState.setStatus(_B)
class _QtechMplsPsSwitchResult_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2))
_QtechMplsPsSwitchResult_Type.__name__=_C
_QtechMplsPsSwitchResult_Object=MibTableColumn
qtechMplsPsSwitchResult=_QtechMplsPsSwitchResult_Object((1,3,6,1,4,1,27514,1,1,10,2,93,1,3,1,1,14),_QtechMplsPsSwitchResult_Type())
qtechMplsPsSwitchResult.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechMplsPsSwitchResult.setStatus(_B)
_QtechMplsPsRowStatus_Type=RowStatus
_QtechMplsPsRowStatus_Object=MibTableColumn
qtechMplsPsRowStatus=_QtechMplsPsRowStatus_Object((1,3,6,1,4,1,27514,1,1,10,2,93,1,3,1,1,15),_QtechMplsPsRowStatus_Type())
qtechMplsPsRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechMplsPsRowStatus.setStatus(_B)
class _QtechMplsPsTrapOpen_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2))
_QtechMplsPsTrapOpen_Type.__name__=_P
_QtechMplsPsTrapOpen_Object=MibScalar
qtechMplsPsTrapOpen=_QtechMplsPsTrapOpen_Object((1,3,6,1,4,1,27514,1,1,10,2,93,1,3,2),_QtechMplsPsTrapOpen_Type())
qtechMplsPsTrapOpen.setMaxAccess(_V)
if mibBuilder.loadTexts:qtechMplsPsTrapOpen.setStatus(_B)
_QtechMplsPsNotifications_ObjectIdentity=ObjectIdentity
qtechMplsPsNotifications=_QtechMplsPsNotifications_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,93,1,4))
_QtechMplsOamPsConformance_ObjectIdentity=ObjectIdentity
qtechMplsOamPsConformance=_QtechMplsOamPsConformance_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,93,1,5))
_QtechMplsOamPsCompliances_ObjectIdentity=ObjectIdentity
qtechMplsOamPsCompliances=_QtechMplsOamPsCompliances_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,93,1,5,1))
_QtechMplsOamPsGroups_ObjectIdentity=ObjectIdentity
qtechMplsOamPsGroups=_QtechMplsOamPsGroups_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,93,1,5,2))
qtechMplsPsGroup=ObjectGroup((1,3,6,1,4,1,27514,1,1,10,2,93,1,5,2,1))
qtechMplsPsGroup.setObjects(*((_A,_f),(_A,_g),(_A,_Q),(_A,_R),(_A,_S),(_A,_T),(_A,_h),(_A,_i),(_A,_j),(_A,_k),(_A,_l),(_A,_m),(_A,_U),(_A,_n),(_A,_d)))
if mibBuilder.loadTexts:qtechMplsPsGroup.setStatus(_B)
qtechMplsOamIgrLSPOutDefect=NotificationType((1,3,6,1,4,1,27514,1,1,10,2,93,1,2,1))
qtechMplsOamIgrLSPOutDefect.setObjects(*((_A,_J),(_A,_K),(_A,_L),(_A,_M)))
if mibBuilder.loadTexts:qtechMplsOamIgrLSPOutDefect.setStatus(_B)
qtechMplsOamIgrLSPInDefect=NotificationType((1,3,6,1,4,1,27514,1,1,10,2,93,1,2,2))
qtechMplsOamIgrLSPInDefect.setObjects(*((_A,_J),(_A,_K),(_A,_L),(_A,_M)))
if mibBuilder.loadTexts:qtechMplsOamIgrLSPInDefect.setStatus(_B)
qtechMplsOamIgrLSPAva=NotificationType((1,3,6,1,4,1,27514,1,1,10,2,93,1,2,3))
qtechMplsOamIgrLSPAva.setObjects(*((_A,_J),(_A,_K),(_A,_L),(_A,_M)))
if mibBuilder.loadTexts:qtechMplsOamIgrLSPAva.setStatus(_B)
qtechMplsOamIgrLSPUnAva=NotificationType((1,3,6,1,4,1,27514,1,1,10,2,93,1,2,4))
qtechMplsOamIgrLSPUnAva.setObjects(*((_A,_J),(_A,_K),(_A,_L),(_A,_M)))
if mibBuilder.loadTexts:qtechMplsOamIgrLSPUnAva.setStatus(_B)
qtechMplsOamEgrLSPOutDefect=NotificationType((1,3,6,1,4,1,27514,1,1,10,2,93,1,2,5))
qtechMplsOamEgrLSPOutDefect.setObjects(*((_A,_F),(_A,_G),(_A,_H),(_A,_I),(_A,_N),(_A,_O)))
if mibBuilder.loadTexts:qtechMplsOamEgrLSPOutDefect.setStatus(_B)
qtechMplsOamEgrLSPInDefect=NotificationType((1,3,6,1,4,1,27514,1,1,10,2,93,1,2,6))
qtechMplsOamEgrLSPInDefect.setObjects(*((_A,_F),(_A,_G),(_A,_H),(_A,_I),(_A,_N),(_A,_O)))
if mibBuilder.loadTexts:qtechMplsOamEgrLSPInDefect.setStatus(_B)
qtechMplsOamEgrLSPAva=NotificationType((1,3,6,1,4,1,27514,1,1,10,2,93,1,2,7))
qtechMplsOamEgrLSPAva.setObjects(*((_A,_F),(_A,_G),(_A,_H),(_A,_I),(_A,_N),(_A,_O)))
if mibBuilder.loadTexts:qtechMplsOamEgrLSPAva.setStatus(_B)
qtechMplsOamEgrLSPUnAva=NotificationType((1,3,6,1,4,1,27514,1,1,10,2,93,1,2,8))
qtechMplsOamEgrLSPUnAva.setObjects(*((_A,_F),(_A,_G),(_A,_H),(_A,_I),(_A,_N),(_A,_O)))
if mibBuilder.loadTexts:qtechMplsOamEgrLSPUnAva.setStatus(_B)
qtechMplsOamEgrFirstPkt=NotificationType((1,3,6,1,4,1,27514,1,1,10,2,93,1,2,9))
qtechMplsOamEgrFirstPkt.setObjects(*((_A,_F),(_A,_G),(_A,_H),(_A,_I),(_A,_o),(_A,_p)))
if mibBuilder.loadTexts:qtechMplsOamEgrFirstPkt.setStatus(_B)
qtechMplsOamEgrAutoProFDI=NotificationType((1,3,6,1,4,1,27514,1,1,10,2,93,1,2,10))
qtechMplsOamEgrAutoProFDI.setObjects(*((_A,_F),(_A,_G),(_A,_H),(_A,_I),(_A,_q)))
if mibBuilder.loadTexts:qtechMplsOamEgrAutoProFDI.setStatus(_B)
qtechMplsPsSwitchPtoW=NotificationType((1,3,6,1,4,1,27514,1,1,10,2,93,1,4,1))
qtechMplsPsSwitchPtoW.setObjects(*((_A,_Q),(_A,_R),(_A,_S),(_A,_T),(_A,_U)))
if mibBuilder.loadTexts:qtechMplsPsSwitchPtoW.setStatus(_B)
qtechMplsPsSwitchWtoP=NotificationType((1,3,6,1,4,1,27514,1,1,10,2,93,1,4,2))
qtechMplsPsSwitchWtoP.setObjects(*((_A,_Q),(_A,_R),(_A,_S),(_A,_T),(_A,_U)))
if mibBuilder.loadTexts:qtechMplsPsSwitchWtoP.setStatus(_B)
qtechMplsPsNotificationGroup=NotificationGroup((1,3,6,1,4,1,27514,1,1,10,2,93,1,5,2,2))
qtechMplsPsNotificationGroup.setObjects(*((_A,_r),(_A,_s)))
if mibBuilder.loadTexts:qtechMplsPsNotificationGroup.setStatus(_B)
qtechMplsOamPsGroupCompliance=ModuleCompliance((1,3,6,1,4,1,27514,1,1,10,2,93,1,5,1,1))
qtechMplsOamPsGroupCompliance.setObjects((_A,_t))
if mibBuilder.loadTexts:qtechMplsOamPsGroupCompliance.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'qtechMplsOam':qtechMplsOam,'qtechMplsOamPs':qtechMplsOamPs,'qtechMplsOamObjects':qtechMplsOamObjects,'qtechMplsOamCapability':qtechMplsOamCapability,'qtechMplsOamIgrTable':qtechMplsOamIgrTable,'qtechMplsOamIgrEntry':qtechMplsOamIgrEntry,_J:qtechMplsOamIgrIndex,_K:qtechMplsOamIgrLspName,'qtechMplsOamIgrLspId':qtechMplsOamIgrLspId,'qtechMplsOamIgrDetType':qtechMplsOamIgrDetType,'qtechMplsOamIgrDetFreq':qtechMplsOamIgrDetFreq,'qtechMplsOamIgrRevType':qtechMplsOamIgrRevType,'qtechMplsOamIgrRevLspName':qtechMplsOamIgrRevLspName,'qtechMplsOamIgrEnable':qtechMplsOamIgrEnable,'qtechMplsOamIgrValid':qtechMplsOamIgrValid,_L:qtechMplsOamIgrAvaState,_M:qtechMplsOamIgrDefectType,'qtechMplsOamIgrRowStatus':qtechMplsOamIgrRowStatus,'qtechMplsOamEgrTable':qtechMplsOamEgrTable,'qtechMplsOamEgrEntry':qtechMplsOamEgrEntry,_F:qtechMplsOamEgrIndex,_G:qtechMplsOamEgrLspName,_H:qtechMplsOamEgrLsrId,_I:qtechMplsOamEgrLspId,_o:qtechMplsOamEgrDetType,_p:qtechMplsOamEgrDetFreq,'qtechMplsOamEgrRevType':qtechMplsOamEgrRevType,'qtechMplsOamEgrRevLspName':qtechMplsOamEgrRevLspName,'qtechMplsOamEgrAutoEn':qtechMplsOamEgrAutoEn,'qtechMplsOamEgrAutoOvertime':qtechMplsOamEgrAutoOvertime,'qtechMplsOamEgrBDIFreq':qtechMplsOamEgrBDIFreq,_q:qtechMplsOamEgrEnable,'qtechMplsOamEgrValid':qtechMplsOamEgrValid,_N:qtechMplsOamEgrAvaState,_O:qtechMplsOamEgrDefectType,'qtechMplsOamEgrRowStatus':qtechMplsOamEgrRowStatus,'qtechMplsOamTrapOpen':qtechMplsOamTrapOpen,'qtechMplsOamNotifications':qtechMplsOamNotifications,'qtechMplsOamIgrLSPOutDefect':qtechMplsOamIgrLSPOutDefect,'qtechMplsOamIgrLSPInDefect':qtechMplsOamIgrLSPInDefect,'qtechMplsOamIgrLSPAva':qtechMplsOamIgrLSPAva,'qtechMplsOamIgrLSPUnAva':qtechMplsOamIgrLSPUnAva,'qtechMplsOamEgrLSPOutDefect':qtechMplsOamEgrLSPOutDefect,'qtechMplsOamEgrLSPInDefect':qtechMplsOamEgrLSPInDefect,'qtechMplsOamEgrLSPAva':qtechMplsOamEgrLSPAva,'qtechMplsOamEgrLSPUnAva':qtechMplsOamEgrLSPUnAva,'qtechMplsOamEgrFirstPkt':qtechMplsOamEgrFirstPkt,'qtechMplsOamEgrAutoProFDI':qtechMplsOamEgrAutoProFDI,'qtechMplsPsObjects':qtechMplsPsObjects,'qtechMplsPsTable':qtechMplsPsTable,'qtechMplsPsEntry':qtechMplsPsEntry,_d:qtechMplsPsIndex,_f:qtechMplsPsGroupName,_g:qtechMplsPsType,_Q:qtechMplsPsWorkLspName,_R:qtechMplsPsWorkLspId,_S:qtechMplsPsProtectLspName,_T:qtechMplsPsProtectLspId,_h:qtechMplsPsRevertiveMode,_i:qtechMplsPsWTR,_j:qtechMplsPsHoldOff,_k:qtechMplsPsSwitchCondition,_l:qtechMplsPsWorkLspState,_m:qtechMplsPsProtLspState,_U:qtechMplsPsSwitchResult,_n:qtechMplsPsRowStatus,'qtechMplsPsTrapOpen':qtechMplsPsTrapOpen,'qtechMplsPsNotifications':qtechMplsPsNotifications,_r:qtechMplsPsSwitchPtoW,_s:qtechMplsPsSwitchWtoP,'qtechMplsOamPsConformance':qtechMplsOamPsConformance,'qtechMplsOamPsCompliances':qtechMplsOamPsCompliances,'qtechMplsOamPsGroupCompliance':qtechMplsOamPsGroupCompliance,'qtechMplsOamPsGroups':qtechMplsOamPsGroups,_t:qtechMplsPsGroup,'qtechMplsPsNotificationGroup':qtechMplsPsNotificationGroup})