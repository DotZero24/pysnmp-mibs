#
# PySNMP MIB module CISCO-DMN-DSG-DECODE-ENABLE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/cisco/CISCO-DMN-DSG-DECODE-ENABLE-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:11:16 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
ciscoDSGUtilities, = mibBuilder.importSymbols("CISCO-DMN-DSG-ROOT-MIB", "ciscoDSGUtilities")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoDSGDecodeEnable = ModuleIdentity((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 13))
ciscoDSGDecodeEnable.setRevisions(('2010-08-30 06:00', '2009-12-07 12:00',))
if mibBuilder.loadTexts: ciscoDSGDecodeEnable.setLastUpdated('201008300600Z')
if mibBuilder.loadTexts: ciscoDSGDecodeEnable.setOrganization('Cisco Systems, Inc.')
decodeEnableTable = MibTable((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 13, 1), )
if mibBuilder.loadTexts: decodeEnableTable.setStatus('current')
decodeEnableEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 13, 1, 1), ).setIndexNames((0, "CISCO-DMN-DSG-DECODE-ENABLE-MIB", "decodeType"))
if mibBuilder.loadTexts: decodeEnableEntry.setStatus('current')
decodeType = MibTableColumn((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 13, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14))).clone(namedValues=NamedValues(("video", 1), ("audio1", 2), ("audio2", 3), ("audio3", 4), ("audio4", 5), ("vbi", 6), ("data", 7), ("mpe1", 8), ("mpe2", 9), ("mpe3", 10), ("mpe4", 11), ("mpe5", 12), ("stt", 13), ("dpi", 14))))
if mibBuilder.loadTexts: decodeType.setStatus('current')
decodeEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 13, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("no", 1), ("yes", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: decodeEnable.setStatus('current')
mibBuilder.exportSymbols("CISCO-DMN-DSG-DECODE-ENABLE-MIB", PYSNMP_MODULE_ID=ciscoDSGDecodeEnable, decodeEnableTable=decodeEnableTable, decodeEnableEntry=decodeEnableEntry, decodeType=decodeType, ciscoDSGDecodeEnable=ciscoDSGDecodeEnable, decodeEnable=decodeEnable)
