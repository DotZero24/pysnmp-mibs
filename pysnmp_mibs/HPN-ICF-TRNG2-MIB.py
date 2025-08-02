_K='hpnicfTrangePeriodicSubIndex'
_J='hpnicfTrangePeriodicNameIndex'
_I='hpnicfTrangeAbsoluteSubIndex'
_H='hpnicfTrangeAbsoluteNameIndex'
_G='hpnicfTrangeIndex'
_F='OctetString'
_E='not-accessible'
_D='HPN-ICF-TRNG2-MIB'
_C='Integer32'
_B='read-create'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_F,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
hpnicfCommon,=mibBuilder.importSymbols('HPN-ICF-OID-MIB','hpnicfCommon')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DateAndTime,DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime','DisplayString','PhysAddress','RowStatus','TextualConvention','TruthValue')
hpnicfTRNG2=ModuleIdentity((1,3,6,1,4,1,11,2,14,11,15,2,121))
if mibBuilder.loadTexts:hpnicfTRNG2.setRevisions(('2013-03-08 00:00','2012-05-14 00:00'))
_HpnicfTRNG2MibObjects_ObjectIdentity=ObjectIdentity
hpnicfTRNG2MibObjects=_HpnicfTRNG2MibObjects_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,121,1))
_HpnicfTrangeCreateTimerangeTable_Object=MibTable
hpnicfTrangeCreateTimerangeTable=_HpnicfTrangeCreateTimerangeTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,121,1,1))
if mibBuilder.loadTexts:hpnicfTrangeCreateTimerangeTable.setStatus(_A)
_HpnicfTrangeCreateTimerangeEntry_Object=MibTableRow
hpnicfTrangeCreateTimerangeEntry=_HpnicfTrangeCreateTimerangeEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,121,1,1,1))
hpnicfTrangeCreateTimerangeEntry.setIndexNames((0,_D,_G))
if mibBuilder.loadTexts:hpnicfTrangeCreateTimerangeEntry.setStatus(_A)
class _HpnicfTrangeIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_HpnicfTrangeIndex_Type.__name__=_C
_HpnicfTrangeIndex_Object=MibTableColumn
hpnicfTrangeIndex=_HpnicfTrangeIndex_Object((1,3,6,1,4,1,11,2,14,11,15,2,121,1,1,1,1),_HpnicfTrangeIndex_Type())
hpnicfTrangeIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:hpnicfTrangeIndex.setStatus(_A)
class _HpnicfTrangeName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_HpnicfTrangeName_Type.__name__=_F
_HpnicfTrangeName_Object=MibTableColumn
hpnicfTrangeName=_HpnicfTrangeName_Object((1,3,6,1,4,1,11,2,14,11,15,2,121,1,1,1,2),_HpnicfTrangeName_Type())
hpnicfTrangeName.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfTrangeName.setStatus(_A)
_HpnicfTrangeValidFlag_Type=TruthValue
_HpnicfTrangeValidFlag_Object=MibTableColumn
hpnicfTrangeValidFlag=_HpnicfTrangeValidFlag_Object((1,3,6,1,4,1,11,2,14,11,15,2,121,1,1,1,3),_HpnicfTrangeValidFlag_Type())
hpnicfTrangeValidFlag.setMaxAccess('read-only')
if mibBuilder.loadTexts:hpnicfTrangeValidFlag.setStatus(_A)
_HpnicfTrangeCreateRowStatus_Type=RowStatus
_HpnicfTrangeCreateRowStatus_Object=MibTableColumn
hpnicfTrangeCreateRowStatus=_HpnicfTrangeCreateRowStatus_Object((1,3,6,1,4,1,11,2,14,11,15,2,121,1,1,1,4),_HpnicfTrangeCreateRowStatus_Type())
hpnicfTrangeCreateRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfTrangeCreateRowStatus.setStatus(_A)
_HpnicfTrangeAbsoluteTable_Object=MibTable
hpnicfTrangeAbsoluteTable=_HpnicfTrangeAbsoluteTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,121,1,2))
if mibBuilder.loadTexts:hpnicfTrangeAbsoluteTable.setStatus(_A)
_HpnicfTrangeAbsoluteEntry_Object=MibTableRow
hpnicfTrangeAbsoluteEntry=_HpnicfTrangeAbsoluteEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,121,1,2,1))
hpnicfTrangeAbsoluteEntry.setIndexNames((0,_D,_H),(0,_D,_I))
if mibBuilder.loadTexts:hpnicfTrangeAbsoluteEntry.setStatus(_A)
class _HpnicfTrangeAbsoluteNameIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_HpnicfTrangeAbsoluteNameIndex_Type.__name__=_C
_HpnicfTrangeAbsoluteNameIndex_Object=MibTableColumn
hpnicfTrangeAbsoluteNameIndex=_HpnicfTrangeAbsoluteNameIndex_Object((1,3,6,1,4,1,11,2,14,11,15,2,121,1,2,1,1),_HpnicfTrangeAbsoluteNameIndex_Type())
hpnicfTrangeAbsoluteNameIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:hpnicfTrangeAbsoluteNameIndex.setStatus(_A)
class _HpnicfTrangeAbsoluteSubIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,12))
_HpnicfTrangeAbsoluteSubIndex_Type.__name__=_C
_HpnicfTrangeAbsoluteSubIndex_Object=MibTableColumn
hpnicfTrangeAbsoluteSubIndex=_HpnicfTrangeAbsoluteSubIndex_Object((1,3,6,1,4,1,11,2,14,11,15,2,121,1,2,1,2),_HpnicfTrangeAbsoluteSubIndex_Type())
hpnicfTrangeAbsoluteSubIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:hpnicfTrangeAbsoluteSubIndex.setStatus(_A)
_HpnicfTrangeAbsoluteStartTime_Type=DateAndTime
_HpnicfTrangeAbsoluteStartTime_Object=MibTableColumn
hpnicfTrangeAbsoluteStartTime=_HpnicfTrangeAbsoluteStartTime_Object((1,3,6,1,4,1,11,2,14,11,15,2,121,1,2,1,3),_HpnicfTrangeAbsoluteStartTime_Type())
hpnicfTrangeAbsoluteStartTime.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfTrangeAbsoluteStartTime.setStatus(_A)
_HpnicfTrangeAbsoluteEndTime_Type=DateAndTime
_HpnicfTrangeAbsoluteEndTime_Object=MibTableColumn
hpnicfTrangeAbsoluteEndTime=_HpnicfTrangeAbsoluteEndTime_Object((1,3,6,1,4,1,11,2,14,11,15,2,121,1,2,1,4),_HpnicfTrangeAbsoluteEndTime_Type())
hpnicfTrangeAbsoluteEndTime.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfTrangeAbsoluteEndTime.setStatus(_A)
_HpnicfTrangeAbsolueRowStatus_Type=RowStatus
_HpnicfTrangeAbsolueRowStatus_Object=MibTableColumn
hpnicfTrangeAbsolueRowStatus=_HpnicfTrangeAbsolueRowStatus_Object((1,3,6,1,4,1,11,2,14,11,15,2,121,1,2,1,5),_HpnicfTrangeAbsolueRowStatus_Type())
hpnicfTrangeAbsolueRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfTrangeAbsolueRowStatus.setStatus(_A)
_HpnicfTrangePeriodicTable_Object=MibTable
hpnicfTrangePeriodicTable=_HpnicfTrangePeriodicTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,121,1,3))
if mibBuilder.loadTexts:hpnicfTrangePeriodicTable.setStatus(_A)
_HpnicfTrangePeriodicEntry_Object=MibTableRow
hpnicfTrangePeriodicEntry=_HpnicfTrangePeriodicEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,121,1,3,1))
hpnicfTrangePeriodicEntry.setIndexNames((0,_D,_J),(0,_D,_K))
if mibBuilder.loadTexts:hpnicfTrangePeriodicEntry.setStatus(_A)
class _HpnicfTrangePeriodicNameIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_HpnicfTrangePeriodicNameIndex_Type.__name__=_C
_HpnicfTrangePeriodicNameIndex_Object=MibTableColumn
hpnicfTrangePeriodicNameIndex=_HpnicfTrangePeriodicNameIndex_Object((1,3,6,1,4,1,11,2,14,11,15,2,121,1,3,1,1),_HpnicfTrangePeriodicNameIndex_Type())
hpnicfTrangePeriodicNameIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:hpnicfTrangePeriodicNameIndex.setStatus(_A)
class _HpnicfTrangePeriodicSubIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,32))
_HpnicfTrangePeriodicSubIndex_Type.__name__=_C
_HpnicfTrangePeriodicSubIndex_Object=MibTableColumn
hpnicfTrangePeriodicSubIndex=_HpnicfTrangePeriodicSubIndex_Object((1,3,6,1,4,1,11,2,14,11,15,2,121,1,3,1,2),_HpnicfTrangePeriodicSubIndex_Type())
hpnicfTrangePeriodicSubIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:hpnicfTrangePeriodicSubIndex.setStatus(_A)
class _HpnicfTrangePeriodicDayOfWeek_Type(Bits):namedValues=NamedValues(*(('sunday',0),('monday',1),('tuesday',2),('wednesday',3),('thursday',4),('friday',5),('saturday',6)))
_HpnicfTrangePeriodicDayOfWeek_Type.__name__='Bits'
_HpnicfTrangePeriodicDayOfWeek_Object=MibTableColumn
hpnicfTrangePeriodicDayOfWeek=_HpnicfTrangePeriodicDayOfWeek_Object((1,3,6,1,4,1,11,2,14,11,15,2,121,1,3,1,3),_HpnicfTrangePeriodicDayOfWeek_Type())
hpnicfTrangePeriodicDayOfWeek.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfTrangePeriodicDayOfWeek.setStatus(_A)
_HpnicfTrangePeriodicStartTime_Type=DateAndTime
_HpnicfTrangePeriodicStartTime_Object=MibTableColumn
hpnicfTrangePeriodicStartTime=_HpnicfTrangePeriodicStartTime_Object((1,3,6,1,4,1,11,2,14,11,15,2,121,1,3,1,4),_HpnicfTrangePeriodicStartTime_Type())
hpnicfTrangePeriodicStartTime.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfTrangePeriodicStartTime.setStatus(_A)
_HpnicfTrangePeriodicEndTime_Type=DateAndTime
_HpnicfTrangePeriodicEndTime_Object=MibTableColumn
hpnicfTrangePeriodicEndTime=_HpnicfTrangePeriodicEndTime_Object((1,3,6,1,4,1,11,2,14,11,15,2,121,1,3,1,5),_HpnicfTrangePeriodicEndTime_Type())
hpnicfTrangePeriodicEndTime.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfTrangePeriodicEndTime.setStatus(_A)
_HpnicfTrangePeriodicRowStatus_Type=RowStatus
_HpnicfTrangePeriodicRowStatus_Object=MibTableColumn
hpnicfTrangePeriodicRowStatus=_HpnicfTrangePeriodicRowStatus_Object((1,3,6,1,4,1,11,2,14,11,15,2,121,1,3,1,6),_HpnicfTrangePeriodicRowStatus_Type())
hpnicfTrangePeriodicRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfTrangePeriodicRowStatus.setStatus(_A)
mibBuilder.exportSymbols(_D,**{'hpnicfTRNG2':hpnicfTRNG2,'hpnicfTRNG2MibObjects':hpnicfTRNG2MibObjects,'hpnicfTrangeCreateTimerangeTable':hpnicfTrangeCreateTimerangeTable,'hpnicfTrangeCreateTimerangeEntry':hpnicfTrangeCreateTimerangeEntry,_G:hpnicfTrangeIndex,'hpnicfTrangeName':hpnicfTrangeName,'hpnicfTrangeValidFlag':hpnicfTrangeValidFlag,'hpnicfTrangeCreateRowStatus':hpnicfTrangeCreateRowStatus,'hpnicfTrangeAbsoluteTable':hpnicfTrangeAbsoluteTable,'hpnicfTrangeAbsoluteEntry':hpnicfTrangeAbsoluteEntry,_H:hpnicfTrangeAbsoluteNameIndex,_I:hpnicfTrangeAbsoluteSubIndex,'hpnicfTrangeAbsoluteStartTime':hpnicfTrangeAbsoluteStartTime,'hpnicfTrangeAbsoluteEndTime':hpnicfTrangeAbsoluteEndTime,'hpnicfTrangeAbsolueRowStatus':hpnicfTrangeAbsolueRowStatus,'hpnicfTrangePeriodicTable':hpnicfTrangePeriodicTable,'hpnicfTrangePeriodicEntry':hpnicfTrangePeriodicEntry,_J:hpnicfTrangePeriodicNameIndex,_K:hpnicfTrangePeriodicSubIndex,'hpnicfTrangePeriodicDayOfWeek':hpnicfTrangePeriodicDayOfWeek,'hpnicfTrangePeriodicStartTime':hpnicfTrangePeriodicStartTime,'hpnicfTrangePeriodicEndTime':hpnicfTrangePeriodicEndTime,'hpnicfTrangePeriodicRowStatus':hpnicfTrangePeriodicRowStatus})