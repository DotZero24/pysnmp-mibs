#
# PySNMP MIB module CPQAPPLIANCE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/hp/CPQAPPLIANCE-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:03:34 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
cpqHoTrapFlags, compaq = mibBuilder.importSymbols("CPQHOST-MIB", "cpqHoTrapFlags", "compaq")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
sysName, = mibBuilder.importSymbols("SNMPv2-MIB", "sysName")
ModuleIdentity, NotificationType, Counter64, enterprises, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "NotificationType", "Counter64", "enterprises", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
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
mibBuilder.exportSymbols("CPQAPPLIANCE-MIB", cpqApInterface=cpqApInterface, cpqApOsCommon=cpqApOsCommon, cpqApMibRevMajor=cpqApMibRevMajor, cpqApMibCondition=cpqApMibCondition, cpqApOsCommonPollFreq=cpqApOsCommonPollFreq, cpqApApplianceId=cpqApApplianceId, cpqApplianceMgmt=cpqApplianceMgmt, cpqApComponent=cpqApComponent, cpqApMibRevMinor=cpqApMibRevMinor, cpqApApplianceDescription=cpqApApplianceDescription, cpqApConfig=cpqApConfig, cpqApMibRev=cpqApMibRev)
