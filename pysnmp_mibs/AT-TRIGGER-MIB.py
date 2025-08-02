_F='triggerLastTriggerActivated'
_E='triggerNumber'
_D='AT-TRIGGER-MIB'
_C='Unsigned32'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
modules,=mibBuilder.importSymbols('AT-SMI-MIB','modules')
ifIndex,=mibBuilder.importSymbols('IF-MIB','ifIndex')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_C,'iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention','TruthValue')
trigger=ModuleIdentity((1,3,6,1,4,1,207,8,4,4,4,53))
if mibBuilder.loadTexts:trigger.setRevisions(('2007-11-28 16:00','2010-06-15 00:15','2010-09-07 00:00'))
_TriggerTraps_ObjectIdentity=ObjectIdentity
triggerTraps=_TriggerTraps_ObjectIdentity((1,3,6,1,4,1,207,8,4,4,4,53,0))
_TriggerLastTriggerActivated_Type=Integer32
_TriggerLastTriggerActivated_Object=MibScalar
triggerLastTriggerActivated=_TriggerLastTriggerActivated_Object((1,3,6,1,4,1,207,8,4,4,4,53,1),_TriggerLastTriggerActivated_Type())
triggerLastTriggerActivated.setMaxAccess(_B)
if mibBuilder.loadTexts:triggerLastTriggerActivated.setStatus(_A)
_TriggerConfigInfoTable_Object=MibTable
triggerConfigInfoTable=_TriggerConfigInfoTable_Object((1,3,6,1,4,1,207,8,4,4,4,53,9))
if mibBuilder.loadTexts:triggerConfigInfoTable.setStatus(_A)
_TriggerConfigInfoEntry_Object=MibTableRow
triggerConfigInfoEntry=_TriggerConfigInfoEntry_Object((1,3,6,1,4,1,207,8,4,4,4,53,9,1))
triggerConfigInfoEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:triggerConfigInfoEntry.setStatus(_A)
class _TriggerNumber_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,250))
_TriggerNumber_Type.__name__=_C
_TriggerNumber_Object=MibTableColumn
triggerNumber=_TriggerNumber_Object((1,3,6,1,4,1,207,8,4,4,4,53,9,1,1),_TriggerNumber_Type())
triggerNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:triggerNumber.setStatus(_A)
_TriggerName_Type=DisplayString
_TriggerName_Object=MibTableColumn
triggerName=_TriggerName_Object((1,3,6,1,4,1,207,8,4,4,4,53,9,1,2),_TriggerName_Type())
triggerName.setMaxAccess(_B)
if mibBuilder.loadTexts:triggerName.setStatus(_A)
_TriggerTypeDetail_Type=DisplayString
_TriggerTypeDetail_Object=MibTableColumn
triggerTypeDetail=_TriggerTypeDetail_Object((1,3,6,1,4,1,207,8,4,4,4,53,9,1,3),_TriggerTypeDetail_Type())
triggerTypeDetail.setMaxAccess(_B)
if mibBuilder.loadTexts:triggerTypeDetail.setStatus(_A)
_TriggerActiveDaysOrDate_Type=DisplayString
_TriggerActiveDaysOrDate_Object=MibTableColumn
triggerActiveDaysOrDate=_TriggerActiveDaysOrDate_Object((1,3,6,1,4,1,207,8,4,4,4,53,9,1,4),_TriggerActiveDaysOrDate_Type())
triggerActiveDaysOrDate.setMaxAccess(_B)
if mibBuilder.loadTexts:triggerActiveDaysOrDate.setStatus(_A)
_TriggerActivateAfter_Type=DisplayString
_TriggerActivateAfter_Object=MibTableColumn
triggerActivateAfter=_TriggerActivateAfter_Object((1,3,6,1,4,1,207,8,4,4,4,53,9,1,5),_TriggerActivateAfter_Type())
triggerActivateAfter.setMaxAccess(_B)
if mibBuilder.loadTexts:triggerActivateAfter.setStatus(_A)
_TriggerActivateBefore_Type=DisplayString
_TriggerActivateBefore_Object=MibTableColumn
triggerActivateBefore=_TriggerActivateBefore_Object((1,3,6,1,4,1,207,8,4,4,4,53,9,1,6),_TriggerActivateBefore_Type())
triggerActivateBefore.setMaxAccess(_B)
if mibBuilder.loadTexts:triggerActivateBefore.setStatus(_A)
_TriggerActiveStatus_Type=TruthValue
_TriggerActiveStatus_Object=MibTableColumn
triggerActiveStatus=_TriggerActiveStatus_Object((1,3,6,1,4,1,207,8,4,4,4,53,9,1,7),_TriggerActiveStatus_Type())
triggerActiveStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:triggerActiveStatus.setStatus(_A)
_TriggerTestMode_Type=TruthValue
_TriggerTestMode_Object=MibTableColumn
triggerTestMode=_TriggerTestMode_Object((1,3,6,1,4,1,207,8,4,4,4,53,9,1,8),_TriggerTestMode_Type())
triggerTestMode.setMaxAccess(_B)
if mibBuilder.loadTexts:triggerTestMode.setStatus(_A)
_TriggerSnmpTrap_Type=TruthValue
_TriggerSnmpTrap_Object=MibTableColumn
triggerSnmpTrap=_TriggerSnmpTrap_Object((1,3,6,1,4,1,207,8,4,4,4,53,9,1,9),_TriggerSnmpTrap_Type())
triggerSnmpTrap.setMaxAccess(_B)
if mibBuilder.loadTexts:triggerSnmpTrap.setStatus(_A)
_TriggerRepeatTimes_Type=DisplayString
_TriggerRepeatTimes_Object=MibTableColumn
triggerRepeatTimes=_TriggerRepeatTimes_Object((1,3,6,1,4,1,207,8,4,4,4,53,9,1,10),_TriggerRepeatTimes_Type())
triggerRepeatTimes.setMaxAccess(_B)
if mibBuilder.loadTexts:triggerRepeatTimes.setStatus(_A)
_TriggerLasttimeModified_Type=DisplayString
_TriggerLasttimeModified_Object=MibTableColumn
triggerLasttimeModified=_TriggerLasttimeModified_Object((1,3,6,1,4,1,207,8,4,4,4,53,9,1,11),_TriggerLasttimeModified_Type())
triggerLasttimeModified.setMaxAccess(_B)
if mibBuilder.loadTexts:triggerLasttimeModified.setStatus(_A)
_TriggerNumberOfActivation_Type=Counter32
_TriggerNumberOfActivation_Object=MibTableColumn
triggerNumberOfActivation=_TriggerNumberOfActivation_Object((1,3,6,1,4,1,207,8,4,4,4,53,9,1,12),_TriggerNumberOfActivation_Type())
triggerNumberOfActivation.setMaxAccess(_B)
if mibBuilder.loadTexts:triggerNumberOfActivation.setStatus(_A)
_TriggerLasttimeActivation_Type=DisplayString
_TriggerLasttimeActivation_Object=MibTableColumn
triggerLasttimeActivation=_TriggerLasttimeActivation_Object((1,3,6,1,4,1,207,8,4,4,4,53,9,1,13),_TriggerLasttimeActivation_Type())
triggerLasttimeActivation.setMaxAccess(_B)
if mibBuilder.loadTexts:triggerLasttimeActivation.setStatus(_A)
class _TriggerNumberOfScripts_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,5))
_TriggerNumberOfScripts_Type.__name__=_C
_TriggerNumberOfScripts_Object=MibTableColumn
triggerNumberOfScripts=_TriggerNumberOfScripts_Object((1,3,6,1,4,1,207,8,4,4,4,53,9,1,14),_TriggerNumberOfScripts_Type())
triggerNumberOfScripts.setMaxAccess(_B)
if mibBuilder.loadTexts:triggerNumberOfScripts.setStatus(_A)
_TriggerScript1_Type=DisplayString
_TriggerScript1_Object=MibTableColumn
triggerScript1=_TriggerScript1_Object((1,3,6,1,4,1,207,8,4,4,4,53,9,1,15),_TriggerScript1_Type())
triggerScript1.setMaxAccess(_B)
if mibBuilder.loadTexts:triggerScript1.setStatus(_A)
_TriggerScript2_Type=DisplayString
_TriggerScript2_Object=MibTableColumn
triggerScript2=_TriggerScript2_Object((1,3,6,1,4,1,207,8,4,4,4,53,9,1,16),_TriggerScript2_Type())
triggerScript2.setMaxAccess(_B)
if mibBuilder.loadTexts:triggerScript2.setStatus(_A)
_TriggerScript3_Type=DisplayString
_TriggerScript3_Object=MibTableColumn
triggerScript3=_TriggerScript3_Object((1,3,6,1,4,1,207,8,4,4,4,53,9,1,17),_TriggerScript3_Type())
triggerScript3.setMaxAccess(_B)
if mibBuilder.loadTexts:triggerScript3.setStatus(_A)
_TriggerScript4_Type=DisplayString
_TriggerScript4_Object=MibTableColumn
triggerScript4=_TriggerScript4_Object((1,3,6,1,4,1,207,8,4,4,4,53,9,1,18),_TriggerScript4_Type())
triggerScript4.setMaxAccess(_B)
if mibBuilder.loadTexts:triggerScript4.setStatus(_A)
_TriggerScript5_Type=DisplayString
_TriggerScript5_Object=MibTableColumn
triggerScript5=_TriggerScript5_Object((1,3,6,1,4,1,207,8,4,4,4,53,9,1,19),_TriggerScript5_Type())
triggerScript5.setMaxAccess(_B)
if mibBuilder.loadTexts:triggerScript5.setStatus(_A)
_TriggerCounters_ObjectIdentity=ObjectIdentity
triggerCounters=_TriggerCounters_ObjectIdentity((1,3,6,1,4,1,207,8,4,4,4,53,10))
_TriggerNumOfActivation_Type=Counter32
_TriggerNumOfActivation_Object=MibScalar
triggerNumOfActivation=_TriggerNumOfActivation_Object((1,3,6,1,4,1,207,8,4,4,4,53,10,1),_TriggerNumOfActivation_Type())
triggerNumOfActivation.setMaxAccess(_B)
if mibBuilder.loadTexts:triggerNumOfActivation.setStatus(_A)
_TriggerNumOfActivationToday_Type=Counter32
_TriggerNumOfActivationToday_Object=MibScalar
triggerNumOfActivationToday=_TriggerNumOfActivationToday_Object((1,3,6,1,4,1,207,8,4,4,4,53,10,2),_TriggerNumOfActivationToday_Type())
triggerNumOfActivationToday.setMaxAccess(_B)
if mibBuilder.loadTexts:triggerNumOfActivationToday.setStatus(_A)
_TriggerNumOfPerodicActivationToday_Type=Counter32
_TriggerNumOfPerodicActivationToday_Object=MibScalar
triggerNumOfPerodicActivationToday=_TriggerNumOfPerodicActivationToday_Object((1,3,6,1,4,1,207,8,4,4,4,53,10,3),_TriggerNumOfPerodicActivationToday_Type())
triggerNumOfPerodicActivationToday.setMaxAccess(_B)
if mibBuilder.loadTexts:triggerNumOfPerodicActivationToday.setStatus(_A)
_TriggerNumOfInterfaceActivationToday_Type=Counter32
_TriggerNumOfInterfaceActivationToday_Object=MibScalar
triggerNumOfInterfaceActivationToday=_TriggerNumOfInterfaceActivationToday_Object((1,3,6,1,4,1,207,8,4,4,4,53,10,4),_TriggerNumOfInterfaceActivationToday_Type())
triggerNumOfInterfaceActivationToday.setMaxAccess(_B)
if mibBuilder.loadTexts:triggerNumOfInterfaceActivationToday.setStatus(_A)
_TriggerNumOfResourceActivationToday_Type=Counter32
_TriggerNumOfResourceActivationToday_Object=MibScalar
triggerNumOfResourceActivationToday=_TriggerNumOfResourceActivationToday_Object((1,3,6,1,4,1,207,8,4,4,4,53,10,5),_TriggerNumOfResourceActivationToday_Type())
triggerNumOfResourceActivationToday.setMaxAccess(_B)
if mibBuilder.loadTexts:triggerNumOfResourceActivationToday.setStatus(_A)
_TriggerNumOfRebootActivationToday_Type=Counter32
_TriggerNumOfRebootActivationToday_Object=MibScalar
triggerNumOfRebootActivationToday=_TriggerNumOfRebootActivationToday_Object((1,3,6,1,4,1,207,8,4,4,4,53,10,6),_TriggerNumOfRebootActivationToday_Type())
triggerNumOfRebootActivationToday.setMaxAccess(_B)
if mibBuilder.loadTexts:triggerNumOfRebootActivationToday.setStatus(_A)
_TriggerNumOfPingPollActivationToday_Type=Counter32
_TriggerNumOfPingPollActivationToday_Object=MibScalar
triggerNumOfPingPollActivationToday=_TriggerNumOfPingPollActivationToday_Object((1,3,6,1,4,1,207,8,4,4,4,53,10,7),_TriggerNumOfPingPollActivationToday_Type())
triggerNumOfPingPollActivationToday.setMaxAccess(_B)
if mibBuilder.loadTexts:triggerNumOfPingPollActivationToday.setStatus(_A)
_TriggerNumOfStackMasterFailActivationToday_Type=Counter32
_TriggerNumOfStackMasterFailActivationToday_Object=MibScalar
triggerNumOfStackMasterFailActivationToday=_TriggerNumOfStackMasterFailActivationToday_Object((1,3,6,1,4,1,207,8,4,4,4,53,10,8),_TriggerNumOfStackMasterFailActivationToday_Type())
triggerNumOfStackMasterFailActivationToday.setMaxAccess(_B)
if mibBuilder.loadTexts:triggerNumOfStackMasterFailActivationToday.setStatus(_A)
_TriggerNumOfStackMemberActivationToday_Type=Counter32
_TriggerNumOfStackMemberActivationToday_Object=MibScalar
triggerNumOfStackMemberActivationToday=_TriggerNumOfStackMemberActivationToday_Object((1,3,6,1,4,1,207,8,4,4,4,53,10,9),_TriggerNumOfStackMemberActivationToday_Type())
triggerNumOfStackMemberActivationToday.setMaxAccess(_B)
if mibBuilder.loadTexts:triggerNumOfStackMemberActivationToday.setStatus(_A)
_TriggerNumOfStackXemStkActivationToday_Type=Counter32
_TriggerNumOfStackXemStkActivationToday_Object=MibScalar
triggerNumOfStackXemStkActivationToday=_TriggerNumOfStackXemStkActivationToday_Object((1,3,6,1,4,1,207,8,4,4,4,53,10,10),_TriggerNumOfStackXemStkActivationToday_Type())
triggerNumOfStackXemStkActivationToday.setMaxAccess(_B)
if mibBuilder.loadTexts:triggerNumOfStackXemStkActivationToday.setStatus(_A)
triggerTrap=NotificationType((1,3,6,1,4,1,207,8,4,4,4,53,0,1))
triggerTrap.setObjects((_D,_F))
if mibBuilder.loadTexts:triggerTrap.setStatus(_A)
mibBuilder.exportSymbols(_D,**{'trigger':trigger,'triggerTraps':triggerTraps,'triggerTrap':triggerTrap,_F:triggerLastTriggerActivated,'triggerConfigInfoTable':triggerConfigInfoTable,'triggerConfigInfoEntry':triggerConfigInfoEntry,_E:triggerNumber,'triggerName':triggerName,'triggerTypeDetail':triggerTypeDetail,'triggerActiveDaysOrDate':triggerActiveDaysOrDate,'triggerActivateAfter':triggerActivateAfter,'triggerActivateBefore':triggerActivateBefore,'triggerActiveStatus':triggerActiveStatus,'triggerTestMode':triggerTestMode,'triggerSnmpTrap':triggerSnmpTrap,'triggerRepeatTimes':triggerRepeatTimes,'triggerLasttimeModified':triggerLasttimeModified,'triggerNumberOfActivation':triggerNumberOfActivation,'triggerLasttimeActivation':triggerLasttimeActivation,'triggerNumberOfScripts':triggerNumberOfScripts,'triggerScript1':triggerScript1,'triggerScript2':triggerScript2,'triggerScript3':triggerScript3,'triggerScript4':triggerScript4,'triggerScript5':triggerScript5,'triggerCounters':triggerCounters,'triggerNumOfActivation':triggerNumOfActivation,'triggerNumOfActivationToday':triggerNumOfActivationToday,'triggerNumOfPerodicActivationToday':triggerNumOfPerodicActivationToday,'triggerNumOfInterfaceActivationToday':triggerNumOfInterfaceActivationToday,'triggerNumOfResourceActivationToday':triggerNumOfResourceActivationToday,'triggerNumOfRebootActivationToday':triggerNumOfRebootActivationToday,'triggerNumOfPingPollActivationToday':triggerNumOfPingPollActivationToday,'triggerNumOfStackMasterFailActivationToday':triggerNumOfStackMasterFailActivationToday,'triggerNumOfStackMemberActivationToday':triggerNumOfStackMemberActivationToday,'triggerNumOfStackXemStkActivationToday':triggerNumOfStackXemStkActivationToday})