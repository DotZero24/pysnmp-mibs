_Q='ciscoLwappScheduledWlanConfigGroup'
_P='cLCalendarProfileMonthlyProfileRowStatus'
_O='cLCalendarProfileWeeklyProfileRowStatus'
_N='cLCalendarProfileRecurrence'
_M='cLCalendarProfileEndTime'
_L='cLCalendarProfileStartTime'
_K='cLCalendarProfileRowStatus'
_J='cLCalendarProfileMonthlyProfileDate'
_I='cLCalendarProfileWeeklyProfileDay'
_H='read-write'
_G='read-create'
_F='not-accessible'
_E='Integer32'
_D='cLCalendarProfileName'
_C='SnmpAdminString'
_B='CISCO-LWAPP-SCHEDULED-WLAN-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB',_C)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention')
ciscoCapwapScheduledWlanMIB=ModuleIdentity((1,3,6,1,4,1,9,9,864))
if mibBuilder.loadTexts:ciscoCapwapScheduledWlanMIB.setRevisions(('2019-04-07 00:00',))
_CiscoLwappScheduledWlanMIBNotifs_ObjectIdentity=ObjectIdentity
ciscoLwappScheduledWlanMIBNotifs=_CiscoLwappScheduledWlanMIBNotifs_ObjectIdentity((1,3,6,1,4,1,9,9,864,0))
_CiscoLwappScheduledWlanMIBObjects_ObjectIdentity=ObjectIdentity
ciscoLwappScheduledWlanMIBObjects=_CiscoLwappScheduledWlanMIBObjects_ObjectIdentity((1,3,6,1,4,1,9,9,864,1))
_CiscoLwappScheduledWlanConfig_ObjectIdentity=ObjectIdentity
ciscoLwappScheduledWlanConfig=_CiscoLwappScheduledWlanConfig_ObjectIdentity((1,3,6,1,4,1,9,9,864,1,1))
_CLCalendarProfileConfigTable_Object=MibTable
cLCalendarProfileConfigTable=_CLCalendarProfileConfigTable_Object((1,3,6,1,4,1,9,9,864,1,1,1))
if mibBuilder.loadTexts:cLCalendarProfileConfigTable.setStatus(_A)
_CLCalendarProfileConfigEntry_Object=MibTableRow
cLCalendarProfileConfigEntry=_CLCalendarProfileConfigEntry_Object((1,3,6,1,4,1,9,9,864,1,1,1,1))
cLCalendarProfileConfigEntry.setIndexNames((0,_B,_D))
if mibBuilder.loadTexts:cLCalendarProfileConfigEntry.setStatus(_A)
class _CLCalendarProfileName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_CLCalendarProfileName_Type.__name__=_C
_CLCalendarProfileName_Object=MibTableColumn
cLCalendarProfileName=_CLCalendarProfileName_Object((1,3,6,1,4,1,9,9,864,1,1,1,1,1),_CLCalendarProfileName_Type())
cLCalendarProfileName.setMaxAccess(_F)
if mibBuilder.loadTexts:cLCalendarProfileName.setStatus(_A)
_CLCalendarProfileRowStatus_Type=RowStatus
_CLCalendarProfileRowStatus_Object=MibTableColumn
cLCalendarProfileRowStatus=_CLCalendarProfileRowStatus_Object((1,3,6,1,4,1,9,9,864,1,1,1,1,2),_CLCalendarProfileRowStatus_Type())
cLCalendarProfileRowStatus.setMaxAccess(_G)
if mibBuilder.loadTexts:cLCalendarProfileRowStatus.setStatus(_A)
class _CLCalendarProfileStartTime_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_CLCalendarProfileStartTime_Type.__name__=_C
_CLCalendarProfileStartTime_Object=MibTableColumn
cLCalendarProfileStartTime=_CLCalendarProfileStartTime_Object((1,3,6,1,4,1,9,9,864,1,1,1,1,3),_CLCalendarProfileStartTime_Type())
cLCalendarProfileStartTime.setMaxAccess(_H)
if mibBuilder.loadTexts:cLCalendarProfileStartTime.setStatus(_A)
class _CLCalendarProfileEndTime_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_CLCalendarProfileEndTime_Type.__name__=_C
_CLCalendarProfileEndTime_Object=MibTableColumn
cLCalendarProfileEndTime=_CLCalendarProfileEndTime_Object((1,3,6,1,4,1,9,9,864,1,1,1,1,4),_CLCalendarProfileEndTime_Type())
cLCalendarProfileEndTime.setMaxAccess(_H)
if mibBuilder.loadTexts:cLCalendarProfileEndTime.setStatus(_A)
class _CLCalendarProfileRecurrence_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('daily',0),('weekly',1),('monthly',2)))
_CLCalendarProfileRecurrence_Type.__name__=_E
_CLCalendarProfileRecurrence_Object=MibTableColumn
cLCalendarProfileRecurrence=_CLCalendarProfileRecurrence_Object((1,3,6,1,4,1,9,9,864,1,1,1,1,5),_CLCalendarProfileRecurrence_Type())
cLCalendarProfileRecurrence.setMaxAccess(_H)
if mibBuilder.loadTexts:cLCalendarProfileRecurrence.setStatus(_A)
_CLCalendarProfileWeeklyConfigTable_Object=MibTable
cLCalendarProfileWeeklyConfigTable=_CLCalendarProfileWeeklyConfigTable_Object((1,3,6,1,4,1,9,9,864,1,1,2))
if mibBuilder.loadTexts:cLCalendarProfileWeeklyConfigTable.setStatus(_A)
_CLCalendarProfileWeeklyConfigEntry_Object=MibTableRow
cLCalendarProfileWeeklyConfigEntry=_CLCalendarProfileWeeklyConfigEntry_Object((1,3,6,1,4,1,9,9,864,1,1,2,1))
cLCalendarProfileWeeklyConfigEntry.setIndexNames((0,_B,_D),(0,_B,_I))
if mibBuilder.loadTexts:cLCalendarProfileWeeklyConfigEntry.setStatus(_A)
class _CLCalendarProfileWeeklyProfileDay_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*(('monday',1),('tuesday',2),('wednesday',3),('thursday',4),('friday',5),('saturday',6),('sunday',7)))
_CLCalendarProfileWeeklyProfileDay_Type.__name__=_E
_CLCalendarProfileWeeklyProfileDay_Object=MibTableColumn
cLCalendarProfileWeeklyProfileDay=_CLCalendarProfileWeeklyProfileDay_Object((1,3,6,1,4,1,9,9,864,1,1,2,1,1),_CLCalendarProfileWeeklyProfileDay_Type())
cLCalendarProfileWeeklyProfileDay.setMaxAccess(_F)
if mibBuilder.loadTexts:cLCalendarProfileWeeklyProfileDay.setStatus(_A)
_CLCalendarProfileWeeklyProfileRowStatus_Type=RowStatus
_CLCalendarProfileWeeklyProfileRowStatus_Object=MibTableColumn
cLCalendarProfileWeeklyProfileRowStatus=_CLCalendarProfileWeeklyProfileRowStatus_Object((1,3,6,1,4,1,9,9,864,1,1,2,1,2),_CLCalendarProfileWeeklyProfileRowStatus_Type())
cLCalendarProfileWeeklyProfileRowStatus.setMaxAccess(_G)
if mibBuilder.loadTexts:cLCalendarProfileWeeklyProfileRowStatus.setStatus(_A)
_CLCalendarProfileMonthlyConfigTable_Object=MibTable
cLCalendarProfileMonthlyConfigTable=_CLCalendarProfileMonthlyConfigTable_Object((1,3,6,1,4,1,9,9,864,1,1,3))
if mibBuilder.loadTexts:cLCalendarProfileMonthlyConfigTable.setStatus(_A)
_CLCalendarProfileMonthlyConfigEntry_Object=MibTableRow
cLCalendarProfileMonthlyConfigEntry=_CLCalendarProfileMonthlyConfigEntry_Object((1,3,6,1,4,1,9,9,864,1,1,3,1))
cLCalendarProfileMonthlyConfigEntry.setIndexNames((0,_B,_D),(0,_B,_J))
if mibBuilder.loadTexts:cLCalendarProfileMonthlyConfigEntry.setStatus(_A)
_CLCalendarProfileMonthlyProfileDate_Type=Unsigned32
_CLCalendarProfileMonthlyProfileDate_Object=MibTableColumn
cLCalendarProfileMonthlyProfileDate=_CLCalendarProfileMonthlyProfileDate_Object((1,3,6,1,4,1,9,9,864,1,1,3,1,1),_CLCalendarProfileMonthlyProfileDate_Type())
cLCalendarProfileMonthlyProfileDate.setMaxAccess(_F)
if mibBuilder.loadTexts:cLCalendarProfileMonthlyProfileDate.setStatus(_A)
_CLCalendarProfileMonthlyProfileRowStatus_Type=RowStatus
_CLCalendarProfileMonthlyProfileRowStatus_Object=MibTableColumn
cLCalendarProfileMonthlyProfileRowStatus=_CLCalendarProfileMonthlyProfileRowStatus_Object((1,3,6,1,4,1,9,9,864,1,1,3,1,2),_CLCalendarProfileMonthlyProfileRowStatus_Type())
cLCalendarProfileMonthlyProfileRowStatus.setMaxAccess(_G)
if mibBuilder.loadTexts:cLCalendarProfileMonthlyProfileRowStatus.setStatus(_A)
_CiscoLwappScheduledWlanConform_ObjectIdentity=ObjectIdentity
ciscoLwappScheduledWlanConform=_CiscoLwappScheduledWlanConform_ObjectIdentity((1,3,6,1,4,1,9,9,864,2))
_CiscoLwappScheduledWlanCompliances_ObjectIdentity=ObjectIdentity
ciscoLwappScheduledWlanCompliances=_CiscoLwappScheduledWlanCompliances_ObjectIdentity((1,3,6,1,4,1,9,9,864,2,1))
_CiscoLwappScheduledWlanGroups_ObjectIdentity=ObjectIdentity
ciscoLwappScheduledWlanGroups=_CiscoLwappScheduledWlanGroups_ObjectIdentity((1,3,6,1,4,1,9,9,864,2,2))
ciscoLwappScheduledWlanConfigGroup=ObjectGroup((1,3,6,1,4,1,9,9,864,2,2,1))
ciscoLwappScheduledWlanConfigGroup.setObjects(*((_B,_K),(_B,_L),(_B,_M),(_B,_N),(_B,_O),(_B,_P)))
if mibBuilder.loadTexts:ciscoLwappScheduledWlanConfigGroup.setStatus(_A)
ciscoLwappScheduledWlanCompliance=ModuleCompliance((1,3,6,1,4,1,9,9,864,2,1,1))
ciscoLwappScheduledWlanCompliance.setObjects((_B,_Q))
if mibBuilder.loadTexts:ciscoLwappScheduledWlanCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'ciscoCapwapScheduledWlanMIB':ciscoCapwapScheduledWlanMIB,'ciscoLwappScheduledWlanMIBNotifs':ciscoLwappScheduledWlanMIBNotifs,'ciscoLwappScheduledWlanMIBObjects':ciscoLwappScheduledWlanMIBObjects,'ciscoLwappScheduledWlanConfig':ciscoLwappScheduledWlanConfig,'cLCalendarProfileConfigTable':cLCalendarProfileConfigTable,'cLCalendarProfileConfigEntry':cLCalendarProfileConfigEntry,_D:cLCalendarProfileName,_K:cLCalendarProfileRowStatus,_L:cLCalendarProfileStartTime,_M:cLCalendarProfileEndTime,_N:cLCalendarProfileRecurrence,'cLCalendarProfileWeeklyConfigTable':cLCalendarProfileWeeklyConfigTable,'cLCalendarProfileWeeklyConfigEntry':cLCalendarProfileWeeklyConfigEntry,_I:cLCalendarProfileWeeklyProfileDay,_O:cLCalendarProfileWeeklyProfileRowStatus,'cLCalendarProfileMonthlyConfigTable':cLCalendarProfileMonthlyConfigTable,'cLCalendarProfileMonthlyConfigEntry':cLCalendarProfileMonthlyConfigEntry,_J:cLCalendarProfileMonthlyProfileDate,_P:cLCalendarProfileMonthlyProfileRowStatus,'ciscoLwappScheduledWlanConform':ciscoLwappScheduledWlanConform,'ciscoLwappScheduledWlanCompliances':ciscoLwappScheduledWlanCompliances,'ciscoLwappScheduledWlanCompliance':ciscoLwappScheduledWlanCompliance,'ciscoLwappScheduledWlanGroups':ciscoLwappScheduledWlanGroups,_Q:ciscoLwappScheduledWlanConfigGroup})