#
# PySNMP MIB module SONICWALL-SMI (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/sonicwall/SONICWALL-SMI
# Produced by pysmi-1.1.12 at Wed Oct  8 10:34:20 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, enterprises, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "enterprises", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
sonicwall = ModuleIdentity((1, 3, 6, 1, 4, 1, 8741))
sonicwall.setRevisions(('2017-01-06 00:00', '2007-01-06 00:00',))
if mibBuilder.loadTexts: sonicwall.setLastUpdated('201804090001Z')
if mibBuilder.loadTexts: sonicwall.setOrganization('SonicWall')
sonicwallFw = ObjectIdentity((1, 3, 6, 1, 4, 1, 8741, 1))
if mibBuilder.loadTexts: sonicwallFw.setStatus('current')
sonicwallCommon = ObjectIdentity((1, 3, 6, 1, 4, 1, 8741, 2))
if mibBuilder.loadTexts: sonicwallCommon.setStatus('current')
sonicwallGMS = ObjectIdentity((1, 3, 6, 1, 4, 1, 8741, 3))
if mibBuilder.loadTexts: sonicwallGMS.setStatus('current')
sonicwallEmailSec = ObjectIdentity((1, 3, 6, 1, 4, 1, 8741, 4))
if mibBuilder.loadTexts: sonicwallEmailSec.setStatus('current')
sonicwallDataCenter = ObjectIdentity((1, 3, 6, 1, 4, 1, 8741, 5))
if mibBuilder.loadTexts: sonicwallDataCenter.setStatus('current')
sonicwallSSLVPN = ObjectIdentity((1, 3, 6, 1, 4, 1, 8741, 6))
if mibBuilder.loadTexts: sonicwallSSLVPN.setStatus('current')
sonicwallCDP = ObjectIdentity((1, 3, 6, 1, 4, 1, 8741, 7))
if mibBuilder.loadTexts: sonicwallCDP.setStatus('current')
sonicwallSMA = ObjectIdentity((1, 3, 6, 1, 4, 1, 8741, 8))
if mibBuilder.loadTexts: sonicwallSMA.setStatus('current')
mibBuilder.exportSymbols("SONICWALL-SMI", sonicwallDataCenter=sonicwallDataCenter, sonicwallSSLVPN=sonicwallSSLVPN, PYSNMP_MODULE_ID=sonicwall, sonicwall=sonicwall, sonicwallEmailSec=sonicwallEmailSec, sonicwallCDP=sonicwallCDP, sonicwallFw=sonicwallFw, sonicwallCommon=sonicwallCommon, sonicwallSMA=sonicwallSMA, sonicwallGMS=sonicwallGMS)
