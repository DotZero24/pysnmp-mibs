_V='hwTRNGGroup'
_U='hwTimerangePeriodicRowStatus'
_T='hwTimerangePeriodicEndTime'
_S='hwTimerangePeriodicStartTime'
_R='hwTrngPeriodicDayOfWeek'
_Q='hwTimerangeAbsolueRowStatus'
_P='hwTimerangeAbsoluteEndTime'
_O='hwTimerangeAbsoluteStartTime'
_N='hwTrngCreateRowStatus'
_M='hwTrngValidFlag'
_L='hwTrngName'
_K='hwTrngPeriodicSubIndex'
_J='hwTrngPeriodicNameIndex'
_I='hwTrngAbsoluteSubIndex'
_H='hwTrngAbsoluteNameIndex'
_G='hwTrngIndex'
_F='OctetString'
_E='not-accessible'
_D='Integer32'
_C='read-create'
_B='A3COM-HUAWEI-TRNG-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_F,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
huaweiDatacomm,=mibBuilder.importSymbols('A3COM-HUAWEI-OID-MIB','huaweiDatacomm')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DateAndTime,DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime','DisplayString','PhysAddress','RowStatus','TextualConvention','TruthValue')
hwTRNG=ModuleIdentity((1,3,6,1,4,1,43,45,1,5,25,13))
if mibBuilder.loadTexts:hwTRNG.setRevisions(('2003-04-11 00:00',))
_HwTRNGMibObjects_ObjectIdentity=ObjectIdentity
hwTRNGMibObjects=_HwTRNGMibObjects_ObjectIdentity((1,3,6,1,4,1,43,45,1,5,25,13,1))
_HwTrngCreateTimerangeTable_Object=MibTable
hwTrngCreateTimerangeTable=_HwTrngCreateTimerangeTable_Object((1,3,6,1,4,1,43,45,1,5,25,13,1,1))
if mibBuilder.loadTexts:hwTrngCreateTimerangeTable.setStatus(_A)
_HwTrngCreateTimerangeEntry_Object=MibTableRow
hwTrngCreateTimerangeEntry=_HwTrngCreateTimerangeEntry_Object((1,3,6,1,4,1,43,45,1,5,25,13,1,1,1))
hwTrngCreateTimerangeEntry.setIndexNames((0,_B,_G))
if mibBuilder.loadTexts:hwTrngCreateTimerangeEntry.setStatus(_A)
class _HwTrngIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,256))
_HwTrngIndex_Type.__name__=_D
_HwTrngIndex_Object=MibTableColumn
hwTrngIndex=_HwTrngIndex_Object((1,3,6,1,4,1,43,45,1,5,25,13,1,1,1,1),_HwTrngIndex_Type())
hwTrngIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:hwTrngIndex.setStatus(_A)
class _HwTrngName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_HwTrngName_Type.__name__=_F
_HwTrngName_Object=MibTableColumn
hwTrngName=_HwTrngName_Object((1,3,6,1,4,1,43,45,1,5,25,13,1,1,1,2),_HwTrngName_Type())
hwTrngName.setMaxAccess(_C)
if mibBuilder.loadTexts:hwTrngName.setStatus(_A)
_HwTrngValidFlag_Type=TruthValue
_HwTrngValidFlag_Object=MibTableColumn
hwTrngValidFlag=_HwTrngValidFlag_Object((1,3,6,1,4,1,43,45,1,5,25,13,1,1,1,3),_HwTrngValidFlag_Type())
hwTrngValidFlag.setMaxAccess('read-only')
if mibBuilder.loadTexts:hwTrngValidFlag.setStatus(_A)
_HwTrngCreateRowStatus_Type=RowStatus
_HwTrngCreateRowStatus_Object=MibTableColumn
hwTrngCreateRowStatus=_HwTrngCreateRowStatus_Object((1,3,6,1,4,1,43,45,1,5,25,13,1,1,1,4),_HwTrngCreateRowStatus_Type())
hwTrngCreateRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:hwTrngCreateRowStatus.setStatus(_A)
_HwTrngAbsoluteTable_Object=MibTable
hwTrngAbsoluteTable=_HwTrngAbsoluteTable_Object((1,3,6,1,4,1,43,45,1,5,25,13,1,2))
if mibBuilder.loadTexts:hwTrngAbsoluteTable.setStatus(_A)
_HwTrngAbsoluteEntry_Object=MibTableRow
hwTrngAbsoluteEntry=_HwTrngAbsoluteEntry_Object((1,3,6,1,4,1,43,45,1,5,25,13,1,2,1))
hwTrngAbsoluteEntry.setIndexNames((0,_B,_H),(0,_B,_I))
if mibBuilder.loadTexts:hwTrngAbsoluteEntry.setStatus(_A)
class _HwTrngAbsoluteNameIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,256))
_HwTrngAbsoluteNameIndex_Type.__name__=_D
_HwTrngAbsoluteNameIndex_Object=MibTableColumn
hwTrngAbsoluteNameIndex=_HwTrngAbsoluteNameIndex_Object((1,3,6,1,4,1,43,45,1,5,25,13,1,2,1,1),_HwTrngAbsoluteNameIndex_Type())
hwTrngAbsoluteNameIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:hwTrngAbsoluteNameIndex.setStatus(_A)
class _HwTrngAbsoluteSubIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,12))
_HwTrngAbsoluteSubIndex_Type.__name__=_D
_HwTrngAbsoluteSubIndex_Object=MibTableColumn
hwTrngAbsoluteSubIndex=_HwTrngAbsoluteSubIndex_Object((1,3,6,1,4,1,43,45,1,5,25,13,1,2,1,2),_HwTrngAbsoluteSubIndex_Type())
hwTrngAbsoluteSubIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:hwTrngAbsoluteSubIndex.setStatus(_A)
_HwTimerangeAbsoluteStartTime_Type=DateAndTime
_HwTimerangeAbsoluteStartTime_Object=MibTableColumn
hwTimerangeAbsoluteStartTime=_HwTimerangeAbsoluteStartTime_Object((1,3,6,1,4,1,43,45,1,5,25,13,1,2,1,3),_HwTimerangeAbsoluteStartTime_Type())
hwTimerangeAbsoluteStartTime.setMaxAccess(_C)
if mibBuilder.loadTexts:hwTimerangeAbsoluteStartTime.setStatus(_A)
_HwTimerangeAbsoluteEndTime_Type=DateAndTime
_HwTimerangeAbsoluteEndTime_Object=MibTableColumn
hwTimerangeAbsoluteEndTime=_HwTimerangeAbsoluteEndTime_Object((1,3,6,1,4,1,43,45,1,5,25,13,1,2,1,4),_HwTimerangeAbsoluteEndTime_Type())
hwTimerangeAbsoluteEndTime.setMaxAccess(_C)
if mibBuilder.loadTexts:hwTimerangeAbsoluteEndTime.setStatus(_A)
_HwTimerangeAbsolueRowStatus_Type=RowStatus
_HwTimerangeAbsolueRowStatus_Object=MibTableColumn
hwTimerangeAbsolueRowStatus=_HwTimerangeAbsolueRowStatus_Object((1,3,6,1,4,1,43,45,1,5,25,13,1,2,1,5),_HwTimerangeAbsolueRowStatus_Type())
hwTimerangeAbsolueRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:hwTimerangeAbsolueRowStatus.setStatus(_A)
_HwTrngPeriodicTable_Object=MibTable
hwTrngPeriodicTable=_HwTrngPeriodicTable_Object((1,3,6,1,4,1,43,45,1,5,25,13,1,3))
if mibBuilder.loadTexts:hwTrngPeriodicTable.setStatus(_A)
_HwTrngPeriodicEntry_Object=MibTableRow
hwTrngPeriodicEntry=_HwTrngPeriodicEntry_Object((1,3,6,1,4,1,43,45,1,5,25,13,1,3,1))
hwTrngPeriodicEntry.setIndexNames((0,_B,_J),(0,_B,_K))
if mibBuilder.loadTexts:hwTrngPeriodicEntry.setStatus(_A)
class _HwTrngPeriodicNameIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,256))
_HwTrngPeriodicNameIndex_Type.__name__=_D
_HwTrngPeriodicNameIndex_Object=MibTableColumn
hwTrngPeriodicNameIndex=_HwTrngPeriodicNameIndex_Object((1,3,6,1,4,1,43,45,1,5,25,13,1,3,1,1),_HwTrngPeriodicNameIndex_Type())
hwTrngPeriodicNameIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:hwTrngPeriodicNameIndex.setStatus(_A)
class _HwTrngPeriodicSubIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,32))
_HwTrngPeriodicSubIndex_Type.__name__=_D
_HwTrngPeriodicSubIndex_Object=MibTableColumn
hwTrngPeriodicSubIndex=_HwTrngPeriodicSubIndex_Object((1,3,6,1,4,1,43,45,1,5,25,13,1,3,1,2),_HwTrngPeriodicSubIndex_Type())
hwTrngPeriodicSubIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:hwTrngPeriodicSubIndex.setStatus(_A)
class _HwTrngPeriodicDayOfWeek_Type(Bits):namedValues=NamedValues(*(('sunday',0),('monday',1),('tuesday',2),('wednesday',3),('thursday',4),('friday',5),('saturday',6)))
_HwTrngPeriodicDayOfWeek_Type.__name__='Bits'
_HwTrngPeriodicDayOfWeek_Object=MibTableColumn
hwTrngPeriodicDayOfWeek=_HwTrngPeriodicDayOfWeek_Object((1,3,6,1,4,1,43,45,1,5,25,13,1,3,1,3),_HwTrngPeriodicDayOfWeek_Type())
hwTrngPeriodicDayOfWeek.setMaxAccess(_C)
if mibBuilder.loadTexts:hwTrngPeriodicDayOfWeek.setStatus(_A)
_HwTimerangePeriodicStartTime_Type=DateAndTime
_HwTimerangePeriodicStartTime_Object=MibTableColumn
hwTimerangePeriodicStartTime=_HwTimerangePeriodicStartTime_Object((1,3,6,1,4,1,43,45,1,5,25,13,1,3,1,4),_HwTimerangePeriodicStartTime_Type())
hwTimerangePeriodicStartTime.setMaxAccess(_C)
if mibBuilder.loadTexts:hwTimerangePeriodicStartTime.setStatus(_A)
_HwTimerangePeriodicEndTime_Type=DateAndTime
_HwTimerangePeriodicEndTime_Object=MibTableColumn
hwTimerangePeriodicEndTime=_HwTimerangePeriodicEndTime_Object((1,3,6,1,4,1,43,45,1,5,25,13,1,3,1,5),_HwTimerangePeriodicEndTime_Type())
hwTimerangePeriodicEndTime.setMaxAccess(_C)
if mibBuilder.loadTexts:hwTimerangePeriodicEndTime.setStatus(_A)
_HwTimerangePeriodicRowStatus_Type=RowStatus
_HwTimerangePeriodicRowStatus_Object=MibTableColumn
hwTimerangePeriodicRowStatus=_HwTimerangePeriodicRowStatus_Object((1,3,6,1,4,1,43,45,1,5,25,13,1,3,1,6),_HwTimerangePeriodicRowStatus_Type())
hwTimerangePeriodicRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:hwTimerangePeriodicRowStatus.setStatus(_A)
_HwTRNGMibConformance_ObjectIdentity=ObjectIdentity
hwTRNGMibConformance=_HwTRNGMibConformance_ObjectIdentity((1,3,6,1,4,1,43,45,1,5,25,13,3))
_HwTRNGMibCompliances_ObjectIdentity=ObjectIdentity
hwTRNGMibCompliances=_HwTRNGMibCompliances_ObjectIdentity((1,3,6,1,4,1,43,45,1,5,25,13,3,1))
_HwTRNGMibGroups_ObjectIdentity=ObjectIdentity
hwTRNGMibGroups=_HwTRNGMibGroups_ObjectIdentity((1,3,6,1,4,1,43,45,1,5,25,13,3,2))
hwTRNGGroup=ObjectGroup((1,3,6,1,4,1,43,45,1,5,25,13,3,2,1))
hwTRNGGroup.setObjects(*((_B,_L),(_B,_M),(_B,_N),(_B,_O),(_B,_P),(_B,_Q),(_B,_R),(_B,_S),(_B,_T),(_B,_U)))
if mibBuilder.loadTexts:hwTRNGGroup.setStatus(_A)
hwTRNGMibCompliance=ModuleCompliance((1,3,6,1,4,1,43,45,1,5,25,13,3,1,1))
hwTRNGMibCompliance.setObjects((_B,_V))
if mibBuilder.loadTexts:hwTRNGMibCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'hwTRNG':hwTRNG,'hwTRNGMibObjects':hwTRNGMibObjects,'hwTrngCreateTimerangeTable':hwTrngCreateTimerangeTable,'hwTrngCreateTimerangeEntry':hwTrngCreateTimerangeEntry,_G:hwTrngIndex,_L:hwTrngName,_M:hwTrngValidFlag,_N:hwTrngCreateRowStatus,'hwTrngAbsoluteTable':hwTrngAbsoluteTable,'hwTrngAbsoluteEntry':hwTrngAbsoluteEntry,_H:hwTrngAbsoluteNameIndex,_I:hwTrngAbsoluteSubIndex,_O:hwTimerangeAbsoluteStartTime,_P:hwTimerangeAbsoluteEndTime,_Q:hwTimerangeAbsolueRowStatus,'hwTrngPeriodicTable':hwTrngPeriodicTable,'hwTrngPeriodicEntry':hwTrngPeriodicEntry,_J:hwTrngPeriodicNameIndex,_K:hwTrngPeriodicSubIndex,_R:hwTrngPeriodicDayOfWeek,_S:hwTimerangePeriodicStartTime,_T:hwTimerangePeriodicEndTime,_U:hwTimerangePeriodicRowStatus,'hwTRNGMibConformance':hwTRNGMibConformance,'hwTRNGMibCompliances':hwTRNGMibCompliances,'hwTRNGMibCompliance':hwTRNGMibCompliance,'hwTRNGMibGroups':hwTRNGMibGroups,_V:hwTRNGGroup})