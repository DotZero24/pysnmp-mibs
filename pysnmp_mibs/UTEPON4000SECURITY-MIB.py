#
# PySNMP MIB module UTEPON4000SECURITY-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/utstarcom/UTEPON4000SECURITY-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:33:42 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
Timeout, MacAddress, BridgeId = mibBuilder.importSymbols("BRIDGE-MIB", "Timeout", "MacAddress", "BridgeId")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TruthValue, RowStatus, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "RowStatus", "TextualConvention", "DisplayString")
utsGeponBBS4000, = mibBuilder.importSymbols("UTS-BBS-COMMON-MIB", "utsGeponBBS4000")
utsGeponBBS4000Security = ModuleIdentity((1, 3, 6, 1, 4, 1, 1949, 1, 3, 10, 200, 6, 5))
if mibBuilder.loadTexts: utsGeponBBS4000Security.setLastUpdated('9407272253Z')
if mibBuilder.loadTexts: utsGeponBBS4000Security.setOrganization('UTSTARcom Inc')
utsEfmPonSecurityExt = MibIdentifier((1, 3, 6, 1, 4, 1, 1949, 1, 3, 10, 200, 6, 5, 1))
utsEponSecExtObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 1949, 1, 3, 10, 200, 6, 5, 1, 1))
utsDot3SecurityMIB = MibIdentifier((1, 3, 6, 1, 4, 1, 1949, 1, 3, 10, 200, 6, 5, 1, 1, 1))
utsDot3SecurityObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 1949, 1, 3, 10, 200, 6, 5, 1, 1, 1, 1))
utsDot3SecurityOltObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 1949, 1, 3, 10, 200, 6, 5, 1, 1, 1, 1, 1))
mibBuilder.exportSymbols("UTEPON4000SECURITY-MIB", utsDot3SecurityObjects=utsDot3SecurityObjects, utsEponSecExtObjects=utsEponSecExtObjects, utsEfmPonSecurityExt=utsEfmPonSecurityExt, utsGeponBBS4000Security=utsGeponBBS4000Security, PYSNMP_MODULE_ID=utsGeponBBS4000Security, utsDot3SecurityMIB=utsDot3SecurityMIB, utsDot3SecurityOltObjects=utsDot3SecurityOltObjects)
