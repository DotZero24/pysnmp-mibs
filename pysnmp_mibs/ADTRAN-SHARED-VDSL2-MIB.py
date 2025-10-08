#
# PySNMP MIB module ADTRAN-SHARED-VDSL2-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/adtran/ADTRAN-SHARED-VDSL2-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:52:54 2025
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
adVdsl2Identity = ModuleIdentity((1, 3, 6, 1, 4, 1, 664, 6, 10000, 65))
adVdsl2Identity.setRevisions(('2008-07-08 00:00',))
if mibBuilder.loadTexts: adVdsl2Identity.setLastUpdated('200807080000Z')
if mibBuilder.loadTexts: adVdsl2Identity.setOrganization('Adtran, Inc.')
adVdsl2 = MibIdentifier((1, 3, 6, 1, 4, 1, 664, 5, 65))
adGenVdsl2 = MibIdentifier((1, 3, 6, 1, 4, 1, 664, 5, 65, 1))
adGenVdsl2ID = MibIdentifier((1, 3, 6, 1, 4, 1, 664, 6, 10000, 65, 1))
mibBuilder.exportSymbols("ADTRAN-SHARED-VDSL2-MIB", adGenVdsl2ID=adGenVdsl2ID, adVdsl2Identity=adVdsl2Identity, adVdsl2=adVdsl2, PYSNMP_MODULE_ID=adVdsl2Identity, adGenVdsl2=adGenVdsl2)
