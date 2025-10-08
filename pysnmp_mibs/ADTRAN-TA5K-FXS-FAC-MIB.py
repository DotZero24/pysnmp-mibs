#
# PySNMP MIB module ADTRAN-TA5K-FXS-FAC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/adtran/ADTRAN-TA5K-FXS-FAC-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:30:02 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
adGenSlotInfoIndex, = mibBuilder.importSymbols("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex")
adTa5kFxsFac, adTa5kFxsFacID = mibBuilder.importSymbols("ADTRAN-GENTA5K-MIB", "adTa5kFxsFac", "adTa5kFxsFacID")
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
adTa5kFxsFacIdentity = ModuleIdentity((1, 3, 6, 1, 4, 1, 664, 6, 10000, 67, 1, 35, 1))
adTa5kFxsFacIdentity.setRevisions(('2011-11-09 00:00',))
if mibBuilder.loadTexts: adTa5kFxsFacIdentity.setLastUpdated('201111090000Z')
if mibBuilder.loadTexts: adTa5kFxsFacIdentity.setOrganization('Adtran, Inc.')
adTa5kFxsFacLimitedThlTable = MibTable((1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 35, 1), )
if mibBuilder.loadTexts: adTa5kFxsFacLimitedThlTable.setStatus('current')
adTa5kFxsFacLimitedThlEntry = MibTableRow((1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 35, 1, 1), ).setIndexNames((0, "ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"))
if mibBuilder.loadTexts: adTa5kFxsFacLimitedThlEntry.setStatus('current')
adTa5kFxsFacLimitedThlStart = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 35, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1))).clone(namedValues=NamedValues(("begin", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: adTa5kFxsFacLimitedThlStart.setStatus('current')
adTa5kFxsFacLimitedThlStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 35, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("na", 1), ("complete", 2), ("fault", 3), ("running", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: adTa5kFxsFacLimitedThlStatus.setStatus('current')
adTa5kFxsFacLimitedThlResults = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 35, 1, 1, 3), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 256))).setMaxAccess("readonly")
if mibBuilder.loadTexts: adTa5kFxsFacLimitedThlResults.setStatus('current')
mibBuilder.exportSymbols("ADTRAN-TA5K-FXS-FAC-MIB", adTa5kFxsFacIdentity=adTa5kFxsFacIdentity, adTa5kFxsFacLimitedThlEntry=adTa5kFxsFacLimitedThlEntry, adTa5kFxsFacLimitedThlStatus=adTa5kFxsFacLimitedThlStatus, adTa5kFxsFacLimitedThlStart=adTa5kFxsFacLimitedThlStart, adTa5kFxsFacLimitedThlResults=adTa5kFxsFacLimitedThlResults, adTa5kFxsFacLimitedThlTable=adTa5kFxsFacLimitedThlTable, PYSNMP_MODULE_ID=adTa5kFxsFacIdentity)
