# SNMP MIB module (FS-CAPWAP-SERVER-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/fscom/FS-CAPWAP-SERVER-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:12:26 2025
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
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

fsCapwapSvrMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 89)
)
if mibBuilder.loadTexts:
    fsCapwapSvrMIB.setRevisions(
        ("2010-08-24 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_FsCapwapSvrMIBObjects_ObjectIdentity = ObjectIdentity
fsCapwapSvrMIBObjects = _FsCapwapSvrMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 89, 1)
)
_FsCapwapSvrWhiteListURLTable_Object = MibTable
fsCapwapSvrWhiteListURLTable = _FsCapwapSvrWhiteListURLTable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 89, 1, 1)
)
if mibBuilder.loadTexts:
    fsCapwapSvrWhiteListURLTable.setStatus("current")
_FsCapwapSvrWhiteListURLEntry_Object = MibTableRow
fsCapwapSvrWhiteListURLEntry = _FsCapwapSvrWhiteListURLEntry_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 89, 1, 1, 1)
)
fsCapwapSvrWhiteListURLEntry.setIndexNames(
    (0, "FS-CAPWAP-SERVER-MIB", "fsCapwapSvrWhiteListIndex"),
)
if mibBuilder.loadTexts:
    fsCapwapSvrWhiteListURLEntry.setStatus("current")
_FsCapwapSvrWhiteListIndex_Type = Unsigned32
_FsCapwapSvrWhiteListIndex_Object = MibTableColumn
fsCapwapSvrWhiteListIndex = _FsCapwapSvrWhiteListIndex_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 89, 1, 1, 1, 1),
    _FsCapwapSvrWhiteListIndex_Type()
)
fsCapwapSvrWhiteListIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsCapwapSvrWhiteListIndex.setStatus("current")


class _FsCapwapSvrWhiteListURL_Type(DisplayString):
    """Custom type fsCapwapSvrWhiteListURL based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_FsCapwapSvrWhiteListURL_Type.__name__ = "DisplayString"
_FsCapwapSvrWhiteListURL_Object = MibTableColumn
fsCapwapSvrWhiteListURL = _FsCapwapSvrWhiteListURL_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 89, 1, 1, 1, 2),
    _FsCapwapSvrWhiteListURL_Type()
)
fsCapwapSvrWhiteListURL.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsCapwapSvrWhiteListURL.setStatus("current")


class _FsCapwapSvrWhiteListURLParserStatus_Type(DisplayString):
    """Custom type fsCapwapSvrWhiteListURLParserStatus based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_FsCapwapSvrWhiteListURLParserStatus_Type.__name__ = "DisplayString"
_FsCapwapSvrWhiteListURLParserStatus_Object = MibTableColumn
fsCapwapSvrWhiteListURLParserStatus = _FsCapwapSvrWhiteListURLParserStatus_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 89, 1, 1, 1, 3),
    _FsCapwapSvrWhiteListURLParserStatus_Type()
)
fsCapwapSvrWhiteListURLParserStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsCapwapSvrWhiteListURLParserStatus.setStatus("current")
_FsCapwapSvrWhiteListURLRowStatus_Type = RowStatus
_FsCapwapSvrWhiteListURLRowStatus_Object = MibTableColumn
fsCapwapSvrWhiteListURLRowStatus = _FsCapwapSvrWhiteListURLRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 89, 1, 1, 1, 4),
    _FsCapwapSvrWhiteListURLRowStatus_Type()
)
fsCapwapSvrWhiteListURLRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsCapwapSvrWhiteListURLRowStatus.setStatus("current")
_FsCapwapSvrWhiteListIPTable_Object = MibTable
fsCapwapSvrWhiteListIPTable = _FsCapwapSvrWhiteListIPTable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 89, 1, 2)
)
if mibBuilder.loadTexts:
    fsCapwapSvrWhiteListIPTable.setStatus("current")
_FsCapwapSvrWhiteListIPEntry_Object = MibTableRow
fsCapwapSvrWhiteListIPEntry = _FsCapwapSvrWhiteListIPEntry_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 89, 1, 2, 1)
)
fsCapwapSvrWhiteListIPEntry.setIndexNames(
    (0, "FS-CAPWAP-SERVER-MIB", "fsCapwapSvrWhiteListIP"),
)
if mibBuilder.loadTexts:
    fsCapwapSvrWhiteListIPEntry.setStatus("current")
_FsCapwapSvrWhiteListIP_Type = IpAddress
_FsCapwapSvrWhiteListIP_Object = MibTableColumn
fsCapwapSvrWhiteListIP = _FsCapwapSvrWhiteListIP_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 89, 1, 2, 1, 1),
    _FsCapwapSvrWhiteListIP_Type()
)
fsCapwapSvrWhiteListIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsCapwapSvrWhiteListIP.setStatus("current")
_FsCapwapSvrWhiteListIPRowStatus_Type = RowStatus
_FsCapwapSvrWhiteListIPRowStatus_Object = MibTableColumn
fsCapwapSvrWhiteListIPRowStatus = _FsCapwapSvrWhiteListIPRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 89, 1, 2, 1, 2),
    _FsCapwapSvrWhiteListIPRowStatus_Type()
)
fsCapwapSvrWhiteListIPRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsCapwapSvrWhiteListIPRowStatus.setStatus("current")
_FsCapwapSvrBlackListURLTable_Object = MibTable
fsCapwapSvrBlackListURLTable = _FsCapwapSvrBlackListURLTable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 89, 1, 3)
)
if mibBuilder.loadTexts:
    fsCapwapSvrBlackListURLTable.setStatus("current")
_FsCapwapSvrBlackListURLEntry_Object = MibTableRow
fsCapwapSvrBlackListURLEntry = _FsCapwapSvrBlackListURLEntry_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 89, 1, 3, 1)
)
fsCapwapSvrBlackListURLEntry.setIndexNames(
    (0, "FS-CAPWAP-SERVER-MIB", "fsCapwapSvrBlackListIndex"),
)
if mibBuilder.loadTexts:
    fsCapwapSvrBlackListURLEntry.setStatus("current")
_FsCapwapSvrBlackListIndex_Type = Unsigned32
_FsCapwapSvrBlackListIndex_Object = MibTableColumn
fsCapwapSvrBlackListIndex = _FsCapwapSvrBlackListIndex_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 89, 1, 3, 1, 1),
    _FsCapwapSvrBlackListIndex_Type()
)
fsCapwapSvrBlackListIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsCapwapSvrBlackListIndex.setStatus("current")


class _FsCapwapSvrBlackListURL_Type(DisplayString):
    """Custom type fsCapwapSvrBlackListURL based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_FsCapwapSvrBlackListURL_Type.__name__ = "DisplayString"
_FsCapwapSvrBlackListURL_Object = MibTableColumn
fsCapwapSvrBlackListURL = _FsCapwapSvrBlackListURL_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 89, 1, 3, 1, 2),
    _FsCapwapSvrBlackListURL_Type()
)
fsCapwapSvrBlackListURL.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsCapwapSvrBlackListURL.setStatus("current")


class _FsCapwapSvrBlackListURLParserStatus_Type(DisplayString):
    """Custom type fsCapwapSvrBlackListURLParserStatus based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_FsCapwapSvrBlackListURLParserStatus_Type.__name__ = "DisplayString"
_FsCapwapSvrBlackListURLParserStatus_Object = MibTableColumn
fsCapwapSvrBlackListURLParserStatus = _FsCapwapSvrBlackListURLParserStatus_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 89, 1, 3, 1, 3),
    _FsCapwapSvrBlackListURLParserStatus_Type()
)
fsCapwapSvrBlackListURLParserStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsCapwapSvrBlackListURLParserStatus.setStatus("current")
_FsCapwapSvrBlackListURLRowStatus_Type = RowStatus
_FsCapwapSvrBlackListURLRowStatus_Object = MibTableColumn
fsCapwapSvrBlackListURLRowStatus = _FsCapwapSvrBlackListURLRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 89, 1, 3, 1, 4),
    _FsCapwapSvrBlackListURLRowStatus_Type()
)
fsCapwapSvrBlackListURLRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsCapwapSvrBlackListURLRowStatus.setStatus("current")
_FsCapwapSvrBlackListIPTable_Object = MibTable
fsCapwapSvrBlackListIPTable = _FsCapwapSvrBlackListIPTable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 89, 1, 4)
)
if mibBuilder.loadTexts:
    fsCapwapSvrBlackListIPTable.setStatus("current")
_FsCapwapSvrBlackListIPEntry_Object = MibTableRow
fsCapwapSvrBlackListIPEntry = _FsCapwapSvrBlackListIPEntry_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 89, 1, 4, 1)
)
fsCapwapSvrBlackListIPEntry.setIndexNames(
    (0, "FS-CAPWAP-SERVER-MIB", "fsCapwapSvrBlackListIP"),
)
if mibBuilder.loadTexts:
    fsCapwapSvrBlackListIPEntry.setStatus("current")
_FsCapwapSvrBlackListIP_Type = IpAddress
_FsCapwapSvrBlackListIP_Object = MibTableColumn
fsCapwapSvrBlackListIP = _FsCapwapSvrBlackListIP_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 89, 1, 4, 1, 1),
    _FsCapwapSvrBlackListIP_Type()
)
fsCapwapSvrBlackListIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsCapwapSvrBlackListIP.setStatus("current")
_FsCapwapSvrBlackListIPRowStatus_Type = RowStatus
_FsCapwapSvrBlackListIPRowStatus_Object = MibTableColumn
fsCapwapSvrBlackListIPRowStatus = _FsCapwapSvrBlackListIPRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 89, 1, 4, 1, 2),
    _FsCapwapSvrBlackListIPRowStatus_Type()
)
fsCapwapSvrBlackListIPRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsCapwapSvrBlackListIPRowStatus.setStatus("current")
_FsCapwapSvrBlackListPortTable_Object = MibTable
fsCapwapSvrBlackListPortTable = _FsCapwapSvrBlackListPortTable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 89, 1, 5)
)
if mibBuilder.loadTexts:
    fsCapwapSvrBlackListPortTable.setStatus("current")
_FsCapwapSvrBlackListPortEntry_Object = MibTableRow
fsCapwapSvrBlackListPortEntry = _FsCapwapSvrBlackListPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 89, 1, 5, 1)
)
fsCapwapSvrBlackListPortEntry.setIndexNames(
    (0, "FS-CAPWAP-SERVER-MIB", "fsCapwapSvrBlackListPort"),
)
if mibBuilder.loadTexts:
    fsCapwapSvrBlackListPortEntry.setStatus("current")
_FsCapwapSvrBlackListPort_Type = Integer32
_FsCapwapSvrBlackListPort_Object = MibTableColumn
fsCapwapSvrBlackListPort = _FsCapwapSvrBlackListPort_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 89, 1, 5, 1, 1),
    _FsCapwapSvrBlackListPort_Type()
)
fsCapwapSvrBlackListPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsCapwapSvrBlackListPort.setStatus("current")
_FsCapwapSvrBlackListPortRowStatus_Type = RowStatus
_FsCapwapSvrBlackListPortRowStatus_Object = MibTableColumn
fsCapwapSvrBlackListPortRowStatus = _FsCapwapSvrBlackListPortRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 89, 1, 5, 1, 2),
    _FsCapwapSvrBlackListPortRowStatus_Type()
)
fsCapwapSvrBlackListPortRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsCapwapSvrBlackListPortRowStatus.setStatus("current")
_FsCapwapSvrWhiteListMacTable_Object = MibTable
fsCapwapSvrWhiteListMacTable = _FsCapwapSvrWhiteListMacTable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 89, 1, 6)
)
if mibBuilder.loadTexts:
    fsCapwapSvrWhiteListMacTable.setStatus("current")
_FsCapwapSvrWhiteListMacEntry_Object = MibTableRow
fsCapwapSvrWhiteListMacEntry = _FsCapwapSvrWhiteListMacEntry_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 89, 1, 6, 1)
)
fsCapwapSvrWhiteListMacEntry.setIndexNames(
    (0, "FS-CAPWAP-SERVER-MIB", "fsCapwapSvrWhiteListMacIndex"),
)
if mibBuilder.loadTexts:
    fsCapwapSvrWhiteListMacEntry.setStatus("current")
_FsCapwapSvrWhiteListMacIndex_Type = Unsigned32
_FsCapwapSvrWhiteListMacIndex_Object = MibTableColumn
fsCapwapSvrWhiteListMacIndex = _FsCapwapSvrWhiteListMacIndex_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 89, 1, 6, 1, 1),
    _FsCapwapSvrWhiteListMacIndex_Type()
)
fsCapwapSvrWhiteListMacIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsCapwapSvrWhiteListMacIndex.setStatus("current")
_FsCapwapSvrWhiteListMac_Type = MacAddress
_FsCapwapSvrWhiteListMac_Object = MibTableColumn
fsCapwapSvrWhiteListMac = _FsCapwapSvrWhiteListMac_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 89, 1, 6, 1, 2),
    _FsCapwapSvrWhiteListMac_Type()
)
fsCapwapSvrWhiteListMac.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsCapwapSvrWhiteListMac.setStatus("current")
_FsCapwapSvrWhiteListMacRowStatus_Type = RowStatus
_FsCapwapSvrWhiteListMacRowStatus_Object = MibTableColumn
fsCapwapSvrWhiteListMacRowStatus = _FsCapwapSvrWhiteListMacRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 89, 1, 6, 1, 3),
    _FsCapwapSvrWhiteListMacRowStatus_Type()
)
fsCapwapSvrWhiteListMacRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsCapwapSvrWhiteListMacRowStatus.setStatus("current")
_FsCapwapSvrMIBConformance_ObjectIdentity = ObjectIdentity
fsCapwapSvrMIBConformance = _FsCapwapSvrMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 89, 2)
)
_FsCapwapSvrMIBCompliances_ObjectIdentity = ObjectIdentity
fsCapwapSvrMIBCompliances = _FsCapwapSvrMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 89, 2, 1)
)
_FsCapwapSvrMIBGroups_ObjectIdentity = ObjectIdentity
fsCapwapSvrMIBGroups = _FsCapwapSvrMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 89, 2, 2)
)

# Managed Objects groups

fsCapwapSvrMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 89, 2, 2, 1)
)
fsCapwapSvrMIBGroup.setObjects(
      *(("FS-CAPWAP-SERVER-MIB", "fsCapwapSvrWhiteListURL"),
        ("FS-CAPWAP-SERVER-MIB", "fsCapwapSvrWhiteListURLParserStatus"),
        ("FS-CAPWAP-SERVER-MIB", "fsCapwapSvrWhiteListURLRowStatus"),
        ("FS-CAPWAP-SERVER-MIB", "fsCapwapSvrWhiteListIP"),
        ("FS-CAPWAP-SERVER-MIB", "fsCapwapSvrWhiteListIPRowStatus"),
        ("FS-CAPWAP-SERVER-MIB", "fsCapwapSvrBlackListURL"),
        ("FS-CAPWAP-SERVER-MIB", "fsCapwapSvrBlackListURLParserStatus"),
        ("FS-CAPWAP-SERVER-MIB", "fsCapwapSvrBlackListURLRowStatus"),
        ("FS-CAPWAP-SERVER-MIB", "fsCapwapSvrBlackListIP"),
        ("FS-CAPWAP-SERVER-MIB", "fsCapwapSvrBlackListIPRowStatus"),
        ("FS-CAPWAP-SERVER-MIB", "fsCapwapSvrBlackListPort"),
        ("FS-CAPWAP-SERVER-MIB", "fsCapwapSvrBlackListPortRowStatus"),
        ("FS-CAPWAP-SERVER-MIB", "fsCapwapSvrWhiteListMac"),
        ("FS-CAPWAP-SERVER-MIB", "fsCapwapSvrWhiteListMacRowStatus"))
)
if mibBuilder.loadTexts:
    fsCapwapSvrMIBGroup.setStatus("deprecated")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

fsCapwapSvrMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 89, 2, 1, 1)
)
fsCapwapSvrMIBCompliance.setObjects(
    ("FS-CAPWAP-SERVER-MIB", "fsCapwapSvrMIBGroup")
)
if mibBuilder.loadTexts:
    fsCapwapSvrMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "FS-CAPWAP-SERVER-MIB",
    **{"fsCapwapSvrMIB": fsCapwapSvrMIB,
       "fsCapwapSvrMIBObjects": fsCapwapSvrMIBObjects,
       "fsCapwapSvrWhiteListURLTable": fsCapwapSvrWhiteListURLTable,
       "fsCapwapSvrWhiteListURLEntry": fsCapwapSvrWhiteListURLEntry,
       "fsCapwapSvrWhiteListIndex": fsCapwapSvrWhiteListIndex,
       "fsCapwapSvrWhiteListURL": fsCapwapSvrWhiteListURL,
       "fsCapwapSvrWhiteListURLParserStatus": fsCapwapSvrWhiteListURLParserStatus,
       "fsCapwapSvrWhiteListURLRowStatus": fsCapwapSvrWhiteListURLRowStatus,
       "fsCapwapSvrWhiteListIPTable": fsCapwapSvrWhiteListIPTable,
       "fsCapwapSvrWhiteListIPEntry": fsCapwapSvrWhiteListIPEntry,
       "fsCapwapSvrWhiteListIP": fsCapwapSvrWhiteListIP,
       "fsCapwapSvrWhiteListIPRowStatus": fsCapwapSvrWhiteListIPRowStatus,
       "fsCapwapSvrBlackListURLTable": fsCapwapSvrBlackListURLTable,
       "fsCapwapSvrBlackListURLEntry": fsCapwapSvrBlackListURLEntry,
       "fsCapwapSvrBlackListIndex": fsCapwapSvrBlackListIndex,
       "fsCapwapSvrBlackListURL": fsCapwapSvrBlackListURL,
       "fsCapwapSvrBlackListURLParserStatus": fsCapwapSvrBlackListURLParserStatus,
       "fsCapwapSvrBlackListURLRowStatus": fsCapwapSvrBlackListURLRowStatus,
       "fsCapwapSvrBlackListIPTable": fsCapwapSvrBlackListIPTable,
       "fsCapwapSvrBlackListIPEntry": fsCapwapSvrBlackListIPEntry,
       "fsCapwapSvrBlackListIP": fsCapwapSvrBlackListIP,
       "fsCapwapSvrBlackListIPRowStatus": fsCapwapSvrBlackListIPRowStatus,
       "fsCapwapSvrBlackListPortTable": fsCapwapSvrBlackListPortTable,
       "fsCapwapSvrBlackListPortEntry": fsCapwapSvrBlackListPortEntry,
       "fsCapwapSvrBlackListPort": fsCapwapSvrBlackListPort,
       "fsCapwapSvrBlackListPortRowStatus": fsCapwapSvrBlackListPortRowStatus,
       "fsCapwapSvrWhiteListMacTable": fsCapwapSvrWhiteListMacTable,
       "fsCapwapSvrWhiteListMacEntry": fsCapwapSvrWhiteListMacEntry,
       "fsCapwapSvrWhiteListMacIndex": fsCapwapSvrWhiteListMacIndex,
       "fsCapwapSvrWhiteListMac": fsCapwapSvrWhiteListMac,
       "fsCapwapSvrWhiteListMacRowStatus": fsCapwapSvrWhiteListMacRowStatus,
       "fsCapwapSvrMIBConformance": fsCapwapSvrMIBConformance,
       "fsCapwapSvrMIBCompliances": fsCapwapSvrMIBCompliances,
       "fsCapwapSvrMIBCompliance": fsCapwapSvrMIBCompliance,
       "fsCapwapSvrMIBGroups": fsCapwapSvrMIBGroups,
       "fsCapwapSvrMIBGroup": fsCapwapSvrMIBGroup}
)
