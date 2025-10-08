#
# PySNMP MIB module UTEPON4000SECURITY-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/utstarcom/UTEPON4000SECURITY-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:17:12 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
Timeout, MacAddress, BridgeId = mibBuilder.importSymbols("BRIDGE-MIB", "Timeout", "MacAddress", "BridgeId")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, Integer32, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, TimeTicks, Bits, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Integer32", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "TimeTicks", "Bits", "IpAddress")
DisplayString, TruthValue, RowStatus, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TruthValue", "RowStatus", "TextualConvention")
utsGeponBBS4000, = mibBuilder.importSymbols("UTS-BBS-COMMON-MIB", "utsGeponBBS4000")
utsGeponBBS4000Security = ModuleIdentity((1, 3, 6, 1, 4, 1, 1949, 1, 3, 10, 200, 6, 5))
if mibBuilder.loadTexts: utsGeponBBS4000Security.setLastUpdated('9407272253Z')
if mibBuilder.loadTexts: utsGeponBBS4000Security.setOrganization('UTSTARcom Inc')
utsEfmPonSecurityExt = MibIdentifier((1, 3, 6, 1, 4, 1, 1949, 1, 3, 10, 200, 6, 5, 1))
utsEponSecExtObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 1949, 1, 3, 10, 200, 6, 5, 1, 1))
utsDot3SecurityMIB = MibIdentifier((1, 3, 6, 1, 4, 1, 1949, 1, 3, 10, 200, 6, 5, 1, 1, 1))
utsDot3SecurityObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 1949, 1, 3, 10, 200, 6, 5, 1, 1, 1, 1))
utsDot3SecurityOltObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 1949, 1, 3, 10, 200, 6, 5, 1, 1, 1, 1, 1))
mibBuilder.exportSymbols("UTEPON4000SECURITY-MIB", utsEfmPonSecurityExt=utsEfmPonSecurityExt, utsGeponBBS4000Security=utsGeponBBS4000Security, PYSNMP_MODULE_ID=utsGeponBBS4000Security, utsDot3SecurityOltObjects=utsDot3SecurityOltObjects, utsEponSecExtObjects=utsEponSecExtObjects, utsDot3SecurityMIB=utsDot3SecurityMIB, utsDot3SecurityObjects=utsDot3SecurityObjects)
