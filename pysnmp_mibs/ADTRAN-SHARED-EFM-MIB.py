#
# PySNMP MIB module ADTRAN-SHARED-EFM-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/adtran/ADTRAN-SHARED-EFM-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:29:44 2025
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
mibBuilder.exportSymbols("ADTRAN-SHARED-EFM-MIB", adGenEfmExt=adGenEfmExt, adGenEfmExtID=adGenEfmExtID, PYSNMP_MODULE_ID=adEfmIdentity, adEfmIdentity=adEfmIdentity, adEfm=adEfm, adGenEfmNtu=adGenEfmNtu, adGenEfmID=adGenEfmID, adGenEfm=adGenEfm, adGenEfmNtuID=adGenEfmNtuID)
