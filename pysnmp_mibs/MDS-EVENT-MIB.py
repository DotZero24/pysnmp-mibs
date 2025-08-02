_I='mdsEventVariablesCeeGroup'
_H='mdsEventNotificationsGroup'
_G='mdsEvent'
_F='mdsEventInfoInCee'
_E='mdsEventName'
_D='read-write'
_C='OctetString'
_B='MDS-EVENT-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_C,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
mdsLogging,=mibBuilder.importSymbols('MDS-ORBIT-SMI-MIB','mdsLogging')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
mdsEventMIB=ModuleIdentity((1,3,6,1,4,1,4130,10,4,1))
if mibBuilder.loadTexts:mdsEventMIB.setRevisions(('2018-05-16 00:00','2013-04-22 00:00'))
_MdsEventMIBObjects_ObjectIdentity=ObjectIdentity
mdsEventMIBObjects=_MdsEventMIBObjects_ObjectIdentity((1,3,6,1,4,1,4130,10,4,1,1))
_MdsEventVariables_ObjectIdentity=ObjectIdentity
mdsEventVariables=_MdsEventVariables_ObjectIdentity((1,3,6,1,4,1,4130,10,4,1,1,1))
class _MdsEventName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_MdsEventName_Type.__name__=_C
_MdsEventName_Object=MibScalar
mdsEventName=_MdsEventName_Object((1,3,6,1,4,1,4130,10,4,1,1,1,1),_MdsEventName_Type())
mdsEventName.setMaxAccess(_D)
if mibBuilder.loadTexts:mdsEventName.setStatus(_A)
class _MdsEventInfoInCee_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,65535))
_MdsEventInfoInCee_Type.__name__=_C
_MdsEventInfoInCee_Object=MibScalar
mdsEventInfoInCee=_MdsEventInfoInCee_Object((1,3,6,1,4,1,4130,10,4,1,1,1,2),_MdsEventInfoInCee_Type())
mdsEventInfoInCee.setMaxAccess(_D)
if mibBuilder.loadTexts:mdsEventInfoInCee.setStatus(_A)
_MdsEventMIBNotifications_ObjectIdentity=ObjectIdentity
mdsEventMIBNotifications=_MdsEventMIBNotifications_ObjectIdentity((1,3,6,1,4,1,4130,10,4,1,2))
_Traps0_ObjectIdentity=ObjectIdentity
traps0=_Traps0_ObjectIdentity((1,3,6,1,4,1,4130,10,4,1,2,1))
_Traps_ObjectIdentity=ObjectIdentity
traps=_Traps_ObjectIdentity((1,3,6,1,4,1,4130,10,4,1,2,1,0))
_MdsEventMIBConformance_ObjectIdentity=ObjectIdentity
mdsEventMIBConformance=_MdsEventMIBConformance_ObjectIdentity((1,3,6,1,4,1,4130,10,4,1,3))
_MdsEventMIBCompliances_ObjectIdentity=ObjectIdentity
mdsEventMIBCompliances=_MdsEventMIBCompliances_ObjectIdentity((1,3,6,1,4,1,4130,10,4,1,3,1))
_MdsEventMIBGroups_ObjectIdentity=ObjectIdentity
mdsEventMIBGroups=_MdsEventMIBGroups_ObjectIdentity((1,3,6,1,4,1,4130,10,4,1,3,2))
mdsEventVariablesCeeGroup=ObjectGroup((1,3,6,1,4,1,4130,10,4,1,3,2,2))
mdsEventVariablesCeeGroup.setObjects(*((_B,_E),(_B,_F)))
if mibBuilder.loadTexts:mdsEventVariablesCeeGroup.setStatus(_A)
mdsEvent=NotificationType((1,3,6,1,4,1,4130,10,4,1,2,1,0,1))
if mibBuilder.loadTexts:mdsEvent.setStatus(_A)
mdsEventNotificationsGroup=NotificationGroup((1,3,6,1,4,1,4130,10,4,1,3,2,1))
mdsEventNotificationsGroup.setObjects((_B,_G))
if mibBuilder.loadTexts:mdsEventNotificationsGroup.setStatus(_A)
mdsEventMIBCompliance=ModuleCompliance((1,3,6,1,4,1,4130,10,4,1,3,1,2))
mdsEventMIBCompliance.setObjects(*((_B,_H),(_B,_I)))
if mibBuilder.loadTexts:mdsEventMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'mdsEventMIB':mdsEventMIB,'mdsEventMIBObjects':mdsEventMIBObjects,'mdsEventVariables':mdsEventVariables,_E:mdsEventName,_F:mdsEventInfoInCee,'mdsEventMIBNotifications':mdsEventMIBNotifications,'traps0':traps0,'traps':traps,_G:mdsEvent,'mdsEventMIBConformance':mdsEventMIBConformance,'mdsEventMIBCompliances':mdsEventMIBCompliances,'mdsEventMIBCompliance':mdsEventMIBCompliance,'mdsEventMIBGroups':mdsEventMIBGroups,_H:mdsEventNotificationsGroup,_I:mdsEventVariablesCeeGroup})