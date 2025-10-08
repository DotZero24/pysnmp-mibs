#
# PySNMP MIB module ZXR10-X25-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/zte/ZXR10-X25-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:10:45 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, enterprises, NotificationType, Integer32, Bits, Unsigned32, mgmt, NotificationType, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "enterprises", "NotificationType", "Integer32", "Bits", "Unsigned32", "mgmt", "NotificationType", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
RowStatus, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "TextualConvention", "DisplayString")
zte = MibIdentifier((1, 3, 6, 1, 4, 1, 3902))
zxr10 = MibIdentifier((1, 3, 6, 1, 4, 1, 3902, 3))
zxr10X25 = MibIdentifier((1, 3, 6, 1, 4, 1, 3902, 3, 4000))
class DisplayString(OctetString):
    pass

zxr10X25OprTable = MibTable((1, 3, 6, 1, 4, 1, 3902, 3, 4000, 1), )
if mibBuilder.loadTexts: zxr10X25OprTable.setStatus('current')
zxr10X25OprEntry = MibTableRow((1, 3, 6, 1, 4, 1, 3902, 3, 4000, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: zxr10X25OprEntry.setStatus('current')
zxr10X25OprXconnenctIfName = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 4000, 1, 1, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: zxr10X25OprXconnenctIfName.setStatus('current')
zxr10X25OprLocalswitchIfName = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 4000, 1, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: zxr10X25OprLocalswitchIfName.setStatus('current')
zxr10X25OprDLCI = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 4000, 1, 1, 3), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: zxr10X25OprDLCI.setStatus('current')
zxr10X25OprType = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 4000, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("localswitch", 1), ("xconnect", 2), ("both", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: zxr10X25OprType.setStatus('current')
zxr10X25OprStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 4000, 1, 1, 5), RowStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: zxr10X25OprStatus.setStatus('current')
mibBuilder.exportSymbols("ZXR10-X25-MIB", zxr10X25OprXconnenctIfName=zxr10X25OprXconnenctIfName, zxr10X25OprEntry=zxr10X25OprEntry, zxr10X25=zxr10X25, DisplayString=DisplayString, zxr10X25OprDLCI=zxr10X25OprDLCI, zxr10X25OprLocalswitchIfName=zxr10X25OprLocalswitchIfName, zte=zte, zxr10X25OprStatus=zxr10X25OprStatus, zxr10X25OprTable=zxr10X25OprTable, zxr10=zxr10, zxr10X25OprType=zxr10X25OprType)
