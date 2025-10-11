# SNMP MIB module (HMIT-DEVINFO-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/hirschmann/HMIT-DEVINFO-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 18:52:57 2025
# On host Robs-Air.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]

if 'mibBuilder' not in globals():
    import sys

    sys.stderr.write(__doc__)
    sys.exit(1)

# Import base ASN.1 objects even if this MIB does not use it

(Integer,
 OctetString,
 ObjectIdentifier) = mibBuilder.importSymbols(
    "ASN1",
    "Integer",
    "OctetString",
    "ObjectIdentifier")

(NamedValues,) = mibBuilder.importSymbols(
    "ASN1-ENUMERATION",
    "NamedValues")
(ConstraintsIntersection,
 ConstraintsUnion,
 SingleValueConstraint,
 ValueRangeConstraint,
 ValueSizeConstraint) = mibBuilder.importSymbols(
    "ASN1-REFINEMENT",
    "ConstraintsIntersection",
    "ConstraintsUnion",
    "SingleValueConstraint",
    "ValueRangeConstraint",
    "ValueSizeConstraint")

# Import SMI symbols from the MIBs this MIB depends on

(hmITMgmt,) = mibBuilder.importSymbols(
    "HMIT-SMI",
    "hmITMgmt")

(ModuleCompliance,
 NotificationGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup")

(Bits,
 Counter32,
 Counter64,
 Gauge32,
 Integer32,
 IpAddress,
 ModuleIdentity,
 MibIdentifier,
 NotificationType,
 ObjectIdentity,
 MibScalar,
 MibTable,
 MibTableRow,
 MibTableColumn,
 TimeTicks,
 Unsigned32,
 iso) = mibBuilder.importSymbols(
    "SNMPv2-SMI",
    "Bits",
    "Counter32",
    "Counter64",
    "Gauge32",
    "Integer32",
    "IpAddress",
    "ModuleIdentity",
    "MibIdentifier",
    "NotificationType",
    "ObjectIdentity",
    "MibScalar",
    "MibTable",
    "MibTableRow",
    "MibTableColumn",
    "TimeTicks",
    "Unsigned32",
    "iso")

(DisplayString,
 PhysAddress,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

hmITDeviceInfoMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 248, 100, 1, 3, 602)
)
if mibBuilder.loadTexts:
    hmITDeviceInfoMib.setRevisions(
        ("2010-01-08 17:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_HmITDeviceInformation_ObjectIdentity = ObjectIdentity
hmITDeviceInformation = _HmITDeviceInformation_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 100, 1, 3, 602, 1)
)
_HmITDeviceSerialNumber_Type = DisplayString
_HmITDeviceSerialNumber_Object = MibScalar
hmITDeviceSerialNumber = _HmITDeviceSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 248, 100, 1, 3, 602, 1, 1),
    _HmITDeviceSerialNumber_Type()
)
hmITDeviceSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmITDeviceSerialNumber.setStatus("current")


class _HmITDevHwModel_Type(DisplayString):
    """Custom type hmITDevHwModel based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_HmITDevHwModel_Type.__name__ = "DisplayString"
_HmITDevHwModel_Object = MibScalar
hmITDevHwModel = _HmITDevHwModel_Object(
    (1, 3, 6, 1, 4, 1, 248, 100, 1, 3, 602, 1, 2),
    _HmITDevHwModel_Type()
)
hmITDevHwModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmITDevHwModel.setStatus("current")
_HmITDeviceInfoTable_Object = MibTable
hmITDeviceInfoTable = _HmITDeviceInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 100, 1, 3, 602, 1, 100)
)
if mibBuilder.loadTexts:
    hmITDeviceInfoTable.setStatus("current")
_HmITDeviceInfoEntry_Object = MibTableRow
hmITDeviceInfoEntry = _HmITDeviceInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 100, 1, 3, 602, 1, 100, 1)
)
hmITDeviceInfoEntry.setIndexNames(
    (0, "HMIT-DEVINFO-MIB", "hmITDevIndex"),
)
if mibBuilder.loadTexts:
    hmITDeviceInfoEntry.setStatus("current")


class _HmITDevIndex_Type(Integer32):
    """Custom type hmITDevIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_HmITDevIndex_Type.__name__ = "Integer32"
_HmITDevIndex_Object = MibTableColumn
hmITDevIndex = _HmITDevIndex_Object(
    (1, 3, 6, 1, 4, 1, 248, 100, 1, 3, 602, 1, 100, 1, 1),
    _HmITDevIndex_Type()
)
hmITDevIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hmITDevIndex.setStatus("current")
_HmITDevName_Type = DisplayString
_HmITDevName_Object = MibTableColumn
hmITDevName = _HmITDevName_Object(
    (1, 3, 6, 1, 4, 1, 248, 100, 1, 3, 602, 1, 100, 1, 2),
    _HmITDevName_Type()
)
hmITDevName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmITDevName.setStatus("current")
_HmITDevType_Type = Unsigned32
_HmITDevType_Object = MibTableColumn
hmITDevType = _HmITDevType_Object(
    (1, 3, 6, 1, 4, 1, 248, 100, 1, 3, 602, 1, 100, 1, 3),
    _HmITDevType_Type()
)
hmITDevType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmITDevType.setStatus("current")
_HmITDevHwSerial_Type = DisplayString
_HmITDevHwSerial_Object = MibTableColumn
hmITDevHwSerial = _HmITDevHwSerial_Object(
    (1, 3, 6, 1, 4, 1, 248, 100, 1, 3, 602, 1, 100, 1, 4),
    _HmITDevHwSerial_Type()
)
hmITDevHwSerial.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmITDevHwSerial.setStatus("current")
_HmITDevHwVersion_Type = DisplayString
_HmITDevHwVersion_Object = MibTableColumn
hmITDevHwVersion = _HmITDevHwVersion_Object(
    (1, 3, 6, 1, 4, 1, 248, 100, 1, 3, 602, 1, 100, 1, 5),
    _HmITDevHwVersion_Type()
)
hmITDevHwVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmITDevHwVersion.setStatus("current")
_HmITDevSwVersion_Type = DisplayString
_HmITDevSwVersion_Object = MibTableColumn
hmITDevSwVersion = _HmITDevSwVersion_Object(
    (1, 3, 6, 1, 4, 1, 248, 100, 1, 3, 602, 1, 100, 1, 6),
    _HmITDevSwVersion_Type()
)
hmITDevSwVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmITDevSwVersion.setStatus("current")


class _HmITDevCfgVersion_Type(DisplayString):
    """Custom type hmITDevCfgVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_HmITDevCfgVersion_Type.__name__ = "DisplayString"
_HmITDevCfgVersion_Object = MibTableColumn
hmITDevCfgVersion = _HmITDevCfgVersion_Object(
    (1, 3, 6, 1, 4, 1, 248, 100, 1, 3, 602, 1, 100, 1, 7),
    _HmITDevCfgVersion_Type()
)
hmITDevCfgVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmITDevCfgVersion.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HMIT-DEVINFO-MIB",
    **{"hmITDeviceInfoMib": hmITDeviceInfoMib,
       "hmITDeviceInformation": hmITDeviceInformation,
       "hmITDeviceSerialNumber": hmITDeviceSerialNumber,
       "hmITDevHwModel": hmITDevHwModel,
       "hmITDeviceInfoTable": hmITDeviceInfoTable,
       "hmITDeviceInfoEntry": hmITDeviceInfoEntry,
       "hmITDevIndex": hmITDevIndex,
       "hmITDevName": hmITDevName,
       "hmITDevType": hmITDevType,
       "hmITDevHwSerial": hmITDevHwSerial,
       "hmITDevHwVersion": hmITDevHwVersion,
       "hmITDevSwVersion": hmITDevSwVersion,
       "hmITDevCfgVersion": hmITDevCfgVersion}
)
