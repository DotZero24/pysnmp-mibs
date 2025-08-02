_I='PKTC-IETF-EVENT-MIB'
_H='pktcEventNotificationGroup'
_G='pktcEventGroup'
_F='PKTC-EVENT-MIB'
_E='pktcEUEMEMVersion'
_D='SnmpAdminString'
_C='pktcEUEMEMGroup'
_B='CL-PKTC-EUE-EVENT-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
pktcEUEMibs,=mibBuilder.importSymbols('CLAB-DEF-MIB','pktcEUEMibs')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB',_D)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
pktcEUEEventMIB=ModuleIdentity((1,3,6,1,4,1,4491,2,2,10,6))
if mibBuilder.loadTexts:pktcEUEEventMIB.setRevisions(('2012-10-30 00:00','2007-11-06 00:00'))
_PktcEUEEventNotifications_ObjectIdentity=ObjectIdentity
pktcEUEEventNotifications=_PktcEUEEventNotifications_ObjectIdentity((1,3,6,1,4,1,4491,2,2,10,6,0))
_PktcEUEEventObjects_ObjectIdentity=ObjectIdentity
pktcEUEEventObjects=_PktcEUEEventObjects_ObjectIdentity((1,3,6,1,4,1,4491,2,2,10,6,1))
class _PktcEUEMEMVersion_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,6))
_PktcEUEMEMVersion_Type.__name__=_D
_PktcEUEMEMVersion_Object=MibScalar
pktcEUEMEMVersion=_PktcEUEMEMVersion_Object((1,3,6,1,4,1,4491,2,2,10,6,1,1),_PktcEUEMEMVersion_Type())
pktcEUEMEMVersion.setMaxAccess('read-only')
if mibBuilder.loadTexts:pktcEUEMEMVersion.setStatus(_A)
_PktcEUEEventConformance_ObjectIdentity=ObjectIdentity
pktcEUEEventConformance=_PktcEUEEventConformance_ObjectIdentity((1,3,6,1,4,1,4491,2,2,10,6,2))
_PktcEUEEventCompliances_ObjectIdentity=ObjectIdentity
pktcEUEEventCompliances=_PktcEUEEventCompliances_ObjectIdentity((1,3,6,1,4,1,4491,2,2,10,6,2,1))
_PktcEUEEventGroups_ObjectIdentity=ObjectIdentity
pktcEUEEventGroups=_PktcEUEEventGroups_ObjectIdentity((1,3,6,1,4,1,4491,2,2,10,6,2,2))
pktcEUEMEMGroup=ObjectGroup((1,3,6,1,4,1,4491,2,2,10,6,2,2,1))
pktcEUEMEMGroup.setObjects((_B,_E))
if mibBuilder.loadTexts:pktcEUEMEMGroup.setStatus(_A)
pktcEUEEventCompliance=ModuleCompliance((1,3,6,1,4,1,4491,2,2,10,6,2,1,1))
pktcEUEEventCompliance.setObjects(*((_F,_G),(_F,_H),(_B,_C)))
if mibBuilder.loadTexts:pktcEUEEventCompliance.setStatus(_A)
pktcEUEEventEuroCompliance=ModuleCompliance((1,3,6,1,4,1,4491,2,2,10,6,2,1,2))
pktcEUEEventEuroCompliance.setObjects(*((_I,_G),(_I,_H),(_B,_C)))
if mibBuilder.loadTexts:pktcEUEEventEuroCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'pktcEUEEventMIB':pktcEUEEventMIB,'pktcEUEEventNotifications':pktcEUEEventNotifications,'pktcEUEEventObjects':pktcEUEEventObjects,_E:pktcEUEMEMVersion,'pktcEUEEventConformance':pktcEUEEventConformance,'pktcEUEEventCompliances':pktcEUEEventCompliances,'pktcEUEEventCompliance':pktcEUEEventCompliance,'pktcEUEEventEuroCompliance':pktcEUEEventEuroCompliance,'pktcEUEEventGroups':pktcEUEEventGroups,_C:pktcEUEMEMGroup})