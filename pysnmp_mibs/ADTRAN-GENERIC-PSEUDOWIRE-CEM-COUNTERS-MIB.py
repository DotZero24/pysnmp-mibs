#
# PySNMP MIB module ADTRAN-GENERIC-PSEUDOWIRE-CEM-COUNTERS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/adtran/ADTRAN-GENERIC-PSEUDOWIRE-CEM-COUNTERS-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:52:31 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
adGenPseudowireCEMPerformance, adGenPseudowireCEMPerfID = mibBuilder.importSymbols("ADTRAN-GENERIC-PSEUDOWIRE-CEM-MGMT-MIB", "adGenPseudowireCEMPerformance", "adGenPseudowireCEMPerfID")
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
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
mibBuilder.exportSymbols("ADTRAN-GENERIC-PSEUDOWIRE-CEM-COUNTERS-MIB", adGenPseudowireCEMPerfProv=adGenPseudowireCEMPerfProv, PYSNMP_MODULE_ID=adGenPseudowireCEMPerfModuleIdentity, adGenPseudowireCEMPerfClear15MinCounters=adGenPseudowireCEMPerfClear15MinCounters, adGenPseudowireCEMPerfModuleIdentity=adGenPseudowireCEMPerfModuleIdentity, adGenPseudowireCEMPerfProvTableEntry=adGenPseudowireCEMPerfProvTableEntry, adGenPseudowireCEMPerfClear24HrCounters=adGenPseudowireCEMPerfClear24HrCounters, adGenPseudowireCEMPerfProvTable=adGenPseudowireCEMPerfProvTable, adGenPseudowireCEMPerfErrorStr=adGenPseudowireCEMPerfErrorStr)
