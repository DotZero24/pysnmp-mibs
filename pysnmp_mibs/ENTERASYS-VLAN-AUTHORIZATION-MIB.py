#
# PySNMP MIB module ENTERASYS-VLAN-AUTHORIZATION-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/enterasys/ENTERASYS-VLAN-AUTHORIZATION-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:33:47 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
dot1dBasePort, = mibBuilder.importSymbols("BRIDGE-MIB", "dot1dBasePort")
etsysModules, = mibBuilder.importSymbols("ENTERASYS-MIB-NAMES", "etsysModules")
EnabledStatus, = mibBuilder.importSymbols("P-BRIDGE-MIB", "EnabledStatus")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
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
mibBuilder.exportSymbols("ENTERASYS-VLAN-AUTHORIZATION-MIB", etsysVlanAuthorizationGroups=etsysVlanAuthorizationGroups, etsysVlanAuthorizationCompliance=etsysVlanAuthorizationCompliance, etsysVlanAuthorizationStatus=etsysVlanAuthorizationStatus, etsysVlanAuthorizationPorts=etsysVlanAuthorizationPorts, etsysVlanAuthorizationEnable=etsysVlanAuthorizationEnable, etsysVlanAuthorizationSystem=etsysVlanAuthorizationSystem, etsysVlanAuthorizationConformance=etsysVlanAuthorizationConformance, etsysVlanAuthorizationEntry=etsysVlanAuthorizationEntry, etsysVlanAuthorizationGroup=etsysVlanAuthorizationGroup, etsysVlanAuthorizationVlanID=etsysVlanAuthorizationVlanID, etsysVlanAuthorizationTable=etsysVlanAuthorizationTable, etsysVlanAuthorizationOperEgress=etsysVlanAuthorizationOperEgress, etsysVlanAuthorizationAdminEgress=etsysVlanAuthorizationAdminEgress, PYSNMP_MODULE_ID=etsysVlanAuthorizationMIB, etsysVlanAuthorizationMIB=etsysVlanAuthorizationMIB, etsysVlanAuthorizationObjects=etsysVlanAuthorizationObjects, etsysVlanAuthorizationCompliances=etsysVlanAuthorizationCompliances, VlanAuthEgressStatus=VlanAuthEgressStatus)
