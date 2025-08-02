_d='ntcAupcClntConfGrpV1Standard'
_c='ntcAupcClientMonEstRmtUpFading'
_b='ntcAupcClientMonCurPwrCompen'
_a='ntcAupcClientMonEsNo'
_Z='ntcAupcClientMonInputLvl'
_Y='ntcAupcClientMonState'
_X='ntcAupcClientCalibNomEsNo'
_W='ntcAupcClientCalibNomInputLvl'
_V='ntcAupcClientCfgRemoteTermId'
_U='ntcAupcClientCfgEnable'
_T='ntcAupcClientASCalibViolation'
_S='ntcAupcClientASCalibAbsent'
_R='ntcAupcClientAlmCalibViolation'
_Q='ntcAupcClientAlmCalibAbsent'
_P='ntcAupcClientMonDemodId'
_O='ntcAupcClientCalibDemodId'
_N='ntcAupcClientCfgDemodId'
_M='ntcAupcClientASDemodId'
_L='Unsigned32'
_K='NtcEnable'
_J='dB'
_I='read-write'
_H='not-accessible'
_G='demod3'
_F='demod2'
_E='demod1'
_D='read-only'
_C='Integer32'
_B='NEWTEC-AUPCCLIENT-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ntcFunction,=mibBuilder.importSymbols('NEWTEC-MAIN-MIB','ntcFunction')
NtcAlarmState,NtcEnable=mibBuilder.importSymbols('NEWTEC-TC-MIB','NtcAlarmState',_K)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_L,'iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
ntcAupcClient=ModuleIdentity((1,3,6,1,4,1,5835,5,2,4100))
if mibBuilder.loadTexts:ntcAupcClient.setRevisions(('2014-10-31 08:00','2013-09-18 08:00','2013-05-22 06:00'))
_NtcAupcClientObjects_ObjectIdentity=ObjectIdentity
ntcAupcClientObjects=_NtcAupcClientObjects_ObjectIdentity((1,3,6,1,4,1,5835,5,2,4100,1))
if mibBuilder.loadTexts:ntcAupcClientObjects.setStatus(_A)
_NtcAupcClientAlarm_ObjectIdentity=ObjectIdentity
ntcAupcClientAlarm=_NtcAupcClientAlarm_ObjectIdentity((1,3,6,1,4,1,5835,5,2,4100,1,1))
if mibBuilder.loadTexts:ntcAupcClientAlarm.setStatus(_A)
_NtcAupcClientAlmCalibAbsent_Type=NtcAlarmState
_NtcAupcClientAlmCalibAbsent_Object=MibScalar
ntcAupcClientAlmCalibAbsent=_NtcAupcClientAlmCalibAbsent_Object((1,3,6,1,4,1,5835,5,2,4100,1,1,1),_NtcAupcClientAlmCalibAbsent_Type())
ntcAupcClientAlmCalibAbsent.setMaxAccess(_D)
if mibBuilder.loadTexts:ntcAupcClientAlmCalibAbsent.setStatus(_A)
_NtcAupcClientAlmCalibViolation_Type=NtcAlarmState
_NtcAupcClientAlmCalibViolation_Object=MibScalar
ntcAupcClientAlmCalibViolation=_NtcAupcClientAlmCalibViolation_Object((1,3,6,1,4,1,5835,5,2,4100,1,1,2),_NtcAupcClientAlmCalibViolation_Type())
ntcAupcClientAlmCalibViolation.setMaxAccess(_D)
if mibBuilder.loadTexts:ntcAupcClientAlmCalibViolation.setStatus(_A)
_NtcAupcClientAlarmStateTable_Object=MibTable
ntcAupcClientAlarmStateTable=_NtcAupcClientAlarmStateTable_Object((1,3,6,1,4,1,5835,5,2,4100,1,2))
if mibBuilder.loadTexts:ntcAupcClientAlarmStateTable.setStatus(_A)
_NtcAupcClientAlarmStateEntry_Object=MibTableRow
ntcAupcClientAlarmStateEntry=_NtcAupcClientAlarmStateEntry_Object((1,3,6,1,4,1,5835,5,2,4100,1,2,1))
ntcAupcClientAlarmStateEntry.setIndexNames((0,_B,_M))
if mibBuilder.loadTexts:ntcAupcClientAlarmStateEntry.setStatus(_A)
class _NtcAupcClientASDemodId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_E,1),(_F,2),(_G,3)))
_NtcAupcClientASDemodId_Type.__name__=_C
_NtcAupcClientASDemodId_Object=MibTableColumn
ntcAupcClientASDemodId=_NtcAupcClientASDemodId_Object((1,3,6,1,4,1,5835,5,2,4100,1,2,1,1),_NtcAupcClientASDemodId_Type())
ntcAupcClientASDemodId.setMaxAccess(_H)
if mibBuilder.loadTexts:ntcAupcClientASDemodId.setStatus(_A)
_NtcAupcClientASCalibAbsent_Type=NtcAlarmState
_NtcAupcClientASCalibAbsent_Object=MibTableColumn
ntcAupcClientASCalibAbsent=_NtcAupcClientASCalibAbsent_Object((1,3,6,1,4,1,5835,5,2,4100,1,2,1,2),_NtcAupcClientASCalibAbsent_Type())
ntcAupcClientASCalibAbsent.setMaxAccess(_D)
if mibBuilder.loadTexts:ntcAupcClientASCalibAbsent.setStatus(_A)
_NtcAupcClientASCalibViolation_Type=NtcAlarmState
_NtcAupcClientASCalibViolation_Object=MibTableColumn
ntcAupcClientASCalibViolation=_NtcAupcClientASCalibViolation_Object((1,3,6,1,4,1,5835,5,2,4100,1,2,1,3),_NtcAupcClientASCalibViolation_Type())
ntcAupcClientASCalibViolation.setMaxAccess(_D)
if mibBuilder.loadTexts:ntcAupcClientASCalibViolation.setStatus(_A)
_NtcAupcClientCfgTable_Object=MibTable
ntcAupcClientCfgTable=_NtcAupcClientCfgTable_Object((1,3,6,1,4,1,5835,5,2,4100,1,3))
if mibBuilder.loadTexts:ntcAupcClientCfgTable.setStatus(_A)
_NtcAupcClientCfgEntry_Object=MibTableRow
ntcAupcClientCfgEntry=_NtcAupcClientCfgEntry_Object((1,3,6,1,4,1,5835,5,2,4100,1,3,1))
ntcAupcClientCfgEntry.setIndexNames((0,_B,_N))
if mibBuilder.loadTexts:ntcAupcClientCfgEntry.setStatus(_A)
class _NtcAupcClientCfgDemodId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_E,1),(_F,2),(_G,3)))
_NtcAupcClientCfgDemodId_Type.__name__=_C
_NtcAupcClientCfgDemodId_Object=MibTableColumn
ntcAupcClientCfgDemodId=_NtcAupcClientCfgDemodId_Object((1,3,6,1,4,1,5835,5,2,4100,1,3,1,1),_NtcAupcClientCfgDemodId_Type())
ntcAupcClientCfgDemodId.setMaxAccess(_H)
if mibBuilder.loadTexts:ntcAupcClientCfgDemodId.setStatus(_A)
class _NtcAupcClientCfgEnable_Type(NtcEnable):defaultValue=0
_NtcAupcClientCfgEnable_Type.__name__=_K
_NtcAupcClientCfgEnable_Object=MibTableColumn
ntcAupcClientCfgEnable=_NtcAupcClientCfgEnable_Object((1,3,6,1,4,1,5835,5,2,4100,1,3,1,2),_NtcAupcClientCfgEnable_Type())
ntcAupcClientCfgEnable.setMaxAccess(_I)
if mibBuilder.loadTexts:ntcAupcClientCfgEnable.setStatus(_A)
class _NtcAupcClientCfgRemoteTermId_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65277))
_NtcAupcClientCfgRemoteTermId_Type.__name__=_L
_NtcAupcClientCfgRemoteTermId_Object=MibTableColumn
ntcAupcClientCfgRemoteTermId=_NtcAupcClientCfgRemoteTermId_Object((1,3,6,1,4,1,5835,5,2,4100,1,3,1,3),_NtcAupcClientCfgRemoteTermId_Type())
ntcAupcClientCfgRemoteTermId.setMaxAccess(_I)
if mibBuilder.loadTexts:ntcAupcClientCfgRemoteTermId.setStatus(_A)
_NtcAupcClientCalibTable_Object=MibTable
ntcAupcClientCalibTable=_NtcAupcClientCalibTable_Object((1,3,6,1,4,1,5835,5,2,4100,1,4))
if mibBuilder.loadTexts:ntcAupcClientCalibTable.setStatus(_A)
_NtcAupcClientCalibEntry_Object=MibTableRow
ntcAupcClientCalibEntry=_NtcAupcClientCalibEntry_Object((1,3,6,1,4,1,5835,5,2,4100,1,4,1))
ntcAupcClientCalibEntry.setIndexNames((0,_B,_O))
if mibBuilder.loadTexts:ntcAupcClientCalibEntry.setStatus(_A)
class _NtcAupcClientCalibDemodId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_E,1),(_F,2),(_G,3)))
_NtcAupcClientCalibDemodId_Type.__name__=_C
_NtcAupcClientCalibDemodId_Object=MibTableColumn
ntcAupcClientCalibDemodId=_NtcAupcClientCalibDemodId_Object((1,3,6,1,4,1,5835,5,2,4100,1,4,1,1),_NtcAupcClientCalibDemodId_Type())
ntcAupcClientCalibDemodId.setMaxAccess(_H)
if mibBuilder.loadTexts:ntcAupcClientCalibDemodId.setStatus(_A)
class _NtcAupcClientCalibNomInputLvl_Type(Integer32):defaultValue=-150;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1000,500))
_NtcAupcClientCalibNomInputLvl_Type.__name__=_C
_NtcAupcClientCalibNomInputLvl_Object=MibTableColumn
ntcAupcClientCalibNomInputLvl=_NtcAupcClientCalibNomInputLvl_Object((1,3,6,1,4,1,5835,5,2,4100,1,4,1,2),_NtcAupcClientCalibNomInputLvl_Type())
ntcAupcClientCalibNomInputLvl.setMaxAccess(_I)
if mibBuilder.loadTexts:ntcAupcClientCalibNomInputLvl.setStatus(_A)
if mibBuilder.loadTexts:ntcAupcClientCalibNomInputLvl.setUnits('dBm')
class _NtcAupcClientCalibNomEsNo_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1000,4000))
_NtcAupcClientCalibNomEsNo_Type.__name__=_C
_NtcAupcClientCalibNomEsNo_Object=MibTableColumn
ntcAupcClientCalibNomEsNo=_NtcAupcClientCalibNomEsNo_Object((1,3,6,1,4,1,5835,5,2,4100,1,4,1,3),_NtcAupcClientCalibNomEsNo_Type())
ntcAupcClientCalibNomEsNo.setMaxAccess(_I)
if mibBuilder.loadTexts:ntcAupcClientCalibNomEsNo.setStatus(_A)
if mibBuilder.loadTexts:ntcAupcClientCalibNomEsNo.setUnits(_J)
_NtcAupcClientMonTable_Object=MibTable
ntcAupcClientMonTable=_NtcAupcClientMonTable_Object((1,3,6,1,4,1,5835,5,2,4100,1,5))
if mibBuilder.loadTexts:ntcAupcClientMonTable.setStatus(_A)
_NtcAupcClientMonEntry_Object=MibTableRow
ntcAupcClientMonEntry=_NtcAupcClientMonEntry_Object((1,3,6,1,4,1,5835,5,2,4100,1,5,1))
ntcAupcClientMonEntry.setIndexNames((0,_B,_P))
if mibBuilder.loadTexts:ntcAupcClientMonEntry.setStatus(_A)
class _NtcAupcClientMonDemodId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_E,1),(_F,2),(_G,3)))
_NtcAupcClientMonDemodId_Type.__name__=_C
_NtcAupcClientMonDemodId_Object=MibTableColumn
ntcAupcClientMonDemodId=_NtcAupcClientMonDemodId_Object((1,3,6,1,4,1,5835,5,2,4100,1,5,1,1),_NtcAupcClientMonDemodId_Type())
ntcAupcClientMonDemodId.setMaxAccess(_H)
if mibBuilder.loadTexts:ntcAupcClientMonDemodId.setStatus(_A)
class _NtcAupcClientMonState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6)));namedValues=NamedValues(*(('off',0),('notCalibrated',1),('calibrated',2),('waitingForController',3),('reporting',4),('nolock',5),('alarm',6)))
_NtcAupcClientMonState_Type.__name__=_C
_NtcAupcClientMonState_Object=MibTableColumn
ntcAupcClientMonState=_NtcAupcClientMonState_Object((1,3,6,1,4,1,5835,5,2,4100,1,5,1,2),_NtcAupcClientMonState_Type())
ntcAupcClientMonState.setMaxAccess(_D)
if mibBuilder.loadTexts:ntcAupcClientMonState.setStatus(_A)
class _NtcAupcClientMonInputLvl_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1000,500))
_NtcAupcClientMonInputLvl_Type.__name__=_C
_NtcAupcClientMonInputLvl_Object=MibTableColumn
ntcAupcClientMonInputLvl=_NtcAupcClientMonInputLvl_Object((1,3,6,1,4,1,5835,5,2,4100,1,5,1,3),_NtcAupcClientMonInputLvl_Type())
ntcAupcClientMonInputLvl.setMaxAccess(_D)
if mibBuilder.loadTexts:ntcAupcClientMonInputLvl.setStatus(_A)
if mibBuilder.loadTexts:ntcAupcClientMonInputLvl.setUnits('dBm')
class _NtcAupcClientMonEsNo_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1000,4000))
_NtcAupcClientMonEsNo_Type.__name__=_C
_NtcAupcClientMonEsNo_Object=MibTableColumn
ntcAupcClientMonEsNo=_NtcAupcClientMonEsNo_Object((1,3,6,1,4,1,5835,5,2,4100,1,5,1,4),_NtcAupcClientMonEsNo_Type())
ntcAupcClientMonEsNo.setMaxAccess(_D)
if mibBuilder.loadTexts:ntcAupcClientMonEsNo.setStatus(_A)
if mibBuilder.loadTexts:ntcAupcClientMonEsNo.setUnits(_J)
class _NtcAupcClientMonCurPwrCompen_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1000,5000))
_NtcAupcClientMonCurPwrCompen_Type.__name__=_C
_NtcAupcClientMonCurPwrCompen_Object=MibTableColumn
ntcAupcClientMonCurPwrCompen=_NtcAupcClientMonCurPwrCompen_Object((1,3,6,1,4,1,5835,5,2,4100,1,5,1,5),_NtcAupcClientMonCurPwrCompen_Type())
ntcAupcClientMonCurPwrCompen.setMaxAccess(_D)
if mibBuilder.loadTexts:ntcAupcClientMonCurPwrCompen.setStatus(_A)
if mibBuilder.loadTexts:ntcAupcClientMonCurPwrCompen.setUnits(_J)
class _NtcAupcClientMonEstRmtUpFading_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1000,5000))
_NtcAupcClientMonEstRmtUpFading_Type.__name__=_C
_NtcAupcClientMonEstRmtUpFading_Object=MibTableColumn
ntcAupcClientMonEstRmtUpFading=_NtcAupcClientMonEstRmtUpFading_Object((1,3,6,1,4,1,5835,5,2,4100,1,5,1,6),_NtcAupcClientMonEstRmtUpFading_Type())
ntcAupcClientMonEstRmtUpFading.setMaxAccess(_D)
if mibBuilder.loadTexts:ntcAupcClientMonEstRmtUpFading.setStatus(_A)
if mibBuilder.loadTexts:ntcAupcClientMonEstRmtUpFading.setUnits(_J)
_NtcAupcClntConformance_ObjectIdentity=ObjectIdentity
ntcAupcClntConformance=_NtcAupcClntConformance_ObjectIdentity((1,3,6,1,4,1,5835,5,2,4100,2))
if mibBuilder.loadTexts:ntcAupcClntConformance.setStatus(_A)
_NtcAupcClntConfCompliance_ObjectIdentity=ObjectIdentity
ntcAupcClntConfCompliance=_NtcAupcClntConfCompliance_ObjectIdentity((1,3,6,1,4,1,5835,5,2,4100,2,1))
if mibBuilder.loadTexts:ntcAupcClntConfCompliance.setStatus(_A)
_NtcAupcClntConfGroup_ObjectIdentity=ObjectIdentity
ntcAupcClntConfGroup=_NtcAupcClntConfGroup_ObjectIdentity((1,3,6,1,4,1,5835,5,2,4100,2,2))
if mibBuilder.loadTexts:ntcAupcClntConfGroup.setStatus(_A)
ntcAupcClntConfGrpV1Standard=ObjectGroup((1,3,6,1,4,1,5835,5,2,4100,2,2,1))
ntcAupcClntConfGrpV1Standard.setObjects(*((_B,_Q),(_B,_R),(_B,_S),(_B,_T),(_B,_U),(_B,_V),(_B,_W),(_B,_X),(_B,_Y),(_B,_Z),(_B,_a),(_B,_b),(_B,_c)))
if mibBuilder.loadTexts:ntcAupcClntConfGrpV1Standard.setStatus(_A)
ntcAupcClntConfCompV1Standard=ModuleCompliance((1,3,6,1,4,1,5835,5,2,4100,2,1,1))
ntcAupcClntConfCompV1Standard.setObjects((_B,_d))
if mibBuilder.loadTexts:ntcAupcClntConfCompV1Standard.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'ntcAupcClient':ntcAupcClient,'ntcAupcClientObjects':ntcAupcClientObjects,'ntcAupcClientAlarm':ntcAupcClientAlarm,_Q:ntcAupcClientAlmCalibAbsent,_R:ntcAupcClientAlmCalibViolation,'ntcAupcClientAlarmStateTable':ntcAupcClientAlarmStateTable,'ntcAupcClientAlarmStateEntry':ntcAupcClientAlarmStateEntry,_M:ntcAupcClientASDemodId,_S:ntcAupcClientASCalibAbsent,_T:ntcAupcClientASCalibViolation,'ntcAupcClientCfgTable':ntcAupcClientCfgTable,'ntcAupcClientCfgEntry':ntcAupcClientCfgEntry,_N:ntcAupcClientCfgDemodId,_U:ntcAupcClientCfgEnable,_V:ntcAupcClientCfgRemoteTermId,'ntcAupcClientCalibTable':ntcAupcClientCalibTable,'ntcAupcClientCalibEntry':ntcAupcClientCalibEntry,_O:ntcAupcClientCalibDemodId,_W:ntcAupcClientCalibNomInputLvl,_X:ntcAupcClientCalibNomEsNo,'ntcAupcClientMonTable':ntcAupcClientMonTable,'ntcAupcClientMonEntry':ntcAupcClientMonEntry,_P:ntcAupcClientMonDemodId,_Y:ntcAupcClientMonState,_Z:ntcAupcClientMonInputLvl,_a:ntcAupcClientMonEsNo,_b:ntcAupcClientMonCurPwrCompen,_c:ntcAupcClientMonEstRmtUpFading,'ntcAupcClntConformance':ntcAupcClntConformance,'ntcAupcClntConfCompliance':ntcAupcClntConfCompliance,'ntcAupcClntConfCompV1Standard':ntcAupcClntConfCompV1Standard,'ntcAupcClntConfGroup':ntcAupcClntConfGroup,_d:ntcAupcClntConfGrpV1Standard})