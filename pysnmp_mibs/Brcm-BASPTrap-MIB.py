#
# PySNMP MIB module Brcm-BASPTrap-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/broadcom/Brcm-BASPTrap-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:18:17 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, enterprises, NotificationType, Bits, Integer32, Unsigned32, NotificationType, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, Counter64, TimeTicks, ModuleIdentity, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "enterprises", "NotificationType", "Bits", "Integer32", "Unsigned32", "NotificationType", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "Counter64", "TimeTicks", "ModuleIdentity", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
broadcom = MibIdentifier((1, 3, 6, 1, 4, 1, 4413))
enet = MibIdentifier((1, 3, 6, 1, 4, 1, 4413, 1))
basp = MibIdentifier((1, 3, 6, 1, 4, 1, 4413, 1, 2))
baspConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 4413, 1, 2, 1))
baspStat = MibIdentifier((1, 3, 6, 1, 4, 1, 4413, 1, 2, 2))
baspTrap = MibIdentifier((1, 3, 6, 1, 4, 1, 4413, 1, 2, 3))
trapAdapterName = MibScalar((1, 3, 6, 1, 4, 1, 4413, 1, 2, 3, 1), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: trapAdapterName.setStatus('mandatory')
trapTeamName = MibScalar((1, 3, 6, 1, 4, 1, 4413, 1, 2, 3, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: trapTeamName.setStatus('mandatory')
trapCauseDirection = MibScalar((1, 3, 6, 1, 4, 1, 4413, 1, 2, 3, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("adapterActive", 1), ("adapterInactive", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: trapCauseDirection.setStatus('mandatory')
trapAdapterActivityCause = MibScalar((1, 3, 6, 1, 4, 1, 4413, 1, 2, 3, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("none", 1), ("linkChange", 2), ("adapterEnabledOrDisabled", 3), ("adapterAddedOrRemoved", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: trapAdapterActivityCause.setStatus('mandatory')
failoverEvent = NotificationType((1, 3, 6, 1, 4, 1, 4413, 1, 2, 3) + (0,1)).setObjects(("Brcm-BASPTrap-MIB", "trapAdapterName"), ("Brcm-BASPTrap-MIB", "trapTeamName"), ("Brcm-BASPTrap-MIB", "trapCauseDirection"), ("Brcm-BASPTrap-MIB", "trapAdapterActivityCause"))
mibBuilder.exportSymbols("Brcm-BASPTrap-MIB", broadcom=broadcom, enet=enet, baspTrap=baspTrap, baspStat=baspStat, basp=basp, trapAdapterActivityCause=trapAdapterActivityCause, failoverEvent=failoverEvent, baspConfig=baspConfig, trapCauseDirection=trapCauseDirection, trapTeamName=trapTeamName, trapAdapterName=trapAdapterName)
