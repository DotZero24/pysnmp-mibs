#
# PySNMP MIB module FS-CAPWAP-MULTICAST6-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/fscom/FS-CAPWAP-MULTICAST6-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:01:25 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
fsMgmt, = mibBuilder.importSymbols("FS-SMI", "fsMgmt")
InetAddress, = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddress")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
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
mibBuilder.exportSymbols("FS-CAPWAP-MULTICAST6-MIB", fsCapwapMulticast6MIB=fsCapwapMulticast6MIB, PYSNMP_MODULE_ID=fsCapwapMulticast6MIB, fsCapwapMulticast6MIBObjects=fsCapwapMulticast6MIBObjects, fsCapwapMulticast6MIBCompliances=fsCapwapMulticast6MIBCompliances, fsCapwapMulticast6WorkingMode=fsCapwapMulticast6WorkingMode, fsCapwapMulticast6MIBGroup=fsCapwapMulticast6MIBGroup, fsCapwapMulticast6MIBConformance=fsCapwapMulticast6MIBConformance, fsCapwapMulticast6MIBGroups=fsCapwapMulticast6MIBGroups, fsCapwapMulticast6Group=fsCapwapMulticast6Group, fsCapwapMulticast6MIBCompliance=fsCapwapMulticast6MIBCompliance)
