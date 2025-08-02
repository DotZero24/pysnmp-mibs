_b='alvarionClientTrackingNotificationGroup'
_a='alvarionClientTrackingInfoMIBGroup'
_Z='alvarionClientTrackingConfigMIBGroup'
_Y='clientTrackingDeAuthenticationFailure'
_X='clientTrackingSuccessfulDeAuthentication'
_W='clientTrackingDisAssociationFailure'
_V='clientTrackingSuccessfulDisAssociation'
_U='clientTrackingAuthenticationFailure'
_T='clientTrackingSuccessfulAuthentication'
_S='clientTrackingReAssociationFailure'
_R='clientTrackingSuccessfulReAssociation'
_Q='clientTrackingAssociationFailure'
_P='clientTrackingSuccessfulAssociation'
_O='clientTrackingDeAuthenticationFailureNotificationEnabled'
_N='clientTrackingSuccessfulDeAuthenticationNotificationEnabled'
_M='clientTrackingDisAssociationFailureNotificationEnabled'
_L='clientTrackingSuccessfulDisAssociationNotificationEnabled'
_K='clientTrackingAuthenticationFailureNotificationEnabled'
_J='clientTrackingSuccessfulAuthenticationNotificationEnabled'
_I='clientTrackingReAssociationFailureNotificationEnabled'
_H='clientTrackingSuccessfulReAssociationNotificationEnabled'
_G='clientTrackingAssociationFailureNotificationEnabled'
_F='clientTrackingSuccessfulAssociationNotificationEnabled'
_E='read-write'
_D='AlvarionNotificationEnable'
_C='clientTrackingEventInformation'
_B='current'
_A='ALVARION-CLIENT-TRACKING-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
alvarionMgmtV2,=mibBuilder.importSymbols('ALVARION-SMI','alvarionMgmtV2')
AlvarionNotificationEnable,=mibBuilder.importSymbols('ALVARION-TC',_D)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
alvarionClientTrackingMIB=ModuleIdentity((1,3,6,1,4,1,12394,1,10,5,19))
_AlvarionClientTrackingMIBObjects_ObjectIdentity=ObjectIdentity
alvarionClientTrackingMIBObjects=_AlvarionClientTrackingMIBObjects_ObjectIdentity((1,3,6,1,4,1,12394,1,10,5,19,1))
_ClientTrackingConfig_ObjectIdentity=ObjectIdentity
clientTrackingConfig=_ClientTrackingConfig_ObjectIdentity((1,3,6,1,4,1,12394,1,10,5,19,1,1))
class _ClientTrackingSuccessfulAssociationNotificationEnabled_Type(AlvarionNotificationEnable):defaultValue=2
_ClientTrackingSuccessfulAssociationNotificationEnabled_Type.__name__=_D
_ClientTrackingSuccessfulAssociationNotificationEnabled_Object=MibScalar
clientTrackingSuccessfulAssociationNotificationEnabled=_ClientTrackingSuccessfulAssociationNotificationEnabled_Object((1,3,6,1,4,1,12394,1,10,5,19,1,1,1),_ClientTrackingSuccessfulAssociationNotificationEnabled_Type())
clientTrackingSuccessfulAssociationNotificationEnabled.setMaxAccess(_E)
if mibBuilder.loadTexts:clientTrackingSuccessfulAssociationNotificationEnabled.setStatus(_B)
class _ClientTrackingAssociationFailureNotificationEnabled_Type(AlvarionNotificationEnable):defaultValue=2
_ClientTrackingAssociationFailureNotificationEnabled_Type.__name__=_D
_ClientTrackingAssociationFailureNotificationEnabled_Object=MibScalar
clientTrackingAssociationFailureNotificationEnabled=_ClientTrackingAssociationFailureNotificationEnabled_Object((1,3,6,1,4,1,12394,1,10,5,19,1,1,2),_ClientTrackingAssociationFailureNotificationEnabled_Type())
clientTrackingAssociationFailureNotificationEnabled.setMaxAccess(_E)
if mibBuilder.loadTexts:clientTrackingAssociationFailureNotificationEnabled.setStatus(_B)
class _ClientTrackingSuccessfulReAssociationNotificationEnabled_Type(AlvarionNotificationEnable):defaultValue=2
_ClientTrackingSuccessfulReAssociationNotificationEnabled_Type.__name__=_D
_ClientTrackingSuccessfulReAssociationNotificationEnabled_Object=MibScalar
clientTrackingSuccessfulReAssociationNotificationEnabled=_ClientTrackingSuccessfulReAssociationNotificationEnabled_Object((1,3,6,1,4,1,12394,1,10,5,19,1,1,3),_ClientTrackingSuccessfulReAssociationNotificationEnabled_Type())
clientTrackingSuccessfulReAssociationNotificationEnabled.setMaxAccess(_E)
if mibBuilder.loadTexts:clientTrackingSuccessfulReAssociationNotificationEnabled.setStatus(_B)
class _ClientTrackingReAssociationFailureNotificationEnabled_Type(AlvarionNotificationEnable):defaultValue=2
_ClientTrackingReAssociationFailureNotificationEnabled_Type.__name__=_D
_ClientTrackingReAssociationFailureNotificationEnabled_Object=MibScalar
clientTrackingReAssociationFailureNotificationEnabled=_ClientTrackingReAssociationFailureNotificationEnabled_Object((1,3,6,1,4,1,12394,1,10,5,19,1,1,4),_ClientTrackingReAssociationFailureNotificationEnabled_Type())
clientTrackingReAssociationFailureNotificationEnabled.setMaxAccess(_E)
if mibBuilder.loadTexts:clientTrackingReAssociationFailureNotificationEnabled.setStatus(_B)
class _ClientTrackingSuccessfulAuthenticationNotificationEnabled_Type(AlvarionNotificationEnable):defaultValue=2
_ClientTrackingSuccessfulAuthenticationNotificationEnabled_Type.__name__=_D
_ClientTrackingSuccessfulAuthenticationNotificationEnabled_Object=MibScalar
clientTrackingSuccessfulAuthenticationNotificationEnabled=_ClientTrackingSuccessfulAuthenticationNotificationEnabled_Object((1,3,6,1,4,1,12394,1,10,5,19,1,1,5),_ClientTrackingSuccessfulAuthenticationNotificationEnabled_Type())
clientTrackingSuccessfulAuthenticationNotificationEnabled.setMaxAccess(_E)
if mibBuilder.loadTexts:clientTrackingSuccessfulAuthenticationNotificationEnabled.setStatus(_B)
class _ClientTrackingAuthenticationFailureNotificationEnabled_Type(AlvarionNotificationEnable):defaultValue=2
_ClientTrackingAuthenticationFailureNotificationEnabled_Type.__name__=_D
_ClientTrackingAuthenticationFailureNotificationEnabled_Object=MibScalar
clientTrackingAuthenticationFailureNotificationEnabled=_ClientTrackingAuthenticationFailureNotificationEnabled_Object((1,3,6,1,4,1,12394,1,10,5,19,1,1,6),_ClientTrackingAuthenticationFailureNotificationEnabled_Type())
clientTrackingAuthenticationFailureNotificationEnabled.setMaxAccess(_E)
if mibBuilder.loadTexts:clientTrackingAuthenticationFailureNotificationEnabled.setStatus(_B)
class _ClientTrackingSuccessfulDisAssociationNotificationEnabled_Type(AlvarionNotificationEnable):defaultValue=2
_ClientTrackingSuccessfulDisAssociationNotificationEnabled_Type.__name__=_D
_ClientTrackingSuccessfulDisAssociationNotificationEnabled_Object=MibScalar
clientTrackingSuccessfulDisAssociationNotificationEnabled=_ClientTrackingSuccessfulDisAssociationNotificationEnabled_Object((1,3,6,1,4,1,12394,1,10,5,19,1,1,7),_ClientTrackingSuccessfulDisAssociationNotificationEnabled_Type())
clientTrackingSuccessfulDisAssociationNotificationEnabled.setMaxAccess(_E)
if mibBuilder.loadTexts:clientTrackingSuccessfulDisAssociationNotificationEnabled.setStatus(_B)
class _ClientTrackingDisAssociationFailureNotificationEnabled_Type(AlvarionNotificationEnable):defaultValue=2
_ClientTrackingDisAssociationFailureNotificationEnabled_Type.__name__=_D
_ClientTrackingDisAssociationFailureNotificationEnabled_Object=MibScalar
clientTrackingDisAssociationFailureNotificationEnabled=_ClientTrackingDisAssociationFailureNotificationEnabled_Object((1,3,6,1,4,1,12394,1,10,5,19,1,1,8),_ClientTrackingDisAssociationFailureNotificationEnabled_Type())
clientTrackingDisAssociationFailureNotificationEnabled.setMaxAccess(_E)
if mibBuilder.loadTexts:clientTrackingDisAssociationFailureNotificationEnabled.setStatus(_B)
class _ClientTrackingSuccessfulDeAuthenticationNotificationEnabled_Type(AlvarionNotificationEnable):defaultValue=2
_ClientTrackingSuccessfulDeAuthenticationNotificationEnabled_Type.__name__=_D
_ClientTrackingSuccessfulDeAuthenticationNotificationEnabled_Object=MibScalar
clientTrackingSuccessfulDeAuthenticationNotificationEnabled=_ClientTrackingSuccessfulDeAuthenticationNotificationEnabled_Object((1,3,6,1,4,1,12394,1,10,5,19,1,1,9),_ClientTrackingSuccessfulDeAuthenticationNotificationEnabled_Type())
clientTrackingSuccessfulDeAuthenticationNotificationEnabled.setMaxAccess(_E)
if mibBuilder.loadTexts:clientTrackingSuccessfulDeAuthenticationNotificationEnabled.setStatus(_B)
class _ClientTrackingDeAuthenticationFailureNotificationEnabled_Type(AlvarionNotificationEnable):defaultValue=2
_ClientTrackingDeAuthenticationFailureNotificationEnabled_Type.__name__=_D
_ClientTrackingDeAuthenticationFailureNotificationEnabled_Object=MibScalar
clientTrackingDeAuthenticationFailureNotificationEnabled=_ClientTrackingDeAuthenticationFailureNotificationEnabled_Object((1,3,6,1,4,1,12394,1,10,5,19,1,1,10),_ClientTrackingDeAuthenticationFailureNotificationEnabled_Type())
clientTrackingDeAuthenticationFailureNotificationEnabled.setMaxAccess(_E)
if mibBuilder.loadTexts:clientTrackingDeAuthenticationFailureNotificationEnabled.setStatus(_B)
_ClientTrackingInfo_ObjectIdentity=ObjectIdentity
clientTrackingInfo=_ClientTrackingInfo_ObjectIdentity((1,3,6,1,4,1,12394,1,10,5,19,1,2))
_ClientTrackingEventInformation_Type=DisplayString
_ClientTrackingEventInformation_Object=MibScalar
clientTrackingEventInformation=_ClientTrackingEventInformation_Object((1,3,6,1,4,1,12394,1,10,5,19,1,2,1),_ClientTrackingEventInformation_Type())
clientTrackingEventInformation.setMaxAccess('accessible-for-notify')
if mibBuilder.loadTexts:clientTrackingEventInformation.setStatus(_B)
_AlvarionClientTrackingMIBNotificationPrefix_ObjectIdentity=ObjectIdentity
alvarionClientTrackingMIBNotificationPrefix=_AlvarionClientTrackingMIBNotificationPrefix_ObjectIdentity((1,3,6,1,4,1,12394,1,10,5,19,2))
_AlvarionClientTrackingMIBNotifications_ObjectIdentity=ObjectIdentity
alvarionClientTrackingMIBNotifications=_AlvarionClientTrackingMIBNotifications_ObjectIdentity((1,3,6,1,4,1,12394,1,10,5,19,2,0))
_AlvarionClientTrackingMIBConformance_ObjectIdentity=ObjectIdentity
alvarionClientTrackingMIBConformance=_AlvarionClientTrackingMIBConformance_ObjectIdentity((1,3,6,1,4,1,12394,1,10,5,19,3))
_AlvarionClientTrackingMIBCompliances_ObjectIdentity=ObjectIdentity
alvarionClientTrackingMIBCompliances=_AlvarionClientTrackingMIBCompliances_ObjectIdentity((1,3,6,1,4,1,12394,1,10,5,19,3,1))
_AlvarionClientTrackingMIBGroups_ObjectIdentity=ObjectIdentity
alvarionClientTrackingMIBGroups=_AlvarionClientTrackingMIBGroups_ObjectIdentity((1,3,6,1,4,1,12394,1,10,5,19,3,2))
alvarionClientTrackingConfigMIBGroup=ObjectGroup((1,3,6,1,4,1,12394,1,10,5,19,3,2,1))
alvarionClientTrackingConfigMIBGroup.setObjects(*((_A,_F),(_A,_G),(_A,_H),(_A,_I),(_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_N),(_A,_O)))
if mibBuilder.loadTexts:alvarionClientTrackingConfigMIBGroup.setStatus(_B)
alvarionClientTrackingInfoMIBGroup=ObjectGroup((1,3,6,1,4,1,12394,1,10,5,19,3,2,2))
alvarionClientTrackingInfoMIBGroup.setObjects((_A,_C))
if mibBuilder.loadTexts:alvarionClientTrackingInfoMIBGroup.setStatus(_B)
clientTrackingSuccessfulAssociation=NotificationType((1,3,6,1,4,1,12394,1,10,5,19,2,0,1))
clientTrackingSuccessfulAssociation.setObjects((_A,_C))
if mibBuilder.loadTexts:clientTrackingSuccessfulAssociation.setStatus(_B)
clientTrackingAssociationFailure=NotificationType((1,3,6,1,4,1,12394,1,10,5,19,2,0,2))
clientTrackingAssociationFailure.setObjects((_A,_C))
if mibBuilder.loadTexts:clientTrackingAssociationFailure.setStatus(_B)
clientTrackingSuccessfulReAssociation=NotificationType((1,3,6,1,4,1,12394,1,10,5,19,2,0,3))
clientTrackingSuccessfulReAssociation.setObjects((_A,_C))
if mibBuilder.loadTexts:clientTrackingSuccessfulReAssociation.setStatus(_B)
clientTrackingReAssociationFailure=NotificationType((1,3,6,1,4,1,12394,1,10,5,19,2,0,4))
clientTrackingReAssociationFailure.setObjects((_A,_C))
if mibBuilder.loadTexts:clientTrackingReAssociationFailure.setStatus(_B)
clientTrackingSuccessfulAuthentication=NotificationType((1,3,6,1,4,1,12394,1,10,5,19,2,0,5))
clientTrackingSuccessfulAuthentication.setObjects((_A,_C))
if mibBuilder.loadTexts:clientTrackingSuccessfulAuthentication.setStatus(_B)
clientTrackingAuthenticationFailure=NotificationType((1,3,6,1,4,1,12394,1,10,5,19,2,0,6))
clientTrackingAuthenticationFailure.setObjects((_A,_C))
if mibBuilder.loadTexts:clientTrackingAuthenticationFailure.setStatus(_B)
clientTrackingSuccessfulDisAssociation=NotificationType((1,3,6,1,4,1,12394,1,10,5,19,2,0,7))
clientTrackingSuccessfulDisAssociation.setObjects((_A,_C))
if mibBuilder.loadTexts:clientTrackingSuccessfulDisAssociation.setStatus(_B)
clientTrackingDisAssociationFailure=NotificationType((1,3,6,1,4,1,12394,1,10,5,19,2,0,8))
clientTrackingDisAssociationFailure.setObjects((_A,_C))
if mibBuilder.loadTexts:clientTrackingDisAssociationFailure.setStatus(_B)
clientTrackingSuccessfulDeAuthentication=NotificationType((1,3,6,1,4,1,12394,1,10,5,19,2,0,9))
clientTrackingSuccessfulDeAuthentication.setObjects((_A,_C))
if mibBuilder.loadTexts:clientTrackingSuccessfulDeAuthentication.setStatus(_B)
clientTrackingDeAuthenticationFailure=NotificationType((1,3,6,1,4,1,12394,1,10,5,19,2,0,10))
clientTrackingDeAuthenticationFailure.setObjects((_A,_C))
if mibBuilder.loadTexts:clientTrackingDeAuthenticationFailure.setStatus(_B)
alvarionClientTrackingNotificationGroup=NotificationGroup((1,3,6,1,4,1,12394,1,10,5,19,3,2,3))
alvarionClientTrackingNotificationGroup.setObjects(*((_A,_P),(_A,_Q),(_A,_R),(_A,_S),(_A,_T),(_A,_U),(_A,_V),(_A,_W),(_A,_X),(_A,_Y)))
if mibBuilder.loadTexts:alvarionClientTrackingNotificationGroup.setStatus(_B)
alvarionClientTrackingMIBCompliance=ModuleCompliance((1,3,6,1,4,1,12394,1,10,5,19,3,1,1))
alvarionClientTrackingMIBCompliance.setObjects(*((_A,_Z),(_A,_a),(_A,_b)))
if mibBuilder.loadTexts:alvarionClientTrackingMIBCompliance.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'alvarionClientTrackingMIB':alvarionClientTrackingMIB,'alvarionClientTrackingMIBObjects':alvarionClientTrackingMIBObjects,'clientTrackingConfig':clientTrackingConfig,_F:clientTrackingSuccessfulAssociationNotificationEnabled,_G:clientTrackingAssociationFailureNotificationEnabled,_H:clientTrackingSuccessfulReAssociationNotificationEnabled,_I:clientTrackingReAssociationFailureNotificationEnabled,_J:clientTrackingSuccessfulAuthenticationNotificationEnabled,_K:clientTrackingAuthenticationFailureNotificationEnabled,_L:clientTrackingSuccessfulDisAssociationNotificationEnabled,_M:clientTrackingDisAssociationFailureNotificationEnabled,_N:clientTrackingSuccessfulDeAuthenticationNotificationEnabled,_O:clientTrackingDeAuthenticationFailureNotificationEnabled,'clientTrackingInfo':clientTrackingInfo,_C:clientTrackingEventInformation,'alvarionClientTrackingMIBNotificationPrefix':alvarionClientTrackingMIBNotificationPrefix,'alvarionClientTrackingMIBNotifications':alvarionClientTrackingMIBNotifications,_P:clientTrackingSuccessfulAssociation,_Q:clientTrackingAssociationFailure,_R:clientTrackingSuccessfulReAssociation,_S:clientTrackingReAssociationFailure,_T:clientTrackingSuccessfulAuthentication,_U:clientTrackingAuthenticationFailure,_V:clientTrackingSuccessfulDisAssociation,_W:clientTrackingDisAssociationFailure,_X:clientTrackingSuccessfulDeAuthentication,_Y:clientTrackingDeAuthenticationFailure,'alvarionClientTrackingMIBConformance':alvarionClientTrackingMIBConformance,'alvarionClientTrackingMIBCompliances':alvarionClientTrackingMIBCompliances,'alvarionClientTrackingMIBCompliance':alvarionClientTrackingMIBCompliance,'alvarionClientTrackingMIBGroups':alvarionClientTrackingMIBGroups,_Z:alvarionClientTrackingConfigMIBGroup,_a:alvarionClientTrackingInfoMIBGroup,_b:alvarionClientTrackingNotificationGroup})