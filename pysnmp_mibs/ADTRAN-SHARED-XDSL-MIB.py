#
# PySNMP MIB module ADTRAN-SHARED-XDSL-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/adtran/ADTRAN-SHARED-XDSL-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:30:05 2025
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
adXdslIdentity = ModuleIdentity((1, 3, 6, 1, 4, 1, 664, 6, 10000, 73))
adXdslIdentity.setRevisions(('2010-06-10 00:00', '2008-07-17 00:00',))
if mibBuilder.loadTexts: adXdslIdentity.setLastUpdated('201006100000Z')
if mibBuilder.loadTexts: adXdslIdentity.setOrganization('Adtran, Inc.')
adXdsl = MibIdentifier((1, 3, 6, 1, 4, 1, 664, 5, 73))
adGenXdsl = MibIdentifier((1, 3, 6, 1, 4, 1, 664, 5, 73, 1))
adGenXdslID = MibIdentifier((1, 3, 6, 1, 4, 1, 664, 6, 10000, 73, 1))
adGenGeminax = MibIdentifier((1, 3, 6, 1, 4, 1, 664, 5, 73, 2))
adGenGeminaxID = MibIdentifier((1, 3, 6, 1, 4, 1, 664, 6, 10000, 73, 2))
mibBuilder.exportSymbols("ADTRAN-SHARED-XDSL-MIB", adGenXdsl=adGenXdsl, adGenGeminax=adGenGeminax, adXdslIdentity=adXdslIdentity, PYSNMP_MODULE_ID=adXdslIdentity, adXdsl=adXdsl, adGenGeminaxID=adGenGeminaxID, adGenXdslID=adGenXdslID)
