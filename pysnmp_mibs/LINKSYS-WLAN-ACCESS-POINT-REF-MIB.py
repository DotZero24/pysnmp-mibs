#
# PySNMP MIB module LINKSYS-WLAN-ACCESS-POINT-REF-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/linksys/LINKSYS-WLAN-ACCESS-POINT-REF-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 11:12:04 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, enterprises, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "enterprises", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
linksys = ModuleIdentity((1, 3, 6, 1, 4, 1, 3955))
linksys.setRevisions(('2014-04-09 12:00',))
if mibBuilder.loadTexts: linksys.setLastUpdated('201404090000Z')
if mibBuilder.loadTexts: linksys.setOrganization('Linksys, LLC. Corporation')
smb = MibIdentifier((1, 3, 6, 1, 4, 1, 3955, 1000))
mibBuilder.exportSymbols("LINKSYS-WLAN-ACCESS-POINT-REF-MIB", linksys=linksys, PYSNMP_MODULE_ID=linksys, smb=smb)
