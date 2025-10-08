#
# PySNMP MIB module FS-CAPWAP-MULTICAST-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/fscom/FS-CAPWAP-MULTICAST-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 09:58:44 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
fsMgmt, = mibBuilder.importSymbols("FS-SMI", "fsMgmt")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
fsCapwapMulticastMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 59))
fsCapwapMulticastMIB.setRevisions(('2009-10-22 00:00',))
if mibBuilder.loadTexts: fsCapwapMulticastMIB.setLastUpdated('200910220000Z')
if mibBuilder.loadTexts: fsCapwapMulticastMIB.setOrganization('FS.COM Inc..')
fsCapwapMulticastMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 59, 1))
fsCapwapMulticastWorkingMode = MibScalar((1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 59, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("unicast", 1), ("multicast", 2))).clone('unicast')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: fsCapwapMulticastWorkingMode.setStatus('current')
fsCapwapMulticastGroup = MibScalar((1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 59, 1, 2), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: fsCapwapMulticastGroup.setStatus('current')
fsCapwapMulticastMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 59, 2))
fsCapwapMulticastMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 59, 2, 1))
fsCapwapMulticastMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 59, 2, 2))
fsCapwapMulticastMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 59, 2, 1, 1)).setObjects(("FS-CAPWAP-MULTICAST-MIB", "fsCapwapMulticastMIBGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    fsCapwapMulticastMIBCompliance = fsCapwapMulticastMIBCompliance.setStatus('current')
fsCapwapMulticastMIBGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 59, 2, 2, 1)).setObjects(("FS-CAPWAP-MULTICAST-MIB", "fsCapwapMulticastWorkingMode"), ("FS-CAPWAP-MULTICAST-MIB", "fsCapwapMulticastGroup"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    fsCapwapMulticastMIBGroup = fsCapwapMulticastMIBGroup.setStatus('current')
mibBuilder.exportSymbols("FS-CAPWAP-MULTICAST-MIB", fsCapwapMulticastMIBGroups=fsCapwapMulticastMIBGroups, fsCapwapMulticastWorkingMode=fsCapwapMulticastWorkingMode, fsCapwapMulticastGroup=fsCapwapMulticastGroup, fsCapwapMulticastMIBCompliance=fsCapwapMulticastMIBCompliance, fsCapwapMulticastMIBObjects=fsCapwapMulticastMIBObjects, fsCapwapMulticastMIBCompliances=fsCapwapMulticastMIBCompliances, PYSNMP_MODULE_ID=fsCapwapMulticastMIB, fsCapwapMulticastMIBConformance=fsCapwapMulticastMIBConformance, fsCapwapMulticastMIBGroup=fsCapwapMulticastMIBGroup, fsCapwapMulticastMIB=fsCapwapMulticastMIB)
