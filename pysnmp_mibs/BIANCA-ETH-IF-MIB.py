#
# PySNMP MIB module BIANCA-ETH-IF-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/bintec/BIANCA-ETH-IF-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 09:58:56 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, enterprises, NotificationType, Bits, Integer32, Unsigned32, iso, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, Counter32, Counter64, TimeTicks, ModuleIdentity, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "enterprises", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "Counter32", "Counter64", "TimeTicks", "ModuleIdentity", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
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
mibBuilder.exportSymbols("BIANCA-ETH-IF-MIB", HexValue=HexValue, eth=eth, bintec=bintec, PhysAddress=PhysAddress, ethIfMACSlot=ethIfMACSlot, ethIfPortGroup=ethIfPortGroup, Date=Date, ethIfTable=ethIfTable, ethIfIndex=ethIfIndex, ethIfAdminStatus=ethIfAdminStatus, bibo=bibo, ethIfMACUnit=ethIfMACUnit, ethIfEntry=ethIfEntry)
