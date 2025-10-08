#
# PySNMP MIB module ADTRAN-SHARED-EFM-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/adtran/ADTRAN-SHARED-EFM-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:53:04 2025
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
adEfmIdentity = ModuleIdentity((1, 3, 6, 1, 4, 1, 664, 6, 10000, 66))
adEfmIdentity.setRevisions(('2007-04-05 00:00',))
if mibBuilder.loadTexts: adEfmIdentity.setLastUpdated('200704050000Z')
if mibBuilder.loadTexts: adEfmIdentity.setOrganization('Adtran, Inc.')
adEfm = MibIdentifier((1, 3, 6, 1, 4, 1, 664, 5, 66))
adGenEfm = MibIdentifier((1, 3, 6, 1, 4, 1, 664, 5, 66, 1))
adGenEfmID = MibIdentifier((1, 3, 6, 1, 4, 1, 664, 6, 10000, 66, 1))
adGenEfmNtu = MibIdentifier((1, 3, 6, 1, 4, 1, 664, 5, 66, 2))
adGenEfmNtuID = MibIdentifier((1, 3, 6, 1, 4, 1, 664, 6, 10000, 66, 2))
adGenEfmExt = MibIdentifier((1, 3, 6, 1, 4, 1, 664, 5, 66, 3))
adGenEfmExtID = MibIdentifier((1, 3, 6, 1, 4, 1, 664, 6, 10000, 66, 3))
mibBuilder.exportSymbols("ADTRAN-SHARED-EFM-MIB", adGenEfmExt=adGenEfmExt, adGenEfm=adGenEfm, adGenEfmNtu=adGenEfmNtu, adGenEfmExtID=adGenEfmExtID, adGenEfmID=adGenEfmID, PYSNMP_MODULE_ID=adEfmIdentity, adGenEfmNtuID=adGenEfmNtuID, adEfm=adEfm, adEfmIdentity=adEfmIdentity)
