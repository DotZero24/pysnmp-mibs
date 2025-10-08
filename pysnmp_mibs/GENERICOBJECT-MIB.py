#
# PySNMP MIB module GENERICOBJECT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/cisco/GENERICOBJECT-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:14:31 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
cardGeneric, = mibBuilder.importSymbols("BASIS-MIB", "cardGeneric")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
genericObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 351, 110, 2, 8))
genericLineNum = MibScalar((1, 3, 6, 1, 4, 1, 351, 110, 2, 8, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: genericLineNum.setStatus('mandatory')
genericLineType = MibScalar((1, 3, 6, 1, 4, 1, 351, 110, 2, 8, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 51, 52, 53, 54, 55, 56, 101, 102, 151, 152, 153, 154))).clone(namedValues=NamedValues(("dsx1ESF", 1), ("dsx1D4", 2), ("dsx1E1", 3), ("dsx1E1CRC", 4), ("dsx1E1MF", 5), ("dsx1E1CRC-MF", 6), ("dsx1E1clearchannel", 7), ("dsx3CbitParity", 51), ("dsx3g832-g804", 52), ("dsx3m13mode", 53), ("dsx3g751", 54), ("dsx3Unframed", 55), ("e3Unframed", 56), ("x21dte", 101), ("x21dce", 102), ("sonetSts3c", 151), ("sonetStm1", 152), ("sonetSts12c", 153), ("sonetStm4", 154)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: genericLineType.setStatus('mandatory')
genericTimeStamp = MibScalar((1, 3, 6, 1, 4, 1, 351, 110, 2, 8, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 30))).setMaxAccess("readonly")
if mibBuilder.loadTexts: genericTimeStamp.setStatus('mandatory')
mibBuilder.exportSymbols("GENERICOBJECT-MIB", genericLineNum=genericLineNum, genericLineType=genericLineType, genericObjects=genericObjects, genericTimeStamp=genericTimeStamp)
