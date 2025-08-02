_T='ttdbOpVehListGroup'
_S='ttdbBasicGroup'
_R='ttdbOpVehOrient'
_Q='ttdbOpVehLeadDir'
_P='ttdbOpVehIsLead'
_O='ttdbOpVehNo'
_N='ttdbOpVehId'
_M='ttdbOpTrnTopoCnt'
_L='ttdbOpVehCnt'
_K='ttdbTrainId'
_J='ttdbConfirmationState'
_I='ttdbValidityState'
_H='ttdbEtbId'
_G='ttdbOpVehIdx'
_F='Integer32'
_E='OctetString'
_D='Unsigned32'
_C='read-only'
_B='TTDB-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_E,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_F,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_D,'iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
iec61375p2=ModuleIdentity((1,0,61375,2))
if mibBuilder.loadTexts:iec61375p2.setRevisions(('2019-11-27 00:00','2014-05-22 00:00'))
class TtdbOrient(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('direct',1),('inverse',2),('undefined',3)))
class TtdbValidity(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('invalid',1),('valid',2),('shared',3)))
class TtdbConfirmation(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('unconfirmed',1),('confirmed',2)))
_Std_ObjectIdentity=ObjectIdentity
std=_Std_ObjectIdentity((1,0))
_Stdx61375_ObjectIdentity=ObjectIdentity
stdx61375=_Stdx61375_ObjectIdentity((1,0,61375))
_Ttdb_ObjectIdentity=ObjectIdentity
ttdb=_Ttdb_ObjectIdentity((1,0,61375,2,3))
_TtdbObjects_ObjectIdentity=ObjectIdentity
ttdbObjects=_TtdbObjects_ObjectIdentity((1,0,61375,2,3,1))
_TtdbGenInfo_ObjectIdentity=ObjectIdentity
ttdbGenInfo=_TtdbGenInfo_ObjectIdentity((1,0,61375,2,3,1,1))
class _TtdbEtbId_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4))
_TtdbEtbId_Type.__name__=_D
_TtdbEtbId_Object=MibScalar
ttdbEtbId=_TtdbEtbId_Object((1,0,61375,2,3,1,1,1),_TtdbEtbId_Type())
ttdbEtbId.setMaxAccess(_C)
if mibBuilder.loadTexts:ttdbEtbId.setStatus(_A)
_TtdbValidityState_Type=TtdbValidity
_TtdbValidityState_Object=MibScalar
ttdbValidityState=_TtdbValidityState_Object((1,0,61375,2,3,1,1,2),_TtdbValidityState_Type())
ttdbValidityState.setMaxAccess(_C)
if mibBuilder.loadTexts:ttdbValidityState.setStatus(_A)
_TtdbConfirmationState_Type=TtdbConfirmation
_TtdbConfirmationState_Object=MibScalar
ttdbConfirmationState=_TtdbConfirmationState_Object((1,0,61375,2,3,1,1,3),_TtdbConfirmationState_Type())
ttdbConfirmationState.setMaxAccess(_C)
if mibBuilder.loadTexts:ttdbConfirmationState.setStatus(_A)
class _TtdbTrainId_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(16,16));fixedLength=16
_TtdbTrainId_Type.__name__=_E
_TtdbTrainId_Object=MibScalar
ttdbTrainId=_TtdbTrainId_Object((1,0,61375,2,3,1,1,4),_TtdbTrainId_Type())
ttdbTrainId.setMaxAccess(_C)
if mibBuilder.loadTexts:ttdbTrainId.setStatus(_A)
_TtdbOpTrnTopoCnt_Type=Unsigned32
_TtdbOpTrnTopoCnt_Object=MibScalar
ttdbOpTrnTopoCnt=_TtdbOpTrnTopoCnt_Object((1,0,61375,2,3,1,1,5),_TtdbOpTrnTopoCnt_Type())
ttdbOpTrnTopoCnt.setMaxAccess(_C)
if mibBuilder.loadTexts:ttdbOpTrnTopoCnt.setStatus(_A)
_TtdbOpVehList_ObjectIdentity=ObjectIdentity
ttdbOpVehList=_TtdbOpVehList_ObjectIdentity((1,0,61375,2,3,1,2))
class _TtdbOpVehCnt_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,63))
_TtdbOpVehCnt_Type.__name__=_D
_TtdbOpVehCnt_Object=MibScalar
ttdbOpVehCnt=_TtdbOpVehCnt_Object((1,0,61375,2,3,1,2,1),_TtdbOpVehCnt_Type())
ttdbOpVehCnt.setMaxAccess(_C)
if mibBuilder.loadTexts:ttdbOpVehCnt.setStatus(_A)
_TtdbOpVehTable_Object=MibTable
ttdbOpVehTable=_TtdbOpVehTable_Object((1,0,61375,2,3,1,2,2))
if mibBuilder.loadTexts:ttdbOpVehTable.setStatus(_A)
_TtdbOpVehEntry_Object=MibTableRow
ttdbOpVehEntry=_TtdbOpVehEntry_Object((1,0,61375,2,3,1,2,2,1))
ttdbOpVehEntry.setIndexNames((0,_B,_G))
if mibBuilder.loadTexts:ttdbOpVehEntry.setStatus(_A)
class _TtdbOpVehIdx_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,63))
_TtdbOpVehIdx_Type.__name__=_D
_TtdbOpVehIdx_Object=MibTableColumn
ttdbOpVehIdx=_TtdbOpVehIdx_Object((1,0,61375,2,3,1,2,2,1,1),_TtdbOpVehIdx_Type())
ttdbOpVehIdx.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:ttdbOpVehIdx.setStatus(_A)
class _TtdbOpVehId_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_TtdbOpVehId_Type.__name__=_E
_TtdbOpVehId_Object=MibTableColumn
ttdbOpVehId=_TtdbOpVehId_Object((1,0,61375,2,3,1,2,2,1,2),_TtdbOpVehId_Type())
ttdbOpVehId.setMaxAccess(_C)
if mibBuilder.loadTexts:ttdbOpVehId.setStatus(_A)
class _TtdbOpVehNo_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,63))
_TtdbOpVehNo_Type.__name__=_D
_TtdbOpVehNo_Object=MibTableColumn
ttdbOpVehNo=_TtdbOpVehNo_Object((1,0,61375,2,3,1,2,2,1,3),_TtdbOpVehNo_Type())
ttdbOpVehNo.setMaxAccess(_C)
if mibBuilder.loadTexts:ttdbOpVehNo.setStatus(_A)
class _TtdbOpVehIsLead_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('notLeading',1),('leading',2)))
_TtdbOpVehIsLead_Type.__name__=_F
_TtdbOpVehIsLead_Object=MibTableColumn
ttdbOpVehIsLead=_TtdbOpVehIsLead_Object((1,0,61375,2,3,1,2,2,1,4),_TtdbOpVehIsLead_Type())
ttdbOpVehIsLead.setMaxAccess(_C)
if mibBuilder.loadTexts:ttdbOpVehIsLead.setStatus(_A)
class _TtdbOpVehLeadDir_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('dir1',1),('dir2',2)))
_TtdbOpVehLeadDir_Type.__name__=_F
_TtdbOpVehLeadDir_Object=MibTableColumn
ttdbOpVehLeadDir=_TtdbOpVehLeadDir_Object((1,0,61375,2,3,1,2,2,1,5),_TtdbOpVehLeadDir_Type())
ttdbOpVehLeadDir.setMaxAccess(_C)
if mibBuilder.loadTexts:ttdbOpVehLeadDir.setStatus(_A)
_TtdbOpVehOrient_Type=TtdbOrient
_TtdbOpVehOrient_Object=MibTableColumn
ttdbOpVehOrient=_TtdbOpVehOrient_Object((1,0,61375,2,3,1,2,2,1,6),_TtdbOpVehOrient_Type())
ttdbOpVehOrient.setMaxAccess(_C)
if mibBuilder.loadTexts:ttdbOpVehOrient.setStatus(_A)
_TtdbConformance_ObjectIdentity=ObjectIdentity
ttdbConformance=_TtdbConformance_ObjectIdentity((1,0,61375,2,3,2))
ttdbBasicGroup=ObjectGroup((1,0,61375,2,3,2,2))
ttdbBasicGroup.setObjects(*((_B,_H),(_B,_I),(_B,_J),(_B,_K),(_B,_L),(_B,_M)))
if mibBuilder.loadTexts:ttdbBasicGroup.setStatus(_A)
ttdbOpVehListGroup=ObjectGroup((1,0,61375,2,3,2,3))
ttdbOpVehListGroup.setObjects(*((_B,_N),(_B,_O),(_B,_P),(_B,_Q),(_B,_R)))
if mibBuilder.loadTexts:ttdbOpVehListGroup.setStatus(_A)
ttdbBasicCompliance=ModuleCompliance((1,0,61375,2,3,2,4))
ttdbBasicCompliance.setObjects(*((_B,_S),(_B,_T)))
if mibBuilder.loadTexts:ttdbBasicCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'TtdbOrient':TtdbOrient,'TtdbValidity':TtdbValidity,'TtdbConfirmation':TtdbConfirmation,'std':std,'stdx61375':stdx61375,'iec61375p2':iec61375p2,'ttdb':ttdb,'ttdbObjects':ttdbObjects,'ttdbGenInfo':ttdbGenInfo,_H:ttdbEtbId,_I:ttdbValidityState,_J:ttdbConfirmationState,_K:ttdbTrainId,_M:ttdbOpTrnTopoCnt,'ttdbOpVehList':ttdbOpVehList,_L:ttdbOpVehCnt,'ttdbOpVehTable':ttdbOpVehTable,'ttdbOpVehEntry':ttdbOpVehEntry,_G:ttdbOpVehIdx,_N:ttdbOpVehId,_O:ttdbOpVehNo,_P:ttdbOpVehIsLead,_Q:ttdbOpVehLeadDir,_R:ttdbOpVehOrient,'ttdbConformance':ttdbConformance,_S:ttdbBasicGroup,_T:ttdbOpVehListGroup,'ttdbBasicCompliance':ttdbBasicCompliance})