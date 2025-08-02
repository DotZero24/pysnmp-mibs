_I='deviceHealthMonMIBGroup'
_H='deviceHealthMonCriticalTrap'
_G='deviceHealthMonWarningTrap'
_F='deviceHealthMonOkTrap'
_E='deviceHealthMonStatus'
_D='read-only'
_C='deviceHealthMonMessage'
_B='BLUECOAT-SG-HEALTHMONITOR-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
blueCoatMgmt,=mibBuilder.importSymbols('BLUECOAT-MIB','blueCoatMgmt')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
bluecoatSGHealthMonMIB=ModuleIdentity((1,3,6,1,4,1,3417,2,12))
if mibBuilder.loadTexts:bluecoatSGHealthMonMIB.setRevisions(('2013-06-10 03:00','2007-11-05 03:00'))
class HealthMonMessageString(TextualConvention,OctetString):status=_A;displayHint='255a';subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
class HealthMonStatus(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('ok',1),('warning',2),('critical',3),('unknown',4)))
_DeviceHealthMonMIBObjects_ObjectIdentity=ObjectIdentity
deviceHealthMonMIBObjects=_DeviceHealthMonMIBObjects_ObjectIdentity((1,3,6,1,4,1,3417,2,12,1))
_DeviceHealthMonValues_ObjectIdentity=ObjectIdentity
deviceHealthMonValues=_DeviceHealthMonValues_ObjectIdentity((1,3,6,1,4,1,3417,2,12,1,1))
_DeviceHealthMonMessage_Type=HealthMonMessageString
_DeviceHealthMonMessage_Object=MibScalar
deviceHealthMonMessage=_DeviceHealthMonMessage_Object((1,3,6,1,4,1,3417,2,12,1,1,1),_DeviceHealthMonMessage_Type())
deviceHealthMonMessage.setMaxAccess(_D)
if mibBuilder.loadTexts:deviceHealthMonMessage.setStatus(_A)
_DeviceHealthMonStatus_Type=HealthMonStatus
_DeviceHealthMonStatus_Object=MibScalar
deviceHealthMonStatus=_DeviceHealthMonStatus_Object((1,3,6,1,4,1,3417,2,12,1,1,2),_DeviceHealthMonStatus_Type())
deviceHealthMonStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:deviceHealthMonStatus.setStatus(_A)
_DeviceHealthMonMIBNotification_ObjectIdentity=ObjectIdentity
deviceHealthMonMIBNotification=_DeviceHealthMonMIBNotification_ObjectIdentity((1,3,6,1,4,1,3417,2,12,2))
_DeviceHealthMonMIBNotifPrefix_ObjectIdentity=ObjectIdentity
deviceHealthMonMIBNotifPrefix=_DeviceHealthMonMIBNotifPrefix_ObjectIdentity((1,3,6,1,4,1,3417,2,12,2,0))
_DeviceHealthMonMIBConformance_ObjectIdentity=ObjectIdentity
deviceHealthMonMIBConformance=_DeviceHealthMonMIBConformance_ObjectIdentity((1,3,6,1,4,1,3417,2,12,3))
_DeviceHealthMonMIBCompliances_ObjectIdentity=ObjectIdentity
deviceHealthMonMIBCompliances=_DeviceHealthMonMIBCompliances_ObjectIdentity((1,3,6,1,4,1,3417,2,12,3,1))
_DeviceHealthMonMIBGroups_ObjectIdentity=ObjectIdentity
deviceHealthMonMIBGroups=_DeviceHealthMonMIBGroups_ObjectIdentity((1,3,6,1,4,1,3417,2,12,3,2))
_DeviceHealthMonMIBNotifGroups_ObjectIdentity=ObjectIdentity
deviceHealthMonMIBNotifGroups=_DeviceHealthMonMIBNotifGroups_ObjectIdentity((1,3,6,1,4,1,3417,2,12,3,3))
deviceHealthMonMIBGroup=ObjectGroup((1,3,6,1,4,1,3417,2,12,3,2,1))
deviceHealthMonMIBGroup.setObjects(*((_B,_E),(_B,_C)))
if mibBuilder.loadTexts:deviceHealthMonMIBGroup.setStatus(_A)
deviceHealthMonOkTrap=NotificationType((1,3,6,1,4,1,3417,2,12,2,0,1))
deviceHealthMonOkTrap.setObjects((_B,_C))
if mibBuilder.loadTexts:deviceHealthMonOkTrap.setStatus(_A)
deviceHealthMonWarningTrap=NotificationType((1,3,6,1,4,1,3417,2,12,2,0,2))
deviceHealthMonWarningTrap.setObjects((_B,_C))
if mibBuilder.loadTexts:deviceHealthMonWarningTrap.setStatus(_A)
deviceHealthMonCriticalTrap=NotificationType((1,3,6,1,4,1,3417,2,12,2,0,3))
deviceHealthMonCriticalTrap.setObjects((_B,_C))
if mibBuilder.loadTexts:deviceHealthMonCriticalTrap.setStatus(_A)
deviceHealthMonMIBNotifGroup=NotificationGroup((1,3,6,1,4,1,3417,2,12,3,3,1))
deviceHealthMonMIBNotifGroup.setObjects(*((_B,_F),(_B,_G),(_B,_H)))
if mibBuilder.loadTexts:deviceHealthMonMIBNotifGroup.setStatus(_A)
deviceHealthMonMIBCompliance=ModuleCompliance((1,3,6,1,4,1,3417,2,12,3,1,1))
deviceHealthMonMIBCompliance.setObjects((_B,_I))
if mibBuilder.loadTexts:deviceHealthMonMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'HealthMonMessageString':HealthMonMessageString,'HealthMonStatus':HealthMonStatus,'bluecoatSGHealthMonMIB':bluecoatSGHealthMonMIB,'deviceHealthMonMIBObjects':deviceHealthMonMIBObjects,'deviceHealthMonValues':deviceHealthMonValues,_C:deviceHealthMonMessage,_E:deviceHealthMonStatus,'deviceHealthMonMIBNotification':deviceHealthMonMIBNotification,'deviceHealthMonMIBNotifPrefix':deviceHealthMonMIBNotifPrefix,_F:deviceHealthMonOkTrap,_G:deviceHealthMonWarningTrap,_H:deviceHealthMonCriticalTrap,'deviceHealthMonMIBConformance':deviceHealthMonMIBConformance,'deviceHealthMonMIBCompliances':deviceHealthMonMIBCompliances,'deviceHealthMonMIBCompliance':deviceHealthMonMIBCompliance,'deviceHealthMonMIBGroups':deviceHealthMonMIBGroups,_I:deviceHealthMonMIBGroup,'deviceHealthMonMIBNotifGroups':deviceHealthMonMIBNotifGroups,'deviceHealthMonMIBNotifGroup':deviceHealthMonMIBNotifGroup})