#
# PySNMP MIB module RFC1414-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/rfc/RFC1414-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:49:23 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Gauge32, MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, Counter64, TimeTicks, ModuleIdentity, mib_2 = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "Counter64", "TimeTicks", "ModuleIdentity", "mib-2")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
tcpConnRemAddress, tcpConnLocalAddress, tcpConnRemPort, tcpConnLocalPort = mibBuilder.importSymbols("TCP-MIB", "tcpConnRemAddress", "tcpConnLocalAddress", "tcpConnRemPort", "tcpConnLocalPort")
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
mibBuilder.exportSymbols("RFC1414-MIB", identTable=identTable, identStatus=identStatus, identOpSys=identOpSys, identInfo=identInfo, identMisc=identMisc, identCharset=identCharset, ident=ident, identEntry=identEntry, identUserid=identUserid)
