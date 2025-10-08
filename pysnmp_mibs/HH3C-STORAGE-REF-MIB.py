#
# PySNMP MIB module HH3C-STORAGE-REF-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/hh3c/HH3C-STORAGE-REF-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 11:09:19 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
hh3c, = mibBuilder.importSymbols("HH3C-OID-MIB", "hh3c")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, NotificationType, Integer32, Bits, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Integer32", "Bits", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
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

mibBuilder.exportSymbols("HH3C-STORAGE-REF-MIB", Hh3cStorageOwnerType=Hh3cStorageOwnerType, Hh3cSoftwareInfoString=Hh3cSoftwareInfoString, Hh3cStorageCapableState=Hh3cStorageCapableState, Hh3cWwpnListType=Hh3cWwpnListType, Hh3cLvIDType=Hh3cLvIDType, PYSNMP_MODULE_ID=hh3cStorageRef, Hh3cStorageActionType=Hh3cStorageActionType, Hh3cRaidIDType=Hh3cRaidIDType, Hh3cStorageEnableState=Hh3cStorageEnableState, Hh3cExtendSelectPolicy=Hh3cExtendSelectPolicy, Hh3cStorageOnlineState=Hh3cStorageOnlineState, Hh3cStorageLedStateType=Hh3cStorageLedStateType, hh3cStorageRef=hh3cStorageRef, Hh3cSessionIDType=Hh3cSessionIDType)
