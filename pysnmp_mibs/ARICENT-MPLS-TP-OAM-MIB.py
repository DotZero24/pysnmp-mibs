_V='fsMplsTpOamMegSubOperStatus'
_U='fsMplsTpOamMegOperStatus'
_T='fsMplsTpMeName'
_S='fsMplsTpMegName'
_R='fsMplsTpOamContextName'
_Q='fsMplsTpMeMpIndex'
_P='fsMplsTpMeIndex'
_O='read-write'
_N='TruthValue'
_M='RowPointer'
_L='InterfaceIndexOrZero'
_K='accessible-for-notify'
_J='not-accessible'
_I='fsMplsTpMegIndex'
_H='fsMplsTpContextId'
_G='ARICENT-MPLS-TP-MIB'
_F='Unsigned32'
_E='DisplayString'
_D='Integer32'
_C='ARICENT-MPLS-TP-OAM-MIB'
_B='read-create'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
fsMplsTpContextId,=mibBuilder.importSymbols(_G,_H)
InterfaceIndexOrZero,=mibBuilder.importSymbols('IF-MIB',_L)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso,zeroDotZero=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_F,'enterprises','iso','zeroDotZero')
DisplayString,PhysAddress,RowPointer,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC',_E,'PhysAddress',_M,'RowStatus','TextualConvention',_N)
fsMplsTpOamMIB=ModuleIdentity((1,3,6,1,4,1,2076,13,9))
if mibBuilder.loadTexts:fsMplsTpOamMIB.setRevisions(('2012-09-05 00:00',))
_FsMplsTpOamNotifications_ObjectIdentity=ObjectIdentity
fsMplsTpOamNotifications=_FsMplsTpOamNotifications_ObjectIdentity((1,3,6,1,4,1,2076,13,9,0))
_FsMplsTpOamObjects_ObjectIdentity=ObjectIdentity
fsMplsTpOamObjects=_FsMplsTpOamObjects_ObjectIdentity((1,3,6,1,4,1,2076,13,9,1))
_FsMplsTpOamScalarObjects_ObjectIdentity=ObjectIdentity
fsMplsTpOamScalarObjects=_FsMplsTpOamScalarObjects_ObjectIdentity((1,3,6,1,4,1,2076,13,9,1,1))
_FsMplsTpMegTable_Object=MibTable
fsMplsTpMegTable=_FsMplsTpMegTable_Object((1,3,6,1,4,1,2076,13,9,1,2))
if mibBuilder.loadTexts:fsMplsTpMegTable.setStatus(_A)
_FsMplsTpMegEntry_Object=MibTableRow
fsMplsTpMegEntry=_FsMplsTpMegEntry_Object((1,3,6,1,4,1,2076,13,9,1,2,1))
fsMplsTpMegEntry.setIndexNames((0,_G,_H),(0,_C,_I))
if mibBuilder.loadTexts:fsMplsTpMegEntry.setStatus(_A)
_FsMplsTpMegIndex_Type=Unsigned32
_FsMplsTpMegIndex_Object=MibTableColumn
fsMplsTpMegIndex=_FsMplsTpMegIndex_Object((1,3,6,1,4,1,2076,13,9,1,2,1,1),_FsMplsTpMegIndex_Type())
fsMplsTpMegIndex.setMaxAccess(_J)
if mibBuilder.loadTexts:fsMplsTpMegIndex.setStatus(_A)
class _FsMplsTpMegName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,48))
_FsMplsTpMegName_Type.__name__=_E
_FsMplsTpMegName_Object=MibTableColumn
fsMplsTpMegName=_FsMplsTpMegName_Object((1,3,6,1,4,1,2076,13,9,1,2,1,2),_FsMplsTpMegName_Type())
fsMplsTpMegName.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMplsTpMegName.setStatus(_A)
class _FsMplsTpMegOperatorType_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('ipCompatible',1),('iccBased',2)))
_FsMplsTpMegOperatorType_Type.__name__=_D
_FsMplsTpMegOperatorType_Object=MibTableColumn
fsMplsTpMegOperatorType=_FsMplsTpMegOperatorType_Object((1,3,6,1,4,1,2076,13,9,1,2,1,3),_FsMplsTpMegOperatorType_Type())
fsMplsTpMegOperatorType.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMplsTpMegOperatorType.setStatus(_A)
class _FsMplsTpMegIdIcc_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,6))
_FsMplsTpMegIdIcc_Type.__name__=_E
_FsMplsTpMegIdIcc_Object=MibTableColumn
fsMplsTpMegIdIcc=_FsMplsTpMegIdIcc_Object((1,3,6,1,4,1,2076,13,9,1,2,1,4),_FsMplsTpMegIdIcc_Type())
fsMplsTpMegIdIcc.setMaxAccess(_O)
if mibBuilder.loadTexts:fsMplsTpMegIdIcc.setStatus(_A)
class _FsMplsTpMegIdUmc_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,7))
_FsMplsTpMegIdUmc_Type.__name__=_E
_FsMplsTpMegIdUmc_Object=MibTableColumn
fsMplsTpMegIdUmc=_FsMplsTpMegIdUmc_Object((1,3,6,1,4,1,2076,13,9,1,2,1,5),_FsMplsTpMegIdUmc_Type())
fsMplsTpMegIdUmc.setMaxAccess(_O)
if mibBuilder.loadTexts:fsMplsTpMegIdUmc.setStatus(_A)
class _FsMplsTpMegServiceType_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('lsp',1),('pseudowire',2),('section',3)))
_FsMplsTpMegServiceType_Type.__name__=_D
_FsMplsTpMegServiceType_Object=MibTableColumn
fsMplsTpMegServiceType=_FsMplsTpMegServiceType_Object((1,3,6,1,4,1,2076,13,9,1,2,1,6),_FsMplsTpMegServiceType_Type())
fsMplsTpMegServiceType.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMplsTpMegServiceType.setStatus(_A)
class _FsMplsTpMegMpLocation_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('perNode',1),('perInterface',2)))
_FsMplsTpMegMpLocation_Type.__name__=_D
_FsMplsTpMegMpLocation_Object=MibTableColumn
fsMplsTpMegMpLocation=_FsMplsTpMegMpLocation_Object((1,3,6,1,4,1,2076,13,9,1,2,1,7),_FsMplsTpMegMpLocation_Type())
fsMplsTpMegMpLocation.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMplsTpMegMpLocation.setStatus(_A)
_FsMplsTpMegRowStatus_Type=RowStatus
_FsMplsTpMegRowStatus_Object=MibTableColumn
fsMplsTpMegRowStatus=_FsMplsTpMegRowStatus_Object((1,3,6,1,4,1,2076,13,9,1,2,1,8),_FsMplsTpMegRowStatus_Type())
fsMplsTpMegRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMplsTpMegRowStatus.setStatus(_A)
_FsMplsTpMeTable_Object=MibTable
fsMplsTpMeTable=_FsMplsTpMeTable_Object((1,3,6,1,4,1,2076,13,9,1,3))
if mibBuilder.loadTexts:fsMplsTpMeTable.setStatus(_A)
_FsMplsTpMeEntry_Object=MibTableRow
fsMplsTpMeEntry=_FsMplsTpMeEntry_Object((1,3,6,1,4,1,2076,13,9,1,3,1))
fsMplsTpMeEntry.setIndexNames((0,_G,_H),(0,_C,_I),(0,_C,_P),(0,_C,_Q))
if mibBuilder.loadTexts:fsMplsTpMeEntry.setStatus(_A)
_FsMplsTpMeIndex_Type=Unsigned32
_FsMplsTpMeIndex_Object=MibTableColumn
fsMplsTpMeIndex=_FsMplsTpMeIndex_Object((1,3,6,1,4,1,2076,13,9,1,3,1,1),_FsMplsTpMeIndex_Type())
fsMplsTpMeIndex.setMaxAccess(_J)
if mibBuilder.loadTexts:fsMplsTpMeIndex.setStatus(_A)
_FsMplsTpMeMpIndex_Type=Unsigned32
_FsMplsTpMeMpIndex_Object=MibTableColumn
fsMplsTpMeMpIndex=_FsMplsTpMeMpIndex_Object((1,3,6,1,4,1,2076,13,9,1,3,1,2),_FsMplsTpMeMpIndex_Type())
fsMplsTpMeMpIndex.setMaxAccess(_J)
if mibBuilder.loadTexts:fsMplsTpMeMpIndex.setStatus(_A)
class _FsMplsTpMeName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,48))
_FsMplsTpMeName_Type.__name__=_E
_FsMplsTpMeName_Object=MibTableColumn
fsMplsTpMeName=_FsMplsTpMeName_Object((1,3,6,1,4,1,2076,13,9,1,3,1,3),_FsMplsTpMeName_Type())
fsMplsTpMeName.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMplsTpMeName.setStatus(_A)
class _FsMplsTpMeMpIfIndex_Type(InterfaceIndexOrZero):defaultValue=0
_FsMplsTpMeMpIfIndex_Type.__name__=_L
_FsMplsTpMeMpIfIndex_Object=MibTableColumn
fsMplsTpMeMpIfIndex=_FsMplsTpMeMpIfIndex_Object((1,3,6,1,4,1,2076,13,9,1,3,1,4),_FsMplsTpMeMpIfIndex_Type())
fsMplsTpMeMpIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMplsTpMeMpIfIndex.setStatus(_A)
class _FsMplsTpMeSourceMepIndex_Type(Unsigned32):defaultValue=0
_FsMplsTpMeSourceMepIndex_Type.__name__=_F
_FsMplsTpMeSourceMepIndex_Object=MibTableColumn
fsMplsTpMeSourceMepIndex=_FsMplsTpMeSourceMepIndex_Object((1,3,6,1,4,1,2076,13,9,1,3,1,5),_FsMplsTpMeSourceMepIndex_Type())
fsMplsTpMeSourceMepIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMplsTpMeSourceMepIndex.setStatus(_A)
class _FsMplsTpMeSinkMepIndex_Type(Unsigned32):defaultValue=0
_FsMplsTpMeSinkMepIndex_Type.__name__=_F
_FsMplsTpMeSinkMepIndex_Object=MibTableColumn
fsMplsTpMeSinkMepIndex=_FsMplsTpMeSinkMepIndex_Object((1,3,6,1,4,1,2076,13,9,1,3,1,6),_FsMplsTpMeSinkMepIndex_Type())
fsMplsTpMeSinkMepIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMplsTpMeSinkMepIndex.setStatus(_A)
class _FsMplsTpMeMpType_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('mep',1),('mip',2)))
_FsMplsTpMeMpType_Type.__name__=_D
_FsMplsTpMeMpType_Object=MibTableColumn
fsMplsTpMeMpType=_FsMplsTpMeMpType_Object((1,3,6,1,4,1,2076,13,9,1,3,1,7),_FsMplsTpMeMpType_Type())
fsMplsTpMeMpType.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMplsTpMeMpType.setStatus(_A)
class _FsMplsTpMeMepDirection_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('up',1),('down',2)))
_FsMplsTpMeMepDirection_Type.__name__=_D
_FsMplsTpMeMepDirection_Object=MibTableColumn
fsMplsTpMeMepDirection=_FsMplsTpMeMepDirection_Object((1,3,6,1,4,1,2076,13,9,1,3,1,8),_FsMplsTpMeMepDirection_Type())
fsMplsTpMeMepDirection.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMplsTpMeMepDirection.setStatus(_A)
class _FsMplsTpMeProactiveOamSessIndex_Type(Unsigned32):defaultValue=0
_FsMplsTpMeProactiveOamSessIndex_Type.__name__=_F
_FsMplsTpMeProactiveOamSessIndex_Object=MibTableColumn
fsMplsTpMeProactiveOamSessIndex=_FsMplsTpMeProactiveOamSessIndex_Object((1,3,6,1,4,1,2076,13,9,1,3,1,9),_FsMplsTpMeProactiveOamSessIndex_Type())
fsMplsTpMeProactiveOamSessIndex.setMaxAccess('read-only')
if mibBuilder.loadTexts:fsMplsTpMeProactiveOamSessIndex.setStatus(_A)
class _FsMplsTpMeProactiveOamPhbTCValue_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*(('ef1',1),('ef2',2),('af1',3),('af2',4),('af3',5),('be',6)))
_FsMplsTpMeProactiveOamPhbTCValue_Type.__name__=_D
_FsMplsTpMeProactiveOamPhbTCValue_Object=MibTableColumn
fsMplsTpMeProactiveOamPhbTCValue=_FsMplsTpMeProactiveOamPhbTCValue_Object((1,3,6,1,4,1,2076,13,9,1,3,1,10),_FsMplsTpMeProactiveOamPhbTCValue_Type())
fsMplsTpMeProactiveOamPhbTCValue.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMplsTpMeProactiveOamPhbTCValue.setStatus(_A)
class _FsMplsTpMeOnDemandOamPhbTCValue_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*(('ef1',1),('ef2',2),('af1',3),('af2',4),('af3',5),('be',6)))
_FsMplsTpMeOnDemandOamPhbTCValue_Type.__name__=_D
_FsMplsTpMeOnDemandOamPhbTCValue_Object=MibTableColumn
fsMplsTpMeOnDemandOamPhbTCValue=_FsMplsTpMeOnDemandOamPhbTCValue_Object((1,3,6,1,4,1,2076,13,9,1,3,1,11),_FsMplsTpMeOnDemandOamPhbTCValue_Type())
fsMplsTpMeOnDemandOamPhbTCValue.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMplsTpMeOnDemandOamPhbTCValue.setStatus(_A)
class _FsMplsTpMeServiceSignaled_Type(TruthValue):defaultValue=2
_FsMplsTpMeServiceSignaled_Type.__name__=_N
_FsMplsTpMeServiceSignaled_Object=MibTableColumn
fsMplsTpMeServiceSignaled=_FsMplsTpMeServiceSignaled_Object((1,3,6,1,4,1,2076,13,9,1,3,1,12),_FsMplsTpMeServiceSignaled_Type())
fsMplsTpMeServiceSignaled.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMplsTpMeServiceSignaled.setStatus(_A)
class _FsMplsTpMeServicePointer_Type(RowPointer):defaultValue=0,0
_FsMplsTpMeServicePointer_Type.__name__=_M
_FsMplsTpMeServicePointer_Object=MibTableColumn
fsMplsTpMeServicePointer=_FsMplsTpMeServicePointer_Object((1,3,6,1,4,1,2076,13,9,1,3,1,13),_FsMplsTpMeServicePointer_Type())
fsMplsTpMeServicePointer.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMplsTpMeServicePointer.setStatus(_A)
_FsMplsTpMeRowStatus_Type=RowStatus
_FsMplsTpMeRowStatus_Object=MibTableColumn
fsMplsTpMeRowStatus=_FsMplsTpMeRowStatus_Object((1,3,6,1,4,1,2076,13,9,1,3,1,14),_FsMplsTpMeRowStatus_Type())
fsMplsTpMeRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMplsTpMeRowStatus.setStatus(_A)
class _FsMplsTpOamContextName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_FsMplsTpOamContextName_Type.__name__=_E
_FsMplsTpOamContextName_Object=MibScalar
fsMplsTpOamContextName=_FsMplsTpOamContextName_Object((1,3,6,1,4,1,2076,13,9,1,4),_FsMplsTpOamContextName_Type())
fsMplsTpOamContextName.setMaxAccess(_K)
if mibBuilder.loadTexts:fsMplsTpOamContextName.setStatus(_A)
class _FsMplsTpOamMegOperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('up',1),('down',2)))
_FsMplsTpOamMegOperStatus_Type.__name__=_D
_FsMplsTpOamMegOperStatus_Object=MibScalar
fsMplsTpOamMegOperStatus=_FsMplsTpOamMegOperStatus_Object((1,3,6,1,4,1,2076,13,9,1,5),_FsMplsTpOamMegOperStatus_Type())
fsMplsTpOamMegOperStatus.setMaxAccess(_K)
if mibBuilder.loadTexts:fsMplsTpOamMegOperStatus.setStatus(_A)
class _FsMplsTpOamMegSubOperStatus_Type(Bits):namedValues=NamedValues(*(('megDown',0),('meDown',1),('oamAppDown',2),('pathDown',3)))
_FsMplsTpOamMegSubOperStatus_Type.__name__='Bits'
_FsMplsTpOamMegSubOperStatus_Object=MibScalar
fsMplsTpOamMegSubOperStatus=_FsMplsTpOamMegSubOperStatus_Object((1,3,6,1,4,1,2076,13,9,1,6),_FsMplsTpOamMegSubOperStatus_Type())
fsMplsTpOamMegSubOperStatus.setMaxAccess(_K)
if mibBuilder.loadTexts:fsMplsTpOamMegSubOperStatus.setStatus(_A)
_FsMplsTpOamConformance_ObjectIdentity=ObjectIdentity
fsMplsTpOamConformance=_FsMplsTpOamConformance_ObjectIdentity((1,3,6,1,4,1,2076,13,9,2))
fsMplsTpOamDefectCondition=NotificationType((1,3,6,1,4,1,2076,13,9,0,1))
fsMplsTpOamDefectCondition.setObjects(*((_C,_R),(_C,_S),(_C,_T),(_C,_U),(_C,_V)))
if mibBuilder.loadTexts:fsMplsTpOamDefectCondition.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'fsMplsTpOamMIB':fsMplsTpOamMIB,'fsMplsTpOamNotifications':fsMplsTpOamNotifications,'fsMplsTpOamDefectCondition':fsMplsTpOamDefectCondition,'fsMplsTpOamObjects':fsMplsTpOamObjects,'fsMplsTpOamScalarObjects':fsMplsTpOamScalarObjects,'fsMplsTpMegTable':fsMplsTpMegTable,'fsMplsTpMegEntry':fsMplsTpMegEntry,_I:fsMplsTpMegIndex,_S:fsMplsTpMegName,'fsMplsTpMegOperatorType':fsMplsTpMegOperatorType,'fsMplsTpMegIdIcc':fsMplsTpMegIdIcc,'fsMplsTpMegIdUmc':fsMplsTpMegIdUmc,'fsMplsTpMegServiceType':fsMplsTpMegServiceType,'fsMplsTpMegMpLocation':fsMplsTpMegMpLocation,'fsMplsTpMegRowStatus':fsMplsTpMegRowStatus,'fsMplsTpMeTable':fsMplsTpMeTable,'fsMplsTpMeEntry':fsMplsTpMeEntry,_P:fsMplsTpMeIndex,_Q:fsMplsTpMeMpIndex,_T:fsMplsTpMeName,'fsMplsTpMeMpIfIndex':fsMplsTpMeMpIfIndex,'fsMplsTpMeSourceMepIndex':fsMplsTpMeSourceMepIndex,'fsMplsTpMeSinkMepIndex':fsMplsTpMeSinkMepIndex,'fsMplsTpMeMpType':fsMplsTpMeMpType,'fsMplsTpMeMepDirection':fsMplsTpMeMepDirection,'fsMplsTpMeProactiveOamSessIndex':fsMplsTpMeProactiveOamSessIndex,'fsMplsTpMeProactiveOamPhbTCValue':fsMplsTpMeProactiveOamPhbTCValue,'fsMplsTpMeOnDemandOamPhbTCValue':fsMplsTpMeOnDemandOamPhbTCValue,'fsMplsTpMeServiceSignaled':fsMplsTpMeServiceSignaled,'fsMplsTpMeServicePointer':fsMplsTpMeServicePointer,'fsMplsTpMeRowStatus':fsMplsTpMeRowStatus,_R:fsMplsTpOamContextName,_U:fsMplsTpOamMegOperStatus,_V:fsMplsTpOamMegSubOperStatus,'fsMplsTpOamConformance':fsMplsTpOamConformance})