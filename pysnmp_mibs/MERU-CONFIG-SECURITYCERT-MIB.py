#
# PySNMP MIB module MERU-CONFIG-SECURITYCERT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/meru/MERU-CONFIG-SECURITYCERT-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 11:08:32 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
Ipv6Address, = mibBuilder.importSymbols("IPV6-TC", "Ipv6Address")
mwConfiguration, = mibBuilder.importSymbols("MERU-SMI", "mwConfiguration")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, enterprises, NotificationType, Integer32, Bits, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, Counter64, TimeTicks, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "enterprises", "NotificationType", "Integer32", "Bits", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "Counter64", "TimeTicks", "Gauge32")
RowStatus, DateAndTime, TextualConvention, TimeInterval, MacAddress, TruthValue, TimeStamp, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "DateAndTime", "TextualConvention", "TimeInterval", "MacAddress", "TruthValue", "TimeStamp", "DisplayString")
mwConfigSecurityCert = ModuleIdentity((1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 10))
if mibBuilder.loadTexts: mwConfigSecurityCert.setLastUpdated('200506050000Z')
if mibBuilder.loadTexts: mwConfigSecurityCert.setOrganization('Meru Networks')
mwSslCertInput = MibIdentifier((1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 10, 2))
mwSslCert = MibIdentifier((1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 10, 3))
mwSslCertInputCertificateName = MibScalar((1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 10, 2, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mwSslCertInputCertificateName.setStatus('current')
mwSslCertInputPfxPassword = MibScalar((1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 10, 2, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mwSslCertInputPfxPassword.setStatus('current')
mwSslCertCertificateName = MibScalar((1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 10, 3, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mwSslCertCertificateName.setStatus('current')
mwSslCertCertFormattedText = MibScalar((1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 10, 3, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mwSslCertCertFormattedText.setStatus('current')
mibBuilder.exportSymbols("MERU-CONFIG-SECURITYCERT-MIB", mwSslCertInput=mwSslCertInput, mwConfigSecurityCert=mwConfigSecurityCert, mwSslCertCertificateName=mwSslCertCertificateName, mwSslCert=mwSslCert, mwSslCertInputCertificateName=mwSslCertInputCertificateName, mwSslCertCertFormattedText=mwSslCertCertFormattedText, PYSNMP_MODULE_ID=mwConfigSecurityCert, mwSslCertInputPfxPassword=mwSslCertInputPfxPassword)
