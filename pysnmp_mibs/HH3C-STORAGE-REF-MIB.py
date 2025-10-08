#
# PySNMP MIB module HH3C-STORAGE-REF-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/hh3c/HH3C-STORAGE-REF-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:42:12 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
hh3c, = mibBuilder.importSymbols("HH3C-OID-MIB", "hh3c")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, NotificationType, iso, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "NotificationType", "iso", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
hh3cStorageRef = ModuleIdentity((1, 3, 6, 1, 4, 1, 25506, 10))
if mibBuilder.loadTexts: hh3cStorageRef.setLastUpdated('200709141452Z')
if mibBuilder.loadTexts: hh3cStorageRef.setOrganization('New H3C Technologies Co., Ltd.')
class Hh3cStorageCapableState(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("support", 1), ("notsupport", 2))

class Hh3cStorageEnableState(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("enable", 1), ("disable", 2))

class Hh3cStorageActionType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("action", 1), ("invalid", 2))

class Hh3cStorageLedStateType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("off", 1), ("on", 2), ("blink", 3))

class Hh3cStorageOnlineState(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("online", 1), ("offline", 2))

class Hh3cLvIDType(TextualConvention, OctetString):
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(1, 20)

class Hh3cSessionIDType(TextualConvention, OctetString):
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(1, 16)

class Hh3cWwpnListType(TextualConvention, OctetString):
    status = 'current'

class Hh3cStorageOwnerType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("spa", 1), ("spb", 2), ("none", 3))

class Hh3cExtendSelectPolicy(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("differentAdapter", 1), ("differentDrive", 2), ("anyDrive", 3), ("none", 4))

class Hh3cRaidIDType(TextualConvention, OctetString):
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(36, 71)

class Hh3cSoftwareInfoString(TextualConvention, OctetString):
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(2, 64)

mibBuilder.exportSymbols("HH3C-STORAGE-REF-MIB", Hh3cSoftwareInfoString=Hh3cSoftwareInfoString, Hh3cStorageCapableState=Hh3cStorageCapableState, Hh3cWwpnListType=Hh3cWwpnListType, Hh3cStorageLedStateType=Hh3cStorageLedStateType, hh3cStorageRef=hh3cStorageRef, Hh3cSessionIDType=Hh3cSessionIDType, PYSNMP_MODULE_ID=hh3cStorageRef, Hh3cStorageOnlineState=Hh3cStorageOnlineState, Hh3cStorageActionType=Hh3cStorageActionType, Hh3cRaidIDType=Hh3cRaidIDType, Hh3cLvIDType=Hh3cLvIDType, Hh3cExtendSelectPolicy=Hh3cExtendSelectPolicy, Hh3cStorageEnableState=Hh3cStorageEnableState, Hh3cStorageOwnerType=Hh3cStorageOwnerType)
