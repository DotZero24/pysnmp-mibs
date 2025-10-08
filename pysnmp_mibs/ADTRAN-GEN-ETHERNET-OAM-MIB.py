#
# PySNMP MIB module ADTRAN-GEN-ETHERNET-OAM-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/adtran/ADTRAN-GEN-ETHERNET-OAM-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:53:17 2025
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
adGenEthernetOAMIdentity = ModuleIdentity((1, 3, 6, 1, 4, 1, 664, 6, 10000, 75))
adGenEthernetOAMIdentity.setRevisions(('2011-06-10 08:00',))
if mibBuilder.loadTexts: adGenEthernetOAMIdentity.setLastUpdated('201106100800Z')
if mibBuilder.loadTexts: adGenEthernetOAMIdentity.setOrganization('ADTRAN, Inc.')
adGenEthernetOAM = MibIdentifier((1, 3, 6, 1, 4, 1, 664, 5, 75))
adGenEthernetCfm = MibIdentifier((1, 3, 6, 1, 4, 1, 664, 5, 75, 1))
adGenEthernetCfmID = MibIdentifier((1, 3, 6, 1, 4, 1, 664, 6, 10000, 75, 1))
adGenY1731 = MibIdentifier((1, 3, 6, 1, 4, 1, 664, 5, 75, 2))
adGenY1731ID = MibIdentifier((1, 3, 6, 1, 4, 1, 664, 6, 10000, 75, 2))
mibBuilder.exportSymbols("ADTRAN-GEN-ETHERNET-OAM-MIB", adGenEthernetOAM=adGenEthernetOAM, adGenY1731ID=adGenY1731ID, adGenEthernetOAMIdentity=adGenEthernetOAMIdentity, adGenEthernetCfm=adGenEthernetCfm, adGenEthernetCfmID=adGenEthernetCfmID, adGenY1731=adGenY1731, PYSNMP_MODULE_ID=adGenEthernetOAMIdentity)
