#
# PySNMP MIB module ADTRAN-GENERIC-PSEUDOWIRE-CEM-COUNTERS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/adtran/ADTRAN-GENERIC-PSEUDOWIRE-CEM-COUNTERS-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:29:21 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
adGenPseudowireCEMPerfID, adGenPseudowireCEMPerformance = mibBuilder.importSymbols("ADTRAN-GENERIC-PSEUDOWIRE-CEM-MGMT-MIB", "adGenPseudowireCEMPerfID", "adGenPseudowireCEMPerformance")
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
adGenPseudowireCEMPerfModuleIdentity = ModuleIdentity((1, 3, 6, 1, 4, 1, 664, 6, 10000, 70, 30, 2, 1))
adGenPseudowireCEMPerfModuleIdentity.setRevisions(('2011-04-28 00:00',))
if mibBuilder.loadTexts: adGenPseudowireCEMPerfModuleIdentity.setLastUpdated('201104280000Z')
if mibBuilder.loadTexts: adGenPseudowireCEMPerfModuleIdentity.setOrganization('ADTRAN, Inc.')
adGenPseudowireCEMPerfProv = MibIdentifier((1, 3, 6, 1, 4, 1, 664, 5, 70, 30, 5, 1))
adGenPseudowireCEMPerfProvTable = MibTable((1, 3, 6, 1, 4, 1, 664, 5, 70, 30, 5, 1, 1), )
if mibBuilder.loadTexts: adGenPseudowireCEMPerfProvTable.setStatus('current')
adGenPseudowireCEMPerfProvTableEntry = MibTableRow((1, 3, 6, 1, 4, 1, 664, 5, 70, 30, 5, 1, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: adGenPseudowireCEMPerfProvTableEntry.setStatus('current')
adGenPseudowireCEMPerfErrorStr = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 70, 30, 5, 1, 1, 1, 1), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adGenPseudowireCEMPerfErrorStr.setStatus('current')
adGenPseudowireCEMPerfClear15MinCounters = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 70, 30, 5, 1, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1))).clone(namedValues=NamedValues(("reset", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: adGenPseudowireCEMPerfClear15MinCounters.setStatus('current')
adGenPseudowireCEMPerfClear24HrCounters = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 70, 30, 5, 1, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1))).clone(namedValues=NamedValues(("reset", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: adGenPseudowireCEMPerfClear24HrCounters.setStatus('current')
mibBuilder.exportSymbols("ADTRAN-GENERIC-PSEUDOWIRE-CEM-COUNTERS-MIB", adGenPseudowireCEMPerfErrorStr=adGenPseudowireCEMPerfErrorStr, adGenPseudowireCEMPerfClear15MinCounters=adGenPseudowireCEMPerfClear15MinCounters, adGenPseudowireCEMPerfClear24HrCounters=adGenPseudowireCEMPerfClear24HrCounters, adGenPseudowireCEMPerfProvTable=adGenPseudowireCEMPerfProvTable, PYSNMP_MODULE_ID=adGenPseudowireCEMPerfModuleIdentity, adGenPseudowireCEMPerfModuleIdentity=adGenPseudowireCEMPerfModuleIdentity, adGenPseudowireCEMPerfProv=adGenPseudowireCEMPerfProv, adGenPseudowireCEMPerfProvTableEntry=adGenPseudowireCEMPerfProvTableEntry)
