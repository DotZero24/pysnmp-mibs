#
# PySNMP MIB module BSUPARAM-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/aperto/BSUPARAM-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:17:17 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
bsu, = mibBuilder.importSymbols("ANIROOT-MIB", "bsu")
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
aniBsuParam = ModuleIdentity((1, 3, 6, 1, 4, 1, 4325, 3, 8))
if mibBuilder.loadTexts: aniBsuParam.setLastUpdated('0111121130Z')
if mibBuilder.loadTexts: aniBsuParam.setOrganization('Aperto Networks')
aniBsuDhcpParamSource = MibScalar((1, 3, 6, 1, 4, 1, 4325, 3, 8, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("local", 1), ("server", 2))).clone('server')).setMaxAccess("readonly")
if mibBuilder.loadTexts: aniBsuDhcpParamSource.setStatus('current')
mibBuilder.exportSymbols("BSUPARAM-MIB", PYSNMP_MODULE_ID=aniBsuParam, aniBsuParam=aniBsuParam, aniBsuDhcpParamSource=aniBsuDhcpParamSource)
