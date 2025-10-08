#
# PySNMP MIB module MIB-Dell-OME (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/dell/MIB-Dell-OME
# Produced by pysmi-1.1.12 at Wed Oct  8 10:43:39 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, enterprises, NotificationType, Bits, Integer32, Unsigned32, NotificationType, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, Counter64, TimeTicks, ModuleIdentity, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "enterprises", "NotificationType", "Bits", "Integer32", "Unsigned32", "NotificationType", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "Counter64", "TimeTicks", "ModuleIdentity", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
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
mibBuilder.exportSymbols("MIB-Dell-OME", sysMgmtBranch=sysMgmtBranch, omeAlertForwardedAlert=omeAlertForwardedAlert, omeAlertCriticalStatus=omeAlertCriticalStatus, DellString=DellString, DellString1=DellString1, omEssentialsTrap=omEssentialsTrap, omeRawAlertInfo=omeRawAlertInfo, dell=dell, omEssentialsMIB=omEssentialsMIB, omeAlertSystemDown=omeAlertSystemDown, omeAlertMessage=omeAlertMessage, omeAlertDevice=omeAlertDevice, omeAlertNormalStatus=omeAlertNormalStatus, omeAlertDataSources=omeAlertDataSources, omeTestAlert=omeTestAlert, omeAlertWarningStatus=omeAlertWarningStatus, enterpriseSW=enterpriseSW, omeAlertSeverity=omeAlertSeverity, omeAlertUnknownStatus=omeAlertUnknownStatus, omeAlertSystemUp=omeAlertSystemUp)
