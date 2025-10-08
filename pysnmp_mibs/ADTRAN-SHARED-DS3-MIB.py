#
# PySNMP MIB module ADTRAN-SHARED-DS3-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/adtran/ADTRAN-SHARED-DS3-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:53:22 2025
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
adDS3Identity = ModuleIdentity((1, 3, 6, 1, 4, 1, 664, 6, 10000, 74))
adDS3Identity.setRevisions(('2008-04-24 00:00',))
if mibBuilder.loadTexts: adDS3Identity.setLastUpdated('200704240000Z')
if mibBuilder.loadTexts: adDS3Identity.setOrganization('Adtran, Inc.')
adDS3 = MibIdentifier((1, 3, 6, 1, 4, 1, 664, 5, 74))
adGenDS3Test = MibIdentifier((1, 3, 6, 1, 4, 1, 664, 5, 74, 1))
adGenDS3TestID = MibIdentifier((1, 3, 6, 1, 4, 1, 664, 6, 10000, 74, 1))
mibBuilder.exportSymbols("ADTRAN-SHARED-DS3-MIB", adDS3Identity=adDS3Identity, PYSNMP_MODULE_ID=adDS3Identity, adGenDS3TestID=adGenDS3TestID, adGenDS3Test=adGenDS3Test, adDS3=adDS3)
