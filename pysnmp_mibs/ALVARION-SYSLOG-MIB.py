_S='alvarionSyslogNotificationGroup'
_R='alvarionSyslogMIBGroup'
_Q='syslogRegExMatchNotification'
_P='syslogSeverityNotification'
_O='syslogMessageRegEx'
_N='syslogTrapSeverityLevel'
_M='syslogSeverityLevel'
_L='syslogRegExMatchNotificationEnabled'
_K='syslogSeverityNotificationEnabled'
_J='SyslogSeverity'
_I='AlvarionNotificationEnable'
_H='syslogMsgText'
_G='syslogMsgSeverity'
_F='syslogMsgFacility'
_E='syslogMsgNumber'
_D='accessible-for-notify'
_C='read-write'
_B='current'
_A='ALVARION-SYSLOG-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
alvarionMgmtV2,=mibBuilder.importSymbols('ALVARION-SMI','alvarionMgmtV2')
AlvarionNotificationEnable,=mibBuilder.importSymbols('ALVARION-TC',_I)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
alvarionSyslogMIB=ModuleIdentity((1,3,6,1,4,1,12394,1,10,5,3))
class SyslogSeverity(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8)));namedValues=NamedValues(*(('emergency',1),('alert',2),('critical',3),('error',4),('warning',5),('notice',6),('info',7),('debug',8)))
_AlvarionSyslogMIBObjects_ObjectIdentity=ObjectIdentity
alvarionSyslogMIBObjects=_AlvarionSyslogMIBObjects_ObjectIdentity((1,3,6,1,4,1,12394,1,10,5,3,1))
_SyslogConfig_ObjectIdentity=ObjectIdentity
syslogConfig=_SyslogConfig_ObjectIdentity((1,3,6,1,4,1,12394,1,10,5,3,1,1))
class _SyslogSeverityNotificationEnabled_Type(AlvarionNotificationEnable):defaultValue=1
_SyslogSeverityNotificationEnabled_Type.__name__=_I
_SyslogSeverityNotificationEnabled_Object=MibScalar
syslogSeverityNotificationEnabled=_SyslogSeverityNotificationEnabled_Object((1,3,6,1,4,1,12394,1,10,5,3,1,1,1),_SyslogSeverityNotificationEnabled_Type())
syslogSeverityNotificationEnabled.setMaxAccess(_C)
if mibBuilder.loadTexts:syslogSeverityNotificationEnabled.setStatus(_B)
class _SyslogRegExMatchNotificationEnabled_Type(AlvarionNotificationEnable):defaultValue=2
_SyslogRegExMatchNotificationEnabled_Type.__name__=_I
_SyslogRegExMatchNotificationEnabled_Object=MibScalar
syslogRegExMatchNotificationEnabled=_SyslogRegExMatchNotificationEnabled_Object((1,3,6,1,4,1,12394,1,10,5,3,1,1,2),_SyslogRegExMatchNotificationEnabled_Type())
syslogRegExMatchNotificationEnabled.setMaxAccess(_C)
if mibBuilder.loadTexts:syslogRegExMatchNotificationEnabled.setStatus(_B)
class _SyslogSeverityLevel_Type(SyslogSeverity):defaultValue=5
_SyslogSeverityLevel_Type.__name__=_J
_SyslogSeverityLevel_Object=MibScalar
syslogSeverityLevel=_SyslogSeverityLevel_Object((1,3,6,1,4,1,12394,1,10,5,3,1,1,3),_SyslogSeverityLevel_Type())
syslogSeverityLevel.setMaxAccess(_C)
if mibBuilder.loadTexts:syslogSeverityLevel.setStatus(_B)
class _SyslogTrapSeverityLevel_Type(SyslogSeverity):defaultValue=5
_SyslogTrapSeverityLevel_Type.__name__=_J
_SyslogTrapSeverityLevel_Object=MibScalar
syslogTrapSeverityLevel=_SyslogTrapSeverityLevel_Object((1,3,6,1,4,1,12394,1,10,5,3,1,1,4),_SyslogTrapSeverityLevel_Type())
syslogTrapSeverityLevel.setMaxAccess(_C)
if mibBuilder.loadTexts:syslogTrapSeverityLevel.setStatus(_B)
_SyslogMessageRegEx_Type=DisplayString
_SyslogMessageRegEx_Object=MibScalar
syslogMessageRegEx=_SyslogMessageRegEx_Object((1,3,6,1,4,1,12394,1,10,5,3,1,1,5),_SyslogMessageRegEx_Type())
syslogMessageRegEx.setMaxAccess(_C)
if mibBuilder.loadTexts:syslogMessageRegEx.setStatus(_B)
_SyslogMessage_ObjectIdentity=ObjectIdentity
syslogMessage=_SyslogMessage_ObjectIdentity((1,3,6,1,4,1,12394,1,10,5,3,1,2))
_SyslogMsgNumber_Type=Unsigned32
_SyslogMsgNumber_Object=MibScalar
syslogMsgNumber=_SyslogMsgNumber_Object((1,3,6,1,4,1,12394,1,10,5,3,1,2,1),_SyslogMsgNumber_Type())
syslogMsgNumber.setMaxAccess(_D)
if mibBuilder.loadTexts:syslogMsgNumber.setStatus(_B)
_SyslogMsgFacility_Type=DisplayString
_SyslogMsgFacility_Object=MibScalar
syslogMsgFacility=_SyslogMsgFacility_Object((1,3,6,1,4,1,12394,1,10,5,3,1,2,2),_SyslogMsgFacility_Type())
syslogMsgFacility.setMaxAccess(_D)
if mibBuilder.loadTexts:syslogMsgFacility.setStatus(_B)
_SyslogMsgSeverity_Type=SyslogSeverity
_SyslogMsgSeverity_Object=MibScalar
syslogMsgSeverity=_SyslogMsgSeverity_Object((1,3,6,1,4,1,12394,1,10,5,3,1,2,3),_SyslogMsgSeverity_Type())
syslogMsgSeverity.setMaxAccess(_D)
if mibBuilder.loadTexts:syslogMsgSeverity.setStatus(_B)
_SyslogMsgText_Type=DisplayString
_SyslogMsgText_Object=MibScalar
syslogMsgText=_SyslogMsgText_Object((1,3,6,1,4,1,12394,1,10,5,3,1,2,4),_SyslogMsgText_Type())
syslogMsgText.setMaxAccess(_D)
if mibBuilder.loadTexts:syslogMsgText.setStatus(_B)
_AlvarionSyslogMIBNotificationPrefix_ObjectIdentity=ObjectIdentity
alvarionSyslogMIBNotificationPrefix=_AlvarionSyslogMIBNotificationPrefix_ObjectIdentity((1,3,6,1,4,1,12394,1,10,5,3,2))
_AlvarionSyslogMIBNotifications_ObjectIdentity=ObjectIdentity
alvarionSyslogMIBNotifications=_AlvarionSyslogMIBNotifications_ObjectIdentity((1,3,6,1,4,1,12394,1,10,5,3,2,0))
_AlvarionSyslogMIBConformance_ObjectIdentity=ObjectIdentity
alvarionSyslogMIBConformance=_AlvarionSyslogMIBConformance_ObjectIdentity((1,3,6,1,4,1,12394,1,10,5,3,3))
_AlvarionSyslogMIBCompliances_ObjectIdentity=ObjectIdentity
alvarionSyslogMIBCompliances=_AlvarionSyslogMIBCompliances_ObjectIdentity((1,3,6,1,4,1,12394,1,10,5,3,3,1))
_AlvarionSyslogMIBGroups_ObjectIdentity=ObjectIdentity
alvarionSyslogMIBGroups=_AlvarionSyslogMIBGroups_ObjectIdentity((1,3,6,1,4,1,12394,1,10,5,3,3,2))
alvarionSyslogMIBGroup=ObjectGroup((1,3,6,1,4,1,12394,1,10,5,3,3,2,1))
alvarionSyslogMIBGroup.setObjects(*((_A,_K),(_A,_L),(_A,_M),(_A,_N),(_A,_O),(_A,_E),(_A,_F),(_A,_G),(_A,_H)))
if mibBuilder.loadTexts:alvarionSyslogMIBGroup.setStatus(_B)
syslogSeverityNotification=NotificationType((1,3,6,1,4,1,12394,1,10,5,3,2,0,1))
syslogSeverityNotification.setObjects(*((_A,_E),(_A,_F),(_A,_G),(_A,_H)))
if mibBuilder.loadTexts:syslogSeverityNotification.setStatus(_B)
syslogRegExMatchNotification=NotificationType((1,3,6,1,4,1,12394,1,10,5,3,2,0,2))
syslogRegExMatchNotification.setObjects(*((_A,_E),(_A,_F),(_A,_G),(_A,_H)))
if mibBuilder.loadTexts:syslogRegExMatchNotification.setStatus(_B)
alvarionSyslogNotificationGroup=NotificationGroup((1,3,6,1,4,1,12394,1,10,5,3,3,2,2))
alvarionSyslogNotificationGroup.setObjects(*((_A,_P),(_A,_Q)))
if mibBuilder.loadTexts:alvarionSyslogNotificationGroup.setStatus(_B)
alvarionSyslogMIBCompliance=ModuleCompliance((1,3,6,1,4,1,12394,1,10,5,3,3,1,1))
alvarionSyslogMIBCompliance.setObjects(*((_A,_R),(_A,_S)))
if mibBuilder.loadTexts:alvarionSyslogMIBCompliance.setStatus(_B)
mibBuilder.exportSymbols(_A,**{_J:SyslogSeverity,'alvarionSyslogMIB':alvarionSyslogMIB,'alvarionSyslogMIBObjects':alvarionSyslogMIBObjects,'syslogConfig':syslogConfig,_K:syslogSeverityNotificationEnabled,_L:syslogRegExMatchNotificationEnabled,_M:syslogSeverityLevel,_N:syslogTrapSeverityLevel,_O:syslogMessageRegEx,'syslogMessage':syslogMessage,_E:syslogMsgNumber,_F:syslogMsgFacility,_G:syslogMsgSeverity,_H:syslogMsgText,'alvarionSyslogMIBNotificationPrefix':alvarionSyslogMIBNotificationPrefix,'alvarionSyslogMIBNotifications':alvarionSyslogMIBNotifications,_P:syslogSeverityNotification,_Q:syslogRegExMatchNotification,'alvarionSyslogMIBConformance':alvarionSyslogMIBConformance,'alvarionSyslogMIBCompliances':alvarionSyslogMIBCompliances,'alvarionSyslogMIBCompliance':alvarionSyslogMIBCompliance,'alvarionSyslogMIBGroups':alvarionSyslogMIBGroups,_R:alvarionSyslogMIBGroup,_S:alvarionSyslogNotificationGroup})