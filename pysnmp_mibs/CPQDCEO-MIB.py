#
# PySNMP MIB module CPQDCEO-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/hp/CPQDCEO-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:08:11 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
compaq, = mibBuilder.importSymbols("CPQHOST-MIB", "compaq")
ifDescr, ifIndex = mibBuilder.importSymbols("IF-MIB", "ifDescr", "ifIndex")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
sysDescr, sysContact, sysLocation, sysName = mibBuilder.importSymbols("SNMPv2-MIB", "sysDescr", "sysContact", "sysLocation", "sysName")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, NotificationType, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, Counter64, TimeTicks, ModuleIdentity, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "NotificationType", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "Counter64", "TimeTicks", "ModuleIdentity", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
cpqDceo = MibIdentifier((1, 3, 6, 1, 4, 1, 232, 173))
environmentalDevice = MibIdentifier((1, 3, 6, 1, 4, 1, 232, 173, 1))
dceoTrapInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 232, 173, 1, 1))
trapDescription = MibScalar((1, 3, 6, 1, 4, 1, 232, 173, 1, 1, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: trapDescription.setStatus('mandatory')
trapDeviceDetails = MibScalar((1, 3, 6, 1, 4, 1, 232, 173, 1, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: trapDeviceDetails.setStatus('mandatory')
trapDeviceMgmtUrl = MibScalar((1, 3, 6, 1, 4, 1, 232, 173, 1, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: trapDeviceMgmtUrl.setStatus('mandatory')
trapDceoHighPriority = NotificationType((1, 3, 6, 1, 4, 1, 232, 173) + (0,1)).setObjects(("SNMPv2-MIB", "sysName"), ("CPQDCEO-MIB", "trapDescription"), ("CPQDCEO-MIB", "trapDeviceDetails"), ("CPQDCEO-MIB", "trapDeviceMgmtUrl"))
trapDceoMediumPriority = NotificationType((1, 3, 6, 1, 4, 1, 232, 173) + (0,2)).setObjects(("SNMPv2-MIB", "sysName"), ("CPQDCEO-MIB", "trapDescription"), ("CPQDCEO-MIB", "trapDeviceDetails"), ("CPQDCEO-MIB", "trapDeviceMgmtUrl"))
trapDceoLowPriority = NotificationType((1, 3, 6, 1, 4, 1, 232, 173) + (0,3)).setObjects(("SNMPv2-MIB", "sysName"), ("CPQDCEO-MIB", "trapDescription"), ("CPQDCEO-MIB", "trapDeviceDetails"), ("CPQDCEO-MIB", "trapDeviceMgmtUrl"))
mibBuilder.exportSymbols("CPQDCEO-MIB", cpqDceo=cpqDceo, trapDescription=trapDescription, trapDceoMediumPriority=trapDceoMediumPriority, dceoTrapInfo=dceoTrapInfo, environmentalDevice=environmentalDevice, trapDceoHighPriority=trapDceoHighPriority, trapDceoLowPriority=trapDceoLowPriority, trapDeviceMgmtUrl=trapDeviceMgmtUrl, trapDeviceDetails=trapDeviceDetails)
