# SNMP MIB module (FS-EGHA-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/fscom/FS-EGHA-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:15:29 2025
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

(fsMgmt,) = mibBuilder.importSymbols(
    "FS-SMI",
    "fsMgmt")

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
 MacAddress,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

fsEghaMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 139)
)
if mibBuilder.loadTexts:
    fsEghaMIB.setRevisions(
        ("2015-06-01 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_FsEghaMIBObjects_ObjectIdentity = ObjectIdentity
fsEghaMIBObjects = _FsEghaMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 139, 1)
)
_FsEghaTopo_ObjectIdentity = ObjectIdentity
fsEghaTopo = _FsEghaTopo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 139, 1, 1)
)


class _FsEghaTopoShape_Type(Integer32):
    """Custom type fsEghaTopoShape based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("chain", 1),
          ("ring", 2))
    )


_FsEghaTopoShape_Type.__name__ = "Integer32"
_FsEghaTopoShape_Object = MibScalar
fsEghaTopoShape = _FsEghaTopoShape_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 139, 1, 1, 1),
    _FsEghaTopoShape_Type()
)
fsEghaTopoShape.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsEghaTopoShape.setStatus("current")
_FsEghaTopoConn_Type = DisplayString
_FsEghaTopoConn_Object = MibScalar
fsEghaTopoConn = _FsEghaTopoConn_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 139, 1, 1, 2),
    _FsEghaTopoConn_Type()
)
fsEghaTopoConn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsEghaTopoConn.setStatus("current")
_FsEghaDeviceInfo_ObjectIdentity = ObjectIdentity
fsEghaDeviceInfo = _FsEghaDeviceInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 139, 1, 2)
)
_FsEghaDomainID_Type = Integer32
_FsEghaDomainID_Object = MibScalar
fsEghaDomainID = _FsEghaDomainID_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 139, 1, 2, 1),
    _FsEghaDomainID_Type()
)
fsEghaDomainID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsEghaDomainID.setStatus("current")
_FsEghaDeviceTable_Object = MibTable
fsEghaDeviceTable = _FsEghaDeviceTable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 139, 1, 2, 2)
)
if mibBuilder.loadTexts:
    fsEghaDeviceTable.setStatus("current")
_FsEghaDeviceEntry_Object = MibTableRow
fsEghaDeviceEntry = _FsEghaDeviceEntry_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 139, 1, 2, 2, 1)
)
fsEghaDeviceEntry.setIndexNames(
    (0, "FS-EGHA-MIB", "fsEghaDeviceID"),
)
if mibBuilder.loadTexts:
    fsEghaDeviceEntry.setStatus("current")
_FsEghaDeviceID_Type = Integer32
_FsEghaDeviceID_Object = MibTableColumn
fsEghaDeviceID = _FsEghaDeviceID_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 139, 1, 2, 2, 1, 1),
    _FsEghaDeviceID_Type()
)
fsEghaDeviceID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsEghaDeviceID.setStatus("current")
_FsEghaDeviceMac_Type = MacAddress
_FsEghaDeviceMac_Object = MibTableColumn
fsEghaDeviceMac = _FsEghaDeviceMac_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 139, 1, 2, 2, 1, 2),
    _FsEghaDeviceMac_Type()
)
fsEghaDeviceMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsEghaDeviceMac.setStatus("current")
_FsEghaDevicePri_Type = Integer32
_FsEghaDevicePri_Object = MibTableColumn
fsEghaDevicePri = _FsEghaDevicePri_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 139, 1, 2, 2, 1, 3),
    _FsEghaDevicePri_Type()
)
fsEghaDevicePri.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsEghaDevicePri.setStatus("current")
_FsEghaDeviceDescr_Type = DisplayString
_FsEghaDeviceDescr_Object = MibTableColumn
fsEghaDeviceDescr = _FsEghaDeviceDescr_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 139, 1, 2, 2, 1, 4),
    _FsEghaDeviceDescr_Type()
)
fsEghaDeviceDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsEghaDeviceDescr.setStatus("current")


class _FsEghaDeviceStatus_Type(Integer32):
    """Custom type fsEghaDeviceStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ok", 1),
          ("recovery", 2))
    )


_FsEghaDeviceStatus_Type.__name__ = "Integer32"
_FsEghaDeviceStatus_Object = MibTableColumn
fsEghaDeviceStatus = _FsEghaDeviceStatus_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 139, 1, 2, 2, 1, 5),
    _FsEghaDeviceStatus_Type()
)
fsEghaDeviceStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsEghaDeviceStatus.setStatus("current")


class _FsEghaDeviceRole_Type(Integer32):
    """Custom type fsEghaDeviceRole based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("standby", 2),
          ("candidate", 3))
    )


_FsEghaDeviceRole_Type.__name__ = "Integer32"
_FsEghaDeviceRole_Object = MibTableColumn
fsEghaDeviceRole = _FsEghaDeviceRole_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 139, 1, 2, 2, 1, 6),
    _FsEghaDeviceRole_Type()
)
fsEghaDeviceRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsEghaDeviceRole.setStatus("current")
_FsEghaLink_ObjectIdentity = ObjectIdentity
fsEghaLink = _FsEghaLink_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 139, 1, 3)
)
_FsEghaPortTable_Object = MibTable
fsEghaPortTable = _FsEghaPortTable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 139, 1, 3, 1)
)
if mibBuilder.loadTexts:
    fsEghaPortTable.setStatus("current")
_FsEghaPortEntry_Object = MibTableRow
fsEghaPortEntry = _FsEghaPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 139, 1, 3, 1, 1)
)
fsEghaPortEntry.setIndexNames(
    (0, "FS-EGHA-MIB", "fsEghaPortIfIndex"),
)
if mibBuilder.loadTexts:
    fsEghaPortEntry.setStatus("current")
_FsEghaPortIfIndex_Type = Integer32
_FsEghaPortIfIndex_Object = MibTableColumn
fsEghaPortIfIndex = _FsEghaPortIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 139, 1, 3, 1, 1, 1),
    _FsEghaPortIfIndex_Type()
)
fsEghaPortIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsEghaPortIfIndex.setStatus("current")
_FsEghaApIf_Type = DisplayString
_FsEghaApIf_Object = MibTableColumn
fsEghaApIf = _FsEghaApIf_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 139, 1, 3, 1, 1, 2),
    _FsEghaApIf_Type()
)
fsEghaApIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsEghaApIf.setStatus("current")


class _FsEghaPortState_Type(Integer32):
    """Custom type fsEghaPortState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("down", 1),
          ("up", 2),
          ("ok", 3),
          ("disable", 4),
          ("aged", 5))
    )


_FsEghaPortState_Type.__name__ = "Integer32"
_FsEghaPortState_Object = MibTableColumn
fsEghaPortState = _FsEghaPortState_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 139, 1, 3, 1, 1, 3),
    _FsEghaPortState_Type()
)
fsEghaPortState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsEghaPortState.setStatus("current")
_FsEghaPortPeerIfIndex_Type = Integer32
_FsEghaPortPeerIfIndex_Object = MibTableColumn
fsEghaPortPeerIfIndex = _FsEghaPortPeerIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 139, 1, 3, 1, 1, 4),
    _FsEghaPortPeerIfIndex_Type()
)
fsEghaPortPeerIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsEghaPortPeerIfIndex.setStatus("current")
_FsEghaApTable_Object = MibTable
fsEghaApTable = _FsEghaApTable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 139, 1, 3, 2)
)
if mibBuilder.loadTexts:
    fsEghaApTable.setStatus("current")
_FsEghaApEntry_Object = MibTableRow
fsEghaApEntry = _FsEghaApEntry_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 139, 1, 3, 2, 1)
)
fsEghaApEntry.setIndexNames(
    (0, "FS-EGHA-MIB", "fsEghaApIndex"),
)
if mibBuilder.loadTexts:
    fsEghaApEntry.setStatus("current")
_FsEghaApIndex_Type = Integer32
_FsEghaApIndex_Object = MibTableColumn
fsEghaApIndex = _FsEghaApIndex_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 139, 1, 3, 2, 1, 1),
    _FsEghaApIndex_Type()
)
fsEghaApIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsEghaApIndex.setStatus("current")
_FsEghaApUptime_Type = DisplayString
_FsEghaApUptime_Object = MibTableColumn
fsEghaApUptime = _FsEghaApUptime_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 139, 1, 3, 2, 1, 2),
    _FsEghaApUptime_Type()
)
fsEghaApUptime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsEghaApUptime.setStatus("current")
_FsEghaDad_ObjectIdentity = ObjectIdentity
fsEghaDad = _FsEghaDad_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 139, 1, 4)
)
_FsEghaDadExIntfTable_Object = MibTable
fsEghaDadExIntfTable = _FsEghaDadExIntfTable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 139, 1, 4, 1)
)
if mibBuilder.loadTexts:
    fsEghaDadExIntfTable.setStatus("current")
_FsEghaDadExIntfEntry_Object = MibTableRow
fsEghaDadExIntfEntry = _FsEghaDadExIntfEntry_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 139, 1, 4, 1, 1)
)
fsEghaDadExIntfEntry.setIndexNames(
    (0, "FS-EGHA-MIB", "fsEghaDadExIfIndex"),
)
if mibBuilder.loadTexts:
    fsEghaDadExIntfEntry.setStatus("current")
_FsEghaDadExIfIndex_Type = Integer32
_FsEghaDadExIfIndex_Object = MibTableColumn
fsEghaDadExIfIndex = _FsEghaDadExIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 139, 1, 4, 1, 1, 1),
    _FsEghaDadExIfIndex_Type()
)
fsEghaDadExIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsEghaDadExIfIndex.setStatus("current")
_FsEghaDadAP_ObjectIdentity = ObjectIdentity
fsEghaDadAP = _FsEghaDadAP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 139, 1, 4, 2)
)


class _FsEghaDadAPEnable_Type(Integer32):
    """Custom type fsEghaDadAPEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("yes", 1),
          ("no", 2))
    )


_FsEghaDadAPEnable_Type.__name__ = "Integer32"
_FsEghaDadAPEnable_Object = MibScalar
fsEghaDadAPEnable = _FsEghaDadAPEnable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 139, 1, 4, 2, 1),
    _FsEghaDadAPEnable_Type()
)
fsEghaDadAPEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsEghaDadAPEnable.setStatus("current")
_FsEghaDadAPIfIndex_Type = Integer32
_FsEghaDadAPIfIndex_Object = MibScalar
fsEghaDadAPIfIndex = _FsEghaDadAPIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 139, 1, 4, 2, 2),
    _FsEghaDadAPIfIndex_Type()
)
fsEghaDadAPIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsEghaDadAPIfIndex.setStatus("current")


class _FsEghaDadAPIfStatus_Type(Integer32):
    """Custom type fsEghaDadAPIfStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 1),
          ("up", 2))
    )


_FsEghaDadAPIfStatus_Type.__name__ = "Integer32"
_FsEghaDadAPIfStatus_Object = MibScalar
fsEghaDadAPIfStatus = _FsEghaDadAPIfStatus_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 139, 1, 4, 2, 3),
    _FsEghaDadAPIfStatus_Type()
)
fsEghaDadAPIfStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsEghaDadAPIfStatus.setStatus("current")
_FsEghaDadAPMemberIfTable_Object = MibTable
fsEghaDadAPMemberIfTable = _FsEghaDadAPMemberIfTable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 139, 1, 4, 2, 4)
)
if mibBuilder.loadTexts:
    fsEghaDadAPMemberIfTable.setStatus("current")
_FsEghaDadAPMemberIfEntry_Object = MibTableRow
fsEghaDadAPMemberIfEntry = _FsEghaDadAPMemberIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 139, 1, 4, 2, 4, 1)
)
fsEghaDadAPMemberIfEntry.setIndexNames(
    (0, "FS-EGHA-MIB", "fsEghaDadAPMemberIfindex"),
)
if mibBuilder.loadTexts:
    fsEghaDadAPMemberIfEntry.setStatus("current")
_FsEghaDadAPMemberIfindex_Type = Integer32
_FsEghaDadAPMemberIfindex_Object = MibTableColumn
fsEghaDadAPMemberIfindex = _FsEghaDadAPMemberIfindex_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 139, 1, 4, 2, 4, 1, 1),
    _FsEghaDadAPMemberIfindex_Type()
)
fsEghaDadAPMemberIfindex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsEghaDadAPMemberIfindex.setStatus("current")


class _FsEghaDadAPMemberIfStatus_Type(Integer32):
    """Custom type fsEghaDadAPMemberIfStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 1),
          ("up", 2))
    )


_FsEghaDadAPMemberIfStatus_Type.__name__ = "Integer32"
_FsEghaDadAPMemberIfStatus_Object = MibTableColumn
fsEghaDadAPMemberIfStatus = _FsEghaDadAPMemberIfStatus_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 139, 1, 4, 2, 4, 1, 2),
    _FsEghaDadAPMemberIfStatus_Type()
)
fsEghaDadAPMemberIfStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsEghaDadAPMemberIfStatus.setStatus("current")
_FsEghaDadAPRelayIfTable_Object = MibTable
fsEghaDadAPRelayIfTable = _FsEghaDadAPRelayIfTable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 139, 1, 4, 2, 5)
)
if mibBuilder.loadTexts:
    fsEghaDadAPRelayIfTable.setStatus("current")
_FsEghaDadAPRelayIfEntry_Object = MibTableRow
fsEghaDadAPRelayIfEntry = _FsEghaDadAPRelayIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 139, 1, 4, 2, 5, 1)
)
fsEghaDadAPRelayIfEntry.setIndexNames(
    (0, "FS-EGHA-MIB", "fsEghaDadAPRelayIfIndex"),
)
if mibBuilder.loadTexts:
    fsEghaDadAPRelayIfEntry.setStatus("current")
_FsEghaDadAPRelayIfIndex_Type = Integer32
_FsEghaDadAPRelayIfIndex_Object = MibTableColumn
fsEghaDadAPRelayIfIndex = _FsEghaDadAPRelayIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 139, 1, 4, 2, 5, 1, 1),
    _FsEghaDadAPRelayIfIndex_Type()
)
fsEghaDadAPRelayIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsEghaDadAPRelayIfIndex.setStatus("current")
_FsEghaDadBFD_ObjectIdentity = ObjectIdentity
fsEghaDadBFD = _FsEghaDadBFD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 139, 1, 4, 3)
)


class _FsEghaDadBFDEnable_Type(Integer32):
    """Custom type fsEghaDadBFDEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("yes", 1),
          ("no", 2))
    )


_FsEghaDadBFDEnable_Type.__name__ = "Integer32"
_FsEghaDadBFDEnable_Object = MibScalar
fsEghaDadBFDEnable = _FsEghaDadBFDEnable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 139, 1, 4, 3, 1),
    _FsEghaDadBFDEnable_Type()
)
fsEghaDadBFDEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsEghaDadBFDEnable.setStatus("current")
_FsEghaDadBFDIfTable_Object = MibTable
fsEghaDadBFDIfTable = _FsEghaDadBFDIfTable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 139, 1, 4, 3, 2)
)
if mibBuilder.loadTexts:
    fsEghaDadBFDIfTable.setStatus("current")
_FsEghaDadBFDIfEntry_Object = MibTableRow
fsEghaDadBFDIfEntry = _FsEghaDadBFDIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 139, 1, 4, 3, 2, 1)
)
fsEghaDadBFDIfEntry.setIndexNames(
    (0, "FS-EGHA-MIB", "fsEghaDadBFDIfIndex1"),
    (0, "FS-EGHA-MIB", "fsEghaDadBFDIfIndex2"),
)
if mibBuilder.loadTexts:
    fsEghaDadBFDIfEntry.setStatus("current")
_FsEghaDadBFDIfIndex1_Type = Integer32
_FsEghaDadBFDIfIndex1_Object = MibTableColumn
fsEghaDadBFDIfIndex1 = _FsEghaDadBFDIfIndex1_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 139, 1, 4, 3, 2, 1, 1),
    _FsEghaDadBFDIfIndex1_Type()
)
fsEghaDadBFDIfIndex1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsEghaDadBFDIfIndex1.setStatus("current")
_FsEghaDadBFDIfIndex2_Type = Integer32
_FsEghaDadBFDIfIndex2_Object = MibTableColumn
fsEghaDadBFDIfIndex2 = _FsEghaDadBFDIfIndex2_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 139, 1, 4, 3, 2, 1, 2),
    _FsEghaDadBFDIfIndex2_Type()
)
fsEghaDadBFDIfIndex2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsEghaDadBFDIfIndex2.setStatus("current")


class _FsEghaDadBFDIfStatus_Type(Integer32):
    """Custom type fsEghaDadBFDIfStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 1),
          ("up", 2))
    )


_FsEghaDadBFDIfStatus_Type.__name__ = "Integer32"
_FsEghaDadBFDIfStatus_Object = MibTableColumn
fsEghaDadBFDIfStatus = _FsEghaDadBFDIfStatus_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 139, 1, 4, 3, 2, 1, 3),
    _FsEghaDadBFDIfStatus_Type()
)
fsEghaDadBFDIfStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsEghaDadBFDIfStatus.setStatus("current")
_FsEghaForward_ObjectIdentity = ObjectIdentity
fsEghaForward = _FsEghaForward_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 139, 1, 5)
)


class _FsEghaForwardApllf_Type(Integer32):
    """Custom type fsEghaForwardApllf based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("on", 1),
          ("off", 2))
    )


_FsEghaForwardApllf_Type.__name__ = "Integer32"
_FsEghaForwardApllf_Object = MibScalar
fsEghaForwardApllf = _FsEghaForwardApllf_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 139, 1, 5, 1),
    _FsEghaForwardApllf_Type()
)
fsEghaForwardApllf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsEghaForwardApllf.setStatus("current")


class _FsEghaForwardEcmpllf_Type(Integer32):
    """Custom type fsEghaForwardEcmpllf based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("on", 1),
          ("off", 2))
    )


_FsEghaForwardEcmpllf_Type.__name__ = "Integer32"
_FsEghaForwardEcmpllf_Object = MibScalar
fsEghaForwardEcmpllf = _FsEghaForwardEcmpllf_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 139, 1, 5, 2),
    _FsEghaForwardEcmpllf_Type()
)
fsEghaForwardEcmpllf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsEghaForwardEcmpllf.setStatus("current")
_FsEghaVersion_Type = DisplayString
_FsEghaVersion_Object = MibScalar
fsEghaVersion = _FsEghaVersion_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 139, 1, 6),
    _FsEghaVersion_Type()
)
fsEghaVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsEghaVersion.setStatus("current")
_FsEghaMIBTraps_ObjectIdentity = ObjectIdentity
fsEghaMIBTraps = _FsEghaMIBTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 139, 2)
)
_FsEghaTrapsNtfObjects_ObjectIdentity = ObjectIdentity
fsEghaTrapsNtfObjects = _FsEghaTrapsNtfObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 139, 2, 1)
)


class _FsEghaDeviceState_Type(Integer32):
    """Custom type fsEghaDeviceState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("plugin", 1),
          ("remove", 2))
    )


_FsEghaDeviceState_Type.__name__ = "Integer32"
_FsEghaDeviceState_Object = MibScalar
fsEghaDeviceState = _FsEghaDeviceState_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 139, 2, 1, 1),
    _FsEghaDeviceState_Type()
)
fsEghaDeviceState.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    fsEghaDeviceState.setStatus("current")
_FsEghaSlotID_Type = Integer32
_FsEghaSlotID_Object = MibScalar
fsEghaSlotID = _FsEghaSlotID_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 139, 2, 1, 2),
    _FsEghaSlotID_Type()
)
fsEghaSlotID.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    fsEghaSlotID.setStatus("current")


class _FsEghaDadResult_Type(Integer32):
    """Custom type fsEghaDadResult based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("good", 1),
          ("bad", 2))
    )


_FsEghaDadResult_Type.__name__ = "Integer32"
_FsEghaDadResult_Object = MibScalar
fsEghaDadResult = _FsEghaDadResult_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 139, 2, 1, 3),
    _FsEghaDadResult_Type()
)
fsEghaDadResult.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    fsEghaDadResult.setStatus("current")
_FsEghaTrapsNotifications_ObjectIdentity = ObjectIdentity
fsEghaTrapsNotifications = _FsEghaTrapsNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 139, 2, 2)
)
_FsEghaMIBConformance_ObjectIdentity = ObjectIdentity
fsEghaMIBConformance = _FsEghaMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 139, 3)
)
_FsEghaMIBCompliances_ObjectIdentity = ObjectIdentity
fsEghaMIBCompliances = _FsEghaMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 139, 3, 1)
)
_FsEghaMIBGroups_ObjectIdentity = ObjectIdentity
fsEghaMIBGroups = _FsEghaMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 139, 3, 2)
)

# Managed Objects groups

fsEghaMIBObjectsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 139, 3, 2, 1)
)
fsEghaMIBObjectsGroup.setObjects(
      *(("FS-EGHA-MIB", "fsEghaTopoShape"),
        ("FS-EGHA-MIB", "fsEghaTopoConn"),
        ("FS-EGHA-MIB", "fsEghaDomainID"),
        ("FS-EGHA-MIB", "fsEghaDeviceID"),
        ("FS-EGHA-MIB", "fsEghaDeviceMac"),
        ("FS-EGHA-MIB", "fsEghaDevicePri"),
        ("FS-EGHA-MIB", "fsEghaDeviceDescr"),
        ("FS-EGHA-MIB", "fsEghaDeviceStatus"),
        ("FS-EGHA-MIB", "fsEghaDeviceRole"),
        ("FS-EGHA-MIB", "fsEghaPortIfIndex"),
        ("FS-EGHA-MIB", "fsEghaApIf"),
        ("FS-EGHA-MIB", "fsEghaPortState"),
        ("FS-EGHA-MIB", "fsEghaPortPeerIfIndex"),
        ("FS-EGHA-MIB", "fsEghaApUptime"),
        ("FS-EGHA-MIB", "fsEghaDadExIfIndex"),
        ("FS-EGHA-MIB", "fsEghaDadAPEnable"),
        ("FS-EGHA-MIB", "fsEghaDadAPIfIndex"),
        ("FS-EGHA-MIB", "fsEghaDadAPIfStatus"),
        ("FS-EGHA-MIB", "fsEghaDadAPMemberIfindex"),
        ("FS-EGHA-MIB", "fsEghaDadAPMemberIfStatus"),
        ("FS-EGHA-MIB", "fsEghaDadAPRelayIfIndex"),
        ("FS-EGHA-MIB", "fsEghaDadBFDEnable"),
        ("FS-EGHA-MIB", "fsEghaDadBFDIfIndex1"),
        ("FS-EGHA-MIB", "fsEghaDadBFDIfIndex2"),
        ("FS-EGHA-MIB", "fsEghaDadBFDIfStatus"),
        ("FS-EGHA-MIB", "fsEghaForwardApllf"),
        ("FS-EGHA-MIB", "fsEghaForwardEcmpllf"),
        ("FS-EGHA-MIB", "fsEghaVersion"),
        ("FS-EGHA-MIB", "fsEghaDeviceState"),
        ("FS-EGHA-MIB", "fsEghaSlotID"),
        ("FS-EGHA-MIB", "fsEghaDadResult"))
)
if mibBuilder.loadTexts:
    fsEghaMIBObjectsGroup.setStatus("current")


# Notification objects

fsEghaNotifyTopoChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 139, 2, 2, 1)
)
fsEghaNotifyTopoChange.setObjects(
    ("FS-EGHA-MIB", "fsEghaTopoShape")
)
if mibBuilder.loadTexts:
    fsEghaNotifyTopoChange.setStatus(
        "current"
    )

fsEghaNotifyDeviceChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 139, 2, 2, 2)
)
fsEghaNotifyDeviceChange.setObjects(
      *(("FS-EGHA-MIB", "fsEghaDeviceID"),
        ("FS-EGHA-MIB", "fsEghaDeviceState"))
)
if mibBuilder.loadTexts:
    fsEghaNotifyDeviceChange.setStatus(
        "current"
    )

fsEghaNotifyDeviceRoleChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 139, 2, 2, 3)
)
fsEghaNotifyDeviceRoleChange.setObjects(
      *(("FS-EGHA-MIB", "fsEghaDeviceID"),
        ("FS-EGHA-MIB", "fsEghaSlotID"),
        ("FS-EGHA-MIB", "fsEghaDeviceRole"))
)
if mibBuilder.loadTexts:
    fsEghaNotifyDeviceRoleChange.setStatus(
        "current"
    )

fsEghaNotifyDad = NotificationType(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 139, 2, 2, 4)
)
fsEghaNotifyDad.setObjects(
    ("FS-EGHA-MIB", "fsEghaDadResult")
)
if mibBuilder.loadTexts:
    fsEghaNotifyDad.setStatus(
        "current"
    )


# Notifications groups

fsEghaMIBTrapsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 139, 3, 2, 2)
)
fsEghaMIBTrapsGroup.setObjects(
      *(("FS-EGHA-MIB", "fsEghaNotifyTopoChange"),
        ("FS-EGHA-MIB", "fsEghaNotifyDeviceChange"),
        ("FS-EGHA-MIB", "fsEghaNotifyDeviceRoleChange"),
        ("FS-EGHA-MIB", "fsEghaNotifyDad"))
)
if mibBuilder.loadTexts:
    fsEghaMIBTrapsGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

fsEghaMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 139, 3, 1, 1)
)
fsEghaMIBCompliance.setObjects(
      *(("FS-EGHA-MIB", "fsEghaMIBObjectsGroup"),
        ("FS-EGHA-MIB", "fsEghaMIBTrapsGroup"))
)
if mibBuilder.loadTexts:
    fsEghaMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "FS-EGHA-MIB",
    **{"fsEghaMIB": fsEghaMIB,
       "fsEghaMIBObjects": fsEghaMIBObjects,
       "fsEghaTopo": fsEghaTopo,
       "fsEghaTopoShape": fsEghaTopoShape,
       "fsEghaTopoConn": fsEghaTopoConn,
       "fsEghaDeviceInfo": fsEghaDeviceInfo,
       "fsEghaDomainID": fsEghaDomainID,
       "fsEghaDeviceTable": fsEghaDeviceTable,
       "fsEghaDeviceEntry": fsEghaDeviceEntry,
       "fsEghaDeviceID": fsEghaDeviceID,
       "fsEghaDeviceMac": fsEghaDeviceMac,
       "fsEghaDevicePri": fsEghaDevicePri,
       "fsEghaDeviceDescr": fsEghaDeviceDescr,
       "fsEghaDeviceStatus": fsEghaDeviceStatus,
       "fsEghaDeviceRole": fsEghaDeviceRole,
       "fsEghaLink": fsEghaLink,
       "fsEghaPortTable": fsEghaPortTable,
       "fsEghaPortEntry": fsEghaPortEntry,
       "fsEghaPortIfIndex": fsEghaPortIfIndex,
       "fsEghaApIf": fsEghaApIf,
       "fsEghaPortState": fsEghaPortState,
       "fsEghaPortPeerIfIndex": fsEghaPortPeerIfIndex,
       "fsEghaApTable": fsEghaApTable,
       "fsEghaApEntry": fsEghaApEntry,
       "fsEghaApIndex": fsEghaApIndex,
       "fsEghaApUptime": fsEghaApUptime,
       "fsEghaDad": fsEghaDad,
       "fsEghaDadExIntfTable": fsEghaDadExIntfTable,
       "fsEghaDadExIntfEntry": fsEghaDadExIntfEntry,
       "fsEghaDadExIfIndex": fsEghaDadExIfIndex,
       "fsEghaDadAP": fsEghaDadAP,
       "fsEghaDadAPEnable": fsEghaDadAPEnable,
       "fsEghaDadAPIfIndex": fsEghaDadAPIfIndex,
       "fsEghaDadAPIfStatus": fsEghaDadAPIfStatus,
       "fsEghaDadAPMemberIfTable": fsEghaDadAPMemberIfTable,
       "fsEghaDadAPMemberIfEntry": fsEghaDadAPMemberIfEntry,
       "fsEghaDadAPMemberIfindex": fsEghaDadAPMemberIfindex,
       "fsEghaDadAPMemberIfStatus": fsEghaDadAPMemberIfStatus,
       "fsEghaDadAPRelayIfTable": fsEghaDadAPRelayIfTable,
       "fsEghaDadAPRelayIfEntry": fsEghaDadAPRelayIfEntry,
       "fsEghaDadAPRelayIfIndex": fsEghaDadAPRelayIfIndex,
       "fsEghaDadBFD": fsEghaDadBFD,
       "fsEghaDadBFDEnable": fsEghaDadBFDEnable,
       "fsEghaDadBFDIfTable": fsEghaDadBFDIfTable,
       "fsEghaDadBFDIfEntry": fsEghaDadBFDIfEntry,
       "fsEghaDadBFDIfIndex1": fsEghaDadBFDIfIndex1,
       "fsEghaDadBFDIfIndex2": fsEghaDadBFDIfIndex2,
       "fsEghaDadBFDIfStatus": fsEghaDadBFDIfStatus,
       "fsEghaForward": fsEghaForward,
       "fsEghaForwardApllf": fsEghaForwardApllf,
       "fsEghaForwardEcmpllf": fsEghaForwardEcmpllf,
       "fsEghaVersion": fsEghaVersion,
       "fsEghaMIBTraps": fsEghaMIBTraps,
       "fsEghaTrapsNtfObjects": fsEghaTrapsNtfObjects,
       "fsEghaDeviceState": fsEghaDeviceState,
       "fsEghaSlotID": fsEghaSlotID,
       "fsEghaDadResult": fsEghaDadResult,
       "fsEghaTrapsNotifications": fsEghaTrapsNotifications,
       "fsEghaNotifyTopoChange": fsEghaNotifyTopoChange,
       "fsEghaNotifyDeviceChange": fsEghaNotifyDeviceChange,
       "fsEghaNotifyDeviceRoleChange": fsEghaNotifyDeviceRoleChange,
       "fsEghaNotifyDad": fsEghaNotifyDad,
       "fsEghaMIBConformance": fsEghaMIBConformance,
       "fsEghaMIBCompliances": fsEghaMIBCompliances,
       "fsEghaMIBCompliance": fsEghaMIBCompliance,
       "fsEghaMIBGroups": fsEghaMIBGroups,
       "fsEghaMIBObjectsGroup": fsEghaMIBObjectsGroup,
       "fsEghaMIBTrapsGroup": fsEghaMIBTrapsGroup}
)
