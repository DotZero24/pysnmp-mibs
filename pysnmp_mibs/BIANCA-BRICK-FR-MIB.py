#
# PySNMP MIB module BIANCA-BRICK-FR-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/bintec/BIANCA-BRICK-FR-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 09:57:27 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, enterprises, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "enterprises", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
bintec = MibIdentifier((1, 3, 6, 1, 4, 1, 272))
bibo = MibIdentifier((1, 3, 6, 1, 4, 1, 272, 4))
fr = MibIdentifier((1, 3, 6, 1, 4, 1, 272, 4, 13))
frMprTable = MibTable((1, 3, 6, 1, 4, 1, 272, 4, 13, 1), )
if mibBuilder.loadTexts: frMprTable.setStatus('mandatory')
frMprEntry = MibTableRow((1, 3, 6, 1, 4, 1, 272, 4, 13, 1, 1), ).setIndexNames((0, "BIANCA-BRICK-FR-MIB", "frMprIfIndex"))
if mibBuilder.loadTexts: frMprEntry.setStatus('mandatory')
frMprIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 272, 4, 13, 1, 1, 1), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: frMprIfIndex.setStatus('mandatory')
frMprMtu = MibTableColumn((1, 3, 6, 1, 4, 1, 272, 4, 13, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(576, 8180)).clone(1500)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: frMprMtu.setStatus('mandatory')
frMprEncapsulation = MibTableColumn((1, 3, 6, 1, 4, 1, 272, 4, 13, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 7))).clone(namedValues=NamedValues(("mpr", 1), ("delete", 7))).clone('mpr')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: frMprEncapsulation.setStatus('mandatory')
frMprIfcType = MibTableColumn((1, 3, 6, 1, 4, 1, 272, 4, 13, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("multipoint", 1), ("point-to-point", 2))).clone('point-to-point')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: frMprIfcType.setStatus('mandatory')
frMprInverseArp = MibTableColumn((1, 3, 6, 1, 4, 1, 272, 4, 13, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2))).clone('disabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: frMprInverseArp.setStatus('mandatory')
mibBuilder.exportSymbols("BIANCA-BRICK-FR-MIB", frMprEncapsulation=frMprEncapsulation, frMprInverseArp=frMprInverseArp, frMprIfcType=frMprIfcType, bintec=bintec, bibo=bibo, frMprEntry=frMprEntry, frMprIfIndex=frMprIfIndex, frMprTable=frMprTable, frMprMtu=frMprMtu, fr=fr)
