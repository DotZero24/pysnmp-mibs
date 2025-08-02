_G='Integer32'
_F='ifDescr'
_E='read-write'
_D='ifIndex'
_C='read-only'
_B='IF-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
h3cCommon,=mibBuilder.importSymbols('HUAWEI-3COM-OID-MIB','h3cCommon')
ifDescr,ifIndex=mibBuilder.importSymbols(_B,_F,_D)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_G,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
h3cE1T1VI=ModuleIdentity((1,3,6,1,4,1,2011,10,2,76))
if mibBuilder.loadTexts:h3cE1T1VI.setRevisions(('2015-08-19 18:00','2010-04-08 18:55','2009-06-08 17:41','2007-04-05 15:42'))
_H3cE1T1VITable_Object=MibTable
h3cE1T1VITable=_H3cE1T1VITable_Object((1,3,6,1,4,1,2011,10,2,76,1))
if mibBuilder.loadTexts:h3cE1T1VITable.setStatus(_A)
_H3cE1T1VIEntry_Object=MibTableRow
h3cE1T1VIEntry=_H3cE1T1VIEntry_Object((1,3,6,1,4,1,2011,10,2,76,1,1))
h3cE1T1VIEntry.setIndexNames((0,_B,_D))
if mibBuilder.loadTexts:h3cE1T1VIEntry.setStatus(_A)
_H3cE1T1VIUsingTimeslots_Type=Integer32
_H3cE1T1VIUsingTimeslots_Object=MibTableColumn
h3cE1T1VIUsingTimeslots=_H3cE1T1VIUsingTimeslots_Object((1,3,6,1,4,1,2011,10,2,76,1,1,1),_H3cE1T1VIUsingTimeslots_Type())
h3cE1T1VIUsingTimeslots.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cE1T1VIUsingTimeslots.setStatus(_A)
_H3cE1T1VIUsingTimeslotsRatio_Type=Integer32
_H3cE1T1VIUsingTimeslotsRatio_Object=MibTableColumn
h3cE1T1VIUsingTimeslotsRatio=_H3cE1T1VIUsingTimeslotsRatio_Object((1,3,6,1,4,1,2011,10,2,76,1,1,2),_H3cE1T1VIUsingTimeslotsRatio_Type())
h3cE1T1VIUsingTimeslotsRatio.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cE1T1VIUsingTimeslotsRatio.setStatus(_A)
_H3cE1T1VITimeslotsUsedUpCount_Type=Unsigned32
_H3cE1T1VITimeslotsUsedUpCount_Object=MibTableColumn
h3cE1T1VITimeslotsUsedUpCount=_H3cE1T1VITimeslotsUsedUpCount_Object((1,3,6,1,4,1,2011,10,2,76,1,1,3),_H3cE1T1VITimeslotsUsedUpCount_Type())
h3cE1T1VITimeslotsUsedUpCount.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cE1T1VITimeslotsUsedUpCount.setStatus(_A)
_H3cE1T1VITimeslotSampleInterval_Type=Integer32
_H3cE1T1VITimeslotSampleInterval_Object=MibTableColumn
h3cE1T1VITimeslotSampleInterval=_H3cE1T1VITimeslotSampleInterval_Object((1,3,6,1,4,1,2011,10,2,76,1,1,4),_H3cE1T1VITimeslotSampleInterval_Type())
h3cE1T1VITimeslotSampleInterval.setMaxAccess(_E)
if mibBuilder.loadTexts:h3cE1T1VITimeslotSampleInterval.setStatus(_A)
_H3cE1T1VIUsingTimeslotsPeak_Type=Integer32
_H3cE1T1VIUsingTimeslotsPeak_Object=MibTableColumn
h3cE1T1VIUsingTimeslotsPeak=_H3cE1T1VIUsingTimeslotsPeak_Object((1,3,6,1,4,1,2011,10,2,76,1,1,5),_H3cE1T1VIUsingTimeslotsPeak_Type())
h3cE1T1VIUsingTimeslotsPeak.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cE1T1VIUsingTimeslotsPeak.setStatus(_A)
_H3cE1T1VITrapTimeSlotsThreshold_Type=Integer32
_H3cE1T1VITrapTimeSlotsThreshold_Object=MibTableColumn
h3cE1T1VITrapTimeSlotsThreshold=_H3cE1T1VITrapTimeSlotsThreshold_Object((1,3,6,1,4,1,2011,10,2,76,1,1,6),_H3cE1T1VITrapTimeSlotsThreshold_Type())
h3cE1T1VITrapTimeSlotsThreshold.setMaxAccess(_E)
if mibBuilder.loadTexts:h3cE1T1VITrapTimeSlotsThreshold.setStatus(_A)
_H3cE1T1VINotifications_ObjectIdentity=ObjectIdentity
h3cE1T1VINotifications=_H3cE1T1VINotifications_ObjectIdentity((1,3,6,1,4,1,2011,10,2,76,2))
_H3cE1T1VITrapPrefix_ObjectIdentity=ObjectIdentity
h3cE1T1VITrapPrefix=_H3cE1T1VITrapPrefix_ObjectIdentity((1,3,6,1,4,1,2011,10,2,76,2,0))
_H3cE1T1VIGeneral_ObjectIdentity=ObjectIdentity
h3cE1T1VIGeneral=_H3cE1T1VIGeneral_ObjectIdentity((1,3,6,1,4,1,2011,10,2,76,3))
class _H3cE1T1VITrapTimeSlotEnable_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('enable',1),('disable',2)))
_H3cE1T1VITrapTimeSlotEnable_Type.__name__=_G
_H3cE1T1VITrapTimeSlotEnable_Object=MibScalar
h3cE1T1VITrapTimeSlotEnable=_H3cE1T1VITrapTimeSlotEnable_Object((1,3,6,1,4,1,2011,10,2,76,3,1),_H3cE1T1VITrapTimeSlotEnable_Type())
h3cE1T1VITrapTimeSlotEnable.setMaxAccess(_E)
if mibBuilder.loadTexts:h3cE1T1VITrapTimeSlotEnable.setStatus(_A)
h3cE1T1VITrapTimeSlot=NotificationType((1,3,6,1,4,1,2011,10,2,76,2,0,1))
h3cE1T1VITrapTimeSlot.setObjects(*((_B,_D),(_B,_F)))
if mibBuilder.loadTexts:h3cE1T1VITrapTimeSlot.setStatus(_A)
mibBuilder.exportSymbols('H3C-E1T1VI-MIB',**{'h3cE1T1VI':h3cE1T1VI,'h3cE1T1VITable':h3cE1T1VITable,'h3cE1T1VIEntry':h3cE1T1VIEntry,'h3cE1T1VIUsingTimeslots':h3cE1T1VIUsingTimeslots,'h3cE1T1VIUsingTimeslotsRatio':h3cE1T1VIUsingTimeslotsRatio,'h3cE1T1VITimeslotsUsedUpCount':h3cE1T1VITimeslotsUsedUpCount,'h3cE1T1VITimeslotSampleInterval':h3cE1T1VITimeslotSampleInterval,'h3cE1T1VIUsingTimeslotsPeak':h3cE1T1VIUsingTimeslotsPeak,'h3cE1T1VITrapTimeSlotsThreshold':h3cE1T1VITrapTimeSlotsThreshold,'h3cE1T1VINotifications':h3cE1T1VINotifications,'h3cE1T1VITrapPrefix':h3cE1T1VITrapPrefix,'h3cE1T1VITrapTimeSlot':h3cE1T1VITrapTimeSlot,'h3cE1T1VIGeneral':h3cE1T1VIGeneral,'h3cE1T1VITrapTimeSlotEnable':h3cE1T1VITrapTimeSlotEnable})