#
# PySNMP MIB module BIANCA-ETH-IF-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/bintec/BIANCA-ETH-IF-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 09:57:25 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, Integer32, enterprises, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, TimeTicks, Bits, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Integer32", "enterprises", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "TimeTicks", "Bits", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
bintec = MibIdentifier((1, 3, 6, 1, 4, 1, 272))
bibo = MibIdentifier((1, 3, 6, 1, 4, 1, 272, 4))
eth = MibIdentifier((1, 3, 6, 1, 4, 1, 272, 4, 37))
class Date(Integer32):
    pass

class HexValue(Integer32):
    pass

class PhysAddress(OctetString):
    pass

ethIfTable = MibTable((1, 3, 6, 1, 4, 1, 272, 4, 37, 1), )
if mibBuilder.loadTexts: ethIfTable.setStatus('mandatory')
ethIfEntry = MibTableRow((1, 3, 6, 1, 4, 1, 272, 4, 37, 1, 1), ).setIndexNames((0, "BIANCA-ETH-IF-MIB", "ethIfIndex"))
if mibBuilder.loadTexts: ethIfEntry.setStatus('mandatory')
ethIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 272, 4, 37, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ethIfIndex.setStatus('mandatory')
ethIfPortGroup = MibTableColumn((1, 3, 6, 1, 4, 1, 272, 4, 37, 1, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 99))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ethIfPortGroup.setStatus('mandatory')
ethIfMACSlot = MibTableColumn((1, 3, 6, 1, 4, 1, 272, 4, 37, 1, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 9))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ethIfMACSlot.setStatus('mandatory')
ethIfMACUnit = MibTableColumn((1, 3, 6, 1, 4, 1, 272, 4, 37, 1, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 9))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ethIfMACUnit.setStatus('mandatory')
ethIfAdminStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 272, 4, 37, 1, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("down", 1), ("up", 2))).clone('down')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ethIfAdminStatus.setStatus('mandatory')
mibBuilder.exportSymbols("BIANCA-ETH-IF-MIB", ethIfAdminStatus=ethIfAdminStatus, ethIfIndex=ethIfIndex, ethIfMACUnit=ethIfMACUnit, eth=eth, Date=Date, ethIfPortGroup=ethIfPortGroup, PhysAddress=PhysAddress, bintec=bintec, bibo=bibo, ethIfEntry=ethIfEntry, ethIfMACSlot=ethIfMACSlot, ethIfTable=ethIfTable, HexValue=HexValue)
