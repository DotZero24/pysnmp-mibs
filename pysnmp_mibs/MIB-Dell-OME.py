#
# PySNMP MIB module MIB-Dell-OME (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/dell/MIB-Dell-OME
# Produced by pysmi-1.1.12 at Thu Sep 11 10:23:27 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, NotificationType, Counter64, enterprises, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "NotificationType", "Counter64", "enterprises", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
dell = MibIdentifier((1, 3, 6, 1, 4, 1, 674))
enterpriseSW = MibIdentifier((1, 3, 6, 1, 4, 1, 674, 11000))
sysMgmtBranch = MibIdentifier((1, 3, 6, 1, 4, 1, 674, 11000, 1000))
omEssentialsMIB = MibIdentifier((1, 3, 6, 1, 4, 1, 674, 11000, 1000, 100))
omEssentialsTrap = MibIdentifier((1, 3, 6, 1, 4, 1, 674, 11000, 1000, 100, 1))
class DellString(DisplayString):
    subtypeSpec = DisplayString.subtypeSpec + ValueSizeConstraint(0, 512)

class DellString1(DisplayString):
    subtypeSpec = DisplayString.subtypeSpec + ValueSizeConstraint(0, 128)

omeAlertMessage = MibScalar((1, 3, 6, 1, 4, 1, 674, 11000, 1000, 100, 1, 1), DellString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: omeAlertMessage.setStatus('mandatory')
omeAlertDevice = MibScalar((1, 3, 6, 1, 4, 1, 674, 11000, 1000, 100, 1, 2), DellString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: omeAlertDevice.setStatus('mandatory')
omeAlertSeverity = MibScalar((1, 3, 6, 1, 4, 1, 674, 11000, 1000, 100, 1, 3), DellString1()).setMaxAccess("readonly")
if mibBuilder.loadTexts: omeAlertSeverity.setStatus('mandatory')
omeAlertDataSources = MibScalar((1, 3, 6, 1, 4, 1, 674, 11000, 1000, 100, 1, 4), DellString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: omeAlertDataSources.setStatus('mandatory')
omeRawAlertInfo = MibScalar((1, 3, 6, 1, 4, 1, 674, 11000, 1000, 100, 1, 5), DellString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: omeRawAlertInfo.setStatus('mandatory')
omeTestAlert = NotificationType((1, 3, 6, 1, 4, 1, 674, 11000, 1000, 100, 1) + (0,1)).setObjects(("MIB-Dell-OME", "omeAlertMessage"), ("MIB-Dell-OME", "omeAlertDevice"), ("MIB-Dell-OME", "omeAlertSeverity"))
omeAlertSystemUp = NotificationType((1, 3, 6, 1, 4, 1, 674, 11000, 1000, 100, 1) + (0,1000)).setObjects(("MIB-Dell-OME", "omeAlertMessage"), ("MIB-Dell-OME", "omeAlertDevice"))
omeAlertSystemDown = NotificationType((1, 3, 6, 1, 4, 1, 674, 11000, 1000, 100, 1) + (0,1001)).setObjects(("MIB-Dell-OME", "omeAlertMessage"), ("MIB-Dell-OME", "omeAlertDevice"))
omeAlertForwardedAlert = NotificationType((1, 3, 6, 1, 4, 1, 674, 11000, 1000, 100, 1) + (0,2000)).setObjects(("MIB-Dell-OME", "omeAlertMessage"), ("MIB-Dell-OME", "omeAlertDevice"), ("MIB-Dell-OME", "omeAlertSeverity"))
omeAlertUnknownStatus = NotificationType((1, 3, 6, 1, 4, 1, 674, 11000, 1000, 100, 1) + (0,3001)).setObjects(("MIB-Dell-OME", "omeAlertMessage"), ("MIB-Dell-OME", "omeAlertDevice"), ("MIB-Dell-OME", "omeAlertDataSources"), ("MIB-Dell-OME", "omeRawAlertInfo"))
omeAlertNormalStatus = NotificationType((1, 3, 6, 1, 4, 1, 674, 11000, 1000, 100, 1) + (0,3002)).setObjects(("MIB-Dell-OME", "omeAlertMessage"), ("MIB-Dell-OME", "omeAlertDevice"), ("MIB-Dell-OME", "omeAlertDataSources"), ("MIB-Dell-OME", "omeRawAlertInfo"))
omeAlertWarningStatus = NotificationType((1, 3, 6, 1, 4, 1, 674, 11000, 1000, 100, 1) + (0,3003)).setObjects(("MIB-Dell-OME", "omeAlertMessage"), ("MIB-Dell-OME", "omeAlertDevice"), ("MIB-Dell-OME", "omeAlertDataSources"), ("MIB-Dell-OME", "omeRawAlertInfo"))
omeAlertCriticalStatus = NotificationType((1, 3, 6, 1, 4, 1, 674, 11000, 1000, 100, 1) + (0,3004)).setObjects(("MIB-Dell-OME", "omeAlertMessage"), ("MIB-Dell-OME", "omeAlertDevice"), ("MIB-Dell-OME", "omeAlertDataSources"), ("MIB-Dell-OME", "omeRawAlertInfo"))
mibBuilder.exportSymbols("MIB-Dell-OME", DellString1=DellString1, dell=dell, omEssentialsMIB=omEssentialsMIB, omeAlertSeverity=omeAlertSeverity, enterpriseSW=enterpriseSW, omeAlertSystemDown=omeAlertSystemDown, omeAlertDataSources=omeAlertDataSources, omEssentialsTrap=omEssentialsTrap, sysMgmtBranch=sysMgmtBranch, omeAlertNormalStatus=omeAlertNormalStatus, omeAlertForwardedAlert=omeAlertForwardedAlert, omeAlertUnknownStatus=omeAlertUnknownStatus, DellString=DellString, omeAlertDevice=omeAlertDevice, omeAlertCriticalStatus=omeAlertCriticalStatus, omeTestAlert=omeTestAlert, omeAlertWarningStatus=omeAlertWarningStatus, omeAlertSystemUp=omeAlertSystemUp, omeRawAlertInfo=omeRawAlertInfo, omeAlertMessage=omeAlertMessage)
