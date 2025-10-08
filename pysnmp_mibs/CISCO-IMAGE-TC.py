#
# PySNMP MIB module CISCO-IMAGE-TC (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/cisco/CISCO-IMAGE-TC
# Produced by pysmi-1.1.12 at Thu Sep 11 10:12:07 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
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

mibBuilder.exportSymbols("CISCO-IMAGE-TC", CeImageInstallableStatus=CeImageInstallableStatus, CeImageInstallableType=CeImageInstallableType, ciscoImageTc=ciscoImageTc, PYSNMP_MODULE_ID=ciscoImageTc)
