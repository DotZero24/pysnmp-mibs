#
# PySNMP MIB module CISCO-IMAGE-TC (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/cisco/CISCO-IMAGE-TC
# Produced by pysmi-1.1.12 at Wed Oct  8 10:24:27 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoImageTc = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 455))
ciscoImageTc.setRevisions(('2005-01-12 00:00',))
if mibBuilder.loadTexts: ciscoImageTc.setLastUpdated('200501120000Z')
if mibBuilder.loadTexts: ciscoImageTc.setOrganization('Cisco Systems, Inc.')
class CeImageInstallableStatus(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9))
    namedValues = NamedValues(("active", 1), ("pendingInstall", 2), ("pendingRemoval", 3), ("installPendingReload", 4), ("removedPendingReload", 5), ("installPendingReloadPendingRemoval", 6), ("removedPendingReloadPendingInstall", 7), ("pruned", 8), ("inactive", 9))

class CeImageInstallableType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))
    namedValues = NamedValues(("base", 1), ("patch", 2), ("script", 3), ("package", 4), ("compositePackage", 5), ("softwareMaintenanceUpgrade", 6))

mibBuilder.exportSymbols("CISCO-IMAGE-TC", PYSNMP_MODULE_ID=ciscoImageTc, CeImageInstallableStatus=CeImageInstallableStatus, CeImageInstallableType=CeImageInstallableType, ciscoImageTc=ciscoImageTc)
