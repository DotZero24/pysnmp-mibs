_K='rlTBIPeriodicEnd'
_J='rlTBIPeriodicStart'
_I='rlTBIPeriodicWeekDayList'
_H='rlTBIPeriodicTimeRangeName'
_G='read-create'
_F='not-accessible'
_E='rlTBITimeRangeName'
_D='read-write'
_C='RADLAN-TBI-MIB'
_B='DisplayString'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
rnd,=mibBuilder.importSymbols('RADLAN-MIB','rnd')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC',_B,'PhysAddress','RowStatus','TextualConvention','TruthValue')
rlTBIMib=ModuleIdentity((1,3,6,1,4,1,89,145))
if mibBuilder.loadTexts:rlTBIMib.setRevisions(('2006-02-12 00:00',))
class RlTBIWeekDayList(TextualConvention,Bits):status=_A;namedValues=NamedValues(*(('monday',0),('tuesday',1),('wednesday',2),('thursday',3),('friday',4),('saturday',5),('sunday',6)))
_RlTBITimeRangeTable_Object=MibTable
rlTBITimeRangeTable=_RlTBITimeRangeTable_Object((1,3,6,1,4,1,89,145,1))
if mibBuilder.loadTexts:rlTBITimeRangeTable.setStatus(_A)
_RlTBITimeRangeEntry_Object=MibTableRow
rlTBITimeRangeEntry=_RlTBITimeRangeEntry_Object((1,3,6,1,4,1,89,145,1,1))
rlTBITimeRangeEntry.setIndexNames((1,_C,_E))
if mibBuilder.loadTexts:rlTBITimeRangeEntry.setStatus(_A)
class _RlTBITimeRangeName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_RlTBITimeRangeName_Type.__name__=_B
_RlTBITimeRangeName_Object=MibTableColumn
rlTBITimeRangeName=_RlTBITimeRangeName_Object((1,3,6,1,4,1,89,145,1,1,1),_RlTBITimeRangeName_Type())
rlTBITimeRangeName.setMaxAccess(_F)
if mibBuilder.loadTexts:rlTBITimeRangeName.setStatus(_A)
class _RlTBITimeRangeAbsoluteStart_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,14))
_RlTBITimeRangeAbsoluteStart_Type.__name__=_B
_RlTBITimeRangeAbsoluteStart_Object=MibTableColumn
rlTBITimeRangeAbsoluteStart=_RlTBITimeRangeAbsoluteStart_Object((1,3,6,1,4,1,89,145,1,1,2),_RlTBITimeRangeAbsoluteStart_Type())
rlTBITimeRangeAbsoluteStart.setMaxAccess(_D)
if mibBuilder.loadTexts:rlTBITimeRangeAbsoluteStart.setStatus(_A)
class _RlTBITimeRangeAbsoluteEnd_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,14))
_RlTBITimeRangeAbsoluteEnd_Type.__name__=_B
_RlTBITimeRangeAbsoluteEnd_Object=MibTableColumn
rlTBITimeRangeAbsoluteEnd=_RlTBITimeRangeAbsoluteEnd_Object((1,3,6,1,4,1,89,145,1,1,3),_RlTBITimeRangeAbsoluteEnd_Type())
rlTBITimeRangeAbsoluteEnd.setMaxAccess(_D)
if mibBuilder.loadTexts:rlTBITimeRangeAbsoluteEnd.setStatus(_A)
_RlTBITimeRangeActiveStatus_Type=TruthValue
_RlTBITimeRangeActiveStatus_Object=MibTableColumn
rlTBITimeRangeActiveStatus=_RlTBITimeRangeActiveStatus_Object((1,3,6,1,4,1,89,145,1,1,4),_RlTBITimeRangeActiveStatus_Type())
rlTBITimeRangeActiveStatus.setMaxAccess('read-only')
if mibBuilder.loadTexts:rlTBITimeRangeActiveStatus.setStatus(_A)
_RlTBITimeRangeRowStatus_Type=RowStatus
_RlTBITimeRangeRowStatus_Object=MibTableColumn
rlTBITimeRangeRowStatus=_RlTBITimeRangeRowStatus_Object((1,3,6,1,4,1,89,145,1,1,5),_RlTBITimeRangeRowStatus_Type())
rlTBITimeRangeRowStatus.setMaxAccess(_G)
if mibBuilder.loadTexts:rlTBITimeRangeRowStatus.setStatus(_A)
_RlTBIPeriodicTable_Object=MibTable
rlTBIPeriodicTable=_RlTBIPeriodicTable_Object((1,3,6,1,4,1,89,145,2))
if mibBuilder.loadTexts:rlTBIPeriodicTable.setStatus(_A)
_RlTBIPeriodicEntry_Object=MibTableRow
rlTBIPeriodicEntry=_RlTBIPeriodicEntry_Object((1,3,6,1,4,1,89,145,2,1))
rlTBIPeriodicEntry.setIndexNames((0,_C,_H),(0,_C,_I),(0,_C,_J),(0,_C,_K))
if mibBuilder.loadTexts:rlTBIPeriodicEntry.setStatus(_A)
class _RlTBIPeriodicTimeRangeName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_RlTBIPeriodicTimeRangeName_Type.__name__=_B
_RlTBIPeriodicTimeRangeName_Object=MibTableColumn
rlTBIPeriodicTimeRangeName=_RlTBIPeriodicTimeRangeName_Object((1,3,6,1,4,1,89,145,2,1,1),_RlTBIPeriodicTimeRangeName_Type())
rlTBIPeriodicTimeRangeName.setMaxAccess(_F)
if mibBuilder.loadTexts:rlTBIPeriodicTimeRangeName.setStatus(_A)
_RlTBIPeriodicWeekDayList_Type=RlTBIWeekDayList
_RlTBIPeriodicWeekDayList_Object=MibTableColumn
rlTBIPeriodicWeekDayList=_RlTBIPeriodicWeekDayList_Object((1,3,6,1,4,1,89,145,2,1,2),_RlTBIPeriodicWeekDayList_Type())
rlTBIPeriodicWeekDayList.setMaxAccess(_D)
if mibBuilder.loadTexts:rlTBIPeriodicWeekDayList.setStatus(_A)
class _RlTBIPeriodicStart_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,7))
_RlTBIPeriodicStart_Type.__name__=_B
_RlTBIPeriodicStart_Object=MibTableColumn
rlTBIPeriodicStart=_RlTBIPeriodicStart_Object((1,3,6,1,4,1,89,145,2,1,3),_RlTBIPeriodicStart_Type())
rlTBIPeriodicStart.setMaxAccess(_D)
if mibBuilder.loadTexts:rlTBIPeriodicStart.setStatus(_A)
class _RlTBIPeriodicEnd_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,7))
_RlTBIPeriodicEnd_Type.__name__=_B
_RlTBIPeriodicEnd_Object=MibTableColumn
rlTBIPeriodicEnd=_RlTBIPeriodicEnd_Object((1,3,6,1,4,1,89,145,2,1,4),_RlTBIPeriodicEnd_Type())
rlTBIPeriodicEnd.setMaxAccess(_D)
if mibBuilder.loadTexts:rlTBIPeriodicEnd.setStatus(_A)
_RlTBIPeriodicRowStatus_Type=RowStatus
_RlTBIPeriodicRowStatus_Object=MibTableColumn
rlTBIPeriodicRowStatus=_RlTBIPeriodicRowStatus_Object((1,3,6,1,4,1,89,145,2,1,5),_RlTBIPeriodicRowStatus_Type())
rlTBIPeriodicRowStatus.setMaxAccess(_G)
if mibBuilder.loadTexts:rlTBIPeriodicRowStatus.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'RlTBIWeekDayList':RlTBIWeekDayList,'rlTBIMib':rlTBIMib,'rlTBITimeRangeTable':rlTBITimeRangeTable,'rlTBITimeRangeEntry':rlTBITimeRangeEntry,_E:rlTBITimeRangeName,'rlTBITimeRangeAbsoluteStart':rlTBITimeRangeAbsoluteStart,'rlTBITimeRangeAbsoluteEnd':rlTBITimeRangeAbsoluteEnd,'rlTBITimeRangeActiveStatus':rlTBITimeRangeActiveStatus,'rlTBITimeRangeRowStatus':rlTBITimeRangeRowStatus,'rlTBIPeriodicTable':rlTBIPeriodicTable,'rlTBIPeriodicEntry':rlTBIPeriodicEntry,_H:rlTBIPeriodicTimeRangeName,_I:rlTBIPeriodicWeekDayList,_J:rlTBIPeriodicStart,_K:rlTBIPeriodicEnd,'rlTBIPeriodicRowStatus':rlTBIPeriodicRowStatus})