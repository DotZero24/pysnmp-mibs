_E='ciscoIpUplinkRedirectMIBGroup'
_D='ciurOperStatus'
_C='ciurStartupStatus'
_B='CISCO-IP-UPLINK-REDIRECT-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention','TruthValue')
ciscoIpUplinkRedirectMIB=ModuleIdentity((1,3,6,1,4,1,9,9,191))
if mibBuilder.loadTexts:ciscoIpUplinkRedirectMIB.setRevisions(('2001-01-22 00:00',))
_CiscoIpUplinkRedirectMIBObjects_ObjectIdentity=ObjectIdentity
ciscoIpUplinkRedirectMIBObjects=_CiscoIpUplinkRedirectMIBObjects_ObjectIdentity((1,3,6,1,4,1,9,9,191,1))
_CiurStartupStatus_Type=TruthValue
_CiurStartupStatus_Object=MibScalar
ciurStartupStatus=_CiurStartupStatus_Object((1,3,6,1,4,1,9,9,191,1,1),_CiurStartupStatus_Type())
ciurStartupStatus.setMaxAccess('read-write')
if mibBuilder.loadTexts:ciurStartupStatus.setStatus(_A)
_CiurOperStatus_Type=TruthValue
_CiurOperStatus_Object=MibScalar
ciurOperStatus=_CiurOperStatus_Object((1,3,6,1,4,1,9,9,191,1,2),_CiurOperStatus_Type())
ciurOperStatus.setMaxAccess('read-only')
if mibBuilder.loadTexts:ciurOperStatus.setStatus(_A)
_CiscoIpUplinkRedirectMIBNotificationPrefix_ObjectIdentity=ObjectIdentity
ciscoIpUplinkRedirectMIBNotificationPrefix=_CiscoIpUplinkRedirectMIBNotificationPrefix_ObjectIdentity((1,3,6,1,4,1,9,9,191,2))
_CiscoIpUplinkRedirectMIBConformance_ObjectIdentity=ObjectIdentity
ciscoIpUplinkRedirectMIBConformance=_CiscoIpUplinkRedirectMIBConformance_ObjectIdentity((1,3,6,1,4,1,9,9,191,3))
_CiscoIpUplinkRedirectMIBCompliances_ObjectIdentity=ObjectIdentity
ciscoIpUplinkRedirectMIBCompliances=_CiscoIpUplinkRedirectMIBCompliances_ObjectIdentity((1,3,6,1,4,1,9,9,191,3,1))
_CiscoIpUplinkRedirectMIBGroups_ObjectIdentity=ObjectIdentity
ciscoIpUplinkRedirectMIBGroups=_CiscoIpUplinkRedirectMIBGroups_ObjectIdentity((1,3,6,1,4,1,9,9,191,3,2))
ciscoIpUplinkRedirectMIBGroup=ObjectGroup((1,3,6,1,4,1,9,9,191,3,2,1))
ciscoIpUplinkRedirectMIBGroup.setObjects(*((_B,_C),(_B,_D)))
if mibBuilder.loadTexts:ciscoIpUplinkRedirectMIBGroup.setStatus(_A)
ciscoIpUplinkRedirectMIBCompliance=ModuleCompliance((1,3,6,1,4,1,9,9,191,3,1,1))
ciscoIpUplinkRedirectMIBCompliance.setObjects((_B,_E))
if mibBuilder.loadTexts:ciscoIpUplinkRedirectMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'ciscoIpUplinkRedirectMIB':ciscoIpUplinkRedirectMIB,'ciscoIpUplinkRedirectMIBObjects':ciscoIpUplinkRedirectMIBObjects,_C:ciurStartupStatus,_D:ciurOperStatus,'ciscoIpUplinkRedirectMIBNotificationPrefix':ciscoIpUplinkRedirectMIBNotificationPrefix,'ciscoIpUplinkRedirectMIBConformance':ciscoIpUplinkRedirectMIBConformance,'ciscoIpUplinkRedirectMIBCompliances':ciscoIpUplinkRedirectMIBCompliances,'ciscoIpUplinkRedirectMIBCompliance':ciscoIpUplinkRedirectMIBCompliance,'ciscoIpUplinkRedirectMIBGroups':ciscoIpUplinkRedirectMIBGroups,_E:ciscoIpUplinkRedirectMIBGroup})