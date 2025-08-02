_J='snmpTsmGroup'
_I='snmpTsmConfigurationUsePrefix'
_H='snmpTsmInvalidPrefixes'
_G='snmpTsmUnknownPrefixes'
_F='snmpTsmInadequateSecurityLevels'
_E='snmpTsmInvalidCaches'
_D='TruthValue'
_C='read-only'
_B='SNMP-TSM-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso,mib_2=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso','mib-2')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention',_D)
snmpTsmMIB=ModuleIdentity((1,3,6,1,2,1,190))
if mibBuilder.loadTexts:snmpTsmMIB.setRevisions(('2009-06-09 00:00',))
_SnmpTsmNotifications_ObjectIdentity=ObjectIdentity
snmpTsmNotifications=_SnmpTsmNotifications_ObjectIdentity((1,3,6,1,2,1,190,0))
_SnmpTsmMIBObjects_ObjectIdentity=ObjectIdentity
snmpTsmMIBObjects=_SnmpTsmMIBObjects_ObjectIdentity((1,3,6,1,2,1,190,1))
_SnmpTsmStats_ObjectIdentity=ObjectIdentity
snmpTsmStats=_SnmpTsmStats_ObjectIdentity((1,3,6,1,2,1,190,1,1))
_SnmpTsmInvalidCaches_Type=Counter32
_SnmpTsmInvalidCaches_Object=MibScalar
snmpTsmInvalidCaches=_SnmpTsmInvalidCaches_Object((1,3,6,1,2,1,190,1,1,1),_SnmpTsmInvalidCaches_Type())
snmpTsmInvalidCaches.setMaxAccess(_C)
if mibBuilder.loadTexts:snmpTsmInvalidCaches.setStatus(_A)
_SnmpTsmInadequateSecurityLevels_Type=Counter32
_SnmpTsmInadequateSecurityLevels_Object=MibScalar
snmpTsmInadequateSecurityLevels=_SnmpTsmInadequateSecurityLevels_Object((1,3,6,1,2,1,190,1,1,2),_SnmpTsmInadequateSecurityLevels_Type())
snmpTsmInadequateSecurityLevels.setMaxAccess(_C)
if mibBuilder.loadTexts:snmpTsmInadequateSecurityLevels.setStatus(_A)
_SnmpTsmUnknownPrefixes_Type=Counter32
_SnmpTsmUnknownPrefixes_Object=MibScalar
snmpTsmUnknownPrefixes=_SnmpTsmUnknownPrefixes_Object((1,3,6,1,2,1,190,1,1,3),_SnmpTsmUnknownPrefixes_Type())
snmpTsmUnknownPrefixes.setMaxAccess(_C)
if mibBuilder.loadTexts:snmpTsmUnknownPrefixes.setStatus(_A)
_SnmpTsmInvalidPrefixes_Type=Counter32
_SnmpTsmInvalidPrefixes_Object=MibScalar
snmpTsmInvalidPrefixes=_SnmpTsmInvalidPrefixes_Object((1,3,6,1,2,1,190,1,1,4),_SnmpTsmInvalidPrefixes_Type())
snmpTsmInvalidPrefixes.setMaxAccess(_C)
if mibBuilder.loadTexts:snmpTsmInvalidPrefixes.setStatus(_A)
_SnmpTsmConfiguration_ObjectIdentity=ObjectIdentity
snmpTsmConfiguration=_SnmpTsmConfiguration_ObjectIdentity((1,3,6,1,2,1,190,1,2))
class _SnmpTsmConfigurationUsePrefix_Type(TruthValue):defaultValue=2
_SnmpTsmConfigurationUsePrefix_Type.__name__=_D
_SnmpTsmConfigurationUsePrefix_Object=MibScalar
snmpTsmConfigurationUsePrefix=_SnmpTsmConfigurationUsePrefix_Object((1,3,6,1,2,1,190,1,2,1),_SnmpTsmConfigurationUsePrefix_Type())
snmpTsmConfigurationUsePrefix.setMaxAccess('read-write')
if mibBuilder.loadTexts:snmpTsmConfigurationUsePrefix.setStatus(_A)
_SnmpTsmConformance_ObjectIdentity=ObjectIdentity
snmpTsmConformance=_SnmpTsmConformance_ObjectIdentity((1,3,6,1,2,1,190,2))
_SnmpTsmCompliances_ObjectIdentity=ObjectIdentity
snmpTsmCompliances=_SnmpTsmCompliances_ObjectIdentity((1,3,6,1,2,1,190,2,1))
_SnmpTsmGroups_ObjectIdentity=ObjectIdentity
snmpTsmGroups=_SnmpTsmGroups_ObjectIdentity((1,3,6,1,2,1,190,2,2))
snmpTsmGroup=ObjectGroup((1,3,6,1,2,1,190,2,2,2))
snmpTsmGroup.setObjects(*((_B,_E),(_B,_F),(_B,_G),(_B,_H),(_B,_I)))
if mibBuilder.loadTexts:snmpTsmGroup.setStatus(_A)
snmpTsmCompliance=ModuleCompliance((1,3,6,1,2,1,190,2,1,1))
snmpTsmCompliance.setObjects((_B,_J))
if mibBuilder.loadTexts:snmpTsmCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'snmpTsmMIB':snmpTsmMIB,'snmpTsmNotifications':snmpTsmNotifications,'snmpTsmMIBObjects':snmpTsmMIBObjects,'snmpTsmStats':snmpTsmStats,_E:snmpTsmInvalidCaches,_F:snmpTsmInadequateSecurityLevels,_G:snmpTsmUnknownPrefixes,_H:snmpTsmInvalidPrefixes,'snmpTsmConfiguration':snmpTsmConfiguration,_I:snmpTsmConfigurationUsePrefix,'snmpTsmConformance':snmpTsmConformance,'snmpTsmCompliances':snmpTsmCompliances,'snmpTsmCompliance':snmpTsmCompliance,'snmpTsmGroups':snmpTsmGroups,_J:snmpTsmGroup})