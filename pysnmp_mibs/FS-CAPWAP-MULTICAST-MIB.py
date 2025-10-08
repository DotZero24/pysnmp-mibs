#
# PySNMP MIB module FS-CAPWAP-MULTICAST-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/fscom/FS-CAPWAP-MULTICAST-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:01:41 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
fsMgmt, = mibBuilder.importSymbols("FS-SMI", "fsMgmt")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
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
mibBuilder.exportSymbols("FS-CAPWAP-MULTICAST-MIB", fsCapwapMulticastMIBCompliance=fsCapwapMulticastMIBCompliance, fsCapwapMulticastMIBGroup=fsCapwapMulticastMIBGroup, fsCapwapMulticastMIBConformance=fsCapwapMulticastMIBConformance, fsCapwapMulticastMIBGroups=fsCapwapMulticastMIBGroups, fsCapwapMulticastWorkingMode=fsCapwapMulticastWorkingMode, fsCapwapMulticastGroup=fsCapwapMulticastGroup, fsCapwapMulticastMIBCompliances=fsCapwapMulticastMIBCompliances, fsCapwapMulticastMIBObjects=fsCapwapMulticastMIBObjects, PYSNMP_MODULE_ID=fsCapwapMulticastMIB, fsCapwapMulticastMIB=fsCapwapMulticastMIB)
