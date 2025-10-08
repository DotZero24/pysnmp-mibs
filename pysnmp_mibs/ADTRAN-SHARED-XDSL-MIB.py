#
# PySNMP MIB module ADTRAN-SHARED-XDSL-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/adtran/ADTRAN-SHARED-XDSL-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:53:37 2025
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
adXdslIdentity = ModuleIdentity((1, 3, 6, 1, 4, 1, 664, 6, 10000, 73))
adXdslIdentity.setRevisions(('2010-06-10 00:00', '2008-07-17 00:00',))
if mibBuilder.loadTexts: adXdslIdentity.setLastUpdated('201006100000Z')
if mibBuilder.loadTexts: adXdslIdentity.setOrganization('Adtran, Inc.')
adXdsl = MibIdentifier((1, 3, 6, 1, 4, 1, 664, 5, 73))
adGenXdsl = MibIdentifier((1, 3, 6, 1, 4, 1, 664, 5, 73, 1))
adGenXdslID = MibIdentifier((1, 3, 6, 1, 4, 1, 664, 6, 10000, 73, 1))
adGenGeminax = MibIdentifier((1, 3, 6, 1, 4, 1, 664, 5, 73, 2))
adGenGeminaxID = MibIdentifier((1, 3, 6, 1, 4, 1, 664, 6, 10000, 73, 2))
mibBuilder.exportSymbols("ADTRAN-SHARED-XDSL-MIB", adGenXdslID=adGenXdslID, adGenGeminaxID=adGenGeminaxID, adXdsl=adXdsl, adXdslIdentity=adXdslIdentity, adGenGeminax=adGenGeminax, adGenXdsl=adGenXdsl, PYSNMP_MODULE_ID=adXdslIdentity)
