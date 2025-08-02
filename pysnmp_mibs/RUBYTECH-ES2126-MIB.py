_T='es2126LoopDetectedfIndex'
_S='es2126PortBandwidthIndex'
_R='es2126PortConfIndex'
_Q='es2126PortStatusIndex'
_P='es2126LogIndex'
_O='es2126EmailUserIndex'
_N='es2126EventIndex'
_M='es2126TrapHostIndex'
_L='es2126AccountIndex'
_K='username'
_J='partnerkey'
_I='actorkey'
_H='groupId'
_G='ifIndex'
_F='IF-MIB'
_E='RUBYTECH-ES2126-MIB'
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
rubytech=ModuleIdentity((1,3,6,1,4,1,5205))
_Switch_ObjectIdentity=ObjectIdentity
switch=_Switch_ObjectIdentity((1,3,6,1,4,1,5205,2))
_Es2126ProductID_ObjectIdentity=ObjectIdentity
es2126ProductID=_Es2126ProductID_ObjectIdentity((1,3,6,1,4,1,5205,2,16))
_Es2126Produces_ObjectIdentity=ObjectIdentity
es2126Produces=_Es2126Produces_ObjectIdentity((1,3,6,1,4,1,5205,2,16,1))
_Es2126System_ObjectIdentity=ObjectIdentity
es2126System=_Es2126System_ObjectIdentity((1,3,6,1,4,1,5205,2,16,1,1))
_Es2126CommonSys_ObjectIdentity=ObjectIdentity
es2126CommonSys=_Es2126CommonSys_ObjectIdentity((1,3,6,1,4,1,5205,2,16,1,1,1))
class _Es2126Reboot_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1),ValueRangeConstraint(2,2))
_Es2126Reboot_Type.__name__=_C
_Es2126Reboot_Object=MibScalar
es2126Reboot=_Es2126Reboot_Object((1,3,6,1,4,1,5205,2,16,1,1,1,1),_Es2126Reboot_Type())
es2126Reboot.setMaxAccess(_B)
if mibBuilder.loadTexts:es2126Reboot.setStatus(_A)
_Es2126BiosVsersion_Type=DisplayString
_Es2126BiosVsersion_Object=MibScalar
es2126BiosVsersion=_Es2126BiosVsersion_Object((1,3,6,1,4,1,5205,2,16,1,1,1,2),_Es2126BiosVsersion_Type())
es2126BiosVsersion.setMaxAccess(_D)
if mibBuilder.loadTexts:es2126BiosVsersion.setStatus(_A)
_Es2126FirmwareVersion_Type=DisplayString
_Es2126FirmwareVersion_Object=MibScalar
es2126FirmwareVersion=_Es2126FirmwareVersion_Object((1,3,6,1,4,1,5205,2,16,1,1,1,3),_Es2126FirmwareVersion_Type())
es2126FirmwareVersion.setMaxAccess(_D)
if mibBuilder.loadTexts:es2126FirmwareVersion.setStatus(_A)
_Es2126HardwareVersion_Type=DisplayString
_Es2126HardwareVersion_Object=MibScalar
es2126HardwareVersion=_Es2126HardwareVersion_Object((1,3,6,1,4,1,5205,2,16,1,1,1,4),_Es2126HardwareVersion_Type())
es2126HardwareVersion.setMaxAccess(_D)
if mibBuilder.loadTexts:es2126HardwareVersion.setStatus(_A)
_Es2126MechanicalVersion_Type=DisplayString
_Es2126MechanicalVersion_Object=MibScalar
es2126MechanicalVersion=_Es2126MechanicalVersion_Object((1,3,6,1,4,1,5205,2,16,1,1,1,5),_Es2126MechanicalVersion_Type())
es2126MechanicalVersion.setMaxAccess(_D)
if mibBuilder.loadTexts:es2126MechanicalVersion.setStatus(_A)
_Es2126SerialNumber_Type=DisplayString
_Es2126SerialNumber_Object=MibScalar
es2126SerialNumber=_Es2126SerialNumber_Object((1,3,6,1,4,1,5205,2,16,1,1,1,6),_Es2126SerialNumber_Type())
es2126SerialNumber.setMaxAccess(_D)
if mibBuilder.loadTexts:es2126SerialNumber.setStatus(_A)
_Es2126HostMacAddress_Type=DisplayString
_Es2126HostMacAddress_Object=MibScalar
es2126HostMacAddress=_Es2126HostMacAddress_Object((1,3,6,1,4,1,5205,2,16,1,1,1,7),_Es2126HostMacAddress_Type())
es2126HostMacAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:es2126HostMacAddress.setStatus(_A)
_Es2126DevicePort_Type=DisplayString
_Es2126DevicePort_Object=MibScalar
es2126DevicePort=_Es2126DevicePort_Object((1,3,6,1,4,1,5205,2,16,1,1,1,8),_Es2126DevicePort_Type())
es2126DevicePort.setMaxAccess(_D)
if mibBuilder.loadTexts:es2126DevicePort.setStatus(_A)
_Es2126RamSize_Type=DisplayString
_Es2126RamSize_Object=MibScalar
es2126RamSize=_Es2126RamSize_Object((1,3,6,1,4,1,5205,2,16,1,1,1,9),_Es2126RamSize_Type())
es2126RamSize.setMaxAccess(_D)
if mibBuilder.loadTexts:es2126RamSize.setStatus(_A)
_Es2126FlashSize_Type=DisplayString
_Es2126FlashSize_Object=MibScalar
es2126FlashSize=_Es2126FlashSize_Object((1,3,6,1,4,1,5205,2,16,1,1,1,10),_Es2126FlashSize_Type())
es2126FlashSize.setMaxAccess(_D)
if mibBuilder.loadTexts:es2126FlashSize.setStatus(_A)
_Es2126IP_ObjectIdentity=ObjectIdentity
es2126IP=_Es2126IP_ObjectIdentity((1,3,6,1,4,1,5205,2,16,1,1,2))
class _Es2126DhcpSetting_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1))
_Es2126DhcpSetting_Type.__name__=_C
_Es2126DhcpSetting_Object=MibScalar
es2126DhcpSetting=_Es2126DhcpSetting_Object((1,3,6,1,4,1,5205,2,16,1,1,2,1),_Es2126DhcpSetting_Type())
es2126DhcpSetting.setMaxAccess(_B)
if mibBuilder.loadTexts:es2126DhcpSetting.setStatus(_A)
_Es2126IPAddress_Type=IpAddress
_Es2126IPAddress_Object=MibScalar
es2126IPAddress=_Es2126IPAddress_Object((1,3,6,1,4,1,5205,2,16,1,1,2,2),_Es2126IPAddress_Type())
es2126IPAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:es2126IPAddress.setStatus(_A)
_Es2126NetMask_Type=IpAddress
_Es2126NetMask_Object=MibScalar
es2126NetMask=_Es2126NetMask_Object((1,3,6,1,4,1,5205,2,16,1,1,2,3),_Es2126NetMask_Type())
es2126NetMask.setMaxAccess(_B)
if mibBuilder.loadTexts:es2126NetMask.setStatus(_A)
_Es2126DefaultGateway_Type=IpAddress
_Es2126DefaultGateway_Object=MibScalar
es2126DefaultGateway=_Es2126DefaultGateway_Object((1,3,6,1,4,1,5205,2,16,1,1,2,4),_Es2126DefaultGateway_Type())
es2126DefaultGateway.setMaxAccess(_B)
if mibBuilder.loadTexts:es2126DefaultGateway.setStatus(_A)
class _Es2126DnsSetting_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1))
_Es2126DnsSetting_Type.__name__=_C
_Es2126DnsSetting_Object=MibScalar
es2126DnsSetting=_Es2126DnsSetting_Object((1,3,6,1,4,1,5205,2,16,1,1,2,5),_Es2126DnsSetting_Type())
es2126DnsSetting.setMaxAccess(_B)
if mibBuilder.loadTexts:es2126DnsSetting.setStatus(_A)
_Es2126DnsServer_Type=IpAddress
_Es2126DnsServer_Object=MibScalar
es2126DnsServer=_Es2126DnsServer_Object((1,3,6,1,4,1,5205,2,16,1,1,2,6),_Es2126DnsServer_Type())
es2126DnsServer.setMaxAccess(_B)
if mibBuilder.loadTexts:es2126DnsServer.setStatus(_A)
_Es2126Time_ObjectIdentity=ObjectIdentity
es2126Time=_Es2126Time_ObjectIdentity((1,3,6,1,4,1,5205,2,16,1,1,3))
_Es2126SystemCurrentTime_Type=DisplayString
_Es2126SystemCurrentTime_Object=MibScalar
es2126SystemCurrentTime=_Es2126SystemCurrentTime_Object((1,3,6,1,4,1,5205,2,16,1,1,3,1),_Es2126SystemCurrentTime_Type())
es2126SystemCurrentTime.setMaxAccess(_D)
if mibBuilder.loadTexts:es2126SystemCurrentTime.setStatus(_A)
_Es2126ManualTimeSetting_Type=DisplayString
_Es2126ManualTimeSetting_Object=MibScalar
es2126ManualTimeSetting=_Es2126ManualTimeSetting_Object((1,3,6,1,4,1,5205,2,16,1,1,3,2),_Es2126ManualTimeSetting_Type())
es2126ManualTimeSetting.setMaxAccess(_B)
if mibBuilder.loadTexts:es2126ManualTimeSetting.setStatus(_A)
_Es2126NTPServer_Type=DisplayString
_Es2126NTPServer_Object=MibScalar
es2126NTPServer=_Es2126NTPServer_Object((1,3,6,1,4,1,5205,2,16,1,1,3,3),_Es2126NTPServer_Type())
es2126NTPServer.setMaxAccess(_B)
if mibBuilder.loadTexts:es2126NTPServer.setStatus(_A)
class _Es2126NTPTimeZone_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-12,13))
_Es2126NTPTimeZone_Type.__name__=_C
_Es2126NTPTimeZone_Object=MibScalar
es2126NTPTimeZone=_Es2126NTPTimeZone_Object((1,3,6,1,4,1,5205,2,16,1,1,3,4),_Es2126NTPTimeZone_Type())
es2126NTPTimeZone.setMaxAccess(_B)
if mibBuilder.loadTexts:es2126NTPTimeZone.setStatus(_A)
class _Es2126NTPTimeSync_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1))
_Es2126NTPTimeSync_Type.__name__=_C
_Es2126NTPTimeSync_Object=MibScalar
es2126NTPTimeSync=_Es2126NTPTimeSync_Object((1,3,6,1,4,1,5205,2,16,1,1,3,5),_Es2126NTPTimeSync_Type())
es2126NTPTimeSync.setMaxAccess(_B)
if mibBuilder.loadTexts:es2126NTPTimeSync.setStatus(_A)
class _Es2126DaylightSavingTime_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-5,5))
_Es2126DaylightSavingTime_Type.__name__=_C
_Es2126DaylightSavingTime_Object=MibScalar
es2126DaylightSavingTime=_Es2126DaylightSavingTime_Object((1,3,6,1,4,1,5205,2,16,1,1,3,6),_Es2126DaylightSavingTime_Type())
es2126DaylightSavingTime.setMaxAccess(_B)
if mibBuilder.loadTexts:es2126DaylightSavingTime.setStatus(_A)
_Es2126DaylightStartTime_Type=DisplayString
_Es2126DaylightStartTime_Object=MibScalar
es2126DaylightStartTime=_Es2126DaylightStartTime_Object((1,3,6,1,4,1,5205,2,16,1,1,3,7),_Es2126DaylightStartTime_Type())
es2126DaylightStartTime.setMaxAccess(_B)
if mibBuilder.loadTexts:es2126DaylightStartTime.setStatus(_A)
_Es2126DaylightEndTime_Type=DisplayString
_Es2126DaylightEndTime_Object=MibScalar
es2126DaylightEndTime=_Es2126DaylightEndTime_Object((1,3,6,1,4,1,5205,2,16,1,1,3,8),_Es2126DaylightEndTime_Type())
es2126DaylightEndTime.setMaxAccess(_B)
if mibBuilder.loadTexts:es2126DaylightEndTime.setStatus(_A)
_Es2126Account_ObjectIdentity=ObjectIdentity
es2126Account=_Es2126Account_ObjectIdentity((1,3,6,1,4,1,5205,2,16,1,1,4))
class _Es2126AccountNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,5))
_Es2126AccountNumber_Type.__name__=_C
_Es2126AccountNumber_Object=MibScalar
es2126AccountNumber=_Es2126AccountNumber_Object((1,3,6,1,4,1,5205,2,16,1,1,4,1),_Es2126AccountNumber_Type())
es2126AccountNumber.setMaxAccess(_D)
if mibBuilder.loadTexts:es2126AccountNumber.setStatus(_A)
_Es2126AccountTable_Object=MibTable
es2126AccountTable=_Es2126AccountTable_Object((1,3,6,1,4,1,5205,2,16,1,1,4,2))
if mibBuilder.loadTexts:es2126AccountTable.setStatus(_A)
_Es2126AccountEntry_Object=MibTableRow
es2126AccountEntry=_Es2126AccountEntry_Object((1,3,6,1,4,1,5205,2,16,1,1,4,2,1))
es2126AccountEntry.setIndexNames((0,_E,_L))
if mibBuilder.loadTexts:es2126AccountEntry.setStatus(_A)
class _Es2126AccountIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,5))
_Es2126AccountIndex_Type.__name__=_C
_Es2126AccountIndex_Object=MibTableColumn
es2126AccountIndex=_Es2126AccountIndex_Object((1,3,6,1,4,1,5205,2,16,1,1,4,2,1,1),_Es2126AccountIndex_Type())
es2126AccountIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:es2126AccountIndex.setStatus(_A)
_Es2126AccountAuthorization_Type=DisplayString
_Es2126AccountAuthorization_Object=MibTableColumn
es2126AccountAuthorization=_Es2126AccountAuthorization_Object((1,3,6,1,4,1,5205,2,16,1,1,4,2,1,2),_Es2126AccountAuthorization_Type())
es2126AccountAuthorization.setMaxAccess(_D)
if mibBuilder.loadTexts:es2126AccountAuthorization.setStatus(_A)
_Es2126AccountName_Type=DisplayString
_Es2126AccountName_Object=MibTableColumn
es2126AccountName=_Es2126AccountName_Object((1,3,6,1,4,1,5205,2,16,1,1,4,2,1,3),_Es2126AccountName_Type())
es2126AccountName.setMaxAccess(_B)
if mibBuilder.loadTexts:es2126AccountName.setStatus(_A)
_Es2126AccountPassword_Type=DisplayString
_Es2126AccountPassword_Object=MibTableColumn
es2126AccountPassword=_Es2126AccountPassword_Object((1,3,6,1,4,1,5205,2,16,1,1,4,2,1,4),_Es2126AccountPassword_Type())
es2126AccountPassword.setMaxAccess(_B)
if mibBuilder.loadTexts:es2126AccountPassword.setStatus(_A)
_Es2126AccountAddName_Type=DisplayString
_Es2126AccountAddName_Object=MibScalar
es2126AccountAddName=_Es2126AccountAddName_Object((1,3,6,1,4,1,5205,2,16,1,1,4,3),_Es2126AccountAddName_Type())
es2126AccountAddName.setMaxAccess(_B)
if mibBuilder.loadTexts:es2126AccountAddName.setStatus(_A)
_Es2126AccountAddPassword_Type=DisplayString
_Es2126AccountAddPassword_Object=MibScalar
es2126AccountAddPassword=_Es2126AccountAddPassword_Object((1,3,6,1,4,1,5205,2,16,1,1,4,4),_Es2126AccountAddPassword_Type())
es2126AccountAddPassword.setMaxAccess(_B)
if mibBuilder.loadTexts:es2126AccountAddPassword.setStatus(_A)
class _Es2126DoAccountAdd_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1))
_Es2126DoAccountAdd_Type.__name__=_C
_Es2126DoAccountAdd_Object=MibScalar
es2126DoAccountAdd=_Es2126DoAccountAdd_Object((1,3,6,1,4,1,5205,2,16,1,1,4,5),_Es2126DoAccountAdd_Type())
es2126DoAccountAdd.setMaxAccess(_B)
if mibBuilder.loadTexts:es2126DoAccountAdd.setStatus(_A)
class _Es2126AccountDel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(2,5))
_Es2126AccountDel_Type.__name__=_C
_Es2126AccountDel_Object=MibScalar
es2126AccountDel=_Es2126AccountDel_Object((1,3,6,1,4,1,5205,2,16,1,1,4,6),_Es2126AccountDel_Type())
es2126AccountDel.setMaxAccess(_B)
if mibBuilder.loadTexts:es2126AccountDel.setStatus(_A)
_Es2126Snmp_ObjectIdentity=ObjectIdentity
es2126Snmp=_Es2126Snmp_ObjectIdentity((1,3,6,1,4,1,5205,2,16,1,2))
_Es2126GetCommunity_Type=DisplayString
_Es2126GetCommunity_Object=MibScalar
es2126GetCommunity=_Es2126GetCommunity_Object((1,3,6,1,4,1,5205,2,16,1,2,1),_Es2126GetCommunity_Type())
es2126GetCommunity.setMaxAccess(_B)
if mibBuilder.loadTexts:es2126GetCommunity.setStatus(_A)
_Es2126SetCommunity_Type=DisplayString
_Es2126SetCommunity_Object=MibScalar
es2126SetCommunity=_Es2126SetCommunity_Object((1,3,6,1,4,1,5205,2,16,1,2,2),_Es2126SetCommunity_Type())
es2126SetCommunity.setMaxAccess(_B)
if mibBuilder.loadTexts:es2126SetCommunity.setStatus(_A)
class _Es2126TrapHostNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,6))
_Es2126TrapHostNumber_Type.__name__=_C
_Es2126TrapHostNumber_Object=MibScalar
es2126TrapHostNumber=_Es2126TrapHostNumber_Object((1,3,6,1,4,1,5205,2,16,1,2,3),_Es2126TrapHostNumber_Type())
es2126TrapHostNumber.setMaxAccess(_D)
if mibBuilder.loadTexts:es2126TrapHostNumber.setStatus(_A)
_Es2126TrapHostTable_Object=MibTable
es2126TrapHostTable=_Es2126TrapHostTable_Object((1,3,6,1,4,1,5205,2,16,1,2,4))
if mibBuilder.loadTexts:es2126TrapHostTable.setStatus(_A)
_Es2126TrapHostEntry_Object=MibTableRow
es2126TrapHostEntry=_Es2126TrapHostEntry_Object((1,3,6,1,4,1,5205,2,16,1,2,4,1))
es2126TrapHostEntry.setIndexNames((0,_E,_M))
if mibBuilder.loadTexts:es2126TrapHostEntry.setStatus(_A)
class _Es2126TrapHostIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,6))
_Es2126TrapHostIndex_Type.__name__=_C
_Es2126TrapHostIndex_Object=MibTableColumn
es2126TrapHostIndex=_Es2126TrapHostIndex_Object((1,3,6,1,4,1,5205,2,16,1,2,4,1,1),_Es2126TrapHostIndex_Type())
es2126TrapHostIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:es2126TrapHostIndex.setStatus(_A)
_Es2126TrapHostIP_Type=IpAddress
_Es2126TrapHostIP_Object=MibTableColumn
es2126TrapHostIP=_Es2126TrapHostIP_Object((1,3,6,1,4,1,5205,2,16,1,2,4,1,2),_Es2126TrapHostIP_Type())
es2126TrapHostIP.setMaxAccess(_B)
if mibBuilder.loadTexts:es2126TrapHostIP.setStatus(_A)
class _Es2126TrapHostPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_Es2126TrapHostPort_Type.__name__=_C
_Es2126TrapHostPort_Object=MibTableColumn
es2126TrapHostPort=_Es2126TrapHostPort_Object((1,3,6,1,4,1,5205,2,16,1,2,4,1,3),_Es2126TrapHostPort_Type())
es2126TrapHostPort.setMaxAccess(_B)
if mibBuilder.loadTexts:es2126TrapHostPort.setStatus(_A)
_Es2126TrapHostCommunity_Type=DisplayString
_Es2126TrapHostCommunity_Object=MibTableColumn
es2126TrapHostCommunity=_Es2126TrapHostCommunity_Object((1,3,6,1,4,1,5205,2,16,1,2,4,1,4),_Es2126TrapHostCommunity_Type())
es2126TrapHostCommunity.setMaxAccess(_B)
if mibBuilder.loadTexts:es2126TrapHostCommunity.setStatus(_A)
class _Es2126TrapBootDelayTime_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,120))
_Es2126TrapBootDelayTime_Type.__name__=_C
_Es2126TrapBootDelayTime_Object=MibScalar
es2126TrapBootDelayTime=_Es2126TrapBootDelayTime_Object((1,3,6,1,4,1,5205,2,16,1,2,8),_Es2126TrapBootDelayTime_Type())
es2126TrapBootDelayTime.setMaxAccess(_B)
if mibBuilder.loadTexts:es2126TrapBootDelayTime.setStatus(_A)
_Es2126Alarm_ObjectIdentity=ObjectIdentity
es2126Alarm=_Es2126Alarm_ObjectIdentity((1,3,6,1,4,1,5205,2,16,1,3))
_Es2126Event_ObjectIdentity=ObjectIdentity
es2126Event=_Es2126Event_ObjectIdentity((1,3,6,1,4,1,5205,2,16,1,3,1))
class _Es2126EventNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_Es2126EventNumber_Type.__name__=_C
_Es2126EventNumber_Object=MibScalar
es2126EventNumber=_Es2126EventNumber_Object((1,3,6,1,4,1,5205,2,16,1,3,1,1),_Es2126EventNumber_Type())
es2126EventNumber.setMaxAccess(_D)
if mibBuilder.loadTexts:es2126EventNumber.setStatus(_A)
_Es2126EventTable_Object=MibTable
es2126EventTable=_Es2126EventTable_Object((1,3,6,1,4,1,5205,2,16,1,3,1,2))
if mibBuilder.loadTexts:es2126EventTable.setStatus(_A)
_Es2126EventEntry_Object=MibTableRow
es2126EventEntry=_Es2126EventEntry_Object((1,3,6,1,4,1,5205,2,16,1,3,1,2,1))
es2126EventEntry.setIndexNames((0,_E,_N))
if mibBuilder.loadTexts:es2126EventEntry.setStatus(_A)
class _Es2126EventIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_Es2126EventIndex_Type.__name__=_C
_Es2126EventIndex_Object=MibTableColumn
es2126EventIndex=_Es2126EventIndex_Object((1,3,6,1,4,1,5205,2,16,1,3,1,2,1,1),_Es2126EventIndex_Type())
es2126EventIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:es2126EventIndex.setStatus(_A)
_Es2126EventName_Type=DisplayString
_Es2126EventName_Object=MibTableColumn
es2126EventName=_Es2126EventName_Object((1,3,6,1,4,1,5205,2,16,1,3,1,2,1,2),_Es2126EventName_Type())
es2126EventName.setMaxAccess(_D)
if mibBuilder.loadTexts:es2126EventName.setStatus(_A)
class _Es2126EventSendEmail_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1))
_Es2126EventSendEmail_Type.__name__=_C
_Es2126EventSendEmail_Object=MibTableColumn
es2126EventSendEmail=_Es2126EventSendEmail_Object((1,3,6,1,4,1,5205,2,16,1,3,1,2,1,3),_Es2126EventSendEmail_Type())
es2126EventSendEmail.setMaxAccess(_B)
if mibBuilder.loadTexts:es2126EventSendEmail.setStatus(_A)
class _Es2126EventSendTrap_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1))
_Es2126EventSendTrap_Type.__name__=_C
_Es2126EventSendTrap_Object=MibTableColumn
es2126EventSendTrap=_Es2126EventSendTrap_Object((1,3,6,1,4,1,5205,2,16,1,3,1,2,1,4),_Es2126EventSendTrap_Type())
es2126EventSendTrap.setMaxAccess(_B)
if mibBuilder.loadTexts:es2126EventSendTrap.setStatus(_A)
_Es2126Email_ObjectIdentity=ObjectIdentity
es2126Email=_Es2126Email_ObjectIdentity((1,3,6,1,4,1,5205,2,16,1,3,2))
_Es2126EmailServer_Type=DisplayString
_Es2126EmailServer_Object=MibScalar
es2126EmailServer=_Es2126EmailServer_Object((1,3,6,1,4,1,5205,2,16,1,3,2,1),_Es2126EmailServer_Type())
es2126EmailServer.setMaxAccess(_B)
if mibBuilder.loadTexts:es2126EmailServer.setStatus(_A)
_Es2126EmailUsername_Type=DisplayString
_Es2126EmailUsername_Object=MibScalar
es2126EmailUsername=_Es2126EmailUsername_Object((1,3,6,1,4,1,5205,2,16,1,3,2,2),_Es2126EmailUsername_Type())
es2126EmailUsername.setMaxAccess(_B)
if mibBuilder.loadTexts:es2126EmailUsername.setStatus(_A)
_Es2126EmailPassword_Type=DisplayString
_Es2126EmailPassword_Object=MibScalar
es2126EmailPassword=_Es2126EmailPassword_Object((1,3,6,1,4,1,5205,2,16,1,3,2,3),_Es2126EmailPassword_Type())
es2126EmailPassword.setMaxAccess(_B)
if mibBuilder.loadTexts:es2126EmailPassword.setStatus(_A)
_Es2126EmailSender_Type=DisplayString
_Es2126EmailSender_Object=MibScalar
es2126EmailSender=_Es2126EmailSender_Object((1,3,6,1,4,1,5205,2,16,1,3,2,4),_Es2126EmailSender_Type())
es2126EmailSender.setMaxAccess(_B)
if mibBuilder.loadTexts:es2126EmailSender.setStatus(_A)
_Es2126EmailReturnPath_Type=DisplayString
_Es2126EmailReturnPath_Object=MibScalar
es2126EmailReturnPath=_Es2126EmailReturnPath_Object((1,3,6,1,4,1,5205,2,16,1,3,2,5),_Es2126EmailReturnPath_Type())
es2126EmailReturnPath.setMaxAccess(_B)
if mibBuilder.loadTexts:es2126EmailReturnPath.setStatus(_A)
class _Es2126EmailUserNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,6))
_Es2126EmailUserNumber_Type.__name__=_C
_Es2126EmailUserNumber_Object=MibScalar
es2126EmailUserNumber=_Es2126EmailUserNumber_Object((1,3,6,1,4,1,5205,2,16,1,3,2,6),_Es2126EmailUserNumber_Type())
es2126EmailUserNumber.setMaxAccess(_D)
if mibBuilder.loadTexts:es2126EmailUserNumber.setStatus(_A)
_Es2126EmailUserTable_Object=MibTable
es2126EmailUserTable=_Es2126EmailUserTable_Object((1,3,6,1,4,1,5205,2,16,1,3,2,7))
if mibBuilder.loadTexts:es2126EmailUserTable.setStatus(_A)
_Es2126EmailUserEntry_Object=MibTableRow
es2126EmailUserEntry=_Es2126EmailUserEntry_Object((1,3,6,1,4,1,5205,2,16,1,3,2,7,1))
es2126EmailUserEntry.setIndexNames((0,_E,_O))
if mibBuilder.loadTexts:es2126EmailUserEntry.setStatus(_A)
class _Es2126EmailUserIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,6))
_Es2126EmailUserIndex_Type.__name__=_C
_Es2126EmailUserIndex_Object=MibTableColumn
es2126EmailUserIndex=_Es2126EmailUserIndex_Object((1,3,6,1,4,1,5205,2,16,1,3,2,7,1,1),_Es2126EmailUserIndex_Type())
es2126EmailUserIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:es2126EmailUserIndex.setStatus(_A)
_Es2126EmailUserAddress_Type=DisplayString
_Es2126EmailUserAddress_Object=MibTableColumn
es2126EmailUserAddress=_Es2126EmailUserAddress_Object((1,3,6,1,4,1,5205,2,16,1,3,2,7,1,2),_Es2126EmailUserAddress_Type())
es2126EmailUserAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:es2126EmailUserAddress.setStatus(_A)
_Es2126Tftp_ObjectIdentity=ObjectIdentity
es2126Tftp=_Es2126Tftp_ObjectIdentity((1,3,6,1,4,1,5205,2,16,1,4))
_Es2126TftpServer_Type=IpAddress
_Es2126TftpServer_Object=MibScalar
es2126TftpServer=_Es2126TftpServer_Object((1,3,6,1,4,1,5205,2,16,1,4,1),_Es2126TftpServer_Type())
es2126TftpServer.setMaxAccess(_B)
if mibBuilder.loadTexts:es2126TftpServer.setStatus(_A)
_Es2126Configuration_ObjectIdentity=ObjectIdentity
es2126Configuration=_Es2126Configuration_ObjectIdentity((1,3,6,1,4,1,5205,2,16,1,5))
_Es2126SaveRestore_ObjectIdentity=ObjectIdentity
es2126SaveRestore=_Es2126SaveRestore_ObjectIdentity((1,3,6,1,4,1,5205,2,16,1,5,1))
class _Es2126SaveStart_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1))
_Es2126SaveStart_Type.__name__=_C
_Es2126SaveStart_Object=MibScalar
es2126SaveStart=_Es2126SaveStart_Object((1,3,6,1,4,1,5205,2,16,1,5,1,1),_Es2126SaveStart_Type())
es2126SaveStart.setMaxAccess(_B)
if mibBuilder.loadTexts:es2126SaveStart.setStatus(_A)
class _Es2126SaveUser_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1))
_Es2126SaveUser_Type.__name__=_C
_Es2126SaveUser_Object=MibScalar
es2126SaveUser=_Es2126SaveUser_Object((1,3,6,1,4,1,5205,2,16,1,5,1,2),_Es2126SaveUser_Type())
es2126SaveUser.setMaxAccess(_B)
if mibBuilder.loadTexts:es2126SaveUser.setStatus(_A)
class _Es2126RestoreDefault_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1),ValueRangeConstraint(2,2))
_Es2126RestoreDefault_Type.__name__=_C
_Es2126RestoreDefault_Object=MibScalar
es2126RestoreDefault=_Es2126RestoreDefault_Object((1,3,6,1,4,1,5205,2,16,1,5,1,3),_Es2126RestoreDefault_Type())
es2126RestoreDefault.setMaxAccess(_B)
if mibBuilder.loadTexts:es2126RestoreDefault.setStatus(_A)
class _Es2126RestoreUser_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1))
_Es2126RestoreUser_Type.__name__=_C
_Es2126RestoreUser_Object=MibScalar
es2126RestoreUser=_Es2126RestoreUser_Object((1,3,6,1,4,1,5205,2,16,1,5,1,4),_Es2126RestoreUser_Type())
es2126RestoreUser.setMaxAccess(_B)
if mibBuilder.loadTexts:es2126RestoreUser.setStatus(_A)
_Es2126ConfigFile_ObjectIdentity=ObjectIdentity
es2126ConfigFile=_Es2126ConfigFile_ObjectIdentity((1,3,6,1,4,1,5205,2,16,1,5,2))
_Es2126ExportConfigName_Type=DisplayString
_Es2126ExportConfigName_Object=MibScalar
es2126ExportConfigName=_Es2126ExportConfigName_Object((1,3,6,1,4,1,5205,2,16,1,5,2,1),_Es2126ExportConfigName_Type())
es2126ExportConfigName.setMaxAccess(_B)
if mibBuilder.loadTexts:es2126ExportConfigName.setStatus(_A)
class _Es2126DoExportConfig_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1),ValueRangeConstraint(2,2))
_Es2126DoExportConfig_Type.__name__=_C
_Es2126DoExportConfig_Object=MibScalar
es2126DoExportConfig=_Es2126DoExportConfig_Object((1,3,6,1,4,1,5205,2,16,1,5,2,2),_Es2126DoExportConfig_Type())
es2126DoExportConfig.setMaxAccess(_B)
if mibBuilder.loadTexts:es2126DoExportConfig.setStatus(_A)
_Es2126ImportConfigName_Type=DisplayString
_Es2126ImportConfigName_Object=MibScalar
es2126ImportConfigName=_Es2126ImportConfigName_Object((1,3,6,1,4,1,5205,2,16,1,5,2,3),_Es2126ImportConfigName_Type())
es2126ImportConfigName.setMaxAccess(_B)
if mibBuilder.loadTexts:es2126ImportConfigName.setStatus(_A)
class _Es2126DoImportConfig_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1),ValueRangeConstraint(2,2))
_Es2126DoImportConfig_Type.__name__=_C
_Es2126DoImportConfig_Object=MibScalar
es2126DoImportConfig=_Es2126DoImportConfig_Object((1,3,6,1,4,1,5205,2,16,1,5,2,4),_Es2126DoImportConfig_Type())
es2126DoImportConfig.setMaxAccess(_B)
if mibBuilder.loadTexts:es2126DoImportConfig.setStatus(_A)
_Es2126Diagnostic_ObjectIdentity=ObjectIdentity
es2126Diagnostic=_Es2126Diagnostic_ObjectIdentity((1,3,6,1,4,1,5205,2,16,1,6))
_Es2126InternalLoopbackTest_Type=DisplayString
_Es2126InternalLoopbackTest_Object=MibScalar
es2126InternalLoopbackTest=_Es2126InternalLoopbackTest_Object((1,3,6,1,4,1,5205,2,16,1,6,1),_Es2126InternalLoopbackTest_Type())
es2126InternalLoopbackTest.setMaxAccess(_D)
if mibBuilder.loadTexts:es2126InternalLoopbackTest.setStatus(_A)
_Es2126ExternalLoopbackTest_Type=DisplayString
_Es2126ExternalLoopbackTest_Object=MibScalar
es2126ExternalLoopbackTest=_Es2126ExternalLoopbackTest_Object((1,3,6,1,4,1,5205,2,16,1,6,2),_Es2126ExternalLoopbackTest_Type())
es2126ExternalLoopbackTest.setMaxAccess(_D)
if mibBuilder.loadTexts:es2126ExternalLoopbackTest.setStatus(_A)
_Es2126PingTest_Type=DisplayString
_Es2126PingTest_Object=MibScalar
es2126PingTest=_Es2126PingTest_Object((1,3,6,1,4,1,5205,2,16,1,6,3),_Es2126PingTest_Type())
es2126PingTest.setMaxAccess(_B)
if mibBuilder.loadTexts:es2126PingTest.setStatus(_A)
_Es2126Watchdog_ObjectIdentity=ObjectIdentity
es2126Watchdog=_Es2126Watchdog_ObjectIdentity((1,3,6,1,4,1,5205,2,16,1,6,4))
class _Es2126WatchdogState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1))
_Es2126WatchdogState_Type.__name__=_C
_Es2126WatchdogState_Object=MibScalar
es2126WatchdogState=_Es2126WatchdogState_Object((1,3,6,1,4,1,5205,2,16,1,6,4,1),_Es2126WatchdogState_Type())
es2126WatchdogState.setMaxAccess(_B)
if mibBuilder.loadTexts:es2126WatchdogState.setStatus(_A)
class _Es2126WatchdogTimeGap_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_Es2126WatchdogTimeGap_Type.__name__=_C
_Es2126WatchdogTimeGap_Object=MibScalar
es2126WatchdogTimeGap=_Es2126WatchdogTimeGap_Object((1,3,6,1,4,1,5205,2,16,1,6,4,2),_Es2126WatchdogTimeGap_Type())
es2126WatchdogTimeGap.setMaxAccess(_B)
if mibBuilder.loadTexts:es2126WatchdogTimeGap.setStatus(_A)
_Es2126WatchdogHost_Type=DisplayString
_Es2126WatchdogHost_Object=MibScalar
es2126WatchdogHost=_Es2126WatchdogHost_Object((1,3,6,1,4,1,5205,2,16,1,6,4,3),_Es2126WatchdogHost_Type())
es2126WatchdogHost.setMaxAccess(_B)
if mibBuilder.loadTexts:es2126WatchdogHost.setStatus(_A)
class _Es2126WatchdogResetMgtInf_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1))
_Es2126WatchdogResetMgtInf_Type.__name__=_C
_Es2126WatchdogResetMgtInf_Object=MibScalar
es2126WatchdogResetMgtInf=_Es2126WatchdogResetMgtInf_Object((1,3,6,1,4,1,5205,2,16,1,6,4,4),_Es2126WatchdogResetMgtInf_Type())
es2126WatchdogResetMgtInf.setMaxAccess(_B)
if mibBuilder.loadTexts:es2126WatchdogResetMgtInf.setStatus(_A)
class _Es2126WatchdogResetMgtInfCount_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,20))
_Es2126WatchdogResetMgtInfCount_Type.__name__=_C
_Es2126WatchdogResetMgtInfCount_Object=MibScalar
es2126WatchdogResetMgtInfCount=_Es2126WatchdogResetMgtInfCount_Object((1,3,6,1,4,1,5205,2,16,1,6,4,5),_Es2126WatchdogResetMgtInfCount_Type())
es2126WatchdogResetMgtInfCount.setMaxAccess(_B)
if mibBuilder.loadTexts:es2126WatchdogResetMgtInfCount.setStatus(_A)
class _Es2126WatchdogResetSystem_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1))
_Es2126WatchdogResetSystem_Type.__name__=_C
_Es2126WatchdogResetSystem_Object=MibScalar
es2126WatchdogResetSystem=_Es2126WatchdogResetSystem_Object((1,3,6,1,4,1,5205,2,16,1,6,4,6),_Es2126WatchdogResetSystem_Type())
es2126WatchdogResetSystem.setMaxAccess(_B)
if mibBuilder.loadTexts:es2126WatchdogResetSystem.setStatus(_A)
class _Es2126WatchdogResetSystemCount_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1000))
_Es2126WatchdogResetSystemCount_Type.__name__=_C
_Es2126WatchdogResetSystemCount_Object=MibScalar
es2126WatchdogResetSystemCount=_Es2126WatchdogResetSystemCount_Object((1,3,6,1,4,1,5205,2,16,1,6,4,7),_Es2126WatchdogResetSystemCount_Type())
es2126WatchdogResetSystemCount.setMaxAccess(_B)
if mibBuilder.loadTexts:es2126WatchdogResetSystemCount.setStatus(_A)
_Es2126Log_ObjectIdentity=ObjectIdentity
es2126Log=_Es2126Log_ObjectIdentity((1,3,6,1,4,1,5205,2,16,1,7))
class _Es2126ClearLog_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1))
_Es2126ClearLog_Type.__name__=_C
_Es2126ClearLog_Object=MibScalar
es2126ClearLog=_Es2126ClearLog_Object((1,3,6,1,4,1,5205,2,16,1,7,1),_Es2126ClearLog_Type())
es2126ClearLog.setMaxAccess(_B)
if mibBuilder.loadTexts:es2126ClearLog.setStatus(_A)
class _Es2126UploadLog_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1))
_Es2126UploadLog_Type.__name__=_C
_Es2126UploadLog_Object=MibScalar
es2126UploadLog=_Es2126UploadLog_Object((1,3,6,1,4,1,5205,2,16,1,7,2),_Es2126UploadLog_Type())
es2126UploadLog.setMaxAccess(_B)
if mibBuilder.loadTexts:es2126UploadLog.setStatus(_A)
class _Es2126AutoUploadLogState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1))
_Es2126AutoUploadLogState_Type.__name__=_C
_Es2126AutoUploadLogState_Object=MibScalar
es2126AutoUploadLogState=_Es2126AutoUploadLogState_Object((1,3,6,1,4,1,5205,2,16,1,7,3),_Es2126AutoUploadLogState_Type())
es2126AutoUploadLogState.setMaxAccess(_B)
if mibBuilder.loadTexts:es2126AutoUploadLogState.setStatus(_A)
class _Es2126LogNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,120))
_Es2126LogNumber_Type.__name__=_C
_Es2126LogNumber_Object=MibScalar
es2126LogNumber=_Es2126LogNumber_Object((1,3,6,1,4,1,5205,2,16,1,7,4),_Es2126LogNumber_Type())
es2126LogNumber.setMaxAccess(_D)
if mibBuilder.loadTexts:es2126LogNumber.setStatus(_A)
_Es2126LogTable_Object=MibTable
es2126LogTable=_Es2126LogTable_Object((1,3,6,1,4,1,5205,2,16,1,7,5))
if mibBuilder.loadTexts:es2126LogTable.setStatus(_A)
_Es2126LogEntry_Object=MibTableRow
es2126LogEntry=_Es2126LogEntry_Object((1,3,6,1,4,1,5205,2,16,1,7,5,1))
es2126LogEntry.setIndexNames((0,_E,_P))
if mibBuilder.loadTexts:es2126LogEntry.setStatus(_A)
class _Es2126LogIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,120))
_Es2126LogIndex_Type.__name__=_C
_Es2126LogIndex_Object=MibTableColumn
es2126LogIndex=_Es2126LogIndex_Object((1,3,6,1,4,1,5205,2,16,1,7,5,1,1),_Es2126LogIndex_Type())
es2126LogIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:es2126LogIndex.setStatus(_A)
_Es2126LogEvent_Type=DisplayString
_Es2126LogEvent_Object=MibTableColumn
es2126LogEvent=_Es2126LogEvent_Object((1,3,6,1,4,1,5205,2,16,1,7,5,1,2),_Es2126LogEvent_Type())
es2126LogEvent.setMaxAccess(_D)
if mibBuilder.loadTexts:es2126LogEvent.setStatus(_A)
_Es2126Firmware_ObjectIdentity=ObjectIdentity
es2126Firmware=_Es2126Firmware_ObjectIdentity((1,3,6,1,4,1,5205,2,16,1,8))
_Es2126FirmwareFileName_Type=DisplayString
_Es2126FirmwareFileName_Object=MibScalar
es2126FirmwareFileName=_Es2126FirmwareFileName_Object((1,3,6,1,4,1,5205,2,16,1,8,1),_Es2126FirmwareFileName_Type())
es2126FirmwareFileName.setMaxAccess(_B)
if mibBuilder.loadTexts:es2126FirmwareFileName.setStatus(_A)
class _Es2126DoFirmwareUpgrade_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1))
_Es2126DoFirmwareUpgrade_Type.__name__=_C
_Es2126DoFirmwareUpgrade_Object=MibScalar
es2126DoFirmwareUpgrade=_Es2126DoFirmwareUpgrade_Object((1,3,6,1,4,1,5205,2,16,1,8,2),_Es2126DoFirmwareUpgrade_Type())
es2126DoFirmwareUpgrade.setMaxAccess(_B)
if mibBuilder.loadTexts:es2126DoFirmwareUpgrade.setStatus(_A)
_Es2126Port_ObjectIdentity=ObjectIdentity
es2126Port=_Es2126Port_ObjectIdentity((1,3,6,1,4,1,5205,2,16,1,9))
_Es2126PortStatus_ObjectIdentity=ObjectIdentity
es2126PortStatus=_Es2126PortStatus_ObjectIdentity((1,3,6,1,4,1,5205,2,16,1,9,1))
class _Es2126PortStatusNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_Es2126PortStatusNumber_Type.__name__=_C
_Es2126PortStatusNumber_Object=MibScalar
es2126PortStatusNumber=_Es2126PortStatusNumber_Object((1,3,6,1,4,1,5205,2,16,1,9,1,1),_Es2126PortStatusNumber_Type())
es2126PortStatusNumber.setMaxAccess(_D)
if mibBuilder.loadTexts:es2126PortStatusNumber.setStatus(_A)
_Es2126PortStatusTable_Object=MibTable
es2126PortStatusTable=_Es2126PortStatusTable_Object((1,3,6,1,4,1,5205,2,16,1,9,1,2))
if mibBuilder.loadTexts:es2126PortStatusTable.setStatus(_A)
_Es2126PortStatusEntry_Object=MibTableRow
es2126PortStatusEntry=_Es2126PortStatusEntry_Object((1,3,6,1,4,1,5205,2,16,1,9,1,2,1))
es2126PortStatusEntry.setIndexNames((0,_E,_Q))
if mibBuilder.loadTexts:es2126PortStatusEntry.setStatus(_A)
class _Es2126PortStatusIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_Es2126PortStatusIndex_Type.__name__=_C
_Es2126PortStatusIndex_Object=MibTableColumn
es2126PortStatusIndex=_Es2126PortStatusIndex_Object((1,3,6,1,4,1,5205,2,16,1,9,1,2,1,1),_Es2126PortStatusIndex_Type())
es2126PortStatusIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:es2126PortStatusIndex.setStatus(_A)
_Es2126PortStatusMedia_Type=DisplayString
_Es2126PortStatusMedia_Object=MibTableColumn
es2126PortStatusMedia=_Es2126PortStatusMedia_Object((1,3,6,1,4,1,5205,2,16,1,9,1,2,1,2),_Es2126PortStatusMedia_Type())
es2126PortStatusMedia.setMaxAccess(_D)
if mibBuilder.loadTexts:es2126PortStatusMedia.setStatus(_A)
_Es2126PortStatusLink_Type=DisplayString
_Es2126PortStatusLink_Object=MibTableColumn
es2126PortStatusLink=_Es2126PortStatusLink_Object((1,3,6,1,4,1,5205,2,16,1,9,1,2,1,3),_Es2126PortStatusLink_Type())
es2126PortStatusLink.setMaxAccess(_D)
if mibBuilder.loadTexts:es2126PortStatusLink.setStatus(_A)
_Es2126PortStatusPortState_Type=DisplayString
_Es2126PortStatusPortState_Object=MibTableColumn
es2126PortStatusPortState=_Es2126PortStatusPortState_Object((1,3,6,1,4,1,5205,2,16,1,9,1,2,1,4),_Es2126PortStatusPortState_Type())
es2126PortStatusPortState.setMaxAccess(_D)
if mibBuilder.loadTexts:es2126PortStatusPortState.setStatus(_A)
_Es2126PortStatusAutoNego_Type=DisplayString
_Es2126PortStatusAutoNego_Object=MibTableColumn
es2126PortStatusAutoNego=_Es2126PortStatusAutoNego_Object((1,3,6,1,4,1,5205,2,16,1,9,1,2,1,5),_Es2126PortStatusAutoNego_Type())
es2126PortStatusAutoNego.setMaxAccess(_D)
if mibBuilder.loadTexts:es2126PortStatusAutoNego.setStatus(_A)
_Es2126PortStatusSpdDpx_Type=DisplayString
_Es2126PortStatusSpdDpx_Object=MibTableColumn
es2126PortStatusSpdDpx=_Es2126PortStatusSpdDpx_Object((1,3,6,1,4,1,5205,2,16,1,9,1,2,1,6),_Es2126PortStatusSpdDpx_Type())
es2126PortStatusSpdDpx.setMaxAccess(_D)
if mibBuilder.loadTexts:es2126PortStatusSpdDpx.setStatus(_A)
_Es2126PortStatusRxPause_Type=DisplayString
_Es2126PortStatusRxPause_Object=MibTableColumn
es2126PortStatusRxPause=_Es2126PortStatusRxPause_Object((1,3,6,1,4,1,5205,2,16,1,9,1,2,1,7),_Es2126PortStatusRxPause_Type())
es2126PortStatusRxPause.setMaxAccess(_D)
if mibBuilder.loadTexts:es2126PortStatusRxPause.setStatus(_A)
_Es2126PortStatusTxPause_Type=DisplayString
_Es2126PortStatusTxPause_Object=MibTableColumn
es2126PortStatusTxPause=_Es2126PortStatusTxPause_Object((1,3,6,1,4,1,5205,2,16,1,9,1,2,1,8),_Es2126PortStatusTxPause_Type())
es2126PortStatusTxPause.setMaxAccess(_D)
if mibBuilder.loadTexts:es2126PortStatusTxPause.setStatus(_A)
_Es2126PortStatusDescription_Type=DisplayString
_Es2126PortStatusDescription_Object=MibTableColumn
es2126PortStatusDescription=_Es2126PortStatusDescription_Object((1,3,6,1,4,1,5205,2,16,1,9,1,2,1,9),_Es2126PortStatusDescription_Type())
es2126PortStatusDescription.setMaxAccess(_D)
if mibBuilder.loadTexts:es2126PortStatusDescription.setStatus(_A)
_Es2126PortConf_ObjectIdentity=ObjectIdentity
es2126PortConf=_Es2126PortConf_ObjectIdentity((1,3,6,1,4,1,5205,2,16,1,9,2))
class _Es2126PortConfNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_Es2126PortConfNumber_Type.__name__=_C
_Es2126PortConfNumber_Object=MibScalar
es2126PortConfNumber=_Es2126PortConfNumber_Object((1,3,6,1,4,1,5205,2,16,1,9,2,1),_Es2126PortConfNumber_Type())
es2126PortConfNumber.setMaxAccess(_D)
if mibBuilder.loadTexts:es2126PortConfNumber.setStatus(_A)
_Es2126PortConfTable_Object=MibTable
es2126PortConfTable=_Es2126PortConfTable_Object((1,3,6,1,4,1,5205,2,16,1,9,2,2))
if mibBuilder.loadTexts:es2126PortConfTable.setStatus(_A)
_Es2126PortConfEntry_Object=MibTableRow
es2126PortConfEntry=_Es2126PortConfEntry_Object((1,3,6,1,4,1,5205,2,16,1,9,2,2,1))
es2126PortConfEntry.setIndexNames((0,_E,_R))
if mibBuilder.loadTexts:es2126PortConfEntry.setStatus(_A)
class _Es2126PortConfIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_Es2126PortConfIndex_Type.__name__=_C
_Es2126PortConfIndex_Object=MibTableColumn
es2126PortConfIndex=_Es2126PortConfIndex_Object((1,3,6,1,4,1,5205,2,16,1,9,2,2,1,1),_Es2126PortConfIndex_Type())
es2126PortConfIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:es2126PortConfIndex.setStatus(_A)
class _Es2126PortConfPortState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1))
_Es2126PortConfPortState_Type.__name__=_C
_Es2126PortConfPortState_Object=MibTableColumn
es2126PortConfPortState=_Es2126PortConfPortState_Object((1,3,6,1,4,1,5205,2,16,1,9,2,2,1,2),_Es2126PortConfPortState_Type())
es2126PortConfPortState.setMaxAccess(_B)
if mibBuilder.loadTexts:es2126PortConfPortState.setStatus(_A)
class _Es2126PortConfSpdDpx_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,5))
_Es2126PortConfSpdDpx_Type.__name__=_C
_Es2126PortConfSpdDpx_Object=MibTableColumn
es2126PortConfSpdDpx=_Es2126PortConfSpdDpx_Object((1,3,6,1,4,1,5205,2,16,1,9,2,2,1,3),_Es2126PortConfSpdDpx_Type())
es2126PortConfSpdDpx.setMaxAccess(_B)
if mibBuilder.loadTexts:es2126PortConfSpdDpx.setStatus(_A)
class _Es2126PortConfFlwCtrl_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1))
_Es2126PortConfFlwCtrl_Type.__name__=_C
_Es2126PortConfFlwCtrl_Object=MibTableColumn
es2126PortConfFlwCtrl=_Es2126PortConfFlwCtrl_Object((1,3,6,1,4,1,5205,2,16,1,9,2,2,1,4),_Es2126PortConfFlwCtrl_Type())
es2126PortConfFlwCtrl.setMaxAccess(_B)
if mibBuilder.loadTexts:es2126PortConfFlwCtrl.setStatus(_A)
_Es2126PortConfDescription_Type=DisplayString
_Es2126PortConfDescription_Object=MibTableColumn
es2126PortConfDescription=_Es2126PortConfDescription_Object((1,3,6,1,4,1,5205,2,16,1,9,2,2,1,5),_Es2126PortConfDescription_Type())
es2126PortConfDescription.setMaxAccess(_B)
if mibBuilder.loadTexts:es2126PortConfDescription.setStatus(_A)
_Es2126PortBandwidth_ObjectIdentity=ObjectIdentity
es2126PortBandwidth=_Es2126PortBandwidth_ObjectIdentity((1,3,6,1,4,1,5205,2,16,1,9,3))
_Es2126PortBandwidthTable_Object=MibTable
es2126PortBandwidthTable=_Es2126PortBandwidthTable_Object((1,3,6,1,4,1,5205,2,16,1,9,3,1))
if mibBuilder.loadTexts:es2126PortBandwidthTable.setStatus(_A)
_Es2126PortBandwidthEntry_Object=MibTableRow
es2126PortBandwidthEntry=_Es2126PortBandwidthEntry_Object((1,3,6,1,4,1,5205,2,16,1,9,3,1,1))
es2126PortBandwidthEntry.setIndexNames((0,_E,_S))
if mibBuilder.loadTexts:es2126PortBandwidthEntry.setStatus(_A)
class _Es2126PortBandwidthIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,26))
_Es2126PortBandwidthIndex_Type.__name__=_C
_Es2126PortBandwidthIndex_Object=MibTableColumn
es2126PortBandwidthIndex=_Es2126PortBandwidthIndex_Object((1,3,6,1,4,1,5205,2,16,1,9,3,1,1,1),_Es2126PortBandwidthIndex_Type())
es2126PortBandwidthIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:es2126PortBandwidthIndex.setStatus(_A)
class _Es2126PortBandwidthIngressRate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(66,1024000))
_Es2126PortBandwidthIngressRate_Type.__name__=_C
_Es2126PortBandwidthIngressRate_Object=MibTableColumn
es2126PortBandwidthIngressRate=_Es2126PortBandwidthIngressRate_Object((1,3,6,1,4,1,5205,2,16,1,9,3,1,1,2),_Es2126PortBandwidthIngressRate_Type())
es2126PortBandwidthIngressRate.setMaxAccess(_B)
if mibBuilder.loadTexts:es2126PortBandwidthIngressRate.setStatus(_A)
class _Es2126PortBandwidthEgressRate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(66,1024000))
_Es2126PortBandwidthEgressRate_Type.__name__=_C
_Es2126PortBandwidthEgressRate_Object=MibTableColumn
es2126PortBandwidthEgressRate=_Es2126PortBandwidthEgressRate_Object((1,3,6,1,4,1,5205,2,16,1,9,3,1,1,3),_Es2126PortBandwidthEgressRate_Type())
es2126PortBandwidthEgressRate.setMaxAccess(_B)
if mibBuilder.loadTexts:es2126PortBandwidthEgressRate.setStatus(_A)
class _Es2126PortBandwidthStormType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4))
_Es2126PortBandwidthStormType_Type.__name__=_C
_Es2126PortBandwidthStormType_Object=MibScalar
es2126PortBandwidthStormType=_Es2126PortBandwidthStormType_Object((1,3,6,1,4,1,5205,2,16,1,9,3,2),_Es2126PortBandwidthStormType_Type())
es2126PortBandwidthStormType.setMaxAccess(_B)
if mibBuilder.loadTexts:es2126PortBandwidthStormType.setStatus(_A)
class _Es2126PortBandwidthStormRate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,100))
_Es2126PortBandwidthStormRate_Type.__name__=_C
_Es2126PortBandwidthStormRate_Object=MibScalar
es2126PortBandwidthStormRate=_Es2126PortBandwidthStormRate_Object((1,3,6,1,4,1,5205,2,16,1,9,3,3),_Es2126PortBandwidthStormRate_Type())
es2126PortBandwidthStormRate.setMaxAccess(_B)
if mibBuilder.loadTexts:es2126PortBandwidthStormRate.setStatus(_A)
_Es2126LoopDetectedConf_ObjectIdentity=ObjectIdentity
es2126LoopDetectedConf=_Es2126LoopDetectedConf_ObjectIdentity((1,3,6,1,4,1,5205,2,16,1,10))
class _Es2126LoopDetectedNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_Es2126LoopDetectedNumber_Type.__name__=_C
_Es2126LoopDetectedNumber_Object=MibScalar
es2126LoopDetectedNumber=_Es2126LoopDetectedNumber_Object((1,3,6,1,4,1,5205,2,16,1,10,1),_Es2126LoopDetectedNumber_Type())
es2126LoopDetectedNumber.setMaxAccess(_D)
if mibBuilder.loadTexts:es2126LoopDetectedNumber.setStatus(_A)
_Es2126LoopDetectedTable_Object=MibTable
es2126LoopDetectedTable=_Es2126LoopDetectedTable_Object((1,3,6,1,4,1,5205,2,16,1,10,2))
if mibBuilder.loadTexts:es2126LoopDetectedTable.setStatus(_A)
_Es2126LoopDetectedEntry_Object=MibTableRow
es2126LoopDetectedEntry=_Es2126LoopDetectedEntry_Object((1,3,6,1,4,1,5205,2,16,1,10,2,1))
es2126LoopDetectedEntry.setIndexNames((0,_E,_T))
if mibBuilder.loadTexts:es2126LoopDetectedEntry.setStatus(_A)
class _Es2126LoopDetectedfIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_Es2126LoopDetectedfIndex_Type.__name__=_C
_Es2126LoopDetectedfIndex_Object=MibTableColumn
es2126LoopDetectedfIndex=_Es2126LoopDetectedfIndex_Object((1,3,6,1,4,1,5205,2,16,1,10,2,1,1),_Es2126LoopDetectedfIndex_Type())
es2126LoopDetectedfIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:es2126LoopDetectedfIndex.setStatus(_A)
class _Es2126LoopDetectedStateEbl_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1))
_Es2126LoopDetectedStateEbl_Type.__name__=_C
_Es2126LoopDetectedStateEbl_Object=MibTableColumn
es2126LoopDetectedStateEbl=_Es2126LoopDetectedStateEbl_Object((1,3,6,1,4,1,5205,2,16,1,10,2,1,2),_Es2126LoopDetectedStateEbl_Type())
es2126LoopDetectedStateEbl.setMaxAccess(_B)
if mibBuilder.loadTexts:es2126LoopDetectedStateEbl.setStatus(_A)
class _Es2126LoopDetectedCurrentStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1))
_Es2126LoopDetectedCurrentStatus_Type.__name__=_C
_Es2126LoopDetectedCurrentStatus_Object=MibTableColumn
es2126LoopDetectedCurrentStatus=_Es2126LoopDetectedCurrentStatus_Object((1,3,6,1,4,1,5205,2,16,1,10,2,1,3),_Es2126LoopDetectedCurrentStatus_Type())
es2126LoopDetectedCurrentStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:es2126LoopDetectedCurrentStatus.setStatus(_A)
class _Es2126LoopDetectedResumed_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1))
_Es2126LoopDetectedResumed_Type.__name__=_C
_Es2126LoopDetectedResumed_Object=MibTableColumn
es2126LoopDetectedResumed=_Es2126LoopDetectedResumed_Object((1,3,6,1,4,1,5205,2,16,1,10,2,1,4),_Es2126LoopDetectedResumed_Type())
es2126LoopDetectedResumed.setMaxAccess(_B)
if mibBuilder.loadTexts:es2126LoopDetectedResumed.setStatus(_A)
class _Es2126LoopDetectedAction_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1))
_Es2126LoopDetectedAction_Type.__name__=_C
_Es2126LoopDetectedAction_Object=MibScalar
es2126LoopDetectedAction=_Es2126LoopDetectedAction_Object((1,3,6,1,4,1,5205,2,16,1,10,3),_Es2126LoopDetectedAction_Type())
es2126LoopDetectedAction.setMaxAccess(_B)
if mibBuilder.loadTexts:es2126LoopDetectedAction.setStatus(_A)
_Es2126TrapEntry_ObjectIdentity=ObjectIdentity
es2126TrapEntry=_Es2126TrapEntry_ObjectIdentity((1,3,6,1,4,1,5205,2,16,1,20))
_Es2126TrapVariable_ObjectIdentity=ObjectIdentity
es2126TrapVariable=_Es2126TrapVariable_ObjectIdentity((1,3,6,1,4,1,5205,2,16,1,21))
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
es2126ModuleInserted=NotificationType((1,3,6,1,4,1,5205,2,16,1,20,1))
es2126ModuleInserted.setObjects((_F,_G))
if mibBuilder.loadTexts:es2126ModuleInserted.setStatus(_A)
es2126ModuleRemoved=NotificationType((1,3,6,1,4,1,5205,2,16,1,20,2))
es2126ModuleRemoved.setObjects((_F,_G))
if mibBuilder.loadTexts:es2126ModuleRemoved.setStatus(_A)
es2126DualMediaSwapped=NotificationType((1,3,6,1,4,1,5205,2,16,1,20,3))
es2126DualMediaSwapped.setObjects((_F,_G))
if mibBuilder.loadTexts:es2126DualMediaSwapped.setStatus(_A)
es2126LoopDetected=NotificationType((1,3,6,1,4,1,5205,2,16,1,20,4))
es2126LoopDetected.setObjects((_F,_G))
if mibBuilder.loadTexts:es2126LoopDetected.setStatus(_A)
es2126StpStateDisabled=NotificationType((1,3,6,1,4,1,5205,2,16,1,20,100))
if mibBuilder.loadTexts:es2126StpStateDisabled.setStatus(_A)
es2126StpStateEnabled=NotificationType((1,3,6,1,4,1,5205,2,16,1,20,101))
if mibBuilder.loadTexts:es2126StpStateEnabled.setStatus(_A)
es2126StpTopologyChanged=NotificationType((1,3,6,1,4,1,5205,2,16,1,20,102))
es2126StpTopologyChanged.setObjects((_F,_G))
if mibBuilder.loadTexts:es2126StpTopologyChanged.setStatus(_A)
es2126RmonRisingAlarm=NotificationType((1,3,6,1,4,1,5205,2,16,1,20,110))
if mibBuilder.loadTexts:es2126RmonRisingAlarm.setStatus(_A)
es2126RmonFallingAlarm=NotificationType((1,3,6,1,4,1,5205,2,16,1,20,111))
if mibBuilder.loadTexts:es2126RmonFallingAlarm.setStatus(_A)
es2126LacpStateDisabled=NotificationType((1,3,6,1,4,1,5205,2,16,1,20,120))
es2126LacpStateDisabled.setObjects(*((_F,_G),(_E,_H)))
if mibBuilder.loadTexts:es2126LacpStateDisabled.setStatus(_A)
es2126LacpStateEnabled=NotificationType((1,3,6,1,4,1,5205,2,16,1,20,121))
es2126LacpStateEnabled.setObjects(*((_F,_G),(_E,_H)))
if mibBuilder.loadTexts:es2126LacpStateEnabled.setStatus(_A)
es2126LacpPortAdded=NotificationType((1,3,6,1,4,1,5205,2,16,1,20,123))
es2126LacpPortAdded.setObjects(*((_F,_G),(_E,_I),(_E,_J)))
if mibBuilder.loadTexts:es2126LacpPortAdded.setStatus(_A)
es2126LacpPortTrunkFailure=NotificationType((1,3,6,1,4,1,5205,2,16,1,20,124))
es2126LacpPortTrunkFailure.setObjects(*((_F,_G),(_E,_I),(_E,_J)))
if mibBuilder.loadTexts:es2126LacpPortTrunkFailure.setStatus(_A)
es2126GvrpStateDisabled=NotificationType((1,3,6,1,4,1,5205,2,16,1,20,140))
if mibBuilder.loadTexts:es2126GvrpStateDisabled.setStatus(_A)
es2126GvrpStateEnabled=NotificationType((1,3,6,1,4,1,5205,2,16,1,20,141))
if mibBuilder.loadTexts:es2126GvrpStateEnabled.setStatus(_A)
es2126VlanPortBaseEnabled=NotificationType((1,3,6,1,4,1,5205,2,16,1,20,151))
if mibBuilder.loadTexts:es2126VlanPortBaseEnabled.setStatus(_A)
es2126VlanTagBaseEnabled=NotificationType((1,3,6,1,4,1,5205,2,16,1,20,152))
if mibBuilder.loadTexts:es2126VlanTagBaseEnabled.setStatus(_A)
es2126VlanMetroBaseEnabled=NotificationType((1,3,6,1,4,1,5205,2,16,1,20,153))
if mibBuilder.loadTexts:es2126VlanMetroBaseEnabled.setStatus(_A)
es2126UserLogin=NotificationType((1,3,6,1,4,1,5205,2,16,1,20,200))
es2126UserLogin.setObjects((_E,_K))
if mibBuilder.loadTexts:es2126UserLogin.setStatus(_A)
es2126UserLogout=NotificationType((1,3,6,1,4,1,5205,2,16,1,20,201))
es2126UserLogout.setObjects((_E,_K))
if mibBuilder.loadTexts:es2126UserLogout.setStatus(_A)
mibBuilder.exportSymbols(_E,**{'rubytech':rubytech,'switch':switch,'es2126ProductID':es2126ProductID,'es2126Produces':es2126Produces,'es2126System':es2126System,'es2126CommonSys':es2126CommonSys,'es2126Reboot':es2126Reboot,'es2126BiosVsersion':es2126BiosVsersion,'es2126FirmwareVersion':es2126FirmwareVersion,'es2126HardwareVersion':es2126HardwareVersion,'es2126MechanicalVersion':es2126MechanicalVersion,'es2126SerialNumber':es2126SerialNumber,'es2126HostMacAddress':es2126HostMacAddress,'es2126DevicePort':es2126DevicePort,'es2126RamSize':es2126RamSize,'es2126FlashSize':es2126FlashSize,'es2126IP':es2126IP,'es2126DhcpSetting':es2126DhcpSetting,'es2126IPAddress':es2126IPAddress,'es2126NetMask':es2126NetMask,'es2126DefaultGateway':es2126DefaultGateway,'es2126DnsSetting':es2126DnsSetting,'es2126DnsServer':es2126DnsServer,'es2126Time':es2126Time,'es2126SystemCurrentTime':es2126SystemCurrentTime,'es2126ManualTimeSetting':es2126ManualTimeSetting,'es2126NTPServer':es2126NTPServer,'es2126NTPTimeZone':es2126NTPTimeZone,'es2126NTPTimeSync':es2126NTPTimeSync,'es2126DaylightSavingTime':es2126DaylightSavingTime,'es2126DaylightStartTime':es2126DaylightStartTime,'es2126DaylightEndTime':es2126DaylightEndTime,'es2126Account':es2126Account,'es2126AccountNumber':es2126AccountNumber,'es2126AccountTable':es2126AccountTable,'es2126AccountEntry':es2126AccountEntry,_L:es2126AccountIndex,'es2126AccountAuthorization':es2126AccountAuthorization,'es2126AccountName':es2126AccountName,'es2126AccountPassword':es2126AccountPassword,'es2126AccountAddName':es2126AccountAddName,'es2126AccountAddPassword':es2126AccountAddPassword,'es2126DoAccountAdd':es2126DoAccountAdd,'es2126AccountDel':es2126AccountDel,'es2126Snmp':es2126Snmp,'es2126GetCommunity':es2126GetCommunity,'es2126SetCommunity':es2126SetCommunity,'es2126TrapHostNumber':es2126TrapHostNumber,'es2126TrapHostTable':es2126TrapHostTable,'es2126TrapHostEntry':es2126TrapHostEntry,_M:es2126TrapHostIndex,'es2126TrapHostIP':es2126TrapHostIP,'es2126TrapHostPort':es2126TrapHostPort,'es2126TrapHostCommunity':es2126TrapHostCommunity,'es2126TrapBootDelayTime':es2126TrapBootDelayTime,'es2126Alarm':es2126Alarm,'es2126Event':es2126Event,'es2126EventNumber':es2126EventNumber,'es2126EventTable':es2126EventTable,'es2126EventEntry':es2126EventEntry,_N:es2126EventIndex,'es2126EventName':es2126EventName,'es2126EventSendEmail':es2126EventSendEmail,'es2126EventSendTrap':es2126EventSendTrap,'es2126Email':es2126Email,'es2126EmailServer':es2126EmailServer,'es2126EmailUsername':es2126EmailUsername,'es2126EmailPassword':es2126EmailPassword,'es2126EmailSender':es2126EmailSender,'es2126EmailReturnPath':es2126EmailReturnPath,'es2126EmailUserNumber':es2126EmailUserNumber,'es2126EmailUserTable':es2126EmailUserTable,'es2126EmailUserEntry':es2126EmailUserEntry,_O:es2126EmailUserIndex,'es2126EmailUserAddress':es2126EmailUserAddress,'es2126Tftp':es2126Tftp,'es2126TftpServer':es2126TftpServer,'es2126Configuration':es2126Configuration,'es2126SaveRestore':es2126SaveRestore,'es2126SaveStart':es2126SaveStart,'es2126SaveUser':es2126SaveUser,'es2126RestoreDefault':es2126RestoreDefault,'es2126RestoreUser':es2126RestoreUser,'es2126ConfigFile':es2126ConfigFile,'es2126ExportConfigName':es2126ExportConfigName,'es2126DoExportConfig':es2126DoExportConfig,'es2126ImportConfigName':es2126ImportConfigName,'es2126DoImportConfig':es2126DoImportConfig,'es2126Diagnostic':es2126Diagnostic,'es2126InternalLoopbackTest':es2126InternalLoopbackTest,'es2126ExternalLoopbackTest':es2126ExternalLoopbackTest,'es2126PingTest':es2126PingTest,'es2126Watchdog':es2126Watchdog,'es2126WatchdogState':es2126WatchdogState,'es2126WatchdogTimeGap':es2126WatchdogTimeGap,'es2126WatchdogHost':es2126WatchdogHost,'es2126WatchdogResetMgtInf':es2126WatchdogResetMgtInf,'es2126WatchdogResetMgtInfCount':es2126WatchdogResetMgtInfCount,'es2126WatchdogResetSystem':es2126WatchdogResetSystem,'es2126WatchdogResetSystemCount':es2126WatchdogResetSystemCount,'es2126Log':es2126Log,'es2126ClearLog':es2126ClearLog,'es2126UploadLog':es2126UploadLog,'es2126AutoUploadLogState':es2126AutoUploadLogState,'es2126LogNumber':es2126LogNumber,'es2126LogTable':es2126LogTable,'es2126LogEntry':es2126LogEntry,_P:es2126LogIndex,'es2126LogEvent':es2126LogEvent,'es2126Firmware':es2126Firmware,'es2126FirmwareFileName':es2126FirmwareFileName,'es2126DoFirmwareUpgrade':es2126DoFirmwareUpgrade,'es2126Port':es2126Port,'es2126PortStatus':es2126PortStatus,'es2126PortStatusNumber':es2126PortStatusNumber,'es2126PortStatusTable':es2126PortStatusTable,'es2126PortStatusEntry':es2126PortStatusEntry,_Q:es2126PortStatusIndex,'es2126PortStatusMedia':es2126PortStatusMedia,'es2126PortStatusLink':es2126PortStatusLink,'es2126PortStatusPortState':es2126PortStatusPortState,'es2126PortStatusAutoNego':es2126PortStatusAutoNego,'es2126PortStatusSpdDpx':es2126PortStatusSpdDpx,'es2126PortStatusRxPause':es2126PortStatusRxPause,'es2126PortStatusTxPause':es2126PortStatusTxPause,'es2126PortStatusDescription':es2126PortStatusDescription,'es2126PortConf':es2126PortConf,'es2126PortConfNumber':es2126PortConfNumber,'es2126PortConfTable':es2126PortConfTable,'es2126PortConfEntry':es2126PortConfEntry,_R:es2126PortConfIndex,'es2126PortConfPortState':es2126PortConfPortState,'es2126PortConfSpdDpx':es2126PortConfSpdDpx,'es2126PortConfFlwCtrl':es2126PortConfFlwCtrl,'es2126PortConfDescription':es2126PortConfDescription,'es2126PortBandwidth':es2126PortBandwidth,'es2126PortBandwidthTable':es2126PortBandwidthTable,'es2126PortBandwidthEntry':es2126PortBandwidthEntry,_S:es2126PortBandwidthIndex,'es2126PortBandwidthIngressRate':es2126PortBandwidthIngressRate,'es2126PortBandwidthEgressRate':es2126PortBandwidthEgressRate,'es2126PortBandwidthStormType':es2126PortBandwidthStormType,'es2126PortBandwidthStormRate':es2126PortBandwidthStormRate,'es2126LoopDetectedConf':es2126LoopDetectedConf,'es2126LoopDetectedNumber':es2126LoopDetectedNumber,'es2126LoopDetectedTable':es2126LoopDetectedTable,'es2126LoopDetectedEntry':es2126LoopDetectedEntry,_T:es2126LoopDetectedfIndex,'es2126LoopDetectedStateEbl':es2126LoopDetectedStateEbl,'es2126LoopDetectedCurrentStatus':es2126LoopDetectedCurrentStatus,'es2126LoopDetectedResumed':es2126LoopDetectedResumed,'es2126LoopDetectedAction':es2126LoopDetectedAction,'es2126TrapEntry':es2126TrapEntry,'es2126ModuleInserted':es2126ModuleInserted,'es2126ModuleRemoved':es2126ModuleRemoved,'es2126DualMediaSwapped':es2126DualMediaSwapped,'es2126LoopDetected':es2126LoopDetected,'es2126StpStateDisabled':es2126StpStateDisabled,'es2126StpStateEnabled':es2126StpStateEnabled,'es2126StpTopologyChanged':es2126StpTopologyChanged,'es2126RmonRisingAlarm':es2126RmonRisingAlarm,'es2126RmonFallingAlarm':es2126RmonFallingAlarm,'es2126LacpStateDisabled':es2126LacpStateDisabled,'es2126LacpStateEnabled':es2126LacpStateEnabled,'es2126LacpPortAdded':es2126LacpPortAdded,'es2126LacpPortTrunkFailure':es2126LacpPortTrunkFailure,'es2126GvrpStateDisabled':es2126GvrpStateDisabled,'es2126GvrpStateEnabled':es2126GvrpStateEnabled,'es2126VlanPortBaseEnabled':es2126VlanPortBaseEnabled,'es2126VlanTagBaseEnabled':es2126VlanTagBaseEnabled,'es2126VlanMetroBaseEnabled':es2126VlanMetroBaseEnabled,'es2126UserLogin':es2126UserLogin,'es2126UserLogout':es2126UserLogout,'es2126TrapVariable':es2126TrapVariable,_K:username,_H:groupId,_I:actorkey,_J:partnerkey,'uplink':uplink})