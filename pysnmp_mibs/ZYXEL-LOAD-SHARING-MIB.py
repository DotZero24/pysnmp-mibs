#
# PySNMP MIB module ZYXEL-LOAD-SHARING-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/zyxel/ZYXEL-LOAD-SHARING-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:38:16 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
EnabledStatus, = mibBuilder.importSymbols("P-BRIDGE-MIB", "EnabledStatus")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
esMgmt, = mibBuilder.importSymbols("ZYXEL-ES-SMI", "esMgmt")
zyxelLoadSharing = ModuleIdentity((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 44))
if mibBuilder.loadTexts: zyxelLoadSharing.setLastUpdated('201207010000Z')
if mibBuilder.loadTexts: zyxelLoadSharing.setOrganization('Enterprise Solution ZyXEL')
zyxelLoadSharingSetup = MibIdentifier((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 44, 1))
zyLoadSharingState = MibScalar((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 44, 1, 1), EnabledStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: zyLoadSharingState.setStatus('current')
zyLoadSharingCriteria = MibScalar((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 44, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("srcIp", 1), ("srcDstIp", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: zyLoadSharingCriteria.setStatus('current')
zyLoadSharingAgingTime = MibScalar((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 44, 1, 3), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: zyLoadSharingAgingTime.setStatus('current')
zyLoadSharingDiscoverTime = MibScalar((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 44, 1, 4), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: zyLoadSharingDiscoverTime.setStatus('current')
zyLoadSharingMaxPaths = MibScalar((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 44, 1, 5), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: zyLoadSharingMaxPaths.setStatus('current')
mibBuilder.exportSymbols("ZYXEL-LOAD-SHARING-MIB", zyxelLoadSharing=zyxelLoadSharing, zyLoadSharingAgingTime=zyLoadSharingAgingTime, zyLoadSharingCriteria=zyLoadSharingCriteria, zyxelLoadSharingSetup=zyxelLoadSharingSetup, PYSNMP_MODULE_ID=zyxelLoadSharing, zyLoadSharingMaxPaths=zyLoadSharingMaxPaths, zyLoadSharingState=zyLoadSharingState, zyLoadSharingDiscoverTime=zyLoadSharingDiscoverTime)
