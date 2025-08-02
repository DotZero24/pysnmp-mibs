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
hpnicfCommon,=mibBuilder.importSymbols('HPN-ICF-OID-MIB','hpnicfCommon')
ifDescr,ifIndex=mibBuilder.importSymbols(_B,_D,_C)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
hpnicfE1T1VI=ModuleIdentity((1,3,6,1,4,1,11,2,14,11,15,2,76))
if mibBuilder.loadTexts:hpnicfE1T1VI.setRevisions(('2010-04-08 18:55','2009-06-08 17:41','2007-04-05 15:42'))
_HpnicfE1T1VITable_Object=MibTable
hpnicfE1T1VITable=_HpnicfE1T1VITable_Object((1,3,6,1,4,1,11,2,14,11,15,2,76,1))
if mibBuilder.loadTexts:hpnicfE1T1VITable.setStatus(_A)
_HpnicfE1T1VIEntry_Object=MibTableRow
hpnicfE1T1VIEntry=_HpnicfE1T1VIEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,76,1,1))
hpnicfE1T1VIEntry.setIndexNames((0,_B,_C))
if mibBuilder.loadTexts:hpnicfE1T1VIEntry.setStatus(_A)
_HpnicfE1T1VIUsingTimeslots_Type=Integer32
_HpnicfE1T1VIUsingTimeslots_Object=MibTableColumn
hpnicfE1T1VIUsingTimeslots=_HpnicfE1T1VIUsingTimeslots_Object((1,3,6,1,4,1,11,2,14,11,15,2,76,1,1,1),_HpnicfE1T1VIUsingTimeslots_Type())
hpnicfE1T1VIUsingTimeslots.setMaxAccess(_F)
if mibBuilder.loadTexts:hpnicfE1T1VIUsingTimeslots.setStatus(_A)
_HpnicfE1T1VIUsingTimeslotsRatio_Type=Integer32
_HpnicfE1T1VIUsingTimeslotsRatio_Object=MibTableColumn
hpnicfE1T1VIUsingTimeslotsRatio=_HpnicfE1T1VIUsingTimeslotsRatio_Object((1,3,6,1,4,1,11,2,14,11,15,2,76,1,1,2),_HpnicfE1T1VIUsingTimeslotsRatio_Type())
hpnicfE1T1VIUsingTimeslotsRatio.setMaxAccess(_F)
if mibBuilder.loadTexts:hpnicfE1T1VIUsingTimeslotsRatio.setStatus(_A)
_HpnicfE1T1VINotifications_ObjectIdentity=ObjectIdentity
hpnicfE1T1VINotifications=_HpnicfE1T1VINotifications_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,76,2))
_HpnicfE1T1VITrapPrefix_ObjectIdentity=ObjectIdentity
hpnicfE1T1VITrapPrefix=_HpnicfE1T1VITrapPrefix_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,76,2,0))
_HpnicfE1T1VIGeneral_ObjectIdentity=ObjectIdentity
hpnicfE1T1VIGeneral=_HpnicfE1T1VIGeneral_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,76,3))
class _HpnicfE1T1VITrapTimeSlotEnable_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('enable',1),('disable',2)))
_HpnicfE1T1VITrapTimeSlotEnable_Type.__name__=_E
_HpnicfE1T1VITrapTimeSlotEnable_Object=MibScalar
hpnicfE1T1VITrapTimeSlotEnable=_HpnicfE1T1VITrapTimeSlotEnable_Object((1,3,6,1,4,1,11,2,14,11,15,2,76,3,1),_HpnicfE1T1VITrapTimeSlotEnable_Type())
hpnicfE1T1VITrapTimeSlotEnable.setMaxAccess('read-write')
if mibBuilder.loadTexts:hpnicfE1T1VITrapTimeSlotEnable.setStatus(_A)
hpnicfE1T1VITrapTimeSlot=NotificationType((1,3,6,1,4,1,11,2,14,11,15,2,76,2,0,1))
hpnicfE1T1VITrapTimeSlot.setObjects(*((_B,_C),(_B,_D)))
if mibBuilder.loadTexts:hpnicfE1T1VITrapTimeSlot.setStatus(_A)
mibBuilder.exportSymbols('HPN-ICF-E1T1VI-MIB',**{'hpnicfE1T1VI':hpnicfE1T1VI,'hpnicfE1T1VITable':hpnicfE1T1VITable,'hpnicfE1T1VIEntry':hpnicfE1T1VIEntry,'hpnicfE1T1VIUsingTimeslots':hpnicfE1T1VIUsingTimeslots,'hpnicfE1T1VIUsingTimeslotsRatio':hpnicfE1T1VIUsingTimeslotsRatio,'hpnicfE1T1VINotifications':hpnicfE1T1VINotifications,'hpnicfE1T1VITrapPrefix':hpnicfE1T1VITrapPrefix,'hpnicfE1T1VITrapTimeSlot':hpnicfE1T1VITrapTimeSlot,'hpnicfE1T1VIGeneral':hpnicfE1T1VIGeneral,'hpnicfE1T1VITrapTimeSlotEnable':hpnicfE1T1VITrapTimeSlotEnable})