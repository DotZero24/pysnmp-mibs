# SNMP MIB module (NEWTEC-REDUNDANCY-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/newtec/NEWTEC-REDUNDANCY-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 22:04:03 2025
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
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

ntcRedundancy = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 1800)
)
if mibBuilder.loadTexts:
    ntcRedundancy.setRevisions(
        ("2018-01-16 10:00",
         "2013-01-08 12:00",
         "2012-06-28 12:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_NtcRedunObjects_ObjectIdentity = ObjectIdentity
ntcRedunObjects = _NtcRedunObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 1800, 1)
)
if mibBuilder.loadTexts:
    ntcRedunObjects.setStatus("current")


class _NtcRedunEnable_Type(NtcEnable):
    """Custom type ntcRedunEnable based on NtcEnable"""
    defaultValue = 0


_NtcRedunEnable_Type.__name__ = "NtcEnable"
_NtcRedunEnable_Object = MibScalar
ntcRedunEnable = _NtcRedunEnable_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 1800, 1, 1),
    _NtcRedunEnable_Type()
)
ntcRedunEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntcRedunEnable.setStatus("current")


class _NtcRedunInitialState_Type(Integer32):
    """Custom type ntcRedunInitialState based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("standby", 0),
          ("active", 1))
    )


_NtcRedunInitialState_Type.__name__ = "Integer32"
_NtcRedunInitialState_Object = MibScalar
ntcRedunInitialState = _NtcRedunInitialState_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 1800, 1, 2),
    _NtcRedunInitialState_Type()
)
ntcRedunInitialState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntcRedunInitialState.setStatus("current")


class _NtcRedunOperationalState_Type(Integer32):
    """Custom type ntcRedunOperationalState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 0),
          ("standby", 1),
          ("na", 2))
    )


_NtcRedunOperationalState_Type.__name__ = "Integer32"
_NtcRedunOperationalState_Object = MibScalar
ntcRedunOperationalState = _NtcRedunOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 1800, 1, 3),
    _NtcRedunOperationalState_Type()
)
ntcRedunOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcRedunOperationalState.setStatus("current")


class _NtcRedunType_Type(Integer32):
    """Custom type ntcRedunType based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("unit", 0),
          ("carrier", 1))
    )


_NtcRedunType_Type.__name__ = "Integer32"
_NtcRedunType_Object = MibScalar
ntcRedunType = _NtcRedunType_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 1800, 1, 4),
    _NtcRedunType_Type()
)
ntcRedunType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntcRedunType.setStatus("current")
_NtcRedunMonitoringTable_Object = MibTable
ntcRedunMonitoringTable = _NtcRedunMonitoringTable_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 1800, 1, 5)
)
if mibBuilder.loadTexts:
    ntcRedunMonitoringTable.setStatus("current")
_NtcRedunMonitoringEntry_Object = MibTableRow
ntcRedunMonitoringEntry = _NtcRedunMonitoringEntry_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 1800, 1, 5, 1)
)
ntcRedunMonitoringEntry.setIndexNames(
    (0, "NEWTEC-REDUNDANCY-MIB", "ntcRedunMonitoringName"),
)
if mibBuilder.loadTexts:
    ntcRedunMonitoringEntry.setStatus("current")
_NtcRedunMonitoringName_Type = Unsigned32
_NtcRedunMonitoringName_Object = MibTableColumn
ntcRedunMonitoringName = _NtcRedunMonitoringName_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 1800, 1, 5, 1, 1),
    _NtcRedunMonitoringName_Type()
)
ntcRedunMonitoringName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ntcRedunMonitoringName.setStatus("current")


class _NtcRedunCarrType_Type(DisplayString):
    """Custom type ntcRedunCarrType based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_NtcRedunCarrType_Type.__name__ = "DisplayString"
_NtcRedunCarrType_Object = MibTableColumn
ntcRedunCarrType = _NtcRedunCarrType_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 1800, 1, 5, 1, 2),
    _NtcRedunCarrType_Type()
)
ntcRedunCarrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcRedunCarrType.setStatus("current")


class _NtcRedunCarrName_Type(DisplayString):
    """Custom type ntcRedunCarrName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_NtcRedunCarrName_Type.__name__ = "DisplayString"
_NtcRedunCarrName_Object = MibTableColumn
ntcRedunCarrName = _NtcRedunCarrName_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 1800, 1, 5, 1, 3),
    _NtcRedunCarrName_Type()
)
ntcRedunCarrName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcRedunCarrName.setStatus("current")


class _NtcRedunOpState_Type(Integer32):
    """Custom type ntcRedunOpState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 0),
          ("standby", 1),
          ("na", 2))
    )


_NtcRedunOpState_Type.__name__ = "Integer32"
_NtcRedunOpState_Object = MibTableColumn
ntcRedunOpState = _NtcRedunOpState_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 1800, 1, 5, 1, 4),
    _NtcRedunOpState_Type()
)
ntcRedunOpState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcRedunOpState.setStatus("current")
_NtcRedunConformance_ObjectIdentity = ObjectIdentity
ntcRedunConformance = _NtcRedunConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 1800, 2)
)
if mibBuilder.loadTexts:
    ntcRedunConformance.setStatus("current")
_NtcRedunConfCompliance_ObjectIdentity = ObjectIdentity
ntcRedunConfCompliance = _NtcRedunConfCompliance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 1800, 2, 1)
)
if mibBuilder.loadTexts:
    ntcRedunConfCompliance.setStatus("current")
_NtcRedunConfGroup_ObjectIdentity = ObjectIdentity
ntcRedunConfGroup = _NtcRedunConfGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 1800, 2, 2)
)
if mibBuilder.loadTexts:
    ntcRedunConfGroup.setStatus("current")

# Managed Objects groups

ntcRedunConfGrpV1Standard = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 1800, 2, 2, 1)
)
ntcRedunConfGrpV1Standard.setObjects(
      *(("NEWTEC-REDUNDANCY-MIB", "ntcRedunEnable"),
        ("NEWTEC-REDUNDANCY-MIB", "ntcRedunInitialState"),
        ("NEWTEC-REDUNDANCY-MIB", "ntcRedunOperationalState"),
        ("NEWTEC-REDUNDANCY-MIB", "ntcRedunType"),
        ("NEWTEC-REDUNDANCY-MIB", "ntcRedunCarrType"),
        ("NEWTEC-REDUNDANCY-MIB", "ntcRedunCarrName"),
        ("NEWTEC-REDUNDANCY-MIB", "ntcRedunOpState"))
)
if mibBuilder.loadTexts:
    ntcRedunConfGrpV1Standard.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ntcRedunConfCompV1Standard = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 1800, 2, 1, 1)
)
ntcRedunConfCompV1Standard.setObjects(
    ("NEWTEC-REDUNDANCY-MIB", "ntcRedunConfGrpV1Standard")
)
if mibBuilder.loadTexts:
    ntcRedunConfCompV1Standard.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NEWTEC-REDUNDANCY-MIB",
    **{"ntcRedundancy": ntcRedundancy,
       "ntcRedunObjects": ntcRedunObjects,
       "ntcRedunEnable": ntcRedunEnable,
       "ntcRedunInitialState": ntcRedunInitialState,
       "ntcRedunOperationalState": ntcRedunOperationalState,
       "ntcRedunType": ntcRedunType,
       "ntcRedunMonitoringTable": ntcRedunMonitoringTable,
       "ntcRedunMonitoringEntry": ntcRedunMonitoringEntry,
       "ntcRedunMonitoringName": ntcRedunMonitoringName,
       "ntcRedunCarrType": ntcRedunCarrType,
       "ntcRedunCarrName": ntcRedunCarrName,
       "ntcRedunOpState": ntcRedunOpState,
       "ntcRedunConformance": ntcRedunConformance,
       "ntcRedunConfCompliance": ntcRedunConfCompliance,
       "ntcRedunConfCompV1Standard": ntcRedunConfCompV1Standard,
       "ntcRedunConfGroup": ntcRedunConfGroup,
       "ntcRedunConfGrpV1Standard": ntcRedunConfGrpV1Standard}
)
