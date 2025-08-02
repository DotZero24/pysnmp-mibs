_J='cienaCesConfigMgmtConfigLastOrigin'
_I='cienaCesConfigMgmtConfigLastUser'
_H='cienaCesConfigMgmtConfigLastContext'
_G='cienaCesConfigMgmtConfigLastSaved'
_F='cienaCesConfigMgmtConfigLastChanged'
_E='cienaGlobalSeverity'
_D='CIENA-GLOBAL-MIB'
_C='read-only'
_B='CIENA-CES-CONFIG-MGMT-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
cienaGlobalSeverity,=mibBuilder.importSymbols(_D,_E)
cienaCesConfig,cienaCesNotifications=mibBuilder.importSymbols('CIENA-SMI','cienaCesConfig','cienaCesNotifications')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DateAndTime,DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime','DisplayString','PhysAddress','TextualConvention')
cienaCesConfigMgmtMIB=ModuleIdentity((1,3,6,1,4,1,1271,2,1,36))
if mibBuilder.loadTexts:cienaCesConfigMgmtMIB.setRevisions(('2017-06-07 00:00','2015-02-11 00:00'))
class CienaCesConfigMgmtContext(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('unknown',1),('cli',2),('snmp',3),('netconf',4)))
_CienaCesConfigMgmtMIBObjects_ObjectIdentity=ObjectIdentity
cienaCesConfigMgmtMIBObjects=_CienaCesConfigMgmtMIBObjects_ObjectIdentity((1,3,6,1,4,1,1271,2,1,36,1))
_CienaCesConfigMgmt_ObjectIdentity=ObjectIdentity
cienaCesConfigMgmt=_CienaCesConfigMgmt_ObjectIdentity((1,3,6,1,4,1,1271,2,1,36,1,1))
_CienaCesConfigMgmtConfigLastSaved_Type=DateAndTime
_CienaCesConfigMgmtConfigLastSaved_Object=MibScalar
cienaCesConfigMgmtConfigLastSaved=_CienaCesConfigMgmtConfigLastSaved_Object((1,3,6,1,4,1,1271,2,1,36,1,1,1),_CienaCesConfigMgmtConfigLastSaved_Type())
cienaCesConfigMgmtConfigLastSaved.setMaxAccess(_C)
if mibBuilder.loadTexts:cienaCesConfigMgmtConfigLastSaved.setStatus(_A)
_CienaCesConfigMgmtConfigLastChanged_Type=DateAndTime
_CienaCesConfigMgmtConfigLastChanged_Object=MibScalar
cienaCesConfigMgmtConfigLastChanged=_CienaCesConfigMgmtConfigLastChanged_Object((1,3,6,1,4,1,1271,2,1,36,1,1,2),_CienaCesConfigMgmtConfigLastChanged_Type())
cienaCesConfigMgmtConfigLastChanged.setMaxAccess(_C)
if mibBuilder.loadTexts:cienaCesConfigMgmtConfigLastChanged.setStatus(_A)
_CienaCesConfigMgmtConfigLastContext_Type=CienaCesConfigMgmtContext
_CienaCesConfigMgmtConfigLastContext_Object=MibScalar
cienaCesConfigMgmtConfigLastContext=_CienaCesConfigMgmtConfigLastContext_Object((1,3,6,1,4,1,1271,2,1,36,1,1,3),_CienaCesConfigMgmtConfigLastContext_Type())
cienaCesConfigMgmtConfigLastContext.setMaxAccess(_C)
if mibBuilder.loadTexts:cienaCesConfigMgmtConfigLastContext.setStatus(_A)
_CienaCesConfigMgmtConfigLastUser_Type=DisplayString
_CienaCesConfigMgmtConfigLastUser_Object=MibScalar
cienaCesConfigMgmtConfigLastUser=_CienaCesConfigMgmtConfigLastUser_Object((1,3,6,1,4,1,1271,2,1,36,1,1,4),_CienaCesConfigMgmtConfigLastUser_Type())
cienaCesConfigMgmtConfigLastUser.setMaxAccess(_C)
if mibBuilder.loadTexts:cienaCesConfigMgmtConfigLastUser.setStatus(_A)
_CienaCesConfigMgmtConfigLastOrigin_Type=DisplayString
_CienaCesConfigMgmtConfigLastOrigin_Object=MibScalar
cienaCesConfigMgmtConfigLastOrigin=_CienaCesConfigMgmtConfigLastOrigin_Object((1,3,6,1,4,1,1271,2,1,36,1,1,5),_CienaCesConfigMgmtConfigLastOrigin_Type())
cienaCesConfigMgmtConfigLastOrigin.setMaxAccess(_C)
if mibBuilder.loadTexts:cienaCesConfigMgmtConfigLastOrigin.setStatus(_A)
_CienaCesConfigMgmtMIBConformance_ObjectIdentity=ObjectIdentity
cienaCesConfigMgmtMIBConformance=_CienaCesConfigMgmtMIBConformance_ObjectIdentity((1,3,6,1,4,1,1271,2,1,36,2))
_CienaCesConfigMgmtMIBCompliances_ObjectIdentity=ObjectIdentity
cienaCesConfigMgmtMIBCompliances=_CienaCesConfigMgmtMIBCompliances_ObjectIdentity((1,3,6,1,4,1,1271,2,1,36,2,1))
_CienaCesConfigMgmtMIBGroups_ObjectIdentity=ObjectIdentity
cienaCesConfigMgmtMIBGroups=_CienaCesConfigMgmtMIBGroups_ObjectIdentity((1,3,6,1,4,1,1271,2,1,36,2,2))
_CienaCesConfigMgmtMIBNotificationsPrefix_ObjectIdentity=ObjectIdentity
cienaCesConfigMgmtMIBNotificationsPrefix=_CienaCesConfigMgmtMIBNotificationsPrefix_ObjectIdentity((1,3,6,1,4,1,1271,2,2,36))
_CienaCesConfigMgmtMIBNotifications_ObjectIdentity=ObjectIdentity
cienaCesConfigMgmtMIBNotifications=_CienaCesConfigMgmtMIBNotifications_ObjectIdentity((1,3,6,1,4,1,1271,2,2,36,0))
cienaCesConfigMgmtConfigSavedNotification=NotificationType((1,3,6,1,4,1,1271,2,2,36,0,1))
cienaCesConfigMgmtConfigSavedNotification.setObjects(*((_D,_E),(_B,_G),(_B,_F)))
if mibBuilder.loadTexts:cienaCesConfigMgmtConfigSavedNotification.setStatus(_A)
cienaCesConfigMgmtConfigChangeNotification=NotificationType((1,3,6,1,4,1,1271,2,2,36,0,2))
cienaCesConfigMgmtConfigChangeNotification.setObjects(*((_D,_E),(_B,_H),(_B,_I),(_B,_J),(_B,_F)))
if mibBuilder.loadTexts:cienaCesConfigMgmtConfigChangeNotification.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'CienaCesConfigMgmtContext':CienaCesConfigMgmtContext,'cienaCesConfigMgmtMIB':cienaCesConfigMgmtMIB,'cienaCesConfigMgmtMIBObjects':cienaCesConfigMgmtMIBObjects,'cienaCesConfigMgmt':cienaCesConfigMgmt,_G:cienaCesConfigMgmtConfigLastSaved,_F:cienaCesConfigMgmtConfigLastChanged,_H:cienaCesConfigMgmtConfigLastContext,_I:cienaCesConfigMgmtConfigLastUser,_J:cienaCesConfigMgmtConfigLastOrigin,'cienaCesConfigMgmtMIBConformance':cienaCesConfigMgmtMIBConformance,'cienaCesConfigMgmtMIBCompliances':cienaCesConfigMgmtMIBCompliances,'cienaCesConfigMgmtMIBGroups':cienaCesConfigMgmtMIBGroups,'cienaCesConfigMgmtMIBNotificationsPrefix':cienaCesConfigMgmtMIBNotificationsPrefix,'cienaCesConfigMgmtMIBNotifications':cienaCesConfigMgmtMIBNotifications,'cienaCesConfigMgmtConfigSavedNotification':cienaCesConfigMgmtConfigSavedNotification,'cienaCesConfigMgmtConfigChangeNotification':cienaCesConfigMgmtConfigChangeNotification})