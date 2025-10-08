#
# PySNMP MIB module MERU-CONFIG-SECURITYCERT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/meru/MERU-CONFIG-SECURITYCERT-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:41:29 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
Ipv6Address, = mibBuilder.importSymbols("IPV6-TC", "Ipv6Address")
mwConfiguration, = mibBuilder.importSymbols("MERU-SMI", "mwConfiguration")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Integer32, enterprises, ObjectIdentity, Gauge32, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, Counter32, iso, MibIdentifier, Counter64, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Integer32", "enterprises", "ObjectIdentity", "Gauge32", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "Counter32", "iso", "MibIdentifier", "Counter64", "Bits", "TimeTicks", "IpAddress")
DisplayString, MacAddress, TimeInterval, TimeStamp, RowStatus, DateAndTime, TruthValue, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "MacAddress", "TimeInterval", "TimeStamp", "RowStatus", "DateAndTime", "TruthValue", "TextualConvention")
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
mibBuilder.exportSymbols("MERU-CONFIG-SECURITYCERT-MIB", PYSNMP_MODULE_ID=mwConfigSecurityCert, mwSslCertInput=mwSslCertInput, mwSslCertInputCertificateName=mwSslCertInputCertificateName, mwSslCertCertFormattedText=mwSslCertCertFormattedText, mwSslCert=mwSslCert, mwConfigSecurityCert=mwConfigSecurityCert, mwSslCertCertificateName=mwSslCertCertificateName, mwSslCertInputPfxPassword=mwSslCertInputPfxPassword)
