#
# PySNMP MIB module FS-CAPWAP-MULTICAST6-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/fscom/FS-CAPWAP-MULTICAST6-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 09:58:36 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
fsMgmt, = mibBuilder.importSymbols("FS-SMI", "fsMgmt")
InetAddress, = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddress")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
fsCapwapMulticast6MIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 85))
fsCapwapMulticast6MIB.setRevisions(('2010-05-20 00:00',))
if mibBuilder.loadTexts: fsCapwapMulticast6MIB.setLastUpdated('201005200000Z')
if mibBuilder.loadTexts: fsCapwapMulticast6MIB.setOrganization('FS.COM Inc..')
fsCapwapMulticast6MIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 85, 1))
fsCapwapMulticast6WorkingMode = MibScalar((1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 85, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("disabled", 1), ("unicast", 2), ("multicast", 3))).clone('disabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: fsCapwapMulticast6WorkingMode.setStatus('current')
fsCapwapMulticast6Group = MibScalar((1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 85, 1, 2), InetAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: fsCapwapMulticast6Group.setStatus('current')
fsCapwapMulticast6MIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 85, 2))
fsCapwapMulticast6MIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 85, 2, 1))
fsCapwapMulticast6MIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 85, 2, 2))
fsCapwapMulticast6MIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 85, 2, 1, 1)).setObjects(("FS-CAPWAP-MULTICAST6-MIB", "fsCapwapMulticast6MIBGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    fsCapwapMulticast6MIBCompliance = fsCapwapMulticast6MIBCompliance.setStatus('current')
fsCapwapMulticast6MIBGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 85, 2, 2, 1)).setObjects(("FS-CAPWAP-MULTICAST6-MIB", "fsCapwapMulticast6WorkingMode"), ("FS-CAPWAP-MULTICAST6-MIB", "fsCapwapMulticast6Group"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    fsCapwapMulticast6MIBGroup = fsCapwapMulticast6MIBGroup.setStatus('current')
mibBuilder.exportSymbols("FS-CAPWAP-MULTICAST6-MIB", fsCapwapMulticast6Group=fsCapwapMulticast6Group, fsCapwapMulticast6WorkingMode=fsCapwapMulticast6WorkingMode, fsCapwapMulticast6MIBGroups=fsCapwapMulticast6MIBGroups, fsCapwapMulticast6MIBCompliance=fsCapwapMulticast6MIBCompliance, fsCapwapMulticast6MIB=fsCapwapMulticast6MIB, fsCapwapMulticast6MIBConformance=fsCapwapMulticast6MIBConformance, fsCapwapMulticast6MIBObjects=fsCapwapMulticast6MIBObjects, fsCapwapMulticast6MIBCompliances=fsCapwapMulticast6MIBCompliances, fsCapwapMulticast6MIBGroup=fsCapwapMulticast6MIBGroup, PYSNMP_MODULE_ID=fsCapwapMulticast6MIB)
