#
# PySNMP MIB module ENTERASYS-AUTO-TRACKING-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/enterasys/ENTERASYS-AUTO-TRACKING-MIB
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
etsysAutoTrackingMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 5624, 1, 2, 92))
etsysAutoTrackingMIB.setRevisions(('2013-02-12 16:56', '2013-02-11 15:57', '2013-01-22 15:32',))
if mibBuilder.loadTexts: etsysAutoTrackingMIB.setLastUpdated('201302121656Z')
if mibBuilder.loadTexts: etsysAutoTrackingMIB.setOrganization('Enterasys Networks, Inc')
etsysAutoTrackingBody = MibIdentifier((1, 3, 6, 1, 4, 1, 5624, 1, 2, 92, 2))
etsysAutoTrackingObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 5624, 1, 2, 92, 2, 1))
etsysAutoTrackingSystem = MibIdentifier((1, 3, 6, 1, 4, 1, 5624, 1, 2, 92, 2, 1, 1))
etsysAutoTrackingPort = MibIdentifier((1, 3, 6, 1, 4, 1, 5624, 1, 2, 92, 2, 1, 2))
etsysAutoTrackingSystemEnable = MibScalar((1, 3, 6, 1, 4, 1, 5624, 1, 2, 92, 2, 1, 1, 1), EnabledStatus().clone('disabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: etsysAutoTrackingSystemEnable.setStatus('current')
etsysAutoTrackingSystemAccountEnable = MibScalar((1, 3, 6, 1, 4, 1, 5624, 1, 2, 92, 2, 1, 1, 2), EnabledStatus().clone('disabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: etsysAutoTrackingSystemAccountEnable.setStatus('current')
etsysAutoTrackingPortTable = MibTable((1, 3, 6, 1, 4, 1, 5624, 1, 2, 92, 2, 1, 2, 1), )
if mibBuilder.loadTexts: etsysAutoTrackingPortTable.setStatus('current')
etsysAutoTrackingPortEntry = MibTableRow((1, 3, 6, 1, 4, 1, 5624, 1, 2, 92, 2, 1, 2, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: etsysAutoTrackingPortEntry.setStatus('current')
etsysAutoTrackingPortEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 5624, 1, 2, 92, 2, 1, 2, 1, 1, 1), EnabledStatus().clone('disabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: etsysAutoTrackingPortEnable.setStatus('current')
etsysAutoTrackingPortAuthenticationsAllowed = MibTableColumn((1, 3, 6, 1, 4, 1, 5624, 1, 2, 92, 2, 1, 2, 1, 1, 2), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: etsysAutoTrackingPortAuthenticationsAllowed.setStatus('current')
etsysAutoTrackingPortAuthenticationsAllocated = MibTableColumn((1, 3, 6, 1, 4, 1, 5624, 1, 2, 92, 2, 1, 2, 1, 1, 3), Unsigned32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: etsysAutoTrackingPortAuthenticationsAllocated.setStatus('current')
etsysAutoTrackingPortSessionTimeout = MibTableColumn((1, 3, 6, 1, 4, 1, 5624, 1, 2, 92, 2, 1, 2, 1, 1, 4), Unsigned32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(0, 0), ValueRangeConstraint(1, 65535), ))).setUnits('seconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: etsysAutoTrackingPortSessionTimeout.setStatus('current')
etsysAutoTrackingPortIdleTimeout = MibTableColumn((1, 3, 6, 1, 4, 1, 5624, 1, 2, 92, 2, 1, 2, 1, 1, 5), Unsigned32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(0, 0), ValueRangeConstraint(1, 65535), ))).setUnits('seconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: etsysAutoTrackingPortIdleTimeout.setStatus('current')
etsysAutoTrackingPortRadiusTimeoutProfileIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 5624, 1, 2, 92, 2, 1, 2, 1, 1, 6), Unsigned32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(0, 0), ValueRangeConstraint(1, 65535), ))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: etsysAutoTrackingPortRadiusTimeoutProfileIndex.setStatus('current')
etsysAutoTrackingPortRadiusRejectProfileIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 5624, 1, 2, 92, 2, 1, 2, 1, 1, 7), Unsigned32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(0, 0), ValueRangeConstraint(1, 65535), ))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: etsysAutoTrackingPortRadiusRejectProfileIndex.setStatus('current')
etsysAutoTrackingConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 5624, 1, 2, 92, 3))
etsysAutoTrackingGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 5624, 1, 2, 92, 3, 1))
etsysAutoTrackingCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 5624, 1, 2, 92, 3, 2))
etsysAutoTrackingSystemGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 5624, 1, 2, 92, 3, 1, 1)).setObjects(("ENTERASYS-AUTO-TRACKING-MIB", "etsysAutoTrackingSystemEnable"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    etsysAutoTrackingSystemGroup = etsysAutoTrackingSystemGroup.setStatus('deprecated')
etsysAutoTrackingPortGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 5624, 1, 2, 92, 3, 1, 2)).setObjects(("ENTERASYS-AUTO-TRACKING-MIB", "etsysAutoTrackingPortEnable"), ("ENTERASYS-AUTO-TRACKING-MIB", "etsysAutoTrackingPortAuthenticationsAllowed"), ("ENTERASYS-AUTO-TRACKING-MIB", "etsysAutoTrackingPortAuthenticationsAllocated"), ("ENTERASYS-AUTO-TRACKING-MIB", "etsysAutoTrackingPortSessionTimeout"), ("ENTERASYS-AUTO-TRACKING-MIB", "etsysAutoTrackingPortIdleTimeout"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    etsysAutoTrackingPortGroup = etsysAutoTrackingPortGroup.setStatus('deprecated')
etsysAutoTrackingSystemGroup2 = ObjectGroup((1, 3, 6, 1, 4, 1, 5624, 1, 2, 92, 3, 1, 3)).setObjects(("ENTERASYS-AUTO-TRACKING-MIB", "etsysAutoTrackingSystemEnable"), ("ENTERASYS-AUTO-TRACKING-MIB", "etsysAutoTrackingSystemAccountEnable"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    etsysAutoTrackingSystemGroup2 = etsysAutoTrackingSystemGroup2.setStatus('current')
etsysAutoTrackingPortGroup2 = ObjectGroup((1, 3, 6, 1, 4, 1, 5624, 1, 2, 92, 3, 1, 4)).setObjects(("ENTERASYS-AUTO-TRACKING-MIB", "etsysAutoTrackingPortEnable"), ("ENTERASYS-AUTO-TRACKING-MIB", "etsysAutoTrackingPortAuthenticationsAllowed"), ("ENTERASYS-AUTO-TRACKING-MIB", "etsysAutoTrackingPortAuthenticationsAllocated"), ("ENTERASYS-AUTO-TRACKING-MIB", "etsysAutoTrackingPortSessionTimeout"), ("ENTERASYS-AUTO-TRACKING-MIB", "etsysAutoTrackingPortIdleTimeout"), ("ENTERASYS-AUTO-TRACKING-MIB", "etsysAutoTrackingPortRadiusTimeoutProfileIndex"), ("ENTERASYS-AUTO-TRACKING-MIB", "etsysAutoTrackingPortRadiusRejectProfileIndex"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    etsysAutoTrackingPortGroup2 = etsysAutoTrackingPortGroup2.setStatus('current')
etsysAutoTrackingCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 5624, 1, 2, 92, 3, 2, 1)).setObjects(("ENTERASYS-AUTO-TRACKING-MIB", "etsysAutoTrackingSystemGroup"), ("ENTERASYS-AUTO-TRACKING-MIB", "etsysAutoTrackingPortGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    etsysAutoTrackingCompliance = etsysAutoTrackingCompliance.setStatus('deprecated')
etsysAutoTrackingCompliance2 = ModuleCompliance((1, 3, 6, 1, 4, 1, 5624, 1, 2, 92, 3, 2, 2)).setObjects(("ENTERASYS-AUTO-TRACKING-MIB", "etsysAutoTrackingSystemGroup2"), ("ENTERASYS-AUTO-TRACKING-MIB", "etsysAutoTrackingPortGroup2"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    etsysAutoTrackingCompliance2 = etsysAutoTrackingCompliance2.setStatus('current')
mibBuilder.exportSymbols("ENTERASYS-AUTO-TRACKING-MIB", PYSNMP_MODULE_ID=etsysAutoTrackingMIB, etsysAutoTrackingSystemGroup2=etsysAutoTrackingSystemGroup2, etsysAutoTrackingCompliance2=etsysAutoTrackingCompliance2, etsysAutoTrackingPortEntry=etsysAutoTrackingPortEntry, etsysAutoTrackingPortTable=etsysAutoTrackingPortTable, etsysAutoTrackingPortRadiusRejectProfileIndex=etsysAutoTrackingPortRadiusRejectProfileIndex, etsysAutoTrackingCompliance=etsysAutoTrackingCompliance, etsysAutoTrackingSystem=etsysAutoTrackingSystem, etsysAutoTrackingGroups=etsysAutoTrackingGroups, etsysAutoTrackingPortAuthenticationsAllocated=etsysAutoTrackingPortAuthenticationsAllocated, etsysAutoTrackingPortRadiusTimeoutProfileIndex=etsysAutoTrackingPortRadiusTimeoutProfileIndex, etsysAutoTrackingConformance=etsysAutoTrackingConformance, etsysAutoTrackingPortGroup2=etsysAutoTrackingPortGroup2, etsysAutoTrackingPortAuthenticationsAllowed=etsysAutoTrackingPortAuthenticationsAllowed, etsysAutoTrackingObjects=etsysAutoTrackingObjects, etsysAutoTrackingSystemEnable=etsysAutoTrackingSystemEnable, etsysAutoTrackingSystemGroup=etsysAutoTrackingSystemGroup, etsysAutoTrackingPortIdleTimeout=etsysAutoTrackingPortIdleTimeout, etsysAutoTrackingPortSessionTimeout=etsysAutoTrackingPortSessionTimeout, etsysAutoTrackingPortEnable=etsysAutoTrackingPortEnable, etsysAutoTrackingCompliances=etsysAutoTrackingCompliances, etsysAutoTrackingSystemAccountEnable=etsysAutoTrackingSystemAccountEnable, etsysAutoTrackingMIB=etsysAutoTrackingMIB, etsysAutoTrackingPort=etsysAutoTrackingPort, etsysAutoTrackingBody=etsysAutoTrackingBody, etsysAutoTrackingPortGroup=etsysAutoTrackingPortGroup)
