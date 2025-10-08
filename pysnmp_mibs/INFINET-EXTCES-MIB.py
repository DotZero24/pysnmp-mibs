#
# PySNMP MIB module INFINET-EXTCES-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/infinet/INFINET-EXTCES-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:07:53 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
externalDevices, = mibBuilder.importSymbols("INFINET-EXTDEVICES-MIB", "externalDevices")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ModuleIdentity, Counter64, Unsigned32, Gauge32, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Unsigned32", "Gauge32", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
cesOverWlan = ModuleIdentity((1, 3, 6, 1, 4, 1, 3942, 2, 1))
cesOverWlan.setRevisions(('2007-06-18 19:10',))
if mibBuilder.loadTexts: cesOverWlan.setLastUpdated('200706181910Z')
if mibBuilder.loadTexts: cesOverWlan.setOrganization('Infinet Wireless Ltd.')
cesOverWlanUnit0 = MibIdentifier((1, 3, 6, 1, 4, 1, 3942, 2, 1, 1))
cesOverWlanUnit0Settings = MibIdentifier((1, 3, 6, 1, 4, 1, 3942, 2, 1, 1, 1))
cesOverWlanUnit0Enabled = MibScalar((1, 3, 6, 1, 4, 1, 3942, 2, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("on", 1), ("off", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cesOverWlanUnit0Enabled.setStatus('current')
cesOverWlanUnit0Mode = MibScalar((1, 3, 6, 1, 4, 1, 3942, 2, 1, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 2, 3, 4, 6, 8, 9, 10))).clone(namedValues=NamedValues(("e1-internal", 0), ("e1-loopback", 2), ("e1-recovery", 3), ("e1-line", 4), ("t1-internal", 6), ("t1-loopback", 8), ("t1-recovery", 9), ("t1-line", 10)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cesOverWlanUnit0Mode.setStatus('current')
cesOverWlanUnit0MaxJitter = MibScalar((1, 3, 6, 1, 4, 1, 3942, 2, 1, 1, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 200))).setUnits('milliseconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: cesOverWlanUnit0MaxJitter.setStatus('current')
cesOverWlanUnit0FramesPerPacket = MibScalar((1, 3, 6, 1, 4, 1, 3942, 2, 1, 1, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 32))).setUnits('frames').setMaxAccess("readwrite")
if mibBuilder.loadTexts: cesOverWlanUnit0FramesPerPacket.setStatus('current')
cesOverWlanUnit0BandwithLimit = MibScalar((1, 3, 6, 1, 4, 1, 3942, 2, 1, 1, 1, 5), Unsigned32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cesOverWlanUnit0BandwithLimit.setStatus('current')
cesOverWlanUnit0PortMap = MibScalar((1, 3, 6, 1, 4, 1, 3942, 2, 1, 1, 1, 6), Unsigned32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cesOverWlanUnit0PortMap.setStatus('current')
cesOverWlanMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 3942, 2, 1, 2))
cesOverWlanGroups = ObjectGroup((1, 3, 6, 1, 4, 1, 3942, 2, 1, 2, 1)).setObjects(("INFINET-EXTCES-MIB", "cesOverWlanUnit0Enabled"), ("INFINET-EXTCES-MIB", "cesOverWlanUnit0Mode"), ("INFINET-EXTCES-MIB", "cesOverWlanUnit0MaxJitter"), ("INFINET-EXTCES-MIB", "cesOverWlanUnit0FramesPerPacket"), ("INFINET-EXTCES-MIB", "cesOverWlanUnit0BandwithLimit"), ("INFINET-EXTCES-MIB", "cesOverWlanUnit0PortMap"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cesOverWlanGroups = cesOverWlanGroups.setStatus('current')
mibBuilder.exportSymbols("INFINET-EXTCES-MIB", cesOverWlanUnit0Enabled=cesOverWlanUnit0Enabled, cesOverWlanUnit0Mode=cesOverWlanUnit0Mode, cesOverWlanUnit0MaxJitter=cesOverWlanUnit0MaxJitter, cesOverWlanUnit0Settings=cesOverWlanUnit0Settings, cesOverWlanUnit0=cesOverWlanUnit0, cesOverWlanMIBConformance=cesOverWlanMIBConformance, cesOverWlan=cesOverWlan, cesOverWlanUnit0BandwithLimit=cesOverWlanUnit0BandwithLimit, cesOverWlanUnit0FramesPerPacket=cesOverWlanUnit0FramesPerPacket, cesOverWlanGroups=cesOverWlanGroups, PYSNMP_MODULE_ID=cesOverWlan, cesOverWlanUnit0PortMap=cesOverWlanUnit0PortMap)
