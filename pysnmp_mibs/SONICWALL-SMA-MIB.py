#
# PySNMP MIB module SONICWALL-SMA-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/sonicwall/SONICWALL-SMA-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:34:20 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
InternationalDisplayString, = mibBuilder.importSymbols("HOST-RESOURCES-MIB", "InternationalDisplayString")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, NotificationType, Integer32, Bits, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Integer32", "Bits", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
sonicwallSMA, = mibBuilder.importSymbols("SONICWALL-SMI", "sonicwallSMA")
sonicwallSMAAppliance = ObjectIdentity((1, 3, 6, 1, 4, 1, 8741, 8, 1))
if mibBuilder.loadTexts: sonicwallSMAAppliance.setStatus('current')
sonicwallSMACMS = ObjectIdentity((1, 3, 6, 1, 4, 1, 8741, 8, 2))
if mibBuilder.loadTexts: sonicwallSMACMS.setStatus('current')
mibBuilder.exportSymbols("SONICWALL-SMA-MIB", sonicwallSMAAppliance=sonicwallSMAAppliance, sonicwallSMACMS=sonicwallSMACMS)
