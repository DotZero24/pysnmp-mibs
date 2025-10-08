#
# PySNMP MIB module RFC1414-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/rfc/RFC1414-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:27:12 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, TimeTicks, MibIdentifier, Integer32, Bits, mib_2, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "TimeTicks", "MibIdentifier", "Integer32", "Bits", "mib-2", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
tcpConnLocalPort, tcpConnRemAddress, tcpConnLocalAddress, tcpConnRemPort = mibBuilder.importSymbols("TCP-MIB", "tcpConnLocalPort", "tcpConnRemAddress", "tcpConnLocalAddress", "tcpConnRemPort")
ident = MibIdentifier((1, 3, 6, 1, 2, 1, 24))
identInfo = MibIdentifier((1, 3, 6, 1, 2, 1, 24, 1))
identTable = MibTable((1, 3, 6, 1, 2, 1, 24, 1, 1), )
if mibBuilder.loadTexts: identTable.setStatus('mandatory')
identEntry = MibTableRow((1, 3, 6, 1, 2, 1, 24, 1, 1, 1), ).setIndexNames((0, "TCP-MIB", "tcpConnLocalAddress"), (0, "TCP-MIB", "tcpConnLocalPort"), (0, "TCP-MIB", "tcpConnRemAddress"), (0, "TCP-MIB", "tcpConnRemPort"))
if mibBuilder.loadTexts: identEntry.setStatus('mandatory')
identStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 24, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("noError", 1), ("unknownError", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: identStatus.setStatus('mandatory')
identOpSys = MibTableColumn((1, 3, 6, 1, 2, 1, 24, 1, 1, 1, 2), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 40))).setMaxAccess("readonly")
if mibBuilder.loadTexts: identOpSys.setStatus('mandatory')
identCharset = MibTableColumn((1, 3, 6, 1, 2, 1, 24, 1, 1, 1, 3), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 40))).setMaxAccess("readonly")
if mibBuilder.loadTexts: identCharset.setStatus('mandatory')
identUserid = MibTableColumn((1, 3, 6, 1, 2, 1, 24, 1, 1, 1, 4), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: identUserid.setStatus('mandatory')
identMisc = MibTableColumn((1, 3, 6, 1, 2, 1, 24, 1, 1, 1, 5), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: identMisc.setStatus('mandatory')
mibBuilder.exportSymbols("RFC1414-MIB", identEntry=identEntry, ident=ident, identCharset=identCharset, identInfo=identInfo, identStatus=identStatus, identTable=identTable, identMisc=identMisc, identOpSys=identOpSys, identUserid=identUserid)
