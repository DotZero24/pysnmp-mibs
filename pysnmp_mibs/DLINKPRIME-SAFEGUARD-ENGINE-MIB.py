#
# PySNMP MIB module DLINKPRIME-SAFEGUARD-ENGINE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/d-link/DLINKPRIME-SAFEGUARD-ENGINE-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:58:15 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
dlinkPrimeCommon, = mibBuilder.importSymbols("DLINK-ID-REC-MIB", "dlinkPrimeCommon")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
MibIdentifier, NotificationType, Integer32, Bits, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Integer32", "Bits", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TruthValue, RowStatus, DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "RowStatus", "DisplayString", "TextualConvention")
dlinkPrimeSafeguardEngineMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 171, 15, 14))
dlinkPrimeSafeguardEngineMIB.setRevisions(('2014-04-26 00:00',))
if mibBuilder.loadTexts: dlinkPrimeSafeguardEngineMIB.setLastUpdated('201404260000Z')
if mibBuilder.loadTexts: dlinkPrimeSafeguardEngineMIB.setOrganization('D-Link Corp.')
dpSafeguardEngineMIBNotif = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 15, 14, 0))
dpSafeguardEngineMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 15, 14, 1))
dpSafeguardEngineMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 15, 14, 2))
dpSafeguardEngineState = MibScalar((1, 3, 6, 1, 4, 1, 171, 15, 14, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2))).clone('disable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dpSafeguardEngineState.setStatus('current')
mibBuilder.exportSymbols("DLINKPRIME-SAFEGUARD-ENGINE-MIB", dlinkPrimeSafeguardEngineMIB=dlinkPrimeSafeguardEngineMIB, dpSafeguardEngineMIBNotif=dpSafeguardEngineMIBNotif, dpSafeguardEngineMIBConformance=dpSafeguardEngineMIBConformance, dpSafeguardEngineState=dpSafeguardEngineState, PYSNMP_MODULE_ID=dlinkPrimeSafeguardEngineMIB, dpSafeguardEngineMIBObjects=dpSafeguardEngineMIBObjects)
