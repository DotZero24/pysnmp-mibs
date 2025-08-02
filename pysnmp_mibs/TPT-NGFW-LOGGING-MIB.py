_X='tptNgfwLoggingNotificationGroup'
_W='tptNgfwLoggingGroup'
_V='tptNgfwVpnLogNotify'
_U='tptNgfwAuditLogNotify'
_T='tptNgfwSysLogNotify'
_S='tptNgfwAuditLogNotifyMessage'
_R='tptNgfwAuditLogNotifyUser'
_Q='tptNgfwAuditLogNotifyResult'
_P='tptNgfwAuditLogNotifyCategory'
_O='tptNgfwAuditLogNotifyIpAddr'
_N='tptNgfwAuditLogNotifyIpAddrType'
_M='tptNgfwAuditLogNotifyType'
_L='tptNgfwAuditLogNotifyAccess'
_K='tptNgfwLogNotifyHost'
_J='tptNgfwLogNotifyText'
_I='tptNgfwLogNotifySeverity'
_H='tptNgfwLogNotifySource'
_G='tptNgfwSystemSerial'
_F='TPT-NGFW-SYSTEM-INFO-MIB'
_E='tptNgfwLogNotifyTime'
_D='SnmpAdminString'
_C='accessible-for-notify'
_B='current'
_A='TPT-NGFW-LOGGING-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress','InetAddressType')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB',_D)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DateAndTime,DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime','DisplayString','PhysAddress','TextualConvention')
Severity,tpt_ngfw_compls,tpt_ngfw_eventsV2,tpt_ngfw_groups,tpt_ngfw_objs,tpt_ngfw_params=mibBuilder.importSymbols('TPT-NGFW-REG-MIB','Severity','tpt-ngfw-compls','tpt-ngfw-eventsV2','tpt-ngfw-groups','tpt-ngfw-objs','tpt-ngfw-params')
tptNgfwSystemSerial,=mibBuilder.importSymbols(_F,_G)
tptNgfwLogging=ModuleIdentity((1,3,6,1,4,1,10734,3,9,2,5))
if mibBuilder.loadTexts:tptNgfwLogging.setRevisions(('2016-05-25 18:54','2013-03-13 12:00'))
class AuditLogResult(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('success',1),('failed',2)))
class AuditLogCategory(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24)));namedValues=NamedValues(*(('undefined',1),('general',2),('login',3),('logout',4),('user',5),('time',6),('policy',7),('update',8),('boot',9),('report',10),('host',11),('cfg',12),('device',13),('sms',14),('server',15),('segment',16),('license',17),('ha',18),('monitor',19),('ipFilter',20),('connTable',21),('hostComm',22),('tse',23),('cf',24)))
_TptNgfwLogNotifyTime_Type=DateAndTime
_TptNgfwLogNotifyTime_Object=MibScalar
tptNgfwLogNotifyTime=_TptNgfwLogNotifyTime_Object((1,3,6,1,4,1,10734,3,9,3,1,60),_TptNgfwLogNotifyTime_Type())
tptNgfwLogNotifyTime.setMaxAccess(_C)
if mibBuilder.loadTexts:tptNgfwLogNotifyTime.setStatus(_B)
class _TptNgfwLogNotifyHost_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_TptNgfwLogNotifyHost_Type.__name__=_D
_TptNgfwLogNotifyHost_Object=MibScalar
tptNgfwLogNotifyHost=_TptNgfwLogNotifyHost_Object((1,3,6,1,4,1,10734,3,9,3,1,61),_TptNgfwLogNotifyHost_Type())
tptNgfwLogNotifyHost.setMaxAccess(_C)
if mibBuilder.loadTexts:tptNgfwLogNotifyHost.setStatus(_B)
class _TptNgfwLogNotifySource_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,80))
_TptNgfwLogNotifySource_Type.__name__=_D
_TptNgfwLogNotifySource_Object=MibScalar
tptNgfwLogNotifySource=_TptNgfwLogNotifySource_Object((1,3,6,1,4,1,10734,3,9,3,1,62),_TptNgfwLogNotifySource_Type())
tptNgfwLogNotifySource.setMaxAccess(_C)
if mibBuilder.loadTexts:tptNgfwLogNotifySource.setStatus(_B)
_TptNgfwLogNotifySeverity_Type=Severity
_TptNgfwLogNotifySeverity_Object=MibScalar
tptNgfwLogNotifySeverity=_TptNgfwLogNotifySeverity_Object((1,3,6,1,4,1,10734,3,9,3,1,63),_TptNgfwLogNotifySeverity_Type())
tptNgfwLogNotifySeverity.setMaxAccess(_C)
if mibBuilder.loadTexts:tptNgfwLogNotifySeverity.setStatus(_B)
class _TptNgfwLogNotifyText_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,4096))
_TptNgfwLogNotifyText_Type.__name__=_D
_TptNgfwLogNotifyText_Object=MibScalar
tptNgfwLogNotifyText=_TptNgfwLogNotifyText_Object((1,3,6,1,4,1,10734,3,9,3,1,64),_TptNgfwLogNotifyText_Type())
tptNgfwLogNotifyText.setMaxAccess(_C)
if mibBuilder.loadTexts:tptNgfwLogNotifyText.setStatus(_B)
_TptNgfwAuditLogNotifyAccess_Type=Unsigned32
_TptNgfwAuditLogNotifyAccess_Object=MibScalar
tptNgfwAuditLogNotifyAccess=_TptNgfwAuditLogNotifyAccess_Object((1,3,6,1,4,1,10734,3,9,3,1,65),_TptNgfwAuditLogNotifyAccess_Type())
tptNgfwAuditLogNotifyAccess.setMaxAccess(_C)
if mibBuilder.loadTexts:tptNgfwAuditLogNotifyAccess.setStatus(_B)
class _TptNgfwAuditLogNotifyType_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,40))
_TptNgfwAuditLogNotifyType_Type.__name__=_D
_TptNgfwAuditLogNotifyType_Object=MibScalar
tptNgfwAuditLogNotifyType=_TptNgfwAuditLogNotifyType_Object((1,3,6,1,4,1,10734,3,9,3,1,66),_TptNgfwAuditLogNotifyType_Type())
tptNgfwAuditLogNotifyType.setMaxAccess(_C)
if mibBuilder.loadTexts:tptNgfwAuditLogNotifyType.setStatus(_B)
_TptNgfwAuditLogNotifyIpAddrType_Type=InetAddressType
_TptNgfwAuditLogNotifyIpAddrType_Object=MibScalar
tptNgfwAuditLogNotifyIpAddrType=_TptNgfwAuditLogNotifyIpAddrType_Object((1,3,6,1,4,1,10734,3,9,3,1,67),_TptNgfwAuditLogNotifyIpAddrType_Type())
tptNgfwAuditLogNotifyIpAddrType.setMaxAccess(_C)
if mibBuilder.loadTexts:tptNgfwAuditLogNotifyIpAddrType.setStatus(_B)
_TptNgfwAuditLogNotifyIpAddr_Type=InetAddress
_TptNgfwAuditLogNotifyIpAddr_Object=MibScalar
tptNgfwAuditLogNotifyIpAddr=_TptNgfwAuditLogNotifyIpAddr_Object((1,3,6,1,4,1,10734,3,9,3,1,68),_TptNgfwAuditLogNotifyIpAddr_Type())
tptNgfwAuditLogNotifyIpAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:tptNgfwAuditLogNotifyIpAddr.setStatus(_B)
_TptNgfwAuditLogNotifyCategory_Type=AuditLogCategory
_TptNgfwAuditLogNotifyCategory_Object=MibScalar
tptNgfwAuditLogNotifyCategory=_TptNgfwAuditLogNotifyCategory_Object((1,3,6,1,4,1,10734,3,9,3,1,69),_TptNgfwAuditLogNotifyCategory_Type())
tptNgfwAuditLogNotifyCategory.setMaxAccess(_C)
if mibBuilder.loadTexts:tptNgfwAuditLogNotifyCategory.setStatus(_B)
_TptNgfwAuditLogNotifyResult_Type=AuditLogResult
_TptNgfwAuditLogNotifyResult_Object=MibScalar
tptNgfwAuditLogNotifyResult=_TptNgfwAuditLogNotifyResult_Object((1,3,6,1,4,1,10734,3,9,3,1,70),_TptNgfwAuditLogNotifyResult_Type())
tptNgfwAuditLogNotifyResult.setMaxAccess(_C)
if mibBuilder.loadTexts:tptNgfwAuditLogNotifyResult.setStatus(_B)
class _TptNgfwAuditLogNotifyUser_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,80))
_TptNgfwAuditLogNotifyUser_Type.__name__=_D
_TptNgfwAuditLogNotifyUser_Object=MibScalar
tptNgfwAuditLogNotifyUser=_TptNgfwAuditLogNotifyUser_Object((1,3,6,1,4,1,10734,3,9,3,1,71),_TptNgfwAuditLogNotifyUser_Type())
tptNgfwAuditLogNotifyUser.setMaxAccess(_C)
if mibBuilder.loadTexts:tptNgfwAuditLogNotifyUser.setStatus(_B)
class _TptNgfwAuditLogNotifyMessage_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,4096))
_TptNgfwAuditLogNotifyMessage_Type.__name__=_D
_TptNgfwAuditLogNotifyMessage_Object=MibScalar
tptNgfwAuditLogNotifyMessage=_TptNgfwAuditLogNotifyMessage_Object((1,3,6,1,4,1,10734,3,9,3,1,72),_TptNgfwAuditLogNotifyMessage_Type())
tptNgfwAuditLogNotifyMessage.setMaxAccess(_C)
if mibBuilder.loadTexts:tptNgfwAuditLogNotifyMessage.setStatus(_B)
tptNgfwLoggingGroup=ObjectGroup((1,3,6,1,4,1,10734,3,9,1,1,9))
tptNgfwLoggingGroup.setObjects(*((_A,_E),(_A,_K),(_A,_H),(_A,_I),(_A,_J),(_A,_L),(_A,_M),(_A,_N),(_A,_O),(_A,_P),(_A,_Q),(_A,_R),(_A,_S)))
if mibBuilder.loadTexts:tptNgfwLoggingGroup.setStatus(_B)
tptNgfwSysLogNotify=NotificationType((1,3,6,1,4,1,10734,3,9,3,0,15))
tptNgfwSysLogNotify.setObjects(*((_F,_G),(_A,_E),(_A,_K),(_A,_H),(_A,_I),(_A,_J)))
if mibBuilder.loadTexts:tptNgfwSysLogNotify.setStatus(_B)
tptNgfwAuditLogNotify=NotificationType((1,3,6,1,4,1,10734,3,9,3,0,16))
tptNgfwAuditLogNotify.setObjects(*((_F,_G),(_A,_E),(_A,_L),(_A,_M),(_A,_N),(_A,_O),(_A,_P),(_A,_Q),(_A,_R),(_A,_S)))
if mibBuilder.loadTexts:tptNgfwAuditLogNotify.setStatus(_B)
tptNgfwVpnLogNotify=NotificationType((1,3,6,1,4,1,10734,3,9,3,0,17))
tptNgfwVpnLogNotify.setObjects(*((_F,_G),(_A,_E),(_A,_I),(_A,_H),(_A,_J)))
if mibBuilder.loadTexts:tptNgfwVpnLogNotify.setStatus(_B)
tptNgfwLoggingNotificationGroup=NotificationGroup((1,3,6,1,4,1,10734,3,9,1,1,10))
tptNgfwLoggingNotificationGroup.setObjects(*((_A,_T),(_A,_U),(_A,_V)))
if mibBuilder.loadTexts:tptNgfwLoggingNotificationGroup.setStatus(_B)
tptNgfwLoggingCompl=ModuleCompliance((1,3,6,1,4,1,10734,3,9,1,2,3))
tptNgfwLoggingCompl.setObjects(*((_A,_W),(_A,_X)))
if mibBuilder.loadTexts:tptNgfwLoggingCompl.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'AuditLogResult':AuditLogResult,'AuditLogCategory':AuditLogCategory,_W:tptNgfwLoggingGroup,_X:tptNgfwLoggingNotificationGroup,'tptNgfwLoggingCompl':tptNgfwLoggingCompl,'tptNgfwLogging':tptNgfwLogging,_T:tptNgfwSysLogNotify,_U:tptNgfwAuditLogNotify,_V:tptNgfwVpnLogNotify,_E:tptNgfwLogNotifyTime,_K:tptNgfwLogNotifyHost,_H:tptNgfwLogNotifySource,_I:tptNgfwLogNotifySeverity,_J:tptNgfwLogNotifyText,_L:tptNgfwAuditLogNotifyAccess,_M:tptNgfwAuditLogNotifyType,_N:tptNgfwAuditLogNotifyIpAddrType,_O:tptNgfwAuditLogNotifyIpAddr,_P:tptNgfwAuditLogNotifyCategory,_Q:tptNgfwAuditLogNotifyResult,_R:tptNgfwAuditLogNotifyUser,_S:tptNgfwAuditLogNotifyMessage})