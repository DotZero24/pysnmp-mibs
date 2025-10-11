# SNMP MIB module (FS-VSF-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/fscom/FS-VSF-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:15:22 2025
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

fsVsfMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 140)
)
if mibBuilder.loadTexts:
    fsVsfMIB.setRevisions(
        ("2015-06-01 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_FsVsfMIBObjects_ObjectIdentity = ObjectIdentity
fsVsfMIBObjects = _FsVsfMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 140, 1)
)
_FsVsfDeviceInfo_ObjectIdentity = ObjectIdentity
fsVsfDeviceInfo = _FsVsfDeviceInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 140, 1, 1)
)
_FsVsfDeviceTable_Object = MibTable
fsVsfDeviceTable = _FsVsfDeviceTable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 140, 1, 1, 1)
)
if mibBuilder.loadTexts:
    fsVsfDeviceTable.setStatus("current")
_FsVsfDeviceEntry_Object = MibTableRow
fsVsfDeviceEntry = _FsVsfDeviceEntry_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 140, 1, 1, 1, 1)
)
fsVsfDeviceEntry.setIndexNames(
    (0, "FS-VSF-MIB", "fsVsfDeviceID"),
)
if mibBuilder.loadTexts:
    fsVsfDeviceEntry.setStatus("current")
_FsVsfDeviceID_Type = Integer32
_FsVsfDeviceID_Object = MibTableColumn
fsVsfDeviceID = _FsVsfDeviceID_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 140, 1, 1, 1, 1, 1),
    _FsVsfDeviceID_Type()
)
fsVsfDeviceID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsVsfDeviceID.setStatus("current")
_FsVsfDeviceMac_Type = MacAddress
_FsVsfDeviceMac_Object = MibTableColumn
fsVsfDeviceMac = _FsVsfDeviceMac_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 140, 1, 1, 1, 1, 2),
    _FsVsfDeviceMac_Type()
)
fsVsfDeviceMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsVsfDeviceMac.setStatus("current")
_FsVsfDeviceDescr_Type = DisplayString
_FsVsfDeviceDescr_Object = MibTableColumn
fsVsfDeviceDescr = _FsVsfDeviceDescr_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 140, 1, 1, 1, 1, 3),
    _FsVsfDeviceDescr_Type()
)
fsVsfDeviceDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsVsfDeviceDescr.setStatus("current")


class _FsVsfDeviceStatus_Type(Integer32):
    """Custom type fsVsfDeviceStatus based on Integer32"""
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


_FsVsfDeviceStatus_Type.__name__ = "Integer32"
_FsVsfDeviceStatus_Object = MibTableColumn
fsVsfDeviceStatus = _FsVsfDeviceStatus_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 140, 1, 1, 1, 1, 4),
    _FsVsfDeviceStatus_Type()
)
fsVsfDeviceStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsVsfDeviceStatus.setStatus("current")
_FsVsf_ObjectIdentity = ObjectIdentity
fsVsf = _FsVsf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 140, 1, 2)
)
_FsVsfPortTable_Object = MibTable
fsVsfPortTable = _FsVsfPortTable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 140, 1, 2, 1)
)
if mibBuilder.loadTexts:
    fsVsfPortTable.setStatus("current")
_FsVsfPortEntry_Object = MibTableRow
fsVsfPortEntry = _FsVsfPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 140, 1, 2, 1, 1)
)
fsVsfPortEntry.setIndexNames(
    (0, "FS-VSF-MIB", "fsVsfPortIfIndex"),
)
if mibBuilder.loadTexts:
    fsVsfPortEntry.setStatus("current")
_FsVsfPortIfIndex_Type = Integer32
_FsVsfPortIfIndex_Object = MibTableColumn
fsVsfPortIfIndex = _FsVsfPortIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 140, 1, 2, 1, 1, 1),
    _FsVsfPortIfIndex_Type()
)
fsVsfPortIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsVsfPortIfIndex.setStatus("current")
_FsVsfApIf_Type = DisplayString
_FsVsfApIf_Object = MibTableColumn
fsVsfApIf = _FsVsfApIf_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 140, 1, 2, 1, 1, 2),
    _FsVsfApIf_Type()
)
fsVsfApIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsVsfApIf.setStatus("current")


class _FsVsfPortState_Type(Integer32):
    """Custom type fsVsfPortState based on Integer32"""
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


_FsVsfPortState_Type.__name__ = "Integer32"
_FsVsfPortState_Object = MibTableColumn
fsVsfPortState = _FsVsfPortState_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 140, 1, 2, 1, 1, 3),
    _FsVsfPortState_Type()
)
fsVsfPortState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsVsfPortState.setStatus("current")
_FsVsfPortPeerIfIndex_Type = Integer32
_FsVsfPortPeerIfIndex_Object = MibTableColumn
fsVsfPortPeerIfIndex = _FsVsfPortPeerIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 140, 1, 2, 1, 1, 4),
    _FsVsfPortPeerIfIndex_Type()
)
fsVsfPortPeerIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsVsfPortPeerIfIndex.setStatus("current")
_FsVsfApTable_Object = MibTable
fsVsfApTable = _FsVsfApTable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 140, 1, 2, 2)
)
if mibBuilder.loadTexts:
    fsVsfApTable.setStatus("current")
_FsVsfApEntry_Object = MibTableRow
fsVsfApEntry = _FsVsfApEntry_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 140, 1, 2, 2, 1)
)
fsVsfApEntry.setIndexNames(
    (0, "FS-VSF-MIB", "fsVsfApIndex"),
)
if mibBuilder.loadTexts:
    fsVsfApEntry.setStatus("current")
_FsVsfApIndex_Type = Integer32
_FsVsfApIndex_Object = MibTableColumn
fsVsfApIndex = _FsVsfApIndex_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 140, 1, 2, 2, 1, 1),
    _FsVsfApIndex_Type()
)
fsVsfApIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsVsfApIndex.setStatus("current")
_FsVsfApUptime_Type = DisplayString
_FsVsfApUptime_Object = MibTableColumn
fsVsfApUptime = _FsVsfApUptime_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 140, 1, 2, 2, 1, 2),
    _FsVsfApUptime_Type()
)
fsVsfApUptime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsVsfApUptime.setStatus("current")
_FsVsfMIBConformance_ObjectIdentity = ObjectIdentity
fsVsfMIBConformance = _FsVsfMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 140, 3)
)
_FsVsfMIBCompliances_ObjectIdentity = ObjectIdentity
fsVsfMIBCompliances = _FsVsfMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 140, 3, 1)
)
_FsVsfMIBGroups_ObjectIdentity = ObjectIdentity
fsVsfMIBGroups = _FsVsfMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 140, 3, 2)
)

# Managed Objects groups

fsVsfMIBObjectsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 140, 3, 2, 1)
)
fsVsfMIBObjectsGroup.setObjects(
      *(("FS-VSF-MIB", "fsVsfDeviceID"),
        ("FS-VSF-MIB", "fsVsfDeviceMac"),
        ("FS-VSF-MIB", "fsVsfDeviceDescr"),
        ("FS-VSF-MIB", "fsVsfDeviceStatus"),
        ("FS-VSF-MIB", "fsVsfPortIfIndex"),
        ("FS-VSF-MIB", "fsVsfApIf"),
        ("FS-VSF-MIB", "fsVsfPortState"),
        ("FS-VSF-MIB", "fsVsfPortPeerIfIndex"),
        ("FS-VSF-MIB", "fsVsfApIndex"),
        ("FS-VSF-MIB", "fsVsfApUptime"))
)
if mibBuilder.loadTexts:
    fsVsfMIBObjectsGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

fsVsfMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 140, 3, 1, 1)
)
fsVsfMIBCompliance.setObjects(
    ("FS-VSF-MIB", "fsVsfMIBObjectsGroup")
)
if mibBuilder.loadTexts:
    fsVsfMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "FS-VSF-MIB",
    **{"fsVsfMIB": fsVsfMIB,
       "fsVsfMIBObjects": fsVsfMIBObjects,
       "fsVsfDeviceInfo": fsVsfDeviceInfo,
       "fsVsfDeviceTable": fsVsfDeviceTable,
       "fsVsfDeviceEntry": fsVsfDeviceEntry,
       "fsVsfDeviceID": fsVsfDeviceID,
       "fsVsfDeviceMac": fsVsfDeviceMac,
       "fsVsfDeviceDescr": fsVsfDeviceDescr,
       "fsVsfDeviceStatus": fsVsfDeviceStatus,
       "fsVsf": fsVsf,
       "fsVsfPortTable": fsVsfPortTable,
       "fsVsfPortEntry": fsVsfPortEntry,
       "fsVsfPortIfIndex": fsVsfPortIfIndex,
       "fsVsfApIf": fsVsfApIf,
       "fsVsfPortState": fsVsfPortState,
       "fsVsfPortPeerIfIndex": fsVsfPortPeerIfIndex,
       "fsVsfApTable": fsVsfApTable,
       "fsVsfApEntry": fsVsfApEntry,
       "fsVsfApIndex": fsVsfApIndex,
       "fsVsfApUptime": fsVsfApUptime,
       "fsVsfMIBConformance": fsVsfMIBConformance,
       "fsVsfMIBCompliances": fsVsfMIBCompliances,
       "fsVsfMIBCompliance": fsVsfMIBCompliance,
       "fsVsfMIBGroups": fsVsfMIBGroups,
       "fsVsfMIBObjectsGroup": fsVsfMIBObjectsGroup}
)
