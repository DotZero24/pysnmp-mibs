# SNMP MIB module (HPNSASOFTWARESUBSYSTEM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/hp/HPNSASOFTWARESUBSYSTEM-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:40:28 2025
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
 enterprises,
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
    "enterprises",
    "iso")

(DisplayString,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Hp_ObjectIdentity = ObjectIdentity
hp = _Hp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11)
)
_Nm_ObjectIdentity = ObjectIdentity
nm = _Nm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2)
)
_Hpnsa_ObjectIdentity = ObjectIdentity
hpnsa = _Hpnsa_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 23)
)
_HpnsaSW_ObjectIdentity = ObjectIdentity
hpnsaSW = _HpnsaSW_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 24)
)
_HpnsaSWMibRev_ObjectIdentity = ObjectIdentity
hpnsaSWMibRev = _HpnsaSWMibRev_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 24, 1)
)


class _HpnsaSWMibRevMajor_Type(Integer32):
    """Custom type hpnsaSWMibRevMajor based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_HpnsaSWMibRevMajor_Type.__name__ = "Integer32"
_HpnsaSWMibRevMajor_Object = MibScalar
hpnsaSWMibRevMajor = _HpnsaSWMibRevMajor_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 24, 1, 1),
    _HpnsaSWMibRevMajor_Type()
)
hpnsaSWMibRevMajor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnsaSWMibRevMajor.setStatus("mandatory")


class _HpnsaSWMibRevMinor_Type(Integer32):
    """Custom type hpnsaSWMibRevMinor based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HpnsaSWMibRevMinor_Type.__name__ = "Integer32"
_HpnsaSWMibRevMinor_Object = MibScalar
hpnsaSWMibRevMinor = _HpnsaSWMibRevMinor_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 24, 1, 2),
    _HpnsaSWMibRevMinor_Type()
)
hpnsaSWMibRevMinor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnsaSWMibRevMinor.setStatus("mandatory")
_HpnsaSWManageability_ObjectIdentity = ObjectIdentity
hpnsaSWManageability = _HpnsaSWManageability_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 24, 2)
)
_HpnsaSWManageabilityTable_Object = MibTable
hpnsaSWManageabilityTable = _HpnsaSWManageabilityTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 24, 2, 1)
)
if mibBuilder.loadTexts:
    hpnsaSWManageabilityTable.setStatus("mandatory")
_HpnsaSWManageabilityEntry_Object = MibTableRow
hpnsaSWManageabilityEntry = _HpnsaSWManageabilityEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 24, 2, 1, 1)
)
hpnsaSWManageabilityEntry.setIndexNames(
    (0, "HPNSASOFTWARESUBSYSTEM-MIB", "hpnsaSWManageabilityIndex"),
)
if mibBuilder.loadTexts:
    hpnsaSWManageabilityEntry.setStatus("mandatory")
_HpnsaSWManageabilityIndex_Type = Integer32
_HpnsaSWManageabilityIndex_Object = MibTableColumn
hpnsaSWManageabilityIndex = _HpnsaSWManageabilityIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 24, 2, 1, 1, 1),
    _HpnsaSWManageabilityIndex_Type()
)
hpnsaSWManageabilityIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnsaSWManageabilityIndex.setStatus("mandatory")


class _HpnsaSWManageabilityFileName_Type(DisplayString):
    """Custom type hpnsaSWManageabilityFileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_HpnsaSWManageabilityFileName_Type.__name__ = "DisplayString"
_HpnsaSWManageabilityFileName_Object = MibTableColumn
hpnsaSWManageabilityFileName = _HpnsaSWManageabilityFileName_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 24, 2, 1, 1, 2),
    _HpnsaSWManageabilityFileName_Type()
)
hpnsaSWManageabilityFileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnsaSWManageabilityFileName.setStatus("mandatory")


class _HpnsaSWManageabilityFileSize_Type(DisplayString):
    """Custom type hpnsaSWManageabilityFileSize based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_HpnsaSWManageabilityFileSize_Type.__name__ = "DisplayString"
_HpnsaSWManageabilityFileSize_Object = MibTableColumn
hpnsaSWManageabilityFileSize = _HpnsaSWManageabilityFileSize_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 24, 2, 1, 1, 3),
    _HpnsaSWManageabilityFileSize_Type()
)
hpnsaSWManageabilityFileSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnsaSWManageabilityFileSize.setStatus("mandatory")


class _HpnsaSWManageabilityFileDate_Type(OctetString):
    """Custom type hpnsaSWManageabilityFileDate based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )
    fixed_length = 6


_HpnsaSWManageabilityFileDate_Type.__name__ = "OctetString"
_HpnsaSWManageabilityFileDate_Object = MibTableColumn
hpnsaSWManageabilityFileDate = _HpnsaSWManageabilityFileDate_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 24, 2, 1, 1, 4),
    _HpnsaSWManageabilityFileDate_Type()
)
hpnsaSWManageabilityFileDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnsaSWManageabilityFileDate.setStatus("mandatory")


class _HpnsaSWManageabilityState_Type(Integer32):
    """Custom type hpnsaSWManageabilityState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("Unknown", 0),
          ("Stopped", 1),
          ("Start_Pending", 2),
          ("Stop_Pending", 3),
          ("Running", 4),
          ("Continue_Pending", 5),
          ("Pause_Pending", 6),
          ("Paused", 7))
    )


_HpnsaSWManageabilityState_Type.__name__ = "Integer32"
_HpnsaSWManageabilityState_Object = MibTableColumn
hpnsaSWManageabilityState = _HpnsaSWManageabilityState_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 24, 2, 1, 1, 5),
    _HpnsaSWManageabilityState_Type()
)
hpnsaSWManageabilityState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnsaSWManageabilityState.setStatus("mandatory")


class _HpnsaSWManageabilityType_Type(Integer32):
    """Custom type hpnsaSWManageabilityType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("Unknown", 0),
          ("Agent", 1),
          ("Service", 2),
          ("Driver", 3),
          ("Other", 4))
    )


_HpnsaSWManageabilityType_Type.__name__ = "Integer32"
_HpnsaSWManageabilityType_Object = MibTableColumn
hpnsaSWManageabilityType = _HpnsaSWManageabilityType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 24, 2, 1, 1, 6),
    _HpnsaSWManageabilityType_Type()
)
hpnsaSWManageabilityType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnsaSWManageabilityType.setStatus("mandatory")


class _HpnsaSWManageabilityVersion_Type(DisplayString):
    """Custom type hpnsaSWManageabilityVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_HpnsaSWManageabilityVersion_Type.__name__ = "DisplayString"
_HpnsaSWManageabilityVersion_Object = MibTableColumn
hpnsaSWManageabilityVersion = _HpnsaSWManageabilityVersion_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 24, 2, 1, 1, 7),
    _HpnsaSWManageabilityVersion_Type()
)
hpnsaSWManageabilityVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnsaSWManageabilityVersion.setStatus("mandatory")


class _HpnsaSWManageabilityDescription_Type(DisplayString):
    """Custom type hpnsaSWManageabilityDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_HpnsaSWManageabilityDescription_Type.__name__ = "DisplayString"
_HpnsaSWManageabilityDescription_Object = MibTableColumn
hpnsaSWManageabilityDescription = _HpnsaSWManageabilityDescription_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 24, 2, 1, 1, 8),
    _HpnsaSWManageabilityDescription_Type()
)
hpnsaSWManageabilityDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnsaSWManageabilityDescription.setStatus("mandatory")
_HpnsaSWDrivers_ObjectIdentity = ObjectIdentity
hpnsaSWDrivers = _HpnsaSWDrivers_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 24, 3)
)
_HpnsaSWDriversTable_Object = MibTable
hpnsaSWDriversTable = _HpnsaSWDriversTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 24, 3, 1)
)
if mibBuilder.loadTexts:
    hpnsaSWDriversTable.setStatus("mandatory")
_HpnsaSWDriversEntry_Object = MibTableRow
hpnsaSWDriversEntry = _HpnsaSWDriversEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 24, 3, 1, 1)
)
hpnsaSWDriversEntry.setIndexNames(
    (0, "HPNSASOFTWARESUBSYSTEM-MIB", "hpnsaSWDriversIndex"),
)
if mibBuilder.loadTexts:
    hpnsaSWDriversEntry.setStatus("mandatory")


class _HpnsaSWDriversIndex_Type(Integer32):
    """Custom type hpnsaSWDriversIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_HpnsaSWDriversIndex_Type.__name__ = "Integer32"
_HpnsaSWDriversIndex_Object = MibTableColumn
hpnsaSWDriversIndex = _HpnsaSWDriversIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 24, 3, 1, 1, 1),
    _HpnsaSWDriversIndex_Type()
)
hpnsaSWDriversIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnsaSWDriversIndex.setStatus("mandatory")


class _HpnsaSWDriversFileName_Type(DisplayString):
    """Custom type hpnsaSWDriversFileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_HpnsaSWDriversFileName_Type.__name__ = "DisplayString"
_HpnsaSWDriversFileName_Object = MibTableColumn
hpnsaSWDriversFileName = _HpnsaSWDriversFileName_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 24, 3, 1, 1, 2),
    _HpnsaSWDriversFileName_Type()
)
hpnsaSWDriversFileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnsaSWDriversFileName.setStatus("mandatory")


class _HpnsaSWDriversFileSize_Type(DisplayString):
    """Custom type hpnsaSWDriversFileSize based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_HpnsaSWDriversFileSize_Type.__name__ = "DisplayString"
_HpnsaSWDriversFileSize_Object = MibTableColumn
hpnsaSWDriversFileSize = _HpnsaSWDriversFileSize_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 24, 3, 1, 1, 3),
    _HpnsaSWDriversFileSize_Type()
)
hpnsaSWDriversFileSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnsaSWDriversFileSize.setStatus("mandatory")


class _HpnsaSWDriversFileDate_Type(OctetString):
    """Custom type hpnsaSWDriversFileDate based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )
    fixed_length = 6


_HpnsaSWDriversFileDate_Type.__name__ = "OctetString"
_HpnsaSWDriversFileDate_Object = MibTableColumn
hpnsaSWDriversFileDate = _HpnsaSWDriversFileDate_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 24, 3, 1, 1, 4),
    _HpnsaSWDriversFileDate_Type()
)
hpnsaSWDriversFileDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnsaSWDriversFileDate.setStatus("mandatory")


class _HpnsaSWDriversState_Type(Integer32):
    """Custom type hpnsaSWDriversState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("Unknown", 0),
          ("Stopped", 1),
          ("Start_Pending", 2),
          ("Stop_Pending", 3),
          ("Running", 4),
          ("Continue_Pending", 5),
          ("Pause_Pending", 6),
          ("Paused", 7))
    )


_HpnsaSWDriversState_Type.__name__ = "Integer32"
_HpnsaSWDriversState_Object = MibTableColumn
hpnsaSWDriversState = _HpnsaSWDriversState_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 24, 3, 1, 1, 5),
    _HpnsaSWDriversState_Type()
)
hpnsaSWDriversState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnsaSWDriversState.setStatus("mandatory")


class _HpnsaSWDriversType_Type(Integer32):
    """Custom type hpnsaSWDriversType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("Unknown", 0),
          ("NetworkInterfaceCard", 1),
          ("SCSI", 2),
          ("DiskArrayController", 3),
          ("System", 4))
    )


_HpnsaSWDriversType_Type.__name__ = "Integer32"
_HpnsaSWDriversType_Object = MibTableColumn
hpnsaSWDriversType = _HpnsaSWDriversType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 24, 3, 1, 1, 6),
    _HpnsaSWDriversType_Type()
)
hpnsaSWDriversType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnsaSWDriversType.setStatus("mandatory")


class _HpnsaSWDriversVersion_Type(DisplayString):
    """Custom type hpnsaSWDriversVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_HpnsaSWDriversVersion_Type.__name__ = "DisplayString"
_HpnsaSWDriversVersion_Object = MibTableColumn
hpnsaSWDriversVersion = _HpnsaSWDriversVersion_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 24, 3, 1, 1, 7),
    _HpnsaSWDriversVersion_Type()
)
hpnsaSWDriversVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnsaSWDriversVersion.setStatus("mandatory")


class _HpnsaSWDriversDescription_Type(DisplayString):
    """Custom type hpnsaSWDriversDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_HpnsaSWDriversDescription_Type.__name__ = "DisplayString"
_HpnsaSWDriversDescription_Object = MibTableColumn
hpnsaSWDriversDescription = _HpnsaSWDriversDescription_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 24, 3, 1, 1, 8),
    _HpnsaSWDriversDescription_Type()
)
hpnsaSWDriversDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnsaSWDriversDescription.setStatus("mandatory")
_HpnsaSWBIOSFirmware_ObjectIdentity = ObjectIdentity
hpnsaSWBIOSFirmware = _HpnsaSWBIOSFirmware_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 24, 4)
)
_HpnsaSWBIOSFirmwareTable_Object = MibTable
hpnsaSWBIOSFirmwareTable = _HpnsaSWBIOSFirmwareTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 24, 4, 1)
)
if mibBuilder.loadTexts:
    hpnsaSWBIOSFirmwareTable.setStatus("mandatory")
_HpnsaSWBIOSFirmwareEntry_Object = MibTableRow
hpnsaSWBIOSFirmwareEntry = _HpnsaSWBIOSFirmwareEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 24, 4, 1, 1)
)
hpnsaSWBIOSFirmwareEntry.setIndexNames(
    (0, "HPNSASOFTWARESUBSYSTEM-MIB", "hpnsaSWBIOSFirmwareIndex"),
)
if mibBuilder.loadTexts:
    hpnsaSWBIOSFirmwareEntry.setStatus("mandatory")


class _HpnsaSWBIOSFirmwareIndex_Type(Integer32):
    """Custom type hpnsaSWBIOSFirmwareIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_HpnsaSWBIOSFirmwareIndex_Type.__name__ = "Integer32"
_HpnsaSWBIOSFirmwareIndex_Object = MibTableColumn
hpnsaSWBIOSFirmwareIndex = _HpnsaSWBIOSFirmwareIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 24, 4, 1, 1, 1),
    _HpnsaSWBIOSFirmwareIndex_Type()
)
hpnsaSWBIOSFirmwareIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnsaSWBIOSFirmwareIndex.setStatus("mandatory")


class _HpnsaSWBIOSFirmwareName_Type(DisplayString):
    """Custom type hpnsaSWBIOSFirmwareName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_HpnsaSWBIOSFirmwareName_Type.__name__ = "DisplayString"
_HpnsaSWBIOSFirmwareName_Object = MibTableColumn
hpnsaSWBIOSFirmwareName = _HpnsaSWBIOSFirmwareName_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 24, 4, 1, 1, 2),
    _HpnsaSWBIOSFirmwareName_Type()
)
hpnsaSWBIOSFirmwareName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnsaSWBIOSFirmwareName.setStatus("mandatory")
_HpnsaSWBIOSFirmwareType_Type = Integer32
_HpnsaSWBIOSFirmwareType_Object = MibTableColumn
hpnsaSWBIOSFirmwareType = _HpnsaSWBIOSFirmwareType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 24, 4, 1, 1, 3),
    _HpnsaSWBIOSFirmwareType_Type()
)
hpnsaSWBIOSFirmwareType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnsaSWBIOSFirmwareType.setStatus("mandatory")


class _HpnsaSWBIOSFirmwareVersion_Type(DisplayString):
    """Custom type hpnsaSWBIOSFirmwareVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_HpnsaSWBIOSFirmwareVersion_Type.__name__ = "DisplayString"
_HpnsaSWBIOSFirmwareVersion_Object = MibTableColumn
hpnsaSWBIOSFirmwareVersion = _HpnsaSWBIOSFirmwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 24, 4, 1, 1, 4),
    _HpnsaSWBIOSFirmwareVersion_Type()
)
hpnsaSWBIOSFirmwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnsaSWBIOSFirmwareVersion.setStatus("mandatory")


class _HpnsaSWBIOSFirmwareDescription_Type(DisplayString):
    """Custom type hpnsaSWBIOSFirmwareDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_HpnsaSWBIOSFirmwareDescription_Type.__name__ = "DisplayString"
_HpnsaSWBIOSFirmwareDescription_Object = MibTableColumn
hpnsaSWBIOSFirmwareDescription = _HpnsaSWBIOSFirmwareDescription_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 24, 4, 1, 1, 5),
    _HpnsaSWBIOSFirmwareDescription_Type()
)
hpnsaSWBIOSFirmwareDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnsaSWBIOSFirmwareDescription.setStatus("mandatory")
_HpnsaSWRevisionHistory_ObjectIdentity = ObjectIdentity
hpnsaSWRevisionHistory = _HpnsaSWRevisionHistory_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 24, 5)
)
_HpnsaSWRevisionHistoryTable_Object = MibTable
hpnsaSWRevisionHistoryTable = _HpnsaSWRevisionHistoryTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 24, 5, 1)
)
if mibBuilder.loadTexts:
    hpnsaSWRevisionHistoryTable.setStatus("mandatory")
_HpnsaSWRevisionHistoryEntry_Object = MibTableRow
hpnsaSWRevisionHistoryEntry = _HpnsaSWRevisionHistoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 24, 5, 1, 1)
)
hpnsaSWRevisionHistoryEntry.setIndexNames(
    (0, "HPNSASOFTWARESUBSYSTEM-MIB", "hpnsaSWRevisionHistoryEntry"),
)
if mibBuilder.loadTexts:
    hpnsaSWRevisionHistoryEntry.setStatus("mandatory")
_HpnsaSWRevisionHistoryIndex_Type = Integer32
_HpnsaSWRevisionHistoryIndex_Object = MibTableColumn
hpnsaSWRevisionHistoryIndex = _HpnsaSWRevisionHistoryIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 24, 5, 1, 1, 1),
    _HpnsaSWRevisionHistoryIndex_Type()
)
hpnsaSWRevisionHistoryIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnsaSWRevisionHistoryIndex.setStatus("mandatory")


class _HpnsaSWRevisionHistoryName_Type(DisplayString):
    """Custom type hpnsaSWRevisionHistoryName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_HpnsaSWRevisionHistoryName_Type.__name__ = "DisplayString"
_HpnsaSWRevisionHistoryName_Object = MibTableColumn
hpnsaSWRevisionHistoryName = _HpnsaSWRevisionHistoryName_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 24, 5, 1, 1, 2),
    _HpnsaSWRevisionHistoryName_Type()
)
hpnsaSWRevisionHistoryName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnsaSWRevisionHistoryName.setStatus("mandatory")


class _HpnsaSWRevisionHistorySize_Type(DisplayString):
    """Custom type hpnsaSWRevisionHistorySize based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_HpnsaSWRevisionHistorySize_Type.__name__ = "DisplayString"
_HpnsaSWRevisionHistorySize_Object = MibTableColumn
hpnsaSWRevisionHistorySize = _HpnsaSWRevisionHistorySize_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 24, 5, 1, 1, 3),
    _HpnsaSWRevisionHistorySize_Type()
)
hpnsaSWRevisionHistorySize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnsaSWRevisionHistorySize.setStatus("mandatory")


class _HpnsaSWRevisionHistoryDate_Type(OctetString):
    """Custom type hpnsaSWRevisionHistoryDate based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )
    fixed_length = 6


_HpnsaSWRevisionHistoryDate_Type.__name__ = "OctetString"
_HpnsaSWRevisionHistoryDate_Object = MibTableColumn
hpnsaSWRevisionHistoryDate = _HpnsaSWRevisionHistoryDate_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 24, 5, 1, 1, 4),
    _HpnsaSWRevisionHistoryDate_Type()
)
hpnsaSWRevisionHistoryDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnsaSWRevisionHistoryDate.setStatus("mandatory")


class _HpnsaSWRevisionHistoryState_Type(Integer32):
    """Custom type hpnsaSWRevisionHistoryState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_HpnsaSWRevisionHistoryState_Type.__name__ = "Integer32"
_HpnsaSWRevisionHistoryState_Object = MibTableColumn
hpnsaSWRevisionHistoryState = _HpnsaSWRevisionHistoryState_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 24, 5, 1, 1, 5),
    _HpnsaSWRevisionHistoryState_Type()
)
hpnsaSWRevisionHistoryState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnsaSWRevisionHistoryState.setStatus("mandatory")


class _HpnsaSWRevisionHistoryCategory_Type(Integer32):
    """Custom type hpnsaSWRevisionHistoryCategory based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("Unknown", 0),
          ("Agent", 1),
          ("Service", 2),
          ("Driver", 3),
          ("BIOSFirmware", 4))
    )


_HpnsaSWRevisionHistoryCategory_Type.__name__ = "Integer32"
_HpnsaSWRevisionHistoryCategory_Object = MibTableColumn
hpnsaSWRevisionHistoryCategory = _HpnsaSWRevisionHistoryCategory_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 24, 5, 1, 1, 6),
    _HpnsaSWRevisionHistoryCategory_Type()
)
hpnsaSWRevisionHistoryCategory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnsaSWRevisionHistoryCategory.setStatus("mandatory")


class _HpnsaSWRevisionHistoryType_Type(Integer32):
    """Custom type hpnsaSWRevisionHistoryType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_HpnsaSWRevisionHistoryType_Type.__name__ = "Integer32"
_HpnsaSWRevisionHistoryType_Object = MibTableColumn
hpnsaSWRevisionHistoryType = _HpnsaSWRevisionHistoryType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 24, 5, 1, 1, 7),
    _HpnsaSWRevisionHistoryType_Type()
)
hpnsaSWRevisionHistoryType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnsaSWRevisionHistoryType.setStatus("mandatory")


class _HpnsaSWRevisionHistoryVersion_Type(DisplayString):
    """Custom type hpnsaSWRevisionHistoryVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_HpnsaSWRevisionHistoryVersion_Type.__name__ = "DisplayString"
_HpnsaSWRevisionHistoryVersion_Object = MibTableColumn
hpnsaSWRevisionHistoryVersion = _HpnsaSWRevisionHistoryVersion_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 24, 5, 1, 1, 8),
    _HpnsaSWRevisionHistoryVersion_Type()
)
hpnsaSWRevisionHistoryVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnsaSWRevisionHistoryVersion.setStatus("mandatory")


class _HpnsaSWRevisionHistoryChangeDate_Type(OctetString):
    """Custom type hpnsaSWRevisionHistoryChangeDate based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )
    fixed_length = 6


_HpnsaSWRevisionHistoryChangeDate_Type.__name__ = "OctetString"
_HpnsaSWRevisionHistoryChangeDate_Object = MibTableColumn
hpnsaSWRevisionHistoryChangeDate = _HpnsaSWRevisionHistoryChangeDate_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 24, 5, 1, 1, 9),
    _HpnsaSWRevisionHistoryChangeDate_Type()
)
hpnsaSWRevisionHistoryChangeDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnsaSWRevisionHistoryChangeDate.setStatus("mandatory")


class _HpnsaSWAgentVersion_Type(DisplayString):
    """Custom type hpnsaSWAgentVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_HpnsaSWAgentVersion_Type.__name__ = "DisplayString"
_HpnsaSWAgentVersion_Object = MibScalar
hpnsaSWAgentVersion = _HpnsaSWAgentVersion_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 24, 6),
    _HpnsaSWAgentVersion_Type()
)
hpnsaSWAgentVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnsaSWAgentVersion.setStatus("mandatory")


class _HpnsaSWPollingState_Type(Integer32):
    """Custom type hpnsaSWPollingState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_HpnsaSWPollingState_Type.__name__ = "Integer32"
_HpnsaSWPollingState_Object = MibScalar
hpnsaSWPollingState = _HpnsaSWPollingState_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 24, 7),
    _HpnsaSWPollingState_Type()
)
hpnsaSWPollingState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnsaSWPollingState.setStatus("mandatory")
_HpnsaSWPollingTime_Type = Integer32
_HpnsaSWPollingTime_Object = MibScalar
hpnsaSWPollingTime = _HpnsaSWPollingTime_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 24, 8),
    _HpnsaSWPollingTime_Type()
)
hpnsaSWPollingTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnsaSWPollingTime.setStatus("mandatory")


class _HpnsaSWManualPolling_Type(Integer32):
    """Custom type hpnsaSWManualPolling based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1234
        )
    )
    namedValues = NamedValues(
        ("CheckRevisionHistory", 1234)
    )


_HpnsaSWManualPolling_Type.__name__ = "Integer32"
_HpnsaSWManualPolling_Object = MibScalar
hpnsaSWManualPolling = _HpnsaSWManualPolling_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 24, 9),
    _HpnsaSWManualPolling_Type()
)
hpnsaSWManualPolling.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnsaSWManualPolling.setStatus("mandatory")


class _HpnsaSWRevisionHistoryReset_Type(Integer32):
    """Custom type hpnsaSWRevisionHistoryReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1234
        )
    )
    namedValues = NamedValues(
        ("ClearHistory", 1234)
    )


_HpnsaSWRevisionHistoryReset_Type.__name__ = "Integer32"
_HpnsaSWRevisionHistoryReset_Object = MibScalar
hpnsaSWRevisionHistoryReset = _HpnsaSWRevisionHistoryReset_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 24, 10),
    _HpnsaSWRevisionHistoryReset_Type()
)
hpnsaSWRevisionHistoryReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnsaSWRevisionHistoryReset.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HPNSASOFTWARESUBSYSTEM-MIB",
    **{"hp": hp,
       "nm": nm,
       "hpnsa": hpnsa,
       "hpnsaSW": hpnsaSW,
       "hpnsaSWMibRev": hpnsaSWMibRev,
       "hpnsaSWMibRevMajor": hpnsaSWMibRevMajor,
       "hpnsaSWMibRevMinor": hpnsaSWMibRevMinor,
       "hpnsaSWManageability": hpnsaSWManageability,
       "hpnsaSWManageabilityTable": hpnsaSWManageabilityTable,
       "hpnsaSWManageabilityEntry": hpnsaSWManageabilityEntry,
       "hpnsaSWManageabilityIndex": hpnsaSWManageabilityIndex,
       "hpnsaSWManageabilityFileName": hpnsaSWManageabilityFileName,
       "hpnsaSWManageabilityFileSize": hpnsaSWManageabilityFileSize,
       "hpnsaSWManageabilityFileDate": hpnsaSWManageabilityFileDate,
       "hpnsaSWManageabilityState": hpnsaSWManageabilityState,
       "hpnsaSWManageabilityType": hpnsaSWManageabilityType,
       "hpnsaSWManageabilityVersion": hpnsaSWManageabilityVersion,
       "hpnsaSWManageabilityDescription": hpnsaSWManageabilityDescription,
       "hpnsaSWDrivers": hpnsaSWDrivers,
       "hpnsaSWDriversTable": hpnsaSWDriversTable,
       "hpnsaSWDriversEntry": hpnsaSWDriversEntry,
       "hpnsaSWDriversIndex": hpnsaSWDriversIndex,
       "hpnsaSWDriversFileName": hpnsaSWDriversFileName,
       "hpnsaSWDriversFileSize": hpnsaSWDriversFileSize,
       "hpnsaSWDriversFileDate": hpnsaSWDriversFileDate,
       "hpnsaSWDriversState": hpnsaSWDriversState,
       "hpnsaSWDriversType": hpnsaSWDriversType,
       "hpnsaSWDriversVersion": hpnsaSWDriversVersion,
       "hpnsaSWDriversDescription": hpnsaSWDriversDescription,
       "hpnsaSWBIOSFirmware": hpnsaSWBIOSFirmware,
       "hpnsaSWBIOSFirmwareTable": hpnsaSWBIOSFirmwareTable,
       "hpnsaSWBIOSFirmwareEntry": hpnsaSWBIOSFirmwareEntry,
       "hpnsaSWBIOSFirmwareIndex": hpnsaSWBIOSFirmwareIndex,
       "hpnsaSWBIOSFirmwareName": hpnsaSWBIOSFirmwareName,
       "hpnsaSWBIOSFirmwareType": hpnsaSWBIOSFirmwareType,
       "hpnsaSWBIOSFirmwareVersion": hpnsaSWBIOSFirmwareVersion,
       "hpnsaSWBIOSFirmwareDescription": hpnsaSWBIOSFirmwareDescription,
       "hpnsaSWRevisionHistory": hpnsaSWRevisionHistory,
       "hpnsaSWRevisionHistoryTable": hpnsaSWRevisionHistoryTable,
       "hpnsaSWRevisionHistoryEntry": hpnsaSWRevisionHistoryEntry,
       "hpnsaSWRevisionHistoryIndex": hpnsaSWRevisionHistoryIndex,
       "hpnsaSWRevisionHistoryName": hpnsaSWRevisionHistoryName,
       "hpnsaSWRevisionHistorySize": hpnsaSWRevisionHistorySize,
       "hpnsaSWRevisionHistoryDate": hpnsaSWRevisionHistoryDate,
       "hpnsaSWRevisionHistoryState": hpnsaSWRevisionHistoryState,
       "hpnsaSWRevisionHistoryCategory": hpnsaSWRevisionHistoryCategory,
       "hpnsaSWRevisionHistoryType": hpnsaSWRevisionHistoryType,
       "hpnsaSWRevisionHistoryVersion": hpnsaSWRevisionHistoryVersion,
       "hpnsaSWRevisionHistoryChangeDate": hpnsaSWRevisionHistoryChangeDate,
       "hpnsaSWAgentVersion": hpnsaSWAgentVersion,
       "hpnsaSWPollingState": hpnsaSWPollingState,
       "hpnsaSWPollingTime": hpnsaSWPollingTime,
       "hpnsaSWManualPolling": hpnsaSWManualPolling,
       "hpnsaSWRevisionHistoryReset": hpnsaSWRevisionHistoryReset}
)
