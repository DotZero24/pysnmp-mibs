#
# PySNMP MIB module POWERFANS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/zte/POWERFANS-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:10:39 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, enterprises, NotificationType, Integer32, Bits, Unsigned32, mgmt, NotificationType, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "enterprises", "NotificationType", "Integer32", "Bits", "Unsigned32", "mgmt", "NotificationType", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
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
mibBuilder.exportSymbols("POWERFANS-MIB", fanStat=fanStat, fanNo=fanNo, fanRotateSpeed=fanRotateSpeed, powerEntry=powerEntry, powerStat=powerStat, DisplayString=DisplayString, zxr10systemconfig=zxr10systemconfig, powerNo=powerNo, PowerStatus=PowerStatus, zte=zte, fanTable=fanTable, fanEntry=fanEntry, powerTemperature=powerTemperature, powerTable=powerTable, enviorment=enviorment, zxr10=zxr10, FanStatus=FanStatus)
