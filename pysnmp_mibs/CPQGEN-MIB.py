#
# PySNMP MIB module CPQGEN-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/hp/CPQGEN-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:03:08 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
sysName, = mibBuilder.importSymbols("SNMPv2-MIB", "sysName")
ModuleIdentity, NotificationType, Counter64, enterprises, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "NotificationType", "Counter64", "enterprises", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
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
mibBuilder.exportSymbols("CPQGEN-MIB", cpqGenericUnregistered=cpqGenericUnregistered, cpqGenComponent=cpqGenComponent, cpqSpecTrapID=cpqSpecTrapID, cpqGenTrapID=cpqGenTrapID, cpqGenUnreg=cpqGenUnreg, cpqGenEntOIDStr=cpqGenEntOIDStr, compaq=compaq, cpqTrapVarBind=cpqTrapVarBind)
