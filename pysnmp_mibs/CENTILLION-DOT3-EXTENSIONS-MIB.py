#
# PySNMP MIB module CENTILLION-DOT3-EXTENSIONS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/nortel/CENTILLION-DOT3-EXTENSIONS-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 09:59:29 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
extensions, = mibBuilder.importSymbols("CENTILLION-ROOT-MIB", "extensions")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
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
mibBuilder.exportSymbols("CENTILLION-DOT3-EXTENSIONS-MIB", cnDot3ExtnIfIndex=cnDot3ExtnIfIndex, cnDot3ExtnIfAdminSpeed=cnDot3ExtnIfAdminSpeed, cnDot3Extensions=cnDot3Extensions, cnDot3ExtnEntry=cnDot3ExtnEntry, cnDot3ExtnTable=cnDot3ExtnTable, cnDot3ExtnIfAdminConnectionType=cnDot3ExtnIfAdminConnectionType, cnDot3ExtnIfOperConnectionType=cnDot3ExtnIfOperConnectionType, cnDot3ExtnIfOperSpeed=cnDot3ExtnIfOperSpeed)
