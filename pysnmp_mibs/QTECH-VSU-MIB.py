# SNMP MIB module (QTECH-VSU-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/qtech/QTECH-VSU-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:57:49 2025
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

(qtechMgmt,) = mibBuilder.importSymbols(
    "QTECH-SMI",
    "qtechMgmt")

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

qtechVsuMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 102)
)
if mibBuilder.loadTexts:
    qtechVsuMIB.setRevisions(
        ("2011-06-21 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_QtechVsuMIBObjects_ObjectIdentity = ObjectIdentity
qtechVsuMIBObjects = _QtechVsuMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 102, 1)
)
_QtechVsuTopo_ObjectIdentity = ObjectIdentity
qtechVsuTopo = _QtechVsuTopo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 102, 1, 1)
)


class _QtechVsuTopoShape_Type(Integer32):
    """Custom type qtechVsuTopoShape based on Integer32"""
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


_QtechVsuTopoShape_Type.__name__ = "Integer32"
_QtechVsuTopoShape_Object = MibScalar
qtechVsuTopoShape = _QtechVsuTopoShape_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 102, 1, 1, 1),
    _QtechVsuTopoShape_Type()
)
qtechVsuTopoShape.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechVsuTopoShape.setStatus("current")
_QtechVsuTopoConn_Type = DisplayString
_QtechVsuTopoConn_Object = MibScalar
qtechVsuTopoConn = _QtechVsuTopoConn_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 102, 1, 1, 2),
    _QtechVsuTopoConn_Type()
)
qtechVsuTopoConn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechVsuTopoConn.setStatus("current")
_QtechVsuDeviceInfo_ObjectIdentity = ObjectIdentity
qtechVsuDeviceInfo = _QtechVsuDeviceInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 102, 1, 2)
)
_QtechVsuDomainID_Type = Integer32
_QtechVsuDomainID_Object = MibScalar
qtechVsuDomainID = _QtechVsuDomainID_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 102, 1, 2, 1),
    _QtechVsuDomainID_Type()
)
qtechVsuDomainID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechVsuDomainID.setStatus("current")
_QtechVsuDeviceTable_Object = MibTable
qtechVsuDeviceTable = _QtechVsuDeviceTable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 102, 1, 2, 2)
)
if mibBuilder.loadTexts:
    qtechVsuDeviceTable.setStatus("current")
_QtechVsuDeviceEntry_Object = MibTableRow
qtechVsuDeviceEntry = _QtechVsuDeviceEntry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 102, 1, 2, 2, 1)
)
qtechVsuDeviceEntry.setIndexNames(
    (0, "QTECH-VSU-MIB", "qtechVsuDeviceID"),
)
if mibBuilder.loadTexts:
    qtechVsuDeviceEntry.setStatus("current")
_QtechVsuDeviceID_Type = Integer32
_QtechVsuDeviceID_Object = MibTableColumn
qtechVsuDeviceID = _QtechVsuDeviceID_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 102, 1, 2, 2, 1, 1),
    _QtechVsuDeviceID_Type()
)
qtechVsuDeviceID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechVsuDeviceID.setStatus("current")
_QtechVsuDeviceMac_Type = MacAddress
_QtechVsuDeviceMac_Object = MibTableColumn
qtechVsuDeviceMac = _QtechVsuDeviceMac_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 102, 1, 2, 2, 1, 2),
    _QtechVsuDeviceMac_Type()
)
qtechVsuDeviceMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechVsuDeviceMac.setStatus("current")
_QtechVsuDevicePri_Type = Integer32
_QtechVsuDevicePri_Object = MibTableColumn
qtechVsuDevicePri = _QtechVsuDevicePri_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 102, 1, 2, 2, 1, 3),
    _QtechVsuDevicePri_Type()
)
qtechVsuDevicePri.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechVsuDevicePri.setStatus("current")
_QtechVsuDeviceDescr_Type = DisplayString
_QtechVsuDeviceDescr_Object = MibTableColumn
qtechVsuDeviceDescr = _QtechVsuDeviceDescr_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 102, 1, 2, 2, 1, 4),
    _QtechVsuDeviceDescr_Type()
)
qtechVsuDeviceDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechVsuDeviceDescr.setStatus("current")


class _QtechVsuDeviceStatus_Type(Integer32):
    """Custom type qtechVsuDeviceStatus based on Integer32"""
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


_QtechVsuDeviceStatus_Type.__name__ = "Integer32"
_QtechVsuDeviceStatus_Object = MibTableColumn
qtechVsuDeviceStatus = _QtechVsuDeviceStatus_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 102, 1, 2, 2, 1, 5),
    _QtechVsuDeviceStatus_Type()
)
qtechVsuDeviceStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechVsuDeviceStatus.setStatus("current")


class _QtechVsuDeviceRole_Type(Integer32):
    """Custom type qtechVsuDeviceRole based on Integer32"""
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


_QtechVsuDeviceRole_Type.__name__ = "Integer32"
_QtechVsuDeviceRole_Object = MibTableColumn
qtechVsuDeviceRole = _QtechVsuDeviceRole_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 102, 1, 2, 2, 1, 6),
    _QtechVsuDeviceRole_Type()
)
qtechVsuDeviceRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechVsuDeviceRole.setStatus("current")
_QtechVsuVsl_ObjectIdentity = ObjectIdentity
qtechVsuVsl = _QtechVsuVsl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 102, 1, 3)
)
_QtechVsuVslPortTable_Object = MibTable
qtechVsuVslPortTable = _QtechVsuVslPortTable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 102, 1, 3, 1)
)
if mibBuilder.loadTexts:
    qtechVsuVslPortTable.setStatus("current")
_QtechVsuVslPortEntry_Object = MibTableRow
qtechVsuVslPortEntry = _QtechVsuVslPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 102, 1, 3, 1, 1)
)
qtechVsuVslPortEntry.setIndexNames(
    (0, "QTECH-VSU-MIB", "qtechVsuVslPortIfIndex"),
)
if mibBuilder.loadTexts:
    qtechVsuVslPortEntry.setStatus("current")
_QtechVsuVslPortIfIndex_Type = Integer32
_QtechVsuVslPortIfIndex_Object = MibTableColumn
qtechVsuVslPortIfIndex = _QtechVsuVslPortIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 102, 1, 3, 1, 1, 1),
    _QtechVsuVslPortIfIndex_Type()
)
qtechVsuVslPortIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechVsuVslPortIfIndex.setStatus("current")
_QtechVsuVslApIf_Type = DisplayString
_QtechVsuVslApIf_Object = MibTableColumn
qtechVsuVslApIf = _QtechVsuVslApIf_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 102, 1, 3, 1, 1, 2),
    _QtechVsuVslApIf_Type()
)
qtechVsuVslApIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechVsuVslApIf.setStatus("current")


class _QtechVsuVslPortState_Type(Integer32):
    """Custom type qtechVsuVslPortState based on Integer32"""
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


_QtechVsuVslPortState_Type.__name__ = "Integer32"
_QtechVsuVslPortState_Object = MibTableColumn
qtechVsuVslPortState = _QtechVsuVslPortState_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 102, 1, 3, 1, 1, 3),
    _QtechVsuVslPortState_Type()
)
qtechVsuVslPortState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechVsuVslPortState.setStatus("current")
_QtechVsuVslPortPeerIfIndex_Type = Integer32
_QtechVsuVslPortPeerIfIndex_Object = MibTableColumn
qtechVsuVslPortPeerIfIndex = _QtechVsuVslPortPeerIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 102, 1, 3, 1, 1, 4),
    _QtechVsuVslPortPeerIfIndex_Type()
)
qtechVsuVslPortPeerIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechVsuVslPortPeerIfIndex.setStatus("current")
_QtechVsuVslTable_Object = MibTable
qtechVsuVslTable = _QtechVsuVslTable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 102, 1, 3, 2)
)
if mibBuilder.loadTexts:
    qtechVsuVslTable.setStatus("current")
_QtechVsuVslEntry_Object = MibTableRow
qtechVsuVslEntry = _QtechVsuVslEntry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 102, 1, 3, 2, 1)
)
qtechVsuVslEntry.setIndexNames(
    (0, "QTECH-VSU-MIB", "qtechVsuVslApIndex"),
)
if mibBuilder.loadTexts:
    qtechVsuVslEntry.setStatus("current")
_QtechVsuVslApIndex_Type = Integer32
_QtechVsuVslApIndex_Object = MibTableColumn
qtechVsuVslApIndex = _QtechVsuVslApIndex_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 102, 1, 3, 2, 1, 1),
    _QtechVsuVslApIndex_Type()
)
qtechVsuVslApIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechVsuVslApIndex.setStatus("current")
_QtechVsuVslApUptime_Type = DisplayString
_QtechVsuVslApUptime_Object = MibTableColumn
qtechVsuVslApUptime = _QtechVsuVslApUptime_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 102, 1, 3, 2, 1, 2),
    _QtechVsuVslApUptime_Type()
)
qtechVsuVslApUptime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechVsuVslApUptime.setStatus("current")
_QtechVsuDad_ObjectIdentity = ObjectIdentity
qtechVsuDad = _QtechVsuDad_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 102, 1, 4)
)
_QtechVsuDadExIntfTable_Object = MibTable
qtechVsuDadExIntfTable = _QtechVsuDadExIntfTable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 102, 1, 4, 1)
)
if mibBuilder.loadTexts:
    qtechVsuDadExIntfTable.setStatus("current")
_QtechVsuDadExIntfEntry_Object = MibTableRow
qtechVsuDadExIntfEntry = _QtechVsuDadExIntfEntry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 102, 1, 4, 1, 1)
)
qtechVsuDadExIntfEntry.setIndexNames(
    (0, "QTECH-VSU-MIB", "qtechVsuDadExIfIndex"),
)
if mibBuilder.loadTexts:
    qtechVsuDadExIntfEntry.setStatus("current")
_QtechVsuDadExIfIndex_Type = Integer32
_QtechVsuDadExIfIndex_Object = MibTableColumn
qtechVsuDadExIfIndex = _QtechVsuDadExIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 102, 1, 4, 1, 1, 1),
    _QtechVsuDadExIfIndex_Type()
)
qtechVsuDadExIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechVsuDadExIfIndex.setStatus("current")
_QtechVsuDadAP_ObjectIdentity = ObjectIdentity
qtechVsuDadAP = _QtechVsuDadAP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 102, 1, 4, 2)
)


class _QtechVsuDadAPEnable_Type(Integer32):
    """Custom type qtechVsuDadAPEnable based on Integer32"""
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


_QtechVsuDadAPEnable_Type.__name__ = "Integer32"
_QtechVsuDadAPEnable_Object = MibScalar
qtechVsuDadAPEnable = _QtechVsuDadAPEnable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 102, 1, 4, 2, 1),
    _QtechVsuDadAPEnable_Type()
)
qtechVsuDadAPEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechVsuDadAPEnable.setStatus("current")
_QtechVsuDadAPIfIndex_Type = Integer32
_QtechVsuDadAPIfIndex_Object = MibScalar
qtechVsuDadAPIfIndex = _QtechVsuDadAPIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 102, 1, 4, 2, 2),
    _QtechVsuDadAPIfIndex_Type()
)
qtechVsuDadAPIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechVsuDadAPIfIndex.setStatus("current")


class _QtechVsuDadAPIfStatus_Type(Integer32):
    """Custom type qtechVsuDadAPIfStatus based on Integer32"""
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


_QtechVsuDadAPIfStatus_Type.__name__ = "Integer32"
_QtechVsuDadAPIfStatus_Object = MibScalar
qtechVsuDadAPIfStatus = _QtechVsuDadAPIfStatus_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 102, 1, 4, 2, 3),
    _QtechVsuDadAPIfStatus_Type()
)
qtechVsuDadAPIfStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechVsuDadAPIfStatus.setStatus("current")
_QtechVsuDadAPMemberIfTable_Object = MibTable
qtechVsuDadAPMemberIfTable = _QtechVsuDadAPMemberIfTable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 102, 1, 4, 2, 4)
)
if mibBuilder.loadTexts:
    qtechVsuDadAPMemberIfTable.setStatus("current")
_QtechVsuDadAPMemberIfEntry_Object = MibTableRow
qtechVsuDadAPMemberIfEntry = _QtechVsuDadAPMemberIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 102, 1, 4, 2, 4, 1)
)
qtechVsuDadAPMemberIfEntry.setIndexNames(
    (0, "QTECH-VSU-MIB", "qtechVsuDadAPMemberIfindex"),
)
if mibBuilder.loadTexts:
    qtechVsuDadAPMemberIfEntry.setStatus("current")
_QtechVsuDadAPMemberIfindex_Type = Integer32
_QtechVsuDadAPMemberIfindex_Object = MibTableColumn
qtechVsuDadAPMemberIfindex = _QtechVsuDadAPMemberIfindex_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 102, 1, 4, 2, 4, 1, 1),
    _QtechVsuDadAPMemberIfindex_Type()
)
qtechVsuDadAPMemberIfindex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechVsuDadAPMemberIfindex.setStatus("current")


class _QtechVsuDadAPMemberIfStatus_Type(Integer32):
    """Custom type qtechVsuDadAPMemberIfStatus based on Integer32"""
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


_QtechVsuDadAPMemberIfStatus_Type.__name__ = "Integer32"
_QtechVsuDadAPMemberIfStatus_Object = MibTableColumn
qtechVsuDadAPMemberIfStatus = _QtechVsuDadAPMemberIfStatus_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 102, 1, 4, 2, 4, 1, 2),
    _QtechVsuDadAPMemberIfStatus_Type()
)
qtechVsuDadAPMemberIfStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechVsuDadAPMemberIfStatus.setStatus("current")
_QtechVsuDadAPRelayIfTable_Object = MibTable
qtechVsuDadAPRelayIfTable = _QtechVsuDadAPRelayIfTable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 102, 1, 4, 2, 5)
)
if mibBuilder.loadTexts:
    qtechVsuDadAPRelayIfTable.setStatus("current")
_QtechVsuDadAPRelayIfEntry_Object = MibTableRow
qtechVsuDadAPRelayIfEntry = _QtechVsuDadAPRelayIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 102, 1, 4, 2, 5, 1)
)
qtechVsuDadAPRelayIfEntry.setIndexNames(
    (0, "QTECH-VSU-MIB", "qtechVsuDadAPRelayIfIndex"),
)
if mibBuilder.loadTexts:
    qtechVsuDadAPRelayIfEntry.setStatus("current")
_QtechVsuDadAPRelayIfIndex_Type = Integer32
_QtechVsuDadAPRelayIfIndex_Object = MibTableColumn
qtechVsuDadAPRelayIfIndex = _QtechVsuDadAPRelayIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 102, 1, 4, 2, 5, 1, 1),
    _QtechVsuDadAPRelayIfIndex_Type()
)
qtechVsuDadAPRelayIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechVsuDadAPRelayIfIndex.setStatus("current")
_QtechVsuDadBFD_ObjectIdentity = ObjectIdentity
qtechVsuDadBFD = _QtechVsuDadBFD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 102, 1, 4, 3)
)


class _QtechVsuDadBFDEnable_Type(Integer32):
    """Custom type qtechVsuDadBFDEnable based on Integer32"""
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


_QtechVsuDadBFDEnable_Type.__name__ = "Integer32"
_QtechVsuDadBFDEnable_Object = MibScalar
qtechVsuDadBFDEnable = _QtechVsuDadBFDEnable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 102, 1, 4, 3, 1),
    _QtechVsuDadBFDEnable_Type()
)
qtechVsuDadBFDEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechVsuDadBFDEnable.setStatus("current")
_QtechVsuDadBFDIfTable_Object = MibTable
qtechVsuDadBFDIfTable = _QtechVsuDadBFDIfTable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 102, 1, 4, 3, 2)
)
if mibBuilder.loadTexts:
    qtechVsuDadBFDIfTable.setStatus("current")
_QtechVsuDadBFDIfEntry_Object = MibTableRow
qtechVsuDadBFDIfEntry = _QtechVsuDadBFDIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 102, 1, 4, 3, 2, 1)
)
qtechVsuDadBFDIfEntry.setIndexNames(
    (0, "QTECH-VSU-MIB", "qtechVsuDadBFDIfIndex1"),
    (0, "QTECH-VSU-MIB", "qtechVsuDadBFDIfIndex2"),
)
if mibBuilder.loadTexts:
    qtechVsuDadBFDIfEntry.setStatus("current")
_QtechVsuDadBFDIfIndex1_Type = Integer32
_QtechVsuDadBFDIfIndex1_Object = MibTableColumn
qtechVsuDadBFDIfIndex1 = _QtechVsuDadBFDIfIndex1_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 102, 1, 4, 3, 2, 1, 1),
    _QtechVsuDadBFDIfIndex1_Type()
)
qtechVsuDadBFDIfIndex1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechVsuDadBFDIfIndex1.setStatus("current")
_QtechVsuDadBFDIfIndex2_Type = Integer32
_QtechVsuDadBFDIfIndex2_Object = MibTableColumn
qtechVsuDadBFDIfIndex2 = _QtechVsuDadBFDIfIndex2_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 102, 1, 4, 3, 2, 1, 2),
    _QtechVsuDadBFDIfIndex2_Type()
)
qtechVsuDadBFDIfIndex2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechVsuDadBFDIfIndex2.setStatus("current")


class _QtechVsuDadBFDIfStatus_Type(Integer32):
    """Custom type qtechVsuDadBFDIfStatus based on Integer32"""
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


_QtechVsuDadBFDIfStatus_Type.__name__ = "Integer32"
_QtechVsuDadBFDIfStatus_Object = MibTableColumn
qtechVsuDadBFDIfStatus = _QtechVsuDadBFDIfStatus_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 102, 1, 4, 3, 2, 1, 3),
    _QtechVsuDadBFDIfStatus_Type()
)
qtechVsuDadBFDIfStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechVsuDadBFDIfStatus.setStatus("current")
_QtechVsuForward_ObjectIdentity = ObjectIdentity
qtechVsuForward = _QtechVsuForward_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 102, 1, 5)
)


class _QtechVsuForwardApllf_Type(Integer32):
    """Custom type qtechVsuForwardApllf based on Integer32"""
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


_QtechVsuForwardApllf_Type.__name__ = "Integer32"
_QtechVsuForwardApllf_Object = MibScalar
qtechVsuForwardApllf = _QtechVsuForwardApllf_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 102, 1, 5, 1),
    _QtechVsuForwardApllf_Type()
)
qtechVsuForwardApllf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechVsuForwardApllf.setStatus("current")


class _QtechVsuForwardEcmpllf_Type(Integer32):
    """Custom type qtechVsuForwardEcmpllf based on Integer32"""
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


_QtechVsuForwardEcmpllf_Type.__name__ = "Integer32"
_QtechVsuForwardEcmpllf_Object = MibScalar
qtechVsuForwardEcmpllf = _QtechVsuForwardEcmpllf_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 102, 1, 5, 2),
    _QtechVsuForwardEcmpllf_Type()
)
qtechVsuForwardEcmpllf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechVsuForwardEcmpllf.setStatus("current")
_QtechVsuVersion_Type = DisplayString
_QtechVsuVersion_Object = MibScalar
qtechVsuVersion = _QtechVsuVersion_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 102, 1, 6),
    _QtechVsuVersion_Type()
)
qtechVsuVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechVsuVersion.setStatus("current")
_QtechVsuMIBTraps_ObjectIdentity = ObjectIdentity
qtechVsuMIBTraps = _QtechVsuMIBTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 102, 2)
)
_QtechVsuTrapsNtfObjects_ObjectIdentity = ObjectIdentity
qtechVsuTrapsNtfObjects = _QtechVsuTrapsNtfObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 102, 2, 1)
)


class _QtechVsuDeviceState_Type(Integer32):
    """Custom type qtechVsuDeviceState based on Integer32"""
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


_QtechVsuDeviceState_Type.__name__ = "Integer32"
_QtechVsuDeviceState_Object = MibScalar
qtechVsuDeviceState = _QtechVsuDeviceState_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 102, 2, 1, 1),
    _QtechVsuDeviceState_Type()
)
qtechVsuDeviceState.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    qtechVsuDeviceState.setStatus("current")
_QtechVsuSlotID_Type = Integer32
_QtechVsuSlotID_Object = MibScalar
qtechVsuSlotID = _QtechVsuSlotID_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 102, 2, 1, 2),
    _QtechVsuSlotID_Type()
)
qtechVsuSlotID.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    qtechVsuSlotID.setStatus("current")


class _QtechVsuDadResult_Type(Integer32):
    """Custom type qtechVsuDadResult based on Integer32"""
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


_QtechVsuDadResult_Type.__name__ = "Integer32"
_QtechVsuDadResult_Object = MibScalar
qtechVsuDadResult = _QtechVsuDadResult_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 102, 2, 1, 3),
    _QtechVsuDadResult_Type()
)
qtechVsuDadResult.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    qtechVsuDadResult.setStatus("current")
_QtechVsuTrapsNotifications_ObjectIdentity = ObjectIdentity
qtechVsuTrapsNotifications = _QtechVsuTrapsNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 102, 2, 2)
)
_QtechVsuMIBConformance_ObjectIdentity = ObjectIdentity
qtechVsuMIBConformance = _QtechVsuMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 102, 3)
)
_QtechVsuMIBCompliances_ObjectIdentity = ObjectIdentity
qtechVsuMIBCompliances = _QtechVsuMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 102, 3, 1)
)
_QtechVsuMIBGroups_ObjectIdentity = ObjectIdentity
qtechVsuMIBGroups = _QtechVsuMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 102, 3, 2)
)

# Managed Objects groups

qtechVsuMIBObjectsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 102, 3, 2, 1)
)
qtechVsuMIBObjectsGroup.setObjects(
      *(("QTECH-VSU-MIB", "qtechVsuTopoShape"),
        ("QTECH-VSU-MIB", "qtechVsuTopoConn"),
        ("QTECH-VSU-MIB", "qtechVsuDomainID"),
        ("QTECH-VSU-MIB", "qtechVsuDeviceID"),
        ("QTECH-VSU-MIB", "qtechVsuDeviceMac"),
        ("QTECH-VSU-MIB", "qtechVsuDevicePri"),
        ("QTECH-VSU-MIB", "qtechVsuDeviceDescr"),
        ("QTECH-VSU-MIB", "qtechVsuDeviceStatus"),
        ("QTECH-VSU-MIB", "qtechVsuDeviceRole"),
        ("QTECH-VSU-MIB", "qtechVsuVslPortIfIndex"),
        ("QTECH-VSU-MIB", "qtechVsuVslApIf"),
        ("QTECH-VSU-MIB", "qtechVsuVslPortState"),
        ("QTECH-VSU-MIB", "qtechVsuVslPortPeerIfIndex"),
        ("QTECH-VSU-MIB", "qtechVsuVslApUptime"),
        ("QTECH-VSU-MIB", "qtechVsuDadExIfIndex"),
        ("QTECH-VSU-MIB", "qtechVsuDadAPEnable"),
        ("QTECH-VSU-MIB", "qtechVsuDadAPIfIndex"),
        ("QTECH-VSU-MIB", "qtechVsuDadAPIfStatus"),
        ("QTECH-VSU-MIB", "qtechVsuDadAPMemberIfindex"),
        ("QTECH-VSU-MIB", "qtechVsuDadAPMemberIfStatus"),
        ("QTECH-VSU-MIB", "qtechVsuDadAPRelayIfIndex"),
        ("QTECH-VSU-MIB", "qtechVsuDadBFDEnable"),
        ("QTECH-VSU-MIB", "qtechVsuDadBFDIfIndex1"),
        ("QTECH-VSU-MIB", "qtechVsuDadBFDIfIndex2"),
        ("QTECH-VSU-MIB", "qtechVsuDadBFDIfStatus"),
        ("QTECH-VSU-MIB", "qtechVsuForwardApllf"),
        ("QTECH-VSU-MIB", "qtechVsuForwardEcmpllf"),
        ("QTECH-VSU-MIB", "qtechVsuVersion"),
        ("QTECH-VSU-MIB", "qtechVsuDeviceState"),
        ("QTECH-VSU-MIB", "qtechVsuSlotID"),
        ("QTECH-VSU-MIB", "qtechVsuDadResult"))
)
if mibBuilder.loadTexts:
    qtechVsuMIBObjectsGroup.setStatus("current")


# Notification objects

qtechVsuNotifyTopoChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 102, 2, 2, 1)
)
qtechVsuNotifyTopoChange.setObjects(
    ("QTECH-VSU-MIB", "qtechVsuTopoShape")
)
if mibBuilder.loadTexts:
    qtechVsuNotifyTopoChange.setStatus(
        "current"
    )

qtechVsuNotifyDeviceChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 102, 2, 2, 2)
)
qtechVsuNotifyDeviceChange.setObjects(
      *(("QTECH-VSU-MIB", "qtechVsuDeviceID"),
        ("QTECH-VSU-MIB", "qtechVsuDeviceState"))
)
if mibBuilder.loadTexts:
    qtechVsuNotifyDeviceChange.setStatus(
        "current"
    )

qtechVsuNotifyDeviceRoleChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 102, 2, 2, 3)
)
qtechVsuNotifyDeviceRoleChange.setObjects(
      *(("QTECH-VSU-MIB", "qtechVsuDeviceID"),
        ("QTECH-VSU-MIB", "qtechVsuSlotID"),
        ("QTECH-VSU-MIB", "qtechVsuDeviceRole"))
)
if mibBuilder.loadTexts:
    qtechVsuNotifyDeviceRoleChange.setStatus(
        "current"
    )

qtechVsuNotifyDad = NotificationType(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 102, 2, 2, 4)
)
qtechVsuNotifyDad.setObjects(
    ("QTECH-VSU-MIB", "qtechVsuDadResult")
)
if mibBuilder.loadTexts:
    qtechVsuNotifyDad.setStatus(
        "current"
    )


# Notifications groups

qtechVsuMIBTrapsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 102, 3, 2, 2)
)
qtechVsuMIBTrapsGroup.setObjects(
      *(("QTECH-VSU-MIB", "qtechVsuNotifyTopoChange"),
        ("QTECH-VSU-MIB", "qtechVsuNotifyDeviceChange"),
        ("QTECH-VSU-MIB", "qtechVsuNotifyDeviceRoleChange"),
        ("QTECH-VSU-MIB", "qtechVsuNotifyDad"))
)
if mibBuilder.loadTexts:
    qtechVsuMIBTrapsGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

qtechVsuMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 102, 3, 1, 1)
)
qtechVsuMIBCompliance.setObjects(
      *(("QTECH-VSU-MIB", "qtechVsuMIBObjectsGroup"),
        ("QTECH-VSU-MIB", "qtechVsuMIBTrapsGroup"))
)
if mibBuilder.loadTexts:
    qtechVsuMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "QTECH-VSU-MIB",
    **{"qtechVsuMIB": qtechVsuMIB,
       "qtechVsuMIBObjects": qtechVsuMIBObjects,
       "qtechVsuTopo": qtechVsuTopo,
       "qtechVsuTopoShape": qtechVsuTopoShape,
       "qtechVsuTopoConn": qtechVsuTopoConn,
       "qtechVsuDeviceInfo": qtechVsuDeviceInfo,
       "qtechVsuDomainID": qtechVsuDomainID,
       "qtechVsuDeviceTable": qtechVsuDeviceTable,
       "qtechVsuDeviceEntry": qtechVsuDeviceEntry,
       "qtechVsuDeviceID": qtechVsuDeviceID,
       "qtechVsuDeviceMac": qtechVsuDeviceMac,
       "qtechVsuDevicePri": qtechVsuDevicePri,
       "qtechVsuDeviceDescr": qtechVsuDeviceDescr,
       "qtechVsuDeviceStatus": qtechVsuDeviceStatus,
       "qtechVsuDeviceRole": qtechVsuDeviceRole,
       "qtechVsuVsl": qtechVsuVsl,
       "qtechVsuVslPortTable": qtechVsuVslPortTable,
       "qtechVsuVslPortEntry": qtechVsuVslPortEntry,
       "qtechVsuVslPortIfIndex": qtechVsuVslPortIfIndex,
       "qtechVsuVslApIf": qtechVsuVslApIf,
       "qtechVsuVslPortState": qtechVsuVslPortState,
       "qtechVsuVslPortPeerIfIndex": qtechVsuVslPortPeerIfIndex,
       "qtechVsuVslTable": qtechVsuVslTable,
       "qtechVsuVslEntry": qtechVsuVslEntry,
       "qtechVsuVslApIndex": qtechVsuVslApIndex,
       "qtechVsuVslApUptime": qtechVsuVslApUptime,
       "qtechVsuDad": qtechVsuDad,
       "qtechVsuDadExIntfTable": qtechVsuDadExIntfTable,
       "qtechVsuDadExIntfEntry": qtechVsuDadExIntfEntry,
       "qtechVsuDadExIfIndex": qtechVsuDadExIfIndex,
       "qtechVsuDadAP": qtechVsuDadAP,
       "qtechVsuDadAPEnable": qtechVsuDadAPEnable,
       "qtechVsuDadAPIfIndex": qtechVsuDadAPIfIndex,
       "qtechVsuDadAPIfStatus": qtechVsuDadAPIfStatus,
       "qtechVsuDadAPMemberIfTable": qtechVsuDadAPMemberIfTable,
       "qtechVsuDadAPMemberIfEntry": qtechVsuDadAPMemberIfEntry,
       "qtechVsuDadAPMemberIfindex": qtechVsuDadAPMemberIfindex,
       "qtechVsuDadAPMemberIfStatus": qtechVsuDadAPMemberIfStatus,
       "qtechVsuDadAPRelayIfTable": qtechVsuDadAPRelayIfTable,
       "qtechVsuDadAPRelayIfEntry": qtechVsuDadAPRelayIfEntry,
       "qtechVsuDadAPRelayIfIndex": qtechVsuDadAPRelayIfIndex,
       "qtechVsuDadBFD": qtechVsuDadBFD,
       "qtechVsuDadBFDEnable": qtechVsuDadBFDEnable,
       "qtechVsuDadBFDIfTable": qtechVsuDadBFDIfTable,
       "qtechVsuDadBFDIfEntry": qtechVsuDadBFDIfEntry,
       "qtechVsuDadBFDIfIndex1": qtechVsuDadBFDIfIndex1,
       "qtechVsuDadBFDIfIndex2": qtechVsuDadBFDIfIndex2,
       "qtechVsuDadBFDIfStatus": qtechVsuDadBFDIfStatus,
       "qtechVsuForward": qtechVsuForward,
       "qtechVsuForwardApllf": qtechVsuForwardApllf,
       "qtechVsuForwardEcmpllf": qtechVsuForwardEcmpllf,
       "qtechVsuVersion": qtechVsuVersion,
       "qtechVsuMIBTraps": qtechVsuMIBTraps,
       "qtechVsuTrapsNtfObjects": qtechVsuTrapsNtfObjects,
       "qtechVsuDeviceState": qtechVsuDeviceState,
       "qtechVsuSlotID": qtechVsuSlotID,
       "qtechVsuDadResult": qtechVsuDadResult,
       "qtechVsuTrapsNotifications": qtechVsuTrapsNotifications,
       "qtechVsuNotifyTopoChange": qtechVsuNotifyTopoChange,
       "qtechVsuNotifyDeviceChange": qtechVsuNotifyDeviceChange,
       "qtechVsuNotifyDeviceRoleChange": qtechVsuNotifyDeviceRoleChange,
       "qtechVsuNotifyDad": qtechVsuNotifyDad,
       "qtechVsuMIBConformance": qtechVsuMIBConformance,
       "qtechVsuMIBCompliances": qtechVsuMIBCompliances,
       "qtechVsuMIBCompliance": qtechVsuMIBCompliance,
       "qtechVsuMIBGroups": qtechVsuMIBGroups,
       "qtechVsuMIBObjectsGroup": qtechVsuMIBObjectsGroup,
       "qtechVsuMIBTrapsGroup": qtechVsuMIBTrapsGroup}
)
