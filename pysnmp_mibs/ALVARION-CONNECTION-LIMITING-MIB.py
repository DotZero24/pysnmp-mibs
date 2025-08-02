_G='alvarionConnectionLimitingInfoMIBGroup'
_F='alvarionConnectionLimitingConfigMIBGroup'
_E='connectionLimitingMaximumSystemConnections'
_D='connectionLimitingMaximumUserConnections'
_C='Integer32'
_B='ALVARION-CONNECTION-LIMITING-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
alvarionMgmtV2,=mibBuilder.importSymbols('ALVARION-SMI','alvarionMgmtV2')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
alvarionConnectionLimitingMIB=ModuleIdentity((1,3,6,1,4,1,12394,1,10,5,18))
_AlvarionConnectionLimitingMIBObjects_ObjectIdentity=ObjectIdentity
alvarionConnectionLimitingMIBObjects=_AlvarionConnectionLimitingMIBObjects_ObjectIdentity((1,3,6,1,4,1,12394,1,10,5,18,1))
_ConnectionLimitingConfig_ObjectIdentity=ObjectIdentity
connectionLimitingConfig=_ConnectionLimitingConfig_ObjectIdentity((1,3,6,1,4,1,12394,1,10,5,18,1,1))
class _ConnectionLimitingMaximumUserConnections_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(20,2000))
_ConnectionLimitingMaximumUserConnections_Type.__name__=_C
_ConnectionLimitingMaximumUserConnections_Object=MibScalar
connectionLimitingMaximumUserConnections=_ConnectionLimitingMaximumUserConnections_Object((1,3,6,1,4,1,12394,1,10,5,18,1,1,1),_ConnectionLimitingMaximumUserConnections_Type())
connectionLimitingMaximumUserConnections.setMaxAccess('read-write')
if mibBuilder.loadTexts:connectionLimitingMaximumUserConnections.setStatus(_A)
_ConnectionLimitingInfo_ObjectIdentity=ObjectIdentity
connectionLimitingInfo=_ConnectionLimitingInfo_ObjectIdentity((1,3,6,1,4,1,12394,1,10,5,18,1,2))
_ConnectionLimitingMaximumSystemConnections_Type=Integer32
_ConnectionLimitingMaximumSystemConnections_Object=MibScalar
connectionLimitingMaximumSystemConnections=_ConnectionLimitingMaximumSystemConnections_Object((1,3,6,1,4,1,12394,1,10,5,18,1,2,1),_ConnectionLimitingMaximumSystemConnections_Type())
connectionLimitingMaximumSystemConnections.setMaxAccess('read-only')
if mibBuilder.loadTexts:connectionLimitingMaximumSystemConnections.setStatus(_A)
_AlvarionConnectionLimitingMIBNotificationPrefix_ObjectIdentity=ObjectIdentity
alvarionConnectionLimitingMIBNotificationPrefix=_AlvarionConnectionLimitingMIBNotificationPrefix_ObjectIdentity((1,3,6,1,4,1,12394,1,10,5,18,2))
_AlvarionConnectionLimitingMIBNotifications_ObjectIdentity=ObjectIdentity
alvarionConnectionLimitingMIBNotifications=_AlvarionConnectionLimitingMIBNotifications_ObjectIdentity((1,3,6,1,4,1,12394,1,10,5,18,2,0))
_AlvarionConnectionLimitingMIBConformance_ObjectIdentity=ObjectIdentity
alvarionConnectionLimitingMIBConformance=_AlvarionConnectionLimitingMIBConformance_ObjectIdentity((1,3,6,1,4,1,12394,1,10,5,18,3))
_AlvarionConnectionLimitingMIBCompliances_ObjectIdentity=ObjectIdentity
alvarionConnectionLimitingMIBCompliances=_AlvarionConnectionLimitingMIBCompliances_ObjectIdentity((1,3,6,1,4,1,12394,1,10,5,18,3,1))
_AlvarionConnectionLimitingMIBGroups_ObjectIdentity=ObjectIdentity
alvarionConnectionLimitingMIBGroups=_AlvarionConnectionLimitingMIBGroups_ObjectIdentity((1,3,6,1,4,1,12394,1,10,5,18,3,2))
alvarionConnectionLimitingConfigMIBGroup=ObjectGroup((1,3,6,1,4,1,12394,1,10,5,18,3,2,1))
alvarionConnectionLimitingConfigMIBGroup.setObjects((_B,_D))
if mibBuilder.loadTexts:alvarionConnectionLimitingConfigMIBGroup.setStatus(_A)
alvarionConnectionLimitingInfoMIBGroup=ObjectGroup((1,3,6,1,4,1,12394,1,10,5,18,3,2,2))
alvarionConnectionLimitingInfoMIBGroup.setObjects((_B,_E))
if mibBuilder.loadTexts:alvarionConnectionLimitingInfoMIBGroup.setStatus(_A)
alvarionConnectionLimitingMIBCompliance=ModuleCompliance((1,3,6,1,4,1,12394,1,10,5,18,3,1,1))
alvarionConnectionLimitingMIBCompliance.setObjects(*((_B,_F),(_B,_G)))
if mibBuilder.loadTexts:alvarionConnectionLimitingMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'alvarionConnectionLimitingMIB':alvarionConnectionLimitingMIB,'alvarionConnectionLimitingMIBObjects':alvarionConnectionLimitingMIBObjects,'connectionLimitingConfig':connectionLimitingConfig,_D:connectionLimitingMaximumUserConnections,'connectionLimitingInfo':connectionLimitingInfo,_E:connectionLimitingMaximumSystemConnections,'alvarionConnectionLimitingMIBNotificationPrefix':alvarionConnectionLimitingMIBNotificationPrefix,'alvarionConnectionLimitingMIBNotifications':alvarionConnectionLimitingMIBNotifications,'alvarionConnectionLimitingMIBConformance':alvarionConnectionLimitingMIBConformance,'alvarionConnectionLimitingMIBCompliances':alvarionConnectionLimitingMIBCompliances,'alvarionConnectionLimitingMIBCompliance':alvarionConnectionLimitingMIBCompliance,'alvarionConnectionLimitingMIBGroups':alvarionConnectionLimitingMIBGroups,_F:alvarionConnectionLimitingConfigMIBGroup,_G:alvarionConnectionLimitingInfoMIBGroup})