#
# PySNMP MIB module QLGC-QLASPTrap-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/dell/QLGC-QLASPTrap-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:23:33 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, NotificationType, Counter64, enterprises, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "NotificationType", "Counter64", "enterprises", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
qlogic = MibIdentifier((1, 3, 6, 1, 4, 1, 3873))
enet = MibIdentifier((1, 3, 6, 1, 4, 1, 3873, 1))
qlasp = MibIdentifier((1, 3, 6, 1, 4, 1, 3873, 1, 2))
qlaspConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 3873, 1, 2, 1))
qlaspStat = MibIdentifier((1, 3, 6, 1, 4, 1, 3873, 1, 2, 2))
qlaspTrap = MibIdentifier((1, 3, 6, 1, 4, 1, 3873, 1, 2, 3))
trapAdapterName = MibScalar((1, 3, 6, 1, 4, 1, 3873, 1, 2, 3, 1), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: trapAdapterName.setStatus('mandatory')
trapTeamName = MibScalar((1, 3, 6, 1, 4, 1, 3873, 1, 2, 3, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: trapTeamName.setStatus('mandatory')
trapCauseDirection = MibScalar((1, 3, 6, 1, 4, 1, 3873, 1, 2, 3, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("adapterActive", 1), ("adapterInactive", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: trapCauseDirection.setStatus('mandatory')
trapAdapterActivityCause = MibScalar((1, 3, 6, 1, 4, 1, 3873, 1, 2, 3, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("none", 1), ("linkChange", 2), ("adapterEnabledOrDisabled", 3), ("adapterAddedOrRemoved", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: trapAdapterActivityCause.setStatus('mandatory')
failoverEvent = NotificationType((1, 3, 6, 1, 4, 1, 3873, 1, 2, 3) + (0,1)).setObjects(("QLGC-QLASPTrap-MIB", "trapAdapterName"), ("QLGC-QLASPTrap-MIB", "trapTeamName"), ("QLGC-QLASPTrap-MIB", "trapCauseDirection"), ("QLGC-QLASPTrap-MIB", "trapAdapterActivityCause"))
mibBuilder.exportSymbols("QLGC-QLASPTrap-MIB", qlaspTrap=qlaspTrap, enet=enet, trapTeamName=trapTeamName, trapCauseDirection=trapCauseDirection, trapAdapterActivityCause=trapAdapterActivityCause, qlasp=qlasp, qlaspStat=qlaspStat, trapAdapterName=trapAdapterName, qlaspConfig=qlaspConfig, failoverEvent=failoverEvent, qlogic=qlogic)
