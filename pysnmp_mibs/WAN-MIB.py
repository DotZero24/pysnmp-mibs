# SNMP MIB module (WAN-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/avaya/WAN-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:04:23 2025
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

(lsg,) = mibBuilder.importSymbols(
    "AVAYAGEN-MIB",
    "lsg")

(dsx0BundleCircuitIdentifier,
 dsx0BundleIfIndex,
 dsx0BundleIndex,
 dsx0BundleRowStatus) = mibBuilder.importSymbols(
    "DS0BUNDLE-MIB",
    "dsx0BundleCircuitIdentifier",
    "dsx0BundleIfIndex",
    "dsx0BundleIndex",
    "dsx0BundleRowStatus")

(DLCI,) = mibBuilder.importSymbols(
    "FRAME-RELAY-DTE-MIB",
    "DLCI")

(InterfaceIndex,
 ifAdminStatus,
 ifAlias,
 ifIndex,
 ifName,
 ifOperStatus) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "ifAdminStatus",
    "ifAlias",
    "ifIndex",
    "ifName",
    "ifOperStatus")

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
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

avayaEISWan = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 6)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class OnOff(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("on", 1),
          ("off", 2),
          ("notRelevant", 255))
    )



# MIB Managed Objects in the order of their OIDs

_DeviceSpecific_ObjectIdentity = ObjectIdentity
deviceSpecific = _DeviceSpecific_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 6, 1)
)
_X330wanSpecific_ObjectIdentity = ObjectIdentity
x330wanSpecific = _X330wanSpecific_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 6, 1, 1)
)
_IntWanPortTable_Object = MibTable
intWanPortTable = _IntWanPortTable_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 6, 1, 1, 1)
)
if mibBuilder.loadTexts:
    intWanPortTable.setStatus("current")
_IntWanPortEntry_Object = MibTableRow
intWanPortEntry = _IntWanPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 6, 1, 1, 1, 1)
)
intWanPortEntry.setIndexNames(
    (0, "WAN-MIB", "intWanGroupID"),
    (0, "WAN-MIB", "intWanPortID"),
)
if mibBuilder.loadTexts:
    intWanPortEntry.setStatus("current")


class _IntWanGroupID_Type(Integer32):
    """Custom type intWanGroupID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_IntWanGroupID_Type.__name__ = "Integer32"
_IntWanGroupID_Object = MibTableColumn
intWanGroupID = _IntWanGroupID_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 6, 1, 1, 1, 1, 1),
    _IntWanGroupID_Type()
)
intWanGroupID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    intWanGroupID.setStatus("current")


class _IntWanPortID_Type(Integer32):
    """Custom type intWanPortID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_IntWanPortID_Type.__name__ = "Integer32"
_IntWanPortID_Object = MibTableColumn
intWanPortID = _IntWanPortID_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 6, 1, 1, 1, 1, 2),
    _IntWanPortID_Type()
)
intWanPortID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    intWanPortID.setStatus("current")


class _IntWanPortSpeed_Type(Integer32):
    """Custom type intWanPortSpeed based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("ethernet", 1),
          ("fastEthernet", 2),
          ("notSupported", 255))
    )


_IntWanPortSpeed_Type.__name__ = "Integer32"
_IntWanPortSpeed_Object = MibTableColumn
intWanPortSpeed = _IntWanPortSpeed_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 6, 1, 1, 1, 1, 3),
    _IntWanPortSpeed_Type()
)
intWanPortSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    intWanPortSpeed.setStatus("current")


class _IntWanPortMode_Type(Integer32):
    """Custom type intWanPortMode based on Integer32"""
    defaultValue = 7

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              7,
              255)
        )
    )
    namedValues = NamedValues(
        *(("halfDuplex", 1),
          ("fullDuplexSymPause", 7),
          ("notSupported", 255))
    )


_IntWanPortMode_Type.__name__ = "Integer32"
_IntWanPortMode_Object = MibTableColumn
intWanPortMode = _IntWanPortMode_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 6, 1, 1, 1, 1, 4),
    _IntWanPortMode_Type()
)
intWanPortMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    intWanPortMode.setStatus("current")


class _IntWanPortAutoNegotiation_Type(Integer32):
    """Custom type intWanPortAutoNegotiation based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2),
          ("notSupported", 255))
    )


_IntWanPortAutoNegotiation_Type.__name__ = "Integer32"
_IntWanPortAutoNegotiation_Object = MibTableColumn
intWanPortAutoNegotiation = _IntWanPortAutoNegotiation_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 6, 1, 1, 1, 1, 5),
    _IntWanPortAutoNegotiation_Type()
)
intWanPortAutoNegotiation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    intWanPortAutoNegotiation.setStatus("current")


class _IntWanPortVLANMode_Type(Integer32):
    """Custom type intWanPortVLANMode based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("perPortOnly", 1),
          ("dot1QTagging", 2),
          ("notSupported", 255))
    )


_IntWanPortVLANMode_Type.__name__ = "Integer32"
_IntWanPortVLANMode_Object = MibTableColumn
intWanPortVLANMode = _IntWanPortVLANMode_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 6, 1, 1, 1, 1, 6),
    _IntWanPortVLANMode_Type()
)
intWanPortVLANMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    intWanPortVLANMode.setStatus("current")


class _IntWanPortVLANBindingMode_Type(Integer32):
    """Custom type intWanPortVLANBindingMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              255)
        )
    )
    namedValues = NamedValues(
        *(("static", 1),
          ("bindToReceive", 2),
          ("bindToAll", 3),
          ("notSupported", 255))
    )


_IntWanPortVLANBindingMode_Type.__name__ = "Integer32"
_IntWanPortVLANBindingMode_Object = MibTableColumn
intWanPortVLANBindingMode = _IntWanPortVLANBindingMode_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 6, 1, 1, 1, 1, 7),
    _IntWanPortVLANBindingMode_Type()
)
intWanPortVLANBindingMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    intWanPortVLANBindingMode.setStatus("current")
_IntWanPortVlanList_Type = OctetString
_IntWanPortVlanList_Object = MibTableColumn
intWanPortVlanList = _IntWanPortVlanList_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 6, 1, 1, 1, 1, 8),
    _IntWanPortVlanList_Type()
)
intWanPortVlanList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    intWanPortVlanList.setStatus("current")
_Ds0BundleMemmbersTable_Object = MibTable
ds0BundleMemmbersTable = _Ds0BundleMemmbersTable_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 6, 1, 1, 2)
)
if mibBuilder.loadTexts:
    ds0BundleMemmbersTable.setStatus("current")
_Ds0BundleMemmbersEntry_Object = MibTableRow
ds0BundleMemmbersEntry = _Ds0BundleMemmbersEntry_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 6, 1, 1, 2, 1)
)
ds0BundleMemmbersEntry.setIndexNames(
    (0, "DS0BUNDLE-MIB", "dsx0BundleIndex"),
)
if mibBuilder.loadTexts:
    ds0BundleMemmbersEntry.setStatus("current")


class _Ds0BundleMemmbersList_Type(OctetString):
    """Custom type ds0BundleMemmbersList based on OctetString"""
    defaultHexValue = "00"


_Ds0BundleMemmbersList_Type.__name__ = "OctetString"
_Ds0BundleMemmbersList_Object = MibTableColumn
ds0BundleMemmbersList = _Ds0BundleMemmbersList_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 6, 1, 1, 2, 1, 1),
    _Ds0BundleMemmbersList_Type()
)
ds0BundleMemmbersList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ds0BundleMemmbersList.setStatus("current")


class _Ds0BundleSpeedFactor_Type(Integer32):
    """Custom type ds0BundleSpeedFactor based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("a64kbps", 1),
          ("a56kbps", 2))
    )


_Ds0BundleSpeedFactor_Type.__name__ = "Integer32"
_Ds0BundleSpeedFactor_Object = MibTableColumn
ds0BundleSpeedFactor = _Ds0BundleSpeedFactor_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 6, 1, 1, 2, 1, 2),
    _Ds0BundleSpeedFactor_Type()
)
ds0BundleSpeedFactor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ds0BundleSpeedFactor.setStatus("current")
_Ifs_ObjectIdentity = ObjectIdentity
ifs = _Ifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 6, 2)
)
_Ds1objs_ObjectIdentity = ObjectIdentity
ds1objs = _Ds1objs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 6, 2, 1)
)


class _Ds1DeviceMode_Type(Integer32):
    """Custom type ds1DeviceMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("e1", 1),
          ("t1", 2),
          ("j1", 3))
    )


_Ds1DeviceMode_Type.__name__ = "Integer32"
_Ds1DeviceMode_Object = MibScalar
ds1DeviceMode = _Ds1DeviceMode_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 6, 2, 1, 1),
    _Ds1DeviceMode_Type()
)
ds1DeviceMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ds1DeviceMode.setStatus("current")


class _Ds1CurrentDeviceMode_Type(Integer32):
    """Custom type ds1CurrentDeviceMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("e1", 1),
          ("t1", 2),
          ("j1", 3))
    )


_Ds1CurrentDeviceMode_Type.__name__ = "Integer32"
_Ds1CurrentDeviceMode_Object = MibScalar
ds1CurrentDeviceMode = _Ds1CurrentDeviceMode_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 6, 2, 1, 2),
    _Ds1CurrentDeviceMode_Type()
)
ds1CurrentDeviceMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ds1CurrentDeviceMode.setStatus("current")
_IfTablePrivateExtensions_ObjectIdentity = ObjectIdentity
ifTablePrivateExtensions = _IfTablePrivateExtensions_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 6, 2, 2)
)
_IfTableXtndTable_Object = MibTable
ifTableXtndTable = _IfTableXtndTable_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 6, 2, 2, 1)
)
if mibBuilder.loadTexts:
    ifTableXtndTable.setStatus("current")
_IfTableXtndEntry_Object = MibTableRow
ifTableXtndEntry = _IfTableXtndEntry_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 6, 2, 2, 1, 1)
)
ifTableXtndEntry.setIndexNames(
    (0, "WAN-MIB", "ifTableXtndIndex"),
)
if mibBuilder.loadTexts:
    ifTableXtndEntry.setStatus("current")
_IfTableXtndIndex_Type = InterfaceIndex
_IfTableXtndIndex_Object = MibTableColumn
ifTableXtndIndex = _IfTableXtndIndex_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 6, 2, 2, 1, 1, 1),
    _IfTableXtndIndex_Type()
)
ifTableXtndIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifTableXtndIndex.setStatus("current")
_IfTableXtndPeerAddress_Type = IpAddress
_IfTableXtndPeerAddress_Object = MibTableColumn
ifTableXtndPeerAddress = _IfTableXtndPeerAddress_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 6, 2, 2, 1, 1, 2),
    _IfTableXtndPeerAddress_Type()
)
ifTableXtndPeerAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifTableXtndPeerAddress.setStatus("current")


class _IfTableXtndVoIPQueue_Type(Integer32):
    """Custom type ifTableXtndVoIPQueue based on Integer32"""
    defaultValue = 255

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              255)
        )
    )
    namedValues = NamedValues(
        *(("on", 1),
          ("off", 2),
          ("fairQ", 3),
          ("notRelevant", 255))
    )


_IfTableXtndVoIPQueue_Type.__name__ = "Integer32"
_IfTableXtndVoIPQueue_Object = MibTableColumn
ifTableXtndVoIPQueue = _IfTableXtndVoIPQueue_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 6, 2, 2, 1, 1, 3),
    _IfTableXtndVoIPQueue_Type()
)
ifTableXtndVoIPQueue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifTableXtndVoIPQueue.setStatus("current")


class _IfTableXtndCableLength_Type(Integer32):
    """Custom type ifTableXtndCableLength based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              255)
        )
    )
    namedValues = NamedValues(
        *(("long15db", 1),
          ("long22dot5db", 2),
          ("long7dot5db", 3),
          ("long0db", 4),
          ("short133ft", 5),
          ("short266ft", 6),
          ("short399ft", 7),
          ("short533ft", 8),
          ("short655ft", 9),
          ("notSupported", 255))
    )


_IfTableXtndCableLength_Type.__name__ = "Integer32"
_IfTableXtndCableLength_Object = MibTableColumn
ifTableXtndCableLength = _IfTableXtndCableLength_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 6, 2, 2, 1, 1, 4),
    _IfTableXtndCableLength_Type()
)
ifTableXtndCableLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifTableXtndCableLength.setStatus("current")


class _IfTableXtndGain_Type(Integer32):
    """Custom type ifTableXtndGain based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("a26", 1),
          ("a36", 2),
          ("notSupported", 255))
    )


_IfTableXtndGain_Type.__name__ = "Integer32"
_IfTableXtndGain_Object = MibTableColumn
ifTableXtndGain = _IfTableXtndGain_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 6, 2, 2, 1, 1, 5),
    _IfTableXtndGain_Type()
)
ifTableXtndGain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifTableXtndGain.setStatus("current")


class _IfTableXtndDescription_Type(DisplayString):
    """Custom type ifTableXtndDescription based on DisplayString"""
    defaultHexValue = ""


_IfTableXtndDescription_Type.__name__ = "DisplayString"
_IfTableXtndDescription_Object = MibTableColumn
ifTableXtndDescription = _IfTableXtndDescription_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 6, 2, 2, 1, 1, 6),
    _IfTableXtndDescription_Type()
)
ifTableXtndDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifTableXtndDescription.setStatus("current")


class _IfTableXtndKeepAlive_Type(Integer32):
    """Custom type ifTableXtndKeepAlive based on Integer32"""
    defaultValue = 0


_IfTableXtndKeepAlive_Type.__name__ = "Integer32"
_IfTableXtndKeepAlive_Object = MibTableColumn
ifTableXtndKeepAlive = _IfTableXtndKeepAlive_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 6, 2, 2, 1, 1, 7),
    _IfTableXtndKeepAlive_Type()
)
ifTableXtndKeepAlive.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifTableXtndKeepAlive.setStatus("current")


class _IfTableXtndMtu_Type(Integer32):
    """Custom type ifTableXtndMtu based on Integer32"""
    defaultValue = 0


_IfTableXtndMtu_Type.__name__ = "Integer32"
_IfTableXtndMtu_Object = MibTableColumn
ifTableXtndMtu = _IfTableXtndMtu_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 6, 2, 2, 1, 1, 8),
    _IfTableXtndMtu_Type()
)
ifTableXtndMtu.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifTableXtndMtu.setStatus("current")


class _IfTableXtndInvertTxClock_Type(OnOff):
    """Custom type ifTableXtndInvertTxClock based on OnOff"""
    defaultValue = 255


_IfTableXtndInvertTxClock_Type.__name__ = "OnOff"
_IfTableXtndInvertTxClock_Object = MibTableColumn
ifTableXtndInvertTxClock = _IfTableXtndInvertTxClock_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 6, 2, 2, 1, 1, 9),
    _IfTableXtndInvertTxClock_Type()
)
ifTableXtndInvertTxClock.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifTableXtndInvertTxClock.setStatus("current")


class _IfTableXtndDTELoopback_Type(OnOff):
    """Custom type ifTableXtndDTELoopback based on OnOff"""
    defaultValue = 255


_IfTableXtndDTELoopback_Type.__name__ = "OnOff"
_IfTableXtndDTELoopback_Object = MibTableColumn
ifTableXtndDTELoopback = _IfTableXtndDTELoopback_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 6, 2, 2, 1, 1, 10),
    _IfTableXtndDTELoopback_Type()
)
ifTableXtndDTELoopback.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifTableXtndDTELoopback.setStatus("current")


class _IfTableXtndIgnoreDCD_Type(OnOff):
    """Custom type ifTableXtndIgnoreDCD based on OnOff"""
    defaultValue = 255


_IfTableXtndIgnoreDCD_Type.__name__ = "OnOff"
_IfTableXtndIgnoreDCD_Object = MibTableColumn
ifTableXtndIgnoreDCD = _IfTableXtndIgnoreDCD_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 6, 2, 2, 1, 1, 11),
    _IfTableXtndIgnoreDCD_Type()
)
ifTableXtndIgnoreDCD.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifTableXtndIgnoreDCD.setStatus("current")


class _IfTableXtndIdleChars_Type(Integer32):
    """Custom type ifTableXtndIdleChars based on Integer32"""
    defaultValue = 255

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              255)
        )
    )
    namedValues = NamedValues(
        *(("flag", 1),
          ("mark", 2),
          ("space", 3),
          ("notRelevant", 255))
    )


_IfTableXtndIdleChars_Type.__name__ = "Integer32"
_IfTableXtndIdleChars_Object = MibTableColumn
ifTableXtndIdleChars = _IfTableXtndIdleChars_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 6, 2, 2, 1, 1, 12),
    _IfTableXtndIdleChars_Type()
)
ifTableXtndIdleChars.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifTableXtndIdleChars.setStatus("current")


class _IfTableXtndBandwidth_Type(Integer32):
    """Custom type ifTableXtndBandwidth based on Integer32"""
    defaultValue = 0


_IfTableXtndBandwidth_Type.__name__ = "Integer32"
_IfTableXtndBandwidth_Object = MibTableColumn
ifTableXtndBandwidth = _IfTableXtndBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 6, 2, 2, 1, 1, 13),
    _IfTableXtndBandwidth_Type()
)
ifTableXtndBandwidth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifTableXtndBandwidth.setStatus("current")


class _IfTableXtndEncapsulation_Type(Integer32):
    """Custom type ifTableXtndEncapsulation based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              255)
        )
    )
    namedValues = NamedValues(
        *(("ppp", 1),
          ("frameRelay", 2),
          ("pppoe", 3),
          ("arpa", 4),
          ("frameRelayNonIetf", 5),
          ("notSupported", 255))
    )


_IfTableXtndEncapsulation_Type.__name__ = "Integer32"
_IfTableXtndEncapsulation_Object = MibTableColumn
ifTableXtndEncapsulation = _IfTableXtndEncapsulation_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 6, 2, 2, 1, 1, 14),
    _IfTableXtndEncapsulation_Type()
)
ifTableXtndEncapsulation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifTableXtndEncapsulation.setStatus("current")


class _IfTableXtndOperStatus_Type(Integer32):
    """Custom type ifTableXtndOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              255)
        )
    )
    namedValues = NamedValues(
        *(("up", 1),
          ("faultDown", 2),
          ("testing", 3),
          ("partiallyDownFault", 4),
          ("adminDown", 5),
          ("dormantDown", 6),
          ("xtndKeepAliveDown", 7),
          ("modemUndetected", 8),
          ("modemReady", 9),
          ("modemDialing", 10),
          ("modemConnectedDialin", 11),
          ("modemConnectedDialout", 12),
          ("notSupported", 255))
    )


_IfTableXtndOperStatus_Type.__name__ = "Integer32"
_IfTableXtndOperStatus_Object = MibTableColumn
ifTableXtndOperStatus = _IfTableXtndOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 6, 2, 2, 1, 1, 15),
    _IfTableXtndOperStatus_Type()
)
ifTableXtndOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifTableXtndOperStatus.setStatus("current")


class _IfTableXtndBackupCapabilities_Type(Integer32):
    """Custom type ifTableXtndBackupCapabilities based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              255)
        )
    )
    namedValues = NamedValues(
        *(("primaryAndBackUp", 1),
          ("primaryOnly", 2),
          ("backupOnly", 3),
          ("notSupported", 255))
    )


_IfTableXtndBackupCapabilities_Type.__name__ = "Integer32"
_IfTableXtndBackupCapabilities_Object = MibTableColumn
ifTableXtndBackupCapabilities = _IfTableXtndBackupCapabilities_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 6, 2, 2, 1, 1, 16),
    _IfTableXtndBackupCapabilities_Type()
)
ifTableXtndBackupCapabilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifTableXtndBackupCapabilities.setStatus("current")
_IfTableXtndBackupIf_Type = InterfaceIndex
_IfTableXtndBackupIf_Object = MibTableColumn
ifTableXtndBackupIf = _IfTableXtndBackupIf_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 6, 2, 2, 1, 1, 17),
    _IfTableXtndBackupIf_Type()
)
ifTableXtndBackupIf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifTableXtndBackupIf.setStatus("current")


class _IfTableXtndBackupEnableDelay_Type(Integer32):
    """Custom type ifTableXtndBackupEnableDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3600),
    )


_IfTableXtndBackupEnableDelay_Type.__name__ = "Integer32"
_IfTableXtndBackupEnableDelay_Object = MibTableColumn
ifTableXtndBackupEnableDelay = _IfTableXtndBackupEnableDelay_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 6, 2, 2, 1, 1, 18),
    _IfTableXtndBackupEnableDelay_Type()
)
ifTableXtndBackupEnableDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifTableXtndBackupEnableDelay.setStatus("current")


class _IfTableXtndBackupDisableDelay_Type(Integer32):
    """Custom type ifTableXtndBackupDisableDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 3600),
    )


_IfTableXtndBackupDisableDelay_Type.__name__ = "Integer32"
_IfTableXtndBackupDisableDelay_Object = MibTableColumn
ifTableXtndBackupDisableDelay = _IfTableXtndBackupDisableDelay_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 6, 2, 2, 1, 1, 19),
    _IfTableXtndBackupDisableDelay_Type()
)
ifTableXtndBackupDisableDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifTableXtndBackupDisableDelay.setStatus("current")
_IfTableXtndPrimaryIf_Type = InterfaceIndex
_IfTableXtndPrimaryIf_Object = MibTableColumn
ifTableXtndPrimaryIf = _IfTableXtndPrimaryIf_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 6, 2, 2, 1, 1, 20),
    _IfTableXtndPrimaryIf_Type()
)
ifTableXtndPrimaryIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifTableXtndPrimaryIf.setStatus("current")


class _IfTableXtndCarrierDelay_Type(Integer32):
    """Custom type ifTableXtndCarrierDelay based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 60),
    )


_IfTableXtndCarrierDelay_Type.__name__ = "Integer32"
_IfTableXtndCarrierDelay_Object = MibTableColumn
ifTableXtndCarrierDelay = _IfTableXtndCarrierDelay_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 6, 2, 2, 1, 1, 21),
    _IfTableXtndCarrierDelay_Type()
)
ifTableXtndCarrierDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifTableXtndCarrierDelay.setStatus("current")


class _IfTableXtndDtrRestartDelay_Type(Integer32):
    """Custom type ifTableXtndDtrRestartDelay based on Integer32"""
    defaultValue = 30

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 900),
    )


_IfTableXtndDtrRestartDelay_Type.__name__ = "Integer32"
_IfTableXtndDtrRestartDelay_Object = MibTableColumn
ifTableXtndDtrRestartDelay = _IfTableXtndDtrRestartDelay_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 6, 2, 2, 1, 1, 22),
    _IfTableXtndDtrRestartDelay_Type()
)
ifTableXtndDtrRestartDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifTableXtndDtrRestartDelay.setStatus("current")


class _IfTableXtndDtrPulseTime_Type(Integer32):
    """Custom type ifTableXtndDtrPulseTime based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 60),
    )


_IfTableXtndDtrPulseTime_Type.__name__ = "Integer32"
_IfTableXtndDtrPulseTime_Object = MibTableColumn
ifTableXtndDtrPulseTime = _IfTableXtndDtrPulseTime_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 6, 2, 2, 1, 1, 23),
    _IfTableXtndDtrPulseTime_Type()
)
ifTableXtndDtrPulseTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifTableXtndDtrPulseTime.setStatus("current")


class _IfTableXtndLoadInterval_Type(Integer32):
    """Custom type ifTableXtndLoadInterval based on Integer32"""
    defaultValue = 300

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(30, 600),
    )


_IfTableXtndLoadInterval_Type.__name__ = "Integer32"
_IfTableXtndLoadInterval_Object = MibTableColumn
ifTableXtndLoadInterval = _IfTableXtndLoadInterval_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 6, 2, 2, 1, 1, 24),
    _IfTableXtndLoadInterval_Type()
)
ifTableXtndLoadInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifTableXtndLoadInterval.setStatus("current")
_IfTableXtndInputRate_Type = Gauge32
_IfTableXtndInputRate_Object = MibTableColumn
ifTableXtndInputRate = _IfTableXtndInputRate_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 6, 2, 2, 1, 1, 25),
    _IfTableXtndInputRate_Type()
)
ifTableXtndInputRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifTableXtndInputRate.setStatus("current")
_IfTableXtndOutputRate_Type = Gauge32
_IfTableXtndOutputRate_Object = MibTableColumn
ifTableXtndOutputRate = _IfTableXtndOutputRate_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 6, 2, 2, 1, 1, 26),
    _IfTableXtndOutputRate_Type()
)
ifTableXtndOutputRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifTableXtndOutputRate.setStatus("current")
_IfTableXtndInputLoad_Type = Gauge32
_IfTableXtndInputLoad_Object = MibTableColumn
ifTableXtndInputLoad = _IfTableXtndInputLoad_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 6, 2, 2, 1, 1, 27),
    _IfTableXtndInputLoad_Type()
)
ifTableXtndInputLoad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifTableXtndInputLoad.setStatus("current")
_IfTableXtndOutputLoad_Type = Gauge32
_IfTableXtndOutputLoad_Object = MibTableColumn
ifTableXtndOutputLoad = _IfTableXtndOutputLoad_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 6, 2, 2, 1, 1, 28),
    _IfTableXtndOutputLoad_Type()
)
ifTableXtndOutputLoad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifTableXtndOutputLoad.setStatus("current")
_IfTableXtndReliability_Type = Gauge32
_IfTableXtndReliability_Object = MibTableColumn
ifTableXtndReliability = _IfTableXtndReliability_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 6, 2, 2, 1, 1, 29),
    _IfTableXtndReliability_Type()
)
ifTableXtndReliability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifTableXtndReliability.setStatus("current")


class _IfTableXtndTrafficShaperRate_Type(Integer32):
    """Custom type ifTableXtndTrafficShaperRate based on Integer32"""
    defaultValue = 0


_IfTableXtndTrafficShaperRate_Type.__name__ = "Integer32"
_IfTableXtndTrafficShaperRate_Object = MibTableColumn
ifTableXtndTrafficShaperRate = _IfTableXtndTrafficShaperRate_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 6, 2, 2, 1, 1, 30),
    _IfTableXtndTrafficShaperRate_Type()
)
ifTableXtndTrafficShaperRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifTableXtndTrafficShaperRate.setStatus("current")


class _IfTableXtndCacBBL_Type(Integer32):
    """Custom type ifTableXtndCacBBL based on Integer32"""
    defaultValue = -1


_IfTableXtndCacBBL_Type.__name__ = "Integer32"
_IfTableXtndCacBBL_Object = MibTableColumn
ifTableXtndCacBBL = _IfTableXtndCacBBL_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 6, 2, 2, 1, 1, 31),
    _IfTableXtndCacBBL_Type()
)
ifTableXtndCacBBL.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifTableXtndCacBBL.setStatus("current")


class _IfTableXtndCacPriority_Type(Integer32):
    """Custom type ifTableXtndCacPriority based on Integer32"""
    defaultValue = 5


_IfTableXtndCacPriority_Type.__name__ = "Integer32"
_IfTableXtndCacPriority_Object = MibTableColumn
ifTableXtndCacPriority = _IfTableXtndCacPriority_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 6, 2, 2, 1, 1, 32),
    _IfTableXtndCacPriority_Type()
)
ifTableXtndCacPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifTableXtndCacPriority.setStatus("current")


class _IfTableXtndCacifStatus_Type(Integer32):
    """Custom type ifTableXtndCacifStatus based on Integer32"""
    defaultValue = 255

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              255)
        )
    )
    namedValues = NamedValues(
        *(("notConfigured", 1),
          ("active", 2),
          ("notActive", 3),
          ("activeECMP", 4),
          ("notSupported", 255))
    )


_IfTableXtndCacifStatus_Type.__name__ = "Integer32"
_IfTableXtndCacifStatus_Object = MibTableColumn
ifTableXtndCacifStatus = _IfTableXtndCacifStatus_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 6, 2, 2, 1, 1, 33),
    _IfTableXtndCacifStatus_Type()
)
ifTableXtndCacifStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifTableXtndCacifStatus.setStatus("current")
_IfTableXtndCommonApplifStatus_Type = OctetString
_IfTableXtndCommonApplifStatus_Object = MibTableColumn
ifTableXtndCommonApplifStatus = _IfTableXtndCommonApplifStatus_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 6, 2, 2, 1, 1, 34),
    _IfTableXtndCommonApplifStatus_Type()
)
ifTableXtndCommonApplifStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifTableXtndCommonApplifStatus.setStatus("current")


class _IfTableXtndIpSecDfBit_Type(Integer32):
    """Custom type ifTableXtndIpSecDfBit based on Integer32"""
    defaultValue = 255

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("clear", 1),
          ("copy", 2),
          ("notSupported", 255))
    )


_IfTableXtndIpSecDfBit_Type.__name__ = "Integer32"
_IfTableXtndIpSecDfBit_Object = MibTableColumn
ifTableXtndIpSecDfBit = _IfTableXtndIpSecDfBit_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 6, 2, 2, 1, 1, 35),
    _IfTableXtndIpSecDfBit_Type()
)
ifTableXtndIpSecDfBit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifTableXtndIpSecDfBit.setStatus("current")
_IfTableXtndMinPmtu_Type = Integer32
_IfTableXtndMinPmtu_Object = MibTableColumn
ifTableXtndMinPmtu = _IfTableXtndMinPmtu_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 6, 2, 2, 1, 1, 36),
    _IfTableXtndMinPmtu_Type()
)
ifTableXtndMinPmtu.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifTableXtndMinPmtu.setStatus("current")
_IfTableXtndConfString_Type = DisplayString
_IfTableXtndConfString_Object = MibTableColumn
ifTableXtndConfString = _IfTableXtndConfString_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 6, 2, 2, 1, 1, 37),
    _IfTableXtndConfString_Type()
)
ifTableXtndConfString.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifTableXtndConfString.setStatus("current")


class _IfTableXtndPppIpcpDnsOptionRequest_Type(Integer32):
    """Custom type ifTableXtndPppIpcpDnsOptionRequest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2),
          ("notSupported", 255))
    )


_IfTableXtndPppIpcpDnsOptionRequest_Type.__name__ = "Integer32"
_IfTableXtndPppIpcpDnsOptionRequest_Object = MibTableColumn
ifTableXtndPppIpcpDnsOptionRequest = _IfTableXtndPppIpcpDnsOptionRequest_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 6, 2, 2, 1, 1, 38),
    _IfTableXtndPppIpcpDnsOptionRequest_Type()
)
ifTableXtndPppIpcpDnsOptionRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifTableXtndPppIpcpDnsOptionRequest.setStatus("current")


class _IfTableXtndKeepaliveTrackId_Type(Unsigned32):
    """Custom type ifTableXtndKeepaliveTrackId based on Unsigned32"""
    defaultValue = 4294967295


_IfTableXtndKeepaliveTrackId_Type.__name__ = "Unsigned32"
_IfTableXtndKeepaliveTrackId_Object = MibTableColumn
ifTableXtndKeepaliveTrackId = _IfTableXtndKeepaliveTrackId_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 6, 2, 2, 1, 1, 39),
    _IfTableXtndKeepaliveTrackId_Type()
)
ifTableXtndKeepaliveTrackId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifTableXtndKeepaliveTrackId.setStatus("current")


class _IfTableXtndFrTrafficShaping_Type(OnOff):
    """Custom type ifTableXtndFrTrafficShaping based on OnOff"""
    defaultValue = 2


_IfTableXtndFrTrafficShaping_Type.__name__ = "OnOff"
_IfTableXtndFrTrafficShaping_Object = MibTableColumn
ifTableXtndFrTrafficShaping = _IfTableXtndFrTrafficShaping_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 6, 2, 2, 1, 1, 40),
    _IfTableXtndFrTrafficShaping_Type()
)
ifTableXtndFrTrafficShaping.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifTableXtndFrTrafficShaping.setStatus("current")


class _IfTableXtndType_Type(Integer32):
    """Custom type ifTableXtndType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              255)
        )
    )
    namedValues = NamedValues(
        *(("nullModem", 1),
          ("usrSporsterModem", 2),
          ("multitechZbaModem", 3),
          ("multitechIsdnModem", 4),
          ("notSupported", 255))
    )


_IfTableXtndType_Type.__name__ = "Integer32"
_IfTableXtndType_Object = MibTableColumn
ifTableXtndType = _IfTableXtndType_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 6, 2, 2, 1, 1, 41),
    _IfTableXtndType_Type()
)
ifTableXtndType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifTableXtndType.setStatus("current")
_XtndKeepAliveTable_Object = MibTable
xtndKeepAliveTable = _XtndKeepAliveTable_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 6, 2, 2, 2)
)
if mibBuilder.loadTexts:
    xtndKeepAliveTable.setStatus("current")
_XtndKeepAliveEntry_Object = MibTableRow
xtndKeepAliveEntry = _XtndKeepAliveEntry_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 6, 2, 2, 2, 1)
)
xtndKeepAliveEntry.setIndexNames(
    (0, "WAN-MIB", "xtndKeepAliveifIndex"),
)
if mibBuilder.loadTexts:
    xtndKeepAliveEntry.setStatus("current")
_XtndKeepAliveifIndex_Type = InterfaceIndex
_XtndKeepAliveifIndex_Object = MibTableColumn
xtndKeepAliveifIndex = _XtndKeepAliveifIndex_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 6, 2, 2, 2, 1, 1),
    _XtndKeepAliveifIndex_Type()
)
xtndKeepAliveifIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xtndKeepAliveifIndex.setStatus("current")


class _XtndKeepAliveMethod_Type(Integer32):
    """Custom type xtndKeepAliveMethod based on Integer32"""
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
        *(("icmpPing", 1),
          ("tcpConnect", 2),
          ("httpGet", 3))
    )


_XtndKeepAliveMethod_Type.__name__ = "Integer32"
_XtndKeepAliveMethod_Object = MibTableColumn
xtndKeepAliveMethod = _XtndKeepAliveMethod_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 6, 2, 2, 2, 1, 2),
    _XtndKeepAliveMethod_Type()
)
xtndKeepAliveMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xtndKeepAliveMethod.setStatus("current")
_XtndKeepAliveTimeout_Type = Integer32
_XtndKeepAliveTimeout_Object = MibTableColumn
xtndKeepAliveTimeout = _XtndKeepAliveTimeout_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 6, 2, 2, 2, 1, 3),
    _XtndKeepAliveTimeout_Type()
)
xtndKeepAliveTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xtndKeepAliveTimeout.setStatus("current")
_XtndKeepAliveUpRetries_Type = Integer32
_XtndKeepAliveUpRetries_Object = MibTableColumn
xtndKeepAliveUpRetries = _XtndKeepAliveUpRetries_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 6, 2, 2, 2, 1, 4),
    _XtndKeepAliveUpRetries_Type()
)
xtndKeepAliveUpRetries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xtndKeepAliveUpRetries.setStatus("current")
_XtndKeepAliveDownRetries_Type = Integer32
_XtndKeepAliveDownRetries_Object = MibTableColumn
xtndKeepAliveDownRetries = _XtndKeepAliveDownRetries_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 6, 2, 2, 2, 1, 5),
    _XtndKeepAliveDownRetries_Type()
)
xtndKeepAliveDownRetries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xtndKeepAliveDownRetries.setStatus("current")
_XtndKeepAliveInterval_Type = Integer32
_XtndKeepAliveInterval_Object = MibTableColumn
xtndKeepAliveInterval = _XtndKeepAliveInterval_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 6, 2, 2, 2, 1, 6),
    _XtndKeepAliveInterval_Type()
)
xtndKeepAliveInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xtndKeepAliveInterval.setStatus("current")


class _XtndKeepAliveSrcIPAddr_Type(IpAddress):
    """Custom type xtndKeepAliveSrcIPAddr based on IpAddress"""
    defaultHexValue = "7f000001"


_XtndKeepAliveSrcIPAddr_Type.__name__ = "IpAddress"
_XtndKeepAliveSrcIPAddr_Object = MibTableColumn
xtndKeepAliveSrcIPAddr = _XtndKeepAliveSrcIPAddr_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 6, 2, 2, 2, 1, 7),
    _XtndKeepAliveSrcIPAddr_Type()
)
xtndKeepAliveSrcIPAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xtndKeepAliveSrcIPAddr.setStatus("current")


class _XtndKeepAliveIPAddr_Type(IpAddress):
    """Custom type xtndKeepAliveIPAddr based on IpAddress"""
    defaultHexValue = "00000000"


_XtndKeepAliveIPAddr_Type.__name__ = "IpAddress"
_XtndKeepAliveIPAddr_Object = MibTableColumn
xtndKeepAliveIPAddr = _XtndKeepAliveIPAddr_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 6, 2, 2, 2, 1, 8),
    _XtndKeepAliveIPAddr_Type()
)
xtndKeepAliveIPAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xtndKeepAliveIPAddr.setStatus("current")


class _XtndKeepAliveNextHopMAC_Type(PhysAddress):
    """Custom type xtndKeepAliveNextHopMAC based on PhysAddress"""
    defaultHexValue = "000000000000"


_XtndKeepAliveNextHopMAC_Type.__name__ = "PhysAddress"
_XtndKeepAliveNextHopMAC_Object = MibTableColumn
xtndKeepAliveNextHopMAC = _XtndKeepAliveNextHopMAC_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 6, 2, 2, 2, 1, 9),
    _XtndKeepAliveNextHopMAC_Type()
)
xtndKeepAliveNextHopMAC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xtndKeepAliveNextHopMAC.setStatus("current")


class _XtndKeepAliveStatus_Type(Integer32):
    """Custom type xtndKeepAliveStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("up", 1),
          ("down", 2),
          ("disable", 3))
    )


_XtndKeepAliveStatus_Type.__name__ = "Integer32"
_XtndKeepAliveStatus_Object = MibTableColumn
xtndKeepAliveStatus = _XtndKeepAliveStatus_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 6, 2, 2, 2, 1, 10),
    _XtndKeepAliveStatus_Type()
)
xtndKeepAliveStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xtndKeepAliveStatus.setStatus("current")


class _XtndKeepAliveMode_Type(Integer32):
    """Custom type xtndKeepAliveMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_XtndKeepAliveMode_Type.__name__ = "Integer32"
_XtndKeepAliveMode_Object = MibTableColumn
xtndKeepAliveMode = _XtndKeepAliveMode_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 6, 2, 2, 2, 1, 11),
    _XtndKeepAliveMode_Type()
)
xtndKeepAliveMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xtndKeepAliveMode.setStatus("current")
_FrameRelay_ObjectIdentity = ObjectIdentity
frameRelay = _FrameRelay_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 6, 2, 4)
)
_FrDlcmiXtndTable_Object = MibTable
frDlcmiXtndTable = _FrDlcmiXtndTable_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 6, 2, 4, 1)
)
if mibBuilder.loadTexts:
    frDlcmiXtndTable.setStatus("current")
_FrDlcmiXtndEntry_Object = MibTableRow
frDlcmiXtndEntry = _FrDlcmiXtndEntry_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 6, 2, 4, 1, 1)
)
frDlcmiXtndEntry.setIndexNames(
    (0, "WAN-MIB", "frDlcmiXtndIndex"),
)
if mibBuilder.loadTexts:
    frDlcmiXtndEntry.setStatus("current")
_FrDlcmiXtndIndex_Type = InterfaceIndex
_FrDlcmiXtndIndex_Object = MibTableColumn
frDlcmiXtndIndex = _FrDlcmiXtndIndex_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 6, 2, 4, 1, 1, 1),
    _FrDlcmiXtndIndex_Type()
)
frDlcmiXtndIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frDlcmiXtndIndex.setStatus("current")


class _FrDlcmiXtndLMIAutoSense_Type(OnOff):
    """Custom type frDlcmiXtndLMIAutoSense based on OnOff"""
    defaultValue = 1


_FrDlcmiXtndLMIAutoSense_Type.__name__ = "OnOff"
_FrDlcmiXtndLMIAutoSense_Object = MibTableColumn
frDlcmiXtndLMIAutoSense = _FrDlcmiXtndLMIAutoSense_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 6, 2, 4, 1, 1, 2),
    _FrDlcmiXtndLMIAutoSense_Type()
)
frDlcmiXtndLMIAutoSense.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frDlcmiXtndLMIAutoSense.setStatus("current")
_FrStaticCircuitTable_Object = MibTable
frStaticCircuitTable = _FrStaticCircuitTable_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 6, 2, 4, 2)
)
if mibBuilder.loadTexts:
    frStaticCircuitTable.setStatus("current")
_FrStaticCircuitEntry_Object = MibTableRow
frStaticCircuitEntry = _FrStaticCircuitEntry_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 6, 2, 4, 2, 1)
)
frStaticCircuitEntry.setIndexNames(
    (0, "WAN-MIB", "frStaticCircuitSubIfIndex"),
    (0, "WAN-MIB", "frStaticCircuitDLCI"),
    (0, "WAN-MIB", "frStaticCircuitDLCIrole"),
)
if mibBuilder.loadTexts:
    frStaticCircuitEntry.setStatus("current")
_FrStaticCircuitSubIfIndex_Type = InterfaceIndex
_FrStaticCircuitSubIfIndex_Object = MibTableColumn
frStaticCircuitSubIfIndex = _FrStaticCircuitSubIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 6, 2, 4, 2, 1, 1),
    _FrStaticCircuitSubIfIndex_Type()
)
frStaticCircuitSubIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frStaticCircuitSubIfIndex.setStatus("current")
_FrStaticCircuitDLCI_Type = DLCI
_FrStaticCircuitDLCI_Object = MibTableColumn
frStaticCircuitDLCI = _FrStaticCircuitDLCI_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 6, 2, 4, 2, 1, 2),
    _FrStaticCircuitDLCI_Type()
)
frStaticCircuitDLCI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frStaticCircuitDLCI.setStatus("current")


class _FrStaticCircuitDLCIrole_Type(Integer32):
    """Custom type frStaticCircuitDLCIrole based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              100)
        )
    )
    namedValues = NamedValues(
        *(("priority6to7", 1),
          ("priority4to5", 2),
          ("priority2to3", 3),
          ("priority0to1", 4),
          ("primary", 100))
    )


_FrStaticCircuitDLCIrole_Type.__name__ = "Integer32"
_FrStaticCircuitDLCIrole_Object = MibTableColumn
frStaticCircuitDLCIrole = _FrStaticCircuitDLCIrole_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 6, 2, 4, 2, 1, 3),
    _FrStaticCircuitDLCIrole_Type()
)
frStaticCircuitDLCIrole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frStaticCircuitDLCIrole.setStatus("current")
_FrStaticCircuitStatus_Type = RowStatus
_FrStaticCircuitStatus_Object = MibTableColumn
frStaticCircuitStatus = _FrStaticCircuitStatus_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 6, 2, 4, 2, 1, 4),
    _FrStaticCircuitStatus_Type()
)
frStaticCircuitStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frStaticCircuitStatus.setStatus("current")


class _FrStaticCircuitMapClass_Type(DisplayString):
    """Custom type frStaticCircuitMapClass based on DisplayString"""
    defaultValue = OctetString("default")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_FrStaticCircuitMapClass_Type.__name__ = "DisplayString"
_FrStaticCircuitMapClass_Object = MibTableColumn
frStaticCircuitMapClass = _FrStaticCircuitMapClass_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 6, 2, 4, 2, 1, 5),
    _FrStaticCircuitMapClass_Type()
)
frStaticCircuitMapClass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frStaticCircuitMapClass.setStatus("current")
_FrSubIfTable_Object = MibTable
frSubIfTable = _FrSubIfTable_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 6, 2, 4, 3)
)
if mibBuilder.loadTexts:
    frSubIfTable.setStatus("current")
_FrSubIfEntry_Object = MibTableRow
frSubIfEntry = _FrSubIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 6, 2, 4, 3, 1)
)
frSubIfEntry.setIndexNames(
    (0, "WAN-MIB", "frSubIfDlcmiIndex"),
    (0, "WAN-MIB", "frSubIfSubIndex"),
    (0, "WAN-MIB", "frSubIfType"),
)
if mibBuilder.loadTexts:
    frSubIfEntry.setStatus("current")
_FrSubIfDlcmiIndex_Type = InterfaceIndex
_FrSubIfDlcmiIndex_Object = MibTableColumn
frSubIfDlcmiIndex = _FrSubIfDlcmiIndex_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 6, 2, 4, 3, 1, 1),
    _FrSubIfDlcmiIndex_Type()
)
frSubIfDlcmiIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frSubIfDlcmiIndex.setStatus("current")
_FrSubIfSubIndex_Type = InterfaceIndex
_FrSubIfSubIndex_Object = MibTableColumn
frSubIfSubIndex = _FrSubIfSubIndex_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 6, 2, 4, 3, 1, 2),
    _FrSubIfSubIndex_Type()
)
frSubIfSubIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frSubIfSubIndex.setStatus("current")


class _FrSubIfType_Type(Integer32):
    """Custom type frSubIfType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("point2point", 1),
          ("point2multiPoint", 2))
    )


_FrSubIfType_Type.__name__ = "Integer32"
_FrSubIfType_Object = MibTableColumn
frSubIfType = _FrSubIfType_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 6, 2, 4, 3, 1, 3),
    _FrSubIfType_Type()
)
frSubIfType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frSubIfType.setStatus("current")
_FrSubIfStatus_Type = RowStatus
_FrSubIfStatus_Object = MibTableColumn
frSubIfStatus = _FrSubIfStatus_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 6, 2, 4, 3, 1, 4),
    _FrSubIfStatus_Type()
)
frSubIfStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    frSubIfStatus.setStatus("current")
_FrMapClassTable_Object = MibTable
frMapClassTable = _FrMapClassTable_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 6, 2, 4, 4)
)
if mibBuilder.loadTexts:
    frMapClassTable.setStatus("current")
_FrMapClassEntry_Object = MibTableRow
frMapClassEntry = _FrMapClassEntry_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 6, 2, 4, 4, 1)
)
frMapClassEntry.setIndexNames(
    (1, "WAN-MIB", "frMapClassName"),
)
if mibBuilder.loadTexts:
    frMapClassEntry.setStatus("current")


class _FrMapClassName_Type(DisplayString):
    """Custom type frMapClassName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_FrMapClassName_Type.__name__ = "DisplayString"
_FrMapClassName_Object = MibTableColumn
frMapClassName = _FrMapClassName_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 6, 2, 4, 4, 1, 1),
    _FrMapClassName_Type()
)
frMapClassName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    frMapClassName.setStatus("current")


class _FrMapClassBcOut_Type(Unsigned32):
    """Custom type frMapClassBcOut based on Unsigned32"""
    defaultValue = 7000


_FrMapClassBcOut_Type.__name__ = "Unsigned32"
_FrMapClassBcOut_Object = MibTableColumn
frMapClassBcOut = _FrMapClassBcOut_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 6, 2, 4, 4, 1, 2),
    _FrMapClassBcOut_Type()
)
frMapClassBcOut.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frMapClassBcOut.setStatus("current")
if mibBuilder.loadTexts:
    frMapClassBcOut.setUnits("Bits")


class _FrMapClassBeOut_Type(Unsigned32):
    """Custom type frMapClassBeOut based on Unsigned32"""
    defaultValue = 0


_FrMapClassBeOut_Type.__name__ = "Unsigned32"
_FrMapClassBeOut_Object = MibTableColumn
frMapClassBeOut = _FrMapClassBeOut_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 6, 2, 4, 4, 1, 3),
    _FrMapClassBeOut_Type()
)
frMapClassBeOut.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frMapClassBeOut.setStatus("current")
if mibBuilder.loadTexts:
    frMapClassBeOut.setUnits("Bits")


class _FrMapClassCirOut_Type(Unsigned32):
    """Custom type frMapClassCirOut based on Unsigned32"""
    defaultValue = 56000


_FrMapClassCirOut_Type.__name__ = "Unsigned32"
_FrMapClassCirOut_Object = MibTableColumn
frMapClassCirOut = _FrMapClassCirOut_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 6, 2, 4, 4, 1, 4),
    _FrMapClassCirOut_Type()
)
frMapClassCirOut.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frMapClassCirOut.setStatus("current")
if mibBuilder.loadTexts:
    frMapClassCirOut.setUnits("Bits per second")


class _FrMapClassFrf12Frag_Type(Integer32):
    """Custom type frMapClassFrf12Frag based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(16, 1600),
    )


_FrMapClassFrf12Frag_Type.__name__ = "Integer32"
_FrMapClassFrf12Frag_Object = MibTableColumn
frMapClassFrf12Frag = _FrMapClassFrf12Frag_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 6, 2, 4, 4, 1, 5),
    _FrMapClassFrf12Frag_Type()
)
frMapClassFrf12Frag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frMapClassFrf12Frag.setStatus("current")
if mibBuilder.loadTexts:
    frMapClassFrf12Frag.setUnits("Bytes")
_FrMapClassRowStatus_Type = RowStatus
_FrMapClassRowStatus_Object = MibTableColumn
frMapClassRowStatus = _FrMapClassRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 6, 2, 4, 4, 1, 6),
    _FrMapClassRowStatus_Type()
)
frMapClassRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frMapClassRowStatus.setStatus("current")
_WanDialer_ObjectIdentity = ObjectIdentity
wanDialer = _WanDialer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 6, 2, 5)
)
_WanDialerTable_Object = MibTable
wanDialerTable = _WanDialerTable_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 6, 2, 5, 1)
)
if mibBuilder.loadTexts:
    wanDialerTable.setStatus("current")
_WanDialerEntry_Object = MibTableRow
wanDialerEntry = _WanDialerEntry_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 6, 2, 5, 1, 1)
)
wanDialerEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    wanDialerEntry.setStatus("current")
_WanDialerModemIf_Type = Integer32
_WanDialerModemIf_Object = MibTableColumn
wanDialerModemIf = _WanDialerModemIf_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 6, 2, 5, 1, 1, 1),
    _WanDialerModemIf_Type()
)
wanDialerModemIf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wanDialerModemIf.setStatus("current")


class _WanDialerState_Type(Integer32):
    """Custom type wanDialerState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11)
        )
    )
    namedValues = NamedValues(
        *(("initModem", 1),
          ("idle", 2),
          ("waiting4Modem", 3),
          ("maxAttemptsDisabled", 4),
          ("preDialReset", 5),
          ("waitForConnect", 6),
          ("waitForDCD", 7),
          ("hangUp", 8),
          ("persistentDelay", 9),
          ("waitForIPCP", 10),
          ("connected", 11))
    )


_WanDialerState_Type.__name__ = "Integer32"
_WanDialerState_Object = MibTableColumn
wanDialerState = _WanDialerState_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 6, 2, 5, 1, 1, 2),
    _WanDialerState_Type()
)
wanDialerState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanDialerState.setStatus("current")
_WanDialerPersistentDelay_Type = Integer32
_WanDialerPersistentDelay_Object = MibTableColumn
wanDialerPersistentDelay = _WanDialerPersistentDelay_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 6, 2, 5, 1, 1, 3),
    _WanDialerPersistentDelay_Type()
)
wanDialerPersistentDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wanDialerPersistentDelay.setStatus("current")
_WanDialerPersistentMaxAttempts_Type = Integer32
_WanDialerPersistentMaxAttempts_Object = MibTableColumn
wanDialerPersistentMaxAttempts = _WanDialerPersistentMaxAttempts_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 6, 2, 5, 1, 1, 4),
    _WanDialerPersistentMaxAttempts_Type()
)
wanDialerPersistentMaxAttempts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wanDialerPersistentMaxAttempts.setStatus("current")
_WanDialerPersistentReenable_Type = Integer32
_WanDialerPersistentReenable_Object = MibTableColumn
wanDialerPersistentReenable = _WanDialerPersistentReenable_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 6, 2, 5, 1, 1, 5),
    _WanDialerPersistentReenable_Type()
)
wanDialerPersistentReenable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wanDialerPersistentReenable.setStatus("current")


class _WanDialerOrder_Type(Integer32):
    """Custom type wanDialerOrder based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("sequential", 1),
          ("roundRobin", 2),
          ("lastSuccessful", 3))
    )


_WanDialerOrder_Type.__name__ = "Integer32"
_WanDialerOrder_Object = MibTableColumn
wanDialerOrder = _WanDialerOrder_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 6, 2, 5, 1, 1, 6),
    _WanDialerOrder_Type()
)
wanDialerOrder.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wanDialerOrder.setStatus("current")
_WanDialerString1_Type = DisplayString
_WanDialerString1_Object = MibTableColumn
wanDialerString1 = _WanDialerString1_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 6, 2, 5, 1, 1, 7),
    _WanDialerString1_Type()
)
wanDialerString1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wanDialerString1.setStatus("current")
_WanDialerString2_Type = DisplayString
_WanDialerString2_Object = MibTableColumn
wanDialerString2 = _WanDialerString2_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 6, 2, 5, 1, 1, 8),
    _WanDialerString2_Type()
)
wanDialerString2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wanDialerString2.setStatus("current")
_WanDialerString3_Type = DisplayString
_WanDialerString3_Object = MibTableColumn
wanDialerString3 = _WanDialerString3_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 6, 2, 5, 1, 1, 9),
    _WanDialerString3_Type()
)
wanDialerString3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wanDialerString3.setStatus("current")
_WanDialerString4_Type = DisplayString
_WanDialerString4_Object = MibTableColumn
wanDialerString4 = _WanDialerString4_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 6, 2, 5, 1, 1, 10),
    _WanDialerString4_Type()
)
wanDialerString4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wanDialerString4.setStatus("current")
_WanDialerString5_Type = DisplayString
_WanDialerString5_Object = MibTableColumn
wanDialerString5 = _WanDialerString5_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 6, 2, 5, 1, 1, 11),
    _WanDialerString5_Type()
)
wanDialerString5.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wanDialerString5.setStatus("current")
_WanDialerLastDialed_Type = DisplayString
_WanDialerLastDialed_Object = MibTableColumn
wanDialerLastDialed = _WanDialerLastDialed_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 6, 2, 5, 1, 1, 12),
    _WanDialerLastDialed_Type()
)
wanDialerLastDialed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanDialerLastDialed.setStatus("current")


class _WanDialerWaitForIpcp_Type(Integer32):
    """Custom type wanDialerWaitForIpcp based on Integer32"""
    defaultValue = 45


_WanDialerWaitForIpcp_Type.__name__ = "Integer32"
_WanDialerWaitForIpcp_Object = MibTableColumn
wanDialerWaitForIpcp = _WanDialerWaitForIpcp_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 6, 2, 5, 1, 1, 13),
    _WanDialerWaitForIpcp_Type()
)
wanDialerWaitForIpcp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wanDialerWaitForIpcp.setStatus("current")


class _WanDialerPersistentInitial_Type(Integer32):
    """Custom type wanDialerPersistentInitial based on Integer32"""
    defaultValue = 10


_WanDialerPersistentInitial_Type.__name__ = "Integer32"
_WanDialerPersistentInitial_Object = MibTableColumn
wanDialerPersistentInitial = _WanDialerPersistentInitial_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 6, 2, 5, 1, 1, 14),
    _WanDialerPersistentInitial_Type()
)
wanDialerPersistentInitial.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wanDialerPersistentInitial.setStatus("current")
_AvayaEISWanTraps_ObjectIdentity = ObjectIdentity
avayaEISWanTraps = _AvayaEISWanTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 6, 4)
)
_AvayaEISWanGroups_ObjectIdentity = ObjectIdentity
avayaEISWanGroups = _AvayaEISWanGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 6, 5)
)
_AvayaEISWanCompliances_ObjectIdentity = ObjectIdentity
avayaEISWanCompliances = _AvayaEISWanCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 6, 7)
)

# Managed Objects groups

hostModuleGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 6, 5, 1)
)
hostModuleGroup.setObjects(
      *(("WAN-MIB", "intWanGroupID"),
        ("WAN-MIB", "intWanPortID"),
        ("WAN-MIB", "intWanPortSpeed"),
        ("WAN-MIB", "intWanPortMode"),
        ("WAN-MIB", "intWanPortAutoNegotiation"),
        ("WAN-MIB", "intWanPortVLANMode"),
        ("WAN-MIB", "intWanPortVLANBindingMode"),
        ("WAN-MIB", "intWanPortVlanList"))
)
if mibBuilder.loadTexts:
    hostModuleGroup.setStatus("current")

wanRouterBladeGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 6, 5, 2)
)
wanRouterBladeGroup.setObjects(
      *(("WAN-MIB", "ds0BundleSpeedFactor"),
        ("WAN-MIB", "ifTableXtndIndex"),
        ("WAN-MIB", "ifTableXtndPeerAddress"),
        ("WAN-MIB", "ifTableXtndVoIPQueue"),
        ("WAN-MIB", "ifTableXtndCableLength"),
        ("WAN-MIB", "ifTableXtndGain"),
        ("WAN-MIB", "ifTableXtndDescription"),
        ("WAN-MIB", "ifTableXtndKeepAlive"),
        ("WAN-MIB", "ifTableXtndMtu"),
        ("WAN-MIB", "ifTableXtndInvertTxClock"),
        ("WAN-MIB", "ifTableXtndDTELoopback"),
        ("WAN-MIB", "ifTableXtndIgnoreDCD"),
        ("WAN-MIB", "ifTableXtndIdleChars"),
        ("WAN-MIB", "ifTableXtndBandwidth"),
        ("WAN-MIB", "ifTableXtndEncapsulation"),
        ("WAN-MIB", "frDlcmiXtndLMIAutoSense"),
        ("WAN-MIB", "frDlcmiXtndIndex"),
        ("WAN-MIB", "frSubIfDlcmiIndex"),
        ("WAN-MIB", "frSubIfSubIndex"),
        ("WAN-MIB", "frSubIfType"),
        ("WAN-MIB", "frSubIfStatus"),
        ("WAN-MIB", "frStaticCircuitDLCIrole"),
        ("WAN-MIB", "ifTableXtndPrimaryIf"),
        ("WAN-MIB", "ifTableXtndBackupDisableDelay"),
        ("WAN-MIB", "ifTableXtndBackupEnableDelay"),
        ("WAN-MIB", "ifTableXtndBackupIf"),
        ("WAN-MIB", "ifTableXtndBackupCapabilities"),
        ("WAN-MIB", "ds1DeviceMode"),
        ("WAN-MIB", "ds0BundleMemmbersList"),
        ("WAN-MIB", "ifTableXtndOperStatus"),
        ("WAN-MIB", "frStaticCircuitSubIfIndex"),
        ("WAN-MIB", "frStaticCircuitDLCI"),
        ("WAN-MIB", "frStaticCircuitStatus"),
        ("WAN-MIB", "ifTableXtndReliability"),
        ("WAN-MIB", "ifTableXtndOutputLoad"),
        ("WAN-MIB", "ifTableXtndInputLoad"),
        ("WAN-MIB", "ifTableXtndOutputRate"),
        ("WAN-MIB", "ifTableXtndInputRate"),
        ("WAN-MIB", "ifTableXtndLoadInterval"),
        ("WAN-MIB", "ifTableXtndDtrPulseTime"),
        ("WAN-MIB", "frMapClassRowStatus"),
        ("WAN-MIB", "frMapClassFrf12Frag"),
        ("WAN-MIB", "frMapClassCirOut"),
        ("WAN-MIB", "frMapClassBeOut"),
        ("WAN-MIB", "frMapClassBcOut"),
        ("WAN-MIB", "ifTableXtndFrTrafficShaping"),
        ("WAN-MIB", "frStaticCircuitMapClass"),
        ("WAN-MIB", "ifTableXtndDtrRestartDelay"),
        ("WAN-MIB", "ifTableXtndCarrierDelay"))
)
if mibBuilder.loadTexts:
    wanRouterBladeGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

hostModuleCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 6, 7, 1)
)
hostModuleCompliance.setObjects(
    ("WAN-MIB", "hostModuleGroup")
)
if mibBuilder.loadTexts:
    hostModuleCompliance.setStatus(
        "current"
    )

wanRouterBladeCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 6, 7, 2)
)
wanRouterBladeCompliance.setObjects(
    ("WAN-MIB", "wanRouterBladeGroup")
)
if mibBuilder.loadTexts:
    wanRouterBladeCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "WAN-MIB",
    **{"OnOff": OnOff,
       "avayaEISWan": avayaEISWan,
       "deviceSpecific": deviceSpecific,
       "x330wanSpecific": x330wanSpecific,
       "intWanPortTable": intWanPortTable,
       "intWanPortEntry": intWanPortEntry,
       "intWanGroupID": intWanGroupID,
       "intWanPortID": intWanPortID,
       "intWanPortSpeed": intWanPortSpeed,
       "intWanPortMode": intWanPortMode,
       "intWanPortAutoNegotiation": intWanPortAutoNegotiation,
       "intWanPortVLANMode": intWanPortVLANMode,
       "intWanPortVLANBindingMode": intWanPortVLANBindingMode,
       "intWanPortVlanList": intWanPortVlanList,
       "ds0BundleMemmbersTable": ds0BundleMemmbersTable,
       "ds0BundleMemmbersEntry": ds0BundleMemmbersEntry,
       "ds0BundleMemmbersList": ds0BundleMemmbersList,
       "ds0BundleSpeedFactor": ds0BundleSpeedFactor,
       "ifs": ifs,
       "ds1objs": ds1objs,
       "ds1DeviceMode": ds1DeviceMode,
       "ds1CurrentDeviceMode": ds1CurrentDeviceMode,
       "ifTablePrivateExtensions": ifTablePrivateExtensions,
       "ifTableXtndTable": ifTableXtndTable,
       "ifTableXtndEntry": ifTableXtndEntry,
       "ifTableXtndIndex": ifTableXtndIndex,
       "ifTableXtndPeerAddress": ifTableXtndPeerAddress,
       "ifTableXtndVoIPQueue": ifTableXtndVoIPQueue,
       "ifTableXtndCableLength": ifTableXtndCableLength,
       "ifTableXtndGain": ifTableXtndGain,
       "ifTableXtndDescription": ifTableXtndDescription,
       "ifTableXtndKeepAlive": ifTableXtndKeepAlive,
       "ifTableXtndMtu": ifTableXtndMtu,
       "ifTableXtndInvertTxClock": ifTableXtndInvertTxClock,
       "ifTableXtndDTELoopback": ifTableXtndDTELoopback,
       "ifTableXtndIgnoreDCD": ifTableXtndIgnoreDCD,
       "ifTableXtndIdleChars": ifTableXtndIdleChars,
       "ifTableXtndBandwidth": ifTableXtndBandwidth,
       "ifTableXtndEncapsulation": ifTableXtndEncapsulation,
       "ifTableXtndOperStatus": ifTableXtndOperStatus,
       "ifTableXtndBackupCapabilities": ifTableXtndBackupCapabilities,
       "ifTableXtndBackupIf": ifTableXtndBackupIf,
       "ifTableXtndBackupEnableDelay": ifTableXtndBackupEnableDelay,
       "ifTableXtndBackupDisableDelay": ifTableXtndBackupDisableDelay,
       "ifTableXtndPrimaryIf": ifTableXtndPrimaryIf,
       "ifTableXtndCarrierDelay": ifTableXtndCarrierDelay,
       "ifTableXtndDtrRestartDelay": ifTableXtndDtrRestartDelay,
       "ifTableXtndDtrPulseTime": ifTableXtndDtrPulseTime,
       "ifTableXtndLoadInterval": ifTableXtndLoadInterval,
       "ifTableXtndInputRate": ifTableXtndInputRate,
       "ifTableXtndOutputRate": ifTableXtndOutputRate,
       "ifTableXtndInputLoad": ifTableXtndInputLoad,
       "ifTableXtndOutputLoad": ifTableXtndOutputLoad,
       "ifTableXtndReliability": ifTableXtndReliability,
       "ifTableXtndTrafficShaperRate": ifTableXtndTrafficShaperRate,
       "ifTableXtndCacBBL": ifTableXtndCacBBL,
       "ifTableXtndCacPriority": ifTableXtndCacPriority,
       "ifTableXtndCacifStatus": ifTableXtndCacifStatus,
       "ifTableXtndCommonApplifStatus": ifTableXtndCommonApplifStatus,
       "ifTableXtndIpSecDfBit": ifTableXtndIpSecDfBit,
       "ifTableXtndMinPmtu": ifTableXtndMinPmtu,
       "ifTableXtndConfString": ifTableXtndConfString,
       "ifTableXtndPppIpcpDnsOptionRequest": ifTableXtndPppIpcpDnsOptionRequest,
       "ifTableXtndKeepaliveTrackId": ifTableXtndKeepaliveTrackId,
       "ifTableXtndFrTrafficShaping": ifTableXtndFrTrafficShaping,
       "ifTableXtndType": ifTableXtndType,
       "xtndKeepAliveTable": xtndKeepAliveTable,
       "xtndKeepAliveEntry": xtndKeepAliveEntry,
       "xtndKeepAliveifIndex": xtndKeepAliveifIndex,
       "xtndKeepAliveMethod": xtndKeepAliveMethod,
       "xtndKeepAliveTimeout": xtndKeepAliveTimeout,
       "xtndKeepAliveUpRetries": xtndKeepAliveUpRetries,
       "xtndKeepAliveDownRetries": xtndKeepAliveDownRetries,
       "xtndKeepAliveInterval": xtndKeepAliveInterval,
       "xtndKeepAliveSrcIPAddr": xtndKeepAliveSrcIPAddr,
       "xtndKeepAliveIPAddr": xtndKeepAliveIPAddr,
       "xtndKeepAliveNextHopMAC": xtndKeepAliveNextHopMAC,
       "xtndKeepAliveStatus": xtndKeepAliveStatus,
       "xtndKeepAliveMode": xtndKeepAliveMode,
       "frameRelay": frameRelay,
       "frDlcmiXtndTable": frDlcmiXtndTable,
       "frDlcmiXtndEntry": frDlcmiXtndEntry,
       "frDlcmiXtndIndex": frDlcmiXtndIndex,
       "frDlcmiXtndLMIAutoSense": frDlcmiXtndLMIAutoSense,
       "frStaticCircuitTable": frStaticCircuitTable,
       "frStaticCircuitEntry": frStaticCircuitEntry,
       "frStaticCircuitSubIfIndex": frStaticCircuitSubIfIndex,
       "frStaticCircuitDLCI": frStaticCircuitDLCI,
       "frStaticCircuitDLCIrole": frStaticCircuitDLCIrole,
       "frStaticCircuitStatus": frStaticCircuitStatus,
       "frStaticCircuitMapClass": frStaticCircuitMapClass,
       "frSubIfTable": frSubIfTable,
       "frSubIfEntry": frSubIfEntry,
       "frSubIfDlcmiIndex": frSubIfDlcmiIndex,
       "frSubIfSubIndex": frSubIfSubIndex,
       "frSubIfType": frSubIfType,
       "frSubIfStatus": frSubIfStatus,
       "frMapClassTable": frMapClassTable,
       "frMapClassEntry": frMapClassEntry,
       "frMapClassName": frMapClassName,
       "frMapClassBcOut": frMapClassBcOut,
       "frMapClassBeOut": frMapClassBeOut,
       "frMapClassCirOut": frMapClassCirOut,
       "frMapClassFrf12Frag": frMapClassFrf12Frag,
       "frMapClassRowStatus": frMapClassRowStatus,
       "wanDialer": wanDialer,
       "wanDialerTable": wanDialerTable,
       "wanDialerEntry": wanDialerEntry,
       "wanDialerModemIf": wanDialerModemIf,
       "wanDialerState": wanDialerState,
       "wanDialerPersistentDelay": wanDialerPersistentDelay,
       "wanDialerPersistentMaxAttempts": wanDialerPersistentMaxAttempts,
       "wanDialerPersistentReenable": wanDialerPersistentReenable,
       "wanDialerOrder": wanDialerOrder,
       "wanDialerString1": wanDialerString1,
       "wanDialerString2": wanDialerString2,
       "wanDialerString3": wanDialerString3,
       "wanDialerString4": wanDialerString4,
       "wanDialerString5": wanDialerString5,
       "wanDialerLastDialed": wanDialerLastDialed,
       "wanDialerWaitForIpcp": wanDialerWaitForIpcp,
       "wanDialerPersistentInitial": wanDialerPersistentInitial,
       "avayaEISWanTraps": avayaEISWanTraps,
       "avayaEISWanGroups": avayaEISWanGroups,
       "hostModuleGroup": hostModuleGroup,
       "wanRouterBladeGroup": wanRouterBladeGroup,
       "avayaEISWanCompliances": avayaEISWanCompliances,
       "hostModuleCompliance": hostModuleCompliance,
       "wanRouterBladeCompliance": wanRouterBladeCompliance}
)
