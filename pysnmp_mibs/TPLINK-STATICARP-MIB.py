#
# PySNMP MIB module TPLINK-STATICARP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/tplink/TPLINK-STATICARP-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 11:01:50 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, Counter32, Counter64, TimeTicks, ModuleIdentity, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "Counter32", "Counter64", "TimeTicks", "ModuleIdentity", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
tplinkMgmt, = mibBuilder.importSymbols("TPLINK-MIB", "tplinkMgmt")
TPRowStatus, = mibBuilder.importSymbols("TPLINK-TC-MIB", "TPRowStatus")
class MacAddress(OctetString):
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(6, 6)
    fixedLength = 6

tplinkStaticARPMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 11863, 6, 54))
tplinkStaticARPMIB.setRevisions(('2014-11-24 14:42',))
if mibBuilder.loadTexts: tplinkStaticARPMIB.setLastUpdated('201411241442Z')
if mibBuilder.loadTexts: tplinkStaticARPMIB.setOrganization('TPLINK')
tplinkStaticARPMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 11863, 6, 54, 1))
tplinkStaticARPNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 11863, 6, 54, 2))
tpStaticARPConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 11863, 6, 54, 1, 1))
tpStaticARPConfigTable = MibTable((1, 3, 6, 1, 4, 1, 11863, 6, 54, 1, 1, 1), )
if mibBuilder.loadTexts: tpStaticARPConfigTable.setStatus('current')
tpStaticARPConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11863, 6, 54, 1, 1, 1, 1), ).setIndexNames((0, "TPLINK-STATICARP-MIB", "tpStaticARPItemIp"))
if mibBuilder.loadTexts: tpStaticARPConfigEntry.setStatus('current')
tpStaticARPItemIp = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 54, 1, 1, 1, 1, 1), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tpStaticARPItemIp.setStatus('current')
tpStaticARPItemMac = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 54, 1, 1, 1, 1, 2), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 20))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: tpStaticARPItemMac.setStatus('current')
tpStaticArpItemInterfaceName = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 54, 1, 1, 1, 1, 3), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: tpStaticArpItemInterfaceName.setStatus('current')
tpStaticARPItemStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 54, 1, 1, 1, 1, 4), TPRowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: tpStaticARPItemStatus.setStatus('current')
mibBuilder.exportSymbols("TPLINK-STATICARP-MIB", PYSNMP_MODULE_ID=tplinkStaticARPMIB, tpStaticARPItemMac=tpStaticARPItemMac, tpStaticArpItemInterfaceName=tpStaticArpItemInterfaceName, tpStaticARPItemStatus=tpStaticARPItemStatus, tpStaticARPItemIp=tpStaticARPItemIp, MacAddress=MacAddress, tplinkStaticARPNotifications=tplinkStaticARPNotifications, tplinkStaticARPMIB=tplinkStaticARPMIB, tpStaticARPConfig=tpStaticARPConfig, tpStaticARPConfigEntry=tpStaticARPConfigEntry, tpStaticARPConfigTable=tpStaticARPConfigTable, tplinkStaticARPMIBObjects=tplinkStaticARPMIBObjects)
