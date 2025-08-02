_W='ciscoHealthMonitorGroup'
_V='ciscoHealthMonitorHealthLevel'
_U='ciscoHealthMonitorPositiveEvents'
_T='ciscoHealthMonitorLowSeverityFaults'
_S='ciscoHealthMonitorMediumSeverityFaults'
_R='ciscoHealthMonitorHighSeverityFaults'
_Q='ciscoHealthMonitorCriticalFaults'
_P='ciscoHealthMonitorCatastrophicFaults'
_O='ciscoHealthMonitorHealthNotifyLowThreshold'
_N='ciscoHealthMonitorHealthNotifyHighThreshold'
_M='ciscoHealthMonitorHealthNotifyEnable'
_L='ciscoHealthMonitorSubsysName'
_K='TruthValue'
_J='SnmpAdminString'
_I='entPhysicalIndex'
_H='ENTITY-MIB'
_G='ciscoHealthMonitorHealth'
_F='HealthLevel'
_E='read-write'
_D='0.01 percent'
_C='read-only'
_B='CISCO-HEALTH-MONITOR-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
entPhysicalIndex,=mibBuilder.importSymbols(_H,_I)
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB',_J)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention',_K)
ciscoHealthMonitorMIB=ModuleIdentity((1,3,6,1,4,1,9,9,243))
if mibBuilder.loadTexts:ciscoHealthMonitorMIB.setRevisions(('2003-09-12 12:30',))
class HealthLevel(TextualConvention,Gauge32):status=_A;subtypeSpec=Gauge32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,10000))
_CiscoHealthMonitorMIBNotifs_ObjectIdentity=ObjectIdentity
ciscoHealthMonitorMIBNotifs=_CiscoHealthMonitorMIBNotifs_ObjectIdentity((1,3,6,1,4,1,9,9,243,0))
_CiscoHealthMonitorMIBObjects_ObjectIdentity=ObjectIdentity
ciscoHealthMonitorMIBObjects=_CiscoHealthMonitorMIBObjects_ObjectIdentity((1,3,6,1,4,1,9,9,243,1))
_CiscoHealthMonitorTable_Object=MibTable
ciscoHealthMonitorTable=_CiscoHealthMonitorTable_Object((1,3,6,1,4,1,9,9,243,1,1))
if mibBuilder.loadTexts:ciscoHealthMonitorTable.setStatus(_A)
_CiscoHealthMonitorEntry_Object=MibTableRow
ciscoHealthMonitorEntry=_CiscoHealthMonitorEntry_Object((1,3,6,1,4,1,9,9,243,1,1,1))
ciscoHealthMonitorEntry.setIndexNames((0,_H,_I),(1,_B,_L))
if mibBuilder.loadTexts:ciscoHealthMonitorEntry.setStatus(_A)
class _CiscoHealthMonitorSubsysName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,128))
_CiscoHealthMonitorSubsysName_Type.__name__=_J
_CiscoHealthMonitorSubsysName_Object=MibTableColumn
ciscoHealthMonitorSubsysName=_CiscoHealthMonitorSubsysName_Object((1,3,6,1,4,1,9,9,243,1,1,1,1),_CiscoHealthMonitorSubsysName_Type())
ciscoHealthMonitorSubsysName.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:ciscoHealthMonitorSubsysName.setStatus(_A)
_CiscoHealthMonitorHealth_Type=HealthLevel
_CiscoHealthMonitorHealth_Object=MibTableColumn
ciscoHealthMonitorHealth=_CiscoHealthMonitorHealth_Object((1,3,6,1,4,1,9,9,243,1,1,1,2),_CiscoHealthMonitorHealth_Type())
ciscoHealthMonitorHealth.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoHealthMonitorHealth.setStatus(_A)
if mibBuilder.loadTexts:ciscoHealthMonitorHealth.setUnits(_D)
class _CiscoHealthMonitorHealthNotifyEnable_Type(TruthValue):defaultValue=2
_CiscoHealthMonitorHealthNotifyEnable_Type.__name__=_K
_CiscoHealthMonitorHealthNotifyEnable_Object=MibTableColumn
ciscoHealthMonitorHealthNotifyEnable=_CiscoHealthMonitorHealthNotifyEnable_Object((1,3,6,1,4,1,9,9,243,1,1,1,3),_CiscoHealthMonitorHealthNotifyEnable_Type())
ciscoHealthMonitorHealthNotifyEnable.setMaxAccess(_E)
if mibBuilder.loadTexts:ciscoHealthMonitorHealthNotifyEnable.setStatus(_A)
class _CiscoHealthMonitorHealthNotifyHighThreshold_Type(HealthLevel):defaultValue=10000
_CiscoHealthMonitorHealthNotifyHighThreshold_Type.__name__=_F
_CiscoHealthMonitorHealthNotifyHighThreshold_Object=MibTableColumn
ciscoHealthMonitorHealthNotifyHighThreshold=_CiscoHealthMonitorHealthNotifyHighThreshold_Object((1,3,6,1,4,1,9,9,243,1,1,1,4),_CiscoHealthMonitorHealthNotifyHighThreshold_Type())
ciscoHealthMonitorHealthNotifyHighThreshold.setMaxAccess(_E)
if mibBuilder.loadTexts:ciscoHealthMonitorHealthNotifyHighThreshold.setStatus(_A)
if mibBuilder.loadTexts:ciscoHealthMonitorHealthNotifyHighThreshold.setUnits(_D)
class _CiscoHealthMonitorHealthNotifyLowThreshold_Type(HealthLevel):defaultValue=0
_CiscoHealthMonitorHealthNotifyLowThreshold_Type.__name__=_F
_CiscoHealthMonitorHealthNotifyLowThreshold_Object=MibTableColumn
ciscoHealthMonitorHealthNotifyLowThreshold=_CiscoHealthMonitorHealthNotifyLowThreshold_Object((1,3,6,1,4,1,9,9,243,1,1,1,5),_CiscoHealthMonitorHealthNotifyLowThreshold_Type())
ciscoHealthMonitorHealthNotifyLowThreshold.setMaxAccess(_E)
if mibBuilder.loadTexts:ciscoHealthMonitorHealthNotifyLowThreshold.setStatus(_A)
if mibBuilder.loadTexts:ciscoHealthMonitorHealthNotifyLowThreshold.setUnits(_D)
_CiscoHealthMonitorCatastrophicFaults_Type=Counter32
_CiscoHealthMonitorCatastrophicFaults_Object=MibTableColumn
ciscoHealthMonitorCatastrophicFaults=_CiscoHealthMonitorCatastrophicFaults_Object((1,3,6,1,4,1,9,9,243,1,1,1,6),_CiscoHealthMonitorCatastrophicFaults_Type())
ciscoHealthMonitorCatastrophicFaults.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoHealthMonitorCatastrophicFaults.setStatus(_A)
_CiscoHealthMonitorCriticalFaults_Type=Counter32
_CiscoHealthMonitorCriticalFaults_Object=MibTableColumn
ciscoHealthMonitorCriticalFaults=_CiscoHealthMonitorCriticalFaults_Object((1,3,6,1,4,1,9,9,243,1,1,1,7),_CiscoHealthMonitorCriticalFaults_Type())
ciscoHealthMonitorCriticalFaults.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoHealthMonitorCriticalFaults.setStatus(_A)
_CiscoHealthMonitorHighSeverityFaults_Type=Counter32
_CiscoHealthMonitorHighSeverityFaults_Object=MibTableColumn
ciscoHealthMonitorHighSeverityFaults=_CiscoHealthMonitorHighSeverityFaults_Object((1,3,6,1,4,1,9,9,243,1,1,1,8),_CiscoHealthMonitorHighSeverityFaults_Type())
ciscoHealthMonitorHighSeverityFaults.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoHealthMonitorHighSeverityFaults.setStatus(_A)
_CiscoHealthMonitorMediumSeverityFaults_Type=Counter32
_CiscoHealthMonitorMediumSeverityFaults_Object=MibTableColumn
ciscoHealthMonitorMediumSeverityFaults=_CiscoHealthMonitorMediumSeverityFaults_Object((1,3,6,1,4,1,9,9,243,1,1,1,9),_CiscoHealthMonitorMediumSeverityFaults_Type())
ciscoHealthMonitorMediumSeverityFaults.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoHealthMonitorMediumSeverityFaults.setStatus(_A)
_CiscoHealthMonitorLowSeverityFaults_Type=Counter32
_CiscoHealthMonitorLowSeverityFaults_Object=MibTableColumn
ciscoHealthMonitorLowSeverityFaults=_CiscoHealthMonitorLowSeverityFaults_Object((1,3,6,1,4,1,9,9,243,1,1,1,10),_CiscoHealthMonitorLowSeverityFaults_Type())
ciscoHealthMonitorLowSeverityFaults.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoHealthMonitorLowSeverityFaults.setStatus(_A)
_CiscoHealthMonitorPositiveEvents_Type=Counter32
_CiscoHealthMonitorPositiveEvents_Object=MibTableColumn
ciscoHealthMonitorPositiveEvents=_CiscoHealthMonitorPositiveEvents_Object((1,3,6,1,4,1,9,9,243,1,1,1,11),_CiscoHealthMonitorPositiveEvents_Type())
ciscoHealthMonitorPositiveEvents.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoHealthMonitorPositiveEvents.setStatus(_A)
_CiscoHealthMonitorMIBConform_ObjectIdentity=ObjectIdentity
ciscoHealthMonitorMIBConform=_CiscoHealthMonitorMIBConform_ObjectIdentity((1,3,6,1,4,1,9,9,243,2))
_CiscoHealthMonitorMIBCompliances_ObjectIdentity=ObjectIdentity
ciscoHealthMonitorMIBCompliances=_CiscoHealthMonitorMIBCompliances_ObjectIdentity((1,3,6,1,4,1,9,9,243,2,1))
_CiscoHealthMonitorMIBGroups_ObjectIdentity=ObjectIdentity
ciscoHealthMonitorMIBGroups=_CiscoHealthMonitorMIBGroups_ObjectIdentity((1,3,6,1,4,1,9,9,243,2,2))
ciscoHealthMonitorGroup=ObjectGroup((1,3,6,1,4,1,9,9,243,2,2,1))
ciscoHealthMonitorGroup.setObjects(*((_B,_G),(_B,_M),(_B,_N),(_B,_O),(_B,_P),(_B,_Q),(_B,_R),(_B,_S),(_B,_T),(_B,_U)))
if mibBuilder.loadTexts:ciscoHealthMonitorGroup.setStatus(_A)
ciscoHealthMonitorHealthLevel=NotificationType((1,3,6,1,4,1,9,9,243,0,1))
ciscoHealthMonitorHealthLevel.setObjects((_B,_G))
if mibBuilder.loadTexts:ciscoHealthMonitorHealthLevel.setStatus(_A)
ciscoHealthMonitorMIBNotificationGroup=NotificationGroup((1,3,6,1,4,1,9,9,243,2,2,2))
ciscoHealthMonitorMIBNotificationGroup.setObjects((_B,_V))
if mibBuilder.loadTexts:ciscoHealthMonitorMIBNotificationGroup.setStatus(_A)
ciscoHealthMonitorMIBCompliance=ModuleCompliance((1,3,6,1,4,1,9,9,243,2,1,1))
ciscoHealthMonitorMIBCompliance.setObjects((_B,_W))
if mibBuilder.loadTexts:ciscoHealthMonitorMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{_F:HealthLevel,'ciscoHealthMonitorMIB':ciscoHealthMonitorMIB,'ciscoHealthMonitorMIBNotifs':ciscoHealthMonitorMIBNotifs,_V:ciscoHealthMonitorHealthLevel,'ciscoHealthMonitorMIBObjects':ciscoHealthMonitorMIBObjects,'ciscoHealthMonitorTable':ciscoHealthMonitorTable,'ciscoHealthMonitorEntry':ciscoHealthMonitorEntry,_L:ciscoHealthMonitorSubsysName,_G:ciscoHealthMonitorHealth,_M:ciscoHealthMonitorHealthNotifyEnable,_N:ciscoHealthMonitorHealthNotifyHighThreshold,_O:ciscoHealthMonitorHealthNotifyLowThreshold,_P:ciscoHealthMonitorCatastrophicFaults,_Q:ciscoHealthMonitorCriticalFaults,_R:ciscoHealthMonitorHighSeverityFaults,_S:ciscoHealthMonitorMediumSeverityFaults,_T:ciscoHealthMonitorLowSeverityFaults,_U:ciscoHealthMonitorPositiveEvents,'ciscoHealthMonitorMIBConform':ciscoHealthMonitorMIBConform,'ciscoHealthMonitorMIBCompliances':ciscoHealthMonitorMIBCompliances,'ciscoHealthMonitorMIBCompliance':ciscoHealthMonitorMIBCompliance,'ciscoHealthMonitorMIBGroups':ciscoHealthMonitorMIBGroups,_W:ciscoHealthMonitorGroup,'ciscoHealthMonitorMIBNotificationGroup':ciscoHealthMonitorMIBNotificationGroup})