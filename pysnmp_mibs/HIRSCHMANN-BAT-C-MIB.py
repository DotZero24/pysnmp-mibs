# SNMP MIB module (HIRSCHMANN-BAT-C-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/hirschmann/HIRSCHMANN-BAT-C-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 18:55:58 2025
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
 MacAddress,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

hmModuleIdentity = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 248, 6)
)
if mibBuilder.loadTexts:
    hmModuleIdentity.setRevisions(
        ("2012-05-09 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class EnabledDisabledStatus(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disableStatus", 0),
          ("enableStatus", 1))
    )



# MIB Managed Objects in the order of their OIDs

_Hirschmann_ObjectIdentity = ObjectIdentity
hirschmann = _Hirschmann_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248)
)
_HmComponents_ObjectIdentity = ObjectIdentity
hmComponents = _HmComponents_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 1)
)
_HmComponentsTable_Object = MibTable
hmComponentsTable = _HmComponentsTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 1, 1)
)
if mibBuilder.loadTexts:
    hmComponentsTable.setStatus("current")
_HmComponentsEntry_Object = MibTableRow
hmComponentsEntry = _HmComponentsEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 1, 1, 1)
)
hmComponentsEntry.setIndexNames(
    (0, "HIRSCHMANN-BAT-C-MIB", "hmComponentsIndex"),
)
if mibBuilder.loadTexts:
    hmComponentsEntry.setStatus("current")


class _HmComponentsIndex_Type(Integer32):
    """Custom type hmComponentsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_HmComponentsIndex_Type.__name__ = "Integer32"
_HmComponentsIndex_Object = MibTableColumn
hmComponentsIndex = _HmComponentsIndex_Object(
    (1, 3, 6, 1, 4, 1, 248, 1, 1, 1, 1),
    _HmComponentsIndex_Type()
)
hmComponentsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmComponentsIndex.setStatus("current")
_HmComponentsName_Type = DisplayString
_HmComponentsName_Object = MibTableColumn
hmComponentsName = _HmComponentsName_Object(
    (1, 3, 6, 1, 4, 1, 248, 1, 1, 1, 2),
    _HmComponentsName_Type()
)
hmComponentsName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmComponentsName.setStatus("current")
_HmComponentsDescr_Type = DisplayString
_HmComponentsDescr_Object = MibTableColumn
hmComponentsDescr = _HmComponentsDescr_Object(
    (1, 3, 6, 1, 4, 1, 248, 1, 1, 1, 3),
    _HmComponentsDescr_Type()
)
hmComponentsDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmComponentsDescr.setStatus("current")
_HmComponentsURL_Type = DisplayString
_HmComponentsURL_Object = MibTableColumn
hmComponentsURL = _HmComponentsURL_Object(
    (1, 3, 6, 1, 4, 1, 248, 1, 1, 1, 4),
    _HmComponentsURL_Type()
)
hmComponentsURL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmComponentsURL.setStatus("current")
_HmComponentsOrderNumber_Type = DisplayString
_HmComponentsOrderNumber_Object = MibTableColumn
hmComponentsOrderNumber = _HmComponentsOrderNumber_Object(
    (1, 3, 6, 1, 4, 1, 248, 1, 1, 1, 5),
    _HmComponentsOrderNumber_Type()
)
hmComponentsOrderNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmComponentsOrderNumber.setStatus("current")
_HmFirmware_ObjectIdentity = ObjectIdentity
hmFirmware = _HmFirmware_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 2)
)
_HmFirmwareVersion_Type = DisplayString
_HmFirmwareVersion_Object = MibScalar
hmFirmwareVersion = _HmFirmwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 248, 2, 1),
    _HmFirmwareVersion_Type()
)
hmFirmwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmFirmwareVersion.setStatus("current")
_HmFirmwareState_Type = DisplayString
_HmFirmwareState_Object = MibScalar
hmFirmwareState = _HmFirmwareState_Object(
    (1, 3, 6, 1, 4, 1, 248, 2, 2),
    _HmFirmwareState_Type()
)
hmFirmwareState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmFirmwareState.setStatus("current")
_HmFirmwareDate_Type = DisplayString
_HmFirmwareDate_Object = MibScalar
hmFirmwareDate = _HmFirmwareDate_Object(
    (1, 3, 6, 1, 4, 1, 248, 2, 3),
    _HmFirmwareDate_Type()
)
hmFirmwareDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmFirmwareDate.setStatus("current")
_HmFirmwareTime_Type = DisplayString
_HmFirmwareTime_Object = MibScalar
hmFirmwareTime = _HmFirmwareTime_Object(
    (1, 3, 6, 1, 4, 1, 248, 2, 4),
    _HmFirmwareTime_Type()
)
hmFirmwareTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmFirmwareTime.setStatus("current")
_HmFirmwareCopyright_Type = DisplayString
_HmFirmwareCopyright_Object = MibScalar
hmFirmwareCopyright = _HmFirmwareCopyright_Object(
    (1, 3, 6, 1, 4, 1, 248, 2, 5),
    _HmFirmwareCopyright_Type()
)
hmFirmwareCopyright.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmFirmwareCopyright.setStatus("current")
_HmNet_ObjectIdentity = ObjectIdentity
hmNet = _HmNet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 3)
)
_HmNetPhyAddress_Type = MacAddress
_HmNetPhyAddress_Object = MibScalar
hmNetPhyAddress = _HmNetPhyAddress_Object(
    (1, 3, 6, 1, 4, 1, 248, 3, 1),
    _HmNetPhyAddress_Type()
)
hmNetPhyAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmNetPhyAddress.setStatus("current")


class _HmNetIpAddress_Type(IpAddress):
    """Custom type hmNetIpAddress based on IpAddress"""
    defaultHexValue = "c0a80063"


_HmNetIpAddress_Type.__name__ = "IpAddress"
_HmNetIpAddress_Object = MibScalar
hmNetIpAddress = _HmNetIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 248, 3, 2),
    _HmNetIpAddress_Type()
)
hmNetIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmNetIpAddress.setStatus("current")


class _HmNetSubnetmask_Type(IpAddress):
    """Custom type hmNetSubnetmask based on IpAddress"""
    defaultHexValue = "ffff0000"


_HmNetSubnetmask_Type.__name__ = "IpAddress"
_HmNetSubnetmask_Object = MibScalar
hmNetSubnetmask = _HmNetSubnetmask_Object(
    (1, 3, 6, 1, 4, 1, 248, 3, 3),
    _HmNetSubnetmask_Type()
)
hmNetSubnetmask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmNetSubnetmask.setStatus("current")


class _HmNetGwIpAddress_Type(IpAddress):
    """Custom type hmNetGwIpAddress based on IpAddress"""
    defaultHexValue = "00000000"


_HmNetGwIpAddress_Type.__name__ = "IpAddress"
_HmNetGwIpAddress_Object = MibScalar
hmNetGwIpAddress = _HmNetGwIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 248, 3, 4),
    _HmNetGwIpAddress_Type()
)
hmNetGwIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmNetGwIpAddress.setStatus("current")


class _HmNetAssignment_Type(Integer32):
    """Custom type hmNetAssignment based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              3)
        )
    )
    namedValues = NamedValues(
        *(("other", 0),
          ("static", 1),
          ("dhcp", 3))
    )


_HmNetAssignment_Type.__name__ = "Integer32"
_HmNetAssignment_Object = MibScalar
hmNetAssignment = _HmNetAssignment_Object(
    (1, 3, 6, 1, 4, 1, 248, 3, 7),
    _HmNetAssignment_Type()
)
hmNetAssignment.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmNetAssignment.setStatus("current")
_HmWLAN_ObjectIdentity = ObjectIdentity
hmWLAN = _HmWLAN_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 5)
)
_HmWLANParameter_ObjectIdentity = ObjectIdentity
hmWLANParameter = _HmWLANParameter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 5, 1)
)
_HmWLANParameterState_Type = EnabledDisabledStatus
_HmWLANParameterState_Object = MibScalar
hmWLANParameterState = _HmWLANParameterState_Object(
    (1, 3, 6, 1, 4, 1, 248, 5, 1, 1),
    _HmWLANParameterState_Type()
)
hmWLANParameterState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmWLANParameterState.setStatus("current")


class _HmWLANParameterSSID_Type(OctetString):
    """Custom type hmWLANParameterSSID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_HmWLANParameterSSID_Type.__name__ = "OctetString"
_HmWLANParameterSSID_Object = MibScalar
hmWLANParameterSSID = _HmWLANParameterSSID_Object(
    (1, 3, 6, 1, 4, 1, 248, 5, 1, 3),
    _HmWLANParameterSSID_Type()
)
hmWLANParameterSSID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmWLANParameterSSID.setStatus("current")


class _HmWLANParameterMode_Type(Integer32):
    """Custom type hmWLANParameterMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("a", 1),
          ("b", 2),
          ("bg", 3),
          ("an", 4),
          ("gn", 5),
          ("bgn", 6),
          ("abgn", 7))
    )


_HmWLANParameterMode_Type.__name__ = "Integer32"
_HmWLANParameterMode_Object = MibScalar
hmWLANParameterMode = _HmWLANParameterMode_Object(
    (1, 3, 6, 1, 4, 1, 248, 5, 1, 4),
    _HmWLANParameterMode_Type()
)
hmWLANParameterMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmWLANParameterMode.setStatus("current")


class _HmWLANParameterChannel_Type(Integer32):
    """Custom type hmWLANParameterChannel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_HmWLANParameterChannel_Type.__name__ = "Integer32"
_HmWLANParameterChannel_Object = MibScalar
hmWLANParameterChannel = _HmWLANParameterChannel_Object(
    (1, 3, 6, 1, 4, 1, 248, 5, 1, 5),
    _HmWLANParameterChannel_Type()
)
hmWLANParameterChannel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmWLANParameterChannel.setStatus("current")
_HmWLANSecurity_ObjectIdentity = ObjectIdentity
hmWLANSecurity = _HmWLANSecurity_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 5, 2)
)


class _HmWLANSecurityMode_Type(Integer32):
    """Custom type hmWLANSecurityMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("wpapsk", 1),
          ("wep64", 2),
          ("wep128", 3))
    )


_HmWLANSecurityMode_Type.__name__ = "Integer32"
_HmWLANSecurityMode_Object = MibScalar
hmWLANSecurityMode = _HmWLANSecurityMode_Object(
    (1, 3, 6, 1, 4, 1, 248, 5, 2, 1),
    _HmWLANSecurityMode_Type()
)
hmWLANSecurityMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmWLANSecurityMode.setStatus("current")


class _HmWLANSecurityWpaEncryptionAlgorithm_Type(Integer32):
    """Custom type hmWLANSecurityWpaEncryptionAlgorithm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("tkip", 1),
          ("aes", 2),
          ("both", 3))
    )


_HmWLANSecurityWpaEncryptionAlgorithm_Type.__name__ = "Integer32"
_HmWLANSecurityWpaEncryptionAlgorithm_Object = MibScalar
hmWLANSecurityWpaEncryptionAlgorithm = _HmWLANSecurityWpaEncryptionAlgorithm_Object(
    (1, 3, 6, 1, 4, 1, 248, 5, 2, 2),
    _HmWLANSecurityWpaEncryptionAlgorithm_Type()
)
hmWLANSecurityWpaEncryptionAlgorithm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmWLANSecurityWpaEncryptionAlgorithm.setStatus("current")


class _HmWLANSecurityWpaPsk_Type(OctetString):
    """Custom type hmWLANSecurityWpaPsk based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_HmWLANSecurityWpaPsk_Type.__name__ = "OctetString"
_HmWLANSecurityWpaPsk_Object = MibScalar
hmWLANSecurityWpaPsk = _HmWLANSecurityWpaPsk_Object(
    (1, 3, 6, 1, 4, 1, 248, 5, 2, 3),
    _HmWLANSecurityWpaPsk_Type()
)
hmWLANSecurityWpaPsk.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmWLANSecurityWpaPsk.setStatus("current")


class _HmWLANSecurityWepAuthType_Type(Integer32):
    """Custom type hmWLANSecurityWepAuthType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("opensystem", 0),
          ("sharedkey", 1),
          ("wpawpa2psk", 2))
    )


_HmWLANSecurityWepAuthType_Type.__name__ = "Integer32"
_HmWLANSecurityWepAuthType_Object = MibScalar
hmWLANSecurityWepAuthType = _HmWLANSecurityWepAuthType_Object(
    (1, 3, 6, 1, 4, 1, 248, 5, 2, 4),
    _HmWLANSecurityWepAuthType_Type()
)
hmWLANSecurityWepAuthType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmWLANSecurityWepAuthType.setStatus("current")


class _HmWLANSecurityWepKeyEncoding_Type(Integer32):
    """Custom type hmWLANSecurityWepKeyEncoding based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("hex", 0),
          ("ascii", 1))
    )


_HmWLANSecurityWepKeyEncoding_Type.__name__ = "Integer32"
_HmWLANSecurityWepKeyEncoding_Object = MibScalar
hmWLANSecurityWepKeyEncoding = _HmWLANSecurityWepKeyEncoding_Object(
    (1, 3, 6, 1, 4, 1, 248, 5, 2, 5),
    _HmWLANSecurityWepKeyEncoding_Type()
)
hmWLANSecurityWepKeyEncoding.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmWLANSecurityWepKeyEncoding.setStatus("current")


class _HmWLANSecurityWepKey_Type(OctetString):
    """Custom type hmWLANSecurityWepKey based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(5, 26),
    )


_HmWLANSecurityWepKey_Type.__name__ = "OctetString"
_HmWLANSecurityWepKey_Object = MibScalar
hmWLANSecurityWepKey = _HmWLANSecurityWepKey_Object(
    (1, 3, 6, 1, 4, 1, 248, 5, 2, 6),
    _HmWLANSecurityWepKey_Type()
)
hmWLANSecurityWepKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmWLANSecurityWepKey.setStatus("current")
_HmWLANVisibleAccessPointTable_Object = MibTable
hmWLANVisibleAccessPointTable = _HmWLANVisibleAccessPointTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 5, 3)
)
if mibBuilder.loadTexts:
    hmWLANVisibleAccessPointTable.setStatus("current")
_HmWLANVisibleAccessPointEntry_Object = MibTableRow
hmWLANVisibleAccessPointEntry = _HmWLANVisibleAccessPointEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 5, 3, 1)
)
hmWLANVisibleAccessPointEntry.setIndexNames(
    (0, "HIRSCHMANN-BAT-C-MIB", "hmWLANVisibleAccessPointEntryIdx"),
)
if mibBuilder.loadTexts:
    hmWLANVisibleAccessPointEntry.setStatus("current")


class _HmWLANVisibleAccessPointEntryIdx_Type(Integer32):
    """Custom type hmWLANVisibleAccessPointEntryIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 49),
    )


_HmWLANVisibleAccessPointEntryIdx_Type.__name__ = "Integer32"
_HmWLANVisibleAccessPointEntryIdx_Object = MibTableColumn
hmWLANVisibleAccessPointEntryIdx = _HmWLANVisibleAccessPointEntryIdx_Object(
    (1, 3, 6, 1, 4, 1, 248, 5, 3, 1, 1),
    _HmWLANVisibleAccessPointEntryIdx_Type()
)
hmWLANVisibleAccessPointEntryIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hmWLANVisibleAccessPointEntryIdx.setStatus("current")
_HmWLANVisibleAccessPointEntrySNR_Type = Integer32
_HmWLANVisibleAccessPointEntrySNR_Object = MibTableColumn
hmWLANVisibleAccessPointEntrySNR = _HmWLANVisibleAccessPointEntrySNR_Object(
    (1, 3, 6, 1, 4, 1, 248, 5, 3, 1, 2),
    _HmWLANVisibleAccessPointEntrySNR_Type()
)
hmWLANVisibleAccessPointEntrySNR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmWLANVisibleAccessPointEntrySNR.setStatus("current")


class _HmWLANVisibleAccessPointEntryChannel_Type(Integer32):
    """Custom type hmWLANVisibleAccessPointEntryChannel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_HmWLANVisibleAccessPointEntryChannel_Type.__name__ = "Integer32"
_HmWLANVisibleAccessPointEntryChannel_Object = MibTableColumn
hmWLANVisibleAccessPointEntryChannel = _HmWLANVisibleAccessPointEntryChannel_Object(
    (1, 3, 6, 1, 4, 1, 248, 5, 3, 1, 3),
    _HmWLANVisibleAccessPointEntryChannel_Type()
)
hmWLANVisibleAccessPointEntryChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmWLANVisibleAccessPointEntryChannel.setStatus("current")


class _HmWLANVisibleAccessPointEntryPower_Type(Integer32):
    """Custom type hmWLANVisibleAccessPointEntryPower based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_HmWLANVisibleAccessPointEntryPower_Type.__name__ = "Integer32"
_HmWLANVisibleAccessPointEntryPower_Object = MibTableColumn
hmWLANVisibleAccessPointEntryPower = _HmWLANVisibleAccessPointEntryPower_Object(
    (1, 3, 6, 1, 4, 1, 248, 5, 3, 1, 4),
    _HmWLANVisibleAccessPointEntryPower_Type()
)
hmWLANVisibleAccessPointEntryPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmWLANVisibleAccessPointEntryPower.setStatus("current")
_HmWLANVisibleAccessPointEntrySSID_Type = OctetString
_HmWLANVisibleAccessPointEntrySSID_Object = MibTableColumn
hmWLANVisibleAccessPointEntrySSID = _HmWLANVisibleAccessPointEntrySSID_Object(
    (1, 3, 6, 1, 4, 1, 248, 5, 3, 1, 5),
    _HmWLANVisibleAccessPointEntrySSID_Type()
)
hmWLANVisibleAccessPointEntrySSID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmWLANVisibleAccessPointEntrySSID.setStatus("current")
_HmWLANVisibleAccessPointEntrySecurity_Type = OctetString
_HmWLANVisibleAccessPointEntrySecurity_Object = MibTableColumn
hmWLANVisibleAccessPointEntrySecurity = _HmWLANVisibleAccessPointEntrySecurity_Object(
    (1, 3, 6, 1, 4, 1, 248, 5, 3, 1, 6),
    _HmWLANVisibleAccessPointEntrySecurity_Type()
)
hmWLANVisibleAccessPointEntrySecurity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmWLANVisibleAccessPointEntrySecurity.setStatus("current")
_HmWLANVisibleAccessPointEntryAddress_Type = MacAddress
_HmWLANVisibleAccessPointEntryAddress_Object = MibTableColumn
hmWLANVisibleAccessPointEntryAddress = _HmWLANVisibleAccessPointEntryAddress_Object(
    (1, 3, 6, 1, 4, 1, 248, 5, 3, 1, 7),
    _HmWLANVisibleAccessPointEntryAddress_Type()
)
hmWLANVisibleAccessPointEntryAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmWLANVisibleAccessPointEntryAddress.setStatus("current")


class _HmWLANVisibleAccessPointEntryConnected_Type(Integer32):
    """Custom type hmWLANVisibleAccessPointEntryConnected based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_HmWLANVisibleAccessPointEntryConnected_Type.__name__ = "Integer32"
_HmWLANVisibleAccessPointEntryConnected_Object = MibTableColumn
hmWLANVisibleAccessPointEntryConnected = _HmWLANVisibleAccessPointEntryConnected_Object(
    (1, 3, 6, 1, 4, 1, 248, 5, 3, 1, 8),
    _HmWLANVisibleAccessPointEntryConnected_Type()
)
hmWLANVisibleAccessPointEntryConnected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmWLANVisibleAccessPointEntryConnected.setStatus("current")
_HmWLANVisibleAccessPointEntryRSSI_Type = Integer32
_HmWLANVisibleAccessPointEntryRSSI_Object = MibTableColumn
hmWLANVisibleAccessPointEntryRSSI = _HmWLANVisibleAccessPointEntryRSSI_Object(
    (1, 3, 6, 1, 4, 1, 248, 5, 3, 1, 9),
    _HmWLANVisibleAccessPointEntryRSSI_Type()
)
hmWLANVisibleAccessPointEntryRSSI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmWLANVisibleAccessPointEntryRSSI.setStatus("current")
_HmWLANVisibleAccessPointEntryNoise_Type = Integer32
_HmWLANVisibleAccessPointEntryNoise_Object = MibTableColumn
hmWLANVisibleAccessPointEntryNoise = _HmWLANVisibleAccessPointEntryNoise_Object(
    (1, 3, 6, 1, 4, 1, 248, 5, 3, 1, 10),
    _HmWLANVisibleAccessPointEntryNoise_Type()
)
hmWLANVisibleAccessPointEntryNoise.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmWLANVisibleAccessPointEntryNoise.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HIRSCHMANN-BAT-C-MIB",
    **{"EnabledDisabledStatus": EnabledDisabledStatus,
       "hirschmann": hirschmann,
       "hmComponents": hmComponents,
       "hmComponentsTable": hmComponentsTable,
       "hmComponentsEntry": hmComponentsEntry,
       "hmComponentsIndex": hmComponentsIndex,
       "hmComponentsName": hmComponentsName,
       "hmComponentsDescr": hmComponentsDescr,
       "hmComponentsURL": hmComponentsURL,
       "hmComponentsOrderNumber": hmComponentsOrderNumber,
       "hmFirmware": hmFirmware,
       "hmFirmwareVersion": hmFirmwareVersion,
       "hmFirmwareState": hmFirmwareState,
       "hmFirmwareDate": hmFirmwareDate,
       "hmFirmwareTime": hmFirmwareTime,
       "hmFirmwareCopyright": hmFirmwareCopyright,
       "hmNet": hmNet,
       "hmNetPhyAddress": hmNetPhyAddress,
       "hmNetIpAddress": hmNetIpAddress,
       "hmNetSubnetmask": hmNetSubnetmask,
       "hmNetGwIpAddress": hmNetGwIpAddress,
       "hmNetAssignment": hmNetAssignment,
       "hmWLAN": hmWLAN,
       "hmWLANParameter": hmWLANParameter,
       "hmWLANParameterState": hmWLANParameterState,
       "hmWLANParameterSSID": hmWLANParameterSSID,
       "hmWLANParameterMode": hmWLANParameterMode,
       "hmWLANParameterChannel": hmWLANParameterChannel,
       "hmWLANSecurity": hmWLANSecurity,
       "hmWLANSecurityMode": hmWLANSecurityMode,
       "hmWLANSecurityWpaEncryptionAlgorithm": hmWLANSecurityWpaEncryptionAlgorithm,
       "hmWLANSecurityWpaPsk": hmWLANSecurityWpaPsk,
       "hmWLANSecurityWepAuthType": hmWLANSecurityWepAuthType,
       "hmWLANSecurityWepKeyEncoding": hmWLANSecurityWepKeyEncoding,
       "hmWLANSecurityWepKey": hmWLANSecurityWepKey,
       "hmWLANVisibleAccessPointTable": hmWLANVisibleAccessPointTable,
       "hmWLANVisibleAccessPointEntry": hmWLANVisibleAccessPointEntry,
       "hmWLANVisibleAccessPointEntryIdx": hmWLANVisibleAccessPointEntryIdx,
       "hmWLANVisibleAccessPointEntrySNR": hmWLANVisibleAccessPointEntrySNR,
       "hmWLANVisibleAccessPointEntryChannel": hmWLANVisibleAccessPointEntryChannel,
       "hmWLANVisibleAccessPointEntryPower": hmWLANVisibleAccessPointEntryPower,
       "hmWLANVisibleAccessPointEntrySSID": hmWLANVisibleAccessPointEntrySSID,
       "hmWLANVisibleAccessPointEntrySecurity": hmWLANVisibleAccessPointEntrySecurity,
       "hmWLANVisibleAccessPointEntryAddress": hmWLANVisibleAccessPointEntryAddress,
       "hmWLANVisibleAccessPointEntryConnected": hmWLANVisibleAccessPointEntryConnected,
       "hmWLANVisibleAccessPointEntryRSSI": hmWLANVisibleAccessPointEntryRSSI,
       "hmWLANVisibleAccessPointEntryNoise": hmWLANVisibleAccessPointEntryNoise,
       "hmModuleIdentity": hmModuleIdentity}
)
