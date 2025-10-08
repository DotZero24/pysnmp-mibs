#
# PySNMP MIB module DOS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/radware/DOS-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:46:35 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
rsDOS, rndErrorSeverity, rndErrorDesc = mibBuilder.importSymbols("RADWARE-MIB", "rsDOS", "rndErrorSeverity", "rndErrorDesc")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, NotificationType, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, Counter64, TimeTicks, ModuleIdentity, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "NotificationType", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "Counter64", "TimeTicks", "ModuleIdentity", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
rsDOSSamplingRatio = MibScalar((1, 3, 6, 1, 4, 1, 89, 35, 1, 117, 1), Integer32().clone(100)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rsDOSSamplingRatio.setStatus('mandatory')
rsDOSSamplerOverloadMode = MibScalar((1, 3, 6, 1, 4, 1, 89, 35, 1, 117, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("forward", 1), ("discard", 2))).clone('forward')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rsDOSSamplerOverloadMode.setStatus('mandatory')
rsDOSOverloadTrap = NotificationType((1, 3, 6, 1, 4, 1, 89, 35, 1, 117) + (0,1)).setObjects(("RADWARE-MIB", "rndErrorDesc"), ("RADWARE-MIB", "rndErrorSeverity"))
mibBuilder.exportSymbols("DOS-MIB", rsDOSSamplerOverloadMode=rsDOSSamplerOverloadMode, rsDOSSamplingRatio=rsDOSSamplingRatio, rsDOSOverloadTrap=rsDOSOverloadTrap)
