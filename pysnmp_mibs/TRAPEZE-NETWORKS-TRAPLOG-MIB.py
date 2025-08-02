_g='trpzTraplogTrapDateGroup'
_f='trpzTraplogGuideDateGroup'
_e='trpzTraplogVarGroup'
_d='trpzTraplogTrapGroup'
_c='trpzTraplogGuideGroup'
_b='trpzTraplogVarCounter64Val'
_a='trpzTraplogVarOidVal'
_Z='trpzTraplogVarIpAddressVal'
_Y='trpzTraplogVarOctetStringVal'
_X='trpzTraplogVarInteger32Val'
_W='trpzTraplogVarTimeTicksVal'
_V='trpzTraplogVarUnsigned32Val'
_U='trpzTraplogVarCounter32Val'
_T='trpzTraplogVarValueType'
_S='trpzTraplogVarID'
_R='trpzTraplogTrapDateAndTime'
_Q='trpzTraplogTrapNumVars'
_P='trpzTraplogTrapNotificationID'
_O='trpzTraplogTrapTime'
_N='trpzTraplogNewestTrapDateAndTime'
_M='trpzTraplogNewestTrapTime'
_L='trpzTraplogNewestTrapIndex'
_K='trpzTraplogOldestTrapIndex'
_J='trpzTraplogVarIndex'
_I='trpzTraplogVarTrapIndex'
_H='trpzTraplogTrapIndex'
_G='DateAndTime'
_F='Integer32'
_E='not-accessible'
_D='Unsigned32'
_C='read-only'
_B='TRAPEZE-NETWORKS-TRAPLOG-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_F,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_D,'iso')
DateAndTime,DisplayString,PhysAddress,TextualConvention,TimeStamp=mibBuilder.importSymbols('SNMPv2-TC',_G,'DisplayString','PhysAddress','TextualConvention','TimeStamp')
trpzMibs,=mibBuilder.importSymbols('TRAPEZE-NETWORKS-ROOT-MIB','trpzMibs')
trpzTraplogMib=ModuleIdentity((1,3,6,1,4,1,14525,4,13))
if mibBuilder.loadTexts:trpzTraplogMib.setRevisions(('2009-03-22 00:09',))
class TrpzTraplogTrapOccurrenceIndex(TextualConvention,Unsigned32):status=_A;displayHint='d';subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
class TrpzTraplogTrapOccurrenceIndexOrZero(TextualConvention,Unsigned32):status=_A;displayHint='d';subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,4294967295))
_TrpzTraplogMibObjects_ObjectIdentity=ObjectIdentity
trpzTraplogMibObjects=_TrpzTraplogMibObjects_ObjectIdentity((1,3,6,1,4,1,14525,4,13,1))
_TrpzTraplogGuideObjects_ObjectIdentity=ObjectIdentity
trpzTraplogGuideObjects=_TrpzTraplogGuideObjects_ObjectIdentity((1,3,6,1,4,1,14525,4,13,1,2))
_TrpzTraplogOldestTrapIndex_Type=TrpzTraplogTrapOccurrenceIndexOrZero
_TrpzTraplogOldestTrapIndex_Object=MibScalar
trpzTraplogOldestTrapIndex=_TrpzTraplogOldestTrapIndex_Object((1,3,6,1,4,1,14525,4,13,1,2,1),_TrpzTraplogOldestTrapIndex_Type())
trpzTraplogOldestTrapIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:trpzTraplogOldestTrapIndex.setStatus(_A)
_TrpzTraplogNewestTrapIndex_Type=TrpzTraplogTrapOccurrenceIndexOrZero
_TrpzTraplogNewestTrapIndex_Object=MibScalar
trpzTraplogNewestTrapIndex=_TrpzTraplogNewestTrapIndex_Object((1,3,6,1,4,1,14525,4,13,1,2,2),_TrpzTraplogNewestTrapIndex_Type())
trpzTraplogNewestTrapIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:trpzTraplogNewestTrapIndex.setStatus(_A)
_TrpzTraplogNewestTrapTime_Type=TimeStamp
_TrpzTraplogNewestTrapTime_Object=MibScalar
trpzTraplogNewestTrapTime=_TrpzTraplogNewestTrapTime_Object((1,3,6,1,4,1,14525,4,13,1,2,3),_TrpzTraplogNewestTrapTime_Type())
trpzTraplogNewestTrapTime.setMaxAccess(_C)
if mibBuilder.loadTexts:trpzTraplogNewestTrapTime.setStatus(_A)
class _TrpzTraplogNewestTrapDateAndTime_Type(DateAndTime):defaultHexValue='0000000000000000'
_TrpzTraplogNewestTrapDateAndTime_Type.__name__=_G
_TrpzTraplogNewestTrapDateAndTime_Object=MibScalar
trpzTraplogNewestTrapDateAndTime=_TrpzTraplogNewestTrapDateAndTime_Object((1,3,6,1,4,1,14525,4,13,1,2,4),_TrpzTraplogNewestTrapDateAndTime_Type())
trpzTraplogNewestTrapDateAndTime.setMaxAccess(_C)
if mibBuilder.loadTexts:trpzTraplogNewestTrapDateAndTime.setStatus(_A)
_TrpzTraplogTrapTable_Object=MibTable
trpzTraplogTrapTable=_TrpzTraplogTrapTable_Object((1,3,6,1,4,1,14525,4,13,1,3))
if mibBuilder.loadTexts:trpzTraplogTrapTable.setStatus(_A)
_TrpzTraplogTrapEntry_Object=MibTableRow
trpzTraplogTrapEntry=_TrpzTraplogTrapEntry_Object((1,3,6,1,4,1,14525,4,13,1,3,1))
trpzTraplogTrapEntry.setIndexNames((0,_B,_H))
if mibBuilder.loadTexts:trpzTraplogTrapEntry.setStatus(_A)
_TrpzTraplogTrapIndex_Type=TrpzTraplogTrapOccurrenceIndex
_TrpzTraplogTrapIndex_Object=MibTableColumn
trpzTraplogTrapIndex=_TrpzTraplogTrapIndex_Object((1,3,6,1,4,1,14525,4,13,1,3,1,1),_TrpzTraplogTrapIndex_Type())
trpzTraplogTrapIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:trpzTraplogTrapIndex.setStatus(_A)
_TrpzTraplogTrapTime_Type=TimeStamp
_TrpzTraplogTrapTime_Object=MibTableColumn
trpzTraplogTrapTime=_TrpzTraplogTrapTime_Object((1,3,6,1,4,1,14525,4,13,1,3,1,2),_TrpzTraplogTrapTime_Type())
trpzTraplogTrapTime.setMaxAccess(_C)
if mibBuilder.loadTexts:trpzTraplogTrapTime.setStatus(_A)
_TrpzTraplogTrapDateAndTime_Type=DateAndTime
_TrpzTraplogTrapDateAndTime_Object=MibTableColumn
trpzTraplogTrapDateAndTime=_TrpzTraplogTrapDateAndTime_Object((1,3,6,1,4,1,14525,4,13,1,3,1,3),_TrpzTraplogTrapDateAndTime_Type())
trpzTraplogTrapDateAndTime.setMaxAccess(_C)
if mibBuilder.loadTexts:trpzTraplogTrapDateAndTime.setStatus(_A)
_TrpzTraplogTrapNotificationID_Type=ObjectIdentifier
_TrpzTraplogTrapNotificationID_Object=MibTableColumn
trpzTraplogTrapNotificationID=_TrpzTraplogTrapNotificationID_Object((1,3,6,1,4,1,14525,4,13,1,3,1,4),_TrpzTraplogTrapNotificationID_Type())
trpzTraplogTrapNotificationID.setMaxAccess(_C)
if mibBuilder.loadTexts:trpzTraplogTrapNotificationID.setStatus(_A)
class _TrpzTraplogTrapNumVars_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_TrpzTraplogTrapNumVars_Type.__name__=_D
_TrpzTraplogTrapNumVars_Object=MibTableColumn
trpzTraplogTrapNumVars=_TrpzTraplogTrapNumVars_Object((1,3,6,1,4,1,14525,4,13,1,3,1,5),_TrpzTraplogTrapNumVars_Type())
trpzTraplogTrapNumVars.setMaxAccess(_C)
if mibBuilder.loadTexts:trpzTraplogTrapNumVars.setStatus(_A)
_TrpzTraplogVarTable_Object=MibTable
trpzTraplogVarTable=_TrpzTraplogVarTable_Object((1,3,6,1,4,1,14525,4,13,1,4))
if mibBuilder.loadTexts:trpzTraplogVarTable.setStatus(_A)
_TrpzTraplogVarEntry_Object=MibTableRow
trpzTraplogVarEntry=_TrpzTraplogVarEntry_Object((1,3,6,1,4,1,14525,4,13,1,4,1))
trpzTraplogVarEntry.setIndexNames((0,_B,_I),(0,_B,_J))
if mibBuilder.loadTexts:trpzTraplogVarEntry.setStatus(_A)
_TrpzTraplogVarTrapIndex_Type=TrpzTraplogTrapOccurrenceIndex
_TrpzTraplogVarTrapIndex_Object=MibTableColumn
trpzTraplogVarTrapIndex=_TrpzTraplogVarTrapIndex_Object((1,3,6,1,4,1,14525,4,13,1,4,1,1),_TrpzTraplogVarTrapIndex_Type())
trpzTraplogVarTrapIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:trpzTraplogVarTrapIndex.setStatus(_A)
class _TrpzTraplogVarIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_TrpzTraplogVarIndex_Type.__name__=_D
_TrpzTraplogVarIndex_Object=MibTableColumn
trpzTraplogVarIndex=_TrpzTraplogVarIndex_Object((1,3,6,1,4,1,14525,4,13,1,4,1,2),_TrpzTraplogVarIndex_Type())
trpzTraplogVarIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:trpzTraplogVarIndex.setStatus(_A)
_TrpzTraplogVarID_Type=ObjectIdentifier
_TrpzTraplogVarID_Object=MibTableColumn
trpzTraplogVarID=_TrpzTraplogVarID_Object((1,3,6,1,4,1,14525,4,13,1,4,1,3),_TrpzTraplogVarID_Type())
trpzTraplogVarID.setMaxAccess(_C)
if mibBuilder.loadTexts:trpzTraplogVarID.setStatus(_A)
class _TrpzTraplogVarValueType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8)));namedValues=NamedValues(*(('counter32',1),('unsigned32',2),('timeTicks',3),('integer32',4),('ipAddress',5),('octetString',6),('objectId',7),('counter64',8)))
_TrpzTraplogVarValueType_Type.__name__=_F
_TrpzTraplogVarValueType_Object=MibTableColumn
trpzTraplogVarValueType=_TrpzTraplogVarValueType_Object((1,3,6,1,4,1,14525,4,13,1,4,1,4),_TrpzTraplogVarValueType_Type())
trpzTraplogVarValueType.setMaxAccess(_C)
if mibBuilder.loadTexts:trpzTraplogVarValueType.setStatus(_A)
_TrpzTraplogVarCounter32Val_Type=Counter32
_TrpzTraplogVarCounter32Val_Object=MibTableColumn
trpzTraplogVarCounter32Val=_TrpzTraplogVarCounter32Val_Object((1,3,6,1,4,1,14525,4,13,1,4,1,5),_TrpzTraplogVarCounter32Val_Type())
trpzTraplogVarCounter32Val.setMaxAccess(_C)
if mibBuilder.loadTexts:trpzTraplogVarCounter32Val.setStatus(_A)
_TrpzTraplogVarUnsigned32Val_Type=Unsigned32
_TrpzTraplogVarUnsigned32Val_Object=MibTableColumn
trpzTraplogVarUnsigned32Val=_TrpzTraplogVarUnsigned32Val_Object((1,3,6,1,4,1,14525,4,13,1,4,1,6),_TrpzTraplogVarUnsigned32Val_Type())
trpzTraplogVarUnsigned32Val.setMaxAccess(_C)
if mibBuilder.loadTexts:trpzTraplogVarUnsigned32Val.setStatus(_A)
_TrpzTraplogVarTimeTicksVal_Type=TimeTicks
_TrpzTraplogVarTimeTicksVal_Object=MibTableColumn
trpzTraplogVarTimeTicksVal=_TrpzTraplogVarTimeTicksVal_Object((1,3,6,1,4,1,14525,4,13,1,4,1,7),_TrpzTraplogVarTimeTicksVal_Type())
trpzTraplogVarTimeTicksVal.setMaxAccess(_C)
if mibBuilder.loadTexts:trpzTraplogVarTimeTicksVal.setStatus(_A)
_TrpzTraplogVarInteger32Val_Type=Integer32
_TrpzTraplogVarInteger32Val_Object=MibTableColumn
trpzTraplogVarInteger32Val=_TrpzTraplogVarInteger32Val_Object((1,3,6,1,4,1,14525,4,13,1,4,1,8),_TrpzTraplogVarInteger32Val_Type())
trpzTraplogVarInteger32Val.setMaxAccess(_C)
if mibBuilder.loadTexts:trpzTraplogVarInteger32Val.setStatus(_A)
_TrpzTraplogVarOctetStringVal_Type=OctetString
_TrpzTraplogVarOctetStringVal_Object=MibTableColumn
trpzTraplogVarOctetStringVal=_TrpzTraplogVarOctetStringVal_Object((1,3,6,1,4,1,14525,4,13,1,4,1,9),_TrpzTraplogVarOctetStringVal_Type())
trpzTraplogVarOctetStringVal.setMaxAccess(_C)
if mibBuilder.loadTexts:trpzTraplogVarOctetStringVal.setStatus(_A)
_TrpzTraplogVarIpAddressVal_Type=IpAddress
_TrpzTraplogVarIpAddressVal_Object=MibTableColumn
trpzTraplogVarIpAddressVal=_TrpzTraplogVarIpAddressVal_Object((1,3,6,1,4,1,14525,4,13,1,4,1,10),_TrpzTraplogVarIpAddressVal_Type())
trpzTraplogVarIpAddressVal.setMaxAccess(_C)
if mibBuilder.loadTexts:trpzTraplogVarIpAddressVal.setStatus(_A)
_TrpzTraplogVarOidVal_Type=ObjectIdentifier
_TrpzTraplogVarOidVal_Object=MibTableColumn
trpzTraplogVarOidVal=_TrpzTraplogVarOidVal_Object((1,3,6,1,4,1,14525,4,13,1,4,1,11),_TrpzTraplogVarOidVal_Type())
trpzTraplogVarOidVal.setMaxAccess(_C)
if mibBuilder.loadTexts:trpzTraplogVarOidVal.setStatus(_A)
_TrpzTraplogVarCounter64Val_Type=Counter64
_TrpzTraplogVarCounter64Val_Object=MibTableColumn
trpzTraplogVarCounter64Val=_TrpzTraplogVarCounter64Val_Object((1,3,6,1,4,1,14525,4,13,1,4,1,12),_TrpzTraplogVarCounter64Val_Type())
trpzTraplogVarCounter64Val.setMaxAccess(_C)
if mibBuilder.loadTexts:trpzTraplogVarCounter64Val.setStatus(_A)
_TrpzTraplogConformance_ObjectIdentity=ObjectIdentity
trpzTraplogConformance=_TrpzTraplogConformance_ObjectIdentity((1,3,6,1,4,1,14525,4,13,2))
_TrpzTraplogCompliances_ObjectIdentity=ObjectIdentity
trpzTraplogCompliances=_TrpzTraplogCompliances_ObjectIdentity((1,3,6,1,4,1,14525,4,13,2,1))
_TrpzTraplogGroups_ObjectIdentity=ObjectIdentity
trpzTraplogGroups=_TrpzTraplogGroups_ObjectIdentity((1,3,6,1,4,1,14525,4,13,2,2))
trpzTraplogGuideGroup=ObjectGroup((1,3,6,1,4,1,14525,4,13,2,2,1))
trpzTraplogGuideGroup.setObjects(*((_B,_K),(_B,_L),(_B,_M)))
if mibBuilder.loadTexts:trpzTraplogGuideGroup.setStatus(_A)
trpzTraplogGuideDateGroup=ObjectGroup((1,3,6,1,4,1,14525,4,13,2,2,2))
trpzTraplogGuideDateGroup.setObjects((_B,_N))
if mibBuilder.loadTexts:trpzTraplogGuideDateGroup.setStatus(_A)
trpzTraplogTrapGroup=ObjectGroup((1,3,6,1,4,1,14525,4,13,2,2,3))
trpzTraplogTrapGroup.setObjects(*((_B,_O),(_B,_P),(_B,_Q)))
if mibBuilder.loadTexts:trpzTraplogTrapGroup.setStatus(_A)
trpzTraplogTrapDateGroup=ObjectGroup((1,3,6,1,4,1,14525,4,13,2,2,4))
trpzTraplogTrapDateGroup.setObjects((_B,_R))
if mibBuilder.loadTexts:trpzTraplogTrapDateGroup.setStatus(_A)
trpzTraplogVarGroup=ObjectGroup((1,3,6,1,4,1,14525,4,13,2,2,5))
trpzTraplogVarGroup.setObjects(*((_B,_S),(_B,_T),(_B,_U),(_B,_V),(_B,_W),(_B,_X),(_B,_Y),(_B,_Z),(_B,_a),(_B,_b)))
if mibBuilder.loadTexts:trpzTraplogVarGroup.setStatus(_A)
trpzTraplogCompliance=ModuleCompliance((1,3,6,1,4,1,14525,4,13,2,1,1))
trpzTraplogCompliance.setObjects(*((_B,_c),(_B,_d),(_B,_e),(_B,_f),(_B,_g)))
if mibBuilder.loadTexts:trpzTraplogCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'TrpzTraplogTrapOccurrenceIndex':TrpzTraplogTrapOccurrenceIndex,'TrpzTraplogTrapOccurrenceIndexOrZero':TrpzTraplogTrapOccurrenceIndexOrZero,'trpzTraplogMib':trpzTraplogMib,'trpzTraplogMibObjects':trpzTraplogMibObjects,'trpzTraplogGuideObjects':trpzTraplogGuideObjects,_K:trpzTraplogOldestTrapIndex,_L:trpzTraplogNewestTrapIndex,_M:trpzTraplogNewestTrapTime,_N:trpzTraplogNewestTrapDateAndTime,'trpzTraplogTrapTable':trpzTraplogTrapTable,'trpzTraplogTrapEntry':trpzTraplogTrapEntry,_H:trpzTraplogTrapIndex,_O:trpzTraplogTrapTime,_R:trpzTraplogTrapDateAndTime,_P:trpzTraplogTrapNotificationID,_Q:trpzTraplogTrapNumVars,'trpzTraplogVarTable':trpzTraplogVarTable,'trpzTraplogVarEntry':trpzTraplogVarEntry,_I:trpzTraplogVarTrapIndex,_J:trpzTraplogVarIndex,_S:trpzTraplogVarID,_T:trpzTraplogVarValueType,_U:trpzTraplogVarCounter32Val,_V:trpzTraplogVarUnsigned32Val,_W:trpzTraplogVarTimeTicksVal,_X:trpzTraplogVarInteger32Val,_Y:trpzTraplogVarOctetStringVal,_Z:trpzTraplogVarIpAddressVal,_a:trpzTraplogVarOidVal,_b:trpzTraplogVarCounter64Val,'trpzTraplogConformance':trpzTraplogConformance,'trpzTraplogCompliances':trpzTraplogCompliances,'trpzTraplogCompliance':trpzTraplogCompliance,'trpzTraplogGroups':trpzTraplogGroups,_c:trpzTraplogGuideGroup,_f:trpzTraplogGuideDateGroup,_d:trpzTraplogTrapGroup,_g:trpzTraplogTrapDateGroup,_e:trpzTraplogVarGroup})