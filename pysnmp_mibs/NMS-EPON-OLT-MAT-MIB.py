#
# PySNMP MIB module NMS-EPON-OLT-MAT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/bdcom/NMS-EPON-OLT-MAT-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:22:50 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
nmsEPONGroup, = mibBuilder.importSymbols("NMS-SMI", "nmsEPONGroup")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
nmsEponOltMat = MibIdentifier((1, 3, 6, 1, 4, 1, 3320, 101, 200))
oltFtpServerIpAddr = MibScalar((1, 3, 6, 1, 4, 1, 3320, 101, 200, 1), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: oltFtpServerIpAddr.setStatus('mandatory')
oltFtpServerPort = MibScalar((1, 3, 6, 1, 4, 1, 3320, 101, 200, 2), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: oltFtpServerPort.setStatus('mandatory')
oltMatInsideIpAddr = MibScalar((1, 3, 6, 1, 4, 1, 3320, 101, 200, 3), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: oltMatInsideIpAddr.setStatus('mandatory')
mibBuilder.exportSymbols("NMS-EPON-OLT-MAT-MIB", oltFtpServerPort=oltFtpServerPort, oltMatInsideIpAddr=oltMatInsideIpAddr, oltFtpServerIpAddr=oltFtpServerIpAddr, nmsEponOltMat=nmsEponOltMat)
