#
# PySNMP MIB module BIANCA-BRICK-FR-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/bintec/BIANCA-BRICK-FR-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 09:59:00 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, enterprises, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, Counter64, TimeTicks, ModuleIdentity, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "enterprises", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "Counter64", "TimeTicks", "ModuleIdentity", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
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
mibBuilder.exportSymbols("BIANCA-BRICK-FR-MIB", frMprIfIndex=frMprIfIndex, bintec=bintec, fr=fr, frMprInverseArp=frMprInverseArp, frMprMtu=frMprMtu, frMprEncapsulation=frMprEncapsulation, frMprEntry=frMprEntry, frMprIfcType=frMprIfcType, frMprTable=frMprTable, bibo=bibo)
