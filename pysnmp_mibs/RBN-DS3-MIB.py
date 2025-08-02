_G='rbnDs3Group'
_F='rbnDsx3AlarmServiceAffecting'
_E='rbnDsx3AlarmSeverity'
_D='rbnDsx3ConfigEntry'
_C='read-only'
_B='RBN-DS3-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
dsx3ConfigEntry,=mibBuilder.importSymbols('DS3-MIB','dsx3ConfigEntry')
RbnAlarmPerceivedSeverity,RbnAlarmServiceAffecting=mibBuilder.importSymbols('RBN-ALARM-TC','RbnAlarmPerceivedSeverity','RbnAlarmServiceAffecting')
rbnMgmt,=mibBuilder.importSymbols('RBN-SMI','rbnMgmt')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
rbnDS3MIB=ModuleIdentity((1,3,6,1,4,1,2352,2,38))
if mibBuilder.loadTexts:rbnDS3MIB.setRevisions(('2005-05-09 00:00',))
_RbnDs3MIBObjects_ObjectIdentity=ObjectIdentity
rbnDs3MIBObjects=_RbnDs3MIBObjects_ObjectIdentity((1,3,6,1,4,1,2352,2,38,1))
_RbnDsx3ConfigTable_Object=MibTable
rbnDsx3ConfigTable=_RbnDsx3ConfigTable_Object((1,3,6,1,4,1,2352,2,38,1,1))
if mibBuilder.loadTexts:rbnDsx3ConfigTable.setStatus(_A)
_RbnDsx3ConfigEntry_Object=MibTableRow
rbnDsx3ConfigEntry=_RbnDsx3ConfigEntry_Object((1,3,6,1,4,1,2352,2,38,1,1,1))
if mibBuilder.loadTexts:rbnDsx3ConfigEntry.setStatus(_A)
_RbnDsx3AlarmSeverity_Type=RbnAlarmPerceivedSeverity
_RbnDsx3AlarmSeverity_Object=MibTableColumn
rbnDsx3AlarmSeverity=_RbnDsx3AlarmSeverity_Object((1,3,6,1,4,1,2352,2,38,1,1,1,1),_RbnDsx3AlarmSeverity_Type())
rbnDsx3AlarmSeverity.setMaxAccess(_C)
if mibBuilder.loadTexts:rbnDsx3AlarmSeverity.setStatus(_A)
_RbnDsx3AlarmServiceAffecting_Type=RbnAlarmServiceAffecting
_RbnDsx3AlarmServiceAffecting_Object=MibTableColumn
rbnDsx3AlarmServiceAffecting=_RbnDsx3AlarmServiceAffecting_Object((1,3,6,1,4,1,2352,2,38,1,1,1,2),_RbnDsx3AlarmServiceAffecting_Type())
rbnDsx3AlarmServiceAffecting.setMaxAccess(_C)
if mibBuilder.loadTexts:rbnDsx3AlarmServiceAffecting.setStatus(_A)
_RbnDs3MIBConformance_ObjectIdentity=ObjectIdentity
rbnDs3MIBConformance=_RbnDs3MIBConformance_ObjectIdentity((1,3,6,1,4,1,2352,2,38,2))
_RbnDs3MIBGroups_ObjectIdentity=ObjectIdentity
rbnDs3MIBGroups=_RbnDs3MIBGroups_ObjectIdentity((1,3,6,1,4,1,2352,2,38,2,1))
_RbnDs3MIBCompliances_ObjectIdentity=ObjectIdentity
rbnDs3MIBCompliances=_RbnDs3MIBCompliances_ObjectIdentity((1,3,6,1,4,1,2352,2,38,2,2))
dsx3ConfigEntry.registerAugmentions((_B,_D))
rbnDsx3ConfigEntry.setIndexNames(*dsx3ConfigEntry.getIndexNames())
rbnDs3Group=ObjectGroup((1,3,6,1,4,1,2352,2,38,2,1,1))
rbnDs3Group.setObjects(*((_B,_E),(_B,_F)))
if mibBuilder.loadTexts:rbnDs3Group.setStatus(_A)
rbnDs3MIBCompliance=ModuleCompliance((1,3,6,1,4,1,2352,2,38,2,2,1))
rbnDs3MIBCompliance.setObjects((_B,_G))
if mibBuilder.loadTexts:rbnDs3MIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'rbnDS3MIB':rbnDS3MIB,'rbnDs3MIBObjects':rbnDs3MIBObjects,'rbnDsx3ConfigTable':rbnDsx3ConfigTable,_D:rbnDsx3ConfigEntry,_E:rbnDsx3AlarmSeverity,_F:rbnDsx3AlarmServiceAffecting,'rbnDs3MIBConformance':rbnDs3MIBConformance,'rbnDs3MIBGroups':rbnDs3MIBGroups,_G:rbnDs3Group,'rbnDs3MIBCompliances':rbnDs3MIBCompliances,'rbnDs3MIBCompliance':rbnDs3MIBCompliance})