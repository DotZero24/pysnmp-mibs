_J='deviceHealthCheckMIBGroup'
_I='deviceHealthCheckTrap'
_H='deviceHealthCheckTime'
_G='deviceHealthCheckState'
_F='DisplayString'
_E='deviceHealthCheckMessage'
_D='deviceHealthCheckName'
_C='read-only'
_B='BLUECOAT-SG-HEALTHCHECK-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
blueCoatMgmt,=mibBuilder.importSymbols('BLUECOAT-MIB','blueCoatMgmt')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_F,'PhysAddress','TextualConvention')
deviceHealthCheckMIB=ModuleIdentity((1,3,6,1,4,1,3417,2,7))
if mibBuilder.loadTexts:deviceHealthCheckMIB.setRevisions(('2013-05-22 03:00','2013-05-21 03:00','2007-11-05 03:00','2002-08-28 03:00'))
class HealthCheckMessageString(TextualConvention,OctetString):status=_A;displayHint='255a';subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
class HealthCheckStatus(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8)));namedValues=NamedValues(*(('unknown',1),('ok',2),('okWithErrors',3),('okForSomeIPs',4),('okButFailing',5),('checkFailed',6),('dnsFailed',7),('okOnAltServer',8)))
_DeviceHealthCheckMIBObjects_ObjectIdentity=ObjectIdentity
deviceHealthCheckMIBObjects=_DeviceHealthCheckMIBObjects_ObjectIdentity((1,3,6,1,4,1,3417,2,7,1))
_DeviceHealthCheckStringValues_ObjectIdentity=ObjectIdentity
deviceHealthCheckStringValues=_DeviceHealthCheckStringValues_ObjectIdentity((1,3,6,1,4,1,3417,2,7,1,1))
_DeviceHealthCheckMessage_Type=HealthCheckMessageString
_DeviceHealthCheckMessage_Object=MibScalar
deviceHealthCheckMessage=_DeviceHealthCheckMessage_Object((1,3,6,1,4,1,3417,2,7,1,1,1),_DeviceHealthCheckMessage_Type())
deviceHealthCheckMessage.setMaxAccess(_C)
if mibBuilder.loadTexts:deviceHealthCheckMessage.setStatus(_A)
_DeviceHealthCheckValues_ObjectIdentity=ObjectIdentity
deviceHealthCheckValues=_DeviceHealthCheckValues_ObjectIdentity((1,3,6,1,4,1,3417,2,7,1,2))
_DeviceHealthCheckValueTable_Object=MibTable
deviceHealthCheckValueTable=_DeviceHealthCheckValueTable_Object((1,3,6,1,4,1,3417,2,7,1,2,1))
if mibBuilder.loadTexts:deviceHealthCheckValueTable.setStatus(_A)
_DeviceHealthCheckValueEntry_Object=MibTableRow
deviceHealthCheckValueEntry=_DeviceHealthCheckValueEntry_Object((1,3,6,1,4,1,3417,2,7,1,2,1,1))
deviceHealthCheckValueEntry.setIndexNames((0,_B,_D))
if mibBuilder.loadTexts:deviceHealthCheckValueEntry.setStatus(_A)
class _DeviceHealthCheckName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,127))
_DeviceHealthCheckName_Type.__name__=_F
_DeviceHealthCheckName_Object=MibTableColumn
deviceHealthCheckName=_DeviceHealthCheckName_Object((1,3,6,1,4,1,3417,2,7,1,2,1,1,1),_DeviceHealthCheckName_Type())
deviceHealthCheckName.setMaxAccess(_C)
if mibBuilder.loadTexts:deviceHealthCheckName.setStatus(_A)
_DeviceHealthCheckState_Type=HealthCheckStatus
_DeviceHealthCheckState_Object=MibTableColumn
deviceHealthCheckState=_DeviceHealthCheckState_Object((1,3,6,1,4,1,3417,2,7,1,2,1,1,2),_DeviceHealthCheckState_Type())
deviceHealthCheckState.setMaxAccess(_C)
if mibBuilder.loadTexts:deviceHealthCheckState.setStatus(_A)
_DeviceHealthCheckTime_Type=Counter64
_DeviceHealthCheckTime_Object=MibTableColumn
deviceHealthCheckTime=_DeviceHealthCheckTime_Object((1,3,6,1,4,1,3417,2,7,1,2,1,1,3),_DeviceHealthCheckTime_Type())
deviceHealthCheckTime.setMaxAccess(_C)
if mibBuilder.loadTexts:deviceHealthCheckTime.setStatus(_A)
_DeviceHealthCheckMIBNotifs_ObjectIdentity=ObjectIdentity
deviceHealthCheckMIBNotifs=_DeviceHealthCheckMIBNotifs_ObjectIdentity((1,3,6,1,4,1,3417,2,7,2))
_DeviceHealthCheckMIBNotifsPrefix_ObjectIdentity=ObjectIdentity
deviceHealthCheckMIBNotifsPrefix=_DeviceHealthCheckMIBNotifsPrefix_ObjectIdentity((1,3,6,1,4,1,3417,2,7,2,0))
_DeviceHealthCheckMIBConformance_ObjectIdentity=ObjectIdentity
deviceHealthCheckMIBConformance=_DeviceHealthCheckMIBConformance_ObjectIdentity((1,3,6,1,4,1,3417,2,7,3))
_DeviceHealthCheckMIBCompliances_ObjectIdentity=ObjectIdentity
deviceHealthCheckMIBCompliances=_DeviceHealthCheckMIBCompliances_ObjectIdentity((1,3,6,1,4,1,3417,2,7,3,1))
_DeviceHealthCheckMIBGroups_ObjectIdentity=ObjectIdentity
deviceHealthCheckMIBGroups=_DeviceHealthCheckMIBGroups_ObjectIdentity((1,3,6,1,4,1,3417,2,7,3,2))
_DeviceHealthCheckMIBNotifGroups_ObjectIdentity=ObjectIdentity
deviceHealthCheckMIBNotifGroups=_DeviceHealthCheckMIBNotifGroups_ObjectIdentity((1,3,6,1,4,1,3417,2,7,3,3))
deviceHealthCheckMIBGroup=ObjectGroup((1,3,6,1,4,1,3417,2,7,3,2,1))
deviceHealthCheckMIBGroup.setObjects(*((_B,_D),(_B,_G),(_B,_H),(_B,_E)))
if mibBuilder.loadTexts:deviceHealthCheckMIBGroup.setStatus(_A)
deviceHealthCheckTrap=NotificationType((1,3,6,1,4,1,3417,2,7,2,0,1))
deviceHealthCheckTrap.setObjects((_B,_E))
if mibBuilder.loadTexts:deviceHealthCheckTrap.setStatus(_A)
deviceHealthCheckMIBNotifGroup=NotificationGroup((1,3,6,1,4,1,3417,2,7,3,3,1))
deviceHealthCheckMIBNotifGroup.setObjects((_B,_I))
if mibBuilder.loadTexts:deviceHealthCheckMIBNotifGroup.setStatus(_A)
deviceHealthCheckMIBCompliance=ModuleCompliance((1,3,6,1,4,1,3417,2,7,3,1,1))
deviceHealthCheckMIBCompliance.setObjects((_B,_J))
if mibBuilder.loadTexts:deviceHealthCheckMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'HealthCheckMessageString':HealthCheckMessageString,'HealthCheckStatus':HealthCheckStatus,'deviceHealthCheckMIB':deviceHealthCheckMIB,'deviceHealthCheckMIBObjects':deviceHealthCheckMIBObjects,'deviceHealthCheckStringValues':deviceHealthCheckStringValues,_E:deviceHealthCheckMessage,'deviceHealthCheckValues':deviceHealthCheckValues,'deviceHealthCheckValueTable':deviceHealthCheckValueTable,'deviceHealthCheckValueEntry':deviceHealthCheckValueEntry,_D:deviceHealthCheckName,_G:deviceHealthCheckState,_H:deviceHealthCheckTime,'deviceHealthCheckMIBNotifs':deviceHealthCheckMIBNotifs,'deviceHealthCheckMIBNotifsPrefix':deviceHealthCheckMIBNotifsPrefix,_I:deviceHealthCheckTrap,'deviceHealthCheckMIBConformance':deviceHealthCheckMIBConformance,'deviceHealthCheckMIBCompliances':deviceHealthCheckMIBCompliances,'deviceHealthCheckMIBCompliance':deviceHealthCheckMIBCompliance,'deviceHealthCheckMIBGroups':deviceHealthCheckMIBGroups,_J:deviceHealthCheckMIBGroup,'deviceHealthCheckMIBNotifGroups':deviceHealthCheckMIBNotifGroups,'deviceHealthCheckMIBNotifGroup':deviceHealthCheckMIBNotifGroup})