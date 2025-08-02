_V='devDS1SendControlIfIndex'
_U='devDS1MonResultTestType'
_T='devDS1MonResultIfIndex'
_S='mon2E11'
_R='mon2E7'
_Q='monUserDefined'
_P='mon2E20'
_O='mon2E15'
_N='mon2047'
_M='mon3in24'
_L='mon1in8'
_K='monOnes'
_J='monZeros'
_I='monQRSS'
_H='devDS1TestType'
_G='devDS1TestIfIndex'
_F='DisplayString'
_E='read-write'
_D='PDN-DS1CONFIG-MIB'
_C='Integer32'
_B='read-only'
_A='mandatory'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
pdn_interfaces,=mibBuilder.importSymbols('PDN-HEADER-MIB','pdn-interfaces')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_F,'PhysAddress','TextualConvention')
_Ent_ds1_ObjectIdentity=ObjectIdentity
ent_ds1=_Ent_ds1_ObjectIdentity((1,3,6,1,4,1,1795,2,24,2,6,5))
_DevDS1Test_ObjectIdentity=ObjectIdentity
devDS1Test=_DevDS1Test_ObjectIdentity((1,3,6,1,4,1,1795,2,24,2,6,5,1))
_DevDS1TestTable_Object=MibTable
devDS1TestTable=_DevDS1TestTable_Object((1,3,6,1,4,1,1795,2,24,2,6,5,1,1))
if mibBuilder.loadTexts:devDS1TestTable.setStatus(_A)
_DevDS1TestEntry_Object=MibTableRow
devDS1TestEntry=_DevDS1TestEntry_Object((1,3,6,1,4,1,1795,2,24,2,6,5,1,1,1))
devDS1TestEntry.setIndexNames((0,_D,_G),(0,_D,_H))
if mibBuilder.loadTexts:devDS1TestEntry.setStatus(_A)
_DevDS1TestIfIndex_Type=Integer32
_DevDS1TestIfIndex_Object=MibTableColumn
devDS1TestIfIndex=_DevDS1TestIfIndex_Object((1,3,6,1,4,1,1795,2,24,2,6,5,1,1,1,1),_DevDS1TestIfIndex_Type())
devDS1TestIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:devDS1TestIfIndex.setStatus(_A)
class _DevDS1TestType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31)));namedValues=NamedValues(*(('llbup',1),('llbdn',2),('llb',3),('plb',4),('rlb',5),('sendQRSS',6),('sendZeros',7),('sendOnes',8),('send1in8',9),('send3in24',10),('send63',11),('send511',12),('send2047',13),('send2E15',14),('send2E20',15),('sendUserDefined',16),(_I,17),(_J,18),(_K,19),(_L,20),(_M,21),('mon63',22),('mon11',23),(_N,24),(_O,25),(_P,26),(_Q,27),('send2E7',28),(_R,29),('send2E11',30),(_S,31)))
_DevDS1TestType_Type.__name__=_C
_DevDS1TestType_Object=MibTableColumn
devDS1TestType=_DevDS1TestType_Object((1,3,6,1,4,1,1795,2,24,2,6,5,1,1,1,2),_DevDS1TestType_Type())
devDS1TestType.setMaxAccess(_B)
if mibBuilder.loadTexts:devDS1TestType.setStatus(_A)
class _DevDS1TestControl_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('idle',1),('running',2)))
_DevDS1TestControl_Type.__name__=_C
_DevDS1TestControl_Object=MibTableColumn
devDS1TestControl=_DevDS1TestControl_Object((1,3,6,1,4,1,1795,2,24,2,6,5,1,1,1,3),_DevDS1TestControl_Type())
devDS1TestControl.setMaxAccess(_E)
if mibBuilder.loadTexts:devDS1TestControl.setStatus(_A)
class _DevDS1TestArgument_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_DevDS1TestArgument_Type.__name__=_F
_DevDS1TestArgument_Object=MibTableColumn
devDS1TestArgument=_DevDS1TestArgument_Object((1,3,6,1,4,1,1795,2,24,2,6,5,1,1,1,4),_DevDS1TestArgument_Type())
devDS1TestArgument.setMaxAccess(_E)
if mibBuilder.loadTexts:devDS1TestArgument.setStatus(_A)
_DevDS1MonResultTable_Object=MibTable
devDS1MonResultTable=_DevDS1MonResultTable_Object((1,3,6,1,4,1,1795,2,24,2,6,5,1,2))
if mibBuilder.loadTexts:devDS1MonResultTable.setStatus(_A)
_DevDS1MonResultEntry_Object=MibTableRow
devDS1MonResultEntry=_DevDS1MonResultEntry_Object((1,3,6,1,4,1,1795,2,24,2,6,5,1,2,1))
devDS1MonResultEntry.setIndexNames((0,_D,_T),(0,_D,_U))
if mibBuilder.loadTexts:devDS1MonResultEntry.setStatus(_A)
_DevDS1MonResultIfIndex_Type=Integer32
_DevDS1MonResultIfIndex_Object=MibTableColumn
devDS1MonResultIfIndex=_DevDS1MonResultIfIndex_Object((1,3,6,1,4,1,1795,2,24,2,6,5,1,2,1,1),_DevDS1MonResultIfIndex_Type())
devDS1MonResultIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:devDS1MonResultIfIndex.setStatus(_A)
class _DevDS1MonResultTestType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(17,18,19,20,21,22,23,24,25,26,27,29,31)));namedValues=NamedValues(*((_I,17),(_J,18),(_K,19),(_L,20),(_M,21),('mon63',22),('mon11',23),(_N,24),(_O,25),(_P,26),(_Q,27),(_R,29),(_S,31)))
_DevDS1MonResultTestType_Type.__name__=_C
_DevDS1MonResultTestType_Object=MibTableColumn
devDS1MonResultTestType=_DevDS1MonResultTestType_Object((1,3,6,1,4,1,1795,2,24,2,6,5,1,2,1,2),_DevDS1MonResultTestType_Type())
devDS1MonResultTestType.setMaxAccess(_B)
if mibBuilder.loadTexts:devDS1MonResultTestType.setStatus(_A)
class _DevDS1MonResultCode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('none',1),('inSyncNoBitErrors',2),('inSyncWithBitErrors',3),('notInSync',4)))
_DevDS1MonResultCode_Type.__name__=_C
_DevDS1MonResultCode_Object=MibTableColumn
devDS1MonResultCode=_DevDS1MonResultCode_Object((1,3,6,1,4,1,1795,2,24,2,6,5,1,2,1,3),_DevDS1MonResultCode_Type())
devDS1MonResultCode.setMaxAccess(_B)
if mibBuilder.loadTexts:devDS1MonResultCode.setStatus(_A)
_DevDS1MonResultErrorCount_Type=Gauge32
_DevDS1MonResultErrorCount_Object=MibTableColumn
devDS1MonResultErrorCount=_DevDS1MonResultErrorCount_Object((1,3,6,1,4,1,1795,2,24,2,6,5,1,2,1,4),_DevDS1MonResultErrorCount_Type())
devDS1MonResultErrorCount.setMaxAccess(_E)
if mibBuilder.loadTexts:devDS1MonResultErrorCount.setStatus(_A)
_DevDS1SendControlTable_Object=MibTable
devDS1SendControlTable=_DevDS1SendControlTable_Object((1,3,6,1,4,1,1795,2,24,2,6,5,1,3))
if mibBuilder.loadTexts:devDS1SendControlTable.setStatus(_A)
_DevDS1SendControlEntry_Object=MibTableRow
devDS1SendControlEntry=_DevDS1SendControlEntry_Object((1,3,6,1,4,1,1795,2,24,2,6,5,1,3,1))
devDS1SendControlEntry.setIndexNames((0,_D,_V))
if mibBuilder.loadTexts:devDS1SendControlEntry.setStatus(_A)
_DevDS1SendControlIfIndex_Type=Integer32
_DevDS1SendControlIfIndex_Object=MibTableColumn
devDS1SendControlIfIndex=_DevDS1SendControlIfIndex_Object((1,3,6,1,4,1,1795,2,24,2,6,5,1,3,1,1),_DevDS1SendControlIfIndex_Type())
devDS1SendControlIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:devDS1SendControlIfIndex.setStatus(_A)
class _DevDS1SendControlInjectErr_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('noOp',1),('inject',2)))
_DevDS1SendControlInjectErr_Type.__name__=_C
_DevDS1SendControlInjectErr_Object=MibTableColumn
devDS1SendControlInjectErr=_DevDS1SendControlInjectErr_Object((1,3,6,1,4,1,1795,2,24,2,6,5,1,3,1,2),_DevDS1SendControlInjectErr_Type())
devDS1SendControlInjectErr.setMaxAccess(_E)
if mibBuilder.loadTexts:devDS1SendControlInjectErr.setStatus(_A)
_DevDS1SendControlErrorCount_Type=Gauge32
_DevDS1SendControlErrorCount_Object=MibTableColumn
devDS1SendControlErrorCount=_DevDS1SendControlErrorCount_Object((1,3,6,1,4,1,1795,2,24,2,6,5,1,3,1,3),_DevDS1SendControlErrorCount_Type())
devDS1SendControlErrorCount.setMaxAccess(_B)
if mibBuilder.loadTexts:devDS1SendControlErrorCount.setStatus(_A)
mibBuilder.exportSymbols(_D,**{'ent-ds1':ent_ds1,'devDS1Test':devDS1Test,'devDS1TestTable':devDS1TestTable,'devDS1TestEntry':devDS1TestEntry,_G:devDS1TestIfIndex,_H:devDS1TestType,'devDS1TestControl':devDS1TestControl,'devDS1TestArgument':devDS1TestArgument,'devDS1MonResultTable':devDS1MonResultTable,'devDS1MonResultEntry':devDS1MonResultEntry,_T:devDS1MonResultIfIndex,_U:devDS1MonResultTestType,'devDS1MonResultCode':devDS1MonResultCode,'devDS1MonResultErrorCount':devDS1MonResultErrorCount,'devDS1SendControlTable':devDS1SendControlTable,'devDS1SendControlEntry':devDS1SendControlEntry,_V:devDS1SendControlIfIndex,'devDS1SendControlInjectErr':devDS1SendControlInjectErr,'devDS1SendControlErrorCount':devDS1SendControlErrorCount})