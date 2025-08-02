_S='tptNgfwUserNotificationGroup'
_R='tptNgfwUserGroup'
_Q='tptNgfwUserAuthLockedIpNotify'
_P='tptNgfwUserAuthLockedAccountNotify'
_O='tptNgfwUserAuthFailNotify'
_N='tptNgfwUserAuthFailNotifyReason'
_M='tptNgfwUserAuthLockedTime'
_L='tptNgfwUserAuthNotifySource'
_K='tptNgfwUserAuthName'
_J='tptNgfwSystemSerial'
_I='TPT-NGFW-SYSTEM-INFO-MIB'
_H='tptNgfwNotifySeverity'
_G='TPT-NGFW-REG-MIB'
_F='SnmpAdminString'
_E='tptNgfwUserAuthSrcIpAddr'
_D='tptNgfwUserAuthSrcIpAddrType'
_C='accessible-for-notify'
_B='current'
_A='TPT-NGFW-USER-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress','InetAddressType')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB',_F)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DateAndTime,DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime','DisplayString','PhysAddress','TextualConvention')
tpt_ngfw_compls,tpt_ngfw_eventsV2,tpt_ngfw_groups,tpt_ngfw_objs,tpt_ngfw_params,tptNgfwNotifySeverity=mibBuilder.importSymbols(_G,'tpt-ngfw-compls','tpt-ngfw-eventsV2','tpt-ngfw-groups','tpt-ngfw-objs','tpt-ngfw-params',_H)
tptNgfwSystemSerial,=mibBuilder.importSymbols(_I,_J)
tptNgfwPolicy=ModuleIdentity((1,3,6,1,4,1,10734,3,9,2,4))
if mibBuilder.loadTexts:tptNgfwPolicy.setRevisions(('2016-05-25 18:54','2013-04-03 12:00'))
class _TptNgfwUserAuthName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,40))
_TptNgfwUserAuthName_Type.__name__=_F
_TptNgfwUserAuthName_Object=MibScalar
tptNgfwUserAuthName=_TptNgfwUserAuthName_Object((1,3,6,1,4,1,10734,3,9,3,1,73),_TptNgfwUserAuthName_Type())
tptNgfwUserAuthName.setMaxAccess(_C)
if mibBuilder.loadTexts:tptNgfwUserAuthName.setStatus(_B)
class _TptNgfwUserAuthFailNotifyReason_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,80))
_TptNgfwUserAuthFailNotifyReason_Type.__name__=_F
_TptNgfwUserAuthFailNotifyReason_Object=MibScalar
tptNgfwUserAuthFailNotifyReason=_TptNgfwUserAuthFailNotifyReason_Object((1,3,6,1,4,1,10734,3,9,3,1,74),_TptNgfwUserAuthFailNotifyReason_Type())
tptNgfwUserAuthFailNotifyReason.setMaxAccess(_C)
if mibBuilder.loadTexts:tptNgfwUserAuthFailNotifyReason.setStatus(_B)
_TptNgfwUserAuthSrcIpAddrType_Type=InetAddressType
_TptNgfwUserAuthSrcIpAddrType_Object=MibScalar
tptNgfwUserAuthSrcIpAddrType=_TptNgfwUserAuthSrcIpAddrType_Object((1,3,6,1,4,1,10734,3,9,3,1,75),_TptNgfwUserAuthSrcIpAddrType_Type())
tptNgfwUserAuthSrcIpAddrType.setMaxAccess(_C)
if mibBuilder.loadTexts:tptNgfwUserAuthSrcIpAddrType.setStatus(_B)
_TptNgfwUserAuthSrcIpAddr_Type=InetAddress
_TptNgfwUserAuthSrcIpAddr_Object=MibScalar
tptNgfwUserAuthSrcIpAddr=_TptNgfwUserAuthSrcIpAddr_Object((1,3,6,1,4,1,10734,3,9,3,1,76),_TptNgfwUserAuthSrcIpAddr_Type())
tptNgfwUserAuthSrcIpAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:tptNgfwUserAuthSrcIpAddr.setStatus(_B)
class _TptNgfwUserAuthNotifySource_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,40))
_TptNgfwUserAuthNotifySource_Type.__name__=_F
_TptNgfwUserAuthNotifySource_Object=MibScalar
tptNgfwUserAuthNotifySource=_TptNgfwUserAuthNotifySource_Object((1,3,6,1,4,1,10734,3,9,3,1,77),_TptNgfwUserAuthNotifySource_Type())
tptNgfwUserAuthNotifySource.setMaxAccess(_C)
if mibBuilder.loadTexts:tptNgfwUserAuthNotifySource.setStatus(_B)
_TptNgfwUserAuthLockedTime_Type=DateAndTime
_TptNgfwUserAuthLockedTime_Object=MibScalar
tptNgfwUserAuthLockedTime=_TptNgfwUserAuthLockedTime_Object((1,3,6,1,4,1,10734,3,9,3,1,78),_TptNgfwUserAuthLockedTime_Type())
tptNgfwUserAuthLockedTime.setMaxAccess(_C)
if mibBuilder.loadTexts:tptNgfwUserAuthLockedTime.setStatus(_B)
tptNgfwUserGroup=ObjectGroup((1,3,6,1,4,1,10734,3,9,1,1,11))
tptNgfwUserGroup.setObjects(*((_A,_K),(_A,_N),(_A,_D),(_A,_E),(_A,_L),(_A,_M)))
if mibBuilder.loadTexts:tptNgfwUserGroup.setStatus(_B)
tptNgfwUserAuthFailNotify=NotificationType((1,3,6,1,4,1,10734,3,9,3,0,18))
tptNgfwUserAuthFailNotify.setObjects(*((_I,_J),(_A,_K),(_A,_N),(_A,_D),(_A,_E),(_A,_L),(_G,_H)))
if mibBuilder.loadTexts:tptNgfwUserAuthFailNotify.setStatus(_B)
tptNgfwUserAuthLockedAccountNotify=NotificationType((1,3,6,1,4,1,10734,3,9,3,0,19))
tptNgfwUserAuthLockedAccountNotify.setObjects(*((_I,_J),(_A,_K),(_A,_D),(_A,_E),(_A,_M),(_A,_L),(_G,_H)))
if mibBuilder.loadTexts:tptNgfwUserAuthLockedAccountNotify.setStatus(_B)
tptNgfwUserAuthLockedIpNotify=NotificationType((1,3,6,1,4,1,10734,3,9,3,0,20))
tptNgfwUserAuthLockedIpNotify.setObjects(*((_I,_J),(_A,_D),(_A,_E),(_A,_M),(_G,_H)))
if mibBuilder.loadTexts:tptNgfwUserAuthLockedIpNotify.setStatus(_B)
tptNgfwUserNotificationGroup=NotificationGroup((1,3,6,1,4,1,10734,3,9,1,1,12))
tptNgfwUserNotificationGroup.setObjects(*((_A,_O),(_A,_P),(_A,_Q)))
if mibBuilder.loadTexts:tptNgfwUserNotificationGroup.setStatus(_B)
tptNgfwUserCompl=ModuleCompliance((1,3,6,1,4,1,10734,3,9,1,2,5))
tptNgfwUserCompl.setObjects(*((_A,_R),(_A,_S)))
if mibBuilder.loadTexts:tptNgfwUserCompl.setStatus(_B)
mibBuilder.exportSymbols(_A,**{_R:tptNgfwUserGroup,_S:tptNgfwUserNotificationGroup,'tptNgfwUserCompl':tptNgfwUserCompl,'tptNgfwPolicy':tptNgfwPolicy,_O:tptNgfwUserAuthFailNotify,_P:tptNgfwUserAuthLockedAccountNotify,_Q:tptNgfwUserAuthLockedIpNotify,_K:tptNgfwUserAuthName,_N:tptNgfwUserAuthFailNotifyReason,_D:tptNgfwUserAuthSrcIpAddrType,_E:tptNgfwUserAuthSrcIpAddr,_L:tptNgfwUserAuthNotifySource,_M:tptNgfwUserAuthLockedTime})