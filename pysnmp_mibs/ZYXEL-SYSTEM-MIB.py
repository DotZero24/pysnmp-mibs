_T='december'
_S='november'
_R='october'
_Q='september'
_P='august'
_O='february'
_N='january'
_M='saturday'
_L='friday'
_K='thursday'
_J='wednesday'
_I='tuesday'
_H='monday'
_G='sunday'
_F='fourth'
_E='second'
_D='Integer32'
_C='read-only'
_B='read-write'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress','InetAddressType')
EnabledStatus,=mibBuilder.importSymbols('P-BRIDGE-MIB','EnabledStatus')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress','RowStatus','TextualConvention')
esMgmt,=mibBuilder.importSymbols('ZYXEL-ES-SMI','esMgmt')
zyxelSystem=ModuleIdentity((1,3,6,1,4,1,890,1,15,3,82))
_ZyxelDateTimeSetup_ObjectIdentity=ObjectIdentity
zyxelDateTimeSetup=_ZyxelDateTimeSetup_ObjectIdentity((1,3,6,1,4,1,890,1,15,3,82,1))
class _ZyDateTimeServerType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('none',1),('daytime',2),('time',3),('ntp',4)))
_ZyDateTimeServerType_Type.__name__=_D
_ZyDateTimeServerType_Object=MibScalar
zyDateTimeServerType=_ZyDateTimeServerType_Object((1,3,6,1,4,1,890,1,15,3,82,1,1),_ZyDateTimeServerType_Type())
zyDateTimeServerType.setMaxAccess(_B)
if mibBuilder.loadTexts:zyDateTimeServerType.setStatus(_A)
_ZyDateTimeZone_Type=Integer32
_ZyDateTimeZone_Object=MibScalar
zyDateTimeZone=_ZyDateTimeZone_Object((1,3,6,1,4,1,890,1,15,3,82,1,3),_ZyDateTimeZone_Type())
zyDateTimeZone.setMaxAccess(_B)
if mibBuilder.loadTexts:zyDateTimeZone.setStatus(_A)
_ZyDateTimeNewDateYear_Type=Integer32
_ZyDateTimeNewDateYear_Object=MibScalar
zyDateTimeNewDateYear=_ZyDateTimeNewDateYear_Object((1,3,6,1,4,1,890,1,15,3,82,1,4),_ZyDateTimeNewDateYear_Type())
zyDateTimeNewDateYear.setMaxAccess(_B)
if mibBuilder.loadTexts:zyDateTimeNewDateYear.setStatus(_A)
_ZyDateTimeNewDateMonth_Type=Integer32
_ZyDateTimeNewDateMonth_Object=MibScalar
zyDateTimeNewDateMonth=_ZyDateTimeNewDateMonth_Object((1,3,6,1,4,1,890,1,15,3,82,1,5),_ZyDateTimeNewDateMonth_Type())
zyDateTimeNewDateMonth.setMaxAccess(_B)
if mibBuilder.loadTexts:zyDateTimeNewDateMonth.setStatus(_A)
_ZyDateTimeNewDateDay_Type=Integer32
_ZyDateTimeNewDateDay_Object=MibScalar
zyDateTimeNewDateDay=_ZyDateTimeNewDateDay_Object((1,3,6,1,4,1,890,1,15,3,82,1,6),_ZyDateTimeNewDateDay_Type())
zyDateTimeNewDateDay.setMaxAccess(_B)
if mibBuilder.loadTexts:zyDateTimeNewDateDay.setStatus(_A)
_ZyDateTimeNewTimeHour_Type=Integer32
_ZyDateTimeNewTimeHour_Object=MibScalar
zyDateTimeNewTimeHour=_ZyDateTimeNewTimeHour_Object((1,3,6,1,4,1,890,1,15,3,82,1,7),_ZyDateTimeNewTimeHour_Type())
zyDateTimeNewTimeHour.setMaxAccess(_B)
if mibBuilder.loadTexts:zyDateTimeNewTimeHour.setStatus(_A)
_ZyDateTimeNewTimeMinute_Type=Integer32
_ZyDateTimeNewTimeMinute_Object=MibScalar
zyDateTimeNewTimeMinute=_ZyDateTimeNewTimeMinute_Object((1,3,6,1,4,1,890,1,15,3,82,1,8),_ZyDateTimeNewTimeMinute_Type())
zyDateTimeNewTimeMinute.setMaxAccess(_B)
if mibBuilder.loadTexts:zyDateTimeNewTimeMinute.setStatus(_A)
_ZyDateTimeNewTimeSecond_Type=Integer32
_ZyDateTimeNewTimeSecond_Object=MibScalar
zyDateTimeNewTimeSecond=_ZyDateTimeNewTimeSecond_Object((1,3,6,1,4,1,890,1,15,3,82,1,9),_ZyDateTimeNewTimeSecond_Type())
zyDateTimeNewTimeSecond.setMaxAccess(_B)
if mibBuilder.loadTexts:zyDateTimeNewTimeSecond.setStatus(_A)
_ZyxelDateTimeDaylightSavingTimeSetup_ObjectIdentity=ObjectIdentity
zyxelDateTimeDaylightSavingTimeSetup=_ZyxelDateTimeDaylightSavingTimeSetup_ObjectIdentity((1,3,6,1,4,1,890,1,15,3,82,1,10))
_ZyDaylightSavingTimeState_Type=EnabledStatus
_ZyDaylightSavingTimeState_Object=MibScalar
zyDaylightSavingTimeState=_ZyDaylightSavingTimeState_Object((1,3,6,1,4,1,890,1,15,3,82,1,10,1),_ZyDaylightSavingTimeState_Type())
zyDaylightSavingTimeState.setMaxAccess(_B)
if mibBuilder.loadTexts:zyDaylightSavingTimeState.setStatus(_A)
class _ZyDaylightSavingTimeStartDateWeek_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('first',1),(_E,2),('third',3),(_F,4),('last',5)))
_ZyDaylightSavingTimeStartDateWeek_Type.__name__=_D
_ZyDaylightSavingTimeStartDateWeek_Object=MibScalar
zyDaylightSavingTimeStartDateWeek=_ZyDaylightSavingTimeStartDateWeek_Object((1,3,6,1,4,1,890,1,15,3,82,1,10,2),_ZyDaylightSavingTimeStartDateWeek_Type())
zyDaylightSavingTimeStartDateWeek.setMaxAccess(_B)
if mibBuilder.loadTexts:zyDaylightSavingTimeStartDateWeek.setStatus(_A)
class _ZyDaylightSavingTimeStartDateDay_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6)));namedValues=NamedValues(*((_G,0),(_H,1),(_I,2),(_J,3),(_K,4),(_L,5),(_M,6)))
_ZyDaylightSavingTimeStartDateDay_Type.__name__=_D
_ZyDaylightSavingTimeStartDateDay_Object=MibScalar
zyDaylightSavingTimeStartDateDay=_ZyDaylightSavingTimeStartDateDay_Object((1,3,6,1,4,1,890,1,15,3,82,1,10,3),_ZyDaylightSavingTimeStartDateDay_Type())
zyDaylightSavingTimeStartDateDay.setMaxAccess(_B)
if mibBuilder.loadTexts:zyDaylightSavingTimeStartDateDay.setStatus(_A)
class _ZyDaylightSavingTimeStartDateMonth_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12)));namedValues=NamedValues(*((_N,1),(_O,2),('march',3),('april',4),('may',5),('june',6),('july',7),(_P,8),(_Q,9),(_R,10),(_S,11),(_T,12)))
_ZyDaylightSavingTimeStartDateMonth_Type.__name__=_D
_ZyDaylightSavingTimeStartDateMonth_Object=MibScalar
zyDaylightSavingTimeStartDateMonth=_ZyDaylightSavingTimeStartDateMonth_Object((1,3,6,1,4,1,890,1,15,3,82,1,10,4),_ZyDaylightSavingTimeStartDateMonth_Type())
zyDaylightSavingTimeStartDateMonth.setMaxAccess(_B)
if mibBuilder.loadTexts:zyDaylightSavingTimeStartDateMonth.setStatus(_A)
_ZyDaylightSavingTimeStartDateHour_Type=Integer32
_ZyDaylightSavingTimeStartDateHour_Object=MibScalar
zyDaylightSavingTimeStartDateHour=_ZyDaylightSavingTimeStartDateHour_Object((1,3,6,1,4,1,890,1,15,3,82,1,10,5),_ZyDaylightSavingTimeStartDateHour_Type())
zyDaylightSavingTimeStartDateHour.setMaxAccess(_B)
if mibBuilder.loadTexts:zyDaylightSavingTimeStartDateHour.setStatus(_A)
class _ZyDaylightSavingTimeEndDateWeek_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('first',1),(_E,2),('third',3),(_F,4),('last',5)))
_ZyDaylightSavingTimeEndDateWeek_Type.__name__=_D
_ZyDaylightSavingTimeEndDateWeek_Object=MibScalar
zyDaylightSavingTimeEndDateWeek=_ZyDaylightSavingTimeEndDateWeek_Object((1,3,6,1,4,1,890,1,15,3,82,1,10,6),_ZyDaylightSavingTimeEndDateWeek_Type())
zyDaylightSavingTimeEndDateWeek.setMaxAccess(_B)
if mibBuilder.loadTexts:zyDaylightSavingTimeEndDateWeek.setStatus(_A)
class _ZyDaylightSavingTimeEndDateDay_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6)));namedValues=NamedValues(*((_G,0),(_H,1),(_I,2),(_J,3),(_K,4),(_L,5),(_M,6)))
_ZyDaylightSavingTimeEndDateDay_Type.__name__=_D
_ZyDaylightSavingTimeEndDateDay_Object=MibScalar
zyDaylightSavingTimeEndDateDay=_ZyDaylightSavingTimeEndDateDay_Object((1,3,6,1,4,1,890,1,15,3,82,1,10,7),_ZyDaylightSavingTimeEndDateDay_Type())
zyDaylightSavingTimeEndDateDay.setMaxAccess(_B)
if mibBuilder.loadTexts:zyDaylightSavingTimeEndDateDay.setStatus(_A)
class _ZyDaylightSavingTimeEndDateMonth_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12)));namedValues=NamedValues(*((_N,1),(_O,2),('march',3),('april',4),('may',5),('june',6),('july',7),(_P,8),(_Q,9),(_R,10),(_S,11),(_T,12)))
_ZyDaylightSavingTimeEndDateMonth_Type.__name__=_D
_ZyDaylightSavingTimeEndDateMonth_Object=MibScalar
zyDaylightSavingTimeEndDateMonth=_ZyDaylightSavingTimeEndDateMonth_Object((1,3,6,1,4,1,890,1,15,3,82,1,10,8),_ZyDaylightSavingTimeEndDateMonth_Type())
zyDaylightSavingTimeEndDateMonth.setMaxAccess(_B)
if mibBuilder.loadTexts:zyDaylightSavingTimeEndDateMonth.setStatus(_A)
_ZyDaylightSavingTimeEndDateHour_Type=Integer32
_ZyDaylightSavingTimeEndDateHour_Object=MibScalar
zyDaylightSavingTimeEndDateHour=_ZyDaylightSavingTimeEndDateHour_Object((1,3,6,1,4,1,890,1,15,3,82,1,10,9),_ZyDaylightSavingTimeEndDateHour_Type())
zyDaylightSavingTimeEndDateHour.setMaxAccess(_B)
if mibBuilder.loadTexts:zyDaylightSavingTimeEndDateHour.setStatus(_A)
_ZyDateTimeServerInetAddressType_Type=InetAddressType
_ZyDateTimeServerInetAddressType_Object=MibScalar
zyDateTimeServerInetAddressType=_ZyDateTimeServerInetAddressType_Object((1,3,6,1,4,1,890,1,15,3,82,1,11),_ZyDateTimeServerInetAddressType_Type())
zyDateTimeServerInetAddressType.setMaxAccess(_B)
if mibBuilder.loadTexts:zyDateTimeServerInetAddressType.setStatus(_A)
_ZyDateTimeServerInetAddress_Type=InetAddress
_ZyDateTimeServerInetAddress_Object=MibScalar
zyDateTimeServerInetAddress=_ZyDateTimeServerInetAddress_Object((1,3,6,1,4,1,890,1,15,3,82,1,12),_ZyDateTimeServerInetAddress_Type())
zyDateTimeServerInetAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:zyDateTimeServerInetAddress.setStatus(_A)
_ZyDateTimeZoneHourMinute_Type=OctetString
_ZyDateTimeZoneHourMinute_Object=MibScalar
zyDateTimeZoneHourMinute=_ZyDateTimeZoneHourMinute_Object((1,3,6,1,4,1,890,1,15,3,82,1,13),_ZyDateTimeZoneHourMinute_Type())
zyDateTimeZoneHourMinute.setMaxAccess(_B)
if mibBuilder.loadTexts:zyDateTimeZoneHourMinute.setStatus(_A)
_ZyDateTimeSyncInterval_Type=Integer32
_ZyDateTimeSyncInterval_Object=MibScalar
zyDateTimeSyncInterval=_ZyDateTimeSyncInterval_Object((1,3,6,1,4,1,890,1,15,3,82,1,14),_ZyDateTimeSyncInterval_Type())
zyDateTimeSyncInterval.setMaxAccess(_B)
if mibBuilder.loadTexts:zyDateTimeSyncInterval.setStatus(_A)
_ZyxelSysInfo_ObjectIdentity=ObjectIdentity
zyxelSysInfo=_ZyxelSysInfo_ObjectIdentity((1,3,6,1,4,1,890,1,15,3,82,2))
_ZySysSwPlatformMajorVers_Type=Integer32
_ZySysSwPlatformMajorVers_Object=MibScalar
zySysSwPlatformMajorVers=_ZySysSwPlatformMajorVers_Object((1,3,6,1,4,1,890,1,15,3,82,2,1),_ZySysSwPlatformMajorVers_Type())
zySysSwPlatformMajorVers.setMaxAccess(_C)
if mibBuilder.loadTexts:zySysSwPlatformMajorVers.setStatus(_A)
_ZySysSwPlatformMinorVers_Type=Integer32
_ZySysSwPlatformMinorVers_Object=MibScalar
zySysSwPlatformMinorVers=_ZySysSwPlatformMinorVers_Object((1,3,6,1,4,1,890,1,15,3,82,2,2),_ZySysSwPlatformMinorVers_Type())
zySysSwPlatformMinorVers.setMaxAccess(_C)
if mibBuilder.loadTexts:zySysSwPlatformMinorVers.setStatus(_A)
_ZySysSwModelString_Type=DisplayString
_ZySysSwModelString_Object=MibScalar
zySysSwModelString=_ZySysSwModelString_Object((1,3,6,1,4,1,890,1,15,3,82,2,3),_ZySysSwModelString_Type())
zySysSwModelString.setMaxAccess(_C)
if mibBuilder.loadTexts:zySysSwModelString.setStatus(_A)
_ZySysSwVersionControlNbr_Type=Integer32
_ZySysSwVersionControlNbr_Object=MibScalar
zySysSwVersionControlNbr=_ZySysSwVersionControlNbr_Object((1,3,6,1,4,1,890,1,15,3,82,2,4),_ZySysSwVersionControlNbr_Type())
zySysSwVersionControlNbr.setMaxAccess(_C)
if mibBuilder.loadTexts:zySysSwVersionControlNbr.setStatus(_A)
_ZySysSwDay_Type=Integer32
_ZySysSwDay_Object=MibScalar
zySysSwDay=_ZySysSwDay_Object((1,3,6,1,4,1,890,1,15,3,82,2,5),_ZySysSwDay_Type())
zySysSwDay.setMaxAccess(_C)
if mibBuilder.loadTexts:zySysSwDay.setStatus(_A)
_ZySysSwMonth_Type=Integer32
_ZySysSwMonth_Object=MibScalar
zySysSwMonth=_ZySysSwMonth_Object((1,3,6,1,4,1,890,1,15,3,82,2,6),_ZySysSwMonth_Type())
zySysSwMonth.setMaxAccess(_C)
if mibBuilder.loadTexts:zySysSwMonth.setStatus(_A)
_ZySysSwYear_Type=Integer32
_ZySysSwYear_Object=MibScalar
zySysSwYear=_ZySysSwYear_Object((1,3,6,1,4,1,890,1,15,3,82,2,7),_ZySysSwYear_Type())
zySysSwYear.setMaxAccess(_C)
if mibBuilder.loadTexts:zySysSwYear.setStatus(_A)
_ZySysHwMajorVers_Type=Integer32
_ZySysHwMajorVers_Object=MibScalar
zySysHwMajorVers=_ZySysHwMajorVers_Object((1,3,6,1,4,1,890,1,15,3,82,2,8),_ZySysHwMajorVers_Type())
zySysHwMajorVers.setMaxAccess(_C)
if mibBuilder.loadTexts:zySysHwMajorVers.setStatus(_A)
_ZySysHwMinorVers_Type=Integer32
_ZySysHwMinorVers_Object=MibScalar
zySysHwMinorVers=_ZySysHwMinorVers_Object((1,3,6,1,4,1,890,1,15,3,82,2,9),_ZySysHwMinorVers_Type())
zySysHwMinorVers.setMaxAccess(_C)
if mibBuilder.loadTexts:zySysHwMinorVers.setStatus(_A)
_ZySysSerialNumber_Type=DisplayString
_ZySysSerialNumber_Object=MibScalar
zySysSerialNumber=_ZySysSerialNumber_Object((1,3,6,1,4,1,890,1,15,3,82,2,10),_ZySysSerialNumber_Type())
zySysSerialNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:zySysSerialNumber.setStatus(_A)
class _ZySysSwBootUpImage_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('image1',1),('image2',2)))
_ZySysSwBootUpImage_Type.__name__=_D
_ZySysSwBootUpImage_Object=MibScalar
zySysSwBootUpImage=_ZySysSwBootUpImage_Object((1,3,6,1,4,1,890,1,15,3,82,2,11),_ZySysSwBootUpImage_Type())
zySysSwBootUpImage.setMaxAccess(_C)
if mibBuilder.loadTexts:zySysSwBootUpImage.setStatus(_A)
_ZySysServiceStatus_Type=DisplayString
_ZySysServiceStatus_Object=MibScalar
zySysServiceStatus=_ZySysServiceStatus_Object((1,3,6,1,4,1,890,1,15,3,82,2,12),_ZySysServiceStatus_Type())
zySysServiceStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:zySysServiceStatus.setStatus(_A)
_ZySysRegisterMacAddress_Type=MacAddress
_ZySysRegisterMacAddress_Object=MibScalar
zySysRegisterMacAddress=_ZySysRegisterMacAddress_Object((1,3,6,1,4,1,890,1,15,3,82,2,13),_ZySysRegisterMacAddress_Type())
zySysRegisterMacAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:zySysRegisterMacAddress.setStatus(_A)
_ZyxelDateTimeTrapNotifications_ObjectIdentity=ObjectIdentity
zyxelDateTimeTrapNotifications=_ZyxelDateTimeTrapNotifications_ObjectIdentity((1,3,6,1,4,1,890,1,15,3,82,3))
zyDateTimeTrapTimeServerNotReachable=NotificationType((1,3,6,1,4,1,890,1,15,3,82,3,1))
if mibBuilder.loadTexts:zyDateTimeTrapTimeServerNotReachable.setStatus(_A)
zyDateTimeTrapTimeServerNotReachableRecovered=NotificationType((1,3,6,1,4,1,890,1,15,3,82,3,2))
if mibBuilder.loadTexts:zyDateTimeTrapTimeServerNotReachableRecovered.setStatus(_A)
mibBuilder.exportSymbols('ZYXEL-SYSTEM-MIB',**{'zyxelSystem':zyxelSystem,'zyxelDateTimeSetup':zyxelDateTimeSetup,'zyDateTimeServerType':zyDateTimeServerType,'zyDateTimeZone':zyDateTimeZone,'zyDateTimeNewDateYear':zyDateTimeNewDateYear,'zyDateTimeNewDateMonth':zyDateTimeNewDateMonth,'zyDateTimeNewDateDay':zyDateTimeNewDateDay,'zyDateTimeNewTimeHour':zyDateTimeNewTimeHour,'zyDateTimeNewTimeMinute':zyDateTimeNewTimeMinute,'zyDateTimeNewTimeSecond':zyDateTimeNewTimeSecond,'zyxelDateTimeDaylightSavingTimeSetup':zyxelDateTimeDaylightSavingTimeSetup,'zyDaylightSavingTimeState':zyDaylightSavingTimeState,'zyDaylightSavingTimeStartDateWeek':zyDaylightSavingTimeStartDateWeek,'zyDaylightSavingTimeStartDateDay':zyDaylightSavingTimeStartDateDay,'zyDaylightSavingTimeStartDateMonth':zyDaylightSavingTimeStartDateMonth,'zyDaylightSavingTimeStartDateHour':zyDaylightSavingTimeStartDateHour,'zyDaylightSavingTimeEndDateWeek':zyDaylightSavingTimeEndDateWeek,'zyDaylightSavingTimeEndDateDay':zyDaylightSavingTimeEndDateDay,'zyDaylightSavingTimeEndDateMonth':zyDaylightSavingTimeEndDateMonth,'zyDaylightSavingTimeEndDateHour':zyDaylightSavingTimeEndDateHour,'zyDateTimeServerInetAddressType':zyDateTimeServerInetAddressType,'zyDateTimeServerInetAddress':zyDateTimeServerInetAddress,'zyDateTimeZoneHourMinute':zyDateTimeZoneHourMinute,'zyDateTimeSyncInterval':zyDateTimeSyncInterval,'zyxelSysInfo':zyxelSysInfo,'zySysSwPlatformMajorVers':zySysSwPlatformMajorVers,'zySysSwPlatformMinorVers':zySysSwPlatformMinorVers,'zySysSwModelString':zySysSwModelString,'zySysSwVersionControlNbr':zySysSwVersionControlNbr,'zySysSwDay':zySysSwDay,'zySysSwMonth':zySysSwMonth,'zySysSwYear':zySysSwYear,'zySysHwMajorVers':zySysHwMajorVers,'zySysHwMinorVers':zySysHwMinorVers,'zySysSerialNumber':zySysSerialNumber,'zySysSwBootUpImage':zySysSwBootUpImage,'zySysServiceStatus':zySysServiceStatus,'zySysRegisterMacAddress':zySysRegisterMacAddress,'zyxelDateTimeTrapNotifications':zyxelDateTimeTrapNotifications,'zyDateTimeTrapTimeServerNotReachable':zyDateTimeTrapTimeServerNotReachable,'zyDateTimeTrapTimeServerNotReachableRecovered':zyDateTimeTrapTimeServerNotReachableRecovered})