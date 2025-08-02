_g='ntwsTraplogTrapDateGroup'
_f='ntwsTraplogGuideDateGroup'
_e='ntwsTraplogVarGroup'
_d='ntwsTraplogTrapGroup'
_c='ntwsTraplogGuideGroup'
_b='ntwsTraplogVarCounter64Val'
_a='ntwsTraplogVarOidVal'
_Z='ntwsTraplogVarIpAddressVal'
_Y='ntwsTraplogVarOctetStringVal'
_X='ntwsTraplogVarInteger32Val'
_W='ntwsTraplogVarTimeTicksVal'
_V='ntwsTraplogVarUnsigned32Val'
_U='ntwsTraplogVarCounter32Val'
_T='ntwsTraplogVarValueType'
_S='ntwsTraplogVarID'
_R='ntwsTraplogTrapDateAndTime'
_Q='ntwsTraplogTrapNumVars'
_P='ntwsTraplogTrapNotificationID'
_O='ntwsTraplogTrapTime'
_N='ntwsTraplogNewestTrapDateAndTime'
_M='ntwsTraplogNewestTrapTime'
_L='ntwsTraplogNewestTrapIndex'
_K='ntwsTraplogOldestTrapIndex'
_J='ntwsTraplogVarIndex'
_I='ntwsTraplogVarTrapIndex'
_H='ntwsTraplogTrapIndex'
_G='DateAndTime'
_F='Integer32'
_E='not-accessible'
_D='Unsigned32'
_C='read-only'
_B='NTWS-TRAPLOG-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ntwsMibs,=mibBuilder.importSymbols('NTWS-ROOT-MIB','ntwsMibs')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_F,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_D,'iso')
DateAndTime,DisplayString,PhysAddress,TextualConvention,TimeStamp=mibBuilder.importSymbols('SNMPv2-TC',_G,'DisplayString','PhysAddress','TextualConvention','TimeStamp')
ntwsTraplogMib=ModuleIdentity((1,3,6,1,4,1,45,6,1,4,13))
if mibBuilder.loadTexts:ntwsTraplogMib.setRevisions(('2009-03-22 00:09',))
class NtwsTraplogTrapOccurrenceIndex(TextualConvention,Unsigned32):status=_A;displayHint='d';subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
class NtwsTraplogTrapOccurrenceIndexOrZero(TextualConvention,Unsigned32):status=_A;displayHint='d';subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,4294967295))
_NtwsTraplogMibObjects_ObjectIdentity=ObjectIdentity
ntwsTraplogMibObjects=_NtwsTraplogMibObjects_ObjectIdentity((1,3,6,1,4,1,45,6,1,4,13,1))
_NtwsTraplogGuideObjects_ObjectIdentity=ObjectIdentity
ntwsTraplogGuideObjects=_NtwsTraplogGuideObjects_ObjectIdentity((1,3,6,1,4,1,45,6,1,4,13,1,2))
_NtwsTraplogOldestTrapIndex_Type=NtwsTraplogTrapOccurrenceIndexOrZero
_NtwsTraplogOldestTrapIndex_Object=MibScalar
ntwsTraplogOldestTrapIndex=_NtwsTraplogOldestTrapIndex_Object((1,3,6,1,4,1,45,6,1,4,13,1,2,1),_NtwsTraplogOldestTrapIndex_Type())
ntwsTraplogOldestTrapIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:ntwsTraplogOldestTrapIndex.setStatus(_A)
_NtwsTraplogNewestTrapIndex_Type=NtwsTraplogTrapOccurrenceIndexOrZero
_NtwsTraplogNewestTrapIndex_Object=MibScalar
ntwsTraplogNewestTrapIndex=_NtwsTraplogNewestTrapIndex_Object((1,3,6,1,4,1,45,6,1,4,13,1,2,2),_NtwsTraplogNewestTrapIndex_Type())
ntwsTraplogNewestTrapIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:ntwsTraplogNewestTrapIndex.setStatus(_A)
_NtwsTraplogNewestTrapTime_Type=TimeStamp
_NtwsTraplogNewestTrapTime_Object=MibScalar
ntwsTraplogNewestTrapTime=_NtwsTraplogNewestTrapTime_Object((1,3,6,1,4,1,45,6,1,4,13,1,2,3),_NtwsTraplogNewestTrapTime_Type())
ntwsTraplogNewestTrapTime.setMaxAccess(_C)
if mibBuilder.loadTexts:ntwsTraplogNewestTrapTime.setStatus(_A)
class _NtwsTraplogNewestTrapDateAndTime_Type(DateAndTime):defaultHexValue='0000000000000000'
_NtwsTraplogNewestTrapDateAndTime_Type.__name__=_G
_NtwsTraplogNewestTrapDateAndTime_Object=MibScalar
ntwsTraplogNewestTrapDateAndTime=_NtwsTraplogNewestTrapDateAndTime_Object((1,3,6,1,4,1,45,6,1,4,13,1,2,4),_NtwsTraplogNewestTrapDateAndTime_Type())
ntwsTraplogNewestTrapDateAndTime.setMaxAccess(_C)
if mibBuilder.loadTexts:ntwsTraplogNewestTrapDateAndTime.setStatus(_A)
_NtwsTraplogTrapTable_Object=MibTable
ntwsTraplogTrapTable=_NtwsTraplogTrapTable_Object((1,3,6,1,4,1,45,6,1,4,13,1,3))
if mibBuilder.loadTexts:ntwsTraplogTrapTable.setStatus(_A)
_NtwsTraplogTrapEntry_Object=MibTableRow
ntwsTraplogTrapEntry=_NtwsTraplogTrapEntry_Object((1,3,6,1,4,1,45,6,1,4,13,1,3,1))
ntwsTraplogTrapEntry.setIndexNames((0,_B,_H))
if mibBuilder.loadTexts:ntwsTraplogTrapEntry.setStatus(_A)
_NtwsTraplogTrapIndex_Type=NtwsTraplogTrapOccurrenceIndex
_NtwsTraplogTrapIndex_Object=MibTableColumn
ntwsTraplogTrapIndex=_NtwsTraplogTrapIndex_Object((1,3,6,1,4,1,45,6,1,4,13,1,3,1,1),_NtwsTraplogTrapIndex_Type())
ntwsTraplogTrapIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:ntwsTraplogTrapIndex.setStatus(_A)
_NtwsTraplogTrapTime_Type=TimeStamp
_NtwsTraplogTrapTime_Object=MibTableColumn
ntwsTraplogTrapTime=_NtwsTraplogTrapTime_Object((1,3,6,1,4,1,45,6,1,4,13,1,3,1,2),_NtwsTraplogTrapTime_Type())
ntwsTraplogTrapTime.setMaxAccess(_C)
if mibBuilder.loadTexts:ntwsTraplogTrapTime.setStatus(_A)
_NtwsTraplogTrapDateAndTime_Type=DateAndTime
_NtwsTraplogTrapDateAndTime_Object=MibTableColumn
ntwsTraplogTrapDateAndTime=_NtwsTraplogTrapDateAndTime_Object((1,3,6,1,4,1,45,6,1,4,13,1,3,1,3),_NtwsTraplogTrapDateAndTime_Type())
ntwsTraplogTrapDateAndTime.setMaxAccess(_C)
if mibBuilder.loadTexts:ntwsTraplogTrapDateAndTime.setStatus(_A)
_NtwsTraplogTrapNotificationID_Type=ObjectIdentifier
_NtwsTraplogTrapNotificationID_Object=MibTableColumn
ntwsTraplogTrapNotificationID=_NtwsTraplogTrapNotificationID_Object((1,3,6,1,4,1,45,6,1,4,13,1,3,1,4),_NtwsTraplogTrapNotificationID_Type())
ntwsTraplogTrapNotificationID.setMaxAccess(_C)
if mibBuilder.loadTexts:ntwsTraplogTrapNotificationID.setStatus(_A)
class _NtwsTraplogTrapNumVars_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_NtwsTraplogTrapNumVars_Type.__name__=_D
_NtwsTraplogTrapNumVars_Object=MibTableColumn
ntwsTraplogTrapNumVars=_NtwsTraplogTrapNumVars_Object((1,3,6,1,4,1,45,6,1,4,13,1,3,1,5),_NtwsTraplogTrapNumVars_Type())
ntwsTraplogTrapNumVars.setMaxAccess(_C)
if mibBuilder.loadTexts:ntwsTraplogTrapNumVars.setStatus(_A)
_NtwsTraplogVarTable_Object=MibTable
ntwsTraplogVarTable=_NtwsTraplogVarTable_Object((1,3,6,1,4,1,45,6,1,4,13,1,4))
if mibBuilder.loadTexts:ntwsTraplogVarTable.setStatus(_A)
_NtwsTraplogVarEntry_Object=MibTableRow
ntwsTraplogVarEntry=_NtwsTraplogVarEntry_Object((1,3,6,1,4,1,45,6,1,4,13,1,4,1))
ntwsTraplogVarEntry.setIndexNames((0,_B,_I),(0,_B,_J))
if mibBuilder.loadTexts:ntwsTraplogVarEntry.setStatus(_A)
_NtwsTraplogVarTrapIndex_Type=NtwsTraplogTrapOccurrenceIndex
_NtwsTraplogVarTrapIndex_Object=MibTableColumn
ntwsTraplogVarTrapIndex=_NtwsTraplogVarTrapIndex_Object((1,3,6,1,4,1,45,6,1,4,13,1,4,1,1),_NtwsTraplogVarTrapIndex_Type())
ntwsTraplogVarTrapIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:ntwsTraplogVarTrapIndex.setStatus(_A)
class _NtwsTraplogVarIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_NtwsTraplogVarIndex_Type.__name__=_D
_NtwsTraplogVarIndex_Object=MibTableColumn
ntwsTraplogVarIndex=_NtwsTraplogVarIndex_Object((1,3,6,1,4,1,45,6,1,4,13,1,4,1,2),_NtwsTraplogVarIndex_Type())
ntwsTraplogVarIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:ntwsTraplogVarIndex.setStatus(_A)
_NtwsTraplogVarID_Type=ObjectIdentifier
_NtwsTraplogVarID_Object=MibTableColumn
ntwsTraplogVarID=_NtwsTraplogVarID_Object((1,3,6,1,4,1,45,6,1,4,13,1,4,1,3),_NtwsTraplogVarID_Type())
ntwsTraplogVarID.setMaxAccess(_C)
if mibBuilder.loadTexts:ntwsTraplogVarID.setStatus(_A)
class _NtwsTraplogVarValueType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8)));namedValues=NamedValues(*(('counter32',1),('unsigned32',2),('timeTicks',3),('integer32',4),('ipAddress',5),('octetString',6),('objectId',7),('counter64',8)))
_NtwsTraplogVarValueType_Type.__name__=_F
_NtwsTraplogVarValueType_Object=MibTableColumn
ntwsTraplogVarValueType=_NtwsTraplogVarValueType_Object((1,3,6,1,4,1,45,6,1,4,13,1,4,1,4),_NtwsTraplogVarValueType_Type())
ntwsTraplogVarValueType.setMaxAccess(_C)
if mibBuilder.loadTexts:ntwsTraplogVarValueType.setStatus(_A)
_NtwsTraplogVarCounter32Val_Type=Counter32
_NtwsTraplogVarCounter32Val_Object=MibTableColumn
ntwsTraplogVarCounter32Val=_NtwsTraplogVarCounter32Val_Object((1,3,6,1,4,1,45,6,1,4,13,1,4,1,5),_NtwsTraplogVarCounter32Val_Type())
ntwsTraplogVarCounter32Val.setMaxAccess(_C)
if mibBuilder.loadTexts:ntwsTraplogVarCounter32Val.setStatus(_A)
_NtwsTraplogVarUnsigned32Val_Type=Unsigned32
_NtwsTraplogVarUnsigned32Val_Object=MibTableColumn
ntwsTraplogVarUnsigned32Val=_NtwsTraplogVarUnsigned32Val_Object((1,3,6,1,4,1,45,6,1,4,13,1,4,1,6),_NtwsTraplogVarUnsigned32Val_Type())
ntwsTraplogVarUnsigned32Val.setMaxAccess(_C)
if mibBuilder.loadTexts:ntwsTraplogVarUnsigned32Val.setStatus(_A)
_NtwsTraplogVarTimeTicksVal_Type=TimeTicks
_NtwsTraplogVarTimeTicksVal_Object=MibTableColumn
ntwsTraplogVarTimeTicksVal=_NtwsTraplogVarTimeTicksVal_Object((1,3,6,1,4,1,45,6,1,4,13,1,4,1,7),_NtwsTraplogVarTimeTicksVal_Type())
ntwsTraplogVarTimeTicksVal.setMaxAccess(_C)
if mibBuilder.loadTexts:ntwsTraplogVarTimeTicksVal.setStatus(_A)
_NtwsTraplogVarInteger32Val_Type=Integer32
_NtwsTraplogVarInteger32Val_Object=MibTableColumn
ntwsTraplogVarInteger32Val=_NtwsTraplogVarInteger32Val_Object((1,3,6,1,4,1,45,6,1,4,13,1,4,1,8),_NtwsTraplogVarInteger32Val_Type())
ntwsTraplogVarInteger32Val.setMaxAccess(_C)
if mibBuilder.loadTexts:ntwsTraplogVarInteger32Val.setStatus(_A)
_NtwsTraplogVarOctetStringVal_Type=OctetString
_NtwsTraplogVarOctetStringVal_Object=MibTableColumn
ntwsTraplogVarOctetStringVal=_NtwsTraplogVarOctetStringVal_Object((1,3,6,1,4,1,45,6,1,4,13,1,4,1,9),_NtwsTraplogVarOctetStringVal_Type())
ntwsTraplogVarOctetStringVal.setMaxAccess(_C)
if mibBuilder.loadTexts:ntwsTraplogVarOctetStringVal.setStatus(_A)
_NtwsTraplogVarIpAddressVal_Type=IpAddress
_NtwsTraplogVarIpAddressVal_Object=MibTableColumn
ntwsTraplogVarIpAddressVal=_NtwsTraplogVarIpAddressVal_Object((1,3,6,1,4,1,45,6,1,4,13,1,4,1,10),_NtwsTraplogVarIpAddressVal_Type())
ntwsTraplogVarIpAddressVal.setMaxAccess(_C)
if mibBuilder.loadTexts:ntwsTraplogVarIpAddressVal.setStatus(_A)
_NtwsTraplogVarOidVal_Type=ObjectIdentifier
_NtwsTraplogVarOidVal_Object=MibTableColumn
ntwsTraplogVarOidVal=_NtwsTraplogVarOidVal_Object((1,3,6,1,4,1,45,6,1,4,13,1,4,1,11),_NtwsTraplogVarOidVal_Type())
ntwsTraplogVarOidVal.setMaxAccess(_C)
if mibBuilder.loadTexts:ntwsTraplogVarOidVal.setStatus(_A)
_NtwsTraplogVarCounter64Val_Type=Counter64
_NtwsTraplogVarCounter64Val_Object=MibTableColumn
ntwsTraplogVarCounter64Val=_NtwsTraplogVarCounter64Val_Object((1,3,6,1,4,1,45,6,1,4,13,1,4,1,12),_NtwsTraplogVarCounter64Val_Type())
ntwsTraplogVarCounter64Val.setMaxAccess(_C)
if mibBuilder.loadTexts:ntwsTraplogVarCounter64Val.setStatus(_A)
_NtwsTraplogConformance_ObjectIdentity=ObjectIdentity
ntwsTraplogConformance=_NtwsTraplogConformance_ObjectIdentity((1,3,6,1,4,1,45,6,1,4,13,2))
_NtwsTraplogCompliances_ObjectIdentity=ObjectIdentity
ntwsTraplogCompliances=_NtwsTraplogCompliances_ObjectIdentity((1,3,6,1,4,1,45,6,1,4,13,2,1))
_NtwsTraplogGroups_ObjectIdentity=ObjectIdentity
ntwsTraplogGroups=_NtwsTraplogGroups_ObjectIdentity((1,3,6,1,4,1,45,6,1,4,13,2,2))
ntwsTraplogGuideGroup=ObjectGroup((1,3,6,1,4,1,45,6,1,4,13,2,2,1))
ntwsTraplogGuideGroup.setObjects(*((_B,_K),(_B,_L),(_B,_M)))
if mibBuilder.loadTexts:ntwsTraplogGuideGroup.setStatus(_A)
ntwsTraplogGuideDateGroup=ObjectGroup((1,3,6,1,4,1,45,6,1,4,13,2,2,2))
ntwsTraplogGuideDateGroup.setObjects((_B,_N))
if mibBuilder.loadTexts:ntwsTraplogGuideDateGroup.setStatus(_A)
ntwsTraplogTrapGroup=ObjectGroup((1,3,6,1,4,1,45,6,1,4,13,2,2,3))
ntwsTraplogTrapGroup.setObjects(*((_B,_O),(_B,_P),(_B,_Q)))
if mibBuilder.loadTexts:ntwsTraplogTrapGroup.setStatus(_A)
ntwsTraplogTrapDateGroup=ObjectGroup((1,3,6,1,4,1,45,6,1,4,13,2,2,4))
ntwsTraplogTrapDateGroup.setObjects((_B,_R))
if mibBuilder.loadTexts:ntwsTraplogTrapDateGroup.setStatus(_A)
ntwsTraplogVarGroup=ObjectGroup((1,3,6,1,4,1,45,6,1,4,13,2,2,5))
ntwsTraplogVarGroup.setObjects(*((_B,_S),(_B,_T),(_B,_U),(_B,_V),(_B,_W),(_B,_X),(_B,_Y),(_B,_Z),(_B,_a),(_B,_b)))
if mibBuilder.loadTexts:ntwsTraplogVarGroup.setStatus(_A)
ntwsTraplogCompliance=ModuleCompliance((1,3,6,1,4,1,45,6,1,4,13,2,1,1))
ntwsTraplogCompliance.setObjects(*((_B,_c),(_B,_d),(_B,_e),(_B,_f),(_B,_g)))
if mibBuilder.loadTexts:ntwsTraplogCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'NtwsTraplogTrapOccurrenceIndex':NtwsTraplogTrapOccurrenceIndex,'NtwsTraplogTrapOccurrenceIndexOrZero':NtwsTraplogTrapOccurrenceIndexOrZero,'ntwsTraplogMib':ntwsTraplogMib,'ntwsTraplogMibObjects':ntwsTraplogMibObjects,'ntwsTraplogGuideObjects':ntwsTraplogGuideObjects,_K:ntwsTraplogOldestTrapIndex,_L:ntwsTraplogNewestTrapIndex,_M:ntwsTraplogNewestTrapTime,_N:ntwsTraplogNewestTrapDateAndTime,'ntwsTraplogTrapTable':ntwsTraplogTrapTable,'ntwsTraplogTrapEntry':ntwsTraplogTrapEntry,_H:ntwsTraplogTrapIndex,_O:ntwsTraplogTrapTime,_R:ntwsTraplogTrapDateAndTime,_P:ntwsTraplogTrapNotificationID,_Q:ntwsTraplogTrapNumVars,'ntwsTraplogVarTable':ntwsTraplogVarTable,'ntwsTraplogVarEntry':ntwsTraplogVarEntry,_I:ntwsTraplogVarTrapIndex,_J:ntwsTraplogVarIndex,_S:ntwsTraplogVarID,_T:ntwsTraplogVarValueType,_U:ntwsTraplogVarCounter32Val,_V:ntwsTraplogVarUnsigned32Val,_W:ntwsTraplogVarTimeTicksVal,_X:ntwsTraplogVarInteger32Val,_Y:ntwsTraplogVarOctetStringVal,_Z:ntwsTraplogVarIpAddressVal,_a:ntwsTraplogVarOidVal,_b:ntwsTraplogVarCounter64Val,'ntwsTraplogConformance':ntwsTraplogConformance,'ntwsTraplogCompliances':ntwsTraplogCompliances,'ntwsTraplogCompliance':ntwsTraplogCompliance,'ntwsTraplogGroups':ntwsTraplogGroups,_c:ntwsTraplogGuideGroup,_f:ntwsTraplogGuideDateGroup,_d:ntwsTraplogTrapGroup,_g:ntwsTraplogTrapDateGroup,_e:ntwsTraplogVarGroup})