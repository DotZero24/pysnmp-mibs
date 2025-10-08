#
# PySNMP MIB module ARRIS-SIP-DOC30-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/arris/ARRIS-SIP-DOC30-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:18:45 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
arrisSipMib, = mibBuilder.importSymbols("ARRIS-SIP-MIB", "arrisSipMib")
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
MibIdentifier, NotificationType, Integer32, Bits, Unsigned32, iso, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Integer32", "Bits", "Unsigned32", "iso", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TruthValue, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "TextualConvention", "DisplayString")
sipCfgDoc30 = ModuleIdentity((1, 3, 6, 1, 4, 1, 4115, 11, 3))
if mibBuilder.loadTexts: sipCfgDoc30.setLastUpdated('200908280000Z')
if mibBuilder.loadTexts: sipCfgDoc30.setOrganization('Arris Interactive')
sipCfgDoc30FeatureSwitch = MibScalar((1, 3, 6, 1, 4, 1, 4115, 11, 3, 1), Bits().clone(namedValues=NamedValues(("removeMACfromUAHeader", 0), ("unused1", 1), ("unused2", 2), ("unused3", 3), ("unused4", 4), ("unused5", 5), ("unused6", 6), ("unused7", 7), ("unused8", 8), ("unused9", 9), ("unused10", 10), ("unused11", 11), ("unused12", 12), ("unused13", 13), ("unused14", 14), ("unused15", 15), ("unused16", 16), ("unused17", 17), ("unused18", 18), ("unused19", 19), ("unused20", 20), ("unused21", 21), ("unused22", 22), ("unused23", 23), ("unused24", 24), ("unused25", 25), ("unused26", 26), ("unused27", 27), ("unused28", 28), ("unused29", 29), ("unused30", 30), ("unused31", 31))).clone(hexValue="00000000")).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sipCfgDoc30FeatureSwitch.setStatus('current')
mibBuilder.exportSymbols("ARRIS-SIP-DOC30-MIB", PYSNMP_MODULE_ID=sipCfgDoc30, sipCfgDoc30=sipCfgDoc30, sipCfgDoc30FeatureSwitch=sipCfgDoc30FeatureSwitch)
