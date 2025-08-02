_T='feSW26LoopDetectedfIndex'
_S='feSW26PortConfIndex'
_R='feSW26PortStatusIndex'
_Q='feSW26LogIndex'
_P='feSW26SMSUserIndex'
_O='feSW26EmailUserIndex'
_N='feSW26EventIndex'
_M='feSW26TrapHostIndex'
_L='feSW26AccountIndex'
_K='username'
_J='partnerkey'
_I='actorkey'
_H='groupId'
_G='ifIndex'
_F='IF-MIB'
_E='PRIVATE-FESW-26-MIB'
_D='read-only'
_C='Integer32'
_B='read-write'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ifIndex,=mibBuilder.importSymbols(_F,_G)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
privatetech=ModuleIdentity((1,3,6,1,4,1,5205))
_Switch_ObjectIdentity=ObjectIdentity
switch=_Switch_ObjectIdentity((1,3,6,1,4,1,5205,2))
_FeSW26ProductID_ObjectIdentity=ObjectIdentity
feSW26ProductID=_FeSW26ProductID_ObjectIdentity((1,3,6,1,4,1,5205,2,16))
_FeSW26Produces_ObjectIdentity=ObjectIdentity
feSW26Produces=_FeSW26Produces_ObjectIdentity((1,3,6,1,4,1,5205,2,16,1))
_FeSW26System_ObjectIdentity=ObjectIdentity
feSW26System=_FeSW26System_ObjectIdentity((1,3,6,1,4,1,5205,2,16,1,1))
_FeSW26CommonSys_ObjectIdentity=ObjectIdentity
feSW26CommonSys=_FeSW26CommonSys_ObjectIdentity((1,3,6,1,4,1,5205,2,16,1,1,1))
class _FeSW26Reboot_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1),ValueRangeConstraint(2,2))
_FeSW26Reboot_Type.__name__=_C
_FeSW26Reboot_Object=MibScalar
feSW26Reboot=_FeSW26Reboot_Object((1,3,6,1,4,1,5205,2,16,1,1,1,1),_FeSW26Reboot_Type())
feSW26Reboot.setMaxAccess(_B)
if mibBuilder.loadTexts:feSW26Reboot.setStatus(_A)
_FeSW26BiosVsersion_Type=DisplayString
_FeSW26BiosVsersion_Object=MibScalar
feSW26BiosVsersion=_FeSW26BiosVsersion_Object((1,3,6,1,4,1,5205,2,16,1,1,1,2),_FeSW26BiosVsersion_Type())
feSW26BiosVsersion.setMaxAccess(_D)
if mibBuilder.loadTexts:feSW26BiosVsersion.setStatus(_A)
_FeSW26FirmwareVersion_Type=DisplayString
_FeSW26FirmwareVersion_Object=MibScalar
feSW26FirmwareVersion=_FeSW26FirmwareVersion_Object((1,3,6,1,4,1,5205,2,16,1,1,1,3),_FeSW26FirmwareVersion_Type())
feSW26FirmwareVersion.setMaxAccess(_D)
if mibBuilder.loadTexts:feSW26FirmwareVersion.setStatus(_A)
_FeSW26HardwareVersion_Type=DisplayString
_FeSW26HardwareVersion_Object=MibScalar
feSW26HardwareVersion=_FeSW26HardwareVersion_Object((1,3,6,1,4,1,5205,2,16,1,1,1,4),_FeSW26HardwareVersion_Type())
feSW26HardwareVersion.setMaxAccess(_D)
if mibBuilder.loadTexts:feSW26HardwareVersion.setStatus(_A)
_FeSW26MechanicalVersion_Type=DisplayString
_FeSW26MechanicalVersion_Object=MibScalar
feSW26MechanicalVersion=_FeSW26MechanicalVersion_Object((1,3,6,1,4,1,5205,2,16,1,1,1,5),_FeSW26MechanicalVersion_Type())
feSW26MechanicalVersion.setMaxAccess(_D)
if mibBuilder.loadTexts:feSW26MechanicalVersion.setStatus(_A)
_FeSW26SerialNumber_Type=DisplayString
_FeSW26SerialNumber_Object=MibScalar
feSW26SerialNumber=_FeSW26SerialNumber_Object((1,3,6,1,4,1,5205,2,16,1,1,1,6),_FeSW26SerialNumber_Type())
feSW26SerialNumber.setMaxAccess(_D)
if mibBuilder.loadTexts:feSW26SerialNumber.setStatus(_A)
_FeSW26HostMacAddress_Type=DisplayString
_FeSW26HostMacAddress_Object=MibScalar
feSW26HostMacAddress=_FeSW26HostMacAddress_Object((1,3,6,1,4,1,5205,2,16,1,1,1,7),_FeSW26HostMacAddress_Type())
feSW26HostMacAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:feSW26HostMacAddress.setStatus(_A)
_FeSW26DevicePort_Type=DisplayString
_FeSW26DevicePort_Object=MibScalar
feSW26DevicePort=_FeSW26DevicePort_Object((1,3,6,1,4,1,5205,2,16,1,1,1,8),_FeSW26DevicePort_Type())
feSW26DevicePort.setMaxAccess(_D)
if mibBuilder.loadTexts:feSW26DevicePort.setStatus(_A)
_FeSW26RamSize_Type=DisplayString
_FeSW26RamSize_Object=MibScalar
feSW26RamSize=_FeSW26RamSize_Object((1,3,6,1,4,1,5205,2,16,1,1,1,9),_FeSW26RamSize_Type())
feSW26RamSize.setMaxAccess(_D)
if mibBuilder.loadTexts:feSW26RamSize.setStatus(_A)
_FeSW26FlashSize_Type=DisplayString
_FeSW26FlashSize_Object=MibScalar
feSW26FlashSize=_FeSW26FlashSize_Object((1,3,6,1,4,1,5205,2,16,1,1,1,10),_FeSW26FlashSize_Type())
feSW26FlashSize.setMaxAccess(_D)
if mibBuilder.loadTexts:feSW26FlashSize.setStatus(_A)
_FeSW26IP_ObjectIdentity=ObjectIdentity
feSW26IP=_FeSW26IP_ObjectIdentity((1,3,6,1,4,1,5205,2,16,1,1,2))
class _FeSW26DhcpSetting_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1))
_FeSW26DhcpSetting_Type.__name__=_C
_FeSW26DhcpSetting_Object=MibScalar
feSW26DhcpSetting=_FeSW26DhcpSetting_Object((1,3,6,1,4,1,5205,2,16,1,1,2,1),_FeSW26DhcpSetting_Type())
feSW26DhcpSetting.setMaxAccess(_B)
if mibBuilder.loadTexts:feSW26DhcpSetting.setStatus(_A)
_FeSW26IPAddress_Type=IpAddress
_FeSW26IPAddress_Object=MibScalar
feSW26IPAddress=_FeSW26IPAddress_Object((1,3,6,1,4,1,5205,2,16,1,1,2,2),_FeSW26IPAddress_Type())
feSW26IPAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:feSW26IPAddress.setStatus(_A)
_FeSW26NetMask_Type=IpAddress
_FeSW26NetMask_Object=MibScalar
feSW26NetMask=_FeSW26NetMask_Object((1,3,6,1,4,1,5205,2,16,1,1,2,3),_FeSW26NetMask_Type())
feSW26NetMask.setMaxAccess(_B)
if mibBuilder.loadTexts:feSW26NetMask.setStatus(_A)
_FeSW26DefaultGateway_Type=IpAddress
_FeSW26DefaultGateway_Object=MibScalar
feSW26DefaultGateway=_FeSW26DefaultGateway_Object((1,3,6,1,4,1,5205,2,16,1,1,2,4),_FeSW26DefaultGateway_Type())
feSW26DefaultGateway.setMaxAccess(_B)
if mibBuilder.loadTexts:feSW26DefaultGateway.setStatus(_A)
class _FeSW26DnsSetting_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1))
_FeSW26DnsSetting_Type.__name__=_C
_FeSW26DnsSetting_Object=MibScalar
feSW26DnsSetting=_FeSW26DnsSetting_Object((1,3,6,1,4,1,5205,2,16,1,1,2,5),_FeSW26DnsSetting_Type())
feSW26DnsSetting.setMaxAccess(_B)
if mibBuilder.loadTexts:feSW26DnsSetting.setStatus(_A)
_FeSW26DnsServer_Type=IpAddress
_FeSW26DnsServer_Object=MibScalar
feSW26DnsServer=_FeSW26DnsServer_Object((1,3,6,1,4,1,5205,2,16,1,1,2,6),_FeSW26DnsServer_Type())
feSW26DnsServer.setMaxAccess(_B)
if mibBuilder.loadTexts:feSW26DnsServer.setStatus(_A)
_FeSW26Time_ObjectIdentity=ObjectIdentity
feSW26Time=_FeSW26Time_ObjectIdentity((1,3,6,1,4,1,5205,2,16,1,1,3))
_FeSW26SystemCurrentTime_Type=DisplayString
_FeSW26SystemCurrentTime_Object=MibScalar
feSW26SystemCurrentTime=_FeSW26SystemCurrentTime_Object((1,3,6,1,4,1,5205,2,16,1,1,3,1),_FeSW26SystemCurrentTime_Type())
feSW26SystemCurrentTime.setMaxAccess(_D)
if mibBuilder.loadTexts:feSW26SystemCurrentTime.setStatus(_A)
_FeSW26ManualTimeSetting_Type=DisplayString
_FeSW26ManualTimeSetting_Object=MibScalar
feSW26ManualTimeSetting=_FeSW26ManualTimeSetting_Object((1,3,6,1,4,1,5205,2,16,1,1,3,2),_FeSW26ManualTimeSetting_Type())
feSW26ManualTimeSetting.setMaxAccess(_B)
if mibBuilder.loadTexts:feSW26ManualTimeSetting.setStatus(_A)
_FeSW26NTPServer_Type=DisplayString
_FeSW26NTPServer_Object=MibScalar
feSW26NTPServer=_FeSW26NTPServer_Object((1,3,6,1,4,1,5205,2,16,1,1,3,3),_FeSW26NTPServer_Type())
feSW26NTPServer.setMaxAccess(_B)
if mibBuilder.loadTexts:feSW26NTPServer.setStatus(_A)
class _FeSW26NTPTimeZone_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-12,13))
_FeSW26NTPTimeZone_Type.__name__=_C
_FeSW26NTPTimeZone_Object=MibScalar
feSW26NTPTimeZone=_FeSW26NTPTimeZone_Object((1,3,6,1,4,1,5205,2,16,1,1,3,4),_FeSW26NTPTimeZone_Type())
feSW26NTPTimeZone.setMaxAccess(_B)
if mibBuilder.loadTexts:feSW26NTPTimeZone.setStatus(_A)
class _FeSW26NTPTimeSync_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1))
_FeSW26NTPTimeSync_Type.__name__=_C
_FeSW26NTPTimeSync_Object=MibScalar
feSW26NTPTimeSync=_FeSW26NTPTimeSync_Object((1,3,6,1,4,1,5205,2,16,1,1,3,5),_FeSW26NTPTimeSync_Type())
feSW26NTPTimeSync.setMaxAccess(_B)
if mibBuilder.loadTexts:feSW26NTPTimeSync.setStatus(_A)
class _FeSW26DaylightSavingTime_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-5,5))
_FeSW26DaylightSavingTime_Type.__name__=_C
_FeSW26DaylightSavingTime_Object=MibScalar
feSW26DaylightSavingTime=_FeSW26DaylightSavingTime_Object((1,3,6,1,4,1,5205,2,16,1,1,3,6),_FeSW26DaylightSavingTime_Type())
feSW26DaylightSavingTime.setMaxAccess(_B)
if mibBuilder.loadTexts:feSW26DaylightSavingTime.setStatus(_A)
_FeSW26DaylightStartTime_Type=DisplayString
_FeSW26DaylightStartTime_Object=MibScalar
feSW26DaylightStartTime=_FeSW26DaylightStartTime_Object((1,3,6,1,4,1,5205,2,16,1,1,3,7),_FeSW26DaylightStartTime_Type())
feSW26DaylightStartTime.setMaxAccess(_B)
if mibBuilder.loadTexts:feSW26DaylightStartTime.setStatus(_A)
_FeSW26DaylightEndTime_Type=DisplayString
_FeSW26DaylightEndTime_Object=MibScalar
feSW26DaylightEndTime=_FeSW26DaylightEndTime_Object((1,3,6,1,4,1,5205,2,16,1,1,3,8),_FeSW26DaylightEndTime_Type())
feSW26DaylightEndTime.setMaxAccess(_B)
if mibBuilder.loadTexts:feSW26DaylightEndTime.setStatus(_A)
_FeSW26Account_ObjectIdentity=ObjectIdentity
feSW26Account=_FeSW26Account_ObjectIdentity((1,3,6,1,4,1,5205,2,16,1,1,4))
class _FeSW26AccountNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,5))
_FeSW26AccountNumber_Type.__name__=_C
_FeSW26AccountNumber_Object=MibScalar
feSW26AccountNumber=_FeSW26AccountNumber_Object((1,3,6,1,4,1,5205,2,16,1,1,4,1),_FeSW26AccountNumber_Type())
feSW26AccountNumber.setMaxAccess(_D)
if mibBuilder.loadTexts:feSW26AccountNumber.setStatus(_A)
_FeSW26AccountTable_Object=MibTable
feSW26AccountTable=_FeSW26AccountTable_Object((1,3,6,1,4,1,5205,2,16,1,1,4,2))
if mibBuilder.loadTexts:feSW26AccountTable.setStatus(_A)
_FeSW26AccountEntry_Object=MibTableRow
feSW26AccountEntry=_FeSW26AccountEntry_Object((1,3,6,1,4,1,5205,2,16,1,1,4,2,1))
feSW26AccountEntry.setIndexNames((0,_E,_L))
if mibBuilder.loadTexts:feSW26AccountEntry.setStatus(_A)
class _FeSW26AccountIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,5))
_FeSW26AccountIndex_Type.__name__=_C
_FeSW26AccountIndex_Object=MibTableColumn
feSW26AccountIndex=_FeSW26AccountIndex_Object((1,3,6,1,4,1,5205,2,16,1,1,4,2,1,1),_FeSW26AccountIndex_Type())
feSW26AccountIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:feSW26AccountIndex.setStatus(_A)
_FeSW26AccountAuthorization_Type=DisplayString
_FeSW26AccountAuthorization_Object=MibTableColumn
feSW26AccountAuthorization=_FeSW26AccountAuthorization_Object((1,3,6,1,4,1,5205,2,16,1,1,4,2,1,2),_FeSW26AccountAuthorization_Type())
feSW26AccountAuthorization.setMaxAccess(_D)
if mibBuilder.loadTexts:feSW26AccountAuthorization.setStatus(_A)
_FeSW26AccountName_Type=DisplayString
_FeSW26AccountName_Object=MibTableColumn
feSW26AccountName=_FeSW26AccountName_Object((1,3,6,1,4,1,5205,2,16,1,1,4,2,1,3),_FeSW26AccountName_Type())
feSW26AccountName.setMaxAccess(_B)
if mibBuilder.loadTexts:feSW26AccountName.setStatus(_A)
_FeSW26AccountPassword_Type=DisplayString
_FeSW26AccountPassword_Object=MibTableColumn
feSW26AccountPassword=_FeSW26AccountPassword_Object((1,3,6,1,4,1,5205,2,16,1,1,4,2,1,4),_FeSW26AccountPassword_Type())
feSW26AccountPassword.setMaxAccess(_B)
if mibBuilder.loadTexts:feSW26AccountPassword.setStatus(_A)
_FeSW26AccountAddName_Type=DisplayString
_FeSW26AccountAddName_Object=MibScalar
feSW26AccountAddName=_FeSW26AccountAddName_Object((1,3,6,1,4,1,5205,2,16,1,1,4,3),_FeSW26AccountAddName_Type())
feSW26AccountAddName.setMaxAccess(_B)
if mibBuilder.loadTexts:feSW26AccountAddName.setStatus(_A)
_FeSW26AccountAddPassword_Type=DisplayString
_FeSW26AccountAddPassword_Object=MibScalar
feSW26AccountAddPassword=_FeSW26AccountAddPassword_Object((1,3,6,1,4,1,5205,2,16,1,1,4,4),_FeSW26AccountAddPassword_Type())
feSW26AccountAddPassword.setMaxAccess(_B)
if mibBuilder.loadTexts:feSW26AccountAddPassword.setStatus(_A)
class _FeSW26DoAccountAdd_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1))
_FeSW26DoAccountAdd_Type.__name__=_C
_FeSW26DoAccountAdd_Object=MibScalar
feSW26DoAccountAdd=_FeSW26DoAccountAdd_Object((1,3,6,1,4,1,5205,2,16,1,1,4,5),_FeSW26DoAccountAdd_Type())
feSW26DoAccountAdd.setMaxAccess(_B)
if mibBuilder.loadTexts:feSW26DoAccountAdd.setStatus(_A)
class _FeSW26AccountDel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(2,5))
_FeSW26AccountDel_Type.__name__=_C
_FeSW26AccountDel_Object=MibScalar
feSW26AccountDel=_FeSW26AccountDel_Object((1,3,6,1,4,1,5205,2,16,1,1,4,6),_FeSW26AccountDel_Type())
feSW26AccountDel.setMaxAccess(_B)
if mibBuilder.loadTexts:feSW26AccountDel.setStatus(_A)
_FeSW26Snmp_ObjectIdentity=ObjectIdentity
feSW26Snmp=_FeSW26Snmp_ObjectIdentity((1,3,6,1,4,1,5205,2,16,1,2))
_FeSW26GetCommunity_Type=DisplayString
_FeSW26GetCommunity_Object=MibScalar
feSW26GetCommunity=_FeSW26GetCommunity_Object((1,3,6,1,4,1,5205,2,16,1,2,1),_FeSW26GetCommunity_Type())
feSW26GetCommunity.setMaxAccess(_B)
if mibBuilder.loadTexts:feSW26GetCommunity.setStatus(_A)
_FeSW26SetCommunity_Type=DisplayString
_FeSW26SetCommunity_Object=MibScalar
feSW26SetCommunity=_FeSW26SetCommunity_Object((1,3,6,1,4,1,5205,2,16,1,2,2),_FeSW26SetCommunity_Type())
feSW26SetCommunity.setMaxAccess(_B)
if mibBuilder.loadTexts:feSW26SetCommunity.setStatus(_A)
class _FeSW26TrapHostNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,6))
_FeSW26TrapHostNumber_Type.__name__=_C
_FeSW26TrapHostNumber_Object=MibScalar
feSW26TrapHostNumber=_FeSW26TrapHostNumber_Object((1,3,6,1,4,1,5205,2,16,1,2,3),_FeSW26TrapHostNumber_Type())
feSW26TrapHostNumber.setMaxAccess(_D)
if mibBuilder.loadTexts:feSW26TrapHostNumber.setStatus(_A)
_FeSW26TrapHostTable_Object=MibTable
feSW26TrapHostTable=_FeSW26TrapHostTable_Object((1,3,6,1,4,1,5205,2,16,1,2,4))
if mibBuilder.loadTexts:feSW26TrapHostTable.setStatus(_A)
_FeSW26TrapHostEntry_Object=MibTableRow
feSW26TrapHostEntry=_FeSW26TrapHostEntry_Object((1,3,6,1,4,1,5205,2,16,1,2,4,1))
feSW26TrapHostEntry.setIndexNames((0,_E,_M))
if mibBuilder.loadTexts:feSW26TrapHostEntry.setStatus(_A)
class _FeSW26TrapHostIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,6))
_FeSW26TrapHostIndex_Type.__name__=_C
_FeSW26TrapHostIndex_Object=MibTableColumn
feSW26TrapHostIndex=_FeSW26TrapHostIndex_Object((1,3,6,1,4,1,5205,2,16,1,2,4,1,1),_FeSW26TrapHostIndex_Type())
feSW26TrapHostIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:feSW26TrapHostIndex.setStatus(_A)
_FeSW26TrapHostIP_Type=IpAddress
_FeSW26TrapHostIP_Object=MibTableColumn
feSW26TrapHostIP=_FeSW26TrapHostIP_Object((1,3,6,1,4,1,5205,2,16,1,2,4,1,2),_FeSW26TrapHostIP_Type())
feSW26TrapHostIP.setMaxAccess(_B)
if mibBuilder.loadTexts:feSW26TrapHostIP.setStatus(_A)
class _FeSW26TrapHostPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_FeSW26TrapHostPort_Type.__name__=_C
_FeSW26TrapHostPort_Object=MibTableColumn
feSW26TrapHostPort=_FeSW26TrapHostPort_Object((1,3,6,1,4,1,5205,2,16,1,2,4,1,3),_FeSW26TrapHostPort_Type())
feSW26TrapHostPort.setMaxAccess(_B)
if mibBuilder.loadTexts:feSW26TrapHostPort.setStatus(_A)
_FeSW26TrapHostCommunity_Type=DisplayString
_FeSW26TrapHostCommunity_Object=MibTableColumn
feSW26TrapHostCommunity=_FeSW26TrapHostCommunity_Object((1,3,6,1,4,1,5205,2,16,1,2,4,1,4),_FeSW26TrapHostCommunity_Type())
feSW26TrapHostCommunity.setMaxAccess(_B)
if mibBuilder.loadTexts:feSW26TrapHostCommunity.setStatus(_A)
_FeSW26Alarm_ObjectIdentity=ObjectIdentity
feSW26Alarm=_FeSW26Alarm_ObjectIdentity((1,3,6,1,4,1,5205,2,16,1,3))
_FeSW26Event_ObjectIdentity=ObjectIdentity
feSW26Event=_FeSW26Event_ObjectIdentity((1,3,6,1,4,1,5205,2,16,1,3,1))
class _FeSW26EventNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_FeSW26EventNumber_Type.__name__=_C
_FeSW26EventNumber_Object=MibScalar
feSW26EventNumber=_FeSW26EventNumber_Object((1,3,6,1,4,1,5205,2,16,1,3,1,1),_FeSW26EventNumber_Type())
feSW26EventNumber.setMaxAccess(_D)
if mibBuilder.loadTexts:feSW26EventNumber.setStatus(_A)
_FeSW26EventTable_Object=MibTable
feSW26EventTable=_FeSW26EventTable_Object((1,3,6,1,4,1,5205,2,16,1,3,1,2))
if mibBuilder.loadTexts:feSW26EventTable.setStatus(_A)
_FeSW26EventEntry_Object=MibTableRow
feSW26EventEntry=_FeSW26EventEntry_Object((1,3,6,1,4,1,5205,2,16,1,3,1,2,1))
feSW26EventEntry.setIndexNames((0,_E,_N))
if mibBuilder.loadTexts:feSW26EventEntry.setStatus(_A)
class _FeSW26EventIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_FeSW26EventIndex_Type.__name__=_C
_FeSW26EventIndex_Object=MibTableColumn
feSW26EventIndex=_FeSW26EventIndex_Object((1,3,6,1,4,1,5205,2,16,1,3,1,2,1,1),_FeSW26EventIndex_Type())
feSW26EventIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:feSW26EventIndex.setStatus(_A)
_FeSW26EventName_Type=DisplayString
_FeSW26EventName_Object=MibTableColumn
feSW26EventName=_FeSW26EventName_Object((1,3,6,1,4,1,5205,2,16,1,3,1,2,1,2),_FeSW26EventName_Type())
feSW26EventName.setMaxAccess(_D)
if mibBuilder.loadTexts:feSW26EventName.setStatus(_A)
class _FeSW26EventSendEmail_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1))
_FeSW26EventSendEmail_Type.__name__=_C
_FeSW26EventSendEmail_Object=MibTableColumn
feSW26EventSendEmail=_FeSW26EventSendEmail_Object((1,3,6,1,4,1,5205,2,16,1,3,1,2,1,3),_FeSW26EventSendEmail_Type())
feSW26EventSendEmail.setMaxAccess(_B)
if mibBuilder.loadTexts:feSW26EventSendEmail.setStatus(_A)
class _FeSW26EventSendSMS_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1))
_FeSW26EventSendSMS_Type.__name__=_C
_FeSW26EventSendSMS_Object=MibTableColumn
feSW26EventSendSMS=_FeSW26EventSendSMS_Object((1,3,6,1,4,1,5205,2,16,1,3,1,2,1,4),_FeSW26EventSendSMS_Type())
feSW26EventSendSMS.setMaxAccess(_B)
if mibBuilder.loadTexts:feSW26EventSendSMS.setStatus(_A)
class _FeSW26EventSendTrap_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1))
_FeSW26EventSendTrap_Type.__name__=_C
_FeSW26EventSendTrap_Object=MibTableColumn
feSW26EventSendTrap=_FeSW26EventSendTrap_Object((1,3,6,1,4,1,5205,2,16,1,3,1,2,1,5),_FeSW26EventSendTrap_Type())
feSW26EventSendTrap.setMaxAccess(_B)
if mibBuilder.loadTexts:feSW26EventSendTrap.setStatus(_A)
_FeSW26Email_ObjectIdentity=ObjectIdentity
feSW26Email=_FeSW26Email_ObjectIdentity((1,3,6,1,4,1,5205,2,16,1,3,2))
_FeSW26EmailServer_Type=DisplayString
_FeSW26EmailServer_Object=MibScalar
feSW26EmailServer=_FeSW26EmailServer_Object((1,3,6,1,4,1,5205,2,16,1,3,2,1),_FeSW26EmailServer_Type())
feSW26EmailServer.setMaxAccess(_B)
if mibBuilder.loadTexts:feSW26EmailServer.setStatus(_A)
_FeSW26EmailUsername_Type=DisplayString
_FeSW26EmailUsername_Object=MibScalar
feSW26EmailUsername=_FeSW26EmailUsername_Object((1,3,6,1,4,1,5205,2,16,1,3,2,2),_FeSW26EmailUsername_Type())
feSW26EmailUsername.setMaxAccess(_B)
if mibBuilder.loadTexts:feSW26EmailUsername.setStatus(_A)
_FeSW26EmailPassword_Type=DisplayString
_FeSW26EmailPassword_Object=MibScalar
feSW26EmailPassword=_FeSW26EmailPassword_Object((1,3,6,1,4,1,5205,2,16,1,3,2,3),_FeSW26EmailPassword_Type())
feSW26EmailPassword.setMaxAccess(_B)
if mibBuilder.loadTexts:feSW26EmailPassword.setStatus(_A)
class _FeSW26EmailUserNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,6))
_FeSW26EmailUserNumber_Type.__name__=_C
_FeSW26EmailUserNumber_Object=MibScalar
feSW26EmailUserNumber=_FeSW26EmailUserNumber_Object((1,3,6,1,4,1,5205,2,16,1,3,2,4),_FeSW26EmailUserNumber_Type())
feSW26EmailUserNumber.setMaxAccess(_D)
if mibBuilder.loadTexts:feSW26EmailUserNumber.setStatus(_A)
_FeSW26EmailUserTable_Object=MibTable
feSW26EmailUserTable=_FeSW26EmailUserTable_Object((1,3,6,1,4,1,5205,2,16,1,3,2,5))
if mibBuilder.loadTexts:feSW26EmailUserTable.setStatus(_A)
_FeSW26EmailUserEntry_Object=MibTableRow
feSW26EmailUserEntry=_FeSW26EmailUserEntry_Object((1,3,6,1,4,1,5205,2,16,1,3,2,5,1))
feSW26EmailUserEntry.setIndexNames((0,_E,_O))
if mibBuilder.loadTexts:feSW26EmailUserEntry.setStatus(_A)
class _FeSW26EmailUserIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,6))
_FeSW26EmailUserIndex_Type.__name__=_C
_FeSW26EmailUserIndex_Object=MibTableColumn
feSW26EmailUserIndex=_FeSW26EmailUserIndex_Object((1,3,6,1,4,1,5205,2,16,1,3,2,5,1,1),_FeSW26EmailUserIndex_Type())
feSW26EmailUserIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:feSW26EmailUserIndex.setStatus(_A)
_FeSW26EmailUserAddress_Type=DisplayString
_FeSW26EmailUserAddress_Object=MibTableColumn
feSW26EmailUserAddress=_FeSW26EmailUserAddress_Object((1,3,6,1,4,1,5205,2,16,1,3,2,5,1,2),_FeSW26EmailUserAddress_Type())
feSW26EmailUserAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:feSW26EmailUserAddress.setStatus(_A)
_FeSW26SMS_ObjectIdentity=ObjectIdentity
feSW26SMS=_FeSW26SMS_ObjectIdentity((1,3,6,1,4,1,5205,2,16,1,3,3))
_FeSW26SMSServer_Type=DisplayString
_FeSW26SMSServer_Object=MibScalar
feSW26SMSServer=_FeSW26SMSServer_Object((1,3,6,1,4,1,5205,2,16,1,3,3,1),_FeSW26SMSServer_Type())
feSW26SMSServer.setMaxAccess(_B)
if mibBuilder.loadTexts:feSW26SMSServer.setStatus(_A)
_FeSW26SMSUsername_Type=DisplayString
_FeSW26SMSUsername_Object=MibScalar
feSW26SMSUsername=_FeSW26SMSUsername_Object((1,3,6,1,4,1,5205,2,16,1,3,3,2),_FeSW26SMSUsername_Type())
feSW26SMSUsername.setMaxAccess(_B)
if mibBuilder.loadTexts:feSW26SMSUsername.setStatus(_A)
_FeSW26SMSPassword_Type=DisplayString
_FeSW26SMSPassword_Object=MibScalar
feSW26SMSPassword=_FeSW26SMSPassword_Object((1,3,6,1,4,1,5205,2,16,1,3,3,3),_FeSW26SMSPassword_Type())
feSW26SMSPassword.setMaxAccess(_B)
if mibBuilder.loadTexts:feSW26SMSPassword.setStatus(_A)
class _FeSW26SMSUserNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,6))
_FeSW26SMSUserNumber_Type.__name__=_C
_FeSW26SMSUserNumber_Object=MibScalar
feSW26SMSUserNumber=_FeSW26SMSUserNumber_Object((1,3,6,1,4,1,5205,2,16,1,3,3,4),_FeSW26SMSUserNumber_Type())
feSW26SMSUserNumber.setMaxAccess(_D)
if mibBuilder.loadTexts:feSW26SMSUserNumber.setStatus(_A)
_FeSW26SMSUserTable_Object=MibTable
feSW26SMSUserTable=_FeSW26SMSUserTable_Object((1,3,6,1,4,1,5205,2,16,1,3,3,5))
if mibBuilder.loadTexts:feSW26SMSUserTable.setStatus(_A)
_FeSW26SMSUserEntry_Object=MibTableRow
feSW26SMSUserEntry=_FeSW26SMSUserEntry_Object((1,3,6,1,4,1,5205,2,16,1,3,3,5,1))
feSW26SMSUserEntry.setIndexNames((0,_E,_P))
if mibBuilder.loadTexts:feSW26SMSUserEntry.setStatus(_A)
class _FeSW26SMSUserIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,6))
_FeSW26SMSUserIndex_Type.__name__=_C
_FeSW26SMSUserIndex_Object=MibTableColumn
feSW26SMSUserIndex=_FeSW26SMSUserIndex_Object((1,3,6,1,4,1,5205,2,16,1,3,3,5,1,1),_FeSW26SMSUserIndex_Type())
feSW26SMSUserIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:feSW26SMSUserIndex.setStatus(_A)
_FeSW26SMSUserMobilePhone_Type=DisplayString
_FeSW26SMSUserMobilePhone_Object=MibTableColumn
feSW26SMSUserMobilePhone=_FeSW26SMSUserMobilePhone_Object((1,3,6,1,4,1,5205,2,16,1,3,3,5,1,2),_FeSW26SMSUserMobilePhone_Type())
feSW26SMSUserMobilePhone.setMaxAccess(_B)
if mibBuilder.loadTexts:feSW26SMSUserMobilePhone.setStatus(_A)
_FeSW26Tftp_ObjectIdentity=ObjectIdentity
feSW26Tftp=_FeSW26Tftp_ObjectIdentity((1,3,6,1,4,1,5205,2,16,1,4))
_FeSW26TftpServer_Type=IpAddress
_FeSW26TftpServer_Object=MibScalar
feSW26TftpServer=_FeSW26TftpServer_Object((1,3,6,1,4,1,5205,2,16,1,4,1),_FeSW26TftpServer_Type())
feSW26TftpServer.setMaxAccess(_B)
if mibBuilder.loadTexts:feSW26TftpServer.setStatus(_A)
_FeSW26Configuration_ObjectIdentity=ObjectIdentity
feSW26Configuration=_FeSW26Configuration_ObjectIdentity((1,3,6,1,4,1,5205,2,16,1,5))
_FeSW26SaveRestore_ObjectIdentity=ObjectIdentity
feSW26SaveRestore=_FeSW26SaveRestore_ObjectIdentity((1,3,6,1,4,1,5205,2,16,1,5,1))
class _FeSW26SaveStart_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1))
_FeSW26SaveStart_Type.__name__=_C
_FeSW26SaveStart_Object=MibScalar
feSW26SaveStart=_FeSW26SaveStart_Object((1,3,6,1,4,1,5205,2,16,1,5,1,1),_FeSW26SaveStart_Type())
feSW26SaveStart.setMaxAccess(_B)
if mibBuilder.loadTexts:feSW26SaveStart.setStatus(_A)
class _FeSW26SaveUser_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1))
_FeSW26SaveUser_Type.__name__=_C
_FeSW26SaveUser_Object=MibScalar
feSW26SaveUser=_FeSW26SaveUser_Object((1,3,6,1,4,1,5205,2,16,1,5,1,2),_FeSW26SaveUser_Type())
feSW26SaveUser.setMaxAccess(_B)
if mibBuilder.loadTexts:feSW26SaveUser.setStatus(_A)
class _FeSW26RestoreDefault_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1),ValueRangeConstraint(2,2))
_FeSW26RestoreDefault_Type.__name__=_C
_FeSW26RestoreDefault_Object=MibScalar
feSW26RestoreDefault=_FeSW26RestoreDefault_Object((1,3,6,1,4,1,5205,2,16,1,5,1,3),_FeSW26RestoreDefault_Type())
feSW26RestoreDefault.setMaxAccess(_B)
if mibBuilder.loadTexts:feSW26RestoreDefault.setStatus(_A)
class _FeSW26RestoreUser_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1))
_FeSW26RestoreUser_Type.__name__=_C
_FeSW26RestoreUser_Object=MibScalar
feSW26RestoreUser=_FeSW26RestoreUser_Object((1,3,6,1,4,1,5205,2,16,1,5,1,4),_FeSW26RestoreUser_Type())
feSW26RestoreUser.setMaxAccess(_B)
if mibBuilder.loadTexts:feSW26RestoreUser.setStatus(_A)
_FeSW26ConfigFile_ObjectIdentity=ObjectIdentity
feSW26ConfigFile=_FeSW26ConfigFile_ObjectIdentity((1,3,6,1,4,1,5205,2,16,1,5,2))
_FeSW26ExportConfigName_Type=DisplayString
_FeSW26ExportConfigName_Object=MibScalar
feSW26ExportConfigName=_FeSW26ExportConfigName_Object((1,3,6,1,4,1,5205,2,16,1,5,2,1),_FeSW26ExportConfigName_Type())
feSW26ExportConfigName.setMaxAccess(_B)
if mibBuilder.loadTexts:feSW26ExportConfigName.setStatus(_A)
class _FeSW26DoExportConfig_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1),ValueRangeConstraint(2,2))
_FeSW26DoExportConfig_Type.__name__=_C
_FeSW26DoExportConfig_Object=MibScalar
feSW26DoExportConfig=_FeSW26DoExportConfig_Object((1,3,6,1,4,1,5205,2,16,1,5,2,2),_FeSW26DoExportConfig_Type())
feSW26DoExportConfig.setMaxAccess(_B)
if mibBuilder.loadTexts:feSW26DoExportConfig.setStatus(_A)
_FeSW26ImportConfigName_Type=DisplayString
_FeSW26ImportConfigName_Object=MibScalar
feSW26ImportConfigName=_FeSW26ImportConfigName_Object((1,3,6,1,4,1,5205,2,16,1,5,2,3),_FeSW26ImportConfigName_Type())
feSW26ImportConfigName.setMaxAccess(_B)
if mibBuilder.loadTexts:feSW26ImportConfigName.setStatus(_A)
class _FeSW26DoImportConfig_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1),ValueRangeConstraint(2,2))
_FeSW26DoImportConfig_Type.__name__=_C
_FeSW26DoImportConfig_Object=MibScalar
feSW26DoImportConfig=_FeSW26DoImportConfig_Object((1,3,6,1,4,1,5205,2,16,1,5,2,4),_FeSW26DoImportConfig_Type())
feSW26DoImportConfig.setMaxAccess(_B)
if mibBuilder.loadTexts:feSW26DoImportConfig.setStatus(_A)
_FeSW26Diagnostic_ObjectIdentity=ObjectIdentity
feSW26Diagnostic=_FeSW26Diagnostic_ObjectIdentity((1,3,6,1,4,1,5205,2,16,1,6))
_FeSW26EEPROMTest_Type=DisplayString
_FeSW26EEPROMTest_Object=MibScalar
feSW26EEPROMTest=_FeSW26EEPROMTest_Object((1,3,6,1,4,1,5205,2,16,1,6,1),_FeSW26EEPROMTest_Type())
feSW26EEPROMTest.setMaxAccess(_D)
if mibBuilder.loadTexts:feSW26EEPROMTest.setStatus(_A)
_FeSW26UartTest_Type=DisplayString
_FeSW26UartTest_Object=MibScalar
feSW26UartTest=_FeSW26UartTest_Object((1,3,6,1,4,1,5205,2,16,1,6,2),_FeSW26UartTest_Type())
feSW26UartTest.setMaxAccess(_D)
if mibBuilder.loadTexts:feSW26UartTest.setStatus(_A)
_FeSW26DramTest_Type=DisplayString
_FeSW26DramTest_Object=MibScalar
feSW26DramTest=_FeSW26DramTest_Object((1,3,6,1,4,1,5205,2,16,1,6,3),_FeSW26DramTest_Type())
feSW26DramTest.setMaxAccess(_D)
if mibBuilder.loadTexts:feSW26DramTest.setStatus(_A)
_FeSW26FlashTest_Type=DisplayString
_FeSW26FlashTest_Object=MibScalar
feSW26FlashTest=_FeSW26FlashTest_Object((1,3,6,1,4,1,5205,2,16,1,6,4),_FeSW26FlashTest_Type())
feSW26FlashTest.setMaxAccess(_D)
if mibBuilder.loadTexts:feSW26FlashTest.setStatus(_A)
_FeSW26InternalLoopbackTest_Type=DisplayString
_FeSW26InternalLoopbackTest_Object=MibScalar
feSW26InternalLoopbackTest=_FeSW26InternalLoopbackTest_Object((1,3,6,1,4,1,5205,2,16,1,6,5),_FeSW26InternalLoopbackTest_Type())
feSW26InternalLoopbackTest.setMaxAccess(_D)
if mibBuilder.loadTexts:feSW26InternalLoopbackTest.setStatus(_A)
_FeSW26ExternalLoopbackTest_Type=DisplayString
_FeSW26ExternalLoopbackTest_Object=MibScalar
feSW26ExternalLoopbackTest=_FeSW26ExternalLoopbackTest_Object((1,3,6,1,4,1,5205,2,16,1,6,6),_FeSW26ExternalLoopbackTest_Type())
feSW26ExternalLoopbackTest.setMaxAccess(_D)
if mibBuilder.loadTexts:feSW26ExternalLoopbackTest.setStatus(_A)
_FeSW26PingTest_Type=DisplayString
_FeSW26PingTest_Object=MibScalar
feSW26PingTest=_FeSW26PingTest_Object((1,3,6,1,4,1,5205,2,16,1,6,7),_FeSW26PingTest_Type())
feSW26PingTest.setMaxAccess(_B)
if mibBuilder.loadTexts:feSW26PingTest.setStatus(_A)
_FeSW26Log_ObjectIdentity=ObjectIdentity
feSW26Log=_FeSW26Log_ObjectIdentity((1,3,6,1,4,1,5205,2,16,1,7))
class _FeSW26ClearLog_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1))
_FeSW26ClearLog_Type.__name__=_C
_FeSW26ClearLog_Object=MibScalar
feSW26ClearLog=_FeSW26ClearLog_Object((1,3,6,1,4,1,5205,2,16,1,7,1),_FeSW26ClearLog_Type())
feSW26ClearLog.setMaxAccess(_B)
if mibBuilder.loadTexts:feSW26ClearLog.setStatus(_A)
class _FeSW26UploadLog_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1))
_FeSW26UploadLog_Type.__name__=_C
_FeSW26UploadLog_Object=MibScalar
feSW26UploadLog=_FeSW26UploadLog_Object((1,3,6,1,4,1,5205,2,16,1,7,2),_FeSW26UploadLog_Type())
feSW26UploadLog.setMaxAccess(_B)
if mibBuilder.loadTexts:feSW26UploadLog.setStatus(_A)
class _FeSW26AutoUploadLogState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1))
_FeSW26AutoUploadLogState_Type.__name__=_C
_FeSW26AutoUploadLogState_Object=MibScalar
feSW26AutoUploadLogState=_FeSW26AutoUploadLogState_Object((1,3,6,1,4,1,5205,2,16,1,7,3),_FeSW26AutoUploadLogState_Type())
feSW26AutoUploadLogState.setMaxAccess(_B)
if mibBuilder.loadTexts:feSW26AutoUploadLogState.setStatus(_A)
class _FeSW26LogNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,120))
_FeSW26LogNumber_Type.__name__=_C
_FeSW26LogNumber_Object=MibScalar
feSW26LogNumber=_FeSW26LogNumber_Object((1,3,6,1,4,1,5205,2,16,1,7,4),_FeSW26LogNumber_Type())
feSW26LogNumber.setMaxAccess(_D)
if mibBuilder.loadTexts:feSW26LogNumber.setStatus(_A)
_FeSW26LogTable_Object=MibTable
feSW26LogTable=_FeSW26LogTable_Object((1,3,6,1,4,1,5205,2,16,1,7,5))
if mibBuilder.loadTexts:feSW26LogTable.setStatus(_A)
_FeSW26LogEntry_Object=MibTableRow
feSW26LogEntry=_FeSW26LogEntry_Object((1,3,6,1,4,1,5205,2,16,1,7,5,1))
feSW26LogEntry.setIndexNames((0,_E,_Q))
if mibBuilder.loadTexts:feSW26LogEntry.setStatus(_A)
class _FeSW26LogIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,120))
_FeSW26LogIndex_Type.__name__=_C
_FeSW26LogIndex_Object=MibTableColumn
feSW26LogIndex=_FeSW26LogIndex_Object((1,3,6,1,4,1,5205,2,16,1,7,5,1,1),_FeSW26LogIndex_Type())
feSW26LogIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:feSW26LogIndex.setStatus(_A)
_FeSW26LogEvent_Type=DisplayString
_FeSW26LogEvent_Object=MibTableColumn
feSW26LogEvent=_FeSW26LogEvent_Object((1,3,6,1,4,1,5205,2,16,1,7,5,1,2),_FeSW26LogEvent_Type())
feSW26LogEvent.setMaxAccess(_D)
if mibBuilder.loadTexts:feSW26LogEvent.setStatus(_A)
_FeSW26Firmware_ObjectIdentity=ObjectIdentity
feSW26Firmware=_FeSW26Firmware_ObjectIdentity((1,3,6,1,4,1,5205,2,16,1,8))
_FeSW26FirmwareFileName_Type=DisplayString
_FeSW26FirmwareFileName_Object=MibScalar
feSW26FirmwareFileName=_FeSW26FirmwareFileName_Object((1,3,6,1,4,1,5205,2,16,1,8,1),_FeSW26FirmwareFileName_Type())
feSW26FirmwareFileName.setMaxAccess(_B)
if mibBuilder.loadTexts:feSW26FirmwareFileName.setStatus(_A)
class _FeSW26DoFirmwareUpgrade_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1))
_FeSW26DoFirmwareUpgrade_Type.__name__=_C
_FeSW26DoFirmwareUpgrade_Object=MibScalar
feSW26DoFirmwareUpgrade=_FeSW26DoFirmwareUpgrade_Object((1,3,6,1,4,1,5205,2,16,1,8,2),_FeSW26DoFirmwareUpgrade_Type())
feSW26DoFirmwareUpgrade.setMaxAccess(_B)
if mibBuilder.loadTexts:feSW26DoFirmwareUpgrade.setStatus(_A)
_FeSW26Port_ObjectIdentity=ObjectIdentity
feSW26Port=_FeSW26Port_ObjectIdentity((1,3,6,1,4,1,5205,2,16,1,9))
_FeSW26PortStatus_ObjectIdentity=ObjectIdentity
feSW26PortStatus=_FeSW26PortStatus_ObjectIdentity((1,3,6,1,4,1,5205,2,16,1,9,1))
class _FeSW26PortStatusNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_FeSW26PortStatusNumber_Type.__name__=_C
_FeSW26PortStatusNumber_Object=MibScalar
feSW26PortStatusNumber=_FeSW26PortStatusNumber_Object((1,3,6,1,4,1,5205,2,16,1,9,1,1),_FeSW26PortStatusNumber_Type())
feSW26PortStatusNumber.setMaxAccess(_D)
if mibBuilder.loadTexts:feSW26PortStatusNumber.setStatus(_A)
_FeSW26PortStatusTable_Object=MibTable
feSW26PortStatusTable=_FeSW26PortStatusTable_Object((1,3,6,1,4,1,5205,2,16,1,9,1,2))
if mibBuilder.loadTexts:feSW26PortStatusTable.setStatus(_A)
_FeSW26PortStatusEntry_Object=MibTableRow
feSW26PortStatusEntry=_FeSW26PortStatusEntry_Object((1,3,6,1,4,1,5205,2,16,1,9,1,2,1))
feSW26PortStatusEntry.setIndexNames((0,_E,_R))
if mibBuilder.loadTexts:feSW26PortStatusEntry.setStatus(_A)
class _FeSW26PortStatusIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_FeSW26PortStatusIndex_Type.__name__=_C
_FeSW26PortStatusIndex_Object=MibTableColumn
feSW26PortStatusIndex=_FeSW26PortStatusIndex_Object((1,3,6,1,4,1,5205,2,16,1,9,1,2,1,1),_FeSW26PortStatusIndex_Type())
feSW26PortStatusIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:feSW26PortStatusIndex.setStatus(_A)
_FeSW26PortStatusMedia_Type=DisplayString
_FeSW26PortStatusMedia_Object=MibTableColumn
feSW26PortStatusMedia=_FeSW26PortStatusMedia_Object((1,3,6,1,4,1,5205,2,16,1,9,1,2,1,2),_FeSW26PortStatusMedia_Type())
feSW26PortStatusMedia.setMaxAccess(_D)
if mibBuilder.loadTexts:feSW26PortStatusMedia.setStatus(_A)
_FeSW26PortStatusLink_Type=DisplayString
_FeSW26PortStatusLink_Object=MibTableColumn
feSW26PortStatusLink=_FeSW26PortStatusLink_Object((1,3,6,1,4,1,5205,2,16,1,9,1,2,1,3),_FeSW26PortStatusLink_Type())
feSW26PortStatusLink.setMaxAccess(_D)
if mibBuilder.loadTexts:feSW26PortStatusLink.setStatus(_A)
_FeSW26PortStatusPortState_Type=DisplayString
_FeSW26PortStatusPortState_Object=MibTableColumn
feSW26PortStatusPortState=_FeSW26PortStatusPortState_Object((1,3,6,1,4,1,5205,2,16,1,9,1,2,1,4),_FeSW26PortStatusPortState_Type())
feSW26PortStatusPortState.setMaxAccess(_D)
if mibBuilder.loadTexts:feSW26PortStatusPortState.setStatus(_A)
_FeSW26PortStatusAutoNego_Type=DisplayString
_FeSW26PortStatusAutoNego_Object=MibTableColumn
feSW26PortStatusAutoNego=_FeSW26PortStatusAutoNego_Object((1,3,6,1,4,1,5205,2,16,1,9,1,2,1,5),_FeSW26PortStatusAutoNego_Type())
feSW26PortStatusAutoNego.setMaxAccess(_D)
if mibBuilder.loadTexts:feSW26PortStatusAutoNego.setStatus(_A)
_FeSW26PortStatusSpdDpx_Type=DisplayString
_FeSW26PortStatusSpdDpx_Object=MibTableColumn
feSW26PortStatusSpdDpx=_FeSW26PortStatusSpdDpx_Object((1,3,6,1,4,1,5205,2,16,1,9,1,2,1,6),_FeSW26PortStatusSpdDpx_Type())
feSW26PortStatusSpdDpx.setMaxAccess(_D)
if mibBuilder.loadTexts:feSW26PortStatusSpdDpx.setStatus(_A)
_FeSW26PortStatusRxPause_Type=DisplayString
_FeSW26PortStatusRxPause_Object=MibTableColumn
feSW26PortStatusRxPause=_FeSW26PortStatusRxPause_Object((1,3,6,1,4,1,5205,2,16,1,9,1,2,1,7),_FeSW26PortStatusRxPause_Type())
feSW26PortStatusRxPause.setMaxAccess(_D)
if mibBuilder.loadTexts:feSW26PortStatusRxPause.setStatus(_A)
_FeSW26PortStatusTxPause_Type=DisplayString
_FeSW26PortStatusTxPause_Object=MibTableColumn
feSW26PortStatusTxPause=_FeSW26PortStatusTxPause_Object((1,3,6,1,4,1,5205,2,16,1,9,1,2,1,8),_FeSW26PortStatusTxPause_Type())
feSW26PortStatusTxPause.setMaxAccess(_D)
if mibBuilder.loadTexts:feSW26PortStatusTxPause.setStatus(_A)
_FeSW26PortStatuDescription_Type=DisplayString
_FeSW26PortStatuDescription_Object=MibTableColumn
feSW26PortStatuDescription=_FeSW26PortStatuDescription_Object((1,3,6,1,4,1,5205,2,16,1,9,1,2,1,9),_FeSW26PortStatuDescription_Type())
feSW26PortStatuDescription.setMaxAccess(_D)
if mibBuilder.loadTexts:feSW26PortStatuDescription.setStatus(_A)
_FeSW26PortConf_ObjectIdentity=ObjectIdentity
feSW26PortConf=_FeSW26PortConf_ObjectIdentity((1,3,6,1,4,1,5205,2,16,1,9,2))
class _FeSW26PortConfNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_FeSW26PortConfNumber_Type.__name__=_C
_FeSW26PortConfNumber_Object=MibScalar
feSW26PortConfNumber=_FeSW26PortConfNumber_Object((1,3,6,1,4,1,5205,2,16,1,9,2,1),_FeSW26PortConfNumber_Type())
feSW26PortConfNumber.setMaxAccess(_D)
if mibBuilder.loadTexts:feSW26PortConfNumber.setStatus(_A)
_FeSW26PortConfTable_Object=MibTable
feSW26PortConfTable=_FeSW26PortConfTable_Object((1,3,6,1,4,1,5205,2,16,1,9,2,2))
if mibBuilder.loadTexts:feSW26PortConfTable.setStatus(_A)
_FeSW26PortConfEntry_Object=MibTableRow
feSW26PortConfEntry=_FeSW26PortConfEntry_Object((1,3,6,1,4,1,5205,2,16,1,9,2,2,1))
feSW26PortConfEntry.setIndexNames((0,_E,_S))
if mibBuilder.loadTexts:feSW26PortConfEntry.setStatus(_A)
class _FeSW26PortConfIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_FeSW26PortConfIndex_Type.__name__=_C
_FeSW26PortConfIndex_Object=MibTableColumn
feSW26PortConfIndex=_FeSW26PortConfIndex_Object((1,3,6,1,4,1,5205,2,16,1,9,2,2,1,1),_FeSW26PortConfIndex_Type())
feSW26PortConfIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:feSW26PortConfIndex.setStatus(_A)
class _FeSW26PortConfPortState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1))
_FeSW26PortConfPortState_Type.__name__=_C
_FeSW26PortConfPortState_Object=MibTableColumn
feSW26PortConfPortState=_FeSW26PortConfPortState_Object((1,3,6,1,4,1,5205,2,16,1,9,2,2,1,2),_FeSW26PortConfPortState_Type())
feSW26PortConfPortState.setMaxAccess(_B)
if mibBuilder.loadTexts:feSW26PortConfPortState.setStatus(_A)
class _FeSW26PortConfSpdDpx_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,5))
_FeSW26PortConfSpdDpx_Type.__name__=_C
_FeSW26PortConfSpdDpx_Object=MibTableColumn
feSW26PortConfSpdDpx=_FeSW26PortConfSpdDpx_Object((1,3,6,1,4,1,5205,2,16,1,9,2,2,1,3),_FeSW26PortConfSpdDpx_Type())
feSW26PortConfSpdDpx.setMaxAccess(_B)
if mibBuilder.loadTexts:feSW26PortConfSpdDpx.setStatus(_A)
class _FeSW26PortConfFlwCtrl_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1))
_FeSW26PortConfFlwCtrl_Type.__name__=_C
_FeSW26PortConfFlwCtrl_Object=MibTableColumn
feSW26PortConfFlwCtrl=_FeSW26PortConfFlwCtrl_Object((1,3,6,1,4,1,5205,2,16,1,9,2,2,1,4),_FeSW26PortConfFlwCtrl_Type())
feSW26PortConfFlwCtrl.setMaxAccess(_B)
if mibBuilder.loadTexts:feSW26PortConfFlwCtrl.setStatus(_A)
_FeSW26PortConfDescription_Type=DisplayString
_FeSW26PortConfDescription_Object=MibTableColumn
feSW26PortConfDescription=_FeSW26PortConfDescription_Object((1,3,6,1,4,1,5205,2,16,1,9,2,2,1,5),_FeSW26PortConfDescription_Type())
feSW26PortConfDescription.setMaxAccess(_B)
if mibBuilder.loadTexts:feSW26PortConfDescription.setStatus(_A)
_FeSW26LoopDetectedConf_ObjectIdentity=ObjectIdentity
feSW26LoopDetectedConf=_FeSW26LoopDetectedConf_ObjectIdentity((1,3,6,1,4,1,5205,2,16,1,10))
class _FeSW26LoopDetectedNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_FeSW26LoopDetectedNumber_Type.__name__=_C
_FeSW26LoopDetectedNumber_Object=MibScalar
feSW26LoopDetectedNumber=_FeSW26LoopDetectedNumber_Object((1,3,6,1,4,1,5205,2,16,1,10,1),_FeSW26LoopDetectedNumber_Type())
feSW26LoopDetectedNumber.setMaxAccess(_D)
if mibBuilder.loadTexts:feSW26LoopDetectedNumber.setStatus(_A)
_FeSW26LoopDetectedTable_Object=MibTable
feSW26LoopDetectedTable=_FeSW26LoopDetectedTable_Object((1,3,6,1,4,1,5205,2,16,1,10,2))
if mibBuilder.loadTexts:feSW26LoopDetectedTable.setStatus(_A)
_FeSW26LoopDetectedEntry_Object=MibTableRow
feSW26LoopDetectedEntry=_FeSW26LoopDetectedEntry_Object((1,3,6,1,4,1,5205,2,16,1,10,2,1))
feSW26LoopDetectedEntry.setIndexNames((0,_E,_T))
if mibBuilder.loadTexts:feSW26LoopDetectedEntry.setStatus(_A)
class _FeSW26LoopDetectedfIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_FeSW26LoopDetectedfIndex_Type.__name__=_C
_FeSW26LoopDetectedfIndex_Object=MibTableColumn
feSW26LoopDetectedfIndex=_FeSW26LoopDetectedfIndex_Object((1,3,6,1,4,1,5205,2,16,1,10,2,1,1),_FeSW26LoopDetectedfIndex_Type())
feSW26LoopDetectedfIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:feSW26LoopDetectedfIndex.setStatus(_A)
class _FeSW26LoopDetectedStateEbl_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1))
_FeSW26LoopDetectedStateEbl_Type.__name__=_C
_FeSW26LoopDetectedStateEbl_Object=MibTableColumn
feSW26LoopDetectedStateEbl=_FeSW26LoopDetectedStateEbl_Object((1,3,6,1,4,1,5205,2,16,1,10,2,1,2),_FeSW26LoopDetectedStateEbl_Type())
feSW26LoopDetectedStateEbl.setMaxAccess(_B)
if mibBuilder.loadTexts:feSW26LoopDetectedStateEbl.setStatus(_A)
class _FeSW26LoopDetectedCurrentStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1))
_FeSW26LoopDetectedCurrentStatus_Type.__name__=_C
_FeSW26LoopDetectedCurrentStatus_Object=MibTableColumn
feSW26LoopDetectedCurrentStatus=_FeSW26LoopDetectedCurrentStatus_Object((1,3,6,1,4,1,5205,2,16,1,10,2,1,3),_FeSW26LoopDetectedCurrentStatus_Type())
feSW26LoopDetectedCurrentStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:feSW26LoopDetectedCurrentStatus.setStatus(_A)
class _FeSW26LoopDetectedResumed_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1))
_FeSW26LoopDetectedResumed_Type.__name__=_C
_FeSW26LoopDetectedResumed_Object=MibTableColumn
feSW26LoopDetectedResumed=_FeSW26LoopDetectedResumed_Object((1,3,6,1,4,1,5205,2,16,1,10,2,1,4),_FeSW26LoopDetectedResumed_Type())
feSW26LoopDetectedResumed.setMaxAccess(_B)
if mibBuilder.loadTexts:feSW26LoopDetectedResumed.setStatus(_A)
class _FeSW26LoopDetectedAction_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1))
_FeSW26LoopDetectedAction_Type.__name__=_C
_FeSW26LoopDetectedAction_Object=MibScalar
feSW26LoopDetectedAction=_FeSW26LoopDetectedAction_Object((1,3,6,1,4,1,5205,2,16,1,10,3),_FeSW26LoopDetectedAction_Type())
feSW26LoopDetectedAction.setMaxAccess(_B)
if mibBuilder.loadTexts:feSW26LoopDetectedAction.setStatus(_A)
_FeSW26TrapEntry_ObjectIdentity=ObjectIdentity
feSW26TrapEntry=_FeSW26TrapEntry_ObjectIdentity((1,3,6,1,4,1,5205,2,16,1,20))
_FeSW26TrapVariable_ObjectIdentity=ObjectIdentity
feSW26TrapVariable=_FeSW26TrapVariable_ObjectIdentity((1,3,6,1,4,1,5205,2,16,1,21))
_Username_Type=DisplayString
_Username_Object=MibScalar
username=_Username_Object((1,3,6,1,4,1,5205,2,16,1,21,1),_Username_Type())
username.setMaxAccess(_D)
if mibBuilder.loadTexts:username.setStatus(_A)
class _GroupId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,8))
_GroupId_Type.__name__=_C
_GroupId_Object=MibScalar
groupId=_GroupId_Object((1,3,6,1,4,1,5205,2,16,1,21,2),_GroupId_Type())
groupId.setMaxAccess(_D)
if mibBuilder.loadTexts:groupId.setStatus(_A)
class _Actorkey_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_Actorkey_Type.__name__=_C
_Actorkey_Object=MibScalar
actorkey=_Actorkey_Object((1,3,6,1,4,1,5205,2,16,1,21,3),_Actorkey_Type())
actorkey.setMaxAccess(_D)
if mibBuilder.loadTexts:actorkey.setStatus(_A)
class _Partnerkey_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_Partnerkey_Type.__name__=_C
_Partnerkey_Object=MibScalar
partnerkey=_Partnerkey_Object((1,3,6,1,4,1,5205,2,16,1,21,4),_Partnerkey_Type())
partnerkey.setMaxAccess(_D)
if mibBuilder.loadTexts:partnerkey.setStatus(_A)
_Uplink_Type=DisplayString
_Uplink_Object=MibScalar
uplink=_Uplink_Object((1,3,6,1,4,1,5205,2,16,1,21,5),_Uplink_Type())
uplink.setMaxAccess(_D)
if mibBuilder.loadTexts:uplink.setStatus(_A)
feSW26ModuleInserted=NotificationType((1,3,6,1,4,1,5205,2,16,1,20,1))
feSW26ModuleInserted.setObjects((_F,_G))
if mibBuilder.loadTexts:feSW26ModuleInserted.setStatus(_A)
feSW26ModuleRemoved=NotificationType((1,3,6,1,4,1,5205,2,16,1,20,2))
feSW26ModuleRemoved.setObjects((_F,_G))
if mibBuilder.loadTexts:feSW26ModuleRemoved.setStatus(_A)
feSW26DualMediaSwapped=NotificationType((1,3,6,1,4,1,5205,2,16,1,20,3))
feSW26DualMediaSwapped.setObjects((_F,_G))
if mibBuilder.loadTexts:feSW26DualMediaSwapped.setStatus(_A)
feSW26LoopDetected=NotificationType((1,3,6,1,4,1,5205,2,16,1,20,5))
feSW26LoopDetected.setObjects((_F,_G))
if mibBuilder.loadTexts:feSW26LoopDetected.setStatus(_A)
feSW26StpStateDisabled=NotificationType((1,3,6,1,4,1,5205,2,16,1,20,100))
if mibBuilder.loadTexts:feSW26StpStateDisabled.setStatus(_A)
feSW26StpStateEnabled=NotificationType((1,3,6,1,4,1,5205,2,16,1,20,101))
if mibBuilder.loadTexts:feSW26StpStateEnabled.setStatus(_A)
feSW26StpTopologyChanged=NotificationType((1,3,6,1,4,1,5205,2,16,1,20,102))
feSW26StpTopologyChanged.setObjects((_F,_G))
if mibBuilder.loadTexts:feSW26StpTopologyChanged.setStatus(_A)
feSW26RmonRisingAlarm=NotificationType((1,3,6,1,4,1,5205,2,16,1,20,110))
if mibBuilder.loadTexts:feSW26RmonRisingAlarm.setStatus(_A)
feSW26RmonFallingAlarm=NotificationType((1,3,6,1,4,1,5205,2,16,1,20,111))
if mibBuilder.loadTexts:feSW26RmonFallingAlarm.setStatus(_A)
feSW26LacpStateDisabled=NotificationType((1,3,6,1,4,1,5205,2,16,1,20,120))
feSW26LacpStateDisabled.setObjects(*((_F,_G),(_E,_H)))
if mibBuilder.loadTexts:feSW26LacpStateDisabled.setStatus(_A)
feSW26LacpStateEnabled=NotificationType((1,3,6,1,4,1,5205,2,16,1,20,121))
feSW26LacpStateEnabled.setObjects(*((_F,_G),(_E,_H)))
if mibBuilder.loadTexts:feSW26LacpStateEnabled.setStatus(_A)
feSW26LacpPortAdded=NotificationType((1,3,6,1,4,1,5205,2,16,1,20,123))
feSW26LacpPortAdded.setObjects(*((_F,_G),(_E,_I),(_E,_J)))
if mibBuilder.loadTexts:feSW26LacpPortAdded.setStatus(_A)
feSW26LacpPortTrunkFailure=NotificationType((1,3,6,1,4,1,5205,2,16,1,20,124))
feSW26LacpPortTrunkFailure.setObjects(*((_F,_G),(_E,_I),(_E,_J)))
if mibBuilder.loadTexts:feSW26LacpPortTrunkFailure.setStatus(_A)
feSW26GvrpStateDisabled=NotificationType((1,3,6,1,4,1,5205,2,16,1,20,140))
if mibBuilder.loadTexts:feSW26GvrpStateDisabled.setStatus(_A)
feSW26GvrpStateEnabled=NotificationType((1,3,6,1,4,1,5205,2,16,1,20,141))
if mibBuilder.loadTexts:feSW26GvrpStateEnabled.setStatus(_A)
feSW26VlanPortBaseEnabled=NotificationType((1,3,6,1,4,1,5205,2,16,1,20,151))
if mibBuilder.loadTexts:feSW26VlanPortBaseEnabled.setStatus(_A)
feSW26VlanTagBaseEnabled=NotificationType((1,3,6,1,4,1,5205,2,16,1,20,152))
if mibBuilder.loadTexts:feSW26VlanTagBaseEnabled.setStatus(_A)
feSW26VlanMetroBaseEnabled=NotificationType((1,3,6,1,4,1,5205,2,16,1,20,153))
if mibBuilder.loadTexts:feSW26VlanMetroBaseEnabled.setStatus(_A)
feSW26UserLogin=NotificationType((1,3,6,1,4,1,5205,2,16,1,20,200))
feSW26UserLogin.setObjects((_E,_K))
if mibBuilder.loadTexts:feSW26UserLogin.setStatus(_A)
feSW26UserLogout=NotificationType((1,3,6,1,4,1,5205,2,16,1,20,201))
feSW26UserLogout.setObjects((_E,_K))
if mibBuilder.loadTexts:feSW26UserLogout.setStatus(_A)
mibBuilder.exportSymbols(_E,**{'privatetech':privatetech,'switch':switch,'feSW26ProductID':feSW26ProductID,'feSW26Produces':feSW26Produces,'feSW26System':feSW26System,'feSW26CommonSys':feSW26CommonSys,'feSW26Reboot':feSW26Reboot,'feSW26BiosVsersion':feSW26BiosVsersion,'feSW26FirmwareVersion':feSW26FirmwareVersion,'feSW26HardwareVersion':feSW26HardwareVersion,'feSW26MechanicalVersion':feSW26MechanicalVersion,'feSW26SerialNumber':feSW26SerialNumber,'feSW26HostMacAddress':feSW26HostMacAddress,'feSW26DevicePort':feSW26DevicePort,'feSW26RamSize':feSW26RamSize,'feSW26FlashSize':feSW26FlashSize,'feSW26IP':feSW26IP,'feSW26DhcpSetting':feSW26DhcpSetting,'feSW26IPAddress':feSW26IPAddress,'feSW26NetMask':feSW26NetMask,'feSW26DefaultGateway':feSW26DefaultGateway,'feSW26DnsSetting':feSW26DnsSetting,'feSW26DnsServer':feSW26DnsServer,'feSW26Time':feSW26Time,'feSW26SystemCurrentTime':feSW26SystemCurrentTime,'feSW26ManualTimeSetting':feSW26ManualTimeSetting,'feSW26NTPServer':feSW26NTPServer,'feSW26NTPTimeZone':feSW26NTPTimeZone,'feSW26NTPTimeSync':feSW26NTPTimeSync,'feSW26DaylightSavingTime':feSW26DaylightSavingTime,'feSW26DaylightStartTime':feSW26DaylightStartTime,'feSW26DaylightEndTime':feSW26DaylightEndTime,'feSW26Account':feSW26Account,'feSW26AccountNumber':feSW26AccountNumber,'feSW26AccountTable':feSW26AccountTable,'feSW26AccountEntry':feSW26AccountEntry,_L:feSW26AccountIndex,'feSW26AccountAuthorization':feSW26AccountAuthorization,'feSW26AccountName':feSW26AccountName,'feSW26AccountPassword':feSW26AccountPassword,'feSW26AccountAddName':feSW26AccountAddName,'feSW26AccountAddPassword':feSW26AccountAddPassword,'feSW26DoAccountAdd':feSW26DoAccountAdd,'feSW26AccountDel':feSW26AccountDel,'feSW26Snmp':feSW26Snmp,'feSW26GetCommunity':feSW26GetCommunity,'feSW26SetCommunity':feSW26SetCommunity,'feSW26TrapHostNumber':feSW26TrapHostNumber,'feSW26TrapHostTable':feSW26TrapHostTable,'feSW26TrapHostEntry':feSW26TrapHostEntry,_M:feSW26TrapHostIndex,'feSW26TrapHostIP':feSW26TrapHostIP,'feSW26TrapHostPort':feSW26TrapHostPort,'feSW26TrapHostCommunity':feSW26TrapHostCommunity,'feSW26Alarm':feSW26Alarm,'feSW26Event':feSW26Event,'feSW26EventNumber':feSW26EventNumber,'feSW26EventTable':feSW26EventTable,'feSW26EventEntry':feSW26EventEntry,_N:feSW26EventIndex,'feSW26EventName':feSW26EventName,'feSW26EventSendEmail':feSW26EventSendEmail,'feSW26EventSendSMS':feSW26EventSendSMS,'feSW26EventSendTrap':feSW26EventSendTrap,'feSW26Email':feSW26Email,'feSW26EmailServer':feSW26EmailServer,'feSW26EmailUsername':feSW26EmailUsername,'feSW26EmailPassword':feSW26EmailPassword,'feSW26EmailUserNumber':feSW26EmailUserNumber,'feSW26EmailUserTable':feSW26EmailUserTable,'feSW26EmailUserEntry':feSW26EmailUserEntry,_O:feSW26EmailUserIndex,'feSW26EmailUserAddress':feSW26EmailUserAddress,'feSW26SMS':feSW26SMS,'feSW26SMSServer':feSW26SMSServer,'feSW26SMSUsername':feSW26SMSUsername,'feSW26SMSPassword':feSW26SMSPassword,'feSW26SMSUserNumber':feSW26SMSUserNumber,'feSW26SMSUserTable':feSW26SMSUserTable,'feSW26SMSUserEntry':feSW26SMSUserEntry,_P:feSW26SMSUserIndex,'feSW26SMSUserMobilePhone':feSW26SMSUserMobilePhone,'feSW26Tftp':feSW26Tftp,'feSW26TftpServer':feSW26TftpServer,'feSW26Configuration':feSW26Configuration,'feSW26SaveRestore':feSW26SaveRestore,'feSW26SaveStart':feSW26SaveStart,'feSW26SaveUser':feSW26SaveUser,'feSW26RestoreDefault':feSW26RestoreDefault,'feSW26RestoreUser':feSW26RestoreUser,'feSW26ConfigFile':feSW26ConfigFile,'feSW26ExportConfigName':feSW26ExportConfigName,'feSW26DoExportConfig':feSW26DoExportConfig,'feSW26ImportConfigName':feSW26ImportConfigName,'feSW26DoImportConfig':feSW26DoImportConfig,'feSW26Diagnostic':feSW26Diagnostic,'feSW26EEPROMTest':feSW26EEPROMTest,'feSW26UartTest':feSW26UartTest,'feSW26DramTest':feSW26DramTest,'feSW26FlashTest':feSW26FlashTest,'feSW26InternalLoopbackTest':feSW26InternalLoopbackTest,'feSW26ExternalLoopbackTest':feSW26ExternalLoopbackTest,'feSW26PingTest':feSW26PingTest,'feSW26Log':feSW26Log,'feSW26ClearLog':feSW26ClearLog,'feSW26UploadLog':feSW26UploadLog,'feSW26AutoUploadLogState':feSW26AutoUploadLogState,'feSW26LogNumber':feSW26LogNumber,'feSW26LogTable':feSW26LogTable,'feSW26LogEntry':feSW26LogEntry,_Q:feSW26LogIndex,'feSW26LogEvent':feSW26LogEvent,'feSW26Firmware':feSW26Firmware,'feSW26FirmwareFileName':feSW26FirmwareFileName,'feSW26DoFirmwareUpgrade':feSW26DoFirmwareUpgrade,'feSW26Port':feSW26Port,'feSW26PortStatus':feSW26PortStatus,'feSW26PortStatusNumber':feSW26PortStatusNumber,'feSW26PortStatusTable':feSW26PortStatusTable,'feSW26PortStatusEntry':feSW26PortStatusEntry,_R:feSW26PortStatusIndex,'feSW26PortStatusMedia':feSW26PortStatusMedia,'feSW26PortStatusLink':feSW26PortStatusLink,'feSW26PortStatusPortState':feSW26PortStatusPortState,'feSW26PortStatusAutoNego':feSW26PortStatusAutoNego,'feSW26PortStatusSpdDpx':feSW26PortStatusSpdDpx,'feSW26PortStatusRxPause':feSW26PortStatusRxPause,'feSW26PortStatusTxPause':feSW26PortStatusTxPause,'feSW26PortStatuDescription':feSW26PortStatuDescription,'feSW26PortConf':feSW26PortConf,'feSW26PortConfNumber':feSW26PortConfNumber,'feSW26PortConfTable':feSW26PortConfTable,'feSW26PortConfEntry':feSW26PortConfEntry,_S:feSW26PortConfIndex,'feSW26PortConfPortState':feSW26PortConfPortState,'feSW26PortConfSpdDpx':feSW26PortConfSpdDpx,'feSW26PortConfFlwCtrl':feSW26PortConfFlwCtrl,'feSW26PortConfDescription':feSW26PortConfDescription,'feSW26LoopDetectedConf':feSW26LoopDetectedConf,'feSW26LoopDetectedNumber':feSW26LoopDetectedNumber,'feSW26LoopDetectedTable':feSW26LoopDetectedTable,'feSW26LoopDetectedEntry':feSW26LoopDetectedEntry,_T:feSW26LoopDetectedfIndex,'feSW26LoopDetectedStateEbl':feSW26LoopDetectedStateEbl,'feSW26LoopDetectedCurrentStatus':feSW26LoopDetectedCurrentStatus,'feSW26LoopDetectedResumed':feSW26LoopDetectedResumed,'feSW26LoopDetectedAction':feSW26LoopDetectedAction,'feSW26TrapEntry':feSW26TrapEntry,'feSW26ModuleInserted':feSW26ModuleInserted,'feSW26ModuleRemoved':feSW26ModuleRemoved,'feSW26DualMediaSwapped':feSW26DualMediaSwapped,'feSW26LoopDetected':feSW26LoopDetected,'feSW26StpStateDisabled':feSW26StpStateDisabled,'feSW26StpStateEnabled':feSW26StpStateEnabled,'feSW26StpTopologyChanged':feSW26StpTopologyChanged,'feSW26RmonRisingAlarm':feSW26RmonRisingAlarm,'feSW26RmonFallingAlarm':feSW26RmonFallingAlarm,'feSW26LacpStateDisabled':feSW26LacpStateDisabled,'feSW26LacpStateEnabled':feSW26LacpStateEnabled,'feSW26LacpPortAdded':feSW26LacpPortAdded,'feSW26LacpPortTrunkFailure':feSW26LacpPortTrunkFailure,'feSW26GvrpStateDisabled':feSW26GvrpStateDisabled,'feSW26GvrpStateEnabled':feSW26GvrpStateEnabled,'feSW26VlanPortBaseEnabled':feSW26VlanPortBaseEnabled,'feSW26VlanTagBaseEnabled':feSW26VlanTagBaseEnabled,'feSW26VlanMetroBaseEnabled':feSW26VlanMetroBaseEnabled,'feSW26UserLogin':feSW26UserLogin,'feSW26UserLogout':feSW26UserLogout,'feSW26TrapVariable':feSW26TrapVariable,_K:username,_H:groupId,_I:actorkey,_J:partnerkey,'uplink':uplink})