_G='enabled'
_F='disabled'
_E='OctetString'
_D='Integer32'
_C='read-only'
_B='read-write'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_E,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
g6,=mibBuilder.importSymbols('MICROSENS-G6-MIB','g6')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,MacAddress,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress','TextualConvention')
management=ModuleIdentity((1,3,6,1,4,1,3181,10,6,3))
if mibBuilder.loadTexts:management.setRevisions(('2018-02-12 16:19',))
_Ntp_ObjectIdentity=ObjectIdentity
ntp=_Ntp_ObjectIdentity((1,3,6,1,4,1,3181,10,6,3,73))
class _NtpEnableNtp_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_F,0),(_G,1)))
_NtpEnableNtp_Type.__name__=_D
_NtpEnableNtp_Object=MibScalar
ntpEnableNtp=_NtpEnableNtp_Object((1,3,6,1,4,1,3181,10,6,3,73,1),_NtpEnableNtp_Type())
ntpEnableNtp.setMaxAccess(_B)
if mibBuilder.loadTexts:ntpEnableNtp.setStatus(_A)
_NtpSyncNow_Type=DisplayString
_NtpSyncNow_Object=MibScalar
ntpSyncNow=_NtpSyncNow_Object((1,3,6,1,4,1,3181,10,6,3,73,2),_NtpSyncNow_Type())
ntpSyncNow.setMaxAccess(_B)
if mibBuilder.loadTexts:ntpSyncNow.setStatus(_A)
class _NtpDhcpProvidesNtpServer_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_F,0),(_G,1)))
_NtpDhcpProvidesNtpServer_Type.__name__=_D
_NtpDhcpProvidesNtpServer_Object=MibScalar
ntpDhcpProvidesNtpServer=_NtpDhcpProvidesNtpServer_Object((1,3,6,1,4,1,3181,10,6,3,73,3),_NtpDhcpProvidesNtpServer_Type())
ntpDhcpProvidesNtpServer.setMaxAccess(_B)
if mibBuilder.loadTexts:ntpDhcpProvidesNtpServer.setStatus(_A)
_NtpMainNtpServer_Type=DisplayString
_NtpMainNtpServer_Object=MibScalar
ntpMainNtpServer=_NtpMainNtpServer_Object((1,3,6,1,4,1,3181,10,6,3,73,4),_NtpMainNtpServer_Type())
ntpMainNtpServer.setMaxAccess(_B)
if mibBuilder.loadTexts:ntpMainNtpServer.setStatus(_A)
_NtpBackupNtpServer_Type=DisplayString
_NtpBackupNtpServer_Object=MibScalar
ntpBackupNtpServer=_NtpBackupNtpServer_Object((1,3,6,1,4,1,3181,10,6,3,73,5),_NtpBackupNtpServer_Type())
ntpBackupNtpServer.setMaxAccess(_B)
if mibBuilder.loadTexts:ntpBackupNtpServer.setStatus(_A)
class _NtpTrustedServer_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_F,0),(_G,1)))
_NtpTrustedServer_Type.__name__=_D
_NtpTrustedServer_Object=MibScalar
ntpTrustedServer=_NtpTrustedServer_Object((1,3,6,1,4,1,3181,10,6,3,73,6),_NtpTrustedServer_Type())
ntpTrustedServer.setMaxAccess(_B)
if mibBuilder.loadTexts:ntpTrustedServer.setStatus(_A)
class _NtpSyncInterval_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_NtpSyncInterval_Type.__name__=_D
_NtpSyncInterval_Object=MibScalar
ntpSyncInterval=_NtpSyncInterval_Object((1,3,6,1,4,1,3181,10,6,3,73,7),_NtpSyncInterval_Type())
ntpSyncInterval.setMaxAccess(_B)
if mibBuilder.loadTexts:ntpSyncInterval.setStatus(_A)
_NtpShowTimeDate_Type=DisplayString
_NtpShowTimeDate_Object=MibScalar
ntpShowTimeDate=_NtpShowTimeDate_Object((1,3,6,1,4,1,3181,10,6,3,73,8),_NtpShowTimeDate_Type())
ntpShowTimeDate.setMaxAccess(_B)
if mibBuilder.loadTexts:ntpShowTimeDate.setStatus(_A)
_NtpListTimeZones_Type=DisplayString
_NtpListTimeZones_Object=MibScalar
ntpListTimeZones=_NtpListTimeZones_Object((1,3,6,1,4,1,3181,10,6,3,73,9),_NtpListTimeZones_Type())
ntpListTimeZones.setMaxAccess(_B)
if mibBuilder.loadTexts:ntpListTimeZones.setStatus(_A)
_NtpTimeZone_Type=DisplayString
_NtpTimeZone_Object=MibScalar
ntpTimeZone=_NtpTimeZone_Object((1,3,6,1,4,1,3181,10,6,3,73,10),_NtpTimeZone_Type())
ntpTimeZone.setMaxAccess(_B)
if mibBuilder.loadTexts:ntpTimeZone.setStatus(_A)
_NtpTimeFormat_Type=DisplayString
_NtpTimeFormat_Object=MibScalar
ntpTimeFormat=_NtpTimeFormat_Object((1,3,6,1,4,1,3181,10,6,3,73,11),_NtpTimeFormat_Type())
ntpTimeFormat.setMaxAccess(_B)
if mibBuilder.loadTexts:ntpTimeFormat.setStatus(_A)
_NtpDateFormat_Type=DisplayString
_NtpDateFormat_Object=MibScalar
ntpDateFormat=_NtpDateFormat_Object((1,3,6,1,4,1,3181,10,6,3,73,12),_NtpDateFormat_Type())
ntpDateFormat.setMaxAccess(_B)
if mibBuilder.loadTexts:ntpDateFormat.setStatus(_A)
class _NtpStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,4,16)));namedValues=NamedValues(*(('unset',0),('manuallySet',1),('synchronized',2),('syncFailed',4),('dayLightSavingTime',16)))
_NtpStatus_Type.__name__=_D
_NtpStatus_Object=MibScalar
ntpStatus=_NtpStatus_Object((1,3,6,1,4,1,3181,10,6,3,73,100),_NtpStatus_Type())
ntpStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:ntpStatus.setStatus(_A)
_NtpLocalTime_Type=DisplayString
_NtpLocalTime_Object=MibScalar
ntpLocalTime=_NtpLocalTime_Object((1,3,6,1,4,1,3181,10,6,3,73,101),_NtpLocalTime_Type())
ntpLocalTime.setMaxAccess(_C)
if mibBuilder.loadTexts:ntpLocalTime.setStatus(_A)
_NtpLocalDate_Type=DisplayString
_NtpLocalDate_Object=MibScalar
ntpLocalDate=_NtpLocalDate_Object((1,3,6,1,4,1,3181,10,6,3,73,102),_NtpLocalDate_Type())
ntpLocalDate.setMaxAccess(_C)
if mibBuilder.loadTexts:ntpLocalDate.setStatus(_A)
_NtpUsedNtpServer_Type=DisplayString
_NtpUsedNtpServer_Object=MibScalar
ntpUsedNtpServer=_NtpUsedNtpServer_Object((1,3,6,1,4,1,3181,10,6,3,73,103),_NtpUsedNtpServer_Type())
ntpUsedNtpServer.setMaxAccess(_C)
if mibBuilder.loadTexts:ntpUsedNtpServer.setStatus(_A)
class _NtpDynamicNtpServer1_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,20))
_NtpDynamicNtpServer1_Type.__name__=_E
_NtpDynamicNtpServer1_Object=MibScalar
ntpDynamicNtpServer1=_NtpDynamicNtpServer1_Object((1,3,6,1,4,1,3181,10,6,3,73,104),_NtpDynamicNtpServer1_Type())
ntpDynamicNtpServer1.setMaxAccess(_C)
if mibBuilder.loadTexts:ntpDynamicNtpServer1.setStatus(_A)
class _NtpDynamicNtpServer2_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,20))
_NtpDynamicNtpServer2_Type.__name__=_E
_NtpDynamicNtpServer2_Object=MibScalar
ntpDynamicNtpServer2=_NtpDynamicNtpServer2_Object((1,3,6,1,4,1,3181,10,6,3,73,105),_NtpDynamicNtpServer2_Type())
ntpDynamicNtpServer2.setMaxAccess(_C)
if mibBuilder.loadTexts:ntpDynamicNtpServer2.setStatus(_A)
class _NtpDynamicNtpServer3_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,20))
_NtpDynamicNtpServer3_Type.__name__=_E
_NtpDynamicNtpServer3_Object=MibScalar
ntpDynamicNtpServer3=_NtpDynamicNtpServer3_Object((1,3,6,1,4,1,3181,10,6,3,73,106),_NtpDynamicNtpServer3_Type())
ntpDynamicNtpServer3.setMaxAccess(_C)
if mibBuilder.loadTexts:ntpDynamicNtpServer3.setStatus(_A)
class _NtpDynamicNtpServer4_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,20))
_NtpDynamicNtpServer4_Type.__name__=_E
_NtpDynamicNtpServer4_Object=MibScalar
ntpDynamicNtpServer4=_NtpDynamicNtpServer4_Object((1,3,6,1,4,1,3181,10,6,3,73,107),_NtpDynamicNtpServer4_Type())
ntpDynamicNtpServer4.setMaxAccess(_C)
if mibBuilder.loadTexts:ntpDynamicNtpServer4.setStatus(_A)
mibBuilder.exportSymbols('G6-NTP-MIB',**{'management':management,'ntp':ntp,'ntpEnableNtp':ntpEnableNtp,'ntpSyncNow':ntpSyncNow,'ntpDhcpProvidesNtpServer':ntpDhcpProvidesNtpServer,'ntpMainNtpServer':ntpMainNtpServer,'ntpBackupNtpServer':ntpBackupNtpServer,'ntpTrustedServer':ntpTrustedServer,'ntpSyncInterval':ntpSyncInterval,'ntpShowTimeDate':ntpShowTimeDate,'ntpListTimeZones':ntpListTimeZones,'ntpTimeZone':ntpTimeZone,'ntpTimeFormat':ntpTimeFormat,'ntpDateFormat':ntpDateFormat,'ntpStatus':ntpStatus,'ntpLocalTime':ntpLocalTime,'ntpLocalDate':ntpLocalDate,'ntpUsedNtpServer':ntpUsedNtpServer,'ntpDynamicNtpServer1':ntpDynamicNtpServer1,'ntpDynamicNtpServer2':ntpDynamicNtpServer2,'ntpDynamicNtpServer3':ntpDynamicNtpServer3,'ntpDynamicNtpServer4':ntpDynamicNtpServer4})