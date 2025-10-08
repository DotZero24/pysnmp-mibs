#
# PySNMP MIB module H3C-STORAGE-REF-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/h3c/H3C-STORAGE-REF-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:22:42 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
h3c, = mibBuilder.importSymbols("HUAWEI-3COM-OID-MIB", "h3c")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, NotificationType, Integer32, Bits, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Integer32", "Bits", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
h3cStorageRef = ModuleIdentity((1, 3, 6, 1, 4, 1, 2011, 10, 10))
if mibBuilder.loadTexts: h3cStorageRef.setLastUpdated('200709141452Z')
if mibBuilder.loadTexts: h3cStorageRef.setOrganization('H3C Technologies Co., Ltd.')
class H3cStorageCapableState(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("support", 1), ("notsupport", 2))

class H3cStorageEnableState(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("enable", 1), ("disable", 2))

class H3cStorageActionType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("action", 1), ("invalid", 2))

class H3cStorageLedStateType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("off", 1), ("on", 2), ("blink", 3))

class H3cStorageOnlineState(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("online", 1), ("offline", 2))

class H3cLvIDType(TextualConvention, OctetString):
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(1, 20)

class H3cSessionIDType(TextualConvention, OctetString):
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(1, 16)

class H3cWwpnListType(TextualConvention, OctetString):
    status = 'current'

class H3cStorageOwnerType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("spa", 1), ("spb", 2), ("none", 3))

class H3cExtendSelectPolicy(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("differentAdapter", 1), ("differentDrive", 2), ("anyDrive", 3), ("none", 4))

class H3cRaidIDType(TextualConvention, OctetString):
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(36, 71)

class H3cSoftwareInfoString(TextualConvention, OctetString):
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(2, 64)

mibBuilder.exportSymbols("H3C-STORAGE-REF-MIB", H3cLvIDType=H3cLvIDType, H3cStorageCapableState=H3cStorageCapableState, H3cStorageOwnerType=H3cStorageOwnerType, H3cRaidIDType=H3cRaidIDType, H3cStorageOnlineState=H3cStorageOnlineState, H3cStorageLedStateType=H3cStorageLedStateType, H3cStorageEnableState=H3cStorageEnableState, H3cWwpnListType=H3cWwpnListType, H3cStorageActionType=H3cStorageActionType, H3cSoftwareInfoString=H3cSoftwareInfoString, h3cStorageRef=h3cStorageRef, H3cSessionIDType=H3cSessionIDType, H3cExtendSelectPolicy=H3cExtendSelectPolicy, PYSNMP_MODULE_ID=h3cStorageRef)
