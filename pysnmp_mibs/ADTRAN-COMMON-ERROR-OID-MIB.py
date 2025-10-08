#
# PySNMP MIB module ADTRAN-COMMON-ERROR-OID-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/adtran/ADTRAN-COMMON-ERROR-OID-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:52:29 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
adGenSlotInfoIndex, = mibBuilder.importSymbols("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex")
adGenTa5kSErrorOidID, adGenTa5kErrorOid = mibBuilder.importSymbols("ADTRAN-GENTA5K-MIB", "adGenTa5kSErrorOidID", "adGenTa5kErrorOid")
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
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
mibBuilder.exportSymbols("ADTRAN-COMMON-ERROR-OID-MIB", PYSNMP_MODULE_ID=adGenCommonErrorOidMIB, adTa5kDuplicateIndexErrorReporting=adTa5kDuplicateIndexErrorReporting, adTa5kErrorOidTableEntry=adTa5kErrorOidTableEntry, adGenCommonErrorOidMIB=adGenCommonErrorOidMIB, adTa5kPseudowireErrorReporting=adTa5kPseudowireErrorReporting, adTa5kErrorOidTable=adTa5kErrorOidTable, adTa5kErrorOidMgmt=adTa5kErrorOidMgmt, adTa5kPhysicalDs1ErrorReporting=adTa5kPhysicalDs1ErrorReporting)
