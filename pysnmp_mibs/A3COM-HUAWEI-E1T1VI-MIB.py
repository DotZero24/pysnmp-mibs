_F='read-only'
_E='Integer32'
_D='ifDescr'
_C='ifIndex'
_B='IF-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
h3cCommon,=mibBuilder.importSymbols('A3COM-HUAWEI-OID-MIB','h3cCommon')
ifDescr,ifIndex=mibBuilder.importSymbols(_B,_D,_C)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
h3cE1T1VI=ModuleIdentity((1,3,6,1,4,1,43,45,1,10,2,76))
if mibBuilder.loadTexts:h3cE1T1VI.setRevisions(('2010-04-08 18:55','2009-06-08 17:41','2007-04-05 15:42'))
_H3cE1T1VITable_Object=MibTable
h3cE1T1VITable=_H3cE1T1VITable_Object((1,3,6,1,4,1,43,45,1,10,2,76,1))
if mibBuilder.loadTexts:h3cE1T1VITable.setStatus(_A)
_H3cE1T1VIEntry_Object=MibTableRow
h3cE1T1VIEntry=_H3cE1T1VIEntry_Object((1,3,6,1,4,1,43,45,1,10,2,76,1,1))
h3cE1T1VIEntry.setIndexNames((0,_B,_C))
if mibBuilder.loadTexts:h3cE1T1VIEntry.setStatus(_A)
_H3cE1T1VIUsingTimeslots_Type=Integer32
_H3cE1T1VIUsingTimeslots_Object=MibTableColumn
h3cE1T1VIUsingTimeslots=_H3cE1T1VIUsingTimeslots_Object((1,3,6,1,4,1,43,45,1,10,2,76,1,1,1),_H3cE1T1VIUsingTimeslots_Type())
h3cE1T1VIUsingTimeslots.setMaxAccess(_F)
if mibBuilder.loadTexts:h3cE1T1VIUsingTimeslots.setStatus(_A)
_H3cE1T1VIUsingTimeslotsRatio_Type=Integer32
_H3cE1T1VIUsingTimeslotsRatio_Object=MibTableColumn
h3cE1T1VIUsingTimeslotsRatio=_H3cE1T1VIUsingTimeslotsRatio_Object((1,3,6,1,4,1,43,45,1,10,2,76,1,1,2),_H3cE1T1VIUsingTimeslotsRatio_Type())
h3cE1T1VIUsingTimeslotsRatio.setMaxAccess(_F)
if mibBuilder.loadTexts:h3cE1T1VIUsingTimeslotsRatio.setStatus(_A)
_H3cE1T1VINotifications_ObjectIdentity=ObjectIdentity
h3cE1T1VINotifications=_H3cE1T1VINotifications_ObjectIdentity((1,3,6,1,4,1,43,45,1,10,2,76,2))
_H3cE1T1VITrapPrefix_ObjectIdentity=ObjectIdentity
h3cE1T1VITrapPrefix=_H3cE1T1VITrapPrefix_ObjectIdentity((1,3,6,1,4,1,43,45,1,10,2,76,2,0))
_H3cE1T1VIGeneral_ObjectIdentity=ObjectIdentity
h3cE1T1VIGeneral=_H3cE1T1VIGeneral_ObjectIdentity((1,3,6,1,4,1,43,45,1,10,2,76,3))
class _H3cE1T1VITrapTimeSlotEnable_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('enable',1),('disable',2)))
_H3cE1T1VITrapTimeSlotEnable_Type.__name__=_E
_H3cE1T1VITrapTimeSlotEnable_Object=MibScalar
h3cE1T1VITrapTimeSlotEnable=_H3cE1T1VITrapTimeSlotEnable_Object((1,3,6,1,4,1,43,45,1,10,2,76,3,1),_H3cE1T1VITrapTimeSlotEnable_Type())
h3cE1T1VITrapTimeSlotEnable.setMaxAccess('read-write')
if mibBuilder.loadTexts:h3cE1T1VITrapTimeSlotEnable.setStatus(_A)
h3cE1T1VITrapTimeSlot=NotificationType((1,3,6,1,4,1,43,45,1,10,2,76,2,0,1))
h3cE1T1VITrapTimeSlot.setObjects(*((_B,_C),(_B,_D)))
if mibBuilder.loadTexts:h3cE1T1VITrapTimeSlot.setStatus(_A)
mibBuilder.exportSymbols('A3COM-HUAWEI-E1T1VI-MIB',**{'h3cE1T1VI':h3cE1T1VI,'h3cE1T1VITable':h3cE1T1VITable,'h3cE1T1VIEntry':h3cE1T1VIEntry,'h3cE1T1VIUsingTimeslots':h3cE1T1VIUsingTimeslots,'h3cE1T1VIUsingTimeslotsRatio':h3cE1T1VIUsingTimeslotsRatio,'h3cE1T1VINotifications':h3cE1T1VINotifications,'h3cE1T1VITrapPrefix':h3cE1T1VITrapPrefix,'h3cE1T1VITrapTimeSlot':h3cE1T1VITrapTimeSlot,'h3cE1T1VIGeneral':h3cE1T1VIGeneral,'h3cE1T1VITrapTimeSlotEnable':h3cE1T1VITrapTimeSlotEnable})