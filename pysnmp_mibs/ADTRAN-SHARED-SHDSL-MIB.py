#
# PySNMP MIB module ADTRAN-SHARED-SHDSL-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/adtran/ADTRAN-SHARED-SHDSL-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:30:08 2025
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
adShdslIdentity = ModuleIdentity((1, 3, 6, 1, 4, 1, 664, 6, 10000, 59))
adShdslIdentity.setRevisions(('2007-04-06 00:00',))
if mibBuilder.loadTexts: adShdslIdentity.setLastUpdated('200704060000Z')
if mibBuilder.loadTexts: adShdslIdentity.setOrganization('Adtran, Inc.')
adSHDSL = MibIdentifier((1, 3, 6, 1, 4, 1, 664, 5, 59))
adGenEShdsl = MibIdentifier((1, 3, 6, 1, 4, 1, 664, 5, 59, 1))
adGenEShdslID = MibIdentifier((1, 3, 6, 1, 4, 1, 664, 6, 10000, 59, 1))
adGenDslProxy = MibIdentifier((1, 3, 6, 1, 4, 1, 664, 5, 59, 4))
adGenDslProxyID = MibIdentifier((1, 3, 6, 1, 4, 1, 664, 6, 10000, 59, 4))
mibBuilder.exportSymbols("ADTRAN-SHARED-SHDSL-MIB", adSHDSL=adSHDSL, PYSNMP_MODULE_ID=adShdslIdentity, adGenEShdsl=adGenEShdsl, adGenEShdslID=adGenEShdslID, adGenDslProxy=adGenDslProxy, adShdslIdentity=adShdslIdentity, adGenDslProxyID=adGenDslProxyID)
