#
# PySNMP MIB module EOAM-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/supermicro/EOAM-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:33:00 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, enterprises, Unsigned32, Gauge32, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "enterprises", "Unsigned32", "Gauge32", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
fseoam = ModuleIdentity((1, 3, 6, 1, 4, 1, 10876, 101, 1, 121))
fseoam.setRevisions(('2012-09-05 00:00',))
if mibBuilder.loadTexts: fseoam.setLastUpdated('201209050000Z')
if mibBuilder.loadTexts: fseoam.setOrganization('Super Micro Computer Inc.')
class EoamOui(TextualConvention, OctetString):
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(3, 3)
    fixedLength = 3

fsEoamSystem = MibIdentifier((1, 3, 6, 1, 4, 1, 10876, 101, 1, 121, 1))
fsEoamSystemControl = MibScalar((1, 3, 6, 1, 4, 1, 10876, 101, 1, 121, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("start", 1), ("shutdown", 2))).clone('start')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: fsEoamSystemControl.setStatus('current')
fsEoamModuleStatus = MibScalar((1, 3, 6, 1, 4, 1, 10876, 101, 1, 121, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2))).clone('disabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: fsEoamModuleStatus.setStatus('current')
fsEoamErrorEventResend = MibScalar((1, 3, 6, 1, 4, 1, 10876, 101, 1, 121, 1, 3), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 10)).clone(10)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: fsEoamErrorEventResend.setStatus('current')
fsEoamOui = MibScalar((1, 3, 6, 1, 4, 1, 10876, 101, 1, 121, 1, 4), EoamOui()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: fsEoamOui.setStatus('current')
fsEoamTraceOption = MibScalar((1, 3, 6, 1, 4, 1, 10876, 101, 1, 121, 1, 5), Integer32().clone(262144)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: fsEoamTraceOption.setStatus('current')
mibBuilder.exportSymbols("EOAM-MIB", fsEoamSystem=fsEoamSystem, fsEoamOui=fsEoamOui, EoamOui=EoamOui, fsEoamErrorEventResend=fsEoamErrorEventResend, fseoam=fseoam, fsEoamSystemControl=fsEoamSystemControl, fsEoamTraceOption=fsEoamTraceOption, fsEoamModuleStatus=fsEoamModuleStatus, PYSNMP_MODULE_ID=fseoam)
