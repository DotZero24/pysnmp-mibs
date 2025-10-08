#
# PySNMP MIB module IANA-STORAGE-MEDIA-TYPE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/rfc/IANA-STORAGE-MEDIA-TYPE-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:27:48 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, TimeTicks, MibIdentifier, Integer32, Bits, mib_2, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "TimeTicks", "MibIdentifier", "Integer32", "Bits", "mib-2", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ianaStorageMediaTypeMIB = ModuleIdentity((1, 3, 6, 1, 2, 1, 237))
ianaStorageMediaTypeMIB.setRevisions(('2016-06-17 00:00', '2015-10-12 00:00',))
if mibBuilder.loadTexts: ianaStorageMediaTypeMIB.setLastUpdated('201606170000Z')
if mibBuilder.loadTexts: ianaStorageMediaTypeMIB.setOrganization('IANA')
class IANAStorageMediaType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))
    namedValues = NamedValues(("other", 1), ("unknown", 2), ("hardDisk", 3), ("opticalDisk", 4), ("floppyDisk", 5))

mibBuilder.exportSymbols("IANA-STORAGE-MEDIA-TYPE-MIB", PYSNMP_MODULE_ID=ianaStorageMediaTypeMIB, IANAStorageMediaType=IANAStorageMediaType, ianaStorageMediaTypeMIB=ianaStorageMediaTypeMIB)
