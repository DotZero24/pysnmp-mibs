#
# PySNMP MIB module ADTRAN-SHARED-DHCP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/adtran/ADTRAN-SHARED-DHCP-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:53:29 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
adShared, adIdentityShared = mibBuilder.importSymbols("ADTRAN-MIB", "adShared", "adIdentityShared")
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
adDhcpIdentity = ModuleIdentity((1, 3, 6, 1, 4, 1, 664, 6, 10000, 80))
adDhcpIdentity.setRevisions(('2009-09-22 00:00',))
if mibBuilder.loadTexts: adDhcpIdentity.setLastUpdated('200909220000Z')
if mibBuilder.loadTexts: adDhcpIdentity.setOrganization('Adtran, Inc.')
adDHCP = MibIdentifier((1, 3, 6, 1, 4, 1, 664, 5, 80))
adGenDhcpClient = MibIdentifier((1, 3, 6, 1, 4, 1, 664, 5, 80, 1))
adGenDhcpClientId = MibIdentifier((1, 3, 6, 1, 4, 1, 664, 6, 10000, 80, 1))
mibBuilder.exportSymbols("ADTRAN-SHARED-DHCP-MIB", PYSNMP_MODULE_ID=adDhcpIdentity, adDhcpIdentity=adDhcpIdentity, adGenDhcpClient=adGenDhcpClient, adDHCP=adDHCP, adGenDhcpClientId=adGenDhcpClientId)
