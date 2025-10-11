# SNMP MIB module (NEWTEC-MPEENCAPS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/newtec/NEWTEC-MPEENCAPS-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 22:04:11 2025
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

(ntcFunction,) = mibBuilder.importSymbols(
    "NEWTEC-MAIN-MIB",
    "ntcFunction")

(NtcEnable,) = mibBuilder.importSymbols(
    "NEWTEC-TC-MIB",
    "NtcEnable")

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

ntcMpeEncaps = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 1900)
)
if mibBuilder.loadTexts:
    ntcMpeEncaps.setRevisions(
        ("2017-07-10 12:00",
         "2013-03-27 10:00",
         "2012-06-28 12:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_NtcMpeEncObjects_ObjectIdentity = ObjectIdentity
ntcMpeEncObjects = _NtcMpeEncObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 1900, 1)
)
if mibBuilder.loadTexts:
    ntcMpeEncObjects.setStatus("current")


class _NtcMpeEncEnable_Type(NtcEnable):
    """Custom type ntcMpeEncEnable based on NtcEnable"""
    defaultValue = 0


_NtcMpeEncEnable_Type.__name__ = "NtcEnable"
_NtcMpeEncEnable_Object = MibScalar
ntcMpeEncEnable = _NtcMpeEncEnable_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 1900, 1, 1),
    _NtcMpeEncEnable_Type()
)
ntcMpeEncEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntcMpeEncEnable.setStatus("current")


class _NtcMpeEncDataPid_Type(Unsigned32):
    """Custom type ntcMpeEncDataPid based on Unsigned32"""
    defaultValue = 3000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(32, 8190),
    )


_NtcMpeEncDataPid_Type.__name__ = "Unsigned32"
_NtcMpeEncDataPid_Object = MibScalar
ntcMpeEncDataPid = _NtcMpeEncDataPid_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 1900, 1, 2),
    _NtcMpeEncDataPid_Type()
)
ntcMpeEncDataPid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntcMpeEncDataPid.setStatus("current")


class _NtcMpeEncSignEnable_Type(NtcEnable):
    """Custom type ntcMpeEncSignEnable based on NtcEnable"""
    defaultValue = 0


_NtcMpeEncSignEnable_Type.__name__ = "NtcEnable"
_NtcMpeEncSignEnable_Object = MibScalar
ntcMpeEncSignEnable = _NtcMpeEncSignEnable_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 1900, 1, 3),
    _NtcMpeEncSignEnable_Type()
)
ntcMpeEncSignEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntcMpeEncSignEnable.setStatus("current")


class _NtcMpeEncSignProgramNumber_Type(Unsigned32):
    """Custom type ntcMpeEncSignProgramNumber based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_NtcMpeEncSignProgramNumber_Type.__name__ = "Unsigned32"
_NtcMpeEncSignProgramNumber_Object = MibScalar
ntcMpeEncSignProgramNumber = _NtcMpeEncSignProgramNumber_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 1900, 1, 4),
    _NtcMpeEncSignProgramNumber_Type()
)
ntcMpeEncSignProgramNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntcMpeEncSignProgramNumber.setStatus("current")


class _NtcMpeEncSignPmtPid_Type(Unsigned32):
    """Custom type ntcMpeEncSignPmtPid based on Unsigned32"""
    defaultValue = 4000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(32, 8190),
    )


_NtcMpeEncSignPmtPid_Type.__name__ = "Unsigned32"
_NtcMpeEncSignPmtPid_Object = MibScalar
ntcMpeEncSignPmtPid = _NtcMpeEncSignPmtPid_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 1900, 1, 5),
    _NtcMpeEncSignPmtPid_Type()
)
ntcMpeEncSignPmtPid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntcMpeEncSignPmtPid.setStatus("current")
_NtcMpeEncChannelsTable_Object = MibTable
ntcMpeEncChannelsTable = _NtcMpeEncChannelsTable_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 1900, 1, 6)
)
if mibBuilder.loadTexts:
    ntcMpeEncChannelsTable.setStatus("current")
_NtcMpeEncChannelsEntry_Object = MibTableRow
ntcMpeEncChannelsEntry = _NtcMpeEncChannelsEntry_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 1900, 1, 6, 1)
)
ntcMpeEncChannelsEntry.setIndexNames(
    (0, "NEWTEC-MPEENCAPS-MIB", "ntcMpeEncChannelsInx"),
)
if mibBuilder.loadTexts:
    ntcMpeEncChannelsEntry.setStatus("current")
_NtcMpeEncChannelsInx_Type = Unsigned32
_NtcMpeEncChannelsInx_Object = MibTableColumn
ntcMpeEncChannelsInx = _NtcMpeEncChannelsInx_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 1900, 1, 6, 1, 1),
    _NtcMpeEncChannelsInx_Type()
)
ntcMpeEncChannelsInx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ntcMpeEncChannelsInx.setStatus("current")


class _NtcMpeChanName_Type(DisplayString):
    """Custom type ntcMpeChanName based on DisplayString"""
    defaultValue = OctetString("")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 100),
    )


_NtcMpeChanName_Type.__name__ = "DisplayString"
_NtcMpeChanName_Object = MibTableColumn
ntcMpeChanName = _NtcMpeChanName_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 1900, 1, 6, 1, 2),
    _NtcMpeChanName_Type()
)
ntcMpeChanName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntcMpeChanName.setStatus("current")


class _NtcMpeChanEnable_Type(NtcEnable):
    """Custom type ntcMpeChanEnable based on NtcEnable"""
    defaultValue = 0


_NtcMpeChanEnable_Type.__name__ = "NtcEnable"
_NtcMpeChanEnable_Object = MibTableColumn
ntcMpeChanEnable = _NtcMpeChanEnable_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 1900, 1, 6, 1, 3),
    _NtcMpeChanEnable_Type()
)
ntcMpeChanEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntcMpeChanEnable.setStatus("current")
_NtcMpeChanMacAddr_Type = MacAddress
_NtcMpeChanMacAddr_Object = MibTableColumn
ntcMpeChanMacAddr = _NtcMpeChanMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 1900, 1, 6, 1, 4),
    _NtcMpeChanMacAddr_Type()
)
ntcMpeChanMacAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntcMpeChanMacAddr.setStatus("current")
_NtcMpeEncConformance_ObjectIdentity = ObjectIdentity
ntcMpeEncConformance = _NtcMpeEncConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 1900, 2)
)
if mibBuilder.loadTexts:
    ntcMpeEncConformance.setStatus("current")
_NtcMpeEncConfCompliance_ObjectIdentity = ObjectIdentity
ntcMpeEncConfCompliance = _NtcMpeEncConfCompliance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 1900, 2, 1)
)
if mibBuilder.loadTexts:
    ntcMpeEncConfCompliance.setStatus("current")
_NtcMpeEncConfGroup_ObjectIdentity = ObjectIdentity
ntcMpeEncConfGroup = _NtcMpeEncConfGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 1900, 2, 2)
)
if mibBuilder.loadTexts:
    ntcMpeEncConfGroup.setStatus("current")

# Managed Objects groups

ntcMpeEncConfGrpV1Standard = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 1900, 2, 2, 1)
)
ntcMpeEncConfGrpV1Standard.setObjects(
      *(("NEWTEC-MPEENCAPS-MIB", "ntcMpeEncEnable"),
        ("NEWTEC-MPEENCAPS-MIB", "ntcMpeEncDataPid"),
        ("NEWTEC-MPEENCAPS-MIB", "ntcMpeEncSignEnable"),
        ("NEWTEC-MPEENCAPS-MIB", "ntcMpeEncSignProgramNumber"),
        ("NEWTEC-MPEENCAPS-MIB", "ntcMpeEncSignPmtPid"),
        ("NEWTEC-MPEENCAPS-MIB", "ntcMpeChanName"),
        ("NEWTEC-MPEENCAPS-MIB", "ntcMpeChanEnable"),
        ("NEWTEC-MPEENCAPS-MIB", "ntcMpeChanMacAddr"))
)
if mibBuilder.loadTexts:
    ntcMpeEncConfGrpV1Standard.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ntcMpeEncConfCompV1Standard = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 1900, 2, 1, 1)
)
ntcMpeEncConfCompV1Standard.setObjects(
    ("NEWTEC-MPEENCAPS-MIB", "ntcMpeEncConfGrpV1Standard")
)
if mibBuilder.loadTexts:
    ntcMpeEncConfCompV1Standard.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NEWTEC-MPEENCAPS-MIB",
    **{"ntcMpeEncaps": ntcMpeEncaps,
       "ntcMpeEncObjects": ntcMpeEncObjects,
       "ntcMpeEncEnable": ntcMpeEncEnable,
       "ntcMpeEncDataPid": ntcMpeEncDataPid,
       "ntcMpeEncSignEnable": ntcMpeEncSignEnable,
       "ntcMpeEncSignProgramNumber": ntcMpeEncSignProgramNumber,
       "ntcMpeEncSignPmtPid": ntcMpeEncSignPmtPid,
       "ntcMpeEncChannelsTable": ntcMpeEncChannelsTable,
       "ntcMpeEncChannelsEntry": ntcMpeEncChannelsEntry,
       "ntcMpeEncChannelsInx": ntcMpeEncChannelsInx,
       "ntcMpeChanName": ntcMpeChanName,
       "ntcMpeChanEnable": ntcMpeChanEnable,
       "ntcMpeChanMacAddr": ntcMpeChanMacAddr,
       "ntcMpeEncConformance": ntcMpeEncConformance,
       "ntcMpeEncConfCompliance": ntcMpeEncConfCompliance,
       "ntcMpeEncConfCompV1Standard": ntcMpeEncConfCompV1Standard,
       "ntcMpeEncConfGroup": ntcMpeEncConfGroup,
       "ntcMpeEncConfGrpV1Standard": ntcMpeEncConfGrpV1Standard}
)
