#
# PySNMP MIB module ADTRAN-GEN-ETHERNET-OAM-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/adtran/ADTRAN-GEN-ETHERNET-OAM-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:29:51 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
adShared, adIdentityShared = mibBuilder.importSymbols("ADTRAN-MIB", "adShared", "adIdentityShared")
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
adGenEthernetOAMIdentity = ModuleIdentity((1, 3, 6, 1, 4, 1, 664, 6, 10000, 75))
adGenEthernetOAMIdentity.setRevisions(('2011-06-10 08:00',))
if mibBuilder.loadTexts: adGenEthernetOAMIdentity.setLastUpdated('201106100800Z')
if mibBuilder.loadTexts: adGenEthernetOAMIdentity.setOrganization('ADTRAN, Inc.')
adGenEthernetOAM = MibIdentifier((1, 3, 6, 1, 4, 1, 664, 5, 75))
adGenEthernetCfm = MibIdentifier((1, 3, 6, 1, 4, 1, 664, 5, 75, 1))
adGenEthernetCfmID = MibIdentifier((1, 3, 6, 1, 4, 1, 664, 6, 10000, 75, 1))
adGenY1731 = MibIdentifier((1, 3, 6, 1, 4, 1, 664, 5, 75, 2))
adGenY1731ID = MibIdentifier((1, 3, 6, 1, 4, 1, 664, 6, 10000, 75, 2))
mibBuilder.exportSymbols("ADTRAN-GEN-ETHERNET-OAM-MIB", adGenEthernetCfm=adGenEthernetCfm, adGenEthernetCfmID=adGenEthernetCfmID, adGenY1731ID=adGenY1731ID, adGenEthernetOAM=adGenEthernetOAM, adGenY1731=adGenY1731, PYSNMP_MODULE_ID=adGenEthernetOAMIdentity, adGenEthernetOAMIdentity=adGenEthernetOAMIdentity)
