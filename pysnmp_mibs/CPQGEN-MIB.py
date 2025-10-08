#
# PySNMP MIB module CPQGEN-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/hp/CPQGEN-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:09:20 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
sysName, = mibBuilder.importSymbols("SNMPv2-MIB", "sysName")
MibIdentifier, enterprises, NotificationType, Bits, Integer32, Unsigned32, NotificationType, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, Counter64, TimeTicks, ModuleIdentity, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "enterprises", "NotificationType", "Bits", "Integer32", "Unsigned32", "NotificationType", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "Counter64", "TimeTicks", "ModuleIdentity", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
compaq = MibIdentifier((1, 3, 6, 1, 4, 1, 232))
cpqGenUnreg = MibIdentifier((1, 3, 6, 1, 4, 1, 232, 151))
cpqGenComponent = MibIdentifier((1, 3, 6, 1, 4, 1, 232, 151, 2))
cpqTrapVarBind = MibIdentifier((1, 3, 6, 1, 4, 1, 232, 151, 2, 2))
cpqGenEntOIDStr = MibScalar((1, 3, 6, 1, 4, 1, 232, 151, 2, 2, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cpqGenEntOIDStr.setStatus('mandatory')
cpqGenTrapID = MibScalar((1, 3, 6, 1, 4, 1, 232, 151, 2, 2, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cpqGenTrapID.setStatus('mandatory')
cpqSpecTrapID = MibScalar((1, 3, 6, 1, 4, 1, 232, 151, 2, 2, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cpqSpecTrapID.setStatus('mandatory')
cpqGenericUnregistered = NotificationType((1, 3, 6, 1, 4, 1, 232) + (0,99999)).setObjects(("CPQGEN-MIB", "cpqGenEntOIDStr"), ("CPQGEN-MIB", "cpqGenTrapID"), ("CPQGEN-MIB", "cpqSpecTrapID"))
mibBuilder.exportSymbols("CPQGEN-MIB", cpqGenTrapID=cpqGenTrapID, cpqGenericUnregistered=cpqGenericUnregistered, compaq=compaq, cpqTrapVarBind=cpqTrapVarBind, cpqGenUnreg=cpqGenUnreg, cpqSpecTrapID=cpqSpecTrapID, cpqGenComponent=cpqGenComponent, cpqGenEntOIDStr=cpqGenEntOIDStr)
