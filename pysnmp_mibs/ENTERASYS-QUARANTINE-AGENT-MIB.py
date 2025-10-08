#
# PySNMP MIB module ENTERASYS-QUARANTINE-AGENT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/enterasys/ENTERASYS-QUARANTINE-AGENT-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:17:33 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
etsysModules, = mibBuilder.importSymbols("ENTERASYS-MIB-NAMES", "etsysModules")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
EnabledStatus, = mibBuilder.importSymbols("P-BRIDGE-MIB", "EnabledStatus")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ModuleIdentity, Counter64, Unsigned32, Gauge32, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Unsigned32", "Gauge32", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
etsysQuarantineAgentMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 5624, 1, 2, 93))
etsysQuarantineAgentMIB.setRevisions(('2013-02-11 18:57', '2013-02-11 15:57', '2013-01-22 15:32',))
if mibBuilder.loadTexts: etsysQuarantineAgentMIB.setLastUpdated('201302111857Z')
if mibBuilder.loadTexts: etsysQuarantineAgentMIB.setOrganization('Enterasys Networks, Inc')
etsysQuarantineAgentBody = MibIdentifier((1, 3, 6, 1, 4, 1, 5624, 1, 2, 93, 2))
etsysQuarantineAgentObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 5624, 1, 2, 93, 2, 1))
etsysQuarantineAgentSystem = MibIdentifier((1, 3, 6, 1, 4, 1, 5624, 1, 2, 93, 2, 1, 1))
etsysQuarantineAgentPort = MibIdentifier((1, 3, 6, 1, 4, 1, 5624, 1, 2, 93, 2, 1, 2))
etsysQuarantineAgentSystemEnable = MibScalar((1, 3, 6, 1, 4, 1, 5624, 1, 2, 93, 2, 1, 1, 1), EnabledStatus().clone('disabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: etsysQuarantineAgentSystemEnable.setStatus('current')
etsysQuarantineAgentSystemAccountEnable = MibScalar((1, 3, 6, 1, 4, 1, 5624, 1, 2, 93, 2, 1, 1, 2), EnabledStatus().clone('disabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: etsysQuarantineAgentSystemAccountEnable.setStatus('current')
etsysQuarantineAgentPortTable = MibTable((1, 3, 6, 1, 4, 1, 5624, 1, 2, 93, 2, 1, 2, 1), )
if mibBuilder.loadTexts: etsysQuarantineAgentPortTable.setStatus('current')
etsysQuarantineAgentPortEntry = MibTableRow((1, 3, 6, 1, 4, 1, 5624, 1, 2, 93, 2, 1, 2, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: etsysQuarantineAgentPortEntry.setStatus('current')
etsysQuarantineAgentPortEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 5624, 1, 2, 93, 2, 1, 2, 1, 1, 2), EnabledStatus().clone('disabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: etsysQuarantineAgentPortEnable.setStatus('current')
etsysQuarantineAgentPortAuthenticationsAllowed = MibTableColumn((1, 3, 6, 1, 4, 1, 5624, 1, 2, 93, 2, 1, 2, 1, 1, 3), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: etsysQuarantineAgentPortAuthenticationsAllowed.setStatus('current')
etsysQuarantineAgentPortAuthenticationsAllocated = MibTableColumn((1, 3, 6, 1, 4, 1, 5624, 1, 2, 93, 2, 1, 2, 1, 1, 4), Unsigned32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: etsysQuarantineAgentPortAuthenticationsAllocated.setStatus('current')
etsysQuarantineAgentPortSessionTimeout = MibTableColumn((1, 3, 6, 1, 4, 1, 5624, 1, 2, 93, 2, 1, 2, 1, 1, 5), Unsigned32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(0, 0), ValueRangeConstraint(1, 65535), ))).setUnits('seconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: etsysQuarantineAgentPortSessionTimeout.setStatus('current')
etsysQuarantineAgentPortIdleTimeout = MibTableColumn((1, 3, 6, 1, 4, 1, 5624, 1, 2, 93, 2, 1, 2, 1, 1, 6), Unsigned32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(0, 0), ValueRangeConstraint(1, 65535), ))).setUnits('seconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: etsysQuarantineAgentPortIdleTimeout.setStatus('current')
etsysQuarantineAgentConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 5624, 1, 2, 93, 3))
etsysQuarantineAgentGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 5624, 1, 2, 93, 3, 1))
etsysQuarantineAgentCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 5624, 1, 2, 93, 3, 2))
etsysQuarantineAgentSystemGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 5624, 1, 2, 93, 3, 1, 1)).setObjects(("ENTERASYS-QUARANTINE-AGENT-MIB", "etsysQuarantineAgentSystemEnable"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    etsysQuarantineAgentSystemGroup = etsysQuarantineAgentSystemGroup.setStatus('deprecated')
etsysQuarantineAgentPortGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 5624, 1, 2, 93, 3, 1, 2)).setObjects(("ENTERASYS-QUARANTINE-AGENT-MIB", "etsysQuarantineAgentPortEnable"), ("ENTERASYS-QUARANTINE-AGENT-MIB", "etsysQuarantineAgentPortAuthenticationsAllowed"), ("ENTERASYS-QUARANTINE-AGENT-MIB", "etsysQuarantineAgentPortAuthenticationsAllocated"), ("ENTERASYS-QUARANTINE-AGENT-MIB", "etsysQuarantineAgentPortSessionTimeout"), ("ENTERASYS-QUARANTINE-AGENT-MIB", "etsysQuarantineAgentPortIdleTimeout"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    etsysQuarantineAgentPortGroup = etsysQuarantineAgentPortGroup.setStatus('current')
etsysQuarantineAgentSystemGroup2 = ObjectGroup((1, 3, 6, 1, 4, 1, 5624, 1, 2, 93, 3, 1, 3)).setObjects(("ENTERASYS-QUARANTINE-AGENT-MIB", "etsysQuarantineAgentSystemEnable"), ("ENTERASYS-QUARANTINE-AGENT-MIB", "etsysQuarantineAgentSystemAccountEnable"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    etsysQuarantineAgentSystemGroup2 = etsysQuarantineAgentSystemGroup2.setStatus('current')
etsysQuarantineAgentCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 5624, 1, 2, 93, 3, 2, 1)).setObjects(("ENTERASYS-QUARANTINE-AGENT-MIB", "etsysQuarantineAgentSystemGroup"), ("ENTERASYS-QUARANTINE-AGENT-MIB", "etsysQuarantineAgentPortGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    etsysQuarantineAgentCompliance = etsysQuarantineAgentCompliance.setStatus('deprecated')
etsysQuarantineAgentCompliance2 = ModuleCompliance((1, 3, 6, 1, 4, 1, 5624, 1, 2, 93, 3, 2, 2)).setObjects(("ENTERASYS-QUARANTINE-AGENT-MIB", "etsysQuarantineAgentSystemGroup2"), ("ENTERASYS-QUARANTINE-AGENT-MIB", "etsysQuarantineAgentPortGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    etsysQuarantineAgentCompliance2 = etsysQuarantineAgentCompliance2.setStatus('current')
mibBuilder.exportSymbols("ENTERASYS-QUARANTINE-AGENT-MIB", etsysQuarantineAgentPortSessionTimeout=etsysQuarantineAgentPortSessionTimeout, etsysQuarantineAgentCompliance2=etsysQuarantineAgentCompliance2, etsysQuarantineAgentSystemAccountEnable=etsysQuarantineAgentSystemAccountEnable, etsysQuarantineAgentSystemGroup=etsysQuarantineAgentSystemGroup, etsysQuarantineAgentPortAuthenticationsAllocated=etsysQuarantineAgentPortAuthenticationsAllocated, etsysQuarantineAgentPortTable=etsysQuarantineAgentPortTable, etsysQuarantineAgentObjects=etsysQuarantineAgentObjects, etsysQuarantineAgentSystem=etsysQuarantineAgentSystem, PYSNMP_MODULE_ID=etsysQuarantineAgentMIB, etsysQuarantineAgentBody=etsysQuarantineAgentBody, etsysQuarantineAgentPortEntry=etsysQuarantineAgentPortEntry, etsysQuarantineAgentPortGroup=etsysQuarantineAgentPortGroup, etsysQuarantineAgentSystemGroup2=etsysQuarantineAgentSystemGroup2, etsysQuarantineAgentCompliance=etsysQuarantineAgentCompliance, etsysQuarantineAgentCompliances=etsysQuarantineAgentCompliances, etsysQuarantineAgentGroups=etsysQuarantineAgentGroups, etsysQuarantineAgentPortAuthenticationsAllowed=etsysQuarantineAgentPortAuthenticationsAllowed, etsysQuarantineAgentPortEnable=etsysQuarantineAgentPortEnable, etsysQuarantineAgentConformance=etsysQuarantineAgentConformance, etsysQuarantineAgentSystemEnable=etsysQuarantineAgentSystemEnable, etsysQuarantineAgentMIB=etsysQuarantineAgentMIB, etsysQuarantineAgentPort=etsysQuarantineAgentPort, etsysQuarantineAgentPortIdleTimeout=etsysQuarantineAgentPortIdleTimeout)
