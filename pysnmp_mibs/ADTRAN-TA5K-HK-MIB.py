#
# PySNMP MIB module ADTRAN-TA5K-HK-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/adtran/ADTRAN-TA5K-HK-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:29:33 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
adGenSlotInfoIndex, = mibBuilder.importSymbols("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex")
adGenTa5kHk, adGenTa5kHkID = mibBuilder.importSymbols("ADTRAN-GENTA5K-MIB", "adGenTa5kHk", "adGenTa5kHkID")
adMgmt, adIdentityShared, adProducts, adIdentity = mibBuilder.importSymbols("ADTRAN-MIB", "adMgmt", "adIdentityShared", "adProducts", "adIdentity")
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, MacAddress, RowStatus, TruthValue, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "MacAddress", "RowStatus", "TruthValue", "TextualConvention")
adTa5kHkModuleIdentity = ModuleIdentity((1, 3, 6, 1, 4, 1, 664, 6, 10000, 67, 1, 7, 1))
if mibBuilder.loadTexts: adTa5kHkModuleIdentity.setLastUpdated('200606120832Z')
if mibBuilder.loadTexts: adTa5kHkModuleIdentity.setOrganization('ADTRAN, Inc.')
adTa5kHkTable = MibTable((1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 7, 1), )
if mibBuilder.loadTexts: adTa5kHkTable.setStatus('current')
adTa5kHkEntry = MibTableRow((1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 7, 1, 1), ).setIndexNames((0, "ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"))
if mibBuilder.loadTexts: adTa5kHkEntry.setStatus('current')
adTa5kHkPresent = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 7, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("true", 1), ("false", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: adTa5kHkPresent.setStatus('current')
adTa5kHkTemp = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 7, 1, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adTa5kHkTemp.setStatus('current')
mibBuilder.exportSymbols("ADTRAN-TA5K-HK-MIB", adTa5kHkPresent=adTa5kHkPresent, PYSNMP_MODULE_ID=adTa5kHkModuleIdentity, adTa5kHkTemp=adTa5kHkTemp, adTa5kHkEntry=adTa5kHkEntry, adTa5kHkModuleIdentity=adTa5kHkModuleIdentity, adTa5kHkTable=adTa5kHkTable)
