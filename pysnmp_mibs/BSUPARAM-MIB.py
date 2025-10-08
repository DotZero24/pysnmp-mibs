#
# PySNMP MIB module BSUPARAM-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/aperto/BSUPARAM-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:07:54 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
bsu, = mibBuilder.importSymbols("ANIROOT-MIB", "bsu")
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
aniBsuParam = ModuleIdentity((1, 3, 6, 1, 4, 1, 4325, 3, 8))
if mibBuilder.loadTexts: aniBsuParam.setLastUpdated('0111121130Z')
if mibBuilder.loadTexts: aniBsuParam.setOrganization('Aperto Networks')
aniBsuDhcpParamSource = MibScalar((1, 3, 6, 1, 4, 1, 4325, 3, 8, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("local", 1), ("server", 2))).clone('server')).setMaxAccess("readonly")
if mibBuilder.loadTexts: aniBsuDhcpParamSource.setStatus('current')
mibBuilder.exportSymbols("BSUPARAM-MIB", aniBsuDhcpParamSource=aniBsuDhcpParamSource, aniBsuParam=aniBsuParam, PYSNMP_MODULE_ID=aniBsuParam)
