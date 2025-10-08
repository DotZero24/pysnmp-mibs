#
# PySNMP MIB module CENTILLION-DOT3-EXTENSIONS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/nortel/CENTILLION-DOT3-EXTENSIONS-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:03:12 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
extensions, = mibBuilder.importSymbols("CENTILLION-ROOT-MIB", "extensions")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, Counter64, TimeTicks, ModuleIdentity, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "Counter64", "TimeTicks", "ModuleIdentity", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
cnDot3Extensions = MibIdentifier((1, 3, 6, 1, 4, 1, 930, 3, 4))
cnDot3ExtnTable = MibTable((1, 3, 6, 1, 4, 1, 930, 3, 4, 1), )
if mibBuilder.loadTexts: cnDot3ExtnTable.setStatus('mandatory')
cnDot3ExtnEntry = MibTableRow((1, 3, 6, 1, 4, 1, 930, 3, 4, 1, 1), ).setIndexNames((0, "CENTILLION-DOT3-EXTENSIONS-MIB", "cnDot3ExtnIfIndex"))
if mibBuilder.loadTexts: cnDot3ExtnEntry.setStatus('mandatory')
cnDot3ExtnIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 930, 3, 4, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cnDot3ExtnIfIndex.setStatus('mandatory')
cnDot3ExtnIfAdminSpeed = MibTableColumn((1, 3, 6, 1, 4, 1, 930, 3, 4, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("forced10", 1), ("forced100", 2), ("auto", 3), ("forced1000", 4)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cnDot3ExtnIfAdminSpeed.setStatus('mandatory')
cnDot3ExtnIfOperSpeed = MibTableColumn((1, 3, 6, 1, 4, 1, 930, 3, 4, 1, 1, 3), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cnDot3ExtnIfOperSpeed.setStatus('mandatory')
cnDot3ExtnIfAdminConnectionType = MibTableColumn((1, 3, 6, 1, 4, 1, 930, 3, 4, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("halfDuplex", 1), ("fullDuplex", 2), ("auto", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cnDot3ExtnIfAdminConnectionType.setStatus('mandatory')
cnDot3ExtnIfOperConnectionType = MibTableColumn((1, 3, 6, 1, 4, 1, 930, 3, 4, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("halfDuplex", 1), ("fullDuplex", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cnDot3ExtnIfOperConnectionType.setStatus('mandatory')
mibBuilder.exportSymbols("CENTILLION-DOT3-EXTENSIONS-MIB", cnDot3ExtnEntry=cnDot3ExtnEntry, cnDot3Extensions=cnDot3Extensions, cnDot3ExtnIfIndex=cnDot3ExtnIfIndex, cnDot3ExtnIfOperConnectionType=cnDot3ExtnIfOperConnectionType, cnDot3ExtnIfAdminSpeed=cnDot3ExtnIfAdminSpeed, cnDot3ExtnIfAdminConnectionType=cnDot3ExtnIfAdminConnectionType, cnDot3ExtnIfOperSpeed=cnDot3ExtnIfOperSpeed, cnDot3ExtnTable=cnDot3ExtnTable)
