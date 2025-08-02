_D='oacEventsGeneralGroup'
_C='oacEventText'
_B='ONEACCESS-EVENTS-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
oacExpIMEvents,oacMIBModules,oneAccess=mibBuilder.importSymbols('ONEACCESS-GLOBAL-REG','oacExpIMEvents','oacMIBModules','oneAccess')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
oacEventsMIBModule=ModuleIdentity((1,3,6,1,4,1,13191,1,100,6600))
if mibBuilder.loadTexts:oacEventsMIBModule.setRevisions(('2011-06-15 00:00',))
_OacEventsObjects_ObjectIdentity=ObjectIdentity
oacEventsObjects=_OacEventsObjects_ObjectIdentity((1,3,6,1,4,1,13191,10,3,4,2,1))
_OacEventText_Type=DisplayString
_OacEventText_Object=MibScalar
oacEventText=_OacEventText_Object((1,3,6,1,4,1,13191,10,3,4,2,1,1),_OacEventText_Type())
oacEventText.setMaxAccess('read-only')
if mibBuilder.loadTexts:oacEventText.setStatus(_A)
_OacEventSeverityLevel_Type=ObjectIdentifier
_OacEventSeverityLevel_Object=MibScalar
oacEventSeverityLevel=_OacEventSeverityLevel_Object((1,3,6,1,4,1,13191,10,3,4,2,1,2),_OacEventSeverityLevel_Type())
oacEventSeverityLevel.setMaxAccess('accessible-for-notify')
if mibBuilder.loadTexts:oacEventSeverityLevel.setStatus(_A)
_OacEventSeverity_ObjectIdentity=ObjectIdentity
oacEventSeverity=_OacEventSeverity_ObjectIdentity((1,3,6,1,4,1,13191,10,3,4,2,1,3))
_OacEventSeverityAlerts_ObjectIdentity=ObjectIdentity
oacEventSeverityAlerts=_OacEventSeverityAlerts_ObjectIdentity((1,3,6,1,4,1,13191,10,3,4,2,1,3,1))
_OacEventSeverityCritical_ObjectIdentity=ObjectIdentity
oacEventSeverityCritical=_OacEventSeverityCritical_ObjectIdentity((1,3,6,1,4,1,13191,10,3,4,2,1,3,2))
_OacEventSeverityErrors_ObjectIdentity=ObjectIdentity
oacEventSeverityErrors=_OacEventSeverityErrors_ObjectIdentity((1,3,6,1,4,1,13191,10,3,4,2,1,3,3))
_OacEventSeverityWarnings_ObjectIdentity=ObjectIdentity
oacEventSeverityWarnings=_OacEventSeverityWarnings_ObjectIdentity((1,3,6,1,4,1,13191,10,3,4,2,1,3,4))
_OacEventSeverityNotifications_ObjectIdentity=ObjectIdentity
oacEventSeverityNotifications=_OacEventSeverityNotifications_ObjectIdentity((1,3,6,1,4,1,13191,10,3,4,2,1,3,5))
_OacEventSeverityInformational_ObjectIdentity=ObjectIdentity
oacEventSeverityInformational=_OacEventSeverityInformational_ObjectIdentity((1,3,6,1,4,1,13191,10,3,4,2,1,3,6))
_OacEventSeverityDebug_ObjectIdentity=ObjectIdentity
oacEventSeverityDebug=_OacEventSeverityDebug_ObjectIdentity((1,3,6,1,4,1,13191,10,3,4,2,1,3,7))
_OacEventsNotifications_ObjectIdentity=ObjectIdentity
oacEventsNotifications=_OacEventsNotifications_ObjectIdentity((1,3,6,1,4,1,13191,10,3,4,2,2))
_OacEventsConformance_ObjectIdentity=ObjectIdentity
oacEventsConformance=_OacEventsConformance_ObjectIdentity((1,3,6,1,4,1,13191,10,3,4,2,3))
_OacEventsGroups_ObjectIdentity=ObjectIdentity
oacEventsGroups=_OacEventsGroups_ObjectIdentity((1,3,6,1,4,1,13191,10,3,4,2,3,1))
_OacEventsCompliances_ObjectIdentity=ObjectIdentity
oacEventsCompliances=_OacEventsCompliances_ObjectIdentity((1,3,6,1,4,1,13191,10,3,4,2,3,2))
oacEventsGeneralGroup=ObjectGroup((1,3,6,1,4,1,13191,10,3,4,2,3,1,1))
oacEventsGeneralGroup.setObjects((_B,_C))
if mibBuilder.loadTexts:oacEventsGeneralGroup.setStatus(_A)
oacEvent=NotificationType((1,3,6,1,4,1,13191,0,1))
oacEvent.setObjects((_B,_C))
if mibBuilder.loadTexts:oacEvent.setStatus('')
oacEventsCompliance=ModuleCompliance((1,3,6,1,4,1,13191,10,3,4,2,3,2,1))
oacEventsCompliance.setObjects((_B,_D))
if mibBuilder.loadTexts:oacEventsCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'oacEvent':oacEvent,'oacEventsMIBModule':oacEventsMIBModule,'oacEventsObjects':oacEventsObjects,_C:oacEventText,'oacEventSeverityLevel':oacEventSeverityLevel,'oacEventSeverity':oacEventSeverity,'oacEventSeverityAlerts':oacEventSeverityAlerts,'oacEventSeverityCritical':oacEventSeverityCritical,'oacEventSeverityErrors':oacEventSeverityErrors,'oacEventSeverityWarnings':oacEventSeverityWarnings,'oacEventSeverityNotifications':oacEventSeverityNotifications,'oacEventSeverityInformational':oacEventSeverityInformational,'oacEventSeverityDebug':oacEventSeverityDebug,'oacEventsNotifications':oacEventsNotifications,'oacEventsConformance':oacEventsConformance,'oacEventsGroups':oacEventsGroups,_D:oacEventsGeneralGroup,'oacEventsCompliances':oacEventsCompliances,'oacEventsCompliance':oacEventsCompliance})