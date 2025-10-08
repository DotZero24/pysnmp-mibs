#
# PySNMP MIB module ADTRAN-TA5K-HK-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/adtran/ADTRAN-TA5K-HK-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:52:49 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
adGenSlotInfoIndex, = mibBuilder.importSymbols("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex")
adGenTa5kHkID, adGenTa5kHk = mibBuilder.importSymbols("ADTRAN-GENTA5K-MIB", "adGenTa5kHkID", "adGenTa5kHk")
adProducts, adMgmt, adIdentity, adIdentityShared = mibBuilder.importSymbols("ADTRAN-MIB", "adProducts", "adMgmt", "adIdentity", "adIdentityShared")
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, NotificationType, Integer32, Bits, Unsigned32, iso, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Integer32", "Bits", "Unsigned32", "iso", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
RowStatus, TextualConvention, MacAddress, TruthValue, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "TextualConvention", "MacAddress", "TruthValue", "DisplayString")
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
mibBuilder.exportSymbols("ADTRAN-TA5K-HK-MIB", PYSNMP_MODULE_ID=adTa5kHkModuleIdentity, adTa5kHkTemp=adTa5kHkTemp, adTa5kHkModuleIdentity=adTa5kHkModuleIdentity, adTa5kHkEntry=adTa5kHkEntry, adTa5kHkPresent=adTa5kHkPresent, adTa5kHkTable=adTa5kHkTable)
