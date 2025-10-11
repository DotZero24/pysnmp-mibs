# SNMP MIB module (OS-PWE3-ICCP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/mrv/OS-PWE3-ICCP-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:05:11 2025
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

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

(ModuleCompliance,
 NotificationGroup,
 ObjectGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup",
    "ObjectGroup")

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
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

osPwe3Iccp = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6926, 2, 29)
)
if mibBuilder.loadTexts:
    osPwe3Iccp.setRevisions(
        ("2014-07-06 13:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class AdminState(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("up", 1),
          ("down", 2))
    )



class BfdStatus(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )



class IccpStatus(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("nonExistent", 0),
          ("initialized", 1),
          ("capSent", 2),
          ("capRecv", 3),
          ("connecting", 4),
          ("operational", 5))
    )



class MlacpStatus(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("nonExistent", 0),
          ("reset", 1),
          ("connSent", 2),
          ("connRecv", 3),
          ("connecting", 4),
          ("operational", 5))
    )



# MIB Managed Objects in the order of their OIDs

_Oaccess_ObjectIdentity = ObjectIdentity
oaccess = _Oaccess_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6926)
)
_OaOptiSwitch_ObjectIdentity = ObjectIdentity
oaOptiSwitch = _OaOptiSwitch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6926, 2)
)
_OsPwe3IccpNotifications_ObjectIdentity = ObjectIdentity
osPwe3IccpNotifications = _OsPwe3IccpNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6926, 2, 29, 0)
)
_OsPwe3IccpObjects_ObjectIdentity = ObjectIdentity
osPwe3IccpObjects = _OsPwe3IccpObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6926, 2, 29, 1)
)
_OsPwe3IccpGen_ObjectIdentity = ObjectIdentity
osPwe3IccpGen = _OsPwe3IccpGen_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6926, 2, 29, 1, 1)
)


class _OsPwe3IccpSupport_Type(Integer32):
    """Custom type osPwe3IccpSupport based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notSupported", 1),
          ("supported", 2))
    )


_OsPwe3IccpSupport_Type.__name__ = "Integer32"
_OsPwe3IccpSupport_Object = MibScalar
osPwe3IccpSupport = _OsPwe3IccpSupport_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 29, 1, 1, 1),
    _OsPwe3IccpSupport_Type()
)
osPwe3IccpSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osPwe3IccpSupport.setStatus("current")
_OsPwe3IccpRGTable_Object = MibTable
osPwe3IccpRGTable = _OsPwe3IccpRGTable_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 29, 1, 2)
)
if mibBuilder.loadTexts:
    osPwe3IccpRGTable.setStatus("current")
_OsPwe3IccpRGEntry_Object = MibTableRow
osPwe3IccpRGEntry = _OsPwe3IccpRGEntry_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 29, 1, 2, 1)
)
osPwe3IccpRGEntry.setIndexNames(
    (0, "OS-PWE3-ICCP-MIB", "osPwe3IccpRGIndex"),
)
if mibBuilder.loadTexts:
    osPwe3IccpRGEntry.setStatus("current")


class _OsPwe3IccpRGIndex_Type(Unsigned32):
    """Custom type osPwe3IccpRGIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_OsPwe3IccpRGIndex_Type.__name__ = "Unsigned32"
_OsPwe3IccpRGIndex_Object = MibTableColumn
osPwe3IccpRGIndex = _OsPwe3IccpRGIndex_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 29, 1, 2, 1, 1),
    _OsPwe3IccpRGIndex_Type()
)
osPwe3IccpRGIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    osPwe3IccpRGIndex.setStatus("current")


class _OsPwe3IccpRGSenderName_Type(DisplayString):
    """Custom type osPwe3IccpRGSenderName based on DisplayString"""
    defaultValue = OctetString("")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_OsPwe3IccpRGSenderName_Type.__name__ = "DisplayString"
_OsPwe3IccpRGSenderName_Object = MibTableColumn
osPwe3IccpRGSenderName = _OsPwe3IccpRGSenderName_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 29, 1, 2, 1, 2),
    _OsPwe3IccpRGSenderName_Type()
)
osPwe3IccpRGSenderName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    osPwe3IccpRGSenderName.setStatus("current")


class _OsPwe3IccpRGPeerAddrType_Type(InetAddressType):
    """Custom type osPwe3IccpRGPeerAddrType based on InetAddressType"""
    defaultValue = 1


_OsPwe3IccpRGPeerAddrType_Type.__name__ = "InetAddressType"
_OsPwe3IccpRGPeerAddrType_Object = MibTableColumn
osPwe3IccpRGPeerAddrType = _OsPwe3IccpRGPeerAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 29, 1, 2, 1, 3),
    _OsPwe3IccpRGPeerAddrType_Type()
)
osPwe3IccpRGPeerAddrType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    osPwe3IccpRGPeerAddrType.setStatus("current")


class _OsPwe3IccpRGPeerAddr_Type(InetAddress):
    """Custom type osPwe3IccpRGPeerAddr based on InetAddress"""
    defaultHexValue = "00000000"


_OsPwe3IccpRGPeerAddr_Type.__name__ = "InetAddress"
_OsPwe3IccpRGPeerAddr_Object = MibTableColumn
osPwe3IccpRGPeerAddr = _OsPwe3IccpRGPeerAddr_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 29, 1, 2, 1, 4),
    _OsPwe3IccpRGPeerAddr_Type()
)
osPwe3IccpRGPeerAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    osPwe3IccpRGPeerAddr.setStatus("current")
_OsPwe3IccpRGStatus_Type = IccpStatus
_OsPwe3IccpRGStatus_Object = MibTableColumn
osPwe3IccpRGStatus = _OsPwe3IccpRGStatus_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 29, 1, 2, 1, 5),
    _OsPwe3IccpRGStatus_Type()
)
osPwe3IccpRGStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osPwe3IccpRGStatus.setStatus("current")


class _OsPwe3IccpRGBfdRef_Type(BfdStatus):
    """Custom type osPwe3IccpRGBfdRef based on BfdStatus"""
    defaultValue = 0


_OsPwe3IccpRGBfdRef_Type.__name__ = "BfdStatus"
_OsPwe3IccpRGBfdRef_Object = MibTableColumn
osPwe3IccpRGBfdRef = _OsPwe3IccpRGBfdRef_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 29, 1, 2, 1, 6),
    _OsPwe3IccpRGBfdRef_Type()
)
osPwe3IccpRGBfdRef.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    osPwe3IccpRGBfdRef.setStatus("current")


class _OsPwe3IccpRGLastError_Type(DisplayString):
    """Custom type osPwe3IccpRGLastError based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 160),
    )


_OsPwe3IccpRGLastError_Type.__name__ = "DisplayString"
_OsPwe3IccpRGLastError_Object = MibTableColumn
osPwe3IccpRGLastError = _OsPwe3IccpRGLastError_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 29, 1, 2, 1, 89),
    _OsPwe3IccpRGLastError_Type()
)
osPwe3IccpRGLastError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osPwe3IccpRGLastError.setStatus("current")


class _OsPwe3IccpRGRowStatus_Type(RowStatus):
    """Custom type osPwe3IccpRGRowStatus based on RowStatus"""
    defaultValue = 2


_OsPwe3IccpRGRowStatus_Type.__name__ = "RowStatus"
_OsPwe3IccpRGRowStatus_Object = MibTableColumn
osPwe3IccpRGRowStatus = _OsPwe3IccpRGRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 29, 1, 2, 1, 90),
    _OsPwe3IccpRGRowStatus_Type()
)
osPwe3IccpRGRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    osPwe3IccpRGRowStatus.setStatus("current")
_OsPwe3IccpMlacpAppTable_Object = MibTable
osPwe3IccpMlacpAppTable = _OsPwe3IccpMlacpAppTable_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 29, 1, 3)
)
if mibBuilder.loadTexts:
    osPwe3IccpMlacpAppTable.setStatus("current")
_OsPwe3IccpMlacpAppEntry_Object = MibTableRow
osPwe3IccpMlacpAppEntry = _OsPwe3IccpMlacpAppEntry_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 29, 1, 3, 1)
)
osPwe3IccpMlacpAppEntry.setIndexNames(
    (0, "OS-PWE3-ICCP-MIB", "osPwe3IccpMlacpIndex"),
)
if mibBuilder.loadTexts:
    osPwe3IccpMlacpAppEntry.setStatus("current")


class _OsPwe3IccpMlacpIndex_Type(Unsigned32):
    """Custom type osPwe3IccpMlacpIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_OsPwe3IccpMlacpIndex_Type.__name__ = "Unsigned32"
_OsPwe3IccpMlacpIndex_Object = MibTableColumn
osPwe3IccpMlacpIndex = _OsPwe3IccpMlacpIndex_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 29, 1, 3, 1, 1),
    _OsPwe3IccpMlacpIndex_Type()
)
osPwe3IccpMlacpIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    osPwe3IccpMlacpIndex.setStatus("current")


class _OsPwe3IccpMlacpChassisId_Type(Unsigned32):
    """Custom type osPwe3IccpMlacpChassisId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_OsPwe3IccpMlacpChassisId_Type.__name__ = "Unsigned32"
_OsPwe3IccpMlacpChassisId_Object = MibTableColumn
osPwe3IccpMlacpChassisId = _OsPwe3IccpMlacpChassisId_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 29, 1, 3, 1, 2),
    _OsPwe3IccpMlacpChassisId_Type()
)
osPwe3IccpMlacpChassisId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    osPwe3IccpMlacpChassisId.setStatus("current")


class _OsPwe3IccpMlacpSystemMac_Type(MacAddress):
    """Custom type osPwe3IccpMlacpSystemMac based on MacAddress"""
    defaultHexValue = "000000000000"


_OsPwe3IccpMlacpSystemMac_Type.__name__ = "MacAddress"
_OsPwe3IccpMlacpSystemMac_Object = MibTableColumn
osPwe3IccpMlacpSystemMac = _OsPwe3IccpMlacpSystemMac_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 29, 1, 3, 1, 3),
    _OsPwe3IccpMlacpSystemMac_Type()
)
osPwe3IccpMlacpSystemMac.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    osPwe3IccpMlacpSystemMac.setStatus("current")


class _OsPwe3IccpMlacpSystemPriority_Type(Unsigned32):
    """Custom type osPwe3IccpMlacpSystemPriority based on Unsigned32"""
    defaultValue = 32768

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_OsPwe3IccpMlacpSystemPriority_Type.__name__ = "Unsigned32"
_OsPwe3IccpMlacpSystemPriority_Object = MibTableColumn
osPwe3IccpMlacpSystemPriority = _OsPwe3IccpMlacpSystemPriority_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 29, 1, 3, 1, 4),
    _OsPwe3IccpMlacpSystemPriority_Type()
)
osPwe3IccpMlacpSystemPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    osPwe3IccpMlacpSystemPriority.setStatus("current")


class _OsPwe3IccpMlacpLastError_Type(DisplayString):
    """Custom type osPwe3IccpMlacpLastError based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 160),
    )


_OsPwe3IccpMlacpLastError_Type.__name__ = "DisplayString"
_OsPwe3IccpMlacpLastError_Object = MibTableColumn
osPwe3IccpMlacpLastError = _OsPwe3IccpMlacpLastError_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 29, 1, 3, 1, 5),
    _OsPwe3IccpMlacpLastError_Type()
)
osPwe3IccpMlacpLastError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osPwe3IccpMlacpLastError.setStatus("current")
_OsPwe3IccpMlacpStatus_Type = MlacpStatus
_OsPwe3IccpMlacpStatus_Object = MibTableColumn
osPwe3IccpMlacpStatus = _OsPwe3IccpMlacpStatus_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 29, 1, 3, 1, 6),
    _OsPwe3IccpMlacpStatus_Type()
)
osPwe3IccpMlacpStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osPwe3IccpMlacpStatus.setStatus("current")


class _OsPwe3IccpMlacpRowStatus_Type(RowStatus):
    """Custom type osPwe3IccpMlacpRowStatus based on RowStatus"""
    defaultValue = 2


_OsPwe3IccpMlacpRowStatus_Type.__name__ = "RowStatus"
_OsPwe3IccpMlacpRowStatus_Object = MibTableColumn
osPwe3IccpMlacpRowStatus = _OsPwe3IccpMlacpRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 29, 1, 3, 1, 7),
    _OsPwe3IccpMlacpRowStatus_Type()
)
osPwe3IccpMlacpRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    osPwe3IccpMlacpRowStatus.setStatus("current")
_OsPwe3IccpMlacpAggTable_Object = MibTable
osPwe3IccpMlacpAggTable = _OsPwe3IccpMlacpAggTable_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 29, 1, 4)
)
if mibBuilder.loadTexts:
    osPwe3IccpMlacpAggTable.setStatus("current")
_OsPwe3IccpMlacpAggEntry_Object = MibTableRow
osPwe3IccpMlacpAggEntry = _OsPwe3IccpMlacpAggEntry_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 29, 1, 4, 1)
)
osPwe3IccpMlacpAggEntry.setIndexNames(
    (0, "OS-PWE3-ICCP-MIB", "osPwe3IccpMlacpAggIndex"),
)
if mibBuilder.loadTexts:
    osPwe3IccpMlacpAggEntry.setStatus("current")


class _OsPwe3IccpMlacpAggIndex_Type(Unsigned32):
    """Custom type osPwe3IccpMlacpAggIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 128),
    )


_OsPwe3IccpMlacpAggIndex_Type.__name__ = "Unsigned32"
_OsPwe3IccpMlacpAggIndex_Object = MibTableColumn
osPwe3IccpMlacpAggIndex = _OsPwe3IccpMlacpAggIndex_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 29, 1, 4, 1, 1),
    _OsPwe3IccpMlacpAggIndex_Type()
)
osPwe3IccpMlacpAggIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    osPwe3IccpMlacpAggIndex.setStatus("current")


class _OsPwe3IccpMlacpAggIccpIndex_Type(Unsigned32):
    """Custom type osPwe3IccpMlacpAggIccpIndex based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 65535),
    )


_OsPwe3IccpMlacpAggIccpIndex_Type.__name__ = "Unsigned32"
_OsPwe3IccpMlacpAggIccpIndex_Object = MibTableColumn
osPwe3IccpMlacpAggIccpIndex = _OsPwe3IccpMlacpAggIccpIndex_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 29, 1, 4, 1, 2),
    _OsPwe3IccpMlacpAggIccpIndex_Type()
)
osPwe3IccpMlacpAggIccpIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    osPwe3IccpMlacpAggIccpIndex.setStatus("current")


class _OsPwe3IccpMlacpAggMode_Type(Integer32):
    """Custom type osPwe3IccpMlacpAggMode based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("undefined", 0),
          ("activeStandby", 1),
          ("activeActive", 2))
    )


_OsPwe3IccpMlacpAggMode_Type.__name__ = "Integer32"
_OsPwe3IccpMlacpAggMode_Object = MibTableColumn
osPwe3IccpMlacpAggMode = _OsPwe3IccpMlacpAggMode_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 29, 1, 4, 1, 3),
    _OsPwe3IccpMlacpAggMode_Type()
)
osPwe3IccpMlacpAggMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    osPwe3IccpMlacpAggMode.setStatus("current")


class _OsPwe3IccpMlacpAggRole_Type(Integer32):
    """Custom type osPwe3IccpMlacpAggRole based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("undefined", 0),
          ("active", 1),
          ("standby", 2))
    )


_OsPwe3IccpMlacpAggRole_Type.__name__ = "Integer32"
_OsPwe3IccpMlacpAggRole_Object = MibTableColumn
osPwe3IccpMlacpAggRole = _OsPwe3IccpMlacpAggRole_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 29, 1, 4, 1, 4),
    _OsPwe3IccpMlacpAggRole_Type()
)
osPwe3IccpMlacpAggRole.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    osPwe3IccpMlacpAggRole.setStatus("current")


class _OsPwe3IccpMlacpAggActiveRole_Type(Integer32):
    """Custom type osPwe3IccpMlacpAggActiveRole based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("undefined", 0),
          ("active", 1),
          ("standby", 2))
    )


_OsPwe3IccpMlacpAggActiveRole_Type.__name__ = "Integer32"
_OsPwe3IccpMlacpAggActiveRole_Object = MibTableColumn
osPwe3IccpMlacpAggActiveRole = _OsPwe3IccpMlacpAggActiveRole_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 29, 1, 4, 1, 5),
    _OsPwe3IccpMlacpAggActiveRole_Type()
)
osPwe3IccpMlacpAggActiveRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osPwe3IccpMlacpAggActiveRole.setStatus("current")


class _OsPwe3IccpMlacpAggRevertive_Type(Integer32):
    """Custom type osPwe3IccpMlacpAggRevertive based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 3600),
    )


_OsPwe3IccpMlacpAggRevertive_Type.__name__ = "Integer32"
_OsPwe3IccpMlacpAggRevertive_Object = MibTableColumn
osPwe3IccpMlacpAggRevertive = _OsPwe3IccpMlacpAggRevertive_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 29, 1, 4, 1, 6),
    _OsPwe3IccpMlacpAggRevertive_Type()
)
osPwe3IccpMlacpAggRevertive.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    osPwe3IccpMlacpAggRevertive.setStatus("current")


class _OsPwe3IccpMlacpAggThreshold_Type(Integer32):
    """Custom type osPwe3IccpMlacpAggThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_OsPwe3IccpMlacpAggThreshold_Type.__name__ = "Integer32"
_OsPwe3IccpMlacpAggThreshold_Object = MibTableColumn
osPwe3IccpMlacpAggThreshold = _OsPwe3IccpMlacpAggThreshold_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 29, 1, 4, 1, 7),
    _OsPwe3IccpMlacpAggThreshold_Type()
)
osPwe3IccpMlacpAggThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    osPwe3IccpMlacpAggThreshold.setStatus("current")
if mibBuilder.loadTexts:
    osPwe3IccpMlacpAggThreshold.setUnits("Precentage")


class _OsPwe3IccpMlacpAggCommand_Type(Integer32):
    """Custom type osPwe3IccpMlacpAggCommand based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("forceSwitch", 2),
          ("revertSwitch", 3))
    )


_OsPwe3IccpMlacpAggCommand_Type.__name__ = "Integer32"
_OsPwe3IccpMlacpAggCommand_Object = MibTableColumn
osPwe3IccpMlacpAggCommand = _OsPwe3IccpMlacpAggCommand_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 29, 1, 4, 1, 8),
    _OsPwe3IccpMlacpAggCommand_Type()
)
osPwe3IccpMlacpAggCommand.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    osPwe3IccpMlacpAggCommand.setStatus("current")


class _OsPwe3IccpMlacpAggSwCause_Type(Integer32):
    """Custom type osPwe3IccpMlacpAggSwCause based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("undefined", 0),
          ("local", 1),
          ("remote", 2),
          ("acFail", 3),
          ("force", 4),
          ("reverting", 5))
    )


_OsPwe3IccpMlacpAggSwCause_Type.__name__ = "Integer32"
_OsPwe3IccpMlacpAggSwCause_Object = MibTableColumn
osPwe3IccpMlacpAggSwCause = _OsPwe3IccpMlacpAggSwCause_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 29, 1, 4, 1, 9),
    _OsPwe3IccpMlacpAggSwCause_Type()
)
osPwe3IccpMlacpAggSwCause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osPwe3IccpMlacpAggSwCause.setStatus("current")


class _OsPwe3IccpMlacpAggLastError_Type(DisplayString):
    """Custom type osPwe3IccpMlacpAggLastError based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 160),
    )


_OsPwe3IccpMlacpAggLastError_Type.__name__ = "DisplayString"
_OsPwe3IccpMlacpAggLastError_Object = MibTableColumn
osPwe3IccpMlacpAggLastError = _OsPwe3IccpMlacpAggLastError_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 29, 1, 4, 1, 89),
    _OsPwe3IccpMlacpAggLastError_Type()
)
osPwe3IccpMlacpAggLastError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osPwe3IccpMlacpAggLastError.setStatus("current")


class _OsPwe3IccpMlacpAggRowStatus_Type(RowStatus):
    """Custom type osPwe3IccpMlacpAggRowStatus based on RowStatus"""
    defaultValue = 2


_OsPwe3IccpMlacpAggRowStatus_Type.__name__ = "RowStatus"
_OsPwe3IccpMlacpAggRowStatus_Object = MibTableColumn
osPwe3IccpMlacpAggRowStatus = _OsPwe3IccpMlacpAggRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 29, 1, 4, 1, 90),
    _OsPwe3IccpMlacpAggRowStatus_Type()
)
osPwe3IccpMlacpAggRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    osPwe3IccpMlacpAggRowStatus.setStatus("current")
_OsPwe3IccpConf_ObjectIdentity = ObjectIdentity
osPwe3IccpConf = _OsPwe3IccpConf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6926, 2, 29, 2)
)
_OsPwe3IccpGroups_ObjectIdentity = ObjectIdentity
osPwe3IccpGroups = _OsPwe3IccpGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6926, 2, 29, 2, 1)
)
_OsPwe3IccpCompliances_ObjectIdentity = ObjectIdentity
osPwe3IccpCompliances = _OsPwe3IccpCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6926, 2, 29, 2, 2)
)

# Managed Objects groups

osPwe3IccpGenGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6926, 2, 29, 2, 1, 2)
)
osPwe3IccpGenGroup.setObjects(
    ("OS-PWE3-ICCP-MIB", "osPwe3IccpSupport")
)
if mibBuilder.loadTexts:
    osPwe3IccpGenGroup.setStatus("current")

osPwe3IccpRGGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6926, 2, 29, 2, 1, 3)
)
osPwe3IccpRGGroup.setObjects(
      *(("OS-PWE3-ICCP-MIB", "osPwe3IccpRGSenderName"),
        ("OS-PWE3-ICCP-MIB", "osPwe3IccpRGPeerAddrType"),
        ("OS-PWE3-ICCP-MIB", "osPwe3IccpRGPeerAddr"),
        ("OS-PWE3-ICCP-MIB", "osPwe3IccpRGStatus"),
        ("OS-PWE3-ICCP-MIB", "osPwe3IccpRGBfdRef"),
        ("OS-PWE3-ICCP-MIB", "osPwe3IccpRGLastError"),
        ("OS-PWE3-ICCP-MIB", "osPwe3IccpRGRowStatus"))
)
if mibBuilder.loadTexts:
    osPwe3IccpRGGroup.setStatus("current")

osPwe3IccpMlacpAggGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6926, 2, 29, 2, 1, 4)
)
osPwe3IccpMlacpAggGroup.setObjects(
      *(("OS-PWE3-ICCP-MIB", "osPwe3IccpMlacpAggIccpIndex"),
        ("OS-PWE3-ICCP-MIB", "osPwe3IccpMlacpAggMode"),
        ("OS-PWE3-ICCP-MIB", "osPwe3IccpMlacpAggRevertive"),
        ("OS-PWE3-ICCP-MIB", "osPwe3IccpMlacpAggRowStatus"),
        ("OS-PWE3-ICCP-MIB", "osPwe3IccpMlacpAggThreshold"),
        ("OS-PWE3-ICCP-MIB", "osPwe3IccpMlacpAggCommand"),
        ("OS-PWE3-ICCP-MIB", "osPwe3IccpMlacpAggRole"),
        ("OS-PWE3-ICCP-MIB", "osPwe3IccpMlacpAggActiveRole"),
        ("OS-PWE3-ICCP-MIB", "osPwe3IccpMlacpAggSwCause"),
        ("OS-PWE3-ICCP-MIB", "osPwe3IccpMlacpAggLastError"))
)
if mibBuilder.loadTexts:
    osPwe3IccpMlacpAggGroup.setStatus("current")

osPwe3IccpMlacpAppGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6926, 2, 29, 2, 1, 5)
)
osPwe3IccpMlacpAppGroup.setObjects(
      *(("OS-PWE3-ICCP-MIB", "osPwe3IccpMlacpChassisId"),
        ("OS-PWE3-ICCP-MIB", "osPwe3IccpMlacpSystemMac"),
        ("OS-PWE3-ICCP-MIB", "osPwe3IccpMlacpSystemPriority"),
        ("OS-PWE3-ICCP-MIB", "osPwe3IccpMlacpLastError"),
        ("OS-PWE3-ICCP-MIB", "osPwe3IccpMlacpStatus"),
        ("OS-PWE3-ICCP-MIB", "osPwe3IccpMlacpRowStatus"))
)
if mibBuilder.loadTexts:
    osPwe3IccpMlacpAppGroup.setStatus("current")


# Notification objects

osPwe3IccpRGUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 6926, 2, 29, 0, 1)
)
osPwe3IccpRGUp.setObjects(
    ("OS-PWE3-ICCP-MIB", "osPwe3IccpRGStatus")
)
if mibBuilder.loadTexts:
    osPwe3IccpRGUp.setStatus(
        "current"
    )

osPwe3IccpRGDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 6926, 2, 29, 0, 2)
)
osPwe3IccpRGDown.setObjects(
    ("OS-PWE3-ICCP-MIB", "osPwe3IccpRGStatus")
)
if mibBuilder.loadTexts:
    osPwe3IccpRGDown.setStatus(
        "current"
    )

osPwe3IccpMlacpUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 6926, 2, 29, 0, 3)
)
osPwe3IccpMlacpUp.setObjects(
    ("OS-PWE3-ICCP-MIB", "osPwe3IccpMlacpStatus")
)
if mibBuilder.loadTexts:
    osPwe3IccpMlacpUp.setStatus(
        "current"
    )

osPwe3IccpMlacpDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 6926, 2, 29, 0, 4)
)
osPwe3IccpMlacpDown.setObjects(
    ("OS-PWE3-ICCP-MIB", "osPwe3IccpMlacpStatus")
)
if mibBuilder.loadTexts:
    osPwe3IccpMlacpDown.setStatus(
        "current"
    )

osPwe3IccpMlacpAggChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 6926, 2, 29, 0, 5)
)
osPwe3IccpMlacpAggChange.setObjects(
      *(("OS-PWE3-ICCP-MIB", "osPwe3IccpMlacpAggActiveRole"),
        ("OS-PWE3-ICCP-MIB", "osPwe3IccpMlacpAggSwCause"))
)
if mibBuilder.loadTexts:
    osPwe3IccpMlacpAggChange.setStatus(
        "current"
    )


# Notifications groups

osPwe3IccpNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6926, 2, 29, 2, 1, 1)
)
osPwe3IccpNotificationGroup.setObjects(
      *(("OS-PWE3-ICCP-MIB", "osPwe3IccpRGUp"),
        ("OS-PWE3-ICCP-MIB", "osPwe3IccpRGDown"),
        ("OS-PWE3-ICCP-MIB", "osPwe3IccpMlacpUp"),
        ("OS-PWE3-ICCP-MIB", "osPwe3IccpMlacpDown"),
        ("OS-PWE3-ICCP-MIB", "osPwe3IccpMlacpAggChange"))
)
if mibBuilder.loadTexts:
    osPwe3IccpNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

osPwe3IccpModuleCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6926, 2, 29, 2, 2, 1)
)
osPwe3IccpModuleCompliance.setObjects(
      *(("OS-PWE3-ICCP-MIB", "osPwe3IccpGenGroup"),
        ("OS-PWE3-ICCP-MIB", "osPwe3IccpRGGroup"),
        ("OS-PWE3-ICCP-MIB", "osPwe3IccpMlacpAggGroup"),
        ("OS-PWE3-ICCP-MIB", "osPwe3IccpMlacpAppGroup"),
        ("OS-PWE3-ICCP-MIB", "osPwe3IccpNotificationGroup"))
)
if mibBuilder.loadTexts:
    osPwe3IccpModuleCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "OS-PWE3-ICCP-MIB",
    **{"AdminState": AdminState,
       "BfdStatus": BfdStatus,
       "IccpStatus": IccpStatus,
       "MlacpStatus": MlacpStatus,
       "oaccess": oaccess,
       "oaOptiSwitch": oaOptiSwitch,
       "osPwe3Iccp": osPwe3Iccp,
       "osPwe3IccpNotifications": osPwe3IccpNotifications,
       "osPwe3IccpRGUp": osPwe3IccpRGUp,
       "osPwe3IccpRGDown": osPwe3IccpRGDown,
       "osPwe3IccpMlacpUp": osPwe3IccpMlacpUp,
       "osPwe3IccpMlacpDown": osPwe3IccpMlacpDown,
       "osPwe3IccpMlacpAggChange": osPwe3IccpMlacpAggChange,
       "osPwe3IccpObjects": osPwe3IccpObjects,
       "osPwe3IccpGen": osPwe3IccpGen,
       "osPwe3IccpSupport": osPwe3IccpSupport,
       "osPwe3IccpRGTable": osPwe3IccpRGTable,
       "osPwe3IccpRGEntry": osPwe3IccpRGEntry,
       "osPwe3IccpRGIndex": osPwe3IccpRGIndex,
       "osPwe3IccpRGSenderName": osPwe3IccpRGSenderName,
       "osPwe3IccpRGPeerAddrType": osPwe3IccpRGPeerAddrType,
       "osPwe3IccpRGPeerAddr": osPwe3IccpRGPeerAddr,
       "osPwe3IccpRGStatus": osPwe3IccpRGStatus,
       "osPwe3IccpRGBfdRef": osPwe3IccpRGBfdRef,
       "osPwe3IccpRGLastError": osPwe3IccpRGLastError,
       "osPwe3IccpRGRowStatus": osPwe3IccpRGRowStatus,
       "osPwe3IccpMlacpAppTable": osPwe3IccpMlacpAppTable,
       "osPwe3IccpMlacpAppEntry": osPwe3IccpMlacpAppEntry,
       "osPwe3IccpMlacpIndex": osPwe3IccpMlacpIndex,
       "osPwe3IccpMlacpChassisId": osPwe3IccpMlacpChassisId,
       "osPwe3IccpMlacpSystemMac": osPwe3IccpMlacpSystemMac,
       "osPwe3IccpMlacpSystemPriority": osPwe3IccpMlacpSystemPriority,
       "osPwe3IccpMlacpLastError": osPwe3IccpMlacpLastError,
       "osPwe3IccpMlacpStatus": osPwe3IccpMlacpStatus,
       "osPwe3IccpMlacpRowStatus": osPwe3IccpMlacpRowStatus,
       "osPwe3IccpMlacpAggTable": osPwe3IccpMlacpAggTable,
       "osPwe3IccpMlacpAggEntry": osPwe3IccpMlacpAggEntry,
       "osPwe3IccpMlacpAggIndex": osPwe3IccpMlacpAggIndex,
       "osPwe3IccpMlacpAggIccpIndex": osPwe3IccpMlacpAggIccpIndex,
       "osPwe3IccpMlacpAggMode": osPwe3IccpMlacpAggMode,
       "osPwe3IccpMlacpAggRole": osPwe3IccpMlacpAggRole,
       "osPwe3IccpMlacpAggActiveRole": osPwe3IccpMlacpAggActiveRole,
       "osPwe3IccpMlacpAggRevertive": osPwe3IccpMlacpAggRevertive,
       "osPwe3IccpMlacpAggThreshold": osPwe3IccpMlacpAggThreshold,
       "osPwe3IccpMlacpAggCommand": osPwe3IccpMlacpAggCommand,
       "osPwe3IccpMlacpAggSwCause": osPwe3IccpMlacpAggSwCause,
       "osPwe3IccpMlacpAggLastError": osPwe3IccpMlacpAggLastError,
       "osPwe3IccpMlacpAggRowStatus": osPwe3IccpMlacpAggRowStatus,
       "osPwe3IccpConf": osPwe3IccpConf,
       "osPwe3IccpGroups": osPwe3IccpGroups,
       "osPwe3IccpNotificationGroup": osPwe3IccpNotificationGroup,
       "osPwe3IccpGenGroup": osPwe3IccpGenGroup,
       "osPwe3IccpRGGroup": osPwe3IccpRGGroup,
       "osPwe3IccpMlacpAggGroup": osPwe3IccpMlacpAggGroup,
       "osPwe3IccpMlacpAppGroup": osPwe3IccpMlacpAppGroup,
       "osPwe3IccpCompliances": osPwe3IccpCompliances,
       "osPwe3IccpModuleCompliance": osPwe3IccpModuleCompliance}
)
