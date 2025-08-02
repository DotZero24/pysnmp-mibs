_V='hpnicfTRNGGroup'
_U='hpnicfTimerangePeriodicRowStatus'
_T='hpnicfTimerangePeriodicEndTime'
_S='hpnicfTimerangePeriodicStartTime'
_R='hpnicfTrngPeriodicDayOfWeek'
_Q='hpnicfTimerangeAbsolueRowStatus'
_P='hpnicfTimerangeAbsoluteEndTime'
_O='hpnicfTimerangeAbsoluteStartTime'
_N='hpnicfTrngCreateRowStatus'
_M='hpnicfTrngValidFlag'
_L='hpnicfTrngName'
_K='hpnicfTrngPeriodicSubIndex'
_J='hpnicfTrngPeriodicNameIndex'
_I='hpnicfTrngAbsoluteSubIndex'
_H='hpnicfTrngAbsoluteNameIndex'
_G='hpnicfTrngIndex'
_F='OctetString'
_E='not-accessible'
_D='Integer32'
_C='read-create'
_B='HPN-ICF-TRNG-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_F,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
hpnicfRhw,=mibBuilder.importSymbols('HPN-ICF-OID-MIB','hpnicfRhw')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DateAndTime,DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime','DisplayString','PhysAddress','RowStatus','TextualConvention','TruthValue')
hpnicfTRNG=ModuleIdentity((1,3,6,1,4,1,11,2,14,11,15,8,13))
if mibBuilder.loadTexts:hpnicfTRNG.setRevisions(('2003-04-11 00:00',))
_HpnicfTRNGMibObjects_ObjectIdentity=ObjectIdentity
hpnicfTRNGMibObjects=_HpnicfTRNGMibObjects_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,8,13,1))
_HpnicfTrngCreateTimerangeTable_Object=MibTable
hpnicfTrngCreateTimerangeTable=_HpnicfTrngCreateTimerangeTable_Object((1,3,6,1,4,1,11,2,14,11,15,8,13,1,1))
if mibBuilder.loadTexts:hpnicfTrngCreateTimerangeTable.setStatus(_A)
_HpnicfTrngCreateTimerangeEntry_Object=MibTableRow
hpnicfTrngCreateTimerangeEntry=_HpnicfTrngCreateTimerangeEntry_Object((1,3,6,1,4,1,11,2,14,11,15,8,13,1,1,1))
hpnicfTrngCreateTimerangeEntry.setIndexNames((0,_B,_G))
if mibBuilder.loadTexts:hpnicfTrngCreateTimerangeEntry.setStatus(_A)
class _HpnicfTrngIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,256))
_HpnicfTrngIndex_Type.__name__=_D
_HpnicfTrngIndex_Object=MibTableColumn
hpnicfTrngIndex=_HpnicfTrngIndex_Object((1,3,6,1,4,1,11,2,14,11,15,8,13,1,1,1,1),_HpnicfTrngIndex_Type())
hpnicfTrngIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:hpnicfTrngIndex.setStatus(_A)
class _HpnicfTrngName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_HpnicfTrngName_Type.__name__=_F
_HpnicfTrngName_Object=MibTableColumn
hpnicfTrngName=_HpnicfTrngName_Object((1,3,6,1,4,1,11,2,14,11,15,8,13,1,1,1,2),_HpnicfTrngName_Type())
hpnicfTrngName.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfTrngName.setStatus(_A)
_HpnicfTrngValidFlag_Type=TruthValue
_HpnicfTrngValidFlag_Object=MibTableColumn
hpnicfTrngValidFlag=_HpnicfTrngValidFlag_Object((1,3,6,1,4,1,11,2,14,11,15,8,13,1,1,1,3),_HpnicfTrngValidFlag_Type())
hpnicfTrngValidFlag.setMaxAccess('read-only')
if mibBuilder.loadTexts:hpnicfTrngValidFlag.setStatus(_A)
_HpnicfTrngCreateRowStatus_Type=RowStatus
_HpnicfTrngCreateRowStatus_Object=MibTableColumn
hpnicfTrngCreateRowStatus=_HpnicfTrngCreateRowStatus_Object((1,3,6,1,4,1,11,2,14,11,15,8,13,1,1,1,4),_HpnicfTrngCreateRowStatus_Type())
hpnicfTrngCreateRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfTrngCreateRowStatus.setStatus(_A)
_HpnicfTrngAbsoluteTable_Object=MibTable
hpnicfTrngAbsoluteTable=_HpnicfTrngAbsoluteTable_Object((1,3,6,1,4,1,11,2,14,11,15,8,13,1,2))
if mibBuilder.loadTexts:hpnicfTrngAbsoluteTable.setStatus(_A)
_HpnicfTrngAbsoluteEntry_Object=MibTableRow
hpnicfTrngAbsoluteEntry=_HpnicfTrngAbsoluteEntry_Object((1,3,6,1,4,1,11,2,14,11,15,8,13,1,2,1))
hpnicfTrngAbsoluteEntry.setIndexNames((0,_B,_H),(0,_B,_I))
if mibBuilder.loadTexts:hpnicfTrngAbsoluteEntry.setStatus(_A)
class _HpnicfTrngAbsoluteNameIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,256))
_HpnicfTrngAbsoluteNameIndex_Type.__name__=_D
_HpnicfTrngAbsoluteNameIndex_Object=MibTableColumn
hpnicfTrngAbsoluteNameIndex=_HpnicfTrngAbsoluteNameIndex_Object((1,3,6,1,4,1,11,2,14,11,15,8,13,1,2,1,1),_HpnicfTrngAbsoluteNameIndex_Type())
hpnicfTrngAbsoluteNameIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:hpnicfTrngAbsoluteNameIndex.setStatus(_A)
class _HpnicfTrngAbsoluteSubIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,12))
_HpnicfTrngAbsoluteSubIndex_Type.__name__=_D
_HpnicfTrngAbsoluteSubIndex_Object=MibTableColumn
hpnicfTrngAbsoluteSubIndex=_HpnicfTrngAbsoluteSubIndex_Object((1,3,6,1,4,1,11,2,14,11,15,8,13,1,2,1,2),_HpnicfTrngAbsoluteSubIndex_Type())
hpnicfTrngAbsoluteSubIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:hpnicfTrngAbsoluteSubIndex.setStatus(_A)
_HpnicfTimerangeAbsoluteStartTime_Type=DateAndTime
_HpnicfTimerangeAbsoluteStartTime_Object=MibTableColumn
hpnicfTimerangeAbsoluteStartTime=_HpnicfTimerangeAbsoluteStartTime_Object((1,3,6,1,4,1,11,2,14,11,15,8,13,1,2,1,3),_HpnicfTimerangeAbsoluteStartTime_Type())
hpnicfTimerangeAbsoluteStartTime.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfTimerangeAbsoluteStartTime.setStatus(_A)
_HpnicfTimerangeAbsoluteEndTime_Type=DateAndTime
_HpnicfTimerangeAbsoluteEndTime_Object=MibTableColumn
hpnicfTimerangeAbsoluteEndTime=_HpnicfTimerangeAbsoluteEndTime_Object((1,3,6,1,4,1,11,2,14,11,15,8,13,1,2,1,4),_HpnicfTimerangeAbsoluteEndTime_Type())
hpnicfTimerangeAbsoluteEndTime.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfTimerangeAbsoluteEndTime.setStatus(_A)
_HpnicfTimerangeAbsolueRowStatus_Type=RowStatus
_HpnicfTimerangeAbsolueRowStatus_Object=MibTableColumn
hpnicfTimerangeAbsolueRowStatus=_HpnicfTimerangeAbsolueRowStatus_Object((1,3,6,1,4,1,11,2,14,11,15,8,13,1,2,1,5),_HpnicfTimerangeAbsolueRowStatus_Type())
hpnicfTimerangeAbsolueRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfTimerangeAbsolueRowStatus.setStatus(_A)
_HpnicfTrngPeriodicTable_Object=MibTable
hpnicfTrngPeriodicTable=_HpnicfTrngPeriodicTable_Object((1,3,6,1,4,1,11,2,14,11,15,8,13,1,3))
if mibBuilder.loadTexts:hpnicfTrngPeriodicTable.setStatus(_A)
_HpnicfTrngPeriodicEntry_Object=MibTableRow
hpnicfTrngPeriodicEntry=_HpnicfTrngPeriodicEntry_Object((1,3,6,1,4,1,11,2,14,11,15,8,13,1,3,1))
hpnicfTrngPeriodicEntry.setIndexNames((0,_B,_J),(0,_B,_K))
if mibBuilder.loadTexts:hpnicfTrngPeriodicEntry.setStatus(_A)
class _HpnicfTrngPeriodicNameIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,256))
_HpnicfTrngPeriodicNameIndex_Type.__name__=_D
_HpnicfTrngPeriodicNameIndex_Object=MibTableColumn
hpnicfTrngPeriodicNameIndex=_HpnicfTrngPeriodicNameIndex_Object((1,3,6,1,4,1,11,2,14,11,15,8,13,1,3,1,1),_HpnicfTrngPeriodicNameIndex_Type())
hpnicfTrngPeriodicNameIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:hpnicfTrngPeriodicNameIndex.setStatus(_A)
class _HpnicfTrngPeriodicSubIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,32))
_HpnicfTrngPeriodicSubIndex_Type.__name__=_D
_HpnicfTrngPeriodicSubIndex_Object=MibTableColumn
hpnicfTrngPeriodicSubIndex=_HpnicfTrngPeriodicSubIndex_Object((1,3,6,1,4,1,11,2,14,11,15,8,13,1,3,1,2),_HpnicfTrngPeriodicSubIndex_Type())
hpnicfTrngPeriodicSubIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:hpnicfTrngPeriodicSubIndex.setStatus(_A)
class _HpnicfTrngPeriodicDayOfWeek_Type(Bits):namedValues=NamedValues(*(('sunday',0),('monday',1),('tuesday',2),('wednesday',3),('thursday',4),('friday',5),('saturday',6)))
_HpnicfTrngPeriodicDayOfWeek_Type.__name__='Bits'
_HpnicfTrngPeriodicDayOfWeek_Object=MibTableColumn
hpnicfTrngPeriodicDayOfWeek=_HpnicfTrngPeriodicDayOfWeek_Object((1,3,6,1,4,1,11,2,14,11,15,8,13,1,3,1,3),_HpnicfTrngPeriodicDayOfWeek_Type())
hpnicfTrngPeriodicDayOfWeek.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfTrngPeriodicDayOfWeek.setStatus(_A)
_HpnicfTimerangePeriodicStartTime_Type=DateAndTime
_HpnicfTimerangePeriodicStartTime_Object=MibTableColumn
hpnicfTimerangePeriodicStartTime=_HpnicfTimerangePeriodicStartTime_Object((1,3,6,1,4,1,11,2,14,11,15,8,13,1,3,1,4),_HpnicfTimerangePeriodicStartTime_Type())
hpnicfTimerangePeriodicStartTime.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfTimerangePeriodicStartTime.setStatus(_A)
_HpnicfTimerangePeriodicEndTime_Type=DateAndTime
_HpnicfTimerangePeriodicEndTime_Object=MibTableColumn
hpnicfTimerangePeriodicEndTime=_HpnicfTimerangePeriodicEndTime_Object((1,3,6,1,4,1,11,2,14,11,15,8,13,1,3,1,5),_HpnicfTimerangePeriodicEndTime_Type())
hpnicfTimerangePeriodicEndTime.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfTimerangePeriodicEndTime.setStatus(_A)
_HpnicfTimerangePeriodicRowStatus_Type=RowStatus
_HpnicfTimerangePeriodicRowStatus_Object=MibTableColumn
hpnicfTimerangePeriodicRowStatus=_HpnicfTimerangePeriodicRowStatus_Object((1,3,6,1,4,1,11,2,14,11,15,8,13,1,3,1,6),_HpnicfTimerangePeriodicRowStatus_Type())
hpnicfTimerangePeriodicRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfTimerangePeriodicRowStatus.setStatus(_A)
_HpnicfTRNGMibConformance_ObjectIdentity=ObjectIdentity
hpnicfTRNGMibConformance=_HpnicfTRNGMibConformance_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,8,13,3))
_HpnicfTRNGMibCompliances_ObjectIdentity=ObjectIdentity
hpnicfTRNGMibCompliances=_HpnicfTRNGMibCompliances_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,8,13,3,1))
_HpnicfTRNGMibGroups_ObjectIdentity=ObjectIdentity
hpnicfTRNGMibGroups=_HpnicfTRNGMibGroups_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,8,13,3,2))
hpnicfTRNGGroup=ObjectGroup((1,3,6,1,4,1,11,2,14,11,15,8,13,3,2,1))
hpnicfTRNGGroup.setObjects(*((_B,_L),(_B,_M),(_B,_N),(_B,_O),(_B,_P),(_B,_Q),(_B,_R),(_B,_S),(_B,_T),(_B,_U)))
if mibBuilder.loadTexts:hpnicfTRNGGroup.setStatus(_A)
hpnicfTRNGMibCompliance=ModuleCompliance((1,3,6,1,4,1,11,2,14,11,15,8,13,3,1,1))
hpnicfTRNGMibCompliance.setObjects((_B,_V))
if mibBuilder.loadTexts:hpnicfTRNGMibCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'hpnicfTRNG':hpnicfTRNG,'hpnicfTRNGMibObjects':hpnicfTRNGMibObjects,'hpnicfTrngCreateTimerangeTable':hpnicfTrngCreateTimerangeTable,'hpnicfTrngCreateTimerangeEntry':hpnicfTrngCreateTimerangeEntry,_G:hpnicfTrngIndex,_L:hpnicfTrngName,_M:hpnicfTrngValidFlag,_N:hpnicfTrngCreateRowStatus,'hpnicfTrngAbsoluteTable':hpnicfTrngAbsoluteTable,'hpnicfTrngAbsoluteEntry':hpnicfTrngAbsoluteEntry,_H:hpnicfTrngAbsoluteNameIndex,_I:hpnicfTrngAbsoluteSubIndex,_O:hpnicfTimerangeAbsoluteStartTime,_P:hpnicfTimerangeAbsoluteEndTime,_Q:hpnicfTimerangeAbsolueRowStatus,'hpnicfTrngPeriodicTable':hpnicfTrngPeriodicTable,'hpnicfTrngPeriodicEntry':hpnicfTrngPeriodicEntry,_J:hpnicfTrngPeriodicNameIndex,_K:hpnicfTrngPeriodicSubIndex,_R:hpnicfTrngPeriodicDayOfWeek,_S:hpnicfTimerangePeriodicStartTime,_T:hpnicfTimerangePeriodicEndTime,_U:hpnicfTimerangePeriodicRowStatus,'hpnicfTRNGMibConformance':hpnicfTRNGMibConformance,'hpnicfTRNGMibCompliances':hpnicfTRNGMibCompliances,'hpnicfTRNGMibCompliance':hpnicfTRNGMibCompliance,'hpnicfTRNGMibGroups':hpnicfTRNGMibGroups,_V:hpnicfTRNGGroup})