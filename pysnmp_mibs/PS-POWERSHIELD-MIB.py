_T='psAlarmInputState'
_S='psAlarmInputNumber'
_R='psAlarmMonoblockMaximum'
_Q='psMonoblockNumber'
_P='not-accessible'
_O='psStringNumber'
_N='OctetString'
_M='psAlarmChannel'
_L='accessible-for-notify'
_K='psAlarmMonoblockMinimum'
_J='psAlarmMinimum'
_I='psAlarmMaximum'
_H='psAlarmMonitor'
_G='psAlarmCatagory'
_F='psAlarmString'
_E='read-only'
_D='psAlarmTimeStamp'
_C='Integer32'
_B='current'
_A='PS-POWERSHIELD-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_N,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
psPowerShield=ModuleIdentity((1,3,6,1,4,1,35154))
if mibBuilder.loadTexts:psPowerShield.setRevisions(('2010-06-10 01:08',))
_PsB1001_ObjectIdentity=ObjectIdentity
psB1001=_PsB1001_ObjectIdentity((1,3,6,1,4,1,35154,1001))
_PsNotificationsObjects_ObjectIdentity=ObjectIdentity
psNotificationsObjects=_PsNotificationsObjects_ObjectIdentity((1,3,6,1,4,1,35154,1001,1))
class _PsAlarmTimeStamp_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(13,13));fixedLength=13
_PsAlarmTimeStamp_Type.__name__=_N
_PsAlarmTimeStamp_Object=MibScalar
psAlarmTimeStamp=_PsAlarmTimeStamp_Object((1,3,6,1,4,1,35154,1001,1,11),_PsAlarmTimeStamp_Type())
psAlarmTimeStamp.setMaxAccess(_L)
if mibBuilder.loadTexts:psAlarmTimeStamp.setStatus(_B)
class _PsAlarmCatagory_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*(('notTriggered',1),('lowLimitExceeded',2),('highLimitExceeded',3),('lowLimitExceededInDischarge',4),('highLimitDischarge',5),('lowLimitExceededInCharge',6),('highLimitCharge',7)))
_PsAlarmCatagory_Type.__name__=_C
_PsAlarmCatagory_Object=MibScalar
psAlarmCatagory=_PsAlarmCatagory_Object((1,3,6,1,4,1,35154,1001,1,12),_PsAlarmCatagory_Type())
psAlarmCatagory.setMaxAccess(_L)
if mibBuilder.loadTexts:psAlarmCatagory.setStatus(_B)
class _PsAlarmChannel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,16))
_PsAlarmChannel_Type.__name__=_C
_PsAlarmChannel_Object=MibScalar
psAlarmChannel=_PsAlarmChannel_Object((1,3,6,1,4,1,35154,1001,1,13),_PsAlarmChannel_Type())
psAlarmChannel.setMaxAccess(_L)
if mibBuilder.loadTexts:psAlarmChannel.setStatus(_B)
class _PsAlarmString_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,16))
_PsAlarmString_Type.__name__=_C
_PsAlarmString_Object=MibScalar
psAlarmString=_PsAlarmString_Object((1,3,6,1,4,1,35154,1001,1,14),_PsAlarmString_Type())
psAlarmString.setMaxAccess(_L)
if mibBuilder.loadTexts:psAlarmString.setStatus(_B)
class _PsAlarmMonitor_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15)));namedValues=NamedValues(*(('master',0),('slave1',1),('slave2',2),('slave3',3),('slave4',4),('slave5',5),('slave6',6),('slave7',7),('slave8',8),('slave9',9),('slave10',10),('slave11',11),('slave12',12),('slave13',13),('slave14',14),('slave15',15)))
_PsAlarmMonitor_Type.__name__=_C
_PsAlarmMonitor_Object=MibScalar
psAlarmMonitor=_PsAlarmMonitor_Object((1,3,6,1,4,1,35154,1001,1,15),_PsAlarmMonitor_Type())
psAlarmMonitor.setMaxAccess(_L)
if mibBuilder.loadTexts:psAlarmMonitor.setStatus(_B)
class _PsAlarmMonoblockMinimum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1280))
_PsAlarmMonoblockMinimum_Type.__name__=_C
_PsAlarmMonoblockMinimum_Object=MibScalar
psAlarmMonoblockMinimum=_PsAlarmMonoblockMinimum_Object((1,3,6,1,4,1,35154,1001,1,16),_PsAlarmMonoblockMinimum_Type())
psAlarmMonoblockMinimum.setMaxAccess(_L)
if mibBuilder.loadTexts:psAlarmMonoblockMinimum.setStatus(_B)
class _PsAlarmMonoblockMaximum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1280))
_PsAlarmMonoblockMaximum_Type.__name__=_C
_PsAlarmMonoblockMaximum_Object=MibScalar
psAlarmMonoblockMaximum=_PsAlarmMonoblockMaximum_Object((1,3,6,1,4,1,35154,1001,1,17),_PsAlarmMonoblockMaximum_Type())
psAlarmMonoblockMaximum.setMaxAccess(_L)
if mibBuilder.loadTexts:psAlarmMonoblockMaximum.setStatus(_B)
class _PsAlarmMinimum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-2147483648,2147483647))
_PsAlarmMinimum_Type.__name__=_C
_PsAlarmMinimum_Object=MibScalar
psAlarmMinimum=_PsAlarmMinimum_Object((1,3,6,1,4,1,35154,1001,1,18),_PsAlarmMinimum_Type())
psAlarmMinimum.setMaxAccess(_E)
if mibBuilder.loadTexts:psAlarmMinimum.setStatus(_B)
class _PsAlarmMaximum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-2147483648,2147483647))
_PsAlarmMaximum_Type.__name__=_C
_PsAlarmMaximum_Object=MibScalar
psAlarmMaximum=_PsAlarmMaximum_Object((1,3,6,1,4,1,35154,1001,1,19),_PsAlarmMaximum_Type())
psAlarmMaximum.setMaxAccess(_E)
if mibBuilder.loadTexts:psAlarmMaximum.setStatus(_B)
class _PsAlarmInputNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,32))
_PsAlarmInputNumber_Type.__name__=_C
_PsAlarmInputNumber_Object=MibScalar
psAlarmInputNumber=_PsAlarmInputNumber_Object((1,3,6,1,4,1,35154,1001,1,20),_PsAlarmInputNumber_Type())
psAlarmInputNumber.setMaxAccess(_L)
if mibBuilder.loadTexts:psAlarmInputNumber.setStatus(_B)
class _PsAlarmInputState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_PsAlarmInputState_Type.__name__=_C
_PsAlarmInputState_Object=MibScalar
psAlarmInputState=_PsAlarmInputState_Object((1,3,6,1,4,1,35154,1001,1,21),_PsAlarmInputState_Type())
psAlarmInputState.setMaxAccess(_L)
if mibBuilder.loadTexts:psAlarmInputState.setStatus(_B)
_PsNotifications_ObjectIdentity=ObjectIdentity
psNotifications=_PsNotifications_ObjectIdentity((1,3,6,1,4,1,35154,1001,2))
_PsNotificationsPrefix_ObjectIdentity=ObjectIdentity
psNotificationsPrefix=_PsNotificationsPrefix_ObjectIdentity((1,3,6,1,4,1,35154,1001,2,0))
_PsStrings_ObjectIdentity=ObjectIdentity
psStrings=_PsStrings_ObjectIdentity((1,3,6,1,4,1,35154,1001,3))
_PsStringTable_Object=MibTable
psStringTable=_PsStringTable_Object((1,3,6,1,4,1,35154,1001,3,1))
if mibBuilder.loadTexts:psStringTable.setStatus(_B)
_PsStringEntry_Object=MibTableRow
psStringEntry=_PsStringEntry_Object((1,3,6,1,4,1,35154,1001,3,1,1))
psStringEntry.setIndexNames((0,_A,_O))
if mibBuilder.loadTexts:psStringEntry.setStatus(_B)
class _PsStringNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,32))
_PsStringNumber_Type.__name__=_C
_PsStringNumber_Object=MibTableColumn
psStringNumber=_PsStringNumber_Object((1,3,6,1,4,1,35154,1001,3,1,1,1),_PsStringNumber_Type())
psStringNumber.setMaxAccess(_P)
if mibBuilder.loadTexts:psStringNumber.setStatus(_B)
class _PsStringFirstMonoblock_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1280))
_PsStringFirstMonoblock_Type.__name__=_C
_PsStringFirstMonoblock_Object=MibTableColumn
psStringFirstMonoblock=_PsStringFirstMonoblock_Object((1,3,6,1,4,1,35154,1001,3,1,1,2),_PsStringFirstMonoblock_Type())
psStringFirstMonoblock.setMaxAccess(_E)
if mibBuilder.loadTexts:psStringFirstMonoblock.setStatus(_B)
class _PsStringLastMonoblock_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1280))
_PsStringLastMonoblock_Type.__name__=_C
_PsStringLastMonoblock_Object=MibTableColumn
psStringLastMonoblock=_PsStringLastMonoblock_Object((1,3,6,1,4,1,35154,1001,3,1,1,3),_PsStringLastMonoblock_Type())
psStringLastMonoblock.setMaxAccess(_E)
if mibBuilder.loadTexts:psStringLastMonoblock.setStatus(_B)
class _PsStringState_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,12))
_PsStringState_Type.__name__=_N
_PsStringState_Object=MibTableColumn
psStringState=_PsStringState_Object((1,3,6,1,4,1,35154,1001,3,1,1,4),_PsStringState_Type())
psStringState.setMaxAccess(_E)
if mibBuilder.loadTexts:psStringState.setStatus(_B)
class _PsStringVoltage_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_PsStringVoltage_Type.__name__=_C
_PsStringVoltage_Object=MibTableColumn
psStringVoltage=_PsStringVoltage_Object((1,3,6,1,4,1,35154,1001,3,1,1,5),_PsStringVoltage_Type())
psStringVoltage.setMaxAccess(_E)
if mibBuilder.loadTexts:psStringVoltage.setStatus(_B)
class _PsStringTemperature_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_PsStringTemperature_Type.__name__=_C
_PsStringTemperature_Object=MibTableColumn
psStringTemperature=_PsStringTemperature_Object((1,3,6,1,4,1,35154,1001,3,1,1,6),_PsStringTemperature_Type())
psStringTemperature.setMaxAccess(_E)
if mibBuilder.loadTexts:psStringTemperature.setStatus(_B)
class _PsStringCurrent_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_PsStringCurrent_Type.__name__=_C
_PsStringCurrent_Object=MibTableColumn
psStringCurrent=_PsStringCurrent_Object((1,3,6,1,4,1,35154,1001,3,1,1,7),_PsStringCurrent_Type())
psStringCurrent.setMaxAccess(_E)
if mibBuilder.loadTexts:psStringCurrent.setStatus(_B)
class _PsStringTimestamp_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,20))
_PsStringTimestamp_Type.__name__=_N
_PsStringTimestamp_Object=MibTableColumn
psStringTimestamp=_PsStringTimestamp_Object((1,3,6,1,4,1,35154,1001,3,1,1,8),_PsStringTimestamp_Type())
psStringTimestamp.setMaxAccess(_E)
if mibBuilder.loadTexts:psStringTimestamp.setStatus(_B)
_PsMonoblocks_ObjectIdentity=ObjectIdentity
psMonoblocks=_PsMonoblocks_ObjectIdentity((1,3,6,1,4,1,35154,1001,4))
_PsMonoblockTable_Object=MibTable
psMonoblockTable=_PsMonoblockTable_Object((1,3,6,1,4,1,35154,1001,4,1))
if mibBuilder.loadTexts:psMonoblockTable.setStatus(_B)
_PsMonoblockEntry_Object=MibTableRow
psMonoblockEntry=_PsMonoblockEntry_Object((1,3,6,1,4,1,35154,1001,4,1,1))
psMonoblockEntry.setIndexNames((0,_A,_Q))
if mibBuilder.loadTexts:psMonoblockEntry.setStatus(_B)
class _PsMonoblockNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1280))
_PsMonoblockNumber_Type.__name__=_C
_PsMonoblockNumber_Object=MibTableColumn
psMonoblockNumber=_PsMonoblockNumber_Object((1,3,6,1,4,1,35154,1001,4,1,1,1),_PsMonoblockNumber_Type())
psMonoblockNumber.setMaxAccess(_P)
if mibBuilder.loadTexts:psMonoblockNumber.setStatus(_B)
class _PsMonoblockOwner_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1280))
_PsMonoblockOwner_Type.__name__=_C
_PsMonoblockOwner_Object=MibTableColumn
psMonoblockOwner=_PsMonoblockOwner_Object((1,3,6,1,4,1,35154,1001,4,1,1,2),_PsMonoblockOwner_Type())
psMonoblockOwner.setMaxAccess(_E)
if mibBuilder.loadTexts:psMonoblockOwner.setStatus(_B)
class _PsMonoblockVoltage_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_PsMonoblockVoltage_Type.__name__=_C
_PsMonoblockVoltage_Object=MibTableColumn
psMonoblockVoltage=_PsMonoblockVoltage_Object((1,3,6,1,4,1,35154,1001,4,1,1,3),_PsMonoblockVoltage_Type())
psMonoblockVoltage.setMaxAccess(_E)
if mibBuilder.loadTexts:psMonoblockVoltage.setStatus(_B)
class _PsMonoblockTemperature_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_PsMonoblockTemperature_Type.__name__=_C
_PsMonoblockTemperature_Object=MibTableColumn
psMonoblockTemperature=_PsMonoblockTemperature_Object((1,3,6,1,4,1,35154,1001,4,1,1,4),_PsMonoblockTemperature_Type())
psMonoblockTemperature.setMaxAccess(_E)
if mibBuilder.loadTexts:psMonoblockTemperature.setStatus(_B)
class _PsMonoblockImpedance_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_PsMonoblockImpedance_Type.__name__=_C
_PsMonoblockImpedance_Object=MibTableColumn
psMonoblockImpedance=_PsMonoblockImpedance_Object((1,3,6,1,4,1,35154,1001,4,1,1,5),_PsMonoblockImpedance_Type())
psMonoblockImpedance.setMaxAccess(_E)
if mibBuilder.loadTexts:psMonoblockImpedance.setStatus(_B)
class _PsMonoblockTimestamp_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,20))
_PsMonoblockTimestamp_Type.__name__=_N
_PsMonoblockTimestamp_Object=MibTableColumn
psMonoblockTimestamp=_PsMonoblockTimestamp_Object((1,3,6,1,4,1,35154,1001,4,1,1,6),_PsMonoblockTimestamp_Type())
psMonoblockTimestamp.setMaxAccess(_E)
if mibBuilder.loadTexts:psMonoblockTimestamp.setStatus(_B)
_PsDebuggingObjects_ObjectIdentity=ObjectIdentity
psDebuggingObjects=_PsDebuggingObjects_ObjectIdentity((1,3,6,1,4,1,35154,1001,5))
class _PsDebuggingTimeouts_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_PsDebuggingTimeouts_Type.__name__=_C
_PsDebuggingTimeouts_Object=MibScalar
psDebuggingTimeouts=_PsDebuggingTimeouts_Object((1,3,6,1,4,1,35154,1001,5,1),_PsDebuggingTimeouts_Type())
psDebuggingTimeouts.setMaxAccess(_E)
if mibBuilder.loadTexts:psDebuggingTimeouts.setStatus(_B)
class _PsDebuggingOverflows_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_PsDebuggingOverflows_Type.__name__=_C
_PsDebuggingOverflows_Object=MibScalar
psDebuggingOverflows=_PsDebuggingOverflows_Object((1,3,6,1,4,1,35154,1001,5,2),_PsDebuggingOverflows_Type())
psDebuggingOverflows.setMaxAccess(_E)
if mibBuilder.loadTexts:psDebuggingOverflows.setStatus(_B)
class _PsDebuggingRequests_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_PsDebuggingRequests_Type.__name__=_C
_PsDebuggingRequests_Object=MibScalar
psDebuggingRequests=_PsDebuggingRequests_Object((1,3,6,1,4,1,35154,1001,5,3),_PsDebuggingRequests_Type())
psDebuggingRequests.setMaxAccess(_E)
if mibBuilder.loadTexts:psDebuggingRequests.setStatus(_B)
class _PsDebuggingResponses_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_PsDebuggingResponses_Type.__name__=_C
_PsDebuggingResponses_Object=MibScalar
psDebuggingResponses=_PsDebuggingResponses_Object((1,3,6,1,4,1,35154,1001,5,4),_PsDebuggingResponses_Type())
psDebuggingResponses.setMaxAccess(_E)
if mibBuilder.loadTexts:psDebuggingResponses.setStatus(_B)
class _PsDebuggingValid_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_PsDebuggingValid_Type.__name__=_C
_PsDebuggingValid_Object=MibScalar
psDebuggingValid=_PsDebuggingValid_Object((1,3,6,1,4,1,35154,1001,5,5),_PsDebuggingValid_Type())
psDebuggingValid.setMaxAccess(_E)
if mibBuilder.loadTexts:psDebuggingValid.setStatus(_B)
class _PsDebuggingInvalid_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_PsDebuggingInvalid_Type.__name__=_C
_PsDebuggingInvalid_Object=MibScalar
psDebuggingInvalid=_PsDebuggingInvalid_Object((1,3,6,1,4,1,35154,1001,5,6),_PsDebuggingInvalid_Type())
psDebuggingInvalid.setMaxAccess(_E)
if mibBuilder.loadTexts:psDebuggingInvalid.setStatus(_B)
class _PsDebuggingRetries_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_PsDebuggingRetries_Type.__name__=_C
_PsDebuggingRetries_Object=MibScalar
psDebuggingRetries=_PsDebuggingRetries_Object((1,3,6,1,4,1,35154,1001,5,7),_PsDebuggingRetries_Type())
psDebuggingRetries.setMaxAccess(_E)
if mibBuilder.loadTexts:psDebuggingRetries.setStatus(_B)
psAlarmMonoblockChargeDischarge=NotificationType((1,3,6,1,4,1,35154,1001,2,0,1))
psAlarmMonoblockChargeDischarge.setObjects(*((_A,_D),(_A,_G),(_A,_F),(_A,_H),(_A,_M),(_A,_K),(_A,_J),(_A,_I)))
if mibBuilder.loadTexts:psAlarmMonoblockChargeDischarge.setStatus(_B)
psAlarmMonoblockFloat=NotificationType((1,3,6,1,4,1,35154,1001,2,0,2))
psAlarmMonoblockFloat.setObjects(*((_A,_D),(_A,_G),(_A,_F),(_A,_H),(_A,_M),(_A,_K),(_A,_J),(_A,_I)))
if mibBuilder.loadTexts:psAlarmMonoblockFloat.setStatus(_B)
psAlarmMonoblockVoltageVariation=NotificationType((1,3,6,1,4,1,35154,1001,2,0,3))
psAlarmMonoblockVoltageVariation.setObjects(*((_A,_D),(_A,_G),(_A,_F),(_A,_K),(_A,_R),(_A,_I)))
if mibBuilder.loadTexts:psAlarmMonoblockVoltageVariation.setStatus(_B)
psAlarmMonoblockVoltageIdle=NotificationType((1,3,6,1,4,1,35154,1001,2,0,4))
psAlarmMonoblockVoltageIdle.setObjects(*((_A,_D),(_A,_G),(_A,_F),(_A,_H),(_A,_K),(_A,_I)))
if mibBuilder.loadTexts:psAlarmMonoblockVoltageIdle.setStatus(_B)
psAlarmStringVoltageChargeDischarge=NotificationType((1,3,6,1,4,1,35154,1001,2,0,5))
psAlarmStringVoltageChargeDischarge.setObjects(*((_A,_D),(_A,_G),(_A,_F),(_A,_J),(_A,_I)))
if mibBuilder.loadTexts:psAlarmStringVoltageChargeDischarge.setStatus(_B)
psAlarmStringVoltageFloat=NotificationType((1,3,6,1,4,1,35154,1001,2,0,6))
psAlarmStringVoltageFloat.setObjects(*((_A,_D),(_A,_G),(_A,_F),(_A,_J),(_A,_I)))
if mibBuilder.loadTexts:psAlarmStringVoltageFloat.setStatus(_B)
psAlarmChargeCurrent=NotificationType((1,3,6,1,4,1,35154,1001,2,0,7))
psAlarmChargeCurrent.setObjects(*((_A,_D),(_A,_G),(_A,_F),(_A,_H),(_A,_M),(_A,_J),(_A,_I)))
if mibBuilder.loadTexts:psAlarmChargeCurrent.setStatus(_B)
psAlarmDischargeCurrent=NotificationType((1,3,6,1,4,1,35154,1001,2,0,8))
psAlarmDischargeCurrent.setObjects(*((_A,_D),(_A,_G),(_A,_F),(_A,_H),(_A,_M),(_A,_J),(_A,_I)))
if mibBuilder.loadTexts:psAlarmDischargeCurrent.setStatus(_B)
psAlarmFloatCurrent=NotificationType((1,3,6,1,4,1,35154,1001,2,0,9))
psAlarmFloatCurrent.setObjects(*((_A,_D),(_A,_G),(_A,_F),(_A,_H),(_A,_M),(_A,_J),(_A,_I)))
if mibBuilder.loadTexts:psAlarmFloatCurrent.setStatus(_B)
psAlarmStringModeCharge=NotificationType((1,3,6,1,4,1,35154,1001,2,0,10))
psAlarmStringModeCharge.setObjects(*((_A,_D),(_A,_F)))
if mibBuilder.loadTexts:psAlarmStringModeCharge.setStatus(_B)
psAlarmStringModeDischarge=NotificationType((1,3,6,1,4,1,35154,1001,2,0,11))
psAlarmStringModeDischarge.setObjects(*((_A,_D),(_A,_F)))
if mibBuilder.loadTexts:psAlarmStringModeDischarge.setStatus(_B)
psAlarmStringModeFloat=NotificationType((1,3,6,1,4,1,35154,1001,2,0,12))
psAlarmStringModeFloat.setObjects(*((_A,_D),(_A,_F)))
if mibBuilder.loadTexts:psAlarmStringModeFloat.setStatus(_B)
psAlarmStringModeIdle=NotificationType((1,3,6,1,4,1,35154,1001,2,0,13))
psAlarmStringModeIdle.setObjects(*((_A,_D),(_A,_F)))
if mibBuilder.loadTexts:psAlarmStringModeIdle.setStatus(_B)
psAlarmModuleFailure=NotificationType((1,3,6,1,4,1,35154,1001,2,0,14))
psAlarmModuleFailure.setObjects(*((_A,_D),(_A,_G),(_A,_F),(_A,_H),(_A,_K)))
if mibBuilder.loadTexts:psAlarmModuleFailure.setStatus(_B)
psAlarmMonitorOffline=NotificationType((1,3,6,1,4,1,35154,1001,2,0,15))
psAlarmMonitorOffline.setObjects(*((_A,_D),(_A,_G),(_A,_H)))
if mibBuilder.loadTexts:psAlarmMonitorOffline.setStatus(_B)
psAlarmMemoryFormat=NotificationType((1,3,6,1,4,1,35154,1001,2,0,16))
psAlarmMemoryFormat.setObjects(*((_A,_D),(_A,_H)))
if mibBuilder.loadTexts:psAlarmMemoryFormat.setStatus(_B)
psAlarmMemoryLow=NotificationType((1,3,6,1,4,1,35154,1001,2,0,17))
psAlarmMemoryLow.setObjects(*((_A,_D),(_A,_H)))
if mibBuilder.loadTexts:psAlarmMemoryLow.setStatus(_B)
psAlarmMemoryFull=NotificationType((1,3,6,1,4,1,35154,1001,2,0,18))
psAlarmMemoryFull.setObjects(*((_A,_D),(_A,_H)))
if mibBuilder.loadTexts:psAlarmMemoryFull.setStatus(_B)
psAlarmLongTermMemoryLow=NotificationType((1,3,6,1,4,1,35154,1001,2,0,19))
psAlarmLongTermMemoryLow.setObjects(*((_A,_D),(_A,_H)))
if mibBuilder.loadTexts:psAlarmLongTermMemoryLow.setStatus(_B)
psAlarmLongTermMemoryFull=NotificationType((1,3,6,1,4,1,35154,1001,2,0,20))
psAlarmLongTermMemoryFull.setObjects(*((_A,_D),(_A,_H)))
if mibBuilder.loadTexts:psAlarmLongTermMemoryFull.setStatus(_B)
psAlarmTemperature=NotificationType((1,3,6,1,4,1,35154,1001,2,0,21))
psAlarmTemperature.setObjects(*((_A,_D),(_A,_G),(_A,_F),(_A,_H),(_A,_M),(_A,_J),(_A,_I)))
if mibBuilder.loadTexts:psAlarmTemperature.setStatus(_B)
psAlarmMonoblockPostTemperature=NotificationType((1,3,6,1,4,1,35154,1001,2,0,22))
psAlarmMonoblockPostTemperature.setObjects(*((_A,_G),(_A,_F),(_A,_K),(_A,_J),(_A,_I)))
if mibBuilder.loadTexts:psAlarmMonoblockPostTemperature.setStatus(_B)
psAlarmMonoblockTemperatureVariation=NotificationType((1,3,6,1,4,1,35154,1001,2,0,23))
psAlarmMonoblockTemperatureVariation.setObjects(*((_A,_G),(_A,_F),(_A,_K),(_A,_I)))
if mibBuilder.loadTexts:psAlarmMonoblockTemperatureVariation.setStatus(_B)
psAlarmMonitoredMains=NotificationType((1,3,6,1,4,1,35154,1001,2,0,24))
psAlarmMonitoredMains.setObjects((_A,_D))
if mibBuilder.loadTexts:psAlarmMonitoredMains.setStatus(_B)
psAlarmCommsNotification=NotificationType((1,3,6,1,4,1,35154,1001,2,0,25))
psAlarmCommsNotification.setObjects((_A,_D))
if mibBuilder.loadTexts:psAlarmCommsNotification.setStatus(_B)
psAlarmBaselineImpedanceExceeded=NotificationType((1,3,6,1,4,1,35154,1001,2,0,26))
psAlarmBaselineImpedanceExceeded.setObjects(*((_A,_D),(_A,_G),(_A,_F),(_A,_H),(_A,_K),(_A,_J),(_A,_I)))
if mibBuilder.loadTexts:psAlarmBaselineImpedanceExceeded.setStatus(_B)
psAlarmStringVarianceImpedanceExceeded=NotificationType((1,3,6,1,4,1,35154,1001,2,0,27))
psAlarmStringVarianceImpedanceExceeded.setObjects(*((_A,_D),(_A,_G),(_A,_F),(_A,_H),(_A,_K),(_A,_J),(_A,_I)))
if mibBuilder.loadTexts:psAlarmStringVarianceImpedanceExceeded.setStatus(_B)
psAlarmInput=NotificationType((1,3,6,1,4,1,35154,1001,2,0,28))
psAlarmInput.setObjects(*((_A,_S),(_A,_T)))
if mibBuilder.loadTexts:psAlarmInput.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'psPowerShield':psPowerShield,'psB1001':psB1001,'psNotificationsObjects':psNotificationsObjects,_D:psAlarmTimeStamp,_G:psAlarmCatagory,_M:psAlarmChannel,_F:psAlarmString,_H:psAlarmMonitor,_K:psAlarmMonoblockMinimum,_R:psAlarmMonoblockMaximum,_J:psAlarmMinimum,_I:psAlarmMaximum,_S:psAlarmInputNumber,_T:psAlarmInputState,'psNotifications':psNotifications,'psNotificationsPrefix':psNotificationsPrefix,'psAlarmMonoblockChargeDischarge':psAlarmMonoblockChargeDischarge,'psAlarmMonoblockFloat':psAlarmMonoblockFloat,'psAlarmMonoblockVoltageVariation':psAlarmMonoblockVoltageVariation,'psAlarmMonoblockVoltageIdle':psAlarmMonoblockVoltageIdle,'psAlarmStringVoltageChargeDischarge':psAlarmStringVoltageChargeDischarge,'psAlarmStringVoltageFloat':psAlarmStringVoltageFloat,'psAlarmChargeCurrent':psAlarmChargeCurrent,'psAlarmDischargeCurrent':psAlarmDischargeCurrent,'psAlarmFloatCurrent':psAlarmFloatCurrent,'psAlarmStringModeCharge':psAlarmStringModeCharge,'psAlarmStringModeDischarge':psAlarmStringModeDischarge,'psAlarmStringModeFloat':psAlarmStringModeFloat,'psAlarmStringModeIdle':psAlarmStringModeIdle,'psAlarmModuleFailure':psAlarmModuleFailure,'psAlarmMonitorOffline':psAlarmMonitorOffline,'psAlarmMemoryFormat':psAlarmMemoryFormat,'psAlarmMemoryLow':psAlarmMemoryLow,'psAlarmMemoryFull':psAlarmMemoryFull,'psAlarmLongTermMemoryLow':psAlarmLongTermMemoryLow,'psAlarmLongTermMemoryFull':psAlarmLongTermMemoryFull,'psAlarmTemperature':psAlarmTemperature,'psAlarmMonoblockPostTemperature':psAlarmMonoblockPostTemperature,'psAlarmMonoblockTemperatureVariation':psAlarmMonoblockTemperatureVariation,'psAlarmMonitoredMains':psAlarmMonitoredMains,'psAlarmCommsNotification':psAlarmCommsNotification,'psAlarmBaselineImpedanceExceeded':psAlarmBaselineImpedanceExceeded,'psAlarmStringVarianceImpedanceExceeded':psAlarmStringVarianceImpedanceExceeded,'psAlarmInput':psAlarmInput,'psStrings':psStrings,'psStringTable':psStringTable,'psStringEntry':psStringEntry,_O:psStringNumber,'psStringFirstMonoblock':psStringFirstMonoblock,'psStringLastMonoblock':psStringLastMonoblock,'psStringState':psStringState,'psStringVoltage':psStringVoltage,'psStringTemperature':psStringTemperature,'psStringCurrent':psStringCurrent,'psStringTimestamp':psStringTimestamp,'psMonoblocks':psMonoblocks,'psMonoblockTable':psMonoblockTable,'psMonoblockEntry':psMonoblockEntry,_Q:psMonoblockNumber,'psMonoblockOwner':psMonoblockOwner,'psMonoblockVoltage':psMonoblockVoltage,'psMonoblockTemperature':psMonoblockTemperature,'psMonoblockImpedance':psMonoblockImpedance,'psMonoblockTimestamp':psMonoblockTimestamp,'psDebuggingObjects':psDebuggingObjects,'psDebuggingTimeouts':psDebuggingTimeouts,'psDebuggingOverflows':psDebuggingOverflows,'psDebuggingRequests':psDebuggingRequests,'psDebuggingResponses':psDebuggingResponses,'psDebuggingValid':psDebuggingValid,'psDebuggingInvalid':psDebuggingInvalid,'psDebuggingRetries':psDebuggingRetries})