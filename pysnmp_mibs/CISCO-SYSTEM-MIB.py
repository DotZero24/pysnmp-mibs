_h='ciscoSystemSummerTimeGroupRev1'
_g='ciscoSystemClockChanged'
_f='csySummerTmZnGMTOffset'
_e='csyStandardTmZnGMTOffset'
_d='csyNotificationsEnable'
_c='csySnmpAuthFailAddress'
_b='csySnmpAuthFailAddressType'
_a='csySnmpAuthFail'
_Z='csyScheduledResetReason'
_Y='csyScheduledResetAction'
_X='csyScheduledResetTime'
_W='csyLocationCountry'
_V='csyClockLostOnReboot'
_U='minutes'
_T='TruthValue'
_S='ciscoSystemNotificationsGroup'
_R='ciscoSystemGeneralGroup'
_Q='ciscoSystemSnmpAuthGroup'
_P='ciscoSystemSummerTimeGroup'
_O='csySummerTimeRecurringEnd'
_N='csySummerTimeRecurringStart'
_M='csySummerTimeOffset'
_L='csySummerTimeStatus'
_K='csyClockDateAndTime'
_J='OctetString'
_I='ciscoSystemScheduledResetGroup'
_H='deprecated'
_G='read-only'
_F='ciscoSystemLocationGroup'
_E='ciscoSystemClockGroup'
_D='Integer32'
_C='read-write'
_B='current'
_A='CISCO-SYSTEM-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_J,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
CountryCode,=mibBuilder.importSymbols('CISCO-TC','CountryCode')
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress','InetAddressType')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DateAndTime,DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime','DisplayString','PhysAddress','TextualConvention',_T)
ciscoSystemMIB=ModuleIdentity((1,3,6,1,4,1,9,9,131))
if mibBuilder.loadTexts:ciscoSystemMIB.setRevisions(('2007-09-16 00:00','2007-05-29 00:00','2001-06-22 00:00','2000-01-25 17:00','1999-02-02 17:00'))
_CiscoSystemMIBObjects_ObjectIdentity=ObjectIdentity
ciscoSystemMIBObjects=_CiscoSystemMIBObjects_ObjectIdentity((1,3,6,1,4,1,9,9,131,1))
_CsyClock_ObjectIdentity=ObjectIdentity
csyClock=_CsyClock_ObjectIdentity((1,3,6,1,4,1,9,9,131,1,1))
_CsyClockDateAndTime_Type=DateAndTime
_CsyClockDateAndTime_Object=MibScalar
csyClockDateAndTime=_CsyClockDateAndTime_Object((1,3,6,1,4,1,9,9,131,1,1,1),_CsyClockDateAndTime_Type())
csyClockDateAndTime.setMaxAccess(_C)
if mibBuilder.loadTexts:csyClockDateAndTime.setStatus(_B)
_CsyClockLostOnReboot_Type=TruthValue
_CsyClockLostOnReboot_Object=MibScalar
csyClockLostOnReboot=_CsyClockLostOnReboot_Object((1,3,6,1,4,1,9,9,131,1,1,2),_CsyClockLostOnReboot_Type())
csyClockLostOnReboot.setMaxAccess(_G)
if mibBuilder.loadTexts:csyClockLostOnReboot.setStatus(_B)
_CsyLocation_ObjectIdentity=ObjectIdentity
csyLocation=_CsyLocation_ObjectIdentity((1,3,6,1,4,1,9,9,131,1,2))
_CsyLocationCountry_Type=CountryCode
_CsyLocationCountry_Object=MibScalar
csyLocationCountry=_CsyLocationCountry_Object((1,3,6,1,4,1,9,9,131,1,2,1),_CsyLocationCountry_Type())
csyLocationCountry.setMaxAccess(_C)
if mibBuilder.loadTexts:csyLocationCountry.setStatus(_B)
_CsySummerTime_ObjectIdentity=ObjectIdentity
csySummerTime=_CsySummerTime_ObjectIdentity((1,3,6,1,4,1,9,9,131,1,3))
_CsySummerTimeStatus_Type=TruthValue
_CsySummerTimeStatus_Object=MibScalar
csySummerTimeStatus=_CsySummerTimeStatus_Object((1,3,6,1,4,1,9,9,131,1,3,1),_CsySummerTimeStatus_Type())
csySummerTimeStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:csySummerTimeStatus.setStatus(_B)
class _CsySummerTimeOffset_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1440))
_CsySummerTimeOffset_Type.__name__=_D
_CsySummerTimeOffset_Object=MibScalar
csySummerTimeOffset=_CsySummerTimeOffset_Object((1,3,6,1,4,1,9,9,131,1,3,2),_CsySummerTimeOffset_Type())
csySummerTimeOffset.setMaxAccess(_C)
if mibBuilder.loadTexts:csySummerTimeOffset.setStatus(_B)
if mibBuilder.loadTexts:csySummerTimeOffset.setUnits('Minutes')
class _CsySummerTimeRecurringStart_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(6,6));fixedLength=6
_CsySummerTimeRecurringStart_Type.__name__=_J
_CsySummerTimeRecurringStart_Object=MibScalar
csySummerTimeRecurringStart=_CsySummerTimeRecurringStart_Object((1,3,6,1,4,1,9,9,131,1,3,3),_CsySummerTimeRecurringStart_Type())
csySummerTimeRecurringStart.setMaxAccess(_C)
if mibBuilder.loadTexts:csySummerTimeRecurringStart.setStatus(_B)
class _CsySummerTimeRecurringEnd_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(6,6));fixedLength=6
_CsySummerTimeRecurringEnd_Type.__name__=_J
_CsySummerTimeRecurringEnd_Object=MibScalar
csySummerTimeRecurringEnd=_CsySummerTimeRecurringEnd_Object((1,3,6,1,4,1,9,9,131,1,3,4),_CsySummerTimeRecurringEnd_Type())
csySummerTimeRecurringEnd.setMaxAccess(_C)
if mibBuilder.loadTexts:csySummerTimeRecurringEnd.setStatus(_B)
class _CsyStandardTmZnGMTOffset_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-720,720))
_CsyStandardTmZnGMTOffset_Type.__name__=_D
_CsyStandardTmZnGMTOffset_Object=MibScalar
csyStandardTmZnGMTOffset=_CsyStandardTmZnGMTOffset_Object((1,3,6,1,4,1,9,9,131,1,3,5),_CsyStandardTmZnGMTOffset_Type())
csyStandardTmZnGMTOffset.setMaxAccess(_C)
if mibBuilder.loadTexts:csyStandardTmZnGMTOffset.setStatus(_B)
if mibBuilder.loadTexts:csyStandardTmZnGMTOffset.setUnits(_U)
class _CsySummerTmZnGMTOffset_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-720,720))
_CsySummerTmZnGMTOffset_Type.__name__=_D
_CsySummerTmZnGMTOffset_Object=MibScalar
csySummerTmZnGMTOffset=_CsySummerTmZnGMTOffset_Object((1,3,6,1,4,1,9,9,131,1,3,6),_CsySummerTmZnGMTOffset_Type())
csySummerTmZnGMTOffset.setMaxAccess(_C)
if mibBuilder.loadTexts:csySummerTmZnGMTOffset.setStatus(_B)
if mibBuilder.loadTexts:csySummerTmZnGMTOffset.setUnits(_U)
_CsyScheduledReset_ObjectIdentity=ObjectIdentity
csyScheduledReset=_CsyScheduledReset_ObjectIdentity((1,3,6,1,4,1,9,9,131,1,4))
_CsyScheduledResetTime_Type=DateAndTime
_CsyScheduledResetTime_Object=MibScalar
csyScheduledResetTime=_CsyScheduledResetTime_Object((1,3,6,1,4,1,9,9,131,1,4,1),_CsyScheduledResetTime_Type())
csyScheduledResetTime.setMaxAccess(_C)
if mibBuilder.loadTexts:csyScheduledResetTime.setStatus(_B)
class _CsyScheduledResetAction_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('reset',1),('resetMinDown',2)))
_CsyScheduledResetAction_Type.__name__=_D
_CsyScheduledResetAction_Object=MibScalar
csyScheduledResetAction=_CsyScheduledResetAction_Object((1,3,6,1,4,1,9,9,131,1,4,2),_CsyScheduledResetAction_Type())
csyScheduledResetAction.setMaxAccess(_C)
if mibBuilder.loadTexts:csyScheduledResetAction.setStatus(_B)
_CsyScheduledResetReason_Type=DisplayString
_CsyScheduledResetReason_Object=MibScalar
csyScheduledResetReason=_CsyScheduledResetReason_Object((1,3,6,1,4,1,9,9,131,1,4,3),_CsyScheduledResetReason_Type())
csyScheduledResetReason.setMaxAccess(_C)
if mibBuilder.loadTexts:csyScheduledResetReason.setStatus(_B)
_CsySnmpAuthentication_ObjectIdentity=ObjectIdentity
csySnmpAuthentication=_CsySnmpAuthentication_ObjectIdentity((1,3,6,1,4,1,9,9,131,1,5))
_CsySnmpAuthFail_Type=Counter32
_CsySnmpAuthFail_Object=MibScalar
csySnmpAuthFail=_CsySnmpAuthFail_Object((1,3,6,1,4,1,9,9,131,1,5,1),_CsySnmpAuthFail_Type())
csySnmpAuthFail.setMaxAccess(_G)
if mibBuilder.loadTexts:csySnmpAuthFail.setStatus(_B)
_CsySnmpAuthFailAddressType_Type=InetAddressType
_CsySnmpAuthFailAddressType_Object=MibScalar
csySnmpAuthFailAddressType=_CsySnmpAuthFailAddressType_Object((1,3,6,1,4,1,9,9,131,1,5,2),_CsySnmpAuthFailAddressType_Type())
csySnmpAuthFailAddressType.setMaxAccess(_G)
if mibBuilder.loadTexts:csySnmpAuthFailAddressType.setStatus(_B)
_CsySnmpAuthFailAddress_Type=InetAddress
_CsySnmpAuthFailAddress_Object=MibScalar
csySnmpAuthFailAddress=_CsySnmpAuthFailAddress_Object((1,3,6,1,4,1,9,9,131,1,5,3),_CsySnmpAuthFailAddress_Type())
csySnmpAuthFailAddress.setMaxAccess(_G)
if mibBuilder.loadTexts:csySnmpAuthFailAddress.setStatus(_B)
_CsyGeneral_ObjectIdentity=ObjectIdentity
csyGeneral=_CsyGeneral_ObjectIdentity((1,3,6,1,4,1,9,9,131,1,6))
class _CsyNotificationsEnable_Type(TruthValue):defaultValue=2
_CsyNotificationsEnable_Type.__name__=_T
_CsyNotificationsEnable_Object=MibScalar
csyNotificationsEnable=_CsyNotificationsEnable_Object((1,3,6,1,4,1,9,9,131,1,6,1),_CsyNotificationsEnable_Type())
csyNotificationsEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:csyNotificationsEnable.setStatus(_B)
_CiscoSystemMIBNotificationPrefix_ObjectIdentity=ObjectIdentity
ciscoSystemMIBNotificationPrefix=_CiscoSystemMIBNotificationPrefix_ObjectIdentity((1,3,6,1,4,1,9,9,131,2))
_CiscoSystemMIBNotifications_ObjectIdentity=ObjectIdentity
ciscoSystemMIBNotifications=_CiscoSystemMIBNotifications_ObjectIdentity((1,3,6,1,4,1,9,9,131,2,0))
_CiscoSystemMIBConformance_ObjectIdentity=ObjectIdentity
ciscoSystemMIBConformance=_CiscoSystemMIBConformance_ObjectIdentity((1,3,6,1,4,1,9,9,131,3))
_CiscoSystemMIBCompliances_ObjectIdentity=ObjectIdentity
ciscoSystemMIBCompliances=_CiscoSystemMIBCompliances_ObjectIdentity((1,3,6,1,4,1,9,9,131,3,1))
_CiscoSystemMIBGroups_ObjectIdentity=ObjectIdentity
ciscoSystemMIBGroups=_CiscoSystemMIBGroups_ObjectIdentity((1,3,6,1,4,1,9,9,131,3,2))
ciscoSystemClockGroup=ObjectGroup((1,3,6,1,4,1,9,9,131,3,2,1))
ciscoSystemClockGroup.setObjects(*((_A,_K),(_A,_V)))
if mibBuilder.loadTexts:ciscoSystemClockGroup.setStatus(_B)
ciscoSystemLocationGroup=ObjectGroup((1,3,6,1,4,1,9,9,131,3,2,2))
ciscoSystemLocationGroup.setObjects((_A,_W))
if mibBuilder.loadTexts:ciscoSystemLocationGroup.setStatus(_B)
ciscoSystemSummerTimeGroup=ObjectGroup((1,3,6,1,4,1,9,9,131,3,2,3))
ciscoSystemSummerTimeGroup.setObjects(*((_A,_L),(_A,_M),(_A,_N),(_A,_O)))
if mibBuilder.loadTexts:ciscoSystemSummerTimeGroup.setStatus(_H)
ciscoSystemScheduledResetGroup=ObjectGroup((1,3,6,1,4,1,9,9,131,3,2,4))
ciscoSystemScheduledResetGroup.setObjects(*((_A,_X),(_A,_Y),(_A,_Z)))
if mibBuilder.loadTexts:ciscoSystemScheduledResetGroup.setStatus(_B)
ciscoSystemSnmpAuthGroup=ObjectGroup((1,3,6,1,4,1,9,9,131,3,2,5))
ciscoSystemSnmpAuthGroup.setObjects(*((_A,_a),(_A,_b),(_A,_c)))
if mibBuilder.loadTexts:ciscoSystemSnmpAuthGroup.setStatus(_B)
ciscoSystemGeneralGroup=ObjectGroup((1,3,6,1,4,1,9,9,131,3,2,6))
ciscoSystemGeneralGroup.setObjects((_A,_d))
if mibBuilder.loadTexts:ciscoSystemGeneralGroup.setStatus(_B)
ciscoSystemSummerTimeGroupRev1=ObjectGroup((1,3,6,1,4,1,9,9,131,3,2,8))
ciscoSystemSummerTimeGroupRev1.setObjects(*((_A,_L),(_A,_M),(_A,_N),(_A,_O),(_A,_e),(_A,_f)))
if mibBuilder.loadTexts:ciscoSystemSummerTimeGroupRev1.setStatus(_B)
ciscoSystemClockChanged=NotificationType((1,3,6,1,4,1,9,9,131,2,0,1))
ciscoSystemClockChanged.setObjects((_A,_K))
if mibBuilder.loadTexts:ciscoSystemClockChanged.setStatus(_B)
ciscoSystemNotificationsGroup=NotificationGroup((1,3,6,1,4,1,9,9,131,3,2,7))
ciscoSystemNotificationsGroup.setObjects((_A,_g))
if mibBuilder.loadTexts:ciscoSystemNotificationsGroup.setStatus(_B)
ciscoSystemMIBCompliance=ModuleCompliance((1,3,6,1,4,1,9,9,131,3,1,1))
ciscoSystemMIBCompliance.setObjects(*((_A,_E),(_A,_F)))
if mibBuilder.loadTexts:ciscoSystemMIBCompliance.setStatus(_H)
ciscoSystemMIBCompliance2=ModuleCompliance((1,3,6,1,4,1,9,9,131,3,1,2))
ciscoSystemMIBCompliance2.setObjects(*((_A,_E),(_A,_F),(_A,_P),(_A,_I)))
if mibBuilder.loadTexts:ciscoSystemMIBCompliance2.setStatus(_H)
ciscoSystemMIBCompliance3=ModuleCompliance((1,3,6,1,4,1,9,9,131,3,1,3))
ciscoSystemMIBCompliance3.setObjects(*((_A,_E),(_A,_F),(_A,_P),(_A,_I),(_A,_Q),(_A,_R),(_A,_S)))
if mibBuilder.loadTexts:ciscoSystemMIBCompliance3.setStatus(_H)
ciscoSystemMIBCompliance4=ModuleCompliance((1,3,6,1,4,1,9,9,131,3,1,4))
ciscoSystemMIBCompliance4.setObjects(*((_A,_E),(_A,_F),(_A,_h),(_A,_I),(_A,_Q),(_A,_R),(_A,_S)))
if mibBuilder.loadTexts:ciscoSystemMIBCompliance4.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'ciscoSystemMIB':ciscoSystemMIB,'ciscoSystemMIBObjects':ciscoSystemMIBObjects,'csyClock':csyClock,_K:csyClockDateAndTime,_V:csyClockLostOnReboot,'csyLocation':csyLocation,_W:csyLocationCountry,'csySummerTime':csySummerTime,_L:csySummerTimeStatus,_M:csySummerTimeOffset,_N:csySummerTimeRecurringStart,_O:csySummerTimeRecurringEnd,_e:csyStandardTmZnGMTOffset,_f:csySummerTmZnGMTOffset,'csyScheduledReset':csyScheduledReset,_X:csyScheduledResetTime,_Y:csyScheduledResetAction,_Z:csyScheduledResetReason,'csySnmpAuthentication':csySnmpAuthentication,_a:csySnmpAuthFail,_b:csySnmpAuthFailAddressType,_c:csySnmpAuthFailAddress,'csyGeneral':csyGeneral,_d:csyNotificationsEnable,'ciscoSystemMIBNotificationPrefix':ciscoSystemMIBNotificationPrefix,'ciscoSystemMIBNotifications':ciscoSystemMIBNotifications,_g:ciscoSystemClockChanged,'ciscoSystemMIBConformance':ciscoSystemMIBConformance,'ciscoSystemMIBCompliances':ciscoSystemMIBCompliances,'ciscoSystemMIBCompliance':ciscoSystemMIBCompliance,'ciscoSystemMIBCompliance2':ciscoSystemMIBCompliance2,'ciscoSystemMIBCompliance3':ciscoSystemMIBCompliance3,'ciscoSystemMIBCompliance4':ciscoSystemMIBCompliance4,'ciscoSystemMIBGroups':ciscoSystemMIBGroups,_E:ciscoSystemClockGroup,_F:ciscoSystemLocationGroup,_P:ciscoSystemSummerTimeGroup,_I:ciscoSystemScheduledResetGroup,_Q:ciscoSystemSnmpAuthGroup,_R:ciscoSystemGeneralGroup,_S:ciscoSystemNotificationsGroup,_h:ciscoSystemSummerTimeGroupRev1})