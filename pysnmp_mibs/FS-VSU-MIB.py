# SNMP MIB module (FS-VSU-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/fscom/FS-VSU-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:15:30 2025
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

fsVsuMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 102)
)
if mibBuilder.loadTexts:
    fsVsuMIB.setRevisions(
        ("2011-06-21 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_FsVsuMIBObjects_ObjectIdentity = ObjectIdentity
fsVsuMIBObjects = _FsVsuMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 102, 1)
)
_FsVsuTopo_ObjectIdentity = ObjectIdentity
fsVsuTopo = _FsVsuTopo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 102, 1, 1)
)


class _FsVsuTopoShape_Type(Integer32):
    """Custom type fsVsuTopoShape based on Integer32"""
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


_FsVsuTopoShape_Type.__name__ = "Integer32"
_FsVsuTopoShape_Object = MibScalar
fsVsuTopoShape = _FsVsuTopoShape_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 102, 1, 1, 1),
    _FsVsuTopoShape_Type()
)
fsVsuTopoShape.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsVsuTopoShape.setStatus("current")
_FsVsuTopoConn_Type = DisplayString
_FsVsuTopoConn_Object = MibScalar
fsVsuTopoConn = _FsVsuTopoConn_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 102, 1, 1, 2),
    _FsVsuTopoConn_Type()
)
fsVsuTopoConn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsVsuTopoConn.setStatus("current")
_FsVsuDeviceInfo_ObjectIdentity = ObjectIdentity
fsVsuDeviceInfo = _FsVsuDeviceInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 102, 1, 2)
)
_FsVsuDomainID_Type = Integer32
_FsVsuDomainID_Object = MibScalar
fsVsuDomainID = _FsVsuDomainID_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 102, 1, 2, 1),
    _FsVsuDomainID_Type()
)
fsVsuDomainID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsVsuDomainID.setStatus("current")
_FsVsuDeviceTable_Object = MibTable
fsVsuDeviceTable = _FsVsuDeviceTable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 102, 1, 2, 2)
)
if mibBuilder.loadTexts:
    fsVsuDeviceTable.setStatus("current")
_FsVsuDeviceEntry_Object = MibTableRow
fsVsuDeviceEntry = _FsVsuDeviceEntry_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 102, 1, 2, 2, 1)
)
fsVsuDeviceEntry.setIndexNames(
    (0, "FS-VSU-MIB", "fsVsuDeviceID"),
)
if mibBuilder.loadTexts:
    fsVsuDeviceEntry.setStatus("current")
_FsVsuDeviceID_Type = Integer32
_FsVsuDeviceID_Object = MibTableColumn
fsVsuDeviceID = _FsVsuDeviceID_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 102, 1, 2, 2, 1, 1),
    _FsVsuDeviceID_Type()
)
fsVsuDeviceID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsVsuDeviceID.setStatus("current")
_FsVsuDeviceMac_Type = MacAddress
_FsVsuDeviceMac_Object = MibTableColumn
fsVsuDeviceMac = _FsVsuDeviceMac_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 102, 1, 2, 2, 1, 2),
    _FsVsuDeviceMac_Type()
)
fsVsuDeviceMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsVsuDeviceMac.setStatus("current")
_FsVsuDevicePri_Type = Integer32
_FsVsuDevicePri_Object = MibTableColumn
fsVsuDevicePri = _FsVsuDevicePri_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 102, 1, 2, 2, 1, 3),
    _FsVsuDevicePri_Type()
)
fsVsuDevicePri.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsVsuDevicePri.setStatus("current")
_FsVsuDeviceDescr_Type = DisplayString
_FsVsuDeviceDescr_Object = MibTableColumn
fsVsuDeviceDescr = _FsVsuDeviceDescr_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 102, 1, 2, 2, 1, 4),
    _FsVsuDeviceDescr_Type()
)
fsVsuDeviceDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsVsuDeviceDescr.setStatus("current")


class _FsVsuDeviceStatus_Type(Integer32):
    """Custom type fsVsuDeviceStatus based on Integer32"""
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


_FsVsuDeviceStatus_Type.__name__ = "Integer32"
_FsVsuDeviceStatus_Object = MibTableColumn
fsVsuDeviceStatus = _FsVsuDeviceStatus_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 102, 1, 2, 2, 1, 5),
    _FsVsuDeviceStatus_Type()
)
fsVsuDeviceStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsVsuDeviceStatus.setStatus("current")


class _FsVsuDeviceRole_Type(Integer32):
    """Custom type fsVsuDeviceRole based on Integer32"""
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


_FsVsuDeviceRole_Type.__name__ = "Integer32"
_FsVsuDeviceRole_Object = MibTableColumn
fsVsuDeviceRole = _FsVsuDeviceRole_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 102, 1, 2, 2, 1, 6),
    _FsVsuDeviceRole_Type()
)
fsVsuDeviceRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsVsuDeviceRole.setStatus("current")
_FsVsuVsl_ObjectIdentity = ObjectIdentity
fsVsuVsl = _FsVsuVsl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 102, 1, 3)
)
_FsVsuVslPortTable_Object = MibTable
fsVsuVslPortTable = _FsVsuVslPortTable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 102, 1, 3, 1)
)
if mibBuilder.loadTexts:
    fsVsuVslPortTable.setStatus("current")
_FsVsuVslPortEntry_Object = MibTableRow
fsVsuVslPortEntry = _FsVsuVslPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 102, 1, 3, 1, 1)
)
fsVsuVslPortEntry.setIndexNames(
    (0, "FS-VSU-MIB", "fsVsuVslPortIfIndex"),
)
if mibBuilder.loadTexts:
    fsVsuVslPortEntry.setStatus("current")
_FsVsuVslPortIfIndex_Type = Integer32
_FsVsuVslPortIfIndex_Object = MibTableColumn
fsVsuVslPortIfIndex = _FsVsuVslPortIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 102, 1, 3, 1, 1, 1),
    _FsVsuVslPortIfIndex_Type()
)
fsVsuVslPortIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsVsuVslPortIfIndex.setStatus("current")
_FsVsuVslApIf_Type = DisplayString
_FsVsuVslApIf_Object = MibTableColumn
fsVsuVslApIf = _FsVsuVslApIf_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 102, 1, 3, 1, 1, 2),
    _FsVsuVslApIf_Type()
)
fsVsuVslApIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsVsuVslApIf.setStatus("current")


class _FsVsuVslPortState_Type(Integer32):
    """Custom type fsVsuVslPortState based on Integer32"""
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


_FsVsuVslPortState_Type.__name__ = "Integer32"
_FsVsuVslPortState_Object = MibTableColumn
fsVsuVslPortState = _FsVsuVslPortState_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 102, 1, 3, 1, 1, 3),
    _FsVsuVslPortState_Type()
)
fsVsuVslPortState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsVsuVslPortState.setStatus("current")
_FsVsuVslPortPeerIfIndex_Type = Integer32
_FsVsuVslPortPeerIfIndex_Object = MibTableColumn
fsVsuVslPortPeerIfIndex = _FsVsuVslPortPeerIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 102, 1, 3, 1, 1, 4),
    _FsVsuVslPortPeerIfIndex_Type()
)
fsVsuVslPortPeerIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsVsuVslPortPeerIfIndex.setStatus("current")
_FsVsuVslTable_Object = MibTable
fsVsuVslTable = _FsVsuVslTable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 102, 1, 3, 2)
)
if mibBuilder.loadTexts:
    fsVsuVslTable.setStatus("current")
_FsVsuVslEntry_Object = MibTableRow
fsVsuVslEntry = _FsVsuVslEntry_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 102, 1, 3, 2, 1)
)
fsVsuVslEntry.setIndexNames(
    (0, "FS-VSU-MIB", "fsVsuVslApIndex"),
)
if mibBuilder.loadTexts:
    fsVsuVslEntry.setStatus("current")
_FsVsuVslApIndex_Type = Integer32
_FsVsuVslApIndex_Object = MibTableColumn
fsVsuVslApIndex = _FsVsuVslApIndex_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 102, 1, 3, 2, 1, 1),
    _FsVsuVslApIndex_Type()
)
fsVsuVslApIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsVsuVslApIndex.setStatus("current")
_FsVsuVslApUptime_Type = DisplayString
_FsVsuVslApUptime_Object = MibTableColumn
fsVsuVslApUptime = _FsVsuVslApUptime_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 102, 1, 3, 2, 1, 2),
    _FsVsuVslApUptime_Type()
)
fsVsuVslApUptime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsVsuVslApUptime.setStatus("current")
_FsVsuDad_ObjectIdentity = ObjectIdentity
fsVsuDad = _FsVsuDad_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 102, 1, 4)
)
_FsVsuDadExIntfTable_Object = MibTable
fsVsuDadExIntfTable = _FsVsuDadExIntfTable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 102, 1, 4, 1)
)
if mibBuilder.loadTexts:
    fsVsuDadExIntfTable.setStatus("current")
_FsVsuDadExIntfEntry_Object = MibTableRow
fsVsuDadExIntfEntry = _FsVsuDadExIntfEntry_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 102, 1, 4, 1, 1)
)
fsVsuDadExIntfEntry.setIndexNames(
    (0, "FS-VSU-MIB", "fsVsuDadExIfIndex"),
)
if mibBuilder.loadTexts:
    fsVsuDadExIntfEntry.setStatus("current")
_FsVsuDadExIfIndex_Type = Integer32
_FsVsuDadExIfIndex_Object = MibTableColumn
fsVsuDadExIfIndex = _FsVsuDadExIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 102, 1, 4, 1, 1, 1),
    _FsVsuDadExIfIndex_Type()
)
fsVsuDadExIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsVsuDadExIfIndex.setStatus("current")
_FsVsuDadAP_ObjectIdentity = ObjectIdentity
fsVsuDadAP = _FsVsuDadAP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 102, 1, 4, 2)
)


class _FsVsuDadAPEnable_Type(Integer32):
    """Custom type fsVsuDadAPEnable based on Integer32"""
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


_FsVsuDadAPEnable_Type.__name__ = "Integer32"
_FsVsuDadAPEnable_Object = MibScalar
fsVsuDadAPEnable = _FsVsuDadAPEnable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 102, 1, 4, 2, 1),
    _FsVsuDadAPEnable_Type()
)
fsVsuDadAPEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsVsuDadAPEnable.setStatus("current")
_FsVsuDadAPIfIndex_Type = Integer32
_FsVsuDadAPIfIndex_Object = MibScalar
fsVsuDadAPIfIndex = _FsVsuDadAPIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 102, 1, 4, 2, 2),
    _FsVsuDadAPIfIndex_Type()
)
fsVsuDadAPIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsVsuDadAPIfIndex.setStatus("current")


class _FsVsuDadAPIfStatus_Type(Integer32):
    """Custom type fsVsuDadAPIfStatus based on Integer32"""
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


_FsVsuDadAPIfStatus_Type.__name__ = "Integer32"
_FsVsuDadAPIfStatus_Object = MibScalar
fsVsuDadAPIfStatus = _FsVsuDadAPIfStatus_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 102, 1, 4, 2, 3),
    _FsVsuDadAPIfStatus_Type()
)
fsVsuDadAPIfStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsVsuDadAPIfStatus.setStatus("current")
_FsVsuDadAPMemberIfTable_Object = MibTable
fsVsuDadAPMemberIfTable = _FsVsuDadAPMemberIfTable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 102, 1, 4, 2, 4)
)
if mibBuilder.loadTexts:
    fsVsuDadAPMemberIfTable.setStatus("current")
_FsVsuDadAPMemberIfEntry_Object = MibTableRow
fsVsuDadAPMemberIfEntry = _FsVsuDadAPMemberIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 102, 1, 4, 2, 4, 1)
)
fsVsuDadAPMemberIfEntry.setIndexNames(
    (0, "FS-VSU-MIB", "fsVsuDadAPMemberIfindex"),
)
if mibBuilder.loadTexts:
    fsVsuDadAPMemberIfEntry.setStatus("current")
_FsVsuDadAPMemberIfindex_Type = Integer32
_FsVsuDadAPMemberIfindex_Object = MibTableColumn
fsVsuDadAPMemberIfindex = _FsVsuDadAPMemberIfindex_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 102, 1, 4, 2, 4, 1, 1),
    _FsVsuDadAPMemberIfindex_Type()
)
fsVsuDadAPMemberIfindex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsVsuDadAPMemberIfindex.setStatus("current")


class _FsVsuDadAPMemberIfStatus_Type(Integer32):
    """Custom type fsVsuDadAPMemberIfStatus based on Integer32"""
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


_FsVsuDadAPMemberIfStatus_Type.__name__ = "Integer32"
_FsVsuDadAPMemberIfStatus_Object = MibTableColumn
fsVsuDadAPMemberIfStatus = _FsVsuDadAPMemberIfStatus_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 102, 1, 4, 2, 4, 1, 2),
    _FsVsuDadAPMemberIfStatus_Type()
)
fsVsuDadAPMemberIfStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsVsuDadAPMemberIfStatus.setStatus("current")
_FsVsuDadAPRelayIfTable_Object = MibTable
fsVsuDadAPRelayIfTable = _FsVsuDadAPRelayIfTable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 102, 1, 4, 2, 5)
)
if mibBuilder.loadTexts:
    fsVsuDadAPRelayIfTable.setStatus("current")
_FsVsuDadAPRelayIfEntry_Object = MibTableRow
fsVsuDadAPRelayIfEntry = _FsVsuDadAPRelayIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 102, 1, 4, 2, 5, 1)
)
fsVsuDadAPRelayIfEntry.setIndexNames(
    (0, "FS-VSU-MIB", "fsVsuDadAPRelayIfIndex"),
)
if mibBuilder.loadTexts:
    fsVsuDadAPRelayIfEntry.setStatus("current")
_FsVsuDadAPRelayIfIndex_Type = Integer32
_FsVsuDadAPRelayIfIndex_Object = MibTableColumn
fsVsuDadAPRelayIfIndex = _FsVsuDadAPRelayIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 102, 1, 4, 2, 5, 1, 1),
    _FsVsuDadAPRelayIfIndex_Type()
)
fsVsuDadAPRelayIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsVsuDadAPRelayIfIndex.setStatus("current")
_FsVsuDadBFD_ObjectIdentity = ObjectIdentity
fsVsuDadBFD = _FsVsuDadBFD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 102, 1, 4, 3)
)


class _FsVsuDadBFDEnable_Type(Integer32):
    """Custom type fsVsuDadBFDEnable based on Integer32"""
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


_FsVsuDadBFDEnable_Type.__name__ = "Integer32"
_FsVsuDadBFDEnable_Object = MibScalar
fsVsuDadBFDEnable = _FsVsuDadBFDEnable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 102, 1, 4, 3, 1),
    _FsVsuDadBFDEnable_Type()
)
fsVsuDadBFDEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsVsuDadBFDEnable.setStatus("current")
_FsVsuDadBFDIfTable_Object = MibTable
fsVsuDadBFDIfTable = _FsVsuDadBFDIfTable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 102, 1, 4, 3, 2)
)
if mibBuilder.loadTexts:
    fsVsuDadBFDIfTable.setStatus("current")
_FsVsuDadBFDIfEntry_Object = MibTableRow
fsVsuDadBFDIfEntry = _FsVsuDadBFDIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 102, 1, 4, 3, 2, 1)
)
fsVsuDadBFDIfEntry.setIndexNames(
    (0, "FS-VSU-MIB", "fsVsuDadBFDIfIndex1"),
    (0, "FS-VSU-MIB", "fsVsuDadBFDIfIndex2"),
)
if mibBuilder.loadTexts:
    fsVsuDadBFDIfEntry.setStatus("current")
_FsVsuDadBFDIfIndex1_Type = Integer32
_FsVsuDadBFDIfIndex1_Object = MibTableColumn
fsVsuDadBFDIfIndex1 = _FsVsuDadBFDIfIndex1_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 102, 1, 4, 3, 2, 1, 1),
    _FsVsuDadBFDIfIndex1_Type()
)
fsVsuDadBFDIfIndex1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsVsuDadBFDIfIndex1.setStatus("current")
_FsVsuDadBFDIfIndex2_Type = Integer32
_FsVsuDadBFDIfIndex2_Object = MibTableColumn
fsVsuDadBFDIfIndex2 = _FsVsuDadBFDIfIndex2_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 102, 1, 4, 3, 2, 1, 2),
    _FsVsuDadBFDIfIndex2_Type()
)
fsVsuDadBFDIfIndex2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsVsuDadBFDIfIndex2.setStatus("current")


class _FsVsuDadBFDIfStatus_Type(Integer32):
    """Custom type fsVsuDadBFDIfStatus based on Integer32"""
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


_FsVsuDadBFDIfStatus_Type.__name__ = "Integer32"
_FsVsuDadBFDIfStatus_Object = MibTableColumn
fsVsuDadBFDIfStatus = _FsVsuDadBFDIfStatus_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 102, 1, 4, 3, 2, 1, 3),
    _FsVsuDadBFDIfStatus_Type()
)
fsVsuDadBFDIfStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsVsuDadBFDIfStatus.setStatus("current")
_FsVsuForward_ObjectIdentity = ObjectIdentity
fsVsuForward = _FsVsuForward_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 102, 1, 5)
)


class _FsVsuForwardApllf_Type(Integer32):
    """Custom type fsVsuForwardApllf based on Integer32"""
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


_FsVsuForwardApllf_Type.__name__ = "Integer32"
_FsVsuForwardApllf_Object = MibScalar
fsVsuForwardApllf = _FsVsuForwardApllf_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 102, 1, 5, 1),
    _FsVsuForwardApllf_Type()
)
fsVsuForwardApllf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsVsuForwardApllf.setStatus("current")


class _FsVsuForwardEcmpllf_Type(Integer32):
    """Custom type fsVsuForwardEcmpllf based on Integer32"""
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


_FsVsuForwardEcmpllf_Type.__name__ = "Integer32"
_FsVsuForwardEcmpllf_Object = MibScalar
fsVsuForwardEcmpllf = _FsVsuForwardEcmpllf_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 102, 1, 5, 2),
    _FsVsuForwardEcmpllf_Type()
)
fsVsuForwardEcmpllf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsVsuForwardEcmpllf.setStatus("current")
_FsVsuVersion_Type = DisplayString
_FsVsuVersion_Object = MibScalar
fsVsuVersion = _FsVsuVersion_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 102, 1, 6),
    _FsVsuVersion_Type()
)
fsVsuVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsVsuVersion.setStatus("current")
_FsVsuMIBTraps_ObjectIdentity = ObjectIdentity
fsVsuMIBTraps = _FsVsuMIBTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 102, 2)
)
_FsVsuTrapsNtfObjects_ObjectIdentity = ObjectIdentity
fsVsuTrapsNtfObjects = _FsVsuTrapsNtfObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 102, 2, 1)
)


class _FsVsuDeviceState_Type(Integer32):
    """Custom type fsVsuDeviceState based on Integer32"""
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


_FsVsuDeviceState_Type.__name__ = "Integer32"
_FsVsuDeviceState_Object = MibScalar
fsVsuDeviceState = _FsVsuDeviceState_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 102, 2, 1, 1),
    _FsVsuDeviceState_Type()
)
fsVsuDeviceState.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    fsVsuDeviceState.setStatus("current")
_FsVsuSlotID_Type = Integer32
_FsVsuSlotID_Object = MibScalar
fsVsuSlotID = _FsVsuSlotID_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 102, 2, 1, 2),
    _FsVsuSlotID_Type()
)
fsVsuSlotID.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    fsVsuSlotID.setStatus("current")


class _FsVsuDadResult_Type(Integer32):
    """Custom type fsVsuDadResult based on Integer32"""
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


_FsVsuDadResult_Type.__name__ = "Integer32"
_FsVsuDadResult_Object = MibScalar
fsVsuDadResult = _FsVsuDadResult_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 102, 2, 1, 3),
    _FsVsuDadResult_Type()
)
fsVsuDadResult.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    fsVsuDadResult.setStatus("current")
_FsVsuTrapsNotifications_ObjectIdentity = ObjectIdentity
fsVsuTrapsNotifications = _FsVsuTrapsNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 102, 2, 2)
)
_FsVsuMIBConformance_ObjectIdentity = ObjectIdentity
fsVsuMIBConformance = _FsVsuMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 102, 3)
)
_FsVsuMIBCompliances_ObjectIdentity = ObjectIdentity
fsVsuMIBCompliances = _FsVsuMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 102, 3, 1)
)
_FsVsuMIBGroups_ObjectIdentity = ObjectIdentity
fsVsuMIBGroups = _FsVsuMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 102, 3, 2)
)

# Managed Objects groups

fsVsuMIBObjectsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 102, 3, 2, 1)
)
fsVsuMIBObjectsGroup.setObjects(
      *(("FS-VSU-MIB", "fsVsuTopoShape"),
        ("FS-VSU-MIB", "fsVsuTopoConn"),
        ("FS-VSU-MIB", "fsVsuDomainID"),
        ("FS-VSU-MIB", "fsVsuDeviceID"),
        ("FS-VSU-MIB", "fsVsuDeviceMac"),
        ("FS-VSU-MIB", "fsVsuDevicePri"),
        ("FS-VSU-MIB", "fsVsuDeviceDescr"),
        ("FS-VSU-MIB", "fsVsuDeviceStatus"),
        ("FS-VSU-MIB", "fsVsuDeviceRole"),
        ("FS-VSU-MIB", "fsVsuVslPortIfIndex"),
        ("FS-VSU-MIB", "fsVsuVslApIf"),
        ("FS-VSU-MIB", "fsVsuVslPortState"),
        ("FS-VSU-MIB", "fsVsuVslPortPeerIfIndex"),
        ("FS-VSU-MIB", "fsVsuVslApUptime"),
        ("FS-VSU-MIB", "fsVsuDadExIfIndex"),
        ("FS-VSU-MIB", "fsVsuDadAPEnable"),
        ("FS-VSU-MIB", "fsVsuDadAPIfIndex"),
        ("FS-VSU-MIB", "fsVsuDadAPIfStatus"),
        ("FS-VSU-MIB", "fsVsuDadAPMemberIfindex"),
        ("FS-VSU-MIB", "fsVsuDadAPMemberIfStatus"),
        ("FS-VSU-MIB", "fsVsuDadAPRelayIfIndex"),
        ("FS-VSU-MIB", "fsVsuDadBFDEnable"),
        ("FS-VSU-MIB", "fsVsuDadBFDIfIndex1"),
        ("FS-VSU-MIB", "fsVsuDadBFDIfIndex2"),
        ("FS-VSU-MIB", "fsVsuDadBFDIfStatus"),
        ("FS-VSU-MIB", "fsVsuForwardApllf"),
        ("FS-VSU-MIB", "fsVsuForwardEcmpllf"),
        ("FS-VSU-MIB", "fsVsuVersion"),
        ("FS-VSU-MIB", "fsVsuDeviceState"),
        ("FS-VSU-MIB", "fsVsuSlotID"),
        ("FS-VSU-MIB", "fsVsuDadResult"))
)
if mibBuilder.loadTexts:
    fsVsuMIBObjectsGroup.setStatus("current")


# Notification objects

fsVsuNotifyTopoChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 102, 2, 2, 1)
)
fsVsuNotifyTopoChange.setObjects(
    ("FS-VSU-MIB", "fsVsuTopoShape")
)
if mibBuilder.loadTexts:
    fsVsuNotifyTopoChange.setStatus(
        "current"
    )

fsVsuNotifyDeviceChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 102, 2, 2, 2)
)
fsVsuNotifyDeviceChange.setObjects(
      *(("FS-VSU-MIB", "fsVsuDeviceID"),
        ("FS-VSU-MIB", "fsVsuDeviceState"))
)
if mibBuilder.loadTexts:
    fsVsuNotifyDeviceChange.setStatus(
        "current"
    )

fsVsuNotifyDeviceRoleChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 102, 2, 2, 3)
)
fsVsuNotifyDeviceRoleChange.setObjects(
      *(("FS-VSU-MIB", "fsVsuDeviceID"),
        ("FS-VSU-MIB", "fsVsuSlotID"),
        ("FS-VSU-MIB", "fsVsuDeviceRole"))
)
if mibBuilder.loadTexts:
    fsVsuNotifyDeviceRoleChange.setStatus(
        "current"
    )

fsVsuNotifyDad = NotificationType(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 102, 2, 2, 4)
)
fsVsuNotifyDad.setObjects(
    ("FS-VSU-MIB", "fsVsuDadResult")
)
if mibBuilder.loadTexts:
    fsVsuNotifyDad.setStatus(
        "current"
    )

fsVsuNotifyDeviceJoin = NotificationType(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 102, 2, 2, 5)
)
fsVsuNotifyDeviceJoin.setObjects(
    ("FS-VSU-MIB", "fsVsuDeviceID")
)
if mibBuilder.loadTexts:
    fsVsuNotifyDeviceJoin.setStatus(
        "current"
    )

fsVsuNotifyDeviceLeave = NotificationType(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 102, 2, 2, 6)
)
fsVsuNotifyDeviceLeave.setObjects(
    ("FS-VSU-MIB", "fsVsuDeviceID")
)
if mibBuilder.loadTexts:
    fsVsuNotifyDeviceLeave.setStatus(
        "current"
    )


# Notifications groups

fsVsuMIBTrapsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 102, 3, 2, 2)
)
fsVsuMIBTrapsGroup.setObjects(
      *(("FS-VSU-MIB", "fsVsuNotifyTopoChange"),
        ("FS-VSU-MIB", "fsVsuNotifyDeviceChange"),
        ("FS-VSU-MIB", "fsVsuNotifyDeviceRoleChange"),
        ("FS-VSU-MIB", "fsVsuNotifyDad"),
        ("FS-VSU-MIB", "fsVsuNotifyDeviceJoin"),
        ("FS-VSU-MIB", "fsVsuNotifyDeviceLeave"))
)
if mibBuilder.loadTexts:
    fsVsuMIBTrapsGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

fsVsuMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 102, 3, 1, 1)
)
fsVsuMIBCompliance.setObjects(
      *(("FS-VSU-MIB", "fsVsuMIBObjectsGroup"),
        ("FS-VSU-MIB", "fsVsuMIBTrapsGroup"))
)
if mibBuilder.loadTexts:
    fsVsuMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "FS-VSU-MIB",
    **{"fsVsuMIB": fsVsuMIB,
       "fsVsuMIBObjects": fsVsuMIBObjects,
       "fsVsuTopo": fsVsuTopo,
       "fsVsuTopoShape": fsVsuTopoShape,
       "fsVsuTopoConn": fsVsuTopoConn,
       "fsVsuDeviceInfo": fsVsuDeviceInfo,
       "fsVsuDomainID": fsVsuDomainID,
       "fsVsuDeviceTable": fsVsuDeviceTable,
       "fsVsuDeviceEntry": fsVsuDeviceEntry,
       "fsVsuDeviceID": fsVsuDeviceID,
       "fsVsuDeviceMac": fsVsuDeviceMac,
       "fsVsuDevicePri": fsVsuDevicePri,
       "fsVsuDeviceDescr": fsVsuDeviceDescr,
       "fsVsuDeviceStatus": fsVsuDeviceStatus,
       "fsVsuDeviceRole": fsVsuDeviceRole,
       "fsVsuVsl": fsVsuVsl,
       "fsVsuVslPortTable": fsVsuVslPortTable,
       "fsVsuVslPortEntry": fsVsuVslPortEntry,
       "fsVsuVslPortIfIndex": fsVsuVslPortIfIndex,
       "fsVsuVslApIf": fsVsuVslApIf,
       "fsVsuVslPortState": fsVsuVslPortState,
       "fsVsuVslPortPeerIfIndex": fsVsuVslPortPeerIfIndex,
       "fsVsuVslTable": fsVsuVslTable,
       "fsVsuVslEntry": fsVsuVslEntry,
       "fsVsuVslApIndex": fsVsuVslApIndex,
       "fsVsuVslApUptime": fsVsuVslApUptime,
       "fsVsuDad": fsVsuDad,
       "fsVsuDadExIntfTable": fsVsuDadExIntfTable,
       "fsVsuDadExIntfEntry": fsVsuDadExIntfEntry,
       "fsVsuDadExIfIndex": fsVsuDadExIfIndex,
       "fsVsuDadAP": fsVsuDadAP,
       "fsVsuDadAPEnable": fsVsuDadAPEnable,
       "fsVsuDadAPIfIndex": fsVsuDadAPIfIndex,
       "fsVsuDadAPIfStatus": fsVsuDadAPIfStatus,
       "fsVsuDadAPMemberIfTable": fsVsuDadAPMemberIfTable,
       "fsVsuDadAPMemberIfEntry": fsVsuDadAPMemberIfEntry,
       "fsVsuDadAPMemberIfindex": fsVsuDadAPMemberIfindex,
       "fsVsuDadAPMemberIfStatus": fsVsuDadAPMemberIfStatus,
       "fsVsuDadAPRelayIfTable": fsVsuDadAPRelayIfTable,
       "fsVsuDadAPRelayIfEntry": fsVsuDadAPRelayIfEntry,
       "fsVsuDadAPRelayIfIndex": fsVsuDadAPRelayIfIndex,
       "fsVsuDadBFD": fsVsuDadBFD,
       "fsVsuDadBFDEnable": fsVsuDadBFDEnable,
       "fsVsuDadBFDIfTable": fsVsuDadBFDIfTable,
       "fsVsuDadBFDIfEntry": fsVsuDadBFDIfEntry,
       "fsVsuDadBFDIfIndex1": fsVsuDadBFDIfIndex1,
       "fsVsuDadBFDIfIndex2": fsVsuDadBFDIfIndex2,
       "fsVsuDadBFDIfStatus": fsVsuDadBFDIfStatus,
       "fsVsuForward": fsVsuForward,
       "fsVsuForwardApllf": fsVsuForwardApllf,
       "fsVsuForwardEcmpllf": fsVsuForwardEcmpllf,
       "fsVsuVersion": fsVsuVersion,
       "fsVsuMIBTraps": fsVsuMIBTraps,
       "fsVsuTrapsNtfObjects": fsVsuTrapsNtfObjects,
       "fsVsuDeviceState": fsVsuDeviceState,
       "fsVsuSlotID": fsVsuSlotID,
       "fsVsuDadResult": fsVsuDadResult,
       "fsVsuTrapsNotifications": fsVsuTrapsNotifications,
       "fsVsuNotifyTopoChange": fsVsuNotifyTopoChange,
       "fsVsuNotifyDeviceChange": fsVsuNotifyDeviceChange,
       "fsVsuNotifyDeviceRoleChange": fsVsuNotifyDeviceRoleChange,
       "fsVsuNotifyDad": fsVsuNotifyDad,
       "fsVsuNotifyDeviceJoin": fsVsuNotifyDeviceJoin,
       "fsVsuNotifyDeviceLeave": fsVsuNotifyDeviceLeave,
       "fsVsuMIBConformance": fsVsuMIBConformance,
       "fsVsuMIBCompliances": fsVsuMIBCompliances,
       "fsVsuMIBCompliance": fsVsuMIBCompliance,
       "fsVsuMIBGroups": fsVsuMIBGroups,
       "fsVsuMIBObjectsGroup": fsVsuMIBObjectsGroup,
       "fsVsuMIBTrapsGroup": fsVsuMIBTrapsGroup}
)
