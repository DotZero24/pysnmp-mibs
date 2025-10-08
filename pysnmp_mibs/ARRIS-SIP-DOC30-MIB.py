#
# PySNMP MIB module ARRIS-SIP-DOC30-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/arris/ARRIS-SIP-DOC30-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:08:41 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
arrisSipMib, = mibBuilder.importSymbols("ARRIS-SIP-MIB", "arrisSipMib")
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TruthValue, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TruthValue", "TextualConvention")
sipCfgDoc30 = ModuleIdentity((1, 3, 6, 1, 4, 1, 4115, 11, 3))
if mibBuilder.loadTexts: sipCfgDoc30.setLastUpdated('200908280000Z')
if mibBuilder.loadTexts: sipCfgDoc30.setOrganization('Arris Interactive')
sipCfgDoc30FeatureSwitch = MibScalar((1, 3, 6, 1, 4, 1, 4115, 11, 3, 1), Bits().clone(namedValues=NamedValues(("removeMACfromUAHeader", 0), ("unused1", 1), ("unused2", 2), ("unused3", 3), ("unused4", 4), ("unused5", 5), ("unused6", 6), ("unused7", 7), ("unused8", 8), ("unused9", 9), ("unused10", 10), ("unused11", 11), ("unused12", 12), ("unused13", 13), ("unused14", 14), ("unused15", 15), ("unused16", 16), ("unused17", 17), ("unused18", 18), ("unused19", 19), ("unused20", 20), ("unused21", 21), ("unused22", 22), ("unused23", 23), ("unused24", 24), ("unused25", 25), ("unused26", 26), ("unused27", 27), ("unused28", 28), ("unused29", 29), ("unused30", 30), ("unused31", 31))).clone(hexValue="00000000")).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sipCfgDoc30FeatureSwitch.setStatus('current')
mibBuilder.exportSymbols("ARRIS-SIP-DOC30-MIB", sipCfgDoc30=sipCfgDoc30, sipCfgDoc30FeatureSwitch=sipCfgDoc30FeatureSwitch, PYSNMP_MODULE_ID=sipCfgDoc30)
