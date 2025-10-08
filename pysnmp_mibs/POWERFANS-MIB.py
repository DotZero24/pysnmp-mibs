#
# PySNMP MIB module POWERFANS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/zte/POWERFANS-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:03:54 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, NotificationType, enterprises, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, NotificationType, iso, MibIdentifier, Integer32, mgmt, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "NotificationType", "enterprises", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "NotificationType", "iso", "MibIdentifier", "Integer32", "mgmt", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
zte = MibIdentifier((1, 3, 6, 1, 4, 1, 3902))
zxr10 = MibIdentifier((1, 3, 6, 1, 4, 1, 3902, 3))
class FanStatus(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("fan-online", 0), ("fan-offline", 1))

class PowerStatus(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("power-work", 0), ("power-online", 1), ("power-offline", 2))

class DisplayString(OctetString):
    pass

zxr10systemconfig = MibIdentifier((1, 3, 6, 1, 4, 1, 3902, 3, 1))
enviorment = MibIdentifier((1, 3, 6, 1, 4, 1, 3902, 3, 200))
fanTable = MibTable((1, 3, 6, 1, 4, 1, 3902, 3, 200, 1), )
if mibBuilder.loadTexts: fanTable.setStatus('current')
fanEntry = MibTableRow((1, 3, 6, 1, 4, 1, 3902, 3, 200, 1, 1), ).setIndexNames((0, "POWERFANS-MIB", "fanNo"))
if mibBuilder.loadTexts: fanEntry.setStatus('current')
fanNo = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 200, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fanNo.setStatus('current')
fanStat = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 200, 1, 1, 2), FanStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fanStat.setStatus('current')
fanRotateSpeed = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 200, 1, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fanRotateSpeed.setStatus('current')
powerTable = MibTable((1, 3, 6, 1, 4, 1, 3902, 3, 200, 2), )
if mibBuilder.loadTexts: powerTable.setStatus('current')
powerEntry = MibTableRow((1, 3, 6, 1, 4, 1, 3902, 3, 200, 2, 1), ).setIndexNames((0, "POWERFANS-MIB", "powerNo"))
if mibBuilder.loadTexts: powerEntry.setStatus('current')
powerNo = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 200, 2, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: powerNo.setStatus('current')
powerStat = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 200, 2, 1, 2), PowerStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: powerStat.setStatus('current')
powerTemperature = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 200, 2, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: powerTemperature.setStatus('current')
mibBuilder.exportSymbols("POWERFANS-MIB", zte=zte, enviorment=enviorment, fanStat=fanStat, powerEntry=powerEntry, FanStatus=FanStatus, powerNo=powerNo, fanTable=fanTable, fanRotateSpeed=fanRotateSpeed, powerTemperature=powerTemperature, powerStat=powerStat, PowerStatus=PowerStatus, powerTable=powerTable, fanEntry=fanEntry, DisplayString=DisplayString, zxr10=zxr10, fanNo=fanNo, zxr10systemconfig=zxr10systemconfig)
