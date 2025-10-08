#
# PySNMP MIB module EOAM-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/supermicro/EOAM-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:57:24 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, enterprises, NotificationType, Integer32, Bits, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "enterprises", "NotificationType", "Integer32", "Bits", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
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
mibBuilder.exportSymbols("EOAM-MIB", fsEoamSystemControl=fsEoamSystemControl, EoamOui=EoamOui, fsEoamOui=fsEoamOui, fsEoamModuleStatus=fsEoamModuleStatus, PYSNMP_MODULE_ID=fseoam, fseoam=fseoam, fsEoamTraceOption=fsEoamTraceOption, fsEoamSystem=fsEoamSystem, fsEoamErrorEventResend=fsEoamErrorEventResend)
