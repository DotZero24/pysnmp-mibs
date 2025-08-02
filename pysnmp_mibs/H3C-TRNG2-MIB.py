_K='h3cTrangePeriodicSubIndex'
_J='h3cTrangePeriodicNameIndex'
_I='h3cTrangeAbsoluteSubIndex'
_H='h3cTrangeAbsoluteNameIndex'
_G='h3cTrangeIndex'
_F='OctetString'
_E='not-accessible'
_D='H3C-TRNG2-MIB'
_C='Integer32'
_B='read-create'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_F,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
h3cCommon,=mibBuilder.importSymbols('HUAWEI-3COM-OID-MIB','h3cCommon')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DateAndTime,DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime','DisplayString','PhysAddress','RowStatus','TextualConvention','TruthValue')
h3cTRNG2=ModuleIdentity((1,3,6,1,4,1,2011,10,2,121))
if mibBuilder.loadTexts:h3cTRNG2.setRevisions(('2013-03-08 00:00','2012-05-14 00:00'))
_H3cTRNG2MibObjects_ObjectIdentity=ObjectIdentity
h3cTRNG2MibObjects=_H3cTRNG2MibObjects_ObjectIdentity((1,3,6,1,4,1,2011,10,2,121,1))
_H3cTrangeCreateTimerangeTable_Object=MibTable
h3cTrangeCreateTimerangeTable=_H3cTrangeCreateTimerangeTable_Object((1,3,6,1,4,1,2011,10,2,121,1,1))
if mibBuilder.loadTexts:h3cTrangeCreateTimerangeTable.setStatus(_A)
_H3cTrangeCreateTimerangeEntry_Object=MibTableRow
h3cTrangeCreateTimerangeEntry=_H3cTrangeCreateTimerangeEntry_Object((1,3,6,1,4,1,2011,10,2,121,1,1,1))
h3cTrangeCreateTimerangeEntry.setIndexNames((0,_D,_G))
if mibBuilder.loadTexts:h3cTrangeCreateTimerangeEntry.setStatus(_A)
class _H3cTrangeIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_H3cTrangeIndex_Type.__name__=_C
_H3cTrangeIndex_Object=MibTableColumn
h3cTrangeIndex=_H3cTrangeIndex_Object((1,3,6,1,4,1,2011,10,2,121,1,1,1,1),_H3cTrangeIndex_Type())
h3cTrangeIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:h3cTrangeIndex.setStatus(_A)
class _H3cTrangeName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_H3cTrangeName_Type.__name__=_F
_H3cTrangeName_Object=MibTableColumn
h3cTrangeName=_H3cTrangeName_Object((1,3,6,1,4,1,2011,10,2,121,1,1,1,2),_H3cTrangeName_Type())
h3cTrangeName.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cTrangeName.setStatus(_A)
_H3cTrangeValidFlag_Type=TruthValue
_H3cTrangeValidFlag_Object=MibTableColumn
h3cTrangeValidFlag=_H3cTrangeValidFlag_Object((1,3,6,1,4,1,2011,10,2,121,1,1,1,3),_H3cTrangeValidFlag_Type())
h3cTrangeValidFlag.setMaxAccess('read-only')
if mibBuilder.loadTexts:h3cTrangeValidFlag.setStatus(_A)
_H3cTrangeCreateRowStatus_Type=RowStatus
_H3cTrangeCreateRowStatus_Object=MibTableColumn
h3cTrangeCreateRowStatus=_H3cTrangeCreateRowStatus_Object((1,3,6,1,4,1,2011,10,2,121,1,1,1,4),_H3cTrangeCreateRowStatus_Type())
h3cTrangeCreateRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cTrangeCreateRowStatus.setStatus(_A)
_H3cTrangeAbsoluteTable_Object=MibTable
h3cTrangeAbsoluteTable=_H3cTrangeAbsoluteTable_Object((1,3,6,1,4,1,2011,10,2,121,1,2))
if mibBuilder.loadTexts:h3cTrangeAbsoluteTable.setStatus(_A)
_H3cTrangeAbsoluteEntry_Object=MibTableRow
h3cTrangeAbsoluteEntry=_H3cTrangeAbsoluteEntry_Object((1,3,6,1,4,1,2011,10,2,121,1,2,1))
h3cTrangeAbsoluteEntry.setIndexNames((0,_D,_H),(0,_D,_I))
if mibBuilder.loadTexts:h3cTrangeAbsoluteEntry.setStatus(_A)
class _H3cTrangeAbsoluteNameIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_H3cTrangeAbsoluteNameIndex_Type.__name__=_C
_H3cTrangeAbsoluteNameIndex_Object=MibTableColumn
h3cTrangeAbsoluteNameIndex=_H3cTrangeAbsoluteNameIndex_Object((1,3,6,1,4,1,2011,10,2,121,1,2,1,1),_H3cTrangeAbsoluteNameIndex_Type())
h3cTrangeAbsoluteNameIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:h3cTrangeAbsoluteNameIndex.setStatus(_A)
class _H3cTrangeAbsoluteSubIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,12))
_H3cTrangeAbsoluteSubIndex_Type.__name__=_C
_H3cTrangeAbsoluteSubIndex_Object=MibTableColumn
h3cTrangeAbsoluteSubIndex=_H3cTrangeAbsoluteSubIndex_Object((1,3,6,1,4,1,2011,10,2,121,1,2,1,2),_H3cTrangeAbsoluteSubIndex_Type())
h3cTrangeAbsoluteSubIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:h3cTrangeAbsoluteSubIndex.setStatus(_A)
_H3cTrangeAbsoluteStartTime_Type=DateAndTime
_H3cTrangeAbsoluteStartTime_Object=MibTableColumn
h3cTrangeAbsoluteStartTime=_H3cTrangeAbsoluteStartTime_Object((1,3,6,1,4,1,2011,10,2,121,1,2,1,3),_H3cTrangeAbsoluteStartTime_Type())
h3cTrangeAbsoluteStartTime.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cTrangeAbsoluteStartTime.setStatus(_A)
_H3cTrangeAbsoluteEndTime_Type=DateAndTime
_H3cTrangeAbsoluteEndTime_Object=MibTableColumn
h3cTrangeAbsoluteEndTime=_H3cTrangeAbsoluteEndTime_Object((1,3,6,1,4,1,2011,10,2,121,1,2,1,4),_H3cTrangeAbsoluteEndTime_Type())
h3cTrangeAbsoluteEndTime.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cTrangeAbsoluteEndTime.setStatus(_A)
_H3cTrangeAbsolueRowStatus_Type=RowStatus
_H3cTrangeAbsolueRowStatus_Object=MibTableColumn
h3cTrangeAbsolueRowStatus=_H3cTrangeAbsolueRowStatus_Object((1,3,6,1,4,1,2011,10,2,121,1,2,1,5),_H3cTrangeAbsolueRowStatus_Type())
h3cTrangeAbsolueRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cTrangeAbsolueRowStatus.setStatus(_A)
_H3cTrangePeriodicTable_Object=MibTable
h3cTrangePeriodicTable=_H3cTrangePeriodicTable_Object((1,3,6,1,4,1,2011,10,2,121,1,3))
if mibBuilder.loadTexts:h3cTrangePeriodicTable.setStatus(_A)
_H3cTrangePeriodicEntry_Object=MibTableRow
h3cTrangePeriodicEntry=_H3cTrangePeriodicEntry_Object((1,3,6,1,4,1,2011,10,2,121,1,3,1))
h3cTrangePeriodicEntry.setIndexNames((0,_D,_J),(0,_D,_K))
if mibBuilder.loadTexts:h3cTrangePeriodicEntry.setStatus(_A)
class _H3cTrangePeriodicNameIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_H3cTrangePeriodicNameIndex_Type.__name__=_C
_H3cTrangePeriodicNameIndex_Object=MibTableColumn
h3cTrangePeriodicNameIndex=_H3cTrangePeriodicNameIndex_Object((1,3,6,1,4,1,2011,10,2,121,1,3,1,1),_H3cTrangePeriodicNameIndex_Type())
h3cTrangePeriodicNameIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:h3cTrangePeriodicNameIndex.setStatus(_A)
class _H3cTrangePeriodicSubIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,32))
_H3cTrangePeriodicSubIndex_Type.__name__=_C
_H3cTrangePeriodicSubIndex_Object=MibTableColumn
h3cTrangePeriodicSubIndex=_H3cTrangePeriodicSubIndex_Object((1,3,6,1,4,1,2011,10,2,121,1,3,1,2),_H3cTrangePeriodicSubIndex_Type())
h3cTrangePeriodicSubIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:h3cTrangePeriodicSubIndex.setStatus(_A)
class _H3cTrangePeriodicDayOfWeek_Type(Bits):namedValues=NamedValues(*(('sunday',0),('monday',1),('tuesday',2),('wednesday',3),('thursday',4),('friday',5),('saturday',6)))
_H3cTrangePeriodicDayOfWeek_Type.__name__='Bits'
_H3cTrangePeriodicDayOfWeek_Object=MibTableColumn
h3cTrangePeriodicDayOfWeek=_H3cTrangePeriodicDayOfWeek_Object((1,3,6,1,4,1,2011,10,2,121,1,3,1,3),_H3cTrangePeriodicDayOfWeek_Type())
h3cTrangePeriodicDayOfWeek.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cTrangePeriodicDayOfWeek.setStatus(_A)
_H3cTrangePeriodicStartTime_Type=DateAndTime
_H3cTrangePeriodicStartTime_Object=MibTableColumn
h3cTrangePeriodicStartTime=_H3cTrangePeriodicStartTime_Object((1,3,6,1,4,1,2011,10,2,121,1,3,1,4),_H3cTrangePeriodicStartTime_Type())
h3cTrangePeriodicStartTime.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cTrangePeriodicStartTime.setStatus(_A)
_H3cTrangePeriodicEndTime_Type=DateAndTime
_H3cTrangePeriodicEndTime_Object=MibTableColumn
h3cTrangePeriodicEndTime=_H3cTrangePeriodicEndTime_Object((1,3,6,1,4,1,2011,10,2,121,1,3,1,5),_H3cTrangePeriodicEndTime_Type())
h3cTrangePeriodicEndTime.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cTrangePeriodicEndTime.setStatus(_A)
_H3cTrangePeriodicRowStatus_Type=RowStatus
_H3cTrangePeriodicRowStatus_Object=MibTableColumn
h3cTrangePeriodicRowStatus=_H3cTrangePeriodicRowStatus_Object((1,3,6,1,4,1,2011,10,2,121,1,3,1,6),_H3cTrangePeriodicRowStatus_Type())
h3cTrangePeriodicRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cTrangePeriodicRowStatus.setStatus(_A)
mibBuilder.exportSymbols(_D,**{'h3cTRNG2':h3cTRNG2,'h3cTRNG2MibObjects':h3cTRNG2MibObjects,'h3cTrangeCreateTimerangeTable':h3cTrangeCreateTimerangeTable,'h3cTrangeCreateTimerangeEntry':h3cTrangeCreateTimerangeEntry,_G:h3cTrangeIndex,'h3cTrangeName':h3cTrangeName,'h3cTrangeValidFlag':h3cTrangeValidFlag,'h3cTrangeCreateRowStatus':h3cTrangeCreateRowStatus,'h3cTrangeAbsoluteTable':h3cTrangeAbsoluteTable,'h3cTrangeAbsoluteEntry':h3cTrangeAbsoluteEntry,_H:h3cTrangeAbsoluteNameIndex,_I:h3cTrangeAbsoluteSubIndex,'h3cTrangeAbsoluteStartTime':h3cTrangeAbsoluteStartTime,'h3cTrangeAbsoluteEndTime':h3cTrangeAbsoluteEndTime,'h3cTrangeAbsolueRowStatus':h3cTrangeAbsolueRowStatus,'h3cTrangePeriodicTable':h3cTrangePeriodicTable,'h3cTrangePeriodicEntry':h3cTrangePeriodicEntry,_J:h3cTrangePeriodicNameIndex,_K:h3cTrangePeriodicSubIndex,'h3cTrangePeriodicDayOfWeek':h3cTrangePeriodicDayOfWeek,'h3cTrangePeriodicStartTime':h3cTrangePeriodicStartTime,'h3cTrangePeriodicEndTime':h3cTrangePeriodicEndTime,'h3cTrangePeriodicRowStatus':h3cTrangePeriodicRowStatus})