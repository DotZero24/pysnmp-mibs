#
# PySNMP MIB module ENTERASYS-QUARANTINE-AGENT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/enterasys/ENTERASYS-QUARANTINE-AGENT-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:34:16 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
etsysModules, = mibBuilder.importSymbols("ENTERASYS-MIB-NAMES", "etsysModules")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
EnabledStatus, = mibBuilder.importSymbols("P-BRIDGE-MIB", "EnabledStatus")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
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
mibBuilder.exportSymbols("ENTERASYS-QUARANTINE-AGENT-MIB", etsysQuarantineAgentMIB=etsysQuarantineAgentMIB, etsysQuarantineAgentPortEntry=etsysQuarantineAgentPortEntry, etsysQuarantineAgentPortIdleTimeout=etsysQuarantineAgentPortIdleTimeout, etsysQuarantineAgentPortTable=etsysQuarantineAgentPortTable, etsysQuarantineAgentPortEnable=etsysQuarantineAgentPortEnable, etsysQuarantineAgentSystemEnable=etsysQuarantineAgentSystemEnable, etsysQuarantineAgentCompliance2=etsysQuarantineAgentCompliance2, etsysQuarantineAgentPortAuthenticationsAllowed=etsysQuarantineAgentPortAuthenticationsAllowed, etsysQuarantineAgentCompliances=etsysQuarantineAgentCompliances, etsysQuarantineAgentSystem=etsysQuarantineAgentSystem, etsysQuarantineAgentBody=etsysQuarantineAgentBody, PYSNMP_MODULE_ID=etsysQuarantineAgentMIB, etsysQuarantineAgentSystemAccountEnable=etsysQuarantineAgentSystemAccountEnable, etsysQuarantineAgentPort=etsysQuarantineAgentPort, etsysQuarantineAgentPortSessionTimeout=etsysQuarantineAgentPortSessionTimeout, etsysQuarantineAgentGroups=etsysQuarantineAgentGroups, etsysQuarantineAgentCompliance=etsysQuarantineAgentCompliance, etsysQuarantineAgentPortGroup=etsysQuarantineAgentPortGroup, etsysQuarantineAgentSystemGroup=etsysQuarantineAgentSystemGroup, etsysQuarantineAgentObjects=etsysQuarantineAgentObjects, etsysQuarantineAgentSystemGroup2=etsysQuarantineAgentSystemGroup2, etsysQuarantineAgentPortAuthenticationsAllocated=etsysQuarantineAgentPortAuthenticationsAllocated, etsysQuarantineAgentConformance=etsysQuarantineAgentConformance)
