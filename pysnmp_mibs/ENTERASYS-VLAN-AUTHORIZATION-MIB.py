#
# PySNMP MIB module ENTERASYS-VLAN-AUTHORIZATION-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/enterasys/ENTERASYS-VLAN-AUTHORIZATION-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:17:16 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
dot1dBasePort, = mibBuilder.importSymbols("BRIDGE-MIB", "dot1dBasePort")
etsysModules, = mibBuilder.importSymbols("ENTERASYS-MIB-NAMES", "etsysModules")
EnabledStatus, = mibBuilder.importSymbols("P-BRIDGE-MIB", "EnabledStatus")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
etsysVlanAuthorizationMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 5624, 1, 2, 48))
etsysVlanAuthorizationMIB.setRevisions(('2004-06-02 19:22',))
if mibBuilder.loadTexts: etsysVlanAuthorizationMIB.setLastUpdated('200406021922Z')
if mibBuilder.loadTexts: etsysVlanAuthorizationMIB.setOrganization('Enterasys Networks, Inc')
class VlanAuthEgressStatus(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("none", 1), ("tagged", 2), ("untagged", 3), ("dynamic", 4))

etsysVlanAuthorizationObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 5624, 1, 2, 48, 1))
etsysVlanAuthorizationSystem = MibIdentifier((1, 3, 6, 1, 4, 1, 5624, 1, 2, 48, 1, 1))
etsysVlanAuthorizationPorts = MibIdentifier((1, 3, 6, 1, 4, 1, 5624, 1, 2, 48, 1, 2))
etsysVlanAuthorizationEnable = MibScalar((1, 3, 6, 1, 4, 1, 5624, 1, 2, 48, 1, 1, 1), EnabledStatus().clone('disabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: etsysVlanAuthorizationEnable.setStatus('current')
etsysVlanAuthorizationTable = MibTable((1, 3, 6, 1, 4, 1, 5624, 1, 2, 48, 1, 2, 1), )
if mibBuilder.loadTexts: etsysVlanAuthorizationTable.setStatus('current')
etsysVlanAuthorizationEntry = MibTableRow((1, 3, 6, 1, 4, 1, 5624, 1, 2, 48, 1, 2, 1, 1), ).setIndexNames((0, "BRIDGE-MIB", "dot1dBasePort"))
if mibBuilder.loadTexts: etsysVlanAuthorizationEntry.setStatus('current')
etsysVlanAuthorizationStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 5624, 1, 2, 48, 1, 2, 1, 1, 1), EnabledStatus().clone('enabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: etsysVlanAuthorizationStatus.setStatus('current')
etsysVlanAuthorizationAdminEgress = MibTableColumn((1, 3, 6, 1, 4, 1, 5624, 1, 2, 48, 1, 2, 1, 1, 2), VlanAuthEgressStatus().clone('untagged')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: etsysVlanAuthorizationAdminEgress.setStatus('current')
etsysVlanAuthorizationOperEgress = MibTableColumn((1, 3, 6, 1, 4, 1, 5624, 1, 2, 48, 1, 2, 1, 1, 3), VlanAuthEgressStatus().clone('none')).setMaxAccess("readonly")
if mibBuilder.loadTexts: etsysVlanAuthorizationOperEgress.setStatus('current')
etsysVlanAuthorizationVlanID = MibTableColumn((1, 3, 6, 1, 4, 1, 5624, 1, 2, 48, 1, 2, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(0, 0), ValueRangeConstraint(1, 4094), ValueRangeConstraint(4095, 4095), ))).setMaxAccess("readonly")
if mibBuilder.loadTexts: etsysVlanAuthorizationVlanID.setStatus('current')
etsysVlanAuthorizationConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 5624, 1, 2, 48, 2))
etsysVlanAuthorizationGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 5624, 1, 2, 48, 2, 1))
etsysVlanAuthorizationCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 5624, 1, 2, 48, 2, 2))
etsysVlanAuthorizationGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 5624, 1, 2, 48, 2, 1, 1)).setObjects(("ENTERASYS-VLAN-AUTHORIZATION-MIB", "etsysVlanAuthorizationEnable"), ("ENTERASYS-VLAN-AUTHORIZATION-MIB", "etsysVlanAuthorizationStatus"), ("ENTERASYS-VLAN-AUTHORIZATION-MIB", "etsysVlanAuthorizationAdminEgress"), ("ENTERASYS-VLAN-AUTHORIZATION-MIB", "etsysVlanAuthorizationOperEgress"), ("ENTERASYS-VLAN-AUTHORIZATION-MIB", "etsysVlanAuthorizationVlanID"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    etsysVlanAuthorizationGroup = etsysVlanAuthorizationGroup.setStatus('current')
etsysVlanAuthorizationCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 5624, 1, 2, 48, 2, 2, 1)).setObjects(("ENTERASYS-VLAN-AUTHORIZATION-MIB", "etsysVlanAuthorizationGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    etsysVlanAuthorizationCompliance = etsysVlanAuthorizationCompliance.setStatus('current')
mibBuilder.exportSymbols("ENTERASYS-VLAN-AUTHORIZATION-MIB", etsysVlanAuthorizationGroups=etsysVlanAuthorizationGroups, etsysVlanAuthorizationVlanID=etsysVlanAuthorizationVlanID, etsysVlanAuthorizationAdminEgress=etsysVlanAuthorizationAdminEgress, etsysVlanAuthorizationStatus=etsysVlanAuthorizationStatus, etsysVlanAuthorizationMIB=etsysVlanAuthorizationMIB, VlanAuthEgressStatus=VlanAuthEgressStatus, etsysVlanAuthorizationConformance=etsysVlanAuthorizationConformance, etsysVlanAuthorizationPorts=etsysVlanAuthorizationPorts, etsysVlanAuthorizationObjects=etsysVlanAuthorizationObjects, etsysVlanAuthorizationEnable=etsysVlanAuthorizationEnable, etsysVlanAuthorizationTable=etsysVlanAuthorizationTable, etsysVlanAuthorizationOperEgress=etsysVlanAuthorizationOperEgress, etsysVlanAuthorizationEntry=etsysVlanAuthorizationEntry, etsysVlanAuthorizationSystem=etsysVlanAuthorizationSystem, etsysVlanAuthorizationCompliances=etsysVlanAuthorizationCompliances, etsysVlanAuthorizationGroup=etsysVlanAuthorizationGroup, etsysVlanAuthorizationCompliance=etsysVlanAuthorizationCompliance, PYSNMP_MODULE_ID=etsysVlanAuthorizationMIB)
