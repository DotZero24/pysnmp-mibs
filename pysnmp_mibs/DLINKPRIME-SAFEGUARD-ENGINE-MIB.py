#
# PySNMP MIB module DLINKPRIME-SAFEGUARD-ENGINE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/d-link/DLINKPRIME-SAFEGUARD-ENGINE-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:33:42 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
dlinkPrimeCommon, = mibBuilder.importSymbols("DLINK-ID-REC-MIB", "dlinkPrimeCommon")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TruthValue, RowStatus, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TruthValue", "RowStatus", "TextualConvention")
dlinkPrimeSafeguardEngineMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 171, 15, 14))
dlinkPrimeSafeguardEngineMIB.setRevisions(('2014-04-26 00:00',))
if mibBuilder.loadTexts: dlinkPrimeSafeguardEngineMIB.setLastUpdated('201404260000Z')
if mibBuilder.loadTexts: dlinkPrimeSafeguardEngineMIB.setOrganization('D-Link Corp.')
dpSafeguardEngineMIBNotif = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 15, 14, 0))
dpSafeguardEngineMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 15, 14, 1))
dpSafeguardEngineMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 15, 14, 2))
dpSafeguardEngineState = MibScalar((1, 3, 6, 1, 4, 1, 171, 15, 14, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2))).clone('disable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dpSafeguardEngineState.setStatus('current')
mibBuilder.exportSymbols("DLINKPRIME-SAFEGUARD-ENGINE-MIB", dpSafeguardEngineMIBConformance=dpSafeguardEngineMIBConformance, dpSafeguardEngineState=dpSafeguardEngineState, dlinkPrimeSafeguardEngineMIB=dlinkPrimeSafeguardEngineMIB, dpSafeguardEngineMIBNotif=dpSafeguardEngineMIBNotif, dpSafeguardEngineMIBObjects=dpSafeguardEngineMIBObjects, PYSNMP_MODULE_ID=dlinkPrimeSafeguardEngineMIB)
