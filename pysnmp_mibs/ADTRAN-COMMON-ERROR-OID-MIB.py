#
# PySNMP MIB module ADTRAN-COMMON-ERROR-OID-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/adtran/ADTRAN-COMMON-ERROR-OID-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:29:20 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
adGenSlotInfoIndex, = mibBuilder.importSymbols("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex")
adGenTa5kErrorOid, adGenTa5kSErrorOidID = mibBuilder.importSymbols("ADTRAN-GENTA5K-MIB", "adGenTa5kErrorOid", "adGenTa5kSErrorOidID")
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
adGenCommonErrorOidMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 664, 6, 10000, 67, 1, 9, 1))
if mibBuilder.loadTexts: adGenCommonErrorOidMIB.setLastUpdated('200711062117Z')
if mibBuilder.loadTexts: adGenCommonErrorOidMIB.setOrganization('ADTRAN, Inc.')
adTa5kErrorOidMgmt = MibIdentifier((1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 9, 1))
adTa5kErrorOidTable = MibTable((1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 9, 1, 1), )
if mibBuilder.loadTexts: adTa5kErrorOidTable.setStatus('current')
adTa5kErrorOidTableEntry = MibTableRow((1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 9, 1, 1, 1), ).setIndexNames((0, "ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"))
if mibBuilder.loadTexts: adTa5kErrorOidTableEntry.setStatus('current')
adTa5kDuplicateIndexErrorReporting = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 9, 1, 1, 1, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 31))).setMaxAccess("readonly")
if mibBuilder.loadTexts: adTa5kDuplicateIndexErrorReporting.setStatus('current')
adTa5kPseudowireErrorReporting = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 9, 1, 1, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 31))).setMaxAccess("readonly")
if mibBuilder.loadTexts: adTa5kPseudowireErrorReporting.setStatus('current')
adTa5kPhysicalDs1ErrorReporting = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 9, 1, 1, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 31))).setMaxAccess("readonly")
if mibBuilder.loadTexts: adTa5kPhysicalDs1ErrorReporting.setStatus('current')
mibBuilder.exportSymbols("ADTRAN-COMMON-ERROR-OID-MIB", adTa5kPhysicalDs1ErrorReporting=adTa5kPhysicalDs1ErrorReporting, adTa5kDuplicateIndexErrorReporting=adTa5kDuplicateIndexErrorReporting, adTa5kErrorOidMgmt=adTa5kErrorOidMgmt, adTa5kPseudowireErrorReporting=adTa5kPseudowireErrorReporting, adTa5kErrorOidTable=adTa5kErrorOidTable, PYSNMP_MODULE_ID=adGenCommonErrorOidMIB, adGenCommonErrorOidMIB=adGenCommonErrorOidMIB, adTa5kErrorOidTableEntry=adTa5kErrorOidTableEntry)
