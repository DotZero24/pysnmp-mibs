#
# PySNMP MIB module CPQAPPLIANCE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/hp/CPQAPPLIANCE-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:10:05 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
cpqHoTrapFlags, compaq = mibBuilder.importSymbols("CPQHOST-MIB", "cpqHoTrapFlags", "compaq")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
sysName, = mibBuilder.importSymbols("SNMPv2-MIB", "sysName")
MibIdentifier, enterprises, NotificationType, Bits, Integer32, Unsigned32, NotificationType, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, Counter64, TimeTicks, ModuleIdentity, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "enterprises", "NotificationType", "Bits", "Integer32", "Unsigned32", "NotificationType", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "Counter64", "TimeTicks", "ModuleIdentity", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
cpqApplianceMgmt = MibIdentifier((1, 3, 6, 1, 4, 1, 232, 21))
cpqApMibRev = MibIdentifier((1, 3, 6, 1, 4, 1, 232, 21, 1))
cpqApComponent = MibIdentifier((1, 3, 6, 1, 4, 1, 232, 21, 2))
cpqApInterface = MibIdentifier((1, 3, 6, 1, 4, 1, 232, 21, 2, 1))
cpqApConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 232, 21, 2, 2))
cpqApOsCommon = MibIdentifier((1, 3, 6, 1, 4, 1, 232, 21, 2, 1, 4))
cpqApMibRevMajor = MibScalar((1, 3, 6, 1, 4, 1, 232, 21, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cpqApMibRevMajor.setStatus('mandatory')
cpqApMibRevMinor = MibScalar((1, 3, 6, 1, 4, 1, 232, 21, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cpqApMibRevMinor.setStatus('mandatory')
cpqApMibCondition = MibScalar((1, 3, 6, 1, 4, 1, 232, 21, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("other", 1), ("ok", 2), ("degraded", 3), ("failed", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cpqApMibCondition.setStatus('mandatory')
cpqApOsCommonPollFreq = MibScalar((1, 3, 6, 1, 4, 1, 232, 21, 2, 1, 4, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cpqApOsCommonPollFreq.setStatus('mandatory')
cpqApApplianceId = MibScalar((1, 3, 6, 1, 4, 1, 232, 21, 2, 2, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cpqApApplianceId.setStatus('mandatory')
cpqApApplianceDescription = MibScalar((1, 3, 6, 1, 4, 1, 232, 21, 2, 2, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 80))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cpqApApplianceDescription.setStatus('mandatory')
mibBuilder.exportSymbols("CPQAPPLIANCE-MIB", cpqApMibCondition=cpqApMibCondition, cpqApOsCommon=cpqApOsCommon, cpqApComponent=cpqApComponent, cpqApMibRevMajor=cpqApMibRevMajor, cpqApplianceMgmt=cpqApplianceMgmt, cpqApInterface=cpqApInterface, cpqApApplianceDescription=cpqApApplianceDescription, cpqApApplianceId=cpqApApplianceId, cpqApOsCommonPollFreq=cpqApOsCommonPollFreq, cpqApConfig=cpqApConfig, cpqApMibRevMinor=cpqApMibRevMinor, cpqApMibRev=cpqApMibRev)
