#
# PySNMP MIB module TPLINK-STATICARP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/tplink/TPLINK-STATICARP-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:36:26 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
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
mibBuilder.exportSymbols("TPLINK-STATICARP-MIB", tpStaticArpItemInterfaceName=tpStaticArpItemInterfaceName, PYSNMP_MODULE_ID=tplinkStaticARPMIB, MacAddress=MacAddress, tplinkStaticARPMIBObjects=tplinkStaticARPMIBObjects, tplinkStaticARPMIB=tplinkStaticARPMIB, tpStaticARPItemIp=tpStaticARPItemIp, tpStaticARPConfigEntry=tpStaticARPConfigEntry, tpStaticARPItemStatus=tpStaticARPItemStatus, tpStaticARPConfigTable=tpStaticARPConfigTable, tpStaticARPItemMac=tpStaticARPItemMac, tpStaticARPConfig=tpStaticARPConfig, tplinkStaticARPNotifications=tplinkStaticARPNotifications)
