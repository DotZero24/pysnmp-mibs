#
# PySNMP MIB module SONICWALL-SMI (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/sonicwall/SONICWALL-SMI
# Produced by pysmi-1.1.12 at Thu Sep 11 10:17:36 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, enterprises, ObjectIdentity, Gauge32, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "enterprises", "ObjectIdentity", "Gauge32", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
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
mibBuilder.exportSymbols("SONICWALL-SMI", sonicwallCommon=sonicwallCommon, sonicwallDataCenter=sonicwallDataCenter, PYSNMP_MODULE_ID=sonicwall, sonicwallGMS=sonicwallGMS, sonicwallFw=sonicwallFw, sonicwallEmailSec=sonicwallEmailSec, sonicwallSMA=sonicwallSMA, sonicwall=sonicwall, sonicwallSSLVPN=sonicwallSSLVPN, sonicwallCDP=sonicwallCDP)
