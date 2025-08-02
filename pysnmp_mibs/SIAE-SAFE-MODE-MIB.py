_G='DisplayString'
_F='IpAddress'
_E='AlarmSeverityCode'
_D='read-only'
_C='Integer32'
_B='read-write'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
AlarmSeverityCode,AlarmStatus=mibBuilder.importSymbols('SIAE-ALARM-MIB',_E,'AlarmStatus')
siaeMib,=mibBuilder.importSymbols('SIAE-TREE-MIB','siaeMib')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,_F,'ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_G,'PhysAddress','TextualConvention')
safeMode=ModuleIdentity((1,3,6,1,4,1,3373,1103,99))
if mibBuilder.loadTexts:safeMode.setRevisions(('2016-03-10 00:00',))
_SafeModeMibVersion_Type=Integer32
_SafeModeMibVersion_Object=MibScalar
safeModeMibVersion=_SafeModeMibVersion_Object((1,3,6,1,4,1,3373,1103,99,1),_SafeModeMibVersion_Type())
safeModeMibVersion.setMaxAccess(_D)
if mibBuilder.loadTexts:safeModeMibVersion.setStatus(_A)
_SafeModeAlarm_Type=AlarmStatus
_SafeModeAlarm_Object=MibScalar
safeModeAlarm=_SafeModeAlarm_Object((1,3,6,1,4,1,3373,1103,99,2),_SafeModeAlarm_Type())
safeModeAlarm.setMaxAccess(_D)
if mibBuilder.loadTexts:safeModeAlarm.setStatus(_A)
class _SafeModeAlarmSeverityCode_Type(AlarmSeverityCode):defaultValue=4
_SafeModeAlarmSeverityCode_Type.__name__=_E
_SafeModeAlarmSeverityCode_Object=MibScalar
safeModeAlarmSeverityCode=_SafeModeAlarmSeverityCode_Object((1,3,6,1,4,1,3373,1103,99,3),_SafeModeAlarmSeverityCode_Type())
safeModeAlarmSeverityCode.setMaxAccess(_B)
if mibBuilder.loadTexts:safeModeAlarmSeverityCode.setStatus(_A)
class _SafeModeStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*(('safeModeStatusInactive',1),('safeModeStatusNoAuxService',2),('safeModeStatusLinkMngmt',3),('safeModeStatusSiteMngmt',4),('safeModeStatusSiteDefault',5),('safeModeStatusSiteRescue',6)))
_SafeModeStatus_Type.__name__=_C
_SafeModeStatus_Object=MibScalar
safeModeStatus=_SafeModeStatus_Object((1,3,6,1,4,1,3373,1103,99,4),_SafeModeStatus_Type())
safeModeStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:safeModeStatus.setStatus(_A)
class _SafeModeRescueAdminStatus_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('disable',1),('enable',2)))
_SafeModeRescueAdminStatus_Type.__name__=_C
_SafeModeRescueAdminStatus_Object=MibScalar
safeModeRescueAdminStatus=_SafeModeRescueAdminStatus_Object((1,3,6,1,4,1,3373,1103,99,5),_SafeModeRescueAdminStatus_Type())
safeModeRescueAdminStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:safeModeRescueAdminStatus.setStatus(_A)
class _SafeModeRescuePwd_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,31))
_SafeModeRescuePwd_Type.__name__=_G
_SafeModeRescuePwd_Object=MibScalar
safeModeRescuePwd=_SafeModeRescuePwd_Object((1,3,6,1,4,1,3373,1103,99,6),_SafeModeRescuePwd_Type())
safeModeRescuePwd.setMaxAccess(_B)
if mibBuilder.loadTexts:safeModeRescuePwd.setStatus(_A)
class _SafeModeRescueIpAddress_Type(IpAddress):defaultHexValue='ac14fd0d'
_SafeModeRescueIpAddress_Type.__name__=_F
_SafeModeRescueIpAddress_Object=MibScalar
safeModeRescueIpAddress=_SafeModeRescueIpAddress_Object((1,3,6,1,4,1,3373,1103,99,7),_SafeModeRescueIpAddress_Type())
safeModeRescueIpAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:safeModeRescueIpAddress.setStatus(_A)
_SafeModeRescueIpNetMask_Type=IpAddress
_SafeModeRescueIpNetMask_Object=MibScalar
safeModeRescueIpNetMask=_SafeModeRescueIpNetMask_Object((1,3,6,1,4,1,3373,1103,99,8),_SafeModeRescueIpNetMask_Type())
safeModeRescueIpNetMask.setMaxAccess(_B)
if mibBuilder.loadTexts:safeModeRescueIpNetMask.setStatus(_A)
mibBuilder.exportSymbols('SIAE-SAFE-MODE-MIB',**{'safeMode':safeMode,'safeModeMibVersion':safeModeMibVersion,'safeModeAlarm':safeModeAlarm,'safeModeAlarmSeverityCode':safeModeAlarmSeverityCode,'safeModeStatus':safeModeStatus,'safeModeRescueAdminStatus':safeModeRescueAdminStatus,'safeModeRescuePwd':safeModeRescuePwd,'safeModeRescueIpAddress':safeModeRescueIpAddress,'safeModeRescueIpNetMask':safeModeRescueIpNetMask})