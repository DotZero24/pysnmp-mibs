#
# PySNMP MIB module DOS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/radware/DOS-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:25:22 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
rsDOS, rndErrorDesc, rndErrorSeverity = mibBuilder.importSymbols("RADWARE-MIB", "rsDOS", "rndErrorDesc", "rndErrorSeverity")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, NotificationType, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "NotificationType", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
rsDOSSamplingRatio = MibScalar((1, 3, 6, 1, 4, 1, 89, 35, 1, 117, 1), Integer32().clone(100)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rsDOSSamplingRatio.setStatus('mandatory')
rsDOSSamplerOverloadMode = MibScalar((1, 3, 6, 1, 4, 1, 89, 35, 1, 117, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("forward", 1), ("discard", 2))).clone('forward')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rsDOSSamplerOverloadMode.setStatus('mandatory')
rsDOSOverloadTrap = NotificationType((1, 3, 6, 1, 4, 1, 89, 35, 1, 117) + (0,1)).setObjects(("RADWARE-MIB", "rndErrorDesc"), ("RADWARE-MIB", "rndErrorSeverity"))
mibBuilder.exportSymbols("DOS-MIB", rsDOSOverloadTrap=rsDOSOverloadTrap, rsDOSSamplingRatio=rsDOSSamplingRatio, rsDOSSamplerOverloadMode=rsDOSSamplerOverloadMode)
