_G='rbnDs1Group'
_F='rbnDsx1AlarmServiceAffecting'
_E='rbnDsx1AlarmSeverity'
_D='rbnDsx1ConfigEntry'
_C='read-only'
_B='RBN-DS1-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
dsx1ConfigEntry,=mibBuilder.importSymbols('DS1-MIB','dsx1ConfigEntry')
RbnAlarmPerceivedSeverity,RbnAlarmServiceAffecting=mibBuilder.importSymbols('RBN-ALARM-TC','RbnAlarmPerceivedSeverity','RbnAlarmServiceAffecting')
rbnMgmt,=mibBuilder.importSymbols('RBN-SMI','rbnMgmt')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
rbnDS1MIB=ModuleIdentity((1,3,6,1,4,1,2352,2,37))
if mibBuilder.loadTexts:rbnDS1MIB.setRevisions(('2005-05-09 00:00',))
_RbnDs1MIBObjects_ObjectIdentity=ObjectIdentity
rbnDs1MIBObjects=_RbnDs1MIBObjects_ObjectIdentity((1,3,6,1,4,1,2352,2,37,1))
_RbnDsx1ConfigTable_Object=MibTable
rbnDsx1ConfigTable=_RbnDsx1ConfigTable_Object((1,3,6,1,4,1,2352,2,37,1,1))
if mibBuilder.loadTexts:rbnDsx1ConfigTable.setStatus(_A)
_RbnDsx1ConfigEntry_Object=MibTableRow
rbnDsx1ConfigEntry=_RbnDsx1ConfigEntry_Object((1,3,6,1,4,1,2352,2,37,1,1,1))
if mibBuilder.loadTexts:rbnDsx1ConfigEntry.setStatus(_A)
_RbnDsx1AlarmSeverity_Type=RbnAlarmPerceivedSeverity
_RbnDsx1AlarmSeverity_Object=MibTableColumn
rbnDsx1AlarmSeverity=_RbnDsx1AlarmSeverity_Object((1,3,6,1,4,1,2352,2,37,1,1,1,1),_RbnDsx1AlarmSeverity_Type())
rbnDsx1AlarmSeverity.setMaxAccess(_C)
if mibBuilder.loadTexts:rbnDsx1AlarmSeverity.setStatus(_A)
_RbnDsx1AlarmServiceAffecting_Type=RbnAlarmServiceAffecting
_RbnDsx1AlarmServiceAffecting_Object=MibTableColumn
rbnDsx1AlarmServiceAffecting=_RbnDsx1AlarmServiceAffecting_Object((1,3,6,1,4,1,2352,2,37,1,1,1,2),_RbnDsx1AlarmServiceAffecting_Type())
rbnDsx1AlarmServiceAffecting.setMaxAccess(_C)
if mibBuilder.loadTexts:rbnDsx1AlarmServiceAffecting.setStatus(_A)
_RbnDs1MIBConformance_ObjectIdentity=ObjectIdentity
rbnDs1MIBConformance=_RbnDs1MIBConformance_ObjectIdentity((1,3,6,1,4,1,2352,2,37,2))
_RbnDs1MIBGroups_ObjectIdentity=ObjectIdentity
rbnDs1MIBGroups=_RbnDs1MIBGroups_ObjectIdentity((1,3,6,1,4,1,2352,2,37,2,1))
_RbnDs1MIBCompliances_ObjectIdentity=ObjectIdentity
rbnDs1MIBCompliances=_RbnDs1MIBCompliances_ObjectIdentity((1,3,6,1,4,1,2352,2,37,2,2))
dsx1ConfigEntry.registerAugmentions((_B,_D))
rbnDsx1ConfigEntry.setIndexNames(*dsx1ConfigEntry.getIndexNames())
rbnDs1Group=ObjectGroup((1,3,6,1,4,1,2352,2,37,2,1,1))
rbnDs1Group.setObjects(*((_B,_E),(_B,_F)))
if mibBuilder.loadTexts:rbnDs1Group.setStatus(_A)
rbnDs1MIBCompliance=ModuleCompliance((1,3,6,1,4,1,2352,2,37,2,2,1))
rbnDs1MIBCompliance.setObjects((_B,_G))
if mibBuilder.loadTexts:rbnDs1MIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'rbnDS1MIB':rbnDS1MIB,'rbnDs1MIBObjects':rbnDs1MIBObjects,'rbnDsx1ConfigTable':rbnDsx1ConfigTable,_D:rbnDsx1ConfigEntry,_E:rbnDsx1AlarmSeverity,_F:rbnDsx1AlarmServiceAffecting,'rbnDs1MIBConformance':rbnDs1MIBConformance,'rbnDs1MIBGroups':rbnDs1MIBGroups,_G:rbnDs1Group,'rbnDs1MIBCompliances':rbnDs1MIBCompliances,'rbnDs1MIBCompliance':rbnDs1MIBCompliance})