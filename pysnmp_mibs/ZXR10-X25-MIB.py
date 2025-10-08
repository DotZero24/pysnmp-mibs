#
# PySNMP MIB module ZXR10-X25-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/zte/ZXR10-X25-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:03:57 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, NotificationType, enterprises, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, NotificationType, iso, MibIdentifier, Integer32, mgmt, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "NotificationType", "enterprises", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "NotificationType", "iso", "MibIdentifier", "Integer32", "mgmt", "Bits", "TimeTicks", "IpAddress")
DisplayString, RowStatus, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "RowStatus", "TextualConvention")
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
mibBuilder.exportSymbols("ZXR10-X25-MIB", zte=zte, zxr10X25OprXconnenctIfName=zxr10X25OprXconnenctIfName, zxr10X25OprType=zxr10X25OprType, zxr10X25OprStatus=zxr10X25OprStatus, zxr10X25=zxr10X25, zxr10X25OprEntry=zxr10X25OprEntry, zxr10X25OprDLCI=zxr10X25OprDLCI, zxr10X25OprTable=zxr10X25OprTable, DisplayString=DisplayString, zxr10=zxr10, zxr10X25OprLocalswitchIfName=zxr10X25OprLocalswitchIfName)
